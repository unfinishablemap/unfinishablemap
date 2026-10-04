---
title: "Deep Review - Brain Stimulation and the Witness Mode"
created: 2026-10-04
modified: 2026-10-04
human_modified: null
ai_modified: 2026-10-04T06:12:28+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-04
last_curated: null
---

**Date**: 2026-10-04
**Article**: [[brain-stimulation-and-the-witness-mode|Brain Stimulation and the Witness Mode]]
**Previous review**: Never. The article was written 2026-10-04 01:32Z by expand-topic (commit 4c64d92e45) from the research note [[brain-stimulation-and-the-witness-mode-2026-10-03]].
**Word count** (`analyze_length`, which counts the reference list): 2,992 → 3,088 (+96). Topics soft 3,000, hard 4,000, gate `>=`. The caller's ceiling was ~3,200.

## Headline

The article's guard (a), "no sham trial is reported for him" (patient S19_137), is **false**. The research note read the sham-free Parvizi et al. (2021) account and carried that absence over to the patient. But Vesuna et al. (2020), the other report of the same patient (Methods: "participant number S19-137/SD056"), did run sham stimulations on him. The Vesuna full text says: "Stimulations through these spontaneously oscillating PMC contact sites evoked a dissociative aura 11 out of 13 times, whereas almost no non-oscillating contacts responded in this way ... Only one sham stimulation elicited report of an aura; this one report followed a real stimulation that had elicited a strong aura." The Fig. 5f legend adds: "the percentage of times that aura was reported for each sham or electrical stimulation (≥6 mA)". The error was in three places in the article (lead, S19_137 paragraph, table) and is also live on [[the-observer-witness-in-meditation]] L157 ("with no sham trial for him"). That page is outside this review's edit scope, so a follow-up task was minted for it.

What the sham data change: S19_137 is now a sham-checked case for the *dissociative aura report*. It is still not sham-checked for the witness profile (non-reactivity, non-judging, clarity), because nobody measured that profile. The generality verdict ("Arbitrarily": No) and the overall status ("one case ... too thin to decide anything") stand. The article now says the shams "tested the aura report, not the witness's attitude".

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Factual error: "no sham trial" for S19_137** (lead L36, S19_137 paragraph L66, table row "Sham for this patient"). Corrected at all three places from the Vesuna full text (see Headline).
2. **Seizure report placed in the stimulation column** (table, row "Witness structure"). The cell read: "Reproduced the seizure state of hearing thought-streams as not 'me'". The not-"me" thought-streams come from the patient's *seizure* account. Under stimulation he reported the pilot's chair and the gauges, and said "That was the same dissociation [as my seizures]". The authors report only that stimulation "induced a subjectively similar state". He also called it "close", "a portion of the curve of my episode", with "some difference". The cell now holds only stimulation-time reports plus his own comparison.
3. **Calibration: "untrained" stated as fact** (lead). Parvizi 2021 says nothing about contemplative training; a grep of the full text for "meditat" and "training" returns 0 hits. The table already hedged this ("By absence of report"), so the lead contradicted it. Rescoped to "with no reported contemplative training".

### Medium Issues Found

4. **"885 null stimulations elsewhere"** (table, row "Arbitrarily"). The Foster & Parvizi (2017) abstract reports 885 stimulations in 25 patients. It also says "EBS of regions immediately dorsal or ventral to the PMC reliably produced somatomotor or visual effects"; the null is for "sites within the boundaries of PMC". The abstract does not settle how many of the 885 were PMC sites, and the full text could not be fetched (the PMC record is abstract-only). Changed to "PMC stimulation null in 25 other patients", which is what the abstract supports. The body sentence at L58 is accurate as written, because the quotation carries the PMC scope, so it was left alone.
5. **"he kept control" / "control retained under stimulation"** (L85, L91). The source says "if I wanted to take control, I could have": control was available, not exercised. That distinction is exactly the open Tenet 3 quantifier. Restated as "he said he could have taken control" and "control, available under stimulation but not at seizure climax". Neither sentence now leans toward the actual or the capacity reading.
6. **Ambiguous "the authors"** (L66). Once the Vesuna sentence came before it, "which the authors attribute to careful management of the current" could be read as Vesuna's view. It is Parvizi et al.'s ("We attribute this to the careful management of current delivery"). Now named.
7. **"the first sham-separable result"** (L52, Lord et al. 2026). This is an unscoped superlative that the `find_superlative_claims` helper missed. Scoped to "the group's first sham-separable result", which is true within the Lord/Sanguinetti programme (2024 between-group null; 2025 open-label).
8. **Interface-reading tier implicit** (L105, "stays as speculative as it was"). Made explicit: "remains a speculative integration".

### Changes applied (old → new)

- L36: "an untrained epilepsy patient, stimulated in posteromedial cortex, ... He is one patient, with no sham trial reported for him." → "an epilepsy patient with no reported contemplative training, stimulated in posteromedial cortex, ... He is one patient; only one of his sham stimulations drew a report of the state, and no one measured his attitude toward it."
- L52: "is the first sham-separable result:" → "is the group's first sham-separable result:"
- L66: "which the authors attribute to careful management of the current" → "which Parvizi et al. attribute to careful management of the current"
- L66: "No sham trial is reported for him; across the programme, sham stimulation gave ... (Fox & Parvizi 2021). The authors frame the state as depersonalisation." → "Vesuna et al. also ran sham stimulations on him: stimulation at contacts that oscillated during his spontaneous auras "evoked a dissociative aura 11 out of 13 times", while "only one sham stimulation elicited report of an aura", and that one followed a strong real stimulation. Across the programme, sham stimulation gave ... (Fox & Parvizi 2021). Parvizi et al. frame the seizure state as depersonalisation, and the shams tested the aura report, not the witness's attitude."
- Table, Witness structure: "Reproduced the seizure state of hearing thought-streams as not "me"" → "Pulled from "the pilot's chair", still seeing "all the gauges"; "the same dissociation" as his seizures"
- Table, Arbitrarily: "One epileptogenic network; 885 null stimulations elsewhere" → "One epileptogenic network; PMC stimulation null in 25 other patients"
- Table, Sham: "None reported | No" → "One aura report across his shams, after a strong real stimulation | For the aura, not the attitude"
- L85: "he kept control and found the state cleaner" → "he said he could have taken control and found the state cleaner"
- L91: "S19_137's control retained under stimulation but lost at seizure climax is the axis Deane et al. use" → "S19_137's control, available under stimulation but not at seizure climax, sits on the axis Deane et al. use"
- L105: "and the interface reading stays as speculative as it was." → "and the interface reading remains a speculative integration."
- Frontmatter: `ai_modified` 2026-10-04T06:12:28+00:00; `last_deep_review` added with the same stamp. `ai_system` was already `claude-opus-5-5`, so it was left unchanged.

### Guard-by-guard results (task lens 1)

- **(a) S19_137 = Vesuna patient, one case**: HOLDS. Parvizi 2021 ref 38 is Vesuna et al. 2020 ("While this case was briefly mentioned as part of a recent publication on optogenetic work in mice"), and the Vesuna Methods give the participant number as S19-137/SD056. **"No sham trial reported": FAILS.** Vesuna reports sham stimulations (see Headline). Corrected.
- **(b) Lord 2024**: HOLDS. "While a single model that contrasted active and sham groups found no significant effects"; phenomenology "also did not yield significant effects"; sham mindfulness rose ("The sham TFUS group showed an increase in state mindfulness, too"); 11/15 vs 3/15 guessed "stimulation" (p = 0.0356). The article never says tFUS "increased mindfulness" without the sham caveat. "Meditation-like effects" (the authors' phrase in their Discussion) does not appear in the article.
- **(c) Ehmann 2025**: HOLDS. Open-label; "cannot support causal inferences regarding the effects of tFUS on meditative development"; NADA-S p = .40 / trend .06 / decrease after session 2 p = .027, all verbatim in the Daily Surveys paragraph. "Effortlessness" and "Spaciousness" appear in "Table 2 Themes Identified Across All Retreat Participants, Independent of Stimulation Day", and the article does not credit them to tFUS. "reduced identification with and solidification of mental phenomena" is tied to stimulation days in the source ("... on stimulation days"). Third author "Erica N. Lord" confirmed from the OSF v2 PDF byline (Crossref: "Cook, Erica"). "Two stimulation sessions" and "ten-day silent retreat" confirmed.
- **(d) Lord 2026 bioRxiv**: HOLDS at abstract level (bioRxiv API, v1 2026-03-13). n = 24, active 16 / sham 8; "two-week 'Body Focus' mindfulness training program"; "greater reductions in DMN-CEN connectivity within the active group predicted larger increases in self-reported acceptance". "(Abstract.)" marked.
- **(e) Lyu 2023**: HOLDS. The aPCu hot zone is "located outside the boundaries of the default mode network (DMN) but connected reciprocally with it". The article files it under "the bodily self, outside the witness story".
- **(f) Foster & Parvizi 2017**: HOLDS in the body. Table cell repaired (Medium 4). The task's own phrasing, "885 PMC stimulations ... null", overreads the abstract in the same way the table did.
- **(g) Fox et al. 2020**: HOLDS. "low rates in the limbic (24%) and default networks (21%)". The false-negative caveat is followed in the source by "several factors mitigate the likelihood that it either explains or biases our findings", which the article renders as "though they judge this unlikely to explain their findings".

### Per-cite ledger (§2.4)

Metadata was checked against Crossref (all 19), Europe PMC core records (13) and the bioRxiv API (Lord 2026). Full texts were read as raw XML (Europe PMC / NCBI efetch) or PDF (OSF v2).

- Abellaneda-Pérez et al. 2024 (*Neurosci Biobehav Rev* 166:105862) — real-correct; abstract quote verbatim.
- Ciaunica et al. 2022 (*Conscious Cogn* 101:103320) — real-correct; abstract quote verbatim; physicalist stance noted in the article.
- Deane, Miller & Wilkinson 2020 (*Front Psychol* 11:539726) — real-correct; the 202-character quote is verbatim (full text); active-inference stance noted ("Both are physicalist models").
- Ehmann et al. 2025 (PsyArXiv, doi 10.31234/osf.io/uxrwy_v2) — real-correct (byline per v2 PDF); see guard (c).
- Foster & Parvizi 2017 (*Neurology* 88(7):685–691) — real-correct; abstract quotes verbatim; table overread repaired.
- Fox & Parvizi 2021 (*Brain Stim* 14(1):77–79) — real-correct; "an overall Type I error rate of 6.9%" and "did not observe any cases of outright confabulation or otherwise complex reports" verbatim (full text).
- Fox et al. 2020 (*Nat Hum Behav* 4(10):1039–1052) — real-correct; see guard (g).
- Garrison et al. 2013 (*Front Hum Neurosci* 7:440) — real-correct. Result direction: the abstract has PCC deactivation corresponding to "undistracted awareness" (including "concentration") and "effortless doing". The article's "deactivation tracks reported effortlessness" is faithful but partial, and is consistent with the effort-axis reading on [[meditation-and-consciousness-modes]].
- Herbet et al. 2014 (*Neuropsychologia* 56:239–244) — real-correct; "loss of external connectedness" verbatim. The source also says "a breakdown in conscious experience" and a dream-like report, consistent with the article's "abolishing awareness of the environment".
- Laukkonen, Friston & Chandaria 2025 (*Neurosci Biobehav Rev* 176:106296) — real-correct metadata. No quote; characterised "as the Map characterises it" (hedge kept).
- Lord, Allen, Young & Sanguinetti 2025 (*Biol Psychiatry CNNI* 10(4):384–392) — real-correct; equanimity definition verbatim.
- Lord et al. 2026 (bioRxiv 10.64898/2026.03.10.710890) — real-correct (bioRxiv authors "Schachtner, J. N." confirm the middle initial that Crossref omits).
- Lord et al. 2024 (*Front Hum Neurosci* 18:1392199) — real-correct; see guard (b).
- Lou et al. 2004 (*PNAS* 101(17):6827–6832) — real-correct; abstract quote verbatim (TMS at 160 ms, self vs other retrieval).
- Lyu et al. 2023 (*Neuron* 111(16):2502–2512.e4) — real-correct; see guard (e).
- Parvizi et al. 2021 (*PNAS* 118(29):e2100522118) — real-correct; see the quote table below.
- Parvizi et al. 2026 (Research Square 10.21203/rs.3.rs-10503199/v1) — real-correct; the abstract (via Crossref) supports "660 ... sites", "63 individuals", and posterior-insula connectivity as "a critical determinant".
- Pons et al. 2026 (*Sci Rep* 16:14673) — real-correct; preregistered, n = 60/61, CDS null, MEDT higher on MS/EDI/NJ/NR, "most participants in both groups described them as mixed" (full text).
- Vesuna et al. 2020 (*Nature* 586(7827):87–94) — real-correct metadata. **Content under-read by the research note**: the same-patient sham stimulations were missed (Critical 1).
- Two Map self-cites (Southgate & Oquatre-cinq; Southgate & Ocinq-cinq) follow the corpus pseudonym convention (91 uses in topics/concepts) and were left alone.

Inline ↔ References: all 19 external references are cited inline, and every inline author-year has an entry. No orphans in either direction. Every abstract-level work is marked "(Abstract.)".

Result-direction leg: no inverted comparatives found. Lord 2026's decoupling is the Condition × Session interaction, with sham trending toward *increased* coupling, and the article does not overstate it. Ehmann's after-session-2 effect is a *decrease*, and the article reports it as one.

Cited-author-stance leg: Deane et al. and Ciaunica et al. are active-inference physicalists, flagged in the text. Parvizi et al. frame S19_137 clinically (DSM-5 depersonalisation), not contemplatively, and the article says so. The Lord/Sanguinetti programme targets equanimity, not the witness, and the article says so. No cited author is presented as endorsing the interface reading.

### Quote fidelity (task lens 2)

All 44 quoted spans in the edited article body were string-matched (case- and quote-mark-normalised) against the fetched raw source. 43 match directly. The 44th, the witness-consciousness falsifier sentence, matches the rendered page: the raw file now pipes `[[brain-stimulation-and-the-witness-mode|neurostimulation]]` inside it, which breaks a naive substring test. A negative control (`"I stopped considering them 'you'"`, `"pilot's seat"`) returned 0 against Parvizi 2021.

Seizure vs stimulation attribution for every S19_137 quote:

| Quote | Source context | Article attribution |
|---|---|---|
| "an observer of an active, internalized experience over which I have little control" | seizures ("according to his own description of the events") | seizures ✓ |
| "I stopped considering them 'me'" | seizures (self-dissociation account) | seizures ✓ (body). It had also been carried into the table's stimulation column; fixed |
| "induced a subjectively similar state, reproducibly" | 50-Hz stimulation, seizure zone + contralateral PMC | stimulation ✓ |
| "I got pulled out of the chair, the pilot's chair, but I could still see all the gauges" | left-PMC stimulation | stimulation ✓ |
| "a nice version of the seizure, cleaner" | stimulation compared with seizure | stimulation ✓ |
| "if I wanted to take control, I could have" | "during the stimulation"; "not the case during the climax of one of his seizures" | stimulation ✓; paraphrases elsewhere repaired (Medium 5) |
| "did not reproduce any signs of auras" | stimulation of temporal lobes, insula, MFC | stimulation ✓ |
| "without the negative valence of an impending seizure" (Vesuna) | left-PMC stimulation | stimulation ✓ |
| "being an outside observer with respect to one's thoughts" | DSM-5 definition quoted in Parvizi's Discussion of the *seizure* semiology | DSM-5, "as Parvizi et al. quote it" ✓ |
| "the same dissociation" (new) | left-PMC stimulation: "That was the same dissociation [as my seizures]" | stimulation ✓ |
| "evoked a dissociative aura 11 out of 13 times"; "only one sham stimulation elicited report of an aura" (new) | Vesuna, same patient | stimulation / sham ✓ |

### Research-note errors (recorded, note not edited)

The note [[brain-stimulation-and-the-witness-mode-2026-10-03]] has three defects. The follow-up task names them, but correcting them is optional:
1. Executive Summary item 1 puts the seizure quote into the stimulation report: "He said he 'stopped considering them 'me'' of his own thought-streams, and he reported that during stimulation...". Its S19_137 table repeats this, citing "I stopped considering them 'me'" as stimulation-time evidence for witness structure. The expand fork had already caught this.
2. "No reported sham trial for him", in the Executive Summary, the S19_137 table ("Sham control for this patient: None reported") and Gaps in Research, is false given Vesuna et al. 2020 (which the note itself marks [F]).
3. "885 PMC stimulations ... null" (Key Sources, Foster & Parvizi) overreads the abstract (see Medium 4).

### Counterarguments Considered

- **Eliminative materialist / physicalist**: "Witness" is just a label for PCC-DMN reconfiguration, and S19_137 shows it can be induced. The article answers in-framework: the structural measure (CDS) does not separate witness from depersonalisation (Pons), so "induced the witness" has not been shown. Separately, it says honestly that a full neural account would not touch the Dualism tenet.
- **Quantum skeptic**: no quantum claim is made. The MQI section says "Not engaged ... macroscopic scale". Clean.
- **Many-worlds defender**: not engaged; correctly marked.
- **Empiricist (Popper)**: the falsifier is unfalsifiable for the interface reading. The article concedes this as a cost ("a reading that accommodates both outcomes gains nothing when either arrives") and notes the falsifier tests the wrong joint. This is the strongest passage and was left intact.
- **Buddhist (Nagarjuna)**: the witness itself may be a reified construct. The constructivist worry is acknowledged at L95. Bedrock; not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The clause-by-clause table against the falsifier is the article's best device. With the sham row corrected, it now shows a case that is sham-checked for the aura but not for the attitude.
- The honest cost statement in §What Each Reading Predicts: the interface reading "permits" an induced witness and "neither forbids its absence".
- §A Design That Would Sharpen the Question, with its explicit admission that the design "would not separate the three readings".
- The witness/depersonalisation boundary built from three independent sources (DSM-5 via Parvizi, Pons 2026, Deane 2020), with "the Map borrows their criterion, not their metaphysics".
- Relation to Site Perspective declines to claim support: "No bearing", "Not engaged", "recorded without inference". The Hardline Empiricist persona would single this out.

### Enhancements Made

None beyond the corrections. The article is at the soft threshold by total count, and every edit was a fidelity or calibration repair.

### Cross-links Added

None. The outbound set is already complete, and every anchor resolves (predictive-processing-and-dualism "The Beautiful-Loop Theory: The Strongest Contemporary Rival", sham-controlled-neurofeedback `{#separating-design}`, and five tenet block refs).

### Reasoning-mode notes (editor-internal)

- Production reading: framework-boundary marking plus data status. It is not refuted, and the article says the connectivity half has one preprint.
- Active inference / beautiful loop: boundary marking with an honest concession ("fits the data at least as well").
- Deane / Ciaunica: criterion borrowed, metaphysics marked as physicalist. No boundary substitution. No label leakage (grep for the forbidden labels returned 0).

## Calibration audit (task lens 3)

- Interface reading = speculative integration: now explicit (L105).
- tFUS = live hypothesis: L54, "That tFUS alters DMN connectivity is a live hypothesis resting on one sham-separable preprint. That it raises mindfulness, equanimity or nondual awareness beyond sham has not been shown."
- S19_137 = one documented case: L64, plus the table and status.
- Creation or abolition independent of training = NOT SHOWN: L105.
- Both costs stated: L93–95 and the lead.
- Witness vs depersonalisation boundary with the falsifier's profile: L81–85.
- Tenet 3 quantifier: not settled (L77, L113). The two paraphrases that framed availability as actual control are repaired, and the "could have" line argues neither reading.
- No Minimal Quantum Interaction claim: L111.
- Consistent with "selects little, not nothing" (L93 quotes it from witness-consciousness L168) and with meditation-modes' effort axis (Further Reading, "the PCC as an effort axis").

## Style audit (task lens 4)

No "This is not X. It is Y." / "X is not Y. It is Z." constructs (scripted two-sentence scan: 0). "load-bearing": 0. The lead is LLM-first: verdict, the falsifier, the one case and its limits, the ultrasound null, the discrimination failure. A named-anchor forward reference is present.

## Remaining Items

- [[the-observer-witness-in-meditation]] L157 still says "a single untrained epilepsy patient, with no sham trial for him". The same two defects are fixed here. Minted as a P2 refine-draft (outside this review's edit scope).
- Research-note defects 1–3 above (optional fix, folded into the same task).
- Foster & Parvizi 2017: the PMC-site share of the 885 stimulations is unknown until someone reads the full text.

## Stability Notes

- Physicalist and active-inference personas will say the witness is a neural configuration and that S19_137 shows it. This is bedrock at the Dualism boundary, and the article's "No bearing" treatment is correct. Do not re-flag.
- The interface reading's ability to absorb both outcomes is already stated as a cost. Future reviews should not "fix" it by claiming test power, and should not delete the concession.
- S19_137 now has a sham record for the dissociative aura. Do not regress to "no sham", and do not upgrade the case to sham-controlled for the witness profile: the attitude measures were never taken.
- The Tenet 3 actual-vs-capacity question is with the operator (NEEDS-HUMAN 2026-08-17). Keep the "recorded without inference" wording until it is decided.
