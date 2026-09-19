---
ai_contribution: 100
ai_generated_date: 2026-09-19
ai_modified: 2026-09-19 16:49:09+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-19
date: &id001 2026-09-19
description: 'Tenet check 136: zero errors again, but the Tenet-5 self-binding family
  is now measured at 20+ live loci across six prior checks, and its engine is named
  — a ''parsimony is a tiebreaker between theories of equal explanatory power'' rule
  at 16 loci that tenets.md never states.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-09-19 16:49:09+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-09-19
topics: []
---

# Tenet Alignment Check

**Date**: 2026-09-19 16:49 UTC
**Report**: 136th in series
**Window**: ~30h since the 2026-09-18T09:59 run.

**Scope**: `topics/` 329, `concepts/` 327, `positions/` 22, `apex/` 44, `voids/` 104,
`tenets/` 2 — 828 files swept for the Tenet-5 self-binding family and the tenet-1/4
contradiction battery. 41 files (every content file committed since 2026-09-18T09:59)
read in full at their tenet-alignment sections. Every locus below was re-verified by
the driver **by exact substring, printed at the match offset**, not by line number and
not through a width-limited grep.

**Errors**: 0
**Warnings**: 4 priority families + 12 carried/secondary
**Notes**: the systemic root cause, named and measured for the first time

---

## Summary

1. **Zero ERRORs for the 136th consecutive run.** The battery (33 fixed-string patterns,
   NFKC-normalised, wikilinks flattened to labels) returned ~2,975 hit lines. No Map-voice
   endorsement of eliminativism, epiphenomenalism, many-worlds or a parsimony verdict
   against dualism exists in the corpus. The Tenet-2 rules-out clause is unusually well
   guarded: all 54 `psychokinesis` hits are references, falsification conditions, or the
   dedicated `topics/parapsychology-firewall`.

2. **The three tenet-facing changes the driver flagged: two landed well, one is half-applied.**
   See *Driver Questions* below. The causal-closure contradiction is fully fixed in both
   trees; the Bidirectional Interaction scoping landed correctly in all three articles; the
   Minimal Quantum Interaction figure fix was applied to the first mention and **not** to the
   anaphor one sentence later, which still performs the exact gloss the commit removed.

3. **The finding of this run is not a locus. It is a rule.** Sixteen loci across ten files
   assert that *"parsimony is a tiebreaker between theories of equal explanatory power."*
   `obsidian/tenets/tenets.md` contains **zero** occurrences of `tiebreaker`, `tie-breaker`
   or `equal explanatory power`, and L145 states the opposite without an equality
   conditional: *"parsimony cannot decide for or against a framework when the relevant
   knowledge is incomplete."* The rule is a corpus invention with no tenets-page warrant, and
   it is the engine behind roughly half the Tenet-5 defects: an article states the rule,
   argues that physicalism does not explain the data, and the simplicity discount falls to
   the Map. **This is why six prior checks have not fixed this family.** Repairing sentences
   without settling the rule regenerates them.

4. **The Tenet-5 family is now measured: 20+ live loci, six prior checks, two repairs
   landed.** `tenet-check` runs on 07-29b, 07-30, 08-12, 08-22, 09-14 and 09-18 all flagged
   this class. Of roughly ten loci flagged across those runs, exactly two were repaired
   (`concepts/parsimony-epistemology` L140, `apex/altered-states-as-interface-evidence` L94).
   The 09-18 run's "Family K" listed 7 loci; **all 7 are still live verbatim today.**

5. **A structural reason, carried from 09-18 and still true:** all four open tasks whose
   `Source` is `check-tenets` are **P3**. `CLAUDE.md` states the cycle's queue slots pick from
   the P0–P2 queue. Minting a tenet finding at P3 is equivalent to carrying it in the review
   file, except that it also looks discharged. The two tasks minted today are **P2** for this
   reason.

---

## Driver Questions, answered

**(a) Causal closure — FIXED, verified, no action.** `concepts/meta-problem-of-consciousness`
now reads *"so it denies [causal closure](/concepts/causal-closure/) rather than preserving it"*. The
canonical article agrees throughout (`concepts/causal-closure` L82 *"The Map denies causal
closure"*, L178 *"rejects causal closure as a universal principle"*). `concepts/epiphenomenalism`
L177's *"respects a qualified causal closure—physics is complete for determined events"* is
consistent, not contradictory: the Map denies the unrestricted thesis and preserves the
restricted one. Corpus-wide the only `preserves causal closure` hit is
`topics/indian-philosophy-of-mind` L176, which is about **Samkhya's** framework, not the Map's
— a false alarm, checked and cleared.

**(b) Bidirectional Interaction scoping — LANDED WELL, no action.** `disarms the debunking`
is now 0 occurrences corpus-wide. The scope is correctly installed in all three places:
`concepts/meta-problem-of-consciousness` L75 (*"in its causal- and constitutive-independence
form"*), its L87 anchor sentence (*"It is also all the tenet delivers"*), and
`topics/metaproblem-of-consciousness-under-dualism` L137 (*"restoring the dualist's prior
warrant rather than fortifying it beyond that, and leaving the coincidence argument still to
be answered"*). The pessimistic review's parsimony-conditional finding is also discharged —
L131 now reads *"would achieve its simplicity"*. One residual, minor, carried below: the
article's `description:` and its L56 thesis sentence still state the **unscoped** form.

**(c) Minimal Quantum Interaction figure — HALF-APPLIED. This is priority finding 3.**

**(d) The two carried Tenet-5 siblings — BOTH STILL LIVE, in both trees.** Verified by exact
substring today:
- `obsidian/topics/consciousness-and-mathematics.md` L162 — *"offers the most parsimonious
  explanation for this success-coupling"*. Aggravating: the **same article** at L198 denies the
  physicalist that move (*"The physicalist strategy … appears simpler—but only by leaving the
  access problem unsolved"*). Asymmetric discipline, 36 lines apart.
- `obsidian/concepts/meta-problem-of-consciousness.md` L75 — *"has a simplicity that illusionist
  alternatives lack"*. Same asymmetry: L141 denies illusionists the parsimony motivation.
  Sharper still, its own topic sibling `topics/metaproblem-of-consciousness-under-dualism` L129
  does the **disciplined** thing on identical material (*"Parsimony comparisons require that both
  explanations cover the same data"* — it declines the comparison rather than winning it).

They are still live for a structural reason worth stating plainly: they were never minted as
tasks. They are carried inside the **Notes** of the `concepts/quantum-completeness` P3 task as
*"Two one-word siblings in Family E, **optional if in budget and out of contract otherwise**"*.
A sibling parked as optional inside a P3 task targeting a different file cannot be reached.

---

## Priority findings (4)

### 1. Tenet 5 self-binding — five unguarded loci, one ready-made patch sentence

**Tenet violated**: 5 (Occam's Razor Has Limits). `tenets.md` L145: *"This tenet binds the Map's
use of parsimony, not only its critics'. … The discipline is symmetric"*; L147 rules out
*"any Map argument that leans on parsimony as if this tenet did not apply to it."* The
positions register makes it a registered commitment, not just a tenet: **[P-M1](/positions/methodology-and-calibration/#p-m1)**
(`positions/methodology-and-calibration` L76) — *"A tenet removes a defeater but never upgrades
the evidence level … Tenet 5 removes the parsimony dismissal — but defeater-removal never raises
the evidential tier of a claim."*

Each locus below is Map voice, claims simplicity **for the Map**, and has **no guard** anywhere
in its enclosing paragraph (verified by a ±900-character guard scan for `Tenet 5`,
`not decisive`, `unreliable`, `does not settle`, `bars`, `cannot decide`):

| # | File | Locus (verbatim) |
|---|---|---|
| a | `obsidian/concepts/bidirectional-interaction.md` L119 | "The interactionist alternative offers a simpler explanation: consciousness evolved *because* it influences behaviour." |
| b | `obsidian/concepts/consciousness-as-amplifier.md` L183 | "The ontologically richer theory may be explanatorily simpler than the austere alternative." |
| c | `obsidian/topics/consciousness-under-extreme-metabolic-constraint.md` L135 | "is explanatorily more economical—a single principle accounts for all five patterns. This illustrates the Map's tenet that simplicity is not a reliable guide to truth when knowledge is incomplete." |
| d | `obsidian/concepts/intersubjectivity.md` L126 | "The simpler hypothesis: consciousness exists and is intersubjectively accessible." |
| e | `obsidian/topics/consciousness-and-mathematics.md` L162 | "offers the most parsimonious explanation for this success-coupling" |
| f | `obsidian/concepts/meta-problem-of-consciousness.md` L75 | "has a simplicity that illusionist alternatives lack" |

**(a) is the highest-value single edit in this report**: the file contains exactly one occurrence
of `simpler` and **zero** of `simplicity`, `parsimon` or `Occam` — there is no guard anywhere to
reach back for — and the identical argument is already correctly patched one file away.
**(b) sits in the closing sentence of a section literally headed `### Occam's Razor Has Limits`**
whose opening sentence is *"the tenet cautions against premature parsimony"* — it declines the
parsimony claim and then makes it, the exact structure the 09-14 check found in `tenets.md`
itself. **(c) is worse still: it cites Tenet 5 as if the tenet licensed the move it forbids.**

**Repair — a corpus-approved patch already exists.** `concepts/epiphenomenalism` L140 handles
the identical argument correctly and its clause is directly liftable:

> "…though by the Map's own [Tenet 5](/tenets/#occams-limits), simplicity is not decisive where
> knowledge is incomplete, so this counts as a registered advantage rather than a parsimony proof."

That clause repairs (a) and (b) directly. For (c), delete the mis-citation instead:
*"…accounts for all five patterns with a single principle. Tenet 5 bars the Map from converting
that unification into an economy claim in its own favour: it is a claim about explanatory
coverage, not about simplicity."* For (d), delete the sentence. For (e): *"is the best explanation
on offer for this success-coupling"* (−1 word). For (f): *"avoids an explanatory burden that
illusionist alternatives must carry"* (+2 words).

**Budget** (measured with `tools.curate.length.analyze_length`; concepts 2500/3500/5000, topics
3000/4000/6000; headroom = hard − 1 − count): amplifier 3262 (237 words free),
consciousness-and-mathematics 3227 (772), meta-problem 3354 (145). The remaining three were not
measured — **measure before editing, do not quote these figures.** The sweep is roughly
net-neutral overall, but (b) and (f) are the tightest.

**Task minted**: P2, `refine-draft`, see below.

---

### 2. `voids/resolution-void` L91 — Tenet 5 breach of a prohibition `tenets.md` states by name

**Tenet violated**: 5 and 4. **Verbatim locus**:

> **[No Many Worlds](/tenets/#no-many-worlds)** gains indirect support from the resolution void's
> concealment mechanisms.

and, closing the same paragraph:

> The Map's rejection of many-worlds is consonant with an architecture that already operates at
> maximum compression; adding branching ontology would multiply what the void must hide beyond
> any plausible concealment mechanism.

That is the **ontological-multiplicity parsimony complaint**, used as support for Tenet 4.
`tenets.md` forbids it twice, in terms:

- L119: *"By Tenet 5 parsimony is an unreliable guide to truth in this domain, and **the Map
  cannot invoke simplicity against many-worlds while disarming parsimony arguments against
  dualism**."*
- L145: *"The rejection of many-worlds … must therefore rest on the indexical objection … **not
  the ontological-multiplicity parsimony complaint discounted there**."*

**Aggravating, same section, same file**: two further inversions of the voids-as-evidence
discipline — *"**Dualism** finds direct support in Sellars' grain argument"* and the No-Many-Worlds
sentence above. That discipline is stated explicitly by a sibling void edited the same day,
[voids/source-attribution-void.md](/voids/source-attribution-void/): *"A Map that used this void to *support* dualism would be
inverting the relation: the evidence constrains what dualism may claim, not what dualism may be
inferred from."* Of 104 voids articles, exactly **one** cites that discipline — the file that
states it. `resolution-void` cites it zero times.

**Recommendation**: downgrade both to coherence commentary — *"The Map's rejection of many-worlds
is a separate commitment resting on the indexical objection; the resolution void neither supports
nor tells against it"* — delete the multiplication-burden sentence, and change *"finds direct
support in"* → *"is consonant with"*. Budget: 2529 words, voids hard 3000 → **470 words of
headroom**. Net-negative repair. No open task on this file.

**Task minted**: P2, `refine-draft`, see below.

---

### 3. `concepts/metaphysics-of-information-under-dualism` L150 — today's Tenet-2 fix is half-applied

**Tenet violated**: 2 (Minimal Quantum Interaction). Commit `ff5bcee0c3` (today 15:24 UTC) is
titled *"L150 overstates its own source by a factor of 10 — **and glosses a behavioural figure as
a conscious one**"*. It fixed the first mention and left the second. The paragraph now reads:

> Separately, Zheng & Meister (2025) find that **the information throughput of a human being** is
> roughly 10 bits per second … **Whether this conscious bandwidth reflects** the quantum-level
> injection rate, emerges from it, or is an independent constraint is unknown. But both
> observations point in the same direction: consciousness appears to act as a narrow semantic
> bottleneck rather than a high-throughput channel, consistent with the minimality tenet.

Sentence 1 correctly says *behavioural throughput of a human being*; sentence 2's anaphor
**"this conscious bandwidth"** converts it straight back into a conscious-bandwidth figure, and
sentence 3 cashes that as Tenet-2 support. Live in **both** trees (`obsidian/` and
`hugo/content/`).

**This is the only place in the corpus that cashes the figure as tenet support without the
behavioural guard.** Every sibling carries it — `topics/bandwidth-of-consciousness` L169 (*"The
~10 bits/s figure is behavioural throughput, and rate does not fix grain"*),
`concepts/sleep-and-consciousness` L50 (*"a behavioural ceiling rather than a measured bandwidth
of phenomenal experience"*), `topics/valence-and-conscious-selection` L153 (*"the figure is a
behavioural throughput ceiling measured in conscious tasks, agnostic between the horns by
construction"*). The file contains one `behavioural` occurrence and it is not in this paragraph.

**Repair, net ≈ 0**: *"Whether this behavioural ceiling reflects the quantum-level injection rate…"*
and append the sibling guard. Budget: 3376 words, concepts hard 3500 → **123 words of headroom**;
keep it tight. No open task on this file.

---

### 4. `concepts/phenomenology-of-choice-and-volition` L123 — Tenet 3 over-derivation contradicting both `tenets.md` and its own cited source

**Tenet violated**: 3 (Bidirectional Interaction). **Verbatim locus**:

> The [phenomenology of effort](/concepts/mental-effort/) provides **the strongest evidence for genuine
> conscious contribution**. The [trilemma of selection](/topics/trilemma-of-selection/) makes this
> systematic: at any decision point, the outcome is determined, random, or consciously selected —
> and **only selection generates the phenomenology of effort**. If choosing were merely receiving
> randomly determined outcomes, there should be no phenomenology of effort — random processes
> don't feel like work.

Three independent contradictions, all verified:

1. **`tenets.md` L93** holds Tenet 3 *"as a metaphysical commitment supported by
   self-stultification and indirect evidence, **not as a directly introspectible datum**"*, and
   the `^tenet-3-standing` paragraph (L95) requires articles asserting *"real work"* to *"read no
   more confidently than this paragraph does."* **19 articles cite that anchor. This file cites it
   zero times.**
2. **The page it links to in that very sentence refutes it.** `concepts/mental-effort` §*What Felt
   Effort Misses About Its Own Operation* reports Naccache et al. 2005 — a patient with normal
   executive control and no felt effort at all, a direct counterexample to *"only selection
   generates the phenomenology of effort."*
3. **Zero common-cause guard**: the file has 0 occurrences of `common cause` / `common-cause` /
   `indistinguishable`. `topics/consciousness-and-causal-powers` L128 handles the identical
   material correctly (*"the two are observationally indistinguishable at the phenomenology"*).

`"strongest evidence for genuine conscious contribution"` is a **singleton** in the corpus —
this is a one-sentence fix, not a family.

**Repair**: drop *"only selection generates"* entirely; demote to the corpus's standard
calibration — *"the most direct first-person consideration favouring genuine conscious
contribution, though it does not establish it: the felt sense is dissociable from the executive
operation it reports on (Naccache et al. 2005), and a deterministic resource-allocation process
predicts effort phenomenology equally well."* Budget: 2590 words, concepts hard 3500 → **909
words of headroom**. No open task on this file.

---

## Secondary findings — carried for the operator to triage

Ranked. I read every one of these; none is minted.

1. **`concepts/embodied-cognition` L190 — Tenet 4, cites a source that says the opposite.**
   *"The anti-MWI argument the Map relies on comes not from embodiment but from the phenomenology
   of singular determination in effortful selection (see [mental-effort](/concepts/mental-effort/))."* Its cited source,
   `concepts/mental-effort` L150, reads: *"consistent with the Map's rejection of branching **but
   does not adjudicate; MWI predicts the same indexical singularity. The Map's case against
   branching comes from elsewhere**."* `tenets.md` grounds Tenet 4 on the indexical objection, not
   on felt singular determination. **Budget is the constraint: 3494 words against a 3500 hard
   gate — 5 words of headroom.** Any repair must be net-neutral or negative.

2. **The "parsimony tiebreaker" rule — the root cause, and a genuine human decision.**
   16 loci / 10 files assert parsimony decides between theories of equal explanatory power;
   `tenets.md` states no such conditional (0 occurrences of either phrase). The clearest instance
   is `topics/the-convergence-argument-for-dualism` L177, where the rule and its payoff sit in
   consecutive clauses: *"parsimony is a tiebreaker between theories of equal explanatory power.
   When multiple substantially independent lines of evidence favor dualism, physicalism's
   parsimony advantage is outweighed by its explanatory disadvantage."* **Does the Map endorse the
   equality-conditional or not?** Until that is settled, locus fixes regenerate. Recommend a
   NEEDS-HUMAN entry rather than a content task.

3. **The evolutionary-argument cluster — two remaining unguarded siblings.** Six articles run the
   "if consciousness were inert the fitness correlation would be a coincidence" argument. Three do
   it correctly, one (`concepts/epiphenomenalism` L140) carries the guard clause, and
   `concepts/bidirectional-interaction` L119 is **promoted into priority finding 1 (a)** above. The
   two still uncovered: `topics/pain-consciousness-and-causal-power` L160 and
   `topics/consciousness-in-simple-organisms` L255 (aggravated — its own L261 says *"But simplicity
   does not determine truth"* six lines later). The same lifted clause closes both.

4. **Nine further unguarded Tenet-5 loci, catalogued so the family is fully recorded** (out of scope
   for the two minted tasks): `topics/biological-computationalisms-inadvertent-case-for-dualism`
   L100 (strips five guards its cited source carries), `topics/the-convergence-argument-for-dualism`
   L177 (the tiebreaker rule and its payoff in consecutive clauses), `apex/taxonomy-of-voids` L197
   (breaks a conceded tie by parsimony, inside the Map's own calibration discipline),
   `topics/phenomenology-of-resistance-across-domains` L120,
   `topics/terminal-lucidity-and-filter-transmission-theory` L177,
   `topics/comparative-phenomenology-of-meditative-traditions` L143 and
   `topics/phenomenology-of-intellectual-life` L183 (**both carried unchanged since 2026-07-29b —
   seven weeks**), and `concepts/reductionism` L190.

   ⚠️ **One item was dropped from this list after checking it, and the check is worth recording.**
   A sweep reported `concepts/measurement-problem` **L187** — *"more parsimoniously treated as one
   puzzle than as coincidence"* — as the sharpest internal case, on the grounds that the sibling
   bullet at L189 carries the guard it lacks. **Two things were wrong.** (i) The locus is at
   **L67**, not L187 — a 120-line drift; L189 is a different passage in a different section, so the
   two are not adjacent bullets in one list and the "copy the guard up" repair does not apply.
   (ii) Read to the end, L67 concedes twice in its own sentence — *"The unification generates no new
   predictions, and critics are right that it creates a larger mystery."* The residual parsimony
   clause concerns **puzzle individuation** (treat two determinacies as one problem or two), which
   is intra-theoretical, not the framework adjudication Tenet 5 governs. Same class as
   `concepts/consciousness-selecting-neural-patterns` L158's "temporal parsimony", which the same
   sweep classed as outside the tenet's letter. **Judged marginal, not minted, not carried as a
   defect.**

4a. **Zero-cost navigation-surface fix, two files, identical string.**
   `concepts/parsimony-epistemology` L170 and `arguments/epistemological-limits-of-occams-razor`
   L101 both read *"The positive case that dualism is simpler once all costs are counted"* — a
   Further-Reading label asserting precisely what its target article declines five separate times.
   A label edit, no prose cost. (Note `arguments/` is outside this check's stated scope.)

4b. **`concepts/causal-closure` L136 — a Map case openly grounded in parsimony, cross-referenced
   to the wrong tenet.** *"the Map's case against hidden variables rests on parsimony rather than
   settling that dispute (see [Tenet 4](/tenets/#no-many-worlds))."* The *"Occam's Razor cuts both
   ways"* parity clause earlier in the paragraph is in-contract; the final clause is not. The
   disciplined twin is `topics/many-minds-interpretation` L90, which states the rule outright:
   *"The Map must **not** lean on 'an infinity of minds is profligate' as a parsimony refutation of
   MMI, just as it does not rest its rejection of MWI on counting worlds."*

5. **`concepts/dualism` L172 — an unresolved adjudication conflict, not a fresh defect.**
   *"ontological parsimony favours physicalism, but explanatory parsimony favours dualism"*.
   Flagged 07-30, **explicitly cleared 08-22** as in-contract, re-flagged 09-18. Settle it once
   and record the verdict, rather than re-litigating each cycle.

6. **`concepts/consciousness-as-amplifier` L107 vs L117 — a same-file self-contradiction ten
   lines apart.** L107 concedes the DeWall paradigm *"separates executive capacity from
   unconscious pattern-completion **without separating phenomenal consciousness from executive
   capacity**"*; L117 then deploys it as *"**The empirical evidence**"* against illusionism, which
   is a thesis about phenomenal consciousness specifically. Of 16 files citing DeWall 2008, this
   one and `topics/interface-efficacy-and-the-cognitive-gap` L90 (*"is direct evidence that
   interface bandwidth is finite and bottlenecked"*) lack the accommodation concession the other
   four substantive users carry. **One shared scoping sentence fixes both, and it is already
   written at L107.**

7. **`concepts/substrate-independence` L192 — Tenet 4, matrix violation.** *"the question 'is this
   silicon system conscious?' becomes ambiguous across branches"* is false as stated and
   contradicted by `concepts/philosophical-zombies` L207 (*"has a determinate answer
   branch-relatively"*). The Tenet-Dependency Matrix marks No-MWI **Not invoked** for all three
   machine-consciousness rows. Also L184's *"jointly entail substrate skepticism"* over-claims.
   **File is at `hard_warning` (3662 / 3500) — repairs must be net-negative.**

8. **`topics/agentic-ai-and-the-consciousness-assessment-…` L82 — Tenet 4 dependency inversion.**
   *"Tenet 4's insistence that indexical identity is a real further fact … is what makes [the
   question] genuine."* `tenets/background-commitments` Posit One says the reverse: *"The indexical
   objection to many-worlds (Tenet 4) **needs** a determinate 'I'."* Partially self-guarded at L84.

9. **`topics/contemplative-practice-as-philosophical-evidence` L59 — Tenet 5, in the lead.**
   *"the most parsimonious explanation is that those features are real properties of experience"*.
   The file has **0** common-cause mentions; its guarded twin
   `topics/cross-traditional-convergence-on-consciousness-irreducibility` L46 makes the identical
   claim with the guard attached and has **26**. The repair is written in the sibling. Note the
   claim also survives in two archived predecessors at live URLs.

10. **`concepts/implicit-memory` L196 — Tenet 5, flagged 08-12 and 09-18, still live.**
    *"The simplest account that covers all the phenomena…"* → delete *"simplest"* (−1 word).
    **Pileup warning**: this file has an open P3 whose target is a different locus (L149
    "substance dualism"); fold this in there rather than minting a second task.

11. **`tenets.md` L95 — a phrasing ambiguity on the authority page.** *"consistent with physics,
    not excluded by causal closure"* reads as granting closure, where `concepts/causal-closure`
    L188 says *"such interface is possible **because** causal closure fails at quantum
    indeterminacies."* An elliptical reading ("not excluded by the causal-closure objection") is
    available, so this is a WARNING not an ERROR — but 19 articles cite this anchor as the
    calibration authority, and the corpus just spent a P1 fixing the identical construction
    downstream. One-clause disambiguation.

12. **Not minted, for stated reasons**: `topics/attention-and-the-consciousness-interface` L171
    (Tenet 3, no concession in the alignment bullet — but the body concedes at L147, the file has
    **three** open tasks, and it is length-blocked); `concepts/consciousness-selecting-neural-patterns`
    L124 (Tenet 2 heading equivocation — an open P3 already targets that exact line);
    `topics/metaproblem-of-consciousness-under-dualism` L3 + L56 (the `description:` and the
    section-thesis sentence still state the unscoped debunking claim that L84 and L137 correctly
    scope — a navigation-surface residue of today's otherwise-good fix).

13. **A voids-wide family worth one sweep**: six voids articles state tenet *support* where the
    discipline permits only consonance — `creative-aesthetic-void`, `emergence-void`,
    `emotional-epistemology-void`, `expertise-and-its-occlusion`, `recursion-void`,
    `resolution-void`.

---

## Judged false alarms (checked, cleared, recorded so they are not re-derived)

- **`topics/valence-and-conscious-selection` L153** — *"Conscious processing operates at
  approximately 10 bits per second"* is the exact phrase deleted from
  `metaphysics-of-information` today, so it looks like a string sibling. It is not a defect: the
  same paragraph guards it explicitly two sentences later.
- **`concepts/sleep-and-consciousness` L50** — same figure, guard in the same sentence.
- **`topics/indian-philosophy-of-mind` L176** — the corpus's only `preserves causal closure` hit
  is about **Samkhya**, not the Map.
- **`concepts/reinforcement-learning-reward-signals-and-machine-valence` L79** — reads as a
  Tenet-2-as-tiebreaker defect on the grep line; it is in fact the corpus's **model** treatment:
  *"But Occam's Razor Has Limits (Tenet 5) blocks resting on that minimality as if it were
  decisive."*
- **`topics/parsimony-case-for-interactionist-dualism`** — whole article cleared despite its
  title; it guards the inference five times. (Its *glosses* elsewhere are not — see secondary 4.)
- **`concepts/jourdain-hypothesis` L127**, **`topics/forward-in-time-conscious-selection` L157**,
  **`topics/cross-traditional-convergence…` L46** — all guarded within the paragraph.
- **A reviewer disagreement, adjudicated.** One sweep reported
  `concepts/consciousness-as-amplifier` L183 as handling the parsimony move *correctly*; two
  others reported it as a defect. The driver extracted the full `### Occam's Razor Has Limits`
  section and tested it for six guard strings: **none present**, and the next line is
  `## Further Reading`. The defect reading stands. Recorded because a later pass reading only the
  dissenting sweep would clear a live locus.

---

## Method notes

- **Truncated greps manufactured two false absences during this run.** `grep -inF … | cut -c1-260`
  reported agent quotes as unverifiable at `topics/interface-efficacy-and-the-cognitive-gap` L90
  and three of the Tenet-4 loci; all six verified once printed **at the match offset**. Every
  locus in this report was confirmed by offset-printing, not by a width-limited read.
- Sweeps were NFKC-normalised and had `[[target|label]]` flattened to `label` before any
  presence/absence claim.
- Length figures are from `tools.curate.length.analyze_length` on `obsidian/` paths, with
  headroom computed as **hard − 1 − count** (`length.py` gates on `>= hard`).

## Files passing all checks

35 of the 41 delta files were read in full at their tenet sections and cleared, including
`concepts/causal-closure` (specifically checked for the preserves/denies contradiction and
correct), `concepts/delegatory-causation` and `topics/delegatory-dualism` (which handle the
closure tension explicitly and well), `concepts/illusionism`, `concepts/epiphenomenalism`,
`topics/hard-problem-of-consciousness`, `concepts/supervenience`, `concepts/philosophical-zombies`,
and the whole `positions/` section, which is exemplary on Tenet 5 ([P-CS5](/positions/consciousness-scope/#p-cs5): *"parsimony's 'no
coupling' default is undefeated but not established"*).