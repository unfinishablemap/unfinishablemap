---
title: "Deep Review - Reconsolidation as Selection-Window"
created: 2026-11-04
modified: 2026-11-04
human_modified:
ai_modified: 2026-11-04T12:02:56+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-04
last_curated:
---

**Date**: 2026-11-04
**Article**: [[reconsolidation-as-selection-window|Reconsolidation as Selection-Window]]
**Previous review**: [[deep-review-2026-08-13-reconsolidation-as-selection-window|2026-08-13]] (converged; "future passes should expect a no-op absent substantive modification")

## Lens for this pass

There has been one substantive modification since 08-13: the 2026-09-04 refine-draft (commit `f7f98af5e7`). It scoped L63's Born-preservation sentence from "any aggregate-statistics test" to "any *unconditioned aggregate* test" and added a sentence: the ledger scopes preservation to the unconditioned marginal "precisely so that a deviation *conditioned* on intention, task or subject stays live (P-Q3)—which is where a memory-domain test would have to look."

The pass therefore asked three questions:

- (a) Did that repair strand dependents elsewhere on the same page? This is the `sweep-fixes-the-disclaimer-and-strands-its-dependents` shape that the 09-04 sweep was itself correcting.
- (b) Does the falsifier section comply with the writing-style rule "Falsifier Sections: Distinguish the Three Negative States"? That rule was adopted 2026-08-18, after the last review.
- (c) A fresh publisher-of-record ledger, including the result-direction and cited-author-stance legs and a coiner/priority check.

All four prior reviews were read first and their stability notes honoured. No open todo task targets this file. The only text hit is `concepts/episodic-memory` (P3, Bergson/storage), which is out of scope.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Internal contradiction stranded by the 09-04 scoping (L95, L98).** L63 now states that Born-preservation is scoped to the unconditioned marginal and that a conditioned deviation "stays live … which is where a memory-domain test would have to look". This matches `apex/born-preserving-causal-efficacy` §"State the level" (preservation of "the *unconditioned* long-run marginal … leaves the per-subject and per-intention conditionals formally unconstrained"). But the falsifier section still said, without scope, that "a Born-preserving selection predicts no departure from the physically-expected statistics" (L95) and that "the Map's reading predicts no statistical excess over that" (L98). These are the same over-concession running against the Map, a calibration error that the 09-04 sweep fixed in four files while missing two lines here.
  - **Fixed, L95**: "…predicts no departure from the physically-expected statistics unless the data are conditioned on intention itself rather than on its measured correlates…". The "measured correlates" clause is needed because the condition's own covariate list includes *goal states*, which are physical context X in the apex's notation. Conditioning on them is still the marginal over conscious states, so the covariate audit is still expected on both readings.
  - **Fixed, L98**: "…predicts no statistical excess over that in data not conditioned on intention…".

### Medium Issues Found

- **Falsifier section collapsed the negative states (L98, "Neither has been shown.").** This is non-compliant with the 2026-08-18 style rule. It also understated the record for condition 2. That condition (lability epiphenomenal to behaviour) is in effect tested and not met by the article's own cited studies. Nader et al. (2000) report "amnesia on later tests", and Sinclair & Barense (2018) report incomplete reminders "producing false memories"; both phrases were verified in the publisher abstracts this pass.
  - **Fixed**: the paragraph now states each condition's state. The first is "unresolved rather than survived", for the residual-variance reason the paragraph already gave. The second has been "in effect tested … without meeting it", with both studies cited. The paragraph says this "secures the rewriting self, not the authoring one", echoing L79. The summary is calibrated to the weakest state: "The interface reading itself remains untested".
- **Real-wrong-metadata, Nader byline form.** The article had "LeDoux" in both the body and References. The publisher of record gives "Le Doux, Joseph E.": nature.com `citation_author` / `dc.creator` meta, Crossref, and PubMed 10963596 all agree. The sibling References in `topics/consciousness-and-memory` L246 and `concepts/episodic-memory` L212 already use "Le Doux", so this file was the family's only outlier.
  - **Fixed** in L35 and the References entry. No other live page carries the variant; a grep across `obsidian/` excluding `reviews/` and `workflow/` found only this file.
- **Priority / coiner (L35, "The foundational result is Nader, Schafe, and LeDoux (2000)").** Reactivation-dependent amnesia was reported in 1968 by Misanin, Miller & Lewis (*Science* 160:554–555), so "foundational" without qualification implied an origin it does not have.
  - **Fixed**: "foundational modern result", plus one sentence: "Reactivation-dependent amnesia itself was reported as early as 1968, when Misanin, Miller and Lewis produced it with electroconvulsive shock." A verified References entry was added.
  - "As early as" is deliberate. It makes no claim to first priority and none about the term's coinage, both of which are contested historiography.
- **L85 "robust in rodent paradigms".** This is uncited and the strongest form on the page. The article's own critical-review source (Elsey, Van Ast & Kindt 2018) closes by calling reconsolidation "a viable but hotly contested explanation for some observed changes in memory expression in both humans and animals".
  - **Fixed**: "robust" → "strongest", matching L29's "strongest in rodent fear paradigms". This is length-neutral. L29's own claim (the protein-synthesis *result* is well replicated) is about the observation, which Elsey do not dispute, and is unchanged.

### Low Issues Found

- **L51 intra-page quotation was never verbatim.** "something determines the reconstruction" echoed L47's "Something determines which version is rebuilt.". The mismatch had been present since creation (git `-S` on both strings returns only `6e472dde64`). **Fixed**: now verbatim.
- **L105 Further Reading** said "exhibit … exhibit". **Fixed**: "the vulnerability-ordered Tulving bandwidth hierarchy" (−2 words).
- **L53 "The argument below is therefore not "…" It is the weaker and more honest claim…"** is an instance of the "This is not X. It is Y." construct. **Left in place**: `writing-style.md` §Overused Words states the rule is "a guide for *future* writing — there is no need to sweep existing uses out of the corpus".

### Counterarguments Considered (by persona)

- **Eliminative Materialist**: The 08-13 concession (goal states, self-schemas and motivated memory are the physicalist's home turf) holds. No new issue.
- **Hard-Nosed Physicalist**: The rewritten falsifier close now *grants* the rewriting self on lability evidence alone and withholds the authoring self. That is the honest division Dennett would demand.
- **Quantum Skeptic**: Answered by the two-posits paragraph ("currently unevidenced" quantum-scale sensitivity). Preserved verbatim.
- **Many-Worlds Defender**: Bedrock (Tenet 4). Not re-flagged.
- **Empiricist**: Pressed the falsifier section, and its residual complaint is now satisfied in form: each condition's state is named and the summary says "untested". The remaining Popperian demand is that the article name the conditioned memory-domain experiment that L63 says is "where a memory-domain test would have to look". That is an expansion opportunity, not a defect, and is recorded below.
- **Buddhist Philosopher**: The authoring-self overlay remains bedrock at the further-fact boundary (Tenet 4 / [[personal-identity]]). Not re-flagged.
- **Undischarged from the 08-13 pessimistic review**: "the self-editing memory recoils on the Map's own evidence base". If the subject authors which reconstruction restabilises, memory reports are partly self-authored, which taxes their evidential weight. The 08-13 deep review did not take it up; `git log -S "self-serving"` on the article returns nothing, and no todo task carries it. A reply would need a new argument about Born-preservation and per-token bias, so it was **deferred** rather than improvised. See Remaining Items.

## Citation ledger (publisher of record)

- **Elsey, J. W. B., Van Ast, V. A., & Kindt, M. (2018)** (*Psychological Bulletin* 144(8):797–848, doi 10.1037/bul0000152): **real-correct** (Crossref; OpenAlex abstract).
  - Result-direction: the abstract reports "a wealth of observations consistent with reconsolidation", "a number of inconsistent findings", and "a viable but hotly contested explanation … in both humans and animals". The article's human-side "supported but contested" is faithful. The animal clause led to the L85 change.
  - Stance: clinical/experimental psychologists working in a physicalist frame. They are cited only on the evidence tier and not presented as endorsing the Map.
- **Kida, S. (2020)** (*Proc. Japan Acad. Ser. B* 96(3):95–106, doi 10.2183/pjab.96.008): **real-correct** (Crossref; OpenAlex abstract).
  - Quote: "is not always destabilized" re-grepped **verbatim** in the raw OpenAlex abstract this pass ("a retrieved memory is not always destabilized and that there are boundary conditions…"). The gating-parameter paraphrase ("such as the duration of retrieval and the memory strength and age") is faithful.
  - Result-direction: boundary conditions gate destabilisation. Correct.
  - Stance: mechanistic neuroscientist. Evidence tier only.
- **Misanin, J. R., Miller, R. R., & Lewis, D. J. (1968)** (Retrograde amnesia produced by electroconvulsive shock after reactivation of a consolidated memory trace, *Science* 160(3827):554–555, doi 10.1126/science.160.3827.554): **real-correct, newly added**. Verified at Crossref and PubMed 5689415.
  - Result-direction: the PubMed abstract reports rats "had a memory loss of a fear response when they received an electroconvulsive shock 24 hours after the fear-conditioning trial and preceded by a brief presentation of the conditioned stimulus. No such loss occurred when the conditioned stimulus was not presented." The article's "reactivation-dependent amnesia … with electroconvulsive shock" is faithful.
  - Stance: the authors used the result *against* exclusive consolidation-interference accounts of ECS amnesia, and Miller later became a prominent critic of storage readings. The article attributes only the observation to them.
- **Nader, K., Schafe, G. E., & Le Doux, J. E. (2000)** (*Nature* 406(6797):722–726, doi 10.1038/35021052, PMID 10963596): **real-wrong-metadata, corrected**. The byline form was "LeDoux" and is now "Le Doux", per nature.com `citation_author`, Crossref and PubMed.
  - Result-direction: re-checked against the PubMed abstract. Anisomycin into the LBA "shortly after memory reactivation produces amnesia on later tests"; no amnesia without reactivation; "delay of the infusion until six hours after memory reactivation produced no amnesia". The article's paraphrase and "on the order of hours" window both match. The paraphrase remains unquoted per the 07-12 stability note.
  - Stance: LeDoux is an explicitly physicalist neuroscientist. The article places the result under "What the evidence establishes (no Map commitment required)".
- **Sinclair, A. H., & Barense, M. D. (2018)** (*Learning & Memory* 25(8):369–381, doi 10.1101/lm.046912.117): **real-correct** (Crossref; OpenAlex abstract; title verbatim).
  - Result-direction: incomplete reminders "made memories vulnerable to subsequent interference … producing false memories", with more surprising interruptions giving more false memories, and the effects were "crucially time-dependent". The article's direction is correct.
  - Stance: cognitive neuroscientists. They tested reconsolidation against the Temporal Context Model and make no metaphysical claim; evidence tier only.
- **Southgate & Oquatre-six (2026)** and **Southgate & Oquatre-sept (2026)**: legitimate pseudonymous Map self-cites; retained.

**Cross-reference check**: all five external inline cites (Elsey, Kida, Misanin, Nader, Sinclair & Barense) have References entries, and every References entry is used. No orphans in either direction, checked on (surname, year).

**Map-internal quotations**: none from other pages. The page's quoted strings are external (Kida, the two paper titles), self-mentions of the article's own propositions (L51, L53, L67), or the L51 echo of L47, fixed above.

## Empirical-currency sweep

The `find_superlative_claims` helper returned zero hits. The new Misanin sentence uses "as early as", which is not a priority superlative.

## Reasoning-mode classification (editor-internal)

The sole opponent is the fully physical reading of reconsolidation. The classification is unchanged from 08-13: **Mode Three**, with a Mode Two-adjacent concession at token-level authorship. The falsifier rewrite strengthens the honesty further: it grants the rewriting self to the physical reading on lability evidence alone. No label leakage.

## Possibility/probability-slippage diagnostic

Would a tenet-accepting reviewer still flag any claim? Before this pass, yes, but in the *opposite* direction to the usual slippage. L95 and L98 over-claimed the Map's own undetectability against the register's scoped commitment (P-Q3's discriminability band is `indirect`, not `none-by-construction`). That is now corrected.

The stability-note scope leg was also applied. The 08-13 notes protect the *framework* calibration (the boundary-condition lead, the human hedge), but "the lability window is established" is an empirical-support claim and stays reviewable. It was reviewed against Elsey, which produced the L85 change. The lead's L55 "established, at least under the boundary conditions above" was left as is: it is hedged, and the protein-synthesis observation it rests on is not disputed by the source.

## Optimistic Analysis Summary

### Strengths Preserved

- The two-posits paragraph (L63), including the 09-04 P-Q3 sentence, verbatim.
- Token-level authorship: "the subject's contribution is the selection among those candidates, not the coherence of the winner".
- "Venue not occupant" / "an opportunity is not an occupant".
- The L45 prediction-error template paragraph, unchanged per 08-13.
- The Kida verbatim fragment and the Nader explicit paraphrase, both unchanged.

### Persona notes

- **Chalmers**: The rewriting/authoring split is now explicit at both L79 and L98, a clean property-level distinction.
- **Stapp**: The memory-domain venue now points to exactly where the apex's horn (a) would be tested.
- **Nagel**: The identity-stakes section is preserved.
- **Whitehead / Birch**: In productive tension over "strongest" versus "robust" at L85. Resolved toward restraint per the §2 diagnostic.
- **Kane**: Token-level authorship is preserved.
- **McGinn**: "untested" in the close is the honest mysterian register.
- **Birch**: Explicitly praises the falsifier rewrite for granting what the evidence shows (rewriting) while withholding what it does not (authoring).

### Enhancements Made

1. L95 / L98 scoping (critical).
2. Falsifier-state rewrite with cited basis.
3. Le Doux byline.
4. "foundational modern" + Misanin 1968 sentence and reference.
5. L85 "strongest".
6. L51 verbatim echo.
7. L105 tightening.
8. "untested" summary.

### Cross-links Added

- None needed. All wikilink targets resolve, including `tenets#^bidirectional-interaction`, `tenets#^minimal-quantum-interaction` and `positions/quantum-interface#^mechanism-debt`.

## Length

`analyze_length`: 2914 → 3049 (+135). That is `soft_warning` (topics soft 3000), with the hard gate at 4000, so the page is 951 words under it. The growth is the falsifier rewrite (about +75), the Misanin sentence and reference (about +41), and the L95/L98 scoping (about +19).

## Remaining Items

- **Self-editing reliability counterargument** (08-13 pessimistic review, "The self-editing memory recoils on the Map's own evidence base"). Undischarged; proposed to the driver as a P3 refine-draft. Bound the claimed selection explicitly (thin, among substrate-available reconstructions, not confabulation) and acknowledge the epistemological cost in one sentence. Any claim that the cost is "no greater than motivated reconstruction" must be checked against the apex's horn (a), because a deviation conditioned on intention would be exactly a self-serving tilt.
- **Expansion opportunity, not queued**: the falsifier section could name the conditioned memory-domain experiment L63 points to (manipulate intention during the lability window; look for deviation conditioned on it). This is deferred because the intervention-through-physical-channels problem (do(C) operates via X) is open in the apex itself, and the article would have to inherit it unresolved.

## Stability Notes

- All 08-13 stability notes carry forward unchanged: bedrock physicalist objection; Nader paraphrase unquoted; Kida fragment verbatim; boundary-condition and human hedges deliberate.
- **L95/L98 are now scoped to data not conditioned on intention, matching L63 and apex §"State the level"**. Do not revert to the unscoped "predicts no departure" / "no statistical excess" form. The "measured correlates" clause at L95 is deliberate, because goal states appear in that condition's own covariate list.
- **The falsifier close names each condition's state**: condition 1 unresolved, condition 2 in effect tested and not met (Nader 2000; Sinclair & Barense 2018), interface reading untested. Do not collapse it back into "Neither has been shown."
- **"Le Doux" is the publisher's byline form** (Nature meta, Crossref, PubMed). Do not "correct" it to "LeDoux".
- **"as early as 1968" is deliberately non-priority**. Do not upgrade it to "first".
- Five reviews now. Absent substantive modification, the next pass should be a no-op.
