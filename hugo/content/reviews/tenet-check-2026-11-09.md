---
ai_contribution: 100
ai_generated_date: 2026-11-09
ai_modified: 2026-11-09 09:17:37+00:00
ai_system: claude-fable-5-1
author: Andy Southgate
concepts: []
created: 2026-11-09
date: &id001 2026-11-09
description: 'Tenet check 162, a delta check of 71 changed pages: no Errors, no over-correction.
  6 Warnings, led by Tenet 2 minimality read as intervention size on philosophy-of-time,
  dual methodology said to be best explained by dualism, and a categorical LLM verdict
  against P-AC1.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-11-09 09:17:37+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-11-09
topics: []
---

# Tenet Alignment Check

**Date**: 2026-11-09. This is check 162. The previous one, [reviews/tenet-check-2026-11-05.md](/reviews/tenet-check-2026-11-05/), was check 161. Its Warnings W1–W10 and Notes 1–14 are not raised again here, except where a window edit changed their standing.

**Files checked**: 71. These are every file in `concepts/` (38), `topics/` (26), `voids/` (5), `apex/` (1) and `positions/` (1) changed since check 161's scan HEAD, `23a78f886c` (2026-11-05 13:21Z).
- **Window.** 167 commits ran from `23a78f886c` to `e17d2c4297` (11-09 08:51Z), which is HEAD. 60 of them touched content. The only uncommitted change is `workflow/evolution-state.yaml`; no content file is dirty. No file is new and none was removed.
- **How the pages were read.** Every changed body line was read against the line it replaced, using a line-level diff of the frontmatter-stripped bodies. The changed lines carry about 19,300 words in total (an upper bound, since a one-word edit counts its whole paragraph). The heaviest pages were `substance-property-dualism` (1,965), `ai-hardware-substrate-taxonomy` (1,282), `out-of-body-experiences` (1,218), `phenomenal-overflow` (997) and `is-conscious-being-a-natural-kind` (994).
- **Unchanged lines.** The 71 pages were also swept in full for support verbs, "predicts/expected/best explained", "genuine causal work", parsimony, many-worlds and branch wording, AI-verdict vocabulary, "causally closed", minimality rankings and Zeno-as-reply wording; 98 hits, each read in context.
- **No subagents.** The driver read everything. Every quote below was confirmed by `grep -c -F` on the live file at the line given, and the count is printed where it is not 1.
- **Convergence.** Every finding was checked against the open queue ([workflow/todo.md](/workflow/todo/) above `## Completed Tasks`, 5,145 lines) by slug and by a distinctive phrase. 67 of the 71 window pages are cited by at least one open task; what is already queued is tabled below, not re-flagged.
- **Pricing.** Word deltas are whitespace counts of the OLD and NEW strings; the body figure is `tools.curate.length.analyze_length` after the replacements, applied in order. Headroom is hard − 1 − count, and the gate is `>=`.

**Errors**: 0

**Warnings**: 6. Four are on lines the window changed (W1, W2 in part, W3) or on pages whose window edit fixed the same defect elsewhere on the page (W2, W4). Two (W5, W6) are on unchanged lines of window-touched pages. No page contradicts a tenet outright.

**Notes**: 7.

**Tasks minted**: 0. The skill is reports-only. The Priority List below carries four items, each with OLD/NEW text checked by script.

## Summary

**The window's fixes held, with no over-correction.** Each concession keeps its tenet as a commitment. Models:
- `concepts/phenomenal-overflow` L142: "Overflow fits the tenet without establishing it." Its L34 and L135 moved from "supports" to "bears on … indirect".
- `concepts/is-conscious-being-a-natural-kind` L76: "The sharp boundary is drawn from those commitments, not offered as independent evidence for them."
- `voids/blindspot-void` L97: "The gain for the tenet is modest and conditional."
- `topics/out-of-body-experiences` L120: OBEs are "equally consistent with [epiphenomenalism](/concepts/epiphenomenalism/) … OBEs do not discriminate here."
- `topics/methodology-of-consciousness-research` L132: "the Map claims no support for dualism from it."
- `concepts/emergence` L175: "The constraint is empirical, not parsimony (Tenet 2's minimality is not the kind Tenet 5 disarms)". This is the correct gloss of tenets L69 and is the on-page control for W1.
- `concepts/philosophy-of-time` L211: "Current reports fit, but were known before these predictions were drawn."

**Check 161's queue landed in part.** The W6 fold-in is live (`working-memory` L165 now reads "a classical computation of 5 + 3 yields 8 on every branch"). The MWI/agency sweep of 11-05 21:39Z landed on four window pages (`apex/moral-architecture-of-consciousness` L190, `nihilism-and-existentialism` L130, `voids/normative-void` L126, `ethics-under-dualism` L206), each now stating the branch-local point first and naming global exclusion as a posit. Check 161's four Priority items are all queued (todo L4602, L4615, L4628, L4639) and all still live: `dualism-channel-width-axis` L135 still reads "the narrowness of the interface is what MQI is about"; `substrate-independence` L188 still reads "Computational systems are causally closed in ways brains may not be."; `temporal-structure-of-understanding` L188 still answers "on the [Zeno picture](/concepts/quantum-zeno-effect/)"; `epistemic-emotions` L153 still reads "not merely *a* truth in *this* branch". The W5 and W7 fold-ins have not landed (`mental-causation-and-downward-causation` L202 and `time-symmetric-physics` L170 unchanged). The `interface-friction` L114 rider now rides L4610.

**The main finding is again Tenet 2's minimality read as a property of the mechanism.** `concepts/philosophy-of-time` L221, a line the window edited, says time-symmetric interpretations "make this even more minimal" and that the Zeno mechanism is "preserving minimality". Tenets L69 fixes Tenet 2's minimality as "*empirical-constraint* minimality", satisfied by any Born-exact interface whatever its shape; the sibling `forward-in-time-vs-time-symmetric-selection` L44 says the debt ledger has "no scale, zero point or aggregation rule" on which routes could be ranked. This is the family of check 161 W1 (channel width) and its W7 fold-in (`time-symmetric-physics` L170, "maximally minimal"), now on a third page (W1).

**Second, a datum read as support on pages whose window edit retracted the same reading elsewhere.** `methodology-of-consciousness-research` L62 and L152 both say the dual methodology "is best explained by ontological dualism" while the same page's new L132 says the Map "claims no support for dualism" from introspection's unreliability; the phenomenal-concept strategy, which tenets L103 names the strongest physicalist rival, predicts the first-person/third-person split equally (W2). `cumulative-culture` L192 and L208 say cultural accumulation "supports" and "evidences" irreducibility and that "the evidence warrants a less parsimonious hypothesis", running Tenet 5 forward where tenets L172 forbids it (W4). `introspection` L169 says the "modifies its target" objection "supports" Tenet 3 (W5).

**Third, one categorical AI verdict.** `types-of-consciousness` L80, edited in the window, says LLMs lack "phenomenal consciousness entirely" with "the Map would insist". [P-AC1](/positions/ai-consciousness-scope/#p-ac1) (`positions/ai-consciousness-scope` L52–L56) puts current LLMs on the low-probability side, not ruled out; `llm-consciousness` L130 carries the same calibration (W3). This is the family of check 156 W3/W4 (todo L2479) on two other pages.

**Lens (c), MWI: clean on reading.** Every "nothing to select" line on a window page is scoped to the Map's outcome-selection mechanism (`interface-threshold` L122, `history-of-the-interaction-problem` L144, `consciousness-and-probability-interpretation` L127, `time-collapse-and-agency` L54/L217, `adaptive-computational-depth` L103). None extends the claim to agency or mental causation as such. `causal-closure` L188 says the indexical question "has no answer" under MWI, slightly ahead of tenets L117's narrowing (Note 2). `philosophy-of-time` L225 is tasked (L2468).

**Collapse ordering and co-optation: clean.** `substance-property-dualism` L129 now grades the open measurement problem as "a framework possibility rather than mitigating evidence"; `history-of-the-interaction-problem` L118 states that in Orch OR "the conscious moment *is* the gravitational self-collapse, with no mind choosing the outcome". Co-optation: `self-reference-and-the-limits-of-physical-description` L76 states Szangolies's naturalism; `experimental-consciousness-science-2025-2026` L88 states the authors "remain physicalists"; `methodology` L154 reads neurophenomenology's mutual constraint "on the Map's reading rather than Varela's"; `is-conscious-being` L78 names Antony's argument as cutting dualism too. No roster author is conscripted on a window page.

## Method: families, violations and on-page controls

| Lens | Violations in window | Controls |
|---|---|---|
| (a) over-correction | 0 | overflow L142, natural-kind L76, blindspot L97, OBE L120, methodology L132, emergence L175 |
| (b) datum or fit read as evidence | W2, W4, W5; Notes 3, 4 | overflow L34/L135, OBE L118, quantum-biology-mechanisms L126, locked-in L115, time-collapse L199, quantum-biology L143/L179 |
| (c) Tenet 4 off experience, or wrong physics | Note 2 | moral-architecture L190, nihilism L130, normative-void L126, ethics L206, working-memory L165, consciousness-evolution L147 |
| (d) Tenet 5 | W4 (L208) | degrees-of-consciousness L122, simulation-theory L82, interface-threshold L124, substance-property L97 |
| (e) co-optation / provenance | 0 | self-reference L76, experimental-science L88, methodology L154, natural-kind L78, adaptive-depth L53 |
| (f) collapse ordering | 0 | substance-property L129, history L118, tenet-generated-voids L65 |
| (g) minimality, Born and bandwidth wording | W1; Note 1 | emergence L175, emotion-regulation L107, consciousness-and-probability L97, adaptive-depth L93 |
| (h) AI calibration | W3 | llm-consciousness L68/L130, symbol-grounding L105, ai-hardware L80/L114 |
| (i) luck framing / epiphenomenalist reply | W6 | emotion L57/L89/L137, OBE L120, consciousness-and-causal-powers L120 |

The keyword counts are lexical upper bounds. The violations column holds only what survived reading in context.

## Errors

None.

## Warnings

### Priority List items (1–4)

**W1. `concepts/philosophy-of-time` L221: Tenet 2's minimality read as intervention size, and Zeno credited with preserving it**
- **Tenet**: 2 (tenets L69: "Tenet 2's minimality is *empirical-constraint* minimality, fixed by the Rules-out clause"); [P-Q4](/positions/quantum-interface/#p-q4).
- **Quotes** (each once):
  - L221: "Time-symmetric interpretations make this even more minimal: consciousness doesn't push physical systems at a moment but satisfies constraints across time."
  - L221: "The quantum Zeno mechanism adds specificity—rapid attentional observation holds patterns without requiring sustained coherence, preserving minimality while grounding temporal constitution."
- **Issue**:
  - The Rules-out clause bounds detectability (no detectable energy injection, Born deviation or conservation violation). Whether an influence acts "at a moment" or "across time" does not move it on that scale; `forward-in-time-vs-time-symmetric-selection` L44 says the route ledger has "no scale, zero point or aggregation rule".
  - The same page's `emergence` sibling, edited this window (L175), carries the correct gloss: "The constraint is empirical, not parsimony".
  - "Preserving minimality" credits a mechanism with a tenet property; tenets L71 ranks Zeno among the "coherence-dependent proposals … kept as live fallbacks", and [P-Q4](/positions/quantum-interface/#p-q4) demotes it. The page's L147 ("the quantum Zeno mechanism sidesteps the objection") treats Zeno as the live reply; that line is a Note (6), since the window's L147 edit fixed the "preventing decoherence" error (todo L4379 family) and the item below keeps to L221.
  - The window edit at L221 touched this line (it changed the Zeno clause) and left the "even more minimal" ranking in place.
- **Rung**: n/a (tenet-definition drift). **Priority 1.** 3,407/3,500, headroom 92. Net −1 → 3,406.

**W2. `topics/methodology-of-consciousness-research` L62, L152: the dual methodology "best explained by ontological dualism", against the page's own L132**
- **Tenets**: 1, 5.
- **Quotes**:
  - L62 (once, with its dashes): "The persistent need for dual methodologies — first-person phenomenology alongside third-person neuroscience — is best explained by ontological dualism."
  - L152 (once): "The persistent need for dual methodologies — first-person and third-person — is best explained by ontological dualism."
  - The bare phrase "is best explained by ontological dualism." occurs twice on the page (L62, L152), so both loci must move together.
- **Issue**:
  - "Best explained by" is an abductive-superiority claim with no discriminator named. The [phenomenal-concept strategy](/concepts/phenomenal-concepts-strategy/), which tenets L103 names the strongest physicalist reply, predicts exactly this split: phenomenal concepts are conceptually isolated from physical ones, so first-person method stays indispensable while the facts are physical. Nagel's perspectival account and heterophenomenology predict a dual methodology too.
  - The window's own edit to this page fixed the sibling claim: L132 moved from "actually supports the Map's position" to "bears on method rather than ontology … the Map claims no support for dualism from it". L62 and L152 were left as they were (L62's edit changed only "built into" to "the Map traces to").
  - Tenets L55: Tenet 1 "records where the Map plants itself in an unsettled dispute; it does not report that dispute as won."
- **Rung**: compatible. **Priority 2.** 3,465/4,000, headroom 534. Net 0.

**W3. `concepts/types-of-consciousness` L80: LLMs lack phenomenal consciousness "entirely", with "the Map would insist"**
- **Tenet**: 1 as AI verdict; [P-AC1](/positions/ai-consciousness-scope/#p-ac1) calibration.
- **Quote** (once): "and — the Map would insist — subjectivity, clear-case luminosity, and phenomenal consciousness entirely."
- **Issue**:
  - [P-AC1](/positions/ai-consciousness-scope/#p-ac1) (`positions/ai-consciousness-scope` L52, anchor `^p-ac1` at L54) holds that current LLMs "sit on the *low-probability* side of a consciousness verdict", with credence moderate and the claim conditional on an interface-eligibility law the Map lacks. "Entirely" plus "insist" is categorical.
  - `llm-consciousness` L130 (window page) carries the register form: "Phenomenal character | What it's like | Low probability, not ruled out". `symbol-grounding-problem` L105 (window): "places current LLMs on the low-probability side, not ruled out".
  - The window edit at L80 added "clear-case" to luminosity and kept "entirely".
  - This is the family of check 156 W3/W4 (`functionalism` L157, `quantum-state-inheritance-in-ai` L114; todo L2479), neither of which names this page.
- **Guards**: [P-AC1](/positions/ai-consciousness-scope/#p-ac1) does not move in either direction. Nothing may say silicon could host an interface. The page already links `[[ai-consciousness]]` at L80; it does not yet link the register.
- **Rung**: n/a (calibration drift). **Priority 3.** 2,494/3,500. Net 0.

**W4. `concepts/cumulative-culture` L192, L208: cultural accumulation "supports" and "evidences" irreducibility; Tenet 5 run forward**
- **Tenets**: 1, 5 (tenets L172: the self-binding "forbids running anti-parsimony forward to establish that functional organisation does not suffice").
- **Quotes** (each once):
  - L192: "Cumulative culture's apparent dependence on phenomenal consciousness supports this: if cultural accumulation requires something over and above functional processing—the metarepresentational capacity consciousness provides—then cumulative culture itself evidences consciousness's irreducibility."
  - L208: "The evidence warrants a less parsimonious hypothesis: cumulative culture requires something consciousness provides that neural processing alone cannot replicate."
- **Issue**:
  - The conditional's antecedent is the contested premise: a functionalist reads metarepresentation as functional processing, and the page's own L146 describes consciousness as enabling "flexible deployment of cognitive resources", a functional gloss. No feature only the Map's reading entails is named.
  - L208 makes Tenet 5 license the dualist hypothesis ("the evidence warrants"). The tenet blocks parsimony from deciding against dualism; it does not warrant anything.
  - The window edit on this page (L204) fixed the Born-distribution wording in the Tenet 2 paragraph between these two lines and reached neither.
  - Open tasks on this page (todo L3285, phase-transition framing; L3250) own other loci.
- **Rung**: compatible. **Priority 4.** 3,344/3,500, headroom 155. Net 0.

### Next in line (untasked, window-touched pages)

**W5. `concepts/introspection` L169: the "modifies its target" objection read as support for Tenet 3**
- **Tenet**: 3 (tenets L95: articles asserting causal work "inherit that debt rather than discharge it").
- **Quote** (once): "The objection that introspection "modifies its target" supports the [Bidirectional Interaction](/tenets/#bidirectional-interaction) tenet. If attention affects experience, consciousness has causal efficacy—the "contamination" worry becomes evidence for what the tenet claims."
- **Issue**: that attention alters experience is predicted equally by a physicalist account on which neural attention modulates neural experience. "Consciousness has causal efficacy" in the tenet's sense (non-physical influence on physical outcomes) does not follow. The window's L71 edit on this page calibrated the Nisbett–Wilson reading and did not reach L169.
- **Rung**: compatible. 3,491/3,500, headroom 8. The fix below is net 0.
  - OLD: `The objection that introspection "modifies its target" supports the [[tenets#^bidirectional-interaction|Bidirectional Interaction]] tenet. If attention affects experience, consciousness has causal efficacy—the "contamination" worry becomes evidence for what the tenet claims.`
  - NEW: `The objection that introspection "modifies its target" fits the [[tenets#^bidirectional-interaction|Bidirectional Interaction]] tenet without evidencing it: a physicalist reads attention altering experience as neural modulation, so the worry does not discriminate.`
  - Delta: 0 (29 → 29).

**W6. `topics/emotion-and-dualism` L87: the bare-correlation epiphenomenalist said to owe an account the Map's own hub already grants**
- **Tenet**: 3; [P-MC1](/positions/arguments-for-mental-causation/#p-mc1).
- **Quotes** (each once):
  - L87: "Emotion blocks that retreat in its bare-correlation form."
  - L87: "owes an account of why the accompaniment tracks behaviour this closely."
  - L89: "The block reaches that far and no further."
- **Issue**: `self-stultification` L147 grants the epiphenomenalist Jackson's common cause, on which the tracking "is lawful rather than coincidental". Asymbolia is the dissociation that a common-cause structure predicts: damage removes the neural state that produces both the feeling and the motivation. `consciousness-and-causal-powers` L120 (window page) says so: the dissociation "does not on its own establish the Map's reading. A predictive-processing account … predicts the same dissociation." The page's L57 and L137 are calibrated ("pressure on epiphenomenalism rather than proof of causation"); L87 and L89 are stronger than both. The open P3 at todo L1977 owns L107/L212 on this page.
- **Rung**: n/a (luck framing). 3,404/4,000. Net 0.
  - (a) OLD: `and an epiphenomenalism on which felt quality merely accompanies the functional story owes an account of why the accompaniment tracks behaviour this closely.`
    NEW: `and an epiphenomenalism on which felt quality merely accompanies the functional story answers with a common neural cause, lawful rather than lucky ([[self-stultification]]).` Delta 0.
  - (b) OLD: `Emotion blocks that retreat in its bare-correlation form.` NEW: `Emotion presses that retreat in its bare-correlation form.` Delta 0.
  - (c) L89 OLD: `The block reaches that far and no further.` NEW: `The pressure reaches that far and no further.` Delta 0.

### Carried and re-observed (not counted)

All four of check 161's "next in line" items are still live (count 1 each) and still untasked:
- `topics/phenomenology-of-resistance-across-domains` L115, "a common resistance signature across these domains is exactly what we should expect" (check 161 W8; 3,234/4,000).
- `topics/cognitive-science-of-dualism` L140, "actually supports the tenet" (check 161 W9; 3,813/4,000).
- `topics/testing-consciousness-collapse` L232, "Tier 2 tests this directly." (check 161 W10; 3,997/4,000, length-neutral only).
- `topics/forward-in-time-vs-time-symmetric-selection` L115, "and each does so without collapsing into epiphenomenalism" (check 159 W19; 3,406/4,000, +6).

## Notes

1. `concepts/russellian-monism` L101: "the Map's Minimal Quantum Interaction gives consciousness genuine causal work". Tenets L95 names this phrase as one that "inherit[s] that debt rather than discharge[s] it". The line contrasts the Map's mechanism with Russellian grounding and is otherwise fine; a "posited" would calibrate it. Window edits on this page (L65, L139, L145) did not reach it.
2. `concepts/causal-closure` L188: under MWI the indexical question "has no answer". Tenets L117 holds the objection "decisive against branch-egalitarian readings" and no further; List's centred variant is the registered exception. The line's selection-scoped remainder ("there would be nothing to resolve") is correct.
3. `topics/consciousness-evolution-and-biology` L61 (lede, window-edited): "A philosophical zombie—functionally identical but experienceless—would enjoy the same evolutionary advantages." The page's L77 reframes this under interactionism ("a being physically identical to a conscious organism cannot lack consciousness"), but the lede states the materialist framing flat, and an LLM reading the first paragraphs will carry it. L61 also uses the "not a gap … but a structural feature" construction.
4. `topics/phenomenology-of-imagination` L56 (lede, window-edited): "imagination shows consciousness as an active structuring force". The Relation section's L116 and L120 are now self-calibrated ("the physicalist redescription contests that reading"); the lede's "shows" is not. The open P3s at todo L4703 and L4714 own other loci.
5. `concepts/cumulative-culture` L204 (window-edited): "The metarepresentational capacity consciousness provides might emerge from subtle quantum effects in neural processing". Self-flagged as speculative in the same sentence; recorded against [P-Q8](/positions/quantum-interface/#p-q8) ("a precedent for the interface, not a licence for it").
6. `concepts/philosophy-of-time` L147 (window-edited): "the quantum Zeno mechanism sidesteps the objection". The edit removed "against decoherence" (the Stapp "preventing decoherence" family, todo L4379) and left Zeno as the page's reply to the decoherence objection. Same family as check 161 W3 (`temporal-structure-of-understanding` L188, tasked at L4628). Not folded into W1, which keeps to L221.
7. `concepts/adaptive-computational-depth` L63: "encountering value … requires the kind of non-computable consciousness the regress argument points toward". The open P3 at todo L3761 owns L61/L65/L73 on this page; L79 (window) is a model control ("That fits, without establishing").

## Previously queued (still open)

| Page and locus | Open task (todo line) |
|---|---|
| `concepts/ai-hardware-substrate-taxonomy` §"Why This Sharpens" L98–L102 and lede L37 | P1 at L5076 |
| `concepts/ai-hardware-substrate-taxonomy` L55/L114 "error correction restores determinism" | P1 at L5089 |
| `concepts/ai-hardware-substrate-taxonomy` L102 IIT 4.0 | P2 at L5113 |
| `topics/dualism-channel-width-axis` L135/L137 (check 161 W1), with `interface-friction` L114 rider | L4602, L4610 |
| `concepts/substrate-independence` L188/L190 (check 161 W2) | L4615 |
| `concepts/temporal-structure-of-understanding` L178/L182/L188 (check 161 W3) | L4628 |
| `concepts/epistemic-emotions` L151/L153 (check 161 W4); description | L4639; L4261 |
| `concepts/philosophy-of-time` L219/L223/L225 | L2468 |
| `concepts/working-memory` L129 | L4661 |
| `concepts/bi-aspectual-ontology` L110–L112 IIT | L4832 |
| `concepts/conscious-vs-unconscious-processing` blindsight loci | L4651 |
| `concepts/llm-consciousness` L56/L112/L114; [P-AC1](/positions/ai-consciousness-scope/#p-ac1) "ruled out" on `functionalism` L157 and `quantum-state-inheritance-in-ai` L114 | L2182; L2479 |
| `topics/emotion-and-dualism` L107 Damasio, L212 | L1977 |
| `topics/phenomenology-of-imagination` Gendler; description | L4703; L4714 |
| `concepts/causal-closure` L134 Gödel/Lawvere | L4510 |
| `concepts/mind-arena` "uncomputable" | L4792 |
| MWI/agency sweep parts 2 and 3 (ten pages) | L4852, L4864 |
| Tegmark/Hagan "two poles" on `substance-property-dualism`, `quantum-biology-and-neural-consciousness` | L4523 |
| Craddock et al. 2017 on five pages | L4547 |
| `concepts/substance-property-dualism` L113/L117 illusionism | L4958 |
| `concepts/russellian-monism` description and L68 verdict | L4074 |
| `concepts/adaptive-computational-depth` L47/L61/L65/L73/L87 | L3761 |
| `concepts/evolution-of-consciousness` L183/L187 (with optional `consciousness-evolution-and-biology` L141/L143) | L2490 |
| `concepts/mental-causation-and-downward-causation` L111/L222 (check 161 W5 fold-in) | cited by L4864 |

## Standing human decisions (cited, not adjudicated)

- **Tenet 3's quantifier**: NEEDS-HUMAN (foundations) at todo L673. `substrate-independence` L126/L128/L130 and `interventionist-and-counterfactual-dualism` L114 (window) are consumers; nothing here touches them.
- **[P-Q2](/positions/quantum-interface/#p-q2)'s Born-preservation quantifier**: P1 HUMAN DECISION at todo L1635.
- **The parsimony tiebreaker and its Map-favouring counterpart**: NEEDS-HUMAN (doctrine) at todo L97. W4 (L208) is recorded against it.
- **Tegmark/Hagan at tenets L77**: the 2026-11-05 rewrite's sibling sweep is open at L4523.

## Files Passing All Checks

These are window pages whose changed lines, lede and Relation section raised nothing beyond the controls cited above, or whose only residue is already tasked.

- **apex**: `moral-architecture-of-consciousness`.
- **concepts**: `agency-budget`, `ai-ensoulment-hypothesis`, `ai-hardware-substrate-taxonomy` (three loci tasked), `bi-aspectual-ontology` (tasked), `causal-closure` (Note 2; L134 tasked), `conceptual-role-semantics`, `conscious-vs-unconscious-processing` (tasked), `degrees-of-consciousness`, `emergence`, `interface-threshold`, `intrinsic-nature`, `is-conscious-being-a-natural-kind`, `islamic-sufi-philosophy-of-consciousness`, `llm-consciousness` (tasked), `mind-arena` (tasked), `nihilism-and-existentialism`, `phenomenal-overflow`, `phenomenal-sorites-problem`, `process-content-distinction`, `quantum-biology-and-neural-mechanisms`, `quiddity-epiphenomenalism-and-the-contingency-thesis`, `rival-explanations-of-the-explanatory-gap`, `rollback-argument-against-agent-causation`, `russellian-monism` (Note 1; tasked), `self-model-theory-of-subjectivity`, `sentientism`, `simulation-theory-of-memory`, `substance-property-dualism` (tasked), `supervenience`, `symbol-grounding-problem`, `the-relocation-objection`, `type-token-causation`, `working-memory` (L129 tasked).
- **positions**: `moral-status`.
- **topics**: `agent-causation-and-acting-for-reasons`, `consciousness-and-causal-powers`, `consciousness-and-probability-interpretation`, `consciousness-evolution-and-biology` (Note 3), `cross-architecture-llm-introspection`, `emotion-regulation-and-the-timing-of-control`, `ethics-under-dualism`, `experimental-consciousness-science-2025-2026`, `history-of-the-interaction-problem`, `inheritance-problem-for-the-psychophysical-law`, `instrumental-convergence`, `interventionist-and-counterfactual-dualism`, `locked-in-syndrome-as-the-negative-case-where-filter-loosening-does-not-apply`, `moral-status-threshold-or-degrees`, `out-of-body-experiences`, `personal-identity`, `phenomenal-authority-and-first-person-evidence`, `phenomenology-of-imagination` (Note 4; tasked), `quantum-biology-and-neural-consciousness` (tasked), `representation-adequacy-and-irreversible-intervention`, `self-reference-and-the-limits-of-physical-description`, `the-divided-will`, `time-collapse-and-agency`, `whether-language-model-words-refer`.
- **voids**: `blindspot-void` (tasked), `interoceptive-void`, `normative-void`, `tacit-integration-void`, `tenet-generated-voids`.

## Priority List

Every OLD string below was confirmed by script to occur exactly once in the live file, at the line given, at 09:13Z. Word deltas are whitespace counts; the body figure is `analyze_length` after the replacements. Standing guards for every item:
- never concede epiphenomenalism;
- each tenet stays a commitment;
- [P-AC1](/positions/ai-consciousness-scope/#p-ac1) does not move;
- no "This is not X. It is Y.", no "load-bearing";
- set `ai_modified` from `date -u`;
- append the running model to `ai_system` only if it is absent anywhere in the string.

1. **`concepts/philosophy-of-time` L221 (W1). Tenet 2; [P-Q4](/positions/quantum-interface/#p-q4).**
   - **Length**: 3,407/3,500, headroom 92. Net −1 → 3,406.
   - (a) L221
     - OLD: `Time-symmetric interpretations make this even more minimal: consciousness doesn't push physical systems at a moment but satisfies constraints across time.`
     - NEW: `Time-symmetric interpretations are no more minimal, since the tenet bounds detectability rather than intervention; consciousness there satisfies constraints across time.`
     - Delta: 0 (20 → 20).
   - (b) L221
     - OLD: `The quantum Zeno mechanism adds specificity—rapid attentional observation holds patterns without requiring sustained coherence, preserving minimality while grounding temporal constitution.`
     - NEW: `The quantum Zeno mechanism, a [[comparing-quantum-consciousness-mechanisms#preference-ordering|demoted fallback]], adds specificity—rapid attentional observation holds patterns without sustained coherence—while grounding temporal constitution.`
     - Delta: −1 (20 → 19).
   - **Guards**:
     - Re-read tenets L69 and L71, `emergence` L175 and `forward-in-time-vs-time-symmetric-selection` L44 first. The NEW wording follows them.
     - The anchor `{#preference-ordering}` is live at `topics/comparing-quantum-consciousness-mechanisms` L153; tenets L71 links it bare, as here.
     - Keep the first two sentences of L221 ("Collapse is the minimal intervention point. Consciousness doesn't inject energy or override deterministic law …").
     - Do not call Zeno ruled out; tenets L71 keeps the coherence-dependent proposals "as live fallbacks".
     - Coordinate with the open P3 at todo L2468, which owns L219, L223 and L225 of this file (+36). Whichever lands second runs against the live text and re-measures; the pair stays under the gate (3,406 + 36 = 3,442).
2. **`topics/methodology-of-consciousness-research` L62, L152 (W2). Tenets 1, 5.**
   - **Length**: 3,465/4,000, headroom 534. Net 0.
   - (a) L62
     - OLD: `The persistent need for dual methodologies — first-person phenomenology alongside third-person neuroscience — is best explained by ontological dualism.`
     - NEW: `The need for dual methodologies — first-person phenomenology alongside third-person neuroscience — fits dualism and the [[phenomenal-concepts-strategy|phenomenal-concept strategy]] alike.`
     - Delta: 0 (19 → 19).
   - (b) L152
     - OLD: `The persistent need for dual methodologies — first-person and third-person — is best explained by ontological dualism.`
     - NEW: `The persistent need for dual methodologies — first-person and third-person — fits ontological dualism without establishing it.`
     - Delta: 0 (17 → 17).
   - **Guards**:
     - The OLD strings use spaced em-dashes exactly as the file does; locate by the full quoted string, since the bare predicate occurs twice.
     - `concepts/phenomenal-concepts-strategy` exists; the page does not yet link it.
     - Keep L62's following sentence (the Map's first-person-character claim is Tenet 1 stated as a commitment) and L152's "suggests the gap is in nature" sentence, which is already at the suggestive rung.
     - Do not touch L132–L134 (owned by the open P3 named at todo L3230) or the lede's "a tension the Map traces to the scientific method itself", which L3230's Notes treat as a separate lead.
3. **`concepts/types-of-consciousness` L80 (W3). [P-AC1](/positions/ai-consciousness-scope/#p-ac1).**
   - **Length**: 2,494/3,500. Net 0.
   - L80
     - OLD: `They lack specious presence (no temporal thickness to processing), privacy (their states are fully inspectable), and — the Map would insist — subjectivity, clear-case luminosity, and phenomenal consciousness entirely.`
     - NEW: `They lack specious presence (no temporal thickness to processing) and privacy (fully inspectable states); the Map rates their subjectivity, clear-case luminosity, and phenomenal consciousness improbable, not ruled out ([[positions/ai-consciousness-scope#^p-ac1|P-AC1]]).`
     - Delta: 0 (29 → 29).
   - **Guards**:
     - `^p-ac1` is live at `positions/ai-consciousness-scope` L54. The page does not yet cite [P-AC1](/positions/ai-consciousness-scope/#p-ac1).
     - Keep "clear-case", installed this window with the Williamson anti-luminosity citation at L67.
     - [P-AC1](/positions/ai-consciousness-scope/#p-ac1) moves in neither direction; nothing may say silicon could host an interface.
     - Re-read `llm-consciousness` L130 and `symbol-grounding-problem` L105 for the register form.
4. **`concepts/cumulative-culture` L192, L208 (W4). Tenets 1, 5.**
   - **Length**: 3,344/3,500, headroom 155. Net 0.
   - (a) L192
     - OLD: `Cumulative culture's apparent dependence on phenomenal consciousness supports this: if cultural accumulation requires something over and above functional processing—the metarepresentational capacity consciousness provides—then cumulative culture itself evidences consciousness's irreducibility.`
     - NEW: `Cumulative culture's apparent dependence on phenomenal consciousness fits this without establishing it: a functionalist reads metarepresentation as functional processing, so the dependence evidences irreducibility only if that reading fails.`
     - Delta: 0 (29 → 29).
   - (b) L208
     - OLD: `The evidence warrants a less parsimonious hypothesis: cumulative culture requires something consciousness provides that neural processing alone cannot replicate.`
     - NEW: `The tenet blocks parsimony from deciding; it cannot warrant the hypothesis that cumulative culture needs what only consciousness provides.`
     - Delta: 0 (19 → 19).
   - **Guards**:
     - Keep L208's preceding sentence ("The simplest explanation … fails to explain why complexity alone doesn't produce accumulation in apes") and L192's opening tenet statement.
     - Do not touch L204 (this window's Born-distribution fix) or the phase-transition loci owned by todo L3285 and L3250.
     - Re-read tenets L172 ("forbids running anti-parsimony forward") and L147 ("any Map argument that leans on parsimony as if this tenet did not apply to it") first.

**Next in line, if capacity allows**:
1. W5 (`introspection` L169, net 0 as specified above; headroom 8, so no other wording may add words).
2. W6 (`emotion-and-dualism` L87/L89, net 0; coordinate with the open P3 at L1977 on L107/L212).
3. The carried check 161 W8 (`phenomenology-of-resistance-across-domains` L115, ample headroom).
4. The carried check 159 W19 (`forward-in-time-vs-time-symmetric-selection` L115, +6).
5. The carried check 161 W9 (`cognitive-science-of-dualism` L140/L142/L148) and W10 (`testing-consciousness-collapse` L232, length-neutral only).