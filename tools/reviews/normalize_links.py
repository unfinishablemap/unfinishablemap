"""Normalize boilerplate display text on links to unfinishablemap.org.

External reviewers (ChatGPT Deep Research, Claude Research, Gemini Deep
Research) emit citation-style anchor text like ``[The Unfinishable Map]``,
``[unfinishablemap]``, ``[The Unfinishable Map+2]``, or
``[unfinishablemap.orgTopics | The Unfinishable Map Opens in a new window]``.
That text carries no information beyond the URL itself.

This module rewrites the display text of any markdown link pointing at
``https://unfinishablemap.org/<path>/`` to the URL path
(``concepts/interactionist-dualism``) when the existing text is boilerplate.
Natural-prose anchors like ``[explanatory gap]`` are preserved because they
do not mention the site by name.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_LINK_RE = re.compile(
    r"\[(?P<text>[^\]]*)\]\((?P<url>https://unfinishablemap\.org/[^)\s]*)\)"
)

_BOILERPLATE_RE = re.compile(r"unfinishable\s*map", re.IGNORECASE)


def _url_to_path(url: str) -> str:
    """``https://unfinishablemap.org/concepts/x/`` → ``concepts/x``.

    Leading/trailing slashes are stripped. Empty path (site root) returns ''.
    """
    path = url[len("https://unfinishablemap.org") :]
    return path.strip("/")


def _is_boilerplate(text: str) -> bool:
    """True if the link text is uninformative reviewer-citation noise.

    Matches both spaceless (``unfinishablemap``) and spaced
    (``The Unfinishable Map``) forms, plus the citation-suffix variants
    (``…+2``, ``…Opens in a new window``) and Gemini's concatenations.
    """
    return _BOILERPLATE_RE.search(text) is not None


def normalize(content: str) -> tuple[str, int]:
    """Rewrite boilerplate ``unfinishablemap.org`` link text to URL paths.

    Returns ``(new_content, replacements_made)``. Idempotent: a second call on
    the result produces no further changes.
    """
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        text = match.group("text")
        url = match.group("url")
        if not _is_boilerplate(text):
            return match.group(0)
        path = _url_to_path(url)
        if not path:
            # Site root — leave the original text alone; "unfinishablemap"
            # is the most informative description we have for the root URL.
            return match.group(0)
        if text == path:
            return match.group(0)
        count += 1
        return f"[{path}]({url})"

    new = _LINK_RE.sub(repl, content)
    return new, count


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+", type=Path,
                    help="Markdown files to normalize in place.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Report replacements without modifying files.")
    args = ap.parse_args()

    total = 0
    changed = 0
    for path in args.paths:
        if not path.is_file():
            print(f"skip (not a file): {path}", file=sys.stderr)
            continue
        original = path.read_text(encoding="utf-8")
        new, count = normalize(original)
        total += count
        if count:
            changed += 1
            if args.dry_run:
                print(f"{path}: {count} replacement(s) [dry-run]")
            else:
                path.write_text(new, encoding="utf-8")
                print(f"{path}: {count} replacement(s)")

    suffix = " [dry-run]" if args.dry_run else ""
    print(f"\nTotal: {total} replacement(s) across {changed} file(s){suffix}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
