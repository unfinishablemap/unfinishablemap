"""Archive workflow files (changelog, completed tasks) into weekly files."""

import re
from datetime import date, datetime, timezone
from pathlib import Path

import frontmatter


def get_iso_week(d: date) -> str:
    """Return ISO week string like '2026-W04'."""
    iso_cal = d.isocalendar()
    return f"{iso_cal.year}-W{iso_cal.week:02d}"


def get_current_iso_week() -> str:
    """Return current ISO week string."""
    return get_iso_week(datetime.now(timezone.utc).date())


def parse_changelog_date(header: str) -> date | None:
    """Parse date from changelog header.

    Handles two formats:
    - '## 2026-01-25 11:16 UTC - ...' (newer format with time)
    - '## 2026-01-21' or '## 2026-01-17 (earlier)' (older date-only format)
    """
    # Try newer format with time first
    match = re.match(r"^## (\d{4}-\d{2}-\d{2}) \d{2}:\d{2} UTC", header)
    if match:
        return date.fromisoformat(match.group(1))
    # Try date-only format (possibly with trailing text like "(earlier)")
    match = re.match(r"^## (\d{4}-\d{2}-\d{2})", header)
    if match:
        return date.fromisoformat(match.group(1))
    return None


def parse_completed_task_date(header: str) -> date | None:
    """Parse date from completed task header like '### ✓ 2026-01-25: ...'."""
    match = re.match(r"^### ✓ (\d{4}-\d{2}-\d{2}):", header)
    if match:
        return date.fromisoformat(match.group(1))
    return None


def _week_start_date(iso_week: str) -> date:
    """Get the Monday of an ISO week like '2026-W04'."""
    year, week = iso_week.split("-W")
    return date.fromisocalendar(int(year), int(week), 1)


def _create_archive_frontmatter(title: str, iso_week: str) -> str:
    """Create frontmatter for an archive file."""
    week_start = _week_start_date(iso_week)
    return f"""---
title: "{title}"
created: {week_start.isoformat()}
archived: true
---

"""


def archive_changelog(
    changelog_path: Path,
    archive_dir: Path,
    keep_weeks: int = 1,
    dry_run: bool = False,
) -> dict[str, int]:
    """
    Move old changelog entries to weekly archive files.

    Args:
        changelog_path: Path to changelog.md
        archive_dir: Directory for archive files
        keep_weeks: Number of recent weeks to keep in main file
        dry_run: If True, don't write files

    Returns:
        Dict mapping ISO week strings to number of entries archived
    """
    post = frontmatter.load(changelog_path)
    content = post.content

    # Split into sections by ## headers (each section is a dated group)
    # This handles both formats:
    # - Newer: ## 2026-01-25 11:16 UTC - task (Session N)
    # - Older: ## 2026-01-21 followed by ### sub-entries
    section_pattern = re.compile(r"^(## .+?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    sections = section_pattern.findall(content)

    current_week = get_current_iso_week()
    entries_by_week: dict[str, list[str]] = {}
    entries_to_keep: list[str] = []

    for section in sections:
        # Strip whitespace and trailing --- separators
        section = section.strip()
        while section.endswith("---"):
            section = section[:-3].strip()
        if not section:
            continue

        # Get the header line
        lines = section.split("\n")
        header = lines[0] if lines else ""

        if not header.startswith("## "):
            entries_to_keep.append(section)
            continue

        entry_date = parse_changelog_date(header)
        if not entry_date:
            entries_to_keep.append(section)
            continue

        entry_week = get_iso_week(entry_date)

        # Calculate weeks difference
        current_week_start = _week_start_date(current_week)
        entry_week_start = _week_start_date(entry_week)
        weeks_ago = (current_week_start - entry_week_start).days // 7

        if weeks_ago < keep_weeks:
            entries_to_keep.append(section)
        else:
            if entry_week not in entries_by_week:
                entries_by_week[entry_week] = []
            entries_by_week[entry_week].append(section)

    # Write archive files
    archived_counts: dict[str, int] = {}
    if not dry_run:
        archive_dir.mkdir(parents=True, exist_ok=True)

    for iso_week, entries in sorted(entries_by_week.items()):
        archive_file = archive_dir / f"changelog-{iso_week}.md"
        archived_counts[iso_week] = len(entries)

        if dry_run:
            continue

        # Check if archive file exists and merge
        if archive_file.exists():
            existing = frontmatter.load(archive_file)
            existing_content = existing.content.strip()
            # Prepend new entries (newer first)
            new_content = "\n\n---\n\n".join(entries)
            if existing_content:
                merged_content = new_content + "\n\n---\n\n" + existing_content
            else:
                merged_content = new_content
        else:
            merged_content = "\n\n---\n\n".join(entries)

        full_content = _create_archive_frontmatter(
            f"AI Activity Changelog - Week {iso_week}", iso_week
        )
        full_content += merged_content
        archive_file.write_text(full_content, encoding="utf-8")

    # Rewrite main file with kept entries
    if not dry_run and entries_by_week:
        new_content = "\n\n---\n\n".join(entries_to_keep)
        post.content = new_content
        changelog_path.write_text(frontmatter.dumps(post), encoding="utf-8")

    return archived_counts


def archive_completed_tasks(
    todo_path: Path,
    archive_dir: Path,
    keep_weeks: int = 1,
    dry_run: bool = False,
) -> dict[str, int]:
    """
    Move old completed tasks to weekly archive files.

    Args:
        todo_path: Path to todo.md
        archive_dir: Directory for archive files
        keep_weeks: Number of recent weeks to keep in main file
        dry_run: If True, don't write files

    Returns:
        Dict mapping ISO week strings to number of tasks archived
    """
    post = frontmatter.load(todo_path)
    content = post.content

    # Find the Completed Tasks section
    completed_match = re.search(r"^## Completed Tasks\n", content, re.MULTILINE)
    if not completed_match:
        return {}

    completed_start = completed_match.end()

    # Find the next section (## heading)
    next_section = re.search(r"^## ", content[completed_start:], re.MULTILINE)
    if next_section:
        completed_end = completed_start + next_section.start()
    else:
        completed_end = len(content)

    completed_section = content[completed_start:completed_end]

    # Split into individual tasks (### headings)
    task_pattern = re.compile(r"^### ✓", re.MULTILINE)
    task_starts = [m.start() for m in task_pattern.finditer(completed_section)]

    if not task_starts:
        return {}

    tasks: list[str] = []
    for i, start in enumerate(task_starts):
        if i + 1 < len(task_starts):
            end = task_starts[i + 1]
        else:
            end = len(completed_section)
        tasks.append(completed_section[start:end].strip())

    current_week = get_current_iso_week()
    tasks_by_week: dict[str, list[str]] = {}
    tasks_to_keep: list[str] = []

    for task in tasks:
        lines = task.split("\n")
        header = lines[0] if lines else ""

        task_date = parse_completed_task_date(header)
        if not task_date:
            tasks_to_keep.append(task)
            continue

        task_week = get_iso_week(task_date)

        current_week_start = _week_start_date(current_week)
        task_week_start = _week_start_date(task_week)
        weeks_ago = (current_week_start - task_week_start).days // 7

        if weeks_ago < keep_weeks:
            tasks_to_keep.append(task)
        else:
            if task_week not in tasks_by_week:
                tasks_by_week[task_week] = []
            tasks_by_week[task_week].append(task)

    # Write archive files
    archived_counts: dict[str, int] = {}
    if not dry_run:
        archive_dir.mkdir(parents=True, exist_ok=True)

    for iso_week, week_tasks in sorted(tasks_by_week.items()):
        archive_file = archive_dir / f"completed-tasks-{iso_week}.md"
        archived_counts[iso_week] = len(week_tasks)

        if dry_run:
            continue

        # Check if archive file exists and merge
        if archive_file.exists():
            existing = frontmatter.load(archive_file)
            existing_content = existing.content.strip()
            new_content = "\n\n".join(week_tasks)
            if existing_content:
                merged_content = new_content + "\n\n" + existing_content
            else:
                merged_content = new_content
        else:
            merged_content = "\n\n".join(week_tasks)

        full_content = _create_archive_frontmatter(
            f"Completed Tasks - Week {iso_week}", iso_week
        )
        full_content += merged_content
        archive_file.write_text(full_content, encoding="utf-8")

    # Rewrite main file with kept tasks
    if not dry_run and tasks_by_week:
        kept_section = "\n\n".join(tasks_to_keep)
        if kept_section:
            kept_section = "\n" + kept_section + "\n"

        new_content = (
            content[:completed_start]
            + kept_section
            + content[completed_end:]
        )
        post.content = new_content
        todo_path.write_text(frontmatter.dumps(post), encoding="utf-8")

    return archived_counts
