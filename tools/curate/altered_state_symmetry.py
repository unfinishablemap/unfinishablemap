"""Altered-state symmetry audit (Audit Two of the calibration audit triple).

Detects articles that cite the *supportive cluster* of altered states
(psychedelics, NDEs, terminal lucidity, contemplative cessation, mystical
experience, OBE) as filter-supportive evidence without engaging the
*symmetric accommodation work* that the *disruptive cluster* (anaesthesia,
slow-wave sleep, brain damage, persistent vegetative state, dementia)
demands of any filter account. The failure mode is treating supportive
altered states as multiple independent confirmations of filter framing
when the cluster carries the evidential weight of a single pattern; see
``obsidian/project/calibration-audit-triple.md`` (Audit Two section) for
the discipline this operationalises.

Mirrors the analysis-plus-warning-list shape of ``tools/curate/length.py``
and the structure of the companion topic-concept anchoring audit
(``tools/curate/anchoring.py``).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import frontmatter

# Filter-framing gate. The audit applies only to articles that frame
# altered-state evidence as support for filter / transmission theory; an
# article surveying psychedelics without taking the filter side is out of
# scope. Crude proxy: any reference to one of these tokens.
FILTER_FRAMING_PATTERNS: tuple[str, ...] = (
    r"\bfilter[ -](?:theory|model|framing|account|view)\b",
    r"\bfilter[ -]transmission\b",
    r"\btransmission[ -](?:theory|model|framing|account|view)\b",
)

# Supportive cluster: altered states whose phenomenology the filter framing
# accommodates more naturally than production framing. Per the spec, the
# canonical members are psychedelics, NDE, terminal lucidity, contemplative
# cessation, mystical experience, OBE.
SUPPORTIVE_CLUSTER_PATTERNS: tuple[tuple[str, str], ...] = (
    ("psychedelics", r"\bpsychedelic(?:s|-induced)?\b|\bpsilocybin\b|\bLSD\b"
                      r"|\bDMT\b|\bayahuasca\b|\bego[ -]dissolution\b"),
    ("near-death", r"\bnear[ -]death(?:[ -]experience)?(?:s)?\b|\bNDEs?\b"),
    ("terminal-lucidity", r"\bterminal[ -]lucidity\b|\bparadoxical[ -]lucidity\b"),
    ("cessation", r"\bcontemplative[ -]cessation\b|\bnirodha[ -]samapatti\b"
                  r"|\bjh[āa]na\b"),
    ("mystical-experience", r"\bmystical[ -](?:experience|type|state)s?\b"
                            r"|\bunitive[ -]experiences?\b"),
    ("out-of-body", r"\bout[ -]of[ -]body\b|\bOBEs?\b"),
)

# Disruptive cluster: altered states whose phenomenology the production
# framing accommodates more naturally than filter framing. Per the spec, the
# canonical members are anaesthesia, slow-wave sleep, brain damage, PVS,
# dementia.
DISRUPTIVE_CLUSTER_PATTERNS: tuple[tuple[str, str], ...] = (
    ("anaesthesia", r"\bana?esthesi[ae]\b|\bana?esthetic(?:s)?\b"
                    r"|\bpropofol\b|\bketamine\b|\bxenon\b"),
    ("slow-wave-sleep", r"\bslow[ -]wave[ -]sleep\b|\bdeep[ -]sleep\b"
                        r"|\bdreamless[ -]sleep\b|\bNREM\b"),
    ("brain-damage", r"\bbrain[ -](?:damage|injury|lesion(?:s)?)\b"
                     r"|\btraumatic[ -]brain[ -]injury\b|\bTBI\b"),
    ("vegetative-state", r"\b(?:persistent[ -])?vegetative[ -]state\b|\bPVS\b"
                         r"|\bminimally[ -]conscious[ -]state\b|\bMCS\b"),
    ("dementia", r"\bdementia\b|\bAlzheimer[''']s\b|\bneurodegeneration\b"),
)

# Symmetry-acknowledgment markers. Check 3 fires when none of these appear:
# the article must explicitly name that filter and production framings each
# accommodate the full altered-state cluster by parallel moves, not that
# the supportive cases constitute independent confirmations. These are the
# phrasings the 2026-05-14 psychedelics-and-the-filter-model article
# converged on after four refine-passes; future refines should reach the
# same load-bearing language earlier.
SYMMETRY_ACKNOWLEDGMENT_PATTERNS: tuple[str, ...] = (
    r"\bsymmetric(?:ally)?\b",
    r"\bsymmetry\b",
    r"\basymmetr(?:y|ic|ically)\b",
    r"\bstructurally identical\b",
    r"\bparallel(?:s|ly)? (?:accommodation|move|burden|debt|work)\b",
    r"\b(?:the same|a parallel) move is available\b",
    r"\bboth (?:framings?|accounts?|readings?|theories|sides?)\b",
    r"\bproduction[ -](?:framing|theory|theorists?|account|view|side)\b",
    r"\bone (?:pattern|phenomenon|cluster), not (?:five|many|several)\b",
    r"\bcluster carries the evidential weight of (?:one|a single)\b",
    r"\bcannot honestly be cited as multiple independent\b",
    r"\bmultiple independent confirmations\b",  # ack via denial of this frame
    r"\bnot.{0,40}independent confirmations\b",
    r"\bfilter accommodates.{0,80}production accommodates\b",
    r"\bdouble[ -]counting\b",
)

DEFAULT_MIN_WORD_COUNT: int = 400  # short articles produce noisy signals
DEFAULT_MIN_SUPPORTIVE_HITS: int = 2  # spec: "≥2 items from the supportive
                                      # cluster" before the audit applies


@dataclass
class SymmetryProfile:
    """Altered-state-symmetry metrics for one article."""

    path: Path
    title: str
    word_count: int
    has_filter_framing: bool
    supportive_clusters: list[str]   # cluster names with ≥1 hit
    disruptive_clusters: list[str]   # cluster names with ≥1 hit
    symmetry_marker_count: int

    @property
    def supportive_hit_count(self) -> int:
        return len(self.supportive_clusters)

    @property
    def disruptive_hit_count(self) -> int:
        return len(self.disruptive_clusters)


@dataclass
class SymmetryFlag:
    """An article flagged for asymmetric altered-state framing."""

    path: Path
    title: str
    profile: SymmetryProfile
    failed_checks: list[str]
    missing_disruptive_examples: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def severity(self) -> int:
        return len(self.failed_checks)


def _strip_for_scan(content: str) -> str:
    """Strip code blocks, comments and URLs before pattern-matching so
    incidental hits inside code samples or links do not score."""
    content = re.sub(r"```[\s\S]*?```", " ", content)
    content = re.sub(r"`[^`]+`", " ", content)
    content = re.sub(r"<!--[\s\S]*?-->", " ", content)
    content = re.sub(r"https?://\S+", " ", content)
    return content


def _has_any_match(text: str, patterns: tuple[str, ...]) -> bool:
    for pat in patterns:
        if re.search(pat, text, flags=re.IGNORECASE):
            return True
    return False


def _clusters_with_hits(
    text: str, named_patterns: tuple[tuple[str, str], ...]
) -> list[str]:
    """Return the names of clusters with at least one regex match."""
    hits: list[str] = []
    for name, pat in named_patterns:
        if re.search(pat, text, flags=re.IGNORECASE):
            hits.append(name)
    return hits


def _count_pattern_matches(text: str, patterns: tuple[str, ...]) -> int:
    total = 0
    for pat in patterns:
        total += len(re.findall(pat, text, flags=re.IGNORECASE))
    return total


def compute_symmetry_profile(file_path: Path) -> Optional[SymmetryProfile]:
    """Compute the altered-state-symmetry profile of one markdown article."""
    try:
        post = frontmatter.load(file_path)
    except Exception:
        return None

    title = post.metadata.get("title", file_path.stem)
    body = _strip_for_scan(post.content)
    word_count = len(body.split())
    if word_count == 0:
        return None

    return SymmetryProfile(
        path=file_path,
        title=str(title),
        word_count=word_count,
        has_filter_framing=_has_any_match(body, FILTER_FRAMING_PATTERNS),
        supportive_clusters=_clusters_with_hits(body, SUPPORTIVE_CLUSTER_PATTERNS),
        disruptive_clusters=_clusters_with_hits(body, DISRUPTIVE_CLUSTER_PATTERNS),
        symmetry_marker_count=_count_pattern_matches(
            body, SYMMETRY_ACKNOWLEDGMENT_PATTERNS
        ),
    )


def evaluate_symmetry(
    file_path: Path,
    *,
    min_word_count: int = DEFAULT_MIN_WORD_COUNT,
    min_supportive_hits: int = DEFAULT_MIN_SUPPORTIVE_HITS,
) -> Optional[SymmetryFlag]:
    """Evaluate a single article against the altered-state symmetry checks.

    Returns ``None`` when the article is not in scope (no filter framing,
    too short, or fewer than ``min_supportive_hits`` supportive-cluster
    items). Returns a :class:`SymmetryFlag` only when the article is in
    scope **and** at least one check fails.

    The three checks (spec: ``calibration-audit-triple.md`` Audit Two
    "Mechanics"):

    1. Filter-framed article cites ≥2 supportive-cluster items → audit applies.
    2. If yes, the article cites ≥1 disruptive-cluster item.
    3. If yes, the article explicitly marks the symmetric accommodation work
       (the supportive cases are one pattern, not multiple independent
       confirmations; the production framing has the parallel accommodation).
    """
    profile = compute_symmetry_profile(file_path)
    if profile is None or profile.word_count < min_word_count:
        return None
    if not profile.has_filter_framing:
        return None
    if profile.supportive_hit_count < min_supportive_hits:
        return None

    failed: list[str] = []
    notes: list[str] = []
    missing: list[str] = []

    if profile.disruptive_hit_count == 0:
        failed.append("missing_disruptive_cluster")
        canonical = [name for name, _ in DISRUPTIVE_CLUSTER_PATTERNS]
        missing.extend(canonical)
        notes.append(
            f"cites {profile.supportive_hit_count} supportive-cluster items "
            f"({', '.join(profile.supportive_clusters)}) but no disruptive-"
            f"cluster items; the symmetric burden is unaddressed"
        )
    elif profile.symmetry_marker_count == 0:
        failed.append("missing_symmetry_acknowledgment")
        cited_disruptive = set(profile.disruptive_clusters)
        canonical_disruptive = [name for name, _ in DISRUPTIVE_CLUSTER_PATTERNS]
        missing.extend(
            [c for c in canonical_disruptive if c not in cited_disruptive]
        )
        notes.append(
            f"cites disruptive-cluster items "
            f"({', '.join(profile.disruptive_clusters)}) but contains no "
            f"explicit symmetry-acknowledgment language; the disruptive "
            f"cases appear without the parallel-accommodation framing"
        )

    if not failed:
        return None

    return SymmetryFlag(
        path=file_path,
        title=profile.title,
        profile=profile,
        failed_checks=failed,
        missing_disruptive_examples=missing,
        notes=notes,
    )


def get_symmetry_flags(
    content_root: Path,
    *,
    min_word_count: int = DEFAULT_MIN_WORD_COUNT,
    min_supportive_hits: int = DEFAULT_MIN_SUPPORTIVE_HITS,
    sections: tuple[str, ...] = ("topics", "concepts", "apex"),
) -> list[SymmetryFlag]:
    """Run the audit across the configured sections.

    Returns flags sorted with the most-severe check-failures first, then by
    descending supportive-hit-count so the densest asymmetries surface first.
    The caller is responsible for any global cap (see
    ``audit_triple.global_task_cap`` in ``evolution-state.yaml``).
    """
    flags: list[SymmetryFlag] = []
    for section in sections:
        section_dir = content_root / section
        if not section_dir.is_dir():
            continue
        for md_file in section_dir.glob("*.md"):
            if md_file.name == f"{section}.md" or md_file.name.startswith("_"):
                continue
            flag = evaluate_symmetry(
                md_file,
                min_word_count=min_word_count,
                min_supportive_hits=min_supportive_hits,
            )
            if flag is not None:
                flags.append(flag)

    flags.sort(
        key=lambda f: (-f.severity, -f.profile.supportive_hit_count)
    )
    return flags


def format_refine_task(flag: SymmetryFlag, today_iso: str) -> str:
    """Render a :class:`SymmetryFlag` as a P2 ``refine-draft`` task block
    suitable for prepending to ``obsidian/workflow/todo.md`` under
    "Active Tasks".
    """
    slug = flag.path.stem
    section = flag.path.parent.name
    failed_list = ", ".join(flag.failed_checks)
    cited_supportive = ", ".join(flag.profile.supportive_clusters) or "(none)"
    cited_disruptive = ", ".join(flag.profile.disruptive_clusters) or "(none)"
    missing_str = ", ".join(flag.missing_disruptive_examples) or "(none)"
    note_lines = "\n".join(f"  - {n}" for n in flag.notes)
    return (
        f"### P2: Install altered-state symmetry in {slug}\n"
        f"- **Type**: refine-draft\n"
        f"- **Status**: pending\n"
        f"- **File**: obsidian/{section}/{slug}.md\n"
        f"- **Notes**: From altered-state symmetry audit {today_iso}. "
        f"The article frames altered-state evidence around filter / "
        f"transmission theory and cites supportive-cluster items "
        f"({cited_supportive}) but fails the symmetric-accommodation "
        f"discipline; failed checks: {failed_list}.\n"
        f"  - Supportive cluster cited: {cited_supportive}\n"
        f"  - Disruptive cluster cited: {cited_disruptive}\n"
        f"  - Disruptive cluster missing or under-engaged: {missing_str}\n"
        f"{note_lines}\n"
        f"  - Action: add a paragraph that (a) names the disruptive-cluster "
        f"items the filter framing must also accommodate, (b) states how "
        f"the filter framing accommodates them, and (c) explicitly marks "
        f"this accommodation as parallel to — and not stronger than — the "
        f"corresponding work the production framing performs for the "
        f"supportive-cluster items. See [[project/calibration-audit-triple]] "
        f"Audit Two for the spec and [[direct-refutation-discipline]] for the "
        f"underlying rule against double-counting convergence-of-cases.\n"
        f"- **Source**: altered-state-symmetry-audit\n"
        f"- **Generated**: {today_iso}\n"
    )
