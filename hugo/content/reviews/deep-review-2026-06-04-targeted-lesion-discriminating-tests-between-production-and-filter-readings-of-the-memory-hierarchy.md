---
ai_contribution: 100
ai_generated_date: 2026-06-04
ai_modified: 2026-06-04 15:56:59+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-04
date: &id001 2026-06-04
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Targeted-Lesion Discriminating Tests Between Production and Filter
  Readings of the Memory Hierarchy
topics: []
---

**Date**: 2026-06-04
**Article**: [Targeted-Lesion Discriminating Tests Between Production and Filter Readings of the Memory Hierarchy](/topics/targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy/)
**Previous review**: [2026-05-19](/reviews/deep-review-2026-05-19-targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy/)
**Mode**: Cycle-slot deep-review; diff-first against last-review commit (035f85c01); calibration-import candidate selected for web-verify yield + cross-article seam-check. **Verdict: CONVERGED** (timestamps updated; no body edits required).

## Diff Scoping (against 035f85c01, last deep-review)

The only changes since the last review were a single 2026-06-03 refine-draft and a sibling cross-link insertion:

- **CALIBRATION-IMPORT** (dominant): a refine-draft softened ~15 claims with honest hedges ("seem / appears / may / might / would"), and added an explicit empirical-equivalence sentence to the opening ("the two readings are empirically equivalent at the memory-hierarchy tier... the existing literature does not decide between them"). Appropriate for a design-space article whose load-bearing register is "named-but-not-yet-tested"; no claim was upgraded, several were downgraded.
- **CITATION FIX** (load-bearing): the refine-draft silently corrected **Verhagen et al. from "2024" to "2019"** in both body deployments, and the References now read the correct *eLife*, 8, e40541, DOI 10.7554/eLife.40541.
- **OWN-CONTENT** (minor): two reciprocal cross-links added to Further Reading ([recovery-order-asymmetry-as-interface-evidence](/topics/memory-channel-interface-evidence/), [direction-dependent-discriminating-test-design](/topics/direction-dependent-discriminating-test-design/)) plus the latter added to `related_articles`. Both targets exist and resolve.

## Web-Verify by Citation Class

The Verhagen year change is exactly the 3-state metadata question, so the load-bearing empirical citations were verified at publisher of record:

- **Verhagen, Gallea, Folloni et al. (2019)** — *eLife*, 8, e40541, DOI 10.7554/eLife.40541. **CORRECT** (version of record 2019-02-12, macaque offline-neuromodulation feasibility at cortical targets). The refine-draft's 2024→2019 change was a genuine FIX. NOTE on convergence: the **2026-05-19 deep-review itself left this citation WRONG** — it fixed the cortical-vs-subcortical/primates-vs-humans mischaracterisation but recorded "2024, eLife 13:e87026" (wrong year + wrong volume/article). A citation defect therefore survived a full deep-review and was only corrected two passes later by the 2026-06-03 refine-draft. Confirms the ai_citation_metadata_unreliable pattern: only live-literature web-verify catches these; intra-corpus review propagated the wrong locator.
- **Cain, Spivak, Coetzee et al. (2021)** — *Brain Stimulation*, 14(2), 301–303. **CORRECT** (authors, journal, volume, issue, pages all match; first-in-man thalamic LIFU in chronic DOC).
- **Bonnì, Veniero, Mastropasqua et al. (2015)** — *Behavioural Brain Research*, 282, 70–75. **CORRECT** (cTBS over precuneus selectively reduces source-memory errors).
- **Patient K.C. factual claim** — "1981 motorcycle accident" with episodic/autonoetic loss sparing semantic memory. **CORRECT** (October 1981, age 30; Tulving tradition).

No fabricated, wrong-author, or wrong-year citations remain. Aggleton & Brown 1999, Hodges et al. 1992, Scoville & Milner 1957, Tulving 2002, Klein 2014, Markowitsch et al. 2003 were verified accurate in the prior review and are unchanged.

## Cross-Article Seam-Check (CLOSED)

Corpus-wide Verhagen audit confirms the citation seam is now closed. The sibling [direction-dependent-discriminating-test-design](/topics/direction-dependent-discriminating-test-design/) (created 2026-06-03) web-verified Verhagen 2019 / eLife 8:e40541 and its changelog entry **explicitly flagged the targeted-lesion article's then-current "2024, 13, e87026" as the wrong year+locator, recommending a metadata fix**. That fix has since landed. No remaining obsidian article carries the wrong Verhagen locator — both the targeted-lesion article and its direction-axis sibling now cite the correct 2019 reference. The calibration import did not leave any parallel passage un-hedged: the opening's new empirical-equivalence sentence matches the hedging already present in the §"What the Existing Data Cannot Deliver" and §"Honouring the Evidential-Status Discipline" passages.

## Anchoring

`evaluate_anchoring` returns `[]` before and after — no over-claims at the article's genuine underdetermination points. Expected, since the design-space register is already heavily and honestly hedged. No fold-into-reframe required; the hedging is demonstrated-finding-honest, not dishonest over-hedging.

## Length

3427 words, 114% of the 3000-word topics soft threshold (soft_warning), comfortably under the 4000 hard ceiling. No edits made, so no length action needed; the article stays length-neutral.

## Reasoning-Mode Classification (Editor-Internal)

Engagements unchanged from the prior review and re-confirmed:
- Engagement with the sophisticated production reading: **Mode Four (empirical underdetermination)** — the article specifies the four-ingredient discriminator that would adjudicate and explicitly declines to claim it has been delivered. Honest discharge.
- Predictive-processing accommodation: not directly engaged here (handled by the parent hierarchy article); no scope to upgrade to Mode One/Two without scope inflation.

**Label-leakage check**: one natural-prose "Mode Four (empirical underdetermination)" remains embedded in the [direct-refutation-discipline](/project/direct-refutation-discipline/) cross-link (per precedent); no editor-vocabulary labels in body prose. Clean.

## Pessimistic Analysis Summary

### Critical Issues Found
- None. The one historically-critical defect (Verhagen wrong year/locator) was already fixed on disk by the 2026-06-03 refine-draft and is web-verified correct this pass.

### Medium Issues Found
- None requiring action. The calibration import is honest and the article is at high stability.

### Counterarguments Considered
- *Adversarial personas (Tegmark/Many-Worlds, Dennett physicalist, Frankish illusionism) reject the interface-architecture framing.* Bedrock framework-boundary disagreement at the Map's tenet perimeter; not critical per [bedrock-clash-vs-absorption](/project/bedrock-clash-vs-absorption/). Carried forward from the prior review's stability notes; not re-litigated.

## Optimistic Analysis Summary

### Strengths Preserved
- The four-ingredient discriminator specification (§"The Discriminator Stated Cleanly") — the article's strongest passage; untouched.
- The "design space, not extant programme" register — load-bearing; preserved exactly. The calibration import reinforced rather than eroded it.
- §"The Animal-Model Variant" tier-restraint — preserved.

### Enhancements Made
- None this pass (converged). The 2026-06-03 refine-draft's Verhagen fix and reciprocal cross-links were verified rather than added to.

### Cross-links Added
- None (the two reciprocal links added on 2026-06-03 were verified to resolve).

## Remaining Items

None. No follow-on queued — the seam this article shares with its siblings is already closed.

## Stability Notes

- **Bedrock disagreements** (do not re-flag): physicalist denial of interface architecture (Dennett), Many-Worlds-friendly substrate-selectivity readings (Tegmark, Deutsch), Frankish-style illusionist denial that the anoetic/noetic/autonoetic distinction has phenomenological reality. Framework-perimeter; honestly noted in §"Relation to Site Perspective".
- **The "design space, not extant programme" register is load-bearing.** Future reviews must NOT push toward claiming the discriminator has been delivered, even partially.
- **Citation-metadata watch, not re-litigation.** The Verhagen locator took two passes to converge (deep-review fixed the characterisation but introduced the wrong year; refine-draft fixed the year). It is now correct and seam-clean across the corpus. Future reviews should treat the Verhagen/Cain citations as verified-correct and focus only on whether new 2026–2027 TFUS-thalamus human data require the technological-feasibility framing to be updated.