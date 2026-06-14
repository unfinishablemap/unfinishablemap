"""Harvest research-topic subjects from the outer/optimistic review corpus.

Motivation: the loop's organic research generators dried up. Replenish mints
expand-topic candidates only from gap analysis (mature corpus → nothing) and
dedupes anything it does propose against the 572-entry Vetoed Tasks bank, so
new-article generation stalled even though topics/concepts have cap headroom
(newest research note was ~7 weeks stale at build time). Meanwhile the outer
reviews — three frontier models independently naming what the corpus does NOT
cover — were mined only for refine-draft fixes to existing articles (45
refine-draft tasks vs 0 research-topic).

This harvester closes that gap: it scans the review files that NOMINATE NEW
TERRITORY (outer-review, outer-review-synthesis, optimistic) for "not covered"
findings and mints `research-topic` tasks. Crucially it dedupes against LIVE
ARTICLES and EXISTING RESEARCH NOTES — NOT against the Vetoed bank — so the
parked-idea backlog no longer suppresses fresh research. The research→
expand-topic chain then lands new articles in the now-uncapped sections.

The semantic extraction ("which findings name an uncovered subject?") is LLM
judgment and lives in the harvest-research-subjects SKILL. This module is the
mechanical half: enumerate unscanned reviews, dedupe candidate subjects, write
tasks, and persist scan/mint state outside cycle_post's YAML re-serialization.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = REPO_ROOT.parent / "unfinishablemap_log"
STATE_PATH = LOG_DIR / "research-harvest-state.json"

REVIEWS_DIR = REPO_ROOT / "obsidian" / "reviews"
RESEARCH_DIR = REPO_ROOT / "obsidian" / "research"
TODO_PATH = REPO_ROOT / "obsidian" / "workflow" / "todo.md"

# Review file prefixes that NOMINATE NEW TERRITORY. deep-review / pessimistic /
# tenet-check / system-tune critique existing articles and are deliberately
# excluded — they feed refine-draft, not research-topic.
SUBJECT_MINE_PREFIXES = (
    "outer-review-synthesis-",
    "outer-review-",
    "optimistic-",
)

# Sections a harvested subject may target. voids is omitted: it is at cap and
# has its own research-voids generator.
ALLOWED_TARGET_SECTIONS = ("topics", "concepts")

# Article sections to dedupe against (a subject already covered anywhere is not
# new). Includes apex/positions/voids even though we don't TARGET them.
ARTICLE_SECTIONS = ("topics", "concepts", "voids", "apex", "positions")

# How many reviews the skill should read per run, and how many tasks to mint.
# Bounds per-run cost and prevents flooding the queue from the backlog.
DEFAULT_READ_BATCH = 8
DEFAULT_MINT_CAP = 4


@dataclass
class HarvestState:
    scanned_reviews: set[str] = field(default_factory=set)
    minted_subjects: set[str] = field(default_factory=set)
    last_run: str | None = None

    @classmethod
    def load(cls) -> "HarvestState":
        if not STATE_PATH.exists():
            return cls()
        try:
            raw = json.loads(STATE_PATH.read_text())
        except (json.JSONDecodeError, OSError):
            return cls()
        return cls(
            scanned_reviews=set(raw.get("scanned_reviews", [])),
            minted_subjects=set(raw.get("minted_subjects", [])),
            last_run=raw.get("last_run"),
        )

    def save(self) -> None:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        STATE_PATH.write_text(
            json.dumps(
                {
                    "scanned_reviews": sorted(self.scanned_reviews),
                    "minted_subjects": sorted(self.minted_subjects),
                    "last_run": self.last_run,
                },
                indent=2,
            )
            + "\n"
        )


def slugify(text: str) -> str:
    """'Chemosensory Qualia (Olfaction/Gustation)' → 'chemosensory-qualia-olfaction-gustation'."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def _strip_trailing_date(stem: str) -> str:
    """'berridge-wanting-liking-2026-06-03' → 'berridge-wanting-liking'."""
    return re.sub(r"-20\d{2}-\d{2}-\d{2}$", "", stem)


def existing_article_slugs() -> set[str]:
    """Slugs of every live and archived article (the real 'already covered' set)."""
    slugs: set[str] = set()
    for base in (REPO_ROOT / "obsidian", REPO_ROOT / "archive"):
        for section in ARTICLE_SECTIONS:
            d = base / section
            if not d.is_dir():
                continue
            for f in d.glob("*.md"):
                if f.stem == section:  # section index file
                    continue
                slugs.add(f.stem)
    return slugs


def existing_research_slugs() -> set[str]:
    """Subject slugs already covered by a research note (date suffix stripped)."""
    if not RESEARCH_DIR.is_dir():
        return set()
    return {_strip_trailing_date(f.stem) for f in RESEARCH_DIR.glob("*.md")}


def _review_date_key(name: str) -> str:
    """Extract the embedded YYYY-MM-DD for cross-prefix newest-first ordering.

    Sorting by raw filename would group by prefix (all synthesis, then all
    outer, then all optimistic), stranding the large optimistic backlog behind
    the daily-refreshing outer stream. Keying on the date interleaves all three
    sources so each run sees the freshest material regardless of type.
    """
    m = re.search(r"(20\d{2}-\d{2}-\d{2})", name)
    return m.group(1) if m else "0000-00-00"


def mine_review_files() -> list[Path]:
    """New-territory review files, newest first by embedded date then name."""
    if not REVIEWS_DIR.is_dir():
        return []
    files = [
        f
        for f in REVIEWS_DIR.glob("*.md")
        if f.name.startswith(SUBJECT_MINE_PREFIXES)
    ]
    return sorted(files, key=lambda f: (_review_date_key(f.name), f.name), reverse=True)


def unscanned_reviews(state: HarvestState, limit: int = DEFAULT_READ_BATCH) -> list[Path]:
    """Up to `limit` newest mine-reviews not yet scanned."""
    return [f for f in mine_review_files() if f.name not in state.scanned_reviews][:limit]


@dataclass
class DedupeResult:
    kept: list[dict]
    rejected: list[tuple[dict, str]]  # (subject, reason)


def dedupe_subjects(subjects: list[dict], state: HarvestState) -> DedupeResult:
    """Drop subjects already covered by an article, a research note, or a prior mint.

    NB: deliberately does NOT dedupe against the Vetoed Tasks bank — that
    suppression is exactly what stalled new-article generation. A subject the
    operator once parked is fair game again when an external reviewer re-raises
    it as an uncovered gap.
    """
    articles = existing_article_slugs()
    research = existing_research_slugs()
    kept: list[dict] = []
    rejected: list[tuple[dict, str]] = []
    seen_this_batch: set[str] = set()

    for s in subjects:
        slug = s.get("slug") or slugify(s.get("title", ""))
        s["slug"] = slug
        target = s.get("target_section", "topics")
        if not slug:
            rejected.append((s, "empty slug"))
        elif target not in ALLOWED_TARGET_SECTIONS:
            rejected.append((s, f"target_section '{target}' not in {ALLOWED_TARGET_SECTIONS}"))
        elif slug in articles:
            rejected.append((s, "already a live/archived article"))
        elif slug in research:
            rejected.append((s, "already has a research note"))
        elif slug in state.minted_subjects:
            rejected.append((s, "already minted in a prior harvest"))
        elif slug in seen_this_batch:
            rejected.append((s, "duplicate within this batch"))
        else:
            seen_this_batch.add(slug)
            kept.append(s)
    return DedupeResult(kept=kept, rejected=rejected)


def _research_task_block(subject: dict, today: str) -> str:
    title = subject["title"].strip()
    slug = subject["slug"]
    target = subject.get("target_section", "topics")
    rationale = subject.get("rationale", "").strip()
    source = subject.get("source_review", "outer/optimistic review")
    priority = subject.get("priority", "P2")
    return (
        f"### {priority}: Research {title}\n"
        f"- **Type**: research-topic\n"
        f"- **Notes**: Harvested from the review corpus ({source}) by "
        f"/harvest-research-subjects — an external/optimistic reviewer flagged this as "
        f"uncovered territory. {rationale} Target section: {target} (cap headroom confirmed "
        f"at harvest). Output a research note to obsidian/research/{slug}-{today}.md; the "
        f"research→expand-topic chain may then create a new {target}/ article. Dedupe: no "
        f"live/archived article and no existing research note for '{slug}' at harvest time. "
        f"NOT deduped against the Vetoed bank by design — verify the subject is genuinely "
        f"worth covering before writing (assess-first, license-to-decline).\n"
        f"- **Source**: research-harvest\n"
        f"- **Generated**: {today}\n"
    )


def mint_tasks(subjects: list[dict], today: str, todo_path: Path | None = None) -> int:
    """Insert research-topic task blocks at the top of Active Tasks. Returns count written.

    `todo_path` resolves to the module TODO_PATH at call time (not def time) so
    tests can monkeypatch the module constant without the default capturing the
    original value.
    """
    if not subjects:
        return 0
    todo_path = todo_path or TODO_PATH
    todo = todo_path.read_text()
    marker = "## Active Tasks\n"
    idx = todo.find(marker)
    if idx == -1:
        raise ValueError("todo.md has no '## Active Tasks' section")
    insert_at = idx + len(marker)
    blocks = "\n" + "\n".join(_research_task_block(s, today) for s in subjects)
    todo_path.write_text(todo[:insert_at] + blocks + todo[insert_at:])
    return len(subjects)


def harvest(
    subjects: list[dict],
    scanned: list[str],
    mint_cap: int = DEFAULT_MINT_CAP,
    now: datetime | None = None,
) -> dict:
    """Dedupe candidate subjects, mint up to `mint_cap`, mark reviews scanned, persist state.

    `subjects` are the LLM-extracted candidates from the skill; `scanned` is the
    list of review filenames the skill read this run (marked scanned whether or
    not they yielded subjects, so the backlog drains).
    """
    now = now or datetime.now(timezone.utc)
    today = now.date().isoformat()
    state = HarvestState.load()

    result = dedupe_subjects(subjects, state)
    to_mint = result.kept[:mint_cap]
    overflow = result.kept[mint_cap:]

    minted = mint_tasks(to_mint, today)
    for s in to_mint:
        state.minted_subjects.add(s["slug"])
    state.scanned_reviews.update(scanned)
    state.last_run = now.isoformat()
    state.save()

    return {
        "minted": minted,
        "minted_slugs": [s["slug"] for s in to_mint],
        "deferred_over_cap": [s["slug"] for s in overflow],
        "rejected": [(s.get("slug", ""), reason) for s, reason in result.rejected],
        "scanned_count": len(scanned),
    }
