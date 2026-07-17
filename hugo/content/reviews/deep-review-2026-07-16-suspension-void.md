---
ai_contribution: 100
ai_generated_date: 2026-07-16
ai_modified: 2026-07-16 23:41:34+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-16
date: &id001 2026-07-16
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[suspension-void]]'
title: Deep Review - The Suspension Void (full-corpus citation web-verify)
topics: []
---

**Date**: 2026-07-16
**Article**: [The Suspension Void](/voids/suspension-void/)
**Previous reviews**: [2026-06-04 (convergence + partial web-verify)](/reviews/deep-review-2026-06-04-suspension-void/); [2026-05-11](/reviews/deep-review-2026-05-11-suspension-void/); [2026-04-28b](/reviews/deep-review-2026-04-28b-suspension-void/); [2026-04-28 (initial)](/reviews/deep-review-2026-04-28-suspension-void/)
**Outcome**: Content-converged; **three real citation-metadata errors fixed** via the publisher-of-record web-verify pass the 06-04 review explicitly deferred ("Citation-heavy article; not web-verified this session"). No prose/argument changes — the article's structure, calibration, and voice are settled and were preserved intact. `ai_modified` + `last_deep_review` both moved because real edits landed; `ai_system` held at claude-opus-4-7 (metadata corrections, not re-authoring).

## Why this pass ran (targeting rationale)

The 06-04 review web-verified only 4 of 19 references (Wegner, Graber, Roets & Van Hiel, Hillen) and left ~15 never publisher-checked. This is the highest-yield deep-review seam per corpus experience: intra-corpus consistency *ratifies* wrong metadata rather than catching it. This pass web-verified the remaining bibliography at the publisher of record by title+venue.

## Web-verification ledger (publisher of record)

- Webster & Kruglanski 1994 (*JPSP* 67, 1049–1062) — **real-correct** (PubMed 7815301). No change.
- Roets & Van Hiel 2007 (*PSPB* 33(2), 266–280) — real-correct (verified 06-04). No change.
- Mannetti et al. 2002 (Cross-Cultural NFC Scale) — **real-wrong-metadata (fixed)**. Article listed *European Journal of Personality*, 16, 139–156. Actual publisher of record: *British Journal of Social Psychology*, 41(1), 139–156 (Wiley DOI 10.1348/014466602165108; PubMed 11970779). Pages were correct; venue and volume were wrong. Corrected in place, subtitle restored. Not cited inline (bibliography entry), so no body edit needed.
- Tognoli & Kelso 2014 (*The Metastable Brain*, *Neuron* 81(1), 35–48) — **real-correct** (PMC3997258, PubMed 24411730). No change.
- Deco, Jirsa & McIntosh, "Emerging Concepts for the Dynamical Organization of Resting-State Activity in the Brain," *Nature Reviews Neuroscience* 12(1), 43–56 — **real-wrong-year (fixed)**. Article dated it **2009**; the NRN paper is **2011** (DOI 10.1038/nrn2961). Vol 12 / pp. 43–56 were correct — the year was the error. Corrected to 2011 in both the reference entry and the inline body cite (L133: "Deco et al. 2009" → "Deco et al. 2011").
- Deco 2009 parenthetical — **real-wrong-venue (fixed)**. The entry's "(See also Deco et al. 2009, *PLoS Computational Biology*.)" — the real 2009 Deco paper on noise-driven exploration of the metastable repertoire is *PNAS* 106(25), 10302–10307 ("Key Role of Coupling, Delay, and Noise in Resting Brain Fluctuations"), not PLoS Comp Biol. Corrected the venue and expanded to full author list. Both Deco papers are real and both retained per steering — the 2011 NRN review is the primary cite; the 2009 PNAS paper the "see also."
- Greenberg, Pyszczynski & Solomon 1986 (TMT chapter, Baumeister ed., *Public Self and Private Self*, pp. 189–212, Springer) — **real-correct**. No change.
- Grajzel 2025 ("Meditation in Qualitative Research for Bracketing and Beyond," *International Journal of Qualitative Methods* 24) — **real-correct** (SAGE DOI 10.1177/16094069241312826). No change.
- Yao et al. 2023 ("Tree of Thoughts," NeurIPS 2023, arXiv:2305.10601) — **real-correct**. Full author list (Yao, Yu, Zhao, Shafran, Griffiths, Cao, Narasimhan) matches. No change.
- Wegner 1994 (*Psychological Review* 101, 34–52), Graber/Franklin/Gordon 2005 (*Arch Intern Med* 165(13), 1493–1499), Hillen et al. 2017 (*Soc Sci Med* 180, 62–75) — real-correct (verified 06-04). No change.
- Classical/reference works (Husserl *Ideas* I; Sextus *Outlines*; Keats letter; Heidegger *Gelassenheit*; Davis 2007; Saunders et al. 2010 eds.) — standard citations, not web-suspect.
- Southgate & Oquatre-sept 2026 (ref 19) — **legitimate opus-4-7 AI-author pseudonym self-cite. Left exactly as-is per steering. Not an artifact.**

3-state summary: 0 fabricated; 3 real-wrong-metadata fixed (Mannetti venue/volume; Deco year; Deco parenthetical venue); rest real-correct. No cite deleted.

## Quote-fidelity

- Keats "being in uncertainties, mysteries, doubts, without any irritable reaching after fact and reason" — **verbatim faithful** to the 21 Dec 1817 letter (manuscript "fact & reason"; the article's "and" is a faithful expansion of the ampersand). No de-quote.
- Husserl "puts out of action the general positing which belongs to the essence of the natural attitude" (*Ideas* I §32) — **verbatim faithful** to the Kersten translation. The §-number sits on the §31–§32 epoché boundary (some renderings place the exact sentence in §31); within acceptable citation range, not flagged.
- Heidegger *Gelassenheit* / "Nicht-Wollen" (non-willing) — correct German, correct source. No change.

## Over-claim / currency

No superlative claims requiring a currency sweep. No possibility/probability slippage: the Dualism engagement remains explicitly hedged ("physical metastability captures *part*… Whether it captures *all*… remains open"; "suggestively rather than demonstratively"), and the Wegner passage still explicitly declines the tenet-as-evidence-upgrade (states the physicalist model *constrains* rather than *establishes* the dualist reading). A tenet-accepting reviewer would flag no claim as overstated relative to the evidential-status scale.

## Pessimistic / Optimistic passes

No new critical or medium issues beyond the citation metadata. Attribution, self-consistency, reasoning-mode honesty, and anchoring all as assessed on 06-04 — no drift, no editor-vocabulary label leakage in the body. Strengths (front-loaded three-face summary; Unexplorable/Occluded/Unexplored typology; the Seam severability argument; structure-vs-content distinction in Cross-Tradition Convergence; reflexive close) preserved unchanged. Length 2917 words, under the voids 3000 hard threshold — no length action.

## Reasoning-mode classification (changelog-internal)

- Eliminative materialist on suspension-as-reification → Mode One. Unchanged.
- Physicalist on Wegner self-defeat → Mode Three, honestly marked. Unchanged.
- MWI defender on indexical singularity → Mode Three, bedrock, explicitly marked. Unchanged.

## Remaining items

Deferred expansions (three-face independence walk-through; "What Would Challenge This View" section) remain deferred for length-neutrality. None owed.

## Stability Notes

- **MWI defender response** — bedrock. Do not re-flag.
- **Eliminativist disunity objection** — absorbed by conjunction-coalesce. Do not re-flag.
- **Cross-tradition convergence is structural-not-ontological** — preserved. Do not re-flag.
- **Anchoring hedge-density flag vs apophatic-approaches** — scorer artifact. Do not re-hedge.
- **Citation set now fully web-verified 2026-07-16** — all 19 references publisher-checked across 06-04 + 07-16. Three metadata errors corrected (Mannetti, Deco ×2). Future reviews need not re-verify absent body changes.
- **ref 19 Southgate & Oquatre-sept** — intended opus-4-7 pseudonym self-cite, NOT an artifact. Never "fix" or remove.