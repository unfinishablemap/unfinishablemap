---
title: "Deep Review - Stapp's Quantum Mind Model"
created: 2026-07-16
modified: 2026-07-16
human_modified: null
ai_modified: 2026-07-16T22:55:04+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-16
last_curated: null
---

**Date**: 2026-07-16
**Article**: [[stapp-quantum-mind|Stapp's Quantum Mind Model]]
**Previous review**: [[deep-review-2026-06-20-stapp-quantum-mind|2026-06-20]] (introduced Georgiev 2015 + Monte Carlo critique; metadata web-verify)

This pass targeted the **claim-match / quote-fidelity / citation-framing** lens rather than metadata. The 2026-06-20 review web-verified citation metadata; this pass verbatim-checked the two quoted James strings at the primary source, re-verified the Denton 2024 study's *type* (experimental vs computational) against the paper, and cross-checked inline↔References. Three critical defects survived the metadata-only pass.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Fabricated/paraphrase-as-quote (William James), line 69** — The article attributed two quoted strings to James: `"Volition is nothing but attention"` and `"The free will question relates solely to the amount of effort of attention."` The first is verbatim (Principles of Psychology, ch. 11 — "we shall see that volition is nothing but attention"). The **second is not verbatim James**: it does not appear in ch. 26 (Will) or the free-will section; it is a paraphrase presented inside quotation marks. This is the recurring James-quote-fabrication defect class (memory: `james-quotes-fabricated-in-mind-dust-cluster`). **Resolution**: kept the verbatim first quote (added the ch. 11 locator), de-quoted the second into faithful indirect speech tied to James's actual claim that effort of attention is the essential phenomenon of willing.

- **Claim-match / study-type overstatement (Denton et al. 2024), line 113** — The article said "Nature Communications **published evidence** that the quantum Zeno effect itself **enables** magnetosensitivity" and called it "a **biological proof-of-concept**." The paper (Denton, Smith, Xu, Pugsley, Toghill & Kattnig, *Nat. Commun.* 15(1), 10823, DOI 10.1038/s41467-024-55124-x) is a **theoretical/computational spin-dynamics modelling study**, not an experimental demonstration. This is the memory-flagged Denton doubly-wrong trap (memory: `denton-2024-first-biological-precedent-propagation`): "demonstrated/evidence" → "modelled/computational." **Resolution**: reframed to "a Nature Communications spin-dynamics *modelling* study argued that the quantum Zeno effect **could** enable magnetosensitivity … a **computational** proof-of-concept—not an experimental demonstration." Cite retained; metadata (15(1), 10823) confirmed real-correct.

- **Inline↔References orphan (Kral et al. 2022), line 79** — "Meditation structural remodelling … has been weakened by replication failures (Kral et al., 2022)" was cited inline with **no References entry**. Verified the paper: Kral, T.R.A., et al. (2022), "Absence of structural brain changes from mindfulness-based stress reduction: Two combined randomized controlled trials," *Science Advances* 8(20), eabk3316 (n=218; failed to replicate MBSR structural change — body claim faithful). **Resolution**: added the References entry.

### Medium Issues Found

- **Wrong page metadata (Georgiev 2012)** — Reference cited "NeuroQuantology, 10(3), **552**." The "552" is the DOI article-id (10.14704/nq.2012.10.3.552), not a page; the real page range is **374–388**. Claim-match faithful (Stapp's model uses projection operators without its own wavefunction — a formal inconsistency). **Resolution**: corrected pages to 374–388 and added the DOI.

### Publisher-of-Record Citation Web-Verify Ledger

- Rajan et al. 2019 (*Cerebral Cortex* 29(7), 2832–2843) — **real-correct**. Willed>instructed frontal theta + frontoparietal coherence claim faithful.
- Denton et al. 2024 (*Nat. Commun.* 15(1), 10823, DOI 10.1038/s41467-024-55124-x) — metadata **real-correct**; **body framing corrected** (computational modelling study, not "published evidence"/"biological proof-of-concept").
- Georgiev 2012 (*NeuroQuantology* 10(3)) — claim **real-correct**; **page metadata corrected** 552 → 374–388 (552 was the DOI-id).
- Georgiev 2015 (*Int. J. Mod. Phys. B* 29(7), 1550039; arXiv:1412.4741) — **real-correct**. "Zeno breaks down beyond brain decoherence time; door left open if a decoherence-free subspace exists" — faithful to the paper.
- James 1890 quotes — "volition is nothing but attention" **real-correct** (ch. 11); "free will question relates solely to the amount of effort of attention" **paraphrase-as-quote, de-quoted**.
- Kral et al. 2022 (*Science Advances* 8(20), eabk3316) — **real-correct**; was an inline orphan, **References entry added**.
- Schwartz et al. 1996, Schwartz/Stapp/Beauregard 2005, Garrison et al. 2013, Zheng & Meister 2025, Tegmark 2000, Hagan et al. 2002, von Neumann 1932, Stapp 1993/1999/2007 — carried forward as **real-correct** from the 2026-06-20 publisher-of-record pass; bodies unchanged since.

**Currency sweep**: no unqualified superlative empirical claims. The ~10 bits/s figure is framed as a discriminator, correctly attributed (Zheng & Meister 2025).

### Counterarguments Considered

- Decoherence objection (Tegmark 10⁻¹³ s), Georgiev Monte Carlo no-go, formalism objection, epiphenomenalist alternative, illusionist challenge — all present and honestly hedged; the Georgiev-2015 decoherence-free-subspace framing correctly converts the objection from "impossible" to "open empirical question." No new critical gaps.

## Optimistic Analysis Summary

### Strengths Preserved

- The prediction set (§What Would Challenge This View) cleanly separates the attention-selection layer (predictions 1,2,3,5,6, shared with a classical account) from the quantum-specific layer (4,7). This calibration honesty is exemplary and was left untouched.
- The epiphenomenalist response's candour ("relocates rather than closes the explanatory gap") honours [[evidential-status-discipline]].

### Enhancements Made

- James attribution now carries a chapter locator and faithful indirect speech.
- Denton framing now states computational-vs-experimental status explicitly — strengthens rather than weakens the passage (the honest "could" reading is more defensible).

### Cross-links Added

- None (the 07-14 cross-link additions to [[quantum-zeno-effect]] and [[bohm-implicate-order-and-active-information]] are recent and sufficient).

## Remaining Items

None outstanding. Article is well-converged on argument structure; the yield this pass was entirely in the quote-fidelity/claim-match channel that metadata review does not reach.

## Stability Notes

- **Bedrock disagreements (do not re-flag as critical)**: the decoherence-timescale dispute (Tegmark vs Hagan/Hameroff), MWI-vs-collapse tension, and the heterophenomenological reading of effort are framework-boundary standoffs the article already marks honestly.
- **Calibration passed**: no possibility/probability slippage — the Denton correction removed the one place tenet-favourable framing had crept toward treating a computational model as empirical evidence. A tenet-accepting reviewer would now find no evidential-status overstatement.
- The James-quote defect is a **corpus-pattern warning**: verbatim-check every James attribution at the primary source; do not trust quotation marks inherited through Stapp's paraphrases.
