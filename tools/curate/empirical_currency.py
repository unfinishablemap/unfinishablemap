"""Empirical-record currency scanner.

Detects superlative empirical claims ("current record", "largest", "first to
demonstrate", "to date", "latest", etc.) that are vulnerable to being
superseded by newer published results. This is a distinct defect class from
citation-metadata errors: the citation may be faithful, but the claim it
supports has been overtaken by a newer result.

The 2026-06-06 tune-system report flagged this as a *separate* currency-sweep
sub-check warranting codification — confirmed cases included:
- ``testing-consciousness-collapse`` citing Fein et al. 2019 (~25k amu) as
  "current record" for macromolecule interferometry, superseded by
  Pedalino et al. 2026 (~170k amu).
- ``dream-consciousness`` superseded statistical claims.

This module supplies the cheap regex-only scan. The actual web-verification
of currency lives in the ``/deep-review`` §2.4 procedure and the
``/literature-drift-review`` audit; both can consult ``find_superlative_claims``
to prioritise articles and locate the exact passages to verify.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

import frontmatter

# Superlative patterns vulnerable to supersession. Each pattern is matched
# case-insensitively as a whole-word phrase. Patterns are deliberately
# conservative — false positives are cheaper than false negatives because
# this is a screening pass, not a verdict.
SUPERLATIVE_PATTERNS: tuple[str, ...] = (
    # Quantitative records
    r"current\s+record",
    r"latest\s+(?:record|result|finding|measurement)",
    r"largest\s+(?:ever|to\s+date|known|recorded)",
    r"heaviest\s+(?:ever|to\s+date|known|recorded|molecule|object)",
    r"highest\s+(?:ever|to\s+date|known|recorded|reported)",
    r"smallest\s+(?:ever|to\s+date|known|recorded)",
    r"longest\s+(?:ever|to\s+date|known|recorded|coherence)",
    r"most[- ]complex\s+(?:ever|to\s+date|known|recorded)",
    # Temporal/historical superlatives
    r"first\s+to\s+(?:demonstrate|show|prove|measure|observe|report)",
    r"first\s+(?:demonstration|measurement|observation|report)\s+of",
    r"earliest\s+(?:known|recorded|reported|demonstration)",
    # Currency-of-state hedges that nonetheless make claims vulnerable
    r"\bto\s+date\b",
    r"\bso\s+far\b(?!\s+as)",  # exclude "so far as"
    r"(?:as|up)\s+of\s+(?:writing|now|today|this\s+writing)",
    r"the\s+state[- ]of[- ]the[- ]art",
    r"current\s+(?:state[- ]of[- ]the[- ]art|best|leading)",
)

_SUPERLATIVE_RE = re.compile(
    r"\b(?:" + "|".join(SUPERLATIVE_PATTERNS) + r")\b",
    re.IGNORECASE,
)


@dataclass
class SuperlativeClaim:
    """A single superlative claim located in an article."""

    path: Path
    line_number: int  # 1-indexed line number in the body
    matched_phrase: str
    context: str  # ~120 chars of surrounding text for the verifier to see


def _strip_for_scan(body: str) -> str:
    """Strip code blocks and inline code; URLs may legitimately contain the
    superlative tokens (e.g. ``state-of-the-art`` in a slug) so leave them in
    but the matcher's whole-word boundary catches most of these correctly.
    """
    body = re.sub(r"```[\s\S]*?```", " ", body)
    body = re.sub(r"`[^`]+`", " ", body)
    body = re.sub(r"<!--[\s\S]*?-->", " ", body)
    return body


def find_superlative_claims(file_path: Path) -> list[SuperlativeClaim]:
    """Scan a markdown article for superlative empirical claims.

    Returns one entry per match. An article with no matches returns ``[]``.
    Caller should expect false positives — every match must still be
    web-verified for actual currency. The value of the scan is locating the
    passages a verifier should look at, not adjudicating supersession.
    """
    try:
        post = frontmatter.load(file_path)
    except Exception:
        return []

    body = _strip_for_scan(post.content)
    lines = body.splitlines()
    matches: list[SuperlativeClaim] = []
    for i, line in enumerate(lines, start=1):
        for match in _SUPERLATIVE_RE.finditer(line):
            # Build a context window around the match for the verifier.
            start = max(0, match.start() - 60)
            end = min(len(line), match.end() + 60)
            context = line[start:end].strip()
            matches.append(
                SuperlativeClaim(
                    path=file_path,
                    line_number=i,
                    matched_phrase=match.group(0),
                    context=context,
                )
            )
    return matches


def scan_corpus(
    content_root: Path,
    sections: Optional[Iterable[str]] = None,
) -> dict[Path, list[SuperlativeClaim]]:
    """Scan a set of corpus sections for superlative claims.

    Returns a dict of ``path → claims``, only including paths with ≥1 match.
    Sections default to those most likely to carry empirical record claims
    (topics, apex). Concepts/voids/positions are excluded by default —
    superlative empirical claims are characteristic of topic/synthesis pages.
    """
    sections = list(sections) if sections is not None else ["topics", "apex"]
    results: dict[Path, list[SuperlativeClaim]] = {}
    for section in sections:
        section_dir = content_root / section
        if not section_dir.is_dir():
            continue
        for md_file in section_dir.glob("*.md"):
            if md_file.name == f"{section}.md" or md_file.name.startswith("_"):
                continue
            claims = find_superlative_claims(md_file)
            if claims:
                results[md_file] = claims
    return results


def rank_by_currency_risk(
    claims_by_path: dict[Path, list[SuperlativeClaim]],
) -> list[tuple[Path, int]]:
    """Rank articles by superlative-claim density (count, descending).

    A higher count means a richer target for the deep-review currency sweep
    or the literature-drift audit. Equal counts retain insertion order
    (path-alphabetical when produced by ``scan_corpus``).
    """
    return sorted(
        ((path, len(claims)) for path, claims in claims_by_path.items()),
        key=lambda kv: -kv[1],
    )
