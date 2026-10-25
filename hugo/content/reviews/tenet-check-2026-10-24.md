---
ai_contribution: 100
ai_generated_date: 2026-10-24
ai_modified: 2026-10-24 23:38:28+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-10-24
date: &id001 2026-10-24
description: 'Tenet check 155: no Errors in 59 changed pages. Twelve Warnings: an
  RSP asserting actual, universal efficacy, an LLM-cluster page moving P-AC1 to ruled
  out, a same-causes concession, Family 5 drift.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-10-24 23:38:28+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-10-24
topics: []
---

# Tenet Alignment Check

**Date**: 2026-10-24. This is check 155. The previous one, [reviews/tenet-check-2026-10-23.md](/reviews/tenet-check-2026-10-23/), was check 154.

**Files checked**: 59. Every `obsidian/` content file changed since 2026-10-23T23:00Z (`git log --name-only`; the brief counted 58), plus `tenets.md` (L47–L188) read in full.
- **Priority 1, read in full (13).** These are the brief's twelve pages: `topics/blocks-harder-problem` (new), `concepts/phenomenology-of-choice-and-volition`, `topics/memory-anomalies`, `concepts/presence-type-and-absence-type-voids`, `concepts/the-ownerless-suffering-argument`, `concepts/nondualistic-interactionism`, `voids/three-kinds-of-void`, `voids/witnessing-void`, `concepts/intentionality`, `concepts/symbol-grounding-problem`, `concepts/language-and-consciousness` and `voids/handedness-void`. The thirteenth is `topics/precommitment-and-the-diachronic-agent`. It is new today (00:23Z, 142 lines) and missing from the brief's list.
- **Priority 2, sampled (46).**
  - All 46 were read diff-scoped: every hunk changed against `f642e1df6e` (the commit before the window).
  - Eight voids had their full Relation to Site Perspective sections read: numbing, preference, assent, fusion, perceptual-reality-monitoring, palette-extension, cross-state and capability-division.
  - Further sections were read in context: `llm-consciousness` L120–L136, `ai-epiphenomenalism` L75–L82, `pairing-problem` L115–L125 and `phenomenological-evidence` L56/L162/L194.
  - Both positions files (`subject-census` and its calibration history) were read diff-scoped. The change corrects a count only.
- **Cross-check sweeps over all 59.** Five family scans ran over the full set: every No Many Worlds paragraph (34 hits); closure and sufficiency wording; parsimony wording; permanent and in-principle wording in the voids; and evidential verbs in descriptions. Every hit was re-read in context. Each zero used below was paired with a positive control.
- **Comparison texts read at the cited lines:**
  - the register: [P-Q2](/positions/quantum-interface/#p-q2) (L64–L73) and [P-Q3](/positions/quantum-interface/#p-q3) (L77–L79) in `positions/quantum-interface`, and [P-AC1](/positions/ai-consciousness-scope/#p-ac1) (L52–L64) in `positions/ai-consciousness-scope`;
  - `concepts/continual-learning-argument` L154–L176;
  - `phenomenal-concepts-strategy` L79;
  - the co-optation firewall roster ([project/writing-style.md](/project/writing-style/) L203–L213).
- **Settled or queued, and not re-raised.** The five open items named in the brief, plus the blocks-harder-problem cross-review (todo L3095). Status is in [Bearing on the open items](#bearing-on-the-open-items).
- **Quote checks.** Every OLD string in the Priority List was confirmed by script (`str.count` = 1 at the line given). Word deltas come from `tools.curate.length.count_words` on the frontmatter-stripped body after the replacement. Totals come from `analyze_length`. Headroom means hard − 1 − count. Description edits cost 0, since `analyze_length` is body-only.

**Errors**: 0

**Warnings**: 12, on 12 files. All are Over-reach or calibration drift. No page contradicts a tenet.

**Notes**: 11

## Summary

The new pages are clean.
- `blocks-harder-problem` grades the harder problem "fits ... without evidencing", holds [P-AC1](/positions/ai-consciousness-scope/#p-ac1) still "in neither direction", and leaves the Tenet 3 quantifier open (L119).
- `precommitment-and-the-diachronic-agent` passes on every family. Its No Many Worlds paragraph (L108) is the window's best Family 5 control: "branch-relative accounts deliver determinate continuity facts too".
- Today's repairs on `phenomenology-of-choice` (L94, L145, L167), `the-ownerless-suffering-argument` (L127), `access-consciousness` and `nondualistic-interactionism` each landed correctly.

The Warnings sit on older text in pages touched today, and they take two shapes.

**1. Relation to Site Perspective paragraphs the repairs never reached.** `concepts/language-and-consciousness` is the worst case.
- Tonight's 22:38 refine fixed its L49 and left a tenet section intact from February and March.
- L93 says "Every meaningful utterance is an instance of downward causation". That asserts actual efficacy and settles the quantifier the NEEDS-HUMAN entry (todo L661) holds open.
- It then says epiphenomenalism "must treat the apparent purposefulness of speech as coincidental". That is the coincidence framing that `tenets.md` L101 and check 154 W7 both retired.
- `symbol-grounding-problem` L105 moves [P-AC1](/positions/ai-consciousness-scope/#p-ac1) to "ruled out": "Since no theory attributes consciousness to lookup tables, none should attribute it to LLMs". The page it cites calls Hoel's inference "defeasible, not necessary" (`continual-learning-argument` L176).

**2. A rule installed on some pages and not on their siblings.**
- **Family 5.** Six window pages concede that an Everettian predicts the same first-person phenomenology on each branch:
  - `precommitment` L108;
  - `episodic-memory` L178;
  - `temporal-void` L152;
  - `diachronic-agency` L133;
  - `self-control` L108;
  - `process-philosophy` L160.

  Four do not: `phenomenology-of-choice` L165, `intentionality` L235, `temporal-consciousness` L202 and `problem-of-other-minds` L202.
- **Family 2.** Today's `blocks-harder-problem` L117 and `ai-epiphenomenalism` L77 both report Block's reply to the same-causes objection. `witnessing-void` L95 still runs the objection: if an AI does everything without witnessing, Tenet 3 "faces serious pressure".
- **[P-V2](/positions/voids-as-evidence/#p-v2).** The newer voids open their tenet sections with the [P-V2](/positions/voids-as-evidence/#p-v2) disclaimer: numbing L92, preference L105 and assent L107. `perceptual-reality-monitoring-void` and `capability-division-problem` have no such disclaimer. Their tenet sections still read "the kind of result the Map expects on dualism" and "evidence that dualism requires".

## Method: families, violations and on-page controls

| # | Family (brief) | Violations in window | Compliant instances found (controls) |
|---|---|---|---|
| 1 | Tenet 3: fits without evidencing; quantifier unresolved | 2: W1 (language L93 "Every meaningful utterance"), W11 (two voids) | blocks-harder-problem L38/L119/L131, emotion-regulation RSP, tonic-immobility RSP, precommitment L104, numbing L100, preference L112, assent L109, phenomenology-of-choice L94/L161 |
| 2 | Never concede epiphenomenalism | 2: W5 (witnessing L95), W1 (language L93 coincidence framing) | blocks-harder-problem L73/L117, ai-epiphenomenalism L77, precommitment L96, cross-state L93, tonic-immobility RSP, volitional-control L132 (outside window) |
| 3 | Closure as sufficiency needs chance-fixing | 1: W8 (pairing-problem L121) | access-consciousness RSP (installed 09:28), interactionist-dualism L119 ("physics specifies probabilities but not outcomes") |
| 4 | Tenet 2 is empirical-constraint minimality | 1: W6 (phenomenology-of-choice L163) | precommitment L106, blocks-harder-problem L129, preference L116 |
| 5 | Tenet 4 a commitment; Posit One posited | 2: W6 (phenomenology-of-choice L165), W7 (three siblings) | precommitment L108, episodic-memory L178, temporal-void L152, diachronic-agency L133, self-control L108, process-philosophy L160, ownerless-suffering L131, subject-census P-SC Depends-on |
| 6 | Tenet 5 binds only the Map's reasoning | 1: W9 (ai-epiphenomenalism L79) | blocks-harder-problem L135, ownerless-suffering L127, phenomenology-of-choice L167, access-consciousness RSP, nondualistic-interactionism L97, precommitment L110, psychophysical-laws L243 |
| 7 | Weak Revelation; no permanent-void claim | 1: W12 (witnessing-void description) | handedness-void L70 ("relative to which theory?"), meta-epistemology L90 (dissolved-limits paragraph, installed today), blocks-harder-problem L40 |
| 8 | Conceivability rests on contested modal rationalism | 0 | blocks-harder-problem L127, presence-type L125, psychophysical-laws (Type-B sentence, installed 01:12), access-consciousness RSP |
| 9 | [P-AC1](/positions/ai-consciousness-scope/#p-ac1) does not move | 3: W3 (symbol-grounding L105), W4 (intentionality L197), W10 (llm-consciousness L130) | blocks-harder-problem L38/L105, language-and-consciousness L49, symbol-grounding L125 and intentionality L141 (tonight), topics/ai-consciousness L165 |
| 10 | Process compatibility is not evidence; Madhyamaka is bedrock | 0 | nondualistic-interactionism L41/L99, process-philosophy L160, ownerless-suffering L99/L129, precommitment L108 |
| 11 | No enlistment; navigation no stronger than body | 1 in the Warnings (W2: PCS as failed, language L83) + description items inside W4, W12 | blocks-harder-problem L40/L91/L127, nondualistic-interactionism L85, emotion-regulation L99 (2005 reading credited to its authors) |

The keyword counts are lexical upper bounds. The violation column holds only what survived reading in context.

## Errors

None.

## Warnings

### W1. `concepts/language-and-consciousness` L93 (with L89 and L91): actual, universal efficacy, and the coincidence framing
- **Family**: 1 and 2. The ladder rung earned is **compatible**.
- **Quote (L93)**: "Every meaningful utterance is an instance of [downward causation](/concepts/mental-causation-and-downward-causation/)—conscious intention shaping physical sound waves and written marks. This directly contradicts [epiphenomenalism](/concepts/epiphenomenalism/), which must treat the apparent purposefulness of speech as coincidental—our words happen to match our experiences, but the experiences play no causal role in producing them."
- **Issue**: Three defects.
  - The paragraph's conditional ("If meaning requires conscious intention ... then") is discharged into a categorical about every utterance. `tenets.md` L95: genuine downward causation "is therefore a posit the interface argument leaves open, not a result it secures". "Every" also picks the universal reading the quantifier NEEDS-HUMAN (todo L661) leaves open.
  - Epiphenomenalism need not call the match coincidence. `tenets.md` L101 states its best reply: reports "can be reliable in virtue of the parallel rather than the cause". Check 154 W7 retired the same framing on `arguments/epiphenomenalism-argument` L136.
  - L89 ("provides independent support for several of the Map's [tenets](/tenets/)") and L91 ("gains support ... exactly what we would expect") grade as support data that the page's own L73 says physicalists explain: phenomenal concepts "explain the *appearance* of an explanatory gap without requiring anything non-physical".
- **Age**: L93 dates from 2026-03-30 (8fc258c4df), and L89/L91 from 2026-02-23/24. Tonight's refine (2e97f7ab5a) touched L49 only. The phrase appears in no review file and no queued task.
- **Recommendation**: Priority 1.

### W2. `concepts/language-and-consciousness` L83: PCS stated as failed
- **Family**: outside the brief's list. It is the sibling of check 154 W5.
- **Quote**: "That debt is what the [phenomenal concepts strategy](/concepts/phenomenal-concepts-strategy/) was built to discharge, and the dilemma above is the reason it does not."
- **Issue**:
  - `phenomenal-concepts-strategy` L79 says "The argument has not closed the debate, and the Map does not present it as having done so", and records that PCS defenders dispute the dilemma's explanandum.
  - `tenets.md` L103 says "The question is open."
  - The line dates from 2026-08-02 (f1acc6421d).
- **Recommendation**: Priority 1 (e). It shares a file with W1, and W1's fix (c) concedes PCS's prediction, so both must move together.

### W3. `concepts/symbol-grounding-problem` L105 and L151: [P-AC1](/positions/ai-consciousness-scope/#p-ac1) moved to "ruled out"
- **Family**: 9.
- **Quotes**:
  - L105: "LLMs achieve linguistic competence without linguistic understanding." … "Since no theory attributes consciousness to lookup tables, none should attribute it to LLMs—and without consciousness, there is no thick grounding."
  - L151 (Further Reading): "Why static systems cannot be conscious (and thus lack thick grounding)".
- **Issue**:
  - [P-AC1](/positions/ai-consciousness-scope/#p-ac1) (`positions/ai-consciousness-scope` L56): "The verdict is *'low probability,' not 'ruled out'*". Its credence is "moderate (low edge)".
  - The cited page declines the strong form: the inference "is therefore defeasible, not necessary" (`continual-learning-argument` L176). Its Dualism paragraph adds that Hoel's result "does not favour dualism" (L158).
  - Tonight's 22:25 refine (3507aa0292) corrected L125 on this page and L49 on its sibling. L105 sat in the same file and was not reached. It dates from 2026-02-02 (07d3bd6ccf).
- **Recommendation**: Priority 2 (a)–(c).

### W4. `concepts/intentionality` L197 (and L191, L195, description): [P-AC1](/positions/ai-consciousness-scope/#p-ac1) grounded on the wrong premise, stated categorically
- **Family**: 9 and 11.
- **Quotes**:
  - L197: "The Map's position: [AI consciousness](/topics/ai-consciousness/) is unlikely given current architectures because they lack whatever grounds original intentionality."
  - L191: "computational systems cannot have genuine intentionality. They manipulate symbols according to rules but never mean anything." This is conditional on Searle.
  - L195: "LLMs lack the phenomenal markers that reveal intentionality in humans".
  - Description: "Phenomenal intentionality theory shows content requires consciousness".
- **Issue**:
  - [P-AC1](/positions/ai-consciousness-scope/#p-ac1) places the verdict "not because they fail behavioural tests, but because a substrate analysis under the Map's mechanism account finds no sites for the interface to act on" (L56). L197 substitutes a premise the register does not use and asserts it as fact. On the page's own moderate PIT, lacking original intentionality is lacking phenomenal consciousness, so the because-clause asserts what the verdict calls "unlikely".
  - L191's "never mean anything" is the exact sibling of the phrase tonight's refine scoped on `symbol-grounding-problem` L125 ("of their own").
  - L195 asserts the absence of phenomenal states as fact.
  - The description says "shows" where the body says "If PIT is correct" (L45, L87).
  - Ages: L197 2026-01-30 (ab90cccfd9), L191 2026-03-01 (02423c4982), L195 2026-07-19 (242805e92d).
- **Coordination**: The file has 4 words of headroom, and the queued P3 at todo L3188 (L139/L141) must be net ≤ 0. Item (d) below is −2 and the description is free. L191 and L195 are not costed. They belong in the same pass if words allow, or in a later condense.
- **Recommendation**: Priority 2 (d)–(e).

### W5. `voids/witnessing-void` L95: the same-causes inference run against Tenet 3
- **Family**: 2.
- **Quote**: "Either witnessing is causally load-bearing (the AI will exhibit characteristic deficits), or it is not (the Map's [Bidirectional Interaction tenet](/tenets/#bidirectional-interaction) faces serious pressure)."
- **Issue**:
  - The dilemma assumes that if a functional duplicate runs without witnessing, witnessing in us is idle. That is the move the brief names: "same effects, same causes".
  - Block's answer, reported on two window pages today: "One need not be an epiphenomenalist to take seriously the hypothesis that there are alternative realizations of the functional roles of our phenomenal states that are phenomenally blank" (`blocks-harder-problem` L73). The second report is `ai-epiphenomenalism` L77.
  - `blocks-harder-problem` L117: "A phenomenally blank Data no more makes our consciousness idle than an electronic twin makes the hydraulic machine's fluid idle."
  - The line dates from 2026-04-24 (be0d9659b5). No other page in the corpus carries "characteristic deficits" (grep, one hit).
- **Coordination**: The queued MPE P3 (todo L3158) targets L81 and L105 of this file, which are different loci. The file is 2,327 against voids hard 3,000.
- **Recommendation**: Priority 3 (a).

### W6. `concepts/phenomenology-of-choice-and-volition` L165 and L163 (and L90): No Many Worlds and Tenet 2 read off the phenomenology
- **Family**: 5 and 4.
- **Quotes**:
  - L165: "Choice phenomenology presupposes singular actualisation. You experience A as *the* outcome, not one branch among equals. The felt openness before decision and closure after matches collapse rather than branching."
  - L163: "Choosing feels like biasing outcomes, not injecting energy." … "matches consciousness repeatedly selecting among competing neural patterns at points of quantum indeterminacy."
  - L90: "This iterative character matches what the Map's framework predicts".
- **Issue**:
  - L165: On Everett each post-branching agent experiences one outcome as *the* outcome. `tenets.md` L172 records that determinate first-person facts are "available branch-relatively", and six window pages concede it (Summary, shape 2).
  - L163: Tenet 2's minimality is "empirical-constraint minimality" (`tenets.md` L69). No feeling can tell a bias from a small energy injection.
  - L90/L163: Any iterative control process matches a renewal rhythm of a few seconds.
  - Today's pessimistic review recorded L165 and L163 as "next in line" ([reviews/pessimistic-2026-10-24-phenomenology-of-choice-and-volition.md](/reviews/pessimistic-2026-10-24-phenomenology-of-choice-and-volition/) L198–L199, L598–L601). They were not minted: only Items 1–3 (done at 15:34Z) and the BLOCKED Item 4 (todo L3116) were. Neither locus touches the Tenet 3 quantifier, so neither needs to wait on todo L661.
- **Recommendation**: Priority 4.

### W7. The same Family 5 drift on three siblings
- **Family**: 5.
- **Quotes**:
  - `concepts/intentionality` L235: "Many-worlds fractures this unity ... none of which is determinately *me* thinking *this*."
  - `concepts/temporal-consciousness` L202: "If MWI branching occurred constantly, there would be no unified temporal experience but fragmentation across branches."
  - `concepts/problem-of-other-minds` L202: "Rejecting MWI means there's a determinate fact about whether you have phenomenal experience".
  - Milder: `symbol-grounding-problem` L137 ("undermining the indexical anchor meaning requires") and `witnessing-void` L103 ("The phenomenology of witnessing is precisely that of singular, undivided presence").
- **Issue**: As in W6. Each branch carries a unified intender, a unified temporal stream and a determinate phenomenal fact. `temporal-void` L152, in the same window, states the concession its concept sibling lacks: "Branch-relative indexicality can already secure the pastness-feel branch-locally".
- **Headroom**: intentionality 4 (W4 governs), problem-of-other-minds 39, temporal-consciousness 493.
- **Recommendation**: Not in the Priority List (cap). The driver may mint it as a sweep that reuses W6's wording, once Priority 4 lands.

### W8. `concepts/pairing-problem` L121: closure denied with no chance-fixing concession anywhere on the page
- **Family**: 3.
- **Quote**: "The quantum framework thus addresses both the causal closure objection (physics has gaps where consciousness acts) and the pairing problem".
- **Issue**:
  - "Gaps where consciousness acts" denies closure and asserts actual efficacy in one clause.
  - The file has 0 hits for chance/born/probab, against 16 for "quantum" (control).
  - Check 153's standard (applied at check 154 Note 9) passes an unscoped line only where the same file carries the concession, and this file does not.
  - The line dates from 2026-01-15. Today's 09:44 refine added the Griffin paragraph and left it.
  - The file is 2,623, headroom 876.
- **Recommendation**: Not in the Priority List. One clause ("physics fixes the chances but not which outcome occurs, and whether consciousness settles it is the Map's open [mechanism debt](/positions/quantum-interface/#mechanism-debt)") would bring it to the `access-consciousness` standard installed today.

### W9. `concepts/ai-epiphenomenalism` L79: an explanatory-exclusion lesson the Map would reject for humans
- **Family**: 6 (internal Tenet 5) and 2.
- **Quote**: "But the epiphenomenal AI scenario shares the zombie argument's central lesson: if you can fully explain the system's behaviour without reference to experience, you have no grounds for positing experience. The computational processes of an LLM explain its outputs completely. Adding a bound conscious entity to this picture explains nothing further—the experience is an idle wheel."
- **Issue**:
  - The "central lesson" is a parsimony-shaped exclusion rule. `tenets.md` L147 rules out "any Map argument that leans on parsimony as if this tenet did not apply to it". Applied to humans under closure-as-sufficiency, the rule would remove the grounds for positing our experience.
  - The zombie argument's lesson runs the other way: experience is a further fact the physical story does not fix.
  - It also sits directly after today's insertion (L77) reporting Block's p. 404. On `blocks-harder-problem` L117, superficial equivalence remains a defeasible reason (C2) that "physical dissimilarity weakens without cancelling", which is not "no grounds".
  - The line dates from 2026-10-03 (f98805bb45). The file is 2,932, headroom 567.
- **Recommendation**: Not in the Priority List. Scope the lesson to *behavioural* grounds ("no behavioural grounds for positing experience") and attribute the inference to the scenario, not to the zombie argument.

### W10. `concepts/llm-consciousness` L124 and L130: the verdict table reads stronger than [P-AC1](/positions/ai-consciousness-scope/#p-ac1)
- **Family**: 9.
- **Quotes**: "| Non-physical component | Yes (per dualism) | No |" and "| Phenomenal character | What it's like | Almost certainly nothing |".
- **Issue**:
  - [P-AC1](/positions/ai-consciousness-scope/#p-ac1)'s credence is "moderate (low edge; conditional ...)" and its verdict is "not 'ruled out'". The table states the absence of a non-physical component flatly, and "almost certainly" claims more than a moderate, low-edge credence in a low-probability verdict.
  - The 2026-06-02 deep review ratified "Almost certainly nothing" as "appropriately hedged" (L49). That stability note predates [P-AC1](/positions/ai-consciousness-scope/#p-ac1)'s 2026-10-15 re-band to "moderate (low edge; conditional)" (register L64), so it should not pre-empt this finding.
  - The page's L132 is conditional ("if the Map's interface account holds"), and L136 ("'almost certainly' is not 'certainly'") already partly qualifies it.
  - The open P3 at todo L2728 targets L68, a different locus. The file is 3,134, headroom 365.
- **Recommendation**: Not in the Priority List. The operator decides whether a stale stability note still binds.

### W11. `voids/perceptual-reality-monitoring-void` L110/L112 and `voids/capability-division-problem` L118/L120: tenet sections without the [P-V2](/positions/voids-as-evidence/#p-v2) disclaimer
- **Family**: 1 (Over-reach). The ladder rung earned is **compatible**.
- **Quotes**:
  - Perceptual-reality-monitoring L110: "the empirical purchase of reality-monitoring strengthens the broader claim that interface-sites are systematically opaque".
  - L112: "The discriminator's structural opacity is the kind of result the Map expects on **dualism**".
  - Capability-division L118: "Tenet 1 ([Dualism](/tenets/#dualism)) establishes that consciousness is irreducible".
  - L120: "The Map interprets the capability division problem as evidence that dualism requires a different kind of explanatory framework than physicalism provides. Physicalism explains vision entirely in neural terms and treats consciousness as something to be explained away."
- **Issue**:
  - No rival is named. L112's own gloss ("a sub-personal mechanism whose outputs are all the consciousness it constitutes ever receives") is physicalist-compatible.
  - L120's "treats consciousness as something to be explained away" describes eliminativism, not physicalism.
  - `tenets.md` L55 calls Tenet 1 "a commitment the Map owns, not a result it reports".
  - [P-V2](/positions/voids-as-evidence/#p-v2) (`positions/voids-as-evidence`) says a tenet removing a defeater does not upgrade a void's evidence.
  - Both files were touched today only for links (f5626231e4, f9b1f468a7). Headroom: 375 and 5.
- **Recommendation**: Not in the Priority List. Capability-division needs a net-zero pass.

### W12. `voids/witnessing-void` description and L41: an unconditioned impossibility claim
- **Family**: 7.
- **Quotes**:
  - Description: "The act of witnessing cannot witness itself—a structural impossibility at the centre of consciousness".
  - L41: "The witnessing void is the impossibility of examining the act of witnessing from the inside."
- **Issue**:
  - `handedness-void` L70, written today: "Every catalogue entry that claims a limit 'in principle' should carry the qualifier: relative to which theory?"
  - The page's body does carry defeaters (L109 "What Would Challenge This View"), so the navigation surface claims more than the body.
- **Recommendation**: Priority 3 (b), at 0 words.

## Notes

1. **`topics/blocks-harder-problem` L109 was checked and passes, conditionally.**
   - The sentence: "Since the sketch runs against the Map's own default commitments, it is no test the Map can run".
   - [P-Q2](/positions/quantum-interface/#p-q2) (L68) keeps outcome frequencies "Born-exact in every publicly conditionable context; only conditionals on the conscious state itself are free". For a machine, a task-conditioned deviation runs against [P-Q2](/positions/quantum-interface/#p-q2), and a conscious-state conditional presupposes the answer. So the sentence is right on the register as written.
   - It reads harder than `tenets.md` L75, where a deviation conditioned on "intention, task or subject would test the corridor itself". That grain is the open P1 HUMAN DECISION at todo L1945. Revisit L109 if the operator widens [P-Q2](/positions/quantum-interface/#p-q2).
2. **`topics/blocks-harder-problem` L142.** The Further Reading label "Searle's view, whose biological claim Block endorsed in 2002" has no body support on the page. It is sourced, however (`research/blocks-harder-problem-2026-10-24` L384, Block p. 406), so it passes.
3. **`concepts/phenomenology-of-choice-and-volition` L137.** "The witness must still steer a little, or it could not cause its own reports" assumes the self-stultification premise that `tenets.md` L101 makes conditional, and leans on the universal reading. It belongs to the quantifier NEEDS-HUMAN (todo L661) and is not tasked.
4. **`concepts/presence-type-and-absence-type-voids` L103 and `voids/three-kinds-of-void` L95** assign kinds without a condition: "Presence-type voids are typically both unexplorable ... *and* occluded". "Typically" softens it, and today's deep review left it. It is held to Family 7's "each void's kind stays conditional" only loosely, and is optional.
5. **`voids/three-kinds-of-void` L73 and L105** were human-authored on 2026-01-31 (Andy Southgate), and are flagged for the operator rather than tasked.
   - L73 uses Minimal Quantum Interaction to float "Reality might have its own immune system against insights that would destabilize it". That sits near the tenet's "Not to be confused with" clause.
   - L105, "Dualism makes the Unexplorable possible", overlooks the page's own L57: McGinn's closure is naturalist ("not because it's supernatural").
6. **`voids/three-kinds-of-void` L59, L85, L87, L97** make old in-principle kind assignments, for example "an architectural ceiling no training shifts" (L87). L97's "unexplorable at the operation" is already a human question on the queued taboo-void task (todo L2774, question (b)). Today's addition (L99) passes: "adds no evidence about what lies behind them".
7. **`concepts/symbol-grounding-problem` L41, L131, L135.** The lead and Dualism paragraph say the problem's persistence "provides evidence" and "supports irreducibility". L135 adds that original intentionality "requires phenomenal consciousness that causally participates in cognition". That is the sibling of the queued P3 at todo L2491 (`intentionality` L231, `naturalisation-failure` L143), and it belongs in that task's scope.
8. **`concepts/interactionist-dualism` L192–L193** carry old residue. "A theory explaining nothing (physicalism on experience) is not parsimonious" overstates the linked page, whose description says the parsimony inference is one "the Map declines". "Phenomenal valence tracking fitness *supports* interactionism" grades as support what the co-optimization page calls constraint "without discriminating". The file has 8 words of headroom.
9. **`concepts/intentionality` L53 and L71.** L53: "This supports both Brentano's thesis and the Map's Dualism commitment", after a paragraph built on Husserl (on the firewall roster) with no statement of his stance. L71: "None has succeeded." Both are old. Headroom governs them, as for W4.
10. **`voids/edge-states-and-void-probes`** (today's L141 lessons paragraph): "as [filter theory](/concepts/filter-theory/) predicts" is compatible-grade. The page is at 3,664 against the voids hard 3,000, over the gate, so it is not tasked.
11. **Smaller over-reaches, untasked.** `concepts/process-philosophy` ("The Map's framework explains why rocks lack experience ... quantum processes provide that interface"); `concepts/temporal-consciousness` ("experience is genuinely extended through quantum collapse"); `concepts/ai-consciousness-typology` L165 ("resist third-person adjudication entirely"), which is already item (3) of the cross-review at todo L3095.

## Bearing on the open items

All five items named in the brief are still live. Each was checked by string count against the live file:
- **`phenomenology-of-choice` label task** (todo L3116, BLOCKED on todo L661): L3 "irreducible evidence for conscious causal efficacy", L56 "as evidence that consciousness is a genuine selector" and L123 "provides the strongest evidence" each count 1. Priority 4 does not touch them.
- **Voids-catalogue drift** (todo L3173): the-silence-void "independent traditions" counts 1, and affective-void "permanently beyond human phenomenological reach" counts 1. The taxonomy-of-voids L133 axis sentence is unchanged.
- **MPE overreach** (todo L3158): witnessing-void L81 and L105 count 1, and sleep-consciousness-void "establishing" counts 1.
  - **Scope addition:** `phenomenological-evidence` has a third independence locus the task does not name. It is L162: "heterophenomenology offers no account of *why* independent traditions converge on these specific beliefs". Add it to the task's L56/L194.
  - Priority 3 touches witnessing-void L95 and the description only.
- **Source-attribution** (todo L3134, L3142): "strongly-supported" counts 1, and "cannot retain it even with effort" counts 1.
- **Intentionality L141/L139** (todo L3188): both count 1. Priority 2 (d) is −2 on the same file, which gives that net-zero task room.
- **"Dualism intensifies"** (cross-review, todo L3095): still live at `topics/ai-consciousness` L185, `apex/machine-question` L181 and the unqualified `problem-of-other-minds` L120 "Physicalism treats the link ... as lawlike or constitutive" (each counts 1). It is already queued and not re-raised.

**Tenet 3 quantifier (todo L661).** Window pages bear on it in three ways.
- **Hold it open:** `blocks-harder-problem` L119 ("Read as universal actual efficacy ... Read dispositionally ...") and `precommitment` L104.
- **Pick the universal reading implicitly:** `language-and-consciousness` L93 ("Every meaningful utterance"; Priority 1 removes the quantifier) and `phenomenology-of-choice` L137 (Note 3).
- **Grant a rival both readings:** `nondualistic-interactionism` L93 ("Satisfied on the headline and on both the existential and universal readings"). That is the correct way to keep the Map's own choice open.

## Files Passing All Checks

These pages were read in full, or diff-scoped as stated, and passed on every family:
- Read in full: `topics/blocks-harder-problem` (Notes 1–2), `topics/precommitment-and-the-diachronic-agent`, `topics/memory-anomalies`, `concepts/presence-type-and-absence-type-voids` (Note 4), `concepts/the-ownerless-suffering-argument`, `concepts/nondualistic-interactionism`, `voids/handedness-void`, `voids/three-kinds-of-void` (today's addition; Notes 5–6 cover older lines).
- RSP read in full: `voids/numbing-void`, `voids/preference-void`, `voids/assent-void`, `voids/fusion-void`, `voids/palette-extension-void`, `voids/cross-state-void`.
- Diff-scoped:
  - concepts: `access-consciousness`, `adaptive-computational-depth`, `ai-consciousness-typology` (Note 11; queued item), `anti-correlated-metacognitive-signal`, `biological-naturalism`, `combination-problem`, `discrimination-problem`, `episodic-memory`, `interactionist-dualism` (Note 8), `organizational-invariance`, `phenomenal-contrast-method`, `process-philosophy` (Note 11), `psychophysical-laws`, `self-control-as-skill-and-scaffolding`, `simulation`, `type-specificity`;
  - topics: `ai-consciousness` (queued item), `akrasia-and-weakness-of-will`, `chemosensory-consciousness-and-the-interface`, `deep-computational-markers-for-machine-consciousness`, `diachronic-agency-and-personal-narrative`, `emotion-regulation-and-the-timing-of-control`, `experimental-consciousness-science-2025-2026`, `falsification-roadmap-for-the-interface-model`, `tonic-immobility-and-awareness`, `visual-indexes-and-demonstrative-reference`;
  - voids: `edge-states-and-void-probes` (Note 10), `meta-epistemology-of-limits`, `resolution-void`, `simulation-detection-void`, `temporal-void`;
  - positions: `subject-census`, `subject-census-calibration-history`.

Twelve files carry Warnings: `language-and-consciousness` (W1, W2), `symbol-grounding-problem` (W3, W7), `intentionality` (W4, W7), `witnessing-void` (W5, W7, W12), `phenomenology-of-choice-and-volition` (W6), `temporal-consciousness` (W7), `problem-of-other-minds` (W7), `pairing-problem` (W8), `ai-epiphenomenalism` (W9), `llm-consciousness` (W10), `perceptual-reality-monitoring-void` (W11) and `capability-division-problem` (W11). That makes 8 + 6 + 33 passing files and 12 with Warnings, 59 in all.

## Priority List

Each OLD string below was confirmed by script to occur exactly once, at the line given. Deltas are `count_words` on the frontmatter-stripped body after the replacement, applied cumulatively in the order listed.

1. **`concepts/language-and-consciousness` L89, L91, L93, L83 (W1, W2).** Families 1, 2 and the PCS standard. The file is 2,140 against concepts hard 3,500, so headroom is 1,359. No task is queued on it.
   - (a) L89
     - OLD: `The philosophy of language provides independent support for several of the Map's [[tenets]].`
     - NEW: `The philosophy of language bears on several of the Map's [[tenets]], fitting them without evidencing them.`
     - Delta: +3.
   - (b) L91
     - OLD: `**[[tenets#^dualism|Dualism]]** gains support from reference failures.`
     - NEW: `**[[tenets#^dualism|Dualism]]** fits the reference failures.`
     - Delta: −1.
   - (c) L91
     - OLD: `These anomalies are exactly what we would expect if consciousness involves something irreducible to the physical.`
     - NEW: `These anomalies are what we would expect if consciousness involves something irreducible to the physical, though the phenomenal concepts strategy predicts the same anomalies on physicalism.`
     - Delta: +10.
   - (d) L93
     - OLD: `finds support in the Gricean analysis of meaning. If meaning requires conscious intention, and meaningful speech is causally efficacious (it changes behaviour, coordinates action, transmits knowledge), then consciousness causally contributes to the physical world through language. Every meaningful utterance is an instance of [[mental-causation-and-downward-causation|downward causation]]—conscious intention shaping physical sound waves and written marks. This directly contradicts [[epiphenomenalism]], which must treat the apparent purposefulness of speech as coincidental—our words happen to match our experiences, but the experiences play no causal role in producing them.`
     - NEW: `meets the Gricean analysis of meaning as a conditional. If meaning requires conscious intention, and meaningful speech is causally efficacious (it changes behaviour, coordinates action, transmits knowledge), then consciousness contributes to the physical world through language, and a meaningful utterance would be an instance of [[mental-causation-and-downward-causation|downward causation]]. An [[epiphenomenalism|epiphenomenalist]] need not call the match between our words and our experiences coincidental: a common neural cause can produce both, and whether that reply survives the self-stultification objection turns on a contested premise about knowledge ([[tenets#^tenet-3-epiphenomenalism|Tenet 3]]). The analysis fits the tenet without evidencing it, and says nothing about how widely conscious efficacy operates.`
     - Delta: +19.
   - (e) L83
     - OLD: `That debt is what the [[phenomenal-concepts-strategy|phenomenal concepts strategy]] was built to discharge, and the dilemma above is the reason it does not.`
     - NEW: `That debt is what the [[phenomenal-concepts-strategy|phenomenal concepts strategy]] was built to discharge; the Map holds that the dilemma above blocks it, while PCS defenders dispute the dilemma, so the exchange stays open.`
     - Delta: +10.
   - Net: **+41** (2,140 → 2,181).
   - Guards:
     - Never concede epiphenomenalism. (d) states its reply and the conditional premise, as `tenets.md` L101 does, and does not adopt it.
     - Keep the quantifier open: no "every", no "whenever".
     - Do not enlist Grice, Searle or Wittgenstein. None argues for dualism.
     - (e) follows `phenomenal-concepts-strategy` L79. Do not name Carruthers & Veillet without adding a References entry.
     - The anchor `tenets#^tenet-3-epiphenomenalism` exists (tenets L101), and the new wikilinks are piped.
2. **`concepts/symbol-grounding-problem` L105, L151 and `concepts/intentionality` L197, description (W3, W4).** Family 9: the LLM-reference cluster edited tonight.
   - **symbol-grounding-problem**: the file is 2,644 against concepts hard 3,500, so headroom is 855.
     - (a) L105
       - OLD: `LLMs achieve linguistic competence without linguistic understanding.`
       - NEW: `Current LLMs probably achieve linguistic competence without linguistic understanding.`
       - Delta: +2.
     - (b) L105
       - OLD: `Since no theory attributes consciousness to lookup tables, none should attribute it to LLMs—and without consciousness, there is no thick grounding.`
       - NEW: `Hoel concludes that no non-trivial theory can attribute consciousness to LLMs; the Map holds that inference defeasible and places current LLMs on the low-probability side, not ruled out ([[positions/ai-consciousness-scope#^p-ac1|P-AC1]]). Without consciousness, there is no thick grounding.`
       - Delta: +15.
     - (c) L151
       - OLD: `Why static systems cannot be conscious (and thus lack thick grounding)`
       - NEW: `Hoel's argument that static systems are not conscious, which the Map holds defeasible`
       - Delta: +2.
     - Net for the file: **+19** (2,644 → 2,663).
   - **intentionality**: the file is 3,495 against concepts hard 3,500, so headroom is 4.
     - (d) L197
       - OLD: `is unlikely given current architectures because they lack whatever grounds original intentionality.`
       - NEW: `is low probability, not ruled out, for current architectures ([[positions/ai-consciousness-scope#^p-ac1|P-AC1]]).`
       - Delta: **−2**.
     - (e) Description (L3)
       - OLD: `Phenomenal intentionality theory shows content requires consciousness`
       - NEW: `Phenomenal intentionality theory holds that content requires consciousness`
       - Delta: 0 (frontmatter).
     - Net for the file: **−2** (3,495 → 3,493).
   - Coordination:
     - Fold (d) and (e) into the queued net-zero P3 at todo L3188 (intentionality L139/L141). Together they keep that task at or below zero with 2 words to spare.
     - L191 ("never mean anything") and L195 ("LLMs lack the phenomenal markers") belong in the same pass if words allow. They are not costed here.
   - Guards:
     - [P-AC1](/positions/ai-consciousness-scope/#p-ac1) moves in neither direction. "Low probability, not ruled out" is the register's own wording (L56).
     - Hoel's conclusion is reported as his, using `continual-learning-argument` L59's "No non-trivial theory".
     - Derived reference does not imply phenomenal understanding.
3. **`voids/witnessing-void` L95 and description (W5, W12).** Families 2 and 7. The file is 2,327 against voids hard 3,000, so headroom is 672.
   - (a) L95
     - OLD: `Either witnessing is causally load-bearing (the AI will exhibit characteristic deficits), or it is not (the Map's [[tenets#^bidirectional-interaction|Bidirectional Interaction tenet]] faces serious pressure).`
     - NEW: `An AI without deficits would show that the functions can run without witnessing, not that witnessing is idle in us: as Block [[blocks-harder-problem#same-causes|replies to the same-causes objection]], a phenomenally blank realisation of our functional roles implies no epiphenomenalism about our own experience, so [[tenets#^bidirectional-interaction|Bidirectional Interaction]] would stand where it does.`
     - Delta: **+27**.
   - (b) Description (L3)
     - OLD: `a structural impossibility at the centre of consciousness`
     - NEW: `on the Map's reading, a structural impossibility at the centre of consciousness`
     - Delta: 0 (frontmatter).
   - Coordination: the queued MPE P3 (todo L3158) edits L81 and L105 of this file. These are different loci, and the order does not matter.
   - Guards:
     - The anchor `blocks-harder-problem#same-causes` exists (L71).
     - Block's sentence is reported, not quoted. The verbatim text is on `blocks-harder-problem` L73 (p. 404).
     - The NEW drops "load-bearing" (writing-style).
     - Keep the following sentence ("The witnessing void does not predict the outcome; it sharpens what the outcome will tell us").
4. **`concepts/phenomenology-of-choice-and-volition` L165, L163, L90 (W6).** Families 5 and 4. The file is 3,174 against concepts hard 3,500, so headroom is 325. The BLOCKED P3 at todo L3116 holds +26 nominal on other loci, which leaves about 299.
   - (a) L165
     - OLD: `Choice phenomenology presupposes singular actualisation. You experience A as *the* outcome, not one branch among equals. The felt openness before decision and closure after matches collapse rather than branching.`
     - NEW: `Choice phenomenology fits singular actualisation: you experience A as *the* outcome. An Everettian predicts the same experience on every branch, felt openness and closure included, so the phenomenology does not discriminate; the Map's rejection of many-worlds rests on the indexical objection, held as a commitment.`
     - Delta: +16.
   - (b) L163
     - OLD: `Choosing feels like biasing outcomes, not injecting energy. The iterative character of sustained voluntary attention — James's "successive efforts" — matches consciousness repeatedly selecting among competing neural patterns at points of quantum indeterminacy.`
     - NEW: `The tenet's minimality is an empirical constraint that no feeling can test: a bias and a small energy injection would feel alike. The iterative character of sustained voluntary attention — James's "successive efforts" — is consistent with repeated selection at points of quantum indeterminacy, as it is with any iterative control process.`
     - Delta: +19.
   - (c) L90 (optional)
     - OLD: `This iterative character matches what the Map's framework predicts:`
     - NEW: `This iterative character fits, without discriminating, what the Map's framework expects:`
     - Delta: +2.
   - Net: **+37** (3,174 → 3,211).
   - Guards:
     - Do NOT touch L3, L56, L121, L123 or L119. They belong to the BLOCKED Item 4 task (todo L3116).
     - These loci do not touch the Tenet 3 quantifier, so they need not wait on todo L661.
     - The James quotations at L84 and L90 are verbatim (pessimistic review L211). Keep them.
     - (a) and (b) follow the pessimistic review's language table (L198–L199) and extend it to the full paragraph, so no sentence is left saying "matches collapse rather than branching".

**Not tasked here:**
- W7 is a Family 5 sweep of three siblings. Mint it after Priority 4 lands, so it can reuse that wording.
- W8–W11 fall below the cap. Each Warning carries its own one-line fix or the operator question.
- Notes 1–11 are leads, or covered by queued tasks. Note 7 should extend the scope of todo L2491. The open-items section gives one scope addition for todo L3158 (`phenomenological-evidence` L162).