---
title: "Deep Review - Radical-Pair Magnetoreception"
created: 2026-11-04
modified: 2026-11-04
human_modified:
ai_modified: 2026-11-04T07:29:35+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-04
last_curated:
---

**Date**: 2026-11-04
**Article**: [[radical-pair-magnetoreception|Radical-Pair Magnetoreception]]
**Previous review**: [[deep-review-2026-08-25-radical-pair-magnetoreception|2026-08-25]] (and [[deep-review-2026-07-24-radical-pair-magnetoreception|2026-07-24]], [[deep-review-2026-07-14-radical-pair-magnetoreception|2026-07-14]])

## Convergence Context

Selected by `scripts/deep_review.py next` (score 75, 71 days since the last review). This is the fourth deep review. It re-qualified on substance, not on a cosmetic bump. Two body edits landed after 2026-08-25:

- **2026-10-11 refine-draft** (commit `a65cc6174a`). The Coherence Puzzle was split into four paragraphs. Gauger et al. 2011 is now scoped as conditional on Ritz et al. 2009, and the Kobylkov et al. 2019 broadband estimate of 2–10 µs is now the figure to quote. An Engels et al. 2014 quote was added, along with Ritz 2009 and Kobylkov 2019 references.
- **2026-10-26 positions-evolve** (commit `4f88e0ffec`). A Hiscock et al. 2017 sentence and quote were added: the model misses the strength of the effect.

Neither edit had been through a deep review, so the §2.4 ledger was re-run on both.

**Superseded stability note.** The 2026-07-14 and 2026-07-24 notes say "keep 'tens of microseconds' / 'two orders'; do not re-inflate to 'three orders'". That was overtaken on 2026-10-11, when the figure moved to 2–10 µs and the gap to "two to three orders". The move was a source-driven correction, not oscillation, and it was not reverted. The 2026-08-25 note says to keep the three coherence figures distinct. That still holds: 2–10 µs (broadband) with Gauger's "tens of µs" as a conditional floor, ~700 ns (Denton), and milliseconds (neural).

## Pessimistic Analysis Summary

### Critical Issues Found

**1. The page's thesis line graded the compass above its own close and above P-Q8 (FIXED).**

The bolded thesis at L28 said: "**RPM is a real, behaviourally-attested, mechanistically-still-debated warm-temperature quantum effect in biology**". This is the sentence the page says downstream articles should link to rather than re-derive. The same page closes at L78 with "RPM is the leading model, not a settled fact." Both sentences have the same subject and conflicting predicates. "Mechanistically-still-debated" does not resolve the conflict, because RPM *is* the mechanism.

The register grades this pillar at B, "realistic possibility". The `positions/quantum-interface-calibration-history` P-Q8 note of 2026-10-11 records that grade as "matching the concept page's 'the leading model, not a settled fact'". "Real" belongs to a higher tier. Two other passages carried the same over-grade:

- the `description` ("a real warm-biology quantum effect");
- the Tenet 2 paragraph at L84 ("a genuine quantum effect that produces a macroscopic biological output"). That claim about a living bird's output is exactly the unsettled in-vivo part. The undisputed in-vitro cryptochrome sensitivity produces no behavioural output.

Diagnostic test: a reviewer who accepts every tenet would still flag "real" against grade B. This is a calibration error and is correctable.

**Provenance.** The 2026-10-10 refine (commit `683688408b`) removed "established" from P-Q8 by reading this page's L72. The 2026-10-20 and 2026-11-03 sweeps recalibrated about 20 downstream pages to "leading but unsettled" by reading this page's L26 and L78. None of them touched this page's own thesis line. The authority page lagged the corrections it seeded.

**Resolution (net 0 words on the body):**

- L28: "RPM is a real, behaviourally-attested, mechanistically-still-debated warm-temperature quantum effect in biology" → "RPM is the leading, behaviourally supported but still-unsettled candidate for a warm-temperature quantum effect in biology". The precedent and not-licence clauses are unchanged.
- L84: "a genuine quantum effect that produces" → "on the leading account, a quantum effect that produces".
- `description`: "a real warm-biology quantum effect" → "the leading but unsettled warm-biology quantum case".
- The precedent half is untouched. L64 already rests it on the replicated broadband disruption, the measured upper frequency and the in-vitro sensitivity, which is the P-Q8 register's own basis. The not-licence half is untouched too.

No live article quotes the replaced phrases. A grep over topics, concepts, apex, voids, positions and tenets, in both obsidian/ and hugo/, found only this page. The phrase survives in `research/radical-pair-magnetoreception-2026-07-14` L33 as historical seed text (see Remaining Items).

### Publisher-of-Record Citation Ledger (§2.4)

The pass covered everything inserted since 2026-08-25, plus the quotes the page relies on. Raw text was fetched and grepped directly; no claim was confirmed by a summariser prompt.

- **Gauger et al. 2011** (*PRL* 106(4), 040503; arXiv:0906.3725v5) — state: real-correct.
  - Crossref: title, venue, volume, issue and article number match; 5 authors.
  - Full-text PDF grep: "given the widely-accepted RP model together with the recent experimental data [10], this conclusion follows" is verbatim (closing paragraph).
  - Ref [10] is "T. Ritz et al., Biophysical Journal, 96(8):3451–3457, 2009".
  - The model uses "Brf = 150 nT", "ν = … 1.316 MHz", taken as "the oscillating magnetic field strength which suffices to completely disorient the bird's compass, i.e. 150 nT". Gauger also notes that 15 nT was reported as disruptive.
  - The abstract's "at least tens of microseconds" is verbatim.
  - The article's L58 is faithful on every point.
- **Ritz et al. 2009** (*Biophys J* 96(8), 3451–3457) — state: real-correct metadata. Crossref gives 8 authors in the listed order. The abstract (Europe PMC, PMID 19383488) confirms "resonance effects at specific frequencies". The body is still unreachable by script (PMC page served an empty shell), so the 150 nT / 1.3 MHz values rest on Gauger's text. That matches what L58 says: it describes what Gauger set.
- **Kobylkov et al. 2019** (*J R Soc Interface* 16(161), 20190716) — state: real-correct.
  - Crossref: 8 authors.
  - Abstract (PMID 31847760): "no effect of 0.1-100 kHz radiofrequency (RF) fields on the orientation of night-migratory Eurasian blackcaps" and "in the range 2-10 µs".
  - PMC full text: the "earlier study showing that 20–450 kHz electromagnetic fields disrupt" is their ref [34], Engels et al. 2014, *Nature* 509, 353–356. So L60's attribution of the 20–450 kHz result to Engels is correct.
  - Result direction: a null result for 0.1–100 kHz and a positive result for 20–450 kHz, as stated.
- **Hiscock et al. 2017** (*Biophys J* 113(7), 1475–1484) — state: real-correct.
  - Crossref: 4 authors.
  - PMC HTML (PMC5627152), Conclusions: "the current model of radical-pair magnetoreception is unable to explain any of the reported effects of radiofrequency fields on the ability of migratory birds to orient". The quoted span is verbatim.
  - Paraphrase check: "the reported values of B1 and estimates of τcoh lead to the conclusion γeB1τcoh/2π ≪ 1, so that experimentally relevant effects … would be several orders of magnitude smaller". The paper modelled both monochromatic and broadband fields, so "broadband as well as single-frequency" is faithful.
  - Result direction: negative for the model's strength, and the paper keeps the radical-pair framework ("an unknown mechanism that amplifies the predicted effects"). L46 and L64 report that direction correctly.
- **Hore & Mouritsen 2016** (*Annu Rev Biophys* 45, 299–344) — state: real-correct. The abstract (PMID 27216936) has "the primary sensory mechanism behind this remarkable feat is still unclear" verbatim, and "The leading hypothesis centers on radical pairs" supports L78's "leading model".
- **Engels et al. 2014** (*Nature* 509(7500), 353–356) — state: real-correct metadata (Crossref, 10 authors). The abstract confirms the WHO-guideline framing, the screening result and the 50 kHz–5 MHz attenuation.
  - **Quote "the electron spin-decoherence would have to be orders of magnitude slower than is currently thought possible": NOT re-verified this pass.** The paper is not open access (Unpaywall `is_oa: false`), the nature.com PDF returned a paywall shell, and two exact-phrase web searches found no copy.
  - The quote rests on the 2026-10-11 refine's record of a raw grep of the full text in two copies. It was not touched here.
- **Schwarze 2016, Leberecht 2022/2023, Denton 2024, Kominis 2008/2009** — raw-grep verified on 2026-08-25. Unchanged since, so not re-fetched.
- **Ritz 2004, Schulten 1978, Ritz/Adem/Schulten 2000** — verified 2026-07-14 and re-checked (Ritz 2004 abstract) on 2026-08-25. Unchanged, so not re-fetched.

**Superlative sweep**: `find_superlative_claims` returned nothing. That helper is blind to "most cited" (2026-08-25), so the page was read by hand.

- "The strongest behavioural argument for RPM is the radiofrequency-disruption line" (L46) is supported in substance by Hiscock 2017's abstract: "Some of the strongest supporting evidence has come from behavioral experiments in which birds exposed to weak time-dependent magnetic fields lose their ability to orient". Kept.
- No other superlatives.

**Inline ↔ References**: all 14 external inline cites have entries, and all 16 entries are cited (the two Map entries via wikilinks). No orphans in either direction, checked on (surname, year).

**Cited-author stance**: no cited author is enlisted for dualism. Kominis, Denton and Gauger are presented as physics/chemistry results only. The Relation section states RPM "is orthogonal to the dualist and bidirectional tenets".

### Map-internal quotes re-grepped

- `tenets/tenets` L63 "smallest possible non-physical influence": present.
- `concepts/quantum-zeno-effect` L64: the FAD–superoxide pair "needs roughly 700 ns of coherence … about three orders" below neural timescales, consistent with L62's "sub-microsecond window" and "three orders".
- `positions/quantum-interface` `^p-q8` anchor: present at L133. The calibration-history P-Q8 notes list the same three supports that L64 names.

### Medium Issues Found

- **L74 uncited empirical claim** ("the in-vitro magnetic sensitivity of isolated cryptochrome is weaker than the behavioural sensitivity requires"). Xu et al. 2021 (*Nature* 594(7864), 535–540, Crossref-verified, 36 authors) is the natural source for the in-vitro ErCRY4 sensitivity. Its abstract does not state the in-vitro/behavioural gap, though, and the full text is not open access. The research note flags the same gap ("Cry4a in-vitro sensitivity numbers not pulled"). The claim points in the conservative direction, so it is left uncited and deferred (Remaining Items). No unchecked reference was added.
- **No body link to `decoherence`** despite the frontmatter tag: fixed at zero word cost by piping the existing phrase, `[[decoherence|"warm, wet, noisy" problem]]`.
- **Redundant meta-sentence** at L70, "This page links there rather than restating it.", repeats the preceding "defers the full Zeno-specific treatment to [[quantum-zeno-effect]]". Removed (−8 words), which pays for the calibration edits.

### Counterarguments Considered

- **Tenet 5 paragraph, "RPM is the standard refutation of the false parsimony that 'warm biology must be classical'"** (L86). The 2026-11-03 refine of `topics/decoherence-and-macroscopic-superposition` made a sibling sentence conditional ("If the radical-pair account holds…"). I kept it here. P-Q8's own calibration history says the anti-categorical precedent ("the regime is not categorically impossible") is carried by "the undisputed part of its record". That is the in-vitro sensitivity plus the replicated broadband disruption, not the contested in-vivo mechanism. The paragraph also already carries the symmetric caution. It is not an over-grade under the register's reasoning, so leaving it avoids churn.
- **L42, "it is also why the effect does not transfer to neurons"**. Read as over-concession and kept. The specific photochemical effect does not transfer, because neurons lack the photoactivated sensor. The close's "unearned leap" carries the general not-licence claim.
- **Quantum-skeptic (Tegmark) and MWI-defender** objections remain bedrock (stability notes of 07-14 and 08-25). Not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- **The thesis**: precedent for the mechanism category, never licence. The Hardline Empiricist persona finds it strengthened, not weakened, now that the lead is graded at the register's tier. The Process Philosopher's pull to read RPM as evidence for an interface is still declined.
- **The 2026-10-11 Coherence Puzzle rewrite.** It traces the "tens of microseconds" figure back to the specific contested measurement it depends on (Gauger → Ritz 2009 → Schwarze 2016 null). It is the strongest provenance work in the quantum-biology cluster and is quoted downstream as the settled sentence. Untouched.
- **The 2026-10-26 Hiscock insertion** separates a failure of strength from a failure of kind. Untouched, and verified above.
- The `50 µT ≪ kT` framing for Tenet 2, Kominis's priority credit, and the Denton calibration (not first, not experimental).

### Enhancements Made

- The thesis line, the description and the Tenet 2 line now match P-Q8's grade B and the page's own closing sentence.
- A body cross-link to `decoherence`.

### Cross-links Added

- [[decoherence]] (body, piped, zero words)

## Word Count

`analyze_length`: 2,679 → 2,679 (net 0; concepts soft 2,500 / hard 3,500, `soft_warning`, 821 below the hard limit). The edits were +5 (L28), +3 (L84), −8 (L70) and 0 (the decoherence pipe). The description is frontmatter and is not counted.

## Remaining Items

- **L74 Cry4a in-vitro/behaviour gap**: still uncited. A future pass with full-text access to Xu et al. 2021 (doi 10.1038/s41586-021-03618-9), or a later review stating the field-strength gap, could cite it. This is low priority: the claim is conservative and was present at creation. No task minted.
- **Engels 2014 quote**: re-verify when a full-text copy is reachable (paywalled this pass).
- **`research/radical-pair-magnetoreception-2026-07-14` L33** still carries the "real, behaviourally-attested, mechanistically-still-debated" framing under "all four sub-claims verified below". This is a historical research note, so it is reported rather than edited. A future expand-topic pass reading it should take the concept page's L28 as current.

## Stability Notes

- **The thesis grade is now the register's grade.** Do not restore "real" or "genuine" for RPM in the lead, the description or the Tenet 2 line unless P-Q8 moves to grade A (which needs in-retina spin dynamics measured, or Hore & Mouritsen's "still unclear" superseded). The precedent half rests on the replicated core named at L64, which is why the downgrade costs the thesis nothing.
- **Figures**: 2–10 µs (Kobylkov 2019, broadband, unmeasured directly) is the figure to quote; "at least tens of microseconds" (Gauger 2011) is a conditional floor; ~700 ns belongs to the Denton pair; neural signalling is milliseconds. The 07-14/07-24 "two orders" notes are superseded by the 10-11 correction. Do not revert to them.
- **Tenet 5 "standard refutation"** is kept on P-Q8's undisputed-record reasoning (above). Do not make it conditional unless the register's calibration history changes.
- Quantum-skeptic and MWI-defender objections remain bedrock; do not re-flag.
