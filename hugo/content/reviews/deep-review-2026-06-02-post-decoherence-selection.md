---
ai_contribution: 100
ai_generated_date: 2026-06-02
ai_modified: 2026-06-02 22:56:49+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-02
date: &id001 2026-06-02
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Post-Decoherence Selection
topics: []
---

**Date**: 2026-06-02
**Article**: [Post-Decoherence Selection](/concepts/post-decoherence-selection/)
**Previous review**: [2026-05-17](/reviews/deep-review-2026-05-17-post-decoherence-selection/) (first full single-doc); [2026-03-29](/reviews/deep-review-2026-03-29-post-decoherence-selection/) (first-pass)

This pass was citation/quote web-verification focused: post-decoherence selection is a quantum-interpretations-dense concept (high fabrication risk), and the own-content change since the last deep review was the candour-gap refine (unfalsifiable-default, MWI boundary-marking, preprint-overclaim). Every reference and body-cited author was verified at the publisher of record.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Fabricated/misquoted Schlosshauer (2004) direct quote** (body opening, was line 43). The article attributed a verbatim direct quote to Schlosshauer's 2004 *Reviews of Modern Physics* review: *"After the basis is chosen and quantum superpositions are suppressed, the system still remains in a mixture of possible outcomes. Decoherence does not tell how and why only one of these outcomes is measured."* Web-verification against the canonical decoherence review (arXiv:quant-ph/0312059, the published Rev Mod Phys 76(4):1267) found this **exact wording does not appear in the paper**. The paper's actual relevant wording is different: *"Does decoherence solve the measurement problem? Clearly not. … At some stage, we still have to apply the usual probability rules of quantum theory"* and *"Decoherence by itself does not yet solve the measurement problem."* The sentiment is correct and genuinely Schlosshauer's — decoherence does not solve the problem of outcomes — but the words in quotation marks are not his (the phrasing tracks SEP-style paraphrase, and the SEP qm-decoherence entry was checked and does **not** contain the sentence either; the earlier search-model "attributed to SEP" claim was confabulation). **Resolution**: per skill instruction, converted to an accurate quote-mark-free paraphrase that tracks the paper's actual claim — *"As Schlosshauer (2004) is explicit, decoherence does not solve the measurement problem: once the preferred basis is selected and interference suppressed, the system is still described by a mixture, and the usual probability rules of quantum theory must still be applied to extract a single observed outcome."* No replacement quote confabulated. This is the canonical fabricated-verbatim-quote pattern (quote plausible, sentiment right, words not in source); both prior reviews asserted the quote was "verbatim and properly cited" without having web-verified it.

- **Orphaned recent-specialist citation now grounded** (MQI tenet paragraph). Torres Alegre (2025) was cited in the body but absent from the References list (refs 1–12) — the exact orphaned-reference + recent-specialist pattern that is high fabrication risk. **Web-verification: the work is REAL.** Enso O. Torres Alegre, "Causal Consistency Selects the Born Rule: A Derivation from Steering in Generalized Probabilistic Theories," arXiv:2512.12636 (Dec 2025). The paper proves the only no-signalling-consistent map between geometric transition probability and predictive probability is the identity Φ(p)=p; nonlinear deviations generate superluminal signalling; steering enforces the Born rule as the unique causally-consistent assignment. The body's attribution is faithful. **Resolution**: (a) added as reference 13 with correct title/arXiv ID; (b) tightened the body gloss from "argues any participant in measurement outcomes must respect [relativistic causality]" to track the paper's actual derivation (Born rule as unique no-signalling-consistent assignment, deviations generating detectable superluminal channels). No softening/removal needed — the cite verified clean.

### Medium Issues Found

None. The candour-gap fixes from the prior refine held (see Calibration check below). No new medium issues.

### Counterarguments Considered

All carried forward from the 2026-05-17 / 2026-03-29 stability notes and still valid (Churchland, Dennett, Tegmark, Deutsch, Popper, Nagarjuna — all bedrock-at-framework-boundary or already-addressed). Not re-flagged.

### Calibration Test (Possibility/Probability Slippage) — candour-gap-held check

Diagnostic test applied (would a tenet-accepting reviewer still flag any claim as overstated?). Specifically re-checked the three candour-gap items the prior refine addressed:

- **Unfalsifiability candour**: "Post-decoherence models operate at the interpretive level … where empirical access is indirect at best" + "The epistemological cost is equally significant: post-decoherence selection is harder to falsify." HELD — no unfalsifiability dodge; the cost is named squarely.
- **MWI boundary-marking**: MWI is "explicitly ruled out by the No Many Worlds tenet" and the rejection is "presented as a framework commitment, not a refutation of MWI on its own terms." HELD — tenet-ruling, not neutral-ground refutation.
- **Preprint-overclaim**: Colanero (2012) and Bhaumik (2023) are arXiv preprints used as supplementary/discussion sources; the canonical improper/proper mixture point rests on d'Espagnat (1976). No preprint treated as established. HELD.
- The comparative claims ("satisfies MQI more cleanly than any competing framework"; "only consciousness-mediated selection is compatible with all five tenets") remain *comparative tenet-coherence / logical-compatibility* claims, not evidence-elevation claims — engaged on each family's own terms with framework-boundary marking. No epistemic→metaphysical slide.

No slippage detected.

### Engagement-Mode Classification (Editor-Internal)

Unchanged from 2026-05-17 (no engagement prose was rewritten this pass):

- Stapp's quantum Zeno / Penrose-Hameroff Orch OR: **Mode Three** (framework-boundary marking) — presented accurately, post-decoherence variant offered as alternative sidestepping timing-gap, no refutation claimed inside Stapp's framework.
- Tegmark's decoherence-timescale objection: **Mode One** (defective on its own terms when applied to the post-decoherence variant) — the calculation is not refuted; it is argued to presuppose pre-decoherence coherence, missing the post-decoherence target.
- Objective collapse (GRW, Penrose-Diósi, CSL): **Mode Two** (unsupported foundational move) — "ad hoc parameters … chosen to match observation rather than derived from first principles" invokes a parsimony/first-principles standard physics itself endorses.
- Consistent histories (Griffiths/Gell-Mann/Hartle): **Mode Two** — the set-selection problem identified as a framework-internal gap.
- Bohmian determinism (Dürr/Goldstein/Zanghì) and Many Worlds (Everett): **Mode Three** (framework-boundary marking).

No label leakage. Verified no forbidden editor-vocabulary tokens in article prose.

### Citation Web-Verification Verdicts

- **Schlosshauer (2004)** Rev Mod Phys 76(4):1267 — reference metadata CORRECT; **verbatim quote FABRICATED/MISQUOTED** → fixed (paraphrase, no quote marks). See Critical above.
- **Torres Alegre (2025)** arXiv:2512.12636 — REAL, attribution faithful; was ORPHANED → added to refs as #13, body gloss tightened. See Critical above.
- **Ghirardi, Rimini & Weber (1986)** "Unified dynamics…" Phys. Rev. D 34(2):470 — VERIFIED clean (vol 34, pp. 470–491, July 1986).
- **Colanero (2012)** arXiv:1208.0904 "Decoherence and definite outcomes" — VERIFIED (correct author/title, ID resolves).
- **Bhaumik (2023)** arXiv:2301.01207 "Can Decoherence Solve the Measurement Problem?" — VERIFIED (Mani L. Bhaumik; ID resolves; title exact).
- **Dürr, Goldstein & Zanghì "Result Assumption"** (Bohmian) — STANCE check: standard, accurate characterization of the Bohmian position (positions guide branch selection; no selection event); presented as framework-boundary bedrock, not as Map endorsement. Clean.
- **Griffiths / Gell-Mann / Hartle** ("architects explicitly deny this interpretation," consistent histories set-selection) — STANCE check: accurate; the architects do not read the set-selection problem as a consciousness opening. Clean.
- **Von Neumann (1932)** *Mathematical Foundations* — canonical, metadata correct.
- **Tegmark (2000)** PRE 61(4):4194 — metadata correct (confirmed clean elsewhere this session).
- **Stapp (1993)** *Mind, Matter, and Quantum Mechanics*, Springer — 1st-ed 1993 is CORRECT (editions 1993/2004/2009); consistent.
- **d'Espagnat (1976)**, **Kastner (2012)** CUP — canonical, metadata correct.

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded opening (concept + gap + Map positioning, truncation-resilient) — preserved through the quote fix; the paraphrase keeps Schlosshauer grounding the residual-gap claim.
- Improper/proper mixture distinction with d'Espagnat + Colanero — the article's strongest, well-supported philosophical move.
- Five-families taxonomy — stable cluster template; untouched.
- Honest pre/post-decoherence falsifiability trade-off — calibration exemplar; held.
- Causal-consistency-constraint / Torres Alegre integration — now properly grounded with the cite in the reference list; the cluster's bridge to the formal no-signalling literature is intact and stronger.
- Full five-tenet comparative engagement deriving (not asserting) why only consciousness-mediated selection satisfies all five.

### Enhancements Made

- Schlosshauer attribution corrected to faithful paraphrase (removes a fabricated-quote credibility liability).
- Torres Alegre (2025) added to References (#13); orphaned cite resolved; body gloss tightened to the paper's actual derivation.

### Cross-links Added

None (the cluster is already fully bidirectionally linked at all three levels; no new links warranted).

## Remaining Items

- **Out-of-scope cluster issue (carried from 2026-05-17, re-confirm)**: the fabricated "Luppi & Adlam, 2012" citation reportedly still appears in [forward-in-time-conscious-selection](/topics/forward-in-time-conscious-selection/). Out of scope for this single-file review; a `refine-draft`/deep-review of that topic article should fix it.
- No deferred items for this article.

## Stability Notes

All prior stability notes (2026-03-29, 2026-05-17) carried forward and still valid: the Quantum Skeptic mechanism objection, MWI's rejection-of-premise, and the pre/post falsifiability asymmetry are bedrock / inherent-to-the-proposal and candidly handled — future reviews must NOT re-flag as critical. The article is the mid-tier of the three-level cluster (apex → concept → topic); preserve the division of labour. The causal-consistency-constraint integration is load-bearing and must not be unwound. The five-families framing is a stable cross-cluster template.

**New (2026-06-02)**: The Schlosshauer opening is now a *paraphrase*, not a direct quote. Future reviews must NOT "restore" a verbatim quote here — the specific words previously quote-marked are not in Schlosshauer (2004). If a verbatim quote is ever wanted, it must be drawn fresh from the paper and checked, not reconstructed from the prior (fabricated) wording. This is the convergence-protection note for this pass: the prior two reviews both certified the quote as "verbatim" without web-verifying it, so the corrective signal only arrived once a citation-web-verify pass was run. Torres Alegre (2025) = arXiv:2512.12636 (Born-rule-from-no-signalling), now in refs; future reviews should treat it as verified, not re-flag as orphaned.