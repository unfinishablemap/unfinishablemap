---
title: "Tenet Alignment Check - 2026-07-29b"
description: "Second 07-29 pass: the day's calibration reached the leaves but not the roots. Two uncalibrated parsimony authority files, a stranded Wheeler sibling, and research/ never swept."
created: 2026-07-29
modified: 2026-07-29
human_modified: null
ai_modified: 2026-07-29T23:55:08+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[tenets]]"
  - "[[concepts/parsimony-epistemology]]"
  - "[[concepts/prebiotic-collapse]]"
  - "[[voids/epistemological-limits-occams-razor]]"
  - "[[positions/quantum-interface]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-07-29
last_curated: null
last_deep_review: null
---

# Tenet Alignment Check (second pass)

**Date**: 2026-07-29 (23:55Z)
**Scope**: All five tenets. Complements `reviews/tenet-check-2026-07-29.md` (01:20Z, Tenets 1/2/3/5) and `reviews/tenet-check-2026-07-28.md` (Tenet 4). This pass audits (a) whether the 01:20Z findings were executed, (b) the ~90 content files changed in the 22 hours since, and (c) two surfaces no tenet-check has ever covered.
**Corpus scanned**: `topics/`, `concepts/`, `positions/`, `apex/`, `voids/`, `arguments/`, plus — for the first time in the history of this skill — `research/` (524 published files).
**Errors**: 22 loci across 19 files
**Warnings**: 14
**Notes**: 11

## Summary

**No direct contradiction of any tenet exists in the corpus.** Nothing endorses eliminative materialism, illusionism about phenomenal consciousness, epiphenomenalism, MWI, quantum mysticism, psychokinesis, or energy injection in the Map's own voice. Every grep hit on those patterns is exposition-to-refute, an attributed third-party claim, or a scoped concession. On the classic reading of this skill the corpus passes.

**The 01:20Z report was almost entirely executed.** All 7 errors are fixed, 10 of 11 warnings, and 7 of 8 notes. `concepts/many-worlds.md` now leads with the indexical objection and demotes extravagance to "a registered cost of MWI rather than a refutation of it"; `concepts/quantum-interpretations.md` L48 now reads "Ontological extravagance is the fifth and the weakest"; `apex/phenomenology-mechanism-bridge.md` L87 now distinguishes the irreducibility claim (which does follow from Tenet 1) from the persisting-substance claim (downstream of agent causation). That is a genuinely large day of calibration and this report does not disturb any of it.

**The finding that matters is structural: today's calibration reached the leaves but not the roots.** Every finding below is an uncalibrated-inheritance failure of one of three kinds, and in each the corpus contains a model article that gets it right:

1. **The parsimony roots are uncalibrated while their dependants were fixed.** `concepts/parsimony-epistemology.md` (32 inbound citations) and `arguments/epistemological-limits-of-occams-razor.md` (14 inbound) are the two files every calibrated leaf cites as its authority. Both contain **zero** self-binding language — `grep -cniE "veto|run forward|symmetr|binds the Map|does not license"` returns 0 for each — and both close with a forward-running parsimony verdict. Meanwhile `topics/parsimony-case-for-interactionist-dualism.md`, `concepts/concession-convergence.md`, `topics/death-and-consciousness.md`, `arguments/materialism-argument.md` and `topics/brain-specialness-boundary.md` all now carry the settled formula. The leaves inherit from two sources that do not hold the discipline.

2. **Same-family siblings were stranded by query-scoped sweeps.** Today's Wheeler calibration fixed `topics/wheelers-participatory-universe-and-it-from-bit.md` and its archived predecessor, but `concepts/prebiotic-collapse.md` still asserts twice what Wheeler explicitly denied, with no disclaimer anywhere in the file. Today's illusionist-regress calibration fixed three hub articles but left six near-verbatim satellite "Illusionist Challenge" sections, plus two more the changed-file scope never reached. Today's self-stultification calibration fixed the concept-definition and scope-limit loci but not the closing-synthesis loci.

3. **`research/` has never been tenet-swept, and it is the upstream of the article pipeline.** No tenet-check in the repo's history has included `research/` in scope — every prior report covers `topics`/`concepts`/`positions` and later `apex`/`voids`/`arguments`/`questions`. All 524 research notes are published. Their "Tenet alignment" and "Relation to site tenets" sections are exactly what `/replenish-queue` and `/expand-topic` inherit from, and five of them carry Map-voice guidance that would seed a tenet-violating article.

## Errors

### Family A — Tenet 5 parsimony run forward, at the authority files

The governing text is `tenets/tenets.md` L144, whose Rules-out clause is explicitly reflexive: "and—internally—any Map argument that leans on parsimony as if this tenet did not apply to it." L142: "parsimony cannot decide for or against a framework." The settled corpus formula is "That tenet does not license the posit; it only refuses to let parsimony *veto* it."

**A1. `obsidian/concepts/parsimony-epistemology.md` L140** — the corpus's most-cited Tenet 5 authority (32 inbound).
> "Ontological parsimony still favours physicalism, but on explanatory adequacy — the dimension most relevant to consciousness — dualism has the advantage; the [[parsimony-case-for-interactionist-dualism|positive parsimony case]] develops this systematically."

Privileges a dimension by fiat ("most relevant"), scores dualism ahead on it, and endorses a "positive parsimony case". The file has no self-binding clause anywhere. Fix: keep the dimension-conflict point as a defeat of the *objection* ("'the simpler theory' is undefined here"), drop "dualism has the advantage", add the settled formula. Length: 2702 words, ARGUMENT 2341, concepts hard 3500 — ample room.

**A2. `obsidian/arguments/epistemological-limits-of-occams-razor.md` L94** — the second authority (14 inbound), also zero self-binding.
> "The [[parsimony-case-for-interactionist-dualism|positive case]] goes further, arguing that when all dimensions of simplicity are counted — not just substance types but theoretical proliferation, brute facts, and explanatory directness — interactionist dualism emerges as the more parsimonious position."

The target article refuses simpler-therefore-truer in terms; this gloss strips the bracketing. L99's Further Reading label repeats it. **Disambiguation hazard**: the near-identically-named `voids/epistemological-limits-occams-razor.md` is **exemplary** — L91 concedes the ecumenical symmetry ("the void does not establish dualism"), L99 says "clearing space for Tenet 1, not as establishing it", L101 carries the Tenet 2 minimality calibration. Do not confuse the two files. Length: 1857 words — ample room.

**A3. `obsidian/concepts/reductionism.md` L188**, under the article's own Occam's-Razor-Has-Limits heading.
> "Physicalism wins on ontological parsimony (one substance type) but loses on explanatory simplicity: it must treat consciousness as a brute fact about physical arrangements, while dualism provides a reason for experience to exist."

Redefine-and-score. Fix: end the comparison at "they yield contradictory verdicts, so parsimony has no verdict to give here." Length: total 3500/3500 but ARGUMENT is 2985 with 515 words of apparatus — the fix is a deletion anyway, so length-safe.

**A4. `obsidian/concepts/dualism.md` L173** — the flagship dualism concept page, highest visibility.
> "Moreover, ontological parsimony favours physicalism, but explanatory parsimony favours dualism—a key distinction from [[parsimony-epistemology]]."

Same redefine-and-score as a bare Map-voice verdict. The line also opens with the too-strong rule "Parsimony arbitrates between theories of *equal* explanatory power."

**A5. `obsidian/concepts/geometric-model-of-mind.md` L113** — mis-sources Tenet 2's minimality to parsimony.
> "the Map because parsimony favours the smallest non-physical influence consistent with the tenets"

`tenets.md` L68 exists specifically to forbid this: "Tenet 2's minimality is *empirical-constraint* minimality… The Map does not claim that within those constraints the smallest interaction is most likely true—only that no larger interaction is empirically tenable." Double defect: parsimony run forward, and Tenet 2 re-grounded on the truth-tracking reading Tenet 5 disowns. The rest of the article is exemplary (bedrock-clash discipline, framework-stage calibration), so this is one sentence out of step. **Model to inherit**: `voids/epistemological-limits-occams-razor.md` L101 — "minimum intervention follows from conservation laws, not mere simplicity preference". **Sibling**: `research/wlodzislaw-duch-consciousness-2026-05-02.md` L122 carries the same sentence and seeded this article.

**A6. `obsidian/topics/biological-computationalisms-inadvertent-case-for-dualism.md` L100** — a stranded sibling of a fix made today.
> "once all explanatory costs are tallied, interactionist dualism emerges as the more parsimonious position"

This is the same claim the 01:20Z report flagged at `concepts/concession-convergence.md` L153 and which was fixed today to read "reads it as an internal critique of the objection rather than positive evidence for dualism." The cited source `topics/parsimony-case-for-interactionist-dualism.md` L138 says "not as positive evidence for dualism but as an internal critique of the objection" and L145 "without ever conceding that the simpler theory is, for that reason, the truer one." This file drops all of it. Last touched 2026-06-24, so today's sweep never reached it. Notably, its Tenet 3 and Tenet 4 sections (L96, L98) are models of calibration — only the Tenet 5 section lapsed.

**A7. `obsidian/topics/the-convergence-argument-for-dualism.md` L177** — the one 01:20Z note still open.
> "physicalism's parsimony advantage is outweighed by its explanatory disadvantage"

Plus "parsimony is a tiebreaker between theories of equal explanatory power" — a stronger rule than the tenet permits. Length: 3998/4000 total, ARGUMENT 3506 with 494 words apparatus; the fix is a deletion.

### Family B — Tenet 2/4: Wheeler misattribution and precedent-as-licence

**B1. `obsidian/concepts/prebiotic-collapse.md` L74 and L204** — the stranded sibling of today's Wheeler work. Three defects in one file; `grep -cniE "Wheeler put registration|nothing whatsoever to do|irreversible amplification"` returns **0**.

L74: "Wheeler extended this cosmologically: the universe exists as a quantum superposition of possible histories, with conscious observation selecting which history becomes actual—not moment by moment, but across the entire temporal span."

L204: "If Wheeler's participatory universe—with future observers selecting past outcomes—became the consensus interpretation, the Map's objective-reduction baseline would be unnecessary. Consciousness would cause collapse after all, just across temporal spans rather than at moments."

Wheeler wrote the opposite. Today's calibrated `topics/wheelers-participatory-universe-and-it-from-bit.md` L154 quotes him: "'Consciousness' has nothing whatsoever to do with the quantum process. We are dealing with an event that makes itself known by an irreversible act of amplification … an act of registration" (Wheeler 1983), and L158 states the settled formula: "Putting consciousness where Wheeler put registration is the Map's move, not his." Fix: replace "conscious observation" with observer-participancy in Wheeler's registration sense and import the disclaimer. **Length caution**: 3520 words, `hard_warning` against the concepts 3500 ceiling — substitution-only.

**B2. `obsidian/concepts/prebiotic-collapse.md` L150** — precedent as licence, with "proof".
> "Avian magnetoreception maintains spin coherence for microseconds in warm biological tissue—proof that evolution can optimise systems to exploit quantum effects despite thermal noise. If birds can do it for navigation, neural systems might do it for consciousness."

`tenets.md` L78: "This establishes a biological *precedent* rather than a licence for neural coherence." `positions/quantum-interface.md` P-Q8 (L124) names this exact drift class: "Warm-quantum-biology results are a precedent for the interface, not a licence for it."

**B3. `obsidian/concepts/entanglement-binding-hypothesis.md` L78** — precedent upgraded to a probability claim.
> "making neural quantum effects probable rather than merely possible"

The immediately preceding paragraph (L76) is *exemplary* — "the Tegmark/Hagan dispute is therefore live rather than settled either way, and the Map's microtubule-scale interest is tenet-driven (Minimal Quantum Interaction) rather than empirically forced" — and L78 then undoes it. Fix: attribute the conclusion to the sibling article as its argument and append the P-Q8 formula.

**B4. `obsidian/concepts/quantum-interpretations.md` L104** — admits a reading two siblings rule out.
> "**Site compatibility:** Moderate to High. The Map is compatible with either \"consciousness causes collapse\" or \"consciousness modulates collapse.\""

Directly contradicted by `concepts/prebiotic-collapse.md` L164 ("A simple \"consciousness causes collapse\" fails") and `concepts/many-worlds.md` L159 ("collapse no longer waits on consciousness, and consciousness biases what would have happened anyway"). Also overshoots Tenet 2, which commits to biasing indeterminate outcomes, not triggering collapse. Fix: narrow to "modulates".

### Family C — Tenet 3: factive self-stultification at the closing-synthesis loci

`tenets.md` L98 is unusually explicit that the Map holds Tenet 3 "*not* because the self-stultification argument refutes epiphenomenalism from inside the epiphenomenalist's framework", and L100 concedes the phenomenal-concept strategy survives the charge. Today's sweep calibrated the concept-definition and scope-limit loci; the residue clusters in closing synthesis paragraphs.

- **`obsidian/concepts/self-stultification.md` L191** — "Self-stultification establishes *that* consciousness must be causally efficacious." Contradicts the same file's calibrated L201.
- **`obsidian/concepts/self-stultification.md` L197** — "a constraint that only theories granting consciousness genuine causal efficacy can satisfy" — an exclusivity claim the conceded phenomenal-concept strategy falsifies.
- **`obsidian/topics/self-stultification-as-master-argument.md` L133** — "they *demonstrate* its falsity by the act of defending it."
- **L137** — "self-stultification shows this recognition must be causally efficacious, not epiphenomenal."
- **L171** — "any theory that lands on epiphenomenalism has destroyed its own rational foundations and cannot be rationally held by the very minds it describes."
- **`obsidian/concepts/causal-closure.md` L185** — "**Consciousness reporting** shows that mental states influence physical behavior." `tenets.md` L92: the conversation *suggests* downward causation. Ground 3 of the same list is correctly calibrated.
- **`obsidian/concepts/working-memory.md` L171** — "WM manipulation demonstrates downward causation."
- **`obsidian/apex/minds-without-words.md` L115 and L151** — "Pain asymbolia demonstrates that phenomenal properties do real causal work" / "demonstrates phenomenal valence does causal work." Contradicts the same file's own constrain-vs-establish discipline at L137.
- **`obsidian/concepts/motor-selection.md` L208** — "The Bidirectional Interaction tenet finds direct support. Motor control is where consciousness visibly affects the physical world." This is the "direct evidence / introspectible datum" move `tenets.md` L92 forbids and the agency void's verification circularity explains.

### Family D — the bare illusionist regress stated as decisive

The calibrated register was installed today at `concepts/illusionism.md` L91, `concepts/explanatory-gap.md` L115 ("Taken bare it proves nothing"), `concepts/mind-brain-separation.md` L96 ("does not settle the matter, and the Map does not run it as though it") and `concepts/mental-effort.md` L126. Eight satellites still run it flat. The six the changed-file scan found:

- `obsidian/concepts/working-memory.md` L161 — "these experiences cannot themselves be illusions without invoking a further level of experience"
- `obsidian/concepts/evolution-of-consciousness.md` L143 — "and that something is doing the experiencing illusionists claim doesn't exist"
- `obsidian/concepts/motor-selection.md` L190 — "To seem one way rather than another, there must be something it's like to seem."
- `obsidian/concepts/substance-property-dualism.md` L107 — "The regress either terminates in genuine phenomenal states or renders the account vacuous."
- `obsidian/concepts/consciousness-as-amplifier.md` L113 — "something must generate them, and that something is either conscious or requires further explanation"
- `obsidian/concepts/baseline-cognition.md` L160 — "something generates them, reinstating the original problem at a higher level"

Two more sit outside the changed-file scope and were found by corpus-wide grep:

- **`obsidian/concepts/haecceity.md` L156** — the worst of the eight, under a "**Response**:" header, treating the regress as decisive: "The illusionist position faces a regress (Tallis 2011). For something to *seem* a certain way, there must be a subject to whom it seems that way—and this seeming is itself phenomenal. The illusion of consciousness requires consciousness to be an illusion *for*." Zero mentions of Frankish or functional seeming in the whole file.
- **`obsidian/concepts/parfit-reductionism.md` L95** — near-verbatim sibling: "Illusionism faces a fundamental difficulty here. For something to *seem* a certain way, there must be a subject to whom it seems that way—and this seeming is itself phenomenal." The file's only Frankish mention is a bare reference-list entry at L165.

Fix for all eight: the bare regress assumes the seeming is itself phenomenal, which illusionists deny; a representational system need not instantiate what it represents. The substantive pressure is the *relocation cost* — whether the second question is tractable — not the regress itself.

## Warnings

- **`obsidian/topics/self-stultification-as-master-argument.md` L155, L167, L79** — "Any theory that violates this constraint is rationally unendorsable"; "not merely counterintuitive but rationally untenable"; illusionism "inherits the same self-stultification", where `concepts/illusionism.md` L151 concedes the convergence "assumes rather than establishes".
- **`obsidian/topics/the-epiphenomenalist-threat.md` L172** — "leaving it rationally unendorsable by the very minds it describes", in an otherwise well-calibrated file (L59, L151, L162).
- **`obsidian/concepts/agent-causation.md` L148** — "the self-defeat of physicalism delivers mental causation without phenomenological premises"; "delivers" overshoots the threatens register.
- **`obsidian/apex/phenomenology-mechanism-bridge.md` L171** — "is what the chain demonstrates", contradicting its own L138 rule that "a tenet may remove a defeater, but it must not upgrade the evidence level".
- **`obsidian/concepts/baseline-cognition.md` L116 and `obsidian/concepts/consciousness-as-amplifier.md` L73** — both over-read the DeWall 2008 cognitive-load study as demonstrating that logical reasoning *requires* consciousness. `tenets.md` L94 renders the same study as "consistent with… corroborates the tenet rather than establishing it".
- **`obsidian/concepts/consciousness-as-amplifier.md` L109** — "contemplative traditions demonstrate that sustained attention… improves cognitive performance"; illusionism absorbs practitioner reports heterophenomenologically. Soften to "report".
- **`obsidian/concepts/moral-responsibility.md` L123 and L125** — the bare regress presented as a desert-*preserving* response rather than as pressure.
- **`obsidian/concepts/interactionist-dualism.md` L179** — heading "### Where the Map's Tenets Take a Substance-Leaning Sub-Reading" sources the lean to the tenets; its own body at L181 and `tenets.md` L56/L180 place it downstream of agent causation. Retitle to the form used at `concepts/substance-property-dualism.md` L159. **This is the run's only Tenet 1 finding.**
- **`obsidian/concepts/phenomenological-evidence.md` L170** — runs the self-stultification move flat: "The epiphenomenalist trusts their own reasoning about consciousness enough to conclude it lacks causal power—but that conclusion depends on introspective access to the very experiences whose evidential status is being denied." No conditionality, no phenomenal-concept concession. Missed by today's sweep because the file is about introspective reliability, not epiphenomenalism.
- **`obsidian/topics/consciousness-in-smeared-quantum-states.md` L110** — "Consciousness is not merely definite in its own experience — it imposes definiteness on physical reality wherever it is present." Global definiteness-imposition conflicts with the objective-reduction baseline and Tenet 2's localisation to neural systems. Also uses the "not X — it is Y" construct `CLAUDE.md` bans.
- **`obsidian/topics/consciousness-in-smeared-quantum-states.md` L120** — "Stapp's model is the most explicit implementation of the Map's tenet." `tenets.md` L70 ranks post-decoherence selection *ahead* of Stapp, and L104 records that Stapp's Process-1 placement is precisely the move the Map has **not** adopted. Post-decoherence selection appears nowhere in this article's tenet section.
- **`obsidian/concepts/mind-matter-interface.md` L146** — "Quantum coherence demonstrably survives in warm biological systems", offered as mitigation with no precedent-not-licence qualifier, while L144 in the same file is exemplary.
- **`obsidian/topics/falsification-roadmap-for-the-interface-model.md` L125** — "indexical identity, ontological profligacy" listed co-equal, no subsidiary demotion.
- **`obsidian/topics/comparative-phenomenology-of-meditative-traditions.md` L143** — "The more parsimonious explanation… The Unfinishable Map takes this as evidence that consciousness has genuine structural features." Parsimony run forward, and cross-traditional convergence spent as evidence rather than indirect support — after three preceding paragraphs that carefully concede the cross-pollination objection and flag the Sino-Indian pair as weakest. Same axis as the open P3 on `topics/phenomenal-normativity-environmental-ethics.md` L63.

## Notes

- **`obsidian/topics/epistemology-of-convergence-arguments.md` L184** — "parsimony is a tiebreaker between theories of equal explanatory power, not a trump card overriding convergent evidence", ranking parsimony below the Map's own evidence. **Length-blocked**: 6602 words, `critical`, under a standing HUMAN LENGTH DECISION. Report only; do not mint.
- **The "tiebreaker" rule as a positive epistemic principle** appears in five further places and is an unearned strengthening — the tenet licenses only "parsimony cannot decide", whereas the tiebreaker rule implies parsimony *does* decide when powers are equal, which the Map then exploits by claiming the powers are unequal in its favour: `arguments/epistemological-limits-of-occams-razor.md` L34, `concepts/parsimony-epistemology.md` L88, `concepts/type-specificity.md` L133, `concepts/interface-threshold.md` L124 (mild — argues against a Map cost), `concepts/combination-problem.md` L187.
- **`obsidian/topics/probability-problem-in-many-worlds.md` L142** — extravagance leads the case list undemoted; L146 of the same file is well calibrated, so this is list-ordering residue only.
- **`obsidian/concepts/quantum-interpretations.md` L185** — "The haecceitistic question—why am I this one?—is meaningful on collapse interpretations and meaningless on MWI", stated as fact. `tenets.md` L118 requires conceding this is a posited claim resting on a non-deflationary "I".
- **`obsidian/concepts/many-worlds.md`** — coverage gap. The corpus's canonical anti-MWI article carries no non-deflationary-"I" presupposition honesty: zero hits for deflationary/Madhyamaka/no-self. `tenets.md` L118 has the paragraph to import.
- **`obsidian/concepts/conservation-laws-and-mental-causation.md` L173** — leads with extravagance before "More fundamentally, MWI raises indexical questions"; the subordination is present but the "registered cost" demotion is absent.
- **`obsidian/concepts/prebiotic-collapse.md` L146** — presents Hagan's recalculation as settled where three siblings carry the "live rather than settled" calibration plus Reimers/McKemmish.
- **`obsidian/topics/phenomenology-of-intellectual-life.md` L183** — "The more parsimonious view: the phenomenology of intellectual life is what it is *like* to think." Offset by a genuine constitution-vs-correlation audit in the next paragraph.
- **`obsidian/topics/phenomenology-of-intellectual-life.md` L234** — Further Reading label "Why denying phenomenology is self-undermining" overstates a destination whose own description now reads "a threat, not a refutation". Same shape as the open P3 about the "Why Attention Schema Theory Fails" label.
- **`obsidian/concepts/explanatory-gap.md`** — has a No-Many-Worlds subsection running inheritance ("Rejecting Many-Worlds means accepting genuine selection") where `tenets.md` L168 marks that cell **not invoked** for the conceivability/qualia cluster and requires coherence-commentary framing.
- **`obsidian/concepts/mental-effort.md` L3** — frontmatter description "reveals about consciousness influencing matter"; the body is exemplary.

## `research/` — never swept, and upstream of the pipeline

All five loci below are published. Their "Tenet alignment" / "Relation to site tenets" / "Implications" sections are what `/replenish-queue` and `/expand-topic` inherit from, which makes them higher-leverage than their obscurity suggests.

- **`obsidian/research/wlodzislaw-duch-consciousness-2026-05-02.md` L122** — "the Map wants minimal interaction because parsimony favours the smallest non-physical influence." The conflation `tenets.md` L68 exists to forbid; sibling of A5 and its likely source.
- **`obsidian/research/qm-interpretations-beyond-mwi-2026-01-16.md` L173** — "**Occam's Razor cuts both ways.** Bohmians add hidden variables… But if consciousness solves the measurement problem more parsimoniously, hidden variables are unnecessary." In a section headed "Explicitly Position Against Bohmian Mechanics" that is written as instruction to the Map.
- **`obsidian/research/voids-anesthesia-void-2026-04-17.md` L164** — "**The interface-disruption reading is more parsimonious**". *Good news*: the live `voids/anesthesia-void.md` did **not** inherit it — L124 reads "a parsimony move that outruns the evidence… Simpler is not safer when the evidence is this layered" and L137 concedes cessation-physicalism "would become the more parsimonious reading". The live article is a model; the research note is the residue.
- **`obsidian/research/terminal-lucidity-filter-theory-2026-03-20.md` L162** — "noting the filter model provides a more parsimonious explanation of the full evidence set". Runs against the dependency matrix, which marks anti-parsimony **required** (not defensive) for the memory-hierarchy row precisely because the filter model is the parsimoniously dispreferred reading.
- **`obsidian/research/limits-of-parsimony-consciousness-2026-03-20.md` L227** — proposes a future article, "Swinburne's Reversal: Is Dualism Actually Simpler?", and asserts it "Aligns with Tenets 1 and 5". A pipeline hazard: as scoped it would seed a Tenet-5-violating article.

Correctly calibrated and **not** to be flagged: `research/cosmopsychism-2026-07-13.md` L201 (uses Tenet 5 defensively against cosmopsychism's own parsimony marketing) and `research/steelman-for-value-blind-selection-2026-06-18.md` (steelmans the parsimonious rival as an explicit discipline).

## Assessed and Excluded — Legitimate, Do Not Flag

The following are the corpus's deliberate settled register, verified at primary sources during the 07-29 session. Flagging any of them as insufficient tenet commitment would reverse verified work.

- Self-stultification "presses hard against" / "threatens" rather than "defeats" — `tenets.md` L98 forbids the stronger inference and L100 concedes the phenomenal-concept strategy survives. The canonical statements at `concepts/bidirectional-interaction.md` L59, `arguments/materialism-argument.md` L86 and L142, and `concepts/self-stultification.md` L201 are **models**, not defects.
- Illusionism as a spectrum rather than a Hard/Soft binary (`concepts/illusionism.md` L71–79, using Graziano's own "subtle" contrast term); the bare regress proving nothing.
- The Wheeler disclaimer at `topics/wheelers-participatory-universe-and-it-from-bit.md` L154/L158 — required honesty, not a Tenet 3 shortfall.
- "Empirically indistinguishable from chance" as a by-construction framework boundary rather than a sensitivity limit — `topics/testing-consciousness-collapse.md` L230 is now exemplary on exactly this.
- Precedent-not-licence on warm quantum biology; Denton 2024 as modelled rather than experimental; magpie mirror self-recognition as contested; human cumulative culture unmatched in degree rather than categorically exclusive.
- Voids and cross-traditional convergence as *indirect* support only; parsimony never run forward; a precedent is not a licence.
- Exposition-to-refute and attributed claims throughout: `topics/eliminative-materialism.md`, `concepts/materialism.md`, `concepts/illusionism.md`, `concepts/objections-to-interactionism.md` L65, `topics/delegatory-dualism.md` L52 (attributed to Saad), `concepts/indexical-identity-quantum-measurement.md` L97 and `concepts/parfit-reductionism.md` L63 (both describing MWI, not endorsing it), and every `Bösch 2006` / `Maier 2018` citation of the negative psi record.
- `apex/phenomenology-of-consciousness-doing-work.md` L155 — "The profile establishes that consciousness does cognitive work" sits inside a paragraph that explicitly disclaims decisiveness and layers the claim honestly. Judged calibrated.
- The two "establishes that consciousness" loci at `topics/argument-from-reason.md` L152 and `concepts/measurement-problem.md` L189 are **already queued** as a P3 whose notes state a no-op is a legitimate outcome. Do not re-mint.

## Recommendation

Priority order by yield, dedupe-checked against all open tasks (none of the loci below is currently targeted):

1. **The two parsimony authority files** (A1, A2) — highest leverage in the corpus. 46 inbound citations inherit from files with zero self-binding, which is why the leaf-level fixes keep regressing. Both have ample length headroom. Fix these and the family stops regenerating.
2. **`concepts/prebiotic-collapse.md`** (B1, B2, plus the L146 note) — three loci, one file, one pass. Contradicts today's own Wheeler calibration on a published page. Substitution-only: 3520 words, `hard_warning`.
3. **The bare-regress satellites** (Family D, eight loci) — mechanical propagation of a formula already on disk at four hub articles. `haecceity.md` and `parfit-reductionism.md` are near-verbatim copies of each other and should be fixed together.
4. **The Tenet 3 closing-synthesis loci** (Family C, ten loci across six files) — the residue of today's sweep, concentrated in the self-stultification pair.
5. **A3–A7** — the remaining parsimony leaves; `reductionism.md` and `the-convergence-argument-for-dualism.md` are within two words of their hard ceilings, but every fix is a deletion.
6. **`research/`** — five loci, one pass, no length ceiling. Worth doing because it is upstream of article generation, and worth a standing decision about whether `research/` enters the tenet-check scope permanently.

Two process notes for whoever executes. **Expect `cycle_post` to close a multi-file task after the first file** — re-queue the remainder rather than trusting the mark. And **do not re-litigate any position**: every finding here is a calibration fix in which the conclusion stands and only the grounds get scoped. Where a fix would require weakening an argument rather than scoping its grounds, decline it and say so.
