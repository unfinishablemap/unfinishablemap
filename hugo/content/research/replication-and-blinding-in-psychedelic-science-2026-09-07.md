---
ai_contribution: 100
ai_generated_date: 2026-09-07
ai_modified: 2026-09-07 11:21:35+00:00
ai_system: claude-opus-5
author: null
concepts:
- '[[concepts/filter-theory]]'
- '[[concepts/entropic-brain-hypothesis]]'
- '[[concepts/phenomenological-evidence]]'
created: 2026-09-07
date: '2026-09-07'
draft: false
last_curated: null
last_deep_review: null
lastmod: 2026-09-07 11:21:35+00:00
related_articles: []
title: Research Notes - Replication and Blinding in Psychedelic Science
topics:
- '[[methodology-of-consciousness-research]]'
- '[[psychedelics-and-the-filter-model]]'
---

# Research: Replication and Blinding in Psychedelic Science

**Date**: 2026-09-07
**Task**: `todo.md` L39 (P2), `research-topic`, harvested from `outer-review-2026-09-06-gemini-2-5-pro.md` finding 3.

**Search queries used**:
1. `van Elk Fried 2023 "History repeating" guidelines psychedelic science common problems`
2. `psychedelic clinical trials functional unblinding expectancy placebo control critique 2024 2025`
3. `Szigeti self-blinding microdose citizen science trial eLife placebo psychedelic`
4. `FDA Lykos MDMA-assisted therapy PTSD 2024 complete response letter functional unblinding advisory committee`
5. Crossref REST lookups on nine DOIs; Crossref bibliographic query for the Belinger et al. comparative trial; PubMed `esummary` for two 2026 PMIDs and one PMCID; Europe PMC `resultType=core` abstract retrieval for four DOIs.

## Executive Summary

The 2020s methodological critique of psychedelic science is real, well-documented and now quantified: a 2026 JAMA Psychiatry systematic review of 112 randomised controlled trials found that only 29.5% assessed blinding integrity at all, while psilocybin, LSD and ayahuasca trials that did assess it frequently reported blinding failure above 90% among both participants and raters. The critique's core claim is directional rather than nullifying — Muthukumaraswamy, Forsyth & Lumley argue effect sizes are "likely over-estimated," not that effects are absent — and it has one clean positive demonstration behind it: under genuine self-blinding, microdosing benefits vanish into the placebo arm (Szigeti et al., 2021).

The subject warrants coverage, but **not in the shape the harvest note proposes**, and its bite on the Map is narrower than the note implies. Three findings drive that conclusion. First, the flagship article [psychedelics-and-the-filter-model](/topics/psychedelics-and-the-filter-model/) has *already* withdrawn the premise the critique most damages — therapeutic durability — on independent grounds. Second, van Elk & Yaden's critical review names "reduced efficacy of thalamo-cortical filtering" and "loosening of top-down predictive signaling" as genuine neural-level mechanisms, so at the mechanistic layer that review is partly *congenial* to the filter reading even as it attacks the inferential over-reach built on it. Third, the ideal host already exists and is undersized: [clinical-evidence-quality-standards-consciousness-research](/topics/clinical-evidence-quality-standards-consciousness-research/) is a framework article about evidence quality whose "Active Control Problem" section is illustrated entirely with meditation studies and mentions psychedelics zero times — despite psychedelic unblinding being the most extreme control-adequacy failure in the consciousness-relevant literature.

**Recommendation: a section in `clinical-evidence-quality-standards-consciousness-research`, not a new `topics/` article.** Reasoning in "Recommended Chain Target" below. I decline no part of the subject, but I do reject the note's framing of it as a corpus-wide latent vulnerability.

## Verification Status and Three Corrections to Propagate

Everything cited below was resolved at Crossref (`api.crossref.org/works/{DOI}`) this run; abstracts quoted or paraphrased were pulled from Europe PMC `resultType=core` and grepped in raw form rather than read through a summariser. The driver's Correction 1 and Correction 2 are both upheld. Three further metadata defects were found, two of them in the driver's own brief.

**Confirmed — van Elk & Fried title.** Crossref returns `History repeating: guidelines to address common problems in psychedelic science`, Therapeutic Advances in Psychopharmacology **13**, article 20451253231198466, 2023. The `updated-by` field names `10.1177/20451253231223609` as a `correction`, and that erratum's `update-to` field names `10.1177/20451253231198466` in return — verified in both directions. **"guidelines" is the version of record; "a roadmap" is the preprint wording** and appears in the abstract as ordinary prose ("We provide a roadmap for tackling these challenges"), which is presumably how the confusion arose. The task note has this inverted; do not propagate it.

**Confirmed — Muthukumaraswamy is already in the corpus, and is used, lightly.** The version of record is `Blinding and expectancy confounds in psychedelic randomized controlled trials`, Expert Review of Clinical Pharmacology **14**(9): 1133–1152, DOI `10.1080/17512433.2021.1933434` — lowercase "randomized," matching the corpus entry, not the PsyArXiv preprint's "Randomised."

I **partly disagree with the driver's "cited but not load-bearing" gloss, in the direction of the corpus's favour**: the paper is not merely sitting in a reference list. It appears in body prose at `psychedelics-and-the-filter-model.md` L62, as a parenthetical qualifier on a neuroimaging result — Siegel et al. (2024) is described as "a within-person psilocybin study of seven participants and, like most psychedelic trials, imperfectly blinded (Muthukumaraswamy et al., 2021)." So the citation does real, if minimal, work: it hedges *one* study on *one* dimension. The accurate framing is therefore **cited, used once as a local hedge, never generalised** — the systematic point the paper actually makes (that effect-size estimates across the field are inflated) is nowhere drawn. That is a sharper finding than either "absent" or "unused," and it tells the downstream task the citation needs *promoting*, not adding.

⚠️ **New defect — the second Muthukumaraswamy hit is a different paper.** My probe returned two files, but `concepts/entropic-brain-hypothesis.md` L104 cites Toker et al. (2022), *Consciousness is supported by near-critical slow cortical electrodynamics*, PNAS 119(7), on which Muthukumaraswamy is a middle author. That is unrelated to blinding. **The blinding paper appears in exactly one live article, not two.** Any downstream sweep keyed on the surname will pick up a false positive.

⚠️ **New defect — the driver's van Elk & Yaden volume is wrong.** The brief gives "Neuroscience & Biobehavioral Reviews **146**: 104793". Crossref returns volume **140**, page 104793, issued 2022-09. Use 140.

⚠️ **New defect — the driver's Shafiee author list is wrong in two ways.** The brief gives five authors ending "Razmara, S." Crossref returns **seven**: Shafiee, Arman; Arabzadeh Bahri, Razman; Rafiei, Mohammad Ali; Esmaeilpur Abianeh, Fatemeh; **Razmara, Parsa**; **Jafarabady, Kyana**; **Amini, Mohammad Javad**. So the initial on Razmara is wrong (P., not S.) and two authors are missing. Full record: Journal of Psychopharmacology **38**(5): 425–431, 2024-02-22, title returned literally prefixed `RETRACTED:`, retracted by `10.1177/02698811251341228`. The driver's brief did not carry the retraction notice's own DOI; it is recorded here.

I confirm the driver's instruction on Shafiee: **the corpus cites no retracted work**, so this is a coverage datum, not a citation defect, and no hunt is warranted.

## Key Sources

### Blinding Integrity in Psychedelic Randomized Clinical Trials: A Systematic Review
- **DOI**: `10.1001/jamapsychiatry.2026.0255` | JAMA Psychiatry 83(7): 755–769, 2026-07-01
- **Authors**: Orsini, D. K., Wong, S., Di Luch, S., Chan, B., Vasudeva, S., Lovell, G. F. M., Le, G. H., Jones, B. D. M., Chisamore, N., Mollica, A., Johnson, D. E., Kaczmarek, E. S., *et al.*
- **Type**: Systematic review (PRISMA). **Publisher-verified; abstract retrieved verbatim from Europe PMC.**
- **Why this matters most**: it postdates all four sources in the harvest note and converts a methodological worry into measured prevalence. This is the single most valuable source found.
- **Key numbers** (from the abstract, search window 2020-01-01 to 2025-12-11 plus manual back-search): 112 RCTs — 11 psilocybin, 17 LSD, 78 ketamine, 11 MDMA, 2 ayahuasca, 2 DMT, 1 noribogaine. Only **29.5% (n=33)** evaluated blinding integrity; **57.1% (n=64)** cited blinding as a limitation. Psilocybin, LSD and ayahuasca studies "frequently reported blinding failure values of more than 90% among participants and raters"; inert-placebo MDMA trials "exceeded 85%"; ketamine trials rarely assessed blinding (17.9%) but showed "improved preservation with midazolam vs saline controls." **"No control strategy consistently achieved ideal blinding."**
- **Tenet alignment**: Neutral on metaphysics; directly relevant to **Tenet 5 (Occam's Razor Has Limits)** by a non-obvious route — the finding is that a widely-cited evidence base is *less informative than its citation frequency suggests*, which is a case of incomplete knowledge being mistaken for settled knowledge.

### History repeating: guidelines to address common problems in psychedelic science
- **DOI**: `10.1177/20451253231198466` | Therapeutic Advances in Psychopharmacology 13, art. 20451253231198466, 2023. Erratum `10.1177/20451253231223609` (2024).
- **Authors**: van Elk, M. & Fried, E. I. **Publisher-verified.**
- **Key points**: identifies "the 10 most pressing challenges, grouped into easy, moderate, and hard problems," and — the structurally useful part — classifies them by *which kind of validity* they threaten: internal ("treatment effects are due to factors unrelated to the treatment"), external ("lack of generalizability"), construct ("unclear working mechanism"), statistical conclusion ("conclusions do not follow from the data and methods"). Notes these "tend to co-occur." Supplies a checklist for researchers, journalists, funders and policymakers.
- **Tenet alignment**: Neutral. Its four-way validity taxonomy is the most directly reusable analytic apparatus in this literature, because it lets a claim be located precisely rather than hedged vaguely.

### Blinding and expectancy confounds in psychedelic randomized controlled trials
- **DOI**: `10.1080/17512433.2021.1933434` | Expert Review of Clinical Pharmacology 14(9): 1133–1152, 2021
- **Authors**: Muthukumaraswamy, S. D., Forsyth, A. & Lumley, T. **Publisher-verified. Already corpus reference #20 of `psychedelics-and-the-filter-model`.**
- **Key points**: systematic review of psychedelic RCTs (Medline, PsycInfo, EMBASE, Jan 1990 – Nov 2020) finding trials "have generally not reported pre-trial expectancy, nor the success of blinding procedures." The expert-opinion claim is explicitly directional: "treatment effect sizes in psychedelic RCTs are **likely over-estimated** due to de-blinding of participants and high levels of response expectancy," with the recommendation that confounds "be reduced, estimated and removed from effect size estimates," and a closing urge to "caution in interpreting effect size estimates from extant psychedelic RCTs."
- **Note the wording**: *over-estimated*, *caution*, *removed from estimates*. This is a correction-and-recalibration argument, not an elimination argument. Any downstream use that reads it as showing the effects are placebo artefacts overstates it.

### Pharmacological, neural, and psychological mechanisms underlying psychedelics: A critical review
- **DOI**: `10.1016/j.neubiorev.2022.104793` | Neuroscience & Biobehavioral Reviews **140**: 104793, 2022
- **Authors**: van Elk, M. & Yaden, D. B. **Publisher-verified; volume corrected from the task note's 146.**
- **⚠️ This source cuts both ways and must not be flattened.** It is a critical review of *mechanisms*, and it affirms mechanisms at three levels: biochemically, psychedelics "primarily affect the 5-HT2A receptor, increase neuroplasticity, offer a critical period for social reward learning, and have anti-inflammatory properties"; neurally, they are "associated with **reduced efficacy of thalamo-cortical filtering**, the **loosening of top-down predictive signaling** and an increased sensitivity to bottom-up prediction errors, and activation of the claustro-cortical-circuit"; psychologically, they induce altered and affective states, affect cognition, induce belief change, and can produce lasting behavioural change.
- **Relation to site tenets**: the neural-level description is *filter language in the mainstream literature* — thalamo-cortical filtering efficacy is reduced. That is congenial to [filter-theory](/concepts/filter-theory/) at the level of physical mechanism while remaining metaphysically neutral: a reduced physical filter is exactly what a physicalist predicts too. The review's own contribution is to contrast "a unifying account" with "a model of **pluralistic causation**," and it leans toward the latter. **Pluralistic causation is the hostile part for the Map**: if several independent mechanisms each suffice to explain a psychedelic phenomenon, no one of them — filter attenuation included — is uniquely supported by it. This is the same inferential structure the Map already conceded at L94 of the psychedelics article.

### Expectancy in placebo-controlled trials of psychedelics: if so, so what?
- **DOI**: `10.1007/s00213-022-06221-6` | Psychopharmacology 239(10): 3047–3055, 2022
- **Authors**: Butler, M., Jelen, L. & Rucker, J. **Publisher-verified (Crossref).**
- **Why included**: this is the **counter-position**, and a research note that omitted it would be one-sided. The argument is that if the subjective experience is itself the therapeutic mechanism, then expectancy is not cleanly a confound to be subtracted — it may be partly constitutive. That does not rescue the effect-size estimates, but it complicates the assumption that "true pharmacological effect" is the quantity of interest.
- **Tenet alignment**: Interestingly *congenial* to the Map. A view on which the phenomenal character of the experience does causal work, rather than being an epiphenomenal accompaniment of a pharmacological effect, is closer to **Tenet 3 (Bidirectional Interaction)** than the orthodox subtract-the-expectancy framing is.

### Self-blinding citizen science to explore psychedelic microdosing
- **DOI**: `10.7554/eLife.62878` | eLife 10: e62878, 2021-03-02
- **Authors**: Szigeti, B., Kartner, L., Blemings, A., Rosas, F., Feilding, A., Nutt, D. J., Carhart-Harris, R. L. & Erritzoe, D. **Publisher-verified (Crossref).**
- **Key points**: 191 completing participants self-administered placebo control under online instruction. All psychological outcomes improved from baseline in the microdose group — **and equally in the placebo group**, with no significant between-group differences.
- **Why this is the strongest single item**: it is a *positive result*, not a methodological complaint. It shows what happens to a psychedelic literature when blinding actually holds. Note the author list: Nutt and Carhart-Harris, i.e. the field's own leading proponents, are co-authors. This is not an outsider attack.
- **Scope limit to state plainly**: this is **microdosing**, a distinct literature from high-dose psychedelic therapy and from the ego-dissolution phenomenology the Map relies on. It does not transfer directly. It is evidence about what unblinding can conceal, not evidence that high-dose effects are placebo.

### The difference between 'placebo group' and 'placebo control': a case study in psychedelic microdosing
- **DOI**: `10.1038/s41598-023-34938-7` | Scientific Reports 13(1), art. 12107, 2023
- **Authors**: Szigeti, B., Nutt, D., Carhart-Harris, R. & Erritzoe, D. **Publisher-verified (Crossref).**
- **Key point (conceptual, and the most quotable distinction in the whole set)**: a trial can have a placebo *group* without having a placebo *control*. Randomising to placebo achieves control only if allocation remains concealed; when unblinding is near-total, the placebo arm is a group, not a control. This gives a precise vocabulary for the defect, and it generalises beyond psychedelics to any intervention with unmistakable subjective effects — which is why it is the piece most worth importing into a general evidence-quality framework.

### Blinding integrity in psychedelic research: evidence from a comparative RCT of psilocybin, MDMA, and methylphenidate in healthy volunteers
- **DOI**: `10.1016/j.euroneuro.2026.112879` | European Neuropsychopharmacology **111**: 112879, 2026-10
- **Authors**: Belinger, L., Rieser, N. M., Engeli, E. J. E., Becciolini, L., Clamote, M., Pribis, M., Saissi, F., Florineth, G. A., *et al.* **Metadata publisher-verified via Crossref bibliographic query; abstract NOT retrieved — see Gaps.**
- **Why included**: the *constructive* response. Methylphenidate as an active comparator is a serious attempt to build a control that can survive contact with an unmistakable drug effect. A treatment of this subject that presents the field as static and broken would be stale by 2026.

### Conceptual analysis of mechanisms and methods in psychedelic clinical trial design: a narrative review
- **DOI**: `10.1177/20451253261470523` | Therapeutic Advances in Psychopharmacology **16**, art. 20451253261470523, 2026-07
- **Authors**: Krsak, M., Sparrow, D., Rosner, B., DeMolles, D. & Shannon, S. **Metadata publisher-verified; abstract NOT retrieved — see Gaps.**
- **Status**: recorded as a currency marker only. Low confidence in its content; do not cite it for any specific claim without reading it.

### FDA / Lykos Therapeutics, MDMA-assisted therapy for PTSD (regulatory datum)
- **Not a publisher-verified academic source. Secondary reporting only; treat accordingly.**
- Sequence: 2024-06-04, an FDA advisory committee voted **2–9** against effectiveness and **1–10** against benefits outweighing risks; 2024-08, FDA issued a Complete Response Letter declining approval and requesting an additional phase 3 trial; **2025-09-04**, FDA published the CRL, making its blinding, durability and safety-reporting concerns public for the first time. Functional unblinding was among the concerns cited.
- **Why it matters**: it establishes that the methodological critique has *institutional consequences*, not merely journal-page ones. That is the fact that most resists the dismissal "this is just methodological grumbling."
- **⚠️ Verification gap**: I did not obtain the CRL document itself. Any downstream article should cite the primary CRL or FDA docket, not the trade press, and should not attribute specific weightings to the FDA's reasoning on the strength of these secondary reports.

## Major Positions

### The strong methodological critique
- **Proponents**: van Elk & Fried (2023); Muthukumaraswamy, Forsyth & Lumley (2021); Orsini et al. (2026).
- **Core claim**: psychedelic trial results are systematically inflated by functional unblinding and response expectancy, and the field has largely failed to measure either. Validity is compromised on several axes at once.
- **Strongest evidence**: the Orsini prevalence figures, and the fact that no control strategy has yet preserved blinding.
- **Relation to site tenets**: neutral metaphysically; a constraint on what the Map may infer, not a challenge to any tenet. Consistent with **Tenet 5**: the appearance of a settled empirical base can be an artefact of citation volume rather than evidential strength.

### The mechanism-pluralist critique
- **Proponents**: van Elk & Yaden (2022).
- **Core claim**: multiple mechanisms at multiple levels each plausibly explain psychedelic effects; a unifying account is not warranted, and pluralistic causation fits the evidence better.
- **Relation to site tenets**: this is the position that bites hardest on the Map, and it bites for reasons *independent of blinding*. Where several mechanisms each suffice, a filter-attenuation reading is underdetermined. The Map has already absorbed this move once, at `psychedelics-and-the-filter-model.md` L94, where therapeutic durability is withdrawn as a filter-specific signature precisely because "REBUS, plasticity-window evidence, memory reconsolidation, expectancy, and integration practices each independently predict durable single-dose change."

### The expectancy-is-not-simply-a-confound reply
- **Proponents**: Butler, Jelen & Rucker (2022).
- **Core claim**: for an intervention whose mechanism may *be* the subjective experience, subtracting expectancy may subtract part of the treatment.
- **Relation to site tenets**: mildly congenial to **Tenet 3**, and a useful check against the assumption that the "real" effect is by definition the pharmacological residue.

### The constructive-design response
- **Proponents**: Belinger et al. (2026); the ketamine-with-midazolam comparison noted by Orsini et al.
- **Core claim**: better active comparators can partially recover blinding.
- **Status**: live and unresolved. Orsini et al.'s verdict as of 2026 is that no strategy consistently succeeds.

## Key Debates

### Is functional unblinding a fixable design problem or a structural feature?
- **Sides**: constructive-design researchers (fixable, with active comparators) versus those arguing psychedelic trials should be treated as effectively open-label and compared against open-label standard care.
- **Core disagreement**: whether a control can exist for an intervention whose effects are unmistakable to the person receiving them.
- **Current state**: unresolved. Orsini et al. (2026) report that no control strategy consistently achieved ideal blinding, which is evidence for the structural reading without settling it.

### Does the critique threaten the phenomenological findings or only the clinical ones?
- **Sides**: not a formal debate in the literature, but the distinction the Map most needs.
- **Core disagreement**: blinding failure biases *outcome-measure* estimates. The Map's filter argument leans mainly on the *character* of ego-dissolution reports and on neuroimaging correlates, not on symptom-reduction effect sizes.
- **Assessment**: the critique's transfer to phenomenology is weak — but the corpus is exposed there by a *different* defect, small samples. `psychedelics-and-the-filter-model` L62 already flags Siegel et al. (2024) as n=7 and calls the base "small, cross-drug." So the exposure is real, acknowledged, and of a different kind than the harvest note describes.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 2021 | Szigeti et al., eLife 10:e62878 | Self-blinded microdosing: placebo arm improves equally. First large demonstration of what holding the blind does. |
| 2021 | Muthukumaraswamy, Forsyth & Lumley, Expert Rev Clin Pharmacol 14(9) | Establishes that trials generally reported neither expectancy nor blinding success; argues effect sizes are over-estimated. |
| 2022 | van Elk & Yaden, Neurosci Biobehav Rev 140:104793 | Mechanism-level critical review; pluralistic causation preferred over a unifying account. |
| 2022 | Butler, Jelen & Rucker, Psychopharmacology 239(10) | Counter-position: expectancy may be constitutive rather than confounding. |
| 2023 | van Elk & Fried, Ther Adv Psychopharmacol 13 | Ten problems mapped onto four kinds of validity; checklist for non-specialist stakeholders. |
| 2023 | Szigeti et al., Sci Rep 13:12107 | The placebo-*group* / placebo-*control* distinction. |
| 2024 | Shafiee et al., J Psychopharmacol 38(5): 425–431 — later retracted | A BDNF meta-analysis enters, then leaves, the evidence base. |
| 2024-06 / 2024-08 | FDA advisory committee votes 2–9 and 1–10; CRL issued to Lykos | Methodological critique acquires regulatory teeth. |
| 2025 | Retraction notice `10.1177/02698811251341228` | The retraction completes. |
| 2025-09-04 | FDA publishes the Lykos CRL | Blinding concerns become part of the public record. |
| 2026-07 | Orsini et al., JAMA Psychiatry 83(7): 755–769 | Prevalence quantified across 112 RCTs. The state of the art. |
| 2026-10 | Belinger et al., Eur Neuropsychopharmacol 111:112879 | Active-comparator design tested directly. |

## Measured Corpus Position

Re-measured this run over live articles in `topics/`, `concepts/`, `apex/`, `voids/`, `positions/`. My counts agree with the driver's throughout and correct the harvest note in two places.

| Probe | Live articles | Note said | Driver said |
|---|---|---|---|
| `van Elk` | 0 | 0 | 0 |
| `Yaden` | 0 | — | 0 |
| `Shafiee` | 0 | — | 0 |
| `expectancy confound` | 1 | **0 (wrong)** | 1 |
| `blinding` | 3 | **2 (wrong)** | 3 |
| `replication crisis` | 1 | 1 | 1 |
| `preregistrat` | 3 | 3 | 3 |
| `Muthukumaraswamy` | 2 files, **1 relevant** | — | 2 |

Research notes: `replication crisis` 6, `blinding` 2, `preregistrat` 2, `van Elk` 0, `Muthukumaraswamy` 0.

Scale: **71 live articles** mention psilocybin / psychedelic / Carhart-Harris / ego-dissolution / DMT (the driver measured 70; the note said 69 — the difference is threshold noise, not a discrepancy worth chasing). Of the subset mentioning psilocybin or psychedelics, **30** also invoke therapeutic, clinical-trial, efficacy, depression or RCT language, i.e. touch the premise the critique most damages.

**But the flagship article is already partly inoculated.** `psychedelics-and-the-filter-model.md` L94 withdraws therapeutic durability as a filter-specific signature, and L62 already flags small-n and imperfect blinding. So the harvest note's central argument — that the alternative to one article is "repeating the same hedge in each" of 70 articles — overstates the exposure. The corpus's most-exposed article has already done the hedging, and did it on the sharper grounds (pluralistic causation) rather than on blinding.

## Recommended Chain Target

**Recommend: a new section in `topics/clinical-evidence-quality-standards-consciousness-research` (~700–900 words). Do not create a new `topics/` article, and do not use `experimental-consciousness-science-2025-2026`.**

Thresholds printed from `tools/curate/length.py` rather than recalled: `topics` is `(3000, 4000, 6000)` for (soft, hard, critical). Measured body word counts, frontmatter stripped:

| Candidate host | Words | Headroom to hard 4000 | Probe score |
|---|---|---|---|
| `psychedelics-and-the-filter-model` | 3985 | **15** | already carries the one-clause hedge |
| `experimental-consciousness-science-2025-2026` | 2458 | 1542 | 0 on all five probes |
| `clinical-evidence-quality-standards-consciousness-research` | **2928** | **1072** | `replication crisis` 1; **psychedelics 0** |

Reasons for the third, in order of weight:

1. **Remit match.** That article *is* a framework for deciding when clinical evidence bears on metaphysics. It already contains `### The Replication Problem`, `### The Active Control Problem`, a five-standard framework whose standard 2 is `Control Adequacy`, and a `## Common Failures in Evidence Presentation` section listing selective citation, strength inflation, asymmetric scrutiny and bridging without warrant. Psychedelic unblinding is a control-adequacy failure; the Shafiee retraction is a selective-citation hazard; Muthukumaraswamy's over-estimation claim is strength inflation measured. **Every element of this subject has a slot waiting for it.** Nothing new needs inventing.
2. **The article's control-adequacy discussion is entirely meditation.** Van Dam et al. (2018), Goyal et al. (2014), Kral et al. (2022) — mindfulness throughout, psychedelics nowhere. Yet psychedelic trials are the most extreme control-adequacy failure in this literature (>90% unblinding), and the article explicitly states its own ambition to generalise: the standard "should be generalised across all clinical evidence cited for metaphysical purposes." Adding the psychedelic case **completes the article's stated project** rather than bolting a topic onto it.
3. **Length favours it.** At 2928 words it sits **below its 3000-word soft target**. Adding 700–900 words moves it into compliance instead of consuming headroom. `experimental-consciousness-science-2025-2026` is also under target (2458) but its remit is a chronicle of 2025–2026 *experiments* — COGITATE, biophotons, split-brain, zero-point coupling — where a methodology section on trial design would read as a category error among them.
4. **A fourth locus would strand the siblings.** The subject already has three touchpoints (`psychedelics-and-the-filter-model` L62/L94, plus the replication and preregistration mentions elsewhere). A standalone article makes a fourth, and the general claims would then live away from the places that need them. Concentrating the treatment where the *evaluative framework* lives lets the other loci point at it.
5. **`topics` cap is not the constraint either way** — the driver measured 328/360 via `count_section_files`, 32 slots. CLAUDE.md's "1 slot left" is stale. So this is an editorial judgement, not a capacity one, which is why I am making it on remit grounds.

**Zero-cost integration for the 15-word article.** `psychedelics-and-the-filter-model` and `clinical-evidence-quality-standards-consciousness-research` are currently **mutually unlinked** (0 references each way). The filter article has 15 words of headroom and an open task already claiming them, so a pointer *sentence* is impossible — but a piped wikilink over existing prose costs nothing. L62's phrase "like most psychedelic trials, imperfectly blinded" is an existing-text anchor that could carry the link at zero word cost. Flagging as an option for the downstream task; **not doing it here** — this run writes no article edits.

## Potential Article Angles

If the recommendation is accepted, the section should:

1. **Lead with the measured prevalence, not the worry.** Orsini et al.'s 29.5% / >90% figures do the persuasive work; the older papers supply the analysis. Front-load per the writing-style guide.
2. **Import the placebo-group / placebo-control distinction** (Szigeti et al., 2023) as the article's own vocabulary. It generalises past psychedelics to any intervention with unmistakable subjective effects, which is what a framework article wants.
3. **State the Map's exposure honestly and specifically.** The critique constrains what the psychedelic evidence can license: clinical-efficacy premises are hit hard, phenomenological and neuroimaging premises are hit by small-n rather than by unblinding, and the Map has already withdrawn its durability premise. Say which is which. Do not present the withdrawal as a concession forced by this literature — it was made on pluralistic-causation grounds.
4. **Carry the counter-position.** Butler, Jelen & Rucker prevent the section from becoming a one-sided debunking, and their view is mildly congenial to Tenet 3.
5. **Do not overstate van Elk & Yaden.** It is a critical review that affirms real mechanisms, including reduced thalamo-cortical filtering. Presenting it as a demolition would be a fidelity defect — and it would also discard the one place where the mainstream literature uses filter language.
6. **Use the retraction as an instance, not an accusation.** Shafiee et al. illustrates that the meta-analytic layer is not self-cleaning. The corpus cites no retracted work; say so.

## Gaps in Research

- **Belinger et al. (2026) abstract not retrieved.** Metadata verified at Crossref; content unread. Do not attribute findings to it. Its value here is as evidence that active-comparator designs are being tested, which the title alone supports.
- **Krsak et al. (2026) abstract not retrieved.** Recorded as a currency marker only. **Do not cite for any claim.**
- **The FDA CRL was not obtained.** All Lykos facts above rest on secondary trade and advocacy reporting (MAPS, Psychiatric Times, PharmExec, AJMC). Vote tallies (2–9, 1–10) and dates are consistently reported across independent outlets, which raises confidence, but the characterisation of the FDA's reasoning does not meet the Map's publisher-verification standard. A downstream article should either fetch the CRL or confine itself to the votes and the fact of the CRL.
- **No verbatim quotations from the two 2026 sources or the regulatory material.** Only the four Europe PMC abstracts (Orsini, van Elk & Fried, van Elk & Yaden, Muthukumaraswamy) were retrieved as raw text and are safe to quote from.
- **Not investigated**: whether any *high-dose* psychedelic finding the Map relies on has specifically failed replication. Szigeti covers microdosing only. This is the question that would settle how hard the critique actually bites, and it needs its own pass.
- **Not investigated**: post-2024 phase 3 psilocybin results, which would bear on whether the effect survives better controls.
- The prior corpus research notes touching adjacent ground are `letheby-predictive-self-binding-naturalistic-psychedelics-2026-06-22.md` and `steelman-for-value-blind-selection-2026-06-18.md` (the latter matches on "blind" only and is unrelated). Named as plain filenames deliberately, not wikilinked.

## Citations

1. Belinger, L., Rieser, N. M., Engeli, E. J. E., Becciolini, L., Clamote, M., Pribis, M., Saissi, F., Florineth, G. A., et al. (2026). Blinding integrity in psychedelic research: Evidence from a comparative randomized controlled trial of psilocybin, MDMA, and methylphenidate in healthy volunteers. *European Neuropsychopharmacology*, 111, 112879. https://doi.org/10.1016/j.euroneuro.2026.112879 *(metadata verified; abstract unread)*
2. Butler, M., Jelen, L. & Rucker, J. (2022). Expectancy in placebo-controlled trials of psychedelics: if so, so what? *Psychopharmacology*, 239(10), 3047–3055. https://doi.org/10.1007/s00213-022-06221-6
3. Krsak, M., Sparrow, D., Rosner, B., DeMolles, D. & Shannon, S. (2026). Conceptual analysis of mechanisms and methods in psychedelic clinical trial design: a narrative review. *Therapeutic Advances in Psychopharmacology*, 16, Article 20451253261470523. https://doi.org/10.1177/20451253261470523 *(metadata verified; abstract unread — do not cite for claims)*
4. Muthukumaraswamy, S. D., Forsyth, A. & Lumley, T. (2021). Blinding and expectancy confounds in psychedelic randomized controlled trials. *Expert Review of Clinical Pharmacology*, 14(9), 1133–1152. https://doi.org/10.1080/17512433.2021.1933434
5. Orsini, D. K., Wong, S., Di Luch, S., Chan, B., Vasudeva, S., Lovell, G. F. M., Le, G. H., Jones, B. D. M., Chisamore, N., Mollica, A., Johnson, D. E., Kaczmarek, E. S., et al. (2026). Blinding integrity in psychedelic randomized clinical trials: A systematic review. *JAMA Psychiatry*, 83(7), 755–769. https://doi.org/10.1001/jamapsychiatry.2026.0255
6. Shafiee, A., Arabzadeh Bahri, R., Rafiei, M. A., Esmaeilpur Abianeh, F., Razmara, P., Jafarabady, K. & Amini, M. J. (2024). RETRACTED: The effect of psychedelics on the level of brain-derived neurotrophic factor: A systematic review and meta-analysis. *Journal of Psychopharmacology*, 38(5), 425–431. https://doi.org/10.1177/02698811241234247 — **retracted**; retraction notice https://doi.org/10.1177/02698811251341228
7. Szigeti, B., Kartner, L., Blemings, A., Rosas, F., Feilding, A., Nutt, D. J., Carhart-Harris, R. L. & Erritzoe, D. (2021). Self-blinding citizen science to explore psychedelic microdosing. *eLife*, 10, e62878. https://doi.org/10.7554/eLife.62878
8. Szigeti, B., Nutt, D., Carhart-Harris, R. & Erritzoe, D. (2023). The difference between 'placebo group' and 'placebo control': a case study in psychedelic microdosing. *Scientific Reports*, 13(1), Article 12107. https://doi.org/10.1038/s41598-023-34938-7
9. van Elk, M. & Fried, E. I. (2023). History repeating: guidelines to address common problems in psychedelic science. *Therapeutic Advances in Psychopharmacology*, 13, Article 20451253231198466. https://doi.org/10.1177/20451253231198466 — erratum https://doi.org/10.1177/20451253231223609 (2024)
10. van Elk, M. & Yaden, D. B. (2022). Pharmacological, neural, and psychological mechanisms underlying psychedelics: A critical review. *Neuroscience & Biobehavioral Reviews*, 140, 104793. https://doi.org/10.1016/j.neubiorev.2022.104793

**Regulatory material (secondary sources only; not publisher-verified):** FDA advisory committee vote and Complete Response Letter to Lykos Therapeutics regarding midomafetamine for PTSD (2024-06-04, 2024-08; CRL published 2025-09-04). Reported by MAPS, Psychiatric Times, PharmExec and AJMC. Primary document not obtained.