---
ai_contribution: 100
ai_generated_date: 2026-09-09
ai_modified: 2026-09-09 17:10:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-09
date: &id001 2026-09-09
description: A close-the-loop run, not a corpus survey. All four priority findings
  of the 2026-09-08 report are re-verified live on current disk; Warning 5 is confirmed
  fixed and its task closed. Mintable detail is given for every live locus.
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-09-09 17:10:00+00:00
modified: *id001
related_articles:
- '[[tenets]]'
- '[[tenets/background-commitments]]'
- '[[apex/self-concealing-interface]]'
- '[[apex/research-programme-decisions-under-the-map]]'
- '[[positions/methodology-and-calibration]]'
- '[[positions/quantum-interface]]'
- '[[concepts/bi-aspectual-ontology]]'
- '[[concepts/measurement-problem]]'
- '[[concepts/zombie-master-argument]]'
- '[[concepts/philosophical-zombies]]'
- '[[concepts/dualism]]'
- '[[concepts/pragmatism]]'
- '[[concepts/prebiotic-collapse]]'
- '[[concepts/self-stultification]]'
- '[[topics/structure-of-attention]]'
- '[[topics/consciousness-and-the-phenomenology-of-constraint-satisfaction]]'
title: Tenet Alignment Check - 2026-09-09
topics: []
---

# Tenet Alignment Check

**Date**: 2026-09-09 (17:10Z)
**Predecessor**: [reviews/tenet-check-2026-09-08.md](/reviews/tenet-check-2026-09-08/)
**Run type**: **status re-verification, not a corpus survey.** No new sweep of the 831-file corpus was attempted.
**Errors**: 0
**Warnings**: 4 families re-confirmed live (09-08 Warnings 6, 8, 1, 12); 1 family confirmed fixed (Warning 5)
**Notes**: 1

## Why this run is shaped differently

`check-tenets/SKILL.md` contains no task-minting step. Greps of the skill file for
`todo.md`, `mint` and `task` return zero. So the 09-08 report's closing line —
"This report mints nothing" — is the skill honouring its contract, and its four
priority findings could only enter the queue by a human or driver reading them.
**None did**: `obsidian/workflow/todo.md` contains the string
`tenet-check-2026-09-08` at offset **-1**.

That absence was confirmed a second, structurally different way. `todo.md` was
split on its enclosing `### ` headers and all blocks mentioning the four target
files were classified open/resolved:

| Target file | Blocks mentioning it | Any OPEN block covering the finding? |
|---|---|---|
| `apex/self-concealing-interface` | 4 (1 open, 3 ✓) | **No** — the open one is the L1443 NEEDS-HUMAN apex-ledger sequencing task |
| `concepts/bi-aspectual-ontology` | 2 (both open) | **No** — an agentic-social solver note and a P3 cross-link task |
| `concepts/zombie-master-argument` | 4 (all ✓) | **No** |
| `topics/structure-of-attention` | 3 (1 open, 2 ✓) | **No** — the open one is a human editorial merge survey |
| `aggregate-statistics` (string) | 1 (✓ 2026-09-04) | **No** |

**All four families below are mint-eligible with no duplicate.**

## Warning 6 — LIVE. Five loci, none moved. The hard test still returns 2.

**Status: LIVE.** The 09-06 completion test — `grep -rnF "aggregate-statistics test"`
over the live tree must return zero — **returns 2**, the same two loci, unmoved.
Neither `apex/self-concealing-interface` nor `positions/methodology-and-calibration`
has had a single commit since 2026-09-07 (`git log --since=2026-09-07` on each: empty).
`apex/research-programme-decisions-under-the-map` was committed on 09-08, but that
commit (`b80998e624`) was the arXiv peer-review-flag fix and did not touch L47.

**Tenet at issue:** Tenet 2 (Minimal Quantum Interaction). **No Rules-out clause is
breached** — over-conceding undetectability runs *toward* the "no empirically
detectable mind-matter interactions" clause, not against it. What these loci
contradict is the canonical scoping at `tenets.md` L75, L81 and L107, which since
2026-08-27/09-04 restrict the indistinguishability to the *unconditioned aggregate*
register and keep a conditioned deviation live. **Severity: WARNING** under this
series' convention (Errors reserved for the direct-contradiction battery).

### On the transplant source: `tenets.md` L107 IS the right line — the doubt was misplaced

The driver's suspicion that L107 is "about outcome-selection versus
context-selection, which may not be the right line" is understandable from the
paragraph's bold lead, but **the scoped wording is in its middle**, verbatim:

> L107: "Because the per-trial bias is constructed to average back to the Born measure, the position is *empirically indistinguishable from chance* under any *unconditioned aggregate* test current or foreseeable instruments could run, though a deviation *conditioned* on intention, task or subject remains live ([P-Q3](/positions/quantum-interface/#mechanism-debt))"

So L107 is a valid transplant source and the 09-08 report was right to name it.
**L75 is the stronger source** and should be preferred, because it adds the clause
L107 omits — "*by construction, not by any sensitivity limit*" — which is exactly
the element the pragmatism-class defects drop:

> L75: "under any *unconditioned aggregate* test the mechanism is *empirically indistinguishable from chance*—by construction, not by any sensitivity limit. … Preservation binds only that unconditioned marginal, however: a deviation *conditioned* on intention, task or subject would test the corridor itself ([P-Q3](/positions/quantum-interface/#mechanism-debt) … ), and one coarse-grain instance has already run null—the preregistered intention-to-RNG tests of Maier et al. (2018)."

The `^mechanism-debt` anchor is defined at [positions/quantum-interface.md](/positions/quantum-interface/) offset
3490 and resolves. Do not "fix" the path-qualified link form.

### Locus 6a — `obsidian/apex/self-concealing-interface.md` L3 (`description:`)

**Current (250 chars):**

> `description: "If the Map is right, the mind-matter interface is not merely hard to detect—it is structurally selected to hide from aggregate measurement, which re-orients the whole evidential programme from bulk physical traces to constrained asymmetries at seams."`

**Proposed (254 chars):**

> `description: "If the Map is right, the mind-matter interface is structurally selected to hide from unconditioned aggregate measurement, re-orienting the evidential programme from bulk physical traces to intention-conditioned tests and constrained asymmetries at seams."`

Secondary gain: the replacement also retires the banned "not merely X—it is Y"
construct the current text carries. **Zero word cost** — `analyze_length` is
body-only, so frontmatter edits do not touch the file's length status.

### Locus 6b — `obsidian/apex/self-concealing-interface.md` L55 (`apex_thesis:`)

**Current:**

> `apex_thesis: "If the Map's tenets are right, the mind-matter interface is structurally selected to hide from aggregate measurement—so the evidence that could ever bear on it lives at constrained asymmetries (disruption, dissociation, graded channel failure, patient-population divergence, first-person/third-person mismatch), not in bulk physical traces."`

**Proposed:**

> `apex_thesis: "If the Map's tenets are right, the mind-matter interface is structurally selected to hide from *unconditioned aggregate* measurement—so the evidence that could ever bear on it lives at intention-conditioned tests and constrained asymmetries (disruption, dissociation, graded channel failure, patient-population divergence, first-person/third-person mismatch), not in unconditioned bulk physical traces."`

The thesis's own evidence taxonomy is the defect, not just the qualifier: its five
named seams are all *asymmetries*, and its own sharpest prediction — L143,
Prediction 2 — is a **conditioned statistical test**, which the taxonomy has no slot
for. Zero word cost (frontmatter).

### Locus 6c — `obsidian/apex/self-concealing-interface.md` L87 (body). This is the contradiction.

**Current (two clauses in one sentence-pair):**

> "[The agency budget](/concepts/agency-budget/) shows that a selector constrained to preserve a distribution exactly is, in information-theoretic terms, a perfectly secure channel — and that perfect security is *equivalent to* **zero third-person statistical evidence**. … and by the same equivalence **no aggregate test can ever witness the channel**, so the architecture inherits a theorem where it might have wanted a defence."

**The self-contradiction, stated precisely.** L143 of the same file predicts
"residual mutual information with a preregistered intention covariate that the
unconditioned distribution does not show: I(outcome ; intention | measured physical
state) > 0 while the marginal stays Born-exact." A mutual information estimated
across trials **is** third-person statistical evidence. L87's unqualified "zero
third-person statistical evidence" therefore denies what L143 predicts. The theorem
L87 invokes constrains the *distribution-preserving marginal* — precisely the
unconditioned register — so the scoped reading is also the mathematically correct one.

**Proposed (minimal, +2 words):**

> "…perfect security is *equivalent to* zero third-person statistical evidence *in the unconditioned aggregate*. … and by the same equivalence no unconditioned aggregate test can ever witness the channel, so the architecture inherits a theorem where it might have wanted a defence."

⚠️ **Length constraint on this file — keep the edit minimal.**
`analyze_length` reads **5116 words against a hard threshold of 5000** (`apex`
thresholds: soft 4000 / hard 5000 / critical 6500) — status `hard_warning`, 116
words over. Do **not** add a conditioned-route sentence here: the route is already
stated exemplarily at L77 of the same file ("The aggregate-statistics routes that
constrained earlier interactionist proposals therefore cannot probe it; a deviation
*conditioned* on intention, task or subject still could") and demonstrated at L143.
**L77 is correct and must not be touched** — the ✓ 2026-09-08 task at `todo.md`
L2313 explicitly lists it as already-scoped, do-not-edit.

### Locus 6d — `obsidian/positions/methodology-and-calibration.md` L112 ([P-M4](/positions/methodology-and-calibration/#p-m4), *Asserts*)

**Current fragment:**

> "…with the testability cost of Born-statistics-preserving outcome-selection (**empirical indistinguishability under aggregate-statistics tests**) stated as a known framework-boundary fact rather than dressed as a near-term experimental opening."

**Proposed (+1 word):**

> "…(empirical indistinguishability under **unconditioned** aggregate-statistics tests) stated as a known framework-boundary fact…"

The file contains **zero** occurrences of `unconditioned` and **zero** of
`conditioned` (Python `str.count`), so the register the canonical page keeps live is
absent from the register file that governs the Map's calibration discipline. Note
the line has drifted from L109 (09-06) to **L112**, so a line-keyed status check
would read a false "repaired" — confirm by string, not line.

⚠️ Length: 3921 words against `positions` hard 2500 — `hard_warning` at 261% of
soft. This is the known state covered by the open NEEDS-HUMAN at `todo.md` L1481
(positions inheriting article thresholds); it is not a reason to skip a +1-word fix,
but it is a reason not to expand here.

### Locus 6e — `obsidian/apex/research-programme-decisions-under-the-map.md` L47 (`apex_thesis:`). Most consequential of the five.

**Current fragment:**

> "…which ranks mechanism-level work (toy models, coherence-time calculations, brain-internal Born-rule tests) and psychophysical tests of the qualia-inversion residue **above aggregate-statistics tests that the self-concealing interface predicts will read null**."

**Why this is more than a wording nit.** This is the apex that *decides what research
is worth doing*. It downranks aggregate-statistics tests wholesale on the ground
that they will read null — but `tenets.md` L75 designates the **conditioned**
register as the tenet's remaining empirical content, and
`concepts/tenet-falsification-conditions` treats that conditional register as the
tenet's entire live empirical content. The file contains **zero** occurrences of
`conditioned`, `unconditioned`, `conditioning` or `intention-conditioned` (Python
`str.count`, all four keys), so nothing elsewhere in the file repairs it. The apex
therefore ranks *out of the programme* the one empirical register the canonical page
keeps *in*.

**Proposed:**

> "…above **unconditioned** aggregate-statistics tests that the self-concealing interface predicts will read null — while a deviation *conditioned* on intention, task or subject remains live and would test the corridor itself ([P-Q3](/positions/quantum-interface/#mechanism-debt))."

Zero word cost (frontmatter). File is 4473 words against `apex` hard 5000 —
`soft_warning`, 527 words of headroom, so a body-side sentence would also fit if the
editor prefers to place the qualification in prose.

## Warning 8 — LIVE, verbatim, unmoved

**Status: LIVE.** `git log --since=2026-09-07 -- obsidian/concepts/bi-aspectual-ontology.md`
is empty. Both sentences read exactly as the 09-08 report quoted them.

**File**: `obsidian/concepts/bi-aspectual-ontology.md`
**Tenet at issue**: Tenet 3 (Bidirectional Interaction) — the warrant assignment.
**Severity**: WARNING. No Rules-out clause breached; the conflict is with a
retired inference on the canonical page.

**Locus 8a — L51:**

> "Why think consciousness fills this role rather than some as-yet-unknown physical process? **Two independent considerations converge** … Second, **the measurement problem marks the point where structural description reaches its limit**: physics specifies what can happen and with what probability, but not why *this* outcome becomes actual. These two facts … make consciousness a motivated candidate for the actualising role, not merely a label for our ignorance."

**Locus 8b — L53:**

> "This does not mean consciousness is the *only* possible candidate. A critic may argue that actualisation is simply a brute fact requiring no further explanation … **The Map disagrees: the existence of definite outcomes demands an account, and consciousness is the only independently motivated non-structural reality available to provide one.**"

**The canonical clause retiring this inference — `tenets.md` L183:**

> "once objective reduction secures definiteness, **the measurement problem cannot itself be evidence for conscious selection**—the agency evidence ([Tenet 3](/tenets/#bidirectional-interaction)) must carry that burden."

**A second, independent contradiction — `tenets.md` L125** (the Map's own prebiotic
resolution): "Physical mechanisms (gravitational collapse, spontaneous localization,
or unknown processes) provide baseline collapse throughout the universe.
Consciousness interfaces with collapse specifically in neural systems, **modulating**
outcomes where the brain provides the right interface." On the Map's own view
consciousness is therefore *not* the only available account of definiteness — so L53
is false by the framework's own commitments, not merely unearned. L53 also
self-contradicts across two sentences: it concedes "not the *only* possible
candidate" and then asserts consciousness is "the only … available".

**Verified: the burden `tenets.md` L183 assigns is carried nowhere locally.** Python
`str.count` over the whole file: `agency` **0**, `agent causation` **0**,
`agent-causation` **0**, `self-stultification` **0**, `Tenet 3` **0**. The file has 6
`Bidirectional` references — L75, L109, L139 — and all three were read: L75 invokes
the tenet to reject parallelism, L109 to press IIT, L139 to distinguish the Map from
dual-aspect monism. **None cites Tenet 3 as the warrant for the actualising role.**

**Model wording, one file away — `concepts/measurement-problem` L203** (verified
verbatim on disk this run):

> "*Definiteness*: [objective collapse](/concepts/spontaneous-collapse-theories/) answers 'why one definite outcome?' without invoking any mind, so the measurement problem itself cannot be evidence for conscious selection. *Compatibility*: … the availability of that location is not evidence that consciousness occupies it. *Warrant*: the positive case that consciousness *does* act is carried by the agency arguments under [Bidirectional Interaction](/tenets/#bidirectional-interaction)—the [self-stultification of epiphenomenalism](/concepts/self-stultification/) chief among them…"

**Proposed replacement, L51** (recast the second consideration from support to
permissibility):

> "Why think consciousness is a candidate for this role rather than some as-yet-unknown physical process? Two considerations make it one — neither of them evidence that it occupies the role. First, the [hard problem](/topics/hard-problem-of-consciousness/) (Chalmers 1996) gives reason to think consciousness is real and irreducible to structure … Second, the measurement problem marks the point where structural description reaches its limit, which supplies the *permissibility condition* for a selection role rather than support for it: [objective collapse](/concepts/spontaneous-collapse-theories/) answers 'why one definite outcome?' without invoking any mind, so the measurement problem cannot itself be evidence for conscious selection ([measurement-problem](/concepts/measurement-problem/); [background posit 2](/tenets/background-commitments/)). Together they make consciousness a *motivated candidate* for the actualising role — the availability of the location, not evidence that consciousness fills it."

**Proposed replacement, L53:**

> "This does not mean consciousness is the *only* possible candidate, and the Map does not claim it is. A critic may argue that actualisation is simply a brute fact requiring no further explanation — that outcomes just happen with their Born-rule probabilities. The Map holds instead that definiteness has an account, but not that consciousness supplies it alone: [physical objective reduction](/concepts/prebiotic-collapse/) provides baseline collapse throughout the universe, prebiotically included, and consciousness *modulates* outcomes where a neural interface exists. The warrant for that modulating role is carried by the agency arguments under [Bidirectional Interaction](/tenets/#bidirectional-interaction) — [the self-stultification of epiphenomenalism](/concepts/self-stultification/) chief among them — and not by the measurement problem ([the Tenet 3 standing paragraph](/tenets/#tenet-3-standing))."

All four new wikilink targets resolve on disk: `obsidian/concepts/prebiotic-collapse.md`,
`obsidian/concepts/self-stultification.md`, `obsidian/concepts/measurement-problem.md`,
and the `^tenet-3-standing` anchor at `tenets.md` L95.

**Length:** 2722 words against `concepts` soft 2500 / hard 3500 — `soft_warning`,
**778 words of headroom to hard**. The additive fix fits comfortably.

## Warning 1 — LIVE, verbatim, unmoved. Highest stakes, and there is a fifth locus.

**Status: LIVE.** `git log --since=2026-09-07 -- obsidian/concepts/zombie-master-argument.md`
is empty. All three quoted loci read exactly as reported, and the whole
"Relation to Site Perspective" block L102–L120 was re-read in context.

**File**: `obsidian/concepts/zombie-master-argument.md`
**Tenet at issue**: Tenet 1 (Dualism) — the standing of the case, not its content.
**Severity**: WARNING. **Not an ERROR**, on the 09-08 driver's own ground: this
over-claims *in the tenet's favour* and endorses nothing a Rules-out clause forbids.

**The canonical clause — `tenets.md` L55**, whose heading is itself the point
("**Rationale (a commitment the Map owns, not a result it reports)**"):

> "The [positive arguments for dualism](/concepts/dualism/) … **form a cumulative case for irreducibility that each opponent disputes at a different point, not a set of independent proofs converging on a settled conclusion. Tenet 1 records where the Map plants itself in an unsettled dispute; it does not report that dispute as won.**"

**Why it survived.** `tenets.md` **L171** quotes this very article approvingly for
its *scoping* half — "[zombie-master-argument](/concepts/zombie-master-argument/) states the resulting discipline
directly: the zombie argument 'does its work under *minimal dualism* — Tenet 1
alone'" — so the canonical page reads past the unhedged half in the same sentence it
endorses.

**Locus 1a — L106:**

> "The case for dualism doesn't rest on any single intuition pump but on **a logical architecture that physicalists have been unable to dismantle despite sustained effort. Each physicalist response concedes ground; the question is only how much.**"

Proposed: "…but on a logical architecture the Map judges physicalists have not
dismantled — a judgement each opponent disputes at a different point rather than a
settled result ([Tenet 1](/tenets/#dualism)'s rationale). How much ground each
physicalist response concedes is itself contested."

**Locus 1b — L112:**

> "At that stage, before any commitment to bidirectional interaction, **zombie conceivability establishes non-entailment and refutes physicalism.** The argument's job is done once it shows that physical description doesn't exhaust reality."

Proposed: "At that stage, before any commitment to bidirectional interaction, *if the
conceivability premise holds*, zombie conceivability yields non-entailment and tells
against physicalism. The argument's job at this stage is to press that
non-entailment, not to settle it."

**Locus 1c — L114:**

> "**Having established dualism** via the conceivability argument, it adds Tenet 3 … The zombie argument is a ladder that, once climbed, the full framework kicks away — **not because the argument was wrong, but because it succeeded in establishing** the dualism that makes bidirectional interaction possible."

Proposed: "Having *argued for* dualism via the conceivability argument, it adds
Tenet 3 … The zombie argument is a ladder that, once climbed, the full framework
kicks away: the argument did its work at the minimal-dualism stage, and the stronger
theory it licenses then excludes the case it used." Note the current text also
carries the banned "not because X, but because Y" construct; the replacement retires
it.

**Locus 1d — L116:**

> "**Zombies remain metaphysically possible — Step 2 holds and physicalism is false** — while being nomologically impossible under the Map's completed framework…"

Proposed: "Zombies remain metaphysically possible on the argument's own terms — if
Step 2 holds, physicalism is false — while being nomologically impossible under the
Map's completed framework…"

**Locus 1e — L120. NEW this run, same family, same section, not in the 09-08 list:**

> "If the physical facts don't necessitate the phenomenal facts, adding consciousness to the ontology isn't an optional extravagance — it's a recognition of **what the argument establishes**."

This sits in the article's Tenet 5 subsection and repeats the settled-result framing
one paragraph after the three flagged loci. Proposed: "…it's a recognition of what
the argument concludes to." Reported so the pass does not strand a sibling four
lines below the ones it fixes — the `sweep-fixes-the-disclaimer-and-strands-its-dependents`
shape.

**Calibrated model wording, and a line correction to the 09-08 report.** The 09-08
report cited `concepts/philosophical-zombies` **L141**; L141 actually reads "The
argument doesn't specify *what* that something is:". The wording it meant exists in
the same file at **L201**, in that article's own Relation-to-Site-Perspective
section, and is the better model because it is the parallel passage:

> L201: "The zombie argument is a central support—**conditional**, as the Interactionist Escape section concedes—for the Map's foundational commitment. If zombies are conceivable, consciousness isn't entailed by physical facts…"

The `concepts/dualism` model the report cites **is** at L134 and verified verbatim:
"No single argument establishes dualism conclusively, and the eight are not
evidentially independent of one another."

**Length:** 2471 words against `concepts` soft 2500 — status `ok`, **1029 words of
headroom to hard**. The hedges are additive and fit easily.

## Warning 12 — LIVE, verbatim. One line, zero word cost.

**Status: LIVE.** `git log --since=2026-09-07 -- obsidian/topics/structure-of-attention.md`
is empty.

**File**: `obsidian/topics/structure-of-attention.md`, **L3** (`description:`)
**Tenet at issue**: Tenet 3, via the debt anchor `tenets.md` L95 `^tenet-3-standing`:
"Genuine, non-epiphenomenal downward causation is therefore **a posit the interface
argument leaves open, not a result it secures**. Articles asserting that consciousness
does 'real work' or 'genuine causal work' **inherit that debt rather than discharge
it, and should read no more confidently than this paragraph does.**"
**Severity**: WARNING.

**Current (167 chars):**

> `description: "Attention divides into willed, instructed, and exogenous modes with distinct neural signatures. This architecture reveals where consciousness does genuine causal work."`

**The body already has it right, twice** — so this is a label defect, not a content one:

- L38: "This structure matters philosophically because it identifies precisely where consciousness **might** do genuine causal work."
- L40: "…those pathways mark where the [bidirectional interaction](/tenets/#bidirectional-interaction) between mind and matter **could** operate."

**Proposed (190 chars):**

> `description: "Attention divides into willed, instructed, and exogenous modes with distinct neural signatures. This architecture identifies candidate sites where consciousness might do genuine causal work."`

**Fix the label, not the body.** Zero word cost (frontmatter). Descriptions reach the
machine-metadata surface regardless of body hedging, and `machine-meta.html` applies
no hedging of its own.

## Warning 5 — FIXED. Do not re-mint; the task is already closed.

**Status: FIXED**, by commit **`b8e95e4139`** (2026-09-08 **01:39:07 +0000**) —
72 minutes *after* the 09-08 report was written at 00:27Z, which is why the report
correctly recorded it live. The commit touched
`obsidian/concepts/pragmatism.md`, `obsidian/tenets/background-commitments.md` and
`obsidian/concepts/buddhism-and-dualism.md` in both trees.

Both loci re-read from disk this run and both now carry **both** canonical scope
elements:

- **`concepts/pragmatism` L44**: "That tenet describes an influence *empirically indistinguishable from chance* under any *unconditioned aggregate* test current or foreseeable instruments could run: … **Preservation binds only that unconditioned marginal, however — a deviation *conditioned* on intention, task or subject would test the corridor itself ([P-Q3](/positions/quantum-interface/#mechanism-debt))**". The pre-08-27 "presently conceivable instrument" framing that was the specific defect is gone, and the sentence no longer recasts the indistinguishability as an instrument-sensitivity limit.
- **`tenets/background-commitments` L60**: "The corridor bias is *empirically indistinguishable from chance* under any *unconditioned aggregate* test — **by construction rather than by any sensitivity limit** — … Preservation binds only that unconditioned marginal, however: a deviation *conditioned* on intention, task or subject would test the corridor itself." The unscoped attribution to "the falsifiability status the Map already records" is repaired.

The owning task is **closed**: `todo.md` L2313, `### ✓ 2026-09-08: Six live articles
still concede the corridor is flat "indistinguishable from chance"…`. A sibling
family task is closed at L2134. **Nothing to mint, and nothing left open here.**

Two things that task's notes settled and that should be carried forward rather than
re-litigated: `apex/self-concealing-interface` **L77** is correctly scoped and must
not be edited, and `topics/epistemology-of-mechanism-at-the-consciousness-matter-interface`
L123 was adjudicated a lexical false high by the 09-07 driver verification.

## Note 1 — a targeted frontmatter sweep, honestly reported

Because two of the four live findings (6a/6b and 12) are **navigation-surface**
defects, and no sweep in this series has keyed on frontmatter, one narrow extra pass
was run: every `description:`, `apex_thesis:` and `title:` line across `topics/`,
`concepts/`, `apex/`, `voids/`, `positions/`, `tenets/`, `arguments/` and
`questions/`, keyed on twelve strings from the Tenet 2 and Tenet 3 families.

**58 lexical hits; 55 of them benign.** "Reveals" is an ordinary descriptive verb in
this corpus — "blindsight reveals a dissociation", "ineffability reveals limits" —
and reporting those as tenet defects would be the
`anchoring-false-high-is-the-base-rate-lexical-vs-structural` failure. Two apparent
hits were read and cleared: `apex/born-preserving-causal-efficacy` L20/L48 frame
"genuine causal work" as the Map's "deepest unpaid debt … one unforced step from
epiphenomenalism", which is the correct debt-carrying form; and
`concepts/mental-imagery` L3 puts it as an open question ("test whether consciousness
does causal work—or only rides along").

**One genuine finding, and it belongs to an existing 09-08 family rather than being
new:** `obsidian/topics/consciousness-and-the-phenomenology-of-constraint-satisfaction`
**L3** is a second, unreported surface of that report's **Warning 13**.

> L3: `description: "Constraint satisfaction has distinctive phenomenal character — the felt texture of navigating limits reveals consciousness as a selector, not a spectator."`

Warning 13 flagged only the L36 lead ("constraint satisfaction feels like something
*because* consciousness is doing genuine causal work at the interface" — re-verified
present on L36 this run). The description asserts the same thing on the metadata
surface. If Warning 13 is ever minted, **both lines belong in one task**; this report
does not widen its scope beyond naming the pairing.

## Secondary scan — deliberately not run

The driver's instruction was to scan for new conflicts in `topics/`, `concepts/` and
`positions/` **only if the four findings were all discharged**. Four of the four are
live, so no corpus scan was attempted and none is implied. The one extra pass above
is scoped to the frontmatter surface the live findings exposed and is reported with
its false-high rate.

## Method note

Counts here are **locus counts within four named families**, not corpus family
counts — the inverse of this series' usual convention, because this is a status run.
Every locus was re-read from disk in paragraph context and quoted as a sentence, not
a fragment. Absences were confirmed twice by structurally different means: Python
`str.count` / `str.find` returning an explicit offset rather than a piped grep
(`tenet-check-2026-09-08` in `todo.md` → **-1**; `conditioned` in
`research-programme-decisions-under-the-map` → **0**), plus a `### `-block split of
`todo.md` classifying open versus ✓-resolved so that resolved entries above the
marker could not be miscounted as coverage. Length figures are from
`tools.curate.length.analyze_length` with `DEFAULT_THRESHOLDS` printed, not quoted
from memory; that function is body-only, so frontmatter edits carry no word cost.
The 09-08 report's `concepts/philosophical-zombies` L141 citation was corrected to
L201 by reading the file rather than by trusting either report. No content file was
modified by this run.