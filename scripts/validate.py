#!/usr/bin/env python3
"""Validate content frontmatter."""

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.curate.validate import validate_frontmatter, validate_directory, fix_frontmatter


console = Console()


@click.command()
@click.argument("path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--strict",
    is_flag=True,
    help="Require all recommended fields",
)
@click.option(
    "--fix",
    is_flag=True,
    help="Attempt to fix issues automatically",
)
def main(path: Path, strict: bool, fix: bool) -> None:
    """Validate frontmatter at PATH (file or directory)."""
    if path.is_file():
        result = validate_frontmatter(path, strict=strict)
        _print_validation_result(result)

        if fix and not result["valid"]:
            if fix_frontmatter(path):
                console.print("[green]Fixed frontmatter issues[/green]")

        sys.exit(0 if result["valid"] else 1)
    else:
        results = validate_directory(path, strict=strict)

        table = Table(title=f"Validation Results: {path}")
        table.add_column("Metric", style="cyan")
        table.add_column("Count", style="white")

        table.add_row("Total files", str(results["total"]))
        table.add_row("Valid", f"[green]{results['valid']}[/green]")
        table.add_row("Invalid", f"[red]{results['invalid']}[/red]")
        table.add_row("Warnings", f"[yellow]{results['warnings']}[/yellow]")

        console.print(table)

        # Show details for invalid files
        for file_result in results["files"]:
            if not file_result["valid"] or file_result["warnings"]:
                console.print(f"\n[bold]{file_result['path']}[/bold]")
                for error in file_result["errors"]:
                    console.print(f"  [red]✗ {error}[/red]")
                for warning in file_result["warnings"]:
                    console.print(f"  [yellow]⚠ {warning}[/yellow]")

        sys.exit(0 if results["invalid"] == 0 else 1)


def _print_validation_result(result: dict) -> None:
    """Print a single validation result."""
    status = "[green]✓ Valid[/green]" if result["valid"] else "[red]✗ Invalid[/red]"
    console.print(f"{result['path']}: {status}")

    for error in result["errors"]:
        console.print(f"  [red]✗ {error}[/red]")
    for warning in result["warnings"]:
        console.print(f"  [yellow]⚠ {warning}[/yellow]")


if __name__ == "__main__":
    main()
