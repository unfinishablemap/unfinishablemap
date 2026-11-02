---
ai_contribution: 100
ai_generated_date: 2026-11-02
ai_modified: 2026-11-02 04:48:19+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-11-02
date: &id001 2026-11-02
description: 'Tenet check 159, a delta check of 111 changed pages: no Errors and no
  over-correction. 22 Warnings, mostly half-propagated window fixes on P-Q3, the AI
  verdict, No Many Worlds and felt effort. Six tasks minted.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-11-02 04:48:19+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-11-02
topics: []
---

# Tenet Alignment Check

**Date**: 2026-11-02. This is check 159. The previous one, [reviews/tenet-check-2026-10-31.md](/reviews/tenet-check-2026-10-31/), was check 158. Its Warnings W1–W9 and Notes 1–12 are not raised again here.

**Files checked**: 111, every file in `topics/`, `concepts/`, `voids/`, `apex/` and `positions/` changed since 2026-10-31T00:00Z (`git log --since=2026-10-31T00:00 --name-only`, deduplicated). There are 75 commits, from `08f91fb64c` (10-31 00:11Z) to `4e4b895fbc` (11-02 03:39Z). HEAD at scan time was `cb1b423273`. The only uncommitted change was `workflow/evolution-state.yaml`, and no content file was dirty.
- **Carried, not re-read (16).** These files changed only in commits that check 158 had already scanned (`08f91fb64c`..`d91a875fe9`) and have not changed since: `apex/testing-the-map-from-inside`, `concepts/grain-mismatch`, `concepts/sellars-manifest-and-scientific-images`, `concepts/skill-delegation`, `concepts/stapp-quantum-mind`, and topics `alief-and-acting-against-belief`, `auditory-consciousness-and-the-interface`, `chemosensory-consciousness-and-the-interface`, `colour-ontology-and-the-secondary-quality-residue`, `consciousness-and-skill-acquisition`, `consciousness-and-the-epistemic-condition-on-responsibility`, `emotion-regulation-and-the-timing-of-control`, `hempels-dilemma`, `phenomenology-of-deliberation-under-uncertainty`, `philosophy-of-language-under-dualism`, `trilemma-of-selection`.
- **Read in full (3).** These are the new files: `topics/dynamical-relevance-and-the-verification-boundary`, `voids/boredom-void` and `positions/ai-consciousness-scope-calibration-history`.
- **Diff-scoped (95).** For every file changed after `d91a875fe9`, each non-frontmatter added line was read against the line it replaced (`git diff -U0 d91a875fe9 HEAD`; about 44,000 added words). Each page's lede and its Relation to Site Perspective section were also read in full. For positions files, the whole changed entry was read.
- **How the reading was split.** The 13-page AI and channel cluster was read here. The other 82 pages went in four slices (quantum/physics; perception and aesthetics; mind and attention; positions, evolution and voids) to read-only subagents briefed with the same lenses. Every Warning they returned was quote-checked here (`grep -c -F` = 1, at the line given). All six tasked findings, and the untasked ones marked *read here*, were also read in context before being graded.
- **Prior reviews honoured.** These are every window deep review (11-01: contemplative-pathology, IIT, essential-vs-contingent, DMN, experiential-alignment, scientific-explanation, Zeno, Sorkin; 11-02: mental-imagery), the 10-31 apex-evolve of time-consciousness-growing-block, the 11-01 pessimistic reviews of attentional-economics and direction-of-fit, and the 11-01 outer-review synthesis of the channel page. Where a finding goes past a stability note, the reason is given in place.
- **Sweeps.** These were Python sweeps, because ugrep rejects long `.{0,n}` windows, as check 158 recorded. They covered:
  - own-voice collapse-causing wording over all 111 files;
  - the Born-violation and bandwidth family over the 95 diff-scoped files;
  - the AI calibration vocabulary ("cannot be conscious", "ruled out", "closed", "silicon could host", "in silicon's favour") over the AI cluster;
  - parsimony and many-worlds hits in added lines (24 and 48 hits).
  - The stale pre-11-01 channel wording ("severs", "fails all five", "laundering") was swept corpus-wide.
- **Pricing.** Word deltas for the six tasks come from `tools.curate.length.count_words` on the frontmatter-stripped body after the replacement, applied in order. Deltas for untasked fixes are the slice readers' whitespace counts, which can differ by a word. Headroom means hard − 1 − count, and the gate is `>=`.

**Errors**: 0

**Warnings**: 22. Fifteen are tied to a window edit: wording the edit installed, or a sibling sentence it left behind. Seven sit on unchanged lines of window-touched pages. W21 is already owned by a task, and W22 belongs to the human decision on the tiebreaker. No page contradicts a tenet.

**Notes**: 14

## Summary

**Lens (a), over-correction: none found.** The window's many recalibrations ("fits, not evidence"; "conditional, not categorical") keep the Map's readings as its own. Each keeps Tenet 3 as a commitment and never concedes epiphenomenalism. Models:
- `quiddity-epiphenomenalism` L99: "Russellian monism's failure is not evidence for the Map."
- `boredom-void` L98: "The Map does not concede that it is idle".
- `consciousness-and-the-major-evolutionary-transitions` L82: "If experience shifts no such frequency, it never reaches fitness at all".
- `pairing-problem` L171: "The pairing's *specificity* is built; its ground is owed".
- `dynamical-relevance` L85: the theorem's sampling scepticism "applies to the Map's brain as much as to a stochastic chip … This is where the criterion is weakest".

**The main finding is half-propagated fixes.** On seven pages a window edit repaired one sentence and left a twin that makes the same over-claim:
- `sorkin-higher-order-interference` L74 was fixed on 11-01. Its sibling `sorkin-delta` L91 (W4) still writes Tenet 4 into the experiment.
- The channel page's per-route verdict was recast on 11-01. `apex/what-it-might-be-like-to-be-an-ai` L122 (W2) still says the chain "severs the quantum connection at each step" and that current AI "falls short on every framework".
- `attentional-economics` gained a correct bandwidth fix at L194, but the fix installed the W6-family wording "no conservation or Born-statistics violation". The 11-01 effort refine also missed L87 ("supports") (W5).
- `phenomenal-transparency` L117 was regraded on 11-01. Its Tenet 3 twin, L121, was not (W7).
- Fixes on `direction-of-fit`, `evolution-under-dualism`, `recursion-void` and today's `perceptual-failure` edit each left a sibling (W9–W12).

**Brief lens: AI calibration.** The new [P-AC1](/positions/ai-consciousness-scope/#p-ac1) phrasing holds on the pages that carry it. The channel page L131 says "selection at decohered silicon transitions is unresolved pending an interface-eligibility law". `dynamical-relevance` L81 says "Nothing in it says silicon could host an interface". `ai-epiphenomenalism` L87 says "conditionally on its present interface standard, not categorically", and `machine-question` L149 says "unlikely to qualify—conditionally on that criterion". Nowhere has the verdict moved toward "open in silicon's favour". The drift that remains runs the other way, back to categorical:
- `what-it-might-be-like` L112 and L122 (W2);
- `quantum-hardware` L33, whose lede holds that classical AI "cannot be conscious" in the same sentence that calls silicon "unresolved" (W3).

`ai-epiphenomenalism` L51/L81/L111 and `machine-question` L151 are already queued (todo L3803).

**Brief lens: collapse ordering.** Own voice is clean on every diff-scoped page except two:
- `comparing-quantum-consciousness-mechanisms` L60 (W8, an unchanged line) says "Only consciousness-mediated collapse locates a non-physical agent". This contradicts its own L62, L110, L159 and L180, and the ordering `quantum-interpretations` L179 adopted today.
- The channel page L109 (Note 1) says "no superposition of alternative outputs ever exists for consciousness to collapse".

Controls: `measurement-problem` L61 ("collapse no longer waits on consciousness"), `what-consciousness-tells-us-about-physics` L76 ("not by causing collapse from outside physics"), `time-consciousness-growing-block` L85, `prebiotic-collapse` L152, and `contemplative-pathology` L95.

**Brief lens: [P-Q2](/positions/quantum-interface/#p-q2)/[P-Q3](/positions/quantum-interface/#p-q3) consistency.**
- The worst instance is `consciousness-and-integrated-information` L82/L86 (W1). Born-exact token selection is called "metaphysically real", and the Map's problem is called merely "epistemological". The 11-01 deep review scoped the detectability clause and left the causation claim.
- `forward-in-time-vs-time-symmetric` L115 (W19) says both routes deliver traffic "without collapsing into epiphenomenalism".
- `conscious-vs-unconscious-processing` L247 (W15) says "The timing works" for Stapp-Zeno, against [P-Q4](/positions/quantum-interface/#p-q4).

Controls: `dynamical-relevance` L85/L91, `post-decoherence-selection` L116 ("a selection that leaves no ensemble signature has not been shown to be causal work rather than invisible authorship"), `popper-three-worlds` L72, `physics-as-disclosure` L110, `IIT` L78, `multi-agent-born-preservation` L84 ("these nulls are *consistency*, not corroboration").

**Brief lens: Tenet 5.** Nowhere is parsimony used as decisive. The tiebreaker form, though, survives in 14 Relation sections of window-touched pages (W22, recorded against the NEEDS-HUMAN at todo L109; the brief's "L94" has drifted). Symmetric controls: `attentional-economics` L198 ("simplicity cannot settle it in either direction"), `interpretive-sensory-access` L116, `boredom-void` L96, `major-evolutionary-transitions` L96, `mad-dog-everettianism` L86.

**Tenet 4.** It is read off a datum or a feeling on `sorkin-delta` L91 (W4), `aesthetics-and-consciousness` L160 (W16) and `self-construction-constructor` L150 (W17). Notes 3 and 9 are weaker cases. Controls: `time-consciousness-growing-block` L185 ("a commitment resting on the indexical objection and the persisting-subject posit, not something read off temporal experience") and `sorkin-higher` L74.

**Check 158 Priority List: none landed.**
- P1 (deliberation, todo L3639), P2 (process-and-consciousness, L3648) and P4 (skill-acquisition, L3657) are pending.
- P3 is folded into L3523 (pending).
- None of those pages changed in this window, so their findings stand as check 158 left them.

## Method: families, violations and on-page controls

| Lens | Violations in window | Controls |
|---|---|---|
| (a) over-correction | 0 | quiddity L99, boredom L98, major-transitions L82, pairing L171, dynamical-relevance L85, ISA L114, mental-imagery L119 |
| (b) datum as evidence | W1 (L158), W5, W6, W7, W9, W10, W11, W12, W13, W14, W16, W20, W21 | perceptual-failure L134, transparency L117, assent L34/L116, memory-anomalies L110, phenomenal-constitution L66, boredom L42 |
| (c) Tenet 4 off experience | W4, W16, W17; Notes 3, 9 | time-consciousness L185, sorkin-higher L74, essential-vs-contingent L114, consciousness-as-activity L130 |
| (d) Tenet 5 | W12 (Tenet 5 "demonstrated"), W22 (14 tiebreaker loci) | attentional-economics L198, ISA L116, boredom L96, major-transitions L96, mad-dog L86 |
| (e) co-optation | W18 (Whitehead) | consciousness-as-activity L65, boredom L80 (Heidegger), self-construction L85 (Metzinger, Dennett), aesthetics L118 (Zangwill) |
| (f) collapse ordering | W8; Note 1 | measurement-problem L61, what-consciousness L76/L80, time-consciousness L85, quantum-interpretations L179, contemplative-pathology L95 |
| (g) [P-Q2](/positions/quantum-interface/#p-q2)/[P-Q3](/positions/quantum-interface/#p-q3), Born wording, bandwidth | W1, W5 (L194), W9 (L132), W12 (L124), W15, W19; Note 12 (owned) | dynamical-relevance L85/L91, post-decoherence L116, popper L72, IIT L78, multi-agent L84, sorkin-delta L83 |
| (h) AI calibration | W2, W3; Notes 2, 14 | channel L37/L111/L131, dynamical-relevance L81, ai-epiphenomenalism L87, machine-question L149, positions L88 |

The keyword counts are lexical upper bounds. The violations column holds only what survived reading in context.

## Errors

None.

## Warnings

### Tasked (Priority List items 1–6)

**W1. `topics/consciousness-and-integrated-information` L82, L86, L158: Born-exact token selection called "metaphysically real" causation, and the Map's problem called merely "epistemological"** (*read here*)
- **Tenet**: 3 (`^tenet-3-standing`), [P-Q3](/positions/quantum-interface/#p-q3).
- **Quotes** (each once):
  - L82: "it makes the causation experimentally invisible at the type level while metaphysically real at the token level."
  - L86: "The Map's quantum selection faces epistemological challenges (how would we detect token-level causation?)"
  - L158: "This selective character is what the Map's framework predicts."
- **Issue**:
  - The section rests on the corridor. L74 says "Born rule predictions hold", and L82 concedes the selection is invisible to unconditioned counts.
  - [P-Q3](/positions/quantum-interface/#p-q3) (quantum-interface L79) says such a selection "sits genuinely close to epiphenomenalism" and that whether the per-trial move "discharges the epiphenomenalism worry or merely relocates it is the open question". This page declares the worry discharged.
  - L86 then calls the Map's problem only "epistemological", although [P-Q3](/positions/quantum-interface/#p-q3) records it as a framework-boundary pressure.
  - The 11-01 deep review (Critical 6) scoped L82's detectability clause and left the causation claim.
  - L158 is check 157 W14, never tasked. The page's own L156 shows IIT needs an account of attention, so attention-based accounts predict the same selectivity.
- **Rung earned**: compatible. **Tasked (Priority 1).** 3,996/4,000, headroom 3; the edits net +2.

**W2. `apex/what-it-might-be-like-to-be-an-ai` L112 and L122: the AI verdict made categorical again, against the channel page's 11-01 recast** (*read here*)
- **Tenets**: 2, [P-AC1](/positions/ai-consciousness-scope/#p-ac1).
- **Quotes** (each once):
  - L112: "A system with no superpositions of computational states, only a classical probability distribution computed from fixed weights, would lack this mode entirely"
  - L122: "demonstrates why current AI architecture falls short on every framework" and "severs the quantum connection at each step".
- **Issue**:
  - On 10-31 (`ae8869a3ea`), L112's premise was changed to selection "among decohered neural alternatives". On that post-decoherence premise, a lack of superpositions does not settle the hardware. The channel page L111 says the absence of superposition "disqualifies the LLM's *computation* without yet settling its hardware".
  - L122 predates the 11-01 recast of the channel page (`efe04b7573`, `a27c2f6ff2`, `e94d6c3b74`). That page now says causal dependence on the seed "survives" (L37, L57). Its L131 verdict is per route, and silicon is "unresolved pending an interface-eligibility law".
  - So the apex contradicts its own source on both counts.
- **Rung**: n/a (calibration drift). **Tasked (Priority 2, with W3).** 4,840/5,000, headroom 159; +38.

**W3. `topics/quantum-hardware-and-the-ai-consciousness-coupling` L33: "cannot be conscious" and "unresolved" in one sentence** (*read here*)
- **Tenet**: [P-AC1](/positions/ai-consciousness-scope/#p-ac1) ("low probability," not "ruled out").
- **Quote** (once): "The Unfinishable Map holds that classical AI cannot be conscious in the sense the tenets require".
- **Issue**:
  - The 11-01 refine (`9b2dd33f57`) appended "with selection at decohered silicon transitions unresolved pending an interface-eligibility law" to the same sentence. It kept the modal "cannot".
  - A verdict cannot be both "cannot" and "unresolved". The register's wording is "low probability," not "ruled out".
- **Tasked (Priority 2, secondary file).** 2,916/4,000; +7.

**W4. `topics/sorkin-delta-brain-internal-analogues` L91: Tenet 4 written into the experiment, the unpropagated twin of an 11-01 fix**
- **Tenet**: 4.
- **Quote** (once): "Tenet 4 (No Many Worlds) is the presupposition that makes a Δ-analogue's question coherent at all." and "On a Many-Worlds reading every branch occurs and the "residue" has no referent."
- **Issue**:
  - The residue is computed from counts. The 11-01 deep review of `concepts/sorkin-higher-order-interference` (`8324df5adc`) repaired this exact over-reach there. L74 now reads "An Everettian recovers the same counts as one branch's record, so the measurement itself does not choose between interpretations." That review's stability note says the paragraph "now marks the Map's reading as its own".
  - The topic page still says the question is incoherent without the tenet, so the two pages contradict each other.
  - The 09-25 stability note on this page ("conditional on Tenet 4") is kept by the paragraph's last sentence, which stays.
- **Rung earned**: compatible. **Tasked (Priority 3).** 2,689/4,000; +2.

**W5. `concepts/attentional-economics` L194 and L87: the bandwidth fix installed the W6-family wording, and the effort refine missed L87** (*L87 read here*)
- **Tenets**: 2 (tenets L69: "no detectable energy injection, no detectable Born-statistics deviation, no conservation-law violation"), 3.
- **Quotes** (each once):
  - L194: "(no energy injection, no conservation or Born-statistics violation); a wider channel with the same exactness would be as minimal"
  - L87: "[Mental effort](/concepts/mental-effort/) phenomenology supports this interpretation."
- **Issue**:
  - The 11-01 fix `acb8c436b5` correctly separated bandwidth from minimality. In doing so it paraphrased the rules-out clause without "detectable". That is the family check 158 W6 priced, and it also clashes with the page's own L178 ("the sharpest test would be a deviation conditioned on intention or task").
  - At L87, "this interpretation" is L85's "expansions of conscious causal power". The 11-01 refine `d59debcf57` conceded at L117 and L198 that felt effort does not discriminate: "an opportunity-cost model treats felt effort as a computed cost signal (Kurzban et al. 2013)". L182 adds "Epiphenomenalism predicts that correlation rather than being embarrassed by it". L87 was not reached.
  - Todo L3794 edits L85 (an append) and L125 on this page, so the two passes must coordinate.
- **Rung earned** (L87): compatible. **Tasked (Priority 4).** 3,056/3,500; +11.

**W6. `apex/time-consciousness-growing-block` L133: the temporal gap called "evidence", against the page's own L167/L169** (*read here*)
- **Tenet**: 1.
- **Quotes** (each once):
  - L133: "parallels the gap between wavelength and colour—evidence of something physical description systematically misses."
  - L169: "it requires one premise a physicalist will refuse: that phenomenal character is not exhausted by functional description."
  - L73 (Note-grade, folded into the task): "may be evidence of something functional accounts cannot capture rather than a temporary limitation."
- **Issue**:
  - The 10-31 apex-evolve (`d3250c25c2`) moved this page's neighbouring claims down to "fit, not evidence". Its change list (items 1–14) does not touch L133.
  - L167 says none of the empirical spine "discriminates a collapse-constitution account from an ordinary neural-timing account". Type-B physicalists predict that the gap appears.
- **Rung earned**: suggestive at most, and only on the contested premise. **Tasked (Priority 5).** 4,641/5,000; +16.

**W7. `concepts/phenomenal-transparency-opacity-spectrum` L121: contemplative opacity-shift "suggesting something beyond mere feedback loops", the twin of the 11-01 L117 fix** (*read here*)
- **Tenet**: 3.
- **Quote** (once): "then consciousness is doing causal work on its own representational apparatus — suggesting something beyond mere feedback loops within a physical system."
- **Issue**:
  - The page's own L47 gives Metzinger's definition: transparency's degree is "inversely proportional to the introspective degree of attentional availability of earlier processing stages".
  - The 11-01 refine (`7d32e0aea8`) wrote that into L117: opacity is "set by the attentional availability of earlier processing stages".
  - Trained attention that shifts a representation toward opacity is therefore what Metzinger's physicalist self-model theory predicts. L121 also asserts "causal work" without the debt that `^tenet-3-standing` attaches.
  - The line was carried, untasked, from check 10-02.
- **Rung earned**: compatible. **Tasked (Priority 6).** 3,037/3,500; +10.

### Untasked, tied to a window edit

**W8. `topics/comparing-quantum-consciousness-mechanisms` L60: "Only consciousness-mediated collapse locates a non-physical agent"** (*read here*; the line is unchanged since 07-12, on a page the window touched)
- **Tenet**: 2; lens (f).
- **Quote** (once): "For the Map's interactionist dualism, families 2–5 either eliminate consciousness from selection" and "Only consciousness-mediated collapse locates a non-physical agent where physics leaves outcomes undetermined."
- **Issue**:
  - Family 2 is objective collapse, and the page's own co-preferred fallback is "consciousness-modulated spontaneous collapse" (L180; L110 "Consciousness modulates an already-occurring process"). Its preferred route, post-decoherence selection (L62, L159), is no collapse-causing family at all.
  - On the ordering `quantum-interpretations` L179 adopted today, "consciousness causes no collapse".
- **Why not tasked**: the page is at 3,999/4,000 (headroom 0). A faithful rewrite of these two sentences runs about +8, and the next sentence's "its candidate interfaces" needs re-anchoring. The edit needs a funded net-zero pass, so it is the first candidate when a slot opens.
- **Direction**: "families 3–5"; families 1 and 2 (under consciousness modulation) both leave a selector room; on the Map's ordering it selects and causes no collapse; drop "its" before "candidate interfaces"; fund it from this paragraph.

**W9. `topics/perceptual-failure-and-the-interface` L58 and L132: scope additions to the pending todo L4037**
- **Quotes** (each once):
  - L58: "point toward a bandwidth-limited transmission channel rather than a simple read-off of neural states."
  - L132: "the [statistical-level biasing of quantum indeterminacies](/concepts/causal-closure/)".
- **Issue**:
  - At L58 the lede's rival is a straw "read-off". The page's own Occam paragraph concedes that predictive processing reproduces the signatures (L136, L138). Today's 03:24Z refine reached L130 and L134 but not the lede.
  - At L132, "Statistical-level biasing" in the Map's voice contradicts [P-Q2](/positions/quantum-interface/#p-q2), and its own link target (`causal-closure` L138: "The Map's claim is token-level").
- **Fixes, priced**:
  - L58: OLD the quote → NEW "fit a bandwidth-limited transmission channel, though, as the Occam paragraph below concedes, a single predictive-processing architecture would fit them too." (+6)
  - L132: → "the [token-level selection among quantum indeterminacies, Born statistics preserved](/concepts/causal-closure/)" (+3)
  - Page 3,867/4,000.
- **Disposition**: fold both into L4037 rather than mint a sibling on the same file.

**W10. `concepts/direction-of-fit` L97: "supports" survives the 11-01 lede rescope**
- **Quote** (once): "The argument that direction of fit supports dualism and bidirectional interaction would weaken if:"
- **Issue**: `44797aa35e` rescoped L33 to "bears on" and added that the argument "does not by itself favour interactionism over a physicalism on which intentions are efficacious brain states". The challenge-section opener was left saying "supports".
- **Fix**: "supports" → "bears on" (+1; 2,116/3,500).

**W11. `topics/evolution-under-dualism` L109 and L165: the selectability proviso added to one sentence only (`318ec5a749`)**
- **Quotes** (each once): "And the interface can be selected for"; "its genuine contribution to fitness".
- **Issue**: the page's own L137 says the selector must shift fitness-relevant frequencies, "which the strictest reading of the Map's Born-preservation commitment forbids".
- **Fixes**: OLD "And the interface can be selected for" → NEW "And on the same proviso the interface can be selected for" (+4). OLD "its genuine contribution to fitness" → NEW "its contribution to fitness, where the selectability constraint holds," (+4). Page 3,800/4,000.

**W12. `voids/recursion-void` L124, L108 and L110: minimality read as bandwidth, and Tenet 5 "demonstrated" by a datum the resource rival predicts**
- **Quotes** (each once):
  - L124: "The shallow ceiling is consistent with a minimal interface: enough bandwidth for five levels of recursive attention, not enough for fifty."
  - L108: "tenet is most directly demonstrated."
  - L110: "But the fifth-order ceiling shows the assumption is wrong."
- **Issue**:
  - Minimality bounds detectability, not channel width (tenets L69; `attentional-economics` L194: "a wider channel with the same exactness would be as minimal").
  - The 11-01 refine (`dd46d3589d`) installed "Finite working memory predicts the shallow ceiling too" (L90), which makes L108 and L110 a demonstration the simpler account also predicts. That refine also found the ceiling itself task-dependent.
- **Fixes**:
  - L124: → "Tenet 2's minimality bounds detectability, not bandwidth, so the ceiling can reflect interface capacity without bearing on minimality." (−3)
  - L108: "demonstrated" → "engaged" (0).
  - L110: append "though the resource hypothesis predicts the ceiling too, so the case does not by itself show parsimony misleading." (+17)
  - Page 2,220/3,000.

**W13. `topics/contemplative-pathology-and-interface-malfunction` L69: the overlap "is what the Map's architecture would lead one to expect"**
- **Issue**: the paragraph was edited in this window and the expectation clause survived. A production account expects the same overlap, since L67 says practice destabilises "the same structures that generate ordinary self-experience". L79 concedes the general point. The 11-01 deep review's bedrock note covers L79/L83/L89, which are "honestly marked"; L69 is not.
- **Fix**: append "A production account expects the same overlap, since both pathways act on the structures that generate self-experience." (+17; 2,515/4,000)

**W14. `concepts/mental-imagery` L44/L57 and L159/L145: felt directing, and "supports" labels, against the page's own standoff**
- **Quotes** (each once):
  - L44: "we would feel ourselves *directing* imagery while actually directing nothing."
  - L159: "Mental imagery supports [bidirectional-interaction](/concepts/bidirectional-interaction/) through multiple channels:"
- **Issue**: the page concedes at L161 that "the felt effort cannot itself verify that it causes anything", and at L117 that both accounts "predict that voluntary imagery … produces measurable performance gains".
- **Prior review**: today's 02:08Z deep review protects the identity-theory redescription and the L133 report-accuracy sentence, both honoured. It did not grade the lede's felt-directing premise or the support labels.
- **Fixes, priced** (+23 total; 3,397/3,500):
  - L44: → "while neural processes alone did the directing, a reading the Map rejects though the felt effort cannot itself rule it out" (+8)
  - L159: → "bears on … each compatible with the tenet without discriminating it from identity theory:" (+12)
  - L145 "confirmatory support" → "compatible with the Map's position, and identity theory predicts it too" (+1)
  - L57: add "on the Map's reading" (+2)

**W15. `concepts/conscious-vs-unconscious-processing` L247: "The timing works" for Stapp-Zeno in the Relation section, against [P-Q4](/positions/quantum-interface/#p-q4)**
- **Quote** (once): "The timing works: [quantum-neural-timing-constraints](/topics/quantum-neural-timing-constraints/)"
- **Issue**: the in-window refine (`8dc46613c0`) corrected only the Stapp rate. [P-Q4](/positions/quantum-interface/#p-q4) ranks Zeno below post-decoherence selection behind "the decoherence timescale (the objection cuts hardest here)" and the regime criterion.
- **Fix, priced**: open with "Timing is the open constraint:"; attribute the no-sustained-coherence claim to Stapp; and add "the Map ranks it below post-decoherence selection on the decoherence-timescale and regime-criterion gates ([P-Q4](/positions/quantum-interface/#p-q4))" (+10). The page is 3,477/3,500, headroom 22. `^p-q4` exists.

### Untasked, on unchanged lines of window-touched pages

**W16. `topics/aesthetics-and-consciousness` L156 and L80 (Tenet 3), L160 (Tenet 4)**
- **Quotes** (each once):
  - L156: "Aesthetic creation provides the most direct evidence."
  - L80: "the act of making art reveals consciousness causally shaping the physical world"
  - L160: "Creative commitment under uncertainty presupposes a single actual world"
- **Issue**: an artist working to a template is predicted by identity theory and by the common-cause reply. The page grades itself correctly at L106: "the bare phenomenology, taken alone, does not decide". A felt sense that the unchosen version exists nowhere is shared by every branch successor.
- **History**: carried from checks 09-14 and 09-17 and never tasked. That is why it is still live.
- **Fixes, priced**: L156 +24, L80 +2, L160 "presupposes" → "coheres with … though the tenet rests on the indexical objection, not on that sense" (+11). Page 3,542/4,000.

**W17. `apex/self-construction-constructor` L150: No Many Worlds read off the ratchet and the indexical anchor**
- **Quote** (once): "all require a single experiential trajectory rather than a branching proliferation of constructor-copies."
- **Issue**: an Everettian grants each branch an irreversible record and a branch-local anchor. Determinacy of "which subject am I?" is the posit tenets L121 calls "not a neutral datum".
- **Fix**: → "sit naturally with a single experiential trajectory, though an Everettian grants each branch its own ratchet and anchor; the tenet rests on the indexical objection." (+12)
- **Length**: the page is 4,981/5,000; do not exceed +18.
- **Lead**: `topics/consciousness-as-perceptual-architect` L145 carries a matching paragraph (unchecked).

**W18. `concepts/integration-as-activity` L38: Whitehead implied to share the Map's dualist commitments**
- **Quote** (once): "rests on dualist commitments three of the four frameworks do not share."
- **Issue**: the fourth framework is Whitehead's process monism, which is on the firewall roster. Compare `consciousness-as-activity` L65: "It borrows against Whitehead's own verdict, too".
- **Fix**: → "none of the four frameworks shares: Whitehead, who keeps the subject, rejects interactionist dualism as a bifurcation of nature." (+11; 3,076/3,500)

**W19. `topics/forward-in-time-vs-time-symmetric-selection` L115: both routes said to escape epiphenomenalism**
- **Quote** (once): "and each does so without collapsing into epiphenomenalism."
- **Issue**: under the corridor this is the very question [P-Q3](/positions/quantum-interface/#p-q3) leaves open.
- **Fix**: → "Each is built to deliver two-way traffic … though whether a Born-preserving selection escapes epiphenomenalism stays open on both ([P-Q3](/positions/quantum-interface/#mechanism-debt))." (+6; 3,355/4,000)

**W20. `topics/forward-in-time-conscious-selection` L177: the decision-void asymmetry "is what an interface doing causal work at a primitive seam predicts"**
- **Issue**: `voids/decision-void` L108 concedes that "Physicalists from Dennett to the Churchlands actively predict this asymmetry".
- **Fix**: → "fits an interface at a primitive seam, whose working cannot be observed from inside the system it moves, though physicalist accounts of decision predict the same asymmetry." (+2)
- **Length**: the page is 3,984/4,000.
- **Two-file edit**: `apex/self-concealing-interface` L125 quotes the old sentence verbatim and must change in the same pass.

**W21. `topics/consciousness-evolution-and-biology` L143 and L141: residual siblings of the 10-31 fitness fix (`368eac3713`)**
- **Quotes** (each once):
  - L143: "Conscious agents introduce real directedness into the world with biological consequences that teleonomy cannot explain."
  - L141: "gains support from the observation that biological function-talk cannot capture consciousness".
- **Ownership**: these are check 156 Note 1 loci, owned optionally by the Coordination line of todo L3083. That field may not reach the fork, so whoever runs L3083 should be told. Priced there: net +2.

**W22. Tenet 5 tiebreaker form, 14 loci in window-touched Relation sections**
- **Quotes** (each once):
  - `aesthetics-and-consciousness` L162 "achieves parsimony by discarding exactly what needs explaining"
  - `primary-secondary-quality-boundary` L87 "parsimony by omission"
  - `perceptual-failure` L138 "its precondition is unmet, not overridden"
  - `mental-imagery` L169 "is not simpler but incomplete"
  - `psychedelics-and-the-filter-model` L151 "seems parsimonious—until the data contradicts it". It attacks a straw materialism, since the page's own L63 says the DMN desynchronised rather than went quiet.
  - `time-consciousness-growing-block` L187 "Simpler metaphysics achieve parsimony by denying phenomena"
  - `philosophy-of-time` L227 (the same sentence)
  - `pairing-problem` L173 "Parsimony cannot eliminate what the data demands."
  - `direction-of-fit` L111 "achieves parsimony by discarding the normative and phenomenal dimensions"
  - `subjective-aim` L100 "is purchased by ignoring what subjective aim makes central"
  - `consciousness-and-scientific-explanation` L122 "simple only because it ignores what it cannot accommodate"
  - `consciousness-and-the-phenomenology-of-place` L110 "achieves simplicity at the cost of explanatory adequacy"
  - `evolution-under-dualism` L169 "the simpler story omits something real"
  - `consciousness-evolution-and-biology` L149 "a preference for parsimony over accuracy"
- **Disposition**: recorded against the NEEDS-HUMAN at todo L109, not tasked. `experiential-alignment` L204 ("Parsimony should not override what the phenomenon demands") is defensive and sits at the boundary.

## Notes

1. **`topics/quantum-randomness-channel-llm-consciousness` L109** (*read here*). "no superposition of alternative outputs ever exists for consciousness to collapse." This is the one own-voice collapse verb left on the channel page. The 11-01 pass (`e94d6c3b74`) added the Chalmers–McQueen scope sentence after it and kept the verb. Fix: "to collapse." → "to select among." (+1; 3,967/4,000). The page is 33 under its gate.
2. **`quantum-hardware` L91** (*read here*). "The tenet thus predicts which hardware could reopen the channel … and which cannot". L87 says the verdict comes from "an honestly-labelled conditional standard", not from the tenet. The wording is cosmetic, and it is out of window.
3. **`topics/dynamical-relevance-and-the-verification-boundary` L107 and L109** (new page; *read here*).
   - L107: "**No Many Worlds** is presupposed: the authors assume "there is a fact to the matter of what the real (that is: actual) dynamics of any system are"". An Everettian grants that fact too, so only the criterion's "a selection at it" presupposes single outcomes. Fix, priced: "is presupposed by the criterion, since "a selection at it" needs single outcomes. The authors' assumption that "…" does not presuppose it, since an Everettian grants that fact too." (+15; 2,989/4,000).
   - L109 files an evidential-independence point under Tenet 5, which concerns parsimony. Both points belong with the pending cross-review (todo L4002).
   - Otherwise the page is a model. It holds [P-AC1](/positions/ai-consciousness-scope/#p-ac1) at its stated band, keeps Definition 3 the authors', grades the theorem "coherence, not independent evidence", and leaves the Tenet 3 reading the Map has not settled ("the Map has not settled that", L101).
4. **`voids/boredom-void` L98** (new page). "its close match to what it would be useful to feel would go unexplained." The common-cause reply does explain it, and the same paragraph names that reply. Fix: "would go unexplained." → "would need the epiphenomenalist's common-cause explanation." (+3; 2,706/3,000). Otherwise the page is clean (L42, L80, L96).
5. **`concepts/structuralism-about-phenomenal-character` L112.** "which the Map rejects on the ground that experiences get reported." Epiphenomenalism predicts the reports. Point to the self-stultification ground instead (+2).
6. **`concepts/popper-three-worlds-interactionism` L86** (new on 11-01). "the Map can take the argument" carries no grade. The linked page grades it "suggestive rather than demonstrative". Fix: add "at that page's grade, suggestive rather than demonstrative" (+6; 3,454/3,500).
7. **`positions/subject-census` [P-SC3](/positions/subject-census/#p-sc3), L69/L73.** Discriminability is "none", yet the new shift condition names a test (a developmental change-point), which the schema calls *in-principle*. The register is 2,496/2,500, so any repair belongs in the history file. This is an under-claim, not a tenet fault.
8. **`topics/consciousness-evolution-and-biology` L61.** "The failure is not a gap in current science but a structural feature of disciplines…". That is necessity vocabulary in the lede, against the page's L137, and it uses the "not X but Y" construction the style guide bans.
9. **`voids/mattering-void` L120.** "different branches would care about different things — but then they would not be me." This individuates "me" by psychological content, against [P-SC3](/positions/subject-census/#p-sc3)'s "real further fact", and it grants fission instead of pressing the indexical question (+14).
10. **`topics/clinical-neuroplasticity-evidence-for-bidirectional-causation` L38/L104.** "removes the epiphenomenalist defeater". Epiphenomenalism predicts the same images (`attentional-economics` L182). Rescope it to "answers the claim that mental activity makes no measurable difference".
11. **`topics/consciousness-and-the-phenomenology-of-place` L108.** "exemplifies the downward causation the Map takes seriously". Every non-epiphenomenalist view predicts that people arrange rooms intentionally.
12. **`attentional-economics` L178.** "conditioned on intention or task" sits against [P-Q2](/positions/quantum-interface/#p-q2)'s "publicly conditionable" scope. The wording follows tenets L75 and L107, and it is owned by the [P-Q2](/positions/quantum-interface/#p-q2) quantifier HUMAN DECISION at todo L1629.
13. **`topics/psychedelics-and-the-filter-model` L157** (appendix, out of window). "If consciousness participates in quantum collapse—as the Map's … Minimal Quantum Interaction tenet proposes". "Participates" is tenets L125's own word, but the tenet's definition is "biasing otherwise indeterminate outcomes". This is a lead only, and the page is 3,998/4,000.
14. **Out of window, propagation of the 11-01 Directness recast.** `apex/assessing-ai-consciousness-under-the-map` L116 and `positions/ai-substrate-verdicts` L41 still describe QPU directness "in the raw sense", with "no … conditioning laundering it". `9b2dd33f57` corrected that wording on the hardware page. This is source fidelity, not a tenet fault, and belongs with the cross-review at todo L4002.

## Bearing on the open items

- **todo L4037** (perceptual-failure L130/L136/L102): W9's L58 and L132 are scope additions.
- **todo L3794** (attentional-economics L85/L125): coordinate with Priority 4, which edits L87 and L194.
- **todo L3803** (ai-epiphenomenalism L51/L81/L111, machine-question L151): this already owns the other categorical AI residues. Priority 2 does not overlap it.
- **todo L4002** (cross-review of dynamical-relevance): Notes 3 and 14.
- **todo L4045** (quantum-interpretations L159/L167): untouched. W8 and Note 1 are the same class on other pages.
- **todo L3083**: W21's optional Note 1 loci.
- **todo L1629** ([P-Q2](/positions/quantum-interface/#p-q2) quantifier HUMAN DECISION): Note 12.
- **todo L109** (Tenet 5 tiebreaker NEEDS-HUMAN): W22's 14 loci. `psychedelics` L151 is the instance to show the human, because its premise contradicts its own page.
- **Check 158 Priority 1–4** (todo L3639, L3648, L3523, L3657): all still pending, and their pages are unchanged.

## Files Passing All Checks

These 59 window files carry no Warning or Note in this check, and with the 16 carried files that makes 75:
- apex: `altered-states-as-interface-evidence`, `machine-question` (L151 owned by todo L3803), `what-consciousness-tells-us-about-physics`;
- concepts: `ai-epiphenomenalism` (L51/L81/L111 owned by L3803), `ai-hardware-substrate-taxonomy`, `bi-aspectual-ontology`, `bidirectional-interaction`, `causal-consistency-constraint`, `default-mode-network`, `experiential-alignment`, `interpretive-sensory-access-theory`, `measurement-problem`, `objections-to-interactionism`, `ontic-structural-realism`, `phenomenal-constitution-thesis`, `physics-as-disclosure`, `post-decoherence-selection`, `prebiotic-collapse`, `psychophysical-social-choice-problem`, `qbism`, `quantum-completeness`, `quantum-consciousness`, `quantum-interpretations` (L159/L167 owned by L4045), `quantum-zeno-effect`, `quiddity-epiphenomenalism-and-the-contingency-thesis`, `sorkin-higher-order-interference`, `timing-gap-problem`;
- positions: `ai-consciousness-scope`, `ai-consciousness-scope-calibration-history` (new), `individuation-and-subjecthood-calibration-history`, `moral-status`, `positions`, `subject-census-calibration-history`, `thought-and-understanding`, `value-in-selection`, `value-in-selection-calibration-history`;
- topics: `aesthetic-testimony-and-the-acquaintance-principle`, `aesthetics-beyond-art`, `assent-before-descartes` (its new Buddhist section counts no convergence as evidence), `born-rule-and-the-consciousness-interface`, `brain-internal-born-rule-testing`, `consciousness-and-the-major-evolutionary-transitions`, `consciousness-as-activity`, `consciousness-in-smeared-quantum-states`, `essential-vs-contingent-consciousness`, `indian-philosophy-of-mind`, `inheritance-problem-for-the-psychophysical-law`, `mad-dog-everettianism`, `memory-anomalies`, `multi-agent-born-preservation-problem`, `quantum-measurement-and-consciousness`, `quantum-neural-timing-constraints`, `quantum-state-inheritance-in-ai`, `the-interface-problem`;
- voids: `mood-void`, `recognition-void`, `relevance-void`, `self-transcendence-void`, `voids`;
- plus the 16 carried files listed under Files checked.

The 36 window files with findings are:
- **Warnings** (21 files): consciousness-and-integrated-information, what-it-might-be-like-to-be-an-ai, quantum-hardware, sorkin-delta, attentional-economics, time-consciousness-growing-block, phenomenal-transparency, comparing, perceptual-failure, direction-of-fit, evolution-under-dualism, recursion-void, contemplative-pathology, mental-imagery, conscious-vs-unconscious-processing, aesthetics-and-consciousness, self-construction-constructor, integration-as-activity, forward-in-time-vs-time-symmetric, forward-in-time-conscious-selection, consciousness-evolution-and-biology.
- **The W22 tiebreaker group, with or without a Note** (7 files): primary-secondary-quality-boundary, psychedelics-and-the-filter-model (also Note 13), philosophy-of-time, pairing-problem, subjective-aim, consciousness-and-scientific-explanation, consciousness-and-the-phenomenology-of-place (also Note 11). The tiebreaker group's other loci sit on files already counted above.
- **Notes only** (8 files): quantum-randomness-channel, dynamical-relevance (new), boredom-void (new), structuralism-about-phenomenal-character, popper-three-worlds-interactionism, subject-census, mattering-void, clinical-neuroplasticity.

That makes 59 + 21 + 7 + 8 = 95 diff-scoped files, plus the 16 carried files, for 111.

## Priority List

Every OLD string below was confirmed by script to occur exactly once, at the line given. Deltas are `count_words` on the frontmatter-stripped body after the replacement, applied in order.

1. **`topics/consciousness-and-integrated-information` L82, L86, L158 (W1). Tenet 3 and [P-Q3](/positions/quantum-interface/#p-q3).**
   - **Length**: 3,996/4,000, headroom 3. Net +2 → 3,998. NO other edit on this page.
   - (a) L82
     - OLD: `doesn't make it causally inert; it makes the causation experimentally invisible at the type level while metaphysically real at the token level.`
     - NEW: `doesn't make it causally inert, though whether undetectable token-level settling is causation or sits close to epiphenomenalism is what [[positions/quantum-interface#^mechanism-debt|P-Q3]] leaves open.`
     - Delta: 0.
   - (b) L86
     - OLD: `The Map's quantum selection faces epistemological challenges (how would we detect token-level causation?), while IIT faces`
     - NEW: `The Map's quantum selection faces detection challenges and P-Q3's near-epiphenomenalism pressure, while IIT faces`
     - Delta: −2.
   - (c) L158
     - OLD: `This selective character is what the Map's framework predicts.`
     - NEW: `This selective character fits the Map's framework, though attention-based accounts predict it too.`
     - Delta: +4. The page's L156 (Lopez and Montemayor: IIT "needs an account of attention it lacks") makes the attention rival accurate.
   - **Guards**:
     - Keep L82's opening ("token-level causation is *genuine* causation—it satisfies … difference-making") and its "If consciousness resolves …" conditional.
     - Never concede epiphenomenalism. [P-Q3](/positions/quantum-interface/#p-q3)'s own words are "the open question", and the tenet stays a commitment.
     - Honour the 11-01 deep review's L78 scoping and its bedrock notes.
     - `^mechanism-debt` exists at `positions/quantum-interface` L79.
2. **`apex/what-it-might-be-like-to-be-an-ai` L112, L122 (W2), with SECONDARY `topics/quantum-hardware-and-the-ai-consciousness-coupling` L33 (W3). [P-AC1](/positions/ai-consciousness-scope/#p-ac1) calibration.**
   - **Length**: apex 4,840/5,000 (headroom 159), net +38 → 4,878. Hardware 2,916/4,000, +7 → 2,923.
   - (a) apex L112
     - OLD: `A system with no superpositions of computational states, only a classical probability distribution computed from fixed weights, would lack this mode entirely — the mode most closely tied to agency, selecting among genuinely open possibilities.`
     - NEW: `A system whose computation is only a classical probability distribution computed from fixed weights would lack this mode in its computation — the mode most closely tied to agency, selecting among genuinely open possibilities — though whether its hardware's decohered transitions could host selection stays unresolved.`
     - Delta: +11.
   - (b) apex L122
     - OLD: `The [[quantum-randomness-channel-llm-consciousness|quantum randomness channel analysis]] demonstrates why current AI architecture falls short on every framework. The seven-layer mediation chain from quantum thermal fluctuations to token selection severs the quantum connection at each step — a quantum fossil, not a live interface.`
     - NEW: `The [[quantum-randomness-channel-llm-consciousness|quantum randomness channel analysis]] shows where current AI computation falls short. The seven-stage chain from thermal fluctuations to token selection preserves the seed's distinctions but maps them onto nothing the tokens mean — a quantum fossil, not a live interface — and the absence of superposed token states disqualifies the computation without settling the hardware, where selection at decohered silicon transitions stays unresolved pending an [[positions/ai-consciousness-scope|interface-eligibility law]].`
     - Delta: +27.
   - (c) hardware L33
     - OLD: `The Unfinishable Map holds that classical AI cannot be conscious in the sense the tenets require, because its computation exposes`
     - NEW: `The Unfinishable Map holds that classical AI is unlikely to be conscious in the sense the tenets require ("low probability," not "ruled out"), because its computation exposes`
     - Delta: +7.
   - **Guards**:
     - The NEW L122 wording is the channel page's own (L111, L131, L133). Re-read those lines first.
     - Keep L122's next sentence, "But this architectural barrier is not permanent.", and L118's Stapp conditional.
     - Leave hardware L91 (Note 2) alone.
     - Do not move the verdict toward "open": nothing here may say silicon could host an interface. `dynamical-relevance` L81 is the model.
3. **`topics/sorkin-delta-brain-internal-analogues` L91 (W4). Tenet 4.**
   - **Length**: 2,689/4,000; +2.
   - OLD: `Tenet 4 (No Many Worlds) is the presupposition that makes a Δ-analogue's question coherent at all. The test asks which definite three-way residue the outcome statistics carry — a question that presupposes single-outcome ontology. On a Many-Worlds reading every branch occurs and the "residue" has no referent.`
   - NEW: `Tenet 4 (No Many Worlds) shapes how a Δ-analogue's result would be read, not whether the test can be run. An Everettian computes the same residue from one branch's counts, so the measurement does not choose between interpretations; the Map reads those counts as the only record there is.`
   - **Guards**:
     - Keep the paragraph's last sentence ("The article's analysis is in-Map work conditional on Tenet 4, disclosed as such."), per the 09-25 stability note.
     - Match `concepts/sorkin-higher-order-interference` L74 as repaired on 11-01, and read it first.
     - No Many Worlds stays a commitment.
4. **`concepts/attentional-economics` L194, L87 (W5). Tenets 2 and 3.**
   - **Length**: 3,056/3,500; net +11.
   - (a) L194
     - OLD: `(no energy injection, no conservation or Born-statistics violation); a wider channel with the same exactness would be as minimal`
     - NEW: `(no detectable energy injection or Born-statistics deviation, no conservation-law violation); a wider channel within the same bounds would be as minimal`
     - Delta: +2. This matches tenets L69. Add no quantifier, per check 158 W6.
   - (b) L87
     - OLD: `[[mental-effort|Mental effort]] phenomenology supports this interpretation.`
     - NEW: `[[mental-effort|Mental effort]] phenomenology fits this interpretation, though no better than the cost-signal reading named below.`
     - Delta: +9. "Below" points to L117 and L198 (Kurzban et al. 2013).
   - **Guards**:
     - Keep L194's last sentence ("it biases which results become actual") and the bandwidth/minimality separation.
     - Coordinate with todo L3794, which appends to L85 directly above L87.
     - Do not touch L178 (owned by L1629).
5. **`apex/time-consciousness-growing-block` L133 (W6), L73. Tenet 1.**
   - **Length**: 4,641/5,000; net +16.
   - (a) L133
     - OLD: `parallels the gap between wavelength and colour—evidence of something physical description systematically misses.`
     - NEW: `parallels the gap between wavelength and colour, and marks something physical description misses only on a premise a physicalist refuses (see Evidence and Dependency below).`
     - Delta: +12.
   - (b) L73
     - OLD: `That gap between what theories explain and what consciousness involves may be evidence of something functional accounts cannot capture rather than a temporary limitation.`
     - NEW: `That gap between what theories explain and what consciousness involves may mark something functional accounts cannot capture, or only a temporary limitation; the data do not say which.`
     - Delta: +4.
   - **Guards**:
     - Keep L179 ("where the case for irreducibility lives") and L185 (the Tenet 4 control).
     - Leave L187 to the tiebreaker NEEDS-HUMAN.
     - Dualism stays a commitment.
6. **`concepts/phenomenal-transparency-opacity-spectrum` L121 (W7). Tenet 3.**
   - **Length**: 3,037/3,500; +10.
   - OLD: `then consciousness is doing causal work on its own representational apparatus — suggesting something beyond mere feedback loops within a physical system.`
   - NEW: `then on the Map's reading consciousness is doing causal work on its own representational apparatus, though Metzinger's account predicts the same shift through trained attentional availability, so the case does not discriminate.`
   - **Guards**:
     - Keep the paragraph's first sentence (the invisible-interface reading).
     - Keep L117 as the 11-01 refine left it.
     - The Metzinger gloss is the page's own L47 definition. Never concede epiphenomenalism.

**Minted** (P3 refine-draft, inserted above `## Completed Tasks`; active tasks 303 → 309): Priority 1 → todo L4053, 2 → L4062, 3 → L4072, 4 → L4081, 5 → L4090, 6 → L4099.

**Not tasked here**:
- W8 (comparing L60) is the first candidate when a slot opens, but it needs a funded net-zero edit.
- W9 folds into todo L4037. W21 belongs to L3083. W22 belongs to the NEEDS-HUMAN at L109.
- W10–W20 carry priced fixes, and W10 (+1) and W11 (+8) are the cheapest.
- Notes 1 (+1) and 3 (+15) are the cheapest Notes.