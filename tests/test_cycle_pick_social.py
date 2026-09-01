"""Tests for the agentic-social cadence gate in cycle_pick.

agentic-social preempts the cycle slot, so a purely time-based gate starves
the cycle whenever the loop's iteration interval exceeds the social interval:
the gate is satisfied on every iteration and no queue task, deep-review or
other cycle work ever runs. These tests pin the extra cycle-progress gate that
prevents that, and the stall valve that keeps it from over-correcting.
"""

from datetime import datetime, timedelta, timezone

from tools.evolution.cycle_pick import (
    AGENTIC_SOCIAL_INTERVAL_MINUTES,
    AGENTIC_SOCIAL_MAX_STALL_MINUTES,
    AGENTIC_SOCIAL_MIN_CYCLE_ADVANCES,
    _should_post_agentic_social,
)
from tools.evolution.state import (
    ContentStats,
    ConvergenceTargets,
    EvolutionState,
    Progress,
    Quality,
    SectionCaps,
    TaskRecord,
)

NOW = datetime(2026, 9, 1, 12, 0, tzinfo=timezone.utc)


def _state(*, last_social_minutes_ago: float | None, records: list[TaskRecord]):
    last_runs: dict[str, datetime | None] = {}
    if last_social_minutes_ago is not None:
        last_runs["agentic-social"] = NOW - timedelta(minutes=last_social_minutes_ago)
    return EvolutionState(
        last_updated=NOW,
        session_count=0,
        cycle_position=0,
        last_runs=last_runs,
        last_git_push=None,
        last_tweet_date=None,
        content_stats=ContentStats(),
        section_caps=SectionCaps(),
        convergence_targets=ConvergenceTargets(),
        progress=Progress(),
        quality=Quality(),
        failed_tasks={},
        recent_tasks=records,
    )


def _social() -> TaskRecord:
    return TaskRecord(
        task="agentic-social", task_type="agentic-social",
        date="2026-09-01", outcome="success", kind="agentic_social",
    )


def _cycle_work(n: int = 1) -> list[TaskRecord]:
    return [
        TaskRecord(
            task="deep-review", task_type="deep-review",
            date="2026-09-01", outcome="success", kind="cycle",
        )
        for _ in range(n)
    ]


def test_never_run_posts_immediately():
    assert _should_post_agentic_social(NOW, _state(last_social_minutes_ago=None, records=[]))


def test_inside_interval_is_blocked():
    state = _state(
        last_social_minutes_ago=AGENTIC_SOCIAL_INTERVAL_MINUTES - 1,
        records=[_social(), *_cycle_work(10)],
    )
    assert not _should_post_agentic_social(NOW, state)


def test_slow_loop_does_not_starve_the_cycle():
    """The reported bug: interval elapsed but the cycle has not advanced.

    With a loop interval longer than the social interval this held on every
    iteration, so social ran forever and the cycle never moved.
    """
    state = _state(
        last_social_minutes_ago=AGENTIC_SOCIAL_INTERVAL_MINUTES + 30,
        records=[_social()],
    )
    assert not _should_post_agentic_social(NOW, state)


def test_posts_once_the_cycle_has_advanced_enough():
    state = _state(
        last_social_minutes_ago=AGENTIC_SOCIAL_INTERVAL_MINUTES + 30,
        records=[_social(), *_cycle_work(AGENTIC_SOCIAL_MIN_CYCLE_ADVANCES)],
    )
    assert _should_post_agentic_social(NOW, state)


def test_partial_cycle_progress_still_blocked():
    state = _state(
        last_social_minutes_ago=AGENTIC_SOCIAL_INTERVAL_MINUTES + 30,
        records=[_social(), *_cycle_work(AGENTIC_SOCIAL_MIN_CYCLE_ADVANCES - 1)],
    )
    assert not _should_post_agentic_social(NOW, state)


def test_interstitial_legs_do_not_count_as_progress():
    """replenish/trigger/collect legs consume an iteration but not a cycle slot."""
    noise = [
        TaskRecord(
            task="replenish-queue", task_type="replenish-queue",
            date="2026-09-01", outcome="success", kind="replenish",
        )
        for _ in range(6)
    ]
    state = _state(
        last_social_minutes_ago=AGENTIC_SOCIAL_INTERVAL_MINUTES + 30,
        records=[_social(), *noise],
    )
    assert not _should_post_agentic_social(NOW, state)


def test_stall_valve_posts_when_cycle_is_wedged():
    """A stalled cycle must not starve social indefinitely either."""
    state = _state(
        last_social_minutes_ago=AGENTIC_SOCIAL_MAX_STALL_MINUTES + 1,
        records=[_social()],
    )
    assert _should_post_agentic_social(NOW, state)


def test_social_aged_out_of_ring_falls_back_to_time_gate():
    state = _state(
        last_social_minutes_ago=AGENTIC_SOCIAL_INTERVAL_MINUTES + 5,
        records=_cycle_work(3),
    )
    assert _should_post_agentic_social(NOW, state)


def test_legacy_records_without_kind_do_not_count_as_progress():
    """Records written before `kind` existed load as None; be conservative."""
    legacy = [
        TaskRecord(
            task="deep-review", task_type="deep-review",
            date="2026-09-01", outcome="success",
        )
        for _ in range(8)
    ]
    state = _state(
        last_social_minutes_ago=AGENTIC_SOCIAL_INTERVAL_MINUTES + 30,
        records=[_social(), *legacy],
    )
    assert not _should_post_agentic_social(NOW, state)


def test_suspension_backoff_wins_over_everything():
    state = _state(
        last_social_minutes_ago=AGENTIC_SOCIAL_MAX_STALL_MINUTES + 100,
        records=[_social(), *_cycle_work(20)],
    )
    state.last_runs["agentic-social-suspended-until"] = NOW + timedelta(hours=2)
    assert not _should_post_agentic_social(NOW, state)
