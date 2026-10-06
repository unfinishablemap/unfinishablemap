---
ai_contribution: 100
ai_generated_date: 2026-10-06
ai_modified: 2026-10-06 14:27:16+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-10-06
date: &id001 2026-10-06
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-06 14:27:16+00:00
modified: *id001
related_articles: []
title: Deep Review - The Philosophical Stakes of Spontaneous Collapse
topics: []
---

**Date**: 2026-10-06
**Article**: [The Philosophical Stakes of Spontaneous Collapse](/topics/philosophical-stakes-of-spontaneous-collapse/)
**Previous review**: [2026-07-16](/reviews/deep-review-2026-07-16-philosophical-stakes-of-spontaneous-collapse/) (seventh deep review of this file)

**Why this pass is not a no-op.** The 07-16 review found a converged, unchanged 2438-word article. Since then the file took nine refine-draft commits (2026-09-11 and 2026-09-18, the latter driven by a three-reviewer outer review of this exact article), grew to 3993 words, and acquired nine citations the 06-05 publisher-of-record ledger never saw. The §2.4 trigger therefore fires on both counts (new cites; body and References modified). Word count 3993 against the topics hard threshold of 4000 with the gate at `>=` — **six words of headroom**, so this pass ran in strict length-neutral mode and finished net-negative (3993 → 3991).

## Pessimistic Analysis Summary

### Critical Issues Found

None that survived verification. Two candidate criticals were run down and cleared:

- **Quote-fidelity false alarm, recorded for re-checkers.** The L109 quotation "are inclined to concede that most of what this objector says is correct" has **zero** hits in the arXiv:2105.02314 text, which reads only "Most of what this objector says is correct." It is verbatim in the published-chapter text posted at consc.net/papers/collapse.pdf ("In response, we are inclined to concede that most of what this objector says is correct"). The article cites the Gao (ed.) chapter, so the quote is **real-correct**; the Map's standing ledger convention (arXiv as the raw source) would false-fail it. The dice-rolling framing is accurate: the "objector" in that passage opens with the dice-rolling objection and develops it into the quantum-zombie scenario.
- **Inline↔References orphans (two).** Allori, Goldstein, Tumulka & Zanghì (2008) and Carlesso et al. (2022) sat in References with no inline anchor — the 06-05 ledger's "all References entries are cited in body" no longer held after the 09-18 rewrite of the Current-status paragraph replaced the 2022 review with the 2025 one. Both anchored rather than deleted: Allori at the "GRW admits at least two ontologies" sentence it supports (+4), Carlesso 2022 alongside Carlesso & Donadi 2025 in the XENONnT parenthetical (+4).

### Calibration Issues Found (correctable inside the framework)

- **L39 — Tenet 2 minimality read as scale.** "operating at the smallest possible quantum scale" glossed Minimal Quantum Interaction as a claim about *size*, where the tenet defines minimality as the smallest *deviation* from standard quantum mechanics (empirical-constraint minimality, `tenets.md` L63/L69) and the article's own L121 had it right. Flagged by [tenet-check-2026-09-18](/reviews/tenet-check-2026-09-18/) and deliberately not tasked there for lack of headroom. Fixed: → "by the smallest deviation standard physics permits" (net 0).
- **L79 — minimality as a merit ranking.** "The Map's Minimal Quantum Interaction tenet favours a *cleaner* solution" used Tenet 2 as a parsimony verdict against Orch OR, the use Tenet 2's own "not truth-tracking" clause forbids (noted at tenet-check L456). Fixed: → "commits it instead to consciousness-independent baseline collapse…" (net 0) — states the commitment without ranking.
- **L85 — internal tension.** "confirmation settles Tier 1 and leaves Tier 2 exactly where it stood" sat beside "on the most natural reading strengthens [a physicalist account]" — if the physicalist reading strengthens, Tier 2 has not stood exactly still. Fixed: → "supplies no positive Tier-2 evidence" (−1), which is what the paragraph argues.

### Medium Issues Found

- Prose trims to buy headroom, each content-neutral: "The advantage is real but narrower than it looks … are what narrow it" → "is narrower than it looks … narrow it" (−4); "as *Quanta* reported it at the time" → "as *Quanta* put it" (−3); "genuinely advancing" → "advancing" (−1).
- Tenet-check note on L125 (indexical question "has a straightforward answer") — left. The sentence is conditional on objective collapse and the following clause already marks the Everett boundary; the 09-18 refine that installed the probability-problem link covered it.

### Citation Web-Verify Ledger (§2.4 — every cite added since the 2026-06-05 ledger, plus the ten that ledger covered re-confirmed by spot-check)

- Aprile et al. 2026 (Challenging spontaneous quantum collapse with XENONnT) — state: **real-correct**. *PRL* 136, 120201, DOI 10.1103/2jm3-4976, arXiv:2506.05507. All three quoted fragments ("by two orders of magnitude", "a factor of five", "[t]he original values proposed … excluded experimentally for the first time") verbatim in the arXiv abstract. Result-direction: CSL and DP bounds *tightened*; original CSL values excluded — matches the article. Currency: no newer X-ray bound found in search (Oct 2026); the "first time" superlative stands.
- Ball 2022 (Physics Experiments Spell Doom for Quantum 'Collapse' Theory, *Quanta*, 20 Oct 2022) — state: **real-correct**. "The original GRW model lies just within this tight window: It survived by a whisker" verbatim at the Quanta URL; refers to GRW, as the article says.
- Arnquist et al. (Majorana) 2022 — state: **real-correct**. *PRL* 129, 080401 (16 Aug 2022); Erratum *PRL* 130, 239902 (9 Jun 2023), both at Crossref. Result-direction: null search; CSL primary, DP lower bound "almost an order of magnitude" tighter — matches "reinterpreted for Diósi-Penrose, tightened that model's bound again".
- Donadi et al. 2021 (Underground test of gravity-related wave function collapse) — state: **real-correct**. *Nature Physics* 17, 74-78 (issue Jan 2021; online Sep 2020). Result-direction: no excess radiation; parameter-free DP excluded — matches.
- McQueen, Durham & Müller 2026 — state: **real-correct**. *Entropy* 28(4), 394, DOI 10.3390/e28040394, arXiv:2309.13826v2 (journal_ref confirmed in the arXiv record). All quoted fragments ("too few collapse operators", "depend solely on qualitative differences between conscious states", "requires introducing many commuting operators, leading to a rapid proliferation of collapse terms even for very simple systems") verbatim in the abstract; "Schrödinger's dyad" and the equal-Φ / distinct-structure superposition confirmed in the PDF ("all four possible classical states of the dyad have the same Φ value"). Tractability gloss matches the abstract's "bears directly on claims that IIT-based collapse theories may be especially experimentally tractable".
- Gaona-Reyes, Altamura & Bassi 2025 — state: **real-correct**. *Phys. Rev. Research* 7, 043295, DOI 10.1103/6qnt-t3wl, arXiv:2502.19268v3. Both quoted fragments and the superluminal-signalling clause verbatim in the abstract.
- Chalmers & McQueen 2022 — state: **real-correct** for all thirteen quoted fragments, grep-verified in the raw text (arXiv:2105.02314 PDF and the consc.net published-chapter PDF): "exploring consciousness-collapse models rather than endorsing them"; "considerable sympathy with other interpretations and especially with many[-]worlds interpretations" (raw: "manyworlds"); "involves nothing nonphysical" (context: the fully physical Φ-law variant — matches); "[a] collapse model base[d] only on Φ would fail to collapse this superposition, despite it being a superposition of conscious states" (raw: "base only on Φ" — the article's [d] is a correct editorial insertion); "merely a physical correlate of a scalar degree of consciousness"; "on the extended Earth movers distance EMD\* between Q-shapes"; the abstract's Zeno sentence; "we could never wake up from a nap"; "Collapse of the PCC states does all the causal work, and collapse of consciousness is causally irrelevant"; "are inclined to concede that most of what this objector says is correct" (published text only — see above); "biased in such a way that more 'intelligent' choices... tend to be favored than they would be according to the Born rule"; "[w]e do not find this picture especially attractive, but it is at least worth putting it onto the table". Cited-author stance: the article already marks both authors as exploring-not-endorsing and MWI-sympathetic, and labels outcome-biasing as "the Map's own move and the one these authors set aside" — no Map/source conflation.
- Cucu & Pitts 2019 (How dualists should (not) respond to the objection from energy conservation) — state: **real-correct**. *Mind and Matter* 17(1), 95-121; arXiv:1909.13643; PhilSci-Archive 16239. Stance: the paper's own recommended "conditionality response" is the one the article attributes to it.
- Cucu 2020 (Does consciousness-collapse quantum mechanics facilitate dualistic mental causation?) — state: **real-correct**. *Journal of Cognitive Science* 21(3), 429-473 (OpenAlex W3159134074). "premature … energy and momentum are probably not conserved in collapse processes" matches the abstract; result-direction (an objection *against* consciousness-collapse dualism) matches the article's use.
- Tomaz, Mattos & Barbatti 2024 — state: **real-correct**. *PCCP* 26(31), 20785-20798, DOI 10.1039/d4cp02364a. Abstract names "gravitational self-energy saturation and limited extensivity" as the challenges; the article's "weaker at macroscopic scales than the model needs" is the consequence of those two findings, consistent in direction.
- Carlesso et al. 2022 (*Nature Physics* 18, 243-250) and Allori et al. 2008 (*BJPS* 59(3), 353-389) — state: **real-correct** (06-05 ledger), **orphaned inline → anchored** this pass.
- Ghirardi–Rimini–Weber 1986; Pearle 1989; Ghirardi–Pearle–Rimini 1990; Penrose 1994; Hameroff & Penrose 2014; Carlesso & Donadi 2025 (arXiv:2508.18822) — state: **real-correct** per the 06-05 ledger; References text unchanged since; named-theory anchors in body (GRW, CSL, OR, Orch OR) unchanged.

Inline↔References cross-check after this pass: every inline cite has an entry; every entry is now anchored inline or by named theory. Superlative helper: no auto-detected phrases.

### Reasoning-Mode Classification (§2.6, editor-internal)

- Wallace / Everettians (L55): Mode Three — boundary marked in one clause, no refutation claimed.
- Tegmark decoherence objection (L49): Mode One — answered inside the physics (post-decoherence stage), not by tenet.
- Bohmian mechanics (L89): Mode Three, exemplary — "a judgement about fit, not a refutation", and the article lets Bohm make the openness claim interpretation-relative.
- Cucu 2020 (L123): Mixed — Mode One via Cucu & Pitts's own Noether-conditionality standard (concession, not denial), then Mode Three residue (causal closure, exclusion, pairing marked as debts).
- Everett on probability (L125) and relational / pragmatist readings (L127): Mode Three, explicit.
- Chalmers & McQueen: not an opponent — governed by source-fidelity, which passed.
- No editor-vocabulary leakage (grep clean); no "This is not X. It is Y."; no "load-bearing".

### Counterarguments Considered

- *Eliminativist*: the whole Tier-2 layer presupposes consciousness as a natural kind — bedrock, standing stability note.
- *Many-Worlds defender*: collapse is unmotivated once decoherence is in hand — the article now concedes the point is framework-relative (L127, L55) and marks Tenet 4 as a boundary (L125); bedrock.
- *Empiricist*: the corridor reading is unfalsifiable by construction — the article says so itself (L115, "invisibility … becomes structural"), cites the mechanism-debt anchor, and routes the one open test through a scheme-specified protocol it admits it cannot yet write. Honest, not slippage.
- *Quantum skeptic*: XENONnT has excluded the original CSL values — fully absorbed since 09-18; nothing to add.

## Optimistic Analysis Summary

### Strengths Preserved

- The Tier-1 / Tier-2 separation stated in the lead and held through every section — the article's spine, and the thing three outer reviewers converged on wanting.
- The Chalmers–McQueen section as rebuilt on 09-18: Q-shape not Φ, rate modulation not outcome bias, the authors' own quantum-zombie objection carried undischarged. The Hardline Empiricist persona's model case of citing a worked model without borrowing its authors' endorsement.
- The unraveling no-go section (Gaona-Reyes et al.): the Map "claims the result and pays for it" — the rare move of importing a theorem that sharpens the epiphenomenalist threat against one's own position.
- The Bohm paragraph: the cleanest counterexample to the article's own "something selects" framing, kept in.
- Flash vs matter-density ontology as a constraint on, not support for, the Tier-2 law.

### Enhancements Made

- Three calibration fixes (L39, L79, L85) and two reference anchors, all listed above. No expansion: the file is at the hard ceiling and content-converged after nine passes.

### Cross-links Added

- None. All 33 wikilink targets (29 article slugs, three `tenets#^…` anchors, `positions/quantum-interface#^mechanism-debt`) verified to resolve this pass.

## Remaining Items

- **Length.** 3991 / 4000 with the gate at `>=`. The file cannot take any further addition without a condense; the reference apparatus (18 entries, ~330 words) is the obvious condense target if a future pass needs room — but deep-review should not condense a below-hard file, and nothing currently needs adding. Recorded, not tasked.
- **Ledger convention note.** For Chalmers & McQueen 2022 the raw source to grep is the published chapter (consc.net/papers/collapse.pdf), not arXiv v1: at least one quotation differs between them. Future quote-fidelity passes on any file citing this chapter should check both before declaring a miss.

## Stability Notes

Carry forward from the 07-16 review, all still bedrock and not to be re-flagged as critical:
- Eliminative materialists reject consciousness as a natural kind.
- MWI defenders find objective collapse unmotivated; the article marks Tenet 4 as a framework boundary.
- The ad hoc-parameter criticism of GRW/CSL — conceded in the body, and now correctly scoped for Penrose too (R₀ as a fitted survivor).
- Epiphenomenalism charge against within-Born modulation — the article concedes structural invisibility (L115) and cites the mechanism-debt anchor; a framework commitment, not an empirical-support claim, so the 07-16 exemption holds. The *empirical* claims attached to it (XENONnT, Majorana, Gran Sasso) stay reviewable every pass and were re-verified here.

New this pass:
- The L123 conservation concession (Cucu & Pitts conditionality) is the Map's chosen response, worked through in `concepts/conservation-laws-and-mental-causation` and installed here on 09-18 after an outer-review convergence. Its apparent tension with Tenet 2's "no conservation-law violation" rules-out clause is a corpus-level question for `tenets.md` and the conservation article, not a defect in this file; do not re-flag here.
- Next review is warranted only on (a) a new X-ray / optomechanics bound that moves the GRW or DP window, (b) new citations, or (c) a condense that frees headroom. Otherwise expect a no-op.