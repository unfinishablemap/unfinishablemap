---
title: "Research Notes - Common versus Stimulus-Specific Neural Coding of Negative Affect, and Mixed-Valence States"
created: 2026-11-25
modified: 2026-11-25
human_modified: null
ai_modified: 2026-11-25T22:44:28+00:00
draft: false
description: "Čeko et al. 2022 read in full, Vaccaro et al. 2024 via its preprint, and the mixed-feelings debate, graded against the single-scalar-currency claim. One fold into valence-as-a-natural-kind."
topics:
  - "[[valence-as-a-natural-kind]]"
  - "[[valence-and-conscious-selection]]"
concepts:
  - "[[valence]]"
  - "[[evaluative-phenomenal-character]]"
related_articles:
  - "[[tenets]]"
  - "[[positions/value-in-selection]]"
  - "[[attitudinal-and-hybrid-theories-of-pleasure-and-unpleasantness-2026-11-25]]"
  - "[[constructed-emotion-and-valence-as-a-natural-kind-2026-09-05]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-25
last_curated: null
recommended_action: fold
target_section: topics
target_slug: valence-as-a-natural-kind
---

# Research: Common versus stimulus-specific neural coding of negative affect, and mixed-valence states

**Date**: 2026-11-25
**Verdict**: `fold` into `topics/valence-as-a-natural-kind`, as one new paragraph in "What Fragmentation Actually Costs" (`{#the-asymmetry}`), directly after the Kron and Lindquist paragraph. Budget **+304 words** by `count_words` (206 body, 98 for four reference entries; measured on the fenced blocks below at 22:46Z). The exact text is in [Fold plan](#fold-plan). `concepts/valence` needs **no change**: its L41 sentence already links the host at the point where its L39 says the scalar question "is disputed below". Topics and concepts are both at 370/370 (`count_section_files`, 22:44Z), so `article` could not be placed. A standalone page would not be warranted even with a free slot, because the material is evidence for an argument the host already runs.

**Search and retrieval used**: PubMed `efetch` (abstracts for PMIDs 35637370, 33349547, 38566509); PMC idconv and `efetch db=pmc` (Lee et al. 2024, PMC11194486, full text); OpenAlex `works/doi:` (abstracts rebuilt from the inverted index) and `filter=cites:` (citing-work screens for Čeko, 122 works, and Vaccaro, 22 works, titles screened); Unpaywall; the bioRxiv API and the JATS source XML of the Vaccaro preprint; Crossref (Larsen 2017 abstract); Semantic Scholar Graph API; the Wayback availability API; `curl` and `pdftotext` on the CoCoAN-lab copy of Čeko et al. and an author-site copy of Cowen and Keltner. WebSearch calls: "Čeko 2022 'common and stimulus-type-specific' negative affect replication OR critique OR follow-up neural signature"; "Vaccaro Kaplan mixed valence feelings fMRI bittersweet bioRxiv preprint full text". One web-fetch subagent call for Bonard et al. (2026) failed at Springer's sign-in redirect. No browser.

## Verification key

- **VERIFIED**: the quoted span was matched by script (whitespace collapsed, ligatures normalised, the PDF's running headers "Articles" and "NATurE NEuroSCiEnCE" removed where they interrupt a sentence, and citation superscripts such as "value6,7" dropped) against the raw text named in the entry. Every quotation in this note was checked this way at 22:45Z. The only spans that did not match are the search-query strings, titles given in sentence case, and phrases quoted from the proposed passage itself.
- **VERIFIED (abstract)**: matched against the abstract only (PubMed text, OpenAlex inverted index, or Crossref JATS abstract). The body was not read.
- **via X**: taken from source X's report and not checked in the original.
- **LEAD**: not read. Do not cite on this note's authority.

## Executive Summary

Čeko, Kragel, Woo, López-Solà and Wager (2022, read in full) had 55 people rate four kinds of aversive stimulus (mechanical pain, thermal pain, aversive sounds, aversive images) on one common scale. They fitted, jointly, a *common* brain model and four *stimulus-type-specific* models of those ratings. The common model predicted every type. The specific models, largely in early sensory pathways, predicted their own type and not the others. Ratings drew on the two kinds of model "in approximately equal parts", and the authors conclude that negative affective experience "is not completely reducible to a common dimension such as valence." Vaccaro et al. (2024; abstract verified, preprint read in full) found that self-reported mixed (bittersweet) states had consistent neural patterns in anterior cingulate and ventromedial prefrontal cortex but not in the insula. The behavioural case that people feel happy and sad at once (Larsen and McGraw) is strong but contested: Russell (2017) keeps core affect bipolar and moves the mixture into "cold" judgments about a situation's aspects, and Larsen (2017) allows that the competing hypotheses "may not be entirely falsifiable."

What these do to the single-scalar-currency claim:

1. **The common component fits a shared evaluative dimension** (compatible). It joins Chikazoe's supramodal code, which the host already cites. Under the selection fork's own crux, which requires felt currency to be a variable distinct from the computed one, a neural common component is equally what the value-blind rival's *computed* currency predicts. So it cannot favour the Map's felt currency over that rival.
2. **The specific components do not, by themselves, show several felt magnitudes** (compatible with both readings, so not discriminating). The design supplied one rating scale. What it found is that one reported quantity has plural neural predictors, which is the degeneracy the host's cluster reading already absorbs. A reading on which the scale commensurated several felt qualities is equally consistent with the data, and the design cannot test it. This is the mirror of the host's Occam point: one measurement scale is not one felt quantity, and plural predictors of one scale are not plural felt qualities.
3. **Mixed states press harder, but only on one *bipolar* felt magnitude** (suggestive). A state felt as good and bad at once is no point on one bipolar scale. Russell's hot/cold reply and Larsen's falsifiability concession keep this from being discriminating. None of the studies concerns choice. So even on the "hot" reading, mixed states give at most the first half of the host's withdrawal condition (felt valence is not one value), observed outside choice, and say nothing about the second half (a commensurating scalar formed only at choice).

The host's grade stands, and so does `concepts/valence`'s ("Whether that is one bipolar scale, let alone one felt magnitude … is disputed").

## Assessment: is the subject worth covering?

Yes, as one paragraph. Three outer reviewers on 2026-11-25 flagged the "common evaluative dimension" language on `concepts/valence`, and the corpus had zero hits for Čeko and Vaccaro (synthesis count, re-checked by grep of `obsidian/` at 22:45Z: outside `workflow/` and `reviews/`, the only hit is this note). Cowen and Keltner (2021) is on no content page either: `voids/affective-void` cites their 2017 *PNAS* paper, which is a different work. The host already grades the bipolar-versus-unipolar measurement record (Kron; Lindquist). It has no within-subject neural test of common versus specific coding, and no mention of mixed feelings, which are the most direct empirical pressure on a *bipolar* felt scalar. The fold fills both gaps without changing the host's verdict.

The Gemini review (2026-11-25) that seeded the harvest characterises Čeko et al. in ways the full text partly supports and partly does not. "N = 55 in training" and "401" new participants are VERIFIED. The claim that specific codes "outperform generalized negative affect for aversive sounds and images" holds by within-participant *r* for both types (sounds 0.38 vs 0.31; images 0.64 vs 0.49). It does not hold for sounds by *unique variance*, where the common model's share is larger (34% vs 29%). Do not repeat "outperform".

## Key Sources

### Čeko, Kragel, Woo, López-Solà & Wager (2022), "Common and stimulus-type-specific brain representations of negative affect" (read in full)

- **URL**: https://doi.org/10.1038/s41593-022-01082-w (read: https://cocoanlab.github.io/pdfs/Ceko2022.pdf, an author-lab copy of the published article with *Nature Neuroscience* running heads; also at https://sites.dartmouth.edu/canlab/files/2021/03/2022_Ceko_NatNeuro.pdf, not fetched)
- **Type**: Empirical paper (fMRI, partial least squares regression, external validation)
- **Design** (VERIFIED): study 1, "N = 55 participants (24 females)"; four aversive types at four intensity levels each, plus pleasant images as a positive control. "Negative affect induced by these stimuli was measured on a uniform scale across stimulus types, allowing direct comparisons across sensory inputs despite variation in stimulus properties." Models were tested in "401 new participants from different cohorts" (studies 2–6).
- **Key points**:
  - Abstract (VERIFIED (abstract), PubMed): "Stimulus-type-specific negative affect was largely encoded in early sensory pathways, whereas generalized negative affect was encoded in a distributed set of midline, forebrain, insular and somatosensory regions." "Common and stimulus-type-specific models were jointly important for predicting subjective experience."
  - VERIFIED: "Negative affect ratings of all types were predicted by a mixture of common and stimulus-type-specific representations in approximately equal parts (mechanical: 33% common, 34% specific; thermal: 31% common, 23% specific; auditory: 34% common, 29% specific; visual: 21% common, 32%, specific)". Shared variance: mechanical 10%, thermal 32%, auditory 5%, visual 25%. These are study-1, cross-validated, within-participant variance shares.
  - VERIFIED, the authors' inference: "these results show that negative affective experience is not completely reducible to a common dimension such as valence."
  - VERIFIED: "No region encoded negative affect in a purely domain-general fashion."
  - VERIFIED, the framing ties the study to the currency question: "Neuroeconomic theories postulate a ‘common currency’ for value, whereby signals from diverse reinforcers are integrated into a common representation that shapes decision-making and behavior."
  - VERIFIED, on bipolarity: the models' "response patterns, and the double dissociation observed between negative and positive affective images, are also inconsistent with bipolar (single-dimension) encoding but consistent with the idea that negative and positive affect are encoded in separable systems". Limitation, VERIFIED: "we only included one type of positive stimuli (visual images)".
  - Generalisation, VERIFIED: across "55 model generalization tests (5 models × 11 tests), the models’ decisions were correct ... in 49 cases." The common model did not predict the "knife on bottle" sound in study 3 (r = 0.13, P = 0.39), and neither the auditory nor the common model predicted the context-driven emotional sounds.
  - Open question the authors flag, VERIFIED: "whether common and type-specific affective codes are parallel or hierarchical". This is the question that would bear on whether a common code is an integration of specific ones.
- **Tenet alignment**: Neutral on Dualism. The paper is a physicalist predictive-modelling study, and its closing claim is to "offer an integrated account of how negative affect is constructed in the brain" (VERIFIED (abstract)). Do not conscript it. On P-VS1, compatible: see the Executive Summary, points 1–2.

### Vaccaro, Wu, Iyer, Shakthivel, Christie, Damasio & Kaplan (2024), "Neural patterns associated with mixed valence feelings differ in consistency and predictability throughout the brain" (abstract verified; preprint read in full)

- **URL**: https://doi.org/10.1093/cercor/bhae122 (published text not obtained: academic.oup.com returned 403). Preprint read: bioRxiv 10.1101/2023.11.22.568316 v1, JATS source XML from https://www.biorxiv.org/content/early/2023/11/23/2023.11.22.568316.source.xml (the PDF route returned a Cloudflare 1015).
- **Type**: Empirical paper (fMRI during a naturalistic film, hidden Markov models, pattern consistency)
- **Key points**:
  - VERIFIED (abstract), published version: "We used functional magnetic resonance imaging (fMRI) to scan 27 subjects watching an animated short film chosen to induce bittersweet mixed feelings." "The insula had unique and consistent neural signatures for univalent states, but not for mixed valence states. The anterior cingulate and ventral medial prefrontal cortex had consistent neural signatures for both univalent and mixed states."
  - VERIFIED (preprint): the self-report was retrospective: "subjects re-watched the video and performed a feeling annotation task", pressing on/off buttons for "Positive", "Negative" and "Mixed". The labels are categorical, with no intensity.
  - VERIFIED (preprint), on the insula: "The key deviation from our hypotheses was the finding that the insular cortex had consistent neural signatures for both positive and negative states, but not for mixed ones." Their 2020 model had predicted insular integration.
  - VERIFIED (preprint), a guard against over-reading: the posterior cingulate result leaves "room for the potential argument that the stability of the mixed feeling state is mostly driven by the component negativity".
  - VERIFIED (preprint): "The hypotheses related to whether the psychology of mixed feelings involves vacillation or a stable mixed state may never be fully falsifiable" (citing Larsen 2017). This sentence was **not** checked in the published text. Cite the concession to Larsen (2017), whose abstract carries it.
  - VERIFIED (preprint): the paper's own placement of constructionism: "In the constructionist approach, bipolar valence is an irreducible dimension of affect and consequently, positivity and negativity cannot simultaneously occur" (citing Russell 2017; Larsen 2017; Barrett & Bliss-Moreau 2009, already on the host).
- **Press-report caution**: the BPS Research Digest (Barratt, 4 July 2024) says that "Mixed feelings were associated with specific patterns of activity in the amygdala and nucleus accumbens". The preprint says the accumbens predicted *transitions* "despite the differently valenced states not being neurally consistent" there. Do not repeat the press version.
- **Tenet alignment**: Neutral on Dualism (Damasio's framework is physicalist and interoceptive; do not conscript). It bears on the bipolar-scalar reading: see the Executive Summary, point 3.

### Larsen & McGraw (2011), "Further evidence for mixed emotions" (abstract verified)

- **URL**: https://doi.org/10.1037/a0021846 (OA copy listed at SSRN, not read)
- **Key points**, VERIFIED (abstract): the authors tested the vacillation explanation "by asking subjects to complete online continuous measures of happiness and sadness. Subjects reported more simultaneously mixed emotions during a bittersweet film clip than during a control clip." Open-ended measures gave the same pattern, "even when subjects were told that they were not expected to report mixed emotions". Their conclusion: "positivity and negativity are separable in experience."
- Precursors, VERIFIED (abstract): Larsen, McGraw & Cacioppo (2001): "although affective experience may typically be bipolar, the underlying processes, and occasionally the resulting experience of emotion, are better characterized as bivariate." Larsen & McGraw (2014) review the "neutralize" alternative: "some have suggested that bittersweet events' pleasant aspects might neutralize their unpleasant aspects". That is a felt-netting hypothesis, and they argue against it.
- **Not in the fold** (budget): the passage cites Vaccaro for the evidence and Larsen (2017) for the concession. If headroom allows, add Larsen & McGraw (2011) as the behavioural citation (+about 24 words with its reference).

### Larsen (2017), "Holes in the case for mixed emotions" (abstract verified)

- **URL**: https://doi.org/10.1177/1754073916639662
- VERIFIED (abstract, Crossref): "Considerable evidence that happiness and sadness can co-occur has accumulated in the past 15 years, but holes in the case remain. ... I also explore the possibility that the case may never be closed, in part because the competing hypotheses may not be entirely falsifiable."

### Russell (2017), "Mixed emotions viewed from the psychological constructionist perspective" (abstract verified)

- **URL**: https://doi.org/10.1177/1754073916639658
- VERIFIED (abstract): "Feeling bad is one thing, judging something to be bad another. This hot/cold distinction helps resolve the debate between bipolar and bivariate accounts of affect." "Core affect is described by a bipolar valence dimension in which feeling good precludes simultaneously feeling bad and vice versa. Judgments of affective quality of opposite valence can occur simultaneously because the stimulus situation has many aspects." Meta-experience "can, but rarely does, embrace simultaneous emotion categories of opposite valence."
- **Tenet alignment**: Russell's reply preserves one bipolar *felt* magnitude (core affect). It is therefore the reading of mixed feelings most favourable to a single felt scalar, offered by a constructionist. The Map may note that, but should not present Russell as supporting the currency claim.

### Cowen & Keltner (2021), "Semantic space theory: a computational approach to emotion" (read in full)

- **URL**: https://doi.org/10.1016/j.tics.2020.11.004 (read: https://emotion.wisc.edu/wp-content/uploads/sites/1353/2026/03/Cowen-and-Keltner-2021.pdf, which is the journal's pre-pagination proof: "TICS 2110 No. of Pages 13", "Month 2020, Vol. xx")
- VERIFIED (abstract, PubMed): "Upwards of 25 distinct varieties of emotional experience have distinct profiles of associated antecedents and expressions. These emotions are high-dimensional, categorical, and often blended. This approach also reveals that specific emotions, more than valence, organize emotional experience, expression, and neural processing."
- VERIFIED (body): "From these specific states, people infer valence, arousal, and eliciting appraisals in a more culture-specific manner". The Basic 6 and valence/arousal models "each" capture "around 30% of the systematic variance in judgments of a wide range of emotion categories", so studies using them "capture only about 30% of the systematic varianc[e]". The Gemini review's "about 30%" is therefore VERIFIED, but it concerns variance in *judgments of emotion categories*, not any test of a felt currency. Neural claim (body): "specific emotions explained greater variability in brain activity than affective dimensions in every cortical and subcortical region of the brain". That is their summary of Horikawa et al. (2020); VERIFIED (abstract) there: "emotion categories better predicted cortical and subcortical responses than affective dimensions". Horikawa's sample size was not checked.
- **Not in the fold.** It bears mainly on the host's first question (categories), and on whether valence is *primary*. It is the reverse of constructionism: categories first, valence inferred. See Observations outside the fold.

### Context sources (abstracts or partial reads; not in the fold)

- **Chang, Gianaros, Manuck, Krishnan & Wager (2015)**, *PLoS Biology* 13(6), e1002180. VERIFIED (abstract): a picture-induced negative-affect signature "was unresponsive to physical pain (emotion-pain = 92% discriminative accuracy)". This is the same lab's earlier evidence for stimulus-specific negative affect.
- **Lee, Lee, Han, Choi, Wager & Woo (2024)**, *PNAS* 121(25), e2310433121 (PMC full text; cites Čeko). VERIFIED: participants "continuously rated their subjective pleasantness and unpleasantness" during oral capsaicin (pain) and chocolate (pleasure). A valence model was defined to "predict both pain and pleasure ratings in relation to the ratings’ directional signs" and generalised to an independent sample (n = 62). The authors write: "Our findings support the existence of the modality-general affective coding in the brain". Limitation, VERIFIED: "their effect sizes were small to medium". This decodes one *signed* axis across pleasure and pain, against Čeko's "inconsistent with bipolar" finding for images. As with Čeko, the design supplied the scale (here a signed one). The neural bipolarity record is design-dependent, which is Kron's measurement point one level down.
- **Berrios, Totterdell & Kellett (2015)**, *Frontiers in Psychology* 6, 428. VERIFIED (abstract): a meta-analysis of "63 experimental studies"; "moderate to high effect size for the elicitation of mixed emotions (d IG+ = 0.77)"; "Studies using the minimum index ... resulted in smaller effect sizes, whereas subjective measures of mixed emotions increased the effect sizes"; the authors conclude that "mixed emotions are a robust, measurable and non-artifactual experience."
- **Cacioppo & Berntson (1994)**, *Psychological Bulletin* 115(3), 401–423. VERIFIED (abstract): "this bipolar dimension is insufficient to portray comprehensively positive and negative evaluative processes and that the question is not whether such processes are reciprocally activated but under what conditions". This is the evaluative space model. The processing notes on the Claude outer review of 2026-11-25 confirmed its metadata at Crossref.
- **Vaccaro, Kaplan & Damasio (2020)**, *Perspectives on Psychological Science* 15(5), 1187–1199. VERIFIED (abstract): it hypothesises "rapid vacillation and simultaneity of positive and negative affect, albeit at different neurobiological levels", with insular processing letting "separate emotional events to be experienced as one 'mixed' and integrated feeling." The 2024 insula result went against that hypothesis.
- **Sun, Jiang, Yin, Li & Chang (2025)**, *Communications Biology* 8, 1455 (EEG, pun-humour). VERIFIED (abstract): "negativity was experienced first, whereas amusement was subsequently felt within a brief period, during which negativity was not offset". LEAD for anything beyond the abstract.
- **Lee, Han, Oh & Cha (2025)**, *Communications Psychology* 3, 123 (EEG, VR awe, N = 43). VERIFIED (abstract): "ambivalent feelings were represented as spatially distinct from positive and negative ones". LEAD beyond the abstract.
- **Kwon et al. (2026)**, *Nature Communications* 17, 5186 (insula mega-analysis, n = 540, co-authors include Wager, Barrett, Čeko's co-author López-Solà). VERIFIED (abstract): "a hierarchical architecture, with a multi-domain convergence zone in bilateral dorsal anterior insula surrounded by progressively converging zones". This bears on Čeko's parallel-or-hierarchical question. LEAD beyond the abstract.
- **Bonard, Dukes & Sander (2026)**, "Valence, mixed feelings, and appraisal processes", *Topoi*, https://doi.org/10.1007/s11245-026-10484-5. **LEAD.** It is CC-BY open access, but Springer returned a bot-challenge page to `curl` and a sign-in redirect to WebFetch, and Wayback has no snapshot. OpenAlex's "abstract" is the opening paragraph, which cites Berrios, Larsen, Vaccaro and others. Sander co-authored "Levels of valence" (Shuman, Sander & Scherer 2013, already on the host), so this paper probably applies the micro/macro-valence framework to mixed feelings. That would bear directly on the host's currency paragraph. **This is the highest-value unread item. Read it before any further edit to the host's Scherer paragraph.**
- **Kragel, Treadway, Admon, Pizzagalli & Hahn (2023)**, "A mesocorticolimbic signature of pleasure in the human brain", *Nature Human Behaviour* 7(8), 1332–1343. LEAD (no abstract in OpenAlex). It is the positive-affect counterpart to Čeko.

No direct reply to, critique of, or replication of Čeko et al. was found. WebSearch returned none. The OpenAlex cites-screen of 122 citing works (titles) shows follow-ups that build signatures (pleasure, disgust, threat, arousal, the insula), not challenges.

## Major Positions

### Common-currency coding (neuroeconomic and core-affect views)
- **Proponents** (as characterised by Čeko et al.): neuroeconomic "common currency" theories; core-affect dimensional models (Russell; Barrett).
- **Core claim**: diverse reinforcers converge on a shared representation of value or valence.
- **Evidence for**: Chikazoe et al. (2014, on the host); Čeko's common model; Lee et al. (2024).
- **Relation to site tenets**: compatible with a shared dimension. By the fork's crux, a neural common code is equally the computed currency of the value-blind rival. It is therefore not evidence for a *felt* currency.

### Stimulus-specific or category-first coding
- **Proponents**: Čeko et al. (jointly with common coding); Chang et al. (2015); Cowen & Keltner (category-first; valence inferred).
- **Core claim**: part of what predicts felt aversiveness is carried in type-specific, largely sensory pathways (Čeko). Or, more strongly, specific emotions organise experience and valence is derived (Cowen & Keltner).
- **Relation to site tenets**: costs the identity claim (P-VS3) nothing, since it can hold distributively, as the host argues. Čeko does not discriminate on one felt magnitude, because the design supplied the scale. Cowen & Keltner press harder on valence's *primacy* than on the currency.

### Bivariate felt valence (evaluative space model)
- **Proponents**: Cacioppo & Berntson; Larsen, McGraw; Berrios et al.; Vaccaro et al.
- **Core claim**: positivity and negativity are separable in experience and can co-occur.
- **Relation to site tenets**: suggestive against a single *bipolar* felt scalar. A bivariate felt state still allows a felt net (two unipolar magnitudes plus an on-balance feeling), so it does not refute a felt currency. It only removes the assumption that the currency is the bipolar scale itself.

### Bipolar core affect with cold mixture (Russell 2017)
- **Core claim**: hot core affect is bipolar; mixed reports are cold judgments of a situation's several aspects, or rare meta-experience.
- **Relation to site tenets**: this is the reading of mixed feelings that best preserves one felt magnitude. It is the reason the mixed-feelings record is suggestive rather than discriminating.

## Key Debates

### Vacillation versus simultaneity versus cold judgment
- **Sides**: Larsen & McGraw (simultaneous, from continuous measures); Russell (cold judgment); Vaccaro et al. 2020 (both, at different levels); Vaccaro et al. 2024 (consistent states in ACC/vmPFC, not insula).
- **Core disagreement**: whether a self-report of "happy and sad" picks out one felt state with two signs, rapid alternation, or a hot state plus a cold appraisal.
- **Current state**: open. Larsen (2017) and Vaccaro et al. (2024 preprint) both say it may never be fully falsifiable. Neural consistency in vmPFC and ACC does not separate the hot and cold readings, because both regions are integration and conflict regions on the authors' own account.

### Is a common neural component a common currency?
- **Sides**: Čeko et al. frame the question in neuroeconomic common-currency terms and answer "partly".
- **Map-specific point**: the selection fork requires the felt currency to be distinct from the computed one. Neural evidence about a common component therefore bears on the computed currency, and reaches the felt one only through a bridge premise the Map does not have.

## Bearing on the single-scalar-currency claim (graded)

| Finding | What it bears on | Grade |
|---|---|---|
| Čeko common model, cross-type and cross-cohort | a shared evaluative dimension (implementation level) | compatible |
| Čeko specific models, "approximately equal parts" | one felt magnitude | compatible with both readings (design supplied the scale): non-discriminating |
| Čeko "inconsistent with bipolar (single-dimension) encoding" (images only) vs. Lee et al. signed axis across pleasure and pain | one *bipolar* neural scale | mixed, design-dependent: non-discriminating |
| Mixed feelings (Larsen & McGraw; Berrios; Vaccaro 2024) | one *bipolar* felt magnitude | suggestive against, with Russell's hot/cold reply open |
| Mixed feelings, any reading | P-VS1's felt currency at choice | non-discriminating: no choice in any study; at most the first half of the host's withdrawal condition |
| Cowen & Keltner, category-first | valence's primacy, not the currency directly | suggestive against valence as the organising dimension of report; silent on a felt net at choice |

Keep `concepts/valence`'s sentence as it stands: "Whether that is one bipolar scale, let alone one felt magnitude making incommensurable states comparable, is disputed below". These results put the "one bipolar scale" clause under more pressure than the "one felt magnitude" clause, which matches the sentence's own ordering.

## Fold plan {#fold-plan}

**Host**: `topics/valence-as-a-natural-kind`. **Measured** by `tools.curate.length.analyze_length` at 22:33Z (driver, and this run): 3396 words, topics hard 4000, gate `>=`, headroom **603** (4000 − 1 − 3396). After this fold the page is about 3700, leaving about 299. **Re-measure before and after.**

**Placement**: a new paragraph immediately **after** the paragraph that ends "exactly as reading one missing module as no kind does." (that string occurs once on the live page, checked 22:4xZ), and immediately **before** the paragraph that begins "The condition under which the currency premise would have to be withdrawn" (that string also occurs once). Both are in "What Fragmentation Actually Costs" `{#the-asymmetry}`. Do not touch "The Attitudinal Alternative" `{#attitudinal}`.

**Passage (206 words by `count_words`; every quotation VERIFIED above)**:

```markdown
Marta Čeko and colleagues had participants rate mechanical pain, thermal pain, aversive sounds and aversive images on one scale. Every type's ratings were predicted by a generalized brain pattern and by stimulus-type-specific ones, largely in early sensory pathways, "in approximately equal parts"; the authors conclude that negative affective experience "is not completely reducible to a common dimension such as valence." The common component fits a shared evaluative dimension. The specific ones give one rated quantity plural neural predictors, degeneracy the cluster reading absorbs; they would show several felt qualities only if the scale had commensurated them, which a design supplying the scale cannot test. Mixed feelings press harder. Anthony Vaccaro and colleagues found consistent anterior cingulate and ventromedial prefrontal patterns, though not insular ones, for self-reported mixed states. A state felt as good and bad at once is no point on one bipolar scale, and is the simplest plural felt state the withdrawal condition below needs at choice, though observed outside it. James Russell keeps core affect bipolar, assigning the mixture to judgments of a situation's aspects, and Jeff Larsen, defending co-occurrence, allows the rival hypotheses "may not be entirely falsifiable". Suggestive against a bipolar felt scalar, the record does not discriminate on the currency premise.
```

**References to add (98 words; the host's list is alphabetical)**:

```markdown
1. Čeko, M., Kragel, P. A., Woo, C.-W., López-Solà, M., & Wager, T. D. (2022). Common and stimulus-type-specific brain representations of negative affect. *Nature Neuroscience*, 25(6), 760–770. https://doi.org/10.1038/s41593-022-01082-w
1. Larsen, J. T. (2017). Holes in the case for mixed emotions. *Emotion Review*, 9(2), 118–123. https://doi.org/10.1177/1754073916639662
1. Russell, J. A. (2017). Mixed emotions viewed from the psychological constructionist perspective. *Emotion Review*, 9(2), 111–117. https://doi.org/10.1177/1754073916639658
1. Vaccaro, A. G., Wu, H., Iyer, R., Shakthivel, S., Christie, N. C., Damasio, A., & Kaplan, J. (2024). Neural patterns associated with mixed valence feelings differ in consistency and predictability throughout the brain. *Cerebral Cortex*, 34(4), bhae122. https://doi.org/10.1093/cercor/bhae122
```

Positions in the list: Čeko after Carruthers (2018) and before Chikazoe (2014); Larsen (2017) after Labukt (2012) and before Lindquist (2016); Russell (2017) after Russell (2003) and before Russell & Barrett (1999), because a single-author entry precedes a co-authored one; Vaccaro after Tye (2018) and before Walle & Dukes (2023).

**Writer checks**:
1. "the withdrawal condition below" must point to the very next paragraph ("The condition under which the currency premise would have to be withdrawn is therefore statable ..."). That paragraph's "therefore" now follows two paragraphs of evidence rather than one. It still reads, but deleting "therefore" (−1) is optional.
2. "degeneracy the cluster reading absorbs" leans on the cluster-section paragraph that begins "Neural degeneracy is compatible with a psychological-level kind". Re-grep it. If a sibling edit has removed it, write "neural degeneracy" in place of "degeneracy the cluster reading absorbs" (−3).
3. Do not say Čeko's specific models encode "sensory" rather than affective content. They predicted negative-affect *ratings* and were valence-specific (no response to positive images or to non-painful warmth). Do not repeat the Gemini review's "outperform" (see Assessment).
4. Vaccaro: do not attribute amygdala or nucleus accumbens *mixed-state* signatures to the paper (that is the BPS digest's error). The self-reports were retrospective, from a re-watch, with categorical labels, n = 27 and one film. If words are spare, "retrospectively self-reported" (+1) is the most informative addition.
5. Do not cite Vaccaro for the falsifiability concession. That sentence was verified only in the bioRxiv preprint. The passage gives it to Larsen (2017), where it is verified in the published abstract.
6. Russell: paraphrase at abstract depth only. Do not add claims about meta-experience or the body of the paper.
7. Conscript no authors. Čeko et al., Vaccaro/Damasio and Russell are all physicalist or constructionist. The passage reports their findings and grades the bearing in the Map's voice.
8. Under the append-only-if-absent rule, `ai_system` already contains `claude-opus-5-5`. Append the fork's actual model only if it is absent anywhere in the string.

**Optional variants (only if headroom allows after re-measuring)**:
- **B (−4)**: drop "though not insular ones," to reach 300 in total.
- **C (+about 40, two sentences plus one reference)**: after "The common component fits a shared evaluative dimension.", add the bipolarity split: *Their negative-versus-positive image dissociation is, they add, "inconsistent with bipolar (single-dimension) encoding", while a pleasure-and-pain study from overlapping labs decoded one signed axis; each design supplied its scale.* Reference: Lee, S. A., Lee, J.-J., Han, J., Choi, M., Wager, T. D., & Woo, C.-W. (2024). Brain representations of affective valence and intensity in sustained pleasure and pain. *PNAS*, 121(25), e2310433121. https://doi.org/10.1073/pnas.2310433121. Take both halves or neither: Čeko's bipolarity line without Lee would be one-sided against the host's existing "neither a bipolar nor a bivalent organisation" sentence.

**`concepts/valence`**: **no change** (0 words), leaving its ~220 headroom to the two open P3s (L91 and the Variant C fold). Its L39 says the scalar question "is disputed below". Its L41 links `[[topics/valence-as-a-natural-kind|Valence as a natural kind]]` with the gloss "finds the Map's exposure falling on the claim that felt valence is a single scalar currency rather than on its reality". That gloss stays accurate after the fold, so no label fix is needed.

**After the edit**: run `/check-links`. This fold adds no anchors and no new wikilinks.

## Observations outside the fold

None of these is to be added under the fold.

- **Cowen & Keltner versus the host's lead.** The host's opening relies on constructionism supplying valence as a felt primitive. Semantic space theory attacks from the other side: categories are primary and valence is "infer[red]" from them "in a more culture-specific manner". If that holds for felt valence, and not only for valence *attributions*, it presses on valence's primacy. It does so without touching the distributive identity claim. A future pass on "The Two Questions" could note it in one sentence. Its evidence is judgment variance and video-fMRI, and it never tests a felt net at choice.
- **Bonard, Dukes & Sander (2026)** is the next read for the host's Scherer paragraph (micro- and macro-valence). It is the one item here that may bear directly on "a currency manufactured at the point of selection".
- **The parallel-or-hierarchical question.** Čeko's open question, together with Kwon et al.'s (2026) hierarchical insular convergence, is the empirical form of the host's withdrawal condition at the neural level: are common codes integrations of specific ones? A hierarchical answer would still be neural integration, not a felt scalar formed after the fact. It belongs with `topics/valence-and-conscious-selection` if that page ever lists implementation-level tests.
- **`topics/valence-and-conscious-selection`.** Mixed anticipatory feelings at choice (ambivalence, bittersweet decisions) are the one place where the mixed-feelings literature could become discriminating for P-VS1. No study found here measures them. It is a candidate gap for that page's test list.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1994 | Cacioppo & Berntson, evaluative space model | positive and negative evaluative processes separable; bipolar scale "insufficient" |
| 1999 | Russell & Barrett, core affect | bipolar valence as a dimension of core affect (on the host) |
| 2001 | Larsen, McGraw & Cacioppo | happy and sad co-reported after bittersweet events |
| 2011 | Larsen & McGraw, continuous measures | simultaneity, not vacillation, on online ratings |
| 2014 | Chikazoe et al. | supramodal OFC valence code (on the host) |
| 2015 | Chang et al., PINES | negative-affect signature unresponsive to pain |
| 2015 | Berrios et al. meta-analysis | 63 studies; mixed emotions "robust, measurable and non-artifactual" |
| 2016 | Lindquist et al. meta-analysis | neither bipolar nor bivalent at fMRI resolution (on the host) |
| 2017 | Russell; Larsen (*Emotion Review* special section) | hot/cold reply; falsifiability concession |
| 2020 | Vaccaro, Kaplan & Damasio | vacillation and simultaneity at different levels; insular integration hypothesised |
| 2021 | Cowen & Keltner, semantic space theory | categories over valence in experience, expression and neural processing |
| 2022 | Čeko et al. | common and stimulus-type-specific coding "in approximately equal parts" |
| 2024 | Vaccaro et al. | consistent mixed-state patterns in ACC/vmPFC, not insula |
| 2024 | Lee et al. | signed valence axis decoded across oral pleasure and pain |
| 2026 | Kwon et al.; Bonard, Dukes & Sander | hierarchical insular convergence; appraisal account of mixed feelings (LEAD) |

## Potential Article Angles

1. **The fold above** (recommended). Evidence for the host's existing grade, at one paragraph.
2. **If `topics/` gains a slot**: a page on "mixed feelings and the felt currency", arguing that ambivalence at choice is the one empirical setting where the single-scalar-currency premise could be tested, and saying what such a test would need (concurrent, not retrospective, report; choice; and a separate "on balance" measure). This is not recommended now. The Bonard et al. read should come first, and the material may fit `topics/valence-and-conscious-selection` instead.

When writing, follow `obsidian/project/writing-style.md`: front-load the grade, keep the Map's voice for the bearing and the authors' voice for their findings, and avoid the "This is not X. It is Y." construct.

## Gaps in Research

- Vaccaro et al. (2024), published text: not obtained (OUP 403). Body claims are from bioRxiv v1 (2023-11-23). The abstracts of the preprint and the published version agree on the insula, ACC and vmPFC results.
- Čeko et al. supplementary tables and extended data: not read.
- Bonard, Dukes & Sander (2026): LEAD, blocked.
- Kragel et al. (2023) pleasure signature: LEAD.
- Horikawa et al. (2020): abstract only; sample size unchecked.
- No published critique or replication of Čeko et al. was found. The screen was of OpenAlex citing-work titles only.
- Larsen & McGraw (2011): abstract only. The SSRN copy was not read.

## Citations

1. Berrios, R., Totterdell, P., & Kellett, S. (2015). Eliciting mixed emotions: a meta-analysis comparing models, types, and measures. *Frontiers in Psychology*, 6, 428. https://doi.org/10.3389/fpsyg.2015.00428 (abstract)
2. Bonard, C., Dukes, D., & Sander, D. (2026). Valence, mixed feelings, and appraisal processes. *Topoi*. https://doi.org/10.1007/s11245-026-10484-5 (LEAD)
3. Cacioppo, J. T., & Berntson, G. G. (1994). Relationship between attitudes and evaluative space: a critical review, with emphasis on the separability of positive and negative substrates. *Psychological Bulletin*, 115(3), 401–423. https://doi.org/10.1037/0033-2909.115.3.401 (abstract)
4. Čeko, M., Kragel, P. A., Woo, C.-W., López-Solà, M., & Wager, T. D. (2022). Common and stimulus-type-specific brain representations of negative affect. *Nature Neuroscience*, 25(6), 760–770. https://doi.org/10.1038/s41593-022-01082-w (read in full)
5. Chang, L. J., Gianaros, P. J., Manuck, S. B., Krishnan, A., & Wager, T. D. (2015). A sensitive and specific neural signature for picture-induced negative affect. *PLoS Biology*, 13(6), e1002180. https://doi.org/10.1371/journal.pbio.1002180 (abstract)
6. Cowen, A. S., & Keltner, D. (2021). Semantic space theory: a computational approach to emotion. *Trends in Cognitive Sciences*, 25(2), 124–136. https://doi.org/10.1016/j.tics.2020.11.004 (read in full, proof version)
7. Horikawa, T., Cowen, A. S., Keltner, D., & Kamitani, Y. (2020). The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions. *iScience*, 23(5), 101060. https://doi.org/10.1016/j.isci.2020.101060 (abstract)
8. Kragel, P. A., Treadway, M. T., Admon, R., Pizzagalli, D. A., & Hahn, E. C. (2023). A mesocorticolimbic signature of pleasure in the human brain. *Nature Human Behaviour*, 7(8), 1332–1343. https://doi.org/10.1038/s41562-023-01639-0 (LEAD)
9. Kwon, M., Bo, K., Botvinik-Nezer, R., Kragel, P. A., Van Oudenhove, L., Wager, T. D., et al. (2026). Convergent and selective representations of pain, appetitive processes, aversive processes, and cognitive control in the insula. *Nature Communications*, 17, 5186. https://doi.org/10.1038/s41467-026-71568-9 (abstract)
10. Larsen, J. T. (2017). Holes in the case for mixed emotions. *Emotion Review*, 9(2), 118–123. https://doi.org/10.1177/1754073916639662 (abstract)
11. Larsen, J. T., & McGraw, A. P. (2011). Further evidence for mixed emotions. *Journal of Personality and Social Psychology*, 100(6), 1095–1110. https://doi.org/10.1037/a0021846 (abstract)
12. Larsen, J. T., & McGraw, A. P. (2014). The case for mixed emotions. *Social and Personality Psychology Compass*, 8(6), 263–274. https://doi.org/10.1111/spc3.12108 (abstract)
13. Larsen, J. T., McGraw, A. P., & Cacioppo, J. T. (2001). Can people feel happy and sad at the same time? *Journal of Personality and Social Psychology*, 81(4), 684–696. https://doi.org/10.1037/0022-3514.81.4.684 (abstract)
14. Lee, J., Han, D. D., Oh, S.-Y., & Cha, J. (2025). Awe is characterized as an ambivalent affect in the human behavior and cortex. *Communications Psychology*, 3, 123. https://doi.org/10.1038/s44271-025-00299-2 (abstract)
15. Lee, S. A., Lee, J.-J., Han, J., Choi, M., Wager, T. D., & Woo, C.-W. (2024). Brain representations of affective valence and intensity in sustained pleasure and pain. *Proceedings of the National Academy of Sciences*, 121(25), e2310433121. https://doi.org/10.1073/pnas.2310433121 (PMC full text, PMC11194486)
16. Russell, J. A. (2017). Mixed emotions viewed from the psychological constructionist perspective. *Emotion Review*, 9(2), 111–117. https://doi.org/10.1177/1754073916639658 (abstract)
17. Sun, Y., Jiang, Z., Yin, X., Li, X., & Chang, R. (2025). Neural representation of mixed feelings during real-time processing of negative words in pun-humor. *Communications Biology*, 8, 1455. https://doi.org/10.1038/s42003-025-08857-4 (abstract)
18. Vaccaro, A. G., Kaplan, J. T., & Damasio, A. (2020). Bittersweet: the neuroscience of ambivalent affect. *Perspectives on Psychological Science*, 15(5), 1187–1199. https://doi.org/10.1177/1745691620927708 (abstract)
19. Vaccaro, A. G., Wu, H., Iyer, R., Shakthivel, S., Christie, N. C., Damasio, A., & Kaplan, J. (2024). Neural patterns associated with mixed valence feelings differ in consistency and predictability throughout the brain. *Cerebral Cortex*, 34(4), bhae122. https://doi.org/10.1093/cercor/bhae122 (abstract; body via bioRxiv preprint 10.1101/2023.11.22.568316 v1)
20. Barratt, E. (2024, 4 July). Mixed emotions may not be mixed after all. *BPS Research Digest*. https://www.bps.org.uk/research-digest/mixed-emotions-may-not-be-mixed-after-all (press report; contradicted on one point by the preprint)
