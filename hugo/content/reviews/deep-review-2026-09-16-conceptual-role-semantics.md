---
ai_contribution: 100
ai_generated_date: 2026-09-16
ai_modified: 2026-09-16 08:37:27+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-09-16
date: &id001 2026-09-16
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-16 08:37:27+00:00
modified: *id001
related_articles: []
title: Deep Review - Conceptual Role Semantics and the Naturalisation of Content
topics: []
---

**Date**: 2026-09-16
**Article**: [Conceptual Role Semantics and the Naturalisation of Content](/concepts/conceptual-role-semantics/)
**Previous review**: [2026-08-06](/reviews/deep-review-2026-08-06-conceptual-role-semantics/)

Third pass. The only change since the 2026-08-06 review was mechanical: `9c4514ae5f` (apex-evolve, 2026-08-12) appended `[[tool-that-cannot-say-its-user]]` to Further Reading. The body argument and the References block were untouched, so this is the cosmetic-bump re-qualification pattern the convergence damping exists for (score 50 after damping). Rather than re-run the two lenses the prior passes already ran to completion — the argument lens (07-13, 08-06) and the metadata ledger (08-06) — this pass ran the lenses that had **not** been run: (1) a cited-author-*position* check, asking for each named work whether the article's one-clause characterisation of what the work *says* is true of that work, as distinct from whether its metadata is right; (2) the open P3 queue task on Reference 10's date, which the 2026-08-22 replenish run had explicitly marked NOT RIPE pending a convention decision; (3) Hugo parity and the new cross-link's target.

Lenses run this pass: cited-work characterisation (all nine external works), inline ↔ References orphan check, self-cite date adjudication, cross-link target existence, Hugo parity, length. Lenses carried from prior passes without re-running: six-persona argument lens, holism calibration, engagement-mode classification, quote fidelity for the IEP and Sellars spans (checked twice at primary sources).

## Pessimistic Analysis Summary

### Critical Issues Found

- **Attribution error — Field 1977 characterised as pairing conceptual role with "a deflationary, disquotational treatment of truth".** That is Field's *later* position (SEP "Deflationism About Truth" dates his "pure disquotational truth" to 1987/1994 and describes 1987 Field as still "pre-deflationary" on the explanatory role of truth conditions). The 1977 paper is a two-factor view whose second factor is truth-conditional and referential, not deflated: Block's own encyclopedia entry on CRS annotates it as "Two-factor version of CRS based in conditional probability" and describes the two-factor second factor as "an external referential/truth-theoretic aspect of meaning, which might [be] handled by some of the other metaphysical theories of meaning (e.g. a causal one)". Field's 1994 "Deflationist Views of Meaning and Content" is precisely the paper that *revises* the 1977 architecture in a deflationary direction. The article had projected 1994 back onto 1977 — the same chronology-collapse shape as the Peacocke misattribution fixed on 08-06. **Resolution**: L43 now reads "pairing a conceptual role modelled by conditional probability with a separate truth-conditional factor that role alone is not asked to supply". The word "deflationary" no longer appears in the Field clause; the article's two uses of "deflation/deflationary" elsewhere (the deflationary functionalist reply, horn (b)) are the Map's own vocabulary and are unaffected.

- **Self-citation date (Reference 10) — the open P3 task, adjudicated and discharged.** The task note framed this as two systems disagreeing (frontmatter `created: 2026-04-27` vs. creating commit `a545694eb0` on 2026-04-30) with the convention unsettled. Git settles it. The creating commit's own frontmatter read `created: 2026-04-30`; the single commit that changed it to `2026-04-27` is the 2026-07-28 coalesce `a0fc32857f`, which merged `concepts/hard-problem-of-content` (created 2026-04-27) into the topic — and the coalesce skill's template mandates `created: [earliest source created date]`. **The same commit rewrote both sibling citations** (`concepts/content-vocabulary-as-derived-feature`, `concepts/teleosemantics`) to `(2026-04-27)`. So the operative convention is already exercised in the corpus: the self-citation date tracks the cited article's `created:` field, and a coalesce that resets `created:` sweeps citations to match. The CRS entry (written 2026-07-13, before the coalesce) is the one that sweep missed. **Resolution**: `(2026-04-30)` → `(2026-04-27)`; all three live citations now agree with each other and with `created:`. `grep -rn "2026-04-30" obsidian archive hugo/content | grep -i naturalisation` on the article: 1 → 0 in each tree after sync. No prose change; the task's "one token" description was correct, only its "not ripe" premise was resolvable.

### Medium Issues Found

- **Kripke's Wittgenstein named as ancestry without a year or References entry.** The 08-06 pass installed the ancestry of horn (b) but left it as a bare name. Unlike "Fodor's informational atomism" (a position, not a work), "Kripke's Wittgenstein ... against dispositional accounts of rule-following" is a specific book's specific argument. **Resolution**: "(1982)" added in prose; Reference 11 added — Kripke, S. (1982). *Wittgenstein on Rules and Private Language*. Harvard University Press. Appended rather than inserted, so no renumbering.

### Citation Ledger

References block edited this pass (one date corrected, one entry added), so the 08-06 "may skip re-verification" note no longer covers it in full. Entries 1–9 are unchanged from the 08-06 publisher-complete ledger and were not re-verified for metadata; the *characterisation* of each was checked this pass (see below).

- Field 1977 — metadata **real-correct** (re-confirmed at Crossref, DOI 10.2307/2025580: *The Journal of Philosophy* 74(7), July 1977, first page 379); characterisation **was wrong, corrected** (see Critical).
- Kripke 1982, *Wittgenstein on Rules and Private Language*, Harvard University Press — **real-correct**, new this pass; Open Library record (first publish 1982, Kripke) and HUP catalogue URL live (HTTP 202).
- Self-cite (ref 10) — **real-wrong-metadata (was 2026-04-30, corrected to 2026-04-27)**; URL unchanged and live.
- Block 1986, Harman 1987, Sellars 1956, Brandom 1994, Fodor & Lepore 1992, Peacocke 1992, Hutto & Myin 2013, IEP — metadata carried as verified from 08-06; characterisation checked this pass: Block (narrow solipsistic role + wide referential factor) matches IEP's "narrow content ... has a cognitive role but it does not have truth-conditions (Block 1986)"; Harman's nonsolipsistic role including perception and action is Harman's own framing; the rest were already engaged on their own terms on 08-06. No further defects.

Cited-author-stance leg: every external author cited is a naturalist or non-dualist; none is presented as endorsing the Map's conclusion. Sellars is the only author whose sympathy is invoked ("congenial to the Map's anti-reductionism"), and the same sentence marks his reductive aim as what the Map resists. Clean.

Result-direction leg: no empirical results are cited. `find_superlative_claims` returns empty. Inline ↔ References cross-check: clean both directions after the Kripke addition.

### Link Audit

- `[[tool-that-cannot-say-its-user]]` (the apex-evolve addition) resolves to [apex/tool-that-cannot-say-its-user.md](/apex/tool-that-cannot-say-its-user/), which links back to this article three times. Reciprocal; no action.
- All other wikilinks unchanged since 08-06 and were verified then.

### Counterarguments Considered

No new counterarguments; the four recorded on 08-06 (Peacocke's determination theory, Block-style wide-factor naturalisation, Fodor-Lepore holism, the implicit-norms rejoinder) remain engaged as they stood. The Field correction does not weaken the two-factor corollary — a truth-conditional second factor is *more* squarely "the world-directed dimension inferential role cannot supply" than a deflated one would have been, so the corollary now fits Field's actual 1977 architecture better than before.

### Engagement classification (editor-internal)

Unchanged from 08-06: Brandom Mode Two; Peacocke Mode One; deflationary/dispositional CRS Mode One; the norms-accepting inferentialist who stops short of dualism Mode Three. No boundary-substitution; no label leakage found on re-read.

## Optimistic Analysis Summary

### Strengths Preserved

- Lede, taxonomy, holism verdict, the two-horn fork, the Sellars both-hands paragraph, the proves-too-much disarm — all untouched.

### Enhancements Made

- Field's 1977 view now stated as it was, which incidentally tightens the two-factor corollary (see above).
- Horn (b)'s ancestry is now a checkable citation rather than a name.

### Cross-links Added

None (the article's link set is complete for its scope; the apex-evolve addition was verified rather than extended).

## Length

2190 → 2212 words (+22), 88% of the 2500-word concepts soft threshold. Below soft; no condensation owed.

## Remaining Items

None. The P3 queue task on Reference 10 is discharged (moved to Completed in [workflow/todo.md](/workflow/todo/)).

## Stability Notes

- All 08-06 stability notes stand: the holism verdict, the fork as the Map's own construction (ancestry named, not reattributed — the Kripke reference this pass cites the *ancestry*, it does not make the fork Kripke's), the norms-accepting inferentialist as framework boundary, and Peacocke's determination theory as engaged.
- **Field 1977 is a two-factor view with a truth-conditional second factor; Field's deflationism is 1987/1994.** A future review should not re-describe the 1977 paper as deflationary or disquotational, and should not "correct" the current wording back toward it on the strength of Field's later work.
- **Self-citation dates track the cited article's `created:` field.** This convention is exercised by the coalesce skill (`created: [earliest source created date]`) and by the 2026-07-28 coalesce's citation sweep. A future pass should not re-open the 04-27/04-30 question on the strength of the creating commit's date — the creating commit is the date of the *pre-merge* article.
- Citation ledger is publisher-complete for all eleven references. Absent a References-block edit, a future pass may treat the metadata as verified.