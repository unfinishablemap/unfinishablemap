"""Post-task state update for the /loop-driven evolution orchestrator.

Called by the `/unfin-cycle` skill after a per-task skill has run.
Mutates `evolution-state.yaml`, `obsidian/workflow/todo.md`,
`.unfin/pending-triggers.json`, runs the anchoring audit at cycle
completion, creates a git commit for any uncommitted changes, and
appends a line to the rotating log.

Mirrors the post-task behaviour of `scripts/evolve_loop.py:run_session`.

Usage:

    uv run python -m tools.evolution.cycle_post \\
        --kind queue --skill refine-draft --status SUCCESS \\
        [--queue-task-line 42] [--note "free-form summary"]
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.evolution.cycle import (  # noqa: E402
    CYCLE_LENGTH,
    get_cycle_triggers,
    is_cycle_complete,
)
from tools.evolution.log_event import emit  # noqa: E402
from tools.evolution.state import (  # noqa: E402
    TaskRecord,
    load_state,
    save_state,
)
from tools.evolution.task_selector import (  # noqa: E402
    load_todo,
    mark_task_completed,
)
from tools.todo.processor import parse_tasks  # noqa: E402

STATE_PATH = REPO_ROOT / "obsidian" / "workflow" / "evolution-state.yaml"
TODO_PATH = REPO_ROOT / "obsidian" / "workflow" / "todo.md"
PENDING_TRIGGERS_PATH = REPO_ROOT / ".unfin" / "pending-triggers.json"

AGENT_AUTHOR = "unfinishablemap.org Agent <agent@unfinishablemap.org>"

# Kinds that consume one cycle slot (advance cycle_position).
CYCLE_CONSUMING_KINDS = {"queue", "cycle"}

# Backoff windows for sentinel-string fault modes (mirror evolve_loop.py).
AGENTIC_SOCIAL_SUSPENSION_BACKOFF_HOURS = 6
LOGIN_BACKOFF_HOURS = 24


def _has_uncommitted_changes() -> bool:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    return bool(result.stdout.strip())


def _commit_as_agent(skill: str, task_info: str | None) -> str | None:
    """Create a deterministic agent-authored commit for any uncommitted state."""
    if not _has_uncommitted_changes():
        return None

    add = subprocess.run(
        ["git", "add", "-A"], capture_output=True, text=True, cwd=REPO_ROOT
    )
    if add.returncode != 0:
        emit("warning", f"git add failed: {add.stderr.strip()}")
        return None

    message = f"auto({skill}): {task_info}" if task_info else f"auto({skill}): Automated execution"
    commit = subprocess.run(
        ["git", "commit", "--author", AGENT_AUTHOR, "-m", message],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if commit.returncode != 0:
        if "nothing to commit" in commit.stdout:
            return None
        emit("warning", f"git commit failed: {commit.stderr.strip()}")
        return None

    rev = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    return rev.stdout.strip()[:8] if rev.returncode == 0 else None


def _load_pending_triggers() -> list[str]:
    if not PENDING_TRIGGERS_PATH.is_file():
        return []
    import json
    try:
        data = json.loads(PENDING_TRIGGERS_PATH.read_text(encoding="utf-8"))
        return [str(t) for t in data] if isinstance(data, list) else []
    except Exception:
        return []


def _save_pending_triggers(triggers: list[str]) -> None:
    import json
    PENDING_TRIGGERS_PATH.parent.mkdir(parents=True, exist_ok=True)
    PENDING_TRIGGERS_PATH.write_text(json.dumps(triggers), encoding="utf-8")


def _detect_sentinels(note: str) -> tuple[bool, bool]:
    """Return (suspension_detected, login_required) flags from a free-form note."""
    n = note.lower()
    return ("suspension_detected" in n, "login_required" in n)


def _mark_queue_task_completed(line_number: int) -> str | None:
    """Mark the queue task at the given line as completed. Returns task title or None."""
    content = load_todo()
    parsed = parse_tasks(content)
    for task in parsed["active"]:
        if task.line_number == line_number:
            try:
                mark_task_completed(task)
            except Exception as e:
                emit("warning", f"mark_task_completed failed for line {line_number}: {e}")
                return None
            return task.title
    emit("warning", f"queue task at line {line_number} not found")
    return None


def _run_anchoring_audit_inplace(state, now: datetime) -> int | None:
    """In-process call to the Audit Three anchoring check.

    Returns the number of refine-draft tasks appended, or None if disabled.
    See scripts/evolve_loop.py:run_anchoring_audit for the reference.
    """
    try:
        from tools.curate.anchoring import format_refine_task, get_anchoring_flags
    except Exception as e:
        emit("warning", f"anchoring audit unavailable: {e}")
        return None

    config = state.audit_triple.get("topic_concept_anchoring", {})
    if not config:
        return None

    flags = get_anchoring_flags(
        REPO_ROOT / "obsidian",
        hedge_density_ratio=float(config.get("hedge_density_ratio", 0.6)),
        strong_assertion_ratio=float(config.get("strong_assertion_ratio", 1.5)),
        min_word_count=int(config.get("min_word_count", 400)),
    )

    if not TODO_PATH.is_file():
        return None
    body = TODO_PATH.read_text(encoding="utf-8")

    global_cap = int(state.audit_triple.get("global_task_cap", 6))
    open_audit_tasks = body.count("**Source**: topic-concept-anchoring-audit")
    open_audit_tasks += body.count("**Source**: literature-drift-audit")
    if open_audit_tasks >= global_cap:
        emit("info", f"anchoring audit skipped — cap reached ({open_audit_tasks}/{global_cap})")
        return 0

    new_flags = [
        f for f in flags
        if (
            f"### P2: Adopt {f.anchor_concept_path.stem} calibration in "
            f"{f.topic_path.stem}"
        ) not in body
    ]
    headroom = global_cap - open_audit_tasks
    per_run = int(config.get("max_tasks_per_run", 2))
    capped = new_flags[: min(per_run, headroom)]
    if not capped:
        config["total_audits"] = int(config.get("total_audits", 0)) + 1
        state.audit_triple["topic_concept_anchoring"] = config
        return 0

    today_iso = now.date().isoformat()
    blocks = [format_refine_task(f, today_iso) for f in capped]
    insertion = "\n".join(blocks) + "\n"
    if "## Active Tasks\n" not in body:
        return 0
    new_body = body.replace("## Active Tasks\n", "## Active Tasks\n\n" + insertion, 1)
    TODO_PATH.write_text(new_body, encoding="utf-8")

    config["total_audits"] = int(config.get("total_audits", 0)) + 1
    config["flagged_audits"] = int(config.get("flagged_audits", 0)) + len(capped)
    state.audit_triple["topic_concept_anchoring"] = config

    return len(blocks)


def main() -> int:
    parser = argparse.ArgumentParser(description="Post-task evolution-state update.")
    parser.add_argument(
        "--kind",
        required=True,
        help=(
            "Pick output kind: queue|cycle|trigger|replenish|collect|"
            "combine|agentic_social|commission"
        ),
    )
    parser.add_argument("--skill", required=True, help="Skill name that ran")
    parser.add_argument("--status", required=True, choices=["SUCCESS", "FAILURE", "TIMEOUT"],
                        help="Outcome of the skill invocation")
    parser.add_argument("--queue-task-line", type=int, default=None,
                        help="todo.md line number — set when kind==queue to mark completion")
    parser.add_argument("--note", default="",
                        help="Free-form summary text; scanned for sentinel markers")
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    state = load_state(STATE_PATH)

    success = args.status == "SUCCESS"
    outcome = {"SUCCESS": "success", "FAILURE": "failed", "TIMEOUT": "timeout"}[args.status]

    # --- Sentinel handling -------------------------------------------------
    suspended, login_required = _detect_sentinels(args.note)
    if args.kind == "agentic_social" and suspended:
        backoff_until = now + timedelta(hours=AGENTIC_SOCIAL_SUSPENSION_BACKOFF_HOURS)
        state.last_runs["agentic-social-suspended-until"] = backoff_until
        emit("warning",
             f"agentic-social suspension detected — backing off until {backoff_until.isoformat()}")
    if args.kind in ("collect", "commission") and login_required:
        backoff_until = now + timedelta(hours=LOGIN_BACKOFF_HOURS)
        # mirror evolve_loop.py: keyed by the commission skill name
        # (collect-side login also blocks the matching commission skill)
        commission_skill = args.skill.replace("collect-", "commission-")
        state.last_runs[f"{commission_skill}-blocked-until"] = backoff_until
        emit("warning",
             f"{args.skill} login required — backing off until {backoff_until.isoformat()}")

    # --- last_runs / recent_tasks ------------------------------------------
    state.last_runs[args.skill] = now

    # Day-stamp the tweet-once-per-day gate. Mirrors evolve_loop.py which
    # sets last_tweet_date on both success and failure paths so the cron
    # doesn't retry the tweet within the same day if the session restarts.
    if args.kind == "trigger" and args.skill in ("add-highlight", "add-highlight-tweet"):
        state.last_tweet_date = now.date().isoformat()

    task_record = TaskRecord(
        task=args.skill,
        task_type=args.skill,
        date=now.date().isoformat(),
        outcome=outcome,
    )
    state.recent_tasks.append(task_record)

    # --- Queue task completion ---------------------------------------------
    completed_title: str | None = None
    if args.kind == "queue" and success and args.queue_task_line is not None:
        completed_title = _mark_queue_task_completed(args.queue_task_line)
        if completed_title:
            emit(
                "info",
                f"marked todo task completed "
                f"(line {args.queue_task_line}): {completed_title}",
            )

    # --- Cycle-position bookkeeping ----------------------------------------
    cycle_complete_now = False
    cycles_completed = state.cycle_position // CYCLE_LENGTH
    if args.kind in CYCLE_CONSUMING_KINDS:
        state.cycle_position += 1
        if is_cycle_complete(state.cycle_position):
            cycle_complete_now = True
            cycles_completed = state.cycle_position // CYCLE_LENGTH

    # --- Cycle-completion triggers -----------------------------------------
    if cycle_complete_now:
        emit("info", f"cycle {cycles_completed} complete")
        # Anchoring audit gates on its own run_every_n_cycles config.
        every_n = int(
            state.audit_triple.get("topic_concept_anchoring", {}).get(
                "run_every_n_cycles", 1
            )
        )
        if every_n > 0 and cycles_completed % every_n == 0:
            try:
                added = _run_anchoring_audit_inplace(state, now)
                if added is None:
                    emit("info", "anchoring audit disabled (no config); skipped")
                elif added > 0:
                    emit("info", f"anchoring audit: appended {added} refine-draft task(s)")
                else:
                    emit("info", "anchoring audit: no new flags")
            except Exception as e:
                emit("warning", f"anchoring audit error (non-fatal): {e}")

        # Enqueue cycle-completion triggers for subsequent /loop iterations.
        triggers = get_cycle_triggers(cycles_completed)
        if triggers:
            existing = _load_pending_triggers()
            merged = existing + [t for t in triggers if t not in existing]
            _save_pending_triggers(merged)
            emit("info", f"enqueued cycle triggers: {triggers}")

    # --- Drain trigger from pending list when kind==trigger ---------------
    if args.kind == "trigger":
        pending = _load_pending_triggers()
        if args.skill in pending:
            pending.remove(args.skill)
            _save_pending_triggers(pending)

    # --- Save state --------------------------------------------------------
    state.last_updated = now
    state.session_count += 1
    save_state(state, STATE_PATH)

    # --- Commit any uncommitted changes -----------------------------------
    commit_info = completed_title or args.kind
    commit_hash = _commit_as_agent(args.skill, commit_info)
    if commit_hash:
        emit("info", f"committed: {commit_hash} (auto({args.skill}): {commit_info})")

    emit("info",
         f"cycle_post done: kind={args.kind} skill={args.skill} status={args.status} "
         f"cycle_position={state.cycle_position}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
