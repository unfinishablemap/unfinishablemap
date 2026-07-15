---
ai_contribution: 100
ai_generated_date: 2026-07-15
ai_modified: 2026-07-15 05:32:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-15
date: &id001 2026-07-15
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Atemporal Causation
topics: []
---

**Date**: 2026-07-15
**Article**: [Atemporal Causation](/concepts/atemporal-causation/)
**Previous review**: [2026-06-03](/reviews/deep-review-2026-06-03-atemporal-causation/) (8th review, converged-no-op confirmation)

## Selection Rationale & Task-Premise Correction

Consumed a queued P2 deep-review minted to hit the **owed-web-verify seam** (per the `owed-web-verify-seam-deep-review-targeting` discipline): citation-dense (10 numbered refs), `ai_contribution: 100`, `ai_system: claude-opus-4-6` (older cohort), last deep-reviewed 2026-06-03 (~42 days converged).

**Premise partially stale.** The task brief stated the article had "only ever been reviewed intra-corpus — never per-citation web-verified." This is **not** accurate: the **2026-06-02** review performed a full publisher-of-record web-verify pass with a per-cite ledger and fixed three attribution defects (Hensen→Vieira, Cramer-quote de-quote, Elitzur→Shushi); the **2026-06-03** review independently re-confirmed those fixes. This is the **9th** review of a strongly converged article.

**Genuine value-add this pass**: the **page-range field** was added to the web-verify audit spec this cycle (the Schaffer 2005 297-328→327-358 defect class), and was *not* explicitly in scope for the June passes. This review therefore re-ran the publisher-of-record verification with page ranges, issue numbers, and article numbers explicitly in scope, plus the two references (Price & Wharton 2013; page ranges on Adlam, Schurger, Aharonov-Cohen-Shushi) that the June ledgers marked "clean, well-established" without an explicit page check.

## Review Disposition

**No critical issues. No medium issues. No content edits.** Converged, clean, page-ranges-verified confirmation pass. Only `last_deep_review` bumped; `ai_modified` deliberately held at the HEAD value (2026-06-02T23:15:00+00:00 — the last genuine content edit) per the no-op discipline; `ai_system` **held at `claude-opus-4-6`** (older cohort, not re-authored — no attribution flip).

## Citation Web-Verification Ledger (publisher of record — page ranges in scope)

Per-cite, 3-state (`citation-verify-false-negative` discipline). Newly page/issue/article-number-verified this pass marked ✓NEW:

| Citation | State |
|---|---|
| Aharonov, Bergmann & Lebowitz (1964), "Time symmetry in the quantum process of measurement", *Phys. Rev.* **134(6B)**, B1410 | **real-correct** — vol/issue/page exact (re-confirmed; verified exact in 06-02). |
| Aharonov, Cohen & Shushi (2015), "Accommodating Retrocausality with Free Will", *Quanta* **5(1)**, **53-60**, arXiv:1512.06689 | **real-correct** ✓NEW — pages 53-60, vol 5, issue 1 confirmed (DOI 10.12743/quanta.v5i1.44). Third author Shushi confirmed (06-02 fix stands). *Year note*: Quanta journal-of-record dates the paper **2016**; arXiv preprint 2015. Article cites (2015) while listing both venues — a defensible dual-citation convention tracking the preprint, re-confirmed across 3 reviews; **not a defect**, not churned. |
| Adlam (2022), "Two roads to retrocausality", *Synthese* **200**, article **422** | **real-correct** ✓NEW — vol 200, article number 422 confirmed (DOI 10.1007/s11229-022-03919-0). Single author Emily Adlam. Stance paraphrase accurate. |
| Cramer (1986), "The transactional interpretation of quantum mechanics", *Rev. Mod. Phys.* **58(3)**, 647 | **real-correct** — canonical (vol 58, start page 647). No verbatim quote remains (the fabricated "occurs along the whole transaction" quote was de-quoted in 06-02; current text is paraphrase). |
| Kastner (2012), *The Transactional Interpretation of Quantum Mechanics: The Reality of Possibility*, Cambridge University Press | **real-correct** — title/publisher exact. |
| Price (2012), "Does time-symmetry imply retrocausality?", *Stud. Hist. Phil. Sci. B* **43(2)**, **75-83** | **real-correct** — pages 75-83 confirmed (re-confirmed; verified 06-02). Physics-vs-metaphysics framing matches Price's actual thesis. |
| Price & Wharton (2013), "Dispelling the Quantum Spooks — a Clue that Einstein Missed?", arXiv:1307.7744 | **real-correct** ✓NEW — arXiv ID, both authors, 2013 confirmed. Article truncates subtitle ("Dispelling the quantum spooks") — main title intact, acceptable abbreviation. *Minor*: no explicit inline `(2013)` anchor — the ref grounds the "Constraint Selection (Wharton/Price)" section, which cites both authors by name; a soft orphan of the same class as the by-name Schurger/Whitehead cites, accepted across 8 prior reviews. Not fixed (adding a parenthetical to converged, soft_warning-length prose is not warranted). |
| Schurger, Sitt & Dehaene (2012), "An accumulator model for spontaneous neural activity prior to self-initiated movement", *PNAS* **109(42)**, **E2904-E2913** | **real-correct** ✓NEW — page range E2904-13 = E2904-E2913, vol 109 issue 42 confirmed (DOI 10.1073/pnas.1210467109, PMID 22869750, ADS 2012PNAS..109E2904S). Cited honestly as a *defeater* condition, not as pro-Map. |
| Vieira, Ramanathan & Cabello (2025), "Test of the physical significance of Bell non-locality", *Nat. Commun.* **16**, **4390**, DOI 10.1038/s41467-025-59247-7 | **real-correct** — authors/vol/article confirmed (06-02 fix of the "Hensen" conflation stands; re-verified 06-03). "All-or-nothing" framing matches the paper's exclusion of partial retrocausal influence. |
| Whitehead (1929), *Process and Reality*, Macmillan | **real-correct** — first-edition publisher/year correct. "Concrescence" is Whitehead's own term. |

**Result: 10/10 references real-correct at publisher of record, page ranges included. Zero defects. Zero fabrications. No superseded superlatives** (no "current record / first-to-demonstrate" superlative claims tied to a cite — the empirical-currency sweep returns nothing to update).

## Verbatim-Quote Fidelity

**N/A — no verbatim sentence-quotes remain.** The only prior verbatim quote (Cramer 1986) was de-quoted in 06-02. Quoted strings in the current text are single technical terms — "handshake", "transaction", "concrescence", "en bloc", "all-at-once", "weak values" — each a genuine term of art of its source (Cramer/Whitehead/Wharton/Aharonov), not sentence quotations requiring publisher char-check. No self-contamination risk (nothing cross-checked against unfinishablemap.org).

## Citation-Framing Accuracy

Clean. No skeptic's-paper-cited-as-pro-Map inversion. Schurger 2012 and the four falsifier conditions are framed as *threats* to the view; Vieira 2025, Adlam 2022, Price 2012, and the TSVF/PTI sources are framed as the physics/metaphysics scaffolding the Map *adapts* — with the Map's original synthesis (consciousness as transaction selector) explicitly flagged as not the source authors' claim ("Kastner herself does not invoke consciousness as the transaction selector"; "Neither Wharton nor Price invoke consciousness").

## Calibration Check

Clean (re-confirmed). No possibility→probability slippage. The entire "Removing an Objection Is Not Providing a Mechanism" section holds objection-removal apart from mechanism-provision; "Not violation of physical law" preserves the load-bearing qualifier "the framework's design constraint rather than a demonstrated result"; interpretive frameworks flagged "all minority positions among physicists." A tenet-accepting reviewer would not flag any claim as overstated on the five-tier scale.

## Reasoning-Mode Check

No new named-opponent engagements since 05-10. Carried-forward Mode-Three (boundary-marking) classifications for Maudlin (TI critique), Schurger (classical reinterpretation), and decoherence theorists remain honest and editor-internal. No label leakage in prose.

## Length

`analyze_length`: unchanged from 06-03 (~3482 words, soft_warning, under the 3500 hard ceiling). Zero net change (no edits). EOF clean, no tool-call artifact.

## Remaining Items

- **Modern analytic precedent** (Dummett / Mellor on backward causation): deferred across 9 reviews. Correct to keep deferred — adding it breaches the hard ceiling without strengthening the argument.
- **Price & Wharton 2013 inline anchor**: soft orphan (by-name, no parenthetical year). Low priority; consistent with Schurger/Whitehead by-name citations. Not worth a prose edit on converged content.

## Stability Notes

Strong convergence: 9 deep reviews; the only defects ever caught post-merge were the three citation-metadata errors fixed 06-02, now re-confirmed AND extended to page-range/issue/article-number verification (clean). Bedrock disagreements (Empiricist "no distinguishing experiment", eliminative-materialist "metaphysical escapism", quantum-skeptic "rhetorical work", Buddhist substantive-self, MWI alternative) remain **bedrock** and must NOT be re-flagged as critical.

**Convergence signal**: zero edits this pass, and the page-range dimension (the one axis not previously in scope) is now verified clean. The owed-web-verify seam is **fully closed** for this article. A 10th review absent new content would be over-review — future triggers should require substantive content modification and should web-verify only newly-added citations.