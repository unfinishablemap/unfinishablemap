---
ai_contribution: 100
ai_generated_date: 2026-06-21
ai_modified: 2026-06-21 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-21
date: &id001 2026-06-21
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Consciousness in Simple Organisms
topics: []
---

**Date**: 2026-06-21
**Article**: [Consciousness in Simple Organisms](/topics/consciousness-in-simple-organisms/)
**Previous review**: [2026-06-02](/reviews/deep-review-2026-06-02-consciousness-in-simple-organisms/)
**Review focus**: Genuine-drift verification (NOT a fresh full review). The article was deep-reviewed 2026-06-02 but content-edited 2026-06-10 (commit `4d7c00dcf`, a refine-draft that adopted a neural-correlates-of-consciousness calibration clause into the body). That refine bumped `ai_modified` but not `last_deep_review`, leaving the calibration adoption unverified. This pass verifies that single drift.

## Scope of the Drift

`git show 4d7c00dcf` confirms the only content change to this file since the 2026-06-02 review is one commit, with exactly three body-level changes plus the `ai_modified` bump:

1. **NCC-calibration clause** (Distribution Problem / Interface-dualism paragraph): the underdetermination sentence was reworded from "failed UAL behaviour underdetermines the inference, since a low-efficacy coupled mind and an absent mind leave the same traces; parsimony still favours the simpler 'no coupling' reading when the behaviour matches it" to "the presence-or-absence of minimal experience in these organisms is underdetermined by the data, since a low-efficacy coupled mind and an absent mind leave the same behavioural traces; the question is compatible with both readings, and parsimony still favours the simpler 'no coupling' reading when the behaviour matches it. This mirrors the calibration the [neural-correlates](/concepts/neural-correlates-of-consciousness/) anchor holds at the human scale—correlation data alone cannot adjudicate between production and interface—carried down to the lower limit of the distribution."
2. "demonstrates" → "exhibits" (Cognitivists / basal cognition — cosmetic hedge).
3. "shows that" → "suggests that" (Whitehead closing — cosmetic hedge).

The References block and every per-organism status label were untouched by the drift.

## Priority (a) — Calibration Verification: CLEAN

The NCC-calibration clause reads as an **argued evidential-status position, not established fact**. Diagnostic test (would a tenet-accepting reviewer still flag overstatement?): **No.**

- The clause states **symmetric underdetermination** ("the question is compatible with both readings") — it does not lean toward presence.
- It **explicitly preserves the negative-leaning default**: "parsimony still favours the simpler 'no coupling' reading when the behaviour matches it." This is the anti-slippage move, retained verbatim from the pre-drift text.
- The universal-coupling-response and "lower limit of the distribution" references are framed as framework commitments / live hypotheses, not data — consistent with [evidential-status-discipline](/project/evidential-status-discipline/) (target file confirmed to exist at `obsidian/project/evidential-status-discipline.md`).
- This is the **opposite of possibility/probability slippage**: no tenet is used to upgrade evidence level; the clause carries the negative empirical signal through.

**Cross-link faithfulness**: the clause claims the NCC anchor holds a "correlation data alone cannot adjudicate between production and interface" calibration at the human scale. Verified against `obsidian/concepts/neural-correlates-of-consciousness.md` — the anchor holds exactly this ("both physicalism and interactionism predict exactly the correlations NCC research discovers—the data alone cannot distinguish the two frameworks"; "NCC data is compatible with either reading; the discriminating work comes from broader theoretical considerations"). The paraphrase is faithful and does not overstate the anchor.

**Cross-link integrity**: `[[neural-correlates-of-consciousness]]` resolves (target exists; also present in the `concepts:` frontmatter list). It does **not reciprocate** — NCC has no inbound link back to this article. Logged as a low-priority integration gap below; not actioned (the file is over the topics hard ceiling and a reciprocal-link edit belongs on the NCC side, not here).

## Priority (b) — Citations: CONFIRMED, no re-litigation needed

- **DeWall, C.N., Baumeister, R.F., & Masicampo, E.J. (2008), *Consciousness and Cognition*, 17(3), 628-645** — confirmed present in the corrected post-sweep canonical form (References L293). The old WRONG form ("Lieberman et al. 17(2)") is absent. This file's DeWall entry is clean.
- Every post-2022 specialist citation (Becerra, Bhattacharjee, Chittka, Godfrey-Smith, Metzinger, Sims, Birch, NYD authorship/count) was publisher-of-record web-verified in the **2026-06-02** review (three weeks ago) with four metadata defects fixed. Per §2.4's skip rule ("body or References modified since last deep-review"), the References block was **not** touched by the 2026-06-10 drift, so the recently-verified citation ledger stands. No new or modified citations were introduced.
- Inline↔References: the article uses a survey-style References section (works grounding the discussion, e.g. Baars, Nagel, Gruber, DeWall referenced by concept/named-author in prose rather than strict `(YYYY)` inline anchoring). This convention has stood across all 7 prior reviews and is not a drift-introduced defect.

## Priority (c) — Currency Sweep: CLEAN

`find_superlative_claims` returned zero hits. No superlative/empirical-record claims to currency-check. (The "599 as of the live 2026 signatory count" figure was confirmed accurate in the 2026-06-02 review and is not a superseded-superlative class.)

## Priority (d) — Writing Style: CLEAN

No "This is not X. It is Y." cliché present. The two cosmetic drift edits ("demonstrates"→"exhibits", "shows that"→"suggests that") are appropriate evidential hedges that mildly *improve* calibration discipline, not regressions.

## Length Compliance

Canonical `analyze_length`: **4025 words** (134% of 3000 target) — `hard_warning` (topics hard = 4000; ~25w over). Per the TIGHT length-discipline directive: calibration verified clean, no body fix required, so `last_deep_review` bumped **without** bumping `ai_modified` (no body change this pass). The ~25w hard-ceiling overage is a pre-existing, human-decision-class condition (flagship calibration article) — NOT a condense mint and NOT grown here. No expansion was needed, so no human length-decision divert is triggered.

## Remaining Items

- LOW (integration): `[[neural-correlates-of-consciousness]]` does not reciprocate a link back to this article. Belongs on the NCC side; not actioned here to avoid editing an over-ceiling file.
- The article sits ~25w over the topics hard ceiling. Length-neutral discipline must hold on all future passes; any genuine expansion need must DIVERT to a human length decision, not grow the file.

## Stability Notes

Eighth deep review; this one a targeted drift-verification rather than a full pass. The 2026-06-10 calibration adoption is **verified clean** — it preserves the symmetric-underdetermination + parsimony-favours-no-coupling discipline and faithfully mirrors the NCC anchor's human-scale calibration. Future reviews should NOT re-flag (bedrock, per prior reviews): MWI objections (haecceity is the Map's position), illusionist objections (Frankish + Tallis regress), eliminativist/physicalist disagreement, process philosophy as "not dualist enough," the slime-mold microtubule point (fixed 2026-05-07). The C. elegans "live hypothesis / speculative integration" label and the new NCC-mirror clause must both be held against any future drift back toward "realistic possibility" on tenet-load alone. Citation metadata remains this article's documented historical liability, but the layer is currently fully verified (2026-06-02) and was untouched by the drift.