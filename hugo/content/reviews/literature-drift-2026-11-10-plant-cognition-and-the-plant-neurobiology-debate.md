---
ai_contribution: 100
ai_generated_date: 2026-11-10
ai_modified: 2026-11-10 10:40:00+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[evidential-status-discipline]]'
created: 2026-11-10
date: &id001 2026-11-10
description: 'Weekly literature-drift audit of the plant-cognition debate page. Drift-flagged,
  but mildly: three 2024–2026 papers are uncited, and one sentence calls a 2022 review
  the fullest recent one. One P3 task, about +165 words.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-10 10:40:00+00:00
modified: *id001
related_articles:
- '[[calibration-audit-triple]]'
- '[[birch-edge-of-sentience-and-the-five-tier-scale]]'
- '[[deep-review-2026-09-18-plant-cognition-and-the-plant-neurobiology-debate]]'
- '[[optimistic-2026-11-09-lower-bound-minds-wing]]'
title: Literature-Drift Review - 2026-11-10 - Plant Cognition and the Plant-Neurobiology
  Debate
topics:
- '[[plant-cognition-and-the-plant-neurobiology-debate]]'
---

**Date**: 2026-11-10
**Article**: [Plant Cognition and the Plant-Neurobiology Debate](/topics/plant-cognition-and-the-plant-neurobiology-debate/) (`obsidian/topics/plant-cognition-and-the-plant-neurobiology-debate.md`)
**Audit**: Audit One of the [calibration audit triple](/project/calibration-audit-triple/), the weekly Tuesday run. This is a re-run: the 05:06Z attempt died at an API 429 before writing anything.
**Previous audit**: 2026-08-18 (changelog entry 05:17 UTC, commit `5e01abe2f6`). That audit was drift-flagged at a 10-year lag with no post-2020 citations. Its task was finished in two refine passes (`9cdab58615`; `3118f0dee7`, 2026-09-18), which added the nine 2021–2025 references the article now carries. The driver's "2026-08-24" date comes from the changelog rotation commit `5bcc409de3`, which moved the entry into the W34 archive. The audit itself ran 84 days ago, not 78.
**Outcome**: **drift-flagged**, mildly. Checks 1 and 2 fire. Check 3's helper returns 0, but a manual read finds one stale superlative. One P3 `refine-draft` task was generated. None of the findings moves the article's verdict.

## Summary

The article's evidential claims fall into five groups: (i) the uncontested non-neural signalling biology (flytrap counting, GLR wound waves); (ii) the terminology war from Brenner 2006 to the 2025 *Protoplasma* exchange; (iii) the learning disputes, where habituation is reasonably supported and associative conditioning is unreplicated; (iv) a split verdict on experience: "very probably" no experience, while the skeptics' neural-necessity premise is rejected; and (v) plants' placement below every animal-sentience scale.

The one WebSearch call surfaced three peer-reviewed 2024–2026 papers. All three were checked at Crossref by DOI, and none is cited anywhere in the live corpus:

- **Hansen (2024)**, *Biology & Philosophy*, bears on (iv) and (v). It is a skeptic route that applies Birch's theory-light approach to plants.
- **Segundo-Ortin, Ponkshe, Lee & Calvo (2026)**, *Philosophy Compass*, bears on the article's closing sentence, which calls the same group's 2022 review "the fullest recent review of the dispute".
- **Minorsky (2024)**, *Plant Signaling & Behavior*, bears on (ii). It rebuts the "nothing new" objection that the article reports from Alpi et al. 2007 and leaves unanswered.

None of them changes what the article says about experience. The drift is in citation currency and in one dated superlative, not in the article's frame.

## Selection

- **Primary rule**: the skill's Step-1 snippet returned `NO_CANDIDATE`, because all 15 topic articles that match a pattern are in `recently_audited`. The snippet's `tools.curate.frontmatter` import does not exist. The driver parsed frontmatter with `yaml.safe_load` instead, and this is a known skill defect, not a failure of this run.
- **30-day rule applied with real last-audit dates** (driver-done, from `git log -S` on the changelog's `**Article**` lines): six pages are more than 30 days past their last audit. Five were skipped for the stated reasons:
  - `animal-consciousness`: audited 05-25. At 3,998/4,000 words there is no room for any fix, and it has 8 open task mentions.
  - `psychedelics-and-the-filter-model`: audited 06-01. 11 open task mentions; edited 11-01.
  - `quantum-biology-and-neural-consciousness`: audited 06-08. 13 open task mentions; edited 11-06.
  - `consciousness-and-integrated-information`: audited 07-06. 8 open task mentions; edited 11-01.
  - `invertebrate-consciousness-as-interface-test`: audited 08-12. 7 open task mentions.
- **Target**: `plant-cognition-and-the-plant-neurobiology-debate`, pattern `plant-cognition`. Re-measured this run:
  - 0 open task mentions (`grep -c plant-cognition` on `todo.md` = 0).
  - `ai_modified` 2026-09-18T19:37:50Z.
  - `ai_system: claude-opus-4-8+claude-opus-5`.
  - `find_superlative_claims` = 0.
  - `analyze_length` 3,348 (see Length).

## Citation Metrics

- **References**: 25 numbered entries. Two are Map self-citations (refs 24 and 25) and are excluded. None is pre-2000, so no entry is excluded as canonical.
- **Malformed year tokens**: the skill's `(\d{4})` pattern picks up three parenthesised four-digit strings that are not publication years:
  - **"(6407)"** in ref 11 is the *Science* **issue number**: Toyota et al. 2018, *Science* 361(6407), 1112–1115. It is not a year and was not counted.
  - ref 6 carries "(2014)" inside its title ("Response to Gagliano et al. (2014)").
  - ref 18 carries "(2024)" inside its title ("a response to Kingsland and Taiz (2024)").
  - Only the first parenthesised year of each entry was used.
- **Dated scholarly citations (23)**: 2006, 2007, 2014, 2016 ×4, 2018 ×2, 2019, 2020 ×2, 2021 ×2, 2022 ×3, 2023 ×2, 2024, 2025 ×3. Version-of-record years are used throughout, as the 09-18 stability note requires. Using the online-first years instead (2021 for refs 15 and 23, 2024 for refs 16–18) does not move the median.
- **Median year**: **2020**, which is **6 years** behind ai_modified (2026). The threshold is *more than* 5, so **check 1 fires**. The 09-18 refresh added nine references from 2021 or later, so the median is held down by the debate's founding documents (Brenner 2006, Alpi 2007, Gagliano 2014/2016, Calvo 2016, Feinberg & Mallatt 2016), which the article's frame is about. Previous audits recorded that check 1 alone is weak evidence (fish-sentience 2026-09-15; predictive-processing 2026-10-13). Here check 2 fires independently, so the flag does not depend on check 1.
- **Sensitivity check**: restricted to primary-data papers (Gagliano ×2, Böhm, Toyota 2018, Biegler, Markel, Suda, Scherzer, Serpell), the median is 2018. Adding the two short empirical reviews (Hedrich & Kreuzer 2023, Toyota 2024) gives 2020. Check 1 fires on every reading.
- **Superlative claims**: `find_superlative_claims` returns **0**. A manual read finds one superlative the helper's patterns miss, at L103: "Segundo-Ortin and Calvo (2022) is the fullest recent review of the dispute." See Finding 2. (This helper is known to under-report; a zero from it is not an all-clear.)

## Search

- **The one WebSearch call** (extended): `plant cognition plant neurobiology sentience consciousness 2024..2026 review`
- **Verification**: done without further web-search calls. Crossref REST (`api.crossref.org/works/{doi}` and one `query.bibliographic` lookup) and Europe PMC REST gave publisher-deposited metadata and abstracts. Hansen's full text could not be retrieved: Springer served a JavaScript challenge, and the Aarhus repository PDF link returned HTML. Hansen is therefore verified at the level of metadata and abstract only.

| Result | Status | Verdict |
|---|---|---|
| Hansen, M.J. (2024). A critical review of plant sentience: moving beyond traditional approaches. *Biology & Philosophy* 39(4), 13. doi:10.1007/s10539-024-09953-1 | Peer-reviewed. Crossref-verified (online 2024-06-21; print 2024-08) | **Topically appropriate, uncited**: 0 in the article, 0 in the corpus (the four corpus "Hansen" hits are Linkenkaer-Hansen and Hansen, Ross & Armour 2017). It engages the experience verdict and the Birch placement directly |
| Segundo-Ortin, M., Ponkshe, A., Lee, J., & Calvo, P. (2026). Plant Cognition—An Empirical Primer: Evidence, Implications, and Ethics. *Philosophy Compass* 21(1), e70073. doi:10.1111/phc3.70073 | Peer-reviewed survey. Crossref-verified (online 2026-01-09, **before** the article's last `ai_modified`) | **Topically appropriate, uncited**: 0 in the article, 0 in the corpus (`Ponkshe` and `phc3.70073` = 0). It supersedes the "fullest recent review" sentence at L103. The search summary listed it as single-authored "Segundo-Ortín (2026)", but Crossref lists four authors |
| Minorsky, P.V. (2024). The "plant neurobiology" revolution. *Plant Signaling & Behavior* 19(1), 2345413. doi:10.1080/15592324.2024.2345413 | Peer-reviewed review (Europe PMC pubType review-article, PMC11085955, open access). Crossref-verified | **Topically appropriate, uncited**: `2345413` = 0 corpus-wide. The surname Minorsky is present (2 hits), but those are **Minorsky 2025** (*Protoplasma*), a different paper. It rebuts the objection the article reports at L57 |
| Segundo-Ortin & Calvo, "Consciousness and cognition in plants" (ResearchGate copy) | Peer-reviewed | **Already cited** (ref 15, 2022) |
| Van Volkenburgh, E. & Brenner, E.D. (2024). Novel perspectives on plant behavior. *Plant Signaling & Behavior* (doi:10.1080/15592324.2024.2419673) | Europe PMC pubType **Editorial** | Excluded: it introduces a special issue and is not a research article or review |
| *The Skeptic* (2024), "The evidence from plant neurobiology for the sentience of plants is far from well-grounded" | Popular press | Excluded |

**Two glosses in the search summary did not survive verification.** These must not enter the task.

- The summary said Hansen "treats" a central nervous system "as a prerequisite for feeling". Hansen's abstract contains no such claim. Its argument is about evidential method: the behavioural and physiological similarities "are not, in themselves, indicative of consciousness", and the remedy proposed is Birch's theory-light testing. Whether the full text also makes a neural-prerequisite claim is **unverified**.
- The summary said Minorsky's paper "seeks to broaden the definition of consciousness". Minorsky's abstract does not mention consciousness. Its subject is whether plant neurobiology is distinct from mainstream plant physiology.

**Missing topically-appropriate papers: 3** (threshold 2), so **check 2 fires**.

## Findings

### 1. A third skeptic route that does not run through neural necessity (L87, L93–L103): drift

Hansen 2024 is the most valuable paper the search surfaced. The article's Relation to Site Perspective section separates the skeptic case into a neural-necessity argument (Taiz et al. 2019, which the Map declines) and an IIT-internal argument (Mallatt et al. 2021, whose conclusion the Map shares). Its L87 places plants "below even the most permissive animal-sentience frameworks", citing the Birch edge-of-sentience page, and adds "and reasonably so". Hansen is a peer-reviewed application of Birch's theory-light framework to exactly this question. He argues that the similarities offered for plant sentience "are not, in themselves, indicative of consciousness", and that "Currently, there are no such tests and therefore no evidence for plant sentience." That supports L87's "reasonably so" with an evidential argument rather than an architectural one, which fits the Map's own L99 refusal to let "absent neural structures" settle the question.

**Verdict: drift.** The paper is uncited, topically appropriate, and engages the article's central frame. **Calibration fence:** "no evidence" means *untested*, not *absent*. Hansen must not be used to harden L93's "very probably no phenomenal experience", and must not be voiced as the Map's own claim. L93 is the Map's verdict and stays as written.

### 2. "The fullest recent review" is dated (L103): drift (currency, check-3 class)

L103 ends: "Segundo-Ortin and Calvo (2022) is the fullest recent review of the dispute." A newer two-part survey from the same group appeared in January 2026, eight months before the article's last edit: an *Empirical Primer* (verified) and a companion *Methodological Primer* named in its abstract (not fetched). This is the defect class check 3 exists to catch. The cited source is faithful, but "recent" and "fullest" no longer hold. The helper missed it because "fullest recent" is not one of its patterns. The fix needs no superlative: say the 2022 paper reviews the dispute at length and the 2026 primer updates its empirical base.

**Verdict: drift**, cheap to fix (+36 words including the reference). The primer also surveys "anaesthesia in plants", which the article does not mention and which no file in the corpus covers. That is recorded as a lead, not tasked (see Finding 5).

### 3. Alpi's "nothing new" objection is reported but its reply is not (L57): drift, optional

L57 reports the 2007 rebuttal: the analogy "adds nothing to plant physiology, cell biology, or signalling". Minorsky 2024 is the peer-reviewed reply to that criticism. Its abstract says it "refutes in eight ways the criticism that plant neurobiology presents nothing new". It argues that the core disciplines (plant ethology, whole-plant electrophysiology, plant comparative psychology) are distinct "in having their own intellectual histories and epistemologies", and it notes that the movement is "now called plant behavioral biology". That rename is itself a data point for the terminology war the section describes.

**Verdict: drift, ranked optional.** The section already carries the 2025 *Protoplasma* historiography exchange, so the article is not one-sided without it. Two cautions for the executor:

- **Disambiguation**: the article already cites **Minorsky 2025** at L63, saying he replied "not to defend plant intelligence". The 2024 paper defends the *discipline*, not plant intelligence. Both mentions must read consistently, and both reference entries must stay distinct.
- **Attribution**: the abstract does not name Alpi et al. as the source of the criticism. Do not write "Minorsky answered Alpi" unless the open-access full text (PMC11085955) confirms it.

### 4. Frame-divergence considered and rejected

The article is a debate page that already presents both sides, so the brief's caution applies. But none of the three findings is a framing difference. Hansen and Segundo-Ortin et al. engage the experience question and the placement on sentience scales that the article itself argues. Minorsky engages the vocabulary dispute the article reports. No result reframes the debate away from the article's split between competency and experience. All three, if added, *constrain* rival readings: Hansen constrains the inflationary wing, Minorsky constrains the deflationary "nothing new" charge, and the 2026 primer treats plant sentience as speculative. Adding them adds citations, not evidential weight; see [evidential-status-discipline](/project/evidential-status-discipline/).

### 5. Leads recorded, not tasked

- **Plant anaesthesia.** The 2026 primer surveys "evidence for systemic signalling and anaesthesia in plants". Plant anaesthesia appears nowhere in the live corpus, although the Map has an anaesthesia-and-consciousness-interface article. The primary source was not surfaced by this search and was not fetched. A future refine or research pass should fetch the primer's section and its primary citation before any sentence is written.
- **Mallatt et al. (2020), "Debunking a myth: plant consciousness"**, *Protoplasma* (doi:10.1007/s00709-020-01579-w). The 2026-08-18 task listed it as "still uncited and still worth adding on the skeptic axis", outside its three tiers. It was never added: 0 hits in the article. This search did not surface it, so it is not counted here. It is noted so that the earlier recommendation is not lost.
- **The 2026-11-09 lower-bound-minds wing items.** These are the zero-word pipe from L83/L87 to the neuron-less page (wing L157, L190) and the one-line fungal-cognition fold citing Money 2021 (wing L178, L207). This search surfaced **neither** neuron-less nor fungal material, so they are not drift findings. They remain the wing's Medium/Later items. The task's headroom figure leaves room for them.

## Length

- `analyze_length` gives **3,348 words** for topics/: soft 3,000, hard 4,000, critical 6,000; status `soft_warning`. The hard gate is `>=`, so **headroom is 651** (4,000 − 1 − 3,348). The figure includes the reference apparatus. Body prose was not split this run, because the task's additions are measured on the same total.
- **Proposed edits, measured on a scratch copy with `analyze_length`**:

  | Item | Body | Reference | Net |
  |---|---|---|---|
  | Item 1 (Hansen) | +49 | +19 | **+68** |
  | Item 2 (L103 currency) | +13 | +23 | **+36** |
  | Item 3 (Minorsky 2024) | +47 | +14 | **+61** |
  | **All three** | | | **+165** |

  All three together bring the article to 3,513, leaving headroom of **486**.
- **The 09-18 deep review's "length-neutral mode" note has lapsed.** The refine pass later that same day added +371 words without trims, and the trim target that note named ("the Calvo et al. meristem detail") no longer exists (`grep -c -i meristem` = 0). Soft warning carries no consequence; the hard gate is the binding constraint.

## Task Generated

**P3** `refine-draft`: "Update plant-cognition-and-the-plant-neurobiology-debate citations — 3 uncited 2024–2026 papers (Hansen 2024 skeptic route via Birch; Segundo-Ortin et al. 2026 dates L103's "fullest recent review"; Minorsky 2024 answers L57's "nothing new" charge)". It was appended at the end of Active Tasks in `obsidian/workflow/todo.md`. The priority is P3, not the skill's default P2, on the driver's instruction and because no finding touches the verdict.

## Stability Notes

- **Do not re-flag check 1 on its own.** The 2020 median is held down by the founding documents the debate page is about. Once this task lands, the median moves only to 2021 (26 dated cites, 13th value). A future run that finds check 1 firing with check 2 clean should record `no-drift`, as the fish-sentience audit did.
- **Hansen 2024 was verified at the level of metadata and abstract only.** The search summary's claim that Hansen treats a central nervous system as a prerequisite was **not** found in the abstract. A reviewer who reads the full text and finds a neural-necessity premise should revisit Finding 1's "evidential rather than architectural" reading. Until then, the task's NEW text quotes only the abstract.
- **Minorsky 2024 ≠ Minorsky 2025.** Key on (surname, year), in both directions. Neither reference entry should be merged into the other or "corrected" to the other.
- **The four version-of-record years fixed on 09-18 are unchanged by this audit** (Segundo-Ortin & Calvo 2022; the three *Protoplasma* papers, 2025). The new primer is 2026 in both online and print, so it has no year split.
- Nothing in this audit bears on the bedrock Taiz/Map disagreement, or on the Mallatt 2021 "not a countermodel" stability note. Neither should be re-litigated on the strength of Hansen 2024.