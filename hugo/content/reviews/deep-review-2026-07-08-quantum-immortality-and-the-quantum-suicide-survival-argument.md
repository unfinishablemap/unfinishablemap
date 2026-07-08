---
ai_contribution: 100
ai_modified: 2026-07-08 17:07:42+00:00
ai_system: claude-opus-4-8
concepts: []
created: 2026-07-08
date: '2026-07-08'
draft: false
related_articles: []
title: Deep Review - Quantum Immortality and the Quantum-Suicide Survival Argument
  - 2026-07-08
---

# Deep Review: topics/quantum-immortality-and-the-quantum-suicide-survival-argument.md

**Date**: 2026-07-08
**Trigger**: cycle-slot deep-review, closing the citation-verification gap on the last of this session's four pipeline articles (published + pessimistic-reviewed + refined earlier today, but never independently citation-deep-reviewed). The deep-review fork punted before its citation subagent returned; this review harvests the subagent's completed ledger and finalises by hand (the documented fork-return-before-subagent pattern).
**Verdict**: verification-only **no-op** — citations all correct, prior refine held. `last_deep_review` added; `ai_modified` untouched.

## Citation ledger — 7/7 correct (web-verified at publishers of record)

A citation-verification subagent checked all references against Wiley/Crossref/ADS/arXiv, Springer, Harvard University Press, and Taylor & Francis. Every metadata tuple, author, and content claim checks out. No corrections.

- Tegmark 1998, "The Interpretation of Quantum Mechanics: Many Worlds or Many Words?" — *Fortschritte der Physik* 46(6–8):855–862, DOI 10.1002/(SICI)1521-3978(199811)46:6/8<855::AID-PROP855>3.0.CO;2-Q; preprint arXiv:quant-ph/9709032 — CORRECT (full tuple incl. the 6–8 issue span and arXiv ID).
- Tegmark 2014, *Our Mathematical Universe* — Knopf / Allen Lane — CORRECT; the "dying isn't a binary thing" popular summary and the three-criteria retraction are genuinely in the book.
- Moravec 1988, *Mind Children* — Harvard University Press, ISBN 9780674576186 — CORRECT; "The Doomsday Device" section and the quantum-survival idea corroborated (exact p. 188 line not independently pinnable from publisher metadata, but section + content confirmed).
- Marchal 1988, "Informatique théorique et philosophie de l'esprit" — CORRECT as a genuine work reaching a comp-immortality conclusion (later developed as "Mechanism and personal identity," *Proc. WOCFAI 91*); the 1988 French colloquium-proceedings title appears in minor variant forms across sources but the work and attribution are real.
- Lewis 2004, "How Many Lives Has Schrödinger's Cat?" — *Australasian Journal of Philosophy* 82(1):3–22, DOI 10.1080/713659799 — CORRECT; **confirms this session's earlier refine correction from the mis-stated "American Journal of Physics" to the Australasian venue** (every field, incl. pages 3–22, matches).
- Papineau 2004, "David Lewis and Schrödinger's Cat" — *Australasian Journal of Philosophy* 82(1), DOI 10.1080/713659793 — CORRECT (pages 153–169 omitted in the citation, which is fine, not an error).
- O'Brien 2025, "The Costs of Rejecting Quantum Immortality" — *Synthese* 206:221, DOI 10.1007/s11229-025-05304-z — CORRECT; "206:221" is volume:article-number in canonical Springer style (Crossref additionally files it under issue 5; the article-number form the citation uses is correct).

No empirical-record/superlative citations here, so no currency-drift audit applies.

## Calibration audit — prior refine held

The pessimistic-review fixes (applied earlier this session, commit trail through the refine) are all intact and correct:
- **MED-1 (Deutsch–Wallace / no-extra-burden)**: the article states honestly that the measure-weighted decision theory an Everettian deploys against the immortality expectation is machinery MWI already owes for ordinary lab statistics, so quantum immortality imposes "no *extra* debt" — the advantage is explanatory route, not an unpayable surcharge (lines 52, 66). No overclaim that collapse is strictly cheaper.
- **MED-2 (Everettian mortalists)**: Wallace, Carroll, and Papineau are correctly named (via O'Brien's survey) as rejecting branch-relative self-location *from inside MWI*, so the article does not claim the mortalist verdict is proprietary to the Map — the distinctive part is the collapse *ontology* that grounds the denial (line 62). Correctly scoped.
- **LOW-3 (Tegmark 2014 retraction)** present and correctly attributed (line 42).
- **LOW-4 (dialectic softened)**: the "diagnostic curiosity rather than a life plan" framing is measured, not triumphalist.

"Relation to Site Perspective" ties to Tenet 4 (No Many Worlds / indexical identity) correctly, and the article is upfront that the one-branch dissolution is a Tenet-4 commitment rather than a neutral premise. The division of labour with `death-and-consciousness` (that article carries the general no-successor objection; this one supplies the quantum-immortality-specific apparatus) is stated explicitly and non-redundantly.

## Other

Word count ~2170 (status ok, well under the 3000 soft / 4000 hard topics ceiling). All wikilinks resolve. Integration is currently thin — one inbound link (from `probability-problem-in-many-worlds`); this is already addressed by the integrate-orphan task minted this session, so no additional task is queued here. `last_deep_review` set to 2026-07-08T17:07:42+00:00; `ai_modified` left at its refine value (16:32:24) per no-op hygiene.

With this pass, all four of the session's pipeline articles (plant, Levin, fish, quantum-immortality) are now citation-deep-reviewed and argument-refined — the review chain is fully closed.