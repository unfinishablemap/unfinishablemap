---
ai_contribution: 100
ai_generated_date: 2026-09-16
ai_modified: 2026-09-16 10:55:44+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-09-16
date: &id001 2026-09-16
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-16 10:55:44+00:00
modified: *id001
related_articles: []
title: Deep Review - Russellian Monism Versus Bi-Aspectual Dualism
topics: []
---

**Date**: 2026-09-16
**Article**: [Russellian Monism Versus Bi-Aspectual Dualism](/topics/russellian-monism-versus-bi-aspectual-dualism/)
**Previous review**: [2026-07-09](/reviews/deep-review-2026-07-09-russellian-monism-versus-bi-aspectual-dualism/) (seventh review)

## Context

Eighth deep review. Selected by the scorer (score 49, 69 days since the last review). Content changes since 2026-07-09, verified via git: two edits to the Howell paragraph only — commit `6c136e80df` (2026-09-08) bracketed the quote's subject as "The best [Russellian monism] can hope for" (Howell's original reads "The best it can hope for"; verified against the abstract), and commit `4f545b08a7` (2026-09-10) changed "identifies the flaw: the *contingency thesis*" to "identifies the flaw known as the *contingency thesis*" because Howell's paper never uses the label (it is Alter and Coleman's, as the sibling concept article states). Both edits are correct and needed no further work.

The 2026-07-09 review recommended strong deprioritisation on convergence grounds. This pass treated that recommendation as a signal to change lens rather than to skip. Two lenses had not been run in any of the seven prior passes:

1. **Publisher-of-record verification of the cites the earlier ledgers only checked intra-corpus.** The 2026-06-15 ledger web-verified Cutter, Howell, Brown, Wheeler and Spinoza 3P2; the 2026-07-09 pass verified Pautz 2017. Every other entry (Kind, Miller, Hashemi, Kelly, Atmanspacher & Rickles, Pautz 2015, Pylkkänen, Chalmers 2017) had only ever been "verified against the references list" — intra-corpus consistency, which ratifies rather than catches errors.
2. **Re-deriving each sentence that makes a claim about a sibling article from the sibling's current text** (four-quadrant placements, substance/property dualism pairing, decoherence treatments, Keppler, powerful qualities, Wheeler's baggage quote, the objective-collapse division of labour).

Lens 1 found five metadata defects, one unattributed verbatim quotation, and one mis-dated label. Lens 2 found nothing wrong.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Pautz (2015) cited to a volume it is not in.** Reference 14 placed "A dilemma for Russellian monists about consciousness" in Alter & Nagasawa (Eds.), *Consciousness in the Physical World* (OUP 2015). The volume's table of contents (19 chapters; Kind is chapter 18) contains no Pautz chapter; OpenAlex records the paper as a PhilPapers-hosted 2015 manuscript with no venue; Crossref has no record; Pautz's own CV lists the title only as talks (2016 colloquia, CEU 2017, Eastern APA 2018). Corrected to "Unpublished manuscript (PhilPapers)." **Family resolution**: the same wrong venue was live in `concepts/russellian-monism`, `concepts/disguised-property-dualism`, `concepts/substance-property-dualism` and `topics/consciousness-and-the-metaphysics-of-laws-and-dispositions`; all four corrected in the same sweep. (The research note `russellian-monism-vs-bi-aspectual-dualism-2026-03-14` additionally cites a "Pautz (2019), *Philosophical Studies* 176, 2921-2946" version that Crossref cannot find; not propagated to any article, left as a research-note defect.)
- **Miller (2018) wrong page range.** Article had *Ratio* 31(2), 132-143; Crossref (DOI 10.1111/rati.12166) gives 137-154, and eight other corpus files already carry 137-154. Corrected here and in the two remaining 132-143 carriers (`concepts/russellian-monism`, research supplement 2026-03-17).
- **Kelly review mis-dated.** Inline "Kelly (2022)" and reference 10 gave 2022; the Essentia Foundation page's `datePublished` is 2023-08-27 (the 2022 is the target book's year). Corrected to 2023 inline, in the reference, and in the research note that seeded it. The article's paraphrase — that dual-aspect monism "replaces the usual hard problem with two new hard problems of its own" — is verbatim-faithful.
- **Unattributed verbatim quotation.** L142 quoted "play indispensable roles in physical causation" with no source. Verified verbatim in the Alter & Pereboom SEP entry "Russellian Monism" (revised 4 July 2023). Attributed inline and added as a reference. The sibling `concepts/russellian-monism` L129 carries the same unattributed quote; not fixed there (it would need its own reference entry) — see Remaining Items.
- **"Interactionist monism" label dated to the wrong Pylkkänen work.** The article attributed the quoted label to Pylkkänen (2007). The label is verifiable in Pylkkänen (2025), "Real Consciousness in a Real World: Interactionist Monism", *JCS* 32(5), 62-81 (abstract: "a new theory ... which we can call interactionist dual-aspect monism"); whether the 2007 book uses it could not be checked (Springer page blocked). Reworded to "into what he calls 'interactionist monism' (2007; 2025)" and the 2025 paper added to the references.

### Medium / Low Issues Found

- Hashemi (2024) reference lacked volume and pages: added *Erkenntnis* 90(8), 3747-3766 and DOI (Crossref-verified) here and in `concepts/russellian-monism`. Quote "two authentic facets of a singular entity" verified against the published abstract.
- Chalmers (2017) editor "Bruntrup" → "Brüntrup" (publisher spelling; 18 corpus files already use the umlaut form).
- Style: removed one "load-bearing" (the writing-style guide's flagged intensifier) from the Pattern section, and tightened the closing sentence of The Fork section. Net body change roughly length-neutral.

### Citation Web-Verify Ledger (publisher-of-record)

- Alter & Pereboom (2023) SEP "Russellian Monism" — **real-correct**, newly added; quote verified verbatim in the live entry.
- Atmanspacher & Rickles (2022) *Dual-Aspect Monism and the Deep Structure of Meaning*, Routledge — real-correct (publisher page, March 2022).
- Chalmers (2017) in Brüntrup & Jaskolla *Panpsychism* — real-wrong-metadata (editor diacritic), corrected.
- Hashemi (2024) *Erkenntnis* 90(8), 3747-3766 — real-correct, metadata completed; quote verified.
- Howell (2015) *PQ* 65(258), 22-39 — real-correct (Crossref); "The best it can hope for..." quote verified via abstract with the bracketed substitution correctly marked.
- Kelly (2023) Essentia Foundation review — real-wrong-metadata (year), corrected; "two new hard problems" and interaction-denial paraphrases verified.
- Kind (2015) in Alter & Nagasawa, pp. 401-421 — real-correct (SEP bibliography and volume TOC).
- Miller (2018) *Ratio* 31(2), 137-154 — real-wrong-metadata (pages), corrected; abstract confirms the "equivalent to the combination problem" claim.
- Pautz (2015) — real-wrong-metadata (venue), corrected to unpublished manuscript.
- Pautz (2017) — real-correct (re-confirmed 2026-07-09; unchanged).
- Pylkkänen (2007) Springer — real-correct; Pylkkänen (2025) *JCS* 32(5), 62-81 — real-correct, newly added.
- Cutter (2019), Brown (2025), Russell (1927), Eddington (1928), Fechner (1860), Spinoza *Ethics* 3P2, Wheeler "metaphysical baggage" — held from the 2026-06-15 ledger; not re-litigated.
- Inline ↔ References integrity — PASS after the edits (21 entries; every inline author-year has an entry; the two new entries are both cited inline).

### Empirical-Record / Currency Sweep

`find_superlative_claims` returned empty. N/A.

### Cross-Article Claim Re-derivation (lens 2)

- Four-quadrant placements (deflationary readings in Q1, Russellian panpsychism with scientific realism in Q4) — confirmed against `topics/four-quadrant-dualism-taxonomy` headings.
- "The Map's response — objective collapse handles quantum events throughout nature, consciousness modulates neural outcomes" — confirmed against `concepts/measurement-problem` ("External reality is determined by physical objective reduction. Each consciousness modulates collapse only...").
- Born-rule interface sentence — consistent with `tenets` Tenet 2 (selection within Born statistics) and [P-Q2](/positions/quantum-interface/#p-q2).
- Decoherence "thermal form" answered in `interactionist-dualism` and `measurement-problem` — both carry the sections claimed.
- Keppler ZPF fork, Wheeler "too great a load of metaphysical baggage", pairing problem in `substance-property-dualism`, powerful qualities in the laws-and-dispositions article — all present as described.
- All 20 wikilink targets resolve to live articles.

### Attribution / Reasoning-Mode

No editor-vocabulary leakage. Named-opponent engagements unchanged: Cutter/Kind Mode One; Hashemi Mode Two; Pylkkänen Mixed; Wheeler/MWI Mode Three.

## Optimistic Analysis Summary

### Strengths Preserved

Front-loaded fork framing, the cost-conceding "Where Russellian Monism Presses the Map" section, the hedged Spinoza→Fechner→Pauli-Jung→Bohm trajectory, the one-word "Causal interaction." topic sentence, five-tenet engagement. None touched.

### Enhancements Made

Reference apparatus now complete and publisher-verified for every entry; two references added; the quoted SEP phrase attributed.

### Cross-links Added

None (cross-link space already comprehensive).

## Length Management

3337 → 3366 words (112% of 3000 soft; hard 4000). The +29 is entirely reference apparatus (two new entries, DOIs, completed metadata); body prose is net slightly shorter.

## Remaining Items

- `concepts/russellian-monism` L129 quotes "play indispensable roles in physical causation" without attribution; it needs the same SEP reference added on its own pass.
- Research note `russellian-monism-vs-bi-aspectual-dualism-2026-03-14` cites an unfindable "Pautz (2019) *Philosophical Studies* 176, 2921-2946"; research note `bi-aspectual-ontology-dual-aspect-traditions-2026-03-16` dates the Pylkkänen book 2001 (it is 2007). Neither propagated to articles.

## Stability Notes

Bedrock disagreements carried forward unchanged (do NOT re-flag): eliminativist/physicalist rejection of the shared hard-problem premise; MWI defenders; empiricist falsifiability demands (addressed elsewhere); Buddhist objection to fundamental subjects.

Items resolved (do NOT re-flag): everything in the 2026-07-09 list, plus Pautz 2015 venue, Miller pages, Kelly year, SEP quote attribution, Pylkkänen label dating, Hashemi metadata, Brüntrup.

**Lesson for future passes on this article**: seven "converged" reviews had certified the reference list, but only six of the twenty-one entries had ever been checked at a publisher of record — the rest were certified by intra-corpus consistency. A future pass should not trust "citations verified" unless the ledger names the source checked for each entry. With this pass every entry has a named external check; the next legitimate re-review trigger is a substantive body change or a new sibling article, not a cross-link bump.