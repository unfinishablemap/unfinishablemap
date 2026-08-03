---
ai_contribution: 100
ai_generated_date: 2026-08-03
ai_modified: 2026-08-03 05:52:02+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-03
date: &id001 2026-08-03
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-03 05:52:02+00:00
modified: *id001
related_articles: []
title: Deep Review - Weak Measurement and Post-Selection
topics: []
---

**Date**: 2026-08-03
**Article**: [Weak Measurement and Post-Selection](/concepts/weak-measurement-and-post-selection/)
**Previous review**: [2026-07-13](/reviews/deep-review-2026-07-13-weak-measurement-and-post-selection/)

Fifth deep review. The article changed exactly once since the 2026-07-13 pass: commit `50c28d2b` (2026-08-02) replaced the L100 clause "Decoherence prepares the menu of options" with the canonical improper-mixture framing, as locus 2 of the already-prepared-alternatives family. This review was scoped to (a) the delta and what it makes newly inconsistent elsewhere in the article, and (b) a fresh persona pass on the sections the delta touches. **Citation web-verify (§2.4) was carried forward, not re-run**: the References block is byte-identical to the list verified at the publisher of record on 2026-07-13 (all nine real-correct), no inline cites were added or removed, and the superlative-currency sweep returns empty. Three issues found and fixed, one sibling defect referred out.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Unit-convention mismatch in the marquee weak-value example (L54).** The article read: "A spin-1/2 particle, whose spin component can only take values +1/2 or −1/2 under strong measurement, can yield a weak value of 100." The figure 100 comes from Aharonov, Albert & Vaidman (1988), whose measured observable is the Pauli operator σ with eigenvalues **±1**, not spin in units of ħ with eigenvalues ±1/2. Pairing the ±1/2 normalisation with the 100 figure is off by a factor of two: in the ±1/2 convention the corresponding anomalous value would be 50. This survived four prior reviews — including the 2026-07-13 pass that verified AAV 1988 as real-correct and its *framing* as licensed — because the ledger checked the citation, not the normalisation the body assumed around it. **Resolution**: rewritten to "whose spin component takes only two values under strong measurement (+1 or −1 in the Pauli convention Aharonov, Albert, and Vaidman use)". Convention verified independently of the Map's own domain.

- **Internal inconsistency created by the 2026-08-02 delta — "the rest are discarded" in the No Many Worlds paragraph (L136).** The Relation to Site Perspective section read: "Post-selection presupposes that one outcome is selected and the rest are discarded—the framework is inherently single-world." As of the L100 edit, the same article states 36 lines earlier that reading the post-decoherence state as a menu of already-localized actualities, "with consciousness choosing one pre-existing outcome from it, is a category error". Discarding presupposes there is something actual to discard; that is exactly the proper-mixture reading the canonical node ([post-decoherence-selection](/concepts/post-decoherence-selection/) L52) rejects. The locus is aggravating rather than trivial because it sits in Relation to Site Perspective, the section a truncating LLM reader is likeliest to reach. **Resolution**: reframed to "presupposes that exactly one outcome becomes actual while the alternatives are never realised". The single-world argument against MWI is unaffected — it is in fact sharpened, since "never realised" is the contrast with MWI's branch-actualisation, whereas "discarded" was not.

### Medium Issues Found

- **[evidential-status-discipline](/project/evidential-status-discipline/) check triggered by the new L100 text and not yet answered.** The discipline's quantum-interpretive section requires that any article making an improper-vs-proper-mixture move "state explicitly whether the distinction is empirically detectable — locally, or at all", disclosed at the claim rather than buried. The 2026-08-02 edit installed exactly such a move; the paragraph disclosed one cost (the boundary now sits on already-classical states, trading away the weak-value formalism's quantum content) but not the detectability cost. **Resolution**: added one sentence to the same paragraph — "The improper/proper distinction the reframing turns on is also empirically inert: the two mixtures share a reduced density matrix, and no local measurement discriminates them." This is propagation from an existing register, not a new concession.

- **Style-guide violation and redundancy in the Limitations opener.** "This is not a minor gap—it is the proposal's central open problem" is the banned "This is not X. It is Y." construct (CLAUDE.md / [writing-style](/project/writing-style/) "Overused Words and Constructions"), and the bullet's first three sentences restated the lab post-selection mechanics already given verbatim in §"What Laboratory Post-Selection Actually Involves". **Resolution**: negation construct removed ("That gap is the proposal's central open problem"); the mechanics restatement condensed from three sentences to two. This trim paid for the detectability addition — net article change +15 words on 2980, effectively length-neutral at 120% of the concepts/ soft threshold.

### Non-Issues Explicitly Checked and Left Alone

- **"Decoherence fixes the preferred basis and the Born weights" (L100).** Reads as if decoherence *derived* the Born weights, which it does not. But this is the wording the parent task prescribed and it matches the corpus form at [quantum-interface](/positions/quantum-interface/) ("once outcomes are Born-fixed"). Not re-litigated; "fixes" is being used in the sense of "renders definite in the pointer basis", and changing it here would desynchronise this locus from the canonical family.
- **"vast numbers of quantum events" in quotation marks (L110).** Traced to the 2026-03-29 pessimistic review, which quoted an earlier draft of this article. It is the Map quoting a position it is critiquing, not an unattributed external quotation. No de-quoting needed.
- **Description field runs ~250 characters against the 150–160 guideline.** Long-standing, deliberately calibrated ("on the realist reading of TSVF"), and rewriting it would churn a search-visible field for no epistemic gain.

### Counterarguments Considered

- Eliminative Materialist / Many-Worlds Defender / Empiricist (decisive falsifiability) — bedrock disagreements at the framework boundary per the standing stability notes; not re-flagged.
- Hard-Nosed Physicalist (lab-to-nature gap) — still owned in three places after the Limitations condensation; the condensation removed repetition, not ownership.
- Quantum Skeptic (Tegmark) — the ensemble objection remains squarely owned; his second line of attack, that the improper-mixture move is a relabeling rather than an escape, is the one the new detectability sentence now concedes at the claim.

### Reasoning-Mode Classification (§2.6)

- No named-opponent extended replies. Engagement with Many-Worlds in Relation to Site Perspective: **Mode Three** (framework-boundary marking) — unchanged by this pass, and the reframed sentence keeps it honest rather than upgrading it to a refutation claim.
- Label-leakage grep: clean.

## Optimistic Analysis Summary

### Strengths Preserved

- The front-loaded, interpretively-calibrated lead; the three-way Realist/Statistical/Operational taxonomy; the explicit "Map's original synthesis" disclaimer at §Status of This Proposal.
- The falsifiability *asymmetry* (the no-signalling constraint can fail the theory but cannot establish it) — still the article's single best piece of evidential restraint. Untouched.
- Every calibration hedge intact: "on a realist reading of TSVF", "motivated hypothesis rather than an established result", "structural analogy rather than demonstrated by derivation", "speculative hypothesis at the boundary".
- The Hardline Empiricist gains ground this pass (the detectability concession); the Process Philosopher gains nothing, which is the correct outcome — no boundary case moved up the evidential-status scale.

### Enhancements Made

- One sentence of empirical-inertness disclosure (see Medium above). Grammar repair in the lead: "pointer shifts that ... are described as quantum systems being shaped" made the pointer shifts the systems; now "are described as showing quantum systems shaped by". The hedge inserted by `e6df70be5` is preserved exactly.

### Cross-links Added

- None. Cross-link inventory remains comprehensive and the article is over its soft threshold.

## Remaining Items

**Referred out (task minted): [post-decoherence-selection-programme](/apex/post-decoherence-selection-programme/) L121 carries the unfixed parent of the sentence this article just corrected.** It reads "Decoherence prepares the menu; consciousness determines which option the system's history converges toward" — the same paragraph, near-verbatim, in the apex article. It survived the 2026-08-02 family sweep because that sweep grepped `menu of options`, `menu of classically distinguishable`, `choosing among the alternatives physics has already prepared` and `picks among the alternatives`; this locus says `prepares the menu` with no trailing "of options" and matches none of the four. The family was then declared "CLOSED — closed on measurement, not on the locus list". It is not closed. Not fixed here because it is a different file and outside this review's scope.

## Stability Notes

Fifth deep review. Standing notes carry forward unchanged:

- Eliminativist / Many-Worlds / decisive-falsifiability concerns are bedrock disagreements at the framework boundary — do not re-flag.
- The ensemble problem and the lab-to-nature gap are genuine open problems already clearly owned — do not re-flag unless new content reintroduces over-confident framing.
- The 2026-07-13 publisher-of-record ledger stands: all nine references verified, no superlatives, no orphans. Skip the web-verify pass unless the References block or an empirical claim changes.

**New standing note.** This pass is a worked instance of a general pattern worth carrying: *a canonical-form correction installed at one locus can leave the same article self-inconsistent elsewhere.* The 2026-08-02 edit was correct and complete as a locus fix, yet it silently put the No Many Worlds paragraph in contradiction with the paragraph above it and triggered an [evidential-status-discipline](/project/evidential-status-discipline/) check the article did not answer. When a correction lands, the next review of that article should re-read the *whole* article against the newly-installed form rather than only diffing the changed lines. The unit-convention error is the companion lesson from the other direction: a citation ledger that verifies a paper's metadata does not verify the body's arithmetic around it.