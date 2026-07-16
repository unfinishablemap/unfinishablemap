"""Topic-concept anchoring audit (Audit Three of the calibration audit triple).

Detects topic articles whose evidential calibration exceeds that of the
concept pages they depend on. Compares a topic article's calibration profile
(hedge density, strong-assertion density, underdetermination markers) against
the profiles of the concept pages it anchors on. Flags topics whose hedge
profile materially under-hedges their anchor concept's, generating a
``refine-draft`` task per flagged article.

See ``obsidian/project/calibration-audit-triple.md`` (Audit Three section)
for the discipline this operationalises. Mirrors the analysis-plus-warning-list
shape of ``tools/curate/length.py``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import frontmatter

# Hedge markers count as whole-word matches. Order-insensitive; the regex
# below joins them with alternation. The list is the spec's enumerated set
# (project/calibration-audit-triple.md Audit Three "Mechanics") plus the
# inflected forms that share the same hedging force.
HEDGE_MARKERS: tuple[str, ...] = (
    "could",
    "may",
    "might",
    "perhaps",
    "possibly",
    "seems",
    "appears",
    "suggests",
    "suggesting",
    "tentative",
    "tentatively",
)

# Strong-assertion verbs used on the load-bearing claim. Crude proxy: any
# occurrence counts; this is intentionally noisy, the spec warns the
# mechanical detection is "crude on purpose" and biased toward false
# positives.
STRONG_ASSERTION_MARKERS: tuple[str, ...] = (
    "proves",
    "demonstrates",
    "establishes",
    "refutes",
    "shows that",
    "confirms",
    "verifies",
)

# Explicit underdetermination markers — the calibration-discipline phrases
# that an anchor concept page typically deploys and that a topic article
# inheriting that anchor's calibration should also deploy. Regex patterns
# (case-insensitive) since wording varies.
UNDERDETERMINATION_PATTERNS: tuple[str, ...] = (
    r"neither (?:interpretation|framing|reading) is forced",
    r"not framework[- ]neutral",
    r"coherent with rather than evidenced by",
    r"(?:the )?evidence does not (?:decisively )?adjudicate",
    r"compatible with (?:either|both) (?:interpretations?|framings?|readings?)",
    r"underdetermined by the (?:data|evidence)",
    r"empirically equivalent",
    r"does not decide between",
    r"does not adjudicate",
)

# Default thresholds (tunable via evolution-state.yaml:audit_triple.
# topic_concept_anchoring). Documented in calibration-audit-triple.md.
DEFAULT_HEDGE_DENSITY_RATIO: float = 0.6  # topic's hedge density must be ≥
                                          # 60% of anchor's
DEFAULT_STRONG_ASSERTION_RATIO: float = 1.5  # topic's strong-assertion
                                             # density must not exceed
                                             # 1.5× anchor's
DEFAULT_MIN_WORD_COUNT: int = 400  # skip articles too short for the ratios
                                   # to be meaningful
# Absolute ceiling on the hedge-density floor a topic must clear. Ultra-dense
# anchor concept pages (qualia ~8.2/kw, valence ~7.2/kw) would otherwise force
# a 60%-of-anchor floor of ~4.4–4.9/kw — mathematically unreachable for a
# calibrated topic without over-hedging into mush. tune-system 2026-06-05
# documented `wanting-liking-and-the-value-in-mechanism-fork` re-drawing the
# same hedge_density refine task ~10× in one session, each closed as no-op.
# 3.0/kw is the empirical "calibrated topic" upper band; capping there keeps
# the audit catching genuinely under-hedged articles without rebroadcasting
# unsatisfiable demands.
HEDGE_DENSITY_FLOOR_CAP: float = 3.0
# Absolute small allowance for strong-assertion density when the anchor has
# zero. Topic articles legitimately use "demonstrates" / "establishes" /
# "shows" when reporting settled empirical findings; a small absolute floor
# prevents the audit penalising 1–2 such uses in an otherwise calibrated
# topic. Per tune-system 2026-06-05 Audit-Three false-high analysis.
STRONG_ASSERTION_ABSOLUTE_ALLOWANCE: float = 0.5

# Wikilink resolution: ``[[slug]]`` and ``[[slug|display]]`` patterns. The
# anchoring audit only needs the slug.
_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


@dataclass
class CalibrationProfile:
    """Calibration metrics for one article."""

    path: Path
    title: str
    word_count: int
    hedge_count: int
    hedge_density: float  # hedges per 1000 words
    strong_assertion_count: int
    strong_assertion_density: float  # strong assertions per 1000 words
    underdetermination_marker_count: int


@dataclass
class AnchoringFlag:
    """A topic article flagged as under-hedged relative to an anchor concept."""

    topic_path: Path
    topic_title: str
    anchor_concept_path: Path
    anchor_concept_title: str
    failed_checks: list[str]  # names of the checks that failed
    topic_profile: CalibrationProfile
    anchor_profile: CalibrationProfile
    notes: list[str] = field(default_factory=list)  # human-readable failure
                                                    # descriptions

    @property
    def severity(self) -> int:
        """Number of failed checks; 2 or 3 means the flag is active."""
        return len(self.failed_checks)


def _strip_for_word_count(content: str) -> str:
    """Strip code blocks, comments and URLs before counting words/markers."""
    content = re.sub(r"```[\s\S]*?```", " ", content)
    content = re.sub(r"`[^`]+`", " ", content)
    content = re.sub(r"<!--[\s\S]*?-->", " ", content)
    content = re.sub(r"https?://\S+", " ", content)
    return content


def _count_word_matches(text: str, words: tuple[str, ...]) -> int:
    """Count whole-word/phrase matches across the body (case-insensitive)."""
    if not words:
        return 0
    # Sort longest-first so multi-word phrases match before single words.
    sorted_words = sorted(words, key=lambda w: -len(w))
    pattern = r"\b(?:" + "|".join(re.escape(w) for w in sorted_words) + r")\b"
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def _count_pattern_matches(text: str, patterns: tuple[str, ...]) -> int:
    total = 0
    for pat in patterns:
        total += len(re.findall(pat, text, flags=re.IGNORECASE))
    return total


def compute_profile(file_path: Path) -> Optional[CalibrationProfile]:
    """Compute the calibration profile of a single markdown article.

    Returns ``None`` if the file cannot be parsed.
    """
    try:
        post = frontmatter.load(file_path)
    except Exception:
        return None

    title = post.metadata.get("title", file_path.stem)
    body = _strip_for_word_count(post.content)
    word_count = len(body.split())
    if word_count == 0:
        return None

    hedge_count = _count_word_matches(body, HEDGE_MARKERS)
    strong_count = _count_word_matches(body, STRONG_ASSERTION_MARKERS)
    underdetermination = _count_pattern_matches(body, UNDERDETERMINATION_PATTERNS)

    per_kw = 1000.0 / word_count
    return CalibrationProfile(
        path=file_path,
        title=str(title),
        word_count=word_count,
        hedge_count=hedge_count,
        hedge_density=round(hedge_count * per_kw, 3),
        strong_assertion_count=strong_count,
        strong_assertion_density=round(strong_count * per_kw, 3),
        underdetermination_marker_count=underdetermination,
    )


def extract_anchor_slugs(file_path: Path) -> list[str]:
    """Return concept-anchor slugs for a topic article.

    Sources, in order:
      1. ``concepts:`` frontmatter list (the explicit anchor list)
      2. Inline ``[[wikilinks]]`` in the article's lead (first ~500 words)

    Slugs are de-duplicated while preserving first-seen order so the
    earliest-named anchor remains the primary one. Returned slugs are
    bare (no ``[[ ]]``) and may need resolution to actual file paths via
    :func:`resolve_concept_path`.
    """
    try:
        post = frontmatter.load(file_path)
    except Exception:
        return []

    slugs: list[str] = []
    seen: set[str] = set()

    def _add(raw: str) -> None:
        # frontmatter entries arrive as "[[slug]]" or "[[slug|display]]" or
        # plain "slug"; normalise.
        m = _WIKILINK_RE.search(raw)
        slug = m.group(1).strip() if m else raw.strip()
        # Strip path prefixes (e.g. "concepts/filter-theory" → "filter-theory")
        slug = slug.rsplit("/", 1)[-1]
        if slug and slug not in seen:
            seen.add(slug)
            slugs.append(slug)

    for entry in post.metadata.get("concepts", []) or []:
        _add(str(entry))

    # Lead-section wikilinks: take the first ~500 words of body.
    lead = " ".join(post.content.split()[:500])
    for match in _WIKILINK_RE.finditer(lead):
        _add(f"[[{match.group(1)}]]")

    return slugs


def resolve_concept_path(slug: str, content_root: Path) -> Optional[Path]:
    """Resolve a wikilink slug to a concrete ``obsidian/concepts/*.md`` path.

    Returns ``None`` if no matching concept file exists. The audit only
    compares against ``concepts/`` — topic-to-topic anchoring is a different
    discipline (the cross-review chain) and is not in scope here.
    """
    candidate = content_root / "concepts" / f"{slug}.md"
    if candidate.is_file():
        return candidate
    return None


def _is_anchoring_exempt(topic_path: Path) -> bool:
    """True if the topic's frontmatter sets ``anchoring_audit_exempt: true``.

    Reserved for flags an operator has verified as false-highs (the article
    calibrates structurally in ways the lexical checks cannot see). Cheap
    front-of-file read; tolerates a trailing YAML comment on the value line.
    """
    try:
        head = topic_path.read_text(encoding="utf-8")[:1500]
    except OSError:
        return False
    return re.search(r'^anchoring_audit_exempt:\s*true\b', head, re.MULTILINE) is not None


def evaluate_anchoring(
    topic_path: Path,
    content_root: Path,
    *,
    hedge_density_ratio: float = DEFAULT_HEDGE_DENSITY_RATIO,
    strong_assertion_ratio: float = DEFAULT_STRONG_ASSERTION_RATIO,
    min_word_count: int = DEFAULT_MIN_WORD_COUNT,
) -> list[AnchoringFlag]:
    """Evaluate a single topic article against all its anchor concepts.

    Returns one :class:`AnchoringFlag` per anchor concept whose comparison
    fires (≥2 of 3 checks failed). An article with no resolvable anchors,
    or that is too short for stable per-thousand-word ratios, returns ``[]``.
    """
    topic_profile = compute_profile(topic_path)
    if topic_profile is None or topic_profile.word_count < min_word_count:
        return []

    # Verified false-high opt-out. The hedge-density and underdetermination
    # checks are lexical: they count modal hedge-words and a fixed set of
    # discipline-phrases. Some articles calibrate STRUCTURALLY instead — their
    # whole thesis is a choice under underdetermination, they concede the
    # discriminating tenet leans to the rival, etc. — using bare-noun
    # "underdetermination" and phrasal hedges ("leans toward", "does not decide
    # it") the regexes do not see. Those articles re-flag every cycle and a
    # refine would only over-hedge and regress the crisp voice. An operator who
    # has verified a flag is a false-high sets `anchoring_audit_exempt: true` in
    # the topic's frontmatter to stop the treadmill without touching the scoring
    # math for every other article.
    if _is_anchoring_exempt(topic_path):
        return []

    flags: list[AnchoringFlag] = []

    for slug in extract_anchor_slugs(topic_path):
        anchor_path = resolve_concept_path(slug, content_root)
        if anchor_path is None or anchor_path == topic_path:
            continue
        anchor_profile = compute_profile(anchor_path)
        if anchor_profile is None or anchor_profile.word_count < min_word_count:
            continue

        failed: list[str] = []
        notes: list[str] = []

        # Check 1: hedge density. Topic's hedge density should be at least
        # ``hedge_density_ratio`` × anchor's, capped at HEDGE_DENSITY_FLOOR_CAP
        # to avoid unsatisfiable demands from ultra-dense concept-page anchors.
        # If anchor has near-zero hedge density the ratio is meaningless — skip.
        if anchor_profile.hedge_density >= 1.0:
            min_topic_density = min(
                anchor_profile.hedge_density * hedge_density_ratio,
                HEDGE_DENSITY_FLOOR_CAP,
            )
            if topic_profile.hedge_density < min_topic_density:
                failed.append("hedge_density")
                notes.append(
                    f"hedge density {topic_profile.hedge_density:.2f}/kw is "
                    f"below {min_topic_density:.2f}/kw (target = "
                    f"{hedge_density_ratio:.0%} of anchor "
                    f"{anchor_profile.hedge_density:.2f}/kw, capped at "
                    f"{HEDGE_DENSITY_FLOOR_CAP:.1f}/kw)"
                )

        # Check 2: strong-assertion density. Topic should not exceed
        # ``strong_assertion_ratio`` × anchor's. If anchor has zero strong
        # assertions, allow a small absolute floor before flagging — topic
        # articles legitimately use strong-assertion verbs when reporting
        # settled empirical findings.
        if anchor_profile.strong_assertion_density == 0:
            if topic_profile.strong_assertion_density > STRONG_ASSERTION_ABSOLUTE_ALLOWANCE:
                failed.append("strong_assertions")
                notes.append(
                    f"topic uses {topic_profile.strong_assertion_count} "
                    f"strong-assertion verbs ({topic_profile.strong_assertion_density:.2f}"
                    f"/kw) where anchor uses none; absolute allowance is "
                    f"{STRONG_ASSERTION_ABSOLUTE_ALLOWANCE:.1f}/kw"
                )
        else:
            max_topic_density = (
                anchor_profile.strong_assertion_density * strong_assertion_ratio
            )
            if topic_profile.strong_assertion_density > max_topic_density:
                failed.append("strong_assertions")
                notes.append(
                    f"strong-assertion density "
                    f"{topic_profile.strong_assertion_density:.2f}/kw exceeds "
                    f"{strong_assertion_ratio:.1f}× anchor "
                    f"({anchor_profile.strong_assertion_density:.2f}/kw)"
                )

        # Check 3: underdetermination markers. If anchor explicitly hedges
        # via "neither interpretation is forced" et al. and topic does not,
        # the topic has inherited none of the anchor's calibration discipline.
        if (
            anchor_profile.underdetermination_marker_count > 0
            and topic_profile.underdetermination_marker_count == 0
        ):
            failed.append("underdetermination_markers")
            notes.append(
                f"anchor declares underdetermination "
                f"({anchor_profile.underdetermination_marker_count}× explicit) "
                f"but topic has no underdetermination markers"
            )

        if len(failed) >= 2:
            flags.append(
                AnchoringFlag(
                    topic_path=topic_path,
                    topic_title=topic_profile.title,
                    anchor_concept_path=anchor_path,
                    anchor_concept_title=anchor_profile.title,
                    failed_checks=failed,
                    topic_profile=topic_profile,
                    anchor_profile=anchor_profile,
                    notes=notes,
                )
            )

    return flags


def get_anchoring_flags(
    content_root: Path,
    *,
    hedge_density_ratio: float = DEFAULT_HEDGE_DENSITY_RATIO,
    strong_assertion_ratio: float = DEFAULT_STRONG_ASSERTION_RATIO,
    min_word_count: int = DEFAULT_MIN_WORD_COUNT,
    section: str = "topics",
) -> list[AnchoringFlag]:
    """Run the audit across the whole topics section.

    Returns flags sorted with the most-failed-checks first, then by the size
    of the hedge-density gap. Worst offenders surface first; the caller is
    responsible for any global cap (see ``audit_triple.global_task_cap``).
    """
    section_dir = content_root / section
    if not section_dir.is_dir():
        return []

    all_flags: list[AnchoringFlag] = []
    for md_file in section_dir.glob("*.md"):
        if md_file.name == f"{section}.md" or md_file.name.startswith("_"):
            continue
        all_flags.extend(
            evaluate_anchoring(
                md_file,
                content_root,
                hedge_density_ratio=hedge_density_ratio,
                strong_assertion_ratio=strong_assertion_ratio,
                min_word_count=min_word_count,
            )
        )

    def _sort_key(f: AnchoringFlag) -> tuple[int, float]:
        anchor = f.anchor_profile.hedge_density or 1.0
        gap = max(0.0, anchor - f.topic_profile.hedge_density) / anchor
        return (-f.severity, -gap)

    all_flags.sort(key=_sort_key)
    return all_flags


def format_refine_task(flag: AnchoringFlag, today_iso: str) -> str:
    """Render an :class:`AnchoringFlag` as a P2 ``refine-draft`` task block
    suitable for prepending to ``obsidian/workflow/todo.md`` under
    "Active Tasks".
    """
    slug = flag.topic_path.stem
    anchor_slug = flag.anchor_concept_path.stem
    failed_list = ", ".join(flag.failed_checks)
    note_lines = "\n".join(f"  - {n}" for n in flag.notes)
    return (
        f"### P2: Adopt {anchor_slug} calibration in {slug}\n"
        f"- **Type**: refine-draft\n"
        f"- **Status**: pending\n"
        f"- **File**: obsidian/topics/{slug}.md\n"
        f"- **Notes**: From topic-concept anchoring audit {today_iso}. "
        f"The topic article over-claims relative to its anchor concept "
        f"[[{anchor_slug}]]; failed checks: {failed_list}.\n"
        f"{note_lines}\n"
        f"  - Action: bring the topic's hedge profile in line with the anchor "
        f"concept's. Preserve the article's voice; this is not a request to "
        f"weaken the central claim, only to inherit the calibration discipline "
        f"the anchor concept already uses. See "
        f"[[project/calibration-audit-triple]] Audit Three for the spec and "
        f"[[evidential-status-discipline]] for the underlying rule.\n"
        f"- **Source**: topic-concept-anchoring-audit\n"
        f"- **Generated**: {today_iso}\n"
    )
