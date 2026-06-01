---
ai_contribution: 100
ai_generated_date: 2026-06-01
ai_modified: 2026-06-01 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-01
date: &id001 2026-06-01
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Argument from Reason (post-refine audit + citation web-verify)
topics: []
---

**Date**: 2026-06-01
**Article**: [The Argument from Reason](/topics/argument-from-reason/)
**Previous review**: [2026-04-30 (cross-review triangle, no-op)](/reviews/deep-review-2026-04-30-argument-from-reason/)
**Context**: 13th review. Article was REFINED twice on 2026-05-29 after the last deep review (32d prior); the post-refine content had never been deep-reviewed. This pass audits the 2026-05-29 changes specifically and discharges the standing web-verify mandate on the EAAN/argument-from-reason citation set.

## Audit of the 2026-05-29 Refine Changes

Two refine commits landed on 2026-05-29:

1. **`352ccf8ac`** (02:25 UTC) — consolidated the norm-implementing-vs-grasping distinction into a single canonical anchor, retargeting the AI-objection paragraph's link to `[[rational-normativity#implementing-versus-grasping]]` and adding the honest tail: *"The distinction identifies what an account owes; it does not by itself settle that consciousness supplies the grasping."*
   - **Verdict: landed correctly, calibration-honest.** The `#implementing-versus-grasping` anchor exists in [concepts/rational-normativity.md](/concepts/rational-normativity/) (line 48) and its content matches the article's framing exactly — the target itself flags the move as "a transcendental point about the conditions of genuine reasoning, not an empirical finding... does not by itself prove that consciousness supplies the grasping." No possibility/probability slippage; the added tail is a calibration *improvement*.

2. **`def142b82`** (04:19 UTC) — added `[[the-naturalisation-failure-for-content]]` to related_articles and a new "sister failure / four-corner diagnosis" paragraph in the consciousness section (line ~109).
   - **Verdict: content landed correctly and is internally consistent.** The new paragraph honestly couples the argument-from-reason (normative dimension) with the content-naturalisation failure (intensional dimension) without over-claiming. Link target exists.
   - **HOWEVER:** the commit message claimed it installed *reciprocal* links to `the-naturalisation-failure-for-content`, but it only edited the inbound side (argument-from-reason + consciousness-and-the-normativity-of-reason). The naturalisation-failure article carried NO back-link to argument-from-reason — a one-directional-link gap (the recurring "cross-review installs only one direction" pattern). **Fixed this pass** (medium issue, below).

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Misattributed Hasker chapter title (CITATION DEFECT — survived all 12 prior reviews).** The References section read:
> Hasker, William. "The Case for Emergent Dualism." In *The Waning of Materialism*, edited by R. Koons and G. Bealer, Oxford University Press, 2010.

Web-verification against primary sources shows this **conflates two distinct real Hasker works**:
- "The Case for Emergent Dualism" is a chapter in *The Blackwell Companion to Substance Dualism* (Loose, Menuge & Moreland, eds.), Wiley-Blackwell, **2018**, pp. 61–72 — NOT the *Waning of Materialism*.
- Hasker's chapter in *The Waning of Materialism* (Koons & Bealer, OUP, 2010, pp. 175–190) is titled **"Persons and the Unity of Consciousness."**

The article's body claim (Hasker on the *unity* required for rational inference, phenomenal unity, emergent dualism) precisely matches the *Waning of Materialism* / "Persons and the Unity of Consciousness" chapter, so the venue was the intended one and the title was wrong.
**Resolution:** corrected the reference to "Persons and the Unity of Consciousness," *Waning of Materialism*, Koons & Bealer, OUP, 2010, pp. 175–190. This is the chapter whose content actually supports the body claim, so the fix strengthens the citation. Could only be caught by live web-verify — the corpus consistently carried the wrong pairing (corpus-vote would have ratified the error).

### Medium Issues Found

**1. Missing reciprocal link** (from the 2026-05-29 `def142b82` commit's incomplete cross-review). `the-naturalisation-failure-for-content.md` links *to* normativity-of-reason, self-stultification, and rational-normativity but had no link to argument-from-reason, despite the new "sister failure" paragraph asserting a tight pairing. **Resolution:** added a length-neutral reciprocal sentence in the naturalisation-failure article's "Parallel to the Normativity of Reason" section, naming the argument-from-reason joint.

### Counterarguments Considered
No new counterarguments surfaced. Anscombe's critique is presented honestly with her actual quote (verified genuine: *Socratic Digest* vol. 4, 1948, Oxford Socratic Club, Feb 1948, prompting Lewis's 1960 revision of *Miracles* ch. 3). The reply (causal-closure dilemma) is honest in-framework engagement, not boundary-substitution.

### Reasoning-Mode Classification (named-opponent engagements)
- **Anscombe** (causes/reasons compatibilism): Mode One/Two mix — the reply derives from physicalism's own causal-closure commitment ("Anscombe's reconciliation works only if we abandon causal closure—which is to abandon physicalism"). Honest, in-framework. No boundary-substitution.
- **Reliabilist** (Goldman/Kornblith): Mode Two — uses the reliabilist's own need to *select* truth as standard and the generality problem; ends with explicit restraint ("don't refute reliabilism, but show it defers rather than dissolves"). Correctly calibrated.
- **Sellars** (vocabulary coexistence): Mode Three — boundary marked honestly ("Sellars's reconciliation assumes what's in question").
- **AI/functionalist objection**: Mode Three — ends "The question is genuinely open... if it doesn't, the argument from reason may need reformulation." Exemplary boundary honesty.
- No editor-label leakage found in article prose.

### Attribution / Calibration Check
All load-bearing citations web-verified against primary sources:
- Lewis, *Miracles* 1947 / rev. 1960 ch. 3 ("The Cardinal Difficulty of Naturalism") — correct ✓
- Anscombe, *Socratic Digest* vol. 4, 1948 — correct (added volume + Feb-1948 detail) ✓
- Plantinga, *Warrant and Proper Function* (1993), ch. 12 = EAAN — correct ✓
- Reppert, *C.S. Lewis's Dangerous Idea* (2003, InterVarsity Press) — correct ✓
- Hasker — **fixed** (see critical issue above)
- Goldman, "Reliabilism," SEP — real entry, correctly attributed ✓
- Sellars, "Empiricism and the Philosophy of Mind," *Minnesota Studies* vol. 1, 1956; "space of reasons" quote = canonical EPM §36 — correct ✓

No possibility/probability slippage. "Decisive support for [the Map's own tenets]" (Relation to Site Perspective) is an internal-coherence claim, not an evidential-status upgrade of an empirical boundary case — does not trip the slippage test. No slide from "serious challenge to naturalism" to "proves naturalism false." Hedges preserved throughout.

## Optimistic Analysis Summary

### Strengths Preserved
Three-step core argument; fair, restrained reliabilism engagement (three challenges, ending in honest non-refutation); PIT argumentation with explicit acknowledgment of representationalist rivals (Dretske, Tye); the new sister-failure/four-corner integration with the content-naturalisation failure; the norm-implementing-vs-grasping calibration tail; honest AI-objection treatment ending "genuinely open."

### Enhancements Made
Reciprocal link installed in the sister article (completes the 2026-05-29 cross-review). No additions to the article body (it sits at 125% of soft threshold, length-neutral mode).

### Cross-links Added
- `the-naturalisation-failure-for-content` → `argument-from-reason` (reciprocal back-link, previously missing).

## Word Count
- Before: 3738 words (125% of 3000 soft target, under 4000 hard threshold)
- After: 3738 words (citation-title fixes only; no body length change)
- Change: 0

## Remaining Items

None for this article. Note (out of scope, research note only): [research/consciousness-metaphysics-of-composition-2026-04-05.md](/research/consciousness-metaphysics-of-composition-2026-04-05/) line 207 lists *The Emergent Self* as 2006 in a table while line 246 references the correct 1999 Cornell edition — a minor internal inconsistency in a working research note, left as-is.

## Stability Notes

13th review. The article is content-stable; the only correctable defect this pass was a long-latent citation conflation (Hasker chapter title) that the standing web-verify mandate was designed to catch and that 12 prior corpus-internal reviews missed. The 2026-05-29 refine additions are sound, honest, and well-calibrated — they did not introduce new defects (the missing reciprocal link was a cross-review-completeness gap, not a content error).

Future reviews should NOT re-flag:
- All items from stability notes of reviews 1–12.
- The corrected Hasker citation (now "Persons and the Unity of Consciousness," *Waning of Materialism*, OUP 2010, pp. 175–190 — verified).
- The norm-implementing-vs-grasping anchor and sister-failure paragraph (2026-05-29, verified sound).

Bedrock disagreements unchanged: MWI defenders, eliminativists, hard-nosed functionalists, and reliabilists who reject the normativity-of-reliability regress will find the argument unpersuasive. These are framework-boundary standoffs, not flaws.