---
title: "Deep Review - The Structure of Attention"
created: 2026-11-13
modified: 2026-11-13
human_modified: null
ai_modified: 2026-11-13T18:49:39+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-13
last_curated: null
---

**Date**: 2026-11-13
**Article**: [[structure-of-attention|The Structure of Attention]]
**Previous review**: [[deep-review-2026-07-17-structure-of-attention|2026-07-17]] (eighth review overall)

This was a scorer pick at 119 days since the last review. It was a real review, not a no-op. Since 2026-07-17 the article absorbed `concepts/voluntary-attention-control-mechanisms` (the 2026-08-03 coalesce, which brought the thalamic, salience-network, spectral and stochastic-challenge material) and went through eight refine-drafts. No prior review had checked the stochastic-challenge, thalamic or contemplative passages against their sources. Each of the six critical findings below is a source-fidelity or calibration defect, which the issue-tracking rule allows to be flagged. None re-opens a bedrock point from the earlier stability notes.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **The contemplative section's neural claim contradicted its source literature and a sibling page (L210).** The article said "FA increases frontal theta and ACC activation (the willed-attention signature); OM reduces them and increases alpha." It cited nothing. Lomas, Ivtzan & Fu (2015) reviewed 56 EEG studies and found mindfulness "most commonly associated with enhanced alpha and theta power" (abstract checked verbatim at Europe PMC, DOI 10.1016/j.neubiorev.2015.09.018). `concepts/meditation-and-consciousness-modes` L56/L66 already carries this repair ("a rhythm split, theta for selection and alpha for witnessing, fails Lomas, Ivtzan and Fu's (2015) review"; "theta marks meditation rather than selection"). The repair never reached this page. **Fixed**: the sentence now says the evidence does not support a theta-for-focus, alpha-for-monitoring split, cites Lomas 2015 and links the sibling page.

2. **Stochastic challenge: an uncited finding, a misread interpretation, and a reply the source's design undercuts (L176–190).**
   - The alpha-predicts-choice finding had no citation. It is Bengson et al. (2014). **Fixed**: cited and added to References. The timing is now stated as the source gives it: "in the ~1,000ms before a choice prompt, but not earlier" (Nadra & Mangun 2023: "in the approximately 1,000 msec prior to free choice decisions (but not earlier)", grepped in the Frontiers full text).
   - The "attentional set" reading was glossed as "prior intentions" and "The brain tracks consequences of *previous* choices". Neither phrase is in the source. Nadra & Mangun say the alpha "may be a form of neural 'noise' … or may reflect variations in specific attentional sets …; the answer is not known." They also argue that the alpha "was not a reflection of a predetermined decision by the subject": choice prompts came on only 33% of trials, at intervals that varied randomly from 2 to 8 s, so subjects "would have had to have been clairvoyant" to decide in advance. The article's third reply ("Distal intentions … may track prior conscious choices") used the very reading the design was built to rule out, and did not say so. **Fixed**: the attentional-set reading is now stated neutrally, with the design argument. The distal-intentions reply now concedes that it is weaker here than against Libet. Replies 1 and 2 are unchanged.
3. **Filevich had a dropped qualifier (L180).** The article said the "cause" of free decisions "may be merely background noise". Filevich et al. (2013) wrote that "the cause of our 'free decisions' may at least in part, be simply the background stochastic fluctuations of cortical excitability" (grepped in the PMC3572111 full text). Their paradigm was also decisions to inhibit action, not choices of where to attend. **Fixed**: the sentence now reads "may be at least part of their 'cause' (Filevich et al. 2013, on decisions to inhibit action)".

4. **The thalamic DCM claim had no citation and overstated its source (L140–143).** The ascending pathways listed thalamic→ACC and thalamic→basal ganglia, and the descending pathway was called "voluntary modulation based on goals, rewards, and intentions". Both come from a secondary review's gloss (Huang, Li & Zhang 2023, *PeerJ*, PMC10274610, the research note's source). That review attributes the descending-voluntary reading to Connor, Egeth & Yantis (2004), not to the DCM study. The DCM study is Jagtap & Diwadkar (2016). It modelled thalamus↔dorsal PFC during a sustained-attention task with graded demand and found descending modulation rising with demand (abstract checked at Europe PMC; title confirmed at Crossref, "frontalthalamic" as published). **Fixed**: the pathways are restated as the study gives them, the study is cited, and the article now notes that it was "a demand manipulation, not a willed–instructed contrast".

5. **Dualism section: internal contradiction and calibration (L218).** "If consciousness were identical to neural processing, willed and instructed attention should show identical signatures" contradicted the article's own L200 ("The neural data are compatible with both interpretations"). An identity theorist expects different circuits for internally and externally sourced goals. A reviewer who accepts the tenets would still flag this. The 2026-10-26 tenet check had already flagged it (W5, Priority 4). **Fixed** with that review's prescribed NEW string, which brings the sentence into line with P-A1 and links `positions/agency-and-will#^p-a1`. There is one deliberate deviation. The prescribed clause "a physicalist expects endogenous and exogenous control to recruit different circuits" became "internally and externally sourced goals". Instructed attention is endogenous (top-down) control prompted by an external cue, as the article's own L70 says, so "exogenous" misnames the contrast. P-A1's wording was re-grepped before the link was installed: L68 reads "consistent with rather than establishing conscious engagement", and L48 reads "only the last of which argues for the framework rather than fitting it".

6. **Minimal Quantum Interaction section: an open question asserted as fact (L230).** The article said that "Thalamic gating, salience-network switching, and competitive selection … all involve junctures where outcomes are not fully fixed by prior physical states." No cited result shows this. Tenet coherence was being presented as evidence. **Fixed**: the sentence is now conditional: "If any resolution is not fully fixed by prior physical states—which the data neither show nor exclude—those junctures are the candidate sites".

### Medium Issues Found

- **Salience network (L158)**: the article said "When you *choose* to redirect attention … the salience network mediates that switch", as if this were Menon & Uddin's model. Their mechanism (2) is switching "when a salient event is detected" (abstract verbatim). **Fixed**: the voluntary case is now labelled the Map's extrapolation. It is supported by the willed-attention dACC result: Rajan et al. 2019's fMRI contrast lists "presupplementary motor area (dACC/pre-SMA) and anterior insula" among the regions "preferentially activated during willed condition".
- **Thura & Cisek (L112)**: the article said they "identified volitional commitment". Their abstract says "We propose that this … constitutes the volitional commitment". **Fixed**: the sentence now reports the finding and then "which they propose constitutes volitional commitment".
- **James (L96)**: the predicate was verbatim, but the subject was compressed ("the free-will question"). James wrote "The question of fact in the free-will controversy is thus extremely simple. It relates solely to …" (psychclassics.yorku.ca ch. XXVI; the "[p. 572]" marker follows, so p. 571 in the 1890 edition is confirmed). **Fixed**: the subject now reads "the question of fact in the free-will controversy", outside the quotation marks. The dropped "of fact" mattered, because James holds the question undecidable on psychological grounds.
- **Orphan references**: Koch & Tsuchiya (2007) and Schwartz & Begley (2002) were in References but cited nowhere in the body. The 2026-07-17 ledger missed both. The Koch entry has been an orphan since the 2026-08-07 re-sourcing of the gamma figures to Wyart & Tallon-Baudry. **Removed.**
- **The pre-choice bias was framed as implementation (L192, table L110)**: "establishes that conscious choices are implemented through neural mechanisms" became "establishes that choices are biased by prior neural states". In the table row, "constrain" became "bias", which is the source's verb.
- **Length** (3,869 at the start, hard limit 4,000): the additions above were offset by three cuts. The redundant L116 rider duplicated L228 and the timescale table. The L40 roadmap list was compressed. The fourth repetition of the three-signature list in the Occam section became "the three willed-mode signatures".

### Counterarguments Considered

- **Identity theory / physicalist reading of the willed–instructed data**: this is bedrock disagreement and stays bedrock. The fix in item 5 only makes the Dualism section say what L200 already said.
- **Neural-noise reading of pre-prompt alpha**: answered by replies 1 and 2 (selection among stochastic options; resolution mismatch). Both depend on the Map's framework and are presented that way. Reply 3 is now honestly weakened.

### Reasoning-mode classification (editor-only)

- Engagement with the physicalist critic (Structure and the Interface): Mixed (Mode Two then Mode Three). Unchanged.
- Engagement with identity theory (Dualism section): now Mode Three. The data fit without evidencing, and the boundary is stated honestly.
- Engagement with the neural-noise reading (Filevich; Bengson/Nadra & Mangun): Mode Three for replies 1–2. Reply 3 has been reduced from an implied in-framework rebuttal to an acknowledged weak reply.
- Engagement with illusionism / the eliminativist "post-hoc narrative" (Occam section): Mode Two. Unchanged.
- Buddhist no-self: Mode Three, with a data-persistence move. Unchanged.

No editor vocabulary appears in the article prose.

## Publisher-of-Record Citation Ledger

Metadata was checked at Europe PMC REST (or at the publisher's or Crossref's metadata) for every entry. Claims were grepped in full text where it was available.

- Rajan, Siegel, Liu, Bengson, Mangun & Ding 2019, *Cerebral Cortex* 29(7):2832–2843. **real-correct**. Result and direction confirmed in the PMC6611462 full text: theta 3–7 Hz; willed theta onset 470/510 ms; alpha-lateralization onset 730 vs 1190 ms (UF dataset); bidirectional Granger causality; RT and accuracy "did not differ significantly" (the Summary's "no reliable difference in task performance"); fMRI willed>instructed includes DLPFC and dACC/pre-SMA (the "Additional frontal recruitment" paragraph).
- Bengson, Kelley, Zhang, Wang & Mangun 2014, *J Cogn Neurosci* 26(11):2578–2584. **real-correct, added**. Abstract: occipital alpha "predicts choices about where human participants will focus spatial attention on a trial-by-trial basis". The ~1,000 ms window comes via Nadra & Mangun 2023.
- COGITATE Consortium 2025, *Nature* 642(8066):133–142. **real-correct**. PFC "temporal generalization … restricted to approximately 0.2–0.4 s" re-grepped in PMC12137136.
- Denton, Smith, Xu, Pugsley, Toghill & Kattnig 2024, *Nat Commun* 15:10823. **real-correct**. The "required 700 ns" of coherence was grepped in PMC11686217. The article correctly calls it a computational result.
- Filevich, Kühn & Haggard 2013, *PLoS ONE* 8(2):e53053. Metadata **real-correct**. A **dropped qualifier** in the article's paraphrase was corrected (item 3).
- Jagtap & Diwadkar 2016, *Hum Brain Mapp* 37(7):2557–2570. **real-correct, added**, replacing an uncited, overstated gloss (item 4).
- Lomas, Ivtzan & Fu 2015, *Neurosci Biobehav Rev* 57:401–410. **real-correct, added** (item 1).
- Menon & Uddin 2010, *Brain Struct Funct* 214(5–6):655–667. **real-correct**. The four mechanisms match the abstract. The voluntary-switch reading is now labelled as the Map's.
- Müller & Rabbitt 1989, *JEP:HPP* 15(2):315–330. **real-correct**. PDF grepped: "Maximum facilitation achieved by peripheral cues (100- to 175-ms SOAs) is greater than that achieved by central cues (at 400- to 725-ms SOAs)". The "requiring 300 ms to reach optimum" passage summarises Müller & Findlay, so the article's "earlier studies … near 300ms" is accurate.
- Nadra & Mangun 2023, *Frontiers in Cognition* 2:1205618, "Placing willed attention in context: a review of attention and free will". **real-correct**. It is now also cited for the design argument (item 2).
- Rizzolatti, Riggio, Dascola & Umiltà 1987, *Neuropsychologia* 25(1A):31–40. **real-correct**.
- Schwartz, Stoessel, Baxter, Martin & Phelps 1996, *Arch Gen Psychiatry* 53(2):109–113. **real-correct**. The abstract has 9 new patients "combined with … nine similar subjects from the previous study", so "18 participants" means the pooled analysis. It also says "replicate … previous findings" within the UCLA group, which is consistent with the article's "not replicated with the same method outside the UCLA group". Kept.
- Thura & Cisek 2014, *Neuron* 81(6):1401–1416. **real-correct**. The ~280 ms figure and the PMD-peak/M1-suppression description match the abstract. The "identified" overstatement was corrected.
- Wyart & Tallon-Baudry 2008, *J Neurosci* 28(10):2667–2679. **real-correct**. 54–64 Hz and 240–500 ms (awareness) and 76–90 Hz (attention) were grepped in PMC6671201.
- Koch & Tsuchiya 2007 (TICS 11(1):16–22) and Schwartz & Begley 2002. Metadata real, but **orphans: removed**.
- James 1890, *Principles* vol. 2 ch. XXVI p. 571. **Verbatim**, grepped at psychclassics.yorku.ca. Subject compression fixed (medium item).

No superlative or currency claims were found (the `find_superlative_claims` helper returned nothing).

**Cited-author stance**: Rajan/Bengson/Nadra/Mangun, Filevich/Haggard, Menon/Uddin, Thura/Cisek, Wyart/Tallon-Baudry, Lomas, Jagtap/Diwadkar and Denton/Kattnig take no dualist position. Haggard, and Thura & Cisek, give physicalist mechanism accounts of volition. The article presents none of them as endorsing the Map's reading; every interpretive step is marked as the Map's. Schwartz is himself a mental-force dualist, and the article cites only his PET result, with the Hebbian alternative noted. James held free will undecidable on psychological grounds and is cited only for framing the effort question.

**Map-internal quotations**: the article quotes no other Map page. The two glosses edited this pass were re-grepped against the current text: `meditation-and-consciousness-modes` L56/L66, and P-A1 (`positions/agency-and-will` L48/L68). The transit-void gloss (L56) matches that page's L113/L127.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-mode taxonomy, with per-mode tables and first-person phenomenology.
- The 2026-10-12 timing repair. Willed deployment is delayed relative to instructed, with the 1,190 vs 730 ms figure, and the "a purely physical decision process would take the same time" rider. Both were re-verified and kept verbatim.
- The 2026-08-07 spectral scoping, which notes that the three rows come from different paradigms and are not three confirmations. The Hardline Empiricist praises it. Left untouched.
- The honest "suggestive rather than decisive" rider on the physicalist counter-interpretation, which the Dualism section now matches.
- The four falsification criteria, and the Buddhist no-self reply at the level of phenomenology.

### Enhancements Made

- The salience-network section is now tied to the willed-attention dACC/anterior-insula result rather than to an unsourced claim about voluntary switching (Chalmers/Kane personas: the interface claim now has a named empirical link).
- The contemplative section now links its sibling page, which carries the corrected evidence.

### Cross-links Added

- [[meditation-and-consciousness-modes]] (body, piped)
- [[positions/agency-and-will#^p-a1|P-A1]] (body)

## Remaining Items

- Outside this article's scope, listed and not edited: `concepts/attention-as-interface` L202 still says "Pre-decision EEG alpha activity predicts free choices ~1000ms before participants decide", with no citation and the same window misstatement. It is the only other live locus; the grep covered topics, concepts, apex, voids and positions. It is small (one sentence, citation plus window), so it is recorded here and not tasked.
- Low and deferred: "Advanced practitioners report increasingly fine-grained awareness of the willed/captured distinction" (L210) has no citation. It is a phenomenological-report claim and is plausible. Assigning exogenous capture to the ventral network alone (L56) is a textbook simplification.
- Length is at 3,993 against a hard gate of 4,000, so future additions must be length-neutral.

## Stability Notes

- The earlier bedrock notes all stand and were not re-opened: physicalist reading, Zeno skepticism, MWI, Buddhist no-self, Schwartz evidence quality.
- **A note for future passes.** The 2026-06-02/06-20 notes said "future reviews need not re-verify". That exemption covered seven references. It did not cover the coalesced material (thalamic, salience, stochastic, contemplative) or the uncited claims, and that is where every defect this pass was found. A stability note exempts verified references. It does not exempt a passage added after the note was written.
- The stochastic challenge is now calibrated to the source. Do not restore "prior intentions" or "tracks consequences of previous choices" as the attentional-set reading. Do not drop the concession in reply 3. The Bengson/Mangun design (33% choice trials, 2–8 s random ITI, debriefing) is the reason.
- The contemplative section must not reintroduce a theta-for-focus, alpha-for-monitoring split. Lomas 2015 is the controlling review, and the sibling page carries the same repair.
- The Dualism section now matches P-A1 ("fit without evidencing"). If P-A1 is re-graded, update this sentence as well.
