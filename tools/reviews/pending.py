"""Pending-review state management.

Persists outstanding outer-review commissions in obsidian/workflow/pending-reviews.yaml
so commission and collect skills can hand off across loop iterations (and across
restarts of evolve_loop).

Schema (one entry per commissioned review):
    - service: chatgpt
      conversation_url: https://chatgpt.com/g/g-p-.../c/<id>
      commissioned_at: 2026-05-04T06:00:00+00:00
      prompt_summary: "drift toward animal consciousness"
      target_filename: outer-review-2026-05-04-chatgpt-5-5-pro.md
      status: pending  # pending | collected | failed | abandoned
      collect_attempts: 0
      last_attempt_at: null
      failure_reason: null
"""

import logging
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import yaml

log = logging.getLogger(__name__)

PENDING_REVIEWS_PATH = Path("obsidian/workflow/pending-reviews.yaml")

VALID_STATUSES = {"pending", "collected", "failed", "abandoned"}


@dataclass
class PendingReview:
    """One commissioned outer review awaiting collection."""

    service: str
    conversation_url: str
    commissioned_at: datetime
    prompt_summary: str
    target_filename: str
    status: str = "pending"
    collect_attempts: int = 0
    last_attempt_at: Optional[datetime] = None
    failure_reason: Optional[str] = None
    # Original prompt (full text), so a recovery commission can reuse it.
    prompt_text: Optional[str] = None

    def __post_init__(self) -> None:
        if self.status not in VALID_STATUSES:
            raise ValueError(
                f"PendingReview status {self.status!r} not in {VALID_STATUSES}"
            )

    def age(self, now: datetime) -> timedelta:
        return now - self.commissioned_at


def _resolve_path(path: Optional[Path]) -> Path:
    return path if path is not None else PENDING_REVIEWS_PATH


def load_pending(path: Optional[Path] = None) -> list[PendingReview]:
    """Load pending reviews from disk. Returns [] if file is missing or empty."""
    p = _resolve_path(path)
    if not p.exists():
        return []
    with open(p, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not data:
        return []
    if not isinstance(data, list):
        raise ValueError(f"{p} must contain a YAML list, got {type(data).__name__}")
    out: list[PendingReview] = []
    for entry in data:
        commissioned_at = entry["commissioned_at"]
        if isinstance(commissioned_at, str):
            commissioned_at = datetime.fromisoformat(commissioned_at)
        last_attempt_at = entry.get("last_attempt_at")
        if isinstance(last_attempt_at, str):
            last_attempt_at = datetime.fromisoformat(last_attempt_at)
        out.append(
            PendingReview(
                service=entry["service"],
                conversation_url=entry["conversation_url"],
                commissioned_at=commissioned_at,
                prompt_summary=entry["prompt_summary"],
                target_filename=entry["target_filename"],
                status=entry.get("status", "pending"),
                collect_attempts=entry.get("collect_attempts", 0),
                last_attempt_at=last_attempt_at,
                failure_reason=entry.get("failure_reason"),
                prompt_text=entry.get("prompt_text"),
            )
        )
    return out


def save_pending(reviews: list[PendingReview], path: Optional[Path] = None) -> None:
    """Persist pending reviews to disk."""
    p = _resolve_path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    out = []
    for r in reviews:
        d = asdict(r)
        d["commissioned_at"] = r.commissioned_at.isoformat()
        d["last_attempt_at"] = (
            r.last_attempt_at.isoformat() if r.last_attempt_at else None
        )
        out.append(d)
    with open(p, "w", encoding="utf-8") as f:
        yaml.safe_dump(out, f, sort_keys=False, default_flow_style=False)


def add_commission(
    service: str,
    conversation_url: str,
    prompt_summary: str,
    target_filename: str,
    commissioned_at: Optional[datetime] = None,
    prompt_text: Optional[str] = None,
    path: Optional[Path] = None,
) -> PendingReview:
    """Append a new pending commission. Returns the created record."""
    reviews = load_pending(path)
    review = PendingReview(
        service=service,
        conversation_url=conversation_url,
        commissioned_at=commissioned_at or datetime.now(timezone.utc),
        prompt_summary=prompt_summary,
        target_filename=target_filename,
        prompt_text=prompt_text,
    )
    reviews.append(review)
    save_pending(reviews, path)
    return review


def _find_index(reviews: list[PendingReview], target_filename: str) -> int:
    for i, r in enumerate(reviews):
        if r.target_filename == target_filename:
            return i
    raise KeyError(f"No pending review with target_filename={target_filename!r}")


def mark_collected(
    target_filename: str, path: Optional[Path] = None
) -> PendingReview:
    reviews = load_pending(path)
    idx = _find_index(reviews, target_filename)
    reviews[idx].status = "collected"
    reviews[idx].last_attempt_at = datetime.now(timezone.utc)
    save_pending(reviews, path)
    return reviews[idx]


def mark_failed(
    target_filename: str,
    reason: str,
    path: Optional[Path] = None,
) -> PendingReview:
    reviews = load_pending(path)
    idx = _find_index(reviews, target_filename)
    reviews[idx].status = "failed"
    reviews[idx].failure_reason = reason
    reviews[idx].last_attempt_at = datetime.now(timezone.utc)
    save_pending(reviews, path)
    return reviews[idx]


def mark_abandoned(
    target_filename: str, path: Optional[Path] = None
) -> PendingReview:
    reviews = load_pending(path)
    idx = _find_index(reviews, target_filename)
    reviews[idx].status = "abandoned"
    reviews[idx].last_attempt_at = datetime.now(timezone.utc)
    save_pending(reviews, path)
    return reviews[idx]


def increment_attempt(
    target_filename: str, path: Optional[Path] = None
) -> PendingReview:
    """Bump collect_attempts and last_attempt_at without changing status."""
    reviews = load_pending(path)
    idx = _find_index(reviews, target_filename)
    reviews[idx].collect_attempts += 1
    reviews[idx].last_attempt_at = datetime.now(timezone.utc)
    save_pending(reviews, path)
    return reviews[idx]


def find_ready(
    now: datetime,
    min_age_minutes: int = 90,
    service: Optional[str] = None,
    path: Optional[Path] = None,
) -> Optional[PendingReview]:
    """Return the oldest pending review whose age >= min_age_minutes.

    Optionally filter by service. Returns None when nothing is ready.
    """
    reviews = load_pending(path)
    candidates = [r for r in reviews if r.status == "pending"]
    if service is not None:
        candidates = [r for r in candidates if r.service == service]
    threshold = timedelta(minutes=min_age_minutes)
    ready = [r for r in candidates if (now - r.commissioned_at) >= threshold]
    if not ready:
        return None
    ready.sort(key=lambda r: r.commissioned_at)
    return ready[0]


def find_abandoned(
    now: datetime,
    max_age_hours: int = 4,
    path: Optional[Path] = None,
) -> list[PendingReview]:
    """Return pending reviews older than max_age_hours that are still pending."""
    reviews = load_pending(path)
    threshold = timedelta(hours=max_age_hours)
    return [
        r
        for r in reviews
        if r.status == "pending" and (now - r.commissioned_at) >= threshold
    ]


def has_in_flight(
    service: str, path: Optional[Path] = None
) -> bool:
    """Whether a pending commission already exists for this service.

    Used by commission skill to refuse to start a second commission while one
    is already in flight.
    """
    return any(
        r.service == service and r.status == "pending"
        for r in load_pending(path)
    )


def find_recent_failed(
    service: str,
    now: datetime,
    cooldown_hours: int = 1,
    path: Optional[Path] = None,
) -> Optional[PendingReview]:
    """Most recent failed entry for service whose failure was within cooldown_hours.

    Used by commission skill to back off auto-retry of failed commissions until
    the cooldown elapses.
    """
    reviews = load_pending(path)
    cutoff = now - timedelta(hours=cooldown_hours)
    failed = [
        r
        for r in reviews
        if r.service == service
        and r.status == "failed"
        and r.last_attempt_at is not None
        and r.last_attempt_at >= cutoff
    ]
    if not failed:
        return None
    failed.sort(key=lambda r: r.last_attempt_at, reverse=True)
    return failed[0]
