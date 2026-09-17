---
title: "Deep Review - Bi-Aspectual Ontology"
created: 2026-09-17
modified: 2026-09-17
human_modified: null
ai_modified: 2026-09-17T23:26:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[bi-aspectual-ontology]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-17
last_curated: null
---

**Date**: 2026-09-17
**Article**: [[bi-aspectual-ontology|Bi-Aspectual Ontology]]
**Previous review**: [[deep-review-2026-07-17-bi-aspectual-ontology|2026-07-17]]
**Primary lens**: stranded-dependents check on the 2026-09-09 scope narrowing, plus inline↔references reconciliation.

## Why this pass was not a no-op

The 2026-07-17 review closed with "treat it as a no-op unless the body is edited." The body **was** edited: `d2aa12533d` (2026-09-09, refine-draft) rewrote L51/L53 to remove the claim that the measurement problem warrants conscious selection and that consciousness is "the only" candidate. That fix is correct and is preserved intact. What it did not do was propagate: the narrowed claim was installed at two lines while **five other loci across the article continued to state the unnarrowed version**. This is the stranded-dependents pattern — grep-invisible semantic dependents left behind by a locus-targeted fix.

Word count 2825 → 2834 (+9, length-neutral; `soft_warning`, concepts soft 2500 / hard 3500).

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Internal contradiction — unrestricted actualisation claim in five loci (FIXED).**
The article's own L53 now reads "denying that consciousness supplies it alone: physical objective reduction provides the baseline collapse that secured definite stellar, chemical, and prebiotic outcomes long before any observer." Five passages contradicted this directly. The corpus canon backs the narrow reading: [[prebiotic-collapse]] ("Objective reduction provides the baseline; consciousness modulates rather than initiates") and [[tenets/background-commitments|Posit Two: Objective Single-Outcome Actualization]]. Fixes, all scope qualifiers rather than rewrites:

- **L37 (lead)** — "Consciousness supplies the actuality that determines which physically permitted outcomes become real" → "Consciousness supplies that actuality where a neural interface exists; elsewhere physical objective reduction fixes outcomes without it." The parenthetical gloss "**actuality** (what consciousness provides)" → "(what makes one possibility real)", since by the article's own account consciousness is not its only provider. This is the most consequential locus: it is the front-loaded summary an LLM truncation reads first.
- **L49** — "consciousness fills this role" → "fills this role at neural interfaces". This locus sat in the paragraph *immediately above* the 09-09 fix, contradicting it across a paragraph break.
- **L63 (commitment 2)** — "actuality resolves them" → "resolves them — consciousness doing so at neural interfaces".
- **L115 (QBism)** — "the Map takes the agent's centrality as **evidence that consciousness plays an ontological role** at the measurement boundary" → "reads the agent's ineliminability as marking where the boundary lies rather than as evidence that consciousness selects — a burden the agency arguments carry." This locus was a second defect as well as a dependent: it re-committed the exact evidential move L51 had just disowned (treating a feature of quantum mechanics as evidence for conscious selection), i.e. possibility/probability slippage, critical per §2 rather than bedrock disagreement. A tenet-accepting reviewer would still flag it.
- **L139 (Bidirectional Interaction)** — "actuality causally selects which structural possibilities become real" → "at neural interfaces actuality causally selects…".

**2. Inline↔references mismatch on Velmans (FIXED).** Body L85 read "Velmans (2009)"; reference #5 read "Velmans, M. (2008)". Orphaned in both directions. Root cause: the 2026-06-25 pass corrected the *reference entry* from 2009/16(2-3)/209-236 to 2008/15(2)/5-50 but left the inline cite untouched; the 2026-07-17 pass recorded the reference as "still correct" without cross-checking inline, so the mismatch survived a review that declared the citation surface converged. Publisher of record confirms 2008: Ingenta Connect, *JCS* 15(2), 5-50. Body corrected to (2008). The stale 2009/16(2-3)/209-236 form still sits in research note `bi-aspectual-ontology-dual-aspect-traditions-2026-03-14` L199/L241 — research-note-only, did not propagate further; left as-is (research notes are dated artefacts).

### Medium Issues Found
- **Le Bihan 2019 reference incomplete (FIXED)** — ref #8 gave *Philosophical Investigations* 42(2) with no page range. Verified at Wiley (DOI 10.1111/phin.12220): **42(2), 186-201**. Added.
- **Redundancy trimmed to pay for the additions** — L45's "the point where structural description reaches its limit and a different kind of account is needed" duplicated L51's identical phrase verbatim; trimmed to the second clause. L101's closing "The interaction is not between alien substances but between complementary dimensions of what exists" was a restatement of the two preceding sentences and an instance of the "not X but Y" construction the style guide flags; removed. No dependents (grep-checked across `obsidian/`).

### Counterarguments Considered
- *The narrowing makes consciousness redundant* (the bias-without-deviation dilemma). Not re-litigated here — [[prebiotic-collapse]] and [[ensemble-level-epiphenomenalism]] carry it explicitly and this article now points at the agency arguments rather than restating the debt.

## §2.4 Publisher-of-Record Citation Ledger

Body citation surface unchanged since the 2026-06-25 full ledger except where noted; this pass re-verified the two live defects and the one open item.

- Velmans 2008, *Reflexive Monism*, *JCS* 15(2):5-50 — **real-wrong-metadata (inline)**: body cite corrected 2009 → 2008; reference entry was already correct.
- Le Bihan 2019, *Aspects in Dual-Aspect Monism and Panpsychism: A Rejoinder to Benovsky*, *Philosophical Investigations* 42(2) — **real-wrong-metadata (incomplete)**: pages 186-201 added. Wiley DOI 10.1111/phin.12220.
- Pautz 2017, *How Is Constitutive Russellian Monism (or Pansychism) Better than Dualism?* — **real-correct**. Open item carried since 06-25 now **closed**: confirmed via PhilPapers/PhilArchive as an unpublished manuscript replying to Roelofs's comments on Pautz 2015. Reference #6's form is right. (The published title carries the typo "Pansychism"; the article's silent correction to "panpsychism" is left standing.)
- Real-correct, unchanged from the 06-25/07-17 ledger: Spinoza 1677 *Ethics*; Della Rocca 2008 (Routledge); Chalmers 1996 (OUP); Atmanspacher & Rickles 2022 (Routledge); Cutter 2019 *Analytic Philosophy* 60(2):109-129; Gleason 1957 *J. Math. Mech.* 6(6):885-893; Zheng & Meister 2025 *Neuron* 113(2):192-204; Tononi 2008 *Biol. Bulletin* 215(3):216-242; Fuchs 2017 *Mind and Matter* 15(2):245-300.
- Map self-cites (never strip): Southgate & Oquatre-six 2026-01-16; Southgate & Oquatre-cinq 2026-01-15.
- **Currency sweep**: `find_superlative_claims` returns 0 — no superlative empirical claims to re-date.
- **Cited-author-stance leg**: no cited author is presented as endorsing the Map's conclusion. Pautz and Cutter are correctly presented as arguing Russellian monism is unstable/no better than dualism, not as endorsing quantum interactionism. Tononi, Fuchs, Velmans, Spinoza and Le Bihan are all framed as rivals or as sources of a distinction the Map repurposes.

## §2.6 Reasoning-Mode Classification (editor-internal)

- **Spinozist parallelism** — Mode Three. Boundary-marking; parallelism is denied by design, and the article says so plainly.
- **Pauli-Jung / Atmanspacher & Rickles** — Mode Three, honestly framed ("closer to the Map's view", differing on the neutral substrate).
- **Russellian monism (Pautz, Cutter)** — Mode One. In-framework: the instability charge is argued from the monist's own parsimony standard, using monist critics' own results.
- **IIT (Tononi)** — Mode One. The article argues from IIT's own structural determination of Φ that its consciousness has no selective role — internal to IIT, not tenet-assertion.
- **QBism (Fuchs)** — Mode Two, **corrected this pass**. The engagement identifies an unsupported foundational move (QBism presupposes agents with determinate experience without accounting for it). The old wording then slid from that into asserting positive evidence for the Map's own ontology; the fix keeps the Mode Two identification and drops the unearned evidential upgrade.
- **Le Bihan / deflationary "aspects" objection** — Mode One; answered on the deflationist's own terms (the vocabulary earns its keep by specifying a relationship and an interface).
- **Label leakage**: none. Grep for all forbidden editor labels returns zero.

## Optimistic Analysis Summary

### Strengths Preserved
- The structure/actuality vocabulary and the "Born rule as interface specification" reading — praised in [[optimistic-2026-03-31]] and untouched.
- The Gleason hedge ("This is the Map's interpretation, not a direct consequence of Gleason's result, but the mathematical uniqueness is suggestive") — an exemplary calibration sentence; left exactly as written.
- The five-way differentiation structure (Spinoza / Pauli-Jung / Velmans / Russellian monism / substance dualism / IIT / QBism), which is what makes this article the corpus's reference statement of the Map's ontology.
- The 2026-09-09 L51/L53 narrowing itself — preserved verbatim and now propagated rather than overwritten.

### Enhancements Made
- The lead now survives truncation *with its scope intact*: an LLM reading only the first paragraph previously got the unrestricted claim.
- The QBism section's conclusion is now consistent with the article's own evidential discipline.

### Cross-links Added
None. The [[ontic-structural-realism]] Further Reading entry added by `40091fb3ab` was checked this pass (it was a drive-by insertion from a review aimed at the OSR article, never itself reviewed): the gloss "whether the denial extends to experience is a separate commitment" is faithful to the OSR article's own finding that no OSR theorist carries the physics thesis across to experience, and the reciprocal link exists in `ontic-structural-realism`'s `related_articles`. Accurate — kept.

## Remaining Items

None blocking. One observation for future passes: the `description` frontmatter glosses actuality as "(consciousness)". That remains the correct *aspect* naming, and the defect fixed here was the scope of the selection claim rather than the aspect naming, so it is left alone — but a future pass that revisits the two-aspect framing should check the description with it.

## Stability Notes

- **The 07-17 "converged, treat as no-op" note was right about the citation surface and wrong as a general licence.** It caused a real defect to survive: the Velmans inline/reference mismatch was created by the 06-25 fix and ratified by the 07-17 pass, which checked the reference entry without checking the inline cite. Future passes should treat "the reference entry was corrected last pass" as a prompt to check the *body* cite, never as certification of it.
- **Scope-narrowing edits need a dependents sweep, and it cannot be done by grep.** The 09-09 fix was correct and self-contained but left five semantic dependents stating the old claim, in the lead, in an adjacent paragraph, in a numbered commitment, in the QBism section, and in the tenet-relation section. When a future pass narrows a claim in this article, it should re-read the lead, the three numbered commitments, and the "Relation to Site Perspective" bullets specifically.
- **Genuine bedrock, do not re-flag**: dual-aspect monists, Russellian monists, and IIT/QBism proponents rejecting causal interaction between aspects. These are framework-boundary standoffs. Unchanged from previous reviews.
- The article is now consistent with [[prebiotic-collapse]] and [[tenets/background-commitments]] on the division of labour between objective reduction and conscious modulation. If either of those moves, this article is a dependent and should be re-checked.
