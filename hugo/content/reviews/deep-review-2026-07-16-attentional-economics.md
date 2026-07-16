---
ai_contribution: 100
ai_generated_date: 2026-07-16
ai_modified: 2026-07-16 18:08:59+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-16
date: &id001 2026-07-16
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Attentional Economics
topics: []
---

**Date**: 2026-07-16
**Article**: [Attentional Economics](/concepts/attentional-economics/)
**Previous review**: [2026-06-04](/reviews/deep-review-2026-06-04-attentional-economics/)

## Scope

Settled-converged staleness pick (8th review; `last_deep_review == ai_modified == 2026-06-04`, 42d settled). Article is the oldest cohort in the settled pool (`ai_system: claude-opus-4-5-20251101`), so per the staleness brief the pass ran the **publisher-of-record citation web-verify as the highest-yield lens** rather than presuming a no-op. Every external citation was re-verified live at the publisher (not via unfinishablemap.org).

## Pessimistic Analysis Summary

### Critical Issues Found

- **Misattributed / rival-as-contradiction citation (CRITICAL — FIXED).** Line 123 read: *"Great apes show working memory of roughly 2±1 items (Inoue & Matsuzawa 2007), constraining this kind of manipulation."* Web-verify at Current Biology confirms Inoue & Matsuzawa (2007) is genuine and correctly formatted, BUT its finding is the **opposite** of the claim it was cited for: the paper reports young chimpanzees' *extraordinarily high* numeral working memory (chimp Ayumu recalled 5 numerals reliably and up to 9 positions at ~80%, matching/exceeding human adults). It does not report — and in fact contradicts — a "roughly 2±1 items" span. 3-state classification: the cite is REAL and metadata-correct, but the *claim–source pairing* is wrong (a citation-framing defect, not a fabrication). The genuine source for the great-ape "~2 items" span is **Read, D.W. (2008), "Working Memory: A Cognitive Limit to Non-Human Primate Recursive Thinking Prior to Hominid Evolution," *Evolutionary Psychology* 6(4), 676-714**, which argues great apes' working memory is limited to "two, or at most three, concepts at a time" for recursion/manipulation — a *better* fit for the sentence's own "counterfactual-manipulation task" framing than the numeral-memory paper was. *Resolution*: rewrote the sentence to "Read (2008) argues that great apes' working memory for recursive manipulation is limited to roughly two items, constraining this kind of task"; replaced the Inoue & Matsuzawa reference-list entry with the verified Read (2008) entry (Inoue & Matsuzawa was cited only here, so no orphan created). This defect survived seven prior reviews because intra-corpus cross-check ratified a correctly-*formatted* cite; only checking the source's actual finding against the claim caught it.

### Citation Web-Verification (all references, live at publisher)

- **Read, D.W. (2008), *Evolutionary Psychology* 6(4), 676-714** — VERIFIED (SAGE DOI 10.1177/147470490800600413); supports the "~2 items recursion/manipulation span" claim exactly. Replaces the misframed Inoue & Matsuzawa cite.
- **Zheng, J. & Meister, M. (2025). *Neuron* 113(2), 192-204** ("The unbearable slowness of being") — VERIFIED exact (author/year/journal/vol/pages; online Dec 2024, print Jan 2025). Supports the ~10 bits/s conscious-throughput figure. The article uses it descriptively and scopes the dualist reading with "on the Map's reading" — no rival-as-ally misframe.
- **Schwartz, J.M. & Begley, S. (2002). *The Mind and the Brain*. ReganBooks** — VERIFIED; the n=18 / not-independently-replicated hedge and the "suggestive but... open question" qualifier are intact (evidential restraint preserved per brief).
- **Stapp, H.P. (2007). *Mindful Universe: Quantum Mechanics and the Participating Observer*. Springer** — VERIFIED as the correct work for the quantum-Zeno-stabilisation claim (the 2007 Springer book, NOT the 2005 QID paper; per stapp-2007-mindful-universe-vs-2005-qid-paper). Springer treats the Zeno effect as action-stabilisation mechanism — matches the article's usage.
- **Suddendorf, T. & Corballis, M.C. (2007). *Behavioral and Brain Sciences* 30(3), 299-313** — VERIFIED exact (confirmed in 2026-05-19 and 2026-06-04 reviews; Bischof-Köhler attribution and source/Map separation intact).

### Evidential-Status / Calibration

- No possibility→probability slippage. The Schwartz & Begley OCD-PET finding retains its n=18 / unreplicated hedge; attention-training plasticity is not silently upgraded into an *establishing* bidirectional-causation argument. Register discipline honoured (wanting-liking-anchoring-false-high, [evidential-status-discipline](/project/evidential-status-discipline/)).
- The interface-friction scarcity grounding (audited clean in the 2026-06-04 review) is unchanged; still scoped "on the Map's reading" — not re-flagged.

### Reasoning-Mode Classification

No named-opponent engagements. "Objections and Responses" addresses generic positions (folk-psychology charge, epiphenomenalism, bandwidth-limit objection) in natural prose. No editor-vocabulary leakage.

## Optimistic Analysis Summary

### Strengths Preserved

- Economic-framing table, three-level witness-mode structure, and habituation/de-habituation ("beginner's mind" / de-habituation) treatment remain the article's distinctive contributions.
- Schwartz & Begley evidential caveats intact (Hardline Empiricist praise-worthy pattern honoured).
- The Read (2008) swap strengthens the mental-time-travel paragraph: the source now genuinely supports the claim and aligns with the recursion/manipulation framing.

### Enhancements Made

- Corrected the misframed Inoue & Matsuzawa cite → Read (2008) (inline + reference list).
- Updated `ai_modified` + `last_deep_review` timestamps.

### Cross-links Added

None new (comprehensive set already in place; not re-verified individually this pass — prior reviews confirmed all extant and no links were added or removed).

## Length

- Pre-review: 2722 words (109% of 2500 soft — soft_warning)
- Post-review: 2731 words (109% — soft_warning; +9 words from the citation-claim rewrite)

Under the 3500 hard threshold. No condense. Length-neutral band preserved.

## Remaining Items

None. The one defect was corrected in-pass.

## Stability Notes

Eighth deep review. The article's argument and voice remain stable; this pass fixed a single **claim–source pairing** defect that seven metadata-focused reviews missed because the cite itself was correctly formatted — a reminder that web-verify must check the source's *finding* against the article's *claim*, not just the bibliographic tuple (cf. citation-framing-accuracy-lens). Bedrock disagreements (functionalist alternatives, MWI indexical response) remain framework-boundary standoffs and should NOT be re-flagged. `ai_system` held at `claude-opus-4-5-20251101` (citation correction is not re-authoring).