#!/usr/bin/env python
"""Give every position in the register a stable block anchor.

Why
---
Positions are `## P-NN: <claim>` headings, so Hugo derives their anchors from
the slugified claim text. Claims are rewritten constantly (`/positions-evolve`
touched positions/ in 51 commits during August alone), so any deep link to a
position breaks silently the moment its wording changes. That is why only three
block anchors exist across the whole register and why every anchored link in the
corpus points at the single stable target, `^mechanism-debt`.

The result: of 511 position references in the wider corpus, 133 are clickable
and none resolves to an individual position.

This script appends an Obsidian block anchor derived from the position ID -- not
its claim -- to each position's `- **Status**:` line, chosen because it is the
first field line and the one least often rewritten:

    - **Status**: live ^p-q3

tools/sync/wikilinks.py:convert_block_references turns that into
`<span id="p-q3"></span>`, and `[[positions/quantum-interface#^p-q3|P-Q3]]`
resolves to `/positions/quantum-interface/#p-q3`.

Idempotent: re-run after adding positions and only the new ones are touched.
Dry run by default; pass --apply to write.

    uv run python scripts/add_position_anchors.py
    uv run python scripts/add_position_anchors.py --apply
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
POSITIONS_DIR = REPO_ROOT / "obsidian" / "positions"

# positions.md is the index; *-calibration-history.md are audit-trail companions.
def domain_files(root: Path) -> list[Path]:
    return sorted(
        p for p in root.glob("*.md")
        if p.name != "positions.md" and "calibration-history" not in p.name
    )


HEADING = re.compile(r"^## (P-[A-Z]{1,4}\d+):", re.M)
STATUS = re.compile(r"^- \*\*Status\*\*:\s*(.*)$")
TRAILING_ANCHOR = re.compile(r"\s+\^[A-Za-z0-9-]+\s*$")


def process(text: str) -> tuple[str, list[str], list[str]]:
    """Return (new_text, added_ids, already_present_ids)."""
    lines = text.split("\n")
    added: list[str] = []
    present: list[str] = []
    current: str | None = None

    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m:
            current = m.group(1)
            continue
        if current is None:
            continue
        sm = STATUS.match(line)
        if not sm:
            continue

        anchor = current.lower()
        existing = TRAILING_ANCHOR.search(line)
        if existing:
            if existing.group(0).strip() == f"^{anchor}":
                present.append(current)
            else:
                # A different anchor already claims this line -- leave it alone
                # and report, rather than clobbering a hand-placed target.
                present.append(f"{current}(has {existing.group(0).strip()})")
        else:
            lines[i] = line.rstrip() + f" ^{anchor}"
            added.append(current)
        current = None  # only the first Status line after a heading

    return "\n".join(lines), added, present


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--dir", type=Path, default=POSITIONS_DIR)
    args = ap.parse_args()

    files = domain_files(args.dir)
    if not files:
        print(f"no domain files under {args.dir}", file=sys.stderr)
        return 1

    total_added = total_present = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        new_text, added, present = process(text)
        total_added += len(added)
        total_present += len(present)
        if added or present:
            note = f"+{len(added)}" if added else "  ."
            skip = f"  ({len(present)} already anchored)" if present else ""
            print(f"  {note:>4}  {path.name:38}{skip}")
            if added:
                print(f"        {' '.join(added)}")
        if added and args.apply:
            path.write_text(new_text, encoding="utf-8")

    print(f"\n  anchors to add : {total_added}")
    print(f"  already present: {total_present}")
    if not args.apply:
        print("\nDRY RUN — nothing written. Re-run with --apply.")
    else:
        print("\nWritten.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
