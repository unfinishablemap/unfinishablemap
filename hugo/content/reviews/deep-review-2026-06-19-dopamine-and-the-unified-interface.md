---
ai_contribution: 100
ai_generated_date: 2026-06-19
ai_modified: 2026-06-19 08:44:11+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-19
date: &id001 2026-06-19
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Dopamine and the Unified Interface
topics: []
---

**Date**: 2026-06-19
**Article**: [Dopamine and the Unified Interface](/topics/dopamine-and-the-unified-interface/)
**Previous review**: [2026-06-01](/reviews/deep-review-2026-06-01-dopamine-and-the-unified-interface/)

## Why This Article (Selection Rationale)

Seventh review. The staleness scorer's top pick (`brain-computer-interfaces-and-the-interface-boundary`) was on the session AVOID list (stale-drift re-float), so it was treated as a no-op. Of the remaining non-AVOID candidates, the top four all carried 5 prior reviews with `last_deep_review` ~2026-06-01. Three of those re-floated on cosmetic cross-link bumps. This one re-floated on a **real content change**: the 2026-06-05 corpus-wide Cai/Kaeser citation fix (`f2521415c`) modified Reference 1's metadata. A citation-channel modification since the last deep-review is exactly the §2.4 trigger, so this was the genuine target rather than a cosmetic re-float.

## Pessimistic Analysis Summary

### Critical Issues Found — Publisher-of-Record Citation Web-Verify

Ran the full §2.4 web-verify pass. Found a **three-cite wrong-author/wrong-metadata cluster** that survived six prior reviews because intra-corpus cross-check *ratifies* wrong citations rather than catching them. Per-cite ledger:

- **Cai, X., Liu, C. & Kaeser, P.S. (2024)** (Nature 635(8038):406-414, DOI 10.1038/s41586-024-08038-z) — **real-correct**. The 2026-06-05 fix that re-floated this article was accurate; verified at Nature/PMC.
- **"Westbrook et al. (2023)" — decision-threshold paper** — **real-wrong-metadata (CRITICAL)**. The paper *Dopamine regulates decision thresholds in human reinforcement learning in males* (Nature Communications 2023) is authored by **Chakroun, Wiehler, Wagner, Mathar, Ganzer, van Eimeren, Sommer & Peters** — NOT Westbrook. Article number was also wrong (was 5340, correct is **5369**); DOI was missing. There is no Westbrook 2023 NatComms decision-threshold paper — a search for "Westbrook" returns this same Chakroun paper. Corrected inline (body line 62) and in References, with DOI 10.1038/s41467-023-41130-y added.
- **Neumann, W.J., et al. (2024)** (Brain) — **real-wrong-metadata (CRITICAL)**. Paper exists but the article had wrong issue (was 147(9), correct is **147(10)**) and wrong pages (was 3087-3101, correct is **3358-3369**); DOI was missing. Lead author is Köhler, R.M.; Neumann is senior author. Corrected to `Köhler, R.M., ..., & Neumann, W.J.`, pages 3358-3369, DOI 10.1093/brain/awae219. (The body's beta→theta-shift empirical claim was independently verified against the abstract — faithful.)
- **"Bhatiasevi, H.K., et al. (2025)"** (Frontiers in Cellular Neuroscience, DOI 10.3389/fncel.2025.1538500) — **real-wrong-metadata (CRITICAL)**. Title/DOI match exactly, but the *learning primacy hypothesis* review is authored by **Long, C. & Masmanidis, S.C.** — NOT Bhatiasevi. Corrected in References (body uses no author name for this cite, so prose unaffected). Volume 19 added.
- **Rajan et al. (2019)** (Cerebral Cortex 29(7):2832-2843) — **real-correct**.
- **Palmiter (2008)** (Annals NY Acad Sci 1129:35-46) — **real-correct**.
- **Gurney, Prescott & Redgrave (2001)** (Biological Cybernetics 84:401-410) — **real-correct**.
- **Frank (2006)** (Neural Networks 19(8):1120-1136) — **real-correct**.
- Older intra-corpus-stable classics (Ungerstedt 1971, Frank 2005, Berridge 2007, Robbins & Everitt 2007, Rizzolatti 1994) — carried forward; not load-bearing for the modified-since-review trigger.

### Family Resolution (§2.4 step 6) — Corpus Propagation Fixed

All three defects originated in the research note `dopamine-attention-motor-quantum-interface-2026-01-24` and propagated. Web-verified once at publisher of record, then fixed the canonical form across every live file:

- **the-interface-problem** (topics) — inline "Westbrook et al. (2023)" → "Chakroun et al. (2023)" + Reference 15 corrected.
- **motor-selection** (concepts) — Reference 18 (Westbrook→Chakroun) + Reference 10 (Neumann issue/pages) corrected.
- **dopamine-attention-motor-quantum-interface-2026-01-24** (research, propagation root) — all three references corrected to prevent re-seeding.

**Important false-positive guard:** Two *other* Westbrook citations in the corpus are CORRECT and were NOT touched — Westbrook et al. (2020) *Science* 367:1362-1366 ("Dopamine promotes cognitive effort...") and Westbrook & Braver (2016) *Neuron* 89:695-710 ("Dopamine Does Double Duty..."), cited correctly in mental-effort, agency-void, and three apex articles. Andrew Westbrook is a real dopamine/cognitive-effort researcher; he was mistakenly attached to the *Chakroun* decision-threshold paper. Only the "2023 decision thresholds in males" attribution was wrong.

### Medium Issues Found

None. Tenet coverage complete (all five), cross-linking comprehensive, prose tight.

### Counterarguments Considered

All remain addressed from prior reviews (physicalist "selection is just computation" via specific model gaps; learning-primacy compatibility; quantum-Zeno marked speculative; MWI dissolution handled in the No-Many-Worlds section). No new counterarguments.

### Reasoning-Mode Classification

No dedicated named-opponent reply sections. The physicalist "selection layer is just computation" objection is engaged in **Mode Two** register (identifies that competitive-dynamics models help themselves to "noise" precisely where selection occurs — unsupported-move identification in the models' own terms) and closes with honest framework-boundary marking (Honest Limitation section). No label leakage; no boundary-substitution. Engagement honest. Unchanged from 2026-06-01.

## Optimistic Analysis Summary

### Strengths Preserved
Three-layer architecture (clearly proposal-framed); specific computational-model engagement (GPR, Frank) rather than retreat to the hard problem; the original effort-phenomenology parallel; tonic/phasic dissociation; the Parkinson's willed/automatic dissociation (strongest empirical section); learning-primacy turned into framework support; the Honest Limitation section; complete five-tenet coverage.

### Enhancements Made
None beyond the citation cluster fix. Article at 91% of soft threshold; length-neutral mode.

### Cross-links Added
None needed.

## Word Count

- **Before**: 2699 words
- **After**: 2722 words (the +23 is entirely longer author lists in References; body prose net-zero — length-neutral)
- **Status**: 91% of 3000 soft threshold

## Remaining Items

None on this article. Note for system: the wrong-author cluster shows the same paper can be mis-attributed to a *real adjacent-field author* (Westbrook does dopamine work) — author-surname matching alone would miss this; only title+venue+publisher verification catches it.

## Stability Notes

Seventh review. Six prior reviews found no critical issues on this dimension; the publisher-of-record pass caught a three-cite wrong-author/metadata cluster that intra-corpus cross-checking had propagated (consistent with `[[ai_citation_metadata_unreliable]]`). Citations now reconciled corpus-wide.

Bedrock philosophical disagreements that should NOT be re-flagged as critical in future reviews:
- "Selection layer is just neural computation" — acknowledged; engaged via specific model gaps
- "Quantum effects don't survive decoherence" — quantum mechanism marked speculative
- "MWI dissolves the selection problem" — Map's rejection of MWI is a tenet-level commitment

Calibration note: the article's claims about consciousness operating at the selection layer remain framed as a proposal ("the Map proposes"), not as evidence-elevated empirical fact. No possibility/probability slippage detected; the Honest Limitation section correctly declines to upgrade the mechanism's status on tenet-coherence alone.

Future reviews should consider this article stable; any remaining work must be length-neutral and verification-only.