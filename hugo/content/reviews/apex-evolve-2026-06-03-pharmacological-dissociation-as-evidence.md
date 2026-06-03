---
ai_contribution: 100
ai_generated_date: 2026-06-03
ai_modified: 2026-06-03 08:48:54+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-03
date: &id001 2026-06-03
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[pharmacological-dissociation-as-evidence]]'
title: 'Apex Evolve Review: Pharmacological Dissociation as Evidence (2026-06-03)'
topics: []
---

# Apex Evolve — Cycle Maintenance Pass, 2026-06-03

## Scope

Cycle-triggered apex-evolve (every 4 cycles). Ran `check`-mode staleness scoring
across all 30 apex articles, applied the assess-first discipline, and performed
one targeted, length-neutral citation-metadata correction.

## apex_sources Integrity Check (all 30 apex articles)

Scanned every apex article's `apex_sources` frontmatter against on-disk content
files. **Result: clean.** Zero missing/renamed/coalesced source slugs across the
entire apex set — no archival link rot in any `apex_sources` graph. No repoints
required.

## Staleness Scoring

Top candidates by `days_stale × changed_source_count`:

| Apex | Score | Stale | Changed sources |
|---|---|---|---|
| machine-question | 66 | 33d | 2 |
| altered-states-as-interface-evidence | 66 | 22d | 3 |
| living-with-the-map | 64 | 32d | 2 |
| interface-specification-programme | 51 | 17d | 3 |
| process-and-consciousness | 42 | 42d | 1 |

### Why not the top scorers

- **machine-question** (4985 words): 15 words under the 5000 hard ceiling.
  Evolving it (integrating 2 changed sources) would breach the hard ceiling on a
  flagship apex whose calibration is load-bearing. Per length discipline, this is
  a human-length-decision case, not an auto-grow. Declined.
- **altered-states-as-interface-evidence** (4406 words): the three flagged source
  changes (coupling-modes, consciousness-disruption, anaesthesia) all predate this
  apex's deep-review of **2026-06-02** (yesterday), which already integrated the
  xenon-ketamine contrast, the KCC2 active-reboot pathway, Montupil's three-state
  framing, and neural inertia. The article is converged and current; re-editing
  would be churn (deep-review-over-reviews-converged). Verified it inherits **no**
  citation defect from the 2026-06-03 corpus-wide niaf011/Kerskens fix. Declined.

## Citation Defect Found and Fixed (the warranted work)

A corpus-wide citation correction landed 2026-06-03 00:22
(`19ae55437`): the *Neuroscience of Consciousness* 2025 paper **niaf011**
("A quantum microtubule substrate of consciousness…binding and epiphenomenalism
problems") was re-attributed from **Hameroff et al. → Wiest, M.C.**

[apex/pharmacological-dissociation-as-evidence.md](/apex/pharmacological-dissociation-as-evidence/) line 156 carried the **old,
now-incorrect** attribution: *"The contested Hameroff et al. (2025)
delayed-luminescence work on anaesthetic effects in microtubule quantum
properties…"* — this is precisely the niaf011 delayed-luminescence paper.

### Web-verification (publisher of record)

Verified at Oxford Academic / PubMed (PMID 40342554): niaf011 is **single-authored
by Michael C. Wiest** (Department of Neuroscience, Wellesley College). The
Hameroff→Wiest correction is correct.

### Fix applied (length-neutral)

Line 156: "The contested Hameroff et al. (2025) delayed-luminescence work…" →
"The contested Wiest (2025) delayed-luminescence work…". The "contested" hedge and
all surrounding calibration language ("compatible with … not entailment …
live-hypothesis tier") preserved verbatim. Net change: one author name. Word count
4200 → 4200, status unchanged (under hard ceiling).

### Corpus-wide confirmation

Scanned all 30 apex articles for any remaining Hameroff-attribution of the niaf011
paper. The two other apex articles citing niaf011
(`open-question-ai-consciousness`, `what-it-might-be-like-to-be-an-ai`) already
carry the correct **Wiest (2025)** attribution. `open-question-ai-consciousness`
line 135's "Penrose-Hameroff's proto-consciousness model" is the legitimate Orch-OR
model name, not a niaf011 misattribution. `pharmacological-dissociation` was the
only apex carrying the defect.

## Calibration

No calibration language altered. Evidential-status and direct-refutation discipline
preserved (the MQI paragraph's "not entailment / live-hypothesis tier" framing is
untouched). No mode labels in body.

## Length Status

| Apex | Words | Status |
|---|---|---|
| pharmacological-dissociation-as-evidence | 4200 | OK (soft 4000 / hard 5000) |
| machine-question | 4985 | At soft warning, 15w under hard — human-length-decision if evolved |
| altered-states-as-interface-evidence | 4406 | OK, converged |

## Frontmatter

`pharmacological-dissociation-as-evidence.md`: `ai_modified` advanced to
2026-06-03T08:48:54+00:00. `apex_last_synthesis` **left unchanged** (2026-05-27) —
this was a citation-defect correction, not a new source-synthesis pass.

## Summary

Assessed all 30 apex; apex_sources integrity clean; declined the two top staleness
scorers (one human-length-decision, one converged-yesterday); fixed one genuine
inherited citation defect (niaf011 Hameroff→Wiest) on the pharmacological apex,
web-verified at the publisher of record. Writes left uncommitted for the orchestrator.