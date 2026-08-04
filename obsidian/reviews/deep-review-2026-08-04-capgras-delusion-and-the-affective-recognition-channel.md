---
title: "Deep Review - Capgras Delusion and the Affective-Recognition Channel"
created: 2026-08-04
modified: 2026-08-04
human_modified:
ai_modified: 2026-08-04T02:08:29+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-04
last_curated:
last_deep_review:
---

**Date**: 2026-08-04
**Article**: [[capgras-delusion-and-the-affective-recognition-channel|Capgras Delusion and the Affective-Recognition Channel]]
**Previous review**: [[deep-review-2026-07-10-capgras-delusion-and-the-affective-recognition-channel|2026-07-10]]

## Scope

Second pass. The 2026-07-10 review was an argument-lens cross-review that explicitly deferred the citation channel ("web-verified at publisher during the create pass; not re-litigated") and recorded no per-cite ledger. Under the skill's §2.4 rule that counts as skipped, so this pass ran the full publisher-of-record web-verify — including full-text PDF extraction for the two paywalled primaries — and it produced the majority of the findings below. Word count 2201 → 2326 (+125); soft threshold 3000, so normal-improvement mode throughout.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Inverted dissociation in the Tenet 1 paragraph** (fixed). The sentence read: felt familiarity "is separable from perceptual identification: the second can be selectively removed while the first runs untouched." The ordinals point the wrong way — that describes prosopagnosia, not Capgras — and it contradicts the article's own lead ("the felt 'mineness' ... is severed while perceptual identification of the face stays intact") and the whole body. Dates from the original create (8624aa521) and survived the 2026-07-10 pass; a `fresh-create-defect-tail` instance. Fixed by naming the components instead of using ordinals.

- **Paraphrase presented as a verbatim quote from Hirstein & Ramachandran** (fixed). The article had the limbic system `"that assigns emotional significance"` in quotation marks. The phrase is not in the paper: full-text extraction (PMC1688258 PDF) shows "assign" occurs once, in an unrelated sentence about memory files. The paper's actual wordings are "the brain's ability to **attach** emotional significance to a familiar face" and "the dorsal visual route responsible for **giving** the face its emotional significance." The source of the error is traceable: the research note ([[capgras-delusion-and-the-affective-recognition-channel-2026-07-10]] line 46) writes the phrase as an *unquoted* paraphrase, and the create pass wrapped that paraphrase in quotation marks — the `coalesce-wraps-paraphrase-as-fabricated-verbatim-quote` pattern. The note itself is fine and needs no fix. Repaired by substituting two grep-verified verbatim fragments: "the limbic complex, especially the amygdala" and "attach emotional significance to a familiar face". The anatomical substance was already faithful (H&R: "a failure of communication between areas of ventral stream processing in the temporal lobe ... and the limbic complex, especially the amygdala").

- **Coltheart & Davies scenario count did not match the list** (fixed). The article listed four targets — acquaintance, familiar voice, pet, personal possession — then called them "five scenarios." The source's five are close relatives *plus* those four; the article had generalised "beyond faces" and silently dropped the base case while keeping the count. Fixed by restoring the close-relative case as the thing being generalised beyond, and marking the total as "five scenarios in all."

### Medium Issues Found

- **Corlett's datum attributed to the wrong patient group** (fixed). "The absent skin-conductance responses may not be specific to familiar faces at all" read as a claim about Capgras patients. Corlett's finding is about the four *non-delusional* vmPFC cases that two-factor theorists cite as evidence Factor 1 alone is insufficient — the generalisation to Capgras patients is an inference, not his datum. Fixed by naming the subject and marking the inference ("if that pattern holds for Capgras patients too"). Corlett's own contrast qualifier, dropped in the original, was also restored: the deficit spared "salient physical stimuli (a deep inhalation and a loud hand-clap)".

- **A directly relevant counter-datum was missing from the Corlett ledger** (fixed). Ellis, Young, Quayle & De Pauw 1997 ran the specificity control Corlett found missing in the vmPFC cases: "orienting responses to auditory tones were normal in magnitude and rate of initial habituation, showing that the hyporesponsiveness is circumscribed." Added — with the scope Tenet 5 requires. Normal auditory orienting rules out a *global* arousal collapse but leaves Corlett's charge standing, because his claim is pitched at "psychologically salient **visual** stimuli" specifically. Adding the datum without that scoping would have converted an honest underdetermination into a false rebuttal; the article now states both halves.

- **Reference-block inconsistency** (fixed). Ellis, Young, Quayle & De Pauw 1997 was the only entry lacking a DOI (10.1098/rspb.1997.0150 added); Corlett 2019 was the only journal entry lacking a PMID (31010382 added).

### Not flagged

- Corlett's challenge remains genuinely unresolved. Per the 2026-07-10 stability note, that is a live empirical question, not a defect, and the article's "underdetermined" stance is the honest one. This pass sharpened the ledger on both sides without moving the verdict.
- The physicalist functional-decomposition rival is left standing. Bedrock framework-boundary standoff; not re-flagged.

## Citation Ledger (publisher-of-record web-verify)

- Ellis & Young 1990, *Accounting for delusional misidentifications*, Br J Psychiatry 157(2) 239–248, DOI 10.1192/bjp.157.2.239, PMID 2224375 — **real-correct**. Mirror-image-of-prosopagnosia framing confirmed at PubMed.
- Hirstein & Ramachandran 1997, *Capgras syndrome: a novel probe...*, Proc R Soc B 264(1380) 437–444, DOI 10.1098/rspb.1997.0062, PMID 9107057 — **real-correct metadata; one quote defect**. Quote "were not larger in magnitude than his responses to photographs of unfamiliar people" — verbatim ✓. Modality-specificity of DS (impostor claim when looking, not on the telephone) — verbatim in abstract ✓. Amygdala anatomy — faithful ✓. Quote "that assigns emotional significance" — **not in the source**; replaced with two verbatim fragments (see Critical above).
- Ellis, Young, Quayle & De Pauw 1997, *Reduced autonomic responses to faces in Capgras delusion*, Proc R Soc B 264(1384) 1085–1092, DOI 10.1098/rspb.1997.0150, PMID 9263474 — **real-wrong-metadata (DOI missing, added)**. Five Capgras patients, five general-public controls, five psychiatric controls on similar antipsychotic medication — all confirmed ✓. Newly-quoted auditory-tone sentence verified verbatim against the abstract.
- Coltheart & Davies 2022, *What is Capgras delusion?*, Cogn Neuropsychiatry 27(1) 69–82, DOI 10.1080/13546805.2021.2011185, PMID 34890309 — **real-correct metadata; one count defect (fixed)**. Quote "this difference is absent" — verbatim ✓ ("In Capgras delusion, this difference is absent, prompting the delusional idea that a familiar person is actually a stranger"). Five scenarios enumerated in the abstract: close relatives, acquaintance, voice of a familiar person, pet, personal possession — article's list corrected.
- Corlett 2019, *Factor one, familiarity and frontal cortex*, Cogn Neuropsychiatry 24(3) 165–177, DOI 10.1080/13546805.2019.1606706, PMID 31010382 — **real-correct metadata (PMID added)**. Quote "any psychologically salient visual stimuli" — **verbatim ✓, vindicated against a near-miss**. The EuropePMC abstract says "salient psychological stimuli more generally" with no "visual", which reads as a misquote; the full text (PMC6686846) contains the article's phrase exactly. A `citation-verify-false-negative` that would have flipped a correct quote had verification stopped at the abstract. "Two of them also had right dorsolateral prefrontal damage" — confirmed verbatim: "Critically, EVR-318 and HS1065 had damage to right dorsolateral prefrontal cortex" ✓. Four vmPFC cases — confirmed ✓.
- Internal Map references 6 and 7 (recognition-void, neurological-dissociations-as-interface-architecture) — live, correct URLs.
- Superlative-claim sweep (`find_superlative_claims`): no hits, no currency exposure.
- All 10 wikilink targets resolve; no bare-slug markdown links; no EOF tool-leak artifact.

## Optimistic Analysis Summary

### Strengths Preserved

- The 1990 → 1997 evidential arc (prediction made before it was tested, then confirmed by a single-case probe and a medication-matched group study) is untouched; it remains the article's strongest structural asset.
- The "Only Factor 1 is the Map's territory" discipline, and the two-distinct-insufficiencies fix from the 2026-07-10 pass, are intact and were not disturbed.
- Voice and calibration preserved throughout. No hedging added beyond what the corrected Corlett scoping required.

### Enhancements Made

- The Corlett section now carries the actual shape of his argument — four cases, two with rDLPFC damage, a visual-salience-general deficit sparing physical stimuli — instead of a compressed gloss. It reads as a stronger challenge, which is what Tenet 5 honesty requires.
- The auditory-tone control gives the Map's side of the ledger a real datum rather than an assertion, while the scoping sentence prevents it from over-reaching.

### Cross-links

No new cross-links. The interpreter-module link added by the 2026-08-04 refine pass is appropriate and was left as-is; the article's integration chain is complete.

## Engagement Classification (editor-internal)

- Physicalist functional-decomposition rival: **Mode Three (framework-boundary marking)** — unchanged and correct; the article concedes the rival explains every datum equally well.
- Corlett 2019: **not an opponent engagement** — a live in-field empirical challenge the Map concedes weight to. This pass increased the weight conceded (fuller statement of his claim) while adding one genuine counter-datum, correctly scoped. No refutation claimed.
- No editor-vocabulary leakage in article prose (checked).

## Remaining Items

None.

## Stability Notes

- Carried forward from 2026-07-10 and reaffirmed: the physicalist functional-decomposition reading is a bedrock standoff, not a fixable defect; Corlett's specificity challenge is a genuine open empirical question and the "underdetermined / consistent-with" stance is the honest position. Neither should be re-flagged as critical.
- **New**: the Corlett quote "any psychologically salient visual stimuli" is verbatim in the paper's full text but *conflicts with the wording of its own abstract*, which drops "visual" and says "more generally". A future reviewer checking only the abstract will read it as a misquote and be tempted to "correct" it. Do not. Verified at full text (PMC6686846) on 2026-08-04.
- The article's own quote-fidelity now rests on full-text extraction for both paywalled primaries; the ledger above records what was checked so it need not be redone unless the References block changes.
