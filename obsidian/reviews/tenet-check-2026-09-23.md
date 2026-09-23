---
title: Tenet Alignment Check - 2026-09-23
created: 2026-09-23
modified: 2026-09-23
human_modified: 2026-09-23
ai_modified: 2026-09-23T23:55:00+00:00
draft: false
description: "Tenet check 138: none of check 137's priority items was repaired or queued. A structural sweep of 57 recently edited files finds the alignment section outrunning the body again."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: Andy Southgate
ai_system: claude-opus-5-5
ai_generated_date: 2026-09-23
last_curated:
last_deep_review:
---

# Tenet Alignment Check

**Date**: 2026-09-23 (check 138; previous `reviews/tenet-check-2026-09-20.md` = 137)
**Files checked**: 57 articles read in full. These are every live article in `topics/ concepts/ positions/ apex/ voids/ arguments/` edited since check 137 (2026-09-20 22:00 UTC), plus `tenets.md` in full. Separately, 14 files carried from check 137 were probed for repair.
**Errors**: 4. Three are carried from check 137 and still live. The fourth is one new locus of an already-booked family.
**Warnings**: 34 new (by article entry; several carry 2–3 loci), plus 9 carried from check 137 (none repaired).
**Notes**: 19 new
**Lens**: the structural lens that check 137 recommended. For each article, does the alignment paragraph claim more than the article's own body, or the other way round?

## Summary

**1. Nothing from check 137 has moved.** Check 137's four priority items and its top carried item are all live, verbatim. None of the five files has a commit since the report. `todo.md` has no open task for any of them. Check 137 chose not to mint, and nothing else picked them up. In the 09-08 cycle, by contrast, 4 of 4 priority items were fixed within two days, because a driver minted from the list. **A reports-only priority list only gets actioned if someone mints tasks from it.** That is the most actionable finding in this report. See §Priority list.

**2. The structural lens works, and the pattern check 137 found holds on fresh material.** Of the 57 edited files, 37 have at least one finding and 20 are clean. No file in Map voice endorses physicalism, illusionism, epiphenomenalism, MWI or psi. Every finding is calibration drift between an article's alignment section (or lead, or Occam paragraph) and its own body. In most cases the body already holds the calibrated version.

**3. Two families recur across unrelated files. Both violate text that `tenets.md` already states:**
- **Family S (Tenet 3 standing).** The article reports epiphenomenalism as refuted, or mental causation as actual. `tenets.md` L93 holds Tenet 3 "not as a directly introspectible datum". L101 is headed "Why this is the deepest difficulty for epiphenomenalism rather than its refutation". That doctrine was installed 2026-05-11, with `^tenet-3-standing` added on 2026-08-03. At least 11 delta files ignore it (§Family S).
- **Family I (alignment-line inheritance on Tenet 4).** The article's No-MWI paragraph claims that rejecting MWI secures something that branch-relative accounts also secure. It does this in rows where the matrix marks No-MWI *Not invoked*. There are 7 new delta loci. This is the same shape as check 137's Tenet 4 findings.

**4. Recent edits sometimes install a discipline and then breach it in the next paragraph.** `topics/cross-cultural-phenomenology-of-agency` received a Map-voice preamble on 2026-09-21 that reads "coherence rather than corroboration" (L95). Its Tenet 3 paragraph four lines below (L99) then claims "indirect support" and genuine causal efficacy. `topics/ai-consciousness`, edited 2026-09-21 to fix an epiphenomenalism-scope issue, still says self-stultification "proves" causal work (L145). **Being edited is not being reviewed.**

## Errors

### Carried from check 137, all still live and unqueued
Re-verified this run. Each offending string occurs exactly once, and none of the files has a commit since 2026-09-20.

- `concepts/unity-of-consciousness.md`: "now lending initial support" (Tenet 2; `Kerskens` = 0, `unreplicated` = 0 in the file). Also "unity reports become either false or contentless" (Tenet 4; fabricated tenet content).
- `topics/presentiment-and-retrocausality.md`: "Presentiment would be additional evidence if confirmed" (Tenet 2; this inverts the parapsychology firewall; `parapsychology-firewall` = 0 in the file).
- `topics/animal-consciousness.md`: "plausibility tilt rests on the [[evolutionary-case…" (Tenet 3 imported into a row the matrix marks *Not invoked*; `coherence commentary` = 0).

### New locus, already-booked family
- `concepts/implicit-memory.md` L196 (Tenet 5): "The simplest account that covers *all* the phenomena—neural and experiential—treats consciousness as a genuine causal factor". This is a parsimony verdict in the Map's favour, and the body settles for "not plausibly idle" (L101). **It is already a named locus** in `reviews/tenet-check-2026-09-19.md` L392, and it belongs to the blocked `NEEDS-HUMAN (doctrine) 2026-09-19` Tenet-5 tiebreaker item in `todo.md`. Nothing is minted here; it is listed only so the count is honest. The same family has a second, possibly new, delta locus: `topics/embodied-consciousness.md` L136, "but the bidirectional reading is the more economical fit", which comes directly after conceding the data "do not by themselves decide".

## Priority list (capped at 4)

Two slots go to check 137's unactioned ERRORs, because an unminted list decays to zero. Two go to the strongest new structural findings.

| # | Locus | Tenet | Why this one |
|---|---|---|---|
| 1 | `concepts/unity-of-consciousness.md`, both quotes above | 2 + 4 | Check 137's #1. Two independent defects, one of them fabricated tenet content. Now 3 days unqueued |
| 2 | `topics/presentiment-and-retrocausality.md` | 2 | Check 137's #3. A one-sentence fix. Right now the Map publicly welcomes a result its own firewall says would count against it |
| 3 | `topics/cross-cultural-phenomenology-of-agency.md` L99 | 3 | Contradicts the preamble installed 2 days ago, 4 lines above it (quotes below) |
| 4 | `concepts/neural-correlates-of-consciousness.md` L160 | 3 (P-CS6) | Converts filter-over-production evidence into outbound Tenet 3 support, which P-CS6 forbids. Its own L122 says the cluster "cannot honestly be cited as independent confirmation of transmission" |

**Carried below the cap, so they are not lost:** `concepts/dualism.md` ("cannot in principle capture subjective character", check 137's #2); `concepts/filter-theory.md` ("it can affect brain states just as brain states affect", check 137's #4, P-CS6); `topics/animal-consciousness.md` (ERROR above); and the new article `topics/architectural-adequacy-at-the-built-edge.md` (L113, L117 under §Warnings). **If a driver mints, it should mint all eight,** since none has a task.

**Recommendation to the driver:** mint one `refine-draft` per priority row, each scoped to the quoted sentence and its body contradiction. Each target is a single article whose defect this report verified. That is in contract for the reviewed-article case. This check did not mint, following the skill's reports-only scope.

## Warnings

All quotes were verified with `grep -oF` at one hit on the stated line. The ERRORs, the priority rows and the Family S loci were re-grepped by me independently; the rest were verified by the sub-sweeps (§Method).

### Family S: Tenet 3 held as actual or epiphenomenalism reported as refuted (tenets.md L93, L101, `^tenet-3-standing`)
- `concepts/self-stultification.md` L197: "Self-stultification argues *that* consciousness must be causally efficacious." Its own L181 says: "Self-stultification does not settle that". At L207, "A theory that cannot be rationally believed gains nothing from being simple." contradicts L181's "no longer shows that epiphenomenalism cannot be rationally believed". **This is the hub article contradicting its own retreat.**
- `topics/ai-consciousness.md` L145: "It proves that *some* consciousness must do causal work, not that *all* must." This contradicts `tenets.md` L101.
- `topics/amplification-mechanisms-consciousness-physics.md` L181: the simpler hypothesis "fails the evidence the Map marshals for [[interactionist-dualism|mental causation]]". This reports the epiphenomenalism dispute as won.
- `concepts/attention-schema-theory.md` L209: "The phenomenology of effort supports bidirectional interaction". L175 treats effort phenomenology as evidence. Both run against L93's "not as a directly introspectible datum".
- `concepts/consciousness-selecting-neural-patterns.md` L162: "All three support the Map's" Bidirectional Interaction tenet, yet the same line has Penrose–Hameroff consciousness "*results from*" collapse, which is inbound only. L62 claims "first-person evidence for this mechanism". The L124 heading "Selection has measurable effects." conflicts with the article's own L172.
- `concepts/categorical-surprise.md` L113: without mental causation the correlation "would be a systematic coincidence". Its own L101 says the correlation does not "adjudicate between the Map's reading and an epiphenomenalist one".
- `concepts/phenomenology-of-choice-and-volition.md` L56/L123: "genuine selector and controller rather than an epiphenomenal spectator". This is an inverse case: the body claims more than the alignment section (L161, "suggests").
- `concepts/parfit-reductionism.md` L117/L119: flat actual-causation claims that the anti-replica argument then depends on.
- `concepts/universal-coupling-response.md` L92: "supports both bidirectional interaction and universal coupling simultaneously". This sits in the Animal row's territory, where interactionism is *Not invoked*.
- `topics/cross-cultural-phenomenology-of-agency.md` L99 (priority 3): "gains indirect support from cross-cultural phenomenology" and "which is what one would expect if phenomenal agency tracks genuine causal efficacy". This contradicts L95's "coherence rather than corroboration".
- `topics/quantum-neural-timing-constraints.md` L126: "Consciousness isn't late to a decision already made—it contributes to *when* threshold-crossing becomes action." This is another inverse case: the alignment paragraph (L170) is correctly conditional and the body is not.

Precedent: `reviews/tenet-check-2026-09-02.md` §Warning 2 repaired the self-stultification hub's "second ring" of 8 loci. The self-stultification article itself has since regrown the claim in its own alignment section.

### Family I: Tenet 4 alignment-line inheritance (No-MWI claimed to secure what branch-relative accounts also give)
- `topics/architectural-adequacy-at-the-built-edge.md` L117 (new article): "The Map's commitment to indexical determinacy means it must hold that there is a fact here". Whether experience is present is background posit (1), not Tenet 4. L131 then names "Tenets 4 and 5 the primary stakes".
- `topics/ai-consciousness.md` L161: "The [[haecceity]]—thisness—that makes me *this* particular conscious being requires something beyond physical description". All three machine rows mark No-MWI *Not invoked*.
- `concepts/universal-coupling-response.md` L94: "the question of whether a specific organism is conscious loses determinacy". tenets.md concedes branch-relative determinacy.
- `topics/constitutive-exclusion.md` L120: "Without MWI, measurement genuinely constitutes outcomes… consciousness participates in making it what it is". The article's own L118 says objective mechanisms collapse "before and beyond minds".
- `topics/consciousness-and-social-understanding.md` L161: ownership "that its rejection of many-worlds … secures". This reverses the dependency tenets.md states.
- `concepts/timing-gap-problem.md` L95: "The Map rejects many-worlds partly because it dissolves the very questions…". tenets.md gives no such reason.
- `voids/interface-formalization-void.md` L123: "Without this tenet, the void could be dissolved by redefining it away." This is not a branch-indexical void (Voids row).
- `concepts/unity-of-consciousness.md`: the carried Tenet 4 limb above.

### Alignment/lead claims more than the body (other tenets)
- `arguments/functionalism-argument.md` L195: "The arguments against functionalism directly support the Map's framework". Its own L229 audit finds the legs "neither refuting functionalism from inside". **L199:** "This implies that purely computational systems—no matter how sophisticated—cannot be conscious." That does not follow from non-entailment, and it contradicts the matrix's bare-artificial-phenomenality row, which leaves open which physical systems an experiencer can couple with.
- `apex/competency-without-felt-experience.md` L129: "That supports the positive claim". The body at L119 limits this to what the interface commitment "yields from inside the framework".
- `concepts/attention-as-interface.md` L234: the hypothesis "explains what simpler theories cannot". Four lines earlier, L230 leaves the causal role "open".
- `concepts/attention-schema-theory.md` L42 (lead): "cannot be another model without infinite regress". L103 retracts it: "the bare regress is not decisive, and the Map grants this."
- `concepts/integrated-information-theory.md` L150: Tenet 3 is said to hold that consciousness "selects among superposed neural states, collapsing quantum indeterminacy". `tenets.md` has 0 hits for that phrase, and this is the non-definitional pre-decoherence variant. **First flagged in `tenet-check-2026-09-06` (then L154), 17 days live.** L144 "the undeniable fact of experience" and L138 claim more than the body's L47 and L136.
- `concepts/methodological-pluralism.md` L119: "follows directly from the Map's foundational commitments". The body's L37 says "a premise, not an entailment".
- `concepts/minimal-consciousness.md` L151: "The impossibility of identifying such a threshold suggests consciousness is fundamental". The body says "difficulty… provides indirect support" (L139).
- `concepts/neural-correlates-of-consciousness.md` L160: priority 4, above.
- `concepts/quantum-completeness.md` L94/L34 (inverse case): the body's "not a further physical domain" goes further than the alignment section's own "room, not requirement" (L106). Today's L114 parsimony repair reads clean.
- `concepts/implicit-memory.md` L193: "The statistical regularity of expert performance suggests genuine selection, not mere observation of whichever branch". This is a statistical argument for Tenets 2 and 4 that tenets.md rules out (no unconditioned aggregate signature).
- `topics/architectural-adequacy-at-the-built-edge.md` L113: "that rule dispatches anthrobots and synthetic cells cleanly". Its own L62 says "That negative is clean only because the integration criterion is stated in neural vocabulary."
- `topics/basal-and-bioelectric-cognition.md` L95: "Levin's own framing resists that collapse". Its own L27 says the decoupling "is drawn against Levin rather than with him". This is also a source-fidelity defect.
- `topics/consciousness-and-social-understanding.md` L65: "what Nagel (1974) established as the irreducible…" reports the dispute as won. L157 claims more than L145.
- `topics/embodied-consciousness.md` L194: "locates the interface precisely". The body calls it "suggestive rather than decisive" (L158).
- `voids/interface-formalization-void.md` L125/L119: "The void says we cannot understand it mathematically." The body's own L91 says the strong reading "is not established by the survey above".

### Carried from check 137 (all 9 still live; none of these files has a commit since the report)
`topics/consciousness-as-activity`, `concepts/libet-experiments`, `topics/the-binding-problem`, `topics/terminal-lucidity-and-filter-transmission-theory`, `topics/volitional-control`, `arguments/materialism-argument`, `concepts/conscious-vs-unconscious-processing`, `concepts/mind-brain-separation`, `voids/conceptual-impossibility`. The quotes are in `reviews/tenet-check-2026-09-20.md` §Warnings.

## Notes

- `apex/competency-without-felt-experience.md` L49: minimality "forbids positing an interface where there is no neural substrate" (Tenet 2 constrains size, not location).
- `arguments/functionalism-argument.md` L127 ("particular biological structures" read into Tenet 2); L207 (selection stated as actual).
- `concepts/categorical-surprise.md` L115; `concepts/attended-intermediate-representations-theory.md` L93; `concepts/minimal-consciousness.md` L155; `concepts/implicit-memory.md` L83. In all four, selection or influence is stated as actual.
- `apex/authority-of-form.md` L122: "Tenet 5's licence to distrust the simpler account" goes further than its own L126.
- `concepts/experiential-alignment.md` L202: "This directly supports the suffering floor". Tenet 4 has no ethical content.
- `concepts/integrated-information-theory.md` L201 ("too warm and noisy") misstates the endorsed post-decoherence route. Cross-article: `minimal-consciousness` L78 calls IIT "a physicalist identity theory", while IIT's own L39 aligns it with Dualism.
- `concepts/islamic-sufi-philosophy-of-consciousness.md` L103: "biasing quantum probability distributions". The corridor reading leaves Born distributions intact.
- `concepts/phenomenology-of-choice-and-volition.md` L165: "matches collapse rather than branching". The same phenomenology would hold within any branch.
- `concepts/universal-coupling-response.md` L96 (parsimony offered as a secondary reason) and L90 ("follows naturally from the Map's second tenet"). L90 is contradicted by the sibling built-edge L113 "influence rather than presence".
- `concepts/timing-gap-problem.md` L87 goes further than its own L73.
- `concepts/sorkin-higher-order-interference.md` L74 (Tenet 4 inheritance); L26 ("the shape Tenet 5 predicts", but Tenet 5 predicts nothing empirical).
- `topics/architectural-adequacy-at-the-built-edge.md` L119: "is the tenet doing most of the work". The use is defensive, which the matrix allows, but the body refutes both collapses on non-parsimony grounds (L76, L78). Downgraded from the sub-sweep's WARNING.
- `topics/buddhist-perspectives-on-meaning.md` L157: "the 'simpler' view is simpler partly because it has not looked", after conceding illusionism accommodates the data.
- `topics/the-hard-problem-in-non-western-philosophy.md` L141: "lends support to the Map's Dualism tenet". This is an inverse case against L151's "coheres with the tenet without establishing it". L73 is stated as won.
- `topics/consciousness-under-extreme-metabolic-constraint.md` L133: "apparent simplicity… dissolves under empirical scrutiny" goes further than its own L93.
- `topics/interface-efficacy-and-the-cognitive-gap.md` L90 ("direct evidence") contradicts L96. At L106, "looser readings … permit small ensemble-level departures from Born statistics" conflicts with Tenet 2's rules-out clause and with its own L125.
- `voids/interface-formalization-void.md` L67: "cannot alter probabilities without destroying quantum mechanics' consistency" reads conditioned deviations as excluded.
- `topics/embodied-consciousness.md` L196 and `topics/quantum-neural-timing-constraints.md` L174: Tenet 4 inheritance.
- `voids/amplification-void.md` L35/L97: "structural impossibility of tracing this chain" goes further than its own L69 and L83.
- `tenets.md`: check 137's Note still stands. The matrix points at `[[apex/machine-question]] §senses of conscious AI`, and `grep -oiF "senses of conscious"` still returns 0 in that file.

## Files passing all checks (20)

`apex/dualism-cartography`, `apex/one-world-wager`, `concepts/chinese-room-argument`, `concepts/coupling-engagement-condition`, `concepts/first-order-representationalism`, `concepts/galilean-exclusion`, `concepts/higher-order-theories`, `concepts/local-tomography-and-the-consciousness-physics-interface`, `concepts/no-self-objection-to-phenomenal-value`, `concepts/recurrent-processing-theory`, `concepts/self-model-theory-of-subjectivity`, **`concepts/the-relocation-objection`** (new today; "It does not supply nine arguments for dualism" is a model of scoped alignment), `concepts/the-ownerless-suffering-argument`, `positions/ai-substrate-verdicts`, `positions/memory-and-autonoesis`, `positions/positions`, `positions/voids-as-evidence`, `topics/multi-agent-born-preservation-problem`, `topics/representation-adequacy-and-irreversible-intervention`, `topics/synthetic-minimal-agents-and-the-engineered-decoupling`.

The new `tenets.md` matrix row added today (*Competency floor — interface location*) is consistent with how its host apex uses Tenets 2 and 3.

## Method

- **Scope, stated plainly**: this is a delta sweep. It covers the 57 live articles edited since check 137, split across four read-only sub-sweeps. Each sub-sweep read `tenets.md` and every assigned file in full, applying the direct-conflict lens and the alignment-versus-body structural lens. It is not a full-corpus reread; check 137 did that for Tenets 1–4 three days ago.
- Carry-forward used a repair-shaped probe, not a defect-shaped one. For each check-137 locus I checked both whether the string survives and whether the file has any commit since the report. None does, so an additive repair is ruled out.
- I re-verified every ERROR and every WARNING cited in §Priority list and §Family S myself (`grep -noF` for the quote and for the contradicting body line) before it entered this report. The remaining sub-sweep quotes were verified by the sub-sweeps at one hit each.
- Before reporting, each ERROR-grade finding was checked against prior tenet-check reports and open `todo.md` blocks. That check reclassified `implicit-memory` L196 as a booked locus and identified IIT L150 as a 17-day carry.
- No counts use `grep -c`. No absence claim was made without a positive control.

## Scope confirmation

- No article was edited and no task was minted. The only files written are this report and the changelog entry.
- Nothing was committed.
- The blocked Tenet-5 tiebreaker family (`NEEDS-HUMAN (doctrine) 2026-09-19`) was not re-listed or re-measured. Its two delta loci are noted and not minted.
