---
ai_contribution: 100
ai_generated_date: 2026-06-09
ai_modified: 2026-06-09 00:00:00+00:00
ai_system: claude-opus-4-8
author: Andy Southgate
concepts:
- '[[evidential-status-discipline]]'
created: 2026-06-09
date: &id001 2026-06-09
description: 'First full audit of the positions register (18 live entries across 4
  domain files): contradictions, dependency resolution, orphans, and confidence calibration.'
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[positions]]'
title: Positions Register Audit - 2026-06-09
topics: []
---

# Positions Register Audit — 2026-06-09

First full audit of the register. **18 live positions** counted on disk (not the stale
`progress.positions_written: 3` state field) across 4 files:

- `quantum-interface.md` — P-Q1 … P-Q10 (10)
- `agency-and-will.md` — P-A1 … P-A5 (5)
- `voids-as-evidence.md` — P-V1 … P-V3 (3)
- `positions.md` — index, no entries

All 18 are `Status: live`; none superseded or retired. (The skill arg expected ~19; actual is 18.)

## Check 1 — Internal contradictions

**No hard contradictions found.** The register is internally coherent. Two latent
tensions were examined and judged non-contradictory by design:

- **P-Q1 (prefers post-decoherence selection) vs P-Q4/P-Q5 (demote Stapp-Zeno / Orch-OR).**
  This is a *ranking*, not a contradiction — P-Q4/P-Q5 explicitly keep both candidates in
  the live set, not retired. Consistent.
- **P-Q2 (Born statistics preserved exactly) vs P-Q3 (bias-without-deviation challenge).**
  P-Q3 is the named tension *inside* P-Q2's reading, registered deliberately. Consistent.
- **P-A3 (invokes an atemporal-selection reading to dissolve the Libet timing puzzle) vs
  P-Q1 (prefers *forward-in-time* post-decoherence selection).** FLAGGED as a soft
  coherence tension, not a contradiction. The `forward-in-time-conscious-selection` article
  treats retrocausal/atemporal selection as the *foil* it argues against ("Why Forward-in-Time
  Models May Be Preferable"), while P-A3 leans (weakly, flagged as a hypothesis) on an atemporal
  reading. P-A3 already hedges the atemporal reading well below its empirical-critique content,
  so the registers do not assert incompatible commitments — but the agency register's atemporal
  fallback and the quantum register's forward-in-time preference sit in tension worth a human
  glance. See Follow-up T3.

## Check 2 — Dependency / citation resolution (priority this run)

**All "Argued in" and "Depends on" wikilink targets resolve to live files. No broken or
archive-only citations. No repointing needed.**

Specifically checked against the recent (2026-06-09) corpus churn the arg flagged:

- **Channel-width coalesce** (`channel-width-third-axis` + `does-a-wide-channel-force-thick-poles`
  → `dualism-channel-width-axis`, old slugs now archived): **no position cites any of these
  three slugs.** `grep` over `positions/` returns nothing. No action.
- **Illusionism cluster edits (2026-06-09).** The only illusionism reference in the register is a
  *paraphrase* inside P-V1's Asserts ("illusionism predicts the introspection-architecture
  cluster") — not a citation to [concepts/illusionism.md](/concepts/illusionism/). The claim it paraphrases is intact and
  still defended in the cited `apex/taxonomy-of-voids` (the rival-prediction table and the
  "compatible-with but not discriminating" verdict). The 2026-06-09 illusionism triple was a
  *citation-defect* convergence on the illusionism page itself; it does not touch any position's
  cited claim. No action.

All 30 distinct path-qualified and bare wikilink targets (apex/, topics/, concepts/, voids/,
project/) were resolved individually — every one hits a live file. `evidential-status-discipline`
is cited both bare and as `[[project/evidential-status-discipline]]`; both resolve to the single
live [project/evidential-status-discipline.md](/project/evidential-status-discipline/). (Note: the SKILL doc references it under
`concepts/`, which does not exist as a path — but no *position* uses that path, so no defect here.)

## Check 3 — Orphans

**No orphan positions.** Every live position's claim is defended by at least one cited live
article (verified by resolving every "Argued in" target and spot-checking that the cited article
actually argues the claim: P-A1 in `topics/free-will`, P-V3 in `voids/what-voids-reveal`, P-Q8 and
P-Q4 in their cited topics — all confirmed).

**Integration gap (not orphan):** position IDs are rarely back-referenced *by ID* in body
articles. `P-Q4..Q8`, all `P-A*`, and all `P-V*` have **zero** in-corpus ID mentions outside
`positions/`. This is expected — the agency and voids domains were created 2026-06-08 and the
articles predate them. The orphan check passes (claims are defended); the gap is an *inbound-link*
opportunity. See Follow-up T1 (P3 integrate-orphan).

## Check 4 — Confidence calibration

- **P-Q7 uses an off-vocabulary band: `moderate-to-high`.** The canonical vocabulary
  (`positions.md`, the SKILL, and `evidential-status-discipline`) enumerates only
  **low / moderate / high**. No interpolated band is sanctioned. NOT auto-edited: snapping it to
  `high` or `moderate` is a substantive calibration decision (it changes the asserted confidence),
  so it is left for a human/`update` call rather than mechanically normalized. See Follow-up T2 (P3).
- High-confidence entries (P-Q2, P-Q6, P-Q10, P-A4) audited for over-assertion: all four are
  either definitional/structural (P-Q2 "structural to the default reading"; P-A4 the verification
  limit), an accepted empirical result (P-Q6 Donadi falsification), or a meta-claim about corpus
  state (P-Q10). Assertive wording matches the band. No drift.
- Low entry (P-V3) audited for over-hedging-the-other-way: wording ("holds, provisionally",
  "whatever cumulative weight the catalogue legitimately earns", "has not yet passed an independent
  grading") correctly matches low. No drift.
- **Item (d) — does the 2026-06-09 convergence warrant band changes to the voids positions?**
  No. That triple was a citation-defect convergence on the illusionism page, not a verdict on
  void-convergence-as-evidence. P-V1 (moderate) / P-V3 (low) already encode the
  convergence-independence discipline correctly: P-V3's confidence is explicitly gated on an
  independent grading that "has not yet passed," and the recent convergence does not supply it.
  No band change justified.

## Check 5 — Staleness

**No stale positions.** All `Last reviewed` dates fall 2026-06-04 … 2026-06-08, well inside the
60-day window. (This audit does not bump them; it is read-only on the entries.)

## Check 6 — Cascade health

**Healthy.** No position is superseded/retired, so there are no retired-with-live-dependents
structural errors. The intra-file `[[P-XN]]` dependency graph in `quantum-interface.md`
(P-Q1→P-Q3; P-Q5→P-Q6; P-Q9→P-Q2/Q5/Q6/Q7; P-Q10 ranges over Q1/Q2/Q3/Q7/Q9) all resolves to
live entries in the same file.

## Edits made this run

**None.** No broken dependency required repointing; no contradiction required a retire; no
calibration error was mechanically fixable without a substantive judgment call. All findings are
reported above and queued below.

## Follow-up tasks queued

- **T1 (P3, integrate-orphan):** Add inbound ID references / paraphrase-anchors from body
  articles to the new agency (P-A1..A5) and voids (P-V1..V3) positions so the register is
  cross-cited from the corpus it summarizes.
- **T2 (P3, positions-evolve update P-Q7):** Normalize the `moderate-to-high` band to a canonical
  band (low/moderate/high), or amend the vocabulary in `positions.md` if an intermediate band is
  intended. Human calibration call.
- **T3 (P3, positions-evolve audit / human note):** Review the P-A3 (atemporal) vs P-Q1
  (forward-in-time-preferred) soft tension; decide whether P-A3's atemporal fallback should be
  re-worded to defer to the quantum register's forward-in-time preference.