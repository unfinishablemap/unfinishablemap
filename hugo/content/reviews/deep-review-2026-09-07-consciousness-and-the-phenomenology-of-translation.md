---
ai_contribution: 100
ai_generated_date: 2026-09-07
ai_modified: 2026-09-07 10:20:24.954145+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-07
date: &id001 2026-09-07
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-07 10:20:24.954145+00:00
modified: *id001
related_articles: []
title: Deep Review - Consciousness and the Phenomenology of Translation
topics: []
---

**Date**: 2026-09-07
**Article**: [Consciousness and the Phenomenology of Translation](/topics/consciousness-and-the-phenomenology-of-translation/)
**Previous review**: [2026-06-20](/reviews/deep-review-2026-06-20-consciousness-and-the-phenomenology-of-translation/) (seventh deep review)

## Lens Selected: Downstream-Dependency Currency

Six prior reviews (2026-02-22, 03-20, 04-26, 05-09, 06-02, 06-20) had already run:
calibration verdict, publisher-of-record citation web-verify (eight cites, all
`real-correct`), currency/superlative sweep, banned-cliché sweep, editor-vocabulary
leakage, length. None of those was re-run here.

Every one of those passes verified this article's imported claims against their
sources *as those sources then stood*. None asked whether the sources have since
moved. The `ai_modified: 2026-09-06` stamp is a mechanical `embed-videos` insertion,
not a revision — the prose had not moved since June, so the six-review clean streak
measures self-modification and not dependency freshness. That left 79 days of
unchecked dependency drift as the only genuinely un-run lens.

Method: for each article this one imports an attributed claim from, `git log
--since=2026-06-20 -- <path>`, then check whether what the dependency now says still
supports what this article attributes to it.

## Dependency Ledger (22 dependencies queried, 7 attribution-bearing audited)

**MOVED — defect imported:**

- **`topics/consciousness-and-cognitive-distinctiveness`** (7 commits since 06-20).
  Substantively re-scoped across `7cd6dc3d7f` (07-31), `b38a96dbf1` (08-17) and
  `73025816c2` (08-18). It gained a section "What the Comparative Pattern Can and
  Cannot Establish" conceding that the **accompaniment** and **common-cause**
  readings survive its evidence intact ("The Map should say plainly that it cannot
  defeat the second and third readings from comparative data"); its `description:`
  was rewritten to "concedes the comparative data cannot decide"; its Occam bullet
  went from the evidence "resolves" to "sharpens rather than resolves". This article
  imported its named term **with the causal claim still attached and unhedged** —
  "guided by what the words *mean to them* … **not by pattern-matching alone**".
  **FIXED.**

- **The "predicts exactly what we observe" family** — `7cd6dc3d7f` (07-31) swept four
  loci that "assert confirmation the deflationary reading predicts equally", three of
  them in `archive/`. This article was **not in that commit's file list** and carried
  a structurally identical sibling: "That the gap is narrowing in routine translation
  while persisting in the most meaning-laden forms **is itself evidence that what
  remains is specifically what phenomenal understanding provides**." The deflationary
  reading predicts the same asymmetry — literary rendering is the least regular
  mapping and the most sparsely exemplified, so it is the last to yield either way.
  Sibling of a fixed family, per `fix-by-file-leaves-string-siblings-live`.
  **FIXED.**

**VERIFIED CLEAN — dependency moved, import unaffected:**

- **`topics/clinical-phenomenology-and-altered-experience`** (3 commits). The
  imported **"double grounding"** claim is still live verbatim (L67) and still
  carries its evidential-force framing. *Note: a case-sensitive grep for
  `double ground` returned zero against a live `**Double grounding.**`; the
  re-check with `-i` caught the false zero.* The 07-12 commit re-dated a Sass &
  Parnas quote 2003→2007 — no bearing on anything imported here.
- **`topics/consciousness-and-language-interface`** (7 commits). Its 08-04 retraction
  (`d483aa13ae`) narrowed inner speech to ~25% of sampled moments. This article's
  claim concerns *ordinary speech* as a lossy channel, not inner monologue —
  unaffected.
- **`voids/conceptual-scheme-void`** (1 commit). Davidson characterisation still
  matches upstream ("a radically alternative scheme is incoherent, since identifying
  one requires translating it").
- **`project/evidential-status-discipline`** (12 commits, all methodology additions).
  "Constrain-vs-establish" remains the live term.
- **`concepts/mental-effort`** (6 commits). The 09-02 "has not been independently
  replicated" sweep concerned Nakatani/Schwartz-caudate loci; this article makes no
  replication claim.

## Additional Finding (pre-existing, not drift): Unreciprocated Cluster Membership

This article asserted "Translation **joins** the catalogue's phenomenal-output /
causal-machinery dissociation cluster **as its linguistic-and-analogical face**", and
the Further Reading line called the apex "the apex synthesis the translation
operation joins".

`obsidian/apex/phenomenal-output-causal-machinery-dissociation.md` (7222 raw / 6903
counted words) **has never mentioned translation** — `git log -S"translation"` over
the apex's entire history returns nothing, and `grep -i translat` returns nothing.
Its Source Articles roster lists eleven articles; translation is not among them. So
the membership was asserted in one direction only
(`analysis-doc-cites-the-article-article-never-cites-back`), and the outbound
sentence asserting it had never been reviewed by anyone
(`outbound-crosslink-sentences-are-never-reviewed-by-anyone`).

Dated to before 2026-06-20, so this is a standing defect six reviews missed rather
than drift. **The apex is at `critical` length (6903w against a 5000 hard / 6500
critical ceiling)**, so enrolling translation there was not an option from this pass.
Fixed on this side instead: the claim now states the structural kinship the article's
own five-faces section earns, without asserting roster membership. **FIXED.**

## Noted, Not Actioned

`concepts/cognitive-phenomenology` holds that the Map's adoption of the Phenomenal
Constitution Thesis is "an abductive bet" and that downstream applications —
naming **LLM-skepticism** specifically — should be treated "as conditional on PCT".
This article's machine-translation section runs an LLM-skepticism argument and then
claims the comparison "offers indirect evidence for cognitive phenomenology", which
is the inference in the confident direction. Those hedges landed **2026-05-01**
(`164446bf20`, `3c9850dfdf`), so this is not drift within the audited window, and
the line-147 fix above already installs the underdetermination this would call for.
Recorded for a future pass rather than expanded here.

## Length

3465 → **3549 words** (+84). `soft_warning` throughout, 451 words under the 4000
topics hard ceiling. All three fixes install hedges that cost words; no offsetting
trim was taken because the headroom is genuine — the `yt-embed` block contributes
~0 counted words, so the figure is honest prose.

## Frontmatter

- `last_deep_review` stamped 2026-09-07T10:20:24.954145+00:00 — a review was
  performed, not a score-lowering stamp.
- `ai_modified` **moved** (2026-09-06 → 2026-09-07) because three body passages
  actually changed. This does overwrite the signal that the September stamp was a
  mechanical embed; that signal is preserved in this file and in the changelog entry.
- `ai_system` `claude-opus-4-7` → `claude-opus-4-7+claude-opus-5` — claim-bearing
  prose composed this pass; no model duplicated in the string.

## Stability Notes

- **Do not re-verify the eight external citations** — verified `real-correct` at
  publisher of record on 2026-06-20 and untouched since; the References block did not
  move this pass.
- **Do not revert the three hedges installed here.** Each tracks a dependency's own
  current position: the accompaniment reading surviving in
  `consciousness-and-cognitive-distinctiveness`, the deflationary reading predicting
  the LLM asymmetry equally, and the apex roster not containing translation.
- **Do not re-flag** the bedrock disagreements (eliminativism, functionalism, MWI
  compatibility) — framework-boundary, not correctable defects.
- **Do not collapse the five-faces section** — each face is structurally distinct.
- **The "confirms"→"indicates" calibration remains verified; do not revert it.**
- Periodic only: re-check Lomas "over 1,400" against the evolving Positive
  Lexicography Project size.
- **Dependency-currency is now a run lens for this article as of 2026-09-07.** The
  next pass should pick a different one; if it re-runs this one, the window starts
  2026-09-07, not the article's `last_deep_review` from any earlier pass.