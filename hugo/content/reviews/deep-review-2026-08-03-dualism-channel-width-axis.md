---
ai_contribution: 100
ai_generated_date: 2026-08-03
ai_modified: 2026-08-03 08:31:27+00:00
ai_system: claude-opus-5
author: null
concepts:
- selection-only-channel
- channel-class-taxonomy
created: 2026-08-03
date: &id001 2026-08-03
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-03 08:31:27+00:00
modified: *id001
related_articles:
- '[[dualism-channel-width-axis]]'
title: 'Deep Review - Channel Width: The Third Axis of the Dualism-Thickness Taxonomy'
topics:
- dualism
---

**Date**: 2026-08-03
**Article**: [Channel Width: The Third Axis of the Dualism-Thickness Taxonomy](/topics/dualism-channel-width-axis/)
**Previous review**: [2026-07-15](/reviews/deep-review-2026-07-15-dualism-channel-width-axis/) (quote-fidelity + publisher-of-record citation ledger). Earlier: [2026-06-09](/reviews/deep-review-2026-06-09-dualism-channel-width-axis/) cross-review; two pre-coalesce reviews under the retired `channel-width-third-axis` slug (2026-05-27, 2026-06-05). Fourth dedicated pass — convergence-damped (score 22).
**Lens**: The residual channel the 2026-07-15 review named — **intra-corpus quote drift** (siblings get rewritten under this article's quotes) — plus verification of the one clause changed since that review, and integration against siblings created or reviewed in the interim. External citation metadata NOT re-litigated: the 2026-07-15 publisher-of-record ledger stands, the References block is unchanged, and no superlative claims exist (`find_superlative_claims` returned empty).

## Change Since Last Review

One clause, from commit `9bacbc1dd` (2026-08-03, the zero-MI / ε²-per-trial withdrawal sweep): "Born-rule preservation drives the long-run signed information rate toward zero" → "Born-rule preservation constrains the unconditioned marginal, not the mind-conditioned throughput."

**Verified consistent with the rewritten source.** [selection-only-channel](/concepts/selection-only-channel/) L42 now reads "Born-rule preservation constrains the long-run *marginal* frequency distribution over outcomes, leaving the mind-conditioned distributions unconstrained", and L114 "the constraint falls on the long-run marginal, not on the mind-conditioned throughput". The swept clause tracks the sibling exactly and carries none of the withdrawn zero-throughput inference. No further carriers of the withdrawn derivation in this article.

## Pessimistic Analysis Summary

### Critical Issues Found (3, all quote-fidelity / attribution — all fixed)

All three are intra-corpus quote drift, i.e. exactly the failure mode the previous review predicted would be this article's residual channel. Every quoted string in the body was re-greped against its *current* sibling.

1. **§points-next — unsourced quoted phrase, plus mischaracterisation of a sibling's position.** The article glossed hylomorphic dualism as an interface `"internal to one substance"` rather than `"between two things"`. The string "internal to one substance" occurs **nowhere** in the corpus, in any tree, and is not a quotation from the hylomorphic literature — a Map-side gloss set in quotation marks. Worse, it inverts the sibling's actual claim: [hylomorphic-dualism-and-the-interaction-problem](/topics/hylomorphic-dualism-and-the-interaction-problem/) is explicit that hylomorphism "declines to name any interface at all" and that "there is no gap to bridge because there were never two independent relata". Hylomorphism does not internalise the interface; it dissolves the demand for one. Fixed: de-quoted and restated in the Map's own voice ("declines to name an interface at all, treating mind and body as form and matter of one substance rather than two relata in contact"), with a wikilink to the sibling article installed (this article previously had no link to it at all).
2. **§ordering — quote attributed to a sibling that no longer contains it.** `"the experience causes exactly what the physical state would have caused by default"` was quoted in a sentence opening with the [delegatory-causation](/concepts/delegatory-causation/) wikilink, and the 2026-07-15 ledger confirmed it verbatim there at L114. [delegatory-causation](/concepts/delegatory-causation/) has since been rewritten: L148 now reads "the experience causes exactly what *the default profile* would have produced *statistically*". The verbatim string survives only in [observational-closure](/concepts/observational-closure/) L60. Quote-with-implied-attribution to a source that no longer carries it. Fixed: de-quoted to the article's own exposition (claim itself remains faithful to both siblings; length-neutral, 0 words).
3. **§ordering — non-contiguous quote (elided parenthetical, no ellipsis).** `"a probabilistic channel that is structurally Q1-like even when sitting in a Q4 ontology"` silently elides "(Stapp's quantum-Zeno mechanism)" from the middle of [mechanism-costs-dualism-thickness-quadrants](/topics/mechanism-costs-dualism-thickness-quadrants/) L115, so the quoted span greps zero at its own source and reads as fabricated to any grep-based check. The 2026-07-15 review noticed the elision and accepted it; this pass makes it verifiable instead. Fixed by re-scoping the quotation marks to the contiguous tail — the mechanism-costs reading calls it a probabilistic channel "structurally Q1-like even when sitting in a Q4 ontology" — which greps 1/1 at the source.

### Medium Issues Found (1, fixed)

4. **Missing link to the corpus's canonical channel-class ordering.** [channel-class-taxonomy](/concepts/channel-class-taxonomy/) (created 2026-05-12, fifteen days *before* this article; deep-reviewed 2026-08-02) specifies the identical five classes this article's §what-it-measures enumerates — selection-only, probability-bias, basis-choice, candidate-generation, energy-injection — in Shannon-channel terms. Neither article linked to the other; this article credited the whole ordering to [selection-only-channel](/concepts/selection-only-channel/). Fixed: inline link installed at the point where the ordering is stated. A Further Reading entry was **not** added — the article sits at the 4000-word topic hard ceiling and the inline link carries the discoverability.

   The same fix repairs a small precision defect: the article's prose ordered the classes linearly ("wider than selection-only… wider still"), whereas [channel-class-taxonomy](/concepts/channel-class-taxonomy/) is explicit that "basis-choice and probability-bias are siblings, not ancestors". The new clause carries that caveat, which also strengthens the article's own §separation-test limit note ("channel width is itself a family, not a scalar") by grounding it in a sibling rather than leaving it as an unsupported aside.

### Quotes re-verified against CURRENT siblings (no change needed)

- "contributing nothing to the alternative set itself" — [selection-only-channel](/concepts/selection-only-channel/) L42 ✓
- "selects *within* Born-rule probabilities rather than deviating from them" — [delegatory-causation](/concepts/delegatory-causation/) L148 ✓ (this half of the L64 sentence survived the sibling's rewrite)
- "quantum-Zeno biasing only" — [four-quadrant-dualism-taxonomy](/topics/four-quadrant-dualism-taxonomy/) L134 ✓
- "*selects* among patterns the brain presents" — [stapp-quantum-mind](/concepts/stapp-quantum-mind/) L61 ✓
- "Cartesian energy-transfer" — [mechanism-costs-dualism-thickness-quadrants](/topics/mechanism-costs-dualism-thickness-quadrants/) L111 ✓
- "by judgement rather than definition" — [four-quadrant-dualism-taxonomy](/topics/four-quadrant-dualism-taxonomy/) L78 ✓
- "three values across what may be only a two-axis taxonomy" — [four-quadrant-dualism-taxonomy](/topics/four-quadrant-dualism-taxonomy/) L78 ✓
- "supply novelty beyond the brain-encoded set" — [selection-only-channel](/concepts/selection-only-channel/) L87 ✓
- "mental content vastly exceeding introspection" — [four-quadrant-dualism-taxonomy](/topics/four-quadrant-dualism-taxonomy/) L62 ✓
- "the strictest reading" — [selection-only-channel](/concepts/selection-only-channel/) L44 ✓
- "the basis-choice layer above sits outside the selection-only class strictly construed" — [selection-only-channel](/concepts/selection-only-channel/) L102 ✓
- "near Q1, with room along the mind-axis" — [mechanism-costs-dualism-thickness-quadrants](/topics/mechanism-costs-dualism-thickness-quadrants/) ✓
- §"Limits of the Thickness Metaphor" — live section heading in [four-quadrant-dualism-taxonomy](/topics/four-quadrant-dualism-taxonomy/) L76 ✓ (structural reference intact)
- Thin-mind / thin-physical definitions in §what-it-claims — faithful to parent L59 and L74 ✓ (scare-quoted terms, not verbatim claims)

### Citations

Not re-verified at publishers. The References block is byte-identical to the state the 2026-07-15 ledger cleared (Saad 2025, Schaffer 2000, Stapp n.d. / 1999, Cucu & Pitts 2019, Kastrup glossary, Shannon 1948, Tegmark 2000, plus four Map self-cites), inline↔References cross-check remains clean in both directions, and the superlative-claim scan returns empty. Per that ledger's own instruction, metadata need not be re-litigated until the block changes.

### Attribution / calibration checks

- **Source/Map separation**: clean. The Born-rule identification of Saad's default causal profile is still explicitly flagged as "The Map's integration". The Kastrup exposition remains de-quoted (fixed 2026-07-15) and matches the parent's scope note that monist entries are "included for contrast, not classification-as-dualism".
- **Possibility/probability slippage**: none. §site-perspective's three cautions still explicitly decline the upgrade — naming MQI's axis is not evidence for MQI, ruling out the wide/thin cell is not evidence for the narrow channel, and the Tegmark decoherence objection is carried as a live open question. The diagnostic test returns "no": a tenet-accepting reviewer would not flag these as overstated.
- **Reasoning-mode classification**: no named-opponent replies in this article — it is cartographic throughout, adjudicating no framework. No boundary-substitution risk, no editor-vocabulary leakage found in prose.

## Optimistic Analysis Summary

### Strengths Preserved
- The structural/contingent partition of the vacant wide-channel/thin-pole cell remains the article's distinctive payoff and is untouched.
- §q4-symmetry's sociological-vs-structural contrast between the two empty cells — a genuine cartographic finding — is preserved; only its closing paragraph was tightened for length, with no claim dropped.
- §site-perspective's evidential-status discipline is exemplary and unchanged.
- The Saad/Stapp "same channel class, different pole thickness" pairing, which is the article's proof that the third axis does independent work.

### Enhancements Made
- Integration with [channel-class-taxonomy](/concepts/channel-class-taxonomy/) and [hylomorphic-dualism-and-the-interaction-problem](/topics/hylomorphic-dualism-and-the-interaction-problem/), both previously unlinked from an article whose subject matter overlaps theirs directly.
- The off-axis discussion is now substantively correct about *why* hylomorphism is off-axis (dissolution, not an internal interface), which makes §points-next's open question sharper rather than merely hedged.

### Cross-links Added
- [channel-class-taxonomy](/concepts/channel-class-taxonomy/) (§what-it-measures)
- [hylomorphic-dualism-and-the-interaction-problem](/topics/hylomorphic-dualism-and-the-interaction-problem/) (§points-next)

## Length

3998 words → 3998 words (net zero; `soft_warning`, under the 4000 topic hard ceiling). Length-neutral mode enforced throughout: the four additions were paid for by tightening the §vacant-cell opening (a clause restating the preceding sentence), the §separation-test recap, and the §q4-symmetry closing paragraph. No claim was removed to make room.

## Remaining Items

- **Reciprocal link**: [channel-class-taxonomy](/concepts/channel-class-taxonomy/) does not link back to this article, though it is the natural "where do these classes sit in the dualism taxonomy" successor. Out of scope for a single-document review, and that concept was itself deep-reviewed 2026-08-02; deferred rather than edited here.
- No Further Reading entry for [channel-class-taxonomy](/concepts/channel-class-taxonomy/) (hard-ceiling constraint). Revisit if the article is ever condensed below ~3900 words.

## Stability Notes

- **The residual channel is confirmed and unchanged: intra-corpus quote drift.** Three of the four defects this pass found were quotes whose *sibling* was rewritten underneath them, two of which a prior review had explicitly certified verbatim. External citation metadata has now been stable and correct across two passes; the sibling-quote surface is where this article decays. Future passes should re-grep every in-quote string against current siblings **and treat a prior review's "✓ verbatim" as expiring** — it certifies the sibling's state on that date, not today's.
- **Grep-verifiability is the standard, not meaning-preservation.** A quote that elides a mid-string parenthetical without an ellipsis is faithful in meaning yet greps zero at its own source, and therefore reads as fabricated to every future automated check. Re-scope the quotation marks to a contiguous span.
- MQI-as-minimum-channel-width remains a structural tenet-restatement, not evidence. §site-perspective flags this correctly; do NOT re-flag as overstatement.
- Persona disagreement at the framework boundary (physicalist / MWI rejection of quantum interactionism) is bedrock, not a correctable defect.
- The conservation-denying thin-Cartesian sliver is correctly framed as logically-available-but-undefended, not a Map position. Not a calibration error.
- The 2026-07-15 publisher-of-record ledger stands for all six external cites; re-run it only if the References block changes.