#!/usr/bin/env python3
"""Run the altered-state symmetry audit (Audit Two of the calibration audit
triple). Flags filter-framed articles that cite the supportive-cluster
altered states without engaging the symmetric burden the disruptive cluster
imposes, and (optionally) prepends ``refine-draft`` task blocks to
``obsidian/workflow/todo.md``.

See ``obsidian/project/calibration-audit-triple.md`` Audit Two for the spec.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.curate.altered_state_symmetry import (
    DEFAULT_MIN_SUPPORTIVE_HITS,
    DEFAULT_MIN_WORD_COUNT,
    SymmetryFlag,
    format_refine_task,
    get_symmetry_flags,
)

REPO_ROOT = Path(__file__).parent.parent
TODO_PATH = REPO_ROOT / "obsidian" / "workflow" / "todo.md"
ACTIVE_TASKS_HEADING = "## Active Tasks"


def _dedupe_against_existing_todo(flags: list[SymmetryFlag]) -> list[SymmetryFlag]:
    """Drop flags whose target article is already represented by an open
    audit-generated task in todo.md."""
    if not TODO_PATH.is_file():
        return flags
    body = TODO_PATH.read_text()
    keep: list[SymmetryFlag] = []
    for flag in flags:
        marker = f"### P2: Install altered-state symmetry in {flag.path.stem}"
        if marker in body:
            continue
        keep.append(flag)
    return keep


def _prepend_to_todo(blocks: list[str]) -> None:
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
    "--min-word-count",
    type=int,
    default=DEFAULT_MIN_WORD_COUNT,
    help="Skip articles shorter than this word count.",
)
@click.option(
    "--min-supportive-hits",
    type=int,
    default=DEFAULT_MIN_SUPPORTIVE_HITS,
    help=(
        "Audit applies only to articles citing at least this many supportive-"
        "cluster items (default: 2, per spec)."
    ),
)
@click.option(
    "--max-tasks",
    type=int,
    default=2,
    help=(
        "Max ``refine-draft`` tasks to emit (per audit_triple.global_task_cap "
        "share; default 2)."
    ),
)
@click.option(
    "--apply",
    is_flag=True,
    help="Prepend generated tasks to todo.md. Default is dry-run.",
)
def main(
    obsidian_root: Path,
    min_word_count: int,
    min_supportive_hits: int,
    max_tasks: int,
    apply: bool,
) -> None:
    """Audit filter-framed articles for altered-state symmetry; optionally
    emit refine-draft tasks.
    """
    flags = get_symmetry_flags(
        obsidian_root,
        min_word_count=min_word_count,
        min_supportive_hits=min_supportive_hits,
    )

    new_flags = _dedupe_against_existing_todo(flags)
    capped = new_flags[:max_tasks]

    click.echo(f"Total flags: {len(flags)}")
    click.echo(f"New (not already in todo.md): {len(new_flags)}")
    click.echo(f"Capped at --max-tasks={max_tasks}: {len(capped)}")
    click.echo("")

    for flag in capped:
        click.echo(f"FLAG  {flag.path.parent.name}/{flag.path.stem}")
        click.echo(f"      failed: {', '.join(flag.failed_checks)}")
        click.echo(
            f"      supportive cited: "
            f"{', '.join(flag.profile.supportive_clusters) or '(none)'}"
        )
        click.echo(
            f"      disruptive cited: "
            f"{', '.join(flag.profile.disruptive_clusters) or '(none)'}"
        )
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
