#!/usr/bin/env python3
"""Archive old workflow entries (changelog, completed tasks) into weekly files."""

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.archive.workflow import archive_changelog, archive_completed_tasks

console = Console()

REPO_ROOT = Path(__file__).parent.parent
WORKFLOW_DIR = REPO_ROOT / "obsidian" / "workflow"
ARCHIVE_DIR = WORKFLOW_DIR / "archive"


@click.command()
@click.option(
    "--keep-weeks",
    default=1,
    help="Number of recent weeks to keep in main files (default: 1)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be archived without making changes",
)
def main(keep_weeks: int, dry_run: bool) -> None:
    """Archive old changelog and completed task entries into weekly files."""
    changelog_path = WORKFLOW_DIR / "changelog.md"
    todo_path = WORKFLOW_DIR / "todo.md"

    if dry_run:
        console.print("[yellow]DRY RUN - no files will be modified[/yellow]\n")

    # Archive changelog
    console.print("[bold]Archiving changelog entries...[/bold]")
    if changelog_path.exists():
        changelog_archived = archive_changelog(
            changelog_path, ARCHIVE_DIR, keep_weeks=keep_weeks, dry_run=dry_run
        )
        if changelog_archived:
            table = Table(title="Changelog Archives")
            table.add_column("Week", style="cyan")
            table.add_column("Entries", style="green", justify="right")
            for week, count in sorted(changelog_archived.items()):
                table.add_row(week, str(count))
            console.print(table)
            total = sum(changelog_archived.values())
            console.print(f"Total changelog entries to archive: {total}\n")
        else:
            console.print("No changelog entries to archive.\n")
    else:
        console.print(f"[red]Changelog not found: {changelog_path}[/red]\n")

    # Archive completed tasks
    console.print("[bold]Archiving completed tasks...[/bold]")
    if todo_path.exists():
        tasks_archived = archive_completed_tasks(
            todo_path, ARCHIVE_DIR, keep_weeks=keep_weeks, dry_run=dry_run
        )
        if tasks_archived:
            table = Table(title="Completed Task Archives")
            table.add_column("Week", style="cyan")
            table.add_column("Tasks", style="green", justify="right")
            for week, count in sorted(tasks_archived.items()):
                table.add_row(week, str(count))
            console.print(table)
            total = sum(tasks_archived.values())
            console.print(f"Total completed tasks to archive: {total}\n")
        else:
            console.print("No completed tasks to archive.\n")
    else:
        console.print(f"[red]Todo file not found: {todo_path}[/red]\n")

    if dry_run:
        console.print("[yellow]DRY RUN complete - run without --dry-run to apply[/yellow]")
    else:
        console.print("[green]Archive complete![/green]")
        console.print(f"Archive files written to: {ARCHIVE_DIR}")


if __name__ == "__main__":
    main()
