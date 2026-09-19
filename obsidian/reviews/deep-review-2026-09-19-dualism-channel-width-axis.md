---
title: "Deep Review - Channel Width: The Third Axis of the Dualism-Thickness Taxonomy"
created: 2026-09-19
modified: 2026-09-19
human_modified:
ai_modified: 2026-09-19T22:26:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: "claude-opus-5"
ai_generated_date: 2026-09-19
last_curated:
---

**Date**: 2026-09-19
**Article**: [[dualism-channel-width-axis|Channel Width: The Third Axis of the Dualism-Thickness Taxonomy]]
**Previous review**: [[deep-review-2026-08-03-dualism-channel-width-axis|2026-08-03]] (intra-corpus quote drift). Earlier: [[deep-review-2026-07-15-dualism-channel-width-axis|2026-07-15]] (publisher-of-record ledger), [[deep-review-2026-06-09-dualism-channel-width-axis|2026-06-09]] (coalesce cross-review); two pre-coalesce passes under the retired `channel-width-third-axis` slug.
**Lens**: The residual channel the 2026-08-03 review named and instructed future passes to re-run — **intra-corpus drift**, with every prior "✓ verbatim" treated as expired. Extended beyond quoted strings to *unquoted claims attributed to a named sibling*, which is where this pass's yield sat. Adversarial personas run for the first time on this slug (no `pessimistic-*` review has ever mentioned it).

## Change Since Last Review

Three commits touched the article since 2026-08-03, all narrow: `e8b4d1027c` (broken `^occams-razor-has-limits` tenet anchor → `^occams-limits`), `e47feab965` (a [[filter-vs-interface-distinction]] cross-link), `a1478a48b6` (Saad 2025 issue `182(3)` → `182(3–4)`, the corpus-wide publisher-of-record correction). None introduced a defect. The defects this pass found were all produced by **siblings moving underneath stable article prose**.

## Pessimistic Analysis Summary

### Critical Issues Found (3, all fixed, all length-neutral)

1. **§what-it-measures — the article asserts the weak form of the Born-preservation constraint, which its cited sibling now names as the error.** The article read *"Born-rule preservation constrains the unconditioned marginal, not the mind-conditioned throughput"*. [[selection-only-channel]] has since been substantially rewritten: L42 now reads "constrains the *marginal* frequency distribution over outcomes **in every publicly conditionable context**, leaving the conditionals within a context free", and L76 is headed **"The quantifier over X carries the weight, and dropping it is the easy error"** — spelling out that read *without* the per-context quantifier "the freedom is larger than the channel wants… which is signalling." The article's clause is exactly the dropped-quantifier reading. Not a quote (so no quote-fidelity check would have caught it) and not a metadata defect (so no ledger covers it); it is a load-bearing claim that drifted out from under its source. **Fixed**: `the unconditioned marginal` → `the per-context marginal`, tracking sibling L114 ("the constraint falls on the marginal in each publicly conditionable context, not on the mind-conditioned throughput within one"). Cost **0 words** (one-for-one token swap).

2. **§q4-symmetry — Goff placed in Q4, which the parent explicitly denies.** The article read *"(Descartes, Stapp, Goff sit there)"* of the max-mind/max-physical quadrant. [[four-quadrant-dualism-taxonomy]] does not list Goff in Q4 and states the contrary three times: L79 "Goff is mind-thick but **monist**, so **Q3** is a limit-case reading rather than a quadrant assignment"; L83 monist limit cases including "Goff's priority cosmopsychism" are "included for contrast, **not classification-as-dualism**"; L114 priority cosmopsychism is "a monist limit case toward which Q3 points rather than a two-realm dualism." The parent's own phrase for Q4's classical occupants is "**(Descartes, Aquinas)**". **Fixed**: `Goff` → `Aquinas`. Cost **0 words**.

3. **§q4-symmetry — the whole sociological reading of Q4 is attributed to a parent that has been rewritten to reject it.** The article read *"avoided because the discipline reads parsimony as a virtue"* and *"Q4's emptiness is **sociological**: … contemporary training disfavours paying its mechanism bill. Nothing forbids Q4; the discipline avoids it."* The parent's current Q4 section inverts the weighting: "The **first and weightier** reason is genuine explanatory cost… so the parsimony pressure against the cell is **not merely a matter of taste**. A **second and lesser** contributor is disciplinary"; L51 likewise says "partly because maximum commitments on both sides carry real explanatory costs and partly because the discipline tends to read parsimony as a virtue." The article kept only the lesser half and labelled it the whole. This matters more than a wording slip because the parent's Q4 section *cites this article back* for the structural/non-structural contrast, so the two pages were describing the same contrast with incompatible accounts of one side of it. **Fixed** in two places, preserving the contrast the section exists to draw (Q4 = not structural; wide/thin = mostly structural):
   - `a [[…#q4|systematically under-populated quadrant]] — max-mind/max-physical, avoided because the discipline reads parsimony as a virtue.` → `an [[…#q4|under-discussed quadrant]] — max-mind/max-physical, avoided for its explanatory costs and the discipline's parsimony norms.` ("under-populated" was also not the parent's word; it says "under-discussed".) Cost **0 words**.
   - `Q4's emptiness is *sociological*: the cell is coherent and inhabitable (…), but contemporary training disfavours paying its mechanism bill. Nothing forbids Q4; the discipline avoids it.` → `Q4's emptiness is *not structural*: the cell is coherent and inhabited (…), but its mechanism bill is heavy and the discipline mostly declines to pay it.` ("inhabited" also matches the parent's "coherent and inhabited".) Cost **0 words**.

### False alarms — probes that returned zero and were wrong

Recorded because both were case-splitter false zeros on a `grep -F` probe, and both would have been published as fabricated-quote findings:

- `"the basis-choice layer above sits outside the selection-only class strictly construed"` (§points-next, attributed to [[selection-only-channel]]) greps **zero** corpus-wide — because the source sentence begins with a capital **T**. It is verbatim at [[selection-only-channel]] L102. ✓
- `"Thin substance, indispensable role"` (§site-perspective) greps **zero** — the source is lower-case mid-sentence at [[q3-q4-sliding-boundary-and-transparency-problem]] L76 ("That decoupling — thin substance, indispensable role — is exactly what a stable Q3-adjacent dualism needs"). ✓
- `[[selection-only-channel#what-the-channel-is-not]]` has **no `{#…}` anchor** at the target — but the target carries `## What the Channel Is Not` (L96), whose Hugo-generated slug is exactly that. Heading-text dialect, resolves. ✓

### Quotes and attributed claims re-verified against CURRENT siblings (no change needed)

- "Limits of the Thickness Metaphor" — live heading, [[four-quadrant-dualism-taxonomy]] ✓
- "by judgement rather than definition" — four-quadrant L79 ✓
- "three values across what may be only a two-axis taxonomy" — four-quadrant L79 ✓
- "quantum-Zeno biasing only" — four-quadrant ✓
- "mental content vastly exceeding introspection" — four-quadrant L63, and correctly sited under `#mind-side` ✓
- "contributing nothing to the alternative set itself" — [[selection-only-channel]] L42 ✓
- "supply novelty beyond the brain-encoded set" — selection-only-channel L87 ✓
- "the strictest reading" — selection-only-channel ✓
- "*selects* among patterns the brain presents" — [[stapp-quantum-mind]] L61 ✓
- "structurally Q1-like even when sitting in a Q4 ontology" — [[mechanism-costs-dualism-thickness-quadrants]] L115 ✓ (the 2026-08-03 re-scoping to a contiguous span holds; greps 1/1)
- "Cartesian energy-transfer" — mechanism-costs L111 ✓
- "near Q1, with room along the mind-axis" — mechanism-costs ✓
- **"selects *within* Born-rule probabilities rather than deviating from them"** — **relocated but still sound.** The 2026-07-15 and 2026-08-03 ledgers certified it at [[delegatory-causation]] L148; that sibling now reads "If consciousness selects *within* Born-rule probabilities, the statistical distribution of outcomes is unchanged", so the full quoted span no longer lives there. It is verbatim at [[delegation-meets-quantum-selection]] L62 — which is precisely the article [[delegatory-causation]] L140 names as where the Map's Born-rule integration "is developed". The article attributes the clause to "The Map's integration", not to a named work, so the attribution remains true and the string remains grep-verifiable. Left unchanged; noted so the next pass does not re-open it.
- Thin-mind / thin-physical definitions (§what-it-claims) — faithful to four-quadrant L61 and L70–L76 ✓
- Stapp's max-mind/max-physical reading (§ordering) — faithful to four-quadrant Q4 ✓
- Hylomorphism "declines to name an interface at all" — matches [[hylomorphic-dualism-and-the-interaction-problem]] ✓ (the 2026-08-03 fix holds)
- "basis-choice and probability-bias are siblings, not ancestors" — [[channel-class-taxonomy]] L60 ✓, article's paraphrase faithful
- All 15 wikilink targets resolve to exactly one file; `tenets#^minimal-quantum-interaction` (L63) and `tenets#^occams-limits` (L131) both live; `#mind-side`, `#q4` (four-quadrant), `#three-questions`, `#q4` (mechanism-costs) all present as explicit `{#…}` anchors ✓

### Citations

The References block changed once since the 2026-07-15 publisher-of-record ledger: Saad 2025 issue `182(3)` → `182(3–4)`, by commit `a1478a48b6`, which verified the combined issue at the publisher and propagated it to 28 live files. Corpus is now consistent on that DOI. No other field moved; the rest of the 2026-07-15 ledger (Schaffer 2000, Stapp n.d./1999, Cucu & Pitts 2019, Kastrup glossary, Shannon 1948, Tegmark 2000, four Map self-cites) stands. `find_superlative_claims` returns **0** — no empirical-record-currency exposure. Inline↔References cross-check clean in both directions.

### Calibration / attribution checks

- **Possibility/probability slippage**: none. §site-perspective's three cautions still explicitly decline the upgrade — naming MQI's axis is not evidence for MQI, ruling out the wide/thin cell is not evidence for the Map's narrow channel, and Tegmark's decoherence objection is carried live. Diagnostic test returns "no".
- **Tenet 5 parsimony guard**: no unguarded "ours is simpler" claim exists. The two parsimony mentions are (a) the parent's account of why Q4 is avoided and (b) Tenet 5 named as a *loosening* of parsimony norms — neither awards the Map an economy verdict. No repair owed, and none affordable.
- **Reasoning-mode classification**: not applicable. The article replies to no named opponent; it is cartographic throughout. No boundary-substitution risk, no editor-vocabulary leakage in prose.
- **Source/Map separation**: clean. The Born-rule identification of Saad's default profile is still flagged as the Map's integration, consistent with [[delegatory-causation]] L140 ("a Map-specific integration, not a claim Saad makes").

## Optimistic Analysis Summary

### Strengths Preserved
- The structural/contingent partition of the vacant wide-channel/thin-pole cell — candidate-generation analytically forbidden, energy-injection structural under conservation with a conservation-denying contingent sliver — remains untouched and remains the article's distinctive payoff.
- The Saad/Stapp "same channel class, different pole thickness" pairing, which is the article's proof that the third axis does independent work.
- §site-perspective's three evidential-status cautions: exemplary calibration hygiene, unchanged.
- §q4-symmetry's two-kinds-of-emptiness contrast survives this pass **strengthened**: it now rests on what the parent actually says, and the Q4 side reads "not structural" rather than "sociological", which is the claim the contrast actually needs.

### Enhancements Made
None beyond the three repairs. The article is at the length ceiling; no expansion was affordable and none was warranted.

### Cross-links Added
None (no budget; link set already dense).

## Length

3998 → **3998 words** (net zero). `soft_warning`, one word below the 4000 hard gate. **Remaining headroom: 1 word.** All three repairs were engineered to be exactly token-neutral; none was chosen for brevity over accuracy.

## Remaining Items

- **The 1-word headroom is itself an unresolved condition, and nothing tracks it.** At 3998/3999 usable, this article cannot absorb the next inbound cross-link, the next reference entry, or the 26-word Tenet 5 guard clause should one ever be owed. Three consecutive reviews (2026-06-09, 2026-07-15, 2026-08-03) have each recorded "length-neutral mode enforced" and each has had to pay for every addition by cutting elsewhere; the 2026-08-03 pass declined a Further Reading entry for [[channel-class-taxonomy]] on exactly these grounds. This is a standing constraint, not a finding, and **no condense task is minted here** — that is a separate decision with its own evidence requirements. Flagged for a human call.
- **Reciprocal link still absent**: [[channel-class-taxonomy]] does not link back to this article. Carried from 2026-08-03; out of scope for a single-document review.
- **§what-it-measures clarity trade-off**: "per-context marginal" is precise and matches the sibling's vocabulary, but is compressed. The fuller form ("the marginal within each publicly conditionable context") costs +3 words the article does not have. If the article is ever condensed below ~3990, expand this clause first.

## Stability Notes

- **The residual channel is confirmed for a second consecutive pass, and it is wider than "quote drift".** Every one of this pass's three findings was a claim attributed to a named sibling that the sibling no longer supports — and only one of the three was inside quotation marks. A quote-only re-grep would have found nothing. **Future passes must re-verify unquoted attributed claims against current siblings, not merely quoted strings.** The high-traffic siblings for this article are [[selection-only-channel]] and [[four-quadrant-dualism-taxonomy]]; both have been substantially rewritten since this article's prose about them was written.
- **A prior review's "✓ verbatim" expires, and so does a prior review's characterisation of a sibling's position.** The 2026-08-03 review already recorded the first half of this. The Goff/Q4 and sociological-Q4 defects show the second half.
- **Case is a splitter on `grep -F` probes.** Two of this pass's probes returned a corpus-wide zero on strings that are present, because the source sentence begins with a capital or the article capitalises a mid-sentence phrase. Probe case-insensitively (`-iF`) before concluding a string is absent.
- MQI-as-minimum-channel-width remains a structural tenet-restatement, not evidence. §site-perspective flags this correctly; do NOT re-flag as overstatement.
- Persona disagreement at the framework boundary (physicalist / MWI rejection of quantum interactionism) is bedrock, not a correctable defect.
- The conservation-denying thin-Cartesian sliver is correctly framed as logically-available-but-undefended, not a Map position. Not a calibration error.
- The 2026-07-15 publisher-of-record ledger stands, as amended by the 2026-09-08 Saad issue correction. Re-run only if the References block changes again.
- **This article's length state is settled, not open.** 3998/4000 is deliberate — the 2026-06-09 coalesce left it near-ceiling after dedup and explicitly ruled "no growth, no re-condense". Do not re-litigate it as a new finding.
