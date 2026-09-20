---
ai_contribution: 100
ai_generated_date: 2026-09-20
ai_modified: 2026-09-20 07:55:58+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-20
date: &id001 2026-09-20
description: 'Optimistic review of the cross-modal capability-division wing, anchored
  on the positions register entry P-PI1: a genuinely well-built two-tier finding whose
  register entry is body-cited by exactly one of the eleven articles it governs.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-09-20 07:55:58+00:00
modified: *id001
related_articles: []
title: Optimistic Review - 2026-09-20 - Cross-Modal Capability-Division Wing
topics: []
---

# Optimistic Review — The Cross-Modal Capability-Division Wing

**Date**: 2026-09-20
**Anchor**: `obsidian/positions/perception-and-the-interface.md` ([P-PI1](/positions/perception-and-the-interface/#p-pi1))

## Articles Reviewed, With Measured Sizes

All four measured this run with `tools.curate.length.analyze_length`. Thresholds **printed, not quoted**. Headroom is computed as `hard − 1 − count`, because `tools/curate/length.py:112` gates on `word_count >= hard` — the hard number itself trips the warning.

| Article | Words | Soft / Hard | Status | Headroom |
|---|---|---|---|---|
| `positions/perception-and-the-interface` (anchor) | 1438 | 1500 / 2500 | `ok` | **1061** |
| `apex/cross-modal-capability-division` | 5005 | 4000 / 5000 | **`hard_warning`** | **−6** |
| `topics/vestibular-consciousness-and-the-interface` | 3023 | 3000 / 4000 | `soft_warning` | 976 |
| `topics/thermal-consciousness-and-the-interface` | 3218 | 3000 / 4000 | `soft_warning` | 781 |

Context for the rest of the wing, measured in the same pass: `concepts/capability-division-in-vision` 2969 (`soft_warning`, headroom 530), `topics/auditory` 3098 (`soft_warning`, 901), `topics/chemosensory` 2682 (`ok`, 1317), `topics/tactile` 3049 (`soft_warning`, 950), `topics/interoceptive` 3807 (`soft_warning`, 192), `topics/dual-domain-proprioception` 2259 (`ok`, 1740), `topics/dualist-perception` 3815 (`soft_warning`, 184), `apex/embodied-interface` 3884 (`ok`, 1115).

**Sizing governs everything below.** The apex is past its hard gate; the anchor and the two spokes reviewed have room. No opportunity named in this review asks the apex for a single net word.

## Selection: Two Brief Premises, One Confirmed and One Corrected

**(a) Confirmed, and stronger than stated.** I re-ran the coverage scan corpus-wide: 559 optimistic reviews against all 832 live files in `topics/`, `concepts/`, `voids/`, `positions/`, `apex/`, `arguments/`. **Exactly two files have never been named in any optimistic review**, and both are in `positions/`: `positions/perception-and-the-interface` and `positions/value-in-selection-calibration-history-p-vs2`. The brief's claim was precise.

**(b) Corrected — the three spokes the brief nominated were all reviewed two days ago.** The brief proposed taking `concepts/capability-division-in-vision`, `topics/auditory-consciousness-and-the-interface` and `topics/chemosensory-consciousness-and-the-interface` as the three spokes. All three are among the five articles reviewed in [reviews/optimistic-2026-09-18-modality-interface-wing.md](/reviews/optimistic-2026-09-18-modality-interface-wing/), and the 09-18 findings on two of them have *already been executed* — `todo.md` L2356 and L2366 are both `✓ 2026-09-19`, and `capability-division-in-vision` has gone 1976 → **2969** words in the interval, which is the calibration-spine-and-falsifiability fix landing. Re-reviewing them would have been a re-praise of work in flight.

I substituted the two scope-condition spokes the anchor's own `Asserts` field turns on and the 09-18 pass did not touch: **vestibular** (the extreme; 5 prior optimistic mentions) and **thermal** (the gradient; 2 — the least-reviewed article in the wing after the anchor). I did not take **interoceptive** (the inversion), which has 9 prior optimistic mentions, the most of the three.

## What `modality-interface-wing` (2026-09-18) Already Owns

Named so this review does not re-praise it:

- The wing's **shared calibration spine** — the `accommodation, not (a) proof` / `settles dualism` family, measured at 7 of 8 members, with the two spelling variants counted separately to avoid a false zero. Owned; not re-argued here.
- The **auditory spoke's underbuilt state** (no dissociation case, half its siblings' length). Owned and **fixed** — auditory is now 3098 words, up from 1798.
- The **vision spoke's missing calibration spine and falsifiability section**. Owned and fixed.
- The **`three-dimensional-world-representation-problem` near-orphan** (linked by 1 of 8, linking back to 1) and its §"What Would Challenge This View?" as the corpus's best falsifiability writing. Owned. Note that article also drew a `deep-review` today.
- The **absence of a `visual-consciousness-and-the-interface` gap** — cleared as principled on 09-18. Not re-opened.

This review's ground is the **register tier**, which 09-18 did not look at: the wing had no position file at all before 2026-09-14.

## Lenses Run, Named

So an unrun lens is visible rather than implied clean.

1. **Corpus-wide coverage scan** — 559 optimistic reviews × 832 live files, content-matched on stem, not filename (per `review-coverage-must-be-measured-on-content-not-filenames`).
2. **Length/sizing** — `analyze_length` on 12 wing members; thresholds printed; headroom computed against the `>= hard` gate.
3. **Register-citation lens** — every inbound body reference to the anchor across the whole `obsidian/` tree, `reviews/` and `workflow/` excluded.
4. **Body-only cross-link matrix** — frontmatter stripped, and the `## Further Reading` / `## Source Articles` nav blocks scored separately from prose, because frontmatter membership is not a link and a nav-list entry is not a prose link.
5. **Tier-debt inheritance lens** — for each spoke, does it carry the debts the apex attaches *to that spoke specifically*: the common-cause null, the named GNW rival, the consonant-not-probative discount. This is the "ask what it omits, not only whether what it says is right" lens.
6. **Open-task ownership** — `todo.md` grepped by path, every hit resolved to its enclosing `### ` header and status, because 46% of path hits sit under a `✓`.
7. **Sibling-pass check** — all `reviews/*2026-09-19*` and `*2026-09-20*` files grepped for the three wing paths before any cross-article finding was written.
8. **Seven persona lenses**, below.

**Not run, and therefore not clean:** quote fidelity against publishers (no web access used this run — the apex's 23 references and the Sanchez 2020 verbatim were *not* re-verified at source); literature currency; the anchoring audit; `hugo/content/` parity. The apex was last deep-reviewed 2026-07-19, two months ago.

## The Body-Only Cross-Link Matrix

Rows link to columns. **P** = prose only · **N** = nav-section only (`Further Reading` / `Source Articles`) · **B** = both · **–** = no link. Frontmatter `topics:` / `concepts:` / `related_articles:` membership is excluded throughout; it renders only through machine-meta and counting it overstates integration.

```
                              P-PI1 apex  vis  aud  chem tact prop  int  vest therm door emb
P-PI1 (anchor)                  ·    P    P    P    P    P    P    P    P    P    P    P
apex                            P    ·    B    B    B    B    B    B    B    B    –    P
vision                          –    B    ·    P    P    P    N    P    P    P    N    –
auditory                        –    N    B    ·    B    B    –    –    –    –    B    –
chemosensory                    –    N    –    B    ·    N    –    B    –    B    B    –
tactile                         –    N    –    B    B    ·    B    P    B    B    B    –
proprioception                  –    N    N    –    –    N    ·    –    –    –    –    –
interoceptive                   –    B    P    –    –    B    N    ·    N    N    –    –
vestibular                      –    B    –    –    –    B    B    B    ·    N    N    N
thermal                         –    B    –    P    –    B    –    B    B    ·    N    N
dualist-perception (front door) –    P    N    P    P    P    P    P    P    P    ·    –
embodied-interface (apex)       –    P    –    –    –    B    N    B    B    B    –    ·
```

Two columns and one row are the findings.

**Column 1 (the anchor): one `P`, ten dashes.** Of the eleven articles the register entry governs, exactly **one** — the apex — links it in body prose. See Priority 1.

**Row `proprioception`: zero `P`s.** It makes three outbound wing links and all three are nav-section entries. Its prose cites no sibling in the wing at all, while five wing members cite it. See Priority 3.

**Row `apex` is the wing's spine and it is complete** — the apex prose-links all ten other members bar the front door, and nav-links all eight spokes. That is not the norm in this corpus and it deserves saying.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)

The anchor's `Would shift if` field is the best piece of writing in the wing and among the best in the corpus. It is not a gesture at falsifiability; it names four distinct retirement conditions, states for each whether it triggers *retirement* or *rewrite*, and then — the rare move — names the evidence that looks like it should count and explains why it does not: "cross-modal recruitment of cortical territory does not, whether primary visual cortex engaged by Braille reading in blind subjects (Sadato et al. 1996), task-organised 'metamodal' cortex (Pascual-Leone & Hamilton 2001)… since what is shared there is tissue recruited downstream of modality-specific transduction, not the extraction code." A falsifier that pre-empts its own most tempting false positive is a falsifier someone actually tried to break.

### The Quantum Mind Theorist (Stapp)

Nothing to work with, and that is the right result. Across the anchor, the apex and both spokes, Tenet 2 appears only as a disclaimer — "no cross-modal datum establishes the quantum-interface mechanism; the dependence runs from the framework to the reading of the data, not the reverse" (apex), and the near-identical sentence in vestibular §Relation to Site Perspective. The wing spends no quantum credit on a domain that does not need it.

### The Phenomenologist (Nagel)

The vestibular spoke does something Nagel would recognise as a genuine move rather than a restatement: it changes the *form* of the gap question. "For colour or pain the gap is 'why is this physical state accompanied by *this* quale rather than another.' The vestibular sense has scarcely any quale to attach the question to—and that is what makes the residue interesting. The question it leaves is: why is there a felt first-person perspective, oriented within a spatial frame, at all?" Choosing the modality with the *least* phenomenology to press the phenomenological question is an inversion of the usual strategy, and the article knows why it works: it "strips away the distracting richness of a proprietary quale."

### The Process Philosopher (Whitehead)

The thermal spoke's central claim — that felt value is not a verdict laid over a neutral percept but is what is felt — is as close to a process reading as the wing comes: "the value cannot be a downstream verdict on a neutral percept, because there is no fixed neutral percept to judge; the phenomenology suggests that what is felt *is* the comfort or distress." And the gradient move (extero/intero as "a partition of *roles a single modality can play* rather than of modalities") replaces a substance-like sorting with a functional one.

**Per this skill's evidential-status constraint, none of that is offered as warrant for any tier-upgrade.** The thermal spoke itself refuses the upgrade in the same section — see Birch below, whose verdict is load-bearing here.

### The Libertarian Free Will Defender (Kane)

Thin and honestly thin. Tenet 3 enters both spokes as *perceptual* participation (vestibular self-motion estimated with motor commands; anticipatory thermoregulation), and each time the article immediately concedes the redescription: "The alignment is interpretive, not probative: the active-inference theorist re-describes the very same motor-prediction in wholly physical terms, and the Map's commitment to bidirectional interaction rests on its broader interaction framework, not on the vestibular case alone." The second clause is the good part — it names where the commitment actually rests, so the reader cannot mistake the spoke for its support.

### The Mysterian (McGinn)

The vestibular spoke refuses to settle a dispute it could easily have settled in its own favour. On whether the sense has a faint phenomenology or none: "The Map does not need to adjudicate this to make its point." And on the depersonalization data, it names two readings — the spatial frame as a *condition* of experience versus a *component* of the subject — and then declines: "The evidence does not adjudicate it… The Map holds this open at the framework boundary." The stronger reading would have served the Map better. It is not taken.

### The Hardline Empiricist (Birch)

**Load-bearing, and the verdict is favourable at the register tier and mixed at the spoke tier.**

The anchor is the corpus's cleanest instance of tier discipline, and it is discipline the Map paid for. [P-PI1](/positions/perception-and-the-interface/#p-pi1) does not state one credence; it states two, with the split reasoned: "credence moderate (high for the architecture tier, whose negative half is textbook sensory neuroanatomy… low for the significance-tier reading, which is the Map's wager and conditional on the interface reading assumed elsewhere)." It does the same for evidence grade — **B** for the architecture tier and **D** for the significance tier *in the same field* — and states the reason the architecture tier is not A: "its positive half rests on one MEG cross-decoding study, Sanchez et al. 2020, so the tier is B rather than A." Grading your own best evidence down because it is a single study is the behaviour this persona exists to praise.

**The tenet-as-evidence-upgrade that is praise-worthily not done.** The wing had the structural opportunity and declined it twice. The apex: the supramodal signature "is a *shared explanandum* that does not discriminate between the theories, not a confirmation of the interface. The Map must out-accommodate the workspace, not enlist Sanchez against it." The anchor goes further and names the forbidden move by its rule: "citing the wing's convergence as support for Tenet 1 is the pattern [P-F1](/positions/finding-level-calibration/#p-f1) forbids." An eight-article convergence is exactly the shape that invites a tier-upgrade, and the register entry exists in part to forbid it.

**The common-cause cap is the strongest single piece of discipline here**, because it is applied *hardest to the wing's own best material*. The apex does not merely concede the cap; it identifies which of its own cases it bites worst: the vestibular case "is the survey's most thoroughly shared-upstream datum: not a seventh converging line but a deeper sounding of the architecture the other lines already tap, extending what the asymmetry *means* without adding to how strongly it is confirmed." That distinction — meaning-extension versus confirmation-addition — is precise and it is the right distinction.

**Where the discipline does not reach: the spokes.** Measured across all eight spokes, the strings `common-cause-null` and the bare phrase `common cause` (checked separately, both case-insensitive and fixed-string) appear in **one** spoke, interoceptive, at L99. `Global Neuronal Workspace` / `Dehaene` / `broadcast` appear in **zero** spokes. The phrase `supramodal` appears once each in six spokes and in **every one of those six it is inside a `Further Reading` line describing the apex**, never in prose. So the significance-tier discount that the anchor and apex state in named, rival-specific terms is carried into the spokes only in its generic form ("accommodation, not a proof"). Priority 2 is the sharpest instance.

## Content Strengths

### `positions/perception-and-the-interface`

- **Strongest point**: the two-tier statement is executed in every field, not just the headline. Credence, evidence grade, discriminability and framework-internality are each split and each split *differently* — which is what makes it a real two-tier entry rather than a two-tier sentence with one-tier metadata.
- **Notable quote**: "Nothing in the architecture tier's robustness transfers to the reading."
- **Why it works**: that is the whole discipline in nine words, and it is stated as a prohibition on the Map rather than as a hedge against a critic.
- **Second strength**: the `About this domain` section argues for the entry's *placement* — why [P-PI1](/positions/perception-and-the-interface/#p-pi1) lives here rather than in `finding-level-calibration` — on a principled distinction (normative conduct rules with axes legitimately n/a, versus a first-order claim with graded axes). Register files rarely justify their own filing.

### `apex/cross-modal-capability-division`

- **Strongest point**: it treats its own scope condition as the finding rather than as damage. "The inversion does not weaken the finding; it locates its scope, and the scope is the discovery."
- **Notable quote**: "The recurrence claim was never universal, and saying so precisely is stronger than asserting it everywhere."
- **Why it works**: the structural claim survived contact with a case that inverted both its terms, and the article's response was to narrow the claim rather than absorb the case. The §"Where the Division Does Not Cleanly Recur" section then lists four disanalogies, two of which (double dissociability of binding and awareness; window-bounded unconscious integration) cut against the Map's own reading, and the article says so: "some of the organising assigned to the brain side is consciousness-involving."
- **Also**: the ownership concession is the most candid sentence in the wing — "The ownership claim is a place the workspace looks incomplete, not a place the Map has independent evidence the workspace lacks."

### `topics/vestibular-consciousness-and-the-interface`

- **Strongest point**: the "two axes" argument, which converts an existing hedge into a structure. "Smell is faint-object and faint-frame; vestibular is faint-object yet foundational-frame. So the mind-side term is not a single scale from smell to touch but a family of distinct contributions." The apex adopts this verbatim and [P-PI1](/positions/perception-and-the-interface/#p-pi1) registers it as "object-unity, owned affect, viewpoint-frame". A spoke that upgraded the register's vocabulary is the wing working as designed.
- **Notable quote**: "a sense whose contribution is so thoroughly a *frame* for the other senses that it has no place where it is processed *as itself*."
- **Why it works**: the anatomical fact (no unisensory vestibular cortex) and the phenomenological fact (paucity of vestibular experience) are shown to be the same fact seen from two sides, rather than two facts stacked.

### `topics/thermal-consciousness-and-the-interface`

- **Strongest point**: it declares which of its claims is the Map's own inference and which its sources support. On the gradient reading: "The gradient reading—exteroception and interoception as ends of a spectrum, thermoception on the line—is the *Map's* inference, asserted by neither source." It then argues *against both its own authorities* (Craig moves the modality inward; Crucianelli & Ehrsson keep two separable components) and gives the reason: "each reclassification saves the dichotomy by assigning a dual-role signal wholly to one side, while the duality is the datum."
- **Notable quote**: "Said plainly, the construction is by a fully specified physical mechanism with a confirmed quantitative prediction—exactly what the mechanism-sufficiency rival expects, no tilt toward the interface."
- **Why it works**: the thermal grill is the wing's most dramatic illusion and the most tempting to over-read. The article writes the anti-over-reading sentence *in the same paragraph as the illusion*, not in a distant caveats section.
- **Also**: §Rivals engages three physicalist accounts and notes they **disagree with each other** — Barrett & Simmons "expressly reject reading interoception as comparison against homeostatic set-points… so the allostatic programme *competes with* the set-point framing this article takes from Cabanac and Craig." Noticing that your rivals are not one rival is rare.

## Priority List — Capped at Four

Ranked. Everything below the cap is in §Secondary Record and is a record, not a plan.

### 1. The register entry is body-cited by 1 of the 11 articles it governs — and its own stated purpose was to be cited by them

**Measured**: inbound body references to `perception-and-the-interface` across the whole `obsidian/` tree (excluding `reviews/` and `workflow/`) are four files: the entry itself, [positions/positions.md](/positions/), [positions/finding-level-calibration.md](/positions/finding-level-calibration/), and [apex/cross-modal-capability-division.md](/apex/cross-modal-capability-division/) (L130). **Zero of the eight modality spokes. Zero from the `topics/dualist-perception` front door.**

Why this is the wing's top finding rather than a housekeeping note: [P-PI1](/positions/perception-and-the-interface/#p-pi1)'s own `About this domain` states the purpose in terms this measurement directly falsifies — "The first entry records it once, in the two-tier form [P-F1](/positions/finding-level-calibration/#p-f1) prescribes, **so the spokes and the `topics/dualist-perception` front door have a registered discount to cite instead of each restating its own**." Measured: each restates its own. The front door at L154 carries the phrase "holds the resulting asymmetry as consonant with the interface reading without being probative of it"; the interoceptive spoke at L103 carries "held as consonant-not-probative"; the thermal spoke at L73 carries "the boundary does not weaken the apex's finding". Three independent restatements of one registered discount, with nothing pointing at the register — which is the drift surface the register was created to close.

**The fix is length-neutral and in several places free.** A piped wikilink installs the citation at zero word cost by wrapping text already present: `topics/dualist-perception` L154 already contains the register's own phrase verbatim, so `[[positions/perception-and-the-interface|consonant with the interface reading without being probative of it]]` is a **+0-word** edit there. Same construction available at `interoceptive` L103 and `thermal` L73. Note `interoceptive` has only 192 words of headroom, so the zero-cost form is not optional there.

⚠️ The fix belongs on the spokes, **not** in `positions/` — that tree is `positions-evolve`'s, and its convention mandates a dated prose `Updated` note per edit, so no edit there is length-neutral.

### 2. The vestibular spoke carries none of the debt the apex attaches specifically to it

The apex singles out exactly two spokes for case-specific epistemic debts. Interoception gets one and **carries it**: L99 of the interoceptive spoke states the common-cause null in full, in its own vocabulary — "a shared allostatic-interoceptive system is a common cause of whatever its channels share, and distributing it across insula, cingulate, and brainstem multiplies nodes, not data. The interoceptive evidence is one datum about the inward limit, not a stack of independent ones."

Vestibular gets the *heavier* debt and carries none of it. The apex: "the common-cause cap bites hardest here… Because the vestibular signal *is* multisensory integration, with no separate channel to converge from… it cannot count as independent confirmation… not a seventh converging line." **Measured in the vestibular spoke**: `common-cause-null` 0 hits, bare phrase `common cause` 0 hits, `supramodal` 0 hits, `workspace`/`broadcast`/`Dehaene` 0 hits — each checked as a separate fixed-string case-insensitive count, not as one regex.

This matters because the spoke's closing paragraph reads its own case in the register the apex denies it. It says the vestibular sense "extends the modality survey in a genuinely new direction" and "adds the limiting case the whole series quietly assumed away." The apex's distinction is precisely that the case extends what the asymmetry *means* "without adding to how strongly it is confirmed" — and "adds" is the word the spoke uses without that qualifier. The spoke is not wrong about anything it says; it omits the one thing the apex says about it.

The asymmetry with interoception is the argument that this is a fixable gap rather than a convention: the wing already demonstrates it can carry the debt at spoke level, in one spoke, in that spoke's own idiom. **Headroom: 976 words.** A ~50–70-word addition to §"What the Interface Reading Accommodates—and the Residue", stating the cap and naming the vestibular case as the one it bites hardest, fits without approaching the soft line's far side.

This is Priority 2 and not 1 only because Priority 1 covers eight articles and this covers one.

### 3. The proprioception spoke is a one-way sink in the wing's prose

**Measured, body-only, nav-sections scored separately**: `topics/dual-domain-capabilities-in-proprioception-and-spatial-imagination` makes **zero prose links** to any of the eleven other wing members. Its only outbound wing links are three `Further Reading` entries (apex, vision, tactile). Inbound it is well-connected — the anchor cites it, the apex both prose- and nav-links it, and `tactile`, `vestibular` and `dualist-perception` all reach it.

This is the same *class* of finding as 09-18's `three-dimensional-world-representation-problem` isolate but a different article, and the direction is different: 3D-world was under-linked in both directions, proprioception is well-fed and returns nothing. It is also, unlike 3D-world, named in [P-PI1](/positions/perception-and-the-interface/#p-pi1)'s `Argued in` field as one of the five spokes the position is argued in — so the register asserts an argumentative role its prose does not reciprocate.

It has **1740 words of headroom**, the most of any spoke, so this one is genuinely cheap. The apex names the natural targets: the "substrate divergence" point proprioception supplies to the apex, and the body-schema/body-image dissociation that `vestibular` and `tactile` both already reach toward it for.

### 4. The apex is past its hard length gate — a constraint to record, not a cut to make

`apex/cross-modal-capability-division` is **5005 words** against a hard threshold of **5000**; `length.py:112` gates on `>=`, so the status is `hard_warning` and headroom is **−6**.

Recording it rather than proposing a condense, for a measured reason: prose-only word count (everything before `## Source Articles`) is **4293**, with **733 words** of reference apparatus — an 8-item `Source Articles` list and 23 numbered references. The gate counts the apparatus; the reader does not experience it as length. So this is largely apparatus inflation and the article is not actually bloated at 4293 words of prose against a 4000 soft line.

But two live consequences follow and both are worth having in writing:

1. **`/replenish-queue`'s length-violation generator reads the gate, not this analysis.** A spurious `condense` task on the apex is now a standing possibility, and whoever picks it should read this paragraph before cutting prose.
2. **Every opportunity in this review is host-constrained.** Nothing here proposes adding to the apex. Priorities 1–3 all place their edits on spokes with 976, 1740 and (for the front door) 184 words of headroom, and Priority 1's preferred form is a +0-word piped wikilink.

## Secondary Record — Below the Cap

A record, not a plan. Not proposed, not minted.

- **Thermal states half of the apex's two-sided caveat.** The apex says of the thermal case: "this straddling eighth source does not strengthen the asymmetry claim, only locate its edge." The thermal spoke at L73 states the reassuring half — "the boundary does not weaken the apex's finding; it locates an edge the finding's terms could not place" — and is silent on the non-strengthening half. Both halves are true and the spoke states the one that is easier to hear. Mild, and only visible when the two texts are read side by side.
- **Six spokes carry `supramodal` only inside a `Further Reading` line.** The wing's positive-half claim reaches most of its members as a nav-list gloss rather than as prose any reader of the article body encounters.
- **The spokes' nav glosses do not carry the three-sense scope.** Each summarises the apex as "modality-specific brain side, supramodal mind-side boundary"; the anchor is careful that the decoding covers "vision, hearing and touch, the three senses so far tested". The gloss is not false but is scope-free.
- **`apex/embodied-interface` does not link the register** either, though the anchor's `Argued in` names it as "the orthogonal cut". It has 1115 words of headroom. Folded conceptually into Priority 1 but not proposed separately.
- **Apex last deep-reviewed 2026-07-19**, two months ago, and `positions/` is structurally excluded from the deep-review candidate pool (`tools/curate/deep_review.py:210`) along with `apex/` and `voids/` — so neither the anchor nor its apex can be reached by the corpus's highest-yield operation. Recorded, not acted on; widening that pool is not this review's call.

## Suspicions Checked and Cleared, With Evidence

A cleared suspicion is a result.

- **Suspected: `topics/dualist-perception` never states the significance-tier discount, so the front door leaks an unhedged claim.** *Cleared.* My first grep appeared to show no `consonant`/`probative` hit in prose — but the hit was there and my output was truncated at 250 characters. L154 ends: "holds the resulting asymmetry as consonant with the interface reading without being probative of it." The front door states the discount correctly in its own words. What it does not do is cite the register — which is Priority 1, a different and much smaller defect than the one I suspected.
- **Suspected: the thermal spoke over-reads the thermal grill illusion as evidence for the interface.** *Cleared.* The anti-over-reading sentence is in the same paragraph as the illusion (L59): "the construction is by a fully specified physical mechanism with a confirmed quantitative prediction—exactly what the mechanism-sufficiency rival expects, no tilt toward the interface."
- **Suspected: the thermal spoke's gradient reading is asserted as though its sources support it.** *Cleared, and the reverse is true.* L71 marks it as "the *Map's* inference, asserted by neither source" and argues against both authorities explicitly.
- **Suspected: the vestibular spoke conscripts its naturalist sources.** *Cleared.* L74 names all seven by name as non-allies: "de Vignemont is a naturalist; Pfeiffer, Serino, Blanke, Lopez, Lenggenhager, Laurens, and Droulez are building physicalist models and draw no dualist conclusion. None of them is an ally of the interface reading, and none is enlisted as one here."
- **Suspected: [P-PI1](/positions/perception-and-the-interface/#p-pi1)'s `Depends on` includes a tenet, so it may fail the foundational-dependency test.** *Cleared.* The entry runs the test explicitly and shows the dependency is forward-only: "Retiring the entry returns the wing to eight per-modality claims and disturbs nothing upstream."
- **Suspected: a sibling pass today or yesterday already covers this ground.** *Cleared.* All eight `reviews/*2026-09-19*` and `*2026-09-20*` files grepped for the three wing paths: only `deep-review-2026-09-19-feminist-phenomenology-and-embodied-consciousness.md` mentions `vestibular`, once, and it mentions neither the apex nor the register.

## Ground Already Owned by Open Tasks — Deliberately Not Re-Proposed

`todo.md` grepped by every wing path, each hit resolved to its enclosing `### ` header and status rather than counted raw.

- **All wing-path tasks are `✓` complete.** `capability-division-in-vision` (L2356, ✓ 09-19), `auditory` (L2366, ✓ 09-19), `three-dimensional-world-representation-problem` (L2361, ✓ 09-19), `positions/perception-and-the-interface` adversarial audit (L1747, ✓ 09-17) and its [P-PI1](/positions/perception-and-the-interface/#p-pi1) rewrite (L2863, ✓ 09-17), the apex L128/L80 insula contradiction (L3219, ✓ 09-14), the register-creation task (L3224, ✓ 09-14), `dualist-perception` §Beyond the Visual (L3231, ✓ 09-14), `chemosensory` valence (L3238, ✓ 09-14), `somatic-interface` hub (L3257, ✓ 09-14). None re-proposed.
- **One open P3 touches the wing and I did not re-propose it**: L1671, "Write article on anosognosia and the reversible self-monitoring channel", which turns on caloric-vestibular stimulation. It is an `expand-topic` and `topics/` has roughly one slot; this review adds no competing `expand-topic` and proposes no new article anywhere.

## Cross-Linking Suggestions

| From | To | Reason |
|---|---|---|
| `topics/dualist-perception` L154 | `positions/perception-and-the-interface` | The register's phrase is already present verbatim; a piped wikilink is a +0-word citation. The front door is the wing's highest-traffic entry point. |
| `topics/vestibular-consciousness-and-the-interface` | `concepts/common-cause-null` | The spoke is the case the apex says the cap bites hardest on and is the one spoke with zero mention of it. |
| `topics/dual-domain-capabilities-in-proprioception-and-spatial-imagination` | `apex/cross-modal-capability-division`, `topics/vestibular-…` | Prose reciprocation for a spoke that five wing members cite and that cites none of them in prose. 1740 words of headroom. |
| `topics/interoceptive-consciousness-and-the-interface` L103 | `positions/perception-and-the-interface` | Same +0-word piped form; required in this form, since the spoke has only 192 words of headroom. |

## New Concept Pages Needed

**None.** The wing is at eight spokes plus two apexes plus a register entry, `topics/` has approximately one slot against its cap, and every finding in this review is an integration or calibration finding rather than a coverage gap. Proposing a ninth modality here would be the wrong read of the evidence.

## Tasks Minted

Two, both on wing articles, both from the top of the priority list, both `refine-draft` with repo-relative `File:` paths.

1. `obsidian/topics/vestibular-consciousness-and-the-interface.md` — carry the common-cause debt the apex attaches to this case, and cite the register (Priorities 2 + 1).
2. `obsidian/topics/dualist-perception.md` — cite the register at L154 with a +0-word piped wikilink (Priority 1, highest-leverage single instance).

Priority 3 (proprioception reciprocation) and the remaining Priority 1 instances are recorded here and not minted, per the four-item cap.