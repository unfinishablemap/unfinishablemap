---
title: "Deep Review - Memory Anomalies: Déjà Vu, Jamais Vu, Cryptomnesia"
created: 2026-07-13
modified: 2026-07-13
human_modified: null
ai_modified: 2026-07-13T01:11:12+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[memory-anomalies]]"
  - "[[deep-review-2026-06-20-memory-anomalies]]"
  - "[[deep-review-2026-06-02-memory-anomalies]]"
  - "[[deep-review-2026-05-09c-memory-anomalies]]"
  - "[[deep-review-2026-05-09b-memory-anomalies]]"
  - "[[deep-review-2026-05-09-memory-anomalies]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-7
ai_generated_date: 2026-07-13
last_curated:
---

**Date**: 2026-07-13 01:11 UTC
**Article**: [[memory-anomalies|Memory Anomalies: Déjà Vu, Jamais Vu, Cryptomnesia]]
**Previous reviews**: [[deep-review-2026-06-20-memory-anomalies|2026-06-20 (convergence stamp)]], [[deep-review-2026-06-02-memory-anomalies|2026-06-02 (full + publisher-of-record metadata verify)]], [[deep-review-2026-05-09c-memory-anomalies|2026-05-09c]], [[deep-review-2026-05-09b-memory-anomalies|2026-05-09b]], [[deep-review-2026-05-09-memory-anomalies|2026-05-09]]
**Pass type**: Attribution-framing + quote-fidelity pass on an orthogonal axis (the 06-02 web-verify covered *metadata* only — author/year/venue/pages; the *who-coined-vs-developed* framing axis and the one attributed direct quote had never been publisher-verified)
**Word count**: 3308 → 3309 body words (net-neutral; two attribution fixes, no expansion). 110% of 3000 soft; well under 4000 hard.

## Scope clarification

The 2026-07-07 `ai_modified` bump was a mechanical `auto(embed-videos)` YouTube-embed commit, not content drift — confirmed via git log (most recent touch = `3ca027c73 auto(embed-videos): trigger`). This pass targeted the never-verified **citation-framing / attribution-accuracy** axis and the article's one attributed direct quote. The 06-02 pass did verify the full ~20-reference *metadata* cluster at the publisher of record (three corrections, all still present and accurate in the live file); those were not re-litigated. Framing accuracy (who coined vs. developed a term) and quote fidelity are orthogonal to metadata and had never been checked.

## Pessimistic Analysis Summary

### Critical Issues Found (attribution / quote — both fixed)

1. **Quote-fidelity + wrong-attribution (line ~74).** The article presented `"a failure to simultaneously engage in creative thinking and monitor where incoming ideas are coming from"` as a verbatim quote from **Brown and Murphy**. Publisher-of-record verification (APA *Monitor on Psychology*, Feb 2002, "Plagiarism or memory glitch?", journalist Siri Carpenter) shows this phrasing is the **journalist's paraphrase of Richard L. Marsh's cognitive-load research** — not a verbatim quote, and not Brown & Murphy's words. Double defect: false-quote + misattribution ([[verbatim-quote-cited-to-wrong-work]] / [[quote-fidelity-defects-survive-metadata-reviews]] pattern). **Fixed** by de-quoting to paraphrase and dropping the false author attribution: "On this source-monitoring account, cryptomnesia is a failure to simultaneously engage in creative thinking and monitor where incoming ideas are coming from." The underlying mechanism (source-monitoring fails under creative load) is exactly the Marsh & Bower finding the surrounding paragraph already develops, so no content or citation was invented or deleted.

2. **Attribution-framing over-ascription (line ~102).** "Flournoy and Jung, who **coined and developed** the term *cryptomnesia*" attributed *coinage* to both. Verification: Théodore Flournoy **coined** the term in *Des Indes à la planète Mars* (1900), studying the medium Hélène Smith; C. G. Jung **developed** it in his 1905 essay "Cryptomnesia," explicitly building on Flournoy. Jung did not coin it. **Fixed** to "Flournoy, who coined the term *cryptomnesia*, and Jung, who developed it, used it precisely to deflate such claims." (citation-framing-accuracy lens.)

### Attribution loci verified accurate (no change)

- **Bergson's "memory of the present" (line ~46, ~84–90; Ref line 138).** "Le souvenir du présent et la fausse reconnaissance," *Revue Philosophique* vol. 66, December 1908 — confirmed at publisher of record (later revised into *L'énergie spirituelle*, 1919). Year, venue, and the English-gloss phrase are faithful. The phrase is a translation gloss, not a verbatim French quotation, so no quote-fidelity concern.
- **Familiarity/recollection "developed by Mandler and refined by Yonelinas, Tulving, and others" (line ~68).** Confirmed: George Mandler's 1980 *Psychological Review* dual-process model ("butcher on the bus") is the canonical development; Yonelinas' 1994 dual-process signal-detection (DPSD) model is the standard quantitative refinement; Tulving's remember/know (1985) is adjacent. Attribution accurate.

### Citation metadata (carried forward from 06-02, not re-litigated)

The ~20-reference recognition-memory cluster was web-verified at the publisher of record on 2026-06-02 (three metadata defects fixed: Cohen et al. 2008 *Psychon Bull Rev* 15(5):906–926; Wixted & Squire 2010 *Behavioural Brain Research* 215(2):197–208; Perrin, Moulin & Sant'Anna 2024 *Philosophical Psychology* 37(8):2466–2496). All three corrections remain present and accurate in the live file. The References block is unchanged since; per §2.4's "References not modified since last deep-review" condition, metadata was not re-verified. This pass independently re-confirmed Flournoy 1900, Bergson 1908, Mandler 1980, and Yonelinas 1994 as part of the framing check — all consistent.

### Self-contamination guard

No verification relied on unfinishablemap.org or a mirror; unfinishablemap.org was blocked from all searches. The Marsh-paraphrase finding rests on the APA primary source directly.

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)

- The architecture-independence move in the CSDT paragraph (the load-bearing claim survives the dual-process-vs-continuous question).
- The déjà vu / déjà vécu distinction (Perrin, Moulin & Sant'Anna).
- The cumulative-convergence self-reference honesty block, conditioning the strongly-supported tier on the common-cause null surviving apex discrimination tests.
- All calibration hedges: Bergson as "one candidate, not commitment"; "does not extend to paranormal claims"; "take the phenomenology seriously without endorsing unbounded paranormal channels." None regressed.

### Enhancements Made

None beyond the two attribution/quote corrections. Article is converged and at length ceiling; no expansion warranted.

## Calibration Check

Intact. No possibility/probability slippage; no epistemic→metaphysical slide. The de-quote fix, if anything, tightens honesty (removes a false verbatim attribution). A tenet-accepting reviewer would not flag any claim as overstated. The article does not drift toward endorsing paranormal memory claims.

## Reasoning-Mode Classification (editor-internal)

Carried forward unchanged (no opponent-engagement prose modified):
- Cognitive-science reductionism / hard-problem residue: Mode Three (framework-boundary marking).
- Paranormal / spiritualist readings of déjà vu: Mode One (defective on its own terms via the Cleary gestalt-match account).

No label leakage.

## Remaining Items

None.

## Stability Notes

- The **metadata** axis (06-02) and now the **framing/quote** axis (this pass) have both been publisher-verified. Future passes should not re-verify either absent a References-block or prose change.
- Do not re-quote the Marsh paraphrase to Brown & Murphy; it is a journalist's paraphrase of Marsh's research, correctly de-quoted.
- Do not re-merge Flournoy/Jung into "coined and developed"; Flournoy coined (1900), Jung developed (1905).
- Do not re-alter the three 06-02-corrected cites; do not "correct" the deliberately-repeated "The the the the" Moulin et al. 2021 title (real published title).
- Carry-forward bedrock disagreements (do not re-flag): physicalist/heterophenomenological dissolution; eliminativist denial that felt certainty picks out a real explanandum; empiricist objection that the hard-problem residue is unfalsifiable.
