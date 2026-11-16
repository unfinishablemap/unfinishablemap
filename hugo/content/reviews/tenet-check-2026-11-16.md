---
ai_contribution: 100
ai_generated_date: 2026-11-16
ai_modified: 2026-11-16 20:12:06+00:00
ai_system: claude-fable-5-2
author: Andy Southgate
concepts: []
created: 2026-11-16
date: &id001 2026-11-16
description: 'Tenet check 167, a delta check of 69 changed pages: no Errors. 12 Warnings,
  all over-claims in a tenet''s name, led by comparative data still read as discriminating
  and a void offered as support for dualism.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-11-16 20:12:06+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-11-16
topics: []
---

# Tenet Alignment Check

**Date**: 2026-11-16. This is check 167. The previous check is [reviews/tenet-check-2026-11-15.md](/reviews/tenet-check-2026-11-15/) (check 166). Points it or earlier checks raised are not counted again here unless the window rewrote the line or a sibling page changed underneath it.

**Files checked**: 69 in the window, plus pattern samples over the whole corpus.
- **Window.** The 69 files in `concepts/` (21), `topics/` (25), `voids/` (21) and `apex/` (2) that differ between check 166's scan HEAD, `072018bdea`, and HEAD, `26374f3370` (122 commits). No `positions/` file and no `tenets/` file changed. The `git log --since="2026-11-15 12:00"` list the driver asked for has 70 entries; the extra one, `voids/inference-void`, changed before check 166's HEAD and was covered there. One page is new: `voids/bereavement-void`.
- **How the pages were read.**
  - `tenets/tenets` was read in full first, then check 166's report, then `positions/voids-as-evidence` ([P-V1](/positions/voids-as-evidence/#p-v1) to [P-V3](/positions/voids-as-evidence/#p-v3) and the candidate ledger).
  - The whole "Relation to Site Perspective" section of all 69 pages was read (about 26,000 words).
  - The window's changed body lines (about 38,000 words, an upper bound because a one-word edit counts its paragraph) were not all read line by line. A tell-word scan over every changed sentence returned 158 sentences, and all 158 were read. `voids/bereavement-void` was read end to end. The driver's four known open items were read in the live files with their surrounding sections.
  - **Corpus sample.** Three patterns were searched across all 940 files in `topics/`, `concepts/`, `voids/`, `apex/` and `positions/`: a mechanism called untestable or undetectable in principle, zombie possibility denied, and a void's Dualism paragraph claiming support. The third returned the family in W12.
- **Recheck.** Every quoted string in a Warning, and every Priority List anchor, was confirmed by script to occur exactly once in the live file on the line given. Queue ownership was checked against [workflow/todo.md](/workflow/todo/) above `## Completed Tasks` (L5698). Earlier reviews were searched for each string.
- **Pricing.** Body counts come from `tools.curate.length.analyze_length`, measured after applying each replacement to a scratch copy. Headroom is hard − 1 − count; the gate fires at `>=`. Hard gates printed by `get_thresholds`: topics 4,000, concepts 3,500, voids 3,000, apex 5,000.

**Errors**: 0

**Warnings**: 12. Eleven sit on window pages; one (W12) is a family of eleven out-of-window void pages found by the corpus sample.

**Notes**: 17.

**Tasks minted**: 0. The skill only reports.

## Summary

**No page in the window contradicts a tenet.** None concedes epiphenomenalism, endorses many-worlds, treats consciousness as reducible, or lets parsimony settle the question against dualism. Every finding is on side (B): a page says more in a tenet's name than the tenets or the registers allow.

**Most of the window's repairs hold, and they are now the models the remaining defects contradict.** Today's work on `concepts/evolution-of-consciousness`, `topics/consciousness-evolution-and-biology`, `concepts/episodic-memory`, `concepts/semantic-memory` (No Many Worlds paragraph), `voids/acquaintance-void`, `voids/plurality-void`, `voids/transit-void` and `topics/precommitment-and-the-diachronic-agent` installed calibrated wording. Most of the twelve Warnings are a sentence that an adjacent sentence, or a sibling page repaired in the last two days, now contradicts.

**Where the Warnings sit.** Five families.
1. **Comparative and performance data graded above compatible (W1, W6).** `consciousness-as-amplifier` was repaired at L49 and L99 today and still argues from the same data in four body sentences. `consciousness-evolution-and-biology` still calls the epiphenomenalist's correlation "a cosmic coincidence", against the co-optimization reply its sibling now grants.
2. **Felt singularity offered against many-worlds (W2, W5, W8, and part of W10).** Four pages treat the phenomenology of settling, loss or solidifying as something branching cannot supply. Tenets L172 and five window pages say it is available branch-locally.
3. **A void offered as support for dualism (W3, W12, and part of W7).** `expertise-and-its-occlusion` says Dualism "gains indirect support". The corpus sample found eleven more void pages opening their Dualism paragraph the same way, none citing the [P-V3](/positions/voids-as-evidence/#p-v3) suspension; one of the eleven is already queued.
4. **Tenet 2 over-read (W4, W9).** Fewness of interventions read as the tenet's minimality, and retrieval "in superposition" for the length of a memory search.
5. **A speculative reading stated flat, and physical frameworks enlisted (W10, W11).** A lead that says "constitutively hidden" over a body that says "may be structural", and a Libet objection that "dissolves entirely" on one page and is "recast rather than dissolved" on its sibling.

**The new article passes.** `voids/bereavement-void` says no tenet is supported by it. That is consistent with its body and is not an over-concession (see Checked and Found Sound).

## Errors

None.

## Warnings

### W1. concepts/consciousness-as-amplifier L73, L117, L121, L125: the body still treats the comparative data as discriminating
- **Tenet**: 3 (tenets L97: the evidence "corroborates the tenet rather than establishing it"; the epiphenomenalist "has a structural counter").
- **Quotes** (each once, on the line given):
  - L73: "**Logical reasoning requires consciousness**"
  - L117: "If reasoning were really unconscious, the pattern should reverse."
  - L121: "needs independent explanation if consciousness is causally inert."
  - L125: "and "tasks that distinguish humans from great apes" would be coincidental."
- **Conflicting Map text**: the page's own repaired lines. L49 (today): "The comparative data are compatible with that reading without discriminating it from its rivals". L99 (today): "The comparative record fits it without ruling out epiphenomenalism: an accompaniment account predicts the same profile". L107: the DeWall paradigm "separates executive capacity from unconscious pattern-completion without separating phenomenal consciousness from executive capacity". L109: which capacities count as consciousness-dependent "is fixed largely by the human-ape gap those capacities are then invoked to explain".
- **Issue**: the Illusionist Challenge section (L113–L125) argues as if L107 and L109 had not been written. L117 uses DeWall against the illusionist, who accepts conscious access and so predicts the same load effect. L121 and L125 present the task-gap correspondence as a coincidence for the rival, two paragraphs after L109 says the correspondence is partly built in by how the tasks were classed.
- **Rung**: compatible. The four sentences claim discriminating.
- **Standing**: the driver's known open item, confirmed. None of the four is a window line. Open todo L2966 owns a different defect on L73 ("Detection, though, is not the bottleneck"); coordinate. Priority 1.

### W2. concepts/consciousness-as-amplifier L177, L179: settling said to be illusory under branching
- **Tenet**: 4 (tenets L172; posit 3 at L184).
- **Quotes** (each once): L177 "The amplification hypothesis supports determinacy"; L179 "The correlation between consciousness-dependent capacities and successful reasoning would be coincidental."
- **Conflicting Map text**: tenets L172, determinate first-person facts "are available branch-relatively". `apex/phenomenology-of-consciousness-doing-work` L173: selection phenomenology is "exactly what a branch-local agent would experience either way, so the phenomenology does not discriminate singular actualisation from branching". `topics/phenomenology-of-agency-vs-passivity` L171: "branching reproduces the contrast rather than contradicting it."
- **Issue**: L179's first sentence says the felt resolution "becomes illusory" if all alternatives are actualised. A branch-local reasoner reaches a determinate conclusion and feels it settle. L179's second sentence then makes the capacity-reasoning correlation "coincidental" under branching, which does not follow: decoherence gives each branch the same correlation. The paragraph also runs the support the wrong way: amplification presupposes determinacy and cannot support it.
- **Standing**: L179 is a window line (today's refine-draft touched it and kept both sentences). L177 was raised by check 2026-10-29 and never minted. Priority 1.

### W3. voids/expertise-and-its-occlusion L123: a void offered as support for dualism, on a misdescription of identity theory
- **Tenet and register**: 1; [P-V3](/positions/voids-as-evidence/#p-v3) (`positions/voids-as-evidence`: "no cumulative weight is claimed, at any band"); [P-V2](/positions/voids-as-evidence/#p-v2).
- **Quotes** (each once): "gains indirect support from the systematic decoupling"; "which sits more naturally with dualism than with identity theory".
- **Issue**: the paragraph says that on identity theories "improved computation should entail richer conscious access, not less". No identity theory identifies consciousness with skilled computation as such. Global-workspace and higher-order accounts predict that practised routines leave the capacity-limited system. The decoupling is therefore predicted by the rival, and "dissociable" in the paragraph's last clause is common ground. The page has no [P-V3](/positions/voids-as-evidence/#p-v3) or common-cause qualifier (count 0 for `voids-as-evidence` and for "common-cause").
- **Conflicting Map text**: sibling voids repaired today. `acquaintance-void` L153: "As a catalogue entry the void adds no independent weight: the voids register has suspended the cumulative step." `transit-void` L192: "The opacity itself does not discriminate: the physicalist models cited above predict it too."
- **Rung**: compatible. It claims suggestive.
- **Standing**: unchanged line on a page with 29 changed lines in the window. Today's [reviews/pessimistic-2026-11-16-expertise-and-its-occlusion.md](/reviews/pessimistic-2026-11-16-expertise-and-its-occlusion/) raised it as an off-list counterargument (L163–L165), so it was not minted. Priority 2.

### W4. voids/expertise-and-its-occlusion L127: fewness of interventions read as Tenet 2's minimality
- **Tenet**: 2 (tenets L69: minimality is "*empirical-constraint* minimality", not a count).
- **Quote** (once): "consciousness already economising its involvement"
- **Conflicting Map text**: `topics/precommitment-and-the-diachronic-agent` L117 (window page): "That is fewness of interventions, not the empirical-constraint minimality the tenet names, and a physical controller enjoys the same economy." This is check 166 W12's defect on a second page.
- **Standing**: unchanged line. Today's pessimistic review noted it under the Quantum Skeptic and let "suggestive parallel" stand. Priority 2.

### W5. voids/expertise-and-its-occlusion L129: felt loss offered against many-worlds, and branching misdescribed
- **Tenet**: 4 (tenets L172, L121).
- **Quote** (once): "is experienced as genuine loss, not as branching"
- **Issue**: two defects. The paragraph says that on Many Worlds "the novice perspective is never truly lost—it persists in other branches". The expert in every branch has the same history of learning, so no branch keeps the novice standpoint for this expert. And felt loss is predicted identically on both ontologies, so the phenomenology cannot "resist this framing". What closes the earlier standpoint for *this* expert is Posit One's determinate subject.
- **Stability note read**: the 2026-07-07 deep review listed "MWI indexical" as a framework-boundary disagreement not to be re-flagged. This finding does not re-raise the Map's rejection of many-worlds. It concerns the paragraph's evidence claim, and the new evidence is the wording five window pages now carry (see W2).
- **Standing**: unchanged line. Priority 2.

### W6. topics/consciousness-evolution-and-biology L79: the epiphenomenalist's correlation called "a cosmic coincidence"
- **Tenet**: 3 (tenets L97, L101).
- **Quote** (once): "its systematic correlation with adaptive behaviour becomes a cosmic coincidence."
- **Conflicting Map text**: `concepts/evolution-of-consciousness` L181 (today): "an epiphenomenalist co-optimizer explains valence-fitness tracking too". `topics/evolutionary-case-for-mental-causation` L153: the co-optimization reply is such a proposal and "the dissociation evidence constrains it without yet discriminating against it". `voids/emotional-epistemology-void` L94: "the Map prices that account's debt but does not claim to have refuted it".
- **Issue**: on the co-optimization reply the correlation has a common cause in the selected neural basis. The next sentence ("argues this cost is too high") also reports the sibling page more strongly than the sibling now reads.
- **Standing**: window line. Check 166 W9's family ("systematic coincidence"). Priority 3.

### W7. topics/consciousness-evolution-and-biology L93, L141, L61: strong emergence "suggests it does"; Dualism "gains support" from a gap the page says sharpens the problem for neither side
- **Tenet**: 1.
- **Quotes** (each once): L93 "of consciousness suggests it does."; L141 "gains support from the observation that biological function-talk cannot capture consciousness"; L61 "The Map reads the gap as support for dualism, within limits".
- **Issue**:
  - L93. The question is whether an organism's unity has anything to do with the unity of consciousness. Strong emergence is the Map's reading, so it cannot serve as the evidence. The next sentence is already conditional ("If consciousness emerges at the level of the organism"). This is the driver's known open item, confirmed; today's completed task "overstates the organism claim" left this sentence.
  - L141 and L61. The same lead says "Evolution sharpens this problem for neither side" and that biology's function accounts are limited in scope, "none was offered as a theory of consciousness". A framework not offered as a theory of consciousness cannot reinforce a claim by failing to explain consciousness, and a type-B physicalist expects the same silence.
- **Rung**: compatible. It claims support.
- **Standing**: all three are window lines. Priority 3.

### W8. topics/consciousness-and-memory L188: a memory's felt solidifying said to presuppose one timeline, against the sibling's repaired paragraph
- **Tenet**: 4.
- **Quote** (once): "presupposes a single experiential timeline"
- **Conflicting Map text**: `concepts/episodic-memory` L178: "Nothing in episodic phenomenology discriminates a single-world physics from an Everettian one: each decohered branch contains a rememberer with a determinate history". `concepts/semantic-memory` L177: "compatible with the tenet; it does not argue for it."
- **Standing**: unchanged line on a window page. Raised by check 2026-09-18 and never minted; counted because both siblings now state the opposite. Priority 4. The page is 3,998/4,000 (headroom 1), so the fix must be net ≤ 1.

### W9. concepts/semantic-memory L173: retrieval held "in superposition", with the decoherence objection waved through
- **Tenet**: 2 (tenets L71, L77, L79).
- **Quotes** (each once): "suggest the objection isn't decisive"; "holding retrieval processes in superposition until the target activates"
- **Conflicting Map text**: tenets L77: "no measurement has observed the required neural coherent state". L79: magnetoreception "establishes a biological *precedent* rather than a licence for neural coherence". L71: post-decoherence selection "sidesteps the requirement that quantum coherence survive at neural timescales and is the strongest path the Map currently endorses".
- **Issue**: a tip-of-the-tongue search lasts seconds. The sentence asks for coherence across that span, the most demanding reading available, and supports it with "revised timescales" (Hagan et al.'s disputed figures, which tenets L77 reports as one side of a dispute) and the precedent the tenet says is no licence.
- **Standing**: unchanged line on a window page. New. Priority 4. The page is 3,487/3,500 (headroom 12).

### W10. voids/creative-aesthetic-void L68, L168, L188: a lead stronger than its body, an undiscounted convergence, and creative selection said to need one world
- **Tenets and registers**: 4; [P-V1](/positions/voids-as-evidence/#p-v1) (common-cause null); [P-M2](/positions/methodology-and-calibration/#p-m2).
- **Quotes** (each once): L68 "Creative processing is constitutively hidden"; L168 "it points toward a feature of consciousness rather than cultural construction"; L188 "requires definite outcomes rather than universal branching".
- **Issue**:
  - L68 against L146 ("The process void may be structural"). The lead states as a constitutive fact what the body offers as a possibility. The page's own L138 reports that the lead-up to insight "can be measured from outside". The driver's known open item, confirmed.
  - L168 infers a feature of consciousness from cross-tradition agreement with no discount. `topics/cross-cultural-phenomenology-of-agency` L97 (window page): "all introspection shares one instrument, so cross-cultural agreement examines one observation many times rather than assembling independent witnesses."
  - L188: creative selection is available branch-locally; global exclusion is posit 3.
- **Standing**: L68 and L168 are window lines. Today's pessimistic review of this page listed L68 under "Not on the priority list". Next in line 1.

### W11. concepts/atemporal-causation L193, L189: the Libet objection "dissolves entirely"; non-physical character "built into" physical frameworks
- **Tenets**: 3; 1; the co-optation rule.
- **Quotes** (each once): L193 "dissolves entirely under atemporal selection"; L189 "Its non-physical character is built into these frameworks".
- **Conflicting Map text**: `concepts/philosophy-of-time` L223 (repaired 2026-11-15): "the Map holds that reading as a speculative extension, so the Libet problem is recast rather than dissolved." This page's own L67: "The Map adapts this framework for consciousness".
- **Issue**: L193 states a result that depends on a reading the sibling holds as speculative. L189 says consciousness's non-physical character is built into Kastner's and Aharonov's frameworks. Both are physical theories, and the placement of consciousness in them is the Map's adaptation, as L67 says.
- **Standing**: unchanged lines; the window changed nine other lines. New. The sibling locus `time-collapse-and-agency` L215 ("This dissolves the Libet problem") is owned by todo L5181. Next in line 2. The page is 3,481/3,500 (headroom 18).

### W12. Eleven void pages outside the window open their Dualism paragraph with a support claim and no [P-V3](/positions/voids-as-evidence/#p-v3) qualifier (corpus sample)
- **Register**: [P-V3](/positions/voids-as-evidence/#p-v3) (cumulative step suspended since 2026-09-15); [P-V2](/positions/voids-as-evidence/#p-v2).
- **Loci** (each line read; none of the pages contains the string `voids-as-evidence` except `binding-void`, which has one hit elsewhere):
  - `voids/valence-void` L115: "finds particularly strong support"
  - `voids/disappearance-voids` L162: "gains support from all three mechanisms"
  - `voids/noetic-feelings-void` L177: "receives support on two lines"
  - `voids/compound-failure-signatures` L143: "gains support from two directions"
  - `voids/meta-epistemology-of-limits` L162: "gains indirect support. Claims that materialism will eventually explain consciousness become epistemically suspect—faith rather than warranted expectation."
  - `voids/binding-void` L133, `voids/conceptual-impossibility` L137, `voids/formal-cognitive-limits` L132: "gains indirect support"
  - `voids/emergence-void` L106: "gains support, but only through a difference in kind"
  - `voids/apophatic-cartography` L156: "gains methodological support"
  - `voids/meaning-void` L128: "finds qualified support"
- **Issue**: two of these (`binding-void`, `formal-cognitive-limits`) are on the framework-independent list, the one subset [P-V3](/positions/voids-as-evidence/#p-v3) was written for, and [P-V3](/positions/voids-as-evidence/#p-v3) now withholds weight from that subset too. The model wording exists on five pages: `handedness-void` L100 ("gains a reading and no evidence"), `stereopsis-void` L85, `molyneux-void` L95, `vitality-form-void` L100 ("gains no support") and today's `acquaintance-void` L153.
- **Limits of this finding**: only the opening sentence and the paragraph of each locus were read, not the page. Some paragraphs qualify themselves further down (`emergence-void`, `meaning-void`). This is a survey for a sweep task, not eleven adjudicated defects.
- **Ownership**: `voids/conceptual-impossibility` L137 is owned by todo L3015. The open queue has no task header naming any of the other ten pages for this defect (one relocated deep-review header names `meta-epistemology-of-limits`).

## Notes

1. **`voids/voids` framework-independent list against [P-V3](/positions/voids-as-evidence/#p-v3)'s count. Owned by todo L3377**, so not counted. The driver's item stands and the owning task's figures are stale. Counted today: the list beginning "**Voids any consciousness framework recognises**" (L107) has 23 bullets naming **26** voids. [P-V3](/positions/voids-as-evidence/#p-v3) says "15 entries, counted 2026-09-15"; `apex/taxonomy-of-voids` L8, L92, L179 and L231 say "roughly twenty"; the task quotes "about twenty-four (20 bullets)". Two further points for whoever runs that task. The list has grown from 15 to 26 in two months while the ledger's rejection column is still empty, which is the uncontrolled selection [P-V3](/positions/voids-as-evidence/#p-v3)'s suspension names. And `voids/bereavement-void` L88 and `voids/sour-grapes-void` L43 each declare themselves framework-independent and are not on the list.
2. **`voids/capability-division-problem` L118, L120 and `concepts/capability-division-in-vision` L98**: "Tenet 1 … establishes that consciousness is irreducible" and "establishes that the division is real and not merely epistemic". A tenet is a chosen starting point (tenets L47) and establishes nothing. The concept page corrects itself at L102 ("an accommodation, not a proof"); the void page does not, and its L120 says physicalism "treats consciousness as something to be explained away", which is true of eliminativism only.
3. **`concepts/phenomenal-contrast-method` L114, L120**: "provides some of the strongest empirical motivation for the Map's dualism"; "serves the Map as both evidence and tool". Liberal physicalists about cognitive phenomenology accept every contrast case, so the method bears on the liberal/conservative dispute and is silent between dualism and physicalism. New.
4. **`topics/consciousness-and-mathematics` L190, L192**: Bidirectional Interaction "receives the strongest domain-specific evidence"; Dualism "is supported from both directions". L192's own next clause grants that "the physicalist Platonist can coherently resist this". New.
5. **`concepts/cognitive-phenomenology` L214**: "The experience of mental effort reflects consciousness intervening in neural processing until understanding crystallizes." Flat, against `concepts/mental-effort` L94 ("fits its doing causal work without showing that it does") and tenets L95.
6. **`concepts/episodic-memory` L170, L180**: the page "argues for Bidirectional Interaction and the limits of parsimony"; "physicalism and dualism do not explain memorial phenomenology equally well, so the precondition for invoking parsimony—equal explanatory power—is unmet." The second sentence decides the dispute in order to suspend parsimony. The page is 3,498/3,500 (headroom 1).
7. **`topics/consciousness-and-memory` L184, L190**: Bidirectional interaction "is what the manipulation-maintenance asymmetry, the choking phenomenon … argue for"; the complexity of consolidation neuroscience "dissolves the apparent parsimony of 'consciousness is just brain activity.'" Complexity inside a physical account is no evidence against a physical account; `concepts/alexithymia` L75 (window page) says exactly that ("heterogeneity of mechanism is no evidence against a physical account").
8. **`topics/brain-computer-interfaces-and-the-interface-boundary` L147**: "This architecture is what bidirectional interaction predicts". The loop is a sensorimotor loop on any account; the page's own L143 says "BCIs illustrate the distinction rather than establish it". "fits" for "is what … predicts".
9. **`topics/emotion-and-dualism` L149**: "The moral urgency of reducing suffering requires that indexical facts matter". Add as a locus to todo L5662 (No Many Worlds said to preserve, support or ground value). `voids/numbing-void` L99 (window page) is the model: "neither the Map nor a many-worlds defender may cite felt magnitude as evidence".
10. **`topics/consciousness-and-the-normativity-of-reason` L133**: reports "accidentally correct at best" if consciousness were epiphenomenal. Tenets L101 grants that a tight correlation "can underwrite report-accuracy without phenomenal causation". Check 166 W8's family.
11. **`topics/self-stultification-as-master-argument` L165**: "the argumentative bedrock on which the case for dualism rests". Tenets L55 rests Tenet 1 on the explanatory gap and the cumulative positive arguments; self-stultification bears on Tenet 3, and tenets L103 says the strongest version of epiphenomenalism survives it. The page's own L169 is calibrated.
12. **`topics/time-collapse-and-agency` L207**: "This synthesis strengthens and deepens each of the five tenets". A synthesis built from the tenets cannot strengthen them. Fold into todo L5181, which owns L215 on this over-gate page (4,600/4,000); "connects to" for "strengthens and deepens" is −2.
13. **`apex/phenomenology-of-consciousness-doing-work` L175**: "why evolution would produce such elaborate phenomenology for a causally inert process"; "fits the evidence better". The co-optimization reply answers the first (W6), and the page's own L169 scopes the claim to epiphenomenalism "rather than against non-reductive physicalism".
14. **`topics/aesthetics-and-consciousness` L146** (window line): contemplative reports that beauty intensifies under investigation are "the opposite of what illusionism predicts". The [P-M2](/positions/methodology-and-calibration/#p-m2) discount is not applied. L160 ("presupposes a single actual world: the artist's sense that the unchosen version does not exist *anywhere*") is W2's family.
15. **`voids/transit-void` L196** (window line): "the epiphenomenalist reading of Libet was the simpler story, and Schurger reveals its simplicity as illusory." Schurger's accumulator is a fully physical account and removes one argument for epiphenomenalism without favouring mental causation. The page's L190 says so ("framework-internal coherence, not interface evidence"); L196 reads as if Schurger sided with the Map.
16. **`voids/acquaintance-void` L157**: "that it shapes behaviour suggests a genuine causal relation". The antecedent is the tenet, so the sentence infers the tenet from itself.
17. **`topics/metaproblem-of-consciousness-under-dualism` L153** (out of window, from the corpus sample): a Further Reading label says interactionism "makes zombies impossible rather than detectable". Today's repairs scope this: `consciousness-evolution-and-biology` L77, "The exclusion is nomological and leaves the metaphysical possibility of zombies untouched." "nomologically impossible" (+1).

## Carried, Not Counted

Raised by earlier checks, live at count 1 on unchanged lines of window pages, with no owner task:
- **`concepts/implicit-memory` L194**: "The simplest account that covers *all* the phenomena—neural and experiential—treats consciousness as a causal factor" and "is not more parsimonious than accepting that phenomenal attention does causal work". A parsimony credit to the Map, which Tenet 5's self-binding (tenets L147) forbids. **Seven earlier checks raised it** (2026-08-12 through 2026-10-02) and it has never been minted. L188 ("more than epiphenomenalism comfortably accommodates") sits beside it. The page is 3,485/3,500.
- **`topics/invertebrate-consciousness-as-interface-test` L135, L137** (check 2026-09-25): Birch's facilitation hypothesis "is precisely what the Bidirectional Interaction tenet predicts" and "tells against epiphenomenalism across phyla"; "'this bee' fragments across branches". Facilitation by conscious processing is predicted by any workspace account, and a branch-relative bee is determinately conscious or not.
- **`topics/trilemma-of-selection` L131** (check 2026-09-28): "The trilemma derives the need for consciousness to bias outcomes", against L129 of the same section (the move "is not *forced* by the trilemma").
- **`topics/aesthetics-and-consciousness` L156** (checks 2026-09-14, 2026-11-02): "Aesthetic creation provides the most direct evidence."
- **`topics/phenomenology-of-attention-to-absence` L104**: "Attention to absence supports this commitment in a specific way". Todo L3243 owns L106 and L96 on this page but not L104.

## Status of Check 166's Findings

- **Fixed**: W14 (`concepts/phenomenology-vs-function-axis` L130). Both strings are gone; the line now reads "comes under empirical pressure across the four exemplars" and "the taxonomy now carries it as a structural feature".
- **Queued, still live** (the driver minted all four Priority List items as P3):
  - Priority 1, `apex/identity-across-transformations` L173, L175, L189 (W7 and two carried items): todo L5651.
  - Priority 2, the four-file "No Many Worlds preserves moral urgency" set (W3, W4, `ethics-under-dualism` L206, `moral-architecture-of-consciousness` L190): todo L5662.
  - Priority 3, `concepts/content-specificity-of-mental-causation` L37, L73 (W9, W12): todo L5675.
  - Priority 4, `concepts/articulability-of-q1` L133 (W2): todo L5687.
- **Live and not queued** (each string confirmed at count 1 today): W1 `parfit-reductionism` L67; W5 `machine-consciousness` L225; W6 `philosophy-of-time` L171; W8 `consciousness-and-testimony` L145; W10 `dopamine-and-the-unified-interface` L176; W11 `consciousness-and-the-phenomenology-of-constraint-satisfaction` L94; W13 `time-collapse-and-agency` L135, L137; W15 `synesthetic-void` L113; W16 all three glosses. Notes 1, 3–7, 9, 11–16 and the carried `delegation-meets-quantum-selection` L114 and `control-theoretic-will` L138 are likewise live. Check 166's "Next in line" list remains the repair text for these.
- **Not re-raised**: nothing check 166 settled is reopened here.

## Checked and Found Sound

- **`voids/bereavement-void`** (new). L88 says "none of the Map's tenets is supported by it", and the body bears that out: attachment learning predicts the lag and hedonic adaptation the lapse, sensed presence is reported as the survivor's experience with "no inference … about whether anyone is there", and the authors cited are not enlisted. It is not an over-concession. L90 keeps the Map's commitment and labels it ("That is a commitment the Map brings to this material, and nothing in the material backs it"), L94 leaves mental causation to be answered "elsewhere and on other grounds", and nothing concedes epiphenomenalism or reducibility. It cites the [P-V3](/positions/voids-as-evidence/#p-v3) suspension. Its lead and its tenet section agree.
- **`concepts/evolution-of-consciousness`** (37 window lines). Zombie possibility is kept: L107 "leaves the metaphysical possibility of zombies untouched". Tenet 3 is "held as a posit" (L181) and global exclusion is "a posit the Map adopts" (L185). L177 and L195 grade magnetoreception "a precedent, not a licence".
- **`topics/consciousness-evolution-and-biology` L77, L145**. The zombie exclusion is "nomological". L145 states Born preservation correctly: invisible "to unconditioned aggregate tests", conditioned tests open, "hard to test, which is weaker than untestable".
- **`apex/what-consciousness-tells-us-about-physics`** (48 window lines; all 46 flagged sentences read). Born preservation is scoped to the unconditioned marginal throughout (L118, L174, L186, L198). L138 makes the collapse-interpretation advantage "conditional … not a neutral refutation of MWI". L202: "one premise package, the tenets, producing compatible readings rather than independent confirmations." L212 and L214 are calibrated.
- **`concepts/episodic-memory` L178 and `concepts/semantic-memory` L177**: No Many Worlds "records conditional consistency … rather than support". These are the models for W8.
- **`topics/precommitment-and-the-diachronic-agent` L115–L121**: each tenet paragraph says what the page does not supply. L117 is the model for W4.
- **Voids that cite the suspension or [P-V2](/positions/voids-as-evidence/#p-v2)**: `acquaintance-void` L153, `plurality-void` L105, `transit-void` L192, `numbing-void` L93, `preference-void` L105, `sour-grapes-void` L107, `source-attribution-void` L131, `beloved-void` L89–L95, `mirth-void` L105–L107, `death-void` L146, `inaccessible-past` L134–L136, `agency-void` L156.
- **Authors not enlisted**: `concepts/popper-three-worlds-interactionism` L90 ("his eminence adds no evidential weight"), `topics/sherrington-dualist-lineage` L91 ("does not claim him for the further step"), `topics/microphenomenological-interview-method` L151, `concepts/thought-insertion` L106 (Billon), `concepts/penfield-interactionist-dualism` L78, `topics/the-sublime-and-negative-aesthetics` L100, `voids/mattering-void` L114, `topics/cross-cultural-phenomenology-of-agency` L95.
- **Rivals given their strongest form**: `concepts/attended-intermediate-representations-theory` L89–L93, `concepts/relational-quantum-mechanics` L137–L153, `concepts/stapp-quantum-mind` L146–L164, `topics/paradoxical-kinesia` L86–L92, `topics/pupillometry-behavioural-channel` L99, `concepts/active-reboot` L93–L101, `topics/anaesthesia-and-the-consciousness-interface` L145–L151, `concepts/alexithymia` L67–L75, `topics/eighteenth-century-influx-debate` L93–L99, `topics/argument-from-reason` L143–L147.
- **Corpus sample, clean on two patterns**: no page in the five sections calls the Map's mechanism untestable or undetectable in principle (6 hits for the pattern, all about other theories or stated as a critic's worry). No page denies zombie possibility outright (4 hits; the only unscoped one is Note 17).

## Priority List

Four items, ranked. Each OLD string was confirmed by script at count 1 on the line given at 2026-11-16T20:08Z. Confirm it again before replacing. Standing guards for every item:
- never concede epiphenomenalism; each tenet stays a commitment, and No Many Worlds is neither refuted nor endorsed;
- no "This is not X. It is Y."; no "load-bearing";
- check pronouns in the sentence after each replacement;
- set `ai_modified` from `date -u`; append the running model to `ai_system` only if it is absent anywhere in the string.

1. **`concepts/consciousness-as-amplifier` L73, L117, L121, L125, L177, L179 (W1, W2). Tenets 3 and 4.**
   - **Length**: 3,307/3,500, headroom 192. Net +77 → 3,384.
   - (a) L73, +3. OLD: `**Logical reasoning requires consciousness**:` NEW: `**Logical reasoning draws on capacity-limited conscious processing**:`
   - (b) L117, +19. OLD: `If reasoning were really unconscious, the pattern should reverse.` NEW: `That tells against reasoning being unconscious in the access sense, which the illusionist need not claim: the load manipulation does not separate phenomenal consciousness from executive capacity (above).`
   - (c) L121, +19. OLD: `needs independent explanation if consciousness is causally inert.` NEW: `needs explaining if consciousness is causally inert, though it is a weaker fact than it looks: the tasks were classed as consciousness-requiring largely by that gap (above).`
   - (d) L125, +12. OLD: `and "tasks that distinguish humans from great apes" would be coincidental.` NEW: `and "tasks that distinguish humans from great apes" would need a common cause, and expanded executive capacity is the one the illusionist offers.`
   - (e) L177, +6 and +11. OLD: `The amplification hypothesis supports determinacy:` NEW: `The amplification hypothesis presupposes determinacy, which a branch also supplies locally:` OLD: `it must select—producing singular outcomes, not branching alternatives.` NEW: `it must select; that the outcome be singular globally, and not only within a branch, is the tenet's addition.`
   - (f) L179, +7. OLD: `If all alternatives are equally actualised across branches, the phenomenology of settling—the felt resolution when a conclusion is reached—becomes illusory. The correlation between consciousness-dependent capacities and successful reasoning would be coincidental.` NEW: `A branch-local reasoner has the same phenomenology of settling—the felt resolution when a conclusion is reached—so it does not decide against branching. What branching removes is the global exclusion of the unchosen conclusions, a [[tenets/background-commitments|posit the Map adopts]].`
   - **Guards**: keep L49 and L99 (today's refine-draft) and L105–L111 (the Deflationary Challenge), which are the models. After (b), the following sentence ("That conflict *detection* runs implicitly … does not rescue the illusionist") must still read; soften "does not rescue" if it now overstates. Todo L2966 owns "Detection, though, is not the bottleneck" on L73; do not touch that sentence. L183's Tenet 5 paragraph already ends "a registered advantage rather than a parsimony proof"; leave it.

2. **`voids/expertise-and-its-occlusion` L123, L127, L129 (W3, W4, W5). Tenets 1, 2, 4; [P-V3](/positions/voids-as-evidence/#p-v3).**
   - **Length**: 2,993/3,000, **headroom 6**. Net −56 for (a)–(c) → 2,937; with the rider, −43 → 2,950.
   - (a) L123, −21. OLD: `gains indirect support from the systematic decoupling of consciousness and cognitive performance. On identity theories, consciousness *is* the relevant computational process, so improved computation should entail richer conscious access, not less; the expertise void shows the opposite. A physicalist can reply that consciousness is identical to a *monitoring* process, separate from the skilled computation it monitors—but that concedes the core point that consciousness and cognitive processing are dissociable, which sits more naturally with dualism than with identity theory.` NEW: `gains a reading and no evidence. Physicalist workspace and monitoring accounts predict the decoupling: automatised processing leaves the capacity-limited system those accounts identify with consciousness. That consciousness dissociates from *some* cognitive processing is common ground and favours neither side. As a catalogue entry the void adds no independent weight: the voids register has [[positions/voids-as-evidence#^p-v3|suspended the cumulative step]].`
   - (b) L127, −14. OLD: `finds a suggestive parallel. The Map posits the smallest possible non-physical influence on quantum outcomes; the expertise void shows consciousness already economising its involvement in a domain we can observe—intervening intensely during learning, then all but withdrawing once the skill runs.` NEW: `gains nothing here. Withdrawal once a skill runs is fewness of interventions, not the empirical-constraint minimality the tenet names, and a physical controller economises the same way.`
   - (c) L129, −21. OLD: `On Many Worlds, every branch is equally real, so the novice perspective is never truly lost—it persists in other branches. The phenomenology of the expertise void resists this framing. The expert's inability to recover their former perception is experienced as genuine loss, not as branching. Indexical identity—being *this* expert, whose earlier way of seeing is closed rather than merely elsewhere—is what gives the void its force.` NEW: `A branch-relative expert has lost the novice standpoint just as irrecoverably, so the felt loss does not decide against Many Worlds. That *this* expert's earlier way of seeing is closed, and not merely elsewhere, rests on the [[tenets/background-commitments|determinate-subject posit]], which the void illustrates without supporting.`
   - **Rider**, L125, +13. OLD: `and the choking evidence shows the interface still exists: consciousness can re-enter, but at a cost.` NEW: `and the choking evidence fits, without showing, an interface that still exists: conscious monitoring can re-enter, but at a cost, as its neural correlate can on a physicalist reading.`
   - **Guards**: models are `handedness-void` L100, `acquaintance-void` L153 and `precommitment-and-the-diachronic-agent` L117. Keep L129's first sentence ("matters because the occlusion is directional …"); after (c) check that it still leads into the new text. Do not reopen the source corrections today's refine-draft made in the body.

3. **`topics/consciousness-evolution-and-biology` L79, L93, L141, L61 (W6, W7). Tenets 3 and 1.**
   - **Length**: 3,223/4,000, headroom 776. Net +6 → 3,229.
   - (a) L79, +13. OLD: `it cannot be selected at all—its systematic correlation with adaptive behaviour becomes a cosmic coincidence. The [[evolutionary-case-for-mental-causation|evolutionary case for mental causation]] argues this cost is too high.` NEW: `it cannot be selected at all, and its systematic correlation with adaptive behaviour needs another source, which the [[co-optimization-reply-to-the-correlation-problem|co-optimization reply]] locates in the selected neural basis. The [[evolutionary-case-for-mental-causation|evolutionary case for mental causation]] constrains that reply without yet discriminating against it.`
   - (b) L93, −1. OLD: `The [[the-strong-emergence-of-consciousness|strong emergence]] of consciousness suggests it does.` NEW: `On the Map's [[the-strong-emergence-of-consciousness|strong-emergence]] reading it may.`
   - (c) L141, −5. OLD: `gains support from the observation that biological function-talk cannot capture consciousness. If the most sophisticated framework biology has for explaining traits cannot account for why consciousness exists rather than mere information processing, this reinforces the claim that consciousness exceeds physical description.` NEW: `is coherent with the observation that biological function-talk leaves experience out, and gains no support from it: no function account was offered as a theory of consciousness (above), and a type-B physicalist expects the same silence.`
   - (d) L61, −1. OLD: `The Map reads the gap as support for dualism, within limits:` NEW: `The Map reads the gap through its dualism, within limits:`
   - **Guards**: (a)'s closing clause quotes `evolutionary-case-for-mental-causation` L153; re-read that line first. Keep L77, L145 and L147 as today's passes left them. After (c), the paragraph's last sentence ("Dualism's advantage is that it takes the difficulty at face value …") should be read against the new opening; "advantage" may need to become "stance". If the description field repeats "support for dualism", match it.

4. **Memory pair: `topics/consciousness-and-memory` L188 and `concepts/semantic-memory` L173 (W8, W9). Tenets 4 and 2.** TWO FILES; report each by name.
   - (a) `topics/consciousness-and-memory` L188. **Length**: 3,998/4,000, **headroom 1**. Net −1 → 3,997. OLD: `The felt experience of a memory solidifying into *this* version rather than another presupposes a single experiential timeline.` NEW: `A memory's felt solidifying into *this* version is available branch-locally too, so it supports nothing here ([[episodic-memory]]).`
   - (b) `concepts/semantic-memory` L173. **Length**: 3,487/3,500, **headroom 12**. Net +8 → 3,495. OLD: `The [[decoherence]] challenge applies here, but the revised timescales and biological precedents (avian magnetoreception) suggest the objection isn't decisive. The feeling of effortful search might reflect sustained [[attention-as-interface|attention]] holding retrieval processes in superposition until the target activates.` NEW: `The [[decoherence]] challenge applies in full to any reading that holds retrieval in superposition: no such neural coherence has been observed, and avian magnetoreception is a precedent, not a licence. The Map's preferred post-decoherence reading needs only a selection among outcomes when the search resolves.`
   - **Guards**: both pages are within a few words of their hard gates; re-measure after the edit and stop if the count reaches the gate. Models are `episodic-memory` L178 and tenets L71, L77, L79. Keep `semantic-memory` L177 (the repaired No Many Worlds paragraph) and L169's "speculative candidate occasion". On `consciousness-and-memory`, keep the sentence before the OLD string ("The Map's framework requires genuine collapse …").

**Next in line, if capacity allows:**
1. W10, `voids/creative-aesthetic-void` (2,439/3,000, headroom 560; net +14). L68: `Creative processing is constitutively hidden—` → `Creative processing is hidden, perhaps structurally—` (+1). L168: `The comparison is informal, but it points toward a feature of consciousness rather than cultural construction.` → `The comparison is informal, and every tradition reports through the same introspective instrument, so the agreement is one observation repeated, not independent witnesses.` (+7). L188: `Genuine creative selection—consciousness contributing what physics does not determine—requires definite outcomes rather than universal branching.` → `Creative selection of that kind is available branch-locally; that the unchosen solutions be globally nonactual is a [[tenets/background-commitments|posit the Map adopts]].` (+6).
2. W11, `concepts/atemporal-causation` (3,481/3,500, headroom 18; net +11). L193: `Atemporal causation receives its strongest support here. The Libet timing objection — the most pointed empirical challenge to bidirectional interaction — dissolves entirely under atemporal selection. Consciousness can genuinely cause physical outcomes even when awareness follows neural preparation in linear time.` → `Atemporal causation does its main work here. The Libet timing objection — the most pointed empirical challenge to bidirectional interaction — is recast, not dissolved: if the speculative atemporal reading holds, consciousness could cause physical outcomes even when awareness follows neural preparation in linear time.` (+4). L189: `Its non-physical character is built into these frameworks rather than awkwardly appended.` → `That placement is the Map's addition: Kastner's and Aharonov's frameworks are physical theories and assign consciousness no such role.` (+7). The second replacement states the authors' positions; verify against their texts or the page's L67 before it lands.
3. W12, a sweep task over the ten unowned void pages (`conceptual-impossibility` is todo L3015): read each Dualism paragraph, and where no discriminator is named replace the opening verb with "gains a reading and no evidence" or "is coherent with", adding the [P-V3](/positions/voids-as-evidence/#p-v3) clause from `acquaintance-void` L153. Price each page separately; several voids sit near 3,000.
4. The carried `concepts/implicit-memory` L194, raised seven times: `The simplest account that covers *all* the phenomena—neural and experiential—treats consciousness as a causal factor rather than an idle shadow of neural events.` → delete, or replace with a sentence stating that Tenet 5 bars the Map from claiming the parsimony point for itself. Net ≤ 0 (3,485/3,500).
5. Notes 9 and 12 as loci on todo L5662 and L5181. Note 1's fresh counts on todo L3377.

## What Was Not Reached

- **The window's changed body lines were not all read.** All 69 tenet sections were read in full and 158 flagged sentences were read, but a defect in a changed body sentence with none of the tell-words would have been missed. The pages with the most unread changed text are `voids/sour-grapes-void` (57 changed lines), `topics/cross-cultural-phenomenology-of-agency`, `concepts/active-reboot`, `voids/transit-void`, `voids/inaccessible-past` and `concepts/capability-division-in-vision`.
- **Leads were checked against bodies only on the known-item pages and the new article**, not on all 69.
- **The rest of the corpus was sampled by three patterns, not scanned.** About 870 pages outside the window were not opened. W12's eleven loci were read at paragraph level only.
- **No source was checked.** Where a repair states what an author holds (W3's workspace accounts, W11's Kastner and Aharonov), the wording follows the Map's own pages and general knowledge of the literature and was not verified at a publisher.
- **`positions/`** had no changed file; the register was read only at `voids-as-evidence`.
- **Check 166's unqueued Warnings were confirmed live by string count only**; their paragraphs were not re-read.

## Files Passing All Checks

Window pages whose tenet section and flagged window sentences raised nothing, or whose only residue is owned or carried.

- **apex/** (1 of 2): `what-consciousness-tells-us-about-physics`. (`phenomenology-of-consciousness-doing-work`: Note 13.)
- **concepts/** (13 of 21): `active-reboot`, `alexithymia`, `attended-intermediate-representations-theory`, `evolution-of-consciousness`, `penfield-interactionist-dualism`, `phenomenology-vs-function-axis` (check 166 W14 fixed), `philosophy-of-time` (L223, L225 owned by todo L5471; L171 is check 166 W6, still live), `popper-three-worlds-interactionism`, `prebiotic-collapse`, `reasons-responsiveness`, `relational-quantum-mechanics`, `stapp-quantum-mind`, `thought-insertion`.
- **topics/** (13 of 25): `anaesthesia-and-the-consciousness-interface`, `argument-from-reason`, `consciousness-and-the-problem-of-induction`, `cross-cultural-phenomenology-of-agency`, `eighteenth-century-influx-debate`, `empirical-phenomena-mental-causation`, `microphenomenological-interview-method`, `paradoxical-kinesia`, `phenomenology-of-agency-vs-passivity`, `precommitment-and-the-diachronic-agent`, `pupillometry-behavioural-channel`, `sherrington-dualist-lineage`, `the-sublime-and-negative-aesthetics`.
- **voids/** (15 of 21): `agency-void`, `anesthesia-void`, `beloved-void`, `bereavement-void` (new), `death-void`, `emotional-epistemology-void`, `inaccessible-past`, `infant-consciousness`, `mattering-void` (L120 carried from check 2026-11-02), `mirth-void`, `numbing-void`, `plurality-void`, `preference-void`, `source-attribution-void`, `sour-grapes-void`. (`voids`: Note 1, owned.)