"""Tests for auto-linking bare position IDs at sync time."""

from pathlib import Path

from tools.sync.positions import autolink_positions, build_position_index

INDEX = {"P-Q3": "quantum-interface", "P-MS1": "moral-status", "P-VS1": "value-in-selection"}


def link(text: str) -> str:
    return autolink_positions(text, INDEX)


def test_bare_id_becomes_a_link():
    out = link("The dilemma P-Q3 is unresolved.")
    assert out == "The dilemma [P-Q3](/positions/quantum-interface/#p-q3) is unresolved."


def test_multiple_ids_across_files():
    out = link("P-Q3 and P-MS1 disagree.")
    assert "/positions/quantum-interface/#p-q3" in out
    assert "/positions/moral-status/#p-ms1" in out


def test_unknown_id_left_alone():
    assert link("P-ZZ9 is not real.") == "P-ZZ9 is not real."


def test_possessive_keeps_apostrophe_outside_the_link():
    out = link("P-Q3's verdict")
    assert out == "[P-Q3](/positions/quantum-interface/#p-q3)'s verdict"


def test_inline_code_untouched():
    assert link("Use `P-Q3` literally.") == "Use `P-Q3` literally."


def test_fenced_code_untouched():
    src = "text\n\n```\nP-Q3\n```\n\nP-MS1"
    out = link(src)
    assert "```\nP-Q3\n```" in out
    assert "[P-MS1]" in out


def test_existing_markdown_link_not_double_wrapped():
    src = "See [P-Q3](/positions/quantum-interface/#p-q3) here."
    assert link(src) == src


def test_html_span_id_untouched():
    src = '- **Status**: live <span id="p-q3"></span>'
    assert link(src) == src


def test_wikilink_label_untouched():
    src = "See [[positions/quantum-interface|P-Q3]] here."
    assert link(src) == src


def test_definition_heading_does_not_self_link():
    src = "## P-Q3: The dilemma\n\n- **Status**: live\n\nLater P-Q3 again."
    out = link(src)
    assert out.startswith("## P-Q3: The dilemma")
    assert "Later [P-Q3](/positions/quantum-interface/#p-q3) again." in out


def test_empty_index_is_a_noop():
    assert autolink_positions("P-Q3", {}) == "P-Q3"


def test_build_index_from_real_register():
    idx = build_position_index(Path("obsidian/positions"))
    assert len(idx) >= 50, f"expected the full register, got {len(idx)}"
    assert idx["P-Q3"] == "quantum-interface"
    assert idx["P-MS1"] == "moral-status"
    # index and calibration-history files define no positions
    assert "positions" not in idx.values()
    assert not any("calibration-history" in v for v in idx.values())


def test_pagelevel_link_gets_its_anchor():
    src = "See [P-Q3](/positions/quantum-interface/) here."
    assert link(src) == "See [P-Q3](/positions/quantum-interface/#p-q3) here."


def test_link_already_anchored_is_left_alone():
    src = "See [P-Q3](/positions/quantum-interface/#p-q3) here."
    assert link(src) == src


def test_label_target_mismatch_is_editorial_intent_not_normalised():
    """Label P-Q3 pointing at a different page is deliberate; don't rewrite."""
    src = "See [P-Q3](/positions/moral-status/) here."
    assert link(src) == src
