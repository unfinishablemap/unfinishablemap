"""Tests for archiving resolved outer-review entries into weekly files."""

from datetime import datetime, timedelta, timezone
from pathlib import Path

from tools.archive.workflow import archive_pending_reviews, get_current_iso_week
from tools.reviews.pending import add_commission, load_pending


def _commission(path: Path, target: str, when: datetime, status: str) -> None:
    add_commission(
        service="chatgpt",
        conversation_url="https://example.test/c",
        prompt_summary="s",
        target_filename=target,
        commissioned_at=when,
        path=path,
    )
    reviews = load_pending(path)
    reviews[-1].status = status
    from tools.reviews.pending import save_pending

    save_pending(reviews, path)


def test_archives_old_resolved_keeps_recent_and_pending(tmp_path: Path) -> None:
    pending = tmp_path / "pending-reviews.yaml"
    archive_dir = tmp_path / "archive"
    now = datetime.now(timezone.utc)
    old = now - timedelta(weeks=4)

    _commission(pending, "old-collected.md", old, "collected")
    _commission(pending, "old-pending.md", old, "pending")  # never archived
    _commission(pending, "recent-collected.md", now, "collected")

    counts = archive_pending_reviews(pending, archive_dir, keep_weeks=1)

    assert sum(counts.values()) == 1
    kept = {r.target_filename for r in load_pending(pending)}
    assert kept == {"old-pending.md", "recent-collected.md"}

    week = get_current_iso_week()
    iso = f"{old.isocalendar().year}-W{old.isocalendar().week:02d}"
    archived = load_pending(archive_dir / f"pending-reviews-{iso}.yaml")
    assert {r.target_filename for r in archived} == {"old-collected.md"}
    assert week  # current week string is well-formed


def test_dry_run_makes_no_changes(tmp_path: Path) -> None:
    pending = tmp_path / "pending-reviews.yaml"
    archive_dir = tmp_path / "archive"
    old = datetime.now(timezone.utc) - timedelta(weeks=4)
    _commission(pending, "old.md", old, "collected")

    counts = archive_pending_reviews(pending, archive_dir, keep_weeks=1, dry_run=True)

    assert sum(counts.values()) == 1
    assert not archive_dir.exists()
    assert {r.target_filename for r in load_pending(pending)} == {"old.md"}


def test_idempotent_merge(tmp_path: Path) -> None:
    pending = tmp_path / "pending-reviews.yaml"
    archive_dir = tmp_path / "archive"
    old = datetime.now(timezone.utc) - timedelta(weeks=4)
    _commission(pending, "a.md", old, "collected")
    archive_pending_reviews(pending, archive_dir, keep_weeks=1)

    # Re-archiving the same entry (simulate it reappearing) must not duplicate.
    _commission(pending, "a.md", old, "collected")
    archive_pending_reviews(pending, archive_dir, keep_weeks=1)

    iso = f"{old.isocalendar().year}-W{old.isocalendar().week:02d}"
    archived = load_pending(archive_dir / f"pending-reviews-{iso}.yaml")
    assert [r.target_filename for r in archived] == ["a.md"]


def test_empty_file_no_op(tmp_path: Path) -> None:
    pending = tmp_path / "pending-reviews.yaml"
    pending.write_text("", encoding="utf-8")
    counts = archive_pending_reviews(pending, tmp_path / "archive", keep_weeks=1)
    assert counts == {}
