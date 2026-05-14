#!/usr/bin/env python3
"""Run the topic-concept anchoring audit (Audit Three of the calibration audit
triple). Flags topic articles whose evidential calibration falls below their
anchor concept pages' and (optionally) prepends ``refine-draft`` task blocks
to ``obsidian/workflow/todo.md``.

See ``obsidian/project/calibration-audit-triple.md`` Audit Three for the spec.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.curate.anchoring import (
    DEFAULT_HEDGE_DENSITY_RATIO,
    DEFAULT_MIN_WORD_COUNT,
    DEFAULT_STRONG_ASSERTION_RATIO,
    AnchoringFlag,
    format_refine_task,
    get_anchoring_flags,
)

REPO_ROOT = Path(__file__).parent.parent
TODO_PATH = REPO_ROOT / "obsidian" / "workflow" / "todo.md"
ACTIVE_TASKS_HEADING = "## Active Tasks"


def _dedupe_against_existing_todo(flags: list[AnchoringFlag]) -> list[AnchoringFlag]:
    """Drop flags whose (topic, anchor) pair is already represented by an
    open audit-generated task in todo.md. This prevents the audit from
    re-stacking the same task each run.
    """
    if not TODO_PATH.is_file():
        return flags
    body = TODO_PATH.read_text()
    keep: list[AnchoringFlag] = []
    for flag in flags:
        marker = (
            f"### P2: Adopt {flag.anchor_concept_path.stem} calibration in "
            f"{flag.topic_path.stem}"
        )
        if marker in body:
            continue
        keep.append(flag)
    return keep


def _prepend_to_todo(blocks: list[str]) -> None:
    """Insert task blocks immediately under the ``## Active Tasks`` heading."""
    if not blocks:
        return
    body = TODO_PATH.read_text()
    if ACTIVE_TASKS_HEADING not in body:
        raise click.ClickException(
            f"Could not find '{ACTIVE_TASKS_HEADING}' heading in {TODO_PATH}"
        )
    insertion = "\n".join(blocks) + "\n"
    new_body = body.replace(
        ACTIVE_TASKS_HEADING + "\n",
        ACTIVE_TASKS_HEADING + "\n\n" + insertion,
        1,
    )
    TODO_PATH.write_text(new_body)


@click.command()
@click.option(
    "--obsidian-root",
    type=click.Path(exists=True, path_type=Path),
    default=REPO_ROOT / "obsidian",
    help="Obsidian content root (default: ./obsidian).",
)
@click.option(
    "--hedge-density-ratio",
    type=float,
    default=DEFAULT_HEDGE_DENSITY_RATIO,
    help="Topic's hedge density must be at least N× the anchor's.",
)
@click.option(
    "--strong-assertion-ratio",
    type=float,
    default=DEFAULT_STRONG_ASSERTION_RATIO,
    help="Topic's strong-assertion density must not exceed N× the anchor's.",
)
@click.option(
    "--min-word-count",
    type=int,
    default=DEFAULT_MIN_WORD_COUNT,
    help="Skip articles shorter than this word count.",
)
@click.option(
    "--max-tasks",
    type=int,
    default=2,
    help=(
        "Max ``refine-draft`` tasks to emit (global cap per "
        "calibration-audit-triple.md; default 2)."
    ),
)
@click.option(
    "--apply",
    is_flag=True,
    help="Prepend generated tasks to todo.md. Default is dry-run.",
)
def main(
    obsidian_root: Path,
    hedge_density_ratio: float,
    strong_assertion_ratio: float,
    min_word_count: int,
    max_tasks: int,
    apply: bool,
) -> None:
    """Audit topic articles for under-hedging relative to their anchor
    concepts; optionally emit refine-draft tasks.
    """
    flags = get_anchoring_flags(
        obsidian_root,
        hedge_density_ratio=hedge_density_ratio,
        strong_assertion_ratio=strong_assertion_ratio,
        min_word_count=min_word_count,
    )

    new_flags = _dedupe_against_existing_todo(flags)
    capped = new_flags[:max_tasks]

    click.echo(f"Total flags: {len(flags)}")
    click.echo(f"New (not already in todo.md): {len(new_flags)}")
    click.echo(f"Capped at --max-tasks={max_tasks}: {len(capped)}")
    click.echo("")

    for flag in capped:
        click.echo(
            f"FLAG  {flag.topic_path.stem}  ->  {flag.anchor_concept_path.stem}"
        )
        click.echo(f"      failed: {', '.join(flag.failed_checks)}")
        for note in flag.notes:
            click.echo(f"        - {note}")
        click.echo("")

    if apply and capped:
        today_iso = datetime.now(timezone.utc).date().isoformat()
        blocks = [format_refine_task(f, today_iso) for f in capped]
        _prepend_to_todo(blocks)
        click.echo(f"Wrote {len(blocks)} refine-draft task(s) to {TODO_PATH}.")
    elif not apply and capped:
        click.echo("(dry-run; re-run with --apply to prepend tasks to todo.md)")


if __name__ == "__main__":
    main()
