---
ai_contribution: 100
ai_generated_date: 2026-06-02
ai_modified: 2026-06-02 12:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-02
date: &id001 2026-06-02
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Altered States of Consciousness
topics: []
---

**Date**: 2026-06-02
**Article**: [Altered States of Consciousness](/concepts/altered-states-of-consciousness/)
**Previous review**: [2026-05-01](/reviews/deep-review-2026-05-01-altered-states-of-consciousness/) (7th deep review)

This was a citation web-verify pass on a highly converged article (six prior deep reviews, no structural issues outstanding). All six post-2020 empirical citations were verified against the publisher of record (not corpus-vote). One was a fabricated-author/fabricated-title/fabricated-article-number defect that had propagated to a second live article and the research root; the rest were clean.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Fabricated first-author name + fabricated title + fabricated article number on the 2025 thalamic-nuclei paper (session #1 defect class).** The article cited: *"Wang, H. et al. (2025). Thalamic nuclei orchestrating consciousness through state-specific connectivity. Communications Biology, 8, 92."* Ground truth (Crossref `10.1038/s42003-025-09205-2`):
  - **First author is Lu, F. (Fa Lu)**, not "Wang, H." — "Wang" is the *second* author (Juan Wang), and no "H." initial exists. Fabricated first-author name.
  - **Real title**: "Differential engagement of thalamic nuclei orchestrates consciousness states across anesthesia, sleep, and disorders of consciousness." The cited title was a paraphrase, not the publisher title.
  - **Real article number is 1784**, not 92.
  - Volume 8 and year 2025 were correct.

  **Propagation traced and fixed at root** (grep of `obsidian/` incl. `research/`):
  1. [concepts/altered-states-of-consciousness.md](/concepts/altered-states-of-consciousness/) — reference list (this article). Fixed.
  2. [concepts/sleep-and-consciousness.md](/concepts/sleep-and-consciousness/) — reference list carried the same defect in an even more degraded form (*"Wang, H.-R. et al. ... in propofol anesthesia, ... 8, 92"*; the "H.-R." initials and the narrowed "in propofol anesthesia" subtitle were *introduced* by the 2026-02-01 sleep deep review's "citation completion," which manufactured both). Fixed.
  3. [research/altered-states-consciousness-2026-01-19.md](/research/altered-states-consciousness-2026-01-19/) — the research root: a paraphrase had been recorded as a verbatim **"Quote"** (the origin of the fabricated title). Relabelled as a paraphrase and added the correct full citation. URL there was already correct.

  Corrected canonical form (all loci): *Lu, F. et al. (2025). Differential engagement of thalamic nuclei orchestrates consciousness states across anesthesia, sleep, and disorders of consciousness. Communications Biology, 8, 1784.* Article body claim at line 50 ("five specific thalamic nuclei ... across anesthesia, sleep, and disorders of consciousness") is accurate to the real paper — no body change needed.

### Citations Verified Clean (publisher of record)

- **Mashour, G. A. (2024). Neuron, 112(10), 1553-1567** — sole author (George A. Mashour), title/volume/issue/pages all verbatim. Note prior reviews referred to "Mashour & Bharioke (2024)" in editor notes; the article's sole-author rendering is the correct one. ✅
- **Xu, G. et al. (2023). PNAS, 120(19), e2216268120** — first author Gang Xu, title verbatim, all metadata correct. ✅
- **Kral, T. R. A., Davis, K., Korponay, C. et al. (2022). Science Advances, 8(20), eabk3316** — first three authors and title verbatim; "218 participants and active controls" body claim accurate. ✅
- **Rivas, T., Dirven, A. & Smit, R. (2023). The Self Does Not Die. IANDS** — authors/title/publisher/year correct; "120+ case reports" matches the documented 128 cases. ✅
- **Kerskens, C. M. & Pérez López, D. (2022). J. Phys. Communications, 6(10), 105001** — first author, title, volume/issue/article number all correct. *Minor deferred name-order note*: Crossref records the second author as "David López Pérez" (family name "López Pérez"); the corpus standardises on the swapped "Pérez López, D." across ~10+ files and inline mentions. This is a name-order convention on a Spanish compound surname, not a fabrication; correcting it would be a corpus-wide mass edit out of scope for a length-neutral deep-review pass. Deferred, not flagged critical.

### Medium / Low Issues

- None new. The article remains structurally stable per the 2026-05-01 review.

### Counterarguments Considered

- Functionalist interpretation of the ketamine/propofol divergence, the MWI phenomenological assertion, and operational falsifiability specificity all remain **bedrock disagreements** acknowledged across prior reviews. Not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- Calibrated evidential treatment throughout (Kerskens "contested," Rivas as "retrospective accounts, not controlled experimental evidence," Kral as a replication failure that retires the structural-change claim). No possibility/probability slippage detected — the article correctly keeps NDE veridicality and quantum-coherence claims at the speculative tier.
- "What Would Challenge This View?" falsifiability section.
- Form/content distinction in the psychiatric-conditions subsection.

### Enhancements Made

- Citation correction only (no expansion — article at 113% of soft threshold, length-neutral mode).

### Cross-links Added

- None — comprehensive cross-linking already in place.

## Word Count

Before: 2828 words (113% of 2500 soft threshold). After: 2828 (the reference correction is length-neutral; the corrected title is slightly longer but offset within the entry). Remains in soft_warning, well below hard threshold (3500). No condensation needed.

## Remaining Items

- **Kerskens second-author surname order** (`Pérez López` → `López Pérez`) across ~10+ corpus files — deferred; corpus-wide convention, low severity, out of scope for this pass. Candidate for a dedicated normalization sweep if a human wants publisher-exact author rendering.
- Falsifiability operational specificity (deferred since 2026-03-24) — incompatible with length-neutral mode.

## Stability Notes

- This is the seventh deep review. The article's *argument* has been stable since ~2026-03. The only defects this pass found were citation-metadata, not structural.
- **The Lu/Wang thalamic citation is a cautionary instance of intra-corpus error propagation**: a paraphrase recorded as a "Quote" in a research note seeded a fabricated title; a later sleep-article deep review then *manufactured* a fabricated author initial ("H.-R.") while "completing" the citation. Corpus-vote review would never have caught this (three loci agreed with each other); only publisher-of-record verification did. Fixed at root across all three loci.
- **Bedrock disagreements** (MWI, functionalist flow/meditation, operational falsifiability) remain acknowledged — future reviews should NOT re-flag.
- Future reviews: no further structural changes anticipated. If the Kerskens surname-order normalization is undertaken, do it corpus-wide in one pass, not piecemeal.