"""Shared rotating-log target for the /loop-driven evolution path.

The Python loop in `scripts/evolve_loop.py` owns its own logger configured via
`setup_logging()`. The /loop-driven path is driven from inside a Claude Code
session — there is no long-running Python process to hold a logger — so each
short-lived Python entry (`cycle_pick`, `cycle_post`, `time_trigger`) imports
this module and calls `emit()` to append to the same rotating file the loop
uses today.

Format matches `setup_logging` so log lines from either path are mutually
readable. File rotation: daily at midnight, no backup retention (cron rotation
takes over post-rotation).
"""

import logging
import os
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent

# Default log path matches scripts/evolve_loop.py's --log-file default so the
# two orchestrators (Python loop + /loop) write to the same daily-rotated file.
# Overridable via UNFIN_LOG_FILE for prototype side-by-side comparison runs.
DEFAULT_LOG_FILE = (
    REPO_ROOT.parent / "unfinishablemap_log" / "evolve_loop.log"
)

_logger: logging.Logger | None = None


def _get_logger() -> logging.Logger:
    """Lazily configure and return the shared rotating logger."""
    global _logger
    if _logger is not None:
        return _logger

    log_path = Path(os.environ.get("UNFIN_LOG_FILE", str(DEFAULT_LOG_FILE)))
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("unfin.cycle")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Avoid duplicate handlers if _get_logger is called multiple times in
    # the same interpreter (e.g. tests).
    if not logger.handlers:
        handler = TimedRotatingFileHandler(
            log_path,
            when="midnight",
            backupCount=0,
            encoding="utf-8",
        )
        handler.suffix = "%Y-%m-%d"
        handler.setFormatter(
            logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        )
        logger.addHandler(handler)

    _logger = logger
    return logger


def emit(level: str, message: str) -> None:
    """Append a log line at the given level ('info', 'warning', 'error').

    Always prints to stderr too so the line is visible in the parent Claude
    Code session's transcript when a Python entry is called from a skill.
    """
    logger = _get_logger()
    log_method = getattr(logger, level.lower(), logger.info)
    log_method(message)
    # Also surface to the calling skill's stdout so the parent turn sees it.
    print(f"[{level.upper()}] {message}", flush=True)
