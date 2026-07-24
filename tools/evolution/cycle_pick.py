"""Pick the next action for the /loop-driven evolution orchestrator.

Reads `evolution-state.yaml`, applies the same dispatch logic as
`scripts/evolve_loop.py:run_session` (minus the time-triggered tasks
that live in their own `/loop`s), and prints a single JSON action on
stdout.

Output schema:

    {"action": "invoke",
     "kind": "queue|cycle|trigger|replenish|collect|combine|agentic_social",
     "skill": "<skill-name>",
     "args": "<args or empty string>",
     "chrome": true|false,         # only present when chrome MCP needed
     "queue_task_line": <int>}     # only when kind == "queue"

    {"action": "idle", "kind": "stop_signal|queue_empty|idle", "reason": "..."}

This module performs *no* state mutation — it is purely a pick.
`cycle_post.py` is responsible for advancing cycle_position, updating
last_runs, marking todo tasks completed, etc.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Repo-root path manipulation so `python -m tools.evolution.cycle_pick`
# works regardless of CWD.
REPO_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.evolution.cycle import get_cycle_task  # noqa: E402
from tools.evolution.state import (  # noqa: E402
    EvolutionState,
    all_sections_at_cap,
    load_state,
)
from tools.evolution.task_selector import (  # noqa: E402
    count_p0_p2_tasks,
    load_todo,
    select_queue_task,
    task_to_skill,
)
from tools.evolution.time_trigger import (  # noqa: E402
    check_all_wall_clock_triggers,
)
from tools.todo.processor import TaskType  # noqa: E402

STATE_PATH = REPO_ROOT / "obsidian" / "workflow" / "evolution-state.yaml"
STOP_SIGNAL_PATH = REPO_ROOT / ".unfin" / "stop-loop"
PENDING_TRIGGERS_PATH = REPO_ROOT / ".unfin" / "pending-triggers.json"
# Sentinel: cycle_pick writes the chosen queue task here so cycle_post can
# look it up by title (stable across line-number drift caused by skills
# adding follow-up tasks to todo.md mid-iteration).
CURRENT_QUEUE_TASK_PATH = REPO_ROOT / ".unfin" / "current-queue-task.json"

MIN_QUEUE_TASKS = 3

# Agentic social cadence (mirrors evolve_loop.py)
AGENTIC_SOCIAL_INTERVAL_MINUTES = 45
AGENTIC_SOCIAL_SUSPENSION_BACKOFF_HOURS = 6

# Chrome automation window (mirrors evolve_loop.py)
AUTOMATION_WINDOW_START_HOUR_UTC = 0
AUTOMATION_LAST_START_HOUR_UTC = 7


def _is_automation_window(now: datetime) -> bool:
    return (
        AUTOMATION_WINDOW_START_HOUR_UTC
        <= now.hour
        < AUTOMATION_LAST_START_HOUR_UTC
    )


def _should_post_agentic_social(now: datetime, state: EvolutionState) -> bool:
    suspended_until = state.last_runs.get("agentic-social-suspended-until")
    if suspended_until is not None and now < suspended_until:
        return False
    last_run = state.last_runs.get("agentic-social")
    if last_run is None:
        return True
    minutes_since = (now - last_run).total_seconds() / 60
    return minutes_since >= AGENTIC_SOCIAL_INTERVAL_MINUTES


def _load_pending_triggers() -> list[str]:
    if not PENDING_TRIGGERS_PATH.is_file():
        return []
    try:
        data = json.loads(PENDING_TRIGGERS_PATH.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return [str(t) for t in data]
    except Exception:
        pass
    return []


def _emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload), flush=True)


def _emit_idle(kind: str, reason: str) -> None:
    _emit({"action": "idle", "kind": kind, "reason": reason})


def _emit_invoke(
    kind: str,
    skill: str,
    args: str = "",
    *,
    chrome: bool = False,
    queue_task_line: int | None = None,
) -> None:
    payload: dict[str, Any] = {
        "action": "invoke",
        "kind": kind,
        "skill": skill,
        "args": args,
    }
    if chrome:
        payload["chrome"] = True
    if queue_task_line is not None:
        payload["queue_task_line"] = queue_task_line
    _emit(payload)


def main() -> int:
    now = datetime.now(timezone.utc)

    # 1. Stop signal — bail before reading anything else.
    if STOP_SIGNAL_PATH.exists():
        _emit_idle("stop_signal", f"{STOP_SIGNAL_PATH} present")
        return 0

    state = load_state(STATE_PATH)

    # 2. Drain pending cycle-completion triggers serially across iterations.
    pending = _load_pending_triggers()
    if pending:
        _emit_invoke("trigger", pending[0])
        return 0

    # 3. Wall-clock triggers (literature-drift, commissions, add-highlight-tweet).
    # Consolidated here so a single /loop cron drives everything.
    wc = check_all_wall_clock_triggers(now, state)
    if wc is not None:
        _emit_invoke(wc.kind, wc.skill, wc.args, chrome=wc.chrome)
        return 0

    # 4. Collect any ready outer review (any service). Chrome required.
    # Must outrank agentic-social: collects can only start inside the
    # automation window (00:00–07:00 UTC), while agentic-social fires every
    # 45 min all day and catches up on the next iteration. On 2026-07-24
    # agentic-social took the last in-window iteration (06:52), the ready
    # gemini collect never ran, and the whole cycle's queue tasks stayed
    # deferred behind the missing synthesis for a full day.
    if _is_automation_window(now):
        try:
            from tools.reviews.pending import find_ready
            from tools.reviews.services import SERVICES
        except Exception as e:
            print(f"[WARN] outer-review modules unavailable: {e}", file=sys.stderr)
        else:
            for svc in SERVICES:
                review = find_ready(
                    now,
                    min_age_minutes=svc.min_collect_age_minutes,
                    service=svc.service,
                )
                if review is not None:
                    _emit_invoke(
                        "collect",
                        svc.skill_collect,
                        review.target_filename,
                        chrome=True,
                    )
                    return 0

    # 5. Agentic-social (every 45 min, with suspension backoff).
    if _should_post_agentic_social(now, state):
        _emit_invoke("agentic_social", "agentic-social")
        return 0

    # 6. Combine outer-reviews for any cycle whose entries are all resolved
    #    and where the synthesis file does not yet exist. No Chrome needed.
    try:
        from tools.reviews.synthesis import cycle_dates_to_synthesize
        cycle_dates = list(cycle_dates_to_synthesize(now))
    except Exception as e:
        print(f"[WARN] outer-review synthesis check failed: {e}", file=sys.stderr)
        cycle_dates = []
    if cycle_dates:
        _emit_invoke("combine", "combine-outer-reviews", cycle_dates[0])
        return 0

    # 7. Queue health → replenish-queue if below threshold.
    #
    # Guard against an infinite replenish loop: when every generative
    # source is exhausted/blocked (all sections at cap → expand-topic
    # refused, length offenders vetoed, no fresh research, zero orphans),
    # replenish-queue can run yet add nothing, leaving p0_p2 below the
    # threshold. Without the guard, step 6 would re-emit replenish every
    # iteration forever and never reach the cycle slot (step 7), so the
    # cycle never advances and the cycle-boundary anchoring audit — which
    # would add reachable refine tasks and heal the queue — never fires.
    # If the immediately-preceding task was already a replenish that did
    # not lift the queue, fall through to the cycle slot instead: cycle
    # slots (deep-review, pessimistic/optimistic-review, coalesce) do not
    # require queue tasks, advance cycle_position, and eventually trigger
    # the anchoring audit that replenishes reachable work organically.
    todo = load_todo()
    cap_skip: set[TaskType] | None = None
    if all_sections_at_cap(state.section_caps):
        cap_skip = {TaskType.EXPAND_TOPIC}
    p0_p2 = count_p0_p2_tasks(todo, skip_types=cap_skip)
    last_task = state.recent_tasks[-1].task if state.recent_tasks else None
    if p0_p2 < MIN_QUEUE_TASKS and last_task != "replenish-queue":
        _emit_invoke("replenish", "replenish-queue")
        return 0

    # 8. Cycle slot — either a queue pick or a named cycle skill.
    cycle_task = get_cycle_task(state.cycle_position)
    if cycle_task == "queue":
        task = select_queue_task(
            todo, executable_only=True, skip_types=cap_skip
        )
        if task is None:
            _emit_idle("queue_empty", "no executable queue tasks")
            return 0
        invocation = task_to_skill(task)
        # Persist the task identity for cycle_post — title is stable
        # across line-number drift caused by skills adding follow-up
        # tasks to todo.md mid-iteration.
        CURRENT_QUEUE_TASK_PATH.parent.mkdir(parents=True, exist_ok=True)
        CURRENT_QUEUE_TASK_PATH.write_text(
            json.dumps({"title": task.title, "line_number": task.line_number}),
            encoding="utf-8",
        )
        _emit_invoke(
            "queue",
            invocation.skill,
            invocation.args or "",
            queue_task_line=task.line_number,
        )
        return 0

    # Named cycle skill (deep-review, pessimistic-review, optimistic-review,
    # coalesce, etc.). The orchestrator skill invokes it; no extra args.
    _emit_invoke("cycle", cycle_task)
    return 0


if __name__ == "__main__":
    sys.exit(main())
