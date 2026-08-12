---
ai_contribution: 100
ai_generated_date: 2026-08-12
ai_modified: 2026-08-12 12:13:13+00:00
ai_system: claude-fable-5
author: null
concepts:
- '[[entropic-brain-hypothesis]]'
- '[[filter-theory]]'
created: 2026-08-12
date: &id001 2026-08-12
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-12 12:13:13+00:00
modified: *id001
related_articles:
- '[[psychedelics-and-the-filter-model]]'
title: Deep Review - The Entropic Brain Hypothesis
topics: []
---

**Date**: 2026-08-12
**Article**: [The Entropic Brain Hypothesis](/concepts/entropic-brain-hypothesis/)
**Previous review**: [2026-06-22](/reviews/deep-review-2026-06-22-entropic-brain-hypothesis/) (deep), plus [2026-08-07](/reviews/pessimistic-2026-08-07-entropic-brain-hypothesis/) (pessimistic; all four of its critical issues were fixed by the 2026-08-08 refine-draft, commit 809ca250d5)
**Review scope**: Full deep review of the post-2026-08-08 text. Focus: (a) verify the 08-08 remediation landed correctly, (b) §2.4 publisher-of-record web-verify of material the 08-07 ledger did not cover (new quotes and reference entries introduced 08-08), (c) fresh pessimistic/optimistic pass on the revised sections.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Verbatim quote cited to the wrong work** (Core Claim): "the entropy of spontaneous brain activity indexes the informational richness of conscious states" was attributed to Carhart-Harris et al. (2014). Publisher-of-record check (EuropePMC, both abstracts retrieved): the phrase does **not** appear in the 2014 *Frontiers in Human Neuroscience* abstract; it is verbatim from the 2018 single-author *Neuropharmacology* "revisited" abstract ("...within upper and lower limits, after which consciousness may be lost, the entropy of spontaneous brain activity indexes the informational richness of conscious states"). The old sentence also hardened 2018's "may be lost" into "is lost" (dropped qualifier). RESOLVED: the Core Claim now states 2014's actual proposal in its own terms (elevated entropy as the defining feature of "primary states", via the connectivity-motif repertoire — faithful to the 2014 abstract) and attributes the canonical one-sentence formulation, with the "may be lost" qualifier restored, to the 2018 revision. This is the anachronistic-formulation variant of quote-to-wrong-work: the 2014 paper proposes the idea, but the quotable sentence is 2018's.
- **Truncated quote not grep-verifiable in the raw source** (Brain Criticality): the Varley et al. qualification was quoted as "All states, however, showed some signs of persistent criticality." with a terminal period, but the source sentence continues. RESOLVED: extended to the full abstract sentence "...when testing for exponent relations and universal shape-collapse." (verified at journals.plos.org).

### Medium Issues Found
- **Unsupported superlative**: "DMT—the most phenomenologically extreme psychedelic available to controlled study" — controlled human 5-MeO-DMT studies exist, so the definite superlative is not supportable. RESOLVED: softened to "among the most phenomenologically intense psychedelics available to controlled study". The parallel "the most intense psychedelic phenomenology on record" in Relation to Site Perspective softened to "some of the most intense...". (The `find_superlative_claims` helper returned no hits — these were caught manually; the helper's patterns do not cover "most phenomenologically extreme".)

### §2.4 Citation Web-Verify Ledger (publisher of record)
Covers everything the 2026-08-07 ledger did not, plus re-confirmation of load-bearing items. All checks 2026-08-12 via EuropePMC REST / journals.plos.org / elifesciences.org:

- Bak, Tang & Wiesenfeld 1987 (*Phys. Rev. Lett.* 59(4), 381–384) — state: real-correct (textbook-standard citation; not re-retrieved).
- Carhart-Harris et al. 2014 (*Front. Hum. Neurosci.* 8:20) — state: real-correct metadata; **body quote was misattributed to it** (fixed, see Critical). Full abstract retrieved; the new paraphrase ("defining feature of primary states... repertoire of functional connectivity motifs that form and fragment across time") tracks the abstract wording.
- Papo 2016 — state: real-correct (verified at publisher 2026-08-07; unchanged since).
- Carhart-Harris 2018 (*Neuropharmacology* 142:167–178, single author) — state: real-correct; the quoted sentence confirmed verbatim in its abstract.
- Carhart-Harris & Friston 2019 (*Pharmacol. Rev.* 71(3):316–344) — state: real-correct (verified 2026-08-07; unchanged).
- Varley et al. 2020 (*PLoS Comput. Biol.* 16(12):e1008418) — state: real-correct; eLocator confirmed; full "All states..." sentence confirmed in abstract; single-macaque claim confirmed in Methods ("one monkey (Chibi)"; second animal excluded for artifacts).
- Letheby 2021 (*Philosophy of Psychedelics*, OUP) — state: real-correct.
- Toker et al. 2022 (*PNAS* 119(7):e2024455119) — state: real-correct; full 13-author list retrieved; Carhart-Harris confirmed 7th of 13, matching the article's non-independence disclosure.
- Rankaduwa & Owen 2023 (*Neurosci. Conscious.* 2023(1), niad001) — state: real-correct; the quoted phrase "an increase in complexity seems to be fully compatible with overall reductions in conscious awareness" grep-verified in the full text via EuropePMC full-text phrase search (exactly 1 hit, this paper).
- Toker et al. 2024 (*eLife* 13:e86547) — state: real-correct; abstract confirms propofol diminishes / 5-MeO-DMT enhances cross-frequency cortical–thalamic information transfer, and the hedged "may be mediated by excursions... toward/away from edge-of-chaos criticality" — the article's "*may be* mediated" preserves the hedge.
- Safron et al. 2025 (*Neurosci. Conscious.* 2025(1), niae038, DOI 10.1093/nc/niae038) — state: real-correct (the niae-prefix/2025-volume pairing is genuine, not a year mismatch).
- Irrmischer et al. 2026 (*J. Neurosci.* 46(2):e0344252025, DOI 10.1523/JNEUROSCI.0344-25.2025) — state: real-correct; 8-author list confirmed with Carhart-Harris 6th; "entropy is increased while complexity is reduced", "toward subcritical regimes", and alpha/theta criticality-shifts correlating with self-dissolution intensity ratings all confirmed against the abstract.
- Southgate & Oquatre-six 2026 (Map self-cite) — state: real-correct (site URL; pseudonymous co-author convention is intentional).

Empirical-record currency sweep: `find_superlative_claims` returned no candidates; manual pass caught the two DMT superlatives above (fixed). No "current record"/"first to demonstrate" claims present.

### 2026-08-08 Remediation Verification
All four critical issues from the 2026-08-07 pessimistic review confirmed fixed in the current text: (1) DMT direction now reported with full force in *Where the Measure Is Contested* (away from criticality, subcritical, complexity reduced) and used as the entropy/criticality decoupling wedge; (2) the four-papers-one-citation compression is unwound — Toker 2022 / Toker 2024 / Varley 2020 / Irrmischer 2026 each separately attributed and referenced; (3) "Independent work" replaced by an explicit non-independence disclosure (Carhart-Harris 7th of 13 on Toker 2022, 6th of 8 on Irrmischer) with the symmetric-standard note; (4) the L42 "reversal" framing replaced by "does not discriminate between the readings" with the accommodation correctly credited to production accounts, and the cross-reference to [psychedelics-and-the-filter-model](/topics/psychedelics-and-the-filter-model/) now accurately characterised. Varley single-macaque caveat and Bak/Rankaduwa/Letheby reference wiring also confirmed in place.

### Counterarguments Considered
- Buddhist Philosopher (self-dissolution as narrowing): now answered in the article itself — the closing sentence of *Where the Measure Is Contested* and the two-branch aperture analysis in *Relation to Site Perspective* take the objection on directly rather than hiding the direction. No further change needed.
- Empiricist (single-animal weight): carried by the in-text single-macaque disclosure and "nothing here should rest on more weight than one animal's data can carry". Adequate.

## Optimistic Analysis Summary

### Strengths Preserved
- The two-branch aperture analysis ("If the aperture is entropy... If the aperture is proximity to criticality...") is the best new passage from the 08-08 revision — it converts the DMT counter-example into a precise open question for the filter reading instead of a defeat or a dodge. Untouched.
- The measure-vs-explanation wedge, the rival-not-ally framing, and the explicit interpretive-overlay marking (per the evidential-status discipline) remain calibration-clean — the Hardline Empiricist persona's checks all pass; no tenet-as-evidence-upgrade anywhere.
- The non-independence disclosure now applies the Map's own convergence-counting standard symmetrically. Genuine credibility asset.

### Enhancements Made
- Quote reattribution (2014 → 2018) with the "may be lost" qualifier restored.
- Varley quote extended to the full, grep-verifiable source sentence.
- Two superlatives softened to supportable form.

### Cross-links Added
- None — the article's link mesh is complete and reciprocal (verified all 12 wikilink targets and both tenet block anchors resolve).

## Remaining Items

None requiring a task. Note for future passes: the article now sits at 2486 words (99% of the 2500 soft threshold) — any future addition must be offset; treat the article as length-neutral from here.

## Stability Notes

- Bedrock (do not re-flag): EBH's originators are physicalists and reject the filter re-description from outside the Map's tenets; the article declares this ("rival framework rather than an ally"). Confirmed stable across three reviews.
- Do not "strengthen" the filter overlay into a discriminating claim — the empirical-equivalence marking is correct and deliberate (carried forward from 2026-06-22).
- The entropy/criticality decoupling (Irrmischer) is now the article's central empirical exhibit; future reviews should not re-fuse the two quantities when summarising EBH, and should not resolve the two-branch aperture question prematurely — neither branch is closed on current evidence, and the article says so on purpose.
- The article has now had 3 substantive review passes (2026-06-22 deep, 2026-08-07 pessimistic, 2026-08-12 deep) and the defect stream has narrowed to citation-fidelity fine grain. Convergence damping should be allowed to work; no re-review needed absent substantive modification.