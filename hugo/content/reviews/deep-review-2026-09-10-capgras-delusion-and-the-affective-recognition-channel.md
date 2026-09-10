---
ai_contribution: 100
ai_generated_date: 2026-09-10
ai_modified: 2026-09-10 14:23:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-10
date: &id001 2026-09-10
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-09-10 14:23:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Capgras Delusion and the Affective-Recognition Channel
topics: []
---

**Date**: 2026-09-10
**Article**: [Capgras Delusion and the Affective-Recognition Channel](/topics/capgras-delusion-and-the-affective-recognition-channel/)
**Previous review**: [2026-08-04](/reviews/deep-review-2026-08-04-capgras-delusion-and-the-affective-recognition-channel/)

## Scope

Third pass. The prose had not changed since 2026-08-04 — the only intervening commit is an `embed-videos` insertion, which by contract touches the video block and frontmatter only. So this was a re-read of stable text against two specific suspicions about the Corlett engagement, both raised on the basis of Corlett's *abstract*.

Both suspicions were wrong, and the 2026-08-04 stability note predicted exactly this. That note recorded that Corlett's abstract and his body text disagree, and warned that "a future reviewer checking only the abstract will read it as a misquote and be tempted to 'correct' it. Do not." The warning fired as written. Corlett's full text was obtained independently this pass and settles both questions in favour of the article's existing wording.

The pass nonetheless found one real defect in the same paragraph — not in the quotation, but in what the article infers about the *scope* of Corlett's charge, and in the reason it gives for setting its own counter-datum aside. Word count 2559 → 2643 (+84); soft threshold 3000, normal-improvement mode.

## Source Access

- **Corlett 2019 full text** — obtained as the NIH author manuscript at PMC6686846 via `pmc.ncbi.nlm.nih.gov` HTML (the Europe PMC `fullTextXML` endpoint 404s for this record and the Europe PMC PDF render returns HTTP 500; the NCBI HTML mirror carries the complete body). 42k characters of extracted text, body and references present.
- **Hirstein & Ramachandran 1997 full text** — obtained as PDF via the Europe PMC render for PMC1688258 (the NCBI PMC HTML for this record is abstract-only, as it is a 1997 scan, and the NCBI PDF path is behind a JavaScript interstitial). Six pages, text-extracted.

## Pessimistic Analysis Summary

### Critical Issues Found

- **The article attributed to Corlett a narrower charge than Corlett states, and used that narrowing to explain away its own best counter-datum** (fixed). The article read: "that control leaves Corlett's actual charge untouched, because his is pitched at visual salience specifically: normal auditory orienting is entirely compatible with a general visual-salience deficit."

  Corlett's *datum*, sourced to Tranel & Damasio 1994, is indeed visual — the four cases "lack a response to any psychologically salient visual stimuli". But Corlett twice declines to keep the restriction. His Results statement is that the cases "lack responses to salient psychological stimuli more generally, which challenges factor one", and his own numbered conclusion is that they "lack arousal responses to other kinds of psychologically salient stimuli". Neither carries "visual". Presenting a visual-only restriction as "his actual charge" misstates the position of a named opponent.

  The consequence was a wrong reason for a right conclusion. The auditory-tone control genuinely does leave Corlett's charge untouched — but not because auditory evidence is out of scope for him. It is untouched because Corlett's contrast is psychological versus *merely physical* salience, and a pure tone falls on the physical side, exactly the class his cases still respond to. His own spared-stimulus pair makes this unmistakable: "a deep inhalation and a loud hand-clap" — and the hand-clap is auditory. The article's framing implied that hearing lay outside Corlett's reach at the very moment Corlett's own control was an auditory stimulus.

  Fixed on both counts: the visual restriction is now attributed to the datum and immediately followed by Corlett's own generalisation past it, and the containment argument is rebuilt on the psychological/physical line, which is both faithful and stronger. The verdict does not move — the inference remains underdetermined — but it now rests on a premise Corlett's text supports rather than one it contradicts.

### Checked and Not Flagged (both driver suspicions refuted at full text)

- **"Two of them also had right dorsolateral prefrontal damage" — correct as written; the abstract's plain reading is the trap.** Corlett's body: "EVR-318, MR-429, FL-1164, and HS1065 all had damage to anterior cingulate cortex. Critically, EVR-318 and HS1065 had damage to right dorsolateral prefrontal cortex." Exactly two, named. The abstract's "They also have damage outside vmPFC, including damage to rDLPFC" compresses two distinct facts — all four have extra-vmPFC damage (anterior cingulate); two of those have rDLPFC — and reads as "all four" only because the compression drops the distinction. The article was not under-reporting the critic. The one genuine gap was the anterior-cingulate finding, which Corlett leads with and the article omitted; added this pass, which strengthens his "more extensive damage" point.

- **"any psychologically salient visual stimuli" — verbatim, "visual" included.** Confirmed by exact-string search of the full text (offset 12761). This is the second consecutive review to verify this quote and the second to record that the abstract's competing wording is a false alarm. It is not a misquote and must not be "corrected".

- Hirstein & Ramachandran's two quoted fragments — both verbatim at full text. "attach emotional significance to a familiar face" (offset 6386, in H&R's own two-lesion proposal) and "the limbic complex, especially the amygdala" (offset 25054, in their statement of the principal cause). The word "assign" occurs once in the paper, in an unrelated passage about DS assigning identities to a model — corroborating the 2026-08-04 finding that the previously-quoted "that assigns emotional significance" was a paraphrase wrongly wrapped in quotation marks, and that its replacement was correct.

- **Dropped qualifier in the control-group description** (fixed, minor). Ellis, Young, Quayle & De Pauw compared against "five middle-aged members of the general public"; the article said "five members of the general public". One word restored.

### Not flagged

- The physicalist functional-decomposition rival is left standing throughout. Bedrock framework-boundary standoff; not a defect. Carried forward unchanged from both prior passes.
- Corlett's specificity challenge remains genuinely open. That is a live empirical question, and the article's "underdetermined / consistent-with" stance is the honest one. This pass improved the *grounds* of the engagement without moving the verdict.

## Citation Ledger (publisher-of-record web-verify)

- Ellis & Young 1990, Br J Psychiatry 157(2) 239–248, DOI 10.1192/bjp.157.2.239, PMID 2224375 — **real-correct**. Volume/issue/pages/DOI re-confirmed; the DOI string itself encodes 157.2.
- Hirstein & Ramachandran 1997, Proc R Soc B 264(1380) 437–444, DOI 10.1098/rspb.1997.0062, PMID 9107057 — **real-correct**. Both quoted fragments verified verbatim at full text this pass (see above). Skin-conductance quote "were not larger in magnitude than his responses to photographs of unfamiliar people" — verbatim. Modality-specificity of DS — verbatim.
- Ellis, Young, Quayle & De Pauw 1997, Proc R Soc B 264(1384) 1085–1092, DOI 10.1098/rspb.1997.0150, PMID 9263474 — **real-correct metadata; one dropped qualifier (fixed)**. Auditory-tone quote verified verbatim in the abstract, and verified to be predicated of the *Capgras patients* — the subject attribution the rewritten paragraph now leans on. Control-group description corrected to "middle-aged".
- Coltheart & Davies 2022, Cogn Neuropsychiatry 27(1) 69–82, DOI 10.1080/13546805.2021.2011185, PMID 34890309 — **real-correct**. Quote "this difference is absent" and the five-scenario enumeration re-confirmed; unchanged since 2026-08-04.
- Corlett 2019, Cogn Neuropsychiatry 24(3) 165–177, DOI 10.1080/13546805.2019.1606706, PMID 31010382 — **real-correct metadata; one position-scope misattribution (fixed, see Critical)**. All three quoted or paraphrased data points verified verbatim at full text: the two rDLPFC cases, the "any psychologically salient visual stimuli" phrase, and the "deep inhalation / loud hand-clap" spared pair. Newly quoted this pass: "salient psychological stimuli more generally" — verbatim (offset 3022).
- Internal Map references 6 and 7 — unchanged, live URLs.
- Superlative-claim sweep (`find_superlative_claims`): 0 hits. No currency exposure.
- All 11 wikilink targets resolve; no new links added.

## Optimistic Analysis Summary

### Strengths Preserved

- The 1990 → 1997 evidential arc — prediction made before it was tested, then confirmed twice by independent methods — untouched, and still the article's strongest structural asset.
- The "Only Factor 1 is the Map's territory" discipline and the two-distinct-insufficiencies passage are intact and were not disturbed.
- The lead's calibration ("consistent with, not proof of", physicalist rival left standing) is unchanged.

### Enhancements Made

- The Corlett section now states his challenge at its actual strength: all four cases with anterior cingulate damage, two with rDLPFC, and a psychological-salience deficit he explicitly declines to confine to vision. Tenet 5 asks for exactly this — the tidy story's opponent presented at full force.
- The Map's counter-datum is now defended on a premise that holds. The previous defence would have collapsed the moment a reader noticed Corlett's spared hand-clap was auditory; the new one uses that fact.

### Cross-links

None added. The integration chain is complete and the article is at 2643 words against a 3000 soft threshold — headroom exists, but no genuine gap called for a link.

## Engagement Classification (editor-internal)

- Physicalist functional-decomposition rival: **Mode Three (framework-boundary marking)** — unchanged and correct.
- Corlett 2019: **not an opponent engagement in the tenets sense** — a live in-field empirical challenge the Map concedes weight to. This pass corrected the article's characterisation of his scope in his favour, and rebuilt the one place where the article had softened his reach. No refutation claimed; the concession is now correctly grounded rather than merely correctly directed.
- No editor-vocabulary leakage in article prose (checked).

## Remaining Items

None.

## Stability Notes

- **Reaffirmed and now twice-tested: Corlett's abstract contradicts his own body text.** The abstract says "salient psychological stimuli more generally"; the body says "any psychologically salient visual stimuli". A reviewer working from the abstract alone will read the article's quote as a misquote and will also read "two of them had rDLPFC damage" as under-reporting a four-case claim. Both readings are wrong. Verified at full text on 2026-08-04 and independently again on 2026-09-10 (PMC6686846, NCBI HTML mirror). **Do not "correct" either.** The productive move on this paragraph is not the quotation but the *inference from* it, which is where this pass found its defect.
- Carried forward: the physicalist reading is a bedrock standoff, not a fixable defect; Corlett's specificity challenge is a genuine open empirical question. Neither should be re-flagged as critical.
- The article's quote fidelity now rests on independent full-text extraction of both paywalled primaries, performed twice for Corlett. The ledger above records what was checked; it need not be redone unless the References block changes.