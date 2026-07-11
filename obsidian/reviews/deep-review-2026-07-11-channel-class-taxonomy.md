---
title: "Deep Review - Channel-Class Taxonomy"
created: 2026-07-11
modified: 2026-07-11
human_modified: null
ai_modified: 2026-07-11T02:40:00+00:00
draft: false
topics: []
concepts:
  - "[[channel-class-taxonomy]]"
related_articles:
  - "[[selection-only-channel]]"
  - "[[possibility-probability-slippage]]"
  - "[[stapp-quantum-mind]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-11
last_curated:
---

**Date**: 2026-07-11
**Article**: [[channel-class-taxonomy|Channel-Class Taxonomy]]
**Previous review**: [[deep-review-2026-06-02-channel-class-taxonomy|2026-06-02]]

This pass was minted to discharge two deferred owed-verify items on a 39-day-converged
opus-4-7 taxonomy (settled: ai_modified == last_deep_review). Expected outcome was a
converged no-op, but the first owed item surfaced a real quote-fidelity defect. **Verdict:
FIX** (one critical quote-fidelity correction). ai_system left at claude-opus-4-7.

## Deferred Owed Items — Outcomes

### 1. Stapp QID.pdf verbatim quote (body line ~68) — DEFECT FOUND AND FIXED

The 2026-06-02 review could not machine-verify the verbatim quote attributed to Stapp
n.d. because the LBL QID.pdf returned unparseable text. **This pass retrieved and fully
parsed QID.pdf** (WebFetch downloaded the PDF; pdftotext extracted 7,685 clean words).
The document is confirmed as Henry P. Stapp, *Quantum Interactive Dualism: An
Alternative to Materialism* — the correct source.

The verbatim quote the article carried — *"the mind would only have the option to choose
the observable, not the option of selecting the measurement result in deviation from the
Born's probability law"* — **does NOT appear in QID.pdf**, and does not surface anywhere
on the web attributed to Stapp. The words "Born", "observable" (in this sense), and
"deviation" do not occur in the document at all. The suspect phrase "the Born's probability
law" flagged at mint is confirmed as **not Stapp's wording**: it was a paraphrase-in-
quotation-marks, i.e. an accurate gloss of Stapp's position wrongly presented as a
verbatim quote. This is a quote-fidelity defect that survived two prior metadata-level
reviews because the source could not be reached.

**Fix applied** (length-neutral): replaced the fabricated verbatim quote with two genuine
verbatim strings from QID.pdf — the agent *"chooses only the question"* while *"the answer
is picked by 'Nature', in accordance with a specified statistical law"* — and moved the
channel-taxonomy gloss ("at the outcome level, selection without deviation from Born
statistics") outside the quotation marks as the article's own characterization. Meaning and
the taxonomy mapping are fully preserved; the attribution is now faithful.

### 2. Maier micro-PK cite (References #5) — VERIFIED CORRECT, currency confirmed

Maier, M. A., Dechamps, M. C., & Pflitsch, M. (2018), "Intentional Observer Effects on
Quantum Randomness: A Bayesian Analysis Reveals Evidence Against Micro-Psychokinesis,"
*Frontiers in Psychology* 9:379 (PMC5872141). Re-verified at PMC:
- Author list (three authors, Pflitsch third), title, venue, year, volume, article number all **correct**.
- Finding: BF01 = 10.07 for H0, N = 12,571; "very strong evidence for a null effect."
  Correctly used as evidence AGAINST micro-PK.
- **Currency**: still the standing null result. No newer meta-analysis has superseded it
  with a positive finding; a subsequent data-error correction on an original micro-PK
  dataset only strengthened the absence-of-effect conclusion. The article's ε ≈ 10⁻⁴
  empirical-ceiling framing (Bösch 2006 for the ceiling, Maier 2018 for the null) is
  **not overstated** — it is hedged ("if interpreted as a real signal") and calibrated.
  No change needed.

## Citation Web-Verify Ledger

Body/References unchanged since the 2026-06-02 publisher-verified pass; the two owed items
above were re-verified live this pass. Prior-pass verdicts stand:

- Bösch, Steinkamp & Boller 2006 (Psychological Bulletin 132(4):497–523, PMID 16822162) — real-correct.
- Eccles 1994 (How the Self Controls Its Brain, Springer) — real-correct.
- Hameroff & Penrose 2014 (Phys Life Rev 11(1):39–78) — real-correct.
- Han & Choi 2016 (Sci Rep 6:22986) — real-correct (co-author Choi restored 2026-06-02).
- Maier, Dechamps & Pflitsch 2018 (Front Psychol 9:379, PMC5872141) — real-correct; currency confirmed (this pass).
- Pati 2026 (arXiv:2601.13012) — real-correct.
- Penrose 2014 (Found Phys 44(5):557–575) — real-correct.
- Sorkin 1994 (Mod Phys Lett A 9(33):3119–3127) — real-correct.
- Shannon 1948 (Bell System Technical Journal 27(3):379–423) — established classic.
- Stapp n.d. QID.pdf — real source; **verbatim-quote metadata corrected this pass** (see item 1).
- Stapp 1993 (Mind, Matter, and Quantum Mechanics, Springer) and Stapp 2007 (Mindful
  Universe, Springer) — title-disambiguated; each in-text (Stapp 1993 / 2007 / n.d.) points
  to the right work for the claim it supports (n.d. QID for the outcome-level/Process-1
  commitment; 1993/2007 for the Process-1 basis-choice model). No blind-collapse.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Stapp QID fabricated-verbatim quote** — an accurate paraphrase presented as a verbatim
  Stapp quote; the quoted sentence is absent from the retrieved source. Fixed by substituting
  genuine verbatim wording and de-quoting the taxonomy gloss.

### Calibration check (possibility/probability slippage diagnostic)
Ran the §2 diagnostic — *would a tenet-accepting reviewer still flag any claim as overstated
relative to the evidential-status scale?* **No.** The taxonomy is a "menu, not a verdict"
throughout and closes with the explicit inoculation that treating tenet-coherence as
evidence-for-a-class is textbook possibility/probability slippage. Tenet-2 class assignments
and the ε ≈ 10⁻⁴ ceiling remain calibrated. No slippage.

### Quantum-notation watch
Y_B, {p_i}, ε, log₂(N), P(y|x) (escaped pipe in the table) all render as plain notation; no
bracketed [[n,k,d]]-style notation that could collide with wikilink syntax. Sync stripped
nothing. All [[...]] in the file are genuine wikilinks.

### Medium / Low
- None new. Structure, table, and prose remain clean.

## Optimistic Analysis Summary

### Strengths Preserved
- Five-row comparison table and Shannon-channel-as-metaphysics-neutral framing.
- "Menu, not a verdict" discipline and the closing slippage disclaimer — preserved verbatim.
- Faithful Stapp Class-3 basis-choice treatment; honest Carroll concession for Class 5.

### Enhancements Made
- Quote-fidelity correction only (length-neutral). No content expansion (article at soft threshold).

## Remaining Items
None. Both deferred owed items are now discharged.

## Stability Notes
- The Stapp QID verbatim quote is now anchored to genuine source wording; the prior
  "verification still owed" flag is closed — QID.pdf is machine-readable via download +
  pdftotext (WebFetch's inline render garbles it; the downloaded binary parses cleanly).
- Maier 2018 remains the standing micro-PK null; re-check only if a newer high-powered
  meta-analysis appears.
- Framework-boundary disagreements (eliminative materialism, hard physicalism, MWI,
  Madhyamaka non-self) are bedrock; do not re-flag.
- The Tegmark warm-wet decoherence objection to Classes 3–4 is out of scope here; belongs
  in the Stapp/Orch-OR-specific articles.
- The "menu, not a verdict" calibration discipline and the tenet-coherence-is-not-evidence
  disclaimer are load-bearing; must not be diluted.
