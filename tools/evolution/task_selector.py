"""Task selection and skill invocation mapping for the evolution loop.

Provides the bridge between todo.md task types and Claude skill invocations.
"""

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from tools.todo.processor import Task, TaskType, complete_task, get_next_task, parse_tasks

log = logging.getLogger(__name__)


class LogicFlawError(Exception):
    """Raised when code reaches a state that indicates a programming error.

    Use this for unhandled enum cases, impossible conditions, and other
    situations that should never occur if the code is correct.
    """

    pass


@dataclass
class SkillInvocation:
    """A skill to invoke with optional arguments."""

    skill: str
    args: Optional[str] = None

    def to_prompt(self) -> str:
        """Convert to a Claude prompt string."""
        if self.args:
            return f"Run the {self.skill} skill with: {self.args}"
        return f"Run the {self.skill} skill"


# Default todo.md path
TODO_PATH = Path(__file__).parent.parent.parent / "obsidian" / "workflow" / "todo.md"


def count_p0_p2_tasks(content: str) -> int:
    """Count active tasks with priority P0, P1, or P2.

    P3 tasks don't count toward queue health - they require human promotion.
    """
    parsed = parse_tasks(content)
    return sum(1 for t in parsed["active"] if t.priority <= 2)


# Task types that can be automatically executed by mapping to a skill
EXECUTABLE_TASK_TYPES = {
    TaskType.EXPAND_TOPIC,
    TaskType.RESEARCH_TOPIC,
    TaskType.REFINE_DRAFT,
    TaskType.DEEP_REVIEW,
    TaskType.VALIDATE_ALL,
    TaskType.CHECK_TENETS,
    TaskType.PESSIMISTIC_REVIEW,
    TaskType.OPTIMISTIC_REVIEW,
    TaskType.CONDENSE,
    TaskType.CROSS_REVIEW,
}


def select_queue_task(content: str, executable_only: bool = True) -> Optional[Task]:
    """Select the next task from the queue.

    Handles:
    - Priority ordering (P0 > P1 > P2 > P3)
    - Skipping blocked/vetoed/in-progress tasks

    Args:
        content: The todo.md content
        executable_only: If True (default), skip tasks with type OTHER that
            can't be mapped to skills. Set to False to return any pending task.
    """
    if not executable_only:
        return get_next_task(content)

    # Get all pending tasks and find first executable one
    parsed = parse_tasks(content)

    # Filter to pending tasks without blockers
    from tools.todo.processor import TaskStatus

    pending = [
        t
        for t in parsed["active"]
        if t.status == TaskStatus.PENDING and not t.blocked_by
    ]

    if not pending:
        return None

    # Sort by priority (ascending) then by line number (ascending)
    pending.sort(key=lambda t: (t.priority, t.line_number))

    # Find first executable task
    for task in pending:
        if task.task_type in EXECUTABLE_TASK_TYPES:
            return task

    # No executable tasks found
    return None


def task_to_skill(task: Task) -> SkillInvocation:
    """Convert a Task to a SkillInvocation.

    Maps task types to their corresponding skills and extracts arguments.
    """
    task_type = task.task_type

    if task_type == TaskType.EXPAND_TOPIC:
        # Extract topic from title like "Write article on X"
        topic = _extract_topic_from_title(task.title)
        return SkillInvocation("expand-topic", topic)

    elif task_type == TaskType.RESEARCH_TOPIC:
        # Extract topic from title like "Research X"
        topic = _extract_topic_from_title(task.title)
        return SkillInvocation("research-topic", topic)

    elif task_type == TaskType.REFINE_DRAFT:
        # Extract file path from title or notes
        file_path = _extract_file_path(task.title, task.notes)
        # Include full task context so skill can read review files, etc.
        args = file_path or ""
        if task.notes:
            args = f"{args}\n\nTask context:\n{task.notes}"
        if task.review_file:
            args = f"{args}\n\nReview file: {task.review_file}"
        return SkillInvocation("refine-draft", args.strip())

    elif task_type == TaskType.DEEP_REVIEW:
        # Extract file path from title like "Deep review X.md"
        file_path = _extract_file_path(task.title, task.notes)
        return SkillInvocation("deep-review", file_path)

    elif task_type == TaskType.VALIDATE_ALL:
        return SkillInvocation("validate-all")

    elif task_type == TaskType.CHECK_TENETS:
        return SkillInvocation("check-tenets")

    elif task_type == TaskType.PESSIMISTIC_REVIEW:
        return SkillInvocation("pessimistic-review")

    elif task_type == TaskType.OPTIMISTIC_REVIEW:
        return SkillInvocation("optimistic-review")

    elif task_type == TaskType.CONDENSE:
        # Extract file path from title like "Condense free-will.md"
        file_path = _extract_file_path(task.title, task.notes)
        return SkillInvocation("condense", file_path)

    elif task_type == TaskType.CROSS_REVIEW:
        # Cross-review: review a file considering insights from new content
        # Title like "Cross-review whether-real.md considering defended-territory insights"
        file_path = _extract_file_path(task.title, task.notes)
        # Pass full title as context so deep-review knows what to consider
        return SkillInvocation("deep-review", f"{file_path} -- Context: {task.title}")

    elif task_type == TaskType.OTHER:
        # OTHER is explicitly unsupported - tasks must have a specific type
        log.error(
            f"Task has type OTHER which cannot be mapped to a skill: {task.title!r}. "
            "Ensure the task has a valid '- **Type**:' field in todo.md."
        )
        raise LogicFlawError(
            f"Cannot map TaskType.OTHER to a skill. Task: {task.title!r}. "
            "Add explicit type handling or fix the task's type field."
        )

    else:
        # Unhandled task type - this is a programming error
        log.error(f"Unhandled task type {task_type} for task: {task.title!r}")
        raise LogicFlawError(
            f"Unhandled task type: {task_type}. "
            "Add a handler in task_to_skill() for this type."
        )


def _extract_topic_from_title(title: str) -> str:
    """Extract topic name from task titles like 'Write article on X' or 'Research X'."""
    # Common patterns
    patterns = [
        r"^Write article on\s+(.+)$",
        r"^Research\s+(.+)$",
        r"^Expand\s+(.+)$",
        r"^expand-topic\s*:\s*(.+)$",
        r"^research-topic\s*:\s*(.+)$",
    ]

    for pattern in patterns:
        match = re.match(pattern, title, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    # Fallback: return the whole title
    return title


def _extract_file_path(title: str, notes: str) -> Optional[str]:
    """Extract file path from title or notes.

    Returns paths relative to repo root (e.g., 'obsidian/topics/free-will.md').

    Looks for patterns like:
    - "Deep review filename.md"
    - "Refine draft obsidian/concepts/foo.md"
    - Notes containing file paths
    """
    repo_root = Path(__file__).parent.parent.parent

    # Look for .md file in title
    match = re.search(r"([a-zA-Z0-9_-]+\.md)", title)
    if match:
        filename = match.group(1)
        # Try to find full path
        full_path = _find_file(filename)
        if full_path:
            # Return path relative to repo root
            try:
                return str(full_path.relative_to(repo_root))
            except ValueError:
                return str(full_path)
        return filename

    # Look in notes
    if notes:
        match = re.search(r"(obsidian/[a-zA-Z0-9_/-]+\.md)", notes)
        if match:
            return match.group(1)

    return None


def _find_file(filename: str) -> Optional[Path]:
    """Find a file by name in the obsidian directory."""
    obsidian_root = Path(__file__).parent.parent.parent / "obsidian"

    # Search common directories
    for subdir in ["concepts", "topics", "voids", "apex", "research"]:
        candidate = obsidian_root / subdir / filename
        if candidate.exists():
            return candidate

    # Recursive search as fallback
    for path in obsidian_root.rglob(filename):
        if path.is_file():
            return path

    return None


def load_todo() -> str:
    """Load todo.md content."""
    return TODO_PATH.read_text(encoding="utf-8")


def mark_task_completed(task: Task, output: Optional[str] = None) -> None:
    """Mark a task as completed in todo.md.

    Args:
        task: The task that was completed
        output: Optional output file path to record
    """
    content = load_todo()
    new_content = complete_task(content, task, output)
    TODO_PATH.write_text(new_content, encoding="utf-8")
