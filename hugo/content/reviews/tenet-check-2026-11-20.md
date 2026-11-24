---
ai_contribution: 100
ai_generated_date: 2026-11-20
ai_modified: 2026-11-20 14:12:18+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-11-20
date: &id001 2026-11-20
description: 'Tenet check 169, a delta check of the 69 pages edited since 2026-11-19:
  no Errors. 7 Warnings, all over-reach; four are sentences the window''s calibration
  edits left above grade on pages they otherwise repaired.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-11-20 14:12:18+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-11-20
topics: []
---

# Tenet Alignment Check

**Date**: 2026-11-20
**Files checked**: 69 (every page under topics, concepts, voids, apex and positions with a commit since 2026-11-19T00:00Z; apex 7, concepts 22, topics 30, voids 10, positions 0)
**Errors**: 0
**Warnings**: 7 (all over-reach)
**Notes**: 9

## Summary

No edit in the window contradicts a tenet, concedes epiphenomenalism, endorses many-worlds, or uses parsimony as a decisive argument against dualism. The window was mostly calibration work. It repaired 14 of the sentences the 2026-11-18 check listed (about 12 above grade, the rest borderline) in 9 files, and today's large rewrites hold the register's grade: `voids/plenitude-void`, `concepts/phenomenal-overflow`, `concepts/consciousness`, `topics/dualist-perception`, `topics/consciousness-and-counterfactual-reasoning` and the AI-consciousness apex pair.

The new failure is local inconsistency. In four pages a calibration edit fixed one sentence and left a neighbouring sentence at the old grade, so each page now says two different things:

- `topics/pragmatist-quantum-foundations-and-the-agent` now says the agents are "congenial and no more" at L135, while L103 still says they corroborate Tenet 1 and are "exactly the shape dualism predicts".
- `voids/interested-party-void` gained "support no tenet" at L98, and L100 still says the fifth tenet "gains additional force here".
- `concepts/interface-threshold` now concedes at L64 that the clustering "does not by itself decide between the models"; L116 still says the pattern "fits a dualist reading better".
- `topics/consciousness-in-smeared-quantum-states` L124 was edited in the window and kept "reinforces the Map's position" for a datum that its sibling `topics/dualist-perception` L166 says cannot decide the point.

These four make up the priority list. Three further warnings are older sentences on pages the window touched for other reasons.

Method. I extracted the window's body diff for all 69 files: 447 changed paragraphs, frontmatter excluded, with word-level markers. I read every changed paragraph, and I read the whole "Relation to Site Perspective" section of the 19 pages rewritten most heavily. I ran three grep passes over the full current body text of all 69 files: 15 contradiction and over-claim patterns, 9 more contradiction probes, and the co-optation roster restricted to tenet sections. I read each hit in context. Every quoted string below has `str.count == 1` in the live file. I did not run the 2026-11-18 corpus-wide support-language survey again; this report only tracks the change in its findings.

## Errors

None.

Contradiction probes, all over the current text of the 69 files: Map concessions of epiphenomenalism; "epiphenomenalism is true or correct"; experience "could be idle"; many-worlds "true", "accepted" or "most plausible"; "consciousness is just / an illusion / reducible"; parsimony "decisively" or "conclusively" favouring physicalism; "consciousness cannot cause"; energy injection; detectable Born deviation; "dualism is false". Every hit was a rival quoted, a conditional premise, a stated rejection, or a concession that an argument fails to refute (the phenomenal-concept reply, which `tenets.md` itself concedes). The two places where an AI's experience might be causally idle (`apex/machine-question` L195 and `apex/open-question-ai-consciousness` L165) follow the open Tenet 3 quantifier decision, as Note 3 below explains, and are not errors.

## Warnings

### W1. [topics/pragmatist-quantum-foundations-and-the-agent.md](/topics/pragmatist-quantum-foundations-and-the-agent/) L103 (page now internally inconsistent)
- **Tenet**: Dualism (over-reach)
- **Quote**: "Under dualism, "primitive and irreducible" is not a concession but a prediction: any physics that requires conscious agents at its foundations *should* find those agents irreducible within its own vocabulary. QBism's agent-shaped hole is exactly the shape dualism predicts." Further on: "so the argument here corroborates Tenet 1 rather than establishing it;"
- **Issue**: L135 was repaired in the window. It now reads: "Under Tenet 1 the Map reads this as congenial and no more: an unexplained primitive is not by itself evidence of irreducibility, and a pragmatist who declines the dualist gloss keeps the same agents." That repair names the rival who predicts the same hole, which leaves L103's "exactly the shape dualism predicts" and "corroborates" without a discriminator. L103 dates from 2026-04-23.
- **Rung earned**: compatible.

### W2. [voids/interested-party-void.md](/voids/interested-party-void/) L100 (a mixed section created by the window's edit)
- **Tenet**: Occam's Razor Has Limits (over-reach; [P-V3](/positions/voids-as-evidence/#p-v3), [P-M1](/positions/methodology-and-calibration/#p-m1))
- **Quote**: "The [fifth tenet](/tenets/#occams-limits)---Occam's Razor Has Limits---gains additional force here: our epistemic preferences, including the preference for parsimony, may themselves be motivated rather than neutral."
- **Issue**: Two lines above, the 2026-11-20 positive-illusions fold added "The positive-illusions studies support no tenet; none of their authors argues for dualism ([P-V3](/positions/voids-as-evidence/#p-v3))." The section therefore states [P-V3](/positions/voids-as-evidence/#p-v3) and then credits the void with force for a tenet. On [P-M1](/positions/methodology-and-calibration/#p-m1), a reason to distrust parsimony judgements removes a defeater and adds no weight. Under the 2026-11-18 scheme the page moves from class D (silent) to class B (mixed).
- **Rung earned**: compatible (illustration). An open task at todo L6145 owns other sentences on this page; this one is not among them.

### W3. [concepts/interface-threshold.md](/concepts/interface-threshold/) L116 (out of step with the edited body)
- **Tenet**: Dualism (over-reach)
- **Quote**: "The cluster-not-gradient pattern fits a dualist reading better than a pure neural-complexity story, but the threshold concept does not by itself force dualism"
- **Issue**: The window edited L64, which now reads "Gradual amplification can match that pattern only if returns accelerate sharply enough, so the clustering does not by itself decide between the models." The rest of L116 also grants that "dualist and physicalist readings [are] each free to identify that condition differently." The sentence therefore names no feature that only the dualist reading entails. L116 dates from 2026-05-11.
- **Rung earned**: compatible.

### W4. [topics/consciousness-in-smeared-quantum-states.md](/topics/consciousness-in-smeared-quantum-states/) L124 (edited in the window; over-claim kept)
- **Tenet**: No Many Worlds (over-reach)
- **Quote**: "but Albert and Loewer's core insight—that conscious experience is always definite—reinforces the Map's position."
- **Issue**: The window inserted the Neven et al. clause into this sentence but kept "reinforces". Albert and Loewer build definiteness into a no-collapse framework, so the datum cannot favour a single world. The sibling page puts it plainly: "Phenomenal determinacy cannot decide the point, since decoherence predicts definite experience within each branch" (`topics/dualist-perception` L166). The next sentence on L124 already limits the claim ("Definiteness does not by itself require consciousness to participate in selection"), so only the verb is above grade.
- **Rung earned**: compatible.

### W5. [concepts/ai-epiphenomenalism.md](/concepts/ai-epiphenomenalism/) L63 (older text on an edited page)
- **Tenet**: Bidirectional Interaction (a posit stated as a result; `tenets#^tenet-3-standing`)
- **Quote**: "The [consciousness-as-amplifier](/concepts/consciousness-as-amplifier/) framework makes this concrete: consciousness does genuine causal work in biological systems precisely because those systems expose quantum indeterminacies at decision-relevant points."
- **Issue**: The tenets page says "Articles asserting that consciousness does 'real work' or 'genuine causal work' inherit that debt rather than discharge it, and should read no more confidently than this paragraph does." This sentence states that work flatly and gives the reason as fact. It is the only flat "genuine/real causal work" sentence among the 69 pages; the other hits are conditional (`phenomenology-of-forgetting` L103) or denials (`emotion-and-dualism` L137). The window's edits on this page were a citation fix and a cross-reference. An open task at todo L2459 owns L51, L81 and L111 on this page, but not L63.
- **Rung earned**: a posit, which the sentence should say ("on the Map's posit").

### W6. [topics/dualist-perception.md](/topics/dualist-perception/) L162 (older text on an edited page)
- **Tenet**: Bidirectional Interaction (over-reach)
- **Quote**: "all suggest that consciousness shapes the perceptual field rather than passively receiving it"
- **Issue**: The data listed (binding, constancy, bistable selection, attention gating) are predicted equally by an identity theorist, on whom conscious processes shape perception because they are neural. The only rival they tell against is epiphenomenalism, and the paragraph does not say so. The Dualism paragraph directly above (L160) gives the rival-naming form this paragraph lacks.
- **Rung earned**: compatible against physicalism; suggestive against epiphenomenalism only.

### W7. [concepts/self-and-self-consciousness.md](/concepts/self-and-self-consciousness/) L68 (older text on an edited page)
- **Tenet**: Dualism (over-reach)
- **Quote**: "The Unfinishable Map treats both the minimal self and self-consciousness as evidence that consciousness has features no physical description captures."
- **Issue**: "treats ... as evidence", with no discriminator and no rival named. The same page's Occam paragraph (L194) leaves the choice "to metaphysical fit". The window's edit on this page was the Duch quotation. Headroom is 2 words (3497 of 3500), so any repair must be net-zero.
- **Rung earned**: the Map's reading ("reads ... as showing").

## Notes

1. [concepts/consciousness.md](/concepts/consciousness/) L137, in a paragraph edited in the window: "The agreement supports a case substantially stronger than any single argument, not five independent confirmations". The paragraph now groups the arguments into two clusters plus the argument from reason, and it points to the convergence page. That is close to grade under [P-M2](/positions/methodology-and-calibration/#p-m2). "Substantially" is the only word at risk.
2. [concepts/consciousness.md](/concepts/consciousness/) L196 (older text): "Consciousness participates in this selection, making indexical identity coherent." This folds the Tenet 2/3 mechanism into the Tenet 4 line. The window's new lead at L188 ("chosen starting points, not results the Map reports") makes the line a commitment, so it is not over-reach, but it paraphrases Tenet 4 more widely than `tenets.md` does.
3. The AI cluster is consistent on the Tenet 3 quantifier after the window: `apex/open-question-ai-consciousness` L177 ("read as universal actual efficacy, rules out epiphenomenal AI experience") and L165 ("excluded on the actual-efficacy reading of Tenet 3, open on the dispositional one"); `apex/machine-question` L195 ("on a dispositional or existential reading the possibility runs inside the framework"); `concepts/ai-epiphenomenalism` (not settled at tenet level). This is the open NEEDS-HUMAN decision recorded in the 2026-11-18 report and is not a defect.
4. [concepts/zombie-master-argument.md](/concepts/zombie-master-argument/) L122 and L126 (older text): "(different quantum outcome distributions)" and "A world physically identical to ours would require the same quantum outcome distributions, which under the Map's framework require conscious biasing." On the corridor reading ([P-Q2](/positions/quantum-interface/#p-q2): Born statistics preserved exactly), a world without consciousness would have the same distributions and differ only in token outcomes. This is not a contradiction, because [P-Q3](/positions/quantum-interface/#p-q3) keeps conditioned deviations live, but "distributions" is in tension with Tenet 2's undetectability. "Token outcomes" would be accurate.
5. [topics/consciousness-and-counterfactual-reasoning.md](/topics/consciousness-and-counterfactual-reasoning/) L112, edited in the window: "the richer explanation, involving irreducible conscious processing, may be closer to the truth despite its ontological cost". This uses Tenet 5 as a reason to entertain the richer account, hedged by "may". It is in the same watch-list form as the 2026-11-18 "licenses" items and needs no action.
6. [topics/pain-consciousness-and-causal-power.md](/topics/pain-consciousness-and-causal-power/) L170, in a paragraph edited in the window: "Pain provides the most intuitive support for irreducibility." "Intuitive" qualifies the grade, so this is borderline. The Bidirectional paragraph on the same page (L172) is a model of the grade: "a pattern compatible with phenomenal causation rather than evidence for it".
7. [topics/phenomenology-of-forgetting.md](/topics/phenomenology-of-forgetting/) L103 (older sentence; the window edited the Mamat & Anderson clause in the same paragraph): "If that intention is doing genuine causal work, then a non-physical (or at least irreducibly mental) act is reaching down into neural tissue and altering it." The consequent does not follow for an identity theorist, and L105 answers only the epiphenomenalist. The page's closing grade (L109, "not as settled evidence for it") keeps the whole page compliant.
8. [voids/interested-party-void.md](/voids/interested-party-void/) L102 (older text): "If consciousness is epiphenomenal, the investigation itself becomes inexplicable". This states self-stultification more flatly than `tenets.md` ("the deepest difficulty for epiphenomenalism rather than its refutation"). It could be folded into the W2 edit.
9. Not a tenet issue, noted for the attribution sweep: [topics/consciousness-in-smeared-quantum-states.md](/topics/consciousness-in-smeared-quantum-states/) L118 and L122 still say "Koch's hypothesis" and "Koch proposes a third option". The window renamed this model "Neven's" in `apex/open-question-ai-consciousness` and cites Neven et al. (2024) at L124 of the same page.

## Change since the 2026-11-18 report

**Repaired in the window** (14 sentences in 9 files): `topics/cognitive-science-of-dualism` (3); `topics/consciousness-and-mathematics` (2); `concepts/inventory-blindness` (2, including the borderline "receives its most direct mechanistic support"); `concepts/introspection` (2); `topics/consciousness-in-simple-organisms`; `topics/pragmatist-quantum-foundations-and-the-agent` L135; `topics/phenomenology-of-linguistic-failure`; `topics/phenomenology-of-recursive-self-awareness`; `topics/consciousness-and-counterfactual-reasoning` (the borderline heading "as Evidence for"). Each repair reads at grade: compatible, illustrated, or "a reading and no evidence".

**Still present on pages the window touched for other reasons** (listed on 2026-11-18, not counted again here): `concepts/motor-selection` L198 "The attention-motor unification supports the [Dualism](/tenets/#dualism) tenet."; `concepts/temporal-consciousness` L190 "Its absence supports the [Dualism](/tenets/#dualism) tenet" (queued) and L148 "supporting [Bidirectional Interaction](/tenets/#bidirectional-interaction)"; `topics/emotion-and-dualism` L137 "finds its strongest empirical support in irreducibility"; `topics/phenomenology-of-anticipation` L119 "gains phenomenological support". The Cai, core-affect and beautiful-loop sweeps passed over each of these.

**Co-optation roster** (tenet sections of all 69 pages): 10 hits. All cite the author as a rival or for a narrow non-tenet point, among them Block as a physicalist at `concepts/phenomenal-overflow` L146 and `voids/plenitude-void` L118, McGinn as a rival predicting the same datum at `topics/consciousness-in-simple-organisms` L251, and Metzinger at `concepts/mine-ness` L136. No author was enlisted.

**Beautiful-loop sweep**: no page claims to refute the theory. All edited mentions route to [P-RR2](/positions/replies-to-rivals/#p-rr2), the "strongest physicalist alternative" or the "functionalist reading". `concepts/near-perfect-adaptation...` grades the exchange "a framework-boundary stalemate rather than a refutation".

## Priority List (at most four)

Rules for all four: re-grep each OLD string (`str.count == 1`) and read its whole paragraph before editing. Do not weaken a commitment the Map holds. No "This is not X. It is Y."; no "load-bearing". Do a pronoun check after each replacement. Word counts are from `tools.curate.length.analyze_length` at this run; gates fire at `>=`, and headroom is hard − 1 − count.

### 1. [topics/pragmatist-quantum-foundations-and-the-agent.md](/topics/pragmatist-quantum-foundations-and-the-agent/) L103: bring it into line with L135
3765 words of 4000 (headroom 234). No open task names this file.
- OLD: `Under dualism, "primitive and irreducible" is not a concession but a prediction: any physics that requires conscious agents at its foundations *should* find those agents irreducible within its own vocabulary. QBism's agent-shaped hole is exactly the shape dualism predicts.`
- NEW: `Under dualism, "primitive and irreducible" reads as expected rather than as a concession: any physics that requires conscious agents at its foundations would find those agents irreducible within its own vocabulary. A pragmatist who reads the agents non-dualistly expects the same hole, so its shape fits dualism without favouring it.`
- OLD: `so the argument here corroborates Tenet 1 rather than establishing it;`
- NEW: `so the argument here is compatible with Tenet 1 and adds no evidence for it;`

### 2. [voids/interested-party-void.md](/voids/interested-party-void/) L100: match the [P-V3](/positions/voids-as-evidence/#p-v3) sentence two lines above
2098 words of 3000 (headroom 901). Open task at todo L6145 (P3, Kunda / terror management / Bacon) owns other sentences on this page. Fold this edit into that task's run or do it separately; the sentences do not overlap.
- OLD: `The [[tenets#^occams-limits|fifth tenet]]---Occam's Razor Has Limits---gains additional force here: our epistemic preferences, including the preference for parsimony, may themselves be motivated rather than neutral.`
- NEW: `The [[tenets#^occams-limits|fifth tenet]]---Occam's Razor Has Limits---is illustrated here and gains no weight: our epistemic preferences, including the preference for parsimony, may themselves be motivated rather than neutral, a caution that binds the Map's judgements of simplicity as much as its critics'.`
- Optional, same paragraph group (Note 8). OLD: `If consciousness is epiphenomenal, the investigation itself becomes inexplicable` NEW: `If consciousness is epiphenomenal, the investigation faces what the Map counts as epiphenomenalism's deepest difficulty`

### 3. [concepts/interface-threshold.md](/concepts/interface-threshold/) L116: match the edited L64
2917 words of 3500 (headroom 582). Open task at todo L3379 (P3) names this file as a Secondary for L110 (a type-token link label); different sentence.
- OLD: `The cluster-not-gradient pattern fits a dualist reading better than a pure neural-complexity story, but the threshold concept does not by itself force dualism`
- NEW: `The cluster-not-gradient pattern is compatible with a dualist reading without favouring it, since a physicalist threshold predicts it too and the clustering does not by itself decide even between the threshold and gradual models ([above](#two-models-of-the-cognitive-discontinuity)); the threshold concept does not force dualism`
- The rest of the sentence (" — only that *some* architectural condition mediates the discontinuity, ...") stays as it is.

### 4. [topics/consciousness-in-smeared-quantum-states.md](/topics/consciousness-in-smeared-quantum-states/) L124: swap one verb and give the reason
3329 words of 4000 (headroom 670). Open task at todo L5538 (P3, L110 "The one proposed experiment"); different sentence. Note 9 (Koch vs Neven naming at L118 and L122) could ride along if that task's driver agrees.
- OLD: `but Albert and Loewer's core insight—that conscious experience is always definite—reinforces the Map's position.`
- NEW: `though Albert and Loewer's core insight—that conscious experience is always definite—fits the Map's position without favouring it, since their own no-collapse framework builds that definiteness in, as decoherence does within each branch.`

W5–W7 are left off the list. W7 has 2 words of headroom; W5 and W6 are single-clause hedges ("on the Map's posit"; "against epiphenomenalism") that a later deep review of either page can carry.

## Files Passing All Checks

No Warning on 62 of the 69 pages. Eleven of these carry a Note (marked †, 7 pages) or a sentence carried from 2026-11-18 (marked ‡, 4 pages).

Apex: machine-question †, mereology-of-mind, minds-without-words, open-question-ai-consciousness †, phenomenology-mechanism-bridge, research-programme-decisions-under-the-map, time-consciousness-growing-block.

Concepts: ai-consciousness-typology, attention-as-interface, consciousness †, epistemic-emotions, interface-friction, introspection, inventory-blindness, metaphysics-of-information-under-dualism, mine-ness, motor-selection ‡, near-perfect-adaptation-and-control-theoretic-competency-without-experience, phenomenal-acquaintance, phenomenal-overflow, quantum-biology-and-neural-mechanisms, quantum-consciousness, temporal-consciousness ‡, training-contamination-confound, types-of-consciousness, zombie-master-argument †.

Topics: ai-consciousness, bandwidth-of-consciousness, brain-organoids-and-the-organoid-intelligence-question, cognitive-science-of-dualism, consciousness-and-counterfactual-reasoning †, consciousness-and-mathematics, consciousness-defeats-explanation, consciousness-in-simple-organisms, eliminative-materialism, emotion-and-dualism ‡, ethics-of-possible-ai-consciousness, machine-consciousness, many-minds-interpretation, non-temporal-consciousness, pain-consciousness-and-causal-power †, phenomenology-of-anticipation ‡, phenomenology-of-forgetting †, phenomenology-of-linguistic-failure, phenomenology-of-recursive-self-awareness, purpose-and-alignment, qm-interpretations-beyond-many-worlds, quantum-randomness-channel-llm-consciousness, quantum-state-inheritance-in-ai, structural-varieties-of-consciousness-and-ai-phenomenology, the-steelman-for-value-blind-selection, time-bias-and-thank-goodness-thats-over, william-james-consciousness.

Voids: cross-state-void, emergence-void, imagery-void, learning-void, numbing-void, observation-and-measurement-void, phenomenal-quality-void, plenitude-void, voids.

Models of the grade worth copying: `voids/learning-void` L85 ("None of the Map's [tenets](/tenets/) is supported by the learning void."); `voids/plenitude-void` L118 and L120 (Block as "compatible with dualism without favouring it"; on Tenet 3, "The Map accepts the first horn" of the traces-or-idle dilemma, with the non-report routes named); `topics/time-bias-and-thank-goodness-thats-over` L95 ("a datum its rivals must explain, without being evidence that decides between them"); `topics/the-steelman-for-value-blind-selection` L107.

## Not Done

- Positions: no page under `obsidian/positions/` was edited in the window, so none was checked.
- Whole-section reads only for the tenet sections of the 19 heaviest rewrites; other pages were read at changed paragraphs plus pattern hits.
- No article, position or todo entry edited. No tasks minted (no Errors). No commit.