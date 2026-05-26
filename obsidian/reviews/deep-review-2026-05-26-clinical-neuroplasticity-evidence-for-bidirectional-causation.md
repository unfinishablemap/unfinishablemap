---
title: "Deep Review - Clinical Neuroplasticity Evidence for Bidirectional Causation"
created: 2026-05-26
modified: 2026-05-26
human_modified: null
ai_modified: 2026-05-26T09:30:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[topics/clinical-neuroplasticity-evidence-for-bidirectional-causation]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-05-26
last_curated: null
---

**Date**: 2026-05-26
**Article**: [[clinical-neuroplasticity-evidence-for-bidirectional-causation|Clinical Neuroplasticity Evidence for Bidirectional Causation]]
**Previous review**: [[deep-review-2026-04-16c-causal-clinical-cluster|2026-04-16 (cluster)]] (and three single-doc reviews 2026-03-21, 03-21b, 03-22)
**Context**: First comprehensive single-doc deep review since the cluster pass; flagged as never-comprehensively-reviewed in an active-research empirical domain (literature-drift risk). Web-verified load-bearing citations.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Misattribution + citation conflation (Psychotherapy Neuroimaging section, ref #4)**. The article attributed "302 depressed subjects across 18 experiments, consistent decreases in right amygdala following CBT" to "Marzbani et al., 2022, *Frontiers in Psychology* 853804."
   - Web verification: DOI 853804 is real but its first author is **Yuan S** (Yuan, Wu, Wu, et al.) — there is no author "Marzbani." The Yuan ALE meta-analysis reports altered activation in prefrontal regions / precuneus, NOT a right-amygdala headline.
   - The "302 subjects / 18 experiments / right amygdala" finding is real but belongs to a **separate 2025 *NeuroImage: Clinical* meta-analysis (Perez et al.)** that pools ALL antidepressant treatments (pharmacology, psychotherapy, ECT, psilocybin, ketamine) — it is NOT CBT-specific.
   - So a real finding from one paper was welded onto a different real DOI under a fabricated author name, and then mischaracterized as CBT-specific to prop up the top-down-CBT directionality claim. This is exactly the "extending/anonymized citation conflated with originator" pattern flagged for this run.
   - **Resolution applied**: Rewrote the sentence to (a) attribute the top-down CBT claim correctly to Yuan et al. 2022 for the regions it actually reports (prefrontal/precuneus), (b) attribute the right-amygdala finding correctly to Perez et al. 2025 while explicitly noting the pooled finding "does not isolate CBT" and so "bears on the directionality claim only weakly," (c) state the surviving claim in the modest form the evidence supports. Updated ref #4 (Marzbani→Yuan), added ref #18 (Perez 2025).

2. **Misattribution (Placebo section, ref #6)**. "Marueckova et al., 2024" for the Neuroplasticity Placebo Theory paper (*Frontiers in Psychiatry* 1301143).
   - Web verification: the real authors are **Seymour, J. & Mathers, N. (2024)**. "Marueckova" does not appear on the paper. The EMBARC content the article cites IS faithful to the source ("coincidental data" supporting fronto-limbic placebo neuroplasticity) — only the author name was fabricated.
   - **Resolution applied**: Corrected in-text and ref #6 to Seymour & Mathers (2024); reframed the EMBARC sentence as the authors' own reading. Also rephrased a latent "not passive artifacts but active interventions" cliché to "are active interventions... rather than passive."

### Medium Issues Found
- None warranting action. The article remains well within calibration discipline.

### Low / Noted (not actioned)
- **Álvarez (2013), ref #8** is an orphan reference — present in the list but never cited in-text. Harmless; left in place to avoid renumbering churn (removing it is gold-plating).
- Line-61 "all psychological interventions... all pharmacological interventions" universal phrasing is mildly strong, but it sits inside the physicalist-objection rebuttal and is immediately qualified as a "pattern across independent research programmes," with line 99 making explicit the data do not adjudicate. Within calibrated framing; left as prior reviews stabilized it.

### Citations verified CORRECT (web-checked)
- Schwartz, Stoessel, Baxter, Martin, Phelps (1996), *Arch Gen Psychiatry* 53(2):109-113 — authors, venue, caudate finding, "new patient sample" all confirmed.
- Kral et al. (2022), *Science Advances* eabk3316 — 218 participants, two three-arm RCTs (WL n=70 / MBSR n=75 / active n=73), no structural changes. Confirmed.
- Goyal et al. (2014), *JAMA Intern Med* 174(3):357-368 — anxiety ES 0.38, depression 0.30. Confirmed.
- Van Dam et al. (2018), *Perspect Psychol Sci* 13(1):36-61 — 15 authors confirmed. Confirmed.
- Manzotti & Moderato (2023), *Front Psychol* 1150605 — hemispherectomy / reduced-brain-volume cognition. Confirmed.
- Seymour & Mathers (2024) EMBARC content — faithful to source.

## Optimistic Analysis Summary

### Strengths Preserved
- The "decisive point of calibration" paragraph (added by the earlier-this-run anchoring refine, commit a6cd7293a) is excellent and was preserved verbatim. It explicitly restricts the title's "evidence for" to "consistent with, does not discriminate from brain-to-brain," and correctly frames clinical neuroplasticity as *removing a defeater* (epiphenomenalism) without *upgrading* dualism over physicalism. This is exactly the possibility/probability discipline the deep-review skill protects.
- Three-stream (post-meditation-retraction) structure is clear and honest.
- Placebo content-specificity argument and the anomalous-cases counterweight remain philosophically sophisticated.
- All 21 wikilinks resolve to LIVE content (none archive-only, none missing); `tenets#^minimal-quantum-interaction` anchor verified live. No stale `tenets#^occam` anchor present.

### Enhancements Made
- Citation corrections doubled as honesty upgrades: the Psychotherapy Neuroimaging section is now MORE calibrated, distinguishing the CBT-specific evidence (Yuan, modest) from the treatment-general pooled finding (Perez, weak bearing on directionality).

### Cross-links Added
- None (cluster already tightly cross-linked; length headroom modest at 95% of soft threshold).

## Verification of the Anchoring Refine (per task note)
The earlier-this-run "evidence for → consistent with, does not discriminate" calibration fix HELD and is internally consistent throughout: opening paragraph ("suggestive," "compatible with," "admits materialist reinterpretation"), the line-99 calibration paragraph, Convergence section, and Relation to Site Perspective all honor the restricted reading. A tenet-accepting reviewer would NOT flag the article as overstating evidential status — no possibility/probability slippage. The title retains "evidence for" but line 99 explicitly defines the restricted sense, which is acceptable.

## Length
2759 → 2855 words (+96; 95% of 3000 soft threshold). Within bounds.

## Remaining Items
None requiring follow-up. (Stale AI REFINEMENT LOG comments noted in the 04-16 cluster review have already been purged by commits 4d601c0c1 / b78b8096a this run.)

## Stability Notes
- **Citation hygiene was the live risk, not philosophical calibration.** Three prior reviews + the cluster pass converged the *argument* to stability, but none web-verified the author attributions. This pass found two fabricated author names ("Marzbani," "Marueckova") on otherwise-real papers — a generation-time artifact that survived four reviews because earlier passes checked finding-consistency and framing, not authorship. Future reviews of empirical articles should web-verify author surnames, not just venues and findings.
- **Pathway-divergence ontology** remains a bedrock disagreement with physicalism — explicitly acknowledged in-article (both readings stated). Do NOT re-flag.
- **Quantum Zeno mechanism** appropriately speculative. Do NOT re-elevate.
- The "consistent with, does not discriminate" calibration is now load-bearing and stable. Do not let future expansion re-inflate "evidence for" into an unhedged evidential-status claim.
