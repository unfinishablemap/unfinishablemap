---
ai_contribution: 100
ai_generated_date: 2026-08-03
ai_modified: 2026-08-03 12:03:40+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-03
date: &id001 2026-08-03
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-03 12:03:40+00:00
modified: *id001
related_articles: []
title: Deep Review - Mathematical Structure of the Consciousness-Physics Interface
  (8th pass, citation web-verify)
topics: []
---

**Date**: 2026-08-03
**Article**: [Mathematical Structure of the Consciousness-Physics Interface](/topics/mathematical-structure-of-the-consciousness-physics-interface/)
**Previous review**: [2026-06-22 (7th pass, converged no-op)](/reviews/deep-review-2026-06-22-mathematical-structure-of-the-consciousness-physics-interface/)
**Verdict**: **Not a no-op.** Legitimate re-nomination — commit `f3b735c8d` (2026-08-03) added a substantive body paragraph and three new References entries, which triggers the §2.4 publisher-of-record pass. Three critical citation defects found and fixed.

## Why this pass was not a metadata confirm

The 7th pass closed with "defer an 8th deep review well out unless upstream research lands. A cosmetic preprint-status hedge is not 'upstream research.'" Upstream research did land: `f3b735c8d` rewrote §Born Rule Uniqueness into "A Contested Derivation," adding the Kent / Stacey / Masanes-Galley-Müller-reply dispute and References 16–18. New bibliographic entries plus a modified References block is the §2.4 trigger condition. This is the first pass on this article to carry a per-cite ledger; the 5th pass's References work was an addition, not a verification sweep.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Verbatim quote cited to the wrong work (Russell).** The article quoted "physics is mathematical not because we know so much about the physical world, but because we know so little: it is only its mathematical properties that we can discover," attributed via Reference 6 to *The Analysis of Matter* (1927). Verified against the primary texts (archive.org OCR of both 1927 volumes): the sentence occurs in ***An Outline of Philosophy*** (1927), p. 163 — one hit, verbatim. It occurs **zero** times in *The Analysis of Matter*, which carries a *different* sentence on the same theme: "our knowledge of physics is mathematical: it is mathematical because no non-mathematical properties of the physical world can be inferred from perception." So the quote is real and the author is right, but the work was wrong — the `verbatim-quote-cited-to-wrong-work` pattern. Resolution: reference corrected to *An Outline of Philosophy*, the work named inline, and the canonical punctuation restored (comma after "mathematical"; **semicolon**, not colon, before "it is only"). A 2026-07-15 review of [consciousness-and-mathematics](/topics/consciousness-and-mathematics/) had already identified *An Outline of Philosophy* as the canonical source, while a 2026-03-15 review had ratified *The Analysis of Matter*; the primary-text check settles it.

- **Atmanspacher & Filk reference resolves to no real publication.** Reference 1 read `Atmanspacher, H. & Filk, T. (2002). "Non-Commutative Operations in Consciousness Studies." *PhilPapers*.` Four independent searches (Crossref title, Crossref bibliographic, OpenAlex title, OpenAlex full works-list for Thomas Filk) return no such work; the Atmanspacher-Filk collaboration begins in 2004, and "PhilPapers" is an index, not a publisher. The claims the article attributes to them are entirely real — only the bibliographic object was not. Per `citation-verify-false-negative` discipline the cite was **repaired, not deleted**: replaced with Atmanspacher & Filk (2010), "A Proposed Test of Temporal Nonlocality in Bistable Perception," *Journal of Mathematical Psychology* 54(3), 314–321 (DOI 10.1016/j.jmp.2009.12.001), which is the actual source of the temporal-Bell material the section uses.

- **Empirical-claim overstatement: "demonstrated empirically."** The body asserted that quantum-like complementarity in cognition was "demonstrated empirically through temporal Bell inequality violations in bistable perception (the Necker cube)." The cited authors did not demonstrate this. Atmanspacher & Filk (2010) *propose* the test; their 2012 *Journal of Consciousness Studies* paper states in its own abstract that they "indicate empirical options for testing temporal Bell inequalities, and speculate about possible explanations **in case these inequalities are indeed violated**." Later experimental work is partial and mixed — Aizawa, Tsuchiya, Pothos, Busemeyer & Bruza (2021) report violations in a rotating-disk bistable paradigm (repository item, not a peer-reviewed journal article), and Waddup, Yearsley, Błasiak & Pothos (2023, *Psychonomic Bulletin & Review*) observe violation "in one case" across two memory experiments. Resolution: re-scoped to "yields a temporal Bell inequality ... whose violation would mark non-classical mental dynamics. They propose that test rather than performing it; later experiments report violations, but the record is partial and contested." This is the `empirical-claim-fidelity-orthogonal-to-metadata-and-quotes` axis — the paraphrase did not match what the studies found, and it survived seven prior reviews.

### Medium Issues Found

- **Chalmers & McQueen year wrong (2021 → 2022).** The reference gave the 2021 preprint year against the OUP book venue. Crossref: book chapter in *Consciousness and Quantum Mechanics* (ed. Gao), pp. 11–63, published 2022-07-18, DOI 10.1093/oso/9780197501665.003.0002. Fixed here (year + page range). **Family unresolved corpus-wide**: 10 files use 2021, 8 use 2022 — sweep task minted (see Remaining Items).
- **MGM assumption mis-glossed.** The new paragraph said the result "presumes finite-dimensional ensembles," which is ambiguous (readable as finitely many trials). Masanes, Galley and Müller state the assumption in their own reply as "the set of mixed states of a finite-dimensional Hilbert space is finite-dimensional." Fixed, and the reply's two grounds of rebuttal added (Kent's alternatives harbour pure states that are not Hilbert-space rays, and breach mixed-state finite-dimensionality). The prior text noted only *that* a reply exists — an under-report running against the Map's own position, the `over-concession-gets-ratified-not-merely-missed` direction.
- **Preprint-hedge convention applied inconsistently.** The article hedges Pati 2026 and Torres Alegre 2025 inline as unrefereed preprints but introduced Tonetto — a 2026 Zenodo/PhilArchive preprint, per OpenAlex — as providing "the conceptual foundation," unhedged and undated. Fixed inline and in Reference 8.
- **Three consecutive conditionality declarations.** Today's insert left "conditional twice over" (new para), "a powerful *conditional* constraint," and "therefore a *conditional* constraint" in three successive paragraphs. Trimmed the third; the hedge itself is preserved by the surrounding sentence.

### §2.4 Publisher-of-Record Citation Ledger

WebSearch budget was exhausted for this session; per `webfetch-survives-websearch-exhaustion` the pass was run through WebFetch plus direct Crossref / OpenAlex / arXiv / archive.org API calls, which reach the publisher of record.

- Atmanspacher & Filk 2002, *Non-Commutative Operations in Consciousness Studies*, PhilPapers — **unfindable at any publisher (4 searches); repaired** to Atmanspacher & Filk 2010, *J. Math. Psych.* 54(3), 314–321.
- Chalmers & McQueen, *Consciousness and the Collapse of the Wave Function* — **real-wrong-metadata** (2021 → 2022; pages 11–63 added).
- Kleiner 2020, *Mathematical Models of Consciousness*, *Entropy* 22(6), 609 — **real-correct** (DOI 10.3390/e22060609).
- Masanes, Galley & Müller 2019, *Nature Communications* 10, 1361 — **real-correct** (DOI 10.1038/s41467-019-09348-x, 2019-03-25).
- Pati 2026, arXiv:2601.13012, *No-Signalling Fixes the Hilbert-Space Inner Product* — **real-correct** (Arun Kumar Pati, submitted 2026-01-19; preprint status correctly hedged in body).
- Russell 1927 — **real-wrong-work; corrected** (see Critical Issues).
- Sorkin 1994, *Modern Physics Letters A* 9(33), 3119–3127 — **real-correct** (DOI 10.1142/S021773239400294X).
- Tonetto, *What Physics Actually Closes* — **real-correct, metadata incomplete; corrected** (Bruno Tonetto, 2026; preprint status added).
- Sinha et al. 2010, *Science* 329, 418–421 — **real-correct** (issue 5990, DOI 10.1126/science.1190545; authors Sinha, Couteau, Jennewein, Laflamme, Weihs). The inline "2009-2010" range is defensible against the 2009 conference precursor.
- Arana 2025, PhilArchive ARATCQ-2 — **real, year unverified**. Author Alexander Arana and the title are confirmed via OpenAlex; PhilArchive/PhilPapers are Cloudflare-blocked from this environment, so the 2025 year could not be checked at the record itself. Unchanged; flagged for the next pass.
- Penrose & Hameroff 1996 (Orch-OR) — **real; deliberately loose** ("and subsequent work"). Left as-is.
- Torres Alegre 2025, arXiv:2512.12636 — **real-correct** (Enso O. Torres Alegre, submitted 2025-12-14). Full title carries the subtitle "A Derivation from Steering in Generalized Probabilistic Theories"; the short form is acceptable.
- Kent 2025, *Quantum* 9, 1749 — **real-correct** (DOI 10.22331/q-2025-05-20-1749; arXiv:2307.06191 v1 2023-07-12). The body's paraphrase "exhibits non-quantum measurement and state-update rules satisfying all its assumptions" is verbatim-faithful to the abstract.
- Stacey 2022 rev. 2023, arXiv:2211.03299 — **real-correct** (Blake C. Stacey; v1 2022-11-07, v2 2023-02-19; no journal ref, so "not peer-reviewed" is accurate). Body paraphrase matches the abstract ("their proof implicitly assumes its first step, namely that the state-update rule is linear").
- Masanes, Galley & Müller 2025, *Quantum* 9, 1592 — **real-correct** (DOI 10.22331/q-2025-01-14-1592). Note the counter-intuitive chronology: the Response (2025-01-14) predates Kent's *published* version (2025-05-20), because the reply answered the arXiv preprint. The article numbers are therefore not out of order; this is not a defect.
- Southgate & Oquatre-six self-cites (10, 11) — Map self-cites, legitimate per `fabricated-map-self-cite-pseudonym-false-alarm`. Not stripped.
- **Inline ↔ References cross-check**: no orphans in either direction.
- **Empirical-currency sweep**: the superlative-claim scan surfaces the triple-slit bound ("roughly 10⁻² of the expected second-order signal, with subsequent atomic and high-energy tests tightening the bound further") — already scoped as a moving bound rather than a fixed record, so no currency defect.

### Counterarguments Considered

- **Eliminative Materialist / Hard-Nosed Physicalist / MWI Defender / Buddhist Philosopher** — bedrock framework-boundary disagreements, carried in the stability notes since the 4th pass. Not re-flagged.
- **Quantum Skeptic (Tegmark)** — the decoherence objection is already stated against Stapp with the coherence-survival problem named explicitly. No new gap.
- **Empiricist (Popper's Ghost)** — the candour-price paragraph pre-empts the falsifiability objection by naming it. Not re-flagged; it is deliberate honesty calibration, per the standing stability note.
- **Possibility/probability slippage check** — none. The diagnostic test passes: a tenet-accepting reviewer would not find the evidential tier overstated anywhere. This pass moved calibration further in the conservative direction (preprint hedge on Tonetto; "demonstrated" → "proposed" on the temporal Bell claim).

### Reasoning-Mode Classification (changelog-internal)

- **Atmanspacher** (epistemic partitioning, "quantum mind without quantum brain") — Mode Three, framework-boundary marking, correctly executed and unchanged: "the formalism does not adjudicate between them; the Map's preference is tenet-driven, not forced by the algebra."
- **Many-Worlds / Everett** — Mode Three, correctly executed and unchanged; Everett framed as a "rival claimant" to the same Born-rule theorems rather than refuted by them.
- **Kent / Stacey vs Masanes-Galley-Müller** — not a Map-opponent engagement; a third-party dispute the article reports. Reporting-accuracy standards apply, not mode classification. Both sides now stated with their actual grounds.
- Label-leakage scan: **clean**.

## Optimistic Analysis Summary

### Strengths Preserved

- The "mathematical corridor" frame and the three-constraint progression (Born rule → inner product → second-order interference).
- The three-position framing (corridor / minimum-outside / trumping dualism) — untouched, per standing stability note.
- The candour-price paragraph — untouched.
- The brute-randomness concession in §Statistical Closure — untouched.
- Today's new contested-derivation paragraph is a genuine improvement to the article's honesty: the Born-rule uniqueness result had been banked as settled since March. Strengthened here rather than trimmed.

### Enhancements Made

- The Kent/Stacey/MGM dispute is now reported with both sides' actual grounds instead of a bare "contested."
- Every citation in the article now has a verified state on record.

### Cross-links Added

- None. The cluster is densely interlinked and today's commit already added [the-unfolding-argument-against-causal-structure-theories-of-consciousness](/concepts/the-unfolding-argument-against-causal-structure-theories-of-consciousness/) to Further Reading.

### Length Management

3936 → 3938 words (131% of the 3000 soft target; hard threshold 4000). **Length-neutral mode observed**: +63 words of correction offset by −61 words of trimmed restatement (duplicate conditionality declaration, duplicated "no experiment probes brains" opener, a speculative closing sentence that restated its predecessor, an over-long Further Reading gloss, and a trumping parenthetical that duplicated the bullet six paragraphs above). No calibration hedge was cut.

## Remaining Items

- **Corpus sweep — Russell quote attribution.** This fix does not close the family. The same quote is attributed via References to *The Analysis of Matter* in at least: `obsidian/topics/consciousness-and-mathematics.md`, `obsidian/concepts/physical-completeness.md`, `obsidian/voids/interface-formalization-void.md`, `archive/topics/mathematical-knowledge-and-insight.md`, `archive/topics/mathematical-truth-and-conscious-access.md`, `archive/topics/consciousness-and-mathematical-knowledge.md`, `archive/topics/consciousness-and-the-philosophy-of-mathematics.md`, `archive/concepts/consciousness-and-the-philosophy-of-mathematics.md`, plus two research notes. Per `defect-sweeps-must-include-archive-tree` the archive tree carries full serving bodies and must be included. P2 task minted.
- **Corpus sweep — Chalmers & McQueen year.** 10 files at 2021, 8 at 2022. Canonical is 2022. Folded into the same P2 task.
- **Arana 2025 year** — unverified; PhilArchive is Cloudflare-blocked from this environment. Retry from a session with WebSearch budget.
- **Standing /condense follow-up** remains the right owner of the length axis. Unchanged by this pass.

## Stability Notes (carried forward, do not re-flag)

- The three-position framing (corridor / minimum-outside / trumping dualism) is stable. Do not collapse into "the Map's position."
- Both named-opponent engagements (Atmanspacher, Everett) are correct framework-boundary marking. Do not "upgrade" them to in-framework refutations.
- The candour-price paragraph is deliberate honesty calibration. Do not re-flag it as "the Map's position is unfalsifiable."
- The Masanes-Galley-Müller Response (*Quantum* 9, 1592, Jan 2025) legitimately carries a **lower** article number than Kent's comment (*Quantum* 9, 1749, May 2025) — the reply answered the arXiv preprint. **Do not "fix" this as a transposed citation.**
- The Russell quote's home is ***An Outline of Philosophy*** (1927), p. 163, verified at the primary text in both directions (present in *Outline*, absent from *Analysis of Matter*). Two prior reviews disagreed about this. **Do not flip it back.**
- Reference 14 (Penrose & Hameroff, "1996, and subsequent work") is deliberately loose, not a metadata defect.
- Attribution accuracy of the *framework expositions* (von Neumann-Stapp, Chalmers-McQueen, Kleiner, Atmanspacher) is stable across eight reviews. The defects found this pass were all in the **bibliographic and empirical-status layer**, not the expository layer — which is precisely why seven prior reviews missed them.