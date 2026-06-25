---
ai_contribution: 100
ai_generated_date: 2026-06-25
ai_modified: 2026-06-25 10:31:00+00:00
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
title: Deep Review - Supervenience
topics: []
---

**Date**: 2026-06-25
**Article**: [Supervenience](/concepts/supervenience/)
**Previous review**: [2026-05-26](/reviews/deep-review-2026-05-26-supervenience/) (and [2026-03-24b](/reviews/deep-review-2026-03-24b-supervenience/), [2026-03-24a](/reviews/deep-review-2026-03-24-supervenience/))

## Disposition: No-op verification pass (converged, unchanged)

This is the article's **fourth** deep review. The body is **unchanged since the 2026-05-26 review**: `ai_modified` equalled `last_deep_review` exactly (both `2026-05-26T07:51:35+00:00`) and `git log` shows no commits touching the file since 2026-05-26. The candidate-selection algorithm would normally *exclude* a reviewed-and-unchanged document; this pass ran only because the file was named explicitly as the skill argument. Per the convergence discipline, the correct action on a thrice-clean unchanged article is a verification pass, **not** cosmetic edits (which would only re-trigger the convergence-damping churn the algorithm is designed to suppress). No content changes were made; only `last_deep_review`/`ai_modified` were bumped.

## Pessimistic Analysis Summary

### Critical Issues Found
None.

### §2.4 Publisher-of-Record Citation Web-Verify
Per-cite ledger (the body is unchanged, but the References block carries fine-grained metadata, so the highest-yield cites were re-verified live):

- Levine, J. (1983) (Materialism and Qualia: The Explanatory Gap, *Pacific Philosophical Quarterly* 64(4):354-361) — **real-correct**. Verified against Wiley Online Library (DOI 10.1111/j.1468-0114.1983.tb00207.x) and the newdualism.org publisher PDF. Volume, issue, and page range all faithful.
- Davidson, D. (1970) (Mental Events, in Foster & Swanson eds., *Experience and Theory*, University of Massachusetts Press) — **real-correct**. Verified via PhilPapers (FOSME / FOSEAT). Editors' surnames/initials and publisher correct; the article omits the optional page range (pp. 79-101), which is not an error.
- Kim, J. (1993) (Supervenience as a Philosophical Concept, in *Supervenience and Mind*, Cambridge University Press) — **real-correct** (canonical collection; no fine-grained metadata to misstate; verified clean in 2 prior reviews against an unchanged body).
- Kim, J. (2005) (*Physicalism, or Something Near Enough*, Princeton University Press) — **real-correct** (canonical monograph).
- Chalmers, D. (1996) (*The Conscious Mind*, Oxford University Press) — **real-correct** (canonical monograph).
- Southgate, A. & Oquatre-six, C. (2026) (The Strong Emergence of Consciousness, *The Unfinishable Map*) — internal Map cross-reference, not an external claim.

Inline ↔ References cross-reference: every inline `Author YYYY` (Davidson, Hare [ethics origin, attribution not bibliographic], Putnam, Levine, Kim, Chalmers) maps to a References entry or is a well-known attribution; no orphans in either direction.

### Empirical-record currency sweep
`find_superlative_claims` returned no matches. This is a conceptual-metaphysics article about a logical relation; it makes no superlative empirical claims, so the currency channel does not apply.

### Attribution / calibration / reasoning-mode (re-confirmed, unchanged)
The 2026-05-26 review's findings stand because the body is byte-identical:
- Attribution clean (Davidson anomalous monism, Hare ethics origin, Putnam multiple realisability, Levine explanatory gap, Kim exclusion + "non-reductive physicalism is unstable", Chalmers psychophysical laws).
- No possibility/probability slippage. The §2 diagnostic test passes: the load-bearing claims are conceptual/logical ("supervenience does not *entail* physicalism" — an entailment-gap claim type-B physicalists concede), not empirical-attribution claims upgraded on tenet-load. The "establishes vs constrains" language is correct throughout.
- Reasoning modes honest and label-free: type-B physicalists engaged Mode Two (unsupported a posteriori necessity, using the opponents' own conceivability structure); Kim engaged Mode Three (Map agrees with Kim's diagnosis, marks the boundary at causal closure / Tenet 3). No editor-vocabulary leaked into prose.

### Medium Issues Found
None. The five previously-unrealized frontmatter concept relationships were resolved with inline links in the 2026-05-26 pass. `knowledge-argument` remains a `related_articles`-only link (forcing the Mary case inline would be filler — agreed).

## Optimistic Analysis Summary

### Strengths Preserved (unchanged — do not edit)
- Front-loaded thesis: "Supervenience describes a pattern; it does not explain it."
- Clean weak/strong/global three-grades taxonomy.
- Kim-exclusion treatment integrating the quantum-indeterminacy response, relocating the disagreement to causal closure.
- "Mutual constraint" framing and "determination-without-explanation is not ontological parsimony" (Occam's-tenet connection).

### Enhancements Made
None (deliberately — see Disposition). Length is 1481 words, 59% of the 2500-word soft threshold; no length action needed.

## Remaining Items
None.

## Stability Notes
The article reached stability in the two 2026-03-24 reviews, was confirmed at 62 days by the 2026-05-26 staleness pass, and is re-confirmed here at 30 days unchanged. These bedrock disagreements must NOT be re-flagged as critical in future reviews:
- Dennett-style deflationism about the explanatory gap is a framework-boundary disagreement, not a fixable flaw.
- The zombie conceivability debate is acknowledged; type-B physicalism is engaged with a Mode-Two reply.
- "Physicalists disagree with dualism" is not a critical issue.
- The Kim-exclusion disagreement is relocated to causal closure (Tenet 3) — a genuine boundary, honestly marked, not slippage.

Calibration note: this is a metaphysics article about a logical relation, not an empirical-consciousness-attribution article, so the minimal-organism possibility/probability slippage risk does not arise.

**Future-review guidance:** this article now has 4 prior reviews and is convergence-damped. It should not be re-selected by staleness unless its body actually changes (`ai_modified` > `last_deep_review` driven by a real content edit, not a cross-link bump in another file). A fifth no-op pass would be pure churn.