"""Completed-task round trip: complete_task -> archive_completed_tasks.

Regression cover for the silent archiving failure found on 2026-09-01. When
`## Completed Tasks` is empty — its state immediately after every archive
sweep — the insertion scan in complete_task ran past the section end and filed
the entry under the *next* heading. archive_completed_tasks only reads the
Completed section, so it found nothing, returned {} and archived nothing. The
two bugs concealed each other for fifteen weeks and todo.md reached 12.7 MB.
"""

from datetime import date

from tools.archive.workflow import archive_completed_tasks
from tools.todo.processor import complete_task, get_next_task

EMPTY_COMPLETED = """---
title: Todo
---

## Active Tasks

### P1: Write the thing
- **Type**: expand-topic
- **File**: obsidian/topics/thing.md

## Completed Tasks

## Blocked Tasks (Needs Human)

Tasks that failed 3+ times.

### ✓ 2026-08-01: An older blocked-section entry
- **Type**: refine-draft

## Vetoed Tasks
"""


def _section(content: str, heading: str) -> str:
    """Text between `heading` and the next '## ' heading."""
    lines = content.split("\n")
    start = next(i for i, ln in enumerate(lines) if ln.startswith(heading))
    end = next(
        (i for i, ln in enumerate(lines) if i > start and ln.startswith("## ")),
        len(lines),
    )
    return "\n".join(lines[start:end])


def test_completion_lands_in_completed_not_the_next_section():
    task = get_next_task(EMPTY_COMPLETED)
    assert task is not None

    updated = complete_task(EMPTY_COMPLETED, task)

    completed = _section(updated, "## Completed Tasks")
    blocked = _section(updated, "## Blocked Tasks")

    assert "Write the thing" in completed, (
        "completion must land in Completed Tasks, not run past the section end"
    )
    assert "Write the thing" not in blocked, (
        "completion leaked into Blocked Tasks — the boundary check regressed"
    )
    # The pre-existing Blocked entry must be left alone.
    assert "An older blocked-section entry" in blocked


def test_completed_entry_is_then_archivable(tmp_path):
    """The half the first bug hid: what lands in Completed must archive."""
    task = get_next_task(EMPTY_COMPLETED)
    updated = complete_task(EMPTY_COMPLETED, task)

    todo = tmp_path / "todo.md"
    todo.write_text(updated, encoding="utf-8")
    archive_dir = tmp_path / "archive"
    archive_dir.mkdir()

    # keep_weeks=0 so this week's entry is swept rather than retained.
    result = archive_completed_tasks(todo, archive_dir, keep_weeks=0)

    assert result, "archive_completed_tasks found nothing to archive"
    assert sum(result.values()) == 1
    written = list(archive_dir.glob("completed-tasks-*.md"))
    assert written, "no weekly archive file written"
    assert "Write the thing" in written[0].read_text(encoding="utf-8")


def test_task_is_removed_from_active():
    task = get_next_task(EMPTY_COMPLETED)
    updated = complete_task(EMPTY_COMPLETED, task)
    active = _section(updated, "## Active Tasks")
    assert "### P1: Write the thing" not in active


def test_entry_carries_today_and_type():
    task = get_next_task(EMPTY_COMPLETED)
    updated = complete_task(EMPTY_COMPLETED, task)
    completed = _section(updated, "## Completed Tasks")
    assert date.today().isoformat() in completed
    assert "expand-topic" in completed
