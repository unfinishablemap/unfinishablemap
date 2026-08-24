---
ai_contribution: 100
ai_generated_date: 2026-08-24
ai_modified: 2026-08-24 17:39:05+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-24
date: &id001 2026-08-24
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-24 17:39:05+00:00
modified: *id001
related_articles: []
title: Deep Review - Interoceptive Consciousness and the Interface
topics: []
---

**Date**: 2026-08-24
**Article**: [Interoceptive Consciousness and the Interface](/topics/interoceptive-consciousness-and-the-interface/)
**Previous review**: [2026-07-19](/reviews/deep-review-2026-07-19-interoceptive-consciousness-and-the-interface/)
**Word count**: 2796 → 2921 (+125), status `ok` against a 3000 soft threshold

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Empirical-claim misattribution to Garfinkel et al. 2015 — FIXED.** The article asserted "anxiety inflates reported sensation without improving it," carried under the Garfinkel citation. The claim is not a finding of that paper. Garfinkel et al. (2015) report a three-way dissociation in a normative sample of eighty healthy participants and make no anxiety finding; anxiety appears in the paper only as a keyword and as background citation to *other* work. Worse, the direction the article asserts runs against what the cited paper's own background actually summarises: "Enhanced interoceptive processing has been documented among individuals with anxiety (Dunn, Stefanovitch, et al., 2010; Pollatos, Traut-Mattausch, Schroeder, & Schandry, 2007; Terasawa et al., 2013)," and "anxiety patients can manifest a more accurate perception of their interoceptive performance than controls" — with the paper immediately flagging the literature as inconsistent ("yet this finding has not always been demonstrated"). Verified by extracting the publisher PDF and grepping the raw text for every occurrence of "anxiet" (11 hits, all background or reference-list).

Replaced with the paper's actual reported structure: the median-split result that mean confidence correlated with objective accuracy among high-accuracy heartbeat trackers (r = 0.43, p = 0.006) but not among low-accuracy trackers (r = −0.13, p = 0.42) — i.e. believing oneself attentive to the body does not predict being accurate about it, and confidence knows the difference only among those who are already accurate. The corrected version is stronger for the section's purpose than the sentence it replaces.

**2. Unlicensed inheritance claim about `capability-division-in-vision`, plus internal contradiction — FIXED.** The article asserted: "This maps directly onto the capability division's deepest structure: the difference between what a system has *access to* and what is *true*." No sibling licenses this. Checked all three upstream sources as they currently stand:

- [capability-division-in-vision](/concepts/capability-division-in-vision/) frames the deep distinction *within* the access side — "Conscious vision is not merely information availability — it is information available *to someone*." Veridicality plays no role in it.
- [cross-modal-capability-division](/apex/cross-modal-capability-division/) restates the same: "The vision article distinguishes information available *to the system* from information available *to someone*."
- [capability-division-problem](/voids/capability-division-problem/) frames it as brain-side extraction versus mind-side phenomenal contribution, ownership, and flexible reasoning.

Access-versus-truth is a *veridicality* axis, orthogonal to the division. The division is in fact agnostic about veridicality: blindsight delivers veridical content without consciousness, and dream rendering delivers non-veridical content with it. The article then contradicted itself twelve lines later, locating the Map's disagreement with the physicalist rival at the *ownership* term (matching the apex) rather than at access-versus-truth.

Re-derived from what the apex's current text does license: the finding that the mind-side term is a *family* of contributions rather than one thing, which the apex reaches by cross-modal comparison while noting that only a clinical case ([pain asymbolia](/concepts/pain-asymbolia/)) supplies within-modality isolation. Garfinkel supplies a second such isolation, psychophysical rather than clinical. Stated at the architecture tier per [P-F1](/positions/finding-level-calibration/) — a structural fact about what is measurable, carrying no significance-tier upgrade.

### Medium Issues Found

**3. Stranded sibling of the 2026-08-23 repair — FIXED.** Commit `edc51a5908` corrected L36 away from the clean (ungraded) capability division. The driver flagged L48 and L76 as string siblings. L48 carried a related residue in a different guise: it stated the partition as unfelt-equals-brain-side / felt-equals-mind-side, and in doing so conflated *content that reaches awareness* with *the mind side's contribution*. That conflicts with the article's own L36 ("conscious experience supplies phenomenal unity, ownership, and flexible deployment") and with its later section ("the mind side is the affective ground of subjecthood itself"). Rewritten so the felt band is the content the mind side receives and the contribution is what consciousness supplies to it. The windows-of-integration grading itself is carried once, at L36, and is not restated at L48 — restating it would be redundant, not stranded.

**4. Loescher et al. 2025 rendering understated the paper's headline — FIXED.** The article had the competition and self-relevance roles "running in parallel." The paper's actual reconciliation is stronger and more specific: "Competition and Facilitation effects were spatially and statistically independent from each other," resolving two frameworks that "developed largely in parallel" into two independent mechanisms. Also restored "integrative sensorimotor and default-mode network regions" (the article had dropped "sensorimotor") and changed "the same cardiac signal" to "the same heartbeat-evoked signal," since the paper's closing emphasis is on "the multidimensionality of HEPs."

### §2.4 Publisher-of-Record Citation Ledger

All seven external citations verified at Crossref (full tuple: authors, year, venue, volume, issue, pages/article number, title). Two additionally checked at PubMed for claim content.

- Craig 2002 (*How do you feel?*) — **real-correct**. NRN 3(8), 655–666, DOI 10.1038/nrn894.
- Critchley, Wiens, Rotshtein, Öhman & Dolan 2004 (*Neural systems supporting interoceptive awareness*) — **real-correct**. Nat Neurosci 7(2), 189–195, DOI 10.1038/nn1176. Five-author list matches exactly.
- Seth 2013 (*Interoceptive inference, emotion, and the embodied self*) — **real-correct**. TiCS 17(11), 565–573, DOI 10.1016/j.tics.2013.09.007.
- Barrett & Simmons 2015 (*Interoceptive predictions in the brain*) — **real-correct**. NRN 16(7), 419–429, DOI 10.1038/nrn3950.
- Park & Tallon-Baudry 2014 (*The neural subjective frame*) — **real-correct**. Phil Trans R Soc B 369(1641), 20130208, DOI 10.1098/rstb.2013.0208.
- Garfinkel, Seth, Barrett, Suzuki & Critchley 2015 (*Knowing your own heart*) — **metadata real-correct** (Biol Psychol 104, 65–74, DOI 10.1016/j.biopsycho.2014.11.004), but **claim-fidelity defect**: the anxiety claim the article drew from it is absent from the paper and contrary in direction to the background it summarises. Corrected in body (Critical Issue 1). This is the metadata-correct / content-wrong case that intra-corpus cross-checking cannot catch.
- Loescher, Haggard & Tallon-Baudry 2025 (*Interoception vs. Exteroception*) — **real-correct**. PNAS 122(49), e2516229122, published 2025-12-02, DOI 10.1073/pnas.2516229122. Rendering sharpened (Medium Issue 4).

Inline ↔ References cross-check: clean in both directions, no orphans. Superlative-currency sweep via `find_superlative_claims`: zero hits, no empirical-record currency risk. The two Map self-citations (entries 8–9) are framework-internal coherence, not external corroboration, per [P-M3](/positions/methodology-and-calibration/).

### Counterarguments Considered

- **Interoceptive inference (Seth; Barrett & Simmons) predicts everything the article observes.** Already handled honestly in "The Rival the Map Must Out-Accommodate" — the framework is cited as a rival to out-accommodate rather than as evidence, and the article states plainly that it does not discriminate. No change needed.
- **The constitutive reading (Damasio; Park & Tallon-Baudry) conflicts with the had-body commitment.** Handled at the framework boundary and correctly marked as bedrock. Not re-flagged.
- **A convergent insular hub is what a physicalist expects.** Stated by the article itself at two loci, and capped by the [common-cause null](/project/common-cause-null/). No change needed.

### Unsupported Claims

None remaining after the Garfinkel correction. The structural claims (insular convergence, affect-and-ownership mind side) are each carried by a verified citation and each accompanied by an explicit consonant-not-probative caveat.

## Register Alignment Check (Lens 2)

The article cites no `P-` entry and no positions file names it, so it has never been reachable by a register-driven audit from either direction. Checked by content against the register's calibration lines rather than by slug. The binding constraints are:

- **P-M1** (a tenet removes a defeater but never upgrades the evidence level) — **aligned**. The article never uses tenet-coherence to lift an empirical claim; the brain-side convergence is explicitly held "neutral between the readings."
- **P-M2** (convergence discounted to framework-internal coherence until a distinguishing test passes) — **aligned**. "Where the Inward Inversion Is Constrained" applies the common-cause null directly and notes the single insular hub is *maximally* a common cause.
- **P-F1** (architecture tier and significance tier cited at their own discounts) — **aligned**, and unusually well: "The convergence is a *structural disanalogy with exteroception*, genuinely sharpening the apex's claim; it is not, by itself, evidence for an interface." That is the two-tier split executed correctly. The Lens 2 rewrite was kept at the architecture tier to preserve this.

No calibration band is exceeded by the prose. Lens 2 returns clean — the article is register-invisible but not register-violating.

## Optimistic Analysis Summary

### Strengths Preserved

- The double-inversion thesis, stated in the first paragraph with both terms named. Truncation-resilient and genuinely the article's reason to exist.
- The self-limiting discipline: three separate loci volunteer that a physicalist expects the same convergence, and the article declines the upgrade each time. The Hardline Empiricist has nothing to object to here.
- "Where the Inward Inversion Is Constrained" — three calibrations that locate the finding rather than hedging it. Untouched.
- The rival-handling in "The Constitutive Reading the Map Does Not Share": Damasio engaged as a genuine rival with the disagreement marked at the framework boundary, explicitly refusing to enlist his evidence. Untouched.

### Enhancements Made

- The Garfinkel result now says what the study measured, with the N and the median-split structure — a weight-class signal the previous version lacked.
- The Garfinkel passage now connects to a real apex structure (the mind-side family claim) instead of an invented one, and adds the within-modality-isolation parallel the apex itself flags as scarce.
- The Loescher independence finding is now stated at the strength the paper reports.

### Cross-links Added

- [pain-asymbolia](/concepts/pain-asymbolia/) — the apex's other within-modality isolation case, previously unlinked from this article.

## Reasoning-Mode Classification (editor-internal)

- Engagement with Seth / Barrett & Simmons (interoceptive inference): **Mode Three, framework-boundary marking**. The article does not claim to refute active inference inside its own commitments; it states the framework does not discriminate and locates the Map's residual disagreement at ownership. Honest and correctly executed. No label leakage in prose.
- Engagement with Damasio / Park & Tallon-Baudry (constitutive reading): **Mode Three**. Explicitly marked at the framework boundary, with the refusal to enlist Damasio's evidence stated in the prose. No upgrade available — no internal-to-the-opponent argument is on the table.
- Label-leakage sweep: clean. No editor vocabulary appears in the article body.

## Remaining Items

None deferred. No follow-up task minted.

## Stability Notes

- **Bedrock, do not re-flag.** Interoceptive inference and the predictive-processing programme will always accommodate this article's data without a non-physical remainder. The article says so itself, twice. That is a framework-boundary standoff, not a correctable defect.
- **Bedrock, do not re-flag.** The constitutive reading (felt body as the substrate consciousness is made *from*) conflicts with the Map's had-body commitment and the evidence does not adjudicate. The article states this outcome explicitly. Future reviews should not treat the non-adjudication as a gap to close.
- **Do not re-introduce an access-versus-truth framing of the capability division.** It was live in this article until 2026-08-24 and is unlicensed by every upstream source. The division's deep distinction is availability-to-the-system versus availability-to-someone; veridicality is a separate axis the division is agnostic about.
- **The `capability-division-in-vision` inheritance loci are now three-for-three consistent.** L36 (graded, repaired 2026-08-23), L48 (content/contribution, repaired here), L76 (family claim, re-derived here). A future review finding a fourth locus should check it against the apex's *current* grading rather than against this article's other loci.
- **Citation set is stable and fully verified as of 2026-08-24.** All seven external cites checked at Crossref, two at PubMed full text. A future citation pass on this article can be skipped unless the References block changes.