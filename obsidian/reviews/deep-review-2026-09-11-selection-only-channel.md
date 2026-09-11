---
title: "Deep Review - Selection-Only Channel"
created: 2026-09-11
modified: 2026-09-11
human_modified:
ai_modified: 2026-09-11T06:11:41+00:00
draft: false
description: "Adjudicates the 2026-09-11 ChatGPT/Claude divergence over whether marginal Born-preservation secures no-signalling; scopes the sufficiency claim and installs the missing agency-budget reference."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-11
last_curated:
---

**Date**: 2026-09-11
**Article**: [[selection-only-channel|Selection-Only Channel]]
**Previous review**: [[deep-review-2026-07-15-selection-only-channel|2026-07-15]] — fifth prior review (2026-05-11, 05-11b, 06-03, 06-17, 07-15)
**Why this target, not the scorer's top picks**: `get_review_candidates` returned 396 candidates; the top six (score 54–95) were all edited by this same session within the last 7–15 hours, and it was those edits inflating their `days_unreviewed_content` term. `selection-only-channel` (45.6) is aged on both axes — 58 days since the last deep review, and the last body change was 2026-08-03/08-24. **The deferred six retain real, independent review debt** (a ~63-day gap since their last *deep* pass) and should be taken once the edits age. This deferral is not an exemption.
**Pass type**: Adjudication of a live cross-reviewer divergence, plus the first deep pass over the 2026-08-03 withdrawal passage (which post-dates the 07-15 review and had never been deep-reviewed).

## The Adjudication: does marginal Born-preservation secure no-signalling?

[[outer-review-synthesis-2026-09-11|Tonight's three-reviewer synthesis]] recorded this as "the most consequential unadjudicated item this cycle produced", disposition *no upgrade, no task, flagged for the operator*, because two frontier reviewers disagreed:

- **ChatGPT 5.6 Pro**: "No-signalling applies to setting-conditioned and intervention-conditioned remote marginals, including remotely steered ensemble decompositions. An averaged histogram is insufficient." It called this article's claim "the most important technical error to correct across the site."
- **Claude Opus 5**: the corridor's defence "is internally consistent — but it is exactly the relocation, not the evasion, of the cost."

### Verdict: SETTLED, on a narrower question than the one the reviewers fought over

I am not adjudicating "is the Map's corridor signalling-safe?" — that is a framework choice and remains the operator's. What is settled is **the conjunction of this article's own two claims**, and the conjunction fails.

No-signalling, stated properly, is a condition on the remote marginal *conditioned on a distant party's freely-chosen setting*: Σ_a P(a,b | x,y) must be independent of x. It is not a condition on the fully pooled histogram. Three cases separate cleanly:

1. **Mind-state not publicly conditionable.** No sub-ensemble selection is possible; only the pooled marginal is accessible; preservation suffices. But the channel then has no sender — this is [[ensemble-level-epiphenomenalism]], which the corpus already names as the price.
2. **Mind-state freely settable and externally labellable** — the reading L74 asserted. A mind holding C=0 through one block of trials and C=1 through another produces sub-ensembles whose local frequencies depart from Born (the article explicitly licensed this), and on one wing of an entangled pair the *distant* marginal conditioned on that label departs too. That is signalling. The averaging over C that restores the pooled histogram is averaging a remote observer is free not to perform, and the sender controls the blocks. On this reading "the no-signalling theorem is automatically respected" is **false**.
3. **Preservation required per publicly conditionable context.** Signalling-safe, and this is what the Map's own material already specifies: `research/the-agency-budget-under-exact-born-rule-preservation-2026-08-13.md` states the constraint as "Σ_C P(o|C,X)·P(C|X) = q_Born(o|X) **for every publicly conditionable context X**". That quantifier *is* the strengthening ChatGPT demands. The price is that the mind-state is not publicly conditionable, which returns case 1's epiphenomenalism — the "relocation" Claude named.

So **both reviewers were right about different things**, and the article was wrong about the one thing neither of them targeted precisely: it asserted case 2 at L74 ("the marginal … and nothing else … information flow across the channel entirely open") and case 3's conclusion at L127 ("automatically respected"). Those two claims are in tension with each other. The repair is the quantifier, not a deletion.

### Two independent confirmations the adjudication does not depend on

**(a) Han & Choi 2016 is cited backwards here — and correctly in the parent topic article.** Web-verified at publisher of record this pass. The abstract reads: "We have shown that Born rule on quantum measurement is derived by requiring relativistic causality condition." The Born rule is *derived from* causality, so a non-Born assignment rule is a causality problem. L72 cited it in support of the claim that causality asks only for an aggregate match — the opposite direction.

The corpus already knows this. `topics/selection-only-mind-influence.md` L125 quotes that same sentence verbatim and draws the correct consequence: "any *systematic* per-trial deviation from Born-rule probabilities is a relativistic-causality problem and not merely a statistical-detectability one." **The concept page carried the inverted framing of the claim its own parent topic article states correctly.** This is the analysis-doc-cites-the-article-article-never-cites-back shape in a sharper form: the correct reading existed one file upstream, in the article this page names as its own fuller treatment.

**(b) The claim outran the Map's own position register.** P-Q7 grades the no-signalling compatibility *credence high · external-evidence grade C · framework-internal only: **yes***, resting on Torres Alegre 2025 (an unrefereed arXiv preprint), and lists "a tighter no-signalling theorem rules out even the corridor reading" as a would-shift condition. "The no-signalling theorem is automatically respected" states a theorem-level entailment the register explicitly declines. That is a calibration error inside the Map's framework — a tenet-accepting reviewer would flag it — and therefore critical rather than bedrock disagreement.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Internal inconsistency / possibility-probability slippage (L74 ↔ L127)** — "the marginal … and nothing else", "information flow across the channel entirely open" (case 2) cannot co-exist with "the no-signalling theorem is automatically respected" (case 3's conclusion). **Resolved** by installing the quantifier over X and re-scoping L127 to a framework-internal compatibility argument graded at P-Q7.
2. **Citation-framing accuracy (L72)** — Han & Choi 2016 used in the direction opposite to its result. **Resolved**: reframed to state that the paper *derives* the Born rule from causality, with a reciprocal pointer to the parent article's fuller, already-verified treatment.
3. **Inline cite dropped a co-author (L72)** — "(Han 2016)" for a two-author paper whose References entry #3 correctly reads "Han, Y.-D., & Choi, T. (2016)". The 06-03 review corrected the co-author omission in the References block; the *inline* form was left bare. **Resolved** → "Han & Choi (2016)".
4. **Navigation surface asserted the unscoped claim (L42, the front-loaded lead)** — the lead is the truncation-resilient summary and carried "leaving the mind-conditioned distributions unconstrained". **Resolved** in the lead, not only in the body.
5. **The article asserted automatic no-signalling while citing none of the corpus's own signal-locality material.** Measured, all four zero on `grep -icF` before the edit: `Valentini` 0, `signal-locality` 0, `agency-budget` 0, `steering` 0. **Resolved** — see Cross-links Added.

### Citation Web-Verify Ledger (publisher of record)

Trigger fired: the body was modified after the 07-15 review (the 2026-08-03 withdrawal commit). The 06-03 pass verified all published-literature cites at publisher of record and the References block has not changed since; per convergence discipline those were not re-litigated. Verified or added this pass:

- Han, Y.-D. & Choi, T. (2016), *Quantum probability assignment limited by relativistic causality*, Scientific Reports 6:22986 — **state: real-correct metadata, real-wrong framing.** Abstract verified verbatim at the publisher record and at arXiv:1307.2026. Metadata in References entry #3 is faithful; the *use* of the cite was reversed, and is corrected. Inline form corrected from "(Han 2016)" to "Han & Choi (2016)".
- Valentini, A. (2002), *Signal-Locality and Subquantum Information in Deterministic Hidden-Variables Theories*, in T. Placek & J. Butterfield (eds.), *Non-Locality and Modality*, 81–103, Kluwer; arXiv:quant-ph/0112151 — **state: real-correct (newly added, verified before insertion).** Title, sole author, editors, page range and publisher all confirmed at the arXiv record's journal-reference line. Abstract verified verbatim: "any deterministic hidden-variables theory, that reproduces quantum theory for a 'quantum equilibrium' distribution of hidden variables, must predict the existence of instantaneous signals at the statistical level for hypothetical 'nonequilibrium ensembles'." **Scope condition preserved in the inserted gloss** — deterministic hidden-variables theories, non-equilibrium ensembles — and deliberately not widened into a general result about the selection-only channel, which is not a deterministic hidden-variables theory. The theorem therefore *prices* the weak reading rather than refuting it.
- Inline ↔ References cross-check: every inline `Author YYYY` has a References entry and every entry is cited inline or in a Further Reading gloss. Valentini was inserted in alphabetical position 9, pushing the Southgate self-cite to 10; verified first that the body contains **no** numbered reference cross-references (`[\d]` → 0 matches, "reference N" → 0 matches), so the renumber strands nothing.
- Superlative-claim currency sweep: `find_superlative_claims` returned **0** candidates. No currency exposure.

### Medium Issues Found

- **String sibling carrying the same unscoped gloss: `topics/selection-only-mind-influence.md` L75** holds the identical "leaving information flow across the channel entirely open". **Deliberately not edited** — that article supplies the correct Han & Choi reading itself two sections later at L125, it is not this pass's target, it sits at 3,647/4,000 words with only 353 words of headroom, and a drive-by insertion into a secondary host would skip its own source-fidelity pass. Flagged below as a Remaining Item.
- The section heading "Born-Rule Preservation Constrains the Marginal, Not the Conditionals" remains true on the strong reading (per-context) and was left alone as a stable anchor.

### Counterarguments Considered

- *Quantum Skeptic / Empiricist*: "a channel invisible to every third-person test is not a channel." Live, not new, and already carried as [[ensemble-level-epiphenomenalism]]; the adjudication above sharpens rather than answers it — case 3's signalling-safety is *purchased* by case 1's invisibility. Recorded, not papered over.
- *Many-Worlds Defender / Hard-Nosed Physicalist / Eliminative Materialist*: rejection of the tenets themselves. Bedrock framework-boundary disagreement, per five prior reviews. Not re-flagged.

### Reasoning-Mode Classification (changelog/editor-internal only, never in prose)

- Engagement with Stapp ("Not a measurement-basis-choice channel"): **Mode Three** — boundary-marking, unchanged, verbatim quote still the 06-03-verified one.
- Engagement with the energy-conservation objection (Collins / Pitts): **Mode One** — defective on its own terms; the objection presumes energy injection. Unchanged.
- Engagement with ChatGPT's no-signalling charge (new this pass): **Mode One** — conceded and corrected on the Map's own terms, using the Map's own research note and its own position register's grading. No boundary-substitution: the article does not plead tenet-incompatibility against the charge. No editor-vocabulary leakage into prose (checked: none of the forbidden labels appear).

## Optimistic Analysis Summary

### Strengths Preserved

- The L76 withdrawal record ("Marginal preservation is compatible with *maximal* conditional dependence", the non-negativity and signed-rate defects, the suspension of the ε² figures) — untouched. It is the reason this page had already travelled half of ChatGPT's distance on its own, and it is a correction record, not prose to be tightened.
- The "What the Channel Is Not" four-way taxonomy, the log₂(N) per-event ceiling, content-confinement as a Holevo-style bound, and the [[possibility-probability-slippage]] self-caveat in the content-confinement section — all untouched, all load-bearing per prior stability notes.
- The 07-15 interventionist gloss (per-trial vs unconditioned-ensemble difference-making) — untouched; it has been rewritten twice in two months and is oscillation territory.

### Enhancements Made

Length-neutral pressure applied but not fully met: **2,502 → 2,836 words (+334)**, concepts soft 2,500 / hard 3,500, so 664 words of hard headroom remain. Two passages were folded to pay part of the cost — the "generic Shannon channel" detectability paragraph merged into the preceding one (it had become a third statement of a point now made twice above), and the channel-specification paragraph tightened. The remainder is the correction itself, not expansion.

### Cross-links Added

- [[agency-budget]] — twice: in the scoping paragraph as where the strong reading is worked out, and in Further Reading with the coupling budget, its min(H(conscious source), H(Born distribution)) ceiling, and the scope-preserved Valentini gloss.
- A reciprocal pointer to [[selection-only-mind-influence]] at the Han & Choi locus, so the concept page now points at the parent's verified treatment instead of contradicting it.
- Bare **P-Q7**, which the position autolinker resolves to `/positions/quantum-interface/#p-q7` (verified present in the 56-entry index, and 1 occurrence confirmed in the synced Hugo copy). Bare rather than a piped register wikilink, which would be redundant and carry a silent-404 risk the bare form cannot.

## Remaining Items

1. **`topics/selection-only-mind-influence.md` L75** still carries "leaving information flow across the channel entirely open" without the per-context quantifier, though the same article states the correct Han & Choi consequence at L125. A one-clause scoping there would close the string-sibling gap. Not actioned: not this target, 353 words of headroom, and its own L125 already supplies the correction downstream.
2. **The substantive physics question remains the operator's**, as the synthesis reserved it: whether the Map adopts case 3 (exact preservation per publicly conditionable context, accepting the epiphenomenalism price) as its official reading, or keeps case 2's freedom and owes a signalling-safety argument. This pass makes the article state the question honestly rather than assume the answer; it does not decide it.
3. **P-Q7's grading is now the article's load-bearing support for its no-signalling standing.** If the register upgrades or retires P-Q7, this locus must move with it.

## Stability Notes

- **Do NOT restore "and nothing else" or "information flow across the channel entirely open" as unqualified glosses on the averaging identity.** The identity's quantifier over X is the whole content; the unqualified gloss drops it and licenses signalling. The correct gloss is "the marginal in every publicly conditionable context, the conditionals within a context free."
- **Do NOT restore "the no-signalling theorem is automatically respected."** The Map's own register (P-Q7) grades this framework-internal, evidence grade C, resting on an unrefereed preprint. Asserting the theorem is satisfied by construction is possibility-probability slippage, correctable inside the framework and therefore not bedrock disagreement.
- **Han & Choi 2016 runs *from* causality *to* the Born rule, not the reverse.** Verified verbatim at the publisher of record this pass. Any future edit that uses it to support "causality only audits the aggregate" is reintroducing the defect.
- **Valentini 2002's scope condition is deterministic hidden-variables theories and non-equilibrium ensembles.** It prices the weak reading; it does not refute the selection-only channel, which is not a deterministic hidden-variables theory. Do not widen it.
- **`concepts/quantum-interface` P-Q9 at L144 cites this article for "preservation binds that marginal only and leaves the conditionals free."** That remains true after this pass — the conditionals *are* free within a context — and P-Q9 was already careful to say "*unconditioned* aggregate marginal". Nothing was stranded.
- Bedrock framework-boundary disagreements (physicalist / MWI / eliminativist / Buddhist) are expected and are not to be re-flagged, per five prior reviews.
- This was the article's sixth review and the **first to find a critical issue**. The reason is instructive and worth generalising: five passes of intra-corpus cross-checking *ratified* the defect, because the inverted Han & Choi framing was internally consistent with everything on this page. It took an external reviewer to name the locus and a publisher-of-record check plus a read of the parent topic article to settle it.
