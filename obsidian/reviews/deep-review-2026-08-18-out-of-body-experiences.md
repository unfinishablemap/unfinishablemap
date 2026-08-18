---
title: "Deep Review - Out-of-Body Experiences"
created: 2026-08-18
modified: 2026-08-18
human_modified: null
ai_modified: 2026-08-18T00:31:31+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-18
last_curated: null
---

**Date**: 2026-08-18
**Article**: [[out-of-body-experiences|Out-of-Body Experiences]]
**Previous review**: [[deep-review-2026-07-14-out-of-body-experiences|2026-07-14]]

## Lens Selected

The 2026-06-03 pass ledgered all citation *metadata* at publisher of record; the 2026-07-14 pass
ran *verbatim-quote fidelity* and fixed the Ehrsson misquote. Both lenses are carried forward.

Since 07-14 the article received one real body change (commit `de29e97800`, the
`sleep-paralysis-and-interface-reassembly` integration chain): a new empirical sentence and a new
reference, **neither of which had ever been verified**. Two lenses were therefore run fresh:

1. **Publisher-of-record verification of the new Herrero et al. 2025 cite** (§2.4).
2. **The parapsychology-firewall lens** — never applied to this article in four prior reviews,
   despite OBEs being the corpus's most psi-adjacent topic.

A full inline↔reference orphan audit was also run.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Herrero et al. 2025 empirical claim wrong on low-gamma — FIXED.** The article stated the two
   OBE episodes showed "increased delta and theta with reduced alpha, beta and low-gamma relative
   to wakefulness." Verified against the publisher full text (nature.com, open access): low-gamma
   moved in **opposite directions** in the two episodes — *"OBE 1 exhibited significant reductions
   in low-gamma relative power across frontal, central, and temporal regions, in contrast to OBE 2,
   which showed increases in parieto-occipital areas."* Beta decrease is real but region-specific:
   *"significant decreases were observed in fronto-central beta relative power for both OBEs, but
   OBE 1 also exhibited increases in temporal and parietal regions."* Delta, theta and alpha were
   correct. Corrected to: "both showing increased delta and theta with reduced alpha and reduced
   fronto-central beta relative to wakefulness, while low-gamma moved in opposite directions in the
   two episodes."

   **This defect was already found and fixed two days earlier in the sibling article**
   ([[deep-review-2026-08-16-sleep-paralysis-and-interface-reassembly|2026-08-16]]) but the fix was
   applied file-by-file and the identical sentence here stayed live — the
   `fix-by-file-leaves-string-siblings-live` shape. Verified independently here from the raw
   publisher text rather than inherited from that review.

2. **Herrero et al. 2025 reference metadata wrong — FIXED.** Verified via Crossref
   (`10.1038/s41598-025-18748-7`, publisher-deposited) and confirmed against the author block on
   the article page: *Nerea L. Herrero, Yohann Corfdir, Aylin A. Vázquez-Chenlo, Lucila Capurro &
   Cecilia Forcato*, *Sci Rep* **15**, 33586 (2025).
   - `Corfdir, C.` → `Corfdir, Y.` (Yohann)
   - `Capurro, A.` → `Capurro, L.` (Lucila)
   - `Vázquez-Chenlo, A.` → `A. A.`
   - Added missing volume/article number: `15, 33586`

3. **Falsifier #1 pointed the wrong way relative to the Map's own firewall — FIXED.** The
   "What Would Challenge This View?" list said replicated above-chance hits on hidden targets would
   mean "the disembodied-consciousness reading would gain serious empirical support." But
   [[parapsychology-firewall]] holds that spectacular, reliable, ensemble-detectable psi
   **disconfirms** the Map's framework: a replicable channel delivering content the brain never
   generated as a candidate breaches Constraint 3 (content-confinement) and, being a reliable
   information channel, Constraint 2 (no-signalling). The Map sits on the *unfavourable* side of
   that result.

   This is a calibration error, not a bedrock disagreement — it passes the §2 diagnostic test: a
   reviewer who fully accepts the Map's tenets would still flag it, because the inconsistency is
   between two Map articles. Fixed by stating the double edge: the result would refute the
   self-model-only account *and* strain the Map's own interface. Added
   `[[parapsychology-firewall]]` to the body, Further Reading, and `related_articles` — the article
   previously had **no link to the firewall at all**, while eleven less psi-adjacent articles do.

### Citation Web-Verify Ledger (publisher of record)

Method: Crossref REST API for publisher-deposited metadata (immune to search-index
self-contamination), plus the open-access full text from nature.com for the empirical claims, plus
PubMed/NEJM for De Ridder. Empirical claims adjudicated by grep of raw retrieved text, never by
extraction-prompt confirmation.

- **Herrero et al. 2025** (*Sci Rep* 15:33586) — **real-wrong-metadata + real-wrong-claim**
  (Critical 1 and 2). Correct in the article: "exploratory", the two-episode count (paper: *"10
  episodes (3 LDs, 2 SP, 2 OBEs, 3 FAs)"*), and increased delta/theta with reduced alpha.
- **De Ridder et al. 2007** (*NEJM* 357(18):1829–1833, `10.1056/NEJMoa070010`) — **real-correct**.
  Author list, venue, volume, issue, pages and year all verified at Crossref and PubMed
  (PMID 17978291). Was an unanchored orphan; now anchored (see Medium 1).
- Blanke 2002/2004, Blanke & Mohr 2005, Lenggenhager 2007, Ehrsson 2007, AWARE I 2014,
  AWARE II 2023 — **real-correct**, carried forward from the exhaustive 06-03 metadata ledger and
  the 07-14 verbatim-quote ledger. Not re-litigated (no body or References change touched them).
- **Metzinger 2009** (*The Ego Tunnel*, Basic Books) — real-correct; was an unanchored orphan, now
  anchored (see Medium 1).
- Southgate & Oquatre-* self-cites — legitimate Map self-citations, anchored via body wikilinks
  rather than author-year. Not orphans. Not stripped.

**Superlative sweep**: the article's "have begun to appear" is *better* calibrated than its source
research note, which called the paper "the first EEG of sleep OBEs". The paper makes **no priority
claim** — every occurrence of "first" in the full text is "first two principal components", "first
author", "first-person reports", or discourse "First,". It explicitly cites prior EEG work on
unusual bodily experiences including OBEs and calls for *"systematic EEG investigations of OBEs
occurring specifically during sleep."* No superlative defect in the article; the superlative was
fixed at its source (see Family Resolution).

### Family Resolution — the defect fixed at origin

The wrong band-power claim and wrong reference metadata originated in
`research/hypnopompia-and-sleep-paralysis-as-interface-reassembly-out-of-order-2026-08-12.md` and
propagated into two articles. The sibling article was fixed on 08-16 and this article today, but the
**research note was still carrying the original error** — so the next `expand-topic` run drawing on
it would have re-propagated the same defect. Corrected at source (6 loci):

- Reference entry: same four metadata corrections as above.
- OBE key-point: low-gamma opposite-directions correction.
- SP key-point: "increased beta and low-gamma" → increased low-gamma in both, beta in only one of
  the two subjects. Verified from full text: *"Both episodes showed increased low-gamma relative
  power"*; against REM only Subject 5 *"demonstrated significant increases in alpha and beta
  activity"*; against S1 the two subjects showed *"contrasting patterns in beta relative power."*
- Executive-summary restatement of the same SP claim.
- Evidence-table row.
- Section header and the explicit "first EEG recordings" priority claim → replaced with the
  authors' actual position.

### Medium Issues Found

1. **Two orphan references, not one — both FIXED by anchoring.** A full surname audit of the body
   (frontmatter and References stripped) found inline counts: Blackmore 3, Blanke 10, Mohr 2,
   Ehrsson 3, Parnia 3, Sabom 1, Lenggenhager 1, Herrero 1 — and **Metzinger 0, De Ridder 0**.
   - *Metzinger 2009* anchored at the lead's first use of "phenomenal self-model", which is
     Metzinger's coinage and was previously used unattributed. Fixes the orphan and an
     unattributed technical term in one edit.
   - *De Ridder 2007* anchored in §TPJ Stimulation with a one-sentence summary verified against the
     NEJM abstract: OBE repeatedly elicited by stimulating an implanted electrode over the right
     superior temporal gyrus in a tinnitus patient, with PET localising activation to the
     temporo-parietal junction. Genuine convergent evidence that strengthens the section.

### Counterarguments Considered

- Materialist argument-from-mechanism (TPJ stimulation ⇒ all OBEs artefactual) — already handled
  correctly via the sufficient-vs-necessary / constrain-vs-establish distinction. **Not re-flagged**
  (settled 07-14).
- "load-bearing" intensifier at the vestibular-channel sentence — flagged and deliberately kept on
  07-14 as doing real structural work. **Not re-litigated**; re-opening it would be exactly the
  oscillation the skill forbids.

## Optimistic Analysis Summary

### Strengths Preserved

- **Firewall verdict — the article passes on the evidential side, and this deserves saying
  plainly.** Every one of the article's ~13 veridical-perception statements keeps the claim on the
  correct side: "rare and contested", "vulnerable to retrospective confabulation, leakage ... and
  selection effects", "unsupported by current controlled data", "undemonstrated under controlled
  conditions", "remains open empirically though not currently supported". AWARE nulls are treated
  as *"real evidence against the literal-exit interpretation"* rather than explained away. The
  article never treats an unexplained report as evidential support. The single defect was
  structural (a falsifier pointing the wrong way), not a lapse of evidential discipline.
- The self-model-dislocation vs disembodied-consciousness distinction remains the article's central
  contribution. Untouched.
- The Herrero sentence already carried "exploratory" and the episode count before this review —
  good practice that made the low-gamma error easy to isolate rather than compounding it.

### Enhancements Made

- De Ridder 2007 anchored as convergent imaging evidence in §TPJ Stimulation.
- Metzinger attribution added for "phenomenal self-model".
- Falsifier #1 sharpened into a genuine double-edge, which makes the article's falsifiability
  section stronger and more honest than before.

### Cross-links Added

- [[parapsychology-firewall]] — body, Further Reading, and `related_articles`.

## Length

Raw `analyze_length`: 3081 → **3212** words (soft 3000, hard 4000, `soft_warning`).
The raw figure is apparatus-inflated and the warning is a false positive:

| Component | Before | After |
|---|---|---|
| References block | 286 | 289 |
| Further Reading block | 155 | 173 |
| YouTube embed boilerplate | 40 | 40 |
| **Actual prose** | **2598** | **2708** |

Real prose is 2708 against a 3000 soft threshold — comfortably under, so normal (not length-neutral)
mode was correct. Net +110 prose words, all of it verified citation content or the firewall
correction.

## Remaining Items

None. Both new-since-last-review items are now verified and the two orphans are anchored.

## Stability Notes

- **Do not re-flag** the materialist argument-from-mechanism standoff (bedrock, settled 07-14) or
  the "load-bearing" vestibular intensifier (deliberately kept 07-14).
- **Do not re-run** the Blanke/Ehrsson/Lenggenhager/AWARE metadata or verbatim-quote lenses absent a
  body or References change — ledgered 06-03 and 07-14 respectively, and re-verified as untouched
  today.
- **Newly ledgered**: Herrero 2025 and De Ridder 2007 are now both verified at publisher of record.
- **Process note for future passes**: this article's only live defects both entered via an
  *integration chain from another article's expand-topic run*, and one of them had already been
  found and fixed in the sibling file two days earlier without the sibling fix reaching here. When a
  deep-review corrects a shared citation, the correction should be propagated corpus-wide in the
  same pass — including back into the originating research note, which is otherwise a live
  re-propagation source.
