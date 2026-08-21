---
ai_contribution: 100
ai_generated_date: 2026-08-21
ai_modified: 2026-08-21 16:46:24+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-21
date: &id001 2026-08-21
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-21 16:46:24+00:00
modified: *id001
related_articles: []
title: Deep Review - The Quantum Zeno Effect
topics: []
---

**Date**: 2026-08-21
**Article**: [The Quantum Zeno Effect](/concepts/quantum-zeno-effect/)
**Previous review**: [2026-07-20](/reviews/deep-review-2026-07-20-quantum-zeno-effect/) (second review; first was the 2026-07-14 cross-review of the fresh create)

Third review. The article re-qualified on a substantive, wholly unreviewed
delta: three commits landed since 2026-07-20, two of them refine-drafts on this
file and one an `expand-topic` that wrote into it from outside
(outbound-crosslink-sentences-are-never-reviewed-by-anyone).

- `25550c0e47` (08-05) — replaced the Denton coherence bullet with the
  sub-microsecond figure and split the budget from the compass radical pair.
- `6ba86802a3` (08-16) — `sign-problem-for-conscious-observation` created;
  installed the Tenet-2 crosslink sentence and the `concepts:` / Further
  Reading entries here.
- `5897c92471` (08-17) — added the Kofman & Kurizki asymmetry paragraph, the
  Naskar & Joarder deferral, the Denton frequency-band bullet, the Fischer
  interval figures, and the warm-biology spectral-density paragraph.

**Six new citations and eleven new quantitative claims entered the article in
that window and none of them appears in the 2026-07-20 per-cite ledger.** This
pass was therefore a full §2.4 publisher-of-record web-verify of the delta plus
a re-check of the carried-forward entries. Yield: **five defects, four of them
attribution or empirical-fidelity errors that survived the two prior reviews
because they were not yet in the article when those reviews ran.**

## Pessimistic Analysis Summary

### Critical Issues Found

- **Attribution error — wrong given name, "Michael Fischer" → Martin Fischer.**
  The 2001 anti-Zeno experimentalist is **Martin C. Fischer** (arXiv
  quant-ph/0104035 submission history, "From: Martin C. Fischer"; Crossref
  gives `M. C.` for DOI 10.1103/PhysRevLett.87.040402). **Fixed**, and swept
  corpus-wide: the error had propagated to
  `concepts/sign-problem-for-conscious-observation` L49, fixed there too
  (§2.4 step 6 family resolution). Four loci total including both Hugo
  mirrors; zero residual after sync.
- **Attribution error — wrong given name, "Vytautas Gontis" → Vygintas Gontis.**
  The Kaulakys co-author is **Vygintas Gontis** (Vilnius University, Institute
  of Theoretical Physics and Astronomy). The sibling
  `sign-problem-for-conscious-observation` already carried the correct form, so
  the two canonical pages of this cluster disagreed on the name of the man who
  predicted the effect one of them exists to explain. **Fixed** on this page;
  the sibling needed no change. Bronislovas Kaulakys verified correct.
- **Empirical-claim fidelity + cross-article contradiction — "A factor of five
  in the interval was enough to flip the sign."** Fischer's two runs are not a
  single-variable comparison. Verified in the paper's own figure captions:
  Fig. 3 (suppression) used `a_interr` = 2,000 m/s², `t_interr` = 50 μs,
  `V₀/h` = 91 kHz; Fig. 4 (enhancement) used 2,800 m/s², 40 μs and 116 kHz.
  Only `a_tunnel` (15,000 m/s²) was held fixed. The dedicated downstream page
  states this correctly and in terms — `sign-problem-for-conscious-observation`
  L49: *"The two runs differed in trap depth and interruption parameters as
  well as in interval, so they establish that both regimes are reachable rather
  than isolating the interval"* — so **the canonical mechanism page asserted
  exactly the isolation its own downstream page declines**. **Fixed**; the 1 μs
  / 5 μs figures themselves are verbatim correct and were kept.
- **Method misattribution — Ishizaki & Fleming (2009) presented as the
  molecular-dynamics case.** The paragraph opened *"A mature adjacent
  literature extracts bath spectral densities for warm biomolecules **from
  molecular dynamics**"* and then offered I&F as its exemplar. I&F did no MD:
  λ = 35 cm⁻¹ and τ_c = 50 fs are adopted from a numerical fit to
  two-dimensional electronic spectra (*"they adopted λ_j = 35 cm⁻¹ and
  τ_c = γ_j⁻¹ = 50 fs … Therefore, we also employ these values"*), and the
  authors flag the relaxation time as *"a numerical fitting parameter for the
  experimental data; it **was not measured directly**."* "Molecular dynamics"
  occurs **once** in the whole paper, in their *future-work* recommendation.
  Huh et al. is the MD case (TDDFT/MD and ZINDO/MD spectral densities).
  **Fixed**: the two routes are now distinguished and I&F's own caveat is
  quoted rather than dropped. The paragraph's conclusion — the published
  spectra sit in a frequency window with no overlap with the neural case — is
  unaffected and survives intact.
- **Superseded citation — Huh et al. cited as a 2013 preprint.** The work has a
  version of record: *J. Am. Chem. Soc.* 2014, 136(5), 2048–2057, DOI
  10.1021/ja412035q. **Fixed** in the article (inline year 2013 → 2014,
  reference entry rebuilt with the JACS metadata and the arXiv preprint
  retained as the anchor for the verified spans) and propagated to the source
  research note.

### ⚠️ A FALSE POSITIVE I RAISED AND WITHDREW — record it so the next reviewer does not repeat it

I first flagged the clause *"the low-frequency region governing inter-unit
transfer below 500 cm⁻¹"* as a **fabricated empirical claim**, on the strength
of a full-text grep of `arXiv:1307.0886` returning `low frequency` = 0,
`inter-unit` = 0, and a single `500 cm⁻¹` that was the static-disorder Gaussian
width for the chlorosome roll. I removed the clause.

**That was wrong. I had downloaded v1.** The paper has two versions and **v2 —
the version the source research note used, and the one matching the JACS
paper — carries an Appendix that v1 does not.** Appendix Figure A.1's caption
reads: *"the spectral density of the baseplate is not too different from the
one of FMO complex in the **low frequency domain (< 500 cm⁻¹)**, which is
**mainly responsible for the exciton transfer between the chlorosome and the
baseplate**."* The article's claim is correct. **The clause was restored**
(reworded to Huh's own "transfer between antenna units", which is more precise
than "inter-unit").

The same version gap nearly produced a second false positive: v1 reads *"The
strong **red** diagonal band"* where v2 reads *"The strong **white** diagonal
band … which leads to the rapid energy dissipation of the localized IS **within
the roll**."* The research note's quote matches **v2 verbatim** and is correct
as written; a v1-only check would have condemned it.

**Lesson for the ledger, and it generalises**: on arXiv sources, a grep-zero is
only evidence about *the version you fetched*. Check the version list before
reading absence as fabrication (citation-verify-false-negative,
narrow-grep-zero-is-not-proof-of-absence). The reference entry in
`research/bath-spectral-densities-for-warm-biological-systems-2026-08-16` now
records the v1/v2 divergence explicitly so the trap is not re-entered.

### Publisher-of-Record Web-Verify Ledger (§2.4)

Delta cites (**new since the last ledger — all verified this pass**):

- **Kofman & Kurizki 2000** (*Acceleration of quantum decay processes by
  frequent observations*), *Nature* 405(6786), 546–550, DOI 10.1038/35014537,
  published 01 June 2000 — **real-correct**. **All four quoted spans verified
  verbatim** against the Nature abstract: "the inhibitory quantum Zeno effect
  may be feasible in a limited class of systems"; "appears to be much more
  ubiquitous"; "fundamentally unattainable in radiative or radioactive decay";
  "the required measurement rates would cause the system to disintegrate".
  Authors A. G. Kofman (Abraham G. Kofman, Weizmann) and G. Kurizki confirmed
  at Crossref. The article's overlap-integral paraphrase matches the abstract's
  "determined by the energy spread incurred by the measurements … and the
  distribution of states to which the decaying state is coupled".
- **Naskar & Joarder 2023** (*Quantum decoherence in Microtubules*),
  arXiv:2304.06518, submitted 11 Apr 2023, Kaushik Naskar & Parthasarathi
  Joarder — **real-correct**; preprint-only, no journal version. Quote
  *"Finding the proper value of C0 is our future proposed work"* verified
  **verbatim and contiguous** in §3.1. Supporting description also verified:
  "Using Ohmic spectral density", "Ω is an upper cutoff frequency for the
  spectral density", and C₀ "depends on the coupling strength of the
  interaction and the spectral density".
- **Ishizaki & Fleming 2009**, *PNAS* 106(41), 17255–17260, DOI
  10.1073/pnas.0908989106 (PMC2762676, PMID 19815512) — **real-correct on
  metadata and on both numbers** (λ = 35 cm⁻¹, τ_c = 50 fs, overdamped
  Brownian oscillator; applied at both 77 K and 300 K). **real-wrong-framing**
  on method — see the critical issue above; corrected.
- **Huh, Saikin, Brookes, Valleau, Fujita & Aspuru-Guzik** — **currency-updated**
  from arXiv-2013 to the version of record, *JACS* 136(5), 2048–2057 (2014),
  DOI 10.1021/ja412035q. All six authors correct. The 1600–2000 cm⁻¹
  exciton–phonon band and the < 500 cm⁻¹ transfer region both verified in v2
  (see the withdrawn-false-positive note above).
- **Denton et al. 2024** — the four *new* quantitative claims all verified
  verbatim in the open-access *Nat. Commun.* text: "the required **700 ns**"
  coherence for geomagnetic magnetosensitivity; "inter-radical couplings up to
  **−1.7 GHz**"; N5 hyperfine "**A∥/(2π) = 49.2 MHz**"; "the electron's Larmor
  precession frequency in the geomagnetic field (**1.4 MHz**)". **real-correct.**
- **Fischer, Gutiérrez-Medina & Raizen 2001** — the *new* interval figures
  verified in the arXiv full text: suppression with "after each tunneling
  segment of 1 μs an interruption of 50 μs"; enhancement "after every 5 μs of
  tunneling". Figures correct; the surrounding sufficiency claim was not, and
  was fixed. Given name corrected (above).
- **Kaulakys & Gontis 1997**, *Phys. Rev. A* 56(2), 1131–1137, DOI
  10.1103/PhysRevA.56.1131 — **real-correct** at Crossref (a search summary
  offering "1138–1141" was not followed; the DOI itself encodes the 1131 start
  page). Given name corrected (above).

Carried-forward cites re-checked, no change: Misra & Sudarshan 1977; Itano et
al. 1990; Ballentine 1991; Itano et al. 1991; Kominis 2009; Tegmark 2000; Hagan
et al. 2002; Reimers et al. 2009; Stapp 2007 (correctly disambiguated from the
2005 LBNL / 2006 *Zygon* QID writings). Self-cites Oquatre-cinq / Oquatre-six
are legitimate Map pseudonyms (fabricated-map-self-cite-pseudonym-false-alarm).

**Inline ↔ References map**: complete in both directions, no orphans.
*Considered and declined*: the prose mention of von Neumann's 1932 measurement
axioms has no References entry, but it is prose lineage rather than an
`Author YYYY` cite, [von-neumann-wigner-interpretation](/concepts/von-neumann-wigner-interpretation/) is linked as its home,
and both prior reviews left it. Not re-flagged.

**Empirical-record currency sweep**: `find_superlative_claims` returns empty.
Manually checked the two superlative-adjacent claims anyway — "the strongest
evidence that warm, wet biology can host Zeno-like dynamics" and Kominis
"**first** framed radical-pair reaction dynamics as a quantum Zeno phenomenon
… predates later cryptochrome work by roughly fifteen years" (2008/09 → 2024 =
15–16 years). Both hold.

### Cross-article and sibling checks

- **Denton coherence budget, both directions.** `radical-pair-magnetoreception`
  L54–56 carries "at least tens of microseconds" for the well-separated compass
  pair (Gauger et al. 2011) and explicitly routes the sub-microsecond
  tightly-bound figure *to this page*. This page reciprocates. Consistent; no
  drift (apex-stale-internal-quote-channel clean here).
- **The Tenet-2 crosslink sentence installed by the 08-16 expand.** *"minimality
  constrains the magnitude of a conscious influence without constraining its
  direction"* — verified against `sign-problem-for-conscious-observation` L29
  and L83, which state exactly this. The sentence nobody reviewed is accurate.
- All nine Further Reading wikilinks resolve to live files.

### Reasoning-mode classification (§2.6, editor-internal)

- Ballentine / Itano interpretation dispute — **Mode Three**, in natural prose:
  the page concedes "the experiment settles that the freezing is real; it does
  not settle the collapse interpretation the Map's reading needs."
- Decoherence objection (Tegmark / Hagan / Reimers) — **Mode Three**,
  unchanged from the 2026-07-20 classification; the timing gap "relocates
  rather than closes."
- No editor-vocabulary label leakage (grepped, zero hits).

### Medium Issues Found

- **"repeated in their conclusions" overstated the recurrence.** The quoted
  Naskar & Joarder sentence occurs **once**, in §3.1. The Conclusions restate
  the deferral in *different words*: "Finding the explicit value of C0 for real
  environment inside neuron is very important … This is our proposed future
  work." **Fixed** to "a deferral their conclusions restate."

### Counterarguments Considered

- Ballentine's no-collapse reading remains in the article as an honest caveat.
  Unchanged strength; not re-litigated.
- The anti-Zeno asymmetry now runs *against* the Map's preferred mechanism and
  the page says so plainly. This is the article's principal virtue and was
  preserved without softening.

## Optimistic Analysis Summary

### Strengths Preserved

- The physics/speculation firewall, still exemplary and now three-layered:
  effect vs. interpretation, experiment vs. model, mechanism-category precedent
  vs. neural licence.
- The Kofman & Kurizki asymmetry paragraph is the strongest addition this file
  has taken since creation — it converts the anti-Zeno caveat from "the
  direction is not guaranteed" into "acceleration is the generic case", which
  is materially harder on the Map's own preferred channel.
- The Denton/Kominis four-bullet calibration block remains the corpus's
  authoritative single locus and is now quantitatively verified end to end.
- The "cite this calibrated statement rather than restate it" instruction to
  downstream articles: kept verbatim, it is doing real corpus-hygiene work.

### Enhancements Made

- I&F's own "was not measured directly" caveat surfaced into the article,
  which strengthens rather than weakens the paragraph's point: the warm-biology
  spectral literature is specific *and* provisional, and still never aimed at a
  neuron.
- Huh brought to its version of record.

### Cross-links Added

None. Integration wiring is complete and reciprocating.

## Length

2799 → 2840 words (+41) against concepts soft 2500 / hard 3500 —
`soft_warning`, 660 words of headroom. Above soft, so length-neutral discipline
applied: one offsetting trim taken in the Denton bullet ("On either budget the
precedent's regime is far shorter than a neural application needs"). The net
growth is entirely correction-carrying — the I&F caveat and the Fischer
multi-variable qualification — and no expansion opportunity was taken. Not a
condense target. Every existing hedge preserved
(condense-regresses-calibration-qualifiers).

## Remaining Items

None deferred. No follow-up task minted.

## Stability Notes

Bedrock disagreements (do **NOT** re-flag as critical) — carried forward from
2026-07-20 and re-confirmed:

- Physicalists and eliminative materialists reject quantum-interactionist
  dualism at the tenet boundary. The page marks the neural application
  undemonstrated rather than claiming refutation.
- Many-Worlds defenders reject the collapse presupposition. The No-Many-Worlds
  paragraph concedes the Zeno freezing still occurs as unitary dynamics under
  MWI and loses only its *selective* role — an honest boundary statement.

New stability note: **the article's own calibration is not the failure surface
here, and future reviews should stop looking for slippage in it.** Three
consecutive reviews have found the evidential-status discipline intact — the
physics is reported as established, the neural application as undemonstrated,
and the Kofman & Kurizki result is allowed to run against the Map's interest.
What this pass found instead was **five defects in the citation and empirical
apparatus, every one of them arrived after the last review, and four of them in
material written into the file by commits whose own reviews read a different
article**. The discriminator on this page is not "has the argument drifted" but
"who has read the newest paragraph against its source". Route the next review
at whatever has entered since 2026-08-21, not at the argument.

Second new note, methodological: **verify arXiv citations against the version
the citing text used.** This pass generated one false-positive fabrication call
and came within one edit of a second, both from checking v1 of a two-version
preprint. Cost: a correct clause deleted and restored inside the same session.