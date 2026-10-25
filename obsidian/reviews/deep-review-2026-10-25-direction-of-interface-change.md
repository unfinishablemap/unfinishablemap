---
title: "Deep Review - Direction-of-Interface-Change Signatures"
created: 2026-10-25
modified: 2026-10-25
human_modified:
ai_modified: 2026-10-25T17:26:55+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-25
last_curated:
---

**Date**: 2026-10-25
**Article**: [[direction-of-interface-change|Direction-of-Interface-Change Signatures]]
**Previous review**: [[deep-review-2026-08-18-direction-of-interface-change|2026-08-18]]

This is the fourth review, 68 days after the third. The page was not converged in the sense the earlier stability notes assumed. Since 2026-08-18 it had eight commits, five of them targeted `refine-draft` passes (09-20, 09-28, 10-11, 10-19, 10-25 03:27Z), plus propagations from `memory-channel-interface-evidence` (10-20) and `census-change-points` (10-13). Prose grew from 1850 to 2439 words. It gained two new references (Huang et al. 2021, Hu et al. 2023) carrying verbatim quotes, and its Constrain, Not Establish and Relation to Site Perspective sections were rewritten. None of this had had a review pass. None of the linked pages changed after the page's last edit at 03:27Z today.

Word count (analyze_length): 2806 → 2813 (+7). Prose 2439, apparatus 374. Status `soft_warning` on the concepts soft threshold of 2500. Hard threshold 3500, not near it. Edits were kept close to length-neutral.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Member two stated the terminal-lucidity channel order as fact, and the citation placement credited that order to Nahm et al. 2012.**

Old (L47): "…channel returns *last* when a deeply anaesthetised brain emerges, yet *first and most prominently* in terminal lucidity, where patients … (Nahm, Greyson, Kelly, and Haraldsson 2012). The same channel, opposite recovery position, distinguished by…"

After the 2026-10-09/10-20 autonoetic-first calibration, the source article treats this ordering as a report, not a measurement. At L106 it says: "no episode has been recorded prospectively … The ordering is what the case literature suggests, not a measured result". At L130 it says "is reported to return *first and most prominently*. If the reports have that sequence right…". The research note `research/autonoetic-first-vulnerability-ordering-2026-10-09` §3 table records that the terminal-lucidity sources (Nahm et al. 2012, Batthyány & Greyson 2021, Griffin et al. 2024) measured "Occurrence, timing, duration, communication quality". On both ordering steps it scores them "Silent", and §1 item 3 says "Terminal lucidity has no channel-order data". The 10-20 propagation pass edited this file's member three but left member two's flat claim in place. A reviewer who accepts the tenets would still flag this, because it drops a qualifier that the page's own named source now carries.

New: "…yet is reported to return *first and most prominently* in terminal lucidity, where patients … (Nahm, Greyson, Kelly, and Haraldsson 2012). The case collections record occurrence and timing, not channel sequence, so the ordering rests on retrospective narratives. If they have it right, the same channel takes opposite recovery positions, distinguished by…"

The same flat claim had been repeated in the Tenet 3 paragraph (L83): "it returns last under rising substrate function yet first under falling substrate function". It now reads "…yet is reported to return first under falling substrate function."

**2. The Non-Independence Caution contradicted the page's own later sorting of hysteresis.**

Old (L65): "The hysteresis, the recovery-order reversal, the abrupt reconnection, and the direction-decoupled timing all trace to one architecture being addressed in direction-dependent order…". The surrounding text is conditioned on "If the interface reading is right". This predates the 10-11 recalibration, after which L71 says the hysteresis and timing members "cost production nothing extra", because generic finite-rate dynamics produce them. L79 also says hysteresis "is a property of the substrate's own bistable switch and touches neither leg". So the sentence placed every member under the interface architecture when the page itself says two members belong to ordinary substrate dynamics. The common-cause caution is not weakened by the fix. It is stronger, because those two members share a cause available to both readings.

New: "All four trace to one architecture addressed in direction-dependent order, and two of them, hysteresis and timing, to dynamics any substrate reading shares (`[[#constrain-not-establish|explained below]]`); none independently re-establishes that the architecture exists." (−1 word)

### Medium Issues Found

- **Tenet 5 self-binding was missing at the one place the page uses parsimony for the Map's side** (L73). Old: "the advantage is comparative and bounded: it is a point on parsimony grounds at the mechanism-cost layer (…), not positive evidence that the filter reading is true." The tenets page says Tenet 5 "binds the Map's use of parsimony, not only its critics'… parsimony cannot decide for or against a framework when the relevant knowledge is incomplete". New: "…a parsimony point at the mechanism-cost layer (…), which the Map's own [[tenets#^occams-limits|Tenet 5]] bars from deciding the comparison, and not positive evidence that the filter reading is true."
- **Banned construct** (L67). Old: "This caution is not a footnote to the family. It is the reason the family is worth naming…". New: "This caution is the reason the family is worth naming…" (−8 words).
- **"load-bearing" as an intensifier** in the description and lead L37 ("is the load-bearing variable"). Both now read "is the explanatory variable" (net 0).
- **Redundant restatement** (L83). The Tenet 3 paragraph had restated L73's bandwidth and reconstruction-cost clause almost word for word ("channels differing in bandwidth and reconstruction cost may block and reopen in an order that depends on the direction and cause of the change"). It was cut, leaving "the section above finds a purely inbound filter consistent with direction-sensitivity, whether or not anything acts back." (−23 words, which offset most of the critical-1 addition.)

### Citation Web-Verification (publisher of record: Crossref REST + Europe PMC abstract, raw text grepped)

- **Huang, Z., Tarnal, V., Vlisides, P. E., et al. (2021)**, *Asymmetric neural dynamics characterize loss and recovery of consciousness*, *NeuroImage* 236, 118042, DOI 10.1016/j.neuroimage.2021.118042 (PMID 33848623, PMC8310457). State: **real-correct**. Crossref lists eight authors with Huang, Tarnal and Vlisides first, so "et al." is right. **Quote**: "Pharmacokinetic effects could not account for the difference" is a verbatim prefix of the abstract's sentence "…the difference in neural dynamics between induction and emergence". **Result direction**: the abstract reports that temporal autocorrelation "gradually increased" en route to unconsciousness and that regaining consciousness was "associated with an abrupt restoration of cortical but not subcortical temporal autocorrelation". It used propofol "at incrementally adjusted target concentrations". The article's paraphrase keeps the direction and the cortical scope. **Stance**: the authors conclude that a rapid increase in cortical processing speed "may be a mechanism that reboots consciousness". This is a physical-mechanism reading. The article uses it correctly, as evidence that ordinary dynamics break the mirror, and does not enlist it for the filter reading.
- **Hu, J.-J., Liu, Y., Yao, H., et al. (2023)**, *Emergence of consciousness from anesthesia through ubiquitin degradation of KCC2 in the ventral posteromedial nucleus of the thalamus*, *Nature Neuroscience* 26(5), 751–764, DOI 10.1038/s41593-023-01290-y (PMID 36973513). State: **real-correct**. Crossref lists eight authors, ending with Song, X.-J. **Quote**: "an active process" is verbatim ("This pathway to recovery is an active process and occurs independent of anesthetic choice"). The article's "across the anaesthetics tested" is a fair, slightly narrower reading of "diverse anesthetics" and "independent of anesthetic choice". **Result direction**: the abstract reports KCC2 downregulation "serves as a common mechanism by which the brain regains consciousness". "Drives emergence" is a close paraphrase and was left as is. **Stance**: a molecular-physiological account, used correctly as production-side physics.
- **Sepúlveda, Tapia & Monsalves (2019)**, **Stone, Kelz, Proekt & Wasilczuk (2025)** and **Nahm, Greyson, Kelly & Haraldsson (2012)**: unchanged since the claim-match pass on 2026-07-16 and the Crossref pass on 2026-08-18. The body claims attached to Sepúlveda and Stone did not change. Not re-fetched. Nahm 2012's **attached claim changed in meaning** under critical 1. The ledger now limits it to what the 07-16 claim-match certified: occurrence in advanced dementia in the hours before death. It does not cover channel order.
- **Inline ↔ References**: all five empirical inline cites have entries, and every entry is cited inline. The two Southgate & Oquatre-sept self-cites are the Map's convention. No orphans in either direction.
- **Coiner check**: "neural inertia" is attributed to Sepúlveda et al. with "characterise", not "coin". Friedman et al. 2010 coined it, and the page makes no coinage claim. "Terminal lucidity" is not credited to anyone on this page. No coiner/populariser error.
- `find_superlative_claims`: no superlatives in the edited passages.

### Counterarguments Considered

- Production theorist (Dennett/Churchland personas): Mode Three, framework-boundary marking, unchanged. The page concedes that "a production account willing to pay the per-case cost absorbs every signature in the family". Since 10-11 it also concedes that two members cost production nothing. No boundary substitution, and no editor vocabulary in the prose.
- Empiricist (Popper): the discriminating test is still stated as "a proposed experiment, not a result". Correct.
- Buddhist (Nagarjuna): not engaged on this page. No madhyamaka claims, so nothing to mark.
- Quantum Skeptic / Many-Worlds: the quantum reading of the timing member stays deferred to the stochastic-emergence article. MWI is not engaged.

## Optimistic Analysis Summary

### Strengths Preserved

- The calibration spine ("constrain… do not establish", "not four independent confirmations", tier-elevation reserved for a discriminator). The Hardline Empiricist reads both critical fixes as further restraint, not upgrades.
- The 10-11 finite-rate physics paragraph (heterogeneous time constants, adaptation, multistability), with its new Huang/Hu evidence, now verified. This is the page's most important improvement since August, and it was kept intact.
- The leg-sorting paragraph in Relation to Site Perspective (P-CS6), and the Tenet 3 paragraph's conclusion that "the family cannot be cited against" a receive-only architecture. That conclusion is an evidential-scope claim and does not concede epiphenomenalism. The outbound leg is still owed separately.
- The "centralisation buys the guard" argument.

### Enhancements Made

- Report-scoping of the terminal-lucidity order, in two places (critical 1).
- Internal-consistency repair of the non-independence sentence, using a named-anchor forward reference (critical 2).
- Tenet 5 self-binding clause (medium).
- Removal of the banned construct and of "load-bearing" (medium ×2).

### Cross-links Added

- `[[tenets#^occams-limits|Tenet 5]]`, a new anchor target for this page.
- `[[#constrain-not-establish|explained below]]`, a same-page anchor. The heading already resolves at `#constrain-not-establish` in Hugo.

## Remaining Items

None on this page. Out-of-scope findings for the driver are below.

- `apex/self-concealing-interface` L107 still states the same order flatly: "the autonoetic channel returns *last* on anaesthesia emergence yet *first and most prominently* in terminal lucidity". It needs the same "is reported to return" scoping. The 10-20 changelog left it alone because memory-channel "itself still uses" the wording, but memory-channel now says "is reported to return". The same line has a "not in the intact ensemble, but in the *order*…" contrast that is close to the banned pattern.
- `archive/topics/recovery-order-asymmetry-as-interface-evidence` L66 ("often returns *first and most prominently*"). Archive, not edited.

## Stability Notes

- The production account absorbing every signature at per-case cost is a bedrock disagreement the page concedes. Reaffirmed. Do not re-flag it.
- **Correction to the 2026-08-18 note "the citation channel is exhausted"**. That note held only until new references arrived. Two arrived on 10-11, and both are now verified with grepped quotes. If a future pass adds a reference or changes the claim attached to an existing one, re-open the channel for that cite only.
- **Stability notes that assume a frozen page fail when targeted refine-drafts keep landing.** Five refine-draft passes landed between reviews, and each fixed one line while the lines next to it went unchecked. In this pass, the member-three fix of 10-19/10-20 left member two's matching defect in place two lines above it.
- Member two now carries its own evidential caveat. Member three remains "the family's least secure member". Do not let an optimistic pass remove either caveat.
- Hysteresis and timing are substrate-dynamics members, and the non-independence section now says so. A future edit that re-attributes them to the interface on the interface reading would re-open critical 2.
