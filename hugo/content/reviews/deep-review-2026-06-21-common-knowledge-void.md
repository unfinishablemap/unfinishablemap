---
ai_contribution: 100
ai_generated_date: 2026-06-21
ai_modified: 2026-06-21 10:41:03+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-21
date: &id001 2026-06-21
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[common-knowledge-void]]'
title: Deep Review - The Common-Knowledge Void
topics: []
---

**Date**: 2026-06-21
**Article**: [The Common-Knowledge Void](/voids/common-knowledge-void/)
**Previous review**: [2026-06-03](/reviews/deep-review-2026-06-03-common-knowledge-void/) (declared converged) / [2026-04-30](/reviews/deep-review-2026-04-30-common-knowledge-void/)
**Word count**: 2999 → 2999 (length-neutral; voids/ soft 2000, hard 3000 — **1 word clear of hard**, strictly length-neutral mode enforced)

## Why this review (genuine-drift trigger, not scorer artefact)

Unlike the 2026-06-03 no-op (a staleness-scorer false-positive on an HTML-comment-block removal), this review was selected because commit **d67673bcb (2026-06-10, "Scope the formal claims")** materially RE-SCOPED the void's load-bearing formal claims *after* the 2026-06-03 convergence declaration, but bumped only `ai_modified` and left `last_deep_review` at 2026-06-03 — so the re-scoped claims were unverified. The re-scope was directionally a **calibration improvement** (it scoped HM *down* from "covers any actual physical interface between embodied minds" presented as part of the theorem, to "honest extrapolation … a step beyond the formal scope," and newly asserted that HM "is not a universal impossibility" because public-announcement models *can* generate common knowledge). The new factual claims required publisher-of-record verification.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Aumann naming misattribution (line 72)** — CRITICAL, FIXED. Article read: *"Aumann (1989) calls this 'the Halpern–Moses paradox.'"* Web-verification at the publisher of record (Gonczarowski & Moses 2024, "Common Knowledge, Regained" — co-authored by Moses himself) establishes that **Aumann (1989) named it the Halpern–Moses *problem***; the term *"paradox"* was first applied by **Morris (2014)**. ("Common Knowledge, Regained" explicitly: *"termed the Halpern–Moses Problem"* by Arrow et al. 1987 and Aumann 1989; *"was called a paradox by Morris (2014)"*.) This is a misattribution of a term to an author who did not use it — the ai_citation_metadata_unreliable pattern in which intra-corpus consistency *ratifies* a wrong cite rather than catching it (the 2026-06-03 review actively marked this pairing "registry-clean"). **Resolution**: corrected to *"Aumann (1989) names this the Halpern–Moses problem."* (net −2 words; length-neutral). Morris (2014) not added as a cite — the "paradox" terminology is already established for the reader via Lederman's title (cited at line 84, *Two Paradoxes of Common Knowledge*), and the article is at the hard ceiling.

### Citation Web-Verification (publisher of record) — per-cite ledger

Focus on the formal anchors touched by / load-bearing for the d67673bcb re-scope; the verbatim-quoted and post-2010 specialist cites were verified clean at publisher of record by the 2026-06-03 review and are unchanged since (not re-litigated).

- **SEP "Common Knowledge" public-announcement attribution (line 52, ref #17)** — **state: real-correct (PRESENT/faithful).** *This was the single highest-priority verification target.* The live SEP entry (Vanderschraaf & Sillari, plato.stanford.edu/entries/common-knowledge/) **does** catalogue public-announcement models in which common knowledge IS generable under stipulated assumptions: Lewis's reliance on "a proposition A* that is *publicly known*, as is the case when agents hear a public announcement"; the Barbecue/Muddy-Children problem in which "by announcing a fact already known to every diner, the cook made this fact *common knowledge* among them." The article's line-52 claim — "in idealised public-announcement models (a synchronous broadcast all parties simultaneously witness), common knowledge *is* generable under the stipulated assumptions, as the SEP entry catalogues" — is faithful. The "honest extrapolation" scoping (lines 42, 52) therefore rests on a verified premise.
- **Halpern & Moses (1990) (ref #7)** — state: real-correct. *JACM* 37(3), 549–587. Coordinated-attack result over unreliable channels confirmed; "common knowledge cannot be attained in practical distributed systems"; preliminary version PODC 1984. The article's strictly-scoped restatement ("unreliable channels — message loss, delay, or timing uncertainty in a specified distributed-systems model — and is not a universal impossibility") is faithful to the theorem's actual scope.
- **Rubinstein (1989) (ref #12)** — state: real-correct. *AER* 79(3), 385–391, June 1989, "The Electronic Mail Game: Strategic Behavior under 'Almost Common Knowledge'." Discontinuity result faithful (arbitrarily-high-order mutual knowledge → no-information outcome; strategic dividend not delivered).
- **Aumann (1976) (ref #1)** — state: real-correct. *Annals of Statistics* 4(6), 1236–1239, "Agreeing to Disagree." Agreement-theorem statement (common prior + common knowledge of posteriors ⇒ equal posteriors) faithful.
- **Aumann (1989) (ref #2, "Notes on Interactive Epistemology", Cowles Foundation working paper)** — state: real-correct *as a reference entry*. This is a genuine 1989 Aumann Cowles Foundation working paper (six Yale lectures, spring 1989; later formally published 1999 as *Interactive Epistemology I/II*, *Int. J. Game Theory*). NOTE: the literature sometimes attributes the Halpern–Moses *problem* naming to a sibling 1989 Aumann manuscript ("Formal common knowledge: an approach to the Halpern-Moses problem"); both are Aumann 1989 Yale/Cowles works, so the body's "Aumann (1989)" attribution is acceptable. The reference-entry metadata (title + venue) is correct and was left unchanged. The *only* defect was the **term** ("paradox" → "problem"), now fixed.
- **SEP entry year (ref #17, cited as 2014)** — state: real-correct, minor imprecision noted (NOT fixed). The SEP entry was first published 2001, revised 2002/2005/2007/2013/**2022** (most recent substantive revision 5 Aug 2022). "2014" falls between revisions and is not *wrong* (the entry existed and substantively contained the public-announcement material then). Left as-is: the date is not load-bearing, the content attribution is verified, and the article is at the hard ceiling. A future editor may optionally update 2014 → 2022 (word-neutral).

**inline ↔ References integrity**: every inline author-year cite (Halpern & Moses 1990; Rubinstein 1989; Aumann 1976; Aumann 1989; Lewis 1969; Schiffer 1972; Lederman 2018; Schelling 1960; Pettit; Bicchieri 2006; Clark & Brennan 1991; Husserl 1931; Levinas; Carruthers 2011/2017; Nāgārjuna via Garfield 1995; SEP via Vanderschraaf & Sillari 2014) has a References entry; every References entry is cited inline or is a Further-Reading internal Map cite. No orphans in either direction.

### Internal-Consistency Check (re-scope did not introduce contradiction)

The genuine-drift concern was whether the scoped intro ("unattainable across a wide, practically universal class of cases", line 42) is quietly over-read back to "structural impossibility" elsewhere. **No contradiction found.** "Structural impossibility" at line 44 ("whose *joint* structural impossibility is the analytical claim") and "the impossibility" at line 133 consistently denote the **conjunction-coalesce claim** — the void as the joint impossibility of the three faces — NOT a re-assertion of Halpern–Moses as a single universal theorem. The description field's "structural impossibility at the heart of coordination" (line 3) describes the void's overall thesis (supported via honest extrapolation), consistent with the scoped body. The single-theorem scope at line 52 is the carefully-delimited claim; the void-level "structural impossibility" is the joint claim. Coherent; not flagged.

### Currency Check (empirical-record-currency-drift)

- No superlative empirical claims detected (`find_superlative_claims` returned empty) — no currency sweep needed.
- **Lederman (2018) deflationary verdict not superseded.** The most recent formal anchor is Lederman 2018. The newest relevant work surfaced (Gonczarowski & Moses, "Common Knowledge, Regained", 2024) pursues a *reconstruction* ("regained") research direction; it does not refute Lederman's deflationary read that the strict construct is overdemanding, and the void's deflationary framing stands. No newer survey overturns the verdict.

## Calibration / Void-Structure Check ([evidential-status-discipline](/project/evidential-status-discipline/))

- **The re-scope is a genuine, internally-consistent calibration improvement** — the opposite direction from possibility/probability slippage. The article now *under*-claims relative to the prior version: HM is explicitly "not a universal impossibility," and the embodied-interface reading is flagged as "honest extrapolation … a step beyond the formal scope," "defensible … but flagged." A tenet-accepting reviewer would NOT flag any claim as overstated; the scoping is the responsible move. No slippage; no upgrade of a boundary case up the five-tier evidential-status scale on tenet-load.
- **Aumann–tenet dependency (line 78) faithful.** The Aumann contrast is explicitly demoted to "contrast rather than a third converging anchor" and made dependent on [No Many Worlds](/tenets/#no-many-worlds) (carries no work where MWI prevails; case falls back on Halpern–Moses and Rubinstein). The `^no-many-worlds` anchor resolves (tenets.md:108). This matches the tenet's own indexical-identity treatment.
- **Conjunction-coalesce three-face structure preserved**: verification (*Unexplorable*), approximation-discontinuity (*Unexplorable*), operational-fiction (*Occluded/possibly Self-Occluded*) intact, apophatic framing un-flattened, void POSITED as the structural shape of a fiction's success-conditions (Madhyamaka reply guards reification).
- All four tenet anchors resolve: `^occams-limits` (most-directly-engaged), `^dualism` (indirect, live-alternatives caveat preserved), `^bidirectional-interaction`, `^no-many-worlds`.

## Reasoning-Mode Classification (named-opponent engagements, editor-internal)

Unchanged from 2026-06-03; re-confirmed, no label leakage into prose:
- **Carruthers (heterophenomenology)** — Mode Three (framework-boundary; explicitly declared bedrock; formal faces survive). Natural prose.
- **Madhyamaka / Nāgārjuna** — Mode Two/Three mix (reply uses the Map's own operational-fiction commitment as the recognised non-reification, then marks residue). Natural prose.
- **Schelling/Pettit/Bicchieri focal-points** — Mode One/Two (salience-regress argument internal to the opponent's own appeal to shared content; "displaces the load rather than dissolving it"). Natural prose.
No editor-vocabulary leakage; no boundary-substitution.

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)
- Front-loaded lead with all named theorems + operational-fiction thesis (LLM-truncation-resilient).
- The three-faces conjunction-coalesce structure (the article's distinctive analytical contribution).
- "Constitutive smoothing"; "if one could inspect common knowledge, one would already have produced it."
- The salience-regress reply (methodologically reusable across the Map).
- The newly-added honest-extrapolation scoping is itself a *strength*: it is exactly the evidential-restraint pattern the Hardline-Empiricist persona praises (tenet-coherent, not evidence-elevating; the formal theorem is not over-read).

### Enhancements Made
- Single citation-metadata correction (Aumann naming). No expansion (hard-ceiling constraint).

### Cross-links
- No additions (length-neutral). Existing wikilinks verified to resolve in prior reviews; the cross-link set is unchanged since 2026-06-03.

## Length / Scorer Guard

`analyze_length` (frontmatter-stripped body): **2999 words**, soft_warning (150% of 2000 target), **1 word clear of the 3000 hard ceiling**. Strictly length-neutral mode enforced throughout — the one edit was net-trimming/neutral. No condense triggered; no expansion attempted; any future addition must offset. Per human-decision-task-mispicked-as-refine, if genuine expansion is ever warranted here it must be diverted to a human length decision, not auto-applied. The budget is justified by the formal/philosophical/phenomenological registers the void spans, each anchored in primary sources.

## Remaining Items

None requiring a follow-on task. Optional future micro-edit (word-neutral): update ref #17 SEP year 2014 → 2022 to match the most recent substantive revision. Not queued (cosmetic, non-load-bearing).

## Stability Notes

The six bedrock disagreements enumerated in the [2026-04-30](/reviews/deep-review-2026-04-30-common-knowledge-void/) and [2026-06-03](/reviews/deep-review-2026-06-03-common-knowledge-void/) reviews stand and must NOT be re-flagged as critical: (1) Carruthers heterophenomenological reading; (2) Madhyamaka emptiness critique; (3) eliminative-materialist "constitutive smoothing is unfalsifiable"; (4) Many-Worlds reading of Aumann; (5) Schelling/Pettit focal-points alternative; (6) Aumann's deliberate demotion to contrast (not third anchor). These are framework-boundary standoffs, not correctable defects.

**New stability note (calibration anchor):** The 2026-06-10 re-scope of the Halpern–Moses claim is the *correct* calibration — HM is NOT a universal impossibility; common knowledge IS generable in idealised public-announcement models (SEP-verified); the embodied-interface coverage is honest extrapolation, explicitly flagged. Future reviews must NOT "tighten" this back to an unqualified "structurally unattainable for finite minds" (the pre-d67673bcb wording) — that would reintroduce an over-read of the theorem. The scoped wording is load-bearing and verified.

## Convergence Declaration

Re-converged after one genuine-drift verification pass. The 2026-06-10 re-scope is verified faithful and is a calibration improvement; one ratified-by-prior-reviews citation-metadata defect (Aumann "paradox" → "problem") was caught only by publisher-of-record web-verification and fixed length-neutrally. All formal anchors verified real-correct at the publisher of record. SEP public-announcement attribution: **real-correct / PRESENT**. Future deep-reviews should require strong new evidence (a published critique, a new formal result, or a substantive Map-internal tenet-treatment change) before flagging issues, and should treat a "no critical issues" finding here as the expected steady state — while preserving the scoped Halpern–Moses calibration intact.