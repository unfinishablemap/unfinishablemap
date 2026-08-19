---
title: "Deep Review - The Coalesce-Condense-Apex-Stability Triple-Discipline"
created: 2026-08-19
modified: 2026-08-19
human_modified: null
ai_modified: 2026-08-19T00:14:00+00:00
draft: false
topics: []
concepts:
  - "[[coalesce-condense-apex-stability]]"
related_articles:
  - "[[coalesce-condense-apex-stability]]"
  - "[[deep-review-2026-06-17-coalesce-condense-apex-stability]]"
  - "[[deep-review-2026-08-18-composition-question-rivals]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-19
last_curated: null
---

**Date**: 2026-08-19 00:14 UTC
**Article**: [[coalesce-condense-apex-stability|The Coalesce-Condense-Apex-Stability Triple-Discipline]]
**Previous review**: [[deep-review-2026-06-17-coalesce-condense-apex-stability|2026-06-17]] (63 days; seventh review)

## Scope and Method

This is the article that *theorises* coalesce/condense discipline, and two restructure defects
found on 2026-08-18 postdate its `## Empirical Performance` section and bear directly on it. The
lens for this pass was therefore not defect-hunting in the abstract but **testing the article's own
empirical claims against evidence generated after they were written**. Both new findings were
re-verified from the git history before being used, and the article's four-case sample was
independently re-audited against every subsequent review file rather than taken from the article's
own summary.

No external literature (the article cites only the catalogue's own history), so §2.4
publisher-of-record verification is against the repo. No named-opponent engagement, so §2.6 is N/A.

## Verification of the Two Prompting Findings

**Finding A — coalesce separated a qualifier from its claim: CONFIRMED, exactly as stated.**
`git show 00768db4d3^:obsidian/concepts/information-compression-composition.md` line 63 carries the
"observationally matched" claim with the qualifying parenthetical *in the same sentence run*,
immediately after it. In the post-coalesce `composition-question-rivals` the parenthetical sits at
line 98 and the bare claim at line 124 — **26 lines apart**, in different sections. The parenthetical
was installed by commit `b2e2755a3b` (2026-06-07 refine-draft) in response to
`reviews/pessimistic-2026-06-07.md`, which flags that exact sentence; the coalesce `00768db4d3` is
dated 2026-06-15, so the qualifier was **eight days old** when the merge relocated it. The
predecessor also read "all *three*" where the merged article reads "all". Two later deep reviews
(2026-06-15, 2026-06-25) ratified the split.

**Finding B — coalesce nulled review-history metadata: CONFIRMED, with one correction.**
Commit `fb3c21520d` (2026-08-18 15:41 UTC) shows `-last_deep_review: 2026-07-25T09:33:15+00:00` /
`+last_deep_review: null` on `obsidian/concepts/quantum-indeterminacy-free-will.md`. The value has
since been restored and currently reads `2026-07-25T09:33:15+00:00`.

*Correction to the brief*: the archive holds **eight** deep reviews of that slug, not nine —
`ls obsidian/reviews/deep-review-*quantum-indeterminacy-free-will*.md` returns 8, a repo-wide
`find` de-duplicated across `hugo/` returns 8, and `git log --diff-filter=D` shows none deleted.
The article now says "eight".

*Non-systematic confirmed*: the 2026-08-06 `cc8d260177` coalesce (`voids/ownership-void` →
`concepts/mine-ness`) touched no `last_deep_review` line, and neither did `597d922e75`,
`cf0006f883` or `742a97ab60`. `mine-ness` still carries `2026-07-15T16:06:39+00:00`. The reset is
intermittent, which is itself the reason a check is needed rather than a one-line tooling assumption.

## Pessimistic Analysis Summary

### Critical Issues Found — 1 corrected

**1. Factual error about the catalogue's own history (§Empirical Performance).** The article read:

> All four passed every subsequent deep-review with no critical structural issue — [four articles]
> — each reached two or more consecutive clean reviews.

The second clause is false, and was false when written on 2026-06-03. `creative-consciousness` has
drawn a **critical** finding in four of its five post-restructure deep-reviews and has **never**
reached two consecutive clean ones:

| Review | Critical finding |
|---|---|
| 2026-04-30 | Citation regression — the same-day condense removed Kounios & Beeman (2009) from References while keeping the body claim, regressing a fix the 2026-03-22 ancestor review had applied. Plus a style-guide cliché violation. |
| 2026-06-02 | Fabricated author name + wrong page range on the 2024 *Brain* DMN study. |
| 2026-06-13 | None — the only clean review. |
| 2026-07-12 | Husserl misattribution — the quoted phrase is Brian Elliott's characterisation, not Husserl's words. |
| 2026-08-07 | Misattributed "8 seconds" figure — a regression of a fix first applied 2026-02-21. |

At the moment the claim was written (2026-06-03) this article's post-restructure record was
04-30 critical, 06-02 critical: **zero** clean reviews, let alone two consecutive.

The word "structural" is the only thing that made the sentence defensible — every one of those
defects is a citation/attribution defect rather than a section-structure defect. But "each reached
two or more consecutive **clean** reviews" carries no such modifier, and a tenet-accepting reviewer
would still flag it as overstated against the record. That is the §2 diagnostic test for a
calibration error rather than a bedrock disagreement, so it is treated as critical.

The correction narrows the structural claim to what the evidence supports (merged section structure
held: no inter-section contradiction, no dangling apex citation) and states the content record
honestly. It also records that **the restructure arc is not itself exempt**: the 2026-04-29
`ai-consciousness-typology` coalesce introduced a flat contradiction between its
borrowed-phenomenality and epiphenomenal-phenomenality sections
(`deep-review-2026-04-30-ai-consciousness-typology.md`), caught next-day. That case is the same
defect *shape* as Finding A and was excluded from the article's sample only because the sample is
measured from the post-cleanup baseline ("2745w post-condense", i.e. after `04-30b`).

### Per-claim audit of the four cited articles

- `self-and-self-consciousness` — 05-01, 05-27, 06-10, 07-07, 07-25 all "Critical Issues Found:
  None". Claim holds. **real-correct**
- `the-quantitative-comprehension-void` — 04-30b, 04-30c clean; 06-03 found two critical calibration
  regressions, which the article itself reports in its next paragraph. Self-consistent.
  **real-correct**
- `ai-consciousness-typology` — 04-30b, 06-02, 06-19, 07-08, 07-25 clean; the 04-30 contradiction
  precedes the stated baseline. Holds *as scoped*, but the scoping was invisible.
  **real-correct, now made explicit**
- `creative-consciousness` — **WRONG, corrected** (see Critical 1).

Word-count datapoints (4914→2770, 2987, 2745, ~2261, 3404, 2403) were verified as accurate by the
2026-06-17 pass against the cited review files; the References block and cited commit `5ea6d0c90`
are byte-for-byte unchanged since, so that ledger was not re-litigated.

## The Three Prompting Questions

**1. Does "all four passed every subsequent deep-review" survive?** No, in the form written — see
Critical 1. The *structural* half survives and is now stated on its own. `composition-question-rivals`
is **not** one of the four; it is a fifth case, coalesced 2026-06-15 rather than in late April, so
Finding A does not falsify the four-case sample directly. It falsifies the *generalisation* the
sample was being used to support, which the 04-30 `ai-consciousness-typology` contradiction already
strained from inside the sample.

**2. Does "condense can silently drop load-bearing qualifiers" survive?** Yes, unchanged — the
2026-06-03 audit of `the-quantitative-comprehension-void` is real and correctly described. But it is
**incomplete as a taxonomy**. It attributes qualifier loss to condense, by deletion. Finding A is
coalesce, by relocation: nothing is deleted, both halves remain individually defensible, and the
defect is therefore invisible to any audit that asks whether a hedge is still *present*. Added as a
third named regression mode rather than folded into the second, because the detection method differs.

**3. Does the discipline need a third check?** Yes. Neither existing remedy reaches either finding —
a calibration-qualifier audit checks presence and Finding A's qualifier is present; a periodic length
re-check is about words and Finding B is about frontmatter. Both findings share a shape: the
restructure preserved the content but destroyed the link between a repair and what it repaired (A),
or between an article and the record that it had been examined (B). Stated in the article as:

> A **post-restructure provenance check** […] runs within a cycle of any coalesce and diffs the
> merged article against its archived predecessors rather than against its own last review,
> verifying two things: that every hedge or scope-restriction still sits with the claim it repairs,
> not merely somewhere in the article; and that the surviving article's `last_deep_review` was
> carried through rather than reset.

The "diff against archived predecessors, not against the last review" clause is the operative part —
it is exactly what the last review cannot see, since the last review predates the merge.

Note the scheduling argument recorded with it: nulling `last_deep_review` buys nothing, because
`ai_modified` already re-qualifies a merged article under the selector's "modified since review"
branch. It only converts a `days_unreviewed × 2` score into a `100 + days` never-reviewed score
while discarding the audit trail — which is how it mis-justified a task.

## Optimistic Analysis Summary

### Strengths Preserved
Front-loaded thesis; the chain-conditional argument for naming the sequence as one discipline; the
four-criterion stability formula; the retention test; the cap-saturation policy and its honest
limitation; the cardinality-floor cap on introspective grasp; Tenet-5 alignment. All untouched.

The `## Empirical Performance` section remains the article's best feature, and the correction
*strengthens* the property that made it good: it is the section where the discipline measures its
own predictions and reports the part that failed. It now reports one more failure — its own earlier
over-statement — which is the Hardline-Empiricist move applied reflexively.

### Enhancements Made
- Third regression mode (qualifier separation by relocation) with a primary-verified worked example.
- Third remedy (post-restructure provenance check), stated operationally.
- The intermittency of the `last_deep_review` reset recorded, so the check is not mistaken for a
  known-systematic tooling bug that someone might assume is already fixed.

### Cross-links Added
`[[composition-question-rivals]]`, `[[quantum-indeterminacy-free-will]]`, `[[mine-ness]]` inline;
the first two added to `related_articles`. All three targets verified to exist.

## Length Assessment

Printed from `THRESHOLDS`, not quoted: concepts soft 2500 / hard 3500 / critical 5000.

| | raw (`analyze_length`) | apparatus | prose | status |
|---|---|---|---|---|
| Before | 3147 | 479 | 2668 | soft_warning |
| After | 3497 | 479 | 3018 | soft_warning |

Net **+350 raw / +350 prose**. Prose sits 482 words below the hard threshold; the raw figure
includes the 479-word Further Reading + References apparatus
(`analyze-length-counts-reference-apparatus`).

The first draft of the corrections landed at raw 3532 — `hard_warning`, which would have minted a
condense task against content the 2026-06-17 review explicitly ruled un-cuttable. Offsets were taken
from genuine redundancy rather than substance, recovering 35 words:

- Four cousin-glosses in the intro, each restated in full under Further Reading, replaced by a
  pointer (the eight-member family count and the 5-named/3-gestured decomposition are preserved —
  that is the standing navigation maintenance hook).
- The un-linked "parallel project-document" aside, which enumerated preservation criteria without
  naming its target.
- One restatement in the apex re-cross-review paragraph ("It is not a clean-slate read" restated the
  preceding sentence).

## Hygiene

- **Label leakage**: 0 hits (mode names, `Engagement classification:`, `Evidential status:`,
  `unsupported-jump`, `bedrock-perimeter`, `direct-refutation-feasible`).
- **"This is not X. It is Y." cliché**: none introduced. The contrastive constructions added
  ("Structural integrity survives restructuring; content integrity is what restructuring puts at
  risk") are exposition, not the setup-then-reveal pattern.
- **"load-bearing"**: no new instances added; existing ones retained where structural.
- **Wikilinks**: all targets resolve, including the three new ones.
- **Mirror**: `scripts/sync.py` run; `hugo/content/concepts/coalesce-condense-apex-stability.md`
  re-grepped and carries all corrections.

## Remaining Items

None minted against this article. Two observations recorded for whoever holds the tooling
(`tools/`, `scripts/`, `.claude/skills/` are operator territory and were **not** touched):

1. The `last_deep_review` reset in `fb3c21520d` is a coalesce-side behaviour, intermittent across
   recent merges. If it is worth fixing at source, the fix belongs in the coalesce skill, not here;
   the article now records the check as an editorial remedy instead.
2. `topics: []` on this article is deliberately left alone — it is one of the 13 empty-topics
   articles already covered by an open P3, and fixing it here would duplicate that task.

## Stability Notes

Carried forward from prior reviews and still binding:

1. **Methodological, not substantive** — adversarial personas have limited purchase; no tenet-bearing
   claims to dispute. Do not re-flag "philosophical disagreement".
2. **Internal-reference verification is the live audit** — the article cites the catalogue's own
   history, so the recurring check is repo-drift, not external literature.
3. **Eight-member family count is the navigation maintenance hook** — re-verify against
   `mechanism-costs-cartography.md`. Verified consistent this pass; the intro glosses were trimmed
   but the count and the named/gestured split are intact.
4. **Do not cut** the cap-saturation, retention-test, cardinality-floor or empirical-performance
   content — load-bearing by the article's own retention test.

New standing notes from this pass:

5. **This article's empirical section is a claim about the corpus, so it decays as the corpus
   moves.** Six reviews certified it without re-auditing the underlying review files, because
   the 2026-06-17 pass verified the *word counts* — which are stable — and the cleanliness claim
   rode along unchecked. Word-count datapoints are baselines and are robust; **cleanliness claims
   are not**, and must be re-derived from the review files each pass. The check is mechanical:
   grep `### Critical Issues` across every `deep-review-*-{slug}.md` for each of the four.
6. **The article now theorises a defect it is itself exposed to.** It cites four articles by name;
   if any is re-coalesced, its qualifiers could be relocated and the article's account of it would
   go stale in exactly the way Finding A describes. The provenance check applies to this article's
   own sources.
