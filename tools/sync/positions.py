"""Auto-link bare position IDs (P-Q3, P-MS1, ...) to the positions register.

The register is cited heavily across the corpus -- 511 mentions outside
`obsidian/positions/` at the time this was written, concentrated in apex
articles -- but only ~26% sat inside a wikilink, so three quarters of them were
inert text. A reader meeting "P-Q3" mid-paragraph had no route to what P-Q3
says.

Hand-linking them is the wrong fix: the IDs are a rigid, greppable pattern and
new ones appear whenever `/positions-evolve` adds an entry, so the links would
rot immediately. This module resolves them at sync time instead, against the
anchors added by `scripts/add_position_anchors.py`.

Deliberately conservative -- a bare ID is linked only when all of these hold:

  * it resolves to a position that actually exists in the register
  * it is not inside code (fenced or inline)
  * it is not already inside a markdown link, an HTML tag, or a wikilink
  * it is not the `## P-NN:` heading that defines the position itself

Anything unresolvable is left as plain text rather than linked to a 404.
"""

from __future__ import annotations

import re
from pathlib import Path

from tools.sync.wikilinks import _split_code_segments

# `## P-Q3: <claim>` -- the definition heading in a domain file.
_DEFINITION = re.compile(r"^## (P-[A-Z]{1,4}\d+):", re.M)

# A bare position ID in prose. Trailing possessives ("P-Q3's") are left outside
# the link so the apostrophe does not end up inside the anchor text.
_BARE_ID = re.compile(r"\bP-[A-Z]{1,4}\d+\b")

# Spans that must never be rewritten: markdown links, HTML tags, wikilinks.
_PROTECTED = re.compile(
    r"\[[^\]]*\]\([^)]*\)"      # [label](url)
    r"|<[^>]*>"                 # <span id="p-q3"></span>
    r"|\[\[[^\]]*\]\]"          # [[wikilink]] (if any survive to this stage)
)


def build_position_index(positions_dir: Path) -> dict[str, str]:
    """Map each position ID to the slug of the domain file that defines it.

    `positions.md` is the section index and `*-calibration-history.md` are
    audit-trail companions; neither defines positions.
    """
    index: dict[str, str] = {}
    if not positions_dir.is_dir():
        return index
    for path in sorted(positions_dir.glob("*.md")):
        if path.name == "positions.md" or "calibration-history" in path.name:
            continue
        text = path.read_text(encoding="utf-8")
        for match in _DEFINITION.finditer(text):
            index[match.group(1)] = path.stem
    return index


def _upgrade_pagelevel_links(content: str, index: dict[str, str], base_path: str) -> str:
    """Add the position anchor to hand-written links that lack one.

    A wikilink written as `[[positions/ai-consciousness-scope|P-AC1]]` converts
    to a page-level URL, dropping the reader at the top of a file holding up to
    eleven positions. Where the label is exactly a position ID and the URL is
    that position's own domain page, append the anchor so it behaves like an
    auto-generated link. Links whose label and target disagree are left alone --
    that mismatch is editorial intent, not something to normalise away.
    """
    def repl(match: re.Match) -> str:
        pid, url = str(match.group(1)), str(match.group(2))
        slug = index.get(pid)
        if slug is None:
            return str(match.group(0))
        expected = f"{base_path.rstrip('/')}/positions/{slug}/"
        if url.rstrip("/") + "/" != expected:
            return str(match.group(0))
        return f"[{pid}]({expected}#{pid.lower()})"

    return re.sub(r"\[(P-[A-Z]{1,4}\d+)\]\(([^)#]*)\)", repl, content)


def autolink_positions(
    content: str,
    index: dict[str, str],
    base_path: str = "/",
) -> str:
    """Replace bare position IDs with links into the register."""
    if not index:
        return content
    content = _upgrade_pagelevel_links(content, index, base_path)

    def link_segment(segment: str) -> str:
        # Collect protected spans once per segment.
        protected = [m.span() for m in _PROTECTED.finditer(segment)]
        # Definition headings: protect the whole line so a position does not
        # link to itself at its own point of definition.
        for m in _DEFINITION.finditer(segment):
            line_end = segment.find("\n", m.start())
            protected.append((m.start(), line_end if line_end != -1 else len(segment)))

        def replace(match: re.Match) -> str:
            pid = str(match.group(0))
            slug = index.get(pid)
            if slug is None:
                return pid
            if any(a <= match.start() < b for a, b in protected):
                return pid
            url = f"{base_path.rstrip('/')}/positions/{slug}/#{pid.lower()}"
            return f"[{pid}]({url})"

        return _BARE_ID.sub(replace, segment)

    segments = _split_code_segments(content)
    for i in range(0, len(segments), 2):  # even indices are outside code
        segments[i] = link_segment(segments[i])
    return "".join(segments)


# --- Build-time metadata for tooltips -------------------------------------

_CALIBRATION = re.compile(r"^- \*\*Calibration\*\*[^:]*:\s*(.+)$", re.M)
_STATUS_LINE = re.compile(r"^- \*\*Status\*\*:\s*(.+)$", re.M)

# The axes surfaced in a tooltip. The register defines six; these three are the
# ones a reader needs in order to weigh a citation without leaving the page:
# how confident the Map is, how much independent evidence backs it, and how much
# of the framework moves if it falls.
_TOOLTIP_AXES = ("credence", "external-evidence grade", "structural centrality")

# The register's band vocabularies are shorthand for a schema defined elsewhere.
# A tooltip has no room for the key and a single-page fetch carries no link to
# it, so bands are rendered as self-standing phrases. Wordings follow the
# definitions in methodology-and-calibration; "grade D" in particular means *no*
# independent support, not merely a poor grade, and reads as the latter to
# anyone who has not seen the scale.
_EVIDENCE_LABEL = {
    "A": "established independent evidence",
    "B": "some independent evidence",
    "C": "limited or indirect evidence",
    "D": "no independent evidence",
    "n/a": "normative, not an empirical claim",
    "n a": "normative, not an empirical claim",
}
_CREDENCE_LABEL = {
    "high": "confidence: high",
    "moderate": "confidence: moderate",
    "low": "confidence: low",
}
_CENTRALITY_LABEL = {
    "high": "framework-critical",
    "moderate": "moderately central",
    "low": "peripheral to the framework",
}

# Bands a reader should not miss: a confident claim with nothing independent
# behind it is the register's own stated liability, so it is flagged rather than
# shown flat alongside the rest.
_WEAK_BANDS = {"no independent evidence", "confidence: low"}


def _axis_band(calibration: str, axis: str) -> str:
    """Pull one axis's band out of a Calibration line, dropping any rationale."""
    for segment in calibration.split("·"):
        segment = segment.strip()
        if segment.lower().startswith(axis):
            value = segment[len(axis):].strip(" :")
            value = re.sub(r"\s*[\(\[].*$", "", value).strip()
            return value
    return ""


def build_position_metadata(positions_dir: Path) -> dict[str, dict[str, str]]:
    """Claim text and headline calibration bands for every position.

    Feeds `hugo/data/positions.yaml`, which the link render hook reads at build
    time to enrich each generated position link.
    """
    meta: dict[str, dict[str, str]] = {}
    if not positions_dir.is_dir():
        return meta
    for path in sorted(positions_dir.glob("*.md")):
        if path.name == "positions.md" or "calibration-history" in path.name:
            continue
        text = path.read_text(encoding="utf-8")
        blocks = re.split(r"\n(?=## P-[A-Z]{1,4}\d+:)", text)
        for block in blocks:
            head = re.match(r"## (P-[A-Z]{1,4}\d+):\s*(.+)", block)
            if not head:
                continue
            pid, claim = head.group(1), head.group(2).strip()
            cal_match = _CALIBRATION.search(block)
            calibration = cal_match.group(1) if cal_match else ""
            status_match = _STATUS_LINE.search(block)
            status = status_match.group(1) if status_match else ""
            # Strip the block anchor we append to the Status line.
            status = re.sub(r"\s+\^[A-Za-z0-9-]+\s*$", "", status).strip()
            credence = _axis_band(calibration, "credence")
            grade = _axis_band(calibration, "external-evidence grade")
            centrality = _axis_band(calibration, "structural centrality")

            bands: list[str] = []
            for raw, table in (
                (credence, _CREDENCE_LABEL),
                (grade, _EVIDENCE_LABEL),
                (centrality, _CENTRALITY_LABEL),
            ):
                if not raw:
                    continue
                bands.append(table.get(raw, raw))

            entry = {
                "id": pid,
                "slug": path.stem,
                "claim": claim,
                "status": status,
                # Raw bands kept so a consumer that does know the schema can
                # still read the register's own vocabulary.
                "credence": credence,
                "grade": grade,
                "structural_centrality": centrality,
                "bands": " · ".join(bands),
                "weak": "yes" if any(b in _WEAK_BANDS for b in bands) else "no",
                # One flat line for the title attribute -- the only carrier that
                # survives server-side HTML-to-markdown conversion.
                "summary": f"{pid}: {claim}" + (f" — {' · '.join(bands)}" if bands else ""),
            }
            meta[pid] = entry
    return meta


def write_position_data(metadata: dict[str, dict[str, str]], out_path: Path) -> None:
    """Write the Hugo data file the render hook reads.

    Keys are lowercased anchor ids (`p-q3`) so the hook can look a position up
    straight from the URL fragment without re-casing.
    """
    import yaml

    payload = {pid.lower(): entry for pid, entry in sorted(metadata.items())}
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        fh.write("# Generated by tools/sync/positions.py — do not edit by hand.\n")
        fh.write("# Source of truth: obsidian/positions/*.md\n")
        yaml.safe_dump(payload, fh, allow_unicode=True, sort_keys=True, width=100)
