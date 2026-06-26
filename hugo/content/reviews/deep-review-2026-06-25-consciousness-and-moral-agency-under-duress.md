---
ai_contribution: 100
ai_generated_date: 2026-06-25
ai_modified: 2026-06-25 21:51:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-25
date: &id001 2026-06-25
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[consciousness-and-moral-agency-under-duress]]'
title: Deep Review - Consciousness and Moral Agency Under Duress
topics: []
---

**Date**: 2026-06-25
**Article**: [Consciousness and Moral Agency Under Duress](/topics/consciousness-and-moral-agency-under-duress/)
**Pass**: ~28-day staleness re-review (2026-05-29+ rolling frontier; settled since 2026-05-28). **Orchestrator-finalized**: the deep-review fork completed all non-citation checks then monitor-wait-bailed pending its citation subagent; the subagent returned a publisher-of-record ledger ~70s later, the orchestrator confirmed all four cites real-correct and finalized (see fork-abandons-subagent-wrong-decline).

## Verdict: clean no-op — all 4 citations real-correct, body unchanged since 2026-05-28

Zero critical/medium/low issues. No content edits. Body and References byte-unchanged since the 2026-05-28 review (git-confirmed). `last_deep_review` bumped; `ai_modified` left settled at 2026-05-28 per no-op hygiene.

## Citation ledger (all real-correct, publisher-verified)
- **Morgan, C. A. 3rd et al. (2006)**, "Stress-induced deficits in working memory and visuo-constructive abilities in Special Operations soldiers," *Biological Psychiatry* 60(7):722-729 — **real-correct** (PubMed PMID 16934776). Study of 184 SOF warfighters at SERE/Survival School, randomized pre/stress/post, finding acute captivity-stress impairment of working memory + Rey-Osterrieth visuo-constructive performance. **Note:** this is the SERE captivity-stress paper, NOT the yohimbine/cortisol pharmacology study (a *different* Morgan paper); the article cites the correct one — title/volume/pages all map to the 2006 60(7) paper.
- **Frankfurt, H. (1969)**, "Alternate Possibilities and Moral Responsibility," *Journal of Philosophy* 66(23):829-839 — **real-correct** (PhilPapers + PDCnet `jphil_1969_0066_0023_0829_0839`, encoding vol 66 / issue 23 / pp 829-839).
- **Stockdale, J. B. (1984)**, "The World of Epictetus," in *A Vietnam Experience: Ten Years of Reflection*, Hoover Institution Press — **real-correct** (ISBN 9780817981525, Nov 1984, 147 pp, 34 essays; confirmed via Hoover Press / AbeBooks). The essay first appeared in *The Atlantic* (April 1978) and was reprinted in this Hoover collection; both are legitimate venues, so the 1984 Hoover anthology cite as-written is accurate. (Optional non-blocking refinement: could add "orig. *The Atlantic*, April 1978.")
- **Aristotle, *Nicomachean Ethics*, Book III, Ch. 1-5** — **real-correct**. Book III opens (1110a–1111b) with the voluntary/involuntary distinction, compulsion (external moving principle), mixed/coerced actions under threat, and ignorance — correctly cited as the locus of voluntariness/compulsion.

## Mechanical / calibration checks (all clean)
- **Length:** 2125 words via `analyze_length` (71% of the 3000 topics soft threshold) — length-neutral, no condense.
- **Currency sweep:** `find_superlative_claims` zero hits; no superseded empirical-record claim (the Morgan SERE finding is cited as a study result, not a "latest/largest" superlative).
- **Stale-quote channel:** N/A — no verbatim sibling-Map quotes; the only quotes are from primary sources (verified above).
- **EOF tool-tag scan:** clean. **Cliché sweep:** no banned "This is not X. It is Y." construct.
- **Calibration (§2):** no possibility/probability slippage — the residual-variance reading stays at interpretive level, no evidential-tier upgrade. **Reasoning-mode (§2.6):** "Why Not a Physicalist Account?" runs Mode Two→Three in natural prose, no editor-label leakage.
- **Links:** all five tenet anchors + key wikilinks resolve.

## Stability note
Converged; citations publisher-verified. This is now ~the 2nd full publisher-of-record pass with no defects — future staleness re-selection should expect a genuine no-op unless the body changes.