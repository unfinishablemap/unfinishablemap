#!/usr/bin/env python3
"""
Cycle-based evolution loop for The Unfinishable Map.

Runs tasks in a deterministic cycle. Speed is controlled by --interval.
The cycle ensures consistent task ratios regardless of speed.

Two scheduling layers:
1. Time-triggered: tweet-highlight at 7am UTC (wall clock)
2. Cycle-triggered: everything else follows the repeating task cycle
"""

import argparse
import logging
import subprocess
import sys
import time
from datetime import date, datetime, timezone
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
    SkillInvocation,
    count_p0_p2_tasks,
    load_todo,
    select_queue_task,
    task_to_skill,
)

# Module-level logger
log = logging.getLogger("evolve_loop")

# Repository root
REPO_ROOT = Path(__file__).parent.parent
STATE_PATH = REPO_ROOT / "obsidian" / "workflow" / "evolution-state.yaml"
CHANGELOG_PATH = REPO_ROOT / "obsidian" / "workflow" / "changelog.md"

# Tweet time (7am UTC)
TWEET_HOUR_UTC = 7

# Minimum P0-P2 tasks before replenishment
MIN_QUEUE_TASKS = 3


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


class SkillTimeout(Exception):
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

    # 2. Build Hugo
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
) -> tuple[bool, str]:
    """Run a skill via Claude CLI.

    Returns:
        Tuple of (success: bool, output: str)
    """
    prompt = invocation.to_prompt()
    log.info(f"Invoking: {prompt}")

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
        raise SkillTimeout(invocation.skill, timeout_seconds)

    output = result.stdout
    if result.stderr:
        output += "\n--- stderr ---\n" + result.stderr

    success = result.returncode == 0
    return success, output


# -----------------------------------------------------------------------------
# Time-triggered tasks
# -----------------------------------------------------------------------------


def should_tweet(now: datetime, state: EvolutionState) -> bool:
    """Check if we should run tweet-highlight.

    Tweets once per day at/after 7am UTC.
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

    # 1. Time-triggered: Tweet at 7am
    if should_tweet(now, state):
        log.info(f"Tweet-highlight triggered ({now.hour}:00 UTC)")
        try:
            success, output = run_skill(
                SkillInvocation("tweet-highlight"),
                timeout_seconds=timeout,
                verbose=verbose,
            )
            if success:
                state.last_tweet_date = now.date().isoformat()
                tasks_executed.append("tweet-highlight")
                log.info("Tweet-highlight completed")
            else:
                log.warning("Tweet-highlight failed (non-fatal)")
        except SkillTimeout:
            log.warning("Tweet-highlight timed out (non-fatal)")

    # 2. Queue health check
    p0_p2_count = count_p0_p2_tasks(todo_content)
    if p0_p2_count < MIN_QUEUE_TASKS:
        log.info(f"Queue low ({p0_p2_count} tasks), running replenish-queue")
        try:
            success, output = run_skill(
                SkillInvocation("replenish-queue"),
                timeout_seconds=timeout,
                verbose=verbose,
            )
            if success:
                tasks_executed.append("replenish-queue")
                todo_content = load_todo()  # Reload
        except (SkillTimeout, Exception) as e:
            log.warning(f"Replenish-queue failed: {e}")

    # 3. Run next task in cycle
    cycle_stats = get_cycle_stats(state.cycle_position)
    task_type = get_cycle_task(state.cycle_position)

    log.info(
        f"Cycle position {cycle_stats['position_in_cycle']}/{CYCLE_LENGTH} "
        f"(cycle {cycle_stats['cycles_completed'] + 1})"
    )
    log.info(f"Task type: {task_type}")

    if task_type == "queue":
        # Pick from todo queue
        task = select_queue_task(todo_content)
        if task:
            invocation = task_to_skill(task)
            log.info(f"Queue task: P{task.priority} {task.title}")
        else:
            log.info("No pending queue tasks, running deep-review instead")
            invocation = SkillInvocation("deep-review")
    else:
        # Run the scheduled skill
        invocation = SkillInvocation(task_type)

    try:
        success, output = run_skill(
            invocation,
            timeout_seconds=timeout,
            verbose=verbose,
        )

        task_name = f"{invocation.skill}"
        if invocation.args:
            task_name += f" ({invocation.args[:50]})"

        if success:
            tasks_executed.append(task_name)
            log.info(f"Task completed: {task_name}")

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

    except SkillTimeout:
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
                )
                if success:
                    tasks_executed.append(trigger_task)
                    state.last_runs[trigger_task] = now
            except (SkillTimeout, Exception) as e:
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
