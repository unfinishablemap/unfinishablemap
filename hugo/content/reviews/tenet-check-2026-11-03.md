---
ai_contribution: 100
ai_generated_date: 2026-11-03
ai_modified: 2026-11-03 18:37:56+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-11-03
date: &id001 2026-11-03
description: 'Tenet check 160, a delta check of 84 changed pages: no Errors, no over-correction,
  no AI-verdict drift. 16 Warnings, chiefly Relation-section twins the day''s Zeno,
  magnetoreception and shared-debt fixes left behind.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-11-03 18:37:56+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-11-03
topics: []
---

# Tenet Alignment Check

**Date**: 2026-11-03. This is check 160. The previous one, [reviews/tenet-check-2026-11-02.md](/reviews/tenet-check-2026-11-02/), was check 159. Its Warnings W1–W22 and Notes 1–14 are not raised again here.

**Files checked**: 84. These are every file in `topics/` (36), `concepts/` (27), `voids/` (10), `apex/` (6), `positions/` (1) and `arguments/` (4) changed since check 159's scan HEAD, `cb1b423273` (2026-11-02 04:07Z).
- **Window.** 157 commits ran from `bf8234e091` (11-02 04:49Z) to `731098aa86` (11-03 18:12Z), which is HEAD. The only uncommitted change is `workflow/evolution-state.yaml`, and no content file is dirty. No file is new.
- **How the pages were read.** Every changed body span was read against the text it replaced, using a word-level diff of the frontmatter-stripped bodies. That came to about 8,150 changed words, 914 of them in `arguments/`.
- **Relation sections.** All 84 were swept with eight lens patterns: support verbs, "predicts/expected", "genuine causal", parsimony, many-worlds, AI-verdict vocabulary, collapse-causing wording and Born/conservation wording. About 40 were read in full, along with every hit.
- **Ledes.** The first three body paragraphs of every page were swept for strong evidential verbs.
- **No subagents.** The driver read everything. Every quote below was confirmed by `grep -c -F` = 1 at the line given.
- **Prior reviews honoured.** These were every window deep review (11-02: dynamical-relevance, evolutionary-case, forward-in-time, functionalism-argument, inner-speech, many-worlds-argument, philosophy-of-action; 11-03: affective-tone, Occam limits, ethics-of-AI, interventionist dualism, single-cell). Also honoured were the 11-02 apex-evolve of self-concealing-interface and its stability notes. Where a finding goes past a stability note, the reason is given in place.
- **Pricing.** Word deltas come from `tools.curate.length.count_words` on the frontmatter-stripped body after each replacement, applied in order. Headroom is hard − 1 − count, and the gate is `>=`.
- **Brief check.** `topics/consciousness-and-the-physics-of-information` did not change in this window. Its last commit is `f36f451fca` (10-12). Its 11-03 optimistic-review work is queued as an open P3 (todo L4070) and has not landed. It was not re-read.

**Errors**: 0

**Warnings**: 16. Eleven sit on window-touched pages next to a sentence the window recalibrated. Five sit on unchanged lines of window-touched pages. No page contradicts a tenet outright.

**Notes**: 14

**Tasks minted**: 0. The skill is reports-only and does not instruct minting. The Priority List below carries four items, each with OLD/NEW text checked by script, plus one fold-in for an open task.

## Summary

**The day's recalibrations held where they landed.** `topics/motor-control-quantum-zeno` was refined four times. It now says:
- the selector "would act" at threshold-crossing (L38);
- the parietal/premotor dissociation is "neural separability, which materialism predicts equally well" (L125);
- the bandwidth "is consistent with" policy-level selection (L127);
- "The Zeno mechanism below does not supply this outcome selection" (L95);
- neural determinism "readily explains the willed/instructed neural difference" (L133).

The seven named satellites took the timing corrections. These include `conscious-vs-unconscious-processing` L247, now "Timing remains open", which closes check 159 W15. The magnetoreception refine (`3623d0d763`) re-graded the avian compass from established to leading-but-unsettled across `decoherence-and-macroscopic-superposition` (L90, L94, L100, L114, L140). `self-concealing-interface` was rebuilt to the null-result rule (L93–L95).

**The main finding is twins left behind in Relation sections.** The pattern is the one check 159 found, now one layer further out:
- **Zeno/motor cluster.** `concepts/motor-selection` was edited twice today as a Zeno satellite. Its own Relation section still makes the three claims the parent just withdrew (W1): L198 "supports the Dualism tenet", L202 "matches", and L214 "still owes an account of why the willed/instructed distinction exists neurally".
  - `concepts/von-neumann-wigner-interpretation` was also edited today. L112 still credits "Stapp's quantum Zeno mechanism that specifies *how* consciousness acts" (W2), against its own L94 ("acknowledges but does not adopt") and [P-Q4](/positions/quantum-interface/#p-q4).
- **Magnetoreception.** `decoherence-and-macroscopic-superposition` L138 says free will "gains support from this picture" and gets "a mechanism for agent causation" (W3). One paragraph below, L140 says "It does not supply positive evidence for the interface".
- **Shared-debt verdict (01:05Z).** `pain-consciousness-and-causal-power` L160 now says "the law itself is shared". Its L174 still says many-worlds realises "every [supervenience](/concepts/supervenience/) mapping … somewhere", and that "the simplest" explanation "may be that the suffering itself was selected for" (W4). That is a physics error and a parsimony move in the Map's favour, in one paragraph.
- **Self-stultification narrowing (11-02 15:27Z).** The hub now says the view cannot be rationally "held if knowing an experience requires causal traffic from it" (L45). `ai-epiphenomenalism` L109 still says the argument "establishes this for human consciousness, against bare-correlation epiphenomenalism" (W5). That contradicts tenets L101, which says the Map holds Tenet 3 "not because the self-stultification argument refutes epiphenomenalism from inside the epiphenomenalist's framework".

**Lens (a), over-correction: none.** Every window concession keeps the tenet as a commitment and inherits its debt rather than conceding epiphenomenalism. Models:
- `cross-state-void` L93: "The Map's reading is compatible with the data rather than supported by them, and inherits the debt recorded at [the tenet's standing note](/tenets/#tenet-3-standing)."
- `valence-void` L117 uses the same form.
- `self-concealing-interface` L95: a null "counts as *neither* confirmation *nor* refutation".
- `affective-tone-divergence` L114: the Bidirectional reading is "held as a live option rather than asserted as the established mechanism".
- `neurological-dissociations` L178: type identity "expects them too: they constrain which states it names without refuting it".

**AI calibration: no drift in either direction.** `ethics-of-possible-ai-consciousness` L44 moved "structural near-exclusion" to "low-probability", and L150 says "the low-probability side". `dynamical-relevance` L106 says Dualism "permits the refusal of Definition 3 without forcing it". `functionalism-argument` L201 ("classical bit operations provide no purchase") is scoped to computation and backed by `ai-hardware-substrate-taxonomy`, per its 11-02 deep review (Note 14). Nothing says silicon could host an interface. Nothing new says "cannot be conscious".

**Collapse ordering: clean.** `von-neumann-wigner` L102 ("collapse no longer requires consciousness; consciousness biases what would have happened anyway") and `decoherence-and-macroscopic-superposition` L136 are controls.

**Tenet 4.**
- `functionalism-argument` L209 enlists No Many Worlds against functionalism (W7), in the cluster where the matrix records it as not invoked.
- `phenomenology-mechanism-bridge` L176 reads it off felt willing (W16).
- `pain` L174 is part of W4.
- Controls:
  - `many-worlds-argument` L62 concedes the diverging-worlds reading: "the Map concedes that this fission-shaped argument does not reach it".
  - `phenomenal-concepts-strategy` L193 says "branching leaves zombie conceivability untouched".
  - `binding-problem` L212 says "felt definiteness is equally available branch-relatively".
  - `pharmacological-dissociation` L186 and `neurological-dissociations` L200 are also controls.

**Tenet 5.**
- Parsimony is nowhere used as decisive against dualism.
- Two pages claim a parsimony advantage *for* the Map (W15), the family owned by the NEEDS-HUMAN at todo L97. One more adds an asymmetric "merely hoped to work" (W14).
- `motor-selection` L214 (W1) and `pain` L174 (W4) carry the Map-favouring form inside tasked items.
- Controls:
  - `phenomenology-mechanism-bridge` L178: "it does not turn the chain's complexity into evidence that reality shares it".
  - `consciousness-disruption` L180: "simplicity alone cannot adjudicate here".
  - `valence-and-conscious-selection` L210.
  - `epistemological-limits-of-occams-razor` L40 (today's deep review).

**Check 159 Priority List.** None of the six tasks has landed: IIT (todo L3798), what-it-might-be-like (L3807), sorkin-delta (L3817), attentional-economics (L3826), time-consciousness (L3835) and phenomenal-transparency (L3844). None of those pages changed in this window, so their findings stand as check 159 left them. Check 159 W15 landed through the Zeno satellite sweep `d532895034`.

## Method: families, violations and on-page controls

| Lens | Violations in window | Controls |
|---|---|---|
| (a) over-correction | 0 | cross-state-void L93, valence-void L117, self-concealing L95, affective-tone L114, neurological-dissociations L178 |
| (b) datum or fit read as evidence | W1 (L198), W3, W4 (L170), W6, W9, W11, W12, W13 | motor-control L125, motor-selection L206, split-brain L182, pain L170 (first clause), inaccessible-past L134 |
| (c) Tenet 4 off experience, or wrongly enlisted | W4 (L174), W7, W16; Notes 1, 5 | many-worlds-argument L62, PCS L193, binding-problem L212, pharmacological L186, precommitment L110 |
| (d) Tenet 5 | W1 (L214), W4 (L174), W14, W15; Note 12 | mechanism-bridge L178, consciousness-disruption L180, valence-selection L210, Occam-limits L40 |
| (e) co-optation / concept provenance | W8 (Loar) | brain-organoids L67 (Wood et al.'s dissent named), single-cell L88 (Levin's inference declined), dynamical-relevance L106 (Chalmers's organizational invariance) |
| (f) collapse ordering | 0 | von-neumann-wigner L102, decoherence-macro L136 |
| (g) mechanism ranking, Born and bandwidth wording | W1 (L202), W2, W5, W10 | self-concealing L79/L105/L171, memory-channel L146, neurological-dissociations L198, bacterial-chemotaxis L90 |
| (h) AI calibration | 0 | ethics-of-AI L44/L150, dynamical-relevance L34/L106, functionalism L201 (Note 14) |

The keyword counts are lexical upper bounds: 222 parsimony hits and 233 many-worlds hits in Relation sections, most of them on index pages. The violations column holds only what survived reading in context.

## Errors

None.

## Warnings

### Priority List items (1–4) and the fold-in

**W1. `concepts/motor-selection` L198, L202, L214: three Relation-section claims the parent page withdrew today**
- **Tenets**: 1, 2, 5.
- **Quotes** (each once):
  - L198: "The attention-motor unification supports the [Dualism](/tenets/#dualism) tenet." It goes on: the dissociation "suggests something contributes to intention that is not identical to motor execution machinery", and the shared feeling of willing is "suggesting a common agent behind both".
  - L202: "(~10 bits/second for conscious processing) matches policy-level operation".
  - L214: "The \"simpler\" neural-determinism view still owes an account of why the willed/instructed distinction exists neurally (why maintain it if epiphenomenal?)".
- **Issue**:
  - The parent `topics/motor-control-quantum-zeno` now says of the same dissociation that it "is neural separability, which materialism predicts equally well" (L125). It says the bandwidth "is consistent with" policy-level selection (L127). It says neural determinism "readily explains the willed/instructed neural difference as added decision load, and why effort tracks difficulty" (L133, refined at 09:03Z by `8061e31d22`).
  - motor-selection was edited at 07:44Z (`a4ef50fa06`) and 10:11Z (`0fa0ed3713`) as a satellite of those fixes, and its Relation section was not reached.
  - L214 also runs neural determinism together with epiphenomenalism. An identity theorist holds the neural difference to be the conscious one.
  - Check 157 W10 named L198/L210/L214 and did not task them ("below the cap"). Today's parent fix turns them into a direct contradiction.
- **Rung earned**: compatible. **Priority 1.** 3,497/3,500, headroom 2. Net −3.

**W2. `concepts/von-neumann-wigner-interpretation` L112: Zeno credited with specifying how consciousness acts**
- **Tenets**: 2, 3 (Definition: outcome-selection; Process 1 "registered … but *not* adopted"), [P-Q4](/positions/quantum-interface/#p-q4).
- **Quote** (once): L112, "and Stapp's quantum Zeno mechanism that specifies *how* consciousness acts."
- **Issue**:
  - The page's own L94 says the Process-1 placement "is one the Map **acknowledges but does not adopt**" and names post-decoherence selection as "the path the Map endorses most strongly".
  - Today's parent fix says "The Zeno mechanism below does not supply this outcome selection" (motor-control L95). On Stapp's reading the agent chooses "which question is put and how often, never the answer" (L105).
  - [P-Q4](/positions/quantum-interface/#p-q4) (`positions/quantum-interface` L88) is headed "Stapp's quantum Zeno mechanism is currently demoted relative to post-decoherence selection".
  - L84 and L96 of this page were corrected today by the Zeno satellite sweep (`d532895034`). L112 was missed. [reviews/tenet-check-2026-09-06.md](/reviews/tenet-check-2026-09-06/) flagged the same sentence.
- **Rung**: n/a (mechanism-ranking drift). **Priority 2.** 2,894/3,500; +10.

**W3. `topics/decoherence-and-macroscopic-superposition` L138: "gains support" one paragraph above "does not supply positive evidence"**
- **Tenets**: 2, 3.
- **Quotes** (each once):
  - L138: "The Map's defense of [free will](/topics/free-will/) gains support from this picture."
  - L138: "this provides a mechanism for agent causation".
  - L138: "The receding quantum-classical boundary expands the domain where such choices could operate."
- **Issue**:
  - L140 has said since 07-18 (`d8274b9d3b`) that the receding boundary leaves Tenet 2 "freed of one objection … though not positively confirmed by it. … It does not supply positive evidence for the interface". Today's 16:57Z magnetoreception refine (`3623d0d763`) re-graded L140's compass sentence and left L138, which has stood since 01-27 (`6357941b31`).
  - The boundary has receded in laboratory systems (hot cat states at 1.8 K, nanoparticle interference; L32). The Map's preferred route does not depend on neural coherence at all (tenets L71).
  - So "a mechanism for agent causation" and "expands the domain" in neural tissue claim what L140 denies.
  - The open P3 at todo L4143 (the magnetoreception ratio) is on a different section of the same page.
- **Rung earned**: compatible. **Priority 3.** 3,354/4,000; +7.

**W4. `topics/pain-consciousness-and-causal-power` L170 (second half) and L174: residue of the 01:05Z shared-debt alignment**
- **Tenets**: 3, 4, 5.
- **Quotes** (each once):
  - L170: "imagined future pain alters present behaviour through phenomenal content alone" and "Suffering's causal efficacy extends further".
  - L174: "every [supervenience](/concepts/supervenience/) mapping is realised somewhere".
  - L174: "the simplest may be that the suffering itself was selected for".
- **Issue**:
  - The 11-03 01:05Z refine (`0380688711`) made L160 say "the [law itself](/topics/inheritance-problem-for-the-psychophysical-law/#harmony) is shared". The 11-02 09:45Z Noordhof refine (`75f598a14a`) made L170's first sentence end "a pattern compatible with phenomenal causation rather than evidence for it".
  - L170's next sentences then assert a purely phenomenal route and "causal efficacy" outright.
  - L174 fails three ways. Everettian branches share one dynamics, so no branch varies the psychophysical mapping, and the premise is false. It uses simplicity in the Map's favour, against tenets L147: "any Map argument that leans on parsimony as if this tenet did not apply to it". And it re-asserts the one-sided correlation verdict L160 retired.
- **Rung earned**: compatible (L170); n/a (L174, a factual error). **Priority 4.** 3,995/4,000, headroom 4. Net −27.

**W5. `concepts/ai-epiphenomenalism` L109: self-stultification said to "establish" efficacy against the bare-correlation view**
- **Tenet**: 3 (`^tenet-3-epiphenomenalism`, L101).
- **Quotes** (each once):
  - L109: "The self-stultification argument establishes this for human consciousness, against bare-correlation epiphenomenalism."
  - L109: "self-stultification then secures actual efficacy only for report-grounded consciousness".
- **Issue**:
  - Tenets L101 names the bare-correlation reply as the epiphenomenalist's best. It holds Tenet 3 "not because the self-stultification argument refutes epiphenomenalism from inside the epiphenomenalist's framework".
  - On 11-02 the hub `concepts/self-stultification` L45 was narrowed (`222640368d`): the view cannot be "held if knowing an experience requires causal traffic from it". `concepts/consciousness` L117 (`74b8b9f758`) and `the-epiphenomenalist-threat` L158 (`7a122c0f70`) retired the luck framing the same day.
  - This page was touched on 11-03 (L85, Schwitzgebel, in the ethics-of-AI deep review) and keeps the un-narrowed form. The open P3 on this file (todo L3548) owns L51/L81/L111 but not L109.
- **Rung**: n/a (argument-strength overstatement). **Fold-in** to todo L3548, not a new task. 2,987/3,500; +17.

### Untasked, on window-touched pages

**W6. `voids/valence-void` L115 (and lede L43): "particularly strong support" in the sentence that now says "without settling"**
- **Tenet**: 1.
- **Quotes** (each once):
  - L115: "**[Dualism](/tenets/#dualism)** finds particularly strong support."
  - L115, two clauses on (installed 11-02 09:45Z by `75f598a14a`): "as the explanatory gap suggests and pain asymbolia illustrates without settling".
  - L43: "Introspection reveals valence as primitive and irreducible".
- **Issue**: the support is conditional on the dualist premise itself ("If the felt badness … cannot be captured"). The 11-02 edit graded the asymbolia leg "without settling" and left the headline. **Rung**: compatible. 2,253/3,000; ample headroom. Next in line after the Priority List.

**W7. `arguments/functionalism-argument` L209 (and L193): No Many Worlds enlisted against functionalism**
- **Tenet**: 4, matrix row "Conceivability arguments / qualia cluster", where No-MWI is **not invoked**.
- **Quotes** (each once):
  - L209: "The [No Many Worlds](/tenets/#no-many-worlds) tenet connects to anti-functionalism through [haecceity](/concepts/haecceity/)".
  - L209: "Functionalism cannot capture that particularity."
  - L193: "connect to all five tenets".
- **Issue**:
  - Tenets L172 says "a No-Many-Worlds subsection in a cluster article should read as an intra-framework coherence remark rather than as inheritance in either direction".
  - Functionalism is neutral between one-world and many-worlds. A functionalist in a collapse world has "one actual outcome" too, so the sentence is a non sequitur.
  - The 11-02 deep review moved the one-outcome clause inside "the Map insists" but kept the inference. It deferred only the Posit One qualifier.
- 3,496/3,500, headroom 3. A fix must be net-negative. The calibrated model is `phenomenal-concepts-strategy` L193.

**W8. `concepts/phenomenal-concepts-strategy` L191: Loar enlisted for consciousness "directly grasping" its states, read as downward causation**
- **Tenet**: 3; concept-provenance leg of the co-optation firewall.
- **Quotes** (each once):
  - L191: "the deployment of phenomenal concepts itself requires causal work".
  - L191: "If phenomenal concepts involve consciousness directly grasping its own states (as Loar suggests), this grasping may constitute the kind of downward causation the Map affirms."
- **Issue**:
  - Loar (1990) is a physicalist. His phenomenal concepts are recognitional concepts that refer directly to *physical* properties, so the "grasping" he describes is the physical-physical route the page's own §PCS sets out.
  - "Requires causal work" slides from brain causation to mental causation.
  - The page was edited on 11-02 (L75, Chalmers's horn 2, `50743e7b69`). 3,455/3,500, headroom 44.

**W9. `topics/evolutionary-case-for-mental-causation` L167: "the interactionist position resolves" against L73's shared debt**
- **Tenets**: 3, 5.
- **Quote** (once): L167, "creates explanatory puzzles the interactionist position resolves".
- **Issue**: the 11-02 deep review installed at L73 that "the interactionist owes its own account of why these neural states present these feelings, a shared debt". The Occam line still says the puzzles are resolved. Its stability notes protect the lede's "strong abductive case" and the selectability sentence, not L167. 3,254/4,000.

**W10. `concepts/interface-friction` L114: Tenet 2's minimality read as narrowness**
- **Tenet**: 2 (L69: minimality is "empirical-constraint minimality, fixed by the Rules-out clause").
- **Quote** (once): L114, "The interface is narrow precisely because the tenet demands minimal intervention."
- **Issue**: the window fixed this reading elsewhere. Examples: `self-concealing-interface` L105, "the tenet's minimality is fixed by the empirical record, not by a bandwidth"; `memory-channel` L146, "its minimality bounds detectability, not channel width"; `neurological-dissociations` L198. The same paragraph's "broader scope, finer grain … would … violate the constraint" goes beyond the Rules-out clause. The page was edited today (L60). 2,569/3,500.

**W11. `topics/volitional-control` L154, L156: "the tenets predict the pattern" against the same paragraph's "Neither result adjudicates"**
- **Tenets**: 1, 3.
- **Quotes** (each once):
  - L154: "predict the pattern the evidence reveals" and, three sentences later, "Neither result adjudicates between physicalism and dualism".
  - L156: "the neuroplasticity evidence is suggestive".
- **Issue**: a "suggestive" grade must say why the Map's reading fits better. Schwartz's therapy-correlated brain changes are predicted equally by physicalism, as `stapp-quantum-mind` L47 now says ("fits a materialist explanation equally well").
- 4,992/4,000: over the hard limit, under the length NEEDS-HUMAN at todo L653. Any fix must be net-negative.

**W12. `topics/motor-control-quantum-zeno` L129, L133: two unchanged lines beside today's fixes**
- **Tenets**: 3, 5.
- **Quotes** (each once):
  - L129: "Motor control is where consciousness most visibly affects the physical world."
  - L133: "less parsimonious but explanatorily richer".
- **Issue**:
  - The satellite already carries the calibrated form: motor-selection L206, "Motor control is where consciousness *seems* most obviously to affect the physical world, but the seeming is not itself the evidence".
  - After today's L133 concession (neural determinism "readily explains" both the neural difference and effort tracking), "explanatorily richer" names no explanandum the rival misses beyond the framework-boundary one.
  - [reviews/tenet-check-2026-09-27.md](/reviews/tenet-check-2026-09-27/) and check 157 (10-29) flagged L129. 3,871/4,000, headroom 128.

**W13. `voids/mood-void` L111, L115: a floor "counts as confirmation"**
- **Tenets**: 1, 3.
- **Quotes** (each once):
  - L111: "Convergence of independent programmes on a non-zero floor counts as confirmation".
  - L115: "structural evidence — not proof".
- **Issue**: the page's own reductionist reply at L121 maps the opacity layers onto circuit architecture, which also predicts floors, and the Map "concedes it may be sufficient as a description". L123 grades the relation "compatibility, which falls short of confirmation". Touched on 11-02 (L37, `39038241ea`). 2,509/3,000.

**W14. `concepts/binding-problem` L214: classical binding "merely hoped to work", next to quantum binding unconfirmed**
- **Tenet**: 5 (matrix "parsimony asymmetry").
- **Quote** (once): L214, "it's merely hoped to work".
- **Issue**: today's fix made L165 read "made quantum binding empirically distinguishable without confirming it". Both hypotheses are unconfirmed, so the asymmetric dismissal goes. 3,383/3,500, headroom 116.

**W15. `topics/the-strong-emergence-of-consciousness` L167; `concepts/phenomenal-concepts-strategy` L195: parsimony claimed for the Map**
- **Tenet**: 5 (Rules-out, internal clause).
- **Quotes** (each once):
  - strong-emergence L167: "the parsimony advantage tilts back toward strong emergence with mechanism".
  - PCS L195: "perhaps the simpler explanation is that physics genuinely cannot capture everything".
- **Issue**: this is the counterpart of the tiebreaker family: the Map takes the parsimony discount Tenet 5 forbids it. Recorded against the NEEDS-HUMAN at todo L97 and not tasked. Both pages were touched in the window (strong-emergence L131 on 11-03, PCS L75 on 11-02).

**W16. `apex/phenomenology-mechanism-bridge` L176: Tenet 4 read off the phenomenology of willing**
- **Tenet**: 4.
- **Quote** (once): L176, "fits singular actualisation more naturally than branching".
- **Issue**: an Everettian predicts the same felt cost and felt singularity on every branch, as `binding-problem` L212 states. Flagged by [reviews/tenet-check-2026-09-25.md](/reviews/tenet-check-2026-09-25/) and [reviews/tenet-check-2026-09-28.md](/reviews/tenet-check-2026-09-28/) and never tasked. Touched today (L183). 4,926/5,000, headroom 73.

## Notes

1. `concepts/consciousness` L198 states No Many Worlds flat in the Map's voice ("Quantum measurement involves real selection, not branching. Consciousness participates in this selection, making indexical identity coherent."). The page was touched on 11-02 at L117.
2. `voids/recognition-void` L120: "receives powerful support" (Tenet 5) is headline-strong. The paragraph's last sentence calibrates it ("a coherence property of the Map's self-image rather than independent confirmation").
3. `apex/taxonomy-of-voids` L231/L233 ("receives the strongest support", "gains cumulative support") were flagged by [reviews/tenet-check-2026-09-28.md](/reviews/tenet-check-2026-09-28/) and [reviews/tenet-check-2026-10-08.md](/reviews/tenet-check-2026-10-08/). Today's edit (L133, "ten"→"nine") did not touch them. The second sentence is already capped by the common-cause null.
4. `voids/transformative-experience-void` L123: "the Map's apophatic methodology is vindicated". This is methodological, but "vindicated" outruns the void's own "mapping" register.
5. Tenet 4 without Posit Three in the motor cluster:
   - `motor-control-quantum-zeno` L131 says branching reduces the agent's contribution "to indexical perspective rather than genuine selection". The open sweep at todo L1874 cites this paragraph as a control (as "L129"; it has drifted to L131).
   - `motor-selection` L210 says "there's nothing for consciousness to select" (check 157 W10). Both should name global exclusion as a posit (`tenets/background-commitments`).
6. `concepts/conscious-vs-unconscious-processing` L46: reading these words "demonstrates consciousness at work". A physicalist grants the functional claim, so the sentence does no dualist work. It belongs to the lede, not a tenet paragraph.
7. `topics/pain-consciousness-and-causal-power` L64 calls asymbolia "the single most discriminating empirical test case in philosophy of mind". The page's own L170 now grades it compatible. There is no headroom after W4 except W4's own savings.
8. `concepts/von-neumann-wigner-interpretation` L114: "the measurement problem's openness to consciousness is a feature, not a bug". Tenets L184: once objective reduction secures definiteness, "the measurement problem cannot itself be evidence for conscious selection". The line is rhetorical, not an evidence claim. It could ride W2.
9. `topics/evolutionary-case-for-mental-causation` L37: "provides significant evidence" sits one sentence before "suggestive rather than demonstrative". The 06-04 stability note protects "strong abductive case", not this phrase.
10. The brief named `consciousness-and-the-physics-of-information` as recalibrated today. It is unchanged since 10-12, and its queued work is the open P3 at todo L4070.
11. **Outside the window, Zeno-ranking leads.** These pages are unchanged, so this is a lead only, for the next propagation sweep:
    - `concepts/attention-as-interface` L155: "The Map's proposed mechanism—the quantum Zeno effect ([Stapp](/concepts/stapp-quantum-mind/))".
    - `topics/the-interface-problem` L117: "Stapp's quantum Zeno model is the most detailed specification".
    - Both are at odds with tenets L71 and [P-Q4](/positions/quantum-interface/#p-q4) as W2 is.
12. `topics/the-epiphenomenalist-threat` L176: "as Kim showed" presents the exclusion argument's collapse of non-reductive physicalism as settled. Kim's argument is contested.
13. `concepts/motor-selection` L188 ("But as Tallis notes, illusions presuppose experience.") and L190 ("this correlation would be coincidental") are check 157 W10 residue. The coincidence framing was retired on 11-02 at `concepts/consciousness` L117 and `the-epiphenomenalist-threat` L158. There is no headroom on this page beyond W1's three-word saving.
14. `arguments/functionalism-argument` L201, "classical bit operations provide no purchase for quantum-consciousness interaction", is a control for [P-AC1](/positions/ai-consciousness-scope/#p-ac1). It speaks of the computation, and its 11-02 deep review sourced it to `ai-hardware-substrate-taxonomy` §The Indeterminacy Distinction. The same line's "This gives empirical content to the anti-functionalist position" is mildly strong for an interpretive tenet.

## Already tasked (cited, not re-flagged)

- `concepts/phenomenology-of-choice-and-volition` L165/L163: Tenet 4 and Tenet 2 read off feeling. Open P3 at todo L2514. Its lede L56 belongs to the BLOCKED label task that P3 names.
- `concepts/ai-epiphenomenalism` L51/L81/L111: the flat AI verdict. Open P3 at todo L3548. W5 is offered as a fold-in to that task.
- `topics/decoherence-and-macroscopic-superposition` §Avian Magnetoreception ratio: open P3 at todo L4143.
- `topics/evolution-under-dualism` L131: the compass presupposed. Open P3 at todo L4152, minted 11-03.
- `apex/moral-architecture-of-consciousness` L148: one-sided co-optimization verdict. Open P3 at todo L3972.
- The parsimony tiebreaker family and its Map-favouring counterpart (W15): NEEDS-HUMAN at todo L97.
- `topics/volitional-control` length: NEEDS-HUMAN at todo L653.
- Check 159's six tasks: todo L3798, L3807, L3817, L3826, L3835, L3844, all pending.

## Files Passing All Checks

These are window pages whose changed spans, lede and Relation section raised nothing beyond the controls cited above.

- **apex**: `apex-articles`, `judging-the-map-as-science`, `pharmacological-dissociation-as-evidence`, `self-concealing-interface`.
- **concepts**: `affective-forecasting-gap`, `blindsight`, `causal-closure`, `decoherence`, `disconnection-neuroscience`, `emergence`, `epiphenomenalism`, `inference-to-the-best-explanation-against-dualism`, `lawful-appearance-problem`, `libet-experiments`, `psychophysical-social-choice-problem`, `scale-types-for-phenomenal-quantities`, `self-stultification`, `source-versus-leeway-incompatibilism`, `stapp-quantum-mind`, `subject-fusion`, `timing-gap-problem`, `zeno-dynamics-on-a-decohered-mixture`.
- **positions**: `agency-and-will`.
- **topics**: `affective-tone-divergence-across-meditative-traditions`, `anarchic-hand-and-action-ownership`, `attention-and-the-consciousness-interface`, `bacterial-chemotaxis-and-minimal-biogenic-cognition`, `born-rule-and-the-consciousness-interface`, `brain-organoids-and-the-organoid-intelligence-question`, `capgras-delusion-and-the-affective-recognition-channel`, `clinical-dissociation-as-systematic-evidence`, `consciousness-disruption-and-the-mind-brain-interface`, `duhem-quine-underdetermination-consciousness`, `dynamical-relevance-and-the-verification-boundary`, `ethics-of-possible-ai-consciousness`, `forward-in-time-vs-time-symmetric-selection`, `immediate-emotions-and-the-affect-heuristic`, `inheritance-problem-for-the-psychophysical-law`, `inner-speech-and-anendophasia`, `interventionist-and-counterfactual-dualism`, `memory-channel-interface-evidence`, `neurological-dissociations-as-interface-architecture`, `neuron-less-animals-sponges-placozoans-and-the-lower-bound-of-cognition`, `phenomenology-of-philosophical-disagreement`, `philosophy-of-action-under-dualism`, `precommitment-and-the-diachronic-agent`, `single-cell-proto-agency-and-the-evidence-problem`, `split-brain-consciousness`, `the-consequence-argument-for-incompatibilism`, `the-enteric-nervous-system-and-the-gut-brain-distributed-interface-question`, `the-experience-requirement-on-well-being`, `valence-and-conscious-selection`.
- **voids**: `cross-state-void`, `inaccessible-past`, `sleep-consciousness-void`, `three-kinds-of-void`, `voids-between-minds`, `voids`.
- **arguments**: `arguments`, `epistemological-limits-of-occams-razor`, `many-worlds-argument`.

## Priority List

Every OLD string below was confirmed by script to occur exactly once, at the line given. Deltas are `count_words` on the frontmatter-stripped body after the replacement, applied in order. Standing guards for every item:
- never concede epiphenomenalism;
- each tenet stays a commitment;
- [P-AC1](/positions/ai-consciousness-scope/#p-ac1) does not move;
- no "This is not X. It is Y.", no "load-bearing";
- set `ai_modified` from `date -u`;
- append the running model to `ai_system` only if it is absent anywhere in the string.

1. **`concepts/motor-selection` L198, L202, L214 (W1). Tenets 1, 2, 5.**
   - **Length**: 3,497/3,500, headroom 2. Net −3 → 3,494. No other edit fits.
   - (a) L198
     - OLD: `The attention-motor unification supports the [[tenets#^dualism|Dualism]] tenet. The dissociation between intention (parietal) and execution (premotor) suggests something contributes to intention that is not identical to motor execution machinery. Both willed attention and willed action feel like *you* doing something, suggesting a common agent behind both.`
     - NEW: `The attention-motor unification fits the [[tenets#^dualism|Dualism]] tenet without evidencing it. The dissociation between intention (parietal) and execution (premotor) is neural separability, which materialism predicts equally well. Willed attention and willed action both feel like *you* doing something, which fits a common agent without showing one.`
     - Delta: 0.
   - (b) L202
     - OLD: `The bandwidth constraint (~10 bits/second for conscious processing) matches policy-level operation`
     - NEW: `The bandwidth constraint (~10 bits/second of behavioural throughput) fits policy-level operation`
     - Delta: 0. Zheng & Meister (2025) measure behavioural throughput, as the parent's L81 now says.
   - (c) L214
     - OLD: `The "simpler" neural-determinism view still owes an account of why the willed/instructed distinction exists neurally (why maintain it if epiphenomenal?) and why accurate effort phenomenology would evolve if causally inert. The [[tenets#^occams-limits|Occam's Razor Has Limits]] tenet explains: parsimony is unreliable when our knowledge is incomplete.`
     - NEW: `The simpler neural-determinism view readily explains the willed/instructed neural difference as added decision load, and why effort tracks difficulty; why that tracking is felt at all sits at the framework boundary, where the [[tenets#^occams-limits|Occam's Razor Has Limits]] tenet bars simplicity from deciding.`
     - Delta: −3.
   - **Guards**:
     - Re-read `topics/motor-control-quantum-zeno` L125, L127 and L133 first. The NEW wording is theirs.
     - Keep L206, the calibrated Bidirectional paragraph.
     - Leave L188, L190 and L210 (Notes 5 and 13). There is no headroom for them.
2. **`concepts/von-neumann-wigner-interpretation` L112 (W2). Tenets 2, 3, [P-Q4](/positions/quantum-interface/#p-q4).**
   - **Length**: 2,894/3,500; +10 → 2,904.
   - OLD: `and Stapp's quantum Zeno mechanism that specifies *how* consciousness acts.`
   - NEW: `and candidate accounts of *how* consciousness acts, led by [[post-decoherence-selection|post-decoherence selection]], with Stapp's question-selecting Zeno mechanism ranked below it ([[positions/quantum-interface#^p-q4|P-Q4]]).`
   - **Guards**:
     - Re-read this page's L94 and motor-control L95/L105 first.
     - `^p-q4` exists at `positions/quantum-interface` L90.
     - Do not call Zeno ruled out. Tenets L71 keeps the coherence-dependent proposals "as live fallbacks".
     - Keep "interface locality that resolves the multi-observer problem". It matches `multi-mind-collapse-problem`'s own "dissolves".
     - Note 8 (L114) may ride if the writer wishes. It is optional.
3. **`topics/decoherence-and-macroscopic-superposition` L138 (W3). Tenets 2, 3.**
   - **Length**: 3,354/4,000; +7 → 3,361.
   - OLD: `The Map's defense of [[topics/free-will|free will]] gains support from this picture. If consciousness can bias quantum outcomes at neural decision points, this provides a mechanism for agent causation—genuinely open futures that conscious choices help determine. The receding quantum-classical boundary expands the domain where such choices could operate.`
   - NEW: `The Map's defense of [[topics/free-will|free will]] is consistent with this picture without gaining support from it. If consciousness can bias quantum outcomes at neural decision points, agent causation would have a candidate locus—open futures that conscious choices help determine—but a boundary receding in laboratory systems does not show that neural tissue supplies one (below).`
   - **Guards**:
     - Keep L140 exactly as it stands, including today's compass wording.
     - Coordinate with the open P3 at todo L4143. It is a different section (§Avian Magnetoreception) and has no textual overlap.
     - Keep the page's "defense" spelling.
4. **`topics/pain-consciousness-and-causal-power` L170, L174 (W4). Tenets 3, 4, 5.**
   - **Length**: 3,995/4,000, headroom 4. Net −27 → 3,968.
   - (a) L170
     - OLD: `The anticipatory dimension broadens this: imagined future pain alters present behaviour through phenomenal content alone, with no current nociceptive input. Suffering's causal efficacy extends further —`
     - NEW: `The anticipatory dimension broadens the pattern: imagined future pain alters present behaviour with no current nociceptive input, which neural simulation explains as readily. Suffering's reach is wider still —`
     - Delta: +3.
   - (b) L174
     - OLD: `The evolutionary argument against epiphenomenalism gains force from the Map's rejection of MWI. Under many-worlds, one might argue that every [[supervenience]] mapping is realised somewhere, weakening the demand to explain *why this particular mapping* — why tissue damage of type X produces suffering of character Y. In a single-history universe, the systematic alignment of suffering-type with damage-type is a contingent fact that demands causal explanation, and the simplest may be that the suffering itself was selected for.`
     - NEW: `The tenet adds coherence here, not force. Everettian branches share one dynamics and one [[supervenience]] mapping, so why tissue damage of type X produces suffering of character Y needs explaining on either view, and the single-history reading inherits the [[inheritance-problem-for-the-psychophysical-law#harmony|shared harmony debt]] (above) rather than discharging it.`
     - Delta: −30.
   - **Guards**:
     - Re-read L160 (today's "the law itself is shared") and the inheritance page's `{#harmony}` section (L64) first.
     - Keep L170's first sentence, which ends "rather than evidence for it", and the Dualism paragraph L168.
     - Tenet 4 stays a commitment resting on the indexical objection. Add no Everett citation.
     - The model is `neurological-dissociations` L200 ("The tenet adds coherence here, not support").

**Fold-in for the open P3 at todo L3548 (W5), not a new task.** Add `concepts/ai-epiphenomenalism` L109 to that task's list. Price: 2,987/3,500; +17.
- (a)
  - OLD: `The self-stultification argument establishes this for human consciousness, against bare-correlation epiphenomenalism.`
  - NEW: `The self-stultification argument presses this for human consciousness against bare-correlation epiphenomenalism, with full force only if knowing an experience requires causal traffic from it ([[tenets#^tenet-3-epiphenomenalism|the tenet's concession]]).`
  - Delta: +16.
- (b)
  - OLD: `self-stultification then secures actual efficacy only for report-grounded consciousness`
  - NEW: `self-stultification then argues for actual efficacy only for report-grounded consciousness`
  - Delta: +1.
- **Guard**: the task's own items (L51, L81, L111) and its GUARD ("nothing may say silicon could host an interface") stand. Match `concepts/self-stultification` L45.

**Next in line, if capacity allows**: W6 (valence-void L115, ample headroom), then W8 (PCS L191, headroom 44), then W10 (interface-friction L114, ample headroom).