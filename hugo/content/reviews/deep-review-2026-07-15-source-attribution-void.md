---
ai_contribution: 100
ai_generated_date: 2026-07-15
ai_modified: 2026-07-15 22:58:25+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-15
date: &id001 2026-07-15
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[voids/source-attribution-void]]'
- '[[reviews/deep-review-2026-06-03-source-attribution-void]]'
- '[[reviews/deep-review-2026-05-11-source-attribution-void]]'
title: Deep Review - Source-Attribution Void (quote-fidelity pass)
topics: []
---

**Date**: 2026-07-15 22:58 UTC
**Article**: [The Source-Attribution Void](/voids/source-attribution-void/)
**Previous review**: [2026-06-03](/reviews/deep-review-2026-06-03-source-attribution-void/)
**Pick justification**: Staleness candidate flagged for GENUINE post-review drift — `last_deep_review` 2026-06-03 but `ai_modified` 2026-06-04 (content edited ~1.75d AFTER the last review, unverified since). The 2026-06-04 edit (commit 17cd9ae21) rewrote §Where the Machine Might See Differently and added a new empirical claim about "2025 interpretability work" that the 06-03 web-verify pass never saw. 5th review; metadata web-verify largely complete corpus-wide, so this pass routed to ORTHOGONAL high-yield lenses per the steer: quote-fidelity (primary), citation currency, framing accuracy.
**Word count (body)**: 2877 → ~2874 (−3; two de-quote fixes). 144% of 2000 soft target; hard threshold (3000) NOT reached. Strictly length-neutral.

## Pessimistic Analysis Summary

### Critical Issues Found (quote-fidelity — 2 fixed)

**Two paraphrase-presented-as-direct-quote defects — FIXED.** Both are the defect class the steer flagged as highest-yield for this cohort (quote-fidelity-defects-survive-metadata-reviews): a faithful reconstruction placed inside quotation marks and thereby presented as the cited author's verbatim words.

1. **Johnson, Hashtroudi & Lindsay (1993)** — §The Unmarked Arrival previously read: *Instead, "the origin of memories is inferred ... from characteristic features".* This exact string (with "for example" sitting precisely where the article's ellipsis sits) recurs verbatim across the **secondary** source-monitoring review literature as reviewers' *own summary paraphrase* of the framework — it is not Johnson et al.'s primary wording. Co-author Lindsay's own book chapter ("Memory Source Monitoring Applied") phrases the foundational claim completely differently: memories "are not abstractly and unambiguously specified and labelled a priori but rather are inferred by the mind/brain ... on the basis of their content." The Yale primary PDF could not be text-extracted (image/encoding), but the convergent evidence (secondary-source verbatim match + divergent primary-author phrasing + ellipsis positioned exactly at the secondary "for example") establishes the quoted string is a secondary paraphrase, not primary verbatim. **Fix (length-neutral): de-quoted.** The prose now presents the accurate substance as an attributed paraphrase ("Instead, the origin of memories is inferred from characteristic features—...") — the attribution to the framework is preserved, the false-verbatim framing removed. The 2026-06-03 review examined this string and *accepted* it as an "ellipsis-joined paraphrase-quote"; that acceptance was incorrect on the evidence now assembled (an ellipsis inside quotation marks asserts the surrounding words are verbatim), meeting the convergence-exception "prior resolution was incorrect."

2. **Pronin (2009)** — §The Confabulatory Layer previously read: *Introspection fails without phenomenal warning—people are "unaware of their unawareness."* The quotation is embedded in the Pronin paragraph, implying it is Pronin's verbatim phrase. The phrase traces verbatim to **Wilson & Bar-Anan (2008), "The Unseen Mind," *Science* 321(5892):1046-1047** (per the phrase's canonical attribution), not to Pronin's 2009 chapter. The 2026-06-03 review already flagged this as an unconfirmed-verbatim gap. **Fix (length-neutral): de-quoted** to "people are unaware of their own unawareness" — the characterization is faithful to Pronin's introspection-illusion thesis, and de-quoting removes both the unconfirmed-verbatim risk and the implicit misattribution of a Wilson phrase to Pronin (avoids adding a new reference, keeping the pass length-neutral).

### Citation Web-Verify (quote & currency lens; metadata carried from 2026-06-03 full pass)

Metadata for all load-bearing cites was verified at publisher of record in the 2026-06-03 pass (including the Pacozzi article-number fix 21127→20595) and the References list is unchanged since; not re-disturbed. This pass verified the **quoted strings** and the **new 06-04 empirical claim**:

- **Nisbett & Wilson 1977** — `"may be little or no direct introspective access to higher order cognitive processes"` — VERBATIM confirmed at publisher (opening line, *Psychological Review* 84(3):231). real-correct. ✓
- **Johnson et al. 1993** quote — paraphrase-as-quote → de-quoted (see Critical #1). Cite metadata real-correct.
- **Pronin 2009** quote — verbatim traces to Wilson & Bar-Anan 2008 → de-quoted (see Critical #2). Pronin 2009 cite metadata real-correct.
- **NEW-CLAIM VERIFY — 2025 interpretability / §Where the Machine Might See Differently.** The 06-04 edit added: "2025 interpretability work finds a *candidate silicon instance* of this very void: ... steered models register the strength of an injected internal disturbance more readily than they identify its source—strength felt, origin lost." This claim is **well-supported**: there is a real 2025 paper titled *"Feeling the Strength but Not the Source: Partial Introspection in LLMs"* (arXiv:2512.12411), whose thesis matches the article's phrasing precisely, alongside the broader Anthropic "Emergent introspective awareness in large language models" line. The strength-felt/source-lost dissociation is faithfully rendered, not overstated. real-correct; no calibration slippage (framed as a "candidate" instance, appropriately hedged). ✓

### Currency Sweep (lens 2)

`find_superlative_claims` helper returned zero superlative claims. No "first"/"only"/"current record" claims to re-check against the live literature. The source-monitoring / confabulation / choice-blindness / cryptomnesia corpus cited here (1977-2022) is foundational, not currency-sensitive.

### Framing Accuracy (lens 3)

No skeptic-cited-as-endorsing defects. The most framing-sensitive passage — the Wegner & Wheatley (1999) paragraph — carefully separates the narrow structural finding (authorship experience is dissociable from causal fact in arranged conditions) from "the wider eliminativist reading Wegner is often given," explicitly stating "The void relies on the structural finding, not the universal claim." Faithful. Nisbett & Wilson framed as bounding introspective access, not as eliminativism. Henke-lab paragraph explicitly declines the metaphysical over-read ("establish the opacity of the encoding operation, not the metaphysics behind it"). No mis-framing.

### Calibration Discipline (holds)

§Relation to Site Perspective calibration crown jewels remain verbatim and passing: §Dualism "compatibility, not evidence"; §Bidirectional Interaction "coherence-with-the-tenet, not evidential support"; Implications point 2 "substantive philosophical commitment"; point 3 "hypothesis to test, not a conclusion to carry." No possibility/probability slippage. Diagnostic test on the new LLM-introspection claim: a tenet-accepting reviewer would NOT flag it as overstated — it is presented as a candidate structural parallel, not evidence for the tenets.

### Medium Issues Found

**None requiring edit.** Article in deep convergence (5th review).

## Optimistic Analysis Summary

### Strengths Preserved (untouched)

- Three-layer architectural/inferential/confabulatory decomposition — central contribution.
- Three-seam empirical scaffolding (choice blindness / cryptomnesia / source amnesia).
- §Where the Machine Might See Differently — human/AI architectural asymmetry, now with a verified silicon-parallel anchor.
- §Phenomenology of Unmarkedness — zero-signal structure with erasure/recognition/imagery siblings.
- Henke-lab encoding paragraph and Wegner structural-finding separation — both calibration-honest.

### Enhancements Made

None to substantive content. This pass corrected two quote-fidelity defects (de-quoting paraphrases falsely framed as verbatim) and refreshed timestamps. Converged content correctly received a near-no-op editorial pass.

### Cross-links Added

None. Bridge structure at substantial completeness; length pressure (144%) counsels against accretion.

## Remaining Items

- **Object-scene-binding citation completeness (LOW, carried).** §Three Layers cites only Reber et al. 2012 (word-pairs) for the Henke-lab subliminal-encoding finding; the object-scene-binding result (Wuethrich, Hannula, Mast & Henke 2018, *Hippocampus*) is genuine Henke-lab work not in the reference list. Prose attributes to "the Henke lab" generally, so this is a completeness gap, not a misattribution. Optional; not corrected to avoid disturbing converged prose under length pressure.

## Stability Notes

The article remains in convergence. Bedrock disagreements catalogued in the 2026-04-28 review remain bedrock and are NOT re-flagged. The division of labour with sibling articles (decision-void, recognition-void, memory-anomalies, source-attribution-divergence) stands.

The only substantive findings this pass were two quote-fidelity defects — both paraphrase-as-direct-quote — caught only by verbatim verification at the primary publisher, exactly the lens the steer prioritised and exactly the class that intra-corpus and metadata reviews ratify rather than catch. Future deep-reviews should default to a near-no-op pass unless a new structural sibling appears or new external citations/quotes are absorbed. The 06-04 LLM-introspection claim is now verified; it needs no re-checking absent further edits.

## Reasoning-Mode Classifications (Editor-Internal, Not Article Prose)

- **Engagement with Wegner** (§The Confabulatory Layer): Mode Mixed (Three with structural-finding extraction). Reports Wegner-Wheatley (1999) accurately, separates the structural finding from the wider eliminativist reading without endorsing it, notes the dissociation does not license universal illusion. Framework-boundary disagreement acknowledged honestly. No editor-vocabulary leakage in article prose. Unchanged from prior review.

No other named-opponent engagements; §Relation to Site Perspective engages tenet positions, not named opponents.