---
title: Tenet Alignment Check - 2026-09-17
created: 2026-09-17
modified: 2026-09-17
human_modified: null
ai_modified: 2026-09-17T01:07:00+00:00
draft: false
description: "Tenet check 134: Family A closed in 36 minutes, the rest of the 09-14 list untouched; a battery blind spot (wikilinks split phrases) under-counted the substance-dualism family 3→5; a 77-file delta read finds two more concept pages stating Tenet 2's content wrongly and two stating Tenet 4's rationale wrongly."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-17
last_curated: null
last_deep_review: null
---

# Tenet Alignment Check

**Date**: 2026-09-17 01:07 UTC
**Report**: 134th in series
**Files checked**: 678 (`topics/` 329, `concepts/` 327, `positions/` 22) by the direct-contradiction battery; 77 (every file in those three sections committed since 2026-09-14 00:00 UTC — 32 concepts, 15 positions, 30 topics) read in full by four independent readers, every reported locus re-verified by the driver at the cited line.
**Counts are FAMILY counts, not locus counts.**

**Errors**: 0
**Warnings**: 14 families (5 carried unactioned from 09-08/09-11, 5 carried-and-extended from 09-14, 4 new) across ~70 loci
**Notes**: 34 loci

## Summary

1. **Zero ERRORs for the 134th consecutive run.** The battery (25 patterns, emphasis- and
   wikilink-normalised, case-insensitive) returned 630 hits; every Tenet 1/3/4 hit is expository,
   conditional, or an opponent's view. No Map-voice endorsement of eliminativism, epiphenomenalism,
   many-worlds, or a parsimony verdict against dualism exists in the three sections.
2. **The 09-14 "if only one thing" item closed in 36 minutes.** Family A
   (`concepts/spontaneous-collapse-theories`, seven loci) was fixed by `5c89e615c4` at 19:50 UTC;
   the diff is read in Part 1 and every replacement is correctly scoped. The 09-14 Part 3
   standalone item (`concepts/quantum-completeness` L110 plus the Family E siblings) was minted as
   a P3 task (`todo.md` L1734) and is not yet actioned. **Nothing else on the 09-14 list moved**:
   items 2–5 and the entire re-carried tail are live at the same lines, in both trees, with no
   covering task. The 09-14 structural prediction held exactly: the single named item and the
   standalone section were actioned; the list was not.
3. **A battery blind spot, corrected today.** Every battery in this series normalised emphasis but
   not wikilinks. A phrase pattern that spans a link — `the Map's substance ⟦dualism⟧` — was
   invisible. The 09-14 positive-control count for "the Map's substance dualism" was 3; with
   wikilinks flattened it is **5**: `topics/kabbalah-tzimtzum-consciousness-matter` L34 (which the
   09-14 report knew about from its reader, not its battery) and a never-flagged
   `concepts/african-philosophy-of-consciousness` L47. The same splitter produced this driver's own
   first-pass false "GONE" for two Family F keys — caught only because a reader reported them
   present. Part 3 turns the corrected count into one five-locus task.
4. **The delta read found two more files that state Tenet 2's *content* wrongly** — the class the
   09-14 report called unique to Family A. `concepts/improper-vs-proper-mixtures` says objective
   collapse is an exit "the Map declines" and that confirming it "would remove the locus where
   consciousness is proposed to act"; `tenets.md` L125 makes objective reduction the Map's own
   baseline. `topics/consciousness-and-the-metaphysics-of-laws-and-dispositions` makes the tenet's
   "defensibility hostage to" neural coherence survival; `tenets.md` L77 says only the
   pre-decoherence mechanisms depend on that (Part 4, Family G). Two sibling files also state
   **Tenet 4's rationale** wrongly — "follows from its ontology" where L117 says the indexical
   objection carries the weight and L183 files single-outcome actualisation as a posit (Family H).
5. **The Tenet 3 over-claim family (B) is roughly twice the size 09-14 measured.** Twenty-five new
   loci in fourteen delta files, most in the comparative-cognition/metacognition and dream/agency
   wings, and in five files the over-claim sits a few lines from a paragraph in the same file that
   concedes the common-cause reply — an intra-file contradiction rather than a tension
   (`lucid-dreaming` L144 vs L136; `phenomenology-of-mathematical-understanding` L150 vs
   L142/L154; `phenomenology-of-cognitive-capacity` L99/L119/L145 vs its 09-14-fixed L139;
   `phenomenology-of-deliberation-under-uncertainty` L137 vs L127;
   `phenomenology-of-agency-vs-passivity` L73/L133/L167 vs L131/L137).

---

## Part 1 — The 09-14 closures verified

**Family A closed — `5c89e615c4`, 2026-09-14 19:50 UTC (36 minutes after the report).** All seven
keys return zero hits in `obsidian/` and `hugo/content/` under emphasis- and wikilink-normalised
search. The diff, read line by line:

| 09-14 locus | Was | Now | Scoped correctly? |
|---|---|---|---|
| L98 | "conflicts with the Map's Minimal Quantum Interaction tenet, which requires consciousness to be rare and localized" | "conflicts with the Map's prebiotic resolution under Minimal Quantum Interaction, which localises the interface to complex neural systems" | yes — the constraint is now attributed to the downstream resolution (`tenets.md` L125), not the tenet |
| L115 | "conflicts with Minimal Quantum Interaction by requiring macroscopic quantum coherence" | "strains Minimal Quantum Interaction by requiring pre-decoherence coherence" | yes — matches L71/L77 |
| L136 | "preserve the causal connection … consciousness modulates" | "leave room for the causal connection …" | yes |
| L159/L160 (table) | "Conflicts with MQI" ×2 | "Conflicts with prebiotic resolution" / "MQI fallback" | yes |
| L182 | "it's the parameter determining quantum collapse dynamics" | "it's a candidate parameter in collapse dynamics" | yes |
| L184 | "This tenet *requires* spontaneous collapse theories" | "This tenet *favours* spontaneous collapse theories … GRW/CSL provide one minimal design" | mostly — see Note 1 |
| L186 | "provides concrete mechanism for" | "sketches a candidate mechanism for" | yes |

Two residuals recorded as Notes 1–2, neither a re-flag: L184 still singles out GRW/CSL where L125
lists three co-equal baselines, and L112 reads Tenet 2's minimality as *scale* ("Requires
large-scale quantum effects … not minimal interaction") where L69 defines it as
empirical-constraint minimality.

**Part 3 standalone (`quantum-completeness` L110) — tasked, not actioned.** `todo.md` L1734, P3,
`Status: pending`, names L110 and the Family E siblings (`consciousness-and-mathematics` L162,
`meta-problem-of-consciousness` L73). All three keys are live. This is the correct state for a
task in queue; it is listed here so the next check does not re-mint it.

**Everything else — live, unmoved, uncovered.** Every remaining 09-14 key returns exactly one hit
in `obsidian/` at the 09-14 line (or +2 in `aesthetics-and-consciousness`, which gained two lines
in an unrelated 21:07 refine commit: L154→L156, L158→L160) and one hit in `hugo/content/`.
`topics/dualist-perception` took a deep-review commit on 09-15 02:36 that left all four flagged
loci in place. `git log` on the other files since 09-14 19:14 is empty. The coverage check (Part
2) found no covering task for any of them.

---

## Part 2 — Carried families still live, unactioned, uncovered

Every key below was re-verified today at the cited line in both trees. `todo.md` split on
enclosing `### ` headers; every open block mentioning each file classified; none covers the
locus. (Open blocks that name these files are cross-link batches, apex syntheses, length
decisions, an `ai_system` audit and a positions-citation task.)

| Family | Tenet | File | Line | Key (verbatim, emphasis stripped) | Budget (body words; soft/hard) |
|---|---|---|---|---|---|
| W2a | 1 | `concepts/qualia` | 205 | "establish that some non-physical element enters the causal story" | 4032 `hard_warning` (2500/3500) — net-negative only |
| W2b | 4 | `concepts/qualia` | 213 | "preserve the determinacy that phenomenology demands" | same |
| W3 | 1 | `topics/enactivism-challenge-to-interactionist-dualism` | 108 | "irreducible without requiring a separate substance" | 2459 `ok` (3000/4000) |
| W9 | 3 | `topics/consciousness-and-integrated-information` | 82 | "metaphysically real at the token level" | 4000 `hard_warning` — at the ceiling; `length.py` trips on the hard number itself |
| W10 | 3 | `topics/language-recursion-and-consciousness` | 190 | "demonstrates downward causation" | 4161 `hard_warning` |
| W11 | 3 | `concepts/ai-epiphenomenalism` | 63 | "consciousness does genuine causal work" | 2689 `soft_warning` |
| W4a / F | 1 | `concepts/implicit-memory` | 149 | "the Map's substance dualism" | 3248 `soft_warning` |
| W4b / F | 1 | `concepts/mind-brain-separation` | 108 | "the Map's substance dualism" | 2541 `soft_warning` |
| W4c / F | 1 | `topics/philosophy-of-habit-under-dualism` | 45 | "not as an ally of the Map's substance dualism" | 2517 `ok` |
| F | 1 | `topics/kabbalah-tzimtzum-consciousness-matter` | 34 | "This is exactly what the Map's substance dualism (Tenet 1) denies" | 2709 `ok` |
| F | 1 | `topics/consciousness-and-intersubjectivity` | 37 | "consciousness is ontologically individual (as the Dualism tenet requires)" | 2885 `ok`; the file's own L105 says the Map's dualism is "at least coherent with this datum" — which contradicts "requires" |
| B (09-14) | 3 | 13 files, 20 loci — see 09-14 Part 4 Family B | all present | e.g. `dualist-perception` L136/L162, `constraint-satisfaction` L36/L94/L100, `translation` L157, `self-reference` L134, `aesthetics` L132/L142/L156 | see 09-14 table |
| C (09-14) | 2 | `concepts/prebiotic-collapse` L136; `topics/ethics-of-cognitive-enhancement-under-dualism` L52; `topics/quantum-darwinism-and-consciousness` L78/L116; `topics/pragmatist-quantum-foundations-and-the-agent` L105 | all present | unscoped indistinguishability; `ethics` still has zero occurrences of "unconditioned" | prebiotic 3607 and ethics 5700 are over hard — net-negative only |
| D (09-14) | 4 | `dualist-perception` L166; `consciousness-and-mathematics` L196; `aesthetics` L160; `intersubjectivity` L121; `prebiotic-collapse` L106 | all present | felt-weight-as-evidence | |
| E (09-14) | 5 | `quantum-completeness` L110; `consciousness-and-mathematics` L162; `meta-problem` L73 | all present | **tasked — `todo.md` L1734** | |

---

## Part 3 — Standalone: the substance-dualism family is five loci, not three, and the battery could not see two of them

**Tenet**: 1 — `tenets.md` L53 ("neutral between substance and property dualism"), L57 (the
substance lean is "downstream of agent causation rather than of this tenet"), L183 ("Tenet 1
advertises substance/property neutrality while the framework operates substance-dualist").

**Method defect.** The battery pattern `the map's substance dualism` was run on emphasis-stripped
text. Two live loci write the phrase with a wikilink in the middle — `the Map's substance
⟦dualism|dualism⟧ (⟦tenets#^dualism|Tenet 1⟧) denies` (⟦ ⟧ standing in for double brackets) (kabbalah L34) and `the Map's substance
⟦dualism⟧` (african-philosophy L47) — and never matched. The 09-14 report's "positive-control
count 3 (all listed)" was therefore an under-count that happened to be rescued for kabbalah by a
reader. This driver reproduced the same false zero today: a first-pass key check reported kabbalah
L34 and intersubjectivity L37 "GONE" in `obsidian/`, and only a reader's "STILL PRESENT" exposed
it. Wikilink flattening added 16 hits to the battery (614 → 630); the other 14 are all
"without injecting energy or violating conservation laws" boilerplate with a link inside the
phrase — expository, in-contract.

**The five loci, one fix shape.** Each is a contrastive use of "substance" that pins the
agency-cluster lean on the tenet or on "the Map" as such, in an article that never invokes agent
causation:

| File | Line | Verbatim (links flattened) | Fix | Δ words |
|---|---|---|---|---|
| `concepts/implicit-memory` | 149 | "differ substantially from the Map's substance dualism" | delete "substance" | −1 |
| `concepts/mind-brain-separation` | 108 | "closer to neutral monism than the Map's substance dualism" | delete "substance" | −1 |
| `topics/philosophy-of-habit-under-dualism` | 45 | "not as an ally of the Map's substance dualism" | delete "substance" | −1 |
| `topics/kabbalah-tzimtzum-consciousness-matter` | 34 | "This is exactly what the Map's substance dualism (Tenet 1) denies" | delete "substance" — the article's argument (emanationist monism vs the Map) runs on irreducibility; L78's "The Map is a substance dualism" was cleared 09-14 as matching L183 and stands | −1 |
| `concepts/african-philosophy-of-consciousness` | 47 | "has anti-substantialist implications that sit uncomfortably with the Map's substance dualism" | "with the Map's substance-leaning reading" — here the contrast with "anti-substantialist" is doing work, so relabel rather than delete | 0 |

Total −4 words across five files, every file `ok` or `soft_warning`. `todo.md` has no block
covering any of the five for this defect. Multi-file caution as before: record partial completion
in the changelog; do not mark done on a partial sweep.

**Standing correction for the series.** Every prior battery count for a phrase pattern that can
span a wikilink is a lower bound. The battery script now flattens `⟦a|b⟧`→`b`, `⟦a⟧`→`a`, and
`[b](url)`→`b` (⟦ ⟧ standing in for the double-bracket link delimiters) before matching; the Method section records the normaliser.

---

## Part 4 — Delta read: 77 files committed since 2026-09-14, read in full

Four readers, 19–20 files each, briefed identically with the tenets page's scoping rules (L53/L57
substance neutrality; L69 minimality ≠ parsimony; L71/L77 fallbacks and the pre-decoherence
scope of the decoherence dispute; L75/L81 unconditioned register; L95 `^tenet-3-standing`; L101
self-stultification is "the deepest difficulty … rather than its refutation"; L117/L121 indexical
objection as a posit; L125 objective reduction with modulation; L145/L147 internal parsimony
clause). **Every locus below was re-verified by the driver at the cited line by normalised search
or direct print; where a reader's quote did not appear in the driver's first print, the cause was
the driver's own column cut on a long line, confirmed by `grep -F` count, not a reader error.**
Severity graded by the driver; seven reader WARNINGs downgraded to NOTEs with reasons stated.

31 of 77 files returned zero findings, including all fifteen `positions/` files — the register
remains uniformly well-scoped, including the three files created since 09-14
(`perception-and-the-interface`, `thought-and-understanding`,
`value-in-selection-calibration-history-p-vs2`).

### Family G — Tenet 2's content stated wrongly (Tenet 2; 4 warning loci in 2 files) — NEW, the Family A class

- **`concepts/improper-vs-proper-mixtures` L58**: "his preferred exits were Bohmian mechanics and
  objective collapse, both of which the Map declines." — `tenets.md` L125: "The Map's resolution:
  *objective reduction with consciousness modulation*. Physical mechanisms (gravitational
  collapse, spontaneous localization, or unknown processes) provide baseline collapse throughout
  the universe." The Map declines *consciousness-free* objective collapse as the whole story; it
  adopts objective collapse as the baseline. The file has zero occurrences of "prebiotic",
  "baseline" or "modulat".
- **same L96**: "confirmation of such dynamics would remove the locus where consciousness is
  proposed to act." — inverts L125 and the corpus's own developed position
  (`topics/forward-in-time-conscious-selection` L157: "one collapse dynamics with a special case …
  consciousness biases *which* element the same collapse process delivers"). Confirmed objective
  collapse would fix the baseline the Map already assumes; only a parameter regime leaving no
  neural slack would remove the locus. This is a canonical concept page for the post-decoherence
  programme, and it tells a reader that the programme's own baseline is its defeater.
- **`topics/consciousness-and-the-metaphysics-of-laws-and-dispositions` L150**: "This dispositional
  analysis is hostage to a physical premise: that quantum indeterminacies survive in the warm wet
  brain long enough to be biased." Followed by the Tegmark 10⁻¹³–10⁻²⁰ s figures as if decisive.
- **same L174**: "The tenet's defensibility is hostage to whether biological architectures can
  sustain quantum coherence against decoherence (Tegmark 2000)". — `tenets.md` L77: "This dispute
  matters only for candidate mechanisms that require *pre-decoherence* coherence at neural scales
  … Post-decoherence-selection proposals do not depend on it." The file has zero occurrences of
  "post-decoherence" (five of "decoherence").

**Fixes.** `improper-vs-proper-mixtures` 3269w, concepts `soft_warning` (2500/3500): L58 →
"Bohmian mechanics and consciousness-free objective collapse, both of which the Map declines"
(+1); L96 → "confirmation of such dynamics would fix the baseline the Map's prebiotic resolution
already assumes; only a regime leaving no neural slack would remove the locus where consciousness
is proposed to act" (+14). `metaphysics-of-laws` **4201w, topics `hard_warning` (3000/4000) —
net-negative only**: L150 "This dispositional analysis is hostage to" → "On its pre-decoherence
reading this analysis is hostage to" (+2); L174 "The tenet's defensibility is hostage to" → "The
coherence-dependent mechanisms are hostage to" (−1); find the offset in the L150 paragraph, whose
Tegmark figures duplicate `tenets.md` L77 and can be cut to a pointer.

### Family H — Tenet 4's rationale misattributed to the actualisation ontology (Tenet 4; 2 warning loci, 1 note) — NEW

- **`topics/russellian-monism-versus-bi-aspectual-dualism` L146**: "The Map's rejection of
  many-worlds follows from its ontology: if consciousness actualises possibilities, coexisting
  branches are ruled out." (L102 makes the same move: "less as a free preference than as
  something its ontology appears to force".) Zero occurrences of "indexical" in the file.
- **`concepts/russellian-monism` L131**: "The Map's rejection of Many Worlds follows from its
  ontology: if consciousness actualises possibilities, multiple coexisting branches are ruled
  out." — the same sentence in the sibling article.
- `tenets.md` L117: the indexical objection "is the argument that carries the tenet's weight";
  L183: "objective single-outcome actualization … follows from rejecting many-worlds together
  with the objective-reduction resolution" — the actualisation ontology is *downstream* of the
  rejection, not its ground, and is filed as a background posit. Deriving the tenet from the
  ontology reverses the dependency and hides the posit.
- Note: `concepts/quantum-interpretations` L139 recasts the ground as Tenet 3 incompatibility
  ("MWI provides no role for consciousness in physics … No Many Worlds encodes this
  incompatibility"), against the same file's L48, which states the indexical objection correctly
  (Note 9).

**Fix, both files, net 0.** "follows from its ontology: if consciousness actualises possibilities,
coexisting branches are ruled out" → "rests on the indexical objection; that consciousness
actualises one possibility is a further posit the rejection makes room for, not its ground".
3366w / 2944w, both `soft_warning`.

### Family B (extended) — Tenet 3 over-claims (Tenet 3; 25 new warning loci in 14 files)

The 09-14 pattern, now measured across the dream/agency and comparative-cognition wings too. The
09-14 template form stands: `topics/phenomenology-of-intellectual-courage` L138, "is what Tenet 3
*asserts*; it is not something the phenomenology can *verify*." A second template now exists in
`topics/phenomenology-of-cognitive-capacity` L139, "the felt gradient is neither proof of efficacy
nor evidence against it" — installed on 09-14 in the Relation-to-Site paragraph while the same
file's body loci were left standing, so the file now contradicts itself.

**B-1: same-file contradictions (fix by copying the file's own guard).**

| File | Line | Key (verbatim, emphasis stripped) | Guard in same file | Budget |
|---|---|---|---|---|
| `topics/lucid-dreaming-and-dualist-rendering` | 144 | "Intention-responsiveness in lucid dreams is mental causation made visible. The dreamer's conscious decision reshapes the experienced world." | L136 "The datum counts against epiphenomenalism of dream *content*, not for conscious *control*." | 3803 `soft_warning` |
| same | 96 | "This is mental causation operating on phenomenal content. Will alters phenomenal reality" | L136 | |
| `topics/phenomenology-of-mathematical-understanding` | 150 | "If consciousness were epiphenomenal, this universally described activity would be illusory … insight *produced checkable physical proofs*" | L142 "Nothing in the Ramanujan case decides between them"; L154 "both survive intact" | 3588 `soft_warning` |
| `topics/phenomenology-of-cognitive-capacity` | 99 | "If consciousness were epiphenomenal, there would be no phenomenology of effort in maintenance" | L139 | 2803 `ok` |
| same | 119 | "The Map interprets this as evidence for bidirectional interaction. Consciousness actively constructs the procedural systems that will replace it, then departs." | L139 | |
| same | 145 | "records the dynamics of a causal agent interacting with the matter it shapes" | L139 | |
| `topics/phenomenology-of-deliberation-under-uncertainty` | 137 | "which conflicts with the systematic relationship between phenomenal experience and judgment quality" | L127 "The epiphenomenalist can appeal to a common neural cause" | 2810 `ok` |
| `topics/phenomenology-of-agency-vs-passivity` | 73 | "hard tasks feel hard because consciousness is doing more … The felt cost of effort corresponds to genuine causal engagement." | L131, L137 "underdetermined by the evidence" | 3630 `soft_warning` |
| same | 133 | "would be a cosmic coincidence if consciousness contributed nothing to producing the states it tracks" | L131 (two lines earlier) | |
| same | 167 | "supports the tenet that consciousness causally contributes to physical outcomes" | L137, L139 | |
| `topics/dream-consciousness` | 217 | "Lucid dreaming provides direct evidence: the dreamer's conscious intention causes changes in the experiential world" | L183 "none is individually decisive" | 3873 `soft_warning` |
| `topics/consciousness-and-the-phenomenology-of-translation` | 157 | "is mental causation producing physical outcomes (the translated text)" | L87, L129 | 3545 `soft_warning` |
| `topics/dualist-perception` | 80 | "bistable perception shows consciousness *actively participating* in settling which reconstruction becomes experience" | L150 "compatible with both readings" | 3815 `soft_warning` |

**B-2: no same-file guard (fix needs the courage-L138 sentence added, +15 to +25 words).**

| File | Line | Key | Budget |
|---|---|---|---|
| `concepts/metacognition` | 134 | "marks where consciousness becomes causally indispensable" | 3541 `hard_warning` (2500/3500) — net-negative only |
| same | 182 | "Metacognitive trainability exemplifies consciousness causally influencing physical processes" | |
| `concepts/cognitive-phenomenology` | 214 | "The experience of mental effort reflects consciousness intervening in neural processing until understanding crystallizes." | 3271 `soft_warning`; zero occurrences of "epiphenomen" |
| `concepts/predictive-processing` | 182 | "consciousness provides the genuine agency that chooses which predictions to enact" | 3493 `soft_warning`; zero "epiphenomen" |
| `concepts/ai-consciousness-typology` | 175 | "lack not just experience but the causal contribution that experience provides" | 3499 `soft_warning` |
| `concepts/jourdain-hypothesis` | 129 | "just as the Bidirectional Interaction tenet predicts" — the tenet makes no comparative-cognition prediction | 3485 `soft_warning`; partial guard L183 |
| `concepts/russellian-monism` | 101 | "gives consciousness genuine causal work—selecting among undetermined quantum outcomes" (the exact `^tenet-3-standing` phrase, offered as a comparative advantage) | 2944 `soft_warning`; partial guard L99 |
| `topics/aesthetics-and-consciousness` | 80 | "the act of making art reveals consciousness causally shaping the physical world" (lead) | 3391 `soft_warning`; zero "common cause" |
| same | 154 | "aesthetic creation shows phenomenal templates guiding material outcomes" | |
| `topics/consciousness-and-mathematics` | 190 | "receives the strongest domain-specific evidence. Mathematical understanding produces physical effects" — the next sentence is conditional, which is why this is the weakest entry here | 3227 `soft_warning` |

**B-3: Tenet 3 content misstated (2 loci).** `concepts/delegatory-causation` L136: "the
self-undermining argument eliminates epiphenomenalism" (L132: "devastating", "cannot command
assent") — `tenets.md` L101 holds self-stultification to be "the deepest difficulty
epiphenomenalism faces rather than its refutation" and L103 that the phenomenal-concept strategy
survives it. Fix: "eliminates" → "presses hardest on" (net 0). 3492w `soft_warning`.
`concepts/composition-question-rivals` L125 attributes to Tenet 3 "the claim that conscious
wholes have causal powers their parts lack" — not tenet content (Note 10; 4136w over hard).

### Family C (extended) — Tenet 2 unscoped indistinguishability (Tenet 2; 1 new warning locus)

- **`concepts/delegatory-causation` L148**: "Observational closure follows necessarily. … Delegation
  produces no empirical anomalies — and so no Born-test exposure" — zero occurrences of
  "conditioned" or "unconditioned" in the file; the conditioned register P-Q3 keeps open is
  silently closed. Fix: "no empirical anomalies" → "no unconditioned-aggregate anomalies" (+1). The
  09-14 Note 21 on this file's L114/L120/L122 is the same defect one section earlier.
- Carried: `ethics-of-cognitive-enhancement` L52 (still zero "unconditioned"), `prebiotic-collapse`
  L136, `quantum-darwinism` L78/L116, `pragmatist-quantum-foundations` L105.

### Family D (extended) — Tenet 4 felt-weight / determinacy as evidence (Tenet 4; 4 new warning loci)

- **`concepts/metacognition` L188**: "Metacognitive reports are uniformly of determinate, singular
  experiences—never superposed or branching states." — every branch-descendant reports exactly
  this; the datum is what MWI predicts. 3541w over hard.
- **`concepts/predictive-processing` L184**: "The fact that PP works as a scientific framework
  depends on outcomes being singular and definite—collapse being real." — branch-relative
  prediction error is well-defined; the paragraph's second half does invoke indexicality but does
  not retract the first.
- **`concepts/mind-brain-separation` L118**: "the phenomenology of choice … suggests genuine
  selection occurs … choosing feels like determining which possibility becomes real because it
  *is* determining which possibility becomes real." — felt-weight plus a flat Tenet 3 assertion;
  the same file's L90 says "the felt phenomenology alone establishes little". 2541w.
- **`topics/vertiginous-question` L160**: "The felt reality of anticipating one future — not
  multiple incompatible ones — suggests an indexical fact that branch-egalitarian MWI cannot
  accommodate." — the canonical indexical-objection article using felt anticipation as evidence;
  partial guard at L164 ("itself a substantive bet rather than a result the indexical objection
  delivers"). 3978w, 22 words under the hard ceiling.
- Model form for all four: `topics/dream-consciousness` L221, "That phenomenology does not by
  itself support collapse: a branching ontology predicts it equally well, since each branch's
  dreamer lives exactly one history."

### Family E (extended) — Tenet 5 parsimony in the Map's favour (Tenet 5; 2 new warning loci)

- **`concepts/jourdain-hypothesis` L127**: "The most parsimonious marker is the phenomenal character
  itself" — contradicted, not guarded, by the same file's L183: "The Map's alternative is less
  parsimonious, and it accepts that cost on this tenet." Fix: "most parsimonious" → "most direct"
  (net 0). 3485w, 14 words under hard.
- **`topics/lucid-dreaming-and-dualist-rendering` L106**: "The filter model's explanation is
  structurally simpler." — unguarded; L150 invokes Tenet 5 *against* the production model without
  retracting L106. Fix: "structurally simpler" → "structurally more direct" (+1).
- Carried and tasked (L1734): `quantum-completeness` L110, `consciousness-and-mathematics` L162,
  `meta-problem` L73.

### Family F (extended) — substance/individuation commitment pinned on Tenet 1 (Tenet 1; 1 new warning locus beyond Part 3)

- **`concepts/ai-consciousness-typology` L171**: "Dualism distinguishes between consciousness
  generated by a system and consciousness coupled to it, and treats each mode as constituted by the
  entity's nature rather than the substrate's organisation." (L79: "On the Map's dualist framework,
  consciousness is not generated by physical systems but couples with them.") — the coupling
  picture needs bindable entities; a property dualist holds Tenet 1 with none. Fix: "Dualism
  distinguishes" → "The Map's substance-leaning reading distinguishes" (+3). 3499w, one word under
  hard — take the offset from L79.

### Family I — Tenet 2 wording that reads as quantum-woo (Tenet 2; 1 warning locus) — NEW

- **`topics/russellian-monism-versus-bi-aspectual-dualism` L114**: "one whose interaction-denial
  rested on a physical assumption (energy conservation at all scales) that quantum mechanics has
  since undermined." — quantum mechanics has not undermined energy conservation, and the same
  sentence's earlier clause makes the correct point ("biasing among physically indeterminate
  outcomes does not require energy injection"). `tenets.md` L85 rules out energy injection; an
  outside reviewer reads "QM undermined conservation" as the woo the tenet disclaims. Fix: "that
  quantum mechanics has since undermined" → "that outcome-biasing does not touch" (net −1).
  Verified by `grep -F` count 1 on L114.

---

## Part 5 — Priority design

The 09-14 report predicted that only its single named item and its standalone section would be
actioned, and that is exactly what happened (Family A in 36 minutes; Part 3 minted as a task; items
2–5 and the tail untouched). This report keeps the same shape and keeps the list to four.

### If only one thing is done from this report

**Family G, `concepts/improper-vs-proper-mixtures` L58 and L96 — one file, two phrase swaps, +15
words, 3269w `soft_warning`.** It is the Family A class — a concept page teaching a Tenet 2 the
tenets page does not hold — on the concept page the post-decoherence programme cites for its
central distinction, and it tells the reader that confirming the Map's own baseline would defeat
the Map.

### Then, in order, each as one task

2. **Part 3 — the five-locus substance sweep** (`implicit-memory` L149, `mind-brain-separation`
   L108, `philosophy-of-habit` L45, `kabbalah` L34, `african-philosophy` L47): −4 words total, no
   file over soft+, one fix shape. Partial-sweep caution applies.
3. **Family G second file + Family H pair**: `metaphysics-of-laws` L150/L174 (net-negative only,
   4201w) and the identical "follows from its ontology" sentence in
   `russellian-monism-versus-bi-aspectual-dualism` L146 and `concepts/russellian-monism` L131 (net
   0 each). Three files, four loci, all tenet-*content* corrections.
4. **Family B-1, the same-file-contradiction batch**: `lucid-dreaming` L144/L96,
   `mathematical-understanding` L150, `cognitive-capacity` L99/L119/L145, `deliberation` L137,
   `agency-vs-passivity` L73/L133/L167, `dream-consciousness` L217 — six files, twelve loci, every
   one with a guard sentence in the same file to copy from. Record partial completion; do not mark
   done on a partial sweep.

### Re-carried without a task

W2, W3, W9, W10, W11 (unchanged since 09-08); the 09-14 Family B/C/D residue listed in Part 2;
Family B-2 and B-3 above; Family C `delegatory-causation` L148; Family D's four new loci; Family E's
`jourdain` L127 and `lucid-dreaming` L106; Family F `ai-consciousness-typology` L171; Family I
`russellian-monism-versus-bi-aspectual` L114; `intersubjectivity` L37 (Part 2, Family F).

---

## Notes

1. `concepts/spontaneous-collapse-theories` **L184** after the 09-14 fix: "This tenet *favours*
   spontaneous collapse theories … GRW/CSL provide one minimal design." In-contract on "favours"
   and "one"; still singles out GRW/CSL where `tenets.md` L125 lists gravitational collapse and
   unknown processes as co-equal baselines. Not re-flagged.
2. same **L112**: "Requires large-scale quantum effects (microtubule-level), not minimal
   interaction" — reads Tenet 2's minimality as scale; L69 defines it as empirical-constraint
   minimality. L115 now points to Stapp (also coherence-dependent) rather than post-decoherence
   selection as the favoured route.
3. `concepts/delegatory-causation` **L150** "The trilemma-of-selection establishes why this
   selection must be conscious" — discharged by the file's own L182 ("It does not establish *that*
   mental causation in fact operates this way"). Reader WARNING downgraded.
4. same **L170** "Reports about consciousness are genuinely caused by conscious experiences" —
   discharged by L182.
5. `concepts/objectivity-and-consciousness` **L146** "If consciousness is causally efficacious
   (evidenced by our ability to report on phenomenal states)" — reports-as-evidence is `tenets.md`
   L93's own rationale; the conditional frame holds. Reader WARNING downgraded. **L142** answers
   the file's L42 methodological-vs-metaphysical question as settled; **L148** states the
   indexical question's meaningfulness as a datum (L121 concedes it is a posit).
6. `concepts/direction-of-fit` **L33** "provides evidence for the Bidirectional Interaction tenet"
   and L75 — the file engages epiphenomenalism four times and L85 concedes Searle leaves the
   phenomenal-vs-realiser question open with "the Map's tenets fill in" the answer. Reader WARNING
   downgraded to the boundary: the L85 concession should be echoed at L33.
7. `concepts/trumping-preemption` **L88** "a genuine addition the Map's tenet framework warrants"
   — the file's own L73 and L87 call it "a methodological choice under underdetermination rather
   than a tenet-entailed one" and "rival options rather than a settled synthesis". Downgraded.
8. `concepts/jourdain-hypothesis` **L175** — conditional in form, but the consequent equivocates
   between "metarepresentation requires phenomenality" and "phenomenality does causal work".
9. `concepts/quantum-interpretations` **L139** — Tenet 4 ground recast as Tenet 3 incompatibility,
   against the same file's L48. **L127** presents TI/TSVF as supplying "the free will mechanism";
   L171 maps it onto the post-decoherence substrate, which is the guard.
10. `concepts/composition-question-rivals` **L125** — attributes a wholes-vs-parts emergent-powers
    claim to Tenet 3 (Family B-3). 4136w, over hard.
11. `concepts/methodological-pluralism` **L115** "The Dualism tenet holds that functional
    organisation is physical" — a downstream premise, not tenet content.
12. `concepts/substance-property-dualism` **L159** "The Map leans toward substance dualism for two
    reasons. First, it avoids the combination problem entirely." — a general rationale for the
    lean where `tenets.md` L57 places it downstream of agent causation only; L163 states the
    agency rationale correctly.
13. `concepts/ai-hardware-substrate-taxonomy` **L62** "one the Map holds at arm's length" (Orch OR)
    — guarded by L113 ("*one* possible way … not as the Map's settled mechanism").
14. `concepts/filter-theory` **L125** frames the interface as needing sustained coherence; L144
    scopes indistinguishability correctly but no coherence guard exists.
15. `concepts/sleep-and-consciousness` **L134** "The Map proposes consciousness operates through
    attention-mediated quantum Zeno selection" — names the coherence-dependent fallback as the
    mechanism. Same defect: `topics/phenomenology-of-agency-vs-passivity` **L147**,
    `topics/experimental-consciousness-science-2025-2026` **L80** ("what the Map's Minimal Quantum
    Interaction tenet requires: a site where consciousness and quantum physics meet in the brain"
    — Keppler's coherence-domain model is pre-decoherence; partial guard L108).
16. `concepts/russellian-monism` **L43** "provides cleaner solutions than monism's attempt" — guarded
    by L73 ("a methodological contrast, not evidence that the Map is true") and L83. **L141**
    "the empirical advantage that the quantum mechanism currently provides" — Tenet 2 is an
    untested consistency claim (L81); "empirical advantage" overstates it.
17. `concepts/somatic-interface` **L43** "theoretical economy claimed *given* the hard problem
    assumed elsewhere" — deflationary in intent; L115 "interpretive, not probative".
18. `concepts/cognitive-phenomenology` **L111** "the knowledge-argument shows that *any* phenomenal
    character resists functional reduction" and
    `topics/consciousness-and-the-metaphysics-of-laws-and-dispositions` **L110** "which the Map
    takes to succeed" — `tenets.md` L55 frames the arguments as a contested cumulative case, "not a
    set of independent proofs".
19. `topics/consciousness-and-mathematics` **L192** "Every path through mathematical ontology either
    requires irreducible consciousness or fails" (won-result register); **L194** "the timescales of
    mathematical cognition far exceed typical quantum coherence times, making the mechanism
    unclear" — treats coherence as what the tenet needs; zero occurrences of "post-decoherence".
20. `topics/aesthetics-and-consciousness` **L142** "consciousness is doing irreducible work" — inside
    Failed Reductions; downgraded from the 09-14 Family B listing to a note because it is an
    irreducibility claim, not an efficacy claim. **L160** (was L158) felt-weight, carried.
21. `topics/consciousness-and-intersubjectivity` **L121** carried (Family D, 09-14).
22. `topics/consciousness-and-the-normativity-of-reason` **L132** "making them accidentally correct
    at best" — the efficacy claim is conditional (in-contract); "accidentally" ignores the
    tight-correlation reply L101 grants. Partial guard L136. Downgraded from the 09-14 listing.
23. `topics/lucid-dreaming-and-dualist-rendering` **L128** "arguably offers a cleaner account …
    explanatory economy against a named rival, not a result the evidence settles" (self-labelled);
    **L148** lacks the dream-consciousness L221 guard.
24. `topics/dream-consciousness` **L189** "more naturally explained by interactionism" — abductive,
    in-contract if read that way; guarded by L183.
25. `topics/dualist-perception` **L160** (Tenet 1, carried) "demonstrate that physical processing
    and conscious experience are separable" against the file's own L84 type-identity reply; **L78**
    "establish that phenomenal rendering and information processing are separable capabilities".
26. `topics/consciousness-and-the-phenomenology-of-translation` **L155/L109** "is evidence that
    meaning exceeds formal structure" — walked back at L111; the Relation-to-Site restatement drops
    the guard.
27. `topics/phenomenology-of-mathematical-understanding` **L90** "demonstrates that the phenomenal
    and the formal come apart" — L92 says the confabulation objection weakens it "considerably".
28. `topics/experimental-consciousness-science-2025-2026` **L112** "reveal consciousness to be …
    less reducible than physicalist frameworks predict" — same sentence-group disclaims proof.
29. `topics/phenomenology-of-intellectual-courage` **L140** "when the evidence of consciousness
    points elsewhere" — guarded by L136 ("constrains without establishing").
30. `topics/quantum-hardware-and-the-ai-consciousness-coupling` **L91** "the tenet requires" — L87
    says the five requirements are "not the law itself".
31. `topics/concession-convergence-philosophy-of-mathematics` **L118** "predicts that reductive
    simplicity will prove deceptive" — over-reads a defeasible-heuristic tenet as predictive;
    direction in-contract.
32. **Battery-only (not in the delta), soft forward-parsimony tail, all previously examined and
    cleared or noted**: `concepts/geometric-model-of-mind` L113 (09-14 Note 24, label defect);
    `topics/contemplative-practice-as-philosophical-evidence` L59 and
    `topics/cross-traditional-convergence-on-consciousness-irreducibility` L46 (08-12 N6, empirical
    IBE); `topics/comparative-phenomenology-of-meditative-traditions` L143 (carried since 07-30);
    `concepts/problem-of-other-minds` L100 "The simplest hypothesis is that others talk about
    consciousness because they have it" (other-minds IBE, not framework adjudication);
    `topics/forward-in-time-conscious-selection` L157 "The most parsimonious reading is not two
    competing collapse mechanisms but one" — parsimony used *within* the framework to count
    mechanisms, and the paragraph itself concedes "a critic may reasonably count the addition as a
    second mechanism". None re-flagged.
33. **Battery-only, Tenet 4**: `concepts/unity-of-consciousness` L146 "If all branches are equally
    real, unity reports become either false or contentless" — within any branch the report is as
    true as anywhere; Family D form in a file not in the delta. 2645w. Recorded for the next
    delta that touches the file.
34. **Positive controls**: "the Map's substance dualism" 5 (Part 3); "genuine causal work" 33
    occurrences, 11 in an unhedged window (all triaged: 6 are Family B loci above or carried W11,
    `emotion-and-dualism` L57/L135 are negations, `evaluative-qualia` L106 and `phantom-limb` L113
    are "as interactionism requires"/"suggests" forms, `valence-and-conscious-selection` L89
    restates the tenet); "does real work" 18 (2 about consciousness: `anoetic` L110 carried B′,
    `compatibilism` L103 about leeway); "all branches equally real" 14 (all expository or
    correctly indexical); "felt weight" 16 (2 are the 09-14 fixed forms, 1 conditional, the rest
    phenomenological description).

---

## Method

- `obsidian/tenets/tenets.md` read first at L49–147 in full and L181–187 for the Background
  Posits; specific reliance on L53, L55, L57, L65, L69, L71, L75, L77, L81, L85, L93, L95, L101,
  L103, L117, L121, L125, L145, L147, L183.
- Direct-contradiction battery: 25 regex patterns (Tenet 1: 6, Tenet 2: 7, Tenet 3: 7, Tenet 4: 6,
  Tenet 5: 5) over 678 files, **emphasis-stripped, wikilink-flattened (`⟦a|b⟧`→`b`,
  `⟦a⟧`→`a`, `[b](u)`→`b`; ⟦ ⟧ stand in for double brackets), whitespace-collapsed, case-insensitive**; 630 hits (614 before
  wikilink flattening; the 16 additions are listed in Part 3). Hit counts are occurrence counts.
  High-risk classes read in context with hedge/negation/scope filters printed, not applied
  silently; every unhedged hit triaged in Note 34.
- Delta read: `git log --since=2026-09-14T00:00:00 --name-only` over the three sections → 77
  files, split into four groups and read in full by four independent readers briefed identically;
  every locus each reader returned was re-verified by the driver by normalised search or direct
  print at the cited line. Three reader quotes initially failed the driver's print because the
  driver cut long lines at 600–700 columns; each was then confirmed present by `grep -F` count at
  the cited line. Zero reader line numbers needed correction. Severity graded by the driver; seven
  reader WARNINGs downgraded (Notes 3, 5, 6, 7, 20, 22 and `consciousness-and-mathematics` L190
  held at the bottom of B-2), with reasons stated.
- Closure verification read the committing diff (`5c89e615c4`), not the commit message; carried
  keys re-verified in both `obsidian/` and `hugo/content/` with the corrected normaliser. The
  driver's first-pass key check, run without wikilink flattening, reported two live loci "GONE";
  the corrected run is the one reported.
- Word counts from `tools.curate.length.analyze_length` (body-only); thresholds printed
  (topics 3000/4000/6000, concepts 2500/3500/5000, positions 1500/2500/4000), never quoted from
  memory.
- `todo.md` coverage measured by splitting on enclosing `### ` headers and classifying each block
  open/done by its header and Status line.
- Reader absence claims ("no epiphenomenalist concession in file", "zero 'unconditioned'") were
  re-measured by counted `grep -ciF` on each file before being used to grade severity.
- **No content file was modified. No task was minted. Nothing was committed.**
- **No wikilink of any form appears anywhere in this report** — every file reference is
  backticked and every quoted wikilink was flattened to its display text, per this series'
  convention. Verified by printed count: the double-bracket token occurs zero times.
