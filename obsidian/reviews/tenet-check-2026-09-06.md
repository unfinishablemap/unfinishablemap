---
title: "Tenet Alignment Check - 2026-09-06"
description: "Sixteenth consecutive zero-error pass. The alignment subsection blind spot is now measured, not estimated — and the tenets page's own designated materialism article states as result what the tenets page states as judgement."
created: 2026-09-06
modified: 2026-09-06
human_modified:
ai_modified: 2026-09-06T09:35:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[tenets]]"
  - "[[concepts/materialism]]"
  - "[[concepts/many-worlds]]"
  - "[[concepts/epiphenomenalism]]"
  - "[[concepts/agency-budget]]"
  - "[[concepts/observational-closure]]"
  - "[[concepts/quantum-interpretations]]"
  - "[[concepts/filter-theory]]"
  - "[[topics/personal-identity]]"
  - "[[topics/arguments-against-materialism]]"
  - "[[voids/voids]]"
  - "[[arguments/many-worlds-argument]]"
  - "[[positions/voids-as-evidence]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-06
last_curated:
last_deep_review:
---

# Tenet Alignment Check

**Date**: 2026-09-06 (09:35Z)
**Scope**: All five tenets. Full read of `tenets/tenets.md` plus its window diff. Window measured from git (base `d063b0f7dc`, the 09-04 check commit, 2026-09-04T12:40:38Z — ~45h, 152 commits; 95 changed files across `topics/`, `concepts/`, `positions/`, `apex/`, `voids/`, `tenets/`). Every window file read in full in six parallel batches, each with its per-file diff against the base, its `description:`/`apex_thesis:` fields, and its `## Relation to Site Perspective` section. **Every flagged locus independently re-verified by the driver with fixed-string matching** (66 checks; **zero** false positives from the batch reviewers). Direct-contradiction battery across the live tree (826), `archive/` (524) and `hugo/content/` (9473). Status check on all seven predecessor warnings and all five predecessor notes.
**Predecessor**: `reviews/tenet-check-2026-09-04.md`.
**Files checked**: 95 (window, full read) + battery and three corpus-wide lenses across three trees
**Errors**: 0 (direct-contradiction battery); 3 Rules-out contradictions reported as Warnings 1, 4 and 6
**Warnings**: 9 (families; ~165 loci, 77 individually verified)
**Notes**: 6 (families)

## Summary

**Zero direct tenet contradictions — the sixteenth consecutive pass returning zero.** Batteries for asserted-epiphenomenalism, consciousness-as-illusion, Map-voice reducibility, energy-injection, MWI-endorsement, parsimony-refutes-dualism and just-neurons returned no Map-voice hits across all three trees. Every hit resolves to rival-description, a clearly-marked conditional, or review/workflow echo.

**Predecessor Warning 3 is closed, and closed well.** `tenets.md` L107 now reads "under any *unconditioned aggregate* test current or foreseeable instruments could run, though a deviation *conditioned* on intention, task or subject remains live ([[positions/quantum-interface#^mechanism-debt|P-Q3]])", and the deleted "and so leaves no statistical trace" clause is gone. L75, L81 and L107 agree for the first time in this series. **Predecessor Warning 7 is closed outright** — all five loci verified gone, including `topics/born-rule-and-the-consciousness-interface` L205/L207, where the fix was the substantive Lakatos-passage rewrite the task asked for rather than a parenthesis patch ("'unfalsifiable' overstates the insulation"). The canonical page settling is what made the rest of this run legible.

**The highest-leverage single finding is the article `tenets.md` points at.** L59 designates `concepts/materialism` as the place for "detailed engagement with the materialist position and its failures". That article's L98 says the anti-materialist arguments "converge on the same conclusion from independent directions"; its L176 says dualism "is accepted because materialism fails" and "Consciousness must be something beyond the physical." `tenets.md` L55 says the opposite in terms — the failure is "a judgement the Map owns, not a result it reports", and the arguments form "a cumulative case … **not a set of independent proofs converging on a settled conclusion**". The article carries no calibration hedge on the failure claim anywhere, so every reader or crawler following the tenets page's own pointer lands on the uncalibrated version. (Warning 1)

**The predecessor's structural finding is now measured rather than estimated, and it holds.** The 09-04 report said "768 articles carry such a section and no lens currently reads them against their own bodies". That lens now exists (Method note): **757 live articles carry the section**, and ranking each one's assertoric register against its own body's, then reading the top eight, found four real defects and three exemplary false positives — usable, but never trustworthy unread. The window batches converged on it independently: **VOIDS-E reports that every one of its twelve findings lives in the alignment section, and that not one body paragraph in its eighteen files carries an inflation the alignment section does not** — with four files (`voids.md`, `disappearance-voids`, `capability-division-problem`, `tenet-generated-voids`) having had their *body* calibrated in this very window while the alignment section kept the retired form. (Warning 2)

**A repair that made its defect more precise instead of removing it.** The Warning-7 task, marked ✓ 2026-09-04, rewrote `concepts/agency-budget` L78 from "can never be witnessed from outside" to "no publicly conditioned test can witness it". The task's instruction was to propagate the file's own L84 scoping upward — but L84 flags that answer as *quietly requiring* conscious states to be publicly unresolvable in principle, i.e. as a dependency, and L78 now presents it as a proof ("as the dependency below makes explicit"). Worse, the file's L33 defines its conservation law over "every context X that an outside tester can publicly condition on", and *task* and *subject* are exactly such contexts — so the new wording forecloses by name the route `tenets.md` L75/L107 was repaired to keep open. The old wording was vague; the new one is precise about the wrong thing. (Warning 4)

**A quotation attributed to the tenets page that the tenets page does not contain.** `topics/personal-identity` L84 has the No-Many-Worlds tenet rejecting MWI "partly because it creates \"unanswerable indexical questions: why am I *this* instance and not another?\"" — in quotation marks. `grep -c unanswerable obsidian/tenets/tenets.md` returns **0**. The string is not in the tenet in any form, and the sentiment is the pre-L117 unscoped version. Two known ancestors of this exact stale-internal-quote were fixed in W31/W32 (`archive/voids/indexical-void` L113, `topics/vertiginous-question` L188); this live locus was missed by that sweep. (Warning 6)

**The L107 repair stranded its own siblings, and one of them is the register entry the register inherits from.** The retired string "aggregate-statistics test" is still live at `positions/methodology-and-calibration` L109 (P-M4, which downstream articles inherit their framework-stage register from), at `apex/research-programme-decisions-under-the-map` L47 (an `apex_thesis` about which experiments are worth running), and in unscoped paraphrase at `apex/self-concealing-interface` L87 — whose own L77 *was* rescoped this window. This is the cheapest fix in the report and the only family with a hard completion test. **I found the third locus only after correcting my own error**: my first status check for that string was scoped to `tenets.md` alone and returned a false "repaired". (Warning 9)

**Queue discipline: the two warnings that were minted were both executed within 48h; the five that were not minted are all untouched.** Warnings 3 and 7 became tasks and both closed. Warnings 1, 2, 4, 5 and 6 produced no task, and driver re-verification found **every spot-checked locus still live** (11 of 11 for the alignment-subsection family, 7 of 7 for the improper-mixture family, 10 of 11 for the Tenet 5 family). The Tenet 5 self-binding family has now gone **four consecutive checks** without a task. And the Tenet 4 append has now **failed three consecutive times**: the task at `todo.md` L2049 is twelve lines long, still carries only its original fourteen 08-26 loci, and names not one of the ~20 loci the 09-02 and 09-04 reports asked to be appended. (Note 5)

## On the error count

The batch reviewers graded several findings ERROR; I have held **Errors: 0** so the headline stays comparable with the fifteen before it. The skill's ERROR bar is a *direct contradiction of a tenet in the Map's own voice*, and nothing meets it. Four findings do contradict a tenet's explicit **Rules-out clause** rather than merely drifting from its register, which is sharper than the Warning label suggests, and are flagged inline: Warnings 1, 3, 4 and 6.

## Errors

None. No article in any tree endorses eliminative materialism, consciousness-as-illusion, quantum mysticism, many-worlds, or parsimony-against-dualism in the Map's own voice.

## Warnings

### Warning 1 — `concepts/materialism`: the tenets page's designated target states as result what the tenets page states as judgement

**Tenets**: 1, 5. **Rules-out contradiction.** Highest leverage in the report.

| Locus | Text | Conflicts with |
|---|---|---|
| `concepts/materialism` **L98** | "together they form … positive arguments for dualism that **converge on the same conclusion from independent directions**"; "Precisely where materialism fails, dualism … **gains support**" | `tenets.md` L55: "a cumulative case for irreducibility that each opponent disputes at a different point, **not a set of independent proofs converging on a settled conclusion**" |
| `concepts/materialism` **L176** | "**[[dualism]]** is accepted **because materialism fails**"; "Consciousness **must be** something beyond the physical" | `tenets.md` L55: materialism's failure is "a judgement the Map owns, **not a result it reports**"; the dispute with illusionism "runs to bedrock" |
| `topics/arguments-against-materialism` **L137** | "The Unfinishable Map's [[tenets]] are **built on the failure of materialism**"; "a conclusion supported by the **convergence of independent arguments**"; the Tenet 3 clause "**insists that consciousness does real causal work**" | same L55; and `tenets.md` L95 for the Tenet 3 clause |
| `topics/arguments-against-materialism` **L139** | "They **establish** something more fundamental: the materialist consensus rests on a failure to take consciousness seriously" | `tenets.md` L95 puts "establishes" in the discharge register |
| `concepts/supervenience` **L67** | "Several **independent** arguments **establish** this." | same L55 |

The non-independence discipline exists and is good where it landed — `apex/one-world-wager` L62 ("The honest count is therefore three independent arguments, not four or five"), `topics/aesthetics-and-consciousness` L82 ("The five are not five independent arguments"), `concepts/interactionist-dualism` L97 ("Seven arguments … though not as seven independent lines"). It reached the hubs and the audits and **not the cross-reference blurbs that describe them**: `topics/argument-from-reason` L169, `topics/the-strong-emergence-of-consciousness` L191, `topics/consciousness-defeats-explanation` L179 and `concepts/grain-mismatch` L93 all still advertise "Multiple independent arguments converging". `concepts/dualism` itself carries only a "cumulative case" register at L190, not the explicit concession, so the blurbs are describing a page that has not been calibrated either.

**Recommendation**: fix `concepts/materialism` first and alone. It is the tenets page's own designated target, it has no hedge to build on, and both loci are single-clause. `tenets.md` L55's own wording is the transplant. Note that this article is *not* the same target as the open `arguments/materialism-argument` work — check for pileup before minting.

### Warning 2 — the alignment subsection carries what the body withdrew: confirmed, measured, and unminted

**Tenets**: 1, 2, 3, 4, 5. The predecessor's Warning 1, carried in full. **No task was minted**, and I re-verified eleven of its sixteen loci by fixed string — **all eleven still live**, in `topics/bandwidth-of-consciousness`, `topics/consciousness-and-skill-acquisition`, `topics/structure-of-attention`, `topics/consciousness-and-memory`, `concepts/stapp-quantum-mind`, `concepts/mental-causation-and-downward-causation`, `concepts/neuroplasticity`, `concepts/degrees-of-consciousness`, `concepts/epiphenomenalism`, `concepts/witness-consciousness`, `concepts/motor-selection`. The strings are tabulated in the predecessor and not repeated here.

New this window, verified, all with the same shape — the alignment section asserting what the same file's body concedes:

| File | Alignment locus | Body locus that withdraws it |
|---|---|---|
| `concepts/quantum-interpretations` | **L185** "MWI cannot explain why *this* branch is mine"; "meaningless on MWI" | L137 "That is not a defeater of MWI … the indexical argument … has been relocated, not answered" |
| `concepts/filter-theory` | **L184** "a selection empirically indistinguishable from random collapse" | L144 was repaired to "under unconditioned aggregate tests"; the alignment section was not |
| `topics/predictive-processing-and-dualism` | **L154** "a singular perspective branching universes cannot ground" | L88 "Neither side refutes the other from inside its own commitments" |
| `topics/the-binding-problem` | **L202** "reveals that phenomenal unity is irreducible to physical coordination"; **L210** "the gap is principled, not a matter of insufficient progress" | L164 "The pattern does not, on its own, discriminate between them" |
| `topics/pain-consciousness-and-causal-power` | **L170** "Pain is the Map's clearest case of consciousness influencing the physical world" | L138/L142/L148 hedge every step ("*suggests* … *may* … though the physicalist may reply") |
| `topics/ethics-under-dualism` | **L197** "the illusionist challenge fails because phenomenal consciousness … grounds value" | L178 "a framework-boundary one, honestly noted, not a refutation either way" |
| `topics/consciousness-and-the-phenomenology-of-place` | **L104/L106** "find significant support"; "gains evidence from" | L88 "Whether that present explanatory gap reflects a permanent metaphysical one is a further claim" |
| `concepts/von-neumann-wigner-interpretation` | **L112** "Stapp's quantum Zeno mechanism that specifies *how* consciousness acts" | L94 "a virtue the Map **acknowledges but does not adopt**"; L82's own "Mechanism deficit" |
| `concepts/somatic-interface` | **L103** "challenging the causal closure thesis"; **L115** "Placebo effects demonstrate" | L41 "does not predict different clinical outcomes"; L43 "neutral between the materialist and interface readings" |
| `concepts/epiphenomenalism` | **L163/L164** table rows "Cannot explain consciousness's existence or distribution" / "Cannot account for introspective access" | L98, **repaired this window**: "the self-undermining charge dissolves". The repair sharpened the concession and thereby sharpened the contradiction; L162 of the same table already carries the calibrated form, so the table is internally inconsistent |
| `voids/voids.md` | **L283** "signpost marking where materialist explanation ends" | L122 "a narrow residue, not a strengthening … reads as coherence of the Map's self-image" — 160 lines above it in the same file, on the most-fetched voids URL |
| `voids/disappearance-voids` | **L162** "**Dualism** gains support from all three mechanisms" | L156, **rewritten this window**: "evidence about the Map's habits of inference rather than about the territory" |
| `voids/capability-division-problem` | **L120** "Dualism … faces the more tractable question of how they collaborate" | L56, **rewritten this window**: "Every candidate for pure brain-side processing becomes disputable" |
| `voids/observation-and-measurement-void` | **L156** "exemplifying the causal efficacy of consciousness" | `tenets.md` L93 excludes the introspective route; this void does not thematise mental causation |
| `voids/language-thought-boundary` | **L152/L154/L156** "receives strongest support" / "gains support through qualia's ineffability" / "This deliberate investigation is mental causation in action" | the file's alignment section carries **no** hedge anywhere, unlike `binding-void` L131, `interoceptive-void` L87, `fusion-void` L92, `mapping-mind-space` L106 |
| `arguments/many-worlds-argument` | **L193+** "Many-worlds leaves nothing for consciousness to select"; "The defender's reply … is epiphenomenalism in disguise" | its own L39 lead says the variants "are not refuted on their own terms". The corpus's canonical Tenet 4 article, contradicting itself in the section that summarises it |

**The `apex_thesis:`/`description:` variant of the same shape**, which matters more per locus because those fields seed downstream synthesis rather than merely summarising:

| File | Locus | Body locus that withdraws it |
|---|---|---|
| `apex/consciousness-and-agency` | **L56** (`apex_thesis:`) "selection … **grounding both free will and moral responsibility**"; **L3** (`description:`) "grounding free will"; **L68** (lead) | L82 "What agent causation distinctively delivers is narrower"; L146 "For much of moral practice a compatibilist account plausibly does equivalent work"; L160. **The body was rewritten toward the narrower register this window (152 lines) and the frontmatter and lead were not moved with it** |
| `apex/cross-modal-capability-division` | **L45** (`apex_thesis:`) "The brain-side machinery of perception is **irreducibly** modality-specific" | L80 "the modality-specificity was contingent on the distance senses' separate transducers all along"; L128 "an *exteroceptive* regularity with a revealing inward exception, not a universal law". The `description:` at L3 *does* carry the scope condition, so the frontmatter is split against itself as well as against the body |
| `apex/phenomenology-of-consciousness-doing-work` | **L3**, **L50** — carried, see Carried families below | L155 |

**Recommendation**: this is the family to mint, and it should be minted as a **contract change rather than a sweep** — the predecessor asked for the same repair one ring out and got surfaces; asked one ring further in and got nothing. The contract: any pass that recalibrates a body claim greps its own file's `## Relation to Site Perspective` block before closing. Start with `concepts/epiphenomenalism` L163/L164 (the table is the hub, the calibrated row is already beside the defective ones) and `voids/voids.md` L283 (section landing page, single clause).

### Warning 3 — the Tenet 5 self-binding family: fourth consecutive check, still never minted

**Tenet**: 5. **Rules-out contradiction** — L147 uniquely names the internal case: "any Map argument that leans on parsimony as if this tenet did not apply to it."

Carried and re-verified live: `concepts/psychophysical-laws` L243 and `topics/psychophysical-laws-bridging-mind-and-matter` L210 (both "justifies the ontological expansion", string-identical across the concept/topic pair, so one wording decision fixes both); `topics/terminal-lucidity-and-filter-transmission-theory` L177 ("the more economical explanation"); `topics/consciousness-under-extreme-metabolic-constraint` L135 ("**explanatorily more economical**", inside its own Occam subsection, which then claims to illustrate the tenet); `concepts/bidirectional-interaction` L119 ("a **simpler** explanation"); `concepts/many-worlds` L158 ("the Map's alternative is **more conservative**", in an article that disarms the same move at L96); `apex/tool-that-cannot-say-its-user` L104 ("predicts all of it **cheaply**", its own Tenet 5 section arguing the converse at L122); `concepts/post-decoherence-selection` L93 ("**more cleanly than any competing framework**", supported by ontological-economy claims about rivals); `topics/the-epiphenomenalist-threat` L176 ("Genuine simplicity must be evaluated after accounting for self-reference" — a corrected metric on which the Map fares better, not a disarming).

`concepts/causal-consistency-constraint` L73 is the instructive one: the window diff rewrote the *end* of that sentence to add the conditioned-deviation caveat, repairing the over-concession, and left "rests on **conservatism (the fifth tenet plus MQI)**" untouched. Tenet 5 supplies no conservatism licence; the legitimate ground is L71's methodological "preference ordering on tenet-fit".

New this run: `voids/amplification-void` L97 — "The simpler hypothesis—that the chain doesn't exist, that consciousness is epiphenomenal or classical—**fails to account for** the evidence the Map marshals for mental causation", inside the Occam subsection, and doubly defective because it also asserts what `tenets.md` L101 withdraws; `voids/binding-void` L135 (Tenet 2's "minimal" read as a count-economy argument, "one unified act rather than billions of independent micro-interactions"); `voids/capability-division-problem` L120; `concepts/quantum-completeness` L110 ("**Parsimony favours** the interpretation that addresses the most questions", two clauses after "The Map's claim is not that dualism is the simplest explanation"); `topics/pain-consciousness-and-causal-power` L160 ("The **simpler** explanation: pain hurts *because* the hurting drives avoidance", disclaimed at L176 of the same file); `topics/ethics-under-dualism` L102 and L205 ("Explanatory economy"); `concepts/galilean-exclusion` L94 ("Genuine parsimony requires accounting for all the phenomena"); `topics/forward-in-time-conscious-selection` L143 ("**Minimality (strong)**" — the outlier in a list whose other four considerations are honestly graded weak/mixed/limited/moderate); `topics/forward-in-time-conscious-selection` L183 ("the more conservative pathway", bare).

⚠️ **Do not sweep this family by string.** I checked eleven further "more parsimonious / more conservative" hits and **all eleven are correctly calibrated**, several exemplary: `topics/graduated-middle-path-valence-modulated-attention` L97 ("the Map may not bank the middle path's minimality"), `concepts/interface-threshold` L124 ("parsimony is a tiebreaker, not a verdict"), `concepts/universal-coupling-response` L93, `topics/parsimony-case-for-interactionist-dualism` L41, `topics/the-steelman-for-process-monism` L87, `voids/epistemological-limits-occams-razor` L64/L96/L104. The string is a hypothesis; the disarming clause is the discriminator.

**Recommendation**: mint. Four checks is enough, and the two `justifies the ontological expansion` loci are one decision.

### Warning 4 — the Warning-7 repair that relocated its defect and made it more precise

**Tenets**: 2, 3. **Rules-out contradiction.** New this window; found by the repair-strength lens, invisible to every string battery because the new wording is on no watchlist.

`concepts/agency-budget` **L78**, rewritten this window under a task marked ✓: "a proof that the interface can be perfectly secure is simultaneously a proof that **no publicly conditioned test can witness it**, as the dependency below makes explicit."

- `tenets.md` L75/L107 reserve as live "a deviation *conditioned* on intention, task or subject" (P-Q3). This file's **L33** defines its conservation law over "every context X that an outside tester can publicly condition on" — and task and subject are such contexts. The new sentence forecloses by name the one route the canonical page was repaired to keep open.
- The task said to propagate **L84**'s scoping upward. But L84 does not license the claim, it *flags* it — "That answer quietly requires conscious states to be publicly unresolvable in principle" — as a dependency to be watched. L78 now cites that dependency as though it discharged the claim.

**Recommendation**: fix before any other Tenet 2 work, and read it as a lesson about the task contract rather than about this file — a repair instruction naming a target locus should also name the *register* the replacement must sit in, or the next repair relocates again. `tenets.md` L107 is the transplant.

### Warning 5 — Tenet 4 scoping: the task exists, and the append has now failed three times

**Tenet**: 4. `tenets.md` L117 confines the indexical objection's decisiveness to branch-egalitarian readings and denies it reaches first-personally centred variants (List 2023); L119 demotes ontological multiplicity to a registered cost; L121 concedes that "the indexical question is meaningful" is itself a posit.

The open task at `todo.md` L2049 is **twelve lines long**, carries only its original fourteen loci from 08-26, and names **none** of the loci the 09-02 and 09-04 reports asked to be appended. Driver-verified by reading the whole task body and grepping it for all twenty-one slugs.

Carried, re-verified live: `concepts/many-worlds` L63 ("something MWI cannot accommodate"), L134, L45 ("MWI raises unanswerable questions about identity") — three contradictions of the same article's own canonical L82, "The objection is therefore not 'MWI cannot accommodate indexical singularity'—it can, branch-locally"; `concepts/conservation-laws-and-mental-causation` L182 (both limbs, with the proliferation limb deployed as a lesser *ground*, which L119 forbids); `concepts/phenomenal-concepts-strategy` L193 ("preserves the zombie intuition in its original force" — `tenets.md` L171 says the opposite in terms, and L163 marks No-MWI "Not invoked" for this cluster).

New this run, verified, in neither task: `apex/machine-question` **L195** ("The [[haecceity]]—thisness—that makes you *this* particular conscious being **requires something beyond physical description**") — all three machine-consciousness matrix rows mark No-MWI **Not invoked** (L159–L161), and the paragraph's own conclusion is correctly deflationary ("Multiple instantiation is thus not an argument against machine consciousness at all"), so the fix is the opening framing sentence, not the substance; the rest of that article handles the three-row split exemplarily; `concepts/quantum-interpretations` L185; `concepts/quantum-completeness` L108 ("many-worlds dissolves the selection question **by denying indexical identity**" — a centred variant builds the privileged present in rather than denying it); `concepts/physical-completeness` L114; `topics/personal-identity` L84 (Warning 6) and L192; `topics/predictive-processing-and-dualism` L154; `topics/consciousness-and-the-phenomenology-of-translation` L159; `voids/phenomenal-quality-void` L132 ("Equal-branch ontology makes all phenomenal stamps equally real" — and its siblings `binding-void` L139 and `mapping-mind-space` L114 both received the branch-relative concession while this file did not); `voids/plurality-void` L87; `voids/resolution-void` L86; `voids/apophatic-cartography` L162; `voids/observation-and-measurement-void` L160; `arguments/many-worlds-argument` L193+.

**Recommendation**: the loci belong **in the task body**, and the append mechanism has now failed three consecutive times, so do not recommend an append again — either rewrite the task with the full ledger in one edit, or split it per-file. `concepts/many-worlds` remains the sharpest: it owns the canonical statement and contradicts it three times in its own text.

### Warning 6 — a quotation of the tenets page that the tenets page does not contain

**Tenet**: 4. **Rules-out contradiction** (fabricated canonical text).

`topics/personal-identity` **L84** has the No Many Worlds tenet rejecting MWI "partly because it creates \"unanswerable indexical questions: why am I *this* instance and not another?\"" — presented as a quotation. `grep -c "unanswerable" obsidian/tenets/tenets.md` returns **0**: the string is nowhere in the tenet in any form, and its unscoped sense is the pre-L117 register. Two ancestors of the same stale-internal-quote were fixed in W31/W32 (`archive/voids/indexical-void` L113, `topics/vertiginous-question` L188); this live locus was missed.

I read all sixteen other quotations attributed to a `tenets` wikilink. **Fourteen are verbatim-correct** against the live page (`concepts/coupling-modes` L36, `concepts/conservation-laws-and-mental-causation` L186, `topics/comparing-quantum-consciousness-mechanisms` L155, `topics/self-stultification-as-master-argument` L73 among them) and two quote *rivals* rather than the tenet. One needs a look: `concepts/integrated-information-theory` **L154** has Bidirectional Interaction holding that consciousness "selects among superposed neural states, collapsing quantum indeterminacy" — not a live quotation, and it states pre-decoherence variant (a) as the tenet's content where L91 leaves the choice open and L105 specifies improper-mixture components "not already-definite alternatives".

**Recommendation**: fix L84 and `integrated-information-theory` L154 together; both single-sentence. Keep the lens — cheap, mechanical, first run.

### Warning 7 — the improper-mixture qualifier: seven siblings, unmoved, unminted

**Tenets**: 2, 3. The predecessor's Warning 4, carried whole. `tenets.md` L105 was corrected on 09-04 to "The brain presents options—**improper-mixture components awaiting actualisation, not already-definite alternatives**—and the mind selects", which blocks reading selection as a pick from a pre-existing classical menu. `apex/moral-architecture-of-consciousness` L146 has the qualifier. **All seven siblings verified still bare, in both trees:**

| File | Line | String |
|---|---|---|
| `topics/valence-and-conscious-selection` | 101 | "The brain presents options; valence denominates them; consciousness selects." — its whole paragraph was rewritten this window and the sentence survived verbatim |
| `concepts/neuroplasticity` | 56 | "The brain presents options; consciousness selects; selection produces plasticity." |
| `topics/attention-and-the-consciousness-interface` | 171 | "The brain presents options (brain → mind); consciousness selects among them" |
| `topics/trilemma-of-selection` | 129 | "The brain presents options to consciousness (world→mind); consciousness selects among them" |
| `topics/brain-computer-interfaces-and-the-interface-boundary` | 83 | "the brain presents options, consciousness biases selection" |
| `concepts/coupling-modes` | 46 | "The brain presents options; consciousness selects which set of options to actualise one from." |
| `concepts/retrocausality` | 155 | "The brain presents options; consciousness selects; the selection determines which neural history becomes actual" |

An eighth, same root: `topics/the-binding-problem` L206 ("selects among possible unified experiences rather than passively registering whatever the brain presents"). A ninth: `voids/language-thought-boundary` L158 frames Tenet 2 as pre-decoherence variant (a).

**Recommendation**: unchanged from the predecessor — one sweep, word swaps only, the replacement clause exists verbatim in two files. Check length on `valence-and-conscious-selection` (open human length decision at `todo.md`). That this is the second consecutive check reporting it unmoved is the finding.

### Warning 8 — Tenet 2 register drift, both directions, and one inverted falsifier

**Tenet**: 2. Now calibrated against a settled canonical page.

- **Inverted falsifier** — `concepts/quantum-interpretations` **L167**: "If well-designed experiments consistently found conscious observation produces identical results to unconscious measurement, the consciousness-collapse hypothesis would weaken." The corridor reading *predicts* identical unconditioned results, so this null cannot disconfirm it; `tenets.md` L81 makes the falsifier a detected *deviation*, not an absence of one.
- **By-construction recast as a sensitivity limit** — `concepts/consciousness-and-scientific-explanation` **L58**, three defects in one sentence: "predicts that consciousness biases otherwise indeterminate quantum outcomes" (novel-prediction register against L81's consistency claim), "a difference **currently below detection thresholds**", and "The prediction could in principle be tested as measurement technology advances". `tenets.md` L75: indistinguishable "by construction, **not by any sensitivity limit**".
- **Over-concession, in-principle immeasurability** — `topics/personal-identity` **L188** ("the quantum mechanism is a philosophical framework, **not a testable hypothesis**"), inherited faithfully from `concepts/measurement-problem` **L63** ("This unfalsifiability is a genuine cost"), so the fix is a two-file one; `voids/observation-and-measurement-void` **L152** ("physical instruments cannot measure it—**not as a practical limitation but as a logical consequence of ontological separation**" — also an LLM-cliché "not X but Y" per CLAUDE.md); `concepts/observational-closure` **L68** ("no amount of experimental refinement can distinguish conscious selection from indeterminate collapse"), which became an intra-file contradiction *this window* when L110 was scoped and L68 was not; `topics/ethics-of-cognitive-enhancement-under-dualism` L53; `voids/predictive-construction-void` L129 ("none currently exist", against L75 naming Maier et al. 2018).
- **"cannot be rationally held"** — `concepts/observational-closure` **L88** and its Further Reading blurb **L121** ("Why epiphenomenalism cannot be rationally held even if it could be true"). `tenets.md` L103: the strongest version survives. The article never mentions the phenomenal-concept strategy, so nothing local absorbs the concession. Same family: `concepts/epiphenomenalism` L96 ("a fatal weakness that interactionism avoids"), two lines above L98's repaired "the self-undermining charge dissolves"; `topics/valence-and-conscious-selection` L182 ("a puzzle epiphenomenalism cannot" — rewritten this window with the "cannot" kept); `topics/phenomenal-value-realism` L176.
- **Mechanism over-commitment** (L71, P-Q10) — `concepts/von-neumann-wigner-interpretation` L112; `voids/capability-division-problem` L118; `voids/tenet-generated-voids` L143 ("the **most plausible** location", where L67 says "a *candidate* location").
- **Already queued, do not re-mint** — `topics/dualism-as-ai-risk-mitigation` L100–L106 (the absence-of-bound slide, "prayer-equivalent dynamics at scale", and the unbounded-magnitude argument, which its own sibling `topics/instrumental-convergence` L87 names "the **absence-of-bound fallacy**" and quarantines into this file). Fully covered by the open **P1** at `todo.md` L46 from `outer-review-2026-09-06-astra-pro`. Worth recording that this check reached the same verdict independently.

**Recommendation**: `consciousness-and-scientific-explanation` L58 and `quantum-interpretations` L167 first — they are wrong in the direction almost nothing else is, and an inverted falsifier is worse than a mis-scoped one because it tells a reader the framework can be refuted by a result it predicts.

### Warning 9 — the L107 repair's stranded siblings: the retired canonical string, still live on two apex theses and the register entry that seeds the register

**Tenet**: 2. **New this window, mechanical, and the cheapest fix in the report.** Found by the dependency-freshness lens; every locus was well-formed until 09-04, when `tenets.md` L107 replaced "any **aggregate-statistics** test" with "any ***unconditioned aggregate*** test" and deleted "and so leaves no statistical trace".

The exact retired string is still live in three places in the live tree, and I found the third only after correcting my own error — my first status check for it was scoped to `tenets.md` alone and returned a false "repaired":

| File | Locus | Why it compounds |
|---|---|---|
| `positions/methodology-and-calibration` | **L109** (P-M4 *Asserts*) — "the testability cost of Born-statistics-preserving outcome-selection (**empirical indistinguishability under aggregate-statistics tests**)" | P-M4 is the register entry downstream articles inherit their framework-stage register *from*. `positions/positions.md` L61 names this exact hazard: "an over-claim of untestability runs *against* the Map, so review tends to ratify it rather than challenge it" |
| `apex/research-programme-decisions-under-the-map` | **L47** (`apex_thesis:`) — ranks work "above **aggregate-statistics tests** that the self-concealing interface predicts will read null" | An `apex_thesis` seeds downstream synthesis, and this one is about *which experiments are worth running* — the register error changes the research-prioritisation output |
| `apex/self-concealing-interface` | **L87** — "perfect security is *equivalent to* **zero third-person statistical evidence**"; "**no aggregate test can ever witness the channel**". Same file **L3** (`description:`) and **L55** (`apex_thesis:`) carry the unscoped "hide from aggregate measurement" | **L77 of this same file was rescoped this window and L87 was not.** L87 forecloses horn (a), which the article's own L133–L135 and Prediction 2 commit to, and contradicts its own L143 ("residual mutual information with a preregistered intention covariate that the unconditioned distribution does not show") |

Two further loci carry the deleted clause rather than the retired string: `concepts/pragmatism` **L44** ("leaves no statistical trace that any presently conceivable instrument could resolve", unscoped) and `topics/the-epiphenomenalist-threat` **L139** ("leaves no statistical trace at the aggregate level", milder). By contrast `positions/subject-census` L47 is **exemplary** and should not be touched — it explicitly *withdraws* the claim: "One consequence registered here is now withdrawn: that the census leaves no statistical trace, because exact Born preservation under the corridor reading … *makes* two models differing on it empirically distinguishable."

**Recommendation**: mint this one first of all of them. It is five loci, all word-class substitutions, all with the transplant wording sitting in `tenets.md` L107; and unlike every other family here it has a hard completion test — `grep -rnF "aggregate-statistics test"` over the live tree must return zero. Do the `self-concealing-interface` trio (L3, L55, L87) in one pass so the surfaces do not strand again.

## Notes

### Note 1 — the "gains support" signature: a measured family, and why the count is not the finding

VOIDS-E observed that `gains support` is greppable, and it is. Corpus-wide, **52 files** carry "(gains|finds|receives) (support|evidence)" applied to a tenet. Splitting them mechanically on whether a disarming clause sits in the same or next line: **27 hedged, 32 bare**. `positions/voids-as-evidence` P-V2 forbids reading a defeater-removal as an evidence upgrade, so the voids share (13 of the 32) is the sharpest.

**The 32 is a candidate set, not a defect count.** I read five and confirmed four — `voids/plurality-void` L87, `concepts/mine-ness` L136, `voids/resolution-void` L82, `concepts/materialism` L98 (Warning 1) — while `topics/phenomenology-of-imagination` L116 is a **false positive**: it hedges in-line with "on the dualist reading" and follows with "*consistent with* … though the physicalist can respond", which my classifier's vocabulary missed. So precision is roughly 4-in-5 and the honest statement is ~25 likely defects, of which 4 are verified. The corrected form exists in-corpus and is worth naming as the transplant: `voids/conceptual-metabolism-void` L114 "a coherence claim, not added support"; `voids/interoceptive-void` L87 "the connection is interpretive rather than evidential"; `voids/fusion-void` (new this window) "this locates the explanatory residue rather than evidencing any account of it".

### Note 2 — matrix inheritance, and the animal/ethics cluster as its clearest instance

`tenets.md` L157–L177 mark cells **Not invoked**; L175 names importing them as support "alignment-line inheritance". Verified live: `topics/phenomenal-normativity-environmental-ethics` **L145** ("Animal consciousness is not epiphenomenal") and **L143** ("neural architectures capable of supporting the relevant quantum-level interactions") — both cells marked Not invoked for the animal row at L162, and L143 additionally contradicts the same file's L119, which fixes the consciousness-distribution boundary on cortical/thalamic homology; `topics/animal-consciousness` L186/L192 make mental causation the load-bearing tilt for a species verdict without declaring the divergence L177 requires; `concepts/sentientism` L95; `concepts/continual-learning-argument` L156/L160/L164; `concepts/ai-epiphenomenalism` L113; `topics/ethics-of-consciousness-invertebrate-question` L47/L51/L115 (mitigated — the claims are conditional — but undeclared).

The corrected form keeps appearing, which is the encouraging half: `topics/moral-status-threshold-or-degrees` L98 (new this window) marks Tenets 2 and 3 as not bearing; `concepts/anti-correlated-metacognitive-signal` L106 "explicitly declares silence on Tenets 2, 4, 5"; `topics/thermal-consciousness-and-the-interface` L97; `concepts/type-specificity` (Tenets 2/3/4 correctly absent for a qualia-cluster article).

### Note 3 — Tenet 3 grounded in the introspective route L93 excludes

`tenets.md` L93 holds Tenet 3 "as *a metaphysical commitment supported by self-stultification and indirect evidence, not as a directly introspectible datum*". Verified live: `voids/observation-and-measurement-void` L156; `voids/language-thought-boundary` L156 ("This deliberate investigation is mental causation in action"); `voids/disappearance-voids` L164; `topics/the-binding-problem` L206 ("Voluntarily shifting attention" / "the felt directedness of consciousness"); `topics/consciousness-and-the-phenomenology-of-place` L108; `topics/consciousness-and-the-phenomenology-of-translation` L157 (contradicted by its own L117, "The translator experiences having translated; the translator does not experience the translating"); `concepts/quantum-interpretations` L157; `concepts/type-token-causation` L102; `concepts/ai-epiphenomenalism` L63; `concepts/valence` L97 and its string sibling `concepts/somatic-interface` L131.

`^tenet-3-standing` citation coverage has grown from 13 files to **14** in two days — one new citation against roughly a dozen new bare assertions. The convention is not spreading at the rate the defects are.

### Note 4 — predecessor line-pointer corrections, recorded so they are not chased again

VOIDS-E could not resolve two of the predecessor's pointers and was right not to force them:

- `voids/observation-and-measurement-void` "near L112" — L112 is the IIT/phi paragraph in both base and HEAD and carries no inflation. The real loci are **L152/L154/L156**.
- `voids/epistemological-limits-occams-razor` "near L49" — **not confirmed**. L48–50 is self-referential-trap/Goodman material. The file is the batch's best-calibrated article (L64 "removing a defeater is not the same as supplying positive evidence"; L104 "The Map's commitment to dualism therefore rests on its other arguments … not on this void") and enforces the Tenet 5 symmetry properly. The predecessor most likely confused it with the near-homonym `arguments/epistemological-limits-of-occams-razor`.

Also corrected: the predecessor's `voids/voids.md` locus has moved L279 → **L283**.

### Note 5 — the positions register: audited band-by-band, and it holds

The register is the surface most reports assume rather than check, so its cleanliness is worth recording.

**`positions/positions.md` L55's discriminability aggregate was re-derived independently and is exact**: direct 3 · indirect 22 · in-principle 1 · none 7 · none-by-construction 3 · n/a 20 = **56 live**. All 56 `**Status**:` fields well-formed; no retired entry silently re-asserted; L78's Tenet 4 scoping still tracks `tenets.md` L117 exactly.

**All three register/calibration-history pairs checked band-by-band, no drift either way** — `value-in-selection` (P-VS2 credence moderate→low, discriminability direct→indirect), `moral-status` (P-MS2 grade D→n/a, plus a documented same-day maturity round trip), `methodology-and-calibration` ("no band moved, no position added" true on both sides). `apex/embodied-interface`'s diff correctly *lowered* P-VS2 and added the attentional-salience-clamp confound, matching `value-in-selection` L60.

Three wording items, no band changes warranted:

- `positions/arguments-for-mental-causation` **L52** (P-MC1 heading) — "Self-stultification **decisively** burdens bare-correlation epiphenomenalism". `tenets.md` L101 conditionalises the bite even against the bare-correlation reply ("The Map accepts this conditionality"), and `positions.md` L84 states the same claim as plain "burdens". The entry's own *Asserts* paragraph is the calibrated version; only the heading outruns it — and it does so at the register home for the one conjunct the foundational-dependency test says Tenet 3's rationale rests on.
- `positions/moral-status` **L49** (P-MS1 *Calibration*) — "for which Tenet 1 is the **sole support**", where the sibling entry P-VS3 words the identical dependency correctly as "Tenet 1 … as defeater-removal only, per P-M1". Effect is benign (grade stays D), but P-M1 names this slide as "its central, named drift vector". A wording fix, not a band fix.
- `apex/born-preserving-causal-efficacy` **L203** — "ensemble-detectable psi would falsify rather than confirm **the Map**". Correctly scoped to *ensemble*, over-scoped in target: an unconditioned deviation falsifies the *corridor reading*, not the Map, which keeps Route 2 — and the same file's L123 calls minimum-outside-corridor "the route the Map is likeliest to be pushed toward". The article is otherwise the batch's exemplar: L93 explicitly refuses to assert preservation "at *every* conditional grain", which "would choose horn (b) by stipulation".

One non-tenet stranded repair worth passing to whoever fixes `cross-modal-capability-division`: this window's diff replaced "single insular integrator" in the brain-side section with "the insula is a node, not the hub: 7-Tesla mapping describes a whole-brain system … not one cortical integrator (Zhang et al., 2025)", and left the retired wording live at **L128** (Synthesis, "converges on a single insular integrator") and **L151** (Source Articles blurb, "converges on the insula"). Both are also live in `hugo/content/apex/cross-modal-capability-division.md` at L135 and L158.

### Note 6 — queue discipline, and the archive tree

**The predecessor's Note 5 pattern held exactly, and is now three-for-three.** A recommendation to **mint a new task** is executed (predecessor Warnings 3 and 7 both minted, both closed within 48h, and the Warning-7 fix went beyond a word swap to the substantive Lakatos rewrite). A recommendation to **amend an existing task** is not (the Tenet 4 append has failed three consecutive times). A warning producing **no task at all** stays live in full (predecessor Warnings 1, 2, 4, 5, 6 — every spot-checked locus still on disk).

Two consequences: the Tenet 5 family has survived four checks unminted and a fifth restatement will not move it; and this report recommends no appends.

**Sync**: clean on every tenet-critical string — "unconditioned aggregate" 29 files / 29, "improper-mixture components awaiting actualisation" 6 / 6, and every flagged locus verified present in both trees. **But the trees were not in sync when this check began**, and the discrepancy is worth recording because it is invisible to any string check that greps both trees for the same string. `embed-videos` ran at 09:01 today (commit `6e3dfc072e`), edited `obsidian/topics/consciousness-and-the-phenomenology-of-translation` — adding the video embed, the `embedded_videos` frontmatter and a fresh `ai_modified` — and **did not sync**. Until this check's sync ran, the served Hugo copy lacked the embed and advertised `ai_modified: 2026-06-09`, three months stale. `obsidian/workflow/todo.md` was likewise ahead of its Hugo copy by the completed-P1 rewrite. Both are now caught up; no other divergence found. Note that the stranded article is one of the three-defect files in Warning 2, so its Hugo copy was serving the uncalibrated text at a stale timestamp.

**Archive tree**: `archive/` (524 files, all `archived: true`, all `noindex`) carries retired registers at live URLs; expected for frozen content and **no action recommended on the prose**. The predecessor's one genuine consequence is **still live**: `archive/topics/value-blind-vs-value-sensitive-selection` L72 links to `[[valence#Valence Does Causal Work]]`, an anchor the 09-02 heading rename killed. The live-tree twin was updated; only the archive copy dangles.

## Carried families

### Family AA — the sign/direction assumption: **OPEN, unmoved**

P3 live at `obsidian/workflow/todo.md`. `apex/attention-as-causal-bridge` L86 and `apex/phenomenology-of-consciousness-doing-work` L99 intact. Per standing instruction: recorded, not re-counted, not re-minted, not patched.

### Predecessor Warning 2 — the repair that re-targeted without weakening: **OPEN**

`apex/phenomenology-of-consciousness-doing-work` L3 (`description:`) and L50 (`apex_thesis:`) still read "epiphenomenalism **cannot accommodate**", mirrored on the corpus's highest-traffic synthesis surface at `apex/apex-articles` L264. L155 still carries "the position the four-feature tracking **falsifies**" and "The profile **establishes** that consciousness does cognitive work" while opening "No single line of evidence is decisive." L181's Further Reading blurb still reads "evidence that consciousness does real causal work". The residue task at `todo.md` L2178 covers the L60 roadmap locus only. `tenets.md` L101/L103 hold epiphenomenalism unrefuted and the phenomenal-concept version surviving.

## Files passing all checks (window, 36 of 95 named individually)

`apex/born-preserving-causal-efficacy`, `apex/embodied-interface`, `concepts/affective-forecasting-gap`, `concepts/anti-correlated-metacognitive-signal`, `concepts/consciousness-value-connection`, `concepts/intrinsic-nature`, `concepts/moral-census-opacity`, `concepts/ontic-structural-realism`, `concepts/penfield-interactionist-dualism`, `concepts/possibility-probability-slippage`, `concepts/type-specificity`, `tenets/tenets`, `topics/authorship-of-action-divergence`, `topics/born-rule-and-the-consciousness-interface`, `topics/conversion-disorder-as-consciousness-side-fault`, `topics/ethics-of-cognitive-enhancement-under-dualism`, `topics/ethics-of-possible-ai-consciousness`, `topics/hylomorphic-dualism-and-the-interaction-problem`, `topics/instrumental-convergence`, `topics/interoceptive-consciousness-and-the-interface`, `topics/moral-status-threshold-or-degrees`, `topics/probability-problem-in-many-worlds`, `topics/reconsolidation-as-selection-window`, `topics/representation-adequacy-and-irreversible-intervention`, `topics/the-experience-requirement-on-well-being`, `topics/the-steelman-for-value-blind-selection`, `topics/thermal-consciousness-and-the-interface`, `topics/wanting-liking-and-the-value-in-mechanism-fork`, `voids/commensurability-void`, `voids/conceptual-metabolism-void`, `voids/epistemological-limits-occams-razor`, `voids/fusion-void`, `voids/interoceptive-void`, `voids/mapping-mind-space`, `voids/palette-extension-void`, `voids/three-kinds-of-void`.

**The `positions/` register passes structurally** — see Note 5: all 56 live entries well-formed, the L55 discriminability aggregate re-derived exact, no retired position re-asserted, all three register/calibration-history pairs checked band-by-band with no drift either way. Three of the eight `positions/` files in the window are therefore not in the list above because they carry a wording item (`arguments-for-mental-causation` L52, `moral-status` L49) or a Warning 9 locus (`methodology-and-calibration` L109); none warrants a band change, and the other five pass outright.

**`tenets.md` itself passes.** The window diff repaired the predecessor's L107-vs-L75/L81 contradiction and introduced no new internal inconsistency; L75, L81 and L107 now agree, and the second hunk (moving Frankish out of the phenomenal-concept attribution into a separately-marked illusionism reply) is consistent with L55. One pre-existing residue: L117 gives Tenet 4 a second support against first-personally-centred variants — "the rejection of modal realism and the insistence on global uniqueness" — that L145's "must therefore rest on the *indexical* objection" does not list. Registered honestly as background posit (3) at L183, so defensible, but the two sections give different answers to what Tenet 4 rests on.

**All five new files this window pass clean** (`topics/moral-status-threshold-or-degrees`, `topics/representation-adequacy-and-irreversible-intervention`, `topics/the-experience-requirement-on-well-being`, `voids/fusion-void`, `voids/palette-extension-void`), several exemplary: `the-experience-requirement-on-well-being` L91 cites `^tenet-3-standing` and inherits the debt by name; `representation-adequacy` L108 surfaces P-Q3 and P-Q10 rather than discharging them; `fusion-void`'s alignment section pre-empts every inflation shape in the catalogue. Third consecutive check reversing the fresh-create defect-tail expectation — now the series' strongest signal that the expand-topic contract has absorbed the calibration discipline.

## Method note

Six parallel batch reviewers (topics ×2, concepts ×2, voids+tenets, apex+positions), each reading full files plus per-file diffs against the base; the driver re-verified **every** flagged locus with fixed-string matching — 66 checks, **zero false positives**, which is the best batch-reviewer precision in this series and is worth attributing to the brief carrying the calibration standards as line-numbered quotations rather than as prose descriptions.

**Two new lenses.**

*The alignment-subsection register lens* — the instrument the predecessor said did not exist. For each of the 826 live articles it extracts the `## Relation to Site Perspective` section, measures strong-modal and hedge density inside it against the same article's body, and ranks by the gap. 757 carry the section; 21 do not, of which 18 are `positions/` register and calibration-history files where the omission is structurally appropriate. Reading the top eight candidates found four real defects (`voids/amplification-void`, `concepts/filter-theory`, `arguments/many-worlds-argument`, `topics/arguments-against-materialism`) and three exemplary false positives (`concepts/penfield-interactionist-dualism`, `concepts/quiddity-epiphenomenalism-and-the-contingency-thesis`, `concepts/improper-vs-proper-mixtures` — all three stating the discipline better than the tenets page does). **The metric counts words, not claims**: it is a queue for reading, never a verdict. The script is disposable; regenerate the ranking, do not cache it.

*Quoted text attributed to `tenets.md`* — cheap, mechanical, found Warning 6 on its first run. Sixteen candidates: one fabricated, one mis-stating the tenet's mechanism commitment, fourteen verbatim-correct.

**The dependency-freshness lens paid for itself twice**, both times because `tenets.md` moved rather than because any article changed — it produced Warning 9 and most of Warning 8's stranded siblings, findings no per-article lens can reach because each locus is well-formed read alone. The procedure worth keeping: after reading the canonical page's diff, grep the live tree for the *exact strings the diff removed*, not for the concepts they expressed.

**Two lenses tried that returned nothing, recorded so they are not re-run.** (1) *Archived descriptions on the machine-metadata surface*: `hugo/layouts/partials/machine-meta.html` has no `archived` guard, so archived articles' `description:` fields are emitted into `citation_description` and JSON-LD with only a `robots` noindex on the page. I checked all 524 for retired tenet claims and the yield is noise — "cannot" in a void's description is definitional, not an over-claim. (2) *Broken tenet anchors*: only seven `^` anchors exist on the tenets page, and a first pass appeared to show ~121 citations of twelve non-existent variants. **That was a grep artefact** — `\b` does not bound against a hyphen, so `tenets#^bidirectional` matched inside `tenets#^bidirectional-interaction`. The live content tree uses **only** the six valid anchors; every odd variant lives in `obsidian/reviews/`, `obsidian/workflow/archive/` or `archive/`, which is echo. I nearly reported a fabricated defect from two confirming greps, and record it here for the same reason the predecessor recorded its own two string-sweep failures: in this corpus a string sweep is a hypothesis, and a *negative* result needs a positive control before it is believed. The one residue is cosmetic — 17 live-tree citations use the heading form (`tenets#no-many-worlds`) rather than the block-anchor form; both resolve in Hugo.

**Two driver errors, both caught, both recorded because the shape recurs.** (1) The grep artefact above — a regex whose `\b` did not bound against a hyphen manufactured 121 phantom broken anchors, confirmed by a second grep that shared the same flaw. (2) My status check for the string retired from `tenets.md` L107 was **scoped to `tenets.md` and `hugo/content/tenets/` only** and printed "NO HITS (repaired)". That was true of the file I searched and false of the corpus: APEX-POSITIONS-F found the string live at `positions/methodology-and-calibration` L109, and widening my own grep then found a third locus F did not have. A narrow zero is not an absence — and a *driver* assertion of absence is worse than a batch reviewer's, because nothing downstream re-checks it.
