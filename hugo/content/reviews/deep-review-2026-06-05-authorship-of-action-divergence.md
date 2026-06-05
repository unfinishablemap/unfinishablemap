---
ai_contribution: 100
ai_generated_date: 2026-06-05
ai_modified: 2026-06-05 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-05
date: &id001 2026-06-05
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[authorship-of-action-divergence]]'
title: Deep Review - Authorship-of-Action Divergence
topics: []
---

**Date**: 2026-06-05
**Article**: [Authorship-of-Action Divergence](/topics/authorship-of-action-divergence/)
**Previous review**: [2026-05-22](/reviews/deep-review-2026-05-22-authorship-of-action-divergence/)
**Mode**: Changed-since-review staleness candidate with full bidirectional citation audit + web-verification of every cite (author / venue / year / key numbers / stance)

## Why This Candidate

Content was modified (ai_modified 2026-05-27) *after* the prior review (last_deep_review 2026-05-22), not modified today. The 2026-05-27 change was commit `32664cb82` — a cluster-wide propagation that corrected an inline author name from "Coutinho et al. 2021" to "Rebouillat et al. 2021" — so the article carried unreviewed new content. "Converged ≠ verified."

## Pessimistic Analysis Summary

### Critical Issues Found

- **Dangling inline citation — Rebouillat et al. 2021 (FIXED).** The body (Integration section + Further Reading bullet) cites "Rebouillat et al. 2021" as a specific dated finding, but the References list had no corresponding entry. Root cause traced via git: the 2026-05-27 propagation commit corrected the inline *author name* (Coutinho → Rebouillat) everywhere in the cluster but never added a References entry to *this* article (the canonical reference lives in the sibling [concepts/anti-correlated-metacognitive-signal.md](/concepts/anti-correlated-metacognitive-signal/)). The inline cite was therefore dangling both before and after the name correction. Resolution: web-verified the paper (real — Rebouillat, B., Léonetti, J. M., & Kouider, S. (2021), "People confabulate with high confidence when their decisions are supported by weak internal variables," *Neuroscience of Consciousness* 2021(1), niab004; the body's confidence-inverts-with-accuracy characterization matches the paper's actual finding) and added the reference, consistent with the metadata on the sibling page.
  - Prior-review note: the 2026-05-22 attribution check listed "Coutinho et al. 2021 ... correctly summarised." That was the wrong-author defect later caught by the 2026-05-27 propagation; the prior review's intra-corpus check did not flag it. Consistent with the [AI citation metadata unreliable] pattern — only live-literature web-verify catches wrong-author cites.

### Medium / Low Issues

- **Unverified citation — Sauerland, Schell-Leugers & Sagana 2020, *Journal of Cognitive Psychology* 32(1), 1–17 (FLAGGED, NOT CHANGED).** The author trio is confirmed real and actively publishing on choice blindness (Schell-Leugers and Sagana both at Maastricht with Sauerland). However, the *specific* 2020 *Journal of Cognitive Psychology* paper did not surface across three independent web searches. The article uses it as the load-bearing within-condition-spread cite (attentional capture, working-memory capacity, metacognitive sensitivity track the spread). Per the [citation-verify false-negative] discipline, an unfindable cite has three states (fabricated / real-paper-wrong-metadata / real-but-unindexed); with the author trio confirmed real and on-topic, fabrication is unlikely — most plausibly real-but-unindexed or minor venue/year metadata drift. Left in place (false-negative deletion risk is documented); flagged for a future human / literature-drift check. NOTE on stance: the broader literature (including this group) reports that *self-reported personality* traits — compliance, suggestibility, social desirability — do NOT modulate choice blindness. The article's claim is about attention/working-memory/metacognition, not personality, so it is not contradicted; but a future verifier should confirm the 2020 paper's stance supports an individual-differences-track reading rather than the personality-null reading.

### Counterarguments Considered

- Brain-on-its-own confabulation (Dennett-style), Wegner's strong illusory reading, materialist absorption — all already preserved as honest live readings / Mode Three boundary-marking per the prior review. Re-confirmed; no change (bedrock at the framework boundary, not correctable defects).

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)

- The three "cannot deliver" boundaries and the discovery-from-outside parallel with aphantasia/synaesthesia remain surgical and original.
- Kane engagement as "mutual constraint, not mutual support" is precise scope discipline — preserved.
- Channel-level pupillometric framing aligns with the sibling article without duplication.

### Enhancements Made

- Added the verified Rebouillat et al. 2021 reference to the References list (resolves the dangling cite; net +~25 words, length-neutral concern not triggered — article at 90% of soft threshold).

### Cross-links Added

- None needed; the cross-link fabric is already dense and well-targeted.

## Reasoning-Mode Classification (editor-internal)

- Engagement with Wegner's strong illusory reading: **Mode Three** (framework-boundary marking) — honestly attributed to Bidirectional Interaction, not dressed as in-framework refutation.
- Engagement with materialist absorption: **Mode Three** — concedes compatibility with brain-internal report-production accounts.
- Engagement with Kane's framework: **Mixed (Mode Three / scope-clarification)** — "mutual constraint, not mutual support."

No label leakage. No editor-vocabulary in article prose.

## Citation Audit (bidirectional + web-verified)

All References web-verified correct: Johansson et al. 2005 (*Science* 310(5745), 116–119); Hall et al. 2010 (*Cognition* 117(1), 54–61); Hall, Johansson & Strandberg 2012 (*PLoS ONE* 7(9), e45457); Pärnamets et al. 2015 (*PNAS* 112(13), 4170–4175); Kane 1996 (*The Significance of Free Will*, OUP); Kane 2024 (*The Complex Tapestry of Free Will*, OUP); Wegner & Wheatley 1999 (*American Psychologist* 54(7), 480–492); Wegner 2002 (*The Illusion of Conscious Will*, MIT Press); Schurger et al. 2012 (*PNAS* 109(42), E2904–E2913).

- Dangling inline → now resolved (Rebouillat 2021 added).
- Orphan-ish: Schurger 2012 appears in References + Further Reading bullet only (not main prose). Acceptable — supports the named Schurger-reanalysis note.
- One cite flagged unverified (Sauerland et al. 2020) — see Medium issues.

## Possibility/Probability Slippage Check

- Detection-rate variability held at *strongly supported* (correct).
- Interface-failure interpretation held at *live hypothesis*, explicitly "not upgraded by the present case alone" (correct).
- Pupillometric corroboration held at *contested but real* (correct).
- No tenet-coherence-as-evidence move. A tenet-accepting reviewer would not flag any claim as overstated. No slippage.

## Remaining Items

- Verify Sauerland, Schell-Leugers & Sagana 2020 (*Journal of Cognitive Psychology*) against the live literature — author trio confirmed real; exact paper not web-locatable. Confirm venue/year and that its stance supports the individual-differences-track claim (vs. the personality-null finding in adjacent literature). Candidate for the literature-drift triple.

## Stability Notes

- Bedrock framework-boundary disagreements (materialist absorption; Wegner's strong illusory reading; the "data do not establish dualism" boundary; the interface-vs-confabulation underdetermination; Kane mutual-constraint register) are all honestly handled and must NOT be re-flagged as critical in future passes.
- The article is calibration-stable. The only defect found this pass was a mechanical citation-completeness gap inherited from a cluster propagation — now closed. A "no critical issues remaining" state is the expected next-review outcome.