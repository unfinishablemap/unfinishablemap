"""Detect whether a research note has already been consumed into an article.

The replenisher's `unconsumed_research` source needs to avoid generating
expand-topic tasks when the topic already has an article under a phrasing
variant of the research-note slug, or when the research has been coalesced
into an archived article.

This module provides phrasing-aware slug matching that handles common
variants:
- Stop-word differences ("normativity-of-reason" vs "the-normativity-of-reason")
- Underscore vs hyphen punctuation
- Singular/plural and gerund inflection (light stemming)
- Reordered tokens (set-based comparison)
- Domain-specific compound terms shared across rephrasings (e.g.
  "dualism-taxonomy" appearing in both "min-max-dualism-taxonomy" and
  "four-quadrant-dualism-taxonomy")

The matching is conservative: false negatives (genuinely-unconsumed research
that fuzzy-matches an unrelated article and is suppressed) are worse than
false positives (a duplicate task that the operator notices and abandons).
The thresholds below are chosen so that only highly-overlapping slugs match.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# Sections that count as "article catalogue" — research consumed into any of
# these (or their archived counterparts) is considered already covered.
ARTICLE_SECTIONS = ("topics", "concepts", "voids", "apex")

# Common English particles and connectives that vary between phrasings.
# Excluding these from token comparison handles "the/a/an"-type noise.
STOPWORDS: frozenset[str] = frozenset(
    {
        "the",
        "a",
        "an",
        "and",
        "or",
        "of",
        "in",
        "on",
        "to",
        "for",
        "with",
        "as",
        "is",
        "are",
        "be",
        "by",
        "vs",
        "versus",
        "from",
        "at",
    }
)

# Trailing date suffix on research filenames: e.g. "-2026-04-07".
_DATE_SUFFIX_RE = re.compile(r"-\d{4}-\d{2}-\d{2}$")

# Light morphological stemming. Order matters: longer suffixes first, so
# "normativity" doesn't reduce via "-y" before the "-ity" rule fires.
_STEM_SUFFIXES: tuple[str, ...] = (
    "ization",
    "isation",
    "ities",
    "ality",
    "ation",
    "ity",
    "ings",
    "ing",
    "ies",
    "ed",
    "es",
    "s",
)

# Confidence tiers, ordered most → least confident.
CONFIDENCE_EXACT = "exact"
CONFIDENCE_STOPWORD = "stopword-equivalent"
CONFIDENCE_FUZZY = "fuzzy"


@dataclass(frozen=True)
class Match:
    """A candidate article that already covers a research note's topic."""

    path: Path
    confidence: str
    score: float
    reason: str


def research_slug(filename: str) -> str:
    """Extract the topical slug from a research filename, stripping date suffix.

    Examples:
        >>> research_slug("consciousness-normativity-of-reason-2026-04-07.md")
        'consciousness-normativity-of-reason'
        >>> research_slug("min-max-dualism-taxonomy-2026-04-21.md")
        'min-max-dualism-taxonomy'
        >>> research_slug("voids-vagueness-void-2026-04-30.md")
        'voids-vagueness-void'
    """
    stem = Path(filename).stem
    return _DATE_SUFFIX_RE.sub("", stem)


def _stem(token: str) -> str:
    """Conservative stemming: reduce common English suffixes.

    Only strips the suffix when the stem retains at least 4 characters,
    avoiding over-aggressive reductions like "is" → "i". Also preserves
    "-ss" endings (consciousness, awareness, process) so the bare "-s"
    rule doesn't mangle non-plural nouns ending in double-s.
    """
    for suffix in _STEM_SUFFIXES:
        if not token.endswith(suffix):
            continue
        if len(token) <= len(suffix) + 3:
            continue
        # Don't strip bare "s" from "-ss" tails — those are noun endings
        # like "consciousness" / "awareness" / "process", not plurals.
        if suffix == "s" and len(token) >= 2 and token[-2] == "s":
            continue
        return token[: -len(suffix)]
    return token


def normalize_tokens(slug: str) -> list[str]:
    """Split a slug into stemmed, stopword-filtered tokens.

    Input is lowercased; hyphens, underscores, slashes, and whitespace all
    serve as token boundaries. Empty tokens and stopwords are dropped.
    Remaining tokens are passed through `_stem` for light morphological
    normalisation.

    Order is preserved so callers can build n-grams.
    """
    if not slug:
        return []
    parts = re.split(r"[-_\s/]+", slug.lower().strip())
    return [_stem(p) for p in parts if p and p not in STOPWORDS]


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def _shared_bigrams(a: list[str], b: list[str]) -> set[tuple[str, str]]:
    """Return contiguous 2-token n-grams present in both token sequences."""
    if len(a) < 2 or len(b) < 2:
        return set()
    a_grams = {(a[i], a[i + 1]) for i in range(len(a) - 1)}
    b_grams = {(b[i], b[i + 1]) for i in range(len(b) - 1)}
    return a_grams & b_grams


def slug_similarity(research: str, candidate: str) -> Match | None:
    """Compare a research-note slug against a candidate article slug.

    Returns a Match describing the highest-confidence relationship found,
    or None if the slugs are not similar enough to be considered the same
    topic.

    Tier 1 (`exact`): the slugs are identical after lowercasing and
    punctuation normalisation.

    Tier 2 (`stopword-equivalent`): token sets are equal after stopword
    removal and stemming. Catches phrasing variants like
    "normativity-of-reason" vs "the-normativity-of-reason".

    Tier 3 (`fuzzy`): a shared compound bigram (e.g. "dualism-taxonomy")
    plus a Jaccard token overlap of at least 0.3, OR Jaccard >= 0.5 alone.
    Catches synonymous rephrasings around a shared technical kernel
    (e.g. "min-max-dualism-taxonomy" vs "four-quadrant-dualism-taxonomy").
    """
    if not research or not candidate:
        return None

    norm_r = research.lower().replace("_", "-")
    norm_c = candidate.lower().replace("_", "-")
    if norm_r == norm_c:
        return Match(path=Path(), confidence=CONFIDENCE_EXACT, score=1.0, reason="identical slug")

    r_tokens = normalize_tokens(research)
    c_tokens = normalize_tokens(candidate)
    if not r_tokens or not c_tokens:
        return None

    r_set = set(r_tokens)
    c_set = set(c_tokens)

    if r_set == c_set:
        return Match(
            path=Path(),
            confidence=CONFIDENCE_STOPWORD,
            score=1.0,
            reason="token sets equal after stopword removal",
        )

    j = _jaccard(r_set, c_set)

    if j >= 0.5 and len(r_set & c_set) >= 2:
        return Match(
            path=Path(),
            confidence=CONFIDENCE_FUZZY,
            score=j,
            reason=f"high token overlap (Jaccard={j:.2f})",
        )

    bigrams = _shared_bigrams(r_tokens, c_tokens)
    if bigrams and j >= 0.3:
        bigram = next(iter(bigrams))
        return Match(
            path=Path(),
            confidence=CONFIDENCE_FUZZY,
            score=j,
            reason=f"shared bigram '{'-'.join(bigram)}' (Jaccard={j:.2f})",
        )

    return None


def find_matching_articles(
    research_path: Path,
    repo_root: Path,
    sections: tuple[str, ...] = ARTICLE_SECTIONS,
) -> list[Match]:
    """Find articles whose slug matches the given research note.

    Searches `obsidian/{section}/` and `archive/{section}/` for each section
    in `sections`. Articles consumed into archived (coalesced) pages are
    treated as covering the research note, since their URL is preserved
    and the content lives elsewhere in the catalogue.

    Returns matches sorted by score (descending). Section index files
    (e.g. `topics.md`) are excluded — they describe the section, not a
    topic that could consume research.
    """
    slug = research_slug(research_path.name)

    matches: list[Match] = []
    for base in (repo_root / "obsidian", repo_root / "archive"):
        for section in sections:
            section_dir = base / section
            if not section_dir.exists():
                continue
            for md_file in section_dir.glob("*.md"):
                # Skip section index files: their stem matches the section name
                # (e.g. obsidian/topics/topics.md serves as the section landing).
                if md_file.stem == section:
                    continue
                m = slug_similarity(slug, md_file.stem)
                if m is None:
                    continue
                rel_path = md_file.relative_to(repo_root)
                matches.append(
                    Match(
                        path=rel_path,
                        confidence=m.confidence,
                        score=m.score,
                        reason=m.reason,
                    )
                )

    # Most confident first; among ties, prefer live obsidian/ matches over
    # archived ones, then shorter paths.
    def sort_key(m: Match) -> tuple[float, int, int, int]:
        is_archive = 1 if m.path.parts and m.path.parts[0] == "archive" else 0
        return (-m.score, _confidence_rank(m.confidence), is_archive, len(str(m.path)))

    matches.sort(key=sort_key)
    return matches


def _confidence_rank(confidence: str) -> int:
    """Order confidence tiers for sorting (lower = more confident)."""
    if confidence == CONFIDENCE_EXACT:
        return 0
    if confidence == CONFIDENCE_STOPWORD:
        return 1
    if confidence == CONFIDENCE_FUZZY:
        return 2
    return 3


def is_research_consumed(
    research_path: Path,
    repo_root: Path,
    min_confidence: str = CONFIDENCE_FUZZY,
) -> Match | None:
    """Return the best match if the research is considered already consumed.

    By default (`min_confidence=CONFIDENCE_FUZZY`) all confidence tiers are
    treated as evidence the research is consumed. Callers that need a stricter
    bar can pass `CONFIDENCE_STOPWORD` or `CONFIDENCE_EXACT`.

    Returns None if no match meets the bar.
    """
    threshold = _confidence_rank(min_confidence)
    for match in find_matching_articles(research_path, repo_root):
        if _confidence_rank(match.confidence) <= threshold:
            return match
    return None
