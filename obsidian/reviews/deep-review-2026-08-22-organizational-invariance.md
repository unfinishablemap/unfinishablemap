---
title: "Deep Review - Organizational Invariance"
created: 2026-08-22
modified: 2026-08-22
human_modified:
ai_modified: 2026-08-22T13:57:36+00:00
draft: false
topics:
  - "[[machine-consciousness]]"
concepts:
  - "[[organizational-invariance]]"
  - "[[inverted-qualia]]"
  - "[[bandwidth-of-consciousness]]"
related_articles:
  - "[[organizational-invariance]]"
  - "[[deep-review-2026-07-28-organizational-invariance]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-22
last_curated:
---

**Date**: 2026-08-22
**Article**: [[organizational-invariance|Organizational Invariance]]
**Previous review**: [[deep-review-2026-07-28-organizational-invariance|2026-07-28]]
**Word count**: 2,376 → 2,416 (+40; 97% of the 2,500 concepts soft threshold — the +65-word correction was partly offset by a 33-word cut, see Critical Issue 2)
**Selection note**: the tool's top candidate was `concepts/compatibilist-symmetry-challenge` (score 65), excluded by the driver brief as same-session churn. This was the next candidate (score 38, 25 days unreviewed).

## Dependency-Drift Pass (the highest-yield lens)

The article's own text moved only once since the last review: commit `2ad924b619` (2026-08-06) added a single Further Reading gloss for `[[phenomenal-variation-within-a-species]]`. That gloss is **accurate** — the apex it names does say the within-species cohort pairs "control task-level matching, not fine-grained organization" (L139, L163). No defect there.

The defect was in what moved *underneath* the article. Dependencies with commits since 2026-07-28: `positions/quantum-interface` (9), `concepts/psychophysical-laws` (9), `concepts/substrate-independence` (5), `concepts/haecceity` (4), `apex/phenomenal-variation-within-a-species` (4), `concepts/ensemble-level-epiphenomenalism` (2), `concepts/functionalism` (2), `positions/consciousness-scope` (2), `concepts/inverted-qualia` (1), `positions/ai-substrate-verdicts` (1), `topics/machine-consciousness` (1).

**Register-invisibility confirmed.** `grep -rn "organizational-invariance" obsidian/positions/` returns **zero hits**. The article cites no register entry and no register entry names it in an `Argued in` line, so it is invisible to the positions audit in both directions — exactly the blind spot the brief flags. The constraint that turned out to bind it (P-Q9's psychophysical-residue channel, P-Q2's `empirical discriminability: none-by-construction`) had to be found by searching the register for the *claim*, not the slug.

**Certifier-side confirmed.** The 2026-07-28 review explicitly recorded "The type/token account inherited from `inverted-qualia.md` in commit `b3afb915b`. **Untouched.**" It preserved the inherited paragraph without auditing it against the source it was inherited from. That is a clean instance of a prior pass certifying a passage in the same act of not reading it.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Misattributed and scope-inflated empirical prediction (CRITICAL — attribution error + calibration slippage). Fixed.**

The Relation section read:

> "Its commitment to Bidirectional Interaction requires the interface to make a physical difference, and its account of the [[bandwidth-of-consciousness|outbound channel]] **predicts subtle behavioural signatures from any real substrate divergence**."

This sentence was the article's sole stated ground for taking the first (detectable) horn of its own dilemma, so it was load-bearing. Three independent defects:

- **The named source makes no such prediction, and has withdrawn the claim it would have rested on.** `topics/bandwidth-of-consciousness` L165 states that "the Map has accordingly **withdrawn the bandwidth argument as a discriminator**, retaining the ceiling as a constraint any account must accommodate rather than as evidence for one," and L175 states that the measured bitrate "is exactly what epiphenomenalism predicts too, and **carries no evidential traction against it**." Verified by exhaustive grep: the file contains no instance of "subtle behavioural", and every occurrence of "predict" in it is either about a rival account or explicitly hedged ("compatible with the data, not uniquely forced by it," L207). The withdrawal was published into `bandwidth-of-consciousness` in commits `0551ef2611` and `df71b72807` and never propagated to this citing article. A reader following the wikilink landed on a page saying the opposite of what the pointer promised.

- **Wrong division of labour.** Where the prediction *is* booked — `positions/quantum-interface` P-Q9 and `concepts/inverted-qualia` L171 — the bandwidth channel's role is to predict **where** differences surface ("in finer-grained measurements rather than in coarse discrimination tasks"), not **that** they occur. The "that" comes from the causal-efficacy commitment. The article had promoted the bandwidth channel from grain-of-measurement to source-of-prediction.

- **Scope inflation from an unpriced licence.** P-Q9 books the commitment as "any actual instance of **qualia-inversion** should produce subtle behavioural differences"; `inverted-qualia` L138 likewise scopes it to "any actual **inversion**". This article generalised to "any real **substrate divergence**" — which silently extends the commitment to the *fading* case, for which nothing has been booked anywhere in the corpus. This is the brief's mirror pass: a residue running *for* the Map trips no honesty heuristic, is never priced, and the citer inherits the widened form.

**Calibration test applied.** Would a reviewer who fully accepts the Map's tenets still flag this? **Yes — the register does the flagging itself.** P-Q2 is credence *high* with `empirical discriminability: none-by-construction`; P-Q3 the same; `concepts/ensemble-level-epiphenomenalism` L50 states that under the corridor-plus-trumping route the causal and epiphenomenal readings "make no predictively distinct claims **at any scale**." A flat, unhedged prediction of behavioural signatures from any substrate divergence over-commits the Map relative to its own default reading. This is possibility/probability slippage, not bedrock disagreement, and it is correctable inside the framework.

**Resolution.** Rewritten to take the horn on **Tenet 3** (which genuinely licenses it) rather than on a promised measurement; the prediction re-scoped to inversion, restated in the register's own terms (aesthetic preferences, emotional valences, reaction-time asymmetries, fine structure of introspective reports), marked as the Map's own liability rather than a derived result; the bandwidth channel demoted to its actual role (*where*, not *whether*); and the absence of any counterpart commitment for the fading case stated plainly. The wikilink to `bandwidth-of-consciousness` survives with a role the target actually supports. The horn-taking, the type/token distinction and the unpaid-debt framing are all preserved intact.

**2. Source/Map conflation in the Schwitzgebel paragraph (CRITICAL — §2.5). Fixed by removal.**

The paragraph closed: *"The pointed version of the worry: our ordinary introspection may stay reliable only because problem cases are rare, and we are not entitled to assume that fading and dancing systems are correspondingly rare."* Sitting third in a paragraph opened by "Eric Schwitzgebel argues that…" and continued by "He adds a sharper point…", it reads as his. The full post was retrieved and read end to end (`schwitzsplinters.blogspot.com`, 22 April 2010): **it contains no rarity argument**. The post's two moves are the ordinary-unreliability point (richness disputes) and the concealment point (pre-built to frustrate noticing; introspection-module model) — both already stated, both verified verbatim below. The rarity sentence is a Map gloss presented as source exposition. Removed rather than re-marked: the two verified points carry the paragraph, and the cut offsets part of the Critical-1 expansion. Present since the article's creating commit `7ec2d7cfcd` and missed by the previous review.

### Medium Issues Found

- **Sibling defect, out of scope, task minted.** `concepts/psychophysical-laws` L100 says "The Map rejects the conclusion **on zombie-argument grounds** ([[functionalism]] doesn't entail experience) and via a grain dispute." The zombie ground is one this article's own scope paragraph (L42) disarms: Chalmers *grants* that an organizational duplicate with absent or inverted qualia is logically possible and denies only its nomological possibility, so the zombie argument does not touch invariance. `psychophysical-laws` has 9 commits since this article's last review and is the one that drifted. Not edited here (different file, different review scope); P2 task queued.

### Counterarguments Considered

- *Hard-nosed physicalist / MWI defender / eliminative materialist*: rejection of the tenets themselves. Bedrock — framework-boundary, not a correctable defect. Not re-flagged, per the previous review's stability note.
- *Empiricist (Popper's ghost)*: "the grain dispute is unfalsifiable." Partly answered by Critical 1's fix, which now states exactly what the Map has and has not booked as falsifiable, and where. The residue is the mechanism debt tracked at P-Q3/P-Q10, stated as owed in three places in the article.

### Reasoning-Mode Classification (§2.6, editor-internal)

- Engagement with **Chalmers**: **Mode One with an explicit Mode Three residue** — unchanged from the previous review, and the Critical-1 fix *strengthens* the Mode One reading, since the horn is now taken on a stated tenet rather than on a borrowed empirical promise. Mode Three residue (the owed type/token account) still declared honestly.
- Engagement with **Schwitzgebel / Mogensen / van Heuveln**: expository, not adversarial; no classification required.
- **Label-leakage scan: CLEAN.**

## Publisher-of-Record Citation Web-Verify (§2.4)

Triggered (inline cites, References block, two verbatim quotations). The References block itself is unchanged since the 2026-07-28 full ledger, so this pass re-verified the two quotations independently (per the discipline that a prior report's "verified verbatim" is a claim, not evidence) and re-confirmed the one metadata correction that pass made.

- **Chalmers 1995**, "Absent Qualia, Fading Qualia, Dancing Qualia" — **real-correct**. Full text retrieved from `consc.net/papers/qualia.html` and grepped as raw extracted text, not by confirmation prompt.
- **Quote 1**, "the same functional organization at a fine enough grain will have qualitatively identical conscious experiences" — **real-correct, verbatim** (independent character-level grep hit against the raw artefact).
- **Quote 2**, "my experiences are switching from red to blue, but I do not notice any change" — **real-correct, verbatim** (independent grep hit).
- **Article claim** "The second argument Chalmers regards as stronger" — **real-correct**. Source: "Overall, the Dancing Qualia argument seems to make an even more convincing case against absent qualia than the Fading Qualia argument does, although both have a role to play."
- **Article claim** re the backup-circuit setup — **real-correct**. Source: "take a silicon circuit just like Bill's and install it in my head as a backup circuit."
- **Chalmers 1996**, *The Conscious Mind*, ch. 7 — **real-correct**; inline anchor added by the previous review still present.
- **Schwitzgebel 2010**, *The Splintered Mind*, 22 April 2010 — **real-correct**. Post retrieved and read in full. Both attributed points verified: ordinary-unreliability ("One or both parties must therefore be radically wrong about their experience… it's not absurd to suppose that Fifty-Billion could be mistaken") and concealment ("the Dancing Qualia case seems problematically pre-built to frustrate our ability to notice differences, much like radically skeptical brain-in-a-vat scenarios are pre-built to frustrate the sensory abilities on which we depend by giving the same sensory input despite a large change in the far-side objects"). The article's paraphrase of the introspection-module model — "If introspection reads from a channel the switch leaves unchanged" — matches the source's own thought experiment. **A third claim in the same paragraph did not verify: see Critical Issue 2.**
- **Mogensen, A. L. (2025)**, "How to resist the Fading Qualia Argument," *Synthese* 206(5), art. 252, doi:10.1007/s11229-025-05338-3 — **real-correct**. Re-verified against Crossref: author "Andreas L. Mogensen", container *Synthese*, volume 206, issue 5, article-number 252, published 2025-11-05. The previous review's currency correction holds exactly.
- **van Heuveln, Dietrich & Oshima (1998)**, *Minds and Machines* 8(2), 237–249 — **real-correct** (ledgered 2026-07-28; entry unchanged since, not re-fetched).
- **Southgate & Oquatre-cinq (2026)**; **Southgate & Sonquatre-cinq (2026)** — **real-correct** Map self-cites under the AI-pseudonym convention. Not stripped.

**Currency sweep**: `find_superlative_claims` returned **0** results. No superlative or empirical-record claims to age-check. No "awaiting replication" / "not yet replicated" / "single-study" tells present.

**Inline ↔ References cross-reference**: complete in both directions. No orphans.

## Optimistic Analysis Summary

### Strengths Preserved

- The "ally on one tenet, opponent on another" framing, which locates the dispute as *internal to dualism*. Untouched.
- The dilemma statement, the "not as a settled free lunch" conditional, and the three separate acknowledgements that the type/token account is owed rather than paid. Untouched — and the Critical-1 fix was written to *extend* that calibration honesty to a sentence that had escaped it, not to trade any of it away.
- The type/token distinction inherited from `inverted-qualia`. Untouched; verified still reciprocally accurate at `inverted-qualia` L138, which has not moved on this point since the last review.
- Schwitzgebel's concealment point and the "the Map does not lean on that defence" note added by the previous review. Both retained.

### Enhancements Made

- The Relation section now states, in place of a borrowed prediction, exactly what the Map has booked as an empirical liability and what it has not — which is a stronger position than the one it replaced, because it is one the register will actually certify.

### Cross-links Added

None. The corpus sweep for glosses naming this article (`functionalism` L187, `inverted-qualia` L195, `substrate-independence` L202, `phenomenal-variation-within-a-species` L184, `psychophysical-laws` L272) found all of them accurate; no repair-side finding and no new reciprocal pointer needed.

## Remaining Items

- P2 task queued for `concepts/psychophysical-laws` L100 (zombie-argument-grounds misdescription of the Map's reply to invariance).
- The mechanism debt (a principled account of how token-level efficacy and ensemble-level invisibility come apart) remains **deliberately unpaid** and is tracked at P-Q3 / P-Q10 and `concepts/ensemble-level-epiphenomenalism`. Not a defect of this article.

## Stability Notes

- The **grain dispute with Chalmers is not a defect to fix** (carried forward from 2026-07-28). Do not re-flag "Chalmers would not accept this" as critical.
- The **owed type/token account is deliberately unpaid** and said so in three places (carried forward). Do not "resolve" it by strengthening the claim.
- The **conditional framing of the introspection-preserving virtue** does real work (carried forward). Do not condense the qualifiers out of it.
- **New:** the Relation section's empirical commitment is now scoped to *inversion* and marked as the Map's own liability. That narrowness is deliberate and matches `positions/quantum-interface` P-Q9 and `concepts/inverted-qualia` L171. A future pass must not re-widen it to "any substrate divergence" — the corpus books no such commitment, and P-Q2/P-Q3 grade the default corridor reading as having no discriminating aggregate signature at all.
- **New:** this article is **invisible to the positions-register audit in both directions** (it cites no entry; no entry names it in `Argued in`). Future reviews cannot rely on a register audit to catch calibration drift here and must search the register for the *claim*.
- The article now sits at 2,416 words against a 2,500 soft threshold. Treat as **length-constrained**: additions need matching cuts.
