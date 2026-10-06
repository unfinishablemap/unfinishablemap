---
title: "Deep Review - Aphantasia"
created: 2026-10-06
modified: 2026-10-06
human_modified:
ai_modified: 2026-10-06T06:27:32+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[aphantasia]]"
  - "[[imagery-void]]"
ai_contribution: 100
author:
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-06
last_curated:
---

**Date**: 2026-10-06
**Article**: [[aphantasia|Aphantasia]]
**Previous review**: [[deep-review-2026-08-01-aphantasia|2026-08-01]] (fifth pass; prior passes 2026-05-08, 06-02, 07-06, 08-01)
**Word count (body)**: 2699 → 2759 (+60; 92% of the 3000 topics soft threshold)

## Scope

The only content delta since 2026-08-01 was one Further Reading cross-link (`[[inner-speech-and-anendophasia]]`, commit `6fa7d5727e`) — the classic cosmetic re-qualification. The References block was unchanged, so the 2026-07-06 full-tail publisher-of-record metadata ledger was carried forward rather than re-run. **This pass was nonetheless not a no-op.** Three prior ledgers certified the article's quoted strings as "drawn from primary sources" without ever grepping the raw sources; the 2026-07-06 "In-Quote String Re-Grep" only checked that the quotes were not inherited from sibling Map articles. Grepping the raw sources this pass surfaced four quote-fidelity / factual defects that survived four reviews, one of which had propagated to a sibling.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Factual error on Galton's sample (FIXED).** § A Brief History said Galton "polled one hundred Royal Society fellows and a wider non-scientific sample." The 1880 *Mind* text (psychclassics.yorku.ca, grepped) says the returns came from "100 adult men, of whom 19 are Fellows of the Royal Society" and "at least half of whom are distinguished in science or in other fields of intellectual work," plus 172 Charterhouse schoolboys. Corrected to the actual composition, quoting Galton's own characterisation.
- **Spliced quotation — Galton (FIXED).** The quoted phrase "I have no power of visualising" is not in the text. Respondent 95's return reads "No power of visualising." — the subject "I have" was spliced inside the quotation marks. Moved the splice outside the quotes and attributed the line to respondent 95. The companion quote "perfectly distinct" is verbatim (three hits). Galton's abstract-thought conjecture is also confirmed verbatim ("an over-readiness to perceive clear mental pictures is antagonistic to the acquirement of habits of highly generalised and abstract thought"), so the article's "likely overdrawn conjecture" framing stands.
- **Non-verbatim quotation — Kay, Keogh & Pearson 2024 (FIXED).** The inline quote "slower but more accurately" matches neither the title ("Slower but more accurate…") nor the abstract ("slower, but more accurate responses than controls" — OpenAlex inverted-index grep, exact match). Replaced with the abstract's verbatim phrase. The block quote ("visual imagery is not crucial for successful performance…") re-confirmed verbatim against the abstract.
- **Dropped qualifier — Kay et al. strategies (FIXED).** "aphantasics use analytic… while imagers use object-based mental rotation" hardened the abstract's "favoured" / "generally favoured". Restored the qualifier in § Empirical Signatures. In § Cognitive Equivalence, "matching the standard angular-disparity signature *of object-based rotation*" misdescribed the finding — both groups show the linear angular-disparity signature while aphantasics favour analytic strategies, which is the point of the paper. Rewritten as "while reproducing the standard angular-disparity signature, despite favouring analytic rather than object-based strategies."
- **Wrong date and missing attribution — *Brains Blog* "we still don't know" (FIXED, propagated).** The article dated the post to 2026 and gave no author or reference entry. The post is Andrea Blomkvist's commentary of **1 April 2025** in the *Brains Blog* symposium on Nanay's *Mental Imagery*, titled "Unconscious imagery in aphantasia? Spoiler: we still don't know" (URL and page date line verified). The sentence now names the author and date and quotes the full title; added as reference #14 (refs #14–#17 renumbered to #15–#18; body uses author-year so numbering is inert). **Family resolution:** the source research note `research/voids-imagery-void-2026-04-28.md` L226 mis-dated the entry "2026-04-01" against a `/2025/04/01/` URL, and `voids/imagery-void.md` L80 inherited "A 2026 *Brains Blog* post". Corrected the sibling in place (author + April 2025; +3 words, within its 63-word hard-threshold headroom), bumped its `ai_modified` only. The research note was left as-is (research notes are source records, not published claims).

### Medium Issues Found

- None new. No label leakage (grep of the forbidden editor-vocabulary list returned nothing), no "This is not X. It is Y." construct, no "load-bearing".

### Counterarguments Considered

- All six adversarial personas re-engaged. Nothing new beyond the standing bedrock items (see Stability Notes). The Empiricist persona is the one that paid off this pass — not with a new counterargument, but by insisting the quoted strings be grepped rather than certified by resemblance.

### Citation Verification Ledger (this pass)

Metadata for every References entry carried forward as real-correct from the 2026-07-06 exhaustive publisher-of-record ledger (References block unchanged since). Quote-fidelity and result-direction legs run this pass:

- Galton 1880 (*Mind* 5(19)) — metadata real-correct (carried); **quote "I have no power of visualising" → spliced, corrected to "No power of visualising"**; "perfectly distinct" verbatim; **sample description factually wrong, corrected (100 men / 19 FRS / 172 Charterhouse boys)**; direction (men of science skew to weak imagery; general sample and boys to vivid) confirmed verbatim ("To my astonishment, I found that the great majority of the men of science… protested that mental imagery was unknown to them").
- Kay, Keogh & Pearson 2024 (*Consciousness and Cognition* 121, 103694) — metadata real-correct (carried); **inline quote non-verbatim, corrected**; block quote verbatim; direction (slower, more accurate; both groups linear in angular disparity; strategy difference) confirmed; **"use" → "favour" qualifier restored**.
- Blomkvist 2025 (*Brains Blog*, 1 April 2025) — **was undated-wrong (2026) and unattributed; now real-correct, added as #14**. Title quote verbatim.
- Zeman 2020/2024 gloss "as vivid as real seeing" — Zeman's own standard description of hyperphantasic report ("imagery so vivid that it rivals 'real seeing'", Zeman et al. 2020 *Cortex*); attribution to hyperphantasic self-report is faithful. No change.
- Schwitzgebel 2008 — the unquoted paraphrase "highly inaccurate, untrustworthy, and faulty" tracks the paper's "faulty, untrustworthy, and misleading"; not presented as verbatim. No change.
- Wundt "sham experiments" (*Scheinexperimente*, 1907) — standard, well-attested translation. No change.
- Wicken 2021, Dawes 2020/2022, Dance 2022, Larner 2024, Zeman 2010/2015/2024, Lennon 2023, Nanay 2025, Scholz 2025, SEP — real-correct, carried; result-direction legs for Wicken (attenuated SCR), Dawes 2022 (fewer episodic details, past and future), Dance (3.9%/0.8% extremes) confirmed in prior ledgers and not contradicted by any change this pass.
- Cited-author-stance leg: no cited author is presented as endorsing the Map's conclusion. Lennon is explicitly "diagnostic rather than probative"; Nanay's predictive-processing reading is reported as his, with Scholz's opposition alongside.
- Inline↔References mechanical set-comparison: balanced in both directions after the Blomkvist addition (Wicken/Pearson 2021 is one cite; Lennon 2023 cited inline by title; Map self-cites cited as wikilinks; SEP cited inline without author by design).

### Currency Sweep

Helper output unchanged from 2026-08-01: one hit, "state of the art" — now removed by the Blomkvist rewrite ("state of play"). Population figures (~1%/~3%) remain the live consensus (Zeman 2024; Dance 2022). No currency defect.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-option trichotomy and the honest option-3 self-undermining conditional in § Cognitive Equivalence — untouched.
- The Würzburg-recurrence observation — untouched.
- Tenet-1 calibration in § Relation to Site Perspective ("not a knockdown argument"; interface speculation demoted to "explicit speculation, not tenet-level commitment") — untouched.

### Enhancements Made

- Galton paragraph now carries the real sample composition, which makes the "scientific cohort skewed toward weak imagery" observation more legible (the reader can see it was a mixed 100 compared against schoolboys, not FRS-only).
- The Kay et al. rewrite in § Cognitive Equivalence states the paper's actual philosophical point (same behavioural signature, different strategy) rather than a garbled version of it.

### Cross-links Added

- None (the article's link apparatus was completed on 2026-08-01; no new link warranted).

## Calibration (evidential-status discipline)

No possibility/probability slippage. The five-tier scale is not invoked and no tenet upgrades an empirical claim. The diagnostic test (would a tenet-accepting reviewer still flag anything as overstated?) returns no. Reasoning-mode classification: the only named-opponent engagement is generic functionalism (option 2) — Mode Three, boundary honestly marked ("the Map flags the standard functionalist rejoinder"); the cumulative within-species wedge is offered as pressure, not refutation. No label leakage.

## Remaining Items

None.

## Stability Notes

Bedrock disagreements from the prior four reviews still hold and must NOT be re-flagged as critical: eliminative-materialist rejection of phenomenology talk; functionalist absorption via fine-grained individuation (named as option 2, not claimed refuted); no quantum/MWI machinery is relevant here.

Transferable lesson (this pass): a "quoted strings are drawn from primary sources" line in a ledger certifies *provenance*, not *fidelity*. Four reviews carried a spliced Galton quote, a paraphrased Kay quote presented as verbatim, a wrong Galton sample, and a mis-dated blog post because each ledger verified metadata and then certified the quotes by resemblance. The check that catches these is a literal grep of each quoted string against the raw source text (psychclassics HTML for Galton; OpenAlex inverted-index abstract for Kay; the blog page itself for Blomkvist). With that done, every quoted string in this article is now grep-verified and the article should return to converged status.
