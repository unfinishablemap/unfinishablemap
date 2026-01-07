"""Deep review candidate selection.

Finds and ranks documents that need comprehensive review based on
their last_deep_review timestamp and modification history.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import frontmatter


@dataclass
class ReviewCandidate:
    """A document that needs deep review."""

    path: Path
    title: str
    modified: Optional[datetime]
    last_deep_review: Optional[datetime]
    days_since_review: int  # -1 if never reviewed
    days_unreviewed_content: int  # days since content changed without review
    score: float  # Higher = more urgent


def parse_timestamp(value: object) -> Optional[datetime]:
    """
    Parse ISO timestamp from frontmatter, handling various formats.

    Args:
        value: Timestamp value (string, datetime, or None)

    Returns:
        Parsed datetime or None if invalid/missing
    """
    if not value:
        return None
    if isinstance(value, datetime):
        return value
    try:
        str_value = str(value)
        if "T" in str_value:
            return datetime.fromisoformat(str_value)
        else:
            # Date-only format
            return datetime.fromisoformat(f"{str_value}T00:00:00")
    except (ValueError, TypeError):
        return None


def _ensure_tz_aware(dt: Optional[datetime]) -> Optional[datetime]:
    """Ensure datetime is timezone-aware (assume UTC if naive)."""
    if dt is None:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt


def _get_latest_modified(metadata: dict) -> Optional[datetime]:
    """Get the most recent modification timestamp from metadata."""
    candidates = [
        parse_timestamp(metadata.get("ai_modified")),
        parse_timestamp(metadata.get("human_modified")),
        parse_timestamp(metadata.get("modified")),
    ]
    # Ensure all timestamps are timezone-aware before comparison
    valid = [_ensure_tz_aware(ts) for ts in candidates if ts is not None]
    return max(valid) if valid else None


def _evaluate_file(
    file_path: Path,
    now: datetime,
    exclude_drafts: bool,
) -> Optional[ReviewCandidate]:
    """
    Evaluate a single file for review candidacy.

    Args:
        file_path: Path to markdown file
        now: Current time (timezone-aware)
        exclude_drafts: Whether to skip draft content

    Returns:
        ReviewCandidate if file needs review, None otherwise
    """
    try:
        post = frontmatter.load(file_path)
    except Exception:
        return None

    # Check draft status
    if exclude_drafts and post.metadata.get("draft", False):
        return None

    # Skip placeholders or empty content
    if not post.content.strip():
        return None

    title = post.metadata.get("title", file_path.stem)

    # Parse timestamps
    modified = _ensure_tz_aware(_get_latest_modified(post.metadata))
    last_deep_review = _ensure_tz_aware(
        parse_timestamp(post.metadata.get("last_deep_review"))
    )

    # Calculate metrics
    if last_deep_review is None:
        # Never reviewed
        days_since_review = -1
        if modified:
            days_unreviewed = (now - modified).days
        else:
            # No modification date - assume high urgency
            days_unreviewed = 30
        # Score: base 100 + age of unreviewed content
        score = 100.0 + days_unreviewed
    else:
        days_since_review = (now - last_deep_review).days
        if modified and modified > last_deep_review:
            # Content modified since last review
            days_unreviewed = (now - last_deep_review).days
            # Score: days of unreviewed content * 2
            score = float(days_unreviewed * 2)
        else:
            # Content unchanged since review - no need to review
            return None

    return ReviewCandidate(
        path=file_path,
        title=title,
        modified=modified,
        last_deep_review=last_deep_review,
        days_since_review=days_since_review,
        days_unreviewed_content=days_unreviewed,
        score=score,
    )


def get_review_candidates(
    content_dir: Path,
    content_types: Optional[list[str]] = None,
    exclude_drafts: bool = True,
) -> list[ReviewCandidate]:
    """
    Find all documents that need deep review.

    Args:
        content_dir: Root obsidian directory
        content_types: Subdirs to scan (default: topics, concepts, tenets, arguments)
        exclude_drafts: Skip draft content

    Returns:
        List of ReviewCandidate sorted by urgency (highest score first)
    """
    content_types = content_types or ["topics", "concepts", "tenets", "arguments"]
    now = datetime.now(timezone.utc)
    candidates: list[ReviewCandidate] = []

    for content_type in content_types:
        type_dir = content_dir / content_type
        if not type_dir.exists():
            continue

        for md_file in type_dir.glob("*.md"):
            # Skip index files (section landing pages)
            if md_file.stem == content_type or md_file.name == "_index.md":
                continue

            candidate = _evaluate_file(md_file, now, exclude_drafts)
            if candidate:
                candidates.append(candidate)

    # Sort by score descending (highest urgency first)
    candidates.sort(key=lambda c: -c.score)
    return candidates


def get_top_candidate(
    content_dir: Path,
    exclude_drafts: bool = True,
) -> Optional[ReviewCandidate]:
    """
    Get the single most urgent review candidate.

    Args:
        content_dir: Root obsidian directory
        exclude_drafts: Skip draft content

    Returns:
        The highest-priority ReviewCandidate, or None if no candidates
    """
    candidates = get_review_candidates(content_dir, exclude_drafts=exclude_drafts)
    return candidates[0] if candidates else None
