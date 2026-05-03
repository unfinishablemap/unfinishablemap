"""Embed YouTube video links into Obsidian articles after the intro section.

Bidirectional:
- Adds a video to an article whose newest published video is publicly
  viewable, scheduled time has passed, and oEmbed liveness check passes.
- Removes a recorded video from an article when it is no longer
  publicly viewable (rejected, deleted, made private) — both the body
  HTML block and the frontmatter entry.

Uses surgical text edits (not full frontmatter re-serialisation) so the
existing key order, quote styles, and whitespace are preserved.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Literal, Optional

import yaml

from .availability import Availability, check_video
from .discovery import VideoRef, discover_published_videos

log = logging.getLogger(__name__)

EMBED_LINK_TEXT = "Watch this article as a video on YouTube"
EMBED_SUMMARY_TEXT = "Video introduction"
EMBED_CAPTION_TEXT = (
    "Videos cover themes but may stray from the Map's position. "
    "The article text is the definitive version. "
    "Clicking play implies consent to YouTube cookies."
)


def privacy_link(video_id: str) -> str:
    """Privacy-preserving viewer URL.

    `youtube-nocookie.com/embed/...` works as a standalone page (no
    chrome, no related videos) and matches the iframe origin so we
    don't leak a separate cookie domain in the rendered markdown.
    """
    return f"https://www.youtube-nocookie.com/embed/{video_id}"

Action = Literal["embedded", "backfilled", "removed", "skipped", "error"]


@dataclass
class EmbedResult:
    path: Path
    action: Action
    video_id: str
    reason: str = ""

    def format(self) -> str:
        marker = {
            "embedded": "[EMBED]",
            "backfilled": "[BACKFILL]",
            "removed": "[REMOVE]",
            "skipped": "[SKIP]",
            "error": "[ERROR]",
        }[self.action]
        bits = [marker, str(self.path)]
        if self.video_id:
            bits.append(f"<- {self.video_id}")
        if self.reason:
            bits.append(f"({self.reason})")
        return " ".join(bits)


# ---------------------------------------------------------------------------
# Embed block (raw HTML, valid in Obsidian, Hugo Goldmark unsafe=true,
# and Cloudflare's HTML→markdown serialiser).
# ---------------------------------------------------------------------------


def _build_embed_block(video: VideoRef) -> str:
    """Raw HTML block.

    `<details>` provides a native collapsible (Pico CSS styles it).
    Pre-hydration the user expands to reveal the link; post-hydration
    JS swaps the anchor for an iframe inside the same disclosure.
    """
    return (
        f'<details class="yt-embed" data-video-id="{video.video_id}">\n'
        f"<summary>{EMBED_SUMMARY_TEXT}</summary>\n"
        f'<a href="{privacy_link(video.video_id)}">{EMBED_LINK_TEXT}</a>\n'
        f'<p class="yt-caption">{EMBED_CAPTION_TEXT}</p>\n'
        f"</details>"
    )


# ---------------------------------------------------------------------------
# Raw frontmatter / body splitting.
# ---------------------------------------------------------------------------


_FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def _split_file(text: str) -> tuple[str, str]:
    m = _FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("file has no frontmatter")
    return m.group(1), text[m.end() :]


def _join_file(fm: str, body: str) -> str:
    fm = fm.rstrip("\n")
    return f"---\n{fm}\n---\n{body}"


# ---------------------------------------------------------------------------
# YAML field surgery.
# ---------------------------------------------------------------------------


def _replace_or_append_scalar(fm: str, field: str, value: str) -> str:
    pattern = re.compile(rf"(?m)^{re.escape(field)}:.*$")
    new_line = f"{field}: {value}"
    if pattern.search(fm):
        return pattern.sub(new_line, fm, count=1)
    return fm.rstrip("\n") + "\n" + new_line


def _take_field(fm: str, field: str) -> tuple[str, Optional[str]]:
    """Strip `field`'s entire block from fm; return (fm_without_field, removed)."""
    lines = fm.split("\n")
    prefix = f"{field}:"
    start: Optional[int] = None
    for i, line in enumerate(lines):
        if line.startswith(prefix) and (
            len(line) == len(prefix) or line[len(prefix)] in (" ", "\t", "")
        ):
            start = i
            break
    if start is None:
        return fm, None

    end = start + 1
    while end < len(lines):
        line = lines[end]
        if line.startswith((" ", "\t")):
            end += 1
        else:
            break

    removed = "\n".join(lines[start:end])
    new_lines = lines[:start] + lines[end:]
    return "\n".join(new_lines), removed


def _parse_existing_videos(fm: str) -> list[dict]:
    try:
        data = yaml.safe_load(fm) or {}
    except yaml.YAMLError:
        return []
    entries = data.get("embedded_videos") or []
    return [e for e in entries if isinstance(e, dict)]


def _format_videos_block(entries: list[dict]) -> str:
    lines = ["embedded_videos:"]
    for entry in entries:
        lines.append(f"  - id: {entry['id']}")
        lines.append(f"    url: {entry['url']}")
        lines.append(f"    embedded: {entry['embedded']}")
        lines.append(f"    source: {entry['source']}")
    return "\n".join(lines)


def _write_videos_field(fm: str, entries: list[dict]) -> str:
    """Strip any existing embedded_videos block, then re-emit at the end.

    If `entries` is empty, the field is omitted entirely.
    """
    fm_no_field, _ = _take_field(fm, "embedded_videos")
    if not entries:
        return fm_no_field.rstrip("\n")
    return fm_no_field.rstrip("\n") + "\n" + _format_videos_block(entries)


# ---------------------------------------------------------------------------
# Body modification.
# ---------------------------------------------------------------------------


_HEADING_RE = re.compile(r"^#+\s")


def _insert_at_end_of_intro(body: str, block: str) -> Optional[str]:
    """Insert block at the end of the intro section (before first heading)."""
    lines = body.split("\n")
    n = len(lines)

    has_content = any(
        l.strip() and not l.strip().startswith("#") for l in lines
    )
    if not has_content:
        return None

    insert_at = n
    for i, raw in enumerate(lines):
        if _HEADING_RE.match(raw):
            insert_at = i
            break

    head = lines[:insert_at]
    tail = lines[insert_at:]
    while head and not head[-1].strip():
        head = head[:-1]
    while tail and not tail[0].strip():
        tail = tail[1:]

    new_lines = head + [""] + block.split("\n") + [""] + tail
    rebuilt = "\n".join(new_lines)
    if body.endswith("\n") and not rebuilt.endswith("\n"):
        rebuilt += "\n"
    return rebuilt


def _remove_block_from_body(body: str, video_id: str) -> tuple[str, bool]:
    """Remove the yt-embed block matching video_id from body.

    Handles both the current `<details>` form and the legacy `<div>`
    form so back-compat works if anything's been pasted manually.
    Trims surrounding blank lines so the seam stays a single paragraph
    break.
    """
    patterns = (
        re.compile(
            rf'<details class="yt-embed" data-video-id="{re.escape(video_id)}">.*?</details>',
            re.DOTALL,
        ),
        re.compile(
            rf'<div class="yt-embed" data-video-id="{re.escape(video_id)}">.*?</div>',
            re.DOTALL,
        ),
    )
    for pat in patterns:
        m = pat.search(body)
        if not m:
            continue
        start, end = m.span()
        while start > 0 and body[start - 1] == "\n":
            start -= 1
        while end < len(body) and body[end] == "\n":
            end += 1
        before = body[:start].rstrip("\n")
        after = body[end:].lstrip("\n")
        if before and after:
            new = f"{before}\n\n{after}"
        elif before:
            new = before + "\n"
        elif after:
            new = after
        else:
            new = ""
        return new, True
    return body, False


# ---------------------------------------------------------------------------
# Per-video status decision.
# ---------------------------------------------------------------------------


def _is_future_scheduled(
    video_id: str,
    now: datetime,
    metadata_by_id: dict[str, VideoRef],
) -> bool:
    """True if auto_unfin metadata says this video's publish time is still ahead.

    Returns False when we have no metadata for the ID (manual entry or
    JSON deleted) — in that case the oEmbed check is the source of truth.
    """
    ref = metadata_by_id.get(video_id)
    if ref is None or ref.scheduled_at is None:
        return False
    return ref.scheduled_at > now


# ---------------------------------------------------------------------------
# Per-article processing.
# ---------------------------------------------------------------------------


def _find_articles_with_recordings(repo_root: Path) -> set[Path]:
    """All obsidian/*.md files that have an embedded_videos field."""
    obsidian = repo_root / "obsidian"
    if not obsidian.is_dir():
        return set()
    paths: set[Path] = set()
    for md in obsidian.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        if re.search(r"(?m)^embedded_videos:", text):
            paths.add(md.resolve())
    return paths


def _process_article(
    md_path: Path,
    *,
    candidates: list[VideoRef],
    metadata_by_id: dict[str, VideoRef],
    now: datetime,
    dry_run: bool,
) -> list[EmbedResult]:
    """Reconcile one article's embedded_videos against current availability.

    Returns one EmbedResult per change (possibly several for the same article).
    """
    try:
        text = md_path.read_text(encoding="utf-8")
        fm, body = _split_file(text)
    except (OSError, ValueError) as exc:
        return [
            EmbedResult(
                path=md_path,
                action="error",
                video_id="",
                reason=f"failed to read frontmatter: {exc}",
            )
        ]

    existing = _parse_existing_videos(fm)
    results: list[EmbedResult] = []
    changed = False

    # 1. Liveness check on existing entries — drop any that are unavailable
    #    or whose JSON metadata says they're scheduled-but-not-yet-public.
    kept: list[dict] = []
    for entry in existing:
        vid = entry.get("id", "")
        if not vid:
            kept.append(entry)
            continue
        if _is_future_scheduled(vid, now, metadata_by_id):
            body, removed = _remove_block_from_body(body, vid)
            results.append(
                EmbedResult(
                    path=md_path,
                    action="removed",
                    video_id=vid,
                    reason="scheduled in future",
                )
            )
            changed = True
            continue
        avail = check_video(vid)
        if avail is Availability.UNAVAILABLE:
            body, removed = _remove_block_from_body(body, vid)
            results.append(
                EmbedResult(
                    path=md_path,
                    action="removed",
                    video_id=vid,
                    reason="unavailable on YouTube",
                )
            )
            changed = True
            continue
        # AVAILABLE or UNKNOWN — keep
        kept.append(entry)

    # 2. If no entries remain after cleanup, consider adding the newest
    #    available candidate (or back-filling a manually-pasted ID).
    new_entry: Optional[dict] = None
    if not kept and candidates:
        candidates_sorted = sorted(
            candidates, key=lambda v: v.sort_key, reverse=True
        )
        # Filter to only candidates that are not future-scheduled.
        live_candidates = [
            v for v in candidates_sorted
            if v.scheduled_at is None or v.scheduled_at <= now
        ]
        # Backfill takes priority: a candidate already in the body wins.
        chosen: Optional[VideoRef] = None
        for v in live_candidates:
            if v.video_id in body:
                chosen = v
                break
        if chosen is None:
            for v in live_candidates:
                if check_video(v.video_id) is Availability.AVAILABLE:
                    chosen = v
                    break

        if chosen is not None:
            in_body_already = chosen.video_id in body
            if not in_body_already:
                inserted = _insert_at_end_of_intro(body, _build_embed_block(chosen))
                if inserted is None:
                    results.append(
                        EmbedResult(
                            path=md_path,
                            action="error",
                            video_id=chosen.video_id,
                            reason="no body content found",
                        )
                    )
                    return results
                body = inserted
            new_entry = {
                "id": chosen.video_id,
                "url": privacy_link(chosen.video_id),
                "embedded": now.isoformat(),
                "source": chosen.auto_unfin_source,
            }
            kept.append(new_entry)
            results.append(
                EmbedResult(
                    path=md_path,
                    action=("backfilled" if in_body_already else "embedded"),
                    video_id=chosen.video_id,
                )
            )
            changed = True

    # 3. Persist if anything changed.
    if changed:
        new_fm = _write_videos_field(fm, kept)
        new_fm = _replace_or_append_scalar(new_fm, "ai_modified", now.isoformat())
        new_text = _join_file(new_fm, body)
        if not dry_run:
            md_path.write_text(new_text, encoding="utf-8")

    return results


# ---------------------------------------------------------------------------
# Public API.
# ---------------------------------------------------------------------------


def embed_video(
    md_path: Path,
    video: VideoRef,
    *,
    dry_run: bool = False,
) -> EmbedResult:
    """Embed a single video into a single article (kept for direct use / tests).

    For full reconciliation across many articles use `embed_all` — it
    handles un-embedding and oEmbed liveness checks too.
    """
    now = datetime.now(timezone.utc)
    metadata_by_id = {video.video_id: video}
    results = _process_article(
        md_path,
        candidates=[video],
        metadata_by_id=metadata_by_id,
        now=now,
        dry_run=dry_run,
    )
    if not results:
        return EmbedResult(
            path=md_path,
            action="skipped",
            video_id=video.video_id,
            reason="article already has a recorded video",
        )
    return results[0]


def embed_all(
    repo_root: Path,
    auto_unfin_dir: Path,
    *,
    dry_run: bool = False,
) -> list[EmbedResult]:
    """Reconcile every article: drop dead embeds, add new ones where due."""
    if not auto_unfin_dir.is_dir():
        log.info("auto_unfin not present at %s — nothing to do", auto_unfin_dir)
        return []

    videos = discover_published_videos(auto_unfin_dir, repo_root)
    metadata_by_id: dict[str, VideoRef] = {v.video_id: v for v in videos}

    by_article: dict[Path, list[VideoRef]] = {}
    for v in videos:
        by_article.setdefault(v.obsidian_path, []).append(v)

    articles_with_recordings = _find_articles_with_recordings(repo_root)
    articles_to_check: set[Path] = set(by_article.keys()) | articles_with_recordings

    now = datetime.now(timezone.utc)
    results: list[EmbedResult] = []
    for path in sorted(articles_to_check):
        results.extend(
            _process_article(
                path,
                candidates=by_article.get(path, []),
                metadata_by_id=metadata_by_id,
                now=now,
                dry_run=dry_run,
            )
        )
    return results
