"""Tests for research-note → article matching used by the replenisher."""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.curate.research_match import (
    CONFIDENCE_EXACT,
    CONFIDENCE_FUZZY,
    CONFIDENCE_STOPWORD,
    find_matching_articles,
    is_research_consumed,
    normalize_tokens,
    research_slug,
    slug_similarity,
)

REPO_ROOT = Path(__file__).parent.parent


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_research(tmp_path: Path, name: str, content: str = "# stub\n") -> Path:
    research_dir = tmp_path / "obsidian" / "research"
    research_dir.mkdir(parents=True, exist_ok=True)
    path = research_dir / name
    path.write_text(content)
    return path


def _make_article(tmp_path: Path, section: str, name: str, base: str = "obsidian") -> Path:
    section_dir = tmp_path / base / section
    section_dir.mkdir(parents=True, exist_ok=True)
    path = section_dir / name
    path.write_text("# stub\n")
    return path


# ---------------------------------------------------------------------------
# research_slug — date suffix handling
# ---------------------------------------------------------------------------


def test_research_slug_strips_date_suffix() -> None:
    assert research_slug("consciousness-normativity-of-reason-2026-04-07.md") == (
        "consciousness-normativity-of-reason"
    )
    assert research_slug("min-max-dualism-taxonomy-2026-04-21.md") == "min-max-dualism-taxonomy"


def test_research_slug_handles_no_date() -> None:
    assert research_slug("epiphenomenalism.md") == "epiphenomenalism"


def test_research_slug_handles_voids_prefix() -> None:
    assert research_slug("voids-vagueness-void-2026-04-30.md") == "voids-vagueness-void"


# ---------------------------------------------------------------------------
# normalize_tokens — stopword removal and stemming
# ---------------------------------------------------------------------------


def test_normalize_tokens_drops_stopwords() -> None:
    assert normalize_tokens("the-normativity-of-reason") == ["normativ", "reason"]
    assert normalize_tokens("consciousness-and-the-normativity-of-reason") == [
        "consciousness",
        "normativ",
        "reason",
    ]


def test_normalize_tokens_stems_inflections() -> None:
    # "ities" suffix should reduce; same root stays comparable across variants.
    assert normalize_tokens("normativities") == normalize_tokens("normativity")


def test_normalize_tokens_handles_underscores_and_slashes() -> None:
    assert normalize_tokens("free_will/agent-causation") == ["free", "will", "agent", "caus"]


def test_normalize_tokens_returns_empty_for_blank() -> None:
    assert normalize_tokens("") == []
    assert normalize_tokens("   ") == []


# ---------------------------------------------------------------------------
# slug_similarity — confidence tiers
# ---------------------------------------------------------------------------


def test_identical_slugs_return_exact() -> None:
    m = slug_similarity("free-will", "free-will")
    assert m is not None
    assert m.confidence == CONFIDENCE_EXACT


def test_underscore_vs_hyphen_returns_exact() -> None:
    m = slug_similarity("free_will", "free-will")
    assert m is not None
    assert m.confidence == CONFIDENCE_EXACT


def test_stopword_difference_returns_stopword_equivalent() -> None:
    """Case 1 from the optimistic-2026-04-30e review."""
    m = slug_similarity(
        "consciousness-normativity-of-reason",
        "consciousness-and-the-normativity-of-reason",
    )
    assert m is not None
    assert m.confidence == CONFIDENCE_STOPWORD
    assert m.score == pytest.approx(1.0)


def test_shared_compound_term_returns_fuzzy() -> None:
    """Case 2 from the optimistic-2026-04-30e review.

    "min-max-dualism-taxonomy" (research) and "four-quadrant-dualism-taxonomy"
    (article) share the compound term "dualism-taxonomy" but otherwise differ
    in their descriptive prefix. The fuzzy tier should catch this.
    """
    m = slug_similarity("min-max-dualism-taxonomy", "four-quadrant-dualism-taxonomy")
    assert m is not None
    assert m.confidence == CONFIDENCE_FUZZY
    assert "dualism" in m.reason and "taxonomy" in m.reason


def test_unrelated_slugs_return_none() -> None:
    """The matcher must not collapse different topics that share one stopword."""
    assert slug_similarity("free-will", "epiphenomenalism") is None
    assert slug_similarity("hard-problem-of-consciousness", "panpsychism") is None
    assert slug_similarity("quantum-measurement", "moral-realism") is None


def test_single_shared_token_does_not_match() -> None:
    """A single shared content token without a compound bigram is not enough."""
    # Both contain "consciousness" but otherwise diverge entirely.
    assert slug_similarity("consciousness-and-time", "consciousness-and-creativity") is None


def test_high_overlap_without_bigram_returns_fuzzy() -> None:
    """Many shared tokens but no contiguous bigram still meets the 0.5 threshold."""
    # Shared tokens: {hard, problem, consciousness}; reordered.
    m = slug_similarity(
        "hard-problem-of-consciousness",
        "consciousness-hard-problem",
    )
    assert m is not None
    assert m.confidence in (CONFIDENCE_FUZZY, CONFIDENCE_STOPWORD)


def test_voids_research_matches_voids_article() -> None:
    """`voids-vagueness-void` (research naming convention) → `vagueness-void`."""
    m = slug_similarity("voids-vagueness-void", "vagueness-void")
    assert m is not None
    # Set-equality after stemming: {void, vagueness} == {vagueness, void}
    assert m.confidence == CONFIDENCE_STOPWORD


# ---------------------------------------------------------------------------
# find_matching_articles — directory scanning
# ---------------------------------------------------------------------------


def test_find_matches_in_obsidian_topics(tmp_path: Path) -> None:
    research = _make_research(tmp_path, "free-will-2026-01-01.md")
    article = _make_article(tmp_path, "topics", "free-will.md")

    matches = find_matching_articles(research, tmp_path)
    assert len(matches) == 1
    assert matches[0].path == article.relative_to(tmp_path)
    assert matches[0].confidence == CONFIDENCE_EXACT


def test_find_matches_includes_archive(tmp_path: Path) -> None:
    """Archived articles should count as covering research."""
    research = _make_research(tmp_path, "old-topic-2026-01-01.md")
    archived = _make_article(tmp_path, "topics", "old-topic.md", base="archive")

    matches = find_matching_articles(research, tmp_path)
    assert len(matches) == 1
    assert matches[0].path == archived.relative_to(tmp_path)


def test_find_matches_searches_apex_voids_concepts(tmp_path: Path) -> None:
    research = _make_research(tmp_path, "binding-problem-2026-01-01.md")
    concept = _make_article(tmp_path, "concepts", "binding-problem.md")

    matches = find_matching_articles(research, tmp_path)
    assert len(matches) == 1
    assert matches[0].path.parts[0] == "obsidian"
    assert matches[0].path.parts[1] == "concepts"
    _ = concept  # keep created file in scope


def test_find_matches_excludes_section_index_files(tmp_path: Path) -> None:
    """`obsidian/topics/topics.md` is the section landing page, not a topic."""
    research = _make_research(tmp_path, "topics-2026-01-01.md")
    _make_article(tmp_path, "topics", "topics.md")

    matches = find_matching_articles(research, tmp_path)
    assert matches == []


def test_find_matches_orders_obsidian_before_archive(tmp_path: Path) -> None:
    """When both live and archived articles match, prefer the live one."""
    research = _make_research(tmp_path, "topic-2026-01-01.md")
    _make_article(tmp_path, "topics", "topic.md")
    _make_article(tmp_path, "topics", "topic.md", base="archive")

    matches = find_matching_articles(research, tmp_path)
    assert len(matches) == 2
    assert matches[0].path.parts[0] == "obsidian"
    assert matches[1].path.parts[0] == "archive"


def test_is_research_consumed_returns_match(tmp_path: Path) -> None:
    research = _make_research(tmp_path, "free-will-2026-01-01.md")
    _make_article(tmp_path, "topics", "free-will.md")

    match = is_research_consumed(research, tmp_path)
    assert match is not None
    assert match.confidence == CONFIDENCE_EXACT


def test_is_research_consumed_returns_none_for_uncovered_topic(tmp_path: Path) -> None:
    research = _make_research(tmp_path, "novel-research-topic-2026-01-01.md")
    _make_article(tmp_path, "topics", "completely-different-subject.md")

    assert is_research_consumed(research, tmp_path) is None


def test_is_research_consumed_respects_min_confidence(tmp_path: Path) -> None:
    """A fuzzy match should not register when the bar is set to exact."""
    research = _make_research(tmp_path, "min-max-dualism-taxonomy-2026-01-01.md")
    _make_article(tmp_path, "topics", "four-quadrant-dualism-taxonomy.md")

    # At fuzzy confidence (the default), the case-2 match registers:
    assert is_research_consumed(research, tmp_path) is not None
    # At exact confidence, it doesn't:
    assert is_research_consumed(research, tmp_path, min_confidence=CONFIDENCE_EXACT) is None


# ---------------------------------------------------------------------------
# Corpus sweep — exercises against the actual repository
# ---------------------------------------------------------------------------


@pytest.mark.skipif(
    not (REPO_ROOT / "obsidian" / "research").exists(),
    reason="No research corpus available in this checkout.",
)
def test_corpus_sweep_catches_known_review_cases() -> None:
    """Both review-documented misses must now be caught by the matcher."""
    case_1 = REPO_ROOT / "obsidian/research/consciousness-normativity-of-reason-2026-04-07.md"
    case_2 = REPO_ROOT / "obsidian/research/min-max-dualism-taxonomy-2026-04-21.md"

    if case_1.exists():
        match_1 = is_research_consumed(case_1, REPO_ROOT)
        assert match_1 is not None, (
            "Case 1 (consciousness-normativity-of-reason) should match "
            "topics/consciousness-and-the-normativity-of-reason.md"
        )
        assert "normativity-of-reason" in str(match_1.path)

    if case_2.exists():
        match_2 = is_research_consumed(case_2, REPO_ROOT)
        assert match_2 is not None, (
            "Case 2 (min-max-dualism-taxonomy) should match "
            "topics/four-quadrant-dualism-taxonomy.md via shared 'dualism-taxonomy' bigram"
        )
        assert "dualism-taxonomy" in str(match_2.path)


@pytest.mark.skipif(
    not (REPO_ROOT / "obsidian" / "research").exists(),
    reason="No research corpus available in this checkout.",
)
def test_corpus_sweep_does_not_explode() -> None:
    """Sanity check: the matcher runs over the whole corpus without error.

    Also produces a useful diagnostic count of how many research notes are
    flagged as consumed, which is what the replenisher will skip.
    """
    research_dir = REPO_ROOT / "obsidian" / "research"
    research_files = list(research_dir.glob("*.md"))
    assert research_files, "Expected research notes to exist in the corpus."

    consumed = 0
    for path in research_files:
        match = is_research_consumed(path, REPO_ROOT)
        if match is not None:
            consumed += 1

    # Rough sanity bound: with 350+ research notes and 200+ articles per
    # section, *some* should match but it should be well below all of them.
    # The exact count drifts as content evolves, so we use a loose floor/ceiling.
    assert 0 < consumed < len(research_files)
