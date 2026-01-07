#!/usr/bin/env python3
"""Deep review candidate selection CLI."""

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.curate.deep_review import get_review_candidates, get_top_candidate


console = Console()


@click.group()
def cli() -> None:
    """Deep review tools for finding documents needing comprehensive review."""
    pass


@cli.command()
@click.option(
    "--obsidian",
    "-o",
    type=click.Path(exists=True, path_type=Path),
    default="obsidian",
    help="Path to Obsidian vault",
)
@click.option(
    "--limit",
    "-n",
    type=int,
    default=10,
    help="Maximum candidates to show",
)
@click.option(
    "--include-drafts",
    is_flag=True,
    help="Include draft content",
)
def candidates(obsidian: Path, limit: int, include_drafts: bool) -> None:
    """List documents needing deep review, ranked by urgency."""
    results = get_review_candidates(
        obsidian,
        exclude_drafts=not include_drafts,
    )

    if not results:
        console.print("[yellow]No candidates found for deep review[/yellow]")
        return

    table = Table(title=f"Deep Review Candidates (top {min(limit, len(results))})")
    table.add_column("Score", style="cyan", justify="right")
    table.add_column("Title", style="white")
    table.add_column("Last Review", style="dim")
    table.add_column("Unreviewed Days", style="yellow", justify="right")
    table.add_column("Path", style="dim")

    for candidate in results[:limit]:
        last_review = (
            "Never" if candidate.days_since_review == -1 else f"{candidate.days_since_review}d ago"
        )
        table.add_row(
            f"{candidate.score:.0f}",
            candidate.title,
            last_review,
            str(candidate.days_unreviewed_content),
            str(candidate.path.relative_to(obsidian)),
        )

    console.print(table)

    if len(results) > limit:
        console.print(f"\n[dim]... and {len(results) - limit} more candidates[/dim]")


@cli.command("next")
@click.option(
    "--obsidian",
    "-o",
    type=click.Path(exists=True, path_type=Path),
    default="obsidian",
    help="Path to Obsidian vault",
)
@click.option(
    "--json",
    "as_json",
    is_flag=True,
    help="Output as JSON for scripting",
)
def next_candidate(obsidian: Path, as_json: bool) -> None:
    """Show the single highest priority candidate for deep review."""
    import json

    candidate = get_top_candidate(obsidian)

    if not candidate:
        if as_json:
            console.print(json.dumps({"candidate": None}))
        else:
            console.print("[yellow]No candidates found for deep review[/yellow]")
        return

    if as_json:
        output = {
            "candidate": {
                "path": str(candidate.path),
                "title": candidate.title,
                "score": candidate.score,
                "days_since_review": candidate.days_since_review,
                "days_unreviewed_content": candidate.days_unreviewed_content,
            }
        }
        console.print(json.dumps(output))
    else:
        console.print("[bold]Next deep review candidate:[/bold]")
        console.print(f"  Title: {candidate.title}")
        console.print(f"  Path: {candidate.path}")
        console.print(f"  Score: {candidate.score:.0f}")

        if candidate.days_since_review == -1:
            console.print("  Status: [red]Never reviewed[/red]")
        else:
            console.print(f"  Last reviewed: {candidate.days_since_review} days ago")
            console.print(f"  Unreviewed content: {candidate.days_unreviewed_content} days")


def main() -> None:
    """Entry point."""
    cli()


if __name__ == "__main__":
    main()
