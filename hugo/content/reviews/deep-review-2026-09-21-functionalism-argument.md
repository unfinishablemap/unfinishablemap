---
ai_contribution: 100
ai_generated_date: 2026-09-21
ai_modified: 2026-09-21 06:14:37+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-21
date: &id001 2026-09-21
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-21 06:14:37+00:00
modified: *id001
related_articles: []
title: Deep Review - Against Functionalism
topics: []
---

**Date**: 2026-09-21
**Article**: `obsidian/arguments/functionalism-argument.md` ("Against Functionalism")
**Previous review**: `deep-review-2026-07-18-functionalism-argument.md`; the substantive intervening pass is `pessimistic-2026-07-31-functionalism-argument.md`
**Outcome**: **NO-OP on the article.** No edits applied. `ai_modified` and `last_deep_review` deliberately **not** bumped.

## Budget

`analyze_length` (via `Path('obsidian/arguments/functionalism-argument.md')`): **3494 words**, soft 2500 / hard 3500, status `soft_warning`. The gate is `>=`, so the usable ceiling is 3499 — **five words of headroom**. Word count after this review: **3494, unchanged.**

Note for future passes: this article's prose is not bloated. `analyze_length` counts the reference apparatus, and this article carries a 12-entry Site Content list plus an 8-entry External Sources list. The soft-to-hard band is being consumed by apparatus, not argument (cf. `reference-apparatus-consumes-the-soft-to-hard-band`). `soft_warning` itself carries no consequence in this repo; crossing to `hard_warning` would mint a spurious condense task.

## Lenses Run

| Lens | Result |
|---|---|
| Quote fidelity (publisher of record) | **Clean** — see ledger below |
| Attribution accuracy (§2.5: misattribution, dropped qualifiers, position strength, source/Map separation, self-contradiction) | **Clean** |
| §2.4 cross-reference inline ↔ References | **Two orphans found** (only finding) |
| §2.4 empirical-record currency sweep | **Clean** — `find_superlative_claims` returns 0 |
| Falsifier discipline (`writing-style.md` L441, three negative states) | **Clean** |
| Tenet drift / propagation from `tenets.md` | **Clean** (no parent movement since `ai_modified`) |
| Prior-review issue discharge (pessimistic 2026-07-31, Issues 1–9) | **All nine discharged** |
| Bibliography convention vs `arguments/` siblings | Driver's flagged gap is a **false alarm** — corrected below |
| Label leakage (`direct-refutation-discipline` editor vocabulary) | **Clean** |

Lenses deliberately **not** re-run, per the driver's list: the six-philosopher persona critique (covered by `pessimistic-2026-07-31-functionalism-argument.md` and `pessimistic-2026-05-26-functionalism.md`), the cluster/composition lenses (`optimistic-2026-08-03`, `optimistic-2026-08-08`, `optimistic-2026-09-10`), and `tenet-check-2026-09-20.md`.

## Quote-Fidelity Ledger (the lens this slot was spent on)

Every source-attributed quoted term and closely-paraphrased span, verified at the publisher of record, not via a summariser.

- **Graziano (2024), "Illusionism Big and Small: Some Options for Explaining Consciousness", *eNeuro* 11(10), ENEURO.0210-24.2024** — state: **real-correct**. Verified by fetching the publisher full text (eNeuro, 141,334 characters of extracted text) and grepping the raw source rather than asking a summariser.
  - `"subtle end"` attributed to Graziano: **verbatim-supported.** The paper reads *"Subtle illusionism is necessarily true of all models in the brain and must be true of consciousness as well. The following hypotheses are consistent with this subtle illusionism."*
  - `"caricature"` preferred to `"illusion"`: **supported, with the article's rationale intact.** The paper reads *"In this context, it has been suggested that the term "caricature" might be a more apt descriptor of consciousness than "illusion" (Graziano, 2019)."* The suggestion is Graziano's own, self-cited to his 2019 book, and he then gives exactly the reason the article gives: *"the term seems to imply that there is nothing present and the brain has made a mistake."* The article carries no year on this clause, so there is no wrong-year defect.
  - `"the hard end"` where *"phenomenal properties have no referent at all"*: **supported.** The paper's **Hypothesis 2 is titled "Hard Illusionism"** — *"Hypothesis 2, Item 1 does not exist"*. ⚠️ A lowercase grep for `hard illusionism` returns **0** on this source; the term is capitalised in the heading. Do not conclude from a case-sensitive zero that the Map has invented the term. (Mirror of `narrow-grep-zero-is-not-proof-of-absence`; default to `grep -iF`.)
  - *"His attention schema theory is the developed implementation"* — **antecedent checked and correct.** The paragraph opens on Frankish, and a careless read would attach AST to him. "His" follows immediately after "Graziano (2024)" and AST is the paper's **Hypothesis 5**. No misattribution.
- **Carruthers, P. & Veillet, B. (2007), "The Phenomenal Concept Strategy", *Journal of Consciousness Studies* 14(9–10), 212–236** — state: **real-correct**. PhilPapers returned HTTP 403 and the author's own copy at `faculty.philosophy.umd.edu` fails TLS (hostname not in the certificate's altnames), so verification went via the **OpenAlex** record: authors *Peter Carruthers* and *Bénédicte Veillet*, year **2007**, volume **14**, title exact. The abstract confirms the paper is *"a defense of the strategy against [Chalmers'] argument"*, which licenses the article's clause *"dispute the explanandum it turns on."* OpenAlex carries no page range, so issue/pages rest on consistent corpus form across [concepts/phenomenal-concepts-strategy.md](/concepts/phenomenal-concepts-strategy/) L216 and [concepts/knowledge-argument.md](/concepts/knowledge-argument/) L207 — verified as *consistent*, not independently as *correct*.
- **Tallis, R. (2024), "Tallis in Wonderland: The Illusion of Illusionism", *Philosophy Now* 161, 58-59** — state: **real-correct**, and the previously-flagged defect is **discharged**. The 2026-07-31 pessimistic review's Issue 7 recorded an unlicensed modal upgrade at the then-L164 (*"certainly cannot"* against Tallis's hedged *"seems even less capable"*). The article now reads *"is even less likely to be able to generate the illusion of it"* — the recommended softening, applied. The passage remains correctly **unquoted** paraphrase pinned to the correct work and the correct issue (**161**), which is the state prior passes worked hard to reach. **Do not disturb it.**
- **Block, N. (1978), "Troubles with Functionalism"** — state: **real-correct**. The article's *"an entire population replicating a brain's functional structure"* and *"a billion people following rules"* match the canonical statement; SEP's *Functionalism* entry records Block stipulating *"the population of China (chosen because its size approximates the number of neurons in a typical human brain)"*.
- **Hardin, C. L. (1988), *Color for Philosophers*** — state: **real-correct**. SEP attributes to Hardin 1988 exactly this objection — inversion is empirically unlikely *"given certain asymmetries in our 'quality space' for color, and differences in the relations of color experiences to other mental states such as emotions (Hardin 1988)"*. The article's reply (*"one confined to a symmetric sub-space delivers it"*) matches the standard move SEP itself records, namely hypothetical creatures with *"perfectly symmetrical color quality spaces"*. The article's specific gloss *"discrimination times and similarity judgements"* is marginally more psychophysically specific than SEP's summary but sits inside paraphrase tolerance for *Color for Philosophers*.
- **Chalmers, D. — `"hard problem"` / `"easy problems"`** — state: **real-correct**. Correctly credited to Chalmers, and correctly kept distinct from the explanatory gap itself (see the origin-attribution note below).
- **Frankish, K. (2016) — *"as traditionally conceived"*** — state: **real-correct**; scope restriction preserved, which is the qualifier the 2026-07-31 Issue 2 was about.
- **Searle, J. (1980)** — state: **real-correct**. The Chinese Room, the Systems Reply, and Searle's internalisation move are all stated accurately, and the article now gives the standard rejoinder (the second, distinct system) rather than presenting Searle's half as decisive.
- **Jackson, F. (1982)** — state: **real-correct**, and the 2026-07-31 Issue 9 orphan is **discharged**: the knowledge argument is now used in the body at the phenomenal-concepts-strategy objection.

**Known failure shapes probed and not found**: no quote verbatim in the predicate but spliced in the subject; no quote attributed to the *replying* paper rather than the target; no over-concession tells (`no possible` / `cannot ever` / `in principle undetectable`) — the Tallis instance was the one such tell and it is already repaired.

## Critical Issues Found

### Two orphan inline citations (§2.4 step 5) — REPORTED, NOT FIXED (unaffordable)

Every inline `Author YYYY` must have a bibliographic entry. Two do not:

| Inline cite | Body | External Sources |
|---|---|---|
| `Graziano (2024)` (§The Illusionist Challenge) | 1 | **0** |
| `Carruthers and Veillet (2007)` (§"The Gap Is in Our Concepts, Not in Reality") | 1 | **0** |

Every other named author — Block, Chalmers, Searle, Jackson, Hardin, Tallis, Frankish — has an entry. These two are the article's only inline cites that carry an explicit year *and* lack one, so the defect is an internal inconsistency in the article's own apparatus rather than a stylistic choice.

**Both canonical forms are verified and ready to paste** (metadata confirmed this run, as per the ledger above):

```
- Carruthers, P. & Veillet, B. (2007). "The Phenomenal Concept Strategy." *Journal of Consciousness Studies*, 14(9–10), 212–236.
- Graziano, M. S. A. (2024). "Illusionism Big and Small: Some Options for Explaining Consciousness." *eNeuro*, 11(10), ENEURO.0210-24.2024.
```

**Why not fixed**: the two entries cost **~32 words** against a **5-word** budget. Funding them by trimming reviewed philosophical prose is the worse trade — this article's prose has been through nine-plus passes and apparent redundancy in it is repeatedly review-installed guard text. Deferred to a condense-then-cite task (minted).

**Rejected cheap variant, recorded so it is not re-proposed**: deleting the two years (`(2024)`, `(2007)`) would save 2 words and remove the orphan-*with-year* shape, matching the article's Hardin/Block/Searle convention. It is a bad trade — it does not supply the missing entries, it only hides the mismatch, and it destroys the cites' locating power. A net-negative-word variant that loses information is worse, not better (`my-replacement-variants-are-scored-on-length-alone`).

## Medium / Low Issues

- **Reverse orphan (low, defensible)**: `Hoel, E. (2026)`, arXiv:2512.12802, appears in External Sources but the body never names Hoel. Unlike the Jackson orphan the 2026-07-31 review flagged, this one is defensible: the list is headed *Further Reading → External Sources*, and the body does route to the Hoel material via `[[continual-learning-argument]]`. It is also correctly marked as a non-peer-reviewed preprint. No action recommended.

## Findings Outside This Article — Reported, Not Actioned

- **The Tallis *Philosophy Now* issue-number defect is still live at two loci**, 52 days after `pessimistic-2026-07-31` flagged it: `obsidian/topics/attention-and-the-consciousness-interface.md` L242 and `archive/topics/attention-schema-theory-critique.md` L209 both read *"Philosophy Now, 159"* where the verified issue is **161**. The reason it has not been executed is structural and worth noting: the finding is parked as sub-item (b) inside an **operator-gated `NEEDS-HUMAN` block** in `todo.md`, so no unattended pass will ever pick it up even though the item itself is explicitly marked *"NOT operator-gated and can ride any future pass"*. A cheap metadata fix is being held hostage by the gating of its host entry. **This article's own Tallis entry is correct (161, 58-59).**

## Driver Brief Corrections

The driver's pre-check (4) reported a *"VERIFIED gap"*: *"Of the 5 substantive `arguments/` articles, 4 carry a `## References` section and this one does not; it has 0 parenthetical year-citations against siblings' 1–5."* **Both legs are wrong, measured across the section:**

| File | Bibliography heading | Parenthetical year-cites |
|---|---|---|
| `epiphenomenalism-argument.md` | `## References` | 20 |
| `epistemological-limits-of-occams-razor.md` | `## References` | 23 |
| `many-worlds-argument.md` | `## References` | 25 |
| `materialism-argument.md` | `## References` | 16 |
| **`functionalism-argument.md`** | **`### External Sources`** | **11** |

The article **does** carry a bibliography — 8 full entries, nested one level under `## Further Reading` and headed `### External Sources` rather than `## References`. The "0 parenthetical year-citations" figure is a false zero. The live difference is a **heading name and nesting depth**, not a missing apparatus, so the driver's ~100-word cost estimate does not apply and the "do not attempt it" instruction was premised on a gap that is not there. What remains is the much narrower orphan-pair finding above. If heading harmonisation across `arguments/` is ever wanted, it is a near-word-neutral rename, not a new section.

## Checks That Came Back Clean (recorded so they are not re-run)

- **Origin-attribution (Levine vs Chalmers on the explanatory gap)**: clean, confirming the driver. `Levine` returns 0, but §"Argument 5: The Explanatory Gap" defers the origin through `[[explanatory-gap|explanatory gap]]` and credits Chalmers only with the *hard problem*, which is correct. This is an **uncredited** origin carried by a wikilink, not a **miscredited** one — materially different from the sibling defect repaired two iterations ago. Not a misattribution; do not report it as one.
- **Falsifier discipline** (`writing-style.md` L441, adopted 2026-08-18 — never previously applied here, since the last deep review predates it): **satisfied, and better than the minimum.** The checkable test targets an uncalibrated summary claim (*"none has occurred"* / *"none has been met"* and equivalents). The article makes **no such summary claim** — the lead-in is only *"The case against functionalism would be weakened if:"* — so there is no over-strong aggregate to calibrate. Each of the three falsifiers states its own negative state with a basis, and two are marked as **state 2 (a serious live countermodel stands)**, which is the honest and least flattering reading:
  1. *"a substantial body of opinion grants the first while denying the second... That position rejects Premise 3 rather than supporting the conclusion, and should not be recruited as support"* — state 2, and it explicitly declines to recruit opponents as allies.
  2. *"Current theories (Global Workspace, Higher-Order, IIT) correlate without explaining the transition from function to experience"* — nothing decisive has come in.
  3. *"The Map's verdict is that the bridge is not yet built—a verdict on a live programme, not a defeated one"* — state 2, live programme.
  ⚠️ **Literal probes for the discipline's canonical phrases will false-zero here**: all three states are expressed in natural wording, none of it lifted from the guide. Do not conclude from a zero-hit grep that the discipline is unapplied.
- **Possibility/probability slippage**: none found. The article is unusually disciplined about this — §"The Substrate May Matter" explicitly labels the Minimal Quantum Interaction material as *"the Map's rival hypothesis, which the functionalist need not accept"* and *"the most heavily contested claim in the framework"*, and the Conclusion table's third column marks Argument 4's substrate claim as *"framework"*. A tenet-accepting reviewer would not flag any claim as overstated relative to the five-tier scale.
- **Prior-review discharge**: all nine Issues from `pessimistic-2026-07-31` are addressed in the current text — the "devastating" regress verdict is gone and replaced with the corpus-settled framing (Issue 1); illusionism is now stated at Frankish's scope restriction and Graziano's subtle end (Issue 2); Argument 3's conclusion is narrowed to semantic properties with the extension marked *"a conjecture, not a corollary"* and the Systems Reply rejoinder supplied (Issue 3); the five-independent-confirmations framing is replaced by the dependency table (Issue 4); the phenomenal concepts strategy is engaged and both articles linked (Issue 5); the unsourced profession claim is gone (Issue 6); the Tallis modal upgrade is softened (Issue 7); the Hardin asymmetry objection is named and answered (Issue 8); Jackson is used in the body (Issue 9).

## Remaining Items

The orphan citation pair, deferred as a condense-then-cite task. Nothing else.

## Stability Notes

**This article has converged. Treat a no-finding pass here as the expected result.**

- The **modal-leg bedrock** is settled and must not be re-flagged: the conceivability→possibility bridge (Premise 3) is the article's most contested step, the article says so in its own voice three times, links `[[conceivability-possibility-inference]]`, and declines to claim the Chalmers dilemma closed the debate. Reviewers who reject the bridge are disagreeing at the framework boundary, not finding a defect.
- The **quantum-substrate claim** in §"The Substrate May Matter" is explicitly fenced as the Map's alternative, with decoherence named as the standard objection and both `[[decoherence]]` and `[[quantum-biology-and-neural-mechanisms]]` linked. A Tegmark-style objection here is bedrock, not a correctable issue. This fence was installed to answer the 2026-07-31 Quantum Skeptic critique; do not read its presence as an unanswered vulnerability.
- The **Tallis passage is at a hard-won equilibrium**: correct work, correct issue (161), correctly hedged consequent, correctly *unquoted*. It has flipped state twice already. Do not re-quote it, do not re-pin it, and do not re-harden the modal. The broader 47-locus quotation decision is operator-gated and is not this article's to make.
- The **length signal is an apparatus artefact**, not prose bloat. A future `hard_warning` on this file should be read as the reference apparatus crossing the line, and answered by rebalancing apparatus, not by cutting argument.
- **Do not mint a References section here.** The article already has one under a different heading.