#!/usr/bin/env python3
"""Fix changelog timestamps by cross-referencing git history.

The evolution loop skills were writing incorrect timestamps because Claude
didn't know the actual current time. This script corrects timestamps by
matching changelog entries to their actual git commit times.
"""

import argparse
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import frontmatter


def get_git_log_entries(repo_root: Path, file_path: Path) -> list[dict]:
    """Get git log for a file with commit timestamps and added lines.

    Returns list of dicts with 'commit', 'timestamp', 'added_lines'.
    """
    result = subprocess.run(
        [
            "git", "log",
            "--format=%H|%ci",  # commit hash and ISO timestamp
            "-p",  # include diff
            "--reverse",  # oldest first for easier processing
            "--", str(file_path)
        ],
        capture_output=True,
        text=True,
        cwd=repo_root,
    )

    if result.returncode != 0:
        raise RuntimeError(f"git log failed: {result.stderr}")

    entries = []
    current_commit = None
    current_timestamp = None
    added_lines = []

    for line in result.stdout.split("\n"):
        # Check for new commit
        if "|" in line and len(line.split("|")[0]) == 40:
            # Save previous commit if exists
            if current_commit:
                entries.append({
                    "commit": current_commit,
                    "timestamp": current_timestamp,
                    "added_lines": added_lines,
                })

            parts = line.split("|", 1)
            current_commit = parts[0]
            # Parse timestamp like "2026-01-29 19:04:24 +0000"
            ts_str = parts[1].strip()
            current_timestamp = datetime.strptime(
                ts_str, "%Y-%m-%d %H:%M:%S %z"
            )
            added_lines = []
        elif line.startswith("+") and not line.startswith("+++"):
            # This is an added line in the diff
            added_lines.append(line[1:])  # Remove the + prefix

    # Don't forget the last commit
    if current_commit:
        entries.append({
            "commit": current_commit,
            "timestamp": current_timestamp,
            "added_lines": added_lines,
        })

    return entries


def find_entry_headers_in_commit(added_lines: list[str]) -> list[tuple[str, str]]:
    """Find changelog entry headers in added lines.

    Handles two formats:
    - New: "## 2026-01-29 21:15 UTC - deep-review"
    - Old: "### 23:10 - cross-review" (needs date context from ## header)

    Returns list of (header_line, combined_signature) tuples.
    """
    results = []
    current_date = None

    for line in added_lines:
        # Check for date-only header (old format)
        date_match = re.match(r"^## (\d{4}-\d{2}-\d{2})$", line)
        if date_match:
            current_date = date_match.group(1)
            continue

        # Check for new format: "## 2026-01-29 21:15 UTC - task"
        new_match = re.match(r"^## (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) UTC - (.+)$", line)
        if new_match:
            sig = f"{new_match.group(1)} {new_match.group(2)} {new_match.group(3)}"
            results.append((line, sig))
            continue

        # Check for old format: "### HH:MM - task"
        old_match = re.match(r"^### (\d{2}:\d{2}) - (.+)$", line)
        if old_match and current_date:
            time_part = old_match.group(1)
            task_part = old_match.group(2)
            sig = f"{current_date} {time_part} {task_part}"
            results.append((line, sig))

    return results


def extract_entry_signature(header: str, extra_context: list[str] = None) -> str:
    """Extract a signature from header for matching.

    Uses the original timestamp as part of the signature since that's what
    makes each entry unique (Claude's hallucinated time is still unique).

    e.g., "## 2026-01-29 21:15 UTC - deep-review (cross-review)"
    -> "2026-01-29 21:15 deep-review (cross-review)"
    """
    match = re.match(r"^## (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) UTC - (.+)$", header)
    if match:
        # Include the original (incorrect) time to make signature unique
        return f"{match.group(1)} {match.group(2)} {match.group(3)}"
    return header


def build_timestamp_map(git_entries: list[dict]) -> dict[str, datetime]:
    """Build a map from entry signatures to correct timestamps.

    Uses the original (incorrect) timestamp in the signature to ensure
    unique matching, since the same task type can run multiple times per day.
    """
    timestamp_map = {}

    for entry in git_entries:
        header_sigs = find_entry_headers_in_commit(entry["added_lines"])
        for _header_line, sig in header_sigs:
            # Only keep the first occurrence (earliest commit for that entry)
            if sig not in timestamp_map:
                timestamp_map[sig] = entry["timestamp"]

    return timestamp_map


def fix_changelog_timestamps(
    changelog_path: Path,
    timestamp_map: dict[str, datetime],
    dry_run: bool = False,
) -> tuple[int, int]:
    """Fix timestamps in the changelog file.

    Handles two formats:
    - New: "## 2026-01-29 21:15 UTC - task"
    - Old: "### HH:MM - task" (with date from previous ## header)

    Returns (entries_fixed, entries_not_found).
    """
    post = frontmatter.load(changelog_path)
    content = post.content

    fixed_count = 0
    not_found_count = 0

    # Track current date for old format
    current_date = [None]  # Use list to allow mutation in nested function

    def replace_new_format(match: re.Match) -> str:
        nonlocal fixed_count, not_found_count

        original = match.group(0)
        date_part = match.group(1)
        time_part = match.group(2)
        task_part = match.group(3)

        sig = f"{date_part} {time_part} {task_part}"

        if sig in timestamp_map:
            correct_ts = timestamp_map[sig]
            correct_ts_utc = correct_ts.astimezone(timezone.utc)
            new_time = correct_ts_utc.strftime("%H:%M")

            if new_time != time_part:
                fixed_count += 1
                print(f"  Fixed: {date_part} {time_part} -> {new_time} ({task_part})")
                return f"## {date_part} {new_time} UTC - {task_part}"
        else:
            not_found_count += 1
            print(f"  Not found in git: {sig}")

        return original

    def replace_old_format(match: re.Match) -> str:
        nonlocal fixed_count, not_found_count

        original = match.group(0)
        time_part = match.group(1)
        task_part = match.group(2)

        if not current_date[0]:
            return original

        sig = f"{current_date[0]} {time_part} {task_part}"

        if sig in timestamp_map:
            correct_ts = timestamp_map[sig]
            correct_ts_utc = correct_ts.astimezone(timezone.utc)
            new_time = correct_ts_utc.strftime("%H:%M")

            if new_time != time_part:
                fixed_count += 1
                print(f"  Fixed: {current_date[0]} {time_part} -> {new_time} ({task_part})")
                return f"### {new_time} - {task_part}"
        else:
            not_found_count += 1
            print(f"  Not found in git: {sig}")

        return original

    # Process line by line to track date context for old format
    lines = content.split("\n")
    new_lines = []

    for line in lines:
        # Check for date-only header (old format context)
        date_match = re.match(r"^## (\d{4}-\d{2}-\d{2})$", line)
        if date_match:
            current_date[0] = date_match.group(1)
            new_lines.append(line)
            continue

        # Try new format first
        new_match = re.match(r"^## (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) UTC - (.+)$", line)
        if new_match:
            new_lines.append(replace_new_format(new_match))
            continue

        # Try old format
        old_match = re.match(r"^### (\d{2}:\d{2}) - (.+)$", line)
        if old_match:
            new_lines.append(replace_old_format(old_match))
            continue

        new_lines.append(line)

    new_content = "\n".join(new_lines)

    if not dry_run and new_content != content:
        post.content = new_content
        changelog_path.write_text(frontmatter.dumps(post), encoding="utf-8")
        print(f"\nWrote changes to {changelog_path}")

    return fixed_count, not_found_count


def main():
    parser = argparse.ArgumentParser(
        description="Fix changelog timestamps by cross-referencing git history"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without writing",
    )
    parser.add_argument(
        "--changelog",
        type=Path,
        default=Path("obsidian/workflow/changelog.md"),
        help="Path to changelog file to fix",
    )
    parser.add_argument(
        "--history-from",
        type=Path,
        default=None,
        help="Path to file to get git history from (defaults to --changelog)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    changelog_path = repo_root / args.changelog
    history_path = repo_root / (args.history_from or args.changelog)

    if not changelog_path.exists():
        print(f"Error: Changelog not found at {changelog_path}")
        return 1

    print(f"Analyzing git history for {history_path}...")
    git_entries = get_git_log_entries(repo_root, history_path)
    print(f"Found {len(git_entries)} commits")

    print("\nBuilding timestamp map...")
    timestamp_map = build_timestamp_map(git_entries)
    print(f"Found {len(timestamp_map)} unique entry signatures")

    print("\nFixing timestamps..." + (" (dry run)" if args.dry_run else ""))
    fixed, not_found = fix_changelog_timestamps(
        changelog_path, timestamp_map, dry_run=args.dry_run
    )

    print(f"\nSummary:")
    print(f"  Entries fixed: {fixed}")
    print(f"  Entries not found in git: {not_found}")

    if args.dry_run and fixed > 0:
        print("\nRun without --dry-run to apply changes")

    return 0


if __name__ == "__main__":
    exit(main())
