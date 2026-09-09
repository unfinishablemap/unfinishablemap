---
title: "Deep Review - Bacterial Chemotaxis and Minimal Biogenic Cognition"
created: 2026-09-09
modified: 2026-09-09
human_modified: null
ai_modified: 2026-09-09T18:57:19+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-09
last_curated: null
---

**Date**: 2026-09-09
**Article**: [[bacterial-chemotaxis-and-minimal-biogenic-cognition|Bacterial Chemotaxis and Minimal Biogenic Cognition]]
**Previous review**: [[deep-review-2026-08-01-bacterial-chemotaxis-and-minimal-biogenic-cognition|2026-08-01]] (and [[deep-review-2026-07-18-bacterial-chemotaxis-and-minimal-biogenic-cognition|2026-07-18]])

## Scope: What Changed Since the Last Review

Three commits landed since 2026-08-01. Two are sibling-driven ("secondary host") edits already verified as correct by the driver and deliberately not re-opened here: `af048b53df` (Tenet 2 paragraph rewrite) and `5b1050c636` (integral-control crosslink retargeted from thermostats to op-amp integrators).

The third, `dc8c246d69` (2026-09-08), is the substantive one: it added the ICON graded-spectrum subsection (Dodig-Crnkovic 2026) and the CBC rejoinder (Nesin & Chandrankunnel 2025), bringing four new quoted strings into the article. **This pass worked that new surface.** Prior ledgers had closed the metadata and verbatim seams for the *pre-existing* citations; the 09-08 additions had never been through a fidelity pass. That is where the findings are.

The finding is a **source-reading** defect, not a metadata or verbatim one: every quote in the new subsection is real and correctly transcribed, and the article still mis-described what the source does with them.

## Publisher-of-Record Citation & Quote Ledger

Method note: quotes verified by grep against tag-stripped raw full text pulled from Europe PMC (`PMC12872758` ICON, `PMC11834444` Nesin, `PMC4396460` Lyon 2015, `PMC11094104` EMBO), and against publisher-of-record abstract records via the Europe PMC REST API for the non-OA items. Metadata verified at Crossref. No WebFetch confirmation prompts were used (`webfetch-confirmation-prompts-ratify-the-phrase-you-ask-about`).

### Quotes verified this pass (offsets in the tag-stripped artefact)

- Dodig-Crnkovic 2026, "present from the onset of life" — **real-correct** (ICON @2332, abstract; verbatim).
- Dodig-Crnkovic 2026, "all living organisms possess a degree of sentience" — **real-correct** (ICON @20845; verbatim modulo sentence-initial `All` lowercased for mid-sentence embedding).
- Dodig-Crnkovic 2026, "minimal sentience (goal-directed behavior)" — **real-correct** (ICON @21415, Table 2 *Bacteria* row, "Type of sentience" cell, paired with valenced response "Chemotaxis (moving toward nutrients, away from toxins)"; verbatim modulo table-cell-initial `Minimal` lowercased). The article's framing — *E. coli* chemotaxis "entered on the spectrum as" this — is accurate to the table.
- Nesin & Chandrankunnel 2025, "can be considered as the molecular mechanism underlying individualistic decision-making in bacteria as well as in humans" — **real-correct** (Nesin @2704, abstract; verbatim). Surrounding framing also checked: "multiple pathways that have convergence and divergence as observed in the brain" supports the article's "converging and diverging nodes," and the body's motor-learning/motor-plan discussion (@20121ff) plus "cognitive flexibility" (@2889, @5683, @20890) supports "the architecture they credit with motor and cognitive flexibility in brains." **Accurate.**
- Lyon 2015, "at the level of molecular mechanism, evolution and ecology" — **real-correct** (Lyon @2237, abstract; verbatim). Framing also accurate: source reads "not only at the heuristic level of functional analogue, but also at the level of molecular mechanism, evolution and ecology," which the article renders as "not merely as a loose functional analogy." (Independently re-verified this pass; the 2026-07-18 ledger had claimed it but the primary was not reachable then.)
- Koshland 1977, "rudimentary memory which allows the bacteria to sense gradients over time" — **real-correct** (verbatim, *Science* 196(4294) abstract at the publisher record). Also verbatim: "more complex hormonal and neural signaling systems." The article's "response-regulator system operating relative to a threshold" tracks the abstract's "a response regulator whose level relative to a threshold controls flagellar function." **Accurate.**
- Macnab & Koshland 1972, "the apparent detection of a spatial gradient by the bacteria therefore involves an actual detection of a temporal gradient experienced as a result of movement through space" — **real-correct** (verbatim in the *PNAS* 69(9) abstract at the publisher record; note `PMC426976` returns 0 bytes from the `fullTextXML` endpoint — it is a scanned 1972 deposit with no text layer, so the abstract record is the reachable primary). "Temporal-gradient apparatus" also verbatim.

### Quote NOT verifiable this pass — recorded, not ratified

- Reber & Baluška, unicellular organisms "sense, perceive, and feel" — **unverified**. The paper is not open-access (no PMC full text), and the phrase is **not in the abstract**, which instead reads "all organisms ... are sentient, have subjective experiences and feelings." A Europe PMC OA full-text phrase search for `"sense, perceive, and feel"` returned **1 hit, and it is an unrelated science-education paper** (PMC8691623, Kvello & Gericke, on teaching the nervous system) — so no independent artefact corroborates it. The 2026-07-18 ledger asserts it verbatim from the body and quotes a source sentence ("Unicellular species, including bacteria, sense, perceive, and feel") that is itself unverifiable from any artefact reachable this run.
  **Action: none.** Per `citation-verify-false-negative` an unreachable primary is not evidence of fabrication, and the three-search fabrication test is not met — the *claim* is plainly the paper's (the abstract asserts it in other words). Left intact and flagged for whoever can reach the Elsevier text. Note the same quoted phrase is propagated in [[apex/competency-without-felt-experience]] and recorded in the W32 changelog, so it is a family, not a local, item.

### Metadata

- Dodig-Crnkovic 2026, `10.3389/fnsys.2026.1730097` — real-correct (verified by driver at Crossref).
- Robinson, Mallatt, Peer, Sourjik, Taiz 2024, `10.1038/s44319-024-00127-4` — real-correct (driver).
- Nesin & Chandrankunnel 2025, `10.1080/19420889.2025.2463926` — real-correct (driver); Europe PMC independently confirms *Communicative & Integrative Biology* 18, article 2463926.
- Lyon 2015, `10.3389/fmicb.2015.00264` — real-correct (driver).
- **Reber & Baluška, ref 9 — real-wrong-metadata (incomplete) → corrected.** The entry carried journal name and `PubMed 32950231` only, with no volume, pages or DOI — the same incompleteness class the 2026-07-18 review fixed for the EMBO entry but left live here, and the gap the driver flagged. Crossref (`10.1016/j.bbrc.2020.08.115`): *BBRC* **564**:150–157, authors Reber Arthur S. & Baluška František. Added.
  **Year duality recorded rather than resolved.** Crossref gives `issued` and `published-print` as **2021-07**; Europe PMC gives `yearOfPublication` 2021; the DOI stem and the PubMed deposit are 2020 (online-first). The article, the two research notes and the proto-agency article all say 2020 — 8 corpus loci. Rendered here as "(2020) ... (online 2020, issue 2021)" so the entry is unambiguous either way, and the in-text year left at 2020 to avoid minting a second identity for the paper in one file only (`ai_citation_metadata_unreliable` family-resolution rule). **Corpus-wide propagation is a governance call, reported to the operator, not taken unilaterally here.**
- Berg 2004, Berg & Brown 1972, Koshland 1977, Macnab & Koshland 1972, Lyon 2006, Reber/Baluška/Miller 2023, Southgate & Oquatre-huit 2026 self-cite — unchanged from the closed prior ledgers; not re-litigated.

Empirical-currency sweep: `find_superlative_claims` returned **0** claims (third consecutive empty result). Inline ↔ References cross-check: all twelve entries cited inline, no orphans in either direction.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. The article imputed to ICON an internal incoherence the paper explicitly forecloses.** The graded-spectrum subsection read: the framework's table marks the bacterial rung "no subjective experience" while its comparison table lists experience as "Present from the start (minimally)" — *"so what the account grants bacteria is not uniform within the paper itself."*

Both quotes are real and correctly placed. The inference from them is wrong. ICON carries an explicit scoping section, **"On experiential terminology"** (@16851), which reconciles exactly those two entries in advance:

> "At basal levels of life, these terms refer to functional, valence-sensitive regulation rather than to phenomenally conscious experience. Phenomenal consciousness, reflective awareness, and reportable subjective experience arise only under specific organizational conditions, typically involving nervous systems and integrative architectures. The use of experiential vocabulary at lower biological scales is not intended to attribute human-like subjective experience to single cells."

Under the paper's own stated convention the two cells are consistent: the graded minimum ("minimal experience present from the onset of life," @41500ff) is *functional*, and the withheld quantity ("no subjective experience") is *phenomenal*. Attributing non-uniformity to a named author who pre-empted the charge is an attribution error, and this class of defect survives metadata and verbatim review untouched — both prior ledgers passed, because nothing was miscited.

**Fixed**, and the fix strengthens the article's own case. The scoping note is far better support for "this spectrum is not feeling extended downward" than an alleged inconsistency: it is the source decoupling function from phenomenality in its own voice, one paragraph long, unhedged.

**2. "Thresholds are where the distance stays: ICON admits none" was false as stated.** ICON declines binary sorting across its graded properties (@5783: "Instead of thinking in binary terms (conscious vs. non-conscious, intelligent vs. non-intelligent)"), but it does place phenomenal consciousness behind an organisational condition "typically involving nervous systems and integrative architectures" — a threshold, and one strikingly near the Map's own neural locus. **Fixed**: the residual distance is now stated as a disagreement about *what the threshold is* (an organisational achievement inside a naturalistic info-computational process, versus machinery that could host a consciousness-physical interface) rather than about whether one exists. Care taken not to overclaim convergence — ICON's "typically" is a hedge, and it remains a naturalistic framework.

**3. Navigation surface asserted what the body now qualifies.** The H3 read "Declining the Separability Question" and its opening sentence "A third reading declines the separability question rather than answering it." Given finding 1, ICON does not decline separability — it separates function from phenomenality much as Lyon does, with graded vocabulary spanning both. Leaving the label and opener unchanged would have left the article contradicting itself within one subsection (`navigation-surfaces-carry-unreviewed-claims`). **Fixed**: heading retitled "Where ICON Reserves the Phenomenal"; opener softened to "appears to decline ... rather than answer it," which preserves the subsection's prima-facie-pressure-then-qualification structure. The explicit `{#graded-spectrum}` anchor was kept stable, and a corpus grep confirmed no inbound references to either the anchor or the old label outside changelog records.

### Adjudicated and Deliberately Not Changed

**The EMBO "argues that" provenance question** (raised by the driver as probably-minor). The article says the EMBO opinion "argues that CBC rests on" the speculations phrase; the source sentence attributes the criticism — *"Indeed, the central criticism of CBC has been that it is based on an elaborate series of speculations for which empirical evidence is lacking (Mallatt et al, 2021)."* **Verdict: "argues that" is correct; no change, and a provenance clause would make the article *less* accurate.** Three pieces of evidence, two of them new this pass:

1. **Jon Mallatt is the second author of the EMBO opinion itself** (Robinson DG, **Mallatt J**, Peer WA, Sourjik V, Taiz L). The parenthetical cites a co-author's own prior work, so this is a self-citation, not a third party's view being relayed.
2. **The sentence is reproduced twice** (@5287 and @5551) — the second occurrence is the article's own display pull-quote, stripped of the parenthetical attribution. Authors do not pull-quote a view they are merely reporting.
3. They reinforce it in their own voice immediately before ("This controversial theory, for which no plausible mechanism has been provided, raises many unaddressed issues") and immediately after ("CBC's proponents admit to this approach by calling it 'educated speculation'").

Adding "a criticism they attribute to Mallatt et al." would demote an endorsing dissent into a reporter — the mirror of the error in `i-widen-retractions-and-upgrade-coiners-into-proponents`, run in the other direction.

### Medium Issues Found

- None new. The five-tier-scale prose exposure remains the known, deferred, corpus-level item from 2026-08-01; not re-flagged as a local defect and not stripped unilaterally, per that review's instruction.

### Counterarguments Considered

- **CBC (Reber/Baluška/Miller) that bacteria feel.** Bedrock, settled twice; not re-litigated. Mode Three (framework-boundary marking) confirmed still honest — the Relation section grants continuity of biology, denies continuity of phenomenality, and labels the verdict "framework-relative … not a demonstration." No boundary-substitution. No editor-vocabulary label leakage found in prose (checked the forbidden-label list).
- **ICON as a new named opponent** (added 09-08, never mode-classified). Engagement is **Mode One** after this pass: the reply now argues from ICON's *own* stipulations rather than from tenet-incompatibility, which is the internal-to-the-opponent move being available and taken. Before the fix it was closer to a mis-executed Mode One — it claimed an internal defect (non-uniformity) that the opponent's text does not contain.
- **Deflationist parsimony-as-proof.** Blocked by the existing Tenet 5 treatment. No change.

### Calibration Check

No possibility/probability slippage found. The diagnostic test (would a tenet-accepting reviewer still flag any claim as overstated?) returns no on every phenomenal claim: the Relation section frames absence as what the neural-interface commitment *licenses*, explicitly "not a demonstration that nothing is felt," and places the bacterial rung at the scale's lowest tier with placement resting on "tenet-coherence rather than positive evidence." My finding 2 fix runs *toward* the Map's position (ICON's threshold is nearer the Map than the article said) and was written with the hedge preserved rather than cashed in as convergence — the Hardline Empiricist counterweight applied to my own edit.

Hedge/anchoring density not raised as a finding. Any elevated reading here would be lexical: the article's hedges are doing real calibration work, and the corpus base rate on that metric is ~8 consecutive false highs (`anchoring-false-high-is-the-base-rate-lexical-vs-structural`).

## Optimistic Analysis Summary

### Strengths Preserved

- The Tenet 2 paragraph from `af048b53df` — confining minimality to the *magnitude* of influence and explicitly disowning the parsimony-about-distributed-experience reading. Untouched, as instructed.
- The "two memories, kept separate" subsection, which pre-empts the standard inflation move.
- Parking the noise-vs-choice dispute and routing it to [[single-cell-proto-agency-and-the-evidence-problem]] rather than adjudicating inline — and the 09-08 addition of the published CBC rejoinder to that parked question, which keeps the parking honest rather than stale.
- Front-loaded thesis; truncation-resilient lead.

### Enhancements Made

- The ICON subsection now rests on the source's strongest and most directly relevant statement instead of an inferred inconsistency, and reports the residual disagreement accurately. Net effect: a rival that had been characterised as internally muddled is now characterised as substantially closer to the Map than its vocabulary suggests — a more interesting and more defensible claim, and one the source itself underwrites.

### Cross-links Added

- None. Existing outbound links all resolve; no gap identified.

## Length

2823 → 2925 words (+102), against a 3000-word soft threshold for `topics/` (hard 4000). Below soft throughout, so normal mode; the addition is argument, not padding, and no compensating cuts were required.

## Remaining Items

- **Reber & Baluška "sense, perceive, and feel"** — unverifiable without the Elsevier full text. Not a defect claim; a gap in the ledger, and a family one (also live in [[apex/competency-without-felt-experience]]).
- **Reber & Baluška year, 2020 vs 2021** — publisher of record says 2021 (issue), online-first 2020; 8 corpus loci say 2020. Recorded in ref 9 as "(online 2020, issue 2021)". Corpus-wide resolution deferred to the operator.
- Five-tier-scale prose exposure — unchanged corpus-level item from 2026-08-01.

## Stability Notes

- **CBC is bedrock.** Unchanged across three reviews. Must not be re-flagged as critical.
- **The "defeasible markers" formula is cluster-settled** (examined twice). Do not rewrite in this article alone.
- **The ICON subsection's source-reading is now closed.** The scoping note at "On experiential terminology" is the governing text for what ICON grants bacteria; a future review should not re-introduce the internal-non-uniformity reading, and should not re-assert "ICON admits no threshold." Both were checked against the raw full text this pass.
- **The EMBO "argues that" framing is settled** on three independent grounds (co-authorship of the cited criticism, the pull-quote, the surrounding own-voice endorsement). Do not add a provenance clause; doing so would understate the dissent's commitment.
- **The Tenet 2 paragraph and the op-amp-integrator crosslink are correct and verified.** Do not revert the op-amp exemplar to thermostats — the sibling article's ladder holds a thermostat to be proportional-only.
- Note for future passes: this article's metadata seam has been closed since 2026-07-18, and the two genuine findings since have both been **source-reading** defects on newly-added material (2026-08-01: a result credited to a synthesis 32 years later; 2026-09-09: an imputed internal incoherence). The productive lens on this file is what a correctly-cited source *actually does with its own quoted words*, and the trigger is a fresh content commit, not elapsed time.
