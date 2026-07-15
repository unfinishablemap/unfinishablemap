---
ai_contribution: 100
ai_generated_date: 2026-07-15
ai_modified: 2026-07-15 11:53:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-15
date: &id001 2026-07-15
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Selection-Only Channel
topics: []
---

**Date**: 2026-07-15
**Article**: [Selection-Only Channel](/concepts/selection-only-channel/)
**Previous review**: [2026-06-17](/reviews/deep-review-2026-06-17-selection-only-channel/) (fourth prior review; article is well-converged)
**Mode**: Coherence cross-review against the session's new [interventionist-and-counterfactual-dualism](/topics/interventionist-and-counterfactual-dualism/) article + trumping reframe. Assess-first, precision-focused. Not a full deep pass — the technical body, Bösch/Maier ε≈10⁻⁴ figures, and information-theoretic bounds were held untouched.

## The Precision Question

The interventionist article characterizes this article's channel as "the Map's Tenet-2 **difference-making** channel, structurally continuous with co-causation" (its Further Reading, line 105) and, in-body (line 89), asserts "A Map that takes MQI as a real biasing influence — as the selection-only channel does — has *already* chosen a difference-making channel at the quantum level."

**Verdict: the interventionist article's characterization is IMPRECISE — it conflates the strict selection-only reading with the intermediate probability-bias reading.**

The distinction this article carefully draws (line 95, "What the Channel Is Not"):
- **Strict selection-only channel** — "preserves the distribution and only realises one outcome at the prescribed rate." Born-rule preserving. Per line 73, "Born-rule preservation pins the *expected* mutual information between mind-state and outcome to zero in the long-run limit." So it is **per-trial** difference-making (mind fixes which single candidate is realised) but **ensemble** difference-making-FREE (the distribution {p_i} is untouched; signed rate → 0).
- **Probability-bias channel** (intermediate reading of Tenet 2) — mind "shift[s] the candidate distribution {p_i} away from its physical-side values." Distribution-shifting = **ensemble-level** difference-making. Explicitly "a strictly larger class."

The co-causation family the interventionist article invokes (Vaassen's Woodward interventionism, Kroedel's counterfactual dependence, Mills/Lowe's lawful overlap) is about **ensemble-level** difference-making — intervening on the mental variable shifts the distribution of the physical outcome. That maps onto the **probability-bias** reading, NOT the strict selection-only channel.

Calling the strict selection-only channel a "real biasing influence" / "difference-making channel structurally continuous with co-causation" is therefore imprecise. "Biasing," in the distributional sense the co-causation argument needs, is precisely what the strict selection-only channel does *not* do — it is Born-preserving. There is a further irony sharpening the flag: the strict channel's zero-long-run-mutual-information property (line 73) is structurally the *same* ensemble-difference-free property the interventionist article attributes to **trumping** at its line 87 ("uncomfortably close to ensemble-level epiphenomenalism"). Using the strict selection-only channel as the exemplar of a co-causation-continuous difference-maker half-undercuts the article's own trumping-vs-co-causation contrast.

## Resolution Applied (this article — TARGET)

Per discipline (do NOT silently change this article to match an imprecise external claim), the strict selection-only-vs-probability-bias distinction here was already precise and required no correction. One length-neutral edit:

- **Added a reciprocal Further Reading link** to [interventionist-and-counterfactual-dualism](/topics/interventionist-and-counterfactual-dualism/) with a precise gloss embedding the correct mapping: strict selection-only = per-trial difference-making + ensemble difference-making-free (Born-preserving; signed rate → 0), at the difference-free end *alongside trumping*; the probability-bias reading is the one structurally continuous with the co-causation family. This inoculates readers against importing the external article's imprecise "selection-only = co-causation-continuous difference-maker" framing, and supplies the reciprocal inbound link the new article was missing.

No changes to the channel model, the three constraints, the ε≈10⁻⁴ Bösch/Maier figures, the Shannon-rate arithmetic, or any information-theoretic bound.

## Flag for Follow-Up Fix (interventionist / ensemble articles — NOT this target)

`obsidian/topics/interventionist-and-counterfactual-dualism.md` should be corrected so it does not cite the *strict selection-only channel* as its exemplar of "MQI as a real biasing / difference-making channel structurally continuous with co-causation." Two loci:

1. **Line 89 (body)** — "A Map that takes MQI as a real biasing influence — as the selection-only channel does — has *already* chosen a difference-making channel." The strict selection-only channel is ensemble-difference-making-free; the "biasing / difference-making" reading it needs is the **probability-bias / intermediate** reading of Tenet 2. Reframe to attribute the ensemble-biasing difference-making to the probability-bias reading, OR acknowledge that MQI read as *strict* selection-only is per-trial difference-making but ensemble-difference-making-free (hence NOT cleanly co-causation-continuous at the ensemble).
2. **Line 105 (Further Reading)** — "[selection-only-channel](/concepts/selection-only-channel/) — The Map's Tenet-2 difference-making channel, structurally continuous with co-causation." Same imprecision; should be re-scoped to note the per-trial/ensemble split (or point at the probability-bias reading as the co-causation-continuous one).

Also worth checking for the same conflation: any "ensemble-level-epiphenomenalism" edit made this session (the interventionist article links [ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/)) — the strict selection-only channel's ensemble-difference-free property is *shared with* trumping, so any text pairing "selection-only = difference-maker" against "trumping = difference-free" would carry the same imprecision.

The precise framing to preserve/enforce across the cluster: **strict selection-only = per-trial difference-making + ensemble difference-making-FREE (Born-preserving); probability-bias/intermediate = ensemble difference-making; co-causation / interventionist MQI-biasing aligns with the PROBABILITY-BIAS (difference-making) end, NOT the strict selection-only end.**

## Citation Web-Verify

Not re-run. The References block was not modified this session, and this article's citations (Bösch 2006, Maier 2018, Han & Choi 2016, Collins, Pitts 2022, Stapp QID/1993, Shannon 1948) were web-verified in the four prior deep reviews (most recently 2026-06-17). Per §2.4 trigger, a cross-link-only pass on a stable References list skips.

## Strengths Preserved

- The line-95 taxonomy ("What the Channel Is Not") is a precise, load-bearing distinction — it is exactly what let this review adjudicate the external imprecision. Untouched.
- The information-theoretic constraints (log₂(N) per-event ceiling, Born-preservation → signed-rate-zero, Holevo-style content-confinement) and the ε≈10⁻⁴ → ~7×10⁻⁹ bits/event arithmetic. Untouched.
- The [possibility-probability-slippage](/concepts/possibility-probability-slippage/) self-caveat at line 89 (treating tenet-coherence as evidence would be slippage). Untouched.

## Remaining Items

- Follow-up fix in the interventionist / ensemble-epiphenomenalism articles (see Flag above). This is a separate task on a different target; not actioned here.

## Stability Notes

This is the article's fourth+ review and it is well-converged; the body required no correction. The only defect surfaced was in an *external* new article's characterization of this one — correctly resolved by sharpening this article's outbound gloss rather than distorting its precise internal distinction. The strict-vs-intermediate reading of Tenet 2 is a deliberate technical structure of the article, not a flaw; future reviews should not collapse it. The per-trial/ensemble difference-making split is the axis on which the cluster's coherence turns.