---
ai_contribution: 100
ai_generated_date: 2026-07-30
ai_modified: 2026-07-30 19:47:42+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-30
date: &id001 2026-07-30
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Quantum Holism and Phenomenal Unity
topics: []
---

**Date**: 2026-07-30
**Article**: [Quantum Holism and Phenomenal Unity](/topics/quantum-holism-and-phenomenal-unity/)
**Previous review**: [2026-07-14](/reviews/deep-review-2026-07-14-quantum-holism-and-phenomenal-unity/)
**Word count**: 3936 → 3950 (+14; prose 3281 → 3298, apparatus 655 → 652). Below the 4000 hard threshold with 49 words headroom.

Seventh consecutive deep review, targeted at the **reference apparatus** rather than the prose. The prose is converged and was left almost entirely alone; the apparatus was not. Seven of 23 references were orphans (never cited in the body), and one carried three-field-wrong metadata. Six orphans integrated, one removed, four metadata defects corrected.

**Verification method**: WebSearch was exhausted for the session, so every citation was verified through the **Crossref REST API** (title + DOI resolution), with **OpenAlex** as a second independent index. No corpus-internal grep was used as evidence, and no result hosted on unfinishablemap.org was treated as confirmation.

## §2.4 Publisher-of-Record Citation Web-Verify (per-cite ledger, 22 entries)

All verified against Crossref DOI resolution unless noted.

- **Baum, E. (2024)** (The Quantum Binding Argument, PhilArchive) — **unconfirmed at publisher**. PhilArchive mints no DOI and is not indexed by Crossref or OpenAlex. Cited consistently across five corpus articles; body correctly flags it as a non-peer-reviewed preprint. *Action*: added the missing `(2024)` year and `(preprint)` marker to the References entry, which previously carried neither while the body said "a 2024 PhilArchive preprint" — an internal inconsistency. Claim itself untouched.
- **Bayne, T. & Chalmers, D. (2003)** — **real-wrong-metadata (corrected)**. Verified via chapter DOI `10.1093/acprof:oso/9780198508571.003.0002`: "What is the unity of consciousness?", Bayne & Chalmers, in *The Unity of Consciousness: Binding, Integration, and Dissociation* (Cleeremans ed.), OUP 2003, **pp. 23-58**. The entry truncated the book subtitle and omitted pages. Both restored.
- **Dennett, D.C. (1991)** (*Consciousness Explained*) — **real-correct**. Monograph, not Crossref-indexed as such; canonical. Body names Dennett ("Dennett-style illusionists", L158), so not an orphan.
- **Denton et al. (2024)** — **real-correct**. DOI `10.1038/s41467-024-55124-x`; *Nature Communications* **15**, article **10823**, 2024-12-30; author list Denton, Smith, Xu, Pugsley, Toghill, Kattnig matches the entry exactly. **Venue check requested by the driver: inline and References agree** — the body says "in *Nature Communications*" and the References entry gives "*Nature Communications*, 15, 10823". No inline/reference venue drift. The calibrated "modelled … computational precedent … not a neural demonstration" framing was left byte-identical.
- **Frankish, K. (2016)** (Illusionism as a theory of consciousness, *JCS* 23(11-12), 11-39) — **real, corroborated but not DOI-confirmed**. JCS backfile before 2021 is not in Crossref. OpenAlex indexes the 2017 Imprint Academic book of the same name and, decisively, **Dennett's reply "Illusionism as the Obvious Default Theory of Consciousness", *JCS* 23 (2016)** — i.e. the special issue built around Frankish's target article. Metadata accepted; exact page range not independently confirmed at a publisher.
- **Hagan, Hameroff & Tuszynski (2002)** — **real-correct**. DOI `10.1103/physreve.65.061901`; *Phys. Rev. E* 65, 061901.
- **Hameroff, S. & Penrose, R. (2014)** — **real-correct**. DOI `10.1016/j.plrev.2013.08.002`; *Physics of Life Reviews* **11(1)**, 39-78, 2014.
- **Kerskens, C. M. & López Pérez, D. (2022)** — **real-correct**. DOI `10.1088/2399-6528/ac94be`; *J. Phys. Commun.* **6(10)**, 105001. Compound surname "López Pérez" confirmed correct (a standard false-fabrication trap; not one here).
- **Khan, S. … Wiest, M. C. et al. (2024)** — **real-correct**. DOI `10.1523/eneuro.0291-24.2024`; *eNeuro* 11(8). Khan-first / Wiest-senior author order re-confirmed; the earlier stale-Wiest-first correction is right and was not regressed.
- **Leibniz, G.W. (1714)** (*Monadology*) — **real-correct**; mill argument at §17. Heavily body-cited.
- **Luo et al. (2025)** — **real-correct**. Parent DOI `10.1021/jacs.5c15726`; *JACS* **147(47)**, 43934-43945. Authors Luo, Hungerland, Solov'yov, Subotnik, Hammes-Schiffer match. (A first Crossref hit resolved to the `.s001` supporting-information *component*, not the article — a near-miss that would have looked like a metadata mismatch; the parent record is clean.)
- **McKemmish et al. (2009)** — **real-correct**. DOI `10.1103/physreve.80.021912`; *Phys. Rev. E* 80(2), 021912.
- **Neven, H. et al. (2024)** — **real-correct**. DOI `10.3390/e26060460`; *Entropy* **26(6)**, 460. Neven confirmed first author (Google Quantum AI), matching the body's attribution. Note a preprints.org version also exists (`10.20944/preprints202402.1751.v1`); the article correctly cites the **published** *Entropy* record.
- **Reimers et al. (2009)** — **real-correct**. DOI `10.1073/pnas.0806273106`; *PNAS* 106(11), 4219-4224.
- **Revonsuo, A. (1999)** — **real-correct**. DOI `10.1006/ccog.1999.0384`; *Consciousness and Cognition* 8(2), 173-185.
- **Saxena, K. et al. (2020)** — **real-wrong-metadata on three fields; entry REMOVED as an orphan** (see below). Verified independently at Crossref *and* OpenAlex: the paper is "Fractal, Scale Free Electromagnetic Resonance of a Single Brain Extracted Microtubule Nanowire, **a Single Tubulin Protein and a Single Neuron**", Saxena, Singh, Sahoo, Sahu, Ghosh, Ray, Fujita, Bandyopadhyay, ***Fractal and Fractional* 4(2), 11**, DOI `10.3390/fractalfract4020011`. The entry gave ***ACS Nano*, 14(2), 2217-2227** — wrong venue, wrong volume, wrong issue, wrong pages, plus a truncated title. Control check: DOI `10.1021/acsnano.9b09163` confirms *ACS Nano* 14(2) at that page region is unrelated content ("Near-Atomic Fabrication with Nucleic Acids", pp. 1319-1337).
- **Schlosshauer, M. (2019)** — **real-correct**. DOI `10.1016/j.physrep.2019.10.001`; *Physics Reports* 831, 1-57.
- **Singer, W. (1999)** — **real-correct**. DOI `10.1016/s0896-6273(00)80821-1`; *Neuron* 24(1), 49-65.
- **Tegmark, M. (2000)** — **real-correct**. DOI `10.1103/physreve.61.4194`; *Phys. Rev. E* 61, 4194-4206.
- **Tononi, G. (2008)** — **real-wrong-metadata (corrected)**. DOI `10.2307/25470707`; the full title is "Consciousness as Integrated Information: **a Provisional Manifesto**", *Biological Bulletin* **215(3)**, 216-242. The entry truncated the title and omitted the issue. Both restored.
- **Vicente et al. (2008)** — **real-correct**. DOI `10.1073/pnas.0809353105`; *PNAS* **105(44)**, 17157-17162; authors Vicente, Gollo, Mirasso, Fischer, Pipa match the entry exactly. This is the load-bearing zero-lag refutation and it is sound.
- **Warren, W. (2023)** — **real-correct**. DOI `10.1088/2399-6528/acc4a8`; *J. Phys. Commun.* **7(3)**, 038001. (Publisher's title uses singular "brain function"; immaterial.)
- **Wiest, M. C. (2025)** — **real-wrong-metadata (corrected)**. DOI `10.1093/nc/niaf011`; *Neuroscience of Consciousness* **2025(1)**, niaf011. The entry truncated the title mid-claim: the full title is "A quantum microtubule substrate of consciousness is experimentally supported **and solves the binding and epiphenomenalism problems**". The dropped clause is directly about binding — the article's own subject — so the truncation understated what the cited paper asserts. Restored, along with the missing issue.

**Not re-litigated**: the Khan 2024 body figures (69 s LORR delay, Cohen's *d* = 1.9) and the Tegmark/Hagan coherence ranges were verbatim-verified at the publisher in the 2026-07-14 pass and the surrounding body text is unchanged since (the only intervening edit was "seven" → "eight to nine orders of magnitude", commit `9d460032c`, which is arithmetically correct: 10⁻¹³ → 10⁻⁵/10⁻⁴).

**Empirical-record currency sweep**: `find_superlative_claims` surfaced no unhedged superlatives requiring re-verification. The one superlative-shaped phrase, "the physical structure that **most closely** mirrors phenomenal unity", is a comparative internal to the Map's own argument and is explicitly tenet-grounded at both loci ("a claim the Map advances on tenet grounds, not one forced by the data"). Not an empirical record claim; no currency risk.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Seven orphan references (23 → 22 entries, all now bidirectionally closed).** An academic apparatus in which 30% of entries are never cited is an apparatus defect: it inflates the appearance of support without supplying it, and it disguises which body claims are actually unsupported. The driver flagged six on a first-author-surname test; a seventh was hidden because the surname test gives a **false pass** when a body mention refers to a *different* paper by the same author. Per-entry verdicts:

  | Reference | Verdict | Rationale |
  |---|---|---|
  | Revonsuo (1999) | **Integrated** | The article's BP1/BP2 framing device *is* Revonsuo's distinction, and his 1999 paper is titled precisely "Binding and the phenomenal unity of consciousness". The Map's whole structural argument runs on this distinction and it was stated with no attribution. Attached at first use. |
  | Bayne & Chalmers (2003) | **Integrated** | The canonical analysis of phenomenal unity. Attached to the sentence that states their definition almost verbatim ("something it is like to have *all of them together* irreducible to what it is like to have each separately"). |
  | Singer (1999) | **Integrated** | Attached to "the most prominent neural account" of gamma-synchrony binding — Singer is that account's principal proponent, and the claim was previously an unattributed appeal to authority. |
  | Tononi (2008) | **Integrated** | Attached to the IIT/Φ statement. The IIT section previously named the theory only through a wikilink, so its central claim had no source. |
  | Frankish (2016) | **Integrated** | Attached at the head of "The Illusionist Challenge". Frankish's paper is the target article that named the position the section spends 400 words rebutting. |
  | **Hameroff & Penrose (2014)** | **Integrated** (7th orphan — missed by the surname test) | "Hameroff" appears in the body only inside the *Hagan et al. 2002* author list, and "Penrose" never appears in body prose at all, so the surname test passed on a mention of a different paper. This was the highest-value fix: the article stated the **Orch OR** mechanism in full ("microtubules sustain entangled superpositions… each objective reduction constitutes a moment of experience") as an unattributed conditional. Naming a well-known theory without attributing it is an unsupported-claim gap independent of the orphan issue. Now reads "—Hameroff and Penrose's Orch OR proposal (2014)—". |
  | Saxena et al. (2020) | **Removed** | The only entry with **no body claim to attach to**. The article makes no microtubule electromagnetic-resonance claim anywhere; the decoherence section's biological precedent runs through avian magnetoreception (Luo 2025), a different mechanism. Manufacturing a claim to justify the entry would have meant asserting EM resonance as evidence for *quantum coherence* — precisely the "coherence-vs-EM-resonance overstatement" that [deep-review-2026-07-22-entanglement-binding-hypothesis](/reviews/deep-review-2026-07-22-entanglement-binding-hypothesis/) declined to risk. Compounding this, its metadata was wrong on venue, volume, issue and pages (see ledger). Removal both closes the orphan and deletes a false citation. |

- **Wiest (2025) title truncation dropped a substantive clause.** Cutting "and solves the binding and epiphenomenalism problems" from the title understated the cited paper's scope on the very question the article is about. This is a metadata error rather than a philosophical one, and correctable. Fixed.

### Medium Issues Found

- **Kerskens/López Pérez debate is presented one-sidedly (deferred, funded-by-nothing).** The body gives Warren's (2023) methodological challenge and concludes "The debate remains open" — but Kerskens & López Pérez published a **formal Reply** (*J. Phys. Commun.* 7(3), **038002**, DOI `10.1088/2399-6528/acc636`, verified this pass). The existing wording is not false, and the omission runs *against* the Map's own interest rather than for it, so it is not a calibration error. It is nonetheless an incompleteness. **Deferred on length grounds**: adding the reply plus its References entry costs ~33 words against 49 remaining headroom, which would leave the next review with none. Recorded here so it is not rediscovered as novel.

### Low Issues Found

- **Corpus-wide Saxena metadata family (out of scope for this file; reported, not silently propagated).** The same paper is cited with **four mutually incompatible venues** across the corpus, none of which is the verified one (*Fractal and Fractional* 4(2), 11):
  - `obsidian/concepts/binding-problem.md:243` — *ACS Nano*, 14(2), **1403-1411**
  - `obsidian/concepts/entanglement-binding-hypothesis.md:135` — ***AIP Advances***, 10(1), 015114
  - `obsidian/research/quantum-superposition-brain-consciousness-2026-01-18.md:250` and three `archive/` files — "*Long-range quantum coherence in microtubules at room temperature*, **arXiv preprint**" (a different, likely non-existent title)
  - `archive/concepts/quantum-binding-experimental-evidence.md` (hugo) — "*Long-lived quantum coherences in room-temperature biological systems*, ***Scientific Reports*** 10, 15436"

  This is a textbook family-resolution case: the variants ratify each other on intra-corpus grep and only publisher resolution separates them. It needs a single corpus-wide propagation pass, which is beyond this file's scope and beyond its word budget. Not actioned here; flagged for the operator.

### Calibration Check (possibility/probability slippage)

Diagnostic test applied — *would a reviewer who fully accepts the Map's tenets still flag any claim as overstated?* **No.** The framework-stage spine is intact and untouched at all four load-bearing loci: the lead's "a claim the Map advances on tenet grounds, not one forced by the data"; L104's "one candidate among several rather than an established result … posited on tenet grounds (Minimal Quantum Interaction) rather than forced by the data"; L128's "The dispute is live, not closed; citing Hagan as a settled rebuttal would be selective citation"; and the close's "a realistic candidate—motivated by structural fit and biological precedent rather than settled by current evidence". The two families the driver pre-cleared were re-read and confirmed correctly calibrated; neither was reopened.

Notably, the *removal* of the Saxena entry improves calibration: an uncited reference in a decoherence-adjacent apparatus reads as unspecified experimental backing for coherence claims that the article, in its body, is careful **not** to make.

### Quote-Fidelity (AXIS 4)

Re-scanned every quoted span. All remain scare-quotes or conceptual labels ("red", "round", "the phrase", "wholes", "observations", "emerges", "one thing") or standard Whitehead vocabulary ("actual occasions", "concrescence", "prehensions", "satisfaction"). Neven's "only true binding agent in physics" remains prose paraphrase, not a marked verbatim quotation, and is explicitly framed as an interpretive commitment. **No new quoted span was introduced by this pass** — all six integrations are bare author-year parentheticals, which cannot break grep-contiguity. Clean.

### Counterarguments Considered

All six adversarial personas re-engaged against the modified text. No new critical issues. The catalogued bedrock disagreements are unchanged and were not re-flagged: eliminativist denial that phenomenal unity is a natural kind; Dennett on the holism premise; Tegmark on decoherence (engaged Mode One, with the Reimers/McKemmish counter-counter left standing); Deutsch/MWI on haecceity; Popper on falsifiability (the five-condition section is intact); Nagarjuna on contemplative testimony.

## Reasoning-Mode Classification (editor-internal; grep-verified no label leakage)

- **Tegmark / decoherence**: Mode One — engages Tegmark's own model with corrected parameters, then marks the live Reimers/McKemmish dispute honestly.
- **Baum (the Map's *own* side)**: Mode One turned inward — the article refutes an argument that favours its conclusion, on peer-reviewed classical grounds. Unchanged and exemplary.
- **IIT (Tononi)**: Mode Two — "definitional solutions relabel rather than explain" invokes IIT's own commitment to explanation. Strengthened this pass only by naming the source.
- **Classical-binding / functionalist**: Mixed — Leibniz-mill opens, intrinsic-singularity boundary-marking closes.
- **Illusionists (Frankish, Dennett)**: Mixed — three in-framework arguments, with the "coherent, but its cost is…" concession marking the residue honestly rather than claiming refutation.
- **MWI defenders**: Mode Three — correctly placed in the No-Many-Worlds tenet section as a haecceity commitment.

Grepped the body for all forbidden editor-vocabulary labels (`direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `Engagement classification:`, `Evidential status:`): **zero hits**. No boundary-substitution introduced.

## Nav-Surface Check

- `title:` "Quantum Holism and Phenomenal Unity" — matches the body's scope.
- `description:` — "Quantum entanglement is the most promising physical **mirror** of phenomenal unity" is calibrated correctly: "mirror" tracks the body's "resembling it … rather than a substrate that constitutes it", and does not assert the constitutive claim the Leibniz argument forbids and the body explicitly disclaims. Its first clause ("classical mechanisms coordinate separate processes but cannot make them one") is consistent with L68's concession that the *temporal synchrony* is classically explicable — the description claims only the unity failure, which is the claim the article actually defends. **No nav-surface overclaim.**
- All link aliases checked against their targets (`[[unity-of-consciousness|Phenomenal unity]]`, `[[illusionism|Illusionists]]`, `[[haecceity|Indexical identity]]`, `[[radical-pair-magnetoreception|Avian magnetoreception]]`, `[[zero-lag-gamma-synchrony-and-the-quantum-binding-argument|Zero-lag gamma synchrony]]` and the rest): all accurate.
- Every `[[wikilink]]` target resolves on disk, and all five `[[tenets#^…]]` anchors (`^dualism`, `^minimal-quantum-interaction`, `^bidirectional-interaction`, `^no-many-worlds`, `^occams-limits`) were confirmed present in `obsidian/tenets/tenets.md`. No push-blocking link.

## Optimistic Analysis Summary

### Strengths Preserved (untouched)

- Front-loaded summary survives truncation; the BP1/BP2 division-of-labour framing remains the article's most distinctive contribution.
- "The Remaining Gap" is a model of intellectual honesty — quantum holism relocates rather than dissolves the hard problem, and the section says so plainly.
- The zero-lag passage refutes an argument that would have *helped* the Map, citing peer-reviewed work against a sympathetic preprint. Rare and worth protecting.
- The Decoherence Debate holds Hagan's correction, its rebuttals, and the selective-citation disclaimer simultaneously.
- Five-condition falsifiability section intact; all five tenets engaged substantively.

### Enhancements Made

- Six orphan references integrated at the exact claims they support, converting decorative apparatus into actual support — most consequentially the Orch OR attribution, which closed a genuine unsupported-claim gap.
- One false citation (Saxena) removed.
- Four reference-metadata defects corrected (Baum year, Bayne & Chalmers subtitle + pages, Tononi title + issue, Wiest title + issue).

### Cross-links

None added. The article is already densely connected (19 concepts, 5 related articles, 16 Further Reading entries) and is at 132% of soft threshold; adding links would cost words for no structural gain.

## Remaining Items

1. **Kerskens & López Pérez (2023) Reply** — optional balance addition, ~33 words, deferred on length grounds. Verified real: *J. Phys. Commun.* 7(3), 038002, DOI `10.1088/2399-6528/acc636`.
2. **Corpus-wide Saxena et al. (2020) family resolution** — four wrong-venue variants across `concepts/`, `research/` and `archive/`; canonical form is *Fractal and Fractional* 4(2), 11, DOI `10.3390/fractalfract4020011`. Needs a dedicated propagation pass.
3. **Frankish (2016) page range** — accepted on strong corroboration, not publisher DOI. Worth one confirmation if a WebSearch budget is ever available.

## Stability Notes

Seventh consecutive review. **The prose is converged; the apparatus was not, and that asymmetry is the lesson.** Six reviews found the body sound and reported the citations "verified" without ever testing whether the References entries were *used*, or whether their metadata survived publisher resolution. Both tests failed on first application.

Standing do-NOT-re-flag list (carried forward and re-confirmed):

1. Bedrock disagreements — functionalist denial of the holism premise, MWI denial of haecceity, eliminativist denial that phenomenal unity is a natural kind — remain bedrock, not defects.
2. The decoherence timing gap (three orders short of ~300 ms) is honestly acknowledged by design.
3. The framework-stage-calibration spine and the evidential-status hedges are deliberate; do not "tighten" them.
4. The Baum/Vicente zero-lag passage and the Denton "modelled … not a neural demonstration" passage are **correctly calibrated and byte-identical to their pre-review state**. Do not reopen either.
5. "Eight to nine orders of magnitude" (Tegmark → Hagan) is arithmetically correct and supersedes the older "seven"; do not revert.

**Citation watch**: all 22 remaining references verified this pass at Crossref/OpenAlex with the ledger above, and the apparatus is now bidirectionally closed (every entry cited inline; every inline cite has an entry). Future reviews may treat these as settled **unless the References block changes**. Two entries carry an explicit caveat and should not be re-verified as though clean: **Baum** (unconfirmable — PhilArchive has no DOI) and **Frankish** (corroborated, not DOI-confirmed).

**Length watch**: 3950 words — 49 below the 4000 hard threshold. The next substantive addition must be funded by a cut. The apparatus is now lean (652 words) and further trimming there would remove real support, so any future condense should target prose redundancy — while noting that the duplicated "most closely mirrors … rather than a substrate that constitutes it" calibration at the lead and at "The Remaining Gap" is **deliberate reinforcement, not redundancy**, and must not be collapsed.