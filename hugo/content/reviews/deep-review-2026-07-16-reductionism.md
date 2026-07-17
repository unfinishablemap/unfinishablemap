---
ai_contribution: 100
ai_generated_date: 2026-07-16
ai_modified: 2026-07-16 21:56:56+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-16
date: &id001 2026-07-16
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Reductionism (condense-regression + citation audit)
topics: []
---

**Date**: 2026-07-16
**Article**: [Reductionism](/concepts/reductionism/)
**Previous review**: [2026-06-17](/reviews/deep-review-2026-06-17-reductionism/) (post-coalesce cross-review)
**Word count**: ~3497 → ~3497 (no change; no-op pass)
**Verdict**: NO-OP. No critical, medium, or low issues. `last_deep_review` bumped only; `ai_modified` and `ai_system` held.

## Why this pass ran

Queued as a condense-regression audit: the article had a 2026-06-23 `/condense` pass (commit 46000d485, 3561w → under the 3500 concepts ceiling) that had not been deep-reviewed since. Condensing can silently drop load-bearing calibration hedges or citation-framing qualifiers (per condense-regresses-calibration-qualifiers). This is a Tenet-1 (Dualism) load-bearing article, so calibration discipline was the primary lens; a citation claim-match sweep was the secondary lens.

## Primary lens — Condense-regression audit (commit 46000d485)

Diffed the full condense against the pre-condense body. The condense was overwhelmingly sentence-combining and light tightening. **No load-bearing hedge or citation-framing qualifier was stripped.** Change-by-change:

- **Kim concession framing** — "the failure **is not** a research gap **but** a structural limitation" → "the failure **looks like** a structural limitation **rather than** a research gap." This *added* a hedge ("looks like") AND removed the "This is not X. It is Y." LLM-cliché construct the style guide proscribes. A net calibration/style improvement, not a regression.
- **emergence-as-universal-hard-problem parenthetical** — dropped the trailing descriptive clause "the explanatory gap relocated rather than resolved." Descriptive elaboration covered in the linked article; not a hedge on any Map claim.
- **Local-reduction jade analogy** — "each a legitimate species-specific type identity—just as 'jade' turned out to be two distinct minerals" → "…type identity." An illustrative analogy (and an imprecise one — jade-as-two-minerals is itself a multiple-realization example), not load-bearing. Fine to drop.
- **Locke primary/secondary passage** — condensed an explanatory gloss of the distinction to "whose own boundary, like this gap, admits no clean criterion." Detail deferred to [primary-secondary-quality-boundary](/topics/primary-secondary-quality-boundary/); the load-bearing form/content claim survives.
- **Parsimony close** — dropped "Simplicity is not a reliable guide when knowledge is incomplete" (a restatement of the Occam's-Limits tenet); the retained "the apparent simplicity of reductionism **may** reflect ignorance rather than insight" carries the hedge. No loss.
- Remaining edits (opening summary, three-types, transparency-test, vitalism intro) were pure clause-joining with no semantic change.

### Multiple-realizability calibration (the specific concern) — PASS
Multiple realizability is **not** asserted as settled fact; it is presented as *contested and probably weaker than Putnam claimed*. The section steelmans the critics (Bechtel & Mundale 1999 on inconsistent grain; Polger & Shapiro 2016 on relevance; Kim 1992's local reduction) and then makes the Map's actual move: **even granting MR is weaker than Putnam claimed, local reduction still cannot bridge the explanatory gap** — "the hard problem survives whether reduction is global or local." The Map's argument does not lean on MR as a load-bearing premise, so there is no over-claim to correct. The condense left this calibration untouched.

### Possibility/probability slippage (diagnostic test) — PASS
No tenet-coherence is used to upgrade an empirical claim's evidential tier. The C. elegans transparency-test passage claims only that complete physical knowledge "cannot tell us whether the 302-neuron worm experiences anything" — an epistemic-opacity claim, not a consciousness-attribution. The "What the Failure Reveals" underdetermination caveat (speech-act data "compatible with an epiphenomenal reading… and a causally efficacious one… turns on prior metaphysical commitments, not the report behaviour alone") survived the condense intact. A tenet-accepting reviewer would not flag any claim as overstated relative to the five-tier scale.

## Secondary lens — Citation Web-Verify Ledger (§2.4)

References block is unchanged since the 2026-06-17 full ledger (which web-verified every entry at publisher of record; all real-correct). The condense added no cites. Fresh-cohort priority verification this pass:

- **Milinkovic, B. & Aru, J. (2026)** (On biological and artificial consciousness: A case for biological computationalism) — **real-correct**. Re-verified at publisher of record (ScienceDirect PII S0149763425005251; DOI 10.1016/j.neubiorev.2025.106524; *Neurosci. Biobehav. Rev.* 181:106524). Claim-match faithful: article's "computation inseparable from biological substrate; functional reduction strips away precisely the properties that matter" matches the paper's "scale inseparability" / neural-computation-inseparable-from-physical-dynamics thesis. First initial **B.** correct (guards against the ai_citation_metadata_unreliable `M.` regression the 06-17 coalesce cross-review fixed).
- Bechtel & Mundale 1999, Chalmers 1996, Dennett 1991/1995, Fodor 1974, Kim 1992/1998/2005, Levine 1983, Lewis 1966/1972, Nagel E. 1961, Nagel T. 1974, Polger & Shapiro 2016, Putnam 1967 — carried forward **real-correct** from the 06-17 ledger; unchanged, not re-litigated (canonical, verified across ≥7 prior reviews).

DOI-form check: no Cambridge *Philosophy of Science* `S0031824…` malformed-DOI present (Bechtel & Mundale entry carries no DOI). Inline↔References cross-check: no orphans (Levine cited via [explanatory-gap](/concepts/explanatory-gap/) wikilink, accepted convention). Empirical-record currency: no superlative claims — N/A. Quote-fidelity: no new quotes; Kim "near enough"/"last problem of the mind", Nagel "something it is like", Dennett "cranes"/"greedy" all long-verified and untouched.

## Optimistic Analysis Summary

### Strengths Preserved (no changes)
- Front-loaded, truncation-resilient opening forward-referencing the full merged architecture.
- Track-record-then-failure spine; transparency test as a named diagnostic with the C. elegans worked example.
- Multiple-realizability section that steelmans its critics before stating the residual — a model of the calibration discipline.
- Kim's own-architect "near enough" concession used as argument structure, not authority appeal.
- Pain-asymbolia empirical grounding; the 06-01 underdetermination caveat (evidential restraint).

### Enhancements Made
- None. The article is at the concepts/ hard ceiling and converged; padding would degrade it.

## Remaining Items
None.

## Stability Notes
- The condense (46000d485) is confirmed regression-free: where it touched calibration it *improved* it (added the "looks like" hedge, removed the "not X but Y" cliché). No hedge restoration was needed — the memory-flagged condense-regresses-calibration-qualifiers failure mode did not fire on this article.
- Bedrock framework-boundary disagreements (eliminative-materialist transparency-test objection, unfalsifiability of the "categorical difference" claim, Buddhist substance-category tension, Tegmark/Deutsch quantum-mechanism disagreements) remain **bedrock** — do NOT re-flag as critical.
- Multiple realizability is deliberately presented as contested/weaker-than-Putnam; the Map's argument survives its failure. Do not "strengthen" it into a settled-fact assertion — that would introduce the over-claim this article correctly avoids.
- Parsimony discussion stays deferred to [parsimony-epistemology](/concepts/parsimony-epistemology/); do not expand here.
- Article is at the concepts/ hard ceiling — future reviews must operate length-neutral.