---
ai_contribution: 100
ai_generated_date: 2026-09-30
ai_modified: 2026-09-30 07:46:00+00:00
ai_system: claude-fable-5-1
author: Andy Southgate
concepts: []
created: 2026-09-30
date: &id001 2026-09-30
description: 'Tenet check 142: all fourteen check-141 ERRORs still live and unminted;
  one new ERROR (wheelers redefines Tenet 2''s minimality); the propagation lens finds
  three tenets-only repairs whose dependents still carry the old wording.'
draft: false
human_modified: 2026-09-30
last_curated: null
last_deep_review: null
lastmod: 2026-09-30 07:46:00+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-09-30
topics: []
---

# Tenet Alignment Check

**Date**: 2026-09-30 (check 142; previous [reviews/tenet-check-2026-09-28.md](/reviews/tenet-check-2026-09-28/) = 141)
**Files checked**: 70 files read in full by five sub-sweeps, every locus grep-verified by the sweep and the ERRORs and priority loci independently re-verified by the driver. This is every live file in `topics/ concepts/ positions/ apex/ voids/` with a commit since check 141 (2026-09-28 12:20 UTC), about 231k words: 23 concepts, 26 topics, 20 voids, 1 apex, 1 positions. Nine of the files are new since check 141 (`concepts/swampman`, `concepts/process-1-specification-problem`, `topics/correlationism-and-the-ancestrality-argument`, `voids/assent-void`, `voids/blindspot-void`, `voids/categorical-perception-void`, `voids/causal-impression-void`, `voids/cross-state-void`, `voids/handedness-void`, `voids/mirth-void`, `voids/taboo-void`). `tenets.md` had no commit this window; L49–147 and L182–186 were re-read and the Rules-out clauses are unchanged. Every carried ERROR from check 141 was re-probed by exact string. Corpus-wide (all sections, not only the window) propagation greps were run for the three tenet wordings qualified in September.
**Errors**: 1 new, 14 carried (all fourteen check-141 ERRORs are still live). 15 live.
**Warnings**: 68 new loci (57 from the window sweeps, 11 from the propagation lens) across about 40 files, plus 25 carried loci still live.
**Notes**: 55
**Lens**: same as checks 138–141 (direct conflict with a Rules-out clause; then lead / alignment-section / body claiming more than the argument or `tenets.md` supports), plus the propagation lens: where `tenets.md` itself was qualified, grep dependents for the OLD unqualified form. Lexical anchoring flags were not counted as violations.

## Summary

**1. Nothing from check 141 was minted, so nothing moved — for a fifth report.** No task in the Active section of [workflow/todo.md](/workflow/todo/) references `tenet-check-2026-09-27` or `-28`, and none of the fourteen check-141 ERROR files has a covering task. All fourteen strings are live at one hit each (list under §Errors → Carried). One probe returned a false zero on the first pass — `consciousness-and-collective-phenomena` L162 is written `The [[tenets#^dualism|Dualism]] tenet predicts…`, so the plain-text probe missed it; the wikilink form is live. Six of the fourteen are now three reports old (check 140), and the `concepts/dualism` L172/L154 pair is on its fourth unminted report.

**2. The propagation lens finds three tenets-only repairs whose dependents were never swept.** This is the check's main new result.
- **The classical-menu analogy (Tenet 3, L105).** Commit 3f5452f920 (2026-09-02) rewrote the tenets' own analogy from "The brain presents options; the mind selects" to "improper-mixture components awaiting actualisation, not already-definite alternatives" because L71 disclaims exactly that menu ontology. The commit touched `tenets.md` alone. The OLD form is live in seven dependents, none flagged in checks 137–141: `topics/trilemma-of-selection` L129 "The brain presents options to consciousness (world→mind); consciousness selects among them (mind→world)"; `topics/attention-and-the-consciousness-interface` L173 "The brain presents options (brain → mind); consciousness selects among them (mind → brain)"; `topics/brain-computer-interfaces-and-the-interface-boundary` L83 "the brain presents options, consciousness biases selection"; `concepts/neuroplasticity` L56 "The brain presents options; consciousness selects; selection produces plasticity"; `concepts/retrocausality` L155 "The brain presents options; consciousness selects; the selection determines which neural history becomes actual"; `concepts/mind-brain-separation` L118 "The rendering engine presents options; consciousness actualizes one"; `apex/phenomenology-mechanism-bridge` L59 "the neural architecture that presents options, through the quantum mechanism that enables selection". Two hits are calibrated and pass: `concepts/von-neumann-wigner-interpretation` L94 and `concepts/coupling-modes` L132 both carry the "not a pick from a pre-existing classical menu" wording; `coupling-modes` L46 uses the phrase to describe Stapp's basis-control model, which L128 marks as not adopted.
- **The unconditioned qualifier (Tenet 2, L75/L81).** Commit 71a78a577b (2026-09-04) scoped "empirically indistinguishable from chance" to "under any *unconditioned aggregate* test… by construction, not by any sensitivity limit", leaving a conditioned deviation live ([P-Q3](/positions/quantum-interface/#p-q3)). It touched `tenets.md` alone. Of 28 corpus hits for the phrase, three state the unscoped form: `topics/epistemology-of-mechanism-at-the-consciousness-matter-interface` L123 "so it is by that construction indistinguishable from chance—a framework-boundary feature rather than a near-term test"; `concepts/sorkin-higher-order-interference` L72 "the Map treats its interaction as empirically indistinguishable from chance rather than as a predicted κ ≠ 0"; `topics/the-steelman-for-process-monism` L75 "must defend that interface against the charge that it is empirically indistinguishable from chance". A fourth, in-window, is worse: `topics/personal-identity` L189 "consciousness-selection within Born probabilities is empirically indistinguishable from random collapse—the quantum mechanism is a philosophical framework, not a testable hypothesis", against tenets L81 falsifier (c). `wheelers` L178 and `apex/post-decoherence-selection-programme` L91 carry the ensemble/conditioned scoping and pass. Check 141's `falsification-roadmap` L107 (sensitivity framing) belongs to this family and is still live.
- **The phenomenal-concept-strategy roster (Tenet 3, L103).** Commit 9afad1f283 (2026-09-05) removed Frankish 2016 from the PCS roster (he is an illusionist; the tenet now says illusionism "is a separate reply that this concession does not absorb") and swept five dependents. It missed `concepts/integration-as-activity` L50 "the phenomenal-concept strategy, developed by Loar (1990), Papineau (2002), and Frankish (2016)" (last commit 2026-07-10).
- Two other September qualifications propagated cleanly: the Maier 2018 external-RNG scoping (e3e689517d) has no new residue beyond the two check-141 loci, and the L117 "decisive against branch-egalitarian readings" scoping has only the carried `born-rule` L221; `mine-ness` L144 ("suggestive of, though not decisive against"), `wavefunction-realism-vs-primitive-ontology` L64 and `decoherence` L71 are calibrated.

**3. One new ERROR: Tenet 2's minimality redefined.** `topics/wheelers-participatory-universe-and-it-from-bit` L156 (committed 9470bb57b4, 2026-09-29): the Map's "minimal" is to be "read as \"smallest actually sufficient,\" not \"smallest that preserves ensemble statistics.\"" Tenets L69 defines Tenet 2's minimality as empirical-constraint minimality "fixed by the Rules-out clause… no Born-statistics violation", and L71 ranks post-decoherence Born-preserving selection as "the strongest path the Map currently endorses"; the article both denies the Born-preservation reading and demotes the endorsed path to one of three unranked branches. The same file's L160 gives Wheeler's "untestability and ontological excess" as a rejection the Map "shares" and merely "adds" the indexical objection to, inverting tenets L117/L119/L145.

**4. Covered elsewhere — recorded, not duplicated.** Today's outer-review synthesis ([reviews/outer-review-synthesis-2026-09-30.md](/reviews/outer-review-synthesis-2026-09-30/) cluster 6) found `concepts/galilean-exclusion`'s tenet section upgrading compatibility into evidence. All three loci are live and are quoted under §Warnings; the sibling P1 refine (todo.md "Husserl, Whitehead and the *Blind Spot* authors are conscripted… and the tenet section states \"it is expected\"") already covers them. The P1 on `project/writing-style` + this skill (co-optation roster has no phenomenological/process line; check-tenets tests for violations only, never over-reach) is likewise queued; this report applied the over-reach lens ad hoc, as checks 138–141 did, and the task should make it part of the skill text. `concepts/implicit-memory` L194 (Tenet-5 tiebreaker) remains booked under the blocked NEEDS-HUMAN (doctrine) item.

**5. The window's families, at the usual density.**
- **Tenet 3 held as actual, or epiphenomenalism/illusionism reported refuted: about 25 new loci.** Densest in the files touched 2026-09-29: `topics/phenomenology-of-intellectual-life` (five loci in one Relation-to-Site section, L184/L186/L190/L214/L218), `topics/predictive-processing-and-dualism` L104/L152/L154 (flagged 09-25, still live after a 09-29 touch), `concepts/binding-problem` L88/L210/L212 (touched 09-29 by the reciprocal-link sweep, all five tenet-section loci untouched), `voids/mirth-void` L94 (fresh create).
- **Compatibility upgraded to "support"/"evidence"/"predicts": about 15 new loci**, including `voids/mattering-void` L114 "primary evidence for **Dualism**" (out of step with the index it sits under, [voids/voids.md](/voids/) L147), `concepts/objectivity-and-consciousness` L84 "what a dualist framework predicts" (its own L122 corrects it), `topics/incubation-effect` L144/L146/L148, `topics/anaesthesia` L143, `topics/consciousness-defeats-explanation` L158, `voids/causal-interface` L158 "Minimal Quantum Interaction predicts this void", `voids/infant-consciousness` L105 "implies".
- **Family I (felt definiteness against MWI, or quick "nothing to select"): 8 new loci** — `binding-problem` L212, `consciousness-and-cognitive-distinctiveness` L188, `modal-structure-of-phenomenal-properties` L115, `intellectual-life` L218, `predictive-processing` L154, `vertiginous-question` L161 (scoped, mild), `time-symmetric-selection-mechanism` L214, `wheelers` L160. The 09-28 `implicit-memory` L191 and `consciousness-defeats-explanation` L166 repairs are the model and are verified in place.
- **Tenet 1 glossed as substance dualism or fundamentality: 8 loci.** Substance: `correlationism` L100/L74, `brain-specialness-boundary` L63, `diachronic-agency` L127 — none cites `where-the-substance-commitment-enters`, the page tenets L57 points at, and that page itself passes. Fundamentality: `three-kinds-of-void` L103/L65, [voids/voids.md](/voids/) L313/L90, `consciousness-defeats-explanation` L110.
- **Tenet 5 misgrounded or used as a verdict: 6 loci** — `causal-interface` L112 "This is not conspiracy but parsimony", `apex/taxonomy-of-voids` L197 "the Map's reading is the simpler accommodation", `intellectual-life` L184, `coupling-modes` L82 (self-corrected L126), `teleosemantics` L92 (carried), `motor-control-quantum-zeno` L131 (carried).

**6. Repairs verified in place (10 loci, 9 files).** `conscious-vs-unconscious-processing` L48 and the L173–175/L193/L235/L241 set (fed735f497); `implicit-memory` L191 (a98b3cc4c1); `constitutive-exclusion` L120→L133 (1e60bfc6f6); `consciousness-defeats-explanation` L166 (6a00f3ebee); `time-symmetric-selection-mechanism` L39→L40 and L139→L140 (4f4faf64ab); `phenomenology-of-imagination` L118 (4b6ef9c0f3); `blindspot-void` L97 (c1c20cd5ca); `intrinsic-nature-void` L117 (f78da095ab); `necessary-opacity` L152/L154 (aebfc92ff7). In each case the old substring returns zero and the calibrated replacement is live. Two of the repairs left a sibling standing in the same file: `imagination` L72 "reflects consciousness doing active work" and `conscious-vs-unconscious` L177 "consciousness must be causally efficacious for our claims about it to be trustworthy".

**7. Fresh-create quality holds, with two exceptions.** Of the nine new articles, seven are clean under the [P-V2](/positions/voids-as-evidence/#p-v2) template (`assent-void`, `blindspot-void`, `categorical-perception-void`, `causal-impression-void`, `handedness-void`, `taboo-void`, `process-1-specification-problem`) and `swampman` and `cross-state-void` carry only a WARNING/NOTE each. `mirth-void` L94 and `correlationism` L100 are the exceptions.

## Errors

Every string below was re-verified by the driver with exact-substring grep (one hit at the stated line; wikilink-formatted lines probed on their plain-text tail). Line numbers are as of 2026-09-30 07:44 UTC.

### New (1)

1. **[topics/wheelers-participatory-universe-and-it-from-bit.md](/topics/wheelers-participatory-universe-and-it-from-bit/) L156** (Tenet 2, contradicts tenets L69/L71). "the Map commits to the *minimal* such interaction — read as \"smallest actually sufficient,\" not \"smallest that preserves ensemble statistics.\"" Same line: "the Map holds this as a live fork… not a settled commitment."
   - Tenets L69: Tenet 2's minimality "is *empirical-constraint* minimality, fixed by the Rules-out clause below: the interaction must respect the empirical record (no detectable energy injection, no Born-statistics violation…)". "Smallest actually sufficient" is the parsimony-shaped reading L69 disowns. Tenets L71 names post-decoherence Born-preserving selection "the strongest path the Map currently endorses", not one branch of an unranked fork.
   - Siblings: L160 (Tenet 4/5 inversion, WARNING); L142 coherence dependence attributed to the Map's thesis, self-corrected in the same paragraph. L84, L86, L116, L178 are correct.
   - **Fix:** "read as the smallest deviation that respects the empirical record — no Born-statistics violation on the unconditioned aggregate, no energy injection — with post-decoherence Born-preserving selection the path the Map endorses most strongly (tenets L69, L71)."

### Carried (14, all from checks 140–141; none minted, none repaired)

2. [concepts/composition-and-consciousness.md](/concepts/composition-and-consciousness/) L111 "It is a basic feature of reality that must be accepted rather than explained in terms of something more fundamental. This is the position the Map endorses through its Dualism tenet." (check 141 #1)
3. [topics/falsification-roadmap-for-the-interface-model.md](/topics/falsification-roadmap-for-the-interface-model/) L173 "this challenges Tenet 3's prediction that consciousness makes an irreplaceable functional contribution"; L107 "partially foreclosed one visible branch of bidirectional interaction". (check 141 #2)
4. [topics/phenomenology-of-returning-attention.md](/topics/phenomenology-of-returning-attention/) L97 "tenet predicts exactly this two-directional structure". (check 141 #3)
5. [apex/consciousness-and-agency.md](/apex/consciousness-and-agency/) L120 "a narrow interface to action-relevant alternatives is what Minimal Quantum Interaction predicts". (check 141 #4)
6. [concepts/haecceity.md](/concepts/haecceity/) L181 "The Map's tenets imply haecceity about conscious subjects… No Many Worlds requires a fact about which conscious subject I am." (check 141 #5)
7. [topics/many-minds-interpretation.md](/topics/many-minds-interpretation/) L86 "modulating the statistics of a real, local collapse". (check 141 #6)
8. [concepts/quantum-consciousness.md](/concepts/quantum-consciousness/) L114 "the philosophical case for consciousness as outcome-selector stands on its own". (check 141 #7)
9. [topics/indexical-identity-quantum-measurement.md](/topics/indexical-identity-quantum-measurement/) L147 "Consciousness determines *for whom* each outcome is actual." (check 141 #8)
10. [topics/kabbalah-tzimtzum-consciousness-matter.md](/topics/kabbalah-tzimtzum-consciousness-matter/) L78 "exactly the monism its first tenet rejects" (with L34, L84). (check 140)
11. [topics/consciousness-and-collective-phenomena.md](/topics/consciousness-and-collective-phenomena/) L162 "The [Dualism](/tenets/#dualism) tenet predicts that consciousness should not arise from just any complex system". Last commit f2e940da1c (2026-09-26) did not reach it. (check 140)
12. [concepts/combination-problem.md](/concepts/combination-problem/) L175 "Not a late emergence but a basic feature of reality (the Dualism tenet)". (check 140)
13. [topics/born-rule-and-the-consciousness-interface.md](/topics/born-rule-and-the-consciousness-interface/) L110 "a further question the Map answers affirmatively" (in window; re-read in full; L219 and L221 also live). (check 140)
14. [topics/brain-internal-born-rule-testing.md](/topics/brain-internal-born-rule-testing/) L157 "instrument-relative rather than principled". (check 140)
15. [topics/testing-consciousness-collapse.md](/topics/testing-consciousness-collapse/) L179 "constitutes indirect evidence that consciousness is structurally implicated". (check 140)

**Booked family, not recounted:** [concepts/implicit-memory.md](/concepts/implicit-memory/) L194 (was L196; "The simplest account that covers *all* the phenomena… treats consciousness as a causal factor"), covered by the blocked `NEEDS-HUMAN (doctrine) 2026-09-19` item.

## Priority list (capped at 4; not minted — see §Method)

| # | Locus | Tenet | Why this one |
|---|---|---|---|
| 1 | **Re-mint check 140/141's priority rows verbatim** (rows 1–3 of check 141: the four check-140 briefs; the fabricated-prediction sweep `falsification-roadmap` L173+L107, `returning-attention` L97+L39, `consciousness-and-agency` L120, `haecceity` L181, `composition-and-consciousness` L111; the Tenet-3 relocation trio `indexical-identity` L147+L161, `many-minds` L86, `quantum-consciousness` L114) | 1/2/3/4 | Fourteen ERRORs, zero tasks, five reports. The briefs are already written in checks 140 and 141 §Priority list |
| 2 | **Propagate the three tenets-only repairs**: (a) classical-menu form in `trilemma-of-selection` L129, `attention-and-the-consciousness-interface` L173, `brain-computer-interfaces` L83, `neuroplasticity` L56, `retrocausality` L155, `mind-brain-separation` L118, `phenomenology-mechanism-bridge` L59 → tenets L105 wording; (b) unconditioned scoping in `epistemology-of-mechanism` L123, `sorkin-higher-order-interference` L72, `the-steelman-for-process-monism` L75, `personal-identity` L189 → tenets L75/L81; (c) PCS roster in `integration-as-activity` L50 → drop Frankish, cite tenets L103 | 2/3 | Twelve loci from one cause: commits 3f5452f920, 71a78a577b and 9afad1f283 fixed the tenet and left (or missed) its dependents. One sweep task with the three grep keys closes all twelve; the 2026-09-27 Maier sweep (e3e689517d) is the model |
| 3 | **`wheelers` L156+L160+L142 and `binding-problem` L88/L132/L142/L210/L212** | 2/4/5 and 1/3/4 | The one new ERROR, and the one in-window file whose whole tenet section runs uncalibrated (illusionism regress-refuted, "a single subject choosing among quantum alternatives", felt global definiteness under the name of the indexical argument). Both touched 2026-09-29 |
| 4 | **Tenet sections written or touched 2026-09-28/29 that upgrade compatibility**: `mirth-void` L94, `mattering-void` L114, `intellectual-life` L184/L186/L190/L214/L218, `causal-interface` L112/L158, `infant-consciousness` L105/L107, `incubation-effect` L144/L146/L148, `correlationism` L100/L74 | 1/2/3/5 | Fresh or freshly-reviewed loci are cheapest to fix before dependents inherit them; `mirth-void` contradicts its own L38/L96, `mattering-void` contradicts its section index |

**Recommendation to the driver:** mint one `refine-draft` per row; row 1 is the three check-141 rows copied verbatim. Each brief should name the *claim*, require a same-file sibling grep before closing, and require the Hugo copy to be checked. Row 2's brief should carry the three grep keys (`presents options`, `indistinguishable from chance`, `Frankish (2016)`) so the fix is a sweep, not a per-file edit.

## Warnings

Grep-verified by the sub-sweep that read the file (one hit at the stated line); the driver independently re-verified the loci named in the priority list. Line numbers as of 2026-09-30 07:44 UTC.

### Propagation lens (tenets qualified; dependents carry the old form)
- Classical-menu form (tenets L71/L105): [topics/trilemma-of-selection.md](/topics/trilemma-of-selection/) L129; [topics/attention-and-the-consciousness-interface.md](/topics/attention-and-the-consciousness-interface/) L173; [topics/brain-computer-interfaces-and-the-interface-boundary.md](/topics/brain-computer-interfaces-and-the-interface-boundary/) L83; [concepts/neuroplasticity.md](/concepts/neuroplasticity/) L56; [concepts/retrocausality.md](/concepts/retrocausality/) L155; [concepts/mind-brain-separation.md](/concepts/mind-brain-separation/) L118; [apex/phenomenology-mechanism-bridge.md](/apex/phenomenology-mechanism-bridge/) L59 (quotes in §Summary 2). [concepts/creative-consciousness.md](/concepts/creative-consciousness/) L130 raises the menu question and answers it ("expands the menu rather than reading a pre-set one") — NOTE only.
- Unconditioned scoping (tenets L75/L81): [topics/epistemology-of-mechanism-at-the-consciousness-matter-interface.md](/topics/epistemology-of-mechanism-at-the-consciousness-matter-interface/) L123; [concepts/sorkin-higher-order-interference.md](/concepts/sorkin-higher-order-interference/) L72; [topics/the-steelman-for-process-monism.md](/topics/the-steelman-for-process-monism/) L75; [topics/personal-identity.md](/topics/personal-identity/) L189 "not a testable hypothesis" (against L81 falsifier (c)); [topics/correlationism-and-the-ancestrality-argument.md](/topics/correlationism-and-the-ancestrality-argument/) L82 "the physical world's statistics are untouched" (NOTE; L106 closer).
- PCS roster (tenets L103): [concepts/integration-as-activity.md](/concepts/integration-as-activity/) L50.

### Tenet 3 held as actual, or epiphenomenalism / illusionism reported refuted (tenets L93, L95 `^tenet-3-standing`, L101–103)
- [concepts/binding-problem.md](/concepts/binding-problem/) L88 "the illusionist faces infinite regress… Denying phenomenal unity undermines the very reasoning by which one arrives at the denial"; L210 "Unified consciousness selects, not merely observes—a single subject choosing among quantum alternatives. Fragmentary consciousness could not exercise coherent causal power".
- [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/) L135 "Eliminating the unified subject eliminates the possibility of systematic illusion" (illusionism structurally refuted; its own L123 applies the boundary discipline to Dennett only); L145 "Bidirectional interaction requires a unified agent" (carried; 5c4270dda1 scoped the diachronic half only).
- [concepts/conscious-vs-unconscious-processing.md](/concepts/conscious-vs-unconscious-processing/) L177 "consciousness must be causally efficacious for our claims about it to be trustworthy" (untouched by fed735f497, inside the recalibrated section).
- [concepts/mental-imagery.md](/concepts/mental-imagery/) L57 "consciousness is not merely observing — it is directing neural activity" (self-corrected L117/L161); L153 "These functions require conscious processing" (against the tenet's own graded comparative-cognition paragraph, L97).
- [concepts/objectivity-and-consciousness.md](/concepts/objectivity-and-consciousness/) L146 "causally efficacious (evidenced by our ability to report on phenomenal states)… which is what a two-way interaction predicts".
- [concepts/stapp-quantum-mind.md](/concepts/stapp-quantum-mind/) L104 ✔, L156 ✔ (carried; L156 "exemplifies minimal interaction" now against its own L124–126 back-action section and L66 classification).
- [topics/anaesthesia-and-the-consciousness-interface.md](/topics/anaesthesia-and-the-consciousness-interface/) L79 self-stultification as refutation.
- [topics/curated-mind.md](/topics/curated-mind/) L105 "The bidirectional channel has different bandwidths in each direction" (meditation/mirror-therapy effects as Tenet 3 in operation); L107.
- [topics/diachronic-agency-and-personal-narrative.md](/topics/diachronic-agency-and-personal-narrative/) L129 "Each choice in a sustained project is an instance of consciousness selecting among physical possibilities".
- [topics/incubation-effect-and-unconscious-processing.md](/topics/incubation-effect-and-unconscious-processing/) L144 "it is necessary for it" (self-corrected L117/L119); L148 "the evidence suggests genuine selection… empirically observable".
- [topics/phenomenology-of-imagination.md](/topics/phenomenology-of-imagination/) L72 "reflects consciousness doing active work" (sibling of the repaired L118).
- [topics/phenomenology-of-intellectual-life.md](/topics/phenomenology-of-intellectual-life/) L186 "the phenomenal work of inference does causal work on which states become actual"; L190 bare seeming-regress against illusionism; L214 "gains support from the causal efficacy of intellectual effort… would be inexplicable"; L235 navigation label.
- [topics/predictive-processing-and-dualism.md](/topics/predictive-processing-and-dualism/) L104 "Consciousness acts on the brain itself by influencing which neural possibilities are realised"; L152 "consciousness changes the brain's state by influencing precision weighting" (self-corrected later in the paragraph).
- [topics/motor-control-quantum-zeno.md](/topics/motor-control-quantum-zeno/) L127 ✔ (carried); [topics/the-interface-problem.md](/topics/the-interface-problem/) L63 ✔ (carried, corrected by L67); [topics/philosophy-of-habit-under-dualism.md](/topics/philosophy-of-habit-under-dualism/) L83 ✔, L87 ✔ (carried; survived the 09-29 deep review); [concepts/implicit-memory.md](/concepts/implicit-memory/) L3 ✔, L41 ✔, L83 ✔, L115 ✔, L185 ✔ (carried).
- [voids/mirth-void.md](/voids/mirth-void/) L94 "Consciousness *causes* laughter but cannot *order* it… The Map reads this as support for its picture of the interface as narrow and selective" (against its own L38 and L96); [voids/infant-consciousness.md](/voids/infant-consciousness/) L107 "a different *mode of interaction* between consciousness and matter — one that operated through a neural substrate we no longer possess".

### Compatibility upgraded to support, evidence or prediction (evidential-status discipline; tenets L55, L81, L93)
- [concepts/galilean-exclusion.md](/concepts/galilean-exclusion/) L92 "the failure of that method to explain subjectivity is not surprising — it is expected"; L94 "implies that the exclusion… leaves *physics* incomplete in domains where consciousness acts"; L96 "Genuine parsimony requires accounting for all the phenomena" — **covered by the queued P1** (synthesis cluster 6).
- [concepts/binding-problem.md](/concepts/binding-problem/) L132 "This supports the view that phenomenal unity isn't *produced by* binding operations but *added* by consciousness"; L142 "Phenomenal unity is contributed by consciousness, not constructed by brain processes".
- [concepts/conscious-vs-unconscious-processing.md](/concepts/conscious-vs-unconscious-processing/) L117 "if overflow is real, it strengthens the dualist position" (Block/Lamme overflow is a physicalist position, its own L111).
- [concepts/objectivity-and-consciousness.md](/concepts/objectivity-and-consciousness/) L84 "Bidirectional causation without bidirectional measurability is what a dualist framework predicts" (self-corrected L122); L150 "observer-independent description fails at the most fundamental physical level" (against posit 2, tenets L125/L184).
- [concepts/swampman.md](/concepts/swampman/) L87 "the Map's first tenet, Dualism, where it is most specific about content" (Tenet 1 says nothing about content; sibling `teleosemantics` L28).
- [topics/anaesthesia-and-the-consciousness-interface.md](/topics/anaesthesia-and-the-consciousness-interface/) L143 "Evidence comes from two directions" (against its own L53/L137).
- [topics/consciousness-defeats-explanation.md](/topics/consciousness-defeats-explanation/) L158 "supports the claim that consciousness is irreducible" (against its own L140).
- [topics/incubation-effect-and-unconscious-processing.md](/topics/incubation-effect-and-unconscious-processing/) L146 "difficult to explain if phenomenal properties reduce to neural properties".
- [topics/modal-structure-of-phenomenal-properties.md](/topics/modal-structure-of-phenomenal-properties/) L3 "supporting dualism through converging modal arguments" (against its own L36/L107).
- [topics/the-interface-problem.md](/topics/the-interface-problem/) L159 ✔ "gains qualified support from dopamine research" (carried).
- [voids/mattering-void.md](/voids/mattering-void/) L114 "The Map interprets the mattering void as primary evidence for **Dualism**" (against [voids/voids.md](/voids/) L147).
- [voids/causal-interface.md](/voids/causal-interface/) L158 "Minimal Quantum Interaction predicts this void… A minimal mechanism would leave minimal traces" (also the sensitivity-limit reading, tenets L75); L110 "to remain below experimental detection thresholds".
- [voids/infant-consciousness.md](/voids/infant-consciousness/) L105 "Bidirectional Interaction implies that infant consciousness… interacts with the physical world in different ways".
- [voids/predictive-construction-void.md](/voids/predictive-construction-void/) L129 "statistical deviations from standard measurement predictions… would be expected under bidirectional influence" (unscoped; [P-Q3](/positions/quantum-interface/#p-q3)).
- [apex/taxonomy-of-voids.md](/apex/taxonomy-of-voids/) L95 "the predictive work is done by the full package" (hedged L171).

### Family I: felt definiteness cited against MWI, or quick "nothing to select" (tenets L117, L121, L184 posit 3)
- [concepts/binding-problem.md](/concepts/binding-problem/) L212 "*this* definite experience requires genuine collapse rather than branch-relative definiteness" (attributed to the indexical argument).
- [concepts/stapp-quantum-mind.md](/concepts/stapp-quantum-mind/) L164 ✔ (carried).
- [topics/consciousness-and-cognitive-distinctiveness.md](/topics/consciousness-and-cognitive-distinctiveness/) L188 "Many-worlds eliminates this distinction. The phenomenology of creative choice… presupposes that possibilities were genuinely narrowed" (compare the calibrated `diachronic-agency` L133).
- [topics/modal-structure-of-phenomenal-properties.md](/topics/modal-structure-of-phenomenal-properties/) L115 "require a single actual world in which determinate experiences occur" (unscoped).
- [topics/personal-identity.md](/topics/personal-identity/) L53 Tenet 4 "commits the Map to a view where personal identity is real" (direction inverted against tenets L121; sibling L193; partly corrected L81).
- [topics/phenomenology-of-intellectual-life.md](/topics/phenomenology-of-intellectual-life/) L218 "The felt singularity of \"I grasped this\" lacks a natural referent".
- [topics/predictive-processing-and-dualism.md](/topics/predictive-processing-and-dualism/) L154 "implies a singular perspective branching universes cannot ground".
- [topics/time-symmetric-selection-mechanism.md](/topics/time-symmetric-selection-mechanism/) L214 "MWI eliminates what the model requires" (new; branch-relative selection not addressed).
- [topics/vertiginous-question.md](/topics/vertiginous-question/) L161 "suggests an indexical fact that branch-egalitarian MWI cannot accommodate" (scoped; mild). The List (2023) boundary at L165/L189 is handled correctly.
- [topics/wheelers-participatory-universe-and-it-from-bit.md](/topics/wheelers-participatory-universe-and-it-from-bit/) L160 Wheeler's "untestability and ontological excess" shared, indexical objection merely added; "requires that observation produces a single definite outcome, not a branching".
- [topics/motor-control-quantum-zeno.md](/topics/motor-control-quantum-zeno/) L129 ✔, [topics/the-interface-problem.md](/topics/the-interface-problem/) L161 ✔ (carried).

### Tenet 1 glossed as substance dualism (tenets L53/L57) or fundamentality (L53)
- Substance: [topics/correlationism-and-the-ancestrality-argument.md](/topics/correlationism-and-the-ancestrality-argument/) L100 "the tenet posits two terms, each existing apart from the other", L74; [topics/brain-specialness-boundary.md](/topics/brain-specialness-boundary/) L63 "the substance dualism of the Map's first tenet" (L158 self-corrected at L110/L120); [topics/diachronic-agency-and-personal-narrative.md](/topics/diachronic-agency-and-personal-narrative/) L127 (NOTE). None cites `where-the-substance-commitment-enters`.
- Fundamentality: [voids/three-kinds-of-void.md](/voids/three-kinds-of-void/) L103 "If consciousness is fundamental and irreducible", L65; [voids/voids.md](/voids/) L313 same gloss plus "where materialist explanation ends" (against tenets L59), L90; [topics/consciousness-defeats-explanation.md](/topics/consciousness-defeats-explanation/) L110 (NOTE).

### Tenet 5: parsimony as verdict, or Tenet 5 misgrounded (tenets L69, L145, L147)
- [voids/causal-interface.md](/voids/causal-interface/) L112 "This is not conspiracy but parsimony… The opacity is a consequence of the minimality" (Tenet 2's minimality as parsimony, against L69).
- [apex/taxonomy-of-voids.md](/apex/taxonomy-of-voids/) L197 "the Map's reading is the simpler accommodation when the across-condition direction is matched".
- [topics/phenomenology-of-intellectual-life.md](/topics/phenomenology-of-intellectual-life/) L184 "The more parsimonious view: the phenomenology of intellectual life is what it is *like* to think".
- [concepts/teleosemantics.md](/concepts/teleosemantics/) L92 ✔ (carried; Tenet 5 as "the limits of reduction"); [topics/motor-control-quantum-zeno.md](/topics/motor-control-quantum-zeno/) L131 ✔ (carried); [concepts/coupling-modes.md](/concepts/coupling-modes/) L82 (NOTE; self-corrected L126); [concepts/stapp-quantum-mind.md](/concepts/stapp-quantum-mind/) L168 (NOTE).

### Tenet 2: coherence dependence, mechanism as fact, minimality misread (tenets L69, L71, L77)
- [topics/wheelers-participatory-universe-and-it-from-bit.md](/topics/wheelers-participatory-universe-and-it-from-bit/) L142 coherence obstacle "presses on any framework, the Map's included" (self-corrected same paragraph).
- [topics/the-interface-problem.md](/topics/the-interface-problem/) L147 ✔ coherence closure as falsifier (carried).
- [topics/born-rule-and-the-consciousness-interface.md](/topics/born-rule-and-the-consciousness-interface/) L165 ranks readings by minimality (NOTE); L167/L170/L207 taxonomy inconsistency (carried NOTE).
- [topics/brain-specialness-boundary.md](/topics/brain-specialness-boundary/) L128 two-horn dilemma omits the Map's actual unconditioned/conditioned position (NOTE).
- [concepts/binding-problem.md](/concepts/binding-problem/) L208 "Quantum collapse provides a mechanism for BP2" (NOTE; coherence-dependent line).
- [concepts/conscious-vs-unconscious-processing.md](/concepts/conscious-vs-unconscious-processing/) L245 tenet "locates this interface at… attention-related neural systems", L247 Zeno "doesn't require sustained coherence" (NOTEs; against tenets L71/L77 and `coupling-modes` L112).
- [concepts/stapp-quantum-mind.md](/concepts/stapp-quantum-mind/) L66 ✔ Stapp classified Born-rule-bending only (carried; `process-1-specification-problem` L89 supplies the two-register fix), L120 ✔ (carried, against L184).

### Carried and still live (files not committed this window; live by construction)
- Every locus in check 141 §Warnings whose file had no commit since 2026-09-28 12:20 UTC, including Family S in the attention/effort wing (`apex/attention-as-causal-bridge`, `concepts/attentional-economics`, `topics/structure-of-attention`, `topics/trilemma-of-selection`, `topics/authentic-vs-inauthentic-choice`), the check-139 `concepts/dualism` L172/L154/L130/L180 set, `concepts/causal-closure` L120/L136/L172/L196/L198, `concepts/ensemble-level-epiphenomenalism` L61 (Maier residue), and the check-141 borderline items (`mathematical-structure` L89/L92/L154, `multi-mind-collapse-problem` L129, `tenet-generated-voids` L77).
- **Carried loci in files committed this window, re-probed and still live:** `born-rule` L110/L219/L221; `stapp-quantum-mind` L66/L104/L120/L156/L164; `teleosemantics` L92; `unity-of-consciousness` L145; `implicit-memory` L3/L41/L83/L115/L185/L194; `motor-control-quantum-zeno` L127/L129/L131; `the-interface-problem` L63/L147/L159/L161; `philosophy-of-habit-under-dualism` L83/L87; `confabulation-void` L105 (was L104; three commits since check 140 did not touch it).

## Notes

- [topics/personal-identity.md](/topics/personal-identity/) L85 quotes retired tenet wording ("unanswerable indexical questions: why am I *this* instance and not another?" — absent from `tenets.md` today, removed in 1f743e48ee); L191 Tenet 3 as actual premise outside the L173 disclaimer's section.
- [concepts/narrative-coherence.md](/concepts/narrative-coherence/) L35 "evidence that the substantial self is more than a philosophical postulate" vs its own L79 "not the evidence that there is a subject" — lead and Strawson section disagree; L79 is the calibrated one.
- [concepts/objectivity-and-consciousness.md](/concepts/objectivity-and-consciousness/) L120 glosses Tenet 4's Rules-out as "eliminate genuine selection" (corrected L122); L152 "features of reality itself".
- [concepts/mental-imagery.md](/concepts/mental-imagery/) L171 "instantiates the bidirectional flow the Map posits"; L139 cognitive phenomenology "reinforces the case for bidirectional interaction" (against its own L145).
- [concepts/coupling-modes.md](/concepts/coupling-modes/) L86 indistinguishability unscoped (partly restored L134); L164 presupposes Tenet 3 to score parsimony; L146 "decoherence-selected alternatives".
- [concepts/apophatic-cartography-four-criteria.md](/concepts/apophatic-cartography-four-criteria/) L126 parsimony-temptation gloss (confirmation-counting, not Tenet 5).
- [concepts/conscious-vs-unconscious-processing.md](/concepts/conscious-vs-unconscious-processing/) L46 lead still runs the modus tollens the body retracts (corrected L48); L207 unfalsifiability as evidence; L255 Tenet 5 as verdict; L274 navigation label "why it fails".
- [concepts/implicit-memory.md](/concepts/implicit-memory/) L117, L141 (Tallis; citation lens), L208/L210 navigation labels.
- [concepts/swampman.md](/concepts/swampman/) L71 "nomologically impossible" (corrected L89). [concepts/teleosemantics.md](/concepts/teleosemantics/) L28 Tenet 1 "requires" rational normativity.
- [concepts/stapp-quantum-mind.md](/concepts/stapp-quantum-mind/) L142 illusionism regress; L168 parsimony near-verdict.
- [topics/born-rule-and-the-consciousness-interface.md](/topics/born-rule-and-the-consciousness-interface/) L165 (above). [topics/brain-specialness-boundary.md](/topics/brain-specialness-boundary/) L128 (above). `topics/correlationism` L82.
- [topics/consciousness-defeats-explanation.md](/topics/consciousness-defeats-explanation/) L90 heterophenomenology "presupposes… the phenomenal capacity it denies"; L110 fundamentality; L160 "what consciousness does".
- [topics/diachronic-agency-and-personal-narrative.md](/topics/diachronic-agency-and-personal-narrative/) L73 no-self answered by phenomenology (tenets L121: bedrock disagreement); L127.
- [topics/hard-problem-of-consciousness.md](/topics/hard-problem-of-consciousness/) L174 (corrected L247); L176 PCS verdict where tenets L103 holds it open.
- [topics/indian-philosophy-of-mind.md](/topics/indian-philosophy-of-mind/) L151 Nyāya "support" without the common-cause caveat L147/L155 carry.
- [topics/modal-structure-of-phenomenal-properties.md](/topics/modal-structure-of-phenomenal-properties/) L95 "how each PCS version fails"; L117 "modal evidence".
- [topics/motor-control-quantum-zeno.md](/topics/motor-control-quantum-zeno/) L125 "exemplifies" (corrected by "would"). [topics/phenomenology-of-imagination.md](/topics/phenomenology-of-imagination/) L118 "exemplifies" (corrected same paragraph).
- [topics/the-naturalisation-failure-for-content.md](/topics/the-naturalisation-failure-for-content/) L143 "could not anchor content"; L123 "shows… cannot be coherently asserted".
- [topics/the-subject-object-distinction-as-philosophical-discovery.md](/topics/the-subject-object-distinction-as-philosophical-discovery/) L111 (corrected L65).
- [voids/assent-void.md](/voids/assent-void/) L107 Tenet 5 as introspective-simplicity claim. [voids/confabulation-void.md](/voids/confabulation-void/) L107 "small-quantum-amplification work". [voids/cross-state-void.md](/voids/cross-state-void/) L93 "evidence that the felt component does causal work" (corrected in the same sentence-group). [voids/mattering-void.md](/voids/mattering-void/) L116. [voids/causal-interface.md](/voids/causal-interface/) L156 (corrected same paragraph). [voids/necessary-opacity.md](/voids/necessary-opacity/) L156 "affects quantum probabilities at femtosecond… scales". [voids/three-kinds-of-void.md](/voids/three-kinds-of-void/) L73 Tenet 2 as reality's "immune system" (self-labelled speculative). [voids/voids.md](/voids/) L302 index blurb "evidence" where the article says "reading".
- [apex/taxonomy-of-voids.md](/apex/taxonomy-of-voids/) L95 (hedged L171).
- **Carried:** tenets.md L159 still points at `[[apex/machine-question]] §senses of conscious`. Not re-probed this window.

## Files passing all checks (22)

- [concepts/affective-forecasting-gap.md](/concepts/affective-forecasting-gap/)
- [concepts/buddhism-and-dualism.md](/concepts/buddhism-and-dualism/)
- [concepts/chinese-room-argument.md](/concepts/chinese-room-argument/)
- [concepts/content-externalism.md](/concepts/content-externalism/)
- [concepts/content-vocabulary-as-derived-feature.md](/concepts/content-vocabulary-as-derived-feature/)
- [concepts/direction-of-interface-change.md](/concepts/direction-of-interface-change/)
- [concepts/process-1-specification-problem.md](/concepts/process-1-specification-problem/) (new)
- [concepts/pudgalavada.md](/concepts/pudgalavada/)
- [concepts/where-the-substance-commitment-enters.md](/concepts/where-the-substance-commitment-enters/)
- [positions/agency-and-will.md](/positions/agency-and-will/)
- [topics/constitutive-exclusion.md](/topics/constitutive-exclusion/) (after 1e60bfc6f6)
- [topics/phenomenology-of-cognitive-limit-types.md](/topics/phenomenology-of-cognitive-limit-types/)
- [voids/assent-void.md](/voids/assent-void/) (new; one NOTE)
- [voids/blindspot-void.md](/voids/blindspot-void/) (new; after c1c20cd5ca)
- [voids/categorical-perception-void.md](/voids/categorical-perception-void/) (new)
- [voids/causal-impression-void.md](/voids/causal-impression-void/) (new)
- [voids/closure-types-void.md](/voids/closure-types-void/)
- [voids/handedness-void.md](/voids/handedness-void/) (new)
- [voids/intrinsic-nature-void.md](/voids/intrinsic-nature-void/) (after f78da095ab)
- [voids/mutation-void.md](/voids/mutation-void/)
- [voids/necessary-opacity.md](/voids/necessary-opacity/) (after aebfc92ff7; one NOTE)
- [voids/taboo-void.md](/voids/taboo-void/) (new)

[tenets/tenets.md](/tenets/) had no commit this window; L49–147 and L182–186 were re-read and are internally consistent.

## Method

1. Read `tenets.md` L49–147 and L182–186 (definitions, rationales, qualifiers, Rules-out clauses, background posits). No commit since check 141.
2. Listed every file in `topics/ concepts/ positions/ apex/ voids/ tenets/` with a commit since 2026-09-28 12:20 UTC (70 files). Five parallel sub-sweeps read each file in full and reported loci in a fixed format with an exact quote each, grep-verified at the stated line; the driver waited for all five in the foreground and folded their results in before writing. The driver independently re-verified the new ERROR, all fourteen carried ERRORs, and every locus named in the priority list by exact substring (the three wikilink-formatted lines by their plain-text tail).
3. Propagation lens: `git log` on `tenets.md` for September identified five qualifying commits (3f5452f920 menu analogy, 71a78a577b unconditioned, 9afad1f283 PCS roster, e3e689517d Maier, and the L117 scoping); `git show --stat` established which touched only the tenets page; corpus-wide greps for each old form were adjudicated line by line.
4. Cross-referenced today's synthesis cluster 6 and the Active section of `todo.md`; the `galilean-exclusion` tenet-section loci and the co-optation-roster / over-reach lens are recorded as covered by queued P1s, not duplicated. Confirmed no task references check 140 or 141.
5. No content file was modified. **No task was minted**: the skill's contract ("only creates report files and updates changelog") does not extend to `todo.md`, so the four priority rows above are left as ready-to-copy briefs for the driver.

## Scope confirmation

All 70 files with a commit since check 141 were read in full; none was skipped or sampled. Files outside the window were probed by exact string only (the carried ERRORs, and the propagation-lens greps across every section), and are reported as carried or as out-of-window grep hits, never as fresh reads.