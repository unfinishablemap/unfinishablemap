---
title: "Deep Review - Type-Token Causation"
created: 2026-08-03
modified: 2026-08-03
human_modified:
ai_modified: 2026-08-03T09:51:20+00:00
draft: false
topics: []
concepts:
  - "[[type-token-causation]]"
related_articles:
  - "[[deep-review-2026-07-11-type-token-causation]]"
  - "[[deep-review-2026-06-03-type-token-causation]]"
  - "[[deep-review-2026-05-11b-type-token-causation]]"
  - "[[deep-review-2026-05-11-type-token-causation]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-03
last_curated:
---

**Date**: 2026-08-03
**Article**: [[concepts/type-token-causation|Type-Token Causation]]
**Previous review**: [[deep-review-2026-07-11-type-token-causation|2026-07-11]]
**Word count**: 2,976 → 3,022 (+46)
**Mode**: Length-neutral (121% of 2,500 soft; hard 3,500, ~478w headroom). ~103w added, ~57w trimmed.

## Verdict

**Not a no-op.** The July review closed with "do not re-pick on a mechanical cross-link timestamp bump; only genuine own-content change warrants a fifth pass." Git-verified: genuine own-content change occurred. Commit `9bacbc1dd` (2026-08-03 08:17, the zero-MI / ε²-per-trial withdrawal sweep) rewrote the third detection-problem response, replacing the withdrawn `ε²/(2 ln 2)` per-trial bound with the surviving `log₂(N)` ceiling plus a new sentence stating that Born-preservation constrains **the unconditioned long-run marginal only** and that the tests bearing on token selection are **conditional residual-structure tests, not generic Born-frequency tests**.

That new sentence is correct — it matches [[selection-only-mind-influence]] (L35, L61, L145) and [[apex/born-preserving-causal-efficacy]] (L85, L89, L93) verbatim in substance. But the sweep was **file-partial in the classic way** (`fix-by-file-leaves-string-siblings-live`): it fixed the paragraph it was pointed at and left four older passages elsewhere in the same file asserting the *superseded stronger* reading — Born-preservation at every grain, undetectability by any frequency experiment. The result was a live internal contradiction inside one article. Fixed this pass. A fifth, separately-caught contradiction (type/token slip in the Kim-locator bullet) was also found and fixed.

## Pessimistic Analysis Summary

### Critical Issues Found

**C1 — Internal contradiction: unconditioned-vs-conditioned grain (4 loci).** The article's new L129 sentence says conditional residual-structure tests *are* where token selection is empirically exposed. Four older passages said the opposite:

- L83 (was): *"Run the same brain a thousand times under the same physical conditions, and the statistical distribution of outcomes matches Born-rule predictions. No experiment measuring frequencies will detect the conscious selection."* — This describes a **conditioned** ensemble (same brain, same conditions) and asserts Born-matching in it. That is horn (b) of the [[born-preserving-causal-efficacy|trilemma]] chosen *by stipulation* — precisely what that article says the Map deliberately does not do ("The register's default reading commits to preservation of the *unconditioned* long-run marginal… That commitment is weaker than it first looks, and deliberately so: it leaves the per-subject and per-intention conditionals formally unconstrained, which keeps horn (a) live"). **Resolution**: rewritten to aggregate over the natural run of conscious states, with the mind-conditioned question explicitly left open and routed to `born-preserving-causal-efficacy`.
- L91 (was): *"conscious selection operates on tokens, not types; experiments measure types. The two never collide."* — "never collide" forecloses horn (a). **Resolution**: rewritten to scope the closure-grounding experiments to unconditioned type-level frequencies.
- L121 (was): *"invisible to any experiment that measures statistical regularities."* **Resolution**: qualified to *unconditioned* statistical regularities.
- L139 (was): *"produces no type-level effect — Born-rule statistics are preserved exactly."* **Resolution**: scoped to the unconditioned long-run marginal, with the grain-restriction of the commitment stated explicitly.

Structural fix installed once at the type-level *definition* (L67) so downstream uses inherit it: *"Which population is aggregated over matters… Below, 'type level' unqualified always means the unconditioned grain."* The lead was also qualified ("the unconditioned type-level Born-rule statistics") so a truncation-resilient reader gets the correct grain.

**C2 — Type/token slip in the Kim-locator bullet.** L89 read: *"The exclusion argument is sound wherever physical causation is type-level sufficient. It fails wherever physical causation is type-level sufficient but token-level open."* Both sentences used the same antecedent to reach opposite verdicts. Kim's argument is sound where physical causation **fixes the token outcome**; it fails where causation is type-sufficient but token-open. Survived four prior reviews. **Resolution**: first sentence rewritten to "wherever physical causation fixes the token outcome."

### Medium Issues Found
- Redundant restatement of the apparent-causal-role clause across the phenomenal-concept section's second and third paragraphs — tightened (−36w), also retiring one `load-bearing` intensifier per the style guide's overused-words rule.
- Detection-problem closing paragraph restated L131 — tightened (−13w).
- Apex/concept deployment paragraph carried "same-day sibling anchors… at their respective deployments" filler — trimmed (−8w). (`hub-articles-accrete-crosslink-length`.)

### Counterarguments Considered
Popperian (unfalsifiability), MWI branch-counting, IIT identity thesis, eliminativist "naming is not explanation" — all four carry over as bedrock from prior reviews, unchanged and not re-flagged. The C1 family is **not** bedrock: it is an intra-framework calibration/consistency error a tenet-accepting reviewer would flag, and it fails the §2 diagnostic test in the correctable direction.

## Citation Web-Verification

**Targeted re-affirm, not a full re-run — reason stated.** The References block is byte-identical to the 2026-07-11 state, which carried a complete publisher-of-record per-cite ledger for all ten external cites. Today's body change introduced **zero new external citations** (one internal wikilink only). Spot-verification of the two most drift-prone entries:

- Saad, B. (2025). "A dualist theory of experience." *Philosophical Studies*, 182(3), 939–967 — **real-correct** (OpenAlex on DOI 10.1007/s11098-025-02290-3: Bradford Saad, Oxford; vol 182, pp. 939–967). OpenAlex records the issue as "3-4" (double-issue merge, a known aggregator artifact); the July pass verified 182(3) at Springer, so the published value stands unchanged — aggregator metadata does not override a publisher-verified field (`quote-aggregator-ratification-corrupts-verbatim`).
- Yablo, S. (1992). "Mental causation." *Philosophical Review*, 101, 245–280 — **real-correct** (OpenAlex on DOI 10.2307/2185535: Stephen Yablo, *The Philosophical Review* 101, first page 245).

Remaining eight (Davidson 1970, Frankish 2016, Kim 1998, Kim 2005, Loar 1990, Macdonald & Macdonald 1986, Papineau 2002, Peirce 1906) — ledger carried forward unchanged from the 2026-07-11 publisher-of-record pass, 23 days old, References untouched since. Inline ↔ References cross-reference re-checked: complete, no orphans either direction.

Note: WebSearch budget was exhausted session-wide; verification ran through OpenAlex via WebFetch (`webfetch-survives-websearch-exhaustion`).

## Currency Sweep
Superlative-claim detector returns empty. Structural concept page; no empirical-record superlative to age-check.

## Internal Cross-Reference Verification
- IIT in-body quote (L81) re-grepped against the live sibling: matches `topics/consciousness-and-integrated-information` L80 verbatim. No stale internal-quote channel.
- `probability-objections-many-worlds` → `probability-problem-in-many-worlds` retarget (from commit `112b81e9f`) verified: old slug is in `archive/concepts/`, new slug is live at `topics/`. Retarget correct.
- All body wikilinks resolve on disk; `born-preserving-causal-efficacy` unambiguous (single match, `obsidian/apex/`). Added to `related_articles`.
- `topics:` field is bare-slug canonical (fixed earlier today by `a94351c33`) — no path-prefixed entries.

## Reasoning-Mode Classification (editor's notes — not in article body)
Carried forward and re-confirmed against the current body: Kim — Mode One. Bohmian — Mode Three. Phenomenal-concept strategy (Loar/Papineau/Frankish) — Mixed. MWI — Mode Three. Popperian — Mode Three. No editor-vocabulary leakage (grep clean). No "This is not X. It is Y." cliché.

## Optimistic Analysis Summary

### Strengths Preserved (do not change)
- Front-loaded lead locating Kim's failure point in sentence three.
- Bohmian pilot-wave caveat — in-framework honesty of a quality the corpus should copy.
- Phenomenal-concept alternative section — names the leading rival, gives two specific preference reasons, and declines to claim incompatibility.
- Popperian cost-owning paragraph (L131) — untouched.

### Enhancements Made
- Grain distinction (unconditioned vs conditioned) installed once at the definition and inherited throughout — the article now says the same thing about Born-preservation in five places instead of two contradictory things.
- Empirical exposure now stated positively ("where the framework's empirical exposure actually sits") rather than denied, aligning the concept page with the apex programme article that carries the argument.

### Cross-links Added
- [[apex/born-preserving-causal-efficacy]] (frontmatter `related_articles` + second body reference at L83).

## Remaining Items

None for this article. **Corpus-level follow-up worth noting, not minted** (no open todo task targets this file; see `outer-review-same-file-task-pileup` for why not to pile on): the `9bacbc1dd` sweep's locus list was derived from carriers of the *ε² string*. This review found that the withdrawal has a second, larger footprint — passages asserting undetectability *at every grain* without ever mentioning ε². Those are invisible to a string-grep for the withdrawn formula. Candidate string families for a future sweep: "no experiment", "never collide", "invisible to any", "preserved exactly", "no type-level effect", searched across `obsidian/`, `hugo/content/`, and `archive/` (`defect-sweeps-must-include-archive-tree`).

## Stability Notes

Bedrock-disagreement entries carry over unchanged and must NOT be re-flagged as critical:
- IIT-theorist's identity-thesis defence — bedrock at framework boundary.
- MWI defender's branch-counting reply — bedrock at Tenet 4 boundary.
- Popperian on the directly-unfalsifiable central claim — bedrock at empirical-discipline boundary; the article owns the cost.
- Eliminative materialist's "naming is not explanation" charge — bedrock at tenet boundary.

**Convergence note:** four prior reviews called this article stable, and on its own former terms it was. What broke convergence was not drift in the article but a *doctrinal* change elsewhere (the Born-preservation grain restriction established by `born-preserving-causal-efficacy`) landing here through a string-scoped partial sweep. The lesson for future picks: a converged article stops being converged the moment a sibling withdraws a premise it quietly relies on, and the timestamp bump that signals it will look cosmetic. Do not re-pick this file on a further cross-link touch; do re-pick if `born-preserving-causal-efficacy` or `selection-only-mind-influence` revise their grain commitments again.
