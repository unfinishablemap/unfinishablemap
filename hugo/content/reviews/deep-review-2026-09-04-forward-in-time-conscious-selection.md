---
ai_contribution: 100
ai_generated_date: 2026-09-04
ai_modified: 2026-09-04 14:15:47+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-04
date: &id001 2026-09-04
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-04 14:15:47+00:00
modified: *id001
related_articles:
- '[[topics/forward-in-time-conscious-selection]]'
title: Deep Review - Forward-in-Time Conscious Selection
topics: []
---

**Date**: 2026-09-04
**Article**: [Forward-in-Time Conscious Selection](/topics/forward-in-time-conscious-selection/)
**Previous review**: [2026-07-14](/reviews/deep-review-2026-07-14-forward-in-time-conscious-selection/)
**Word count**: 3809 → 3830 (+21; soft_warning, 128% of 3000 target, under the 4000 hard cap — length-neutral mode observed: body prose shrank ~30 words, the +21 is entirely two new bibliographic entries)

## Scope

5th deep-review (plus 4 cross-reviews). Unlike the 2026-07-14 pass, this one was **not** a cosmetic re-qualification: the article's body and References block both changed since that review (commit `875542607b`, a refine-draft that re-attributed the improper-mixture quote from Schlosshauer 2004 to Tomaz et al. 2025; commit `79461d4d16`, adding the `[[improper-vs-proper-mixtures]]` wikilink; and the `topics/free-will` → `free-will` canonical-slug fix). The §2.4 publisher-of-record trigger therefore fired.

**The 2026-06-05 "all 15 references verified, ZERO defects" clean bill was not inherited.** That audit is on record as having *falsely verified* the Schlosshauer attribution that a later refine-draft had to correct — direct, in-article evidence for `citation-ledger-ratifies-the-reading-not-just-the-metadata`. Every cite was therefore re-checked independently at the publisher of record.

## Pessimistic Analysis Summary

### Critical Issues Found

**C1 — Factual error: wrong year and wrong category for the Gran Sasso result (FIXED).** The Orch OR section opened "A 2022 experiment at Gran Sasso ruled out the simplest version of the Diósi-Penrose (DP) collapse model." Two errors in one clause, and the claim carried no citation at all:

- The experiment is **Donadi et al. (2021)**, *Nature Physics* 17(1), 74–78 (online 2020-09-07, print 2021-01) — never 2022.
- The 2022 item in this literature is **Derakhshani et al. (2022)**, *Physics of Life Reviews* 42, 8–14, which is an **analysis paper**, not an experiment: McQueen's own text describes it as claiming a result "based on radiation emission measurements described in [Donadi et al.]".

The rest of the corpus already had this right — [positions/quantum-interface-calibration-history.md](/positions/quantum-interface-calibration-history/), [research/penrose-gravity-collapse-empirical-2026-03-14.md](/research/penrose-gravity-collapse-empirical-2026-03-14/), [research/tenet-falsification-conditions-2026-04-05.md](/research/tenet-falsification-conditions-2026-04-05/) and several changelog entries all say Donadi 2021. This article was the corpus outlier, and had been since at least the 2026-04-30 create.

**C2 — Attribution error: McQueen (2023)'s argument misstated in the Map's favour (FIXED).** The article said McQueen "argues this does not apply to Orch OR proper, since the refuted variant was generic DP collapse in bulk matter, not the biologically orchestrated collapse Hameroff and Penrose actually propose." Checked against the full text (arXiv:2301.12306), **none of that is McQueen's argument**:

- McQueen *agrees* an Orch OR variant is refuted — his opening sentence is "I agree with this claim."
- His actual point is terminological and dynamical, not biological-vs-bulk: the refuted model should be called the **"parameter-free Diósi model"**, because the Diósi–Penrose *criterion* for superposition lifetime (t = ħ/E_g) is untouched — "This formula has not been refuted. Nothing Penrose has put forward has been refuted." What survives the radiation bound is Penrose's *instantaneous, retroactive* collapse (and CSL/GRW-based variants), because Diósi's collapse is gradual and Penrose's is not.
- He explicitly does **not** exempt Hameroff and Penrose: the result "cuts out a small class of possible variants and leaves behind questions and challenges for the rest, **including the variant preferred by HP**."

The article's gloss made McQueen sound like he clears Orch OR, which is the direction that flatters the Map. The passage was rewritten to McQueen's actual position (narrowing, not exemption) with both underlying sources now cited.

Worth noting: the Map's **own positions register already holds the correct reading** (`quantum-interface-calibration-history.md` L62–63: "Penrose supplies a decay timescale (τ ≈ ℏ/E_Δ), not a stochastic collapse dynamics; Donadi et al. assume Poissonian collapse…"). This article had drifted out of sync with a position the register settled on 2026-07-31.

**C3 — Reference venue errors (FIXED).**
- McQueen 2023 was cited to *PhilArchive* when a peer-reviewed version of record exists: *Physics of Life Reviews* 44, 201–203, DOI 10.1016/j.plrev.2023.01.021 (Europe PMC, PMID 36791569). Material here, since the cite is load-bearing against the Gran Sasso objection.
- Von Neumann 1932 was paired with Princeton University Press. The 1932 original is *Mathematische Grundlagen der Quantenmechanik* (Springer, Berlin); Princeton published Beyer's 1955 English translation. Corrected to `1932/1955 … (R.T. Beyer, Trans.)`.

**C4 — Inline↔References orphans (FIXED).** Ghirardi/Rimini/Weber 1986 and Stapp 1993 both sat in the References with no inline cite. Anchored rather than deleted: GRW at the spontaneous-collapse-baseline sentence, Stapp 1993 at the "orthodox quantum mechanics without new physics" framing (safe for that book; Process 3 was deliberately *not* pinned to 1993).

### §2.4 Publisher-of-Record Citation Ledger

Every reference independently re-verified this pass (Crossref / arXiv API / Europe PMC / publisher pages), not inherited:

- Chalmers & McQueen 2021, arXiv:2105.02314 — **real-correct** (title/authors/ID exact)
- Derakhshani et al. 2022, *Phys. Life Rev.* 42, 8–14 — **added** (Crossref DOI 10.1016/j.plrev.2022.05.004)
- d'Espagnat 1976, *Conceptual Foundations of QM* 2nd ed., Benjamin — **real-correct**
- Donadi et al. 2021, *Nature Physics* 17(1), 74–78 — **added** (Crossref DOI 10.1038/s41567-020-1008-4; six-author list verified)
- Duch 2005, *J. Mind and Behavior* 26(1-2) — **real-correct**; page range 1–22 added (not in Crossref; verified via the journal's own back-issue listing at umaine.edu/jmb plus PhilPapers)
- Duch 2019, *Phys. Life Rev.* 31, 28–31 — **real-correct** (DOI resolves exactly)
- Georgiev 2017, CRC Press — **real-correct**
- Ghirardi, Rimini & Weber 1986, *Phys. Rev. D* 34(2), 470–491 — **real-correct**
- Hagan, Hameroff & Tuszyński 2002, *Phys. Rev. E* 65(6), 061901 — **real-correct**
- Hameroff & Penrose 2014, *Phys. Life Rev.* 11(1), 39–78 — **real-correct**
- Kastner 2012, CUP — **real-correct**
- Colanero 2012, arXiv:1208.0904 — **real-correct**
- McQueen 2023 — **real-wrong-metadata**: venue *PhilArchive* → *Physics of Life Reviews* 44, 201–203 (see C3)
- Tomaz, Mattos & Barbatti 2025, arXiv:2502.19278 — **real-correct**, and the **quote is verbatim**. Downloaded arXiv v3 PDF, extracted text, grep-matched three ways: "Decoherence does not tell how and why only one of these outcomes is measured." appears exactly, in the §problem-of-outcomes passage. The 2026-08 refine-draft's re-attribution off Schlosshauer was **correct** and is confirmed here, not flipped back (`tallis-misrepresentation-quote-propagation` discipline: re-extracted from the raw artefact rather than asking a summariser). Journal version of record noted (*Philosophical Magazine C*, 2025).
- Stapp 1993, Springer — **real-correct**; orphan fixed
- Stapp 2007, *Mindful Universe*, Springer — **real-correct** (title-disambiguated per `stapp-2007-mindful-universe-vs-2005-qid-paper`; this is the book, legitimately 2007, not the QID paper)
- Tegmark 2000, *Phys. Rev. E* 61(4), 4194–4206 — **real-correct**
- Von Neumann — **real-wrong-metadata**: 1932/Princeton → 1932/1955 with translator (see C3)
- Torres Alegre 2025, arXiv:2512.12636 — **real-correct** (exact-ID fetch: "Causal Consistency Selects the Born Rule…", single author Enso O. Torres Alegre, submitted 2025-12-14). The article's inline "not yet peer-reviewed" flag remains accurate — no journal ref on the arXiv record.
- Southgate & Oquatre-* self-cites (4) — Map internal, pseudonymous by convention; **not stripped** per `fabricated-map-self-cite-pseudonym-false-alarm`

Zero fabricated cites. Empirical-currency sweep: `find_superlative_claims` returns 0 — no superlative claims to re-date.

### Medium Issues Found

- Redundancy at three points (pre-decoherence vulnerability restated in the post-decoherence section head; the von Neumann-cut minimality claim stated twice; the post-decoherence-triad differentiation restated after §109 already made it). Trimmed — this supplied the length offsets.
- The `[[conjunction-coalesce]]` cross-link sentence claimed the editorial coalesce discipline exhibits "the same defeasibility logic" as the selection-criterion trilemma's third horn, "exactly as" route (iii). That over-identifies an editorial merge heuristic with a metaphysical primitive. Reduced to "a parallel restraint," link preserved. Classic `outbound-crosslink-sentences-are-never-reviewed-by-anyone` accretion.

### Counterarguments Considered

All six adversarial personas engaged. Nothing new survived as critical: the Quantum Skeptic's decoherence-timescale attack is already the article's own §"The Decoherence-Timescale Question"; the Empiricist's falsifiability charge is conceded in the article's own words ("This cost is paid, not avoided"); the eliminativist and MWI lines are catalogued bedrock (see Stability Notes).

### Hazard scans

- Editor-vocabulary label leakage (Mode One/Two/Three, `Engagement classification:`, `Evidential status:` callouts, `unsupported-jump`, `bedrock-perimeter`): clean.
- "This is not X. It is Y." cliché: clean.
- `load-bearing`: one usage, genuine structural work; retained.
- Possibility/probability slippage: clean, and unusually well self-policed — the article self-invokes [possibility-probability-slippage](/concepts/possibility-probability-slippage/) in the Dualism-tenet passage and explicitly disclaims that the improper mixture *forces* the Map's reading.
- Bare-slug markdown links bypassing the wikilink validator: none.
- QEC `[[n,k,d]]`-notation collision: none.
- Numeric cross-references into the References list (renumbering hazard, `inserting-into-a-numbered-ledger-breaks-cross-references`): grep-checked corpus-wide before renumbering — the body uses author-year only and no other file cites this article's reference numbers. Renumbering 1–23 verified sequential after the edit.

## Optimistic Analysis Summary

### Strengths Preserved
- Two-axes framing (temporal direction × collapse stage), with the honest note that collapse-stage is meaningful only inside the forward branch.
- Sustained calibration discipline: defeater-removal is repeatedly distinguished from evidence; the FAPP-invisibility of the proper/improper distinction is named as "the gap the framework occupies," with the critic's symmetric reading granted.
- The selection-criterion trilemma, with the third horn owned as an unanalysable primitive rather than hidden.
- The prebiotic "one mechanism with a conditional modulation term" framing, including its explicit honest residue.

### Enhancements Made
The Orch OR passage is now stronger *because* it is accurate: McQueen's real argument (the DP *criterion* survives; Penrose's retroactive collapse is not what the radiation bound measures) is a better defence of the pre-decoherence strand than the invented bulk-vs-biological one, and it comes with the cost attached rather than hidden.

### Cross-links Verified
`[[improper-vs-proper-mixtures]]` (added 2026-08) resolves to `obsidian/concepts/improper-vs-proper-mixtures.md`; `[[conjunction-coalesce]]` retained.

## Remaining Items

None blocking. One observation for whoever next touches the quantum-interface cluster: this article's Gran Sasso error survived four deep-reviews and a full citation audit because the audit checked *reference metadata* and the defective claim was an **uncited body sentence**. Uncited empirical claims are outside the §2.4 ledger's reach by construction.

## Stability Notes

Bedrock disagreements from prior reviews remain bedrock and were NOT re-flagged: eliminativist "selection is folk vocabulary"; MWI-defender's "indexical question is malformed"; Buddhist deconstruction of the selecting self; Quantum Skeptic's demand for an explicit selection operator; Empiricist's "no specific predictions"; Duch's classical-neurodynamics closure (which the article already routes to the Dualism tenet rather than claiming to defeat).

Editor-internal reasoning-mode classifications, unchanged: Georgiev — Mode Three; Tegmark — Mode One/Two; Duch — Mode Three; MWI defender — Mode Three. **McQueen is not an opponent** and carries no mode; the C2 defect was a fidelity error, not a boundary substitution.

**Correction to the 2026-07-14 guidance.** That review advised excluding this article from re-review absent "a body/citation change." That rule was right and it fired correctly here — the body *and* citations had changed, the pass was substantive, and it found two critical defects. But the defects it found were **older than the change that triggered it**: C1 and C2 had been live since the 2026-04-30 create and were ratified by four reviews and a full citation audit. Convergence damping measures *self*-modification, not correctness (`convergence-damping-keys-on-self-modification-not-dependency-freshness`). A quiet article is not a verified one.