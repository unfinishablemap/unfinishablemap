---
ai_contribution: 100
ai_generated_date: 2026-11-15
ai_modified: 2026-11-15 03:25:46+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-15
date: &id001 2026-11-15
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-15 03:25:46+00:00
modified: *id001
related_articles: []
title: Deep Review - Content-Specificity of Mental Causation
topics: []
---

**Date**: 2026-11-15
**Article**: [Content-Specificity of Mental Causation](/concepts/content-specificity-of-mental-causation/)
**Previous review**: [2026-07-18](/reviews/deep-review-2026-07-18-content-specificity-of-mental-causation/) (ninth review overall)

## Context

Selected by the skill's scorer as the top eligible candidate after the cycle's skip list (pages touched since 2026-11-13, `topics/personal-identity`, and pages named in open todo headings or File/Secondary lines) removed the 18 higher-ranked entries. No open todo task names this page.

Changes since the 2026-07-18 review: the References block changed twice, so the §2.4 web-verify trigger fired this time. `5c2e104b0c` (2026-08-07) re-attributed the ~10 bits/s figure to Zheng & Meister 2025 and added that reference. `5986c301a5` (2026-08-19) merged two archived self-citations into one entry for `empirical-phenomena-mental-causation`. `c5ff07b480` (2026-10-21) added a `[[causal-relevance-of-content]]` wikilink. Length was 2131 words before this review and 2420 after. The concepts soft threshold is 2500, so the review ran in normal mode.

The 2026-07-18 stability note said all ten citations were "publisher-of-record verified clean". That covered metadata. The result-direction leg (§2.4 step 7) had not been run against the raw abstracts. When it was, four of the article's claims were found not to match their cited sources.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Pollo et al. 2001 misdescribed (factual error).** The article said: "Believing a pill is a *strong* painkiller produces greater analgesia than believing it is *mild*." The raw PubMed abstract (PMID 11406341) contradicts this. The three groups got a saline infusion and were told either nothing, that it was "either a powerful painkiller or a placebo", or that it was "a potent painkiller". No group was told the drug was mild. The outcome was buprenorphine requests (11.55 / 9.15 / 7.65 mg), and "analgesia was the same in the three groups." So the qualifier being manipulated was certainty, not drug strength, and the measured effect was opioid intake, not analgesia. The 2026-06-06 review had accepted the old sentence as "a fair characterisation". **Fixed**: the sentence now describes the actual design, the three doses and the equal pain levels, and the granularity sentence now names the distinction as certain versus uncertain expectation, producing a graded response.
2. **Pain asymbolia overclaim (calibration error).** The article said: "Pain asymbolia isolates the role of phenomenal quality … Strip away the specific phenomenal quality and the specific behavioural response disappears." The page it sends readers to, `topics/pain-consciousness-and-causal-power`, says the opposite. It "declines any pristine one-variable reading". It says "Losing the affective signal degrades avoidance whether or not felt awfulness does causal work of its own". It calls the pattern "compatible with phenomenal causation rather than evidence for it." A reviewer who accepts the tenets would still flag "isolates". **Fixed**: the paragraph now says the case dissociates felt badness from detection and does not isolate phenomenal quality as a single variable, because aversive processing is lost along with it. It then states what the case does show. Added a `[[pain-asymbolia]]` link.
3. **Relation to Site Perspective opened with "provides empirical grounding for" the Bidirectional Interaction tenet.** The same paragraph concedes that the data are "the access-level result a non-reductive physicalist grants as readily as a dualist". The sibling's evidential-status rule calls such data compatible with the tenet, not support for it. This was an internal tension. **Fixed**: the paragraph now opens "bears on … as a pattern compatible with it, not as evidence favouring it over physicalist rivals". The rest of the paragraph is unchanged.

### Medium Issues Found

- **Beilock & Carr 2001 over-attributed.** "Outcome-focused attention preserves it" does not appear in the raw abstract (PMID 11757876). The study's finding is that self-consciousness training eliminated choking while dual-task training left it unchanged. The uncited follow-on, "certain forms of distraction actually *improve* expert performance", is the Beilock, Carr, MacMahon & Starkes 2002 result (PMID 12009178, verified). **Fixed**: B&C 2001 is now stated as the abstract gives it, and the distraction result is cited to Beilock et al. 2002 with its dominant-foot qualifier. That reference was added. The sibling `empirical-phenomena-mental-causation` L119 already splits the attribution this way.
- **Gröpel & Mesagno 2019 overstated.** The article said the review "confirms the distraction/self-focus split as the field's two governing models and reports that distraction routines and acclimatisation reliably counteract the effect". In the OpenAlex abstract the review sorts its 47 studies into distraction-based and self-focus-based interventions plus a third acclimatisation group, and finds that "in general" all three benefit performance. "Distraction routines" is not the review's term, and "reliably" and "confirms" are stronger than its wording. **Fixed** to match the abstract.
- **Colloca & Miller 2011 examples not in the source.** "Patients warned about nausea experience nausea from inert pills; those warned about headaches experience headaches." The PMC full text (PMC3167012) does not contain those cases. It does contain sham-stimulus headache in healthy volunteers and the finasteride disclosure result (43.6% vs 15.3% sexual side effects). **Fixed**: those two examples now carry the citation as "(reviewed in …)". "Specific physiological change" became "specific symptom", since both outcomes are reported symptoms.
- **Kaptchuk 2010 inference too strong.** The article said the open-label result suggests "explicit propositional belief is not the sole driver". The trial told patients the pills had "been shown in clinical studies to produce significant improvement", so explicit expectation of benefit was induced. All of its outcomes (IBS-GIS, IBS-SSS, IBS-AR, IBS-QoL) are patient-reported. **Fixed**: the paragraph now says belief in an active drug is not required and gives both limits. The complication itself is kept, as the 2026-06-26 stability note asks.
- **Creative cognition presented as a replicated domain.** The lead read "replicated across … creative cognition", and the creative paragraph cites no experiment. This conflicts with the article's own 2026-06-26 statement that the data hold "in some channels — analgesic and motor placebo, self-focused interference with skill". **Fixed**: the lead now reads "documented in … and plausibly extending to creative cognition", the creative paragraph says the case "rests on phenomenological description rather than experiment", and Systematic mapping says "more tentatively, creative thought". The cross-domain structure that earlier reviews praised is kept.

### Low Issues Found

- Zheng & Meister 2025 measure the information rate of human behaviour. The article had "Consciousness operates at". **Fixed**: it now reads "Conscious throughput, measured as behavioural output, runs at", matching how `topics/bandwidth-of-consciousness` L193 frames the figure.
- The Further Reading label "consciousness and creative distinctiveness" was left over from the target's old title. **Fixed** to "consciousness and cognitive distinctiveness". The Creative insight link is now anchored to `#The Creative Mechanism`, a heading that exists on the target.

### Citation publisher-of-record web-verify (§2.4) — per-cite ledger

Raw sources were fetched and grepped: PubMed efetch abstracts, PMC BioC full text for Colloca & Miller, the OpenAlex abstract index for Gröpel & Mesagno, and the arXiv HTML for Zheng & Meister.

- Beilock & Carr 2001 (On the fragility of skilled performance) — metadata real-correct. Claim over-attributed ("outcome-focused attention preserves it"); fixed.
- Beilock, Carr, MacMahon & Starkes 2002 (When paying attention becomes counterproductive), *J Exp Psychol Appl* 8(1):6-16 — new citation, real-correct. Dual-task better than skill-focused for experienced golfers and for experienced soccer players using the dominant foot.
- Benedetti et al. 2003 (Conscious expectation and unconscious conditioning…), *J Neurosci* 23(10):4315-4323 — real-correct. Direction verified: verbal expectations "antagonized completely" conditioning for pain and motor responses and had no effect on GH or cortisol.
- Colloca & Miller 2011 (The nocebo effect and its relevance for clinical practice), *Psychosom Med* 73(7):598-603 — metadata real-correct. Illustrative examples were not in the source; replaced with examples that are.
- De la Fuente-Fernández et al. 2001, *Science* 293(5532):1164-1166 — real-correct. Striatal dopamine release to placebo, verified.
- Gröpel & Mesagno 2019, *IRSEP* 12(1):176-201 (online 2017-12-19) — metadata real-correct. Claim overstated; fixed.
- Kaptchuk et al. 2010, *PLoS ONE* 5(12):e15591 — metadata real-correct. Rationale and self-report limits added.
- Levine, Gordon & Fields 1978, *Lancet* 312(8091):654-657 — real-correct. PubMed gives the volume as 2(8091), ScienceDirect numbers it 312; both conventions are legitimate. The abstract says the data are "consistent with" endorphin mediation, and the article's present-tense statement reflects the later consensus.
- Nørretranders 1998, *The User Illusion*, Viking — real-correct. The ~16 bits/s figure was set by refine-draft `5c2e104b0c` and not re-litigated.
- Pollo et al. 2001, *Pain* 93(1):77-84 — metadata real-correct. Result misdescribed (critical); fixed.
- Smoulder et al. 2024, *Neuron* 112(20):3424-3433.e8 — real-correct. Preparatory activity is driven "into, and then past, a zone of optimal performance".
- Zheng & Meister 2025, *Neuron* 113(2):192-204 — real-correct. The figure measures behaviour, and the gloss was aligned to that.
- Southgate & Oquatre-six (2026-02-02) self-citation — title matches the live page. The date matches its `created` field, and three of the four citers in the corpus use the same form; left as is.

Inline ↔ References check by (surname, year), in both directions: complete. Beilock 2001 and Beilock 2002 are two separate works, and each now has both an inline cite and a reference entry. No superlative claims (helper output empty).

Cited-author stance: Benedetti, Zheng & Meister, Smoulder et al. and Pollo et al. are cited for empirical results only, and none is presented as endorsing the Map's dualist reading.

### Map-internal checks

The article contains no quotations of other Map pages. Anchors were verified against current text: `intentionality#Phenomenal Intentionality Theory` (L85), `empirical-phenomena-mental-causation#What Is Established and What Is Not` (L163), `tenets` block IDs `^dualism`, `^minimal-quantum-interaction` and `^bidirectional-interaction`, and the new `consciousness-and-cognitive-distinctiveness#The Creative Mechanism` (L149). The established/not-established paraphrase at L59 still matches the sibling's L165-167.

### Reasoning-Mode Classification (§2.6)

The Functionalist Response is Mixed (Two → Three), unchanged from earlier reviews. No editor vocabulary appears in the article prose.

### Counterarguments Considered

- Functionalist response — bedrock disagreement; not re-flagged.
- Open-label placebos — kept as an honest limit and made more precise (self-report and explicit-expectation caveats), not dismissed.
- Neural-level explanation in principle — unchanged.

## Optimistic Analysis Summary

### Strengths Preserved

- The channel-accurate Benedetti opening (analgesic and motor yes, hormonal no).
- The 2026-06-26 access/phenomenal demarcation, which this pass extends to the asymbolia and Relation-to-Site paragraphs, where it had not yet been applied.
- The four-feature significance analysis. Qualifier sensitivity now rests on the real Pollo design, which still makes the point: changing a qualifier on the same content (certain versus uncertain) grades the response.
- The bandwidth-to-quantum-tenet connection, still labelled as the Map's interpretation.

### Enhancements Made

- Nocebo examples are now taken from the cited review.
- The choking evidence is split correctly across Beilock & Carr 2001 and Beilock et al. 2002.
- The open-label complication is made more precise.

### Cross-links Added

- [pain-asymbolia](/concepts/pain-asymbolia/)
- [consciousness-and-cognitive-distinctiveness](/topics/consciousness-and-cognitive-distinctiveness/) (anchored to The Creative Mechanism)

## Remaining Items

- Out of scope, not edited: [concepts/interface-friction.md](/concepts/interface-friction/) L78 says "the distraction/self-focus split confirmed across 47 intervention studies by Gröpel & Mesagno 2019". This overstates the review in the same way the sentence fixed here did: the review sorts interventions by the two models and does not confirm them.
- Out of scope, not edited: [topics/empirical-phenomena-mental-causation.md](/topics/empirical-phenomena-mental-causation/) L97 says of Kaptchuk et al. (2010) "since here patients believe the opposite". The trial told patients the pills had "been shown in clinical studies to produce significant improvement", so explicit expectation of efficacy was induced. The sentence's own self-report/objective point is sound.
- In-page, left as is: Open-label "These remain content-specific—the improvement tracks the *type* of condition being treated" generalises from a single-condition trial. It is a low-priority wording issue.

## Stability Notes

- Ninth review. The calibration fixes made here (asymbolia, Relation to Site, creative cognition) apply the article's own 2026-06-26 access/phenomenal discipline to the paragraphs it had not reached. Future reviews should not restore "isolates the role of phenomenal quality", "provides empirical grounding", or "replicated across … creative cognition".
- Pollo et al. 2001 manipulated certainty (potent painkiller vs painkiller-or-placebo vs nothing). It did not manipulate drug strength, and the measured outcome was opioid requests at equal pain. Do not restore "strong vs mild … greater analgesia".
- Beilock & Carr 2001 does not test outcome-focused attention. The distraction-benefit result belongs to Beilock et al. 2002.
- The functionalist response is bedrock and is not to be re-flagged. The Benedetti channel qualifier is to be kept.
- The ledger above records metadata and result direction verified against the raw sources on 2026-11-15. Run the result-direction leg again only if the body or References change.