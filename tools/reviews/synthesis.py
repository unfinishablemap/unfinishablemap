"""Outer-review synthesis trigger logic.

Determines when a same-date "cycle" of outer reviews has finished resolving and
is ready for the synthesis pass (`combine-outer-reviews` skill). A cycle is
identified by the YYYY-MM-DD embedded in pending-reviews.yaml entries'
target_filename and in the corresponding review files on disk.
"""

import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import frontmatter

from .pending import PendingReview, load_pending

REVIEWS_DIR = Path("obsidian/reviews")
SYNTHESIS_PREFIX = "outer-review-synthesis-"
_DATE_RE = re.compile(r"outer-review-(\d{4}-\d{2}-\d{2})-")
# Match any outer-review filename anywhere in a task block (Review file/Review
# files/notes/etc.). Excludes synthesis files via the trailing service slug.
_OUTER_REVIEW_FILE_RE = re.compile(
    r"outer-review-(\d{4}-\d{2}-\d{2})-[^/\s)`'\"]+\.md"
)
# Match the `Source: outer-review` marker tolerant of common todo.md styling:
# `Source: outer-review`, `**Source**: outer-review`, `- **Source**: outer-review`.
_SOURCE_OUTER_REVIEW_RE = re.compile(
    r"Source\*{0,2}\s*:\s*outer-review", re.IGNORECASE
)


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


def _cycle_resolved_but_unsynthesizable(
    date: str,
    *,
    reviews_dir: Path = REVIEWS_DIR,
    pending_path: Optional[Path] = None,
) -> bool:
    """True iff the cycle has all pending-reviews entries resolved but
    fewer than 2 processed — synthesis cannot and will not fire.

    A cycle with no pending-reviews entries at all (e.g., a manually-created
    review file with no automation state) is also treated as unsynthesizable:
    there is nothing for the synthesis trigger to wait on.
    """
    pending = load_pending(pending_path)
    entries = [e for e in pending if date in e.target_filename]
    if not entries:
        return True
    if any(e.status == "pending" for e in entries):
        return False
    processed = 0
    for e in entries:
        if e.status != "collected":
            continue
        path = reviews_dir / e.target_filename
        if not path.exists():
            continue
        try:
            post = frontmatter.load(path)
        except Exception:
            continue
        if post.metadata.get("outer_review_status") == "processed":
            processed += 1
    return processed < 2


def is_outer_review_task_deferred(
    task_block: str,
    now: datetime,
    *,
    grace_period_days: int = 7,
    pending_path: Optional[Path] = None,
    reviews_dir: Path = REVIEWS_DIR,
) -> bool:
    """Whether a queue-eligible outer-review-source task should be deferred.

    The synthesis pass (`/combine-outer-reviews`) runs only after all
    reviewers in a cycle have processed. Per-review tasks land in todo.md
    immediately when each `/outer-review` fires — so without a deferral, the
    queue dispatcher could execute outer-review-source tasks BEFORE the
    convergence-dedup pass merges duplicates and upgrades convergent
    priorities. This helper returns True when the task should be skipped
    by the selector for that reason.

    A task is deferred iff:

    - Its body declares `Source: outer-review` (any styling — bullet,
      bold-key, plain).
    - It references at least one `outer-review-YYYY-MM-DD-{slug}.md`
      filename (typically in a `Review file:` / `Review files:` field).
    - At least one referenced cycle date has none of these escape clauses:
      (a) `outer-review-synthesis-{date}.md` already exists,
      (b) the cycle is `_cycle_resolved_but_unsynthesizable` (synthesis
          will never fire — quorum lost),
      (c) the cycle is older than `grace_period_days` (something is stuck;
          fall back to executing rather than waiting forever).

    Tasks without a recognised outer-review filename, or with no
    `Source: outer-review` marker, are never deferred.
    """
    if not _SOURCE_OUTER_REVIEW_RE.search(task_block):
        return False
    cycle_dates = _OUTER_REVIEW_FILE_RE.findall(task_block)
    if not cycle_dates:
        return False
    grace = timedelta(days=grace_period_days)
    for date in cycle_dates:
        if synthesis_path_for(date, reviews_dir).exists():
            continue
        try:
            cycle_dt = datetime.strptime(date, "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )
        except ValueError:
            continue
        if (now - cycle_dt) > grace:
            continue
        if _cycle_resolved_but_unsynthesizable(
            date, reviews_dir=reviews_dir, pending_path=pending_path
        ):
            continue
        return True
    return False
