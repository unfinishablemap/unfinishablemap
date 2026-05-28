"""Chrome process management for outer-review automation.

Adapted from the sibling auto_unfin's tools/video/chrome.py. Owns a dedicated
profile at ``~/unfin/chrome-profiles/unfinishable`` so Chrome instances we
launch are always distinct from anything the user is running interactively
or from the auto_unfin video pipeline.

The Claude Code extension installed in this profile must be seeded once by
the user (one-time interactive launch + login + extension install). After
that, every commission/collect cycle starts a fresh Chrome from this profile,
runs the task, and stops Chrome — Chrome with the Claude Code extension tends
to become unusable over long sessions, so a fresh start per cycle is the cure.

Concurrency is enforced cross-repo via a shared advisory lock at
``~/unfin/chrome-profiles/.automation.lock``. Both this repo and auto_unfin
should hold this lock while their Chrome is running. ``ChromeUnavailableError``
is raised when the lock is held by someone else.

Profile-presence check: the user must seed the profile with the Claude Code
extension and ChatGPT credentials before any task can run. ``is_profile_seeded()``
returns False if the user hasn't done this — the dispatcher should skip the
task and log a one-time warning.
"""

from __future__ import annotations

import contextlib
import errno
import fcntl
import logging
import os
import shutil
import signal
import subprocess
import time
from collections.abc import Iterator
from pathlib import Path
from typing import Optional

log = logging.getLogger(__name__)

PROFILE_DIR = Path("~/unfin/chrome-profiles/unfinishable").expanduser()
LOCK_FILE = Path("~/unfin/chrome-profiles/.automation.lock").expanduser()
PIDFILE = Path("~/unfin/chrome-profiles/.chrome.pid").expanduser()

# Substring match for pgrep -f. Leading "--" is dropped because pgrep parses
# arguments starting with "--" as flags; the dashes still appear in Chrome's
# argv but we don't need them in the match string.
_PROFILE_MATCH = f"user-data-dir={PROFILE_DIR}"

# Wait this many seconds for our Chrome process to appear in the process list.
_LAUNCH_TIMEOUT_S = 30
# Wait this many seconds for SIGTERM to take effect before SIGKILL.
_TERM_TIMEOUT_S = 10


class ChromeUnavailableError(RuntimeError):
    """Raised when Chrome can't be used — lock held by another automation,
    profile not seeded, or launch failed."""


def is_profile_seeded() -> bool:
    """Return True if the profile dir exists and looks usable.

    The user must seed the profile interactively once (install the Claude Code
    extension and log in to ChatGPT). Heuristic: profile must have a Default
    subdirectory and at least one extension installed. We don't try to verify
    the *specific* extension because Chrome's extension layout changes; the
    presence of any installed extension is a strong signal the user did the
    one-time setup.
    """
    default_dir = PROFILE_DIR / "Default"
    if not default_dir.is_dir():
        return False
    extensions_dir = default_dir / "Extensions"
    if not extensions_dir.is_dir():
        return False
    # Any extension installed (subdir with at least one file) indicates the
    # user has used the profile interactively.
    for child in extensions_dir.iterdir():
        if child.is_dir() and any(child.iterdir()):
            return True
    return False


def _our_chrome_pids() -> list[int]:
    """Return PIDs of Chrome processes running under our profile."""
    try:
        result = subprocess.run(
            ["pgrep", "-f", _PROFILE_MATCH],
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return []
    if result.returncode != 0:
        return []
    return [int(line) for line in result.stdout.split() if line.strip().isdigit()]


def _kill_pids(pids: list[int]) -> None:
    """SIGTERM then SIGKILL the given pids."""
    for pid in pids:
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    time.sleep(3)
    for pid in pids:
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            continue
        try:
            os.kill(pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    time.sleep(1)


class ChromeManager:
    """Lifecycle manager for an isolated Chrome instance.

    Tracks the process group of the Chrome we launched and only signals
    processes whose argv contains our profile path.
    """

    def __init__(self) -> None:
        self._process: Optional[subprocess.Popen[bytes]] = None
        self._pgid: Optional[int] = None

    def ensure_running(self) -> None:
        """Ensure our profile's Chrome is running. Launch it if not.

        If a leftover Chrome from a prior unclean shutdown is still bound
        to our profile, it gets killed and replaced — we never trust tab
        state we didn't just create.
        """
        if self._process is not None and self._process.poll() is not None:
            log.info("Chrome (ours) exited unexpectedly, clearing state")
            self._process = None
            self._pgid = None

        leftover = _our_chrome_pids()
        if leftover and self._pgid is None:
            log.info(f"Found leftover Chrome on our profile (pids {leftover}); killing")
            _kill_pids(leftover)

        if _our_chrome_pids():
            return

        self._launch()

    def stop(self) -> None:
        """Stop Chrome we launched. No-op if we didn't launch any.

        Kills via process group (since we used start_new_session=True),
        then sweeps any stragglers still matching our profile path.
        """
        if self._pgid is not None:
            log.info(f"Stopping Chrome process group {self._pgid}")
            try:
                os.killpg(self._pgid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            deadline = time.time() + _TERM_TIMEOUT_S
            while time.time() < deadline:
                if not _our_chrome_pids():
                    break
                time.sleep(0.5)
            else:
                log.warning("Chrome process group did not exit, sending SIGKILL")
                try:
                    os.killpg(self._pgid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                time.sleep(1)

        strays = _our_chrome_pids()
        if strays:
            log.warning(f"Killing stray Chrome pids on our profile: {strays}")
            _kill_pids(strays)

        self._process = None
        self._pgid = None

    def _launch(self) -> None:
        """Launch Chrome under our dedicated profile."""
        PROFILE_DIR.mkdir(parents=True, exist_ok=True)
        chrome_bin = shutil.which("google-chrome") or "google-chrome"
        log.info(f"Launching Chrome under {PROFILE_DIR}")
        self._process = subprocess.Popen(
            [
                chrome_bin,
                f"--user-data-dir={PROFILE_DIR}",
                "--no-first-run",
                "--no-default-browser-check",
                "--restore-last-session",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        try:
            self._pgid = os.getpgid(self._process.pid)
        except ProcessLookupError:
            self._pgid = None

        deadline = time.time() + _LAUNCH_TIMEOUT_S
        while time.time() < deadline:
            if _our_chrome_pids():
                break
            if self._process.poll() is not None and not _our_chrome_pids():
                rc = self._process.returncode
                self._process = None
                self._pgid = None
                raise ChromeUnavailableError(f"Chrome failed to start (exit {rc})")
            time.sleep(0.5)
        else:
            self._process = None
            self._pgid = None
            raise ChromeUnavailableError("Chrome did not appear in process list within 30s")

        log.info(f"Chrome launched (pgid {self._pgid})")


class _AutomationLock:
    """Cross-repo advisory lock for Chrome-using automations.

    Held by whichever automation (auto_unfin video, this repo's outer-review)
    is currently driving Chrome. Non-blocking: if the lock is held, the
    caller must back off — never block waiting since automation runs are
    short and another process holding the lock means it's busy with Chrome.
    """

    def __init__(self, path: Path = LOCK_FILE) -> None:
        self.path = path
        self._fd: Optional[int] = None

    def acquire(self) -> None:
        """Acquire the lock non-blockingly. Raises ChromeUnavailableError if held."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        # O_CREAT | O_RDWR — we never write content, just hold the lock.
        self._fd = os.open(str(self.path), os.O_CREAT | os.O_RDWR, 0o644)
        try:
            fcntl.flock(self._fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as e:
            os.close(self._fd)
            self._fd = None
            if e.errno in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise ChromeUnavailableError(
                    f"Automation lock held by another process at {self.path}"
                ) from e
            raise

    def release(self) -> None:
        """Release the lock. Idempotent."""
        if self._fd is None:
            return
        try:
            fcntl.flock(self._fd, fcntl.LOCK_UN)
        except OSError:
            pass
        try:
            os.close(self._fd)
        except OSError:
            pass
        self._fd = None


@contextlib.contextmanager
def chrome_session(
    require_seeded: bool = True,
) -> Iterator[ChromeManager]:
    """Context manager that runs a fresh Chrome for the duration of the with-block.

    On enter: acquires the cross-repo automation lock, launches Chrome under
    our profile, yields the ``ChromeManager``. On exit: stops Chrome, releases
    the lock — whether the with-block exited normally or by exception.

    Raises:
        ChromeUnavailableError: if the profile isn't seeded (and ``require_seeded``
            is True), or if the cross-repo lock is held by another process,
            or if Chrome fails to launch within 30s.
    """
    if require_seeded and not is_profile_seeded():
        raise ChromeUnavailableError(
            f"Chrome profile at {PROFILE_DIR} is not seeded — "
            f"the user must launch Chrome with this profile once, install "
            f"the Claude Code extension, and log in to ChatGPT before "
            f"automation can use it."
        )

    lock = _AutomationLock()
    lock.acquire()
    manager = ChromeManager()
    try:
        manager.ensure_running()
        yield manager
    finally:
        try:
            manager.stop()
        finally:
            lock.release()


# -----------------------------------------------------------------------------
# Detached start/stop + diagnostics CLI
#
# `/unfin-cycle` (the in-Claude orchestrator that replaced scripts/evolve_loop.py)
# cannot wrap a Skill-tool invocation in the `chrome_session()` Python context
# manager — the Skill call is a runtime tool call, not a subprocess. So the
# orchestrator calls `python -m tools.chrome_session start` via Bash before
# invoking a Chrome-using skill, then `python -m tools.chrome_session stop`
# after. `start` launches Chrome detached and records its PID in a pidfile;
# `stop` reads the pidfile and kills it. `start` is idempotent: if our Chrome
# is already running, it returns success without relaunching, so back-to-back
# Chrome tasks within the automation window reuse a live Chrome.
#
# The fcntl lock at LOCK_FILE is still used briefly during `start` to serialise
# concurrent starts. It is NOT held for the duration of Chrome's life — once
# the pidfile is written, the lock is released. The pidfile + cmdline check
# is the durable "is Chrome ours and alive?" signal.
#
# Run via `python -m tools.chrome_session <start|stop|status>`
# (legacy flags `--status` and `--force-cleanup` still work for compatibility).
# -----------------------------------------------------------------------------


def _read_pidfile() -> Optional[int]:
    """Return the PID recorded in the pidfile, or None if absent/malformed."""
    if not PIDFILE.exists():
        return None
    try:
        text = PIDFILE.read_text().strip()
    except OSError:
        return None
    return int(text) if text.isdigit() else None


def _write_pidfile(pid: int) -> None:
    PIDFILE.parent.mkdir(parents=True, exist_ok=True)
    PIDFILE.write_text(str(pid))


def _remove_pidfile() -> None:
    try:
        PIDFILE.unlink()
    except FileNotFoundError:
        pass


def _pid_is_our_chrome(pid: int) -> bool:
    """Return True if pid is alive AND its cmdline contains our profile path."""
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except (ProcessLookupError, PermissionError):
        return False
    return _PROFILE_MATCH in _process_argv(pid)


def start_detached() -> tuple[str, int]:
    """Launch Chrome detached and record its PID in the pidfile. Idempotent.

    Returns ``(message, exit_code)``. Exit code 0 means Chrome is running
    under our profile (either just launched or already was). Exit code 2
    means we couldn't start it (profile not seeded, lock held by another
    process, Chrome binary missing, launch timed out).
    """
    if not is_profile_seeded():
        return (
            f"Chrome profile at {PROFILE_DIR} is not seeded — "
            "install the Claude Code extension interactively first.",
            2,
        )

    lock = _AutomationLock()
    try:
        lock.acquire()
    except ChromeUnavailableError as e:
        return (f"CHROME_UNAVAILABLE: {e}", 2)

    try:
        existing_pid = _read_pidfile()
        if existing_pid is not None and _pid_is_our_chrome(existing_pid):
            return (f"Chrome already running on our profile (pid {existing_pid})", 0)

        if existing_pid is not None:
            _remove_pidfile()

        leftover = _our_chrome_pids()
        if leftover:
            log.info(f"Killing leftover Chrome on our profile before relaunch: {leftover}")
            _kill_pids(leftover)

        PROFILE_DIR.mkdir(parents=True, exist_ok=True)
        chrome_bin = shutil.which("google-chrome") or "google-chrome"
        try:
            process = subprocess.Popen(
                [
                    chrome_bin,
                    f"--user-data-dir={PROFILE_DIR}",
                    "--no-first-run",
                    "--no-default-browser-check",
                    "--restore-last-session",
                ],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
        except FileNotFoundError:
            return (f"CHROME_UNAVAILABLE: {chrome_bin} not found on PATH", 2)

        deadline = time.time() + _LAUNCH_TIMEOUT_S
        while time.time() < deadline:
            if _our_chrome_pids():
                break
            if process.poll() is not None:
                return (
                    f"CHROME_UNAVAILABLE: chrome exited during startup (rc {process.returncode})",
                    2,
                )
            time.sleep(0.5)
        else:
            return ("CHROME_UNAVAILABLE: chrome did not appear in process list within 30s", 2)

        _write_pidfile(process.pid)
        return (f"Chrome launched detached (pid {process.pid})", 0)
    finally:
        lock.release()


def stop_detached() -> tuple[str, int]:
    """Kill Chrome under our profile and clear the pidfile. Idempotent.

    Always returns exit code 0 — `stop` is best-effort cleanup that must
    not block the next iteration of the orchestrator.
    """
    pids_to_kill = set(_our_chrome_pids())
    recorded = _read_pidfile()
    if recorded is not None:
        pids_to_kill.add(recorded)

    if not pids_to_kill:
        _remove_pidfile()
        return ("No Chrome processes on our profile; nothing to stop.", 0)

    pids_list = sorted(pids_to_kill)
    _kill_pids(pids_list)
    _remove_pidfile()

    remaining = _our_chrome_pids()
    if remaining:
        return (f"Killed {pids_list}; some pids remain: {remaining}", 0)
    return (f"Killed {pids_list}; Chrome stopped.", 0)


def _lslocks_pids(lock_path: Path) -> list[int]:
    """Return PIDs holding a fcntl lock on lock_path. Empty list if none or unavailable."""
    if not lock_path.exists():
        return []
    try:
        result = subprocess.run(
            ["lslocks", "--noheadings", "--raw", "--output", "PID,PATH"],
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return []
    if result.returncode != 0:
        return []
    pids: list[int] = []
    target = str(lock_path.resolve())
    for line in result.stdout.splitlines():
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            continue
        pid_str, path = parts
        if path == target and pid_str.isdigit():
            pids.append(int(pid_str))
    return pids


def _process_argv(pid: int) -> str:
    """Best-effort: return /proc/<pid>/cmdline as a single string, or '<gone>'."""
    cmdline = Path(f"/proc/{pid}/cmdline")
    if not cmdline.exists():
        return "<gone>"
    try:
        raw = cmdline.read_bytes()
    except OSError:
        return "<unreadable>"
    return raw.replace(b"\x00", b" ").decode("utf-8", errors="replace").strip()


def _status_report() -> str:
    """Human-readable snapshot of Chrome+lock+pidfile state under our profile."""
    lines: list[str] = []
    lines.append(f"Profile dir:   {PROFILE_DIR}")
    lines.append(f"Profile seeded: {is_profile_seeded()}")
    lines.append(f"Lock file:     {LOCK_FILE}")
    if LOCK_FILE.exists():
        holders = _lslocks_pids(LOCK_FILE)
        if not holders:
            lines.append("Lock holders:  none (lock file exists but is unheld)")
        else:
            lines.append(f"Lock holders:  {holders}")
            for pid in holders:
                lines.append(f"  pid {pid}: {_process_argv(pid)[:160]}")
    else:
        lines.append("Lock holders:  none (lock file does not exist)")
    recorded = _read_pidfile()
    if recorded is None:
        lines.append(f"Pidfile:       {PIDFILE} (absent)")
    elif _pid_is_our_chrome(recorded):
        lines.append(f"Pidfile:       {PIDFILE} → pid {recorded} (alive, our chrome)")
    else:
        lines.append(f"Pidfile:       {PIDFILE} → pid {recorded} (STALE — pid not our chrome)")
    chromes = _our_chrome_pids()
    if chromes:
        lines.append(f"Chrome procs on our profile: {chromes}")
    else:
        lines.append("Chrome procs on our profile: none")
    return "\n".join(lines)


def _force_cleanup() -> str:
    """Kill any Chrome under our profile. Returns a status line.

    The fcntl lock auto-releases when its holder exits, so killing wedged
    Chromes (and any parent that was stuck on them) is sufficient — there
    is no separate lock-removal step.
    """
    chromes = _our_chrome_pids()
    if not chromes:
        return "No Chrome processes on our profile; nothing to clean up."
    log.warning(f"Force-cleanup: killing Chrome pids {chromes}")
    _kill_pids(chromes)
    remaining = _our_chrome_pids()
    if remaining:
        return f"Killed {chromes}; some pids remain: {remaining}"
    return f"Killed {chromes}; no Chrome processes remain on our profile."


def _cli_main(argv: list[str]) -> int:
    import argparse

    # Subcommands (start/stop/status) take precedence over legacy flags.
    if argv and argv[0] in ("start", "stop", "status"):
        cmd = argv[0]
        if cmd == "start":
            msg, code = start_detached()
            print(msg)
            return code
        if cmd == "stop":
            msg, code = stop_detached()
            print(msg)
            return code
        # status
        print(_status_report())
        return 0

    ap = argparse.ArgumentParser(
        description=(
            "Manage Chrome session state for the unfinishable profile. "
            "Use subcommands `start`, `stop`, or `status` for /unfin-cycle integration; "
            "legacy flags below are for operator diagnostics."
        )
    )
    ap.add_argument(
        "--status",
        action="store_true",
        help="Show current Chrome + lock state (default).",
    )
    ap.add_argument(
        "--force-cleanup",
        action="store_true",
        help="Kill any Chrome under our profile. The fcntl lock auto-releases.",
    )
    args = ap.parse_args(argv)

    if args.force_cleanup:
        print(_force_cleanup())
        _remove_pidfile()
        print()
    print(_status_report())
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(_cli_main(sys.argv[1:]))
