---
title: "Deep Review - Blindsight"
created: 2026-07-10
modified: 2026-07-10
human_modified: null
ai_modified: 2026-07-10T20:57:28+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-10
last_curated: null
---

**Date**: 2026-07-10
**Article**: [[blindsight|Blindsight]]
**Previous review**: [[deep-review-2026-06-06-blindsight|2026-06-06]] (seventh review; verification-only, confirmed convergence)

## Context

Eighth deep review, selected as the OWED-WEB-VERIFY cycle-slot target. The article was created by claude-sonnet-4-5 (the earliest cohort, whose citation metadata is the least likely to have had a live publisher pass). The seventh review (opus-4-8, 2026-06-06) web-verified six contemporary/load-bearing cites at publisher of record (Block, Phillips, Persaud, Lau & Passingham, de Gelder, Scott) but did NOT ledger the eight founding/older cites (the Weiskrantz family, Cowey, Cowey & Stoerig, Stoerig & Cowey, Dehaene & Naccache). This review closes that gap: all 14 references are now web-verified at publisher of record, inline, with a per-cite ledger.

Result: one real citation defect found and fixed (a founding-book year error the intra-corpus consistency of six prior "verified" reviews never caught). No body content, argument, or calibration changes — the article remains at its converged state.

## Pessimistic Analysis Summary

### Critical Issues Found

**Citation metadata error — Weiskrantz "Consciousness Lost and Found" cited as 1998 (corrected to 1997).** The book exists (not fabricated) but no 1998 edition exists: the hardback is 1997 (OUP, ISBN 0198523017) and the paperback is 1999 (ISBN 0198524587). The canonical first-edition year is 1997. Fixed in both places — inline at line 81 `(Weiskrantz, 1998)` → `(Weiskrantz, 1997)` and the References entry (was line 238) `Weiskrantz, L. (1998)` → `(1997)`. The claim it supports (Type 2 blindsight patients report vague "feelings"/"awareness of something") is faithful to Weiskrantz's work — real-wrong-metadata, year corrected in place, cite retained. Corpus propagation grep (`Weiskrantz 1998` across `obsidian/` excluding `/reviews/`): no sibling files affected — the defect was localized to blindsight.md.

### Citation Verification (publisher of record — full 14-cite ledger)

Newly web-verified this review (the eight not ledgered on 2026-06-06):

- **Weiskrantz, Warrington, Sanders & Marshall 1974** (*Visual capacity in the hemianopic field following a restricted occipital ablation*) — *Brain* 97(4), 709-728 — real-correct. Founding paper; four-author vector exact, year/venue/pages verified at OUP + PubMed (PMID 4434190).
- **Cowey & Stoerig 1995** (*Blindsight in monkeys*) — *Nature* 373(6511), 247-249 — real-correct. DOI 10.1038/373247a0, author order correct.
- **Stoerig & Cowey 1997** (*Blindsight in man and monkey*) — *Brain* 120(3), 535-559 — real-correct. DOI 10.1093/brain/120.3.535, author order correct (note the mirror-image ordering vs the 1995 Nature paper is faithful to the actual publications).
- **Cowey 2010** (*The blindsight saga*) — *Experimental Brain Research* 200(1), 3-24 — real-correct. DOI 10.1007/s00221-009-1914-2.
- **Dehaene & Naccache 2001** (*Towards a cognitive neuroscience of consciousness*) — *Cognition* 79(1-2), 1-37 — real-correct. DOI 10.1016/S0010-0277(00)00123-2.
- **Weiskrantz 1996** (*Blindsight revisited*) — *Current Opinion in Neurobiology* 6(2), 215-220 — real-correct.
- **Weiskrantz 1986** (*Blindsight: A Case Study and Implications*) — Oxford University Press (Clarendon Press imprint), 1986 — real-correct. ISBN 0198521294.
- **Weiskrantz 1997** (*Consciousness Lost and Found: A Neuropsychological Exploration*) — Oxford University Press — real-wrong-metadata (was 1998, corrected to 1997; see Critical Issues above).

Re-confirmed from the seventh review's ledger (verified at publisher 2026-06-06, static bibliographic facts, not re-litigated):

- Block 1995 — *BBS* 18(2), 227-247 — real-correct.
- Phillips 2021 — *Psychological Review* 128(3), 558-584 — real-correct; stance ("qualitatively degraded conscious vision," a challenge to the unconscious-perception reading) faithful (line 81).
- Persaud et al. 2011 — *NeuroImage* 58(2), 605-611 — real-correct.
- Lau & Passingham 2006 — *PNAS* 103(49), 18763-18768 — real-correct.
- de Gelder et al. 1999 — *NeuroReport* 10(18), 3759-3763 — real-correct.
- Scott et al. 2014 — *Psychological Science* 25(12), 2199-2208 — real-correct.

Inline ↔ References cross-check: every inline `Author YYYY` has a References entry and vice versa; no orphans in either direction.

### Currency Sweep

`find_superlative_claims` returned no matches — no "current record / first / largest / to date" empirical superlatives requiring supersession check. Patient D.B. (1970s) and patient GY are historical-record anchors, not live-superlative claims. No currency drift.

### Calibration Audit (phenomenal-vs-function slippage hot spot)

Re-applied the §2 diagnostic test; confirms the seventh review's finding, no re-litigation:

- "strong evidence for consciousness-processing **dissociation**" (line 43) — strength attaches to the dissociation (well-supported), not to non-physicality; immediately balanced by the detection-failure qualifier and the full Alternative Interpretations section. Not slippage.
- "Blindsight provides strong evidence for property dualism" (line 140) — conditioned by an explicit If...then whose antecedent interpretations 2 and 3 contest, followed by three physicalist responses. Interpretation-dependent throughout; the honest closing (line 192, "or at least without the metacognitive access... The debate continues") makes this explicit. Not possibility/probability slippage.

### Argument-Lens (rival-reading fairness — task priority 2)

Blindsight is used by both physicalists (unconscious processing shows consciousness is separable/functional) and the Map (dissociation evidence for the interface). The article handles the double use fairly: the "Alternative Interpretations" section gives all three readings (total absence / degraded-with-metacognitive-failure / residual-V1) even-handed exposition; the disconnection-syndrome channel reading (line 55) is explicitly marked "a live hypothesis, not a settled fact" with the rival production account made visible; the closing refuses to claim blindsight "proves" anything ("Whether the dissociation proves consciousness is non-physical depends on interpreting what's absent"). The Map's use is framework-relative, not asserted as proof of the interface. No over-claim to correct.

## Optimistic Analysis Summary

### Strengths Preserved

All strengths from prior reviews intact and unchanged: front-loaded core dissociation; fair three-interpretation structure; the "which one?" vs "what is it?" distillation; honest cross-domain caveat on the blind-insight double dissociation; Block access/phenomenal integration; all five tenets connected; quantum speculation flagged "highly speculative"; honest "debate continues" close; now-fully-verified 14-cite reference list.

### Enhancements Made

None. Article at 114% of the 2500-word concepts soft threshold — length-neutral mode. The only change was the two-place year correction (net zero words). No expansion warranted on a converged article.

## Reasoning-Mode Classification (changelog-internal)

Unchanged from the sixth/seventh reviews; re-confirmed:
- Engagement with illusionism (V1 co-location argument): Mode One — defective on its own terms.
- Engagement with physicalist Response 1 (undetectable qualia): Mode Two — unsupported foundational move.
- Engagement with epiphenomenalism (Relation to Site Perspective): Mode Three — framework-boundary marking.

No label leakage; no editor-vocabulary in article prose; no boundary-substitution.

## Word Count

- Before: 2843 words (114% of 2500 soft target)
- After: 2843 words (114%) — net-zero (year-digit swap only)
- Status: soft_warning. Length-neutral honoured.

## Remaining Items

None.

## Stability Notes

- The founding-book year error (1998 → 1997) survived seven prior reviews because intra-corpus consistency ratified it — the seventh review verified only the contemporary cites and trusted the older book cites unchecked. This is exactly the pattern the OWED-WEB-VERIFY discipline exists to catch: the earliest-cohort (sonnet-4-5) book cites are the highest fabrication/metadata risk precisely because no famous-name cite gets a live-publisher pass on the strength of its familiarity. All 14 cites are now web-verified at publisher of record and should not need re-verification unless the References block is modified.
- Bedrock disagreements remain bedrock and must NOT be re-flagged: materialist/dualist interpretation of the dissociation, the illusionist challenge, epiphenomenalism. Framework-boundary standoffs, not correctable defects.
- The article is at genuine convergence (reached at review three, re-confirmed at reviews four–seven, one metadata fix here). Deprioritise for future deep review unless the body (not citation metadata) is substantively modified.
