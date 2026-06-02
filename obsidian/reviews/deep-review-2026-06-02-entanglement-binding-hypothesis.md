---
title: "Deep Review - The Entanglement Binding Hypothesis"
created: 2026-06-02
modified: 2026-06-02
human_modified: null
ai_modified: 2026-06-02T00:14:58+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-02
last_curated: null
---

**Date**: 2026-06-02
**Article**: [[entanglement-binding-hypothesis|The Entanglement Binding Hypothesis]]
**Previous review**: [[deep-review-2026-05-02-entanglement-binding-hypothesis|2026-05-02]]

This review was diff-scoped against the 2026-05-02 deep-review baseline commit (6137a684). The genuinely-new content since that review is: a new **Separability No-Go** section engaging Georgiev (2021); a rewritten decoherence paragraph adding Reimers et al. (2009) and McKemmish et al. (2009); a new Wiest-2025 sentence; and reconciled citation metadata for Escolà-Gascón (2025) and the Khan/Wiest epothilone paper. The audit focused on this new content, with live-literature web-verification of every load-bearing citation in it.

## Citation Web-Verification (publisher of record)

All five load-bearing citations in the new/changed content were verified against the live literature:

- **Escolà-Gascón (2025)** — VERIFIED. *Comput. Struct. Biotechnol. J.* **30**, 21-40, doi:10.1016/j.csbj.2025.03.001. The prior session's metadata reconciliation (from an earlier "26, 166-178" to "30, 21-40") is correct.
- **Georgiev (2021)** — VERIFIED. *Symmetry* **13**(5), 773, doi:10.3390/sym13050773. The article's paraphrase of the separability no-go is faithful (see below).
- **Khan et al. (2024)** — VERIFIED. Sana Khan first author, Mike Wiest corresponding; *eNeuro* **11**(8), ENEURO.0291-24.2024. The prior 2026-05-28 misattribution fix (Wiest→Khan as first author) is correct.
- **McKemmish et al. (2009)** — VERIFIED. *Phys. Rev. E* **80**(2), 021912. Central argument: tubulin does not undergo the rapid conformational switching the Orch-OR qubit picture requires.
- **Reimers et al. (2009)** — VERIFIED. *PNAS* **106**(11), 4219-4224 (ADS 2009PNAS..106.4219R). Central argument: coherent Fröhlich condensation is energetically inaccessible in biological tissue (Wu-Austin Hamiltonian has no finite ground state).

No fabricated references, page ranges, co-authors, or statistics found. Metadata is clean.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Mischaracterization of Reimers (2009) and McKemmish (2009) — dropped-qualifier / wrong-characterization defect (CRITICAL, fixed).** The new decoherence paragraph asserted that these papers "re-derived the recalibration and found the Hagan parameter assumptions **rest on** microtubule dielectric properties that are not empirically established." This is the degraded single-pronged form of a claim the rest of the corpus (decoherence.md, quantum-holism-and-phenomenal-unity.md, decoherence-and-macroscopic-superposition.md, mental-causation-and-downward-causation.md) carries correctly in two-pronged form ("**either** rely on dielectric properties not empirically established **or** specify regimes microtubules do not occupy in living tissue"). Web-verification of both source papers showed (a) neither paper "re-derives" Hagan's specific decoherence-time computation — the verb overstated the directness, and (b) the dielectric strand is only one prong and not the central result of either paper: Reimers argues energetic/Fröhlich impossibility, McKemmish argues tubulin conformational switching is irreversible. **Resolution**: rewrote the sentence to attribute each paper's actual argument distinctly (Reimers = energetic Fröhlich inaccessibility; McKemmish = no rapid tubulin conformational switching) and then state the two-pronged conclusion. This is now more accurate than even the sibling files' generic two-pronged hedge. Length-neutral (~+30 words; article 94% of soft, headroom available). The sibling files already carry the correct two-pronged framing and were left unchanged.

### Medium Issues Found

None. The Separability No-Go section is well-constructed and the Wiest-2025 sentence is appropriately hedged ("a stronger claim than this article endorses").

### Reasoning-Mode Classification (§2.6)

- **Engagement with Georgiev's separability no-go: Mode One, with honest Mode-Three residue.** The section states the no-go honestly ("The no-go is real") and answers it by locating binding in the interaction Hamiltonian rather than coherence — an answer **derived from Georgiev's own analysis** ("Georgiev's own analysis supplies the condition"), not from tenet-incompatibility. It closes with honest boundary-marking of the unresolved empirical question (whether biological tissue sustains the requisite coupling). No boundary-substitution; no editor-label leakage in prose. Exemplary; preserved unchanged.

### Counterarguments Considered

- All six pessimistic personas' standing objections (eliminativist rejection of phenomenal unity, MWI compatibility, decoherence-timescale gap) were marked bedrock disagreements in prior reviews and are not re-flagged. No new content reintroduces them.

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded BP1/BP2 distinction (opening paragraph).
- The structural non-separability argument — the article's distinctive philosophical contribution.
- The new **Separability No-Go** section — a high-value addition: it raises the sharpest available technical objection (sharper than decoherence) and answers it from the objector's own formalism, then honestly marks the residual empirical question. This is the calibration discipline working well: a constraint that "sharpens [the open question] rather than settling it."
- Evidential restraint throughout: experimental studies individually caveated; Wiest-2025's stronger framing explicitly declined.

### Enhancements Made

- Attribution-accurate rewrite of the Reimers/McKemmish characterization (see Critical Issues).

### Cross-links Added

None. Cross-link structure remains comprehensive.

## Remaining Items

None.

## Stability Notes

- **Reimers/McKemmish characterization**: now attributes each paper's actual argument and uses the corpus-canonical two-pronged conclusion. Future reviews should not re-flag unless a source-paper re-reading contradicts the energetic-Fröhlich / conformational-switching split.
- **Separability No-Go section**: faithful Mode-One engagement with Georgiev (2021), web-verified. Bedrock-stable; do not re-flag.
- Prior stability notes (eliminativist rejection, MWI compatibility, decoherence-timescale gap, "seven orders of magnitude" phrasing, Baum's zero-lag argument) carry forward unchanged.

The article remains stable. The 2026-06-01 refine pass added genuinely valuable content (the Georgiev no-go), and this review corrected the one calibration/attribution defect that pass introduced in the adjacent decoherence paragraph.
