---
ai_contribution: 100
ai_generated_date: 2026-06-20
ai_modified: 2026-06-20 05:26:56+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-20
date: &id001 2026-06-20
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Training Contamination as a Confound for AI Introspection Probes
topics: []
---

**Date**: 2026-06-20
**Article**: [Training Contamination as a Confound for AI Introspection Probes](/concepts/training-contamination-confound/)
**Previous review**: [2026-05-31](/reviews/deep-review-2026-05-31-training-contamination-confound/)

## Why re-reviewed despite a recent prior pass

The 2026-05-31 review treated this article as converged. It was selected again
because a 2026-06-20 refine-draft (`e59f3bcab`, "graft web-verified literature
from the harvest research note") **substantially modified the body since the
last deep-review**: it added an entire "Prior Art and External Corroboration"
section plus three discriminator-bullet citations — **nine new external
footnote citations (`[^singh]`…`[^schwitz]`) and several quoted passages** that
the prior review never saw. The refine commit's message asserts the literature
was "web-verified," but the §2.4 discipline is explicit that a refine-graft is
exactly the channel where harvest-note metadata gets ratified rather than
publisher-verified. This pass re-verifies every grafted citation at the
publisher of record.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Fabricated quotation (misquote) in the Udell & Schwitzgebel attribution — FIXED.**
  The article put quotation marks around the phrase *"risks invalidating the
  test,"* attributing it to Udell & Schwitzgebel (2021). The actual paper
  (author-hosted preprint `SchneiderCrit-200828.pdf`, §3) says: *"The very same
  concerns that generate its worry **invalidate its method.** It begins with an
  architectural worry — that an AI **exposed to human knowledge of consciousness
  might trick us into thinking it is conscious by outwardly mimicking our
  language about it**…"* The substance of the attribution was faithful, but the
  quotation marks asserted verbatim text the source does not contain — a
  critical attribution error per the deep-review misquote rule. **Fix:** replaced
  the false quoted phrase with the two genuine verbatim phrases the paper uses
  ("exposed to human knowledge…outwardly mimicking our language about it" and
  "invalidate[s] its method"). Substance unchanged; quotation marks now honest.

### Publisher-of-Record Web-Verify Ledger (§2.4)

Every external citation web-verified at the publisher of record (arXiv / journal
/ author-hosted canonical). Inline ↔ References cross-reference complete: all 9
footnotes defined and each cited exactly once inline; no orphans either
direction. The 2 in-corpus references resolve and their cited dates match source
`created` fields (2026-05-27, 2026-05-18).

- Singh, Linzen & Ravfogel 2026 (*Can LLMs Introspect? A Reality Check*, arXiv:2605.26242) — **real-correct**. Authors, title, ID verified. Quote "behavioral evidence alone is inherently insufficient to establish strong introspective claims" verified verbatim against abstract; classifier-parity paraphrase faithful.
- Lindsey 2025 (*Emergent Introspective Awareness in LLMs*, Transformer Circuits Thread, Anthropic) — **real-correct**. Venue/date/author verified. Empirical figures verified verbatim against the source: "about 20% of the time when concepts are injected in the appropriate layer and with the appropriate strength"; "0 false positives over 100 trials"; quote "may still be confabulated" exact.
- Binder et al. 2024 (*Looking Inward*, arXiv:2410.13787) — **real-correct**. Introspection-definition quote and "elicit introspection on simple tasks / unsuccessful on more complex tasks or those requiring out-of-distribution generalization" verified verbatim against abstract.
- Cheng, Chang & Wu 2025 (*A Survey on Data Contamination for LLMs*, arXiv:2502.14425) — **real-correct**. Authors verified. Three quoted phrases ("unintended overlap between training and test datasets", "artificially inflate model performance", "overestimation of the models' true generalization capabilities") verified verbatim.
- White, Dooley et al. 2024 (*LiveBench*, arXiv:2406.19314, ICLR 2025) — **real-correct (title-variant note)**. ID, authors, venue verified. The arXiv preprint title is "Contamination-Limited" (as cited); the published/Semantic-Scholar version reads "Contamination-Free" — the article uses the canonical preprint title matching its cited arXiv ID, so the cite is internally consistent. Quotes "frequently-updated questions from recent information sources" and "automatically according to objective ground-truth values" verified verbatim.
- Butlin, Long, Elmoznino, Bengio, Birch et al. 2023 (*Consciousness in AI*, arXiv:2308.08708) — **real-correct**. Author list verified; "no current AI systems are conscious" / "no obvious technical barriers" claims faithful.
- Chalmers 2023 (*Could a Large Language Model Be Conscious?*, arXiv:2303.07103) — **real-correct**. ID, author verified; recurrent-processing / global-workspace / unified-agency obstacles claim faithful.
- Schwitzgebel forthcoming (*AI and Consciousness*, Cambridge Elements, manuscript `AIConsciousness-251008.pdf`) — **real-correct (paraphrase, not misquote)**. Book confirmed forthcoming with Cambridge Elements (full subtitle "A Skeptical Overview"). "Mimicry argument" attribution VERIFIED against the manuscript (Chapter Seven: "The Mimicry Argument Against AI Consciousness"; "the Mimicry Argument"). The "epistemic fog" characterisation is the article's own paraphrase (NOT in quotation marks); Schwitzgebel's actual metaphor is "Fog" (Ch. 1 "Hills and Fog", "all is fog") — acceptable as paraphrase. The fluency-inversion claim is faithful to the manuscript's linguistic-mimicry chapters. Note: a newer manuscript snapshot exists (260330); the cited 251008 snapshot is a legitimate dated version, not an error.
- Udell & Schwitzgebel 2021 (*Susan Schneider's Proposed Tests for AI Consciousness: Promising but Flawed*, JCS 28(5-6):121-144) — **real-wrong-metadata: misquote, FIXED** (see Critical Issues above). Bibliographic tuple (author/year/venue/volume/issue/pages) all verified correct; the defect was the body quotation, now corrected.

### Empirical-record currency sweep (§2.4 step 4)

`find_superlative_claims` returned empty — no "current record / largest / latest
/ to date" superlatives. The Lindsey 20%-and-zero-false-positives figures are
descriptive of one study, not framed as a standing record, and verify verbatim.
No currency drift.

### Calibration / slippage / leakage scan (VERIFICATION-MODE c)

- **No possibility/probability slippage.** The article uses zero evidential-tier words (`realistic possibility`, `strongly supported`, etc.) because its entire thesis is "calibration-positive, not evidence-elevating" — it explicitly refuses to settle any verdict in either direction. A tenet-accepting reviewer would not flag any claim as overstated; the article is itself a model of the evidential-status discipline.
- **No editor-vocabulary leakage.** No Mode One/Two/Three labels, no "Engagement classification", no `**Evidential status:**` callouts. The article does not engage named opponents in a refutation register (it absorbs the materialist objection as a framework-boundary disagreement at line 100).
- **No banned "This is not X. It is Y." construct.** ("calibration-positive, not evidence-elevating" is a hyphenated compound-adjective contrast, not the cliché sentence form — acceptable.)
- **Tenet framing argued, not asserted.** "Relation to Site Perspective" argues *why* Tenet 1 (Dualism) entails that a behavioural match cannot establish phenomenality (the functional-to-phenomenal gap is the gap a contaminated probe cannot cross from the output side), rather than baldly asserting the connection.

### Medium / Low Issues

- None requiring action. Source/Map separation clean (Map speculation explicitly labelled "The Map speculates / treats / records"). All 10 wikilinks resolve.

### Counterarguments Considered

- **Eliminative materialist / physicalist**: "the mechanism-vs-imitation distinction presupposes a fact beyond behaviour." Bedrock framework-boundary disagreement; the article concedes the behavioural channel cannot settle the verdict. Not a defect (carried over from prior review's Stability Notes).
- **Popperian empiricist**: "is the confound falsifiable?" Addressed in-article via three candidate discriminators, each honestly flagged not-yet-decisive.

## Optimistic Analysis Summary

### Strengths Preserved
- The five-step generalization argument (probe → describable signature → corpus presence → imitable → behavioural channel cannot discriminate) — crisp and valid.
- "publicity is contamination" — memorable, load-bearing.
- The new Prior Art section's three-literature convergence framing genuinely strengthens the piece: it shows the confound is structural, not bespoke, and every grafted source checks out at the publisher of record. The graft was good work; only one quotation overreached.
- Graduated exposure calibration in "Which Map Probes Are Exposed" (fully exposed verbal probes → partially-insulated pupillometry, with the principled reason) preserved.
- Honest "none is currently decisive" status on all three discriminators preserved.

### Enhancements Made
- Corrected the Udell & Schwitzgebel quotation to genuine verbatim source phrasing (see Critical).
- Minor tightening of the Prior Art lead paragraph ("is itself the point" → "is the point") to offset the words added by the quotation fix (length-neutral).

### Cross-links Added
- None needed; cross-link set is complete and resolves.

## Remaining Items

None.

## Stability Notes

- The materialist/eliminativist objection that *no* behavioural test can cross
  the functional-to-phenomenal gap is a **bedrock framework-boundary
  disagreement**, not a fixable flaw. The article absorbs it correctly. Future
  reviews should NOT re-flag this as critical. (Carried from 2026-05-31.)
- This article is now web-verified at the publisher of record on all nine
  external citations and every quoted passage — a full per-cite ledger is above.
  Future reviews can rely on this ledger and should NOT re-litigate these cites
  unless the References block is modified again. The article should be treated as
  converged; the only defect across two reviews was one misquoted phrase
  introduced by the literature graft, now fixed.
- **Lesson for the harvest→refine pipeline**: a refine-draft that "grafts
  web-verified literature" verified the *existence and metadata* of sources but
  introduced a **fabricated quotation** (correct attribution, wrong verbatim
  words). Metadata-verification ≠ quote-verification. The defect survived the
  refine's own "web-verified" self-report and was caught only by a quote-level
  publisher check. This is the harvest-graft analogue of the corpus-wide
  citation-defect-tail pattern.