---
title: "Research: Anticipatory Feeling and Time Preference"
created: 2026-10-05
modified: 2026-10-05
human_modified: null
ai_modified: 2026-10-05T08:24:00+00:00
draft: false
description: "Research notes on savouring and dread: the anticipatory-utility literature models felt anticipation as exponential or constant, never hyperbolic, yet still derives preference reversals, in directions hyperbolic valuation does not predict."
topics:
  - "[[the-divided-will]]"
  - "[[valence-and-conscious-selection]]"
  - "[[akrasia-and-weakness-of-will]]"
  - "[[phenomenology-of-anticipation]]"
  - "[[wanting-liking-and-the-value-in-mechanism-fork]]"
concepts:
  - "[[affective-forecasting-gap]]"
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-05
last_curated: null
last_deep_review: null
---

# Research: Anticipatory Feeling and Time Preference — Is the Felt Currency Hyperbolic?

**Date**: 2026-10-05
**Target**: `topics/`, intended slug `anticipatory-feeling-and-time-preference`
**Originating claim**: [[the-divided-will]] §"What a Unitary Selector Must Add" says O1 and O3 (preference reversal under delay) "need a present-weighted currency, which is ad hoc unless the felt-valence currency ... is independently shown to be hyperbolic."

**Search queries used**:
- Loewenstein 1987 "Anticipation and the Valuation of Delayed Consumption" savoring dread
- anticipatory utility savoring dread hyperbolic discounting preference reversal time inconsistency
- Iigaya Story Kurth-Nelson Dolan Dayan "The modulation of savouring by prediction error"
- does anticipatory emotion intensity follow hyperbolic function of temporal distance (extended search)
- Loewenstein 1996 "Out of Control: Visceral Influences on Behavior"
- Ainslie hyperbolic discounting anticipatory utility savoring dread critique
- OpenAlex / Crossref / Europe PMC lookups by DOI for every item in the citation list

**Verification method**: Six sources were downloaded as raw artefacts (publisher XML, PMC HTML, or PDF converted with `pdftotext`) and every quotation below marked **[verbatim]** was matched by script against that raw text. Items marked **[abstract only]** were read as publisher abstracts via OpenAlex or Europe PMC. Items marked **[not reached]** were not read at all; nothing is attributed to their contents beyond bibliographic existence.

## Executive Summary

The literature does not show that felt anticipation is hyperbolic, and it does not show the opposite. No study located fits rival functional forms to a *felt* anticipatory quantity; the one modelling paper that could have done so (Story et al. 2013) says the data cannot separate the forms and adopts exponential discounting "for the sake of simplicity". Loewenstein (1987) models savouring and dread as rising *exponentially* as the event nears; Berns et al. (2006) assume *constant* instantaneous dread; Story et al. (2013) find dread rising toward the event, best fitted exponentially. So the sentence in the-divided-will sets a test the field has never run.

The more useful finding is that the test is mis-specified. Preference reversal requires non-stationarity, and a hyperbola is only one way to get it. A two-component value (discounted consumption plus proximity-weighted anticipation) is non-stationary even when both components are exponential, and it produces reversals: Loewenstein's "reverse time inconsistency" for savoured goods, and a dread-driven reversal that Harris (2012, Study 4) reports as the *modal* response pattern in a hypothetical-shock study. These reversals run in directions hyperbolic outcome valuation does not predict. Felt anticipation is also non-monotone in its effect on value: roughly half or more of participants expedite pain, and a minority show value peaking at intermediate delay.

For the Map this cuts both ways. The felt-currency horn gains a datum its rival must add an assumption to cover (expedited dread), and loses the appetitive case: savouring pushes *toward* delay, so the impulsive reversal that defines akrasia cannot come from savouring. It would have to come from a different felt state, impatience or visceral craving (Loewenstein 1996; Hardisty & Weber 2020), whose dependence on delay nobody has measured as a function.

## Key Sources

### Loewenstein (1987), "Anticipation and the Valuation of Delayed Consumption"
- **URL**: https://www.cmu.edu/dietrich/sds/docs/loewenstein/AnticipationDelayed.pdf (author-hosted JSTOR scan; doi 10.2307/2232929)
- **Type**: Paper, *The Economic Journal* 97(387), 666–684
- **Read**: full text (OCR layer of a scan; spacing and Greek letters are damaged, so quotations below are whitespace-normalised and symbol-bearing sentences are paraphrased)
- **Key points**:
  - Defines the two terms the field still uses. **[verbatim, whitespace-normalised]**: "the term 'savouring' refers to positive utility derived from anticipation of future consumption; 'dread' refers to negative utility resulting from contemplation of the future."
  - Illustrative survey, N = 30 undergraduates, hypothetical willingness to pay. Money items were discounted conventionally. The kiss from a film star was worth most at a three-day delay. The shock was worth *more* to avoid when delayed. **[verbatim]**: "Subjects on average were willing to pay more to experience a kiss delayed by 3 days than an immediate kiss or one delayed by three hours or one day."
  - **The functional form is exponential.** Equation (2)–(3) makes utility from anticipation at time *t* proportional to consumption utility multiplied by an exponential decay in the remaining delay (T − t), with its own rate parameter, which the paper describes as **[verbatim]** "a measure of the degree to which the individual derives immediate utility from anticipated consumption" and as distinct from "the conventional discount rate". The total is then discounted at the conventional rate *r*, also exponentially. Nothing in the model is hyperbolic.
  - The exponential shape is motivated by Jevons's introspective report, quoted in the paper **[verbatim]**: "the nearer the date fixed for leaving home approaches, the greater does the intensity of anticipal pleasure become: at first when the holiday is still many weeks ahead, the intensity increases slowly; then, as the time grows closer, it increases faster and faster, until it culminates on the eve of departure". The paper's support for an accelerating felt curve is this quotation plus willingness-to-pay data; no felt intensity is measured.
  - The model separates *discounting* (preference for earlier utility) from *devaluing* (how an outcome's present value changes with delay). **[verbatim]**: "For consumption that is fleeting and easy to imagine devaluing will often be initially negative."
  - **Time inconsistency follows without hyperbolic discounting.** **[verbatim]**: "While not ruling out such forms of time inconsistency, the current model predicts, under certain conditions, a related phenomenon, which could be termed 'reverse time inconsistency'." The agent who deferred to savour has the same reason to defer again on arrival. Loewenstein's example is children hoarding Hallowe'en sweets until they go stale.
  - For undesirable outcomes the model yields an indifference delay: allowed to defer beyond it the person defers, constrained to act before it the person wants it over at once (the dental-appointment pattern).
  - Vividness or imaginability is a parameter of the model, with Böhm-Bawerk cited as precedent.
- **Tenet alignment**: Neutral. The model is a utility model. It treats a presently felt state as an input to choice, which the value-sensitive horn needs, and says nothing on whether the feeling or its neural realiser does the work.

### Story, Vlaev, Seymour, Winston, Darzi & Dolan (2013), "Dread and the Disvalue of Future Pain"
- **URL**: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003335
- **Type**: Paper, *PLoS Computational Biology* 9(11), e1003335 (open access; publisher XML read in full)
- **Key points**:
  - Experiment 1: real electric shocks at delays up to 15 minutes, 25 participants analysed for time preference. Experiment 2: hypothetical dental appointments at delays up to about eight months, 30 participants.
  - Group result **[verbatim]**: "We show that future pain initially becomes increasingly aversive with increasing delay, but does so at a decreasing rate. This is consistent with a value model in which moment-by-moment dread increases up to the time of expected pain, such that dread becomes equivalent to the discounted expectation of pain."
  - Individual classification in Experiment 1 (counts read from the text): zero time preference 7/25, positive 4/25, negative 12/25, reversing 2/25. So 14 of 25 expedited pain over some range, and only 4 of 25 behaved as standard discounting predicts.
  - **Non-monotonicity** **[verbatim]**: "For a minority of individuals pain has maximum negative value at intermediate delay, suggesting that the dread function may itself be prospectively discounted in time." The authors limit the claim **[verbatim]**: "A small proportion of participants (2 out of 25 in Experiment 1) exhibited negative time preference which reverted to positive time preference at longer delays", and they add that they "have insufficient evidence to support this conclusion at the group level".
  - **On the hyperbolic question, directly** **[verbatim]**: "Although different forms of discounting function, such as hyperbolic and quasi-hyperbolic, are of importance in standard models of financial discounting, they have a relatively subtle effect here, since the more complex functional forms resulting from the addition of dread depend little on the precise shape of the basic discounting function; we therefore adopt exponential discounting for the sake of simplicity." This sentence is the only place the string "hyperbol" occurs in the paper (twice, as "hyperbolic" and "quasi-hyperbolic"). The hyperbolic form was set aside, not tested.
  - Winning model: "Exponential Dread", which the authors identify with **[verbatim]** "the original form of the anticipation-discounting model proposed by Loewenstein".
  - Framing matters: describing the same outcome as relief reduced the preference to expedite pain. Dread is therefore not a fixed function of delay and magnitude.
- **Tenet alignment**: Neutral. Dread is inferred from choice; no felt report is collected.

### Berns, Chappelow, Cekic, Zink, Pagnoni & Martin-Skurski (2006), "Neurobiological Substrates of Dread"
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC1820741/
- **Type**: Paper, *Science* 312(5774), 754–758 (PMC author manuscript read in full)
- **Key points**:
  - fMRI, 32 participants waiting for real foot shocks, then real choices between voltage-and-delay pairs.
  - Cluster analysis gave **[verbatim]** "extreme dreaders ( n = 9) and mild dreaders ( n = 23)". Extreme dreaders "preferred more voltage sooner to less voltage later".
  - **Functional form assumed, not estimated** **[verbatim]**: "For the sake of simplicity, we assumed that the instantaneous intensity of dread was constant". Consumption utility is discounted exponentially. This differs from both Loewenstein's rising exponential and the hyperbola.
  - The neural signature of dread sat in posterior (somatosensory and attentional) elements of the pain matrix. **[verbatim, abstract]**: "This suggests that dread derives, in part, from the attention devoted to the expected physical response and not simply from fear or anxiety."
  - The abstract's closing phrase is the strongest statement in this literature that a felt state drives the choice **[verbatim]**: "a neurobiological link between the experienced disutility of dread and subsequent decisions about unpleasant outcomes." The evidence is a between-subject correlation between a passive-phase BOLD time course and later choices.
- **Tenet alignment**: Neutral to mildly congenial. "Experienced disutility" causing choice is the shape Bidirectional Interaction wants, but the paper's evidence is neural and correlational and a physicalist reads it without strain. The attentional finding is closer to the Map's valence-modulates-attention middle path than to valence as a direct selector.

### Harris (2012), "Feelings of Dread and Intertemporal Choice"
- **URL**: https://charris.ucsd.edu/articles/Harris_JBDM2010.pdf (author-hosted; doi 10.1002/bdm.709)
- **Type**: Paper, *Journal of Behavioral Decision Making* 25(1), 13–28 (published online 2010; full text read)
- **Key points**:
  - Five studies, internet samples, hypothetical outcomes throughout. Monetary and property losses were mostly postponed; pain, embarrassment and rejection produced highly variable timing preferences, with many choosing immediacy. Timing preferences for negative experiences correlated with each other and were independent of time preference for rewards (abstract).
  - **Study 4, a dread-driven preference reversal.** 193 participants. **[verbatim]**: "152 out of 193 participants (79%) preferred to undergo the shock immediately", and "41% of all participants (79 out of 193) preferred immediate shock even to a shock they were told to regard as 20% less intense, to be delivered in 1 week."
  - Of the 103 who preferred 40 V now to 36 V in a week **[verbatim]**: "When given the same options with 24 weeks interposed, 76% of these individuals reversed their preference and chose the more delayed (and lower voltage) shock. This preference reversal was not only frequent—it was in fact the modal response pattern in the study."
  - The reversal in the classic hyperbolic direction was rare **[verbatim]**: "This pattern of responding, which was quite uncommon in the present study (6% of all participants), could be interpreted as a 'classic' preference reversal predicted by temporal discounting following a hyperbolic function (although other interpretations may be possible)." (The source prints the inner quotation marks as doubled single quotes.)
  - **Study 5, the nearest thing to a measured dread curve.** 304 participants rated on a 1–7 scale the dread they would feel *today* for a 40 V shock at four distances. **[verbatim]**: "A very similar pattern was seen in the median reports of anticipated degree of dread (6, 5, 4, and 2, for tomorrow, 1 week, 1 month, and 1 year, respectively)."
  - Harris states what the reversal requires **[verbatim]**: "A critical assumption in the foregoing discussion of time preferences is that people anticipate that feelings of dread inspired by a negative event will sharply increase with temporal proximity to the event." A uniform dread rate would still favour immediacy but would not produce the reversal.
  - **A null the article must carry** **[verbatim]**: "choices regarding the preferred timing of a shock were not significantly correlated with estimates of the amount of dread experienced at any of the four points in time". The reported range of *r* runs to .10 at its upper end; the lower bound prints with an unreadable glyph before ".04" in the PDF text layer, probably a minus sign, so read it as roughly −.04 to .10 and check a clean copy.
  - Real-life dread is common: about two-thirds recalled an episode in the previous 24 hours, with a median distance to the dreaded event of 7 days.
- **Caveats**: The Study 5 ratings are forecasts of an anticipatory emotion for a hypothetical event. In the vocabulary of [[affective-forecasting-gap]] they are *anticipated anticipatory* emotion, two removes from an occurrent valence. Four ordinal points on a bounded scale cannot discriminate exponential from hyperbolic decline (this note's inference; Harris does not attempt a fit).
- **Tenet alignment**: Neutral.

### Loewenstein (1996), "Out of Control: Visceral Influences on Behavior"
- **URL**: https://www.cmu.edu/dietrich/sds/docs/loewenstein/Outofcontrol.PDF
- **Type**: Paper, *Organizational Behavior and Human Decision Processes* 65(3), 272–292, doi 10.1006/obhd.1996.0028 (full text read). The 2004 item in the task lead, doi 10.1515/9781400829118-029, is this paper reprinted as chapter 26 of Camerer, Loewenstein & Rabin (eds.), *Advances in Behavioral Economics*, pp. 689–724 **[reprint not reached; pagination from OpenAlex]**.
- **Key points**:
  - Visceral factors are felt states by definition **[verbatim]**: "The defining characteristics of visceral factors are, first, a direct hedonic impact (which is usually negative), and second, an effect on the relative desirability of different goods and actions."
  - **A named rival to hyperbolic discounting as the account of impulsivity** **[verbatim]**: "Nevertheless, the non-exponential discounting perspective has at least two significant limitations as a general theory of impulsivity. First, it does not shed light on why certain types of consumption are commonly associated with impulsivity while others are not."
  - **[verbatim]**: "Second, the hyperbolic discounting perspective cannot explain why many situational features other than time delay—for example, physical proximity and sensory contact with a desired object—are commonly associated with impulsive behavior."
  - The positive thesis **[verbatim]**: "It views impulsivity as resulting not from the disproportionate attractiveness of immediately available rewards but from the disproportionate effect of visceral factors on the desirability of immediate consumption."
  - Proposition 2 **[verbatim]**: "Future visceral factors produce little discrepancy between the value we plan to place on goods in the future and the value we view as desirable." This is the cold-to-hot gap: a currently felt state weighs heavily, a forecast one hardly at all.
  - The two accounts make different predictions. On the hyperbolic account desirability rises automatically as a reward becomes imminent. On the visceral account immediacy produces impulsivity only when proximity elicits an appetitive response, so sensory cues without a change in delay should produce it, and short delays without cue-elicited appetite should not. Loewenstein cites the delay-of-gratification finding that a photograph of the reward helped children wait where the reward itself did not.
- **Tenet alignment**: This is the most congenial source for the value-sensitive horn, because it locates present-weighting in an occurrent felt state and offers a prediction that separates it from hyperbolic valuation. It is also phenomenality-neutral: Loewenstein's visceral factors are functionally specified drive states, and a mechanist takes them as they stand.

### Ainslie (2017), "De Gustibus Disputare: Hyperbolic delay discounting integrates five approaches to impulsive choice"
- **URL**: https://picoeconomics.org/HTarticles/Gustibus/Gustibus2.html (author-hosted HTML; journal version *Journal of Economic Methodology* 24(2), 166–189, doi 10.1080/1350178X.2017.1309373 per Crossref)
- **Type**: Paper (author-hosted text read; not checked against the journal's typeset version)
- **Key points**:
  - The reply available to the divided-will's leading rival. Ainslie argues that appetites and emotions are themselves reward-governed behaviours, so the visceral factors Loewenstein treats as exogenous fall under hyperbolic discounting of reward. **[verbatim]**: "Craving cannot be based on mere association--Something must be pulling it."
  - Abstract **[verbatim]**: "I suggest that the roles of all five phenomena follow from the hyperbolic discounting of expected reward".
  - He notes that the status of felt appetite is unsettled in psychology **[verbatim]**: "psychology has never worked out whether visceral responses such as appetites and emotions are intrinsic parts of the expectations that induce them, or are separable behaviors motivated by these expectations."
  - The text read does not discuss savouring, dread or Loewenstein (1987): a keyword count on the fetched page gives 0 for "savor", 0 for "Loewenstein", 1 for "dread" (in an unrelated quotation about idleness). Ainslie's treatment of anticipatory utility, if any, is elsewhere.
- **Tenet alignment**: Conflicts in spirit with the Map's selector (as the-divided-will already records). On this view the felt currency *is* hyperbolic, because feeling is a species of discounted reward, and that is a reduction of the felt currency rather than independent support for it.

### Hardisty & Weber (2020), "Impatience and Savoring vs. Dread"
- **URL**: https://doi.org/10.1002/jcpy.1169
- **Type**: Paper, *Journal of Consumer Psychology* 30(4), 598–613 **[abstract only]**
- **Key points** (from the abstract):
  - Anticipation of a positive event has two felt components that oppose each other. **[verbatim, abstract]**: "when consumers think about a future positive event, they both enjoy imagining it (savoring) while simultaneously disliking the feeling of waiting for it (impatience), but when consumers think about a negative event, they both dislike imagining it (dread) and dislike the feeling of waiting for it."
  - Net anticipatory utility is "strongly negative" for negative events and "weakly positive" for positive ones, hence **[verbatim, abstract]** "The desire for immediate positives is stronger than the desire to delay negatives."
- **Relevance**: Impatience, a felt aversive state attached to waiting, is the candidate felt source of present-weighting for rewards. The abstract gives no functional form.

### Iigaya, Story, Kurth-Nelson, Dolan & Dayan (2016), "The modulation of savouring by prediction error and its effects on choice"
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC4866828/
- **Type**: Paper, *eLife* 5, e13747 (PMC text read in part: abstract, introduction, model description)
- **Key points**:
  - Reinforcement-learning model in which anticipation is an appetitive quantity integrated over the waiting period, growing toward reward and itself temporally discounted, after Loewenstein (1987). Cue value is an inverted U in delay. **[verbatim]**: "this inverted U-shape was confirmed previously for the case of savoring, using hypothetical questionnaire studies".
  - Participants preferred advance information about reward more strongly at longer waits.
  - The modelling again uses exponential forms for both growth and discounting.
- **Follow-up**: Iigaya et al. (2020), *Science Advances* 6(25), eaba3828 **[abstract only]** reports that "ventromedial prefrontal cortex tracks the value of anticipatory utility". The mechanist therefore has a located neural variable for anticipatory utility and does not need a felt one.

### Caplin & Leahy (2001), "Psychological Expected Utility Theory and Anticipatory Feelings"
- **URL**: https://doi.org/10.1162/003355301556347
- **Type**: Paper, *Quarterly Journal of Economics* 116(1), 55–79 **[abstract only]**
- **Key point** **[verbatim, abstract]**: "We show how these anticipatory feelings may result in time inconsistency." This is the general theoretical statement of what Loewenstein (1987) shows for a special case: anticipatory feelings are sufficient for time inconsistency.

### Kim & Zauberman (2009), "Perception of Anticipatory Time in Temporal Discounting"
- **URL**: https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/2009-KIm-and-Zauberman-JNPE-vol2(2)-95-101.pdf
- **Type**: Paper, *Journal of Neuroscience, Psychology, and Economics* 2(2), 91–101 (abstract and opening read)
- **Key point**: A third locus for the hyperbola. **[verbatim, abstract]**: "diminishing sensitivity to longer time horizons ... and the level of time contraction overall ... contribute to the degree of hyperbolic discounting." If hyperbolicity lives in subjective time, then neither the felt value nor an outcome-valuation module need be hyperbolic; exponential feeling over logarithmically compressed felt duration would look hyperbolic in clock time. This is a phenomenological variable (how long a wait *seems*), which bears on the Map's question though the paper is not about feeling as currency.

### Supporting items
- **Grillon et al. (1993)**, *Psychophysiology* 30(4), 340–346 **[abstract only]**: fear-potentiated startle during a 45 s threat-of-shock period "became progressively larger in the threat condition the longer the light was on". A physiological index of anticipatory anxiety rising with proximity, over seconds; no functional form fitted.
- **McClure, Laibson, Loewenstein & Cohen (2004)**, *Science* 306(5695), 503–507 **[abstract only]**; already cited in the-divided-will as reference 1.
- **Kable & Glimcher (2007)**, *Nature Neuroscience* 10(12), 1625–1633 **[abstract only]**: activity in ventral striatum, medial prefrontal and posterior cingulate cortex "tracks the revealed subjective value of delayed monetary rewards". Whether that paper's fitted function is hyperbolic was not verified here.
- **Loewenstein, Weber, Hsee & Welch (2001)**, "Risk as feelings" **[abstract only; the available copy is an image-only scan]**. Already the Map's source for the anticipated/anticipatory distinction. Its discussion of fear intensifying as the moment of truth approaches is a lead that could not be quote-verified.
- **Frederick, Loewenstein & O'Donoghue (2002)**, "Time Discounting and Time Preference: A Critical Review", *Journal of Economic Literature* 40(2), 351–401 **[abstract only; image-only scan]**. The abstract's insistence on "distinguishing time preference, per se, from many other considerations that also influence intertemporal choices" is the methodological frame for this whole topic.
- **Loewenstein & Prelec (1993)**, "Preferences for sequences of outcomes", *Psychological Review* 100(1), 91–108 **[abstract only]**: preference for improving sequences when choices are framed as sequences.

## Major Positions

### Anticipatory utility (two-component value)
- **Proponents**: Loewenstein (1987), following Bentham and Jevons; Caplin & Leahy; Berns et al.; Story et al.; Iigaya et al.; Harris.
- **Core claim**: The present value of a delayed outcome is discounted consumption utility plus the utility felt while waiting. The second term reverses sign conventions that standard discounting predicts.
- **Key arguments**: Delayed kisses and expedited shocks; extreme dreaders paying in voltage to shorten the wait; value peaking at intermediate delay; reversal when a front-end delay is added.
- **Relation to site tenets**: This is the literature the value-sensitive horn of [[valence-and-conscious-selection]] should cite for the claim that a presently felt valence about a future outcome enters choice. It supplies structure and data. It does not supply phenomenality: every paper infers the anticipatory term from choice or BOLD signal, and Iigaya et al. (2020) assign it to vmPFC.

### Hyperbolic valuation of outcomes
- **Proponents**: Ainslie; Mazur; the behavioural-economics mainstream (quasi-hyperbolic variants: Laibson).
- **Core claim**: Value falls off with delay faster than exponentially near the present, which alone yields preference reversal as rewards approach.
- **Relation to anticipatory utility**: Standard hyperbolic discounting predicts that punishments are deferred and rewards advanced. Expedited pain and deferred kisses are anomalies for it. Ainslie (2017) can absorb felt appetite by making emotion a reward-seeking behaviour, at the cost of treating feeling as derivative.
- **Relation to site tenets**: This is the distributed rival's engine in the-divided-will. Nothing here weakens its claim to derive O1 and O3 for appetitive goods.

### Visceral factors
- **Proponent**: Loewenstein (1996).
- **Core claim**: Impulsivity tracks the intensity of occurrent felt drive states. Temporal proximity matters because, and only when, it elicits such a state.
- **Relation to site tenets**: Offers the value-sensitive horn a non-ad-hoc reason for present-weighting (only present feelings are felt) and a discriminating prediction (cue-dependence versus delay-dependence). Mechanism-sufficient readings remain available: incentive salience is the obvious one, and the Map's wanting/liking article already covers that fork.

### Subjective-time accounts
- **Proponents**: Kim & Zauberman (2009); related psychophysical work (Takahashi and colleagues, cited by Story et al., not reached).
- **Core claim**: Discounting may be exponential over perceived time, with hyperbolicity arising from compressive time perception.
- **Relation to site tenets**: Relocates the hyperbola into felt duration. Worth a paragraph because it is a third option the-divided-will's sentence overlooks.

## Key Debates

### Is the felt anticipatory quantity hyperbolic in delay?
- **Sides**: Nobody has argued either side with data on a felt measure. Models assume exponential rise (Loewenstein; Story; Iigaya) or constancy (Berns).
- **Core disagreement**: None joined. Story et al. say the dread-augmented value function is insensitive to the basic discount shape.
- **Current state**: Open and untested. The honest wording for the Map is "not shown", with the added point that the field's own models reach reversal without it.

### Does preference reversal need a hyperbolic currency at all?
- **Sides**: The-divided-will's sentence presupposes yes. Loewenstein (1987), Caplin & Leahy (2001) and Harris (2012) show no: anticipatory feeling generates time inconsistency with exponential components.
- **Core disagreement**: Which reversals. Anticipatory utility derives (a) repeated deferral of savoured goods and (b) taking worse-sooner pain when near but better-later pain when both are distant. Hyperbolic valuation derives (c) taking smaller-sooner reward when near. Akrasia as the Map discusses it is mostly (c).
- **Current state**: Each account derives the reversals the other must accommodate. Harris's data put (b) at the modal pattern and the hyperbolic-direction reversal for shocks at 6%, in one hypothetical-choice study.

### Does the feeling drive the choice?
- **Sides**: Berns et al. claim a link from "experienced disutility of dread" to decisions. Harris's Study 5 found self-estimated dread uncorrelated with timing choices (|r| no larger than .10).
- **Current state**: Unresolved. The neural correlate predicts choice between subjects; the self-report does not. Story et al.'s framing effect shows the dread term moves with description, which fits a constructed valuation as easily as a felt one.

### Visceral cue-dependence versus delay-dependence
- **Sides**: Loewenstein (1996) against the hyperbolic account; Ainslie (2017) absorbing visceral responses into discounted reward.
- **Current state**: Loewenstein's contrast is stated as a pair of differing predictions. This note did not locate a study that pits them against each other with delay held fixed and cue varied; that search is owed (see Gaps).

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1789 | Bentham, *Introduction to the Principles of Morals and Legislation* | Pleasures and pains of expectation counted among the ingredients of utility (as reported by Loewenstein 1987; not reached) |
| 1905 | Jevons, *Essays on Economics* | "Anticipal pleasure" and "anticipal pain"; introspective claim that intensity accelerates as the date nears (quoted in Loewenstein 1987; original not reached) |
| 1975 | Ainslie, "Specious reward" | Hyperbolic discounting and preference reversal (bibliographic entry in Loewenstein 1987; not reached) |
| 1987 | Loewenstein, "Anticipation and the Valuation of Delayed Consumption" | Savouring and dread formalised; exponential anticipation; reverse time inconsistency |
| 1996 | Loewenstein, "Out of Control" | Visceral factors as rival account of impulsivity; two stated limitations of hyperbolic discounting |
| 2001 | Caplin & Leahy; Loewenstein et al., "Risk as feelings" | Anticipatory feelings in expected-utility theory; anticipated versus anticipatory emotion |
| 2006 | Berns et al. | Neural correlate of dread; extreme dreaders accept more voltage to shorten the wait |
| 2012 | Harris | Dread-driven preference reversal as modal pattern; projected dread by temporal distance |
| 2013 | Story et al. | Dread rises toward the event; value peaks at intermediate delay in a minority; hyperbolic form explicitly set aside |
| 2016 | Iigaya et al. | Savouring boosted by prediction error; inverted-U cue value |
| 2017 | Ainslie, "De Gustibus Disputare" | Emotion and appetite folded into hyperbolically discounted reward |
| 2020 | Hardisty & Weber; Iigaya et al. | Savouring offset by impatience; vmPFC tracks anticipatory utility |

## Potential Article Angles

1. **Correct the test, then report the result (recommended).** The article's first move is that "shown to be hyperbolic" is the wrong demand: reversal needs a non-stationary currency, and a felt term that rises with proximity is non-stationary whatever its shape. It then reports that such a term exists in the literature, is modelled as exponential, and derives reversals. The verdict for the-divided-will is split. On aversive outcomes the felt-currency horn *derives* a datum (expedited dread, the Harris reversal) that hyperbolic outcome valuation only accommodates, which would be the first asymmetry in that article running the selector's way. On appetitive outcomes savouring points the wrong way, and the akratic reversal has to be carried by impatience or visceral craving, for which no curve has been measured. The article should say plainly that the favourable asymmetry concerns a felt *currency* and gives no support to a unitary *selector*: a distributed architecture with an anticipation term in vmPFC (Iigaya et al. 2020) inherits the same derivation. This aligns with Bidirectional Interaction only conditionally and with Occam's Razor Has Limits not at all; the article should not claim more.
2. **Three places the hyperbola could live.** Outcome valuation (Ainslie), felt drive state (Loewenstein 1996), felt duration (Kim & Zauberman). Structured as a locator article, with the Map's interest in the second and third because both are phenomenological variables. Risk: thinner evidence base, since the third is represented here by one paper read in part.
3. **Fold into existing articles instead of a new one.** The findings would fit as a paragraph in the-divided-will §accommodation plus a section in [[affective-forecasting-gap]] (which already draws the anticipated/anticipatory line). Worth pricing honestly: topics/ has headroom (343 files against a cap of 360 at time of writing), but the core result is one corrected sentence and two derived asymmetries. A standalone article is justified if it carries the visceral-versus-delay prediction and the measured-curve gap as its own content.

Whichever angle is taken, the-divided-will's sentence needs a follow-up edit. Suggested direction: replace "independently shown to be hyperbolic" with a requirement that the felt currency be independently shown to be present-weighted in the akratic direction, and record that the anticipatory-utility literature shows present-weighting for dread and the opposite for savouring.

When writing the article, follow `obsidian/project/writing-style.md` for:
- Named-anchor summary technique for forward references
- Background vs. novelty decisions (skip the general exposition of hyperbolic discounting; the-divided-will has it)
- Tenet alignment requirements
- LLM optimization (front-load the corrected test and the split verdict)

Calibration notes for the writer:
- Every study here infers the anticipatory term from choice or from BOLD signal, apart from Harris Study 5, which collects forecasts about hypothetical dread. None measures occurrent felt valence. Do not write "the felt currency has been shown to be exponential"; the supportable claim is that it has been *modelled* as exponential and the form left untested.
- Sample sizes are small (30; 32; 25 and 30) or hypothetical-choice internet samples (193; 304). Harris's modal-reversal result is one study.
- Loewenstein (1987) quotations come from an OCR layer; re-check against a clean copy before publishing any that this note marks whitespace-normalised.
- Expedited pain is a majority pattern in these samples for shocks, and is not general across negative outcomes: money and property losses are mostly postponed (Harris abstract; Loewenstein 1987 survey).

## Gaps in Research

- **No functional-form test on a felt measure was found.** One extended search aimed at exactly this returned nothing on point. Absence is reported for the searches run and is not a claim that no such study exists; experience-sampling and psychophysiology literatures (startle, skin conductance over longer delays) were not searched systematically.
- **Cue-versus-delay experiments** testing Loewenstein's (1996) contrast were not searched. Delay-of-gratification work (Mischel) is the obvious place; only Loewenstein's summary of it was read.
- **Not reached**: Frederick, Loewenstein & O'Donoghue (2002) and Loewenstein et al. (2001) beyond abstracts (image-only scans, no OCR tool available); Loewenstein & Prelec (1991) "Negative time preference"; Elster & Loewenstein (1992) "Utility from memory and anticipation"; Hardisty & Weber (2020) full text, including how anticipatory feelings were measured; the 2004 reprint of "Out of Control"; Ainslie's *Breakdown of Will* on emotion as reward, and whether Ainslie anywhere addresses savouring and dread directly.
- **Philosophical literature not covered.** The research found no Stanford Encyclopedia entry on time bias at the URL tried, and did not search PhilPapers. Parfit on bias toward the near and the recent time-bias literature (Sullivan; Greene & Sullivan; Dougherty) are untouched and are leads only. The article will lean on economics and psychology unless a further pass is made.
- **Kable & Glimcher (2007)**: whether the tracked subjective value is specifically hyperbolic was not verified at source.
- **Jevons and Bentham** are quoted only as Loewenstein quotes them.
- **Dawson & Johnson (2026)**, "Asymmetric Anticipatory Emotions and Economic Preferences", *Cognitive Science* 50(1), e70160, surfaced in an OpenAlex search with an abstract linking stronger dread-over-savouring asymmetry to impatience. Metadata and abstract come from OpenAlex only and were not checked at the publisher; treat as a lead.

## Citations

1. Ainslie, G. (2017). De gustibus disputare: Hyperbolic delay discounting integrates five approaches to impulsive choice. *Journal of Economic Methodology*, 24(2), 166–189. https://doi.org/10.1080/1350178X.2017.1309373 (read at https://picoeconomics.org/HTarticles/Gustibus/Gustibus2.html)
2. Berns, G. S., Chappelow, J., Cekic, M., Zink, C. F., Pagnoni, G., & Martin-Skurski, M. E. (2006). Neurobiological substrates of dread. *Science*, 312(5774), 754–758. https://doi.org/10.1126/science.1123721 (read at https://pmc.ncbi.nlm.nih.gov/articles/PMC1820741/)
3. Caplin, A., & Leahy, J. (2001). Psychological expected utility theory and anticipatory feelings. *Quarterly Journal of Economics*, 116(1), 55–79. https://doi.org/10.1162/003355301556347
4. Frederick, S., Loewenstein, G., & O'Donoghue, T. (2002). Time discounting and time preference: A critical review. *Journal of Economic Literature*, 40(2), 351–401. https://doi.org/10.1257/002205102320161311
5. Grillon, C., Ameli, R., Merikangas, K., Woods, S. W., & Davis, M. (1993). Measuring the time course of anticipatory anxiety using the fear-potentiated startle reflex. *Psychophysiology*, 30(4), 340–346. https://doi.org/10.1111/j.1469-8986.1993.tb02055.x
6. Hardisty, D. J., & Weber, E. U. (2020). Impatience and savoring vs. dread: Asymmetries in anticipation explain consumer time preferences for positive vs. negative events. *Journal of Consumer Psychology*, 30(4), 598–613. https://doi.org/10.1002/jcpy.1169
7. Harris, C. R. (2012). Feelings of dread and intertemporal choice. *Journal of Behavioral Decision Making*, 25(1), 13–28. https://doi.org/10.1002/bdm.709 (read at https://charris.ucsd.edu/articles/Harris_JBDM2010.pdf)
8. Iigaya, K., Story, G. W., Kurth-Nelson, Z., Dolan, R. J., & Dayan, P. (2016). The modulation of savouring by prediction error and its effects on choice. *eLife*, 5, e13747. https://doi.org/10.7554/eLife.13747
9. Iigaya, K., Hauser, T. U., Kurth-Nelson, Z., O'Doherty, J. P., Dayan, P., & Dolan, R. J. (2020). The value of what's to come: Neural mechanisms coupling prediction error and the utility of anticipation. *Science Advances*, 6(25), eaba3828. https://doi.org/10.1126/sciadv.aba3828
10. Kable, J. W., & Glimcher, P. W. (2007). The neural correlates of subjective value during intertemporal choice. *Nature Neuroscience*, 10(12), 1625–1633. https://doi.org/10.1038/nn2007
11. Kim, B. K., & Zauberman, G. (2009). Perception of anticipatory time in temporal discounting. *Journal of Neuroscience, Psychology, and Economics*, 2(2), 91–101. https://doi.org/10.1037/a0017686
12. Loewenstein, G. (1987). Anticipation and the valuation of delayed consumption. *The Economic Journal*, 97(387), 666–684. https://doi.org/10.2307/2232929
13. Loewenstein, G. (1996). Out of control: Visceral influences on behavior. *Organizational Behavior and Human Decision Processes*, 65(3), 272–292. https://doi.org/10.1006/obhd.1996.0028 (reprinted 2004 as ch. 26 of *Advances in Behavioral Economics*, Princeton University Press, https://doi.org/10.1515/9781400829118-029)
14. Loewenstein, G., & Prelec, D. (1993). Preferences for sequences of outcomes. *Psychological Review*, 100(1), 91–108. https://doi.org/10.1037/0033-295X.100.1.91
15. Loewenstein, G. F., Weber, E. U., Hsee, C. K., & Welch, N. (2001). Risk as feelings. *Psychological Bulletin*, 127(2), 267–286. https://doi.org/10.1037/0033-2909.127.2.267
16. McClure, S. M., Laibson, D. I., Loewenstein, G., & Cohen, J. D. (2004). Separate neural systems value immediate and delayed monetary rewards. *Science*, 306(5695), 503–507. https://doi.org/10.1126/science.1100907
17. Story, G. W., Vlaev, I., Seymour, B., Winston, J. S., Darzi, A., & Dolan, R. J. (2013). Dread and the disvalue of future pain. *PLoS Computational Biology*, 9(11), e1003335. https://doi.org/10.1371/journal.pcbi.1003335
