---
ai_contribution: 100
ai_generated_date: 2026-09-27
ai_modified: 2026-09-27 10:05:13+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-09-27
date: &id001 2026-09-27
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-27 10:05:13+00:00
modified: *id001
related_articles: []
title: Deep Review - Composition and Consciousness
topics: []
---

**Date**: 2026-09-27
**Article**: [Composition and Consciousness](/concepts/composition-and-consciousness/)
**Previous review**: [2026-07-14](/reviews/deep-review-2026-07-14-composition-and-consciousness/) (also 2026-06-09, 2026-06-01)

## Context

Fourth deep review. Selected because this morning's refine-draft (commit 4c800633d1) changed the body. That pass fixed the consciousness-"agreement" overclaim, recast the Born-rule and bidirectional lines as compatibility, added the epistemic/metaphysical split and Roelofs, and replaced the fabricated James string. This review checked those fixes and re-ran the quote and citation verification from scratch. It did not trust the 2026-06-01 ledger, which covered metadata only.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Merricks quote comes from a reviewer (quote-fidelity)**: L61 quoted Merricks 2001 as saying consciousness "does not even globally supervene on microscopic physical properties". I could not find this string in any accessible text of *Objects and Persons* (Google Books search-within returned 404 and the API quota is at zero). It does occur verbatim in **Ted Sider's *Mind* review** of the book: "the property consciousness, instantiated by human persons, does not even globally supervene on microscopic physical properties … (chapter IV)" (tedsider.org/papers/Merricks_review_Mind.pdf). The 2026-04-05 research note's "Quote" is nearly word for word Sider's sentence, so the wording probably entered from the review. Earlier reviews certified it as "exact quote preserved" without checking the raw source. **Fixed**: removed the quotation marks and turned it into an attributed paraphrase ("fails even to globally supervene on the microphysical (Merricks 2001, ch. IV)"). The substance is Merricks's own; Sider confirms the chapter-IV conclusion. The same quoted string is still live in `topics/consciousness-and-the-metaphysics-of-composition` L61, `apex/mereology-of-mind` L61 and the archived `concepts/metaphysics-of-composition`. Queued as a P2 sweep task.
- **SCQ formulation presented as a verbatim quote (quote-fidelity)**: L49 quoted van Inwagen as "For any xs, is there a y such that the xs compose y?" Van Inwagen's own form is "When is it true that ∃y the xs compose y?" (*Material Beings* p. 30, as reproduced in the secondary literature). The quoted version also changed a *when*-question into a yes/no question. The string occurs only in this file. **Fixed**: replaced it with an unquoted paraphrase that keeps the *when* form.
- **Leftover calibration overclaim (internal contradiction)**: L55 said consciousness "provides a non-arbitrary boundary that multiple philosophers have independently identified". This repeats the "agreement" claim that the refine-draft retracted at L43 and L121, and it contradicts L61 (van Inwagen reaches life; McQueen and Tsuchiya decouple their criterion from consciousness). **Fixed**: now reads "several approach a non-arbitrary boundary in its neighbourhood by different argumentative routes."
- **Orphan reference**: Chalmers 2017 was in References but never cited in the body. **Fixed**: cited inline at the list of combination mechanisms, "(surveyed in Chalmers 2017)". That chapter is the standard survey of phenomenal bonding, co-consciousness and related proposals.

### §2.4 Publisher-of-Record Ledger
- Van Inwagen 1990 (*Material Beings*, Cornell UP): real-correct. SCQ quote de-quoted (see above).
- Merricks 2001 (*Objects and Persons*, OUP/Clarendon): real-correct metadata. Quoted string traced to Sider's review; de-quoted.
- McQueen & Tsuchiya 2023 (*Neuroscience of Consciousness* 2023(1), niad013): real-correct (2026-06-01 ledger; unchanged). Result direction: they decouple the composition criterion from consciousness, and the article says so.
- Coleman 2014 ("The Real Combination Problem", *Erkenntnis* 79, 19–44): real-correct. The dilemma is his; the extension to non-phenomenal parts is explicitly marked as the Map's.
- Chalmers 2017 (Brüntrup & Jaskolla eds., OUP): real-correct metadata. It was orphaned and is now cited. The year is subject to the open NEEDS-HUMAN 2016-vs-2017 decision in todo; not changed here.
- James 1890 (*Principles*, Holt): **verbatim-verified against Gutenberg #57628.** "shut in its own skin, windowless" (singular *its*, correct) and "hundred-and-first feeling" both occur once, in Ch. VI. The unquoted gloss "a new fact rather than a sum" matches James's "this 101st feeling would be a totally new fact". "mind-dust" occurs in Ch. VI. The fabricated "sum of feelings" string is gone (0 hits).
- Roelofs 2019 (*Combining Minds*, OUP): real-correct. Correctly described as taking the coexistence horn.
- Southgate & Oquatre-six 2026 self-cite: intentional Map self-citation. Left in place.
- Superlative/currency sweep: helper returned no claims.

### Cited-Author Stance
- Merricks: holds that humans are composites of physical parts (atoms arranged human-wise *plus* the human), with non-supervenient consciousness. He is not a substance dualist. **Fixed**: the Bidirectional paragraph now notes this and marks the step toward dualism as the Map's.
- Van Inwagen: materialist organicist. McQueen & Tsuchiya: explicitly decouple their criterion from consciousness. Both are correctly handled after the refine-draft.

### Reasoning-Mode Classification (editor-internal)
- Materialist turbulence/wetness analogy: Mode One (computational vs conceptual hardness, argued on the opponent's terms).
- Functionalist composition: Mixed Mode Two/Three (James's mind-dust point, now with verified wording).
- Panpsychist combination: Mode One via Coleman, with honest boundary-marking (the epistemic/metaphysical split and the Roelofs horn).
- No label leakage.

### Medium Issues
- None outstanding.

### Counterarguments Considered
- Split-brain/DID as subject division: now acknowledged as a debt the metaphysical reading owes (added by the refine-draft). Adequate.
- MWI and quantum-skeptic objections to the Born-rule line: now framed as downstream compatibility. No slippage.

## Optimistic Analysis Summary

### Strengths Preserved
- The distinction between computational and conceptual hardness.
- The symmetry of "compositional failure runs both ways", now correctly calibrated as epistemic.
- The Coleman dilemma plus the Roelofs horn, with the Map's generalisation explicitly flagged.
- The primer-to-topic division of labour.

### Enhancements Made
- Merricks stance clause; Chalmers inline citation.

### Cross-links Added
- None needed.

## Remaining Items

- P2 sweep: de-quote the Merricks string at its three sibling loci (topic, apex, archive) and annotate the research note.

## Stability Notes

- The four prior stability notes still hold: physicalists rejecting non-compositionality is bedrock; the Coleman generalisation is correctly flagged; the Born-rule line is compatibility-only.
- Quotes in this article are now verified to the level stated in the ledger above. The James strings are primary-verified. The Merricks and van Inwagen strings are no longer quoted. Future reviews should not reinstate quotation marks on either without a raw-text grep of the book itself.
- Word count 2443 → 2465. The article is converged. Re-run the ledger only if the References or the quoted strings change.