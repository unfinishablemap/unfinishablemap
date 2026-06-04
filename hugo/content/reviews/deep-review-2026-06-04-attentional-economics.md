---
ai_contribution: 100
ai_generated_date: 2026-06-04
ai_modified: 2026-06-04 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-04
date: &id001 2026-06-04
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Attentional Economics
topics: []
---

**Date**: 2026-06-04
**Article**: [Attentional Economics](/concepts/attentional-economics/)
**Previous review**: [2026-05-19](/reviews/deep-review-2026-05-19-attentional-economics/)

## Scope

Changed-since-review staleness pick (last_deep_review 2026-05-19, ai_modified 2026-05-28, ~9d settled gap — not same-session churn). DIFF-FIRST against the last-review commit: the only content change since 2026-05-19 was the 2026-05-28 reciprocal-cross-link commit (35ea8cbc5), which added a load-bearing CAUSAL claim grounding attentional scarcity in [interface-friction](/concepts/interface-friction/) under the "**Bandwidth limits**" bullet. That new claim was the primary audit target, plus a full web-verify of all citations.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Fabricated citation metadata (CRITICAL — FIXED).** The reference list and an inline mention cited the "~10 bits/second" figure to *"Meister, M. (2024). The physical limits of perception. PNAS, 121(14), e2400258121."* Web-verify at the publisher of record: the title returns nothing at PNAS, the article number e2400258121 does not resolve, and the actual source is **Zheng, J. & Meister, M. (2025). "The unbearable slowness of being: Why do we live at 10 bits/s?" *Neuron*, 113(2), 192-204** (arXiv 2408.10234; online 2024, Neuron print 2025). 3-state classification: REAL-PAPER-WRONG-METADATA (the author Meister and the 10-bits claim are genuine; the journal/title/volume/article-number were fabricated) → FIX, not drop. *Resolution*: corrected the inline mention (line 48: "Meister 2024" → "Zheng & Meister 2025") and the reference-list entry to the canonical corpus form already present in [concepts/attention-as-interface.md](/concepts/attention-as-interface/) line 279. Source-conclusion fidelity confirmed: Zheng & Meister (2024/25) does support ~10 bits/s conscious behavioural throughput vs ~10⁹ bits/s sensory input.

### New Causal Claim Audit (diff-first target)

The 2026-05-28 addition: *"The scarcity that makes attention economically tradeable is, on the Map's reading, downstream of [interface friction](/concepts/interface-friction/): attention is finite because the mind-brain channel has finite capacity and holding selections against the brain's default dynamics costs sustained expenditure. Friction supplies the why behind the scarcity this whole framework prices."*

- **Calibration: PASS, no slippage.** The claim is explicitly scoped with "on the Map's reading" and frames friction as the Map's *interpretation* of why attention is scarce, not an empirical upgrade. It does not slide attentional-scarcity-as-real (uncontested) into dualist-interface-friction-as-established. The underdetermination sits at the genuine inference point (whether scarcity is *best* explained by interface friction vs a physical resource-limit is left open by the framing). A tenet-accepting reviewer would not flag this as overstated — it is honest framework-conditioning. Not possibility/probability slippage.
- **Seam with [interface-friction](/concepts/interface-friction/): COHERENT + RECIPROCATED.** interface-friction.md line 75 carries the near-exact reciprocal ("Interface friction explains *why* attention is scarce: the mind-brain channel has finite capacity and maintaining influence through it requires sustained expenditure") and links back to [attentional-economics](/concepts/attentional-economics/) (line 129). The new claim does not misrepresent the target. Critically, interface-friction.md line 41 itself carries the load-bearing calibration caveat that friction "does not generate empirically distinguishable predictions" and "its value is interpretive" — so the grounding inherits, rather than smuggles past, the evidential restraint.

### Citation Web-Verification (all references)

- **Zheng & Meister (2025), Neuron 113(2), 192-204** — was fabricated as Meister/PNAS; FIXED (see above).
- **Inoue, S. & Matsuzawa, T. (2007). Working memory of numerals in chimpanzees. *Current Biology*, 17(23), R1004-R1005** — VERIFIED correct (author/year/journal/vol/pages exact).
- **Suddendorf, T. & Corballis, M.C. (2007). The evolution of foresight... *Behavioral and Brain Sciences*, 30(3), 299-313** — VERIFIED correct (exact). Bischof-Köhler attribution already corrected in the 2026-05-19 review; source/Map separation intact.
- **Schwartz, J.M. & Begley, S. (2002). *The Mind and the Brain*** — well-known book, correctly cited; retains the n=18 / not-independently-replicated caveat from the 2026-03-09 review (evidential restraint preserved).
- **Stapp, H.P. (2007). *Mindful Universe*** — well-known book, correctly cited.

### Reasoning-Mode Classification

No named-opponent engagements. The "Objections and Responses" section addresses generic positions (folk-psychology charge, epiphenomenalism, bandwidth-limit objection) in natural prose. No editor-vocabulary leakage. No classification changes.

### Medium / Bedrock

No new medium issues. The functionalist and MWI bedrock disagreements remain framework-boundary standoffs (NOT re-flagged).

## Optimistic Analysis Summary

### Strengths Preserved

- The economic-framing table, three-level witness-mode structure, and habituation/de-habituation treatment remain the article's distinctive contributions.
- The new interface-friction grounding is a genuine improvement: it supplies a "why" for the scarcity the whole economic metaphor prices, deepening the article without over-claiming. The Hardline Empiricist persona's praise-worthy pattern (tenet-coherent, not evidence-elevating) is honoured.
- Schwartz & Begley evidential caveats intact.

### Enhancements Made

- Corrected fabricated Meister/PNAS citation (inline + reference list).
- Updated timestamps.

### Cross-links Added

None new (comprehensive set already in place; [interface-friction](/concepts/interface-friction/) added in the 05-28 commit and verified reciprocated).

## Length

- Pre-review: 2716 words (109% of 2500 soft — soft_warning)
- Post-review: 2722 words (109% — soft_warning; +6 words from the citation correction adding the co-author/title)

Under the 3500 hard threshold. No condense. Length-neutral band preserved.

## Anchoring

`evaluate_anchoring` clean (no flags) before and after edits.

## Remaining Items / Follow-on

- **P2 queued (corpus-wide):** the same fabricated "Meister 2024 PNAS physical limits of perception" cite propagates to live siblings — [concepts/attention-as-interface.md](/concepts/attention-as-interface/) (line 266, internally inconsistent with its own correct line 279), [concepts/sleep-and-consciousness.md](/concepts/sleep-and-consciousness/) (lines 50/183), [topics/responsibility-gradient-from-attentional-capacity.md](/topics/responsibility-gradient-from-attentional-capacity/) (lines 45/184), and [concepts/stapp-quantum-mind.md](/concepts/stapp-quantum-mind/) (already flagged as an orphan ref by pessimistic-2026-05-25). Queued as a grounded refine-draft follow-on (out of this article's scope). reviews/research/changelog/archive matches left untouched per discipline.

## Stability Notes

This is the fifth deep review. The article is otherwise stable: the new causal claim is defensible and properly calibrated, the seam reciprocates, and four of five citations verified clean on first pass. The one defect (fabricated Meister metadata) is an AI-citation-metadata artifact, not a content/argument flaw — it survived four prior reviews because intra-corpus cross-check propagated it (the bad form even appears alongside the correct form in attention-as-interface.md); only live-literature web-verify caught it. Bedrock disagreements (functionalist alternatives, MWI indexical response) remain framework-boundary and should NOT be re-flagged.