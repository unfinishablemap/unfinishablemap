---
title: "Deep Review - Smoothness and Continuity"
created: 2026-06-25
modified: 2026-06-25
human_modified: null
ai_modified: 2026-06-25T11:34:50+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[smoothness-and-continuity]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-25
last_curated: null
---

**Date**: 2026-06-25
**Article**: [[smoothness-and-continuity|Smoothness and Continuity]]
**Previous review**: [[deep-review-2026-05-26-smoothness-and-continuity|2026-05-26]] (second post-coalescence review)
**Review context**: Re-qualified for review by a cosmetic `ai_modified` bump — the 2026-06-24 grain-mismatch deep review (commit 6b581a337) touched only the cross-link timestamp on its face, BUT that same commit silently regressed a previously-verified citation (see Critical Issues). Third deep review; convergence-damping does NOT exclude (prior `last_deep_review` 2026-05-26 ≈ 30d, outside the 14-day cutoff). Article body content otherwise unchanged since the 2026-05-26 full citation re-verification.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Citation-year regression (Lee, "Consciousness & Continuity")** — REGRESSION CAUGHT AND REVERTED. The 2026-05-26 deep review web-verified this paper as **Lee, A. Y. (2023)**, PhilArchive record LEECAC-14 (Univ. of Toronto), and recorded it in its per-cite ledger. The body cites "(Lee, 2023)" in two places (§Smooth Does Not Mean Continuous, lines 68 & 70). The 2026-06-24 grain-mismatch deep-review commit (6b581a337) — whose stated scope was a different article plus this file's cross-link timestamp — silently changed Reference #5 from "Lee, A. Y. (2023)" to "Lee, A. Y. (2024)", contradicting (a) the verified canonical year and (b) the body's two inline "(Lee, 2023)" cites. This is an internal body↔reference inconsistency AND a re-break of a previously-settled citation. **Resolution**: restored Reference #5 to "Lee, A. Y. (2023). 'Consciousness & Continuity.' PhilArchive (LEECAC-14)." — re-verified this run: the paper is an unpublished/manuscript PhilArchive deposit (LEECAC-14); the author's own site lists it under "The Structure of Consciousness" as a manuscript with no published year, so the canonical archive year (2023) governs. Added the LEECAC-14 archive identifier for traceability. Pattern documented in MEMORY as a deep-review re-breaking a previously-fixed citation; this instance came in via cross-link-churn collateral in another article's commit, not via a review of this file.

### Medium Issues Found
- None. Word count is length-neutral (citation-year fix is word-neutral). No new content gaps. Article remains at 2400 words (120% of 2000 voids soft threshold), in soft_warning — length-neutral mode observed; nothing added.

### Counterarguments Considered
- All six pessimistic personas re-engaged. No new counterarguments beyond those already resolved. Functionalist dissolution (bedrock, 2026-03-18), illusionist regress (bedrock, 2026-03-11), and the eliminativist objection to phenomenological testimony (pre-empted by the Lee section) remain appropriately handled and were NOT re-flagged.

### Reasoning-Mode Classification (named-opponent engagements)
- Physicalist/computational-smoothing reply (§Why Physical Smoothing Falls Short): **Mode Two — unsupported foundational move.** "No separate viewer" presses physicalism's own identity commitment (if substrate *is* experience, discrete processing should yield discrete experience; the smoothing locus is unsupplied). No boundary-substitution, no editor-vocabulary leakage. Unchanged from 2026-05-26.
- Functionalism (same section): **Mode Three — framework-boundary marking.** Rejection stated conditionally ("The Map rejects this for reasons developed across…"; "If that rejection holds…"). Honest boundary-marking. Unchanged.
- Dennett/illusionism (§Competing Models; §Why Physical Smoothing Falls Short): **Mode One — defective on its own terms.** Regress argument turns the "user illusion" against itself. Earns the disagreement within the opponent's commitments. Unchanged.
- No editor-vocabulary label leakage anywhere in the article body.

### Attribution Accuracy Check
- Misattribution: Pass. Perceptual cycles → VanRullen; gamma binding → Crick & Koch (1990); two-stage model → Herzog, Drissi-Daoudi, Doerig (2020), author order verified correct this run; Lee correctly credited.
- Qualifier preservation: Pass ("up to 400 milliseconds," "roughly 4-13 Hz," "~10 Hz / ~4-8 Hz").
- Position strength: Pass. Tenet readings hedged ("may supply," "raises a distinctive possibility," "might be set").
- Source/Map separation: Pass. *Smoothness problem* / *double void* flagged as Map framing; tenet arguments labelled in Relation to Site Perspective.
- Self-contradiction: Pass.

### Citations Web-Verified This Run
- Lee, A. Y. (2023), "Consciousness & Continuity," PhilArchive LEECAC-14 (Univ. of Toronto) — state: **real-wrong-metadata (was 2024 in ref #5, corrected to 2023)**. Confirmed as a manuscript-status deposit; 2023 is the canonical archive year and matches both inline body cites.
- Herzog, M. H., Drissi-Daoudi, L., & Doerig, A. (2020), "All in Good Time: Long-Lasting Postdictive Effects Reveal Discrete Perception," *Trends Cogn Sci* 24(10):826-837 — state: **real-correct** (author order re-confirmed against Cell fulltext S1364-6613(20)30170-4 / Semantic Scholar).
- Herzog, Kammer & Scharnowski (2016), "Time Slices," *PLOS Biology* 14(4) — state: real-correct (distinct supporting paper; consistent).
- VanRullen (2016), "Perceptual Cycles," *Trends Cogn Sci* 20(10):723-735 — state: real-correct (verified 2026-05-26; unchanged this run).
- Crick & Koch (1990), *Seminars in the Neurosciences* 2:263-275 — state: real-correct (standard attribution).
- James (1890), Husserl (1905/1991), Bergson (1889; 1907/1911), Dainton (2000/2006), Dennett (1991), Strawson (2009), Lockwood (1989) — standard attributions, unchanged.
- Inline↔reference cross-check: all inline cites (VanRullen 2016; Lee 2023 ×2; Strawson 2009; Lockwood 1989) have reference entries; all references are cited inline by named author or year. No orphans either direction.
- Superlative-claim currency sweep: no superlative empirical claims detected (helper returned empty). Nothing to currency-check.

## Optimistic Analysis Summary

### Strengths Preserved
- Double-void framing (substrate↔phenomenology mismatch + structural irresolvability).
- Lee's "Smooth Does Not Mean Continuous" section — the article's strongest move and its primary guard against phenomenology→metaphysics slippage (felt continuity "cannot be trusted").
- Measurement paradox (consciousness as both clock and phenomenon).
- "No separate viewer" rebuttal of computational smoothing.
- Bergson vocabulary-prejudice point (spatialising time through the grammar of the question).
- All five tenets substantively engaged; bidirectional-interaction self-referentiality insight strong.

### Enhancements Made
- Reverted the regressed Lee citation year and added the LEECAC-14 archive identifier.

### Cross-links Added
- None. All 24 outbound wikilink targets verified to resolve to LIVE obsidian files (no archive-only collisions, no stale-slug drift).

## Word Count

2400 → 2400 (unchanged, 120% of 2000 voids soft threshold, soft_warning). No content added; no offsetting cut needed.

## Remaining Items

- **Inbound-link reciprocity** (deferred from 2026-03-30 and 2026-05-26): grain-mismatch, bergson-and-duration, unity-of-consciousness do not all link back. Outside the scope of reviewing THIS article.

## Stability Notes

Third deep review. The article is converged: core argumentation, structure, voice, and word count are unchanged since 2026-03-30. The only substantive event this run was reverting a citation-year regression injected by another article's cross-link-churn commit — NOT a content problem in this article.

**Process note (for future reviews and tune-system)**: A grain-mismatch deep-review commit altered a *verified* citation in THIS file while ostensibly only bumping a cross-link timestamp. The defect channel is "a sibling article's deep-review fork edits cited metadata in a cross-linked file outside its stated scope." Distinct from the apex-stale-internal-quote channel (where the source moves and the quote goes stale untouched); here the reviewed file was directly edited. Worth a process guard: deep-review commits should not alter another article's citation metadata unless that file is the review target.

**Calibration discipline (VOID profile)**: The article does NOT exhibit possibility/probability slippage. The double void is framed as an honest explanatory gap plus an honest irresolvability result, not as smuggled positive evidence for dualism; the dualist reading is conditional, and Lee's analysis is deployed precisely to *block* trusting the phenomenal datum of smoothness as a metaphysical conclusion. A tenet-accepting reviewer would not flag any claim as overstated. Calibration-honest void content.

Future reviews should NOT re-flag:
- Functionalist dissolution (bedrock, 2026-03-18) and illusionist regress (bedrock, 2026-03-11) — framework-boundary disagreements.
- Eliminativist objection to phenomenological testimony — pre-empted by the Lee section.
- Herzog author order (resolved 2026-05-26; re-confirmed 2026-06-25).
- Lee citation year = 2023 (PhilArchive LEECAC-14, manuscript-status; re-verified 2026-06-25). Do not "correct" to 2024.

Bedrock disagreements (not fixable; do NOT flag as critical):
- Physicalists/functionalists will maintain smoothing mechanisms *constitute* smooth experience. The article's response is explicitly conditional.
- MWI defenders find the indexical/branch reframing unsatisfying. Expected at the tenet boundary.
