#!/usr/bin/env python3
"""Embed published YouTube videos into Obsidian articles.

Scans the sibling auto_unfin repo for video metadata where
`stage == "youtube_published"`, then for each matching article inserts a
small raw-HTML block after the first paragraph (one video per run, newest
unrecorded first). Records each embedding in the article's frontmatter so
the operation is idempotent.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import click

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.videos import embed_all

log = logging.getLogger("embed_videos")

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_AUTO_UNFIN = REPO_ROOT.parent / "auto_unfin"


@click.command()
@click.option(
    "--auto-unfin-dir",
    type=click.Path(path_type=Path),
    default=DEFAULT_AUTO_UNFIN,
    show_default=True,
    help="Path to the sibling auto_unfin repo.",
)
@click.option(
    "--repo-root",
    type=click.Path(exists=True, path_type=Path),
    default=REPO_ROOT,
    show_default=True,
    help="Path to the unfinishablemap repo root.",
)
@click.option(
    "--dry-run",
    "-n",
    is_flag=True,
    help="Report planned changes without writing to disk.",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Enable debug logging.",
)
def main(
    auto_unfin_dir: Path,
    repo_root: Path,
    dry_run: bool,
    verbose: bool,
) -> None:
    """Embed published YouTube videos into matching Obsidian articles."""
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(message)s",
    )

    if not auto_unfin_dir.exists():
        click.echo(
            f"auto_unfin not found at {auto_unfin_dir} — nothing to do.",
            err=True,
        )
        return

    results = embed_all(
        repo_root=repo_root,
        auto_unfin_dir=auto_unfin_dir,
        dry_run=dry_run,
    )

    if not results:
        click.echo("No articles needed embedding.")
        return

    counts = {"embedded": 0, "backfilled": 0, "removed": 0, "skipped": 0, "error": 0}
    for r in results:
        counts[r.action] += 1
        click.echo(r.format())

    summary = ", ".join(f"{k}={v}" for k, v in counts.items() if v)
    prefix = "[DRY RUN] " if dry_run else ""
    click.echo(f"\n{prefix}{summary}")

    if counts["error"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
