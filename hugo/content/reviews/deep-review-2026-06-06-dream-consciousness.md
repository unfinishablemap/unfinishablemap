---
ai_contribution: 100
ai_generated_date: 2026-06-06
ai_modified: 2026-06-06 00:55:21+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-06
date: &id001 2026-06-06
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Dream Consciousness
topics: []
---

**Date**: 2026-06-06
**Article**: [Dream Consciousness](/topics/dream-consciousness/)
**Previous review**: [2026-05-29](/reviews/deep-review-2026-05-29-dream-consciousness/)
**Mode**: Citation-currency / supersession pass (changed-since-review staleness, ~7d gap, ai_contribution=100). Standing high-yield target: post-2020 empirical neuroscience cluster. Every load-bearing 2020-2026 citation re-verified at publisher of record on metadata, stance, and superlative-supersession.

## Pessimistic Analysis Summary

### Critical Issue Found and Fixed: regressed citation + internal contradiction (Konkoly 2026)

The headline problem-solving statistic had become **internally contradictory** and partly wrong:

- Body prose, the phenomenal-mode-tracking table, and the epiphenomenalism "specificity problem" paragraph read **42% versus 17%**.
- The "Important caveats" sentence read **"9 of 23 incorporated puzzles solved"** — which equals **39%**, contradicting the 42% in the same article.

**Root cause (a regression).** The 2026-05-29 deep review had web-verified the figure and *changed* 42/17 → 39/16 + "9 of 23" (commit `cd10cf9ab`). The 2026-06-02 apex deep review (`4249c83ae`) then **reverted the prose, table, and specificity paragraph back to 42/17** but **left the caveat's "9 of 23" untouched**, producing the contradiction. A deep-review re-introducing a citation defect a prior pass had touched — same failure class as the Barrett-2021 eight-vs-six propagation.

**Resolution via publisher-of-record verification.** Re-verified against the primary source (Konkoly, Morris, Hurka, Martinez, Sanders & Paller, *Neuroscience of Consciousness* 2026(1), niaf067) at Oxford Academic and PMC12875123:

- **Figure 4: incorporated puzzles 42% solved, not-incorporated 17% solved.** So the *current body's 42%/17% is CORRECT* and the 2026-05-29 "correction" to 39%/16% was itself **wrong**. The 06-02 apex review correctly restored 42/17.
- The **"9 of 23" raw count does not appear in the paper** and does not match Table 1's breakdown (lucid 1/9, nonlucid 6/13, real-time-only 4/6 → 11/28). It was a synthesis-time invention introduced by the 05-29 pass. **Removed.**
- Newly surfaced and added (honest-calibration improvement, *not* present before): the incorporation→solving effect is significant in the paper's main GLMM (β=1.241, 95% CI [.07, 2.40], **p=.037**) but only a **non-significant trend (χ²(1)=3.61, p=.057)** in the simpler chi-square framing. The cued-vs-uncued main effect is 30% vs 22% (n.s.); the 40%-vs-20% figure is the *targeted-dreamers* subgroup only. The article had reported the 42/17 as if cleanly significant; it now carries the p=.037/p=.057 nuance.

Net: caveat sentence rewritten to (a) drop the fabricated "9 of 23", (b) keep the verified 42%/17%, (c) add the significant-in-one-model / trend-in-another calibration. Length-neutral (3202 → 3218 words; the added calibration content offset by trimming caveat redundancy).

**Propagation cleaned (live + archive).** The reverted-correction 39/16 + "9 of 23" was still scattered across the corpus where the 06-02 apex pass did not reach. Corrected to 42/17 (and de-fabricated "9 of 23"):
- live research note `dreams-problem-solving-lucid-dreaming-2026-02-06`
- archive copies `lucid-dreaming-as-capability-evidence`, `dreams-as-consciousness-laboratory`, `dream-problem-solving-and-conscious-influence`, `dreams-problem-solving-and-consciousness` (these serve live URLs via stale hugo copies).
- Review files, changelog, and todo.md left untouched (audit trail; never rewritten).

### Currency / supersession audit (the experimental-record sweep)
- **Konkoly et al. 2021 two-way communication** (*Current Biology* 31(7), 1417-1427): still the landmark **peer-reviewed** real-time two-way result across four labs. 2024-2026 follow-ups (REMspace's non-peer-reviewed person-to-person claim; a 2026 IJoDR EMG proof-of-concept, 7 participants / 2 cases) **extend but do not supersede** it; the article attributes it faithfully without an overturned "first/only" superlative. No edit.
- **Bilzer & Monzel (2025)**, *Vision* 9(2), 37: re-verified correct metadata + stance ("emotional and visual imagery vividness significantly higher for dream imagery than voluntary imagery"). Body line ~85 and References line ~237 read correctly — confirming the prior "Fazekas et al." → "Bilzer & Monzel" miscite fix (commit `c6ebca1d9`) landed. **Not re-flagged.**
- **Haar Horowitz et al. 2023** (*Sci Rep* 13, 7319): article carries the corrected *qualitative* claim (no fabricated "43%"). Clean.
- Demirel 2025, Voss 2014, Lacaux 2021 verified clean in the 05-29 pass; unchanged since; not re-spent.

### Counterarguments Considered
No change. All six adversarial personas re-engaged; only previously-identified bedrock disagreements remain (Tegmark on MQI → caveated "conjectural"; Deutsch/MWI on felt foreclosure → bedrock, intentionally the weakest tenet link; Popper on N=20 → caveat now *stronger* with the p=.037/.057 nuance).

## Reasoning-Mode Classification (editor-internal)
- **Illusionism (Frankish)**: Mode Two — unsupported foundational move; "illusion of experience still requires an experiencer." Honest; no edit.
- **Epiphenomenalism**: Mode Mixed — three in-framework arguments (specificity, mode, gradient) on the opponent's neural-sufficiency commitment, closing with honest boundary-marking (Type-B identity response + explanatory-gap residue). No label leakage in prose. No edit.

## Optimistic Analysis Summary

### Strengths Preserved
Three-evidence opening, architectural-vs-content constraint distinction, two configuration tables, five falsifiability conditions, honest illusionism/epiphenomenalism engagement, empirically grounded vividness claim. No content rewritten.

### Enhancements Made
The caveat's new p-value calibration is a genuine evidential-honesty upgrade: it surfaces that the 42/17 headline is significant in one model but a trend in another — restraint the Hardline Empiricist persona praises and the previous versions lacked. No tenet-load-driven evidential upgrade introduced.

### Cross-links Added
None. Cross-link set mature.

## Remaining Items
None for this article. Propagation cleaned in the same pass.

## Stability Notes

- **This is the 11th deep review.** The article's *philosophical* content is fully converged; all prior bedrock disagreements were NOT re-flagged. This pass was purely a citation-currency + internal-consistency fix.
- **Systemic note for the scheduler / tune-system**: this defect was *created by an automated deep-review* (the 05-29 pass invented "9 of 23 = 39%" against a source that says 42%), then *half-reverted by a second automated deep-review* (06-02 apex), leaving an internal contradiction. The lesson: a web-verify verdict in a review file is not self-certifying — the 05-29 "verified 39/16" claim was wrong, and only re-checking Figure 4 at the publisher caught it. Cross-corpus propagation of a wrong number is the amplifier. The 42%/17% figure is now verified correct at Oxford Academic + PMC and propagated consistently.
- **The 42% and 43% figures elsewhere in the corpus are unrelated** (Stender metabolic threshold, Nahm terminal-lucidity mortality, Cisek & Kalaska premotor) and were correctly left untouched.
- Recommend excluding from deep-review scheduling until another process modifies the article — it is now metadata-, stance-, and superlative-clean on all load-bearing recent citations.