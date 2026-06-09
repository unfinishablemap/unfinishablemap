"""Task cycle management for deterministic evolution scheduling.

The cycle is a fixed sequence of task types that repeats indefinitely.
Speed is controlled by --interval; the cycle ensures consistent task ratios.
"""

from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .state import EvolutionState

# The main task cycle - 24 slots that repeat
# "queue" = pick from P0-P2 todo queue
# Other values = run that skill directly
TASK_CYCLE: list[str] = [
    "queue",              # 0  - Pick from P0-P2 queue
    "queue",              # 1
    "deep-review",        # 2  - LLM picks which file
    "queue",              # 3
    "queue",              # 4
    "pessimistic-review", # 5  - Site-wide critique
    "queue",              # 6
    "queue",              # 7
    "deep-review",        # 8
    "queue",              # 9
    "queue",              # 10
    "optimistic-review",  # 11 - Site-wide opportunities
    "queue",              # 12
    "queue",              # 13
    "deep-review",        # 14
    "queue",              # 15
    "coalesce",           # 16 - LLM finds candidates
    "queue",              # 17
    "queue",              # 18
    "deep-review",        # 19
    "queue",              # 20
    "queue",              # 21 - Was second coalesce slot; reduced 2/24 → 1/24 per tune-system 2026-04-29b (voids/ post-saturation; six consecutive coalesce abandonments + null archive audit)
    "queue",              # 22
    "queue",              # 23
]

CYCLE_LENGTH = len(TASK_CYCLE)

# Less frequent tasks - run every N complete cycles
# Key = skill name, Value = run every N cycles
CYCLE_TRIGGERS: dict[str, int] = {
    "embed-videos": 1,     # Every cycle — picks up newly-published YouTube videos
    "check-model-fallback": 1,  # Every cycle — Fable→Opus fallback detection (attribution)
    "check-links": 2,      # Every 2 cycles (48 sessions)
    "research-voids": 2,   # Every 2 cycles (48 sessions) - moved from main cycle; voids at capacity
    "check-tenets": 3,     # Every 3 cycles (72 sessions)
    "apex-evolve": 4,      # Every 4 cycles (96 sessions)
    "tune-system": 6,      # Every 6 cycles (144 sessions)
}

# Per-skill wall-clock minimum age before a cycle-trigger may re-fire it,
# regardless of the cycle-count math above. At fast `--interval` the cycle
# trigger fires far more often than some skills are designed for. tune-system's
# SKILL.md mandates a monthly cadence — without this gate it was running daily
# (9 reports in 9 days, each declining to apply Tier-1 changes). Minutes are
# the unit so a future skill can request a sub-hour gate if needed.
#
# Skills NOT listed here are not gated and fire purely on the cycle-count
# schedule above.
TRIGGER_MIN_AGE_HOURS: dict[str, float] = {
    # tune-system: monthly cadence per SKILL.md; the every-6-cycles trigger
    # otherwise fires it ~daily at fast --interval.
    "tune-system": 30 * 24,
}


def filter_triggers_by_min_age(
    triggers: list[str],
    state: "EvolutionState",
    now: Optional[datetime] = None,
) -> tuple[list[str], list[str]]:
    """Apply per-skill wall-clock min-age gates to a cycle-trigger list.

    Returns ``(allowed, gated)`` — ``allowed`` is the subset that may run
    this iteration; ``gated`` is the subset suppressed by their per-skill
    minimum age. Caller is responsible for logging gated skills.
    """
    if now is None:
        now = datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)

    allowed: list[str] = []
    gated: list[str] = []
    for skill in triggers:
        min_age_hours = TRIGGER_MIN_AGE_HOURS.get(skill)
        if min_age_hours is None:
            allowed.append(skill)
            continue
        last_run = state.last_runs.get(skill)
        if last_run is None:
            allowed.append(skill)
            continue
        if last_run.tzinfo is None:
            last_run = last_run.replace(tzinfo=timezone.utc)
        age = now - last_run
        if age >= timedelta(hours=min_age_hours):
            allowed.append(skill)
        else:
            gated.append(skill)
    return allowed, gated


def get_cycle_task(position: int) -> str:
    """Get the task type for a given cycle position.

    Args:
        position: The current cycle position (0-based, can exceed CYCLE_LENGTH)

    Returns:
        Task type string: "queue" or a skill name like "deep-review"
    """
    return TASK_CYCLE[position % CYCLE_LENGTH]


def get_cycle_triggers(cycles_completed: int) -> list[str]:
    """Get tasks that should run when a cycle completes.

    Args:
        cycles_completed: Total number of complete cycles (cycle_position // CYCLE_LENGTH)

    Returns:
        List of skill names to run (may be empty)
    """
    if cycles_completed == 0:
        return []

    triggers = []
    for task, every_n in CYCLE_TRIGGERS.items():
        if cycles_completed % every_n == 0:
            triggers.append(task)

    return triggers


def is_cycle_complete(position: int) -> bool:
    """Check if the current position marks a cycle completion.

    Args:
        position: The cycle position AFTER incrementing

    Returns:
        True if we just completed a cycle (position is multiple of CYCLE_LENGTH)
    """
    return position > 0 and position % CYCLE_LENGTH == 0


def get_cycle_stats(position: int) -> dict[str, int]:
    """Get statistics about the current cycle state.

    Args:
        position: Current cycle position

    Returns:
        Dict with cycles_completed, position_in_cycle, sessions_until_cycle_end
    """
    return {
        "cycles_completed": position // CYCLE_LENGTH,
        "position_in_cycle": position % CYCLE_LENGTH,
        "sessions_until_cycle_end": CYCLE_LENGTH - (position % CYCLE_LENGTH),
    }


def describe_cycle() -> str:
    """Return a human-readable description of the cycle for logging."""
    queue_count = sum(1 for t in TASK_CYCLE if t == "queue")
    other_tasks = [t for t in TASK_CYCLE if t != "queue"]
    unique_others = sorted(set(other_tasks))

    lines = [
        f"Task cycle: {CYCLE_LENGTH} slots",
        f"  Queue tasks: {queue_count} ({queue_count * 100 // CYCLE_LENGTH}%)",
    ]

    for task in unique_others:
        count = other_tasks.count(task)
        lines.append(f"  {task}: {count}")

    lines.append("Cycle triggers (every N cycles):")
    for task, every_n in sorted(CYCLE_TRIGGERS.items(), key=lambda x: x[1]):
        lines.append(f"  {task}: every {every_n} cycles ({every_n * CYCLE_LENGTH} sessions)")

    return "\n".join(lines)
