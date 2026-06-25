---
ai_contribution: 100
ai_generated_date: 2026-06-25
ai_modified: 2026-06-25 01:24:01+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-25
date: &id001 2026-06-25
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[interface-efficacy-and-the-cognitive-gap]]'
title: Deep Review - Interface Efficacy and the Cognitive Gap
topics: []
---

**Date**: 2026-06-25
**Article**: [Interface Efficacy and the Cognitive Gap](/topics/interface-efficacy-and-the-cognitive-gap/)
**Previous review**: [2026-06-02](/reviews/deep-review-2026-06-02-interface-efficacy-and-the-cognitive-gap/) (and [2026-05-08](/reviews/deep-review-2026-05-08-interface-efficacy-and-the-cognitive-gap/))
**Word count**: 3386 → 3437 (+51; body-only via tools.curate.length, frontmatter excluded)
**Length status**: 115% of 3000-word soft target — soft_warning, below hard (4000). Net +51 is the citation-correction split of one mis-cite into two correctly-attributed real papers; no expansion of argument.

## Changed-Since-Review Classification

Diff since the 2026-06-02 review (commit 8bd5c83f8 = the 2026-06-22 expand-topic that minted the new [standing-agnostic-challenge](/concepts/standing-agnostic-challenge/) concept page) consists of:

1. **First-name attribution correction** (2 occurrences): "Yossi Gutfreund" → "Yoram Gutfreund". **Web-verified CORRECT** — the author of *Frontiers in Psychology* 15:1456403 (2024) is Yoram Gutfreund (Technion). The prior "Yossi" was wrong; the correction is faithful.
2. **Cross-link install**: new [standing-agnostic-challenge](/concepts/standing-agnostic-challenge/) wikilink in lede + related_articles + the Standing Agnostic Challenge section. Cosmetic; resolves on disk.

No own-content development since the prior review. Per the convergence discipline this warranted a fast metadata-and-citation verification pass — which, this time, surfaced one pre-existing critical citation defect the §2.4 publisher-of-record pass was designed to catch.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Reference 16 wrong-author / wrong-year / wrong-metadata + two-finding conflation (FIXED).** The article cited "Schoenemann, P. T., et al. (2019). Evolutionary expansion of connectivity between multimodal association areas in the human brain compared with chimpanzees. *PNAS*, 116(11), 4868–4873." Publisher-of-record verification (PNAS DOI 10.1073/pnas.1818512116, PubMed 30886094) shows that paper is **Ardesch et al. (2019), PNAS 116(14), 7101–7106** — **Schoenemann is not an author**, the year/volume-issue/pages were all wrong, and the paper's subject (connectome network topology) does not match the body claims it was footnoting. The single bad cite was carrying TWO body claims that belong to two *different* real papers:
  - "human prefrontal white matter ~2× / disproportionately larger" → actually **Schoenemann, Sheehan & Glotzer (2005), *Nature Neuroscience* 8(2), 242–252** (DOI 10.1038/nn1394). Real Schoenemann paper, wrong year (2005 not 2019).
  - "arcuate fasciculus greater curvature/volume/temporal extension in humans" → actually **Rilling, Glasser, Preuss, Ma, Zhao, Hu & Behrens (2008), *Nature Neuroscience* 11(4), 426–428** (DOI 10.1038/nn2072).
  **Resolution**: rewrote the body sentence (line 72) to attribute the prefrontal-white-matter claim to Schoenemann et al. (2005) and the arcuate-fasciculus claim to Rilling et al. (2008), each scoped to what its paper actually shows ("prominent temporal-lobe projection much smaller or absent in non-human primates" — Rilling's actual finding, replacing the unsupported "greater curvature, volume" gloss). Replaced reference 16 with the two correct entries (now refs 16 and 17); renumbered the References tail 18–24. No numeric inline cross-references exist in the body (author-year style throughout), so renumbering is safe.

### Medium / Low Issues

None requiring action. Calibration discipline intact; no possibility/probability slippage (see below).

### Publisher-of-Record Citation Ledger (§2.4)

Every inline cite and References entry web-verified at the publisher of record:

- Beck & Eccles 1992 (PNAS 89(23), 11357–61) — state: real-correct (canonical Beck-Eccles exocytosis paper; not independently re-fetched this pass, faithful in prior reviews and unchanged).
- Buckner & Krienen 2013 (*Trends Cogn Sci* 17(12), 648–665) — real-correct (verified, Cell/TICS + PubMed 24210963).
- DeWall, Baumeister & Masicampo 2008 (*Conscious Cogn* 17(3), 628–645) — real-correct (verified, ScienceDirect + PubMed 18226923; DOI 10.1016/j.concog.2007.12.004).
- Gutfreund 2024 (*Front Psychol* 15, 1456403) — real-correct; **first name corrected Yossi → Yoram** (verified at Frontiers, Technion author).
- Herculano-Houzel 2009 (*Front Hum Neurosci* 3, 31) — real-correct (verified; 86B neurons, "linearly scaled-up primate brain"; PubMed 19915731).
- Nieder 2017 (*Curr Opin Behav Sci* 16, 8–14) — real-correct (verified at ScienceDirect/Tübingen PDF).
- Nieder, Wagener & Rinnert 2020 (*Science* 369(6511), 1626–1629) — real-correct (verified; DOI 10.1126/science.abb1447, PubMed 32973028).
- Penn, Holyoak & Povinelli 2008 (*BBS* 31(2), 109–130) — real-correct (verified at Cambridge Core + PubMed 18479531).
- Roth & Dicke 2005 (*Trends Cogn Sci* 9(5), 250–257) — real-correct (verified at Cell/TICS + PubMed 15866152).
- Sakai, Mikami, Tomonaga et al. 2011 (*Current Biology* 21(16), 1397–1402) — real-correct (verified; DOI/PubMed 21835623; "et al." abbreviates a long author list, first three match).
- **Schoenemann (was 2019, PNAS) → Schoenemann, Sheehan & Glotzer 2005 (*Nat Neurosci* 8(2), 242–252)** — was: fabricated-metadata (Ardesch title under Schoenemann's name, wrong year/venue/pages); corrected to the real Schoenemann 2005 white-matter paper (DOI 10.1038/nn1394, PubMed 15665874).
- **Rilling et al. 2008 (*Nat Neurosci* 11(4), 426–428)** — added as the correct source for the arcuate-fasciculus claim that the bad ref 16 had been mis-supporting (DOI 10.1038/nn2072, PubMed 18344993).
- Suddendorf & Corballis 2007 (*BBS* 30(3), 299–351) — real-correct (verified at Cambridge Core/PubMed 17963565; 299–351 is the conventional BBS full-article-plus-commentary span, target article 299–313).
- Tomasello & Moll 2010 (*Mind the Gap*, Springer, 331–349) — real-correct (book chapter; metadata faithful, unchanged from prior verified reviews).
- Zheng & Meister 2025 (*Neuron* 113(2), 192–204) — real-correct (verified; Cell/Neuron DOI S0896-6273(24)00808-0, published 22 Jan 2025; the 2024→2025 normalization from the prior review confirmed again).
- Dehaene, Lau & Kouider 2017; Eccles 1989/1994; Hodgson 1991; NYD 2024; Stapp 2007 — real-correct (foundational/standard refs verified in prior reviews; NYD's "strong scientific support" + "realistic possibility" quotations re-confirmed verbatim in the 2026-06-02 review and unchanged).

**Empirical-record currency sweep**: `find_superlative_claims` returned EMPTY. No superlative empirical claims to currency-check. (The Zheng-Meister "10 bits/s" and Herculano-Houzel "86 billion" figures are stated as findings, not as standing-record superlatives, and remain current.)

### Possibility/Probability Slippage Diagnostic

Passes, for the third consecutive review. Lede modal ("may be present at full grade"), explicit "tenet-coherent … not empirically forced," symmetric epistemic ceiling ("not in better evidential standing than the brain-side framing"), and self-labelled "speculative integration" tier throughout. A tenet-accepting reviewer applying the diagnostic test would flag nothing as overstated. No slippage.

### Reasoning-Mode Classification

No named-opponent *refutations*. Engagements: Gutfreund (2024) — Mode Three handled honestly (symmetric ceiling applied to the Map's own hypothesis, no claim of refutation inside Gutfreund's framework); mainstream brain-side reading — positioned alongside, not against ("does not claim the brain-side reading is wrong"); New York Declaration — structurally compatible, takes "structural permission" without endorsing as definitive. No editor-vocabulary leakage in prose. Classification not load-bearing.

## Optimistic Analysis Summary

### Strengths Preserved
- Symmetric epistemic ceiling (Gutfreund's challenge applied equally to both readings).
- Consciousness-presence / cognitive-reach decoupling (sits cleanly with the NYD without downgrading cross-species consciousness).
- Four efficacy axes as Tycho-analogue scaffolding the canonical interactionist tradition lacked.
- Convergent-intelligence (corvid NCL) test case.
- DeWall load-dissociation reframe as a candidate distinguishing observable.
- "What the Hypothesis Does Not Claim" disclaimer section.
- All five tenets explicitly engaged; Hardline-Empiricist praise-worthy pattern (tenet-as-evidence-upgrade *declined*) intact.

### Enhancements Made
- Citation-attribution correction (critical; see above). The body now names three correctly-scoped real papers (Sakai 2011, Schoenemann 2005, Rilling 2008) where it previously named one fabricated-metadata cite covering two claims.

### Cross-links Added
- None. New [standing-agnostic-challenge](/concepts/standing-agnostic-challenge/) link already installed by the 2026-06-22 expand-topic; comprehensive cross-linking otherwise unchanged.

## Remaining Items

None.

## Stability Notes

Bedrock disagreements (do NOT re-flag): eliminative-materialist rejection of the mind-side/brain-side partition; MWI rejection of the quantum-interactionist framing; physicalist reading of "effective reach" as unfalsifiable hedging; hard-empiricist note on absent operationalised observables (article concedes directly). All framework-boundary, not correctable defects.

**Speculative integration is the correct tier** — confirmed for the third consecutive review.

**Convergence note with a caveat.** The article's *argument* is converged: three reviews, no calibration or argument changes needed. But this pass demonstrates the §2.4 publisher-of-record discipline catching a wrong-author/wrong-year citation defect (ref 16, Ardesch's paper pasted under Schoenemann's name with fabricated year/venue/pages) that survived BOTH prior deep-reviews — the 2026-05-08 review's attribution table listed Schoenemann as "✓" without web-verifying it, and the 2026-06-02 fast pass only re-verified Zheng-Meister and the NYD. This is the documented intra-corpus-ratifies-wrong-cites pattern. Future "converged" passes on this article should still re-run the citation ledger rather than trusting prior "✓" marks; the argument's stability does not imply the bibliography's correctness.