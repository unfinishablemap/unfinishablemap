---
title: "Deep Review - Sorkin-Δ Brain-Internal Analogues"
created: 2026-09-25
modified: 2026-09-25
human_modified: null
ai_modified: 2026-09-25T23:49:03+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-09-25
last_curated: null
---

**Date**: 2026-09-25
**Article**: [[sorkin-delta-brain-internal-analogues|Sorkin-Δ Brain-Internal Analogues]]
**Previous review**: [[deep-review-2026-07-19-sorkin-delta-brain-internal-analogues|2026-07-19]] (also 2026-07-08, 2026-06-03)

## Selection and delta

Fourth deep review. The delta since 2026-07-19 is substantive: refine-draft commit `d9c7e6b025` (2026-09-25 16:48) rewrote the Stapp paragraph, the probability-bias paragraph (δ vs ε), the "pattern" summary and the second Relation-to-Site paragraph. The fix established that literal Zeno is standard QM and leaves ε = 0. This review checked the rewritten prose and the claims that sit next to it. The earlier reviews' stability notes cover the unchanged framing and do not cover the new physics.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Orch-OR third-order residue: incorrect scientific claim, same shape as the Zeno error.** The article said "The Born rule does not hold at the OR event, so an Orch-OR brain genuinely could carry a non-zero third-order residue," and that a brain Δ-analogue "at threshold precision would constrain" the Diósi-Penrose parameter space. The formal Diósi-Penrose model, like every consistent Markovian collapse model, evolves the density matrix by a *linear* master equation (needed for no-signalling). A density-matrix state links at most two paths coherently (Dakić, Paterek & Brukner 2014, "Density cubes and higher-order interference theories", *NJP* 16:023028), so ensemble probabilities stay quadratic and I₃ = 0. Unitarity-breaking is not quadratic-form-breaking. The collapse signature is second-order visibility loss, which is what MAQRO tests. Only Penrose's unformalised "non-computable selection" claim could depart from Born statistics. **Fixed**: the paragraph is rewritten on that basis. The "pattern" paragraph now says the Δ-analogue is silent against the formal DP dynamics too. The Relation-to-Site paragraph now narrows what the design space can adjudicate to non-quadratic bias channels plus Orch-OR's selection element if it is ever specified. The refine-draft's own "Orch-OR remains the adjudicable reading" framing had spread this error into two more paragraphs.
2. **Source/Map conflation (attribution).** "The seventh falsifier Stapp's model already lists" credited the falsifier list to Stapp. The list is the Map's (`concepts/stapp-quantum-mind` L180, "prediction 7"). **Fixed**: now "the seventh falsifier the Map's [[stapp-quantum-mind]] entry lists for Stapp's model".

### Citation ledger (§2.4)

The References block is byte-identical to the one fully verified at the publisher of record on 2026-07-08, and this delta adds no new citations. Carried forward:
- Sinha et al. 2010 (*Science* 329:418): real-correct (07-08)
- Sorkin 1994 (*MPLA* 9:3119): real-correct (07-08)
- Tegmark 2000 (*PRE* 61:4194): real-correct (07-08)
- Hagan, Hameroff & Tuszyński 2002 (*PRE* 65:061901): real-correct (07-08)
- Wiest 2025 (*NoC* niaf011): real-correct (07-08)
- Kerskens & López Pérez 2022 (*J Phys Commun* 6:105001): real-correct (07-08)
- Escolà-Gascón 2025 (*CSBJ* 30:21): real-correct (07-08)
- Donadi et al. 2021 (*Nat Phys* 17:74): real-correct (07-08). Result direction was re-checked this pass: it excludes the parameter-free DP model through spontaneous radiation (heating), not through any Born-rule violation. The rewritten paragraph now says this correctly.
- Gildert 2025: real-correct (07-08)
- New physics claim checked this pass: collapse models have linear density-matrix dynamics, and higher-order interference is absent for density-matrix states. Confirmed by web search (Dakić et al. 2014; Bassi collapse-model reviews). Stated in prose without a new References entry, as standard background.
- The superlative-claims helper found nothing.

### Medium / Low
- The RNG δ ≈ 10⁻⁴ ceiling has no inline cite. It was unchanged across the prior reviews. Deferred as low.

### Reasoning-mode (§2.6)
The Stapp, Orch-OR and bias-channel treatments are expository mechanism analyses, not replies to opponents. There is no boundary-substitution and no leaked editor-vocabulary labels.

## Optimistic Analysis Summary

### Strengths Preserved
- The three-feature decomposition of why the optical protocol fails to translate to the brain.
- The Relation-to-Site passage that openly owns the corridor's structural silence. It is now *stronger*: the article concedes that the Δ-analogue is silent against almost every articulated mechanism, not just the corridor.
- The refine-draft's δ/ε disambiguation and its pointer to the rate-response discriminator.

### Enhancements Made
- Orch-OR paragraph rewritten; pattern and RSP paragraphs realigned; Stapp falsifier attribution fixed.

## Length
2443 → 2532 words (topics soft 3000). Status ok.

## Remaining Items
- The same error sits in the companion `topics/brain-internal-born-rule-testing` at L102 ("The Born rule does not hold at the OR event"). That host is about 3 words below its hard limit. A P2 refine-draft task has been added to todo.md. A sweep of `Born rule does not hold` found no other locus.

## Stability Notes
- The Δ-analogue's silence against the corridor, literal Zeno and the formal DP dynamics is now the article's settled physics. Do not re-install "informative against Orch-OR at threshold precision" unless Penrose's selection element is given a quantitative non-quadratic form in the literature.
- Earlier stability notes still hold: the corridor's silence is owned, the coherence dispute is left open, and the article is conditional on Tenet 4.
