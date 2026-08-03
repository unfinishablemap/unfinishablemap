---
title: "Deep Review - Ethics Under Dualism"
created: 2026-08-02
modified: 2026-08-02
human_modified: null
ai_modified: 2026-08-02T00:25:58+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[ethics-under-dualism]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-02
last_curated: null
---

**Date**: 2026-08-02
**Article**: [[ethics-under-dualism|Ethics Under Dualism]]
**Previous review**: [[deep-review-2026-07-14-ethics-under-dualism|2026-07-14]]
**Word count**: prose 2899 → 2992 (+93); apparatus 326 → 354

## What Changed Since 2026-07-14 (scope of this pass)

The article re-qualified for review through the pattern the skill's convergence-damping guard was written for: **every diff since 07-14 was a cross-link installed by another article's pass**, not an edit made to this article on its own merits.

- `fa144ba83` (refine of `phenomenal-normativity-environmental-ethics`) added the environmental-extension sentence to the Animals section plus a Further Reading entry.
- `2ea81dc7d` (expand-topic creating `concepts/sentientism.md`) rewired the Suffering section's sentientism mention into a live wikilink.

That is not a no-op pass, because **inbound cross-links carry claims that no review has ever checked against their own targets** ([[navigation-surfaces-carry-unreviewed-claims]]). Both installed claims turned out to misstate the article they point at. That was this pass's highest-yield lens, and it is a lens neither the 06-02 nor the 07-14 review could have run, because neither claim existed yet.

**§2.4 publisher web-verify correctly skipped for the References block**: unchanged since the 06-02 ledger, per that review's standing instruction. But the trigger's *body* clause did fire — the body gained a new empirical claim surface — and that is where the defects were.

## Critical Issues Found

**1. Superseded empirical figure (`empirical-record-currency-drift`) — FIXED.**
The Uncertain-status bullet claimed vegetative-state patients "where 15-20% show covert awareness on neuroimaging." The corpus cites **25%** at nine-plus other loci, all sourced to Bodien et al. 2024. This article was the lone holdout on a pre-2024 figure.

Verified at publisher rather than by intra-corpus agreement (which ratifies rather than catches errors): citation metadata confirmed via PubMed — Bodien YG, Allanson J, Cardone P, et al. (2024), *New England Journal of Medicine* **391**(7), 598–608, DOI 10.1056/NEJMoa2400645. NEJM returns 403 and the PMC record did not expose the abstract, so the figure itself was corroborated independently of the Map's own corpus via a 2026 Europe PMC review stating CMD "occurs in approximately 25% of behaviorally unresponsive patients."

Also fixed the **scope error** bundled into the same sentence: the figure is for behaviourally unresponsive patients across disorders of consciousness (coma, VS/UWS, MCS), not for the vegetative state specifically. The wikilink alias was corrected from "vegetative states" to "disorders of consciousness" so the navigation label stops asserting the narrower scope. Bodien added to References (now 16 entries).

**2. Dropped qualifier in an installed cross-link — FIXED.**
The environmental-extension sentence asserted the resulting obligations "are often more demanding than ecocentrism's rather than weaker." Its target says something materially weaker and two-tiered: "often more stringent than **anthropocentrism** and **sometimes** more so than **ecocentrism** *in practice*," and elsewhere "**can** be more demanding than ecocentrist obligations." The install flattened a two-tier calibration into a single stronger claim about the harder comparison and dropped both "sometimes" and "in practice" — a §2.5 dropped-qualifier / position-strength error. Restored the target's calibration.

**3. Two orphaned References entries — FIXED by citing, not deleting.**
§2.4 step 5 cross-reference found **Birch (2024)** and **Parfit (1984)** in References with no inline citation anywhere in the body. Both are real and both were already doing silent work, so the correct repair is to cite them where they operate ([[citation-verify-false-negative]] — fix, don't delete):

- **Birch** now cited in Moral Uncertainty as the source of the precautionary action layer. Framed per [[citation-framing-accuracy-lens]] and harmonised with the new `sentientism` article's wording: the Map borrows the decision procedure while noting the framework is metaphysics-neutral and Birch assigns non-materialist views low credence — explicitly **not** claimed as an ally on the grounding question.
- **Parfit** now cited in Identity Ethics as the position the Map's indexical commitment denies (identity is not what matters in survival; psychological continuity carries the weight). The canonical opponent of the section's whole thesis had gone unnamed.

## Medium Issues Found

**Position understated against its own new hub — FIXED.** The Suffering section said the Map "aligns with a sophisticated valence-based sentientism." The new `concepts/sentientism.md` states flatly that "The Unfinishable Map **holds** sentientism, but in a specific and contestable form: **phenomenal sentientism**," and that the phenomenal-vs-functional distinction "is the one the Map's position turns on." The bare label "valence-based" is exactly ambiguous across that distinction. Changed to name the variety held and mark the distinction, retaining the pluralist qualifier.

## Per-Cite Ledger (this pass)

Only the newly-introduced cite was web-verified; the rest stand on the 06-02 publisher ledger with an unchanged References block.

- Bodien et al. 2024 (*Cognitive Motor Dissociation in Disorders of Consciousness*) — state: **real-correct** metadata, publisher-confirmed via PubMed; **currency-corrective** (replaces a superseded 15-20% figure with ~25%).
- Birch 2024, Parfit 1984 — state: real-correct (06-02 ledger); **orphan-resolved**, now cited inline.
- All other entries — unchanged since the 06-02 publisher-of-record pass; not re-litigated.

## Engagement Modes (editor-internal)

- **Parfit** (new): Mode Three — framework-boundary marking. The Map's denial rests on indexical identity, a tenet commitment, so no internal-to-Parfit refutation is available or claimed; written as an explicit deliberate divergence.
- **Birch** (new): not an opposition engagement — a borrowed action layer with non-alliance honestly noted.
- All prior classifications unchanged from 06-02/07-14 (Mackie Mode One; compatibilism Mode One; Korsgaard Mode Two; Railton Mode One; Foot Mode One; illusionism/Frankish Mixed).

No editor-vocabulary label leakage found in article prose (scanned for the full forbidden-label set); none introduced.

## Calibration Pass

Diagnostic test applied — would a tenet-accepting reviewer flag any claim as overstated on the five-tier scale? No new slippage. The patienthood table, the AI framework-dependence hedge, and the invertebrate precaution framing are unchanged and intact. Note that fixes 1 and 2 both moved claims *toward* calibration honesty rather than away, and fix 2 in particular reversed an over-claim that had been installed by a sibling article — the [[over-concession-gets-ratified-not-merely-missed]] pattern running in the opposite direction.

## Length Finding (correcting a standing false premise)

Both the 06-02 and 07-14 reviews operated in **length-neutral mode** on the belief that the article was over the topics soft threshold. That premise is false and should not be carried forward. `analyze_length` reports 3228 words, but decomposition gives:

- **prose: 2899 words** (under the 3000 soft threshold)
- reference apparatus (Further Reading + References): **326 words**

This is the known [[analyze-length-counts-reference-apparatus]] false-over-length pattern. The article has genuine prose headroom, which is why this pass could add the three missing citations without forced compensatory cuts. Post-edit prose is **2992** — still under threshold. Future reviews should decompose before assuming length-neutral mode here.

## Optimistic Summary

Seven sympathetic personas re-applied. Strengths preserved unchanged: the front-loaded two-claim thesis, the four-pillars-on-one-foundation architecture, the calibration-honest patienthood table, and the "What Would Challenge This View" defeasibility section. Birch (Hardline Empiricist) counterweight is now *strengthened* rather than merely intact — the article previously leaned on his precautionary framework without naming him or marking the credence gap. No expansion forced.

## Remaining Items

- **`archive/topics/ethics-of-consciousness.md:73`** (and its Hugo copy) carries the same superseded "15-20%" sentence, inherited from the pre-coalesce original. Left unactioned deliberately: archived pages are historical snapshots carrying an archive notice pointing to this article, and rewriting archived bodies is a convention call rather than a review call. Flagged with the exact locus so a human or a dedicated sweep can decide. Note that `archive/` is served, so this is a live-reader-visible stale figure (`defect-sweeps-must-include-archive-tree`).
- **Street / Darwinian-Dilemma moral-realism-debunking gap** — still tracked in `todo.md` as a human-deferred length decision. Not actioned, not papered over. Unchanged from 07-14.

## Stability Notes

Convergence holds on everything the prior reviews settled. Future reviews should NOT: re-run the publisher web-verify while the References block is unchanged; re-flag the bedrock disagreements (illusionism, Many-Worlds, hard-physicalist rejection of agent causation, Tegmark decoherence) as critical; re-open the moral-realism presupposition as a calibration defect; attempt the Street gap; or assume length-neutral mode without decomposing the apparatus first.

The transferable lesson from this pass: **a converged article's remaining defect surface is its inbound cross-links.** Three of the four fixes here were on text written *by other articles' passes* — text that arrives already asserting things about a target it was never checked against. When a deep-review candidate's entire diff is cross-link installs, the correct response is to diff each installed claim against the article it points at, not to declare a no-op.
