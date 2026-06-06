"""Tests for the empirical-record currency scanner."""

from __future__ import annotations

from pathlib import Path

from tools.curate.empirical_currency import (
    find_superlative_claims,
    rank_by_currency_risk,
    scan_corpus,
)


def _write(tmp_path: Path, section: str, slug: str, body: str) -> Path:
    section_dir = tmp_path / section
    section_dir.mkdir(parents=True, exist_ok=True)
    path = section_dir / f"{slug}.md"
    path.write_text(f"---\ntitle: {slug}\n---\n{body}")
    return path


def test_finds_current_record_claim(tmp_path: Path) -> None:
    body = "Fein et al. 2019 holds the current record for macromolecule interferometry."
    path = _write(tmp_path, "topics", "macromolecule", body)
    claims = find_superlative_claims(path)
    assert len(claims) == 1
    assert claims[0].matched_phrase.lower() == "current record"
    assert "macromolecule interferometry" in claims[0].context


def test_finds_first_to_demonstrate(tmp_path: Path) -> None:
    body = "Smith et al. 2024 was the first to demonstrate the effect at room temperature."
    path = _write(tmp_path, "topics", "demo", body)
    claims = find_superlative_claims(path)
    assert any("first to demonstrate" in c.matched_phrase.lower() for c in claims)


def test_skips_code_blocks(tmp_path: Path) -> None:
    body = (
        "Normal text without claims.\n"
        "```python\n# current record largest first to demonstrate\n```\n"
        "More normal text."
    )
    path = _write(tmp_path, "topics", "codey", body)
    assert find_superlative_claims(path) == []


def test_so_far_is_flagged_but_so_far_as_is_not(tmp_path: Path) -> None:
    # Hits both forms; "so far as" must be excluded.
    body = (
        "The AWARE studies have so far returned zero hits. "
        "So far as the framework allows, this is consistent."
    )
    path = _write(tmp_path, "topics", "so-far-edge", body)
    claims = find_superlative_claims(path)
    # Exactly one match — the bare "so far"; the "so far as" form is excluded.
    assert len(claims) == 1
    assert claims[0].context.startswith("The AWARE")


def test_clean_article_returns_no_claims(tmp_path: Path) -> None:
    body = (
        "This article describes a phenomenon without making record claims. "
        "It cites multiple studies but does not assert any single result is "
        "the best, largest, or first."
    )
    path = _write(tmp_path, "topics", "calm", body)
    assert find_superlative_claims(path) == []


def test_scan_corpus_filters_by_section(tmp_path: Path) -> None:
    _write(tmp_path, "topics", "with-claim",
           "Smith et al. 2024 holds the current record.")
    _write(tmp_path, "concepts", "with-claim",
           "This is the current record but in concepts dir.")
    results = scan_corpus(tmp_path, sections=["topics"])
    assert len(results) == 1
    assert next(iter(results.keys())).parts[-2] == "topics"


def test_scan_corpus_excludes_section_index(tmp_path: Path) -> None:
    _write(tmp_path, "topics", "topics",
           "Index page mentioning current record should be skipped.")
    _write(tmp_path, "topics", "real-article",
           "Smith 2024 holds the current record.")
    results = scan_corpus(tmp_path, sections=["topics"])
    assert len(results) == 1
    assert next(iter(results.keys())).stem == "real-article"


def test_rank_orders_by_descending_count(tmp_path: Path) -> None:
    _write(tmp_path, "topics", "two-claims",
           "The current record holder is Smith. So far no rival has emerged.")
    _write(tmp_path, "topics", "one-claim",
           "Jones holds the largest known value to date.")
    # to date + largest known = 2; let me re-check that my regex requires the
    # full phrase. "largest known" → match; "to date" → match. So one-claim has 2.
    # Use simpler examples to make ordering crisp.
    _write(tmp_path, "topics", "three-claims",
           "First to demonstrate, current record, and largest ever recorded.")
    results = scan_corpus(tmp_path)
    ranked = rank_by_currency_risk(results)
    counts = [c for _, c in ranked]
    assert counts == sorted(counts, reverse=True)
    # The three-claims article should be first.
    assert ranked[0][0].stem == "three-claims"
