---
ai_contribution: 100
ai_generated_date: 2026-10-02
ai_modified: 2026-10-02 00:54:01+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-10-02
date: &id001 2026-10-02
description: 'Tenet check 143: all fifteen carried ERRORs are repaired, but 125 changed
  files yield thirteen new ones, led by a Tenet 4 cluster that misreads tenets L123/L172
  and the source of the wheelers minimality error in born-rule L197.'
draft: false
human_modified: 2026-10-02
last_curated: null
last_deep_review: null
lastmod: 2026-10-02 00:54:01+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-10-02
topics: []
---

# Tenet Alignment Check

**Date**: 2026-10-02 (check 143; previous [reviews/tenet-check-2026-09-30.md](/reviews/tenet-check-2026-09-30/) = 142)
**Files checked**: 125, every live file in `topics/ concepts/ voids/ apex/ positions/` with a commit since check 142 (2026-09-30 07:50 UTC; window baseline cc23865423). That is 54 concepts, 54 topics, 10 apex, 4 voids and 3 positions files, about 418k body words. All 125 were read in full by fourteen parallel sub-sweeps (none targeted), and every locus was grep-verified at its stated line. The driver independently re-verified every ERROR and every priority-list locus by exact substring. Ten files are new this window: `concepts/cotard-delusion`, `concepts/depersonalisation`, `concepts/thought-insertion`, `concepts/revelation-thesis`, `concepts/inference-to-the-best-explanation-against-dualism`, `concepts/quantum-factorisation-problem`, `topics/eighteenth-century-influx-debate`, `topics/outcome-devaluation-and-dual-task-costs-in-parkinsons`, `topics/covert-consciousness-and-cognitive-motor-dissociation` and `topics/colour-ontology-and-the-secondary-quality-residue`; the brief counted nine and omitted the colour page. `tenets.md` has had no commit since e3e689517d (2026-09-27). L49–147 and L149–188 were re-read, and the Rules-out clauses are unchanged.
**Errors**: 13 live, all new to the ERROR grade. Twelve are in the window: two re-surface from earlier unminted flags, and one (`mine-ness` L136) is already covered by an open P2. One is outside the window, found by the driver's corpus probe. Carried: 0. **All 15 carried ERRORs from checks 140–142 are REPAIRED.**
**Warnings**: 334 findings in the window, many bundling sibling lines. 93 files have a WARNING verdict, and the ten ERROR-verdict files carry further warnings. The 14 sweeps re-probed 199 prior loci: 61 REPAIRED, 135 STILL LIVE, 3 confirmed passing. Outside the window, 28 carried loci re-probed by the driver are still live, and two propagation tails remain open: "actually sufficient", 6 loci in 4 files, and "tenet predicts", about 15 loci.
**Notes**: 381
**Lens**: the same as checks 138–142. First, direct conflict with a Rules-out clause. Second, over-reach: a lead, alignment section or body claiming more than its argument or `tenets.md` supports, graded on the compatible / suggestive / discriminating ladder of `project/evidential-status-discipline` §Compatibility vs. Support. Third, the co-optation firewall, including the phenomenological/process roster line. Fourth, propagation: whether a repair reached its siblings. Honest "compatible, not discriminating" verdicts and lexical anchoring were not counted.

## Summary

**1. Every carried ERROR is repaired, for the first time in six reports.** Check 142's priority rows 1–3 were minted and executed on 09-30:
- 62e09be708 (group A: `born-rule` L110, `brain-internal-born-rule-testing` L157, `testing-consciousness-collapse` L179, `kabbalah` L34/L78/L84, `consciousness-and-collective-phenomena` L162, `combination-problem` L175).
- f60ad5b851 (group B: `falsification-roadmap` L173/L107, `phenomenology-of-returning-attention` L97/L39, `apex/consciousness-and-agency` L120, `haecceity` L181, `composition-and-consciousness` L111, `many-minds` L86, `quantum-consciousness` L114, `indexical-identity` L147).
- 53c0949707 (`wheelers` L156/L160, `binding-problem` L88/L132/L142/L210/L212).
- 1d5474fd41, the propagation sweep: seven classical-menu loci, four unconditioned-scoping loci, and the Frankish PCS roster at `integration-as-activity` L50.

Each repair was checked by word-diff. The old string returns zero hits and the replacement reads at the calibrated rung (table under §Errors → Carried).

**2. The repairs were sentence-local, and siblings survived in most repaired files.** The sweeps found the same defect, reworded, in a neighbouring sentence:
- At 5 of the 7 menu sites the improper-mixture qualifier now sits beside an unchanged sentence that still asserts the menu, Tenet 3 as actual, or felt choice against MWI. These are `trilemma-of-selection` L129, `attention-and-the-consciousness-interface` L173, `retrocausality` L127/L155, `mind-brain-separation` L118 ("because it *is* determining which possibility becomes real") and `apex/phenomenology-mechanism-bridge` L59, against its own L92–98.
- The "unconditioned" scope added at `brain-internal-born-rule-testing` L157 is contradicted by the unscoped L3, L106, L116 and L147 in the same file. `falsification-roadmap` L87/L142 have the same problem.
- `wheelers` L86/L178 still demote the endorsed path to "one live branch among three", which was half of the L156 ERROR. Commit 53c0949707 says it covered L142, but its diff does not touch L142.
- The grep keys missed `adaptive-computational-depth` L83 ("presents quantum-level options") and `consciousness-and-integrated-information` L78 ("no experiment measuring frequencies could detect"). Future sweeps should key on `presents .{0,20}options` and on "detect" as well as "indistinguishable".
- Three cross-file repairs did not travel:
  - `anaesthesia` L81 → `self-stultification-as-master-argument` L81
  - `delegation-meets-quantum-selection` L108/L62 → `delegatory-causation` L172/L148
  - `galilean-exclusion` L106 → `methodology-of-consciousness-research` L156 and `primary-secondary-quality-boundary` L87

**3. Thirteen new ERRORs, in four classes** (full entries under §Errors):
- **Tenet 4 and the subject posit (tenets L121, L123, L172), six loci in five files.**
  - Two files describe the agency argument and the anti-MWI case as "coherentist mutual support" or a "mutually supporting cluster", where tenets L123 says "*logical* interdependence, not mutual evidential support": `trilemma-of-selection` L131 and `self-and-self-consciousness` L166.
  - Two loci attribute content to Tenet 4 that the tenets deny: "affirms definite facts about consciousness" (`substrate-independence` L192) and "preserves the zombie intuition" (`phenomenal-concepts-strategy` L193).
  - `haecceity` L71 says Tenet 1 has "haecceitistic implications", contradicting its own repaired L181.
  - `substrate-independence` L98 gives "the dualist conclusion" a verdict on silicon that tenets L170 reserves.
- **Fabricated tenet entailments and predictions, five loci in four files.**
  - `self-stultification-as-master-argument` L153 ("directly entails three of the Map's five tenets") and L145 (Tenet 3 "grounded in the quantum interaction mechanism").
  - `sorkin-higher-order-interference` L26 ("exactly the shape Tenet 5 predicts").
  - `mine-ness` L136, already covered by open P2 todo L1656.
  - `concepts/consciousness-and-scientific-explanation` L58 (out of window). The MQI tenet "predicts … subtly different distributions … a difference currently below detection thresholds", which is the sensitivity-limit reading tenets L75 disowns. This locus has been on check 141's candidate list since 09-28 and was never swept.
- **Tenet 2 minimality, one locus.** `born-rule-and-the-consciousness-interface` L197 says the MQI tenet "strictly read, privileges whichever minimum is *actually sufficient*". This is the same redefinition counted as an ERROR in `wheelers` L156 on 09-30. The repaired wheelers now cites born-rule as its taxonomy source, so the corpus contradicts itself. Six "actually sufficient" loci in four more files carry the same reading, presented as "a live structural fork".
- **Tenet 2 Rules-out, one locus.** `death-and-consciousness` L187: "Shared death experiences suggest consciousness-to-consciousness interaction may occur outside normal sensory channels". That interaction class is excluded by tenets L83 ("not … parapsychology") and L85 (anything "empirically detectable under current experimental precision"); a prospective study the page itself requests would detect it. The 09-20 check graded it a NOTE on different grounds.

**4. Today's calibration passes (brief scope b) recalibrated bodies but left tenet paragraphs behind.**
- The CMD-ledger batches A–D fixed figures and overreads in the body text, but in `consciousness-disruption-and-the-mind-brain-interface` (L172 "production-predicted-absence", L174 "the coordinated reboot is suggestive", L178 same subject "returns"), `experimental-consciousness-science-2025-2026` (L108 biophotons as interface candidates, a claim the body withdrew on 2026-07-16; L106 "COGITATE results support the Map's fifth tenet") and `clinical-phenomenology-and-altered-experience` (L167, L135/L157 parsimony) the Relation-to-Site sections still state readings their own bodies withdrew.
- Batch B introduced one defect: `clinical-phenomenology` L125 now says "the other two cases … resist straightforward neural explanation", and one of the two is pain asymbolia, which L147 calls evidence of neural modularity.
- The thought-insertion cross-review (6e32cffa4d) made only the thought-insertion limb of `consciousness-and-the-ownership-problem`'s double dissociation reading-dependent. The depersonalisation limb (L60) and the downstream "demonstrating that ownership is a separable structural feature" (L82) are untouched, against `depersonalisation` L39.
- The kind-claim-falsifier relabel (9677abc2b8) is calibrated on all three pages. One residue, `cotard-delusion` L64 "and it passes", over-claims a guaranteed outcome.

**5. Fresh-create quality is the best yet.** The ten new pages have 0 ERRORs and 4 WARNINGs:
- `cotard-delusion` L36/L72: "at most suggestive" where the page earns only compatible.
- `revelation-thesis` L75: the phenomenal-concepts claim is folded into the "weak Revelation" that physicalists accept.
- `quantum-factorisation-problem` L80: the Tenet 4 debt is called symmetric although Level 2 is Map-only. This contests deep-review Stability Note 3, so the driver must adjudicate.
- `eighteenth-century-influx-debate` L35: the lead gives the Map's reconstruction as "the answer".

`covert-consciousness-and-cognitive-motor-dissociation` is clean. `inference-to-the-best-explanation-against-dualism` is a model of symmetric Tenet 5 handling.

**6. Reciprocal links installed this window: most are accurate, and a few over-claim their targets.**
- `apex/identity-across-transformations` L119 says CMD is "present in roughly a quarter of patients classified as unresponsive", "with full cognitive function" and is "production-predicted absence". The covert-consciousness page it now links refutes all three.
- `apex/self-construction-constructor` L86 and `topics/phenomenology-of-agency-vs-passivity` L125 (plus `phenomenology-of-recursive-self-awareness` L117) state the thought-insertion dissociation flat. Their target says it "holds only on the agency reading"; the source of the flat form is `mine-ness` L60/L82.
- `history-of-the-interaction-problem` L99 has influx "displaced" harmony; the target declines the dominance claim. `occasionalism` L58 has the same issue (NOTE).
- `mental-effort` L146 puts the Parkinson's sentence under the MQI bullet, but its target says "None of these data bear on the Minimal Quantum Interaction mechanism".
- `parsimony-epistemology` L88/L90 asserts a parity failure that the newly linked IBE page grades provisional.
- All 16 link hunks in sweep C5b's set are accurate to their targets, though two leave their host sentence in tension; 7 of 9 in C5c's set are accurate.

**7. Doctrinal items for human attention. No task is proposed; each is a canonical-source question.**
- (a) **Zeno classification.** Tenets L71 lists Stapp's quantum Zeno among proposals that "depend on pre-decoherence coherence". `topics/comparing-quantum-consciousness-mechanisms` L159 (last commit 2026-08-24) says it "sit[s] naturally inside" the post-decoherence preference. `interactionist-dualism` L135/L153 follow the comparing page, and `contemplative-path` L184 and `entanglement-binding-hypothesis` L76 attribute Zeno or microtubule interest to Tenet 2 itself. About eight T2 WARNINGs this check depend on which source is canonical.
- (b) **Minimality versus the outside-corridor fork.** Tenets L69 makes minimality empirical-constraint ("no Born-statistics violation"), yet L81 names "minimum-outside-corridor readings" as what falsifier (c) bites on, and that sentence is the textual hook for the "actually sufficient" fork. Priority row 3 resolves the dependents in L69's favour, following the 09-30 wheelers precedent. If the operator wants the fork kept open, L69 must change instead, and wheelers L156 would need reverting.
- (c) The phrase "mind prior to matter" (`kabbalah` L62/L78) appears nowhere else in the Map. It contradicts the late-arrival reading (tenets L125, L184 posit 2) but names "the Map", not a tenet, so it is held at WARNING.

**8. Check 142's priority row 4 was never minted.** All of its loci are re-verified live and unchanged (their files have no commit in the window):
- `voids/mirth-void` L94
- `voids/mattering-void` L114
- `topics/phenomenology-of-intellectual-life` L184/L186/L214/L218
- `voids/causal-interface` L110/L112/L158 (wikilink form)
- `voids/infant-consciousness` L105/L107
- `topics/incubation-effect-and-unconscious-processing` L144/L146/L148
- `topics/correlationism-and-the-ancestrality-argument` L100

**9. Grading decisions where the driver differed from a sweep.**
- Held at WARNING, by checks 141–142 precedent for the family:
  - `kabbalah` L62/L78 ("mind is prior to matter"; names the Map, not a tenet)
  - `causal-closure-debate-historical-survey` L115 (coherence closure stated as the Map's falsifier; precedent `the-interface-problem` L147)
  - `phenomenal-acquaintance` L42/L96 (Tenet 1 glossed as substance dualism; precedent `brain-specialness-boundary` L63)
  - `interaction-problem-across-traditions` L98 and `qualia` L205 (sweeps called both borderline)
- Kept at ERROR: `self-stultification` L145, because tenets L95 states the contrary in so many words.
- A sweep claimed that `phenomenal-concepts-strategy` L193 has an archive sibling. The phrase has 0 hits in `archive/topics/phenomenal-concepts-as-materialist-response.md`, so no archive action is owed.

## Errors

Every string below was re-verified by the driver with an exact-substring grep (one hit at the stated line). Line numbers are as of 2026-10-02 00:45 UTC.

### New (13)

1. **[topics/born-rule-and-the-consciousness-interface.md](/topics/born-rule-and-the-consciousness-interface/) L197** (Tenet 2; contradicts tenets L69).
   - Quote: "The Minimal Quantum Interaction tenet, strictly read, privileges whichever minimum is *actually sufficient*, which is why the corridor is a working hypothesis".
   - Tenets L69 says the minimality is empirical-constraint ("no Born-statistics violation") and that "The Map does not claim that within those constraints the smallest interaction is most likely true".
   - It also contradicts the page's own L114 and L217.
   - Same class as 09-30 #1 (`wheelers` L156, repaired), whose new text cites this page.
   - Sibling L167: "read as \"smallest interaction actually sufficient\"".
2. **[concepts/substrate-independence.md](/concepts/substrate-independence/) L192** (Tenet 4 misstated; tenets L121, L172, matrix L159–161).
   - Quote: "The No Many Worlds tenet affirms definite facts about consciousness." The paragraph then argues that "is this silicon system conscious?" "becomes ambiguous across branches".
   - Tenets L121 endorses the non-deflationary "I" "not from within this tenet". L172 says determinate first-person facts are available branch-relatively. All three machine-consciousness rows mark No-MWI "Not invoked".
   - First flagged by the 09-19 check (item 7); never minted.
3. **[concepts/substrate-independence.md](/concepts/substrate-independence/) L98** (Tenet 1 verdict; tenets L170).
   - Quote: "Silicon systems, implementing causal structures without the non-physical component, lack what matters." It is introduced as "The dualist conclusion".
   - Tenets L170: irreducibility "is what leaves open which physical systems an experiencer can couple with". The page's own L48 says the same.
4. **[concepts/self-and-self-consciousness.md](/concepts/self-and-self-consciousness/) L166** (tenets L123).
   - Quote: "haecceity, No Many Worlds, and Bidirectional Interaction form a mutually supporting cluster the alternative reading would dissolve simultaneously".
   - Tenets L123: "*logical* interdependence, not mutual evidential support … neither is independent support for the other". L184: the three "are not mutually independent".
5. **[topics/trilemma-of-selection.md](/topics/trilemma-of-selection/) L131** (tenets L123).
   - Quote: "The relationship is one of coherentist mutual support rather than linear derivation—neither argument grounds the other, but they stand or fall together".
   - The relata are the trilemma (the agency route) and the Map's case against many-worlds, which is exactly the pair tenets L123 describes in the opposite terms.
6. **[concepts/haecceity.md](/concepts/haecceity/) L71** (Tenet 1; tenets L53, L184 posit 1).
   - Quote: "The Map's Dualism tenet treats consciousness as irreducible to physical processes. This commitment has haecceitistic implications."
   - Tenets L184 places primitive subject individuation *beneath* the tenets, as a posit they draw on. The page's own repaired L181 now says the tenets "presuppose haecceity … rather than imply it".
   - Same-step siblings: L75 "The difference must be non-qualitative" (a non sequitur, because phenomenal properties are qualitative), L153, and L187 "haecceity provides the individuating principle".
7. **[topics/self-stultification-as-master-argument.md](/topics/self-stultification-as-master-argument/) L153** (fabricated entailment; tenets L55, L93, L101, L145).
   - Quote: "This commitment directly entails three of the Map's five tenets:".
   - The page's own L155 adds a further premise ("and physical causation alone cannot track normative relationships"), so "directly" fails on its own text.
8. **[topics/self-stultification-as-master-argument.md](/topics/self-stultification-as-master-argument/) L145** (Tenet 3 grounding; tenets L93, L95).
   - Quote: Tenet 3 is "a commitment grounded in the quantum interaction mechanism and evolutionary evidence, not solely in self-stultification".
   - Tenets L93: "supported by self-stultification and indirect evidence". L95: downward causation is "a posit the interface argument leaves open, not a result it secures".
   - Graded at the ERROR/WARNING border and kept at ERROR.
9. **[concepts/sorkin-higher-order-interference.md](/concepts/sorkin-higher-order-interference/) L26** (fabricated Tenet 5 prediction, in the lead).
   - Quote: "The bound is real, tightening, and silent about the brain: exactly the shape Tenet 5 predicts." (wikilink form).
   - Tenet 5 is a defeasibility claim about parsimony (tenets L131–147) and predicts nothing.
10. **[topics/death-and-consciousness.md](/topics/death-and-consciousness/) L187** (Tenet 2 Rules-out; tenets L83, L85).
    - Quote: "Shared death experiences suggest consciousness-to-consciousness interaction may occur outside normal sensory channels when the filtering apparatus is compromised."
    - The sentence sits in the Tenet 3 paragraph but is not Tenet 3 content (tenets L91: consciousness biasing outcomes in the brain).
    - The 09-20 check graded it a NOTE as "off-target for Tenet 3". It is regraded here on the L83/L85 ground, which that check did not raise.
11. **[concepts/phenomenal-concepts-strategy.md](/concepts/phenomenal-concepts-strategy/) L193** (Tenet 4; tenets L172).
    - Quote: "The Map's rejection of many-worlds preserves the zombie intuition in its original force."
    - Tenets L172 says branching "leaves the conceivability of a zombie twin or an inverted spectrum untouched".
    - Flagged by check 2026-08-01 as its top priority; never minted.
12. **[concepts/mine-ness.md](/concepts/mine-ness/) L136** (fabricated Dualism prediction; tenets L53).
    - Quote: "The Dualism tenet finds direct support in mine-ness's separability" … "is exactly what dualism predicts".
    - **Covered by the open P2 at todo L1656** ("Bring mine-ness's Dualism verdict down…"). It is not in the priority list.
13. **[concepts/consciousness-and-scientific-explanation.md](/concepts/consciousness-and-scientific-explanation/) L58** (out of window; Tenet 2, tenets L75, L81).
    - Quote: "a conscious system and an unconscious but physically similar system would show subtly different distributions of quantum outcomes — a difference currently below detection thresholds" … "The prediction could in principle be tested as measurement technology advances".
    - Tenets L75: indistinguishable on the unconditioned aggregate "by construction, not by any sensitivity limit".
    - Same class as check 140's `brain-internal` L157 "instrument-relative" (repaired 09-30).
    - It has been on the 09-28 candidate list since then and was never swept.

### Carried (0): all fifteen REPAIRED

| 09-30 # | Locus | Repair | Replacement now reads |
|---|---|---|---|
| 1 | `wheelers` L156 | 53c0949707 | "minimal in the empirical-constraint sense: no Born-statistics violation, indistinguishable from chance under any unconditioned aggregate test" |
| 2 | `composition-and-consciousness` L111 | f60ad5b851 | "irreducible—not explained in terms of something physical … states irreducibility rather than fundamentality" |
| 3 | `falsification-roadmap` L173, L107 | f60ad5b851 | "would erode the indirect evidence Tenet 3 rests on, not falsify a prediction it makes"; "at an *external* RNG—outside the brain-locality Tenet 3 concerns" |
| 4 | `phenomenology-of-returning-attention` L97 | f60ad5b851 | "consistency with the tenet rather than a prediction the tenet alone makes" |
| 5 | `apex/consciousness-and-agency` L120 | f60ad5b851 | "consistent with … though the narrowness comes from the agent-causal constraints rather than from the tenet" |
| 6 | `haecceity` L181 | f60ad5b851 | "presuppose haecceity about conscious subjects rather than imply it" |
| 7 | `many-minds-interpretation` L86 | f60ad5b851 | "biases which single outcome is realised … while leaving the aggregate statistics Born" |
| 8 | `quantum-consciousness` L114 | f60ad5b851 | "leaves room for the Map's outcome-selection posit without supplying evidence for it" |
| 9 | `indexical-identity-quantum-measurement` L147 | f60ad5b851 | "biases which of the physically possible, already-decohered outcomes becomes actual—and that outcome is actual for everyone" |
| 10 | `kabbalah-tzimtzum` L78 (+L34, L84) | 62e09be708 | "a divergence located in the substance lean … not in Tenet 1, whose irreducibility claim a mind-first monism satisfies" |
| 11 | `consciousness-and-collective-phenomena` L162 | 62e09be708 | "The Map's interface model — not the Dualism tenet, which asserts irreducibility and predicts nothing about which systems host consciousness — leads one to expect" |
| 12 | `combination-problem` L175 | 62e09be708 | "irreducible … though not, for the Map, a basic feature present from the start" |
| 13 | `born-rule` L110 (+L219) | 62e09be708 | "Baseline actuality is physical … the Map posits only that consciousness biases neural outcomes"; "permits, without establishing, bidirectional causation" |
| 14 | `brain-internal-born-rule-testing` L157 | 62e09be708 | "insulation from unconditioned tests is by construction, not instrument-relative" |
| 15 | `testing-consciousness-collapse` L179 | 62e09be708 | "is compatible with, not evidence for, consciousness being structurally implicated in measurement" |

**Booked, not recounted:** `concepts/implicit-memory` L194 ("The simplest account that covers…") is still live, under the blocked `NEEDS-HUMAN (doctrine) 2026-09-19` item.

## Priority list (capped at 4; ready to mint)

Word costs are body words from `tools.curate.length.analyze_length`. The gate is the section's hard threshold, crossed at `>=`. Headroom = hard − 1 − words.

**1. refine-draft: Tenet 4 and the subject posit misstated (six ERRORs, five files; tenets L121, L123, L172, L170).**
- [topics/trilemma-of-selection.md](/topics/trilemma-of-selection/) L131 (3076/4000, headroom 923). "The relationship is one of coherentist mutual support rather than linear derivation" → "The relationship is logical interdependence, not mutual evidential support" (−3). Same paragraph, L129: append ", or with the positions set aside above" to "Without this bidirectionality, we are left with Horns 1 or 2." (+7).
- [concepts/self-and-self-consciousness.md](/concepts/self-and-self-consciousness/) L166 (3537/3500, **38 over: net-negative required**). Replace "form a mutually supporting cluster the alternative reading would dissolve simultaneously" with "share one root, the subject the Map posits, which the alternative reading would dissolve; none independently supports the others" (+5). In the same paragraph group, cut L192's "Many-worlds' proliferation of subjects undermines the determinacy self-consciousness presupposes." (Family I against tenets L172; −9), so the file lands net-negative. Open P3 todo L1702 also wants a trim from this file; keep the two trims distinct.
- [concepts/substrate-independence.md](/concepts/substrate-independence/) (3661/3500, **162 over**):
  - L192: replace the No Many Worlds paragraph with: "The No Many Worlds tenet is not invoked by the substrate question (tenets matrix, machine-consciousness rows): whether a system is conscious is determinate branch-relatively even under many-worlds, so the tenet bears on this page as coherence only." (−43)
  - L98: delete "Silicon systems, implementing causal structures without the non-physical component, lack what matters." (−12)
  - L184: "jointly entail substrate skepticism" → "motivate substrate skepticism about bidirectionally coupled consciousness" (+2)
  - Net −53.
- [concepts/haecceity.md](/concepts/haecceity/) (3451/3500, headroom 48):
  - L71: "This commitment has haecceitistic implications." → "This commitment is hospitable to haecceitism without implying it." (+4)
  - L75: "The difference must be non-qualitative" → "The difference is phenomenal; haecceity enters when one asks what makes *this* subject, rather than a phenomenal duplicate, the one here" (+5)
  - L187: "haecceity provides the individuating principle" → "haecceity is the Map's posited individuating principle" (+2)
  - L191: "Consciousness's causal role implies its particularity" → "…presupposes rather than implies its particularity" (+2)
  - Net about +13.
- [concepts/phenomenal-concepts-strategy.md](/concepts/phenomenal-concepts-strategy/) (3477/3500, headroom 22):
  - L193: replace "The Map's rejection of many-worlds preserves the zombie intuition in its original force." and the sentence before it ("Many-worlds interpretations complicate indexicality…") with "An Everettian grants determinate first-person facts branch-locally, so branching leaves zombie conceivability untouched; Tenet 4 rests on the indexical objection, not on this argument." (about −2)
  - Fund it by deleting L187 "The persistence of the debate after decades of sophisticated work suggests the gap reflects something real" (−18; PCS predicts the persistence, per the page's own L53).
- Brief note: name the *claim* (tenets L123 "logical interdependence, not mutual evidential support"; L172 Tenet 4 not invoked for conceivability or substrate), require a same-file sibling grep for `mutual`, `mutually supporting`, `affirms definite`, `implications`, `implies its`, and check the Hugo copies.

**2. refine-draft: fabricated tenet entailments and predictions (four ERRORs, three files).**
- [topics/self-stultification-as-master-argument.md](/topics/self-stultification-as-master-argument/) (3451/4000, headroom 548). Last deep review 2026-07-12; the brief's "deep-reviewed 09-30" is a mislabel.
  - L153: "This commitment directly entails three of the Map's five tenets:" → "This commitment bears on three of the Map's five tenets, each through a further premise:" (+5)
  - L145: "a commitment grounded in the quantum interaction mechanism and evolutionary evidence, not solely in self-stultification" → "a commitment held on self-stultification and indirect evidence, the quantum interface showing such causation available rather than actual" (+3)
  - L81: port the 09-30 anaesthesia repair. Replace "would presuppose the very causal efficacy epiphenomenalism denies" with "would look self-stultifying; the phenomenal-concept strategy can ground them in correlation alone, so the case constrains, without defeating, epiphenomenalism" (about +7).
  - Net about +15.
- [concepts/sorkin-higher-order-interference.md](/concepts/sorkin-higher-order-interference/) (2217/3500, headroom 1282):
  - L26: "exactly the shape Tenet 5 predicts." → "exactly where Tenet 5's caution against extrapolating a simple result applies." (+4)
  - L76: "a consciousness-interface proposal would need" → "a pre-decoherence interface proposal would need" (+1; tenets L77)
- [concepts/consciousness-and-scientific-explanation.md](/concepts/consciousness-and-scientific-explanation/) L58 (2468/3500, headroom 1031; out of window):
  - Replace "In principle, this means a conscious system and an unconscious but physically similar system would show subtly different distributions of quantum outcomes — a difference currently below detection thresholds." with "On the corridor reading the Map endorses, the unconditioned aggregate stays Born by construction, not by any sensitivity limit; only a deviation conditioned on intention, task or subject would test it ([P-Q3](/positions/quantum-interface/#p-q3))." (about +4)
  - Replace "The prediction could in principle be tested as measurement technology advances, but no concrete experimental protocol currently exists." with "No such conditioned protocol yet exists." (−13)
  - "tenet predicts that consciousness biases" → "tenet holds that consciousness biases" (0)
  - Net about −9.
- Exclude `mine-ness` L136 (open P2 L1656).
- Brief note: grep each file for every sentence in which a tenet, by name, *predicts*, *entails*, *requires* or *implies* something, and check each against `tenets.md`.

**3. refine-draft: Tenet 2 minimality read as "smallest actually sufficient" (one ERROR plus its tail; grep key `actually sufficient`).**
- [topics/born-rule-and-the-consciousness-interface.md](/topics/born-rule-and-the-consciousness-interface/) (5445/4000, **1446 over: net ≤ 0**):
  - L197: "The Minimal Quantum Interaction tenet, strictly read, privileges whichever minimum is *actually sufficient*, which is why the corridor is a working hypothesis" → "The Minimal Quantum Interaction tenet's minimality is empirical-constraint minimality—no Born-statistics violation on the unconditioned aggregate—so the corridor is the endorsed working hypothesis" (about −1)
  - L167: attribute the "read as \"smallest interaction actually sufficient\"" premise to the family ("on this family's reading, not Tenet 2's") (+5)
  - Offset with L219 "The trilemma-of-selection supports this:" → "The trilemma adds a heuristic, not a proof:" (−1; it re-inflates the repaired "permits, without establishing"), and cut "on their own terms" at L221 (−4).
  - Net about 0.
- Tail, same change on each: never call the corridor/outside-corridor split "a live structural fork, not a settled commitment" or Tenet 2 "read as smallest actually sufficient". State that the corridor is the reading Tenet 2's empirical-constraint minimality endorses (tenets L69, L71), and that outside-corridor readings are fallbacks accepting a sub-detection Born departure, which falsifier (c) bites on (L81). Loci:
  - [concepts/ensemble-level-epiphenomenalism.md](/concepts/ensemble-level-epiphenomenalism/) L59, L77 (2412/3500, headroom 1087; in window; sweep C5a passed L77, the driver overrules)
  - [concepts/causal-consistency-constraint.md](/concepts/causal-consistency-constraint/) L95 (2494/3500)
  - [topics/consciousness-and-probability-interpretation.md](/topics/consciousness-and-probability-interpretation/) L97 (3219/4000)
  - [apex/born-preserving-causal-efficacy.md](/apex/born-preserving-causal-efficacy/) L123, L189 (5149/5000, 150 over and **under the NEEDS-HUMAN length block, todo L432**: net-negative only, otherwise record and skip)
  - The four false positives ("counterfactually sufficient" in `trumping-preemption`, `four-quadrant-dualism-taxonomy`, `interventionist-and-counterfactual-dualism`, `mechanism-costs-dualism-thickness-quadrants`) must not be touched.
- [topics/wheelers-participatory-universe-and-it-from-bit.md](/topics/wheelers-participatory-universe-and-it-from-bit/) (3995/4000, headroom 4):
  - L86 "the Map now holds the corridor reading alongside two alternatives" → "holds the corridor reading as its endorsed path, with two fallbacks" (−1)
  - L178 "one live branch among three" → "the endorsed branch, with two fallbacks" (−2)
- See Summary 7(b) for the doctrinal caveat (tenets L81's wording).

**4. refine-draft: CMD-ledger follow-through. Today's tenet sections are stranded behind recalibrated bodies, plus the death-and-consciousness ERROR (four files).**
- [topics/death-and-consciousness.md](/topics/death-and-consciousness/) (3552/4000, headroom 447):
  - L187: delete "Shared death experiences suggest consciousness-to-consciousness interaction may occur outside normal sensory channels when the filtering apparatus is compromised." (−19; tenets L83/L85)
  - L189: replace "The deeply personal quality of death phenomenology … reinforces that indexical identity matters" with "The personal particularity of death phenomenology is what each branch would also contain; it shows the stakes, not the case" (about −8; tenets L172, and the page's own L69)
- [topics/consciousness-disruption-and-the-mind-brain-interface.md](/topics/consciousness-disruption-and-the-mind-brain-interface/) (3889/4000, headroom 110):
  - L172: rename "production-predicted-absence-yet-observed-presence" → "behaviour-predicted-absence-yet-observed-presence", and "a straightforward production reading predicts" → "behavioural or subtraction inference predicts" (±0)
  - L174: "the coordinated reboot is suggestive: a dedicated reopening mechanism is what one would expect" → "the coordinated reboot is compatible with the brain re-establishing an interface, though production accounts accommodate it equally" (−9; against own L146)
  - L178: "and the same indexical subject returns afterward—not merely a similar observer in a related branch" → "and the Map holds that the same indexical subject returns; no report could distinguish this from branch-relative continuation" (+8)
  - L130: "We can prove presence" → "Neuroimaging can make presence probable" (+3)
  - Net about +2. Do not touch L3 or the IIT/falsifier loci; open P2 todo L1729 owns them, so merge if both are picked together.
- [topics/experimental-consciousness-science-2025-2026.md](/topics/experimental-consciousness-science-2025-2026/) (2588/4000, headroom 1411):
  - L108: "Both identify quantum-level processes in the brain that could serve as the interface" → Keppler as a coherence-dependent fallback candidate, and extracranial biophoton detection "not yet established as cortical (above)" (+12; body L66)
  - L80: "provides a concrete physical mechanism for what the Map's MQI tenet requires" → "…for the coherence-dependent fallbacks the tenet registers; the endorsed post-decoherence route does not need it" (+8; tenets L71/L77)
  - L106: "The COGITATE results support the Map's fifth tenet" → "illustrate the condition the fifth tenet names" (±0)
  - L112: "more resilient, more fundamental, and less reducible than physicalist frameworks predict" → "compatible with the Map's framework … none discriminates the interface model from its physicalist rivals" (−11)
  - Net about +9.
- [topics/clinical-phenomenology-and-altered-experience.md](/topics/clinical-phenomenology-and-altered-experience/) (3583/4000, headroom 416):
  - L125 (introduced by 966607deba): "In the other two cases, the experiential disruption is systematic and selective in ways that resist straightforward neural explanation" → "In DID the experiential disruption is out of scale with its neural correlates; pain asymbolia, by contrast, has a well-mapped substrate (below)" (±0)
  - L167: "generates doubly grounded evidence for channel-specific interface architecture" → "is compatible with a channel-specific interface but, as the convergence section concedes, does not adjudicate between interface and substrate readings" (±0)

**Runners-up (not ranked, not for minting from this report):**
- `consciousness-and-the-ownership-problem` L82/L60: completes 6e32cffa4d across the depersonalisation limb.
- `methodology-of-consciousness-research` L156/L62/L152/L128/L104 plus `primary-secondary-quality-boundary` L87: the galilean-exclusion repair propagation.
- Fresh-create residues: `cotard-delusion` L36/L72/L64, `revelation-thesis` L75 (never deep-reviewed), `quantum-factorisation-problem` L80/L98 (contests Stability Note 3), `eighteenth-century-influx-debate` L35/L51/L93.
- Check 142's unminted row 4 (Summary 8).
- `apex/phenomenology-of-consciousness-doing-work` L175/L76/L78 (live since check 140).
- `concepts/qualia` L205/L213: the page tenets L172 names, contradicting that matrix entry.
- `parsimony-case-for-interactionist-dualism` L136/L144/L109.
- The Family I "nothing to select" pattern across about 15 files. The model wording is at `contemplative-path` L196 and `phenomenology-of-agency-vs-passivity` L171.

## Warnings

The sweeps grep-verified every locus at the stated line. The driver re-verified the loci named in the priority list. Line numbers are as of 2026-10-02 00:45 UTC.

### Families in this window

- **Tenet 3 held as actual, or epiphenomenalism/illusionism reported refuted (tenets L93, L95, L101, L103): the largest family**, densest in the agency/effort and quantum wings. Representative loci:
  - `apex/post-decoherence-selection-programme` L171 "Post-decoherence selection is the mechanism by which consciousness causally influences the physical world" (carried since 09-27)
  - `apex/phenomenology-of-consciousness-doing-work` L175 "consciousness does genuine work … fits the evidence better"
  - `mind-brain-separation` L118
  - `quantum-consciousness` L52 "without surrendering causal efficacy" (a residue of the f60ad5b851 repair)
  - `interactionist-dualism` L195 "eliminativism about *that* is incoherent"
  - `epiphenomenalism` L102/L116 "could never have entered the physical world"
  - `mental-effort` L94 "and so does causal work", in the paragraph the evidential-status discipline quotes as its model
  - `self-opacity` L139
  - `ethics-under-dualism` L198
  - `phenomenal-authority-and-first-person-evidence` L209
- **Compatibility upgraded to support, evidence, prediction or explanation (evidential-status ladder): about as large.** Representative loci:
  - `degrees-of-consciousness` L100/L114: "discriminates between production and interface models"; "support dualism". This is the canonical filter-vs-REBUS failure in its plainest form.
  - `apex/taxonomy-of-voids` L97/L233, against its own L197.
  - `consciousness-disruption` L172.
  - `experimental-consciousness-science` L112.
  - `neuroplasticity` L34 (lead).
  - `brain-computer-interfaces` L143/L145/L147.
  - `qbism` L109.
  - `quantum-holism-and-phenomenal-unity` L176, live through four checks.
- **Tenet 2: coherence dependence attributed to the Map, classical menu, unscoped indistinguishability, mechanism stated as fact, minimality misread (tenets L69, L71, L75, L77, L91).**
  - Coherence dependence: `causal-closure-debate-historical-survey` L115 and `the-epiphenomenalist-threat` L143–151 make neural coherence the Map's falsifier, with 0 mentions of post-decoherence selection. Also `epistemology-of-mechanism` L69, `personal-identity` L161, `attention-and-the-consciousness-interface` L153, `filter-theory` L125, `integrated-information-theory` L201, `substrate-independence` L118/L122/L172, `apex/consciousness-and-agency` L90 (0 "post-decoherence" in the apex) and `russellian-monism` L141.
  - Classical menu: `adaptive-computational-depth` L83, `pairing-problem` L122, `dopamine-and-the-unified-interface` L207, `predictive-processing-and-dualism` L52/L54.
  - Unscoped indistinguishability: `consciousness-and-integrated-information` L78, `conservation-laws` L168, `the-epiphenomenalist-threat` L133, `judging-the-map-as-science` L86/L142.
  - Context-selection as the Map's mechanism: `adaptive-computational-depth` L81, `neuroplasticity` L152, `apex/phenomenology-mechanism-bridge` L114/L116, `testing-consciousness-collapse` L153.
- **Family I: felt definiteness against MWI, or a quick "nothing to select" without branch-relative agency (tenets L117, L121, L172, L184 posit 3).** Representative loci:
  - `concepts/many-worlds` L186/L128 (the file has 0 hits for "agency")
  - `predictive-processing-and-dualism` L150 (third check running; survived the 09-30 deep review)
  - `self-opacity` L163
  - `motor-selection` L210
  - `dopamine` L211
  - `history-of-the-interaction-problem` L142
  - `interaction-problem-across-traditions` L98 (also misgrounds Tenet 4 as protecting mental causation)
  - `qualia` L213 (undoes its own L211 concession)
  - `mine-ness` L144
  - `apex/identity-across-transformations` L145/L147
  - `apex/phenomenology-mechanism-bridge` L174
  - `conservation-laws` L190
  - `measurement-problem` L117
  - `sorkin` L74
  - `ethics-under-dualism` L204
  - `death-and-consciousness` L189
- **Tenet 1 glossed as substance dualism or fundamentality (tenets L53, L57).**
  - Substance: `phenomenal-acquaintance` L42/L96 ("but for substance dualism", live since February), `russellian-monism` L99, `kabbalah` L62.
  - Fundamentality: `integrated-information-theory` L39/L196, `attention-and-the-consciousness-interface` L102, `contemplative-path` L150, `intrinsic-nature` L81, `parsimony-case` L136 ("co-fundamental", inherited from `bi-aspectual-ontology` L61).
  - "In kind": `the-steelman-for-process-monism` L85.
- **Tenet 5 as verdict, or asymmetric parsimony (tenets L145, L147).** Loci:
  - `methodology-of-consciousness-research` L156, the exact defect repaired at galilean L96
  - `philosophy-of-science-under-dualism` L118
  - `qualia` L217
  - `clinical-phenomenology` L135/L157
  - `ethics-under-dualism` L103
  - `interactionist-dualism` L192
  - `consciousness-and-causal-powers` L196
  - `brain-computer-interfaces` L151
  - `combination-problem` L187
  - `parsimony-epistemology` L60 (on Tenet 5's own page; counts physicalism's brute facts and not dualism's)
  - `retrocausality` L153 (Tenet 2 minimality read as parsimony)
  - `kabbalah` L70
- **Co-optation, mostly the new phenomenological/process line (Whitehead): 13 loci without a stance sentence.** These are `integrated-information-theory` L170, `substrate-independence` L154, `many-worlds` L140, `binding-problem` L157, `apex/consciousness-and-agency` L100, `haecceity` L131, `phenomenal-concepts-strategy` L165–169, `contemplative-path` L150, `process-philosophy` L158, `mind-brain-separation` L108, `integration-as-activity` L38, `consciousness-and-integrated-information` L150 and `methodology-of-consciousness-research` L152/L70 (Husserl, Thompson). On the PP roster, `filter-theory` L87 recruits REBUS (Carhart-Harris and Friston) with no stance line, on the filter-theory page itself.
- **Access/phenomenal (evidential-status L319).** Loci:
  - `apex/consciousness-and-agency` L132 (CBT, with a fabricated physicalist prediction)
  - `epiphenomenalism` L148
  - `the-epiphenomenalist-threat` L95
  - `qualia` L62 (placebo)
  - `phenomenal-transparency-opacity-spectrum` L121
  - `phenomenal-quality-void` L130
  - `contemplative-path` L126/L136
  - `phenomenology-of-agency-vs-passivity` L101 (choking)
  - `apex/taxonomy-of-voids` L199 (placebo/choking)
  - `falsification-roadmap` L105 (baseline cognition)
- **Normative gate (evidential-status L404).** `ethics-under-dualism` L55/L210 present shared sentientist verdicts as distinctive to dualism. L167 says "more demanding" with no divergence case.

### Per-file index (window; sweep IDs A1–C5d; E = ERROR, W = WARNING lines, N = NOTE lines)

New this window (sweeps A1–A2):
- `concepts/cotard-delusion` W L36/L72; N L64, L68, L74
- `concepts/depersonalisation` N L89
- `concepts/thought-insertion` N L108
- `concepts/revelation-thesis` W L75; N L53
- `concepts/inference-to-the-best-explanation-against-dualism` N L68/L92, L70
- `concepts/quantum-factorisation-problem` W L80; N L98, L76
- `topics/eighteenth-century-influx-debate` W L35; N L51, L93, L87/L73, L33, L97
- `topics/outcome-devaluation-and-dual-task-costs-in-parkinsons` N L93
- `topics/colour-ontology-and-the-secondary-quality-residue` N L84/L94

Calibration passes edited 10-01 (B1–B2):
- `topics/consciousness-disruption-and-the-mind-brain-interface` W L172/L3, L174, L178, L130; N L193, L142, L110, L148, L172
- `topics/locked-in-syndrome-as-the-negative-case-where-filter-loosening-does-not-apply` N L111, L72
- `topics/clinical-phenomenology-and-altered-experience` W L167, L135/L157, L3/L119, L125, L95, L137; N L143, L103, L187
- `topics/death-and-consciousness` E L187; W L189; N L183, L185, L3/L51/L111/L119
- `topics/ethics-under-dualism` W L55/L210, L198, L204, L135/L200, L167, L103/L206; N L202
- `topics/experimental-consciousness-science-2025-2026` W L108, L80, L106, L112/L38/L3, L74, L100; N L84/L88, L94, L110
- `topics/consciousness-and-the-ownership-problem` W L82, L3/L68/L74, L130; N L96, L80, L132
- `concepts/active-reboot` W L95, L101; N L39, L99, L97
- `concepts/filter-theory` W L87, L174, L125; N L178, L83, L109, L148, L97, L184, L117
- `concepts/integrated-information-theory` W L39/L196, L138, L170, L201; N L146, L152
- `concepts/degrees-of-consciousness` W L100/L96, L114, L118, L120, L122, L38; N L68, L116, L54, L110
- `concepts/qbism` W L109; N L115, L101, L133, L127, L79
- `concepts/substrate-independence` E L98, L192; W L184, L114/L126, L118/L122/L172/L190, L128, L150, L154–156, L162; N L46, L86, L180, L188, L148
- `concepts/self-and-self-consciousness` E L166; W L134/L190, L192, L194; N L148, L174, L68, L140, L188, L118
- `voids/self-opacity` W L163, L139, L159, L165; N L161, L153, L71

Substantive window edits (C1–C2):
- `concepts/galilean-exclusion` N L68, L66 (09-30 loci L92/L94/L96 REPAIRED; co-optation fix verified)
- `apex/taxonomy-of-voids` W L97, L233, L199; N L231, L237, L213, L8, L173
- `topics/predictive-processing-and-dualism` W L150, L52/L54, L146, L144, L130, L128; N L148, L104, L74/L136, L144, L98
- `concepts/cross-mechanism-convergence` W L97; N L59, L81
- `topics/primary-secondary-quality-boundary` W L87; N L43/L91, L85, L73
- `topics/methodology-of-consciousness-research` W L156, L62/L152, L128, L152/L70, L104, L118, L132, L124, L154; N L70, L62/L78, L138, L126
- `apex/judging-the-map-as-science` W L86/L142; N L120/L140, L64/L120
- `topics/delegation-meets-quantum-selection` W L84, L104; N L106, L108, L124, L3
- `concepts/delegatory-causation` W L172, L122, L148, L132/L134, L136, L150; N L51, L206, L176, L136, L146
- `positions/ai-substrate-verdicts` N L41 (feed-forward basis ground; matrix row unnamed). All four 09-30 positions-evolve fixes HOLD.
- `positions/subject-census` N L59 ("einselected menu"), L71
- `topics/self-stultification-as-master-argument` E L153, L145; W L81, L143, L149, L165; N L49, L75, L95, L135, L167
- `topics/anaesthesia-and-the-consciousness-interface` N L81, L145, L99, L109 (09-30 loci L79/L143 REPAIRED)
- `topics/emergence-as-universal-hard-problem` W L113, L111 (both carried from check 140); N L61, L115, L109, L93, L37

Repaired-ERROR files (C3a–C3b):
- `topics/born-rule-and-the-consciousness-interface` E L197; W L219; N L221, L165/L217, L167/L170/L207/L209
- `topics/brain-internal-born-rule-testing` W L3/L106/L116/L147, L120; N L151, L66, L122
- `topics/testing-consciousness-collapse` W L149, L232, L213–216; N L153, L121, L159
- `topics/many-minds-interpretation` W L84, L88; N L98, L86, L48
- `concepts/many-worlds` W L186/L128, L108, L140; N L57, L63/L82, L45/L188, L170, L182
- `concepts/quantum-consciousness` W L52, L58, L60, L152, L73, L144; N L186/L192, L188, L94, L128
- `topics/indexical-identity-quantum-measurement` W L127/L131; N L129, L163, L153, L109, L182
- `topics/wheelers-participatory-universe-and-it-from-bit` W L86/L178, L142; N L156, L148
- `topics/falsification-roadmap-for-the-interface-model` W L87/L142, L95, L105, L125; N L111, L157, L163
- `concepts/binding-problem` W L210, L116, L136, L157, L165/L167/L172; N L142, L208, L206, L214, L178, L102
- `concepts/composition-and-consciousness` W L83/L43, L127, L121; N L111, L75, L123
- `topics/phenomenology-of-returning-attention` W L144, L146; N L97 ("below" should be "above"), L3, L83, L99
- `apex/consciousness-and-agency` W L90, L88/L94, L100, L132, L110, L114, L134/L158; N L112, L92, L142
- `concepts/haecceity` E L71 (+L75/L153/L187); W L191, L193, L143, L131; N L133, L85, L43
- `topics/kabbalah-tzimtzum-consciousness-matter` W L62/L78 (held from ERROR), L62 substance, L70; N L34/L72/L76
- `topics/consciousness-and-collective-phenomena` W L164, L154, L52, L62, L158; N L162, L166, L170, L104, L74
- `concepts/combination-problem` W L185, L187, L163; N L157, L142, L126

Propagation-sweep files (C4a–C4b):
- `topics/trilemma-of-selection` E L131; W L76, L54, L91, L113, L127, L129, L99; N L125, L131, L133, L119, L109, L127
- `topics/attention-and-the-consciousness-interface` W L57, L102, L153, L169, L173; N L135, L149, L141
- `topics/brain-computer-interfaces-and-the-interface-boundary` W L77, L151, L143, L145, L147; N L149, L83, L75, L121, L109
- `concepts/neuroplasticity` W L34, L119, L144, L148, L152; N L117, L138, L154, L95
- `concepts/retrocausality` W L127, L103, L54/L58, L153; N L56, L95, L121, L157, L99/L139, L155
- `concepts/mind-brain-separation` W L118, L112, L116, L108; N L42, L78, L98
- `apex/phenomenology-mechanism-bridge` W L174, L176, L132, L144/L140/L148, L102/L138, L114/L116, L168/L81/L73; N L59, L79, L170, L130
- `topics/valence-and-conscious-selection` N L208, L182, L59, L127
- `topics/epistemology-of-mechanism-at-the-consciousness-matter-interface` W L69/L121, L91, L125; N L97–99, L53, L43
- `concepts/sorkin-higher-order-interference` E L26; W L74, L76; N L76
- `topics/the-steelman-for-process-monism` W L85/L33; N L89, L87
- `topics/personal-identity` W L161, L131/L133, L53, L193; N L85, L191
- `concepts/integration-as-activity` W L38, L62; N L48, L64, L56/L117, L134
- `concepts/adaptive-computational-depth` W L83, L81, L65/L67, L79/L33, L87; N L99, L85/L103
- `concepts/measurement-problem` W L67, L67/L187, L117, L197, L125; N L61, L63
- `topics/consciousness-and-integrated-information` W L78/L82, L80/L82, L62, L150, L158, L168, L178; N L52/L60/L176, L84, L120, L180, L158

Rest of the window (C5a–C5d):
- `apex/assessing-ai-consciousness-under-the-map` W L116 (gate-class arguments [P-AS1](/positions/ai-substrate-verdicts/#p-as1) retired on 09-30)
- `apex/contemplative-path` W L126/L136, L134/L136, L190, L150, L184; N L94, L192, L130, L118, L64
- `apex/identity-across-transformations` W L119, L145/L147, L149; N L157, L193, L117
- `apex/phenomenology-of-consciousness-doing-work` W L175, L76, L78, L117/L119; N L171, L183/L184/L186, L141, L155
- `apex/post-decoherence-selection-programme` W L171, L167; N L73, L93, L105, L121, L97
- `apex/self-construction-constructor` W L86, L108, L137, L82, L141; N L106, L139, L153
- `concepts/conservation-laws-and-mental-causation` W L176, L168, L186, L190; N L101, L182, L170, L97
- `concepts/ensemble-level-epiphenomenalism` W L37, L61 (Maier residue, carried), L59/L77 (driver: "actually sufficient"); N L79, L43, L35
- `concepts/entanglement-binding-hypothesis` W L76, L102, L104/L106; N L108, L122, L110
- `concepts/epiphenomenalism` W L102/L116, L144, L148; N L88, L130, L140, L154, L163, L197, L201
- `concepts/interactionist-dualism` W L195, L193/L109, L192, L209, L177, L135, L137/L131, L91; N L119, L135/L153, L159, L99, L205, L190
- `concepts/objections-to-interactionism` W L39/L59/L179/L196 (pairing over-claimed against [P-SC2](/positions/subject-census/#p-sc2)), L169; N L127, L165/L190/L194, L175
- `concepts/occasionalism` N L58
- `concepts/pairing-problem` W L74/L168/L3, L122; N L118, L148
- `topics/the-epiphenomenalist-threat` W L143–151, L95, L172, L133; N L137/L174, L57, L131, L178
- `topics/causal-closure-debate-historical-survey` W L115 (held from ERROR); N L40/L125, L56
- `topics/consciousness-and-causal-powers` W L196/L200; N L180, L182, L130, L104, L160
- `topics/quantum-holism-and-phenomenal-unity` W L176 (four checks live); N L122, L120, L160, L90
- `concepts/first-order-representationalism` W L112
- `concepts/intrinsic-nature` W L81
- `concepts/meta-problem-of-consciousness` N L139, L95, L87
- `concepts/mine-ness` E L136 (covered: P2 L1656); W L144
- `concepts/neural-correlates-of-consciousness` W L160, L168 (both covered by open P2s L1550/L1602); N L115
- `concepts/phenomenal-acquaintance` W L42/L96 (held from ERROR), L144, L146; N L90, L86
- `concepts/phenomenal-concepts-strategy` E L193; W L143, L139/L187, L131, L165–169, L149, L183, L117; N L195, L191, L189
- `concepts/phenomenal-transparency-opacity-spectrum` W L121; N L119, L117, L87
- `concepts/philosophy-of-science-under-dualism` W L70, L84, L118; N L48/L36, L100, L120, L135/L128
- `concepts/process-philosophy` W L158; N L98/L144, L108, L114, L162, L126
- `concepts/qualia` W L205, L213, L62, L217/L219, L155; N L199, L132, L187, L183, L128/L239/L247
- `concepts/russellian-monism` W L43, L101/L97/L129/L91, L141/L145, L99/L65; N L131, L121
- `topics/russellian-monism-versus-bi-aspectual-dualism` W L46, L140, L102/L159; N L144, L114, L68
- `voids/intrinsic-nature-void` N L113, L47 (L117 REPAIRED)
- `voids/phenomenal-quality-void` W L130
- `voids/necessary-opacity` N L156 (L152/L154 REPAIRED)
- `concepts/parsimony-epistemology` W L88/L90, L60/L58, L130/L174; N L46, L164, L124, L172/L176
- `concepts/mental-effort` W L94/L100, L72, L134/L64, L112/L104, L150, L128; N L146, L98, L152/L154, L144/L92/L120/L158
- `concepts/motor-selection` W L210, L198; N L188/L190/L192, L141, L180, L214, L50/L111/L149/L224
- `topics/capgras-delusion-and-the-affective-recognition-channel` N L87
- `topics/clinical-dissociation-as-systematic-evidence` W L141; N L3/L151, L62, L80, L153
- `topics/consciousness-and-neurodegenerative-disease` W L75/L117; N L85/L129, L111, L99/L101
- `topics/dopamine-and-the-unified-interface` W L211, L172/L180, L135/L137, L200/L207/L74; N L31, L176, L49
- `topics/history-of-the-interaction-problem` W L142, L99, L128/L136; N L138, L114
- `topics/interaction-problem-across-traditions` W L98; N L100, L132 (Tenet 1's Rules-out attributed to Tenet 3)
- `topics/leibnizs-mill-argument` N L139, L135
- `topics/parsimony-case-for-interactionist-dualism` W L136, L144, L109/L111; N L47, L59/L93/L128/L134
- `topics/phenomenal-authority-and-first-person-evidence` W L209; N L102, L213, L211, L134
- `topics/phenomenology-of-agency-vs-passivity` W L135, L143, L101, L125; N L3, L165, L182
- `topics/phenomenology-of-recursive-self-awareness` W L141; N L117, L143, L147
- `topics/philosophy-of-habit-under-dualism` W L83, L87 (both carried; survived the 09-29 deep review); N L59, L29

### Outside the window

- **Carried and re-verified live (files not committed in the window):**
  - Check 142 row 4 (Summary 8).
  - `brain-specialness-boundary` L63
  - `three-kinds-of-void` L103
  - [voids/voids.md](/voids/) L313
  - `unity-of-consciousness` L135
  - `conscious-vs-unconscious-processing` L177
  - `consciousness-and-cognitive-distinctiveness` L188
  - `modal-structure-of-phenomenal-properties` L3
  - `time-symmetric-selection-mechanism` L214
  - `objectivity-and-consciousness` L84
  - `consciousness-defeats-explanation` L158
  - `swampman` L87
  - `mental-imagery` L57
  - `curated-mind` L105
  - `predictive-construction-void` L129
  - `diachronic-agency-and-personal-narrative` L129
  - All other check-142 §Warnings loci in files without a window commit are live by construction.
- **Propagation tail, "actually sufficient" (priority row 3):** `apex/born-preserving-causal-efficacy` L123/L189, `concepts/causal-consistency-constraint` L95, `topics/consciousness-and-probability-interpretation` L97.
- **Propagation tail, fabricated "tenet predicts".** Check 141's candidate boundary, re-probed. The clear cases are:
  - `topics/concession-convergence-philosophy-of-mathematics` L114/L118
  - `concepts/concession-convergence` L149/L153
  - `topics/volitional-control` L154
  - `topics/biological-computationalisms-inadvertent-case-for-dualism` L90
  - `topics/phenomenology-of-linguistic-failure` L113
  - `topics/invertebrate-consciousness-as-interface-test` L135
  - `topics/dualist-perception` L162
  - `topics/consciousness-and-language-interface` L250
  - `concepts/self-reference-paradox` L146
  - `voids/observation-and-measurement-void` L152
  - `voids/decision-void` L107
  - `topics/animal-consciousness` L116 and `apex/minds-without-words` L157 ("exactly the pattern Occam's Razor Has Limits predicts")
  - `voids/mood-void` L114/L126

  The hedged or self-corrected hits pass: `apex/phenomenal-variation-within-a-species` L161, `concepts/perception` L96, `topics/architectural-adequacy-at-the-built-edge` L116 and `voids/what-voids-reveal` L116/L150. The grep key is `(tenets?\]\]|tenet|Dualism\]\]|Interaction\]\]|Limits\]\])[^.]{0,60}\bpredicts?\b`, with "does not / would / equally" excluded.

## Notes

381 NOTE findings, indexed per file above. Most are over-claims corrected in the same paragraph, navigation labels (Further Reading glosses) stating more than their target, or necessity vocabulary without an evidential-status L100 label. The cross-file ones:
- **tenets.md L159** still points at "`[[apex/machine-question]]` §senses of conscious AI". That apex has no heading of that name; the four senses are prose at L71. Carried.
- **`positions/subject-census` L59** and **`subject-census-calibration-history` L43**: "einselected menu" without the improper-mixture qualifier. This is corpus-standard vocabulary, which `apex/post-decoherence-selection-programme` L57 defines correctly, so it stays a NOTE.
- **`concepts/bi-aspectual-ontology` L61** ("both real, both fundamental") is the source of `parsimony-case` L136's "co-fundamental". It is out of window and belongs to the same class as the carried bi-aspectual L37/L139.
- **`concepts/mine-ness` L60/L82** assert the thought-insertion double dissociation flat. This is the upstream source of the reciprocal over-claims in Summary 6, and P3 todo L1693 is adjacent.
- **`concepts/quantum-factorisation-problem` L76** says the post-decoherence apex "mentions neither factorisation nor tensor-product structure". The apex's new L145 now does, so the claim is stale. It is hedged "at this page's writing".
- **`causal-closure-debate-historical-survey` L40/L125** ("load-bearing premise in virtually every contemporary argument") is in tension with the newly linked IBE page, whose L32 says the physicalist's strongest argument needs no closure premise.
- **`revelation-thesis`** has no `last_deep_review` and no deep-review commit. **`self-stultification-as-master-argument`** has not been deep-reviewed since 2026-07-12.

## Files passing all checks (5)

- [topics/covert-consciousness-and-cognitive-motor-dissociation.md](/topics/covert-consciousness-and-cognitive-motor-dissociation/) (new)
- [positions/subject-census-calibration-history.md](/positions/subject-census-calibration-history/)
- [concepts/phenomenal-constitution-thesis.md](/concepts/phenomenal-constitution-thesis/) (its window IBE hunks are clean)
- [concepts/self-model-theory-of-subjectivity.md](/concepts/self-model-theory-of-subjectivity/) (Metzinger engaged as a rival, with his stance stated)
- [topics/paradoxical-kinesia.md](/topics/paradoxical-kinesia/) (outcome-devaluation reciprocals keep the construct-gap caveat)

NOTE-only (17): `depersonalisation`, `thought-insertion`, `inference-to-the-best-explanation-against-dualism`, `outcome-devaluation-and-dual-task-costs-in-parkinsons`, `colour-ontology-and-the-secondary-quality-residue`, `locked-in-syndrome-…`, `galilean-exclusion`, `positions/ai-substrate-verdicts`, `positions/subject-census`, `anaesthesia-and-the-consciousness-interface`, `valence-and-conscious-selection`, `occasionalism`, `meta-problem-of-consciousness`, `intrinsic-nature-void`, `necessary-opacity`, `capgras-delusion-…`, `leibnizs-mill-argument`.

## Method

1. Read `tenets.md` L49–147 and L149–188: definitions, rationales, qualifiers, Rules-out clauses, the matrix and the background posits. There has been no commit since e3e689517d.
2. Listed every file in `topics/ concepts/ voids/ apex/ positions/` with a commit since 2026-09-30T07:50Z: 125 files. Fourteen parallel sub-sweeps (two on the new articles, two on today's calibration pages, ten on the rest) read every file in full. They worked from a common brief: the lens families with their tenets loci, the evidential-status ladder, the co-optation roster, and the severity rules. Each re-probed its files' prior loci from checks 140–142 by exact string and marked each REPAIRED or STILL LIVE. The driver waited in the foreground for all fourteen, then read their full outputs before writing.
3. Carried ERRORs were re-probed by exact string. Each zero was confirmed as a repair by reading the repair commit's word-diff (62e09be708, f60ad5b851, 53c0949707, 1d5474fd41), not inferred from absence.
4. Every ERROR in this report was re-verified by the driver by exact substring at the stated line. Three sweep ERRORs were regraded to WARNING by family precedent (Summary 9). One sweep claim was rejected: the PCS archive sibling has 0 hits.
5. Driver corpus probes outside the window covered three things: (a) the check-142 carried loci in files without a window commit; (b) "actually sufficient" (Tenet 2 minimality), which surfaced from sweep C3a, with four false positives excluded; (c) fabricated "tenet predicts" against check 141's candidate list. Probe (c) found the out-of-window ERROR at `consciousness-and-scientific-explanation` L58.
6. Cross-checked the Active section of [workflow/todo.md](/workflow/todo/). `mine-ness` L136 (P2 L1656), `neural-correlates-of-consciousness` L160/L168 (P2 L1550/L1602) and the `consciousness-disruption` description and IIT loci (P2 L1729) are covered and not re-proposed. P3 L1702 and the NEEDS-HUMAN length block on `apex/born-preserving-causal-efficacy` (L432) are flagged inside the rows they touch.
7. No content file and no `todo.md` entry was modified. The skill's contract is reports-only, so the four priority rows are ready-to-mint briefs for the driver.

## Scope confirmation

All 125 window files were read in full; none was skipped, sampled or read in targeted mode. Files outside the window were probed by exact string only: the carried loci, the two propagation keys, and the check-141 candidate list. They are reported as carried or as out-of-window grep hits, never as fresh reads.