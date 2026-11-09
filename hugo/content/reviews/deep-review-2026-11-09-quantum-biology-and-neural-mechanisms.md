---
ai_contribution: 100
ai_generated_date: 2026-11-09
ai_modified: 2026-11-09 17:37:06+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-11-09
date: &id001 2026-11-09
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-09 17:37:06+00:00
modified: *id001
related_articles: []
title: Deep Review - Quantum Biology and Neural Mechanisms
topics: []
---

**Date**: 2026-11-09
**Article**: [Quantum Biology and Neural Mechanisms](/concepts/quantum-biology-and-neural-mechanisms/)
**Previous review**: [2026-07-25](/reviews/deep-review-2026-07-25-quantum-biology-and-neural-mechanisms/) (seventh review of this slug — also 2026-07-09, 2026-06-18, 2026-06-04, 2026-05-11, 2026-03-26)

## Selection & Drift Assessment

Cycle deep-review slot; selector score 76 (`last_deep_review` 2026-07-25, `ai_modified` 2026-11-08, 107 days unreviewed). Eleven commits touched the file after the 07-25 review; the three the driver singled out were re-verified against their source pages:

- **2026-10-11 warm-biology sweep** — L56 "on its leading but unsettled model", L76 "If the leading model holds", L148 "*precedent, not licence*", L172 "on the leading but unsettled compass model". Consistent with [P-Q8](/positions/quantum-interface/#p-q8) ("a precedent for the interface, not a licence for it"), with `topics/quantum-biology-and-neural-consciousness` L45/L134/L136 and with today's `concepts/ai-hardware-substrate-taxonomy` L74 ("precedent, not licence") and L112 (microtubule processing as *one* possible host). Landed cleanly.
- **2026-10-12 radical-pair figure** — L72 reproduces the reusable sentence from `concepts/radical-pair-magnetoreception` L62 word for word ("has not been measured; broadband radiofrequency experiments … suggest roughly 2–10 µs (Kobylkov et al. 2019) … the older 'at least tens of microseconds' (Gauger et al. 2011) depends on a single-frequency result that has not replicated"). L74's 700 ns FAD–superoxide budget and the "2–10 µs" comparison match the same page. Reads as an estimate, unmeasured in vivo. Landed cleanly.
- **2026-11-08 Family 3 sweep** — the sweep changed only the tail of the SNARE sentence (L126: "directly supporting" → "a route that would fit … without evidencing it") and left the head, "Consciousness could bias tunneling probabilities". Against [P-Q2](/positions/quantum-interface/#p-q2) ("biases *which* outcome becomes actual, but outcome frequencies stay Born-exact") that head still reads as altering the statistics. Fixed this pass (below). L166 ("where consciousness might bias outcomes within these constraints") already matches the register.

## Pessimistic Analysis Summary

### Critical Issues Found

- **L88 / L92 misdescribed what Tegmark (2000) calculated.** The page said Tegmark "estimated microtubule conformational superpositions … would decay in ~10⁻¹³ seconds" and the table said his figure was "aimed at Orch-OR-style microtubule conformational superpositions". Tegmark's abstract says his microtubule figure is for "kink-like polarization excitations"; Hagan, Hameroff & Tuszyński (2002), abstract point 1, make exactly this their first objection ("a hybrid that replaces the superposed protein conformations of the 'Orch OR' theory with a soliton in superposition"). The page therefore silently took the anti-Hagan side on point 1 while reporting Hagan's other points, and disagreed with the Map's canonical homes, which already say "modelled as kinks" (`topics/quantum-biology-and-neural-consciousness` L51, `topics/quantum-neural-timing-constraints` L41/L54). **Resolution**: L88 → "estimated that superposed kink-like excitations in microtubules—his stand-in for the conformational superpositions Penrose-Hameroff orchestrated-objective-reduction requires—would decay"; Hagan's objections now open with "had modelled a soliton hybrid rather than Orch OR's conformational superposition"; table row → "microtubule superpositions, modelled as kinks". Paid by dropping "in the 24 years since publication" (a figure that went stale annually).
- **L126 register conflict with [P-Q2](/positions/quantum-interface/#p-q2).** "Consciousness could bias tunneling probabilities" → "Consciousness could select which tunnelling outcome actualises" (the 11-08 sweep's own phrasing on `concepts/emergence` L175: "biases which outcome actualises within the Born distribution").
- **L110 unattributed quotation.** "large and opposite effects on synaptic transmission" was quoted with no inline source and no preprint flag ("In 2025, multi-electrode array experiments showed"). → "Esmaeilpour et al. (2025), a bioRxiv preprint, showed with multi-electrode arrays that". The phrase is verbatim in the bioRxiv abstract (verified via the bioRxiv API, posted 2025-08-28).
- **L233 Warren 2023 title.** The quoted title read "…non-classical brain function**s**"; Crossref (10.1088/2399-6528/acc4a8) gives the singular "function". Corrected (real-wrong-metadata, zero words).

### Medium Issues Found

- **L104 internal tension**: "each has theoretical and experimental support" contradicted L112 ("The proposal remains theoretical") and the uncited ordered-water paragraph. → "each has at least theoretical support" (zero words).
- **L110 Posner coherence stated as fact**: "have coherence times of ~10⁵ seconds" while L94 and L128 say the estimates are disputed. → "are estimated (Fisher 2015) to keep coherence for ~10⁵ seconds". Prior reviews (03-26, 05-11) ticked the figure as "correctly hedged" on the strength of L94/L128; the L110 sentence itself was not.
- L116 "far beyond" → "beyond" (one-word pay-back; the strength claim had no support).

### Citation Web-Verify Ledger (publisher of record, 2026-11-09)

Re-verified at Crossref by DOI or bibliographic query, plus arXiv/bioRxiv abstracts for the quoted strings and figures:

- Tegmark 2000 (Importance of quantum decoherence in brain processes) — PRE 61(4) 4194–4206 — state: real-correct; abstract gives 10⁻¹³–10⁻²⁰ s, microtubule figure for kink-like excitations (body reading corrected, above).
- Hagan, Hameroff & Tuszyński 2002 — PRE 65(6) 061901 — real-correct; abstract gives 10⁻⁵–10⁻⁴ s and the soliton-hybrid objection. The 10⁻⁵–10⁻⁴ s figure is credited to Hagan et al. 2002, not Hameroff 1998, at L88 and L93 (consistent with today's taxonomy fix). "Warm, wet, and noisy" is presented as the standard objection with no coiner claim — no populariser/coiner defect.
- Babcock et al. 2024 — JPCB 128(17) 4035–4046, DOI matches — real-correct.
- Fisher 2015 — Annals of Physics 362, 593–602 — real-correct; ~10⁵ s is Fisher's estimate (now labelled as such).
- Kerskens & López Pérez 2022 — J. Phys. Commun. 6(10) 105001 — real-correct.
- Warren 2023 — J. Phys. Commun. 7(3) 038001 — real-wrong-metadata (title "functions" → "function"); corrected.
- Engel et al. 2007 — Nature 446, 782–786 — real-correct. Duan et al. 2017 — PNAS 114(32) 8493–8498 — real-correct (year-order: 2017 answers 2007 ✓).
- Gauger et al. 2011 — PRL 106(4) 040503 — real-correct; "at least tens of microseconds" verbatim in abstract. Kobylkov et al. 2019 — J R Soc Interface 16(161) 20190716 — real-correct.
- Denton et al. 2024 — Nat Commun 15, 10823 (article-number confirmed) — real-correct. Luo et al. 2025 — JACS 147(47) 43934–43945 — real-correct.
- Vicente et al. 2008 — PNAS 105(44) 17157–17162 — real-correct (pre-dates Baum 2024; "refutes that premise" is a pre-existing result, not a reply, and reads correctly).
- Esmaeilpour et al. 2025 — bioRxiv 10.1101/2025.08.23.671929, posted 2025-08-28 — real-correct; quotation verbatim.
- Mavromatos et al. 2025 — EPJ Plus 140(11) 1116 — real-correct. Qaswal et al. 2021 — Pathophysiology 28(1) 116–154 — real-correct. Georgiev & Glazebrook 2018 — Prog Biophys Mol Biol 135, 16–29 — real-correct. Craddock et al. 2017 — Sci Rep 7, 9877 — real-correct. Kalra et al. 2023 — ACS Cent Sci 9(3) 352–361 — real-correct. Khan et al. 2024 — eNeuro 11(8) — real-correct. Wiest 2025 — Neurosci Conscious 2025(1) niaf011 — real-correct ("experimentally supported" is in the title).
- Ritz et al. 2000 — Biophys J 78(2) 707–718 — real-correct. Turin 1996 — Chem Senses 21(6) 773–791 — real-correct. McGinn 1989 — Mind 98(391) 349–366 — real-correct. Beck & Eccles 1992 — PNAS 89(23) 11357–11361 (DOI 10.1073/pnas.89.23.11357) — real-correct. Fröhlich 1968 — IJQC 2(5) 641–649 — real-correct. Hameroff & Penrose 2014 — Phys Life Rev 11(1) 39–78 (DOI 10.1016/j.plrev.2013.08.002) — real-correct.
- Frankish 2016, Dennett 2016 (JCS 23(11-12)), Stapp 2007, Tallis 2024, Baum 2024 (preprint) — not reachable by Crossref this pass; unchanged since the 06-04 full-ledger verification; no quoted strings depend on them (the Tallis verbatim quote was removed corpus-wide on 07-30; L152 is paraphrase).

Superlative sweep (`find_superlative_claims`): empty. Inline ↔ References: every inline (surname, year) has an entry; uncited-background entries (Beck-Eccles, Fröhlich, Hameroff-Penrose, Stapp, Tallis, Turin, McGinn) stand per the 07-25 stability note; Esmaeilpour 2025 is now cited inline.

### Quotation fidelity

47 quote-delimited strings; 38 are frontmatter wikilinks/paths and the title/description. Body: 3 attributed quotations (Gauger "at least tens of microseconds" — verified; Esmaeilpour "large and opposite effects on synaptic transmission" — verified; Wiest "experimentally supported" — title) and 5 scare-quotes ("observations", "predictions held up", "illusions", "real", "illusory"). One Map-internal near-quotation (L72 from `radical-pair-magnetoreception` L62) is current. No stale internal quotes.

### Counterarguments Considered

All bedrock standoffs (MWI indexical argument, eliminativist burden-of-proof, Tegmark microsecond gap, Buddhist non-self) were declared bedrock across six prior reviews and are not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The "primarily *defensive*" framing, the Established / Hypothesised / Uncertain status summary, the discrete-vs-sustained distinction, the five falsifiers, and the Craddock 613 THz "computational prediction awaiting observation" flag — all untouched.
- Calibration verdict: the page does not promote microtubule coherence beyond one possible host (L124 "a contested proposal, not a settled one"; Wiest flagged as partisan at L124 and L148); the "Five Neural Quantum Mechanisms" table's "Growing (2024-2025)" for microtubules is honest given the classical-reading caveats attached at L124 and L168. "What Would Challenge This View?" names five live falsifiers. Consistent with [P-Q8](/positions/quantum-interface/#p-q8) (neural exploitation unestablished) and with the preference ordering in `topics/comparing-quantum-consciousness-mechanisms#preference-ordering`.

### Enhancements Made

None beyond the calibration fixes above. Length-neutral mode (3,455 → 3,480 words against a 3,500 hard gate).

### Cross-links Added

None; inline wikilink density is saturated. All 43 wikilink targets resolve.

## Reasoning-Mode Classification (editor-internal)

- Illusionists: Mode Two (Tallis regress) + Mode Three residue. Unchanged.
- Tegmark: Mode One — Hagan et al. correct him within his own framework; the page now states Hagan's first point rather than silently siding against it.
- McGinn: Mode Three. Unchanged. No label leakage.

## Remaining Items

None on this page. Cross-page: `topics/quantum-holism-and-phenomenal-unity` L120 and `concepts/entanglement-binding-hypothesis` L78 summarise Hagan's objections without the soliton-vs-conformation point; neither asserts Tegmark modelled conformational superpositions, so no defect — noted for the next review of those pages only.

## Stability Notes

Seventh review. The body remains converged; this pass corrected one reading of a cited paper (Tegmark's target) and three register/attribution details, none of which prior reviews had flagged. Do not re-flag the bedrock standoffs or the deliberate uncited-background References entries. Future passes should keep hygiene on whatever the latest sweep touched and on the three quoted strings listed above.

## Word Count

- Before: 3,455 words
- After: 3,480 words (+25)
- Status: 139% of 2,500 soft; under the 3,500 hard gate.