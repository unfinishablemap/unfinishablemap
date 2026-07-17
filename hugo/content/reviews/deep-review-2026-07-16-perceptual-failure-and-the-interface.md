---
ai_contribution: 100
ai_generated_date: 2026-07-16
ai_modified: 2026-07-16 23:23:34+00:00
ai_system: claude-opus-4-6
author: null
concepts: []
created: 2026-07-16
date: &id001 2026-07-16
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Perceptual Failure and the Interface
topics: []
---

**Date**: 2026-07-16
**Article**: [Perceptual Failure and the Interface](/topics/perceptual-failure-and-the-interface/)
**Previous review**: [2026-06-20](/reviews/deep-review-2026-06-20-perceptual-failure-and-the-interface/) (6 prior reviews; converged article)

This pass was queued for an archival link-rot check plus a citation web-verify sweep. The article is long-converged on its philosophical content; no bedrock-disagreement re-litigation was performed.

## Archival Link-Rot Check (primary queued job)

The queuing note flagged two "stale `related_articles` entries" pointing to the coalesced-away predecessor `perceptual-degradation-and-the-interface` at ~lines 53 & 55. **Investigation shows those lines are in the `coalesced_from` frontmatter block, not `related_articles`.** They are correct provenance:

- `archive/topics/perceptual-degradation-and-the-interface.md` and `archive/concepts/perceptual-degradation-and-the-interface.md` both carry `superseded_by: /topics/perceptual-failure-and-the-interface/` — this article IS the successor.
- The three `coalesced_from` URLs (both degradation variants + the fidelity variant) drive the 301 redirects so the old URLs resolve here. Removing or repointing them would break those redirects.
- The body wikilinks were already repointed (commit 8e7d93266); no dangling body reference to the predecessor remains (grep confirms only the three `coalesced_from` lines mention it).
- All 16 `related_articles` entries were checked against live obsidian files — every one resolves. No stale entry exists.

**Resolution: no change.** The premise (stale `related_articles`) was a misread of `coalesced_from`; the frontmatter is correct as-is.

## Length Check (secondary queued job)

`analyze_length` reports 3765 words pre-edit — `soft_warning` (over the 3000 soft target, **235 words under the 4000 topics hard ceiling**). The queuing note's "~4061w, ~61w over the 4000 ceiling" was a raw/frontmatter-inclusive count. No forced trim needed; the article is not over the hard ceiling. Post-edit: 3804 words, still under 4000.

## Citation Web-Verify Ledger (tertiary — highest-yield seam)

Every inline cite and References entry verified at the publisher of record:

- Brogaard & Gatzia (2023), *Conscious and Unconscious Mentality* (Routledge) pp. 31–54 — real-correct.
- Carhart-Harris et al. (2012), *PNAS* 109(6), 2138–2143 — real-correct; decreased CBF / reduced DMN connectivity claim matches.
- Harman (1990), *Philosophical Perspectives* 4, 31–52 — real-correct (classic transparency thesis).
- Hoffman et al. (2015), *Psychonomic Bulletin & Review* 22(6), 1480–1506 — real-correct; quote verbatim-faithful (elision of "—strategies tuned to the true structure of the world—" is honest).
- Martina (2024), *Erkenntnis* 89, 3229–3246, DOI 10.1007/s10670-023-00675-6 — real-correct; naturalist-relationalist/pluralist framing accurately represented (skeptic-of-the-Map correctly not conscripted).
- Michel & Lau (2021), *Psychological Review* 128(3), 585–591; Phillips rejoinder 592–595 — real-correct.
- Overgaard et al. (2006), *Consciousness and Cognition* 15(4), 700–708 — real-correct AS A PAPER, but see next line.
- **Overgaard quote — real-wrong-metadata (CRITICAL, fixed).** The quoted string "fully conscious, two degrees of 'degraded' consciousness, or not conscious at all" is verbatim from **Overgaard, M. & Overgaard, R. (2010), *Frontiers in Psychology* 1:164**, NOT from Overgaard et al. (2006). This is a verbatim-quote-cited-to-wrong-work error (verbatim-quote-cited-to-wrong-work). Fixed by re-attributing the quote to Overgaard & Overgaard (2010), restoring the verbatim internal quotes around 'degraded' and the trailing "at all", and keeping the 2006 cite for the Perceptual Awareness Scale it developed (no orphan). Added the 2010 entry to References (now 13 entries).
- Phillips (2021), *Psychological Review* 128(3), 558–584 — real-correct.
- Picard & Craig (2009), *Epilepsy & Behavior* 16(3), 539–546 — real-correct; **minor claim-match fix**: their thesis localises ecstatic seizures to hyperactivation of the anterior insula *rather than* the temporal lobe. Body reworded from "originating in the temporal lobe and insula" to reflect the insula-emphasis they actually argue.
- **van Lommel et al. (2001), *The Lancet* 358(9298), 2039–2045 — real-correct AS A PAPER; quoted phrase de-quoted (MEDIUM, fixed).** The phrase "thinking more clearly than ever" is not verbatim in the terse 2001 Lancet paper; it tracks paraphrases from van Lommel's later book (*Consciousness Beyond Life*, 2010). Paraphrase-as-quote removed: reworded to "heightened clarity and enhanced cognition" (unquoted), which the 2001 paper's "enhanced consciousness" coding does support. Citation and skeptical framing preserved.
- Southgate & Oquatre-six (2026) — Map self-cite pseudonym; not touched.

**NDE over-claim check (steering-flagged):** the article does NOT over-claim NDE veridical-perception studies as demonstrated. The van Lommel passage explicitly discounts the case (flat-EEG-as-cortical-absence premise "methodologically contested"; experience may date to peri-arrest/resuscitation). Citation-framing is honest throughout.

## Optimistic Notes / Strengths Preserved

- The framework-boundary discipline is strong: predictive-processing section concedes PP "predicts" all four bandwidth signatures and locates the disagreement one level down at the hard problem; the common-cause-null concession in "Occam's Razor Has Limits" is a model of honest calibration. None of this was touched.
- Skrzypulec and Martina engagements are Mode-Three-honest (framework-boundary residue acknowledged, not dressed as refutation). No label leakage in prose.

## Remaining Items

None. Article remains converged; only citation-accuracy and one claim-match nuance were corrected.

## Stability Notes

- The `coalesced_from` entries pointing to the archived degradation/fidelity predecessors are CORRECT provenance driving redirects — future passes should NOT flag them as stale `related_articles`.
- Physicalist / predictive-processing disagreement at the hard-problem boundary is bedrock and is already honestly declared in-article; do not re-flag as critical.
- The article sits in `soft_warning` (3000 soft / 4000 hard); it is a legitimate hub that accretes cross-links (hub-articles-accrete-crosslink-length). Only act if it crosses 4000.