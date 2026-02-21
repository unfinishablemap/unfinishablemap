#!/usr/bin/env python3
"""Check if a proposed filename would create a slug collision."""

import sys
from pathlib import Path

import click

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.sync.wikilinks import SYNC_DIRS, check_slug_available


@click.command()
@click.argument("slug")
@click.argument("section")
@click.option(
    "--obsidian",
    type=click.Path(exists=True, path_type=Path),
    default=Path(__file__).parent.parent / "obsidian",
    help="Path to Obsidian vault root",
)
def main(slug: str, section: str, obsidian: Path) -> None:
    """Check if SLUG is available in SECTION without collision.

    SLUG is the proposed filename stem (e.g. 'free-will').
    SECTION is the target directory (e.g. 'topics', 'concepts', 'voids').
    """
    if section not in SYNC_DIRS:
        click.echo(f"ERROR: Unknown section '{section}'. Valid: {', '.join(SYNC_DIRS)}")
        raise SystemExit(1)

    collision = check_slug_available(slug, section, obsidian)
    if collision:
        click.echo(f"COLLISION: {collision}")
        raise SystemExit(1)
    else:
        click.echo(f"OK: Slug '{slug}' is available in {section}/")


if __name__ == "__main__":
    main()
