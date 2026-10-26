---
ai_contribution: 100
ai_generated_date: 2026-10-26
ai_modified: 2026-10-26 11:24:35+00:00
ai_system: claude-fable-5-1
author: null
concepts:
- '[[multi-mind-collapse-problem]]'
- '[[many-worlds]]'
- '[[alexithymia]]'
created: 2026-10-26
date: &id001 2026-10-26
description: Strengths and openings in three voids pages that each treat a structural
  feature of the subject (being one, attending, having a body) as the source of territory
  it cannot map. The two pages edited in October carry the Map's calibration idiom;
  the oldest reads tenets off the void.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-26 11:24:35+00:00
modified: *id001
related_articles:
- '[[plurality-void]]'
- '[[attention-and-consciousness]]'
- '[[embodiment-cognitive-limits]]'
- '[[tacit-integration-void]]'
- '[[positions/individuation-and-subjecthood]]'
- '[[tenets]]'
title: Optimistic Review - 2026-10-26 - The subject-structure wing (plurality, attention,
  embodiment)
topics:
- '[[split-brain-consciousness]]'
- '[[philosophy-of-mind]]'
---

# Optimistic Review

**Date**: 2026-10-26 (11:04–11:30 UTC). This is a driver-briefed wing review and reports only. No article, `todo.md` line, archive file or state file was modified, and nothing was committed. The driver mints from the Priority List below.

**Content reviewed.** I read all three pages in full. Line numbers are file lines with the frontmatter included, at commit `3295fb2532` (HEAD throughout). Lengths come from `tools.curate.length.analyze_length`, which counts the body only (references included). The thresholds printed from `tools/curate/length.py` are **voids 2,000 soft / 3,000 hard** (the driver brief's "concepts 2000/3000" is wrong: concepts are 2,500/3,500; topics 3,000/4,000). The gate fires at `>=`, so headroom is hard − 1 − count.

| File | Words | Hard | Headroom | Inbound (live body) | Last deep review | Last content edit |
|---|---:|---:|---:|---:|---|---|
| `voids/plurality-void` (PV) | 1,803 | 3,000 | 1,196 | 6 | 2026-07-18 | 2026-10-07 (manyism link only) |
| `voids/attention-and-consciousness` (AC) | 2,275 | 3,000 | 724 | 13 | 2026-07-07 | 2026-10-22 (visual-indexes link) |
| `voids/embodiment-cognitive-limits` (EC) | 2,235 | 3,000 | 764 | 18 | 2026-06-25 (no-op, 4th) | 2026-09-20 (title retarget) |

I also read the passages the proposals touch or lean on: `concepts/many-worlds` L69–L75 (the branch-relative indexicality section); `positions/individuation-and-subjecthood` L97–L103 ([P-I5](/positions/individuation-and-subjecthood/#p-i5)); `tenets/tenets` L121–L123 (what the indexical objection presupposes); `concepts/multi-mind-collapse-problem` L37 and L72; `topics/split-brain-consciousness` L96, L134, L202; `voids/tacit-integration-void` L65 and its References; `concepts/alexithymia` L23/L49 (as left by yesterday's review). Prior reviews read: the Stability Notes of `deep-review-2026-07-18-plurality-void`, `deep-review-2026-07-07-attention-and-consciousness` and `deep-review-2026-06-25-embodiment-cognitive-limits`, plus `deep-review-2026-03-10-plurality-void` L28–L34/L69, `deep-review-2026-04-28-plurality-void` L40–L44 and `deep-review-2026-04-01-attention-and-consciousness` L32.

**Why these three.** Coverage was counted on review *content*, not filenames. Every line of all 617 `reviews/optimistic-*` files was tokenised and matched against 846 live non-draft pages in `topics/`, `concepts/` and `voids/` (sidecars and section index files removed). A page counted as a *target* when its slug sat in a heading, on a "Content reviewed" line or in a table row; list-item hits were counted separately because the 10-25 review found a false zero in that format. I removed every page touched in `git log --since=2026-10-24T11:00Z` (110 content files).
- Seven short slugs (`qualia`, `dualism`, `qbism`, `valence`, `kairos`, `manyism`, `empathy`) scored zero only because my tokeniser dropped slugs under eight characters. They are false zeros of my own making and were discarded unexamined.
- Among the real zeros, `phenomenology-of-recursive-self-awareness` is the known list-format false zero (10-25 review), `voids-between-minds` has 12 list hits and 6 words of headroom, `non-human-minds-as-void-explorers` has 5 list hits and 15 words of headroom, and `concepts/modal-epistemology` was created on 10-22 and deep-reviewed the same day. That leaves **PV, AC and EC**: 0 targets each, 2–3 list hits each (all incidental mentions), and the only zero-target voids pages with room to take an edit.
- **The join.** Each page argues that a structural feature of the subject generates territory the subject cannot map: being *one* (PV L31, L49), *attending* (AC L47, L53), *having a body* (EC L33, L143). Each then separates the physicalist's machinery result from the consciousness question (PV L43, AC L103/L123, EC L35/L75/L125). None of the three links either of the others (checked both directions, 0 hits in all six cells). All three share one hub, `non-human-minds-as-void-explorers`, which AC and EC link and PV does not, although PV's "What AI Might See" (L75–L81) is that page's method applied to plurality.

**Exclusions and open tasks.** None of the three pages appears in the 48-hour log; the working tree shows only `evolution-state.yaml` modified. The active section of `todo.md` (above `^## Completed Tasks$`, L3432) gives:
- **EC: one task.** The P3 at L3170 (refine-draft, `voids/embodiment-cognitive-limits`, status pending) targets L43 only (the apraxia/optic-ataxia pairing and the Merleau-Ponty ch. 3 attribution). Item 4 below touches L85, L99 and the References and does not collide; the brief should say so.
- **AC: three mentions, no task.** L1160 (a superseded fatigue-void task), L2378 and L2417 both cite AC L125 as the *model* for the "fits the tenet without evidencing it" family installed on 10-20. Item 3 touches L59 and the References only.
- **PV: no hits.**
- **Sibling pages touched by the items:** `voids/tacit-integration-void` has one active mention (L2205, a coverage list, not an edit); `topics/split-brain-consciousness` has a pending P3 at L2057 on L122/L154 (the reciprocal pipe proposed below sits at L96 or in `related_articles`, no collision).

---

## Executive Summary

The wing's strength is a shared discipline. Each page states the physicalist's best result in the physicalist's own terms (constitutive embodiment is "a physicalist achievement", EC L35; attention voids arise from "lateral inhibition, biased competition, executive gating", AC L123; the multiple-drafts deflation is given its strongest form, PV L43) and then locates the residue precisely: not the machinery but why the machinery's exclusions have phenomenal character (AC L123), whether the body constitutes *experience* as well as cognition (EC L125), and the first-person datum of being one (PV L43). AC and EC were edited in October and carry the Map's current calibration idiom ("coherence rather than support", AC L123; "fits the tenet without evidencing it", AC L125; "it does not follow", EC L125).

The wing's systematic defect is that PV's Relation section, written 2026-02-24 and untouched since, predates that idiom and reads tenets off the void: No Many Worlds "finds direct support" (L87), Bidirectional Interaction "requires a singular causal agent" (L91), singularity "may be a fundamental feature of non-physical mind" (L89). Two of those three overclaim against pages the Map wrote later: L87 is answered by PV's own dissociative-identity verdict at L67 (a split "creates multiple singularities rather than a genuine plurality", which is exactly what Everettian fission claims) and by the register ([P-I5](/positions/individuation-and-subjecthood/#p-i5): framework boundary, not in-framework refutation); L91's "that no one has articulated" is contradicted by `concepts/multi-mind-collapse-problem`. PV also inverts the role of its best source: Schechter (L39) states the inconceivability argument in order to answer it (SEP §3.1.4), and the page presents her as its author. Separately, AC L59's James sentence is from *A Pluralistic Universe* (1909), not *Principles* (1890); the 2026-04-01 deep review ratified the wrong work with a chapter number, and the same citation recurs in `tacit-integration-void` L65.

Every proposed edit fits current headroom: PV +125 (1,803 → 1,928), AC +21 (2,275 → 2,296), EC +111 (2,235 → 2,346), with the `tacit-integration-void` sibling near zero.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)
AC L123 places the gap exactly where Chalmers would: neural mechanisms "explain *how* attention creates voids", and the physicalist's routing story for "suppressed content that stays represented but unexperienced" is stated rather than hidden; what is left is "*why* there is something it is like to have content excluded from awareness. The suppressive dark has phenomenal character." The rivalry paragraph (L67) earns that sentence, because it reports the no-report evidence that keeps content in high-level representation while it is out of experience (Hesse & Tsao 2020; the 2026 preprint, labelled "unreplicated"), and concludes only that "the void's boundary is not drawn at representation".

EC L35 draws the distinction the whole page turns on, embodied *cognition* against embodied *consciousness*, and grants the first to the physicalist outright. PV L43 gives Dennett's multiple-drafts deflation its strongest form before answering it, and the answer is the right one for a property dualist: the singularity of experience "is among the most certain deliverances of introspection".

### The Quantum Mind Theorist (Stapp)
AC and PV do not enlist quantum mechanics, and Stapp would credit the restraint; AC marks Minimal Quantum Interaction as not engaged by omission, and PV's L91 is about the *structure* of the causal agent rather than any mechanism. EC L129 engages the tenet conditionally ("*If* consciousness operates through quantum processes in biological systems, embodiment provides the physical interface") and claims nothing beyond the conditional. This praise is for restraint only; no item below adds a quantum claim, and item 2(b) moves PV L91 from "requires" to "is specified for".

### The Phenomenologist (Nagel)
PV's "The Phenomenology of Trying" (L45–L53) is the wing's best writing from the inside: "Every attempt to hold two perspectives folds back into one perspective imagining another" (L49), and the finding that "we" "has no phenomenological content" when it is asked to name a plural first person (L51). AC's five phenomenological entries (L73–L81) are each a describable experience rather than a label, and "the suppressive dark" (L77) names something the neuroscience of the penumbra (L57) predicts but cannot describe. EC's Merleau-Ponty paragraph (L41) gets the "I can" before "I know" ordering right and keeps the body schema below awareness.

### The Process Philosopher (Whitehead)
AC's opening section is a process claim: "To see a figure requires producing a ground" and "Making the margin thematic creates a new margin" (L51). The void is an event-structure of attending, not a region. PV L93 ends on the possibility that "the question may be malformed in ways we cannot recognise from within singular experience", which is where `split-brain-consciousness` L166 brings Whitehead in ("How many minds?" assumes a substance metaphysics).

**Calibration note.** This persona's praise is for compatibility only. No passage in the wing uses process resonance to move anything on the five-tier evidential scale, and the wing has no minimal-organism case. The one place process-friendliness could tempt a reader into a stronger claim is PV L89 (counting), and the Hardline Empiricist takes it below.

### The Libertarian Free Will Defender (Kane)
AC L125 is the right shape for agency: "We *choose* what to attend to (at least partially). This choice produces the void", immediately qualified so that the voids "fit the tenet without evidencing it". EC L137 keeps the agency implication conditional ("*If* motor intentionality grounds agency"). Kane's own account is naturalistic, so this praise is for the structure of answerable agency only; no page enlists him and none touches the luck question.

### The Mysterian (McGinn)
Each page classifies its own void honestly. PV L33: "primarily unexplorable" with "an occluded dimension akin to mysterianism". AC L97: the lifelong-disorder case is an occluded void because the reporter has no baseline. EC L71: a *mixed* void, with the structural and contingent parts separated at L73–L77 and the sentence McGinn would want at L79: "The challenge is distinguishing which limits belong to cognition, which to consciousness, and which are contingent." PV L51 already carries the mysterian's guard for manyism ("inconceivability does not establish impossibility"); item 1 extends it to the partial-unity case that L39 currently closes.

### The Hardline Empiricist (Birch)
No minimal-organism or boundary-case claim appears in the wing, and the five-tier scale is not engaged, so this persona's verdict is about tenet-coherence versus tenet-evidence.

**Praise.** AC L123 and L125 are the installed model for the whole corpus: the 10-20 refine lowered "Every attention void is evidence of mental causation" to "fit the tenet without evidencing it", and two open tasks (todo L2378, L2417) cite that line as the pattern to copy. EC does the same move three times without the idiom (L35, L75, L125): the body's constitutive role in cognition is conceded as "a physicalist achievement" and the consciousness question is left open at L67 and L87 ("The evidence from neuroscience supports the former; the latter remains an open question"). That is "tenet-coherent, not evidence-elevating" in practice.

**Flag.** PV's Relation section does the opposite in three consecutive paragraphs. L87: No Many Worlds "finds direct support here" and the void "provides philosophical grounding for the tenet". L89: "If consciousness were straightforwardly physical ... we should be able to count instances as easily as we count physical objects", so singularity "may be a fundamental feature of non-physical mind". L91: Bidirectional Interaction "requires a singular causal agent". The first is answered by the page itself (L67) and by [P-I5](/positions/individuation-and-subjecthood/#p-i5); the second is answered by `split-brain-consciousness` L96, which says "How many minds?" may be malformed "like asking 'How many heaps'", an analogy that makes physical counting hard too; the third is answered by `multi-mind-collapse-problem`. Because the Process Philosopher's praise of L93 and this flag of L87–L91 point at the same section, the section contains possibility/probability slippage, and the yield is a `refine-draft` (item 2), not an expansion. L89 is left as a routed note below because item 2 already spends the paragraph budget on L87 and L91.

## Content Strengths

### voids/plurality-void
- **Strongest point**: the DID verdict at L67. "The plurality exists but is not experienced as plural by any single subject ... the split creates multiple singularities rather than a genuine plurality." It is the page's sharpest distinction and, once item 2 lands, the sentence that keeps the No Many Worlds paragraph honest.
- **Notable quote**: "Every attempt to think plural consciousness collapses back into a single viewpoint trying to imagine another single viewpoint. The plurality itself never arrives." (L31)
- **Why it works**: the page treats the limit as a datum about imagination and refuses Schrödinger's monist inference from it (L31), which is the restraint the rest of the wing shares.

### voids/attention-and-consciousness
- **Strongest point**: the rivalry paragraph (L67) and the two Relation paragraphs (L123, L125). The empirical claim is stated with its weakest link exposed ("two monkeys, percepts labelled by human viewers, unreplicated") and the tenet claim is stated with its physicalist twin exposed.
- **Notable quote**: "This makes the attention void among the most fundamental in the Map's framework — it concerns not content we cannot access but the *mechanism* by which we access anything." (L117)
- **Why it works**: the page's own medium-status paragraph (L119) demotes it to "medium-adjacent" and calls the cluster's count "provisional", so the superlative at L117 is immediately priced.

### voids/embodiment-cognitive-limits
- **Strongest point**: the cognition/consciousness partition (L35) carried through every section rather than announced once. The "Evidence for Genuine Limits" entries each end by saying which side of the partition the evidence reaches (L85, L87, L89).
- **Notable quote**: "The body shapes what we *think about* and *how* we think; it does not follow that the body constitutes the *experience* of thinking." (L125)
- **Why it works**: the page's weakest paragraphs (L99, L103) are the ones that forget the partition, which is why item 4 touches L99 and the Aymara point at L85 strengthens the inference rather than the conclusion.

### What the three share
Each page names a structural feature of the subject and derives a void from it; each concedes the physicalist's machinery result; none links the others. The wing is held together only through `non-human-minds-as-void-explorers`, which AC and EC link and PV does not. The Cross-Linking table closes that at zero body cost.

## Expansion Opportunities

### High Priority

None as `expand-topic`. Measured caps (`tools.evolution.state.count_section_files`, 11:05Z): topics 366/370, concepts 368/370, voids 113/125, positions 25/90. The CLAUDE.md table (voids cap 100, "1 slot left") is stale; voids has 11 slots, concepts 1, topics 3. Even so, every opening below is better served by a refine or a research note that folds, because the host pages have 700–1,200 words of headroom.

#### Partial unity of consciousness as a named option (fold into PV)
- **Builds on**: PV L39 and L59 ("Two-Streams, Switch, and Partial Unity ... remain viable"), `split-brain-consciousness` L170.
- **Would address**: the Map names partial unity as a live model in two places and never says what it is (Lockwood's co-consciousness as a non-transitive relation; Bayne's and Schechter's objections and her a priori/empirical split). Three live files mention it; none defines it.
- **Estimated scope**: a research note, then a 120–180 word paragraph in PV after item 1, where "the void keeps her datum" currently points at nothing further.
- **Tenet alignment**: Dualism via unity-of-consciousness; No Many Worlds via [P-I2](/positions/individuation-and-subjecthood/#p-i2)'s "what the indexical objection presupposes".

### Medium Priority

#### Cross-cultural time construal as a test of the embodiment inference (fold into EC)
- **Builds on**: EC L49–L53 and L85; item 4 installs the first case (Aymara).
- **Would address**: EC infers "different bodies → different concepts" and never tests the converse. Same-bodied speakers vary in the mapping (Aymara front-past; Mandarin vertical time; the Yupno uphill future), which shows the body supplies source domains without fixing mappings. Zero live files carry any of this; two research notes mention Aymara in other contexts.
- **Estimated scope**: research note; the article already has a host paragraph.
- **Tenet alignment**: Dualism, by keeping the embodiment result on the cognition side of EC's partition.

#### Gurwitsch's thematic field as the theory behind the attention void (fold into AC or tacit-integration-void)
- **Builds on**: AC L51; `tacit-integration-void` L65 (where Gurwitsch is already "the most direct ally").
- **Would address**: both pages use Gurwitsch's theme/field/margin triad as a premise ("Making the margin thematic creates a new margin") without saying why the margin obeys "different organisational principles". The 1964 text's account of relevancy-organisation would make AC's first structural argument (L109) more than an assertion.
- **Estimated scope**: research note; +100–150 words in one of the two hosts.

### Ideas for Later
- PV L89's counting argument, rewritten so it no longer assumes physical objects are easy to count (see `split-brain-consciousness` L96).
- EC's three near-identical sentences "would think differently about *everything*" (L33, L53, L73); a length-neutral consolidation if the page ever needs room.
- EC's references 8–10 (a *Journal of Cognition* URL, a Harvard Medicine magazine piece, a 2025 *HSSC* opinion piece) are cited nowhere in the body; a future refine should either cite or drop them.

## Cross-Linking Suggestions

| From | To | Reason | Cost |
|------|-----|--------|-----:|
| PV L33 "in split-brain research" | `split-brain-consciousness` | PV discusses callosotomy for a whole subsection (L57–L61) and never links the Map's 3,989-word page on it. Pipe: `in [[split-brain-consciousness\|split-brain research]]`. | 0 |
| `split-brain-consciousness` | PV | Reciprocal. The page has 10 words of headroom, so `related_articles` only, or a pipe on L96's existing "How many minds does a split-brain patient have?" | 0 |
| PV L77 "AI presents a distinctive asymmetry" | `non-human-minds-as-void-explorers` | PV's AI section is that page's "common asymmetry method" applied to plurality. Pipe: `AI presents a [[non-human-minds-as-void-explorers\|distinctive asymmetry]]`. | 0 |
| `non-human-minds-as-void-explorers` | PV | Reciprocal; 15 words of headroom, so `related_articles` only. | 0 |
| PV L91 | `multi-mind-collapse-problem` | Installed by item 2(b): PV says no one has articulated plural non-physical agency; that page is the Map's account. | in item 2 |
| `multi-mind-collapse-problem` L72 "bounded by its embodiment" | EC and PV | Pipe `bounded by its [[embodiment-cognitive-limits\|embodiment]]` (0) and add PV to `related_articles`; 594 words of headroom allow an optional sentence that locality is specified per body, not per subject. | 0–20 |
| EC L99 | `alexithymia` | Installed by item 4(b); `alexithymia` (2,056 words) should add EC to `related_articles` in return. | in item 4 |
| EC L143 and AC L117 | each other | Both say the instrument of access is what cannot be inspected ("The body structures thought in ways thought cannot represent"; "the *mechanism* by which we access anything"). `related_articles` both ways, plus one Further Reading line each. | +15 each |

Every target was collision-checked: each slug resolves to exactly one live file (`many-worlds` also has an `archive/arguments/` copy, so the body link should stay as the existing heading-anchored form `[[many-worlds#MWI's Branch-Relative Indexicality Reply|...]]`, which EC L133 already uses and which resolves).

## New Concept Pages Needed

- **partial-unity-of-consciousness**: deserves a page in principle (three live mentions, no definition anywhere), but concepts has one slot by the gating count and PV has 1,071 words of headroom after item 1. Recommend a `research-topic` whose expected action is *fold* into PV, not an `expand-topic`.

---

## Priority List (for the driver to mint)

Each item gives exact OLD → NEW text and its word cost by `analyze_length`. I applied every edit to scratch copies (`…/scratchpad/simF/obsidian/voids/`) and re-measured after each one. Every OLD string has `str.count == 1` in the live file at `3295fb2532`. The sibling sweep covered live `topics/`, `concepts/`, `voids/`, `apex/`, `positions/`, `tenets/`, plus `archive/` and `hugo/content`; the only live siblings found are named inside the items.

**Shared guards for every brief:**
- Never concede epiphenomenalism; keep the Tenet 3 quantifier ([P-Q2](/positions/quantum-interface/#p-q2)) unresolved.
- Do not enlist Schechter, Wallace or Saunders for dualism; keep "argues" (not "concedes") for Wallace, per the 03-10 review.
- Keep PV's manyism paragraph (L51) as it is; item 1 points at it.
- Use Tenet 5 only on the Map's own reasoning.
- Avoid "This is not X. It is Y." and "load-bearing".
- Set `ai_modified` from `date -u`; append the model to `ai_system` only if it is absent anywhere in the string.
- Write the changelog before syncing, verify both trees (obsidian and `hugo/content`), and do not commit from the fork.
- File fields: `obsidian/voids/plurality-void.md`, `obsidian/voids/attention-and-consciousness.md`, `obsidian/voids/embodiment-cognitive-limits.md`, `obsidian/voids/tacit-integration-void.md`.

### 1. PV L39: give Schechter her own position (+48; 1,803 → 1,851)

**File**: `obsidian/voids/plurality-void.md`.

**Basis.** SEP "The Unity of Consciousness" §3.1.4 (fetched 11:12Z) introduces the quoted sentence as the strong form of the inconceivability argument *against* partial unity, cited to Schechter 2014, and then reports her reply: "As Schechter (2014) points out, it is not easy to see why this argument would not equally target the dual-stream account", and "it is unacceptable, Schechter argues, to reject all contenders but the single stream view on purely a priori grounds." Her 2014 chapter is titled "A Preliminary Defense". She rejects partial unity for split-brain patients on *empirical* grounds (same section), so she is neither the argument's author nor a partial-unity believer; she is the person who says the argument does not settle anything a priori. PV L39 ("sharpened the point") presents her as the argument's author. The 04-28 review "verified against SEP", which ratified the words but not the role.

**Quote fidelity.** SEP's rendering begins "there is nothing"; PV has "There exists nothing". I could not reach the MIT Press chapter. The NEW text uses SEP's rendering; the brief should check the chapter (Bennett & Hill eds., 2014; Google Books search-within-volume) and keep whichever wording the chapter has, or paraphrase without quotation marks if neither can be confirmed. The framing fix does not depend on which two words open the sentence.

```text
OLD: Elizabeth Schechter sharpened the point: "There exists nothing that would even count as successfully imagining what it is like to have a partially unified consciousness." We cannot even begin to construct the phenomenological template. We have no experiential model for partial sharing, partial merger, or partial overlap between conscious perspectives. The imagination simply stalls.
NEW: Elizabeth Schechter states the strongest form of the point, that "there is nothing that would even count as successfully imagining what it is like to have a partially unified consciousness", and then declines its conclusion: the same argument would rule out the two-streams account of split-brain patients, and no contender can be rejected on a priori grounds alone. The void keeps her datum. We cannot even begin to construct the phenomenological template. We have no experiential model for partial sharing, partial merger, or partial overlap between conscious perspectives. The imagination simply stalls, and, as with manyism below, inconceivability does not establish impossibility.
```
"As with manyism below" points at L51, which already says "inconceivability does not establish impossibility"; the two sentences should stay in agreement if either is later edited. The research note [research/voids-plurality-void-2026-02-24.md](/research/voids-plurality-void-2026-02-24/) carries the old rendering; research notes are left alone.

### 2. PV L87 and L91: bring the Relation section up to the register (+77; 1,851 → 1,928)

**File**: `obsidian/voids/plurality-void.md`. Two edits, one task.

**Basis for 2(a).** L87 says No Many Worlds "finds direct support here" because the interpretation "requires consciousness to branch" and "the branching of consciousness is incoherent from the inside". The page's own L67 says a split "creates multiple singularities rather than a genuine plurality"; Everettian fission claims exactly that (`concepts/many-worlds` L71: "Singularity is preserved branch-locally"). So the void does not reach branching as such. What the Map's objection actually is, the tenets page states at L121 ("meaningful only on a *non-deflationary* conception of personal identity—an 'I' whose branch-assignment is a real further fact") and the register fixes its reach at [P-I5](/positions/individuation-and-subjecthood/#p-i5) ("a framework boundary, not an in-framework refutation"). L87's rendering of Wallace ("the notion of 'I' can make sense only if consciousness is confined to a single branch") is also a garble of branch-relative indexicality, which is a *rescue* of branching, not a constraint on it; the 03-10 and 04-28 reviews fixed the verb and kept the garble. The NEW text uses the heading-anchored link EC L133 already uses, and the plain token "[P-I5](/positions/individuation-and-subjecthood/#p-i5)", which autolinks.

```text
OLD: **[[tenets#^no-many-worlds|No Many Worlds]]** finds direct support here. The Map rejects the many-worlds interpretation partly because it requires consciousness to branch with the wave function. David Wallace argues that the notion of "I" can make sense only if consciousness is confined to a single branch. If consciousness is constitutively singular, any interpretation of physics that requires it to split makes a demand consciousness cannot meet. The plurality void provides philosophical grounding for the tenet: we reject many worlds partly because the branching of consciousness is incoherent from the inside.
NEW: **[[tenets#^no-many-worlds|No Many Worlds]]** is engaged here, with a narrower reach than a first reading suggests. The Map's objection to the many-worlds interpretation is indexical: if every branch is equally real, why am I *this* one? The Everettian answer is [[many-worlds#MWI's Branch-Relative Indexicality Reply|branch-relative indexicality]] (Saunders, Wallace): branching is fission, and each successor truly says "I" of its own branch. The plurality void does not refute that answer, because branching so described yields multiple singularities rather than a plural subject, the verdict this page reaches for dissociative identity above. What the void supplies is the precondition the [[tenets|tenets page]] states for the indexical objection, a non-deflationary "I": the singularity of experience is the first-person datum that "I" rests on. The register records the upshot as a framework boundary rather than an in-framework refutation (P-I5).
```
(+45.) Saunders 2010 and Wallace 2012 are already in the Map's reference apparatus (`concepts/many-worlds`, `topics/qm-interpretations-beyond-many-worlds`); PV's References need no new entry for this paragraph, though adding Wallace 2012 is in scope if the driver prefers every named author listed.

**Basis for 2(b).** L91 says plural causal agency is "a theory ... that no one has articulated". `concepts/multi-mind-collapse-problem` is that theory for the many-bodies case: "each consciousness interfaces only with its own brain. Selections are local, not global" (L37); "consciousness's causal reach is bounded by its embodiment. Alice's consciousness selects among Alice's neural patterns; Bob's selects among Bob's" (L72). It says nothing about two subjects in one brain or one experience in several subjects (0 hits for split, dissociative, one brain, same brain), which is where PV's void actually bites. Neither page links the other.

```text
OLD: **[[tenets#^bidirectional-interaction|Bidirectional Interaction]]** requires a singular causal agent. If consciousness influences quantum outcomes in the brain, the mechanism must be channelled through something that acts as *one*. Plural consciousness would require a theory of plural causal agency—multiple non-physical influences coordinating at the quantum level—that no one has articulated.
NEW: **[[tenets#^bidirectional-interaction|Bidirectional Interaction]]** is specified for a singular agent. If consciousness influences quantum outcomes in the brain, the Map's mechanism channels that influence through something that acts as *one*, and its answer to the many-minds question, the [[multi-mind-collapse-problem|interface-locality account]], bounds each subject's reach by its own brain. That account handles many singular subjects in many bodies; it has no story for two subjects in one brain, or for one experience shared across subjects, which is where the void would bite.
```
(+32.) Secondary, zero body cost: add `[[plurality-void]]` to `related_articles` of `concepts/multi-mind-collapse-problem` (2,905 words; a one-sentence pointer at L72 is optional and affordable).

**Also in this task, zero cost:** the two pipes from the Cross-Linking table, `in [[split-brain-consciousness|split-brain research]]` at L33 and `AI presents a [[non-human-minds-as-void-explorers|distinctive asymmetry]]` at L77 (both measured ±0), and the matching `related_articles` entries. Reciprocals in `split-brain-consciousness` (10 words of headroom) and `non-human-minds-as-void-explorers` (15) go in `related_articles` only.

### 3. AC L59 and `tacit-integration-void` L65: cite the James sentence to the work it comes from (+21; 2,275 → 2,296; sibling ≈ ±0)

**Files**: `obsidian/voids/attention-and-consciousness.md`; `obsidian/voids/tacit-integration-void.md`.

**Basis.** The sentence "My present field of consciousness is a centre surrounded by a fringe that shades insensibly into a subconscious more" is in *A Pluralistic Universe* (1909), Lecture VII, "The Continuity of Experience" (Project Gutenberg #11984, plain text, lines 4920–4921, read 11:14Z). Both volumes of *The Principles of Psychology* (Gutenberg #57628, #57634) have 0 hits for "shades insensibly" and 0 for "surrounded by a fringe"; the *Principles* introduces the fringe (45 hits in vol. 1) but never with this sentence. AC L59 quotes it with ref 6 = James 1890; `tacit-integration-void` L65 quotes it as "(James, 1890)" with ref 7 = James 1890. The 2026-04-01 deep review (L32) asserted it is "from Chapter IX, 'The Stream of Thought,' in *Principles of Psychology*" and deferred the fix as minor; that assertion was wrong and should not be carried forward as a verification. The archived `archive/voids/attention-created-voids.md` carries the same citation and is left alone (archive pages are frozen behind their notice).

AC, two edits:
```text
OLD: William James identified a complementary structure: the fringes of consciousness. Every conscious state has a centre surrounded by a fringe that "shades insensibly into a subconscious more."
NEW: William James identified a complementary structure: the fringes of consciousness, introduced in the *Principles* and restated in 1909: "My present field of consciousness is a centre surrounded by a fringe that shades insensibly into a subconscious more."
```
```text
OLD: 6. James, W. (1890). *The Principles of Psychology*. Henry Holt and Company.
NEW: 6. James, W. (1890). *The Principles of Psychology*. Henry Holt and Company.
7. James, W. (1909). *A Pluralistic Universe*. Longmans, Green. Lecture VII.
```
AC's References are numbered 1–10 in citation order, so inserting "7." requires renumbering 7–10 to 8–11 (four lines; nothing in the body cites by number, 0 hits for `[7]`-style tokens). If the driver prefers no renumbering, append it as 11.

`tacit-integration-void`, one or two edits:
```text
OLD: "shades insensibly into a subconscious more" (James, 1890)
NEW: "shades insensibly into a subconscious more" (James, 1909)
```
Its References are alphabetical with James 1890 at ref 7 (file L142). L65 is the only citation of a specific James work in that body (the other mention, "James, Gurwitsch, and Polanyi all grant first-person phenomenology...", names no work), so replace ref 7 outright with `7. James, W. (1909). *A Pluralistic Universe*. Longmans, Green.`; no renumbering. (The page is at 2,250 words; the edit costs about +2.)

### 4. EC L85 and L99: test the embodiment inference in both directions, and hand the Jamesian claim to its test page (+111; 2,235 → 2,346)

**File**: `obsidian/voids/embodiment-cognitive-limits.md`. Does not touch L43 (open P3 at todo L3170); say so in the brief.

**Basis for 4(a).** L85 infers "different bodies produce different abstract concepts" from conceptual-metaphor research and never asks whether the same body fixes the concept. Núñez & Sweetser 2006 (*Cognitive Science* 30(3): 401–450, doi 10.1207/s15516709cog0000_62; Crossref metadata confirmed 11:16Z) show Aymara speakers mapping the known past to the space in front and the unknown future behind, in both speech and co-speech gesture, reversing the front-future mapping of most studied languages. Same body, different mapping: the body supplies source domains and underdetermines the mapping. This strengthens the page's partition (the result is firmly on the cognition side) while weakening its one-directional inference, which is what a calibration edit should do. Zero live files currently carry this.

```text
OLD: **Conceptual metaphor is embodiment-specific.** Research on conceptual metaphor (Lakoff & Johnson 1980, 1999) shows humans use spatial metaphors for time and force metaphors for causation across cultures. But *specific* metaphors depend on embodiment—different bodies produce different abstract concepts. This constrains the cognitive tools available, though it does not settle whether consciousness itself is similarly constrained.
NEW: **Conceptual metaphor is embodiment-specific, but the body underdetermines the mapping.** Research on conceptual metaphor (Lakoff & Johnson 1980, 1999) shows humans use spatial metaphors for time and force metaphors for causation across cultures. The mappings vary among identically embodied speakers: Aymara speakers place the known past in front and the unknown future behind, in language and in gesture (Núñez & Sweetser 2006), reversing the mapping most languages share. So the inference from a different body to different abstract concepts runs one way: a different body would change the source domains, but a shared body does not fix the mapping. This constrains the cognitive tools available, though it does not settle whether consciousness itself is similarly constrained.
```
(+61.) Reference, appended after ref 13 (+33):
```text
OLD: 13. Seth, A. K. (2013). "Interoceptive Inference, Emotion, and the Embodied Self." *Trends in Cognitive Sciences*, 17(11), 565-573.
NEW: 13. Seth, A. K. (2013). "Interoceptive Inference, Emotion, and the Embodied Self." *Trends in Cognitive Sciences*, 17(11), 565-573.
14. Núñez, R. E., & Sweetser, E. (2006). "With the Future Behind Them: Convergent Evidence From Aymara Language and Gesture in the Crosslinguistic Comparison of Spatial Construals of Time." *Cognitive Science*, 30(3), 401-450. https://doi.org/10.1207/s15516709cog0000_62
```
The brief should re-verify the abstract's front/back claim at the publisher before installing; I verified the metadata only.

**Basis for 4(b).** L99 asserts the Jamesian ordering flat ("Emotions arrive as bodily sensations before cognitive labeling"), which the Map's `alexithymia` page treats as the open question (its L57: whether the felt affect is present and unreachable or partly absent is "genuinely open"; yesterday's review kept it open). The page should own the reading and link the test case.

```text
OLD: **Emotional processing:** Emotions arrive as bodily sensations before cognitive labeling.
NEW: **Emotional processing:** On the Jamesian reading, emotions arrive as bodily sensations before cognitive labelling; [[alexithymia]] is the Map's test of whether the felt state precedes its label.
```
(+17.) Secondary, zero body cost: add `[[embodiment-cognitive-limits]]` to `related_articles` of `concepts/alexithymia`.

---

## Defects routed (not in the Priority List)

- **PV L89 counting inference.** "If consciousness were straightforwardly physical ... we should be able to count instances as easily as we count physical objects" assumes physical counting is easy; `split-brain-consciousness` L96 uses heaps to argue the opposite. A later refine of PV should soften L89 to the register's framing ([P-I1](/positions/individuation-and-subjecthood/#p-i1) holds closed individualism as framework-internal, Grade D) rather than offer counting as evidence for non-physicality. Not minted here because item 2 already rewrites the two neighbouring paragraphs and the brief should stay reviewable.
- **Review-process note.** `deep-review-2026-04-01-attention-and-consciousness` L32 asserted a chapter of the wrong book for the James sentence. The driver should not treat prior "verified" notes on that sentence as settled; item 3 carries the primary-text evidence.
- **EC references 8–10** are uncited in the body (0 hits for `joc.116`, `Harvard`, `s41599`, and also 0 for `Harnad` and `Varela`, whose entries at 5 and 7 are likewise uncited). A future EC refine should cite or drop them; not length-relevant now.

## Uncovered subjects (for the harvester)

1. **Partial unity of consciousness** (Lockwood 1989; Bayne 2010; Schechter 2014): named as a live model in `plurality-void` L59, `split-brain-consciousness` L170 and `binding-problem` L132, defined nowhere. Three research notes mention the phrase in passing (02-10, 02-15, 02-24); no note is about it. Expected action: article-or-fold, with fold into PV the likely verdict given caps.
2. **Cross-cultural spatial construals of time** (Núñez & Sweetser 2006; Boroditsky 2001; Núñez, Cooperrider et al. 2012 on Yupno): 0 live files; 2 research notes mention Aymara in unrelated contexts. Expected action: fold into EC after item 4.
3. **Gurwitsch's relevancy-organised thematic field** as the theory behind "making the margin thematic creates a new margin": 2 live files use it as a premise (AC L51, tacit-integration-void L65), 2 research notes mention him. Expected action: fold into whichever of the two hosts has more headroom at the time (AC 724, tacit 749 today).

## Method notes

- Coverage scan: `…/scratchpad/coverage.py` (set-membership tokeniser; the first regex version did not finish in 120 s and was abandoned). 846 pages × 617 reviews in about one second.
- Sources read from raw text: SEP "The Unity of Consciousness" (first 100,000 characters; the bibliography was beyond the read window); Project Gutenberg #11984, #57628, #57634 (plain text, grep); Crossref for Núñez & Sweetser 2006. I did not reach Schechter 2014 or Coleman 2014 themselves; Coleman, James 1890, Sperry, de Haan and Goff were verified at the publisher of record by the 2026-06-04 audit and are not re-litigated here.
- No file other than this review was written.