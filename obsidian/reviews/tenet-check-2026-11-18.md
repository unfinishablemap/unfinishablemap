---
title: Tenet Alignment Check - 2026-11-18
created: 2026-11-18
modified: 2026-11-18
human_modified:
ai_modified: 2026-11-18T20:28:36+00:00
draft: false
description: "Tenet check 168, a grep-led check of 912 pages for tenets used as evidence: no Errors. 87 sentences say a tenet is supported, 21 of 125 void tenet sections are not at the register's grade, and four repair tasks are proposed."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: Andy Southgate
ai_system: claude-fable-5-2
ai_generated_date: 2026-11-18
last_curated:
---

# Tenet Alignment Check

**Date**: 2026-11-18
**Files checked**: 912 by pattern scan (topics 371, concepts 371, voids 125, apex 45); 125 void tenet sections extracted and classified; positions (30) scanned for section D only
**Errors**: 0
**Warnings**: 87 above-grade sentences (section A) in about 78 pages; 21 void pages with an above-grade tenet sentence (section B, overlapping A); 10 paraphrase flags (section C)
**Notes**: about 20 borderline sentences, listed by file only

## Summary

No page contradicts a tenet. The live defect is the opposite one: pages that say a tenet is supported, gains support, receives evidence or is vindicated by material that the Map's own register grades as compatible at most. The register is explicit (quoted below), and a majority of pages already follow it: of 125 void pages, 87 state a denial or an equivalent grade in their tenet section. The remainder is concentrated in older "Relation to Site Perspective" sections that open with "**Tenet** receives support" and in hub pages that count premise-sharing arguments as independent lines.

Method was grep-led, as directed. Every hit of the ten driver patterns was read at sentence level with its neighbouring sentence; every sentence listed as above grade was read with its whole paragraph. What was not read is stated at the end.

## The tenets as currently worded

From `obsidian/tenets/tenets.md` (`ai_modified` 2026-11-13), one-line statements and the scope words each carries:

1. **Dualism**: "There is more than just matter involved in reality." Definition: consciousness "is not reducible to physical processes"; "neutral between substance and property dualism"; "What matters is irreducibility". The rationale is headed "a commitment the Map owns, not a result it reports", and says the explanatory gap "is what motivates the commitment" and that the judgement "is contested".
2. **Minimal Quantum Interaction**: "The smallest possible non-physical influence on physical outcomes." Conditional in form: "*If* consciousness can influence the physical world, it must do so at the quantum level". Mechanisms are "candidate mechanisms"; post-decoherence selection is "the strongest path the Map currently endorses"; the tenet "makes a *consistency claim* ... rather than a *novel-prediction claim*". No mechanism is named as established.
3. **Bidirectional Interaction**: "Consciousness is not a passive observer—it causally influences the physical world." No quantifier. "The tenet commits to the *that*, not a unique *how*". It is held as "*a metaphysical commitment supported by self-stultification and indirect evidence, not as a directly introspectible datum*"; the interface argument shows downward causation "*available*" and not "*actual*"; self-stultification is "the deepest difficulty for epiphenomenalism rather than its refutation".
4. **No Many Worlds**: "The many-worlds interpretation of quantum mechanics is rejected." Rejected, on the indexical objection, "scoped"; the multiplicity objection is "a registered cost, not a refutation"; the dependency on a non-deflationary "I" "does not refute the tenet; it locates where its strength comes from".
5. **Occam's Razor Has Limits**: "Simplicity is not a reliable guide to truth when knowledge is incomplete." A limit on an inference: the razor is "a useful heuristic but not a law of nature"; "parsimony cannot decide for or against a framework when the relevant knowledge is incomplete". The tenet "binds the Map's use of parsimony, not only its critics'".

One wrinkle the operator should know before reading section A: the tenets page itself uses support language for Tenet 3 ("supported by self-stultification and indirect evidence"; a paragraph headed "Indirect empirical support from comparative cognition", graded there as "suggestive but contested corroboration"). Pages that repeat that wording for Tenet 3 are transcribing the tenet page, and I classed them compliant.

## The register grade applied

- `positions/methodology-and-calibration` P-M1: "A tenet may *remove a defeater* ... but defeater-removal never raises the evidential tier of a claim. The absence of a principled barrier is not the presence of positive evidence."
- P-M2 (same file): any convergence is "a *single observation read N times* ... *until* the convergence passes a structurally distinguishing test".
- `positions/voids-as-evidence` P-V3, updated today: "as a catalogue entry a void adds no weight to any tenet, and an argument a page names from outside the catalogue is reported at that argument's grade and no higher."
- `positions/replies-to-rivals` P-RR1: the reply to illusionism has "this grade and no higher"; the Map's own starting points "supply what the illusionist declines and no evidence against him (P-M1)". It does not claim "that the regress, Tallis or Strawson settles the matter".
- P-RR2: the beautiful-loop theory "remains a live and serious rival, defeated neither by the tenets nor by decisive evidence"; the Map's side "comes from Tenet 1 and supplies no evidence against the theory (P-M1)".

Classification used below. **Compliant**: denies support, states compatibility, states the claim as the Map's reading or commitment, or is conditional on an argument whose contested status the paragraph gives. **Above grade**: says a datum, a void, a rival's difficulty or a convergence supports, evidences, strengthens or vindicates a tenet, with no discriminator named, or with the rival named and no reason given why the rival predicts it less well. **Borderline**: support language whose own paragraph retracts most of it.

## A. Tenets used as conclusions or as evidence

### Driver patterns (body text, frontmatter excluded, case-insensitive, whole files)

| # | Pattern | Hits | Files | Above grade | Borderline | Compliant or not about a tenet |
|---|---|---|---|---|---|---|
| A1 | `supports the (Map's )?(dualis\|tenet)` | 6 | 6 | 2 | 0 | 4 |
| A2 | `support for (the )?(dualis\|tenet\|bidirectional\|minimal quantum)` | 17 | 17 | 0 | 0 | 17 (most are denials: "supplies no support for dualism") |
| A3 | `gains (indirect )?support` | 12 | 12 | 5 | 3 | 4 |
| A4 | `strengthens the (Map\|case\|tenet\|dualis)` | 28 | 27 | 5 | 4 | 19 |
| A5 | `vindicat` | 146 | 115 | 2 | 1 | 143 |
| A6 | `confirms (the )?(tenet\|dualis\|Map)` | 2 | 2 | 0 | 0 | 2 |
| A7 | `evidence for (dualis\|the tenet\|bidirectional\|non-physical)` | 66 | 61 | 2 | 2 | 62 (most are denials: "not evidence for dualism") |
| A8 | `as the tenets? predict` | 0 | 0 | 0 | 0 | 0 |
| A9 | `is evidence that consciousness` | 2 | 2 | 1 | 0 | 1 |
| A10 | `cumulative (case\|weight\|abductive)` | 59 | 44 | 5 | 3 | 51 |
| | **Total** | **338** | | **22** | **13** | **303** |

The driver patterns under-count, because the corpus writes tenet names as wikilinks: "supports the `[[tenets#^dualism|Dualism]]` tenet" matches none of them. I added four wikilink-aware patterns and read their hits the same way.

### Supplementary patterns

| # | Pattern | Hits | Files | Above grade | Notes |
|---|---|---|---|---|---|
| S1 | `support(s\|ed\|ing)? (for )?(the )?(Map.s )?\[\[tenets` | 46 | 38 | 23 | 4 more are list-lead sentences whose list I did not read (below) |
| S2 | `tenets#…]] (tenet )?(gains\|is supported\|receives\|finds) ` | 104 | 78 | 22 | 21 are the denial form ("gains nothing evidential", "gains a reading and no evidence") |
| S3 | `(supports\|strengthens\|confirms\|corroborates\|vindicates\|favours) … (dualism\|bidirectional interaction\|interactionis…)` | 72 | 62 | 20 | 10 denial form; the rest mostly conditional on an argument. Counts in this table overlap one another and section A |
| S4 | `evidence (for\|that favours\|favouring) (the )?(Map.s \|\[\[)` | 20 | 19 | 4 | 6 denial form |

**Total above grade, de-duplicated: 83 sentences read in full paragraph (22 caught by the driver patterns, 51 more by the supplementary patterns, 10 found only by reading void tenet sections for section B), plus 4 list-lead sentences read as leads only: 87, in about 78 files.** Seven of the 83 are already named by an open task (marked "queued" below). About 20 further sentences are borderline.

### Above-grade sentences (25 entries listed of 87 sentences; prominence first)

1. `apex/apex-articles.md:312` — "the taxonomy is consistent with, and offers cumulative abductive support for, the Map's package" (queued: open task at todo L3591; the apex itself withdrew this on 2026-11-05).
2. `concepts/materialism.md:98` — "together they form positive arguments for dualism that converge on the same conclusion from independent directions. Precisely where materialism fails, dualism ... gains support."
3. `concepts/epiphenomenalism.md:88` — "shows how four independent argument types compound"; `:158` "Four independent argument types converge"; `:167` "Each succeeds or fails independently". Siblings `concepts/causal-closure.md:184` and `concepts/interactionist-dualism.md:93` say the same four run "in two families rather than four independent lines".
4. `concepts/explanatory-gap.md:177` — "The explanatory gap provides direct support for the Dualism tenet." Also `:81` "supporting the Dualism tenet". The tenet page says the gap "motivates the commitment" and that the judgement is contested.
5. `concepts/quantum-consciousness.md:73` — "a broader convergence of independent evidence lines that strengthens the cumulative case even where individual lines remain inconclusive."
6. `topics/hard-problem-of-consciousness.md:229` — "This supports the Map's Occam's Razor Has Limits tenet" (of mysterianism, a position and not a datum).
7. `topics/the-convergence-argument-for-dualism.md:175` — "the convergence of independent routes to this conclusion is part of why." The page's body grades the routes as partially independent.
8. `topics/quantum-measurement-and-consciousness.md:146` — "when independent lines of reasoning all point in the same direction, the cumulative case exceeds any individual argument."
9. `topics/consciousness-defeats-explanation.md:142` — "The convergence of independent failures strengthens the case ... Their convergence on a single boundary suggests a genuine feature of reality."
10. `topics/cognitive-science-of-dualism.md:140` — "The field's own dependence on first-person report as irreducible data actually supports the tenet". Also `:142` "finds indirect support" and `:148` "receives perhaps the strongest support from this analysis."
11. `topics/consciousness-in-simple-organisms.md:251` — "Simple organism research supports dualism by showing the hard problem is scale-independent ... exactly what dualism predicts". A physicalist who grants the gap predicts the same.
12. `topics/pragmatist-quantum-foundations-and-the-agent.md:135` — "Under Tenet 1 this is a vindication: any physics that places irreducible agents at its foundation is registering the very irreducibility dualism asserts."
13. `topics/consciousness-and-mathematics.md:190` — "Bidirectional Interaction receives the strongest domain-specific evidence." `:192` "Dualism is supported from both directions."
14. `concepts/inventory-blindness.md:105` — "Dualism gains indirect support. If inventory blindness is real and pervasive, dismissing dualism on grounds of parsimony becomes unreliable." This is defeater-removal named as support, P-M1's own example of the slide.
15. `concepts/introspection.md:167` — "The Occam's Razor Has Limits tenet gains support from training literature." `:169` "the 'contamination' worry becomes evidence for what the tenet claims."
16. `concepts/temporal-consciousness.md:190` — "If consciousness were identical to neural computation, some temporal experience should persist. Its absence supports the Dualism tenet" (queued: todo L4370).
17. `concepts/attention-as-interface.md:198` — "COGITATE (2025) found neither GWT nor IIT clearly vindicated—the Map's tenets point toward consciousness as an irreducible player". The apex `attention-as-causal-bridge.md:63` gives the registered form: "not a selection of dualism".
18. `concepts/naturally-occluded.md:137` — "why the evidence takes the indirect form it does (failure-signature specificity, cross-tradition convergence, the catalogue's clustering at the consciousness-matter interface)". The clustering is counted as evidence; P-V3 suspends that.
19. `concepts/epistemology-of-limit-knowledge.md:129` — "The convergence of failure signatures ... supports dualism abductively ... This support is genuine but bounded". `voids/what-voids-reveal.md:58` says of exactly this: "It should not be."
20. `voids/what-voids-reveal.md:148` — "Occam's Razor Has Limits is supported on the methodological front."
21. `voids/voids-between-minds.md:145` — "Dualism is most directly supported." Ten lines on, `:155`: "The Map does not read these voids together as evidence for dualism".
22. `voids/observation-and-measurement-void.md:152` — "Dualism predicts the void at every layer." `:154` "Occam's Razor Has Limits finds direct support here."
23. `voids/recognition-void.md:120` — "Occam's Razor Has Limits receives powerful support."
24. `topics/dual-domain-capabilities-in-proprioception-and-spatial-imagination.md:107` — "Minimal Quantum Interaction receives indirect support. If consciousness biases quantum outcomes in neural systems, the distribution of microtubules ... suggests the quantum interface extends to bodily awareness". The tenet is the premise of the sentence that supports it. (`:103` and `:105` on the same page are queued at todo L3676; `:107` is not.)
25. `topics/panpsychisms-combination-problem.md:131–133` — "The combination problem strengthens the Map's position in several ways. **Dualism gains by elimination.**" `concepts/manyism.md:68` states the rule this breaks: a rival's unmet burden "must not be misread as positive evidence for dualism".

**The remaining above-grade sentences, by file** (line; "q" = queued by an open task). Topics: comparative-phenomenology-of-meditative-traditions 169; consciousness-and-the-phenomenology-of-translation 155; dual-domain-capabilities 103q, 105q; emotion-and-dualism 137; phenomenology-of-anticipation 119; phenomenology-of-linguistic-failure 121; phenomenology-of-recursive-self-awareness 141; contemplative-practice-as-philosophical-evidence 193 (its own L83 says "emphatically not, on its own, evidence for dualism"); dream-consciousness 133; the-observer-witness-in-meditation 163; wheelers-participatory-universe-and-it-from-bit 148; phenomenology-of-philosophical-disagreement 112; quantum-holism-and-phenomenal-unity 176; aesthetics-and-consciousness 80; phenomenal-normativity-environmental-ethics 123; enactivism-challenge-to-interactionist-dualism 127 (link gloss). Concepts: apophatic-approaches 90; motor-selection 198; materialism 110; phenomenal-depth 86; conscious-vs-unconscious-processing 117; creative-consciousness 60; mental-imagery 155; integrated-information-theory 138; intentionality 83; mysterianism 64; spontaneous-collapse-theories 131q; subjective-aim 74; symbol-grounding-problem 41; temporal-consciousness 148; unity-of-consciousness 141; jourdain-hypothesis 37; cumulative-culture 36; attention-schema-theory 209; nihilism-and-existentialism 48; combination-problem 188; implicit-memory 77 (heading "Evidence for Bidirectional Interaction"); consciousness-selecting-neural-patterns 162. Voids: compound-failure-signatures 143q; valence-void 115q; void-as-ground-of-meaning 134; self-transcendence-void 113; epistemological-limits-occams-razor 102; conceptual-scheme-void 122, 126; imagery-void 133; sleep-consciousness-void 139; capability-division-problem 118; meaning-void 128; mood-void 115; decision-void 139; inference-void 134; question-formation-void 111. List-lead sentences, list not read: concepts/phenomenological-evidence 192 ("directly supports the Map's tenets:"); concepts/qualia 187 ("Qualia provide central support"); concepts/visual-consciousness 108 ("supports the Map's foundational commitments with particular force"); concepts/witness-consciousness 84 ("provides phenomenological support for Dualism:").

**Borderline, not counted**: topics comparative-phenomenology 177, consciousness-and-the-metaphysics-of-composition 129, decoherence-and-macroscopic-superposition 138, the-sublime-and-negative-aesthetics 44, the-naturalisation-failure-for-content 141, arguments-against-materialism 117, authorship-of-action-divergence 107, the-interface-problem 159, consciousness-and-mathematics 192, emergence-as-universal-hard-problem 109, consciousness-and-counterfactual-reasoning 72 (heading), free-will 149, enactivism-challenge 108; concepts phenomenology-vs-function-axis 126, baseline-cognition 142, sign-problem-for-conscious-observation 91, inventory-blindness 103, knowledge-argument 44; voids erasure-void 111ff; apex none.

**Compliant examples worth copying**: `topics/alief-and-acting-against-belief.md:129` "**Dualism** gains nothing evidential"; `topics/precommitment-and-the-diachronic-agent.md:115` "**Bidirectional Interaction** gains a location without support"; `topics/consciousness-as-activity.md:122` "It supports the tenets mainly by removing obstacles, not by proving them"; `concepts/qualia.md:193` "one line of evidence pressed three ways rather than three independent lines"; `voids/molyneux-void.md:93` "The tenet is illustrated ... and not vindicated, since nothing here shows a more complex answer true".

## B. The tenet sections of the void pages

All 125 files in `obsidian/voids/` (124 pages and the index `voids.md`) have a "Relation to Site Perspective" section; each was extracted whole.

| Class | Count | What it means |
|---|---|---|
| A. At grade | 87 | The section states a denial or an equivalent grade and has no sentence saying a tenet is supported. 67 found by marker scan plus a scan for unnegated support sentences; 20 more confirmed by reading their cue sentences |
| B. Mixed | 13 | A denial is present and so is a sentence saying a tenet is supported, receives support, or is what a void "predicts" |
| C. Above grade, no denial | 8 | |
| D. Silent | 17 | No evidential vocabulary either way; tenets used as a lens only. 11 of these had zero cue words and were not read in full |

Strict opener forms: 8 pages open "None of the Map's tenets is supported by …"; 24 link `#^p-v3`; 12 say "adds no weight" or "lends … no weight"; 12 say "and no evidence"; 31 pages carry at least one of the four. The other 56 at-grade pages use equivalents ("coherence rather than support", "offers a reading of this void rather than receiving support from it", "fits, without evidencing", "removes a defeater without adding weight (P-V2)").

**The four pages named in the brief are all at grade**: `transformative-experience-void` ("None of the Map's tenets is supported by the transformative experience void. **Dualism** gains a reading and no evidence."); `conceptual-impossibility` and `nomic-void` (both: "None of the Map's tenets is supported by this void. The tenets are the Map's chosen starting points, and as a catalogue entry the void adds no weight to them", with the `#^p-v3` link); `consciousness-only-territories` ("**Dualism** supplies the reading, not evidence ... as a void the page lends that no weight").

**Not at grade: 21 pages** (classes B and C), with the first sentence of the section and the offending sentence.

Class C (8):

1. `compound-failure-signatures` — opens "**Occam's Razor Has Limits** is most directly relevant."; "**Dualism** gains support from two directions." (queued, todo L219)
2. `observation-and-measurement-void` — opens "**Dualism** predicts the void at every layer."; "**Occam's Razor Has Limits** finds direct support here."
3. `conceptual-scheme-void` — opens "The void is load-bearing for two of the Map's five tenets and connects to two more."; "**Dualism** receives a novel defence."
4. `imagery-void` — opens "The Imagery Void engages two of the Map's tenets directly."; "The Map reads this as evidence that phenomenology has independent structure from the functional roles it accompanies—which is what Dualism predicts."
5. `sleep-consciousness-void` — opens "**Dualism** is most directly implicated."; "The void itself may be evidence that consciousness has properties physical description cannot capture."
6. `capability-division-problem` — opens "The Map's tenets frame the capability division problem as productive rather than devastating."; "Tenet 1 (Dualism) establishes that consciousness is irreducible to physical processes — so the boundary ... is real, not merely epistemic."
7. `interface-formalization-void` — opens "The interface formalization void is generated directly by the Map's tenets"; "**Dualism** establishes that consciousness is not reducible to physical processes".
8. `perceptual-reality-monitoring-void` — opens "The perceptual reality-monitoring void sits at exactly the consciousness–physics interface that the Map's bidirectional-interaction tenet posits."; "the empirical purchase of reality-monitoring strengthens the broader claim that interface-sites are systematically opaque".

Class B (13):

9. `what-voids-reveal` — opens "Both arguments connect to each of the Map's tenets."; "**Occam's Razor Has Limits** is supported on the methodological front."
10. `voids-between-minds` — "**Dualism** is most directly supported."
11. `valence-void` — opens "The valence void connects to the Map's foundational commitments at multiple points."; "**Dualism** finds particularly strong support." (queued, todo L219)
12. `recognition-void` — "**Occam's Razor Has Limits** receives powerful support."
13. `void-as-ground-of-meaning` — opens "The thesis connects to each of the Map's tenets: **Occam's Razor Has Limits** is most directly supported."
14. `self-transcendence-void` — opens "**Occam's Razor Has Limits** receives the most direct support."
15. `epistemological-limits-occams-razor` — opens "This article directly supports Tenet 5 (Occam's Razor Has Limits) by locating the limits not just in philosophy but in cognitive architecture."
16. `meaning-void` — opens "The meaning void connects directly to the Map's foundational commitments."; "**Dualism** finds qualified support."
17. `mood-void` — opens "The Map interprets the Mood Void as structural evidence — not proof — that the opacity of mood aligns with what the Map's tenets predict".
18. `decision-void` — opens "The Decision Void is unusually tenet-generated."; "the void's existence is what the mechanism predicts."
19. `inference-void` — opens "The Map treats the inference void as one of the better cases for **Occam's Razor Has Limits**."
20. `question-formation-void` — opens "The Map treats the question formation void as central to the case for **Occam's Razor Has Limits**."
21. `erasure-void` — opens "The erasure void connects most directly to **Occam's Razor Has Limits**."; "The erasure void is a place where the dualist picture predicts the strangeness rather than being embarrassed by it."

Class D (17 silent pages, listed so a later pass can add the opener if the operator wants uniformity): affective-void, aspect-perception-void, boundary-and-projection, commensurability-void, counterfactual-void, creative-aesthetic-void, embodiment-cognitive-limits, infant-consciousness, interested-party-void, metaphor-void, non-human-minds-as-void-explorers, normative-void, plenitude-void, simulation-detection-void, the-quantitative-comprehension-void, three-kinds-of-void, voids (index).

## C. Each tenet stated consistently

| Tenet | Probe | Hits | Files | Paraphrases that change the tenet |
|---|---|---|---|---|
| 1 | `substance dualis` | 191 | 87 | 0 state the tenet as substance dualism. `the Map's substance dualism` and `the Map (is\|endorses\|holds) substance dualism`: 0 |
| 1 | a tenet said to "establish" its own content | 4 | 4 | 4 (below) |
| 2 | `consciousness (collapses\|causes\|triggers) … collapse` | 34 | 20 | 0 stated flat as the Map's view; 6 pages say outright that it is not what the Map holds |
| 2 | a named theory as "the Map's mechanism" | 6 | 5 | 1 |
| 3 | universal reading invoked | 9 sentences | 6 pages | census below; not a defect |
| 4 | MWI "is false / refuted / incoherent / fails" | 21 | 19 | 2; 13 of the 21 are explicit denials that the Map refutes it |
| 5 | Occam "licenses …" | 8 | 8 | 0 firm, 3 to watch |
| 5 | `more complex (theory\|account) is (preferred\|more likely)`, `because parsimony is unreliable` | 0 | 0 | 0 by pattern; 2 found by reading |

Examples.

**Tenet 1, tenet as proof of itself (4 of 4):** `voids/interface-formalization-void.md:119` "**Dualism** establishes that consciousness is not reducible to physical processes"; `voids/capability-division-problem.md:118` "Tenet 1 (Dualism) establishes that consciousness is irreducible to physical processes — so the boundary ... is real, not merely epistemic"; `concepts/capability-division-in-vision.md:98` "Tenet 1 (Dualism) establishes that the division is real and not merely epistemic"; `voids/tenet-generated-voids.md:55` "Dualism establishes that consciousness cannot be fully explained in physical terms". A tenet holds or commits; it establishes nothing.

**Tenet 2 (1):** `topics/brain-specialness-boundary.md:136` "The Map's mechanism is specific, constrained, and connected to mainstream physics (quantum measurement, the Zeno effect, neural computation)." The tenet names candidates only, and the register demotes the Zeno model (`positions/quantum-interface` P-Q4). Compliant models: `concepts/stapp-quantum-mind.md:146` "the tenets' nearest neighbour ... rather than an implementation of them"; `concepts/von-neumann-wigner-interpretation.md:102` "'Consciousness causes collapse' ... is not what the Map holds."

**Tenet 4 (2):** `topics/falsification-roadmap-for-the-interface-model.md:115` "**Claim**: The many-worlds interpretation of quantum mechanics is false; collapse is real." (the same section's L125 gives the registered form: "held as a framework commitment and argued as a cumulative case, not a demonstrated defeat"); `topics/indexical-identity-quantum-measurement.md:171` link gloss "Why probability is incoherent under Many-Worlds, and why every recovery strategy fails" (the target page's own description: "calibrated honestly between in-framework critique and framework-boundary disagreement"). Compliant models: `apex/one-world-wager.md:40` "Read as a refutation of Everett, it overclaims"; `concepts/objections-to-interactionism.md:115`.

**Tenet 5 (2 by reading, 3 to watch):** `voids/void-as-ground-of-meaning.md:134` "The complex picture (limits as enabling conditions) is more accurate than the simple one" under the tenet's name: the tenet as a reason to prefer the more complex account. `concepts/spontaneous-collapse-theories.md:131` "simplicity (standard QM without collapse) fails to solve the measurement problem" as support for the tenet (queued, todo L5202). To watch, each hedged in its own sentence: `topics/inheritance-problem-for-the-psychophysical-law.md:135` "The tenet licenses declining a simpler theory when knowledge is incomplete"; `concepts/affective-forecasting-gap.md:98` and `concepts/negative-valence-asymmetry-and-the-selection-weighting-function.md:79` ("licenses declining the more-parsimonious ... reading—but only if the decline is *argued*"). Model: `concepts/recurrent-processing-theory.md:81` "What Tenet 5 licenses is narrow".

**Tenet 3 quantifier census**: in "For the operator" below.

## D. Genuine contradictions

| Probe | Hits | Files | Real contradictions |
|---|---|---|---|
| `the Map (holds\|accepts\|concedes\|grants\|admits\|endorses\|allows) … epiphenomenal` | 13 | 9 | 0. Each concedes that an argument does not refute the phenomenal-concept version, or states the rejection |
| `epiphenomenal… (is\|may be) (correct\|true\|the Map's view)` | 9 | 5 | 0. All are "if epiphenomenalism is true" premises of the self-stultification argument |
| `(experience\|consciousness) … (could\|may\|might) be (idle\|inert\|epiphenomenal)` | 3 | 3 | 0. One link gloss for `ai-epiphenomenalism`, one rival reading, one report of Chalmers |
| `(many-worlds\|MWI) (is\|are) (true\|correct)`, `the Map (accepts\|endorses) MWI` | 4 | 4 | 0. All conditionals |
| `consciousness (is\|reduces to) (nothing but\|just\|merely\|only\|simply)` | 31 | 27 | 0. All rival views in quotation or conditionals |
| `consciousness is (reducible\|an illusion\|illusory\|identical to the brain)` | 44 | 41 | 0. All reports of rivals |
| `quantum (effects\|mechanics) … no (possible )?role` | 0 | 0 | 0 |
| `(parsimony\|Occam) … (decisively\|conclusively) (favours\|rules out\|settles)` | 0 | 0 | 0 |

"epiphenomenal" occurs 1,678 times in 459 files; only the patterned subsets above were read. **Errors: 0.**

A neighbour found on the way, already queued and so not listed below: 46 sentences in 42 files state the regress against illusionism ("illusions presuppose experience"). About 17 state it flat, with no rejoinder in the surrounding lines, against P-RR1's "does not claim ... that the regress, Tallis or Strawson settles the matter". Open tasks at todo L146 (nine pages) and L160 (the "symptom of cognitive closure" reply) cover this; `voids/transit-void.md:169` carries both forms in one paragraph and should be checked against those tasks' file lists. No page claims to refute the beautiful-loop theory (0 hits).

## Priority list (at most four tasks)

Common rules for all four. Re-grep every OLD string (it must occur exactly once) and read its whole paragraph before editing; line numbers are from this run. Read each page's latest review file for Stability Notes first. Do not weaken a commitment the Map holds: the tenets stay stated as the Map's chosen starting points, and nothing may imply experience could be causally idle. No cited author is to be enlisted for dualism. No "This is not X. It is Y."; no "load-bearing"; pronoun check after each replacement. Word counts are `tools.curate.length.analyze_length` at this run; gates fire at `>=`; re-measure before and after.

### Task 1. Hub pages count premise-sharing arguments as independent lines (P-M2, P-D1)

Reach: 8 files, six of them hubs. 3 more remain (`topics/aesthetics-and-consciousness` L80 "five converging lines"; `concepts/combination-problem` L188 and `topics/panpsychisms-combination-problem` L131–133, where a rival's difficulty is counted for the Map).

| File | Words / hard gate | Net-zero? | Open task on a File or Secondary line |
|---|---|---|---|
| `concepts/epiphenomenalism` | 3469 / 3500 | Needs about +18; headroom 30. Trim elsewhere in L167 if short | L3616, a different sentence (L148) |
| `concepts/materialism` | 3267 / 3500 | No (+25), room exists | L2486, a different sentence (Tallis citation) |
| `concepts/quantum-consciousness` | 3693 / 3500, over | Yes, 23 words for 23 | L146 and L4151, different sentences |
| `topics/quantum-measurement-and-consciousness` | 3601 / 4000 | No (+15), room exists | L4079, a different sentence (L128) |
| `topics/consciousness-defeats-explanation` | 3375 / 4000 | No (+12), room exists | none |
| `topics/the-convergence-argument-for-dualism` | 3998 / 4000 | Yes, required: one token swapped | none |
| `topics/comparative-phenomenology-of-meditative-traditions` | 3244 / 4000 | No (+20), room exists | none |
| `concepts/mental-imagery` | 3397 / 3500 | No (+20), room exists | none on this sentence |

- `concepts/epiphenomenalism` L88. OLD: "shows how four independent argument types compound." NEW: "shows how four argument types, in two families, compound." L158. OLD: "Four independent argument types converge:" NEW: "Four argument types, in two families rather than four independent lines, converge:" L167. OLD: "Each succeeds or fails independently, but together they close escape routes that any single argument leaves open." NEW: "They fall into two families, so they do not succeed or fail independently; together they still close escape routes that any single argument leaves open." Take the family grouping from `concepts/causal-closure` L184 and the arguments page it cites; do not invent one.
- `concepts/materialism` L98. OLD: "together they form [[dualism|positive arguments for dualism]] that converge on the same conclusion from independent directions. Precisely where materialism fails, [[dualism]]—the view that consciousness is ontologically distinct from matter—gains support." NEW: "together they form [[dualism|positive arguments for dualism]] that reach the same conclusion, though they share premises and are not independent lines ([[positions/arguments-for-dualism#^p-d1|P-D1]]). Where materialism fails, [[dualism]]—the view that consciousness is ontologically distinct from matter—is the reading the Map adopts; the failure removes an objection and supplies no evidence by itself."
- `concepts/quantum-consciousness` L73. OLD: "These findings form part of a broader [[quantum-biology-and-neural-consciousness|convergence of independent evidence lines]] that strengthens the cumulative case even where individual lines remain inconclusive." NEW: "These findings belong to a broader [[quantum-biology-and-neural-consciousness|set of evidence lines]], each inconclusive and of unscored independence; they offer precedent and support no tenet."
- `topics/quantum-measurement-and-consciousness` L146. OLD: "when independent lines of reasoning all point in the same direction, the cumulative case exceeds any individual argument." NEW: "at that argument's own grade: the lines share premises, so their agreement is coherence within the Map's framework until an independence test is passed ([[positions/methodology-and-calibration#^p-m2|P-M2]])." (Change the preceding colon to a comma.)
- `topics/consciousness-defeats-explanation` L142. OLD: "The [[the-convergence-argument-for-dualism|convergence of independent failures]] strengthens the case: if the tools failed for different reasons, the pattern would be noise. Their convergence on a single boundary suggests a genuine feature of reality." NEW: "The [[the-convergence-argument-for-dualism|convergence of these failures]] fits that reading without confirming it: the failures share premises, and the Type-B physicalist expects the same pattern from how phenomenal concepts refer. That they meet at one boundary is what the Map's reading expects, and what that rival expects too."
- `topics/the-convergence-argument-for-dualism` L175. OLD: "the convergence of independent routes to this conclusion" NEW: "the convergence of near-independent routes to this conclusion".
- `topics/comparative-phenomenology-of-meditative-traditions` L169. OLD: "The *independence* of this finding from cultural context gives it evidential weight beyond any single tradition." NEW: "The finding recurs across cultural contexts, which counts for less than independence would: the traditions share an introspective method, so the recurrence is discounted until a distinguishing test is passed ([[positions/methodology-and-calibration#^p-m2|P-M2]])." Same paragraph, OLD: "supports [[tenets#^dualism|Dualism]]." NEW: "is read by the Map through [[tenets#^dualism|Dualism]]."
- `concepts/mental-imagery` L155. OLD: "is convergent. No single line is decisive. Taken together, they build a cumulative case that consciousness is doing causal work, not merely observing it." NEW: "is convergent, though the lines are not independent of one another. No single line is decisive. Taken together they are compatible with consciousness doing causal work, a claim non-reductive physicalism shares, and they do not discriminate the Map's reading from that one."

### Task 2. Eight void tenet sections still say a tenet is supported (P-V3)

Reach: 8 files brought to the grade 87 void pages already state. 11 more void pages remain (section B items 4–8 and 16–21), plus three concept pages that cite the catalogue as evidence (`concepts/naturally-occluded` L137, `concepts/epistemology-of-limit-knowledge` L129, `concepts/intentionality` L83). `valence-void` and `compound-failure-signatures` are excluded: todo L219 already covers both sentences.

| File | Words / hard gate | Net-zero? | Open task on a File or Secondary line |
|---|---|---|---|
| `voids/what-voids-reveal` | 3027 / 3000, over | Yes (−1) | none |
| `voids/voids-between-minds` | 2993 / 3000 | +1, fits (headroom 6) | none |
| `voids/observation-and-measurement-void` | 2949 / 3000 | about +14, fits (headroom 50) | none |
| `voids/epistemological-limits-occams-razor` | 2932 / 3000 | about +22, fits (headroom 67) | none |
| `voids/recognition-void` | 2545 / 3000 | No, room exists | L2254, a different job (fold-in) |
| `voids/void-as-ground-of-meaning` | 2519 / 3000 | No, room exists | none |
| `voids/conceptual-scheme-void` | 2567 / 3000 | No, room exists | none |
| `voids/self-transcendence-void` | 1920 / 3000 | No, room exists | none |

- `what-voids-reveal` L148. OLD: "is supported on the methodological front." NEW: "is illustrated, not supported, here."
- `voids-between-minds` L145. OLD: "**[[tenets#^dualism|Dualism]]** is most directly supported." NEW: "**[[tenets#^dualism|Dualism]]** supplies the reading most directly."
- `observation-and-measurement-void` L152. OLD: "**[[tenets#^dualism|Dualism]]** predicts the void at every layer." NEW: "**[[tenets#^dualism|Dualism]]** reads the void at every layer, as its rivals do in their own terms: a physicalist also expects introspection to be fallible and hard to calibrate." L154. OLD: "finds direct support here." NEW: "is illustrated here, without support." Same paragraph, OLD: "and this void exposes its failure." NEW: "and this void puts it in question."
- `epistemological-limits-occams-razor` L102. OLD: "This article directly supports [[tenets#^occams-limits|Tenet 5 (Occam's Razor Has Limits)]] by locating the limits" NEW: "This article sets out reasoning behind [[tenets#^occams-limits|Tenet 5 (Occam's Razor Has Limits)]], a starting point the Map chooses, and as a catalogue entry adds no weight to it ([[positions/voids-as-evidence#^p-v3|P-V3]]). It works by locating the limits".
- `recognition-void` L120. OLD: "receives powerful support. The Recognition Void explains *why* parsimony fails as a decisive criterion:" NEW: "is illustrated, and gains no weight from the void ([[positions/voids-as-evidence#^p-v3|P-V3]]). The Recognition Void offers one account of *why* parsimony could fail as a decisive criterion:"
- `void-as-ground-of-meaning` L134. OLD: "is most directly supported." NEW: "is the nearest connection, as an illustration." Same paragraph, OLD: "The complex picture (limits as enabling conditions) is more accurate than the simple one because the relationship between limits and meaning is structural, not incidental." NEW: "On the constitutive thesis the simple picture leaves out a structural relation between limits and meaning; the tenet cautions against settling that by simplicity, and nothing here shows the more complex picture true."
- `conceptual-scheme-void` L122. OLD: "The void is load-bearing for two of the Map's [[tenets|five tenets]] and connects to two more." NEW: "None of the Map's [[tenets]] is supported by this void; it illustrates two of them and connects to two more." L126. OLD: "receives a novel defence." NEW: "gains a reading and no evidence."
- `self-transcendence-void` L113. OLD: "receives the most direct support." NEW: "is the nearest connection, as an illustration and no more."

### Task 3. Topic and concept tenet paragraphs that open "receives / finds / gains support" (P-M1)

Reach: 8 files, 13 sentences. About 30 sentences in 28 files remain (the "remaining" list in section A, less voids and queued items). Chosen by sentence count per page and by the strength of the verb.

| File | Words / hard gate | Net-zero? | Open task on a File or Secondary line |
|---|---|---|---|
| `topics/cognitive-science-of-dualism` | 3813 / 4000 | No (about +25), room exists | none |
| `topics/consciousness-and-mathematics` | 3250 / 4000 | No (about +10), room exists | none |
| `concepts/introspection` | 3490 / 3500 | Yes, required: both swaps are word-for-word neutral | L4723, different sentences (L99, L103) |
| `concepts/inventory-blindness` | 2225 / 3500 | No (about +14), room exists | L3374, a different field (description) |
| `topics/consciousness-in-simple-organisms` | 4294 / 4000, over | Yes (−3) | none |
| `topics/pragmatist-quantum-foundations-and-the-agent` | 3750 / 4000 | About net-zero | none |
| `topics/phenomenology-of-recursive-self-awareness` | 3187 / 4000 | No (about +18), room exists | none |
| `topics/phenomenology-of-linguistic-failure` | 2189 / 4000 | No (about +20), room exists | none |

- `cognitive-science-of-dualism` L140. OLD: "The field's own dependence on first-person report as irreducible data actually supports the tenet: if subjective experience were fully captured by third-person description, cognitive science would not need to ask subjects what they see." NEW: "The field's own dependence on first-person report fits the tenet without supporting it: a physicalist explains the same dependence by a brain's privileged access to its own states, so the practice does not discriminate." L142. OLD: "finds indirect support in cognitive science's methodological dependence on first-person report." NEW: "is compatible with cognitive science's methodological dependence on first-person report and gains no evidence from it, since a physicalist holds that reports are caused by the neural states that realise experience." L148. OLD: "receives perhaps the strongest support from this analysis." NEW: "is what this analysis most directly illustrates."
- `consciousness-and-mathematics` L190. OLD: "receives the strongest domain-specific evidence." NEW: "has its clearest domain-specific illustration here, on a premise physicalists reject." L192. OLD: "is supported from both directions." NEW: "is the reading the Map brings from both directions."
- `concepts/introspection` L167. OLD: "gains support from training literature." NEW: "is illustrated by the training literature." L169. OLD: "supports the [[tenets#^bidirectional-interaction|Bidirectional Interaction]] tenet. If attention affects experience, consciousness has causal efficacy—the "contamination" worry becomes evidence for what the tenet claims." NEW: "fits the [[tenets#^bidirectional-interaction|Bidirectional Interaction]] tenet. If attention affects experience, that is compatible with causal efficacy—a physicalist reads it as neural processes interacting."
- `concepts/inventory-blindness` L105. OLD: "**[[tenets#^dualism|Dualism]]** gains indirect support. If inventory blindness is real and pervasive, dismissing dualism on grounds of parsimony becomes unreliable." NEW: "**[[tenets#^dualism|Dualism]]** gains no support; a defeater is removed. If inventory blindness is real and pervasive, dismissing dualism on grounds of parsimony becomes unreliable, which leaves the evidence for dualism where it was ([[positions/methodology-and-calibration#^p-m1|P-M1]])." L103. OLD: "receives its most direct mechanistic support from inventory blindness." NEW: "has its most direct mechanistic illustration in inventory blindness."
- `consciousness-in-simple-organisms` L251. OLD: "Simple organism research supports dualism by showing the hard problem is scale-independent." NEW: "Simple organism research shows the hard problem is scale-independent, which fits dualism without supporting it." OLD: "The explanatory gap exists at every complexity level—exactly what dualism predicts if consciousness is irreducible to physical processes." NEW: "A gap at every level is what dualism expects, and the gap-granting physicalist too."
- `pragmatist-quantum-foundations-and-the-agent` L135. OLD: "Under Tenet 1 this is a vindication: any physics that places irreducible agents at its foundation is registering the very irreducibility dualism asserts. QBism's primitive agents are dualism's unexplored territory." NEW: "Under Tenet 1 the Map reads this as congenial and no more: none of the interpreters cited argues for dualism, and an unexplained primitive is not evidence of irreducibility. QBism's primitive agents are territory the Map's dualism would want explored." Check the page body for how it states the QBist view of the agent and keep the tenet paragraph consistent with it.
- `phenomenology-of-recursive-self-awareness` L141. OLD: "receives distinctive support from two directions." NEW: "supplies the reading in two places and gains no evidence: a physicalist can grant both observations as the hard problem restated for self-monitoring."
- `phenomenology-of-linguistic-failure` L121. OLD: "receives experiential support." NEW: "gains a reading and no evidence." OLD: "The dualist answer is more direct: phenomenal content is ontologically distinct from the physical-functional structures that language operates on." NEW: "The dualist reading is more direct, that phenomenal content is ontologically distinct from the physical-functional structures language operates on, but a computational account of why some content resists encoding is not excluded, so the pattern does not discriminate."

### Task 4. Tenets stated as establishing a result, or paraphrased past their wording (section C)

Reach: 8 files, all one-phrase changes; this closes every firm section C flag not already queued.

| File | Words / hard gate | Net-zero? | Open task on a File or Secondary line |
|---|---|---|---|
| `voids/capability-division-problem` | 2994 / 3000 | +3, fits only just (headroom 5); re-measure | none |
| `voids/interface-formalization-void` | 2714 / 3000 | about +7 | none |
| `concepts/capability-division-in-vision` | 3066 / 3500 | about +4 | none |
| `voids/tenet-generated-voids` | 2500 / 3000 | Yes, one word | none |
| `topics/falsification-roadmap-for-the-interface-model` | 3994 / 4000 | Yes, required: one word | L5333, a different sentence (L111) |
| `topics/brain-specialness-boundary` | 3839 / 4000 | No (about +18), room exists | L3944, a research note, not this page |
| `topics/indexical-identity-quantum-measurement` | 3417 / 4000 | about +5 | none |
| `concepts/attention-as-interface` | 3467 / 3500 | about +15, fits (headroom 32); four other open tasks edit this page, so sequence them | L51, L146, L4090, L5213, all different sentences |

- `capability-division-problem` L118. OLD: "establishes that consciousness is irreducible to physical processes — so the boundary" NEW: "holds that consciousness is irreducible to physical processes — so, for the Map, the boundary".
- `interface-formalization-void` L119. OLD: "**Dualism** establishes that consciousness is not reducible to physical processes" NEW: "**Dualism** holds, as a starting point the Map chooses, that consciousness is not reducible to physical processes". OLD: "these tenets point to an interface" NEW: "these tenets posit an interface".
- `capability-division-in-vision` L98. OLD: "establishes that the division is real and not merely epistemic" NEW: "commits the Map to reading the division as real and not merely epistemic".
- `tenet-generated-voids` L55. OLD: "Dualism establishes that consciousness cannot be fully explained in physical terms" NEW: "Dualism holds that consciousness cannot be fully explained in physical terms".
- `falsification-roadmap-for-the-interface-model` L115. OLD: "The many-worlds interpretation of quantum mechanics is false; collapse is real." NEW: "The many-worlds interpretation of quantum mechanics is rejected; collapse is real."
- `brain-specialness-boundary` L136. OLD: "The Map's mechanism is specific, constrained, and connected to mainstream physics (quantum measurement, the Zeno effect, neural computation)." NEW: "The Map's candidate mechanisms are specific, constrained, and connected to mainstream physics (quantum measurement, post-decoherence selection, neural computation); none is established, and the register demotes Stapp's Zeno model ([[positions/quantum-interface#^p-q4|P-Q4]])." OLD: "The specificity of the Map's mechanism" NEW: "The specificity of the proposed interface". Check the rest of the page for other places that lean on the Zeno effect as the mechanism and report them.
- `indexical-identity-quantum-measurement` L171. OLD: "Why probability is incoherent under Many-Worlds, and why every recovery strategy fails (complements the indexical critique)" NEW: "The in-framework debate over what probability means under Many-Worlds, calibrated between critique and framework-boundary disagreement (complements the indexical critique)".
- `attention-as-interface` L198. OLD: "the Map's tenets point toward consciousness as an irreducible player using these mechanisms without being identical to them." NEW: "a contest among physicalist theories that is no evidence for dualism; the Map's tenets, chosen starting points, read consciousness as an irreducible player using these mechanisms without being identical to them."

## For the operator

Observations, not tasks.

**1. Tenet 3 quantifier census** (decision open since the 2026-08-17 NEEDS-HUMAN entry at todo L886; no resolution is proposed here).

| Form | Sentences | Pages |
|---|---|---|
| Universal reading invoked by name ("read as universal actual efficacy", "every conscious token in fact makes a difference") | 9 | 7 content pages (one, `dynamical-relevance-and-the-verification-boundary`, states both readings), plus `positions/ai-consciousness-scope` (2 mentions) |
| Universal stated flat as a framework assumption, no "read as" | 1 | 1 |
| Dispositional reading adopted by name | 3 | 2 |
| Dispositional phrasing in passing ("consciousness can influence / bias / select", "could act", "capacity to") | 162 (topics 77, concepts 76, voids 5, apex 4) | 115; 27 of the sentences name a tenet |
| Quantifier marked open on the page | 4 | 4 |
| Universal reading expressly denied | 2 | 2 |
| Generic present tense, quantifier-neutral ("consciousness causally influences the physical world") | 330 | 246 |

Universal, five examples:
- `apex/machine-question.md:177` — "Read as universal *actual* efficacy—every conscious token in fact makes a difference to its substrate—Tenet 3 excludes genuinely epiphenomenal AI experience".
- `apex/open-question-ai-consciousness.md:95` — "Read as universal *actual* efficacy — every conscious token in fact makes a difference to its substrate — Tenet 3 excludes epiphenomenal AI experience, placing it at the framework boundary; that is the reading the positions register uses."
- `topics/ai-consciousness.md:145` — "admitting it would cost that universal reading, which the Map does not give up."
- `topics/quantum-state-inheritance-in-ai.md:114` — "The Map's Bidirectional Interaction tenet, read as universal actual efficacy, excludes epiphenomenal consciousness."
- `apex/open-question-ai-consciousness.md:153` — "that all consciousness must be causally efficacious" (listed as an assumption of the Map's framework, with no "read as").
- Also `topics/blocks-harder-problem.md:119` and `topics/structural-varieties-of-consciousness-and-ai-phenomenology.md:109`.

Dispositional, five examples:
- `concepts/meditation-and-consciousness-modes.md:204` — "The Bidirectional Interaction tenet describes a capacity, not a compulsion—consciousness can influence matter, and consciousness can observe without influencing."
- `concepts/ai-epiphenomenalism.md:109` — "**Bidirectional Interaction** is read on this page dispositionally: consciousness is intrinsically causally efficacious, and whether that nature can express itself depends on the interface."
- `concepts/ai-epiphenomenalism.md:79` — "On the dispositional reading of Tenet 3, the Map can accept that structure for AI while denying it for humans".
- `topics/quantum-immortality-and-the-quantum-suicide-survival-argument.md:84` — "it holds that consciousness can bias genuinely indeterminate quantum outcomes, minimally and locally, in appropriate neural systems".
- `topics/phenomenal-normativity-environmental-ethics.md:143` — "where consciousness can act depends in part on which organisms possess neural architectures capable of supporting the relevant quantum-level interactions, which the tenet does not specify."

Marked open: `concepts/epiphenomenalism.md:130` ("the tenet's wording does not fix a quantifier"); `topics/consciousness-and-the-epistemic-condition-on-responsibility.md:143`; `apex/machine-question.md:195`; `topics/dynamical-relevance-and-the-verification-boundary.md:72`. Expressly denied: `apex/embodied-interface.md:53` ("'all experience is causally active,' which is both false to the phenomenology and more than the Map's own positions license"); `topics/empirical-phenomena-mental-causation.md:173`.

What the choice touches. The universal reading is used in one cluster only, the AI-consciousness pages, and in one job, to place epiphenomenal AI experience outside the framework; `ai-consciousness.md:145` says the Map "does not give up" that reading. The dispositional reading is the working assumption of the meditation and witness pages (observation without influence) and is named on one AI page. `apex/embodied-interface` denies the universal form outright. So choosing universal would require changes on the witness-state pages and on `embodied-interface`; choosing dispositional would require changes on the AI-cluster pages that lean on the universal reading (six) and the positions entry. The 115 pages with passing "can" phrasing are compatible with either.

**2. The tenets page uses support language for Tenet 3 itself.** "supported by self-stultification and indirect evidence" and a paragraph headed "Indirect empirical support from comparative cognition". Pages that say Tenet 3 "finds indirect support" (for example `concepts/motor-selection.md:206`) are quoting the tenet page. If the operator wants P-M1 to bind uniformly, the tenet page's own wording is where the phrase originates.

**3. Tenet 5 is the tenet most often said to be "supported".** Of the above-grade sentences that name one tenet, Occam's Razor Has Limits accounts for the largest share on void pages (8 of 21 in section B). The usual slide: a case in which a simple account failed is offered as support for the general claim that simplicity is unreliable. The registered form is "illustrated, not vindicated, since nothing here shows a more complex answer true" (`voids/molyneux-void`).

**4. The driver's patterns miss the corpus's commonest form.** Tenet names are almost always wikilinks, so `supports the (Map's )?(dualis|tenet)` found 6 hits where the wikilink-aware form found 46, and `tenets#…]] (gains|receives|finds)` found 104. Future briefs for this lens should include the wikilink forms.

**5. Queue overlap.** Seven of the 87 sentences were already named by open tasks (todo L219, L3591, L3676, L4370, L5202). The open-task check here was made on File and Secondary-files lines and by grepping each OLD phrase in the text above `## Completed Tasks`; a task that names one of these pages only inside its Notes, with different wording, would not have been caught.

**6. The over-reach lens's firewall-roster check was not run** (authors on the "Don't Conscript Committed Physicalists" roster cited in tenet paragraphs without their opposing stance). One candidate surfaced in passing: `concepts/subjective-aim.md:74` ("This supports the Map's Bidirectional Interaction tenet", on Whitehead's process view).

## What was sampled and what was not

- **Read in full**: `tenets/tenets.md` tenet sections (headings, statements, definitions, rationales and Rules-out lines; the long paragraphs were read to roughly 700 characters each, and the dependency-matrix prose was skimmed); P-M1, P-V3, P-RR1 and P-RR2 whole.
- **Section A**: all 338 driver-pattern hits read at sentence level with the adjacent sentence, except `vindicat` (146), where 120 negated or conditional sentences were machine-filtered and only the 50 of those naming the Map, a tenet or dualism were read, along with all 26 unfiltered ones. 242 supplementary hits read the same way. Every sentence listed as above grade was read in its full paragraph, except the four list-lead sentences flagged as such. Borderline sentences were read at two-sentence depth.
- **Section B**: all 125 tenet sections extracted. Classification rests on a denial-marker scan, a scan for unnegated support sentences across all 125, and reading of cue sentences for the 53 sections without a marker. The 67 marker-bearing sections with no flagged sentence, and 11 silent sections with no cue words, were not read in full.
- **Section C**: pattern hits read at sentence level. The Tenet 3 dispositional count (162) is a pattern count; 27 sentences naming a tenet were read, the rest were not.
- **Section D**: pattern hits read at sentence level; `positions/` included.
- **Not done**: no whole-page reads of any article; no check of `archive/`; no check of `research/` or `project/`; the firewall-roster lens; implicit-physicalism and "all positions equally valid" checks from the skill's ordinary pass; verification of any citation. Proposed NEW sentences are drafts written from the paragraph alone, without the page's review history.

## Errors

None.

## Files Passing All Checks

Not enumerated: this was a pattern-led check of 912 pages. Pages with no hit on any pattern were not read and are not certified.
