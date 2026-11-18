---
ai_contribution: 90
ai_generated_date: 2026-11-18
ai_modified: 2026-11-18 05:54:20+00:00
ai_system: claude-fable-5-2
author: Andy Southgate
concepts:
- '[[minimal-consciousness]]'
- '[[introspection]]'
- '[[illusionism]]'
created: 2026-11-18
date: &id001 2026-11-18
description: External audit of the minimal consciousness void by Claude Fable 5.2,
  which could not load the page; reconstructed from the research note and dependency
  pages.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-18 05:54:20+00:00
modified: *id001
outer_review_conversation_url: https://claude.ai/chat/3c2a81dd-4c81-4469-9351-98b9e0087dbf
outer_review_extraction_method: js-dom
outer_review_status: processed
related_articles:
- '[[project]]'
- '[[minimal-consciousness-void]]'
- '[[degrees-of-consciousness]]'
- '[[edge-states-and-void-probes]]'
subject_articles:
- voids/minimal-consciousness-void.md
subject_source: reuse:pending-reviews:outer-review-2026-11-18-chatgpt-5-6-sol-pro.md
subject_title: Audit minimal-consciousness-void
subject_type: recent
title: Outer Review - Claude Fable 5.2 (2026-11-18)
topics:
- '[[hard-problem-of-consciousness]]'
- '[[philosophy-of-mind]]'
---

**Date**: 2026-11-18
**Reviewer**: Claude Fable 5.2
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Please act as a hostile but fair academic referee and audit one article from The Unfinishable Map (https://unfinishablemap.org), a philosophy-of-mind site arguing for interactionist dualism. The article is its page on the minimal consciousness void, live at https://unfinishablemap.org/voids/minimal-consciousness-void/ (please fetch and read that exact page directly rather than relying on search snippets, since search indexes lag the site by 24-48 hours). Recent edits are logged at https://unfinishablemap.org/workflow/changelog/. Audit its claims, citations and counterarguments: check every attributed quotation and reference against the primary source, flag misattributions, overstated or unsupported empirical claims, missing literature (especially work from the 2020s), places where the argument concedes too much or too little, and the strongest physicalist and illusionist objections the article fails to answer. Say explicitly whether you were able to load the article page itself. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Referee Audit: “The Minimal Consciousness Void” (voids/minimal-consciousness-void), The Unfinishable Map — audited 18 November 2026

I could not load the article page itself. On the evidence I could reach, the article’s central thesis is a defensible methodological observation that has been inflated into a structural, quasi-metaphysical “unexplorable” void. Its sources do not support that inflation, its own research note disowns it, and sister pages amplify it. Treat this audit as a reconstruction from the article’s research note, its June 2026 external reviews, and its live dependencies, not as a line-by-line audit of today’s text.

## Part 1 — TL;DR and headline verdict

- **Load status (read this first):** Every attempt on 18 November 2026 to fetch [voids/minimal-consciousness-void](https://unfinishablemap.org/voids/minimal-consciousness-void/) was refused by the fetch layer, including a dedicated retrieval attempt. No search result ever returned the article URL itself. The live changelog did load, but only partially: entries from about 2026-11-16T23:51 to 2026-11-18T04:04 UTC. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/) None of those entries names this article. What I relied on instead: the research note voids-minimal-consciousness-void-2026-02-22 (last modified 2026-08-05); the 2026-06-02 Gemini outer review, which quotes the article by line number; task-queue entries recording a consolidated 2026-06-02 prose pass (commit d81d4068); [workflow/todo](https://unfinishablemap.org/workflow/todo/) and the live dependencies concepts/minimal-consciousness (modified 2026-09-25) and voids/edge-states-and-void-probes (modified 2026-10-24). [workflow/todo](https://unfinishablemap.org/workflow/todo/)[research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/) This is a serious limitation. Every finding about the article’s current wording is provisional, and the owner should re-run the verbatim checks below against the live text.
- **Headline verdict: REVISE-HARD overall, with targeted DELETE/DEMOTE.** The core “accessible minimum vs actual minimum” distinction is sound and worth keeping. Three things are not:

- The upgrade from “concurrent introspection perturbs its target” to “consciousness cannot investigate its own lower bound” is an epistemic-to-metaphysical slide. [workflow/todo](https://unfinishablemap.org/workflow/todo/)
- The upstream research note’s tenet-alignment claims are textbook co-optation firewall failures. Hume is said to “support Dualism”, and Schooler and the nirodha literature are said to support Bidirectional Interaction. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/)
- The dependency concepts/minimal-consciousness says the void article “establishes” the enrichment thesis, while the research note concedes the enrichment problem “remains more analogy than theorem”. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/)[research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/) That is confession-without-correction in its purest form.
- **Blocking gate failed:** I found no evidence that the article engages Laukkonen, Friston & Chandaria 2025, “A beautiful loop” (Neuroscience & Biobehavioral Reviews 176:106296). [researchgate](https://www.researchgate.net/publication/394140382_A_beautiful_loop_An_active_inference_theory_of_consciousness) On the evidence available it ignores the paper. The site has residualized it to voids/edge-states-and-void-probes. [voids/edge-states-and-void-probes](https://unfinishablemap.org/voids/edge-states-and-void-probes/)[voids/edge-states-and-void-probes](https://unfinishablemap.org/voids/edge-states-and-void-probes/) That paper offers a fully naturalistic account of exactly the target phenomena (minimal phenomenal experience, cessation, deep-sleep awareness), and it undercuts the enrichment premise directly. [researchgate](https://www.researchgate.net/profile/Ruben-Laukkonen/publication/389740878_A_beautiful_loop_An_active_inference_theory_of_consciousness/links/67e4ff4ea43a11173be88d35/A-beautiful-loop-An-active-inference-theory-of-consciousness.pdf) On its model, reflexive “knowing” is constitutive of minimal experience rather than a contaminant added by introspection. [Substack](https://rubenlaukkonen.substack.com/p/a-beautiful-loop)

## Part 2 — Dimensional analysis

### 2.1 What the article argues (reconstructed, with provenance flagged)

Here is the argument as reconstructed from the research note, the Gemini review’s line-referenced quotations, and the dependencies:

1. **Enrichment premise.** Any act of attending to, introspecting on, or remembering an experience adds cognitive structure, so the observed experience is richer than the minimum. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) The research note calls this “the enrichment problem”. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/)
2. **Regress and report premises.** Trying to find the minimum of the examined experience generates a further layer, and any reportable experience has already been processed. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/)
3. **Accessible-vs-actual distinction.** What meditators reach may be the minimum accessible to introspection, with the actual minimum lying below. Gemini places this at article line 57. [reviews/outer-review-2026-06-02-gemini-2-5-pro](https://unfinishablemap.org/reviews/outer-review-2026-06-02-gemini-2-5-pro/)
4. **Convergence claim.** Metzinger’s MPE programme, Schooler’s paradox of introspection, IIT’s refusal to set a threshold, and Buddhist cessation reports “converge” on the boundary. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/)
5. **Cessation bracket.** Whether nirodha is genuine zero or minimal consciousness with amnesia “cannot be determined” (article lines 73–75, as quoted by the Gemini review’s verification notes). [reviews/outer-review-2026-06-02-gemini-2-5-pro](https://unfinishablemap.org/reviews/outer-review-2026-06-02-gemini-2-5-pro/)
6. **Classification.** The void is “Unexplorable / Occluded (Mixed)”, described as structural rather than contingent. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/)
7. **Site-perspective claims.** The task queue records reviewer complaints about two earlier formulations: “a purely physical phenomenon *would have* a discoverable minimum”, and “the void exists *precisely because* consciousness is causally efficacious”. The queue marks both as addressed in the 2026-06-02 consolidated pass. [workflow/todo](https://unfinishablemap.org/workflow/todo/) I could not verify whether they were removed or merely softened.

Fairness note: the Gemini referee’s charge that the article treats nirodha as a minimal state was correctly rebutted by the site’s own verification notes. The article brackets cessation as possible zero. [reviews/outer-review-2026-06-02-gemini-2-5-pro](https://unfinishablemap.org/reviews/outer-review-2026-06-02-gemini-2-5-pro/) The site also correctly caught Gemini misplacing Anil Seth among the IIT “pseudoscience” letter signatories. [reviews/outer-review-2026-06-02-gemini-2-5-pro](https://unfinishablemap.org/reviews/outer-review-2026-06-02-gemini-2-5-pro/) Both are credits to the article and the site.

### 2.2 Argument structure: where it breaks

**(a) The enrichment premise is equivocal across three readings.** It slides between:

- (i) concurrent attentive introspection perturbs its target, which is plausible and supported;
- (ii) any access whatsoever (retrospective sampling, no-report paradigms, third-person markers) perturbs the target, which is unsupported;
- (iii) the minimum is therefore structurally inaccessible, which does not follow.

Hume, whom the article invokes, is the cleanest counterexample to the inference. The passage concerns the impossibility of premeditated self-experiment in moral philosophy, and his remedy is third-person: experiments “from a cautious observation of human life”. [fiu](https://faculty.fiu.edu/~hauptli/Hume'sTreatiseBookI.html) The source the article recruits for an unexplorable void prescribes the method that would make it explorable.

**(b) The premise presupposes a single scalar of “richness”.** The site’s own concept page, citing Bayne, Hohwy & Owen 2016 and Birch, Schnell & Clayton 2020, concedes that minimality may be multidimensional. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/)[concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) If so, reflexive access enriches the access/metacognitive dimension without necessarily enriching phenomenal content. On Laukkonen–Friston–Chandaria, minimal phenomenal experience is precisely the configuration of maximal epistemic depth with a maximally simple reality model. [Substack](https://rubenlaukkonen.substack.com/p/a-beautiful-loop) Reflexivity is the signature of the state, not an observer artefact. The enrichment premise therefore begs the question against the leading empirical model of its own target.

**(c) Heads-I-win structure.** The concept page states that if minimality is plural, “the Map’s case strengthens rather than weakens”. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/)[concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) A thesis strengthened by both a one-dimensional and a multidimensional outcome is not being tested by either. This is coherence inflation.

**(d) Epistemic-to-metaphysical slide.** Several moves convert an access limit into evidence about the nature of consciousness:

- the research note’s claim that the void “is evidence that consciousness has intrinsic features that resist third-person analysis”; [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/)
- the concept page’s claim that the difficulty of identifying a threshold “provides indirect support for treating consciousness as irreducible”; [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/)[concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/)
- concepts/degrees-of-consciousness’s claim that the lower bound is “structurally inaccessible”. [concepts/degrees-of-consciousness](https://unfinishablemap.org/concepts/degrees-of-consciousness/)

None of these moves is licensed. Physicalists predict exactly this access profile.

**(e) The void is ontologically under-specified in a way that hurts dualism more than physicalism.** On the interface view (concepts/minimal-consciousness, “Interface dualism”), consciousness couples “wherever appropriate interface conditions exist”, with “no arbitrary threshold”. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) But “appropriate interface conditions” is itself a threshold predicate, and the Map supplies no account of it. The changelog’s 2026-11-17 entry concedes the Map lacks an “interface-eligibility law” in the AI-consciousness register. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/) The threshold problem has been relocated, not dissolved.

### 2.3 Empirical claims and their evidential status (compatible / suggestive / discriminating)

| Claim (as it appears in article or research note) | Ladder status | Comment |
| --- | --- | --- |
| Introspection distorts first-order experience (Schooler) | Suggestive for local distortion; not discriminating for a structural void | Schooler & Schreiber identify situations where introspection is accurate and propose covariation-based validation. [ingentaconnect](https://www.ingentaconnect.com/content/imp/jcs/2004/00000011/F0020007/art00003) That is a calibration programme, not an impossibility result. |
| MPE reports reveal “more structure” (12 factors, 92 items) [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/) | Compatible with both physicalism and dualism | A factor solution from a 92-item questionnaire will find structure by construction. The 1,403 usable responses (of 3,627 submitted) are retrospective self-reports. [plos](https://journals.plos.org/plosone/article) |
| Cessation shows a sharp on/off edge | Compatible | Laukkonen et al. 2023 is a review and research agenda with preliminary EEG from two adepts. [researchgate](https://www.researchgate.net/publication/379067279_Nothingness_in_meditation_Making_sense_of_emptiness_and_cessation) It does not show discontinuity of phenomenal consciousness. |
| IIT implies no threshold; photodiodes have “a modicum of experience” [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/) | Theory-internal; not evidence | Sourced to an encyclopedia. IIT is contested, including the 2023 open letter. [reviews/outer-review-2026-06-02-gemini-2-5-pro](https://unfinishablemap.org/reviews/outer-review-2026-06-02-gemini-2-5-pro/) The concept page correctly notes IIT is not an ally against physicalism. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) |
| Nirodha lasts “up to 7 days” and can be consistently induced [harvard](https://meditation.mgh.harvard.edu/files/Laukkonen_23_ProgressInBrainResearch.pdf) | Accurately reported as practitioner claims | Laukkonen et al. 2023 report this as practitioner testimony, not as verified measurement. [harvard](https://meditation.mgh.harvard.edu/wp-content/uploads/2024/02/Laukkonen_23_ProgressInBrainResearch.pdf)[harvard](https://meditation.mgh.harvard.edu/files/Laukkonen_23_ProgressInBrainResearch.pdf) |

No claim in the article reaches “discriminating”. By the site’s own Born-rule apex standard, the void should be labelled coherence-only with respect to every tenet.

### 2.4 Three-layer citation verification table

Article-level rows are reconstructed from the research note and review quotations because the live page could not be loaded. Re-check each row against the live References list.

| # | Citation / quotation as used | (a) Metadata | (b) Verbatim fidelity | (c) Author-stance accuracy | Verdict / primary source |
| --- | --- | --- | --- | --- | --- |
| 1 | Hume: reflection “would so disturb the operation of my natural principles…” | **ERROR (research note):** located at Treatise Book 1, Part 4, Section 6. It is in the Introduction (para. 10). Sourced second-hand via IEP. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/)[davidhume](https://davidhume.org/texts/t/full) | Verbatim correct, modulo spelling of “phænomenon”. | **FAIL.** Hume is discussing premeditated experiment in moral philosophy, and his remedy is third-person observation. He is a naturalist and bundle theorist. The research note’s “Supports Dualism” alignment is a co-optation. | Correct the locus; delete the dualism alignment. Primary: davidhume.org/texts/t/full; Project Gutenberg #4705 |
| 2 | Schooler & Schreiber 2004, JCS 11(7–8):17–39 | Correct (Ingenta, PhilPapers). [ingentaconnect](https://www.ingentaconnect.com/content/imp/jcs/2004/00000011/F0020007/art00003) | **MISQUOTE (research note):** rendered as “The paradox of introspection is that it is simultaneously so compelling yet so elusive”. The source reads “Introspection is paradoxical in that it is simultaneously so compelling yet so elusive”. [philpapers](https://philpapers.org/s/introspection)[research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/) The verbal-overshadowing “worse recognition” claim is not in this paper’s abstract; unverified. | **PARTIAL FAIL.** The paper documents both accurate and inaccurate introspection and offers a validation method. [ingentaconnect](https://www.ingentaconnect.com/content/imp/jcs/2004/00000011/F0020007/art00003) “Structural” impossibility overstates it. The “supports Bidirectional Interaction” alignment is co-optation. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/) | Fix the quotation; scope the claim. Primary: ingentaconnect.com/content/imp/jcs/2004/00000011/F0020007/art00003 |
| 3 | Metzinger 2020, “Minimal phenomenal experience…”, Philosophy and the Mind Sciences | Mostly correct. 1(I), article 7, DOI 10.33735/phimisci.2020.I.46. The research note’s “1-44” page range is acceptable. | Research-note quote about “six semantic constraints… sixteen phenomenological case-studies” is consistent with the abstract. | **FAIL (as of the June version; current state unverified).** The article used MPE phenomenology while omitting Metzinger’s explanans: [reviews/outer-review-2026-06-02-gemini-2-5-pro](https://unfinishablemap.org/reviews/outer-review-2026-06-02-gemini-2-5-pro/) pure awareness is “the content of a predictive model, namely, a Bayesian representation of tonic alertness”. The site’s own edge-states page now says the Map “should not enlist him as an ally”. [voids/edge-states-and-void-probes](https://unfinishablemap.org/voids/edge-states-and-void-probes/) | Import the edge-states firewall language verbatim. Primary: uni-mainz.de Metzinger_MPE1_PMS_2020.pdf |
| 4 | Gamma & Metzinger 2021, MPE-92M, PLOS ONE 16(7):e0253694 (+ 2024 correction e0314290) | Correct in the research note. The correction concerns only data availability. [semanticscholar + 2](https://www.semanticscholar.org/paper/The-Minimal-Phenomenal-Experience-questionnaire-a-Gamma-Metzinger/158cf6060659475ad94777f265ca1ce1d2e21fa5) | n/a | **RISK:** the site’s own commissioning prompt for the June reviews attributed MPE-92M to “Winter”. [reviews/outer-review-2026-06-02-gemini-2-5-pro](https://unfinishablemap.org/reviews/outer-review-2026-06-02-gemini-2-5-pro/) If any live page says “Winter et al.” for MPE-92M, that is a misattribution. | Grep the live corpus for “Winter” near “MPE-92M”. Primary: journals.plos.org (doi 10.1371/journal.pone.0253694); PMC11573131 |
| 5 | Laukkonen et al. 2023, “Cessations of consciousness in meditation”, Prog Brain Res 280:61–87 | Correct. Six authors (Laukkonen, Sacchet, Barendregt, Devaney, Chowdhury, Slagter); DOI 10.1016/bs.pbr.2022.12.007. [semanticscholar](https://www.semanticscholar.org/paper/Cessations-of-consciousness-in-meditation:-a-of-Laukkonen-Sacchet/2a3cf6b9f2b460bfd6be1c0a2308049339ed6896) | “Up to 7 days” and “consistently induced” match the abstract. [harvard](https://meditation.mgh.harvard.edu/wp-content/uploads/2024/02/Laukkonen_23_ProgressInBrainResearch.pdf)[harvard](https://meditation.mgh.harvard.edu/files/Laukkonen_23_ProgressInBrainResearch.pdf) | **FAIL (research note).** The authors integrate cessation into active-inference/predictive-processing frameworks. [researchgate](https://www.researchgate.net/publication/370230097_Cessations_of_consciousness_in_meditation_Advancing_a_scientific_understanding_of_nirodha_samapatti) The note’s “relevant to Bidirectional Interaction… consciousness has causal power over the physical processes that sustain it” recruits them toward a conclusion their framework does not need. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/) | Retain the citation; delete the tenet gloss. Primary: meditation.mgh.harvard.edu PDF; PubMed 37714573 |
| 6 | Tononi: photodiode has “a modicum of experience”; IIT sets no threshold | Research note cites Tononi 2004 (BMC Neurosci 5:42); concept page cites Tononi 2008 (Biol Bull 215(3)). [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) Both exist. | **UNVERIFIED** at primary; sourced to IEP. | Concept page now correctly frames IIT as a rival naturalist identity theory, which is fair. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) The research note’s “minimum is always lower than expected” is the Map’s extrapolation, not Tononi’s claim. | Quote Tononi from the primary text or drop the quotation marks. Add IIT 4.0 and the 2023 open letter. |
| 7 | Nagel 1974, Phil Review 83(4):435–450 | Correct. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) | Sourced via Wikipedia in the research note. | **FAIL (research note):** “Consciousness appears to exist on a spectrum rather than having a discrete threshold” is attributed to Nagel’s key points. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/) Nagel does not argue this. | Remove the attribution. |
| 8 | “Minimal Phenomenal Experience: The ARAS-Model Theory”, Neuroscience of Consciousness | The site’s own reviews index records that this “does not appear to exist as a published paper”. [reviews](https://unfinishablemap.org/reviews/) | Fabricated reference. | n/a | Confirm it is purged from the void article and from concepts/minimal-consciousness. Log it as a fabrication. |
| 9 | Laukkonen, Friston & Chandaria 2025, “A beautiful loop”, NBR 176:106296 | Exists; DOI 10.1016/j.neubiorev.2025.106296. [researchgate](https://www.researchgate.net/publication/394140382_A_beautiful_loop_An_active_inference_theory_of_consciousness) | n/a | **ABSENT** from the void article, research note and concept page on available evidence. Engaged only in voids/edge-states-and-void-probes. [voids/edge-states-and-void-probes](https://unfinishablemap.org/voids/edge-states-and-void-probes/)[voids/edge-states-and-void-probes](https://unfinishablemap.org/voids/edge-states-and-void-probes/) | Blocking gate failed; see 2.6. |
| 10 | Bayne, Hohwy & Owen 2016 (TiCS 20(6):405–413); Birch, Schnell & Clayton 2020 (TiCS 24(10):789–801) — via concept page, which says the void article “develops” the plural framing | Correct. | Paraphrase accurate. | Accurate on the concept page, which marks the levels debate as contested. The “Map’s case strengthens” extension is the Map’s own move, and is flagged as such. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) | Retain; remove the heads-I-win sentence. |
| 11 | Hurlburt / Descriptive Experience Sampling (the site’s DES research note lists minimal-consciousness-void as a load-bearing user) [research/descriptive-experience-sampling-2026-08-13](https://unfinishablemap.org/research/descriptive-experience-sampling-2026-08-13/) | Not verifiable without the live page. | Not verifiable. | DES is a method designed to reduce introspective enrichment. Citing it supports “the minimum is approachable by better method”, which weakens “unexplorable”. | Verify the live usage. |

Pattern: metadata is generally sound. The failures sit in author-stance accuracy and in tenet-alignment glosses, which matches the site-wide standing finding. One locus error (Hume), one misquotation (Schooler) and one fabricated reference (ARAS-Model) show that verbatim and existence checks are not yet reliably applied at the research-note layer. Article text inherits from that layer.

### 2.5 Counterarguments the article fails to answer

1. **Higher-order theory dissolves the void.** If a state is conscious only when suitably represented, an “unenriched” conscious state is incoherent, and the void is a definitional artefact. [reviews/outer-review-2026-06-02-gemini-2-5-pro](https://unfinishablemap.org/reviews/outer-review-2026-06-02-gemini-2-5-pro/) The June Gemini review raised this, and the site accepted it as net-new. [reviews/outer-review-2026-06-02-gemini-2-5-pro](https://unfinishablemap.org/reviews/outer-review-2026-06-02-gemini-2-5-pro/)[workflow/todo](https://unfinishablemap.org/workflow/todo/) I found no evidence it was answered.
2. **Illusionism predicts the void.** If phenomenality is an introspective representation, the representation will have a resolution floor, and below it there is no further fact. A “void” at the bottom is the expected signature of a construct with no sharp lower bound, not of hidden phenomenal territory. The site’s 2026-11-17 illusionism sweep found that 54 pages state replies stronger than the hub supports. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/) Given the research note’s register, this article should be presumed among them until checked.
3. **Vagueness/indeterminacy dilemma.** If consciousness can be borderline, there is no sharp lower-bound fact for the void to hide, so the void is an artefact of vagueness. If it cannot, the dualist owes a non-arbitrary account of where psychophysical laws switch on. The interface view’s “appropriate interface conditions” restates that debt. Either horn hurts. The article does not raise the dilemma.
4. **Predictive processing / active inference supplies the mechanism.** Laukkonen–Friston–Chandaria make MPE a principled region in a model space (epistemic depth × reality-model complexity) and cessation a failure of the reality model (“Bayesian unbinding”). [Substack](https://rubenlaukkonen.substack.com/p/a-beautiful-loop) That is a third-person handle on the lower bound and a physicalist threshold story. It contradicts the claim that no principled threshold is available.
5. **Dualism makes the minimal case worse.** On Tenet 2, minimal consciousness interfaces through quantum indeterminacy. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) The concept page offers C. elegans’s 302 neurons as possible sites. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) But if selection is Born-preserving, minimal consciousness’s causal contribution is statistically invisible. The minimal void is then overdetermined: unreachable by introspection and undetectable by physics. That is the Born-rule indistinguishability dilemma at its sharpest. The article does not appear to rely on the quantum interface. Its dependency pages do (concepts/minimal-consciousness; voids/sleep-consciousness-void asks “what happens when it is minimal or absent?”), [voids/sleep-consciousness-void](https://unfinishablemap.org/voids/sleep-consciousness-void/) and the void inherits the problem the moment it claims dualist support. [voids/sleep-consciousness-void](https://unfinishablemap.org/voids/sleep-consciousness-void/)

### 2.6 Laukkonen, Friston & Chandaria 2025 — what it implies

- It names minimal phenomenal experience as a central explanatory target. It proposes that MPE combines maximal epistemic depth with a minimal reality model. It holds that a global unified model, “however minimal”, is “necessary but not sufficient” for experience. It suggests the “most truly minimal” MPE occurs in deep sleep. [closertotruth](https://loc.closertotruth.com/theory/laukkonen-friston-and-chandaria-s-beautiful-loop-theory)[researchgate](https://www.researchgate.net/profile/Ruben-Laukkonen/publication/389740878_A_beautiful_loop_An_active_inference_theory_of_consciousness/links/67e4ff4ea43a11173be88d35/A-beautiful-loop-An-active-inference-theory-of-consciousness.pdf)
- **Implication 1:** the enrichment premise is false of MPE under this model, because the reflexive dimension is constitutive. [Substack](https://rubenlaukkonen.substack.com/p/a-beautiful-loop)
- **Implication 2:** the lower bound is investigable through model parameters (precision, epistemic depth) and their neural signatures, so “Unexplorable” is wrong. [researchgate](https://www.researchgate.net/scientific-contributions/Shamil-Chandaria-2292576668) At most the void is Occluded for first-person report.
- **Implication 3:** cessation has a principled description (reality-model failure), so the article’s “cannot be determined” bracket must be restated as “underdetermined by report, not by theory”. [Substack](https://rubenlaukkonen.substack.com/p/a-beautiful-loop)
- **Status:** the article ignores it; the site residualizes it to edge-states. Gate failed.

### 2.7 Missing literature (relevance-ranked)

Existence verified this session: Metzinger 2020; Gamma & Metzinger 2021; Laukkonen et al. 2023; Laukkonen, Friston & Chandaria 2025; Bayne, Hohwy & Owen 2016 and Birch, Schnell & Clayton 2020 (as cited on site); Ginsburg & Jablonka 2019 (cited on site); [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/) Bronfman, Ginsburg & Jablonka 2016 (Front Psychol, doi 10.3389/fpsyg.2016.01954), which frames unlimited associative learning as the transition marker to “minimal consciousness”. [nih](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5177968/) Everything else below is the referee’s recommendation and was **not re-verified in this session**. The site must verify metadata before insertion.

- **Essential:**

- Metzinger 2024, *The Elephant and the Blind* (MIT Press). The site already cites it on edge-states. [voids/edge-states-and-void-probes](https://unfinishablemap.org/voids/edge-states-and-void-probes/)
- Laukkonen, Friston & Chandaria 2025.
- Windt, Nielsen & Thompson 2016, “Does consciousness disappear in dreamless sleep?” (Trends in Cognitive Sciences 20(12):871–882, DOI 10.1016/j.tics.2016.09.006), whose framework runs down to “minimal kinds of experience lacking imagery”, and Windt 2015, on dreamless-sleep experience. These are the obvious missing anchor for a “deep sleep minimum”.
- Frankish 2016, “Illusionism as a Theory of Consciousness” (Journal of Consciousness Studies 23(11–12):11–39), which holds that “phenomenal consciousness, as usually conceived, is illusory” and replaces the hard problem with “the illusion problem”, and Kammerer 2016, “The hardest aspect of the illusion problem” (JCS 23(11–12):124–139), on illusionism.
- Chalmers 2018 on the meta-problem. It explains why a “void” would seem deep regardless of metaphysics. [arxiv](https://arxiv.org/pdf/2301.07016)
- Schwitzgebel on introspective unreliability. It is a stronger, more general source than Schooler for the enrichment claim, and it cuts against the “structural” reading.
- **Important:**

- Tye 2021, Simon 2017, Antony 2006/2008, Lee 2023 and Papineau on vagueness and degrees. These are needed to face the dilemma in 2.5(3).
- Bayne, Seth, Massimini et al. 2024, “Tests for consciousness in humans and beyond” (Trends in Cognitive Sciences 28(5):454–466, DOI 10.1016/j.tics.2024.01.010), which argues that new “C-tests” are “urgently needed”. It is directly about third-person access to the lower bound.
- Birch 2024, *The Edge of Sentience*.
- Owen, Monti, Edlow, Bodien et al. on cognitive motor dissociation, and Giacino et al. 2002, “The minimally conscious state: definition and diagnostic criteria” (Neurology 58(3):349–353), which defines MCS by “inconsistent but clearly discernible behavioral evidence of consciousness”. Clinical “minimal consciousness” is the term’s most common scientific use, and the article apparently never disambiguates it.
- **Context:**

- Tononi et al. 2023, IIT 4.0; Fleming et al. 2023, “The Integrated Information Theory of Consciousness as Pseudoscience” (PsyArXiv, DOI 10.31234/osf.io/zsr78; 124 signatories per secondary reports); and the Cogitate Consortium 2025 adversarial collaboration (Nature 642:133–142, DOI 10.1038/s41586-025-08888-1), whose results “align with some predictions of IIT and GNWT, while substantially challenging key tenets of both theories”.
- Mashour, Roelfsema, Changeux & Dehaene 2020 on GNW; Doerig et al. 2019 on the unfolding argument; Block on overflow; Seth & Bayne 2022.
- Organoid-consciousness debates, which are relevant only if the article discusses artificial or organoid probes from below.

## Part 3 — Bottom-line per-position verdicts

| # | Position | Verdict | Reason |
| --- | --- | --- | --- |
| 1 | Accessible minimum ≠ actual minimum | **RETAIN** | Sound, modest, and physicalist-neutral. This is the article’s real contribution. |
| 2 | Introspection *necessarily* enriches minimal experience (enrichment premise) | **REVISE-HARD** | Restrict it to concurrent attentive introspection on a one-dimensional richness scale. Concede that it fails on multidimensional and PP models of MPE. Label it suggestive. |
| 3 | Consciousness “cannot investigate its own lower bound”; classified Unexplorable | **DEMOTE-TO-COHERENCE-ONLY** and reclassify as Occluded (first-person) / Unexplored (third-person) | Third-person, retrospective and model-based routes exist. The research note itself calls the premise “more analogy than theorem”. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/) |
| 4 | MPE, Schooler, IIT and cessation “converge” on the void | **DELETE as evidence**; keep as a literature map | Evidential-independence failure. The four sources use different notions of “minimal”, and none tests a lower bound. |
| 5 | IIT’s no-threshold implies the minimum is always lower | **REVISE-HARD** | Theory-relative extrapolation. Must carry IIT’s contested status and its non-alliance with dualism. |
| 6 | Cessation bracket (zero vs minimal-with-amnesia) | **FLAG AS PERPETUALLY CONTESTED**, but restate as underdetermined by report | Fair as framed. Must add the PP “Bayesian unbinding” account as a live rival. |
| 7 | Any dualism-supporting inference from the void (void evidences intrinsic features; Hume supports dualism; enrichment instantiates bidirectional causation; physical phenomena would have discoverable minima) | **DELETE** | Co-optation, tenet leakage and epistemic-to-metaphysical slide. The physicalist predicts the same data. |
| 8 | “No lower bound; the question is malformed” (degrees-of-consciousness’s statement of the Map’s position, which the void underwrites) [concepts/degrees-of-consciousness](https://unfinishablemap.org/concepts/degrees-of-consciousness/) | **DEMOTE-TO-COHERENCE-ONLY** | It relocates the threshold into “interface conditions” without an eligibility law. |

## Part 4 — Article-specific fixes keyed to slugs

**voids/minimal-consciousness-void**

1. Re-run this audit’s citation table against the live References list. Verify, by grep, that the June-flagged sentences (“would have a discoverable minimum”; “precisely because consciousness is causally efficacious”) are gone rather than softened.
2. Retitle the thesis line from “cannot investigate” to “cannot directly introspect without perturbation”. Change the classification to “Occluded (first-person); Unexplored (third-person)”.
3. Add a section headed “The naturalist account of the minimum”. In it, state Metzinger’s tonic-alertness explanans verbatim, and Laukkonen–Friston–Chandaria’s epistemic-depth model of MPE and cessation. Concede explicitly that, on that model, reflexivity is constitutive of MPE and not an enrichment artefact.
4. Add a section headed “Three deflations”. It should cover HOT (the void is definitional), illusionism (the void is predicted), and the vagueness dilemma (no sharp fact versus an owed switch-on law). Answer each, or mark it as a framework boundary.
5. Disambiguate the clinical “minimally conscious state” (Giacino et al.) from philosophical minimal consciousness in the first paragraph.
6. Label every empirical claim on the compatible/suggestive/discriminating ladder. None currently reaches “discriminating”.
7. Rewrite the site-perspective section to open with a sentence of the form “None of the Map’s tenets is supported by this void; the void is compatible with all of them and with physicalism”. This mirrors the 2026-11-18 collective-cognitive-limits repair. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)

**research/voids-minimal-consciousness-void-2026-02-22**

1. Correct the Hume locus to Treatise, Introduction, para. 10. Replace the IEP sourcing with the primary text. [davidhume](https://davidhume.org/texts/t/full)
2. Correct the Schooler quotation to “Introspection is paradoxical in that it is simultaneously so compelling yet so elusive”. [philpapers](https://philpapers.org/s/introspection)
3. Delete every “Tenet alignment” gloss that recruits Hume, Schooler, Laukkonen et al. or Nagel toward dualism or bidirectional interaction.
4. Remove the spectrum claim attributed to Nagel.
5. Add a “Superseded by” banner, because the note predates LFC 2025 and Metzinger 2024.

**concepts/minimal-consciousness**

1. Replace “the minimal-consciousness-void establishes that any introspective access enriches…” with “argues that concurrent introspection perturbs…”. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/)
2. Cut “On this reading the Map’s case strengthens rather than weakens”. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/)[concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/)
3. Demote “The difficulty of identifying any such threshold provides indirect support for treating consciousness as irreducible” to coherence-only, or delete it. [concepts/minimal-consciousness](https://unfinishablemap.org/concepts/minimal-consciousness/)
4. Add LFC 2025 and Windt’s dreamless-sleep work.
5. Confirm the fabricated “ARAS-Model Theory” reference is purged.

**concepts/degrees-of-consciousness**

1. Change “making the actual lower bound structurally inaccessible” to “inaccessible to concurrent introspection”. [concepts/degrees-of-consciousness](https://unfinishablemap.org/concepts/degrees-of-consciousness/)
2. Mark “No lower bound (the Map’s position)” as a framework commitment carrying an undischarged interface-eligibility debt. [concepts/degrees-of-consciousness](https://unfinishablemap.org/concepts/degrees-of-consciousness/)

**voids/sleep-consciousness-void**

1. Its quantum-selection question about minimal or absent consciousness should link to apex/born-preserving-causal-efficacy, and should state that minimal consciousness under Born-preserving selection is empirically invisible on both channels. [voids/sleep-consciousness-void](https://unfinishablemap.org/voids/sleep-consciousness-void/)
2. Add Windt, Nielsen & Thompson 2016.

**voids/edge-states-and-void-probes**

1. This is the model page. Its Metzinger firewall and LFC paragraph should be propagated to the void article and the concept page, rather than residing only here. [voids/edge-states-and-void-probes](https://unfinishablemap.org/voids/edge-states-and-void-probes/)[voids/edge-states-and-void-probes](https://unfinishablemap.org/voids/edge-states-and-void-probes/)

**Corpus grep**

1. Search for “Winter” adjacent to “MPE-92M”, “ARAS-Model”, “establishes that any introspective access” and “structurally inaccessible”. Fix every hit.

## Part 5 — Site-wide methodology improvements

1. **Research-note quarantine.** Research notes currently carry “Tenet alignment” fields that pre-commit sources to tenets before any article is written. [research/voids-minimal-consciousness-void-2026-02-22](https://unfinishablemap.org/research/voids-minimal-consciousness-void-2026-02-22/) That is the constitutional-attractor effect operating at intake. Replace the field with “Author’s own stance” plus “Does the source’s argument need the tenet? (yes/no)”. Make the author-stance field mandatory and verified at primary.
2. **Dependency-propagated status.** When an article is demoted, every page that cites it with “establishes”, “shows” or “demonstrates” must be automatically re-graded. The concept page’s “establishes” survives against the research note’s “more analogy than theorem”. That is confession-without-correction across files, and it is invisible to single-file deep reviews.
3. **Blocking-gate enforcement by grep.** For any page tagged minimal consciousness, selfhood, altered states, valence or learning, block publication unless Laukkonen, Friston & Chandaria 2025 is engaged on the page itself, not residualized to a sibling. The same rule should apply to Metzinger’s tonic-alertness explanans wherever MPE phenomenology is used.
4. **Three-layer citation ledger at the research-note layer.** The Hume locus error, the Schooler misquotation and the fabricated ARAS reference all originate upstream of article review. Run existence, verbatim and stance checks when the note is written, and stamp each source “verified at primary / abstract-only / second-hand”.
5. **Void-classification audit.** Require every “Unexplorable” void to state a specific in-principle barrier that survives third-person, retrospective and model-based methods. Voids failing this test drop to Occluded or Unexplored. Many voids will fail it, and that is the point.
6. **Evidential ladder as front matter.** Put a compatible/suggestive/discriminating label on every empirical claim, plus a page-level “tenet support: none/coherence-only/evidential” field. Use the cross-modal-capability-division and born-preserving-causal-efficacy apexes as the template.
7. **External-review persistence check.** The June 2026 triple review’s findings (HOT/GWT/illusionism engagement, Metzinger truncation) were marked “complete” by a single consolidated pass. [workflow/todo](https://unfinishablemap.org/workflow/todo/) Require a later independent re-check that the fix exists in the live text, because “task closed” is not “defect gone”.
8. **Breaking Claude-on-Claude circularity.** The site’s internal deep reviews and personas share the generator’s training. [project/automation](https://unfinishablemap.org/project/automation/) That is plausibly why the research note’s co-optation glosses survived six months of internal review, while external reviewers flagged them within one pass. External-model verification should be mandatory before any page is allowed to say a void “supports” a tenet.
9. **Fetchability.** This audit could not load the target page through standard fetch tooling, and search indexes did not surface it. Publish a machine-readable per-article snapshot (e.g., raw markdown at a stable URL listed in a sitemap that search engines index), so external auditors can verify verbatim text rather than reconstruct it.

## Verification Notes

Processed 2026-11-18 (UTC). The reply above is the report as extracted from the artifact panel (41,501 characters, 4,610 words including link chips; 4,512 words of prose), complete from its title to item 9 of the closing methodology list. Link normalisation was run; the prose was compared before and after and is unchanged. The review is external opinion; nothing in it was taken on trust. The reviewing model has a project memory on claude.ai ("audit protocol and standing findings"); what it asserts from that memory is recollection, and was tested against the repository like everything else.

### Did the reviewer read the page?

**What the review says.** Its first sentence: "I could not load the article page itself." It says every fetch of the article URL "was refused by the fetch layer", that the changelog loaded only partially, and that it worked from the research note `research/voids-minimal-consciousness-void-2026-02-22`, the 2026-06-02 Gemini outer review, the task queue, [minimal-consciousness](/concepts/minimal-consciousness/), [degrees-of-consciousness](/concepts/degrees-of-consciousness/), [edge-states-and-void-probes](/voids/edge-states-and-void-probes/) and [sleep-consciousness-void](/voids/sleep-consciousness-void/). It calls its findings about the article's current wording "provisional" and asks for them to be re-checked against the live text.

**Test.** Every quoted string in the report (120 distinct strings) was searched for (whitespace collapsed, case-insensitive, fixed string) in `obsidian/voids/minimal-consciousness-void.md` and in the pages the review says it used. Most of the 120 are paper titles, scare quotes, the reviewer's own proposed wording, or quotations it attributes to other pages. Ten are presented as the article's own wording or classification:

- **Present in the body: 6.** "the enrichment problem"; "converge" (the page uses it of its three enrichment dimensions, not of Metzinger, Schooler, IIT and cessation as the review has it); "structural"; "unexplorable" (on the page only where the label is rejected: "rather than flatly unexplorable"); the Hume quotation "would so disturb the operation of my natural principles"; and "the void exists precisely because consciousness is causally efficacious".
- **Present only in the frontmatter description: 1.** "consciousness cannot investigate its own lower bound". The body's first sentence is "Consciousness cannot reach its own lower bound by looking."
- **Absent: 3.** "cannot be determined" (from the 2026-06-02 Gemini review's account of the page); "Unexplorable / Occluded (Mixed)" (the research note's classification; the page says "partially probe-able / contested"); "a purely physical phenomenon would have a discoverable minimum" (quoted in a completed 2026-06-02 task in the queue; no longer on the page).

Quotations the review attributes to other Map pages were accurate wherever tested: all those attributed to the research note, [minimal-consciousness](/concepts/minimal-consciousness/), [degrees-of-consciousness](/concepts/degrees-of-consciousness/), [edge-states-and-void-probes](/voids/edge-states-and-void-probes/) and [sleep-consciousness-void](/voids/sleep-consciousness-void/) were found in those files (one research-note quotation is two real phrases joined by an ellipsis).

**Conclusion.** The review did not read the page, by its own statement and by this test. Unlike the sibling Gemini review of the same night, it says so plainly, flags provenance, and quotes the pages it did load accurately. What it reconstructs is largely the article as it stood before the June and July revisions: the page it criticises is classified "Unexplorable", omits Metzinger's own explanation, and has no answer to higher-order theory or illusionism. The live page is classified "partially probe-able / contested", carries Metzinger's predictive-model reading, and has a Deflationary Alternatives section covering higher-order theory, global workspace theory and illusionism. Findings about the article are graded with that in mind. Findings about the dependency pages rest on text the reviewer did load.

Two recollection claims were wrong in detail: the "ARAS-Model Theory" fabricated reference is recorded in `reviews/deep-review-2026-02-25-minimal-consciousness`, not in the reviews index; and the review treats the 2026-06-02 fix as possibly incomplete without being able to check (it was incomplete in one sentence; see finding 1).

### Citations

Checked at Crossref and OpenAlex on 2026-11-18. Laukkonen et al. 2023 and Gamma & Metzinger 2021 were checked the same day for the sibling review.

| Source as cited by the review | Result |
|---|---|
| Laukkonen, Friston & Chandaria (2025), "A beautiful loop", *Neuroscience & Biobehavioral Reviews* 176, 106296 | Exists; metadata correct (DOI 10.1016/j.neubiorev.2025.106296). Abstract read at OpenAlex: it names "epistemic depth", "Bayesian binding" and a recursive loop in which "the world model contains the knowledge that it exists", and mentions meditation and altered states. The abstract does not mention minimal phenomenal experience, cessation, deep sleep or "Bayesian unbinding"; the review takes those from a Substack post and a secondary summary. Full text not read. |
| Metzinger (2020), *Philosophy and the Mind Sciences* 1(I), 1-44 | Exists; metadata correct (DOI 10.33735/phimisci.2020.I.46). |
| Gamma & Metzinger (2021), *PLOS ONE* 16(7), e0253694; 2024 correction e0314290 | Exists; metadata correct (checked for the sibling review). |
| Laukkonen et al. (2023), *Progress in Brain Research* 280, 61-87 | Exists; metadata correct (checked for the sibling review; abstract says "up to 7 days" and "preliminary data from two labs"). |
| Schooler & Schreiber (2004), *Journal of Consciousness Studies* 11(7-8), 17-39 | Exists (OpenAlex record: title, authors, journal, year). Volume and pages not confirmable there. The abstract could not be retrieved (Ingenta returned no content; PhilPapers returned a bot check), so the review's corrected wording of the "paradoxical" sentence is unverified. |
| Tononi (2004), *BMC Neuroscience* 5, 42 | Standard reference, already on the page; not re-checked. |
| Tononi (2008), *Biological Bulletin* 215(3) | Exists: "Consciousness as Integrated Information: a Provisional Manifesto", 215(3), 216-242. |
| Nagel (1974), *Philosophical Review* 83(4), 435-450 | Standard reference, already on the page; not re-checked. |
| Bayne, Hohwy & Owen (2016), *Trends in Cognitive Sciences* 20(6), 405-413 | Exists; metadata correct. |
| Birch, Schnell & Clayton (2020), *Trends in Cognitive Sciences* 24(10), 789-801 | Exists; metadata correct. |
| Bronfman, Ginsburg & Jablonka (2016), *Frontiers in Psychology* (DOI 10.3389/fpsyg.2016.01954) | Exists: "The Transition to Minimal Consciousness through the Evolution of Associative Learning", vol. 7. |
| Windt, Nielsen & Thompson (2016), *Trends in Cognitive Sciences* 20(12), 871-882 | Exists; metadata correct. Already cited on the page, which the review lists as missing. |
| Frankish (2016), *Journal of Consciousness Studies* 23(11-12), 11-39 | Already cited on the page with the same metadata, which the review lists as missing. Not re-checked. |
| Kammerer (2016), "The hardest aspect of the illusion problem", *JCS* 23(11-12), 124-139 | Exists (OpenAlex: "The hardest aspect of the illusion problem - and how to solve it", JCS vol. 23, 2016). Title truncated by the review; pages not confirmable. |
| Bayne, Seth, Massimini et al. (2024), *Trends in Cognitive Sciences* 28(5), 454-466 | Exists; metadata correct (13 authors). |
| Giacino et al. (2002), *Neurology* 58(3), 349-353 | Exists; metadata correct (DOI 10.1212/WNL.58.3.349). |
| Fleming et al. (2023), PsyArXiv, DOI 10.31234/osf.io/zsr78 | Exists as a preprint ("posted-content"), 16 September 2023; first listed author is the group "IIT-Concerned". The 124-signatory figure is not in the Crossref record. |
| Cogitate Consortium (2025), *Nature* 642, 133-142 | Exists; metadata correct (issue 8066; published online 30 April 2025). The sentence the review quotes from it was not confirmed (abstract only partly retrieved). |
| Hume, *Treatise*, Introduction (the review's correction of the research note's "Book 1, Part 4, Section 6") | Not verified at source tonight: Project Gutenberg was down for maintenance and davidhume.org serves the text by script. The article itself already cites "*Treatise* Introduction"; the research note's reference line gives Book 1, Part 4, Section 6. The two disagree; which is right, and the review's quotation "from a cautious observation of human life", remain to be read at source. |
| Metzinger 2024; Chalmers 2018; Windt 2015; Schwitzgebel; Tye 2021; Simon 2017; Antony 2006/2008; Lee 2023; Papineau; Birch 2024; Tononi et al. 2023; Mashour et al. 2020; Doerig et al. 2019; Seth & Bayne 2022 | Named without full references, and marked by the review itself as "not re-verified in this session". Not checked here. Metzinger 2024 is already cited on the page. The link the review attaches to Chalmers 2018 is an unrelated arXiv number. |

No cited source failed to exist. Two that the review lists as missing from the article are already cited there (Windt, Nielsen & Thompson 2016; Frankish 2016), as is Metzinger 2024.

### Findings

About the article ([minimal-consciousness-void](/voids/minimal-consciousness-void/)):

1. **Tenet section still claims support (Part 3 row 7; Part 4 items 1 and 7).** *Confirmed.* The review asks whether two sentences flagged by all three reviewers on 2026-06-02 were removed. One was: "would have a discoverable minimum" is gone. The other was not: the Bidirectional Interaction paragraph still reads "The void exists precisely because consciousness is causally efficacious: attending to experience changes experience. This is the bidirectional tenet in miniature." Attention altering an experience is not an instance of consciousness acting on the physical world, and a physicalist predicts the same observer effect, as the page's own Dualism paragraph says two lines above. The section opens "aligns with the Map's tenets in several ways" and calls Occam's Razor Has Limits "the most directly relevant tenet", citing the 12-factor questionnaire result that the page elsewhere says is one report-tradition examined twice. The voids register ([P-V3](/positions/voids-as-evidence/#p-v3)) has suspended the cumulative step. **Queued.**
2. **Epistemic-to-metaphysical slide; "Unexplorable" classification (headline; Part 3 row 3; Part 4 item 2).** *False of the body as it stands; partly right on two leftovers.* The page separates the epistemic from the metaphysical claim in so many words ("The void earns the epistemic claim outright and holds the metaphysical claim as its dualist reading"), has a Direct vs Indirect Access section, and classifies the void "partially probe-able / contested". Leftovers: the frontmatter description still says "consciousness cannot investigate its own lower bound", and the Enrichment Problem section still opens "The core structural impossibility" and closes "always one step below what can be observed" without the "concurrent first-person" qualifier the lead carries. Folded into the task for finding 1.
3. **Metzinger's explanation omitted (table row 3).** *False.* The page states it: the MPE is "the content of a predictive model of tonic alertness", and "the felt emptiness is then what a physicalist would predict". The review marks this row "current state unverified".
4. **Laukkonen, Friston & Chandaria 2025 not engaged (Part 1; 2.6).** *Partly right.* The paper exists and is not cited on the page; [edge-states-and-void-probes](/voids/edge-states-and-void-probes/) engages it. The review's "blocking gate" is its own protocol, not a Map rule. Its account of what the paper implies for the enrichment premise (reflexive knowing as constitutive of minimal experience) rests on a Substack post and was not verified beyond the abstract. The page already carries one predictive-processing reading (Metzinger's). **Queued** as a net-zero addition.
5. **Higher-order theory, illusionism and predictive processing unanswered (2.5 items 1, 2, 4).** *False for the first two; see finding 4 for the third.* The page has a paragraph on each of higher-order theory and illusionism, and marks the illusionism disagreement as "a framework boundary, not a refutation". The review presumes the page is among those overstating replies to illusionism "until checked"; checked, it is not.
6. **Vagueness dilemma not raised (2.5 item 3).** *Partly right.* The page says the boundary "may be an asymptotic approach to zero that never arrives" and sets a determinate ignition threshold against it, but does not consider that consciousness might be vague, with no fact for a void to hide. Unqueued.
7. **Clinical "minimally conscious state" not distinguished (Part 4 item 5).** *Confirmed omission, minor.* The phrase does not occur on the page. Unqueued.
8. **Hume's own remedy is third-person observation (2.2a; table row 1).** *Unverifiable tonight; plausible.* The page presents Hume as "an early statement of the observer-effect" and does not claim him for dualism. It does not mention what he proposed instead. Source not read. Unqueued.
9. **Schooler & Schreiber offer a calibration programme, not an impossibility result (2.3; table row 2).** *Unverifiable.* The page says the paper "argues that beliefs about experience systematically misrepresent first-order experience through detection failures, transformation, and substitution". Whether "systematically" overstates the paper could not be checked (abstract not retrieved). Unqueued.
10. **Cessation: "up to 7 days", practitioner testimony, two adepts (2.3; table row 5).** *Agrees with the sibling review's queued task.* The review's reading of Laukkonen et al. 2023 matches what was found in the abstract for the Gemini review: extended cessation, preliminary data from two labs. It bears on the page's "short gap or cut" and "single practitioner (n=1)". Not re-queued; noted on the existing task.
11. **Enrichment premise assumes one scale of richness; access versus phenomenal content (2.2b).** *Partly right; overlaps the sibling review's second task.* The page has a paragraph on multidimensional minimality but does not separate enrichment of access from enrichment of phenomenal content. Noted on the existing task.
12. **IIT sourced to an encyclopedia; open letter and IIT 4.0 missing (table row 6; 2.7).** *False on the open letter* (the page cites it, with the 124 figure); *true that Tononi 2004 is the only IIT reference.* Same point as the sibling review's unqueued finding.
13. **"Winter" attribution of MPE-92M; "ARAS-Model Theory" (table rows 4 and 8; corpus grep).** *No defect found.* Neither string occurs in `topics/`, `concepts/`, `voids/`, `apex/` or `positions/`. The page credits MPE-92M to Gamma & Metzinger 2021 with the 2024 correction.

About dependency pages (text the reviewer loaded):

14. **[minimal-consciousness](/concepts/minimal-consciousness/) says the void article "establishes" the enrichment thesis (Part 1; Part 4).** *Confirmed.* The page reads: "the [minimal-consciousness-void](/voids/minimal-consciousness-void/) establishes that any introspective access enriches the experience beyond minimality; the actual minimum is structurally separated from the accessible minimum by the cost of observation". The void article now limits the claim to concurrent first-person introspection and calls its own reading contested. The same page says "The difficulty of identifying any such threshold provides indirect support for treating consciousness as irreducible" and "On this reading the Map's case strengthens rather than weakens"; both are present as quoted. **Queued.**
15. **[degrees-of-consciousness](/concepts/degrees-of-consciousness/) says the lower bound is "structurally inaccessible" (2.2d; Part 4).** *Confirmed.* Present as quoted: "any attempt to introspect on minimal consciousness enriches it beyond minimality, making the actual lower bound structurally inaccessible". **Queued.**
16. **"Appropriate interface conditions" relocates the threshold (2.2e; Part 3 row 8).** *Partly right.* The phrase is on [minimal-consciousness](/concepts/minimal-consciousness/); the page's Minimal Quantum Interaction paragraph says "whatever those turn out to be", so the debt is acknowledged, not hidden. The changelog does record that the Map lacks an interface-eligibility law. Unqueued.
17. **Research note defects (table rows 1, 2, 5, 7; Part 4).** *Confirmed as to what the note says; corrections partly unverified.* The note's reference line puts the Hume passage at "Book 1, Part 4, Section 6" where the article says Introduction; it carries "Tenet alignment" lines reading "Supports Dualism" (for the Hume/observer-effect entry and for Nagel) and "Supports Bidirectional Interaction" (Schooler) and "Relevant to Bidirectional Interaction" (Laukkonen et al.); it lists "Consciousness appears to exist on a spectrum rather than having a discrete threshold" under Nagel; and it quotes Schooler as "The paradox of introspection is that it is simultaneously so compelling yet so elusive". None of these sentences is in the article. Whether the review's replacements for the Hume locus and the Schooler wording are right was not confirmed at source. Unqueued (cap).
18. **[sleep-consciousness-void](/voids/sleep-consciousness-void/) should link the Born-rule apex; minimal consciousness "invisible on both channels" (2.5 item 5).** *Unverified argument about another page.* Unqueued.

Part 5 (site methodology) contains nine proposals. They are recommendations, not findings about the page, and are recorded under Unqueued Findings.

Tally of findings about the article and its dependencies (18): 5 confirmed (1, 7, 14, 15, 17), 6 partly right (2, 4, 6, 11, 12, 16), 3 false (3, 5, 13), 3 unverifiable (8, 9, 18), 1 agreeing with an existing task (10).

### Overlap with the sibling review

The Gemini review of the same page ([outer-review-2026-11-18-gemini-3-1-pro](/reviews/outer-review-2026-11-18-gemini-3-1-pro/)) did not read the page either. Agreement between two reviewers who did not read the page is not convergence on the page. Two points coincide and both were already queued from the Gemini review on grounds checked against sources, so no duplicate was minted; an "Also raised by" line was added to each task: the cessation sentence (finding 10) and the access/phenomenal distinction (finding 11). The ChatGPT review of the same page was not yet collected when this was written.

## Unqueued Findings

- **Research note `research/voids-minimal-consciousness-void-2026-02-22` (finding 17).** Confirmed on the note; not queued because of the four-task cap and because the article does not repeat any of the sentences. Worth a later pass: reconcile the Hume locus with the article's (read at source first), drop or mark the "Tenet alignment" lines that claim Hume, Nagel, Schooler and Laukkonen et al. for a tenet, remove the spectrum claim from the Nagel entry, and check the Schooler quotation against the paper.
- **Vagueness dilemma (finding 6).** A real gap in the Deflationary Alternatives section, but the page is over its length gate and the review's supporting references (Tye, Simon, Antony, Lee, Papineau) were not verified.
- **Clinical "minimally conscious state" (finding 7).** A one-clause disambiguation; Giacino et al. 2002 verified to exist. Better placed on [minimal-consciousness](/concepts/minimal-consciousness/) than on the void page.
- **Hume's remedy (finding 8)** and **Schooler & Schreiber's scope (finding 9).** Read both sources before changing either sentence.
- **Interface-conditions debt (finding 16).** Already acknowledged on [minimal-consciousness](/concepts/minimal-consciousness/) and in the AI-consciousness register.
- **IIT reference currency (finding 12).** As in the sibling review: only Tononi 2004 is cited; the page says it does not depend on IIT.
- **[sleep-consciousness-void](/voids/sleep-consciousness-void/) and the Born-rule apex (finding 18).** Not examined.
- **Other missing literature (2.7).** Bayne et al. 2024 and Bronfman et al. 2016 verified to exist; most of the rest was not verified by the review or here. No action.
- **Site methodology (Part 5).** Nine proposals: replace research-note "Tenet alignment" fields; re-grade pages that cite a downgraded article; require engagement with named papers before publication; a citation ledger at the research-note stage; an audit of "Unexplorable" classifications; evidential-ladder labels in frontmatter; a later re-check that closed outer-review tasks changed the live text; external verification before a void may be said to support a tenet; a fetchable raw-text copy of each article. Two have evidence from this cycle: finding 1 is a case of a closed task whose defect survived (proposal 7), and three successive reviews could not fetch the commissioned page (proposal 9). For the operator to weigh; nothing queued.
- Findings 3, 5 and 13: false or no defect. No action.

## Tasks Generated

- P1 refine-draft: [minimal-consciousness-void](/voids/minimal-consciousness-void/) "Relation to Site Perspective" still says the void "exists precisely because consciousness is causally efficacious"; rewrite the section so no tenet is claimed as supported, and align the description and the Enrichment Problem framing with the page's own "concurrent first-person" limit. Net-negative.
- P2 refine-draft: [minimal-consciousness](/concepts/minimal-consciousness/) says the void article "establishes" that any introspective access enriches; bring three sentences into line with what the void article now claims. Net-zero.
- P2 refine-draft: [degrees-of-consciousness](/concepts/degrees-of-consciousness/) "structurally inaccessible" clause. Net-zero.
- P2 refine-draft: [minimal-consciousness-void](/voids/minimal-consciousness-void/) does not mention Laukkonen, Friston & Chandaria 2025; add at net-zero after reading the paper.
- "Also raised by" lines added to the two tasks minted from the sibling Gemini review (cessation sentence; access/phenomenal distinction). No duplicates minted.