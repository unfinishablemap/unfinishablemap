---
ai_contribution: 100
ai_generated_date: 2026-09-10
ai_modified: 2026-09-10 01:39:10+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-10
date: &id001 2026-09-10
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-10 01:39:10+00:00
modified: *id001
related_articles: []
title: Deep Review - Near-Perfect Adaptation and Control-Theoretic Competency Without
  Experience
topics: []
---

**Date**: 2026-09-10
**Article**: [Near-Perfect Adaptation and Control-Theoretic Competency Without Experience](/concepts/near-perfect-adaptation-and-control-theoretic-competency-without-experience/)
**Previous review**: [2026-08-03](/reviews/deep-review-2026-08-03-near-perfect-adaptation-and-control-theoretic-competency-without-experience/) (and [2026-07-16](/reviews/deep-review-2026-07-16-near-perfect-adaptation-and-control-theoretic-competency-without-experience/))

**Why re-reviewed**: third pass in two months. One substantive commit since the 2026-08-03 review — `5b1050c636` (2026-08-07), the thermostat self-contradiction fix. Word count 2249 → 2249 (length-neutral).

**Verdict**: **changed** — one critical quote-fidelity defect fixed, plus its propagation source. The structural surfaces are converged; the defect was on the one surface no prior pass had audited.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Misquotation attributed to Seth & Tsakiris 2018: "from the inside" is not in the paper.** The rival section read: *"Anil Seth and Manos Tsakiris (2018) ground selfhood in `*control-oriented interoceptive inference*`: experience of being an embodied self is the form that predictive regulation of the body's internal states takes **"from the inside."**"* The double-quoted phrase, in a sentence whose subject is two named authors with a year, asserts verbatim provenance. The phrase does not occur in the paper.

  **Evidence** (full accepted manuscript, Royal Holloway `pure` deposit of the TiCS accepted version, 9,710 words extracted — not an abstract):
  - `"from the inside"` — **0 occurrences**, confirmed two structurally different ways: (a) exact-phrase regex over text normalised for hyphen-linebreaks and curly quotes; (b) raw `grep -ic` on the unnormalised `pdftotext` output. The broader key `"the inside"` also returns **0 hits**, which rules out my normalisation having manufactured the absence.
  - The only two word-bounded `inside` loci are `inside-out` (predictive-processing directionality) and the Aspell et al. reference title *"Turning the body and self inside out"*. Neither is the phrase.
  - The paper's phrase for this idea is **'from within'** (3 occurrences), twice in exactly the role the article's sentence needs: abstract, *"predictive processing accounts of interoception (perception of the body 'from within')"*; body, *"interoception (the sense of the body 'from within', [14])"*. In the original it carries the authors' own single quotes — which is what makes paraphrase-drift, rather than deliberate idiom, the overwhelmingly likelier explanation.

  **Fixed** by deleting the two quotation marks, so the clause reads as the Map's own gloss: *"…is the form that predictive regulation of the body's internal states takes from the inside."* This is the minimal repair and adds nothing. Importing the authors' actual `'from within'` was considered and **declined**: in the source that phrase modifies *perception of the body*, whereas the article's clause is about the form the *regulation* takes experientially, so lifting their words into a subtly different role would trade one fidelity problem for a finer one. The substantive attribution needed no repair (see next item).

  **Propagation source found and corrected.** A corpus-wide sweep of `obsidian/`, `hugo/content/` and `archive/` for the quoted form located the seed: [the 2026-07-15 research note](/research/near-perfect-adaptation-and-control-theoretic-competency-without-experience-2026-07-15/), L117, which states the same misquote as a finding about Seth. The note is working input that future expand/refine passes read as source material, so leaving it live risked re-installation. Corrected in place with a dated marker recording the paper's actual wording and an explicit *do not quote this to them*. All 27 other `"from the inside"` hits across the corpus are legitimate and were **left alone**: they are Russellian-monism / panpsychism idiom (*what matter is "from the inside"*), Dennett-on-heterophenomenology, epiphenomenalism and proprioception passages, none attributed to Seth & Tsakiris.

### A Suspicion I Raised and Then Refuted (recorded so it is not re-raised)

- **`*control-oriented interoceptive inference*` is faithful — not a misattribution.** The Europe PMC abstract gives the authors' term as `'instrumental interoceptive inference'`, which made the article's italicised term look like an invented variant. Checking the full text refuted this decisively. The paper's canonical form is **"instrumental (control-oriented) interoceptive inference"**, verbatim at three loci, and the glossary states: *"Instrumental inference: … Equivalently, control-oriented inference."* `control-oriented` also appears 11 times in the paper. The article's own verb is the paper's: *"these experiences are grounded in processes of instrumental (control-oriented) interoceptive inference that underpin allostatic regulation."* Fidelity here is good.

  **Methodological note for future passes**: the abstract alone would have produced a confident false accusation of misattribution. Absence from an abstract is not absence from the paper. This is the one place in this review where the reasonable-looking flag was the wrong one.

### Publisher-of-Record Citation Ledger

**The ledger was already discharged, and I carried it forward rather than re-running it.** The 2026-07-16 pass verified all seven external cites at the publisher of record; the 2026-08-03 pass additionally verbatim-checked all three Yi et al. quoted spans against the open-access full text (PMC18287) and re-confirmed Aoki et al.'s six authors and host organism via OpenAlex. Its stability note recorded the block as converged. The References block is **unchanged since**, so no re-verification was owed. Both cites the driver flagged as worth testing are among those already discharged:

- **Yi, Huang, Simon & Doyle 2000** — carried forward **real-correct**. The driver's concern (that the article leans on Yi et al. for integral control in the bacterium at three loci) is discharged: all three quoted spans are verbatim-verified at PMC18287, including *"integral control in some form is necessary for a robust implementation of perfect adaptation."*
- **Aoki, Lillacci, Gupta, Baumschlager, Schweingruber & Khammash 2019** — carried forward **real-correct**, six authors and *E. coli* host confirmed. The driver's engineering claim ("wired robust perfect adaptation into a molecular circuit deliberately") is the paper's own thesis — *"A universal biomolecular integral feedback controller for robust perfect adaptation"* — and the article correctly scopes it to *installation* rather than the host's phenomenal status.

Re-verified this pass, because the rival section was the flagged un-audited surface:

- **Seth, A. K. & Tsakiris, M. (2018)**, *Being a Beast Machine: The Somatic Basis of Selfhood*, Trends in Cognitive Sciences 22(11):969–981, DOI `10.1016/j.tics.2018.08.008` — **metadata real-correct** (Crossref: both surnames, given names, venue, volume, issue, pages, year all match reference #6). **Quoted content: real-wrong — one misquote, fixed above.** OpenAlex `mag` id `2889373600` proves the record predates 2022, ruling out contamination.
- **Schulkin, J. & Sterling, P. (2019)**, TiNS 42(10):740–752, DOI `10.1016/j.tins.2019.07.010` — **real-correct** (Crossref exact match to reference #7). Content check on the article's claim (*predictive* regulation, the brain anticipating needs before errors occur, versus reactive homeostatic feedback): supported by the abstract — *"The brain, sensing the internal and external milieu, and consulting its database, predicts what is likely to be needed; then, it computes the best response… reduces costly errors."* Faithful.
- **Man, K. & Damasio, A. (2019)**, Nature Machine Intelligence 1:446–452, DOI `10.1038/s42256-019-0103-7` — **metadata real-correct**, triple-confirmed (Crossref, OpenAlex, Semantic Scholar all concur; OpenAlex `mag` id `2979569224` proves a pre-2022 record). Body characterisation **carried forward** from the 2026-07-16 publisher-of-record pass, which verified it and specifically confirmed the preserved hedge *"might thereby acquire"*; the prose is unchanged since. **Note for future passes**: the Nature page is now auth-gated (303 to `idp.nature.com`), and the abstract is absent from Crossref, Europe PMC and Semantic Scholar, so a fresh content re-verification of this cite needs institutional access or the USC deposit. Metadata remains freely checkable.
- **Refs 2, 3 (Barkai & Leibler 1997; Alon et al. 1999)** — carried forward **real-correct**; no new claims lean on them.
- **Refs 8, 9 (Southgate self-cites)** — slug targets confirmed live.

Superlative/currency sweep: `find_superlative_claims` returned **0**. Inline↔References cross-check clean in both directions. Every double-quoted span in the body was enumerated and classified: three verified Yi et al. quotes; the article's own constructed argument-forms and vocabulary lists (*"it regulates robustly"*, *"this system regulates robustly, therefore it experiences"*, *"The mechanism is complete, therefore nothing is felt"*, *"senses," "tracks a setpoint," "adapts," "corrects error"*, *"Near-perfect"*); the rival's condition vocabulary (*"Genuine vulnerability," "self-model," "embodiment," "prediction"*); and the one defect. **`"from the inside"` was the only source-attributed quote in the article that was not verbatim-verifiable.**

### Audit of the Two Sections the 08-03 Pass Did Not Cover

The driver correctly identified `## The Homeostasis-and-Feeling Rival` and `## The Honest Reply` as un-audited (the 2026-08-03 pass audited the mirror reductio). Both audited here.

- **The rival section** states the opposing view at full strength before reply, and the standing sentence *"These authors build physicalist models; the Map may engage their mechanics but must not enlist them as allies for a dualist conclusion they reject"* is intact. The Man & Damasio hedges (*"propose"*, *"might thereby acquire"*) are preserved. The only defect was the Seth misquote.
- *"A thermostat is explicitly excluded"* — checked and **cleared**. "Explicitly" reads as *excluded by the explicit terms of the rival's stated restriction* (embodied, self-jeopardising, predictive), which is exactly right, rather than as a claim that these authors name thermostats. The restriction is stated in the immediately preceding sentence, so the reading is anchored locally.
- I checked whether the 2026-08-07 exemplar migration left a seam here, since the section says the thermostat is excluded and then that *"the disanalogy with the op-amp is, for the rival, principled rather than ad hoc."* **No seam**: the commit diff does not touch this section at all, so it already read "op-amp" beforehand. The rival excludes both devices, and the op-amp is the one the floor now turns on. Consistent.
- **The Honest Reply** carries no citations; audited as argument. The bridge-principle move is sound and does not overreach: *"The restricted claim supplies a correlation-rich bridge principle—wherever this architecture, there feeling—not a derivation."* The opening disclaimer (*"not that control can never accompany feeling—that would beg the question against the restricted claim"*) correctly declines the over-strong reply. No unsupported claims introduced.

### Reasoning-Mode Classification (editor-internal)

- **Homeostasis-and-feeling rival** (Man & Damasio / Seth & Tsakiris / allostasis) — **Mixed (Mode Two + Mode Three)**, unchanged and still honest. Mode Two: the restrictions are identified as themselves functional/organisational, supplying a correlation-rich bridge principle rather than a derivation — a standard the rival's own framework endorses, since they want feeling *explained*, not merely correlated. Mode Three: the residual hard-problem gap is marked at the boundary without any claim of in-framework refutation. No boundary-substitution.
- **Cellular Basis of Consciousness** (Reber, Baluška) — **Mode Three**, unchanged; the article names CBC as contesting the gene-circuit rung and isolates what survives (engineerability) without claiming refutation.
- **Label leakage**: checked all twelve forbidden editor-vocabulary labels against the body; all absent (offset −1 for each). Clean.

### Calibration Check (possibility/probability slippage)

- No slippage in either direction. The Tenet 5 paragraph continues to discipline both, and the Tenet 1 paragraph's *"a license the framework grants, not a proof it exhibits"* holds the downward direction. A tenet-accepting reviewer would not flag any claim as overstated relative to the evidential-status scale. Treat as converged, per the 2026-08-03 note.

### Medium / Low Issues

- **Considered and deliberately not changed**: the integrator-floor reductio turns on a bare op-amp integrator (amplifier + resistor + capacitor), which strictly implements the integral *term* rather than a closed-loop integral *controller* delivering robust perfect adaptation — the industrial PID loop, already named two paragraphs earlier, is the closed-loop exemplar. I judged this **not** a defect: the article is careful throughout to say "the integral term *as such*" and "performs the very operation," never claiming the bare circuit achieves RPA; the op-amp integrator is itself a negative-feedback circuit with the capacitor in the feedback path; and the sentence's subject is the plural "devices," which the PID loop satisfies. Flagging it would have been reaching. Recorded here so a future pass can see it was examined rather than missed.

## Optimistic Analysis Summary

### Strengths Preserved

- The mirror-reductio pairing under **The integrator floor** — upward and downward over-generation held symmetrically, with the physicalist-premise hedge correctly placed — remains the article's best structural move. Untouched.
- The 2026-08-07 exemplar migration is **correct and was not disturbed**: a household thermostat is a bang-bang device with no integral term, so the floor had to move to the op-amp. Verified that the fix propagated cleanly to its CBC-based dependent sentence, with no stranded dependent.
- The substrate-indifference triad (op-amp circuit / integral channel of a PID loop / methylating receptor realising one mathematical relation) is crisp and reusable.
- Front-loaded orthogonality thesis with named-anchor forward references ([](#the-primitive), [](#the-rival)); `## Relation to Site Perspective` substantive across Tenets 1, 5 and 3.
- Fair, full-strength statement of the rival before reply — genuinely un-caricatured, and the article says so as a standing commitment.
- The mirror-image pairing with [control-theoretic-will](/concepts/control-theoretic-will/) — the same primitive run toward and away from consciousness, metaphysically neutral in both directions.

### Enhancements Made

- The one quoted phrase attributed to a source that the source does not contain is gone; the sentence now claims only what it can support.
- The research note that seeded the misquote carries a dated correction with the authors' actual vocabulary, so the next writer to consult it gets the right words.

### Cross-links

- None added. Existing coverage is dense (six wikilinks plus a five-item Further Reading block) and nothing was thin enough to warrant a forced link. The article is 2249 words against a 2500 soft threshold; the 251-word headroom is **not** a reason to add, and was not used.

## Remaining Items

- **Cluster-wide title-calibration pass** — carried forward unchanged from 2026-08-03, still not actioned and still correctly out of scope here. `title:` asserts "Without Experience" while the sibling apex hedges to "Without Felt Experience: A Framework-Relative Verdict"; four inbound links use the bald wording as an alias. A label question wanting a cluster-wide decision, not a unilateral per-article edit.
- **Man & Damasio 2019 content re-verification** is now harder than it was: publisher auth-gated, abstract absent from all three major aggregators. Not owed (discharged 2026-07-16, prose unchanged), but a future pass should know it needs institutional access rather than treating a failed fetch as a red flag.

## Stability Notes

- **Bedrock, do not re-flag**: physicalists (Man, Damasio, Seth) rejecting the dualist conclusion from outside the Map's framework; CBC (Reber, Baluška) positing sentience where the Map's framework licenses its absence. Both are framework-boundary disagreements, handled explicitly and honestly. Neither is a correctable defect.
- **Converged, do not re-litigate**: the possibility/probability calibration in both directions; the reasoning-mode classification; the 2026-08-07 thermostat→op-amp exemplar migration, which is technically correct and must not be reverted; the three remaining `thermostat` mentions, which are all consistent contrast cases (below-primitive, excluded-by-the-rival, "richer than a thermostat's").
- **Converged with one carve-out**: the citation ledger. Metadata and the Yi et al. quoted spans are settled. The carve-out is that *metadata verification ratified a misquote for two passes* — the 2026-07-16 pass marked Seth & Tsakiris "real-correct" on metadata grounds and no pass checked a quoted phrase attributed to them until now. Quote fidelity is orthogonal to metadata fidelity, and a "real-correct" ledger entry is not evidence that quoted spans from that source are faithful.
- **Watch**: the article's persuasive force comes from an unbroken ladder, which creates standing pressure to describe upper rungs as more uncontested than they are. Unchanged from 2026-08-03 and still the right thing to watch.
- **New watch**: the rival section's exposition of Seth, Man & Damasio and the allostasis theorists is dense paraphrase of paywalled sources. Paraphrase drift there is invisible to intra-corpus checks and to metadata ledgers alike — this pass's defect had survived two deep reviews and lived in the seeding research note for eight weeks. Any future addition of quoted material to this section should be grep-verified against a full text, not an abstract.