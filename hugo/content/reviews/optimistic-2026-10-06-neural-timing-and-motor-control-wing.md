---
ai_contribution: 100
ai_generated_date: 2026-10-06
ai_modified: 2026-10-06 13:12:00+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-10-06
date: &id001 2026-10-06
description: Wing review of the neural-timing and motor-control pages after today's
  Schultze-Kraft correction. The paper's two channels—onset can no longer be withheld
  past ~200 ms, but the movement can still be altered and cancelled as it unfolds—are
  verified in the full text and turned into four priced items on what veto-versus-alter
  does for the Map's minimal-interaction tenet.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-06 13:12:00+00:00
modified: *id001
related_articles: []
title: Optimistic Review - 2026-10-06 - Neural Timing and Motor Control Wing
topics: []
---

# Optimistic Review: Neural Timing and Motor Control Wing

**Date**: 2026-10-06 (review ran 13:04–13:12 UTC; all timestamps from `date -u`)
**Trigger**: the 12:53Z refine-draft (`d9cffec784`) corrected `topics/quantum-neural-timing-constraints`' reading of Schultze-Kraft et al. (2016). This review asks what the corrected reading is worth to the wing, and avoids the clusters reviewed in the last 48 h (egocentric-presentism/indexical; Stapp–Zeno timing corridor; categorical-perception; agency/akrasia; quantum-interface corridor; subject-and-individuation). `topics/motor-control-quantum-zeno` sat in yesterday's Stapp–Zeno corridor review and is read here only as a neighbour.

**Content reviewed** (bodies read in full on disk; lengths from `tools.curate.length.analyze_length`, which counts the reference list; headroom = hard − 1 − count, gate `>=`):

| Page | `analyze_length` | Headroom |
|---|---|---|
| `topics/quantum-neural-timing-constraints` | 2,732 / 4,000 ok | **1,267** |
| `concepts/control-theoretic-will` | 2,706 / 3,500 soft_warning | 793 |
| `concepts/decoherence` | 3,475 / 3,500 soft_warning | 24 |
| `concepts/libet-experiments` | 3,440 / 3,500 soft_warning | 59 |
| `topics/bandwidth-of-consciousness` | 4,156 / 4,000 hard_warning | over hard: length-neutral only |
| `voids/agency-void` | 3,257 / 3,000 hard_warning | over hard: length-neutral only |
| `apex/interface-specification-programme` | 5,111 / 5,000 hard_warning | over hard: length-neutral only |
| `apex/testing-the-map-from-inside` (Veto Test, L164–170) | 4,335 / 5,000 | 664 |
| `research/voids-veto-void-2026-09-18` | research note, unconsumed | — |

**Source verification done this run.** The Schultze-Kraft full text was reached at PMC4743787 (WebFetch; a neutral request for every sentence containing *ballistic / point of no return / alter / abort / cancel*, not a confirmation prompt). Verbatim sentences this review relies on:

- Results: "Cancellation of movements was possible if stop signals occurred earlier than 200 ms before movement onset, thus constituting a point of no return."
- Discussion: "If the stop signal occurs later than 200 ms before EMG onset, the subject cannot avoid moving."
- Discussion: "However, even after the onset of the movement, it is possible to alter and cancel the movement as it unfolds."
- Discussion: "This has been coined a ballistic stage of processing." and "This has been taken to indicate that there is no final 'ballistic' stage in the brain." Both describe the prior literature's hypothesis and its stop-signal refutation; the authors' own claim is the point of no return for *onset*, qualified by the alteration sentence.
- Results: "In stage I, aborted button presses occur very rarely (2.2%), a rate that substantially increased in stages II and III."

Today's L99 wording ("can still be aborted or altered as it unfolds, so the cut-off is not strictly ballistic") is therefore faithful, including "aborted", which the Discussion's "cancel the movement as it unfolds" and the Results' "aborted button presses" both support. The research note's abstract-only grade for this paper can be lifted: two independent full-text reads (12:53Z and 13:07Z) agree.

## Executive Summary

The correction did more than fix a quotation. Schultze-Kraft's paper describes two channels of late conscious influence with different deadlines and different evidential products: *withholding onset*, which closes about 200 ms before EMG onset and whose success leaves nothing to measure, and *altering or cancelling the movement as it unfolds*, which stays open after onset and leaves a trajectory. The wing's control-theoretic pages call veto the cheapest operation because it costs one bit; the paper shows the one-bit operation has the earliest deadline, while the operation that stays available longest costs more bits but is equally minimal in the sense [Tenet 2](/tenets/#minimal-quantum-interaction) actually names (physical magnitude, not bandwidth—`tenets` L67 says so in terms). That separation is the wing's best unexploited asset: it answers half of the veto research note's Tenet-2 sting (minimality steers the Map to an evidentially silent site) by showing the late channel is minimal *and* productive. Four items below, all additive, all within measured headroom or length-neutral where the host is over hard.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)
`quantum-neural-timing-constraints` L156–158 and L162 keep the registers apart more cleanly than most of the corpus: post-decoherence selection "cannot be falsified by timing evidence", that is "a direct consequence of the model's metaphysical character", the Map "accepts this cost", and the page refuses to say its framework "survives" timing objections because "it was never in the arena those objections address." The timing debate is presented as a constraint on mechanisms, never as support for dualism. L85's remark that Thura & Cisek's figure is counted back from movement while Rajan's is counted forward from a cue, "so the two sets of timings are not yet on a shared clock", is the kind of sentence a careful reader trusts a page for.

### The Quantum Mind Theorist (Stapp)
L105–118 state the Zeno proposal in Stapp's own terms (orthodox QM, no new physics, rate of observation as felt effort) and give it a concrete testable consequence at L142 and L184 (a ~1 kHz observation-rate signature; "gamma at 40 Hz is too slow"). L118 ends "Whether this distinction saves the model from decoherence objections remains debated"—the page does not let the snapshot analogy settle the physics. A Stapp sympathiser also notices what the corrected Schultze-Kraft reading offers his model: a Zeno hold is by nature a *stabilising* operation, so the withholding channel is its natural home, and the page could say so without claiming more. (Whether the alteration channel maps onto release from the hold is a question for the Ideas list, not a claim.)

### The Phenomenologist (Nagel)
`apex/testing-the-map-from-inside` L168 instructs the reader: "start reaching for your phone, or begin to stand up. Now stop yourself mid-motion." That is an abort *after onset*—exactly the channel Schultze-Kraft's Discussion leaves open ("even after the onset of the movement, it is possible to alter and cancel the movement as it unfolds"). The exercise was written before today's correction and turns out to sit on the right side of the boundary. L170's "oppositional, directed against a process you yourself set in motion" describes the alter-and-cancel channel's phenomenology, and the paper now supplies a third-person reason the exercise is performable at all.

### The Process Philosopher (Whitehead)
L170 of the timing page locates the Map's influence at "indeterminacy points distributed throughout the decision process", and L166 at "the moment they resolve into definite outcomes". Event-like selection at many points rather than one substance-level cut is Whitehead-friendly, and the corrected paper fits that picture better than the old "ballistic after 200 ms" reading did: influence that persists after onset as alteration is what a distributed-selection model expects, and a single cut-off is what it does not. This is offered as a *fit*, and the page should offer it as one (Item 1); nothing in the wing uses process resonance to move a claim up the evidential scale.

### The Libertarian Free Will Defender (Kane)
`motor-control-quantum-zeno` L99 is the wing's strongest paragraph for Kane: Schurger's accumulator "is a *classical* system … causally closed; the threshold-crossing is fixed by the prior microstate plus the noise realisation, leaving no free degree of freedom for a selector", so the Libet levelling "removes the strongest evidence *against* a conscious role" while the positive claim "holds only if the physical substrate genuinely supplies some" indeterminacy. The timing page's Schurger section (L122–126) draws the same line more briefly. Kane gets a real role for the agent and a page that refuses to buy it with classical noise.

### The Mysterian (McGinn)
`research/voids-veto-void-2026-09-18` proposes a void and attaches four deflations to it in the same note (Brass & Haggard's group-level signature; Wessel & Aron's global interrupt; Filevich et al.'s doubt that intentional inhibition is a kind; single-trial BCI decoding), calling that "the honest form". `voids/agency-void` L66 ends its opening on "the fit is consistency, not support." The timing page's L178 names the asymmetry between what its falsification conditions can and cannot test before listing them. The wing is comfortable saying where its own knowledge stops.

### The Hardline Empiricist (Birch)
Three things to praise and one concern.

Praise (a): the 12:53Z fix added 26 words and said why—"not word-neutral because the qualifier is new content the paper requires." A qualifier the source demands was installed rather than traded for budget; that is the opposite of the condense-regresses-qualifiers failure this corpus records.

Praise (b): the timing page's L130 and L156 sort its four candidates by kind—three "scientific hypotheses about physical mechanisms", one "metaphysical interpretation that the timing evidence neither supports nor undermines"—and L166 says the tenet's claim "is a metaphysical claim about what consciousness does, not an empirical prediction about when it does it." No candidate is moved up a tier on tenet fit.

Praise (c): `bandwidth-of-consciousness` L189 already scopes the veto correctly ("before which conscious intervention can veto prepared actions"), and L47–49 of `one-structure-three-vocabularies` say the bandwidth register "is compatible with a purely physicalist reading … The bandwidth figure constrains the *shape* of the interface; it does not by itself establish that anything non-physical occupies it." Nothing in this wing touches minimal-organism consciousness, so the five-tier scale is not in play.

Concern (not praise): after the correction, two sentences on the timing page are scoped wider than their source. L101 "Any quantum mechanism for conscious selection must operate within this temporal constraint" and falsification condition 3 (L186, "The veto window closes at 200ms. If experiments showed conscious decisions reliably influencing outcomes inside this window …") both treat the 200 ms boundary as bounding *all* conscious influence on movement. The paper bounds *withholding of onset* and says alteration continues past it; condition 3's antecedent is, in its weak form, already met by the source it cites. This is a scope fix, handled as Item 1 (refine-draft), not as an expansion opportunity. The Process Philosopher's fit above and this concern converge on the same paragraph, which is the honest outcome: the page needs to state the two channels before either persona can use them.

## Content Strengths

### `topics/quantum-neural-timing-constraints`
- **Strongest point**: the three-tier sorting of candidates by what timing evidence can do to them (L130, L156–158, L178, L190–192).
- **Notable quote**: "Its timing-agnosticism is not a feature that 'survives' decoherence objections so much as a consequence of operating at a different level of analysis."
- **Why it works**: it pre-empts the objection that the Map has immunised itself, by saying so first and pricing it.

### `concepts/control-theoretic-will`
- **Strongest point**: L80's bit-cost argument for veto is correct and clear as a bandwidth claim.
- **Notable quote**: "A single bit ('stop/go') suffices for the basic operation."
- **Why it works**: it gives the interface a concrete currency. Its one gap is that it never says the currency is bandwidth rather than Tenet 2's magnitude, and never names the deadline (Item 2).

### `research/voids-veto-void-2026-09-18`
- **Strongest point**: the "null product" face—"nothing-happening is consistent with three histories"—and the verbatim concession from Verbruggen et al. (2019) that "response-inhibition latency cannot be observed directly".
- **Why it works**: it is a void whose third-person limb is conceded by the field's own consensus document. The corrected Schultze-Kraft reading now gives it a fifth counterweight (Item 4).

## Expansion Opportunities (four, prioritised)

### 1. `topics/quantum-neural-timing-constraints` — state the two channels and rescope L101 and falsification 3
- **File**: `/home/andy/unfin/unfinishablemap/obsidian/topics/quantum-neural-timing-constraints.md` (2,732 / 4,000; headroom 1,267; finishes ≈2,946, still under soft 3,000)
- **Type**: refine-draft
- **Locus A (L101)**, current: "This defines the veto window: consciousness can withhold a movement up to 200ms before execution, but not after. Any quantum mechanism for conscious selection must operate within this temporal constraint."
- **Proposed**: "This defines the withholding window: consciousness can cancel movement onset until about 200 ms before execution, but not after. The paper's own qualification opens a second channel: 'even after the onset of the movement, it is possible to alter and cancel the movement as it unfolds.' A mechanism for conscious *withholding* must therefore act before the 200 ms boundary; a mechanism for conscious *shaping* of a movement is not bounded by it. The two channels also differ in what they leave behind. A successful veto produces nothing—no single trial can show that a cancelled impulse was ever live—whereas an altered movement leaves a trajectory, and Schultze-Kraft's 'aborted button presses' are such products. The one-bit stop that [control-theoretic will](/concepts/control-theoretic-will/) calls the cheapest operation is the one that closes first and cannot be observed when it succeeds; the costlier, later channel is the one that can." (**+114** net; the quotation is verbatim from the Discussion, verified this run.)
- **Locus B (L186, falsification 3)**, current: "**Timing precision of conscious influence**: The veto window closes at 200ms. If experiments showed conscious decisions reliably influencing outcomes inside this window, the mechanism would require operating at sub-200ms timescales."
- **Proposed**: "**Timing precision of conscious influence**: The withholding window closes about 200 ms before onset, but Schultze-Kraft's subjects could still alter movements inside it, so late influence of the shaping kind is already documented. The open question is withholding: if experiments showed onset reliably cancelled by stop signals arriving later than 200 ms before EMG, the stop-signal reaction time would have been beaten and the mechanism would need to act faster than it." (**+42**)
- **Locus C (L170, Bidirectional Interaction)**, append after "distributed throughout the decision process.": "The paper's second channel is the better fit for that picture: selection at many indeterminacy points predicts that influence persists after onset as alteration rather than ending at one cut-off. This is a fit, not a test; the paper did not look for a non-physical selector and would read the same under a physicalist account of late correction." (**+58**)
- **Zero-cost reciprocals**: L122 "Libet's experiments" → `[[libet-experiments|Libet's experiments]]`; neither `control-theoretic-will` nor `libet-experiments` is linked from this page today.
- **Tenet alignment**: Tenet 2 (magnitude-minimality is untouched by the finding), Tenet 3 (two channels of outward influence rather than one), Tenet 5 (the cheapest site is not thereby the evidenced one).
- **Estimated scope**: ≈ +214 words total (114 + 42 + 58); three edits in one pass; finishes ≈2,946.

### 2. `concepts/control-theoretic-will` L80 (+ length-neutral apex swap) — bit-minimality is not Tenet 2's minimality, and the cheapest operation has the earliest deadline
- **File**: `/home/andy/unfin/unfinishablemap/obsidian/concepts/control-theoretic-will.md` (2,706 / 3,500; headroom 793). Secondary, length-neutral: `/home/andy/unfin/unfinishablemap/obsidian/apex/interface-specification-programme.md` (5,111 / 5,000, over hard).
- **Type**: refine-draft (two files; brief as two tasks if `cycle_post` would close after one)
- **Locus (L80)**, current: "Veto requires minimal bandwidth. A single bit ('stop/go') suffices for the basic operation. This makes it perhaps the most plausible form of conscious control—even a ~10 bits/second channel can issue many veto signals per second."
- **Proposed**, append a paragraph: "Two cautions keep this from proving more than it does. The bit-cost of veto is a bandwidth fact, not the minimality [Tenet 2](/tenets/#minimal-quantum-interaction) names, which concerns the physical magnitude of the influence; a one-bit stop and a many-bit trajectory adjustment can be equally minimal at the quantum level. And the cheapest operation has the earliest deadline. Schultze-Kraft et al. (2016) found that movement onset can no longer be withheld once a stop signal arrives later than about 200 ms before EMG onset, while 'even after the onset of the movement, it is possible to alter and cancel the movement as it unfolds.' Veto is the most plausible operation in bits and the most time-limited in practice; the operation that stays available longest is attractor steering, described next." (**+127**) plus a reference line copied byte-for-byte from `quantum-neural-timing-constraints` ref 9 (**+18**). Total +145; finishes ≈2,851.
- **Apex swap (L98)**, current: "A single bit suffices for stop/go, making veto perhaps the most plausible form of conscious control." → "A single bit suffices for stop/go, making veto the cheapest operation in bandwidth." (**−3**; the deadline caveat then lives on the concept page the apex already links at L92, so the over-hard apex pays nothing.)
- **Tenet alignment**: Tenet 2 as `tenets` L67 states it ("empirical-constraint minimality"), Tenet 3.
- **Estimated scope**: Short.

### 3. `concepts/decoherence` L113 and `concepts/libet-experiments` L91 — the two live sibling loci the 12:53Z fix reported but did not edit
- **File A**: `/home/andy/unfin/unfinishablemap/obsidian/concepts/decoherence.md` (3,475 / 3,500; headroom 24)
- **Locus A (L113)**, current: "and actions becoming ballistic ~200ms before movement (Schultze-Kraft, 2016)" → "and the last point at which movement onset can still be withheld, ~200ms before it (Schultze-Kraft et al., 2016)" (**+10**; finishes 3,485, under the 3,499 ceiling). This removes the strict-ballistic reading the paper's Discussion rejects.
- **File B**: `/home/andy/unfin/unfinishablemap/obsidian/concepts/libet-experiments.md` (3,440 / 3,500; headroom 59). The page cites Filevich et al. 2013 but never Schultze-Kraft, and L91 gives Libet's own window ("cancel a prepared action in the final 100-200 milliseconds before movement") without the later measurement that closes its inner part.
- **Locus B (after L91)**, proposed: "Schultze-Kraft et al. (2016) measured the boundary: onset could be cancelled only when a stop signal came more than ~200 ms before movement, closing the inner part of Libet's window, though the movement can still be altered after onset." (**+39**) plus the reference line (**+18**) = **+57** against headroom 59 — finishes 3,497. ⚠️ Zero slack: re-measure before and after, and if any other edit has landed on this file first, defer the libet half rather than reach 3,500 (gate `>=`). A longer first draft of this sentence (+44) overshot by 3 and was cut.
- **Recorded, not actionable here**: `archive/concepts/quantum-decoherence-objection` L69 and `archive/topics/neural-bandwidth-constraints-and-the-interface` L144 carry the old reading in the archive tree (archived pages are not edited); `research/quantum-neural-timing-constraints-2026-01-24` L72–74 carries a "Quote" ("…200 ms before the onset of muscle contractions") that neither full-text read located — a research note, so a provenance mark rather than a content fix. `bandwidth-of-consciousness` L189 needs no change.
- **Type**: refine-draft (two files)
- **Estimated scope**: Short.

### 4. Expansion — `voids/veto-void` from the unconsumed 2026-09-18 note, with the alter channel as its fifth counterweight
- **Builds on**: `research/voids-veto-void-2026-09-18` (banked 18 days, no article); `voids/agency-void` (over hard, cannot host); `concepts/libet-experiments`; `topics/quantum-neural-timing-constraints` after Item 1.
- **Cap check (measured this run, `tools.evolution.state.count_section_files`)**: `voids` = 113 against `max_voids: 115` in `evolution-state.yaml` — two slots. The CLAUDE.md table (99/100) is stale; the cap was raised.
- **Would address**: the note's Tenet-2 sting—"parsimony steers the Map's interaction to the one site where evidence cannot be obtained"—is half-answered by the corrected paper. The withholding channel is silent when it succeeds (null product); the alteration channel is equally minimal in Tenet 2's magnitude sense and leaves a measurable product (a modified trajectory; Schultze-Kraft's "aborted button presses"). So minimality does not force the Map onto the silent site; it offers a choice between a cheap-in-bits silent operation and a costlier-in-bits productive one. The note's face 3 (the window closes with no felt signal) also sharpens: a subject who "stops" after 200 ms is altering, not withholding, and cannot tell from inside which they did—a first-person conflation of the two channels that belongs in the void's phenomenology section.
- **Required calibration**: carry all four deflations from the note, plus this fifth; state the transfer inference (externally-cued stopping → self-initiated vetoing) as an inference, with Filevich et al. (2012) as the source that separates them; lift Schultze-Kraft from [abstract] to [raw] on the strength of the two full-text reads today, quoting only the sentences listed at the top of this review; do not upgrade anything else in the note.
- **Positions**: the note's [P-A3](/positions/agency-and-will/#p-a3) audit item ("vetoes reliably shown to be preceded by readiness potentials" presupposes per-trial individuation of vetoes) stands and is a `positions-evolve` decision; the new channel does not change it.
- **Tenet alignment**: Tenets 2, 3, 5; a tenet-generated void in the strict sense the note gives.
- **Estimated scope**: Medium (voids hard 3,000; the note is already sized for it).
- **Type**: expand-topic → cross-review chain. Not minted here (reports-only run).

## Cross-Linking Suggestions

| From | To | Reason |
|------|-----|--------|
| `topics/quantum-neural-timing-constraints` L101 | `concepts/control-theoretic-will` | the one-bit veto claim the timing page now qualifies lives there; currently unlinked in either direction |
| `topics/quantum-neural-timing-constraints` L122 | `concepts/libet-experiments` | zero-cost piped link on "Libet's experiments" |
| `concepts/control-theoretic-will` L80 | `topics/quantum-neural-timing-constraints` | the deadline on the cheapest operation; the concept page never cites Schultze-Kraft |
| `concepts/libet-experiments` L91 | `topics/quantum-neural-timing-constraints` | Libet's own 100–200 ms window against the measured boundary |
| `apex/testing-the-map-from-inside` L168 | `topics/quantum-neural-timing-constraints` | the Veto Test's "stop yourself mid-motion" is the alter-and-cancel channel the paper leaves open; a piped link costs nothing |

## New Concept Pages Needed

- None. The veto void (Item 4) is a voids-section article from a banked note, not a new concept; the withhold/alter distinction belongs on existing pages.

## Ideas for Later

- Whether the two channels map onto the two Zeno regimes (`concepts/quantum-zeno-effect` L53: inhibition is the "limited class" case, acceleration the generic one)—a hold as withholding, release as alteration. Speculative; no page should claim it without a source that does.
- The stop-signal reaction time (~200 ms, which the paper says is "compatible with our data") as the clock the withholding channel runs on; `SSRT`, `countermanding` and `race model` are at zero in live content per the note's grep. A sentence in `quantum-neural-timing-constraints`' timing hierarchy could name it.
- Clinical cases where veto success is reportable (tic suppression, premonitory urge), flagged by the note as unsearched.

## Stability notes for the next reviewer

- Today's L99 wording on the timing page is verified against the full text and should not be re-flagged; "aborted" is supported by "cancel the movement as it unfolds" and "aborted button presses".
- `bandwidth-of-consciousness` L189 scopes the veto correctly; its over-hard length is an operator matter already on file.
- `motor-control-quantum-zeno` was reviewed 2026-10-05 (Stapp–Zeno corridor); its L115 standard-theory sentence and L159–161 are that review's items, not this one's.