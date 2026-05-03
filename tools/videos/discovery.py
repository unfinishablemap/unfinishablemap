"""Discover published YouTube videos in the sibling auto_unfin repo."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

log = logging.getLogger(__name__)

PUBLISHED_STAGE = "youtube_published"
DEFAULT_SUBDIRS: tuple[str, ...] = ("notebooklm",)


@dataclass(frozen=True)
class VideoRef:
    """Reference to a published video tied to an Obsidian article."""

    slug: str  # auto_unfin slug, e.g. "0046-01-split-brain-consciousness"
    category: str  # "topics", "concepts", "apex", "voids", ...
    article: str  # article slug, e.g. "split-brain-consciousness"
    obsidian_path: Path  # absolute path to the .md file
    video_id: str
    video_url: str
    title: Optional[str]
    sort_key: datetime  # used to pick "newest" when an article has several
    scheduled_at: Optional[datetime]  # publish time (None == "publish now")
    auto_unfin_source: str  # e.g. "notebooklm/0046-01-split-brain-consciousness"


def _parse_iso(value: object) -> Optional[datetime]:
    if not value:
        return None
    if isinstance(value, datetime):
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value
    try:
        parsed = datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def _scheduled_at(youtube: dict) -> Optional[datetime]:
    date = youtube.get("scheduled_date")
    if not date:
        return None
    time_str = youtube.get("scheduled_time") or "00:00"
    try:
        return datetime.fromisoformat(f"{date}T{time_str}:00+00:00")
    except ValueError:
        return None


def _resolve_obsidian_path(repo_root: Path, category: str, article: str) -> Path:
    """Build the canonical path to the Obsidian markdown for a video.

    Uses category + article fields directly; the JSON's `source.path`
    encodes the same information in a less robust relative form.
    """
    return (repo_root / "obsidian" / category / f"{article}.md").resolve()


def discover_published_videos(
    auto_unfin_dir: Path,
    repo_root: Path,
    subdirs: Iterable[str] = DEFAULT_SUBDIRS,
) -> list[VideoRef]:
    """Walk auto_unfin metadata and return all published videos.

    Args:
        auto_unfin_dir: Path to the sibling auto_unfin repo root.
        repo_root: Path to the unfinishablemap repo root (for resolving
            Obsidian article paths).
        subdirs: Which auto_unfin subdirectories to scan. Defaults to
            ("notebooklm",); pass extra dirs to extend coverage.

    Returns:
        VideoRefs whose stage is youtube_published. Articles whose
        Obsidian markdown does not exist are skipped with a warning.
    """
    refs: list[VideoRef] = []

    for subdir in subdirs:
        root = auto_unfin_dir / subdir
        if not root.is_dir():
            log.debug("Skipping missing auto_unfin subdir: %s", root)
            continue

        for json_path in sorted(root.glob("*/*.json")):
            try:
                data = json.loads(json_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                log.warning("Failed to parse %s: %s", json_path, exc)
                continue

            if data.get("stage") != PUBLISHED_STAGE:
                continue

            youtube = data.get("youtube") or {}
            video_id = youtube.get("video_id")
            video_url = youtube.get("video_url")
            if not video_id or not video_url:
                log.warning(
                    "%s claims %s but has no youtube.video_id/url",
                    json_path,
                    PUBLISHED_STAGE,
                )
                continue

            source = data.get("source") or {}
            category = source.get("category")
            article = source.get("article")
            if not category or not article:
                log.warning("%s missing source.category/article", json_path)
                continue

            obsidian_path = _resolve_obsidian_path(repo_root, category, article)
            if not obsidian_path.exists():
                log.warning(
                    "Skipping %s: target article %s not found",
                    json_path.name,
                    obsidian_path,
                )
                continue

            scheduled_at = _scheduled_at(youtube)
            sort_key = (
                scheduled_at
                or _parse_iso(data.get("modified"))
                or _parse_iso(data.get("created"))
                or datetime.min.replace(tzinfo=timezone.utc)
            )

            refs.append(
                VideoRef(
                    slug=data.get("slug", json_path.stem),
                    category=category,
                    article=article,
                    obsidian_path=obsidian_path,
                    video_id=video_id,
                    video_url=video_url,
                    title=youtube.get("title"),
                    sort_key=sort_key,
                    scheduled_at=scheduled_at,
                    auto_unfin_source=f"{subdir}/{data.get('slug', json_path.stem)}",
                )
            )

    return refs
