---
title: "Research Notes - Immediate Emotions and the Affect Heuristic in Choice"
created: 2026-10-22
modified: 2026-10-22
human_modified: null
ai_modified: 2026-10-22T11:51:16+00:00
draft: false
description: "Research notes on felt affect as an input to choice: immediate and integral emotions, risk-as-feelings, the affect heuristic and incidental carryover, with replications and nulls, read against P-VS1."
topics:
  - "[[the-steelman-for-value-blind-selection]]"
  - "[[valence-and-conscious-selection]]"
  - "[[wanting-liking-and-the-value-in-mechanism-fork]]"
concepts:
  - "[[affective-forecasting-gap]]"
  - "[[miswanting]]"
  - "[[somatic-interface]]"
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-22
last_curated: null
last_deep_review: null
recommended_action: article
target_section: topics
target_slug: immediate-emotions-and-the-affect-heuristic
---

# Research: Immediate Emotions and the Affect Heuristic in Choice

**Date**: 2026-10-22
**Target**: `topics/`, intended slug `immediate-emotions-and-the-affect-heuristic` (free per `check_slug.py`; topics at 357/370 by `count_section_files`, measured 10:04Z). Suggested title: "Immediate Emotions and the Affect Heuristic: Felt Affect as an Input to Choice".
**Originating finding**: the 2026-10-22 outer-review cycle (all three reviewers; see `reviews/outer-review-synthesis-2026-10-22`) found that [[positions/value-in-selection|P-VS1]]'s candidate currency, the *presently felt* valence of anticipating each option, had been argued without the decision-science literature that measures and manipulates felt affect as an input to choice. [[miswanting]]'s former claim that "no design measured felt anticipation at choice" was false because that literature uses other names.

**Search queries used** (field vocabulary, forward citation and known controversy, per the "Absence and Exclusivity Claims" rule in `project/writing-style.md`):
- Author/title lookups: Slovic Finucane Peters MacGregor "The affect heuristic" 2007; Loewenstein Lerner 2003 "role of affect in decision making"; Lerner Li Valdesolo Kassam 2015; Peters "functions of affect" "common currency"
- Field vocabulary: "integral emotions" "incidental emotions" appraisal tendency; experimentally manipulating integral anticipatory emotion at choice; immediate emotions manipulation risky decision
- Known controversy: replication "Heart strings and purse strings"; replication Rottenstreich Hsee 2001 affect-rich probability weighting; Lerner Keltner 2001 replication preregistered; affect heuristic Finucane 2000 time pressure replication; meta-analysis incidental emotion risk taking
- Forward citation: OpenAlex `cites:` lists for Schlösser et al. 2013 (W1786510013, 87 citing works) and Young et al. 2019 (W2888549006, 12 citing works), screened by title
- Crossref, OpenAlex (`abstract_inverted_index`), PMC and repository lookups by DOI for every item in the citation list

**Verification legend**. **[full text]**: raw text downloaded (PDF via `pdftotext`, PMC/publisher HTML), and every quotation marked **[verbatim]** was matched by grep against it. **[abstract only]**: abstract read as Crossref JATS or reconstructed from OpenAlex's inverted index; quotations are verbatim to that abstract. **[reused]**: verified earlier today by the fork that refined [[affective-forecasting-gap]] (refs 36–38), not re-verified here. **[metadata only]**: existence, authors, venue and pages confirmed at Crossref; contents not read. WebFetch and search-engine summaries were used only to locate sources and count for nothing.

## Verdict: Proceed, as a `topics/` Article

The subject justifies its own page, for four reasons.

1. **No page treats this literature as a whole.** Live-corpus counts made for this note: "affect heuristic" 0; Finucane, Pham, Lerner & Keltner, Pachur, Many Labs 2, Bartholomeyczik, Marini, Jäger 0 each. The vocabulary gap that produced miswanting's false absence claim is still open everywhere except two paragraphs.
2. **It adds far more than the three studies already in [[affective-forecasting-gap]].** That page and [[miswanting]] carry Schlösser et al. 2013, Young et al. 2019, Dorison et al. 2019, Loewenstein et al. 2001 and Davis et al. 2009. This note adds about twenty verified works. Four of them change what the Map can say:
   - a null for incidental emotion on incentivised risk-taking at n = 7,000, under a detailed pre-analysis plan (Dong et al. 2026);
   - a Many Labs 2 failure, in the opposite direction, of the flagship risk-as-feelings probability study (Klein et al. 2018 on Rottenstreich & Hsee 2001);
   - a preregistered meta-analysis showing that integral and incidental emotion are not interchangeable (Ferrer & Ellis 2021);
   - a registered replication of Lerner & Keltner 2001 that held for risk *judgment* but not for risk *preference* (Lu et al. 2026).
3. **A fold is infeasible on length.** Measured with `analyze_length` at 10:05Z: [[affective-forecasting-gap]] 3,789 words (`hard_warning`, over the 3,500 concepts hard threshold); [[miswanting]] 3,188 (312 below hard); [[somatic-interface]] 3,195; `positions/value-in-selection` 2,498 of 2,500 (2 words of headroom). The material needs about 1,500 words of prose.
4. **It is distinct from both neighbouring notes.**
   - [[research/anticipatory-feeling-and-time-preference-2026-10-05]] asks whether felt anticipation (savouring and dread) is hyperbolic *in delay*, and whether that yields preference reversal. This note does not touch delay. It asks what is known about felt affect *at the moment of choice* as an input: whether it was measured, whether it was manipulated, whether it is felt at all, and whether its valence or its appraisal content does the work.
   - [[affective-forecasting-gap]] and [[miswanting]] ask how accurate the forecast is and whether forecast error changes choice. This note asks whether the present feeling feeds choice at all.

## Executive Summary

Decision science has a large literature on felt affect as an input to choice. It goes by several names: **immediate** or **anticipatory** emotions, **integral** affect, **risk-as-feelings**, the **affect heuristic** and, for carried-over mood, **incidental** emotion. That literature establishes three things relevant to [[positions/value-in-selection|P-VS1]].

1. Option-directed affect measured just before choice predicts choice beyond anticipated emotions and subjective probability (Schlösser et al. 2013; Young et al. 2019; Grimani et al. 2024). It is measured, though, not manipulated, and it also tracks outcome value. In learning tasks, *expected* valence predicts choice better than *current* feeling does (Jäger et al. 2020, 2022).
2. Incidental affect carries over into valuation. Sadness raises choice prices, and that effect has been replicated (Lerner et al. 2004; Garg et al. 2018). Its effect on *risk preference* is weak or null in the best-powered tests:
   - Dong et al. 2026: n = 7,000, detailed pre-analysis plan, manipulation effective, no effect on risk-taking;
   - Marini 2023: only fear shows a small effect;
   - Lu et al. 2026: Lerner & Keltner's preference result did not replicate.

   Integral and incidental effects can also differ in direction (Ferrer & Ellis 2021).
3. Where affect matters, the operative variable is often appraisal content rather than valence. Same-valence emotions push in opposite directions (Lerner & Keltner 2001; Lerner et al. 2004; Bartholomeyczik et al. 2022). This bears on P-VS1's existing micro-valence shift condition.

Two further facts limit any dualist use of this literature. First, the field's "affect" is explicitly consciousness-neutral: Slovic et al. define it as experienced "with or without consciousness". Second, the regulation studies that come closest to manipulating integral affect at choice either measured arousal and set subjective feeling aside (Sokol-Hessner et al. 2009) or regulated *incidental* emotion (Heilman et al. 2010). The literature therefore fits P-VS1's candidate currency without evidencing it. It also supplies one result that cuts against a prediction the Map made in writing, explained below at [Bearing on the battery](#bearing-on-p-vs1-and-the-p-vs2-battery).

## Vocabulary Map: the Field's Names for Felt Affect at Choice

The article should carry a version of this table. It makes future absence searches possible and prevents a repeat of the miswanting error.

| Field term | Where defined (verified source) | Timing | Object | Felt? | Map construct |
|---|---|---|---|---|---|
| Anticipatory emotion | Loewenstein et al. 2001 | at decision | the risk or uncertainty | yes, by definition ("immediate visceral reactions") | P-VS1's candidate currency |
| Anticipated / expected emotion | Loewenstein et al. 2001; Loewenstein & Lerner 2003 (as reported by Jäger et al. 2020) | forecast of later | the outcome | a judgement, not necessarily felt now | predicted utility ([[affective-forecasting-gap]]) |
| Immediate emotion | Schlösser et al. 2013, after Loewenstein & Lerner 2003 | "at the cusp of making a decision" | a specific option | yes (self-report) | P-VS1's candidate currency |
| Integral affect | Peters 2006; Pham 2007; Young et al. 2019 | at decision | the stimulus or option itself | sometimes; see next row | P-VS1's currency *if felt* |
| Affect heuristic / "affect pool" | Slovic et al. 2002/2007; Finucane et al. 2000 | at judgement | the stimulus's affective tags | "with or without consciousness" | not by itself a felt currency |
| Incidental affect / carryover | Peters 2006; Pham 2007; Lerner et al. 2004 | prior and unrelated | misattributed to the option | yes (induced moods) | the "shift present affect" row ([[miswanting#misattribution]]) |
| Current affect / current valence | Jäger et al. 2020 ("Please rate how you are feeling now.") | before each choice | global, not option-directed | yes | closer to incidental mood than to P-VS1's input |
| Emotions-as-input / emotions-as-outcome | Davis, Love & Maddox 2009 | — | — | measured by skin conductance | the countermodel |
| Affect-rich / affect-poor outcomes | Rottenstreich & Hsee 2001; Pachur et al. 2014 | — | outcome type | inferred, not measured | a predicted signature of a felt input |
| Reducible emotion | Pfister & Böhm 2008 | at choice, as *belief* | consequences | "not as momentary feelings" | the cool route afg L76 says gives P-VS1 no input |
| Affect as "common currency" | Peters et al. 2006, after Cabanac 1992 | — | — | — | the Map's word "currency", already in the field |

## Key Sources

### A. The framing papers

#### Loewenstein, Weber, Hsee & Welch (2001), "Risk as feelings"
- **Citation**: *Psychological Bulletin*, 127(2), 267–286. https://doi.org/10.1037/0033-2909.127.2.267 **[full text]**. Two copies were used: an author-site scan from CMU with no text layer, read visually, and an OCR'd course-site copy (dl1.cuni.cz), against which the quotes below were grep-matched. OCR artefacts: em dashes appear as hyphens, and "risk-as-feelings" loses a hyphen at one line break.
- **Already on the Map**: [[affective-forecasting-gap]] ref 35 (anticipated vs anticipatory) and [[miswanting]] ref 17.
- **Key points**:
  - It names the received view the Map's dualism might want to enlist, though the word is used in a psychological sense **[verbatim]**: "Feelings triggered by the decision situation and imminent risky choice are seen as epiphenomenal-that is, not integral to the decision-making process." The scan has an em dash.
  - The definitions **[verbatim]**: "Anticipated emotions are typically not experienced in the immediate present but are expected to be experienced in the future." The anticipatory definition ("Anticipatory emotions are immediate visceral reactions (e.g., fear, anxiety, dread) to risks and uncertainties") straddles a page break in the OCR. The first part is grep-verified, and the final word "uncertainties" was confirmed visually on the scan, p. 267–268.
  - **The authors' own identification condition**, which matters most for the article **[verbatim]**: "If risk-related feelings and cognitive evaluations had identical determinants as well as consequences for behavior, the risk-asfeelings hypothesis would be little more than an alternative description of the psychological processes underlying decision making, and anticipatory feelings would not be required as an intervening construct." (The OCR drops the hyphen in "risk-as-feelings".) Feelings earn a place in the model only where their determinants diverge from cognitive evaluation. This is the field's version of the battery's middle row in [[affective-forecasting-gap]]: shift present affect while holding forecast and learned value fixed.
  - The divergence factors **[verbatim]**: "These include the vividness with which consequences can be imagined, personal exposure to or experience with outcomes, and past history of conditioning." Also: "feelings about risk are largely insensitive to changes in probability, whereas cognitive evaluations do take probability into account."
  - A methodological recommendation that the field partly followed **[verbatim]**: "those doing risk-related research should make it a routine practice to collect information on emotional reactions to risks, in addition to such traditional measures as probabilities and outcome values."
- **Tenet alignment**: neutral and naturalist. Its "epiphenomenal" means "not modelled as an input". It is *not* the metaphysical thesis, and the article must not trade on the word.

#### Slovic, Finucane, Peters & MacGregor (2007), "The affect heuristic"
- **Citation**: *European Journal of Operational Research*, 177(3), 1333–1352. https://doi.org/10.1016/j.ejor.2005.04.006 **[full text]**, from the course-site PDF of the EJOR version. The EJOR article is a **reprint** of the 2002 chapter in Gilovich, Griffin & Kahneman (eds.), *Heuristics and Biases*, pp. 397–420 (https://doi.org/10.1017/CBO9780511808098.025, **[metadata only]**). The first page carries "© 2002 Cambridge University Press". It was reprinted again in Lichtenstein & Slovic (eds.), *The Construction of Preference* (2006), pp. 434–453 (https://doi.org/10.1017/CBO9780511618031.024, **[metadata only]**). The task brief's "2002/2007" is therefore one text, not two papers. Cite one version and mention the other.
- **Key points**:
  - The definition **[verbatim]**: affect is "the specific quality of 'goodness' or 'badness' (i) experienced as a feeling state (with or without consciousness) and (ii) demarcating a positive or negative quality of a stimulus." The raw text renders the inner quotes as doubled apostrophes. **The field's "affect" is consciousness-neutral by definition.**
  - The mechanism **[verbatim]**: "people consult or refer to an 'affect pool' containing all the positive and negative tags consciously or unconsciously associated with the representations."
  - On causation **[verbatim]**: "These data support the theory that risk and benefit judgments are causally determined, at least in part, by the overall affective evaluation." This refers to Finucane et al.'s information manipulation. The claim concerns *judgements* of risk and benefit, not choices among options.
  - On awareness **[verbatim]**: "Manipulation of affect is no less powerful but is made more insidious by often taking place without our awareness."
- **Discrepancy to carry**: Slovic et al. describe the time-pressure experiment as Finucane et al.'s "second study". Finucane et al.'s own abstract makes it Study 1. Cite the study by content, not by number.
- **Tenet alignment**: neutral. The affect heuristic substitutes a fast evaluative tag for analytic weighing. Whether the tag is felt is left open by design, so it supports neither horn. That is the "reverse overreach" guard in the brief.

#### Finucane, Alhakami, Slovic & Johnson (2000), "The affect heuristic in judgments of risks and benefits"
- **Citation**: *Journal of Behavioral Decision Making*, 13(1), 1–17. https://doi.org/10.1002/(SICI)1099-0771(200001/03)13:1<1::AID-BDM333>3.0.CO;2-S **[abstract only]**.
- **Key points [verbatim]**:
  - "As expected, the inverse relationship was strengthened when time pressure was introduced."
  - People derive "both risk and benefit evaluations from a common source—affective reactions to the stimulus item."
- **Replication**: Efendić et al. (2022), *Social Psychological and Personality Science* 13(7), 1173–1184, https://doi.org/10.1177/19485506211056761 **[abstract only]**. Their verdict **[verbatim]**: "In two well-powered studies, using a more stringent analytic strategy, we replicated the original finding." They add caveats: "there was no change in risks when highlighting low benefits", and "the negative relationship can depend on incidental mood". They replicated the *information-manipulation* experiment (original r = −.74). No independent replication of the time-pressure experiment was found.

#### Loewenstein & Lerner (2003), "The role of affect in decision making"
- **Citation**: in R. J. Davidson, K. R. Scherer & H. H. Goldsmith (eds.), *Handbook of Affective Sciences* (pp. 619–642). Oxford University Press. https://doi.org/10.1093/oso/9780195126013.003.0031 (online 2002-12-19) **[metadata + opening text only]**. The chapter is paywalled, and the CMU author copy returns 404.
- **Key points**:
  - The opening text (OpenAlex) **[verbatim]**: "even incidental affect—affect that is unrelated to the decision at hand—can have a significant impact on judgment and choice".
  - The expected vs immediate taxonomy is attributed to this chapter by Jäger et al. 2020 **[verbatim there]**: "Loewenstein and Lerner (2003) broadly distinguished expected from immediate emotions." The chapter's own wording was **not reached**. Cite the taxonomy to the chapter only as a secondary attribution.

#### Pham (2007), "Emotion and rationality"
- **Citation**: *Review of General Psychology*, 11(2), 155–178. https://doi.org/10.1037/1089-2680.11.2.155 **[abstract only]**.
- **Key points [verbatim]**:
  - "Two types of emotional phenomena are examined—incidental emotional states and integral emotional responses".
  - Incidental states "are often misattributed to focal objects, distort beliefs in an assimilative fashion, disrupt self-control when intensely negative, but do not necessarily increase risk-taking."
  - "Integral emotional responses are often used as proxies for values".
  - "any categorical statement about the overall rationality or irrationality of emotion would be misleading."
- **Bearing**: "proxies for values" is the field's own statement of the value-blind rival's reading of integral affect, which treats it as a stand-in for learned value. Pham does not take sides on whether the proxy is felt.

#### Lerner, Li, Valdesolo & Kassam (2015), "Emotion and decision making"
- **Citation**: *Annual Review of Psychology*, 66, 799–823. https://doi.org/10.1146/annurev-psych-010213-115043 **[abstract only]**. eScholarship, Harvard, PhilArchive and the Annual Reviews e-print all returned 403.
- **Key points [verbatim]**:
  - "emotions constitute potent, pervasive, predictable, sometimes harmful and sometimes beneficial drivers of decision making";
  - the review proposes "the emotion-imbued choice model".
- **Guard**: the integral/incidental vocabulary and the appraisal-tendency framework are widely attributed to this review, but its full text was not read. Cite those constructs to Pham 2007, Peters 2006, Lerner & Keltner 2001 and Lerner et al. 2004, which were verified. Cite Lerner et al. 2015 only for its abstract.

#### Peters (2006) and Peters, Västfjäll, Gärling & Slovic (2006): affect as "common currency"
- **Citations**:
  - Peters, E. (2006). "The functions of affect in the construction of preferences", in Lichtenstein & Slovic (eds.), *The Construction of Preference*, pp. 454–463. https://doi.org/10.1017/CBO9780511618031.025 **[first-page text only, via OpenAlex]**.
  - Peters, Västfjäll, Gärling & Slovic (2006). *Journal of Behavioral Decision Making*, 19(2), 79–85. https://doi.org/10.1002/bdm.528 **[abstract only]**.
- **Key points [verbatim]**:
  - The chapter's definitions: "integral affect (positive and negative feelings about a stimulus) and incidental affect (positive and negative feelings such as mood states that are independent of a stimulus but can be misattributed to it)".
  - The editorial's four functions: "(affect as information, as a spotlight, as a motivator, and as common currency)".
- **Bearing**: the word "currency" already belongs to this field. Peters follows Cabanac (1992), "Pleasure: the common currency" (cited by the Map in two interface topics, not in the valence cluster), in treating affect as the dimension on which disparate options are compared. The Map's P-VS1 claims the same role for *felt* affect. Peters' functional claim is neutral about phenomenality.

#### Pfister & Böhm (2008), "The multiplicity of emotions"
- **Citation**: *Judgment and Decision Making*, 3(1), 5–17. https://doi.org/10.1017/S1930297500000127. Open access under CC-BY **[full text]**, Cambridge Core HTML.
- **Key points [verbatim]**:
  - Their summary of Peters: "Following Cabanac (Reference Cabanac 1992), Peters claims that affective reactions enable people to compare disparate events and complex arguments on a common underlying dimension." The bracketed reference string is a Cambridge HTML artefact.
  - Their critique of a single currency: "We doubt, however, that the totality of experiences, including complex cognitions, can be collapsed onto one hedonic scale of simple affect". Also: "many emotions cannot be mapped uniquely onto the positive-negative dimension", and ambivalence and trade-off difficulty "indicate the ubiquity of different currencies with frequently unknown exchange rates".
  - **On how valence enters choice**: "When making a choice, reducible emotions are mentally represented as beliefs about the decision's consequences, not as momentary feelings." And: "From memory or from imagination you infer how you might feel, but you do not necessarily feel it at that moment."
- **Bearing**: this is a decision-science statement of the route that [[affective-forecasting-gap]] L76 says leaves P-VS1 without input: a cool judgement of how one will feel, with flat present affect. It also bears on P-VS1's micro-valence shift condition (Shuman, Sander & Scherer 2013, already in [[valence-as-a-natural-kind]]) and on P-VS4 pluralism.

### B. Integral affect measured at choice

#### Schlösser, Dunning & Fetchenhauer (2013), "What a feeling"
- **Citation**: *Journal of Behavioral Decision Making*, 26(1), 13–30. https://doi.org/10.1002/bdm.757 **[reused; abstract only]**. Already in [[affective-forecasting-gap]] (ref 36) and [[miswanting]] (ref 15). Its quotations are on those pages.
- **New here: the 2009 Cologne dissertation**: T. M. Schlösser, *Deciding Emotions* (University of Cologne, KUPS 2770), https://kups.ub.uni-koeln.de/2770/ **[full text, 147 pp.]**.
  - Study 4: N = 108 Cornell students, an Ellsberg two-urn choice for $5. The design measured immediate emotions before choice, anticipated emotions, and felt emotions after the outcome was revealed.
  - **The post-outcome comparison is with *anticipated* emotions, not immediate ones** (Figure 5): "participants were well able to predict their average emotional states regarding the outcomes" **[verbatim]**. Arousal was overestimated in two outcome groups (t(19) = 3.68, p = .002; t(42) = 2.17, p = .036).
  - The authors answer the tautology objection (that people report feelings compatible with a choice they have already made) **[verbatim]**: "the participants were asked to indicate their emotions for both possible alternatives of betting or keeping the money, immediately before they had to make their final decision."
- **Guards**:
  - The dissertation's Study 4 may differ from the published Study 4, whose full text was unreachable (Wiley 403).
  - The outer review's claim that the design "directly refutes" the absence of an at-choice measure alongside later experience is right that both were *measured* in the same participants. The analysis found, though, sets later experience against the *anticipated* measure. So [[miswanting]]'s narrowed claim, that no study the Map found *sets* felt anticipation at choice *against* later experience, survives as scoped. It should mention that the data to do so existed in this design.

#### Young, Shuster & Mikels (2019), "The sure thing"
- **Citation**: *Emotion*, 19(6), 1035–1043. https://doi.org/10.1037/emo0000505 **[reused; full text verified by today's fork]**.
- **Reuse exactly as [[affective-forecasting-gap]] L76 has it**: probes "prior to participants' decision"; N = 32 and 24; immediate affect toward the sure option partially mediated framing; the anticipated-affect mediator was null (p = .63).
- **New context**: Cheng, Burns & Revie (2022) found that integral *fear and anger* did not account for risky-choice framing in one-off decisions. Their abstract **[verbatim]**: "suggest that the effects of risky-choice framing are not due to integral emotions". They also suggest that multi-problem designs may carry affect over from trial to trial. They measured discrete emotions rather than option-directed valence, so this is a tension with Young et al. rather than a failed replication. Do not say Cheng et al. targeted Young et al.: Cheng et al. is not among the 12 OpenAlex works citing Young et al.

#### Grimani, Yemiscigil, Wang, Kirilov, Kudrna & Vlaev (2024)
- **Citation**: "How do emotions respond to outcome values and influence choice?" *Psychological Research*, 88(8), 2234–2250. https://doi.org/10.1007/s00426-024-02001-3 **[abstract only]**.
- **Key points [verbatim]**:
  - "anticipatory and anticipated emotions responded very similarly to changes in value for the sure gains in both studies";
  - "Although anticipatory emotions mediated a larger portion of the effect, anticipated emotions also show some mediation."
- **Bearing**: anticipatory feeling *tracks outcome value*, as the value-blind rival predicts if integral affect is a correlate of learned or represented value. The post-decision timing of the "anticipatory" items is reported on [[miswanting]] and was **not re-verified here**: the Springer PDF returned HTML.

#### Jäger and colleagues (Bamberg): current versus expected valence in learning tasks
- **Citations**:
  - Jäger, Boltzmann, Rollnik & Rüsseler (2020), *Frontiers in Neuroscience* 14:580970, https://doi.org/10.3389/fnins.2020.580970 **[full text]**;
  - Jäger, Behrens & Rüsseler (2022), *Cognition and Emotion* 36(3), 560–567, https://doi.org/10.1080/02699931.2021.2020730 **[abstract only]**;
  - Jäger & Rüsseler (2025), *Frontiers in Psychology* 16:1570369, https://doi.org/10.3389/fpsyg.2025.1570369 **[abstract only]**.

  All three surfaced in the forward-citation search on Schlösser et al.
- **Key points**:
  - 2020: Experiment 1 had N = 25 Bamberg students, in an experience-based gambling task where option values must be *learned*.
  - The "current affect" item is **global, not option-directed** **[verbatim]**: "Please rate how you are feeling now." The expected item: "Please rate how you would feel if you decided to gamble".
  - 2020 result **[verbatim]**: "Results suggest a guiding function of expected valence for decisions". Also: "Incorporating subjective feelings and expectancies of subjective feelings into one model shows that there is no predictive power of current affect as a goal-directed account of emotions would predict."
  - 2022 **[verbatim]**: "While expected valence had the biggest effect size, current valence and the interaction still contributed significantly to the prediction of choice." And: "participants relied more on the current valence if expectations were unclear or positive".
  - 2025: current, short-term and long-term expected valence were all significant, with weights that depend on context.
- **Bearing**: this is the closest observational approach to the battery's bottom row, where learned value varies. Where value is learned, expected valence carries most of the weight and current felt state carries least, which is the profile the value-blind rival predicts. The guard: "current affect" here is global mood, not the option-directed felt anticipation P-VS1 names. The result therefore says little about P-VS1's input and something about incidental mood.

#### Petrova, Cokely, Sobkow, Traczyk, Garrido & Garcia-Retamero (2023), BERRI
- **Citation**: "Measuring feelings about choices and risks: The Berlin Emotional Responses to Risk Instrument (BERRI)". *Risk Analysis*, 43(4), 724–746 (online 2022). https://doi.org/10.1111/risa.13946 **[abstract only]**.
- **Key points**: seven studies, n = 2,120, measuring *anticipatory affective reactions*. **[verbatim]**: "choices were generally better explained by the unique influences of positive and negative affect".
- **Bearing**: a validated instrument a future battery test could use. Its finding that positive and negative affect act as separate inputs is another datum against a single scalar currency.

### C. The risk-as-feelings signature: affect-rich outcomes and probability

#### Rottenstreich & Hsee (2001), "Money, kisses, and electric shocks"
- **Citation**: *Psychological Science*, 12(3), 185–190. https://doi.org/10.1111/1467-9280.00334 **[abstract only]**. Loewenstein et al. 2001 cite it as a 1999 manuscript.
- **Key points [verbatim]**: "Weighting functions will be more S-shaped for lotteries involving affect-rich than affect-poor outcomes." And: "An affect-poor prize was preferred over an affect-rich prize under certainty, but the direction of preference reversed under low probability."
- **Replication: failed, in the opposite direction.** Klein et al. (2018), Many Labs 2, *Advances in Methods and Practices in Psychological Science*, 1(4), 443–490, https://doi.org/10.1177/2515245918810225 **[full text]**, open repository copy (TU/e). They replicated Study 1, a kiss from a favourite movie star versus $50:
  - Original: 70% chose the kiss at 1% probability vs 35% when certain; N = 40, d = 0.74.
  - Replication **[verbatim]**: "In the aggregate replication sample (N = 7,218), when the outcome was unlikely, 47% of participants preferred the affectively attractive choice, and when the outcome was certain, 51% preferred the affectively attractive choice. The difference was significant, p = .002, odds ratio (OR) = 0.87, d = −0.08, 95% CI = [−0.13, −0.03], but in the direction opposite the prediction of the hypothesis".
  - The reversal was significant at p < .05 but not at ML2's strict p < .0001.
- **Conceptual support from other paradigms**:
  - Pachur, Hertwig & Wolkewitz (2014), *Decision* 1(1), 64–78, https://doi.org/10.1037/dec0000006 **[abstract only]**: "systematic within-subject preference reversals" between affect-rich choices (medical side effects) and affect-poor ones (monetarily equivalent losses). Process data show that people "pay less attention to probability information" in affect-rich choices.
  - Suter, Pachur & Hertwig (2016; online 2015), *Journal of Behavioral Decision Making* 29(4), 437–449, https://doi.org/10.1002/bdm.1888 **[abstract only]**: a minimax (probability-neglect) rule fits affect-rich choices better. "The affect gap persisted even when affect-rich outcomes were supplemented by numerical information".
- **Bearing**: this is the one *signature* risk-as-feelings predicts for a felt input, namely probability insensitivity scaled by affect. Its classic demonstration failed at scale, and its surviving support compares *domains* (health vs money), in which affect-richness is confounded with everything else that differs between the domains. No study found measured felt affect as the mediator of the gap.

### D. Incidental affect, manipulated

#### Lerner & Keltner (2001), "Fear, anger, and risk"
- **Citation**: *Journal of Personality and Social Psychology*, 81(1), 146–159. https://doi.org/10.1037/0022-3514.81.1.146 **[abstract only]**.
- **Key points [verbatim]**:
  - "fear and anger have opposite effects on risk perception. Whereas fearful people expressed pessimistic risk estimates and risk-averse choices, angry people expressed optimistic risk estimates and risk-seeking choices."
  - "estimates of angry people more closely resembled those of happy people than those of fearful people."
  - "Appraisals of certainty and control moderated and (in the case of control) mediated the emotion effects."
- **Registered replication: mixed.** Lu, Efendić & Feldman (2026; online December 2025), *Journal of Personality and Social Psychology*, 131(4), e1–e18, https://doi.org/10.1037/pspp0000586 **[abstract only; OpenAlex's text begins mid-sentence]**. N = 780, a close replication of Experiments 1–3. **[verbatim]**: "We found support for the appraisal-tendency framework for risk optimism in general, risk optimism for positive events, and risk optimism for ambiguous events, but not for risk preference and risk optimism for negative events." Their hope extension (a positive-valence emotion with low certainty and control) "failed to find support for the assumptions of the appraisal-tendency framework."
- **Bearing**: the appraisal account survives for *judgement* and fails for *preference*, the part that concerns choice.

#### Ferrer, Maclay, Litvak & Lerner (2017; online 2016)
- **Citation**: "Revisiting the effects of anger on risk-taking: Empirical and meta-analytic evidence for differences between males and females". *Journal of Behavioral Decision Making*, 30(2), 516–526. https://doi.org/10.1002/bdm.1971 **[abstract only]**.
- **Key point [verbatim]**: "incidental anger is significantly more likely to drive risky decision making among males than among females". This is a moderator, and it helps explain why pooled anger effects average to null.

#### Lerner, Small & Loewenstein (2004), "Heart strings and purse strings"
- **Citation**: *Psychological Science*, 15(5), 337–341. https://doi.org/10.1111/j.0956-7976.2004.00679.x **[abstract only]**. It is already a lead in [[research/miswanting-and-forecast-driven-mischoice-2026-10-12]], where its replication status was unknown.
- **Key points [verbatim]**:
  - incidental disgust carried over to unrelated economic decisions, "reducing selling and choice prices and eliminating the endowment effect";
  - sadness reduced selling prices but increased choice prices;
  - "emotions of the same valence can have opposing effects on such decisions."
- **Replication: succeeded, for sadness and choice prices.** Garg, Williams & Lerner (2018), *PLOS ONE* 13(6), e0199433, https://doi.org/10.1371/journal.pone.0199433 **[full text]**:
  - New induction clips (*Steel Magnolias* / *Blue Planet* replacing *The Champ* / National Geographic) and a new commodity (a water bottle);
  - original d = 0.49, replication d = 0.40; "a meta-analysis of the original effect and that observed in the present study yielded a small-to-medium effect (Cohen's d = 0.43)" **[verbatim]**;
  - abstract **[verbatim]**: "Sadness increases how much decision makers pay to acquire goods, even when decision makers are unaware of it."
  - It did **not** test disgust or selling prices.

#### Meta-analyses of incidental emotion and risk
- **Bartholomeyczik, Gusenbauer & Treffers (2022)**: *Cognition and Emotion*, 36(6), 1054–1073. https://doi.org/10.1080/02699931.2022.2099349 **[abstract only]**. 28 experimental studies. **[verbatim]**: "We find emotion-specific, moderately heterogeneous effects partially in line with the expectations of the ATF". Effects depend "on appraisals other than valence".
- **Marini (2023)**: "Emotions and financial risk-taking in the lab: A meta-analysis". *Journal of Behavioral Decision Making*, 36(4), e2342. https://doi.org/10.1002/bdm.2342 **[abstract only]**. 114 effect sizes from 26 articles. **[verbatim]**: the meta-regressions "find causal impact of fear on risk aversion, albeit to a small extent. On the contrary, average null effects characterize happiness, sadness, and anger."
- **Angie, Connelly, Waples & Kligyte (2011)**: *Cognition & Emotion*, 25(8), 1393–1422. https://doi.org/10.1080/02699931.2010.550751 **[abstract only]**. Discrete emotions have "moderate to large effects on judgement and decision-making outcomes", with moderation by design. This is older and broader than the two above. Cite it as background only.

#### Dong, Dreber, Johannesson & Kilicgedik (2026), "Incidental emotions and financial risk-taking"
- **Citation**: *Journal of Economic Behavior & Organization*, 246, 107556. https://doi.org/10.1016/j.jebo.2026.107556. The licence is CC-BY, but only the **[abstract]** was reached: ScienceDirect returned 403 and the Elsevier API requires a key.
- **Key points [verbatim]**:
  - A "high powered (n=7,000) conceptual replication study on Prolific based on a detailed pre-analysis plan", with five emotion conditions and a no-induction control.
  - "The emotion manipulations worked as intended with large manipulation effects on the targeted emotions. However, we find no evidence of causal effects of incidental emotions on risk-taking."
  - "There are no statistically significant differences in risk-taking between the positive and negative emotion conditions and no effect of emotions compared to the control condition."
  - "at least in this setting."
  - **The manipulation check was run in a separate condition** **[verbatim]**: "As an emotion manipulation check, we also include a condition that rates the emotions of the movie clips without the risk task."
- **Bearing**: this is the strongest test found of the battery's "shift present affect" row, and it returned null for risk preference. See [the battery section](#bearing-on-p-vs1-and-the-p-vs2-battery) for what it does and does not show.

#### Ferrer & Ellis (2021; online 2020): integral and incidental emotion are not interchangeable
- **Citation**: "Preliminary evidence for differential effects of integral and incidental emotions on risk perception and behavioral intentions: A meta-analysis of eight experiments". *Journal of Behavioral Decision Making*, 34(2), 275–289. https://doi.org/10.1002/bdm.2209 **[abstract only]**. It appeared in the forward-citation list for Young et al.
- **Key points [verbatim]**:
  - a "pre-registered meta-analysis of eight experiments (n = 5,336)" which "rendered emotion integral or incidental to the threat by varying the type of outcomes assessed (matched or unmatched to the emotion induction)";
  - "Most notably, incidental anger decreased risk perceptions, whereas integral anger increased them";
  - "even when the direction of the effect of integral and incidental emotions was similar, the magnitude of the integral effect was larger";
  - "the common practice of manipulating incidental emotions and generalizing findings to integral emotions may not be advisable".
- **Bearing**: the outcomes are risk perceptions and behavioural intentions, not choices. The paper shows that incidental induction, the field's standard way of manipulating affect, is not a safe proxy for the integral affect P-VS1 names. It also cuts both ways for the Map, as the debates below set out.

#### Mood as information: a replication caution
- Schwarz & Clore (1983), *JPSP* 45(3), 513–523, https://doi.org/10.1037/0022-3514.45.3.513 **[metadata only]**: the misattribution paradigm behind "incidental affect".
- Yap et al. (2017), *JPSP* 113(6), 939–961, https://doi.org/10.1037/pspp0000115 **[abstract only]**: nine direct and conceptual replications. **[verbatim]**: "Most of the 9 studies resulted in nonsignificant effects on life satisfaction and happiness judgments, and those that were significant were substantially smaller than effects found in previous research."
- **Bearing**: the misattribution mechanism [[miswanting#misattribution]] calls "the risk specific to a felt currency" has weak large-sample support in its classic judgement domain. The article should mention this in one clause if it relies on misattribution.

### E. Felt affect at choice manipulated by regulation

#### Sokol-Hessner, Hsu, Curley, Delgado, Camerer & Phelps (2009), "Thinking like a trader"
- **Citation**: *PNAS*, 106(13), 5035–5040. https://doi.org/10.1073/pnas.0806761106 **[full text]**, PMC2656558.
- **Design**: Study 1 had N = 30. Study 2 had 52 completers, of whom 32 remained after exclusions.
  - Participants chose under an "Attend" strategy ("as if it was the only one") and a "Regulate" strategy ("as if creating a portfolio") **[verbatim]**.
  - Regulation "uniquely reduced both behavioral loss aversion and arousal to losses relative to gains" **[verbatim]**.
- **The guard that matters**: the authors list emotion's components ("facial and vocal expression, subjective feelings, action tendencies, bodily responses, and cognitive appraisals") and then **[verbatim]**: "For the following study, we focus on the latter 3 components." Subjective feeling was **not measured**, and arousal is skin conductance.
- The "portfolio" instruction also changes choice bracketing (broad versus narrow), a cognitive reframing that could lower loss aversion without any felt mediator.
- The Map already cites Sokol-Hessner et al. 2015 in [[negative-valence-asymmetry-and-the-selection-weighting-function]].

#### Heilman, Crişan, Houser, Miclea & Miu (2010)
- **Citation**: "Emotion regulation and decision making under risk and uncertainty". *Emotion*, 10(2), 257–265. https://doi.org/10.1037/a0018489 **[abstract only]**.
- **Key point [verbatim]**: "cognitive reappraisal of these negative emotions promotes risky decisions (reduces risk aversion) in the Balloon Analogue Risk Task". The emotions were laboratory-induced fear and disgust, which are incidental.

#### Morawetz, Mohr, Heekeren & Bode (2019)
- **Citation**: *Social Cognitive and Affective Neuroscience*, 14(10), 1109–1118. https://doi.org/10.1093/scan/nsz078 **[abstract only]**.
- **Key point [verbatim]**: "emotion regulation was followed by less risky decisions". Here too the regulated emotions were incidental.
- **Heterogeneity**: reappraisal *raised* risk-taking in Heilman et al. and *lowered* it in Morawetz et al. Tasks and stimuli differ, so do not average them.

### F. The countermodel

#### Davis, Love & Maddox (2009), "Anticipatory emotions in decision tasks"
- **Citation**: *Cognition*, 112(1), 195–200. https://doi.org/10.1016/j.cognition.2009.04.002 **[full text, PMC2735832; re-grepped today]**. Already on [[miswanting]] (ref 19).
- **Verbatim, re-confirmed**:
  - "We find that emotions are associated with responses as opposed to stimuli."
  - "there is no economic valence in a rule-plus-exception task"
  - "not a refutation of the theory as a whole"
- **Reuse the miswanting limits verbatim**: stimulus *risk* versus response, not value; skin-conductance arousal, not felt valence.

### G. Reused without new verification
- **Dorison, Minson & Rogers (2019)**, *Cognition* 188, 98–107, https://doi.org/10.1016/j.cognition.2019.02.010 **[reused]**:
  - forecasts p = .028; experience p = .002; the authors concede demand;
  - the replication's choice effect was .21 vs .14, p < .001, and it measured no forecasts;
  - **do not use "34%".**

  This is the battery's top row, which discriminates nothing.

## Major Positions

### Cognitive-consequentialist models
- **Proponents**: expected-utility and prospect-theory traditions, as characterised by Loewenstein et al. 2001.
- **Core claim**: choice integrates desirability and likelihood. Feelings at decision are not modelled as inputs.
- **Relation to tenets**: the psychological "epiphenomenal" here is modelling scope, not metaphysics. It bears on Tenet 3 only by inheritance from the value-blind rival, which needs no felt term ([[the-steelman-for-value-blind-selection#selection-without-a-felt-value-currency|selection without a felt-value currency]]).

### Risk-as-feelings
- **Proponents**: Loewenstein, Weber, Hsee & Welch (2001).
- **Core claim**: anticipatory feelings and cognitive evaluations are parallel inputs. They have different determinants (vividness, conditioning, evolutionary preparedness, probability insensitivity), and when they diverge, feelings "often drive behavior".
- **Relation to tenets**: this is the closest decision-science analogue of P-VS1, and it is naturalist. Its signature prediction (affect-scaled probability insensitivity) failed at scale in ML2 and survives in between-domain designs.

### The affect heuristic
- **Proponents**: Slovic, Finucane, Peters & MacGregor; Finucane et al. 2000.
- **Core claim**: people judge using a fast evaluative tag, drawn from an "affect pool", as a substitute for analysis. Time pressure increases reliance on it.
- **Relation to tenets**: consciousness-neutral by definition ("with or without consciousness"). Speed and substitution fit a sub-personal valuation process as well as a felt one. Any article use must say that it supports neither horn.

### The appraisal-tendency framework
- **Proponents**: Lerner & Keltner 2000/2001; Lerner et al. 2004, 2015.
- **Core claim**: discrete emotions carry appraisals (certainty, control) that set decision-relevant tendencies. Same-valence emotions can push choice in opposite directions.
- **Relation to tenets**: the relation runs through P-VS1's **micro-valence shift condition**. The condition holds that if felt valence at choice is several qualitatively distinct evaluations, integrated *for* the choice rather than consulted at it, the currency premise is retired while P-VS3 stands. ATF findings support distinct evaluative contents doing the work, but their replication record is mixed: judgement holds, preference does not (Lu et al. 2026), and the effects are small and specific to fear (Marini 2023). This supports P-VS4 pluralism more than it threatens P-VS3.

### Emotions-as-outcome
- **Proponents**: Davis, Love & Maddox 2009.
- **Core claim**: anticipatory affect may be produced by deciding rather than fed into it.
- **Relation to tenets**: a live countermodel to any "measured before choice, therefore input" inference. It neither shows nor implies epiphenomenalism, since the authors allow that such processes "could impact trial-by-trial decision-making" (quoted on [[miswanting]]).

### One currency or many
- **Proponents**: Peters et al. 2006 and Cabanac 1992 (common currency) versus Pfister & Böhm 2008 (multiple currencies with "unknown exchange rates"); Petrova et al. 2023 (positive and negative affect as separate inputs).
- **Relation to tenets**: this is the decision-science face of the dimensionality question [[valence-as-a-natural-kind]] already takes from Shuman, Sander & Scherer. Its natural home is P-VS4.

## Key Debates

### 1. Is the field's "affect" felt?
- **Sides**: the risk-as-feelings and immediate-emotion work measures self-reported feeling. The affect-heuristic tradition defines affect "with or without consciousness". The physiological tradition (Davis; Sokol-Hessner; somatic markers) measures arousal.
- **Core disagreement**: none within the field, which does not need the distinction. That is exactly why the Map cannot import the results as evidence for a *felt* currency without a bridging argument.
- **Current state**: unresolved and mostly unasked. The self-report studies (Schlösser, Young, BERRI) are the only ones that bear on felt valence, and they are correlational.

### 2. Does affect at choice feed choice, or follow it?
- **Sides**:
  - Input readings: Loewenstein et al. 2001; Schlösser et al. 2013, with its tautology reply; Young et al. 2019.
  - Output and correlate readings: Davis et al. 2009; Grimani et al. 2024, where anticipatory emotion tracks outcome value; Pham 2007, "proxies for values".
- **Current state**: open. Measurement before choice rules out post-hoc rationalisation of a *completed* choice. It does not rule out affect produced by an *incipient* choice or by value computation.

### 3. Does incidental affect move choice?
- **Positive**: Lerner et al. 2004 (valuation), replicated by Garg et al. 2018 (sadness → choice price, d ≈ 0.4); Ferrer et al. 2017 (anger, males).
- **Weak or null**:
  - Dong et al. 2026: n = 7,000, detailed pre-analysis plan, null on risk-taking with an effective manipulation;
  - Marini 2023: fear small, others null;
  - Lu et al. 2026: ATF preference not replicated;
  - Yap et al. 2017: mood-as-information mostly null in large samples.
- **Current state**: domain-dependent. Effects on valuation are better supported than effects on risk preference.

### 4. Are integral and incidental affect the same input?
- **Sides**: the field's "common practice", which uses incidental induction to study integral effects, versus Ferrer & Ellis 2021, where the two diverge in direction for anger and in size generally.
- **Current state**: preliminary, by the authors' own label. For the Map this is a symmetric hazard, set out under the battery below.

### 5. Is the probability-insensitivity signature real?
- **Sides**: Rottenstreich & Hsee 2001; Pachur et al. 2014; Suter et al. 2016 versus Many Labs 2 (Study 1 reversed, N = 7,218).
- **Current state**: the classic demonstration failed. Between-domain support remains, confounded by domain.

## Bearing on P-VS1 and the P-VS2 Battery

The battery from [[affective-forecasting-gap]] (L86–L90) is used below with its own row labels.

**Row 1, "Debias forecast (checked)"**: Dorison et al. 2019 (reused). Nothing new here; the row does not discriminate between the readings.

**Row 2, "Shift present affect; forecast, learned value fixed"**: this literature is the field's attempt at this row. Its findings:
- **Incidental induction** is the standard tool.
  - It moves valuation in one replicated case (sadness → choice price).
  - It leaves risk preference unmoved in the best-powered test (Dong et al. 2026).
  - Random assignment holds the options' learned value fixed in expectation.
  - No study found measured or held the *forecast*.
  - Dong et al.'s manipulation check was between-subjects. Risk-task participants' felt state was not reported, so the row's "manipulation check" requirement (afg L92) is only partly met.
- **Regulation** manipulates *integral* affect at choice (Sokol-Hessner 2009) but confounds it with reframing and did not measure subjective feeling. The other two regulation studies regulated incidental emotion.
- **Ferrer & Ellis 2021** warn that incidental results may not generalise to integral affect.
- **The commitment the Map has already made.** [[miswanting#misattribution]] says: "choice left unmoved by induced incidental affect, with learned value and bodily state held fixed, would count against P-VS1." Dong et al. 2026 is, in the risk domain, a large pre-analysis-planned instance of choice left unmoved by effectively induced incidental affect. Learned value was held by randomisation; bodily state was not measured. The honest reading is a **partial hit on the Map's own stated falsifier, confined to risk preference**, and it counts modestly against P-VS1's misattribution prediction there. The Map **must not** escape it by switching to "incidental affect is not the currency" (Ferrer & Ellis): it chose incidental affect as the test, so either the falsifier stands or the miswanting sentence must be rewritten in advance of results, with the integral/incidental hazard stated symmetrically. Positive incidental results (Garg et al.) are equally *non*-evidence of a felt currency on that same hazard, since the rival predicts state-dependent valuation too. That page already concedes the rival's behavioural-grain analogue.

**Row 3, "Shift learned value; affect, forecast fixed"**: there is no manipulation, but the closest observational analogue is the Jäger series. Where values must be learned, expected valence dominates and global current affect adds little, which is the rival's profile. The guard: that "current affect" is not option-directed.

**Net**: no band change for P-VS1 is warranted. Credence stays low and grade D, held on prior commitments, with the mechanism-sufficiency rival undefeated. The register cannot take a length-neutral edit (2 words of headroom). Any update belongs in a dated calibration-history note. Two candidate notes:
- the Dong et al. partial falsifier hit (risk domain);
- decision-science support for the micro-valence shift condition (ATF; Pfister & Böhm; BERRI).

## Potential Article Angles

1. **Primary** (recommended): "Immediate Emotions and the Affect Heuristic: Felt Affect as an Input to Choice".
   - *Lede*: the field measures felt affect at choice and finds that it predicts choice. Front-load the claim's status: measured not manipulated, consciousness-neutral where it is a heuristic, and null for risk preference when induced incidentally at scale, so it fits P-VS1's currency without evidencing it.
   - *Sections*:
     - The vocabulary (a compressed table);
     - What was measured (Schlösser, Young, Grimani, BERRI; Jäger as the learning-task contrast);
     - What was manipulated (incidental: Lerner, Garg, Lerner & Keltner with Lu, Dong, the meta-analyses; regulation: Sokol-Hessner, Heilman);
     - Whether the affect is felt (Slovic's definition; Sokol-Hessner's component choice; Davis);
     - Valence or appraisal? (ATF; Pfister & Böhm, linking to [[valence-as-a-natural-kind]] and P-VS1's micro-valence condition);
     - The risk-as-feelings signature and its failed replication;
     - Bearing on the battery, row by row;
     - Relation to Site Perspective.
   - *Length*: a 2,500–3,200-word body fits topics soft 3,000 / hard 4,000. Keep references to about 30.
2. **Alternative**: a short `concepts/` vocabulary page (integral vs incidental vs immediate affect). Not recommended: concepts are at 362/370, and the substantive findings would be stranded.

**Integration** (for the article's cross-review chain; do not edit these pages from the article task):
- [[affective-forecasting-gap]] L76: one link at "immediate emotions";
- [[miswanting]] at #misattribution: the Dong et al. partial hit and the Yap et al. caution (a refine task, not an article edit);
- [[the-steelman-for-value-blind-selection#selection-without-a-felt-value-currency|the steelman's currency section]]: Pham's "proxies for values" and Grimani's value-tracking anticipatory affect strengthen the rival's exhibit (1,003 words of headroom there);
- [[somatic-interface]]: a Further Reading link only;
- [[numbing-void]]: already cites Hsee & Rottenstreich 2004 (the 2004 *JEP: General* paper, not the 2001 study ML2 failed). Check it for any reliance on the 2001 kiss/shock result before linking.

## Guards for the Article Writer (Binding)

1. **Never concede that feeling is idle.** Nulls for *incidental* affect on *risk preference* do not show that felt valence does no work. Loewenstein's "epiphenomenal" is psychological modelling scope, not the metaphysical thesis. Do not quote it as if the field endorsed or refuted epiphenomenalism.
2. **No reverse overreach.** The affect heuristic ("feeling substitutes for deliberation") supports neither horn, because its affect is defined "with or without consciousness". Do not frame speed, substitution or time-pressure effects as evidence for P-VS1.
3. **Fit, never evidence.** Measured integral affect fits P-VS1's candidate currency without evidencing it:
   - measured, not manipulated;
   - mediation is not causal identification;
   - the rival reads integral affect as a correlate of learned value (Pham's "proxies for values"; Grimani's value-tracking);
   - Davis et al. 2009 is the live countermodel.
4. **Do not escape Dong et al. selectively.** If the article invokes Ferrer & Ellis to discount incidental nulls, it must discount incidental positives (Lerner, Garg) by the same argument. It must also note that [[miswanting#misattribution]] committed to incidental induction as a test.
5. **Do not cite Lerner et al. 2015 or Loewenstein & Lerner 2003 for content beyond their abstracts or opening text.** Neither full text was read. Attribute the integral/incidental definitions to Peters 2006 or Pham 2007. Attribute expected vs immediate to Loewenstein & Lerner only "as reported by" Jäger et al. 2020.
6. **Slovic et al. 2002/2007 is one text.** Cite the EJOR 2007 reprint (read in full) and note the 2002 original. Do not count it as two works.
7. **Finucane et al.'s time-pressure study is Study 1** by their own abstract. Slovic et al. call it the "second study". Avoid study numbers, or use Finucane's. Its replication (Efendić et al. 2022) covers the *information* experiment, not time pressure.
8. **Rottenstreich & Hsee 2001**: always pair it with the Many Labs 2 reversal (Study 1, N = 7,218, d = −0.08, opposite direction). Do not present affect-scaled probability weighting as established. Pachur and Suter support an "affect gap" between domains, not the original paradigm.
9. **Lerner & Keltner 2001**: pair it with Lu et al. 2026. The ATF replicated for risk *optimism* (judgement), not for risk *preference*.
10. **Sokol-Hessner et al. 2009 did not measure subjective feeling**; the "focus on the latter 3 components" sentence is the reason. Its regulation instruction is also a bracketing reframe.
11. **Jäger et al.'s "current affect" is global mood** ("how you are feeling now"), not option-directed. Do not set it against Schlösser or Young as a like-for-like contradiction.
12. **Schlösser's dissertation is not the published paper.** Use it only for what it states and flag possible divergence. Its post-outcome comparison is with *anticipated* emotion, and it found forecasts accurate on average (arousal overestimated in two cells).
13. **Absence claims**: see the next section. Every "no study" must name the search scope.
14. **Quotations**: use only strings marked **[verbatim]** above. The Loewenstein et al. OCR text substitutes a hyphen for the em dash in "epiphenomenal—that is". Quote from the scan's punctuation, or paraphrase.

## Absence and Exclusivity Claims (Scoped)

Each claim below is licensed by the three searches the style rule requires:
- **field vocabulary**: immediate, anticipatory, integral and incidental emotion, affect heuristic, emotion regulation, risky choice;
- **forward citation**: Schlösser et al. 2013, all 87 citing works screened by title; Young et al. 2019, all 12;
- **known controversy**: ML2; Lu et al. RR; Dong et al.; Efendić et al.; Garg et al.; the Bartholomeyczik, Marini and Ferrer & Ellis meta-analyses; Cheng et al.; Yap et al.

Each is still scoped to that search.

- **(a)** No study the Map has found manipulated *option-directed* felt affect at choice with a within-participant felt-valence manipulation check while measuring and holding fixed both the forecast and learned value, which are the conditions of the battery's middle row. The nearest are:
  - incidental induction (Dong; Lerner; Garg), where the forecast is unmeasured and the check is between-subjects or separate;
  - regulation (Sokol-Hessner, where feeling was unmeasured; Heilman and Morawetz, which regulated incidental emotion);
  - Ferrer & Ellis's integral inductions, whose outcomes were perceptions and intentions rather than choices.
- **(b)** No study the Map has found sets option-directed immediate emotion *against later experienced emotion* in an analysis. Schlösser's dissertation Study 4 measured both but reports the experience comparison for anticipated emotion only.
- **(c)** No independent replication of Finucane et al.'s time-pressure experiment was found. Efendić et al. replicated the information experiment.
- **(d)** No study the Map has found measured felt affect as the *mediator* of the affect-rich/affect-poor probability gap.

The article must carry these as "no study the Map has found …" with the inclusion criterion inline. None licenses a description- or lede-level "no study" claim without that qualifier.

## Historical Timeline

| Year | Event/Publication | Significance |
|---|---|---|
| 1983 | Schwarz & Clore, mood as information | Origin of the incidental-misattribution paradigm; weak in large-sample replications (Yap et al. 2017) |
| 1992 | Cabanac, "Pleasure: the common currency" | The "common currency" idea that Peters later carries into decision science |
| 2000 | Finucane, Alhakami, Slovic & Johnson | Affect heuristic experiments (time pressure; information manipulation) |
| 2001 | Loewenstein, Weber, Hsee & Welch, "Risk as feelings" | Anticipatory vs anticipated emotion; the identification condition |
| 2001 | Rottenstreich & Hsee | Affect-rich outcomes and S-shaped weighting |
| 2001 | Lerner & Keltner | Fear and anger, of the same valence, move risk in opposite directions |
| 2002 / 2007 | Slovic et al., "The affect heuristic" (chapter; EJOR reprint) | The affect pool, "with or without consciousness" |
| 2003 | Loewenstein & Lerner, *Handbook of Affective Sciences* | Expected vs immediate emotions (secondary attribution) |
| 2004 | Lerner, Small & Loewenstein | Incidental disgust and sadness on the endowment effect |
| 2006 | Peters; Peters, Västfjäll, Gärling & Slovic | Integral vs incidental defined; four functions, including "common currency" |
| 2007 | Pham | Integral responses as "proxies for values"; incidental states do not necessarily increase risk-taking |
| 2008 | Pfister & Böhm | Several currencies; valence enters choice as belief, "not as momentary feelings" |
| 2009 | Sokol-Hessner et al.; Davis, Love & Maddox | Regulation lowers loss aversion and arousal (feeling unmeasured); emotions-as-outcome |
| 2011–2013 | Schlösser, Dunning & Fetchenhauer (online 2011) | Immediate emotions predict risky choice beyond anticipated emotions |
| 2014–2016 | Pachur et al.; Suter et al. | The "affect gap" between domains; probability neglect |
| 2015 | Lerner et al., *Annual Review* | The emotion-imbued choice model |
| 2018 | Many Labs 2; Garg, Williams & Lerner | Rottenstreich & Hsee Study 1 reversed at N = 7,218; sadness → choice price replicated |
| 2019 | Young, Shuster & Mikels | Immediate (not anticipated) affect mediates framing (N = 32, 24) |
| 2020–2025 | Jäger et al. | Expected valence outweighs current mood in learning tasks |
| 2021 | Ferrer & Ellis | Integral ≠ incidental (preregistered, n = 5,336) |
| 2022 | Bartholomeyczik et al.; Efendić et al.; Cheng, Burns & Revie | ATF meta-analysis; affect heuristic replicated; integral fear and anger do not explain framing |
| 2023 | Marini; Petrova et al. (BERRI) | Only fear moves financial risk, and only slightly; positive and negative affect as separate inputs |
| 2024 | Grimani et al. | Anticipatory emotion tracks outcome value |
| 2026 | Dong, Dreber, Johannesson & Kilicgedik; Lu, Efendić & Feldman | n = 7,000 null for incidental emotion on risk; ATF replicated for judgement, not preference |

## Gaps in Research

- **Full texts not reached**:
  - Lerner et al. 2015 (all hosts 403);
  - Loewenstein & Lerner 2003 (paywalled; CMU 404);
  - Schlösser et al. 2013 (Wiley 403; dissertation used instead);
  - Dong et al. 2026 (CC-BY but 403; risk task, incentives and per-condition felt-state data unknown);
  - Lu et al. 2026 (Maastricht 403; OpenAlex abstract truncated at its start);
  - Ferrer & Ellis 2021; Marini 2023; Bartholomeyczik et al. 2022; Pachur et al. 2014; Suter et al. 2016; Heilman et al. 2010; Morawetz et al. 2019; Cheng et al. 2022; Grimani et al. 2024 (Springer returned HTML); Peters 2006 (first page only); Efendić et al. 2022.
- **Not extracted**: Garg et al. 2018's sample size; the numbers in Sokol-Hessner et al.'s exclusion arithmetic beyond "52 … 32 remaining".
- **Grimani et al.'s item timing** (post-decision, per [[miswanting]]) was not re-verified.
- **Not searched**:
  - the neuroeconomics of integral affect (insula and amygdala value signals);
  - clinical anxiety and choice;
  - van Winden, Krawczyk & Hopfensitz (2011) on resolution timing, since it overlaps the time-preference note;
  - Engelmann et al.'s threat-of-shock studies (incidental anxiety);
  - Mellers' decision affect theory beyond what [[miswanting]] carries.
- **Forward-citation coverage**: the screen was by title only. A citing work with an uninformative title could have been missed.
- **Replication status unknown**: Sokol-Hessner et al. 2009, Young et al. 2019 and Schlösser et al. 2013.

## Citations

1. Angie, A. D., Connelly, S., Waples, E. P., & Kligyte, V. (2011). The influence of discrete emotions on judgement and decision-making: A meta-analytic review. *Cognition & Emotion*, 25(8), 1393–1422. https://doi.org/10.1080/02699931.2010.550751
2. Bartholomeyczik, K., Gusenbauer, M., & Treffers, T. (2022). The influence of incidental emotions on decision-making under risk and uncertainty: A systematic review and meta-analysis of experimental evidence. *Cognition and Emotion*, 36(6), 1054–1073. https://doi.org/10.1080/02699931.2022.2099349
3. Cheng, H., Burns, C., & Revie, M. (2022). Risky-choice framing and its null effect on integral emotions. *Journal of Risk Research*, 25(4), 453–467. https://doi.org/10.1080/13669877.2021.1936611
4. Davis, T., Love, B. C., & Maddox, W. T. (2009). Anticipatory emotions in decision tasks: Covert markers of value or attentional processes? *Cognition*, 112(1), 195–200. https://doi.org/10.1016/j.cognition.2009.04.002
5. Dong, Y., Dreber, A., Johannesson, M., & Kilicgedik, G. (2026). Incidental emotions and financial risk-taking. *Journal of Economic Behavior & Organization*, 246, 107556. https://doi.org/10.1016/j.jebo.2026.107556
6. Dorison, C. A., Minson, J. A., & Rogers, T. (2019). Selective exposure partly relies on faulty affective forecasts. *Cognition*, 188, 98–107. https://doi.org/10.1016/j.cognition.2019.02.010
7. Efendić, E., Chandrashekar, S. P., Lee, C. S., Yeung, L. Y., Kim, M. J., Lee, C. Y., & Feldman, G. (2022). Risky therefore not beneficial: Replication and extension of Finucane et al.'s (2000) affect heuristic experiment. *Social Psychological and Personality Science*, 13(7), 1173–1184. https://doi.org/10.1177/19485506211056761
8. Ferrer, R. A., & Ellis, E. M. (2021). Preliminary evidence for differential effects of integral and incidental emotions on risk perception and behavioral intentions: A meta-analysis of eight experiments. *Journal of Behavioral Decision Making*, 34(2), 275–289. https://doi.org/10.1002/bdm.2209
9. Ferrer, R. A., Maclay, A., Litvak, P. M., & Lerner, J. S. (2017). Revisiting the effects of anger on risk-taking: Empirical and meta-analytic evidence for differences between males and females. *Journal of Behavioral Decision Making*, 30(2), 516–526. https://doi.org/10.1002/bdm.1971
10. Finucane, M. L., Alhakami, A., Slovic, P., & Johnson, S. M. (2000). The affect heuristic in judgments of risks and benefits. *Journal of Behavioral Decision Making*, 13(1), 1–17. https://doi.org/10.1002/(SICI)1099-0771(200001/03)13:1<1::AID-BDM333>3.0.CO;2-S
11. Garg, N., Williams, L. A., & Lerner, J. S. (2018). The misery-is-not-miserly effect revisited: Replication despite opportunities for compensatory consumption. *PLOS ONE*, 13(6), e0199433. https://doi.org/10.1371/journal.pone.0199433
12. Grimani, A., Yemiscigil, A., Wang, Q., Kirilov, G., Kudrna, L., & Vlaev, I. (2024). How do emotions respond to outcome values and influence choice? *Psychological Research*, 88(8), 2234–2250. https://doi.org/10.1007/s00426-024-02001-3
13. Heilman, R. M., Crişan, L. G., Houser, D., Miclea, M., & Miu, A. C. (2010). Emotion regulation and decision making under risk and uncertainty. *Emotion*, 10(2), 257–265. https://doi.org/10.1037/a0018489
14. Jäger, D. T., Boltzmann, M., Rollnik, J. D., & Rüsseler, J. (2020). Expected valence predicts choice in a recurrent decision task. *Frontiers in Neuroscience*, 14, 580970. https://doi.org/10.3389/fnins.2020.580970
15. Jäger, D. T., Behrens, C., & Rüsseler, J. (2022). Current and expected affective valence interact to predict choice in recurrent decisions. *Cognition and Emotion*, 36(3), 560–567. https://doi.org/10.1080/02699931.2021.2020730
16. Jäger, D. T., & Rüsseler, J. (2025). Time matters: On the predictive power of current, short- and long-term expected valence in an experience based learning task. *Frontiers in Psychology*, 16, 1570369. https://doi.org/10.3389/fpsyg.2025.1570369
17. Klein, R. A., Vianello, M., Hasselman, F., et al. (2018). Many Labs 2: Investigating variation in replicability across samples and settings. *Advances in Methods and Practices in Psychological Science*, 1(4), 443–490. https://doi.org/10.1177/2515245918810225
18. Lerner, J. S., & Keltner, D. (2001). Fear, anger, and risk. *Journal of Personality and Social Psychology*, 81(1), 146–159. https://doi.org/10.1037/0022-3514.81.1.146
19. Lerner, J. S., Li, Y., Valdesolo, P., & Kassam, K. S. (2015). Emotion and decision making. *Annual Review of Psychology*, 66, 799–823. https://doi.org/10.1146/annurev-psych-010213-115043
20. Lerner, J. S., Small, D. A., & Loewenstein, G. (2004). Heart strings and purse strings: Carryover effects of emotions on economic decisions. *Psychological Science*, 15(5), 337–341. https://doi.org/10.1111/j.0956-7976.2004.00679.x
21. Loewenstein, G., & Lerner, J. S. (2003). The role of affect in decision making. In R. J. Davidson, K. R. Scherer, & H. H. Goldsmith (Eds.), *Handbook of Affective Sciences* (pp. 619–642). Oxford University Press. https://doi.org/10.1093/oso/9780195126013.003.0031
22. Loewenstein, G. F., Weber, E. U., Hsee, C. K., & Welch, N. (2001). Risk as feelings. *Psychological Bulletin*, 127(2), 267–286. https://doi.org/10.1037/0033-2909.127.2.267
23. Lu, S., Efendić, E., & Feldman, G. (2026). Associations of fear, anger, happiness, and hope with risk judgments: Revisiting appraisal-tendency framework with a replication and extensions Registered Report of Lerner and Keltner (2001). *Journal of Personality and Social Psychology*, 131(4), e1–e18. https://doi.org/10.1037/pspp0000586
24. Marini, M. M. (2023). Emotions and financial risk-taking in the lab: A meta-analysis. *Journal of Behavioral Decision Making*, 36(4), e2342. https://doi.org/10.1002/bdm.2342
25. Morawetz, C., Mohr, P. N. C., Heekeren, H. R., & Bode, S. (2019). The effect of emotion regulation on risk-taking and decision-related activity in prefrontal cortex. *Social Cognitive and Affective Neuroscience*, 14(10), 1109–1118. https://doi.org/10.1093/scan/nsz078
26. Pachur, T., Hertwig, R., & Wolkewitz, R. (2014). The affect gap in risky choice: Affect-rich outcomes attenuate attention to probability information. *Decision*, 1(1), 64–78. https://doi.org/10.1037/dec0000006
27. Peters, E. (2006). The functions of affect in the construction of preferences. In S. Lichtenstein & P. Slovic (Eds.), *The Construction of Preference* (pp. 454–463). Cambridge University Press. https://doi.org/10.1017/CBO9780511618031.025
28. Peters, E., Västfjäll, D., Gärling, T., & Slovic, P. (2006). Affect and decision making: A "hot" topic. *Journal of Behavioral Decision Making*, 19(2), 79–85. https://doi.org/10.1002/bdm.528
29. Petrova, D., Cokely, E. T., Sobkow, A., Traczyk, J., Garrido, D., & Garcia-Retamero, R. (2023). Measuring feelings about choices and risks: The Berlin Emotional Responses to Risk Instrument (BERRI). *Risk Analysis*, 43(4), 724–746. https://doi.org/10.1111/risa.13946
30. Pfister, H.-R., & Böhm, G. (2008). The multiplicity of emotions: A framework of emotional functions in decision making. *Judgment and Decision Making*, 3(1), 5–17. https://doi.org/10.1017/S1930297500000127
31. Pham, M. T. (2007). Emotion and rationality: A critical review and interpretation of empirical evidence. *Review of General Psychology*, 11(2), 155–178. https://doi.org/10.1037/1089-2680.11.2.155
32. Rottenstreich, Y., & Hsee, C. K. (2001). Money, kisses, and electric shocks: On the affective psychology of risk. *Psychological Science*, 12(3), 185–190. https://doi.org/10.1111/1467-9280.00334
33. Schlösser, T. M. (2009). *Deciding Emotions* [Doctoral dissertation, University of Cologne]. https://kups.ub.uni-koeln.de/2770/
34. Schlösser, T., Dunning, D., & Fetchenhauer, D. (2013). What a feeling: The role of immediate and anticipated emotions in risky decisions. *Journal of Behavioral Decision Making*, 26(1), 13–30. https://doi.org/10.1002/bdm.757
35. Schwarz, N., & Clore, G. L. (1983). Mood, misattribution, and judgments of well-being: Informative and directive functions of affective states. *Journal of Personality and Social Psychology*, 45(3), 513–523. https://doi.org/10.1037/0022-3514.45.3.513
36. Slovic, P., Finucane, M. L., Peters, E., & MacGregor, D. G. (2007). The affect heuristic. *European Journal of Operational Research*, 177(3), 1333–1352. https://doi.org/10.1016/j.ejor.2005.04.006 (reprinted from Gilovich, Griffin & Kahneman (Eds.), *Heuristics and Biases*, 2002, pp. 397–420, https://doi.org/10.1017/CBO9780511808098.025)
37. Sokol-Hessner, P., Hsu, M., Curley, N. G., Delgado, M. R., Camerer, C. F., & Phelps, E. A. (2009). Thinking like a trader selectively reduces individuals' loss aversion. *Proceedings of the National Academy of Sciences*, 106(13), 5035–5040. https://doi.org/10.1073/pnas.0806761106
38. Suter, R. S., Pachur, T., & Hertwig, R. (2016). How affect shapes risky choice: Distorted probability weighting versus probability neglect. *Journal of Behavioral Decision Making*, 29(4), 437–449. https://doi.org/10.1002/bdm.1888
39. Yap, S. C. Y., Wortman, J., Anusic, I., Baker, S. G., Scherer, L. D., Donnellan, M. B., & Lucas, R. E. (2017). The effect of mood on judgments of subjective well-being: Nine tests of the judgment model. *Journal of Personality and Social Psychology*, 113(6), 939–961. https://doi.org/10.1037/pspp0000115
40. Young, N. A., Shuster, M. M., & Mikels, J. A. (2019). The sure thing: The role of integral affect in risky choice framing. *Emotion*, 19(6), 1035–1043. https://doi.org/10.1037/emo0000505
