---
ai_contribution: 100
ai_generated_date: 2026-11-10
ai_modified: 2026-11-10 23:08:22+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-10
date: &id001 2026-11-10
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-10 23:08:22+00:00
modified: *id001
related_articles: []
title: Cross-Review - Emotion Regulation and the Timing of Control
topics: []
---

**Date**: 2026-11-10
**Article**: [Emotion Regulation and the Timing of Control](/topics/emotion-regulation-and-the-timing-of-control/)
**Previous review**: [2026-10-24](/reviews/deep-review-2026-10-24-emotion-regulation-and-the-timing-of-control/)
**Mode**: cross-review, integration only. No deep pass: the article was deep-reviewed at 2026-10-24 02:04Z and its Stability Notes were read first. `last_deep_review` is left at 2026-10-24T02:04:03Z.
**Link plan**: [optimistic-2026-10-24-fresh-article-wing](/reviews/optimistic-2026-10-24-fresh-article-wing/) §"ER cross-review (L3066)"; outer-review addenda [outer-review-2026-10-31-chatgpt-5-6-sol-pro](/reviews/outer-review-2026-10-31-chatgpt-5-6-sol-pro/) (improvements 16, 21, 22) and [outer-review-2026-10-31-claude-opus-5-5](/reviews/outer-review-2026-10-31-claude-opus-5-5/) §4.

## Quote Re-verification (raw PubMed abstracts, E-utilities efetch, string counts)

- Sheppes & Gross 2011 (PMID 21233326): "require effort that is proportional to the intensity of the emotional response" count 1; "require minimal effort" count 1; the abstract frames both as an "alternative process-specific timing hypothesis", so "hypothesise" is accurate. Negative control "require maximal effort" 0. Metadata real-correct (*PSPR* 15(4):319-31).
- Ochsner, Bunge, Gross & Gabrieli 2002 (PMID 12495527): "prefrontal cortex is involved in constructing reappraisal strategies that can modulate activity in multiple emotion-processing systems" count 1; control 0. Metadata real-correct (*J Cogn Neurosci* 14(8):1215-29).
- Buhle et al. 2014 (PMID 23765157): "48" count 1 ("a meta-analysis of 48 neuroimaging studies of reappraisal"); "the use of cognitive control to modulate semantic representations of an emotional stimulus" count 1; control 0. Metadata real-correct (*Cereb Cortex* 24(11):2981-90).
- Sheppes & Meiran 2008 (PMID 19102598), for the research-note annotation: "Late distraction but not reappraisal impaired memory encoding" count 1; "self control resources" count 1; "Stroop" 0 in the abstract (the Stroop measure is from the full text, per the 2026-10-24 review L29).

## Hosts Edited (each OLD count 1 immediately before replacement, NEW count 1 after)

| Edit | Host | Change | Words |
|---|---|---|---|
| E1 | `concepts/self-control-as-skill-and-scaffolding` L46 | "whose authors had already narrowed" → "whose proponents had already narrowed" (the 1998 model is Gross's alone; the narrowing is Sheppes and Gross 2011) | 3038 → 3038 |
| E2 | `concepts/mental-effort` L106 | "costly mainly when begun late" → "less effective when begun late" (rests on Sheppes & Meiran 2007's efficacy result, not the 2008 depletion measure) | 3360 → 3360 |
| E3 | `concepts/control-theoretic-will` L74, end of §Stabilisation | appended the Sheppes and Gross (2011) "hypothesise" sentence linking `#not-uniform`; reference added alphabetically between Schwartz & Begley and Stapp | 2907 → 2966 (+59) |
| E4 | `topics/clinical-neuroplasticity-evidence-for-bidirectional-causation` L108 | appended the Ochsner/Buhle sentence linking `#stapp-example`; references 23 and 24 added | 3732 → 3840 (+108) |
| E5 | `voids/numbing-void` L56 | zero-word pipe on "emotion regulation" | 2821 → 2821 |
| E6 | `topics/precommitment-and-the-diachronic-agent` L66 | zero-word pipe on "situation modification" to `#five-points` | 2941 → 2941 |

### E4 re-anchoring and references

The plan's OLD anchor ("preventing decoherence into alternative states.") is gone, because L108 was rewritten. The sentence was appended after the paragraph's new last sentence, "the authors take decoherence into account rather than claiming attention prevents it." Two wording changes from the plan: "so it adds no stream" became "so the example adds no stream", because "it" could be read as the meta-analysis; and "(Buhle et al. 2014)" became "(Buhle et al., 2014)", the host's comma style. "Their" still refers to Schwartz, Stapp and Beauregard through "the authors". The next paragraph's "This proposal is speculative" still refers to the Zeno proposal. The L102-L104 down-count is untouched, and reappraisal is explicitly not counted as a stream.

The host's numbered References list is in accretion order, neither alphabetical nor first-citation: Baxter 1992, first cited at L42, is #20, and entries 12-22 were all appended. Following that convention, Ochsner went in as 23 and Buhle as 24, in in-sentence citation order, with no existing entry moved. The list now runs 1-24 contiguously. The body has no numeric cites, so no in-text number depended on the order.

## Article Edits (outbound, zero-word)

- E7, L95: "writing about assent," → "writing about [assent](/topics/assent-before-descartes/#stoic-double-claim),". The target traces Stoic *synkatathesis* from Zeno of Citium.
- Claude-leg addendum, L53: "from the conscious selection the Map discusses elsewhere" → "from the [conscious selection](/topics/trilemma-of-selection/) the Map discusses elsewhere". The phrase is true of the target, whose third horn is consciousness selecting among options. That page's depletion-wording P1 has landed: no "deplet" string remains.
- Word count 3606 → 3606.

## Declines and Skips

- `[[attention-and-the-consciousness-interface]]`: skipped. No existing ER phrase is true of it. The one fitting phrase, "active inference" (L93), is already linked to `consciousness-selecting-neural-patterns#the-active-inference-rival`. Pipes on the process-model table's "attentional deployment" or "on what is attended" would imply that the strategy family is where the interface acts, against the article's fit-not-evidence calibration.
- `concepts/skill-delegation` and `topics/valence-as-a-natural-kind`: skipped. Neither mentions emotion regulation, reappraisal or the process model, so neither offers a zero-word anchor. ER already links both.
- Optional reverse Further Reading line on `topics/assent-before-descartes`: not added (not in the brief).
- No additions, as declined, to immediate-emotions, epistemic-emotions, stapp-quantum-mind, libet-experiments, attention-as-interface, conscious-vs-unconscious-processing, valence-and-conscious-selection or epiphenomenalism.

## Research Note Annotations

[emotion-regulation-and-the-timing-of-control-2026-10-23](/research/emotion-regulation-and-the-timing-of-control-2026-10-23/): dated `[2026-11-10 note: …]` brackets were appended at L306 (the Sheppes & Meiran 2008 entry's Flag) and L799 (§Evidence not to lean on). Both record three points: the memory-encoding impairment is a cost of late *distraction* and cannot stand in for a reappraisal cost; the 2008 reappraisal cost is a subsequent-Stroop ego-depletion measure; and late reappraisal should rest on the 2007 efficacy result. Nothing else in the note changed. Its pre-existing "at any stage" and "load-bearing" strings predate this pass and were left alone.

## Guards Honoured

- The superseded wording "needs no conscious contribution at any stage" is installed on no host. The new sentences contain no "at any stage", and no ego-depletion support.
- E3 presents "require minimal effort" as Sheppes and Gross's hypothesis. The L82 Tenet 2 caution in control-theoretic-will is untouched.
- numbing-void L100's "an illustration, not an instance" is untouched.
- No "This is not X. It is Y." and no "load-bearing" in any new text.

## Remaining Items

None for this task. Observation only: ER's Further Reading glosses [numbing-void](/voids/numbing-void/) as "proactive down-regulation as a field instance", while numbing-void L100 calls the Bidirectional Interaction case "an illustration, not an instance". The two use "instance" in different senses (an instance of proactive regulation, against an instance of the tenet), so they are compatible. A future pass on either page could still make the wording consistent.

## Stability Notes

- All 2026-10-24 Stability Notes stand. The one exception is the note on "Regulation needs no conscious contribution at any stage", which the 2026-10-31 P1 rescoped to "no conscious regulatory goal or supervision and no awareness of regulating". The article's L37 and L75 carry the rescoped form, and no host should receive the older wording.
- The inbound cluster now covers eight hosts: alief-and-acting-against-belief, emotion-and-dualism, mental-effort, self-control-as-skill-and-scaffolding, control-theoretic-will, clinical-neuroplasticity, numbing-void and precommitment. Further integration passes should not add hosts without a new article to integrate.
- The clinical-neuroplasticity sentence is the down-count's reciprocal of ER's Stapp example. Do not strengthen it into a fourth evidence stream, and do not trim it as redundant with ER.