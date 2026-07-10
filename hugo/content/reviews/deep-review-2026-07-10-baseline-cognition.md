---
ai_contribution: 100
ai_generated_date: 2026-07-10
ai_modified: 2026-07-10 14:24:13+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-10
date: &id001 2026-07-10
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Baseline Cognition
topics: []
---

**Date**: 2026-07-10
**Article**: [Baseline Cognition](/concepts/baseline-cognition/)
**Previous review**: [2026-06-03](/reviews/deep-review-2026-06-03-baseline-cognition/)
**Cumulative review count**: 11
**Pick justification**: OWED-WEB-VERIFY. Oldest citation cohort (article `ai_system` claude-opus-4-5); 16 references; converged 34 days (last_deep_review == ai_modified, no drift). The 2026-06-03 pass web-verified only the *recent/specialist* cluster (Bohn 2023, Gruber 2015, Streicher 2025) and explicitly trusted "prior reviews" for the pre-2020 canonical cites — meaning ~13 references had only ever had intra-corpus attribution checks, never a live publisher verify. That was the high-yield seam, and it yielded.

## Pessimistic Analysis Summary

### Critical Issues Found (citation web-verify — publisher of record)

**1. "Ratcheting up the ratchet" misattributed to Whiten et al. 2010 (CRITICAL — fixed).**
Reference read: "Whiten, A., et al. (2010). Ratcheting up the ratchet: On the evolution of cumulative culture. *Philosophical Transactions of the Royal Society B*, 365(1558), 2405-2415." Live verification (royalsocietypublishing.org DOI 10.1098/rstb.2009.0052; St Andrews research portal; Semantic Scholar) shows the paper is:
- Real: **Tennie, C., Call, J., & Tomasello, M. (2009). Ratcheting up the ratchet: on the evolution of cumulative culture. *Philosophical Transactions of the Royal Society B*, 364(1528), 2405-2415.**
- Famous-name substitution: "Whiten, A." is the canonical cumulative-culture name (the *same* failure mode as the Gruber/Whiten Jourdain conflation fixed here in June). Title and page range (2405-2415) match exactly; author, year (2009 not 2010), volume (364 not 365), and issue (1528 not 1558) were all wrong.
- **Resolution**: corrected author to Tennie, Call & Tomasello; year 2009; volume 364(1528). Page range preserved. The inline body reference is a bare conceptual "ratchet effect" mention (no author named), so no inline edit required.

**2. Tomasello, Kruger & Ratner 1993 wrong end-page (real-wrong-metadata — fixed).**
Reference read "16(3), 495-511". Live verification (Cambridge Core; PhilPapers TOMCL; core.ac.uk PDF; SciRP) confirms the correct range is **495-552**. End-page corrected 511 → 552.

**3. Tomasello 2010 missing co-author (real-wrong-metadata — fixed).**
"Ape and human cognition: What's the difference?" *Curr Dir Psychol Sci* 19(1) 3-8 is by **Tomasello, M., & Herrmann, E.** (SAGE 10.1177/0963721409359300; Duke Scholars). Reference listed only Tomasello. Added "& Herrmann, E." Inline "Tomasello (2010)" (first-author) left as-is.

### Per-citation ledger (all 16 references)

| # | Cite | State | Source checked |
|---|------|-------|----------------|
| 1 | Bohn et al. 2023, *Nat Ecol Evol* 7, 927-938 | real-correct | nature.com / PubMed 37106158 (verified June) |
| 2 | Cowan 2001, *BBS* 24(1), 87-114 | real-correct | Cambridge Core 44023F11 |
| 3 | De Neys 2012, *Perspect Psychol Sci* 7(1), 28-38 | real-correct | SAGE 10.1177/1745691611429354; PubMed 26168420 |
| 4 | Dehaene & Changeux 2011, *Neuron* 70(2), 200-227 | real-correct | ScienceDirect S0896-6273(11)00258-3 |
| 5 | DeWall, Baumeister & Masicampo 2008, *Conscious Cogn* 17(3), 628-645 | real-correct | PubMed 18226923; DOI 10.1016/j.concog.2007.12.004 |
| 6 | Gruber et al. 2015, *Front Psychol* 6, 91 | real-correct | Frontiers / PMC4319388 (verified + re-attributed June) |
| 7 | Mulcahy & Call 2006, *Science* 312(5776), 1038-1040 | real-correct | Science 10.1126/science.1125456; PubMed 16709782 |
| 8 | Povinelli 2000, *Folk Physics for Apes*, OUP | real-correct | global.oup.com 9780198572190 |
| 9 | Streicher et al. 2025, *Neurosci Conscious* 2025(1) niaf042 | real-correct | academic.oup/nc (verified June) |
| 10 | Read 2008, *Evolutionary Psychology* 6(4), 676-714 | real-correct | SAGE 10.1177/147470490800600413 |
| 11 | Suddendorf & Corballis 2007, *BBS* 30(3), 299-313 | real-correct | Cambridge Core; PubMed 17963565 |
| 12 | Tomasello 2010, *Curr Dir Psychol Sci* 19(1), 3-8 | **real-wrong-metadata (fixed)** | added co-author Herrmann, E. — SAGE 10.1177/0963721409359300 |
| 13 | Tomasello 2014, *A Natural History of Human Thinking*, Harvard UP | real-correct | canonical, correctly attributed |
| 14 | Tomasello, Kruger & Ratner 1993, *BBS* 16(3), 495-552 | **real-wrong-metadata (fixed)** | end-page 511→552 — Cambridge Core; PhilPapers TOMCL |
| 15 | Van Hoeck et al. 2015, *Front Hum Neurosci* 9, 420 | real-correct | Frontiers 10.3389/fnhum.2015.00420; PubMed 26257633 |
| 16 | ~~Whiten et al. 2010, PTRSB 365(1558)~~ → Tennie, Call & Tomasello 2009, PTRSB 364(1528), 2405-2415 | **real-wrong-metadata (fixed)** | royalsocietypublishing 10.1098/rstb.2009.0052 |

No fabricated/unfindable cites. All three defects are famous-name / metadata errors on real papers — content preserved, metadata corrected.

### Empirical-record currency sweep
No superlative/"first"/"only"/"record" empirical claims in the body that turn on a supersedable fact. The Streicher "~10% of unconscious-processing effects survived" (8/80 conditions) and the Cowan 4±1 / chimpanzee 2±1 working-memory figures are stable, correctly-scoped findings. No currency drift.

### Calibration Check (possibility/probability slippage)
Diagnostic test applied (would a tenet-accepting reviewer still flag any claim as overstated?): no. Map claims remain framework-relative ("The Unfinishable Map proposes", "the hypothesis proposes", "One explanation consistent with this evidence"). The quantum claim is hedged ("might bias... though classical attention-based selection could produce similar effects"). Great-ape phenomenality is calibrated ("likely have genuine phenomenal experience"). The five-prediction falsifiability section is intact. No slippage.

### Reasoning-Mode Classification (changelog-internal)
- Engagement with **epiphenomenalism**: Mode Two — uses the opponent's own commitment to causal explanation to argue the type-specific gap pattern would be coincidental under epiphenomenalism. Honest.
- Engagement with **illusionism**: Mode Mixed — empirical dissociation (Mode Two), regress problem (Mode One), training-effects question (Mode One). Honest.
No editor-vocabulary label leakage in article body. No boundary-substitution.

## Optimistic Analysis Summary

### Strengths Preserved
- Three-function GWT mapping (durable maintenance / novel combinations / spontaneous intentional action → ape limitations) — structural backbone; untouched.
- Five-prediction falsifiability section — exemplary evidential discipline; untouched.
- Type-specificity argument against epiphenomenalism — preserved.
- Quantum-interaction hedging — exemplary calibration; preserved unchanged.

### Enhancements Made
None beyond citation corrections. Citation-integrity-only pass.

### Cross-links checked
Spot-checked 13 key wikilink targets (consciousness-as-amplifier, metacognition, cumulative-culture, counterfactual-reasoning, delegatory-causation, delegatory-dualism, minds-without-words, anoetic-noetic-autonoetic-consciousness, ai-consciousness-typology, cetacean-and-corvid-consciousness, type-specificity, consciousness-and-cognitive-distinctiveness, jourdain-hypothesis) — all resolve to live files. No archival link-rot. No cross-links added; article is densely connected.

## Length Assessment
Net length-neutral. The three fixes altered author/year/page metadata only (+2 words from the Herrmann addition). Body prose unchanged. ~2620 words, ~105% of 2500 soft, well under 3500 hard. No condense queued; no human-length-decision flag.

## Remaining Items

**Minor note (not fixed — defensible as-is):** the inline attribution of the "zone of latent solutions" term to "Tomasello (2010)" is slightly loose — the ZLS coinage is the Tennie, Call & Tomasello 2009 paper (now correctly in the References as #16). Tomasello is a co-author of the concept and his 2010 review covers the same ground, so the first-author attribution is defensible and was left unchanged to avoid over-editing a converged article. Future refine passes may optionally point this inline mention at Tennie et al. 2009.

## Stability Notes
Eleventh review. Content has been converged for many reviews; the outstanding debt was pre-2020 citation metadata, which nine intra-corpus reviews *ratified* rather than caught, and which the June web-verify pass deliberately scoped out (recent-cluster-only). This pass closes that seam: three real-paper metadata defects (one famous-name author substitution + two page/co-author errors) surfaced only at the publisher of record — a fresh instance of ai_citation_metadata_unreliable.

**Do not re-flag in future reviews:**
- Bedrock disagreements with eliminative materialism, functionalism, MWI — engaged at framework boundary; not correctable.
- Three-function GWT mapping — structural backbone; do not restructure.
- Cumulative-culture-requires-metarepresentation — Tomasello/Tennie/Gruber framework choice, not slippage.
- Quantum-interaction hedging — exemplary; do not strengthen or weaken.
- All 16 References — now web-verified at publisher of record; do not re-question. The Tennie/Call/Tomasello 2009 ratchet cite, Tomasello-Kruger-Ratner 1993 (495-552), and Tomasello & Herrmann 2010 are the corrected canonical forms.