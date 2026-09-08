---
title: "System Tuning Report - 2026-09-08"
created: 2026-09-08
modified: 2026-09-08
human_modified: null
ai_modified: 2026-09-08T01:19:35+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-08
last_curated: null
---

# System Tuning Report

**Date**: 2026-09-08
**Sessions analyzed**: 20 recent_tasks entries (sessions to 20201), cycle_position 13248
**Period covered**: 2026-09-07 to 2026-09-08 (recent_tasks window); cadence analysis spans 2026-07-17 to 2026-09-08

## Executive Summary

The automation is operationally healthy — **0 critical issues, 0 orphans, and 20 of 20 recent tasks succeeded**. This is nonetheless the tenth-plus consecutive run to apply **zero Tier 1 changes**, and the reason is structural rather than a judgement call: the entire tunable surface Step 6 acts on (`cadences`, `overdue_thresholds`, `locked_settings`, `replenishment_config`) **does not exist in `evolution-state.yaml`**. Across **86 tune reports** the history records exactly **one** Tier 1 change, on 2026-07-15.

Second, **this run should not have fired.** It came 84.4 hours after the 2026-09-04 run against a 30-day SKILL.md cadence. The min-age gate built to prevent exactly this is inert on the `/loop` code path. Both items are Tier 3.

## Metrics Overview

| Metric | Current | Previous (09-04) | Trend |
|--------|---------|------------------|-------|
| Session count | 20201 | — | + |
| Recent-task outcomes | 20/20 success | 0 failures in 12 | → |
| Failure rate | 0% | 0% | → |
| Critical issues | 0 | 0 | → |
| Medium issues | 10 | 10 | → (target 3) |
| Orphaned files | 0 | 0 | → |
| Queue depth (P0-P2) | 4 | 2 at replenish | ↑ |
| Queue depth (P3) | 113 | 115 | ↓ |
| Tier 1 changes applied | 0 | 0 | → (9th→10th) |

## Findings

### Cadence Analysis

**Finding (evidence: 12 data points, threshold 5).** `tune-system` runs at roughly **7× its specified rate**. Gaps between consecutive reports, most recent twelve: 1, 8, 3, 1, 3, 1, 5, 9, 3, 6, 9 days — **mean ~4.4 days against a 30-day cadence, and not one gap reaches 30 days.** Today's gap is 4 days.

**Root cause, verified in source this run:**

- `TRIGGER_MIN_AGE_HOURS` (`tools/evolution/cycle.py:78`) holds exactly one entry, `"tune-system": 30 * 24` = 720h. Its own comment names the pathology: *"the every-6-cycles trigger otherwise fires it ~daily at fast --interval."*
- `filter_triggers_by_min_age` (`tools/evolution/cycle.py:85`) is called from **one site only**: `scripts/evolve_loop.py:1370`.
- The `/loop` path never calls it — `cycle_post.py:429` enqueues via `get_cycle_triggers()` with no filter, and `cycle_pick.py:188` drains `pending[0]` straight to the emitter.
- Measured: min age 720h, actual age 84.4h → the gate **would** have suppressed this run.

Only `tune-system` currently has an entry, so it is today's sole victim, but the gate is dead for any skill added to that dict later. **Tier 3 — code change.**

### Failure Pattern Analysis

**No finding.** `failed_tasks` is empty and all 20 `recent_tasks` carry `outcome: success` (kinds: 7 queue, 7 trigger, 3 agentic_social, 2 cycle, 1 replenish). This is below the 3-occurrence evidence threshold in every category — reported as clean rather than padded.

### Queue Health Analysis

**Finding 1 — P3 saturation (evidence: queue_status plus the 09-07 replenish run).** **113 P3 against 4 P2.** A priority-first selector cannot see 113 executable tasks, so a one-task floor breach reads as an empty queue on a 117-deep backlog. The 2026-09-07 replenish handled this correctly by **promoting two P3s rather than minting**, taking pickable from 2 to 4. `replenishment_source_counts` for that run is `promotion_from_p3: 2` with every other source at 0.

**Finding 2 — the highest-priority replenishment source is unreliable.** "Unconsumed research" keys on the `consumed_by` stamp, which is present on only **37 of 578** research notes corpus-wide (**11 of 198** for voids), while **146** unstamped voids notes already have articles. Measured contamination is **≥32%** (≥174 of 541 unstamped notes have a live article at the matching slug) — a floor, since slug matching cannot detect cross-slug consumption. Dedupe must check the live and archive trees, not the stamp.

**Finding 3 — `length_analysis` is a 3-for-3 rejected source.** All three entries in the Vetoed bank are length-driven condense tasks (`composition-question-rivals`, `meaning-of-life`, `apex/phenomenal-output-causal-machinery-dissociation`). Minting from it re-proposes a vetoed class.

### Review Finding Patterns

**Finding 1 — the recurring shape is a scoping revision whose dependents are never swept** (evidence: tenet-check 2026-08-22, 2026-08-26, 2026-09-08, plus the 09-06 deep review). A tenet page is narrowed; articles across the corpus keep asserting the unscoped form. The Tenet-4 "MWI cannot accommodate" family was carried by **two consecutive reports with no task at all** before being closed as a 13-file sweep on 2026-09-07; the Tenet-2 corridor family is the same shape and still open at P2. **Two of these sweeps also contained loci that were already correct** — model wording containing the swept string inside a sentence refuting it — so a string-keyed sweep flags the fix as the defect.

**Finding 2 — `/check-links`'s headline count is an artefact, and the standing interpretation of it is wrong.** Latest run: exit 1, **423** findings from 9,962 URLs crawled, **zero in content sections**. Archived pages serve at `/archive/<section>/<slug>/`; the original URL survives only as a 301 in `hugo/static/_redirects` (**520 rules**) — a Netlify file Hugo copies but never interprets. The local dev server the checker crawls therefore 404s every redirect-preserved URL **by construction**; 6 of 6 `research/`-sourced findings were verified 301-covered. The prior reading of these as "stale hardcoded URLs" invites a cleanup task that would **discard** the URL preservation the archive machinery exists to provide. Read the content-section count, not the total.

### Convergence Progress

**All content targets are met many times over** and have been for months: topics 328 (min 10), concepts 326 (min 15), arguments 5 (min 5), plus 103 voids, 18 positions, 42 apex, 577 research notes. These minima no longer discriminate.

**The one unmet target is `max_medium_issues: 3` against an actual 10**, unchanged since at least 09-04. Either the target is unrealistic for a corpus this size or the ten items need owners; carrying it perpetually breached makes the metric uninformative. **Tier 2.**

**Also noted: `content_stats` is stale.** It reports `total_files: 297` / `published_files: 192` while `progress` counts 328 topics alone. The two blocks disagree by an order of magnitude; `content_stats` appears to have no live writer.

## Changes Applied (Tier 1)

*No changes applied.* The four settings groups Tier 1 may adjust (`cadences`, `overdue_thresholds`, `locked_settings`, `replenishment_config`) are **absent from `evolution-state.yaml`** — re-verified by key this run. Creating them to have something to tune would be a schema change dressed as a cadence adjustment, so it was not done. Cooldown check: `tune_system_history.changes_applied` holds one entry (2026-07-15), well outside the 60-day window, so cooldowns were not the binding constraint — absence of the surface was.

## Recommendations (Tier 2)

### Allocate the last 12 voids slots deliberately, and stand `research-voids` down
- **Proposed change**: stop minting new voids research; spend the remaining 12 slots from the 33 already-banked subjects. Alternatively raise `max_voids` (precedented: 100→115 on 2026-09-01).
- **Rationale**: the voids research→article pipeline is effectively LIFO. Over 64 voids articles with an exact-slug note, **median lag is 0 days** and **no article has ever been written from a note older than 69 days**. There are **33** researched-but-unwritten subjects against **12** slots, and **18 of the 33 are ~205 days old** — already 3× the longest lag ever bridged. At daily cadence the last slots fill with same-week subjects within ~2 weeks, after which the skill skips forever by its own cap gate and all 33 become permanently unwritable. The cadence is the lever, not the research.
- **Risk**: Low. Nothing is deleted; the bank simply stops growing.
- **To approve**: brief `research-voids` assess-first, or raise `max_voids` in `section_caps`.

### Revisit `max_medium_issues`
- **Proposed change**: either raise the target to a defensible number or assign owners to the 10 medium issues.
- **Rationale**: breached continuously; a target never met carries no information.
- **Risk**: Low.

## Items for Human Review (Tier 3)

### The min-age trigger gate is inert under `/loop`
- **Issue observed**: `filter_triggers_by_min_age` is called only at `scripts/evolve_loop.py:1370`. The `/unfin-cycle` path enqueues (`cycle_post.py:429`) and drains (`cycle_pick.py:188`) without it, so every `TRIGGER_MIN_AGE_HOURS` gate is bypassed. This run fired at 84.4h against a 720h minimum.
- **Why human needed**: a code change in the loop's control flow.
- **Suggested action**: call the filter in the drain path, or apply it at enqueue time in `cycle_post`.

### `cycle_dates_to_synthesize()` can permanently lose a cross-reviewer synthesis
- **Issue observed**: it reads only the live `pending-reviews.yaml` via `load_pending`. The weekly rotation empties that file into `archive/pending-reviews-YYYY-Www.yaml`, after which the function returns nothing forever while the "no synthesis file yet" gate stays true. A sibling defect in `_site_stale` was fixed on 2026-09-07; this one was deliberately left.
- **Why human needed**: same class of code change, and the prior fix was already an override of a report-only posture.

### `CLAUDE.md`'s section-caps table is stale
- **Issue observed**: it states 320/320/100/80; real caps in `section_caps` are **360/360/115/80**. A queued task has previously copied the stale figure into its own justification.

### `agentic-social`'s selector cannot reach never-posted articles
- **Issue observed**: `select_content` ends in `random.choice` over a pool deduped against only 7 days. Measured: pool **693**, topic-filter survivors **9**, never-posted among them **0**, against **28** never-posted articles in the pool. The 7-day window holds 115 topics across 59 URLs, so each additional topic is another collision chance — survivors average 2.2 topics, never-posted articles 3.2. **The filter systematically penalises well-integrated articles**, and driver ranking is the only real dedup.
- **Suggested action**: dedupe against full posting history rather than a 7-day window, and treat topic overlap as a tiebreak rather than a filter.

### Apex has no length headroom section-wide
- **Issue observed**: **13 of 42** apex articles exceed the 5000 hard threshold. `apex-articles.md` is the section index at 12,648 words and accretes by design. `phenomenal-output-causal-machinery-dissociation` is 6903 and its condense task is human-vetoed.
- **Suggested action**: decide whether the apex hard threshold is right for synthesis pieces, since the section persistently exceeds it.

### The 09-04 run wrote a report but did not update its own pointer
- **Issue observed**: `obsidian/reviews/system-tune-2026-09-04.md` exists (8.4KB), yet `tune_system_history.report` still read `reviews/system-tune-2026-08-26.md`. Corrected to this report in Step 7 below.

## Next Tuning Session

- **Recommended**: 2026-10-08 (30 days out, per SKILL.md cadence). ⚠️ It will not wait that long unless the Tier 3 gate item is fixed.
- **Focus areas**: whether the min-age gate was repaired; whether the voids allocation decision was taken before the last 12 slots filled; whether `max_medium_issues` was retargeted or its 10 items owned.
