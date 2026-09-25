---
title: "Optimistic Review - 2026-09-25 - The Discriminating-Test Wing"
created: 2026-09-25
modified: 2026-09-25
human_modified: null
ai_modified: 2026-09-25T13:40:00+00:00
draft: false
description: "Wing review of eight empirical interface-evidence articles. Today's two new pages grade their evidence well. The 2026-09-19 repair that found the filter reading forbids no ordering has not reached the test-design page or the apex."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-09-25
last_curated: null
last_deep_review: null
---

# Optimistic Review: The Discriminating-Test Wing

**Date**: 2026-09-25
**Slot**: cycle optimistic-review, with no driver brief. I chose the target by coverage. Across the optimistic reviews dated 2026-07 to 2026-09, **63** live topics/concepts/voids files are never named by slug. Eight of them form a coherent wing. These are the pages that turn the interface model into empirical tests: they either grade the existing evidence or design a test that would separate the filter/interface reading from production rivals. Two of the eight (`sham-controlled-neurofeedback…`, `anosognosia…`) were created and deep-reviewed today.

**Content reviewed** (bodies read in full on disk; lengths from `tools.curate.length.analyze_length`, body-only; headroom = hard − 1 − count; topics hard line 4000):

| article | body words | status | headroom | last deep review | body inbound |
|---|---|---|---|---|---|
| `obsidian/topics/memory-channel-interface-evidence.md` | 4542 | **hard_warning** | **−543** | 2026-08-08 | 16 |
| `obsidian/topics/empirical-evidence-for-consciousness-selecting.md` | 3816 | soft_warning | **183** | 2026-07-12 | 9 |
| `obsidian/topics/interface-efficacy-and-the-cognitive-gap.md` | 3675 | soft_warning | 324 | 2026-09-23 | 19 |
| `obsidian/topics/targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy.md` | 3548 | soft_warning | 451 | 2026-08-02 | 16 |
| `obsidian/topics/sham-controlled-neurofeedback-and-the-consciousness-comparator.md` | 3035 | soft_warning | 964 | 2026-09-25 | 3 |
| `obsidian/topics/anosognosia-and-the-reversible-self-monitoring-channel.md` | 2925 | ok | 1074 | 2026-09-25 | 2 |
| `obsidian/topics/dopamine-and-the-unified-interface.md` | 2825 | ok | 1174 | 2026-07-19 | 12 |
| `obsidian/topics/direction-dependent-discriminating-test-design.md` | 2357 | ok | 1642 | 2026-06-20 | 9 |

Line numbers below are **file** line numbers, frontmatter included, taken on 2026-09-25. The `memory-channel` over-length is mostly real prose. The body up to `## Further Reading` is about 3980 words by `wc -w`, so any fix there must be length-neutral or shorter. `empirical-evidence` is about 3017 words of prose; its apparatus is what brings it to 3816. Section counts from `tools.evolution.state.count_section_files`: topics 331/360, concepts 329/360.

## Executive Summary

**The two pages written today are the wing's best calibration writing.** `sham-controlled-neurofeedback` reads a negative clinical result (real neurofeedback does no better than sham) as a test Tenet 3 "must price" (L35). It gives the deflationary reading full strength and designs a 2×2 trial that would separate the two readings (L73). `anosognosia` concedes that Fotopoulou's intra-cerebral account "fits the data at least as well as an interface reading does" (L38). It then states the Map's gain as a *correction to how the Map describes the syndrome*, not as evidence (L84, L104). Both pages apply the [[evidential-status-discipline]] to themselves, even where the result is unflattering to the Map.

**A repair made on 2026-09-19 has not propagated.** Commit `743041228a` corrected `memory-channel-interface-evidence` L136: the filter reading "is *consistent with* a direction-sensitive signature rather than deriving one… That clause forbids no ordering, the mirror-symmetric one included." Four loci still describe the test as though the filter reading made a prediction of its own:

- **The same paragraph's last sentence** says the test-design articles offer "a reversible perturbation whose up-ramp and down-ramp orderings the rival readings predict oppositely".
- **`direction-dependent-discriminating-test-design` L38** promises "opposite, advance-stated predictions".
- **`falsification-roadmap-for-the-interface-model` L201** labels the page as one "whose channel orderings the rival readings predict oppositely".
- **`apex/self-concealing-interface` L127** lists as a failure condition "a focal perturbation producing a recovery sequence the filter reading forbids", with the readings "already… pinned to opposite orderings". L180 repeats the claim.

The design page's own body is more careful (L48 "is **not committed** to their symmetry", L62 "permits them to dissociate"). So the lead contradicts its body, and the apex has inherited the lead.

**Two older pages lag behind the wing's standard.** `dopamine-and-the-unified-interface` says the unified interface "supports" Dualism (L188). It also quotes a phrase with no citation (L196) and rests its Occam paragraph on an epiphenomenalist rival that none of its siblings would accept (L215). `empirical-evidence-for-consciousness-selecting` has a grading table that stops every line at *supports-mental-causation* (L117–128), yet its lead (L42) and conclusion (L143) still say the convergence may "favour the hypothesis over its competitors".

**Intra-wing wiring is thin.** Of 56 possible directed links among the eight pages, **6** exist, all inside the memory-channel / targeted-lesion / direction-dependent triangle. Five pages link to no sibling. The anosognosia page is the only *observed* reversible perturbation of a channel. The direction-dependent design needs exactly that case, and neither page links to the other.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)

Chalmers would praise the wing for keeping the hard problem as the Map's case for dualism instead of spending it on clinical data. `anosognosia` L100 is the model: "The reversals can be told fully in production terms… What remains unexplained is the general gap between any such account and what it is like for the patient to realise, at last, that her arm does not move. That gap is the hard problem and is not special to this syndrome. The Map should not present anosognosia as a dualist datum." `sham-controlled-neurofeedback` L67 draws the same line from the other side. The physicalist "can accept the intention reading completely and describe the effort as one neural process affecting another". Deciding between contingency and effort "would not by itself settle whether effort is anything over and above its neural realisation." `empirical-evidence` L55 names the further arguments the Map actually uses (explanatory gap, conceivability, causal closure) and does not claim that evolution supplies them.

The exception is `dopamine` L190: "The experience of being drawn toward valued options… is not a neural computation but a conscious state." That states the dualist conclusion as a datum. The hard problem does support a weaker claim: a neural computation does not *explain* the felt pull. That is the claim Chalmers would sign.

### The Quantum Mind Theorist (Stapp)

Stapp would like `dopamine` L62 and L84. They say where his Process 1 could sit in a drift-diffusion race without breaking it: dopamine moves the threshold, learned value sets the drift, and "when two options are closely matched, the mechanism by which one finally wins is left to noise in these models." He would also like the honest hedge at L160, where the quantum Zeno mechanism is "one proposed but speculative model". The fuller calibration he would want is in `empirical-evidence` L94, where Denton et al. (2024) is "a computational precedent for the mechanism category, not a demonstration that evolution has deployed it neurally". This is the corpus's settled wording for Denton, and the page uses it.

`interface-efficacy` L106 is the most careful Stapp-adjacent move in the wing. The Born-deviation observable "exists only on the looser readings of Minimal Quantum Interaction… the strict selection-only reading predicts none". Stapp is a strict reader, and the page does not saddle him with a prediction he disowns. The same page's L125 then says all four efficacy axes stay "within the Born-rule corridor", which the looser reading at L106 does not. That is a small slip, noted in Minor Findings below.

### The Phenomenologist (Nagel)

`anosognosia` L58 has the wing's strongest phenomenological datum. The patient's denial "had been unaltered when she observed her plegic arm in her ipsilateral visual field", yet she corrected "at once when it came in the third person and off-line." Nagel would note that the difference is in the *point of view*: the information was the same and the perspective changed. The page reads this with care and draws no dualist lesson from it (L82: the interface reading "gets the specificity from the same brain-level distinction Fotopoulou already uses, so it adds nothing she lacks"). The finding still belongs in the Map's perspectival cluster, as a clinical case where first-person and third-person access to one's own body come apart. See Cross-Linking.

`memory-channel` L112 is the other strong page for Nagel. In depersonalisation, "autonoetic content is present but the felt *ownership* is missing". The page takes this to show that autonoetic experience has internal structure (content, mine-ness, pastness) that can dissociate. That is a phenomenological claim made on clinical evidence, at the right grain.

### The Process Philosopher (Whitehead)

Whitehead would like `interface-efficacy`'s central move (L98). Consciousness may be present "at full grade" across species while its *effective reach* into behaviour varies. That separates experience from cognitive performance, which is the process philosopher's instinct. The page labels the hypothesis *speculative integration* (L51) and says what it takes from each side (L119: permission from the New York Declaration, discipline from Gutfreund).

**This persona's praise must not upgrade the tier, and one sentence comes close.** L49 says consciousness "may be present at full grade across many species — consistent with the New York Declaration on Animal Consciousness (2024)". The Declaration says nothing about *grade*. It asserts "strong scientific support" for mammals and birds and a "realistic possibility" for other vertebrates and many invertebrates (the page quotes this correctly at L94). "Full grade" is the hypothesis's own posit, and attaching it to the Declaration makes it sound endorsed. The Hardline Empiricist flags this below.

### The Libertarian Free Will Defender (Kane)

Kane would take the most from `sham-controlled-neurofeedback`'s *intention reading* (L63). The sham arm is "an intention condition as well as a control", so equal improvement in both arms may mean "the effort, not the feedback contingency, is what helps". The effort stays with the patient, and the machine is only scaffolding. The page then limits the reading. The trained band did not change in either arm (L65), so the intention reading "cannot claim these trials as a demonstration of the neuroplasticity article's selection mechanism." Kane would call that honest, since his view does not need neuroplasticity, only effort that makes a difference.

`dopamine` L84 is the wing's closest approach to Kane's "plural voluntary control". Frank's subthalamic "hold your horses" signal "raises the threshold globally, buying time for striatal dynamics to settle, yet what determines which option ultimately wins when two are closely matched remains noise." A torn decision is where Kane places self-forming actions. The page locates it correctly and calls the identification a proposal.

### The Mysterian (McGinn)

McGinn would praise how often the wing marks a question as *undecided* rather than *undecidable*, and how carefully it keeps the two apart. `targeted-lesion` L132: "the dispute appears empirically undetermined at the resolution present techniques can deliver, not metaphysically irresolvable." `interface-efficacy` L131: whether the alternative prevails "is something current methods cannot decide, and the Standing Agnostic Challenge says it may stay undecidable at the behavioural level". This is a mysterian ceiling named as a *possibility* and left open. `sham-controlled-neurofeedback` L89 refuses to let simplicity settle an empirical question that has a design: "the Map's position is to wait for the design rather than let simplicity settle it."

### The Hardline Empiricist (Birch)

Birch's verdict matters most for this wing, because every page in it is about evidence. Four pages earn his praise without reservation:

- **`anosognosia` L90–94** grades three tiers explicitly. Under "Established, with small samples", each finding carries its n (58; 2 of 4; n = 1; 3 of 12; 6 of 7). The reversible-channel reading is a "Live hypothesis… not evidence-elevating, for two reasons". The case is placed in "state 2: **a serious live countermodel stands**". The page even cites a *measurement* caveat against itself: every measure is of verbal report, and Striemer and Danckert (2010) show how measured improvement in neglect can leave the deficit in place.
- **`sham-controlled-neurofeedback` L81** states the scope of a strongly supported negative ("for the conditions and outcomes tested") and names three reasons it does not generalise, including a secondary outcome that ran the other way (L51, medication at follow-up) which "a fair summary includes". Reporting a result that cuts against the page's own framing is the restraint Birch rewards.
- **`empirical-evidence` L117–128** credits each line of evidence "only with the *weakest* claim it establishes, not the strongest claim it is compatible with". It adds a physicalist/illusionist column for every row. This is the Map's clearest statement of "tenet-coherent, not evidence-elevating" applied to its own flagship evidence page.
- **`direction-dependent` L70** declines to treat anaesthetic hysteresis as evidence. Proekt and Hudson's ten-state stochastic model produces hysteresis with no direction-specific machinery, so "the *discriminating* read-out is not hysteresis-presence but the **cross-channel ordering** under direction reversal." It also notes that the stronger rival sharpens the caution.

**Flags (calibration concerns, not praise):**

1. **The filter reading is described as making a prediction it no longer makes.** See the Executive Summary. `memory-channel` L136 now says the filter clause "forbids no ordering, the mirror-symmetric one included". The same paragraph's last sentence, `direction-dependent` L38 ("**opposite, advance-stated predictions**"), `falsification-roadmap` L201 and `apex/self-concealing-interface` L127 and L180 all still describe a two-sided test. In fact the test is one-sided: the substrate-symmetric production reading forbids a reversal and the filter reading permits one. A reversal removes the simplest production rival, as `direction-dependent` L74 says correctly. A symmetry result counts against the direction-dependence *family's* accommodation-grade support (L76), but it cannot falsify a filter reading that forbids nothing. The apex's claim that the recovery-order seam "admits genuine failure conditions" through "a recovery sequence the filter reading forbids" (L127) is therefore a falsifiability claim the source article has withdrawn.
2. **`memory-channel` contradicts itself about the dissociative rows.** L88 says "The decoupling cases — ketamine, depersonalisation, DID — invert it". L118, from the same 2026-09-19 commit (`e2762d7039`), says "The weight falls on the dissociative rows, which carry the ordering with no degradation variable to appeal to." The table (L84–86) shows DID and dissociative amnesia *following* the ordering (autonoetic severed, noetic and anoetic preserved). Only the ketamine row inverts it, and ketamine is pharmacological, not dissociative. L88 therefore groups DID with the wrong cases. Removing "depersonalisation, DID" from L88's list fixes both sentences with a net cut in words.
3. **`empirical-evidence`'s lead and conclusion outrun its grading table.** L42 says the lines "collectively appear to favour the hypothesis over its competitors". L143 says they are "convergent evidence that may favour one hypothesis over its competitors". The page's own table puts every line at or below *supports-mental-causation* (L117: "none reaches the last three"). L141 says the convergence "leaves consciousness-selecting *among the surviving candidates*; singling it out from its true rivals is separate work." L106's bullet ("microtubule stabilisation delays unconsciousness") restates as a finding the reading that L98 says "cannot yet be read as a clean… signature". L153's "Current evidence trends favourable" has no grade. All four are small wording changes in a page with **183 words** of headroom.
4. **`dopamine`'s Relation section is a tenet-as-evidence upgrade.** L188 says "The unified interface supports Dualism". L196 says dopamine-deficient animals, "virtually unconscious behaviorally", show "what happens when the brain-to-consciousness channel fails". The quoted phrase has no citation on the page. The research note (`research/dopamine-attention-motor-quantum-interface-2026-01-24.md` L66–70) traces it to PMC11223727, which is not in the reference list. It also describes *behaviour*, and the page reads it as a failure of a consciousness channel. L215 names the rival as "consciousness is epiphenomenal". The wing's own grading (`empirical-evidence` L121–123) names the real rival as non-reductive physicalism, which keeps mental causation. The empirical premise at L82 and L174 ("automatic gait" and "Preserved reflexes… Only willed action impaired") is contested by the page's own L172 (freezing of gait). There is also a well-known reading on which Parkinson's primarily damages *habitual* control, with patients falling back on goal-directed control (Redgrave et al. 2010, *Nature Reviews Neuroscience*; this is a lead to verify, not a checked citation). If that reading holds, the dissociation the page builds on runs the other way.
5. **`interface-efficacy` L90 calls DeWall et al. (2008) "direct evidence that interface bandwidth is finite and bottlenecked".** The sibling `empirical-evidence` L68 says a physicalist account "accommodates the DeWall findings equally well", and its table grades DeWall at *supports-mental-causation* (L122). The phrase "direct evidence" upgrades the finding on tenet-load. "Is what the reading would expect" would fit the page's own *speculative integration* label (L51).

## Content Strengths

### topics/sham-controlled-neurofeedback-and-the-consciousness-comparator.md
- **Strongest point**: It turns a negative result into a test design. The existing trials vary contingency and hold intention fixed. The 2×2 (contingency × active/passive instruction, with expectation measured) varies intention and holds feedback fixed, and each reading has a stated prediction for each cell (L73).
- **Notable quote**: "Whether effort is a nuisance variable or the active ingredient is a choice about which arm counts as the control." (L89)
- **Why it works**: It names the classification decision that the parsimony argument depends on. The Occam's-Limits tenet is applied to a specific methodological choice instead of being asserted in general.

### topics/anosognosia-and-the-reversible-self-monitoring-channel.md
- **Strongest point**: The route-specificity analysis (L82). First-person viewing fails and third-person viewing succeeds. An intra-cerebral two-route account predicts this, and the interface reading "adds nothing she lacks".
- **Notable quote**: "It shows what such a test looks like. It also shows that such a test can come back favouring an intra-cerebral account as readily as an interface one." (L96)
- **Why it works**: It supplies the "targeted, reversible perturbation" that `clinical-dissociation-as-systematic-evidence` says the catalogue lacks. It then reports honestly that the perturbation does not favour the Map.

### topics/empirical-evidence-for-consciousness-selecting.md
- **Strongest point**: The six-category weakest-claim grading table with the physicalist column (L117–128).
- **Notable quote**: "A line of evidence should be credited only with the *weakest* claim it establishes, not the strongest claim it is compatible with—compatibility with dualism is not evidence for dualism." (L117)
- **Why it works**: Any page in the corpus that cites "the empirical case" can be checked against it. It also shows that the page's own framing at L42 and L143 is too strong.

### topics/direction-dependent-discriminating-test-design.md
- **Strongest point**: The common-cause caution (L78). A positive reversal "is **not** an independent fourth or fifth confirmation"; what it adds "is not multiplicity but *quality*".
- **Notable quote**: "The upgrade is in evidential grade on one axis, not in the number of axes." (L78)
- **Why it works**: It stops a future positive result from being counted twice, before any such result exists.

### topics/memory-channel-interface-evidence.md
- **Strongest point**: The self-applied fitting charge at L122. Bandwidth and reconstruction cost "are ranked partly by the very ordering they are then invoked to explain, which is a milder form of the after-the-fact fitting this argument charges against rivals."
- **Why it works**: The page charges itself with the same fault it finds in its rivals, and it narrows its own claimed advantage accordingly.

### topics/targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy.md
- **Strongest point**: The three candidate region pairs are graded by tractability, from "a demonstrated human focal target to one no current modality reaches" (L122). The anterior-thalamic entry (L120) cites Krishna et al. (2023) and says the ablative modality supplies "the focal-lesion ingredient rather than the reversible neuromodulation a within-subject discriminator would prefer."
- **Why it works**: The design space is tied to what the technology can currently deliver.

### topics/interface-efficacy-and-the-cognitive-gap.md
- **Strongest point**: The brain-side reading is set out at full strength first (L68–76), including the Herculano-Houzel (2014) elephant count that "retir[es] the elephant anomaly". That is a correction against the page's own motivating puzzle.

### topics/dopamine-and-the-unified-interface.md
- **Strongest point**: L62's drift-versus-threshold reading of Chakroun et al. (2023). L-DOPA lowered the threshold "roughly uniformly, producing faster but *less* accurate responses rather than selectively favoring high-value options". It is the most exact placement of an empirical finding against the selection hypothesis anywhere in the wing.

## Expansion Opportunities

### High Priority

#### Paradoxical Kinesia and the Direction of the Parkinsonian Dissociation
- **Builds on**: `dopamine-and-the-unified-interface` (L82, L172–182), `volitional-control`, `consciousness-and-neurodegenerative-disease`, `motor-selection`.
- **Would address**: The dopamine page's central premise is that Parkinson's "disables willed movement" while automatic movement survives. The main rival reading is that Parkinson's primarily damages *habitual* control and patients rely on effortful goal-directed control (Redgrave et al. 2010, lead). The two readings interpret the external-cue bypass (L178–182) oppositely. Paradoxical kinesia is the sharpest test case: a patient who cannot initiate gait runs from a fire, or catches a thrown ball (Souques 1921; Glickstein & Stein 1991, *Trends in Neurosciences*; both leads to verify). "paradoxical kinesia" and "kinesia paradoxa" have **0** hits in topics/concepts/voids/apex/research, and "habitual control" has 0. A page would grade both readings. It would say what each predicts about cue-driven and emergency-driven movement and where the Map's selection-interface reading stands. That standing may be lower than the dopamine page currently claims.
- **Estimated scope**: Medium article (topics/, 331/360).
- **Tenet alignment**: Tenet 3 (Bidirectional Interaction) at the calibrated *available-not-actual* standing. Tenet 5, because the parsimony question here is which dissociation the data show, not whether dualism is simpler.

### Medium Priority

- **Wire the anosognosia reversal into the design pair.** This is link work, not a new page (see Cross-Linking). The anosognosia case is the one observed reversible channel perturbation, and it came back neutral. The direction-dependent design (L56) proposes a reversible perturbation as its enabling feature. Each page is the other's worked instance.

### Ideas for Later

- A short concept page on **one-sided versus two-sided discriminators**: tests where only one rival forbids an outcome, as against tests where the rivals forbid opposite outcomes. The flag-1 propagation failure shows the corpus lacks a name for this distinction. `discrimination-problem` could host it as a section. It should be weighed against that page's headroom before minting.
- The yoked-sham / passive-viewing design (sham L73–77) could become an entry in `falsification-roadmap-for-the-interface-model`. That page links the two memory designs but not the effort design.

## Cross-Linking Suggestions

| From | To | Reason |
|------|-----|--------|
| `direction-dependent-discriminating-test-design` (L56, "reversibility is the design's enabling feature") | `anosognosia-and-the-reversible-self-monitoring-channel` | The only observed reversible channel perturbation. It is also a worked warning that such a test can favour the intra-cerebral account. |
| `anosognosia-and-the-reversible-self-monitoring-channel` (L96) | `direction-dependent-discriminating-test-design` | L96 describes "what such a test looks like". The designed version exists. |
| `empirical-evidence-for-consciousness-selecting` (L124, placebo row) | `sham-controlled-neurofeedback-and-the-consciousness-comparator` | The sham trials are the cleanest test of whether the effort in that row is the active ingredient. They also cut against the "Directed conscious effort correlates with measurable neural changes" bullet (L85). |
| `dopamine-and-the-unified-interface` (L118–122, the effort parallel) | `sham-controlled-neurofeedback-and-the-consciousness-comparator` | That page shows effort held constant and the targeted neural pattern unchanged, which bears directly on "effort is what conscious engagement with the selection mechanism feels like". |
| `interface-efficacy-and-the-cognitive-gap` (L90, DeWall) | `empirical-evidence-for-consciousness-selecting` | The same finding is graded there at *supports-mental-causation*. The link fixes the calibration and adds a reciprocal at no word cost (piped link). |
| `sham-controlled-neurofeedback…` | `empirical-evidence-for-consciousness-selecting` | Reciprocal of row 3. The sham page's L85 already cites the grading logic without linking it. |

## New Concept Pages Needed

- None beyond the "Ideas for Later" item above. The wing's gaps are propagation and wiring, not missing concepts.

## Minor Findings (no task)

- `memory-channel` L83: the table marks the terminal-lucidity anoetic channel "Often returns last". Nothing in the section (L104–108) sources an anoetic ordering, and L106 says even the autonoetic ordering "is what the case literature suggests, not a measured result". Consider "Not reported".
- `anosognosia` L76 says "weaker evidence" in two consecutive sentences about the same point; one of the two can go.
- `interface-efficacy` L96 says the hypothesis offers "a single mechanism that subsumes phenomena", and L117 says it "does not specify a mechanism for the interface itself". "A single explanatory variable" would fit both.
- `interface-efficacy` L125 ("all within the Born-rule corridor") is true only on the strict reading L106 distinguishes.
- `targeted-lesion` L54 states the production reading's prediction in a form that is hard to parse ("should produce a narrower-than-usual deficit only if…"). It also says autonoetic *preservation* after an autonoetic-only lesion would favour production. That favours neither reading straightforwardly, since production also predicts that damage to autonoetic substrate impairs the autonoetic channel. L110 (channel-down vs channel-degraded) states the discriminator more clearly. A future deep review should reconcile L54 with L44 and L110.
