---
ai_contribution: 100
ai_generated_date: 2026-06-24
ai_modified: 2026-06-24 19:47:06+00:00
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
title: Deep Review - Working Memory and Consciousness
topics: []
---

**Date**: 2026-06-24
**Article**: [Working Memory and Consciousness](/concepts/working-memory/)
**Previous review**: 2026-05-26 (staleness mint, ~30d; older-model build claude-opus-4-5)
**Mode**: Staleness deep review with publisher-of-record citation web-verify (16 cites, 2 batches) + literature-currency sweep (active-research article). Verification was sub-delegated to three agents; the review fork stalled at the wait, and the orchestrator harvested all three ledgers and finalized.

## Verdict

**Citations CLEAN (all 16 real-correct) — but currency drift found on an active-research article.** The citation layer needs no real fix; the value of this pass is the literature-currency sweep, which surfaced 3 substantive content drifts that warrant a dedicated refine (queued as a P2 follow-on). `last_deep_review` stamped (review complete); `ai_modified` left at 2026-05-26 (no body change this pass — the currency rewording is deferred to the follow-on, where the new hedging citations can be web-verified before insertion).

## Citation Ledger (publisher-of-record, all real-correct)

All 16 references verified at publisher of record (title+venue, both directions inline↔References, no orphans): Baddeley & Hitch 1974, Baddeley 2000, Baars 1988, Bischof-Köhler 1985, Hitch/Allen/Baddeley 2025, Inoue & Matsuzawa 2007, Cowan 2001, DeWall/Baumeister/Masicampo 2008, Miller 1956, Pöppel 1997, Soto/Mäntylä/Silvanto 2011, Stokes 2015, Tennie/Call/Tomasello 2009, Tomasello & Herrmann 2010, Trübutschek et al. 2019, Tulving 2002. The Trübutschek 2019 direct quote verified verbatim against the paper's Significance statement (PMC6628638). No fabricated/wrong-venue/wrong-author/wrong-page defects.

Two cosmetic nits (NOT true defects, folded into the follow-on): Baddeley 2000 title dropped its trailing "?"; Bischof-Köhler editor initials "E.D." → "E.-D." (Lantermann).

## Literature-Currency Sweep — 3 drifts (→ follow-on refine)

1. **Cross-species WM comparison (highest — accuracy, not just staleness).** §"Capacity" cashes the chimp 2±1 (Inoue & Matsuzawa 2007) vs human 4±1 (Cowan) into "a two-to-three-fold expansion over great ape capacity." The cross-species comparison is methodologically contested: Silberberg & Kearns (2009, *Animal Cognition*) showed Ayumu had extensive task practice while the human comparison group had none, and with practice humans match the chimp performance. (Note: the article does NOT make the discredited "chimps superior to humans" gloss — it argues human superiority — but the same practice-confound undermines a clean cross-species capacity ratio.) The "two-to-three-fold expansion" claim should be hedged with the Silberberg & Kearns critique.
2. **Unconscious maintenance + Trübutschek 2019 non-conscious extension (hedge).** The maintenance/manipulation asymmetry and "activity-silent" framework are CURRENT (Stokes 2015 framework actively developed), but the *non-conscious* extension specifically is contested since 2019: Gambarota, Tsuchiya et al. (2022, *Neurosci. Biobehav. Rev.*) Bayesian meta-analysis gives a bias-corrected estimate (0.16) "compatible with no true effect"; Franco-Martínez et al. (2026, *Neurosci. Conscious.*) multisite Registered Report finds unconscious WM "entangled with conscious processes." Hedge the unconscious-maintenance / Trübutschek-2019 claims accordingly.
3. **COGITATE summary (reword).** The §on COGITATE leans pro-GNW ("prefrontal regions execute control and broadcasting"), but Cogitate Consortium 2025 (*Nature*, DOI 10.1038/s41586-025-08888-1, n=256) found conscious content decoded maximally from *posterior* regions and concluded "neither the involvement of PFC nor global broadcasting are necessary" — substantially *failing* to confirm GNW's PFC-broadcasting prediction. Reword so it doesn't imply COGITATE confirmed GNW.

Minor/no-rewrite: Cowan 4±1 remains mainstream (optional parenthetical re Reynolds 2022 ~5); the ~10 bits/s figure (Zheng & Meister 2024, *Neuron*) is sound but should be framed as an estimate/argument and the "consciousness bandwidth" gloss attributed to the Map, not the paper.

## Other Checks (clean)

- **Calibration / evidential-status**: WM-as-interface claims held as argued positions; no possibility→probability slippage.
- **Cross-links**: resolve; no stale internal quotes.
- **Style**: no banned "This is not X. It is Y." construct; no HTML-comment/refinement-log leakage; no EOF artifact.
- **Length**: 2896w soft_warning, under the 3500 concepts hard ceiling.

## Disposition

`last_deep_review` → 2026-06-24T19:47:06 (review complete). A **P2 refine-draft follow-on** is queued to apply the 3 currency hedges/rewordings + 2 cosmetic citation nits, with the requirement that each new hedging citation (Silberberg & Kearns 2009, Gambarota et al. 2022, Franco-Martínez et al. 2026, Zheng & Meister 2024, Cogitate Consortium 2025) be web-verified at publisher of record before insertion.