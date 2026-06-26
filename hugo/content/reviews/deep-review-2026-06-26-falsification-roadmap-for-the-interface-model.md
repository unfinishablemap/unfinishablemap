---
ai_contribution: 100
ai_generated_date: 2026-06-26
ai_modified: 2026-06-26 14:38:28+00:00
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
title: Deep Review - Falsification Roadmap for the Interface Model
topics: []
---

**Date**: 2026-06-26
**Article**: [Falsification Roadmap for the Interface Model](/topics/falsification-roadmap-for-the-interface-model/)
**Previous review**: [2026-06-02 (ninth review)](/reviews/deep-review-2026-06-02-falsification-roadmap-for-the-interface-model/)

## Drift-Axis Self-Select Rationale

The candidate scorer's top pick (`consciousness-and-the-normativity-of-reason`, score 15) and the first drift-axis probe (`neural-refresh-rates-and-the-smoothness-problem`) were both rejected as converged no-op targets:
- **normativity-of-reason** — 6 prior deep reviews; the 2026-06-05 (6th) pass did a full bidirectional publisher-of-record citation audit (fixed Crane→Pernu), explicitly recommended "continued exclusion from routine rotation absent substantive new content." Its score-15 re-qualification traces to commit c3559335f (2026-06-20), a *cosmetic* NORM↔CM cross-link install — the no-op re-trigger the convergence-damping rule guards against.
- **neural-refresh-rates** — deep-reviewed *yesterday* (2026-06-25, its 7th pass; review file named `deep-review-2026-06-25-neural-refresh-rates.md`, a near-miss slug that the candidate scorer's damping and a naive `deep-review-*-{slug}.md` glob both undercount). Fully converged, "should not draw a fresh deep-review again."

Self-selected `falsification-roadmap-for-the-interface-model` instead: genuine drift (ai_modified 2026-06-24 vs last_deep_review 2026-06-02, ~22d gap), older-model build (claude-opus-4-6), citation-bearing, and — decisively — its **Kerskens citation surname was re-canonicalized by a corpus sweep (commit 11c8554f5) AFTER its last review**, so the post-review change was unverified at the publisher of record. Body 3980→3985 words (133% of 3000 soft; under the 4000 hard ceiling), confirming cross-link/citation accretion was nudging it toward the ceiling.

## Pessimistic Analysis Summary

### Critical Issues Found
- **None.** Tenth review; long-converged at the framework boundary. The two edits below are should-fix maintenance, not critical defects.

### Should-Fix Issues Addressed
1. **References archival-rot (Ref 8) — FIXED.** Ref 8 cited *"The Interface Specification Problem"* at `https://unfinishablemap.org/topics/the-interface-specification-problem/`. That article is **archived** (`archive/topics/the-interface-specification-problem.md`) and its URL **301-redirects** to the live successor `/topics/the-interface-problem/` ("The Interface Problem: Location and Specification"). The prose-URL self-citation was pointing at a redirect source (the archival_link_rot + check-slug-misses-archive-redirect-collisions pattern). The body already wikilinks the live `[[the-interface-problem]]` correctly; only the reference-list URL was stale. **Resolution**: repointed Ref 8 to the live successor URL + title + date (2026-05-01, the successor's ai_generated_date), byline numeral corrected six→sept to match the opus-4-7-era regeneration date (point-in-time stamp convention, confirmed against Ref 9 invertebrate / Ref 10 born-rule).
2. **Melloni 2025 incomplete citation (Ref 7) — COMPLETED.** Ref 7 read "*Nature*." with no volume/pages/date; the date was deferred "for human verification" across prior reviews (06-02 Remaining Item). Web-verified at publisher of record and completed.

### Citation Web-Verification (publisher of record)

Per-cite ledger for citations changed-since-review or previously-deferred (the load-bearing set was fully verified clean on 2026-06-02 and is not re-spent this run):

- **Kerskens & López Pérez (2022)** (line 167; "Experimental indications of non-classical brain functions", *J. Phys. Commun.* 6, 105001) — state: **real-correct (compound surname now canonical)**. The 2026-06-02 review verified the paper as "Kerskens & Pérez"; the corpus sweep (commit 11c8554f5, "Pérez, D. L." → "López Pérez, D.", 21 files) ran *after* that review. WebSearch of the IOPscience publisher of record (DOI 10.1088/2399-6528/ac94be) confirms the second author is **David López Pérez** — the compound surname is the correct canonical form, so the post-review sweep was right and the current body text needs no change. This closes the verification gap created by an after-review corpus edit; it is the exact ai_citation_metadata_unreliable compound-surname trap, here resolving in favour of the sweep.
- **Melloni et al. (2025)** (Ref 7) — state: **real-wrong-metadata (incomplete → completed)**. Web-verified at nature.com/articles/s41586-025-08888-1: *Nature* **642**(8066), 133–142, published **5 June 2025**, DOI 10.1038/s41586-025-08888-1. Completed the reference. (256 participants; fMRI/MEG/iEEG; preregistered IIT-vs-GNWT adversarial collaboration — the article's body characterization is accurate.)
- **arXiv:2512.02838** (Horchani, "Experimental Blueprint for Distinguishing Decoherence from Objective Collapse") — state: **real-correct**. Verified real on 2026-06-02; unchanged; not re-spent.
- **Donadi et al. (2021)** *Nature Physics* 17, 74–78; **Maier, Dechamps & Pflitsch (2018)** *Frontiers in Psychology* 9, 379 (NULL stance); **Deutsch (1985)** *Proc. R. Soc. A* 400, 97–117; **Hameroff (2020)**, **Hameroff & Penrose (2014)**, **Pitts (2020)**, **Kleiner (2021)** — all web-verified clean on 2026-06-02; unchanged this cycle; per-cite ledger inherited.

### Empirical-Record Currency Sweep
- `find_superlative_claims` returns only "so far" (Tenet 1 honest assessment: "best available... so far") — a rhetorical hedge, not an empirical-record superlative. No currency action. The Hameroff "most complete, most easily falsifiable theory of consciousness" claim is correctly attributed as Hameroff's *own* characterization (Ref 3 title), not asserted by the Map. No superseded superlatives.

### Attribution / Qualifier / Position-Strength / Source-Map / Self-Contradiction
- PASS on all five. Body prose unchanged from the 2026-06-02 converged state. Kleiner structural-falsification problem honestly conceded "not specific to the Map"; Hameroff Orch-OR claims framed as proponent self-assessment with "Independent assessment of these claims remains limited"; Pitts conservation-of-energy challenge engaged on its own terms; the Tenet-2 mechanism-family split keeps the corridor/trumping readings' weaker falsifiability from being silently exported from the mechanism-committed rows' traction.

### Reasoning-Mode Classification (named-opponent engagements; editor-internal)
- **Pitts (2020)** conservation-of-energy / causal closure (§Tenet 3): **Mode Two** — presses the standard quantum-interactionist selection-among-energetically-equivalent-outcomes move, which conservation laws read locally leave open. Honest; unchanged.
- **Kleiner (2021)** structural falsification (§Structural Falsification Problem): **Mode Three** — honest boundary-marking ("not specific to the Map... does not excuse failing to specify"). Unchanged.
- **Lakatosian critic** (§Tenet 2 honest assessment): **Mode Three** — "acknowledge the worry directly rather than rebut it." Honest boundary-marking, no substitution. Unchanged.
- No boundary-substitution; no editor-vocabulary label leakage in prose (grep-confirmed).

### Calibration Check (load-bearing)
- PASS. No possibility/probability slippage. A falsification *roadmap* proposes refutation conditions; it does not treat tenet-coherence as evidence. The Tenet-2 split *down*-calibrates the strict-corridor / trumping rows ("not Popper-refutable", "empirically indistinguishable from epiphenomenalism on Born-rule data alone"). Diagnostic test: a tenet-accepting reviewer would not flag any claim as overstated relative to the five-tier scale. The 06-02 causal-closure / underdetermination softening at Tenets 1/3/4 is preserved, not re-strengthened.

## Optimistic Analysis Summary

### Strengths Preserved
- The "Honest assessment" subsection pattern (ten reviews); the falsification-asymmetry table with the within-Tenet-2 mechanism-family decomposition (the article's strongest feature); the deflationary, calibration-first register throughout; the brain-internal-born-rule-testing reciprocity subsection.

### Enhancements Made
- Two reference-maintenance fixes (Ref 7 completion, Ref 8 archival-rot repoint). No body-prose change; no calibration content cut (per the 06-02 review's explicit instruction not to resolve length by cutting calibration language).

### Cross-links Added
- None. All wikilinks resolve; the body's `[[the-interface-problem]]` already points to the live successor (only the reference-list URL was stale).

## Length Check
- Body 3985 words (133% of 3000 soft; 15 words under the 4000 hard ceiling). soft_warning, not over hard. The Melloni completion added ~5 words; the Ref 8 repoint was net-neutral. Operated length-neutral in spirit — no body prose added. **Watch**: continued related_articles / Further Reading accretion (now 21 related + 13 Further Reading entries) is the drift vector pushing this article toward the ceiling. If body content ever breaches 4000, this is a methodology/calibration article whose framing language is load-bearing — flag for a human length-decision; do NOT auto-condense the Tenet-2 split or calibration content.

## Remaining Items
- **Babcock-Hameroff 2025** table cell (line 145): still a defensible table-characterization (the 2025 *Neuroscience of Consciousness* niaf011 paper), not a formal reference. Could be pinned if the table is ever promoted to formal refs; low priority, carried.

## Stability Notes

Tenth review. The article is long-converged on structure, voice, argumentation, calibration, and (now) citation canon including the after-review Kerskens compound-surname re-canonicalization, which this pass verified at the publisher of record.

Future reviews should NOT re-flag:
- **Kerskens & López Pérez (2022)** compound surname — web-verified canonical at IOPscience this pass; the older "Kerskens & Pérez" form is the pre-sweep version and must NOT be reintroduced.
- **Melloni et al. (2025)** metadata — *Nature* 642(8066):133–142, 5 Jun 2025, doi:10.1038/s41586-025-08888-1; verified this pass, closes the long-deferred date item.
- **Ref 8 → the-interface-problem** repoint — the specification-problem URL is an archived 301 redirect source; do not revert toward it.
- The Tenet-2 mechanism-family split, the brain-internal-born-rule-testing subsection, and the causal-closure / underdetermination softening — calibrated core (06-02), not unfalsifiability evasion or hedging-into-mush.

Bedrock disagreements (not fixable; do NOT flag as critical):
- Dualism lacks direct falsification (framework commitment, cumulative-only by the article's own table); Tenet 5 is epistemological, not scientific; MWI rejection is primarily philosophical; the interface-specification problem is unsolved. All conceded honestly in-article; framework-boundary standoffs, not defects.

**Convergence recommendation**: Stable at ten reviews. Should not draw a fresh deep-review unless its *body* (not related_articles / Further Reading) is substantively modified, or a new empirical development supersedes a load-bearing citation. The recurring re-qualification driver for this article is link-list accretion bumping `ai_modified`, not content drift.