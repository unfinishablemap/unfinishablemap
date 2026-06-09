#!/usr/bin/env python3
"""Check Claude Code transcripts for model-fallback events (Fable → Opus).

Thin CLI wrapper around tools.evolution.model_fallback. See that module's
docstring for what a fallback is and why attribution cares.

Usage:
    uv run python scripts/check_model_fallback.py                # report only
    uv run python scripts/check_model_fallback.py --queue-task   # + queue P2 task
    uv run python scripts/check_model_fallback.py --since-hours 48
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.evolution.model_fallback import run  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--queue-task",
        action="store_true",
        help="Append a P2 attribution-check task to todo.md per fallback event",
    )
    parser.add_argument(
        "--since-hours",
        type=float,
        default=None,
        help="Override the scan window (default: since last run, 24h on first run)",
    )
    args = parser.parse_args()

    events = run(queue_tasks=args.queue_task, since_hours=args.since_hours)
    # Report-only semantics: exit 0 even when events found; the report and
    # queued task are the signal, not the exit code.
    suspected = sum(1 for e in events if e.severity == "FALLBACK-SUSPECTED")
    print(f"Done: {len(events)} mixed-model transcript(s), {suspected} fallback-suspected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
