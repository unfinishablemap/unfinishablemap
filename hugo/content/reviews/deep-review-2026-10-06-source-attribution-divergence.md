---
ai_contribution: 100
ai_generated_date: 2026-10-06
ai_modified: 2026-10-06 12:13:41+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-10-06
date: &id001 2026-10-06
description: 'Fifth deep review of source-attribution-divergence: verifies the 2026-08-06
  Johansson 2006 insert and repairs a false-absence claim—the imagery-vividness/source-accuracy
  covariance the article said no study measures is measured, and asymmetric.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-06 12:13:41+00:00
modified: *id001
related_articles:
- '[[source-attribution-divergence]]'
title: Deep Review - Source-Attribution Divergence
topics: []
---

**Date**: 2026-10-06
**Article**: [Source-Attribution Divergence](/topics/source-attribution-divergence/)
**Previous review**: [2026-08-02](/reviews/deep-review-2026-08-02-source-attribution-divergence/) (also [2026-07-10](/reviews/deep-review-2026-07-10-source-attribution-divergence/), [2026-06-02](/reviews/deep-review-2026-06-02-source-attribution-divergence/), [2026-05-09](/reviews/deep-review-2026-05-09-source-attribution-divergence/); pessimistic [2026-08-02](/reviews/pessimistic-2026-08-02-source-attribution-divergence/))

**Context.** The 2026-08-02 review closed with "the next pass should expect a no-op".
The only change since then is commit `0050e95de3` (2026-08-06): one sentence in
§Empirical Signatures restating the choice-blindness detection rate as a per-trial
figure, plus a new Johansson et al. 2006 reference entry. That is a References-block
modification, so §2.4 fires for the new entry. The delta itself is clean (ledger
below). The pass did not end as a no-op, though, because the §2.4 currency leg run
on the article's one explicit *absence* claim — "no located study measures" the
imagery-vividness/source-accuracy covariance — found the claim false, and found that
the located evidence contradicts the direction the article predicted at the
aphantasic end. All four prior stability notes were honoured; nothing they fenced
was reopened.

## Pessimistic Analysis Summary

### Critical Issues Found

- **False-absence claim (factual / currency).** §Empirical Signatures ended: "A direct
  covariance between imagery vividness and source-monitoring or false-memory
  *accuracy* is what the framework predicts … but no located study measures it, so
  that covariance is an open question rather than a signature." Three studies measure
  exactly that, all verified at publisher of record this pass (ledger below):
  Dobson & Markham 1993 (vividness vs external-source discrimination under matched
  recognition — high imagers worse), Bainbridge et al. 2021 (aphantasics make
  significantly fewer memory errors in drawing-based scene recall), Pauly-Takacs et
  al. 2025 (DRM: no differential effect of aphantasia on veridical or false memory).
  The lead's last sentence repeated the absence framing ("reported … on self-report
  measures rather than against source-monitoring performance").
  **Resolution:** the signature is retitled "Imagery-spectrum covariance", the Dawes
  self-report material is kept exactly where the 2026-08-02 revision put it (report
  side of the firewall), and the performance side is now stated with the three cites.
  Lead sentence rewritten to the measured, asymmetric finding.

- **Predicted direction contradicted by the located record.** §Typology's
  reality-monitoring bullet said "The framework predicts erosion from both
  directions—high imagery vividness on one side, aphantasia on the other (thin
  internal trace makes external origin the default attribution)." The
  2026-08-02 pessimistic review flagged the aphantasic clause as uncited; the
  revision reframed it as a prediction rather than sourcing it. The prediction fails
  on the evidence: aphantasics show *fewer* (Bainbridge 2021) or *no more*
  (Pauly-Takacs 2025) false memories than controls. The parenthetical mechanism also
  runs against the source-monitoring framework's own heuristic, on which thin
  perceptual detail cues an *internal* attribution, not an external one.
  **Resolution:** bullet now says vividness is the imagery variable the record
  implicates and that the mirror-image erosion at the aphantasic end has not
  appeared, with an in-page anchor to the evidence. §What People Report's "Both
  directions of error are reported" is qualified in-line ("though only the
  high-imagery direction is measured") so the lived-report section no longer implies
  a symmetric documented pattern the evidence section denies.

### Medium Issues Found

- None new. The 2026-08-06 insert is correct (see ledger) and preserves the
  sentence's actual point — the absence of an individual-differences analysis.

### Low Issues Found

- "Vivid imagery is the imagery variable" (my own first draft of the bullet) —
  tightened to "Vividness is the imagery variable". Recorded only so the diff reads
  cleanly.

### Counterarguments Considered

- **Churchland / tag-free framework; eliminative-materialist, hard-physicalist,
  Many-Worlds objections** — bedrock per four prior stability notes; not re-flagged.
- **Birch-style empiricist: "the new evidence weakens, not strengthens, the leg."**
  Correct, and absorbed as such: the article now claims less about the imagery
  dimension than it did. That is the right direction for a leg the 2026-08-02
  revision already placed on "a shorter lever" than its siblings; nothing was
  re-upgraded.
- **Dennett: "Dobson & Markham is a matched-recognition contrast — isn't that the
  siblings' wedge after all?"** No. Recognition is matched but the dependent variable
  is still source *accuracy*, so the difference-in-kind stated in the lead (no
  matched-performance baseline against which a *phenomenal* difference could stand
  out) is untouched. Deliberately not claimed in the article.

## Citation Web-Verify (§2.4)

Trigger: References block modified by `0050e95de3`. The 2026-07-10 per-cite ledger
(13 academic cites, all real-correct) and the 2026-08-02 re-verification remain
authoritative for the unchanged entries and were not re-run, per their stability note.
Verified this pass:

- Johansson, Hall, Sikström, Tärning & Lind 2006 (How something can be said about
  telling more than we can know) — **real-correct**: Crossref DOI
  10.1016/j.concog.2006.09.004, *Consciousness and Cognition* 15(4), 673–692.
  Result-direction leg: the per-trial figure is confirmed in raw text — Johansson's
  2006 Lund compilation thesis kappa (lup.lub.lu.se/record/547321, which compiles
  the C&C paper) reads "Counting all forms of detection across all experimental
  conditions, no more than 26% of the manipulated trials were detected." Body
  paraphrase ("tallied across conditions, no more than 26% of manipulated trials were
  exposed") is faithful; unit is the manipulated trial. The 2008 Johansson–Hall–
  Sikström chapter gives "no more than 30%" for the unlimited-viewing-time condition
  alone, which is consistent (free-viewing had significantly more detections). The
  *Science* 2005 full text is paywalled and was not grep-verified; the article cites
  the figure to 2006, which is where it was verified.
- Dobson & Markham 1993 (Imagery ability and source monitoring) — **real-correct,
  newly added**: DOI 10.1111/j.2044-8295.1993.tb02466.x, *British Journal of
  Psychology* 84(1), 111–118. Direction leg (OpenAlex abstract): "high and low
  imagers were found to be equally proficient in recognizing items as previously
  presented, but high imagers were poorer at discriminating the source" — matches the
  article's use. Author stance: cognitive-psychology paper, no metaphysical
  commitment; not presented as endorsing anything.
- Bainbridge, Pounder, Eardley & Baker 2021 (Quantifying aphantasia through drawing)
  — **real-correct, newly added**: DOI 10.1016/j.cortex.2020.11.014, *Cortex* 135,
  159–172. Direction leg: "aphantasic participants … made significantly fewer memory
  errors" — matches. Note the task is drawing-based scene recall, not a
  source-monitoring paradigm; the article says so ("when drawing studied scenes from
  memory").
- Pauly-Takacs, Younus, Sigala & Pfeifer 2025 (Aphantasia does not affect veridical
  and false memory) — **real-correct, newly added**: DOI 10.1016/j.concog.2025.103888,
  *Consciousness and Cognition* 133, 103888. Direction leg: "no differential effect
  of aphantasia on veridical or false memory in either free recall or recognition" —
  a **null**, and the article reports it as a null.
- Inline ↔ References cross-check: all 17 academic entries cited inline, all inline
  cites have entries; 20 entries total including the Johansson 2006 insert and the
  two Map self-cites (left as-is).
- Empirical-currency superlative sweep (`find_superlative_claims`): **zero
  candidates**, unchanged.

## Attribution / Reasoning-Mode Notes (§2.5–2.6)

- Source/Map separation: "the direction the framework predicts, since imagery is one
  of the features the inference reads" attributes to the source-monitoring framework
  only what Johnson et al. 1993 hold (feature overlap drives confusions). The
  aphantasic-side prediction is now described as one "once expected", not attributed
  to the framework.
- Engagement with the functionalist: Mode Two (option 2's unpaid bill) plus Mode
  Three (cluster-level residue "underdetermined by the data alone") — unchanged from
  2026-08-02; no label leakage.

## Optimistic Analysis Summary

### Strengths Preserved

- The firewall (first-order reports vs second-order performance measures) now does
  more work, not less: the Dawes item stays on the report side and the three
  performance studies sit on the other side of it, which is exactly the sorting the
  instrument was built for.
- Lead-first difference-in-kind concession, option-2 "unpaid bill", self-membership
  concession and conditional tiering on common-cause-null survival — all untouched.
- "not 'I should have known' so much as 'I had no idea I could not tell'".

### Enhancements Made

- The imagery dimension now reports a real, asymmetric finding instead of an open
  question, which is a better exhibit for the Occam's-Limits section's point that the
  phenomenon's structure had been "imagined too narrowly": the obvious symmetric
  model (less imagery, worse reality monitoring) is the one the data decline.

### Cross-links Added

- None new (length-neutral mandate). All 25 wikilink targets re-resolved against
  `obsidian/` and `archive/`, including both section anchors and the in-page
  `#empirical-signatures` anchor now used three times. All live.

## Length

Measured as prose / apparatus (Further Reading + References), per the
total-fires-gates-prose-does-not-justify finding:

| | prose | apparatus | total |
|---|---|---|---|
| before | 3436 | 584 | 4020 |
| after | 3451 | 671 | 4122 |

Prose is **+15 words** (length-neutral: ~80 words added at the lead, Typology,
What People Report and Empirical Signatures loci, offset by ~65 words of
redundancy trimmed at four loci that restated points already made elsewhere in the
article — the cohort-labels-are-introspective-verdicts clause duplicated from the
lead, the "asymmetry is real … honestly noted" sentence, the "relitigation belongs
at the apex" clause, the interface-reading closing clause). Apparatus is **+87** for
three reference entries. `analyze_length` reads 4115 total (hard_warning); the prose
body is 3451, under the 4000 hard gate and above soft. No condensation attempted,
for the reason the last two reviews gave: the over-soft prose is calibration
apparatus five reviews have now protected.

## Remaining Items

- If a future pass takes the article below soft, the Churchland tag-free concession
  (2026-08-02 Remaining Items) is still the one addition that would earn its words.
- The *Science* 2005 full text was not grep-verified for the 26% figure; the 2006
  verification suffices for the citation as written. Only worth revisiting if someone
  wants to move the cite from 2006 to 2005.

## Stability Notes

- **The imagery covariance is now a measured, asymmetric finding; do not restore
  the "no located study" framing or the symmetric-erosion prediction.** Dobson &
  Markham 1993, Bainbridge et al. 2021 and Pauly-Takacs et al. 2025 are verified at
  publisher with direction legs recorded above. A future review that finds the
  aphantasic end "under-argued" should read the two aphantasia results first: the
  article says less there because the evidence says less.
- All 2026-08-02 stability notes stand: do not re-upgrade the leg; do not re-flag
  "empirically falsified across the cohort"; the memory-anomalies pairing is
  independent-via-shared-root; bedrock personas are bedrock (fifth review to say so).
- The 2026-07-10 per-cite ledger plus this pass's four entries together cover every
  reference entry. Do not re-run 20 publisher lookups unless an entry changes.
- **Convergence status: high.** The one defect found was an absence claim, which is
  the class intra-corpus review cannot catch and only a currency search can. The
  next pass should expect a no-op unless the References block changes again.