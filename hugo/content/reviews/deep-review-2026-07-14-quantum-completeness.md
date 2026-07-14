---
ai_contribution: 100
ai_generated_date: 2026-07-14
ai_modified: 2026-07-14 08:44:03+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-14
date: &id001 2026-07-14
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[quantum-completeness]]'
title: Deep Review - Quantum Completeness
topics: []
---

**Date**: 2026-07-14
**Article**: [Quantum Completeness](/concepts/quantum-completeness/)
**Previous reviews**: [2026-06-25](/reviews/deep-review-2026-06-25-quantum-completeness/) (4th), [2026-05-27](/reviews/deep-review-2026-05-27-quantum-completeness/) (3rd), [2026-04-18](/reviews/deep-review-2026-04-18-quantum-completeness/) (2nd), [2026-03-18](/reviews/deep-review-2026-03-18-quantum-completeness/) (1st). This is the **5th** deep review.

## Scope / Mode

Orthogonal-lens pass on a citation-dense, converged (sonnet-4-6 build) article. The **citation-metadata seam is exhausted here**: the 2026-05-27 review ran a full 16-cite publisher-of-record ledger (fixing the Krizek-Mairhofer taxonomy hallucination, the Barrett year, and the Stapp venue) and the 2026-06-25 pass re-spot-checked the three highest-value cites — all real-correct. Per the loop's steering that the metadata seam is near-exhausted across the reachable older cohort, this pass shifted to the orthogonal lenses: **quote-fidelity**, **citation-framing** (does the cited paper's own conclusion support the use made of it), and **empirical-currency / recomputation**. HELD the existing `ai_system: claude-sonnet-4-6` (a one-word verbatim-quote correction is not re-authoring).

## Verdict: real-findings pass — 1 quote-fidelity fix (verbatim misquote of Fuchs, survived 4 prior reviews)

## Fix applied

**Quote-fidelity — Fuchs "act of creation" → "moment of creation" (§QBism, line 94).**
The article rendered QBism's characterisation of measurement as, *in Fuchs's phrase,* **"a little act of creation."** Publisher-of-record / primary-source verification (Fuchs, *On Participatory Realism*, arXiv:1601.04360 and the participatory-realism corpus) establishes Fuchs's actual verbatim construction is **"a little moment of creation"** — *"when an agent reaches out and touches the world, a little moment of creation occurs in response,"* and measurements are *"moments of creation."* The word **"act"** belongs to a *different* Fuchs construction ("an elementary **act** of creation is happening"), not the "a little ___ of creation" phrase the article quotes. The article's "a little act of creation" is a conflation of the two, presented as a direct quotation.

Corrected in place: `"a little act of creation"` → `"a little moment of creation"`. This is a re-frame-to-verbatim fix (the QBism point — measurement as active creation, not passive observation — is preserved), not a deletion.

**Why it survived four prior reviews.** The 2026-06-25 review explicitly stated *"The one verbatim external quote (Fuchs's 'a little act of creation') is correctly attributed to QBism."* That check confirmed **attribution** (the idea is Fuchs's / QBism's) but never verified the **verbatim wording** at the primary publisher. This is the exact quote-fidelity-defects-survive-metadata-reviews channel: verbatim accuracy of quoted text is orthogonal to citation-metadata correctness, and metadata-focused passes ratify a misquote whose attribution is sound.

## Orthogonal lenses that came back clean (checked, no fix — recorded so future passes don't re-litigate)

- **Citation-framing — Barrett (2006), *Erkenntnis* 65(1):97-115.** The article says *"Barrett (2006) argues that this structural opening in quantum mechanics favours mind-body dualism across interpretation families."* Verified against Barrett's **own** stated conclusion (publisher/PDF): *"a strong mind–body dualism is required of any formulation of quantum mechanics that satisfies a relatively weak set of explanatory constraints… it is the preferred basis problem that pushes both collapse and no-collapse theories in the direction of a strong dualism."* The article's framing ("favours … across interpretation families") faithfully tracks Barrett's both-collapse-and-no-collapse thesis and correctly hedges with "favours" rather than "proves." **Real-correct framing.** (Note for future passes: Barrett also offers an escape — dropping a constraint at the cost of a "physical–physical dualism"; the article's one-clause use does not misrepresent by omitting it, since "favours" is appropriately weak.)
- **Empirical-currency / recomputation — decoherence timescale.** The claim *"off-diagonal elements … decay … on timescales of 10⁻¹³ seconds or less for macroscopic objects at room temperature (Zurek 2003, Schlosshauer 2007)"* is a **loose upper bound**, not a record claim. The canonical macroscopic figure (e.g. Zurek's 1 g / 1 cm superposition at room temperature) is ~10⁻²³ s — which *is* "less than 10⁻¹³ s," so the "or less" hedge holds. 10⁻¹³ s is nearer the neural/mesoscopic (Tegmark-2000-class) estimate; the phrasing is mildly loose but not false. The 2026-06-25 pass already considered and accepted this. **No fix** (per steering: do not manufacture a fix).
- **QBism founders / attribution.** "developed by Caves, Fuchs, and Schack and later joined by Mermin" — correct (Caves/Fuchs/Schack founded QBism; Mermin joined later). Fuchs, Mermin & Schack 2014 (AJP 82(8):749-754) entry stands (verified in prior ledger).
- **No-go theorem cites** (Bell 1964, Hardy 1993, Kochen-Specker 1967, PBR 2012, Hensen 2015 loophole-free) — metadata verified in the 2026-05-27 full ledger and the 2026-06-25 spot-check; PBR's "part of the ontic furniture" claim is correctly conditionalised ("given a natural independence assumption … under that assumption") with the Emerson et al. 2013 caveat retained. Not re-litigated.

## Attribution / Source-Map Separation
Clean and unchanged. Map-specific moves (consciousness-selection at Process 1, the five tenets) explicitly labelled; Barrett, Stapp, Zurek, Schlosshauer, PBR, Albert/Kent accurately attributed.

## Reasoning-Mode Classification (named-opponent replies)
- **QBism (Caves/Fuchs/Schack/Mermin)**: Mode Two — unsupported-foundational-move engagement (QBism "dissolves rather than solves"; credence-only reading forfeits PBR's force), conceding QBism "correctly identifies" agent-dependence. Honest, no label leakage. Unchanged.
- **Many-worlds / Everettians**: Mode Three — framework-boundary marking, done explicitly (concedes Everettian parsimony before the indexical-identity / Tenet-4 objection, Albert 2010 / Kent 2010 supporting the residue honestly). Unchanged.

## Tenet 4 / Evidential-Status Check
No possibility/probability slippage. In-framework theorems argued as results; consciousness-selection explicitly flagged "empirically unfalsifiable" and "a philosophical framework compatible with physics, not a competing physical hypothesis." A tenet-accepting reviewer would not flag any claim as overstated. Holds.

## Length
~2600 words (104% of 2500 concepts soft target — soft_warning, well under 3500 hard). The fix is word-neutral. No length action.

## Integrity Checks
Wikilinks and internal anchors (`#decoherence-objection`, `#many-worlds-honestly`, `#process-1`, `#six-senses`) resolve. No bare `[[n,k,d]]` QEC notation. EOF clean (ends on reference 16). No future-dated timestamps (fix stamped at real `date -u` 2026-07-14T08:44:03Z). Cliché sweep: the line-94 "not passive observation but … 'a little moment of creation'" is a substantive single-sentence contrast, not the hollow banned construct.

## Remaining Items
None.

## Stability Notes
- Bedrock-disagreement notes from all four prior reviews remain in force and must NOT be re-flagged: the MWI indexical-identity standoff (Tenet 4 boundary), the eliminativist rejection of "gap → consciousness," and the acknowledged unfalsifiability of consciousness-selection.
- **Citation metadata is fully publisher-verified and stable across five passes** (16-cite ledger 2026-05-27, spot-check 2026-06-25). The orthogonal lenses are now also recorded: Barrett framing (real-correct), decoherence timescale (defensible upper bound), and the one quote-fidelity defect fixed this pass. Future deep reviews should treat this article as converged unless the body or References block is substantively modified; the verbatim-quote channel has now been closed, so a future pass need not re-verify the Fuchs quote unless the surrounding sentence is re-edited.