---
title: "Outer Review - Claude Opus 5 (2026-08-07)"
created: 2026-08-07
modified: 2026-08-07
human_modified: null
ai_modified: 2026-08-07T04:52:00+00:00
draft: false
description: "Claude Opus 5 audits attention-as-causal-bridge. Its headline 'fabricated gamma bands' charge is refuted — the bands are real (Wyart & Tallon-Baudry 2008) but misattributed; the Sjöberg author-stance inversion is verified."
topics:
  - "[[structure-of-attention]]"
  - "[[attention-and-the-consciousness-interface]]"
  - "[[volitional-control]]"
  - "[[free-will]]"
concepts:
  - "[[attention-as-interface]]"
  - "[[mental-effort]]"
  - "[[evidential-status-discipline]]"
  - "[[common-cause-null]]"
related_articles:
  - "[[project]]"
ai_contribution: 90
author: "Andy Southgate"
ai_system: "claude-opus-5"
ai_generated_date: 2026-08-07
last_curated: 2026-08-07
outer_review_status: processed
outer_review_conversation_url: https://claude.ai/chat/144ad82a-b97b-46f7-80a4-8aeebde83045
outer_review_extraction_method: js-dom
subject_type: recent
subject_title: "Audit attention-as-causal-bridge"
subject_articles:
  - apex/attention-as-causal-bridge.md
subject_source: reuse:pending-reviews:outer-review-2026-08-07-chatgpt-5-6-sol.md
---

**Date**: 2026-08-07
**Reviewer**: Claude Opus 5
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

You are a hostile pre-publication referee assessing a single article on The Unfinishable Map for a top-tier philosophy journal: https://unfinishablemap.org/apex/attention-as-causal-bridge/ . It was last substantively revised on 2026-07-31, and external search indexes lag this site by 24-48 hours, so consult the changelog at https://unfinishablemap.org/workflow/changelog/ and the site root https://unfinishablemap.org before judging currency. The article is a synthesis piece arguing that attention is the locus at which consciousness exerts causal influence on physical outcomes. Audit four things: whether its empirical claims about attention, neural gain and volition match what the cited studies actually found; whether its citations are real, correctly attributed and current with 2020s literature; which strong counterarguments (physicalist, predictive-processing, epiphenomenalist, illusionist) it leaves untested; and where it treats a disputed framing as settled or brackets a problem to protect a prior commitment. Do not describe the site's automation or review pipeline; audit the article's arguments only. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# HOSTILE PRE-PUBLICATION REFEREE REPORT

**Article under review:** "Attention as the Causal Bridge" — [apex/attention-as-causal-bridge](https://unfinishablemap.org/apex/attention-as-causal-bridge/) (apex synthesis; created 2026-02-14; last substantively modified 2026-07-31; live version fetched directly by slug and confirmed against the site changelog and root, both current to 2026-08-07).

## 1. TL;DR VERDICT

**REVISE-HARD, bordering DEMOTE-TO-COHERENCE-ONLY.** The article is dialectically more self-aware than its genre norm — its Attention Schema Theory section is genuinely competent and its handling of Cai et al. (2024) is a model of calibration — but it rests on defects that no amount of hedging repairs. Two are blocking: (i) a fabricated, uncited, load-bearing empirical claim — the "frequency analysis" assigning conscious content to ~55–65 Hz and attentional control to ~75–90 Hz, which corresponds to no primary source and inverts what the actual gamma literature reports; and (ii) at least two author-stance inversions in which explicitly anti-dualist sources (Sjöberg 2024; Koch & Tsuchiya 2007) are recruited toward a dualist conclusion they expressly reject. Compounding these, the piece exhibits a pervasive *confession-without-correction* pattern: it names nearly every fatal objection — decoherence, the predictive-processing/active-inference rival, "borrowed" falsifiability, the constrain-vs-establish gap, common-cause dependence — and then retains its thesis at full strength. Because the article itself concedes that its strongest rival "is genuinely compatible with almost everything the article's evidence directly establishes," its positive dualist conclusion is unearned. Correct the fabrication and the inversions or demote to a coherence-only exhibit.

## 2. DIMENSIONAL ANALYSIS

### (A) EMPIRICAL ACCURACY

**A blocking fabrication (the gamma bands).** The sentence — *"Frequency analysis supports the separability: conscious content correlates with low gamma oscillations (~55-65 Hz) while attentional control operates in high gamma (~75-90 Hz)"* — is uncited and unsupported. Targeted verification against the primary literature finds no peer-reviewed source that assigns conscious *contents* to a 55–65 Hz band and attentional *control* to a distinct 75–90 Hz band. The claim garbles three separate real findings and gets the shape of each wrong:

- The canonical consciousness–gamma result is **Melloni et al. 2007** (*J. Neurosci.* 27(11):2858–2865), whose abstract states verbatim: *"Both perceived and nonperceived words caused a similar increase of local (gamma) oscillations in the EEG, but only perceived words induced a transient long-distance synchronization of gamma oscillations across widely separated regions of the brain."* The distinguishing marker of conscious access is long-range gamma **synchrony**, not a low-gamma frequency band — and local gamma *power did not distinguish* conscious from unconscious. This is the opposite of the article's logic.
- Attention is associated with *stronger* and only marginally higher-frequency gamma — a peak-frequency shift on the order of a few Hz within a single broad band (**Bosman et al. 2012**, *Neuron* 75(5):875–888; **Fries 2015**, *Neuron* 88(1):220–235) — not a categorical jump between a "content" band and a "control" band. (The specific "2–3 Hz" magnitude is the referee's characterization of the Bosman finding; the article's precise Hz figures are author-supplied, not quoted from any source.)
- "High gamma" above ~80 Hz is, per **Ray & Maunsell 2011** (*PLoS Biology* 9(4):e1000610), largely broadband, non-oscillatory activity indexing local spiking — not a narrowband oscillation that could carry an "attentional control" function.

This is false precision on a claim the "Dualism" tenet paragraph explicitly leans on ("Frequency analysis supports the separability… reinforces the irreducibility of experience"). It must be deleted or completely re-sourced.

**Sjöberg 2024 — empirically real, catastrophically misread (see B).** The datum — patients with the supplementary motor area resected retain the subjective sense of willing (reporting maximal effort to move) while losing execution — is reported accurately at the observation level. But the paper (Sjöberg, *Brain* 147(7):2267–2269) draws the *opposite* moral: the SMA does execution, not decision, so the Libet finding is (editor's summary, verbatim) *"in fact irrelevant to the neuroscientific discussion about free will,"* and (body, verbatim) *"dualism has been completely out of fashion in the neurosciences for almost half a century."* Sjöberg endorses Schurger's stochastic-accumulator reinterpretation and cites Sapolsky approvingly. [Oxford Academic + 2](https://academic.oup.com/brain/article/147/7/2267/7685995)

**Tegmark/decoherence — bracketed, not answered.** The article concedes neural decoherence "may be too fast for Zeno stabilisation" and defers to the "mental effort" concept article. **Tegmark 2000** (*Phys. Rev. E* 61:4194–4206) states verbatim: *"We find that the decoherence timescales (∼10⁻¹³–10⁻²⁰ seconds) are typically much shorter than the relevant dynamical timescales (∼10⁻³–10⁻¹ seconds), both for regular neuron firing and for kink-like polarization excitations in microtubules."* The direct-simulation literature (Georgiev's Monte Carlo studies of the QZE in the brain, 2015) shows Stapp's Zeno mechanism collapses once environmental decoherence is included in a basis different from the mind's; and the Itano et al. 1990 QZE demonstration was shown not to involve wavefunction collapse (Ballentine's critique), so it does not underwrite Stapp's "Process 1" use. None of this is engaged in-text; it is deferred, which protects the Minimal Quantum Interaction tenet.

**Cai et al. 2024 — a model of calibration.** The handling of Cai et al. (*Nature* 635(8038):406–414) is correct and appropriately hedged: the third "consciousness" layer is stated to be "consistent with rather than licensed by Cai et al." and to "stand or fall with the broader interface argument." This is how the rest of the empirical apparatus should read and does not.

**Other empirical citations check out at the finding level** but with two caveats. Verified accurate: Koch & Tsuchiya 2007; Nartker et al. 2025 (*eLife* 13:RP100337); the Cogitate Consortium 2025 (*Nature* 642(8066):133–142); Desmurget et al. 2009 (*Science* 324(5928):811–813); Thura & Cisek 2014 (*Neuron* 81(6):1401–1416); **Hagger & Chatzisarantis 2016** (*Perspectives on Psychological Science* 11(4):546–573), verbatim: *"Multiple laboratories (k = 23, total N = 2,141)… the size of the ego-depletion effect was small with 95% confidence intervals (CIs) that encompassed zero (d = 0.04, 95% CI [−0.07, 0.15])"*; Naccache et al. 2005 (*Neuropsychologia* 43(9):1318–1328); Zheng & Meister 2025 (*Neuron* 113(2):192–204). Caveats: (1) the COGITATE result is oversimplified — the article says "neither GWT nor IIT was clearly vindicated," but the reported outcome corroborated IIT's posterior-sufficiency prediction and challenged GWT's prefrontal-necessity prediction; "null" flattens an asymmetric result. (2) The Block-style overflow reading of the Nartker/Sperling data ("phenomenal experience persisting beyond the reach of cognitive access") is stated as established when it is precisely contested — Nartker et al. themselves frame their result around a conservative response criterion, i.e., a report-bias artefact rather than confirmed unconscious phenomenal overflow.

### (B) CITATION INTEGRITY

**Layer 1 — metadata accuracy: clean.** Every citation in the reference list exists with substantially correct author, title, year, journal, volume, and pages. No fabricated, composite, or non-existent citation was found. Minor: the Sauerbrei & Pruszynski entry omits volume/pages (it is *Nat. Neurosci.* 28(7):1365–1366, 2025) but is real.

**Layer 2 — verbatim fidelity: clean.** The single direct quotation — James's "The essential achievement of the will, when it is most 'voluntary,' is to attend to a difficult object and hold it fast before the mind" — is verbatim accurate to *The Principles of Psychology* (Ch. XXVI, "Will"). [Google Books](https://books.google.com/books/about/Psychology.html)

**Layer 3 — author-stance accuracy (the decisive check): two blocking inversions, one borderline recruitment, one correctly handled case.**

- **Sjöberg 2024 — BLOCKING inversion.** Sjöberg's piece is an explicitly anti-dualist obituary for the Eccles/Libet dualism debate. It is recruited (in "Why Effort Matters" and the Synthesis) as evidence that the surviving sense of willing shows "consciousness does genuine causal work." Sjöberg draws no such inference; he reads the identical datum as showing the SMA implements *execution*, and states dualism has been out of fashion for half a century. This is precisely the physicalist-recruited-to-dualism failure the audit flags.
- **Koch & Tsuchiya 2007 — structural inversion at the conclusion level.** The paper — "Attention and consciousness: *two distinct brain processes*" — is by two physicalists explicitly seeking consciousness's "material substrate." The article converts their functional dissociation into "consciousness is the non-physical subject; attention is the physical mechanism." The dissociation is real; the ontological gloss is the authors' express denial.
- **Naccache et al. 2005 — borderline recruitment.** The executive-control / felt-effort dissociation is reported accurately, but the paper is Dehaene-lab work in the global-workspace tradition the article opposes; treating the "autonomic-coupling residue" as evidence that felt effort "does causal work" reads more into it than its authors would grant.
- **Graziano / AST — handled correctly, and credited.** The article does *not* invert Graziano. It explicitly frames AST as deflationary, concedes AST can rejoin at several points, and states the disagreement "is about which framework to inhabit… rather than dressing tenet-incompatibility as a victory on AST's terms." This is the strongest section in the piece and the correct template for the rest.

**Currency: mixed.** The article engages 2024–2025 work (Sjöberg, Cai, Nartker, COGITATE), but its volition case leans on Desmurget 2009 without engaging the published Karnath et al. 2010 critique (that direct electrical stimulation may deactivate rather than activate cortex), and does not engage the Schurger et al. 2012/2021 readiness-potential reinterpretation in-text — despite Sjöberg himself citing Schurger 2012 approvingly in the very paper the article uses.

### (C) UNTESTED / UNDER-ENGAGED COUNTERARGUMENTS

- **Predictive processing / active inference — named, then abandoned (the central failure).** To its credit the article now carries a dedicated section conceding that on the precision-weighting reading "the same evidence lands" without ontological distinctness, and that active inference/FEP is "a *total* generative framework that natively models the very explananda the interface hypothesis reserves for a non-physical subject." It then states that confronting this framework "is owed and not discharged here." This is a confession, not an engagement: the strongest live physicalist rival is admitted to accommodate the entire evidence base, and the thesis survives unchanged. Everything the article's positive argument needs, this concession removes.
- **Causal closure / exclusion.** Kim's exclusion argument, the pairing problem, and the interface ("where") objection are addressed only by the "conservation laws are preserved because the energy… comes from ordinary metabolic processes" line — an assertion that answers the energy worry but not the exclusion worry (the problem is causal redundancy given a sufficient physical cause, not energy). Lowe's and Gibb's replies are not invoked; the objection is not even stated in its strong form.
- **Epiphenomenalism.** The article never seriously entertains that attention could be a wholly physical process consciousness merely accompanies; the overdetermination worry is unaddressed. The Naccache autonomic residue is offered as though it settles this, but it does not discriminate the two readings.
- **Illusionism.** The effort phenomenology is treated as a datum that "demands explanation," and the illusionist reply is waved off with a one-line regress ("who experiences the model?"). This is exactly the datum Frankish/Wegner explain away; treating it as evidence rather than as the contested explanandum begs the question against the deflationary rival — the same move the article scrupulously avoids against Graziano but commits here.

### (D) DISPUTED-AS-SETTLED AND PROTECTIVE BRACKETING

- **Epistemic-to-metaphysical slide.** "Consciousness without attention means phenomenal experience persisting beyond the reach of cognitive access" treats the overflow reading as fact; it is contested, and the cited primary source (Nartker) frames it as a criterion artefact.
- **Constrain-vs-establish.** "The leading materialist frameworks cannot accommodate the full pattern" plus the COGITATE null is offered as support for dualism — then the article itself later admits "an unsettled contest among materialist theories is not evidence for dualism." The admission never propagates back to retract the earlier claim.
- **Protective bracketing.** Decoherence deferred to another article; the interaction problem deferred; MWI's falsity assumed rather than argued ("if all branches persist equally, there is nothing for consciousness to select"); "minimal quantum influence" assumed energetically free.
- **Confession without correction (systemic).** The article self-labels its falsifiability as "borrowed," flags the PP total-framework as unconfronted, and notes the effort dissociations cut against its own reading — and changes no claim strength anywhere. Naming a defeater is treated as discharging it. This is the article's signature pathology.
- **Evidential-independence failure.** The five "interlocking components" are presented as convergent while the article's own appeal to the "common-cause null" concedes they largely reduce to one premise (partial reliability of introspective report / a single interface posit). Counting them as five independent confirmations is the error its own discipline names.
- **Tenet leakage.** Site vocabulary ("the Map's interface hypothesis," "policy-level selection," "bidirectional interaction in miniature") is embedded inside nominally neutral empirical exposition, pre-loading the dualist reading before it is argued.

## 3. BOTTOM-LINE VERDICT

**REVISE-HARD.** The article is not deletable: its citation metadata is clean, its AST section is genuinely good, and its Cai handling models correct calibration. But it cannot be retained as a positive argument for non-physical causation. It contains a fabricated empirical claim (the gamma bands), two author-stance inversions at the conclusion level (Sjöberg; Koch & Tsuchiya), and a self-admitted failure to confront the one rival framework (active inference / FEP) that accommodates all of its evidence. The confession-without-correction pattern means the article's rhetorical honesty is doing the work its arguments cannot: it tells the reader everything wrong with it and asserts its conclusion anyway. If the specific fixes below are not made — above all the fabrication and the two inversions — the correct disposition is **DEMOTE-TO-COHERENCE-ONLY**: retain as an internally consistent statement of a position, stripped of any claim to evidential support.

## 4. ARTICLE-SPECIFIC FIXES *(and 5. site-wide methodology improvements — combined concrete list, per instruction that the report end with these)*

**Article-specific (keyed to slugs):**

1. **`apex/attention-as-causal-bridge` — delete or re-source the gamma claim (BLOCKING).** Remove "conscious content correlates with low gamma oscillations (~55-65 Hz) while attentional control operates in high gamma (~75-90 Hz)" and the "Frequency analysis supports the separability" sentence in the Dualism tenet section. If a gamma argument is kept, restate it as the defensible, weaker pair: conscious access correlates with long-range gamma *synchrony* (Melloni et al. 2007), and attention with enhanced, modestly higher-frequency gamma synchronization (Fries 2015; Bosman et al. 2012), with the Ray & Maunsell 2011 caveat that high-gamma is largely a spiking proxy.
2. **`apex/attention-as-causal-bridge` — repair the Sjöberg inversion (BLOCKING).** State that Sjöberg 2024 concludes the SMA implements execution, not decision, and reads the finding as anti-dualist ("irrelevant to the neuroscientific discussion about free will"); then argue, on the Map's own separate grounds, why the retained sense of willing is nonetheless suggestive — never on Sjöberg's authority. Sweep sibling loci: check `concepts/mental-effort` and `concepts/libet-experiments` (the latter already cites Sjöberg).
3. **`apex/attention-as-causal-bridge` — de-invert Koch & Tsuchiya.** Add that they treat both dissociable processes as physical brain processes seeking a "material substrate"; mark the non-physical-subject reading as the Map's own, taken against the source's stated conclusion.
4. **`apex/attention-as-causal-bridge` — convert the PP/FEP confession into engagement or lower the claim.** Either discharge active inference (derive attention, effort, and agency from free-energy minimisation and isolate a genuine residue) or lower the article's positive thesis to match the concession that the rival accommodates the whole evidence base.
5. **`apex/attention-as-causal-bridge` — stop counting the five components as independent.** Apply the article's own common-cause null in-text: state that the components share the single premise of partially unreliable introspection and so are not five independent confirmations.
6. **`apex/attention-as-causal-bridge` — correct the COGITATE gloss and the overflow claim.** Report the asymmetric COGITATE outcome (IIT posterior-sufficiency corroborated, GWT prefrontal-necessity challenged) rather than a flat "null"; mark the Block-style overflow reading of Nartker as contested and note the authors' own criterion-artefact framing.
7. **`topics/attention-and-the-consciousness-interface` and `topics/structure-of-attention` — flag the willed/instructed marker inference.** The move from frontal-theta / frontoparietal-coherence markers to "consciousness's contribution" is a physicalist-to-dualist slide the cited authors (Bengson; Mangun) do not make; label it the Map's inference, not the data's.
8. **`concepts/decoherence` / `concepts/stapp-quantum-mind` — stop presenting the Zeno mechanism as live without in-text caveat.** Acknowledge that direct simulation (Georgiev 2015) shows the mechanism fails under environmental decoherence and that Itano et al. 1990 does not support Stapp's "Process 1" use; the apex should not defer this silently.

**Site-wide methodology improvements (argumentative/editorial discipline):**

1. **Institute a mandatory author-stance-at-conclusion gate.** Layer-1 metadata verification is demonstrably working (no fabricated citations found); stance verification is not. Every citation of a physicalist, functionalist, or illusionist author (Dehaene, Koch, Tsuchiya, Sjöberg, Graziano, Desmurget, Schurger, Haggard, Friston, Seth, Frankish) should carry a recorded note of the author's own conclusion and whether the Map's use runs with or against it. The Sjöberg and Koch & Tsuchiya inversions would have been caught.
2. **Treat uncited empirical claims as defects, not prose.** The gamma fabrication survived because it bore no citation and so escaped the citation ledger entirely. Any quantitative empirical assertion (specific Hz bands, bit-rates, millisecond latencies) must require a source or be explicitly marked unsupported, on par with citations.
3. **Adopt a confession-without-correction rule.** When an article names a defeater (decoherence, PP/FEP, borrowed falsifiability, common-cause dependence), the editorial standard must require that the downstream claim strength actually change. Self-disclosure of a weakness may not substitute for adjusting the conclusion. This is the single most consequential failure mode the article exhibits.
4. **Require strongest-rival discharge for any causal claim.** Predictive processing / active inference is a corpus-wide blind spot; this article admits its total-framework form goes unconfronted. Any article asserting a non-physical causal role for consciousness should be required to steelman and either defeat or concede to the free-energy account before asserting a residue.
5. **Enforce, not merely state, the independence audit for "convergent evidence."** The common-cause-null discipline exists but was not applied here. Convergence claims should require an explicit demonstration that the cited phenomena do not reduce to a shared premise or mechanism.
6. **Add a currency trigger on volition and stimulation evidence.** Reliance on Desmurget 2009 or Libet-era framing without engaging Karnath et al. 2010 and Schurger et al. 2012/2021 should raise an automatic currency flag.

## Verification Notes

Checked 2026-08-07 during outer-review processing. The reviewer's two "blocking" findings were checked at primary sources; **one is verified and one is refuted in its central claim.** The refutation matters for the remedy: the reviewer prescribes deletion where the evidence supports re-attribution.

**Verified claims:**

- ✓ **The gamma sentence is real and verbatim in the article.** `apex/attention-as-causal-bridge.md` L60 contains the quoted sentence exactly as reproduced. The reviewer did not fabricate the target quote — worth stating, because hostile outer reviews on this site have done so before.
- ✓ **The gamma claim is uncited at the apex locus.** L60 carries no inline citation, so the reviewer is right that it escaped the citation ledger.
- ✓ **Sjöberg 2024 is anti-dualist, and the apex does not say so.** Verified at the primary text (PMC11224596): *"In line with contemporary approaches to the mind–brain problem, dualism has been completely out of fashion in the neurosciences for almost half a century."* Sjöberg rejects Eccles's dualism and endorses Schurger's stochastic-accumulator reinterpretation. The apex recruits him at L84 and L162 toward "consciousness does genuine causal work" without marking that its author draws the opposite moral.
- ✓ **Sjöberg 2024 page range is 2267-2269**, as the reviewer states (Europe PMC, *Brain* 147(7), PMC11224596). Two research notes carry 2267–2274 and are wrong.
- ✓ **Koch & Tsuchiya 2007 did not supply the frequency bands.** They are cited as the source in `topics/structure-of-attention.md` L165–166 for numbers their paper does not report.

**Disputed claims (the reviewer is wrong):**

- ✗ **"A fabricated … claim … which corresponds to no primary source" — REFUTED.** The bands trace to a real experiment: **Wyart, V. & Tallon-Baudry, C. (2008), "Neural dissociation between visual awareness and spatial attention," *J. Neurosci.* 28(10):2667–2679, DOI 10.1523/jneurosci.4748-07.2008, PMID 18322110.** Its abstract reports "distinct and independent neural correlates of visual awareness and spatial attention at different frequencies in the gamma range (30-150 Hz)", with awareness-related **mid**-frequency gamma (54–64 Hz) and attention-related **high**-frequency gamma (76–90 Hz). The sibling ChatGPT review of the same subject independently identified this source; the two reviewers converge on the defect and diverge on its diagnosis, and ChatGPT has it right.
- ✗ **"Inverts what the actual gamma literature reports" — REFUTED.** Wyart & Tallon-Baudry assign the *lower* gamma band to awareness and the *higher* to attention, which is the same direction the article states. The reviewer's Melloni/Bosman/Fries/Ray-&-Maunsell reconstruction is about a different literature and does not establish an inversion.
- ✗ **Remedy misprescribed.** Because the numbers are real, the correct fix is **re-attribute and scope**, not delete. The genuine defects are misattribution (credited to Koch & Tsuchiya), an uncited apex locus, and overgeneralisation of a paradigm-specific MEG result (faint visual stimuli, contralateral visual cortex, 240–500 ms window) into fixed "operating frequencies". Deleting a real, correctly-directed finding would be a regression.

**Partially disputed:**

- ~ **Koch & Tsuchiya "structural inversion at the conclusion level."** The dissociation/ontology distinction is real, but the article does mark the gloss as its own — L60 opens "The Map's interpretation:" before making the non-physical-subject claim. What is genuinely missing is any statement that Koch and Tsuchiya are physicalists seeking a material substrate. This is a labelling gap, not an unmarked inversion.
- ~ **Sjöberg "sweep sibling loci."** The sweep is warranted but the Map is in better shape than the reviewer assumes: `topics/volitional-control.md` L53 already states *"Sjöberg is himself no dualist"* and that the cases "remove a defeater rather than confirming conscious causation", and `topics/motor-control-quantum-zeno.md` L55 already quotes his anti-Libet conclusion. The defect is an **internal inconsistency** — the Map knows the correct framing and does not apply it at the apex — which is a stronger and more tractable finding than the reviewer's.
- ~ **The Sjöberg quote is verbatim-correct where the Map uses it.** The reviewer renders it "in fact irrelevant"; the Map renders it "completely irrelevant to the neuroscientific discussion about free will". The primary text reads *"the findings made by Libet et al. are in fact completely irrelevant to the neuroscientific discussion about free will."* The Map's quotation is accurate and must not be "corrected" to match the reviewer's looser rendering.

**Unverified (carried forward as candidates, not findings):**

- ? The COGITATE asymmetry claim (IIT posterior-sufficiency corroborated vs GWT prefrontal-necessity challenged) is plausible but was not checked against the *Nature* paper in this pass.
- ? The claim that Nartker et al. frame their own result as a conservative-criterion artefact was not verified; their paper argues *for* preserved sensitivity, so the reviewer's gloss may itself be inverted. Check before acting.
- ? Georgiev 2015 on Zeno-mechanism collapse and the Ballentine critique of Itano et al. 1990 were not checked.

**Process finding:** the Koch & Tsuchiya misattribution was *introduced by an internal review*. `reviews/deep-review-2026-03-11-attention-as-interface.md` L30 records the uncited gamma claim being "**Resolved** — Added inline citation" by attributing it to Koch & Tsuchiya on the strength of a sibling article already doing so. The repair propagated the error rather than sourcing it. This is the strongest support in the review for its own methodology proposal #2 (treat uncited quantitative claims as defects), and it argues for a companion rule: a citation added to discharge an "uncited claim" flag must be verified against the source, not copied from a sibling.
