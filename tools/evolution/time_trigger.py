"""Wall-clock decision functions for the unified /unfin-cycle orchestrator.

All wall-clock-triggered actions (commission-{chatgpt,claude,gemini}-review,
literature-drift-review, add-highlight-tweet) used to live in dedicated
cron `/loop`s. Rolled into the main /unfin-cycle so the operator only
maintains one /loop (which avoids re-arming every seven days).

`check_all_wall_clock_triggers(now, state)` is the single entry point.
It returns the first `TriggerDecision` that fires, in priority order, or
None if no wall-clock trigger is due.

These checks mirror the gating in `scripts/evolve_loop.py` —
automation-window membership, per-day uniqueness, in-flight check,
failure cooldown, login backoff.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Callable

# Mirror evolve_loop.py constants.
TWEET_HOUR_UTC = 8
LITERATURE_DRIFT_WEEKDAY = 1  # Tuesday (Mon=0)
LITERATURE_DRIFT_HOUR_UTC = 5
AUTOMATION_WINDOW_START_HOUR_UTC = 0
AUTOMATION_LAST_START_HOUR_UTC = 7
# Fallback detection is wall-clock, not cycle-based: only ~25% of loop
# iterations consume a cycle slot (the rest are replenish/social/outer-review
# legs), so "every cycle" stretched to ~29h of uptime — too slow when a
# session-level Fable→Opus stick can run for days (confirmed 2026-06-10/11).
MODEL_FALLBACK_INTERVAL_HOURS = 4


@dataclass
class TriggerDecision:
    kind: str        # "commission" or "trigger"
    skill: str
    args: str = ""
    chrome: bool = False


def _is_automation_window(now: datetime) -> bool:
    return AUTOMATION_WINDOW_START_HOUR_UTC <= now.hour < AUTOMATION_LAST_START_HOUR_UTC


def check_commission(
    service_short: str, now: datetime, state
) -> TriggerDecision | None:
    """Gate one commission-* trigger. Mirrors evolve_loop._due_for_commission()."""
    try:
        from tools.reviews.services import SERVICES
    except Exception:
        return None

    svc = next((s for s in SERVICES if s.service == service_short), None)
    if svc is None:
        return None

    if not _is_automation_window(now):
        return None

    blocked_until = state.last_runs.get(f"{svc.skill_commission}-blocked-until")
    if blocked_until is not None and now < blocked_until:
        return None

    if now.hour < svc.commission_hour_utc:
        return None

    last_run = state.last_runs.get(svc.skill_commission)
    if last_run is not None and last_run.date() == now.date():
        return None

    try:
        from tools.reviews.pending import find_recent_failed, has_in_flight
    except Exception:
        return None

    if has_in_flight(svc.service):
        return None

    if find_recent_failed(svc.service, now, cooldown_hours=1):
        return None

    return TriggerDecision(
        kind="commission",
        skill=svc.skill_commission,
        chrome=True,
    )


def check_literature_drift(now: datetime, state) -> TriggerDecision | None:
    """Tue ≥05:00 UTC, once per Tuesday. No Chrome needed."""
    if now.weekday() != LITERATURE_DRIFT_WEEKDAY:
        return None
    if now.hour < LITERATURE_DRIFT_HOUR_UTC:
        return None
    last_run = state.last_runs.get("literature-drift-review")
    if last_run is not None and last_run.date() == now.date():
        return None
    return TriggerDecision(kind="trigger", skill="literature-drift-review")


def check_model_fallback(now: datetime, state) -> TriggerDecision | None:
    """Every MODEL_FALLBACK_INTERVAL_HOURS. Cheap transcript grep, no Chrome.

    The script keeps its own scan high-water mark, so an extra firing is a
    fast no-op; last_runs gating here just bounds the iteration overhead.
    """
    last_run = state.last_runs.get("check-model-fallback")
    if last_run is not None:
        age_hours = (now - last_run).total_seconds() / 3600
        if age_hours < MODEL_FALLBACK_INTERVAL_HOURS:
            return None
    return TriggerDecision(kind="trigger", skill="check-model-fallback")


def check_add_highlight_tweet(now: datetime, state) -> TriggerDecision | None:
    """≥08:00 UTC, once per day. Underlying skill picks its own candidate."""
    if now.hour < TWEET_HOUR_UTC:
        return None
    today = now.date().isoformat()
    if state.last_tweet_date == today:
        return None
    return TriggerDecision(kind="trigger", skill="add-highlight", args="--tweet")


def check_harvest_research(now: datetime, state) -> TriggerDecision | None:
    """Once per day. Mines outer/optimistic reviews for new research-topic subjects.

    Wall-clock (not cycle-based) for the same reason as check-model-fallback:
    cycle cadence stretches to ~29h of uptime and drifts. No Chrome, no
    automation-window gating — pure local review-corpus scan. The skill is a
    cheap no-op when there are no unscanned mine-reviews.
    """
    last_run = state.last_runs.get("harvest-research-subjects")
    if last_run is not None and last_run.date() == now.date():
        return None
    return TriggerDecision(kind="trigger", skill="harvest-research-subjects")


# Priority order — first match wins per iteration. Subsequent iterations
# pick up the next eligible trigger (since last_runs/last_tweet_date are
# updated by cycle_post on success).
_PRIORITY: list[Callable[[datetime, object], "TriggerDecision | None"]] = [
    check_literature_drift,
    lambda now, state: check_commission("chatgpt", now, state),
    lambda now, state: check_commission("claude", now, state),
    lambda now, state: check_commission("gemini", now, state),
    check_add_highlight_tweet,
    check_harvest_research,
    check_model_fallback,
]


def check_all_wall_clock_triggers(now: datetime, state) -> TriggerDecision | None:
    """Return the first wall-clock trigger that fires, or None."""
    for check in _PRIORITY:
        decision = check(now, state)
        if decision is not None:
            return decision
    return None
