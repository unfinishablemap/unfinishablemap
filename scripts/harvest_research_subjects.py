#!/usr/bin/env python3
"""Harvest research-topic subjects from the outer/optimistic review corpus.

Mechanical half of the harvest-research-subjects skill. The skill does the
LLM extraction (reading review prose, deciding which findings name an
uncovered subject); this CLI handles enumeration, dedup, task-writing, and
state. See tools/research/harvester.py for the why.

Usage:
    # 1. Ask which reviews to read this run (newest unscanned mine-reviews):
    uv run python scripts/harvest_research_subjects.py --list-unscanned

    # 2. After the skill extracts candidates, mint them (JSON on stdin):
    echo '{"subjects": [...], "scanned": ["optimistic-2026-06-14.md", ...]}' \
        | uv run python scripts/harvest_research_subjects.py --mint

    # Inspect state:
    uv run python scripts/harvest_research_subjects.py --status
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.research.harvester import (  # noqa: E402
    DEFAULT_MINT_CAP,
    DEFAULT_READ_BATCH,
    HarvestState,
    harvest,
    unscanned_reviews,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument(
        "--list-unscanned",
        action="store_true",
        help="Print newest unscanned mine-review paths (one per line) for the skill to read",
    )
    g.add_argument(
        "--mint",
        action="store_true",
        help="Read {subjects, scanned} JSON from stdin; dedupe, mint tasks, update state",
    )
    g.add_argument("--status", action="store_true", help="Print harvest state summary")
    parser.add_argument(
        "--batch",
        type=int,
        default=DEFAULT_READ_BATCH,
        help=f"How many reviews --list-unscanned returns (default {DEFAULT_READ_BATCH})",
    )
    parser.add_argument(
        "--mint-cap",
        type=int,
        default=DEFAULT_MINT_CAP,
        help=f"Max research-topic tasks to mint per run (default {DEFAULT_MINT_CAP})",
    )
    args = parser.parse_args()

    if args.list_unscanned:
        state = HarvestState.load()
        for path in unscanned_reviews(state, limit=args.batch):
            print(path.relative_to(Path.cwd()) if path.is_relative_to(Path.cwd()) else path)
        return 0

    if args.status:
        state = HarvestState.load()
        print(f"last_run: {state.last_run}")
        print(f"scanned_reviews: {len(state.scanned_reviews)}")
        print(f"minted_subjects: {len(state.minted_subjects)}")
        remaining = len(unscanned_reviews(state, limit=10_000))
        print(f"unscanned mine-reviews remaining: {remaining}")
        return 0

    # --mint
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON on stdin: {e}", file=sys.stderr)
        return 2
    subjects = payload.get("subjects", [])
    scanned = payload.get("scanned", [])
    if not isinstance(subjects, list) or not isinstance(scanned, list):
        print("ERROR: payload needs list 'subjects' and list 'scanned'", file=sys.stderr)
        return 2

    report = harvest(subjects, scanned, mint_cap=args.mint_cap)
    print(f"[MINTED] {report['minted']} research-topic task(s): {report['minted_slugs']}")
    if report["deferred_over_cap"]:
        print(
            f"[DEFERRED] {len(report['deferred_over_cap'])} over mint-cap (re-eligible next "
            f"run): {report['deferred_over_cap']}"
        )
    for slug, reason in report["rejected"]:
        print(f"[SKIP] {slug or '(no slug)'}: {reason}")
    print(f"[SCANNED] marked {report['scanned_count']} review(s) scanned")
    return 0


if __name__ == "__main__":
    sys.exit(main())
