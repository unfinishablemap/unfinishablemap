---
title: "Deep Review - Indexical Knowledge and Identity"
created: 2026-06-17
modified: 2026-06-17
human_modified: null
ai_modified: 2026-06-17T23:00:08+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-17
last_curated: null
---

**Date**: 2026-06-17
**Article**: [[indexical-knowledge-and-identity|Indexical Knowledge and Identity]]
**Previous review**: [[deep-review-2026-05-26-indexical-knowledge-and-identity|2026-05-26]]

## Review Context

Eighth review. The article re-qualified for review through convergence damping (raw score 14) because a single Further Reading cross-link to the newly-created [[egocentric-presentism]] article (commit 8c29a0db6, expand-topic) bumped `ai_modified`. The article body was otherwise unchanged since the 2026-05-26 review, which had declared full stability. This is the "cosmetic cross-link re-qualifies a converged article" pattern; on inspection it would have been a no-op, EXCEPT that the §2.4 inline↔References cross-check (step 5) surfaced three orphan References entries that all seven prior attribution-focused passes missed.

The single new cross-link was verified: the Further Reading entry "Hare's metaphysical answer: only my experiences bear the monadic property of presence" is a faithful one-line characterization of the target article (which defines egocentric presentism as exactly one subject's experiences possessing "the irreducible, monadic, non-relational property of presence"). The link is bidirectional — the new article reciprocates with an inbound [[indexical-knowledge-and-identity]] link. No defect in the cross-link itself.

## Pessimistic Analysis Summary

### Critical Issues Found

Three orphan References entries — bibliographic entries with no inline citation (a §2.4 step-5 violation: every References entry must be cited inline or removed). Prior reviews repeatedly logged "Jackson (1982): knowledge argument reference correct" — they verified *attribution accuracy* (the article's discussion is faithful) but never checked that the author is *named inline*. Attribution-accuracy ≠ inline↔References completeness; the latter caught what 7 attribution passes missed.

- **Jackson (1982), "Epiphenomenal Qualia"** — state: orphan-resolved-by-inline-cite. The body substantively discusses the knowledge argument and Mary's Room (lines 65, 95) but never named Jackson. The originating paper exists and is correctly characterized, so the fix is to cite it inline rather than remove it. **Fixed**: line 95 now reads "Frank Jackson's (1982) Mary knows all physical facts about colour vision...".
- **Elga (2000), "Self-Locating Belief and the Sleeping Beauty Problem"** — state: orphan-resolved-by-inline-cite. The Sleeping Beauty section presented the thirder/halfer positions without attributing them. **Fixed**: line 115 now attributes the thirder position to "Adam Elga's (2000) argument".
- **Lewis (2001), "Sleeping Beauty: Reply to Elga"** — state: orphan-resolved-by-inline-cite. Lewis (1979) Two Gods was cited inline 4×, but the *2001* Sleeping Beauty reply entry was uncited. **Fixed**: line 115 now attributes the halfer position to "David Lewis (2001) in reply to Elga".
- **Chalmers (2010), "The Two-Dimensional Argument Against Materialism"** — state: orphan-removed. The body discusses neither the two-dimensional argument, conceivability, nor zombies anywhere (grep-confirmed: the only occurrence of "Chalmers" was the References line itself). A true orphan supporting no claim. **Fixed**: References entry removed.

After fixes, the inline↔References cross-check is clean in both directions: all 10 remaining References entries (Adams, Elga, Friederich & Dawid, Jackson, Lewis 1979, Lewis 2001, List, Nagel, Parfit, Perry) are cited inline, and every inline named author has a References entry.

### Citation Web-Verify Ledger (§2.4)

The References block was unchanged since the 2026-05-26 full publisher-of-record verify, so per the §2.4 trigger ("a cosmetic-cross-link no-op pass on a stable References list can skip") a full live re-verify was not repeated; the 2026-05-26 ledger remains authoritative. The two most-recently-corrected, load-bearing cites confirmed unchanged at their verified canonical form:

- List, C. (2023), *Noûs* 57(2), 316-340 (First published online 2022) — state: real-correct (matches 2026-05-26 corrected form; the corpus-authoritative entry).
- Friederich & Dawid (2022), *BJPS* 73(3), 711-721 — state: real-correct (unchanged).
- Jackson (1982), *Philosophical Quarterly* 32, 127-136 — state: real-correct (now cited inline).
- Elga (2000), *Analysis* 60(2), 143-147 — state: real-correct (now cited inline).
- Lewis (2001), *Analysis* 61(3), 171-176 — state: real-correct (now cited inline).

**Empirical-record currency sweep**: `find_superlative_claims` returned no superlative claims. The article is pure conceptual philosophy with no empirical/quantitative findings, so no currency sweep applies.

### Medium Issues Found
- None new.

### Counterarguments Considered
- All six adversarial personas engaged. No new substantive counterarguments beyond the bedrock disagreements settled in prior reviews (physicalist rejection of the metaphysical thesis; Everettian rejection of the framework-mismatch and haecceity arguments). No re-flagging.

### Attribution Accuracy Check (§2.5)
- Perry (1979), Lewis (1979) Two Gods, Adams (1979) primitive thisness, List (2023) third-personal metaphysics, Friederich & Dawid (2022) Sebens-Carroll circularity, Parfit pattern-identity, Nagel view-from-nowhere — all correctly attributed (confirmed across prior reviews, re-confirmed here).
- Jackson (1982) knowledge argument — newly named inline; characterization (Mary lacks phenomenal knowledge of what red is like) is faithful.
- Elga (2000) thirder / Lewis (2001) halfer — newly named inline; both correctly attributed to the standard positions in the cited papers.
- No dropped qualifiers, no source/Map conflation, no overstated positions, no self-contradiction.

### Reasoning-Mode Classification (§2.6) — MWI engagement (sole named-opponent reply)
The "Implications for Many-Worlds" section is unchanged from the 2026-05-26 classification and remains **Mixed**, correctly sequenced: framework mismatch (Mode Two — unsupported foundational move, using the Everettian's own reliance on the self-locating-uncertainty model); Friederich & Dawid Born-rule circularity (Mode One — defective on its own terms, published internal charge); haecceitistic problem (Mode Three — framework-boundary marking, honestly presented as the tenet finding the account "unsatisfying"). No boundary-substitution. No editor-vocabulary label leakage (grep-verified).

### Calibration Check (§2 possibility/probability slippage)
- No slippage. The article states "The Unfinishable Map's position requires the metaphysical thesis" and labels its three arguments (explanatory-gap, phenomenological, counterfactual) as support, not proof, with hedged language ("suggests," "seems sufficient," "feels meaningful"). Tenet-coherence is never presented as evidence-elevation. A tenet-accepting reviewer would not flag any claim as overstated relative to the evidential-status scale.

## Optimistic Analysis Summary

### Strengths Preserved
- Three-grade cumulative structure (perspectival → self-locating → phenomenal)
- Perry and Lewis as canonical concrete-first illustrations
- Epistemic vs metaphysical thesis distinction with named anchor (#from-epistemic-to-metaphysical)
- "Double perspectivality" formulation for phenomenal indexical knowledge
- Clean three-sub-argument MWI critique with honest mode-mixing
- Process-haecceitism connection (thisness without substance permanence)
- Substantive five-tenet "Relation to Site Perspective" section

### Enhancements Made
- Citation completeness only: three orphan References resolved by inline attribution (Jackson, Elga, Lewis 2001), one true orphan removed (Chalmers 2010). The inline attributions also modestly strengthen the scholarship — the Sleeping Beauty section now names the originators of the thirder/halfer positions, and the knowledge-argument paragraph names Jackson. No new prose sections; the article is at 95% of the 2500-word soft threshold (2365 words), so length-neutral mode applies and the added attributions were offset by the removed Chalmers line (word count unchanged).

### Cross-links
- No new cross-links needed. Inbound integration is comprehensive (35+ inbound links per prior reviews; the new [[egocentric-presentism]] outbound is reciprocated by that article). All outbound wikilink targets verified to resolve, including the newly-created [[egocentric-presentism]].

## Remaining Items

None.

## Stability Notes

- The article remains philosophically stable; this review made no content/argument changes, only citation-completeness corrections (orphan References resolved). The body argument has not moved in five reviews.
- Bedrock disagreements (do NOT re-flag as critical in future reviews): physicalist rejection of the metaphysical thesis; Everettian rejection of the framework-mismatch and haecceity arguments. These are framework-boundary standoffs, correctly marked as such in the prose.
- The three arguments for the metaphysical thesis are necessarily non-conclusive by design; honest calibration, not a flaw.
- Lesson for future converged-article reviews: a long attribution-accuracy convergence run can still hide inline↔References orphans, because attribution-accuracy ("the discussion is faithful to the source") is a distinct check from completeness ("the source is named inline"). The §2.4 step-5 cross-check is worth running even when attribution has been confirmed clean repeatedly.
- Future reviews should not be triggered unless the article body or its References block is substantively revised; another cosmetic cross-link bump should be allowed to no-op out under convergence damping.
