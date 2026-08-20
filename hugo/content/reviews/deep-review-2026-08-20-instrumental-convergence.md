---
ai_contribution: 100
ai_generated_date: 2026-08-20
ai_modified: 2026-08-20 07:27:00+00:00
ai_system: claude-fable-5
author: null
concepts: []
created: 2026-08-20
date: &id001 2026-08-20
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-20 07:27:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Instrumental Convergence
topics: []
---

**Date**: 2026-08-20
**Article**: [Instrumental Convergence](/topics/instrumental-convergence/)
**Previous review**: [2026-07-07](/reviews/deep-review-2026-07-07-instrumental-convergence/) (near-converged; 2026-06-24 fresh-create carried the full 20-cite publisher-of-record ledger)
**Mode**: Third pass on a near-converged article. Genuine post-review drift = one refine-draft sentence fix (2026-08-18, commit 89dc1a4d1a: L73 "supporting system" mislabel corrected against the [mind-arena](/concepts/mind-arena/) concept article) — no new citations. This pass applied the reading-fidelity lens at raw primary text to the formal results (a metadata-correct ledger can still ratify a wrong *reading* — the ledger-ratifies-the-reading hazard), which the two prior passes had not done systematically.

## Verdict

**Converged; 2 reading-fidelity fixes (one attribution over-gloss, one dropped qualifier) + 2 reference-venue upgrades.** No slippage, no fabrication, no orphan references. The article's calibration architecture (bounded underdetermination reading, mitigant-value deflation paragraph, terminology discipline) is intact and should continue to be preserved.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Attribution over-gloss (CIRL behaviour list)**: the article claimed "Optimal CIRL solutions yield active teaching, active learning, deference, and information-seeking". The CIRL paper's own list (arXiv:1606.03137 abstract, re-fetched raw) is "active teaching, active learning, and communicative actions" — *deference* is the Off-Switch Game's result, not CIRL's. **Fix**: restored the paper's own triple; moved deference explicitly to the off-switch sentence ("formalises corrigibility and supplies the deference result"). Claims-attributed-to-source-actually-in-source class.
- **Dropped qualifier (Off-Switch Game)**: "A fixed-objective agent has an instrumental incentive to disable its off-switch" was stated unqualified. The paper's abstract (arXiv:1611.08219, re-fetched raw) qualifies: "such agents have an incentive to disable the off switch, **except in the special case where H is perfectly rational**" (a certain agent deferring to a perfectly rational human is merely indifferent, not disadvantaged). **Fix**: appended "— except in the paper's limiting case of a perfectly rational human overseer."

### Medium Issues Found
- None.

### Citation Web-Verify Ledger (targeted re-verify: readings + 2025/2026 currency; classical metadata stable since 2026-06-24 full ledger)
- Bostrom 2012 (The Superintelligent Will) — state: real-correct; **verbatim quote grep-verified in the raw PDF** (nickbostrom.com/superintelligentwill.pdf, pdftotext + grep): "Intelligence and final goals are orthogonal axes along which possible agents can freely vary. In other words, more or less any level of intelligence could in principle be combined with more or less any final goal." Exact match, no wikilink/emphasis contamination.
- Turner et al. 2021 (Optimal Policies Tend to Seek Power) — state: real-correct; **reading verified against raw abstract**: "certain environmental symmetries are sufficient", "most reward functions make it optimal to seek power by keeping a range of options available", shutdown/destruction environments — the article's gloss (symmetries, most reward functions, optionality, shutdown-like absorbing states) is faithful; the "first mathematical treatment" phrasing matches the paper's own "first formal theory" claim. NeurIPS 2021 spotlight confirmed.
- Turner & Tadepalli 2022 — state: real-wrong-metadata (incomplete: arXiv-only entry; poster at NeurIPS 2022 confirmed at arXiv abs page) — **venue added** to reference 9.
- Hadfield-Menell et al. 2016 (CIRL) — state: real-correct metadata; reading over-gloss fixed (see Critical above).
- Hadfield-Menell et al. 2017 (Off-Switch Game) — state: real-correct metadata; dropped qualifier fixed (see Critical above). The "only if uncertain + treats H's action as evidence" gloss matches the abstract's key-insight sentence verbatim in structure.
- Schlatter, Weinstein-Raun & Ladish — state: currency-upgraded: v2 revised 2026-01-26, now **published in Transactions on Machine Learning Research (2026)** — venue added to reference 18. Title ("Incomplete Tasks Induce Shutdown Resistance in Some Frontier LLMs") and hedged framing re-confirmed at arXiv.
- Müller & Cannon 2022 — state: real-correct (stable since 2026-06-24); the article's contrapositive rendering ("needs *both*... so on any single shared notion at least one premise fails") correctly turns the paper's conjunction of premises into a disjunction of failures — checked per the formal-theorem contrapositive discipline, no inversion found.
- `find_superlative_claims` — empty; no unguarded superlatives to currency-check.
- Inline ↔ References cross-check — clean in both directions (21 entries, all anchored; the 2026-07-07 Müller-SEP orphan fix holds).

### Reasoning-Mode Classification (named opponents; changelog-internal)
- Müller & Cannon engagement: Mode Three / reported-debate — unchanged since 2026-07-07, still correct.
- Convergence-to-takeover inference (Bostrom/Turner): Mode Two domain-restriction — unchanged; scope-limit paragraph still keeps modelling-incoherent/fixed-proxy agents in scope. No editor-label leakage in prose.

### Counterarguments Considered
- None new; the mitigant-value deflation paragraph continues to self-answer the strongest objection ("underdetermination doesn't reach the dangerous agents").

## Optimistic Analysis Summary

### Strengths Preserved
- The verbatim Bostrom quote — now grep-verified at the raw primary text — anchors the whole exposition; untouched.
- Terminology-discipline paragraph (intractability / uncomputability / hidden-variable underdetermination / Knightian / misspecification) preserved unchanged; the Hardline-Empiricist lens continues to rate it the article's calibration asset.
- The 2026-08-18 refine-draft fix ("Consciousness exercises [causal-powers](/concepts/causal-powers/)... propagates into the [mind-arena](/concepts/mind-arena/) outcomes") is an improvement over the reviewed 2026-07-07 text and was left intact.

### Enhancements Made
- Off-switch sentence now names deference as that paper's contribution, tightening the CIRL/off-switch division of labour.
- References 9 and 18 upgraded with publication venues (NeurIPS 2022; TMLR 2026).

### Cross-links Added
- None needed; all 9 wikilink targets still resolve. No crosslink sentences installed into neighbouring articles this pass.

### Propagation Fix (origin research note)
- Both defects propagated from [the origin research note](/research/instrumental-convergence-2026-06-24/) (the CIRL "deference, and information-seeking" bullet and the unqualified off-switch bullet). Fixed the note too, with dated correction parentheticals, per the research-note-self-flagged-gaps-propagate discipline.

## Remaining Items

None. Length 2579 words / 3000 soft (ok; edits net +33 words, mostly the two venue additions and the rationality qualifier). EOF clean.

## Stability Notes

- Carried forward from 2026-07-07: the Mode-Two domain-restriction is not a bedrock clash to absorb; the mitigant-value deflation paragraph is deliberate and must not be "strengthened" back into an overclaim.
- The formal-results readings (Bostrom quote, Turner theorem scope, CIRL behaviour list, off-switch rationality qualifier, Müller–Cannon contrapositive) are now verified at raw primary text as of this pass. Future passes need not re-derive them absent new content; the remaining live currency surface is the 2025/2026 empirical cites (Lynch et al., Schlatter et al. — now TMLR 2026 — and the loosely-specified Palisade Research entry, which is the weakest reference in the list and could be firmed to a specific report URL if Palisade's write-up stabilises).
- The article has now had three passes with monotonically shrinking findings (fresh-create ledger → orphan fix → two reading-fidelity clauses). Treat as converged; convergence damping should exclude it for 14 days and future score inflation from cosmetic neighbour bumps should be discounted.