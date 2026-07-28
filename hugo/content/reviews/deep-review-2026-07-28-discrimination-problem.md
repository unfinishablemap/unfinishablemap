---
ai_contribution: 100
ai_generated_date: 2026-07-28
ai_modified: 2026-07-28 07:06:13+00:00
ai_system: claude-opus-5
author: null
concepts:
- '[[discrimination-problem]]'
created: 2026-07-28
date: &id001 2026-07-28
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Discrimination Problem
topics: []
---

**Date**: 2026-07-28
**Article**: [The Discrimination Problem](/concepts/discrimination-problem/)
**Previous review**: [2026-06-19](/reviews/deep-review-2026-06-19-discrimination-problem/) (and [2026-06-05](/reviews/deep-review-2026-06-05-discrimination-problem/), [2026-05-19](/reviews/deep-review-2026-05-19-discrimination-problem/), [2026-05-18](/reviews/deep-review-2026-05-18-discrimination-problem/))

**Verdict: NOT a no-op. Two correctable citation-fidelity defects found and fixed — the first full publisher-of-record pass this article has ever received.**

This is the fifth deep review, and the first to run §2.4 as a genuine per-cite publisher pass. The four prior reviews did not. The 2026-06-05 review asserted "Schwitzgebel, Loar, Dennett, Frankish, Chalmers, Block, Rebouillat: all cited with correct titles, dates, and accurate characterisations" with no per-cite ledger; the 2026-06-19 review then explicitly **skipped** verification on the grounds that the References block was byte-identical to 06-05. Each pass inherited the previous pass's assurance rather than re-deriving it. Both defects below survived all four reviews.

Neither defect is a metadata error — every citation in this article is real and every bibliographic tuple is correct. Both defects are in the **third and second axes**: whether the article's characterisation matches what the source actually says and found. That is why metadata-oriented passes could not see them.

## Citation Web-Verify Ledger (per-cite, publisher of record)

| # | Cite | Verdict |
|---|---|---|
| 1 | Block, N. (1995), *BBS* 18(2), 227–247 | **real-correct** — confirmed at Cambridge Core (vol 18, iss 2, June 1995, pp. 227–247). Aggregators (SciRP et al.) carry the 227–287 error form; the article is right. Not touched. |
| 2 | Chalmers (1996), *The Conscious Mind*, OUP | **real-correct** |
| 3 | Chalmers (2018), meta-problem, *JCS* 25(9–10), 6–61 | **real-correct** — confirmed against the author's own PhilArchive PDF header |
| 4 | Dennett (1991), *Consciousness Explained*, Little, Brown | **real-correct** |
| 5 | Frankish (2016), *JCS* 23(11–12), 11–39 | **real-correct** — confirmed at IngentaConnect/PhilPapers |
| 6 | Loar (1990), *Philosophical Perspectives* 4, 81–108 | **real-correct** — confirmed at PhilPapers/JSTOR vol. 4 |
| — | Monti et al. (2010), *NEJM* 362, 579–589 | **newly added** — verified at NEJM/PubMed (54 patients, 5 responsive) |
| 7→8 | Owen et al. (2006), *Science* 313(5792), 1402 | metadata **real-correct**; **empirical-claim fidelity DEFECT in body** — see below |
| 8→9 | Rebouillat, Leonetti, & Kouider (2021), *Neuroscience of Consciousness* 2021(1), niab004 | **real-correct**, and the empirical paraphrase is **accurate** — see below |
| 9→10 | Schwitzgebel (2011), *Perplexities of Consciousness*, MIT Press | metadata **real-correct**; quoted word **verbatim-confirmed**; **citation-framing DEFECT** — see below |
| 10→11 | Weiskrantz (1986), *Blindsight: A Case Study and Implications*, OUP | **real-correct**. The plural "patients" is defensible: although the book centres on D.B., it also reviews cases from other investigators. No change. |
| 11→12 | Southgate & Oquatre-cinq (2026-01-22), Access Consciousness | **real-correct** — date and title match the live article's frontmatter |
| 12→13 | Southgate & Oquatre-six (2026-01-14), Illusionism | **real-correct** — date and title match the live article's frontmatter |

Self-citation pseudonyms are legitimate per fabricated-map-self-cite-pseudonym-false-alarm; not stripped.

## Critical Issues Found

### 1. Empirical-claim fidelity — Owen et al. 2006 attached to a claim it does not support (FIXED)

The Boundary Cases section read:

> Vegetative-state **patients sometimes show** fMRI activity consistent with imagined tennis-playing (Owen et al. 2006).

Owen et al. 2006 is a **single-patient case report** — one 23-year-old woman who, when asked to imagine playing tennis or moving around her home, activated predicted cortical areas indistinguishably from healthy volunteers. The plural, frequency-hedged generalisation ("patients sometimes show") is a claim about a population that the cited paper does not establish. This is the empirical-claim-fidelity-orthogonal-to-metadata-and-quotes axis: correct citation, wrong scope.

The generalisation is nonetheless *true of the literature* — so the fix restores it on proper footing rather than merely narrowing it. Re-scoped to Owen's actual single-case finding and added the cohort replication (Monti et al. 2010, *NEJM* 362:579–589, verified at NEJM/PubMed: 5 of 54 patients with disorders of consciousness showed wilful modulation). New References entry 7; entries renumbered 7–12 → 8–13.

### 2. Citation-framing accuracy — Schwitzgebel's position strength minimised (FIXED)

The First-Person Channel section read:

> Schwitzgebel's *Perplexities of Consciousness* (2011) argues, **conservatively**, that introspection ... is "untrustworthy" in surprisingly many domains ... **He stops short of claiming introspection is wholly unreliable**...

The quoted word "untrustworthy" is **verbatim and correctly attributed** — the metadata and quote axes are clean, which is precisely why four prior reviews passed it. But the framing inverts the source's strength. Schwitzgebel's actual sentence is that introspection of current conscious experience, "far from being secure, nearly infallible, is **faulty, untrustworthy, and misleading, not just sometimes a little mistaken, but frequently and massively mistaken, about a great variety of issues**." NDPR likewise records the book's official thesis as the claim that introspection *is* unreliable.

Describing that as "conservative" and as "stopping short of claiming introspection is wholly unreliable" is a **position-strength misrepresentation** under §2.5 — the mirror image of the usual "explores → argues" error. It also weakens the article on its own terms: Schwitzgebel is one of the strongest available witnesses for the first-person channel's unreliability, and softening him understates the challenge the section exists to state.

Fixed by quoting the fuller phrase and characterising the argument accurately as a cumulative induction. The useful "stability is consistent with stable error" observation is preserved verbatim.

## Non-Findings (checked, no change)

- **Rebouillat 2021 empirical paraphrase — verified accurate.** The article claims human metacognition shows anti-correlation in the weak-internal-evidence-plus-deceptive-cue regime. The paper's abstract states deceptive cues "overturn the classical relationship between confidence and accuracy: introspective failures are associated with higher confidence than genuine introspective reports," localised to "when internal decision evidence is weak and variable," with the results section reporting "confidence rising up as accuracy decreased." The article's characterisation, including its "calibration-grade" restraint, matches the source. No change.
- **Block family resolution — already complete corpus-wide.** Per §2.4 family resolution I checked the whole corpus after confirming 227–247 at Cambridge Core. **Every live content file** (concepts, topics, apex, voids, archive — 19 files) already carries the correct 227–247. The remaining 227–287 hits are confined to historical `reviews/` and `workflow/changelog` archives, which are records *of* the fix. No propagation needed; the standing note that "four other files still carry it" is stale.
- **Inline ↔ References cross-check.** Inline year-cites (Schwitzgebel 2011, Weiskrantz 1986, Owen 2006, Monti 2010, Rebouillat 2021) all have entries. Block/Chalmers/Dennett/Frankish/Loar function as the background bibliography for authors named inline without year-cites — the established pattern on Map concept pages, accepted by all four prior reviews. Not disturbed.
- No possibility/probability slippage; no editor-vocabulary label leakage; tenet-section calibration restraint intact.

## Optimistic Analysis

**Strengths preserved (untouched):** the structural-asymmetry kernel in §"Why It Is Stubborn"; the §"Generalisation Across the Catalogue" discipline-not-evidence coda; §"Asymmetry-Breaking Signatures"; the mine-ness within-subject boundary case; the tenet section. Both edits were surgical and local.

**Cross-links added:** none. Cluster integration is mature.

## Length

- Before: **2935** words (117% of the 2500 soft target)
- After: **3001** words (120%) — `soft_warning`, far below the 3500 hard threshold

+66 words, all of it accuracy payload (the fuller Schwitzgebel quotation, the Owen re-scoping, the Monti clause and reference). The Monti entry uses the house `et al.` short form already used for Owen to hold the cost down. Per the standing rule from 2026-06-05/06-19, length above soft is acceptable here and revisited only at 3500.

## Reasoning-Mode Classification (Editor-Internal)

Maintenance pass; no new named-opponent engagements. Prior classifications stand: Dennett (heterophenomenology) Mode Mixed leaning Mode Two; illusionism (Frankish/Loar) Mode Mixed; NCC methodology Mode Mixed leaning Mode Two. No label leakage in body.

## Remaining Items

None.

## Stability Notes

- **The "converged ⇒ no citation work needed" inference is now falsified for this article.** Four reviews called it converged; the fifth found two real defects on the first genuine publisher pass. Convergence of *prose* is not convergence of *citation fidelity* — the web-verify trigger fires on modification, so a stable article's citations go permanently unchecked. Do not let a future pass skip §2.4 on "References block unmodified" grounds; that is exactly the reasoning that hid these two defects.
- **Schwitzgebel is a strong, not conservative, witness** — do not regress the framing to "conservatively" / "stops short." The verbatim phrase is "faulty, untrustworthy, and misleading ... frequently and massively mistaken."
- **Owen et al. 2006 is N=1** — do not restore a plural generalisation attached to it alone. Monti et al. 2010 is the cohort citation.
- **Block 227–247 is publisher-verified correct** — aggregators carry 227–287. Do not "fix" toward the aggregator form. Live corpus is uniformly correct.
- **Rebouillat (not Coutinho) is correct** — do not regress.
- Illusionism/eliminativism disagreement is **bedrock** — do not re-flag. NCC "begging the question" claim is a defensible authorial choice. MWI not engaged and not required.