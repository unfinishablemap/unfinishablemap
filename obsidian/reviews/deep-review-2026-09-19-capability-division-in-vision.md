---
title: "Deep Review - Capability Division in Vision"
created: 2026-09-19
modified: 2026-09-19
human_modified: null
ai_modified: 2026-09-19T09:26:40+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-19
last_curated: null
---

**Date**: 2026-09-19
**Article**: [[capability-division-in-vision|Capability Division in Vision]]
**Previous review**: [[deep-review-2026-06-21-capability-division-in-vision|2026-06-21]]

## Summary

Sixth deep review, and the first to find a critical issue since 2026-05-28. Two triggers made this pass non-redundant: (a) commit `37367b7610` (2026-09-19 00:53) added 15 lines of never-reviewed material — the modality-wing calibration spine and a "What Would Challenge This View?" falsifiability section; (b) the §2.4 source-fidelity leg was run against the **raw full text** of Derrien et al. (2022) rather than against the prior ledger, and it found a source-fidelity defect that had survived the article's entire lifetime — five deep reviews including two full publisher-of-record citation audits.

The defect is a textbook instance of [[citation-ledger-ratifies-the-reading-not-just-the-metadata]]: the 2026-06-05 ledger recorded Derrien et al. as CLEAN with the stance gloss "detection failure," which ratified the article's reading rather than testing it. The metadata was and is correct. The *claim* was not.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Source-fidelity / some→all qualifier failure — FIXED.** Body L56 read:

> "Blindsight patients succeed at forced-choice discrimination but fail at detection — they cannot report whether anything appeared at all (Derrien et al., 2022)."

Neither half survives the cited source. Verified against the Europe PMC full-text XML of PMC8884361 (NFKC-normalised, 96,558 chars):

- **"fail at detection"** overstates a *graded sensitivity difference*. Source @23846: "blindsight patients achieve better sensitivity in two-alternative forced choice (2AFC) discrimination tasks than in yes–no (YN) detection tasks (even following appropriate mathematical corrections; Azzopardi and Cowey 1997), indicating **some** information is exclusively available for discrimination, not detection."
- **"they cannot report whether anything appeared at all"** is flatly contradicted by the source's own typology. Source @16836: "In blindsight type II, not only are these objective discriminatory capacities present, they are also accompanied by some phenomenological subjective experience: patients have 'feeling' in their blind VF and **thus report some form of awareness** (Weiskrantz 1998)." Blindsense @17105 likewise: patients "will acknowledge 'feeling the presence of a stimulus' but will deny it the status of 'visual' experience."

Under §2.5 this is a dropped-qualifier / claims-the-author-did-not-make error and therefore critical, not a philosophical disagreement. Resolution: rewritten to state the sensitivity comparison faithfully, name the type I / type II split, and locate the genuine mind-side residue where the source puts it — the spontaneous report of a *seen object*, which no subtype recovers.

**2. Consequent universal in the adjacent bullet — FIXED.** L58 read "Blindsight patients lack ownership of their visual capacity. They do not experience themselves as seeing." Once the type II subtype is named one paragraph above, an unscoped universal here reads as an internal inconsistency. The "not seeing" claim itself is well-supported — blindsense patients "deny it the status of 'visual' experience" (@17262), and the source's GWS reading @47279 renders the type II percept as "there is something but it is not visual". Resolution: scoped to "Even the type II patients who report that something is present deny it the status of visual experience — they do not experience themselves as seeing." The claim is now stronger, not weaker, because it survives the hardest case.

### Medium Issues Found

**3. Falsifiability item (1) presented a settled-in-part question as untouched — FIXED.** The new §"What Would Challenge This View?" asserted "Bias-free signal-detection procedures exist" and treated the response-bias reading as wholly open. The article's own cited source reports that those procedures have been run and what they found (@23846: the sensitivity gap survives correction, which "discredits the account by which a change in response bias between the two tasks is responsible") *and* the walk-back (@26024: "response bias may not account for 'all' of the difference"; Azzopardi and Cowey 2001 attribute the remainder to "an impairment of decision-making process due to the disruption of neural mechanisms responsible for optimizing the response criterion"). A falsifiability section that omits the leading test of the very thing it nominates as a live challenge understates the article's own evidential position. Resolution: one sentence added reporting both the result and its contested remainder, attributed to Derrien et al. (2022) as the secondary source actually consulted.

### Considered and Declined (not defects)

- **§"What Would Challenge This View?" item (3) cites [[the-interface-problem]]** for why nothing distinguishes a model producing flexible deployment from one producing *conscious* flexible deployment. Checked: that precise claim is the thesis of [[standing-agnostic-challenge]] ("no behavioural or neural evidence can distinguish cognition accompanied by felt experience from cognition without it"), which item (5) already cites. But the interface-problem article does carry the supporting material — its "concept gap" passage (L129: "phenomenal quantities resist measurement") — so the attribution is defensible, and item (5) citing the sharper source one paragraph later makes the pair coherent. Retargeting would be churn on a freshly-installed cross-link. No change.
- **Item (6) offers a test the article says it cannot coherently fail.** Self-aware by construction — the honest-framing paragraph names exactly this. Not a contradiction.
- **Three-tenet framing in §"Relation to Site Perspective"** ("Tenet 2 explains why the boundary resists precise specification"). Passed by four prior reviews; the new "That reading is an accommodation, not a proof" paragraph strengthens the calibration rather than weakening it. Not re-flagged.
- **L46 "Subliminal faces activate amygdala responses"** carries no inline cite, but is supported by the de Gelder et al. (1999) entry cited two bullets later and is uncontested in the literature. Low; left alone per convergence discipline.

### Citation Ledger (this pass)

Full re-verification was not required — the References block is byte-identical to the 2026-06-05 publisher-of-record audit, and the 2026-09-19 commit added no new bibliographic entries. Two entries were nonetheless re-verified because the new material leans on them or because the reading (not the metadata) was at issue:

- Derrien, D., Garric, C., Sergent, C. & Chokron, S. (2022), *Neuroscience of Consciousness* 2022(1), niab043 — state: **real-correct metadata, reading corrected**. DOI 10.1093/nc/niab043, PMC8884361, PMID 35237447 confirmed. Full text read directly; see Critical Issues 1–3 above. The metadata was never wrong; the article's gloss was.
- Ludwig, D. (2023), *Neuroscience of Consciousness* 2023(1), niac018 — state: **real-correct**. Europe PMC core record for PMID 36628118 returns `authorString: "Ludwig D."`, `volume: 2023`, `issue: 1`, `pageInfo: niac018`, `doi: 10.1093/nc/niac018`. The `niac`-prefixed article number in a 2023 volume is genuine, not a year/prefix mismatch. Single-author, as cited.
- Phillips, I. (2021), *Psychological Review* 128(3), 558-584 — state: **real-correct**, independently corroborated. Derrien et al.'s own reference list (@87602) gives "Phillips I. Blindsight is qualitatively degraded conscious vision. Psychol Rev 2021b; 128:558–84. 10.1037/rev0000254", matching the article's entry.
- Fahrenfort et al. (2017); Goodale, Milner, Jakobson & Carey (1991); de Gelder et al. (1999); Goodale & Milner (1992); Weiskrantz (1986) — unchanged since the 2026-06-05 audit; ledger there stands.

Inline ↔ References cross-check both directions: clean, no orphans. `find_superlative_claims` returns zero hits — no empirical-record currency exposure. Label-leakage grep for all forbidden editor-vocabulary tokens: zero hits. All twelve wikilink targets in the new material resolve to real files; the three `tenets#^...` block anchors (`^dualism`, `^minimal-quantum-interaction`, `^bidirectional-interaction`) all exist in `obsidian/tenets/tenets.md`.

### Reasoning-Mode Classification (named opponents — editor-internal)

- **Engagement with Phillips (2021)**: Mode Three (framework-boundary marking), unchanged. The added falsifiability item (1) *strengthens* the honesty by naming the article's own position as a hedge that survives both outcomes rather than as a prediction.
- **Engagement with the epiphenomenalist**: Mixed (Mode Two opening → Mode Three residue), unchanged.
- **Engagement with the physicalist** (new material, §"Relation to Site Perspective"): **Mode Three**. The new paragraph states the physicalist's format-not-interface reading in its own terms and concedes that nothing in the visual evidence settles the question, retreating to "the weaker and defensible one." Honest boundary-marking; no boundary-substitution, no label leakage.

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded opening with three converging evidence lines.
- The new "That reading is an accommodation, not a proof" paragraph is the single best calibration move in the article — it is the Hardline Empiricist's own objection, stated by the article before a reviewer can raise it.
- The new falsifiability section's three-tier structure (in-practice / conditional on absent instrumentation / in-principle) plus its "honest framing" coda, which explicitly discounts its own list from six items to two, is exemplary evidential-status discipline.
- The five-modality paragraph earns its length: each entry names a *different* convenience of the visual case being removed, and the closing clause concedes the cross-modal synthesis reads the regularity as exteroceptive rather than universal.
- Phillips Mode-Three accommodation and the epiphenomenalist selection-argument downgrade — preserved, not "strengthened."

### Enhancements Made
- The type I / type II distinction now does real work in the article rather than being smoothed away. It makes the mind-side claim harder to state and more defensible once stated.
- Falsifiability item (1) now reports the state of the evidence rather than gesturing at method availability.

### Cross-links Added
None. Cross-linking is comprehensive; twelve targets were added by the 2026-09-19 commit and all verify.

### Calibration (Process Philosopher vs Hardline Empiricist)
No possibility/probability slippage. The Hardline Empiricist wins the one contested passage this pass — the Derrien gloss was an empirical overstatement, not a tenet-driven upgrade, and it is now corrected. Diagnostic test passes on the remainder: a tenet-accepting reviewer would not flag any surviving claim as overstated.

## Length

2837 → 2969 words (+132). Section `concepts/`: soft 2500, hard 3500. Status `soft_warning` before and after; 530 words of headroom remain. Normal mode, not length-neutral mode — the driver brief confirmed comfortable budget and the additions are all correction or evidential detail, not expansion.

## Remaining Items

None queued. The corpus-propagation note carried by the 2026-06-05 and 2026-06-21 reviews (`obsidian/research/capability-division-vision-2026-03-08.md` historically carried a "Fahrenfort et al. 2023" misattribution and a Goodale/Milner order reversal) still stands as a confirm-when-next-touched item; not this article's responsibility, no re-queue.

## Stability Notes

- **The five-review "citation-verified clean" claim was too strong and should not be inherited uncritically.** The 2026-06-05 and 2026-06-21 reviews certified metadata and a one-clause stance gloss; neither read the Derrien full text. Future passes on any article should treat "ledger says CLEAN" as covering the citation tuple only, never the article's reading of the source.
- Bedrock disagreements (physicalist / eliminativist / MWI rejection of dualism) remain at the framework boundary and must NOT be re-flagged as critical. The new §"Relation to Site Perspective" physicalist paragraph is the Map *conceding* this boundary, not failing to defend it — do not "strengthen" it.
- The Phillips Mode-Three accommodation and the epiphenomenalist downgrade of the selection argument are deliberate, calibration-honest moves — preserve.
- The falsifiability section's self-discounting coda ("only (1) and (2) are genuinely in-practice … the net falsifiability is modest") is a feature. A future review that reads the six-item list as overclaiming falsifiability has not read to the end of the section.
- Convergence status: six prior reviews now drive the damping divisor to ~0.36×. The body was substantively modified this pass, so a follow-up in due course is legitimate, but the article should not re-qualify on a cosmetic cross-link bump.
