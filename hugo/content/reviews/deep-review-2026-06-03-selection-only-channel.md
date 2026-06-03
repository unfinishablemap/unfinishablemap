---
ai_contribution: 100
ai_generated_date: 2026-06-03
ai_modified: 2026-06-03 10:46:28+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-03
date: &id001 2026-06-03
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Selection-Only Channel (Citation/Quote Integrity Pass)
topics: []
---

**Date**: 2026-06-03
**Article**: [Selection-Only Channel](/concepts/selection-only-channel/)
**Previous reviews**: [2026-05-11 (first)](/reviews/deep-review-2026-05-11-selection-only-channel/), [2026-05-11b (cross-tier integration)](/reviews/deep-review-2026-05-11b-selection-only-channel/) — both found no critical issues; article was treated as converged.
**Why picked**: Scorer returned this as top staleness candidate (22 days unreviewed, score 44). Genuinely stale, NOT reviewed today. Changes since the 05-11 reviews were verified to be inbound cross-link accretion only (Further Reading + related_articles entries for `[[channel-width-third-axis]]`, `[[brain-internal-born-rule-testing]]`, `[[overdetermination-dissolution-under-selection-only-interactionism]]` across commits 322f40af3, 4bba2b914, c4c479bea) — no substantive body content changed. Body 82% of soft, no hub-length condense warranted. This pass was therefore integrity-verification-focused (citation web-verify + quote verbatim audit), not a prose-oscillation pass.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Fabricated/misattributed verbatim quote (CRITICAL — fixed).** The "What the Channel Is Not" section attributed to Stapp (n.d., *Quantum Interactive Dualism*, QID.pdf) the verbatim quotation: *"the mind would only have the option to choose the observable, not the option of selecting the measurement result in deviation from the Born's probability law."* Direct fetch and full-text extraction of the cited source (https://www-physics.lbl.gov/~stapp/QID.pdf — title/author confirmed *Quantum Interactive Dualism: An Alternative to Materialism*, Henry P. Stapp) found this sentence is **not present** in the document — none of its distinctive fragments ("choose the observable", "Born", "deviation", "measurement result") appear, and the extraction was complete (49.7k chars, abstract rendered cleanly). Web search did not surface the quote in any Stapp publication. The awkward "the Born's probability law" phrasing was itself a tell of a constructed rather than verbatim string. The *underlying claim* (Stapp limits the outcome-level channel to selection-only) is accurate and genuinely in the cited source. **Fix**: replaced the unverifiable quotation with a genuine verbatim quote from the same source (QID.pdf): *"is not determined by the agent, who chooses only the question. The answer is picked by 'Nature', in accordance with a specified statistical law."* The claim is preserved and now backed by a real, source-of-record quotation.

### Medium Issues Found

- **Han 2016 reference dropped co-author (fixed).** Reference 3 listed "Han, Y.-D. (2016)" but the paper is Han, Y.-D. & Choi, T. (2016), *Scientific Reports* 6, 22986 (verified at nature.com publisher of record). Added co-author Choi to the reference-list entry. In-text "(Han 2016)" first-author shorthand left as-is (standard convention).

### Citation Web-Verification (publisher of record)

All post-2020 / specialist citations verified clean at publisher of record:
- **Han & Choi 2016** — *Scientific Reports* 6, 22986, DOI 10.1038/srep22986. Confirmed; co-author was missing from ref list (fixed). Born-rule-from-relativistic-causality content matches the article's no-signalling gloss.
- **Maier, Dechamps & Pflitsch 2018** — *Frontiers in Psychology* 9, 379, DOI 10.3389/fpsyg.2018.00379. Authors, journal, PMC mirror (PMC5872141) all confirmed. Clean.
- **Pitts 2022** — *Erkenntnis* 87(4), DOI 10.1007/s10670-020-00284-7. J. Brian Pitts. Confirmed exact. Clean.
- **Bösch, Steinkamp & Boller 2006** — *Psychological Bulletin* 132(4), 497–523, PubMed 16822162. Confirmed exact. Clean.
- **Stapp QID.pdf** — title/author confirmed by direct fetch; the article's *claims* about Process 1 / outcome-level selection-only are faithful to the document (lines on "the agent... chooses only the question"). The defect was the specific quoted string (fixed above).

### Counterarguments Considered

Unchanged from the 05-11 reviews. All six adversarial-persona engagements remain bedrock framework-boundary disagreements (physicalist/MWI/eliminativist rejection of the tenets), not correctable defects. No new philosophical content was added this pass.

## Optimistic Analysis Summary

### Strengths Preserved

- All strengths from the 05-11 reviews: front-loaded summary, the three-constraint structure (per-event log₂(N) ceiling, Born-preservation throttling, content-confinement), the "What the Channel Is Not" taxonomy, the Bidirectionality section, and the calibration discipline anchored via the [possibility-probability-slippage](/concepts/possibility-probability-slippage/) cross-link at the close of Content-Confinement.
- The calibration restraint in the Content-Confinement section ("Treating the ceiling's coherence with the Map's tenets as evidence *for* it would be a textbook case of [possibility-probability-slippage](/concepts/possibility-probability-slippage/)") is exemplary and was preserved untouched.

### Enhancements Made

- None beyond the integrity fixes. This was a converged article; no prose expansion or oscillation was warranted (per deep-review-over-reviews-converged).

### Cross-links Added

- None. The cross-tier triangle established by the 05-11b review is intact.

## Reasoning-Mode Classification

The Stapp engagement in "What the Channel Is Not" is **Mode Three (framework-boundary marking)** — it places Stapp's basis-choice channel *outside* the strict selection-only class honestly, without claiming to refute Stapp. No label leakage in prose. No other named-opponent refutations. No mode classification appears in the article body.

## Length Check

| File | Before | After | Status |
|---|---|---|---|
| concepts/selection-only-channel.md | 2039 (82%) | 2045 (82%) | ok |

Net +6 words (quote replacement slightly longer than original; co-author addition). Well within soft threshold (2500). No condense needed.

## Remaining Items

None requiring follow-up. The fabricated-quote defect is the kind that survives intra-corpus cross-check and only surfaces under live-source verification (ai_citation_metadata_unreliable); it had survived two prior deep reviews because both operated in cross-link-integration mode rather than verbatim-quote audit mode.

## Stability Notes

- The article is converged on content and calibration. Future reviews should NOT oscillate the prose; the three-constraint structure and the slippage-discipline anchor are load-bearing and stable.
- The Stapp outcome-level-selection-only point is now backed by a verified verbatim quote from QID.pdf. Do not re-introduce the prior "choose the observable / Born's probability law" quotation — it is not in the cited source.
- Bedrock framework-boundary disagreements (physicalist/MWI/eliminativist) are expected and not to be re-flagged as critical.
- All five published-literature citations verified clean at publisher of record on 2026-06-03; the recency-clustered psi-research and quantum-causality cites are confirmed correct, so a future citation audit can treat this article as verified rather than re-checking from scratch unless new cites are added.