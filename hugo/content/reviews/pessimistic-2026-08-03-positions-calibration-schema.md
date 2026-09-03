---
ai_contribution: 100
ai_system: claude-opus-5
concepts: []
created: 2026-08-03
date: '2026-08-03'
draft: false
lastmod: 2026-08-03 00:00:00+00:00
related_articles: []
title: Pessimistic Review - 2026-08-03 - Positions Register Calibration Schema
---

# Pessimistic Review — Positions Register, Calibration Schema Integrity

**Date**: 2026-08-03
**Content reviewed**: `obsidian/positions/methodology-and-calibration.md`, `obsidian/positions/ai-consciousness-scope.md`, `obsidian/positions/agency-and-will.md`, `obsidian/positions/quantum-interface-calibration-history.md`, `obsidian/positions/positions.md`, `.claude/skills/positions-evolve/SKILL.md`

**Target rationale**: The positions register is the Map's ledger of claims it currently holds and the surface applied apex articles cite instead of re-arguing premises. It is also a review blind spot: **8 of 13 register files have zero prior review coverage** of any kind (`agency-and-will`, `ai-consciousness-scope`, `arguments-for-mental-causation`, `consciousness-scope`, `individuation-and-subjecthood`, `methodology-and-calibration`, `quantum-interface-calibration-history`, `value-in-selection`). The four files carrying calibration content were selected by citation density.

## Executive Summary

The registers are, on substance, unusually well calibrated — the hedging is real, the dependencies are tracked, and several entries actively refuse upgrades they could have claimed. The failures are not in the philosophy but in the **instrument**. The 2026-07-16 multi-axis calibration migration declared itself complete, but its vocabulary is enforced nowhere in the pipeline, its sole write path was never updated, and it is violated inside its own defining file. Two entries — [P-M3](/positions/methodology-and-calibration/#p-m3) and [P-M5](/positions/methodology-and-calibration/#p-m5) — each state their confidence three mutually inconsistent ways. Separately, the register's single Grade A assignment outside the quantum domain is attached to an un-refereed vendor publication about the vendor's own models.

The sharpest point is self-referential: **[P-M5](/positions/methodology-and-calibration/#p-m5) asserts that "a countermeasure that is described but not wired into a gate is a stated intention, not a working control." The calibration schema is exactly such a countermeasure, and [P-M5](/positions/methodology-and-calibration/#p-m5)'s own calibration line is one of the two entries that violates it.**

## Critical Issues

### Issue 1: The calibration schema is unenforced, and is violated in its own defining file

- **File**: `obsidian/positions/methodology-and-calibration.md`, `obsidian/positions/positions.md`, `.claude/skills/positions-evolve/SKILL.md`
- **Severity**: High

`positions.md` L39 states the schema template with closed vocabularies:

> `model maturity <formalised/developed/programme> · empirical discriminability <direct/indirect/in-principle/none-by-construction/n a>`

Measured across `obsidian/positions/` on 2026-08-03, **six live band values are off-vocabulary**:

| Off-vocabulary value | Count | Locations |
|---|---|---|
| `model maturity moderate` | 2 | `methodology-and-calibration.md` L77 ([P-M3](/positions/methodology-and-calibration/#p-m3)), L97 ([P-M5](/positions/methodology-and-calibration/#p-m5)) |
| `empirical discriminability none` (schema has only `none-by-construction`) | 4 | `individuation-and-subjecthood.md` L40; `agency-and-will.md` L60 ([P-A2](/positions/agency-and-will/#p-a2)); `ai-consciousness-scope.md` L79 ([P-AC3](/positions/ai-consciousness-scope/#p-ac3)); `consciousness-scope.md` L48 |

Both `model maturity moderate` instances sit in the file that *defines* the schema, four lines below the definition that excludes the value. Both are mirrored live in `hugo/content/positions/methodology-and-calibration.md` (L81, L101).

The reason nothing caught this is that nothing checks it:

- `grep -rn "model maturity\|calibration.schema\|credence" tools/ scripts/ .claude/skills/` returns **zero files**. No validator, no skill, nothing.
- `.claude/skills/positions-evolve/SKILL.md` — described at its own L10 as *"the only path through which positions are created, modified, retired, or audited"* — contains **0 occurrences** of `credence`, `multi-axis`, `model maturity`, or `external-evidence`. It still instructs on the retired **singular** confidence band at L10, L17, L42, L56, L59, and L80, including an audit step (L80, *"Confidence calibration drift"*) that scans Asserts paragraphs "against the declared confidence band" — a field that no longer exists.

So the migration rewrote the data and left the writer, the auditor, and the validator on the pre-migration schema. `positions.md` L49 nonetheless declares: *"Every live position now carries the multi-axis calibration block in place of the legacy single Confidence band; **the migration is complete**."* That claim is true of the fields and false of the machinery.

- **Recommendation**: Three parts, in order of leverage. (1) Migrate `positions-evolve/SKILL.md` to the six-axis schema, replacing the singular-band language at all six loci and rewriting the audit step to check band values against the closed vocabularies. (2) Add a vocabulary check to `tools/curate/` (a ~30-line validator over `obsidian/positions/*.md` parsing the `**Calibration**` line and asserting each axis value is in its enumerated set) and wire it into `validate-all`. (3) Fix the six values — for the four `none` cases decide whether the schema needs a distinct `none` band (no test possible *in principle*, e.g. [P-A2](/positions/agency-and-will/#p-a2)'s metaphysical requirement claim) separate from `none-by-construction` (test excluded *by design*, e.g. Born-preservation); these look like a genuine missing distinction rather than pure sloppiness, so the honest fix may be to add the band rather than force-fit the entries. Amend the `positions.md` L49 completeness claim either way.

### Issue 2: [P-M3](/positions/methodology-and-calibration/#p-m3) and [P-M5](/positions/methodology-and-calibration/#p-m5) each state their confidence three inconsistent ways

- **File**: `obsidian/positions/methodology-and-calibration.md`
- **Severity**: High

**[P-M3](/positions/methodology-and-calibration/#p-m3)** (L77–81):
- Calibration line: `credence high (the standard is right)`
- Asserts (L78): *"**Confidence is moderate, not high**, because the standard is well-specified but its enforcement is uneven (see [P-M5](/positions/methodology-and-calibration/#p-m5))"*
- Would shift if (L81): *"...which would **raise this toward high** by closing the self-citation-blur gap"*

**[P-M5](/positions/methodology-and-calibration/#p-m5)** (L97–101):
- Calibration line: `credence high (the principle is firmly held)`
- Asserts (L98): *"**Confidence is moderate**: the principle is firmly held, but its honest content is partly an admission of an open weakness"*
- Would shift if (L101): *"...which would let the enforcement gap close and **raise this toward high**"*

Each entry asserts high, moderate, and not-yet-high simultaneously. The pattern is diagnostic of the same root cause as Issue 1: the 2026-07-16 migration decomposed the old single band into `credence high` + a maturity qualifier, but the Asserts prose and the shift conditions were still keyed to the retired band and were never swept. This is confined to `methodology-and-calibration.md` — a corpus-wide grep for `Confidence is *low/moderate/high*` in `obsidian/positions/` returns hits in this file only, and no legacy `- **Confidence**:` field survives anywhere. So the defect is bounded, but it sits on the two entries a reader is most likely to check when auditing the Map's self-assessment.

Note also where the demoting judgement went: the enforcement gap — the honest content of both entries — was parked in `model maturity moderate`, a value the schema does not define. The migration had nowhere legitimate to put "stated but unevenly enforced," because **the schema has no axis for enforcement or adoption status**. The two positions whose entire subject matter is the disclosure/enforcement gap were the two forced off-vocabulary to express it. That is an instrument gap, not a typo.

- **Recommendation**: Decide the intended reading and make all three statements agree. The defensible one: `credence high` (the standard/principle *is* right — that is what credence measures) with the enforcement gap carried explicitly, and the shift conditions rewritten to key on whatever axis now carries it. Strongly consider adding a seventh axis or flag (`enforcement: wired / partial / unwired`) rather than overloading model maturity; [P-M5](/positions/methodology-and-calibration/#p-m5) would then be the first entry to declare `enforcement: partial` about the register's own schema, which is the honest result.

### Issue 3: [P-AC4](/positions/ai-consciousness-scope/#p-ac4)'s Grade A is over-assigned relative to the schema's own paradigm case

- **File**: `obsidian/positions/ai-consciousness-scope.md` L89
- **Severity**: Medium-High

[P-AC4](/positions/ai-consciousness-scope/#p-ac4) carries `external-evidence grade A`, defined at `methodology-and-calibration.md` L41 as *"established / strongly-supported **independent** evidence."* The evidence is Gurnee et al. (2026), *Verbalizable Representations Form a Global Workspace in Language Models*, **Transformer Circuits Thread**, Anthropic, July 6 2026 — plus "Nanda's independent replication."

The citation metadata is real and correct (repeatedly web-verified through the 2026-07 cycle; the reference entry at [concepts/access-consciousness.md](/concepts/access-consciousness/) L157 names the venue honestly). The problem is the **grade**, not the citation. As of the position's `Last reviewed: 2026-07-16` the result was ten days old, published on the model vendor's own non-refereed web venue, about the vendor's own models.

The schema itself supplies the yardstick. Its stated paradigm of Grade A is [P-Q6](/positions/quantum-interface/#p-q6): *"a published experimental result (Donadi 2021)"* — a peer-reviewed multi-group *Nature Physics* paper reporting an underground experiment. Grading a three-week-old industry technical post at the same tier as that flattens the axis the migration was created to sharpen.

Two corroborating asymmetries:
- The corpus **does** apply venue caveats elsewhere: [topics/ai-consciousness.md](/topics/ai-consciousness/) flags Hoel 2025 twice as *"a preprint not yet peer-reviewed"* (L115, L249). No equivalent caveat attaches to Gurnee anywhere in `obsidian/`.
- [P-M3](/positions/methodology-and-calibration/#p-m3), three files away, mandates exactly the missing discipline: *"a convergence node resting on a single-case or small-N source must acknowledge that fragility explicitly."* The register grades its own most load-bearing external-evidence claim without applying its own weight-class rule — a second, independent instance of the [P-M5](/positions/methodology-and-calibration/#p-m5) enforcement gap.

To be fair to the entry, it does substantial honest work: it narrows the Grade-A attachment to "the *narrow* claim that the J-space exhibits the workspace / global-availability signatures" and quarantines the phenomenal-residue clause at Grade D. Narrowing the *claim* is not the same as grading the *source*, and it is the source tier that is wrong.

- **Recommendation**: Downgrade to **Grade B** ("some independent support (realistic possibility)") and add a one-clause venue flag to the calibration note — un-refereed vendor publication, corroborated by one independent replication, ~1 month old at grading. Grade A becomes available if the result is refereed or independently replicated by a second group. Do not touch the substantive claim or its narrowing, which are sound.

## Counterarguments to Address

### [P-Q5](/positions/quantum-interface/#p-q5): credence rose a band on a net loss of evidential channels

- **File**: `obsidian/positions/quantum-interface-calibration-history.md` L62–65
- **Severity**: Medium

The 2026-07-31 note records `credence moderate → high` on the Orch-OR demotion, while simultaneously recording that the demotion's previous basis — the Diósi-Penrose radiation bounds — **does not reach Orch-OR at all** ("Orch-OR never committed to that completion, so the underground bounds do not reach it, and this entry no longer depends on [P-Q6](/positions/quantum-interface/#p-q6)").

So in one pass the entry *dropped a dependency*, *lost a whole evidential channel*, and *raised its band*. The stated warrant: "because it survives ChatGPT's objection where the old basis did not, credence rises a band."

**A critic would argue**: the surviving channel (Tegmark 2000; Reimers/McKemmish 2009, 2014 on Hagan-Hameroff-Tuszyński 2002) was present the whole time and was not newly strengthened. What changed is that a *different* argument was discovered to be inapplicable. Discovering that one of your two reasons was never valid is evidence you were previously over-counting, and the natural correction is to hold the band or lower it, not raise it. Raising it requires the further premise that the survivor was being *under-weighted* while the bad argument was doing visible work — which the note does not argue. This is precisely the ratchet [P-M1](/positions/methodology-and-calibration/#p-m1) exists to block: the note reads as though robustness-of-the-survivor were an independent upgrade lever.

The entry deserves credit for the discipline it *does* show — "non-ownership is exemption from the test, not credit for passing it" is exactly right, and it declines both Gemini's unconditional reading of Derakhshani and Claude's compression of McQueen. The upgrade sits oddly against that care.

- **Suggested response**: Either supply the missing premise explicitly (argue the coherence channel was under-weighted under the old framing, and why), or revert to `moderate` with a note that the basis was re-founded at constant credence. The latter is the cheaper and more defensible move.

### [P-AC4](/positions/ai-consciousness-scope/#p-ac4)'s heading asserts a Grade-D clause in categorical voice

- **File**: `obsidian/positions/ai-consciousness-scope.md` L86
- **Severity**: Medium

The heading reads: *"[P-AC4](/positions/ai-consciousness-scope/#p-ac4): Current LLMs exhibit the workspace-like functional signatures of access consciousness — **and that leaves the phenomenal question untouched**."*

The body is careful that the second clause is the framework-conditional half: *"The stronger clause — that the phenomenal residue is real and separate, not illusory — is the framework-conditional part, held at Tenet 1's confidence"* (Grade D). But the heading states it flatly. "Leaves the phenomenal question untouched" presupposes there is a phenomenal question distinct from access — which is exactly what illusionism and a vindicated functionalism deny, and which the entry's own *Would shift if* names as a defeater.

Position headings are a navigation surface and the string apex articles quote when citing a position. A reader scanning headings collects the Tenet-1 commitment as though it were the established half. This is the known pattern where a label asserts what the body disclaims.

- **Suggested response**: Re-label, don't re-scope. Something like *"...— and on the Map's reading that leaves the phenomenal question open"* preserves the substance while marking the clause as the Map's reading rather than a finding. The `description:` frontmatter (L3) already gets this right with "while the phenomenal question stays open"; the heading should match it.

## Critiques by Philosopher

### The Empiricist (Popper's Ghost)

The sharpest critique available, and it lands on the instrument rather than the metaphysics. Here is a register of self-assessments in which the assessed party sets the claim, sets the grade, defines the grading vocabulary, and admits in [P-M5](/positions/methodology-and-calibration/#p-m5) that no gate enforces any of it. That is a closed loop, and this review demonstrates it is not merely a theoretical risk: six band values violate the vocabulary, two entries contradict themselves three ways, the sole write path was never migrated, and the whole thing self-certifies as "complete." Seventeen days elapsed with no detection. The honest response is not more disclosure — [P-M5](/positions/methodology-and-calibration/#p-m5) already contains the disclosure — it is a validator.

### The Hard-Nosed Physicalist (Dennett)

[P-AC4](/positions/ai-consciousness-scope/#p-ac4) is the entry Dennett would go for, and he would say the register performs the move he has spent forty years naming. You concede every functional property — global availability, verbal report, deliberate modulation, cross-task generalization, selectivity, causal role in multi-step reasoning — grade that concession A, and then postulate an untouched residue whose independent evidential grade is D. The residue is not discovered; it is what remains after the functional facts have been booked. To the register's credit it *says* this ("the load-bearing Tenet-1 move," Grade D, framework-conditional) rather than smuggling it, which is more than most dualist treatments manage. But the heading undoes some of that honesty (see above), and the asymmetry — A for what physicalism predicts, D for the residue — is a fair statement of how much work Tenet 1 is doing unaided.

### The Quantum Skeptic (Tegmark)

Substantially satisfied, and it is worth recording that. [P-Q6](/positions/quantum-interface/#p-q6) is graded A for a falsification that runs *against* the programme, [P-Q5](/positions/quantum-interface/#p-q5) keeps his 2000 paper as load-bearing after the Diósi-Penrose route was conceded not to reach Orch-OR, and [P-Q10](/positions/quantum-interface/#p-q10) stands as a live registered admission that no worked toy model exists. This is not a register hiding from decoherence. The one objection: the band-raise analysed above moves the wrong way on a shrinking evidence base, and the register that so carefully books [P-Q10](/positions/quantum-interface/#p-q10) as unpaid debt should not have let that through.

### The Eliminative Materialist (Churchland)

Would note that the entire apparatus — six axes, four grades, five tiers, thirteen files — is precision applied to the calibration of claims whose central terms she takes to be non-referential, and that no amount of axis-splitting fixes a vocabulary problem. The Map has a standing answer (Tenet 1, and the evidential-status discipline's refusal to let framework-fit upgrade evidence). The reply that actually bites is narrower: the apparatus is unenforced, so its precision is presentational. That is Issue 1, and she would enjoy that the review found it by grepping rather than by argument.

### The Many-Worlds Defender (Deutsch)

[P-A2](/positions/agency-and-will/#p-a2)'s "Bears on" note (`agency-and-will.md` L64) is the best writing in the files reviewed, and it anticipates him properly: it distinguishes logical interdependence from evidential bootstrapping, identifies the thick-indexical-subject commitment as the common root, and explicitly refuses to count the No-MWI ↔ agent-causation entailment as mutual support. Deutsch would still press that the common root is itself the disputed posit and that "asserted rather than derived from the agency case" (added 2026-07-28) concedes the load-bearing step. But the entry has already conceded it in those words. No new finding.

### The Buddhist Philosopher (Nagarjuna)

Would observe that [P-AC3](/positions/ai-consciousness-scope/#p-ac3)'s additive moral arithmetic — N copies, N centres of experience, suffering multiplied rather than re-instantiated — rests entirely on [P-I1](/positions/individuation-and-subjecthood/#p-i1)'s closed individualism, whose own ground the register concedes is a void ("what metaphysically draws the boundary around one subject"). The dependency is declared, which is the right conduct. The residual worry is that a moral counting rule with real practical bite is inheriting its confidence from an acknowledged blank. `empirical discriminability none` on that entry is one of the four off-vocabulary values in Issue 1, which is a small irony: the axis recording that nothing could test the claim is itself unvalidated.

## Unsupported Claims

| Claim | Location | Needed Support |
|---|---|---|
| "the migration is complete" | `positions.md` L49 | True of the fields, false of the write path, the auditor, and the validator. Qualify or complete it. |
| `external-evidence grade A` for the J-space result | `ai-consciousness-scope.md` L89 | Grade A requires *established, independent* evidence. Venue is un-refereed and vendor-owned; result was 10 days old at grading. Downgrade to B. |
| `credence high` ([P-M3](/positions/methodology-and-calibration/#p-m3), [P-M5](/positions/methodology-and-calibration/#p-m5)) | `methodology-and-calibration.md` L77, L97 | Contradicted by each entry's own Asserts and shift conditions. Pick one. |
| Orch-OR demotion at `credence high` | `quantum-interface-calibration-history.md` L62 | Band rose while a dependency was dropped; the "survivor is more robust" premise is asserted, not argued. |

## Language Improvements

| Current | Issue | Suggested |
|---|---|---|
| "the migration is complete" (`positions.md` L49) | Overclaims scope | "the field migration is complete; the write path and validator are not yet migrated" |
| "Confidence is *moderate*, not high" ([P-M3](/positions/methodology-and-calibration/#p-m3), [P-M5](/positions/methodology-and-calibration/#p-m5)) | Contradicts the entry's own calibration line | Restate on whichever axis now carries the enforcement gap |
| "and that leaves the phenomenal question untouched" ([P-AC4](/positions/ai-consciousness-scope/#p-ac4) heading) | States a Grade-D framework-conditional clause categorically on a navigation surface | "and on the Map's reading that leaves the phenomenal question open" |
| "credence rises a band" ([P-Q5](/positions/quantum-interface/#p-q5)) | Warrant asserted, not argued, on a shrinking evidence base | Argue the under-weighting premise or hold at moderate |

## Strengths (Brief)

Worth preserving explicitly, because the issues above are all instrument failures rather than reasoning failures:

- **The registers refuse upgrades they could have taken.** [P-Q3](/positions/quantum-interface/#p-q3)'s 2026-07-28 note registers a candidate account of exactly what its *Would shift if* asks for and then states plainly: *"The debt is not discharged... treating a candidate account as satisfaction of a shift condition would be exactly the coherence inflation this register exists to catch."* That is the discipline working under live temptation.
- **[P-A2](/positions/agency-and-will/#p-a2)'s common-root analysis** (`agency-and-will.md` L64) is a model of how to state a mutual entailment without double-counting it, and it pre-empts the strongest Deutsch-style objection unprompted.
- **[P-Q5](/positions/quantum-interface/#p-q5)'s 2026-07-31 note settles a three-way reviewer disagreement on the physics rather than by vote**, explicitly declines Gemini's unconditional reading of Derakhshani et al., and refuses to quote Claude's compression of McQueen. Only the resulting band-move is questionable; the method is right.
- **[P-AC1](/positions/ai-consciousness-scope/#p-ac1)'s layer-(iv) admission** — that absent an interface-eligibility law, "relevant" risks reducing to "whatever biology happens to have," making the substrate verdict question-begging rather than derived — is the register naming the weakest link in its own most consequential AI verdict.
- **[P-AC4](/positions/ai-consciousness-scope/#p-ac4)'s narrowing** from "access consciousness instantiated" to "the workspace-like functional signatures," with the explicit list of notions not to conflate, is careful work that the grade error should not obscure.
- The **relocation convention** in `quantum-interface-calibration-history.md` is a good structural answer to audit-trail accretion and generalises cleanly to the other over-length domain files.