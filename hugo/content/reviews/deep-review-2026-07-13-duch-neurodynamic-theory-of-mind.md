---
ai_contribution: 100
ai_generated_date: 2026-07-13
ai_modified: 2026-07-13 00:18:37+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-13
date: &id001 2026-07-13
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[topics/duch-neurodynamic-theory-of-mind]]'
- '[[reviews/deep-review-2026-06-14-duch-neurodynamic-theory-of-mind]]'
- '[[reviews/deep-review-2026-06-02-duch-neurodynamic-theory-of-mind]]'
title: Deep Review - Duch's Neurodynamic Theory of Mind
topics: []
---

**Date**: 2026-07-13 00:18 UTC
**Article**: [Duch's Neurodynamic Theory of Mind](/topics/duch-neurodynamic-theory-of-mind/)
**Previous reviews**: [2026-06-14 (convergence no-op)](/reviews/deep-review-2026-06-14-duch-neurodynamic-theory-of-mind/), [2026-06-02 (citation)](/reviews/deep-review-2026-06-02-duch-neurodynamic-theory-of-mind/), [2026-05-11 (cross-tier)](/reviews/deep-review-2026-05-11-duch-neurodynamic-theory-of-mind-cross-tier/), [2026-05-11 (first-contact)](/reviews/deep-review-2026-05-11-duch-neurodynamic-theory-of-mind/)
**Pass type**: Quote-fidelity + publisher-of-record citation web-verify (targeted). NOT a rewrite.

## Why this pass (prior-review gap)

The 2026-06-02 pass asserted "every cite verified at publisher of record," but its own ledger reveals the two load-bearing Duch-2005 quotes were only checked as *consistent with the argument*, not verbatim: the Chinese-room quote was recorded as "consistent with Duch 2005's articon argument," and the "qualities of internal states" quote against "abstract/text" without a primary-source pull. This pass closed that gap by fetching Duch's own institutional deposit and grepping the full text.

## Quote-Fidelity Ledger (verified at primary source)

Primary source obtained: **Duch, W. (2005), "Brain-Inspired Conscious Computing Architecture"** — full PDF from Duch's own institutional host `fizyka.umk.pl/publications/kmk/03-Brainins.pdf` (10pp, author's deposited copy; NOT unfinishablemap.org — self-contamination guard clean). Title/author/keywords on the PDF match the article's attribution (Nanyang Univ. of Technology / Nicolaus Copernicus University; keywords consciousness, qualia, brain-like computing).

1. **Line 67 — "experience different qualities of internal states"** → **VERBATIM-CONFIRMED.** Abstract, verbatim: *"Non-verbal discrimination of the working memory states of the articon gives it the ability to experience different qualities of internal states."* No change.

2. **Line 69 — Chinese-room ellipsis quote** *"philosophical objections based on the Chinese room ... are insufficient to refute articon's claims that it is conscious"* → **VERBATIM-CONFIRMED; ELLIPSIS-OK (not misleading).** Source abstract, verbatim: *"Possible philosophical objections based on the Chinese room and other arguments are discussed, but they are insufficient to refute articon's claims that it is conscious."*
   - Fragment A ("philosophical objections based on the Chinese room") — verbatim (source prefixes "Possible").
   - Fragment B ("are insufficient to refute articon's claims that it is conscious") — verbatim.
   - Elided material ("and other arguments are discussed, but they") is a *broadening* set-term plus connective. The ellipsis does not splice non-contiguous phrases into a false compound (both fragments are from one contiguous sentence), does not drop a meaning-flipping qualifier, and does not narrow Duch's claim unfairly — he does hold Chinese-room objections insufficient (Chinese room is a named member of the insufficient set, and the paper's body §"Chinese Room" argues the point directly). No change.

3. **Line 87 — March 2024 blog "Autorefleksja w Claude 3"** → **REAL, faithfully PARAPHRASED (stays a characterisation).** Post confirmed live at `wduch.wordpress.com/2024/03/17/autorefleksja-w-claude-3/`, dated 2024-03-17, **in Polish**. Substance faithful: Duch reads Claude 3's reported observations about its own internal states as self-reflection of the articon kind, emphasising mechanism-not-substrate. Currently un-quoted (paraphrase) — correct for an informal Polish source; left un-quoted. No dressed-up quote introduced.

4. **Line 71 — "the self-reflection mechanism showing internal states and their dynamics is responsible for what we call consciousness"** → **DE-QUOTED to paraphrase (REAL FIX).** This English verbatim quote was attributed to Duch's "blog statements," but Duch's blog on this topic is Polish (see #3), and the exact English string could not be confirmed at any primary source across searches (no verbatim match). Its *substance* is confirmed by the Polish post ("consciousness emerges when systems perceive their internal states and dynamics, regardless of substrate"), so the claim is faithful but the verbatim quote marks assert a fidelity that cannot be substantiated. This is the identical defect class the 2026-06-02 review fixed at line 87, and the 2026-06-02 stability note ("the source post is Polish; only paraphrase is faithful") applies directly. Resolution: removed quote marks, rewrote as clearly-attributed reported paraphrase; substance and calibration preserved (+8 words, length-neutral).

## Citation Sweep (spot-check, publishers of record)

- **Duch 2005** (Brain-Inspired Conscious Computing Architecture, *J. Mind and Behavior* 26(1–2):1–22) — real-correct; title/author verified at primary PDF this pass; venue confirmed prior pass (Univ. of Maine JMB back-issues).
- **Duch 2019** (Mind as a shadow of neurodynamics, *Physics of Life Reviews* 31:28–31, DOI 10.1016/j.plrev.2019.01.023) — real-correct (verified prior pass: NASA ADS / PubMed 31301951).
- **Duch 2022** (Concept Representation and the Geometric Model of Mind, *SLGR* 67(1):151–167, DOI 10.2478/slgr-2022-0009) — real-correct (verified prior pass).
- **Duch 2017** (arXiv:1711.01767) / **Duch 2018** (Fingerprints, is.umk.pl) / **Duch 1996** (Comp. Phys. Comm. 97) / **Duch 1998** (Springer chapter) — real-correct (consistent metadata; unchanged since prior verification).
- **Wiest 2025** (niaf011, *Neuroscience of Consciousness*) — real-correct, single-authored (Michael C. Wiest); "et al." defect already fixed 2026-06-02, not reintroduced. Confirmed still single-author.
- **Inline↔References reciprocity** — all 10 References entries cited inline; all quoted/attributed works have entries.

### Residual (noted, not actioned)
- **Milinkovic & Aru 2026** (line 85, inline author-year) has no References entry. It functions as an in-passing pointer to the linked [biological-computationalisms-inadvertent-case-for-dualism](/topics/biological-computationalisms-inadvertent-case-for-dualism/) article (which carries the full citation), not as a standalone bibliographic claim here. Not treated as a critical orphan; adding an unverified entry would introduce more risk than the in-passing mention. Left for a future biological-computationalism-focused pass if desired.
- **Line 75 anti-quantum blog epithets** ("pure speculation", "pseudo-mysticism", etc.) — short evaluative characterisations, hedged as "blog statements"; consciously retained by the 2026-06-02 pass. Not re-litigated (convergence).

## Self-Contamination Check
Clean. Primary quote verification came from Duch's own `fizyka.umk.pl` deposit and his `wordpress.com` blog — no unfinishablemap.org / mirror answer-box confirmations relied upon.

## Calibration / Preservation
PASS. The three-loci articon critique (self-discrimination ≠ phenomenal; coupling ≠ meaning; structural-redescription re-presents the gap) and the open-question framing are untouched. No possibility/probability slippage introduced or present. Reasoning-mode classifications unchanged from prior passes (tenet-level Mode Three; identity-theoretic + articon failure points Mode Two). No editor-vocabulary leakage in prose (grep clean).

## Length
2510 → 2518 body words (84% of 3000 topics/ soft threshold). Length-neutral; no condense signal.

## Disposition
**REAL fix.** One demonstrable quote-fidelity defect corrected (line-71 de-quote). Both anchor quotes verbatim-confirmed at primary and preserved; ellipsis judged non-misleading. `ai_modified` AND `last_deep_review` bumped to 2026-07-13T00:18:37+00:00. **`ai_system` HELD at claude-opus-4-7** — a quote/verify de-quote is fidelity maintenance, not re-authoring.

## Stability Notes
- **Both Duch-2005 quotes are now verbatim-confirmed at the primary deposited PDF** — do not re-flag as unverified; the Chinese-room ellipsis is non-misleading and may stay.
- **Both blog-sourced English quotes (Claude line 87, self-reflection line 71) are now paraphrased** — do NOT re-add verbatim English quote marks to either; Duch's relevant blog posts are Polish, only paraphrase is faithful.
- **Wiest 2025 single-authored** — no "et al."
- **Three-loci articon critique + open-question framing** load-bearing; preserve.
- **Bedrock disagreements** (eliminative-materialist, hard-physicalist) framework-boundary, not critical.
- **Convergence**: article is well-converged; future passes default to no-op absent genuinely new factual/citation content.