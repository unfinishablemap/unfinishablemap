---
title: "Deep Review - Authorship-of-Action Divergence"
created: 2026-07-16
modified: 2026-07-16
human_modified:
ai_modified: 2026-07-16T19:05:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[authorship-of-action-divergence]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-16
last_curated:
---

**Date**: 2026-07-16
**Article**: [[authorship-of-action-divergence|Authorship-of-Action Divergence]]
**Previous reviews**: [[deep-review-2026-06-16-authorship-of-action-divergence|2026-06-16]], [[deep-review-2026-06-05-authorship-of-action-divergence|2026-06-05]], [[deep-review-2026-05-22-authorship-of-action-divergence|2026-05-22]]
**Mode**: Staleness pass on the corpus's most citation-dense staleness candidate (older-cohort `claude-opus-4-7`). Prior three passes verified citation *metadata* (author/venue/year) but never claim-match. This pass ran check (i) — does each cite's claim match the paper's *actual finding* — and caught a claim/paper mismatch the metadata-only passes ratified.

## Why This Candidate

Converged article (last_deep_review == ai_modified == 2026-06-16), 30d stale, `ai_contribution: 100`, `ai_system: claude-opus-4-7`. Documented citation-propagation defect history (Coutinho→Rebouillat misattribution; fabricated "Sauerland 2020" — both resolved in the June passes). Re-scrutinized citations hard rather than presuming no-op. "Converged ≠ verified."

## Pessimistic Analysis Summary

### Critical Issues Found

- **Citation claim/paper mismatch — Pärnamets et al. 2015 (FIXED).** The "Pupillometric corroboration" paragraph attributed "pupil-dilation signatures distinguishing undetected swap trials from baseline at the autonomic level" to Pärnamets et al. 2015. **Pärnamets et al. 2015 PNAS ("Biasing moral decisions by exploiting the dynamics of eye gaze," 112(13), 4170–4175) is a gaze-*timing* manipulation study of moral decisions — not a pupillometry study, and not a choice-blindness swap-detection study.** It uses gaze-contingent prompting to bias moral choices; it records no pupil-dilation swap-detection signal. Verified at the publisher of record (PMC4386374). This is the Inoue–Matsuzawa pattern: correctly-formatted metadata (title/venue/year all right, which is why three prior metadata-only web-verify passes ratified it) paired with a claim the paper does not make.
  - **Root cause**: the demonstrated pupillometric-covert-detection-of-swaps finding belongs to Grassi, P. R., Hoeppe, L., Baytimur, E., & Bartels, A. (2025), "Restoring sight in choice blindness: pupillometry and behavioral evidence of covert detection," *Frontiers in Psychology*, 16, 1598254 (DOI 10.3389/fpsyg.2025.1598254; PMC12713319). Verified at publisher: "increased pupil responses during manipulated trials regardless of whether they verbally reported detecting the swap." Notably the sibling [[pupillometry-behavioural-channel]] article does NOT name Pärnamets 2015 for this claim and does not even list it in its References — the misattribution was local to this article.
  - **Resolution**: re-sourced the inline cite and the References entry to Grassi et al. 2025 (the real demonstration); dropped Pärnamets 2015 entirely (it had no other function here). Re-scoped the evidential framing: "cross-laboratory replication is solid" was itself an overclaim once anchored on a single recent study, so it now reads as a recent autonomic-dissociation finding with a live covert-detection-vs-lower-level-surprise interpretive dispute. Kept *contested but real* tier (consistent with the sibling article's framing).

### Publisher-of-Record Citation Web-Verify (per-cite ledger)

Ran check (i) claim-direction, (ii) URL/DOI-vs-author, and (iii) fabrication on the choice-blindness core this pass:

- Grassi, Hoeppe, Baytimur & Bartels 2025 (*Frontiers in Psychology* 16, 1598254; DOI 10.3389/fpsyg.2025.1598254) — **real-correct** (newly added; verified at PMC12713319; claim-direction matches: pupil registers manipulation even when verbal report does not).
- Pärnamets et al. 2015 (*PNAS* 112(13), 4170–4175) — **real-wrong-claim (removed)**: paper is real and metadata was exact, but its finding (gaze-timing biases moral choices) does not support the pupillometric-swap-detection claim it was attached to. De-cited.
- Johansson, Hall, Sikström & Olsson 2005 (*Science* 310(5745), 116–119) — **real-correct**; claim-direction faithful (subjects fail to notice intention/outcome mismatch; confabulated justifications match authentic ones). Re-verified prior passes.
- Rebouillat, Léonetti & Kouider 2021 (*Neuroscience of Consciousness* 2021(1), niab004) — **real-correct**; claim-direction faithful (high-confidence confabulation when internal variables are weak → confidence does not track accuracy). Deflationary source used honestly, not toward a dualist conclusion.
- Sagana, Sauerland & Merckelbach 2014 (*Frontiers in Psychology* 5, 449) — **real-correct** (re-verified from June pass; the June re-source of the fabricated "Sauerland 2020" held; zero residue).
- Hall et al. 2010 (*Cognition* 117(1), 54–61); Hall, Johansson & Strandberg 2012 (*PLOS ONE* 7(9), e45457); Kane 1996/2024 (OUP); Wegner & Wheatley 1999 (*American Psychologist* 54(7), 480–492); Wegner 2002 (*The Illusion of Conscious Will*, MIT Press); Schurger, Sitt & Dehaene 2012 (*PNAS* 109(42), E2904–E2913) — all **real-correct**, web-verified across the two June passes and unchanged; claim-directions faithful. Not re-litigated.

**Empirical-record currency sweep**: helper returns no superlative claims. Nothing to currency-check.

**Inline ↔ References cross-reference**: complete after the swap. No orphans in either direction (Pärnamets removed from both inline and References simultaneously; Grassi added to both; Schurger 2012 supports the named reanalysis note, acceptable).

### Citation-Framing / Rival-as-Ally Check (task item d)

Choice-blindness and confabulation researchers (Johansson, Hall, Wegner, Rebouillat) are typically deflationary about conscious authorship. The article cites them honestly: the interface-failure reading is held at *live hypothesis* and "not upgraded by the present case alone"; the Wegner section explicitly *declines* the strong illusory reading and attributes the Map's pushback to "broader grounds, not from the choice-blindness data" (Mode Three boundary-marking); the "data do not establish dualism" boundary is stated outright. No rival-as-ally framing.

### Counterarguments Considered

- Brain-on-its-own confabulation (Dennett-style), Wegner's strong illusory reading, materialist absorption — preserved as honest live readings / Mode Three boundary-marking per all three prior reviews. Bedrock at the framework boundary; not correctable defects; not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The three "cannot deliver" boundaries and the discovery-from-outside parallel with aphantasia/synaesthesia remain surgical and original.
- Kane engagement as "mutual constraint, not mutual support" is precise scope discipline.
- Detection-rate-variability-as-cleanest-exhibit section's three-feature structure is a strong organizing device.

### Enhancements Made

- Re-sourced the pupillometric corroboration to the correct study and tightened its evidential framing (net +23 words; 2806 words, 94% of soft threshold — no length concern).

### Cross-links Added

- None needed; cross-link fabric is dense and all spot-checked wikilinks resolve live (phenomenal-output-causal-machinery-dissociation, introspection-architecture-independence-scoring, anti-correlated-metacognitive-signal, microphenomenological-interview-method, project/common-cause-null, aphantasia, synaesthesia, source-attribution-divergence, agency-void).

## Reasoning-Mode Classification (editor-internal)

- Engagement with Wegner's strong illusory reading: **Mode Three** (framework-boundary marking).
- Engagement with materialist absorption: **Mode Three**.
- Engagement with Kane's framework: **Mixed (Mode Three / scope-clarification)** — "mutual constraint, not mutual support."

No label leakage. No editor-vocabulary in article prose.

## Possibility/Probability Slippage Check

- Detection-rate variability held at *strongly supported* (correct).
- Interface-failure interpretation held at *live hypothesis*, explicitly "not upgraded by the present case alone" (correct).
- Pupillometric corroboration held at *contested but real*, and the fix removed an incidental "cross-laboratory replication is solid" overclaim (now honest about the finding's recency). A tenet-accepting reviewer would not flag any remaining claim as overstated. No slippage.

## Length Check

- 2806 words (94% of 3000 soft threshold) — ok. Net +23 words from the citation re-source; no trim required.

## Remaining Items

None. The metadata-only-verification blind spot that ratified the Pärnamets mismatch across three passes is now closed for this article; the check-(i) claim-match discipline should be carried into future citation audits corpus-wide.

## Stability Notes

- The prior "converged, no critical issues" verdict was correct *on the dimensions the prior passes checked* (metadata) but missed the claim-match dimension. This is not oscillation — it is a genuinely new defect class surfaced by a check the prior passes did not run. Future passes should NOT re-flag the resolved Pärnamets/Grassi swap.
- Bedrock framework-boundary disagreements (materialist absorption; Wegner's strong illusory reading; the "data do not establish dualism" boundary; the interface-vs-confabulation underdetermination; Kane mutual-constraint register) are all honestly handled and must NOT be re-flagged as critical.
- With claim-match now verified alongside metadata, the article's citation base is on its firmest footing across four passes. A "no critical issues" state is the expected steady-state outcome; convergence damping should reduce re-selection frequency.
