---
title: "Deep Review - Phenomenal Contrast Method"
created: 2026-11-15
modified: 2026-11-15
human_modified: null
ai_modified: 2026-11-15T21:36:53+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-2
ai_generated_date: 2026-11-15
last_curated: null
---

**Date**: 2026-11-15
**Article**: [[phenomenal-contrast-method|Phenomenal Contrast Method]]
**Previous review**: [[deep-review-2026-07-31-phenomenal-contrast-method|2026-07-31]]
**Review number**: 7th (prior: 2026-03-17, 2026-04-17, 2026-04-28, 2026-06-01, 2026-07-07, 2026-07-31)
**Outcome**: FIVE critical repairs, one orphan reference cited. 2,084 → 2,237 words (concepts soft 2,500 / hard 3,500).

## Why This Page

`scripts/deep_review.py next` returned `concepts/interface-threshold`. The first thirteen
candidates were passed over: eleven are named on a File or Secondary line of a pending task
above `## Completed Tasks` (interface-threshold, metaphysics-of-information-under-dualism,
pain-consciousness-and-causal-power, indian-philosophy-of-mind, epistemic-emotions,
interface-friction, substrate-independence, pairing-problem,
the-steelman-for-value-blind-selection, purpose-and-alignment,
consciousness-and-the-problem-of-other-properties) and two were on the driver's skip list
(clinical-dissociation-as-systematic-evidence, phenomenal-acquaintance). This page was the
fourteenth candidate (score 76) and the first clear one. Its only mention in the open part
of the todo is a dependency note inside another task.

## Scope of This Pass

Six earlier reviews called this page converged, and the 2026-07-31 pass was a no-op. Those
reviews certified the citations on metadata. This pass checked what the cited works say, and
that is where every finding below came from. The stability notes on framework commitments
were honoured; none of the repairs touches a bedrock disagreement.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Siegel example misattributed (attribution error).** The page said Siegel "argues that an
   ornithologist seeing a pine grosbeak has a different phenomenal experience from a novice."
   Siegel's case is pine *trees*: one subject before and after acquiring the ability to
   recognise them. No source found puts a grosbeak or an ornithologist in Siegel; the 03-17
   and 06-01 reviews both certified "pine grosbeak" as accurate. **Repaired**: the subsection
   now gives the pine-tree case.
2. **Siegel's conclusion presented as support for cognitive phenomenology (stance error).**
   The page drew "cognitive states contribute to phenomenal character" from her case. Siegel
   concludes that the *visual* experience represents the kind property, and argues against
   explaining the contrast by an accompanying judgement. **Repaired**: her conclusion is
   stated as perceptual and the Map's use of the shared structure is marked as the Map's.
   She is also now credited with naming the "method of phenomenal contrast", which the page
   had not attributed to anyone.
3. **Kay, Keogh & Pearson 2024: non-verbatim quotation and unmeasured "neural correlates".**
   `"slower but more accurately"` is not in the paper; the abstract reads "slower, but more
   accurate responses than controls" and the title "Slower but more accurate". The paper is
   behavioural (two rotation tasks plus strategy reports) and has no neural data, yet the
   page claimed "measurable behavioural and neural correlates". **Repaired**: quotation marks
   removed, "neural" removed, "imagery-based" corrected to the abstract's "object-based".
4. **Zeman 2024 cited for a result it does not report.** The page said the aphantasia
   literature documents "the cognitive contrasts of understanding, recognising, and grasping
   persisting across that spectrum", and that "people who lack mental imagery still report
   phenomenal differences between understanding and not understanding". Zeman's review
   reports prevalence, heritability, multi-modality and associations (including face
   recognition *difficulty*); no study tests the understanding contrast across the spectrum.
   **Repaired**: Zeman is cited for the spectrum only; Lennon's argument is described as
   abductive, with "some thoughts" restored and "falsifying" replaced by the abstract's
   "counterexample"; the page now says outright that the contrast itself is untested.
5. **Knowledge-argument parallel overstated (calibration error).** The page said both
   arguments "demonstrate that phenomenal facts exceed what physical or functional
   description can capture" and that "in both cases, complete physical information fails".
   A contrast case holds sensory input fixed and nothing else: the two listeners differ in
   brain state and function. A tenet-accepting reviewer would flag this. **Repaired**: the
   parallel is stated as partial, and the closing sentence of the tenet section now says
   "beyond sensation into thought and agency" in place of "beyond what physical and
   functional accounts predict".

### Medium Issues Found

- **Bidirectional Interaction paragraph** asserted the felt difference "is not a passive
   observation ... but a marker of consciousness actively shaping action". The contrast shows
   a phenomenology of authorship; efficacy is a further claim. Reworded as the Map's reading,
   with the limit stated. "support" → "fit".
- **Bayne & Montague 2011** was in References and cited nowhere (earlier reviews reported no
   orphans). Now cited in Introspective Reliability as collecting both sides of the dispute.

### Citation Web-Verify Ledger

- Siegel 2010 (*The Contents of Visual Experience*, OUP) — metadata real-correct; **content
  wrong, repaired** (items 1 and 2). Checked against a course handout on Siegel's natural-kinds
  argument (pine trees, recognitional disposition, reply to the accompanying-judgement
  objection; zero hits for bird, ornithologist, grosbeak) and two searches. The book itself was
  not opened; the "hired to cut down the pines" detail was left out because it was not seen in
  a fetched source.
- Kay, Keogh & Pearson 2024 — real-correct metadata (Crossref: *Consciousness and Cognition*
  121, 103694). Result direction confirmed from the abstract (OpenAlex): slower, more accurate,
  analytic strategies; behavioural only. **Quote and "neural" repaired** (item 3).
- Zeman 2024 — real-correct (Crossref: *Trends in Cognitive Sciences* 28(5), 467–480).
  Abstract read; **claim re-scoped** (item 4). Reference entry lacks volume and pages; left.
- Lennon 2023 — metadata real-correct (carried from 07-31). Abstract read via OpenAlex. The
  quoted span `"no sensory reduction base"` is verbatim, three times, in Lennon's own 2022
  précis of the argument on The Junkyard ("Aphantasics have some thoughts, aphantasic thoughts,
  that have no sensory reduction base"). **The chapter text is still unverified**: philarchive
  and philpapers returned 403 again. The quote is the author's own wording for this argument;
  whether the chapter prints it identically is open.
- Schwitzgebel 2008 — not re-opened; verbatim confirmed 07-31, text unchanged.
- Strawson 1994, Pitt 2004 — metadata carried from 07-07; the page paraphrases both and quotes
  neither. Strawson's Jack/Jacques case not re-read at source this pass.
- Bayne & Montague 2011 — real-correct; now cited inline.
- Inline ↔ References on (surname, year): all eight external entries now cited; no in-text
  citation lacks an entry. The scary-narrative task (L86) is mentioned without a citation and
  makes no result claim.
- Map-internal quotation: "retronasal smell is experienced as taste" matches
  `voids/modality-void` L58 as it stands today.
- Currency sweep: `find_superlative_claims` returned nothing.

### Counterarguments Considered

- Functionalist, eliminativist and heterophenomenological resistance: bedrock, per the standing
  stability notes; not re-flagged.

## Reasoning-Mode Classification (editor-internal)

- Functionalism (AI subsection): Mode Two then boundary-marking; unchanged.
- Schwitzgebel: Mode Three, calibrated; unchanged.
- Sensory-reduction sceptic (Prinz-style constraint): now Mode One in form. The reply rests on
  Lennon's abductive premise, and the page says so.

## Optimistic Analysis Summary

### Strengths Preserved
- The three-step statement of the method; the stark-versus-graded calibration of the
  Schwitzgebel reply; the scope concession; "does not prove dualism on its own".

### Enhancements Made
- The knowledge-argument section now says what a contrast can and cannot show, which is the
  restraint the Hardline Empiricist persona asks for.
- Siegel credited as the method's namer.

### Cross-links Added
None.

## Remaining Items

- Lennon chapter text for `"no sensory reduction base"` (see ledger).
- Zeman 2024 reference entry lacks volume, issue and pages (28(5), 467–480).
- L66 anarchic hand: "strips away the agentive phenomenology while preserving sensory and motor
  signals" is uncited and was not checked.

## Stability Notes

- Carried forward unchanged: heterophenomenology, scope problem, functionalist resistance,
  Schwitzgebel engagement (do not re-strengthen; quote is verbatim), eliminativism, Lennon
  venue.
- **Superseded**: "sensory reduction (responded via aphantasia/dissociation + Lennon/Zeman)"
  settled the *shape* of the reply. It had not settled what Zeman and Lennon report. The reply
  is now scoped to what they do report; do not restore the "persisting across the spectrum"
  claim without a study that tests it.
- Do not restore "pine grosbeak". Do not re-quote Kay et al. unless the words are copied from
  the paper.
- The knowledge-argument parallel is deliberately partial. A contrast fixes sensory input only.
