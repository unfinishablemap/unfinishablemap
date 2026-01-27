#!/usr/bin/env python3
"""
Cycle-based evolution loop for The Unfinishable Map.

Runs tasks in a deterministic cycle. Speed is controlled by --interval.
The cycle ensures consistent task ratios regardless of speed.

Two scheduling layers:
1. Time-triggered: add-highlight-tweet at 8am UTC (wall clock)
2. Cycle-triggered: everything else follows the repeating task cycle
"""

import argparse
import logging
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.evolution.cycle import (
    CYCLE_LENGTH,
    describe_cycle,
    get_cycle_stats,
    get_cycle_task,
    get_cycle_triggers,
    is_cycle_complete,
)
from tools.evolution.state import EvolutionState, TaskRecord, load_state, save_state
from tools.evolution.task_selector import (
    LogicFlawError,
    SkillInvocation,
    count_p0_p2_tasks,
    load_todo,
    mark_task_completed,
    select_queue_task,
    task_to_skill,
)

# Module-level logger
log = logging.getLogger("evolve_loop")

# Repository root
REPO_ROOT = Path(__file__).parent.parent
STATE_PATH = REPO_ROOT / "obsidian" / "workflow" / "evolution-state.yaml"
CHANGELOG_PATH = REPO_ROOT / "obsidian" / "workflow" / "changelog.md"

# Add-and-tweet time (8am UTC)
TWEET_HOUR_UTC = 8

# Minimum P0-P2 tasks before replenishment
MIN_QUEUE_TASKS = 3

# Agent author for automated commits
AGENT_AUTHOR = "unfinishablemap.org Agent <agent@unfinishablemap.org>"


class GitError(Exception):
    """Raised when a git command fails."""

    def __init__(self, command: str, returncode: int, stdout: str, stderr: str):
        self.command = command
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        super().__init__(f"Git command failed: {command}")


class SkillError(Exception):
    """Raised when a skill invocation fails."""

    def __init__(self, skill: str, returncode: int, stdout: str, stderr: str):
        self.skill = skill
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        super().__init__(f"Skill {skill} failed with exit code {returncode}")


class SkillTimeoutError(Exception):
    """Raised when a skill invocation times out."""

    def __init__(self, skill: str, timeout_seconds: int):
        self.skill = skill
        self.timeout_seconds = timeout_seconds
        super().__init__(f"Skill {skill} timed out after {timeout_seconds}s")


def setup_logging(log_file: Path) -> None:
    """Configure logging with console and rotating file handlers."""
    log.setLevel(logging.INFO)

    # Console handler
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(message)s"))
    log.addHandler(console)

    # Daily rotating file handler
    file_handler = TimedRotatingFileHandler(
        log_file,
        when="midnight",
        backupCount=0,
        encoding="utf-8",
    )
    file_handler.suffix = "%Y-%m-%d"
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    )
    log.addHandler(file_handler)


def format_duration(seconds: float) -> str:
    """Format seconds as human-readable duration."""
    if seconds < 60:
        return f"{seconds:.0f}s"
    elif seconds < 3600:
        return f"{seconds / 60:.1f}m"
    else:
        return f"{seconds / 3600:.1f}h"


# -----------------------------------------------------------------------------
# Git operations
# -----------------------------------------------------------------------------


def get_unpushed_commits() -> int:
    """Count commits ahead of origin."""
    result = subprocess.run(
        ["git", "rev-list", "--count", "@{u}..HEAD"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        raise GitError(
            "git rev-list --count @{u}..HEAD",
            result.returncode,
            result.stdout,
            result.stderr,
        )
    return int(result.stdout.strip())


def git_push() -> None:
    """Push to origin."""
    result = subprocess.run(
        ["git", "push"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        raise GitError("git push", result.returncode, result.stdout, result.stderr)


def has_uncommitted_changes() -> bool:
    """Check if there are uncommitted changes (staged or unstaged)."""
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    return bool(result.stdout.strip())


def commit_as_agent(skill_name: str, task_info: str | None = None) -> str | None:
    """Commit any uncommitted changes with agent authorship.

    Args:
        skill_name: Name of the skill that made the changes
        task_info: Optional additional context (e.g., file reviewed)

    Returns:
        Commit hash if a commit was made, None otherwise
    """
    if not has_uncommitted_changes():
        return None

    # Stage all changes
    result = subprocess.run(
        ["git", "add", "-A"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        raise GitError("git add -A", result.returncode, result.stdout, result.stderr)

    # Build commit message
    if task_info:
        message = f"auto({skill_name}): {task_info}"
    else:
        message = f"auto({skill_name}): Automated execution"

    # Commit with agent author
    result = subprocess.run(
        ["git", "commit", "--author", AGENT_AUTHOR, "-m", message],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        # Check if it's just "nothing to commit"
        if "nothing to commit" in result.stdout:
            return None
        raise GitError("git commit", result.returncode, result.stdout, result.stderr)

    # Get commit hash
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    return result.stdout.strip()[:8] if result.returncode == 0 else None


# -----------------------------------------------------------------------------
# Validation (runs before push)
# -----------------------------------------------------------------------------


def run_pre_push_validation() -> bool:
    """Run validation before pushing. Returns True if safe to push."""
    log.info("Running pre-push validation...")

    # 1. Sync Obsidian to Hugo
    result = subprocess.run(
        ["uv", "run", "python", "scripts/sync.py"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        log.error(f"Sync failed: {result.stderr}")
        return False

    # 2. Commit any synced files (hugo/ files created by sync)
    # This fixes the bug where sync creates hugo/ files but they're never committed
    if has_uncommitted_changes():
        try:
            commit_hash = commit_as_agent("sync", "Sync obsidian → hugo")
            if commit_hash:
                log.info(f"Committed synced files: {commit_hash}")
        except GitError as e:
            log.warning(f"Failed to commit synced files: {e}")
            # Continue anyway - validation can still pass

    # 3. Build Hugo
    result = subprocess.run(
        ["hugo", "--gc", "--minify"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT / "hugo",
    )
    if result.returncode != 0:
        log.error(f"Hugo build failed: {result.stderr}")
        return False

    log.info("Validation passed")
    return True


# -----------------------------------------------------------------------------
# Skill invocation
# -----------------------------------------------------------------------------


def run_skill(
    invocation: SkillInvocation,
    timeout_seconds: int = 5400,
    verbose: bool = True,
    skip_commit: bool = False,
) -> tuple[bool, str]:
    """Run a skill via Claude CLI.

    Args:
        invocation: The skill to invoke
        timeout_seconds: Maximum time to wait
        verbose: Whether to use verbose Claude output
        skip_commit: If True, append instruction to skip git commit

    Returns:
        Tuple of (success: bool, output: str)
    """
    prompt = invocation.to_prompt()
    if skip_commit:
        prompt += (
            " IMPORTANT: Do NOT create a git commit. "
            "Leave changes uncommitted - the automation system will handle committing."
        )

    # Show timestamp for monitoring hung executions
    now = datetime.now(timezone.utc)
    log.info(f"[{now.strftime('%Y-%m-%d %H:%M:%S')} UTC] Invoking: {prompt}")

    cmd = [
        "claude",
        "--dangerously-skip-permissions",
        "--output-format", "text",
    ]
    if verbose:
        cmd.append("--verbose")
    cmd.extend(["-p", prompt])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired:
        raise SkillTimeoutError(invocation.skill, timeout_seconds)

    output = result.stdout
    if result.stderr:
        output += "\n--- stderr ---\n" + result.stderr

    success = result.returncode == 0
    return success, output


def run_agent_commit(
    skill_name: str,
    skill_output: str,
    timeout_seconds: int = 300,
    verbose: bool = False,
) -> str | None:
    """Run the agent-commit skill to create a meaningful commit.

    Args:
        skill_name: Name of the skill that made the changes
        skill_output: Output from the skill (will be truncated if too long)
        timeout_seconds: Maximum time to wait for commit skill
        verbose: Whether to use verbose Claude output

    Returns:
        Commit hash if a commit was made, None otherwise
    """
    if not has_uncommitted_changes():
        return None

    start_time = time.time()
    start_ts = datetime.now(timezone.utc)

    # Truncate output to avoid overwhelming the commit skill
    max_output_chars = 2000
    output_summary = skill_output[:max_output_chars]
    if len(skill_output) > max_output_chars:
        output_summary += f"\n... (truncated, {len(skill_output)} total chars)"

    # Build prompt for agent-commit skill
    prompt = (
        f"Run the agent-commit skill. "
        f"Previous skill: {skill_name}. "
        f"Output summary:\n{output_summary}"
    )

    log.info(
        f"[{start_ts.strftime('%Y-%m-%d %H:%M:%S')} UTC] "
        f"Running agent-commit for {skill_name}..."
    )

    cmd = [
        "claude",
        "--dangerously-skip-permissions",
        "--output-format", "text",
    ]
    if verbose:
        cmd.append("--verbose")
    cmd.extend(["-p", prompt])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired:
        duration = time.time() - start_time
        log.warning(
            f"agent-commit timed out after {timeout_seconds}s "
            f"(elapsed: {format_duration(duration)})"
        )
        # Fall back to simple commit
        return commit_as_agent(skill_name)

    duration = time.time() - start_time
    end_ts = datetime.now(timezone.utc)

    if result.returncode != 0:
        log.warning(
            f"[{end_ts.strftime('%Y-%m-%d %H:%M:%S')} UTC] "
            f"agent-commit failed after {format_duration(duration)}: {result.stderr[:200]}"
        )
        # Fall back to simple commit
        return commit_as_agent(skill_name)

    log.info(
        f"[{end_ts.strftime('%Y-%m-%d %H:%M:%S')} UTC] "
        f"agent-commit completed in {format_duration(duration)}"
    )

    # Extract commit hash from output (skill should output it)
    # Look for a short hash pattern in the output
    hash_match = re.search(r"\b([0-9a-f]{7,8})\b", result.stdout)
    if hash_match:
        return hash_match.group(1)

    # Check if a commit was actually made
    check_result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    return check_result.stdout.strip()[:8] if check_result.returncode == 0 else None


# -----------------------------------------------------------------------------
# Time-triggered tasks
# -----------------------------------------------------------------------------

# Task types worth highlighting
HIGHLIGHT_WORTHY = {
    "expand-topic",
    "research-topic",
    "research-voids",
    "deep-review",
    "coalesce",
    "apex-evolve",
}

# Task types to skip for highlighting
HIGHLIGHT_SKIP = {
    "validate-all",
    "check-links",
    "check-tenets",
    "condense",
    "replenish-queue",
    "tweet-highlight",
    "add-highlight",
}


def find_highlight_candidate(
    recent_tasks: list[TaskRecord], today: str
) -> TaskRecord | None:
    """Find highlight-worthy work from today's successful tasks.

    Args:
        recent_tasks: List of recent task records
        today: ISO date string for today

    Returns:
        TaskRecord to highlight, or None if nothing worthy found.
    """
    for task in reversed(recent_tasks):  # Most recent first
        if task.date != today:
            continue
        if task.outcome != "success":
            continue
        if task.task_type in HIGHLIGHT_SKIP:
            continue
        if task.task_type in HIGHLIGHT_WORTHY:
            return task

    return None


def should_add_and_tweet(now: datetime, state: EvolutionState) -> bool:
    """Check if we should run add-highlight with tweet.

    Runs once per day at/after 8am UTC.
    """
    if now.hour < TWEET_HOUR_UTC:
        return False

    today = now.date().isoformat()
    return state.last_tweet_date != today


# -----------------------------------------------------------------------------
# Main loop
# -----------------------------------------------------------------------------


def run_session(
    state: EvolutionState,
    now: datetime,
    verbose: bool = True,
    timeout: int = 5400,
) -> tuple[EvolutionState, list[str]]:
    """Run a single evolution session.

    Returns:
        Updated state and list of tasks executed
    """
    tasks_executed = []
    todo_content = load_todo()

    # 1. Time-triggered: Add highlight and tweet at 8am UTC
    today = now.date().isoformat()
    if should_add_and_tweet(now, state):
        log.info(f"Add-and-tweet triggered ({now.hour}:00 UTC)")
        candidate = find_highlight_candidate(state.recent_tasks, today)
        if candidate:
            log.info(f"Highlight candidate: {candidate.task_type} - {candidate.task}")
            try:
                # Pass task info to skill - Claude will read file and compose highlight
                # The --tweet flag triggers: add → commit → push → wait for deploy → tweet
                success, output = run_skill(
                    SkillInvocation(
                        "add-highlight",
                        f"--from-task '{candidate.task_type}: {candidate.task}' --tweet",
                    ),
                    timeout_seconds=600,  # 10 min for push+deploy+tweet
                    verbose=verbose,
                )
                if success:
                    state.last_tweet_date = today
                    tasks_executed.append("add-highlight-tweet")
                    log.info("Add-and-tweet completed")
                else:
                    log.warning("Add-and-tweet failed (non-fatal)")
                    state.last_tweet_date = today  # Don't retry today
            except SkillTimeoutError:
                log.warning("Add-and-tweet timed out (non-fatal)")
                state.last_tweet_date = today  # Don't retry today
        else:
            log.info("No highlight-worthy work found today")
            state.last_tweet_date = today  # Don't retry today

    # 2. Queue health check
    p0_p2_count = count_p0_p2_tasks(todo_content)
    if p0_p2_count < MIN_QUEUE_TASKS:
        log.info(f"Queue low ({p0_p2_count} tasks), running replenish-queue")
        try:
            success, output = run_skill(
                SkillInvocation("replenish-queue"),
                timeout_seconds=timeout,
                verbose=verbose,
                skip_commit=True,
            )
            if success:
                tasks_executed.append("replenish-queue")
                todo_content = load_todo()  # Reload
                # Commit any changes with agent authorship
                try:
                    commit_hash = run_agent_commit("replenish-queue", output)
                    if commit_hash:
                        log.info(f"Committed as agent: {commit_hash}")
                except (GitError, Exception) as e:
                    log.warning(f"Failed to commit: {e}")
        except (SkillTimeoutError, Exception) as e:
            log.warning(f"Replenish-queue failed: {e}")

    # 3. Run next task in cycle
    cycle_stats = get_cycle_stats(state.cycle_position)
    task_type = get_cycle_task(state.cycle_position)

    log.info(
        f"Cycle position {cycle_stats['position_in_cycle']}/{CYCLE_LENGTH} "
        f"(cycle {cycle_stats['cycles_completed'] + 1})"
    )
    log.info(f"Task type: {task_type}")

    queue_task = None  # Track if this is a queue task for completion marking
    invocation = None  # None means skip this cycle slot
    if task_type == "queue":
        # Pick from todo queue (only executable tasks by default)
        queue_task = select_queue_task(todo_content)
        if queue_task:
            try:
                invocation = task_to_skill(queue_task)
                log.info(f"Queue task: P{queue_task.priority} {queue_task.title}")
            except LogicFlawError as e:
                # Task type not mapped - skip this slot entirely
                log.warning(f"Cannot execute queue task (skipping slot): {e}")
                queue_task = None
                invocation = None
        else:
            # No executable tasks in queue - skip this slot
            log.info("No executable queue tasks, skipping this cycle slot")
            invocation = None
    else:
        # Run the scheduled skill
        invocation = SkillInvocation(task_type)

    # Skip execution if no invocation (e.g., no executable queue tasks)
    if invocation is None:
        log.info("No task to execute, advancing cycle position")
        state.cycle_position += 1
        save_state(state, STATE_PATH)
        return state, tasks_executed

    try:
        success, output = run_skill(
            invocation,
            timeout_seconds=timeout,
            verbose=verbose,
            skip_commit=True,  # We'll commit with agent authorship below
        )

        task_name = f"{invocation.skill}"
        if invocation.args:
            task_name += f" ({invocation.args[:50]})"

        if success:
            tasks_executed.append(task_name)
            log.info(f"Task completed: {task_name}")

            # Mark queue task as completed in todo.md
            if queue_task:
                try:
                    mark_task_completed(queue_task, invocation.args)
                    log.info(f"Marked task completed in todo.md: {queue_task.title}")
                except Exception as e:
                    log.warning(f"Failed to mark task completed: {e}")

            # Commit any changes with agent authorship
            try:
                commit_hash = run_agent_commit(invocation.skill, output)
                if commit_hash:
                    log.info(f"Committed as agent: {commit_hash}")
            except (GitError, Exception) as e:
                log.warning(f"Failed to commit: {e}")

            # Record in recent_tasks
            state.recent_tasks.append(
                TaskRecord(
                    task=task_name,
                    task_type=invocation.skill,
                    date=now.date().isoformat(),
                    outcome="success",
                )
            )
            # Keep only last 50
            state.recent_tasks = state.recent_tasks[-50:]
        else:
            log.error(f"Task failed: {task_name}")
            state.recent_tasks.append(
                TaskRecord(
                    task=task_name,
                    task_type=invocation.skill,
                    date=now.date().isoformat(),
                    outcome="failed",
                )
            )

        # Log output summary
        output_lines = output.strip().split("\n")
        if len(output_lines) > 30:
            log.info(f"Output ({len(output_lines)} lines, showing last 30):")
            for line in output_lines[-30:]:
                log.info(f"  {line}")
        else:
            for line in output_lines:
                log.info(f"  {line}")

    except SkillTimeoutError:
        log.error(f"Task timed out: {invocation.skill}")
        state.recent_tasks.append(
            TaskRecord(
                task=invocation.skill,
                task_type=invocation.skill,
                date=now.date().isoformat(),
                outcome="timeout",
            )
        )

    # Increment cycle position
    state.cycle_position += 1

    # 4. Check cycle-completion triggers
    if is_cycle_complete(state.cycle_position):
        cycles_completed = state.cycle_position // CYCLE_LENGTH
        log.info(f"Cycle {cycles_completed} complete!")

        triggers = get_cycle_triggers(cycles_completed)
        for trigger_task in triggers:
            log.info(f"Running cycle trigger: {trigger_task}")
            try:
                success, output = run_skill(
                    SkillInvocation(trigger_task),
                    timeout_seconds=timeout,
                    verbose=verbose,
                    skip_commit=True,
                )
                if success:
                    tasks_executed.append(trigger_task)
                    state.last_runs[trigger_task] = now
                    # Commit any changes with agent authorship
                    try:
                        commit_hash = run_agent_commit(trigger_task, output)
                        if commit_hash:
                            log.info(f"Committed as agent: {commit_hash}")
                    except (GitError, Exception) as e:
                        log.warning(f"Failed to commit: {e}")
            except (SkillTimeoutError, Exception) as e:
                log.warning(f"Cycle trigger {trigger_task} failed: {e}")

    # Update state
    state.last_updated = now
    state.session_count += 1

    return state, tasks_executed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cycle-based evolution loop",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Speed is controlled by --interval. The task cycle ensures consistent ratios.

Examples:
  Fast (testing):     --interval 600   (10 min, ~144 sessions/day)
  Normal:             --interval 2400  (40 min, ~36 sessions/day)
  Slow (low budget):  --interval 14400 (4 hours, ~6 sessions/day)
""",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=2400,
        help="Seconds between sessions (default: 2400 = 40 minutes)",
    )
    parser.add_argument(
        "--push-interval",
        type=int,
        default=14400,
        help="Minimum seconds between git pushes (default: 14400 = 4 hours)",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=0,
        help="Stop after N sessions (0 = unlimited)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=5400,
        help="Skill timeout in seconds (default: 5400 = 90 minutes)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Reduce Claude output verbosity",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        default=Path(__file__).parent.parent.parent
        / "unfinishablemap_log"
        / "evolve_loop.log",
        help="Log file path",
    )
    parser.add_argument(
        "--describe-cycle",
        action="store_true",
        help="Print cycle description and exit",
    )
    args = parser.parse_args()

    if args.describe_cycle:
        print(describe_cycle())
        return 0

    # Ensure log directory exists
    args.log_file.parent.mkdir(parents=True, exist_ok=True)
    setup_logging(args.log_file)

    # Stats tracking
    iterations = 0
    successes = 0
    failures = 0
    start_time = time.time()

    # Load initial state
    state = load_state(STATE_PATH)

    log.info("=" * 60)
    log.info("Evolution Loop Started (Cycle-Based)")
    log.info("=" * 60)
    log.info(f"  Session interval: {format_duration(args.interval)}")
    log.info(f"  Push interval: {format_duration(args.push_interval)}")
    log.info(f"  Max iterations: {args.max_iterations or 'unlimited'}")
    log.info(f"  Starting cycle position: {state.cycle_position}")
    log.info(f"  Log file: {args.log_file}")
    log.info("")
    log.info(describe_cycle())
    log.info("=" * 60)

    try:
        while True:
            if args.max_iterations and iterations >= args.max_iterations:
                log.info(f"Reached max iterations ({args.max_iterations})")
                break

            iterations += 1
            session_start = time.time()
            now = datetime.now(timezone.utc)

            log.info("")
            log.info("-" * 60)
            log.info(f"Session {iterations} | {now.strftime('%Y-%m-%d %H:%M:%S')} UTC")
            log.info(f"Stats: {successes} succeeded, {failures} failed")
            log.info(f"Runtime: {format_duration(time.time() - start_time)}")
            log.info("-" * 60)

            # Run session
            try:
                state, tasks_executed = run_session(
                    state,
                    now,
                    verbose=not args.quiet,
                    timeout=args.timeout,
                )

                if tasks_executed:
                    successes += 1
                    log.info(f"Session complete. Tasks: {', '.join(tasks_executed)}")
                else:
                    failures += 1
                    log.warning("Session complete with no tasks executed")

            except Exception as e:
                failures += 1
                log.exception(f"Session failed: {e}")

            # 5. Push on wall-clock interval
            try:
                unpushed = get_unpushed_commits()
                if unpushed > 0:
                    last_push = state.last_git_push
                    if last_push:
                        seconds_since_push = (now - last_push).total_seconds()
                    else:
                        seconds_since_push = float("inf")

                    if seconds_since_push >= args.push_interval:
                        log.info(f"Push check: {unpushed} commits, validating...")
                        if run_pre_push_validation():
                            log.info("Pushing...")
                            git_push()
                            state.last_git_push = now
                            log.info("Push complete")
                        else:
                            log.warning("Validation failed, skipping push")
                    else:
                        remaining = args.push_interval - seconds_since_push
                        log.info(
                            f"{unpushed} unpushed, next push in {format_duration(remaining)}"
                        )
            except GitError as e:
                log.warning(f"Git operation failed: {e.command}")

            # Save state after each session
            save_state(state, STATE_PATH)

            # Sleep until next session
            session_duration = time.time() - session_start
            sleep_seconds = max(0, args.interval - session_duration)

            if sleep_seconds > 0:
                log.info(f"Sleeping {format_duration(sleep_seconds)}...")
                time.sleep(sleep_seconds)

    except KeyboardInterrupt:
        log.info("Interrupted by user")

    # Final stats
    log.info("")
    log.info("=" * 60)
    log.info("Evolution Loop Summary")
    log.info("=" * 60)
    log.info(f"  Total sessions: {iterations}")
    log.info(f"  Succeeded: {successes}")
    log.info(f"  Failed: {failures}")
    if iterations:
        log.info(f"  Success rate: {successes / iterations * 100:.0f}%")
    log.info(f"  Total runtime: {format_duration(time.time() - start_time)}")
    log.info(f"  Final cycle position: {state.cycle_position}")

    # Final push
    try:
        unpushed = get_unpushed_commits()
        if unpushed > 0:
            log.info(f"Final push ({unpushed} commits)...")
            if run_pre_push_validation():
                git_push()
                state.last_git_push = datetime.now(timezone.utc)
                save_state(state, STATE_PATH)
                log.info("Final push complete")
    except GitError:
        pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
