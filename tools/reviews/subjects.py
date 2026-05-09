"""Outer-review subject selection.

When a commission skill fires, it asks this module: "what should the next
outer review focus on?". The first commission of a UTC date picks the
subject; subsequent commissions of the same date reuse it (so all three
services review the same subject and the synthesis pass sees real
convergence). Selection cascade:

1. Reuse — if any pending-reviews entry already exists for the cycle date
   with subject metadata, reconstruct the subject from it. No mutation.
2. Queue — pop the highest-priority open task from
   `obsidian/workflow/outer-todo.md` (P0 > P1 > P2 > P3, FIFO within a
   tier). Mutation deferred until `mark-consumed`.
3. Site fallback — if no review with subject_type=site (or legacy `-site-`
   filename infix) was commissioned in the last 7 days, return a
   site-review subject.
4. Recent-aged fallback — pick the most-recently-modified article from
   topics/concepts/apex/voids whose `ai_modified` is between (now - 60d)
   and (now - 7d) and that has not been the focus of an outer review in
   the last 60 days.
5. None — return type='none'; the commission skill exits cleanly.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import frontmatter

from .pending import PendingReview, load_pending

REVIEWS_DIR = Path("obsidian/reviews")
OUTER_TODO_PATH = Path("obsidian/workflow/outer-todo.md")
ARTICLE_DIRS = [
    Path("obsidian/topics"),
    Path("obsidian/concepts"),
    Path("obsidian/apex"),
    Path("obsidian/voids"),
]
SITE_URL = "https://unfinishablemap.org"
CHANGELOG_URL = "https://unfinishablemap.org/workflow/changelog/"

# Section-index files that share the section name; skipped when scanning
# articles for the recent-aged fallback (they are landing pages).
_INDEX_FILE_NAMES = {"apex.md", "topics.md", "concepts.md", "voids.md"}

_PRIORITY_RE = re.compile(r"^### P([0-3]):\s*(.+)$")
_DONE_RE = re.compile(r"^### ✓\s+\d{4}-\d{2}-\d{2}:\s*(.+)$")
_FIELD_RE = re.compile(r"^- \*\*([^*]+)\*\*:\s*(.*)$")
_REVIEW_DATE_RE = re.compile(r"outer-review-(\d{4}-\d{2}-\d{2})-")


@dataclass
class CycleSubject:
    """A subject for one cycle of outer reviews.

    Same dataclass for queue/site/recent/none — branch on `type` in the
    consuming skill.
    """

    type: str  # "queue" | "site" | "recent" | "none"
    title: str
    prompt_seed: str
    articles: list[str] = field(default_factory=list)
    source: str = ""
    notes: str = ""


@dataclass
class _OuterTodoTask:
    """One open task parsed from outer-todo.md."""

    priority: int  # 0..3
    title: str
    articles: list[str]
    notes: str
    line_no: int  # 1-indexed line of the `### P{N}:` heading
    added: str = ""


def _strip_code_fences(text: str) -> list[Optional[str]]:
    """Return one entry per source line. Lines inside fenced code blocks are
    set to None so the parser can preserve original line numbers while
    skipping example/illustrative content.
    """
    out: list[Optional[str]] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(None)
            continue
        out.append(None if in_fence else line)
    return out


def _parse_outer_todo(text: str) -> list[_OuterTodoTask]:
    """Parse open `### P{N}:` tasks from outer-todo.md.

    Skips `### ✓` (consumed) headings and any content inside ```fenced```
    code blocks (so format-illustration examples in the file's header
    aren't mistaken for real tasks). Lines are 1-indexed in the returned
    `line_no` so consumers can refer to them as `outer-todo.md:L{n}`.
    """
    tasks: list[_OuterTodoTask] = []
    lines = _strip_code_fences(text)
    i = 0
    while i < len(lines):
        line = lines[i]
        if line is None:
            i += 1
            continue
        m = _PRIORITY_RE.match(line)
        if not m:
            i += 1
            continue
        priority = int(m.group(1))
        title = m.group(2).strip()
        line_no = i + 1  # 1-indexed
        articles: list[str] = []
        notes_parts: list[str] = []
        added = ""
        j = i + 1
        while j < len(lines):
            raw = lines[j]
            if raw is None:
                j += 1
                continue
            if raw.startswith("### ") or raw.startswith("## "):
                break
            fm = _FIELD_RE.match(raw)
            if fm:
                key = fm.group(1).strip().lower()
                value = fm.group(2).strip()
                if key == "articles":
                    articles = [a.strip() for a in value.split(",") if a.strip()]
                elif key == "notes":
                    notes_parts.append(value)
                elif key == "added":
                    added = value
                else:
                    # Unknown field — leave a trace in notes so it doesn't
                    # vanish silently.
                    notes_parts.append(f"{key}: {value}")
            elif raw.strip():
                # Continuation of multi-line notes.
                notes_parts.append(raw.strip())
            j += 1
        tasks.append(
            _OuterTodoTask(
                priority=priority,
                title=title,
                articles=articles,
                notes=" ".join(notes_parts).strip(),
                line_no=line_no,
                added=added,
            )
        )
        i = j
    return tasks


def _truncate_title(title: str, max_len: int = 80) -> str:
    """Word-boundary truncation with ellipsis when the title overflows."""
    if len(title) <= max_len:
        return title
    cut = title[: max_len - 1]
    space = cut.rfind(" ")
    if space > 0:
        cut = cut[:space]
    return cut.rstrip(",.;:!?- ") + "…"


def _select_top_queue_task(tasks: list[_OuterTodoTask]) -> Optional[_OuterTodoTask]:
    """Highest-priority FIFO winner. P0 > P1 > P2 > P3, then by line order."""
    if not tasks:
        return None
    return min(tasks, key=lambda t: (t.priority, t.line_no))


def _build_queue_subject(task: _OuterTodoTask) -> CycleSubject:
    article_urls = [_article_to_url(a) for a in task.articles]
    parts = [
        f"User-curated subject (P{task.priority}, added {task.added or 'n/d'}): "
        f"{task.title}"
    ]
    if article_urls:
        parts.append(
            "Focus on these articles: " + ", ".join(article_urls) + "."
        )
    if task.notes:
        parts.append(f"Notes from the commissioner: {task.notes}")
    return CycleSubject(
        type="queue",
        title=_truncate_title(task.title),
        prompt_seed=" ".join(parts),
        articles=task.articles,
        source=f"outer-todo.md:L{task.line_no}",
        notes=task.notes,
    )


def _build_site_subject() -> CycleSubject:
    seed = (
        f"Analyse {SITE_URL} as a whole. Identify novel insights or "
        f"inferences the site has not yet stated; structural weaknesses; "
        f"tenet-coherence issues; cross-cluster contradictions. End the "
        f"report with a concrete list of improvements to specific articles "
        f"and to the site's methodology. Consult the changelog at "
        f"{CHANGELOG_URL} so you see recent activity that web-search "
        f"indices have not yet picked up."
    )
    return CycleSubject(
        type="site",
        title="Full-site audit",
        prompt_seed=seed,
        articles=[],
        source="fallback:site-stale-7d",
        notes="",
    )


def _build_recent_subject(article_path: str, ai_modified: datetime) -> CycleSubject:
    url = _article_to_url(article_path)
    seed = (
        f"The article {url} was last substantively modified "
        f"{ai_modified.date().isoformat()} (≥7 days ago, so search engines "
        f"have had time to re-index). Audit its claims, citations, "
        f"counterargument coverage, and integration with surrounding "
        f"articles. Look for insufficient evidence, missed counterarguments, "
        f"tenet-protective bracketing, and stale references. The site "
        f"changelog is at {CHANGELOG_URL}; the site root is {SITE_URL}."
    )
    return CycleSubject(
        type="recent",
        title=f"Audit {Path(article_path).stem}",
        prompt_seed=seed,
        articles=[article_path],
        source="fallback:recent-aged",
        notes="",
    )


def _none_subject() -> CycleSubject:
    return CycleSubject(
        type="none",
        title="",
        prompt_seed="",
        articles=[],
        source="",
        notes="",
    )


def _article_to_url(path: str) -> str:
    """Convert an obsidian path like 'topics/foo.md' to a Map URL."""
    p = path
    # Strip leading "obsidian/" if present
    if p.startswith("obsidian/"):
        p = p[len("obsidian/"):]
    # Drop trailing .md
    if p.endswith(".md"):
        p = p[: -len(".md")]
    return f"{SITE_URL}/{p}/"


def _reuse_subject_for_cycle(
    cycle_date: str, pending: list[PendingReview]
) -> Optional[CycleSubject]:
    """If any pending entry for this cycle already carries subject metadata,
    reconstruct a CycleSubject from it. Returns None if no entry exists or
    if existing entries are legacy (no subject_type)."""
    for entry in pending:
        if cycle_date not in entry.target_filename:
            continue
        if entry.subject_type is None:
            continue
        return CycleSubject(
            type=entry.subject_type,
            title=entry.subject_title or entry.prompt_summary,
            # We don't persist prompt_seed in pending — reconstruct a thin
            # one. The reusing skill should still compose its own
            # service-specific prompt around the subject.
            prompt_seed=entry.prompt_summary,
            articles=list(entry.subject_articles or []),
            source=f"reuse:pending-reviews:{entry.target_filename}",
            notes="",
        )
    return None


def _site_stale(now: datetime, days: int, pending: list[PendingReview]) -> bool:
    """True iff no site-type review has been commissioned in the last `days`."""
    cutoff = now - timedelta(days=days)
    for entry in pending:
        if entry.commissioned_at < cutoff:
            continue
        if entry.subject_type == "site":
            return False
        # Legacy site reviews used a `-site-` infix in the filename.
        if "-site-" in entry.target_filename:
            return False
    return True


def _articles_recently_outer_reviewed(
    now: datetime, window_days: int, reviews_dir: Path
) -> set[str]:
    """Set of article paths that have been the focus of an outer review in
    the last `window_days`.

    Reads each `outer-review-YYYY-MM-DD-{slug}.md` (excluding synthesis
    files) and pulls `subject_articles` from frontmatter. Falls back to
    `related_articles` (wikilinks) for legacy reviews so the dedupe still
    has signal. Review date is taken from the filename, since
    `commissioned_at` isn't carried in the file frontmatter.
    """
    if not reviews_dir.exists():
        return set()
    cutoff = (now - timedelta(days=window_days)).date()
    out: set[str] = set()
    for path in reviews_dir.glob("outer-review-*.md"):
        if path.name.startswith("outer-review-synthesis-"):
            continue
        m = _REVIEW_DATE_RE.match(path.name)
        if not m:
            continue
        try:
            review_date = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            continue
        if review_date < cutoff:
            continue
        try:
            post = frontmatter.load(path)
        except Exception:
            continue
        subject_articles = post.metadata.get("subject_articles")
        if isinstance(subject_articles, list):
            for a in subject_articles:
                if isinstance(a, str):
                    out.add(a)
            continue
        # Legacy fallback: related_articles wikilinks.
        related = post.metadata.get("related_articles")
        if isinstance(related, list):
            for ref in related:
                if not isinstance(ref, str):
                    continue
                # Strip wikilink syntax: "[[topics/foo]]" or "[[foo]]"
                inner = ref.strip("[]")
                if "|" in inner:
                    inner = inner.split("|", 1)[0]
                # Heuristic: only count refs that look like real article
                # paths (contain a section/ prefix). "[[project]]" etc.
                # don't count.
                if "/" in inner:
                    out.add(inner + ".md" if not inner.endswith(".md") else inner)
    return out


def _parse_ai_modified(metadata: dict) -> Optional[datetime]:
    """Pull the most recent modification timestamp from frontmatter."""
    candidates = []
    for key in ("ai_modified", "human_modified", "modified"):
        v = metadata.get(key)
        if v is None:
            continue
        if isinstance(v, datetime):
            candidates.append(v)
            continue
        if isinstance(v, str):
            try:
                candidates.append(datetime.fromisoformat(v))
            except ValueError:
                # `modified` is sometimes YYYY-MM-DD only.
                try:
                    candidates.append(
                        datetime.strptime(v, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                    )
                except ValueError:
                    continue
    if not candidates:
        return None
    out = max(candidates)
    if out.tzinfo is None:
        out = out.replace(tzinfo=timezone.utc)
    return out


def _pick_recent_aged_article(
    now: datetime,
    *,
    min_age_days: int,
    max_age_days: int,
    excluded: set[str],
    article_dirs: list[Path],
) -> Optional[tuple[str, datetime]]:
    """Return (relative_path, ai_modified) of the most-recently-modified
    article whose age is in [min_age_days, max_age_days] and which is not
    in `excluded`. None if no candidate exists.
    """
    min_cutoff = now - timedelta(days=max_age_days)
    max_cutoff = now - timedelta(days=min_age_days)
    best: Optional[tuple[str, datetime]] = None
    for d in article_dirs:
        if not d.exists():
            continue
        for path in d.glob("*.md"):
            if path.name in _INDEX_FILE_NAMES:
                continue
            # Relative-to-obsidian path, e.g. "topics/foo.md".
            rel = f"{d.name}/{path.name}"
            if rel in excluded:
                continue
            try:
                post = frontmatter.load(path)
            except Exception:
                continue
            mod = _parse_ai_modified(post.metadata)
            if mod is None:
                continue
            if mod < min_cutoff:
                continue
            if mod > max_cutoff:
                continue
            if best is None or mod > best[1]:
                best = (rel, mod)
    return best


def select_cycle_subject(
    cycle_date: str,
    now: datetime,
    *,
    min_recent_age_days: int = 7,
    max_recent_age_days: int = 60,
    site_stale_days: int = 7,
    review_dedupe_days: int = 60,
    pending_path: Optional[Path] = None,
    outer_todo_path: Path = OUTER_TODO_PATH,
    reviews_dir: Path = REVIEWS_DIR,
    article_dirs: Optional[list[Path]] = None,
) -> CycleSubject:
    """Run the selection cascade. See module docstring."""
    pending = load_pending(pending_path)

    # 1. Reuse — same-cycle entry already chosen.
    reuse = _reuse_subject_for_cycle(cycle_date, pending)
    if reuse is not None:
        return reuse

    # 2. Queue — pop top of outer-todo.md (without mutating yet).
    if outer_todo_path.exists():
        text = outer_todo_path.read_text(encoding="utf-8")
        tasks = _parse_outer_todo(text)
        top = _select_top_queue_task(tasks)
        if top is not None:
            return _build_queue_subject(top)

    # 3. Site fallback.
    if _site_stale(now, site_stale_days, pending):
        return _build_site_subject()

    # 4. Recent-aged fallback.
    excluded = _articles_recently_outer_reviewed(now, review_dedupe_days, reviews_dir)
    pick = _pick_recent_aged_article(
        now,
        min_age_days=min_recent_age_days,
        max_age_days=max_recent_age_days,
        excluded=excluded,
        article_dirs=article_dirs or ARTICLE_DIRS,
    )
    if pick is not None:
        rel_path, mod = pick
        return _build_recent_subject(rel_path, mod)

    # 5. Nothing to review.
    return _none_subject()


def mark_consumed(
    subject: CycleSubject,
    cycle_date: str,
    *,
    outer_todo_path: Path = OUTER_TODO_PATH,
) -> bool:
    """Mutate outer-todo.md to mark a queue subject consumed.

    No-op for non-queue subjects (returns False). Returns True when the
    file was modified.
    """
    if subject.type != "queue" or not subject.source.startswith("outer-todo.md:L"):
        return False
    line_no = int(subject.source.split(":L", 1)[1])
    text = outer_todo_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    idx = line_no - 1
    if idx < 0 or idx >= len(lines):
        raise ValueError(
            f"mark_consumed: line {line_no} out of range "
            f"({len(lines)} lines in {outer_todo_path})"
        )
    heading = lines[idx]
    m = _PRIORITY_RE.match(heading)
    if not m:
        # Already consumed (### ✓) or schema drifted — refuse.
        if _DONE_RE.match(heading):
            return False
        raise ValueError(
            f"mark_consumed: line {line_no} is not a `### P{{N}}:` heading: "
            f"{heading!r}"
        )
    title = m.group(2).strip()
    lines[idx] = f"### ✓ {cycle_date}: {title}"

    # Append `Reviewed:` footer to the task block (just before next
    # heading or EOF).
    j = idx + 1
    while j < len(lines):
        raw = lines[j]
        if raw.startswith("### ") or raw.startswith("## "):
            break
        j += 1
    # Insert the Reviewed footer inside the block (immediately before
    # whatever currently terminates it).
    insert_at = j
    # Trim a trailing blank within the block so we sit cleanly above any
    # gap before the next heading.
    while insert_at > idx + 1 and not lines[insert_at - 1].strip():
        insert_at -= 1
    lines.insert(insert_at, f"- **Reviewed**: cycle {cycle_date}")

    out_text = "\n".join(lines)
    if text.endswith("\n") and not out_text.endswith("\n"):
        out_text += "\n"
    outer_todo_path.write_text(out_text, encoding="utf-8")
    return True


def _cli_select(args: argparse.Namespace) -> int:
    now = datetime.now(timezone.utc)
    subject = select_cycle_subject(
        cycle_date=args.cycle_date,
        now=now,
        min_recent_age_days=args.min_recent_age_days,
        max_recent_age_days=args.max_recent_age_days,
        site_stale_days=args.site_stale_days,
        review_dedupe_days=args.review_dedupe_days,
    )
    json.dump(asdict(subject), sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


def _cli_mark_consumed(args: argparse.Namespace) -> int:
    # Reconstruct just enough CycleSubject for mark_consumed to find the line.
    subject = CycleSubject(
        type="queue", title="", prompt_seed="", articles=[], source=args.source
    )
    changed = mark_consumed(subject, args.cycle_date)
    json.dump({"changed": changed, "source": args.source}, sys.stdout)
    sys.stdout.write("\n")
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="tools.reviews.subjects")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_sel = sub.add_parser("select", help="Pick the subject for a cycle date.")
    p_sel.add_argument("--cycle-date", required=True, help="YYYY-MM-DD")
    p_sel.add_argument("--min-recent-age-days", type=int, default=7)
    p_sel.add_argument("--max-recent-age-days", type=int, default=60)
    p_sel.add_argument("--site-stale-days", type=int, default=7)
    p_sel.add_argument("--review-dedupe-days", type=int, default=60)
    p_sel.set_defaults(func=_cli_select)

    p_mc = sub.add_parser(
        "mark-consumed", help="Mark a queue task ✓ in outer-todo.md."
    )
    p_mc.add_argument("--source", required=True, help="e.g., outer-todo.md:L24")
    p_mc.add_argument("--cycle-date", required=True, help="YYYY-MM-DD")
    p_mc.set_defaults(func=_cli_mark_consumed)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
