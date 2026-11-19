---
title: "Deep Review - The Phenomenology of Forgetting"
created: 2026-11-19
modified: 2026-11-19
human_modified: null
ai_modified: 2026-11-19T00:30:55+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-19
last_curated: null
---

**Date**: 2026-11-19
**Article**: [[phenomenology-of-forgetting|The Phenomenology of Forgetting]]
**Previous review**: [[deep-review-2026-08-17-phenomenology-of-forgetting|2026-08-17]]

## Scope

Fourth pass. Since the 2026-08-17 review, the body has changed in one sentence only. The expand-topic for `voids/learning-void` appended it to the "Retrieval-induced forgetting" paragraph on 2026-11-17, and the learning-void deep review edited it the same day. That sentence had never been checked against its sources on this page. This pass checked it, then followed the prior review's method note ("yield lives in quoted spans and empirical paraphrase") over the rest of the empirical surface. Each abstract was fetched raw from PubMed E-utilities (efetch, `rettype=abstract`), and the strings were grepped after collapsing whitespace. Full texts came from PMC efetch XML. No browser was used.

Three defects in the empirical paraphrase had passed earlier reviews. One was an inversion that the 2026-06-20 review recorded as verified.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Preregistered replication reported the wrong way round** (FIXED). Old L73 read: "while at least one preregistered study has reproduced it". The research note (L176) gives its source as Wiechert et al. 2023, *Memory* 31(7), 989–1002, and calls it "a successful pre-registered replication". The PubMed abstract (PMID 37165713) says the opposite: "Overall, we did not replicate the suppression-induced forgetting effect (same-probe: BF01 = 7.84 …)". The 2026-06-20 review (L43) wrote that this paper "reproduced the canonical below-baseline SIF effect", so the error was ratified, not caught. The 2026-08-17 review then certified the paragraph as "verified accurate against the live literature". A search for some other preregistered study that did reproduce the effect turned up only Wolsink, Jacob & Merz 2026 (*Collabra: Psychology* 12(1), preregistered analysis plan). Its abstract reports a same-probe effect that was "significant but small, and it was not supported by a Bayesian analysis". That does not support "reproduced" either. NEW: "A preregistered replication run online did not reproduce the effect, though its authors flag the online format as a possible reason (Wiechert et al., 2023)." The caveat is the abstract's own ("These null results should be considered in light of our online implementation"). Wiechert et al. was added to References.

2. **Clinical training result: a predictor was reported as an outcome** (FIXED). Old L103 read: "a training study found that practising suppression relieved symptoms of anxiety and post-traumatic stress (Mamat & Anderson, 2023)". In the paper, pandemic-related post-traumatic stress (Impact of Event Scale, IES) was measured as a pre-training predictor and a covariate. The outcomes were depression, state anxiety, worry, negative and positive affect, and well-being. Abstract (PMID 37729415): "participants reported less anxiety, negative affect, and depression … Participants high in trait anxiety and pandemic-related posttraumatic stress gained the largest and most durable mental health benefits." A search of the PMC full text (PMC10511195) for a reported reduction in IES scores returned nothing; the IES at follow-up fed the growth-curve model. NEW: "reduced anxiety, negative affect and depression, with the largest and most durable gains in people high in trait anxiety or in pandemic-related post-traumatic stress". The 2026-08-17 ledger had summarised the study correctly but wrote the slide into the article sentence. The clause "real consequences for a life, not merely a lab score" still holds.

3. **Learning-void host sentence**, the driver's lead (FIXED). Old: "…yet during practice the sense of learning follows ease, a misjudgement that delay and test experience reduced in experiments". The sentence opens by saying that learners misjudge a *method* (that self-testing aids retention), so "a misjudgement" reads as that method-level error. The two studies behind "delay and test experience" measured item-level judgements of learning. Koriat & Bjork 2006 (PMID 17128596): "foresight bias can be alleviated by study-test experience (Experiment 1), particularly test experience (Experiments 2 and 3), and by delaying JOLs after study (Experiment 4)". Rhodes & Tauber 2011 (PMID 21219059): "robust benefits to relative accuracy (g = 0.93)", gamma correlations between item JOLs and recall. For the method-level misjudgement about *testing*, the learning void's source is Tullis et al. 2013 (PMID 23242770). It found that learners "generalize that knowledge to future learning only with considerable guidance", and it found that cue-only JOLs reflected the testing benefit "both immediately and at a delay", so delay was not the lever there. The old clause is literally true of the item-level foresight bias but slides onto the method claim. The learning-void review asked for exactly this to be kept separate ("A later review should keep the three apart", its L155). NEW: "…and the way round is to check with a later test, the answer out of sight". This is the learning void's own thesis (L35 "has a plain way round: test yourself later, with the answer out of sight"; L77 "A delayed test with the answer covered measures the thing the feeling was standing in for"). It says the later test is a check, not a cure. Crosslink kept. One correction to the driver's lead: Yan, Bjork & Bjork 2016 is about interleaving, not retrieval practice, so the matching method-level source for testing is Tullis 2013. The lead's verdict that the old clause over-compresses is right.

### Medium Issues Found

4. **Wessel et al. 2020 paraphrase covered only half the result** (FIXED). Old: "found the below-baseline effect fragile across analytic choices". Abstract (PMID 32701389): same-probe effects were significant in "all (samples 2 and 4)" of the analyses, in "some tests (sample 3)", and in "only one test" in sample 1; "Recall probed with novel cues (Independent Probes, IP) predominantly rendered non-significant results. The absence of statistically significant IP suppression effects raises problems for inhibition theory". NEW: "found the below-baseline effect robust across analytic choices in some samples and fragile in others, and mostly non-significant when recall was tested with new cues, which the authors note raises problems for the inhibition account". This also gives the next sentence's "the mechanism remain[s] genuinely disputed" a source.

5. **Uncited compliance claim, stated more strongly than its source** (FIXED). Old: "and task compliance strongly moderates how large the effect appears", with no citation. The research note's source is Liu, Hulbert, Yang, Guo, Qiu & Anderson 2021, *Scientific Reports* 11, 20166 (Crossref-verified; PMC8505621). Its abstract: "In addition to successfully replicating SIF, we found that the magnitude of the effect was significantly and negatively correlated with participants' reported compliance". The full text: "suppression-induced forgetting declined with increasing memory checking". The authors also say the direction of cause is not established ("might be driven by a third variable"). NEW: "A large study that did reproduce it found less forgetting among participants who reported checking on or rehearsing the suppressed words against instructions (Liu et al., 2021)." This keeps the finding correlational and drops "strongly". Added to References.

6. **Dropped qualifier in the Anderson & Hulbert gloss** (FIXED). Old: "the prefrontal cortex exerts top-down inhibition over hippocampal mnemonic activity". Abstract (PMID 32928060): "top-down control over mnemonic activity in the hippocampus and other brain structures, often via inhibitory control". NEW: "exerts top-down control, often inhibitory, over mnemonic activity in the hippocampus". The quoted span "triggering windows of anterograde and retrograde amnesia in healthy people" was re-verified in the abstract (count 1).

7. **Nietzsche phrase in quotation marks was not the translation's wording** (FIXED). Old: Nietzsche's "active forgetting". The Samuel translation (archive.org `genealogyofmoral00nietuoft`, djvu text, Second Essay §1) reads "the utility … of the active forgetfulness" (count 1; "active forgetting" count 0). The "positive inhibiting force" gloss matches "a power of obstruction, active and, in the strictest sense of the word, positive". NEW: "active forgetfulness". A Nietzsche entry was added to References, since he is named in the body and had no entry.

8. **Two Further Reading glosses misdescribed their targets** (FIXED, checked against each page's current text):
   - `memory-anomalies`. Old: "distortions, false memories, and the limits of mnemonic reliability". The page covers déjà vu, jamais vu and cryptomnesia (title, L44). "False memory" occurs only in a reference title, and "distort" and "reliab" occur nowhere. NEW: "déjà vu, jamais vu and cryptomnesia, the last a forgotten memory mistaken for original thought" (L44: "cryptomnesia (a forgotten memory mistaken for original thought)").
   - `phenomenology-of-attention-to-absence`. Old: "…the converse of the shaped gap". The page gives James's tip-of-the-tongue gap as its own "Cognitive absence" case ("The gap is not empty; it has the shape of what is missing"). That is the same structure as this article's, not its converse, and the passage was already on the page when the gloss went in on 2026-06-26 (b64778cd16). NEW: "…with the tip-of-the-tongue gap as its cognitive case".

### Citation Web-Verify Ledger (publisher of record / PubMed raw abstracts)

- Anderson & Green 2001 — real-correct. The below-baseline framing is supported via Wessel's abstract ("fewer of those words than baseline words").
- Anderson, Bjork & Bjork 1994 — real-correct (PMID 7931095). "The impairment remains when output interference is controlled, suggesting a retrieval-based suppression that endures for 20 min or more"; the low-frequency result argues against blocking. Result leg matches.
- Anderson & Hulbert 2021 — real-correct metadata; paraphrase qualifier restored (item 6); quote verbatim.
- Schmitz et al. 2017 — real-correct (PMID 29101315): "greater resting concentrations of hippocampal GABA predicted better mnemonic control".
- Anderson, Crespo-García & Subbulakshmi 2025 — real-correct (PMID 40379896), as in the 2026-08-17 ledger.
- Davis & Zhong 2017 — real-correct (PMID 28772119); "the default state of the brain" verbatim, count 1; *Drosophila*, dopamine and Rac1 present.
- Gagnepain et al. 2017 — real-correct (PMID 28559378): "stopping episodic retrieval to suppress an unpleasant image triggers parallel inhibition of mnemonic and emotional content".
- Catarino et al. 2015 — real-correct (PMID 25847536): "Retrieval suppression was compromised significantly in PTSD patients".
- Mamat & Anderson 2023 — real-correct metadata; result leg corrected (item 2).
- Wessel et al. 2020 — real-correct metadata; result leg completed (item 4).
- Wiechert et al. 2023 — NEW; Crossref and PubMed verified; null result.
- Liu et al. 2021 — NEW; Crossref verified (6 authors; article 20166); replicated, compliance correlational.
- James 1890 — real-correct; "a sort of wraith of the name" re-grepped in the raw psychclassics ch. IX text (count 1), as were "intensely active" and "beckoning us in a given direction".
- Ricoeur 2004 — not re-fetched; covered by the stability note (verified twice).
- Nietzsche 1887 (Samuel trans.) — NEW entry; phrase corrected (item 7).
- Learning-void sources behind the host sentence (Koriat & Bjork 2006, Rhodes & Tauber 2011, Tullis et al. 2013, Yan et al. 2016, Roediger & Karpicke 2006, Kornell & Son 2009) — abstracts fetched raw; see item 3.

Currency sweep (`find_superlative_claims`): 0 hits. Inline ↔ References: complete in both directions after the additions. Directed forgetting stays uncited (see Remaining Items).

### Map-internal paraphrase re-grep (against current text)

- erasure-void "absence of absence" — holds (heading "The Phenomenology of Absence-of-Absence", L76; L80 "A void with no phenomenal signal cannot be approached at all from the inside").
- inaccessible-past "concludes that memory reconstructs rather than retrieves" — holds (description; §"Memory Is Reconstruction, Not Retrieval").
- consciousness-and-memory / reconsolidation "treat forgetting as a consolidation side-effect" — holds as a characterisation. CAM L86: "as the hippocampal contribution fades, those details erode"; reconsolidation L29: "the trace must be actively rebuilt or it is lost". Neither page uses the word "forgetting" in its body, so this is a gloss, not a quotation.
- "As the Map holds elsewhere, the conversation about consciousness *suggests* downward causation without exhibiting it from inside" — holds; `tenets/tenets.md` L93 carries this wording.
- agency-void "verification circularity" — holds (§"The Verification Circularity", L100–102).
- learning-void — item 3. memory-anomalies and attention-to-absence — item 8.

### Reasoning-mode classification (editor-internal)

- Engagement with the epiphenomenalist: Mode Three, unchanged. No label leakage. The over-concession check from 2026-08-17 still applies.

### Banned-construction checks

"This is not X. It is Y.": absent in new text. "load-bearing": absent. Relation to Site Perspective: present and substantive. YouTube embed block untouched.

## Optimistic Analysis Summary

### Strengths Preserved

- The volitional / sub-personal cordon, the four phenomenological textures, and the hand-off to the erasure void are untouched.
- "The Record Is Real but Contested" keeps its calibration. "real but contested" and "No quantitative suppression claim should be stated here as fact" are unchanged, and no effect sizes were added (stability note honoured). The corrections make the section more honest without shifting its overall verdict: the large replication (Liu et al.) and the preregistered null (Wiechert et al.) now both appear, which is what "contested" should mean.
- The Hardline Empiricist is better served. The clinical sentence now claims only what the single training study measured.

### Enhancements Made

- The replication record now names its sources (two new references) and carries the independent-probe result, which is where the mechanism dispute actually lies.
- The learning-void aside is shorter in what it claims and accurate to its target, and the crosslink is kept.

### Cross-links

- No new links. Two Further Reading glosses were corrected.

### Fit of the learning-void sentence (driver question)

It is acceptable where it is, as a one-sentence contrast. The hinge is real: retrieval practice costs the competitors (RIF) and benefits the practised items (the testing effect). The paragraph's job is to show control-driven forgetting, though, so the aside should stay one clause long. Do not expand it. If a later review finds it distracting, the right move is to put the link in Further Reading, not to add more learning-void content here.

## Word count

2,516 → 2,689 (+173) by `analyze_length`. About 75 words are the three new reference entries; the rest is the replication record (+~70) and the clinical sentence (+~15). Below the topics soft threshold of 3,000.

## Remaining Items

- **Directed-forgetting paragraph (L67) has no citations.** The research note (L126) puts the "unbinding" result in "2021 fMRI" work, without naming the paper. A later pass could identify and verify it, or attribute the paragraph more loosely. Low priority. Not minted.
- **Wolsink, Jacob & Merz 2026** (preregistered analysis plan; same-probe SIF significant but small, not supported by Bayesian analysis) could be added to the replication record if the paragraph is ever revisited. Not added now, to avoid over-weighting the null side beyond what is needed to remove the inversion.

## Stability Notes

- All prior notes stand: the epiphenomenalist standoff is bedrock; Ricoeur's "happy forgetting" stays quoted and unaffirmed; the James span is "a sort of wraith of the name".
- **Amended:** the think/no-think *calibration* ("real but contested", no effect sizes as fact) remains stable. The 2026-08-17 claim that the replication *detail* was "verified accurate against the live literature" was wrong: the "preregistered study has reproduced it" clause was inverted. Wiechert et al. 2023 is a **null** preregistered replication. Do not restore "reproduced" or "successful". The research note (L176) has been corrected with a dated bracket so it cannot re-seed the error.
- Mamat & Anderson 2023 measured post-traumatic stress as a *predictor* of benefit, not as an outcome. Do not re-word the sentence to "relieved post-traumatic stress".
- The learning-void sentence names the *way round* (a later test), not a remedy for the feeling. Do not reinstate "delay and test experience reduced" here. Those are item-level results, and the learning void keeps them apart from method judgements.
- Method lesson for this article: a prior ledger's "verified" on an empirical paraphrase means the paper was found, not that its result was read. This pass's three critical findings each came from reading the result sentence of an abstract the earlier ledgers had already cited.
