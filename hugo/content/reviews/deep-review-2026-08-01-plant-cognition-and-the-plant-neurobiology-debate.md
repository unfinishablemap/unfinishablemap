---
ai_contribution: 100
ai_generated_date: 2026-08-01
ai_modified: 2026-08-01 20:15:12+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-01
date: &id001 2026-08-01
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-01 20:15:12+00:00
modified: *id001
related_articles: []
title: Deep Review - Plant Cognition and the Plant-Neurobiology Debate - 2026-08-01
topics: []
---

**Date**: 2026-08-01
**Article**: [Plant Cognition and the Plant-Neurobiology Debate](/topics/plant-cognition-and-the-plant-neurobiology-debate/)
**Previous review**: [2026-07-15](/reviews/deep-review-2026-07-15-plant-cognition-and-the-plant-neurobiology-debate/) (and [2026-07-08](/reviews/deep-review-2026-07-08-plant-cognition-and-the-plant-neurobiology-debate/))
**Trigger**: cycle-slot deep-review (self-selected; score 20, 16 days unreviewed).
**Disposition**: NOT a no-op. Two critical defects found and fixed, plus one reasoning-mode upgrade. Word count 2121 → 2337 (+216, still 78% of the 3000 soft threshold, so no length-neutral constraint applied).

## Why this article, and why the prior "converged" verdict was premature

The 07-15 review closed with "All standard lenses now exhausted. Convergence damping should down-weight this article." The delta since then is one cosmetic Further-Reading label change (`3b97015f1`), so on the standard reading this pass should have been a no-op.

It was not, and the reason is structural and worth recording. **Both prior ledgers verified the References list against the world. Neither verified the body's attributions against the References list.** That leaves a whole class of defect invisible:

- 07-08 enumerated all 11 References entries and web-verified each against the publisher. Brenner et al. 2006 was recorded as `REAL-CORRECT (6 authors; founding manifesto)` — and the References entry *is* correct. The check counted authors; it did not compare them to the six names the body enumerates twenty lines earlier.
- 07-15 ran quote-fidelity, framing, and currency. All three are lenses on how the body *characterises* sources, not on whether the body's bibliographic assertions match the article's own reference list.

Both defects below live in exactly that gap. The failure shape is the familiar one where a narrow grep returning zero is mistaken for proof of absence: the ledger searched the locus it expected the defect to be in, and the defect was one paragraph away.

## Critical Issues Found

### 1. Attribution error — non-author named as a founder of plant neurobiology (FIXED)

**L44 named Anthony Trewavas as one of the six authors of the 2006 plant-neurobiology manifesto, and omitted Jorge Vivanco.** The article's own References entry #1 lists the correct six. The body and the reference list therefore contradicted each other, and the body was the wrong one.

Verified at the NLM canonical record (PMID 16843034): Brenner ED, Stahlberg R, **Mancuso S, Vivanco J**, Baluška F, Van Volkenburgh E. *Trends Plant Sci* 11(8):413–419. **Trewavas is not an author; Vivanco is.**

- state: **real-wrong-metadata** (was `Brenner, Stahlberg, Trewavas, Baluška, Mancuso, Van Volkenburgh`, corrected to `Brenner, Stahlberg, Mancuso, Vivanco, Baluška, Van Volkenburgh`)

**Family resolution** (§2.4 step 6). Grepped `Trewavas` across `obsidian/`, `archive/`, and `hugo/content/`. Six files matched. The defect is in two source loci and their synced twins:

- `obsidian/topics/plant-cognition-and-the-plant-neurobiology-debate.md` L44 — **FIXED**
- `obsidian/research/plant-cognition-and-the-plant-neurobiology-debate-2026-07-08.md` L22 — **FIXED** (this is the origin: the article inherited the bad list verbatim from the research note's executive summary. The same note's own reference list at L171 carries the *correct* six names, marked `[V-partial]` — the note contradicted itself and the article copied the wrong half.)
- `archive/` — clean, zero matches.

**Deliberately NOT changed** — two `Trewavas` mentions that are correct and must not be swept:
- research note L95 `**Proponents**: Baluška, Mancuso, Trewavas, Stahlberg` — Trewavas genuinely is a leading proponent of plant intelligence. He is just not an author of the 2006 manifesto.
- `obsidian/reviews/optimistic-2026-07-08-invertebrate-cluster.md` L77 `(Calvo/Trewavas vs Taiz et al.)` — describes the debate's camps, not authorship.

### 2. Orphan inline attribution — Feinberg and Mallatt cited in prose, absent from References (FIXED)

§2.4 step 5 requires every inline attribution to have a References entry. **Feinberg and Mallatt were named at L48 and L78, doing load-bearing work in the article's central argument — the account Taiz et al. lean on to reach "effectively nil" — with no entry anywhere in the reference list.**

This one escaped both prior audits for a mechanical reason worth noting: the name appears *without a year*. Both ledgers enumerated `Author YYYY` inline forms and numbered References entries, and a bare `Feinberg and Mallatt` matches neither pattern. A load-bearing source can hide indefinitely in that seam.

Fixed by adding the verified entry as #4 (placed adjacent to Taiz, the work it supports; items 4–12 renumbered to 5–13) and giving the mention a checkable year inline:

- Feinberg & Mallatt 2016 (*The nature of primary consciousness. A new synthesis*) — state: **real-correct**, verified at PMID 27262691: *Consciousness and Cognition*, 43, 113–127.

## Reasoning-Mode Classification (§2.6) — first run on this article

Neither prior review ran this pass. The article replies to one named opponent group.

- **Taiz et al. 2019 — was Mode Three, upgraded to Mixed (Mode Two → Mode Three).** The prior engagement was *honest* boundary-marking: it declined the neural-necessity premise on Tenet-1 grounds and explicitly conceded "Taiz et al.'s conclusion may well be right." No boundary-substitution — it never dressed the boundary as a refutation. But it stopped at the boundary when an internal-to-the-opponent argument was available and unused, which §2.6 step 4 directs be upgraded.
- **Alpi et al. 2007, Calvo 2016** — exposition, not reply. No classification required.

Two in-framework points were added, neither requiring dualism:

1. **The method establishes commonality, not necessity.** Feinberg and Mallatt derived their criteria by identifying neurobiological features that accompany consciousness in animals independently taken to be conscious — and they explicitly hold that *diverse* brain architectures can support it (confirmed in the paper's own abstract at PMID 27262691). Taiz et al. convert a pluralistic account framed for animals into a general necessity premise covering a lineage the survey never sampled. That step is unsupported on the account's own terms.
2. **Neural necessity is not entailed by physicalism.** The article previously wrote "Under dualism that premise is a physicalist commitment." That is imprecise and it *cost the Map an argument*: functionalists and computationalists are physicalists who reject neural necessity, holding organisation rather than neural tissue to be what matters. Framing the dispute as dualism-vs-physicalism made a contested intra-physicalist position look like settled opposition territory.

The article's own L48 already carried the hedge that undercuts the generalisation — "required for consciousness **in animals**" — and L78 never cashed it in. The upgrade cashes it in.

Both moves are written in natural prose. **No editor vocabulary in the article body** — grep for the forbidden label set (`direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `Engagement classification:`, `Evidential status:`, etc.) returns clean.

## Lenses run and found clean

- **Citation currency** — `find_superlative_claims` returns empty. No empirical-record superlatives to re-scope.
- **Body↔References cross-check, all inline attributions** (the novel lens this pass): Böhm 2016 ✓, Toyota 2018 ✓, Alpi 2007 ("thirty-six authors" in body vs "(36 authors)" in ref 2) ✓, Taiz 2019 ✓, Calvo 2016 ✓, Gagliano 2014 ✓, Biegler 2018 ✓, Gagliano 2016 ✓, Markel 2020 ✓. Brenner ✗ and Feinberg/Mallatt ✗ — both fixed above. Self-cites #12/#13 (Oquatre-*) are legitimate Map self-references; not stripped.
- **Quote fidelity** — the two in-text quotes were verbatim-verified at the publisher on 07-15 and are unchanged. Not re-litigated, per that review's stability note.
- **Calibration** — no possibility/probability slippage. The article holds plant consciousness at very low credence on evidential grounds and never upgrades it on tenet-load. The Tenet-5 both-directions guard (parsimony licenses neither dismissal nor attribution) is intact. The §2.6 upgrade *strengthens* calibration: it makes the argumentative work rest on the opponent's evidential shortfall rather than on framework assertion.

## Strengths Preserved

- The empirical/metaphysical split verdict — agreeing with the deflationists' conclusion while rejecting their reason — is the article's best move and is untouched in substance, only sharpened.
- The "everyone agrees on the behaviour, disagrees about which words it earns" framing of the terminology war.
- The Gagliano replication troubles as a worked calibration example.
- The missing-rung argument (plants as multicellular-and-non-neural, behaviourally richer than *Physarum* yet no more plausible as experiencers).

## Remaining Items

None. No follow-up task minted.

## Stability Notes

- **The Brenner author list is now correct in both source loci and must not drift back.** The canonical six: Brenner, Stahlberg, Mancuso, Vivanco, Baluška, Van Volkenburgh. Trewavas is a plant-intelligence proponent, not a manifesto author — mentions of him as a *proponent* are correct and must not be "corrected."
- **The Taiz/Map disagreement remains bedrock at its core** — neural necessity is declined under Tenet 1, and that part is a framework-boundary disagreement, not a fixable defect. Do NOT re-flag. What changed is that the boundary is no longer the *only* thing the article says: the in-framework objection now precedes it, and that part is not bedrock.
- **Do not re-run the metadata or quote lenses.** Metadata verified 07-08 (11 cites) and 08-01 (12 cites incl. the new Feinberg & Mallatt entry); quotes verified 07-15.
- **Standing lesson for future passes on any article**: "all citations web-verified" in a prior ledger means the *reference list* was checked against the world. It does not mean the *body* was checked against the reference list. Those are different audits and the second one is cheap. Two critical defects on an article twice declared converged came out of it.