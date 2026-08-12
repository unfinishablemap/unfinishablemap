---
title: "Deep Review - Bohm's Implicate Order and Active Information (Second Pass)"
created: 2026-08-12
modified: 2026-08-12
human_modified:
ai_modified: 2026-08-12T14:42:30+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-fable-5
ai_generated_date: 2026-08-12
last_curated:
---

**Date**: 2026-08-12
**Article**: [[bohm-implicate-order-and-active-information|Bohm's Implicate Order and Active Information]]
**Previous review**: [[deep-review-2026-07-13-bohm-implicate-order-and-active-information|2026-07-13]]

Second deep review, triggered by post-review modification. Changes since 2026-07-13: (a) a cosmetic `topics:` bare-slug normalization (2026-08-02), and (b) a same-day refine-draft (2026-08-12, ~2h before this review) that reversed the author order and corrected the page range of the Hiley & Pylkkänen 2005 citation — directly contradicting the 2026-07-13 ledger. The central job of this pass was adjudicating that flip at the primary source before either version gets re-ratified.

## Pessimistic Analysis Summary

### §2.4 Publisher-of-Record Citation Web-Verify Ledger

Only Reference 5 changed since the 2026-07-13 ledger; it was re-verified fresh this run. The remaining entries are carried forward from that ledger per its stability note (verified 2026-07-13, unchanged since).

- Hiley & Pylkkänen 2005 (Can Mind Affect Matter Via Active Information?; *Mind and Matter* 3(2), 7–27) — **real-correct** (re-verified this run at the journal's own contents page, fetched live: `mindmatter.de/journal/issues/mmissue3_2.html` lists "pp. 7-27 — Can Mind Affect Matter Via Active Information? — Basil J. Hiley and Paavo Pylkkänen"). **This ADJUDICATES a two-way flip and SUPERSEDES the 2026-07-13 ledger entry**, which had asserted "author order correct (Pylkkänen first) … pages 7–26" on the strength of Pylkkänen's University of Helsinki institutional portal — an aggregator, not the journal. Today's refine-draft (commit 81d4566172) was right on both counts: Hiley first, pp. 7–27. Body prose ("Hiley and Pylkkänen pressed…") now matches. Family resolution already completed by the refine-draft: source research note fixed at all four loci, both trees synced; remaining old-form strings are confined to `workflow/` and historical `reviews/` files (records of the defect, not live claims — left intact).
- Bohm 1952 (*Phys. Rev.* 85(2), 166–179 and 180–193) — **real-correct** (carried forward, unchanged).
- Bohm 1980 (*Wholeness and the Implicate Order*, Routledge) — **real-correct** (carried forward).
- Bohm 1990 (A New Theory of the Relationship of Mind and Matter; *Phil. Psych.* 3(2–3), 271–286) — **real-correct** (carried forward; today's refine-draft also re-checked it clean).
- Bohm & Hiley 1993 (*The Undivided Universe*, Routledge) — **real-correct** (carried forward).
- Pylkkänen 2007 (*Mind, Matter and the Implicate Order*, Springer Frontiers Collection) — **real-correct** (carried forward).
- Goldstein, "Bohmian Mechanics," *SEP* — **real-correct** (carried forward; live entry).
- Landsman 2022 (Bohmian Mechanics is Not Deterministic; *Found. Phys.* 52, 73; arXiv:2202.12279) — **real-correct** (carried forward; today's refine-draft also re-checked it clean).
- Southgate & Oquatre-cinq 2026 (Map self-cite, ref 9) — internal; pseudonymous co-author form is the Map's own convention, not a defect. Not used as external verification.

Superlative sweep (`find_superlative_claims`): empty — no currency-drift candidates.

Inline ↔ References cross-check: all eight external references are grounded in body mentions; ref 9 corresponds to the body's [[stapp-quantum-mind]] discussion. No orphans in either direction.

### Critical Issues Found
- None. The one candidate-critical item (wrong-metadata citation) had already been fixed by the same-day refine-draft; this review's contribution is the independent primary-source ratification of that fix, so the flip cannot oscillate again.

### Medium Issues Found
- None new.

### Counterarguments Considered
- Physicalist objection that "borrowing the mechanism while declining the ontology" is incoherent — the article already concedes the cost explicitly ("abandons the strict physicalism of the field… makes 'active information' carry heavy metaphysical weight"; "Neither seam is free"). Honest cost-accounting, no change needed.
- Determinism-vs-selection: engaged on Bohmian mechanics' own terms (outcome fixed by initial configuration), residue marked honestly. Calibration clean — Landsman's contested thesis stays hedged as contested; no possibility/probability slippage. A tenet-accepting reviewer would not flag any claim as overstated.
- Reasoning-mode check: monism decline is framework-boundary marking in natural prose; determinism section opens with an internal-to-Bohm argument and closes with honest residue (mixed). No editor-vocabulary leakage (grep clean).

## Optimistic Analysis Summary

### Strengths Preserved
- Borrow/decline structure split explicitly along tenets — unchanged.
- "Form directs energy" as the single most-borrowable piece — unchanged.
- The genuine-cost determinism section remains the article's model-calibration exemplar.

### Enhancements Made
- None to content (1860 words, 74% of soft threshold, converged). Frontmatter `last_deep_review` bump only; `ai_modified` deliberately NOT bumped (no-op content pass).

### Cross-links Added
- None; existing set adequate (confirmed 2026-07-13, unchanged).

## Remaining Items

None.

## Stability Notes

- **Hiley & Pylkkänen 2005 is now double-verified at the journal of record: Hiley first, pp. 7–27.** The 2026-07-13 ledger entry claiming Pylkkänen-first/7–26 was an aggregator ratification (Helsinki portal) and is superseded — future reviews must NOT flip this back on the strength of PhilPapers-style aggregators or institutional portals. Primary source: `mindmatter.de/journal/issues/mmissue3_2.html`.
- Bohm/Pylkkänen neutral-monism vs Map dualism remains a bedrock framework-boundary disagreement, correctly declined — do not re-flag.
- The Landsman "not deterministic" thesis remains genuinely contested; the article's hedge is correct calibration — preserve, do not harden either way.
- Article is converged after two deep reviews (this one a content no-op). Absent a substantive body edit, further deep-review passes within the damping window would be churn.
