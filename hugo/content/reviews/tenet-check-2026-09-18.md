---
ai_contribution: 100
ai_generated_date: 2026-09-18
ai_modified: 2026-09-18 09:55:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-18
date: &id001 2026-09-18
description: 'Tenet check 135: the 09-17 lead item closed in 47 minutes and items
  2-3 became tasks that cannot be picked — four check-tenets tasks are open at P3,
  which the cycle never selects. A 53-file delta read finds the Tenet-3 alignment
  paragraph is the corpus''s single systematic defect, self-contradicting in twelve
  files.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-09-18 09:55:00+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-09-18
topics: []
---

# Tenet Alignment Check

**Date**: 2026-09-18 09:55 UTC
**Report**: 135th in series
**Files checked**: 678 (`topics/` 329, `concepts/` 327, `positions/` 22) by the direct-contradiction battery, extended to `apex/` and `voids/` for the two corpus-wide family sweeps; 53 (every file in the three sections committed since 2026-09-17 00:00 UTC — 28 topics, 23 concepts, 2 positions) read in full by three independent readers. Every locus below was re-verified by the driver at the cited line, printed at the match offset rather than from the line start.
**Counts are FAMILY counts, not locus counts.**

**Errors**: 0
**Warnings**: 15 families (7 carried unactioned, 3 carried-and-extended, 5 new) across ~95 loci
**Notes**: 21 loci

## Summary

1. **Zero ERRORs for the 135th consecutive run.** The battery (33 patterns, emphasis- and
   wikilink-normalised, NFKC, case-insensitive) returned 391 hits. A marker filter isolated the 28
   with no expository, conditional or attributive cue in their preceding context; all 28 were then
   read by hand and all 28 are expository — an opponent's view, an `if epiphenomenalism is true`
   antecedent, a Further Reading gloss, a `description:` field, or a Map-voice rejection. No
   Map-voice endorsement of eliminativism, epiphenomenalism, many-worlds, or a parsimony verdict
   against dualism exists in the corpus.

2. **The 09-17 lead item closed in 47 minutes and closed well.** `a9bb5bef1d` (01:54 UTC) fixed
   `concepts/improper-vs-proper-mixtures` L58 and L96 exactly as specified, in both trees. An
   independent reader who did not know it had been flagged read the file today and named L96 as a
   model treatment of `tenets.md` L125. Part 1 records a method warning about how it was verified.

3. **The structural finding of this run: items 2 and 3 *were* minted as tasks, and that is why
   they will not happen.** Four content tasks with `Source: check-tenets` are open and `pending` —
   from 2026-08-26, 2026-09-14 and 2026-09-17 (×2). **Every one is P3.** `CLAUDE.md` states the
   cycle's queue slots pick "from P0-P2 todo queue" and that replenishment counts "active tasks
   (P0-P2)". Minting a tenet finding at P3 is therefore equivalent to carrying it in the review
   file, except that it also looks discharged. The 08-26 task names
   `psychophysical-laws-bridging-mind-and-matter` L204; a reader who had never seen that task
   re-found the identical locus today, 23 days later, unchanged (Part 3).

4. **The Tenet-3 alignment paragraph is the corpus's one systematic defect, and it is now
   measured.** Across 53 delta files the three readers independently converged on the same shape:
   an article whose Tenet-1, Tenet-4 and Tenet-5 alignment paragraphs are scrupulously calibrated,
   whose **Bidirectional Interaction** paragraph then lets felt effort, felt agency, or a
   conscious/unconscious processing dissociation stand as evidence for *actual* mental causation,
   with no common-cause concession. **In twelve files the refusal of that exact move is written in
   the same file** — usually in the adjacent paragraph. `concepts/episodic-memory` L178 says
   "Episodic memory is compatible with the tenet; it does not argue for it" and L176 says the
   working-memory asymmetry "exemplifies this causal role". `concepts/moral-responsibility` refuses
   the phenomenology move for Tenet 4 twice (L99, L159) and runs it for Tenet 3 four times
   (L66, L87, L127, L143). This is not a blind spot; it is a discipline applied everywhere but one
   paragraph (Part 4, Family B).

5. **Four new families, two of them tenet-*content* errors rather than over-claims.**
   `apex/contemplative-path` L136 calls it "The honest assessment" that contemplative evidence
   "eliminates epiphenomenalism and reductive materialism decisively", while the same file's L184
   and L194 concede the plasticity evidence "does not discriminate" (Family J).
   `concepts/spontaneous-collapse-theories` L115 names Stapp-Zeno as what "The Map's framework
   favors", where `tenets.md` L71 makes post-decoherence selection the strongest endorsed path —
   and the file contains **zero** occurrences of "post-decoherence" against a control of 40
   concept files that have it (Family M). Family K is a seven-locus Tenet-5 family in which the Map
   claims the parsimony point for its own option; Family L is a three-file propagation chain in
   which two articles inherit an unscoped unfalsifiability claim by citing the file that makes it.

---

## Part 1 — The 09-17 closures verified, and a method warning

**Lead item closed — `a9bb5bef1d`, 2026-09-17 01:54 UTC (47 minutes after the report).** Diff read
line by line:

| 09-17 locus | Was | Now | Scoped correctly? |
|---|---|---|---|
| `improper-vs-proper-mixtures` L58 | "his preferred exits were Bohmian mechanics and objective collapse, both of which the Map declines" | "…and **consciousness-free** objective collapse, both of which the Map declines" | yes — matches `tenets.md` L125 |
| same L96 | "confirmation of such dynamics would remove the locus where consciousness is proposed to act" | "…would **fix the baseline the Map's prebiotic resolution already assumes; only a regime leaving no neural slack would** remove the locus…" | yes — and a reader blind to the task independently named L96 a model treatment today |

**Method warning for this series — a substring key cannot verify a fix that *extends* the matched
phrase.** The driver's first-pass check of both keys reported them PRESENT at the original line
numbers and concluded nothing had moved. Both were false presences: the repaired text still
contains "both of which the Map declines" (now preceded by "consciousness-free") and still contains
"remove the locus where consciousness is proposed to act" (now governed by "only a regime leaving no
neural slack would"). The corrected rule: **when the recommended fix is an insertion or a
qualification, the closure key must be the *disqualifying* string, not the original phrase.** Verify
by reading the diff, not by matching the old key.

**Items 2 and 3 tasked, not actioned.** The five-file substance sweep (`- **File**:
`obsidian/concepts/implicit-memory.md`) and the russellian-monism pair plus `metaphysics-of-laws`
(`- **File**: `obsidian/concepts/russellian-monism.md`), both `Status: pending`, both P3. (Line
numbers are deliberately omitted: this report inserts blocks into `todo.md`, which shifts them —
grep the header text instead.) All keys live
at the 09-17 lines in both trees. Part 3 is about why.

**Item 4 (Family B-1) not tasked.** **Everything else is live and unmoved.** `git log` since
2026-09-17 01:07 UTC is empty for all fifteen carried-family files checked individually.

---

## Part 2 — Carried families still live, unactioned, uncovered

Every key re-verified today at the cited line in both trees, printed at the match offset.
`todo.md` split on enclosing `### ` headers; every open block naming each file was classified.
None covers the locus (the hits are cross-link batches, an `ai_system` audit, agentic-social
tuning, length decisions, and a citation-sourcing task).

| Family | Tenet | File | Line | Key (verbatim, links flattened) | Budget (body words; soft/hard) |
|---|---|---|---|---|---|
| W2a | 1 | `concepts/qualia` | 205 | "establish that some non-physical element enters the causal story" | 4032 `hard_warning` (2500/3500) — net-negative only |
| W2b | 4 | `concepts/qualia` | 213 | "preserve the determinacy that phenomenology demands" | same |
| W3 | 1 | `topics/enactivism-challenge-to-interactionist-dualism` | 108 | "irreducible without requiring a separate substance" | 2459 `ok` |
| W9 | 3 | `topics/consciousness-and-integrated-information` | 82 | "token-level causation is genuine causation" | 4000 `hard_warning` — at the ceiling; the gate is `>= hard`, so headroom is −1 |
| W10 | 3 | `topics/language-recursion-and-consciousness` | 190 | "demonstrates downward causation" | 4161 `hard_warning` |
| W11 | 3 | `concepts/ai-epiphenomenalism` | 63 | "consciousness does genuine causal work" | 2689 `soft_warning` |
| F (Part 3 of 09-17) | 1 | five files | — | "the Map's substance dualism" ×5 | **tasked, P3, pending** |
| F | 1 | `topics/consciousness-and-intersubjectivity` | 37 | "consciousness is ontologically individual (as the Dualism tenet requires)" | 2885 `ok`; the file's own L113 hedges the same claim |
| G (2nd file) | 2 | `topics/consciousness-and-the-metaphysics-of-laws-and-dispositions` | 150, 174 | "This dispositional analysis is hostage to" / "The tenet's defensibility is hostage to" | **tasked (with H), P3, pending**; 4201 `hard_warning`, net-negative only |
| H | 4 | `concepts/russellian-monism` 131; `topics/russellian-monism-versus-bi-aspectual-dualism` 146 | | "follows from its ontology" | **tasked, P3, pending** |
| I | 2 | `topics/russellian-monism-versus-bi-aspectual-dualism` | 114 | "that quantum mechanics has since undermined" | 3366 `soft_warning` |
| B (09-14/09-17) | 3 | 24 files, ~45 loci | all present | see 09-14 Part 4 and 09-17 Family B | see those tables |
| C | 2 | `concepts/delegatory-causation` 148; `topics/ethics-of-cognitive-enhancement-under-dualism` 52; `topics/quantum-darwinism-and-consciousness` 78/116; `topics/pragmatist-quantum-foundations-and-the-agent` 105; `concepts/prebiotic-collapse` 136 | all present | unscoped indistinguishability | `delegatory-causation` 3492, 7 words of headroom |
| D | 4 | `dualist-perception` 166; `consciousness-and-mathematics` 196; `aesthetics` 160; `intersubjectivity` 121; `prebiotic-collapse` 106; `metacognition` 188; `predictive-processing` 184; `mind-brain-separation` 118; `vertiginous-question` 160 | all present | felt-weight / felt-determinacy as evidence | |
| E | 5 | `quantum-completeness` 110 | | **tasked — P3, since 09-14**; see also Family K | 3176 `soft_warning`, 323 to hard |
| B-3 | 3 | `concepts/delegatory-causation` | 136 | "the self-undermining argument eliminates epiphenomenalism" | folded into Family J below |

---

## Part 3 — Standalone: four check-tenets tasks are open, and all four are unpickable

**This is the highest-leverage finding in the report and it is about the queue, not the corpus.**

Measured on `obsidian/workflow/todo.md` today, splitting on enclosing `### ` headers and reading
`- **Status**:` inside each block (the count excludes blocks under a `✓` or `~~` marker):

| Generated | Priority | File | Review file | Status |
|---|---|---|---|---|
| 2026-08-26 | **P3** | `topics/psychophysical-laws-bridging-mind-and-matter` | `tenet-check-2026-08-26.md` | pending |
| 2026-09-14 | **P3** | `concepts/quantum-completeness` | `tenet-check-2026-09-14.md` | pending |
| 2026-09-17 | **P3** | `concepts/russellian-monism` (+2 files) | `tenet-check-2026-09-17.md` | pending |
| 2026-09-17 | **P3** | `concepts/implicit-memory` (+4 files) | `tenet-check-2026-09-17.md` | pending |

`CLAUDE.md` describes the 24-slot cycle's sixteen queue slots as picking "from P0-P2 todo queue",
and describes replenishment as triggering when "active tasks (P0-P2) drop below 3". On that
description a P3 task is never selected by the loop; it waits for a human or for a promotion that
nothing in the tenet pipeline performs. The four tasks above are consistent with that: none has
moved, and the oldest has not moved in 23 days.

**The independent confirmation is the strongest part of this finding.** Today's reader for the
`topics/` batch had no knowledge of `todo.md`. It read
`psychophysical-laws-bridging-mind-and-matter` cold and returned L204 —
"The tenet is a philosophical commitment grounded in the phenomenology of agency—the experienced
reality that intention affects action, that effort affects outcome" — as its second-sharpest
finding, against `tenets.md` L93 ("not as a directly introspectible datum"). That is character for
character the locus the 2026-08-26 task was minted to fix, quoted verbatim in that task's own Notes
field. Twenty-three days and one full task lifecycle later, the sentence is unchanged.

**What follows for this report.** The actioning mechanism observed across 09-11, 09-14 and 09-17 is
the single "if only one thing" item, which has now closed three runs running (36 min, 36 min,
47 min). The list does not action, and *minting the list as P3 tasks does not action either* — it
converts a visible carry into an invisible one. This report therefore:

- mints **two** new tasks, both at **P2**, not P3, and says so in each task's Notes so the operator
  can demote them in one edit if the priority is unwanted;
- extends two existing tasks in place rather than minting siblings;
- carries everything else here, explicitly, rather than minting P3s that would read as discharged.

**For the operator.** The four tasks above are the real backlog. If P3 is intended to mean "never
picked by the loop", the tenet pipeline should stop minting at P3; if it is not intended to mean
that, the four are evidence of a selection gap worth a look.

---

## Part 4 — Delta read: 53 files committed since 2026-09-17, read in full

Three readers, 16–19 files each, briefed identically with the tenets page's scoping rules (L53/L57
substance neutrality; L69 minimality is empirical-constraint, not parsimony and not scale; L71/L77
live fallbacks and the pre-decoherence scope of the decoherence dispute; L75/L81/L107 unconditioned
register; L93/L95 `^tenet-3-standing`; L97 the comparative-cognition concession; L101/L103
self-stultification is not a refutation; L117/L121/L123/L183 the indexical objection and the
background posits; L145/L147 symmetric self-binding; L151–L177 the dependency matrix).

**21 of 53 files returned zero findings**, including both `positions/` files. Named where the file
is a model: `concepts/process-content-distinction` L83 (the model `^tenet-3-standing` treatment),
`topics/valence-and-conscious-selection` L79/L206 (the model L69 treatment),
`topics/sherrington-dualist-lineage` L95 ("On Tenets 2 and 3 Sherrington is silent, and the Map
records that silence rather than papering over it"), `topics/the-hard-problem-in-non-western-philosophy`
L149 ("This section is the Map's coherence commentary, not support the traditions supply"),
`concepts/improper-vs-proper-mixtures` (yesterday's fix), `topics/cross-architecture-llm-introspection`
L94, `topics/fish-sentience-and-the-teleost-pain-debate` L80,
`topics/plant-cognition-and-the-plant-neurobiology-debate` L101.

### Family B (extended) — the Tenet-3 alignment paragraph (Tenet 3; ~30 new warning loci in 18 files)

The single largest and most systematic family in the corpus. `tenets.md` L95 (`^tenet-3-standing`)
is explicit: the interface argument shows downward causation to be *available*, not *actual*, and
"Articles asserting that consciousness does 'real work' or 'genuine causal work' inherit that debt
rather than discharge it." L93 adds that consciousness "cannot first-person-verify its own causal
power". L97 supplies the mandatory concession shape for dissociation evidence: "the same physical
substrate that produces logical reasoning could produce its phenomenal correlate without phenomenal
causation—so this evidence corroborates the tenet rather than establishing it."

**B-1: the same-file contradiction — the file's own neighbouring paragraph refuses this exact move.**
Fix by copying the guard that is already there. Twelve files:

| File | Tenet-3 locus | Verbatim (links flattened) | The guard, same file | Budget |
|---|---|---|---|---|
| `topics/phenomenology-of-linguistic-failure` | 115 | "An epiphenomenal consciousness could not try. … the experience of *effort* … implies causal participation." (also L111 heading "The Attempt as Evidence", L113, L123) | **none — but see B-2**; `epiphenomen` occurs only in the dismissing sentence | 2189 `ok` — **1810 to hard, the roomiest file in the family** |
| `topics/the-binding-problem` | 206 | "The fact that effortful attention shapes which streams unify suggests top-down causation … consciousness actively selects" | L204 "It is a candidate, not an established mechanism"; L208 "a framework-boundary disagreement, honestly noted as such"; L164 "does not, on its own, discriminate" — L206 is the **only** alignment paragraph in the file without a calibration clause | **3999 — 0 words to hard. Net-negative only.** |
| `topics/the-strong-emergence-of-consciousness` | 139, 163, 57 | "is evidence consciousness does causal work" / "Bidirectional Interaction is what strong emergence with downward causation entails" / "it exercises genuine downward causation" | L151 states the discipline the file then breaks: "A datum equally consistent with a classical mechanism cannot support the quantum reading *over* the classical one … a precedent, not a licence" | **3965 — 34 words to hard** |
| `concepts/moral-responsibility` | 66, 87, 127, 143 | "is the empirical ground on which agent-causal control, and so desert, stands" / "corresponds to genuine exercise of causal power" / "it provides evidence for what agent causation claims" | L99 "The objection is not that Many-Worlds fails the phenomenology, which it does not"; L159 "The phenomenology of choosing is not refuted by Many-Worlds; it is reproduced inside each branch" — the rule applied to Tenet 4 twice, refused for Tenet 3 four times | **3475 — 24 words to hard** |
| `concepts/episodic-memory` | 170, 176 | "it argues for Bidirectional Interaction" / "exemplifies this causal role" | L172 "the explanandum in sharpened form rather than support the Map draws from memory"; L178 "Episodic memory is compatible with the tenet; it does not argue for it" | **3498 — 1 word to hard. Net-negative only.** |
| `concepts/intersubjectivity` | 124 | "If phenomenology were epiphenomenal, it could not cause the verbal behavior…" | L122 "Phenomenological realism does not by itself entail dualism"; L110 "Intersubjectivity provides data; it doesn't determine interpretation"; L86 "suggestive support, not independent corroboration" | 2637 `soft_warning`, 862 to hard |
| `concepts/phenomenal-contrast-method` | 116 | "a marker of consciousness actively shaping action" | L114 "The method does not prove dualism on its own"; L104 concedes introspective unreliability. (Also a "not X but Y" style violation) | 2019 `ok`, 1480 to hard |
| `topics/phenomenology-of-memory-and-the-self` | 151 | "but the self that remembers also *revises*, sustaining commitments that influence future choices" | L79 "phenomenological reports—evidence about the structure of experience, not by themselves evidence for dualism"; L149 "the reading the Map places on this material rather than a conclusion the material delivers"; L153 Tenet 4 done correctly | **3996 — 3 words to hard. Net-negative only**, and an open NEEDS-HUMAN ceiling task already names this file. |
| `topics/consciousness-and-memory` | 96, 100, 102, 184 | "this distinction would be inexplicable" / "The most striking evidence for consciousness's causal role" / "attending to an automatic skill could not affect its execution" / "is what … argue for" | L182 does the discipline for Tenet 1 two lines above: "Dualism's explanandum is *sharpened rather than evidenced* by…". L102 does raise the materialist redescription and argue against it, which is why B-1 and not B-2 | **3995, 4 words of headroom — net-negative only** |
| `topics/contemplative-practice-as-philosophical-evidence` | 147, 197, 213 | "if consciousness were epiphenomenal, this distinction should not exist" / "the case for causal efficacy weighs heavily against epiphenomenalism" | L149 guards a different flank (physicalism vs dualism), L161, L173 — none addresses the common-cause reply | 3884 `soft_warning` |
| `topics/consciousness-and-probability-interpretation` | 123 | "requires causal flow from consciousness to physical behaviour … providing evidence of the very interface" | L93, same file: "invites the charge that it rides a distribution physics already fixed rather than doing causal work—the worry named ensemble-level-epiphenomenalism, which the Map holds open rather than resolved" | 2856 `ok` |
| `topics/the-self-minimal-narrative-and-substantial` | 147 | "if the substantial self is what the evidence actually discloses—through … the phenomenology of agency … through the regress that undermines eliminativism" | L97 "tilts the case toward substantiality without settling it"; L103 "the regress is pressing but not, on its own, decisive"; L129 "suggestive, not probative" — three guards, all contradicted; and the agency strand is never developed in the article | 3212 `soft_warning`, 787 to hard; the fix is −2 |

**B-2: no same-file guard** (fix needs the concession added, +10 to +19 words).
`topics/phenomenology-of-linguistic-failure` L115 (sharpest single locus in the delta: three
unhedged sentences, and the string `epiphenomenal` appears in the file only in the sentence
dismissing it); `concepts/binding-problem` L209 ("Unified consciousness selects, not merely
observes") — 3191w, 308 to hard, so the +19 concession is affordable;
`concepts/conservation-laws-and-mental-causation` L176 ("implies it's causally
efficacious") — **3813w, over the concepts hard ceiling by 314, net-negative only; happily the fix is
net-0: "implies" → "suggests"**, and the file's own L170 already says the
framework shows compatibility "not that it is *proven by*" physics;
`topics/quantum-holism-and-phenomenal-unity` L188 ("consciousness has downward causal efficacy" —
**+1 fix: → "downward causal efficacy would be available"**);
`topics/psychophysical-laws-bridging-mind-and-matter` L159 (pain asymbolia, "phenomenal valence
does causal work" — near-verbatim the phrase L95 flags; the disciplined version already exists at
`topics/valence-and-conscious-selection` L165);
`topics/emergence-as-universal-hard-problem` L113 (3130w, 869 to hard; equivocates an *explanatory* gap into a *causal*
claim — also the L175 alignment-line-inheritance failure, in the cluster the matrix marks
interactionism **not invoked** for); `topics/cross-cultural-phenomenology-of-agency` L95 ("tracks
genuine causal efficacy" — **net-0 fix: → "is an irreducible feature of experience"**, which moves
the claim to the tenet the argument actually reaches).

**B-3: Tenet 3 content misstated** — folded into Family J.

### Family J — epiphenomenalism reported as eliminated or incoherent (Tenet 3; 5 warning loci in 3 files) — NEW

`tenets.md` L101: self-stultification is "the deepest difficulty epiphenomenalism faces rather than
its refutation". L103: the phenomenal-concept strategy "handles the self-stultification objection
more directly", the charge "dissolves", and "the strongest version of the position survives".

**Positive control — the calibrated form exists and has propagated to five files**, which is what
makes the outliers defects rather than an unsettled house style:
`concepts/bidirectional-interaction` L59, `concepts/self-stultification` L205,
`positions/arguments-for-mental-causation` L56, `topics/self-stultification-as-master-argument` L169,
`topics/the-epiphenomenalist-threat` L172 — all of the form "not because self-stultification
*refutes* epiphenomenalism from inside the epiphenomenalist's framework".

| File | Line | Verbatim | Note |
|---|---|---|---|
| `apex/contemplative-path` | 136 | "**The honest assessment**: contemplative evidence eliminates epiphenomenalism and reductive materialism **decisively**." | **The same file concedes the opposite twice.** L184: "Reading neuroplastic change as downward causation is inherited from Tenet 3, and *by the admission above the plasticity evidence does not discriminate*." L194: "The evidence constrains rather than establishes … *so alone it does not discriminate*." |
| same | 126 | "This eliminates epiphenomenalism while staying neutral between physicalist and dualist accounts of how" | under the section heading "What the Evidence Eliminates" |
| `concepts/substrate-independence` | 188 | "See `concepts/epiphenomenalism` for why causally inert consciousness is **incoherent**." | the target article's own `description:` field says the opposite: "Self-stultification burdens its bare-correlation form; **the phenomenal-concept reply survives**" |
| same | 214 | "- `concepts/epiphenomenalism` — Why causally inert consciousness is incoherent" | a navigation surface carrying an unreviewed claim |
| `concepts/delegatory-causation` | 136 | "the self-undermining argument **eliminates** epiphenomenalism" | carried unactioned from 09-17 B-3 |

**Adjudicated NOT defects** (checked and cleared, so the next run does not re-flag them):
`concepts/possibility-probability-slippage` L87 "Tenet 3 … rules out epiphenomenalism" — this is
tenet content, `tenets.md` L109 literally says "**Rules out**: Pure epiphenomenalism";
`concepts/causal-powers` L85 — explicitly "a consequence conditional on the framework rather than an
independent refutation"; `topics/delegatory-dualism` L60 — a stipulated desideratum of the
framework, and the file guards at L164 ("Delegation does not refute these rivals").

**Fixes.** `apex/contemplative-path` **4341w, apex `soft_warning` (4000/5000), 658 words of
headroom**: L136 "eliminates epiphenomenalism and reductive materialism decisively" → "presses
hardest on epiphenomenalism and reductive materialism" (−1); L126 "This eliminates
epiphenomenalism" → "This presses hard on epiphenomenalism" (0); consider retitling L124.
`concepts/substrate-independence` **3662w, `hard_warning` (2500/3500) — net-negative only**: both
loci "is incoherent" → "is hard to sustain" (0 each). `delegatory-causation` L136 "eliminates" →
"presses hardest on" (0), 7 words of headroom.

**Why this is the lead item.** `apex/` is excluded from the deep-review candidate pool
(`tools/curate/deep_review.py`), so no other lens in the system reaches this page; the sentence
labels itself "The honest assessment"; and the file already contains the correction, twice, fifty
lines further down.

### Family K — Tenet 5 parsimony run forward for the Map (Tenet 5; 7 warning loci in 6 files) — NEW

`tenets.md` L145: "This tenet binds the Map's use of parsimony, not only its critics'. … The
discipline is symmetric: parsimony cannot decide for or against a framework when the relevant
knowledge is incomplete." L147 rules out "**internally**—any Map argument that leans on parsimony as
if this tenet did not apply to it." L175 names this as the *parsimony asymmetry* failure.

**Positive control — the corpus is overwhelmingly right about this.** Of 38 "more parsimonious"
occurrences, the large majority concede parsimony runs *against* the Map and invoke Tenet 5 to
decline it: `concepts/interface-threshold` L124 ("parsimony is a tiebreaker, not a verdict"),
`concepts/reinforcement-learning-reward-signals-and-machine-valence` L79,
`concepts/the-ownerless-suffering-argument` L127 ("the Map declines to let that count in its own
favour, as the tenet requires"), `topics/the-steelman-for-process-monism` L87,
`topics/graduated-middle-path-valence-modulated-attention` L97, `concepts/categorical-surprise` L105,
`concepts/universal-coupling-response` L93. The outliers are exceptions to a live discipline.

| File | Line | Verbatim | Fix | Δ |
|---|---|---|---|---|
| `concepts/dualism` | 172 | "ontological parsimony favours physicalism, but **explanatory parsimony favours dualism**" — in the canonical Tenet-1 concept page, under "### The Parsimony Objection"; no parsimony guard in the file | delete the clause; the paragraph's opening ("a 'simpler' theory that doesn't account for the data hasn't earned the parsimony discount") is the legitimate, symmetric move and stands alone | −13 |
| `concepts/intersubjectivity` | 126 | "The simpler hypothesis: consciousness exists and is intersubjectively accessible." | delete | −9 |
| `topics/the-strong-emergence-of-consciousness` | 167 | "the parsimony advantage **tilts back toward** strong emergence with mechanism" | → "neither side's parsimony advantage survives this tenet" | −4 |
| `concepts/implicit-memory` | 196 | "The **simplest** account that covers all the phenomena … treats consciousness as a genuine causal factor" — inside a section headed "### Occam's Razor Has Limits" | → "The account that covers all the phenomena…" | −1 |
| `topics/contemplative-practice-as-philosophical-evidence` | 59 | "the **most parsimonious** explanation is that those features are real properties of experience" — in the lead; the file's own L201 calls the opponent's use "the false parsimony the Map rejects" | → "the better explanation" | −2 |
| `concepts/quantum-completeness` | 110 | "Parsimony favours the interpretation that addresses the most questions, not the one with the fewest equations" — **intra-sentence contradiction**: the immediately preceding clause on the same line disclaims it ("The Map's claim is not that dualism is the simplest explanation") | delete the final sentence | −16 |
| `concepts/jourdain-hypothesis` | 127 | "The most parsimonious marker is the phenomenal character itself" — contradicted by the same file's L183 | → "The most direct marker" | 0 |

The whole family is **−45 words**. `quantum-completeness` L110 is the task from 09-14; the rest are
new or carried.

### Family L — an unscoped unfalsifiability claim propagating by citation (Tenet 2; 3 warning loci in 3 files) — NEW

`tenets.md` L75 scopes the indistinguishability to the *unconditioned aggregate* register and keeps
the intention-conditioned register open ([P-Q3](/positions/quantum-interface/#p-q3)); L81 lists three named falsifiers and calls Tenet 2 a
*consistency claim*, not an unfalsifiable one.

- **`concepts/measurement-problem` L63** (source): "Honest limitation: … consciousness-selection
  within Born probabilities is empirically indistinguishable from random collapse. **This
  unfalsifiability is a genuine cost.** The Map treats it as a philosophical framework compatible
  with physics rather than a competing physical hypothesis." Zero occurrences of "unconditioned",
  "conditioned on", "aggregate" or "[P-Q3](/positions/quantum-interface/#p-q3)" in the file. 3659w `hard_warning` — net-negative only.
- **`concepts/adaptive-computational-depth` L91** (dependent): "Adaptive computational depth …
  **inherits the unfalsifiability** … **As the measurement problem article acknowledges**,
  consciousness-selection within Born probabilities is empirically indistinguishable from random
  collapse." 1919w `ok` — 1580 words of headroom.
- **`topics/personal-identity` L188** (dependent): "**as the measurement-problem article
  acknowledges** … empirically indistinguishable from random collapse—the quantum mechanism is **a
  philosophical framework, not a testable hypothesis**." 4045w `hard_warning` — net-negative only,
  and an open NEEDS-HUMAN length decision already exists on this file.

Both dependents name the source in the citing sentence, so this is a measured propagation chain
rather than three coincidences: fixing L63 licenses and shapes both dependents. A file-level sweep
found 43 files making an indistinguishability claim, 25 of which carry the scoping vocabulary — the
control that makes this a defect rather than the house style.

### Family M — Tenet 2 content: the wrong mechanism named as the Map's own (Tenet 2; 2 warning loci) — NEW

**`concepts/spontaneous-collapse-theories`** — the file the 09-14 report fixed at seven loci, with
two residuals the 09-17 report recorded as notes. Both residuals are now confirmed as warnings, and
the second is worse than "notes" conveyed:

- **L112**: "- Requires large-scale quantum effects (microtubule-level), **not minimal
  interaction**" — reads Tenet 2's minimality as spatial *scale*. `tenets.md` L69 defines it as
  *empirical-constraint* minimality fixed by the rules-out clause, explicitly not parsimony-tracking
  and not a scale claim. `topics/bacterial-chemotaxis-and-minimal-biogenic-cognition` L90 cites this
  scoping note and gets it right.
- **L115**: "Orch OR … strains Minimal Quantum Interaction by requiring pre-decoherence coherence.
  **The Map's framework favors smaller-scale quantum selection (see `stapp-quantum-mind`)** or
  hybrid CSL-IIT models". `tenets.md` L71 makes post-decoherence selection "the strongest path the
  Map currently endorses" and groups Stapp's quantum Zeno with the proposals that "depend on
  pre-decoherence coherence and stand or fall with that more demanding assumption";
  `positions/quantum-interface` [P-Q4](/positions/quantum-interface/#p-q4) records Stapp-Zeno as demoted. The sentence is also
  self-undercutting: it faults Orch OR for requiring pre-decoherence coherence and then recommends a
  mechanism that requires it too.
- **Absence verified with a positive control**: `post-decoherence` occurs **0** times in this file
  (`decoherence` 13, `stapp` 3, `unconditioned` 0), against **40** concept files that do contain
  "post-decoherence". The Map's endorsed path is absent from its own collapse-theory concept page.

**Budget: 2857w `soft_warning` (2500/3500), 642 words of headroom** — the only file in the report's
priority list with room to spare. Fix: L112 → "Requires sustained pre-decoherence coherence at
neural scales" (−3); L115 → "The Map's framework favours post-decoherence selection (see
`apex/post-decoherence-selection-programme`), with Stapp-Zeno and hybrid CSL-IIT models as live
fallbacks below it" (+8).

### Family H (extended) — Tenet 4 derived from the actualisation ontology (Tenet 4; 1 new locus)

- **`concepts/bi-aspectual-ontology` L141**: "**No Many Worlds follows from taking actuality
  seriously.** If selection is real, one outcome becomes actual and the alternatives do not
  persist." Identical in structure to the two tasked russellian-monism loci; `tenets.md` L117 makes
  the indexical objection the weight-bearer and L183 files single-outcome actualisation as
  background posit (2), *downstream* of the rejection. The file guards the cognate Tenet-3 point
  correctly at L51 and L53 and leaves the Tenet-4 derivation unguarded. 2834w `soft_warning`, 665 to hard.
  **Action: extend `todo.md` L1738 rather than mint.**

### Family D (extended) — felt determinacy as evidence against MWI (Tenet 4; 4 new loci)

- **`concepts/binding-problem` L211**: "Phenomenal unity appears *globally* definite, not
  branch-relative." The next sentence correctly relocates the load to the indexical argument, which
  makes this one redundant as well as wrong — **delete, −7 words**.
- **`topics/quantum-holism-and-phenomenal-unity` L190**: "The phenomenal fact that *this* experience
  is unified—that I am having *this* binding rather than another—**requires** real collapse."
  The sibling `topics/the-binding-problem` L208 handles the identical point correctly ("the Map's
  reason for declining it is the prior commitment, not an internal contradiction").
- **`topics/consciousness-and-memory` L188**: "The felt experience of a memory solidifying into
  *this* version rather than another presupposes a single experiential timeline." The model
  withdrawal is verbatim available in the sibling `concepts/semantic-memory` L181.
- **`concepts/spontaneous-collapse-theories` L177/L189** (note): grounds Tenet 4 in the
  actualisation ontology; defensible as coherence commentary, but the indexical objection is never
  stated in the file.

### Family F (extended) — a background posit pinned on Tenet 1 (Tenet 1; 1 new locus)

- **`concepts/moral-census-opacity` L108**: "**Because consciousness is a distinct category** rather
  than a configuration of parts, the boundary around a subject is a real further fact the
  description of the parts does not contain." Derives primitive subject individuation from Tenet 1,
  which `tenets.md` L53 makes neutral between substance and property readings and L183 files as
  *unstated background posit (1)*; the file never invokes agent causation (L57). The file's own L64
  gives the commitment its correct home — "The Map holds closed individualism … ([P-I1](/positions/individuation-and-subjecthood/#p-i1))" — which is
  where L108 should source it. Otherwise an exemplary file: L112 applies Tenet 5 *against* a
  Map-convenient default. **Fix: source the claim to [P-I1](/positions/individuation-and-subjecthood/#p-i1) and background posit (1) instead of
  deriving it.** **Budget: 3495w against a concepts hard ceiling of 3500 — 4 words. The +15 wording is NOT affordable; use a net-zero swap instead — "Because consciousness is a distinct category" → "Because the Map holds subject boundaries real ([P-I1](/positions/individuation-and-subjecthood/#p-i1))" (0).**

### Family N — an unsettled dispute reported as won (Tenet 1; 2 warning loci) — NEW

`tenets.md` L55: the Map's concept pages "hold the contest open rather than settled", concede
illusionism "captures something", and "Tenet 1 records where the Map plants itself in an unsettled
dispute; it does not report that dispute as won."

- **`concepts/spontaneous-collapse-theories` L135**: "Either way, something requires explanation that
  pure physics doesn't provide." The sibling in the same delta batch,
  `concepts/quantum-interpretations` L147, states the correct position: "Frankish (2016) rebuts the
  naive 'something must be under the illusion' reply … The 'subject of the illusion' objection begs
  the question against this distinction."
- **`topics/the-binding-problem` L202**: "The shared structure across all five varieties **reveals**
  that phenomenal unity is irreducible to physical coordination" — over-claims against the file's
  own L164 ("The pattern does not, on its own, discriminate"). Fix: "reveals" → "is the Map's reason
  for holding" (+4).
- Note: `concepts/quantum-indeterminacy-free-will` L162 ("The position is self-undermining") is the
  same shape in an otherwise best-in-class file (L120, L178, L156, L205, L122 are all model work).

### Notes (21 loci, recorded not flagged)

`concepts/conservation-laws-and-mental-causation` L168 grounds indistinguishability in *sensitivity
limits* where L75 insists it holds "by construction, not by any sensitivity limit" (the file's own
L97 has the correct version); same file L186 extends "minimal" into a scope dimension the tenet does
not define. `concepts/quantum-interpretations` L167 offers as a falsifier something the corridor
reading predicts by construction (+9 to scope it to the conditioned register); same file L139
recasts Tenet 4's ground as Tenet 3 incompatibility against its own correct L48.
`concepts/post-decoherence-selection` L106 uses minimality as a comparative merit ranking — well
guarded twice, so a note only. `topics/psychophysical-laws-bridging-mind-and-matter` L175 and
`topics/quantum-holism-and-phenomenal-unity` L132 both misclassify Stapp's Zeno as not requiring
pre-decoherence coherence, against L71/L77 — and the former is contradicted inside its own file at
L143/L145. `topics/completeness-in-physics-under-dualism` L124 ("the positive case for dualism from
physics itself") overshoots its own following two sentences, which deliver only compatibility.
`topics/the-convergence-argument-for-dualism` L143 ("the empirical evidence for mental causation",
unscoped) and L177 (parsimony granted tiebreaker standing, sitting uneasily with L133).
`concepts/moral-responsibility` L97/L137 read the cryptochrome result as a licence where L79 makes
it a *precedent*. `concepts/islamic-sufi-philosophy-of-consciousness` L87 imports a persisting
subject without citing background posit (1), in a file whose L99/L101/L105/L107 are model work.
`concepts/bi-aspectual-ontology` L122–123, `concepts/ai-ensoulment-hypothesis` L74,
`concepts/physics-as-disclosure` L92, `concepts/semantic-memory` L173,
`topics/the-self-minimal-narrative-and-substantial` L141/L145,
`topics/philosophical-stakes-of-spontaneous-collapse` L79 ("cleaner") and L125.

**`topics/philosophical-stakes-of-spontaneous-collapse` L39 — flagged, deliberately not tasked.**
"consciousness modulates a collapse process that would occur anyway, *operating at the smallest
possible quantum scale*" reads Tenet 2's minimality as scale (L69), where the file's own L121 gets
it right. The file took seven passes on 2026-09-18 and measures **3993 words against a 4000 hard
ceiling with the gate at `>= hard` — 6 words of headroom** — and one task is already open on it.
The fix is net-negative ("operating at the smallest possible quantum scale" (7) → "the smallest
deviation standard physics permits" (6), **−1**), so it can ride along with whatever pass next
condenses the file. **It needs a condense first if paired with anything else; do not mint against
this file.**

---

## Part 5 — Priority design

Three runs in a row, the "if only one thing" item closed inside an hour and nothing else on the
list moved. Part 3 shows the list does not become action by being minted at P3 either. This report
therefore names one lead item, mints one more at P2, extends two existing tasks in place, and
carries the rest here.

### If only one thing is done from this report

**Family J — `apex/contemplative-path` L126 and L136.** Two phrase swaps, **−1 word net**, in a file
with 658 words of headroom. L136 calls it "The honest assessment" that the evidence "eliminates
epiphenomenalism and reductive materialism decisively"; the same file's L184 and L194 already say
the plasticity evidence "does not discriminate". It is an apex page — the human-readable synthesis
tier — and `apex/` is excluded from the deep-review candidate pool, so no other lens in the system
will reach it. The correction is already written fifty lines below the error.

### Then, in order

2. **Family M — `concepts/spontaneous-collapse-theories` L112 and L115** (minted, P2). A concept
   page on collapse theories that names Stapp-Zeno as the Map's favoured mechanism and never says
   "post-decoherence". +5 words net into 642 words of headroom. Tenet *content*, not tone.
3. **Family K — the seven Tenet-5 loci** (carried). **−45 words total**; five of the seven fixes are
   deletions, and two of the files (`concepts/dualism`, `concepts/quantum-completeness`) contradict
   themselves in the same paragraph or the same sentence. The cheapest family in the report.
4. **Family B-1 — the twelve same-file contradictions** (carried). Every one has a guard sentence in
   the same file to copy from, so the fix is transcription rather than invention. **Budget is the
   binding constraint here, not difficulty**: measured this run, five of the twelve are within four
   words of their hard ceiling (`the-binding-problem` 3999 → **0**, `episodic-memory` 3498 → **1**,
   `phenomenology-of-memory-and-the-self` 3996 → **3**, `consciousness-and-memory` 3995 → **4**,
   `moral-responsibility` 3475 → 24), and the readers' suggested concessions for those run +8 to
   +19. **Do those five net-negative or not at all.** Start instead with the roomy ones and the
   net-0-or-negative fixes, which are unconstrained: `phenomenology-of-linguistic-failure`
   (2189w, 1810 to hard — and the sharpest single locus in the delta),
   `the-self-minimal-narrative-and-substantial` (3212w, −2 fix),
   `intersubjectivity` L124 (2637w, 862 to hard), `phenomenal-contrast-method` (2019w, 1480 to
   hard). Record partial completion; do not mark done on a partial sweep.

   Two cheap cross-family fixes worth folding into the same pass, both outside B-1:
   `concepts/conservation-laws-and-mental-causation` L176 ("implies" → "suggests", **net 0** — the
   file is 314 words over hard, so nothing dearer is possible) and `concepts/binding-problem` L211
   (delete a sentence the next line makes redundant, **−7**).

### Tasks touched this run

- **Minted P2** (not P3 — see Part 3): Family J (lead), Family M.
- **Extended in place**: `todo.md` L1738 gains `concepts/bi-aspectual-ontology` L141 as a third
  Family H locus; the 2026-08-26 psychophysical-laws task gains L159 (pain asymbolia) as a third
  locus, since a reader re-found its L204 cold today.
- **Not minted**: everything in Parts 2 and 4 above, and nothing at all against
  `topics/philosophical-stakes-of-spontaneous-collapse`.

### Re-carried without a task

W2a/W2b, W3, W9, W10, W11, Families C, D, F, I and N in full; Family B-1's remaining eight files and
all of B-2; Family L (all three files); the 21 notes.