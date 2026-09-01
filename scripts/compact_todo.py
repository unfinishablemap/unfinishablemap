#!/usr/bin/env python
"""One-off repair: re-file completed tasks that were mis-inserted into the
wrong sections of todo.md, so the weekly archiver can sweep them.

Background
----------
`complete_task` builds its insertion point by scanning forward from
`## Completed Tasks` for the next `### ` header. Until 2026-09-01 that scan had
no `## ` section-boundary check, so whenever Completed Tasks was empty — its
state immediately after every archive sweep — the scan ran past the section end
and filed the entry under the following heading, `## Blocked Tasks`.

`archive_completed_tasks` only reads the Completed section, so it found nothing,
returned {} and archived nothing. The two faults concealed each other from
~2026-05 (ISO week 20) and todo.md grew to 12.7 MB / 22.5k lines, re-parsed on
every cycle.

The code fault is fixed in tools/todo/processor.py. This script repairs the
accumulated data: it moves `### ✓` / `### ✅` blocks out of Active Tasks and
Blocked Tasks into Completed Tasks, where `scripts/archive_workflow.py` can
then sweep them into weekly files.

Scope
-----
- Moves ONLY completion-marked blocks (`### ✓`, `### ✅`).
- Normalises `✅` to `✓`, because the archiver's split pattern is `^### ✓` and
  would otherwise skip those entries forever.
- Leaves genuinely blocked entries (NEEDS-HUMAN, HUMAN, BLOCKED, P0-P3) in
  place, and leaves the Vetoed Tasks section untouched — vetoed-and-done is a
  different state from completed.

Dry run by default. Pass --apply to write, which first saves a .bak alongside.

    uv run python scripts/compact_todo.py
    uv run python scripts/compact_todo.py --apply
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT))

import frontmatter  # noqa: E402

TODO_PATH = REPO_ROOT / "obsidian" / "workflow" / "todo.md"

# Sections we lift completed blocks OUT of.
SOURCE_SECTIONS = ("## Active Tasks", "## Blocked Tasks")
TARGET_SECTION = "## Completed Tasks"

COMPLETED_HEADER = re.compile(r"^###\s*[✓✅]\s*", re.UNICODE)
DATE_IN_HEADER = re.compile(r"(\d{4}-\d{2}-\d{2})")


def split_sections(lines: list[str]) -> list[tuple[str, list[str]]]:
    """Split body lines into (heading, lines-including-heading) sections.

    Content before the first '## ' heading is returned under heading ''.
    """
    sections: list[tuple[str, list[str]]] = []
    current_heading = ""
    current: list[str] = []
    for line in lines:
        if line.startswith("## "):
            sections.append((current_heading, current))
            current_heading = line
            current = [line]
        else:
            current.append(line)
    sections.append((current_heading, current))
    return sections


def extract_completed_blocks(
    section_lines: list[str],
) -> tuple[list[str], list[list[str]]]:
    """Split a section into (kept lines, completed blocks).

    A block runs from its '### ' header to the line before the next '### '
    or '## '.
    """
    kept: list[str] = []
    blocks: list[list[str]] = []
    i = 0
    n = len(section_lines)
    while i < n:
        line = section_lines[i]
        if line.startswith("### "):
            end = i + 1
            while end < n and not (
                section_lines[end].startswith("### ")
                or section_lines[end].startswith("## ")
            ):
                end += 1
            block = section_lines[i:end]
            while block and block[-1].strip() == "":
                block.pop()
            if COMPLETED_HEADER.match(line):
                blocks.append(block)
            else:
                kept.extend(block)
                kept.append("")
            i = end
        else:
            kept.append(line)
            i += 1
    while kept and kept[-1].strip() == "":
        kept.pop()
    kept.append("")
    return kept, blocks


def block_sort_key(block: list[str]) -> str:
    m = DATE_IN_HEADER.search(block[0])
    return m.group(1) if m else "0000-00-00"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--path", type=Path, default=TODO_PATH)
    args = ap.parse_args()

    post = frontmatter.load(args.path)
    lines = post.content.split("\n")
    original_header_count = sum(1 for ln in lines if ln.startswith("### "))

    sections = split_sections(lines)
    moved: list[list[str]] = []
    rebuilt: list[tuple[str, list[str]]] = []

    for heading, body in sections:
        if any(heading.startswith(s) for s in SOURCE_SECTIONS):
            kept, blocks = extract_completed_blocks(body)
            moved.extend(blocks)
            print(f"  {heading.strip():34} -> lifted {len(blocks):5} completed blocks")
            rebuilt.append((heading, kept))
        else:
            rebuilt.append((heading, body))

    if not moved:
        print("\nNothing to compact — no misfiled completed blocks found.")
        return 0

    # Normalise ✅ -> ✓ so the archiver's `^### ✓` split matches, and order
    # newest-first to match the Completed section convention.
    normalised = 0
    for block in moved:
        if "✅" in block[0]:
            block[0] = block[0].replace("✅", "✓")
            normalised += 1
    moved.sort(key=block_sort_key, reverse=True)

    out: list[str] = []
    for heading, body in rebuilt:
        if heading.startswith(TARGET_SECTION):
            out.append(heading)
            out.append("")
            for block in moved:
                out.extend(block)
                out.append("")
            # Preserve anything already in Completed (normally nothing).
            tail = [ln for ln in body[1:] if ln.strip()]
            if tail:
                out.extend(tail)
                out.append("")
        else:
            out.extend(body)

    new_content = "\n".join(out)
    new_header_count = sum(1 for ln in new_content.split("\n") if ln.startswith("### "))

    print(f"\n  moved            : {len(moved)}")
    print(f"  ✅ normalised to ✓: {normalised}")
    print(f"  '### ' headers    : {original_header_count} -> {new_header_count}")
    undated = sum(1 for b in moved if block_sort_key(b) == "0000-00-00")
    print(f"  without a parseable date (archiver will retain these): {undated}")

    if new_header_count != original_header_count:
        print("\nABORT: header count changed — blocks would be lost.", file=sys.stderr)
        return 1

    size_before = args.path.stat().st_size
    if not args.apply:
        print(f"\nDRY RUN — {args.path} unchanged ({size_before:,} bytes).")
        print("Re-run with --apply to write.")
        return 0

    backup = args.path.with_suffix(".md.bak")
    shutil.copy2(args.path, backup)
    post.content = new_content
    args.path.write_text(frontmatter.dumps(post), encoding="utf-8")
    print(f"\n  backup : {backup}")
    print(f"  written: {args.path} ({size_before:,} -> {args.path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
