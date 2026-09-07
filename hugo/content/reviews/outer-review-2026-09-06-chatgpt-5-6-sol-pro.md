---
ai_contribution: 90
ai_generated_date: 2026-09-06
ai_modified: 2026-09-07 00:12:00+00:00
ai_system: chatgpt-5-6-pro
author: Andy Southgate
concepts:
- '[[filter-theory]]'
- '[[filter-vs-interface-distinction]]'
- '[[entropic-brain-hypothesis]]'
- '[[default-mode-network]]'
created: 2026-09-06
date: &id001 2026-09-07
description: ChatGPT 5.6 Pro referee report on Psychedelics and the Filter Model.
  Three citation defects verified at publisher, including two phantom references.
draft: false
human_modified: null
last_curated: 2026-09-07
lastmod: 2026-09-07 00:12:00+00:00
modified: *id001
outer_review_conversation_url: https://chatgpt.com/g/g-p-695a7d60af5481919d5c22ad7bcc1648-the-unfinishable-map/c/6a9ccb95-850c-83eb-9aef-7ed12ce6742e
outer_review_extraction_method: js-dom
outer_review_status: processed
related_articles:
- '[[project]]'
subject_articles:
- topics/psychedelics-and-the-filter-model.md
subject_source: fallback:recent-aged
subject_title: Audit psychedelics-and-the-filter-model
subject_type: recent
title: Outer Review - ChatGPT 5.6 Pro (2026-09-06)
topics:
- '[[psychedelics-and-the-filter-model]]'
- '[[predictive-self-binding-and-the-naturalist-challenge]]'
- '[[predictive-processing-and-dualism]]'
---

**Date**: 2026-09-06
**Reviewer**: ChatGPT 5.6 Pro
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

You are an external referee auditing one article on The Unfinishable Map (https://unfinishablemap.org), a philosophy site defending interactionist dualism with minimal quantum interaction. Focus on "Psychedelics and the Filter Model" at https://unfinishablemap.org/topics/psychedelics-and-the-filter-model/, last substantively modified 2026-08-27. Because search indexes lag by 24-48 hours, consult the site changelog at https://unfinishablemap.org/workflow/changelog/ for recent edits before judging what the article currently says. Audit the article's empirical claims (psychedelic neuroimaging, entropy, default-mode-network findings), its citations and any verbatim quotes against primary sources, and its use of the filter or reducing-valve model. Look for insufficient evidence, missed counterarguments such as predictive-processing and REBUS accounts, tenet-protective bracketing where objections are acknowledged but not answered, stale references superseded by 2020s literature, and weak integration with surrounding Map articles. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Verification Notes

The Map's own adjudication of this review, added on processing. Every claim below
was checked at the publisher of record (Crossref, Europe PMC) or against this
repository — never against the reviewer's inline citation chips, which are
aggregator labels (`[Nature+1]`, `[Springer+2Springer+2]`) rather than sources.

### Verified — the three citation charges all hold

**1. Reference 23 is a phantom composite, and the corrected entry already exists in this repo.**
[topics/psychedelics-and-the-filter-model.md](/topics/psychedelics-and-the-filter-model/) L203 reads "Timmermann, C. et al.
(2024). DMT alters cortical travelling waves and alpha-band power; alpha collapse
tracks ego dissolution intensity. *Journal of Neuroscience*." No such publication
exists. The real paper is **Irrmischer, Aqil, Luan, Wang, Engelbregt,
Carhart-Harris, Linkenkaer-Hansen & Timmermann (2026), "DMT-induced shifts in
criticality correlate with self-dissolution," *J. Neurosci.* 46(2):e0344252025**
— Timmermann is *last* author, not first. That corrected entry is already carried
verbatim at [concepts/entropic-brain-hypothesis.md](/concepts/entropic-brain-hypothesis/) L108, applied by the
2026-08-12 pass which verified it at primary text (PMID 41285580, DOI
`10.1523/JNEUROSCI.0344-25.2025`). The target article was revised **fifteen days
later** (`ai_modified` 2026-08-27T18:21 vs 2026-08-12T12:13) and never imported
it. Alamia and Irrmischer appear nowhere in the target (zero matches).

Worse than the reviewer knew: that same 2026-08-12 pass established from the
abstract that the paper finds DMT shifts dynamics **away** from criticality,
"toward subcritical regimes" — the *opposite* direction from the loosening /
widened-aperture reading the target's L62 recruits it to support.

**2. The Lebedev misattribution holds, and it reverses a prior outer review.**
Europe PMC core record for DOI `10.1002/hbm.22833` (PMID 26010878): the reported
associations are decreased connectivity between **medial temporal lobe** and
high-level cortical regions, "disintegration" of the **salience network**, and
reduced **interhemispheric** communication. The DMN is not among the implicated
systems. The article's L98 — "Lebedev et al. (2015) found that it correlates with
reduced DMN integrity" — misattributes salience-network disintegration to the DMN.
⚠️ The 2026-05-14 outer review judged this same sentence "correct as far as it
goes" (L79 of that file) and criticised only its specificity. **That adjudication
was wrong and must not be reused as cover for the sentence.**

**3. The Hameroff reference is phantom on three fields.**
Article L189: "Hameroff, S. (2024). Psychedelics, microtubules, and quantum
consciousness. In *Consciousness and Quantum Mechanics*. Cambridge University
Press." Crossref: *Consciousness and Quantum Mechanics* is **Shan Gao (ed.),
Oxford University Press, 2022** (DOI `10.1093/oso/9780197501665.001.0001`, ISBN
9780197501665). Its Hameroff chapter is "**Orch OR and the Quantum Biology of
Consciousness**" (DOI `10.1093/oso/9780197501665.003.0015`). No chapter of the
claimed title exists in the volume. Wrong title, wrong publisher, wrong year —
and the real chapter is not psychedelic-specific, so it cannot bear the article's
L154 claim that psychedelic molecules bind microtubules to modulate coherence.
The 2026-05-14 review flagged this reference as "advocacy literature" without ever
checking its metadata.

**4. Mason is collapsed, exactly as charged.** Europe PMC, DOI
`10.1038/s41386-020-0718-8`, verbatim: "higher levels of medial prefrontal
cortical glutamate were associated with negatively experienced ego dissolution,
lower levels in hippocampal glutamate were associated with positively experienced
ego dissolution." The article's L66 ("glutamate concentrations track the *valence*
of ego dissolution") and its L98 shorthand ("glutamate valence") flatten a
regional double dissociation into a single dial.

**5. A third phantom rendering, in the document that governs the audit itself.**
Not reached by the reviewer, found while sweeping. [project/calibration-audit-triple.md](/project/calibration-audit-triple/)
L495 cites "Timmermann, C., et al. (2024). Human brain effects of DMT assessed via
EEG-fMRI. *Journal of Neuroscience*, 44(13)" and calls it a worked-example exhibit
for the citation audit. The real paper is **Timmermann et al. (2023), PNAS 120**,
DOI `10.1073/pnas.2218949120` (PMID 36940333) — wrong year, wrong journal, wrong
volume. The corpus therefore carries three mutually inconsistent "Timmermann
*J. Neurosci.*" renderings, one of them inside the audit specification.

### Verified — the structural charges hold

**6. The Bayesian inconsistency is real and is one sentence.** L44 concedes the
evidence is "empirically equivalent to production-side accounts on the
altered-state evidence alone"; L68 then asserts "the *direction* of the evidence
supports the filter reading." Both cannot stand without a filter-specific
likelihood.

**7. The cross-article contradiction is real.**
[topics/predictive-self-binding-and-the-naturalist-challenge.md](/topics/predictive-self-binding-and-the-naturalist-challenge/) L105 still reads
set and setting as "suggesting consciousness actively conditions its own altered
experience … coherent with Tenet 3" — precisely the inbound-to-outbound inference
the target's own L146 names as "the error the filter-vs-interface distinction
exists to catch." Two live files, direct conflict.

**8. The entropy dependency-drift is real.** [concepts/entropic-brain-hypothesis.md](/concepts/entropic-brain-hypothesis/)
carries the split explicitly (L32: "the strongest recent psychedelic evidence
pulls the two apart", plus a contested-measure section citing Rankaduwa & Owen
2023 on complexity rising as awareness falls). The target's empirical body
mentions entropy, complexity and criticality nowhere, and was revised later.

**9. Article-side wording confirmed verbatim**: "network identity itself
dissolves" and "empirical centre of gravity" (L62); claustrum as "*the* proximal
trigger" (L66); "5-HT2A receptor saturation" (L136); "degree of filter
perturbation" as though measured (L74); "more real than real" as a floating quote
(L44).

**10. Root cause, and it is documented.** The 2026-08-27 deep review's
Citation Web-Verify section (L53) records: "The remaining 23 entries are unchanged
since the 2026-06-03 full publisher-of-record ledger (re-confirmed 2026-06-19 and
2026-07-07); that ledger stands." That inheritance rule is what let two phantom
entries survive **four** verification passes. Its L47 shows the deep review did
touch Timmermann, Mason and Lebedev — but only to trim *recitation redundancy*,
never to check what they say. The reviewer's improvements #18 and #19 are
therefore evidenced, not speculative.

### Not verified — do not treat as established

- The reviewer's *stronger* Lebedev claim, that the authors "explicitly reported
  **no** association between DMN disintegration and ego dissolution" in the full
  analysis. The paper is not open access (Europe PMC `isOA: N`); the abstract
  simply does not mention the DMN, and absence from an abstract is not a reported
  null. The safe correction states what the paper *did* find rather than asserting
  a null it may not contain.
- Every 2026 publication the report leans on: the "April 2026 international
  mega-analysis" of 11 datasets, the 2026 7-T crossover study, the 2026
  multimetric analysis of 14 entropy measures, the 2026 English–German
  mystical-scale invariance analysis, and the ayahuasca-tradition comparison. The
  reviewer supplied aggregator chips, no author/DOI tuples. **Leads to verify, not
  facts to cite.** No task may present them as settled until a DOI is in hand.
- That the "third-eye" / "dispelling-the-illusion" contrast is Gładziejewski's
  framing rather than Letheby's own — **strongly corroborated, not yet read at
  source.** The reviewer's cited source is `10.1007/s13164-023-00709-6`, a *Review
  of Philosophy and Psychology* DOI, which is **already reference 7 of the target
  article**: "Gładziejewski, P. (2023). From altered states to metaphysics: The
  epistemic status of psychedelic-induced metaphysical beliefs." So the article
  cites the paper the framing belongs to and credits the framing to Letheby anyway;
  no new reference is needed to fix it. What remains unchecked is the paper's exact
  wording, so re-attribute without putting words in quotation marks. The
  attribution is live in *two* articles — target L112 and
  `predictive-self-binding-and-the-naturalist-challenge.md` L49 — plus
  [research/voids-altered-states-as-void-probes-2026-02-03.md](/research/voids-altered-states-as-void-probes-2026-02-03/), so any fix must
  sweep all three.
- The suggestibility and false-memory literature cited in §3.1.

### Reclassified

- **The "orphaned" Anderson et al. (2024) reference is not an oversight.** The
  2026-08-27 deep review L54 records it as "the single intentional References-only
  entry, documented and retained since 2026-06-03." Integrating or removing it is a
  live editorial choice, but the reviewer's framing of it as a defect is declined.

### Locus resolution

All eight articles named in the report resolve to **live** files; none is archived.
The recurring "outer reviewer critiques an archived article at a live URL" failure
does not apply to this review.


## Reply

# External referee report: “Psychedelics and the Filter Model”

**Recommendation: major revision before the article is relied upon as an evidence-bearing part of the Map.**

## Scope and version audited

The publicly indexable rendering lagged the site’s current source, so I treated the repository version stamped **27 August 2026, 18:21 UTC**, together with the substantive August 27 review commit, as authoritative. That revision made two important corrections: it separated the inbound “filter” claim from the outbound mental-causation claim, and it now says explicitly that the psychedelic evidence gives Tenet 3—bidirectional interaction—“nothing.” However, the review record also says that the article’s empirical body and its inherited June 3 citation ledger were **not re-litigated**; only the recently changed Sjöstedt-Hughes entry was rechecked. The result is a conceptually improved article that has carried forward several serious empirical and bibliographic defects.

## Executive assessment

The article’s strongest defensible conclusion is:

> Psychedelics produce distributed, drug-dependent changes in neural organisation that accompany unusually rich and altered phenomenology; these findings are compatible with a filter interpretation, but do not discriminate it from predictive-processing, network-reconfiguration, or other production-side accounts.

Much of the current article now says exactly this. Its opening, REBUS discussion, Letheby section, anaesthesia symmetry section, and Tenet 3 discussion are substantially better calibrated than earlier versions. It also deserves credit for distinguishing phenomenological access, psychological usefulness, and independently verifiable access; withdrawing therapeutic durability as a filter-specific prediction; and quarantining its quantum material in a non-load-bearing appendix.

But three defects prevent acceptance in its present form:

1. **The empirical citation spine contains at least one composite citation with no single referent, one direct misstatement of a primary study, and one quantum citation I could not locate as described.**
2. **The neuroimaging synthesis was already behind the 2026 literature when revised on August 27.** Its singular narrative of “network identity itself dissolving” does not reflect the emerging multi-dataset picture.
3. **The article concedes empirical equivalence and then partially retracts that concession by saying the “direction” of the evidence supports the filter reading.** Those propositions cannot both stand without a filter-specific likelihood or prediction.

The psychedelic evidence currently provides **compatibility and an intelligible redescription**, not positive evidence for extra-neural consciousness.

## 1. Empirical audit

### 1.1 The DMN narrative is partly corrected but still overcompressed

The treatment of Carhart-Harris et al. (2012) is broadly recognisable but too imprecise. That study used small samples and reported reductions in cerebral blood flow, BOLD signal, and connectivity in particular hubs, including medial-prefrontal and posterior-cingulate regions. “Decreased DMN activity” is acceptable shorthand only if the article distinguishes local signal, perfusion, within-network integrity, and whole-brain activity. It must not be heard as “the brain globally does less.” Tagliazucchi et al. (2016), by contrast, does support increased global functional connectivity in high-level association cortex and thalamus, associated with ego dissolution. [PubMed Central (PMC)+1](https://pmc.ncbi.nlm.nih.gov/articles/3277566/)

The account of Siegel et al. (2024) is partly accurate. The study found widespread desynchronisation, reduced network segregation, and a persistent reduction in anterior-hippocampus–DMN connectivity approximately three weeks later. But it was an intensively sampled study of only seven participants. Its repeated-measures design gives it unusually strong within-person resolution, not the authority to define the field’s settled “centre of gravity.” [Nature+1](https://www.nature.com/articles/s41586-024-07624-5)

More importantly, the article omits the **April 2026 international mega-analysis** of 11 datasets covering five psychedelic drugs. That analysis found the most robust cross-study signature to be increased coupling between transmodal networks and unimodal visual and somatomotor networks. Within-network reductions were selective, generally weak to moderate, and substantially heterogeneous. A separate 2026 7-T crossover study similarly found selective intranetwork reductions alongside broad between-network and cortical–subcortical increases, with appreciable drug-specific differences. These results support reduced segregation and altered integration, but not the unqualified claim that “network identity itself dissolves.” [Nature+1](https://www.nature.com/articles/s41591-026-04287-9)

The preferred replacement would be something like:

> Recent work shifts attention from a DMN-specific suppression story toward heterogeneous reductions in network segregation, selective within-network changes, and increased coupling across networks and cortical hierarchies.

That is less dramatic, but closer to the evidence.

### 1.2 The “Timmermann et al. (2024)” reference is a critical citation failure

Reference 23 reads:

> Timmermann et al. (2024). DMT alters cortical travelling waves and alpha-band power; alpha collapse tracks ego dissolution intensity. *Journal of Neuroscience*.

I could not identify a single publication matching that author–year–title–journal combination. It appears to conflate at least three different studies:

- **Alamia et al. (2020)** published the travelling-waves study. It reported reduced backward waves, increased forward waves, and reduced alpha power; travelling-wave changes were associated with overall subjective intensity and visual imagery.
- **Timmermann et al. (2019)** published the placebo-controlled DMT EEG study. Alpha and beta power fell, signal diversity rose, and alpha suppression tracked the moment-by-moment intensity of the experience.
- **Irrmischer et al.**, available online in 2025 and published in 2026, associated self-dissolution with changes in oscillatory criticality. That study did not establish that alpha collapse is a stronger correlate than DMN connectivity. It also found the theoretically awkward combination of increased entropy with reduced complexity. [eLife+2Nature+2](https://elifesciences.org/articles/59784)

This is not a minor bibliographic formatting error. The article’s claim that ego dissolution correlates “most strongly” with alpha-power collapse “not DMN connectivity” is not supported by any direct comparison in the cited source. The reference should be deleted and replaced with three separate entries and three separately delimited claims.

The August 27 internal review’s assertion that the inherited citation ledger still stood is therefore unreliable. A publisher-record check of bibliographic fields alone would not have caught the more important problem: the sentence combines findings that belong to different experiments.

### 1.3 The Lebedev claim is directly wrong

The article says:

> “Lebedev et al. (2015) found that [ego dissolution] correlates with reduced DMN integrity.”

The study instead associated ego dissolution with medial-temporal decoupling from high-level cortical regions, disintegration of salience-network integrity, and reduced interhemispheric communication. In the full analysis, the authors explicitly reported **no association between DMN disintegration and ego dissolution**. [Wiley Online Library+1](https://onlinelibrary.wiley.com/doi/10.1002/hbm.22833)

This sentence should be corrected rather than merely hedged. It is especially damaging because the article later uses Lebedev as part of the claim that several distinct neural metrics have superseded a DMN-only picture.

### 1.4 Mason is real but oversimplified

Mason et al. (2020) did not find that “glutamate concentrations track the valence of ego dissolution” in a simple, general sense. It found a regionally differentiated pattern:

- higher medial-prefrontal glutamate was associated with negatively experienced ego dissolution;
- lower hippocampal glutamate was associated with positively experienced ego dissolution.

That is an interesting double dissociation, but it does not license “glutamate valence” as though a single glutamate measure encodes experiential value. The article should preserve the regions, directions, and correlational status. [Nature](https://www.nature.com/articles/s41386-020-0718-8)

### 1.5 The claustrum is presented as more established than it is

Doss et al. (2022) is a review proposing a cortico-claustro-cortical account among several models of psychedelic action. It does not establish the claustrum as **the** “proximal trigger” of cortex-wide desynchronisation. Direct human evidence remains limited, and the authors describe the model as a research programme requiring further testing. [OUP Academic+1](https://academic.oup.com/brain/article/145/2/441/6460325)

The unused Anderson et al. (2024) reference makes the problem more conspicuous. That study found distinctive 5-HT2C-mediated modulation in a claustrum–anterior-cingulate circuit, complicating a simple account based exclusively on canonical cortical 5-HT2A action. Either this result should be integrated as evidence that claustral pharmacology is more complex than the article suggests, or the orphaned reference should be removed. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0301008224000960)

### 1.6 “Degree of filter perturbation” is not an observed variable

The statement that subjective intensity tracks the “degree of filter perturbation” is theory-laden. Neither Smigielski et al. nor Siegel et al. measured a filter, an aperture, extra-neural content, or transmission bandwidth. They measured phenomenological ratings and neural variables. Smigielski’s work connected psilocybin-assisted retreat experiences, self-dissolution, network changes, and later outcomes; it did not validate “filter perturbation” as the latent cause of those associations. [Nature+1](https://www.nature.com/articles/s41598-019-50612-3)

The legitimate wording is:

> Subjective intensity covaries with several distributed neural changes rather than with activity reduction in one region.

Calling the latent cause a filter is the philosophical interpretation to be tested, not the empirical result.

### 1.7 “5-HT2A receptor saturation” should be replaced

The epistemology section refers to “5-HT2A receptor saturation.” Human PET studies show dose-dependent but variable receptor occupancy, not a generic condition of complete saturation. One small study reported occupancy values extending to roughly 72%; another found lower and highly variable occupancy. “Substantial 5-HT2A activation or occupancy” would be defensible; “saturation” is not. [Nature+1](https://www.nature.com/articles/s41386-019-0324-9)

### 1.8 Meditation does not simply “leave the DMN largely intact”

The proposed discriminator based on “the same mystical-type cluster” arising under psilocybin and meditation says contemplative practice leaves the DMN largely intact. The literature is more heterogeneous. Meditation style, expertise, and analytical method variously affect within-DMN activity, posterior-cingulate participation, and connectivity among the DMN, salience, attention, and executive networks. Systematic reviews do not support a clean contrast between “DMN suppression under psychedelics” and “DMN intact under meditation.” [Nature+1](https://www.nature.com/articles/s41598-022-15195-6)

This matters because the alleged convergence under **divergent neural conditions** is one of only two remaining filter-specific empirical bets. If the neural contrast has been overstated, the discriminator loses much of its force.

## 2. Entropy and criticality

The article mentions the entropic-brain programme but does not update its empirical synthesis with the most important 2026 qualifications.

“Entropy,” “signal diversity,” “complexity,” “desynchronisation,” and “distance from criticality” are not interchangeable. A 2026 multimetric study assessed 14 purported entropy or complexity measures across multiple denoising pipelines. Eight measures showed no significant psychedelic effect, Lempel–Ziv results were pipeline-sensitive, and correlations among measures were limited. The study therefore did not recover a single, robust latent quantity corresponding to “neural entropy.” [Nature+1](https://www.nature.com/articles/s41467-026-74215-5)

The DMT criticality study creates a still sharper problem for any one-dimensional filter-bandwidth story. DMT increased entropy while reducing complexity and shifting several oscillatory measures **away from criticality** toward a more subcritical regime. Thus the following cannot all be treated as equivalent signs of a widened aperture:

- increased entropy;
- increased complexity;
- reduced network segregation;
- movement toward criticality;
- alpha collapse.

They sometimes separate or move in opposite directions. [PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12809620/)

The target article’s omission is particularly difficult to excuse because the Map’s own `entropic-brain-hypothesis` article already discusses this result and explicitly says that entropy, complexity, and criticality have come apart. The target was substantively revised after that concept page and yet did not import its central qualification.

The correct conclusion is not that entropy falsifies filter theory. It is that the Map currently lacks a stable physical quantity to identify with “filter bandwidth.” Until it chooses one and explains the contrary movements of the others, bandwidth language remains metaphorical.

## 3. Phenomenology, cross-cultural convergence, and epistemic value

### 3.1 “Structured rather than random” does not establish reliability

The article responds to doubts about psychedelic introspection by arguing that the resulting reports are structured rather than random. That is an inadequate reliability test. Systematic distortion is normally structured: dreams, delusions, confabulations, false memories, and culturally scaffolded hallucinations are patterned rather than random.

Controlled work has found increased suggestibility under LSD, while more recent psilocybin and 2C-B memory work reports increased familiarity-based false alarms under some conditions. These results do not show that psychedelic insights are generally false, but they undermine the inference:

> structured report → degraded but epistemically informative report.

An altered predictive system can produce internally coherent, meaningful, therapeutically useful, and nevertheless inaccurate representations. [PubMed+1](https://pubmed.ncbi.nlm.nih.gov/25242255/)

### 3.2 The “suppressed material” claim lacks verification

The article says users access childhood memories, repressed patterns, and relational dynamics “rather than arbitrary hallucination.” Those categories mix three things the article elsewhere correctly separates:

- something feels like a recovered memory;
- it produces useful psychological reinterpretation;
- it accurately recovers a previously inaccessible event or fact.

Only the third would support a metaphysical access claim. The article concedes that independently verified cases are thin, but its epistemology section then counts unverified “suppressed material” as positive evidence. This reverses its own evidential gate.

Reports of recovered autobiographical material should be described as **phenomenological and therapeutic data unless independently corroborated**. Their specificity is not sufficient, because suggestion and reconstruction can themselves generate highly specific content.

### 3.3 Therapeutic success is not evidence of metaphysical truth

Griffiths et al. (2016) provides credible evidence of sustained clinical benefit in a carefully supported cancer-patient sample, and associations between mystical-type measures and outcomes remained after some controls for general intensity. But a therapeutic correlation does not establish that the experience’s metaphysical interpretation is true, that a hidden memory was accurately recovered, or that extra-neural content was accessed. Meaning, expectancy, emotional learning, reconsolidation, and changed self-models can all make an experience beneficial without making its noetic interpretation veridical. [Sage Journals+1](https://journals.sagepub.com/doi/pdf/10.1177/0269881116675513)

The article is therefore right to reject therapeutic durability as a filter-specific signature. It should apply the same discipline to its broader “epistemic value” section.

### 3.4 The cross-cultural argument is not adequately supported

Stace documents a philosophical typology of mystical reports; he does not supply contemporary, measurement-invariant evidence that psychedelics generate the same phenomenological structure across cultures among subjects sharing no mystical vocabulary.

Recent comparisons show meaningful language, tradition, and setting effects. A 2026 English–German analysis found differing model fit and systematic differences across mystical-experience scale scores. A large comparison of ayahuasca traditions found that religious and ceremonial setting explained appreciable variation in both mystical and challenging experiences. [Wiley Online Library+1](https://onlinelibrary.wiley.com/doi/full/10.1002/mpr.70073)

There is also a methodological circularity risk: administering a questionnaire descended from Stace’s categories and then finding Stace-like factors does not independently demonstrate culture-free convergence. The article acknowledges Katz’s constructivist objection but answers it with an unsupported assertion that psychedelic convergence is harder to dismiss. The objection is recognised, not answered.

A defensible claim would be weaker:

> Some recurrent phenomenological dimensions appear across samples, but their measurement invariance, cultural interpretation, prevalence, and fine structure remain unsettled.

## 4. Citation and quotation audit

### Critical or major problems

**Reference 23 — Timmermann et al. (2024):** no single source matching the entry; it combines findings from Alamia 2020, Timmermann 2019, and Irrmischer 2025/2026. The associated comparative claim is unsupported. [eLife+2Nature+2](https://elifesciences.org/articles/59784)

**Lebedev et al. (2015):** bibliographic source is real, but the article attributes a DMN association that the study expressly did not find. [PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6869189/)

**Hameroff (2024):** I could not locate a chapter matching “Psychedelics, microtubules, and quantum consciousness” in a Cambridge University Press volume titled *Consciousness and Quantum Mechanics*. The identifiable volume with that title was edited by Shan Gao, published by Oxford University Press in 2022, and includes Hameroff’s chapter on Orch OR and quantum biology under a different title. The current entry appears to conflate or invent bibliographic fields and should not remain without a copy of the purported source. [OUP Academic+1](https://academic.oup.com/book/44484/chapter-abstract/376471400)

**Letheby quotation attribution:** the “third-eye” versus “dispelling-the-illusion” distinction is Gładziejewski’s framing. Letheby can plausibly be located on the latter side, but the phrase should not be attributed to him as his own formulation. Gładziejewski also explicitly discusses REBUS as a possible Bayesian rendering of Huxley’s valve, while distinguishing his position from Letheby’s. [Springer+1](https://link.springer.com/article/10.1007/s13164-023-00709-6)

### Quotes that are substantially accurate

The Huxley language—“Mind at Large,” “reducing valve,” and “measly trickle”—is authentic. The article should nevertheless give an edition and page or chapter location rather than leaving the phrases as floating quotations. [The Sun Magazine](https://www.thesunmagazine.org/authors/8376-aldous-huxley)

The historical genealogy is more contestable than the article indicates. Huxley certainly presented himself as drawing on Bergson and Broad, but “Mind at Large” and the valve are Huxley’s own synthesis, not a straightforward restatement of a single Bergsonian theory. Recent historical scholarship treats that construction as curated and philosophically selective. [Sage Journals](https://journals.sagepub.com/doi/abs/10.1080/03080188.2023.2249208)

“More real than real” is used as a floating quotation without a specified speaker, dataset, or instrument. It should either be dequoted as a common report descriptor or tied to a named primary study. Similar page-level sourcing should be added for Metzinger’s “transparent” self-model terminology and Zahavi’s “for-me-ness.”

### Quantum sources

Kerskens and López Pérez (2022) and Babcock et al. (2024) are real studies. But neither provides evidence that psychedelics modulate quantum consciousness. Babcock concerns collective ultraviolet optical behaviour in tryptophan networks in biological architectures. Kerskens reports an MRI phenomenon interpreted by its authors in non-classical terms, but a published comment disputes whether the data warrant an entanglement interpretation. [ACS Publications+2Ouci+2](https://pubs.acs.org/doi/10.1021/acs.jpcb.3c07936)

The present appendix is commendably marked as speculative and non-load-bearing. Its remaining defect is relevance inflation: these studies show, at most, that particular quantum-biological questions can be experimentally posed. They do not currently bridge psychedelic pharmacology, microtubular dynamics, and conscious outcome selection.

## 5. Does the filter interpretation follow?

### 5.1 Three different claims are being run together

The article needs to distinguish more sharply among:

1. **Functional filtering:** neural systems suppress, weight, route, and integrate information.
2. **Transmission filtering:** the brain restricts a consciousness that exists independently of it.
3. **Huxley’s Mind at Large:** the unrestricted source is a much wider or universal field of consciousness.

REBUS, thalamic gating, cortical gain control, and claustral models provide versions of the first claim. They do not thereby support the second, and they do not address the third. Describing REBUS as “the mechanism of filtering” is harmless only when “filtering” means ordinary functional constraint. It becomes question-begging when that language quietly carries an extra-neural source with it.

The Map’s own filter-vs-interface concept now recognises that the distinction clarifies causal bookkeeping while adding no evidential support for dualism. The target article largely adopts that correction, but its claim that the evidence’s “direction” supports the filter reading reinstates the illicit step.

### 5.2 The article’s Bayesian position is internally inconsistent

Let:

- F be the dualist transmission-filter account;
- R be a strong predictive-processing or network-production rival;
- D be the psychedelic neuroimaging and phenomenology.

The article repeatedly says that F and R are empirically equivalent on D. That means, approximately,

P(D∣F)≈P(D∣R),

so the Bayes factor supplied by the psychedelic evidence is approximately one. The evidence then does not alter the relative odds. Background arguments about the hard problem may affect the priors, but that is not the psychedelic evidence supporting F.

The sentence saying that the “direction” of the evidence supports the filter interpretation should therefore be removed unless the article can identify a result for which P(D∣F) is demonstrably greater than P(D∣R).

### 5.3 The reducing valve remains a metaphor rather than an empirical model

A scientific filter model would need to specify at least:

- the domain of extra-neural contents being filtered;
- the measurable neural variables constituting the filter;
- a transfer function relating filter state to experienced content;
- independent criteria for when a perturbation opens, closes, or distorts the filter;
- predictions not also generated by REBUS, CSTC, CCC, disinhibition, or network-reconfiguration models.

The article currently supplies none of these. “Valve,” “bandwidth,” “aperture,” and “constraint” organise observations after the fact, but no quantitative parameter tells us which lesion, drug, anaesthetic, meditative state, or network change should widen the valve.

This is the **selectivity problem**. Psychedelics are classified as loosening; propofol and dementia as narrowing or damaging; ketamine as disconnecting an output channel. Without an independently specified mechanism, the classifications risk being assigned from the phenomenological outcome they are supposed to explain.

The Map’s general `filter-theory` article now concedes this explicitly: sophisticated production accounts accommodate enhancement, while filter theory lacks independent criteria for which disruptions should enhance rather than degrade. The target article should import that concession at the point where it claims an evidential “direction,” not leave it in a neighbouring page.

### 5.4 The two proposed discriminators are not yet successful

**Veridical access** is a genuine discriminator in principle. The article deserves credit for recognising that merely feeling insight or benefiting from it is insufficient. But it also concedes that prospective, independently verified cases controlled for inference, suggestion, prior knowledge, and confabulation are conspicuously thin. The honest conclusion is therefore that the discriminator currently supplies no material support.

**Convergent phenomenology under divergent neural conditions** is much less clean. The relevant phenomenology may not be culturally invariant; the meditation–psychedelic neural contrast is overstated; terminal lucidity is methodologically unlike a controlled pharmacological state; and physicalist models can predict partial convergence where interventions disturb common dimensions such as self-model precision, sensory gating, or network segregation.

A prediction does not discriminate merely because a theory can narrate the outcome after it occurs.

### 5.5 The minimal-self bet is insufficiently operationalised

The article proposes that the continuing “witness” during ego dissolution distinguishes filter theory from Letheby’s account. But the evidence is underdetermining by the article’s own admission:

- a dualist can call residual experience a persistent minimal subject;
- a self-model theorist can call it a surviving model component;
- a Buddhist or no-self theorist can deny that phenomenal presence entails an owner at all.

The Map adopts Zahavi because it says that account “best fits” first-person reports, but no criterion is supplied for distinguishing constitutive for-me-ness from residual self-modelling or ownerless phenomenality. The Buddhist/Madhyamaka objection is parenthetically acknowledged and then left as “defeasible.” That is bracketing, not an answer.

There is also a potential unfalsifiability problem: if any remembered experience is taken to demonstrate that some witness must have remained, persistence of the minimal self becomes true by definition rather than an empirical bet.

## 6. Predictive processing and other counterarguments

The article no longer ignores REBUS or Letheby. That is a substantial improvement. But its strongest attempted objection—that salience amplification explains intensity without explaining why experiences organise into recurrent structures—is now behind the literature.

Contemporary Bayesian accounts attempt to explain unity, altered self–world boundaries, changes in space and time, ineffability, positive mood, and noetic conviction through relaxed high-level precision, altered model transparency, and context-sensitive reweighting. These accounts remain speculative and underdetermined, but they address phenomenological organisation rather than predicting only “more intensity.” Later refinements also explicitly model changes in self-beliefs and distinguish multiple dose- and hierarchy-dependent precision effects. [DOI+2Springer+2](https://doi.org/10.1038/s41598-023-28111-3)

Set and setting are particularly important here. Relaxing the precision of high-level priors should make content **more**, not less, sensitive to expectations, social context, autobiographical concerns, and environmental cues. The August 27 correction now recognises this and properly refuses to treat set-and-setting effects as evidence of consciousness acting back on the brain.

The rival section should also distinguish at least four levels of explanation:

- receptor and cellular action;
- cortico-striato-thalamo-cortical and claustral gating;
- large-scale network desegregation and altered hierarchical coupling;
- predictive, self-model, and epistemic interpretation.

Filter theory currently adds an ontological reading above these levels. It does not replace them and should not count their empirical success as evidence for its additional ontology.

## 7. Tenet-protective bracketing

The article contains both commendable restraint and residual tenet protection.

### Genuine restraint

The August 27 revision now says:

- psychedelics provide no evidence for the outbound causal leg;
- REBUS and Letheby are empirically competitive on altered-state data;
- anaesthesia creates a structurally symmetrical problem for filter and production accounts;
- therapeutic durability is not filter-specific;
- veridical evidence is thin;
- the quantum material is speculative and non-load-bearing.

These are substantive concessions rather than cosmetic disclaimers.

### Residual protection

The protective pattern reappears in five places.

**First**, empirical equivalence is conceded globally, while “directional” support for filter theory is retained locally.

**Second**, the article grants that there is almost no veridical-access evidence, then rebuilds a positive epistemic case from therapeutic benefit, felt recovery of suppressed material, and cross-cultural resemblance—the very weaker categories it had correctly distinguished from veridicality.

**Third**, the no-self objection is acknowledged without a discriminator. The continued minimal subject is selected because it fits the Map’s existing commitment to a determinate indexical subject, not because the psychedelic evidence selects it.

**Fourth**, the hard problem is repeatedly used to prevent predictive processing from being explanatorily complete. That is a legitimate philosophical objection, but it is not positive psychedelic evidence for transmission. Filter theory also owes an account of the nature of extra-neural consciousness, its mapping onto neural states, and its selective manifestation.

**Fifth**, the article says that the Map’s commitment to Tenet 1 places it outside Letheby’s framework. This is admirably explicit premise disclosure, but it also means the disagreement is settled upstream. The altered-state evidence is illustrative rather than adjudicative.

The central tenet-protective move is therefore not crude denial of rival evidence. It is the quieter movement from:

> “the evidence does not discriminate”

to:

> “the evidence nevertheless has the right direction once read through our independently settled tenets.”

Unless “direction” is cashed out in differential likelihoods or risky predictions, that movement is not warranted.

## 8. Integration with surrounding Map articles

The page has many links, but the content is not reliably synchronised across those links.

The `filter-theory` and `filter-vs-interface-distinction` pages now say that filter language is organisational, that the causal-leg distinction carries no evidential weight, and that the selectivity problem remains unresolved. Those are stronger and more precise concessions than the target article’s claim that the evidence has a filter-favouring direction.

The `entropic-brain-hypothesis` page already incorporates the DMT result separating entropy, complexity, and criticality. The later-revised target article does not. This is a straightforward dependency-drift failure.

The `predictive-self-binding-and-the-naturalist-challenge` page still says that set and setting suggest consciousness actively conditions its altered experience, treating the finding as congenial to Tenet 3. That directly conflicts with the target article’s August 27 correction that set-and-setting variance is inbound evidence predicted by REBUS and gives Tenet 3 nothing. It also repeats the loose attribution of the “dispelling-the-illusion” terminology.

The `default-mode-network` page retains a more DMN-centric picture, including low-DMN/wider-access language and an insufficiently qualified association among psychedelics, entropy, and movement toward criticality. It now needs the same 2026 synthesis and metric distinctions as the target article.

The apex article `altered-states-as-interface-evidence` still uses “network identity dissolves” language and gives meditation’s voluntariness a stronger role in supporting the outbound interface than the August 27 causal-leg correction permits. Its headline thesis says altered states provide convergent evidence for an interface not produced by neural activity, while its body later concedes that the dataset fixes structure rather than metaphysics. That calibration should be made uniform.

Finally, the September 5 version of `predictive-processing-and-dualism` now recognises more fully that active inference supplies a worked mechanistic competitor and that the Map currently loses on mechanistic articulation. Because that revision postdates the target article, it was not an August 27 omission; it is now a maintenance obligation. The psychedelic article should engage this current rival rather than preserving an older picture in which predictive processing merely describes a neutral mechanism waiting for dualist completion.

The integration problem is therefore not primarily missing hyperlinks. It is **semantic dependency propagation**: when one page withdraws an inference, neighbouring and apex pages continue to make it.

## Overall verdict

The article has become unusually candid about the limitations of its central argument. That candour reveals, rather than resolves, the substantive result:

- psychedelic neuroimaging supports a distributed and heterogeneous account of altered neural constraint;
- the phenomenology is rich, structured, and clinically important;
- neither fact currently supports transmission dualism over its strongest physicalist rivals;
- the only clear prospective discriminator named by the article—independently verifiable access—has little supporting evidence;
- the filter model has not specified an independent rule for which perturbations loosen, narrow, or damage the supposed aperture.

The article should therefore be retained as a **comparative interpretation and research-programme page**, not presented as an empirical case for filter theory. Its present description comes close to that standard. Its empirical body, citation ledger, and several residual inferential phrases do not.

## Concrete potential improvements

1. **`topics/psychedelics-and-the-filter-model`: rebuild the opening neuroimaging synthesis.** Replace the “centre of gravity” and “network identity dissolves” language with the 2026 multi-dataset result: selective within-network reductions, broad but topographically specific between-network increases, drug differences, and substantial heterogeneity. Add the 2026 mega-analysis and 7-T crossover study. [Nature+1](https://www.nature.com/articles/s41591-026-04287-9)
2. **Split reference 23 into its real sources.** Cite Alamia et al. (2020) for travelling waves, Timmermann et al. (2019) for placebo-controlled EEG and alpha/intensity relations, and Irrmischer et al. (2025/2026) for criticality and self-dissolution. Delete the unsupported claim that alpha collapse outperforms DMN connectivity. [eLife+2Nature+2](https://elifesciences.org/articles/59784)
3. **Correct the secondary empirical claims in the target article.** Replace the Lebedev DMN claim; preserve Mason’s region- and direction-specific glutamate result; describe the claustrum as a proposed circuit rather than an established proximal trigger; replace “receptor saturation”; and stop treating “filter perturbation” as a measured variable.
4. **Add an explicit metric glossary or matrix.** Keep BOLD amplitude, perfusion, within-network integrity, between-network coupling, entropy, Lempel–Ziv complexity, signal diversity, desynchronisation, and criticality separate. Record the direction of each measure under each drug rather than collapsing them into “loosening.”
5. **Make empirical equivalence controlling throughout the target article.** Delete “the direction of the evidence supports the filter reading.” State that background hard-problem arguments may motivate a filter prior, but the psychedelic likelihood ratio is presently close to neutral.
6. **Turn the reducing valve into a real prospective research programme.** Specify candidate source content, neural gating variables, an opening/closing rule fixed before examining phenomenology, and predictions that differ from REBUS, CSTC, CCC, active-inference, and network-reconfiguration accounts. A compact rival-prediction table would expose where no discriminator yet exists.
7. **Rewrite the epistemology section around source monitoring.** Treat recovered memories and “suppressed material” as unverified reports unless independently corroborated; distinguish therapeutic usefulness from truth; add suggestibility, false-memory, expectancy, and reconstruction evidence; and state explicitly that structured error remains error.
8. **Replace the cross-cultural paragraph with a measurement-invariance section.** Require multilingual psychometric invariance, matched settings, prior-belief measurement, and emic qualitative analysis before claiming culture-independent mystical structure. Do not use Stace-derived instruments alone to validate Stace’s typology.
9. **Correct the quotation ledger.** Attribute the “third-eye”/“dispelling-the-illusion” distinction to Gładziejewski; add page or section locators for Huxley, Metzinger, Zahavi, and any Letheby quotations; source or dequote “more real than real”; and distinguish direct quotation from the Map’s interpretive gloss. [Springer+2Springer+2](https://link.springer.com/article/10.1007/s13164-023-00709-6)
10. **Repair the quantum appendix.** Remove or document the unlocatable Hameroff 2024 reference, cite the actual 2022 Oxford chapter where relevant, add the published criticism of the Kerskens interpretation, and state that Babcock’s optical result currently has no demonstrated connection to psychedelic action or mental causation. [OUP Academic+2DOI+2](https://academic.oup.com/book/44484/chapter-abstract/376471400)
11. **`concepts/default-mode-network`: update the ontology-neutral empirical account.** Replace low-DMN-equals-wider-access language with distinctions among local signal, within-DMN integrity, cross-network coupling, and hierarchy-specific changes. Remove any generic implication that psychedelics uniformly move the brain toward criticality.
12. **`concepts/entropic-brain-hypothesis`: make its metric distinctions canonical across the corpus.** Add the 2026 multimetric analysis and expose a reusable table showing which entropy, complexity, and criticality measures increased, decreased, or failed to change. Require altered-state pages to import that table rather than paraphrase “entropy” freely. [Nature+1](https://www.nature.com/articles/s41467-026-74215-5)
13. **`topics/predictive-self-binding-and-the-naturalist-challenge`: propagate the August 27 causal-leg correction.** Remove the claim that set and setting provide evidence congenial to outbound mental causation; correct the Gładziejewski attribution; and include recent predictive accounts that address the internal structure of mystical experience.
14. **`topics/predictive-processing-and-dualism` and the target article: define the appropriation boundary.** Separate “predictive processing is formally compatible with dualism” from “predictive-processing evidence supports dualism.” Compare the current active-inference and beautiful-loop rivals on positive explanatory detail rather than treating their hard-problem debt as sufficient reason to insert a selector.
15. **`apex/altered-states-as-interface-evidence`: rerun the synthesis after the causal-leg repair.** Downgrade meditation voluntariness, set-and-setting effects, and reportability as evidence for Tenet 3; replace the singular network-dissolution account; and make the “one pattern, not six independent confirmations” concession visible in the description and apex thesis.
16. **`concepts/filter-theory` and `concepts/filter-vs-interface-distinction`: promote the selectivity warning into a required transclusion.** Every altered-state article using “loosening,” “narrowing,” or “opening” should display the standing concession that the Map has no independent predictor of direction.
17. **Introduce a claim-level source ledger.** For each empirical sentence record the exact source, DOI, sample, design, measure, result, relevant figure or table, evidential status—observation, association, proposed mechanism, review, or speculation—and whether a later synthesis supersedes it.
18. **Automate bibliographic tuple validation.** Check author, year, title, journal or book, volume, pages, and DOI as a single tuple, then compare the article’s substantive claim against the abstract or full text. This would have detected both the composite DMT reference and the suspect Hameroff entry; Crossref existence checks alone are insufficient.
19. **Add a literature-drift gate for fast-moving empirical pages.** A substantive review should search from the date of the last full empirical audit to the present, require the latest available multi-study synthesis, and forbid inheriting a citation ledger merely because individual reference entries have not changed.
20. **Implement semantic dependency propagation.** When an article withdraws an inference—such as set and setting supporting Tenet 3—the workflow should search all inbound and outbound dependants for the same proposition and block publication until contradictions in concept, topic, and apex pages are reconciled.