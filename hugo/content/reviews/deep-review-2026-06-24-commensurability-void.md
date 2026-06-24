---
ai_contribution: 100
ai_generated_date: 2026-06-24
ai_modified: 2026-06-24 16:51:31+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-24
date: &id001 2026-06-24
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Commensurability Void
topics: []
---

**Date**: 2026-06-24
**Article**: [The Commensurability Void](/voids/commensurability-void/)
**Previous review**: [2026-05-25](/reviews/deep-review-2026-05-25-commensurability-void/) (and [2026-03-26](/reviews/deep-review-2026-03-26-commensurability-void/), [2026-03-19](/reviews/deep-review-2026-03-19-commensurability-void/))

This is the fourth deep review, a fresh-eyes staleness pass (~30d since the 2026-05-25 confirmation; settled `ai_modified == last_deep_review`, no own-body churn). The article was confirmed stable and well-calibrated by the prior three reviews. The focus of this pass per the task brief was a **publisher-of-record citation web-verify** — the one channel that intra-corpus consistency cannot audit. That focus paid off: three citation/quotation defects survived three prior "verified" reviews and are corrected here.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

**Publisher-of-record citation web-verify (per-cite ledger):**

- **Nagel, T. (1974). "What Is It Like to Be a Bat?" *The Philosophical Review*, 83(4), 435–450** — state: **real-correct**. Verified via Duke UP / PhilPapers / UConn PDF. Volume, issue, pages all match. The inline paraphrases ("organized along dimensions we cannot even conceive", the "continuum" line) are correctly attributed as Nagel's; the deeper commensurability reading is framed as the article's interpretation. No change.

- **Díaz Boils, J. et al. (2025). "Structural Constraints to Compare Phenomenal Experience." arXiv:2502.02154** — state: **real-correct (paper/metadata); real-wrong-metadata (the in-quote)**. arXiv:2502.02154 verified at the publisher of record (arxiv.org/abs/2502.02154): authors J. Díaz-Boils, N. Tsuchiya, C.M. Signorelli (3 authors — "et al." is correct), title matches, submitted 2025-02-04, partial-order-not-total-order conclusion confirmed. **The quotation was a misquotation inside quotation marks.** Article had: *"some experiences may carry qualitative aspects that make them incompatible or non-comparable with other experiences."* Source abstract reads: *"it might be right that **some experiences carry** qualitative aspects that make them incompatible or non-comparable with other experiences, **quantitatively speaking**."* **Fix applied** — corrected to *"some experiences carry qualitative aspects that make them incompatible or non-comparable with other experiences, quantitatively speaking."* The dropped "quantitatively speaking" is load-bearing: it is exactly the article's own point (Φ measures *quantity*, not qualitative character), so restoring it strengthens rather than weakens the argument. (The surname appears hyphenated "Díaz-Boils" at the publisher and unhyphenated "Díaz Boils" in the article; the author publishes under both forms — left as-is, not a defect.)

- **Wittgenstein, L. (1953). *Philosophical Investigations*. §§243–315** — state: **real-correct (citation); real-wrong-metadata (the in-quote)**. §-range correct (private-language argument). **The quotation was a misquotation inside quotation marks.** Article had: *"the essential thing about private experience is not that each person possesses his own exemplar, but that nobody knows whether **people** also have this or something else."* Anscombe translation (§272) reads: *"The essential thing about private experience is **really** not that each person possesses his own exemplar, but that nobody knows whether **other people** also have this or something else."* **Fix applied** — restored "really" and "other people". The "other people" → "people" drop matters (the beetle-in-the-box point is specifically about *other* minds). The §272 source sits inside the cited §§243–315 span, so the range citation is fine.

- **Kagan, S. et al. (2022). "Welfare Comparisons Within and Across Species." *Philosophical Studies*, 179, 1–28** — state: **real-paper-WRONG-AUTHOR (and wrong year/volume/pages)**. This is the highest-severity find. The paper exists and the content the article draws from it (underdetermination; two indistinguishable sources of variation; SWU approaches presupposing the commensurability they aim to establish) is faithful — but the author is **Heather Browning, not Shelly Kagan**. Verified at Springer Nature Link (DOI 10.1007/s11098-022-01907-1) and Browning's own research page. Correct citation: **Browning, H. (2023). "Welfare comparisons within and across species." *Philosophical Studies*, 180(2), 529–551.** Every metadata field was wrong: author (Kagan→Browning), year (2022→2023), volume (179→180), pages (1–28→529–551). **Fix applied** to the article References. This survived three prior reviews precisely because intra-corpus author-only matching ratifies a wrong author when title + venue are correct — the task brief's instruction to verify TITLE+venue, not just author+year, is what caught it.

  **Inline↔References orphan (fixed):** the Browning/Kagan reference had no inline citation — the Ethical Stakes paragraph drew on the argument without naming the source. **Fix applied** — added inline "as Browning (2023) argues" to the underdetermination sentence, reconciling the orphan in both directions.

  **Corpus propagation (fixed):** the wrong "Kagan/2022" form also lived in (a) [research/voids-commensurability-void-2026-03-19.md](/research/voids-commensurability-void-2026-03-19/) (section header + reference list — note its URL already pointed at the correct Browning DOI) and (b) an open expand-topic task in `todo.md` ("Kagan et al. 2022 is already cited in commensurability-void"). Both corrected to Browning (2023) so the future welfare-triage expand-topic task does not reintroduce the wrong author.

**Empirical-record currency sweep** — `find_superlative_claims` returned no superlative claims; no currency-supersession risk. The Díaz Boils result is appropriately framed as a *conditional* formalization ("If the partial ordering result holds"), not a settled empirical record.

### Calibration Check (possibility/probability slippage)
- **No slippage** — re-confirmed against the diagnostic test. The "structurally impossible, not merely uncertain" thesis stays consistently conditional throughout ("If the partial ordering result holds," "may be structurally impossible," "might still possess," "may not merely be difficult"). The dualism connection in Relation to Site Perspective is framed as coherence/prediction ("the Map's dualism predicts"), not as evidence that elevates the evidential status of the partial-ordering result. A tenet-accepting reviewer would not flag any claim as overstated relative to the five-tier scale. The conditional framing must be preserved; do not "upgrade" structural-impossibility to flat assertion.

### Reasoning-Mode Classification
- **Not applicable** — the article replies to no named opponent. IIT is engaged as an impersonal counterargument (Φ as universal measure), honestly: Φ measures quantity not qualitative character; identical Φ may accompany incommensurable experience. No boundary-substitution, no label leakage.

### Void Classification Check
- **Confirmed unexplorable** on the territory axis (per [voids](/voids/) three-kinds framework). The article explicitly distinguishes structural impossibility ("no such mapping exists") from practical difficulty, which is the unexplorable classification. The conditional hedging keeps the unexplorable claim appropriately scoped. No reclassification.

### Medium / Low Issues
- None requiring action.

### Counterarguments Considered
- All six adversarial personas' objections remain bedrock framework-boundary disagreements documented in the three prior reviews (eliminative materialists reject "phenomenal experience"; functionalists question the structural/phenomenal distinction). Not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)
- "Conceptual vertigo" metaphor and the "ruler inside the thing being measured" analogy
- Partial-ordering mathematical anchor; clean total-order/partial-order distinction
- Wittgenstein private-language section
- Clean distinction from the Conceptual Scheme Void
- Imagery-void within-species data point (neutralizes the "extrapolation from a marginal bat case" objection)
- Four indirect approaches (structural comparison, apophatic cartography, translation chains, partial-ordering acceptance)

### Enhancements Made
- The three quote/citation fixes are net strengthenings, not just corrections: the restored "quantitatively speaking" aligns the Díaz Boils quote with the article's own Φ argument; the inline Browning attribution closes a reference orphan.

### Cross-link Reciprocity (voids cluster)
- Verified reciprocal: [imagery-void](/voids/imagery-void/) (links back, §"inter-subjective face intersects commensurability-void"), [synesthetic-void](/voids/synesthetic-void/) (links back, "The commensurability-void formalises this"), [mysterianism](/concepts/mysterianism/) (links back, "extends this insight to inter-mind comparison"), [animal-consciousness](/topics/animal-consciousness/) (links back, "takes this further"). All inbound/outbound links resolve. No changes needed.

## Remaining Items

None. The three citation defects are the substantive output of this pass; the article is otherwise at stable equilibrium.

## Stability Notes

After four deep reviews the *argument* is stable and the *calibration* is correct — both must be preserved (do not oscillate the conditional framing). The lesson of this pass is the inverse of "converged = no-op": a four-times-reviewed article still carried a wrong-author citation (Kagan→Browning) and two in-quote misquotations because intra-corpus consistency *ratifies* citation defects rather than catching them. Only the publisher-of-record web-verify surfaces them. Future reviews of this article can treat the body argument as settled, but should re-run the §2.4 web-verify if any citation or References entry is touched.

The adversarial personas' objections are bedrock framework-boundary disagreements and must NOT be re-flagged as critical. The structural-impossibility thesis is correctly hedged as conditional on the Díaz Boils partial-ordering result; preserve that hedge.