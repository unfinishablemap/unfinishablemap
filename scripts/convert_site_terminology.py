#!/usr/bin/env python3
"""Convert 'this site' / 'the site' terminology to 'The Unfinishable Map' / 'The Map'.

First mention in each file becomes 'The Unfinishable Map', subsequent mentions become 'The Map'.
"""

import re
import sys
from pathlib import Path

# Patterns to match (case-insensitive for detection, but we preserve/fix case in output)
PATTERNS = [
    (r"\bThis site\b", "this_site"),
    (r"\bthis site\b", "this_site"),
    (r"\bThe site\b", "the_site"),
    (r"\bthe site\b", "the_site"),
    (r"\bthe site's\b", "the_site_possessive"),
    (r"\bThe site's\b", "the_site_possessive"),
    (r"\bthis site's\b", "this_site_possessive"),
    (r"\bThis site's\b", "this_site_possessive"),
]


def convert_file(filepath: Path, dry_run: bool = True) -> tuple[bool, list[str]]:
    """Convert a single file. Returns (changed, list of changes)."""
    content = filepath.read_text(encoding="utf-8")
    original = content
    changes = []

    # Track if we've made the first mention yet
    first_mention_made = False

    def replace_match(match: re.Match) -> str:
        nonlocal first_mention_made
        matched_text = match.group(0)

        # Determine if possessive
        is_possessive = matched_text.lower().endswith("'s")

        # Check if at start of sentence (capital T in original)
        starts_with_capital = matched_text[0] == "T"

        if not first_mention_made:
            first_mention_made = True
            replacement = "The Unfinishable Map's" if is_possessive else "The Unfinishable Map"
            changes.append(f"  '{matched_text}' -> '{replacement}' (first mention)")
        else:
            # "The Map" at start of sentence, "the Map" mid-sentence
            if starts_with_capital:
                replacement = "The Map's" if is_possessive else "The Map"
            else:
                replacement = "the Map's" if is_possessive else "the Map"
            changes.append(f"  '{matched_text}' -> '{replacement}'")

        return replacement

    # Combined pattern for all variants
    combined_pattern = r"\b[Tt]h(?:is|e) site(?:'s)?\b"

    content = re.sub(combined_pattern, replace_match, content)

    changed = content != original

    if changed and not dry_run:
        filepath.write_text(content, encoding="utf-8")

    return changed, changes


def main():
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    if dry_run:
        print("DRY RUN - no files will be modified\n")

    # Find all markdown files in obsidian/ and hugo/content/
    base = Path(__file__).parent.parent
    paths = []
    paths.extend((base / "obsidian").rglob("*.md"))
    paths.extend((base / "hugo" / "content").rglob("*.md"))

    # Also check key config files
    for config_file in ["CLAUDE.md", "README.md"]:
        config_path = base / config_file
        if config_path.exists():
            paths.append(config_path)

    # Check .claude/skills
    paths.extend((base / ".claude" / "skills").rglob("*.md"))

    total_changed = 0
    total_replacements = 0

    for filepath in sorted(set(paths)):
        changed, changes = convert_file(filepath, dry_run=dry_run)
        if changed:
            total_changed += 1
            total_replacements += len(changes)
            rel_path = filepath.relative_to(base)
            print(f"{rel_path}: {len(changes)} replacements")
            if verbose:
                for change in changes:
                    print(change)

    print(f"\n{'Would modify' if dry_run else 'Modified'} {total_changed} files")
    print(f"Total replacements: {total_replacements}")

    if dry_run:
        print("\nRun without --dry-run to apply changes")


if __name__ == "__main__":
    main()
