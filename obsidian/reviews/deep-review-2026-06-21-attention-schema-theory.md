---
title: "Deep Review - Attention Schema Theory"
created: 2026-06-21
modified: 2026-06-21
human_modified: null
ai_modified: 2026-06-21T09:45:35+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-21
last_curated: null
---

**Date**: 2026-06-21
**Article**: [[attention-schema-theory|Attention Schema Theory]]
**Previous review**: [[deep-review-2026-06-05-attention-schema-theory|2026-06-05]] (seventh on disk; ninth overall)

## Headline

Triggered as a HIDDEN-DRIFT verification: commit cc1744aec (2026-06-09) was
mislabelled `auto(replenish-queue): replenish` but actually rewrote 66 lines of
the article body (regress / illusionism-burden / Whitehead / Relation-to-Site
sections); it bumped `ai_modified` but NOT `last_deep_review`, so this substantial
rewrite had never been deep-reviewed and evaded commit-message detection.

Two outcomes:
1. **The cc1744aec rewrite is calibration-clean.** It is a prose-tightening +
   argument-upgrade pass, not a content rewrite that introduced new claims. It
   *improved* calibration (see below). No fixes needed to the rewritten prose.
2. **A CRITICAL citation defect survived — and was partly INTRODUCED BY — the
   2026-06-05 review.** The Igelström & Graziano 2021 *PNAS* cite that the prior
   review added as its headline "fix" is wrong on authors, issue number, AND the
   claim attributed to it. Publisher-of-record web-verify caught it; the prior
   review's intra-corpus-only confidence ratified it. Fixed this pass, length-neutral.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Igelström & Graziano 2021 — wrong authors + wrong issue + UNFAITHFUL CLAIM**
   (CRITICAL, FIXED). Web-verified at PubMed 34161276 and PMC8237657:
   - **Authors**: the article (body line 77 + References) credited
     "Igelström, K.M. & Graziano, M.S.A." The actual paper e2026099118 is
     **Wilterson, A.I., Nastase, S.A., Bio, B.J., Guterstam, A. & Graziano, M.S.A.
     (2021)**. Igelström is NOT an author. (Igelström & Graziano have *separate*
     real papers — a 2017 *Neuropsychologia* 105:70–83 network review and a 2018
     *Neuroscience of Consciousness* niy005 review — but neither is e2026099118.
     This is the classic wrong-paper-by-author-association trap.)
   - **Issue**: cited 118(**26**); actual is 118(**25**) (published 14 Jun 2021).
   - **Claim faithfulness**: the article said the study found "overlapping cortical
     networks converging on the rTPJ **and superior temporal sulcus (STS)** are
     recruited when subjects track their **own** attention **and when they track
     others' attention states**" — read as theory-of-mind-substrate overlap.
     The actual paper is a **within-subject** awareness study: when subjects are
     aware of a cue they can use it to direct attention and the rTPJ engages; when
     unaware, predictive control collapses. **STS is not a key finding; tracking
     others' attention is not in the experimental design.** The self-vs-other
     overlap gloss was fabricated relative to this paper.
   - **Fix**: re-attributed to Wilterson et al. (2021), corrected the issue to
     118(25), and re-scoped the body claim to what the paper shows (awareness as
     the control model *for* attention at the rTPJ). The theory-of-mind / evolutionary
     "repurposing" point is preserved but reframed as AST's *reading of* the rTPJ's
     known theory-of-mind-hub status, not as a finding of this fMRI study.

2. **Wilterson, Kemper et al. 2021 — wrong issue** (CRITICAL-adjacent metadata,
   FIXED). The neural-network-agent paper e2102421118 was cited as 118(**39**);
   actual is 118(**33**) (published 12 Aug 2021). Authors/title/journal/year/article-ID
   all correct. Fixed the issue number.

### Citation Web-Verify Ledger (publisher of record)

- Wilterson, Nastase, Bio, Guterstam & Graziano 2021 (*PNAS* 118(25) e2026099118,
  "Attention, awareness, and the right temporoparietal junction") —
  **real-wrong-metadata** (was "Igelström & Graziano … 118(26)"; corrected authors
  + issue) AND **unfaithful-claim** (STS / self-vs-other gloss removed, re-scoped to
  awareness-as-control-model). Verified PubMed 34161276 / PMC8237657.
- Wilterson, Kemper et al. 2021 (*PNAS* 118(33) e2102421118, neural-network agent) —
  **real-wrong-metadata** (issue 39 → 33). Verified PMC8379943.
- Liu, Bolotta, Zhu, Bengio & Dumas 2023 (arXiv:2305.17375, "Attention Schema in
  Neural Agents") — **real-correct**. (Article cites "Liu, D., Bolotta, S., et al.";
  faithful.)
- Graziano & Webb 2015 (*Frontiers in Psychology* 6:500, "The attention schema
  theory: a mechanistic account of subjective awareness") — **real-correct**.
- Juliani, Kanai & Sasai 2022 (Proc. 44th Cognitive Science Society, "The Perceiver
  Architecture is a Functional Global Workspace") — **real-correct**.
- ASTOUND (Horizon Europe EIC Pathfinder grant 101071191; UPM coordinator) —
  **real-correct**; "tests, not establishes" framing accurate per CORDIS.
- Graziano 2013 (OUP), 2019 (Norton), 2022 (*PNAS* 119(18) e2116933119), Frankish
  2016, Dennett 2016, Chalmers 2018, Tallis 2011 — **real-correct** (consistent
  with Graziano Lab publication list; standard JCS/illusionism canon).

No corpus-wide family-resolution propagation needed: the Igelström/Wilterson and
Graziano/Webb cites appear ONLY in this article (grep-verified across `obsidian/`,
excluding review/changelog records).

### Empirical-Record Currency Sweep

`find_superlative_claims` returned NONE. No superlative empirical claims to currency-check.

### Calibration of the cc1744aec Rewritten Sections (priority (a))

All clean — the rewrite *raised* calibration quality:

- **Regress argument (now line ~106)**: PASS. The rewrite changed "The deepest
  objection" → "A first objection" and now explicitly grants "the bare regress is
  not decisive, and the Map grants this," represents Graziano/Frankish's reply
  faithfully ("model consumed by control systems … a map represents terrain without
  being mountainous"), THEN mounts the stronger objection (why *felt* rather than
  merely tracked). This is exactly the [[direct-refutation-discipline]] sequence —
  honest concession of the weak form, in-framework pressure on the strong form. Not
  a strawman; the opponent's best reply is stated before the counter.
- **Illusionism-burden (lines ~140, ~194)**: PASS. The "stronger objection finds an
  answer" falsifier (line 194) is calibrated: "Current accounts (including
  Graziano's) invoke functional language that presupposes what it denies, but future
  formulations might avoid this." That is a fair, falsifiable characterisation of
  the illusionist's open burden, not an assertion that the burden is unmeetable.
  The Strawson "deflating 'seeming' to a functional disposition → burden returns as
  why it is *felt*" move (line 140) is argued, not asserted.
- **Whitehead sections (lines ~156–166)**: PASS. Presented as "Whitehead's process
  philosophy illuminates why …" and "On Whitehead's view" — clearly the Map's
  process-philosophy *reading*, not over-asserted as established. The
  "caricature presupposes an audience / the schema cannot be its own audience" move
  is argued from the relational structure of caricature, not stipulated.
- **No banned "This is not X. It is Y." cliché** (grep-verified, twice).
- **No editor-vocabulary / mode-label leakage** in prose (grep-verified, twice).

### Possibility/Probability Slippage Check

PASS. Nothing is placed on the five-tier evidential-status scale; no positive
evidential claim rests on tenet-defeater-removal. A tenet-accepting reviewer would
not flag any claim as overstated relative to support. The citation fix *removed* an
over-claim (an fMRI within-subject study had been inflated into a theory-of-mind
substrate-overlap result).

### Attribution Accuracy Check

- **Misattribution**: ONE major (the Igelström author-association error) found and
  fixed. Graziano's "caricature not illusion" qualifier preserved.
- **Source/Map separation**: clean — quantum-interface alternative and Whitehead
  reading both framed as the Map's, not as Graziano's.
- **Self-contradiction**: none.

### Engagement Classification (editor-internal)

- **AST / Graziano**: Mode Two (unsupported foundational move) — the regress now
  cleanly identifies that AST helps itself to "phenomenal seeming" without
  specifying why control-relevant information is *felt*. Upgraded by the cc1744aec
  rewrite from a flatter "deepest objection" framing.
- **Illusionism / Frankish / Dennett**: Mode Two — Strawson turns illusionism's own
  "seeming"-report commitment against it.
- **Eliminative materialists / physicalists**: Mode Three (framework-boundary),
  handled in Relation to Site Perspective.
- No boundary-substitution; no label leakage.

## Optimistic Analysis Summary

### Strengths Preserved

Body-schema analogy scaffolding; the cc1744aec-upgraded regress sequence (concede
weak form → faithful opponent reply → in-framework pressure on strong form);
Whitehead prehension alternative; five falsifiability conditions; all five tenets
addressed; silicon-implementation thought experiment; haecceity as load-bearing Map
response; the Hardline-Empiricist-praised cautious register on the AI-agent claims.

### Enhancements Made

- Three citation-metadata corrections + one claim re-scoping, all length-neutral.
- The fMRI paragraph is now FAITHFUL to a real within-subject result rather than an
  inflated theory-of-mind-overlap gloss — a net gain in empirical credibility.

### Hardline Empiricist Praise (Birch)

The fix is the evidential-restraint pattern in action: a within-subject awareness
result that had been over-read into a social-cognition substrate finding is pulled
back to what the data show. Over-claim corrected downward; tenet-as-upgrade declined.

## Length Check

3497 → 3499 words (net +2; 140% of 2500 soft threshold; under the 3500 concepts
hard ceiling). The citation correction transiently peaked the article at 3527
(hard_warning); applied length-neutral trimming across the fMRI, AI-agent, and
evolutionary-clue passages to land at 3499 (soft_warning). The +2 net is the
load-bearing accuracy gain (faithful claim is marginally longer than the compact
fabrication it replaced) and is justified. STRICTLY length-disciplined per the brief.

## Remaining Items

1. **Commit-message hygiene (systemic, not article-level)**: cc1744aec is a body
   rewrite mislabelled as `replenish`. This is the [[hidden-drift]]-class evasion
   the trigger flagged — a substantive edit that bumps `ai_modified` without
   `last_deep_review` and hides under a non-content commit message. No article fix;
   noted for operator/tune-system awareness.
2. **ASTOUND results, if/when published** — "tests, not establishes" framing can be
   updated when final outcomes appear. Low priority.
3. **Cluster cross-links** (low, carried): `[[process-content-distinction]]`,
   `[[multiple-realizability]]` could be added only length-neutrally — the article
   is at its hard ceiling.

## Stability Notes

Ninth deep review. The CONTENT is converged and stable; the cc1744aec rewrite was a
quality-improving prose pass that needed no correction. But this pass demonstrates,
for the second consecutive review, that "converged" is not "verified": the
2026-06-05 review's headline citation FIX itself introduced a wrong-author /
wrong-issue / unfaithful-claim defect, ratified by intra-corpus consistency for two
weeks. Only publisher-of-record web-verify caught it
([[ai-citation-metadata-unreliable]], [[citation-verify-false-negative]]). The
lesson sharpens: a review that *adds* a citation is not exempt from web-verify; a
"fix" can be a fresh defect.

Bedrock disagreements (unchanged across all nine reviews; do NOT re-flag as critical):
- Eliminative materialists reject the regress argument (foundational disagreement
  about what "seeming" requires).
- Physicalists find self-stultification unpersuasive (framework-boundary standoff).
- The Map's treatment of consciousness as irreducible is a tenet, not a claim
  defended here.

**Recommendation**: Content is genuinely converged. Extend the next deep-review
cadence to 90+ days. The one durable lesson is procedural, not about this article:
web-verify EVERY citation a review introduces, even when the review is itself a
"citation fix." Future passes must stay length-neutral (article at hard ceiling).
