---
title: "Deep Review - Neural Implementation Specifics"
created: 2026-07-11
modified: 2026-07-11
human_modified: null
ai_modified: 2026-07-11T07:58:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-5-20251101
ai_generated_date: 2026-07-11
last_curated: null
---

**Date**: 2026-07-11
**Article**: [[neural-implementation-specifics|Neural Implementation Specifics]]
**Previous review**: [[deep-review-2026-06-05-neural-implementation-specifics|2026-06-05]]
**Review number**: 7th (after 2026-02-02, 2026-02-08, 2026-03-03, 2026-03-25, 2026-05-22, 2026-06-05)

## Context

Selected as a staleness / owed-web-verify pass. The article was untouched since its 2026-06-05 review (`ai_modified` == `last_deep_review` == 2026-06-05, 36 days converged). The 2026-06-05 review is just after the pre-discipline cutoff and web-verified four load-bearing cites (Denton, Khan, Wiest, Player & Hore) but took the other six on "consistent with prior-review" trust. Because the References are the corpus's highest-defect-density cluster (quantum-biology / microtubule) with several fast-moving recent empirical cites, this pass ran a **full 11-cite publisher-of-record re-verification** rather than trusting the intra-corpus record.

Length 2413 words (80% of the 3000 topics soft target) — length-safe. Pass operated length-neutral; no growth.

## Pessimistic Analysis Summary

### Critical Issues Found

None.

### Publisher-of-Record Citation Ledger (all 11 web-verified this pass)

- Beck & Eccles 1992 (Quantum aspects of brain activity...) — **real-correct**. PNAS 89(23) 11357-11361, DOI 10.1073/pnas.89.23.11357. Exocytosis-tunneling model attributed correctly.
- Denton et al. 2024 (Magnetosensitivity of tightly bound radical pairs... quantum Zeno effect) — **real-correct**. Nature Communications 15, 10823, DOI 10.1038/s41467-024-55124-x, lead author Denton (Exeter). Article's "showing computationally" hedge is faithful (paper is a modelling study).
- Fisher 2015 (Quantum cognition...) — **real-correct**. Annals of Physics 362, 593-602, arXiv:1508.05929. Posner Ca9(PO4)6 phosphorus-qubit proposal attributed correctly.
- Georgiev & Glazebrook 2018 (Quantum physics of synaptic communication via SNARE) — **real-correct**. Prog. Biophys. Mol. Biol. 135, 16-29, PubMed 29371042. Davydov-soliton upgrade of Beck-Eccles attributed correctly.
- Hagan, Hameroff & Tuszynski 2002 (Quantum computation in brain microtubules...) — **real-correct**. Physical Review E 65(6) 061901, ADS 2002PhRvE..65f1901H. Cited as the decoherence-feasibility objection — correct role.
- Kalra et al. 2023 (Electronic energy migration in microtubules) — **real-correct**. ACS Central Science 9(3) 352-361, DOI 10.1021/acscentsci.2c01114, arXiv:2208.10628. Anesthetics-decrease-energy-migration stance confirmed by the paper's own findings (etomidate/isoflurane decrease migration).
- Khan et al. 2024 (Epothilone B delays anesthetic-induced unconsciousness) — **real-correct**. eNeuro 11(8) ENEURO.0291-24.2024 (re-confirmed; matches 2026-06-05 verification).
- Player & Hore 2018 (Posner qubits: Ca9(PO4)6...) — **real-correct**. J. R. Soc. Interface 15(147) 20180494, arXiv:1807.06339. ~37-min coherence upper bound confirmed.
- Qaswal et al. 2021 (Mathematical modeling of ion quantum tunneling...) — **real-correct**. Pathophysiology 28(1) 116-154, PMC8830480, University of Jordan. Excitability-disorder / voltage-gated-channel tunneling model attributed correctly.
- Tegmark 2000 (Importance of quantum decoherence in brain processes) — **real-correct**. Physical Review E 61(4) 4194-4206, arXiv:quant-ph/9907009. Decoherence-timescale objection attributed correctly.
- Wiest 2025 (A quantum microtubule substrate of consciousness...) — **real-correct**. Neuroscience of Consciousness 2025(1) niaf011, DOI 10.1093/nc/niaf011, PubMed 40342554. **NOT a phantom** (cf. babcock-hameroff-2025 phantom-cite trap). Superlative check: the paper's strong title claim ("experimentally supported and solves the binding and epiphenomenalism problems") appears only in the References entry (its actual title); the body attributes the super-radiance and MRI-detection claims to Wiest with explicit hedges ("though the evidence remains under evaluation", "if validated") and does **not** adopt the title claim as settled fact. No source/Map conflation, no over-claim.

**Result: 11/11 real-correct. Zero fabrications, zero wrong-metadata, zero currency-superseded superlatives.** Every inline `Author YYYY` has a References entry and vice versa (no orphans; the Hagan orphan was resolved in the 2026-06-05 pass and remains anchored).

### Empirical-currency / superlative sweep

`find_superlative_claims` returned only a false-positive header ("So Far"). No categorical/"experimentally established" framing asserted as Map fact. The five-month gap since authoring introduced no known superseding result for the 2023-2025 empirical cites.

### Notation / EOF hygiene

- Posner notation `Ca₉(PO₄)₆`, isotope labels `³¹P`/`³⁰P`, `Na⁺`/`K⁺`/`Ca²⁺` all use Unicode sub/superscripts and parentheses — **no square brackets**, so no `[[...]]` wikilink collision (qec-notation trap does not apply here). No backtick-wrap needed.
- No leaked tool-call-tag artifact at EOF of article or this review file.

### Calibration check (§2 diagnostic)

A tenet-accepting reviewer would not flag any evidential-status label as overstated. Tenet-2 (Minimal Quantum Interaction) and Tenet-3 (Bidirectional Interaction) structure the "Relation to Site Perspective" survey; no mechanism (Orch-OR, Posner, radical-pair, ion-channel, SNARE) is asserted as established. The decoherence-timing table's "Verified" for radical-pair coherence *time* is honest — microsecond coherence is demonstrated in cryptochrome — and the body (line 61) explicitly keeps coherence-demonstrated separate from cognitive-role-unestablished. No possibility/probability slippage.

### Cross-link integrity

All 12 body + Further Reading wikilinks resolve to live (non-archived) obsidian targets; the `related_articles` research-note reference (`quantum-biology-neural-mechanisms-2026-01-24`) also resolves. No archival-link-rot.

## Optimistic Analysis Summary

### Strengths Preserved

Three-criteria evidence hierarchy; falsifiable "Required evidence" per mechanism; scannable comparison tables; front-loaded summary; mechanism-agnosticism; Crucial Experiments section; the underdetermination sentence added in the 05-22 refine (radical-pair coherence settles what *can* happen, not what consciousness exploits).

### Enhancements Made

None. The article is at durable content stability; the high-value work this pass was the full citation re-verification, which came back clean. No change-for-change's-sake edits.

## Remaining Items

None.

## Stability Notes

- **Seven reviews; textbook convergence.** All 11 citations now independently web-verified at the publisher of record (the six previously trusted on intra-corpus consistency are now confirmed exact). No re-verification needed absent substantive new content.
- **Wiest title-claim discipline holds**: the strong "solves the binding and epiphenomenalism problems" phrasing lives only in the References (its real title); the body hedges. Future reviews should not read the References-entry title as a Map assertion.
- **Bedrock disagreements** (eliminative materialist, Dennettian functionalist, Tegmark decoherence [addressed Mode One via Tegmark's own computation/effects distinction], MWI selection-language, Buddhist non-self) — do not re-flag.
- **QuantNeuro / Waterloo claim** — stable "peer-reviewed publication pending" hedge across seven reviews; tighten only if published.
- **Stamp policy this pass**: settle-verdict after real scrutiny with no content fix → `last_deep_review` bumped to 2026-07-11, `ai_modified` held at 2026-06-05, `ai_system` held at claude-opus-4-5-20251101 (verify pass, not re-authoring).
