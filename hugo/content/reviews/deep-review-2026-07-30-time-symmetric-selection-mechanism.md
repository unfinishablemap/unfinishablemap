---
ai_contribution: 100
ai_generated_date: 2026-07-30
ai_modified: 2026-07-30 11:48:15+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-30
date: &id001 2026-07-30
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-30 11:48:15+00:00
modified: *id001
related_articles: []
title: Deep Review - Time-Symmetric Selection Mechanism
topics: []
---

**Date**: 2026-07-30
**Article**: [Time-Symmetric Selection Mechanism](/topics/time-symmetric-selection-mechanism/)
**Previous review**: [2026-07-15](/reviews/deep-review-2026-07-15-time-symmetric-selection-mechanism/)
**Word count**: 2777 → 2999 total (prose +~85, apparatus 369 → 500 for four newly-required References entries); status `ok` both before and after

## What ran this pass, and what the prior ledgers already covered

The 2026-06-04 review ran a full publisher-of-record **metadata** verify on all nine citations (3-state, per-cite). The 2026-07-15 review ran **quote-fidelity**, **currency-sweep** and **citation-framing** and found all three clean. Both findings substantially hold and were not re-litigated.

What neither pass ran is **claim-match at the level of what each paper actually establishes** — whether the proposition the citation is bolted to is the proposition the paper supports. 06-04 verified that Cramer 1986 *is* Rev. Mod. Phys. 58(3):647; it did not ask whether the 1964 ABL paper does the work the article credits it with. 07-15's framing pass checked whether skeptics were co-opted as allies (they were not) but did not check whether a *formalism* was credited with an *ontological* result. That gap is where this pass found three critical defects.

Quote-fidelity was re-confirmed rather than re-run: `grep -o '"[^"]\{25,\}"'` returns only the frontmatter `title`/`description` and the SEP entry title. There are **zero external verbatim quotations** in the body — every quoted string is a scare-quoted term of art ("handshakes", "offer waves", "readiness potentials", "become real", "late", "crystallisation", "timeless"). The brief's estimate of "~7 quoted spans of ≥30 chars" did not match the file. One new quotation was *introduced* by this pass and is grep-verified contiguous (below).

## Critical Issues Found

### C1. TSVF presented as establishing retrocausality — contradicted by two of the article's own References. FIXED.

Line 69 read: *"TSVF enables 'weak measurements' … **and it makes retrocausality mathematically explicit rather than interpretive**."*

This is source/Map conflation of the exact kind §2.5 targets, and it is refuted by two sources sitting in the article's own bibliography:

- The SEP entry the article cites states that the TSVF's "emphasis … is on the operational elements of the theory, and there are very few ontological prescriptions, including how best to understand causality. It is in principle compatible with a variety of supplemented retrocausal ontologies." Compatible-with-when-supplemented is the opposite of *mathematically explicit*.
- Price (2012) — also in the References — asks the question in his title and answers "Maybe", affirmatively only under additional assumptions about quantum ontology. Price also has a companion paper, *Time-symmetry without retrocausality*, arguing the other side.
- Aharonov & Vaidman's own TSVF reviews make no retrocausal-causation claim; they describe a time-symmetrised re-description of standard QM.

The retrocausal reading is the Map's interpretive addition. Rewritten to say so explicitly, quoting the SEP verbatim and citing Price's actual answer. This does not weaken the article — it relocates the commitment to where it belongs and inoculates the section against the "physics forces our conclusion" reading.

### C2. TSVF and weak measurements mis-attributed to Aharonov, Bergmann & Lebowitz (1964). FIXED.

Line 64 read: *"Aharonov, Bergmann, and Lebowitz (1964) **developed** the Two-State Vector Formalism (TSVF)"*, and the paragraph then credited that citation with enabling weak measurements.

Web-verified attribution chain:
- ABL 1964 (Phys. Rev. 134(6B):B1410) supplies the **ABL rule** — a time-symmetric probability formula for a measurement conditioned on earlier and later outcomes. Vaidman's own review says TSVF "originated in" ABL; it does not say ABL developed it.
- The **two-state vector itself** ⟨Φ‖Ψ⟩ was formulated in Aharonov & Vaidman (1990), *Phys. Rev. A* 41(1):11–20.
- **Weak measurements / weak values** arrived in Aharonov, Albert & Vaidman (1988), *Phys. Rev. Lett.* 60(14):1351–1354 — 24 years after the cited paper. Vaidman's review: "The most important outcome of the TSVF is the discovery of weak values," citing AAV 1988.
- Additionally, the article's own cited SEP entry says the formalism "was first proposed by Watanabe (1955), and then **rediscovered** by Aharonov, Bergmann, and Lebowitz (1964)" — so "developed" contradicts the article's own source twice over.

Rewritten to attribute each element to the paper that produced it; AAV 1988 and Aharonov & Vaidman 1990 added to References.

### C3. Photosynthetic coherence claim superseded by the post-2017 literature. FIXED.

Line 129, response (3) to the decoherence challenge, read: *"Biological quantum effects (avian magnetoreception, photosynthetic energy transfer) **demonstrate** evolution's capacity to exploit coherence."*

`find_superlative_claims` returns **zero** for this file, so this defect is invisible to the currency helper — "demonstrate" is not a superlative. It is nonetheless a textbook `empirical-record-currency-drift` case, verified at the publisher:

Duan, Prokhorenko, Cogdell, Ashraf, Stevens, Thorwart & Miller (2017), *PNAS* 114(32):8493–8498, DOI 10.1073/pnas.1702261114 — titled, in full, **"Nature does not rely on long-lived electronic quantum coherence for photosynthetic energy transfer."** The abstract reports 2D photon-echo spectra that "do not provide evidence of any long-lived electronic quantum coherence" and "confirm the orthodox view of rapidly decaying electronic quantum coherence on a timescale of 60 fs", concluding electronic coherence "plays no biofunctional role in photoactive biomolecular complexes." Corroborated by Cao et al. (2020, *Sci. Adv.* 6:eaaz4888) and Thyrhaug et al.: the long-lived FMO beats of Engel et al. 2007 are now attributed to **vibrational**, not electronic, coherence, and incoherent exciton transport has been re-established as the working paradigm.

This over-claim ran *in the Map's favour*, which is exactly the direction that most needs correcting. Re-scoped: avian magnetoreception (radical-pair mechanism) named as the surviving strongest case; photosynthesis explicitly withdrawn with the citation. **This locus recurs corpus-wide — see Remaining Items.**

## Per-cite web-verify ledger (claim-match focus)

| Cite | Source read | Verdict |
|---|---|---|
| Aharonov, Bergmann & Lebowitz 1964 | Vaidman TSVF reviews (arXiv quant-ph/0105101, ar5iv 0706.1347); SEP `qm-retrocausality` | **real-wrong-claim-match** — supplies the ABL rule, did not develop TSVF, predates weak measurements by 24 years. Re-attributed (C2) |
| Aharonov, Albert & Vaidman 1988 | PRL 60(14):1351–1354, DOI 10.1103/PhysRevLett.60.1351 | real-correct — **newly added**; the actual weak-value paper |
| Aharonov & Vaidman 1990 | Phys. Rev. A 41(1):11–20 | real-correct — **newly added**; the actual two-state-vector paper |
| Cramer 1986 | Rev. Mod. Phys. 58:647–688 | real-correct; claim-match **confirmed** — "handshake" between retarded (offer) and advanced (confirmation) waves is Cramer's own framing |
| Duan et al. 2017 | PNAS 114(32):8493–8498, DOI 10.1073/pnas.1702261114, PMID 28743751 | real-correct — **newly added** to support C3 |
| Friederich & Evans 2023 (SEP) | plato.stanford.edu/entries/qm-retrocausality/ + SEP author-info page | **real-wrong-metadata** — entry was cited with no authors and no date; authors are Simon Friederich and Peter W. Evans, first published 2019-06-03, substantive revision 2023-11-13. Corrected |
| Hagan, Hameroff & Tuszyński 2002 | arXiv quant-ph/0005025 (= Phys. Rev. E 65:061901) | real-correct, **and the 2026-07-29 figure revision verified**: paper attributes 10⁻¹³ s to Tegmark and extends it to 10⁻⁵–10⁻⁴ s. "Eight to nine orders longer than Tegmark's" ✓; "still only 10⁻⁵ to 10⁻⁴ seconds" ✓ verbatim; "three to five orders short of 10²–10³ ms" ✓ arithmetic |
| Kastner 2012 | Cambridge UP catalogue; Kastner PTI papers (arXiv 1204.5227) | real-correct; claim-match **confirmed** — "prespacetime of pure physical possibility", transactions between possibilities as source of the actual, absorbers generating confirmation waves. Article's characterisation is faithful |
| Libet et al. 1983 | *Brain* 106(3):623–642 | real-correct (06-04 ledger); "several hundred milliseconds" ✓ (RP ~550 ms, W ~200 ms pre-movement) |
| Price 2012 | arXiv 1002.0906 + PhilPapers; SHPMP 43(2):75–83 | real-correct; **framing now load-bearing** — his answer is "Maybe", used in the C1 fix. Title in References is the short form (subtitle *How the Quantum World Says "Maybe"* omitted); left as-is, not a defect |
| Schurger, Sitt & Dehaene 2012 | PNAS 109(42):E2904–E2913 (06-04 ledger) | real-correct; **framing re-confirmed as correct** — see below |
| Soon et al. 2008 | *Nat. Neurosci.* 11(5):543–545; PMID 18408715 | real-correct; **60% figure verified** — ~60% prediction accuracy from medial frontopolar cortex and precuneus, 10-fold cross-validated. Article's use is deflationary, not inflationary |
| Stapp 2011 | Springer, DOI 10.1007/978-3-642-18076-7 | real-correct — **edition question resolved**: 1st ed. 2007, **2nd ed. 2011** (The Frontiers Collection, adds two chapters on free will and the placebo effect). The year 2011 is right for the 2nd edition. Marked `(2nd ed.)` for disambiguation against the corpus's Stapp-2007 entries. No inline year cite exists, so no `[[stapp-2007-mindful-universe-vs-2005-qid-paper]]` collision |
| Tegmark 2000 | Phys. Rev. E 61(4):4194–4206 | **inline-cite orphan, FIXED** — "Tegmark's" was cited by name in the body with no References entry, a §2.4 step-5 cross-reference gap that survived nine prior reviews. Entry added |

## Specifically on the brief's three flagged clusters

**Libet / Soon / Schurger triad — no framing defect; the article is already exemplary here.** The brief's worry was that Schurger might be enrolled alongside Libet and Soon as though all three point the same way. It is not. Schurger is introduced with "honesty requires engaging the strongest deflationary rival", is stated to make the timing puzzle "largely dissolve with no quantum, no retrocausality, and no atemporal selection", is called "a live and well-supported account", and the article says the mechanism "must coexist with it rather than claim to have refuted it". The direction is correctly inverted relative to Libet/Soon. Nor does the article overstate Soon: the 60% figure is deployed *deflationarily* ("leaves substantial room for undetermined factors"), and Soon's multi-second predictivity is flagged as "under active debate". Confirms 07-15. **Do not re-flag.**

**ABL / Price / Kastner — two real defects, both in the ABL/TSVF paragraph, none in Kastner.** ABL was over-credited (C2) and the formalism was credited with an ontological result it does not deliver (C1). Kastner's possibilist TI is characterised faithfully. Price was not mis-framed because he was not cited inline at all — he now is, correctly, as the source of the "maybe".

**Stapp edition year — 2011 is correct, verified as the 2nd edition**, not a wrong-year defect. Annotated rather than changed.

## Secondary finding, not treated as a defect

**"What These Frameworks Share" over-attributed a collapse thesis to the TSVF.** The three shared claims included *"'Collapse' is constraint satisfaction across time"*, which is Cramer's and Kastner's ontological proposal, not the TSVF's — the TSVF re-describes standard QM and takes no position on collapse. Sharpened, and one striking fact marked in prose because it bears directly on Tenet 4: **Lev Vaidman, the TSVF's principal developer, is an Everettian** (he authors the SEP entry on the Many-Worlds Interpretation). The Map borrows the formalism from an author whose collapse ontology it rejects; the article now says it takes "formal structure from both and collapse ontology only from the transactional side." The closing over-claim "This provides the physics for atemporal selection" was replaced.

## Style-guide fix

Line 104 carried the banned LLM construct — *"This isn't causation running backward. It's causation not running in either direction—…"* — the two-sentence "This is not X. It is Y." pattern CLAUDE.md forbids. Rewritten as a single direct claim. Also softened the lead's "This resolves the apparent timing problem" to "This is how the framework addresses…", since the article's own Schurger concession denies that the puzzle is resolved by this route.

## Calibration / Evidential-Status Check

No possibility/probability slippage. The three fixes all move calibration *downward* (a formalism no longer credited with forcing retrocausality; a superseded empirical precedent withdrawn; "resolves" → "addresses"), and none was made by invoking tenet-coherence as evidence. The decoherence caveat's honest shortfall concession — flagged by 06-04 and 07-15 as load-bearing and not to be "strengthened" — was preserved intact and was *not* strengthened even though the Hagan paper offered a warrant to do so (see Remaining Items).

## Reasoning-Mode Classification (editor-internal; not in article prose)

- Illusionism / standard epiphenomenalist reading: **Mode One** — isolates the load-bearing premise (causation must flow forward) and challenges it; concedes Schurger as a stronger rival on its own terms. Unchanged.
- Decoherence/Tegmark objection: **Mode Two → honest concession** — uses the opponent's own quantitative standard. Strengthened *against* the Map by C3's withdrawal of the photosynthesis precedent.
- MWI: **Mode Three — framework-boundary marking.** Now sharper, since the article acknowledges borrowing formal machinery from an Everettian while rejecting the ontology.

No editor-vocabulary label leakage in article prose (grepped for `direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `Engagement classification`, `Evidential status:` — zero hits).

## Optimistic Analysis Summary

### Strengths Preserved
- The Schurger-2012 deflationary paragraph — untouched, and re-confirmed as the article's best passage.
- The decoherence honest-shortfall concession — untouched in direction and deliberately not strengthened.
- "Phenomenology illustrates but does not discriminate" — the load-bearing hedge is preserved in the section opener; only its two verbatim restatements were removed.
- Two-pathway framing, three-step Libet resolution, "What Selection Is Not" preemption, modified growing block, tenet-by-tenet Relation to Site Perspective.

### Enhancements Made
Five: correct attribution chain for TSVF/weak measurements; explicit Map-vs-formalism separation on retrocausality; withdrawal of the superseded photosynthesis precedent with citation; TSVF/transactional collapse-ontology divergence marked (with the Vaidman-is-an-Everettian point); banned construct removed.

### Cross-links Added
None. Cross-link structure is mature; all `[[wikilinks]]` resolve.

## Remaining Items

1. **The photosynthesis over-claim is corpus-wide.** Six further live files assert essentially the same superseded claim: [topics/evolutionary-case-for-quantum-neural-effects.md](/topics/evolutionary-case-for-quantum-neural-effects/), [topics/biological-computationalisms-inadvertent-case-for-dualism.md](/topics/biological-computationalisms-inadvertent-case-for-dualism/), [concepts/entanglement-binding-hypothesis.md](/concepts/entanglement-binding-hypothesis/), [concepts/prospective-memory.md](/concepts/prospective-memory/), [concepts/biological-computationalism.md](/concepts/biological-computationalism/) (plus a refinement-log sidecar for `non-temporal-consciousness`, which should not be touched). Not swept in this pass — reported for task minting. Note that `find_superlative_claims` will not surface these; grep `photosynthetic energy transfer` and `photosynthe.*coheren` instead.
2. **Deliberately not touched: Hagan et al.'s actin-gelation figure.** The paper also proposes that actin gelation could extend decoherence to 10⁻²–10⁻¹ s, which would reach the low end of the neural timescale and would let the article's concession be softened. Adding it would "strengthen" the honest concession that 06-04 and 07-15 both flagged as must-not-be-strengthened, so it was left out. Recording it here so a future pass does not mistake the omission for an oversight.
3. Price 2012's References entry omits the subtitle *How the Quantum World Says "Maybe"*. Cosmetic; the short title is a legitimate citation form.

## Stability Notes

Prior stability notes (2026-02-01 → 2026-07-15) all remain valid and are carried forward:
- Eliminative-materialist / physicalist rejection is bedrock framework-boundary disagreement.
- Many-Worlds preference is expected per the No Many Worlds tenet; Mode Three boundary-marking.
- Schurger-2012 is correctly positioned as a coexisting rival — do **not** re-flag "the article doesn't refute Schurger".
- The decoherence honest concession is load-bearing and must not be strengthened into an overclaim (now doubly so: see Remaining Item 2).
- Time-symmetric vs non-retrocausal selection is a live question *within* the framework — not a defect.

**New stability notes:**
- The retrocausal reading of the TSVF is now explicitly labelled as the Map's interpretive addition rather than a mathematical result. Future passes must **not** "tighten" this back into "TSVF makes retrocausality explicit" — that claim is refuted by the SEP entry and by Price 2012, both of which are in this article's own References.
- The photosynthesis precedent has been deliberately withdrawn on Duan et al. 2017 grounds. Do **not** restore it as a biological-coherence example.
- The article's own bibliography contains its best critics. When a future pass wants to escalate a claim about time-symmetric physics, check Price 2012 and Friederich & Evans (2023) first — they are the ones who will contradict it.
- Convergence note: nine prior reviews plus a full metadata ledger did **not** catch C1, C2 or C3, because metadata verification, quote-fidelity and skeptic-co-option framing were all clean while *claim-match against what the paper establishes* had never been run. Intra-corpus and metadata consistency ratified a formalism/ontology conflation for five months. The lens that yielded here was: **does this citation support the proposition, or merely exist?**