---
ai_contribution: 100
ai_generated_date: 2026-07-26
ai_modified: 2026-07-26 02:17:48+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-26
date: &id001 2026-07-26
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-26 02:17:48+00:00
modified: *id001
related_articles: []
title: Deep Review - Phenomenal Authority and First-Person Evidence (post-refine calibration
  verify + length decomposition)
topics: []
---

**Date**: 2026-07-26
**Article**: [Phenomenal Authority and First-Person Evidence](/topics/phenomenal-authority-and-first-person-evidence/)
**Previous review**: [2026-07-11](/reviews/deep-review-2026-07-11-phenomenal-authority-and-first-person-evidence/) (9th review; clean settle + one low style fix)
**This pass**: 10th review. Genuine post-refine pass — the 2026-07-21 `auto(refine-draft)` (commit 8300f12f0, CONVERGENT outer reviews ChatGPT 5.6 Pro + Claude Opus 4.8) added ~450 words of load-bearing calibration prose across four passages. This review verifies that the refine landed clean and resolves the raw-length false-breach that has been length-blocking the article in `/replenish-queue`.

## Verdict

**CLEAN SETTLE (NO BODY EDITS) + LENGTH DECOMPOSITION.** No critical, medium, or actionable low issues. The 2026-07-21 refine's four calibration changes are exemplary implementations of the possibility/probability-slippage discipline — all verified sound; none reverted. The apparent 4441-word hard-ceiling breach is a `[[analyze_length counts reference apparatus]]` artifact: **argument prose is 3757 words, under the 4000 topics hard ceiling**; the overage is the 490-word References block plus the 195-word Further Reading list. No condensation of protected calibration prose. Frontmatter: `last_deep_review` advanced; `ai_modified` held at HEAD (2026-07-21T12:17:30) per no-op-body discipline.

## What changed since the last review (2026-07-21 refine — verified sound)

The refine touched **no citations, no References entries, no attributed quotes** (diff confirmed). It rewrote four passages, each correcting a residual over-claim the convergent outer reviews flagged. All four are the calibration discipline working exactly as intended:

1. **Phenomenal Conservatism — "cuts both ways" paragraph (added).** New prose concedes PC is a *general* thesis: the naturalist's closure/third-person seemings earn the same prima facie justification, so the Map's asymmetry "has to be argued rather than read off PC." Textbook honesty; removes any read of PC as self-privileging phenomenal seemings. **CLEAN.**

2. **Rorty / moderate section (rewritten).** The old text asserted incorrigibility "forces" a dualist conclusion ("phenomenal states possess an epistemic property no physical state has"). The refine replaces this with an honest Mode-Two self-correction: an identity theorist can grant incorrigibility under a first-person mode while the neurological description stays revisable under another ("one referent under two modes of access"), so "treating incorrigibility as by itself forcing dualism would be an unsupported foundational move." The Map now presses the narrower explanatory demand instead of reading ontology off epistemology. This is the Map catching *its own* prior over-claim. Natural journal prose; **no editor-vocabulary leakage** ("unsupported foundational move" / "helps itself to a step it has not earned" are the sanctioned writing-style expressions, not the forbidden hyphenated labels). **CLEAN.**

3. **Heterophenomenology (recast).** Old: Dennett's neutrality "presupposes that no epistemically distinctive first-person access exists — the very question at issue" (a boundary-substitution / near-strawman). New: reads heterophenomenology at its strongest as a rival *policy* about what public inquiry may infer, "not a denial heterophenomenology need not make." Fairer Mode-Three engagement; removes the strawman the §2.6 discipline warns against. **CLEAN.**

4. **Bidirectional Interaction / Tenet 3 (recast).** Old: "Training-dependent improvement of introspective accuracy is *itself evidence for* bidirectional interaction." This was exactly the possibility/probability slippage the discipline exists to catch. New: training improvement is "*compatible with* bidirectional interaction... but it does not discriminate that reading from its rivals" (common-cause physical mechanisms predict the same result); it "removes a defeater... without thereby upgrading the dualist reading over its physicalist rival." **This is the single highest-value fix** — a defeater-removal is no longer mis-sold as evidence-elevation. **CLEAN.**

## Pessimistic Analysis Summary

### Critical Issues
- **None** (10th review; 9th consecutive no-critical body). All six adversarial personas engaged. The standing framework-boundary objections — illusionist/eliminativist theory-ladenness (located honestly at the constitutive-vs-referring bedrock), Dennett's functional-exhaustion, the Buddhist no-self residue — are declared honestly as bedrock and are **not** re-flagged per convergence discipline.

### Calibration check (possibility/probability slippage)
Diagnostic test applied (would a tenet-accepting reviewer still flag any claim as overstated?): **no**. The 07-21 refine tightened the two passages most exposed to slippage (Rorty epistemology→ontology; Tenet-3 training-as-evidence). Layered defeasibility intact (layer 1 "approaches incorrigibility"; layer 2 "strong but fallible"; layer 3 "may be no more reliable than third-person inference"). PC confined to "what experience presents"; irreducibility flagged as a separate metaphysical judgement. No epistemic→metaphysical slide; no tenet-as-evidence-upgrade. **PASS — and improved since last review.**

### Citation web-verify (§2.4)
**Not re-triggered.** The 07-21 refine changed zero inline `Author YYYY` cites and zero References entries (diff confirmed). The carried per-cite ledger from 2026-06-03 / 06-21 / 07-11 stands (Berghofer 2019/2023, Brewer 2011, Chalmers 2003, Carruthers 2011, Schwitzgebel 2008/2011, Petitmengin 2006, Fox et al. 2012, Rebouillat 2021 niab004, Husserl *Cartesian Meditations* §9 and Rorty title-phrase quotes — all real-correct / verbatim-confirmed at source of record). No superlative empirical claims (`find_superlative_claims` clean on prior passes; body-argument superlatives unchanged).

### Reasoning-mode classification (editor-internal)
- Eliminativism / theory-ladenness (constitutive-vs-referring): Mode Two → Mode Three (unchanged; honest).
- **Rorty / moderate: now cleanly Mode Two** ("unsupported foundational move" identified against the incorrigibility-forces-dualism inference) then framework-boundary residue marked — upgraded from the prior over-claim by the 07-21 refine.
- **Dennett / heterophenomenology: Mode Three** (policy-reading; upgraded from the prior "very question at issue" boundary-substitution) plus the narrowed self-stultification point at "adequately captures what experience is like" (Mode Two).
- Carruthers / inferentialism: Mode One (in-framework).
- No editor-vocabulary leakage in prose (grep clean).

## Optimistic Analysis Summary

### Strengths Preserved
- Husserl evidence-taxonomy → three-layer decomposition (unique synthesis).
- Gradient of Warranted Trust table.
- PC / irreducibility separation, now reinforced by the "cuts both ways" symmetry paragraph.
- Constitutive-vs-referring section locating the bedrock honestly.
- Calibration saturation — now *deepened* by the 07-21 convergent-outer-review refine.

### Enhancements Made
None this pass. The 07-21 refine already made the enhancements; this review's job was to verify them, which it did.

### Cross-links
Dense and current; no archival link rot introduced by the refine (it added no wikilinks). Prior spot-checks stand.

## Length Decomposition (dissolves the standing false-breach)

`analyze_length` reports **4441 words / `hard_warning`** — and this raw figure has been actively length-blocking the article: `/replenish-queue` run-811 (2026-07-25) explicitly rejected it as "phenomenal-authority... 4441w OVER hard = length-blocked." Decomposing per `[[analyze_length counts reference apparatus]]`:

| Segment | Words |
|---|---|
| **Argument prose** (lead → end of Objections/Relation-to-Site) | **3757** |
| Further Reading (20-item link list) | 195 |
| References (27 entries) | 490 |
| **Total** | **4442** |

The **argument prose is 3757 words — under the 4000 topics hard ceiling (94%)**. The 442-word "overage" is entirely the reference apparatus (a 27-item bibliography + a 20-item Further Reading list), which burdens neither reader nor LLM the way argument prose does. **This is not a genuine hard-ceiling breach**, and condensing the protected calibration prose to satisfy a refs-inflated raw count would be self-defeating (the trap documented in `[[human-decision-task-mispicked-as-refine]]`). No condensation applied; no calibration hedging touched.

The 07-21 refine grew argument prose ~+450 words (from ~3304 to 3757), so **~240 words of argument headroom remain** before even the decomposed argument-only basis reaches 4000. The next *required* argument addition exceeding that headroom (not a reference line, and not absorbable by a genuinely peripheral trim) becomes a human length decision — but the article is **not** there yet.

## Remaining Items

- **Standing length note updated (supersedes the 06-21/07-11 note):** on the decomposed argument basis the article is **under** the 4000 hard ceiling (3757w argument); the raw 4441 is reference-apparatus inflation. Future deep-review candidate selection / replenish length filters that key off the raw `analyze_length` total will keep false-flagging this article as over-ceiling — treat those as `[[analyze_length counts reference apparatus]]` false-highs, decompose, do NOT auto-condense the calibration prose. ~240 words argument headroom remain.
- Citations/quotes: carried ledger stands; re-verify only if the quoted text or a References entry changes.

## Stability Notes

Tenth review; body converged and, as of the 07-21 convergent-outer-review refine, **more calibrated than at any prior pass** (the two residual over-claims — Rorty incorrigibility→ontology and Tenet-3 training-as-evidence — are now corrected). Do NOT re-flag as critical: the illusionist/eliminativist theory-ladenness residue, the Dennett functional-exhaustion objection, or the Buddhist no-self objection — all bedrock framework-boundary disagreements the article locates and declares honestly. Do NOT add or remove calibration hedging. Do NOT auto-condense on the strength of the raw `analyze_length` total — decompose first; the argument prose is under ceiling. This pass made no body edits (no-op body): only `last_deep_review` advanced; `ai_modified` held at the 07-21 HEAD value.