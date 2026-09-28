---
title: Tenet Alignment Check - 2026-09-28
created: 2026-09-28
modified: 2026-09-28
human_modified: 2026-09-28
ai_modified: 2026-09-28T12:20:00+00:00
draft: false
description: "Tenet check 141: none of check 140's six ERRORs was minted or repaired; eight new ERRORs, five of them fabricated tenet predictions and three relocating Tenet 3 away from outcome-selection."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: Andy Southgate
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-28
last_curated:
last_deep_review:
---

# Tenet Alignment Check

**Date**: 2026-09-28 (check 141; previous `reviews/tenet-check-2026-09-27.md` = 140)
**Files checked**: 101 files read in full by five sub-sweeps. This covers every live file in `topics/ concepts/ positions/ apex/ voids/ tenets/` with a commit since check 140 (2026-09-27 06:25 UTC), about 354k words. Four of the files are new: `concepts/diverging-worlds-everettianism`, `concepts/pudgalavada`, `topics/paradoxical-kinesia`, `topics/time-bias-and-thank-goodness-thats-over`. `tenets.md` was read in full. It had one commit since check 140 (e3e689517d), which changed only the Maier et al. 2018 clause in the Tenet-2 "Empirical risk" paragraph; the five definitions and every Rules-out clause are unchanged. Every carried locus from checks 137–140 was re-probed by exact string.
**Errors**: 8 new, 6 carried (all six check-140 ERRORs are still live). 14 live.
**Warnings**: about 105 new loci across about 55 files, plus about 30 carried loci that are still live.
**Notes**: about 90
**Lens**: same as checks 138–140. First test: direct conflict with a Rules-out clause. Second test: does the lead, the alignment section or a body sentence claim more than the article's own argument or `tenets.md` supports?

## Summary

**1. Nothing from check 140 was minted, so nothing moved.** `grep tenet-check-2026-09-27 workflow/todo.md` returns no task. All six check-140 ERROR strings are live at one hit each, and no open task in the Active section covers any of them. Three of the six files had no commit; the other three (`born-rule-and-the-consciousness-interface`, `causal-closure`) were touched only by sweeps (601e49b435, e3e689517d) that did not reach the flagged sentence. The check-139 priority 4 (`concepts/dualism` L172/L154) is now on its third unminted report. The pattern from checks 138–140 holds for a fourth report: minting is what moves items, and a report that is not minted produces nothing.

**2. The Maier correction propagated cleanly, with two exceptions.** e3e689517d re-scoped 15 files so that the Maier et al. 2018 external-RNG null is no longer a conditioned test of the brain-internal corridor. A corpus-wide grep for "Maier" finds every out-of-window mention (`brain-specialness-boundary` L101, `selection-only-channel` L78, `channel-class-taxonomy` L78, `machine-question` L149) already correctly scoped as an external null. Two loci in committed files still count it against Tenet 3:
- `topics/falsification-roadmap-for-the-interface-model.md` L107: the null "has already partially foreclosed one visible branch of bidirectional interaction", and the surviving reading is "suppressed deviations below current sensitivity", which is the sensitivity-limit framing tenets L75 rules out ("by construction, not by any sensitivity limit").
- `concepts/ensemble-level-epiphenomenalism.md` L61 charges the null against the outside-corridor family while its own L67 exempts external RNGs via brain-locality.

**3. New ERROR class: fabricated tenet predictions and entailments (5 of 8).** Check 140 found Tenet 1 made to "predict" and "reject" things. This window the same move appears against every tenet but Tenet 5:
- Tenet 3 "predicts" an irreplaceable functional contribution (falsification-roadmap L173) and "predicts exactly this two-directional structure" (returning-attention L97).
- Tenet 2 "predicts" a narrow interface to action-relevant alternatives (consciousness-and-agency L120).
- Tenet 4 "requires a fact about which conscious subject I am" and the tenets jointly "imply haecceity" (haecceity L181), against tenets L121, which says the non-deflationary "I" is endorsed "on independent grounds… not from within this tenet".
- Tenet 1 endorses consciousness as "a basic feature of reality" (composition-and-consciousness L111), the check-140 ERROR-3 class.
A corpus-wide grep for the attribution forms (`tenet predicts`, `Tenet N predicts`, `tenets imply`, `Interaction]] predicts`, `Dualism]] predicts`) hits 20 files. Not every hit is a defect, but the list is the sweep boundary and is given under Priority 2.

**4. New ERROR class: Tenet 3 relocated away from outcome-selection (3 of 8).** Tenets L91 commits Tenet 3 to outcome-selection and registers the context-selection alternative as "not adopted". Three quantum-wing articles put the Map somewhere else:
- `indexical-identity-quantum-measurement` L147/L161: physical mechanisms select; consciousness only "determines *for whom* each outcome is actual". That is the acausal many-minds structure `many-minds-interpretation` L86 says is "where MMI and the Map part decisively".
- `many-minds-interpretation` L86: Tenet 3 has consciousness "modulating the statistics of a real, local collapse", against tenets L75 (the bias acts on the single outcome, the aggregate measure is left intact) and P-Q2.
- `quantum-consciousness` L114: "something must still select… the philosophical case for consciousness as outcome-selector stands on its own", against tenets L184 ("the measurement problem cannot itself be evidence for conscious selection").
All eight new ERROR strings were present at the check-140 baseline (`git show HEAD@{2026-09-27T06:25:00Z}` finds each). They are new to the report because their files were committed this window, not because a commit introduced them.

**5. The families persist, at the same density.**
- **Family S (Tenet 3 held as actual, or epiphenomenalism reported refuted): about 45 new loci.** The densest new cluster is the attention/effort wing after the Rajan sweep (3e228ba788 touched 18 files and left the causal gloss in place in most of them): `apex/attention-as-causal-bridge` L52/L80/L140/L172, `concepts/attentional-economics` L50/L87/L103, `topics/structure-of-attention` L195/L221/L249, `topics/trilemma-of-selection` L76/L127/L129, `topics/authentic-vs-inauthentic-choice` L33.
- **Family I (felt definiteness cited against MWI): about 15 new loci**, plus a sub-class the 2026-09-28 refines of `agent-teleology` and `meaning-void` repaired in two files and left in the rest: the quick "under MWI there is nothing to select" argument. Corpus-wide the phrase family hits 18 files; in this window it is live at `attentional-economics` L196, `brain-interface-boundary` L170, `neuroplasticity` L152, `consciousness-selecting-neural-patterns` L152, `empirical-evidence-for-consciousness-selecting` L169, `the-interface-problem` L161, `quantum-neural-timing-constraints` L174.
- **Illusionism/physicalism reported refuted by self-stultification or the bare "an illusion must appear to something" regress: about 12 loci** (`libet-experiments` L141, `quantum-indeterminacy-free-will` L162, `reasons-responsiveness` L82, `agent-teleology` L63, `phenomenology-of-agency-vs-passivity` L143, plus bare-regress NOTEs). Tenets L101–103 hold self-stultification as "the deepest difficulty… rather than its refutation"; `illusionism` L91 says the regress "proves nothing".
- **Coherence closure listed as a framework falsifier: 7 loci** (`consciousness-selecting-neural-patterns` L166/L170, `quantum-consciousness` L172, `evolution-under-dualism` L155, `authentic-vs-inauthentic-choice` L214, `agent-causation` L160, `the-interface-problem` L147), against tenets L77 ("post-decoherence-selection proposals do not depend on it").
- **Tenet 5 misgrounded: 4 loci** treat Tenet 2's minimality as parsimony or Tenet 5 as a thesis about reduction (`causal-consistency-constraint` L73, `teleosemantics` L92, `tenet-generated-voids` L77, and out-of-window `geometric-model-of-mind` L113 "the Map because parsimony favours the smallest non-physical influence"), against tenets L69, which says Tenet 2's minimality "is not the kind of minimality Tenet 5 declares unreliable".

**6. The four new articles are clean.** `diverging-worlds-everettianism` states the Tenet-4 scoping, the global-exclusion posit and the Tenet-5 discipline correctly; `pudgalavada` holds the persisting subject as a posit and records Vasubandhu's closure argument as an unrefuted rival; `paradoxical-kinesia` holds Tenet 3 "at its available standing"; `time-bias-and-thank-goodness-thats-over` rests its MWI remark on indexicality and concedes the branch-weight reply. Fresh-create quality is not the problem; the backlog is.

## Errors

All fourteen were independently re-verified with exact-string grep: one hit at the stated line, context read. Line numbers are as of 2026-09-28 12:10 UTC.

### New (8)

1. **`concepts/composition-and-consciousness.md` L111** (Tenet 1, fabricated tenet content). "It is a basic feature of reality that must be accepted rather than explained in terms of something more fundamental. This is the position the Map endorses through its [[tenets#^dualism|Dualism tenet]]."
   - Tenets L53: Tenet 1 states irreducibility. Tenets L125: minds arrive "billions of years before" nothing; consciousness is a late arrival on the Map's own account. Same class as check-140 ERROR 3 (`combination-problem` L175), which is also still live.
   - **Fix:** "Consciousness is irreducible—not explained in terms of something physical. This is the position the Map holds through its Dualism tenet."
2. **`topics/falsification-roadmap-for-the-interface-model.md` L173** (Tenet 3, fabricated tenet content). "this challenges Tenet 3's prediction that consciousness makes an irreplaceable functional contribution."
   - Tenets L93: Tenet 3 is "a metaphysical commitment supported by self-stultification and indirect evidence". It predicts nothing about AI capacity; the matrix's machine-consciousness rows mark interactionism *not invoked* for bare phenomenality.
   - Same-file sibling **L107**: the Maier null "partially foreclosed one visible branch of bidirectional interaction" and "suppressed deviations below current sensitivity remain compatible", against tenets L75 and the e3e689517d correction. **L93** "in-principle accessible as detection thresholds improve" is the check-140 ERROR-5 class, scoped to the mapping problem.
   - **Fix:** L173 "this would remove the indirect empirical support the Map cites for Tenet 3, not falsify a prediction the tenet makes"; L107 re-scope the null as external and replace "below current sensitivity" with "in the conditioned register only".
3. **`topics/phenomenology-of-returning-attention.md` L97** (Tenet 3, fabricated tenet content). "The [[tenets#^bidirectional-interaction|Bidirectional Interaction]] tenet predicts exactly this two-directional structure within a single attentional event."
   - The article's own L79 says the three accounts at L71–75 are "underdetermined by the evidence" and the Map's reading is "a stance taken within that underdetermination". A tenet that predicts what its rivals also predict predicts nothing. Sibling: L39 (the lead) "predicts exactly this structure".
   - **Fix:** "is what the Bidirectional Interaction tenet would lead one to expect; the accounts at L71–75 expect the same".
4. **`apex/consciousness-and-agency.md` L120** (Tenet 2, fabricated tenet content). "a narrow interface to action-relevant alternatives is what [[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]] predicts."
   - Tenets L61–85 make no claim about counterfactual scope. The narrowness comes from the article's own agent-causation constraints, not the tenet.
   - **Fix:** "is consistent with Minimal Quantum Interaction".
5. **`concepts/haecceity.md` L181** (Tenet 4, contradicts tenets L121). "The Map's tenets imply haecceity about conscious subjects… **No Many Worlds** requires a fact about which conscious subject I am."
   - Tenets L121: the non-deflationary "I" is endorsed "on independent grounds (the agency cluster's substance-leaning sub-reading needs a persisting subject…), not from within this tenet." Tenets L123: the tenet "inherits weight from the Map's theory of subjecthood", not the reverse. The article's own L183/L189 say the diachronic fact is posited.
   - **Fix:** "The Map's tenets *presuppose* haecceity about conscious subjects rather than imply it: No Many Worlds draws on a fact about which subject I am (tenets L121)".
6. **`topics/many-minds-interpretation.md` L86** (Tenets 2/3, contradicts tenets L75). "Under [[tenets#^bidirectional-interaction|Tenet 3]], consciousness *biases* which outcome obtains, modulating the statistics of a real, local collapse."
   - Tenets L75: "The bias acts on which single outcome is realised, not on the aggregate measure". P-Q2 preserves Born statistics exactly. "Modulating the statistics" states the outside-corridor reading as the tenet.
   - Same wording at `concepts/many-worlds.md` L186 "by modulating statistics within objective-collapse events" and `concepts/quantum-consciousness.md` L52 "consciousness *modulates* statistics within those events" (counted as WARNINGs; the latter two add "within Born-rule limits" nearby).
   - **Fix:** "biases which single outcome is realised at a real, local collapse while leaving the aggregate statistics Born".
7. **`concepts/quantum-consciousness.md` L114** (Tenets 2/4, contradicts tenets L184). "After decoherence, the system remains in a statistical mixture—something must still select which outcome becomes actual… the philosophical case for consciousness as outcome-selector stands on its own."
   - Tenets L184: "once objective reduction secures definiteness, the measurement problem cannot itself be evidence for conscious selection—the agency evidence (Tenet 3) must carry that burden." Tenets L125: baseline selection is physical. This is the check-140 ERROR-6 class (`testing-consciousness-collapse` L179, still live) in the concept article `tenets.md` itself links for Orch OR.
   - **Fix:** "the measurement problem remains open, which leaves room for the Map's outcome-selection posit without supplying evidence for it".
8. **`topics/indexical-identity-quantum-measurement.md` L147** (Tenet 3, contradicts tenets L91; Tenet 4). "Physical mechanisms… select which outcomes are possible. Consciousness determines *for whom* each outcome is actual." Sibling L161 "determining which outcome is actual *for this subject*".
   - This is presented as "The proposal" the tenets suggest, not as a rival. Tenets L91: Tenet 3 commits to "*outcome-selection*, influence over which definite outcome becomes actual" and registers context-selection as "not adopted". Subject-relative actuality is neither; it is the acausal many-minds structure that `many-minds-interpretation` L86 says the Map rejects, and it sits against the global-nonactuality posit the same article invokes at L165. The article's own L141 says reports "must involve causal flow from mind to matter", which L147's picture does not supply.
   - **Fix:** either rewrite the proposal as outcome-selection ("consciousness biases which of the physically possible outcomes becomes actual, and that outcome is actual for everyone") or mark it explicitly as a registered alternative the Map has not adopted, as tenets L91 does for context-selection.

### Carried (6, all from check 140; none minted, none repaired)

9. `topics/kabbalah-tzimtzum-consciousness-matter.md` L78 "The Map is a substance dualism… exactly the monism its first tenet rejects" (with L34, L84). No commit.
10. `topics/consciousness-and-collective-phenomena.md` L162 "The Dualism tenet predicts that consciousness should not arise from just any complex system". No commit.
11. `concepts/combination-problem.md` L175 "Not a late emergence but a basic feature of reality (the Dualism tenet)". No commit.
12. `topics/born-rule-and-the-consciousness-interface.md` L110 "a further question the Map answers affirmatively". Two commits since (601e49b435, e3e689517d) touched L170 and L209 only. L219 sibling "reflects genuine bidirectional causation" also live.
13. `topics/brain-internal-born-rule-testing.md` L157 "instrument-relative rather than principled", with L143, L153, L155. No commit.
14. `topics/testing-consciousness-collapse.md` L179 "constitutes indirect evidence that consciousness is structurally implicated", with the L203 table row and L215. No commit.

**Booked family, not recounted:** `concepts/implicit-memory.md` L196 (Tenet-5 tiebreaker), covered by the blocked `NEEDS-HUMAN (doctrine) 2026-09-19` item.

**Borderline (counted as WARNING):**
- `topics/mathematical-structure-of-the-consciousness-physics-interface.md` L89/L92/L154: if micro-PK signals appeared, "MQI would sanction moving the minimum outside the corridor without any tenet change". Tenets L85 rules out "any interaction that would be empirically detectable under current experimental precision", so a detected signal is a tenet change, not a reading change. Tenets L81 does name "minimum-outside-corridor readings", which is why this is held at WARNING pending adjudication rather than counted as an ERROR. `falsification-roadmap` L95 mirrors it.
- `concepts/multi-mind-collapse-problem.md` L129: neural statistics "should deviate from what pure decoherence predicts—particularly during focused attention". Testable only in the conditioned register (P-Q3); as written it predicts an unconditioned deviation against the article's own L97.
- `voids/tenet-generated-voids.md` L77 "why exactly minimal? The fine-tuning cries out for explanation" reads Tenet 2's minimality as a tuned magnitude; tenets L69 makes it empirical-constraint minimality, and sibling `voids/amplification-void.md` L61 says the question "does no work". A cross-article adjudication row is warranted.

## Priority list (capped at 4)

| # | Locus | Tenet | Why this one |
|---|---|---|---|
| 1 | **Re-mint check 140's four priority rows verbatim** (`born-rule` L110+L219; `brain-internal-born-rule-testing` L157+L143/L153/L155; Tenet-1 fabrication sweep `kabbalah` L34/L78/L84, `collective-phenomena` L162, `combination-problem` L175; `testing-consciousness-collapse` L179+L203+L215) | 1/2/3 | Six ERRORs, two reports old, zero tasks. The briefs are already written in check 140 §Priority list and need only copying |
| 2 | **Fabricated-tenet-prediction sweep**: `falsification-roadmap` L173+L107+L93, `phenomenology-of-returning-attention` L97+L39, `apex/consciousness-and-agency` L120, `haecceity` L181, `composition-and-consciousness` L111 | 1/2/3/4 | Five ERRORs of one class. The brief should say "grep the file for every sentence in which a tenet, by name, *predicts*, *requires*, *implies*, *establishes* or *rejects* something, and check each against `tenets.md`". Candidate boundary for a corpus sweep (20 files, not all defects): `brain-internal-born-rule-testing` L3, `microphenomenological-interview-method` L127, `concession-convergence-philosophy-of-mathematics` L118, `phenomenology-of-linguistic-failure` L113, `invertebrate-consciousness-as-interface-test` L135, `concepts/concession-convergence` L153, `content-specificity-of-mental-causation` L73, `jourdain-hypothesis` L129, `consciousness-and-scientific-explanation` L58, `tenet-falsification-conditions` L34, `apex/ai-as-introspection-control` L142, `apex/minds-without-words` L157, `apex/phenomenal-variation-within-a-species` L161, `voids/imagery-void` L122, `voids/what-voids-reveal` L116, `voids/mood-void` L126 |
| 3 | **Tenet 3 relocated in the quantum wing**: `indexical-identity-quantum-measurement` L147+L161, `many-minds-interpretation` L86, `quantum-consciousness` L114 (+L52, L172), with the `many-worlds` L186 wording sibling | 2/3/4 | Three ERRORs that put the Map's mechanism somewhere `tenets.md` L91 says it is not. `quantum-consciousness` is linked from `tenets.md` itself; `indexical-identity` is the article a reader reaches for the indexical objection |
| 4 | **Carried below the cap for a third report**: `concepts/dualism` L172/L154 (check-139 priority 4), `causal-closure` L120/L196/L198/L172/L136, `quantum-holism-and-phenomenal-unity` L176, `panpsychism` L186, `apex/interface-specification-programme` L66/L132 | 1/2/3/5 | Each has been re-verified live in three consecutive reports. `concepts/dualism` is the concept page Tenet 1 links for the positive arguments |

**Recommendation to the driver:** mint one `refine-draft` per priority row (row 1 is four tasks, copied from check 140). Each brief should name the *claim*, require a same-file sibling grep before closing, and require the Hugo copy to be checked. This check did not mint, per the skill's reports-only scope.

## Warnings

Every quote below was grep-verified by the sub-sweep that read the file (one hit at the stated line). I independently re-verified the ERRORs, the borderline items, §Summary 2 and the carried loci. Line numbers are as of 2026-09-28 12:10 UTC.

### Family S: Tenet 3 held as actual, or epiphenomenalism reported refuted (tenets L93, L95 `^tenet-3-standing`, L101–103)
- `apex/attention-as-causal-bridge.md` L52 (lead) "the effort of sustaining it reveals genuine causal work"; L80 "among the strongest phenomenological evidence for consciousness doing real causal work"; L140 "exemplify bidirectional interaction within a single event"; L172 (synthesis). All against its own L90 "left open, a debt Tenet 3 records".
- `apex/consciousness-and-agency.md` L110 "would be coincidental if phenomenology had no functional role" (epiphenomenalism predicts the correlation; `attentional-economics` L182 concedes it); L114 "Together these answer the rollback" (against its own L112); L134 argument from reason as failsafe.
- `apex/phenomenology-mechanism-bridge.md` L132 "consistent with — and predicted by — consciousness doing causal work" (against its own L75); L144; L176 "each fail at the level where they claim explanatory power".
- `apex/born-preserving-causal-efficacy.md` L191 ✔ "secures that *something* must select" (carried).
- `apex/interface-specification-programme.md` L72 ✔, L173 ✔ (carried).
- `concepts/agent-causation.md` L145 "if phenomenology were epiphenomenal the correlation would be coincidental" (new); L121 ✔, L127 ✔, L147 ✔, L151 ✔ (carried); L178 causal powers "by its nature" as a substance.
- `concepts/attentional-economics.md` L50 "How you spend your attentional budget determines which neural patterns actualise" ("This isn't metaphor"); L87 "This felt effort corresponds to genuine work"; L103 (against its own L182).
- `concepts/attention-as-interface.md` L153 "What holds neural patterns stable is the conscious act of attending" (against its own L161).
- `concepts/consciousness-selecting-neural-patterns.md` L62 "supplies first-person evidence for this mechanism" (tenets L93 verification circularity); L124 "Selection has measurable effects" (Schwartz PET); L146 "The mechanism specifies *how* bidirectional interaction works" (against its own L172, P-Q10); L162 ✔ (carried from 138).
- `concepts/libet-experiments.md` L3 (the description) "Consciousness retains genuine causal power over action" (against its own L195).
- `concepts/multi-mind-collapse-problem.md` L153 "The alternative (epiphenomenalism) makes consciousness do nothing at all" (physicalist mental causation erased); L181 "consciousness's quantum influence, while real, is local".
- `concepts/neuroplasticity.md` L144 "provides empirical support for several" tenets (against its own L146 and L36).
- `concepts/retrocausality.md` L127 "Retrocausality vindicates this—the selection *is* genuine" (against its own L79).
- `concepts/witness-consciousness.md` L184 "the effortful mode involves genuine causal intervention" (against its own L109/L196).
- `topics/authentic-vs-inauthentic-choice.md` L33 (lead) "authentic choice engages consciousness's genuine selection function" (against its own L132 "speculative", L138); L134, L186, L196.
- `topics/completeness-in-physics-under-dualism.md` L128 "invisible to structural physics but causally real"; L126.
- `topics/consciousness-and-mathematics.md` L190 "If understanding has essential phenomenal character, consciousness causally influences behaviour" (the inference epiphenomenalism denies).
- `topics/consciousness-and-probability-interpretation.md` L125 ✔ (carried).
- `topics/consciousness-and-the-ontology-of-temporal-becoming.md` L165 "The growing block makes causal efficacy genuine rather than perspectival" (against its own L103).
- `topics/empirical-evidence-for-consciousness-selecting.md` L42 (lead, partial repair: "over no-collapse physicalism" still against its own L139); L134 ✔, L141 ✔ (carried).
- `topics/free-will.md` L66 ✔ (lead, carried); L149 ✔ (carried, was L147); L141 "which physical causation alone cannot instantiate" (new; against its own L143). **Repaired:** L100 is now a bare Rajan citation; L110 now adds "a physically realised control process predicts it equally".
- `topics/motor-control-quantum-zeno.md` L127 ✔ (carried).
- `topics/phenomenology-of-agency-vs-passivity.md` L135 ✔ (carried).
- `topics/phenomenology-of-returning-attention.md` L39 (lead) "predicts exactly this structure" (ERROR-3 sibling); L144.
- `topics/quantum-measurement-and-subjective-probability.md` L124 "must involve real causal flow from mind to matter"; L130 "so the connection is genuinely causal"; L154.
- `topics/structure-of-attention.md` L195 "Willed attention is where consciousness adds something" (against its own L199); L221; L249.
- `topics/temporal-consciousness-structure-and-agency.md` L251 "it determines how long selection is sustained".
- `topics/the-interface-problem.md` L63 "The Map can say *that* consciousness acts on matter" (against its own L67 "framework-supplied").
- `topics/trilemma-of-selection.md` L76 "The felt cost corresponds to genuine causal engagement" (against its own L113); L54 common-cause strawman (against its own L78); L127 "derives the need for consciousness to bias outcomes" (against its own L117); L129 exhaustiveness (against its own L87).
- `topics/volitional-control.md` L154 tenets "predict the pattern the evidence reveals" (against its own L118).
- `topics/eastern-philosophy-consciousness.md` L127 "Dream yoga exemplifies Bidirectional Interaction" (L193 later withdraws the support).
- `voids/emergence-void.md` L108 "we can affirm it on the basis of evidence"; `voids/origin-of-consciousness.md` L156 "makes consciousness causally efficacious—it does something"; `voids/tenet-generated-voids.md` L145 "is required by our ability to discuss consciousness at all" and "the aggregate-level silence of something causally real".

### Family I: felt definiteness cited against MWI (tenets L117 scoping, L172 "predict definite qualia within each branch", posit 3)
- `apex/attention-as-causal-bridge.md` L186 "has no causal explanation if all options are equally actualised".
- `apex/phenomenology-mechanism-bridge.md` L174 "fits singular actualisation more naturally than branching".
- `concepts/self-and-self-consciousness.md` L192 "proliferation of subjects undermines the determinacy self-consciousness presupposes".
- `concepts/stapp-quantum-mind.md` L164 "This phenomenology creates tension with MWI, supporting collapse interpretations" (same paragraph concedes MWI predicts singular-feeling experience).
- `concepts/witness-consciousness.md` L158 "the felt singularity counts against interpretations"; L188.
- `concepts/quantum-consciousness.md` L60 "The core objection: MWI makes consciousness epiphenomenal" (tenets L117: the indexical objection carries the weight).
- `topics/authentic-vs-inauthentic-choice.md` L200 "dissolving the weight that authentic choice carries".
- `topics/many-minds-interpretation.md` L88 "the felt singularity of being *this* observer… as evidence for a haecceitistic fact" (`quantum-immortality` L78 has the calibrated form).
- `topics/phenomenology-of-returning-attention.md` L146 "coheres better with a framework where selection is ontologically singular".
- `topics/quantum-measurement-and-consciousness.md` L128 "is not credence but actualisation" and "is eliminated independently of whether probability is rescued".
- `topics/quantum-neural-timing-constraints.md` L174 "becomes meaningless—every possibility is actual somewhere".
- `topics/temporal-consciousness-structure-and-agency.md` L212 "carries a phenomenal texture that branching leaves unexplained"; L255.
- `voids/tenet-generated-voids.md` L147 "what cannot branch cannot split across worlds" (against its own L89).
- **Quick "nothing to select" sub-class** (branch-relative selection not flagged; the 09-28 `agent-teleology`/`meaning-void` repairs are the model): `concepts/attentional-economics.md` L196; `concepts/brain-interface-boundary.md` L170; `concepts/neuroplasticity.md` L152; `concepts/consciousness-selecting-neural-patterns.md` L152; `concepts/motor-selection.md` L210; `topics/empirical-evidence-for-consciousness-selecting.md` L169; `topics/the-interface-problem.md` L161; `topics/quantum-measurement-and-consciousness.md` L178; `topics/dopamine-and-the-unified-interface.md` L211; `concepts/attention-as-interface.md` L216 (against its own L232).

### Tenet 5: parsimony used as a verdict, or Tenet 5 misgrounded (tenets L145, L147, L69)
- `concepts/attentional-economics.md` L198 "explains what simpler accounts cannot".
- `concepts/causal-closure.md` L136 ✔ (carried).
- `concepts/causal-consistency-constraint.md` L73 "rests on conservatism (the fifth tenet plus MQI)" (Tenet 5 licenses no preference; tenets L69).
- `concepts/teleosemantics.md` L92 Tenet 5 cited as "the limits of reduction".
- `concepts/naturally-occluded.md` L143 ✔ (carried); `voids/biological-cognitive-closure.md` L135 "receives the strongest support" (Tenet 5 grounded in FBT, same class).
- `topics/empirical-evidence-for-consciousness-selecting.md` L151 ✔ (carried).
- `topics/evolution-under-dualism.md` L169 "purchases explanatory resources the physicalist account lacks".
- `topics/motor-control-quantum-zeno.md` L131 ✔ (carried).
- `topics/quantum-measurement-and-consciousness.md` L180 "names the phenomenon without explaining it" (random baseline collapse is the Map's own posit, tenets L125).
- `topics/structure-of-attention.md` L233 strawman "simplest account".
- `voids/tenet-generated-voids.md` L77 (borderline, above).
- Out of window: `concepts/geometric-model-of-mind.md` L113 (last commit 2026-07-27) "the Map because parsimony favours the smallest non-physical influence consistent with the tenets".

### Tenet 2: coherence dependence, dilution, statistics-modulation and mechanism overclaims (tenets L71, L75, L77, L85)
- Coherence closure as falsifier: `concepts/consciousness-selecting-neural-patterns.md` L166 "experiments definitively show no quantum effects survive in neural tissue" and L170; `concepts/quantum-consciousness.md` L172 "Definitive closure of neural quantum coherence"; `topics/evolution-under-dualism.md` L155 "the specific mechanism the Map proposes… would fail"; `topics/authentic-vs-inauthentic-choice.md` L214 "the decoherence objection proved decisive"; `concepts/agent-causation.md` L160 ✔ (carried); `topics/the-interface-problem.md` L147; `topics/attention-and-the-consciousness-interface.md` L153 "empirical viability presently rides on the short-coherence integrationist response"; `topics/consciousness-and-mathematics.md` L194.
- Dilution or sensitivity framing: `concepts/causal-closure.md` L120 ✔, L196 ✔, L198 ✔ (carried); `topics/falsification-roadmap-for-the-interface-model.md` L107 (ERROR-2 sibling), L93.
- Statistics modulation: `concepts/many-worlds.md` L186; `concepts/quantum-consciousness.md` L52; `concepts/multi-mind-collapse-problem.md` L129 (borderline, above); `concepts/quantum-probability-consciousness.md` L176 "Born probabilities describe the selection probabilities at consciousness-quantum coupling" (against its own L118).
- Mechanism stated as fact: `concepts/multi-mind-collapse-problem.md` L107 (Zeno; against its own L80); `concepts/causal-closure.md` L150; `topics/structure-of-attention.md` L229; `topics/quantum-neural-timing-constraints.md` L170; `topics/time-symmetric-selection-mechanism.md` L139.
- Corridor boundary: `topics/mathematical-structure-of-the-consciousness-physics-interface.md` L89, L92, L154 (borderline, above); `topics/falsification-roadmap` L95.
- Precedent over-read: `topics/empirical-evidence-for-consciousness-selecting.md` L92 "This objection has collapsed" (against its own L104 and tenets L79); L149 ✔, L153 ✔ (carried, reworded: "removes the mechanism's necessary precondition", "the substrate… disappears"); `concepts/agent-causation.md` L111 ✔ (carried).
- `apex/born-preserving-causal-efficacy.md` L71 ✔ (carried); `concepts/ensemble-level-epiphenomenalism.md` L37 ✔ (carried), L61 (Maier residue, §Summary 2).
- `topics/many-minds-interpretation.md` L84 "MMI is striking evidence for the *plausibility* of Tenet 1" (non-supervenience follows from Albert–Loewer's own premise).
- `topics/quantum-measurement-and-consciousness.md` L174 "transforms this from an isolated hypothesis into a prediction" (against its own L82 "circularity").

### Alignment, lead or body claims more than the argument supports (Tenet 1 and other)
- "Establishes" class (tenets L47 "not proven"): `apex/interface-specification-programme.md` L66 ✔, L132 ✔ (carried); `voids/interface-formalization-void.md` L119 "establishes that consciousness is not reducible"; `voids/origin-of-consciousness.md` L150 "The irreducibility established by dualism"; `voids/tenet-generated-voids.md` L55 "Dualism establishes that consciousness cannot be fully explained".
- Fundamentality attributed to Tenet 1 (ERROR-1 class, softer): `voids/tenet-generated-voids.md` L109, L135, L151; `voids/temporal-void.md` L60, L146; `topics/eastern-philosophy-consciousness.md` L71 "Advaita takes consciousness as fundamental… aligning with the Dualism tenet".
- Tenet 3 made to require a subject/bearer (check-140 `unity-of-consciousness` L144 class, still live there): `concepts/self-and-self-consciousness.md` L134 "requires a subject whose influence on physical outcomes is real"; `concepts/agent-teleology.md` L122 "is, in effect, a commitment to agent teleology".
- Illusionism or physicalism reported refuted: `concepts/libet-experiments.md` L141 "The illusionist cannot coherently claim to have *reasoned* to their position"; `concepts/quantum-indeterminacy-free-will.md` L162 "The position is self-undermining"; `concepts/reasons-responsiveness.md` L82 "self-stultifying for physicalism", L126; `concepts/agent-teleology.md` L63 "for the same reasons physicalism fails generally"; `topics/phenomenology-of-agency-vs-passivity.md` L143; `apex/phenomenology-mechanism-bridge.md` L176.
- Trilemma treated as exhaustive (missed by 3437ce4bb8): `concepts/reasons-responsiveness.md` L50 "and only the third preserves authorship"; `topics/authentic-vs-inauthentic-choice.md` L130; `topics/born-rule-and-the-consciousness-interface.md` L219; `topics/trilemma-of-selection.md` L129; `concepts/causal-closure.md` L172 ✔ (carried).
- Alignment sections overclaiming against the body: `topics/completeness-in-physics-under-dualism.md` L124 "the positive case for dualism from physics itself" (against its own L70); `topics/quantum-measurement-and-subjective-probability.md` L150 "supports dualism" (against its own L37); `topics/quantum-measurement-and-consciousness.md` L146 "the cumulative case exceeds any individual argument" (against its own L82); `topics/attention-and-the-consciousness-interface.md` L169, L173; `topics/memory-channel-interface-evidence.md` L154 "a substrate-only picture cannot" (against its own L136); `topics/structure-of-attention.md` L217; `concepts/motor-selection.md` L198; `concepts/reasons-responsiveness.md` L120 "reflects ontological irreducibility" (against its own L44); `concepts/composition-and-consciousness.md` L75 ✔, L83 ✔, L127 ✔ (carried).

### Carried and still live (no commit since the flagging report, so live by construction; each file's last commit predates check 140)
- **From check 139, unminted:** `concepts/dualism` L172, L154, L130, L180; `concepts/neural-correlates-of-consciousness` L160; `topics/cross-cultural-phenomenology-of-agency` L47; `topics/pain-consciousness-and-causal-power` L174; `topics/dream-consciousness` L217, L223; `topics/ethics-of-consciousness-invertebrate-question` L53.
- **From check 138:** `concepts/self-stultification` L197; `topics/ai-consciousness` L145; `topics/amplification-mechanisms-consciousness-physics` L181; `concepts/attention-schema-theory` L209; `concepts/categorical-surprise` L113; `concepts/universal-coupling-response` L92; `topics/constitutive-exclusion` L120; `concepts/timing-gap-problem` L95; `apex/competency-without-felt-experience` L129; `concepts/methodological-pluralism` L119; `topics/basal-and-bioelectric-cognition` L95.
- **From check 137:** `topics/the-binding-problem` L176; `arguments/materialism-argument` L140; `concepts/conscious-vs-unconscious-processing` L48; `voids/conceptual-impossibility` L143.
- **From check 140 (files not committed this window):** every locus in check 140 §Warnings for `phenomenology-of-consciousness-doing-work`, `post-decoherence-selection-programme` L171, `pharmacological-dissociation-as-evidence` L142, `mental-effort` L72/L94/L134, `problem-of-other-minds` L126/L196/L202, `russellian-monism` L43/L97/L101/L141, `emergence-as-universal-hard-problem` L111/L113, `consciousness-and-the-metaphysics-of-laws-and-dispositions`, `delegatory-dualism` L240, `delegatory-causation` L51/L132/L136/L150/L206, `spontaneous-intentional-action` L132/L136, `mind-brain-separation` L112/L118, `post-decoherence-selection` L104, `consciousness-in-smeared-quantum-states` L46/L100, `consciousness-and-testimony` L131/L145, `surprise-prediction-error-and-consciousness` L133/L141/L195/L199, `bi-aspectual-ontology` L37/L139, `consciousness-and-collective-phenomena` L52/L74/L154, `implicit-memory` L3/L41/L191–193, `phenomenal-transparency-opacity-spectrum` L121, `phenomenology-of-choice-and-volition` L3/L56/L145/L165, `philosophy-of-habit-under-dualism` L83/L87, `phenomenal-depth` L86, `voids-between-minds` L144, `confabulation-void` L104, `consciousness-and-social-understanding` L161, `animal-consciousness` L190, `embodied-consciousness` L194/L196, `consciousness-as-activity` L132, `llm-consciousness` L56/L100/L114/L165, `measurement-problem` L67/L117/L187/L197, `terminal-lucidity-and-filter-transmission-theory` L86/L152/L177, `combination-problem` L185/L187, `entanglement-binding-hypothesis` L76/L102–106/L122, `testing-consciousness-collapse` L159, `sorkin-delta-brain-internal-analogues` L37, `panpsychism` L55/L134/L142/L186/L188, `russellian-monism-versus-bi-aspectual-dualism` L46/L140, `illusionism` L3, `functional-seeming` L93, `unity-of-consciousness` L144, `frankfurt-hierarchical-mesh-theory-of-the-will` L88, `brain-internal-born-rule-testing` L153.
- **Carried loci in files committed this window, re-probed by string and still live:** `apex/born-preserving-causal-efficacy` L71, L191; `apex/interface-specification-programme` L66, L72, L132, L173; `concepts/agent-causation` L121, L127, L147, L151, L160; `concepts/causal-closure` L120, L136, L172, L196, L198; `concepts/composition-and-consciousness` L75, L83, L127; `concepts/consciousness-selecting-neural-patterns` L162; `concepts/ensemble-level-epiphenomenalism` L37; `concepts/naturally-occluded` L143; `concepts/attention-as-interface` L234; `topics/free-will` L66, L149; `topics/empirical-evidence-for-consciousness-selecting` L134, L141, L149, L151, L153; `topics/motor-control-quantum-zeno` L127, L131; `topics/phenomenology-of-agency-vs-passivity` L135; `topics/consciousness-and-probability-interpretation` L93, L125; `topics/born-rule-and-the-consciousness-interface` L219; `topics/overdetermination-dissolution-under-selection-only-interactionism` L93; `topics/quantum-neural-timing-constraints` L126; `topics/volitional-control` L156; `voids/interface-formalization-void` L123; `topics/introspection-architecture-independence-scoring` L191.
- **Repaired this window:** `topics/free-will` L100 and L110; `concepts/causal-closure` L144/L146 (Maier now external); `concepts/brain-interface-boundary` L124 (trumping exception); `topics/neural-refresh-rates-and-the-smoothness-problem` L120; `concepts/panprotopsychism` L74 (now followed by a calibration sentence); `topics/born-rule-and-the-consciousness-interface` L209 (Maier external); `topics/parapsychology-firewall` L51; `apex/self-concealing-interface` L135; `apex/research-programme-decisions-under-the-map` L124.

## Notes

- `topics/born-rule-and-the-consciousness-interface.md` L221 "the Map regards as decisive" (carried; tenets L117 scopes "decisive" to branch-egalitarian readings). L170: the Chalmers-McQueen row now says Born-preserving (601e49b435) but still sits under the L167 heading "Minimum-outside-the-corridor dualism (Born-rule-bending)"; L207 also calls it Born-compliant.
- `positions/quantum-interface.md` L55: P-Q1 makes conscious selection "the effective reduction to a single actual branch" where tenets L125 and `background-commitments` L42 have objective reduction supply baseline definiteness. Same class as check 140's note on `post-decoherence-selection-programme` L73/L93/L167. The rest of the register is consistent with tenets L49–147; the Maier correction landed at L78, L84, L152.
- `tenets/background-commitments.md` passes; L60 carries the Maier correction.
- `concepts/stapp-quantum-mind.md` L66 still classifies Stapp as "Born-rule-bending" (a9c67c3027 fixed the sibling in `quantum-measurement-and-consciousness` L136 only); L104, L120, L156.
- `concepts/haecceity.md` L99, L201 (Further-Reading label "Why indexical identity problems doom many-worlds" overclaims against its own L171).
- `concepts/many-worlds.md` L57 "Before measurement, there is one you" is the sentence the new `diverging-worlds-everettianism` L52 says is false on divergence; L63 (Family I in the body, calibrated at L88).
- `concepts/quantum-consciousness.md` L186 "The quantum opening provides the mechanism" (P-Q10); L192 "strong emergentism that specifies its mechanism" fixes an ontology tenets L53 leaves neutral.
- `concepts/quantum-probability-consciousness.md` L114, L156, L166 (over-concedes the conditioned register, P-Q3; same class as `measurement-problem` L63).
- `concepts/quantum-indeterminacy-free-will.md` L122 mental causation imported into the zombie construct (the `phenomenal-depth` L86 class).
- Bare "an illusion must appear to something" regress presented as a reply (`illusionism` L91: "proves nothing"): `concepts/retrocausality` L121; `apex/attention-as-causal-bridge` L84; `concepts/attention-as-interface` L204; `concepts/brain-interface-boundary` L128; `concepts/motor-selection` L188; `concepts/quantum-probability-consciousness` L156.
- Argument from reason stated flat as delivering Tenet 3: `concepts/agent-teleology` L67; `apex/phenomenology-mechanism-bridge` L144; `concepts/causal-closure` L168 ✔; `topics/falsification-roadmap` L111; `topics/clinical-evidence-quality-standards-consciousness-research` L140.
- Global exclusion asserted without the posit marker (`background-commitments` L46–50): `topics/consciousness-and-mathematics` L196; `topics/consciousness-and-the-ontology-of-temporal-becoming` L167; `topics/motor-control-quantum-zeno` L129 ✔; `topics/dopamine-and-the-unified-interface` L211.
- `topics/completeness-in-physics-under-dualism.md` L72, L116; `topics/consciousness-and-mathematics.md` L88, L110; `topics/consciousness-and-probability-interpretation.md` L89, L146; `topics/consciousness-and-the-ontology-of-temporal-becoming.md` L163; `topics/dopamine-and-the-unified-interface.md` L31, L176.
- `topics/eastern-philosophy-consciousness.md` L191; `topics/empirical-evidence-for-consciousness-selecting.md` L155; `topics/evolution-under-dualism.md` L165; `topics/falsification-roadmap` L125 (lists ontological profligacy as a co-motivation for Tenet 4; tenets L119 demotes it); `topics/hoel-llm-consciousness-continual-learning.md` L104; `topics/indexical-identity-quantum-measurement.md` L163; `topics/many-minds-interpretation.md` L98; `topics/memory-channel-interface-evidence.md` L118; `topics/phenomenology-of-agency-vs-passivity.md` L125, L165; `topics/phenomenology-of-returning-attention.md` L111; `topics/quantum-biology-and-neural-consciousness.md` L53.
- `topics/quantum-measurement-and-consciousness.md` L166; `topics/quantum-measurement-and-subjective-probability.md` L122 (Tenet 2 "rejects" QBism); `topics/structure-of-attention.md` L98; `topics/temporal-consciousness-structure-and-agency.md` L70, L160, L249; `topics/the-interface-problem.md` L159, L161 (Tenet 5 "counsels patience"); `topics/time-symmetric-selection-mechanism.md` L39 (tenets "require a mechanism"; they commit to the *that*); `topics/trilemma-of-selection.md` L99, L113.
- `voids/biological-cognitive-closure.md` L143 misstates MWI (closure is permanent branch-locally); `voids/interface-formalization-void.md` L67; `voids/temporal-void.md` L72, L154. `voids/tenet-generated-voids.md` derivability check: Nature (T1), Mechanism (T2), Selection (T4), Meta (T5) and Detection (T3 plus corridor) voids all derive from the tenet text; only the L77 fine-tuning gloss does not.
- `concepts/self-and-self-consciousness.md` L194; `concepts/witness-consciousness.md` L136, L180; `concepts/agent-causation.md` L109 ✔ (carried); `apex/self-concealing-interface.md` L103; `concepts/collapse-and-time.md` L87 (corrected by its own L89).
- **Carried:** tenets.md L159 still points at `[[apex/machine-question]] §senses of conscious`. Not re-probed this window.

## Files passing all checks (25)

- `apex/mereology-of-mind.md`
- `apex/research-programme-decisions-under-the-map.md`
- `apex/steelmanning-as-method.md`
- `concepts/buddhism-and-dualism.md`
- `concepts/consciousness-physics-interface-formalism.md`
- `concepts/direction-of-interface-change.md`
- `concepts/diverging-worlds-everettianism.md` (new)
- `concepts/egocentric-presentism.md`
- `concepts/fitness-beats-truth.md`
- `concepts/pudgalavada.md` (new)
- `concepts/quantum-completeness.md`
- `tenets/background-commitments.md`
- `topics/buddhist-perspectives-on-meaning.md`
- `topics/chemosensory-consciousness-and-the-interface.md`
- `topics/consciousness-and-the-metaphysics-of-composition.md`
- `topics/direction-dependent-discriminating-test-design.md`
- `topics/neural-refresh-rates-and-the-smoothness-problem.md`
- `topics/paradoxical-kinesia.md` (new)
- `topics/parapsychology-firewall.md`
- `topics/quantum-immortality-and-the-quantum-suicide-survival-argument.md`
- `topics/sham-controlled-neurofeedback-and-the-consciousness-comparator.md`
- `topics/time-bias-and-thank-goodness-thats-over.md` (new)
- `voids/amplification-void.md`
- `voids/meaning-void.md`
- `voids/void-as-ground-of-meaning.md`

`tenets/tenets.md` was read in full and is internally consistent; its one commit this window (e3e689517d) is correct.

## Method

1. Read `tenets.md` in full and diffed it against the check-140 baseline. Only the Maier clause changed.
2. Listed every file in `topics/ concepts/ positions/ apex/ voids/ tenets/` with a commit since 2026-09-27 06:25 UTC (101 files, 4 new). Five parallel sub-sweeps read each file in full and reported loci in a fixed format with an exact quote each; every quote was grep-verified by the sub-sweep at the stated line.
3. I independently re-verified all 14 ERRORs and the borderline items by exact string with context, checked whether each new ERROR string was present at the check-140 baseline (all were), and re-probed every carried locus from checks 137–140 by exact string or by the file's last-commit date.
4. Corpus-wide sweeps (all sections, not only the changed set) for the Maier residue, the fabricated-prediction attribution forms, the "nothing to select" class, the "establishes" class and the parsimony-verdict forms; the counts are in §Summary and Priority 2.
5. No content file was modified. No task was minted.

## Scope confirmation

All 101 files with a commit since check 140 were read in full; none was skipped or sampled. Files outside the window were probed by exact string only, and are reported as carried (live by construction, no commit) or as out-of-window grep hits, never as fresh reads.
