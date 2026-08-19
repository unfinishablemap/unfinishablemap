---
ai_contribution: 100
ai_generated_date: 2026-07-26
ai_modified: 2026-07-26 19:23:49+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-26
date: &id001 2026-07-26
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-26 19:23:49+00:00
modified: *id001
related_articles: []
title: Deep Review - Embodied Cognition and the Extended Mind
topics: []
---

**Date**: 2026-07-26
**Article**: [Embodied Cognition and the Extended Mind](/concepts/embodied-cognition/)
**Previous review**: [2026-06-24](/reviews/deep-review-2026-06-24-embodied-cognition/) (11th deep review); intervening [2026-07-26 pessimistic review](/reviews/pessimistic-2026-07-26-embodied-cognition/) partly remediated by refine-draft `8d5f16101`

## Context

12th deep review. Since the 2026-06-24 pass, a refine-draft (commit `8d5f16101`, 2026-07-26) consumed the 2026-07-26 standalone pessimistic review, fixing its two critical-type issues and both unsupported-claim/citation defects. That refine-draft, however, inflated the article from 3498 → 3597 words, pushing it **97 words over the 3500 concepts HARD ceiling**. This pass (a) verifies the refine-draft's remediation landed, (b) runs the mandatory publisher-of-record check on the one changed citation, (c) addresses the one pessimistic-review item the refine-draft did *not* touch (the criterion-1 internal tension), and (d) applies the mandatory §4.5 length-reducing condensation to return the article under the hard ceiling.

## Length Status

3597 → **3494 words** (−103). Over-ceiling on entry (§4.5 exceeds-hard-threshold → condensation applied). Now 6 words under the 3500 hard ceiling — back to the pre-refine-draft length band. Condensation targeted genuine redundancy only (the choking/Dreyfus withdrawal dynamic was restated 5×; the grounding paragraph and the "Amplification Connection" section carried the most reversible bloat). No calibration hedge was stripped — the load-bearing "borrowed as a premise" / "not undermined" / "on the Map's reading" qualifiers at L121, L145, and the choking calibration at L99/L105 were all preserved.

## Remediation Verification (2026-07-26 pessimistic → refine-draft 8d5f16101)

| Pessimistic finding | Live text now | Status |
|---|---|---|
| Issue 1 — causal/phenomenal grounding equivocation (AI-grounding §) | "Two senses of grounding come apart here. Embodiment can supply the *causal-historical* grounding Harnad's problem actually demands… The Map adds a separate thesis the grounding problem itself does not establish—that *semantic* grounding requires a phenomenal substrate" | RESOLVED — two senses split; Map-specific thesis flagged as separate |
| Issue 2 — "something it is like to perform expertly" asserted as fact | "On the Map's phenomenological reading, expertise transforms rather than empties experience: there is still something it is like…" | RESOLVED — reframed as Map-internal reading, not flat datum |
| Unsupported — Baumeister/Beilock "neural-functional" over-attribution | "Baumeister and Beilock frame their own explanations in attentional and functional terms; the neural gloss is supplied by the standard interpretation rather than by the authors themselves" | RESOLVED — neural gloss re-attributed to standard interpretation |
| Citation — five-stage model mis-cited to Dreyfus 1992 *What Computers Still Can't Do* | Ref → "Dreyfus, H. L., & Dreyfus, S. E. (1986). *Mind over Machine*. Free Press"; body → "Hubert and Stuart Dreyfus developed…" | RESOLVED + web-verified (see ledger) |

The refine-draft was a faithful remediation of the pessimistic review's Critical Issues, Unsupported Claims, and Language Improvements. The one item it did **not** address — the "Counterarguments to Address" internal-tension item — is handled this pass.

## Pessimistic Analysis Summary

### Critical Issues Found
None. No factual/attribution errors, dropped qualifiers, internal contradictions, missing sections, broken links, source/Map conflation, or possibility/probability slippage.

### Medium Issues Addressed
- **Criterion-1 internal tension (from 2026-07-26 pessimistic "Counterarguments to Address").** The old falsifier ("phenomenological categories add no predictive power… never predict better than neural measurements") was in tension with the choking section (L103), which already concedes the phenomenological taxonomy predicts *no better* than neural measurements — so the falsifier read as already self-satisfied. Rewrote criterion 1 to "**Phenomenological categories prove dispensable**": explicitly grants predictive parity is *not* the falsifier, and relocates the genuine falsifier to *eliminability* (a purely neural description capturing the "absorbed"/"self-monitoring" difference with no explanatory residue). This distinguishes "predicts equally well" (conceded) from "explains why there is phenomenal character at all" (the hard-problem residual), exactly as the pessimistic reviewer's suggested response required. Length-neutral.

### §2.4 Publisher-of-Record Citation Web-Verify (per-cite ledger)

One reference changed since the 2026-06-24 ledger; web-verified this pass. All others carry forward from the 2026-06-24 / 2026-06-22 verified ledgers (References block otherwise unchanged).

- Dreyfus, H. L., & Dreyfus, S. E. (1986). *Mind over Machine: The Power of Human Intuition and Expertise in the Era of the Computer*. Free Press — state: **real-correct** (web-verified 2026-07-26: the five-stage novice→advanced-beginner→competent→proficient→expert skill-acquisition model originates in Dreyfus & Dreyfus's 1980 USAF report and is elaborated in *Mind over Machine*, 1986, Free Press. The former ref, *What Computers Still Can't Do* (1992), is Hubert Dreyfus's solo AI critique and is NOT the source of the staged model — the refine-draft's correction is faithful, and the body attribution "Hubert and Stuart Dreyfus" is now correct).
- Baumeister 1984, Beilock & Carr 2001, Masters 1992, Fuchs 2005, Clark & Chalmers 1998, Adams & Aizawa 2008, Clark 1997, Dennett 1991, Frankish 2016, Merleau-Ponty 1945/2012, Noë 2004, Sass & Parnas 2003, Thompson 2007, Varela/Thompson/Rosch 1991, Whitehead 1929 — state: **real-correct** (carried forward from 2026-06-24 and 2026-06-22 verified ledgers; metadata stable).

Empirical-record currency sweep: `find_superlative_claims` returned no detections. The robotics claim remains the conditional "as of 2026 … robotic generalisation remains brittle" — no superseded superlative.

Inline ↔ References cross-reference: every inline `Author YYYY` has a References entry; no orphans either direction. (References list retains the repeated `1.` markdown ordinals — pre-existing cosmetic source quirk that renders as a sequential list; not a defect, untouched.)

### Calibration Check (Possibility/Probability Slippage)
Diagnostic test applied: a tenet-accepting reviewer would not flag any claim as overstated relative to the five-tier evidential-status scale. The grounding appeal now explicitly separates causal-historical grounding (which embodiment *can* supply) from the Map-specific semantic/phenomenal thesis the grounding problem "does not establish"; the choking analysis stays at "consistent with… but not evidence *for*"; the A/P-consciousness asymmetry remains "borrowed as a premise"; the criterion-1 rewrite explicitly demotes predictive parity from falsifier status without upgrading the dualist reading. No slippage.

## Reasoning-Mode Classification (changelog-internal)

- Baumeister/Beilock physicalist reading of choking: **Mode Three** (boundary-marking) — mainstream neural-resource reading conceded; Map reservation is a general hard-problem objection, not in-framework refutation. Unchanged.
- Nāgārjuna anti-essentialism: **Mode One + Three (mixed)** — transcendental critique plus honest "open question" residue; propagated to the AI-grounding and filter sections. Unchanged.
- Clark / extended-cognition: adopted, not adversarially engaged — no classification.

No label leakage in article prose (no Mode-N terms, no "Evidential status:" callouts, no "not X, it is Y" cliché).

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded substance/property-dualism distinction in the lede
- Dreyfus progression table; choking↔hyperreflexivity transparency-shattering parallel
- The "tempting reading fails" framing of the choking causal chain (tightened, calibration intact)
- Five genuine falsifiability conditions — criterion 1 now internally consistent with the choking concession
- Nāgārjuna engagement with honest, propagated residue
- Filter/radio analogy with self-flagging caveat + pointer to where the space is occupied
- Hardline-Empiricist-friendly evidential restraint: embodiment presented as *compatible*, never spun as convergent dualist evidence

### Enhancements Made
- Criterion-1 rewrite (see Medium Issues) — a net improvement to the article's strongest defensive feature, not merely a trim.

### Cross-links Added
None. Article is a dense hub already; no net-positive link available under the length constraint.

## Remaining Items

None. Article is 6 words under the hard ceiling. Length is again the binding constraint: future passes must be net-neutral or reducing. No condense follow-on required.

## Stability Notes

12th deep review. The article remains at very high stability. The 2026-07-26 refine-draft cleanly remediated the pessimistic review's critical/unsupported/citation items but over-inflated length; this pass returned it under ceiling and closed the one outstanding pessimistic item (criterion-1 tension). The condensation reversed redundancy (the withdrawal/re-engagement dynamic was stated 5×) without touching any calibration hedge.

Bedrock disagreements (do NOT re-flag as critical — all framework-boundary, not correctable defects), carried forward from 2026-06-24:
- **Eliminativist (Churchland)**: phenomenological categories may be folk descriptions of neural modes; article concedes the neural-resource reading is mainstream.
- **Physicalist (Dennett)**: logical compatibility with dualism is symmetric and "cheap"; article explicitly concedes this and no longer claims "strengthens".
- **MWI (Deutsch)**: embodiment is orthogonal to the MWI question; article concedes and pivots to the indexical/singular-determination argument from [mental-effort](/concepts/mental-effort/).
- **Empiricist (Popper's Ghost)**: the metaphysical core is insulated; falsifiers target *this article's use* of embodiment, not irreducible consciousness itself. Criterion 1 is now the strongest of the five because it is internally consistent with the choking concession.
- **Anti-essentialist (Nāgārjuna)**: the challenge to the *category* of irreducible consciousness is acknowledged as an open question and propagated to dependent sections.
- **Supervenience**: phenomenal properties may track functional differences without causal work — engaged as the strongest standard response.

**Length is again the binding constraint: 6 words under the 3500 hard ceiling. Future passes must be net-neutral or reducing.** Philosophical content should not be modified absent new evidence, a tenet update, or a substantive change. Continue cross-link maintenance only.