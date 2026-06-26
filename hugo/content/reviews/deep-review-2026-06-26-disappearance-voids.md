---
ai_contribution: 100
ai_generated_date: 2026-06-26
ai_modified: 2026-06-26 13:35:25+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-26
date: &id001 2026-06-26
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: 'Deep Review - The Disappearance Voids: Absorption, Habituation, and Fatigue
  (Citation Family-Resolution)'
topics: []
---

**Date**: 2026-06-26
**Article**: [The Disappearance Voids: Absorption, Habituation, and Fatigue](/voids/disappearance-voids/)
**Previous reviews**: [2026-05-31](/reviews/deep-review-2026-05-31-disappearance-voids/), [2026-04-17](/reviews/deep-review-2026-04-17-disappearance-voids/), [2026-04-09](/reviews/deep-review-2026-04-09-disappearance-voids/)
**Trigger**: Queued staleness deep-review (~26 days). Fourth pass on a converged article. Standing CITATION web-verify + CALIBRATION + archival-rot pass.

## Convergence Status

Four reviews. The argument and structure are settled (no critical issues across the prior three). This pass was a maintenance audit. Per the steering, I scrutinised rather than assumed no-op — and that scrutiny found one real attribution defect that survived all three prior reviews (see below). Bedrock disagreements logged previously were NOT re-flagged.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Wrong-author + truncated-title citation defect (CRITICAL — attribution error), FIXED**: Reference 5 read `Sparby, T. (2024). "Toward a Unified Account of Advanced Concentrative Absorption Meditation." *Mindfulness*.` The paper is co-authored — **Sparby, T. & Sacchet, M. D.** — and the title is truncated (missing the subtitle ": A Systematic Definition and Classification of Jhāna"); the entry also lacked volume/pages. Publisher-of-record verified: *Mindfulness* (2024), **15, 1375-1394**, DOI 10.1007/s12671-024-02367-w (Springer link confirmed; second search confirmed both authors and vol/pages). 3-state classification: **real-wrong-metadata → fix, do not de-cite.** **Resolution**: corrected to `Sparby, T. & Sacchet, M. D. (2024). "Toward a Unified Account of Advanced Concentrative Absorption Meditation: A Systematic Definition and Classification of Jhāna." *Mindfulness*, 15, 1375-1394.`

  *Why it survived three reviews*: the 2026-05-31 pass flagged this exact entry as "the weakest-anchored references-only entry" but classified it only as an orphaned-reference nit — it never web-verified the metadata, so the dropped co-author and truncated title were missed. Intra-corpus consistency could not catch it (the corpus's *other* Sparby/Sacchet cites are different papers — the 2025 NeuroImage Yang et al. and the 2025 Chowdhury et al. — both already carry full author vectors, so this 2024 paper was the lone outlier with no cross-check). Only the live publisher caught it.

### Family Resolution (propagated)
- The same defective `Sparby, T. (2024)` "Unified Account" form (single-author, truncated) also appeared in the live research note `obsidian/research/voids-absorption-void-2026-02-22.md` (L207). **Propagated the canonical form there.**
- It also appears in `archive/voids/absorption-void.md` (L111, the frozen coalesce source). Left untouched — archives are historical snapshots; the archive notice already redirects readers to this live article, which now carries the corrected cite.

### Medium / Low
- **Menon (2023)** — real-correct, but the References entry lacks volume/issue/pages (verified: *Neuron* 111(16), 16 Aug 2023). Incomplete, not wrong; not fixed this pass (no defect, only optional completeness). Logged for awareness.
- Orphaned-reference nit (several References lack inline name-attribution) — carried from the 2026-05-31 review, still below the action threshold; the sources are all real and verifiable. No queue churn generated.

### Counterarguments Considered
- Eliminative-materialist objection (functional/phenomenal dissociation does not *require* dualism) — bedrock, NOT re-flagged.
- Physicalist reframing of flow "peak experience" — bedrock, NOT re-flagged.

## Citation Web-Verify Ledger (publisher of record, this pass)

- Sparby & Sacchet 2024 (Toward a Unified Account of ACAM) — **real-wrong-metadata** (was single-author "Sparby, T." with truncated title; corrected to two-author, full title, *Mindfulness* 15:1375-1394 per Springer DOI 10.1007/s12671-024-02367-w)
- Ciocan 2025 (Phenomenology of Fatigue) — real-correct (*Phenomenology and the Cognitive Sciences*, Springer DOI 10.1007/s11097-025-10115-1; exact title incl. subtitle verified)
- Killgore 2010 (Effects of Sleep Deprivation on Cognition) — real-correct (*Progress in Brain Research* 185, 105-129 — exact)
- Menon 2023 (20 years of the default mode network) — real-correct (*Neuron* 111(16), Aug 2023; entry could add vol/issue/pages — optional)
- James 1890 quote ("A thing may be present to a man a hundred times…") — real-correct, verbatim, correctly attributed to *Principles of Psychology* (psychclassics, Ch. 11)
- Singer & Klimecki 2014, Montupil et al. 2023, Csikszentmihalyi 1990 — fully verified in the 2026-05-31 pass; not re-litigated (References block unchanged for these).
- No superlative empirical claims detected (empirical-currency helper returned empty) — no currency sweep required.

## Calibration Analysis (Void Article)

No change from the converged 2026-05-31 finding. Re-applied the diagnostic test (would a tenet-accepting reviewer flag any claim as overstated relative to the five-tier scale?): **no**.
- "Why the Void is Structural" — four genuine evidence lines, hedged verbs ("support," "suggesting"). No slippage.
- Classification section — honest Unexplored/Unexplorable/Potentially-occluded partition with consistent "may/appears" hedges.
- Relation to Site Perspective — "gains support from"/"supporting the claim that"; dissociation offered as *support* for dualism, framework-boundary disagreement left standing. No possibility/probability slippage.
- Anti-mush: framework-boundary concessions preserved (Dreyfus-Zahavi unresolved; minimal-self-awareness caveat). No over-hedging introduced.

## Mechanical Checks
- EOF tool-tag scan: clean (no `</content></invoke>` artifact).
- Duplicate frontmatter keys: none.
- All 29 wikilinks (frontmatter + inline) resolve to live pages — no archival rot. (The `conscious-vs-unconscious-processing` link correctly targets the live concept; the archive copy's `superseded_by` points to the same live slug.)
- Tenet sub-anchors canonical: `^dualism`, `^bidirectional-interaction`, `^occams-limits` (not truncated).
- No "This is not X. It is Y." cliché; no memory-slug/editor wikilinks.

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded opening summary (untouched).
- Three-mechanism architecture (intensity / repetition / depletion).
- "Comfort of narrowing" insight; Levinas *il y a* reading of fatigue; Singer empathy/compassion dissociation; anesthesia three-states integration.

### Enhancements Made
- None to body prose. Only the corrected Sparby & Sacchet citation metadata (References) + family-resolution propagation to the research note.

## Length Management
- Before: 2669 words. After: 2682 words (+13, entirely from the expanded Sparby citation metadata in References). Body prose unchanged — length-neutral. 134% of 2000 soft threshold, acceptable for this coalesced three-void article with three separate literatures (carried verdict).

## Remaining Items
None requiring action. Optional (non-blocking): add Menon vol/issue/pages on a future condense/refine.

## Stability Notes
- Eliminative-materialist and physicalist objections remain **bedrock** at the framework boundary — future reviews must NOT re-flag as critical.
- Length above soft threshold (134%) is acceptable (carried).
- Anesthesia three-states treatment settled — do not flip its citations.
- Csikszentmihalyi case count is calibrated to "thousands" — do not re-introduce a specific number without a primary-source page reference.
- The Sparby (2024) "Unified Account" cite is now canonical (Sparby & Sacchet, full title, vol/pages). If it reappears elsewhere in a single-author/truncated form, fix to this form. The frozen `archive/voids/absorption-void.md` copy was intentionally left in the old form.
- Four reviews; converged. The metadata defect found here shows even converged citation-bearing articles benefit from a publisher-of-record pass — but a longer re-review interval remains advisable to avoid pure metadata churn between substantive changes.