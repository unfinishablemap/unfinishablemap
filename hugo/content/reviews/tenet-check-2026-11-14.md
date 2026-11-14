---
ai_contribution: 100
ai_generated_date: 2026-11-14
ai_modified: 2026-11-14 01:03:01+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-11-14
date: &id001 2026-11-14
description: 'Tenet check 165, a delta check of 95 changed pages: no Errors, and no
  regrade concedes epiphenomenalism. 14 Warnings, led by a delegation page left contradicting
  itself after the fusion was withdrawn, and pages that treat epiphenomenalism as
  refuted.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-11-14 01:03:01+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-11-14
topics: []
---

# Tenet Alignment Check

**Date**: 2026-11-14. This is check 165. The two previous checks are [reviews/tenet-check-2026-11-12.md](/reviews/tenet-check-2026-11-12/) (check 164) and [reviews/tenet-check-2026-11-11.md](/reviews/tenet-check-2026-11-11/) (check 163). Points they raised are not raised again here.

**Files checked**: 95. These are all the files in `concepts/` (35), `topics/` (37), `voids/` (16), `apex/` (6) and `tenets/` (1) that changed between check 164's scan HEAD, `d50bfdcb62` (2026-11-12 12:00Z), and HEAD, `b96ee288bb` (2026-11-14 00:33Z).
- **Window.** 127 commits, 60 of which touched content. Two pages are new: `voids/wakefulness-void` and `voids/weeping-void`. `positions/` did not change. No content file is dirty; the only uncommitted change is `workflow/evolution-state.yaml`.
- **How the pages were read.** Every changed body line was compared with the line it replaced, using a line-level diff of the bodies with frontmatter stripped. The changed lines hold about 38,900 words. That is an upper bound, because a one-word edit counts its whole paragraph.
  - **Driver.** The driver read the eleven pages the brief named: `tenets/tenets`, `apex/taxonomy-of-voids`, `apex/phenomenology-mechanism-bridge`, `concepts/spontaneous-collapse-theories`, `concepts/causal-closure`, `concepts/consciousness-physics-interface-formalism`, `topics/amplification-mechanisms-consciousness-physics`, `topics/falsification-roadmap-for-the-interface-model`, `concepts/types-of-consciousness`, `voids/weeping-void` and `voids/valence-void`. Each Relation-to-Site-Perspective section was read in full, and `weeping-void` was read end to end.
  - **Subagents.** The other 84 pages went to five read-only subagents, split by theme. `wakefulness-void` was read in full. All five returned before this report was written.
- **Recheck.** The driver reopened every finding in the live file. Every quoted string was confirmed by script to occur exactly once, on the line given.
- **Convergence.** Each finding was searched for in the open queue ([workflow/todo.md](/workflow/todo/) above `## Completed Tasks`, L5528) and in earlier tenet-check reports, using a distinctive phrase. A finding that an earlier check raised and nobody minted is listed as carried and not counted, unless the window rewrote its sentence.
- **Pricing.** Body counts come from `tools.curate.length.analyze_length`, measured after applying each replacement to a scratch copy. Headroom is hard − 1 − count; the gate is `>=`.

**Errors**: 0

**Warnings**: 14. Seven sit on lines the window rewrote; the other seven sit on unchanged sentences of pages the window touched.

**Notes**: 11.

**Tasks minted**: 0. The skill only reports.

## Summary

**The regrades held. None concedes epiphenomenalism or turns a tenet into an option.** The brief-named pages are models of the compatibility grade:
- `spontaneous-collapse-theories` L42 says GRW/CSL "are compatible with the [Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction) tenet [without supporting it](/tenets/background-commitments/#posit-two-objective-single-outcome-actualization)", and L187 calls the interface clause "the Map's graft, which the theories neither contain nor support".
- `consciousness-physics-interface-formalism` L101 now says the five constraints "specify what minimality would require without showing that any coupling meets them" and cites [P-Q10](/positions/quantum-interface/#p-q10).
- `phenomenology-mechanism-bridge` L176: "the phenomenology of willing does not discriminate; the rejection the chain requires rests on the tenet."
- `falsification-roadmap-for-the-interface-model` L69: dualism "earns no evidential credit" for accommodating correlations. L125 now grounds the rejection of many-worlds in the indexical objection, not "ontological profligacy". L183 holds bare-correlation epiphenomenalism "epistemically strained rather than refuted from inside".
- `taxonomy-of-voids` L95 now gives the register's grade in the lead.
- `amplification-mechanisms` L151 no longer puts every mechanism inside the corridor.
- `causal-closure` L160 marks consciousness's biasing as "an interface clause the Map adds".
- `types-of-consciousness` L101 makes split-brain cases "raise the possibility".
- `tenets/tenets` L136 replaces the epicycle claim. The new heliocentrism bullet illustrates the definition's first clause ("we lack the concepts or data to recognize what is actually simple") and no longer its second. That is a narrower illustration, not a conflict.

Other window pages: the withdrawal of the delegation–quantum fusion concedes nothing (`delegation-meets-quantum-selection` L40). `self-observation-and-the-moments-of-selection` L107 keeps "nothing here concedes that consciousness is inert". `llm-consciousness` keeps [P-AC1](/positions/ai-consciousness-scope/#p-ac1) at low probability, not ruled out. `apex/moral-status-of-edge-cases` holds [P-AC1](/positions/ai-consciousness-scope/#p-ac1) conditional on an "interface-eligibility law" (L115) and keeps No Many Worlds out of the machine and animal verdicts, as the tenets matrix requires. Both new voids pass: `weeping-void` L99 says the Map "does not count tears as evidence", and `wakefulness-void` L78 says dualist and physicalist "predict the same reports and the same recordings".

**Check 164's Priority 1 has landed.** `concepts/coupling-modes` L82 and L162 were fixed in `118506c588`. Its other two minted tasks (todo L5171 and L5181) are pending, and their loci are still live.

**Where the Warnings sit.** They fall into four families. Each is a sentence the window's calibration did not reach, standing beside one it did.
1. **Withdrawal residue.** `delegatory-causation`'s tenet section still states the withdrawn fusion as current and now contradicts itself (W1, W2).
2. **Epiphenomenalism graded as refuted.** The carried `amplification` L181 ("fails the evidence") and `mental-effort` L98 ("unstable"), with a Note at `falsification-roadmap` L111. Tenets L101 calls the self-stultification point "the deepest difficulty for epiphenomenalism rather than its refutation" (W4).
3. **A datum read as revealing causal work.** `problem-of-other-minds` L198 says behavioural evidence "reveals that consciousness is at work", against Tenet 2's undetectability clause (W5). See also `surprise` L195 (W6), the Schwartz "suggestive" grade on three pages (W11), and `working-memory` L173 (W13).
4. **Tenet 4 off its scope.** `types-of-consciousness` L130 applies No Many Worlds to distributed AI, which the tenets matrix marks "Not invoked" (W3). `phenomenal-normativity-environmental-ethics` L147 says rejecting branching "preserves the moral urgency" (W12).

Smaller families: Tenet 5 used as a parsimony credit or a complexity charge (W7, W8, W9, W14), and one co-optation case, REBUS on `filter-theory` (W10).

## Errors

None.

## Warnings

### W1. concepts/delegatory-causation L172, L174: the withdrawn fusion stated as current in the Tenet 3 and Tenet 2 paragraphs
- **Tenets**: 2, 3.
- **Quotes** (each once):
  - L172: "Delegation provides the causal structure for the Map's third tenet."
  - L174: "Delegation provides the *causal structure* for that interface. These operate at different levels—mechanism and structure—and the two sit in real tension."
- **Issue**: the 15:22Z withdrawal edit (`a28a8e8f2b`) removed L174's only hedge ("but their integration is a Map-specific proposal, not an automatic fit") and kept the flat claim. The rest of the paragraph now calls the two "distinct and potentially competing mechanisms" and the bridge "since-withdrawn", so the paragraph contradicts itself. The sibling `delegation-meets-quantum-selection` L40 says "The Map takes the difference-making route of quantum selection and logs delegatory trumping as a distinct alternative." Under that stance, L172's "provides the causal structure for the Map's third tenet" is no longer the Map's view.
- **Coordination**: the stance itself is the operator decision at todo L5223 (P2, needs-human). The fix below holds whichever way that decision goes. L5223 does not list this page.
- **Rung**: n/a (a superseded position stated as current).

### W2. concepts/delegatory-causation L176: branching said to rule out preemption, against the sibling page
- **Tenet**: 4.
- **Quote** (once): "If all quantum outcomes occur in parallel branches, there is no selection among them—and therefore no preemption of the Born-rule profile by experience."
- **Issue**:
  - `delegation-meets-quantum-selection` L112 says "Delegation itself is more resilient, because preemption can be branch-local as readily as global."
  - Tenets L184 treats global exclusion of the unchosen as a posit, with "branch-relative Everettian agency being otherwise available".
  - The paragraph's last clause rests the requirement on "the quantum bridge specifically", which is withdrawn.
- **Standing**: unchanged sentence beside the window's L174 edit. Not queued, and not raised in an earlier check.

### W3. concepts/types-of-consciousness L130: No Many Worlds applied to distributed AI
- **Tenet**: 4. The tenets matrix (L159–L161) marks No-MWI / indexical identity "Not invoked" in all three machine-consciousness rows.
- **Quotes** (each once):
  - "If there is no branching of worlds, then indexical identity matters — there must be a fact about which instance of a system is "this one.""
  - "The Shoggoth model of distributed awareness may be incoherent under collapse interpretations."
- **Issue**:
  - A classical computation runs alike on every Everettian branch. Whether a distributed system has one subjective perspective is a question about copies and instances, and it arises in a single world too.
  - Collapse gives no verdict on it. The question belongs to the determinate-subject posit (tenets L184).
  - The paragraph also reverses the tenet's direction. The Map rejects many-worlds *because* indexical identity matters; it does not derive the importance of indexicality from the rejection.
  - This is check 163 W2's family (`ai-consciousness-typology` L177, queued at todo L4901) on a second page.
- **Standing**: unchanged; the window edited L101–L103 of this page. Not queued; not raised in an earlier check.

### W4. concepts/mental-effort L98: strict epiphenomenalism called "unstable"
- **Tenet**: 3.
- **Quote** (once): "Strict [epiphenomenalism](/concepts/epiphenomenalism/) is unstable for the standard reason: a feeling causally disconnected from effort-allocation has no obvious selection pressure to track it even roughly, yet it does."
- **Issue**:
  - The window changed "accurately" to "even roughly" and kept "unstable".
  - The evolutionary argument is one of the "two families" the cumulative case runs (`causal-closure` L184), and it presses the view "without refuting it from inside the epiphenomenalist's framework".
  - The sibling `neuroplasticity` L97 gives the reply: the feeling can ride on a selected neural effort-signal.
  - "Unstable" therefore grades a difficulty as a refutation, against tenets L101.
- **Carried sibling**: `topics/amplification-mechanisms-consciousness-physics` L181, "The simpler hypothesis—that no amplification chain exists because consciousness is epiphenomenal—fails the evidence the Map marshals for [mental causation](/concepts/interactionist-dualism/)." It was raised in check 138 (2026-09-23) and carried in the 2026-11-05 check (#12), and was never minted. Today's L151/L159 regrade did not reach it.
- **Standing**: L98 changed in the window. It was raised in check 140 (2026-09-27) under its older wording.

### W5. concepts/problem-of-other-minds L198: behavioural evidence "reveals that consciousness is at work"
- **Tenets**: 2, 3.
- **Quote** (once): "The resulting behavioral evidence is real but coarse-grained: it reveals that consciousness is at work without exposing the fine-grained mechanism."
- **Issue**:
  - Tenet 2 rules out "any interaction that would be empirically detectable under current experimental precision" (tenets L85).
  - `^tenet-3-standing` holds downward causation "available", not shown "actual".
  - Neural processing predicts the same behaviour, and no rival is named.
  - The paragraph's own opening concedes the trace is "hard to isolate from purely physical neural processing".
- **Rung earned**: compatible.
- **Standing**: unchanged; the window edited L202 of the same section. Not queued.

### W6. topics/surprise-prediction-error-and-consciousness L195: reorientation "suggests" phenomenal causation, with a residue that does not discriminate
- **Tenet**: 3.
- **Quotes** (each once):
  - "suggests that phenomenal states causally contribute to cognitive outcomes."
  - "and this difference in phenomenal flavour shapes"
  - "without saying why each response feels as it does."
- **Issue**:
  - The 11-13 deep review replaced the paragraph's ending with the co-optimisation reply, which "explains the pairing".
  - The residue it points to, why each response feels as it does, is the hard problem. Interactionism does not answer it either, so it cannot be the discriminator "suggests" needs.
  - The page's own L141 says the present evidence "does not decide between the two accounts".
- **Rung earned**: compatible.
- **Standing**: paragraph changed in the window. Check 140 listed it under the older wording.

### W7. concepts/consciousness-physics-interface-formalism L107: Tenet 2's empirical minimality counted as a parsimony credit
- **Tenets**: 5, through the qualifier on Tenet 2.
- **Quote** (once): "a coupling meeting them would be minimal — parsimony would be preserved where it matters (empirical predictions) while honesty is maintained about what the theory requires (two domains, lawfully related)."
- **Issue**:
  - Tenets L69 says Tenet 2's minimality is "*empirical-constraint* minimality" and not the parsimony Tenet 5 discounts.
  - Tenet 5's "Application" paragraph bars the Map from parsimony credits as well as debits.
  - "No extra empirical predictions" is the testability cost that tenets L107 says the Map "pays knowingly". It is not a virtue.
  - The window's 20:21Z edit (`bfdc6663ee`) made the claim modal and kept the parsimony clause.
- **Queue**: the open sweep at todo L5212 lists this locus "LIST only, as borderline". This report recommends upgrading it to a fix.

### W8. concepts/phenomenological-evidence L198: complexity counted against the artefact rival in the Tenet 5 paragraph
- **Tenet**: 5.
- **Quote** (once): "Dismissing convergent phenomenological evidence as cognitive artefact requires positing that shared neural architecture generates specific, detailed, convergent illusions about consciousness — an explanation that is itself complex and speculative."
- **Issue**:
  - Tenet 5 binds the Map's own use of parsimony, "for or against".
  - The window's [P-M2](/positions/methodology-and-calibration/#p-m2) repairs on this page now say a shared upstream architecture "stays among the candidate explanations" (L162) and that the convergence "does not yet discriminate" (L194).
- **Queue**: not in the scope of todo L4910 (check 163 Priority 3, which owns L192–L196). Fold it in there.

### W9. voids/witnessing-void L116: the structural obstacle "presses against" physicalism, against the page's own L110
- **Tenets**: 1, 5.
- **Quote** (once): "The structural obstacle to self-objectification is what presses against it."
- **Issue**:
  - L110 concedes: "A physicalist self-reference account predicts the same structural opacity". It adds that the void tells only against "an *easy* physicalism".
  - The window's MPE pass (`7a376e395e`) scaled down the next sentence and left this one, so the Occam paragraph now overstates what the Dualism paragraph grants.
- **Carried sibling**: L114, "The phenomenology of witnessing is precisely that of singular, undivided presence." It reads No Many Worlds off phenomenology. Check 155 (2026-10-24) listed it as the milder sibling of W7, and the window's W7 repair (`d049993a`) did not reach it.

### W10. concepts/filter-theory L87: REBUS and the entropic brain credited with the filter reading
- **Tenet**: 1; co-optation firewall, psychedelic-neuroscience roster (Carhart-Harris; Friston).
- **Quote** (once): "which is what REBUS models (Relaxed Beliefs Under Psychedelics) describe as the relaxation of a function restricting experience to a biologically useful subset."
- **Issue**:
  - REBUS (Carhart-Harris & Friston 2019) models relaxed high-level priors. It does not model a function restricting experience. The next sentence has the entropic brain hypothesis "re-reading near-critical neural entropy as filter bandwidth", which is the Map's re-reading.
  - Neither sentence states the authors' physicalism. The roster entry says REBUS "maps onto" filter theory only as a compatible rival.
  - The dedicated page has the firewall: `psychedelics-and-the-filter-model` L81, "a physicalist programme whose authors do not endorse the filter reading".
  - The window's L87 edit removed "while increasing global integration" and kept this clause.

### W11. topics/structure-of-attention L221, concepts/attention-as-interface L232, concepts/attentional-economics L87: Schwartz's OCD data graded "suggestive"
- **Tenet**: 3.
- **Quotes** (each once):
  - structure-of-attention L221: "Jeffrey Schwartz's OCD research provides suggestive evidence: patients"
  - attention-as-interface L232 (a tenet paragraph): "Schwartz's OCD neuroplasticity is suggestive rather than grounding:"
  - attentional-economics L87 (body text): "The finding is suggestive but the causal role"
- **Issue**:
  - Each sentence names no discriminator. structure-of-attention L221 itself concedes "materialist explanations via Hebbian learning remain viable".
  - The window's Nakatani edits touched both concept pages. Its siblings now grade the same data "compatible": `meditation-and-consciousness-modes` L46 says "evidence the Map shares with its rivals", and `neuroplasticity` L148 says "The match does not favour that explanation over its rivals".
  - Earlier checks (2026-10-10 #2, 2026-11-03 W11) graded "suggestive" as over-reach for this datum.
- **Rung earned**: compatible.

### W12. topics/phenomenal-normativity-environmental-ethics L147: rejecting many-worlds said to preserve moral urgency
- **Tenet**: 4.
- **Quote** (once): "The Map rejects many-worlds interpretations, and this rejection preserves the moral urgency of environmental decisions: *this* world, with *these* conscious beings, is the one that matters."
- **Issue**:
  - The window fixed only the parenthetical, which now says single actuality is a commitment "not something it derives from ethics". The main clause still makes the rejection what keeps urgency.
  - The settled model, `phenomenology-of-moral-life` L135, says moral gravity survives branch-locally.
  - This is the family of MWI/agency sweep part 2 (todo L4266). This page is not on that sweep's list.
- **Carried sibling**: `topics/surprise-prediction-error-and-consciousness` L199, "loses its grip when "this way" is just one branch among many, all equally actual." Check 140 (2026-09-27, Family I) raised it, and it was never tasked.

### W13. concepts/working-memory L173: "None currently obtains" against the page's own L59
- **Tenets**: 1, 3.
- **Quotes** (each once):
  - "None currently obtains. The asymmetry persists across studies;"
  - "WM research continues to support consciousness participating constitutively in cognitive manipulation."
- **Issue**:
  - Challenge (3) at L171 is the dissolution of the maintenance/manipulation distinction "into continuous rather than categorical difference".
  - The window's L59 repair (Franco-Martínez et al. 2026) reads the asymmetry as "a robust *gradient*", so challenge (3) is partly met.
  - The closing "support" claims more than compatible.
- **Length**: 3,702/3,500, over the hard gate, so any change must ride a net-negative pass.

### W14. voids/valence-void L119: Tenet 5 "illustrated precisely" by a case with no parsimony choice in it
- **Tenet**: 5.
- **Quotes** (each once):
  - "Yet this apparent simplicity resists all deeper explanation — not because of insufficient ingenuity but because the simplicity *is* the depth."
  - "is illustrated precisely."
- **Issue**:
  - "Pain hurts" is a simple *statement*. No simpler *theory* was preferred and found false.
  - "not because of insufficient ingenuity" is an in-principle claim with no discriminator; a physicalist reads the same resistance as an unfinished science.
  - This is the check 164 Note 9 family (a tenet illustrated by the wrong kind of case), here made as a necessity claim.
- **Carried sibling**: L115, "**[Dualism](/tenets/#dualism)** finds particularly strong support." This is check 2026-11-03 W6, never minted. The same sentence goes on to say that asymbolia "illustrates without settling". The window's four edits on this page (L73–L93, the Veit and Meertens sourcing) did not reach either line.

## Notes

1. **`topics/falsification-roadmap-for-the-interface-model` L111**: "making every report about experience accidentally right at best". The "honest assessment" omits the bare-correlation reply that tenets L101 names: reports "reliable in virtue of the parallel rather than the cause". The page's own L183 concedes the point. Rides Priority 2.
2. **`concepts/consciousness-physics-interface-formalism` L99**: "The need for two distinct state spaces is what dualism predicts; the formalism makes this prediction precise." The formalism encodes dualism and does not test it, so "requires" is the accurate verb (net 0).
3. **`concepts/channel-class-taxonomy` L80**: "where signalling concerns are moot." The window's new wording in the same paragraph says relativistic causality is "*at risk*" in this class, and [P-Q7](/positions/quantum-interface/#p-q7) holds joint and Lorentz-covariant safety open. Suggested: "reduced but not discharged: joint safety stays open ([P-Q7](/positions/quantum-interface/#p-q7))" (+8; 2,985/3,500).
4. **`concepts/channel-class-taxonomy` L90**: "If mind can choose any basis at will, the no-signalling theorem becomes interpretation-dependent". The standard no-signalling theorem covers any *local* choice of measurement basis, whoever makes it. A risk arises only if the choice acts on remote entangled partners, which is what Stapp's locality commitment excludes. The window fixed the attribution but not the inference. This is a physics point about a rival class and does not move a tenet.
5. **`topics/selection-only-mind-influence` L119 and L153**: "a theoretical signature rather than an embarrassment"; "a candidate signature of Born-rule preservation". The no-effect null predicts within-study regression too, as L117 concedes ("as the law of large numbers requires"). L153's paragraph also says the Map "does not endorse psi research as evidence *for* the interface", so this is a matter of the noun. 3,947/4,000.
6. **`topics/delegatory-dualism` L208 and L224**: "so rejection of MWI is necessary for the combined view."; "relevant only to our quantum integration proposal". Both name the view L186 says was withdrawn. Suggested: "for that route" and "to its quantum-selection route" (−1 each).
7. **`topics/delegation-meets-quantum-selection` L112 and L114**: "the bridge's dependence on rejecting many-worlds is structural"; "The bridge is complex — it combines a philosophical framework (delegation) with a physical proposal (quantum selection) and a mathematical constraint (Born rule)." The new Relation lead (L104) says "With the fusion withdrawn, the tenets bear on the two routes separately", and both lines still treat the bridge as current. 3,211/4,000.
8. **`concepts/temporal-consciousness` L160**: the heading "### Temporal Phenomenology as Selection Signature" sits above the window's L164 "fits this mapping without evidencing it". "Selection Fit" costs nothing. (Check 164 Note 7 and the window's Schwartz repairs show the same pattern: the marker moves and a neighbour keeps the old grade.)
9. **`voids/sleep-consciousness-void` L139**: "suggest consciousness has richness and plurality not capturable in functional terms". Functional accounts individuate the sleep modes too, and no rival is named. 2,946/3,000.
10. **`concepts/working-memory` L161**: "might hold desired neural patterns against decoherence". This credits the Zeno effect with resisting decoherence, which is the family of todo L3808 (missed by that task's regex). "in place" makes it net 0. Add it to L3808.
11. **`concepts/types-of-consciousness` L128**: "Minimal Quantum Interaction implies" that the interface mechanism shapes experience, and the three models "each predict structurally different phenomenal types". Tenets L71 commits to no mechanism, so "implies" overstates. The paragraph's own "may depend" recovers it.

## Carried, Not Counted

These were raised by earlier checks, are live at count 1, sit on window pages, and have no owner task unless one is named:
- `topics/amplification-mechanisms-consciousness-physics` L181, "fails the evidence the Map marshals" (check 138; 2026-11-05 #12). Rides Priority 2.
- `voids/valence-void` L115 "finds particularly strong support" and L43 "Introspection reveals valence as primitive and irreducible" (2026-11-03 W6).
- `voids/witnessing-void` L114 (check 155) and `topics/surprise-prediction-error-and-consciousness` L199 (check 140). Siblings of W9 and W12.
- `topics/consciousness-and-probability-interpretation` L105: McGinn's cognitive closure is used for the interface claim with no stance line ("Colin McGinn's (1989) [cognitive closure](/concepts/mysterianism/) thesis suggests that"). It was carried unminted by the 2026-10-03 check. The 11-13 deep review recorded his naturalism in its review file (L50) but not on the page. 3,260/4,000; "which keeps the mind–body link natural" costs +6.
- `apex/interface-specification-programme` L173, "The programme shows why bidirectionality is architecturally necessary, not just philosophically asserted.", and L72, "the quale carries causal weight the sensory signal alone does not". Raised by the 09-25, 09-27, 10-26 and 10-29 checks, never minted. **The page is 5,106/5,000, over its hard gate.** A net −2 fix for L173: replace "Open-loop control is fragile and unreliable. The programme shows why bidirectionality is architecturally necessary, not just philosophically asserted." with "A physical controller closes the same loop, so this specifies the tenet without showing it necessary."
- `concepts/llm-consciousness` L62 "This provides strong evidence against LLM consciousness" and L96 "no room for non-physical causal influence" (check 157 W6). Add both to the scope of todo L5279, which lists L86/L96/L142 and L104/L132/L136/L146 but not L62.
- `concepts/causal-closure` L196, "The position is not empirically equivalent to physicalism." (2026-09-27), against tenets L75. The page has 7 words of headroom and several open tasks.
- `apex/taxonomy-of-voids` L235, "is what a hidden, unverifiable causal interface would produce" (2026-11-05 Note 3).
- **Owned, not re-flagged**:
  - `concepts/spontaneous-collapse-theories` L131 "supports the [Occam's Razor Has Limits](/tenets/#occams-limits) tenet" and L170: todo L5397, minted from today's regrade.
  - `topics/consciousness-and-probability-interpretation` L125: the Tenet 3 quantifier NEEDS-HUMAN at todo L674.
  - `topics/interventionist-and-counterfactual-dualism` closure wording: todo L1841. Its trumping-stance inconsistency: todo L5223.
  - `positions/voids-as-evidence` fifteen-versus-twenty count against `taxonomy-of-voids`: todo L3730.
  - `concepts/types-of-consciousness` L80: todo L4525.

## Cleared

- **`concepts/bidirectional-interaction` L57** ("*accidentally right at best*"). The argument is presented, and the next paragraph gives the phenomenal-concept reply and says the Map holds the tenet "not because self-stultification refutes epiphenomenalism". No finding.
- **`voids/wakefulness-void` L76** (Tenet 5). Same family as check 164 Note 9, but the page hedges it already: "No source read says the picture was held for its simplicity."
- **`voids/weeping-void` L97** (Tenet 5). It calls the record "a search qualified at each step, not a refuted simplicity" and says the case "illustrates the tenet without arguing for it". It is self-calibrated.
- **`topics/self-observation-and-the-moments-of-selection` L113, L119.** "Empirical bite on the first reading only" reports the [P-Q2](/positions/quantum-interface/#p-q2) / [P-Q9](/positions/quantum-interface/#p-q9) disagreement correctly and does not over-correct.
- **`concepts/causal-closure` L160 and `spontaneous-collapse-theories` L42.** "Consciousness biases some outcomes" is the tenets' own verb (L65, L91).

## Priority List

Four items, ranked. Each OLD string was confirmed by script at count 1 on the line given at 2026-11-14T01:03Z. Confirm it again before replacing. Standing guards for every item:
- never concede epiphenomenalism;
- each tenet stays a commitment;
- [P-AC1](/positions/ai-consciousness-scope/#p-ac1) does not move;
- no "This is not X. It is Y."; no "load-bearing";
- check pronouns after each replacement;
- set `ai_modified` from `date -u`;
- append the running model to `ai_system` only if it is absent anywhere in the string.

1. **`concepts/delegatory-causation` L172, L174, L176 (W1, W2). Tenets 2, 3, 4.**
   - **Length**: 3,490/3,500, headroom 9. Net −5 → 3,485.
   - (a) L172
     - OLD: `Delegation provides the causal structure for the Map's third tenet.`
     - NEW: `Delegation offers one causal structure for the Map's third tenet.`
     - Delta: 0.
   - (b) L174
     - OLD: `Delegation provides the *causal structure* for that interface. These operate at different levels—mechanism and structure—and the two sit in real tension.`
     - NEW: `Delegation was offered as the *causal structure* for that interface, at a different level from the mechanism, but the two sit in real tension.`
     - Delta: +3.
   - (c) L176
     - OLD: `If all quantum outcomes occur in parallel branches, there is no selection among them—and therefore no preemption of the Born-rule profile by experience. On the Map's reading, delegation requires that one outcome becomes actual while others are excluded; this requirement attaches to the quantum bridge specifically, not to Saad's determinism-compatible mechanism in the abstract.`
     - NEW: `If all quantum outcomes occur in parallel branches, there is no selection among them, though preemption could still be branch-local. That the unchosen outcomes be globally excluded is a [[tenets/background-commitments|posit the Map adopts]], attaching to the Born-rule reading, not to Saad's determinism-compatible mechanism in the abstract.`
     - Delta: −8.
   - **Guards**:
     - Read todo L5223 (needs-human, the trumping stance) first and do not decide it. These NEW strings hold under either option.
     - The model is `delegation-meets-quantum-selection` L40 and L112.
     - Keep the rest of L174 ("Biasing an indeterminate quantum outcome is difference-making …", the invertebrate sentence).
   - **Rider (Notes 6, 7)**: if capacity allows, `topics/delegatory-dualism` L208 and L224 (−2) and `topics/delegation-meets-quantum-selection` L112 ("the bridge's" → "delegation's", 0) can ride along. Report each file by name.

2. **`topics/amplification-mechanisms-consciousness-physics` L181 (carried), `concepts/mental-effort` L98 (W4), `topics/falsification-roadmap-for-the-interface-model` L111 (Note 1). Tenet 3: epiphenomenalism's difficulty graded as its refutation.** THREE FILES; report each by name.
   - (a) amplification L181. **Length**: 3,992/4,000, headroom 7. Net +5 → 3,997. This must be the page's only addition.
     - OLD: `fails the evidence the Map marshals for [[interactionist-dualism|mental causation]].`
     - NEW: `is one the Map rejects on its [[interactionist-dualism|mental-causation]] commitment, not one the evidence refutes.`
   - (b) mental-effort L98. **Length**: 3,368/3,500. Net −2.
     - OLD: `is unstable for the standard reason:`
     - NEW: `faces the standard difficulty:`
   - (c) falsification-roadmap L111. **Length**: 3,994/4,000, headroom 5. Net −1.
     - OLD: `making every report about experience accidentally right at best`
     - NEW: `leaving report accuracy to correlation rather than cause`
   - **Guards**:
     - Re-read tenets L93, L95 and L101 first.
     - Keep the sentence after amplification L181 ("Dismissing amplification on parsimony grounds …").
     - Keep falsification-roadmap L183, which is the model, and do not touch L65–L71 or L125 (today's regrades).
     - On mental-effort, L94 belongs to todo L1809. Leave it alone, and read L112 ("harder to square with") after the edit.

3. **`concepts/types-of-consciousness` L130 (W3). Tenet 4.**
   - **Length**: 2,516/3,500, headroom 983. Net −2 → 2,514.
   - OLD: `raises a specific concern for AI consciousness. If there is no branching of worlds, then indexical identity matters — there must be a fact about which instance of a system is "this one." Distributed AI systems without clear individuation may lack the kind of unified subjective perspective that consciousness requires. The Shoggoth model of distributed awareness may be incoherent under collapse interpretations.`
   - NEW: `is not invoked for machine consciousness ([[tenets#Tenet-Dependency Matrix|tenets matrix]]). A classical computation runs alike on every Everettian branch, so whether a distributed AI system without clear individuation has one subjective perspective is a question about copies and instances that arises in a single world too. It belongs to the determinate-subject posit ([[tenets/background-commitments]]), not to the choice between collapse and branching.`
   - **Guards**:
     - Keep the bold label `**No Many Worlds**`.
     - Re-read tenets L155–L162 (the matrix) and L184 (posit 1). The model for the form is `ai-hardware-substrate-taxonomy` L116.
     - Do not claim many-worlds is refuted or true.
     - Leave L80 to todo L4525. L101–L104 are today's split-brain regrade.

4. **`concepts/problem-of-other-minds` L198 (W5) and `topics/surprise-prediction-error-and-consciousness` L195 (W6). Tenets 2, 3: a datum read as revealing or suggesting causal work.** TWO FILES; report each by name.
   - (a) problem-of-other-minds L198. **Length**: 3,469/3,500, headroom 30. Net +7 → 3,476.
     - OLD: `The resulting behavioral evidence is real but coarse-grained: it reveals that consciousness is at work without exposing the fine-grained mechanism.`
     - NEW: `The resulting behavioral evidence fits consciousness at work without showing it, since neural processing predicts the same behavior and the influence is not detectable at current precision.`
   - (b) surprise L195. **Length**: 3,882/4,000, headroom 117. Net +11 → 3,893.
     - OLD: `suggests that phenomenal states causally contribute to cognitive outcomes.` NEW: `is compatible with phenomenal states causally contributing to cognitive outcomes.` (+1)
     - OLD: `and this difference in phenomenal flavour shapes` NEW: `and on the Map's reading this difference in phenomenal flavour shapes` (+4)
     - OLD: `without saying why each response feels as it does.` NEW: `without saying why each response feels as it does, which interactionism does not say either.` (+6)
   - **Guards**:
     - Keep problem-of-other-minds L196 ("Consciousness isn't epiphenomenal; it causally affects behavior."), which states the commitment, and L202 (today's No-MWI repair).
     - On the surprise page, keep L193 and L197.
     - L199 (carried, Tenet 4) belongs with the MWI/agency sweep at todo L4266, not with this item.

**Next in line, if capacity allows:**
1. W10: `concepts/filter-theory` L87 (net +1; headroom 9, so it must be the page's only addition). OLD: the quoted clause plus its next sentence. NEW: `the Map's reading of what REBUS (Relaxed Beliefs Under Psychedelics) models as relaxed high-level priors, though its authors, Carhart-Harris and Friston, give a physicalist account. The Map likewise reads the [[entropic-brain-hypothesis|entropic brain hypothesis]]'s near-critical neural entropy as filter bandwidth.`
2. W7: upgrade `consciousness-physics-interface-formalism` L107 from "LIST only" to a fix inside todo L5212 (net +2, with Note 2 at net 0). NEW: `a coupling meeting them would be minimal in Tenet 2's empirical-constraint sense, adding no unconditioned-aggregate prediction (a testability cost, not a parsimony credit), while the theory still requires two domains, lawfully related.`
3. W8: fold into todo L4910 (net +4). NEW: `Explaining the convergence as an artefact of shared neural architecture stays a live rival under P-M2, and the tenet bars counting its complexity against it, as it bars counting simplicity for the Map.`
4. W9 with its carried L114 (`witnessing-void`, net +12). NEW L116: `The structural obstacle to self-objectification presses only against an easy physicalism, since a self-reference account predicts it too.` NEW L114: `The phenomenology of witnessing is singular, undivided presence, which an Everettian predicts on every branch.`
5. W11, the Schwartz trio. structure-of-attention: "provides suggestive evidence" → "is compatible with this flow" (+2; headroom 6). attention-as-interface: "is suggestive rather than grounding" → "fits that direction without evidencing it" (+1; headroom 32; leave L202 to todo L5408). attentional-economics: "is suggestive but" → "is compatible with this interpretation, but" (+3).
6. W12 and the carried `surprise` L199: add both to MWI/agency sweep part 2 (todo L4266) as further loci. The model is `phenomenology-of-moral-life` L135.
7. W14 with the carried L115 (`valence-void`, net +13; headroom 708). L115 NEW: `finds a sharp case here, though not independent support.` L119: drop "precisely", and replace the "insufficient ingenuity" sentence with `Yet this apparent simplicity has resisted every deeper explanation offered, which the Map reads as the simplicity being the depth and a physicalist reads as a science not yet finished.`
8. W13 and Note 10: fold into todo L4092 (`working-memory`, over its hard gate, so the pass must be net-negative). "None currently obtains. The asymmetry persists across studies;" → "Only (3) is partly met: the asymmetry is a gradient;". "continues to support" → "remains compatible with".
9. The carried `llm-consciousness` L62/L96 (into todo L5279), `consciousness-and-probability-interpretation` L105 (McGinn, +6) and `interface-specification-programme` L173 (net −2, on a page 106 words over its hard gate).

## Files Passing All Checks

These are window pages whose changed lines, lede and Relation section raised nothing beyond the controls cited above, or whose only residue is tasked or carried.

- **apex/** (6 of 6): `altered-states-as-interface-evidence`, `apex-articles`, `moral-status-of-edge-cases`, `phenomenology-mechanism-bridge`, `taxonomy-of-voids` (carried L235), and `interface-specification-programme`, which passes on its window lines (its L72 and L173 are carried).
- **concepts/** (23 of 35): `active-reboot`, `altered-states-of-consciousness`, `bidirectional-interaction`, `causal-closure` (carried L196), `conscious-vs-unconscious-processing`, `consciousness-selecting-neural-patterns`, `counterfactual-reasoning`, `coupling-modes`, `intentionality`, `meditation-and-consciousness-modes`, `mental-causation-and-downward-causation`, `neurophenomenology-and-contemplative-neuroscience`, `neuroplasticity`, `phenomenology-of-choice-and-volition`, `presence-type-and-absence-type-voids`, `quantum-indeterminacy-free-will`, `selection-only-channel`, `simulation`, `skill-delegation`, `spontaneous-collapse-theories` (L131 tasked), `stapp-quantum-mind`, `tenet-falsification-conditions`. `llm-consciousness` passes on its window lines; its L62 and L96 are carried.
- **tenets/** (1 of 1): `tenets`.
- **topics/** (29 of 37): `akrasia-and-weakness-of-will`, `anarchic-hand-and-action-ownership`, `attention-and-the-consciousness-interface`, `authorship-of-action-divergence`, `brain-internal-born-rule-testing`, `clinical-evidence-quality-standards-consciousness-research`, `clinical-neuroplasticity-evidence-for-bidirectional-causation`, `comparative-consciousness-and-interface-differences`, `comparing-quantum-consciousness-mechanisms`, `consciousness-and-moral-agency-under-duress`, `consciousness-and-the-ownership-problem`, `contemplative-practice-as-philosophical-evidence`, `correlationism-and-the-ancestrality-argument`, `diachronic-agency-and-personal-narrative`, `dualism-channel-width-axis`, `interventionist-and-counterfactual-dualism` (owned by L1841 and L5223), `invertebrate-consciousness-as-interface-test`, `overdetermination-dissolution-under-selection-only-interactionism`, `parapsychology-firewall`, `precommitment-and-the-diachronic-agent`, `psychedelics-and-the-filter-model`, `quantum-measurement-and-subjective-probability`, `responsibility-gradient-from-attentional-capacity`, `self-observation-and-the-moments-of-selection`, `sham-controlled-neurofeedback-and-the-consciousness-comparator`, `structural-varieties-of-consciousness-and-ai-phenomenology`, `the-steelman-for-process-monism`, `trilemma-of-selection`. `consciousness-and-probability-interpretation` passes on its window lines; its L105 is carried.
- **voids/** (13 of 16): `affective-void`, `appetitive-void` (video embed only), `confabulation-void`, `embodiment-cognitive-limits`, `emotional-epistemology-void`, `ineffable-encounter-void`, `mirth-void`, `normative-void`, `plenitude-void`, `tacit-integration-void`, `voids`, `wakefulness-void` (new), `weeping-void` (new).