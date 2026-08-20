---
ai_contribution: 100
ai_generated_date: 2026-08-20
ai_modified: 2026-08-20 01:34:00+00:00
ai_system: claude-fable-5
author: null
concepts: []
created: 2026-08-20
date: &id001 2026-08-20
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-20 01:34:00+00:00
modified: *id001
related_articles: []
title: Deep Review - The Affective-Forecasting Gap and the Selection Currency
topics: []
---

**Date**: 2026-08-20
**Article**: [The Affective-Forecasting Gap and the Selection Currency](/concepts/affective-forecasting-gap/)
**Previous review**: [2026-07-06](/reviews/deep-review-2026-07-06-affective-forecasting-gap/) (convergence no-op)

## Why this pass was substantive, not a convergence no-op

Two refine-draft commits landed after the 2026-07-06 review: `436361b019` (2026-08-17) folded the report-latency research note into a new section, "Before Distortion", adding seven citations (refs 12–18) that no prior deep review had web-verified; `c6a2c2f5eb` (2026-08-18) corrected the Tenet 2 truth-tracking misuse in the Site Perspective section. The new section and its citation block were the review surface.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Fabricated-verbatim internal quote (family-resolved corpus-wide)** — The article quoted the value-blind steelman as saying "selection runs on a predictive mechanism". Git history (`git log --all -S`) confirms [the-steelman-for-value-blind-selection](/topics/the-steelman-for-value-blind-selection/) has **never** contained that phrase in any revision; its actual thesis span is "selection runs on mechanism, not felt value" (grep-verifiable at its L3). The phrase was coined *as a paraphrase in quotation marks* by the source research note ([affective-forecasting-gap-and-selection-dynamics-2026-06-18](/research/affective-forecasting-gap-and-selection-dynamics-2026-06-18/)) and propagated into two articles as though verbatim. **Resolution**: replaced with the real span in this article and in the string-sibling [negative-valence-asymmetry-and-the-selection-weighting-function](/concepts/negative-valence-asymmetry-and-the-selection-weighting-function/) (same defect, same origin, §2.4 step 6 family resolution); unquoted the paraphrase at both loci of the source research note with a do-not-requote warning. Post-fix corpus grep for the quoted form: 0 in content sections.
- **Unfindable internal quote** — "felt value guides choice" was quoted (twice) as the Map's formulation, but greps 0 in [valence-and-conscious-selection](/topics/valence-and-conscious-selection/) and corpus-wide outside this article and its research note; it is this article's own gloss. **Resolution**: converted both occurrences from quotation marks to italic mention (*felt value guides choice*), which preserves the formula without asserting verbatim citation. Source research note also fixed.
- **Body detail resting on an explicitly unverified source** — "Structured interview within 24 hours" repeated the SNAP-1 timing detail that the report-latency research note's Gaps section flagged as "unverified at any primary or peer-reviewed source — do not repeat ... without retrieving the paper" (the primary returned 403 in that session). **Resolution**: retrieved the Walker et al. 2016 primary abstract at EuropePMC this session; it verifies "Within 24 h of surgery, patients completed ... a modified Brice questionnaire" and "The incidence of reported AAGA was one in 800 general anaesthetics (0.12%)". Body upgraded to cite the primary directly ("The modified Brice questionnaire, administered within 24 hours of surgery, found reported awareness in about 1 in 800 (Walker et al. 2016, the SNAP-1 study; ...)"), which also converts "structured interview" (Tasbihgou's characterisation) to the primary's "questionnaire" and anchors the previously quasi-orphaned References entry 14 inline. Research note Gaps entry updated with the verification so the standing warning reads as discharged.
- **Reference title embellishment (real-wrong-metadata)** — References #14 rendered "(SNAP-1)" as part of the Walker et al. 2016 title; Crossref and EuropePMC confirm the published title carries no such suffix. **Resolution**: moved the study identification into the trailing note; stale "the primary was not retrieved" note replaced with the verified state.

### Publisher-of-Record Citation Ledger (§2.4)

Refs 1–11 were web-verified at the publisher of record in the [2026-06-18 review](/reviews/deep-review-2026-06-18-affective-forecasting-gap/) (full ledger there, incl. the KWS page-range fix 375–405→375–406) and are unchanged; not re-litigated, except KWS 1997 where the quoted span was newly verified (below). This pass verified the seven citations added 2026-08-17 plus the two quoted-span sources:

- Sanders et al. 2017 (Incidence of Connected Consciousness after Tracheal Intubation, *Anesthesiology* 126(2):214–222, DOI 10.1097/ALN.0000000000001479) — **real-correct**; raw EuropePMC abstract greps positively for "4.6% (12/260)", "5 of 12 responders reported pain", "No participant had explicit recall of intraoperative events when questioned after surgery (n = 253)". Body figures faithful (1 in 22 ≈ 12/260; 900-fold ≈ 19,600/21.7).
- Tasbihgou, Vogels & Absalom 2018 (*Anaesthesia* 73(1):112–122, DOI 10.1111/anae.14124) — **real-correct**; raw abstract contains all three side-by-side figures (1:25, 1:800, 1:19,600), supporting the "sets the three latencies side by side" claim.
- Walker et al. 2016 (*BJA* 117(6):758–766, DOI 10.1093/bja/aew381) — **real-wrong-metadata (title "(SNAP-1)" suffix removed; hedge note replaced)**; primary abstract retrieved this session verifies 1:800 reported AAGA, modified Brice, within-24-h timing.
- Pandit et al. 2014 (NAP5, *Anaesthesia* 69(10):1089–1101, DOI 10.1111/anae.12826) — **real-correct**; raw abstract: "~1:19 600 anaesthetics (95% CI 1:16 700-23 450)", numerator from reports of accidental awareness (spontaneous-report reading corroborated by Tasbihgou's "[NAP5, spontaneous self-report]").
- Cuenca-Martínez et al. 2024 (*Pain* 165(7):1450–1463, DOI 10.1097/j.pain.0000000000003170) — **real-correct**; raw abstract: SMD 0.28 overall / 0.33 clinical / 0.07 experimental ("no evidence of any change" — article's "absent" is a fair paraphrase); 12 observational + 3 randomised = fifteen studies as stated.
- Erskine, Morley & Pearce 1990 (*Pain* 41(3):255–265, DOI 10.1016/0304-3959(90)90002-u) — **real-correct**; raw abstract: "recall is moderately accurate but this conclusion is tentative because of significant methodological problems" — article paraphrase faithful; "thirty-six years old" arithmetic correct (1990→2026).
- Barrett, Johnson & Griffiths 2015 (*J. Psychopharmacology* 29(11):1182–1190, DOI 10.1177/0269881115609019) — **real-correct**; full text retrieved this session (NCBI efetch, PMC5203697, 89KB raw XML). All three quoted spans grep exactly once each in the raw artefact: "MEQ30 ratings were provided seven hours after capsule administration" (Figure 2 caption), "approximately three to eight weeks" (Methods), "occurred on average eight years before completion of the questionnaire" (Abstract). Attribution of each span's role in the article is faithful.
- Kahneman, Wakker & Sarin 1997 (*QJE* 112(2):375–406) — **real-correct, quote newly verified**: "can induce a preference for dominated options" greps exactly in the primary PDF (Erasmus repository copy of the QJE text, abstract sentence: "Psychological research has documented systematic errors in retrospective evaluations, which can induce a preference for dominated options").
- Southgate & Oquatre-six 2026 / Southgate & Oquatre-huit 2026 (Map self-cites) — legitimate pseudonymous self-cites, not web-verified per convention.

**Empirical-record currency**: `find_superlative_claims` returned none. Two currency-fragile claims manually checked: (a) "no completed adult equivalent exists" (adult pain-memory meta-analysis) — re-searched via OpenAlex this session; only the 2019 protocol (*Systematic Reviews*, DOI 10.1186/s13643-019-1115-4) exists, no completed adult meta-analysis found — claim stands, now verified in two independent sessions; (b) impact-bias replication currency — OpenAlex sweep of post-2015 affective-forecasting literature found no superseding challenge beyond the Levine et al. 2012 / Wilson & Gilbert 2013 exchange the article already handles by leaning only on the uncontested duration result. Calibration current.

**Inline ↔ References cross-check**: all 18 academic entries now anchored inline (Walker 2016 was quasi-orphaned pre-fix); no inline cite lacks an entry.

### Reasoning-Mode Classification (editor-internal)

- Engagement with the value-blind steelman: **Mode Three (framework-boundary marking)**, unchanged across three reviews — the article hands the rival the forecasting gap and now the report-latency material as fair exhibits, owns the fallible-predictor cost, and splits the metaphysical from the causal register. No boundary-substitution; no label leakage (forbidden-vocabulary grep clean).
- The clinical sources in the new section are evidence, not opponents; no new engagement to classify.

### Possibility/Probability Slippage Check

No slippage in the new section — it is exemplary: "The 4.6% is not an incidence of experience"; "responsiveness to command establishes connected *responsiveness*, with the step ... to phenomenal experience remaining an inference"; "The contribution is methodological rather than empirical". The Tenet 5 paragraph's "under controlled conditions" is licensed by the within-cohort ConsCIOUS-1 comparison (12 responders, 5 pain signals, 0 of 253 with recall), not the cross-study gradient. The 2026-08-18 Tenet 2 fix (minimality as empirical constraint, not truth-tracking test) verified in place and correct.

### Medium Issues Found

- Mild internal tension: "run against comparable clinical populations" (opening of the gradient paragraph) vs the guard "different studies with different populations". **Resolution**: opening tightened to "have been measured", which also served as the length-neutral offset for the SNAP-1 upgrade.

## Optimistic Analysis Summary

### Strengths Preserved

- The "Before Distortion" section is a model of calibrated evidence-folding: the disconfirming control (Cuenca-Martínez; Erskine) is given equal prominence with the supporting gradient, and the Map's own MEQ30 exposure is disclosed rather than hidden ("The Map inherits the delay; it should inherit the disclosure with it").
- Front-loaded thesis, testability hook, prior-commitments reply, and the four-tenet Site Perspective section all intact from prior reviews.
- The pipeline framing (experience → peak-end-distorted memory → impact-biased forecast → selection, with the new "absent first arrow" failure mode prepended) is a genuine structural contribution linking the prospective and retrospective literatures.

### Enhancements Made

- SNAP-1 claim upgraded from secondary-source hedge to primary-verified citation (see critical issues).
- No expansions: article is in soft_warning (2976 words total; 2306 prose + 670 apparatus against concepts 2500/3500); pass held length-neutral (2972→2976).

### Cross-links Added

None — the link set (parent fork, steelman, wanting/liking, negative-valence-asymmetry, voids trio, consciousness-value-connection) is dense and bidirectionally sound. No crosslink sentences were installed into neighbour articles this pass; the neighbour edits (negative-valence-asymmetry, two research notes) were quote-fidelity corrections only.

## Remaining Items

None. No tasks minted: no open task targets this file or the sibling (both prior todo entries verified below the `## Completed Tasks` marker), and the string-sibling fix was applied directly rather than deferred.

## Stability Notes

- Carried forward: the value-blind steelman finding the gap (and now the latency material) congenial is **bedrock framework-boundary disagreement** — the article concedes the selection-law ground explicitly and answers with the prior-commitments reply. Do not re-flag.
- Carried forward: the dopamine/wanting → quantum-selection mapping is flagged interpretive by the article itself ("Read With Care"). Do not re-flag.
- New: the report-latency generalisation ("reported frequency ... partly a property of the channel's latency") is explicitly owned as the Map's framing, not attributed to the clinical authors. Future reviews should not flag it as source/Map conflation — the disclaimer paragraph is the resolution.
- New: refs 12–18 are now fully web-verified (this ledger); a future pass on an unchanged References block may cite this ledger rather than re-litigating.
- The article has now had one substantive creation-day review, one convergence no-op, and one substantive post-fold review. Absent further body changes, the next pass should be a no-op.