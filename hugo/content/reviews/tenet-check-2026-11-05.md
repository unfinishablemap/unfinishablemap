---
ai_contribution: 100
ai_generated_date: 2026-11-05
ai_modified: 2026-11-05 13:51:09+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-11-05
date: &id001 2026-11-05
description: 'Tenet check 161, a delta check of 69 changed pages: no Errors, no over-correction,
  no AI-verdict drift. 10 Warnings, led by Tenet 2 read as channel width and stale
  luck, Zeno and MWI-physics lines on window-touched pages.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-11-05 13:51:09+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-11-05
topics: []
---

# Tenet Alignment Check

**Date**: 2026-11-05. This is check 161. The previous one, [reviews/tenet-check-2026-11-03.md](/reviews/tenet-check-2026-11-03/), was check 160. Its Warnings W1–W16 and Notes 1–14 are not raised again here, except where a window edit changed their standing.

**Files checked**: 69. These are every file in `topics/` (28), `concepts/` (26), `voids/` (6), `apex/` (5), `tenets/` (2), `positions/` (1) and `arguments/` (1) changed since check 160's scan HEAD, `731098aa86` (2026-11-03 18:12Z).
- **Window.** 187 commits ran from `10cc16501f` (11-03 18:46Z) to `23a78f886c` (11-05 13:21Z), which is HEAD. 64 of them touched content. The only uncommitted change is `workflow/evolution-state.yaml`, and no content file is dirty. No file is new.
- **How the pages were read.** Every changed body span was read against the text it replaced, using a word-level diff of the frontmatter-stripped bodies. That came to about 7,130 added words. The heaviest pages were `mechanism-costs-dualism-thickness-quadrants` (730), `medium-status-voids-in-cognition` (580), `phenomenology-of-agency-vs-passivity` (552) and `weak-measurement-and-post-selection` (456).
- **Relation sections.** All 69 were read in full, not only their lens hits. The lens sweep covered support verbs, "predicts/expected", "genuine causal", parsimony, many-worlds and branch wording, AI-verdict vocabulary, collapse wording and Born/conservation wording.
- **Ledes.** The first three body paragraphs of every page were swept for strong evidential verbs, and every hit was read.
- **No subagents.** The driver read everything. Every quote below was confirmed by `grep -c -F` = 1 at the line given, with one exception, marked where it occurs.
- **Prior reviews honoured.** These were every check since 09-02 that flagged a window page, and the stability notes of today's refines. Where a finding was already flagged and never tasked, it is listed under "Carried" and not counted as new.
- **Pricing.** Word deltas come from `tools.curate.length.count_words` on the frontmatter-stripped body after each replacement, applied in order. Headroom is hard − 1 − count, and the gate is `>=`.

**Errors**: 0

**Warnings**: 10. All ten sit on unchanged lines of window-touched pages. Six (W1–W6) contradict a sibling page or the tenets text, usually one edited in this window. Two (W7, W8) now contradict the same page's own window edit. Two (W9, W10) contradict an unchanged line on the same page. No page contradicts a tenet outright.

**Notes**: 14 (five of them carried from earlier checks and re-observed live).

**Tasks minted**: 0. The skill is reports-only and does not instruct minting. The Priority List below carries four items and three fold-ins for open tasks, each with OLD/NEW text checked by script.

## Summary

**The day's fixes held where they landed, with no over-correction.** Each window concession keeps the tenet as a commitment and inherits its debt rather than conceding epiphenomenalism. Models:
- `apex/medium-status-voids-in-cognition` L172: "The cluster fits the tenet without establishing it."
- `apex/process-and-consciousness` L175: "the Map's causal claim fits that picture without following from it".
- `concepts/epistemic-emotions` L135: "Epistemic emotions fit the … Bidirectional Interaction tenet without establishing it."
- `topics/empirical-evidence-for-consciousness-selecting` L134: epiphenomenalism is "Strained (byproduct and co-optimization replies remain)" rather than "Fails".
- `voids/confabulation-void` L105: "So the middle case is not a signature only a non-physical witness could leave."
- `topics/open-individualism-and-the-de-combination-problem` L107: "Open individualism is therefore a rival the Map rejects". The 07:44Z/07:58Z refines weakened the avoidance claim without giving up the rejection.

The eleven fixes the brief listed were all confirmed live and are not re-flagged. They were on `apex/taxonomy-of-voids`, `perceptual-failure-and-the-interface`, `open-individualism`, `apex/process-and-consciousness`, `psychophysical-indexing-law`, `tenets.md` with its six siblings, `machine-consciousness`, `substrate-independence` L126, `tenets/background-commitments`, [P-CS7](/positions/consciousness-scope/#p-cs7) and `cognitive-science-of-dualism` L103.

**The main finding is Tenet 2 read as a bandwidth.** `topics/dualism-channel-width-axis` L135 says "the narrowness of the interface is what MQI is about" (W1). Tenets L69 fixes Tenet 2's minimality as "*empirical-constraint* minimality". Three pages say the opposite of L135 outright:
- `topics/memory-channel-interface-evidence` L146: "its minimality bounds detectability, not channel width".
- `topics/responsibility-gradient-from-attentional-capacity` L158, a window page: minimality "is satisfied by the channel's Born-exactness … not by its narrowness".
- Today's semantic-ratification dilemma on `concepts/psychophysical-indexing-law` L99: "the law's nomological, semantic and coordination complexity is a separate cost".

This is the family check 160 W10 found on `interface-friction` L114. Neither instance is tasked.

**Second, stale framings on pages the window touched.** Each of these lines now contradicts a sibling hub or the page's own window edit:
- **Luck framing.** `self-stultification` L147 holds that on a common-cause structure the tracking "is lawful rather than coincidental". Against it:
  - `substrate-independence` L188 says AI reports "would be accidentally accurate at best" (W2);
  - `temporal-structure-of-understanding` L182 says "a perfect parallel that does no work would be a remarkable accident" (W3).
- **AI-hardware closure stated flat.** `substrate-independence` L188 says "Computational systems are causally closed in ways brains may not be". The canonical standing (`ai-epiphenomenalism` L87) holds "conditionally on its present interface standard" (W2).
- **Zeno as the Map's reply.** `temporal-structure-of-understanding` L188 answers the decoherence objection "on the [Zeno picture](/concepts/quantum-zeno-effect/)". [P-Q4](/positions/quantum-interface/#p-q4) demotes Zeno, and tenets L77 says the timescale dispute matters only for pre-decoherence mechanisms (W3).
- **Everett physics errors.** Three lines claim Everett branching does what it does not:
  - `working-memory` L165 says "every manipulation would produce all possible outcomes in different branches". A classical computation of 5 + 3 yields 8 on every branch (W6).
  - `epistemic-emotions` L153 says the discovered truth is "not merely *a* truth in *this* branch", but a true insight is true on every branch (W4).
  - `mental-causation-and-downward-causation` L202 makes No Many Worlds "Required for mental causation to be possible", against tenets L184's "branch-relative Everettian agency being otherwise available" (W5).
- **Own-page contradiction.** `time-symmetric-physics` L176 says "Fundamental physics provides no privileged temporal direction". The page's own 11-04 L118 says denying time-symmetry "is also a live option within physics" through the collapse realism the Map relies on (W7).

**Lens (c), MWI "nothing to select": three lines pass on reading.** These lines are scoped to the Map's outcome-selection mechanism, for which they are true by definition. They make no claim about agency, so they do not need Posit Three:
- `mind-matter-interface` L174, "If all outcomes occur (MWI), selection is illusory.";
- `consciousness-selecting-neural-patterns` L152, "Selection requires collapse to be real.";
- `empirical-evidence-for-consciousness-selecting` L169, "if all outcomes occur, there is nothing to select".

Only `mental-causation` L202 extends the claim to mental causation as such (W5). The calibrated agency form is at `agent-teleology` L126 ("What branching denies is that the unchosen alternative was genuinely rejected rather than routed to a counterpart.") and `phenomenology-of-agency-vs-passivity` L171 ("branching reproduces the contrast rather than contradicting it").

**AI calibration: no drift.**
- `language-recursion-and-consciousness` L120 now opens: "The Map's [register](/positions/ai-consciousness-scope/) puts LLM consciousness at low probability, not ruled out."
- Its L201 gloss moved from "holds current AI systems lack consciousness" to "doubts current AI systems are conscious".
- Nothing says silicon could host an interface.
- The one flat hardware line, `substrate-independence` L188, is W2.

**Collapse ordering: clean.** `background-commitments` L60 now books the collapse-priority debt ("no combined law has been supplied"). `post-decoherence-selection` L116 matches it.

**Check 160 Priority List: none landed.** All four tasks are pending: motor-selection (todo L4041), von-neumann-wigner L112 (L4051), decoherence-and-macroscopic-superposition L138 (L4061) and pain-consciousness L170/L174 (L4071). The W5 fold-in rides the ai-epiphenomenalism P3 at L3406. VNW changed in the window at L56–L126, but L112 still reads "Stapp's quantum Zeno mechanism that specifies *how* consciousness acts".
- Check: L4051's guard says to keep "interface locality that resolves the multi-observer problem". This window's L60 says "Interface locality cannot do this work" for nested Wigner's-friend cases. That could look like a contradiction, but it is not one: `multi-agent-born-preservation-problem` L56 holds that interface locality "resolves" the generic whose-consciousness question, and L64 books only the nested case as residue. The guard stands.

## Method: families, violations and on-page controls

| Lens | Violations in window | Controls |
|---|---|---|
| (a) over-correction | 0 | medium-status L172, process L175, epistemic-emotions L135, empirical-evidence L134, confabulation L105, open-individualism L107 |
| (b) datum or fit read as evidence | W8, W9, W10; Notes 3, 7, 8 | resistance L39/L117, phenomenology-of-agency L167, cetacean L144/L148, reconsolidation L87, synthetic-minimal L78 |
| (c) Tenet 4 off experience, or wrong physics | W4, W5, W6; Note 2 | william-james L190, quantum-holism L182, agency-vs-passivity L171, agent-teleology L126, weak-measurement L136 |
| (d) Tenet 5 | W7 (L170), W8 (L121); Note 9 | medium-status L176, synthetic-minimal L82, boredom L96, acquaintance L120, forward-vs L105 |
| (e) co-optation / concept provenance | 0 | medium-status L112/L118/L120 (each author's stance stated), competency L95 and cognitive-immune L55 (Levin's inference reported and declined), process L163 |
| (f) collapse ordering | 0 | background-commitments L60, post-decoherence L116, VNW L102 |
| (g) mechanism ranking, Born and bandwidth wording | W1, W3 (L188), W10; Note 1 | responsibility-gradient L158, type-token L138, causal-exclusion L88, radical-pair L84 |
| (h) AI calibration | W2 (L188) | language-recursion L120/L201, substrate-independence L192, machine-consciousness L229 |

The keyword counts are lexical upper bounds. The violations column holds only what survived reading in context.

## Errors

None.

## Warnings

### Priority List items (1–4)

**W1. `topics/dualism-channel-width-axis` L135, L137: Tenet 2's minimality read as a channel-width commitment**
- **Tenet**: 2 (tenets L69: "Tenet 2's minimality is *empirical-constraint* minimality, fixed by the Rules-out clause").
- **Quotes** (each once):
  - L135: "the narrowness of the interface is what MQI is about".
  - L135: "In channel-width terms, MQI says: locate the Map at or near the floor of this axis".
  - L137: "a narrow channel firmly (MQI)".
- **Issue**:
  - The Rules-out clause bounds detectability: no detectable energy injection, Born deviation or conservation violation. A Born-exact channel satisfies it at any width.
  - Siblings state the opposite of L135:
    - `memory-channel-interface-evidence` L146: "its minimality bounds detectability, not channel width";
    - `responsibility-gradient-from-attentional-capacity` L158 (window page): "is satisfied by the channel's Born-exactness";
    - `psychophysical-indexing-law` L99 (today): "the law's nomological, semantic and coordination complexity is a separate cost".
  - The page's own L139 already calls the mapping "a structural restatement of a tenet". The fix keeps the Map's choice of the narrow end and drops the claim that the tenet requires it.
  - `concepts/interface-friction` L114 ("The interface is narrow precisely because the tenet demands minimal intervention.", check 160 W10) is the same family. It can ride this item with ample headroom (2,569/3,500).
- **Rung**: n/a (tenet-definition drift). **Priority 1.** 3,996/4,000, headroom 3. Net +1.

**W2. `concepts/substrate-independence` L188, L190: hardware closure stated flat, the luck framing, and neural quantum exploitation asserted**
- **Tenets**: 2, 3; [P-Q8](/positions/quantum-interface/#p-q8); [P-AC1](/positions/ai-consciousness-scope/#p-ac1) calibration.
- **Quotes** (each once):
  - L188: "Computational systems are causally closed in ways brains may not be."
  - L188: "would be accidentally accurate at best".
  - L190: "biological systems have evolved to exploit quantum effects where engineered systems suppress them".
- **Issue**:
  - `ai-epiphenomenalism` L87 gives the standing: "For current AI hardware the Map answers no, conditionally on its present interface standard". L188 drops the condition.
  - `self-stultification` L147 grants the epiphenomenalist a common cause on which the tracking "is lawful rather than coincidental". "Accidentally accurate" is the retired luck framing.
  - [P-Q8](/positions/quantum-interface/#p-q8) (`positions/quantum-interface` L131) is headed "a precedent for the interface, not a licence for it". Neural quantum exploitation is unestablished.
  - Today's 12:24Z refine fixed L126 on this page but did not reach L188/L190.
- **Guards**: do not touch L126, L128 or L130 (Tenet 3 quantifier NEEDS-HUMAN, todo L673, 12:24Z addendum). Nothing may say silicon could host an interface.
- **Rung**: n/a (calibration drift). **Priority 2.** 3,610/3,500, already over the hard limit. Net −4.

**W3. `concepts/temporal-structure-of-understanding` L178, L182, L188: the coincidence objection, Zeno as "the Map's reply", and a Dualism paragraph resting on guidance**
- **Tenets**: 1, 2, 3; [P-Q4](/positions/quantum-interface/#p-q4).
- **Quotes** (each once):
  - L182: "a perfect parallel that does no work would be a remarkable accident".
  - L188: "The Map's reply is that this compares the wrong quantities: on the [Zeno picture](/concepts/quantum-zeno-effect/)".
  - L178: "Understanding's temporal phenomenology supports this".
  - L178: "But phenomenal guidance of cognitive behavior suggests otherwise."
- **Issue**:
  - L182 restates the coincidence objection that `self-stultification` L147 answers with a common cause.
  - L188 makes the demoted Zeno picture the Map's reply. Tenets L77 says the timescale dispute matters only for pre-decoherence mechanisms: "Post-decoherence-selection proposals do not depend on it". The per-event-summation reply works equally under post-decoherence selection.
  - L178 rests Tenet 1 on Tenet 3's guidance claim. The matrix records interactionism as not invoked for bare-phenomenality arguments.
- **Rung**: compatible (L178); n/a (L182, L188). **Priority 3.** 3,893/3,500, over the hard limit. Net −3.

**W4. `concepts/epistemic-emotions` L151, L153: Tenet 4 read off the feel of insight, with a truth/branch confusion**
- **Tenet**: 4 (tenets L117; matrix, lens c).
- **Quotes** (each once):
  - L151: "you don't experience accessing one among infinitely many equally real knowledge-states".
  - L153: "the discovered truth is *the* truth, not merely *a* truth in *this* branch".
  - L153: "The tenet claims MWI makes such indexical facts unintelligible."
- **Issue**:
  - An Everettian predicts the same felt determination on every branch. `william-james-consciousness` L190 says so: "a stream would appear singular from inside any branch". So does `quantum-holism-and-phenomenal-unity` L182.
  - What an insight discovers, if true, is true on every branch where it occurs, so truth is not branch-relative.
  - Tenets L117 calls the indexical objection "decisive against branch-egalitarian readings" and not beyond. "Unintelligible" outruns that.
  - The 11-04 19:10Z refine fixed L135 only. The open P3 at todo L4451 owns the frontmatter description and has no textual overlap.
- **Rung**: n/a (argument error). **Priority 4.** 2,606/3,500. Net −17.

### Fold-ins for open tasks

**W5. `concepts/mental-causation-and-downward-causation` L202, L198: No Many Worlds made a precondition of mental causation; self-stultification not narrowed**
- **Tenets**: 3, 4 (tenets L184; `^tenet-3-epiphenomenalism` L101).
- **Quotes** (each once):
  - L202: "Required for mental causation to be possible."
  - L198: "and we lose epistemic access to our own minds".
- **Issue**:
  - Tenets L184 says "branch-relative Everettian agency being otherwise available". Today's `mechanism-costs-dualism-thickness-quadrants` L130 records that the taxonomy "grants that an Everettian dualist would be locatable".
  - L198 states the self-stultification consequence without the condition tenets L101 attaches ("Whether the self-stultification objection then bites depends on whether knowledge of one's experience requires *causal traffic*").
  - The 11-04 23:16Z refine (`535ae9e2d5`) changed L81–L85, L111–L115, L200 and the Further Reading glosses on this page, and left L198/L202.
- **Fold-in** to the open P3 at todo L4398 (same file, L111/L222). 3,568/3,500, over the hard limit. Net −4.

**W6. `concepts/working-memory` L165, L167: an Everett physics error and "following where the evidence leads"**
- **Tenets**: 4, 5.
- **Quotes** (each once):
  - L165: "In Many-Worlds, every manipulation would produce all possible outcomes in different branches".
  - L167: "it's following where the evidence leads".
- **Issue**:
  - A classical computation of 5 + 3 does not branch into different answers. The same paragraph also uses the banned "is not of … —it is of" construction.
  - On L167: `language-recursion-and-consciousness` L53 (window) calls the 2026 multisite result "adverse, or at best mixed, evidence" for any categorical claim that WM operation requires conscious access, and calls the manipulation asymmetry "the dominant reading, not a settled one".
  - This is the W4 family from check 160 (pain L174), on a page the window touched (L51–L202, Baddeley).
- **Fold-in** to the open P2 at todo L4544 (same file, L127). 3,746/3,500, over the hard limit. Net −42 (which also helps that P2's budget).

**W7. `concepts/time-symmetric-physics` L176, L170: own-page contradiction, and an unscaled minimality ranking**
- **Tenets**: 2, 5.
- **Quotes** (each once):
  - L176: "Fundamental physics provides no privileged temporal direction".
  - L170: "Time-symmetric selection is maximally minimal."
- **Issue**:
  - The 11-04 14:08Z refine made L118 say that denying time-symmetry at the quantum-ontology level "is also a live option within physics: collapse realism, on which the Map's modified growing block (below) relies". L176 now contradicts it.
  - On L170: the sibling `forward-in-time-vs-time-symmetric-selection` L44 (window) says "With no scale, zero point or aggregation rule" the ledger "records which items each route is charged, never how heavy any is".
- **Fold-in** to the open P3 at todo L4215 (same file; it owns L103, L110, L126 and L172, not L170 or L176). 2,363/3,500. Net +26.

### Untasked, on window-touched pages

**W8. `topics/phenomenology-of-resistance-across-domains` L115, L121: "exactly what we should expect", and parsimony claimed for the Map**
- **Tenets**: 1, 5.
- **Quotes** (each once):
  - L115: "is more naturally explained on a dualist ontology than on a strict materialism".
  - L115: "a common resistance signature across these domains is exactly what we should expect".
  - L121: "treating them as six unrelated coincidences is less parsimonious than positing a common structure".
- **Issue**:
  - The page's own 11-04 L39 grants that "dual-process and predictive accounts predict felt effort too". A single control architecture meeting varied constraints predicts a common signature as well. No discriminator is named.
  - L121 is the Map-favouring parsimony form recorded against the NEEDS-HUMAN at todo L97.
  - The 11-04 22:29Z refine fixed L39 and L117 only.
- **Rung**: compatible. 3,234/4,000, ample headroom. Next in line.

**W9. `topics/cognitive-science-of-dualism` L40, L140, L142, L148: first-person report method read as support**
- **Tenets**: 1, 3, 5.
- **Quotes** (each once):
  - L140: "actually supports the tenet".
  - L142: "finds indirect support in cognitive science's methodological dependence on first-person report".
  - L142: "The field's own practice presupposes that conscious experience causally contributes to verbal and behavioural outputs."
  - L148: "receives perhaps the strongest support from this analysis".
  - Lede L40: "the irreducibility of first-person report".
- **Issue**:
  - Heterophenomenology and every physicalist methodology use report as data without granting irreducibility. The field presupposes that *access* causes report, which the physicalist grants.
  - The page's own L146 declines the parallel move for Tenet 4: "an assumption shared by two rival intuitions is exactly the kind of thing evolved cognition would install".
  - Today's 13:12Z refine was scoped to L103 (Laukkonen).
- **Rung**: compatible. 3,813/4,000, headroom 186.

**W10. `topics/testing-consciousness-collapse` L232: Tier 2 said to test Tenet 3 "directly"**
- **Tenets**: 2, 3; [P-Q2](/positions/quantum-interface/#p-q2).
- **Quotes**:
  - L232 (once): "Tier 2 tests this directly."
  - L232 (once): "that no purely physical mechanism would produce".
  - L228: "a branch the Map registers as a live fall-back but does not endorse". This phrase occurs twice, at L121 and L228.
  - L230 (once): "register carries no differential prediction".
- **Issue**:
  - The page's own L228/L230 say the Φ-threshold tests probe a minimum-outside-corridor branch. On the corridor reading the Map endorses, the unconditioned aggregate "carries no differential prediction". A Tier 2 null would therefore not test Tenet 3 on the Map's reading.
  - Φ and Q-shapes are structural quantities, so a Φ-keyed collapse law is itself a candidate physical mechanism.
  - The window touched L135, L153, L161 and L175.
- **Rung**: n/a (scope drift). 3,997/4,000, headroom 2. A fix must be length-neutral.

### Carried and re-observed (not counted)

- `topics/forward-in-time-vs-time-symmetric-selection` L115: "and each does so without collapsing into epiphenomenalism" (once). This is check 159 W19 ([reviews/tenet-check-2026-11-02.md](/reviews/tenet-check-2026-11-02/)), never tasked. The page was refined twice in this window (11-04 12:48Z and 12:59Z, which together rewrote the L44–L113 ledger) and neither pass reached L115. Check 159's fix still applies: "though whether a Born-preserving selection escapes epiphenomenalism stays open on both ([P-Q3](/positions/quantum-interface/#mechanism-debt))" (+6; 3,406/4,000).

## Notes

1. `topics/mechanism-costs-dualism-thickness-quadrants` L154: "pushes that cost toward Q1's narrow probabilistic channel". This is a milder sibling of W1. `four-quadrant-dualism-taxonomy` L149 frames the same push as physical-side thinness ("physics is complete except at probabilistic indeterminacies"), which does follow from the empirical constraint.
2. `voids/biological-cognitive-closure` L143: "under many-worlds, all developmental trajectories are realised". Only quantum-sensitive divergences branch. This is the W6 family, at Note grade because the line is a coherence remark.
3. `apex/taxonomy-of-voids` L235: the self-knowledge cluster "is what a hidden, unverifiable causal interface would produce". [P-V1](/positions/voids-as-evidence/#p-v1) names illusionism as predicting the introspection-architecture cluster outright. This line sits two paragraphs below today's L231/L233 fix.
4. `topics/machine-consciousness` L223: epiphenomenalism is said to render consciousness "evolutionarily inexplicable". The co-optimization reply stands, and sibling Relation sections (`epistemic-emotions` L135, `resistance` L117) now say the Map "counts that reply's costs without claiming to refute it". The line sits beside today's L229 fix.
5. `concepts/agent-causation` L176: "substances *act*; that's what makes them substances". This slides from having causal powers to having powers over the physical. An epiphenomenal mental substance could still act mentally.
6. `concepts/decoherence` L199 lists magnetoreception as a quantum-biology discovery that "shows that nature's strategies are more resourceful than our assumptions predicted". Today's `radical-pair-magnetoreception` L28 grades it "the leading, behaviourally supported but still-unsettled candidate". Enzyme tunnelling alone carries the sentence.
7. `concepts/intentionality` L237: phenomenal intentionality "actually explains content determinacy where naturalistic alternatives fail". That is a contested claim stated flat.
8. `concepts/radical-pair-magnetoreception` L86: "RPM is the standard refutation of the false parsimony" sits against the same page's new L28 grade. The paragraph's own closing caution partly calibrates it.
9. `topics/four-quadrant-dualism-taxonomy` L153 still reads the parsimony argument as "parsimonious given what we are committed to". Today's `mechanism-costs` L156 withdrew the "least mechanism cost" verdict. Recorded against the NEEDS-HUMAN at todo L97.
10. Carried from check 138: `apex/competency-without-felt-experience` L129, "That supports the positive claim". Its L133 ("indeed it is what dualism leads one to expect") is self-calibrated in the same sentence.
11. Carried from check 149 (Note 5): `apex/identity-across-transformations` L193, "Your consciousness has made choices that shaped physical outcomes." This is stated flat against tenets L95.
12. Carried from check 138: `topics/amplification-mechanisms-consciousness-physics` L181, where the epiphenomenalist hypothesis "fails the evidence the Map marshals".
13. Carried from checks 09-25 and 09-27: `topics/quantum-holism-and-phenomenal-unity` L176, "supports dualism". Its own L182 is a model control.
14. `concepts/mind-matter-interface` L170: the corridor "makes 'minimal' precise: consciousness cannot alter ensemble statistics". This reads [P-Q2](/positions/quantum-interface/#p-q2)'s default as definitional. It is recorded against the P1 HUMAN DECISION on [P-Q2](/positions/quantum-interface/#p-q2)'s quantifier (todo L1626) and not adjudicated here.

## Already tasked (cited, not re-flagged)

- Check 160's four Priority items: todo L4041 (motor-selection), L4051 (VNW L112), L4061 (decoherence-macro L138), L4071 (pain L170/L174). All pending. The W5 fold-in rides L3406.
- `apex/process-and-consciousness`:
  - L115/L123 and the "all five" framing: P3 at todo L4737;
  - L129/L135/L177 (Tenet 4): P3 at L3251;
  - L179: the NEEDS-HUMAN at L97.
- `concepts/time-symmetric-physics` L103/L110/L126/L172: P3 at L4215. W7 is offered as a fold-in.
- `concepts/working-memory` L127: P2 at L4544. W6 is offered as a fold-in.
- `concepts/mental-causation-and-downward-causation` L111/L222: P3 at L4398. W5 is offered as a fold-in.
- `concepts/consciousness-selecting-neural-patterns` L88: P3 at L4237.
- `concepts/epistemic-emotions` description: P3 at L4451.
- `concepts/selection-only-channel` L123 (the semantic-ratification follow-up): P3 at L4749. It coordinates with W1 and has no shared file.
- `topics/phenomenology-of-anticipation` L143/L145/L157: P3 at L4275.
- `voids/observer-selection-void` L79/L91: P3 at L4849.
- `voids/boredom-void`: P3s at L4090 and L4101 (L98's "would go unexplained").
- `topics/clinical-neuroplasticity-evidence-for-bidirectional-causation` L38/L104: P3 at L4606.
- `topics/cetacean-and-corvid-consciousness` L39/L75: P3 at L4316.
- `topics/language-recursion-and-consciousness` L102: P3 at L4442.
- `topics/reconsolidation-as-selection-window` L79: P3 at L4175.
- `apex/apex-articles` taxonomy entry: P3 at L4597.
- Today's sibling follow-ups named in the brief:
  - Tegmark/Hagan "two poles": L4793;
  - Craddock on five pages: L4815;
  - Szangolies: L4761, L4771, L4782;
  - Stapp "preventing decoherence": L4643;
  - tenet-independence residue: L4804;
  - Goyal/Yuan: L4621, L4632;
  - cosmopsychism and panpsychism de-combination residue: L4667, L4680;
  - motor-clock comparison: L4827;
  - Sjöberg caveat: L4838.

## Standing human decisions (cited, not adjudicated)

- **Tenet 3's quantifier**: NEEDS-HUMAN (foundations) at todo L673. Consumers in the window are `substrate-independence` L126/L128/L130 (12:24Z addendum) and `responsibility-gradient-from-attentional-capacity` L156 (10-05 addendum). W2 is scoped to avoid them.
- **[P-Q2](/positions/quantum-interface/#p-q2)'s Born-preservation quantifier**: P1 HUMAN DECISION at todo L1626. Note 14 is recorded against it.
- **The homepage dualism gloss**: NEEDS-HUMAN at todo L4513.
- **The dissociation-as-evidence retitle**: NEEDS-HUMAN at todo L4503.
- **The parsimony tiebreaker and its Map-favouring counterpart**: NEEDS-HUMAN (doctrine) at todo L97. W8 (L121), Note 9 and process L179 are recorded against it.

## Files Passing All Checks

These are window pages whose changed spans, lede and Relation section raised nothing beyond the controls cited above, or whose only residue is already tasked.

- **apex**: `medium-status-voids-in-cognition`.
- **concepts**: `agent-teleology`, `bidirectional-interaction`, `causal-exclusion-argument`, `census-change-points`, `consciousness-selecting-neural-patterns` (L88 tasked), `content-externalism`, `global-workspace-theory`, `post-decoherence-selection`, `pragmatism`, `psychophysical-indexing-law`, `thought-insertion`, `type-token-causation`, `von-neumann-wigner-interpretation` (L112 tasked), `weak-measurement-and-post-selection`, `where-the-substance-commitment-enters`.
- **positions**: `consciousness-scope`.
- **tenets**: `tenets`, `background-commitments`.
- **topics**: `acquaintance-without-causation`, `cetacean-and-corvid-consciousness` (tasked), `clinical-neuroplasticity-evidence-for-bidirectional-causation` (tasked), `clinical-phenomenology-and-altered-experience`, `consciousness-and-the-authority-of-formal-systems`, `empirical-evidence-for-consciousness-selecting`, `language-recursion-and-consciousness` (L102 tasked), `open-individualism-and-the-de-combination-problem`, `perceptual-failure-and-the-interface`, `phenomenology-of-agency-vs-passivity`, `phenomenology-of-anticipation` (tasked), `quantum-biology-and-neural-consciousness` (tasked), `reconsolidation-as-selection-window` (L79 tasked), `responsibility-gradient-from-attentional-capacity`, `synthetic-minimal-agents-and-the-engineered-decoupling`, `the-cognitive-immune-system-and-immunological-selfhood`, `the-naturalisation-failure-for-content`, `william-james-consciousness`.
- **voids**: `boredom-void` (tasked), `confabulation-void`, `intrinsic-nature-void`, `observer-selection-void` (tasked), `voids`.
- **arguments**: `arguments`.

## Priority List

Every OLD string below was confirmed by script to occur exactly once, at the line given. Deltas are `count_words` on the frontmatter-stripped body after the replacement, applied in order. Standing guards for every item:
- never concede epiphenomenalism;
- each tenet stays a commitment;
- [P-AC1](/positions/ai-consciousness-scope/#p-ac1) does not move;
- no "This is not X. It is Y.", no "load-bearing";
- set `ai_modified` from `date -u`;
- append the running model to `ai_system` only if it is absent anywhere in the string.

1. **`topics/dualism-channel-width-axis` L135, L137 (W1). Tenet 2.**
   - **Length**: 3,996/4,000, headroom 3. Net +1 → 3,997.
   - (a) L135
     - OLD: `a commitment about *channel width* specifically — the narrowness of the interface is what MQI is about.`
     - NEW: `most at home at the narrow end, though its minimality bounds detectability rather than width.`
     - Delta: −2.
   - (b) L135
     - OLD: `In channel-width terms, MQI says: locate the Map at or near the floor of this axis`
     - NEW: `In channel-width terms, the Map locates itself at or near the floor of this axis`
     - Delta: −1.
   - (c) L137
     - OLD: `a narrow channel firmly (MQI), a thin mind-pole only loosely`
     - NEW: `a narrow channel firmly (permitted, not required, by MQI), a thin mind-pole only loosely`
     - Delta: +4.
   - **Guards**:
     - Re-read tenets L69, `memory-channel-interface-evidence` L146 and `responsibility-gradient` L158 first. The NEW wording follows them.
     - Keep L139's three cautions and the selection-only quotation in L135.
     - Do not edit `concepts/selection-only-channel` here. The open P3 at todo L4749 owns it.
     - Optional rider: `concepts/interface-friction` L114 ("The interface is narrow precisely because the tenet demands minimal intervention.") with the same correction (2,569/3,500).
2. **`concepts/substrate-independence` L188, L190 (W2). Tenets 2, 3; [P-Q8](/positions/quantum-interface/#p-q8).**
   - **Length**: 3,610/3,500, over the hard limit. Net −4 → 3,606.
   - (a) L188
     - OLD: `Computational systems are causally closed in ways brains may not be.`
     - NEW: `On the Map's present interface standard, computation is causally closed in ways brains may not be.`
     - Delta: +5.
   - (b) L188
     - OLD: `The self-stultification problem applies: if our discussions of consciousness are caused by consciousness, and AI outputs are not caused by any conscious experience, then AI reports of consciousness would be accidentally accurate at best.`
     - NEW: `If an AI had experience that caused none of its outputs, its reports could match that experience only through a common cause, which [[self-stultification|the self-stultification hub]] grants is lawful rather than lucky.`
     - Delta: −2.
   - (c) L190
     - OLD: `The [[decoherence]] challenge doesn't eliminate this distinction; it sharpens it by highlighting how biological systems have evolved to exploit quantum effects where engineered systems suppress them.`
     - NEW: `The [[decoherence]] challenge doesn't eliminate this distinction, though whether neural tissue exploits quantum effects at all is unestablished ([[positions/quantum-interface#^p-q8|P-Q8]]).`
     - Delta: −7.
   - **Guards**:
     - `^p-q8` exists at `positions/quantum-interface` L133.
     - Leave L126, L128 and L130 alone (Tenet 3 quantifier NEEDS-HUMAN, todo L673).
     - Nothing may say silicon could host an interface.
     - Re-read `ai-epiphenomenalism` L87 and `self-stultification` L147 first.
3. **`concepts/temporal-structure-of-understanding` L178, L182, L188 (W3). Tenets 1, 2, 3; [P-Q4](/positions/quantum-interface/#p-q4).**
   - **Length**: 3,893/3,500, over the hard limit. Net −3 → 3,890.
   - (a) L178
     - OLD: `Understanding's temporal phenomenology supports this:`
     - NEW: `Understanding's temporal phenomenology fits this:`
     - Delta: 0.
   - (b) L178
     - OLD: `If understanding required only neural sequence, not experienced sequence, temporal phenomenology would be epiphenomenal. But phenomenal guidance of cognitive behavior suggests otherwise.`
     - NEW: `Whether that addition does cognitive work is the Bidirectional question below.`
     - Delta: −11.
   - (c) L182
     - OLD: `the coincidence objection applies: a perfect parallel that does no work would be a remarkable accident.`
     - NEW: `the coincidence objection presses, though a common cause makes the parallel lawful rather than lucky ([[self-stultification]]).`
     - Delta: 0.
   - (d) L182 (pronoun guard)
     - OLD: `It does not touch the illusionist, who posits no phenomenal states`
     - NEW: `The objection does not touch the illusionist, who posits no phenomenal states`
     - Delta: +1.
   - (e) L188
     - OLD: `The Map's reply is that this compares the wrong quantities: on the [[quantum-zeno-effect|Zeno picture]] selection operates at each collapse event`
     - NEW: `The Map's reply is that this compares the wrong quantities: on its preferred [[post-decoherence-selection|post-decoherence selection]], as on the demoted [[quantum-zeno-effect|Zeno picture]], selection operates at each collapse event`
     - Delta: +7.
   - **Guards**:
     - Keep L182's "neither is refuted from inside the other's framework" and the illusionist and identity-theorist clauses.
     - Keep L188's closing debt ("owes an account of how per-event biases sum").
     - Do not call Zeno ruled out. Tenets L71 keeps the coherence-dependent proposals "as live fallbacks".
4. **`concepts/epistemic-emotions` L151, L153 (W4). Tenet 4.**
   - **Length**: 2,606/3,500. Net −17 → 2,589.
   - (a) L151
     - OLD: `tenet connects to epistemic emotions through the indexical structure of knowing. When doubt resolves into certainty, you don't experience accessing one among infinitely many equally real knowledge-states. The phenomenology is of *this* determination mattering.`
     - NEW: `tenet bears on epistemic emotions as coherence only. When doubt resolves into certainty the phenomenology is of *this* determination mattering, but an Everettian predicts the same felt determination on every branch.`
     - Delta: −3.
   - (b) L153
     - OLD: `The "aha" moment exemplifies this: the phenomenal character involves genuine discovery—something was unknown, now it is known, and this transition is real. In Many-Worlds, the transition occurs in some branches while alternative insights occur in others; no insight is privileged. Yet the phenomenology of insight involves precisely this privilege—the discovered truth is *the* truth, not merely *a* truth in *this* branch. The tenet claims MWI makes such indexical facts unintelligible.`
     - NEW: `The "aha" moment shows the limit. Its phenomenal character involves genuine discovery—something was unknown, now it is known—yet what an insight discovers, if true, is true on every branch where it occurs, so the feel of discovery cannot tell one world from many. The tenet rests on the indexical objection, not on the phenomenology of knowing.`
     - Delta: −14.
   - **Guards**:
     - The model is `william-james-consciousness` L190.
     - Tenet 4 stays a commitment resting on the indexical objection.
     - Coordinate with the open P3 at todo L4451 (frontmatter description only). There is no textual overlap.

**Fold-ins for open tasks (not new tasks).**
- **To the P3 at todo L4398 (`mental-causation-and-downward-causation`; W5).** 3,568/3,500, over the hard limit. Net −4.
  - (a) L198
    - OLD: `if consciousness causes nothing, our reports and beliefs about experience are causally disconnected from actual experiences, and we lose epistemic access to our own minds.`
    - NEW: `if consciousness causes nothing, reports about experience are causally disconnected from it, costing self-knowledge if knowing requires causal traffic ([[tenets#^tenet-3-epiphenomenalism|the tenet's concession]]).`
    - Delta: −3.
  - (b) L202
    - OLD: `Required for mental causation to be possible. If every outcome actualises in branching universes, there's no selection for consciousness to perform.`
    - NEW: `Required for the Map's selection mechanism, since nothing is selected if every outcome actualises; branch-relative mental causation survives ([[tenets/background-commitments|Posit Three]]).`
    - Delta: −1.
- **To the P2 at todo L4544 (`working-memory`; W6).** 3,746/3,500, over the hard limit. Net −42.
  - (a) L165
    - OLD: `In Many-Worlds, every manipulation would produce all possible outcomes in different branches; the sense that *this* manipulation produced *this* result would be branch-relative illusion. But the phenomenology of successful manipulation is not of accessing one among many equally real outcomes—it is of determining what the answer *is*. This indexical determinacy fits collapse interpretations where manipulation genuinely selects outcomes. This represents a philosophical standoff rather than decisive refutation; Many-Worlds proponents will analyse the phenomenology differently.`
    - NEW: `Many-Worlds leaves that determinacy intact, since a classical computation of 5 + 3 yields 8 on every branch, so the tenet bears on working memory as coherence only.`
    - Delta: −46.
  - (b) L167
    - OLD: `Postulating that manipulation requires consciousness isn't unnecessary complexity—it's following where the evidence leads.`
    - NEW: `That manipulation requires consciousness is the dominant reading, not a settled one, and simplicity cannot decide it.`
    - Delta: +4.
- **To the P3 at todo L4215 (`time-symmetric-physics`; W7).** 2,363/3,500. Net +26.
  - (a) L170
    - OLD: `Time-symmetric selection is maximally minimal.`
    - NEW: `Time-symmetric selection bids strongly for minimality, though the [[forward-in-time-vs-time-symmetric-selection|debt inventory]] has no scale on which to rank it against the forward route.`
    - Delta: +17.
  - (b) L176
    - OLD: `Fundamental physics provides no privileged temporal direction; adding one requires justification that physics doesn't supply.`
    - NEW: `The dynamical laws provide no privileged temporal direction, though collapse realism, on which the Map's modified growing block relies, supplies one at measurement (above).`
    - Delta: +9.

**Next in line, if capacity allows**:
1. W8 (resistance L115, ample headroom).
2. The carried check 159 W19 (forward-in-time L115, +6).
3. W9 (cognitive-science L140/L142/L148, headroom 186).
4. W10 (testing L232, length-neutral only).