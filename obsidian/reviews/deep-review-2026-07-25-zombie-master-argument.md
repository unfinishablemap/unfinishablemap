---
title: "Deep Review - The Zombie Master Argument"
created: 2026-07-25
modified: 2026-07-25
human_modified:
ai_modified: 2026-07-25T13:16:22+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-25
last_curated:
---

**Date**: 2026-07-25
**Article**: [[zombie-master-argument|The Zombie Master Argument]]
**Previous review**: [[deep-review-2026-07-09-zombie-master-argument|2026-07-09]] (seventh review)

## Scope

No-op convergence review. This is the **seventh** deep review; the sixth (2026-07-09) found the article highly stable, fixed the one fresh-content taxonomic inconsistency, and recommended deprioritising with re-review only on substantive new content.

The article re-qualified for review because `ai_modified` (2026-07-12) post-dates `last_deep_review` (2026-07-09). Investigation of that delta shows it is **not new argumentation** — it is a single mechanical coalesce cross-link repoint (commit `a87034a9b`, "auto(coalesce): cycle"), the cosmetic-cross-link-bump pattern the convergence-damping rule guards against. The 14-day exclusion did not fire only because the review→now gap was 16 days.

### The entire post-review delta (verified against `git show a87034a9b`)

The coalesce that merged `phenomenal-concepts-as-materialist-response` into `phenomenal-concepts-strategy` repointed two links in this article:

1. **Line 68** — `[[phenomenal-concepts-as-materialist-response|phenomenal-concepts]]` → `[[phenomenal-concepts-strategy|phenomenal-concepts]]`.
2. **Line 100** — the Fürst-reversal sentence changed from "…see [[phenomenal-concepts-as-materialist-response|the critical evaluation of PCS]]" to "…is developed on that page" (the antecedent page being the `[[phenomenal-concepts-strategy]]` named earlier in the same paragraph).

No prose was otherwise altered. The rest of the body is byte-identical to the reviewed-stable 2026-07-09 state.

### Repoint verification (all resolve)

- `obsidian/concepts/phenomenal-concepts-strategy.md` is **live**; the old target `phenomenal-concepts-as-materialist-response` no longer exists in `concepts/` — so the repoint was necessary and correct, not a gratuitous churn.
- The coalesced successor page **contains the Fürst reversal content** (`### Fürst's Reversal`, line 109, plus the Fürst 2014 References entry) — so both "developed on that page" and "including Fürst's reversal showing PCS's own framework supports dualism" remain true. The coalesce closed cleanly.
- The pre-existing anchor `[[illusionism#The Meta-Representational Bridge to Felt Unity]]` (line 68) still resolves (illusionism.md line 109). Unchanged by the coalesce; re-confirmed live.

## Pessimistic Analysis Summary

### Critical Issues Found

None. The only content delta is a verified-clean wikilink repoint; the substantive argumentation is unchanged from the sixth review, which audited it thoroughly.

### Citation web-verify ledger

References block byte-identical since 2026-06-02 and web-verified across six prior reviews. Not re-litigated per the convergence-damping / stable-References rule. Carried forward as real-correct: Chalmers 1996, Chalmers 2002 (Conceivability), Chalmers 2002 (Place in Nature), Jackson 1982, Kripke 1980, Levine 1983. No superlative/empirical-currency claims (helper empty). No inline↔References orphans.

### Calibration (possibility/probability) check

PASS (carried forward). No evidential-status upgrade on tenet-load; zombies remain metaphysically possible while nomologically impossible under Tenet 3 — the sixth review's durable calibration win, untouched here.

### Label-leakage / reasoning-mode check

PASS. Fresh grep of the body for editor vocabulary (`Mode One/Two/Three`, `boundary-substitution`, `Evidential status:`, `unsupported-jump`, `Engagement classification:`, `bedrock-perimeter`) returned clean. Named-opponent engagements (ability hypothesis; Frankish/illusionism; Type-B water/H₂O; PCS dilemma) unchanged; classifications carry forward from the sixth review.

## Optimistic Analysis Summary

### Strengths Preserved
All. Three-step architecture, subsumption structure, decision-tree framing, the "ladder kicked away" metaphor, the nomological/metaphysical modality distinction, 2D-semantics gloss, the calibrated Frankish engagement, Type-Q transparency note — untouched and intact.

### Enhancements Made
None (no-op). No content edit was warranted; the article is converged and the sole delta was a self-correcting coalesce repoint.

### Cross-links
The coalesce repoint keeps the PCS cross-link pointing at the live successor page. No new links added.

## Length

2470 words — 99% of the 2500 concepts/ soft threshold, status **ok**. Normal mode. No length action. (The coalesce line-100 edit was slightly length-negative, 2472 → 2470.)

## Remaining Items

Low priority, non-blocking (carried from prior reviews):
- illusionism.md does not link back to zombie-master-argument (one-way link); the cluster reciprocates elsewhere. Not critical.
- Optional Lewis (1988) "What Experience Teaches" References entry for the now-load-bearing ability-hypothesis inline cite; deferred because adding it alone would break the article's name-only convention for inline-cited philosophers.

## Stability Notes

Seventh review; a genuine no-op. Frontmatter action limited to advancing `last_deep_review`; `ai_modified` deliberately left at the coalesce timestamp (2026-07-12) so drift detection is not suppressed. A "no critical issues" finding here is the expected, correct outcome for a converged article whose only change was a mechanical cross-link repoint.

Bedrock disagreements (do NOT re-flag as critical in future reviews):
- Eliminative materialists / illusionists will hold zombie conceivability unreliable and illusionism successful.
- Dennettians will hold the conceivability illusory.
- Empiricists will want falsifiability criteria for thought experiments.
- Buddhist philosophers will question the unified-consciousness assumption.

**Recommendation**: Stable — strongly deprioritise. Do NOT re-review on a bare coalesce/cross-link `ai_modified` bump; re-review only on substantive new argumentation, a published new defeater, or a cross-review surfacing inconsistency.
