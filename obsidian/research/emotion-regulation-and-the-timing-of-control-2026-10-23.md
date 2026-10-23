---
title: "Research Notes - Emotion Regulation and the Timing of Control"
created: 2026-10-23
modified: 2026-10-23
human_modified: null
ai_modified: 2026-10-23T20:23:40+00:00
draft: false
description: "Research notes on where in an emotion's time course regulation acts: Gross's process model, the antecedent/response split, its timing tests and revisions, implicit regulation, and what that leaves the Map's selector."
topics:
  - "[[alief-and-acting-against-belief]]"
  - "[[emotion-and-dualism]]"
  - "[[immediate-emotions-and-the-affect-heuristic]]"
  - "[[clinical-neuroplasticity-evidence-for-bidirectional-causation]]"
  - "[[valence-as-a-natural-kind]]"
concepts:
  - "[[self-control-as-skill-and-scaffolding]]"
  - "[[control-theoretic-will]]"
  - "[[mental-effort]]"
  - "[[skill-delegation]]"
  - "[[content-specificity-of-mental-causation]]"
  - "[[epiphenomenalism]]"
related_articles:
  - "[[tenets]]"
  - "[[numbing-void]]"
  - "[[stapp-quantum-mind]]"
  - "[[positions/agency-and-will]]"
  - "[[research/self-control-as-skill-and-scaffolding-2026-10-04]]"
  - "[[research/alief-and-acting-against-what-one-believes-2026-10-20]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-23
last_curated: null
recommended_action: article
target_section: topics
target_slug: emotion-regulation-and-the-timing-of-control
---

# Research: Emotion Regulation and the Timing of Control

**Date**: 2026-10-23
**Origin**: P3 queue task (research-harvest 2026-10-23), from `reviews/optimistic-2026-10-22-location-wing`, New-Territory Candidate 2 and its High Priority entry "Emotion regulation and where control enters". Driver brief 19:53Z.

**Routes used**:
- Crossref API for metadata on every DOI below (66 DOIs resolved, rechecked after drafting; none failed).
- NCBI PubMed `efetch` raw abstracts for every paper marked [V-abs] that PubMed indexes (40 papers).
- The OpenAlex `abstract_inverted_index` for papers PubMed does not index: Gross 1998 (*RGP*), Gross 2015, Gross & Barrett 2011, Kappas 2011, Torre & Lieberman 2018, Mauss, Bunge & Gross 2007, Gross & Muñoz 1995, Uusberg et al. 2019, Ford & Troy 2019, Hiekkaranta et al. 2023, Levy-Gigi & Shamay-Tsoory 2022, and the five philosophy papers.
- Full text, read as raw text:
  - NCBI PMC `efetch` XML: Gross & Barrett 2011 (PMC3072688); Gyurak, Gross & Etkin 2011 (PMC3280343); Williams et al. 2009 (PMC2796590); Duckworth, Gendler & Gross 2016 (PMC4736542).
  - Europe PMC XML: Braunstein, Gross & Ochsner 2017 (PMC5647798).
  - PMC article HTML: Goldin et al. 2008 (PMC2483789); Schwartz, Stapp & Beauregard 2005 (PMC1569494).
  - `pdftotext` on PDFs: Gross & John 2003 (journal PDF on a University of Victoria course site; the APA header, DOI and page range match); Webb, Schweiger Gallo, Miles, Gollwitzer & Sheeran 2012 (*ERSP*; the authors' Taylor & Francis download copy, hosted at Konstanz).
  - Seneca, *De Ira* II: Aubrey Stewart's 1900 translation (Wikisource raw wikitext) and the Latin text (The Latin Library).
- Two PMC pages (Buhle et al. 2014; Beauregard et al. 2001) returned a captcha, so those two are abstract-only.
- WebSearch, for leads only (5 calls): the Gross & John PDF; the Webb et al. 2012 meta-analysis full text (not found open; Sussex copy embargoed); philosophy of emotion regulation; 2023–2025 meta-analyses; nothing else.
- OpenAlex forward search: works citing Sheppes & Gross 2011 with "timing" or "temporal" in the title, 2019 on (5 hits); reappraisal meta-analyses 2017 on (42 hits, mostly off-topic).

**Search queries used**:
- Crossref bibliographic: Kerr "rationality of emotion regulation"; *Philosophical Topics* emotion regulation (Glazer); Colombetti & Krueger "Scaffoldings of the affective mind"; Sorabji *Emotion and Peace of Mind*.
- WebSearch: `Gross John 2003 "Individual differences in two emotion regulation processes" pdf`; `Webb Miles Sheeran 2012 "Dealing with feeling" situation selection ... pdf`; `philosophy of emotion regulation agency voluntary control ...`; `2023 OR 2024 OR 2025 meta-analysis emotion regulation strategies reappraisal suppression distraction ...`.
- Wikisource API: `Of Anger Seneca`.

**Verification tags**:
- **[V-full]**: the full text was read as raw text and every quoted span greps there.
- **[V-abs]**: the abstract was read as raw text and every quoted span greps there.
- **[AS-QUOTED-IN X]**: the words were read only inside source X's raw text.
- **[META]**: Crossref metadata only; the content has not been read.
- **[LEAD]**: unverified, from a search summary or a secondary citation.

Every quoted span in this note was checked by script against the raw source text or the Map page it comes from. There were two passes, whitespace-normalised only, and no quote-mark normalisation was needed:
- 147 spans listed by hand before drafting;
- an extraction pass over the finished note, in which 275 unique quoted spans matched. The unmatched remainder are article titles, section headings and this note's own recommended or forbidden wording.

The passes caught two slips, now fixed: a capitalised "Late" at the head of a Sheppes & Meiran span, and the hyphen case below. In the Gross & John 2003 PDF, "emotion-generative" breaks across a line ("emotion- generative" in the text layer). The hyphen belongs to the compound, so the note prints it as one word.

## Executive Summary

**The process model is a map of *where*, and the article should treat it as such.**
- Gross (1998, *Review of General Psychology*) says "emotion may be regulated at five points in the emotion generative process: (a) selection of the situation, (b) modification of the situation, (c) deployment of attention, (d) change of cognitions, and (e) modulation of responses".
- Gross (1998, *JPSP*) adds the coarser cut: "a distinction between antecedent-focused and response-focused emotion regulation is proposed."
- Gross & John (2003) define the two halves by timing. Antecedent-focused strategies come "before the emotion response tendencies have become fully activated"; response-focused strategies come "once an emotion is already underway".

**The model's own authors revised "earlier is easier" into a narrower claim.**
- Sheppes & Gross (2011) name the original reading the "generic timing hypothesis": down-regulating emotions before they are "up and running" "is always easier".
- They replace it with a "process-specific timing hypothesis". Early-stage strategies "require minimal effort", and late-stage strategies "require effort that is proportional to the intensity of the emotional response".
- Effectiveness does not track stage order. In Webb, Miles & Sheeran's (2012) meta-analysis of 306 experimental comparisons, attentional deployment pooled at d+ = 0.00, response modulation at 0.16 and cognitive change at 0.36. "There were also important within-process differences": distraction worked (0.27) and concentration did not (−0.26).

**Timing has been measured within single episodes, and a strategy's family label does not fix when it acts.**
- In Goldin et al. (2008; 17 women, disgust films), reappraisal produced "early (0-4.5 sec)" prefrontal responses and lower amygdala and insula responses. Suppression produced "late (10.5-15 sec)" prefrontal responses and higher amygdala and insula responses.
- In EEG, distraction cut the late positive potential "earlier than reappraisal" (Thiruchselvam et al. 2011).
- But "expressive suppression affected emotional responding as early as distraction" (Paul et al. 2013). The authors read this as suppression being "used preventively".
- Initiation time matters for reappraisal specifically. Distraction "was effective even when initiated late", whereas late reappraisal was less effective, "suggesting a possible point of no return for this strategy" (Sheppes & Meiran 2007).

**Regulation does not require a conscious contribution at any stage.**
- Implicit emotion regulation is "any process that operates without the need for conscious supervision or explicit intentions" (Koole & Rothermund 2011).
- Gyurak, Gross & Etkin (2011) give an uninstructed laboratory case, emotional conflict adaptation, which "proceeds without awareness".
- Braunstein, Gross & Ochsner (2017) separate two orthogonal axes: whether the *goal* is conscious, and whether the *change process* is controlled or automatic. A conscious goal can be served by an automatic process.
- **This cuts against any "consciousness does the regulating" reading, and the article must say so plainly.** It does not show that consciousness is idle where it is present ([Guards](#guards)).

**The timing frame presupposes a distinction some emotion theorists deny.**
- Gross & Barrett (2011) arrange theories on a continuum and find that toward the constructionist end "the conceptual separation of emotion generation and emotion regulation becomes increasingly suspect."
- Kappas (2011): "For all practical purposes unregulated emotion is not a realistic concept."
- If there is no prior emotion for regulation to act on, "where does control enter?" needs restating. The article must flag this.

**The Map is already committed to a reading of one reappraisal experiment without having said so.**
- Schwartz, Stapp & Beauregard (2005), cited on about fifteen Map pages for the quantum Zeno mechanism, use Ochsner et al.'s (2002) reappraisal experiment as their worked example.
- They write: "In the experiments of Ochsner the effort of the subject to ‘reappraise’ causes the ‘reappraise’ template to be held in place and the holding in place of this template causes the suppression of the limbic response."
- No live Map page names Ochsner (0 hits). A calibrated page on reappraisal's timing is therefore owed. The neural route Buhle et al.'s (2014) meta-analysis gives runs through "semantic representations" and lateral temporal cortex, with no experiential term.

**Where the Map could locate a conscious contribution, and what that location is worth.**
- The regulation literature itself puts explicit control at three points:
  - the *goal* (Braunstein's explicit end);
  - the extended process model's *identification* and *selection* stages, which decide whether to regulate and which strategy to use (Gross 2015);
  - policy moments made before the episode: situation selection and if-then plans for emotion. Implementation-intention instructions pooled at d+ = 0.91 against no instruction (Webb, Schweiger Gallo et al. 2012).
- This matches the [[self-control-as-skill-and-scaffolding|self-control page]]'s "moments of policy" and the [[alief-and-acting-against-belief#noticing-condition|alief page's noticing condition]].
- **It is fit, not evidence.** Every stage is modelled without an experiential term (regulation as valuation, Gross 2015; Etkin, Büchel & Gross 2015), and every stage has an implicit form.

**A precedent two thousand years old.** Seneca (*De Ira* 2.4.1) splits anger's onset into three *motus*:
1. the first "is involuntary" (*non uoluntarius*);
2. the next "is combined with a wish, though not an obstinate one";
3. the third "is already beyond our control, because it overrides reason".

That is a timing-of-control thesis, and it anticipates Sheppes & Meiran's "point of no return". It is precedent only. The Stoic doctrine concerns assent and must not be mapped onto Gross's stages one to one.

## Verdict: article, not fold {#verdict}

Assessed under the licence to decline.

- **Fold into `concepts/self-control-as-skill-and-scaffolding`: rejected on measurement and on focus.**
  - The page stands at 2,998/3,500 (`analyze_length`, 19:53Z), so headroom is 501. It is already past the concepts soft limit (2,500).
  - The material needs about 2,300–2,700 body words:
    1. the five families and the antecedent/response cut;
    2. the within-episode timing studies;
    3. the generic-to-process-specific revision and the effectiveness record;
    4. implicit regulation and the goal/process axes;
    5. the generation/regulation dispute;
    6. the Map's placement, with the Stapp worked example calibrated.
  - A fold would also move that page off its subject, which is the conflict between judgement and desire and its resolution in action. Its emotion-relevant sentences (L46 on Duckworth, Gendler & Gross 2016; L72 on hot/cool) are correct where they stand. It needs one pointer sentence ([Integration](#integration)).
- **Fold into `topics/emotion-and-dualism`** (3,350/4,000, headroom 649): rejected. It is a general survey of emotion under dualism, and the timing analysis would need roughly four times its headroom.
- **Fold into `topics/alief-and-acting-against-belief`** (3,317/4,000, headroom 682): rejected. Alief is a state type and regulation is a family of operations, so a fold would replace that page's question with this one's.
- **No other single host fits.** The material bears on at least nine pages across three sections. Spread across them it would arrive as asides, with no page holding the timing analysis the asides would point to.
- **Decline (`none`): considered and rejected.**
  - The gap is real. "expressive suppression", "antecedent-focused", "response-focused", "response modulation", "situation selection", "Sheppes", "Webb, Miles", "Gross & John", "Ochsner", "implicit emotion regulation" and "extended process model" give 0 live hits ([Coverage](#coverage)).
  - The Map meets emotion regulation only in passing (4 live pages, none treating it).
  - It is already committed, through Schwartz, Stapp & Beauregard 2005, to a quantum-Zeno reading of a reappraisal experiment it never discusses.
  - The sources are verifiable: 10 read in full, about 45 by abstract.
  - The subject gives the Map's location question its finest temporal grain (seconds within one episode, where the self-control literature works at hours and days). It also supplies the literature's own correction of the "earlier is better" intuition, which a Map writer would otherwise be tempted to read as support for a low-bandwidth selector.
- **Duplication check.** The article must not redo:
  - the self-control page's "moments of policy" argument (it cross-links it instead);
  - the affect-heuristic page's reappraisal-and-risk studies (Heilman et al. 2010 and Morawetz et al. 2019 stay there);
  - the numbing void's proactive down-regulation (Cameron & Payne 2011 stays there, cited once as a field instance).
- **Section and slug.**
  - `count_section_files`, 19:53Z: topics 363/370 (the function over-counts by one sidecar), concepts 364/370. Topics is the home, beside `alief-and-acting-against-belief` and `immediate-emotions-and-the-affect-heuristic`.
  - `check_slug.py emotion-regulation-and-the-timing-of-control topics`: OK. The alternative `emotion-regulation-and-where-control-enters` is also free.
  - Suggested title: "Emotion Regulation and the Timing of Control: Where a Conscious Contribution Could Enter".

## Coverage on the Map (scoped) {#coverage}

These are case-insensitive fixed-string file counts, run 2026-10-23 at 19:54Z. "Live" means obsidian `topics/ concepts/ apex/ voids/ positions/ tenets/`, with `.refinement-log` sidecars excluded. "Research" means `research/`.

| String | Live | Research | Note |
|---|---|---|---|
| "emotion regulation" | 4 | 4 | all passing: `immediate-emotions…` L93 (a search-vocabulary list), `neuroplasticity` L107 (a gloss on Weng et al. 2013), `numbing-void` L56/L100/L113 (Cameron & Payne), `dissociative-subtype-of-ptsd` L146 (a reference title) |
| "reappraisal" | 1 | 4 | `mental-effort` L106, "Effortful cognitive reappraisal engages prefrontal regulatory circuits" (see [Side-findings](#side-findings)) |
| "cognitive reappraisal" | 1 | 1 | the same sentence |
| "expressive suppression", "antecedent-focused", "antecedent focused", "response-focused", "response modulation", "situation selection", "Gross (1998)", "Gross 1998", "Gross & John", "Gross and John", "Sheppes", "Webb, Miles", "Gyurak", "Koole", "Rothermund", "Etkin", "implicit emotion regulation", "automatic emotion regulation", "regulatory choice", "regulatory flexibility", "extended process model", "Bonanno", "Lazarus" | 0 each | 0 each (except "situation selection": research 1, the self-control note's absence count) | |
| "Ochsner" | 0 | 1 | the alief note lists Ochsner & Gross 2005 [meta] |
| "situation modification" | 1 | 1 | `self-control…` L46, quoting Duckworth et al. |
| "attentional deployment" | 4 | 1 | none in Gross's sense: `valence-and-conscious-selection` L159, `agent-causation` L125, `retrocausality` L103 (attention timing), `synesthetic-void` L113 |
| "cognitive change" | 2 | 3 | none in Gross's sense |
| "down-regulat" | 5 | 2 | meditation and cessation pages, plus `numbing-void` |
| "affect labeling" | 1 | 0 | `emotion-and-dualism` L212, a reference with no body citation (see [Side-findings](#side-findings)) |
| "Gross, J" | 2 | 2 | `self-control…` (Duckworth et al. 2016, two papers) |
| "process model" | 9 | 14 | Inzlicht/Kurzban effort models and others, none Gross's |
| "Beauregard" | 16 | 11 | 15 of 16 are Schwartz, Stapp & Beauregard 2005; one is Beauregard & Paquette 2006 (`ineffable-encounter-void`) |
| "appraisal" | 20 | 17 | mostly appraisal theory of emotion (Lerner & Keltner etc.), not regulation |

**Positive controls.**
- "self-control" gives live 21 and research 24 (the review counted 20/23 at 02:37Z; one page of each has been added since).
- "Duckworth" gives live 10.
- "amygdala" gives live 32.
- "Inzlicht" gives live 7.

So the search reaches the self-control, effort and affective-neuroscience corpus, and the process-model literature is absent from it.

**Map apparatus the article must use, not duplicate:**
- [[self-control-as-skill-and-scaffolding#where-selection-sits|Where Selection Sits]]:
  - L86: "Ordinary success moves to moments of policy (choosing a situation, forming an if-then plan, adopting a rule), each made while the temptation is weak or absent." It adds the Dretske structuring-cause reading (added 2026-10-23).
  - L88: "The fit discriminates nothing."
- [[alief-and-acting-against-belief#noticing-condition|The Noticing Condition]], L113: "Effort can appear where the rival guide is noticed and checked; where interference goes unseen there is nothing to feel."
- [[control-theoretic-will]]:
  - L74, stabilisation: "The effort required scales with the disturbance magnitude".
  - L76–L82, veto, including the Map's own statement of Tenet 2: "The bit-cost of veto is a bandwidth fact, not the minimality [[tenets#^minimal-quantum-interaction|Tenet 2]] names, which the tenet fixes by the empirical record it must respect (no detectable energy injection, no Born or conservation violation), not by how much is influenced".
- [[numbing-void]]:
  - L56: Cameron & Payne's people regulate "proactively, by preventing themselves from ever experiencing as much emotion toward groups as toward individuals".
  - L100 reads the case as "an illustration, not an instance" of Tenet 3.
- [[clinical-neuroplasticity-evidence-for-bidirectional-causation]]: "the clinical findings are compatible with both interpretations, and the data do not adjudicate between them". Its three streams are down-counted to one preferential signature.
- [[content-specificity-of-mental-causation]]: the observation "stated at the strength the data carry".
- [[positions/agency-and-will#^p-a4|P-A4]]: "no agent can certify its own causal efficacy by introspection".

## The Process Model and Its Timing Claim {#process-model}

**Five families, ordered by first point of action.** Gross (1998, *RGP*) characterises emotion "in terms of response tendencies". It defines the field as the study of "how individuals influence which emotions they have, when they have them, and how they experience and express them". The five points run along the situation → attention → appraisal → response sequence, and McRae & Gross (2020) call them "5 families of strategies defined by when they impact the emotion generation process".

| Family | Example strategies | Antecedent or response? | Where it first acts |
|---|---|---|---|
| Situation selection | avoiding or approaching a situation | antecedent | before the situation is met |
| Situation modification | changing the situation's features | antecedent | in the situation, before attention |
| Attentional deployment | distraction, concentration | antecedent | on what is attended |
| Cognitive change | reappraisal (reconstrual, repurposing), distancing | antecedent | on the appraisal |
| Response modulation | expressive suppression, other response control | response | on the response once generated |

**The antecedent/response cut** (Gross & John 2003, [V-full]):
- "Antecedent-focused strategies refer to things we do before the emotion response tendencies have become fully activated and have changed our behavior and peripheral physiological responding."
- "Response-focused strategies refer to things we do once an emotion is already underway, after the response tendencies have already been generated."
- Webb, Schweiger Gallo et al. (2012, [V-full]) put it as "Antecedent-focused processes occur before appraisals give rise to a full-blown emotional response."

**The timing rationale, in the authors' words** (Gross & John 2003):
- Reappraisal "occurs early, and intervenes before the emotion response tendencies have been fully generated".
- Suppression "comes relatively late in the emotion-generative process, and primarily modifies the behavioral aspect of the emotion response tendencies".
- "because suppression comes late in the emotion-generative process, it requires the individual to effortfully manage emotion response tendencies as they continually arise".

**Gross & John scope their own evidence.** Their five ERQ studies "do not address causal claims or the specific temporal ordering of reappraisal and suppression postulated by our model." The trait (ERQ) literature therefore says nothing about timing. Timing claims must rest on the experimental and neural studies.

**The extended process model.**
- Gross (2015, [V-abs]) recasts regulation: "this model considers emotion regulation to be one type of valuation, and distinguishes three emotion regulation stages (identification, selection, implementation)".
- McRae & Gross (2020, [V-abs]) add monitoring: "a need for regulation is identified, a strategy is selected and implemented, and monitoring occurs to track success".
- This gives the regulatory act its own time course, nested inside the emotion's. **For the Map's question these are the two clocks to keep apart**:
  1. *when in the emotion* a strategy acts (the five families);
  2. *which stage of the regulatory decision* is in play (identification, selection, implementation, monitoring).
- Gross (2015) also warns that "enthusiasm for this topic continues to outstrip conceptual clarity".

**Cycles, not a line.** Duckworth, Gendler & Gross (2016, [V-full]) carry the model over to self-control and note that it iterates. A plan made "in an earlier cycle" can beat a situational move in a later one: "rules and plans formulated well in advance of encounters with temptation may trump situational strategies deployed in later cycles of impulse generation". Timing is relative to the cycle as well as to the stage.

## Key Sources {#key-sources}

### A. The process model and its revisions

#### Gross, J. J. (1998a). "The Emerging Field of Emotion Regulation: An Integrative Review." *Review of General Psychology* 2(3): 271–299. DOI 10.1037/1089-2680.2.3.271 [V-abs, OpenAlex]
- The source of the five-point model (quoted above).
- Body not read.
- **Labels:** sources disagree on "1998a/1998b". Webb, Schweiger Gallo et al. 2012 use 1998a for this paper and 1998b for the *JPSP* paper. The *JPSP* paper appeared first (January, against September). Cite both by journal.
- **Tenet alignment**: neutral. A functional, evolutionary framing.

#### Gross, J. J. (1998b). "Antecedent- and response-focused emotion regulation: Divergent consequences for experience, expression, and physiology." *JPSP* 74(1): 224–237. DOI 10.1037/0022-3514.74.1.224 [V-abs]
- The 120-participant disgust-film experiment.
- Instructions: reappraisal, to "think about the film in such a way that they would feel nothing"; suppression, to "behave in such a way that someone watching them would not know they were feeling anything"; or watch.
- Result: both reduced expressive behaviour; "reappraisal decreased disgust experience, whereas suppression increased sympathetic activation".
- **Tenet alignment**: neutral.

#### Gross, J. J., & John, O. P. (2003). "Individual differences in two emotion regulation processes: Implications for affect, relationships, and well-being." *JPSP* 85(2): 348–362. DOI 10.1037/0022-3514.85.2.348 [V-full]
- The ERQ. Key items: "I control my emotions by changing the way I think about the situation I’m in" (reappraisal); "I control my emotions by not expressing them" (suppression).
- Results: habitual reappraisal goes with more positive and less negative emotion, better interpersonal functioning and well-being; suppression goes the other way (abstract).
- **Its own scope sentence** (above) disclaims causal and timing claims.
- **Tenet alignment**: neutral.

#### Gross, J. J. (2015). "Emotion Regulation: Current Status and Future Prospects." *Psychological Inquiry* 26(1): 1–26. DOI 10.1080/1047840X.2014.940781 [V-abs, OpenAlex]
- The extended process model: valuation; identification, selection, implementation.
- Body not read. Do not quote the stage definitions beyond the abstract.

#### McRae, K., & Gross, J. J. (2020). "Emotion regulation." *Emotion* 20(1): 1–9. DOI 10.1037/emo0000703 [V-abs]
- Adds monitoring.
- "Reappraisal is thought to be generally effective and adaptive, but there are important qualifications."

#### Sheppes, G., & Gross, J. J. (2011). "Is Timing Everything? Temporal Considerations in Emotion Regulation." *Personality and Social Psychology Review* 15(4): 319–331. DOI 10.1177/1088868310395778 [V-abs]
- **The central paper for this article.**
- It names the process model's original assumption: down-regulating emotions before they are "up and running" "is always easier than down-regulating emotions once they have gathered force (i.e., generic timing hypothesis)".
- It proposes instead a "process-specific timing hypothesis, in which emotion-generative and emotion-regulatory processes compete at either earlier or later stages of information processing".
  - "Regulation strategies that target early processing stages require minimal effort." Their efficacy should be "relatively unaffected by emotion intensity".
  - Late-stage strategies "require effort that is proportional to the intensity of the emotional response".
- Body not read.
- **Tenet alignment**: neutral. A competition model between two information-processing streams.

#### Duckworth, A. L., Gendler, T. S., & Gross, J. J. (2016). "Situational Strategies for Self-Control." *Perspectives on Psychological Science* 11(1): 35–55. DOI 10.1177/1745691615623247 [V-full, PMC4736542]
- "Readers familiar with the process model of emotion regulation will recognize this theoretical framework", which they "expand here to include other types of conflicts".
- Abstract: "the full range of self-control strategies can be organized by considering the timeline of the developing tempting impulse".
- Their prescriptive claim: "as a rule, earlier intervention is best". Also "This framework predicts that situational strategies should be more effective than intrapsychic strategies because they are deployed earlier in the process of impulse generation."
- **Note:** this is the generic timing hypothesis carried into self-control *after* Sheppes & Gross (2011) narrowed it for emotion. The article should notice the asymmetry and not resolve it.
- Already cited on the Map (`self-control…` L46, abstract only).

### B. Timing studies (within an episode)

#### Goldin, P. R., McRae, K., Ramel, W., & Gross, J. J. (2008). "The Neural Bases of Emotion Regulation: Reappraisal and Suppression of Negative Emotion." *Biological Psychiatry* 63(6): 577–586. DOI 10.1016/j.biopsych.2007.05.031 [V-full, PMC2483789]
- 17 women; 15 s disgust films; four conditions.
- "Reappraisal resulted in early (0-4.5 sec) prefrontal cortex (PFC) responses, decreased negative emotion experience, and decreased amygdala and insular responses."
- "Suppression produced late (10.5-15 sec) PFC responses, decreased negative emotion behavior and experience, but increased amygdala and insular responses."
- Limitations, theirs: "the study sample included only women"; "emotion experience ratings were collected during fMRI only after each 15s film clip"; small sample.
- **Note:** suppression *decreased* reported experience here, against Gross & Levenson 1993 and Kalokerinos et al. 2015 (below). Do not state "suppression leaves experience unchanged" as settled.
- **Tenet alignment**: neutral. Pre-2020, single-site fMRI, so pair it with Buhle et al. 2014 and Morawetz et al. 2017 (citation-aging rule).

#### Thiruchselvam, R., Blechert, J., Sheppes, G., Rydstrom, A., & Gross, J. J. (2011). "The temporal dynamics of emotion regulation: An EEG study of distraction and reappraisal." *Biological Psychology* 87(1): 84–92. DOI 10.1016/j.biopsycho.2011.02.009 [V-abs]
- "distraction reduced the late positive potential (LPP) earlier than reappraisal".
- On re-exposure, "images with a distraction (but not reappraisal) history elicited a larger LPP than images with an attend history". Distraction's early block has a later cost.

#### Paul, S., Simon, D., Kniesche, R., Kathmann, N., & Endrass, T. (2013). "Timing effects of antecedent- and response-focused emotion regulation strategies." *Biological Psychology* 94(1): 136–142. DOI 10.1016/j.biopsycho.2013.05.019 [V-abs]
- All strategies reduced the LPP and self-reported negative affect. "Surprisingly, expressive suppression affected emotional responding as early as distraction."
- Authors' reading: "suppression was used preventively and disrupted the emotion-generative process from the very beginning instead of targeting the emotional response itself". They stress "the importance of considering the point in time when response-focused emotion regulation strategies are being implemented".
- **This is the key result for the location question.** "Response-focused" names a target, and when the strategy acts is a separate, empirical matter.

#### Sheppes, G., & Meiran, N. (2007). "Better Late Than Never? On the Dynamics of Online Regulation of Sadness Using Distraction and Cognitive Reappraisal." *PSPB* 33(11): 1518–1532. DOI 10.1177/0146167207305537 [V-abs]
- Initiation point manipulated within sad films.
- "Distraction was effective even when initiated late". By contrast, "reappraisal was less effective when initiated late, suggesting a possible point of no return for this strategy".

#### Sheppes, G., & Meiran, N. (2008). "Divergent cognitive costs for online forms of reappraisal and distraction." *Emotion* 8(6): 870–874. DOI 10.1037/a0013711 [V-abs]
- Late initiation revealed "for the first time a cognitive cost for reappraisal": "late reappraisal, relative to distraction, resulted in an expenditure of self control resources".
- **Flag:** "self control resources" is the ego-depletion construct ([Evidence not to lean on](#not-to-lean-on)). Its memory-encoding result ("Late distraction but not reappraisal impaired memory encoding") is the safer half.

#### Levy-Gigi, E., & Shamay-Tsoory, S. (2022). "Affect labeling: The role of timing and intensity." *PLOS ONE* 17(12): e0279303. DOI 10.1371/journal.pone.0279303 [V-abs, OpenAlex]
- Experiment 1 (n = 63): "We found that affect labeling efficiently down-regulated distress independent of the labeling timing" (simultaneous, immediately after, or 10 s after).
- Experiment 2 (n = 79): "while affect labeling reduces distress in high-intensity aversive conditions, it increases distress in low-intensity conditions".
- A second result against any generic timing rule.

#### Gross, J. J., & Levenson, R. W. (1993). "Emotional suppression: Physiology, self-report, and expressive behavior." *JPSP* 64(6): 970–986. DOI 10.1037/0022-3514.64.6.970 [V-abs]
- Defines suppression as "the conscious inhibition of emotional expressive behavior while emotionally aroused". The word "conscious" is in the definition.
- 85 participants. "Suppression had no impact on the subjective experience of emotion."

### C. Effectiveness and its moderators

#### Webb, T. L., Miles, E., & Sheeran, P. (2012). "Dealing with feeling: A meta-analysis of the effectiveness of strategies derived from the process model of emotion regulation." *Psychological Bulletin* 138(4): 775–808. DOI 10.1037/a0027600 [V-abs]
- The reappraisal meta-analysis the brief names. 306 experimental comparisons.
- "Attentional deployment had no effect on emotional outcomes (d(+) = 0.00), response modulation had a small effect (d(+) = 0.16), and cognitive change had a small-to-medium effect (d(+) = 0.36)."
- Within processes:
  - "Whereas distraction was an effective way to regulate emotions (d(+) = 0.27), concentration was not (d(+) = -0.26)."
  - "suppressing the expression of emotion proved effective (d(+) = 0.32), but suppressing the experience of emotion or suppressing thoughts of the emotion-eliciting event did not".
  - "reappraising the emotional response proved less effective (d(+) = 0.23) than reappraising the emotional stimulus (d(+) = 0.36) or using perspective taking (d(+) = 0.45)".
- **Scope**: the abstract pools attentional deployment, cognitive change and response modulation only. Whether situation selection or modification were meta-analysed was not checked (body not read; the Sussex copy is embargoed). A comment exists (*Psychol Bull* 139(3): 725–9, DOI 10.1037/a0030026), not read.
- **Tenet alignment**: neutral.

#### Webb, T. L., Schweiger Gallo, I., Miles, E., Gollwitzer, P. M., & Sheeran, P. (2012). "Effective regulation of affect: An action control perspective on emotion regulation." *European Review of Social Psychology* 23(1): 143–186. DOI 10.1080/10463283.2012.718134 [V-full, authors' download copy]
- Meta-analysis of implementation intentions for emotional outcomes:
  - k = 21, N = 1,306, d+ = 0.91 against no instructions;
  - k = 29, N = 1,208, d+ = 0.53 against goal-intention instructions.
- The PDF text layer renders "=" as "¼" and "d+" as "dþ". Transcribe the numbers; do not quote the glyphs.
- **Bridge:** this is the emotion-domain counterpart to the self-control page's Gollwitzer and Sheeran et al. figures, and the clearest evidence that a *policy moment* made before the episode regulates the episode.

#### Sheppes, G., Scheibe, S., Suri, G., & Gross, J. J. (2011). "Emotion-Regulation Choice." *Psychological Science* 22(11): 1391–1396. DOI 10.1177/0956797611418350 [V-abs]
- Three experiments. Low intensity → preference for "engagement reappraisal, which allows emotional processing". High intensity → preference for "disengagement distraction, which blocks emotional processing at an early stage before it gathers force".

#### Sheppes, G., Scheibe, S., Suri, G., Radu, P., Blechert, J., & Gross, J. J. (2014). "Emotion regulation choice: A conceptual framework and supporting evidence." *JEP: General* 143(1): 163–181. DOI 10.1037/a0030831 [V-abs]
- Six studies. "healthy adaptation requires flexibly choosing between regulation strategies in a manner that is responsive to differing situational demands".

#### Troy, A. S., Shallcross, A. J., & Mauss, I. B. (2013). "A Person-by-Situation Approach to Emotion Regulation: Cognitive Reappraisal Can Either Help or Hurt, Depending on the Context." *Psychological Science* 24(12): 2505–2514. DOI 10.1177/0956797613496434 [V-abs; erratum 2016]
- n = 170. "reappraisal may be adaptive when stressors are uncontrollable (when the person can regulate only the self) but maladaptive when stressors can be controlled (when the person can change the situation)".
- **Bearing:** where the situation can be changed, the earlier family (situation modification) is the apt one, and the later family (cognitive change) can harm. Correlational.

#### Bonanno, G. A., & Burton, C. L. (2013). "Regulatory Flexibility: An Individual Differences Perspective on Coping and Emotion Regulation." *Perspectives on Psychological Science* 8(6): 591–612. DOI 10.1177/1745691613504116 [V-abs]
- Coins "the fallacy of uniform efficacy": the assumption "that particular regulatory strategies are consistently beneficial or maladaptive".

#### Ford, B. Q., & Troy, A. S. (2019). "Reappraisal Reconsidered: A Closer Look at the Costs of an Acclaimed Emotion-Regulation Strategy." *Current Directions in Psychological Science* 28(2): 195–203. DOI 10.1177/0963721419827526 [V-abs, OpenAlex]
- "people are often unable to use reappraisal successfully, and second, even when successful, using reappraisal to feel better is not always functional".

#### Uusberg, A., Taxer, J. L., Yih, J., Uusberg, H., & Gross, J. J. (2019). "Reappraising Reappraisal." *Emotion Review* 11(4): 267–282. DOI 10.1177/1754073919862617 [V-abs, OpenAlex]
- Reappraisal works by shifting appraisal outcomes, "either by changing the construal ( reconstrual) or by changing the goal set ( repurposing)". The spaces before the closing words are in the OpenAlex text.

#### Wang, K., Goldenberg, A., Dorison, C. A., et al. (2021). "A multi-country test of brief reappraisal interventions on emotions during the COVID-19 pandemic." *Nature Human Behaviour* 5(8): 1089–1110. DOI 10.1038/s41562-021-01173-x [V-abs; erratum 2022; volume and pages confirmed at Crossref]
- "Participants from 87 countries and regions (n = 21,644)". Both reappraisal interventions reduced negative and increased positive emotion against both controls. "Reconstrual and repurposing interventions had similar effects."
- The largest test of reappraisal's *efficacy*. It says nothing about timing.
- **Do not quote** the abstract sentence containing "vesus" (a typo in the source).

#### Kalokerinos, E. K., Greenaway, K. H., & Denson, T. F. (2015). "Reappraisal but not suppression downregulates the experience of positive and negative emotion." *Emotion* 15(3): 271–275. DOI 10.1037/emo0000025 [V-abs]
- Over 1,300 participants. "Suppression did not reduce the experience of either positive or negative emotion relative to the control condition."

#### Richards, J. M., & Gross, J. J. (2000). "Emotion regulation and memory: The cognitive costs of keeping one's cool." *JPSP* 79(3): 410–424. DOI 10.1037/0022-3514.79.3.410 [V-abs]
- "Only suppression led to poorer slide memory."

#### Butler, E. A., Egloff, B., Wilhelm, F. H., Smith, N. C., Erickson, E. A., & Gross, J. J. (2003). "The social consequences of expressive suppression." *Emotion* 3(1): 48–67. DOI 10.1037/1528-3542.3.1.48 [V-abs]
- "Suppression also reduced rapport and inhibited relationship formation."
- Crossref misspells "Wilhelm" as "Wlhelm".

#### Soto, J. A., Perez, C. R., Kim, Y.-H., Lee, E. A., & Minnick, M. R. (2011). "Is expressive suppression always associated with poorer psychological functioning? A cross-cultural comparison between European Americans and Hong Kong Chinese." *Emotion* 11(6): 1450–1455. DOI 10.1037/a0023340 [V-abs]
- "expressive suppression was associated with adverse psychological functioning for European Americans, but not for Chinese participants" (n = 71 and 100).

#### Chen, M. S., Cai, Q., Omari, D., Sanghvi, D. E., Lyu, S., & Bonanno, G. A. (2025). "Emotion regulation and mental health across cultures: a systematic review and meta-analysis." *Nature Human Behaviour* 9(6): 1176–1200. DOI 10.1038/s41562-025-02168-8 [V-abs]
- "249 articles, n = 150,474, 861 effect sizes, 37 countries/regions".
- Cultural moderation of both strategies' associations. Correlational, so it says nothing about timing.

#### Aldao, A., Nolen-Hoeksema, S., & Schweizer, S. (2010). "Emotion-regulation strategies across psychopathology: A meta-analytic review." *Clinical Psychology Review* 30(2): 217–237. DOI 10.1016/j.cpr.2009.11.004 [V-abs]
- 114 studies. Rumination largest; suppression medium to large; reappraisal small to medium. "These results are surprising, given the prominence of reappraisal and acceptance in treatment models".

#### Brans, K., Koval, P., Verduyn, P., Lim, Y. L., & Kuppens, P. (2013). "The regulation of negative and positive affect in daily life." *Emotion* 13(5): 926–939. DOI 10.1037/a0032400 [V-abs]
- Experience sampling (N = 46, 95). Use ordering: "distraction being used more than sharing and reappraisal". Suppression and rumination went with increased negative affect.

#### Hiekkaranta, A. P., Kirtley, O. J., Eisele, G., Houben, M., Lafit, G., & Myin-Germeys, I. (2023). "Time to reappraise or distract? temporal and situational context in emotion regulation in daily life." *Current Psychology*. DOI 10.1007/s12144-023-05233-5 [V-abs, OpenAlex]
- N = 74. Its "temporal context" is *clock* time: "Time of day and weekday were not associated with reappraisal or distraction use".
- **Do not use it for within-episode timing.** It is listed here so that a later writer who meets the title does not mistake it for one.

### D. Implicit and automatic regulation

#### Koole, S. L., & Rothermund, K. (2011). "'I feel better but I don't know why': The psychology of implicit emotion regulation." *Cognition and Emotion* 25(3): 389–399. DOI 10.1080/02699931.2010.550505 [V-abs]
- Definition: "Implicit emotion regulation can be broadly defined as any process that operates without the need for conscious supervision or explicit intentions, and aims at modifying the quality, intensity, or duration of an emotional response."
- "Implicit emotion regulation is likely to be pervasive in everyday life". Note the hedge "likely".
- Special-issue editorial.

#### Gyurak, A., Gross, J. J., & Etkin, A. (2011). "Explicit and implicit emotion regulation: A dual-process framework." *Cognition and Emotion* 25(3): 400–412. DOI 10.1080/02699931.2010.544160 [V-full, PMC3280343]
- Definitions:
  - "we define explicit emotion regulation as those processes that require conscious effort for initiation and demand some level of monitoring during implementation, and are associated with some level of insight and awareness";
  - "Implicit processes are believed to be evoked automatically by the stimulus itself and run to completion without monitoring and can happen without insight and awareness".
- Boundaries: "explicit/implicit regulation are not mutually exclusive categories, but rather have porous boundaries".
- The emotional-conflict case (Etkin et al. 2006) fits because "the process is uninstructed, effortless and proceeds without awareness". They add that "despite careful probing, participants do not report any awareness of the key processes of the task" (citing Etkin et al. 2010, not read).
- Their open questions:
  - "it is less clear whether deploying and executing regulation without awareness can have similar benefits";
  - "We also expect future research to assess whether understanding the temporal unfolding of an emotional response will help conceptually organize implicit emotion regulation in the way that it has for explicit regulation".
- **Bearing:** the timing framework was built for explicit regulation, and whether it organises implicit regulation is, for these authors, open.

#### Braunstein, L. M., Gross, J. J., & Ochsner, K. N. (2017). "Explicit and implicit emotion regulation: a multi-level framework." *SCAN* 12(10): 1545–1557. DOI 10.1093/scan/nsx096 [V-full, PMC5647798]
- Two orthogonal dimensions: "(i) the nature of the emotion regulation goal (ranging from implicit/nonconscious to explicit/conscious) and (ii) the nature of the emotion change process (ranging from more automatic to more controlled)". Four classes result.
- "Explicit emotion regulation goals involve a conscious desire to change one’s emotions", whereas "implicit goals do not involve the conscious desire to change emotional responding".
- On primed regulation: "Although no imaging studies have examined primed emotion regulation". That holds as of 2017, theirs.
- **The most useful framework for the article.** It separates *whether the goal is conscious* from *whether the process is controlled*. That lets the Map place a possible contribution at the goal without claiming the change process.

#### Mauss, I. B., Bunge, S. A., & Gross, J. J. (2007). "Automatic Emotion Regulation." *Social and Personality Psychology Compass* 1(1): 146–167. DOI 10.1111/j.1751-9004.2007.00005.x [V-abs, OpenAlex]
- "AER is pervasive in everyday life", per their review. But "the behavioral literature has yet to address the mechanisms underlying the observed effects".

#### Torre, J. B., & Lieberman, M. D. (2018). "Putting Feelings Into Words: Affect Labeling as Implicit Emotion Regulation." *Emotion Review* 10(2): 116–124. DOI 10.1177/1754073917742706 [V-abs, OpenAlex]
- "affect labeling may not even feel like a regulatory process as it occurs".
- The review's argument: its effects resemble explicit regulation across experiential, autonomic, neural and behavioural domains.

#### Lieberman, M. D., Eisenberger, N. I., Crockett, M. J., Tom, S. M., Pfeifer, J. H., & Way, B. M. (2007). "Putting Feelings Into Words: Affect Labeling Disrupts Amygdala Activity in Response to Affective Stimuli." *Psychological Science* 18(5): 421–428. DOI 10.1111/j.1467-9280.2007.01916.x [V-abs]
- Labelling diminished amygdala response, with a proposed RVLPFC → MPFC → amygdala pathway.
- Already in `emotion-and-dualism`'s references, with no body citation.

#### Etkin, A., Egner, T., Peraza, D. M., Kandel, E. R., & Hirsch, J. (2006). "Resolving Emotional Conflict." *Neuron* 51(6): 871–882. DOI 10.1016/j.neuron.2006.07.029 [V-abs]
- Conflict resolution is associated with rostral ACC activation and "a simultaneous and correlated reduction of amygdalar activity".

#### Williams, L. E., Bargh, J. A., Nocera, C. C., & Gray, J. R. (2009). "The unconscious regulation of emotion: Nonconscious reappraisal goals modulate emotional reactivity." *Emotion* 9(6): 847–854. DOI 10.1037/a0017745 [V-full, PMC2796590]
- A scrambled-sentence prime of a reappraisal goal "achieved the same decrease in physiological reactivity as those explicitly instructed to reappraise" (heart rate).
- Experiment 1 had "Thirty-nine undergraduates" across three conditions. Funnel debriefing found no suspicion.
- **Flag:** small cells, and a goal-priming method from a literature with replication problems ([Evidence not to lean on](#not-to-lean-on)).

#### Mauss, I. B., Cook, C. L., & Gross, J. J. (2007). "Automatic emotion regulation during anger provocation." *JESP* 43(5): 698–711. DOI 10.1016/j.jesp.2006.07.003 [META; content AS-QUOTED-IN Gyurak et al. 2011 and Braunstein et al. 2017]
- Gyurak et al. summarise it: priming control tendencies "seemed to confer similar benefits during anger provocation".

#### Koole, S. L., Webb, T. L., & Sheeran, P. L. (2015). "Implicit emotion regulation: feeling better without knowing why." *Current Opinion in Psychology* 3: 6–10. DOI 10.1016/j.copsyc.2014.12.027 [META]

### E. Generation versus regulation

#### Gross, J. J., & Feldman Barrett, L. (2011). "Emotion Generation and Emotion Regulation: One or Two Depends on Your Point of View." *Emotion Review* 3(1): 8–16. DOI 10.1177/1754073910380974 [V-full, PMC3072688]
- "Emotion regulation has the odd distinction of being a wildly popular construct whose scientific existence is in considerable doubt."
- The continuum runs basic emotion → appraisal → psychological construction → social construction: "as we move from left to right along the continuum, the conceptual separation of emotion generation and emotion regulation becomes increasingly suspect".
- "In the psychological construction portion of the conceptual terrain, it is increasingly difficult to distinguish emotion generation from emotion regulation."
- **Co-authored by Gross and Barrett**, the process model's author and constructionism's leading proponent. Neither concedes the other's view. The paper is a map of perspectives, not a verdict.

#### Gross, J. J., Sheppes, G., & Urry, H. L. (2011). *Cognition and Emotion* 25(5): 765–781. DOI 10.1080/02699931.2011.555753 [V-abs]
- **Title anomaly:** Crossref, PubMed, Europe PMC and OpenAlex all give the title as "Cognition and Emotion Lecture at the 2010 SPSP Emotion Preconference". The article's working title, "Emotion generation and emotion regulation: A distinction we should make (carefully)", is from memory and appears in none of those records: [LEAD]. Cite by DOI, and give the working title only if it is confirmed.
- Commentaries: Mesquita & Frijda, "An emotion perspective on emotion regulation" (25(5): 782–784, DOI 10.1080/02699931.2011.586824) [META]; Kappas, "Emotion is not just an alarm bell—it's the whole tootin' fire truck" (785–788, DOI 10.1080/02699931.2011.587641) [META].
- "This distinction fits comfortably with folk theories, which view emotions as passions that arise unbidden and then must be controlled."
- Their verdict: "in some circumstances, the distinction between emotion generation and emotion regulation is indeed useful".

#### Kappas, A. (2011). "Emotion and Regulation are One!" *Emotion Review* 3(1): 17–25. DOI 10.1177/1754073910380971 [V-abs, OpenAlex]
- "emotions are not just regulated—they regulate". "For all practical purposes unregulated emotion is not a realistic concept."

### F. Neural accounts

#### Ochsner, K. N., Bunge, S. A., Gross, J. J., & Gabrieli, J. D. E. (2002). "Rethinking Feelings: An fMRI Study of the Cognitive Regulation of Emotion." *Journal of Cognitive Neuroscience* 14(8): 1215–1229. DOI 10.1162/089892902760807212 [V-abs]
- "Neural correlates of reappraisal were increased activation of the lateral and medial prefrontal regions and decreased activation of the amygdala and medial orbito-frontal cortex."
- **This is the experiment Schwartz, Stapp & Beauregard (2005) model** (§G).

#### Ochsner, K. N., & Gross, J. J. (2005). "The cognitive control of emotion." *Trends in Cognitive Sciences* 9(5): 242–249. DOI 10.1016/j.tics.2005.03.010 [V-abs]
- "These two forms of emotion regulation depend upon interactions between prefrontal and cingulate control systems and cortical and subcortical emotion-generative systems."
- Upgrades the alief note's [meta] entry.

#### Buhle, J. T., Silvers, J. A., Wager, T. D., et al. (2014). "Cognitive Reappraisal of Emotion: A Meta-Analysis of Human Neuroimaging Studies." *Cerebral Cortex* 24(11): 2981–2990. DOI 10.1093/cercor/bht154 [V-abs; Crossref "issued" 2013, online first]
- 48 studies. "Reappraisal consistently 1) activated cognitive control regions and lateral temporal cortex, but not vmPFC, and 2) modulated the bilateral amygdala, but no other brain regions."
- Reading: "reappraisal involves the use of cognitive control to modulate semantic representations of an emotional stimulus".

#### Morawetz, C., Bode, S., Derntl, B., & Heekeren, H. R. (2017). "The effect of strategies, goals and stimulus material on the neural mechanisms of emotion regulation: A meta-analysis of fMRI studies." *Neuroscience & Biobehavioral Reviews* 72: 111–128. DOI 10.1016/j.neubiorev.2016.11.014 [V-abs; volume and pages confirmed at Crossref]
- "The left ventrolateral prefrontal cortex (VLPFC), the anterior insula and the supplementary motor area were consistently activated independent of the regulation strategy."
- **Bearing:** localisation does not cleanly separate strategies, so timing claims should rest on time-resolved designs (Goldin; Thiruchselvam; Paul), not on which regions light up.

#### Etkin, A., Büchel, C., & Gross, J. J. (2015). "The neural bases of emotion regulation." *Nature Reviews Neuroscience* 16(11): 693–700. DOI 10.1038/nrn4044 [V-abs]
- "Drawing on computational approaches to value-based decision-making and reinforcement learning, we propose a unifying conceptual framework".

#### Braunstein et al. 2017 (above) also reviews the neural bases by class.

### G. Dualist-leaning readings already in the Map's bibliography

#### Schwartz, J. M., Stapp, H. P., & Beauregard, M. (2005). "Quantum physics in neuroscience and psychology: a neurophysical model of mind–brain interaction." *Phil. Trans. R. Soc. B* 360(1458): 1309–1327. DOI 10.1098/rstb.2004.1598 [V-full, PMC1569494 HTML]
- Cited on about fifteen Map pages.
- The paper lists "self-directed regulation of emotional response, via cognitive reframing and attentional re-contextualization mechanisms" studies, including Beauregard et al. 2001, Ochsner et al. 2002 and Lévesque et al. 2003.
- It then applies its quantum Zeno model to Ochsner et al. (2002): "In the experiments of Ochsner the effort of the subject to ‘reappraise’ causes the ‘reappraise’ template to be held in place and the holding in place of this template causes the suppression of the limbic response."
- The abstract's thesis: "Contemporary physical theory brings directly and irreducibly into the overall causal structure certain psychologically described choices made by human agents about how they will act."
- **Author stance**: explicitly interactionist (Stapp's von Neumann framework). One of the few sources in this note that argues for a non-physical-causal reading.

#### Beauregard, M., Lévesque, J., & Bourgouin, P. (2001). "Neural Correlates of Conscious Self-Regulation of Emotion." *Journal of Neuroscience* 21(18): RC165. DOI 10.1523/JNEUROSCI.21-18-j0001.2001 [V-abs]
- Inhibition of sexual arousal to erotic film excerpts, in male participants. The abstract's interpretive sentence: the findings "suggest that humans have the capacity to influence the electrochemical dynamics of their brains, by voluntarily changing the nature of the mind processes unfolding in the psychological space".

#### Beauregard, M. (2007). "Mind does really matter: Evidence from neuroimaging studies of emotional self-regulation, psychotherapy, and placebo effect." *Progress in Neurobiology* 81(4): 218–236. DOI 10.1016/j.pneurobio.2007.01.005 [V-abs]
- The findings "strongly support the view that the subjective nature and the intentional content (what they are "about" from a first-person perspective) of mental processes (e.g., thoughts, feelings, beliefs, volition) significantly influence the various levels of brain functioning".
- Proposes a "Psychoneural Translation Hypothesis".
- **Author stance**: non-materialist. Report it as his interpretation, never as what the neuroimaging shows.

### H. Philosophy and history

#### Seneca, *De Ira* II.2–4. Aubrey Stewart's translation, *Minor Dialogs* (Bohn's Classical Library, 1900), via Wikisource ("Of Anger/Book II"); Latin via The Latin Library [V-full for 2.2–2.4]
- 2.2: anger "if it springs up against our will, it never will yield to reason: because all the motions which take place without our volition are beyond our control and unavoidable".
- 2.3: "the mind, if I may so express it, rather suffers passions to act upon itself than forms them". He also says "no impulse can take place without the consent of the mind".
- 2.4.1 (Latin): "est primus motus non uoluntarius, quasi praeparatio adfectus et quaedam comminatio … tertius motus est iam inpotens".
- Stewart's English:
  - "the first emotion is involuntary, and is, as it were, a preparation for a passion, and a threatening of one";
  - "The next is combined with a wish, though not an obstinate one";
  - "The third emotion is already beyond our control, because it overrides reason".
- 2.4.2: of the first impressions, "Reason is unable to overcome these habits, which perhaps might be weakened by practice and constant watchfulness".
- **Translation note**: Stewart renders *motus* as "emotion". "Movement" is closer, and the article should give the Latin.
- **Tenet alignment**: Stoic psychology is corporealist. Seneca is no dualist ally.

#### Sorabji, R. (2000). *Emotion and Peace of Mind*. Oxford University Press. DOI 10.1093/acprof:oso/9780199256600.001.0001 (Oxford Scholarship Online, 2002) [META]
- The standard modern treatment of the Stoic "first movements" (from general knowledge; not read). Cite only for the existence of the scholarly discussion. Its subtitle is not in the Crossref or OpenAlex records, so do not supply one.

#### Kerr, D. (2021). "On the rationality of emotion regulation." *Philosophical Psychology* 34(4): 453–473. DOI 10.1080/09515089.2021.1915969 [V-abs, OpenAlex]
- "If an agent feels an emotion that is obviously problematic for the agent to feel and she is aware that it is problematic, then the agent ought to regulate her emotions in future similar situations."
- The obligation he states is diachronic and runs through awareness.

#### Madjar, S. (2020). "Emotion regulation and evaluative understanding." *Philosophical Psychology* 33(6): 777–798. DOI 10.1080/09515089.2020.1751102 [V-abs, OpenAlex]
- Distinguishes "engaged forms of emotion regulation which keep us engaged with our emotional concern" from disengaging forms. This is the philosophical counterpart of Sheppes's engagement/disengagement.

#### Glazer, T. (2021). "Emotion regulation and cooperation." *Philosophical Psychology* 34(8): 1125–1145. DOI 10.1080/09515089.2021.1942812 [V-abs, OpenAlex]
- Treats "emotion regulation skills, or abilities to intervene on and manage one’s emotions in real time".

#### Colombetti, G., & Krueger, J. (2015). "Scaffoldings of the affective mind." *Philosophical Psychology* 28(8): 1157–1176. DOI 10.1080/09515089.2014.976334 [V-abs, OpenAlex; Crossref "issued" 2014, online first]
- "human affectivity (and not just cognition) is environmentally supported".
- The scaffolding counterpart of situation selection and modification.

#### Archer, A., & Mills, G. (2019). "Anger, Affective Injustice, and Emotion Regulation." *Philosophical Topics* 47(2): 75–94. DOI 10.5840/philtopics201947216 [V-abs, OpenAlex]
- In the 2019 *Philosophical Topics* issue on emotion regulation (with Maibom, "Empathy and Emotion Regulation", 149–163 [META]). Out of scope except as evidence that a philosophical literature exists.

### I. Ego depletion (for the flag only)

#### Baumeister, R. F., Bratslavsky, E., Muraven, M., & Tice, D. M. (1998). "Ego depletion: Is the active self a limited resource?" *JPSP* 74(5): 1252–1265. DOI 10.1037/0022-3514.74.5.1252 [V-abs]
- "In Experiment 3, suppressing emotion led to a subsequent drop in performance of solvable anagrams."

#### Hagger, M. S., Chatzisarantis, N. L. D., et al. (2016). "A Multilab Preregistered Replication of the Ego-Depletion Effect." *Perspectives on Psychological Science* 11(4): 546–573. DOI 10.1177/1745691616652873 [V-abs]
- k = 23, total N = 2,141. Effect "d = 0.04, 95% CI [-0.07, 0.15]".
- The protocol was "based on a sequential-task paradigm by Sripada et al.", an attention task, not emotion suppression. The replication therefore does not directly test the suppression version.

### J. Metadata or leads only

- Gross, J. J., & Muñoz, R. F. (1995). "Emotion regulation and mental health." *Clinical Psychology: Science and Practice* 2(2): 151–164. DOI 10.1111/j.1468-2850.1995.tb00036.x [V-abs, OpenAlex]. Whether it states the antecedent/response distinction before Gross (1998b) was not checked.
- Aldao, A., Sheppes, G., & Gross, J. J. (2015). "Emotion Regulation Flexibility." *Cognitive Therapy and Research* 39(3): 263–278. DOI 10.1007/s10608-014-9662-4 [META]
- Ochsner, K. N., Silvers, J. A., & Buhle, J. T. (2012). "Functional imaging studies of emotion regulation: a synthetic review and evolving model of the cognitive control of emotion." *Annals of the New York Academy of Sciences* 1251: E1–E24. DOI 10.1111/j.1749-6632.2012.06751.x [META]
- Lévesque et al. (2003) and Paquette et al. (2003): [AS-QUOTED-IN Schwartz, Stapp & Beauregard 2005] only.
- Gross & Thompson (2007), *Handbook of Emotion Regulation* chapter: cited by Webb, Schweiger Gallo et al. and Gyurak et al. Not looked up.
- Graver, M. (2007). *Stoicism and Emotion*: [LEAD], from general knowledge.

## What the Timing Evidence Shows {#timing-evidence}

Four claims are licensed. Each is scoped to the sources above.

1. **Strategies differ in when they first change the emotional response, and this is measurable within seconds.**
   - fMRI: early versus late prefrontal recruitment for reappraisal versus suppression (Goldin et al. 2008; n = 17, women, disgust).
   - EEG: distraction reduces the LPP before reappraisal (Thiruchselvam et al. 2011).
2. **A family label does not fix the time of action.**
   - Suppression can act as early as distraction when used preventively (Paul et al. 2013).
   - Cycles mean a cognitive-change plan made in advance can precede a situational move (Duckworth et al. 2016).
   - The article should treat the five families as *targets* (situation, attention, appraisal, response). When a given instance acts is an empirical question.
3. **Earlier is not uniformly easier or better.**
   - The process model's authors narrowed the generic timing hypothesis to a process-specific one (Sheppes & Gross 2011).
   - Late *distraction* still works, and late *reappraisal* loses efficacy (Sheppes & Meiran 2007).
   - Affect labelling worked at all three timings tested (Levy-Gigi & Shamay-Tsoory 2022).
   - Pooled effectiveness does not follow stage order (Webb et al. 2012: attentional deployment 0.00, response modulation 0.16, cognitive change 0.36).
   - Context reverses verdicts: controllable versus uncontrollable stress (Troy et al. 2013); culture (Soto et al. 2011; Chen et al. 2025); intensity (Sheppes et al. 2011; Levy-Gigi & Shamay-Tsoory 2022). Bonanno & Burton's "fallacy of uniform efficacy" names the error.
4. **What is robust about late regulation is its cost profile, not its timing as such.**
   - Expressive suppression usually leaves reported experience unchanged (Gross & Levenson 1993; Kalokerinos et al. 2015; Webb et al. 2012's "suppressing the experience" and "suppressing thoughts" nulls). Goldin et al. 2008 is the exception here.
   - It impairs memory for the episode (Richards & Gross 2000).
   - It has social costs (Butler et al. 2003).
   - The physiological result is mixed: increased sympathetic activation in Gross 1998b, a "mixed physiological state" in Gross & Levenson 1993.

**What the record does not show:**
- that situation selection or modification is the most effective family for *emotion* (no pooled estimate was found here; see [Gaps](#gaps));
- that early regulation needs fewer or smaller *interventions* in any sense that bears on Tenet 2;
- anything about consciousness. Every study above is consistent with an entirely physical valuation-and-control architecture, and several are framed in one (Gross 2015; Etkin, Büchel & Gross 2015; Sheppes & Gross 2011).

## Major Positions {#positions}

### The process model (Gross; Sheppes; McRae; Ochsner)
- **Core claim**: regulation is goal-directed influence on an emotion-generative sequence, and strategies are typed by where in that sequence they act. The extended model adds a regulatory valuation cycle (identification, selection, implementation, monitoring).
- **Key arguments**: the timing studies; the strategy-specific effectiveness record; neural dissociations.
- **Relation to tenets**: neutral. A functional decomposition with no experiential term. It gives the Map a set of *locations* and no evidence about what occupies them.

### Implicit and dual-process regulation (Koole & Rothermund; Gyurak, Gross & Etkin; Mauss; Braunstein, Gross & Ochsner)
- **Core claim**: much regulation runs without conscious goals or monitoring. Explicit and implicit forms have porous boundaries, and goal consciousness and process control vary independently.
- **Relation to tenets**: the strongest local pressure on any "consciousness regulates emotion" reading. It does not touch the Map's commitment, which never needed consciousness at every stage. It does constrain the article's register.

### Constructionism about emotion (Barrett, as represented in Gross & Barrett 2011; Kappas 2011 on auto-regulation)
- **Core claim**: emotions are continually constructed, so there is no prior emotion for a separate regulator to act on, and the generation/regulation split is perspectival.
- **Relation to tenets**: the Map has engaged constructionism on valence ([[valence-as-a-natural-kind]]). Here it bites on the *framing*: "when does control enter?" presupposes something to enter. The article must state which side of the continuum its timing talk assumes, and that the question survives on a weakened, perspectival distinction (Gross, Sheppes & Urry 2011).

### Regulation as evidence of mental causation (Beauregard; Schwartz, Stapp & Beauregard)
- **Core claim**: neuroimaging of voluntary regulation shows mental content influencing brain function, and quantum theory supplies the mechanism.
- **Relation to tenets**: aligned with Tenets 2 and 3 in aspiration. On the Map's own calibration ([[clinical-neuroplasticity-evidence-for-bidirectional-causation]]) the data "do not adjudicate". The neural route has a physical description (Buhle et al. 2014), and the Zeno account is a posit.

### Regulatory flexibility (Bonanno & Burton; Aldao, Sheppes & Gross; Troy; Ford & Troy)
- **Core claim**: no strategy is good or bad as such. Adaptiveness depends on fit to context.
- **Relation to tenets**: neutral. Its bearing here is a warning against reading "reappraisal good, suppression bad" as a fact about early versus late.

### Philosophers of emotion regulation (Kerr; Madjar; Glazer; Colombetti & Krueger; Archer & Mills)
- **Core claim**: various normative and phenomenological theses (rationality, evaluative understanding, cooperation, scaffolding, injustice).
- **Relation to tenets**: none engages the metaphysics of mind. Kerr's diachronic "ought" and Colombetti & Krueger's scaffolding are the two the article could use.

## Key Debates {#debates}

### 1. Is earlier always easier?
- **Sides**: the generic timing hypothesis (the process model's original rationale; Duckworth et al. 2016 for self-control: "as a rule, earlier intervention is best") against the process-specific hypothesis (Sheppes & Gross 2011), plus findings that do not order by stage (Webb et al. 2012; Levy-Gigi & Shamay-Tsoory 2022).
- **Current state**: for emotion, the process model's authors have narrowed it. For self-control, the same group stated the generic form five years later. Unresolved, and the article should present both without picking.

### 2. Does suppression reduce experience?
- **Sides**: no (Gross & Levenson 1993; Gross 1998b on disgust; Kalokerinos et al. 2015, n > 1,300; Webb et al. 2012 for suppressing experience or thoughts). Yes, in one fMRI sample (Goldin et al. 2008).
- **Current state**: mostly no for *expressive* suppression's effect on felt experience, with exceptions. Write "usually leaves reported experience unchanged".

### 3. Are generation and regulation distinct?
- **Sides**: distinct where useful (Gross, Sheppes & Urry 2011); perspectival (Gross & Barrett 2011); one process (Kappas 2011).
- **Current state**: ongoing.

### 4. Is implicit regulation as effective as explicit regulation?
- **Sides**: primed reappraisal equals instructed reappraisal on heart rate (Williams et al. 2009, small). For Gyurak et al., "it is less clear".
- **Current state**: open, and the priming evidence is weak.

### 5. Is suppression's cost a resource drain?
- **Sides**: depletion readings (Baumeister et al. 1998, Experiment 3; Sheppes & Meiran 2008's "self control resources") against the failed multi-lab replication of the depletion effect (Hagger et al. 2016, with a different task).
- **Current state**: do not adopt a resource reading. The memory and social costs stand without it.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| c. 41–49 CE | Seneca, *De Ira* II.2–4 | Three *motus*: involuntary first movement, a second "combined with a wish", a third "beyond our control"; a timing-of-control thesis |
| 1993 | Gross & Levenson, *JPSP* | Expressive suppression leaves experience unchanged and raises some sympathetic activity |
| 1995 | Gross & Muñoz | Emotion regulation framed for mental health |
| 1998 | Gross, *JPSP*; Gross, *RGP* | Antecedent/response distinction; five-point process model |
| 1998 | Baumeister et al. | Emotion suppression used as an ego-depletion manipulation |
| 2000 | Richards & Gross | Suppression's memory cost |
| 2001 | Beauregard, Lévesque & Bourgouin | "Conscious Self-Regulation of Emotion" fMRI, with a non-materialist reading |
| 2002 | Ochsner et al. | Reappraisal fMRI ("Rethinking Feelings") |
| 2003 | Gross & John | ERQ; trait reappraisal and suppression |
| 2005 | Schwartz, Stapp & Beauregard | Quantum Zeno model applied to Ochsner et al. 2002 |
| 2005 | Ochsner & Gross | Prefrontal/cingulate control of emotion-generative systems |
| 2007 | Sheppes & Meiran | Late reappraisal loses efficacy: "point of no return" |
| 2007 | Mauss, Bunge & Gross | Automatic emotion regulation |
| 2008 | Goldin et al. | Early versus late prefrontal timing for reappraisal versus suppression |
| 2011 | Sheppes & Gross | Generic → process-specific timing hypothesis |
| 2011 | Gross & Barrett; Kappas; Gross, Sheppes & Urry | Generation/regulation dispute |
| 2011 | Gyurak, Gross & Etkin; Koole & Rothermund | Implicit emotion regulation framed |
| 2011 | Sheppes et al. | Regulation choice by intensity |
| 2012 | Webb, Miles & Sheeran | 306-comparison meta-analysis; effectiveness does not follow stage order |
| 2013 | Paul et al.; Troy et al.; Bonanno & Burton | Suppression acts early when preventive; context reverses reappraisal; "fallacy of uniform efficacy" |
| 2014 | Buhle et al. | 48-study reappraisal neuroimaging meta-analysis |
| 2015 | Gross; Etkin, Büchel & Gross | Extended process model; regulation as valuation |
| 2016 | Duckworth, Gendler & Gross | Process model carried into self-control; "earlier intervention is best" |
| 2016 | Hagger et al. | Ego-depletion multi-lab null |
| 2017 | Braunstein, Gross & Ochsner; Morawetz et al. | Goal × process axes; strategy-general neural network |
| 2021 | Wang et al. | 87-country reappraisal intervention test |
| 2022 | Levy-Gigi & Shamay-Tsoory | Affect labelling works at all three timings tested |
| 2025 | Chen et al. | 249-article cross-cultural meta-analysis |

## The Map's Question: Where a Conscious Contribution Would Sit {#maps-question}

**The Map's interest.**
- The self-control page relocates the selector's ordinary work to "moments of policy".
- The alief page conditions felt effort on noticing.
- The control-theoretic page says stabilisation effort "scales with the disturbance magnitude".
- Emotion regulation is where those three claims meet a literature that has measured *when* control acts, at a resolution of seconds.

**Two clocks.** The article needs this table, or one like it, to keep the two clocks apart.

| Stage | What it is | Can it run implicitly? | Where the Map would place a contribution, if any | What the physical model says |
|---|---|---|---|---|
| Identification (regulatory) | registering that an emotion calls for regulation | yes: emotional conflict adaptation is uninstructed and "proceeds without awareness" (Gyurak et al.) | the noticing condition: an explicit goal needs the emotion noticed | a valuation that the current state departs from a goal (Gross 2015) |
| Selection (regulatory) | choosing a strategy | partly: choice tracks intensity (Sheppes et al. 2011), and goals can be primed (Williams; Mauss) | the policy moment: choosing *how* to regulate | a second-order valuation (Gross 2015; Etkin, Büchel & Gross 2015) |
| Situation selection or modification | changing what one meets | yes: habitual avoidance; scaffolding (Colombetti & Krueger) | the self-control page's "choosing a situation", made before the episode | planning under a cost signal (the self-control page's L88 rival) |
| Attentional deployment | distraction, concentration | yes: automatic attention shifts (Mauss, Bunge & Gross; not detailed here) | weak: the pooled family effect is d+ = 0.00 | attention control |
| Cognitive change | reappraisal | yes, at least for affect labelling, which "may not even feel like a regulatory process" | Stapp's worked example | semantic representations modulating the amygdala (Buhle et al.) |
| Response modulation | expressive suppression | partly: habitual suppression; preventive use (Paul et al.) | the veto analogue (`control-theoretic-will` L76) | late inhibitory control, with costs |

**What the Map can say.**
- The regulation literature locates *explicit* control at the goal (Braunstein's conscious-goal end) and at the regulatory stages of identification and selection. Implementation can then be automatic even for an explicit goal (their "explicit automatic" class).
- If a non-physical selector operates in emotion regulation, the Map's reading puts its ordinary work there, and at policy moments made before the episode (situation selection; implementation intentions, d+ = 0.91 against no instruction). That is the shape of [[skill-delegation]] and of the self-control relocation.
- Seneca's second *motus* ("combined with a wish, though not an obstinate one") is a precedent for placing the voluntary contribution after an involuntary onset and before a point of no return. The article may cite it as precedent, not as evidence.

**What the Map cannot say.**
- **That the placement is evidence.** Each stage is modelled as valuation or control with no experiential term, and each has an implicit form. A physical valuation architecture predicts the same timing record, including the cost profile of late regulation, so the placement is fit only.
- **That consciousness does the regulating.** Implicit regulation is real and, per Koole & Rothermund, "likely" pervasive. The article must say plainly that emotion regulation does not require a conscious contribution at any stage.
- **That consciousness is idle where it is present.** That every stage can run without consciousness shows that consciousness is not necessary for regulation. It does not show that consciousness is idle when an explicit goal is held. Williams et al.'s outcome equivalence (primed versus instructed reappraisal), even if it replicated, shows that two routes reach one effect, not that the conscious route contributes nothing. P-A4 applies symmetrically: introspection certifies neither efficacy nor its absence.
- **That the timing record supports Tenet 2.** Early, low-effort regulation is an economy of control effort. Tenet 2's minimality is fixed by the empirical record the interaction must respect (the control-theoretic page's wording, quoted in [Coverage](#coverage)), not by how few or how small the interventions are.
- **That Schwartz, Stapp & Beauregard's reading of Ochsner et al. is the right one.** The Map can record that its preferred mechanism's worked example is a reappraisal experiment. It must add that the same data have a physical route (Buhle et al.'s semantic-representation pathway) and that the Zeno account is a posit, which is the clinical-neuroplasticity page's verdict.

**The symmetric cut, in the Map's own voice.**
- The finer the literature's temporal resolution becomes, the more completely each stage is described without consciousness. The Map gains a precise location and loses any claim that the location is evidentially special.
- That cuts against using emotion regulation as support, and against reading the implicit-regulation record as a refutation. The Map records both.

**What would decide something.**
- A design that separates goal consciousness from process within the same strategy and timing, with preregistration and adequate power: instructed versus primed (or masked) reappraisal, initiated at matched early and late points, with time-resolved measures (LPP; early versus late prefrontal recruitment).
- If outcomes and time courses were indistinguishable, a physical goal representation would suffice for the regulatory effect at every timing. If the conscious-goal condition alone showed the late-initiation benefit, that would locate a difference, but not its metaphysics.
- **Either result is compatible with both the interface and production readings.** It would settle where conscious goals make a *functional* difference, nothing more.

## Potential Article Angles {#angles}

1. **Recommended: the timing-and-placement article** (2,300–2,700 body words).
   1. Lede:
      - the process model is a map of where regulation acts;
      - its authors narrowed "earlier is easier";
      - regulation needs no conscious contribution at any stage;
      - the Map can locate a possible contribution at the regulatory goal and at policy moments, and the location is fit, not evidence.
   2. "Five Points and Two Halves" {#five-points}: the five families (compact table, 5 rows) and the antecedent/response cut, with Gross & John's own scope sentence.
   3. "What Timing Studies Measure" {#timing}: Goldin; Thiruchselvam; Paul (suppression acting early); Sheppes & Meiran (point of no return). One paragraph on time-resolved versus localisation evidence (Morawetz).
   4. "Earlier Is Not Uniformly Better" {#not-uniform}: the generic and process-specific timing hypotheses; Webb's non-monotone pooled effects; context reversals; "fallacy of uniform efficacy". Note Duckworth et al.'s generic form for self-control as a live asymmetry.
   5. "Regulation Without a Regulator's Awareness" {#implicit}: Koole & Rothermund; Gyurak et al.; Braunstein's goal × process axes; affect labelling. One sentence on goal priming, flagged.
   6. "Is There a Before?" {#generation-regulation}: Gross & Barrett; Kappas; Gross, Sheppes & Urry. Link [[valence-as-a-natural-kind]] for constructionism.
   7. "Where a Conscious Contribution Would Sit" {#placement}: the two clocks; identification and selection; policy moments (Webb, Schweiger Gallo et al.'s implementation intentions); Seneca's three *motus* as precedent; the Stapp worked example, calibrated against Buhle.
   8. Relation to Site Perspective.
2. **Alternative: a narrower "reappraisal versus suppression" piece.** Rejected: it repeats the field's best-known contrast and loses the implicit and generation/regulation material, which is what makes the location question hard.
3. **Alternative: a concepts page "process model of emotion regulation".** Rejected: the brief requires the timing question, and a neutral concept page would invite the general survey the brief rules out.

When writing, follow `obsidian/project/writing-style.md` for the named-anchor forward references, background vs novelty, tenet alignment and front-loading.

## Guards for the Article Writer (Binding) {#guards}

### Author stances

- **Gross; Sheppes; McRae; Ochsner; Goldin; Etkin; Braunstein; Gyurak.**
  - Affective scientists in a functional, information-processing frame.
  - Gross (2015) and Etkin, Büchel & Gross (2015) model regulation as valuation and reinforcement learning.
  - None argues for dualism or engages the metaphysics. **Cite as rivals at the framework boundary, not as allies.** Their models need no experiential term.
- **Barrett** (through Gross & Barrett 2011).
  - Constructionist, and physicalist about emotion.
  - The co-authored paper is a map of perspectives. Do not cite it as Barrett conceding that regulation is distinct, or as Gross conceding that it is not.
- **Kappas.** Emotions as self-regulating processes, on a functional view.
- **Koole; Rothermund; Mauss; Bargh; Williams.**
  - Automaticity researchers.
  - Bargh's programme holds that much goal pursuit is nonconscious. Do not enlist it for or against the Map.
- **Webb; Sheeran; Gollwitzer.** Action-control psychologists. Implementation intentions "delegate" control to cues (the self-control page quotes Gollwitzer). Their framework is physical.
- **Duckworth; Gendler.** Gendler is the alief theorist and here a co-author of a psychology paper. Do not read alief into it.
- **Beauregard** (2001, 2007) and **Schwartz, Stapp & Beauregard** (2005).
  - **The exceptions: they argue for a non-materialist or interactionist reading of regulation neuroimaging.**
  - Report Beauregard's sentences as his interpretation. Report the Zeno account as Stapp's posit.
  - The Map's own calibration ([[clinical-neuroplasticity-evidence-for-bidirectional-causation]]: the data "do not adjudicate") binds here.
  - Do not let their framing of Ochsner et al. stand as Ochsner's.
- **Seneca.** A Stoic corporealist writing therapy. His three *motus* are a thesis about assent, not about Gross's stages.
- **Kerr; Madjar; Glazer; Colombetti & Krueger; Archer & Mills.** Philosophers of emotion working on rationality, understanding, cooperation, scaffolding and injustice. None engages dualism.
- **No author in this note except Beauregard and Schwartz, Stapp & Beauregard argues for a non-physical reading.** Write "the process model needs no experiential term" as the Map's observation about the models, not as any author's thesis.

### The calibration rule (binding)

1. **Substrate-neutral, so fit, not evidence (Tenet 3).**
   - Process-model findings, timing studies included, are predicted by a physical valuation-and-control architecture.
   - Any placement of a conscious contribution is coherence within the Map's framework only. It is neither support nor challenge, as the self-control page's L88 already rules ("The fit discriminates nothing").
2. **Implicit regulation exists, and regulation does not require a conscious contribution at any stage.**
   - Say this plainly, in the article's own voice, and early.
   - It cuts against any "consciousness does the regulating" reading.
   - Cite Koole & Rothermund's definition, Gyurak et al.'s emotional-conflict case, Braunstein's axes and affect labelling.
3. **Never concede epiphenomenalism.**
   - That the stages run without consciousness does not show that consciousness is idle where it is present.
   - Do not argue the converse either: "explicit regulation feels effortful, so consciousness does it" fails by the [[alief-and-acting-against-belief#noticing-condition|noticing condition]] and by the effort page's cost-signal reading.
   - P-A4 makes the limit symmetric.
4. **Tenet 2 is empirical-constraint minimality, not fewness or smallness of interventions.**
   - Do not read "early regulation needs less effort", "policy moments need few interventions" or "a single goal setting suffices" as support for Tenet 2.
   - Quote or paraphrase the control-theoretic page's statement (see [Coverage](#coverage)).
   - The self-control page's L106 already carries this correction (refined 2026-10-23). Match it.
5. **The Stapp worked example is a posit.**
   - Record that Schwartz, Stapp & Beauregard model Ochsner et al. 2002, and keep the Map's existing verdict: compatible, not discriminating.
   - Do not add reappraisal neuroimaging as a further independent stream in the clinical-neuroplasticity convergence. It shares the prefrontal top-down route with CBT and placebo, which that page already down-counts.
6. **Content-specificity.**
   - Reappraisal is a clean "same stimulus, different construal, different response" case. If the article mentions [[content-specificity-of-mental-causation]], it must carry that page's own functionalist response and "stated at the strength the data carry".
   - Note that a task to build a cumulative case from such instances ("Write concept page on content-specificity as evidence for mental causation", which lists emotion regulation) sits in the Vetoed bank (todo.md L7350). The article must not revive it.
7. **Timing claims rest on time-resolved designs.**
   - Use Goldin's 0–4.5 s and 10.5–15 s windows, Thiruchselvam's LPP and Paul's LPP.
   - Do not infer timing from which regions activate (Morawetz et al. 2017: strategy-general VLPFC, insula and SMA).
8. **The family label is not the time.** After Paul et al. 2013, never write "suppression acts late" without "when used reactively" or "on the process model's account".
9. **Keep the generation/regulation dispute visible.** At least one sentence: the timing question presupposes that generation and regulation are distinct, which constructionists contest.
10. **Absence claims scoped** (see [Absence and Exclusivity Claims](#absence)).

### Quote status {#quote-status}

**Cleared to quote.** Every passage quoted in [Key Sources](#key-sources) and the sections above it greps in the raw text of the source named, at the verification tag shown. These specific constraints apply:
- **Gross & John 2003**: write "emotion-generative" as one hyphenated word (it breaks across a line in the PDF).
- **Webb, Schweiger Gallo et al. 2012**: the implementation-intention figures as numbers only (the PDF text layer garbles "=" and "d+").
- **Schwartz, Stapp & Beauregard 2005**: the Ochsner sentence keeps its curly single quotes around ‘reappraise’.
- **Beauregard 2001, 2007**: quote only as his interpretation.
- **Seneca**: attribute the English to Stewart's 1900 translation, cite "*De Ira* 2.4.1" (or 2.2, 2.3), and give the Latin *motus* where the article uses "movement".
- **Wang et al. 2021**: not the abstract sentence containing "vesus".
- **Baumeister et al. 1998; Hagger et al. 2016; Sheppes & Meiran 2008's "self control resources"**: for the ego-depletion flag only.
- **Abstract-only sources** ([V-abs]): quote abstract wording only, and do not attribute body-level claims to them.

**Quote only "as quoted in", or paraphrase:**
- Mauss, Cook & Gross 2007: through Gyurak et al. 2011.
- Etkin et al. 2010 ("despite careful probing…"): through Gyurak et al. 2011.
- Lévesque et al. 2003; Paquette et al. 2003: through Schwartz, Stapp & Beauregard 2005.

**Do not quote:**
- anything from the bodies of Gross 1998 (*RGP*), Gross 2015, Sheppes & Gross 2011, Webb et al. 2012 (*Psych Bull*), Buhle et al. 2014 or Beauregard et al. 2001 (bodies not read);
- Sorabji 2000 or Graver 2007 (not read);
- any definition of "identification", "selection" or "implementation" beyond Gross 2015's and McRae & Gross 2020's abstracts;
- any effect size for situation selection or modification in emotion regulation (none found);
- the Wang et al. abstract sentence containing "vesus".

### Evidence not to lean on {#not-to-lean-on}

- **Ego depletion.**
  - Do not explain suppression's costs, or late reappraisal's costs, as resource depletion.
  - Baumeister et al. 1998 used emotion suppression as a depleting task. The multi-lab replication found d = 0.04 [−0.07, 0.15] (Hagger et al. 2016), though with a different task.
  - Sheppes & Meiran's (2008) "self control resources" is the depletion construct. Use its memory result instead.
  - If depletion comes up at all, flag it in one clause and link [[mental-effort]]'s depletion discussion.
- **Goal priming as evidence for or against conscious contribution.** Williams et al. 2009 (Experiment 1, n = 39 across three cells, scrambled-sentence prime) and Mauss, Cook & Gross 2007 belong to a priming literature with replication problems, and Braunstein et al. (2017) note that no imaging study had examined primed regulation. At most one hedged sentence.
- **Goldin et al. 2008 alone.** n = 17, women only, disgust only, experience rated after each clip. Pair it with Thiruchselvam and Paul, and with Buhle and Morawetz for the neural claims (citation-aging rule).
- **ERQ trait correlations as timing evidence.** Gross & John disclaim it themselves.
- **"Reappraisal is good, suppression is bad."** Context-dependent (Troy; Soto; Chen; Ford & Troy). Use "fallacy of uniform efficacy".
- **Hiekkaranta et al. 2023** for within-episode timing. Its "temporal" means clock time.
- **Beauregard's or Stapp's readings** as findings.
- **Seneca as evidence.** Precedent only.
- **The Wang et al. 2021 multi-country result as bearing on timing.** It tests efficacy only.

### Coiner and populariser

- **Process model of emotion regulation; five families; antecedent-focused versus response-focused**: Gross 1998 (*JPSP* and *RGP*). Whether Gross & Muñoz 1995 states the antecedent/response cut first was not checked, so write "proposed in Gross (1998)", not "coined in".
- **Generic and process-specific timing hypotheses**: Sheppes & Gross 2011 (their names).
- **Extended process model**: Gross 2015.
- **"Point of no return"**: Sheppes & Meiran 2007 use the phrase with "a possible". Keep the hedge.
- **"fallacy of uniform efficacy"; "regulatory flexibility"**: Bonanno & Burton 2013 ("We label this assumption…", "we refer to as regulatory flexibility").
- **Implicit emotion regulation**: in use by many groups. Koole & Rothermund's 2011 special issue is a definition, not a coinage. Do not credit a coiner.
- **Affect labelling as implicit regulation**: Torre & Lieberman 2018 make the case. The labelling effect is older (Lieberman et al. 2007 and earlier).
- **"Engagement" versus "disengagement" regulation**: Sheppes et al. 2011 in psychology; Madjar 2020 in philosophy ("engaged"/"disengaging"). Credit each for their own use.
- **Seneca's *primus motus***: Seneca's phrase. **The Greek *propatheia* is not in *De Ira* II** (0 hits in the Latin of Book II) and is a later term. Do not attribute it to Seneca.
- **Situational self-control strategies, "process model of self-control"**: Duckworth, Gendler & Gross (2014, cited in their 2016 paper; 2014 not looked up).

### Term traps

- **"Suppression"** means *expressive* suppression in Gross. It is distinct from thought suppression (Wegner) and from "suppressing the experience" (Webb's separate category, d+ ≈ 0). Ainslie's "Suppression" (the self-control page's L68: "inhibiting valuation of (modulating) and/or keeping attention from (filtering)") is a third sense. Name which on every use.
- **"Response-focused"** names a target, not a time (Paul et al.).
- **"Implicit"** in Braunstein is about the *goal*; "automatic" is about the *process*. Keep them apart. Gyurak et al. run them together, by their own account "porous".
- **"Selection"** is the extended model's strategy-selection stage. It is unrelated to the Map's "selection" by a conscious selector, and unrelated to *situation* selection. The article uses all three, so disambiguate each on first use.
- **"Regulation"** in "emotion regulation" is distinct from "regulation" in [[control-theoretic-will]] (stabilisation against disturbance). Do not let the shared word carry an inference.
- **"Attentional deployment"** on the Map (`valence-and-conscious-selection` L159, `retrocausality` L103) means attention timing and allocation, not Gross's family. Do not link those uses as if they were the same.
- **"Reappraisal"** covers reconstrual and repurposing (Uusberg et al.), and distancing. Webb distinguishes reappraising the stimulus, reappraising the response and perspective taking.
- UK spelling outside quotations (behaviour, labelling, organise); US spelling inside them ("behavior", "labeling").

### Integration passages for the cross-review {#integration}

Word counts are `analyze_length` body words against the hard limit, measured 19:53–20:05Z. Headroom is hard − 1 − count. This note writes **no wikilink to the new slug**, because the target does not exist yet; the cross-review adds them.

| Host | Words / hard | Headroom | Passage |
|---|---|---|---|
| `concepts/self-control-as-skill-and-scaffolding` | 2,998/3,500 | 501 | **L46**, after the Duckworth, Gendler & Gross (2016) clause: one sentence (≤35 words). Their "process model of self-control" expands Gross's (1998) model of emotion regulation, whose authors later narrowed its "earlier is easier" premise for emotion. Link the new article. **Must not touch L86 (Dretske), L88 ("The fit discriminates nothing") or L106 (Tenet 2, refined today).** |
| `topics/alief-and-acting-against-belief` | 3,317/4,000 | 682 | **§The Noticing Condition, after L113**: one sentence (≤40 words). The extended process model makes identification the first stage of explicit regulation, the emotion-regulation form of the noticing condition, and implicit regulation runs without it. Link. Optional: pipe "situational self-control strategies" at L119 unchanged. Must keep L113's conditional. |
| `voids/numbing-void` | 2,681/3,000 | 318 | **L56**: pipe "emotion regulation" (inside "skilled at emotion regulation") to the new article at zero cost. Optional ≤20 words after the Cameron & Payne "proactively" quote: in process-model terms, proactive down-regulation is antecedent-focused. **Must keep L100's "an illustration, not an instance".** |
| `concepts/mental-effort` | 3,348/3,500 | 151 | **L106**: pipe "cognitive reappraisal" to the new article at zero cost. Optional, length-neutral: "Effortful cognitive reappraisal" → "Cognitive reappraisal, effortful when initiated late," or similar (see [Side-findings](#side-findings)). No other additions. |
| `topics/emotion-and-dualism` | 3,350/4,000 | 649 | **§Emotional Causation (L105–L107)**: one or two sentences (≤50 words). Emotions are routinely modified by regulation, explicitly and implicitly. Affect labelling dampens amygdala response (Lieberman et al. 2007), which gives the orphaned L212 reference a body citation. Link. Must not repeat the "Damasio … causally idle" sentence (see [Side-findings](#side-findings)). |
| `concepts/control-theoretic-will` | 2,907/3,500 | 592 | **§Stabilisation, after L74**: one sentence (≤40 words). In emotion regulation, the process-specific timing hypothesis (Sheppes & Gross 2011) restricts intensity-proportional effort to late-stage strategies, and early strategies "require minimal effort". Link. Optional: **§Veto (L76–L82)**, ≤25 words: expressive suppression as the emotional analogue of veto, the costliest family. Must keep the L82 Tenet 2 caution and the "no current prediction separates…" verdict. |
| `topics/clinical-neuroplasticity-evidence-for-bidirectional-causation` | 3,620/4,000 | 379 | **§Proposed Mechanisms (L108)**, after the Schwartz-Stapp-Beauregard sentence: one sentence (≤35 words). Their worked example is Ochsner et al.'s (2002) reappraisal experiment, whose neural route a 48-study meta-analysis describes physically (Buhle et al. 2014). Link. **Must not add reappraisal as a further evidence stream** (the L102–L104 down-counting). |
| `concepts/content-specificity-of-mental-causation` | 2,131/3,500 | 1,368 | Optional, §The Core Pattern: ≤50 words naming reappraisal as a case (same stimulus, different construal, different response), with the functionalist reading made explicit. Low priority, and subject to calibration rule 6. |
| `concepts/skill-delegation` | 2,437/3,500 | 1,062 | Optional: one sentence. Explicit and implicit regulation "have porous boundaries" (Gyurak et al.), and Braunstein's "explicit automatic" class (a conscious goal served by an automatic process) is the delegation shape in the affective domain. Link. Low priority. |
| `topics/valence-as-a-natural-kind` | 2,998/4,000 | 1,001 | Optional: one sentence noting that constructionism also contests the generation/regulation split (Gross & Barrett 2011). Link. Low priority. |
| `concepts/alexithymia` | 2,056/3,500 | 1,443 | Optional, Map's step only: difficulty identifying feelings is a deficit at the identification stage. No verified source links alexithymia to the extended process model, so label it as the Map's step or omit. Low priority. |
| `topics/immediate-emotions-and-the-affect-heuristic` | 3,332/4,000 | 667 | **No additions.** Its L93 "emotion regulation" is a search-vocabulary list, and its regulation-and-risk studies stay there. A piped link is not needed. |
| `concepts/epistemic-emotions` | 2,587/3,500 | 912 | **No additions.** No passage bears on the timing question (no "regulat" hits). |
| `concepts/stapp-quantum-mind` | 4,000/3,500 | over hard | **No additions.** |
| `concepts/libet-experiments` | 3,497/3,500 | 2 | **No additions.** |
| `concepts/attention-as-interface` | 3,468/3,500 | 31 | **No additions.** Do not use Webb's attentional-deployment null there. |
| `concepts/conscious-vs-unconscious-processing` | 3,477/3,500 | 22 | **No additions.** |
| `topics/valence-and-conscious-selection` | 4,338/4,000 | over hard | **No additions.** |
| `concepts/epiphenomenalism` | 3,459/3,500 | 40 | **No additions.** |

### Length

- Target 2,300–2,700 body words. The topics soft limit is 3,000 and the hard limit 4,000.
- Expect 25–30 references. Memory notes record reference apparatus consuming the soft-to-hard band, so cite only what the prose uses. Drop unless the prose needs them: Aldao 2010; Brans 2013; Hiekkaranta 2023; Wang 2021; Chen 2025; Soto 2011; Butler 2003; Richards & Gross 2000; Madjar; Glazer; Archer & Mills; Mauss, Cook & Gross; Baumeister 1998; Hagger 2016.
- One compact five-family table (5 rows) and, if space allows, a reduced two-clocks table (4–6 rows). Prose for the rest.

### Prose

- No "This is not X. It is Y."
- Avoid "load-bearing" as an intensifier.
- No exposed internal labels ("fit, not evidence" is plain English and may stand; "framework-internal only" may not).
- The description must not contain a literature-wide absence claim.

## Absence and Exclusivity Claims (Scoped) {#absence}

Per `writing-style.md` §"Absence and Exclusivity Claims", every absence claim carries its search scope.

**On-Map absences (licensed, scoped).**
- Write: "no Map page the 2026-10-23 search found discusses Gross's process model, expressive suppression, the antecedent/response distinction or implicit emotion regulation".
- Scope: case-insensitive fixed-string search of live topics, concepts, apex, voids, positions and tenets, with positive controls ([Coverage](#coverage)).
- Keep these out of the description and lede.

**Literature-scope absences (licensed only with the scope).**
- Write: "this search found no pooled estimate for situation selection or situation modification as emotion-regulation strategies".
  - Scope: the Webb et al. 2012 abstract, the Webb, Schweiger Gallo et al. 2012 review and one WebSearch, 2026-10-23. The meta-analysis body was not read.
  - **Do not write** "situation selection has never been tested".
- Write: "Gross and John's trait studies, by their own statement, do not test the model's temporal ordering". Licensed by the quoted sentence.
- Write: "as of 2017, no imaging study had examined primed emotion regulation, according to Braunstein, Gross and Ochsner". Attribute it. It is their claim, dated.
- Write: "this search found no 2023–2025 experimental meta-analysis of process-model strategies; the recent syntheses found are correlational" (Chen et al. 2025; one WebSearch, plus OpenAlex). Scope as stated.

**Literature-wide claims: not licensed. Do not write:**
- "Earlier regulation is always more effective." Contradicted.
- "Suppression never reduces experience." Goldin 2008.
- "Reappraisal is the best strategy." Context-dependent.
- "Implicit regulation is as effective as explicit regulation." Open.
- "The field agrees that generation and regulation are distinct." Contested.
- "Emotion regulation requires consciousness" or "emotion regulation is entirely unconscious." Neither.
- "Consensus", "well established" or "recent work has shown" about timing, beyond the specific studies.

**Currency.**
- The newest timing-specific sources read are Levy-Gigi & Shamay-Tsoory 2022 and Paul et al. 2013. The newest frameworks are Braunstein et al. 2017 and McRae & Gross 2020. The newest syntheses are Chen et al. 2025 (correlational) and Wang et al. 2021 (efficacy).
- The forward search on Sheppes & Gross 2011 found 5 titled timing studies from 2019 on. None overturns the process-specific hypothesis on this reading; only two were read (Levy-Gigi; Hiekkaranta).
- Treat the timing debate as **2007–2017-anchored**, with a 2022 extension.

## Gaps in Research {#gaps}

- **Webb et al. 2012 body.** Unread (embargoed). Whether situation selection and modification were included, and the moderator analyses, are unknown.
- **Sheppes & Gross 2011 body.** Unread. The process-specific hypothesis is attested by its abstract only. The empirical tests it reviews are known only through Sheppes & Meiran's abstracts.
- **Gross 2015 body.** Unread. The definitions of the identification, selection and implementation stages, and whether Gross places awareness at any stage, are unknown. **This is the first thing to read if the expand-topic run has budget**, because the article's placement claim leans on it.
- **Situation selection and modification for emotion.** No experimental pooled estimate found.
- **Direct replications of the timing studies.** Paul et al. 2013 partly contradicts the family-equals-time reading; no direct replication of Goldin et al. 2008 or Sheppes & Meiran 2007 was searched.
- **Replication of the goal-priming regulation studies.** Not searched beyond Braunstein's 2017 remark.
- **Other titled timing studies from 2019 on.** Ortner et al. 2021 (*Cognition & Emotion*, "temporal goals on emotion regulation choice: a replication and extension") and two others were not read.
- **Gross & Muñoz 1995.** Whether it states the antecedent/response cut was not checked.
- **Soter (2025)'s borrowed "mechanistic account of control of the guidance function for 'emotion-type states'"** (`alief…` L85). Its source was not identified. If it is a process-model source, the alief page's mechanism chain runs through this literature. See [Side-findings](#side-findings).
- **The Stoic first-movement scholarship** (Sorabji 2000; Graver 2007). Unread.
- **Etkin et al. 2010** (the awareness probe Gyurak et al. cite). Unread.

## Side-Findings (leads only) {#side-findings}

- **`concepts/mental-effort` L106**: "Effortful cognitive reappraisal engages prefrontal regulatory circuits that modulate subcortical processing".
  - Under Sheppes & Gross 2011, early reappraisal requires "minimal effort". Sheppes & Meiran 2008 found "for the first time a cognitive cost for reappraisal" only when it was initiated late.
  - The unqualified "Effortful" overstates. A calibration-lens lead, not a factual error.
  - The page has 151 words of headroom, so any fix must be near length-neutral.
- **`topics/emotion-and-dualism` L212**: Lieberman et al. 2007 is in the reference list, and no body sentence cites it (grep for "Lieberman", "labell", "into words": reference line only). An orphaned reference. The integration passage above would give it a body citation.
- **`topics/emotion-and-dualism` L107**: "Damasio's somatic marker hypothesis, which treats consciousness as causally idle".
  - Damasio's somatic markers can operate overtly or covertly. Whether Damasio treats consciousness as causally idle is a characterisation this note did not verify, and it may be a fidelity defect (the populariser/originator family).
  - Lead only. Check Damasio 1994 or 1996 before any change.
- **Schwartz, Stapp & Beauregard 2005 across ~15 Map pages.**
  - No page mentions that its worked example is Ochsner et al.'s reappraisal experiment ("Ochsner": 0 live).
  - Not a defect on any page. It means the Map's preferred mechanism's one worked empirical case sits in a literature the Map has not otherwise examined. The new article closes that gap. The clinical-neuroplasticity integration sentence is the propagation.
- **The alief research note** (`research/alief-and-acting-against-what-one-believes-2026-10-20`) lists Ochsner & Gross 2005 as "[meta] … The abstract was not checked." It is now [V-abs] here. No live page cites it, so no change is needed.
- **The self-control page's Duckworth, Gendler & Gross (2016) citation is abstract-only.** The full text (read here) states the generic timing claim ("as a rule, earlier intervention is best"). The process model's authors narrowed that claim for emotion in 2011. The self-control page's L46 hedge ("may be especially effective") already matches the abstract. Confirmed; no change needed beyond the pointer sentence.
- **Brief discrepancy, for the driver.** The brief says `immediate-emotions-and-the-affect-heuristic` was "refined today at L85: 'push risk estimates in opposite directions'". At 20:12Z the file reads "Fear and anger, both negative, push risk in opposite directions" (L85). Its `ai_modified` is 2026-10-22T11:48:21Z, and no 2026-10-23 commit touches it. Either a pending edit has not landed or the brief misdescribes the line. No consequence for this note.
- **Chain mechanics, for the driver.** This note's stem appears in the originating todo task's Notes ("Output a research note to obsidian/research/emotion-regulation-and-the-timing-of-control-2026-10-23.md"). `chain_note` skips any note whose stem is in `todo.md` ("a todo task already references this note"), so the expand-topic task will need minting by hand. This is the known same-day-harvest false skip.

## Citations {#citations}

1. Aldao, A., Nolen-Hoeksema, S., & Schweizer, S. (2010). Emotion-regulation strategies across psychopathology: A meta-analytic review. *Clinical Psychology Review*, 30(2), 217–237. https://doi.org/10.1016/j.cpr.2009.11.004
2. Aldao, A., Sheppes, G., & Gross, J. J. (2015). Emotion regulation flexibility. *Cognitive Therapy and Research*, 39(3), 263–278. https://doi.org/10.1007/s10608-014-9662-4
3. Archer, A., & Mills, G. (2019). Anger, affective injustice, and emotion regulation. *Philosophical Topics*, 47(2), 75–94. https://doi.org/10.5840/philtopics201947216
4. Baumeister, R. F., Bratslavsky, E., Muraven, M., & Tice, D. M. (1998). Ego depletion: Is the active self a limited resource? *Journal of Personality and Social Psychology*, 74(5), 1252–1265. https://doi.org/10.1037/0022-3514.74.5.1252
5. Beauregard, M. (2007). Mind does really matter: Evidence from neuroimaging studies of emotional self-regulation, psychotherapy, and placebo effect. *Progress in Neurobiology*, 81(4), 218–236. https://doi.org/10.1016/j.pneurobio.2007.01.005
6. Beauregard, M., Lévesque, J., & Bourgouin, P. (2001). Neural correlates of conscious self-regulation of emotion. *The Journal of Neuroscience*, 21(18), RC165. https://doi.org/10.1523/JNEUROSCI.21-18-j0001.2001
7. Bonanno, G. A., & Burton, C. L. (2013). Regulatory flexibility: An individual differences perspective on coping and emotion regulation. *Perspectives on Psychological Science*, 8(6), 591–612. https://doi.org/10.1177/1745691613504116
8. Braunstein, L. M., Gross, J. J., & Ochsner, K. N. (2017). Explicit and implicit emotion regulation: A multi-level framework. *Social Cognitive and Affective Neuroscience*, 12(10), 1545–1557. https://doi.org/10.1093/scan/nsx096
9. Brans, K., Koval, P., Verduyn, P., Lim, Y. L., & Kuppens, P. (2013). The regulation of negative and positive affect in daily life. *Emotion*, 13(5), 926–939. https://doi.org/10.1037/a0032400
10. Buhle, J. T., Silvers, J. A., Wager, T. D., Lopez, R., Onyemekwu, C., Kober, H., Weber, J., & Ochsner, K. N. (2014). Cognitive reappraisal of emotion: A meta-analysis of human neuroimaging studies. *Cerebral Cortex*, 24(11), 2981–2990. https://doi.org/10.1093/cercor/bht154
11. Butler, E. A., Egloff, B., Wilhelm, F. H., Smith, N. C., Erickson, E. A., & Gross, J. J. (2003). The social consequences of expressive suppression. *Emotion*, 3(1), 48–67. https://doi.org/10.1037/1528-3542.3.1.48
12. Chen, M. S., Cai, Q., Omari, D., Sanghvi, D. E., Lyu, S., & Bonanno, G. A. (2025). Emotion regulation and mental health across cultures: A systematic review and meta-analysis. *Nature Human Behaviour*, 9(6), 1176–1200. https://doi.org/10.1038/s41562-025-02168-8
13. Colombetti, G., & Krueger, J. (2015). Scaffoldings of the affective mind. *Philosophical Psychology*, 28(8), 1157–1176. https://doi.org/10.1080/09515089.2014.976334
14. Duckworth, A. L., Gendler, T. S., & Gross, J. J. (2016). Situational strategies for self-control. *Perspectives on Psychological Science*, 11(1), 35–55. https://doi.org/10.1177/1745691615623247
15. Etkin, A., Büchel, C., & Gross, J. J. (2015). The neural bases of emotion regulation. *Nature Reviews Neuroscience*, 16(11), 693–700. https://doi.org/10.1038/nrn4044
16. Etkin, A., Egner, T., Peraza, D. M., Kandel, E. R., & Hirsch, J. (2006). Resolving emotional conflict: A role for the rostral anterior cingulate cortex in modulating activity in the amygdala. *Neuron*, 51(6), 871–882. https://doi.org/10.1016/j.neuron.2006.07.029
17. Ford, B. Q., & Troy, A. S. (2019). Reappraisal reconsidered: A closer look at the costs of an acclaimed emotion-regulation strategy. *Current Directions in Psychological Science*, 28(2), 195–203. https://doi.org/10.1177/0963721419827526
18. Glazer, T. (2021). Emotion regulation and cooperation. *Philosophical Psychology*, 34(8), 1125–1145. https://doi.org/10.1080/09515089.2021.1942812
19. Goldin, P. R., McRae, K., Ramel, W., & Gross, J. J. (2008). The neural bases of emotion regulation: Reappraisal and suppression of negative emotion. *Biological Psychiatry*, 63(6), 577–586. https://doi.org/10.1016/j.biopsych.2007.05.031
20. Gross, J. J. (1998a). The emerging field of emotion regulation: An integrative review. *Review of General Psychology*, 2(3), 271–299. https://doi.org/10.1037/1089-2680.2.3.271
21. Gross, J. J. (1998b). Antecedent- and response-focused emotion regulation: Divergent consequences for experience, expression, and physiology. *Journal of Personality and Social Psychology*, 74(1), 224–237. https://doi.org/10.1037/0022-3514.74.1.224
22. Gross, J. J. (2015). Emotion regulation: Current status and future prospects. *Psychological Inquiry*, 26(1), 1–26. https://doi.org/10.1080/1047840X.2014.940781
23. Gross, J. J., & Feldman Barrett, L. (2011). Emotion generation and emotion regulation: One or two depends on your point of view. *Emotion Review*, 3(1), 8–16. https://doi.org/10.1177/1754073910380974
24. Gross, J. J., & John, O. P. (2003). Individual differences in two emotion regulation processes: Implications for affect, relationships, and well-being. *Journal of Personality and Social Psychology*, 85(2), 348–362. https://doi.org/10.1037/0022-3514.85.2.348
25. Gross, J. J., & Levenson, R. W. (1993). Emotional suppression: Physiology, self-report, and expressive behavior. *Journal of Personality and Social Psychology*, 64(6), 970–986. https://doi.org/10.1037/0022-3514.64.6.970
26. Gross, J. J., & Muñoz, R. F. (1995). Emotion regulation and mental health. *Clinical Psychology: Science and Practice*, 2(2), 151–164. https://doi.org/10.1111/j.1468-2850.1995.tb00036.x
27. Gross, J. J., Sheppes, G., & Urry, H. L. (2011). Cognition and Emotion Lecture at the 2010 SPSP Emotion Preconference [title as indexed; working title unverified]. *Cognition and Emotion*, 25(5), 765–781. https://doi.org/10.1080/02699931.2011.555753
28. Gyurak, A., Gross, J. J., & Etkin, A. (2011). Explicit and implicit emotion regulation: A dual-process framework. *Cognition and Emotion*, 25(3), 400–412. https://doi.org/10.1080/02699931.2010.544160
29. Hagger, M. S., Chatzisarantis, N. L. D., Alberts, H., et al. (2016). A multilab preregistered replication of the ego-depletion effect. *Perspectives on Psychological Science*, 11(4), 546–573. https://doi.org/10.1177/1745691616652873
30. Hiekkaranta, A. P., Kirtley, O. J., Eisele, G., Houben, M., Lafit, G., & Myin-Germeys, I. (2023). Time to reappraise or distract? Temporal and situational context in emotion regulation in daily life. *Current Psychology*. https://doi.org/10.1007/s12144-023-05233-5
31. Kalokerinos, E. K., Greenaway, K. H., & Denson, T. F. (2015). Reappraisal but not suppression downregulates the experience of positive and negative emotion. *Emotion*, 15(3), 271–275. https://doi.org/10.1037/emo0000025
32. Kappas, A. (2011). Emotion and regulation are one! *Emotion Review*, 3(1), 17–25. https://doi.org/10.1177/1754073910380971
33. Kerr, D. (2021). On the rationality of emotion regulation. *Philosophical Psychology*, 34(4), 453–473. https://doi.org/10.1080/09515089.2021.1915969
34. Koole, S. L., & Rothermund, K. (2011). "I feel better but I don't know why": The psychology of implicit emotion regulation. *Cognition and Emotion*, 25(3), 389–399. https://doi.org/10.1080/02699931.2010.550505
35. Koole, S. L., Webb, T. L., & Sheeran, P. L. (2015). Implicit emotion regulation: Feeling better without knowing why. *Current Opinion in Psychology*, 3, 6–10. https://doi.org/10.1016/j.copsyc.2014.12.027
36. Levy-Gigi, E., & Shamay-Tsoory, S. (2022). Affect labeling: The role of timing and intensity. *PLOS ONE*, 17(12), e0279303. https://doi.org/10.1371/journal.pone.0279303
37. Lieberman, M. D., Eisenberger, N. I., Crockett, M. J., Tom, S. M., Pfeifer, J. H., & Way, B. M. (2007). Putting feelings into words: Affect labeling disrupts amygdala activity in response to affective stimuli. *Psychological Science*, 18(5), 421–428. https://doi.org/10.1111/j.1467-9280.2007.01916.x
38. Madjar, S. (2020). Emotion regulation and evaluative understanding. *Philosophical Psychology*, 33(6), 777–798. https://doi.org/10.1080/09515089.2020.1751102
39. Mauss, I. B., Bunge, S. A., & Gross, J. J. (2007). Automatic emotion regulation. *Social and Personality Psychology Compass*, 1(1), 146–167. https://doi.org/10.1111/j.1751-9004.2007.00005.x
40. Mauss, I. B., Cook, C. L., & Gross, J. J. (2007). Automatic emotion regulation during anger provocation. *Journal of Experimental Social Psychology*, 43(5), 698–711. https://doi.org/10.1016/j.jesp.2006.07.003
41. McRae, K., & Gross, J. J. (2020). Emotion regulation. *Emotion*, 20(1), 1–9. https://doi.org/10.1037/emo0000703
42. Morawetz, C., Bode, S., Derntl, B., & Heekeren, H. R. (2017). The effect of strategies, goals and stimulus material on the neural mechanisms of emotion regulation: A meta-analysis of fMRI studies. *Neuroscience & Biobehavioral Reviews*, 72, 111–128. https://doi.org/10.1016/j.neubiorev.2016.11.014
43. Ochsner, K. N., Bunge, S. A., Gross, J. J., & Gabrieli, J. D. E. (2002). Rethinking feelings: An fMRI study of the cognitive regulation of emotion. *Journal of Cognitive Neuroscience*, 14(8), 1215–1229. https://doi.org/10.1162/089892902760807212
44. Ochsner, K. N., & Gross, J. J. (2005). The cognitive control of emotion. *Trends in Cognitive Sciences*, 9(5), 242–249. https://doi.org/10.1016/j.tics.2005.03.010
45. Ochsner, K. N., Silvers, J. A., & Buhle, J. T. (2012). Functional imaging studies of emotion regulation: A synthetic review and evolving model of the cognitive control of emotion. *Annals of the New York Academy of Sciences*, 1251, E1–E24. https://doi.org/10.1111/j.1749-6632.2012.06751.x
46. Paul, S., Simon, D., Kniesche, R., Kathmann, N., & Endrass, T. (2013). Timing effects of antecedent- and response-focused emotion regulation strategies. *Biological Psychology*, 94(1), 136–142. https://doi.org/10.1016/j.biopsycho.2013.05.019
47. Richards, J. M., & Gross, J. J. (2000). Emotion regulation and memory: The cognitive costs of keeping one's cool. *Journal of Personality and Social Psychology*, 79(3), 410–424. https://doi.org/10.1037/0022-3514.79.3.410
48. Schwartz, J. M., Stapp, H. P., & Beauregard, M. (2005). Quantum physics in neuroscience and psychology: A neurophysical model of mind–brain interaction. *Philosophical Transactions of the Royal Society B*, 360(1458), 1309–1327. https://doi.org/10.1098/rstb.2004.1598
49. Seneca, L. A. (1900). Of Anger, Book II. In *L. Annaeus Seneca, Minor Dialogs Together with the Dialog "On Clemency"* (A. Stewart, Trans.), pp. 76–114. George Bell and Sons. https://en.wikisource.org/wiki/Of_Anger/Book_II ; Latin: *De Ira* II, The Latin Library, https://www.thelatinlibrary.com/sen/sen.ira2.shtml
50. Sheppes, G., & Gross, J. J. (2011). Is timing everything? Temporal considerations in emotion regulation. *Personality and Social Psychology Review*, 15(4), 319–331. https://doi.org/10.1177/1088868310395778
51. Sheppes, G., & Meiran, N. (2007). Better late than never? On the dynamics of online regulation of sadness using distraction and cognitive reappraisal. *Personality and Social Psychology Bulletin*, 33(11), 1518–1532. https://doi.org/10.1177/0146167207305537
52. Sheppes, G., & Meiran, N. (2008). Divergent cognitive costs for online forms of reappraisal and distraction. *Emotion*, 8(6), 870–874. https://doi.org/10.1037/a0013711
53. Sheppes, G., Scheibe, S., Suri, G., & Gross, J. J. (2011). Emotion-regulation choice. *Psychological Science*, 22(11), 1391–1396. https://doi.org/10.1177/0956797611418350
54. Sheppes, G., Scheibe, S., Suri, G., Radu, P., Blechert, J., & Gross, J. J. (2014). Emotion regulation choice: A conceptual framework and supporting evidence. *Journal of Experimental Psychology: General*, 143(1), 163–181. https://doi.org/10.1037/a0030831
55. Sorabji, R. (2000). *Emotion and Peace of Mind*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199256600.001.0001
56. Soto, J. A., Perez, C. R., Kim, Y.-H., Lee, E. A., & Minnick, M. R. (2011). Is expressive suppression always associated with poorer psychological functioning? A cross-cultural comparison between European Americans and Hong Kong Chinese. *Emotion*, 11(6), 1450–1455. https://doi.org/10.1037/a0023340
57. Thiruchselvam, R., Blechert, J., Sheppes, G., Rydstrom, A., & Gross, J. J. (2011). The temporal dynamics of emotion regulation: An EEG study of distraction and reappraisal. *Biological Psychology*, 87(1), 84–92. https://doi.org/10.1016/j.biopsycho.2011.02.009
58. Torre, J. B., & Lieberman, M. D. (2018). Putting feelings into words: Affect labeling as implicit emotion regulation. *Emotion Review*, 10(2), 116–124. https://doi.org/10.1177/1754073917742706
59. Troy, A. S., Shallcross, A. J., & Mauss, I. B. (2013). A person-by-situation approach to emotion regulation: Cognitive reappraisal can either help or hurt, depending on the context. *Psychological Science*, 24(12), 2505–2514. https://doi.org/10.1177/0956797613496434
60. Uusberg, A., Taxer, J. L., Yih, J., Uusberg, H., & Gross, J. J. (2019). Reappraising reappraisal. *Emotion Review*, 11(4), 267–282. https://doi.org/10.1177/1754073919862617
61. Wang, K., Goldenberg, A., Dorison, C. A., Miller, J. K., Uusberg, A., Lerner, J. S., Gross, J. J., et al. (2021). A multi-country test of brief reappraisal interventions on emotions during the COVID-19 pandemic. *Nature Human Behaviour*, 5(8), 1089–1110. https://doi.org/10.1038/s41562-021-01173-x
62. Webb, T. L., Miles, E., & Sheeran, P. (2012). Dealing with feeling: A meta-analysis of the effectiveness of strategies derived from the process model of emotion regulation. *Psychological Bulletin*, 138(4), 775–808. https://doi.org/10.1037/a0027600
63. Webb, T. L., Schweiger Gallo, I., Miles, E., Gollwitzer, P. M., & Sheeran, P. (2012). Effective regulation of affect: An action control perspective on emotion regulation. *European Review of Social Psychology*, 23(1), 143–186. https://doi.org/10.1080/10463283.2012.718134
64. Williams, L. E., Bargh, J. A., Nocera, C. C., & Gray, J. R. (2009). The unconscious regulation of emotion: Nonconscious reappraisal goals modulate emotional reactivity. *Emotion*, 9(6), 847–854. https://doi.org/10.1037/a0017745
