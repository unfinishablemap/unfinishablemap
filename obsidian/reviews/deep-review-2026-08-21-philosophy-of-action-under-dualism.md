---
title: "Deep Review - Philosophy of Action under Dualism"
created: 2026-08-21
modified: 2026-08-21
human_modified: null
ai_modified: 2026-08-21T11:58:32+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-21
last_curated: null
---

**Date**: 2026-08-21
**Article**: [[philosophy-of-action-under-dualism|Philosophy of Action under Dualism]]
**Previous review**: [[deep-review-2026-07-18-philosophy-of-action-under-dualism|2026-07-18]]

## Convergence Context

Third deep review; the 2026-07-18 pass found the article converged and predicted no-ops "absent new citations or substantive content additions." A substantive addition arrived on 2026-08-21: commit `4650f1ac25` (refine-draft, folding `research/deviant-causation-bci-mediated-action-2026-08-20`) installed a **new inline citation (Yashin 2025)** plus three sentences of paraphrase into the Deviant Causal Chains section, added a References entry, and added one `related_articles` and one Further-Reading link.

That insertion is the classic unreviewed-outbound-crosslink case: the fork's actual subject was `brain-computer-interfaces-and-the-interface-boundary`, and the sentences it wrote *into this article* were never read by any review of this article. The §2.4 trigger fired (new inline cite, References block modified), so this pass is a real one, not a no-op — and it found two attribution defects in the inserted text.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Overstated position strength on Yashin's verdicts (§2.5 Position Strength / dropped qualifier).** The inserted sentence read:

> Yashin (2025) argues the BCI cases invalidate the sensitivity and well-functioning repairs **outright** and **force the debate onto reliability** …

Neither half survives the source. The originating research note flagged this explicitly ("the MDPI PDF was never retrieved and all Yashin material is paraphrase"), and the paraphrase over-strengthened in two places. Full text retrieved this pass (reader proxy; MDPI blocks direct fetch with HTTP 403) and grep-checked against §3, §5 and §6:

- **"outright" is wrong — the sensitivity verdict is scoped.** Yashin §3: the sensitivity strategy fails "in a BCI with a limited set of discrete operations", where "minor alterations in intention do not change the outcome." He also names *sustaining causation* alongside sensitivity (same discrete-operations reason), and holds that the *immediacy* strategy "faces significant challenges" rather than being invalidated. The article's two-item list presented as an outright invalidation misstates both the scope and the roster.
- **"force the debate onto reliability" is wrong — reliability is a direction, not a forced conclusion.** Yashin §6: "the reliability strategy appears to be a promising approach"; §5: "I do not propose a complete solution to the problem of deviant causal chains… However, the reasoning presented so far points in a promising direction."
- **The boundary demand was mis-attached.** The article made the boundary analysis a requirement *of the reliability strategy*. Yashin attaches it to evaluating deviance in machine-mediated action generally: "a general theory still requires additional analysis to determine the boundaries of the system enabling action", and Case 2 vs Case 3 turns on "whether it occurs inside or outside the system that enables action." Bodily movement is exempt because "the boundaries of the body are well-defined."

*Resolution*: paragraph rewritten to Yashin's own strength and scope. The well-functioning reason (BCI functions are "the result of purposeful design" rather than evolved) was verified correct and kept. "No proposed repair commands consensus" moved up to close the survey of repairs, so the paragraph now ends on the Map's own relocation.

**2. Family resolution — the same over-strengthening in the sibling host.** The same fork wrote the fuller version into [[brain-computer-interfaces-and-the-interface-boundary]] ("BCI cases invalidate the standard anti-deviance repairs… What survives is a reliability strategy"). Per §2.4.6, corrected there in the same pass rather than left as a live string sibling: "renders several of the standard anti-deviance repairs invalid", sensitivity scoped to limited-discrete-operation interfaces, "judges reliability strategies the promising direction—while declining to offer them as a complete solution", and the body-boundary exemption stated as Yashin states it.

**3. Root correction in the research note.** `research/deviant-causation-bci-mediated-action-2026-08-20` carried the same claim in its executive summary and left an open verification ceiling ("Before quoting Yashin verbatim… retrieve the PDF"). Both corrected: the ceiling is marked RESOLVED with the retrieval date and the two corrections recorded, so a future consumer of the note does not re-mint the overstatement.

### Publisher-of-Record Citation Ledger (§2.4)

- Yashin, A. S. (2025). Causal Deviance in Brain–Computer Interfaces (BCIs)… *Philosophies*, 10(2), 37 — **real-correct metadata** (Crossref + OpenAlex agree: sole author Artem S. Yashin, published 2025-03-25, vol 10 iss 2, article/page 37, DOI `10.3390/philosophies10020037`). Title corrected to the canonical **en dash** ("Brain–Computer") and author initials spaced, in both host articles. **Paraphrase corrected** — see Critical Issues 1–2. Full text retrieved and grep-verified this pass; the note's standing verification ceiling is discharged.
- Ward, S. (2024). PPR 108(2), 374–395 — real-correct (Crossref `10.1111/phpr.12977`; online-first 2023-04-26, **print issue March 2024**, so the 2024 year as cited is the issue year and correct).
- Pereboom, D. (2014). *Philosophical Studies* 169(1), 59–69 — real-correct (Crossref `10.1007/s11098-012-9899-2`; online-first 2012, **print issue May 2014**; given name "Derk" correct in body and references).
- Lowe, E. J. (2006). *Erkenntnis* 65(1), 5–23 — real-correct (Crossref confirms venue, volume, issue, pages, 2006).
- Anscombe 1957, Chisholm 1964, Davidson 1963, Hornsby 1980, Lowe 2008, O'Connor 2000 — carried forward from the 2026-07-06 full web-verify and unmodified since; no re-verification trigger.
- Southgate & Oquatre-sept 2026 / Southgate & Oquatre-six 2026 — Map self-cites (legitimate AI-pseudonym convention; never strip).

Cross-reference check: every inline cite has a References entry and every References entry is cited inline or in Further Reading. Superlative/currency sweep (`find_superlative_claims`) returned **0** claims — no empirical-record drift surface.

### Medium Issues Found

- **References list looseness.** The 2026-08-21 insert left a blank line before item 10, turning a tight ordered list into a loose one (every entry wrapped in `<p>`). Removed.

### Low Issues Found (deferred, with reason)

- **"panicky metaphysics" is a quoted span with no attribution.** The phrase is Strawson's ("the obscure and panicky metaphysics of libertarianism", *Freedom and Resentment*, Proc. Br. Acad. 48, 1–25, 1962 — metadata verified). Attribution was **not** added because the verbatim span could not be grep-verified at a primary text this pass: the British Academy PDF 403s and two mirrors failed to retrieve. Per quote-fidelity discipline an unverified quoted attribution is worse than none, so the phrase stays as an unattributed term of art. A future pass with the primary text in hand can attribute it and add the Strawson reference entry.

### Attribution Check (§2.5)

- Misattribution: none remaining after the Yashin fix. Davidson's causal skeleton is borrowed with the monism explicitly rejected; Lowe's substance-causation regress-stopper is his own view; the Anscombe reconciliation is still flagged as the Map's move, not hers.
- Qualifier preservation: the Yashin fix **is** the qualifier restoration ("in a BCI with a limited set of discrete operations", "promising" not "forced").
- Position strength: corrected — see Critical Issue 1.
- Source/Map separation: intact. The new final clause ("no boundary an engineer could draw is the one that fixes authorship") is clearly the Map's reply, syntactically separated from Yashin's argument and hyperlinked to where the Map argues it.
- Self-contradiction: none. The new material and the closing "Deviance is relocated, not removed" agree on the same relocation.

### Reasoning-Mode Audit (editor-internal)

- Davidson — Mode Three (framework boundary: monism vs dualism; causal skeleton borrowed, boundary honestly marked). Unchanged.
- Pereboom's disappearing agent — in-framework repair; the objection is met on its own "too thin" terms. Unchanged.
- Anscombe — Mode Three with the reconciling move disclaimed as the Map's own. Unchanged.
- **Yashin (new) — Mode Three.** The Map does not refute Yashin inside his framework; it relocates the junction on tenet grounds and says so. The revised text now marks that boundary rather than implying the reliability debate has been won. The sibling article states the same limit explicitly ("a commitment flowing from the Map's… tenets, not a refutation of reliability strategies on their own ground").
- Label leakage: grep-clean (no editor vocabulary, no `Evidential status:` callouts, no "This is not X. It is Y.", no stray "load-bearing").

### Counterarguments Considered

- *Quantum Skeptic / Empiricist*: the mind→quantum-selection junction is unverifiable. Already owned by the article's closing epistemic-residue paragraph and the [[agency-void]] hand-off. Not re-flagged.
- *Hardline Empiricist (calibration check)*: the article makes no evidential-status claim about an empirical matter — it is metaphysics selecting among theories of action. No possibility/probability slippage found. The one place tenets do work ("Occam's Razor Has Limits") is explicitly limited: the tenet "does not license the posit; it only refuses to let parsimony *veto* it."

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded lead naming the selected position and both motivating failure points before any survey — untouched.
- The calibration paragraph on parsimony, which declines exactly the tenet-as-evidence-upgrade move the Hardline Empiricist watches for.
- "Deviance is relocated, not removed" — the article's most honest passage, and now better supported: the survey section it depends on no longer overclaims that the mainstream repairs have been settled.

### Enhancements Made

- The Yashin engagement is now *more* informative than the overstated version it replaces: it names the mechanism of the sensitivity failure (discrete operation sets) and the mechanism of the well-functioning failure (design vs evolution), where the old text asserted only that they were invalidated.
- Paragraph now closes on the Map's own position rather than trailing into a concessive fragment.

### Cross-links Added

- None new. The 2026-08-21 additions ([[brain-computer-interfaces-and-the-interface-boundary]] in `related_articles`, Further Reading, and the section-anchored inline link) were verified: target file exists and the `#whose-action-is-a-decoded-movement` anchor resolves to the "## Whose Action Is a Decoded Movement?" heading.

## Word Count

2475 → 2556 (+81; 85% of the topics/ 3000 soft threshold). Below soft threshold, so normal mode; the addition is net-informative rather than padding.

## Remaining Items

- Strawson attribution for "panicky metaphysics" — deferred pending primary-text retrieval (see Low Issues).

## Stability Notes

- Davidson's anomalous monism, physicalist/MWI rejection of quantum interactionism, and eliminativist rejection of substance-agency remain **bedrock framework-boundary disagreements**. Do not re-flag.
- The "panicky metaphysics" extravagance charge is acknowledged and bounded by Tenet 5; not a fixable flaw.
- **New standing note**: this article is a *secondary host* for material written by forks working on other articles (the 2026-07-10 anomalous-monism link and the 2026-08-21 Yashin insert both arrived that way). Its `ai_modified` bumps therefore often mean "someone else's fork wrote here", and those sentences carry no review history of their own. Future passes should diff since `last_deep_review` and treat any inserted citation as unverified until checked at the publisher of record, regardless of how converged the rest of the article is.
