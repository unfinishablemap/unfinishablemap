"""Errors for the Obsidian-to-Hugo sync pipeline."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class BrokenWikilink:
    """A single unresolved wikilink."""

    source_file: Path
    target: str  # The raw wikilink target text
    slug: str  # The slugified form that was looked up


@dataclass
class SlugCollision:
    """A slug that maps to multiple sections."""

    slug: str
    urls: list[str]  # All URLs that share this slug


@dataclass
class SyncReport:
    """Collected errors and warnings from a sync run."""

    broken_wikilinks: list[BrokenWikilink] = field(default_factory=list)
    slug_collisions: list[SlugCollision] = field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return len(self.broken_wikilinks) > 0

    def format_report(self) -> str:
        """Format a human-readable error report."""
        lines: list[str] = []

        if self.slug_collisions:
            lines.append(f"=== SLUG COLLISIONS ({len(self.slug_collisions)}) ===")
            lines.append(
                "These slugs exist in multiple sections. "
                "Use path-qualified wikilinks (e.g. [[topics/free-will]])."
            )
            for c in self.slug_collisions:
                lines.append(f"  {c.slug}: {', '.join(c.urls)}")
            lines.append("")

        if self.broken_wikilinks:
            # Group by target slug for readability
            by_slug: dict[str, list[BrokenWikilink]] = {}
            for bw in self.broken_wikilinks:
                by_slug.setdefault(bw.slug, []).append(bw)

            lines.append(
                f"=== BROKEN WIKILINKS ({len(self.broken_wikilinks)} "
                f"references to {len(by_slug)} targets) ==="
            )
            for slug, refs in sorted(by_slug.items(), key=lambda x: -len(x[1])):
                files = sorted({str(r.source_file) for r in refs})
                lines.append(f"  [[{refs[0].target}]] ({len(refs)} refs in {len(files)} files)")
                for f in files[:5]:
                    lines.append(f"    - {f}")
                if len(files) > 5:
                    lines.append(f"    ... and {len(files) - 5} more")
            lines.append("")

        return "\n".join(lines)


class SyncValidationError(Exception):
    """Raised when the sync completes but broken wikilinks were found."""

    def __init__(self, report: SyncReport):
        self.report = report
        n_broken = len(report.broken_wikilinks)
        n_targets = len({bw.slug for bw in report.broken_wikilinks})
        super().__init__(
            f"Sync found {n_broken} broken wikilink references "
            f"to {n_targets} unresolved targets"
        )
