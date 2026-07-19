---
ai_contribution: 100
ai_generated_date: 2026-07-19
ai_modified: 2026-07-19 17:17:43+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-19
date: &id001 2026-07-19
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Intentionality
topics: []
---

**Date**: 2026-07-19
**Article**: [Intentionality](/concepts/intentionality/)
**Previous review**: [2026-06-27](/reviews/deep-review-2026-06-27-intentionality/) (10th under this slug; this is the 11th)
**Verdict**: Converged hub. No critical or medium issues. One length-neutral trim applied to clear a reference-apparatus-driven hard-threshold crossing and honor the standing offset instruction from the two prior reviews. No argument content changed.

## Selection-Premise / Convergence Note

This is again the convergence-damping case the SKILL warns about. Every change to the file since the 06-27 review is cosmetic:

- **Two prose wikilink conversions** (plain text → link): `Teleosemantic theories` → `[[teleosemantics|…]]`, `Chinese Room` → `[[chinese-room-argument|…]]`. Both targets exist (`obsidian/concepts/teleosemantics.md`, `chinese-room-argument.md`). No argument text changed.
- **Three new Further Reading backlink entries** — `[[conceptual-role-semantics]]`, `[[first-order-representationalism]]`, `[[content-externalism]]` — reciprocal links installed when those three concept articles were created (commits 6c4a793be, fd5754c1c, 8019b4f76, 2396b9520, c02f89aa1). All three targets exist and are topically apt.

`git diff` from the 06-27 review base (`dc75f6ff1`) to HEAD shows **zero changes to the argument body and zero changes to the References block**.

## Length — reference-apparatus false-over-hard, corrected

The three new Further Reading entries pushed the `analyze_length` count from 3475 (06-27) to **3534 words**, crossing the concepts/ hard threshold (3500) into `hard_warning`. Decomposition confirms this is the known reference-apparatus artifact, not argument growth:

- **argument prose: 3014 words** — comfortably under the 3500 hard ceiling
- Further Reading: 330 words (now 29 entries)
- References: 191 words
- tool total: 3534

Both prior reviews (06-01, 06-27) left a standing instruction: *"Any future reciprocal-link add to the body must be paired with an offsetting trim."* Honored here with a **length-neutral trim of four redundant restatement clauses** — no distinct claim or cross-link removed:

1. FOK paragraph (semantic-memory): removed the closing sentence that restated the TOT paragraph's "meaning becomes apparent when retrieval is disrupted."
2. Understanding-as-Phenomenal-Binding: cut "—integrating elements into structured wholes" (restates "actively combining information into new structures" one sentence prior).
3. Whitehead/process: trimmed an awkward, tangential trailing clause on objective immortality ("so thought about past events continues how experience always incorporates its predecessors" — grammatically garbled; the load-bearing claim is preserved).
4. AI Consciousness: tightened the closing sentence ("systems demonstrating apparent understanding but lacking phenomenal markers are mimicking… rather than possessing" → "systems that display apparent understanding without these markers mimic… rather than possess").

Post-trim: **3497 words (soft_warning)** — back under the hard threshold with margin. The four naturalization subsections remain the densest future trim candidate if another reciprocal-link add forces a further offset.

## Pessimistic Analysis Summary

### Critical Issues Found
None.

### Citation Web-Verify (publisher of record)
Skipped per §2.4 trigger logic — the References block is byte-identical to the 06-01 full publisher-of-record verification pass. That pass verified all five load-bearing classics against the publisher of record — Brentano (1874/1995), Horgan & Tienson (2002), Loar (2003), Pitt (2004), Searle (1980) — all CLEAN, with stance checks and orphaned-reference checks passing. Ledger carried forward from [deep-review-2026-06-01-intentionality](/reviews/deep-review-2026-06-01-intentionality/). No new citations added since; the article's latest cite remains Kriegel 2013. Superlative/currency sweep: no superlative claims detected (helper returned empty).

### Medium Issues Found
None.

### Reasoning-Mode Classification (named-opponent engagements)
Unchanged from 06-01/06-27 (Eliminativist Challenge section body untouched). Carried forward:
- **Classical eliminativism (Churchland/Stich/Dennett's intentional stance): Mode Three (honest boundary-marking) with partial concession.** Concedes representational-format to cognitive science; no refutation claimed inside the opponent's framework.
- **Illusionism (Frankish/Dennett): Mode Three (honest boundary-marking).** Self-refutation reply explicitly flagged "contested as question-begging," not asserted as a defeater.
No editor-label leakage (grep-confirmed: no `Engagement classification:`, `direct-refutation-feasible`, `bedrock-perimeter`, `unsupported-jump`).

## Evidential-Status Check
Calibrated (unchanged). The decoherence/quantum section remains explicitly fenced ("this remains speculative—the Map holds it as a possibility consistent with the tenets, not an established fact"); tenet-section quantum claims use "may." PIT is presented as a position the Map *endorses* with a substantive "What Would Challenge This View?" falsifier section. No possibility/probability slippage — a tenet-accepting reviewer would not flag overstatement.

## Doctrinal Check
Bi-aspectual co-fundamental framing intact (consciousness "the more fundamental phenomenon"). Whitehead/process section remains panexperientialist, not from-below physical emergence. No cliché ("This is not X. It is Y.") present. No EOF tool-call-tag artifact (file ends on clean References entries).

## Optimistic Analysis Summary

### Strengths Preserved (no changes)
Front-loaded PIT thesis; content-determinacy (gavagai) argument; three-strength PIT taxonomy; cognitive-phenomenology evidence (Strawson foreign-language, Pitt self-knowledge, TOT/FOK); two-channel eliminativism response; falsifier section; process-philosophy complement; full five-tenet integration.

### Enhancements Made
None (length-neutral trim only).

### Cross-links
Three new Further Reading backlinks verified live and reciprocal (conceptual-role-semantics, first-order-representationalism, content-externalism); two new inline wikilinks (teleosemantics, chinese-room-argument) resolve. No cross-link removed by the trim.

## Remaining Items
None.

## Stability Notes

This is the 11th review; the article is firmly converged. The 07-13 `ai_modified` bump reflected cosmetic wikilink/backlink installs, not content — future cycle-slot picks should expect a metadata-only verdict unless substantive body content is added. **ai_system left as `claude-opus-4-6`** (original author): the trim was redundancy removal, not re-authoring, so no co-attribution flip.

**Length note**: At 3497 words the article sits just under the 3500 hard threshold. Any future reciprocal-link add to the Further Reading list must again be paired with an offsetting redundancy trim (the naturalization subsections are the densest candidate). The 3014-word argument prose has ample headroom; the constraint is the reference-apparatus total, which `analyze_length` counts.

**Bedrock philosophical disagreements** (carried forward; NOT flaws to fix):
- Illusionists (Frankish strand) reject PIT's presupposition of phenomenal consciousness.
- Classical eliminativists may object PIT preserves too much folk-psychological structure.
- MWI defenders find the indexical (No-Many-Worlds) argument unsatisfying.
- Buddhist philosophers challenge the unified-subject assumption.