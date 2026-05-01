#!/usr/bin/env python3
"""Check whether a research note has already been consumed into an article.

Used by the replenish-queue skill to filter `unconsumed_research` candidates
before generating expand-topic tasks. The check looks across both the live
catalogue (`obsidian/{topics,concepts,voids,apex}/`) and the archive
(`archive/{topics,concepts,voids,apex}/`), since research consumed into
coalesced/archived articles still counts as covered.
"""

from __future__ import annotations

import sys
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.curate.research_match import (
    CONFIDENCE_EXACT,
    CONFIDENCE_FUZZY,
    CONFIDENCE_STOPWORD,
    find_matching_articles,
    research_slug,
)


@click.command()
@click.argument("research_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--repo-root",
    type=click.Path(exists=True, path_type=Path),
    default=Path(__file__).parent.parent,
    help="Repository root containing obsidian/ and archive/ directories.",
)
@click.option(
    "--min-confidence",
    type=click.Choice([CONFIDENCE_EXACT, CONFIDENCE_STOPWORD, CONFIDENCE_FUZZY]),
    default=CONFIDENCE_FUZZY,
    help=(
        "Minimum confidence to count as consumed. 'exact' = identical slug; "
        "'stopword-equivalent' = same tokens after stopword removal; "
        "'fuzzy' = high token overlap with shared compound term (default)."
    ),
)
@click.option(
    "--all",
    "show_all",
    is_flag=True,
    help="Show every match, not just the highest-confidence one.",
)
def main(
    research_path: Path,
    repo_root: Path,
    min_confidence: str,
    show_all: bool,
) -> None:
    """Check whether RESEARCH_PATH has a corresponding article.

    Exits 0 with "CONSUMED: <article-path>" if a match is found at or above
    the configured confidence; exits 1 with "UNCONSUMED" otherwise.
    """
    slug = research_slug(research_path.name)
    matches = find_matching_articles(research_path, repo_root)

    confidence_rank = {
        CONFIDENCE_EXACT: 0,
        CONFIDENCE_STOPWORD: 1,
        CONFIDENCE_FUZZY: 2,
    }
    threshold = confidence_rank[min_confidence]
    qualifying = [m for m in matches if confidence_rank[m.confidence] <= threshold]

    if not qualifying:
        click.echo(f"UNCONSUMED: no articles match research slug '{slug}'")
        if matches and show_all:
            click.echo("  (below-threshold candidates considered:)")
            for m in matches:
                click.echo(f"    - {m.path} [{m.confidence}, score={m.score:.2f}: {m.reason}]")
        raise SystemExit(1)

    best = qualifying[0]
    click.echo(
        f"CONSUMED: {best.path} [{best.confidence}, score={best.score:.2f}: {best.reason}]"
    )
    if show_all and len(qualifying) > 1:
        click.echo("  (additional matches:)")
        for m in qualifying[1:]:
            click.echo(f"    - {m.path} [{m.confidence}, score={m.score:.2f}: {m.reason}]")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
