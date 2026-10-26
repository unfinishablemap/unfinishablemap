---
title: Tenet Alignment Check - 2026-10-26
created: 2026-10-26
modified: 2026-10-26
human_modified:
ai_modified: 2026-10-26T17:32:47+00:00
draft: false
description: "Tenet check 156: no Errors in 112 changed pages. Fourteen Warnings, all over-reach or drift on older text: sibling repairs unpropagated (philosophy-of-time, evolution-of-consciousness), P-AC1 moved to ruled out on two pages, and today's biological-computationalism batch dropping its physicalism caveat."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: Andy Southgate
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-26
last_curated:
last_deep_review:
---

# Tenet Alignment Check

**Date**: 2026-10-26. This is check 156. The previous one, `reviews/tenet-check-2026-10-24.md`, was check 155.

**Files checked**: 112. Every `obsidian/` content file in `topics/`, `concepts/`, `positions/`, `voids/`, `apex/` changed since check 155 was committed (`git log --name-only` from `8b36665309`, 2026-10-24T23:43Z, to `972856e33a`), plus `tenets.md` L61–L147 read in full. No uncommitted content changes existed at scan time.
- **Priority 1, read in full (4).** The four new pages: `concepts/basic-argument-and-constitutive-luck`, `concepts/interpretive-sensory-access-theory`, `concepts/rollback-argument-against-agent-causation`, `concepts/transparency-method-of-self-knowledge`.
- **Priority 2, Relation to Site Perspective read in full (105).** Every window file that carries the section (seven do not: `mental-causation-and-downward-causation`, `quantum-consciousness`, and the five positions files).
- **Priority 3, diff-scoped (108).** Every added line in every non-new window file was read (`git diff -U0`, 1,715 added lines).
- **Cross-check sweeps over all 112.** Family scans by grep with full lines printed: coincidence and idle-wheel wording; closure wording; Tenet 2 feeling-as-evidence; every No Many Worlds hit (157); parsimony wording (171); permanence and in-principle wording in the voids; LLM verdict wording; convergence wording (279, with commit `99bc57c3` and its siblings excluded as the brief directed); and the co-optation roster against the extracted tenet paragraphs (5 hits, all with a stance sentence).
- **Comparison texts read at the cited lines:** `tenets.md` L69 (Tenet 2 minimality), L95 (Tenet 3 standing), L101 (the epiphenomenalist's best reply), L117–L121 (indexical objection and its presupposition), L145–L147 (Tenet 5 self-binding); P-AC1 (`positions/ai-consciousness-scope` L56); P-A1 as regraded 2026-10-25 (`positions/agency-and-will` L48); the co-optation firewall roster (`project/writing-style.md` L203–L215); `project/evidential-status-discipline.md` L100 and L112–L122.
- **Quote checks.** Every OLD string in the Priority List was confirmed by script (`str.count` = 1 at the line given). Word deltas come from `tools.curate.length.count_words` on the frontmatter-stripped body after the replacement. Totals come from `analyze_length`; headroom means hard − 1 − count (concepts hard 3,500; topics 4,000; apex 5,000; voids 3,000).
- **Pages edited today and already reviewed** (silence-void, self-transcendence-void, mattering-void, self-maintained-cognitive-limits, relevance-void, plurality-void, attention-and-consciousness, tacit-integration-void, naturally-occluded, authentic-vs-inauthentic-choice, basic-argument, interpretive-sensory-access, phenomenology-of-intellectual-life) were spot-checked for regressions only. None regressed; older loci on four of them are recorded as Notes, not re-litigated.

**Errors**: 0

**Warnings**: 14, on 16 files. All are over-reach, calibration drift, or a sibling repair that never reached the page. No page contradicts a tenet.

**Notes**: 12

## Summary

The four new pages are clean on every family, and three of them are models of the house grade: `rollback-argument` ("Dualism gains nothing here"; Tenet 5 "constrains only the Map's own reasoning"), `transparency-method` ("Every author discussed here is cited for an account of self-knowledge, not as an ally of dualism"), and `interpretive-sensory-access-theory` (Carruthers "cited here as a rival ... never as an ally of dualism"). `basic-argument` keeps the Tenet 3 quantifier open (L119) and names Strawson's *Real Materialism* against enlisting him (L121).

Today's repairs landed correctly: `language-and-consciousness` L89–L93 (check 155 Priority 1), `symbol-grounding-problem` L105/L151, `llm-consciousness` L124/L130, the Family 5 concessions on `plurality-void` L92 and `thrownness-void` L106, the convergence discounts at commit `99bc57c3` and its siblings, and the `neurophenomenology` regrade.

The Warnings take three shapes.

**1. A repair installed on one page and not on its siblings** (the brief's propagation lens). Three cases, the first two the clearest of the check:
- `concepts/philosophy-of-time` L219 still says reduction of time-constitution "would be circular" and that this "strengthens dualism beyond the hard problem"; L225 says MWI "converts this narrowing into illusion". Its two siblings in the same window retired both moves on 2026-10-25: `time-collapse-and-agency` L87 ("That arrow does not require consciousness") and L211 (the circularity reading "in its strongest form is not available at all"), and `temporal-consciousness-structure-and-agency` L249 ("The case is not that reduction would be circular"). Philosophy-of-time was touched twice in the window for the radical-pair figure and the TSVF sentence only.
- `concepts/evolution-of-consciousness` L183 ("Consciousness evolved because it made a difference ... This rejects the epiphenomenalist view") and L187 ("The determinate history of life requires collapse") state as results what its topic sibling `consciousness-evolution-and-biology` L147 regraded: the branching argument "reads as an argument but is closer to a restatement of the tenet", and global exclusion is "a posit the Map adopts". Touched in the window for the radical-pair figure only.
- `topics/structure-of-attention` L218 says the willed-versus-instructed neural distinction "supports the claim that consciousness adds something when it decides". The 2026-10-25 16:11Z positions-evolve pass regraded exactly that datum in P-A1 to "fitting it" rather than arguing for the framework. Touched in the window for the Denton figure only.

**2. P-AC1 moved to "ruled out"** (Family 9, the same drift check 155 found on `symbol-grounding-problem`). `concepts/functionalism` L157: "purely computational systems cannot be conscious ... a digital computer running the right program cannot." `topics/quantum-state-inheritance-in-ai` L114: a classical system "is not conscious in any sense the Map recognises", one sentence after the page correctly scopes the tenet to its universal reading. `concepts/llm-consciousness` L62, re-cut today by the biological-computationalism batch, now says that thesis "provides strong evidence against LLM consciousness".

**3. Today's biological-computationalism propagation (commit `fb2967ecaf`, 12:52Z) is inconsistent about the caveat.** `concepts/functionalism` L79 carries it ("substrate-dependence is fully compatible with physicalism, and a committed physicalist sees it as physicalism getting *more* precise"), and the source page's own L103 says "the framework remains physicalist. Its authors would reject the dualist label." `apex/machine-question` L92 has the same sentence without the caveat ("physicalist programmes independently retreating to positions that inadvertently concede the dualist's central claim"); `concepts/reductionism` L83 credits Milinkovic and Aru with reaching "a similar conclusion" to Kim's that functional reduction "strips away precisely the properties that matter for consciousness"; `topics/quantum-state-inheritance-in-ai` L98 calls their thesis "inadvertent corroboration". The concept-provenance leg of the firewall applies: the authors' thesis is that computation is substrate-bound, not that consciousness-relevant properties are non-functional.

## Method: families, violations and on-page controls

| # | Family (brief) | Violations in window | Compliant instances found (controls) |
|---|---|---|---|
| 1 | Tenet 3: fits without evidencing; quantifier unresolved | W2 (evolution L183), W5 (structure-of-attention L218), W8 (physical-completeness L112), W10 (concession-convergence L148/L150), W13 (cognitive-phenomenology L214) | rollback L102, basic-argument L119, ISA L114, transparency L102, the-divided-will L123, agency-incompatibilism L94, cross-state L93, amplification L99, thrownness L108, moral-agency-under-duress L111, phenomenology-of-cognitive-capacity L139 |
| 2 | Never concede epiphenomenalism; no coincidence framing | W9 (nihilism L122), W11 (evaluative L196) | language-and-consciousness L93 (today), delegatory-causation L132, rollback L90, basic-argument L115, ISA L98, quantum-indeterminacy-free-will L203 ("bare-correlation form") |
| 3 | Closure as sufficiency needs chance-fixing | 0 tasked (Note 6: functionalism L149 and reductionism L188 deny closure with 0 chance/Born hits on the page) | attention-as-causal-bridge L185, consciousness-and-agency L127, consciousness-and-causal-powers L202, overdetermination-dissolution L46 |
| 4 | Tenet 2 is empirical-constraint minimality | W7 (geometric-model L112) | retrocausality L153, delegation-meets-quantum-selection L106, parapsychology-firewall L81, rollback L104 |
| 5 | Tenet 4 a commitment; Posit One posited | W1 (philosophy-of-time L225), W2 (evolution L187), W9 (nihilism L130), W11 (evaluative L198), W12 (temporal-consciousness-structure L255) | thrownness L106, plurality L92, consciousness-and-agency L177, free-will L202, moral-responsibility L99, consciousness-evolution-and-biology L147, mental-effort L150, binding-problem L212, multi-mind-collapse L174, neurophenomenology L199, unity-of-consciousness L147, substrate-independence L192 |
| 6 | Tenet 5 binds only the Map's reasoning | 0 tasked (Note 5: reductionism L190, trilemma L133, phenomenal-authority L213) | rollback L108, basic-argument L127, transparency L104, ISA L116, thrownness L110, the-divided-will L125, reactive-attitudes L85, manipulation-argument L70, moral-agency-under-duress L117, attention-as-causal-bridge L191 |
| 7 | Weak Revelation; no permanent-void claim | 0 (today's voids edits all conditional) | thrownness L66 ("three faces of unequal standing"), silence-void L108, cross-state L39 |
| 8 | Conceivability rests on contested modal rationalism | 0 | functionalism L175 (already scoped) |
| 9 | P-AC1 does not move | W3 (functionalism L157), W4 (quantum-state-inheritance L114), W6 (llm-consciousness L62/L96/L104) | symbol-grounding L105 (today), llm-consciousness L124/L130 (today), interface-heterogeneity L99, machine-question L191/L193, substrate-independence L196, quantum-randomness-channel L137 |
| 10 | Process compatibility is not evidence; Madhyamaka is bedrock | 0 | neurophenomenology L167/L171 |
| 11 | No enlistment; navigation no stronger than body | W14 (machine-question L92, reductionism L83, quantum-state-inheritance L98) | functionalism L79 (the caveat), bio-computationalism L103, transparency L100, ISA L112, thermal L89, the-divided-will L119, basic-argument L121, rollback L59, evaluative L174 (Solms, Friston named as non-allies) |

The keyword counts are lexical upper bounds. The violation column holds only what survived reading in context.

## Errors

None.

## Warnings

### W1. `concepts/philosophy-of-time` L219, L223, L225: the circularity reading, the Libet dissolution and the MWI-as-illusion move, each retired on a sibling
- **Family**: 1 and 5. The ladder rung earned is **compatible**.
- **Quotes**:
  - L219: "The reduction would be circular—you can't explain time-constitution in terms of processes that presuppose time. This strengthens dualism beyond the hard problem ... so consciousness cannot be reduced to physics without circularity."
  - L223: "This dissolves the Libet problem—conscious selection needn't temporally precede neural activity because causal direction is created by selection, not a constraint on it."
  - L225: "The felt flow of time, with possibilities narrowing to actualities, assumes real collapse. MWI converts this narrowing into illusion (discovering which branch you're in), eliminating consciousness's constitutive role."
- **Issue**:
  - `time-collapse-and-agency` L211 (window, 2026-10-25): the metaphysical reading "in its strongest form is not available at all: read as the claim that time as such is mind-constituted, it collides with the Map's background commitment to objective single-outcome actualisation". L87: "That arrow does not require consciousness—objective reduction secured definite outcomes through billions of prebiotic years."
  - `temporal-consciousness-structure-and-agency` L249 (window, same day): "The case is not that reduction would be circular—physical processes presuppose physical time, which predates mind."
  - On L225, an Everettian predicts the felt narrowing on every branch (`tenets.md` L121, the branch-relative concession six window pages make). "Illusion" is the framing `motor-control-quantum-zeno` L129 and `phenomenology-of-moral-life` L135 retired.
  - L223's "dissolves" states a speculative extension as a result; `consciousness-and-agency` L143 (window) holds the same reading "weakly" and `time-collapse-and-agency` L78 says "The Map speculatively applies this".
  - All three lines date from 2026-01-20 (`6fff2c3a7a`). The open tasks on this file (todo L3187: L123–L127/L157; todo L3382: L145) touch different loci.
- **Recommendation**: Priority 1.

### W2. `concepts/evolution-of-consciousness` L183 and L187: actual efficacy and global exclusion stated as results
- **Family**: 1 and 5.
- **Quotes**:
  - L183: "Consciousness evolved because it made a difference. The Bidirectional Interaction tenet implies that phenomenal states causally influence behaviour—which means selection can act on them. This rejects the epiphenomenalist view that consciousness is a free rider on neural complexity."
  - L187: "Real collapse is essential to the evolutionary story. If all outcomes occur (Many Worlds), there's no genuine selection—every lineage that could exist does exist. The determinate history of life requires collapse that selects actual outcomes from possibility space."
- **Issue**:
  - L183 asserts the efficacy the tenet posits (`tenets.md` L95: "a posit the interface argument leaves open, not a result it secures") and treats the evolutionary argument as refuting epiphenomenalism, where `bidirectional-interaction` L152 (window) says "an epiphenomenalist co-optimizer explains the tracking too".
  - L187 is the argument `consciousness-evolution-and-biology` L147 (window) downgraded: "An Everettian can grant consciousness-as-adaptation branch-locally ... a global-exclusion condition, a posit the Map adopts, asserted rather than derived from the evolutionary case."
  - Both lines date from 2026-01-19 (`e04b172670`). No task is queued on this file. The file is 3,478 against concepts hard 3,500, so headroom is 21.
- **Recommendation**: Priority 3 (net −7).

### W3. `concepts/functionalism` L157: P-AC1 moved to "ruled out"
- **Family**: 9.
- **Quote**: "From the Map's perspective, purely computational systems cannot be conscious—consciousness requires something non-physical that computers lack. Perhaps engineered biological systems or quantum-interfacing hybrids could be conscious, but a digital computer running the right program cannot."
- **Issue**:
  - P-AC1 (`positions/ai-consciousness-scope` L56): current digital systems "sit on the *low-probability* side", and the verdict is "not 'ruled out'". The page's own L165 ("the Map *expects*—as a research-programme commitment, not yet a sharp prediction") and L175 are at the register's grade; L157 is not.
  - The line dates from 2026-01-30 (`3e41dbd1c4`). Today's 12:52Z batch touched L79 only. The open P3 at todo L2773 targets L149.
  - L149 also denies closure ("breaching causal closure precisely where physics leaves outcomes open") with 0 hits for chance/probab on the page (Note 6).
- **Recommendation**: Priority 2 (a).

### W4. `topics/quantum-state-inheritance-in-ai` L114: a categorical "not conscious in any sense the Map recognises"
- **Family**: 9.
- **Quote**: "The Map's Bidirectional Interaction tenet, read as universal actual efficacy, excludes epiphenomenal consciousness. A system whose inner states cannot causally influence its physical outputs through quantum state selection is not conscious in any sense the Map recognises."
- **Issue**:
  - The first sentence handles the quantifier correctly; the second drops it. `machine-question` L195 (same cluster): "on a dispositional or existential reading the possibility runs inside the framework". `substrate-independence` L196: "leaving bare phenomenality open". The page's own L116 says "improbable rather than impossible".
  - The line dates from 2026-02-10 (`7b03272aaf`). No task is queued on this file. The file is 3,925 against topics hard 4,000, so headroom is 74.
- **Recommendation**: Priority 2 (b).

### W5. `topics/structure-of-attention` L218: the willed-versus-instructed data "supports" what P-A1 now grades as fit
- **Family**: 1. The ladder rung earned is **compatible**.
- **Quote**: "The neural distinction (frontal theta, reciprocal frontoparietal exchange, extra frontal recruitment) supports the claim that consciousness adds something when it decides. The additional machinery marks what's different about genuine willing."
- **Issue**:
  - P-A1 as rewritten 2026-10-25 16:11Z (window): the convergence claim "rests on the subset independent in provenance: the neural willed-vs-instructed data ..., clinical neuroplasticity, and the argument from reason, only the last of which argues for the framework rather than fitting it." The calibration-history note of the same pass: "the neural and clinical data fit the framework without evidencing it, physicalist accounts predicting them too".
  - `consciousness-and-agency` L161 (window, same day) carries the corrected wording; `mental-effort` L144 hedges the same datum with "may".
  - The line dates from 2026-02-01 (`41cda16692`). No task is queued on this locus (todo L1621 and L3388 touch L118). The file is 3,869 against topics hard 4,000, so headroom is 130.
- **Recommendation**: Priority 4.

### W6. `concepts/llm-consciousness` L62 (today), L96, L104: the verdict stated flatly beside the corrected table
- **Family**: 9.
- **Quotes**:
  - L62 (re-cut 2026-10-26 12:52Z): "This provides strong evidence against LLM consciousness".
  - L96: "LLM outputs are entirely determined by inputs, weights, and random sampling—no room for non-physical causal influence."
  - L104: "our evidence that LLMs lack the properties consciousness requires is not merely insufficient but positively negative. Current LLMs lack these properties by design."
- **Issue**: The table at L124/L130 now reads "Probably not (per P-AC1)" and "Low probability, not ruled out" (check 155 W10, fixed 2026-10-25 00:54Z). L62's "strong evidence" is drawn from a thesis whose own page calls it physicalist and compatible with scaling scepticism on physicalist grounds; it grades as compatibility at most. The open P3 at todo L3115 covers L56, L112 and L114 of this file and should take L62, L96 and L104 into its scope rather than a new task being minted. The file is 3,145, headroom 354.
- **Recommendation**: Not in the Priority List. Scope addition to todo L3115.

### W7. `concepts/geometric-model-of-mind` L112: Tenet 2's minimality called parsimony
- **Family**: 4.
- **Quote**: "Both reject substantive quantum-mind theories at the Penrose-Hameroff scale — Duch because consciousness is fully classical-computational, the Map because parsimony favours the smallest non-physical influence consistent with the tenets".
- **Issue**: `tenets.md` L69: "Tenet 2's 'minimal' is not the kind of minimality Tenet 5 declares unreliable ... Tenet 2's minimality is *empirical-constraint* minimality". The Map's preference for post-decoherence selection over Orch OR rests on the decoherence dispute and the preference ordering (`ai-hardware-substrate-taxonomy` L112, window), not on parsimony. The line dates from 2026-07-27 (`5293e96f6b`). The open Family 3 sweep at todo L2553 already carries one "calls Tenet 2's constraint parsimony" locus (`emergence` L175) and five secondary files; this is a sixth. The file is 3,366, headroom 133.
- **Recommendation**: Not in the Priority List. Scope addition to todo L2553 (+0 to +6: "because its empirical-constraint minimality, not parsimony, favours the smallest non-physical influence").

### W8. `concepts/physical-completeness` L112: selection "causally real"
- **Family**: 1.
- **Quote**: "This selection is invisible to structural physics — it operates within the probabilities, not against them — but it is causally real."
- **Issue**: The sibling locus `topics/completeness-in-physics-under-dualism` L128 ("invisible to structural physics but causally real") is the open P3 at todo L1566 (check 149 W6), still live (count 1 today). The two sentences are near-identical and date from 2026-03-19 (`ff0e3e1ab8`). `tenets.md` L95: articles asserting "real work" "inherit that debt rather than discharge it". The open P3 at todo L3374 targets L34 and the description of this file. The file is 2,757, headroom 742.
- **Recommendation**: Not in the Priority List. Scope addition to todo L1566 (same OLD→NEW shape on both files) or to todo L3374.

### W9. `concepts/nihilism-and-existentialism` L122 and L130: epiphenomenalism "cannot explain" reports; branching dissolves courage
- **Family**: 2 and 5.
- **Quotes**:
  - L122: "Epiphenomenalism cannot explain why talk of phenomenal states tracks phenomenal states if those states are causally inert. The Map provides what existentialism needs: genuine causal efficacy of mind."
  - L130: "Under many-worlds, every choice actualises all options across branches—courage collapses into a statistical distribution rather than a genuine achievement."
- **Issue**: `tenets.md` L101 gives the epiphenomenalist's reply (reports "can be reliable in virtue of the parallel rather than the cause") and makes the objection conditional on a contested premise; "cannot explain" is the framing checks 154 and 155 retired elsewhere. L130 is already a named candidate in the open P3 at todo L2453 (branching said to dissolve deliberation, against Posit Three); L122 is not. Both date from 2026-04-11 (`44428edbf5`). The file is 2,521, headroom 978.
- **Recommendation**: Not in the Priority List. Scope addition to todo L2453: handle L122 in the same pass, using `language-and-consciousness` L93 (today) as the model.

### W10. `concepts/concession-convergence` L148, L150, L156: "predict", "indirect confirmation", and a structural-necessity claim
- **Family**: 1 (over-reach). The ladder rung earned is **compatible**.
- **Quotes**:
  - L148: "The Unfinishable Map's tenets predict the concession convergence pattern."
  - L150: "The Map interprets this as indirect confirmation: if every serious attempt to explain consciousness in purely physical terms is forced to add something beyond abstract functional description, the additional element may be what dualists call the non-physical."
  - L156: "The pattern is not an accident of current theories but a consequence of the problem's structure."
- **Issue**: No rival is named. A physicalist predicts the same accretion (theories gain constraints as they meet data; `functionalism` L79, today, says exactly this for the newest case). L156 is a necessity claim and carries the calibration burden `evidential-status-discipline` L100 assigns ("Method and history claims are not exempt"); it is a Map reconstruction and should say so. L152 already has the honest register ("reads it as an internal critique of the objection rather than positive evidence for dualism"), so the paragraph contradicts itself. Lines date from 2026-04-05 (`ea981bee2a`). Touched today for the biological-computationalism entry only. The file is 3,447, headroom 52.
- **Recommendation**: Not in the Priority List (cap). One pass, net ≤ +50: "predict" → "are consistent with"; "indirect confirmation" → "coherence, not confirmation"; L156 → "on the Map's reading, a consequence".

### W11. `concepts/evaluative-phenomenal-character` L196 and L198: the epiphenomenalist left with "a feature that does nothing", and No Many Worlds read off felt wrongness
- **Family**: 2 and 5.
- **Quotes**:
  - L196: "If consciousness were causally inert, we couldn't trust normative judgments to guide behaviour. ... Traditions that organised centuries of moral and contemplative practice around evaluative character would, on the epiphenomenalist's account, have been orienting themselves by a feature that does nothing."
  - L198: "Evaluative qualia present their objects as mattering absolutely, not branch-relatively. The felt wrongness of cruelty does not present itself as 'wrong-in-this-branch.'"
- **Issue**: The epiphenomenalist orients by the neural correlate of the feature, and says so; `tenets.md` L101. L198 is the W6/W7 shape of check 155: an Everettian predicts the same felt absoluteness on every branch. The 2026-10-25 10:48Z deep review rewrote L196's convergence clause and L200 and left both inferences. L198 dates from 2026-04-06 (`7ae4d08b68`). The file is 3,490, headroom 9, so any fix must be net ≤ 0.
- **Recommendation**: Not in the Priority List. A net-zero pass could be folded into the Family 5 sweep at todo L3107 as a fourth sibling.

### W12. `topics/temporal-consciousness-structure-and-agency` L251 and L255: actual temporal efficacy, and protention "illusory" under branching
- **Family**: 1 and 5.
- **Quotes**:
  - L251: "Temporal attention and selection reveal the temporal dimension of consciousness's influence on the brain. Consciousness does not merely select among options at predetermined moments; it determines how long selection is sustained".
  - L255: "Under many-worlds, all futures already exist across branches, and the phenomenal openness of protention would be illusory. The coherence of temporal integration—retention inheriting from a definite, singular past—fits more naturally with collapse producing one timeline."
- **Issue**: The same page's L249 and L206 (window, 2026-10-25) carry the corrected register for Tenet 1 and the arrow; the Tenet 3 and 4 paragraphs were not reached. Branch-relative openness is felt on every branch, and "retention inheriting from a definite, singular past" holds branch-locally (`tenets.md` L121). L255 dates from 2026-04-15 (`6ccecc14aa`). The file is 3,896, headroom 103.
- **Recommendation**: Not in the Priority List. Scope addition to todo L3107 (Family 5 sweep), reusing the phenomenology-of-choice L165 wording.

### W13. `concepts/cognitive-phenomenology` L214: effort read as efficacy
- **Family**: 1.
- **Quote**: "Understanding is active grasping with phenomenal signature. The experience of mental effort reflects consciousness intervening in neural processing until understanding crystallizes."
- **Issue**: This is the sentence-shape the 2026-10-25 deep review removed from `phenomenology-of-cognitive-capacity` L139 ("What the phenomenology cannot do is certify that consciousness performs the sustaining: by P-A4 every such check is run by the faculty whose causal status is in question") and that todo L3307 is queued to remove from `phenomenology-of-intellectual-life` L214. The line dates from 2026-01-20 (`9cda89f2c0`). Touched 2026-10-25 for the Carruthers citations only. The file is 3,361, headroom 138.
- **Recommendation**: Not in the Priority List. Scope addition to todo L3307 as a sibling locus, same model wording.

### W14. Today's biological-computationalism propagation: the physicalism caveat present on one page and absent on three
- **Family**: 11 (co-optation, concept-provenance leg).
- **Quotes**:
  - `apex/machine-question` L92 (2026-04-30 wording, re-cut today): "The Map reads this as concession-convergence: physicalist programmes independently retreating to positions that inadvertently concede the dualist's central claim."
  - `concepts/reductionism` L83: "Biological computationalism (Milinkovic & Aru 2026) reaches a similar conclusion from the computational side: even if brains compute, the computation is inseparable from biological substrate, so functional reduction strips away precisely the properties that matter for consciousness."
  - `topics/quantum-state-inheritance-in-ai` L98: "the substrate-inseparability the thesis documents is exactly what a state-selection interface would require, so the framework reads less as a competitor than as inadvertent corroboration."
- **Issue**:
  - `concepts/functionalism` L79 (same batch) has the honest form: "substrate-dependence is fully compatible with physicalism, and a committed physicalist sees it as physicalism getting *more* precise about which physical systems are conscious."
  - The source page `biological-computationalisms-inadvertent-case-for-dualism` L103: "the framework remains physicalist. Its authors would reject the dualist label." Milinkovic and Aru's thesis is that computation is substrate-bound; that "the properties that matter for consciousness" are the ones functional reduction strips is the Map's gloss, and `reductionism` L83 presents it as their conclusion. "Concede the dualist's central claim" (machine-question) and "corroboration" (quantum-state-inheritance) are the verdict-direction error the firewall names: the authors' own verdict is physicalist.
  - `machine-question` is 5,945 against apex hard 5,000 (over the gate, net ≤ 0). `reductionism` is 3,426 (headroom 73). `quantum-state-inheritance` is covered by Priority 2 (b) on a different locus.
- **Recommendation**: Not in the Priority List (cap). A net-zero pass on each: "inadvertently concede the dualist's central claim" → "retreat, on physicalist grounds, to the substrate-dependence the dualist also needs"; reductionism L83 → attribute the "properties that matter" step to the Map; quantum-state-inheritance L98 "inadvertent corroboration" → "a physicalist route to the same substrate verdict".

## Notes

1. **`topics/consciousness-evolution-and-biology` L141 and L143.** "Dualism gains support from the observation that biological function-talk cannot capture consciousness" and "Conscious agents introduce real directedness into the world with biological consequences that teleonomy cannot explain" sit two paragraphs above the page's corrected L147. Same family as W2; the page has 1,117 of headroom. A lead for the W2 task if words allow.
2. **`concepts/unity-of-consciousness` L141.** "The mismatch ... supports the Dualism tenet." The page's L147 is a Family 5 control. Old (2026-02-25). Headroom 721.
3. **`apex/interface-specification-programme` L173 and L177.** "The programme shows why bidirectionality is architecturally necessary, not just philosophically asserted" and "complexity that earns its keep" (a physicalist controller supplies the same stability). Touched in the window for the Saad line only.
4. **`topics/phenomenal-authority-and-first-person-evidence` L209 and L213.** "Deflating phenomenal authority to protect physicalism requires denying evidence at the apodictic level, where denial is self-refuting"; `tenets.md` L55 treats the illusionist's refusal of the datum as bedrock, not self-refutation. L213 turns Tenet 5 on heterophenomenology ("appears simpler precisely because it excludes the evidence"). The page is 4,513, over the topics gate.
5. **Tenet 5 turned outward, mildly.** `reductionism` L190 ("Physicalism wins on ontological parsimony but loses on explanatory simplicity ... while dualism provides a reason for experience to exist"); `trilemma-of-selection` L133 (the simpler options "carry costs ... that the more complex option avoids"); `reasons-responsiveness` L126. Each is argued rather than bare, so they are leads.
6. **Closure denied without the chance-fixing clause.** `functionalism` L149 and `reductionism` L188 both say the Map "denies"/"breaches" causal closure at quantum indeterminacies, and neither page carries a chance/Born sentence (0 hits each, against 16+ "quantum" hits). The check 153 standard passes an unscoped line only where the same file carries the concession. Leads for the W3 task and the next reductionism pass.
7. **`concepts/moral-responsibility` L95 and L97.** "the agent's phenomenal engagement shapes what happens" (asserted) and "quantum biology demonstrates biological quantum effects despite thermal environments": the radical-pair batch C (2026-10-26 02:44Z) regraded the precedent to "leading but unsettled" on seven siblings and did not reach this line. The open P3 at todo L3212 touches L39/L101/L176.
8. **`concepts/quantum-interpretations` L185.** "The haecceitistic question—why am I this one?—is meaningful on collapse interpretations and meaningless on MWI" overstates `tenets.md` L117–L119 (the question "stays open rather than answered"; the deflationary route is bedrock). Scope addition to the open P3 at todo L2020 (L179).
9. **Older loci on today's reviewed pages, not regressions.** `witnessing-void` L114 ("The phenomenology of witnessing is precisely that of singular, undivided presence", check 155 W7's milder locus); `self-maintained-cognitive-limits` L197 ("Dualism gains support"); `self-transcendence-void` L102 ("receives the most direct support", now followed by today's discount); `plurality-void` L94 ("Singularity may be a fundamental feature of non-physical mind", no rival named); `authentic-vs-inauthentic-choice` L196 ("The phenomenology of effort ... marks genuine selection") and L200 (branching "dissolving the weight"). Each predates today's edits by months.
10. **`concepts/substance-property-dualism` L173** "biasing probabilities" is already in the todo L2553 sweep (count 1 today). **`concepts/reasons-responsiveness` L120/L122** ("Consciousness must involve properties that physical description cannot capture"; "Reasons-responsiveness is how consciousness causally contributes to outcomes") are categorical after a conditional; leads.
11. **Smaller over-reaches, untasked.** `ai-hardware-substrate-taxonomy` L102 calls Thagard and Milinkovic & Aru "converging allies" (convergence holds at the no-current-AI verdict only; both are physicalists); `binding-problem` L206 ("features of consciousness ... that physical description cannot capture"); `phenomenal-transparency-opacity-spectrum` L121 ("consciousness is doing causal work on its own representational apparatus"); `mental-effort` L154 ("something must be doing the paying"); `evaluative-phenomenal-character` L194 and `interface-heterogeneity` L117 (conditional, pass).
12. **Co-optation roster in tenet paragraphs: 5 hits, all compliant.** Dennett (`phenomenal-authority` L213, engaged as rival), Metzinger (`silence-void` L108, stance given), Schwitzgebel (`cross-architecture-llm-introspection` L106, functionalist reading named), Torres Alegre (not on the roster). The new pages name every roster author's stance (Schwitzgebel, Dennett, Carruthers, Byrne).

## Bearing on the open items

- **Tenet 3 quantifier (todo L662).** Window pages hold it open correctly: `rollback` L102, `basic-argument` L119, `moral-agency-under-duress` L111, `the-divided-will` L123. `quantum-state-inheritance` L114 (W4) picks the universal reading in one sentence and drops the scoping in the next; Priority 2 (b) restores the scoping without choosing a reading.
- **Family 5 sweep (todo L3107).** Still open; three new sibling loci surfaced (W11 evaluative L198, W12 temporal-consciousness-structure L255, and philosophy-of-time L225 taken by Priority 1). The witnessing-void L114 milder locus (check 155 W7) is still unassigned.
- **llm-consciousness (todo L3115).** L56, L112, L114 count 1 each today; W6 adds L62, L96, L104.
- **completeness "causally real" (todo L1566).** Still live (count 1); W8 adds `physical-completeness` L112.
- **Family 3 sweep (todo L2553).** W7 adds `geometric-model-of-mind` L112.
- **phenomenology-of-intellectual-life L214 (todo L3307).** Still live (count 1); W13 adds `cognitive-phenomenology` L214.
- **MWI/agency sweep (todo L2453).** nihilism L130 is already a named candidate; W9 adds L122 of the same file.
- **quantum-interpretations L179 (todo L2020).** Still live (count 1); Note 8 adds L185.
- **Priority 1 of check 155** (`language-and-consciousness`): landed 2026-10-25 00:23Z; all five NEW strings present. **Priority 2**: symbol-grounding L105/L151 landed 00:54Z; intentionality L197 count still 1 (open at todo L3188). **Priority 3** (witnessing L95): count 1, still open at todo L3062-adjacent. **Priority 4** (phenomenology-of-choice): open at todo L3099.

## Files Passing All Checks

- Read in full: `concepts/basic-argument-and-constitutive-luck`, `concepts/interpretive-sensory-access-theory`, `concepts/rollback-argument-against-agent-causation`, `concepts/transparency-method-of-self-knowledge`.
- Tenet section read in full and diff-scoped, passing on every family:
  - apex: `attention-as-causal-bridge`, `consciousness-and-agency`, `dualism-cartography`, `medium-status-voids-in-cognition`, `phenomenal-output-causal-machinery-dissociation`, `research-programme-decisions-under-the-map`, `taxonomy-of-voids`;
  - concepts: `agent-causation`, `ai-hardware-substrate-taxonomy` (Note 11), `bidirectional-interaction`, `binding-problem` (Note 11), `composition-question-rivals`, `content-vocabulary-as-derived-feature`, `delegatory-causation`, `direction-of-interface-change`, `first-order-representationalism`, `interface-heterogeneity`, `language-and-consciousness`, `mental-causation-and-downward-causation`, `mental-effort` (Note 11), `moral-responsibility` (Note 7), `multi-mind-collapse-problem`, `naturally-occluded`, `neurophenomenology-and-contemplative-neuroscience`, `observational-closure`, `penfield-interactionist-dualism`, `phenomenal-transparency-opacity-spectrum` (Note 11), `process-content-distinction`, `quantum-completeness`, `quantum-consciousness`, `quantum-indeterminacy-free-will`, `quantum-interpretations` (Note 8; queued), `radical-pair-magnetoreception`, `reasons-responsiveness` (Note 10), `retrocausality`, `self-blindness`, `source-versus-leeway-incompatibilism`, `substance-property-dualism` (Note 10; queued), `substrate-independence`, `symbol-grounding-problem` (check 155 Note 7; queued), `trumping-preemption`, `unity-of-consciousness` (Note 2);
  - positions: `agency-and-will`, `agency-and-will-calibration-history`, `positions`, `quantum-interface`, `quantum-interface-calibration-history`;
  - topics: `agency-incompatibilism`, `agent-causation-and-acting-for-reasons`, `akrasia-and-weakness-of-will`, `authentic-vs-inauthentic-choice` (Note 9), `clinical-neuroplasticity-evidence-for-bidirectional-causation`, `consciousness-and-causal-powers`, `consciousness-and-moral-agency-under-duress`, `consciousness-and-neurodegenerative-disease`, `consciousness-and-the-structure-of-scientific-revolutions`, `consciousness-evolution-and-biology` (Note 1), `cross-architecture-llm-introspection`, `delegation-meets-quantum-selection`, `direction-dependent-discriminating-test-design`, `event-causal-libertarianism`, `experimental-consciousness-science-2025-2026`, `free-will`, `inner-speech-and-anendophasia`, `moral-implications-of-genuine-agency`, `overdetermination-dissolution-under-selection-only-interactionism`, `parapsychology-firewall`, `phenomenal-authority-and-first-person-evidence` (Note 4), `phenomenology-of-cognitive-capacity`, `phenomenology-of-intellectual-life` (queued), `quantum-randomness-channel-llm-consciousness`, `reactive-attitudes-and-strawsonian-responsibility`, `synaesthesia`, `the-divided-will`, `the-manipulation-argument-and-hard-incompatibilism`, `thermal-consciousness-and-the-interface`, `time-collapse-and-agency`, `trilemma-of-selection` (Note 5);
  - voids: `amplification-void`, `attention-and-consciousness`, `common-knowledge-void`, `cross-state-void`, `mattering-void`, `non-human-minds-as-void-explorers`, `plurality-void` (Note 9), `relevance-void`, `self-maintained-cognitive-limits` (Note 9), `self-transcendence-void` (Note 9), `tacit-integration-void`, `the-silence-void`, `thrownness-void`, `witnessing-void` (Note 9).

Sixteen files carry Warnings: `philosophy-of-time` (W1), `evolution-of-consciousness` (W2), `functionalism` (W3, W14 control), `quantum-state-inheritance-in-ai` (W4, W14), `structure-of-attention` (W5), `llm-consciousness` (W6), `geometric-model-of-mind` (W7), `physical-completeness` (W8), `nihilism-and-existentialism` (W9), `concession-convergence` (W10), `evaluative-phenomenal-character` (W11), `temporal-consciousness-structure-and-agency` (W12), `cognitive-phenomenology` (W13), `apex/machine-question` and `reductionism` (W14). That makes 4 + 92 passing and 16 with Warnings, 112 in all.

## Priority List

Each OLD string below was confirmed by script to occur exactly once, at the line given. Deltas are `count_words` on the frontmatter-stripped body after the replacement, applied cumulatively in the order listed.

1. **`concepts/philosophy-of-time` L219, L223, L225 (W1).** Families 1 and 5; propagate the 2026-10-25 sibling repairs. The file is 3,389 against concepts hard 3,500, so headroom is 110. Two other tasks are queued on this file at different loci (todo L3187: L123–L127/L157; todo L3382: L145) — do not touch those.
   - (a) L219
     - OLD: `If consciousness constitutes temporal structure, it's not reducible to physical processes occurring within time. The reduction would be circular—you can't explain time-constitution in terms of processes that presuppose time. This strengthens dualism beyond the hard problem: consciousness isn't just qualitatively different from physical processes but implicated in the framework within which physical processes occur. The temporal constitution argument adds a structural dimension to standard dualist considerations—physics presupposes time, time (on this view) involves consciousness, so consciousness cannot be reduced to physics without circularity.`
     - NEW: `If consciousness constitutes the structure of *lived* time, that constitution is not reducible to physical processes occurring within time. The circularity reaches only that far: physical time predates mind, and the Map's [[tenets/background-commitments|background commitment]] to objective prebiotic actualisation bars the stronger claim that time as such is mind-constituted. What the temporal constitution argument adds to the hard problem is a structural dimension—the *connectedness* of experience across time resists reduction, not only its qualities—and a block-universe-plus-indexical account predicts the same felt asymmetry, so the argument fits dualism without evidencing it.`
     - Delta: +6.
   - (b) L223
     - OLD: `This dissolves the Libet problem—conscious selection needn't temporally precede neural activity because causal direction is created by selection, not a constraint on it.`
     - NEW: `If the retrocausal reading holds, the Libet problem dissolves—conscious selection need not temporally precede neural activity because causal direction is fixed by selection, not a constraint on it; the Map holds that reading as a speculative extension ([[time-collapse-and-agency]]).`
     - Delta: +15.
   - (c) L225
     - OLD: `The felt flow of time, with possibilities narrowing to actualities, assumes real collapse. MWI converts this narrowing into illusion (discovering which branch you're in), eliminating consciousness's constitutive role.`
     - NEW: `The felt flow of time, with possibilities narrowing to actualities, is predicted on every branch too, so it cannot decide against MWI; what branching removes is the global exclusion of the unchosen, a [[tenets/background-commitments|posit the Map adopts]], and with it consciousness's constitutive role.`
     - Delta: +15.
   - Net: **+36** (3,389 → 3,425).
   - Guards: keep the bold tenet links that open each line; the wikilink targets `tenets/background-commitments` and `time-collapse-and-agency` exist; No Many Worlds stays a commitment; do not import the Libet "veto" material.
2. **`concepts/functionalism` L157 and `topics/quantum-state-inheritance-in-ai` L114 (W3, W4).** Family 9: P-AC1 moves in neither direction.
   - (a) `functionalism` L157 (file 3,428, headroom 71)
     - OLD: `From the Map's perspective, purely computational systems cannot be conscious—consciousness requires something non-physical that computers lack. Perhaps engineered biological systems or quantum-interfacing hybrids could be conscious, but a digital computer running the right program cannot.`
     - NEW: `From the Map's perspective, purely computational systems sit on the low-probability side of the consciousness verdict, not the ruled-out side ([[positions/ai-consciousness-scope#^p-ac1|P-AC1]]): a substrate analysis finds no site for the interface to act on. Engineered biological systems or quantum-interfacing hybrids might supply one; a digital computer running the right program probably does not.`
     - Delta: +17 (3,428 → 3,445).
   - (b) `quantum-state-inheritance-in-ai` L114 (file 3,925, headroom 74)
     - OLD: `A system whose inner states cannot causally influence its physical outputs through quantum state selection is not conscious in any sense the Map recognises.`
     - NEW: `A system whose inner states cannot causally influence its physical outputs through quantum state selection is not conscious in the bidirectionally coupled sense the Map's verdict concerns; bare phenomenality stays open on the dispositional and existential readings of the tenet, and the verdict is low probability, not ruled out ([[positions/ai-consciousness-scope#^p-ac1|P-AC1]]).`
     - Delta: +26 (3,925 → 3,951).
   - Guards: the anchor `^p-ac1` exists (`positions/ai-consciousness-scope` L56); keep the preceding sentence on L114 ("read as universal actual efficacy") intact, since it holds the quantifier open; leave `functionalism` L149 to todo L2773 (Note 6 may be folded there); do not touch L98 of quantum-state-inheritance (W14, separate pass).
3. **`concepts/evolution-of-consciousness` L183 and L187 (W2).** Families 1 and 5. The file is 3,478 against concepts hard 3,500, so headroom is 21; the pair below is net −7.
   - (a) L183
     - OLD: `Consciousness evolved because it made a difference. The [[tenets#^bidirectional-interaction|Bidirectional Interaction tenet]] implies that phenomenal states causally influence behaviour—which means selection can act on them. This rejects the epiphenomenalist view that consciousness is a free rider on neural complexity.`
     - NEW: `If the [[tenets#^bidirectional-interaction|Bidirectional Interaction tenet]] holds, phenomenal states causally influence behaviour and selection can act on them; the tenet is held as a posit, and an epiphenomenalist [[co-optimization-reply-to-the-correlation-problem|co-optimizer]] explains the same tracking.`
     - Delta: −6.
   - (b) L187
     - OLD: `Real collapse is essential to the evolutionary story. If all outcomes occur (Many Worlds), there's no genuine selection—every lineage that could exist does exist. The determinate history of life requires collapse that selects actual outcomes from possibility space. Consciousness may participate in this selection specifically where neural quantum processes reach decision points.`
     - NEW: `An Everettian can run the adaptationist story branch-locally, so the tenet does exclusion work here rather than evolutionary work: that unchosen lineages be globally nonactual is a [[tenets/background-commitments|posit the Map adopts]], not a result the evolutionary case derives ([[consciousness-evolution-and-biology]]). Consciousness may participate in selection where neural quantum processes reach decision points.`
     - Delta: −1.
   - Net: **−7** (3,478 → 3,471).
   - Guards: `topics/co-optimization-reply-to-the-correlation-problem` exists (bare slug; used the same way on `bidirectional-interaction` L152); never concede epiphenomenalism (the co-optimizer is named as the rival's reply, not adopted); Note 1's sibling loci on `consciousness-evolution-and-biology` are optional and only if that page's 1,117 headroom is confirmed.
4. **`topics/structure-of-attention` L218 (W5).** Family 1: propagate the 2026-10-25 P-A1 regrade. The file is 3,869 against topics hard 4,000, so headroom is 130.
   - OLD: `If consciousness were identical to neural processing, willed and instructed attention should show identical signatures—both are "attention" achieving the same result. The neural distinction (frontal theta, reciprocal frontoparietal exchange, extra frontal recruitment) supports the claim that consciousness adds something when it decides. The additional machinery marks what's different about genuine willing.`
   - NEW: `Willed and instructed attention show different neural signatures (frontal theta, reciprocal frontoparietal exchange, extra frontal recruitment), and the Map reads the difference as consciousness adding something when it decides. The data fit that reading without evidencing it: a physicalist expects endogenous and exogenous control to recruit different circuits too, and the positions register grades the willed-versus-instructed data as consistent with rather than establishing conscious engagement ([[positions/agency-and-will#^p-a1|P-A1]]).`
   - Delta: **+15** (3,869 → 3,884).
   - Guards: the anchor `^p-a1` exists (`positions/agency-and-will`); keep the Rajan et al. attention framing on the page unchanged; optional sibling `mental-effort` L144 ("That something may be consciousness engaging at the selection point") is already hedged and may stay.

**Not tasked here:**
- W6, W7, W8, W9, W12, W13 and Note 8 are scope additions to open tasks (todo L3115, L2553, L1566/L3374, L2453, L3107, L3307, L2020 respectively) and are recorded under Bearing on the open items.
- W10, W11 and W14 fall below the cap; each carries its own one-line fix. W14 is the one with a same-day cause (commit `fb2967ecaf`) and is the first candidate when a slot opens.
