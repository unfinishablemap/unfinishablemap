"""Outer-review synthesis trigger logic.

Determines when a same-date "cycle" of outer reviews has finished resolving and
is ready for the synthesis pass (`combine-outer-reviews` skill). A cycle is
identified by the YYYY-MM-DD embedded in pending-reviews.yaml entries'
target_filename and in the corresponding review files on disk.
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Optional

import frontmatter

from .pending import PendingReview, load_pending

REVIEWS_DIR = Path("obsidian/reviews")
SYNTHESIS_PREFIX = "outer-review-synthesis-"
_DATE_RE = re.compile(r"outer-review-(\d{4}-\d{2}-\d{2})-")


def _date_from_filename(filename: str) -> Optional[str]:
    """Extract YYYY-MM-DD from an outer-review filename. None if it doesn't match."""
    if filename.startswith(SYNTHESIS_PREFIX):
        return None
    m = _DATE_RE.match(filename)
    return m.group(1) if m else None


def synthesis_path_for(date: str, reviews_dir: Path = REVIEWS_DIR) -> Path:
    """Canonical synthesis-file path for a given cycle date."""
    return reviews_dir / f"{SYNTHESIS_PREFIX}{date}.md"


def _is_processed(path: Path) -> bool:
    """Whether a review file's frontmatter declares outer_review_status: processed."""
    if not path.exists():
        return False
    try:
        post = frontmatter.load(path)
    except Exception:
        return False
    return post.metadata.get("outer_review_status") == "processed"


def count_processed_reviews_for(
    date: str, reviews_dir: Path = REVIEWS_DIR
) -> int:
    """Count outer-review files for a date with `outer_review_status: processed`.

    Excludes the synthesis file itself.
    """
    if not reviews_dir.exists():
        return 0
    count = 0
    for path in reviews_dir.glob(f"outer-review-{date}-*.md"):
        if path.name.startswith(SYNTHESIS_PREFIX):
            continue
        if _is_processed(path):
            count += 1
    return count


def cycle_dates_to_synthesize(
    now: datetime,
    reviews_dir: Path = REVIEWS_DIR,
    pending_path: Optional[Path] = None,
) -> list[str]:
    """Return cycle dates (YYYY-MM-DD) ready for `combine-outer-reviews`.

    A date is ready when:

    - pending-reviews.yaml has at least one entry whose target_filename
      embeds that date,
    - all entries for that date are resolved (none with status='pending';
      i.e., every entry is collected/abandoned/failed),
    - at least 2 of those entries have status='collected' AND the file
      named by target_filename has `outer_review_status: processed` in
      frontmatter,
    - no `obsidian/reviews/outer-review-synthesis-{date}.md` exists yet.

    `now` is accepted for symmetry with other dispatcher helpers and to allow
    future grace-period logic; it is currently unused.

    Returns dates sorted ascending (oldest cycle first); the dispatcher
    typically handles one per iteration.
    """
    del now  # reserved for future use
    pending = load_pending(pending_path)
    by_date: dict[str, list[PendingReview]] = {}
    for entry in pending:
        date = _date_from_filename(entry.target_filename)
        if date is None:
            continue
        by_date.setdefault(date, []).append(entry)

    ready: list[str] = []
    for date, entries in by_date.items():
        if synthesis_path_for(date, reviews_dir).exists():
            continue
        if any(e.status == "pending" for e in entries):
            continue
        processed_count = 0
        for e in entries:
            if e.status != "collected":
                continue
            if _is_processed(reviews_dir / e.target_filename):
                processed_count += 1
        if processed_count >= 2:
            ready.append(date)

    ready.sort()
    return ready
