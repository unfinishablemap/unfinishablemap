---
ai_contribution: 100
ai_generated_date: 2026-05-28
ai_modified: 2026-05-28 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-05-28
date: &id001 2026-05-28
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Interface Friction
topics: []
---

**Date**: 2026-05-28
**Article**: [Interface Friction](/concepts/interface-friction/)
**Previous review**: [2026-04-17](/reviews/deep-review-2026-04-17-interface-friction/) (5th deep review overall; prior passes 2026-02-20, 2026-03-19, 2026-04-16, 2026-04-17)

## Context

Staleness-triggered deep review (41 days). The article is the canonical mechanism page for interface-friction costs (selection effort, bandwidth, precision loss). Standing-guidance task: run a CITATION-CURRENCY pass alongside the normal convergence/calibration/reasoning-mode checks — live web-verify every external citation against primary sources, and re-derive internal quantitative claims. The article was already converged (the 2026-04-17 pass found no critical issues, one minor enumeration fix). This pass targeted citation currency and internal arithmetic, where prior convergence reviews had not looked.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Internal arithmetic over-derivation in the decoherence gap (CRITICAL — calibration/arithmetic).** The Decoherence Pressure section stated decoherence "10⁻¹³ seconds … while neural decision windows span hundreds of milliseconds. This thirteen-order-of-magnitude gap…". Re-derived from the article's own figures: 10⁻¹ s (hundreds of ms) / 10⁻¹³ s = 10¹² = **twelve** orders of magnitude, not thirteen. The corpus has explicitly litigated this exact pairing (changelog 2026-XX: "twelve orders" between 10⁻¹³ and 10⁻³ corrected to ten; the twelve-to-sixteen figure is correct only when paired with Tegmark's 10⁻¹ s attentional bound). Sibling articles mental-effort.md and temporal-consciousness.md both state "twelve orders of magnitude" for the femtosecond-vs-millisecond gap; this article's "thirteen" was an outlier that over-derived by one order and survived four prior deep reviews. **Resolution**: changed "thirteen-order-of-magnitude gap" → "twelve-order-of-magnitude gap" and added the explicit "(~10⁻¹ s)" anchor so the derivation is self-checking in the prose.

- **Citation year-label drift, Zheng & Meister (CRITICAL — citation metadata; detection tell i).** Body text said "Zheng and Meister (2024)" and the reference read "Zheng, J. & Meister, M. (2024). … *Neuron*, 113(2), 192–204." Web-verified against primary source: bound issue is *Neuron* **113(2), 192–204, published 22 January 2025** (online-first 17 Dec 2024; DOI 10.1016/j.neuron.2024.11.008). The corpus-dominant corrected form is **2025** (bandwidth-of-consciousness.md and the-interface-problem.md/temporal-consciousness.md were fixed to 2025 in prior sessions). This article still carried the drifted 2024 year-label in both body and reference. **Resolution**: changed both inline citation and reference to (2025); volume/issue/pages were already correct.

### Medium Issues Found

- **Reciprocity gap (deferred to follow-on).** interface-friction prominently forward-links attentional-economics, mental-effort, and filter-theory in both body and frontmatter, but none of the three links back. Forward links all resolve (not build-breaking; content-quality only). Adding backlinks to three sibling articles is out of scope for an in-place length-neutral deep-review pass; queued as a P3 integrate-orphan/repoint follow-on.

### Counterarguments Considered

- All six adversarial personas re-engaged. No new counterarguments beyond those catalogued across four prior reviews. Eliminative Materialist / Hard-Nosed Physicalist objections are explicitly granted in-text (physicalist re-description adequacy conceded in "Friction and the Filter Model" and "What Resists"); Quantum Skeptic's decoherence objection is the load-bearing content of the section just corrected (and is presented as "the strongest quantitative objection," not dodged); MWI / Popperian / Buddhist objections remain bedrock framework-boundary disagreements, not correctable defects.

### Attribution / Source-Separation Check

- Original Map concept, not a single-source exposition — no misattribution surface. Map-specific arguments (tenets, quantum Zeno, post-decoherence selection lineage) are clearly labelled as the Map's reading throughout ("on the Map's reading," "on the dualist account," "the filter framework offers a different level of explanation"). No source/Map conflation.

### Reasoning-Mode Classification (§2.6)

- The article does not reply to a named opponent in an extended refutation. The physicalist is engaged generically and the engagement is honest Mode Three boundary-marking with a Mode Two seed ("whether this deeper 'why' adds genuine explanatory value or merely restates the same facts in dualist vocabulary is the central question") — the article explicitly concedes the physicalist re-description is locally adequate and frames the disagreement as the open question rather than a refutation. No boundary-substitution. No label leakage (no editor-vocabulary terms in prose).

### Calibration Check (evidential-status discipline)

- PASSED. Interface-friction costs are framed as a HYPOTHESIS-tier consequence of the two-layer model throughout — "interpretive, not predictive," "does not generate empirically distinguishable predictions," "would become genuinely explanatory if it predicted something standard neuroscience does not." No possibility/probability slippage; no tenet-coherence presented as evidence-elevating. The Pathological Friction section is a model of restraint (clinical mappings explicitly "redescribe what neuroscience already explains … without generating predictions that distinguish the interface-friction account"). The psychedelic evidence is presented as "suggestive … but the evidence is mixed."

### Citation-Currency Pass (all external citations web-verified against primary sources)

- **Zheng & Meister (2025)** *Neuron* 113(2):192–204 ✓ (DOI 10.1016/j.neuron.2024.11.008) — year-label fixed 2024→2025 (see Critical above).
- **Tegmark (2000)** *Phys. Rev. E* 61, 4194–4206 ✓ — canonical, consistent corpus-wide.
- **Hagan, Hameroff & Tuszynski (2002)** *Phys. Rev. E* 65, 061901 ✓ (PMID 12188753; arXiv quant-ph/0005025).
- **Schwartz, Stapp & Beauregard (2005)** *Phil. Trans. R. Soc. B* 360(1458), 1309–1327 ✓ (PMID 16147524) — matches article exactly.
- **Carhart-Harris et al. (2012)** *PNAS* 109(6), 2138–2143 ✓ (PMID 22308440) — matches article exactly.
- **Stapp (2007)** *Mindful Universe*, Springer ✓; **Norretranders (1998)** *The User Illusion*, Viking ✓; **Zimmermann (1986)** chapter in Schmidt (Ed.) *Fundamentals of Sensory Physiology* ✓ — canonical books/chapters, no metadata defects.
- No orphaned references; every reference has an in-text home. No same-field author conflation (no Khan/Wiest, Musslick/Wu, Kiefer/Beni pattern present).

### Self-Contradiction Check

- None. The article consistently holds (a) interface friction is the mind-brain variant of a broader resistance pattern and (b) it is interpretive/explanatory, not predictive, of already-observed phenomena.

## Optimistic Analysis Summary

### Strengths Preserved

- Four-source friction taxonomy (bandwidth, decoherence, coupling imprecision, attentional cost).
- Honest epistemic framing ("interpretive, not predictive") — exemplary calibration; the Hardline Empiricist persona's praise applies directly.
- Balanced psychedelic-evidence treatment (aperture-vs-precision distinction).
- "Friction is the price of minimality" formulation and the bandwidth/quantum-Zeno tension with proposed sub-personal-observation resolution.
- Comprehensive five-tenet coverage.

### Enhancements Made

- None beyond the two corrections and the "(~10⁻¹ s)" derivation anchor. Article is converged; license to near-no-op exercised.

### Cross-links Added

- None this pass (forward links all resolve; reciprocity gap deferred — see Remaining Items).

## Length Check

- Before: 2230 words (89% of 2500 soft threshold — OK)
- After: 2232 words (89% — OK)
- Mode: Length-neutral. Net +2 words (the "(~10⁻¹ s)" anchor). Below soft threshold; stable.

## Remaining Items

- **Reciprocity follow-on (P3)**: add backlinks to interface-friction from attentional-economics.md, mental-effort.md, and filter-theory.md.
- **psychophysical-coupling article**: still referenced as a concept but not created. Carried forward from prior reviews.
- Developmental dimension (friction across the lifespan) and epistemic friction (brain-to-consciousness direction) remain deferred expansion opportunities to keep the article at concept-length.

## Stability Notes

- **The article is at high stability.** Five deep reviews; this pass found two correctable defects that convergence reviews missed (one arithmetic over-derivation, one citation year-label drift) — both surfaced only by the citation-currency / re-derivation discipline, not by re-reading for philosophical gaps. No content/argument edits were needed.
- **New stability note (arithmetic)**: the femtosecond-vs-millisecond decoherence gap is **twelve** orders of magnitude (10⁻¹³ s vs ~10⁻¹ s) when derived from this article's own figures. Do NOT re-inflate to "thirteen." The larger twelve-to-sixteen-order figure is corpus-correct only when paired with attentional rates against Tegmark's 10⁻¹ s bound — a different comparison.
- **New stability note (citation)**: Zheng & Meister is **(2025)**, *Neuron* 113(2):192–204 (online-first 2024). Keep this year in sync with the corpus-dominant form; do not regress to 2024.
- All prior stability notes remain valid: adversarial-persona disagreements are bedrock; the quantum-Zeno rate tension has an acknowledged proposed resolution (do not re-flag); psychedelic evidence is balanced (do not oscillate); the interpretive-not-predictive framing is deliberate (do not re-flag as "insufficiently empirical"); the six-domain resistance enumeration is kept in sync with phenomenology-of-resistance-across-domains.md.