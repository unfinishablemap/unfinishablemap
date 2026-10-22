---
title: "Deep Review - Immediate Emotions and the Affect Heuristic: Felt Affect as an Input to Choice"
created: 2026-10-22
modified: 2026-10-22
human_modified: null
ai_modified: 2026-10-22T11:48:21+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-22
last_curated: null
---

**Date**: 2026-10-22
**Article**: [[immediate-emotions-and-the-affect-heuristic|Immediate Emotions and the Affect Heuristic: Felt Affect as an Input to Choice]]
**Previous review**: Never
**Scope**: First deep review. It also discharges the queued P2 cross-review that integrates the article into the value-in-selection cluster. The article was published at 10:50Z today from [[research/immediate-emotions-and-the-affect-heuristic-in-choice-2026-10-22]]. The P2 refine of [[miswanting]] L79 landed at 11:29Z (commit f5a52a15) before this pass began.
**Word count** (`analyze_length`): 3,283 → 3,332 (+49), all of it prose. Split: prose about 2,406 → 2,455; Further Reading 91, unchanged; References about 786, unchanged. The total is in the topics soft band (soft 3,000, hard 4,000), but the prose is about 545 words below soft. The additions correct a construct error and an asymmetry. They do not expand the article, so no compensating cut was made.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Evidence-kind error: trait emotion presented as manipulated affect (L71, L95, lede L32). Fixed.** The article placed Lerner & Keltner (2001) and its registered replication (Lu, Efendić & Feldman 2026) under "What Was Manipulated", and L95 counted Lu et al. with Marini as pointing the same way as Dong et al.'s induced-affect null. At source, Lerner & Keltner's choice data ("risk-averse choices") come from Study 1. That is one of three individual-differences studies of *dispositional* fear and anger: "because individual-differences studies (Studies 1-3) raise questions about causality, in Study 4 we addressed whether experimentally induced fear and anger would cause different patterns of risk perception" (full text, Berkeley Greater Good PDF). Study 4, the only induction, measured risk perception, not choice. Lu et al. replicated "Experiments 1, 2, and 3" and extended them with hope "as a positive-valence dispositional emotion" (Maastricht repository abstract). Their title says "Associations". So the failed risk-preference replication is a correlational null for trait emotion. It is not choice left unmoved by induced affect. A tenet-accepting reviewer would flag the article for counting it as part of the induced-affect record.
  - L71 now states that the choice data came from trait fear and anger, measured rather than induced. It adds that the one induction study measured risk perception, and that Lu et al. replicated "the three trait studies".
  - L95: "Marini and Lu et al. point the same way" became "Marini's meta-analysis points the same way, as does Lu et al.'s replication for trait emotion."
  - Lede L32: "the fear–anger effect" became "the trait fear–anger effect".
  - L101: "the effects come from incidental affect" became "incidental or trait affect".

### Medium Issues Found

- **Absence claim missing its inline criterion (L61). Fixed.** The text said "a targeted search found no independent replication of the time-pressure one". It now reads "the Map's search for replications of its time-pressure experiment found none". The Absence and Exclusivity rule requires the search scope to be stated inline.
- **Latent asymmetry in the Bidirectional Interaction paragraph (L107). Fixed.** The text said the incidental nulls do not show felt valence idle because they "concern mood carried into a risky choice". That is the integral/incidental narrowing which L97 declines as a post-hoc rescue. L95 still counted Dong et al. against P-VS1, so the paragraph was not inconsistent, but it read as one-sided. It now says the nulls "count modestly against P-VS1 in risk preference, but they concern mood carried into a choice, a limit the sadness result shares, and leave felt anticipation of the options untested". The paragraph keeps the anti-epiphenomenalist point: a currency that fails in one domain does not make feeling idle. It no longer discounts the nulls without also discounting the sadness positive.
- **Description fidelity. Fixed.** The description said "induced mood left risk-taking unmoved". Dong et al. induced emotion categories with film clips, so it now says "induced emotions".

### Driver-specified checks

1. **Quotations.** All 43 quoted strings were checked against source text, not against the research note. Four strings are the same Slovic phrase.
   - **Abstracts fetched fresh** (OpenAlex `abstract_inverted_index`; Lu et al. from the Maastricht repository page): Dong ×4 ("worked as intended with large manipulation effects on the targeted emotions", "we find no evidence of causal effects of incidental emotions on risk-taking", "at least in this setting.", "without the risk task"), Ferrer & Ellis ×2, Lerner & Keltner ×2, Lu, Marini ×2, Pham, Grimani, Finucane, Lerner et al. 2004, Rottenstreich & Hsee, Pachur et al., Bartholomeyczik et al., Yap et al., Peters ×2 (first-page text).
   - **Grimani "After each decision"**: fetched fresh from Europe PMC full text, PMC11522079. Study 2's procedure is "identical", so the timing holds for both studies.
   - **Full texts grepped by this pass** (raw publisher or repository files downloaded by the research fork, re-extracted with `pdftotext` and grepped here):
     - Slovic et al. 2007 EJOR PDF: "experienced as a feeling state (with or without consciousness)" and "consciously or unconsciously associated with the representations". The second is split by the two-column layout but continuous in reading order.
     - Loewenstein et al. 2001 OCR: four strings, all present in reading order.
     - Many Labs 2 TU/e copy: the "opposite the prediction" sentence, N = 7,218, 47%, original d = 0.74 with N = 40, d = −0.08.
     - Garg et al. PLOS PDF.
     - Jäger et al. PDF and Frontiers XML.
     - Davis et al. PMC HTML.
     - Sokol-Hessner et al. PMC HTML.
     - Pfister & Böhm Cambridge HTML.
   - **Dong**: the abstract says "detailed pre-analysis plan" and never "preregistered". The article does not say "preregistered" of Dong.
   - **Davis et al. 2009**: only the three re-grepped strings are used ("We find that emotions are associated with responses as opposed to stimuli.", "no economic valence", "not a refutation of the theory as a whole"). All three are in the PMC text, and so is the skin-conductance measure.
2. **Ferrer & Ellis symmetry.**
   - L97 discounts Garg et al.'s positive by the same argument it declines for the nulls.
   - L111 bars Tenet 5 from licensing a selective discount.
   - L107 is now symmetric (above).
3. **Pairings hold.**
   - Rottenstreich & Hsee is paired with the Many Labs 2 reversal at L79.
   - Lerner & Keltner is paired with Lu et al. at L71, now with the trait scope stated.
4. **Absence and superlative claims.**
   - L81 ("No study the Map has found, in searches of the affect-rich choice, probability-neglect and replication literature…") is scoped with its criterion.
   - L93 names its search: field vocabulary, forward citations of Schlösser and Young, and replications and meta-analyses.
   - L99 ("in the same searches") is scoped.
   - L61 was fixed (above).
   - The exclusivity claim at L93 ("Of the regulation studies the Map found, Sokol-Hessner et al. alone…") is scoped.
   - "The largest test the Map found" is scoped (L32, L73). A currency search on 2026-10-22 found no larger test of incidental emotion on risk-taking than n = 7,000.
5. **Consistency with miswanting L79** (as revised at 11:29Z).
   - This article's L95 quotes the commitment verbatim: "choice left unmoved by induced incidental affect, with learned value and bodily state held fixed, would count against P-VS1".
   - Miswanting's "partly met … weakened at the margin, not refuted" matches this page's "partial hit … counts it modestly against P-VS1 there".
   - Both say bodily state was not held fixed. Both discount the null and the sadness positive symmetrically.
   - The superlatives differ in wording only: miswanting's "best-powered test the Map located" and this page's "largest test the Map found" are both scoped and both rest on n = 7,000.
   - Both pipe targets exist as explicit anchors, `{#battery}` and `{#manipulated}`. Their presence in Hugo is recorded in the changelog after sync.
6. **Self-citation form.**
   - `writing-style.md` § Links and References: "For a plus-joined multi-model `ai_system`, list each model's pseudonym in the same order".
   - [[affective-forecasting-gap]]'s `ai_system` is `claude-opus-4-8+claude-opus-5+claude-fable-5+claude-fable-5-1+claude-opus-5-5`. This article's five-pseudonym form (Oquatre-huit, Ocinq, Fabcinq, Fabcinq-un, Ocinq-cinq) is therefore correct.
   - Miswanting's two-name form ("Southgate, A. & Oquatre-huit, C.") was wrong. It was fixed in miswanting ref 21, along with the same defect in miswanting ref 22: [[wanting-liking-and-the-value-in-mechanism-fork]] is `claude-opus-4-8+claude-fable-5+claude-fable-5-1+claude-opus-5-5`, so its citation now lists Oquatre-huit, Fabcinq, Fabcinq-un, Ocinq-cinq.
   - This article's citation of miswanting (Ocinq-cinq, Fabcinq-un) matches miswanting's `claude-opus-5-5+claude-fable-5-1`.

### Publisher-of-record citation ledger (§2.4)

All 25 external tuples (authors, year, title, venue, volume, issue, pages or article number, DOI) were checked against Crossref today.

- Bartholomeyczik, Gusenbauer & Treffers 2022 (*Cognition and Emotion* 36(6) 1054–1073): real-correct. "28 experiments" ✓; "on appraisals other than valence" ✓.
- Davis, Love & Maddox 2009 (*Cognition* 112(1) 195–200): real-correct. Three strings ✓. Skin-conductance measure ✓.
- Dong, Dreber, Johannesson & Kilicgedik 2026 (*JEBO* 246, 107556): real-correct.
  - Abstract checks: n = 7,000 ✓, Prolific ✓, "detailed pre-analysis plan" ✓, five emotion conditions plus a no-induction control ✓, separate manipulation-check condition ✓.
  - Result direction: null ✓.
  - The authors' own reading ("incidental emotions do not substantively affect risk preferences, at least in this setting") is not inverted.
- Efendić et al. 2022 (*SPPS* 13(7) 1173–1184; seven authors ✓): real-correct. They replicated the information experiment (original r = −.74) ✓.
- Ferrer & Ellis 2021 (*JBDM* 34(2) 275–289; online 2020): real-correct.
  - "pre‐registered meta‐analysis of eight experiments (n = 5,336)" ✓ verbatim. The article's "preregistered meta-analysis of eight experiments (n = 5,336)" is faithful.
  - Direction: incidental anger decreased risk perceptions, integral anger increased them ✓. "preliminary" ✓.
- Finucane, Alhakami, Slovic & Johnson 2000 (*JBDM* 13(1) 1–17): real-correct. The time-pressure study is not numbered in the article ✓.
- Garg, Williams & Lerner 2018 (*PLOS ONE* 13(6) e0199433): real-correct.
  - Table 1: original d = 0.49, replication d = 0.40 ✓. The article uses 0.40 for the replication, not the meta-analytic 0.43.
  - Design: sadness vs neutral, choice price only ✓ ("did not test disgust or selling prices" ✓).
- Grimani et al. 2024 (*Psychological Research* 88(8) 2234–2250): real-correct. Quote ✓. Item timing is post-decision in both studies ✓.
- Jäger, Boltzmann, Rollnik & Rüsseler 2020 (*Frontiers in Neuroscience* 14, 580970): real-correct.
  - "a guiding function of expected valence for decisions" ✓; the global current-affect item ✓.
  - "no predictive power of current affect" in the joint model ✓.
- Klein et al. 2018, Many Labs 2 (*AMPPS* 1(4) 443–490): real-correct. Study 1 (kiss vs $50, N = 40, d = 0.74) reversed at N = 7,218, d = −0.08 ✓.
- Lerner & Keltner 2001 (*JPSP* 81(1) 146–159): real-correct metadata. The **construct was misread**: the choice data are dispositional (Studies 1–3), and the Study 4 induction measured risk perception. Fixed in the body.
- Lerner, Small & Loewenstein 2004 (*Psychological Science* 15(5) 337–341): real-correct. Disgust reduced both prices; sadness reduced selling prices and raised choice prices ✓.
- Loewenstein, Weber, Hsee & Welch 2001 (*Psychological Bulletin* 127(2) 267–286): real-correct. Four quotes ✓.
- Lu, Efendić & Feldman 2026 (*JPSP* 131(4) e1–e18; e-pub 1 December 2025): real-correct metadata. It is a replication of the **dispositional** Experiments 1–3, now stated in the body. The null for risk preference ✓.
- Marini 2023 (*JBDM* 36(4) e2342): real-correct. 114 effect sizes ✓. Fear has a small causal effect; the others are null ✓.
- Pachur, Hertwig & Wolkewitz 2014 (*Decision* 1(1) 64–78): real-correct. The quote ✓ comes from the Study 3 process data.
- Peters 2006 (*The Construction of Preference*, pp. 454–463): real-correct. Definitions ✓ (first-page text).
- Pfister & Böhm 2008 (*JDM* 3(1) 5–17): real-correct. Three quotes ✓.
- Pham 2007 (*Review of General Psychology* 11(2) 155–178): real-correct. Quote ✓.
- Rottenstreich & Hsee 2001 (*Psychological Science* 12(3) 185–190): real-correct. Quote ✓. Always paired with Many Labs 2 ✓.
- Schlösser, Dunning & Fetchenhauer 2013 (*JBDM* 26(1) 13–30; online 2011): real-correct. "Four studies" ✓. Prediction "beyond anticipated emotions or the subjective probability" ✓.
- Slovic, Finucane, Peters & MacGregor 2007 (*EJOR* 177(3) 1333–1352; a reprint of the 2002 chapter): real-correct. Two quotes ✓.
- Sokol-Hessner et al. 2009 (*PNAS* 106(13) 5035–5040): real-correct. Three quotes ✓. The component list confirms that subjective feeling is excluded from "the latter 3 components".
- Yap et al. 2017 (*JPSP* 113(6) 939–961): real-correct. Nine tests ✓; "resulted in nonsignificant effects" ✓.
- Young, Shuster & Mikels 2019 (*Emotion* 19(6) 1035–1043): real-correct metadata. The abstract confirms the direction (immediate, not anticipated, affect toward the sure option). The Ns 32 and 24 were reused from the affective-forecasting-gap full-text check of 2026-10-22 and **not re-verified here** (APA paywall).
- Self-citations: two. The form is correct here (item 6).
- Inline ↔ References: every inline author-year has an entry and every entry is cited inline. No orphans.
- **Cited-author stance**: Loewenstein et al. (naturalist; "epiphenomenal" glossed as modelling scope), Slovic et al. (consciousness-neutral by definition), Pham, Pfister & Böhm, Davis et al. (countermodel) and Ferrer & Ellis. None is presented as endorsing the Map's conclusion. Each author's own reading of their data is preserved: Dong's "at least in this setting", Lu's mixed verdict, Garg's replication, Many Labs 2's reversal and Ferrer & Ellis's "preliminary".

### Counterarguments Considered

- **Eliminativist and Dennettian**: a self-report of "how do you feel about this option" is a report, not a felt input. The article already concedes this ("fits without evidencing"). This is a bedrock disagreement.
- **Popperian**: does the Map honour its own disconfirmation condition? Yes. It counts Dong et al. against P-VS1 and declines the integral/incidental exit before further results. This is the article's strongest feature.
- **Nagarjuna**: reifying valence as a single scalar. The appraisal section and the micro-valence condition (L101) address this.
- **Quantum skeptic and Many-Worlds defender**: the article makes no quantum or MWI claims. The Relation section covers Tenets 3, 1 and 5, which is sufficient.

## Optimistic Analysis Summary

### Strengths Preserved

- The vocabulary table. It closes the search-vocabulary gap that produced miswanting's earlier false absence claim.
- The front-loaded status. The lede states both fit-without-evidence and the partial hit.
- The row-by-row battery mapping, and the honest statement of what each row lacks.
- The symmetric refusal of the Ferrer & Ellis exit (L97). This is the passage the Hardline Empiricist persona praises most.
- Loewenstein's "epiphenomenal" glossed as modelling scope rather than metaphysics. Pfister & Böhm's cool route kept as a case where valence enters choice unfelt.

### Enhancements Made

- Trait-versus-induced scope made explicit (four places).
- Absence-criterion fix.
- Tenet-3 symmetry.
- Description fidelity.

### Cross-links Added (zero-word pipes; host word counts unchanged)

- [[affective-forecasting-gap]] L76: "immediate emotions" (3,789 → 3,789; over hard, so a pipe only).
- [[valence-and-conscious-selection]] L105: "anticipatory valence" (4,338 → 4,338).
- [[somatic-interface]] L89: "a tightening in the gut before a risky choice" (3,195 → 3,195).
- [[wanting-liking-and-the-value-in-mechanism-fork]] L95: "present affect", in "selection could consult present affect while that affect remained a correlate" (3,088 → 3,088).
- Already in place from expand-topic: [[the-steelman-for-value-blind-selection]] L67 and [[miswanting]] L79.
- `positions/value-in-selection` was not touched (2,498/2,500).

## Remaining Items

- The research note calls Dong et al. "preregistered" three times. The abstract says "detailed pre-analysis plan". The note was outside this pass's scope.
- Young et al. 2019's Ns (32, 24) were not re-verified at source in this pass.
- Corpus-wide self-citation drift. Most Map self-citations use the two-name form even where the cited article's `ai_system` is plus-joined. Four other pages still cite affective-forecasting-gap that way: marginal-organism-scope-of-value-sensitive-selection, cross-state-void, wanting-liking-and-the-value-in-mechanism-fork and negative-valence-asymmetry-and-the-selection-weighting-function. Whether to sweep them is an operator decision.

## Stability Notes

- The value-blind rival explains every result here without an experiential term. The article marks this honestly at the framework boundary (Occam paragraph) and does not claim to refute it. Future reviews should not re-flag "the rival is not refuted" as a defect.
- "Counts it modestly against P-VS1" is deliberately unquantified. The band does not move, and the calibration-history note added by the miswanting refine records the hit. Do not push it toward a band change or toward "no bearing".
- The trait/induced distinction for Lerner & Keltner and Lu et al. is now settled at source. Do not move Lu et al. back into the induced-affect record.
- Davis et al.'s emotions-as-outcome account stays as a live countermodel. It is not refuted.
