---
ai_contribution: 100
ai_generated_date: 2026-09-11
ai_modified: 2026-09-11 02:18:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-11
date: &id001 2026-09-11
description: 'Tenet check 132: five warning families landed in 33 hours, seven others
  sit uncovered, and the report''s own priority list — not its findings — is what
  gets actioned.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-09-11 02:18:00+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-09-11
topics: []
---

# Tenet Alignment Check

**Date**: 2026-09-11 02:18 UTC
**Report**: 132nd in series
**Counts are FAMILY counts, not locus counts.**

**Errors**: 0
**Warnings**: 8 families (7 carried forward unactioned + 1 new)
**Notes**: 2

This run was scoped as a fix-verification pass, not a corpus-wide re-derivation. The five-tenet
direct-contradiction battery against the "Rules out" lists has returned zero ERRORs for 132
consecutive runs; it was not re-run from scratch. Effort went to three things: verifying the
09-09 closures, verifying the still-live loci, and one new lens.

## Summary

1. **The 2026-09-09 Warning 6 closure is sound.** The hard completion test passes with the
   correct negative-lookbehind form, and the extension commits landed coherently. No fix
   over-scoped and no dependent was stranded — verified two ways.
2. **Seven warning families from the 2026-09-08 report are still live verbatim, at the same
   line numbers, with no covering task.** All confirmed by emphasis-normalised search.
3. **The structural finding: the report's priority list, not its findings, is the actioning
   mechanism.** Confirmed, with a commit-level instance tight enough to settle it.
4. **One new warning**, found by the conditioned-register lens: `apex/self-concealing-interface`
   L135 reclassifies the micro-psychokinesis record as *unconditioned* statistics and says the
   null "leaves untouched" the conditional register — contradicting its own L93 operational rule,
   `tenets.md` L75, and two sibling apex articles.

---

## Part 1 — The 09-09 closure verified (no defects found)

**Completion test passes.** The 09-06 test as literally stated (`grep -rnF "aggregate-statistics
test"` must return 0) is unsatisfiable, because the fix *prefixes* the searched string. Under the
correct form, across the seven content trees:

```
grep -rnoP "(?<!unconditioned )aggregate-statistics test"  ->  0
grep -rnoP "unconditioned aggregate-statistics test"       ->  2  (positive control)
```

The two positive-control hits are `positions/methodology-and-calibration` L112 and
`apex/research-programme-decisions-under-the-map` L47. All five W6 loci carry the scoping:
`apex/self-concealing-interface` L3 (description), L55 (`apex_thesis`), L63 (lead), L77, L87.
`unconditioned` occurrence counts (`grep -o`, not `grep -c`): self-concealing-interface 9,
research-programme-decisions 15, methodology-and-calibration 1.

*Correction to the driver's figures:* `grep -c unconditioned` reports 11 lines for
research-programme-decisions; the 15 the driver quoted is the occurrence count and is right.
Everything else in the driver's W6 table confirms exactly.

**(a) No fix over-scoped.** The scoped surfaces assert that evidence "lives at ...
intention-conditioned statistical tests". `tenets.md` L75 licenses precisely that — "a deviation
*conditioned* on intention, task or subject would test the corridor itself" — and the two apex
extensions kept the accompanying null. `research-programme-decisions` L47's added clause reads
"a null that does not extend to intention-conditioned tests of the same corridor", which is
literally true of the *unconditioned* null and does not assert detectability; L124 of the same
file then carries the register's own counterweight verbatim ("One coarse grain has run null (the
preregistered intention-to-RNG tests of Maier et al. 2018) ... the channel is open exposure
rather than banked support"). That is calibrated correctly.

**(b) No dependent stranded.** Normalised search across all seven content trees *and* `archive/`
for the stale unqualified subtitle returned zero: `hide from aggregate` 0, `hide from ordinary
aggregate` 0, `selected to hide` 6 — all six being the qualified form at
`self-concealing-interface` L3/L55/L63, `born-preserving-causal-efficacy` L200,
`apex-articles` L601/L603. The sweep was complete and left no orphan label.

**(c) Extension commits landed coherently — verified by diff, not by commit message.**
`f7c071ff2f` inserted the qualifier at `apex-articles` L601/L603 and
`born-preserving-causal-efficacy` L200, matching each file's own house form (italicised
`*unconditioned*` in born-preserving, which already carried "*unconditioned aggregate* test" at
L75). Its L603 rewrite also removed a CLAUDE.md-banned "not X — it is Y" construct by inverting to
positive-claim-first, copying the live article's L63 ordering; that is correct. `fce0d542b9` is the
best of the three: on `apex/assessing-ai-consciousness-under-the-map` it inserted the
`*unconditioned*` scoping **and** added the caveat that would otherwise have over-scoped it — "the
intention-conditioned channel left open is substrate-neutral in *form*, but whether it reaches a
digital system awaits the interface-eligibility law the Map concedes it lacks." That is a fix that
declined the free win, which is the right call.

The residual unqualified `aggregate` forms inside `self-concealing-interface` (L81, L101, L165,
L175) are **not** defects. Each names *aggregate Born-statistics tests* specifically, which is the
type-level claim and true as written. **No string sweep should be proposed on them** — this is the
09-08 Note 1 constraint (the family is scoped by the type/token distinction, not by the word
"unconditioned"), and it still holds.

---

## Part 2 — Seven families still live, unactioned, uncovered

Each key below was searched after stripping `*` and `_` and collapsing whitespace, case-insensitively.
Every one returned **exactly one hit, at the line the 2026-09-08 report cited**: zero line drift
in three days.

| Family | Tenet | File | Line | Key (verbatim) |
|---|---|---|---|---|
| W2a | 1 | `concepts/qualia` | 205 | "establish that *some* non-physical element enters the causal story" |
| W2b | 4 | `concepts/qualia` | 213 | "preserve the determinacy that phenomenology demands" |
| W3 | 1 | `topics/enactivism-challenge-to-interactionist-dualism` | 108 | "irreducible without requiring a separate *substance*" |
| W4a | 1 | `concepts/implicit-memory` | 149 | "the Map's substance dualism" |
| W4b | 1 | `concepts/mind-brain-separation` | 108 | "the Map's substance dualism" |
| W7a | 2 | `topics/completeness-in-physics-under-dualism` | 90 | "No experiment can detect" |
| W7b | 2 | same | 96 | "It cannot point to a prediction that, were it to fail, would refute it." |
| W7c/d | 2 | same | 98 | "empirically closed for all parties" / "statistically invisible" |
| W9 | 3 | `topics/consciousness-and-integrated-information` | 82 | "metaphysically real at the token level" |
| W10 | 3 | `topics/language-recursion-and-consciousness` | 190 | "demonstrates downward causation" |
| W11 | 3 | `concepts/ai-epiphenomenalism` | 63 | "consciousness does genuine causal work" |

**Coverage check.** `todo.md` was split on its enclosing `### ` headers and every block mentioning
each target file was classified open/done. The open blocks that mention these files are: a P3
cross-link batch (L6237, L6272), two NEEDS-HUMAN length decisions (L784, L819), an agentic-social
topic-dedup NEEDS-HUMAN (L632), a HUMAN COALESCE DECISION (L3650), a P3 on a *research note's*
Tulving quote (L437), a P3 about model-pointer referents (L540), a P3 on the positions register's
citations (L1450), a P3 to write a *new* enactivism article (L6098), and a P3 apex synthesis
(L6740). **None covers any of the seven findings.**

### Priority order — this list is the actioning mechanism, so it is written to be acted on

1. **W7 — `topics/completeness-in-physics-under-dualism`, four loci in one file (L90, L96, L98×2).**
   The densest carrier, and the only file where the over-concession is structural rather than a
   single sentence: L90 "No experiment can detect the difference", L96 "cannot point to a
   prediction that, were it to fail, would refute it", L98 "empirically closed for all parties"
   and "statistically invisible by construction". All four are unscoped where `tenets.md` L75,
   L81 and L107 scope the same claim to the *unconditioned* register and L81 names falsifier (c)
   explicitly. 3599w, `soft_warning` (topics 3000/4000/6000) — **word-neutral qualifier inserts
   only**; four single-word or short-clause scopings fit inside the budget.
2. **W9 — `topics/consciousness-and-integrated-information` L82.** The sharpest Tenet 3 finding:
   "metaphysically real at the token level" asserts as settled exactly what `tenets.md` L95
   (`^tenet-3-standing`) says the interface argument leaves open — "Articles asserting that
   consciousness does 'real work' or 'genuine causal work' inherit that debt rather than discharge
   it". 4000w, `hard_warning`, exactly at the hard ceiling — **word-neutral or net-negative only**.
3. **W3 — `topics/enactivism-challenge-to-interactionist-dualism` L108.** The inverse failure: the
   article disclaims a commitment the framework actually holds ("irreducible without requiring a
   separate *substance*"), where `tenets.md` L183 states plainly that "Tenet 1 advertises
   substance/property neutrality while the framework operates substance-dualist". 2459w, `ok`
   (topics soft 3000) — **the only one of the seven with real room to expand**, so this is where a
   proper two-sentence scoping paragraph belongs rather than a compressed insert.
4. **W2 — `concepts/qualia` L205, L213.** Two distinct tenets in one file: L205 says qualia
   arguments "establish that *some* non-physical element enters the causal story" (Tenet 1
   over-claim against L55's "cumulative case ... not a set of independent proofs"); L213 says
   single-outcome interpretations "preserve the determinacy that phenomenology demands" (Tenet 4
   over-claim, and the same file's L207 already concedes decoherence "does predict definite qualia
   within each branch"). 4032w, `hard_warning` — **word-neutral**; L205's fix is a verb swap
   (`establish` → `argue`, or `support`), L213's is a hedge the neighbouring line already models.
5. **W11 — `concepts/ai-epiphenomenalism` L63.** "consciousness does genuine causal work in
   biological systems" — the exact phrase `tenets.md` L95 names as inheriting mechanism debt.
   2689w, `soft_warning` — **word-neutral**; a single qualifier.
6. **W10 — `topics/language-recursion-and-consciousness` L190.** "Speaking recursive sentences
   demonstrates downward causation." Note the same paragraph *ends* correctly ("*If* this effort
   reflects consciousness causally influencing neural production...") and the adjacent Tenet 2 and
   Tenet 4 subsections (L188, L192) are model-calibrated. The defect is the topic-sentence only.
   4161w, `hard_warning` — **word-neutral**; `demonstrates` → `exemplifies` / `is the Map's
   candidate case of` and the paragraph is consistent with itself.
7. **W4 — `concepts/implicit-memory` L149 and `concepts/mind-brain-separation` L108.** The
   weakest of the seven, and honestly so: both are *contrastive* uses ("differ substantially from
   the Map's substance dualism", "closer to neutral monism than the Map's substance dualism"), so
   the bare assertion of a substance commitment is incidental to the sentence's work. Still a
   Tenet 1 scoping defect under `tenets.md` L183 (the commitment is downstream of agent causation,
   not of the tenet). 3248w and 2501w, both `soft_warning` — mind-brain-separation is 1 word over
   soft, so **strictly word-neutral there**.

---

## Part 3 — Warning 12 (new): the conditioned register is described as evidentially virgin at the one place the register cites for it

**Tenet**: 2 (Minimal Quantum Interaction) — against `tenets.md`'s own scoping at L75 and L81.
**Severity**: WARNING, not ERROR. Per this series' convention, ERROR is reserved for the
direct-contradiction battery; a mis-scoped evidential claim runs *toward* Tenet 2's rules-out
clause and is measured against the tenets page's scoping rather than against a "Rules out" list.

**File**: `apex/self-concealing-interface`, **L135**.

**Quote**: "The seam tests below are instances of horn (a): they are *conditional
residual-structure* tests, not generic Born-frequency tests, and a null on unconditioned outcome
statistics (the micro-psychokinesis record) leaves them untouched because it never conditioned on
the variable said to carry the effect."

**Issue.** The micro-psychokinesis record is not unconditioned outcome statistics, and it did
condition on the variable said to carry the effect: intention. The corpus says so in four places,
three of them agreeing with each other and against L135.

- `tenets.md` **L75**: "a deviation *conditioned* on intention, task or subject would test the
  corridor itself ... and **one coarse-grain instance has already run null**—the preregistered
  intention-to-RNG tests of Maier et al. (2018)."
- `apex/born-preserving-causal-efficacy` **L89**: "the Map should not overstate how much of it
  remains unexplored: intention-to-RNG micro-psychokinesis *is* a conditional test at the
  coarsest grain, and it has returned preregistered nulls (Maier et al. 2018). Those nulls leave
  open only the finer grains no instruction reproduces."
- `apex/research-programme-decisions-under-the-map` **L124**, quoting the register: "One coarse
  grain has run null ... so the channel is **open exposure rather than banked support**."
- `apex/self-concealing-interface` **L135**: the null "leaves them untouched".

**The article also contradicts itself.** Its own L93 sets the operational rule: a null does
evidential work iff "a *quantitative prediction was preregistered*: a specific effect, at a
specified conditioning grain, with a stated magnitude or bound, fixed before the data were seen."
Maier, Dechamps & Pflitsch (2018) is preregistered, Bayesian, at a specified conditioning grain
(intention-to-RNG), with a reported BF01 = 10.07 (quoted in `topics/selection-only-mind-influence`
L105). By L93's own rule that null *does* evidential work against the coarsest conditional grain.
L135 then exempts it.

**Why this locus matters more than its word count suggests.** `positions/quantum-interface` L144
routes the register's conditional-statistical exposure through exactly this article — "its
sharpest form is the second prediction of `apex/self-concealing-interface`". So the one surface
the register nominates as its sharpest conditional test is the one surface that describes the
conditional register as untested. L135 also opens by pointing at
`apex/born-preserving-causal-efficacy` as "the same fork", and that file's L89 says the opposite
in the same breath. `self-concealing-interface` cites Maier nowhere (0 occurrences).

**Relation to the 09-09 closure.** L135 dates to `f92041ee58f` (2026-07-16) and predates the W6
fix, so this is not a fix-induced regression. It is the sharper thing: the W6 fix made the
article's invisibility claim consistently *unconditioned*-scoped and pointed its evidential
programme at intention-conditioned tests, which raises L135 from a loose aside to the load-bearing
claim about where the Map's exposure now sits. The scoping sweep strengthened a sentence it never
read.

**Recommended fix — word-neutral, and not invented.** The file is **5116w against apex hard 5000**
(`hard_warning`), so nothing may be added net. Replace the clause at L135:

- was: "and a null on unconditioned outcome statistics (the micro-psychokinesis record) leaves
  them untouched because it never conditioned on the variable said to carry the effect" (25 words)
- to: "and the preregistered intention-to-RNG nulls (Maier et al. 2018) constrain only the
  coarsest conditioning grain, leaving the finer grains no instruction reproduces untested"
  (23 words) — **net −2**

The replacement wording is lifted in substance from `research-programme-decisions` L124's own
register quote, so it imports no new position. No reference-list entry is needed: the file has no
reference section, and the sentence already links `apex/born-preserving-causal-efficacy`, which
carries the full Maier citation at L222.

**Do not touch L77**, which is exemplary and listed do-not-edit by a closed task. L93 needs no
change — it is the rule L135 violates, and it is correct as written.

---

## Notes

**Note 1 — W13 is covered, and the coverage came from a different review series.** `todo.md`
**L227** is an open P3 on `topics/consciousness-and-the-phenomenology-of-constraint-satisfaction`
L36, naming exactly the "*because* consciousness is doing genuine causal work" lead with the fix
specified; its `Source` line reads `optimistic-review`, review file
[reviews/optimistic-2026-08-27-intellectual-life-wing.md](/reviews/optimistic-2026-08-27-intellectual-life-wing/). **L182** covers the sibling
`topics/phenomenology-of-cognitive-capacity` L139. Both loci verified still live at the cited
lines. **Do not re-mint either.** Worth recording that the only one of the eight unactioned
families to acquire coverage acquired it from optimistic-review, twelve days before the
tenet-check that found it independently.

**Note 2 — the `research/` locus is out of scope, and I judge it should stay that way.**
[research/the-agency-budget-under-exact-born-rule-preservation-2026-08-13.md](/research/the-agency-budget-under-exact-born-rule-preservation-2026-08-13/) L25 still carries the
unscoped "perfect security is *equivalent to* zero third-person statistical evidence", where the
article that consumed it (`apex/self-concealing-interface` L87) now reads "...in the unconditioned
marginal". This skill's stated scan scope is `topics/`, `concepts/`, `positions/`. Research notes
are dated, superseded-by-design artefacts of the state of thinking on their date; scoping them to
match later article revisions would misrepresent what was known on 2026-08-13. Recorded as a Note
and deliberately not escalated.

---

## Part 4 — Structural finding: the priority list is the actioning mechanism

`check-tenets/SKILL.md` has no minting step, which is correct — the skill is reports-only. A
finding therefore enters the queue only if a driver reads the report. The 2026-09-08 report closed
with a section titled "What to do first, if anything is minted", naming four items in priority
order: W6, W8, W1, W12.

**All four were actioned within two days. Zero of the eight families outside that list were.**

| Family | On the 09-08 priority list? | `todo.md` | Outcome |
|---|---|---|---|
| W6 (five-locus self-concealing) | yes (1st) | L2206 | ✓ 2026-09-09 |
| W8 (`concepts/bi-aspectual-ontology` L51/L53) | yes (2nd) | L2196 | ✓ 2026-09-09 |
| W1 (`concepts/zombie-master-argument` L106–120) | yes (3rd) | L2201 | ✓ 2026-09-09 |
| W12 (`topics/structure-of-attention` L3) | yes (4th) | L2033 | ✓ 2026-09-10 |
| W5 (pragmatism / background commitments) | no — already owned by an open P2 | L2521 | ✓ 2026-09-08 |
| W2, W3, W4, W7, W9, W10, W11 | no | — | no task, no edit |
| W13 | no | L227 | covered by optimistic-review, not by this series |

Also resolved in the window: the upstream [P-Q9](/positions/quantum-interface/#p-q9) unscoped-aggregate-channel task at L2186
(✓ 2026-09-09). The correlation across the 09-08 report is exact: **being on the priority list,
not being a finding, is what determined action.** Items 5–13 of a thirteen-family report are
empirically invisible.

**The tightest instance — the same line, not merely the same file.** Commit **`2cc1cf5585`**
(2026-09-10 14:10 UTC, `auto(refine-draft)`) edited
`topics/completeness-in-physics-under-dualism` **L98** — the exact line carrying W7c
("empirically closed for all parties") and W7d ("statistically invisible") — and changed only
"Process 1" to "Process 3" inside it. The diff confirms the line was rewritten and both
over-concessions were carried through verbatim, because the editing task keyed on a different
string. **Being edited is not being reviewed**, even when the editor's cursor is inside the
defective sentence.

**Consequence for this report's design.** The priority list in Part 2 *is* this report's
actionable output, and it is deliberately ordered, budgeted and pre-scoped so that a driver
reading only that list still actions all seven. Part 3's new warning is listed separately because
it is a different file and a different budget constraint. If only one thing is done from this
report, do W7 — four loci, one file, `soft_warning`, and the line already proven to survive an
edit.

## Method

- `obsidian/tenets/tenets.md` read first, at L55, L75, L81, L95, L107, L163, L171, L175, L177, L183.
- All presence and absence tests normalised markdown emphasis (`*`, `_` stripped), collapsed
  whitespace, and ran case-insensitively. Absence tests were paired with positive controls.
- Substring keys guarded: `(?<!un)conditioned`, `(?<!unconditioned )aggregate-statistics test`.
- Occurrence counts used `grep -o | wc -l`, never `grep -c` (which counts lines).
- Word counts measured with `tools.curate.length.analyze_length` (body-only; no frontmatter
  subtraction applied).
- `todo.md` coverage measured by splitting on enclosing `### ` headers, not by line-proximity grep.
- **No content file was modified. No task was minted. Nothing was committed.**
- **No wikilink of any form appears anywhere in this report** — every file reference is backticked,
  per this series' convention, so no synced-wikilink push hazard is introduced. Verified by
  printed offset: the double-bracket token occurs zero times.