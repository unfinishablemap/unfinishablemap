"""Tests for the altered-state symmetry audit (Audit Two of the calibration
audit triple)."""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.curate.altered_state_symmetry import (
    SymmetryFlag,
    SymmetryProfile,
    compute_symmetry_profile,
    evaluate_symmetry,
    format_refine_task,
    get_symmetry_flags,
)

# Reusable corpora -----------------------------------------------------------

# A body long enough to clear the min-word-count gate. Cites filter theory
# and two supportive-cluster items (psychedelics and NDEs) but no disruptive
# cluster — the canonical Audit-Two failure mode.
ASYMMETRIC_BODY = (
    "This article surveys altered-state evidence for filter theory in detail. "
    "Padding sentences fill out the word count so the audit's min-word-count "
    "gate is cleared without the symmetry-specific markers being affected. " * 30
    + " Psychedelic experience under psilocybin and DMT reveals filter-loosening. "
      "Near-death experiences exhibit the same filter-loosening pattern; "
      "ego-dissolution under LSD likewise. The convergence is striking and "
      "supports the filter framing across independent altered-state cases."
)

# Same body but also engages the disruptive cluster — anaesthesia, slow-wave
# sleep, brain damage — and explicitly names the symmetric burden in
# production-framing language. The audit should clear this article.
SYMMETRIC_BODY = (
    ASYMMETRIC_BODY
    + " The symmetric counter-question is unavoidable: anaesthesia, "
      "slow-wave sleep, and brain damage decrease brain activity and "
      "experience contracts to nothing. The same move is available to "
      "production theorists; both framings accommodate the full set of "
      "altered states by structurally identical moves. The supportive "
      "cluster cannot honestly be cited as multiple independent "
      "confirmations of filter theory."
)

# Body that cites disruptive items but never makes the symmetry argument
# (check 2 passes, check 3 fails).
DISRUPTIVE_WITHOUT_SYMMETRY_BODY = (
    "This article surveys altered-state evidence for filter theory in detail. "
    "Padding sentences fill out the word count so the audit's gate is cleared "
    "without the marker words leaking into the body. " * 30
    + " Psychedelic experience under psilocybin and DMT reveals filter-"
      "loosening. Terminal lucidity in late-stage dementia patients exhibits "
      "the same pattern. Anaesthesia is also discussed as background; the "
      "article then moves on without engaging the broader question."
)

# Body that does not invoke filter framing — out of audit scope. Care is
# taken not to use any token that would trip the filter-framing regex.
NO_FILTER_FRAMING_BODY = (
    "This article reviews psychedelic neuroimaging at a survey level. "
    "Padding sentences fill the word count for the audit's gate without "
    "leaking marker words into the body of the article. " * 40
    + " Psychedelics under psilocybin produce ego-dissolution; near-death "
      "experiences exhibit a similar phenomenology. The piece leaves the "
      "interpretive question open and does not commit to one reading."
)


def _make_article(
    tmp_path: Path,
    section: str,
    slug: str,
    *,
    body: str,
    title: str | None = None,
) -> Path:
    section_dir = tmp_path / section
    section_dir.mkdir(parents=True, exist_ok=True)
    front = (
        "---\n"
        f"title: \"{title or slug}\"\n"
        "---\n"
    )
    path = section_dir / f"{slug}.md"
    path.write_text(front + body)
    return path


# compute_symmetry_profile --------------------------------------------------


def test_compute_profile_counts_supportive_disruptive_clusters(
    tmp_path: Path,
) -> None:
    path = _make_article(tmp_path, "topics", "demo", body=SYMMETRIC_BODY)
    profile = compute_symmetry_profile(path)
    assert profile is not None
    assert profile.has_filter_framing is True
    assert "psychedelics" in profile.supportive_clusters
    assert "near-death" in profile.supportive_clusters
    assert "anaesthesia" in profile.disruptive_clusters
    assert "slow-wave-sleep" in profile.disruptive_clusters
    assert "brain-damage" in profile.disruptive_clusters
    assert profile.symmetry_marker_count >= 3


def test_compute_profile_no_filter_framing(tmp_path: Path) -> None:
    path = _make_article(tmp_path, "topics", "demo", body=NO_FILTER_FRAMING_BODY)
    profile = compute_symmetry_profile(path)
    assert profile is not None
    assert profile.has_filter_framing is False


def test_compute_profile_excludes_code_blocks(tmp_path: Path) -> None:
    """Markers inside fenced code blocks must not contribute to the counts."""
    body = (
        ASYMMETRIC_BODY
        + "\n\n```python\n"
          "# filter theory psychedelics anaesthesia symmetric\n"
          "```\n"
    )
    path = _make_article(tmp_path, "topics", "code-fence", body=body)
    base = compute_symmetry_profile(
        _make_article(tmp_path, "topics", "base", body=ASYMMETRIC_BODY)
    )
    fenced = compute_symmetry_profile(path)
    assert base is not None and fenced is not None
    assert fenced.disruptive_clusters == base.disruptive_clusters
    assert fenced.symmetry_marker_count == base.symmetry_marker_count


def test_compute_profile_returns_none_for_empty_body(tmp_path: Path) -> None:
    path = _make_article(tmp_path, "topics", "empty", body="")
    assert compute_symmetry_profile(path) is None


# evaluate_symmetry ---------------------------------------------------------


def test_asymmetric_filter_article_is_flagged(tmp_path: Path) -> None:
    path = _make_article(tmp_path, "topics", "asymmetric", body=ASYMMETRIC_BODY)
    flag = evaluate_symmetry(path)
    assert flag is not None
    assert "missing_disruptive_cluster" in flag.failed_checks
    assert flag.profile.supportive_hit_count >= 2
    assert flag.profile.disruptive_hit_count == 0
    # missing-disruptive-cluster fires before the symmetry check, and reports
    # every canonical disruptive item as missing.
    assert "anaesthesia" in flag.missing_disruptive_examples


def test_symmetric_filter_article_is_not_flagged(tmp_path: Path) -> None:
    path = _make_article(tmp_path, "topics", "symmetric", body=SYMMETRIC_BODY)
    assert evaluate_symmetry(path) is None


def test_disruptive_cluster_without_symmetry_marker_is_flagged(
    tmp_path: Path,
) -> None:
    path = _make_article(
        tmp_path, "topics", "no-symmetry-marker",
        body=DISRUPTIVE_WITHOUT_SYMMETRY_BODY,
    )
    flag = evaluate_symmetry(path)
    assert flag is not None
    assert "missing_symmetry_acknowledgment" in flag.failed_checks
    assert flag.profile.disruptive_hit_count >= 1
    assert flag.profile.symmetry_marker_count == 0


def test_article_without_filter_framing_is_out_of_scope(tmp_path: Path) -> None:
    path = _make_article(
        tmp_path, "topics", "no-filter", body=NO_FILTER_FRAMING_BODY
    )
    assert evaluate_symmetry(path) is None


def test_short_article_is_skipped(tmp_path: Path) -> None:
    body = (
        "Filter theory is briefly mentioned. Psychedelics and NDE are "
        "noted. Too short for stable signals."
    )
    path = _make_article(tmp_path, "topics", "short", body=body)
    assert evaluate_symmetry(path) is None


def test_too_few_supportive_hits_is_skipped(tmp_path: Path) -> None:
    body = (
        "Filter theory is the framing under discussion in this article. "
        "Padding to clear the min-word-count gate without adding any "
        "additional supportive-cluster items. " * 40
        + " Psychedelic experience is noted. (No second supportive item.)"
    )
    path = _make_article(tmp_path, "topics", "one-supportive", body=body)
    assert evaluate_symmetry(path) is None


def test_min_supportive_hits_is_tunable(tmp_path: Path) -> None:
    # Article with exactly one supportive item: out of scope at default
    # threshold of 2; in scope at threshold of 1.
    body = (
        "Filter theory is the framing under discussion in this article. "
        "Padding to clear the min-word-count gate without adding any "
        "additional supportive-cluster items. " * 40
        + " Psychedelic experience under psilocybin is the canonical case. "
          "No disruptive-cluster items are engaged."
    )
    path = _make_article(tmp_path, "topics", "one-supportive", body=body)
    assert evaluate_symmetry(path) is None
    relaxed = evaluate_symmetry(path, min_supportive_hits=1)
    assert relaxed is not None
    assert "missing_disruptive_cluster" in relaxed.failed_checks


# get_symmetry_flags --------------------------------------------------------


def test_get_symmetry_flags_scans_configured_sections(tmp_path: Path) -> None:
    _make_article(tmp_path, "topics", "asymmetric", body=ASYMMETRIC_BODY)
    _make_article(tmp_path, "topics", "symmetric", body=SYMMETRIC_BODY)
    _make_article(tmp_path, "topics", "no-filter", body=NO_FILTER_FRAMING_BODY)
    flags = get_symmetry_flags(tmp_path)
    assert len(flags) == 1
    assert flags[0].path.stem == "asymmetric"


def test_get_symmetry_flags_skips_section_index(tmp_path: Path) -> None:
    # obsidian/topics/topics.md is the section index — must not be audited.
    _make_article(tmp_path, "topics", "topics", body=ASYMMETRIC_BODY)
    assert get_symmetry_flags(tmp_path) == []


def test_get_symmetry_flags_sorts_worst_first(tmp_path: Path) -> None:
    _make_article(tmp_path, "topics", "fully-asymmetric", body=ASYMMETRIC_BODY)
    _make_article(
        tmp_path, "topics", "partial",
        body=DISRUPTIVE_WITHOUT_SYMMETRY_BODY,
    )
    flags = get_symmetry_flags(tmp_path)
    assert len(flags) == 2
    severities = [f.severity for f in flags]
    assert severities == sorted(severities, reverse=True)


# format_refine_task --------------------------------------------------------


def test_format_refine_task_produces_task_block(tmp_path: Path) -> None:
    path = _make_article(tmp_path, "topics", "asymmetric", body=ASYMMETRIC_BODY)
    flag = evaluate_symmetry(path)
    assert flag is not None
    block = format_refine_task(flag, "2026-05-14")
    assert block.startswith("### P2: Install altered-state symmetry in asymmetric")
    assert "altered-state-symmetry-audit" in block
    assert "refine-draft" in block
    assert "obsidian/topics/asymmetric.md" in block
    assert "Generated**: 2026-05-14" in block
    assert "[[project/calibration-audit-triple]]" in block


# Corpus smoke test ---------------------------------------------------------


REPO_ROOT = Path(__file__).parent.parent


@pytest.mark.skipif(
    not (REPO_ROOT / "obsidian" / "topics").is_dir(),
    reason="No obsidian corpus available in this checkout.",
)
def test_corpus_smoke_runs_without_error() -> None:
    """The audit must run over the live corpus without raising."""
    flags = get_symmetry_flags(REPO_ROOT / "obsidian")
    assert isinstance(flags, list)
    for f in flags:
        assert isinstance(f, SymmetryFlag)
        assert isinstance(f.profile, SymmetryProfile)
        assert f.severity >= 1


@pytest.mark.skipif(
    not (
        REPO_ROOT / "obsidian" / "topics"
        / "psychedelics-and-the-filter-model.md"
    ).is_file(),
    reason="The canonical exhibit article is not present in this checkout.",
)
def test_canonical_exhibit_passes_post_refinement() -> None:
    """After the 2026-05-14 refine-pass installed the symmetry section, the
    canonical psychedelics article should no longer be flagged."""
    path = (
        REPO_ROOT / "obsidian" / "topics"
        / "psychedelics-and-the-filter-model.md"
    )
    assert evaluate_symmetry(path) is None, (
        "The canonical exhibit article should clear the audit after the "
        "2026-05-14 symmetry-installation refine pass; if this test fails, "
        "either the article has regressed or the audit's symmetry markers "
        "no longer match the installed language."
    )
