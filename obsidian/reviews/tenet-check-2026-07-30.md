---
title: "Tenet Alignment Check - 2026-07-30"
description: "The corpus still passes on the classic reading. The new finding: the conceivability cluster has never been swept against the dependency-matrix row added two days ago, and runs Tenets 3 and 4 as inheritance."
created: 2026-07-30
modified: 2026-07-30
human_modified: null
ai_modified: 2026-07-30T23:40:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[tenets]]"
  - "[[concepts/philosophical-zombies]]"
  - "[[concepts/zombie-master-argument]]"
  - "[[concepts/inverted-qualia]]"
  - "[[topics/personal-identity]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-07-30
last_curated: null
last_deep_review: null
---

# Tenet Alignment Check

**Date**: 2026-07-30 (23:40Z)
**Scope**: All five tenets, all three trees (`obsidian/`, `archive/`, `hugo/content/`).
**Predecessor**: `reviews/tenet-check-2026-07-29b.md` (23:55Z, ~23h ago). This pass (a) re-verifies its 22 error loci against current disk, (b) applies one lens no tenet-check has used before — the **tenet-dependency matrix** at `tenets/tenets.md` L152–174, whose conceivability-arguments row was added 2026-07-28 and has never been swept against the cluster it governs.
**Files checked**: 799 obsidian article-tree files (`topics/` 319, `concepts/` 318, `voids/` 101, `apex/` 40, `arguments/` 6, `positions/` 12, `questions/` 1, `tenets/` 2), 510 archive files, 8957 hugo files.
**Errors**: 18 loci across 16 files (plus Family D, enumerated separately)
**Warnings**: 6
**Notes**: 7
**False-positive rate on inspected candidates**: ~90% (see "Patterns Run", below)

## Summary

**The corpus still passes on the classic reading. No direct contradiction of any tenet exists in the Map's own voice.** This finding is re-verified, not inherited. I ran ten direct-contradiction patterns across all three trees and read every obsidian article-tree hit — 61 loci for Tenets 1, 3 and 4, and 7 for Tenet 2. **Zero** endorse eliminative materialism, illusionism about phenomenal consciousness, epiphenomenalism, MWI, quantum mysticism, psychokinesis or energy injection. Every hit is exposition-to-refute, an attributed third-party claim, a conditional antecedent ("If consciousness is epiphenomenal, …"), or a definition being set up for rejection. The predecessor's identical finding holds and should be preserved.

**A1 and A2 are closed and are not re-reported.** The 07-29b claim that both parsimony authority files carry "zero self-binding" was false when written; `concepts/parsimony-epistemology.md` L164 now closes with *"This page's claim stays defensive, as the fifth tenet requires: parsimony lacks the standing to settle the question in either direction"*, and `arguments/epistemological-limits-of-occams-razor.md` L94 has read *"This article makes the defensive case: parsimony cannot settle the consciousness debate"* throughout. A2 is a model, not a defect. One residue survives at A1 and is reported below as a **single-sentence internal contradiction**, quoted verbatim with its line number, which is the gate the driver set.

**The new finding is structural, and it is a scope gap rather than a regression.** `tenets/tenets.md` gained a conceivability-arguments row in its dependency matrix on 2026-07-28 (L160, L168). That row marks the quantum tenets and No-Many-Worlds **not invoked** for the zombie / knowledge-argument / explanatory-gap / inverted-qualia cluster, and states the discipline explicitly: *"a No-Many-Worlds subsection in a cluster article should read as an intra-framework coherence remark rather than as inheritance in either direction."* Four of the five cluster articles have "Relation to the Map's Perspective" subsections that run exactly the inheritance the row forbids. Of the five, only `concepts/inverted-qualia.md` carries a coherence marker; the other four score **zero**. The matrix was written; the cluster was never brought to it.

## Patterns Run (so the next pass can diff pattern-vs-enumeration)

Per-tree hit counts, `grep -rniE`, `--include='*.md'`. Article-tree scope for obsidian excludes `workflow/`, `reviews/`, `project/`, `research/`; hugo counts include `reviews/` and are therefore inflated by this report's own predecessors.

| # | Pattern | obs | arch | hugo | survived inspection |
|---|---|---|---|---|---|
| T1a | `consciousness is (just\|merely\|nothing but\|simply\|only) (neur\|brain\|comput\|inform\|physical\|matter)` | 11 | 5 | 54 | 0 |
| T1b | `consciousness is nothing over and above` | 0 | 2 | 7 | 0 |
| T1c | `consciousness (is\|can be) (fully \|wholly \|completely )?reducible to` | 3 | 3 | 10 | 0 |
| T1d | `consciousness is an illusion\.` / `qualia (do not\|don't) exist\.` | 4 | 2 | 10 | 0 |
| T2a | `(evidence for\|supports?\|establishes\|demonstrates) (macroscopic )?psychokinesis` | 0 | 0 | 0 | 0 |
| T2b | `(inject\|add\|supply\|impart)(s\|ing\|ed)? energy (into\|to) the (brain\|physical\|neural)` | 1 | 4 | 6 | 0 |
| T2c | `(would be\|is) empirically detectable` / `measurable (mind-matter\|psychokinetic) (effect\|influence)` | 4 | 4 | 20 | 0 |
| T2d | `proof that (evolution\|biology\|nature)` / `demonstrably survives` / `proves that quantum` | 2 | 3 | 15 | 3 |
| T3a | `consciousness is (indeed \|in fact )?epiphenomenal` / `the Map (accepts\|endorses\|adopts) epiphenomenalism` | 23 | 10 | 76 | 0 |
| T3b | `consciousness is (merely \|just )?along for the ride` | 3 | 2 | 11 | 1 |
| T4a | `(the Map\|we) (accept\|endorse\|adopt\|prefer)s? (the )?many.worlds` / `many.worlds is (correct\|true\|the best)` | 0 | 2 | 14 | 0 |
| T4b | `all branches are equally real` | 17 | 17 | 62 | 0 |
| T5a | `more parsimonious` | 36 | 21 | 167 | 3 |
| T5b | `parsimon(y\|ious) (favours\|favors\|supports\|tells\|points)` | 9 | 6 | 65 | 2 |
| T5c | `tie.?breaker` | 16 | 7 | 73 | 2 |
| T5d | `the simpler (theory\|explanation) is (therefore \|thus )?(more likely\|probably\|the) (true\|truer\|correct)` | 1 | 0 | 2 | 0 |
| D1 | `subject to whom it seems` | 4 | 0 | 4 | 2 |
| D2 | `something must .{0,40}(experienc\|conscious\|seem\|generat)` | 48 files | 28 files | — | 8 |
| M | matrix lens: `no.many.worlds\|minimal quantum interaction\|bidirectional interaction` within the conceivability cluster, then read in full | 5 files | — | — | 4 |

Three methodological notes on the patterns themselves.

**The A1/A2 lesson generalises, and it changed my results.** The predecessor's `veto|run forward|binds the Map|does not license` returns 0 on both authority files; `cannot settle|does not settle|category error|not the whole of|defensive case` returns 6 and 4. I therefore built every calibration test out of the vocabulary the *target file's author* would use, not the vocabulary of a fix. The clearest payoff is Family D: my calibration marker was `functional-seeming|Frankish|quasi-phenomenal|proves nothing|does not settle|relocat`, which correctly cleared `concepts/jourdain-hypothesis.md` (calibrated in the line immediately after the hit) and `topics/the-self-minimal-narrative-and-substantial.md` L103 (*"the regress is pressing but not, on its own, decisive"*) — both of which a fix-vocabulary grep would have reported as defects.

**Family D's two phrasing families are disjoint, as recorded, and both are incomplete.** I ran both. D1 (`subject to whom it seems`) returns 4 obsidian article loci; D2 returns 48 obsidian article files. Neither surfaces the other's loci. Today's `/pessimistic-review` (02:5xZ, `reviews/pessimistic-2026-07-30-mysterianism.md` L197) enumerated 15 D2 loci with a ±5-line calibration window; my file-scoped window found **48 files**, of which 11 have no calibration marker anywhere in the file. The family is larger again than either enumeration.

**False-positive rate: ~90%.** Of roughly 118 obsidian article-tree candidates inspected, 11 survived. Broken down: direct-contradiction patterns (T1/T3/T4, 61 candidates) — **100% false**, which is the headline finding rather than a failure of the patterns. T5a `more parsimonious` (36 candidates) — 92% false; the corpus uses the phrase overwhelmingly for historical counterexamples, steelmen of rivals, and explicit Tenet-5 self-binding. Family D2 zero-marker list (11 candidates) — **55% false**; six were not the regress at all (`something must break this symmetry`, `something must select the outcome`, Epicurus on death) or were calibrated in adjacent prose. Family D1 (3 new candidates) — 67% false. **Do not act on any locus list below without reading the line.**

## Errors

### Family M — the conceivability cluster has never met its own matrix row (NEW)

Governing text, `tenets/tenets.md` L168: *"Interactionism is accordingly not merely unneeded here but downstream—a cluster article that imports mental causation as background has borrowed a commitment that, at the stage its own argument occupies, would dissolve the thought experiment. … No-MWI is not invoked either … determinate first-person phenomenal facts are available branch-relatively … so whether the unchosen alternatives occur elsewhere leaves the conceivability of a zombie twin or an inverted spectrum untouched."*

The model is on disk twice. `concepts/zombie-master-argument.md` L112: *"The zombie argument does its work under *minimal dualism* — Tenet 1 alone — where the only claim is that consciousness is not entailed by physical facts."* And `concepts/inverted-qualia.md` L181, the only cluster article that gets the No-MWI cell right: *"An Everettian grants that much branch-locally—each branch-relative subject has a definite indexical experience … What branching does not supply is that the alternatives fail to occur *anywhere*, and that global exclusion is a [[tenets/background-commitments|posit the Map adopts]] rather than a deliverance of indexical experience. The disagreement sits at the framework boundary."*

**M1. `obsidian/concepts/philosophical-zombies.md` L203** (live at `hugo/content/concepts/philosophical-zombies.md` L205) — Tenet 3 run as inheritance, in the direction the matrix says dissolves the thought experiment.
> "**Bidirectional Interaction**: If consciousness causes our reports about consciousness, this causal role distinguishes us from zombies. The physicalist who reasons about their own experience presupposes exactly the causal efficacy of consciousness that the zombie argument vindicates."

The same file already knows better at L163: *"The interactionist's honest reply is to reject the stipulation. If consciousness genuinely causes reports (per Bidirectional Interaction), then a being physically identical to a conscious human *cannot* produce identical reports without consciousness."* L203 then claims the argument *vindicates* the commitment that L163 says makes its own subject impossible. Internal contradiction, not merely uncalibrated inheritance. Fix: import the L112 formula from `zombie-master-argument.md` and mark the subsection as coherence commentary. **Length: 3531 words, `hard_warning` against the concepts 3500 ceiling — substitution-only.**

**M2. `obsidian/concepts/philosophical-zombies.md` L207** (hugo L209) — Tenet 4 run as inheritance, contradicting the matrix directly.
> "The zombie argument requires determinate facts—*this* being is either conscious or not. … under MWI, the notion of a *specific* duplicate dissolves into a branching tree where every quantum outcome is realised. This doesn't refute the zombie argument, but it pressures the metaphysical framework the argument relies on: definite identity, definite physical facts, and a single actual world. The Map's rejection of many-worlds preserves these conditions."

`tenets.md` L168 says the opposite in terms: branch-relative determinacy is available, so MWI *leaves the conceivability of a zombie twin untouched*. The article asserts the argument "relies on" a single actual world. `inverted-qualia.md` L181 is the same subsection done correctly.

**M3. `obsidian/concepts/explanatory-gap.md` L191** — noted at 07-29b, still present, and now an error rather than a note because the matrix row is on disk.
> "Rejecting Many-Worlds means accepting genuine selection—which consciousness may perform, even if we cannot explain how."

Straight inheritance in a cell marked not-invoked. **Length: 3538 words, `hard_warning` — substitution-only.**

**M4. `obsidian/concepts/knowledge-argument.md` L167** — Tenet 3 inheritance in the Mary's-Room article (NEW).
> "If consciousness were causally inert, Mary couldn't form beliefs about her new experiences. But she does—she reports that seeing red is revelatory. Her phenomenal states causally influence her beliefs. Consciousness isn't just correlated with physical processes; it participates in the causal order."

Three flat assertions of mental causation as a *conclusion the knowledge argument supports*. The matrix marks interactionism **not invoked** for this row. Length 2619 words, `soft_warning` — ample room. (This locus also uses the "isn't just X; it participates in Y" shape that `CLAUDE.md` bans.)

### Family A — Tenet 5 parsimony run forward (5 loci still open from 07-29b, all re-verified on disk today)

**A1-residue. `obsidian/concepts/parsimony-epistemology.md` L140** — the one sentence that survives, and it now contradicts the file's own calibrated close at L164.
> "Ontological parsimony still favours physicalism, but on explanatory adequacy — the dimension most relevant to consciousness — dualism has the advantage; the [[parsimony-case-for-interactionist-dualism|positive parsimony case]] develops this systematically."

L164 was calibrated today (commit `0b67e721c`) to *"This page's claim stays defensive, as the fifth tenet requires."* L140 privileges a dimension by fiat and scores dualism ahead on it in the Map's own voice, 24 lines earlier. The fix is a scoping edit at L140, not a re-opening of the family — and it is the only A1 locus. **Do not re-report the rest of A1, and do not touch A2, which is the model.**

**A3. `obsidian/concepts/reductionism.md` L188** — unchanged. "Physicalism wins on ontological parsimony (one substance type) but loses on explanatory simplicity". Redefine-and-score. The very next sentence of the same paragraph is calibrated (*"parsimony cannot serve as a tie-breaker"*), so this is one clause out of step.

**A4. `obsidian/concepts/dualism.md` L173** — unchanged. "Moreover, ontological parsimony favours physicalism, but explanatory parsimony favours dualism". Bare Map-voice verdict on the flagship dualism page, plus the too-strong rule "Parsimony arbitrates between theories of *equal* explanatory power."

**A5. `obsidian/concepts/geometric-model-of-mind.md` L113** — unchanged. "the Map because parsimony favours the smallest non-physical influence consistent with the tenets". `tenets.md` L68 exists to forbid exactly this: Tenet 2's minimality is *empirical-constraint* minimality, not truth-tracking. **Archive sibling**: `archive/topics/duch-neurodynamic-theory-of-mind.md` L104 carries the same paragraph.

**A6. `obsidian/topics/biological-computationalisms-inadvertent-case-for-dualism.md` L100** — unchanged. "once all explanatory costs are tallied, interactionist dualism emerges as the more parsimonious position", stated in Map voice where the cited source states it as its own contention.

**A7. `obsidian/topics/the-convergence-argument-for-dualism.md` L177** — unchanged. "physicalism's parsimony advantage is outweighed by its explanatory disadvantage", plus the tiebreaker rule.

### Family B — Tenet 2: precedent-as-licence, and one overshoot (archive tree adds two loci)

**B2. `obsidian/concepts/prebiotic-collapse.md` L150** — unchanged from 07-29b.
> "Avian magnetoreception maintains spin coherence for microseconds in warm biological tissue—proof that evolution can optimise systems to exploit quantum effects despite thermal noise. If birds can do it for navigation, neural systems might do it for consciousness."

`tenets.md` L78: *"This establishes a biological *precedent* rather than a licence for neural coherence."* `positions/quantum-interface.md` P-Q8 names the drift class.

**B2-archive. `archive/topics/collapse-before-minds.md` L137** — the identical sentence, on a full serving body at a preserved URL (NEW). A fix confined to `obsidian/` leaves this live.

**B2-archive-2. `archive/concepts/quantum-biology.md` L75** (NEW) — the same overshoot in stronger terms: *"This is the strongest evidence that evolution can optimise biological systems for quantum-coherent function."*

**B4. `obsidian/concepts/quantum-interpretations.md` L104** — unchanged. "The Map is compatible with either 'consciousness causes collapse' or 'consciousness modulates collapse.'" Contradicted by `concepts/prebiotic-collapse.md` L164 and `concepts/many-worlds.md` L159, and overshoots Tenet 2, which commits to biasing indeterminate outcomes, not triggering collapse.

**B5. `obsidian/concepts/mind-matter-interface.md` L146** — unchanged (warning at 07-29b, promoted here because the archive siblings show the family is corpus-wide). "Quantum coherence demonstrably survives in warm biological systems", with no precedent-not-licence qualifier, while L144 of the same file is exemplary.

### Family C — Tenet 3 factive register at closing-synthesis loci (4 of 10 still open)

The two headline loci from 07-29b are **fixed**: `concepts/self-stultification.md` L191 and `topics/self-stultification-as-master-argument.md`'s "demonstrate its falsity" are both gone. Four remain, all re-verified on disk:

- **`obsidian/concepts/causal-closure.md` L185** — "**Consciousness reporting** shows that mental states influence physical behavior." `tenets.md` L92: the conversation *suggests* downward causation, and Tenet 3 is held "*not* as a directly introspectible datum". Ground 3 of the same list is correctly calibrated, so this is one item out of step.
- **`obsidian/concepts/working-memory.md` L171** — "WM manipulation demonstrates downward causation."
- **`obsidian/apex/minds-without-words.md` L115** — "Pain asymbolia demonstrates that phenomenal properties do real causal work". Contradicts the same file's constrain-vs-establish discipline at L137.
- **`obsidian/concepts/motor-selection.md` L208** — "The Bidirectional Interaction tenet finds direct support. Motor control is where consciousness visibly affects the physical world." The direct-evidence move `tenets.md` L92 forbids and the agency void's verification circularity explains.

### Family D — the bare illusionist regress (both phrasing families run; enumeration below is a CANDIDATE list)

Two tasks are already in flight (a P2 on `concepts/mysterianism.md`, a P3 on `concepts/haecceity.md`), and today's `/pessimistic-review` enumerated 15 D2 loci. **The five below are outside all three of those enumerations** and were read individually, so they are confirmed rather than grepped:

- **`obsidian/concepts/evaluative-phenomenal-character.md` L165** — "**The regress response**: something must *seem* a certain way for the illusion to occur". Bare, under an "Illusionist Challenge" heading, no Frankish anywhere in the file. Length 2826, `soft_warning`.
- **`obsidian/voids/apophatic-cartography.md` L140** — "**The regress applies**: to be under an illusion that consciousness is beyond articulation, something must *experience* that illusion." Listed as the first of "three responses [that] preserve the framework", so it carries argumentative weight. Length 2796, `soft_warning`.
- **`obsidian/topics/phenomenology-of-intellectual-life.md` L189** — "The chain terminates only when something genuinely seems some way to something." Engages quasi-seeming, then treats the regress as terminating, which is the move illusionists deny.
- **`obsidian/topics/eastern-philosophy-consciousness.md` L130** — "First, the regress: for something to *seem* a certain way, there must be a subject to whom it seems." Bare, and the D1 phrasing family, so neither the open P3's grep nor the pessimistic review's D2 grep reaches it.
- **`obsidian/concepts/binding-problem.md` L87** — "The Unfinishable Map rejects this. First, the illusionist faces infinite regress". Map voice, flat. (Also in the pessimistic review's list; repeated here because it is the only locus where the bare regress is the stated ground of a Map-voice rejection.)

**The model for this whole family is not the four hub articles 07-29b named — it is `obsidian/topics/personal-identity.md` L148–150**, which runs the regress, states the Dennett/Frankish deflationary rebuttal by name, constructs the dilemma, and then concedes: *"The Map does not claim to refute the deflationary reading on its own terms—a deflationist prepared to deny there is anything it is like to undergo the seeming can hold the line consistently. … That is a genuine framework-boundary disagreement."* Anyone fixing Family D should inherit from this file rather than from a shorter formula. `topics/the-self-minimal-narrative-and-substantial.md` L103 is a compact second model: *"the regress is pressing but not, on its own, decisive."*

## Warnings

- **`obsidian/apex/attention-as-causal-bridge.md` L66** — "Exogenous attention (~100ms): a loud noise, a flash of light. … **Consciousness is along for the ride.**" This is the exact phrase Tenet 3's Rules-out clause bans (`tenets.md` L106), asserted in Map voice with no scoping qualifier on the line. The surrounding three-mode structure makes clear it is scoped to exogenous capture only, and the article's whole thesis is willed attention as the causal bridge — so this is a phrasing collision, not a position. Rephrase to "the subject does not initiate the shift" or similar. This is the run's only Tenet 3 finding outside Family C.
- **`obsidian/concepts/qualia.md` L197–199** — the No-Many-Worlds subsection concedes the key point *"MWI with decoherence does predict definite qualia within each branch"* (the sentence `tenets.md` L168 quotes as its warrant for marking the cell not-invoked) and then runs the indexical objection forward anyway inside the cluster. Half-calibrated: keep the concession, reframe the remainder as coherence commentary. Length 3474, `soft_warning`.
- **`obsidian/concepts/philosophical-zombies.md` L205** — the Minimal Quantum Interaction subsection opens as inheritance ("the quantum mechanism specifies where the interaction occurs") but *does* close with a proper hedge ("locating that selection at quantum loci is a separate Map commitment, not one the zombie argument establishes"). Warning rather than error because the hedge is present; the fix is to lead with it.
- **`obsidian/topics/comparative-phenomenology-of-meditative-traditions.md` L143** — unchanged from 07-29b. "The more parsimonious explanation… The Unfinishable Map takes this as evidence". Parsimony run forward, after three well-calibrated concession paragraphs.
- **`obsidian/concepts/interface-threshold.md` L124** — "Gradual amplification is the more parsimonious of the two models considered here. The Map accepts the parsimony cost of the threshold model… parsimony is a tiebreaker". The parsimony use runs *against* the Map's own model, which is the permitted direction; the residual defect is only the tiebreaker rule (see Notes).
- **`obsidian/topics/phenomenology-of-intellectual-life.md` L183** — unchanged. "The more parsimonious view: the phenomenology of intellectual life is what it is *like* to think." Offset by a genuine constitution-vs-correlation audit in the next paragraph.

## Notes

- **The "tiebreaker" rule as a positive epistemic principle** persists at 16 obsidian loci. The tenet licenses only "parsimony cannot decide"; the tiebreaker rule implies parsimony *does* decide when explanatory powers are equal, which the Map then exploits by claiming the powers are unequal in its favour. Carried over from 07-29b unchanged; listed here because the count is now measured (16 obsidian / 7 archive).
- **`obsidian/concepts/measurement-problem.md` L189** is the corpus's best treatment of the tiebreaker hazard and should be the model: *"that appeal to least disruption is a simplicity consideration, and the Map's own fifth tenet holds simplicity unreliable under incomplete knowledge. The move is therefore a defeasible heuristic for *where* to look, not evidence that consciousness acts there, and it stands in acknowledged tension with the tenet that warns against trusting it."* Its L187 "more parsimoniously treated as one puzzle" is hedged in the same sentence and is **not** a defect.
- **`obsidian/concepts/inverted-qualia.md` L181** is the only conceivability-cluster article that satisfies the matrix row. Name it in any Family M task.
- **`obsidian/topics/the-steelman-for-process-monism.md` L73/L87** reads "It is more parsimonious. One ontological kind is simpler than two" — and this is **correct practice**, not a defect: the article steelmans a rival and then declines it, saying "This is exactly the situation Tenet 5 is for." Do not flag. Same for `topics/the-steelman-for-value-blind-selection.md` and `apex/steelmanning-as-method.md`.
- **Archive-tree scope confirmed material.** `archive/` holds full serving bodies, and two Tenet-2 loci (B2-archive, B2-archive-2) and one Tenet-5 locus (`archive/topics/duch-neurodynamic-theory-of-mind.md` L104) exist only there. A sweep scoped to `obsidian/` misses them. `archive/topics/limits-of-parsimony-in-consciousness-science.md` L97 is by contrast **well calibrated** ("Swinburne's reversal does not establish that dualism is simpler overall") and is a better model than its live descendant at `concepts/parsimony-epistemology.md` L140.
- **Hugo tree is in sync.** I spot-checked four recent fixes (mysterianism L186 Tenet-4 reversal, prebiotic-collapse Wheeler, parsimony-epistemology L164, self-stultification L191) and all four are current in `hugo/content/`. No obsidian-only-fix hazard this run. Conversely, the Family M defects **are live**: `hugo/content/concepts/philosophical-zombies.md` L205 and L209.
- **`research/` was not re-swept this run.** 07-29b swept it for the first time and found five loci; whether it enters permanent scope is a standing decision for the operator, not something this pass should settle by precedent.

## Verified Fixed Since 07-29b — Do Not Re-Report

Re-checked against current disk, not inherited from the changelog:

- `concepts/parsimony-epistemology.md` L164 and `arguments/epistemological-limits-of-occams-razor.md` L94 — the A1/A2 "zero self-binding" premise was **false when written**. A2 is a model. Only A1 L140 survives.
- `concepts/prebiotic-collapse.md` — the Wheeler misattribution (B1) is gone; "conscious observation selecting which history" returns 0 in all three trees.
- `concepts/entanglement-binding-hypothesis.md` L78 — "probable rather than merely possible" (B3) is gone.
- `concepts/self-stultification.md` L191 and `topics/self-stultification-as-master-argument.md` "demonstrate its falsity" — both gone.
- `concepts/mysterianism.md` — the 07-30 calibration holds on disk: L186 now reads that mysterianism "defends the legitimacy of the indexical question that many-worlds dissolves; it supplies no reason to think many-worlds false", and the invisibility-as-confirmation clause is deleted. Verified live in hugo.
- `archive/concepts/cognitive-closure.md` L69 — the matching fix is present.

## Assessed and Excluded — Legitimate, Do Not Flag

- **Every direct-contradiction hit in Tenets 1, 3 and 4.** 61 obsidian article-tree loci, all exposition-to-refute, attributed, conditional-antecedent, or definitional. Specifically: all 17 `all branches are equally real` loci describe MWI in order to reject it (including `tenets.md` L112, which is the definition); all 23 `consciousness is epiphenomenal` loci are antecedents of reductio conditionals; `concepts/buddhism-and-dualism.md` L52 and `concepts/witness-consciousness.md` L57 say Buddhism *does not* claim consciousness is an illusion.
- **Steelman articles running a rival's parsimony case in the rival's voice** — the discipline `apex/steelmanning-as-method.md` installs.
- **Historical counterexamples using "more parsimonious"** (geocentrism, caloric, extensionist biogeography) — these are Tenet 5's own evidence.
- **`concepts/jourdain-hypothesis.md` L147** and **`topics/the-self-minimal-narrative-and-substantial.md` L103** — both run the regress and both calibrate it in the adjacent line. A zero-marker grep flags them; reading clears them.
- **`obsidian/topics/personal-identity.md` L148–150** — the corpus's most complete treatment of the regress. Flagging it would reverse verified work.
- **`concepts/physics-as-disclosure.md` L98, `topics/consciousness-and-the-ontology-of-temporal-becoming.md` L100, `voids/death-void.md` L58** — pattern-matched by D2 but not the regress at all.

## Recommendation

Priority order by yield. Loci checked against the open queue: Family M and the archive B2 siblings are not targeted by any open task; Families A, C and D partially are.

1. **Family M — `concepts/philosophical-zombies.md` L203 and L207** (highest leverage). The flagship conceivability page contradicts both `tenets.md` L168 and its own L163, on a live hugo page, and the corrected text exists verbatim at `concepts/zombie-master-argument.md` L112 and `concepts/inverted-qualia.md` L181. Substitution-only (`hard_warning`, 3531 words). Doing this one file also establishes the pattern for M3 and M4.
2. **Family M remainder — `concepts/explanatory-gap.md` L191 and `concepts/knowledge-argument.md` L167.** Same fix, two files, no length pressure at knowledge-argument.
3. **`concepts/parsimony-epistemology.md` L140** — a single sentence, the last A1 residue, currently contradicting its own L164 twenty-four lines later. Cheapest high-visibility fix in the report (32 inbound citations).
4. **Family B archive siblings — `archive/topics/collapse-before-minds.md` L137 and `archive/concepts/quantum-biology.md` L75**, together with `concepts/prebiotic-collapse.md` L150. Three loci, one precedent-not-licence formula, and the archive pair has never been touched by any sweep. These are full serving bodies.
5. **Family D's five un-enumerated loci**, inheriting from `topics/personal-identity.md` L148–150 rather than from a short formula. Coordinate with the open P2/P3 and today's pessimistic review to avoid a same-file pileup.
6. **Families A3–A7 and C's four remaining loci** — the residue of prior sweeps, all deletions or scoping edits, all re-verified present today.
7. **`apex/attention-as-causal-bridge.md` L66** — one phrase, trivially fixed, and it is the only place in the corpus where a Rules-out clause's own words appear unqualified in Map voice.

Two process notes. **The archive tree must be in scope for every family sweep** — three of this run's loci exist only there, and per-tree counts in the table above show `archive/` carrying 20–100% of `obsidian/`'s hit volume on most patterns. And **treat every locus list in this report as a candidate list**: my measured false-positive rate on inspected candidates was ~90%, concentrated in exactly the patterns that look most alarming in aggregate.
