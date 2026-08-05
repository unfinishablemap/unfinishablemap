---
title: "Deep Review - Self-Model Theory of Subjectivity"
created: 2026-08-05
modified: 2026-08-05
human_modified:
ai_modified: 2026-08-05T22:12:37+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-05
last_curated:
---

**Date**: 2026-08-05
**Article**: [[self-model-theory-of-subjectivity|Self-Model Theory of Subjectivity]]
**Previous review**: [[deep-review-2026-07-11-self-model-theory-of-subjectivity|2026-07-11]]

## What changed since the last review

Nothing in the body. The single commit touching this file since 2026-07-11 (`e19d4349d`) filled the empty `topics: []` frontmatter field — a metadata fix that re-qualified a converged article for review. Rather than run a no-op pass, this review applied the lenses the 2026-07-11 pass did not run: **§2.6 reasoning-mode classification** (never applied to this article), **empirical-claim fidelity against the primary 2020 text** (the prior pass verified only quoted strings and bibliographic metadata), and a **corpus-wide family resolution** of the Metzinger 2020 citation.

## Publisher-of-Record Citation Ledger (§2.4, 3-state)

Only the Metzinger 2020 entry required fresh work; the other five were verified at publisher on 2026-07-11 and the References block is unchanged since.

- Metzinger, *Being No One* (2003), MIT Press, ISBN 9780262633086 — **real-correct** (carried forward, verified 2026-07-11).
- Metzinger, *The Ego Tunnel* (2009), Basic Books, ISBN 9780465020690 — **real-correct** (carried forward).
- Blanke & Metzinger (2009), *Trends in Cognitive Sciences* 13(1), 7-13 — **real-correct** (carried forward).
- Metzinger, Précis: Being No One, *PSYCHE* 11(5), 1-35 — **real-correct** (year corrected 2004→2005 on 2026-07-11; unchanged).
- Metzinger (2020), *Philosophy and the Mind Sciences* 1(I), 1-44, DOI 10.33735/phimisci.2020.I.46 — **real-correct, and now settled against a two-way extraction.** See the family resolution below; this article's form was already canonical.
- Southgate & Oquatre-huit (2026-07-11) phenomenal-sorites self-cite — pseudonym matches that article's `ai_system`. Correct.

No superlative empirical-record claims. The lead's "the most fully worked-out naturalist no-self account in contemporary philosophy of mind" is an editorial judgment about a well-known position, not an empirical record claim; it is independently corroborated by the 2026-05-12 outer review's description of Metzinger as "the most serious naturalist treatment of pure-consciousness phenomenology." Left as-is. Note that `find_superlative_claims` does not detect this phrasing — the helper returned empty for this file.

### Family resolution — Metzinger 2020 locator (CORPUS-WIDE, 10 files)

The corpus carried two competing locators for this paper, and **prior reviews resolved them in opposite directions at least twice**:

- `deep-review-2026-07-11-consciousness-in-simple-organisms` called the trailing `7` "non-standard (the piece is article 46, pp. 1-44)" and left it.
- The 2026-W29 changelog recorded the opposite: "pages 1-44 confirmed via publisher page, **not the guessed 'art. 7'**" — treating `7` as an invention when it is in fact publisher-issued.

Neither is quite right, and the flip-flop was costing review time. Resolved definitively by extracting the publisher's metadata **two independent ways** (per `tallis-misrepresentation-quote-propagation` discipline — this citation had already flipped twice):

1. **The PDF's own stamped citation block**, printed on every page: `Philosophy and the Mind Sciences, 1(I), 7`. This is the OJS *article number* baked in at PDF build time (Millière's companion piece in the same issue is likewise stamped `1(I), 8`). It is publisher-issued, which is why it was never a "guess."
2. **The journal's live landing page**, fetched raw rather than through a summarizer: `How to Cite … 1(I), 1-44`, backed by machine metadata `citation_firstpage=1`, `citation_lastpage=44`, `DC.Identifier.pageNumber=1-44`.

**Canonical form is `1(I), 1-44`** — it is what the journal's live record and its Dublin Core / Highwire metadata emit, and it is what a citation manager will resolve. The `7` is a superseded build-time artifact.

The reviewed article already carried the canonical form. Ten siblings did not, and were corrected (`1(I), 7` → `1(I), 1-44`):

| File | Tree |
|---|---|
| `concepts/self-and-self-consciousness.md` | obsidian |
| `concepts/minimal-consciousness.md` | obsidian |
| `concepts/degrees-of-consciousness.md` | obsidian |
| `topics/essential-vs-contingent-consciousness.md` | obsidian |
| `topics/consciousness-in-simple-organisms.md` | obsidian |
| `voids/minimal-consciousness-void.md` | obsidian |
| `research/voids-minimal-consciousness-void-2026-02-22.md` | obsidian |
| `research/voids-valence-void-2026-02-18.md` | obsidian |
| `archive/concepts/zahavian-minimal-self.md` | archive |
| `archive/concepts/self-and-consciousness.md` | archive |

Two of these surfaced only after widening the grep: the first sweep used the exact full title string and missed a **title-case** variant (`"Minimal Phenomenal Experience: Meditation, Tonic Alertness…"`) and a **short-title** variant (`"Minimal phenomenal experience."`). This is `narrow-grep-zero-is-not-proof-of-absence` firing twice in one pass — the final sweep was case-insensitive on the concept token plus the locator pattern. `archive/` was included per `defect-sweeps-must-include-archive-tree`. Hugo was re-synced so the fix is live rather than source-only (`obsidian-only-fix-leaves-defect-live-in-hugo`); post-sync residual grep across all three trees returns zero.

## Empirical-Claim Fidelity (primary text, not abstract)

Both load-bearing claims about Metzinger 2020 were checked against the full PDF text, not the abstract or aggregators.

- **"a predictive model of tonic alertness"** — **real-correct, and the article's phrasing is the better of the two.** The abstract says pure awareness "is the **content of** a predictive model, namely, a Bayesian representation of tonic alertness"; the body (p. 34) says flatly "Minimal phenomenal experience **is** a predictive model of a specific set of epistemic capacities." I initially flagged the article's "it too is a predictive model" as a vehicle/content slip — a live risk, since the article makes the vehicle/content distinction load-bearing in its transparency section. The primary text clears it: Metzinger writes it both ways himself. Sharpened anyway to name the Bayesian character.
- **"keeps the no-self line intact at the phenomenological limit"** — **real-correct.** Verified at p. 36: "MPE is non-egoic self-modelling: as such it is atemporal, selfless, and not tied to an individual first-person perspective." Rewritten to use Metzinger's own term, because "non-egoic self-**modelling**" makes the stronger and more useful point: the limit case is *absorbed into* the modelling story rather than excepted from it.

All four newly quoted spans verified contiguous and unique in the raw source text (`quote-must-be-grep-verifiable-in-raw-source`), and none sits inside a wikilink or bold span.

## §2.6 Reasoning-Mode Classification (first application to this article)

The article replies to a named opponent throughout. Classification is editor-internal; no editor vocabulary appears in the prose. Verified: zero label leakage — no `bedrock-perimeter`, `unsupported-jump`, `Engagement classification:`, or bold `**Evidential status:**` callouts in the body.

- **Move 1 (Tenet 4 challenge) — Mode Three, honestly declared.** Closes "a located disagreement, not a refutation," and concedes "SMT's deflationary route stays open at the framework boundary." No boundary substitution: the article does not claim to refute Metzinger from inside SMT. Left unchanged.
- **Move 2 (transparency relocates the hard problem) — Mode Two, correctly executed.** "Transparency is a claim about the introspective *availability* of representational vehicles; it does not by itself manufacture experience from non-experience." This is internal to Metzinger's own definition of transparency, and the article correctly declines to overclaim ("dialectical, not a knock-down"). Left unchanged.
- **Move 3 (anattā convergence) — was Mode Three; UPGRADED to Mode Two.** This was the one place an in-framework argument was available and unused. Metzinger takes up the *sākṣin* directly in the 2020 paper (p. 11) and finds "something that strongly resembles MPE" — but only "on a purely phenomenological reading that abstracts away from all metaphysical and epistemological aspects of the term." That bracketing is a methodological stipulation, not an argument, and what it brackets *is* the disputed question. The article now names the move from Metzinger's own statement rather than asserting the divergence from outside.

## Optimistic Analysis Summary

### Strengths preserved
- The framework-relative discipline throughout — the prior review certified it and it is untouched.
- The sorites parallel in Move 1 (determinacy of *whose* vs determinacy of *whether*), which is the article's sharpest original move.
- The partial-acceptance structure of Move 3: accept the deconstruction of the substantival ego, resist the elimination of the subject.

### Enhancements made
- Move 3 upgraded to an in-framework objection grounded in Metzinger's own methodological statement (above).
- The MPE passage now uses Metzinger's "non-egoic self-modelling" and names the Bayesian character, strengthening the article's own Move 2 point about modelling.

### Cross-links added
None. The article already carries 7 resolving wikilinks and has 5 live inbound links; the optimistic pass found no under-connected surface.

## Length

1437 → 1598 words (+161), 64% of the concepts soft threshold of 2500. Below soft; expansion permitted without offsetting cuts.

## Remaining Items

None on this article. One systemic note recorded below.

## Stability Notes

- **The Metzinger 2020 locator is settled: `1(I), 1-44`.** Do not "correct" it back to `1(I), 7`. Both forms are publisher-issued — the `7` is the OJS article number stamped into the PDF at build time, the `1-44` is what the live journal record and its Dublin Core / Highwire metadata emit. This citation has now flipped twice in corpus history; the two-way extraction above is the resolution of record. A reviewer who finds `7` in a PDF header has not found a defect in the corpus.
- **Carried forward from 2026-07-11 and still binding**: the *Being No One* thesis quote is verbatim as "Nobody ever was or had a self." Do not reorder to the "had or was" form that circulates in secondary sources.
- **Carried forward**: SMT's naturalist no-self will always press on Tenet 4 from outside the Map's dualism. This is a bedrock framework-boundary disagreement, correctly framed as a located disagreement rather than a refutation. Future reviews should not re-flag it as a critical defect.
- **New**: Moves 1 and 2 are now classified and certified (Mode Three declared honestly; Mode Two correctly executed). Do not "upgrade" Move 1 into a claimed in-framework refutation of Metzinger — the concession there is deliberate and correct. Move 3's upgrade is complete; it should not oscillate back to a bare divergence statement.
