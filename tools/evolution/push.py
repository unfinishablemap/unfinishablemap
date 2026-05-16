"""Pre-push validation + git push for the /loop-driven orchestrator.

Mirrors the wall-clock push logic in `scripts/evolve_loop.py`:

    if unpushed_commits > 0 and seconds_since_last_push >= push_interval:
        run_workflow_archive()
        sync obsidian → hugo
        commit any sync changes
        build hugo
        git push
        record state.last_git_push

Called from `cycle_post.py` at the end of every iteration. The check is
cheap; the heavy work (sync + build + push) only runs when the wall-clock
interval has elapsed.

The Python loop in `scripts/evolve_loop.py` keeps its own copies of these
helpers for the fallback path; this module is the /loop-path equivalent.
"""

from __future__ import annotations

import subprocess
from datetime import datetime, timezone
from pathlib import Path

from tools.evolution.log_event import emit

REPO_ROOT = Path(__file__).parent.parent.parent

# Default push interval — mirrors evolve_loop.py --push-interval default
# (14400s = 4h). Overridable via UNFIN_PUSH_INTERVAL_SECONDS.
DEFAULT_PUSH_INTERVAL_SECONDS = 14400

AGENT_AUTHOR = "unfinishablemap.org Agent <agent@unfinishablemap.org>"


def _run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        **kwargs,
    )


def _has_uncommitted() -> bool:
    return bool(_run(["git", "status", "--porcelain"]).stdout.strip())


def get_unpushed_commits() -> int:
    """Count commits ahead of upstream. Returns 0 if no upstream configured."""
    result = _run(["git", "rev-list", "--count", "@{u}..HEAD"])
    if result.returncode != 0:
        emit("warning", f"could not count unpushed commits: {result.stderr.strip()}")
        return 0
    try:
        return int(result.stdout.strip())
    except ValueError:
        return 0


def _run_workflow_archive() -> None:
    """Archive old changelog/completed-task entries. Non-fatal on failure."""
    result = _run(
        ["uv", "run", "python", "scripts/archive_workflow.py", "--keep-weeks", "1"]
    )
    if result.returncode != 0:
        emit("warning", f"archive_workflow failed (non-fatal): {result.stderr.strip()}")


def _sync_obsidian_to_hugo() -> bool:
    """Run scripts/sync.py. Returns True on success."""
    result = _run(["uv", "run", "python", "scripts/sync.py"])
    if result.returncode != 0:
        emit("error", f"sync failed: {result.stderr.strip()}")
        return False
    return True


def _commit_sync_changes() -> None:
    """Commit any post-sync working-tree changes (hugo/ files created by sync)."""
    if not _has_uncommitted():
        return
    add = _run(["git", "add", "-A"])
    if add.returncode != 0:
        emit("warning", f"git add (sync) failed: {add.stderr.strip()}")
        return
    commit = _run(
        ["git", "commit", "--author", AGENT_AUTHOR, "-m",
         "auto(sync): Sync obsidian → hugo"]
    )
    if commit.returncode != 0 and "nothing to commit" not in commit.stdout:
        emit("warning", f"git commit (sync) failed: {commit.stderr.strip()}")
        return
    rev = _run(["git", "rev-parse", "HEAD"])
    if rev.returncode == 0:
        emit("info", f"committed synced files: {rev.stdout.strip()[:8]}")


def _hugo_build() -> bool:
    """Run `hugo --gc --minify` in hugo/. Returns True on success."""
    result = subprocess.run(
        ["hugo", "--gc", "--minify"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT / "hugo",
    )
    if result.returncode != 0:
        emit("error", f"hugo build failed: {result.stderr.strip()}")
        return False
    return True


def _git_push() -> bool:
    """Push HEAD to origin. Returns True on success."""
    result = _run(["git", "push"])
    if result.returncode != 0:
        emit("error", f"git push failed: {result.stderr.strip()}")
        return False
    return True


def push_if_due(state, push_interval_seconds: int = DEFAULT_PUSH_INTERVAL_SECONDS):
    """Validate + push when wall-clock interval has elapsed and commits are unpushed.

    Updates `state.last_git_push` on successful push. Caller is responsible
    for persisting state. No-op (returning quickly) when nothing to do.

    Returns True if a push was attempted and succeeded, False otherwise.
    """
    import os
    interval = int(
        os.environ.get("UNFIN_PUSH_INTERVAL_SECONDS", str(push_interval_seconds))
    )

    unpushed = get_unpushed_commits()
    if unpushed == 0:
        return False

    now = datetime.now(timezone.utc)
    last_push = state.last_git_push
    if last_push is not None:
        seconds_since = (now - last_push).total_seconds()
        if seconds_since < interval:
            remaining_min = int((interval - seconds_since) / 60)
            emit(
                "info",
                f"{unpushed} unpushed, next push in ~{remaining_min}m",
            )
            return False

    emit("info", f"push due: {unpushed} unpushed, validating...")

    _run_workflow_archive()
    if not _sync_obsidian_to_hugo():
        emit("warning", "validation failed (sync); skipping push")
        return False
    _commit_sync_changes()
    if not _hugo_build():
        emit("warning", "validation failed (hugo build); skipping push")
        return False

    emit("info", "validation passed, pushing...")
    if not _git_push():
        return False

    state.last_git_push = now
    emit("info", "push complete")
    return True
