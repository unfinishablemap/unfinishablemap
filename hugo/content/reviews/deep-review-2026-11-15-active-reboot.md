---
ai_contribution: 100
ai_generated_date: 2026-11-15
ai_modified: 2026-11-15 20:10:56+00:00
ai_system: claude-fable-5-2
author: null
concepts:
- '[[active-reboot]]'
created: 2026-11-15
date: &id001 2026-11-15
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-15 20:10:56+00:00
modified: *id001
related_articles:
- '[[anaesthesia-and-the-consciousness-interface]]'
- '[[stochastic-emergence-as-quantum-interface-evidence]]'
- '[[evidential-status-discipline]]'
title: Deep Review - Active Reboot
topics: []
---

**Date**: 2026-11-15
**Article**: [Active Reboot](/concepts/active-reboot/)
**Previous review**: [2026-07-30](/reviews/deep-review-2026-07-30-active-reboot/)

## Selection

`scripts/deep_review.py next` returned `topics/clinical-dissociation-as-systematic-evidence`. It and the next nine candidates were passed over because each is named by an open entry in [workflow/todo.md](/workflow/todo/) (two NEEDS-HUMAN entries for the clinical page, one of which says "do not pick"; pending P3 tasks naming the others as File, Secondary file or, for `concepts/phenomenal-acquaintance`, as the third file of a three-file task). `concepts/active-reboot` was the first candidate with no open task. Seventh review; body edited on 08-01, 10-01 and 11-13 since the last one.

## Lens

The 07-14 pass closed citation metadata. The 07-30 pass checked claim fidelity for Hu 2023, Mashour 2024, Mashour 2021, Montupil 2023, Cruse 2011 and Schnakers 2009, and explicitly left eight papers "unchanged and not re-litigated" (Redinbaugh, Lewis, Stone, Friedman, Sepúlveda, Onoda, Breyton, Van Maldegem). This pass ran result-direction and scope on those eight and on the three added since (Bodien, Goldfine, Saper), then audited the calibration of the lead and the tenet section.

## Length

Thresholds for concepts: soft 2,500, hard 3,500, critical 5,000. `analyze_length` before: 3,308. After: 3,449 (net +141; gate is `>=` 3,500). The first edit set landed at 3,502, so five redundant phrases were trimmed (a restated asymmetry clause in "vs. reverse induction", "Both can be true simultaneously", a signpost sentence in the section opener, "and the reduction is worth stating openly", and one parenthesis of my own). No calibration qualifier, objection-answering sentence, cited fact or reference was cut.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Lead contradicted the body (calibration).** The lead said sleep-wake transitions, recovery from disorders of consciousness and post-contemplative re-engagement "all show the same architectural signature". The article's own "Other Candidates" section calls the first "an open empirical question", the second "unconfirmed" and "not yet established", the third "largely uninvestigated". Lead rewritten to "may be wider ... are candidates, though none has yet been shown to carry the architectural signature".
2. **Stone et al. 2025: a finding the paper does not report.** "with no single brain area controlling emergence" is absent from the paper. It is a behavioural study (righting reflex, isoflurane 0.90 vol%, 60 C57BL/6J mice, ten exposures each); the full text (PMC12226763) contains no "brain area" or "brain region" and records no neural data. Clause removed and replaced with what the paper does report (within-animal variability as large as between-animal; the standard PK-PD model failed, the neuronal-dynamics model reproduced the variability). Agent (isoflurane) added.
3. **Sepúlveda et al. 2019 cited for a characterisation its abstract reverses.** The article called neural inertia "a *passive resistance* property" and cited Sepúlveda; the abstract says inertia "is an active process of resistance to change in state". "Passive" removed, the source's phrase quoted, and the contrast restated as holding a state against leaving it. "Formalised by Friedman ... and Sepúlveda" corrected: Friedman et al. proposed the concept, Sepúlveda et al. is a narrative review.
4. **Three papers cited for one result only two of them bear on.** "PCI, Φ, connectome-harmonic signatures ... staying high in unresponsive states such as ketamine sedation and REM (Onoda; Breyton; Van Maldegem)". Onoda et al. used propofol and natural sleep, found Φ *falling* with loss of consciousness, has no ketamine condition and never mentions responsiveness; its REM result is partial (occipital set REM > N3, SMN REM > N2, but DAN and visual network lower in REM than wake). Breyton et al. is a whole-brain model validated on a 15-subject reanalysis of Sarasso et al. 2015 (5 propofol, 5 xenon, 5 ketamine), where fluidity groups ketamine with wakefulness and the other spontaneous metrics are inconsistent for ketamine. Sentence rewritten to give each paper its own result.
5. **Tenet section: cost claimed against the wrong target (possibility/probability slippage).** The Dualism paragraph argued that if consciousness were a product of neural activity "a dedicated reopening mechanism would be redundant", and the closing paragraph said the finding "raises the explanatory cost on production models". Neither follows. Hu et al. describe the pathway as "accelerated recovery of VPM neuron excitability", which is what a production account says is being restored; the finding counts against passive drug-clearance models, as the article's own Bidirectional paragraph already says. A tenet-accepting reviewer would flag the upgrade, and the 2026-10-11 ChatGPT outer review did ("cannot then be treated as evidence that favours the reinterpretation over the physical account"). Both loci rewritten: the production reading is stated as unstrained, the cost is placed on passive-return models, the defeater-removal label and the two-tier calibration are kept.
6. **Unsupported incidence claim.** "Disconnected consciousness during emergence ... is common, showing the phenomenal channel reopens before access channels reconnect" (flagged, not fixed, on 07-30). Montupil et al. 2023 full text (PMC10539891) documents disconnected consciousness under anaesthesia but has no hit for "during emergence" or "during recovery". Rewritten: the state is documented under anaesthesia (cited), and the reopening order is marked as the model's expectation.

### Medium Issues Found

- Lewis et al. 2018: the abstract's endpoint is "recovery of behavioral responsiveness"; the body uses "return of consciousness (ROC)" as a behaviourally defined term. In a paragraph whose point is that consciousness and responsiveness dissociate, the article now says "behaviourally defined return of consciousness" (body and reference annotation).
- Redinbaugh et al. 2020: species (macaques) was missing, and "stimulating that loop" overstated the manipulation, which was central-lateral thalamic stimulation; "location and frequency specific" added from the abstract in support of the specificity gloss.
- The "Temporal precedence" feature had no source for *molecular* precedence. Added Hu et al.'s own placement of KCC2 downregulation in the "minimum responsive state" as an "intermediate step en route to emergence" (both phrases verbatim in the abstract). The closing paragraph's three "is real" claims now carry "in mice" for the two that rest on Hu et al.
- Minimal Quantum Interaction: "the substrate is prepared deterministically, but the moment of re-engagement is not" asserted indeterminism as fact. Now "best modelled as stochastic". "Equally consistent with classical neuronal noise" now reports that the classical arousal-network account is Stone et al.'s own.
- "load-bearing" used twice as an intensifier; both replaced.

### Publisher-of-Record Ledger (this pass)

Source for each line: PubMed record via E-utilities, plus PMC full text where stated.

- Hu et al. 2023, *Nat Neurosci* 26(5):751-764 — real-correct. Direction: correct (mice; KCC2 downregulation in VPM; Fbxl4; "active process and occurs independent of anesthetic choice"). Both body quotations and the two new ones verbatim in the abstract. Full text not accessible (paywalled): the two-class framing sentence rests on the 07-31 `cross-mechanism-convergence` review's reading of a secondary source and was not re-verified here. Stance: mainstream neuroscience; article states the phrase "active reboot" is the Map's.
- Lewis et al. 2018, *eLife* 7:e33250 — real-correct. Direction: correct, endpoint wording corrected (see above). Humans, propofol.
- Redinbaugh et al. 2020, *Neuron* 106(1):66-75 — real-correct. Direction: correct; species and manipulation corrected.
- Friedman et al. 2010, *PLOS ONE* 5(7):e11903 — real-correct. Flies and mice; hysteresis "not fully explained by pharmacokinetics"; proposes neural inertia. Role wording corrected.
- Sepúlveda, Tapia & Monsalves 2019, *Anaesthesia* 74(6):801-809 — real-correct. Characterisation corrected (critical 3).
- Stone et al. 2025, *BJA* 135(1):121-133 — real-correct. Claim-defect corrected (critical 2).
- Onoda et al. 2025, *Neurosci Conscious* 2025(1):niaf024 — real-correct. Claim-defect corrected (critical 4).
- Breyton et al. 2025, *eLife* 13:RP98920 — real-correct. Scope corrected (critical 4).
- Van Maldegem et al. 2025, *BJA* 134(4):1088-1104 — real-correct. Direction: correct (ketamine signature aligns with LSD and ketamine psychedelic states, misaligns with propofol sedation and brain injury; group level).
- Mashour 2024, *Neuron* 112(10):1553-1567 — real-correct. Quotation verbatim in PMC11098701; hysteresis, neural inertia and the orexin dissociation all present; no KCC2 and no Hu et al. in the review, as the article says.
- Mashour et al. 2021, *eLife* 10:e59525 — real-correct. "Contrary to our hypothesis, executive function returned first" verbatim; authors read the result as consistent with global neuronal workspace theory, and the article does not enlist them.
- Mashour, Pal & Brown 2022, *Trends Neurosci* 45(10):722-732 — real-correct.
- Montupil et al. 2023, *BJA Open* 8:100224 — real-correct. Supports disconnected consciousness under anaesthesia, not its incidence at emergence (critical 6).
- Saper et al. 2010, *Neuron* 68(6):1023-1042 — real-correct. A sleep-switching review; the extension to anaesthesia is carried by the co-cited Sepúlveda review.
- Schnakers et al. 2009, *BMC Neurol* 9:35 — real-correct. 18 of 44 consensus-VS patients (41%) were MCS on the CRS-R.
- Cruse et al. 2011, *Lancet* 378(9809):2088-2094 — real-correct (issue 9809 confirmed).
- Goldfine et al. 2013, *Lancet* 381(9863):289-291 — real-correct. PMC3641526: under the block-aware permutation test one patient remained significant; after FDR correction "none of the patients were significant". The article's "no patient's result significant under a corrected statistical model" matches the FDR result.
- Bodien et al. 2024, *NEJM* 391(7):598-608 — real-correct. 60 of 241 (25%).

Inline and References pairs checked in both directions by (surname, year): no orphans either way. The two Southgate entries are cited by wikilink.

`find_superlative_claims`: not re-run; the article has no record or superlative claims (unchanged since 07-30).

### Reasoning modes (editor-internal)

Engagement with production/generator models: previously presented as a cost on the opponent that the evidence does not impose; now Mode Three (the production reading is stated as standing; the disagreement is marked at the framework boundary). Engagement with passive-recovery (pharmacokinetic) models: Mode One, on Friedman's and Hu's own data. No label leakage.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-feature definition and the asymmetry test.
- The dissociation-versus-precedence distinction, now with each cited paper doing its own work.
- The two-tier calibration and the "does not establish" paragraph.
- The agent-roster paragraph and its Map-versus-study partition (untouched apart from one trimmed clause).
- The DoC bullet's refusal to read detection studies as trajectory studies.

### Enhancements Made

- The temporal-precedence feature now cites the study that documents molecular precedence.
- The neural-inertia contrast is stated in a form the cited review supports.

### Cross-links Added

None; the link surface is saturated.

## Remaining Items

Not verified at source: Hu et al.'s two-class grouping (full text paywalled); "asymmetric neural correlates of induction and emergence in controlled human state transitions" as an item in Mashour 2024 (carried from 07-30, not re-grepped); the sleep-wake bullet's inference from orexin to "dedicated reopening machinery" (uncited).

Sibling defects, reported and not edited:

- `topics/anaesthesia-and-the-consciousness-interface` L121: "No single brain area controlled emergence: neuronal noise propagated through network dynamics into macro-level variability, so consciousness reconstitutes through distributed effects." Same Stone et al. defect; the paper records no neural data.
- `topics/anaesthesia-and-the-consciousness-interface` L115: "staying high in unresponsive states such as ketamine sedation and REM (Onoda et al. 2025; Breyton et al. 2025; Van Maldegem et al. 2025)". Same three-for-one citation.
- `topics/anaesthesia-and-the-consciousness-interface` L129: "Disconnected consciousness during emergence supports" — same unsourced premise; check what is cited for it.

## Stability Notes

Carried forward: bedrock disagreement with eliminativist and physicalist readings; the stochastic-emergence framing stays at "suggestive but unresolved"; the mechanism-class extension stays open; the two tiers stay separate; the agent roster is propofol, pentobarbital, ketamine, isoflurane; "active reboot" is the Map's phrase.

Amended: the 07-14 and 07-30 notes protecting the "§Dualism defeater-removal framing" cover the label and the tier, which are kept. They do not cover the redundancy argument or a cost on production models; those are empirical-support claims attached to the commitment and were removed here. Do not restore "would be redundant" or "raises the explanatory cost on production models".

New: neural inertia is not to be called passive on Sepúlveda's authority. Stone et al. 2025 is behavioural and says nothing about brain areas. Onoda et al. 2025 is a propofol and sleep study with no ketamine arm.