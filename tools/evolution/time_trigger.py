"""Wall-clock gating for time-triggered evolution skills.

The cron `/loop`s ("/loop 0 2 * * * /unfin-commission-chatgpt-review", etc.)
fire when the wall clock matches. This module performs the *additional*
gating that the Python loop currently does — automation-window check,
"already ran today" check, in-flight check, failure cooldown, login
backoff — and prints a JSON decision the wrapper skill consumes.

Output schema:

    {"action": "invoke", "skill": "<content-skill>", "args": "", "chrome": true|false}
    {"action": "skip",   "reason": "<one-line reason>"}

Recognized trigger names (passed via --name):

  commission-chatgpt-review
  commission-claude-review
  commission-gemini-review
  literature-drift-review
  add-highlight-tweet
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.evolution.state import load_state  # noqa: E402

STATE_PATH = REPO_ROOT / "obsidian" / "workflow" / "evolution-state.yaml"

# Mirror evolve_loop.py constants.
TWEET_HOUR_UTC = 8
LITERATURE_DRIFT_WEEKDAY = 1  # Tuesday (Mon=0)
LITERATURE_DRIFT_HOUR_UTC = 5
AUTOMATION_WINDOW_START_HOUR_UTC = 0
AUTOMATION_LAST_START_HOUR_UTC = 7


def _emit_invoke(skill: str, args: str = "", chrome: bool = False) -> None:
    payload = {"action": "invoke", "skill": skill, "args": args}
    if chrome:
        payload["chrome"] = True
    print(json.dumps(payload), flush=True)


def _emit_skip(reason: str) -> None:
    print(json.dumps({"action": "skip", "reason": reason}), flush=True)


def _is_automation_window(now: datetime) -> bool:
    return AUTOMATION_WINDOW_START_HOUR_UTC <= now.hour < AUTOMATION_LAST_START_HOUR_UTC


def _decide_commission(service_short: str, now: datetime, state) -> None:
    """Gate one commission-* trigger. Mirrors _due_for_commission()."""
    try:
        from tools.reviews.services import SERVICES
    except Exception as e:
        _emit_skip(f"outer-review module unavailable: {e}")
        return

    svc = next((s for s in SERVICES if s.service == service_short), None)
    if svc is None:
        _emit_skip(f"unknown commission service: {service_short}")
        return

    if not _is_automation_window(now):
        _emit_skip("outside automation window")
        return

    blocked_until = state.last_runs.get(f"{svc.skill_commission}-blocked-until")
    if blocked_until is not None and now < blocked_until:
        _emit_skip(f"login backoff active until {blocked_until.isoformat()}")
        return

    if now.hour < svc.commission_hour_utc:
        _emit_skip(f"commission hour not yet reached ({now.hour} < {svc.commission_hour_utc})")
        return

    last_run = state.last_runs.get(svc.skill_commission)
    if last_run is not None and last_run.date() == now.date():
        _emit_skip("already commissioned today")
        return

    try:
        from tools.reviews.pending import find_recent_failed, has_in_flight
    except Exception as e:
        _emit_skip(f"outer-review module unavailable: {e}")
        return

    if has_in_flight(svc.service):
        _emit_skip("commission already in flight")
        return

    if find_recent_failed(svc.service, now, cooldown_hours=1):
        _emit_skip("recent failure — within 1h cooldown")
        return

    _emit_invoke(svc.skill_commission, chrome=True)


def _decide_literature_drift(now: datetime, state) -> None:
    """Tue ≥05:00 UTC, once per Tuesday."""
    if now.weekday() != LITERATURE_DRIFT_WEEKDAY:
        _emit_skip(f"not Tuesday (weekday={now.weekday()})")
        return
    if now.hour < LITERATURE_DRIFT_HOUR_UTC:
        _emit_skip(f"before {LITERATURE_DRIFT_HOUR_UTC}:00 UTC")
        return
    last_run = state.last_runs.get("literature-drift-review")
    if last_run is not None and last_run.date() == now.date():
        _emit_skip("already ran today")
        return
    _emit_invoke("literature-drift-review")


def _decide_add_highlight_tweet(now: datetime, state) -> None:
    """≥08:00 UTC, once per day, only if highlight candidate exists."""
    if now.hour < TWEET_HOUR_UTC:
        _emit_skip(f"before {TWEET_HOUR_UTC}:00 UTC")
        return
    today = now.date().isoformat()
    if state.last_tweet_date == today:
        _emit_skip("already tweeted today")
        return
    # Defer candidate selection to the underlying skill — the skill itself
    # can search recent_tasks and the unhighlighted backlog. We just gate
    # on time-of-day + already-tweeted.
    _emit_invoke("add-highlight", args="--tweet")


def main() -> int:
    parser = argparse.ArgumentParser(description="Wall-clock gating for time-triggered skills.")
    parser.add_argument(
        "--name",
        required=True,
        help=(
            "Trigger name: commission-{chatgpt,claude,gemini}-review | "
            "literature-drift-review | add-highlight-tweet"
        ),
    )
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    state = load_state(STATE_PATH)

    name = args.name
    if name == "commission-chatgpt-review":
        _decide_commission("chatgpt", now, state)
    elif name == "commission-claude-review":
        _decide_commission("claude", now, state)
    elif name == "commission-gemini-review":
        _decide_commission("gemini", now, state)
    elif name == "literature-drift-review":
        _decide_literature_drift(now, state)
    elif name == "add-highlight-tweet":
        _decide_add_highlight_tweet(now, state)
    else:
        _emit_skip(f"unknown trigger name: {name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
