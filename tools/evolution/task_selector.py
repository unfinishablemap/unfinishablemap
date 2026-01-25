"""Task selection and skill invocation mapping for the evolution loop.

Provides the bridge between todo.md task types and Claude skill invocations.
"""

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from tools.todo.processor import Task, TaskType, get_next_task, parse_tasks


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


def select_queue_task(content: str) -> Optional[Task]:
    """Select the next task from the queue.

    Delegates to processor.get_next_task which handles:
    - Priority ordering (P0 > P1 > P2 > P3)
    - Skipping blocked/vetoed/in-progress tasks
    """
    return get_next_task(content)


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
        return SkillInvocation("refine-draft", file_path)

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

    else:
        # TaskType.OTHER - use notes as context
        return SkillInvocation("expand-topic", task.notes or task.title)


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

    Looks for patterns like:
    - "Deep review filename.md"
    - "Refine draft obsidian/concepts/foo.md"
    - Notes containing file paths
    """
    # Look for .md file in title
    match = re.search(r"([a-zA-Z0-9_-]+\.md)", title)
    if match:
        filename = match.group(1)
        # Try to find full path
        full_path = _find_file(filename)
        if full_path:
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
