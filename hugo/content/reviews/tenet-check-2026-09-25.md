---
ai_contribution: 100
ai_generated_date: 2026-09-25
ai_modified: 2026-09-25 09:30:00+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-09-25
date: &id001 2026-09-25
description: 'Tenet check 139: check 138''s priority list was fully repaired within
  hours. A delta sweep of 85 edited files finds partial repairs leaving stronger sibling
  claims live.'
draft: false
human_modified: 2026-09-25
last_curated: null
last_deep_review: null
lastmod: 2026-09-25 09:30:00+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-09-25
topics: []
---

# Tenet Alignment Check

**Date**: 2026-09-25 (check 139; previous [reviews/tenet-check-2026-09-23.md](/reviews/tenet-check-2026-09-23/) = 138)
**Files checked**: 85 articles read in full. This is every live file in `topics/ concepts/ positions/ apex/ voids/ arguments/` with a commit since check 138 (2026-09-23 23:55 UTC), five of them new. `tenets.md` was also read in full (unchanged since check 138). Separately, 42 carried loci from checks 137 and 138 were probed for repair.
**Errors**: 2. One is new (introduced by a repair commit on 2026-09-24). One is carried from check 138. A third locus belongs to an already-booked family and is not counted again.
**Warnings**: about 100 new loci across 50 files, plus 25 carried WARNING loci that are still live.
**Notes**: about 45 new
**Lens**: the same as check 138. Direct conflicts, plus the structural question: does the alignment section, lead or Occam paragraph claim more than the article's own body (or the reverse)?

## Summary

**1. Check 138's priority list was repaired quickly. Minting worked.** All four priority rows were fixed between 00:16 and 01:47 UTC on 2026-09-24, two to three hours after the report: `unity-of-consciousness` (7f66c398), `presentiment-and-retrocausality` (2e4c8e57), `cross-cultural-phenomenology-of-agency` L99 (e996c619) and `neural-correlates-of-consciousness` L160 (e4e9e6e0). Four of the five items carried below the cap were fixed as well: `dualism` (Levine), `filter-theory` ([P-CS6](/positions/consciousness-scope/#p-cs6)), both `architectural-adequacy` loci, and IIT L150. So were `functionalism-argument` L199 and, from check 137's carry list, `consciousness-as-activity` (supervenience) and `terminal-lucidity` L175. All eight are verified gone (0 hits, each file committed since). Check 138 said that a reports-only priority list gets actioned only if someone mints tasks from it. This cycle confirms it: once minted, the items were fixed.

**2. What did not get minted did not move.** Every one of the 18 check-138 WARNING loci in files with no commit since is still live, verbatim. So are 7 of check 137's 9 carried loci, and the `animal-consciousness` ERROR. `todo.md` L752 records that last one as "the only one unqueued".

**3. New dominant pattern: a partial repair leaves a stronger sibling claim live.** A refine fixes the sentence it was pointed at, and a sentence a few lines away that makes the same overclaim more strongly survives. Loci this window, all verified by me:
- [concepts/neural-correlates-of-consciousness.md](/concepts/neural-correlates-of-consciousness/) L160. The covert-consciousness sentence was fixed, but the same line still says "supporting the claim that conscious involvement at NCC sites is genuinely causal rather than epiphenomenal".
- [topics/cross-cultural-phenomenology-of-agency.md](/topics/cross-cultural-phenomenology-of-agency/). L99 was fixed, but the lead at L47 still says "The Unfinishable Map holds that consciousness genuinely causes physical outcomes", and the description says "consciousness as genuinely causal".
- [topics/terminal-lucidity-and-filter-transmission-theory.md](/topics/terminal-lucidity-and-filter-transmission-theory/). L175 was fixed, but L86 still says "That the filter model absorbs the phenomenon at lower cost is a point in its favour on parsimony grounds". L173 and L177 also overclaim, against L118 and L158.
- [topics/pain-consciousness-and-causal-power.md](/topics/pain-consciousness-and-causal-power/). L160 had "simpler" removed, but L174 still says "and the simplest may be that the suffering itself was selected for" (Tenet 5 used as a verdict in the Map's favour).
- [topics/dream-consciousness.md](/topics/dream-consciousness/). L215 was fixed, but L217 still says "Lucid dreaming provides direct evidence". L223 also claims more than L96.
- [concepts/dualism.md](/concepts/dualism/). The Levine sentence was fixed, but L172 says "explanatory parsimony favours dualism", against tenets L145 "parsimony cannot decide for or against a framework". L154 says "The Map rejects this because it is self-undermining", against tenets L101.
- [topics/quantum-holism-and-phenomenal-unity.md](/topics/quantum-holism-and-phenomenal-unity/). Three refines on 09-25 rewrote the body, but the alignment section at L184 still says "The structural mismatch between physical relations and phenomenal unity supports dualism." L188 states downward efficacy flat. An open P1 in `todo.md` (the Leibniz concession not carried into the lead and alignment) already covers this, so nothing new is owed here.

**The implication for drivers:** a refine brief should name the *claim*, not the sentence, and should ask the executor to grep the file for sibling statements of the same claim before closing.

**4. A repair installed a new ERROR.** [topics/consciousness-as-activity.md](/topics/consciousness-as-activity/) L85 was introduced by 1524a5a7 (2026-09-24 22:49). It says "the [agent-causal selection](/concepts/agent-causation/) the Bidirectional Interaction tenet requires needs a selector that persists across its selections". `tenets.md` L91 commits the tenet only to "*outcome-selection*". L184 says the substance commitment is "downstream of [agent causation](/concepts/agent-causation/), not the tenet". This is fabricated tenet content, the same class as check 138's unity-of-consciousness ERROR.

**5. The families from check 138 persist in fresh material:**
- **Family I (Tenet 4 inheritance): about 20 new loci.** The felt singularity of choice or experience is cited against MWI, even though tenets L172 concedes that branch-relative accounts "predict definite qualia within each branch". Several of these loci sit in rows the matrix marks *Not invoked*.
- **Family S (Tenet 3 held as actual): about 40 loci.**
- **Tenet 5 used as a verdict in the Map's favour: about 12 loci.**
- **Tenet 2 overclaims:** a new sub-pattern, described below.

No file endorses, in Map voice, physicalism, illusionism, epiphenomenalism, MWI, psi or energy injection.

## Errors

### New
- [topics/consciousness-as-activity.md](/topics/consciousness-as-activity/) L85 (Tenet 3, fabricated tenet content). Quote and contradiction are in §Summary 4. It was introduced by this window's refine. **Fix:** "the agent-causal reading the Map's agency cluster adopts needs a selector that persists…".

### Carried from check 138, still live and unqueued
- [topics/animal-consciousness.md](/topics/animal-consciousness/) L192 "plausibility tilt rests on the [[evolutionary-case…" (Tenet 3 imported into a row the matrix marks *Not invoked*). There is no commit since check 137. This is now its third consecutive report.

### Booked family, not recounted
- [concepts/implicit-memory.md](/concepts/implicit-memory/) L196 "The simplest account that covers *all* the phenomena" is still live. It belongs to the blocked `NEEDS-HUMAN (doctrine) 2026-09-19` Tenet-5 tiebreaker item. The same holds for [topics/embodied-consciousness.md](/topics/embodied-consciousness/) L136.

### Borderline (counted as WARNING)
- [topics/ethics-of-consciousness-invertebrate-question.md](/topics/ethics-of-consciousness-invertebrate-question/) L53: "a claim the Map owes to [Tenet 1](/tenets/#dualism) and its resistance to ontic vagueness". `tenets.md` never mentions vagueness: `grep -noiF "vague"` returns 0, and a control grep for "Dualism" hits L49. The sentence is ambiguous: "its" can be read as referring to the Map rather than to Tenet 1. **Fix:** attribute the claim to the Map's metaphysics of subjects.

## Priority list (capped at 4)

| # | Locus | Tenet | Why this one |
|---|---|---|---|
| 1 | [topics/consciousness-as-activity.md](/topics/consciousness-as-activity/) L85 | 3 | New ERROR. Fabricated tenet content, installed by a repair. One-clause fix |
| 2 | [topics/animal-consciousness.md](/topics/animal-consciousness/) L192 | 3 | Carried ERROR. The only item from the 09-23 list that nobody minted |
| 3 | [concepts/causal-closure.md](/concepts/causal-closure/) L144 "its influence is lost in the statistical noise of vastly many unbiased quantum events" | 2 | Offers dilution as a Born-preservation route, which tenets L75 excludes: Born preservation holds "by construction, not by any sensitivity limit". The file's own L146 says the same. It survives inside a hunk this window edited. The same file carries L198 "if quantum coherence proves impossible at neural timescales" as a falsifier, which contradicts tenets L77 (post-decoherence proposals "do not depend on it"), and L136 "the Map's case against hidden variables rests on parsimony" |
| 4 | [concepts/dualism.md](/concepts/dualism/) L172 + L154 | 5 + 3 | The hub concept page gives a parsimony verdict for dualism and reports epiphenomenalism as refuted. Both contradict tenets.md text directly. Left standing by the 09-24 repair |

**Carried below the cap, so they are not lost:** the partial-repair siblings in §Summary 3 (NCC L160, cross-cultural L47, terminal-lucidity L86/L173/L177, pain L174, dream L217/L223). Each is a one-sentence edit in a file that was just repaired for the same claim. **If a driver mints, it should mint these as one refine per file,** with the brief "grep the file for every sibling of the repaired claim".

**Recommendation to the driver:** mint one `refine-draft` per priority row. As with check 138, those items were fixed within hours of being minted. This check did not mint, per the skill's reports-only scope.

## Warnings

The sub-sweeps grep-verified every quote with `grep -noF`, one hit at the stated line. I independently re-verified the ERRORs, the priority rows, §Summary 3, and the loci marked ✔. Line numbers are as of 2026-09-25 09:20 UTC.

### Family S: Tenet 3 held as actual, or epiphenomenalism reported refuted (tenets L93, L95 `^tenet-3-standing`, L101)
- [apex/post-decoherence-selection-programme.md](/apex/post-decoherence-selection-programme/) L171 ✔ "Post-decoherence selection is the mechanism by which consciousness causally influences the physical world". Contradicted by its own L93, which holds this as "a live hypothesis".
- [apex/interface-specification-programme.md](/apex/interface-specification-programme/) L72 "the quale carries causal weight the sensory signal alone does not"; L173 "architecturally necessary, not just philosophically asserted" (against L114).
- [apex/phenomenology-mechanism-bridge.md](/apex/phenomenology-mechanism-bridge/) L144: the argument from reason is listed as a "framework-independent" anchor, while L148 says "framework-internal only".
- [topics/pain-consciousness-and-causal-power.md](/topics/pain-consciousness-and-causal-power/) L64, L170 "Pain is the Map's clearest case of consciousness influencing the physical world", L176. The body concedes at L142 and L154.
- [topics/clinical-neuroplasticity-evidence-for-bidirectional-causation.md](/topics/clinical-neuroplasticity-evidence-for-bidirectional-causation/) L124 "as evidence that mental causation is not reducible" (against L104).
- [concepts/meditation-and-consciousness-modes.md](/concepts/meditation-and-consciousness-modes/) L46 "Effort does real work here". The phrase tenets L95 names.
- [concepts/neural-correlates-of-consciousness.md](/concepts/neural-correlates-of-consciousness/) L160 ✔ (§Summary 3).
- [topics/invertebrate-consciousness-as-interface-test.md](/topics/invertebrate-consciousness-as-interface-test/) L135 "tells against epiphenomenalism across phyla" (Animal row: *Not invoked*).
- [topics/predictive-processing-and-dualism.md](/topics/predictive-processing-and-dualism/) L152 "Active inference is the strongest empirical case for bidirectional causation in cognitive science"; L104.
- [concepts/stapp-quantum-mind.md](/concepts/stapp-quantum-mind/) L152 "consciousness determines which possibility actualises" (against its own L66); L164 "effort genuinely determines outcomes".
- [topics/consciousness-and-causal-powers.md](/topics/consciousness-and-causal-powers/) L180 "Consciousness continues to *do* cognitive work" (against L182); L130 "evidence for" (against L128).
- [arguments/functionalism-argument.md](/arguments/functionalism-argument/) L207 "Consciousness adds something—selection among quantum possibilities—that the functional story misses."
- [topics/phenomenology-of-anticipation.md](/topics/phenomenology-of-anticipation/) L119 "gains phenomenological support" (against L153 "consonant with Tenet 3 rather than demonstrating it").
- [concepts/retrocausality.md](/concepts/retrocausality/) L127 "Retrocausality vindicates this—the selection *is* genuine" (against L125, L79).
- [concepts/phenomenal-transparency-opacity-spectrum.md](/concepts/phenomenal-transparency-opacity-spectrum/) L121; [concepts/phenomenal-contrast-method.md](/concepts/phenomenal-contrast-method/) L116 "a marker of consciousness actively shaping action".
- [concepts/dualism.md](/concepts/dualism/) L154 ✔ (priority 4); [concepts/baseline-cognition.md](/concepts/baseline-cognition/) L57 "provides evidence against [epiphenomenalism](/concepts/epiphenomenalism/)", L148, and L202 "fails the systematic pattern".
- [topics/consciousness-in-simple-organisms.md](/topics/consciousness-in-simple-organisms/) L255 ✔ "If consciousness were epiphenomenal, its correlation with flexible learning would be inexplicable." (the Animal row marks interactionism *Not invoked*).
- [topics/dream-consciousness.md](/topics/dream-consciousness/) L217 ✔; `topics/terminal-lucidity…` L173.
- [concepts/prebiotic-collapse.md](/concepts/prebiotic-collapse/) L154 "modulating it in neural systems suffices for free will" (against L132).
- [concepts/witness-consciousness.md](/concepts/witness-consciousness/) L184 "the effortful mode involves genuine causal intervention" (against `phenomenal-conservatism` L98).
- [voids/consciousness-only-territories.md](/voids/consciousness-only-territories/) L102 "tenet holds that our discussing consciousness shows consciousness does something" (misstates tenets L93 "*suggests*").
- [topics/cross-cultural-phenomenology-of-agency.md](/topics/cross-cultural-phenomenology-of-agency/) L47 ✔ and the description.
- [topics/quantum-holism-and-phenomenal-unity.md](/topics/quantum-holism-and-phenomenal-unity/) L188 (already queued, P1).
- [topics/brain-computer-interfaces-and-the-interface-boundary.md](/topics/brain-computer-interfaces-and-the-interface-boundary/) L151 (against L121 "The prediction has not been tested directly").
- [concepts/causal-closure.md](/concepts/causal-closure/) L172 "the Map provides the *mechanism* Kane leaves underspecified" (against L142); L150.
- [topics/evolutionary-case-for-mental-causation.md](/topics/evolutionary-case-for-mental-causation/) L63, heading "## Why the Response Fails" (against L143 "without on its own refuting them").
- [topics/phenomenology-of-returning-attention.md](/topics/phenomenology-of-returning-attention/) L39 "predicts exactly this structure" (against L79).
- [concepts/entanglement-binding-hypothesis.md](/concepts/entanglement-binding-hypothesis/) L106 (flat selection claim, against L32 "contested").
- [concepts/neuroplasticity.md](/concepts/neuroplasticity/) L34 and L119 "attention is the bridge between conscious selection and physical change". The new `sham-controlled-neurofeedback` article (L61) cites this very claim as one the trials do not show.
- [concepts/phenomenal-depth.md](/concepts/phenomenal-depth/) L86 "The Map holds that depth is causally relevant" (qualia row: *Not invoked*).

### Family I: Tenet 4 inheritance (tenets L172: branch-relative accounts "predict definite qualia within each branch")
- [topics/quantum-hardware-and-the-ai-consciousness-coupling.md](/topics/quantum-hardware-and-the-ai-consciousness-coupling/) L93 ✔ "Reject Tenet 4 for many-worlds and the point dissolves". No-cloning holds in unitary QM, so it survives Everett; the machine row marks this *Not invoked*.
- [topics/invertebrate-consciousness-as-interface-test.md](/topics/invertebrate-consciousness-as-interface-test/) L137 and [topics/consciousness-in-simple-organisms.md](/topics/consciousness-in-simple-organisms/) L257: "this bee/worm fragments across branches" (Animal row: *Not invoked*).
- [topics/neurological-dissociations-as-interface-architecture.md](/topics/neurological-dissociations-as-interface-architecture/) L199; [topics/pain-consciousness-and-causal-power.md](/topics/pain-consciousness-and-causal-power/) L174 ("every supervenience mapping is realised somewhere"); [topics/consciousness-as-activity.md](/topics/consciousness-as-activity/) L132; [concepts/visual-consciousness.md](/concepts/visual-consciousness/) L124 (qualia row: *Not invoked*).
- [topics/predictive-processing-and-dualism.md](/topics/predictive-processing-and-dualism/) L154 "a singular perspective branching universes cannot ground" (the same line concedes the opposite); [concepts/predictive-processing.md](/concepts/predictive-processing/) L184 (prediction error "meaningless" under MWI).
- [concepts/stapp-quantum-mind.md](/concepts/stapp-quantum-mind/) L164; [arguments/functionalism-argument.md](/arguments/functionalism-argument/) L211; [topics/phenomenology-of-anticipation.md](/topics/phenomenology-of-anticipation/) L157; [concepts/baseline-cognition.md](/concepts/baseline-cognition/) L200; [concepts/witness-consciousness.md](/concepts/witness-consciousness/) L158 and L188.
- [apex/phenomenology-mechanism-bridge.md](/apex/phenomenology-mechanism-bridge/) L174 "fits singular actualisation more naturally than branching"; `topics/brain-computer-interfaces…` L149; [topics/phenomenology-of-returning-attention.md](/topics/phenomenology-of-returning-attention/) L146 (the same line concedes the Everettian reply).
- [concepts/entanglement-binding-hypothesis.md](/concepts/entanglement-binding-hypothesis/) L110 "Phenomenal unity appears indexically definite". This now contradicts the repaired sibling `quantum-holism` L190: "Synchronic unity within a decoherent branch is well defined under Everett".

**Note:** the correct concession already exists at [topics/dream-consciousness.md](/topics/dream-consciousness/) L221, [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/) L146 and `quantum-holism` L190. Every one of these loci could adopt that wording.

### Tenet 5: parsimony used as a verdict (tenets L145, L147)
- [concepts/dualism.md](/concepts/dualism/) L172 ✔ (priority 4).
- [topics/pain-consciousness-and-causal-power.md](/topics/pain-consciousness-and-causal-power/) L174 ✔.
- `topics/terminal-lucidity…` L86 ✔ and L177.
- [topics/consciousness-in-simple-organisms.md](/topics/consciousness-in-simple-organisms/) L255 ✔.
- [topics/dream-consciousness.md](/topics/dream-consciousness/) L223 "adds one postulate… but resolves".
- [concepts/filter-theory.md](/concepts/filter-theory/) L174 "strains the parsimony illusionism was supposed to provide".
- [concepts/causal-consistency-constraint.md](/concepts/causal-consistency-constraint/) L73 "rests on conservatism (the fifth tenet plus MQI)". Tenet 5 cannot ground a preference.
- [concepts/causal-closure.md](/concepts/causal-closure/) L136.
- [apex/phenomenology-mechanism-bridge.md](/apex/phenomenology-mechanism-bridge/) L176 "each fail" (against L79).
- [topics/evolutionary-case-for-mental-causation.md](/topics/evolutionary-case-for-mental-causation/) L167 "puzzles the interactionist position resolves" (against L153).

### Tenet 2: detectability, coherence dependence and mechanism overclaims (tenets L71, L75, L77)
- [concepts/causal-closure.md](/concepts/causal-closure/) L144 ✔ (priority 3), L196 and L198 ✔.
- [concepts/integrated-information-theory.md](/concepts/integrated-information-theory/) L201 "the quantum superpositions the proposal requires" (against tenets L77). This was first flagged as a NOTE in check 138 and has been upgraded because the same stale dependence recurs in causal-closure.
- [topics/consciousness-and-causal-powers.md](/topics/consciousness-and-causal-powers/) L104 "phenomenal factors… shift those distributions" (against L204 "no signature in *unconditioned* outcome frequencies").
- [concepts/stapp-quantum-mind.md](/concepts/stapp-quantum-mind/) L156 "Stapp's proposal exemplifies minimal interaction" (against L126, L66).
- [concepts/causal-consistency-constraint.md](/concepts/causal-consistency-constraint/) L95 and L97 "causally consistent by construction". The changed L61 now scopes the constraint to single-system marginals, and the alignment section was not updated to match.
- [concepts/retrocausality.md](/concepts/retrocausality/) L54 "empirical grounding in physics" (against L93).
- `topics/brain-computer-interfaces…` L145 "BCI evidence supports the minimality constraint" (against L77 "neutral").
- [topics/hypnagogic-phenomenology-and-interface-modulation.md](/topics/hypnagogic-phenomenology-and-interface-modulation/) L158 "micro-awakenings that briefly restore interface function" (against L84 and L86).
- [topics/quantum-holism-and-phenomenal-unity.md](/topics/quantum-holism-and-phenomenal-unity/) L112 "Entanglement provides the ontological unity" (against L120 "analogical and locational, not constitutive").
- [arguments/functionalism-argument.md](/arguments/functionalism-argument/) L127 "tenet holds that consciousness requires… particular biological structures". The tenet contains no substrate clause.

### Alignment, lead or body claims more than the argument supports (Tenet 1 and other)
- [apex/interface-specification-programme.md](/apex/interface-specification-programme/) L66 "Its five tenets establish that consciousness is irreducible". Contradicted by tenets L47: "They are not proven—they are chosen starting points".
- [apex/assessing-ai-consciousness-under-the-map.md](/apex/assessing-ai-consciousness-under-the-map/) L90 (against L86 "low probability rather than ruled out").
- [topics/attention-and-the-consciousness-interface.md](/topics/attention-and-the-consciousness-interface/) L169 (against L88).
- `topics/neurological-dissociations…` L193 "the Map's strongest empirical argument" (against L179 "Both readings predict the same dissociation phenomenology").
- [voids/erasure-void.md](/voids/erasure-void/) L115 and L117 "the puzzle dissolves" (against L54).
- [topics/consciousness-in-simple-organisms.md](/topics/consciousness-in-simple-organisms/) L251 (against L58).
- [concepts/minimal-consciousness.md](/concepts/minimal-consciousness/) L139 and L151 "The impossibility of identifying such a threshold suggests consciousness is fundamental". Carried from check 138 and still live after this window's edit.
- [topics/overdetermination-dissolution-under-selection-only-interactionism.md](/topics/overdetermination-dissolution-under-selection-only-interactionism/) L93 "The two approaches are compatible." Contradicted by its own L91 and by `interface-specification-programme` L112 ("a choice between two routes"). **This is a cross-article contradiction to adjudicate, not a local fix.**
- [concepts/dualism.md](/concepts/dualism/) L130 "The self-defeat structure is decisive" (against L134).
- [topics/enactivism-challenge-to-interactionist-dualism.md](/topics/enactivism-challenge-to-interactionist-dualism/) L108 "as evidence for dualism" (against L96).
- [concepts/phenomenal-contrast-method.md](/concepts/phenomenal-contrast-method/) L80.
- [topics/consciousness-and-neurodegenerative-disease.md](/topics/consciousness-and-neurodegenerative-disease/) L99 (identity asserted, against L135).
- [topics/phenomenal-authority-and-first-person-evidence.md](/topics/phenomenal-authority-and-first-person-evidence/) L209 (against L183).
- `topics/quantum-holism…` L184 ✔ (queued P1).
- `topics/brain-computer-interfaces…` L143 "would be meaningless" (against L77).
- [concepts/integrated-information-theory.md](/concepts/integrated-information-theory/) L144 (against L152).
- [concepts/entanglement-binding-hypothesis.md](/concepts/entanglement-binding-hypothesis/) L102.
- [concepts/phenomenal-overflow.md](/concepts/phenomenal-overflow/) L34, and L150 (qualia row: *Not invoked*).
- [concepts/phenomenal-depth.md](/concepts/phenomenal-depth/) L88.
- [topics/ethics-of-consciousness-invertebrate-question.md](/topics/ethics-of-consciousness-invertebrate-question/) L53 (the borderline item above).

### Carried and still live (no commit since the flagging report)
- **From check 138 (all 18 probed live):** `concepts/self-stultification` L197, `topics/ai-consciousness` L145, `topics/amplification-mechanisms-consciousness-physics` L181, `concepts/attention-schema-theory` L209, `concepts/consciousness-selecting-neural-patterns` L162, `concepts/categorical-surprise` L113, `concepts/phenomenology-of-choice-and-volition` L56, `concepts/universal-coupling-response` L92, `topics/quantum-neural-timing-constraints` L126, `topics/constitutive-exclusion` L120, `topics/consciousness-and-social-understanding` L161, `concepts/timing-gap-problem` L95, `voids/interface-formalization-void` L123, `apex/competency-without-felt-experience` L129, `concepts/attention-as-interface` L234, `concepts/methodological-pluralism` L119, `topics/basal-and-bioelectric-cognition` L95, `topics/embodied-consciousness` L194.
- **From check 137 (7 of 9 live):** `concepts/libet-experiments` L83, `topics/the-binding-problem` L176, `topics/volitional-control` L156, `arguments/materialism-argument` L140, `concepts/conscious-vs-unconscious-processing` L48, `concepts/mind-brain-separation` L112, `voids/conceptual-impossibility` L143.

## Notes

- [apex/self-concealing-interface.md](/apex/self-concealing-interface/) L81 and L165: "entailed" is still unconditional, while the changed L63 now says "Whether one exists is open". L77 "already-classical alternatives" conflicts with tenets L71.
- [apex/post-decoherence-selection-programme.md](/apex/post-decoherence-selection-programme/) L167 treats the formalism-actuality gap as the place a non-physical principle operates, against tenets L184.
- [topics/vertiginous-question.md](/topics/vertiginous-question/) L160 (mild Family I; the alignment text changed this window is clean). [concepts/neural-correlates-of-consciousness.md](/concepts/neural-correlates-of-consciousness/) L168 "This supports No Many Worlds". `topics/enactivism…` L114.
- [concepts/prebiotic-collapse.md](/concepts/prebiotic-collapse/) L106 "MWI eliminates the causal role for consciousness entirely" (against `interface-specification-programme` L175). L144 "proof that evolution can optimise" and L202 "indirect support" go further than tenets L79 "precedent rather than a licence".
- [concepts/meditation-and-consciousness-modes.md](/concepts/meditation-and-consciousness-modes/) L38, L181 ("a claim about possibility, not necessity" could read as though the tenet were merely modal), and L191.
- `topics/clinical-neuroplasticity…` L104 "removes a defeater" is scoped too widely.
- `topics/neurological-dissociations…` L197: the "10 bits per second" figure is assigned to consciousness.
- [topics/synaesthesia.md](/topics/synaesthesia/) L108; `topics/invertebrate-consciousness…` L103 "most parsimonious position for dualism"; `topics/phenomenal-authority…` L213; [concepts/entanglement-binding-hypothesis.md](/concepts/entanglement-binding-hypothesis/) L108 "no epistemic warrant"; [concepts/neuroplasticity.md](/concepts/neuroplasticity/) L154; `topics/quantum-holism…` L192; [topics/consciousness-and-causal-powers.md](/topics/consciousness-and-causal-powers/) L196; [concepts/retrocausality.md](/concepts/retrocausality/) L153. In each, parsimony leans in the Map's favour, or the tenet is stated more strongly than "defeasible".
- [topics/ethics-of-consciousness-invertebrate-question.md](/topics/ethics-of-consciousness-invertebrate-question/) L117; [concepts/visual-consciousness.md](/concepts/visual-consciousness/) L120 (Tenet 2 imported into rows the matrix marks *Not invoked*).
- [topics/quantum-hardware-and-the-ai-consciousness-coupling.md](/topics/quantum-hardware-and-the-ai-consciousness-coupling/) L33 "classical AI cannot be conscious" needs the conditional.
- [topics/born-rule-and-the-consciousness-interface.md](/topics/born-rule-and-the-consciousness-interface/) L219 "reflects genuine bidirectional causation"; [topics/phantom-limb-phenomena.md](/topics/phantom-limb-phenomena/) L83 and L113 "does real causal work"; [concepts/predictive-processing.md](/concepts/predictive-processing/) L182; [topics/phenomenology-of-returning-attention.md](/topics/phenomenology-of-returning-attention/) L144; [topics/conversion-disorder-as-consciousness-side-fault.md](/topics/conversion-disorder-as-consciousness-side-fault/) L123 (against L121). Each is a mild Family S case.
- Illusionism regress: [concepts/predictive-processing.md](/concepts/predictive-processing/) L122 and [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/) L134 still lean on it. `consciousness-in-simple-organisms` L191 ("it proves nothing") and unity's own L122 disclaim it. [concepts/dualism.md](/concepts/dualism/) L180 treats illusionism as refuted.
- [concepts/witness-consciousness.md](/concepts/witness-consciousness/) L180; [concepts/filter-theory.md](/concepts/filter-theory/) L178; [concepts/retrocausality.md](/concepts/retrocausality/) L103; [topics/consciousness-and-neurodegenerative-disease.md](/topics/consciousness-and-neurodegenerative-disease/) L107 (against L129).
- [apex/phenomenology-mechanism-bridge.md](/apex/phenomenology-mechanism-bridge/) L168; [apex/interface-specification-programme.md](/apex/interface-specification-programme/) L132 (against L120); `topics/pain-consciousness…` L76; [concepts/causal-closure.md](/concepts/causal-closure/) L182; [concepts/integrated-information-theory.md](/concepts/integrated-information-theory/) L138; [concepts/phenomenal-overflow.md](/concepts/phenomenal-overflow/) L142; [topics/clinical-evidence-quality-standards-consciousness-research.md](/topics/clinical-evidence-quality-standards-consciousness-research/) L148.
- **Register bookkeeping (not tenet issues):**
  - [positions/quantum-interface.md](/positions/quantum-interface/) L37 "all eleven" vs L43 "the ten positions".
  - [positions/methodology-and-calibration.md](/positions/methodology-and-calibration/) L68 grades [P-Q2](/positions/quantum-interface/#p-q2)/[P-Q7](/positions/quantum-interface/#p-q7) at "Grade D"; `quantum-interface.md` L122 grades them C.
  - [positions/positions.md](/positions/) L59 "Ten of the fifty-six" is stale against L73 "eleven of sixty-one".
  - [positions/subject-census.md](/positions/subject-census/) L71 "four booked gaps" vs L59 "Five gaps".
- **Carried:** tenets.md L159 still points at `[[apex/machine-question]] §senses of conscious`, and `grep -noiF "senses of conscious"` returns 0 in that file. The control hit is tenets.md L159 itself.

## Files passing all checks (26)

`apex/born-preserving-causal-efficacy`, `concepts/attended-intermediate-representations-theory`, **`concepts/cognitive-penetration`** (new), `concepts/constitution-vs-causal-work`, `concepts/disconnection-neuroscience`, `concepts/functional-seeming`, `concepts/phenomenal-conservatism` (its L98 is the model statement for effort phenomenology), `concepts/quiddity-epiphenomenalism-and-the-contingency-thesis`, `concepts/scale-types-for-phenomenal-quantities`, **`concepts/seemings`** (new), `concepts/self-model-theory-of-subjectivity`, `concepts/the-relocation-objection`, `positions/ai-substrate-verdicts`, `positions/methodology-and-calibration`, `positions/positions`, `positions/quantum-interface`, `positions/quantum-interface-calibration-history`, **`positions/subject-census-calibration-history`** (new), **`topics/anosognosia-and-the-reversible-self-monitoring-channel`** (new; links `^tenet-3-standing` and runs Tenet 5 in both directions), `topics/architectural-adequacy-at-the-built-edge` (both check-138 loci repaired; its No-MWI paragraph is correctly scoped), `topics/clinical-dissociation-as-systematic-evidence`, `topics/conversion-disorder-as-consciousness-side-fault` (one Note), `topics/presentiment-and-retrocausality` (the firewall is now correct at L105: "Confirmed presentiment would weigh against the Map, not for it."), **`topics/sham-controlled-neurofeedback-and-the-consciousness-comparator`** (new; holds Tenet 3 at available-not-actual), `topics/synaesthesia` (one Note), `voids/language-thought-boundary`.

All five new articles in this window pass. The expand-topic output is better calibrated than the older articles that the refines are patching.

## Method

- **Scope:** a delta sweep. It covers every live article with a commit in `git log --since=2026-09-23T23:55Z` across the six content sections, 85 files and about 290k words. The files were split into four balanced, read-only sub-sweeps. Each sub-sweep read `tenets.md` and every assigned file in full, had the delta diff available, and applied the direct-conflict lens and the alignment-versus-body structural lens. This is not a full-corpus reread.
- **Carry-forward** used a repair-shaped probe. For each of 42 prior loci, I checked whether the string survives *and* whether the file has a commit since the flagging report. The one absence without a commit hash (`consciousness-as-activity` supervenience) was confirmed as a repair from the diff (`git log -p`), with a positive control (`neural` hits L89 and L120).
- **Independent verification:** I re-verified with `grep -noF` the new ERROR, the carried ERROR, all four priority rows, all of §Summary 3, and every locus marked ✔. The remaining quotes were grep-verified by the sub-sweeps at one hit each. The WARNING and NOTE counts are approximate because several entries bundle two or three loci.
- **Open-task check:** I checked open `todo.md` blocks for each priority file. Only `quantum-holism-and-phenomenal-unity` has an open task covering its alignment section (P1, Leibniz concession). None of the four priority rows is queued.
- No counts use `grep -c`.

## Scope confirmation

- No article was edited and no task was minted. The only files written are this report and the changelog entry. Nothing was committed.
- The blocked Tenet-5 tiebreaker family (`NEEDS-HUMAN (doctrine) 2026-09-19`) was not re-measured. Its delta-adjacent loci are listed under Tenet 5 for visibility only.