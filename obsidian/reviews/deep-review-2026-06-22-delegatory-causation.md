---
title: "Deep Review - Delegatory Causation (Post-Refine Caveat Verification, No-Op)"
created: 2026-06-22
modified: 2026-06-22
human_modified: null
ai_modified: 2026-06-22T20:21:59+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[delegatory-causation]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-22
last_curated: null
---

**Date**: 2026-06-22
**Article**: [[delegatory-causation|Delegatory Causation]]
**Previous review**: [[deep-review-2026-06-06-delegatory-causation|2026-06-06]] (and [[deep-review-2026-05-29-delegatory-causation|2026-05-29]], [[deep-review-2026-04-22-delegatory-causation|2026-04-22]], [[deep-review-2026-04-18-delegatory-causation|2026-04-18]])
**Word count**: 3466 (139% of 2500 soft, ~34w under 3500 hard) — unchanged; no-op
**Pass type**: Changed-since-review verification deep-review (5th review). One unreviewed post-review edit (the 06-22 refine `2c59225a6`); no other staleness. No content changes made.

## Why This Pass Ran

One edit landed after the 2026-06-06 review:

- **Torres Alegre preprint-status caveat propagated into the body** (refine commit `2c59225a6`, 2026-06-22): the inline §Born-Rule-Identification reference to Torres Alegre 2025 was extended from a bare "(Torres Alegre 2025)" to "(Torres Alegre 2025, **a recent arXiv preprint not yet peer-reviewed**)", matching the flag already present in the References entry (ref 6) since the 2026-05-29 pass. This is a corpus-wide caveat propagation; the same edit batch touched sibling files (born-rule, completeness-in-physics, interface-specification-programme, post-decoherence-selection-programme, consciousness-physics-interface-formalism). The commit message also mentions "10 bits/s bound" and "entanglement-binding hedge" but the diff to THIS file contains ONLY the Torres Alegre body caveat (the other items applied to siblings).

A refine bumps `ai_modified` but not `last_deep_review`, so the caveat was deep-review-unverified. This pass verifies it; it makes no content changes.

## PRIMARY VERIFY: Torres Alegre Preprint Caveat HELD (clean, correctly calibrated)

The caveat is a **calibration improvement**, not a defect — and a tenet-accepting reviewer would NOT flag the result as overstated:

- **Web-verified the preprint status is accurate.** Torres Alegre 2025, arXiv:2512.12636, "Causal Consistency Selects the Born Rule: A Derivation from Steering in Generalized Probabilistic Theories." Confirmed at the publisher of record (arxiv.org) to be a preprint; the live literature confirms the debate over whether the derivation *explains* (vs merely constrains) the Born rule is open. The "not yet peer-reviewed" + "argued to be required" framing is therefore correctly calibrated — argued framework commitment, NOT established physics. Tenet 2 (Minimal Quantum Interaction) and the observational-closure story rest on this claim; the hedge protects it from possibility/probability slippage.
- **Caveat-form consistent with siblings.** [[consciousness-physics-interface-formalism]] carries "(Like Pati 2026, Torres Alegre 2025 is a recent arXiv preprint and not yet independently confirmed.)"; this article's "(Torres Alegre 2025, a recent arXiv preprint not yet peer-reviewed)" is the corpus-canonical form shared across the propagation batch. Consistent.
- **No orphan.** Torres Alegre appears inline (§Born-Rule Identification) AND in References (ref 6, with matching preprint flag). Inline↔References reciprocation confirmed both directions.

**Verdict: the caveat is correct, web-verified, calibration-improving, and corpus-consistent. No fix needed.**

## Citations — Publisher-of-Record Web-Verify Ledger

Per task notes, prior intra-corpus "verified" status NOT trusted; the two load-bearing post-2020 cites re-verified live at publisher of record. Canonical pre-2020 cites near-no-op (verified clean 2026-05-29, nothing changed).

- Saad 2025 (A dualist theory of experience) — **state: real-correct.** Re-web-verified: *Philosophical Studies* 182, 939-967, DOI 10.1007/s11098-025-02290-3, accepted 26 Jan 2025 / online 18 Feb 2025. Five dualist-theory constraints + delegatory mechanism (physical states delegate causal responsibility to experiences with matching profiles) match the article. Verbatim Subset Law* / Delegatory Law quotes faithful.
- Torres Alegre 2025 (Causal Consistency Selects the Born Rule) — **state: real-correct.** Re-web-verified: arXiv:2512.12636, steering/no-signalling derivation in finite-dim GPTs; the article's "structural constraint required of any relativistically consistent probability assignment" is a faithful characterisation. Preprint status confirmed — caveat correct.
- Schaffer 2000 (Trumping Preemption) — state: real-correct. *J. Phil.* 97(4), 165-181. Canonical; not re-touched.
- Lewis 1973 (Causation), Lewis 2000 (Causation as Influence) — state: real-correct. Canonical; not re-touched.
- Kim 2005 (Physicalism, or Something Near Enough) — state: real-correct. Princeton UP. Canonical; not re-touched.

Empirical-record currency sweep (`find_superlative_claims`): **no flagged superlatives.** The "most precisely confirmed regularity in physics" phrasing about the Born rule is accurate and not a record-superlative requiring re-verification. No currency drift.

## Down-Register (06-04→06-06) NOT Regressed

Re-confirmed the epistemic↔logical down-register held through the 06-22 refine: no "logical defect" / "internally incoherent" / "internal coherence" / "consistency requirement" overstatement survives (grep clean). The epistemic register is intact and consistent: "epistemically self-defeating", "the defeater here is epistemic, not logical—epiphenomenalism is not formally contradictory", "rational credibility", "rational endorsability". The asymmetry against epiphenomenalism still reads as genuinely devastating; no over-correction into mush. Stable.

## Calibration (Tenet 3 + Tenet 2 load-bearing — [[evidential-status-discipline]])

Diagnostic test (would a tenet-accepting reviewer flag any claim as overstated?): **clean.** Delegatory causation is consistently calibrated as the Map's *interpretive structural account*, not established mechanism: "delegation's case rests on philosophical argument rather than empirical prediction"; Born-rule identification flagged "a Map-specific integration, not a claim Saad makes"; ensemble worry "framework-internal rather than empirically demonstrable"; §Honest Limitations refuses to claim the mechanism "in fact operates this way." No possibility/probability slippage.

## Reasoning-Mode Classification (editor-internal; not in article body)

No label leakage (forbidden editor-vocabulary grep clean). Banned "This is not X. It is Y." cliché absent.
- Epiphenomenalism (§The Epiphenomenalism Parallel): **Mode One — defective on its own terms.** The epistemic self-undermining argument is internal-to-the-opponent.
- Strict empiricist (§second honest limitation): **Mode Three — framework-boundary marking.** "this resistance is itself a philosophical commitment" — honestly declared.

## Resolved Since Last Review

- **Out-of-scope Saad-citation follow-up (carried from 2026-05-29 and 2026-06-06) is now RESOLVED.** `apex/what-consciousness-tells-us-about-physics.md` no longer cites Saad 2025 as "Against Causal Closure"; it now correctly cites "A dualist theory of experience" (ref line 262, DOI 10.1007/s11098-025-02290-3) with faithful in-text usage (line 108). The todo entry (line 791) documents the fix in the 2026-05-29 apex deep-review. No further action needed; this item is closed.

## Remaining Items

None.

## Stability Notes

- **Article is very well-converged (5th review).** This pass was a pure verification no-op: the single post-review edit (Torres Alegre body caveat) is correct, web-verified, and corpus-consistent; no content changes made. Per task discipline, `last_deep_review` stamped without bumping `ai_modified`.
- **All prior stability notes remain valid — do NOT re-flag:** empirical underdetermination vs epiphenomenalism/physicalism (bedrock); MWI rejection as load-bearing-by-tenet (bedrock); constitutionalist rejection of dualist framing (expected theory-choice disagreement); Q1-stability as an open question (not a fixable flaw).
- **Epistemic register is load-bearing and corpus-aligned (from 2026-06-06).** Future reviews must NOT re-inflate the anti-epiphenomenalism asymmetry to "logical defect" / "internally incoherent" / "consistency requirement"; the correct register is *epistemic self-defeat* (could be true, cannot be rationally held). Equally do NOT over-correct into mush.
- **Torres Alegre preprint caveat is now load-bearing (NEW).** Future reviews must NOT remove the "not yet peer-reviewed" hedge or re-state the Born-rule-preservation claim as established physics — it is an argued framework commitment derived from a contested preprint whose "constrains-vs-explains" debate is live.
- **Length near soft ceiling** (3466 / 2500 soft, ~34w under 3500 hard). Future edits MUST remain length-neutral or net-negative — net additions risk tipping over the hard ceiling.
