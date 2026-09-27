---
ai_contribution: 100
ai_generated_date: 2026-09-27
ai_modified: 2026-09-27 06:25:01+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-09-27
date: &id001 2026-09-27
description: 'Tenet check 140: three of check 139''s four priorities repaired; six
  new ERRORs, four fabricating tenet content or contradicting tenets.md on Born preservation
  and collapse.'
draft: false
human_modified: 2026-09-27
last_curated: null
last_deep_review: null
lastmod: 2026-09-27 06:25:01+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-09-27
topics: []
---

# Tenet Alignment Check

**Date**: 2026-09-27 (check 140; previous [reviews/tenet-check-2026-09-25.md](/reviews/tenet-check-2026-09-25/) = 139)
**Files checked**: 79 articles read in full. This covers every live file in `topics/ concepts/ positions/ apex/ voids/ arguments/` with a commit since check 139 (2026-09-25 09:26 UTC), about 262k words. Three of the files are new: `concepts/empathy`, `concepts/panprotopsychism` and `topics/thoughtful-local-friendliness-and-the-artificial-friend`. `tenets.md` was read in full; it has had no commit since check 139. Carried loci from checks 137–139 were probed for repair.
**Errors**: 6 new. None is carried: both check-139 ERRORs were repaired. One booked-family locus is not recounted.
**Warnings**: about 100 new loci across about 55 files, plus 27 carried loci that are still live.
**Notes**: about 50
**Lens**: same as checks 138 and 139. The first test is direct conflict. The second is structural: does the lead, the alignment section or a body sentence claim more than the article's own argument or `tenets.md` supports?

## Summary

**1. Minted rows were repaired. The one unminted row was not.** Check 139's priorities 1–3 were each minted on 2026-09-25 and each is repaired:
- `consciousness-as-activity` L85 now reads "the Bidirectional Interaction tenet itself commits only to outcome-selection".
- `animal-consciousness`: the Bidirectional paragraph at L188 is now marked "Coherence commentary only".
- `causal-closure` L144 now reads "Not by dilution in the noise of unbiased events". L198 is scoped "(defeating pre-decoherence mechanisms only)".

Priority 4 (`concepts/dualism` L172 "explanatory parsimony favours dualism" and L154 "The Map rejects this because it is self-undermining") was never minted. It has no commit since and both strings are still live. The same holds for every carried-below-cap sibling from check 139 §Summary 3 in a file with no commit since:
- NCC L160
- cross-cultural L47
- pain L174
- dream L217
- `ethics-of-consciousness-invertebrate-question` L53

The pattern from checks 138 and 139 holds for a third report: minting is what moves items.

**2. Partial repairs dominate again, and three now come from the targeted repairs themselves.** Each item below was the subject of a named repair commit or task. In each, the repair fixed the sentence it was pointed at and left a sibling statement of the same claim live:
- [concepts/causal-closure.md](/concepts/causal-closure/). The 09-25 repair fixed L144's dilution clause. The same dilution framing survives at L120 "statistical invisibility within quantum noise" and L196 "any biases average out to undetectable fluctuations". L136 was reworded but still uses parsimony to disfavour hidden variables. L172 "the outcome is either random or consciously directed" was also missed by today's trilemma sweep, 3437ce4bb8.
- [topics/kabbalah-tzimtzum-consciousness-matter.md](/topics/kabbalah-tzimtzum-consciousness-matter/). Commit ae32dee539 swept five files for "the Map's substance dualism". In this file it changed one sentence. L78 "The Map is a substance [dualism](/concepts/dualism/)… exactly the monism its first tenet rejects" survives, and so do L34 and L84. It is ERROR 1 below.
- [topics/quantum-holism-and-phenomenal-unity.md](/topics/quantum-holism-and-phenomenal-unity/) L176 "The structural mismatch between physical relations and phenomenal unity supports dualism." Check 139 carried this as covered by an open P1. That P1 is now ✓ (2026-09-25, the Leibniz concession). The file has three commits since, and the sentence is still live. The article's own L88 calls the premise "a commitment of the Map's dualism, not a finding".
- The trilemma non-exhaustiveness sweep (3437ce4bb8, 2026-09-27) did not reach these loci:
  - [concepts/mental-effort.md](/concepts/mental-effort/) L72 "only selection explains why choosing feels effortful"
  - [concepts/delegatory-causation.md](/concepts/delegatory-causation/) L150 and L206 "must be conscious"
  - `causal-closure` L172
- Other files that had a commit this window but kept a stronger sibling of the claim that commit fixed:
  - [concepts/russellian-monism.md](/concepts/russellian-monism/) L43. The lead still draws No-MWI from "consciousness to act at measurement"; 01981c75ad re-scoped only L131. L141 also makes neural coherence a falsifier.
  - [topics/free-will.md](/topics/free-will/) L100. It survived today's refine of L202.
  - [concepts/measurement-problem.md](/concepts/measurement-problem/) L67 and L187 "more parsimoniously treated as one puzzle". The same file's L189 flags this very move.
  - [concepts/bi-aspectual-ontology.md](/concepts/bi-aspectual-ontology/) L37 and L139, against the repaired L53.
  - [apex/interface-specification-programme.md](/apex/interface-specification-programme/) L66 "Its five tenets establish" (carried from 139, the file was committed) and L132, against L120.
  - [apex/post-decoherence-selection-programme.md](/apex/post-decoherence-selection-programme/) L171 (carried from 139, the file was committed).
- **Deep-review and refine passes left carried loci alone.** `concepts/phenomenal-depth` L86 was flagged in check 139. It was deep-reviewed at 21:47 on 2026-09-25 (94bc4976c2) and is still live. `concepts/implicit-memory` L196 (the booked Tenet-5 family) survived ae32dee539.

**Recommendation carried from 139:** a refine brief should name the *claim*, not the sentence, and should make the executor grep the file for siblings before closing. This is now affecting sweep commits as well as single-file refines.

**3. New ERROR class concentration: the Born-rule and measurement cluster.** Three of the six new ERRORs sit in the corpus's quantum-interface core. They contradict `tenets.md` text on the two points it states most carefully:
- Born preservation holds "by construction, not by any sensitivity limit" (L75).
- Objective reduction supplies baseline definiteness, so "the measurement problem cannot itself be evidence for conscious selection" (L125, L184).

**4. Fabricated tenet content recurs, and Tenet 1 is now its main target.** Check 139 found the Bidirectional tenet made to "require" agent causation. This window has three Tenet-1 fabrications:
- Tenet 1 "rejects" emanationist monism (kabbalah).
- The Dualism tenet "predicts that consciousness should not arise from just any complex system" (collective-phenomena).
- Consciousness is "fundamental… not a late emergence" by "the Dualism tenet" (combination-problem). This contradicts tenets L125, where minds arrive billions of years late.

There are also softer attributions to Tenet 3 and to the tenets in general:
- `unity-of-consciousness` L144 "Bidirectional interaction requires a unified agent"
- `frankfurt-hierarchical-mesh` L88 "origination"
- `panpsychism` L186 "The [tenets](/tenets/) establish consciousness as irreducible and causally efficacious", the same class as interface-spec L66

**5. The families persist:**
- **Family S (Tenet 3 held as actual): about 40 loci.**
- **Family I (felt definiteness cited against MWI, contradicting tenets L172): about 15 loci.**
- **Tenet 5 used as a verdict: about 12 loci.**
- **Tenet 2: about 12 loci.** Neural coherence is treated as a falsifier or precondition of the Map's route, against tenets L77, and dilution/"lost in noise" is treated as the Born-preservation route, against L75.

No file endorses, in Map voice, physicalism, illusionism, epiphenomenalism, MWI, psi or energy injection. `concepts/entanglement-binding-hypothesis` L70 correctly treats the psi-scale twin study as a falsifier.

## Errors

All six were independently re-verified by me with `grep -noF`: one hit at the stated line, and context read.

1. **[topics/kabbalah-tzimtzum-consciousness-matter.md](/topics/kabbalah-tzimtzum-consciousness-matter/) L78** (Tenet 1, fabricated tenet content; partial repair). It says "The Map is a substance [dualism](/concepts/dualism/)—consciousness and matter are ontologically distinct" and "exactly the monism its first tenet rejects". The same claim appears at L34 "This is exactly what the Map's [dualism](/concepts/dualism/) ([Tenet 1](/tenets/#dualism)) denies" and at L84 "the Map's two substances".
   - Tenets L53: Tenet 1 is "neutral between substance and property dualism". Irreducibility does not rule out an idealist or emanationist monism.
   - Tenets L184: the substance lean is "downstream of agent causation, not the tenet".
   - **Fix:** "the Map's framework, which operates substance-dualist in its agency cluster". Move the divergence off Tenet 1.
2. **[topics/consciousness-and-collective-phenomena.md](/topics/consciousness-and-collective-phenomena/) L162** (Tenet 1, fabricated tenet content). It says "The [Dualism](/tenets/#dualism) tenet predicts that consciousness should not arise from just any complex system". `tenets.md` contains no such prediction.
   - **Fix:** attribute it to the Map's interface model.
3. **[concepts/combination-problem.md](/concepts/combination-problem/) L175** (Tenet 1, fabricated tenet content). It says "**Consciousness is fundamental**: Not a late emergence but a basic feature of reality (the [Dualism](/tenets/#dualism) tenet)."
   - Tenet 1 states irreducibility, not fundamentality.
   - Tenets L125: stars, chemistry and mutations ran "billions of years before the first mind", so consciousness is a late arrival on the Map's own account.
   - **Fix:** "Consciousness is irreducible (the Dualism tenet)".
4. **[topics/born-rule-and-the-consciousness-interface.md](/topics/born-rule-and-the-consciousness-interface/) L110** (Tenets 2/3; contradicts tenets L125, L184). It says "Whether this actuality requires phenomenal consciousness is a further question the Map answers affirmatively".
   - Tenets L125: physical collapse supplies baseline actuality everywhere, and consciousness modulates locally.
   - Tenets L184: once objective reduction secures definiteness, the measurement problem cannot be evidence for conscious selection.
   - **Fix:** "the Map holds that consciousness can bias which outcome is actual in neural systems; baseline actuality is supplied physically".
5. **[topics/brain-internal-born-rule-testing.md](/topics/brain-internal-born-rule-testing/) L157** (Tenet 2; contradicts tenets L75 and the article's own L106/L116). It says "The corridor's unfalsifiability is instrument-relative rather than principled."
   - L75: indistinguishability holds "by construction, not by any sensitivity limit".
   - Same-file siblings:
     - L143 "survives because the brain-internal testing regime is between first-generation instruments".
     - L155 "standard quantum mechanics is not empirically adequate at the brain-internal regime". The article's own L138 supports only "untested".
     - L153 invokes the "[parsimony-epistemology](/concepts/parsimony-epistemology/) case against MWI's branching ontology", against tenets L119 and L145.
   - **Fix:** the insulation is by construction in the unconditioned register; testability lives only in conditioned deviations ([P-Q3](/positions/quantum-interface/#p-q3)).
6. **[topics/testing-consciousness-collapse.md](/topics/testing-consciousness-collapse/) L179** (contradicts tenets L184). It says "The persistent difficulty of observer-free derivations constitutes indirect evidence that consciousness is structurally implicated in quantum measurement". The table row at L203 "| Consciousness structurally implicated |" repeats it, and L215 lists "Evidence that decoherence cannot solve the measurement problem" as support.
   - **Fix:** "is compatible with, not evidence for".

**Booked family, not recounted:** [concepts/implicit-memory.md](/concepts/implicit-memory/) L196 "The simplest account that covers *all* the phenomena" is still live after ae32dee539 touched the file. It is covered by the blocked `NEEDS-HUMAN (doctrine) 2026-09-19` Tenet-5 tiebreaker item.

**Borderline (counted as WARNING):**
- [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/) L144 "Bidirectional interaction requires a unified agent".
- [concepts/frankfurt-hierarchical-mesh-theory-of-the-will.md](/concepts/frankfurt-hierarchical-mesh-theory-of-the-will/) L88 "Under… Bidirectional Interaction (Tenet 3), the Map cares that a free action be the agent's own *origination*". The gloss after the dash matches L91's outcome-selection, but "origination" imports agent-causal sourcehood (tenets L57, L184).
- [concepts/panpsychism.md](/concepts/panpsychism/) L186 "The [tenets](/tenets/) establish consciousness as irreducible and causally efficacious", against tenets L47 "not proven" and L95. This is the same class as interface-spec L66, which check 139 counted as a WARNING.

## Priority list (capped at 4)

| # | Locus | Tenet | Why this one |
|---|---|---|---|
| 1 | [topics/born-rule-and-the-consciousness-interface.md](/topics/born-rule-and-the-consciousness-interface/) L110 | 2/3 | ERROR in a matrix-named core article (Born Rule row). It contradicts the tenets' own prebiotic-collapse resolution. The fix is one clause. Mint together with the L219 sibling "so observer-dependence reflects genuine bidirectional causation" |
| 2 | [topics/brain-internal-born-rule-testing.md](/topics/brain-internal-born-rule-testing/) L157 + L143, L153, L155 | 2, 5 | ERROR plus three same-file siblings. It inverts the L75 "by construction" clause the whole corridor reading rests on |
| 3 | Tenet-1 fabrication sweep: `kabbalah-tzimtzum` L34/L78/L84, `consciousness-and-collective-phenomena` L162, `combination-problem` L175 | 1 | Three ERRORs of one class, each a short attribution fix. The kabbalah loci are the residue of the ae32dee539 sweep. The brief should say "grep each file for every sentence attributing a claim to Tenet 1 or 'the Map's dualism'" |
| 4 | [topics/testing-consciousness-collapse.md](/topics/testing-consciousness-collapse/) L179 + L203 + L215 | 1/3 | ERROR repeated in a summary table, so a reader skimming the table gets the overclaim without the body |

**Carried below the cap, so they are not lost:**
- [concepts/dualism.md](/concepts/dualism/) L172 and L154. Check 139 priority 4, unminted, and this is its second report.
- [concepts/causal-closure.md](/concepts/causal-closure/) L120, L196, L136 and L172. Partial repair of check 139 priority 3.
- [topics/quantum-holism-and-phenomenal-unity.md](/topics/quantum-holism-and-phenomenal-unity/) L176. Its covering P1 closed without fixing it.
- [apex/post-decoherence-selection-programme.md](/apex/post-decoherence-selection-programme/) L171 and [apex/interface-specification-programme.md](/apex/interface-specification-programme/) L66, both carried from 139.
- [concepts/panpsychism.md](/concepts/panpsychism/) L186.
- The check-139 §Summary 3 siblings still live: NCC L160, cross-cultural L47, pain L174, dream L217 and L223, terminal-lucidity L86/L173/L177.

**Recommendation to the driver:** mint one `refine-draft` per priority row, plus one each for `dualism` and the `causal-closure` residue. Each brief should name the claim and require a sibling grep before closing. This check did not mint, per the skill's reports-only scope.

## Warnings

The sub-sweeps grep-verified every quote below with `grep -noF`, one hit at the stated line. I independently re-verified the ERRORs, the priority rows and §Summary 2. Line numbers are as of 2026-09-27 06:20 UTC. The counts are approximate because some entries bundle two or three loci.

### Family S: Tenet 3 held as actual, or epiphenomenalism reported refuted (tenets L93, L95 `^tenet-3-standing`, L101)
- [apex/phenomenology-of-consciousness-doing-work.md](/apex/phenomenology-of-consciousness-doing-work/) L76 "felt effort is wired into the regulatory chain, doing causal work even where…"; L78 "so the tracking is real". Both are against its own L78 "tracking is not evidence for the Map's account against them".
- [apex/post-decoherence-selection-programme.md](/apex/post-decoherence-selection-programme/) L171 ✔ "Post-decoherence selection is the mechanism by which consciousness causally influences the physical world" (against its own L93). Carried.
- [apex/interface-specification-programme.md](/apex/interface-specification-programme/) L72 "the quale carries causal weight"; L173 "architecturally necessary, not just philosophically asserted" (against L114). Both carried.
- [apex/pharmacological-dissociation-as-evidence.md](/apex/pharmacological-dissociation-as-evidence/) L142 "the reportability is itself evidence of causal connection" (against its own L182 and tenets L101–103).
- [concepts/agent-causation.md](/concepts/agent-causation/): L121 "demonstrates causal efficacy"; L127 "First-person experience confirms this" (against L141); L147/L151 "the self-defeat of physicalism delivers mental causation".
- [concepts/mental-effort.md](/concepts/mental-effort/) L94 "and so does causal work"; L134 (mechanism stated as fact, against L116).
- [concepts/problem-of-other-minds.md](/concepts/problem-of-other-minds/) L126 and L196 "no principled reason to trust behavioral evidence" (against its own L128 and tenets L101).
- [concepts/russellian-monism.md](/concepts/russellian-monism/) L97 and L101 "gives consciousness genuine causal work", as an advantage over Russellian monism, which ignores [P-Q3](/positions/quantum-interface/#p-q3)'s "sits genuinely close to epiphenomenalism".
- [topics/emergence-as-universal-hard-problem.md](/topics/emergence-as-universal-hard-problem/) L113 "the causal traffic between them runs in both directions" (against its own L39).
- [topics/consciousness-and-the-metaphysics-of-laws-and-dispositions.md](/topics/consciousness-and-the-metaphysics-of-laws-and-dispositions/) L146 "a real phenomenal property doing real causal work"; L158; L110 "which the Map takes to succeed"; L146 "fall to refutations already established" (against tenets L55).
- [topics/delegatory-dualism.md](/topics/delegatory-dualism/) L240 "provides theoretical justification for the claim" (against its own L216).
- [concepts/delegatory-causation.md](/concepts/delegatory-causation/) L51 "can do real causal work" (against its own L184); L132 "devastating"; L136 "the self-undermining argument eliminates epiphenomenalism" (tenets L101, L103).
- [topics/free-will.md](/topics/free-will/) L66 (the lead) "genuinely influences physical outcomes", against its own L108 and L118; L100 ✔ (partial repair); L108 "would be coincidental"; L147 "reflects genuine causal engagement".
- [concepts/spontaneous-intentional-action.md](/concepts/spontaneous-intentional-action/) L132 "where conscious causal influence does the most work" (against its own L80).
- [concepts/mind-brain-separation.md](/concepts/mind-brain-separation/) L118 "because it *is* determining which possibility becomes real" (also Family I).
- [concepts/post-decoherence-selection.md](/concepts/post-decoherence-selection/) L104 "and something non-physical actualizes the outcome" (against its own L96 and L116, and tenets L184).
- [topics/consciousness-and-probability-interpretation.md](/topics/consciousness-and-probability-interpretation/) L125 "requires causal flow from consciousness to physical behaviour" (tenets L93 "suggests").
- [topics/consciousness-in-smeared-quantum-states.md](/topics/consciousness-in-smeared-quantum-states/) L46 (the lead) "this determinacy is not incidental but causal" (against its own L124; partial repair).
- [topics/born-rule-and-the-consciousness-interface.md](/topics/born-rule-and-the-consciousness-interface/) L219 "reflects genuine bidirectional causation" (priority 1 sibling).
- [topics/consciousness-and-testimony.md](/topics/consciousness-and-testimony/) L145 "must causally influence" and "would be coincidental"; L131 (against its own L125).
- [topics/surprise-prediction-error-and-consciousness.md](/topics/surprise-prediction-error-and-consciousness/) L133 "Surprise provides evidence against [epiphenomenalism](/concepts/epiphenomenalism/)"; L141; L195.
- [topics/motor-control-quantum-zeno.md](/topics/motor-control-quantum-zeno/) L127 "where consciousness most visibly affects the physical world" (against its own L58); L131 (against L107 and L117).
- [concepts/bi-aspectual-ontology.md](/concepts/bi-aspectual-ontology/) L37 and L139 (against the repaired L53).
- [topics/consciousness-and-collective-phenomena.md](/topics/consciousness-and-collective-phenomena/) L52, L74, L154: the causal quantum substrate is stated as fact, against its own L70 "a model-relative consequence".
- [topics/empirical-evidence-for-consciousness-selecting.md](/topics/empirical-evidence-for-consciousness-selecting/) L42, where the lead overclaims (against its own L128 and L141); L134 "Fails (selection requires effects)"; L141 "Epiphenomenalism fails the first three lines outright" (against its own L53 and tenets L101).
- [topics/phenomenology-of-agency-vs-passivity.md](/topics/phenomenology-of-agency-vs-passivity/) L135 (common-cause strawman, against L133).
- [concepts/implicit-memory.md](/concepts/implicit-memory/) L3 (the description) and L41 "consciousness causally affects procedural execution" (against L101 and L188).
- [concepts/phenomenal-transparency-opacity-spectrum.md](/concepts/phenomenal-transparency-opacity-spectrum/) L121 "then consciousness is doing causal work on its own representational apparatus".
- [concepts/phenomenology-of-choice-and-volition.md](/concepts/phenomenology-of-choice-and-volition/) L3 "irreducible evidence for conscious causal efficacy" (against its own L161); L56 carried from 138.
- [topics/philosophy-of-habit-under-dualism.md](/topics/philosophy-of-habit-under-dualism/) L83 and L87 "the clearest everyday case of consciousness leaving a physical mark" (against its own L85).
- [concepts/phenomenal-depth.md](/concepts/phenomenal-depth/) L86 ✔ "but this concedes the point" imports mental causation into the zombie construct (qualia row: *Not invoked*; tenets L172). Carried from 139 and survived a deep review.
- [voids/voids-between-minds.md](/voids/voids-between-minds/) L144 "Dualism … is most directly supported" (against its own L154). [voids/confabulation-void.md](/voids/confabulation-void/) L104 "The middle case is what dualism predicts" (false dichotomy against L56–58).

### Family I: felt definiteness cited against MWI (tenets L172: branch-relative accounts "predict definite qualia within each branch")
- [concepts/problem-of-other-minds.md](/concepts/problem-of-other-minds/) L202 ✔ "Rejecting MWI means there's a determinate fact about whether you have phenomenal experience".
- [topics/surprise-prediction-error-and-consciousness.md](/topics/surprise-prediction-error-and-consciousness/) L199 ✔ "The phenomenology of surprise presupposes singular outcomes".
- [topics/consciousness-and-social-understanding.md](/topics/consciousness-and-social-understanding/) L161 "and with it the determinacy interpersonal understanding presupposes". The same sentence concedes "does not fail branch-internally". Carried from 138, and the file was committed.
- [topics/animal-consciousness.md](/topics/animal-consciousness/) L190 "not all possible experiences in branching worlds" (Animal row: *Not invoked*; it also misstates MWI).
- [topics/embodied-consciousness.md](/topics/embodied-consciousness/) L196 "collapse—not branching—is what produces the determinate bodily engagement" (carried from 138).
- [concepts/spontaneous-intentional-action.md](/concepts/spontaneous-intentional-action/) L136 "one thing, not many".
- [topics/consciousness-in-smeared-quantum-states.md](/topics/consciousness-in-smeared-quantum-states/) L100 "rather than explaining it away through observer-splitting".
- [concepts/implicit-memory.md](/concepts/implicit-memory/) L191–193. "there would be branches where the expert misses every shot" is wrong on Born weighting.
- [topics/consciousness-as-activity.md](/topics/consciousness-as-activity/) L132 (carried from 139; branch-relative agency is not flagged, tenets L184 posit 3).
- [concepts/phenomenology-of-choice-and-volition.md](/concepts/phenomenology-of-choice-and-volition/) L165 "matches collapse rather than branching" (carried from 138).
- [concepts/llm-consciousness.md](/concepts/llm-consciousness/) L100 "There is no "I" to be in one branch rather than another". All three machine rows mark No-MWI *Not invoked*.
- [concepts/measurement-problem.md](/concepts/measurement-problem/) L117: MWI "eliminates … mental causation" (tenets L170 and L184: branch-relative agency is available).
- [concepts/russellian-monism.md](/concepts/russellian-monism/) L43 ✔ (the lead; No-MWI drawn from consciousness acting at measurement, against tenets L117).

**Model wording** for these fixes is at [topics/phenomenology-of-agency-vs-passivity.md](/topics/phenomenology-of-agency-vs-passivity/) L171, [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/) L146 and [topics/consciousness-and-intersubjectivity.md](/topics/consciousness-and-intersubjectivity/) L121.

### Tenet 5: parsimony used as a verdict (tenets L145, L147)
- [concepts/dualism.md](/concepts/dualism/) L172 ✔ (carried, unminted).
- [concepts/measurement-problem.md](/concepts/measurement-problem/) L67 and L187 ✔ "more parsimoniously treated as one puzzle".
- [concepts/causal-closure.md](/concepts/causal-closure/) L136 ✔ "Occam's Razor cuts both ways … no less parsimonious than hidden variables".
- [topics/terminal-lucidity-and-filter-transmission-theory.md](/topics/terminal-lucidity-and-filter-transmission-theory/) L86 ✔ "a point in its favour on parsimony grounds" (now qualified, but still a verdict); L152 "accommodates more economically"; L177 "may actually be the more economical explanation".
- [topics/empirical-evidence-for-consciousness-selecting.md](/topics/empirical-evidence-for-consciousness-selecting/) L151 "parsimony favours it".
- [topics/brain-internal-born-rule-testing.md](/topics/brain-internal-born-rule-testing/) L153 (priority 2).
- [apex/phenomenology-of-consciousness-doing-work.md](/apex/phenomenology-of-consciousness-doing-work/) L175 "the more complex explanation … fits the evidence better" (against L157).
- [topics/emergence-as-universal-hard-problem.md](/topics/emergence-as-universal-hard-problem/) L111 "the apparent simplicity of physicalism is illusory".
- [concepts/combination-problem.md](/concepts/combination-problem/) L185 "strengthens the case" and L187 "cleaner ontology" (against its own L193).
- [concepts/naturally-occluded.md](/concepts/naturally-occluded/) L143: the claim that "anti-parsimony commitment is methodologically downstream of" the FBT theorem is an invented grounding for Tenet 5 (tenets L133–141).

### Tenet 2: coherence dependence, dilution and mechanism overclaims (tenets L71, L75, L77)
- [concepts/causal-closure.md](/concepts/causal-closure/) L120 ✔ "statistical invisibility within quantum noise" and L196 ✔ "average out to undetectable fluctuations". Both are residue of the priority-3 repair, against its own L144.
- [concepts/causal-closure.md](/concepts/causal-closure/) L198 "not empirically equivalent to physicalism" (against its own L146 and tenets L75).
- [concepts/russellian-monism.md](/concepts/russellian-monism/) L141 "demonstrating that quantum effects cannot survive in warm biological systems" is treated as a falsifier.
- [concepts/agent-causation.md](/concepts/agent-causation/) L160 "excluding quantum coherence in brain tissue would break the interface mechanism" (against its own L111).
- [concepts/ensemble-level-epiphenomenalism.md](/concepts/ensemble-level-epiphenomenalism/) L37 treats brain-scale superposition survival as "logically prior".
- [apex/born-preserving-causal-efficacy.md](/apex/born-preserving-causal-efficacy/) L71 "This article assumes both", one of which is superposition survival; L191 "secures that *something* must select".
- [topics/empirical-evidence-for-consciousness-selecting.md](/topics/empirical-evidence-for-consciousness-selecting/) L149 and L153 "Current evidence trends favourable".
- [concepts/llm-consciousness.md](/concepts/llm-consciousness/) L165 "a non-quantum-coherent system" is called conscious-impossible.
- [concepts/panpsychism.md](/concepts/panpsychism/) L134: the Map's reply draws only on Stapp and Orch OR and omits post-decoherence selection.
- [concepts/entanglement-binding-hypothesis.md](/concepts/entanglement-binding-hypothesis/): L76 "the Map's microtubule-scale interest is tenet-driven (Minimal Quantum Interaction)" is an invented attribution to Tenet 2. L104 and L106 state the mechanism as fact. L102 claims more than its own L32. L122 "makes quantum neural effects probable" goes beyond its own L78 "a realistic possibility".
- [topics/testing-consciousness-collapse.md](/topics/testing-consciousness-collapse/) L159 "sidesteps the timescale problem entirely" (the apex L57 limits this to the atemporal variant).
- [topics/sorkin-delta-brain-internal-analogues.md](/topics/sorkin-delta-brain-internal-analogues/) L37 (the lead; against its own L83 "structurally silent against the strict corridor").
- [topics/consciousness-and-probability-interpretation.md](/topics/consciousness-and-probability-interpretation/) L93 "the rule encodes the consciousness-physics interface" (against its own L89).

### Alignment, lead or body claims more than the argument supports (Tenet 1 and other)
- [concepts/panpsychism.md](/concepts/panpsychism/) L186 ✔ (borderline ERROR); L55 "precisely because the explanatory gap cannot be closed"; L142 "Physicalism fails, the hard problem is real"; L188. All are against its own L49 and tenets L55.
- [apex/interface-specification-programme.md](/apex/interface-specification-programme/) L66 ✔ "Its five tenets establish" (carried; tenets L47); L132 (against L120).
- [topics/quantum-holism-and-phenomenal-unity.md](/topics/quantum-holism-and-phenomenal-unity/) L176 ✔ "supports dualism" (against its own L88).
- [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/) L144 ✔ (borderline); [concepts/frankfurt-hierarchical-mesh-theory-of-the-will.md](/concepts/frankfurt-hierarchical-mesh-theory-of-the-will/) L88 ✔ (borderline).
- [topics/russellian-monism-versus-bi-aspectual-dualism.md](/topics/russellian-monism-versus-bi-aspectual-dualism/) L46 "marks a genuine ontological boundary"; L140 "is the honest expression of what Russellian monism's commitments entail" (against its own L40).
- [concepts/composition-and-consciousness.md](/concepts/composition-and-consciousness/) L75, L83 and L127 "explains why this must be so" (against its own L85, "the epistemic reading").
- [topics/embodied-consciousness.md](/topics/embodied-consciousness/) L194 "locates the interface precisely" (against L158; carried from 138).
- [concepts/mental-effort.md](/concepts/mental-effort/) L72 ✔; [concepts/delegatory-causation.md](/concepts/delegatory-causation/) L150 and L206; [concepts/causal-closure.md](/concepts/causal-closure/) L172 ✔. All three treat the trilemma as exhaustive and were missed by 3437ce4bb8.
- [concepts/illusionism.md](/concepts/illusionism/) L3 (the description) "an equally hard illusion problem" (against L67 "potentially as hard").
- [concepts/phenomenology-of-choice-and-volition.md](/concepts/phenomenology-of-choice-and-volition/) L145: the regress is presented as a refutation, against `illusionism` L91 "proves nothing".
- [concepts/functional-seeming.md](/concepts/functional-seeming/) L93: the Mary verdict is stated flatly, with no framework-boundary flag (compare `illusionism` L115).
- [topics/terminal-lucidity-and-filter-transmission-theory.md](/topics/terminal-lucidity-and-filter-transmission-theory/) L112, L173 and L177 (against L118, L132 and L156).
- [concepts/llm-consciousness.md](/concepts/llm-consciousness/) L56 "they lack the non-physical component consciousness requires" and L114 (against its own L86 and L150).
- [concepts/measurement-problem.md](/concepts/measurement-problem/) L197 "a structural feature … not a technical gap" (against its own L203).

### Carried and still live (no commit since the flagging report)
- **From check 139, both unminted:**
  - `concepts/dualism` L172 and L154 (and L130 and L180)
  - `concepts/neural-correlates-of-consciousness` L160
  - `topics/cross-cultural-phenomenology-of-agency` L47
  - `topics/pain-consciousness-and-causal-power` L174
  - `topics/dream-consciousness` L217 and L223
  - `topics/ethics-of-consciousness-invertebrate-question` L53
- **From check 138 (all 21 files with no commit since are live by construction):**
  - `concepts/self-stultification` L197
  - `topics/ai-consciousness` L145
  - `topics/amplification-mechanisms-consciousness-physics` L181
  - `concepts/attention-schema-theory` L209
  - `concepts/consciousness-selecting-neural-patterns` L162
  - `concepts/categorical-surprise` L113
  - `concepts/universal-coupling-response` L92
  - `topics/quantum-neural-timing-constraints` L126
  - `topics/constitutive-exclusion` L120
  - `concepts/timing-gap-problem` L95
  - `voids/interface-formalization-void` L123
  - `apex/competency-without-felt-experience` L129
  - `concepts/attention-as-interface` L234
  - `concepts/methodological-pluralism` L119
  - `topics/basal-and-bioelectric-cognition` L95
- **From check 137:**
  - `concepts/libet-experiments` L83
  - `topics/the-binding-problem` L176
  - `topics/volitional-control` L156
  - `arguments/materialism-argument` L140
  - `concepts/conscious-vs-unconscious-processing` L48
  - `voids/conceptual-impossibility` L143
- **Carried loci in files committed this window, re-probed by string and still live:**
  - `concepts/mind-brain-separation` L112 "The division of faculties supports both"
  - `concepts/phenomenology-of-choice-and-volition` L56 and L165
  - `topics/consciousness-and-social-understanding` L65 and L161
  - `topics/embodied-consciousness` L194

## Notes

- [concepts/african-philosophy-of-consciousness.md](/concepts/african-philosophy-of-consciousness/) L47 "the Map's [substance-leaning reading](/concepts/dualism/)" in a non-agency article. This is ae32dee539's own chosen replacement wording, and it is defensible under tenets L184 ("the framework operates substance-dualist"). It would read better as "the Map's agency-cluster substance lean".
- [topics/overdetermination-dissolution-under-selection-only-interactionism.md](/topics/overdetermination-dissolution-under-selection-only-interactionism/) L93 "The two approaches are compatible." is still live. It is carried from 139 as a cross-article adjudication against `interface-specification-programme` L112, not as a local defect. The rest of the file passes.
- [topics/born-rule-and-the-consciousness-interface.md](/topics/born-rule-and-the-consciousness-interface/) L221 "the Map regards as decisive" (tenets L117 scopes "decisive" to branch-egalitarian readings).
- [apex/post-decoherence-selection-programme.md](/apex/post-decoherence-selection-programme/) L73, L93 and L167 (a non-physical principle placed in the formalism–actuality gap, against tenets L125 and L184).
- [topics/brain-internal-born-rule-testing.md](/topics/brain-internal-born-rule-testing/) L151: "directly tested", although the corridor predicts a null by construction.
- [topics/testing-consciousness-collapse.md](/topics/testing-consciousness-collapse/) L149 "convergence evidence for bidirectional causation".
- [concepts/measurement-problem.md](/concepts/measurement-problem/) L63 "predicts exactly what standard quantum mechanics predicts" over-concedes: it ignores the conditioned register ([P-Q3](/positions/quantum-interface/#p-q3)).
- [concepts/causal-closure.md](/concepts/causal-closure/) L134 and L168.
- [concepts/articulability-of-q1.md](/concepts/articulability-of-q1/) L62 "tenets *posit* that such a law operates" (tenets.md names no psychophysical law); L131. [concepts/supervenience.md](/concepts/supervenience/) L83 and L101.
- [concepts/disconnection-neuroscience.md](/concepts/disconnection-neuroscience/) L86 "the interface reading the Dualism tenet underwrites".
- [concepts/bi-aspectual-ontology.md](/concepts/bi-aspectual-ontology/) L55, L129 and L143 (Tenet 5 "justifies").
- [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/) L134 (the illusionism regress reads as a refutation, against L122).
- [concepts/llm-consciousness.md](/concepts/llm-consciousness/) L104 and L142.
- [concepts/entanglement-binding-hypothesis.md](/concepts/entanglement-binding-hypothesis/) L108 "parsimony has no epistemic warrant" (stronger than tenets L133 "lacks universal").
- [concepts/post-decoherence-selection.md](/concepts/post-decoherence-selection/) L66 and L108. [topics/consciousness-in-smeared-quantum-states.md](/topics/consciousness-in-smeared-quantum-states/) L120.
- [topics/free-will.md](/topics/free-will/) L234 "Dream evidence for consciousness's causal role". This Further-Reading label survived today's cut of the dream paragraph. L218 and L231 are stronger than the body.
- [topics/embodied-consciousness.md](/topics/embodied-consciousness/) L174. [topics/russellian-monism-versus-bi-aspectual-dualism.md](/topics/russellian-monism-versus-bi-aspectual-dualism/) L114 (QM has not "undermined" energy conservation) and L144.
- [topics/panpsychisms-combination-problem.md](/topics/panpsychisms-combination-problem/) L139 (unity attributed to Tenet 3). [voids/source-attribution-void.md](/voids/source-attribution-void/) L133. [voids/voids.md](/voids/) L295.
- [concepts/where-the-substance-commitment-enters.md](/concepts/where-the-substance-commitment-enters/) L28 names two sub-tenet sources where tenets L184 names one. It is reconciled at L56 and L77. Consider a one-line cross-reference in tenets L184.
- [apex/phenomenology-of-consciousness-doing-work.md](/apex/phenomenology-of-consciousness-doing-work/) L171 and L186. [topics/introspection-architecture-independence-scoring.md](/topics/introspection-architecture-independence-scoring/) L191 (against L193).
- [concepts/agent-causation.md](/concepts/agent-causation/) L109 and L111 (the quantum-biology claim goes beyond tenets L79 "precedent rather than a licence"). [concepts/mental-effort.md](/concepts/mental-effort/) L98 "unstable".
- [concepts/problem-of-other-minds.md](/concepts/problem-of-other-minds/) L100 "The simplest hypothesis". [topics/emergence-as-universal-hard-problem.md](/topics/emergence-as-universal-hard-problem/) L61 and L115.
- [topics/phenomenology-of-trust.md](/topics/phenomenology-of-trust/) L95 and L125. [concepts/ensemble-level-epiphenomenalism.md](/concepts/ensemble-level-epiphenomenalism/) L79 (the trilemma "secures only that selection occurs"). [concepts/phenomenal-depth.md](/concepts/phenomenal-depth/) L88.
- [topics/consciousness-and-testimony.md](/topics/consciousness-and-testimony/) L3 and L147 (the No-MWI remark is circular). [topics/surprise-prediction-error-and-consciousness.md](/topics/surprise-prediction-error-and-consciousness/) L197. [topics/motor-control-quantum-zeno.md](/topics/motor-control-quantum-zeno/) L129 (global exclusion not marked as a posit). [voids/voids-between-minds.md](/voids/voids-between-minds/) L146 and L150.
- [apex/born-preserving-causal-efficacy.md](/apex/born-preserving-causal-efficacy/) L193. [apex/interface-specification-programme.md](/apex/interface-specification-programme/) L177. [topics/phenomenology-of-agency-vs-passivity.md](/topics/phenomenology-of-agency-vs-passivity/) L3.
- [concepts/illusionism.md](/concepts/illusionism/) L159. [concepts/implicit-memory.md](/concepts/implicit-memory/) L83, L115 and L185. [topics/consciousness-as-activity.md](/topics/consciousness-as-activity/) L77 (against its own L126).
- [concepts/naturally-occluded.md](/concepts/naturally-occluded/) L139 frames invisibility as a detection threshold, against tenets L75. [concepts/phenomenal-transparency-opacity-spectrum.md](/concepts/phenomenal-transparency-opacity-spectrum/) L119.
- [concepts/phenomenology-of-choice-and-volition.md](/concepts/phenomenology-of-choice-and-volition/) L151 and L163. [concepts/functional-seeming.md](/concepts/functional-seeming/) L67. [topics/akrasia-and-weakness-of-will.md](/topics/akrasia-and-weakness-of-will/) L100. [concepts/panprotopsychism.md](/concepts/panprotopsychism/) L73.
- **Carried:** tenets.md L159 still points at `[[apex/machine-question]] §senses of conscious`. That anchor has not been re-probed this window; the file has no commit.

## Files passing all checks (15)

- `topics/cross-architecture-llm-introspection`: claims compatibility only and credits the rival.
- `topics/cross-species-behavioural-confidence-proxy-tests`: the bounded-witness reading is marked as internal to the Map.
- **`topics/thoughtful-local-friendliness-and-the-artificial-friend`** (new): conditional throughout.
- `topics/consciousness-and-intersubjectivity`: L121 is a model No-MWI treatment.
- **`concepts/empathy`** (new): explicitly declines to claim that dualism follows.
- `concepts/seemings`
- `concepts/local-tomography-and-the-consciousness-physics-interface`: says outright that it gives no evidence for the interface reading.
- `topics/overdetermination-dissolution-under-selection-only-interactionism`: one carried Note.
- `concepts/disconnection-neuroscience`: one Note.
- `concepts/articulability-of-q1`: Notes only.
- `concepts/phenomenal-conservatism`
- `topics/akrasia-and-weakness-of-will`: one Note.
- **`concepts/panprotopsychism`** (new): one Note, and good framework-boundary handling.
- `voids/source-attribution-void`: one Note. Its Dualism and Bidirectional sections are models of the compatibility-not-evidence framing.
- `concepts/where-the-substance-commitment-enters`: one Note.

All three new articles pass. As in check 139, expand-topic output is better calibrated than the older articles the refines are patching.

## Method

- **Scope:** a delta sweep. It covers every live article with a commit in `git log --since=2026-09-25T09:26:36Z` across the six content sections plus `tenets/`: 79 files and about 262k body words. `tenets.md` has no commit in the window. The files were split into four balanced, read-only sub-sweeps. Each sub-sweep read `tenets.md` and every assigned file in full and applied the direct-conflict lens and the structural lens. This is not a full-corpus reread.
- **Carry-forward** used a repair-shaped probe: for each prior locus, does the string survive, and does the file have a commit since the flagging report? All three absences (`consciousness-as-activity` L85, `animal-consciousness` L192, `causal-closure` L144 dilution) were confirmed as repairs by reading the replacement text at the new line.
  - `causal-closure` L198 is still present but has been rescoped to "(defeating pre-decoherence mechanisms only)".
  - Carried check-137 and check-138 loci in files with no commit since are live by construction. Those in files committed this window were re-probed by string.
- **Independent verification:** I re-verified with `grep -noF` all six ERRORs, the three borderline items, every priority row, and every locus marked ✔. I read the surrounding context for each ERROR. Two sub-sweep ERROR proposals were downgraded to WARNING for consistency with checks 138 and 139, which class Family I as WARNING: `problem-of-other-minds` L202 and `surprise` L199. Three others were downgraded as well:
  - `african-philosophy` L47, to a Note: it is the repair commit's own wording.
  - `panpsychism` L186 and `frankfurt` L88, to borderline WARNING, matching the class of interface-spec L66.
- **Open-task check:** the check-139 priorities 1–3 have ✓ tasks in `todo.md` (L1786 area, L1871, L1876, L1878). No task covers `concepts/dualism`. The `quantum-holism` P1 that check 139 relied on is now ✓, and L176 survived it.
- No counts use `grep -c`.

## Scope confirmation

- No article was edited and no task was minted. The only files written are this report and the changelog entry. Nothing was committed.
- The blocked Tenet-5 tiebreaker family (`NEEDS-HUMAN (doctrine) 2026-09-19`) was not re-measured.