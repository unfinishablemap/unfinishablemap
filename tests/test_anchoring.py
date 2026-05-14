"""Tests for the topic-concept anchoring audit (Audit Three of the
calibration audit triple)."""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.curate.anchoring import (
    DEFAULT_HEDGE_DENSITY_RATIO,
    AnchoringFlag,
    CalibrationProfile,
    compute_profile,
    evaluate_anchoring,
    extract_anchor_slugs,
    format_refine_task,
    get_anchoring_flags,
    resolve_concept_path,
)

# Reusable corpora -----------------------------------------------------------


HEDGED_BODY = (
    "This is a long article body padded to several hundred words so that the "
    "per-thousand-word ratios remain stable; without enough words the audit's "
    "hedge density bounces around on each marker added. " * 40
    + " The hypothesis may be true. The evidence could support it. "
      "Neither interpretation is forced by the data alone. The reading "
      "appears compatible with both framings. Perhaps further work seems warranted."
)

ASSERTIVE_BODY = (
    "This is a long article body padded to several hundred words so that the "
    "per-thousand-word ratios remain stable; without enough words the audit's "
    "hedge density bounces around on each marker added. " * 40
    + " The hypothesis is true. The evidence proves it. The result demonstrates "
      "the central claim. The argument establishes the conclusion. "
      "The data refutes the alternative. The findings confirms the framing."
)


def _make_article(
    tmp_path: Path,
    section: str,
    slug: str,
    *,
    body: str,
    concepts: list[str] | None = None,
    title: str | None = None,
) -> Path:
    section_dir = tmp_path / section
    section_dir.mkdir(parents=True, exist_ok=True)
    concept_lines = ""
    if concepts:
        concept_lines = "concepts:\n" + "".join(
            f'  - "[[{c}]]"\n' for c in concepts
        )
    front = (
        "---\n"
        f"title: \"{title or slug}\"\n"
        f"{concept_lines}"
        "---\n"
    )
    path = section_dir / f"{slug}.md"
    path.write_text(front + body)
    return path


# compute_profile -----------------------------------------------------------


def test_compute_profile_counts_hedges_and_strong_assertions(tmp_path: Path) -> None:
    path = _make_article(tmp_path, "topics", "demo", body=HEDGED_BODY)
    profile = compute_profile(path)
    assert profile is not None
    assert profile.hedge_count >= 5  # may, could, perhaps, appears, seems
    assert profile.strong_assertion_count == 0
    assert profile.underdetermination_marker_count >= 2
    assert profile.hedge_density > 0


def test_compute_profile_assertive_body_has_no_hedges(tmp_path: Path) -> None:
    path = _make_article(tmp_path, "topics", "demo", body=ASSERTIVE_BODY)
    profile = compute_profile(path)
    assert profile is not None
    assert profile.hedge_count == 0
    assert profile.strong_assertion_count >= 5
    assert profile.underdetermination_marker_count == 0


def test_compute_profile_returns_none_for_empty_body(tmp_path: Path) -> None:
    path = _make_article(tmp_path, "topics", "empty", body="")
    assert compute_profile(path) is None


def test_compute_profile_excludes_code_blocks(tmp_path: Path) -> None:
    body = (
        HEDGED_BODY
        + "\n\n```python\n# could may might perhaps possibly\n```\n"
    )
    path = _make_article(tmp_path, "topics", "code", body=body)
    base = compute_profile(_make_article(tmp_path, "topics", "base", body=HEDGED_BODY))
    code = compute_profile(path)
    assert base is not None and code is not None
    # The hedge words inside the code block must not raise the count.
    assert code.hedge_count == base.hedge_count


# extract_anchor_slugs ------------------------------------------------------


def test_extract_anchor_slugs_reads_frontmatter(tmp_path: Path) -> None:
    path = _make_article(
        tmp_path,
        "topics",
        "demo",
        body=HEDGED_BODY,
        concepts=["filter-theory", "default-mode-network"],
    )
    slugs = extract_anchor_slugs(path)
    assert "filter-theory" in slugs
    assert "default-mode-network" in slugs


def test_extract_anchor_slugs_includes_inline_wikilinks(tmp_path: Path) -> None:
    body = (
        "Lead paragraph mentions [[inline-concept]] up front. "
        + HEDGED_BODY
    )
    path = _make_article(
        tmp_path,
        "topics",
        "demo",
        body=body,
        concepts=["explicit-concept"],
    )
    slugs = extract_anchor_slugs(path)
    assert slugs[0] == "explicit-concept"  # frontmatter ordered first
    assert "inline-concept" in slugs


def test_extract_anchor_slugs_dedupes(tmp_path: Path) -> None:
    body = "Mentions [[shared]] [[shared]] again. " + HEDGED_BODY
    path = _make_article(
        tmp_path, "topics", "demo", body=body, concepts=["shared"]
    )
    slugs = extract_anchor_slugs(path)
    assert slugs.count("shared") == 1


def test_extract_anchor_slugs_strips_path_prefix(tmp_path: Path) -> None:
    path = _make_article(
        tmp_path,
        "topics",
        "demo",
        body=HEDGED_BODY,
        concepts=["concepts/filter-theory"],
    )
    assert "filter-theory" in extract_anchor_slugs(path)


# resolve_concept_path -------------------------------------------------------


def test_resolve_concept_path_finds_existing(tmp_path: Path) -> None:
    _make_article(tmp_path, "concepts", "filter-theory", body=HEDGED_BODY)
    resolved = resolve_concept_path("filter-theory", tmp_path)
    assert resolved is not None
    assert resolved.name == "filter-theory.md"


def test_resolve_concept_path_returns_none_for_missing(tmp_path: Path) -> None:
    assert resolve_concept_path("nonexistent", tmp_path) is None


# evaluate_anchoring --------------------------------------------------------


def test_assertive_topic_against_hedged_anchor_is_flagged(tmp_path: Path) -> None:
    _make_article(tmp_path, "concepts", "filter-theory", body=HEDGED_BODY)
    topic = _make_article(
        tmp_path,
        "topics",
        "psychedelics-and-the-filter-model",
        body=ASSERTIVE_BODY,
        concepts=["filter-theory"],
    )

    flags = evaluate_anchoring(topic, tmp_path)
    assert len(flags) == 1
    flag = flags[0]
    assert flag.anchor_concept_path.stem == "filter-theory"
    # All three checks should fire on the extreme contrast.
    assert "hedge_density" in flag.failed_checks
    assert "underdetermination_markers" in flag.failed_checks
    assert flag.severity >= 2


def test_well_calibrated_topic_is_not_flagged(tmp_path: Path) -> None:
    _make_article(tmp_path, "concepts", "filter-theory", body=HEDGED_BODY)
    # Topic with the same body as the anchor concept — calibration matches.
    topic = _make_article(
        tmp_path,
        "topics",
        "demo",
        body=HEDGED_BODY,
        concepts=["filter-theory"],
    )
    assert evaluate_anchoring(topic, tmp_path) == []


def test_short_article_is_skipped(tmp_path: Path) -> None:
    _make_article(tmp_path, "concepts", "filter-theory", body=HEDGED_BODY)
    short_body = "Very short. " * 20
    topic = _make_article(
        tmp_path,
        "topics",
        "demo",
        body=short_body,
        concepts=["filter-theory"],
    )
    # Short article cannot be assessed reliably; the audit skips it.
    assert evaluate_anchoring(topic, tmp_path) == []


def test_missing_anchor_concept_is_skipped(tmp_path: Path) -> None:
    # No concepts/filter-theory.md exists.
    topic = _make_article(
        tmp_path,
        "topics",
        "demo",
        body=ASSERTIVE_BODY,
        concepts=["filter-theory"],
    )
    assert evaluate_anchoring(topic, tmp_path) == []


def test_evaluates_against_multiple_anchors(tmp_path: Path) -> None:
    _make_article(tmp_path, "concepts", "anchor-a", body=HEDGED_BODY)
    _make_article(tmp_path, "concepts", "anchor-b", body=HEDGED_BODY)
    topic = _make_article(
        tmp_path,
        "topics",
        "demo",
        body=ASSERTIVE_BODY,
        concepts=["anchor-a", "anchor-b"],
    )
    flags = evaluate_anchoring(topic, tmp_path)
    assert {f.anchor_concept_path.stem for f in flags} == {"anchor-a", "anchor-b"}


def test_threshold_is_tunable(tmp_path: Path) -> None:
    _make_article(tmp_path, "concepts", "filter-theory", body=HEDGED_BODY)
    # A marginal topic — only some hedging, not enough to clear the 60% bar
    # but enough to pass at 30%.
    marginal_body = HEDGED_BODY.replace("may", "is").replace("could", "is")
    topic = _make_article(
        tmp_path,
        "topics",
        "demo",
        body=marginal_body,
        concepts=["filter-theory"],
    )
    strict = evaluate_anchoring(
        topic, tmp_path, hedge_density_ratio=DEFAULT_HEDGE_DENSITY_RATIO
    )
    lenient = evaluate_anchoring(topic, tmp_path, hedge_density_ratio=0.1)
    # Loosening the ratio should never produce *more* flags than strict.
    assert len(lenient) <= len(strict)


# get_anchoring_flags --------------------------------------------------------


def test_get_anchoring_flags_scans_topics_section(tmp_path: Path) -> None:
    _make_article(tmp_path, "concepts", "anchor", body=HEDGED_BODY)
    _make_article(
        tmp_path, "topics", "flagged", body=ASSERTIVE_BODY, concepts=["anchor"]
    )
    _make_article(
        tmp_path, "topics", "clean", body=HEDGED_BODY, concepts=["anchor"]
    )
    flags = get_anchoring_flags(tmp_path)
    assert len(flags) == 1
    assert flags[0].topic_path.stem == "flagged"


def test_get_anchoring_flags_skips_section_index(tmp_path: Path) -> None:
    _make_article(tmp_path, "concepts", "anchor", body=HEDGED_BODY)
    # obsidian/topics/topics.md is the section index — must not be audited.
    _make_article(
        tmp_path, "topics", "topics", body=ASSERTIVE_BODY, concepts=["anchor"]
    )
    assert get_anchoring_flags(tmp_path) == []


def test_get_anchoring_flags_sort_worst_first(tmp_path: Path) -> None:
    _make_article(tmp_path, "concepts", "anchor", body=HEDGED_BODY)
    # "mild" topic has one hedge marker but no underdetermination phrase;
    # it should fail two checks (hedge density + underdetermination) and
    # rank below "severe" which fails all three.
    mild_body = HEDGED_BODY.replace("Neither interpretation is forced", "").replace(
        "appears compatible with both framings", ""
    )
    mild_body = mild_body.replace("may be true", "is true").replace(
        "could support", "supports"
    ).replace("Perhaps further", "Further").replace(
        "seems warranted", "is warranted"
    )
    _make_article(tmp_path, "topics", "mild", body=mild_body, concepts=["anchor"])
    _make_article(
        tmp_path,
        "topics",
        "severe",
        body=ASSERTIVE_BODY,
        concepts=["anchor"],
    )
    flags = get_anchoring_flags(tmp_path)
    assert len(flags) == 2
    severities = [f.severity for f in flags]
    assert severities == sorted(severities, reverse=True)
    # Worst-first ordering: severe (3 failed) before mild (2 failed).
    assert flags[0].topic_path.stem == "severe"


# format_refine_task --------------------------------------------------------


def test_format_refine_task_produces_task_block(tmp_path: Path) -> None:
    _make_article(tmp_path, "concepts", "filter-theory", body=HEDGED_BODY)
    topic = _make_article(
        tmp_path,
        "topics",
        "psychedelics-and-the-filter-model",
        body=ASSERTIVE_BODY,
        concepts=["filter-theory"],
    )
    flag = evaluate_anchoring(topic, tmp_path)[0]
    block = format_refine_task(flag, "2026-05-14")
    assert block.startswith("### P2: ")
    assert "psychedelics-and-the-filter-model" in block
    assert "[[filter-theory]]" in block
    assert "refine-draft" in block
    assert "topic-concept-anchoring-audit" in block
    assert "Generated**: 2026-05-14" in block


# Corpus smoke test ---------------------------------------------------------


REPO_ROOT = Path(__file__).parent.parent


@pytest.mark.skipif(
    not (REPO_ROOT / "obsidian" / "topics").is_dir(),
    reason="No obsidian corpus available in this checkout.",
)
def test_corpus_smoke_runs_without_error() -> None:
    """The audit must run over the live corpus without raising."""
    flags = get_anchoring_flags(REPO_ROOT / "obsidian")
    assert isinstance(flags, list)
    for f in flags:
        assert isinstance(f, AnchoringFlag)
        assert isinstance(f.topic_profile, CalibrationProfile)
        assert f.severity >= 2
