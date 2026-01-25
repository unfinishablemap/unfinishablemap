"""Task cycle management for deterministic evolution scheduling.

The cycle is a fixed sequence of task types that repeats indefinitely.
Speed is controlled by --interval; the cycle ensures consistent task ratios.
"""

from typing import Optional

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
    "research-voids",     # 21
    "queue",              # 22
    "queue",              # 23
]

CYCLE_LENGTH = len(TASK_CYCLE)

# Less frequent tasks - run every N complete cycles
# Key = skill name, Value = run every N cycles
CYCLE_TRIGGERS: dict[str, int] = {
    "check-links": 2,     # Every 2 cycles (48 sessions)
    "check-tenets": 3,    # Every 3 cycles (72 sessions)
    "apex-evolve": 4,     # Every 4 cycles (96 sessions)
    "tune-system": 6,     # Every 6 cycles (144 sessions)
}


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
