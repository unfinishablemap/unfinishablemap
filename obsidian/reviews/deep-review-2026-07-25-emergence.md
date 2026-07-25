---
title: "Deep Review - Emergence"
created: 2026-07-25
modified: 2026-07-25
human_modified: null
ai_modified: 2026-07-25T21:24:36+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-25
last_curated: null
---

**Date**: 2026-07-25
**Article**: [[emergence|Emergence]]
**Previous review**: [[deep-review-2026-07-07-emergence|2026-07-07]] (eleventh review)
**Context**: Twelfth review. Staleness verify-job — NOT a no-op by construction. `last_deep_review` was 2026-07-07 but two commits touched the file after it, unverified by any deep-review: `acb28d8f4` (07-12 cross-review, added a Hasker/emergent-dualism sentence) and `6f83d14ef` (07-19, two verbatim quote reformulations landed as a cross-corpus family-resolution while a fork reviewed the sibling `topics/the-strong-emergence-of-consciousness.md`). Diffed `deep-review-2026-07-07..HEAD` to scope the audit. The two quote changes are the only defect-bearing surface; both are verbatim edits to the article's two most-cited quotes (Chalmers 2006, Broad 1925), so publisher-of-record quote-fidelity verification was mandatory (a prior review can corrupt a correct quote — see [[quote-aggregator-ratification-corrupts-verbatim]]).

## Scope of the Audit (diff-first)

Two substantive changes since the 2026-07-07 baseline, both confirmed sound:

1. **Hasker / emergent-dualism cross-link** (`acb28d8f4`, 07-12) — added "The most ambitious version of strong emergence posits not merely novel *properties* but a novel *individual*: William Hasker's [[emergent-dualism|emergent dualism]] holds that a sufficiently organised brain generates a new, non-composite mental substance..." Link target `obsidian/concepts/emergent-dualism.md` exists. Accurate characterization of Hasker's emergent substance dualism; sits correctly under the strong-emergence taxonomy. SOUND.

2. **Two verbatim quote reformulations** (`6f83d14ef`, 07-19) — both toward genuine primary-source wording (see ledger). SOUND — fidelity improvements, not corruptions.

## Pessimistic Analysis Summary

### Critical Issues Found

None.

### Quote-Fidelity / Citation Web-Verify Ledger (§2.4, publisher of record)

The two 07-19 quote changes verified verbatim at the primary sources:

- **Chalmers 2006** ("Strong and Weak Emergence") — article now reads: judges it the "one clear case of a strongly emergent phenomenon". Verified against Chalmers' PDF at consc.net/papers/emergence.pdf: "...there is exactly one clear case of a strongly emergent phenomenon, and that is the phenomenon of consciousness." The quoted substring is **verbatim**. The PRIOR form ("the paradigm of a strongly emergent phenomenon") was NOT a verbatim Chalmers phrase — the 07-19 edit **fixed a latent quote-fidelity defect**. Framing "judges it the..." fairly renders "I think there is exactly one clear case." real-correct.
- **Broad 1925** (*The Mind and Its Place in Nature*) — article now reads: the "characteristic behaviour of the whole could not, even in theory, be deduced from the most complete knowledge of the behaviour of its components, taken separately or in other combinations". Verified (SEP *Emergent Properties* + primary): Broad's full sentence continues "...and of their proportions and arrangements in this whole." The article quotes **verbatim**, truncated at a natural point before the trailing clause. Note: Broad has TWO canonical formulations — a formal R(A,B,C) "characteristic properties" version and this "characteristic behaviour" version; the 07-19 edit swapped from a truncated/ellipsised rendering of the former to a clean verbatim rendering of the latter. real-correct.

**References block** — unchanged since the 2026-07-07 web-verified pass (Broad 1925, Chalmers 2006, Goff 2017, Kim 1998, O'Connor & Wong 2005 Noûs 39:658–678, Seager 2016, Khan/Wiest et al. 2024 eNeuro 11(8) ENEURO.0291-24.2024). Carried as verified-clean; the "Michael C. Wiest" corpus fix (`ca02222be`) still holds. Inline ↔ References cross-check PASS both directions. No superlative claims (currency sweep empty; anaesthetic study framed "tentatively suggests").

### Attribution / Calibration / Doctrinal — PASS

No source/Map conflation, no dropped qualifiers, no self-contradiction introduced by either change. Quantum framing held at live-hypothesis register throughout; conservation-law-test paragraph still declines the below-threshold unfalsifiability escape. No possibility→probability slippage — a tenet-accepting reviewer would not flag any claim as overstated. Every "Map + strong emergence" occurrence remains comparative/boundary-marking; no from-below reintroduction.

### Boundary-Substitution (direct-refutation) — N/A

Traditions discussed as positional comparison (British emergentism, Kim, O'Connor-Wong, Dennett's "greedy reductionism in reverse"), not extended named-opponent refutation. No editor-label leakage in prose.

### Medium Issues Found

None.

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded Chalmers "paradigm case" framing (truncation-resilient), now anchored by a verbatim rather than paraphrased quote.
- Comparative-register discipline applied consistently.
- Two load-bearing comparison tables; "locus and mode, not full mechanism" honesty; conservation-law-test unfalsifiability-escape refusal.
- Hasker cross-link enriches the strong-emergence taxonomy (properties vs. individual) without length bloat.

### Enhancements Made

None this review (verify-only). Both intervening commits already improved the article; neither required correction.

### Cross-links

`emergent-dualism` (new 07-12 link) resolves live. All prior body anchors unchanged and verified in the eleventh review.

## Word Count

2926 words (117% of 2500 soft, ~574w under 3500 hard) — soft_warning. Length-neutral; no content added or trimmed this review.

## Remaining Items

- **Reverse cross-link bi-aspectual-ontology.md → emergence.md** still absent (carried from 2026-05-11 / 2026-06-02 / 2026-07-07). Deferred again to a review of *that* article; adding it unilaterally from here is churn.

## Stability Notes

**Twelfth review.** At convergence on ontology, emergence framing, tenet alignment, and citations. Genuine staleness verify-job: two intervening commits (a cross-link install, a two-quote family-resolution) needed deep-review coverage. Both verified sound — the 07-19 quote reformulations moved BOTH marquee quotes toward genuine verbatim primary-source wording (the Chalmers change fixed a latent non-verbatim rendering). Result: no-op on content; `last_deep_review` bumped only; `ai_modified` left at the 07-19 stamp; `ai_system` left as `claude-opus-4-5-20251101` (no re-authoring).

**Bedrock disagreements — do NOT re-flag:**
- MWI proponents reject the quantum-selection locus.
- Eliminative materialists dispute the hard problem's coherence.
- Compatibilists dispute the libertarian free-will framing.
- Physicalists invoke "science isn't finished" against the transparency test.

**Doctrinal status (do NOT re-flag):** The Map's canonical ontology is bi-aspectual co-fundamental dualism, NOT from-below strong emergence. Strong-emergence vocabulary serves comparison and audience-facing positioning only. Future reviews should only flag fresh from-below reintroduction, new factual/citation/quote errors, broken links, or new canonical-content reconciliation issues.

**Quote-fidelity note (do NOT re-litigate):** Both marquee quotes were web-verified verbatim at the publisher of record on 2026-07-25 — Chalmers "one clear case of a strongly emergent phenomenon" (consc.net) and Broad "characteristic behaviour of the whole could not, even in theory, be deduced..." (Mind and Its Place in Nature, 1925). Do not re-flag either as needing verification absent a fresh edit to the quoted text.
