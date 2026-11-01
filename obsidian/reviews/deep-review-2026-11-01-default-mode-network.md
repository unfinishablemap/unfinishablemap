---
title: "Deep Review - Default Mode Network"
created: 2026-11-01
modified: 2026-11-01
human_modified: null
ai_modified: 2026-11-01T22:52:33+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-01
last_curated: null
---

**Date**: 2026-11-01
**Article**: [[default-mode-network|Default Mode Network]]
**Previous review**: [[deep-review-2026-07-09-default-mode-network|2026-07-09]] (eighth pass; this is the ninth)

## Why this article, and what moved under it

This was the top deep-review candidate once today-edited articles and open-task File targets were excluded. Three edits have landed since the 07-09 review: 07-30 (the Kral/Fox structural-change hedge), 08-08 (an inbound-gloss relabel) and 09-07 (the Siegel/Doss re-characterisation of the psychedelic evidence, plus the entropic-brain criticality sentence). Together they took the article from 2601 to 2955 words. None of those additions had been through a deep review. Its dependencies `psychedelics-and-the-filter-model` (09-09), `consciousness-under-extreme-metabolic-constraint` (09-23), `witness-consciousness` and `meditation-and-consciousness-modes` (October) and `self-construction-constructor` (10-14) have also changed since then.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Result-direction error: psychedelic therapy and the DMN (old L129).** The article said: "Treatments that reduce rumination—mindfulness-based cognitive therapy, psychedelic-assisted therapy—also reduce DMN hyperactivity. Breaking the DMN's grip correlates with symptom relief." The available evidence points the other way. Carhart-Harris et al. 2017 (*Sci Rep* 7:13187, open-label, 16 patients with usable fMRI) report "increased RSFC was observed within the default-mode network (DMN) post-treatment". Their predictor of response was *increased* vmPFC–inferior-lateral-parietal connectivity, which links two DMN nodes. **Fix**: replaced with the verified finding, labelled as small and open-label: "symptom relief went with a reorganised DMN, not a silenced one." The MBCT half of the claim was uncited and has been removed, not rewritten.
2. **Currency drift: "Major depression shows hyperactive DMN" (old L127).** This was stated flatly. Yan et al. 2019 (*PNAS* 116(18):9078–9083; REST-meta-MDD, 848 patients vs 794 controls after exclusion) found "reduced rather than increased FC within the DMN", and only in recurrent MDD, not first-episode drug-naive patients. **Fix**: re-scoped to "has often been linked to heightened DMN activity and connectivity", followed by the Yan qualification. I first wrote "The largest pooled sample" and changed it to "A large pooled sample": a superlative would need its own currency check, and UK Biobank-scale analyses may since have exceeded the REST-meta-MDD sample. "The DMN keeps running when it should quiet" was deleted.
3. **Result framing: Siegel et al. 2024 (old L104).** The article said psilocybin dissolves network distinctions "rather than suppressing the DMN specifically". The paper's own abstract says "Psilocybin-driven FC changes were strongest in the default mode network". The Fig. 1d legend reports a spin test with P_spin < 0.001 for the DMN and P_spin > 0.05 for every other network. The old sentence implied the DMN was not specially affected. **Fix**: "the DMN changed more than any other network, but by desynchronizing rather than simply going quiet". I added the sample size ("tracking seven participants": the figure legend gives the imaging timeline for 7 participants, and most analyses use n = 6). The closing sentence changed from "The DMN still participates … what does not survive is the inference" to "The DMN remains central … what weakens, on this small evidence base, is the inference … *explained by* reduced DMN activity specifically". This brings it in line with the dependency's own calibration ("a shift of emphasis rather than a settled result").
4. **Attribution/strength: Doss et al. 2022 (old L104).** The old text said Doss "set out a cortico-claustro-cortical model on which the claustrum is a proximal trigger for cortical desynchronization, with DMN disruption downstream", framed as "The 2020s mechanism literature has also shifted explanatory weight upstream". The paper's own wording is: "we propose that the claustrum entrains canonical cortical network states, and that psychedelic drugs disrupt 5-HT2A-mediated network coupling between the claustrum and the cortex, leading to attenuation of canonical cortical networks." The "trigger neurons" language belongs to a rodent study Doss cite (their ref. 19). Doss also add that "cortical layer V pyramidal neurons … and the thalamus could also be directly involved". **Fix**: "Doss et al. (2022) propose a cortico-claustro-cortical model on which psychedelics disrupt the claustrum's coupling with cortex and so attenuate canonical cortical networks, the DMN among them". The "literature has shifted" frame became "Mechanism models have also looked upstream", and "is spread across" became "looks spread across".
5. **Date error in the lead (old L34).** "Discovered by Marcus Raichle in the early 2000s" was wrong. Raichle 2015 says the discovery "was an unexpected consequence of brain-imaging studies first performed with positron emission tomography". Shulman et al. 1997 (*J Cogn Neurosci* 9(5):648–663, Raichle a co-author) is the 1990s PET deactivation study. Raichle et al. 2001 named the "default mode". **Fix**: "Named by Marcus Raichle and colleagues in 2001, after 1990s PET studies had shown its regions deactivating during tasks (Raichle et al., 2001; Raichle, 2015)".
6. **Orphan References (old L231, L235, L234, L239).** Buckner et al. 2008, Carhart-Harris et al. 2012, Carhart-Harris & Friston 2019 and Raichle 2015 had no inline citation. The 07-09 ledger's "no orphans either direction" was a surname-level check: "Raichle" and "Carhart-Harris" appear in the body, but not those works. **Fix**: inline cites added. Buckner 2008 now supports the anatomy list, whose regions match Buckner's core set. Carhart-Harris 2012 supports the psilocybin DMN-reduction claim. REBUS is now attributed to "Carhart-Harris and Friston's REBUS model (…; 2019)"; it had been credited to Carhart-Harris alone. Raichle 2015 supports the lead.
7. **Navigation surface misstates its target (Further Reading).** The `consciousness-under-extreme-metabolic-constraint` gloss read "DMN suppression as evidence that metabolic reduction intensifies rather than dims experience". That page now says the opposite (L63): "The psychedelic case therefore does not show consciousness intensifying as metabolic supply falls … Of the five lines of evidence here, this one discriminates least … it is often cited as metabolic evidence for the filter model, and it is not." **Fix**: "Consciousness failing to track metabolic supply; psychedelic DMN reconfiguration, with metabolism rising, is the line that discriminates least".

### Medium Issues Found

- **Differential-prediction overclaim (old L153).** "Filter theory would predict exactly this: the filter serves survival, not wellbeing" implied filter theory had a prediction that production accounts lack. Elsewhere the article is careful about this ("Both production and filter models predict this convergence"). **Fix**: "Filter theory accommodates this—the filter serves survival, not wellbeing—though a production account shaped by natural selection predicts the same."
- **Calibration wording in Relation to Site Perspective / Dualism (old L179).** "Evidence for this reading comes from…" sat awkwardly next to the same paragraph's "neither interpretation is forced by the data alone". It now reads "The reading draws on…". The paragraph was tightened, and every calibration qualifier was kept.
- **Over-reach in the contemplative-convergence paragraph (old L119).** "The convergence confirms the DMN's role in self-referential processing" drew a neural conclusion from phenomenological convergence. That clause was deleted and the frameworks-indistinguishable conclusion kept.
- **Apex gloss shifted a framework commitment into "on either reading" (Further Reading).** The `self-construction-constructor` gloss attached "on either the production or the filter reading" to the minimal-self claim. The apex (L85) marks that claim as resting on the Map's three-layer model and Tenet 1 subject-realism, which Dennett "rejects at the source". **Fix**: "…built (on the Map's three-layer model) upon a minimal self it cannot produce".
- **Redundancy: REBUS stated twice.** The "DMN and Predictive Models" subsection repeated the REBUS paragraph in the psychedelic section almost word for word, and called the DMN "the brain's primary system for maintaining self-related predictive models", which is uncited. The subsection was deleted. Its one distinctive gloss ("who one is, what one values, what to expect") and the `[[predictive-processing]]` body link were folded into the REBUS sentence.
- **Uncited lesion claims (L73).** "Patients with mPFC lesions show reduced self-reflection; PCC damage impairs autobiographical memory…" These were not fixed (see Remaining Items).

### Publisher-of-Record Citation Ledger (§2.4)

All metadata was checked against Crossref (DOI lookups). Claim-level checks used the PubMed abstracts, plus full text where stated.

- Buckner, Andrews-Hanna & Schacter 2008 (*The Brain's Default Network*), *Ann NY Acad Sci* 1124(1):1–38, DOI 10.1196/annals.1440.011. Status: real-correct. Now cited inline.
- Fox, Nijeboer, Dixon et al. 2014, *Neurosci Biobehav Rev* 43:48–73, DOI 10.1016/j.neubiorev.2014.03.016. Status: real-correct. The abstract confirms 21 studies, ~300 practitioners, d = 0.46, and "Publication bias and methodological limitations are strong concerns". The "largely cross-sectional" description is confirmed in Kral et al. 2022's full text (Europe PMC): "Most of the included studies focused on cross-sectional research of long-term meditation practitioners".
- Kral, Davis, Korponay et al. 2022, *Sci Adv* 8(20):eabk3316, DOI 10.1126/sciadv.abk3316. Status: real-correct. The abstract confirms n = 218 meditation-naive participants, waitlist and "validated, matched active control" arms, and "no evidence that MBSR produced neuroplastic changes compared to either control group". The article's "218 participants with both waitlist and active controls … no structural change from 8-week MBSR" is faithful.
- Carhart-Harris & Friston 2019 (REBUS), *Pharmacol Rev* 71(3):316–344, DOI 10.1124/pr.118.017160. Status: real-correct. The body attribution now includes Friston.
- Carhart-Harris et al. 2012, *PNAS* 109(6):2138–2143, DOI 10.1073/pnas.1119598109. Status: real-correct. Now cited inline for psilocybin specifically, since the study tested only psilocybin.
- Carhart-Harris, Roseman, Bolstridge et al. 2017, *Sci Rep* 7:13187, DOI 10.1038/s41598-017-13282-7. Status: real-correct, NEW. Direction checked: within-DMN RSFC *increased* post-treatment; open-label; 16 of 19 patients had usable data.
- Killingsworth & Gilbert 2010, *Science* 330(6006):932, DOI 10.1126/science.1192439. Status: real-correct. The 46.9% figure was grep-verified in the paper's PDF (control term "wandering": 20 hits): "Mind wandering occurred in 46.9% of the samples". "Approximately 47% of waking hours" is a fair experience-sampling estimate. Left unchanged.
- Gross, Raynes, Schooler, Guo & Dobkins 2025, *Emotion* 25(3):671–682, DOI 10.1037/emo0001434. Status: real-correct. The abstract confirms "the relationship between attention state and mood is substantially accounted for by thought valence".
- Raichle, MacLeod, Snyder, Powers, Gusnard & Shulman 2001, *PNAS* 98(2):676–682, DOI 10.1073/pnas.98.2.676. Status: real-correct. The abstract supports a "group of areas that consistently exhibit decreases" during goal-directed behaviour.
- Raichle 2015, *Annu Rev Neurosci* 38:433–447, DOI 10.1146/annurev-neuro-071013-014030. Status: real-correct. Now cited inline for the PET-discovery history.
- Siegel et al. 2024, *Nature* 632(8023):131–138, DOI 10.1038/s41586-024-07624-5. Status: real-correct metadata, **framing corrected** (critical issue 3). Full text was checked via Europe PMC.
- Doss, Madden, Gaddis, Nebel, Griffiths, Mathur & Barrett 2022, *Brain* 145(2):441–456, DOI 10.1093/brain/awab406. Status: real-correct metadata, **model characterisation corrected** (critical issue 4). Full text was checked on PMC (PMC9014750).
- Yan, Chen, Li et al. 2019, *PNAS* 116(18):9078–9083, DOI 10.1073/pnas.1900390116. Status: real-correct, NEW. Direction checked: DMN FC reduced, recurrent MDD only, associated with medication.

**External quotation**: Huxley's "reducing valve". This was grep-verified in an archive.org full text of *The Doors of Perception* (control "Mind at Large": 9 hits). The passage reads: "To make biological survival possible, Mind at Large has to be funneled through the reducing valve of the brain and nervous system." The article's paraphrase ("narrows consciousness to what is useful for biological survival") is faithful.

**Superlative scan** (`find_superlative_claims`): no hits before or after the edits.

**Inline ↔ References**: after the edits, every References entry has a body attribution and every body attribution has an entry.

### Map-internal dependency check

- `psychedelics-and-the-filter-model#The Neuroimaging Paradox`: the anchor resolves. The target's restatement is now no stronger than the dependency's own calibration. The dependency carries the same Siegel and Doss framing defects (see Remaining Items).
- `entropic-brain-hypothesis`: the target's criticality sentence ("under DMT, criticality and complexity fall while entropy rises, and complexity can rise as awareness falls under ketamine") matches that page's L62–66 (Rankaduwa & Owen 2023; Irrmischer et al. 2026). No change needed.
- `witness-consciousness` / `meditation-and-consciousness-modes` (October edits): Brewer 2011 is now read as finding DMN deactivation that is "meditation-general". The target makes no witness-specificity claim, so there is no conflict.
- The `tenets` anchors `^dualism`, `^bidirectional-interaction`, `^minimal-quantum-interaction` and `^occams-limits` all resolve. All 20 body and frontmatter wikilink targets resolve to live files.
- Map-internal quotations: the target quotes no Map page verbatim. Its glosses were checked, and two were fixed (critical issue 7 and the apex gloss).

### Reasoning-mode classification (editor-internal)

- Physicalist objection in "The DMN as Narrative Filter": Mode Three, unchanged and honest.
- Carhart-Harris/REBUS physicalist reading: Mode Three (framework boundary noted).
- Physicalist account of meditation in Bidirectional Interaction: Mode Three ("a philosophical interpretation of the data, not a claim that neuroscience requires it").
- Label-leakage scan: clean. "This is not X. It is Y." scan: clean. "load-bearing": absent.

### Possibility/probability slippage

None was introduced. Two existing soft spots were corrected in the conservative direction: "Evidence for this reading comes from" and "Filter theory would predict exactly this". The Siegel/Doss closing sentence now carries a small-evidence-base qualifier.

## Optimistic Analysis Summary

### Strengths Preserved
- The production-versus-filter framing is balanced throughout. "Neither reading is forced by the data alone" is kept at every site.
- The falsifiability section ("What Would Challenge This View?") is unchanged.
- The Kral/Fox structural-change hedge from 07-30 is unchanged.
- The Killingsworth & Gilbert / Gross qualification ("do not re-broaden it", 07-09) is unchanged.
- The entropic-brain criticality sentence (09-07) is unchanged.
- The four tenet connections are intact. No Many Worlds is correctly skipped.

### Enhancements Made
- The depression subsection now reports the evidence in the direction it actually runs, which is more interesting for the Map: the DMN that relieves depression is a reorganised one, not a silenced one.
- The psychedelic paragraph now carries Siegel's DMN-prominence finding. This makes the DMN-filter reading neither stronger nor weaker than the data allow.

### Cross-links Added
- `[[predictive-processing|prior beliefs]]` (moved into the REBUS sentence from the deleted subsection)
- `[[#The Psychedelic Evidence|psychedelic evidence]]` (in-page anchor, Dualism section)

## Length

`analyze_length` (concepts soft 2500 / hard 3500): **2955 → 2954** (−1, soft_warning). The fixes needed about +115 words: two new references, four inline cites, and the depression, Siegel and lead rewrites. These were offset by deleting the duplicate "DMN and Predictive Models" subsection (−78 with heading, about +12 folded back), two filler sentences (old L63 opener and the Occam correlation sentence) and the over-reaching convergence clause, by tightening the GWT intro and the Executive Gateway close, and by shortening the apex gloss.

## Remaining Items

- **Lesion claims (L73) are uncited.** Philippi et al. 2012 (*J Cogn Neurosci*, "Medial PFC damage abolishes the self-reference effect") would support the mPFC half. Philippi et al. 2012 (*PLoS ONE*, preserved self-awareness after extensive insula/ACC/mPFC damage) bears directly on falsifier #4 and would be a genuine expansion. Neither was verified this pass, and there is no length headroom for them.
- **Anxiety subsection (L131–133)** is uncited and vague. It is low priority.
- **Out of scope, not fixed (cross-page leads):** the same Siegel framing ("rather than suppressing the DMN specifically" / "rather than suppression of this one in particular") appears in `topics/psychedelics-and-the-filter-model` L63, `apex/self-construction-constructor` L85 and `apex/altered-states-as-interface-evidence` L88. All three omit Siegel's own finding that FC change was largest in the DMN. `psychedelics-and-the-filter-model` L67 also carries the Doss "proximal trigger … DMN disruption downstream" gloss, and its "2020–2025 literature has also shifted explanatory weight upstream" rests on one review plus Mason 2020.

## Stability Notes

- Carried forward from 07-09: the eliminative-materialist, phenomenological-reliability and quantum-speculation objections are bedrock framework-boundary disagreements. Do NOT re-flag them as critical.
- **Length**: 2954 words (118% of soft). Future passes stay length-neutral. The cheap slack (the duplicate REBUS subsection, filler openers) is now spent. Further fixes will need trims from Further Reading glosses or the Relation to Site Perspective prose.
- **Depression evidence**: the section now reports the mixed record (heightened DMN in many studies, reduced connectivity in REST-meta-MDD, increased DMN connectivity after psilocybin therapy). Do not restore a flat "hyperactive DMN" or "treatment reduces DMN" claim without a newer source that reverses Yan 2019 or Carhart-Harris 2017.
- **Siegel 2024**: the DMN was the most affected network. Do not re-word it back into "not DMN-specific".
- **Convergence**: this was the ninth pass. Its defects were all in content added after 07-09 or in uncited claims that earlier passes had never source-checked. The argumentative frame is stable.
