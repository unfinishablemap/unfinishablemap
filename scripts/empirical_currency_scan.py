#!/usr/bin/env python3
"""Scan the corpus for empirical-record superlative claims.

Surfaces articles carrying "current record / first to demonstrate / largest /
to date" claims that are vulnerable to being silently superseded by newer
published results — a distinct defect class from citation-metadata errors
(see ``[[empirical-record-currency-drift]]``).

This is a screening pass only: every claim still needs web-verification.
The value of the scan is locating the passages a deep-review or
literature-drift-review should look at.
"""

from __future__ import annotations

import sys
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.curate.empirical_currency import (
    find_superlative_claims,
    rank_by_currency_risk,
    scan_corpus,
)

REPO_ROOT = Path(__file__).parent.parent


@click.command()
@click.option(
    "--obsidian-root",
    type=click.Path(exists=True, path_type=Path),
    default=REPO_ROOT / "obsidian",
    help="Obsidian content root (default: ./obsidian).",
)
@click.option(
    "--section",
    "sections",
    multiple=True,
    default=("topics", "apex"),
    help="Section(s) to scan. May be passed multiple times. Default: topics + apex.",
)
@click.option(
    "--file",
    "single_file",
    type=click.Path(exists=True, path_type=Path),
    default=None,
    help="Scan a single article instead of a section sweep.",
)
@click.option(
    "--top",
    type=int,
    default=20,
    help="Show only the top N articles by claim count.",
)
@click.option(
    "--show-claims",
    is_flag=True,
    help="Print each matched claim with line number and context.",
)
def main(
    obsidian_root: Path,
    sections: tuple[str, ...],
    single_file: Path | None,
    top: int,
    show_claims: bool,
) -> None:
    """Scan articles for superlative empirical claims."""
    if single_file:
        claims = find_superlative_claims(single_file)
        click.echo(f"{single_file}: {len(claims)} superlative claim(s)")
        for c in claims:
            click.echo(f"  L{c.line_number}: \"{c.matched_phrase}\"")
            click.echo(f"    {c.context}")
        return

    claims_by_path = scan_corpus(obsidian_root, sections=sections)
    ranked = rank_by_currency_risk(claims_by_path)

    click.echo(f"Articles with superlative claims: {len(ranked)}")
    click.echo("")

    for path, count in ranked[:top]:
        click.echo(f"  {count:3d}  {path.relative_to(obsidian_root)}")
        if show_claims:
            for c in claims_by_path[path]:
                click.echo(f"        L{c.line_number}: \"{c.matched_phrase}\" — {c.context}")
    if len(ranked) > top:
        click.echo(f"  ... and {len(ranked) - top} more")


if __name__ == "__main__":
    main()
