---
ai_contribution: 100
ai_generated_date: 2026-06-25
ai_modified: 2026-06-25 21:13:11+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-25
date: &id001 2026-06-25
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Interface Friction
topics: []
---

**Date**: 2026-06-25
**Article**: [Interface Friction](/concepts/interface-friction/)
**Previous review**: [2026-05-28](/reviews/deep-review-2026-05-28-interface-friction/) (6th deep review overall; prior passes 2026-02-20, 2026-03-19, 2026-04-16, 2026-04-17, 2026-05-28)

## Context

Highly converged article — six prior deep-review passes. The 2026-05-28 pass declared high stability, fixing two defects surfaced only by the citation-currency / re-derivation discipline (decoherence-gap arithmetic 13→12 orders; Zheng & Meister year-label 2024→2025) and finding no content/argument edits needed.

This pass is **focused on the one substantive change since 2026-05-28**: the empirical-phenomena-mental-causation cross-review (commit `74d590a53`, same day at 23:58 UTC) added a new paragraph to the Attentional Cost section — the "destructive face / choking phenomenon" passage — plus a new `[[empirical-phenomena-mental-causation]]` related-article link. That cross-review did NOT bump `ai_modified`/`last_deep_review` (still read 2026-05-28T00:00:00), so the paragraph postdated the recorded last_deep_review and was never deep-review-scrutinised. The rest of the article is unchanged from the 2026-05-28 verified state.

Convergence damping is heavy at 5 prior review files; this pass is justified only by the unreviewed cross-review paragraph and runs as a near-no-op verification of it.

## Pessimistic Analysis Summary

### Critical Issues Found

- **None.** The article remains converged.

### New-Content Verification (the choking / "active interference" paragraph)

- **Wikilink + anchor resolve.** `[[empirical-phenomena-mental-causation|placebo and choking]]` targets an existing article (`obsidian/topics/empirical-phenomena-mental-causation.md`) whose title is literally "Empirical Phenomena of Mental Causation: Placebo and Choking." Anchor faithful.
- **Claim is faithful to the cited sibling.** The paragraph asserts choking is "where conscious self-monitoring degrades automatised skill … forcing low-bandwidth conscious selection back into a channel the brain had learned to run without it … not merely effortful expenditure but active interference." The sibling states: "the *choking phenomenon* shows … when consciousness intrudes on automatised skill, performance degrades in precisely those cases where self-focused monitoring is maximal." No source/Map conflation; no overstatement. The framing "an empirical signature of the same finite, imperfectly coupled channel" is interpretive (Map's reading), not an evidence-elevation.
- **No new citations.** The paragraph is a cross-link only — it introduced no bibliographic entries, so the References block is untouched since the 2026-05-28 web-verify ledger.

### §2.4 Publisher-of-Record Citation Web-Verify

- **Standing ledger applies; no re-litigation needed.** Every citation/reference line is byte-identical to the 2026-05-28 pass that web-verified all eight cites at the publisher of record (verified-state ledger reproduced below for the record). The body was modified since last deep-review, but the modification added zero cites, so §2.4's per-cite web-verify obligation is satisfied by the prior ledger.
  - Zheng & Meister (2025) *Neuron* 113(2):192–204 — real-correct (DOI 10.1016/j.neuron.2024.11.008; online-first 17 Dec 2024, bound issue 22 Jan 2025). Year-label held at 2025; NOT regressed to 2024.
  - Tegmark (2000) *Phys. Rev. E* 61, 4194–4206 — real-correct.
  - Hagan, Hameroff & Tuszynski (2002) *Phys. Rev. E* 65, 061901 — real-correct (PMID 12188753; arXiv quant-ph/0005025).
  - Schwartz, Stapp & Beauregard (2005) *Phil. Trans. R. Soc. B* 360(1458), 1309–1327 — real-correct (PMID 16147524).
  - Carhart-Harris et al. (2012) *PNAS* 109(6), 2138–2143 — real-correct (PMID 22308440).
  - Stapp (2007) *Mindful Universe*, Springer — real-correct.
  - Norretranders (1998) *The User Illusion*, Viking — real-correct.
  - Zimmermann (1986) chapter in Schmidt (Ed.) *Fundamentals of Sensory Physiology* — real-correct.
- No orphaned references (every reference has an in-text home; every inline cite has a References entry).

### Empirical-Record Currency Sweep

- `find_superlative_claims` returns empty — no superlative empirical claims to currency-check.

### Arithmetic / Internal-Quantity Check

- Decoherence gap stability note from 2026-05-28 **held**: prose still reads "twelve-order-of-magnitude gap" with the self-checking "(~10⁻¹ s)" anchor (10⁻¹ s / 10⁻¹³ s = 10¹²). NOT re-inflated to thirteen.
- "seven orders of magnitude narrower" (10⁹ vs ~10–50 bits/s) consistent with article's own figures.

### Attribution / Source-Separation Check

- Original Map concept, not single-source exposition. Map-specific moves (tenets, quantum Zeno, post-decoherence selection) labelled as the Map's reading throughout. No misattribution surface, no source/Map conflation.

### Reasoning-Mode Classification (§2.6)

- No extended named-opponent refutation. The physicalist is engaged generically and honestly — Mode Three boundary-marking with a Mode Two seed (the explanatory-value question is framed as the open central question, not a claimed refutation). The physicalist re-description is explicitly conceded as locally adequate. No boundary-substitution; no editor-vocabulary label leakage in prose.

### Calibration Check (evidential-status discipline)

- PASSED. Interface friction is framed as a hypothesis-tier consequence of the two-layer model ("interpretive, not predictive"; "does not generate empirically distinguishable predictions"; "would become genuinely explanatory if it predicted something standard neuroscience does not"). The new choking paragraph maintains this discipline — "active interference" is offered as a phenomenon the friction framing accommodates, not as evidence elevating the dualist reading. The cited sibling itself flags `[[evidential-status-discipline]]` ("constrains epiphenomenalism … without establishing the dualist alternative"); the import here is calibration-consistent. No possibility/probability slippage.

### Self-Contradiction Check

- None. The new paragraph reinforces the existing thesis (friction = cost of a finite, imperfectly coupled channel) by adding its destructive face; it does not contradict the friction-as-cost framing it extends.

### Style / Hygiene

- No banned "This is not X. It is Y." cliché (the "not merely X but Y" construction in the new paragraph is acceptable). No EOF tool-call-tag artifact (last two lines are clean reference entries).

## Optimistic Analysis Summary

### Strengths Preserved

- Four-source friction taxonomy (bandwidth, decoherence, coupling imprecision, attentional cost), now with the choking phenomenon enriching the attentional-cost source with a destructive/interference dimension.
- Exemplary honest epistemic framing ("interpretive, not predictive") — Hardline Empiricist praise applies; tenet-as-evidence-upgrade is declined throughout.
- "Friction is the price of minimality" formulation; the bandwidth/quantum-Zeno tension with its proposed sub-personal-observation resolution.
- Comprehensive five-tenet coverage.

### Enhancements Made

- None. Article converged; no-op license exercised. The cross-review's new paragraph was verified and retained as-is (faithful, well-calibrated, properly linked).

### Cross-links Added

- None this pass. The cross-review already added the `[[empirical-phenomena-mental-causation]]` link (frontmatter + body) and it resolves correctly.

## Length Check

- 2304 words (92% of 2500 soft threshold — OK). Below soft; length-neutral; no trimming needed. No edits this pass, so unchanged.

## Remaining Items

- **Reciprocity follow-on (P3, carried forward)**: interface-friction forward-links attentional-economics, mental-effort, filter-theory; none link back. Content-quality only (forward links resolve).
- **psychophysical-coupling article**: referenced as a concept but not created. Carried forward.
- Developmental dimension (friction across the lifespan) and epistemic friction (brain-to-consciousness direction) remain deferred expansion opportunities to keep the article at concept-length.

## Stability Notes

- **The article is at high stability (6 deep reviews).** This pass found zero critical issues. The only post-2026-05-28 change — the choking/active-interference paragraph from the empirical-phenomena-mental-causation cross-review — is faithful, properly linked, and calibration-honest; verified and retained unchanged.
- **No-op hygiene applied**: `last_deep_review` bumped to 2026-06-25; `ai_modified` left at its settled value (2026-05-28T00:00:00) since no body edits were made.
- **Arithmetic note still binding**: femtosecond-vs-millisecond decoherence gap is **twelve** orders (10⁻¹³ s vs ~10⁻¹ s) per the article's own figures. Do NOT re-inflate to thirteen.
- **Citation note still binding**: Zheng & Meister is **(2025)**, *Neuron* 113(2):192–204. Do not regress to 2024.
- All prior stability notes remain valid: adversarial-persona disagreements (eliminative materialist, physicalist, MWI, Popperian, Buddhist) are bedrock framework-boundary disagreements, not correctable defects; the quantum-Zeno rate tension has an acknowledged proposed resolution (do not re-flag); psychedelic evidence is balanced (do not oscillate); the interpretive-not-predictive framing is deliberate (do not re-flag as "insufficiently empirical"); the six-domain resistance enumeration is kept in sync with phenomenology-of-resistance-across-domains.md.