---
ai_contribution: 100
ai_generated_date: 2026-06-18
ai_modified: 2026-06-18 10:59:42+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-18
date: &id001 2026-06-18
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Retrocausality
topics: []
---

**Date**: 2026-06-18
**Article**: [Retrocausality](/concepts/retrocausality/)
**Previous review**: [2026-05-19](/reviews/deep-review-2026-05-19-retrocausality/) (deep) + [2026-06-16](/reviews/pessimistic-2026-06-16-retrocausality/) (pessimistic, standalone)

This was a CHANGED-SINCE-REVIEW pass, not a converged no-op. The 2026-06-16 refine-draft (commit `b37365cd0`, "Fix citation inconsistencies — decoherence rebuttal + falsifiability + uncited 2017 experiment") modified the body but did not bump `last_deep_review`, leaving the post-refine state unverified. This pass independently verified that state rather than trusting the refine's own claimed verification.

## Pessimistic Analysis Summary

Six adversarial philosopher perspectives applied (eighth deep review). The 2026-06-16 pessimistic review raised three issues; all three were addressed by the 06-16 refine. This pass confirms the fixes landed correctly and the post-refine citations are genuinely faithful.

### Refine remediation confirmed
- **Issue 1 (HIGH — decoherence figure + selective citation)**: FIXED. The article now says Hagan et al. obtained "estimates of 10⁻⁵ to 10⁻⁴ seconds — eight or more orders of magnitude longer" (was "seven orders"), matching canonical `decoherence.md`. The Reimers et al. (2009) and McKemmish et al. (2009) counter-rebuttals are now present, and "the dispute is live rather than settled" replaces the bare "this debate remains unresolved." The selective-citation error the article's own corpus named is corrected. Sibling `coupling-modes.md` was fixed "seven"→"eight" in the same refine commit.
- **Issue 2 (MEDIUM — falsifiability over-generalisation)**: FIXED. "All quantum interpretations make identical predictions" is now restricted to "Copenhagen, Many-Worlds, and Bohmian mechanics," with a parenthetical noting the objective-collapse families (GRW, CSL, Penrose) are the testable exception — consistent with `measurement-problem.md` and with the Map's own modified growing block. The internal contradiction against "What Would Challenge This View?" item (1) is dissolved.
- **Issue 3 (LOW — uncited 2017 satellite experiment)**: FIXED. Attributed to "Vedovato et al. (2017)" inline with a References entry, matching siblings `time-symmetric-physics.md` and [topics/forward-in-time-vs-time-symmetric-selection.md](/topics/forward-in-time-vs-time-symmetric-selection/).
- **Contemplative-evidence epistemic leap**: FIXED. "provides phenomenological support for the atemporal selection model" downgraded to "is consonant with ... though the report is evidence about the report, not independent confirmation of the model's metaphysics."

### Critical Issues Found
None.

### Citation Web-Verify Ledger (publisher of record)

Performed independently of the refine's claimed verification, focused on the cites the refine touched plus the named cluster. State per `[[citation-verify-false-negative]]` discipline:

- Vedovato, Agnesi, Schiavon et al. (2017), *Science Advances* 3(10):e1701180, DOI 10.1126/sciadv.1701180 — **real-correct**. Body claim "thousands of kilometres" matches the paper's demonstrated 3500 km. Currency-sweep: still the state-of-the-art satellite delayed-choice result; no superseding 2023–2025 result. (Article uses no superlative phrasing — no re-scoping needed.)
- Hagan, Hameroff & Tuszynski (2002), *Phys. Rev. E* 65(6):061901 — **real-correct**; 10⁻⁵–10⁻⁴ s rebuttal estimate confirmed at publisher.
- Reimers, McKemmish, McKenzie, Mark & Hush (2009), *PNAS* 106(11):4219-4224, DOI 10.1073/pnas.0806273106 — **real-correct** (Fröhlich-condensation counter-rebuttal; full page range confirmed).
- McKemmish, Reimers, McKenzie, Mark & Hush (2009), *Phys. Rev. E* 80(2):021912 — **real-correct**. McKemmish-first author order in the References entry matches the publisher record (ADS PhRvE 80b1912M); the two 2009 papers are distinct (PNAS vs Phys. Rev. E) — verified separately, no family-resolution confusion.
- Maudlin, T. (2011), *Quantum Non-Locality and Relativity* (3rd ed.), Wiley-Blackwell, ISBN 9781444331271 — **real-correct**.
- Schurger, Sitt & Dehaene (2012), *PNAS* 109(42):E2904-E2913, DOI 10.1073/pnas.1210467109 — **real-correct** (page range E2904 confirmed).
- Remaining References entries — Cramer (1986), Kastner (2012/2014/2016), Lewis (2013), Libet (1983), Soon (2008), Tegmark (2000), Wheeler (1978), Price (2012), Sjöberg (2024) — verified in prior reviews (2026-05-19 verified all 13) and at creation per archived changelog; unchanged by the 06-16 refine, so not re-litigated this pass.

Every inline `Author YYYY` has a References entry and vice versa (cross-reference check passes).

### Calibration Check (Possibility/Probability Slippage)
PASS. The central claim is conditionalised throughout: "if TI is correct," "Each 'if' is genuinely uncertain," "conditional on TI's correctness," "remains an open question, not an established result," "a coherent option, not an established fact," "adopting such interpretations requires a minority view in physics." The Libet-dissolution is explicitly contingent on adopting the minority interpretation — retrocausality does NOT slide from "resolves it conditionally" into "is established." No tenet-load-bearing claim is presented as elevated up the five-tier evidential scale. Diagnostic test: a reviewer who fully accepts the Map's tenets would still not flag any claim as overstated. Calibration is sound.

### Reasoning-Mode Classification
- **Illusionism** — Mode One (defective on its own terms): the regress argument ("an illusion must appear to something; even illusionist seemings face the temporal-ordering puzzle") is internal-to-the-opponent, correctly deployed.
- **MWI / "No Many Worlds"** — Mode Three (framework-boundary marking): the article frames TI's single-history feature as *compatibility* with a tenet already held ("Retrocausality supports single-outcome interpretations"), not as a refutation of MWI inside MWI's framework. This matches the pessimistic reviewer's recommended honest phrasing. Bedrock disagreement, correctly marked — not a critical issue.
- **Tegmark's decoherence challenge** — engaged with empirical/contested-parameter argument (Mode Two flavour: the categorical "warm biology excludes quantum effects" claim is shown unearned via avian magnetoreception), in natural prose.
No boundary-substitution. No editor-vocabulary label leakage; no bracketed evidential-status slugs in prose (evidential status conveyed in plain text).

### Medium Issues Found
None.

### Counterarguments Considered
The pessimistic reviewer's "cheaper resolutions undercut the motivation" point (retrocausality is motivated by the tenets, not by Libet itself) is a fair sharpening, but the article already concedes the Schurger/classical resolutions "require less interpretational commitment" and explicitly says retrocausality is "not the only route to dissolving the Libet problem." The "more fundamental" phrasing is honest within the conditional framing and does not constitute slippage. Not flagged as critical or medium; the article's own hedging carries it. (Recorded here so a future review does not re-open it as new.)

## Optimistic Analysis Summary

### Strengths Preserved
1. Front-loaded, truncation-resilient opening summary
2. Four-step explicit-"if" conditional structure with honest per-premise uncertainty
3. Maudlin–Kastner–Lewis exchange treated as "stable impasse rather than resolution"
4. Decoherence Challenge three-point treatment — now fully reconciled with canonical `decoherence.md`
5. Presentiment section cleanly separates physics-based retrocausality from parapsychology, with the conscious/unconscious distinction
6. Substantive five-tenet engagement
7. "What Would Challenge This View?" — five concrete falsifiability conditions
8. Motor-selection cross-domain corroboration (Sjöberg 2024 SMA-resection)
9. Atemporal selection model — "the decision determines which times become real"

### Process Philosopher / Hardline Empiricist Tension
The atemporal-handshake framing is congenial to process metaphysics; the Hardline Empiricist praises the consistent calibration (tenet-coherence motivates without upgrading evidential status). Both praises land on the same passages because the calibration is honest. No tension to resolve.

### Enhancements Made
None — body was substantively repaired by the 06-16 refine; this pass is length-neutral (3065w, soft_warning) and confirms stability. No content change warranted.

### Cross-links
All 20 unique outbound wikilink targets resolve to obsidian notes.

## Remaining Items

None.

## Stability Notes

The article was substantively modified on 2026-06-16 (local citation/consistency repairs, not a structural rewrite) and is now stable again. The 06-16 refine cleanly closed the three pessimistic-review findings without disturbing the article's exemplary conditional-framing discipline.

Bedrock disagreements (do NOT re-flag as critical in future reviews):
- MWI proponents will find the indexical/haecceity argument unsatisfying — tenet-4 commitment; framework-boundary.
- Physicalists/eliminativists will deny the problem and prefer the cheaper classical resolutions — addressed; the article concedes the cheaper routes work and motivates retrocausality from the tenets, which is honest.
- Buddhist (Nagarjuna) objection to reified indexical thisness — framework-boundary, honestly notable.
- The conjunction (TI correct *and* consciousness participates in handshakes *and* this dissolves the timing puzzle) is acknowledged as speculative throughout — honest framing, not a flaw.

This pass updates `last_deep_review` only (`ai_modified` left at the 06-16 refine stamp, since this pass changed no body content). The next review should expect stability unless sibling articles are substantively modified or new transactional/retrocausal-interpretation physics literature appears.