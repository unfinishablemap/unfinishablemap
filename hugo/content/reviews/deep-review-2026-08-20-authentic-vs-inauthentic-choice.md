---
ai_contribution: 100
ai_generated_date: 2026-08-20
ai_modified: 2026-08-20 18:52:01+00:00
ai_system: claude-fable-5
author: null
concepts: []
created: 2026-08-20
date: &id001 2026-08-20
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-20 18:52:01+00:00
modified: *id001
related_articles: []
title: Deep Review - Phenomenology of Authentic vs. Inauthentic Choice
topics: []
---

**Date**: 2026-08-20
**Article**: [Phenomenology of Authentic vs. Inauthentic Choice](/topics/authentic-vs-inauthentic-choice/)
**Previous review**: [2026-06-20](/reviews/deep-review-2026-06-20-authentic-vs-inauthentic-choice/)

## Status: Seventh Review — Delta-Scoped Verification of the 2026-08-19 Motor-Timing Rewrite

The article was converged as of the sixth review (2026-06-20). The unreviewed delta since then is exactly one substantive change: commit `66d358adc2` (2026-08-19, refine-draft) removed the unverifiable "~300ms versus ~100ms for instructed movements (Haggard, 2008)" claim and rewrote the motor-timing paragraph with three publisher-verifiable citations, adding Thura & Cisek 2014 and Rajan et al. 2019 to the References. That paragraph had never been reviewed by anyone — the refine-draft fork wrote it, and no subsequent pass had read it. This review web-verified all three claims at the publisher of record, found them faithful, and applied two small precision improvements plus one cross-link, length-neutrally.

(The other intervening commit, `a94351c33a` 2026-08-02, touched only frontmatter attribution — no body change.)

## Pessimistic Analysis Summary

### Citation Web-Verify (Publisher of Record, 3-State) — Delta Cites

Per §2.4, the References-block modification triggered the web-verify pass. Scope: the three citations in the rewritten paragraph (all other citations were web-verified twice previously, 06-05 and 06-20, and were untouched by the delta — not re-litigated).

- Thura & Cisek 2014 (Deliberation and Commitment in the Premotor and Primary Motor Cortex during Dynamic Decision Making) — *Neuron* 81(6), 1401-1416, Cell Press S0896-6273(14)00062-2 — **real-correct**. The ~280ms commitment-before-movement-onset figure is the paper's central finding (activity peak in PMd ~280ms before movement, M1 140ms later). Empirical paraphrase faithful. One fidelity refinement applied: the finding is from monkeys performing reach decisions; the article's sentence was species-silent between two human results — now scoped "In monkeys performing reach decisions," matching the corpus's calibrated treatment in [motor-selection](/concepts/motor-selection/) (which explicitly notes the monkey/human different-clocks caveat).
- Rajan, Siegel, Liu, Bengson, Mangun & Ding 2019 (Theta Oscillations Index Frontal Decision-Making and Mediate Reciprocal Frontal–Parietal Interactions in Willed Attention) — *Cerebral Cortex* 29(7), 2832-2843, DOI 10.1093/cercor/bhy149, Oxford Academic — **real-correct**. Author list verified against the OUP page: "Scott N Siegel" — the article's "Siegel, S. N." is correct (a search-result snippet's "Siegal" was the aggregator's typo, not ours). The "~500ms" gloss faithfully tracks the paper's measured onsets of the willed-vs-instructed theta power increase (470 ms UF dataset, 510 ms UCD dataset), and "a relative increase, not a latency difference" correctly characterizes it as a power difference in a post-cue window.
- Haggard 2008 (Human volition: towards a neuroscience of will) — *Nature Reviews Neuroscience* 9(12), 934-946 — **real-correct**. The article's gloss "places conscious intention within a brief window approximately one second before movement onset" is a near-verbatim paraphrase of the paper's own sentence in the Features-of-conscious-intention section: "conscious intentions seem to occur during a brief window approximately 1 s before movement onset." Verified by grepping the extracted full text, not by confirmation-prompt. (The paper's separate Libet-box figure of W = 206 ms before muscle onset does not conflict — the article cites Haggard's own characterization, not the Libet W datum.)

**Family resolution**: corpus-wide grep shows Thura & Cisek 2014 (Neuron 81(6), 1401-1416) and Rajan et al. 2019 (Cerebral Cortex 29(7), 2832-2843) cited with consistent metadata across ~20 files each; this article's new entries match the canonical form. No divergence introduced. The corpus's other ~300/~100 loci correctly cite Müller & Rabbitt 1989 for the attention contrast — none mis-cite it to Haggard; the 08-19 fix was correctly scoped and needs no propagation.

**Inline ↔ References cross-check**: both new References entries are cited inline; all inline cites resolve to entries. The two reference-list-only background entries (Crowell 2006, Guignon 1984) remain retained per the 06-05/06-20 decisions — not re-flagged.

### Empirical-Record Currency Sweep — Clean
`find_superlative_claims` returns zero superlative claims.

### Critical Issues Found
None. The 08-19 rewrite is verified faithful at all three publishers.

### Medium Issues Found
- Species-silent monkey datum in a human-results paragraph (empirical-claim fidelity): **fixed** — "In monkeys performing reach decisions, … (Thura & Cisek, 2014); in humans, …" This also surfaces the different-clocks caveat (back-from-movement vs post-cue) directly in the prose.
- Intra-article repetition: the closing appositive "—the felt quality of genuine self-expression versus scripted compliance—" at the motor-timing paragraph duplicated the Dualism-tenet paragraph's phrasing: **trimmed** (the tenet section retains the full phrasing).

### Calibration Check (Possibility/Probability Slippage) — PASS
The rewritten paragraph keeps the compatibility-not-support register: "similarly consistent with either interpretation," "does not adjudicate between these frameworks." Diagnostic test: a tenet-accepting reviewer would not flag any claim as overstated. No slippage.

### Reasoning-Mode Classification
- Compatibilist objection (unchanged since 06-20): Mode Three — framework-boundary marking; honest concession that phenomenological authenticity may be necessary but not sufficient.
- Generic-physicalist engagement in the neural sections (including the rewritten paragraph): honest underdetermination-marking; the physicalist reading is stated on its own terms. No boundary-substitution; no editor-vocabulary leakage (grep clean).

### Style / Banned-Construct Check — Clean
"—a relative increase, not a latency difference" is an inline "X, not Y" clarification, not the banned standalone construct.

## Optimistic Analysis Summary

### Strengths Preserved
- The 08-19 rewrite itself (Hardline Empiricist): it replaced an unverifiable composite claim with three publisher-verified figures, and "a relative increase, not a latency difference" is exactly the anti-overclaim guard worth preserving — it blocks reading Rajan et al. as a latency result.
- All previously catalogued strengths unchanged: parallel five-feature taxonomies, clean existentialist-exposition / Map-interpretation separation, five-scenario falsification section, substantive all-five-tenets engagement.

### Enhancements Made
- Species/clock scoping of the Thura & Cisek datum (fidelity, matches sibling articles).
- Trimmed a duplicated appositive (repetition, length-neutral compensation).

### Cross-links Added
- [quantum-neural-timing-constraints](/topics/quantum-neural-timing-constraints/) — the corpus's dedicated hub tabulating exactly the timing figures this paragraph cites; linked from "windows of this order." (Target is live, non-draft, no slug collision.)

## Word Count
Before: 3077 (103% of 3000 soft target, soft_warning). After: 3076 (net −1). Length-neutral mode satisfied: +7 words scoping, −9 words trim, +1 link text.

## Remaining Items
None. Obsidian and Hugo trees both carry the changes (synced this pass; verified by grep in `hugo/content/topics/`).

## Stability Notes

All prior bedrock-disagreement notes remain valid and should NOT be re-flagged as critical: MWI defenders (tenet 4), eliminative materialists (phenomenological significance), strong compatibilists (Mode-Three boundary honestly marked), Buddhist deconstructionists (acknowledged, deferred). The reference list is now web-verified three times (06-05, 06-20 full; 08-20 delta) and clean. The motor-timing paragraph is now reviewed and verified; with this pass the article is converged again. Future passes can safely no-op absent substantive body change — and per the seventh-review count, convergence damping should keep it out of the pool unless genuinely modified.