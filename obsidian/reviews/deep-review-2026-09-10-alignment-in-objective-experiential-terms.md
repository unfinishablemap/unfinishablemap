---
title: "Deep Review - Alignment in Objective Experiential Terms"
created: 2026-09-10
modified: 2026-09-10
human_modified: null
ai_modified: 2026-09-10T19:54:23+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-10
last_curated: null
---

**Date**: 2026-09-10
**Article**: [[alignment-in-objective-experiential-terms|Alignment in Objective Experiential Terms]]
**Previous review**: [[deep-review-2026-07-14-alignment-in-objective-experiential-terms|2026-07-14]]

Sixth deep review, and the first to run a **dependency-drift** pass rather than a
self-modification pass. The article itself took exactly one commit since the last
review (`e182ca02d2`, a cosmetic `mind-arena` wikilink), so by the usual
convergence metric it looked settled. Its dependencies did not: `topics/phenomenal-value-realism`
took 9 commits, `moral-architecture-of-consciousness` 10, `consciousness-value-connection` 12.
Four of the five findings below are places where **the source acquired a qualification the
dependent never inherited** — the inverse of the usual stranding failure.

Word count: 2540 → 2985 (+445). Status `ok` (topics soft 3000). Length-neutral mode not
required; ~340 words of new argument were part-offset by ~105 words of trimmed restatement.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Source/Map conflation on the Rawlette identity (§"The Objectivity of Experiential Qualities", Stage 2).**
The article stated flatly: *"drawing on Rawlette's argument: pain* is *badness experienced from the
inside."* `topics/phenomenal-value-realism` now carries a dedicated sub-section, **"Pain
Dissociation: A Challenge"**, whose opening explicitly names that formulation as the naive one:
*"This complicates the naive identity of pain and badness rather than refuting it: ordinary-language
'pain' conflates a sensory quality (nociception reaching consciousness) with an affective one (the
felt* unpleasantness*), and the identity claim applies to the affective component."*
**Resolution**: the identity is now stated over felt unpleasantness, with the asymbolia case
carried across and linked to [[pain-consciousness-and-causal-power]].

**2. Is-ought treated as dissolved where the source treats it as rejected (same paragraph).**
The article said *"This is not a naturalistic fallacy (deriving ought from is) because the phenomenal
property in question is already normative. The is and the ought are one."* The source now separates
two readings: *"On the logical reading, no 'ought' follows from purely 'is' statements without a
smuggled normative premise—which the position never violates... On the stronger ontological reading,
no property can be both descriptive and normative; that claim the position rejects."* The article
answered the logical reading and silently helped itself to the ontological one.
**Resolution**: both readings are now distinguished, and the ontological rejection is marked as
a commitment the position makes rather than a result it establishes.

**3. Constraint form derived from objectivity alone (§"From Objectivity to Alignment Criteria",
first bullet).** The article closed: *"This is why constraints are more appropriate than optimisation:
you do not negotiate with objective badness."* Objectivity is symmetric between badness and goodness;
it licenses no floor. `topics/phenomenal-value-realism`'s new **"The Sign of Aggregate Experience"**
section says so directly: *"It is silent on the exchange rate between felt badness and felt goodness,
and on whether the two counterbalance at all—which leaves the sign of aggregate experience open."*
That section also states the consequence for exactly this article's domain: *"The protective case for
artificial agents cannot lean on a value asymmetry."*
**Resolution**: the asymmetry is now disclaimed and the constraint form re-grounded on
[[haecceity]] (no interpersonal offsetting) plus Goodhart-resistance — which is also the reason
[[experiential-alignment]] itself gives: *"Rather than maximizing a weighted sum (which invites
Goodhart manipulation), the objective specifies constraints."*

**4. "Dissolve" overclaims what the source now concedes (§"What Would Challenge This View?",
condition 4).** The article said *"The Map's position is that these apparent counterexamples dissolve
on phenomenological analysis."* `consciousness-value-connection` now says the opposite about both
halves of that family — of Moore: *"Moore's test is a real datum and the Map takes it as one,
disputing the reading rather than the case"*; of the welfare-subject literature (Carruthers,
Mogensen, Bradford): *"This is the rival family the connection is most exposed to, and the exposure
is recorded below rather than argued away."*
**Resolution**: condition 4 now says the Map disputes the readings rather than the cases, and names
the welfare-subject family as live exposure.

### Medium Issues Found

**5. Falsifiability section omitted its source's only live defeater.** The article listed five
challenge conditions, all conceptual or long-run. `topics/phenomenal-value-realism` closes its own
equivalent section with *"None has occurred, and they are not equally remote: the last names an active
research programme rather than a hypothetical, which makes it the condition under live pressure"* —
the last being **"Predictive construction shown sufficient"** (interoceptive / active-inference
accounts of valence). The article's Stage 2 rests entirely on the identity claim that condition
targets, yet never named it. **Resolution**: added as condition 6, cross-linked to
[[the-steelman-for-value-blind-selection]]. No new bibliographic citation was introduced — the
corpus article carries the Joffily & Coricelli reference.

**6. Pluralist extension attributed by omission to Rawlette (§"From Objectivity to Alignment
Criteria", second bullet).** The article moved from a Rawlette-sourced Stage 2 straight to eight
dimensions including agency, meaning, understanding and connection. Two dependencies now flag the
extension explicitly — `topics/phenomenal-value-realism`: *"Rawlette defends a hedonistic version:
pleasure and pain exhaust intrinsic value. The Map extends this to phenomenal value pluralism"*;
`consciousness-value-connection`: *"Her own version is hedonistic... and the extension to beauty,
knowledge, love and meaning is the Map's, not hers."* **Resolution**: the extension is now marked
as the Map's, linked to the source's own `#Beyond Hedonism` section. The same edit carries
[[experiential-alignment]]'s own qualifier, which the article had also dropped: *"These dimensions
are not exhaustive. They represent a working hypothesis about what matters experientially."*

**7. Internal over-claim on manipulation resistance.** §"Why Preferences Lack Objective Standing"
already qualifies: *"Context, expectation, and even placebo effects can modulate the intensity of
experiential states—but they cannot make agony pleasant."* Three sections later the flat form
returned: *"You cannot manipulate what agony feels like."* The 2026-04-06 fix and the three
subsequent verification passes had checked the first locus, not the second.
**Resolution**: second locus brought into line with the first.

### Counterarguments Considered

- **The is-ought objection (the article's central exposure).** *Verdict: the value half was argued,
  the normative half was assumed.* The article earned "suffering is objectively bad" through its
  three-stage argument, then moved without argument to "a fact to be respected", "you do not
  negotiate with objective badness", and "would fail alignment" — each of which requires that an
  objective disvalue generate an agent-directed requirement. The corpus has a dedicated treatment of
  precisely this step at [[consciousness-and-normative-force]] (deep-reviewed 2026-09-09), which
  states the gap the article had elided: *"This is related to but distinct from Hume's is-ought gap,
  which concerns logical derivation. The problem of normative force is phenomenological: even when
  you* accept *a normative claim, what makes it grip you?"* The article linked neither that article
  nor the demand-character machinery. **Resolution**: a new paragraph closes
  §"The Objectivity of Experiential Qualities", grounding the bridge in demand character, marking it
  as a further commitment rather than a corollary of the objectivity argument, and inheriting the
  apex's grading (`moral-architecture-of-consciousness` L168: phenomenal value realism has "the
  strongest independent case"; "Normativity loses much of its force without genuine agency"). It
  also draws the alignment-specific consequence — a system with no phenomenal states cannot feel a
  demand, which is why `experiential-alignment` makes human authority over the targets a governance
  requirement.
- **Bedrock, not re-flagged**: illusionist, eliminativist, physicalist and MWI-defender disagreement
  with the tenet base; the first-person epistemic challenge (answered by the telescope analogy and
  triangulation); the conditional framing "if the Map's metaphysics is correct".

### Publisher-of-Record Citation Web-Verify

**Skipped by the §2.4 trigger clause, correctly.** The References block is byte-identical since the
last deep-review, and the only body commit in the window (`e182ca02d2`) inserted one wikilink —
"a cosmetic-cross-link no-op pass on a stable References list can skip". All six entries were
publisher-verified across the 2026-06-02 and 2026-07-14 passes; the full ledger stands in
[[deep-review-2026-07-14-alignment-in-objective-experiential-terms|the 2026-07-14 archive]].
No new bibliographic citations were added by this pass — every addition cross-links to a corpus
article that carries its own sources. `find_superlative_claims` returned empty; no currency sweep
needed.

### Possibility/Probability Slippage Check

Finding 3 is the closest thing to slippage in the article, and it is a sibling rather than an
instance: the article did not upgrade an empirical claim's evidential tier on tenet-load, but it
*did* treat a metaphysical result (badness is objective) as if it had delivered a structural
consequence (therefore a floor rather than a target) that the axiology explicitly does not supply.
A tenet-accepting reviewer would flag it — which is the diagnostic test — so it was treated as
correctable, not as bedrock. Fixed. No tier-labelled empirical claims elsewhere in the article.

### Reasoning-Mode Classification

- **Preferentism** — engaged as a generic position, not a named author's framework, so no
  named-opponent classification is triggered. The engagement is nonetheless Mode Two in shape:
  preferentism is charged with helping itself to conscious subjects while ignoring what makes them
  matter, using a standard it endorses (that welfare is what is good *for* someone).
- **Illusionism** (Tenet-1 sub-section, and challenge condition 1) — **Mode Three**, framework-boundary
  marking, honestly stated.
- No editor-vocabulary leakage in prose; checked the article against the forbidden-label list.

### Attribution / Internal-Consistency Check

Findings 1, 2, 6 are the misattribution and dropped-qualifier hits; finding 7 the self-contradiction
hit. All fixed. No other attribution defects found.

### Link Integrity

All new bare wikilinks verified present in `build_content_index` before writing:
`consciousness-and-normative-force`, `the-steelman-for-value-blind-selection`,
`pain-consciousness-and-causal-power`, `consciousness-value-connection`,
`moral-architecture-of-consciousness`, `experiential-alignment`, `haecceity`. Anchors
`topics/phenomenal-value-realism#suffering-focused-asymmetry` (explicit `{#...}` in source) and
`#Beyond Hedonism` (form already used by `consciousness-and-normative-force`) both target live
headings. All five `tenets#^...` anchors still resolve.

## Optimistic Analysis Summary

### Strengths Preserved

- The **epistemic vs metaphysical objectivity** distinction (§"Two Senses of Objective") — the
  article's original contribution, untouched, and it survives every dependency change in the window.
- The front-loaded thesis paragraph; the three-stage argument skeleton.
- §"Objectivity Without Universality" — **checked and found sound**. This was the section flagged as
  a possible site of an unearned move, and it is not one: it argues *against* a stronger conclusion
  (objective ingredients do not dictate a single recipe), and the nutrition analogy is a real
  disanalogy-resistant one. It is also consistent with `phenomenal-value-realism`'s new
  incommensurability material, which reaches the same place from the other direction.
- §"The Measurement Problem Does Not Undermine Objectivity" — sound, and its triangulation summary
  is **verbatim-faithful** to `experiential-alignment`'s current text (self-report, trained
  introspection, physiological correlates, behavioural indicators; divergence as signal).
- The five-tenet §"Relation to Site Perspective", including the target-side / threat-model-side
  complementarity note.

### Enhancements Made

- Normative-force bridge paragraph (new; §"The Objectivity of Experiential Qualities").
- Asymmetry disclaimer and re-grounding of the constraint form (§"From Objectivity to Alignment
  Criteria", first bullet).
- Rawlette-scope and working-hypothesis qualifications (same section, second bullet).
- Affective-component identity + asymbolia; two-reading is-ought treatment (Stage 2).
- Challenge condition 6 (predictive construction); condition 4 re-calibrated.

### Cross-links Added

- [[consciousness-and-normative-force]] — body, Further Reading, and `related_articles`. The
  corpus's dedicated treatment of the article's own load-bearing step, previously unlinked from it.
- [[pain-consciousness-and-causal-power]] — asymbolia.
- [[the-steelman-for-value-blind-selection]] — the deflationary reading at full strength.
- [[topics/phenomenal-value-realism#suffering-focused-asymmetry]] and `#Beyond Hedonism` — anchored
  into the two sections that grew the qualifications.

### Style

- Removed three "not X but Y" / "This is not X. It is Y." constructions (Stage 3's triple negation,
  the telescope paragraph, the diversity-maintenance closer, the Minimal-Quantum-Interaction
  clause) and one generic **"load-bearing"** intensifier ("Dualism is alignment-load-bearing" →
  "Dualism bears on alignment").
- The `description`'s dash-contrast ("an objective fact—not a preference") was examined and
  **deliberately left**: it is a positive claim with a trailing contrast, not the two-sentence LLM
  tic the guide bans, and `description` is the search/social meta field where churn has an SEO cost.

## Remaining Items

- The article is now 2985 words against a 3000 soft threshold. **The next substantive addition
  will require length-neutral mode.** Trim candidates identified but not taken: the four-bullet
  §"Why Preferences Lack Objective Standing" carries some restatement between bullets 1 and 4.
- `topics/phenomenal-value-realism` is at 3979 (`soft_warning`) and
  `moral-architecture-of-consciousness` at 4743 (`soft_warning`). Neither is this article's business,
  but both are now large enough that further qualification-growth there will keep producing drift
  in dependents. The dependency-drift lens used here is worth re-running on the other articles that
  cite those two.

## Stability Notes

**The clean-streak metric was actively misleading here.** Five consecutive reviews had converged on
"no changes needed", and the sixth found four critical issues — none of which existed when the fifth
ran. Every one arrived from underneath, through a dependency. Future reviews of a long-stable article
should ask what moved *under* it, not only what moved *in* it.

Do NOT re-flag:

- Bedrock disagreement with illusionists, eliminativists, physicalists and MWI defenders. Framework
  boundary, correctly marked.
- The conditional framing "if the Map's metaphysics is correct".
- The first-person epistemic challenge (telescope analogy + triangulation).
- The `description`'s dash-contrast (examined 2026-09-10, deliberately kept — see Style above).
- The citation block: six entries, all publisher-verified 2026-06-02 / 2026-07-14, unchanged since.

Newly settled by this pass, and not to be re-litigated as defects:

- The normative-force step is a **further commitment** resting on demand-character phenomenology,
  not a corollary of the objectivity argument. It is now stated as such. That it is weaker than the
  value claim is the apex's own grading, not a flaw introduced here.
- The suffering floor's asymmetry comes from haecceity and Goodhart-resistance, **not** from the
  objectivity of badness. Any future edit that re-derives the floor from objectivity alone is a
  regression of finding 3.
