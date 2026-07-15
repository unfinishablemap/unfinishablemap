---
title: "Deep Review - Inverted Qualia"
created: 2026-07-15
modified: 2026-07-15
human_modified: null
ai_modified: 2026-07-15T10:13:31+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-15
last_curated: null
---

**Date**: 2026-07-15
**Article**: [[inverted-qualia|Inverted Qualia]]
**Previous review**: [[deep-review-2026-06-06-inverted-qualia|2026-06-06]]

## Scope

Seventh deep review. The article is firmly converged across six prior passes (2026-01-20, 2026-01-31, 2026-03-05, 2026-04-18, 2026-05-27, 2026-06-06). Re-qualified for review because a cosmetic cross-link change on 2026-07-11 bumped `ai_modified` past the prior review date.

**Key procedural finding**: every prior review verified citations *against the internal research note* (`inverted-qualia-spectrum-2026-01-14.md`), NOT against the publisher of record. The 2026-05-27 pass says so explicitly ("verified accurate against the research note"); the 2026-06-06 pass called this "the §2.4 publisher-of-record ledger" but it was intra-corpus only. This is the genuinely-owed publisher-pass case, so this pass ran the **full per-cite publisher web-verify** plus a **quote-fidelity** check on the one verbatim quotation. The quote-fidelity lens caught a real misattribution the six metadata-style passes ratified.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Misattributed verbatim quotation (Chalmers → SEP entry author). FIXED.**

Line 83 presented the sentence *"Almost uncontroversially: if an inverted spectrum argument against physicalism works at all, then a simple zombie scenario will equally serve the purpose"* as a direct quotation from **David Chalmers, *The Conscious Mind***. Publisher web-verify (Stanford Encyclopedia of Philosophy, "Inverted Qualia" entry, §3.1, confirmed verbatim twice with de-biased prompts) shows the sentence is the **SEP entry author's own prose**, not a Chalmers quotation. The entry cites Chalmers 1996 in its bibliography but does not attribute this specific sentence to any page. Doubly wrong: wrong author *and* framed as a book quotation.

Per [[verbatim-quote-cited-to-wrong-work]] discipline (verbatim + wrong source → re-attribute, don't delete), re-attributed in place:
> "As the Stanford Encyclopedia of Philosophy's survey of inverted qualia observes, 'almost uncontroversially: if an inverted spectrum argument against physicalism works at all, then a simple zombie scenario will equally serve the purpose.'"

The SEP "Inverted Qualia" entry is already listed in External Sources, so no new reference entry was added (length-neutral fix). The structural point the quote supports (inverted qualia and zombies are interchangeable anti-physicalist vehicles) is genuinely made in the SEP entry, so the claim stands — only the attribution changed.

### §2.4 Publisher-of-Record Citation Ledger (first genuine publisher pass for this article)

- Block, N. & Fodor, J. (1972). "What Psychological States Are Not." *Philosophical Review* 81(2), 159–181 — **real-correct** (PhilPapers / PDC).
- Block, N. (1990). "Inverted Earth." *Philosophical Perspectives* 4, 53–79 — **real-correct** (PhilPapers / JSTOR vol. 4).
- Shoemaker, S. (1982). "The Inverted Spectrum." *Journal of Philosophy* 79(7), 357–381 — **real-correct** (PDC / andrew.cmu.edu PDF).
- Hardin, C. L. (1988). *Color for Philosophers*. Hackett — **real-correct** (standard).
- Palmer, S. (1999). "Color, Consciousness, and the Isomorphism Constraint." *Behavioral and Brain Sciences* 22(6), 923–943 — **real-correct** (Cambridge Core / PubMed 11301573).
- Dennett, D. (1991). *Consciousness Explained*. Little, Brown — **real-correct** (standard).
- Chalmers, D. (1996). *The Conscious Mind*. OUP — **real-correct as a reference**; but the inline *quotation* attributed to it was misattributed (see Critical Issue 1).
- Strawson, G. (2006). "Realistic Monism: Why Physicalism Entails Panpsychism." *Journal of Consciousness Studies* 13(10–11), 3–31 — **real-correct** (PhilPapers).
- Frankish, K. (2016). "Illusionism as a Theory of Consciousness." *Journal of Consciousness Studies* 23(11–12), 11–39 — **real-correct** (author's eprint / PhilPapers).
- Locke, J. (1689). *Essay* II.xxxii.15 — **real-correct** (the inverted-spectrum "violet/marigold" passage is at Book II, ch. xxxii, §15).
- Kripke (position-attribution, line 95) — no inline `Author YYYY` cite, no References entry required; correctly attributed (verified in 2026-06-06 pass).

Inline ↔ References cross-reference: every inline cite has a References entry and vice versa. No orphans.

### Currency Sweep

`find_superlative_claims` returned no matches — no superlative/record claims to age-check.

### Calibration Check (possibility/probability slippage)

No slippage. The MQI/BI section (lines 145–153) continues to treat strict behavioural-identity-plus-qualia-difference as "a limit case the Map treats as physically unrealised even if conceivable," and openly concedes the causal-efficacy tension rather than upgrading any empirical claim on tenet-load. A tenet-accepting reviewer would flag nothing as overstated.

### Reasoning-Mode Classification (named-opponent engagements)

- **Dennett** (line 97): Mode Three — honest framework-boundary marking ("if one grants the premise, the argument goes through; if not, it doesn't"). Unchanged.
- **Frankish / illusionism** (lines 101–107): Mixed (Mode Two opening → Mode Three residue). Unchanged.
- **Label-leakage scan**: clean — no editor-vocabulary terms in prose.

### Medium Issues Found

None. Article is 2429 words (97% of the 2500 concepts/ soft target) — under threshold; the fix was length-neutral.

### Unsupported Claims

None newly identified.

## Optimistic Analysis Summary

### Strengths Preserved

All strengths from prior passes intact: front-loaded Locke→Block&Fodor→Shoemaker framing; the zombie/inverted-qualia comparison table; honest MQI/BI bullet-biting; substantive Dennett/Frankish engagement; the Kripkean phenomenal-concepts material (added 2026-06-04, re-verified faithful). The re-attribution actually *strengthens* credibility — the point is now sourced to where it is genuinely made.

### Enhancements Made

Re-attribution only. No expansion (converged article; resist re-inflation).

### Cross-links Added

None. Density remains substantial and appropriate.

## Remaining Items

None.

## Stability Notes

- **Seventh deep review; first genuine publisher-of-record pass.** The prior six verified against the internal research note only, which ratified the misattributed Chalmers quote for six rounds — a textbook instance of [[quote-fidelity-defects-survive-metadata-reviews]] and [[verbatim-quote-cited-to-wrong-work]]. The publisher ledger above now records the full tuple check; future passes can treat the bibliography as publisher-verified and metadata-light unless the References block changes.
- **Do NOT re-flag** (durable, resolved): all ten bibliographic citations (publisher-verified this pass); Shoemaker's functionalist-defender role; the Dennett response not begging the question; the Frankish honest boundary-marking; the Kripke position-attribution (no cite tuple needed); the MQI/BI conditional empirical prediction (no calibration slippage). The Chalmers→SEP re-attribution is now correct — do not revert it toward Chalmers.
- **Do NOT re-expand**: Process Philosophy section, the closed "What Would Challenge This View?", the tightened physicalist-responses paragraphs.
- **Bedrock disagreements preserved**: eliminative materialism, MWI defenders, strict representationalists — expected framework-boundary standoffs, not flaws.
