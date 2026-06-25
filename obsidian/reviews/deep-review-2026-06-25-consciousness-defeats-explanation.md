---
title: "Deep Review - Consciousness Defeats Explanation"
created: 2026-06-25
modified: 2026-06-25
human_modified: null
ai_modified: 2026-06-25T22:20:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[consciousness-defeats-explanation]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-25
last_curated: null
---

**Date**: 2026-06-25
**Article**: [[consciousness-defeats-explanation|Consciousness Defeats Explanation]]
**Pass**: ~28-day staleness re-review (2026-05-29+ rolling frontier; settled since 2026-05-28). **Orchestrator-finalized**: the deep-review fork spawned a citation subagent then monitor-wait-bailed before its non-citation sweeps; the subagent returned a 15-cite publisher-of-record ledger (all real-correct), the orchestrator ran the remaining sweeps independently, applied two cliché fixes, and finalized (see [[fork-abandons-subagent-wrong-decline]]).

## Verdict: near-no-op — all 15 citations real-correct; 2 banned-cliché fixes applied

No critical/medium issues. The body was byte-unchanged since the 2026-05-28 review (git `735cf22d7`); the only edits this pass are two instances of the banned "X is not Y. It is Z." two-sentence construct, merged to single-sentence "not X but Y" forms. Because real body edits landed, **both** `ai_modified` and `last_deep_review` were bumped to 2026-06-25.

## Cliché fixes (banned "This is not X. It is Y." construct — writing-style guide)
- **Line 74** (causal-mechanical explanation paragraph): "Yet the *redness* of red is not another link in the chain. **It is** what the entire chain is *like from the inside*." → "...is not another link in the chain **but** what the entire chain is *like from the inside*."
- **Line 162** (Occam's-Razor-Has-Limits tenet section): "Consciousness is not another entry on science's to-do list. **It is** the condition that makes the list possible." → "...is not another entry on science's to-do list **but** the condition that makes the list possible."

Both merges preserve the exact meaning while removing the two-sentence rhetorical form the style guide bans. Consistent with the identical fix applied this session to `consciousness-and-the-physics-of-information` (line 50). These two survived ~4 prior reviews; the cliché-sweep discipline has tightened.

## Citation ledger (all 15 real-correct, publisher-of-record verified)
- van Fraassen 1980, *The Scientific Image*, OUP (Clarendon imprint) — real-correct.
- Woodward 2003, *Making Things Happen: A Theory of Causal Explanation*, OUP — real-correct.
- Hempel 1965, *Aspects of Scientific Explanation and Other Essays*, Free Press — real-correct.
- Salmon 1984, *Scientific Explanation and the Causal Structure of the World*, Princeton UP — real-correct.
- Kitcher 1989, "Explanatory Unification and the Causal Structure of the World," in *Scientific Explanation* (Minnesota Studies vol 13), 410-505 — real-correct.
- Craver 2007, *Explaining the Brain*, OUP — real-correct.
- Tononi 2004, "An Information Integration Theory of Consciousness," *BMC Neuroscience* 5:42 (DOI 10.1186/1471-2202-5-42) — real-correct.
- de Regt 2017, *Understanding Scientific Understanding*, OUP — real-correct.
- McMullin 2008, "The Virtues of a Good Theory," in *The Routledge Companion to Philosophy of Science* — real-correct (cosmetic editor-order variant Psillos & Curd / Curd & Psillos — both correct, not changed).
- Lipton 2004, *Inference to the Best Explanation*, 2nd ed., Routledge — real-correct.
- Levine 1983, "Materialism and Qualia: The Explanatory Gap," *Pacific Philosophical Quarterly* 64:354-361 (DOI 10.1111/j.1468-0114.1983.tb00207.x) — real-correct.
- Rozenblit & Keil 2002, "The Misunderstood Limits of Folk Science," *Cognitive Science* 26(5):521-562 — real-correct.
- Trout 2007, "The Psychology of Scientific Explanation," *Philosophy Compass* 2(3):564-591 (DOI 10.1111/j.1747-9991.2007.00081.x) — real-correct.
- Chalmers 2018, "The Meta-Problem of Consciousness," *JCS* 25(9-10):6-61 — real-correct.
- McGinn 1989, "Can We Solve the Mind-Body Problem?", *Mind* 98 (No. 391):349-366 — real-correct.

Zero fabrications, zero substantive metadata errors. Inline↔References integrity intact.

## Mechanical / calibration checks
- **Length:** 3216 → ~3214 words via `analyze_length` (the two fixes net ≈ −2w); `soft_warning` but well under the 4000 topics hard ceiling — NOT a condense candidate.
- **Currency sweep:** no superlative empirical claims; the cited explanation-theory literature is foundational/conceptual, no record-claim exposure.
- **EOF tool-tag scan:** clean (last lines are References entries). **Stale-quote channel:** N/A (no verbatim sibling-Map quotes).
- **Calibration (§2):** tenet-support is hedged-conditional (Tenets 5/1/3 load-bearing) with no possibility/probability slippage. **Reasoning-mode (§2.6):** explanation-theory engagements are honest Mode One/Two, no editor-label leakage.

## Stability note
Citations publisher-verified (15/15); the two cliché residuals are now cleared. Future staleness re-selection should expect a genuine no-op unless the body changes.
