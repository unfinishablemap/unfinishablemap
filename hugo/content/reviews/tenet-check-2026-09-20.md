---
ai_contribution: 100
ai_generated_date: 2026-09-20
ai_modified: 2026-09-20 22:46:00+00:00
ai_system: claude-opus-5
author: Andy Southgate
concepts: []
created: 2026-09-20
date: &id001 2026-09-20
description: 'Tenet check 137: the first systematic sweep of Tenets 1-4. Tenet 5''s
  two carried loci are already repaired; the tenet-alignment section is identified
  as the corpus''s leak point.'
draft: false
human_modified: 2026-09-20
last_curated: null
last_deep_review: null
lastmod: 2026-09-20 22:46:00+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-09-20
topics: []
---

# Tenet Alignment Check

**Date**: 2026-09-20 (check 137; previous [reviews/tenet-check-2026-09-19.md](/reviews/tenet-check-2026-09-19/) = 136)
**Files checked**: 834 live articles — `topics/` 329, `concepts/` 327, `voids/` 104, `apex/` 45, `positions/` 23, `arguments/` 6
**Errors**: 3
**Warnings**: 12
**Notes**: 9
**Tenets swept**: 1, 2, 3, 4 (Tenet 5 deliberately not re-swept — see §Tenet 5)

## Summary

Check 137 is the first run in seven to spend its effort on **Tenets 1–4**. Two results dominate.

**First, the two Tenet-5 loci carried forward from check 136 are already repaired**, and the carry was a
false positive produced by measuring a bare string. Details in §Tenet 5. No Tenet-5 work was done beyond
verifying that.

**Second, the four Tenets 1–4 sweeps independently converged on the same structural locus: the mandated
`## Relation to Site Perspective` section.** Not one of the three ERRORs and barely any of the fifteen
lesser findings sits in an article's *argument*. They sit in the tenet-alignment paragraphs, and in most
cases the article's own body already states the calibrated version. The body does the careful work; the
mandated tenet paragraph then restates it one notch too strongly. This is the corpus's leak point.

Crucially — and this is the operational difference from the Tenet-5 tiebreaker family — **the governing
doctrine already exists**. `tenets.md` §Hidden-inheritance failures names this exact pattern
(*"Alignment-line inheritance: an article fills a tenet-alignment subsection with argumentative work simply
because the tenet appears in its alignment line"*) and states the remedy (*"a subsection covering a
not-invoked cell should mark itself as coherence commentary"*). Fixing sentences here will **not**
regenerate them, because the rule they violate is already written down. That is why this family is safe to
work through and the Tenet-5 family was not.

Tenets 1–4 did **not** come back clean, but they came back **sound at the core**. Two results are worth
stating as findings in their own right: **no ERROR-grade Tenet-1 violation exists anywhere in 834 files** —
nothing asserts in Map voice that consciousness is reducible to the physical or that phenomenal
consciousness is an illusion — and **Tenet 4's core is clean**, with no article endorsing MWI in its own
voice. The flagship clusters are well calibrated and several are exemplary. What fails is peripheral,
implicit, and bounded.

## Tenet 5 — not re-swept, and the two carried loci are already fixed

Per the driver brief, the booked `NEEDS-HUMAN (doctrine) 2026-09-19` tiebreaker family at `todo.md:55` was
**not** re-listed, not re-measured, and nothing was minted against it. I confirm that.

The brief carried two loci forward as "STILL LIVE (1)". Both strings are indeed still present — and both
have **already been repaired**:

| locus | string still present | guard now present | repair commit |
|---|---|---|---|
| `concepts/bidirectional-interaction` L119 | yes (1) | yes | `57c01f4290`, 2026-09-19 17:39:33 +0000 |
| `concepts/consciousness-as-amplifier` L183 | yes (1) | yes | `ccaf13d9ae`, 2026-09-19 21:55:37 +0000 |

Both commits are ancestors of HEAD. The repair was **additive**: the guard clause
`—though by the Map's own [Tenet 5](/tenets/#occams-limits), simplicity is not decisive where knowledge is
incomplete, so this counts as a registered advantage rather than a parsimony proof` was appended to the
same sentence rather than the sentence being rewritten. So the offending substring survives verbatim while
the defect does not.

**Method lesson worth booking:** a bare-string probe cannot detect an additive repair. The check-136
carry-forward measured `grep -oiF "<offending phrase>"` and correctly got 1, but the correct question was
whether a guard sits within the same sentence. Both loci were, by check 136's own description, the report's
two highest-value edits; both were fixed within nine hours of that report; and check 137 was briefed to
re-flag them. Carry-forward items need a **repair-shaped** probe, not a **defect-shaped** one.

Net effect: this freed both reserved priority slots for Tenets 1–4, which is what the brief asked for.

## Errors

### [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/)
Two independent defects, surfaced by two separate sweeps that did not share context.

- **Tenet violated**: 2 (Minimal Quantum Interaction) — and separately 4 (No Many Worlds)
- **Quote (Tenet 2)**: "MRI signatures of entanglement correlating with consciousness and microtubule-stabilising drugs delaying anaesthesia—now lending initial support"
- **Issue**: asserted flatly in the Map's own voice, this claims a currently-measured, brain-scale quantum-entanglement signature tracking consciousness — the near-term detectable signature Tenet 2 forbids. The file contains **zero** occurrences of `unreplicated`, `contested`, `replicat`, `Kerskens` or `single laboratory` (positive control: `entanglement` = 9), so nothing walks it back. The Map's own `concepts/entanglement-binding-hypothesis` says the same MRI line "rests on a single laboratory's unreplicated protocol". **24 live articles cite Kerskens by name; this one does not cite him at all yet asserts his result as support** — it carries the claim without the attribution that would let a reader trace its standing.
- **Quote (Tenet 4)**: "The [No Many Worlds tenet](/tenets/#no-many-worlds) holds that first-person unity claims require genuine collapse. If all branches are equally real, unity reports become either false or contentless."
- **Issue**: the tenet holds no such thing. The `## No Many Worlds` section of `tenets.md` contains **0** occurrences of `unity` or `unified` (positive control: `collapse` = 7 within that section). This is fabricated tenet content, unique to this file corpus-wide. It also contradicts the matrix's own concession that decoherence "does predict definite qualia within each branch" — a branch-local unity report is neither false nor contentless.
- **Recommendation**: hedge the Kerskens line to its sibling's register; replace the Tenet-4 paragraph's fabricated attribution with the indexical objection, which is what actually carries the tenet.

### [topics/presentiment-and-retrocausality.md](/topics/presentiment-and-retrocausality/)
- **Tenet violated**: 2 (Minimal Quantum Interaction)
- **Quote**: "Presentiment would be additional evidence if confirmed"
- **Issue**: this inverts the sign of the Map's own parapsychology firewall. `topics/parapsychology-firewall` states "the Map needs psi to be *small or absent*, not large" and lists "High-bandwidth telepathy or precognition" among the results that sit on the wrong side of the bound. Confirmed presentiment would therefore **disconfirm**, not support. `grep -oiF "parapsychology-firewall"` returns **0** for this file (positive control: `presentiment` = 34) — the article never links the doctrine. The firewall article postdates it, so this is unpropagated doctrine rather than settled disagreement.
- **Recommendation**: invert the sentence and link the firewall.

### [topics/animal-consciousness.md](/topics/animal-consciousness/)
- **Tenet violated**: 1 (via the tenet-dependency matrix)
- **Quote**: "the plausibility tilt rests on the [evolutionary argument for mental causation](/topics/evolutionary-case-for-mental-causation/)" — and the alignment paragraph "**[Bidirectional Interaction](/tenets/#bidirectional-interaction)**: The [evolutionary argument for mental causation](/topics/evolutionary-case-for-mental-causation/) holds that if consciousness evolved, it plausibly has causal effects"
- **Issue**: verified three ways. (i) The tenet-dependency matrix marks the Animal consciousness row's *Interactionist dualism (mental causation)* cell **Not invoked**. (ii) The register's **[P-CS2](/positions/consciousness-scope/#p-cs2)** *Depends on* line excludes it, resting on markers, Tenet 1 and Tenet 5. (iii) `tenets.md` names this exact case in its leakage list — *"an article... on animal consciousness imports interactionist commitments from the agency cluster... a genuine error in that scope."* The article's central plausibility tilt rests on a commitment the matrix says the row does not need and the register does not book. `ai_modified` is 2026-09-19, so the breach is current, not legacy.
- **Recommendation**: re-scope the tilt to the marker-convergence and no-anthropocentric-barrier grounds [P-CS2](/positions/consciousness-scope/#p-cs2) actually rests on; mark the Tenet-3 paragraph as coherence commentary per the matrix's stated remedy.

## Priority list (capped at 4 — everything below the cap is carried, not buried)

The two slots reserved for the check-136 carries are released (both already fixed), so all four go to
Tenets 1–4. One item per tenet, paying host named for each.

| # | Locus | Tenet | Paying host |
|---|---|---|---|
| 1 | [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/) — both quotes above | 2 + 4 | `concepts/unity-of-consciousness` |
| 2 | [concepts/dualism.md](/concepts/dualism/) | 1 | `concepts/dualism` |
| 3 | [topics/presentiment-and-retrocausality.md](/topics/presentiment-and-retrocausality/) | 2 | `topics/presentiment-and-retrocausality` |
| 4 | [concepts/filter-theory.md](/concepts/filter-theory/) | 3 ([P-CS6](/positions/consciousness-scope/#p-cs6)) | `concepts/filter-theory` |

**1. [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/)** — as above. Ranked first because it is the only article found
with two independent tenet defects, one of them fabricated tenet content, and because two sweeps that did
not share context reached it independently.

**2. [concepts/dualism.md](/concepts/dualism/)** — verbatim: `The gap isn't epistemic but conceptual—the kinds of concepts
physical science employs cannot in principle capture subjective character.` Three problems in one sentence,
in the corpus's **flagship Tenet-1 article**. (i) It reports the dispute as won, against `tenets.md`'s own
*"it does not report that dispute as won."* (ii) It breaks a rule the Map states explicitly in
`concepts/neural-correlates-of-consciousness`: *`"may never" is not "cannot in principle,"`*. (iii) It
attributes to Levine the opposite of what `concepts/explanatory-gap` says he held — *"Levine's original
formulation was carefully modest: the gap is epistemic"* — so this is a citation-fidelity defect as well as
a calibration one. All 18 corpus instances of `cannot in principle` were triaged; the other 17 are
conditionals, Tenet-5 material, or the Map correctly refusing the move. This one is the exception.

**3. [topics/presentiment-and-retrocausality.md](/topics/presentiment-and-retrocausality/)** — as above. Cheap to fix, and it currently has the Map
publicly welcoming a result its own firewall says would falsify the framework.

**4. [concepts/filter-theory.md](/concepts/filter-theory/)** — verbatim: `If consciousness uses the brain as interface, it can affect
brain states just as brain states affect conscious experience`. This derives Tenet 3's outbound leg by
entailment from the filter premise, which today's new **[P-CS6](/positions/consciousness-scope/#p-cs6)** expressly forbids: *"transmission-over-production
evidence bears on Tenet 1 and nothing else... Tenet 3's outbound leg is therefore owed a separate argument
rather than carried over."* The next clause, `consciousness selects among neural possibilities`, asserts
the selection thesis unhedged. **The sharp part**: [P-CS6](/positions/consciousness-scope/#p-cs6)'s own *Argued in* list names `concepts/filter-theory`
as a place the partition is argued. The register cites this article as authority for a partition the
article breaches. The adjacent Tenet-2 paragraph in the same section carries a caveat this one lacks.

**Top carried item, named so it is not lost**: [topics/animal-consciousness.md](/topics/animal-consciousness/) (ERROR, above) is the
strongest finding *below* the cap. It was displaced only because the four above span all four tenets and
two are ERROR-grade in the Map's own voice. If a fifth slot exists, it takes it.

## Warnings

**Tenet 1 — implicit drift (no ERROR-grade violation exists anywhere in the corpus).** Nothing in 834 files
asserts in Map voice that consciousness is reducible or identical to the physical, or that phenomenal
consciousness is an illusion. All four Tenet-1 findings are implicit:

- [concepts/dualism.md](/concepts/dualism/) — see priority 2 above.
- [topics/consciousness-as-activity.md](/topics/consciousness-as-activity/) — "conscious activity supervenes on neural processes". Psychophysical supervenience is the defining thesis of **non-reductive physicalism**; it makes the mental a function of the neural, the shape the Map disavows by name elsewhere (`concepts/is-conscious-being-a-natural-kind`: *"The Map's dualism is not of that shape."*; `topics/many-minds-interpretation` cites *"mental states do not supervene on brain states"* as a point in the Map's favour). The article's alignment section denies only *identity*, never supervenience. `supervene` occurs twice — this sentence and its own licensing analogy, which is an intra-physical case, and that is what makes the sentence read as physical-but-higher-level.
- [concepts/libet-experiments.md](/concepts/libet-experiments/) — "The parietal cortex produces the experience of intending; the premotor cortex produces movement." Flat Map-voice **production** claim about a phenomenal state, with none of the filter/production distinction the Map insists on (`filter` = 0 in the file; positive controls `parietal` 7, `produc` 4). A corpus sweep for "brain-structure produces phenomenal-noun" returned 13 hits and **this is the only one in flat Map voice**. The sibling `concepts/phenomenology-of-choice-and-volition` handles the identical Desmurget data in the disciplined form, so this is drift, not house style. Survived a deep review on 2026-07-12. **Note the inversion**: here the alignment section is disciplined and the *body* carries the stronger claim — the mirror of the pattern in §The systemic finding.
- [topics/the-binding-problem.md](/topics/the-binding-problem/) — "cortical processing generates phenomenal content without corresponding sensory data". Unattributed, unhedged Map voice asserting cortical processing *generates* phenomenal content. The alignment section rebuts only production of *unity*, not of phenomenal *content*; `filter` = 0 (positive control `binding` = 67).

**Tenets 2–4 — alignment-section drift:**

- [concepts/unity-of-consciousness.md](/concepts/unity-of-consciousness/) (Tenet 4 limb) — the fabricated tenet attribution described under Errors.
- [topics/terminal-lucidity-and-filter-transmission-theory.md](/topics/terminal-lucidity-and-filter-transmission-theory/) — "a brief window of enhanced downward causation before the interface fails completely". [P-CS6](/positions/consciousness-scope/#p-cs6) partition breach: filter-loosening evidence, the paradigm inbound datum, converted straight into an outbound claim. The article's own §The Evidential Trajectory concedes the 2025 data are "consistent with neurochemical mechanisms rather than vindicating the filter reading". `topics/consciousness-and-neurodegenerative-disease` already handles the identical inference correctly — the calibrated version exists in-corpus. (Article predates [P-CS6](/positions/consciousness-scope/#p-cs6) by ~3 weeks.)
- [topics/volitional-control.md](/topics/volitional-control/) — "The Map interprets this as a site where consciousness modulates quantum-indeterminate processes". Attaches the quantum reading to Schwartz's PET-measurable caudate changes. Contradicted by the article's own body, which says classical Hebbian re-weighting "fully accounts for these changes, and the Map does not claim otherwise here".
- [arguments/materialism-argument.md](/arguments/materialism-argument/) — "converge on the claim that materialism *cannot in principle* explain consciousness, rather than that it merely *hasn't yet*". Tenet 1's own rationale says the opposite about its own standing: *"Tenet 1 records where the Map plants itself in an unsettled dispute; it does not report that dispute as won."* The section's closing hedge disclaims *proving dualism* but leaves the in-principle modal claim standing. Found only because `arguments/` was swept — see §Coverage gap.
- [concepts/conscious-vs-unconscious-processing.md](/concepts/conscious-vs-unconscious-processing/) — "These findings directly support the" (…Bidirectional Interaction tenet). A 2025 fMRI reanalysis about the weakness of *unconscious* processing presented as *directly* supporting Tenet 3, which is held at available-not-actual standing.
- [concepts/mind-brain-separation.md](/concepts/mind-brain-separation/) — "The division of faculties supports both." "Both" is Tenets 1 and 3; a transmission-side argument is booked as supporting the outbound leg.
- [voids/conceptual-impossibility.md](/voids/conceptual-impossibility/) — "not merely absent from our branch". The Tenet-4 paragraph reasons wholly inside an Everettian multiverse as operative background and never indicates the Map rejects MWI.

## Notes

- [topics/death-and-consciousness.md](/topics/death-and-consciousness/) — "Shared death experiences suggest consciousness-to-consciousness interaction may occur outside normal sensory channels when the filtering apparatus is compromised". Doubly off-target for Tenet 3: consciousness-to-consciousness traffic is not consciousness changing the brain's physical state.
- [topics/william-james-consciousness.md](/topics/william-james-consciousness/) — "treating the felt effort of sustained attention as genuine causal engagement rather than as epiphenomenal report". Tenet-3 overclaim; the opening hedge governs James's reading, not the Map's further step.
- [topics/brain-computer-interfaces-and-the-interface-boundary.md](/topics/brain-computer-interfaces-and-the-interface-boundary/) — "BCI evidence supports the minimality constraint". Self-corrects two sentences later; the flat opening claim remains.
- [topics/phenomenology-of-musical-understanding.md](/topics/phenomenology-of-musical-understanding/) — "dissipates into a proliferation of equally-real variants". Rejects MWI on the ontological-multiplicity ground the tenet books as **subsidiary**, after conceding the indexical point.
- [voids/expertise-and-its-occlusion.md](/voids/expertise-and-its-occlusion/) — "The phenomenology of the expertise void resists this framing." Grounds the rejection on phenomenology discriminating between ontologies, which the branch-relative concession forbids.
- [topics/the-reverse-inference.md](/topics/the-reverse-inference/) — "is *derived* by the reverse inference rather than merely assumed". `tenets.md` books global exclusion as a posit "asserted rather than derived from sourcehood".
- [voids/origin-of-consciousness.md](/voids/origin-of-consciousness/) — "keeps focus on singular existence rather than endless multiplication". Opens on indexical grounds, closes by re-grounding on proliferation.
- [concepts/neurophenomenology-and-contemplative-neuroscience.md](/concepts/neurophenomenology-and-contemplative-neuroscience/) — "contemplatives report a singular perspective, not branching identity". Directly contradicted by sibling [apex/contemplative-path.md](/apex/contemplative-path/).
- `tenets.md` itself — the matrix cites `[[apex/machine-question]] §senses of conscious AI`, but that section does not exist: `grep -oiF "senses of conscious"` returns **0** in [apex/machine-question.md](/apex/machine-question/) (positive control: file is 49,888 bytes and a known heading returns 1). The phrase lives in `concepts/consciousness-as-amplifier`. The row governing the corpus's sparsest inheritance profile points at nothing, so an author cannot locate the scope it governs.

## The systemic finding: the alignment section and the body are not held to the same standard

Four independent sweeps, plus one pre-existing queued review finding, converge:

- Tenet 2 sweep: 3 of 4 findings sit in a `Relation to Site Perspective` section and are contradicted by their own article's body.
- Tenet 3 sweep: 5 of 6 findings sit in one.
- Tenet 4 sweep: **all** findings sit in one — "peripheral articles whose *entire* MWI treatment is the single flagged paragraph".
- My own two findings (`animal-consciousness`, `materialism-argument`) sit in one.
- Independent corroboration, already queued: the open P3 on `topics/consciousness-and-neurodegenerative-disease` (from [reviews/optimistic-2026-09-16-clinical-evidence-wing.md](/reviews/optimistic-2026-09-16-clinical-evidence-wing/)) reports exactly this shape — tenet section claims "supports" where the body says "an interpretation, not a straightforward observation" — and includes a Tenet-4 misattribution structurally identical to the `unity-of-consciousness` one.

**The honest qualifier — it runs both ways.** The Tenet-1 sweep found the *inverse* in two of its four
findings: in `concepts/libet-experiments` and `topics/the-binding-problem` the alignment section is
disciplined and the **body** carries the stronger claim. So the correct statement is not "alignment
sections overclaim" but "**the alignment section and the body are not held to the same standard, and
whichever one a given lens is not reading is where the drift sits.**" That is a stronger and more useful
finding than the one-directional version, and it means a fix pass must compare the two rather than
patching the section.

**Mechanism.** The writing-style guide mandates the section for every article: 807 of 811 live articles carry
one (786 as `Relation to Site Perspective`, 23 as the `Relation to the Map's Perspective` variant — note that
a heading-keyed audit false-zeroes on the variant). Every article must therefore produce tenet paragraphs
whether or not its argument touches those tenets. The matrix predicted precisely this and already supplies
the remedy.

**Bounding it honestly.** A lexical probe over alignment sections only — strong support verb present, no
hedge token anywhere — returns **29 of 785 (3%)**. Report that as a **candidate pool, not a defect count**:
it is a lexical metric, it runs false-high in this corpus, and it did **not** catch any of my four priority
items (all of which contain hedge tokens elsewhere in the section). Its real value is the upper bound: this
is a bounded, tractable family in the tens, not a corpus-wide rot. It needs a **structural** lens —
"does the alignment paragraph claim more than this article's own body?" — not a word list.

**Recommended next lens, not minted here**: one pass per article comparing each tenet paragraph against the
body it summarises. It is the highest-yield lens available and it has explicit doctrine behind it.

## Coverage gap in this skill

`SKILL.md` §2 scans only `obsidian/topics/`, `obsidian/concepts/` and `obsidian/positions/`. That omits
`obsidian/arguments/` — six files that are the corpus's **dedicated tenet-defence articles**
(`materialism-argument` → Tenet 1, `epiphenomenalism-argument` → Tenet 3, `many-worlds-argument` → Tenet 4,
`functionalism-argument`, `epistemological-limits-of-occams-razor` → Tenet 5). They are the most
tenet-load-bearing files on the site and no tenet check has ever scanned them. It also omits `apex/` (45)
and `voids/` (104), which between them supplied four findings above. This check swept all of them: 834 files
rather than the scoped 679. Recommend widening the skill's scan list.

## What came back clean (reported as findings, since they are)

- **Tenet 4 core: clean.** No article in any section endorses MWI in its own voice, treats branches as equally real as the Map's ontology, or calls the indexical question meaningless. Every "all branches are equally real" hit checked is rival-definition. The flagship cluster (`apex/one-world-wager`, `concepts/many-worlds`, `topics/probability-problem-in-many-worlds`, `topics/indexical-identity-quantum-measurement`, `concepts/indexical-knowledge-and-identity`, `topics/vertiginous-question`, `positions/individuation-and-subjecthood`) all carry the branch-egalitarian / List-2023 narrowing.
- **Tenet 1 reduction/illusion endorsement: clean on every probe run.** The Map-voice endorsement vocabulary is abundant in the corpus but expository throughout. The three rarest and therefore riskiest forms were read in full: `consciousness is nothing but` (1 file — `concepts/argument-from-mechanism`, quoted as a *tempting* inference the article then says the pharmacology "licenses neither" of); `is reducible to physical` (1 file — `concepts/objectivity-and-consciousness`, inside "denying that consciousness is reducible to physical facts. This is dualism, not idealism"); `materialism is true` (3 files — one Schwitzgebel 2015 title in a reference list, one Kammerer 2022 concession under discussion, one antecedent of a self-stultification conditional). The high-frequency forms (`consciousness is an illusion` 27 files, `consciousness is identical to` 22, `consciousness reduces to` 22) are rival-statement inventory. The dedicated sweep confirms this independently across six lexical passes (225 + 47 + 13 + 10 hits hand-triaged, plus a lead-paragraph pass over all files and an alignment-section pass), and reports **every** rival-theory article — illusionism, IIT, GNW, AST, functionalism, type-identity, predictive processing, eliminative materialism — as carrying a scoping section. `concepts/` returned clean independently; `apex/`, `voids/` and `positions/` are clean. The four Tenet-1 findings above are all implicit drift.
- **Tenet 3 epiphenomenalist drift: clean.** All 21 live-tree occurrences of "along for the ride" (21 files, re-measured across `topics/ concepts/ apex/ voids/ positions/ arguments/`) are opponent exposition, tenet statement, or answered challenge. No article's own voice accepts causal closure or leaves the conclusion standing.
- **Tenet 2 core cluster: hardened.** Every psychokinesis / parapsychology / energy-injection hit across `parapsychology-firewall`, `brain-specialness-boundary`, `conservation-laws-and-mental-causation`, `selection-only-mind-influence`, `born-preserving-causal-efficacy`, `coupling-modes`, `amplification-*` is exposition-to-reject or correctly-scoped disclaimer.
- **Substance-leaning leakage: zero.** Every matrix row marked *Not invoked* for the substance-leaning column (`brain-internal-born-rule-testing`, `born-rule-and-the-consciousness-interface`, `quantum-biology-and-neural-consciousness`, `machine-consciousness`, `apex/machine-question`, `animal-consciousness`) returns **0** for `agent causation`, `agent-causal`, `persisting subject`, `substance dualism`, `substance dualist` — with `consciousness` counts of 30–163 as positive controls.
- **Conceivability cluster: correctly scoped.** `concepts/philosophical-zombies` states the discipline explicitly — "The zombie argument works under minimal dualism—Tenet 1 alone—so interactionism is downstream of it" — and its Interactionist Escape section self-corrects an earlier Tenet-3 gesture in the same article.
- **`arguments/` section: well calibrated on Tenets 1–4** apart from the one `materialism-argument` overclaim above. `many-worlds-argument` cites [P-I5](/positions/individuation-and-subjecthood/#p-i5) and the branch-egalitarian narrowing; `epiphenomenalism-argument` concedes the phenomenal-concept escape survives; `materialism-argument` cites [P-D2](/positions/arguments-for-dualism/#p-d2)/[P-MC1](/positions/arguments-for-mental-causation/#p-mc1).
- **Positions register: clean on Tenets 1–4.** [P-I5](/positions/individuation-and-subjecthood/#p-i5) handles variant-relative reach and explicitly books why the extravagance objection cannot substitute.
- **[P-CS6](/positions/consciousness-scope/#p-cs6) compliance already widespread.** `concepts/filter-vs-interface-distinction`, `topics/psychedelics-and-the-filter-model`, `concepts/altered-states-of-consciousness`, `apex/pharmacological-dissociation-as-evidence`, `concepts/near-death-experiences`, `topics/locked-in-syndrome-...`, `concepts/mind-matter-interface`, `concepts/default-mode-network` all partition correctly, several citing `^tenet-3-standing` directly. The partition is a day old and most of its cluster already honours it.

## Method

- All counts by `grep -oiF "<literal>" <path> | wc -l`; never `grep -c`, which counts lines, and these articles are long single-line paragraphs. Never piped through `head`/`cut`.
- Every absence claim is backed by a positive control in the same file. Two confirming zero-greps were treated as grounds for more suspicion, not less.
- Every finding returned by a sub-sweep was re-verified independently by me before it entered this report. One returned string (`unity-of-consciousness`, Tenet 4) false-zeroed on first probe: it was a wikilink-markup-stripped paraphrase. The underlying text was located and the claim held. That is the expected splitter, not a fork error — but it is why fork strings get re-greppped rather than pasted.
- The `arguments/` heading variant (`Relation to the Map's Perspective`) initially read as a missing tenet-alignment section in `epiphenomenalism-argument`; checked before reporting, and it is not a defect.
- **Substring trap caught in flight**: a `reducible to physical` probe silently matches `irreducible to physical` — the Map's own position — and manufactured 7 false positives in the Tenet-1 sweep before it was caught. Any absence-or-presence test on a phrase the Map's own doctrine *prefixes* is unsound by construction. Recorded because this is the second distinct measurement artefact this check turned up, the first being the additive-repair blindness in §Tenet 5.
- Nothing in this report rests on a fork's unverified assertion. Where a returned string and the file disagreed, the file won.

## Scope confirmation

- **No article was edited.** This check is reports-only. The only file written is this report, plus the changelog entry.
- **Nothing was committed** — `cycle_post` handles that.
- **No task was minted.** The four priority items are all on articles I reviewed, so minting would have been in contract, but each was first grepped against the open-task blocks in `todo.md` (splitting on `### ` and skipping `✓` headers) and none has an open task pileup risk worth pre-empting the operator's read of this report. The priority table above is the actionable list.
- **The booked Tenet-5 tiebreaker family at `todo.md:55` was not re-listed, not re-measured, and nothing was minted against it.**