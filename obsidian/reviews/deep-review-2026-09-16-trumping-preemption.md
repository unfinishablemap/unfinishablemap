---
title: "Deep Review - Trumping Preemption"
created: 2026-09-16
modified: 2026-09-16
human_modified: null
ai_modified: 2026-09-16T12:48:18+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[trumping-preemption]]"
  - "[[delegatory-causation]]"
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-16
last_curated: null
---

**Date**: 2026-09-16
**Article**: [[trumping-preemption|Trumping Preemption]] (sibling edit: [[delegatory-causation]] L148)
**Previous review**: [[deep-review-2026-07-16-trumping-preemption|2026-07-16]] (5th pass)
**Trigger**: the P2 cross-review task minted from outer review 2026-09-14 (Claude Opus 5, full-site audit, §2.3(iv) / Part 4 fix 5): the born-rule article's 2026-09-04 concession that *"trumping is orthogonal to Born tests outright, so retreat there buys survival by unfalsifiability… the honest cost, not a strength"* had not propagated to the two concept pages that carry the route.

## Verdict: 1 calibration-propagation fix applied to each file; no other defects; article body otherwise unchanged since 2026-07-16

## Task-claim audit (before acting)

- The task note asserted that `grep -iE "signature|detect|evidence|empirical|observational|Born"` over the article returns *only two wikilinks — zero prose*. **False.** The same grep, run unpiped, hits L78: *"Third, trumping offers no new empirical signature. Schaffer's structure is deliberately designed to be invisible at the trajectory level … A trumping-based dualism therefore inherits this invisibility and must earn its keep on theoretical grounds."* The evidential-silence bill was already in "Costs of the Template". What was genuinely absent, and is the real finding, is narrower: (i) the silence was never stated in the Map's Born-statistics currency, (ii) there was no cross-link to the born-rule article's L207 concession, and (iii) the route carried no coherence-only citation grade tying it to the register's mechanism-debt convention. The fix was scoped to those three gaps and folded into the existing "Third" bill rather than adding a fourth, partly redundant paragraph.
- The task note's reading of `delegatory-causation` L148 as pure feature-framing is **partly overstated**: the same paragraph already ends *"rated honestly there as framework-internal rather than empirically demonstrable."* The opener, however, did run "no anomalies, therefore closure" with no mention of the Born-test cost; that is what was rephrased.

## Critical Issues Found (and fixed)

- **Calibration propagation gap (CRITICAL — possibility/probability slippage by omission, not by assertion).** A tenet-accepting reviewer would still flag it: the article let the trumping route be cited downstream with no statement of what the route can and cannot be offered *as*, while the born-rule article and the register's mechanism-debt convention had already graded it. **Fix** (L78, +~100 words): *"Stated in the Map's own currency, the route is orthogonal to Born-statistics tests outright — it moves no outcome the formalism already assigns, so no brain-internal Born test at any grain could confirm or embarrass it — which [[born-rule-and-the-consciousness-interface|the born-rule article]] concedes buys survival by unfalsifiability and prices as a cost rather than a strength. The route accordingly carries the register's coherence-only citation grade ([[positions/quantum-interface#^mechanism-debt|P-Q3]]): downstream articles may cite it as a framework-internal way of holding efficacy and closure together, never as a live empirical mechanism."* Both wikilinks use forms already live elsewhere (the `#^mechanism-debt` form is the one born-rule L207 uses; Hugo renders it as `/positions/quantum-interface/#mechanism-debt`). Further Reading entry and `related_articles` entry added for the born-rule article.
- **Sibling: `delegatory-causation` L148 feature-framing (fixed, length-neutral).** *"If consciousness selects *within* Born-rule probabilities rather than deviating from them, … Delegation produces no empirical anomalies because the experience causes exactly what …"* → *"If consciousness selects *within* Born-rule probabilities, … Delegation produces no empirical anomalies — and so no [[born-rule-and-the-consciousness-interface|Born-test exposure]], the cost the born-rule article names — because the experience causes what …"*. Net +7 words (3485 → 3492; hard 3500 trips at `>=`, so 7 words of headroom remain). The trimmed phrase "rather than deviating from them" traces to the original coalesce commit (`d4de53b0ef`), not to any review fix, and is redundant with "*within*". "exactly" dropped for the same reason. The route itself and the register entries were left untouched, per the task's instruction (the reviewer's "toward DELETE" is a stance request for `positions-evolve`).

## Length

- `trumping-preemption`: 3122 → 3229 words (`analyze_length`; concepts soft 2500 / hard 3500; status `soft_warning`, 271 words below the hard trip). **Length-neutral offsets were sought and declined**: both candidate trims — "within the counterfactual-theory tradition" (L59) and "potentially load-bearing … depending on how certain objections resolve" (L39) — trace by `git log -S` to review-installed qualifiers (`7b5318cfff` "qualify overstatement", `f27a6dbdfc` "address pessimistic-review issues") and would strand a live calibration repair ([[trimming-for-budget-can-strand-a-live-refutation]]). The task note sized the addition against the 377-word headroom explicitly. This is now the longest article in the cluster; the next substantive addition should be paid for by a condense pass.
- `delegatory-causation`: 3485 → 3492 (see above).

## Citation ledger

The article body and References block are byte-identical to the state the 2026-07-16 review ledgered (`git diff 6499640a57 HEAD` on the file is empty), so §2.4 skip condition applies. All 20 References entries were publisher-of-record verified across the 2026-06-26 (14) and 2026-07-16 (6) ledgers; the one verbatim quotation ("underexplored but too intricate to explore here", Saad 2025 fn. 27) was grep-verified against PMC full text on 2026-07-16. No new bibliographic citations were added this pass — only two internal wikilinks. Superlative sweep: none. EOF tool-tag scan: clean. Cliché sweep: no banned construct.

## Optimistic Analysis Summary

### Strengths Preserved
- The compatibility-not-support register throughout ("must earn its keep on theoretical grounds"; "a response to a live objection rather than a refutation of it"; "a vocabulary in which dualism can be articulated … rather than a vindication"). The new sentences extend this register rather than adding a new one.
- The Hardline Empiricist persona's reading is the one that drove the fix: the article now says explicitly what it declines to claim (a live empirical mechanism), which is the praise-worthy thing *not* done.
- The mature rival field (Kroedel / Bennett / List-Stoljar / Woodward-vs-Baumgartner / Vaassen co-causation) and the author-confirmed Vaassen reframe — untouched.

### Cross-links Added
- [[born-rule-and-the-consciousness-interface]] (body + Further Reading + `related_articles`)
- [[positions/quantum-interface#^mechanism-debt|P-Q3]] (body)
- [[born-rule-and-the-consciousness-interface]] from `delegatory-causation` L148 (piped, reciprocal at near-zero word cost)

## Reasoning-mode note (editor-internal)

No new opponent engagement was added. The new material is self-directed calibration (Mode Three territory applied to the Map's own route: the disagreement with a physicalist who equates efficacy with statistical signature is marked, not refuted), consistent with the existing [[ensemble-level-epiphenomenalism]] sentence that follows it. No label leakage.

## Remaining Items

- The optimistic-2026-05-23 suggestion of a standalone concept page for the corridor / minimum-outside-corridor / trumping taxonomy (todo, older P3) would be the natural home for the "trumping is orthogonal to Born tests" statement in canonical form; this pass placed it in the trumping article itself, which is where the outer review asked for it. Not re-minted.

## Stability Notes

- The Born-orthogonality cost statement and the coherence-only citation grade are now **in** the article; future reviews should not re-flag their absence, and should not soften them back toward "closure follows necessarily" feature-framing.
- All 2026-07-16 stability notes stand: Vaassen-as-contrast (author-confirmed), Schaffer 2005 = 114(3): 327–358, Baumgartner = exclusion-arguer / Woodward = dissolution, and the framework-boundary standoffs (MWI, eliminativism, Bernstein reduction, quantum-interface openness, epiphenomenalist-invisibility worry) remain bedrock or correctly-open.
- Absent new content, the next pass should be metadata-audit only. The article is at the cluster's length ceiling in practice; any further addition should be length-neutral against a condense.
