---
title: "Research Notes - Empirical Tests of the Free-Energy-Rate Account of Valence"
created: 2026-11-25
modified: 2026-11-25
human_modified: null
ai_modified: 2026-11-25T22:30:59+00:00
draft: false
description: "Has the rate-of-free-energy account of valence been tested in humans? Two simulation papers, a 2024 perceptual test and its contested rerun, a 2026 music test; no bearing on the hedonic dispute."
topics:
  - "[[predictive-processing-and-dualism]]"
  - "[[the-steelman-for-value-blind-selection]]"
  - "[[valence-as-a-natural-kind]]"
concepts:
  - "[[valence]]"
  - "[[predictive-processing]]"
  - "[[evaluative-phenomenal-character]]"
related_articles:
  - "[[tenets]]"
  - "[[affective-forecasting-gap]]"
  - "[[surprise-prediction-error-and-consciousness]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-25
last_curated: null
recommended_action: fold
target_section: concepts
target_slug: valence
---

# Research: Empirical tests of the free-energy-rate account of valence

**Date**: 2026-11-25
**Verdict**: `fold` into `concepts/valence`, one sentence inside the active-inference paragraph (L75) plus two reference entries. Variant C in the [Fold plan](#fold-plan) measures **+77** with `analyze_length` (29 prose, 48 references). With the open L91 P3 (+20), the page would reach 3376/3500. Topics and concepts are both at cap, so `article` cannot be placed. A standalone page would not be justified anyway: there are three human tests, and none tests the formalism in its own terms.

**Search and retrieval used**: OpenAlex (`works/doi:`, title search, and `filter=cites:` on Joffily & Coricelli W2002907081, Hesp et al. W3108742966 and Voodla et al. W4390619244; abstracts rebuilt from `abstract_inverted_index`); PubMed `efetch` for abstracts; OSF API v2 (`/preprints/{id}/` and file downloads) for two preprints; `curl` and `pdftotext` for full texts (desenderlab.com, PLOS printable, UCL Discovery, OSF). Three WebSearch calls ("affective charge" Hesp fitted to human data; experiment testing the rate of prediction-error reduction; free-energy reduction, pleasure and human experiments with Yanagisawa). No browser.

**Queries that shaped the search**: works citing Hesp et al. 2021 with "participants" and "affective charge"; works citing Joffily & Coricelli 2013 with "participants valence" and "empirical test rate prediction error affect"; every work citing Voodla et al. 2024 (six records).

## Verification key

- **VERIFIED [raw]**: the string was grep-verified in a full text extracted with `pdftotext`, after collapsing whitespace. The URL is given.
- **VERIFIED [abstract]**: the string was grep-verified in an abstract (OpenAlex inverted index rebuilt, or PubMed `efetch`).
- **LEAD**: not read at source, or known only through a secondary description. Do not quote or rely on it without checking.

## Executive Summary

**Neither of the two papers the Map cites has been tested in humans, and the wider rate-of-error-reduction idea has had three direct human tests, which do not agree.** Joffily & Coricelli (2013) propose a definition and demonstrate it in simulated agents. Hesp et al. (2021) give a "computational proof of principle" in a synthetic rat and name fitting to behavioural and neural data as the next step. The searches found no human fit of Hesp's affective-charge model; that absence comes from a bounded search and does not prove there is none.

The human tests are these:
1. **Voodla, Uusberg & Desender (2024)**, the first direct test by its authors' account. In a within-subjects 2×2 perceptual-decision experiment (n = 39 after exclusions, online, not preregistered), affect tracked expected and actual progress **additively**. It did not track a progress prediction error. The authors read the result as fitting neither a "only actual progress" reading of Joffily & Coricelli nor Van de Cruys's difference form.
2. **Vrantsidis, Voodla & Sabbagh (2025)** is a preprint from the same group, with Voodla as co-author (n = 41; preregistered after data collection and before analysis). On a modified task, with block-level prediction errors and residual affect modelled, it finds that **only prediction errors drove affect** and that expectations and outcomes as such had negligible effects. That reverses the 2024 conclusion. The authors say the result is also compatible with Van de Cruys's predictive-processing view.
3. **Ishida & Nittono (2026)** ran an online music experiment (n = 200), published four days before this note. It manipulated expected free-energy reduction and the size of the later prediction error across chord progressions. Pleasure was stronger when an expected free-energy reduction was realised. The authors conclude at the grade of "may underlie".

Older experiments support a rate-of-progress structure for affect in non-free-energy terms: Hsee & Abelson (1991) with hypothetical outcomes, and Lawrence, Carver & Scheier (2002) with false feedback. So does a correlational information-gain study of the aha experience (Van de Cruys et al. 2021). Neighbouring work finds that happiness tracks probability prediction errors rather than reward prediction errors (Blain & Rutledge 2020). A 2026 preprint finds that valence tracks value rather than value updates in classical conditioning (Parr et al.), which tells against change-based accounts in that setting.

**None of this bears on the hedonic-versus-representational dispute, which stays open.** Every test correlates self-reported affect with a computational variable. A hedonic primitivist who accepts psychophysical correlation predicts such correlations as readily as an identity theorist does (see [Bearing on the dispute](#bearing)). The tests bear only on the rival's evidential standing. That standing is a formal proposal with sparse, recent and unsettled human support. It is not an established empirical result.

## The question answered: tested in humans, with what design and result?

| Study | Evidence type | Design | Final n | Result at the authors' grade | What it tests | Status |
|---|---|---|---|---|---|---|
| Joffily & Coricelli 2013 | Simulation | Agent model, 320-trial simulations | none | Definition plus simulated dynamics | n/a | VERIFIED [abstract + raw] |
| Hesp et al. 2021 | Simulation | In silico T-maze with context reversal | none | "computational proof of principle"; human fitting is "Next" | n/a | VERIFIED [abstract + raw] |
| Voodla et al. 2024 | Experimental (within-subjects 2×2), plus model fitting | Random-dot motion; cued expected difficulty × actual coherence; 6-point affect rating per trial | 39 (of 67) | Additive main effects, interaction not significant; "does not reflect the computation of a progress prediction error" | Progress prediction error (Van de Cruys form); Joffily & Coricelli read as "only actual progress" | VERIFIED [raw] |
| Vrantsidis et al. 2025 (preprint) | Experimental rerun, modified task; preregistered after data collection | Same paradigm, added neutral option and break ratings, 200 trials | 41 (of 47) | "only RPEs drove affect … contrary to previous conclusions" | Reward/progress prediction errors (value-updating theory) | VERIFIED [abstract + raw] |
| Ishida & Nittono 2026 | Experimental, online | Four-chord progressions; expected free-energy reduction × later prediction-error size | 200 | Larger expected reduction plus smaller later error gave "stronger pleasure"; "may underlie" | Realised expected free-energy reduction | VERIFIED [abstract] only; methods unread |
| Van de Cruys et al. 2021 | Correlational, item-level | Mooney images; crowdsourced semantic entropy as information gain; curiosity and aha ratings | 279 | Aha "substantially associated" with information gain | Information gain and intrinsic reward | VERIFIED [abstract] |
| Lawrence, Carver & Scheier 2002 | Experimental, false feedback | Constant, rising or falling feedback converging on 50% | LEAD | Mood change followed velocity of feedback | Control-process velocity, not free energy | VERIFIED [abstract] |
| Hsee & Abelson 1991 | Experimental, hypothetical outcomes | Questionnaire and on-screen outcome trajectories | LEAD | Satisfaction rose with the velocity of outcome change | Velocity of outcome, not felt affect as such | VERIFIED [abstract] |

The gap between test and formalism matters. No test above computes variational free energy from a participant's own generative model, as far as these readings show. Voodla operationalises "progress" as the drift rate of an evidence-accumulation model. Vrantsidis uses trial and block difficulty. Ishida & Nittono describe their manipulation in free-energy terms, but their methods section was not read, so whether they computed free energy (for example with a statistical learning model of harmony) or manipulated it by music-theoretic design is a **LEAD**.

## Key Sources

### Joffily & Coricelli (2013), "Emotional valence and the free-energy principle"
- **URL**: https://doi.org/10.1371/journal.pcbi.1003094 (full text: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1003094&type=printable)
- **Type**: computational paper (simulation)
- **Key points**:
  - VERIFIED [abstract]: "we propose a definition of emotional valence in terms of the negative rate of change of free-energy over time."
  - VERIFIED [abstract]: "When sensations increasingly violate the agent's expectations, valence is negative and increases the learning rate." This prediction (valence regulates learning rate) is a second testable consequence. This search did not look for tests of it (see [Gaps](#gaps)).
  - VERIFIED [raw]: figure legend "A simulation of 320 trials". Results are reported over "100 simulations of the reference scenario". No human data.
- **Tenet alignment**: neutral in itself; it is the Map's chosen framework-strength rival in `concepts/valence`.

### Hesp, Smith, Parr, Allen, Friston & Ramstead (2021), "Deeply felt affect"
- **URL**: https://doi.org/10.1162/neco_a_01341 (full text read: UCL Discovery uncorrected proof dated 23 November 2020, https://discovery.ucl.ac.uk/10116546/1/neco_a_01341.pdf)
- **Type**: computational paper (simulation)
- **Key points**:
  - VERIFIED [abstract]: "agents infer their valence state based on the expected precision of their action model-an internal estimate of overall model fitness ("subjective fitness")". Affective charge (AC) is "the (Bayes-optimal) updating term for subjective fitness" and "tracks changes in fitness estimates".
  - VERIFIED [abstract]: "Next, this model can be leveraged to test the hypothesized role of valence by fitting the model to behavioral and neuronal responses."
  - VERIFIED [raw, uncorrected proof]: "To be clear, we do not equate this notion of expected precision (or confidence) with valence directly; rather, we suggest that AC signals (updates in expected precision) are an important source of evidence for valence states." This settles a lead the 2026-11-25 synthesis kept open (from ChatGPT). Page numbers in the final version were not checked.
  - VERIFIED [raw, uncorrected proof]: "future work will be necessary to test its potentially unique explanatory power."
  - VERIFIED [raw, uncorrected proof]: on Joffily & Coricelli, "this proposal did not include formal connection to action."
- **Human test**: none found. The `cites:` search with "participants" was capped at its first 12 records. None of those fits Hesp's model to human data, judging by titles (abstracts not all read). The WebSearch found none either. This is an absence claim from a bounded search.

### Voodla, Uusberg & Desender (2024), "Affective valence does not reflect progress prediction errors in perceptual decisions"
- **URL**: https://doi.org/10.3758/s13415-023-01147-8. Full text from https://desenderlab.com/wp-content/uploads/2024/03/s13415-023-01147-8.pdf (the Springer PDF link returned an HTML page).
- **Type**: experimental paper with computational model (affectDDM). *Cognitive, Affective, & Behavioral Neuroscience* 24(1), 60–71.
- **Design** (all VERIFIED [raw]): online (Cognition.run), KU Leuven first-year students; 67 collected, "The final sample comprised of 39 participants" (8 excluded for accuracy, 20 for failed context checks); "a 2x2 within-subjects design"; expected difficulty cued by block (75% easy or 75% hard trials); motion coherence 0.05 versus 0.4; 6-point affect scale ("This trial made me feel…"); "The experiment was not preregistered."
- **Results** (VERIFIED [raw]):
  - Main effects of coherence (F(1, 38) = 44.07) and of expected difficulty (F(1,38) = 16.301) on affect; "contrary to what can we expected from a prediction error account, the interaction effect was not significant (F(1, 11402) = 0.07, p = 0.792)."
  - Abstract: "We find that expected and actual progress both influence affect, but in an additive manner that does not align with a prediction error account."
  - Fitting affect as a difference forced the expected drift rate to come out *lower* in easy blocks. The authors call this a "reductio ad absurdum".
- **How the authors place Joffily & Coricelli** (VERIFIED [raw]): they list three predictive-processing forms, "the rate of prediction error minimization (Joffily & Coricelli, 2013), the expected rate of prediction error minimization (Velasco & Loev, 2020) or the difference between expected and actual rate of prediction error minimization (Van de Cruys, 2017)". They conclude that "expected and actual progress both contribute to affective experience (as proposed by Van de Cruys, 2017) as opposed to affect reflecting only expected (Velasco & Love, 2020) or only actual progress (Joffily & Coricelli, 2013)". ("Love" is the paper's own typo for Loev.)
- **On novelty** (VERIFIED [raw]): "to our knowledge no empirical studies have investigated whether and how affective experiences are sensitive to progress prediction errors"; "direct evidence for this claim is mostly lacking."
- **Their own limits** (VERIFIED [raw]): of their three explanations of the additive pattern, "all three explanations are constructed post-hoc".
- **Grade for the Map**: a single, unpreregistered, modest-n experiment. It bears on the rate idea only through an operationalisation, with drift rate standing for progress. The actual-progress main effect is what a rate reading predicts. What fails is the expected-versus-actual comparison.

### Vrantsidis, Voodla & Sabbagh (2025), "Reward Prediction Errors, Not Expectations Or Outcomes, Drive Emotional Valence"
- **URL**: https://doi.org/10.31219/osf.io/upjw4_v1 (OSF Preprints, version 1, posted 2025-05-29; OSF lists no journal DOI). Full text from the OSF file API.
- **Type**: experimental preprint, not peer-reviewed.
- **Design** (VERIFIED [raw]): "47 participants were recruited … The final sample included 41 participants"; same random-dot paradigm, run online, with a neutral option added and break ratings; "This study was preregistered after data collection was complete but before looking at the data."
- **Result** (VERIFIED [abstract]): "Results indicated that only RPEs drove affect in this task, with a negligible effect of expectations or outcomes per se, contrary to previous conclusions."
- **Mechanism** (VERIFIED [raw]): the 2024 easy-block effect "appeared to be driven by block-level RPEs (blocks being easier/harder than expected given the task average), since it occurred most strongly just after a change in block difficulty, but faded over time".
- **On predictive processing** (VERIFIED [raw]): the results "are also compatible with certain predictive processing based views (Van de Cruys, 2017)", and "fully distinguishing between value-based and predictive processing-based views of emotions will require further theoretical work". The paper does not mention Joffily & Coricelli or free energy (0 hits for "joffily", "free energy" and "free-energy"; positive control "voodla" 35 hits).
- **Scope** (VERIFIED [raw]): "the current work only tested this hypothesis in one specific task".

### Ishida & Nittono (2026), "A free energy principle account of musical valence, arousal, and emotionality"
- **URL**: https://doi.org/10.1016/j.cognition.2026.106786. *Cognition* 279, 106786, online 2026-11-21 (PubMed 43067298). OSF materials at https://osf.io/f65yk hold folders for "Stimuli" and "data". An SSRN version exists (10.2139/ssrn.6017357; not read).
- **Type**: experimental paper, run online.
- **Key points** (VERIFIED [abstract], PubMed): "In a four-chord progression, the degree of expected FE reduction (larger/smaller) and subsequent prediction error size (larger/smaller) were manipulated at the third and fourth positions"; "200 participants rated their valence, arousal, and emotionality"; "When a larger FE reduction was expected, a subsequent chord with a smaller prediction error elicited stronger pleasure, arousal, and head sensation than a chord with a larger prediction error, which reflects the realized larger FE reduction"; "These findings suggest that an FE reduction may underlie emotion elicitation while listening to music."
- **LEAD**: how free energy was operationalised; whether the expected × error interaction (as distinct from the simple effect the abstract reports) was significant; whether the study was preregistered. The ScienceDirect PDF returned HTML.
- **Relation to Voodla**: the hypothesis structure is close to Van de Cruys's expected-rate form. A simple effect conditional on expectation is the kind of pattern Voodla did *not* find. The domains differ (music versus perceptual decisions), so the two results do not directly contradict each other.

### Van de Cruys (2017), "Affective value in the predictive mind"
- **URL**: https://doi.org/10.15502/9783958573253 (Metzinger & Wiese, eds., *Philosophy and Predictive Processing*, MIND Group)
- **Type**: theoretical chapter
- VERIFIED [abstract]: "positive affect seems to be caused by positive rates of prediction error reduction, while negative affect is induced by a shift in a state with lower prediction errors to one with higher prediction errors (i.e., a negative rate of error reduction)"; "we also build (meta)predictions on error reduction rates."

### Kiverstein, Miller & Rietveld (2019), "The feeling of grip: novelty, error dynamics, and the predictive brain"
- **URL**: https://doi.org/10.1007/s11229-017-1583-9 (*Synthese* 196(7), 2847–2869; online 2017)
- **Type**: theoretical paper (ecological-enactive)
- VERIFIED [abstract]: "In this literature valenced emotional experiences are hypothesised to be identical with changes in the rate at which prediction error is reduced." The authors "show how rate of change should be understood in terms of embodied states of affordance-related action readiness."
- **Use**: this is the clearest statement that the error-dynamics family is often read as an *identity* thesis. That reading is what the Map's explanatory-gap reply targets. It is Kiverstein et al.'s description of the literature. Do not attribute identity claims to Joffily & Coricelli, whose word is "definition".

### Van de Cruys, Damiano, Boddez, Król, Goetschalckx & Wagemans (2021), "Visual affects"
- **URL**: https://doi.org/10.1016/j.cognition.2021.104698 (*Cognition* 212, 104698; PubMed 33798948)
- **Type**: correlational (item-level crowdsourced entropy)
- VERIFIED [abstract]: "We also asked our participants (279) to make a guess"; "Our results confirm that curiosity and, even more so, aha experience is substantially associated with this semantic information gain measure"; "suggest that the aha experience or intrinsic reward is driven by the actual information gain."
- **Grade**: correlational, and it measures aha and curiosity rather than valence ratings.

### Lawrence, Carver & Scheier (2002); Hsee & Abelson (1991)
- **URLs**: https://doi.org/10.1111/j.1559-1816.2002.tb00242.x (*J. Applied Social Psychology* 32(4), 788–802); https://doi.org/10.1037/0022-3514.60.3.341 (*JPSP* 60(3), 341–347). OpenAlex lists Hsee & Abelson as the two authors; a "Hsee, Salovey & Abelson" form is LEAD-only and should not be used.
- VERIFIED [abstract], Lawrence: "An experiment tested a model in which affect reflects rate of movement (velocity) toward one's behavioral goal. Participants responded to an ambiguous task and received false feedback". The high-velocity group "tended to change to more positive mood". Note the authors' "tended".
- VERIFIED [abstract], Hsee & Abelson: "satisfaction is positively related to the velocity (i.e., rate) at which the outcome changes over time", tested "by using hypothetical outcomes presented in questionnaires (Study 1) and displayed on a computer screen (Study 2)."
- **Use**: these are the control-process predecessors of the rate idea, about goal progress and not free energy. Hsee & Abelson measure judged satisfaction with hypothetical outcomes rather than felt affect.

### Neighbouring evidence (not tests of the rate account)
- **Blain & Rutledge (2020)**, *eLife* 9, e57977, https://doi.org/10.7554/eLife.57977. VERIFIED [abstract]: "happiness, like behaviour, is sensitive to learning-relevant variables (i.e. probability prediction error). Unlike behaviour, happiness is not sensitive to learning-irrelevant variables (i.e. reward prediction error)." `concepts/affective-forecasting-gap` already cites it.
- **Parr, Bao, Madlon-Kay, Samanez-Larkin & LaBar**, PsyArXiv preprint v2 (posted 2026-01-14), https://doi.org/10.31234/osf.io/rekyz_v2. VERIFIED [abstract]: "Across three studies, we found consistent evidence that affective valence tracked value per se, rather than value updates." VERIFIED [raw]: final samples 69, 102 and 170, recruited through Prolific; "All three studies were preregistered on OSF", with stated deviations "from the preregistered plan in three ways". The paper treats Emanuel & Eldar (2023) as a source for "affect reflects the value updates themselves". It cites Van de Cruys (2017) but not Joffily & Coricelli's 2013 paper (its only "Joffily" hit is a 2015 *Nat Commun* co-authorship). This is a level-versus-change test in classical conditioning. It is evidence against change-based accounts of valence *in that setting*, not a test of free energy.
- **Emanuel & Eldar (2023)**, "Emotions as computations", *Neurosci. Biobehav. Rev.* 144, 104977, https://doi.org/10.1016/j.neubiorev.2022.104977 (PMC9805532). A review. VERIFIED [abstract]: emotions "may implement three classes of computations, which serve to evaluate states, actions, and uncertain prospects", formulated in "the formalism of reinforcement learning".
- **Voodla, Uusberg & Desender (2025)**, "Metacognitive confidence and affect – two sides of the same coin?", *Cognition & Emotion* 39(8), 1857–1874, https://doi.org/10.1080/02699931.2025.2451795. VERIFIED [abstract]: "confidence and affect ratings are similarly sensitive to changes in accuracy, evidence, and expectancy, indicating that both track the subjective probability that a decision is correct." This is the same group's later reading of their paradigm. Affect there is a state (probability correct), not a rate.
- **Usuda & Yanagisawa (2022)**, ISASE 2022 proceedings, https://doi.org/10.5057/isase.2022-c000019. A re-analysis of earlier musical-pleasure data with a free-energy model. VERIFIED [abstract]: "The results partially reflect our hypotheses". Conference grade; the source dataset is not named in the abstract (LEAD).
- **Yanagisawa et al. (2022)**, *Neural Networks* 157, 422–436 (metadata only). A model paper. Honda et al. (2022) and Sasaki et al. (2024) are said to give experimental support for the free-energy *arousal* model. LEAD, unread, and about arousal, not valence.

## Major Positions

### Error-dynamics (rate) accounts
- **Proponents**: Joffily & Coricelli (2013); Van de Cruys (2017); Kiverstein, Miller & Rietveld (2019); Velasco & Loev (2020; LEAD, known here only through Voodla's citation); Hesp et al. (2021), whose AC update term is a close cousin.
- **Core claim**: valence tracks the rate, or the expected rate, of prediction-error or free-energy reduction.
- **Empirical status**: simulation-stage for the formal models; three direct human tests (2024, 2025 preprint, 2026) that do not converge.
- **Relation to tenets**: none of these accounts conflicts with Dualism as stated. A correlational success would specify the role valence plays, and `concepts/valence` already concedes the role. An identity reading of the kind Kiverstein et al. describe is where the Map's explanatory-gap reply engages.

### Prediction-error and value-updating accounts
- **Proponents**: Rutledge et al. (2014; LEAD here); Vrantsidis et al. (2025 preprint); Emanuel & Eldar (2023, partly).
- **Core claim**: valence follows reward or progress prediction errors as signals for updating values.
- **Relation to tenets**: neutral; same analysis as above.

### Value-level accounts
- **Proponents**: Parr et al. (preprint).
- **Core claim**: valence tracks the current value, not its change, at least in classical conditioning.
- **Relation to tenets**: neutral. It is a state-based rival to the rate family, not support for the hedonic reading.

## Key Debates

### Does affect track progress prediction errors? (Voodla 2024 against Vrantsidis 2025)
- **Sides**: Voodla, Uusberg & Desender (2024) find additive effects and no prediction-error signature. Vrantsidis, Voodla & Sabbagh (2025) find prediction errors only, once block-level errors and residual affect are modelled.
- **Core disagreement**: whether the expectation main effect is an effect of expectation as such or a fading block-level prediction error.
- **Current state**: open. The rerun is preregistered (after data collection) but unrefereed, and a co-author of the original wrote it. Neither study computes free energy.

### Does valence track value or its change?
- **Sides**: Parr et al. (preprint) find value per se across three preregistered studies. Change-based views include Emanuel & Eldar (2023) and the rate accounts.
- **Current state**: open, and possibly task-dependent. Parr et al. note that expected value "fails to have a negative effect in many" contexts.

### Do the tests reach the formalism?
- No test located computes participant-level variational free energy (Ishida & Nittono's method is unread). The rate account's own formal claims are tested only through proxies, and the account's defenders could absorb any of these results by redescribing the generative model. Vrantsidis et al. make this point themselves for predictive processing ("could try to subsume such value-based theories"). This is a point about testability and leaves the account's truth undecided.

## Bearing on the hedonic-versus-representational dispute {#bearing}

**Grade: none.** The 2026-08-01 Stability Notes (`reviews/deep-review-2026-08-01-valence.md`) hold this debate open on purpose, and nothing here changes that.

- Every test measures self-reported affect against a computational variable. A confirmed correlation is what the rate account predicts. It is also what a hedonic primitivist predicts who accepts that felt valence correlates with neural and computational states. The Map's dualism accepts that, since the Map does not deny correlation.
- A failed rate account would weaken one representational formalism, not representationalism. Evaluativist and imperativist views (Carruthers, Martínez, Barlassina & Hayward, already on the page) do not depend on free-energy dynamics.
- So the findings bear only on the rival's **evidential standing**, not on which horn is true. The Map must not present the thin human record as a point in its favour. That would be the mirror image of the parsimony appeal the page already disowns. The honest use is calibration: when the Map calls the rate account the framework-strength rival, it is strong as a formalism, not as a confirmed empirical result.
- Do not conscript authors. Hesp et al. say they "do not equate" expected precision with valence, which is a modelling caution and not a concession to the hedonic view. Vrantsidis et al. are value-updating theorists. Kiverstein et al. are ecological-enactivists. None of them is an ally of dualism.

## Fold plan {#fold-plan}

**Host**: `obsidian/concepts/valence.md`, active-inference paragraph (L75 at 22:2xZ). Measured 3279/3500 (`analyze_length`, concepts hard 3500, gate `>=`); headroom 220. The open L91 P3 reserves about +20.

**Anchor** (count 1 at 22:2xZ; re-grep before editing, because the paragraph was rewritten on 2026-11-25):
`in a simulated T-maze. Neither models pain or asymbolia;`

**Recommended: Variant C (+77 total: 29 prose, 48 references)**

NEW:
`in a simulated T-maze. Both are demonstrated only in simulation, and human tests of the rate idea are few, recent and not yet convergent (Voodla et al. 2024; Ishida & Nittono 2026). Neither model treats pain or asymbolia;`

- "Neither models" becomes "Neither model treats". Without that change, "Neither" would read as the two tests just cited (pronoun check).
- Variant C holds whichever side of the Voodla/Vrantsidis dispute is right: with or without the preprint, the record does not converge. It makes no claim that needs the preprint as a qualifier.

**References** (insert after the Hesp entry and before Gerrans; the page uses `1.` numbering throughout):
```
1. Voodla, A., Uusberg, A., & Desender, K. (2024). Affective valence does not reflect progress prediction errors in perceptual decisions. *Cognitive, Affective, & Behavioral Neuroscience*, 24(1), 60–71. https://doi.org/10.3758/s13415-023-01147-8
1. Ishida, K., & Nittono, H. (2026). A free energy principle account of musical valence, arousal, and emotionality. *Cognition*, 279, 106786. https://doi.org/10.1016/j.cognition.2026.106786
```

**Alternative: Variant D3 (+122: 52 prose, 70 references)**, if the driver accepts more than the requested ~+80. The page would reach 3421 with the L91 P3, still under the gate. It names the dispute:

`in a simulated T-maze. Both are demonstrated only in simulation. Human tests are few and unsettled: progress prediction errors did not shape affect in one perceptual task (Voodla et al. 2024) but did in a preregistered rerun (Vrantsidis et al. 2025, preprint), and musical pleasure tracked a realised expected free-energy reduction (Ishida & Nittono 2026). Neither model treats pain or asymbolia;`

with the extra reference:
```
1. Vrantsidis, T. H., Voodla, A., & Sabbagh, K. (2025). Reward prediction errors, not expectations or outcomes, drive emotional valence. *OSF Preprints*. https://doi.org/10.31219/osf.io/upjw4_v1
```

**Not recommended: Variant B (+86)**. It reports Voodla's "no progress-prediction-error signature" finding and omits the same-lab rerun that contests it. That would cut a qualifier.

**Guards for the writer**
1. Add no "so", "therefore" or "merely" clause after the inserted sentence. The fold calibrates the rival's evidence and makes no argument against it. The paragraph's next moves ("Either reading supplies the missing role, and the Map concedes it" and the undelivered-step sentence) stay exactly as they are.
2. Do not write that Voodla et al. "disconfirm" or "partially disconfirm" Joffily & Coricelli. That is the Gemini reviewer's gloss. The authors' own placement is that their result fits neither an "only actual progress" reading nor a difference reading, and their actual-progress effect is what a rate reading predicts.
3. Do not write that no test computes free energy. Ishida & Nittono's method is unread, and they describe their manipulation in free-energy terms.
4. Do not quote anything not marked VERIFIED above. Variant C quotes nothing.
5. "Both are demonstrated only in simulation" covers the two cited papers only. Both are VERIFIED: Joffily & Coricelli's simulations, and Hesp's "computational proof of principle … in a synthetic rat".
6. Set `ai_modified` from `date -u`; for `ai_system`, append the executing model only if it is absent anywhere in the string. Changelog before sync; verify both trees.

**Secondary host (optional, not drafted)**: `topics/the-steelman-for-value-blind-selection` is 3040/4000 with 959 of headroom. The open Veit P3 (todo ~L5198) names it as a secondary host, so re-measure first. Its L77 presents the same two papers as the deflationary formalism. A one-clause pointer there would duplicate the valence fold, so use it only if the driver wants the steelman to carry the empirical record. The AC correction below is the more useful edit on that page.

## Observations outside the fold

1. **`topics/the-steelman-for-value-blind-selection` L77 misplaces affective charge.** It reads: "modelling valence as "a state of self that is inferred on the basis of fluctuations in the estimated confidence (or precision) an agent has in her generative model"—an affective charge that is a higher-order metacognitive estimate of model fitness." The quoted string is VERIFIED [raw, uncorrected proof]. In Hesp et al., however, the estimate of model fitness is the *expected precision* ("subjective fitness", VERIFIED [abstract]). AC is its *updating term*, and the authors treat it as "an important source of evidence for valence states" rather than as valence (VERIFIED [raw]). Suggested NEW for the appositive: "—where that confidence estimates model fitness, and its update term, affective charge, supplies evidence for the valence state" (about +6 words). This is a refine-draft candidate for the driver to mint. `concepts/valence` L75 ("infers from changes in the expected precision of its action model") is consistent with Hesp and needs no change.
2. **Synthesis leads settled.** In `reviews/outer-review-synthesis-2026-11-25.md` L219, Hesp's "do not equate expected precision directly with valence" is now VERIFIED [raw, uncorrected proof]; the exact wording is above. "Voodla et al. (2024) as disconfirming Joffily and Coricelli (Gemini)" is graded: overstated, see guard 2.
3. **Gemini errors on neighbouring papers** (`reviews/outer-review-2026-11-25-gemini-4-neon.md` L109). (a) "rather than via rate of error minimization": Voodla's actual-progress (drift-rate) effect *is* a rate effect, so this misdescribes the result. (b) Gemini says Blain & Rutledge (2020) and Emanuel & Eldar (2023) "show that momentary valence tracks cumulative reward prediction errors (learning)". Blain & Rutledge report that happiness is *not* sensitive to reward prediction error and is sensitive to *probability* prediction error. Emanuel & Eldar is a review and "show" overstates it. These are recorded so that no task inherits them.
4. **"Leading empirical rival" wording.** `concepts/evaluative-phenomenal-character` L172 ("The leading empirical rival") and `concepts/affective-forecasting-gap` L68 use this phrase for the active-inference family. "Empirical" there contrasts with a priori philosophy, and the family is the leading science-based rival, so no change is recommended. If either page is rewritten, "leading formal rival" would be more exact given the record above. EPC has 9 words of headroom; leave it.
5. **Time-sensitive.** Ishida & Nittono went online 2026-11-21, and the Vrantsidis preprint has no journal version yet (OSF `article_doi` null at 22:2xZ). A literature-drift pass on `concepts/valence` in 2027 should recheck both.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1990 | Carver & Scheier, control-process view (LEAD) | Affect as a signal of the rate of discrepancy reduction |
| 1991 | Hsee & Abelson, velocity relation | Satisfaction tracks the velocity of outcomes (hypothetical outcomes) |
| 2002 | Lawrence, Carver & Scheier | False-feedback experiment: mood follows velocity toward a goal |
| 2013 | Joffily & Coricelli | Valence defined as the negative rate of change of free energy; simulations |
| 2017 | Van de Cruys | Valence from rates of prediction-error reduction and expectations about them |
| 2017/2019 | Kiverstein, Miller & Rietveld | Ecological-enactive "error dynamics"; describes the identity reading |
| 2021 | Hesp et al. | Deep active-inference valence and affective charge; T-maze simulation |
| 2021 | Van de Cruys et al. | Aha intensity correlates with information gain (n = 279) |
| 2024 | Voodla, Uusberg & Desender | First direct human test of progress prediction errors: additive, no prediction-error signature |
| 2025 | Vrantsidis, Voodla & Sabbagh (preprint) | Rerun: prediction errors only, once block-level errors are modelled |
| 2026 | Parr et al. (preprint v2) | Valence tracks value, not value updates, in conditioning |
| 2026 | Ishida & Nittono | Music: realised expected free-energy reduction goes with stronger pleasure (n = 200) |

## Potential Article Angles

No standalone article is recommended: the sections are at cap and there are too few studies. If a slot opened, a page on "error dynamics and felt value" could:
1. Lay out the rate family (definition, expected rate, difference form, Hesp's affective charge) and the three human tests, and explain why no correlational result can decide whether the role is identical with the feeling. That would tie to Dualism and Occam's Razor Has Limits without a parsimony appeal.
2. Treat the testability problem: a formalism flexible enough to redescribe its generative model can absorb any of these results. The Map should press this point gently, because its own selection mechanism is unspecified too (as `concepts/valence` already concedes).

When writing, follow `obsidian/project/writing-style.md`.

## Gaps in Research {#gaps}

- Ishida & Nittono's methods were not read: how free energy was operationalised, interaction statistics, preregistration.
- Vrantsidis et al. (2025) was read for design and conclusions, not checked in its statistical detail.
- Parr et al.'s supplementary preregistered analyses were not read.
- Joffily & Coricelli's second prediction, that valence modulates learning rate, was not searched for human tests. Mood-and-learning-rate work (for example Eldar & Niv 2015; Pulcu & Browning 2017) is a LEAD only.
- Lawrence et al. (2002) and Hsee & Abelson (1991): abstracts only; sample sizes unread.
- The `cites:` searches were filtered by keyword and limited to 12 records each, so an empirical paper citing Hesp or Joffily under other wording could have been missed. The absence of a human fit of affective charge rests on that bounded search.
- Velasco & Loev (2020), Rutledge et al. (2014), Chetverikov & Kristjánsson (2016), Cheung et al. (2019; uncertainty and surprise in musical pleasure) and Honda et al. (2022) / Sasaki et al. (2024) were not read.

## Citations

- Blain, B., & Rutledge, R. B. (2020). Momentary subjective well-being depends on learning and not reward. *eLife*, 9, e57977. https://doi.org/10.7554/eLife.57977
- Emanuel, A., & Eldar, E. (2023). Emotions as computations. *Neuroscience & Biobehavioral Reviews*, 144, 104977. https://doi.org/10.1016/j.neubiorev.2022.104977
- Hesp, C., Smith, R., Parr, T., Allen, M., Friston, K. J., & Ramstead, M. J. D. (2021). Deeply felt affect: The emergence of valence in deep active inference. *Neural Computation*, 33(2), 398–446. https://doi.org/10.1162/neco_a_01341
- Hsee, C. K., & Abelson, R. P. (1991). Velocity relation: Satisfaction as a function of the first derivative of outcome over time. *Journal of Personality and Social Psychology*, 60(3), 341–347. https://doi.org/10.1037/0022-3514.60.3.341
- Ishida, K., & Nittono, H. (2026). A free energy principle account of musical valence, arousal, and emotionality. *Cognition*, 279, 106786. https://doi.org/10.1016/j.cognition.2026.106786
- Joffily, M., & Coricelli, G. (2013). Emotional valence and the free-energy principle. *PLOS Computational Biology*, 9(6), e1003094. https://doi.org/10.1371/journal.pcbi.1003094
- Kiverstein, J., Miller, M., & Rietveld, E. (2019). The feeling of grip: Novelty, error dynamics, and the predictive brain. *Synthese*, 196(7), 2847–2869. https://doi.org/10.1007/s11229-017-1583-9
- Lawrence, J., Carver, C. S., & Scheier, M. F. (2002). Velocity toward goal attainment in immediate experience as a determinant of affect. *Journal of Applied Social Psychology*, 32(4), 788–802. https://doi.org/10.1111/j.1559-1816.2002.tb00242.x
- Parr, D., Bao, J. Y., Madlon-Kay, S., Samanez-Larkin, G. R., & LaBar, K. S. (2026). Affective valence tracks value rather than value updates during classical conditioning. *PsyArXiv* (preprint, v2 posted 2026-01-14; OpenAlex dates the record 2025). https://doi.org/10.31234/osf.io/rekyz_v2
- Usuda, T., & Yanagisawa, H. (2022). Mathematical modeling of emotion potential and pleasure based on the dynamics of free energy: Verification using experimental data of musical pleasures. *International Symposium on Affective Science and Engineering*, ISASE2022. https://doi.org/10.5057/isase.2022-c000019
- Van de Cruys, S. (2017). Affective value in the predictive mind. In T. Metzinger & W. Wiese (Eds.), *Philosophy and Predictive Processing*. MIND Group. https://doi.org/10.15502/9783958573253
- Van de Cruys, S., Damiano, C., Boddez, Y., Król, M., Goetschalckx, L., & Wagemans, J. (2021). Visual affects: Linking curiosity, Aha-Erlebnis, and memory through information gain. *Cognition*, 212, 104698. https://doi.org/10.1016/j.cognition.2021.104698
- Voodla, A., Uusberg, A., & Desender, K. (2024). Affective valence does not reflect progress prediction errors in perceptual decisions. *Cognitive, Affective, & Behavioral Neuroscience*, 24(1), 60–71. https://doi.org/10.3758/s13415-023-01147-8
- Voodla, A., Uusberg, A., & Desender, K. (2025). Metacognitive confidence and affect – two sides of the same coin? *Cognition & Emotion*, 39(8), 1857–1874. https://doi.org/10.1080/02699931.2025.2451795
- Vrantsidis, T. H., Voodla, A., & Sabbagh, K. (2025). Reward prediction errors, not expectations or outcomes, drive emotional valence. *OSF Preprints* (v1). https://doi.org/10.31219/osf.io/upjw4_v1
