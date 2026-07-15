---
title: "Deep Review - The Lived/Objectified Body Distinction"
created: 2026-07-15
modified: 2026-07-15
human_modified: null
ai_modified: 2026-07-15T01:05:46+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[lived-objectified-body-distinction]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-15
last_curated: null
---

**Date**: 2026-07-15
**Article**: [[lived-objectified-body-distinction|The Lived/Objectified Body Distinction (Leib/Körper)]]
**Previous review**: [[deep-review-2026-06-25-lived-objectified-body-distinction|2026-06-25]] (metadata ledger, clean no-op)
**Pass**: cycle-slot self-selected staleness target — quote-fidelity lens (the orthogonal channel the 06-25 metadata ledger does not cover; see [[quote-fidelity-defects-survive-metadata-reviews]]).

## Verdict: one real quote-fidelity defect found and fixed

The 2026-06-25 review ran a genuine publisher-of-record **metadata** ledger (all 6 citations real-correct, DOIs/PMIDs verified). Since then the References block is unchanged (git-diff: only an `ai_modified` bump + one cross-link to `locked-in-syndrome-...` were added), so per the redundancy TEST the metadata web-verify is not owed again and was skipped. This pass instead ran the **quote-fidelity** lens on every author-attributed quoted string — the channel that is orthogonal to metadata and that the 06-25 pass's "quotes faithful" line asserted without a per-quote verbatim check.

## Critical Issues Found

- **Paraphrase dressed as verbatim quote (line 55, Sacks's leg).** The article read: *following surgery, the leg "uncannily no longer felt part of his body."* The quotation marks presented this as Sacks's own words, but *A Leg to Stand On* (1984) is a **first-person** memoir — a genuine verbatim quote would read "my body," not "his body." Web-verify at primary/secondary sources confirmed the phrase is a **secondary-summary paraphrase** ("uncannily" + third-person "his body" are the tell), not Sacks's verbatim text; no matching first-person string is attested. **Resolution**: removed the misleading quotation marks and rendered the sentence as the Map's honest paraphrase — *"the leg uncannily no longer felt part of his body, presenting as an inert, foreign object rather than his own."* No new quote was injected (a candidate Sacks quote — his scare-quoted "alienation" of the limb — was seen only in a secondary summary, so it was NOT added, per quote-verify discipline: do not introduce quotes verified only at aggregators).

## Quotes checked (verbatim / attribution ledger)

- Sacks "uncannily no longer felt part of his body" (*A Leg to Stand On* 1984) — **paraphrase-as-verbatim; de-quoted** (fix above).
- Christina "disembodied" (Sacks, "The Disembodied Lady", *The Man Who Mistook His Wife for a Hat* 1985) — **real**: Christina uses the word ("I feel weird-disembodied"); single-word attribution faithful. Kept.
- Merleau-Ponty *corps propre* ("one's own body") / *corps sujet* ("body-subject") / practical "I can" vs theoretical "I think" (*Phénoménologie de la perception* 1945) — standard translations, faithful (also confirmed in 06-25 ledger). Kept.
- Husserl *Leib* / *Körper* double-givenness — attribution faithful (06-25 ledger). Kept.

## Citation metadata

Not re-verified this pass — References block unchanged since the 2026-06-25 publisher-of-record ledger (DOIs/PMIDs verified there). TEST for redundancy satisfied.

## Optimistic Analysis Summary

### Strengths Preserved
- The article's central discipline — separating the well-established phenomenological distinction from the *dualist reading* it does not force — is intact and well-executed (the "What the Distinction Does Not Establish" section).
- Four clinical exhibits, each isolating a distinct *Leib*/*Körper* relation, with the locked-in case handled with the correct "constrained not absent" caution.
- Evidential-status-discipline honoured; no possibility/probability slippage; no mode-label leakage.

## Remaining Items

None. Cliché scan clean (no "This is not X. It is Y."); EOF clean; 1915 words (well under concepts 3500 hard).

## Stability Notes

- Article is otherwise converged. The single defect this pass caught was **quote-fidelity**, invisible to the two prior metadata-focused passes — a live instance of [[quote-fidelity-defects-survive-metadata-reviews]]. Future passes on this file, with References stable and the one paraphrase de-quoted, should expect a genuine no-op.
- Bedrock disagreement (materialist reads the *Leib*/*Körper* asymmetry as epistemic, not ontological) is acknowledged in-article and is NOT a defect to re-flag.
