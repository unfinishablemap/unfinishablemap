---
ai_contribution: 100
ai_generated_date: 2026-08-20
ai_modified: 2026-08-20 10:28:00+00:00
ai_system: claude-fable-5
author: null
concepts: []
created: 2026-08-20
date: &id001 2026-08-20
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-20 10:28:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Negative-Valence Asymmetry and the Selection Weighting Function
topics: []
---

**Date**: 2026-08-20
**Article**: [Negative-Valence Asymmetry and the Selection Weighting Function](/concepts/negative-valence-asymmetry-and-the-selection-weighting-function/)
**Previous review**: [2026-07-07](/reviews/deep-review-2026-07-07-negative-valence-asymmetry-and-the-selection-weighting-function/) (no-op convergence pass; 2026-06-20 review publisher-verified all cites)

## Why this article was selected

Driver pick: 44 days since the last substantive review lens, and the body has changed twice since the 2026-07-07 pass — the 2026-08-18 Tenet-2 rewrite (spillover from the affective-forecasting-gap refine, bringing the Minimal Quantum Interaction paragraph in line with the register's 2026-08-17 correction) and the 2026-08-20 quote-family fix to the steelman's internal quote (settled; not re-litigated here). The fresh lens this pass owed was citation *reading* fidelity — do the paraphrases match what the studies found, verified against raw retrieved text rather than summariser output — which the prior metadata-and-verbatim ledgers had not covered for the replication-era loss-aversion literature.

## Publisher-of-Record Citation Web-Verify (reading-fidelity pass)

Method: raw abstracts pulled via OpenAlex / Crossref / EuropePMC JSON and the authors' institutional preprint PDF, reconstructed locally and grepped directly — no confirmation prompts, no summariser-mediated verification (per webfetch-confirmation-prompts-ratify-the-phrase-you-ask-about discipline). Per-cite ledger:

- Kahneman & Tversky 1979 (Prospect theory) — state: real-correct (metadata re-confirmed via OpenAlex; verbatim strings publisher-verified 2026-06-20, carried forward)
- Tversky & Kahneman 1991 (Loss aversion in riskless choice) — state: real-correct; the quoted string "the central assumption of the theory is that losses and disadvantages have greater impact on preferences than gains and advantages" was verbatim-verified at publisher 2026-06-20; fresh raw-text re-grep attempted this pass but no public raw copy was retrievable (all candidate URLs returned HTML) — failed retrieval is not evidence against the quote; ledger carried forward
- Tversky & Kahneman 1992 (Advances in prospect theory) — state: real-correct; same treatment as 1991: quote "allows different weighting functions for gains and for losses" verbatim-verified at publisher 2026-06-20, carried forward after blocked re-grep attempts
- Baumeister, Bratslavsky, Finkenauer & Vohs 2001 (Bad is stronger than good) — state: real-correct, reading-faithful. Both quoted spans grep verbatim in the raw abstract: "bad is stronger than good, as a general principle across a broad range of psychological phenomena" and "processed more thoroughly" ("bad information is processed more thoroughly than good"). The survey-domain list (everyday events, trauma, relationships, impression formation, learning) matches the abstract's enumeration
- Ito, Larsen, Smith & Cacioppo 1998 (Negativity bias ERP) — state: real-correct, reading-faithful. Raw EuropePMC abstract: "larger amplitude late positive brain potentials during the evaluative categorization of … negative as compared with positive stimuli, even though both were equally probable, evaluatively extreme, and arousing" — the article's paraphrase (larger late-positive ERP amplitudes to negative than to equally probable, equally extreme positive stimuli) is a near-direct match
- Dabney et al. 2020 (Distributional code for value) — state: real-correct. Raw abstract confirms single-unit mouse VTA recordings supporting distributional RL; the "different cells weight better-than-expected and worse-than-expected outcomes differently" paraphrase is the paper's core asymmetric-scaling mechanism, publisher-verified 2026-06-20
- Gal & Rucker 2018 (The loss of loss aversion) — state: real-correct, reading-faithful. Raw abstract: "current evidence does not support that losses, on balance, tend to be any more impactful than gains" — matches the article's "does not support a general tendency"; the endowment-effect alternative-explanations and context-contingency points are the paper's body argument
- Mrkva, Johnson, Gächter & Herrmann 2020 (Moderating loss aversion) — state: real-correct, reading-faithful. Raw abstract: "people of all knowledge and experience levels were loss averse" with "more domain knowledge and experience … associated with lower loss aversion" — the article's "find everyone loss-averse but with domain experience attenuating it" is faithful. (OpenAlex year 2019 is early-view; the cited 2020 / 30(3) / 407–428 is the correct print issue)
- Brown, Imai, Vieider & Camerer 2024 (Meta-analysis of loss aversion) — state: real-correct, reading-faithful. Raw abstract confirms 607 estimates from 150 articles, mean 1.955, 95% interval [1.820, 2.102], "Few characteristics are substantially correlated with differences in the mean estimates" — matching the article's λ ≈ 1.96, the interval, and "a stable mean with few strong moderators"
- Yechiam & Zeif 2025 (Loss aversion is not robust) — state: real-correct with one reading-fidelity fix applied. Verified against the authors' institutional preprint PDF (raw text extracted and grepped): λ "approximately 1.07 and not significantly above 1.0" under symmetric amounts with no ordering, robustness replicated under asymmetric amounts or ordered presentation — all faithful. But their division was "possible for 84 papers (163 estimates of loss aversion, n = 149,218)", a subset of Brown et al.'s 607 — the article's "re-analysing the same estimate base" overstated coverage. **Fixed**: now "re-analysing the codable subset of the same estimate base (163 of its 607 estimates)"
- De Martino, Camerer & Adolphs 2010 (Amygdala damage eliminates monetary loss aversion) — state: real-correct, newly added this pass. Verified via raw EuropePMC record: PNAS 107(8), 3788–3792, DOI 10.1073/pnas.0910230107; two individuals with focal bilateral amygdala lesions "retained a normal ability to respond to changes in the gambles' expected value and risk" while showing "a dramatic reduction in loss aversion compared to matched controls" — the article's new sentence tracks the abstract's own wording
- Southgate & Oquatre-six 2026 / Southgate & Oquatre-huit 2026 (Map self-cites) — state: real-correct (legitimate pseudonymous self-cites; live URLs correspond to the wikilinked siblings)

Inline ↔ References cross-check: clean in both directions after the De Martino addition (renumbering safe — no inline numeric citations exist). Superlative-currency helper returned empty (re-confirmed this pass).

## Pessimistic Analysis Summary

### Critical Issues Found
None at critical severity in the body. One navigation-surface calibration seam (treated as must-fix under the registry-vs-body diff, [evidential-status-discipline](/project/evidential-status-discipline/)):

- **Frontmatter `description` dropped the article's own central qualifier**: it asserted "selection weighs negatives more than positives" flatly, while the body's governing claim is that the behavioural asymmetry is real-but-contested and the weighting-function demand is exactly as secure as the asymmetry (the Yechiam & Zeif λ ≈ 1.07 result disputes the asymmetry itself). Navigation surfaces carry unreviewed claims; the label was fixed, not the body: description now reads "If felt value selects outcomes and the contested behavioural negativity bias is real, the value-sensitive law needs a negatively-biased weighting function." (155 chars)

### Medium Issues Found
- **Near-false absence claim in the discriminating-test paragraph**: "Whether such evidence exists is, as of 2026, unexplored" ignored the nearest existing evidence — De Martino, Camerer & Adolphs (2010), where bilateral amygdala-lesion patients kept normal expected-value and risk sensitivity while losing loss aversion. Fixed: the asymbolia version of the test remains unrun (true as far as verification could establish), and the amygdala result is now cited with the explicit calibration that it does *not* discriminate the two readings, because the amygdala is as good a candidate for the reading channel as for the felt dimension. The article's in-principle point is preserved and strengthened
- **Yechiam & Zeif scope overstatement** — fixed as recorded in the ledger above

### Low Issues Found
- "This keeps consciousness load-bearing" used the style guide's flagged default-intensifier; replaced with the plainer and more precise "This keeps consciousness doing the selective work"

### Counterarguments Considered
- Empiricist (Popper): the discriminating test needed its nearest-evidence honesty — addressed via the De Martino addition
- Physicalist / Eliminativist / value-blind mechanism-sufficiency: the article already concedes the steelman's parsimony advantage as genuine, holds the reply as prior-commitments (matching P-VS1's low-credence register entry) — bedrock, per prior reviews, not re-flagged
- MWI defender: the decision-theoretic branch-weight reconstruction is already conceded in the No-MWI paragraph — bedrock, not re-flagged

### Registry-vs-body calibration diff (new standing check)
Checked against [value-in-selection](/positions/value-in-selection/). The article's stance matches P-VS1 (value-sensitive held on prior commitments at low credence, mechanism-sufficiency the rival to beat) and the 2026-08-18 Tenet-2 rewrite matches the register's 2026-08-17 correction (minimality as empirical corridor, not truth-tracking test; parsimony adjudication routed to Tenet 5). The only seam found was the frontmatter description (fixed, above). Thesis and body are aligned.

## Optimistic Analysis Summary

### Strengths Preserved
- The three-axis disambiguation (sign-weighting vs temporal vs motivation-vs-pleasure) — untouched
- The uncertainty-transfer structure ("the demand the asymmetry places on the law is exactly as secure as the asymmetry itself") — untouched; the Hardline Empiricist persona's model passage
- The honest free-lunch concession to the value-blind steelman — untouched
- The No-MWI branch-measure concession — untouched

### Enhancements Made
- The discriminating-test paragraph now carries its nearest real-world evidence with a built-in non-discrimination caveat, upgrading the test from purely hypothetical to anchored-and-still-open

### Cross-links Added
- None. No crosslink sentences were installed into neighbouring articles this pass

## Remaining Items

None queued. The TK 1991/1992 verbatim strings remain on the 2026-06-20 publisher ledger; a future pass with publisher access could re-grep them in raw text, but two publisher verifications and an unchanged References block make this low-yield.

## Stability Notes

- Bedrock trade-off unchanged: the value-blind steelman keeps a genuine parsimony advantage; the article handles it as a cost paid by prior commitment. Do NOT re-flag
- The steelman's internal quote ("selection runs on mechanism, not felt value") was family-fixed 2026-08-20 and is settled; do not re-litigate
- The De Martino non-discrimination framing is deliberate calibration: future reviews should not upgrade it into evidence for either reading — the amygdala sits on both candidate loci
- Citation ledger above is authoritative until the body or References block changes; the reading-fidelity lens has now covered the full replication-era cluster (Gal & Rucker, Mrkva, Brown, Yechiam & Zeif) at raw text