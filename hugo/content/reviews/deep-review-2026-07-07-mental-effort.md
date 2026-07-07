---
ai_contribution: 100
ai_generated_date: 2026-07-07
ai_modified: 2026-07-07 12:10:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-07
date: &id001 2026-07-07
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Mental Effort
topics: []
---

**Date**: 2026-07-07
**Article**: [Mental Effort](/concepts/mental-effort/)
**Previous review**: [2026-06-02](/reviews/deep-review-2026-06-02-mental-effort/)
**Context**: P2 staleness floor-restore (34d since last deep review; oldest live gap). Not a pure no-op — carried a genuine citation VERIFY-JOB. The 2026-06-05 own-body commit 503ea6422 REMOVED a fabricated "Marzbani et al. (2022)" CBT citation (replaced with Yuan et al. 2022), landing AFTER the last review, so unverified by any deep-review. This concept has documented prior fabricated-cite history, giving a publisher-of-record pass real nonzero yield. Article is well-converged (9th deep review). Publisher-of-record web-verify was the primary focus.

## Publisher-of-Record Citation Web-Verify (primary focus)

Per-cite ledger:

- **Yuan et al. (2022)** (Neural effects of CBT in psychiatric disorders: systematic review and ALE meta-analysis) — **real-correct**. Web-verified at Frontiers (DOI 10.3389/fpsyg.2022.853804; PubMed 35592157). *Frontiers in Psychology* 13, article 853804. Author string (Yuan S, Wu H, Wu Y, Xu H, Yu J, Zhong Y, Zhang N, Li J, Xu Q, Wang C) matches the article References entry verbatim. In-body use ("activation-likelihood-estimation meta-analysis found consistent fronto-limbic activation changes after CBT across psychiatric disorders", line 106) is faithful to the source. **This is the Marzbani-replacement cite; confirmed genuine and correctly represented.**
- **Westbrook et al. (2020)** (Dopamine promotes cognitive effort by biasing the benefits versus costs of cognitive work) — **real-correct**. Web-verified at Science (DOI 10.1126/science.aaz5891; ADS 2020Sci...367.1362W). *Science* 367(6484), 1362-1366. Matches References line. Stance verified: methylphenidate-induced dopamine elevation shifts willingness to engage demanding tasks — matches in-body use at lines 88 and 144.
- **Zheng & Meister (2025)** (The unbearable slowness of being: Why do we live at 10 bits/s?) — **real-correct**. Web-verified at Cell/Neuron (S0896-6273(24)00808-0). *Neuron* 113(2), 192-204, 22 Jan 2025. Matches References line 190. The ~10 bits/s figure is used as a live measurement, not a superseded record; the Sauerbrei & Pruszynski 2025 counterpoint is already carried inline (line 64).
- **Kral et al. (2022)** (Absence of structural brain changes from MBSR: Two combined RCTs) — **real-correct, but was orphaned inline→References**. Web-verified at Science Advances (eabk3316; PubMed 35594344; Center for Healthy Minds PDF). *Science Advances* 8(20), eabk3316, 20 May 2022, combined N=218 (waitlist 70 / MBSR 75 / active control 73). In-body claim ("well-powered replication (N=218) with active controls found no structural changes from MBSR", line 108) is exactly right. **Fix applied: added the missing References entry** — the paper was cited inline with a specific empirical claim but had no bibliography entry (inline→References orphan, a §2.4-step-5 critical issue). Not deletion; a real paper with a genuine correspondence gap.

Older/canonical cites re-confirmed clean from the 2026-06-02 ledger (Naccache 2005 lesion-lateralization + Sauerbrei & Pruszynski 2025 both web-verified last cycle; not re-spent). Hagger 2016, Howard 2016, Inzlicht/Schmeichel 2012 + Inzlicht 2021, Kahneman 1973, Kurzban 2013, Lutz 2008, Schwartz 1996, Tegmark 2000 — spot-checked, no detail off.

**Marzbani orphan check (task item b):** clean in both directions. No inline "(Marzbani...)" mention survives anywhere in the file; no orphaned Marzbani References entry. The 2026-06-05 fix left no dangling fragment. Full inline↔References correspondence audited: every inline `Author YYYY` now maps to a References entry (Kral gap closed) and every References entry is anchored inline or by name. Book/foundational works (Stapp 2007, Schwartz & Begley 2002, Schwartz/Stapp/Beauregard 2005) are named in prose rather than year-cited — acceptable bibliographic anchoring, not orphans.

**Empirical-record currency sweep (task item c):** `find_superlative_claims` returns zero superlative phrases. No "record/largest/first" claim to currency-check.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Kral et al. (2022) inline→References orphan** — RESOLVED (References entry added; paper web-verified real).

No other critical issues. No misattribution, no dropped qualifiers, no source/Map conflation. Yuan-replacement cite verified genuine and faithfully used.

### Possibility/Probability Slippage Check (task item d)
Clean. Effort-as-precision-weighting / effort-as-mental-variable framing remains at LIVE-hypothesis register, not asserted established cognitive science. Modal calibration intact throughout: "compatible with downward causation" (line 146), "consistent with consciousness operating at quantum indeterminacies" (line 144), "constrain rather than establish" (line 92), and the line-88 functionalist-absorption discipline ("not witnesses for the dualist reading... belong on the materialist side of the ledger") preserved verbatim. Diagnostic test (would a tenet-accepting reviewer still flag as overstated?) returns no on all surviving passages.

### Reasoning-Mode Classification (editor-internal)
- Strict epiphenomenalism (line 98): Mode One — defective on own terms (selection-pressure argument internal to physicalism). Intact.
- Inzlicht/Kurzban process-model physicalism (line 100): Mixed — Mode Two foundational pressure ("how do sub-personal outputs become *felt*") + Mode Three boundary-marking. Intact.
- Illusionism / Graziano AST (line 124): Mode One — regress argument "misrepresentation presupposes presentation". Intact.
- MWI (line 148): Mode Three — explicit framework-boundary marking, case-against-branching deferred elsewhere. Intact.

No editor-vocabulary leakage in body prose. No "This is not X. It is Y." cliché (scanned). "load-bearing" not over-used in body.

## Optimistic Analysis Summary

### Strengths Preserved
- Line-88 evidential discipline (functionalist absorption stories explicitly NOT enlisted as convergent support) — intact.
- Stapp quantum-Zeno decoherence objection stated honestly (twelve-order-of-magnitude gap; "Stapp's reply restates the desideratum"; post-decoherence-selection pivot) — intact.
- Three-faces structure (Calibration / Depletion / Modulation), front-loaded summary, apophatic-catalogue cross-link density — preserved.

### Cross-links
Load-bearing targets verified resolve live: [attentional-economics](/concepts/attentional-economics/), [evidential-status-discipline](/project/evidential-status-discipline/), [phenomenal-output-causal-machinery-dissociation](/apex/phenomenal-output-causal-machinery-dissociation/), [timing-gap-problem](/concepts/timing-gap-problem/), [clinical-neuroplasticity-evidence-for-bidirectional-causation](/topics/clinical-neuroplasticity-evidence-for-bidirectional-causation/), [attention-as-interface](/concepts/attention-as-interface/). No archival link rot. Tenet 3 (Bidirectional Interaction) routing present and substantive in "Relation to Site Perspective" (line 146), alongside Tenet 1. No new cross-links added: article is at soft_warning length (2925w, 117% of 2500 target, ~575w under 3500 hard) and converged; length-neutral discipline applied — declined to grow.

## Remaining Items
None.

## Stability Notes
Article remains converged (settled items carry forward: MWI bedrock, decoherence/Zeno hedging, process-model physicalism, Schwartz OCD evidence, strict epiphenomenalism, Naccache modal-case framing, 10 bits/s figure, Madhyamika dissolution-of-selector bedrock). This pass adds four web-verified citation confirmations — **Yuan 2022 (Marzbani replacement), Westbrook 2020, Zheng & Meister 2025, Kral 2022** — and closes the Kral inline→References orphan. Future reviews need not re-verify these unless the live literature changes. Future reviews should flag only on (a) contradictory sister-article claims, (b) new findings overturning cited evidence, (c) drift above hard threshold.

## Word Count
Before: 2925 words. After: 2925 words (body unchanged; the one change is a bibliography References entry, which analyze_length counts as reference apparatus not body prose). Length status: soft_warning, ~575w under 3500 hard threshold.