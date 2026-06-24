---
ai_contribution: 100
ai_generated_date: 2026-06-24
ai_modified: 2026-06-24 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-24
date: &id001 2026-06-24
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Consciousness-Selecting Neural Patterns
topics: []
---

**Date**: 2026-06-24
**Article**: [Consciousness-Selecting Neural Patterns](/concepts/consciousness-selecting-neural-patterns/)
**Previous review**: [2026-06-20](/reviews/deep-review-2026-06-20-consciousness-selecting-neural-patterns/)
**Word count**: 3490 (body, pre-edit) → 3503 (post-edit; net +13 from a body sentence rewrite required to fix two miscitations, partly offset by trims)

## Purpose of this pass: GENUINE-DRIFT verification of two unverified refines

The 2026-06-20 review verified the article through commit 4abeddfa9 and declared converged. **Two substantive refine-draft commits landed afterward**, both "from convergent outer reviews," neither verified by a deep-review:

- **569f582ce** (2026-06-23) — added the **"Active-Inference Rival"** subsection (the omitted physicalist competitor) + the Sandved-Smith et al. 2021 citation.
- **186132d5a** (2026-06-23) — conditioned the causal-closure claim (now "a *possible* breach... only conditionally," listing Everettian/Bohmian/objective-collapse/quietist alternatives), pulled distributed caveats inline, and **added two 2024–26 literature citations** (BMC Anesthesiology 2025, Scientific Reports 2024) to the microtubule passage.

A refine stamp is not a review stamp. This pass scrutinised the post-refine content directly. **Verdict: the new argument content is correctly calibrated, but the §2.4 publisher-of-record web-verify caught TWO real citation defects in the newly-added cites — wrong-author/wrong-species and fabricated-title — that intra-corpus consistency could not surface.** Both fixed.

## (a) Citation ledger — full web-verify of the 3 NEW cites (3-state)

The ~15 pre-existing cites were exhaustively web-verified real-correct in the 2026-06-05 and 2026-06-20 passes and are unchanged; this pass web-verified the three cites the two refines introduced (the highest-yield defect channel per §2.4).

- **Sandved-Smith, L., Hesp, C., Mattout, J., Friston, K., Lutz, A., & Ramstead, M.J.D. (2021)** — *Neuroscience of Consciousness* 2021(1), niab018, "Towards a computational phenomenology of mental action…" — **real-correct** (web-verified Oxford Academic / PubMed 34457352). Authors, title, venue, article ID all exact. Body characterization ("attention as a controllable policy, mental effort as precision-weighting, focus→distraction→meta-awareness→refocus cycle, policy selection over higher-level cognitive states") matches the paper's own abstract verbatim-in-substance. (A published correction niab035 exists; niab018 is the correct canonical article ID — not a defect.)

- **2025 *BMC Anesthesiology* study** — **real-paper-WRONG-AUTHOR + WRONG-SPECIES → FIXED (CRITICAL).** The DOI s12871-025-02956-9 is real, but the refine cited it as **"Khan, S. et al. (2025)… in rats"** with an invented title "Microtubule-binding drugs modulate anesthetic sensitivity in rats." Web-verify (Springer / BMC) shows the actual paper is **Li, N., You, Z., Ren, Y., … Martyn, J.A.J. (2025), "Microtubule-modulating drugs alter sensitivity to isoflurane in mice," *BMC Anesthesiology* 25:109** — first author **Na Li** (Martyn lab), NOT Khan, and the study used **CD1 mice, NOT rats**. The refine appears to have conflated this paper with the genuinely-Khan/Wiest 2024 *eNeuro* **rats** epothilone-B paper (correctly cited elsewhere in the same passage). The *findings* the body reports (epothilone D + vinblastine left-shift the isoflurane ED50; paclitaxel slightly resistant) are accurate. Corrected: inline "Khan et al. (2025)… ED50" → "Li et al. … in mice the isoflurane ED50"; References entry rewritten to the canonical Li/2025/mice/25:109 form. This is exactly the wrong-author/wrong-species class §2.4 / ai_citation_metadata_unreliable targets — invisible to intra-corpus cross-check.

- **2024 *Scientific Reports* study** — **real-paper-FABRICATED-TITLE → FIXED (CRITICAL).** The DOI s41598-024-68852-3 is real, but the refine gave it the **invented title "Non-thermal microwave exposure and anesthetic unconsciousness"** with no author. Web-verify (nature.com / PMC11306338) shows the actual paper is **Hammarin, G. et al. (2024), "No observable non-thermal effect of microwave radiation on the growth of microtubules," *Scientific Reports* 14:18286** (Neutze group, Chalmers) — about microtubule *growth*, **nothing to do with anaesthesia**. The body's gloss ("a non-thermal-microwave null") was directionally fine but the invented reference title fabricated the paper's subject. Corrected: References entry rewritten to the canonical Hammarin/2024/microtubule-growth/14:18286 form; body softened to "found no non-thermal microwave effect on microtubule growth once heating controls were applied" (faithful to the paper's actual finding, which was a thermal artifact). (An Author Correction s41598-024-72098-4 exists; the primary article 68852-3 is correct.)

**Inline ↔ References cross-check (both directions):** complete after fixes. Every inline author-year (now incl. Li, Sandved-Smith) has a References entry; the two corrected entries are each cited inline; no orphans.

### Family-resolution sub-finding
The BMC 2025 paper is also cited in sibling [empirical-evidence-for-consciousness-selecting](/topics/empirical-evidence-for-consciousness-selecting/). **That article cites it CORRECTLY** — "mouse study," correct title, correct directional findings (it does not carry the Khan/rats defect; it lists the entry author-as-journal-name "BMC Anesthesiology" alphabetized under B, a stylistic imperfection, not a metadata error). Left as-is to avoid disturbing its alphabetical ordering convention; its body and title are faithful. The defect was specific to the new content in the article under review (one refine fork got it wrong; the independently-written sibling got it right) — confirming intra-corpus consistency does NOT ratify across separately-authored files here.

## (b) New argument content — calibration & reasoning-mode

- **Active-Inference Rival subsection (new, 569f582ce)** — **calibration PASS, Mode Three (framework-boundary marking), no boundary-substitution, no label leakage.** The section (1) names active inference "the strongest physicalist rival," (2) explicitly *declines* a false Mode-One refutation ("Active inference is not defective on its own terms"), (3) locates the disagreement at the residual which-outcome step and marks it bedrock ("a determinist or brute-chance theorist can occupy the same architecture and decline the selector"), (4) invokes [evidential-status-discipline](/project/evidential-status-discipline/) to forbid dressing it as a refutation, and (5) states the bandwidth argument "constrains the *form*… without showing that one operates at all." This is honest restraint, not slippage. Diagnostic test passes: a tenet-accepting reviewer would not flag any evidential label as overstated. No editor-vocabulary leaked into prose (grep-confirmed). New wikilinks [predictive-processing-and-dualism](/topics/predictive-processing-and-dualism/), [evidential-status-discipline](/project/evidential-status-discipline/) both resolve.
- **Conditioned causal-closure claim (186132d5a)** — **calibration PASS / improvement.** The old flat "Causal closure fails precisely at this gap" is now "the Map locates a *possible* breach… but only conditionally," explicitly listing the four rival resolutions (Everettian, Bohmian, objective-collapse, quietist) that close the gap without a selector and marking the dualist reading as "one interpretation… chosen partly for tenet-fit, not a result forced on anyone." This is a strict honesty upgrade — removes an over-claim a tenet-accepting reviewer would have flagged. No new defect introduced.

## (c) Currency / construct / leakage sweep — PASS

- **Superlative-claim sweep** (`tools.curate.empirical_currency.find_superlative_claims`): **none detected.** No empirical-record-currency-drift exposure.
- **Banned construct** ("This is not X. It is Y."): none present.
- **Label leakage** (direct-refutation-feasible, unsupported-jump, bedrock-perimeter, Engagement classification:, Evidential status: callouts, etc.): none in prose.
- **Wikilinks**: all new targets resolve (post-decoherence-selection, adaptive-computational-depth, amplification-void, predictive-processing-and-dualism, evidential-status-discipline).

## (d) Length — HARD-THRESHOLD breach flagged for human decision

The two unverified refines added ~470 body words to a converged 3016-word article (2026-06-20 measure), brushing the **3500 hard ceiling** for concepts/. Post-fix the article is **3503 words (140% of soft, hard_warning)** — ~3 words over. I trimmed prose redundancy in the active-inference section and the microtubule sentence (recovering ~15 words) but stopped short of cutting into load-bearing argument, which would risk the documented over-correction-into-mush failure mode on a Tenet-3 flagship. The 3-word overage is not worth degrading the argument; a human length decision is queued (see todo). This is NOT auto-condensable — the calibration register must be preserved.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Wrong-author/wrong-species cite** (BMC 2025: "Khan et al. … in rats" → Li et al. … in mice) — FIXED, web-verified.
- **Fabricated reference title** (Sci Rep 2024: invented anaesthesia title → real Hammarin microtubule-growth title) — FIXED, web-verified.

### Medium Issues Found
- Article ~3 words over hard length ceiling after the two refines — trimmed toward the ceiling; residual overage flagged for human length decision (not auto-condensable).

### Counterarguments Considered
All six adversarial personas engaged. Bedrock disagreements (eliminative-materialist rejection of a selecting subject, MWI-defender dissatisfaction with the indexical answer, Buddhist-anatta pressure on the enduring selector, materialist reading of the Schwartz OCD result — already self-caveated n=18/no-replication) are inherent to the Map's dualist position and are NOT re-flagged. The new active-inference engagement is a genuine strengthening: the strongest physicalist rival is now confronted on its own terms rather than ignored.

## Optimistic Analysis Summary

### Strengths Preserved
- Post-decoherence framing as the most defensible version (front-loaded).
- Bandwidth → policy argument with explicit bridging premise.
- Four-response decoherence structure with the honest coherence→specificity trade.
- Illusionism reply (regress + self-representation) without the Dennett strawman.
- Falsifiability Dilemma with honest metaphysical framing (tenet-as-evidence-upgrade explicitly declined).
- **NEW, preserved**: the Active-Inference Rival section (strongest physicalist competitor confronted honestly) and the conditioned causal-closure claim (over-claim removed).

### Enhancements Made
- Two citation defects fixed (web-verified to publisher of record).
- Prose trims in the active-inference section and microtubule passage (redundancy removal, length recovery).

### Cross-links
No new cross-links needed; the two new wikilinks from the refines resolve.

## Remaining Items

- **Human length decision**: article sits ~3 words over the 3500 hard ceiling after legitimate convergent-outer-review additions. Decide whether to accept the marginal overage (the additions are load-bearing) or commission a deeper condense. NOT auto-condensable — Tenet-3 calibration register must be preserved.

## Stability Notes

Tenth deep review. The article's prose and argument are at firm convergence; the only churn is (1) citation hygiene on freshly-added cites and (2) reviewer-driven honesty upgrades (conditioned closure, active-inference confrontation). Both 2026-06-23 refines were content-positive but the §2.4 web-verify was essential: a refine fork that adds 2024–26 literature is a fresh-create-style defect surface (fresh-create-defect-tail, ai_citation_metadata_unreliable) — here it conflated the Khan/2024/rats paper with the Li/2025/mice paper and invented an anaesthesia title for a microtubule-growth paper. Both invisible to intra-corpus cross-check; only the publisher of record caught them.

Bedrock philosophical disagreements (eliminative-materialist, MWI-defender, Buddhist-anatta, materialist-reading-of-Schwartz) are inherent to the Map's dualist position and should NOT be re-flagged as critical in future reviews. The selection mechanism's modal register — the Map's Tenet-3 hypothesis / metaphysical interpretation, not established science — is correctly held throughout and must be preserved against any future condense pass. The active-inference engagement is Mode-Three honest boundary-marking and should NOT be "upgraded" to a refutation. `ai_system` of the source is the historical `claude-opus-4-5-20251101`; an authorship record, not a defect.

Future reviews of any refine that touches the References block of this (or any) citation-heavy article MUST re-run the §2.4 publisher-of-record web-verify on the changed cites — this pass is the proof that "a refine added literature" is sufficient to re-qualify for verification even when the deep-review converged days earlier.