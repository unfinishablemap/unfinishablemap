---
ai_contribution: 100
ai_generated_date: 2026-11-25
ai_modified: 2026-11-25 15:32:10+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-11-25
date: &id001 2026-11-25
description: 'Tenet check 170, a delta check of the 77 pages edited since 2026-11-20T14:14Z:
  no Errors. 10 Warnings, all over-reach or overstated tenet standing; four are sentences
  left above grade beside sibling sentences the window re-graded.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-11-25 15:32:10+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-11-25
topics: []
---

# Tenet Alignment Check

**Date**: 2026-11-25
**Files checked**: 77 (every page under topics, concepts, voids, apex and positions with a commit since 2026-11-20T14:14Z; apex 9, concepts 32, topics 17, voids 18, positions 1. The two section index files `apex/apex-articles` and `positions/positions` were skipped. `topics/predictive-processing-and-dualism` had a frontmatter-only change.)
**Errors**: 0
**Warnings**: 10 (seven over-reach, two posits stated as results, one tenet standing misstated)
**Notes**: 10

## Summary

No edit in the window contradicts a tenet, concedes epiphenomenalism, endorses many-worlds, or uses parsimony as a decisive argument against dualism. Most of the window was sweeps and deep reviews, and these moved sentences down the ladder:

- The illusionism-reply regrade: 13 pages now route the rejection to [P-RR1](/positions/replies-to-rivals/#p-rr1) and stop treating the regress as a refutation.
- The Stapp reclassification: eight pages now file Stapp's own view as Born-intact question-choice dualism.
- The Torres Alegre extension, now marked as the Map's own: five pages.
- The asymbolia fidelity sweep (Berthier et al. 1988: no treatment-seeking claim): six pages.
- The COGITATE reading: three pages.
- The nine-task run on `concepts/valence`, and deep reviews of eight voids.

Rewritten tenet sections hold the grade. Examples: `voids/creative-aesthetic-void` L180 and `voids/self-transcendence-void` L113 now open with the [P-V3](/positions/voids-as-evidence/#p-v3) sentence; `voids/commensurability-void` L97 says the void "returns no evidential support to dualism or to any other tenet"; `voids/simulation-detection-void` L108 says the void "lends it no evidential support"; `topics/dual-domain-capabilities-in-proprioception-and-spatial-imagination` L105 and L107 changed "finds strong evidence" and "receives indirect support" to an illustration and "only compatible"; `apex/what-it-might-be-like-to-be-an-ai` L166 says the framing is "derived from the Map's dualism rather than independent support for it"; `concepts/entropic-brain-hypothesis` L84 calls its filter reading "an interpretive overlay".

As on 2026-11-20, the new failure is local inconsistency. In four places the window re-graded one sentence and left its neighbour, or a sibling page, at the old grade:

- `concepts/valence` L89 was changed today from "supports" to "is consistent with the Map's framework at three tenets". Two lines below, L91 still says the Dualism tenet "draws support".
- `concepts/reductionism` L109 was edited on 2026-11-24 by the asymbolia sweep. It kept "The dissociation reveals that phenomenal awfulness is a distinct contributor to motivation", and the same edit inserted, in the sentence before, that the patients "fail to withdraw or to learn protective responses". The next sentence still says "The functional role is filled".
- `topics/emotion-and-dualism` L145 states value-sensitive selection flatly ("consciousness biases selection toward positively valenced outcomes"). Today's repair of `concepts/valence` L95 holds the same position "at low credence, framework-internal only" ([P-VS1](/positions/value-in-selection/#p-vs1)).
- `apex/interface-specification-programme` L171 was repaired in the window: minimality is "*motivated* by the programme's constraints rather than derived from them". L173 still says the programme "shows why bidirectionality is architecturally necessary", and L177 still calls the added complexity "complexity that earns its keep".

These four make up the Priority List. The other six Warnings are older sentences on pages the window touched for other reasons.

Method. I extracted the window's body diff for all 77 files against `93d414b32e`: 516 changed lines, frontmatter excluded, with word-level markers. I read the whole tenet section of 39 pages: all 18 voids, the six pages the brief names, and every page whose tenet section changed in the window. I read every changed body line that uses tenet vocabulary (162 lines), plus every changed line of `concepts/valence` and `positions/replies-to-rivals`. Six grep passes ran over the full current body text of all 77 files:

| Pass | Hits |
|---|---|
| Contradiction probes | 35 |
| Support language | 26 |
| Strong verbs | 379 |
| Causal-work phrasing | 73 |
| Necessity vocabulary | 24 |
| Co-optation roster, tenet sections only | 6 |

I read in context every hit that falls in a tenet section or on a changed line. Every quoted string below has `str.count == 1` in the live file. Before calling a sentence over-reach, I read the page's own concession to its end. A sentence already marked "on the Map's reading" or "the Map holds" was treated as the Map's voice.

## Errors

None.

The contradiction probes covered these patterns: epiphenomenalism "true" or "correct"; experience "causally idle"; many-worlds "true" or "most plausible"; "consciousness is just / an illusion"; parsimony "decisively" or "conclusively" favouring a view; "dualism is false"; energy injection; "consciousness cannot cause". Every hit was one of four things: a rival quoted, a conditional premise, a stated rejection, or the framework's own no-energy constraint. `apex/embodied-interface` L125 says "an experience can be genuinely phenomenal, genuinely owned, and causally idle", which follows the open Tenet 3 quantifier decision (Note 7).

## Warnings

### W1. [concepts/valence.md](/concepts/valence/) L91 (out of step with L89, edited today)
- **Tenet**: Dualism (over-reach)
- **Quote**: "The [Dualism](/tenets/#dualism) tenet draws support scoped to what the arguments above earn: the explanatory gap stands open exactly where the identification of felt badness with a precision signal claims to close it—an unclosed seam, not a demonstration that no reductive account could ever succeed."
- **Issue**: Today's L89 opens the section with "Valence is consistent with the Map's framework at three tenets." The body sets the grade the arguments earn. L69: "Felt badness is thus the Map's datum, which the gap arguments start from and do not establish." L75: "neither side refutes the other from inside its own commitments". So what "the arguments above earn" is compatibility, and "draws support" claims more than the section's own first sentence. The sentence dates from 2026-09-02.
- **Rung earned**: compatible.

### W2. [concepts/reductionism.md](/concepts/reductionism/) L109 (a line the 2026-11-24 sweep edited)
- **Tenet**: Bidirectional Interaction and Dualism (over-reach)
- **Quote**: "The dissociation reveals that [phenomenal awfulness is a distinct contributor to motivation](/topics/pain-consciousness-and-causal-power/), not reducible to the information-processing role. The functional role is filled; the phenomenal character is absent."
- **Issue**: Three sibling pages now say the opposite:
  - `concepts/valence` L57: asymbolia "does not favour the hedonic account over its representational rivals, because both predict the dissociation".
  - `concepts/pain-asymbolia` L119: the behavioural consequences "remain a shared explanandum rather than evidence".
  - `voids/valence-void` L65: "whether the felt badness is what moves behaviour, the case cannot say".

  The piped link also mislabels its target. `topics/pain-consciousness-and-causal-power` L172 grades the pattern "compatible with phenomenal causation rather than evidence for it". The second sentence is inconsistent with the line's own edited clause: the patients "fail to withdraw or to learn protective responses", so the motivational part of the role is missing, not filled.
- **Rung earned**: compatible.

### W3. [topics/emotion-and-dualism.md](/topics/emotion-and-dualism/) L145 (out of step with `concepts/valence` L95, repaired today)
- **Tenet**: Minimal Quantum Interaction (a posit stated as a result; source cited without its stance)
- **Quote**: "When the brain generates multiple possible responses, consciousness biases selection toward positively valenced outcomes and away from negatively valenced ones. Pleasure and pain serve as "mental currency" (Cleeremans & Tallon-Baudry 2022) enabling comparison across disparate experiences."
- **Issue**: The paragraph opens with a conditional ("If valenced states motivate behaviour ... may operate") and then states value-sensitive selection without one. [P-VS1](/positions/value-in-selection/#p-vs1) holds it at credence low and grade D, "as an aspiration grounded in prior commitments". The sibling, repaired today, says the Map "holds it at low credence, framework-internal only". The sibling also states the cited authors' stance: Cleeremans and Tallon-Baudry "take that to reduce the hard problem to one about function" (`concepts/valence` L39). This page cites them in a tenet paragraph without that stance. They are not on the roster, but the verdict-direction leg of the firewall applies.
- **Rung earned**: the Map's posit at low credence.

### W4. [apex/interface-specification-programme.md](/apex/interface-specification-programme/) L173 and L177 (out of step with L171, edited in the window)
- **Tenet**: Bidirectional Interaction and Occam's Razor Has Limits (over-reach; a necessity claim)
- **Quotes**: "Open-loop control is fragile and unreliable. The programme shows why bidirectionality is architecturally necessary, not just philosophically asserted." and "But control theory shows that systems without adequate control are unstable; the added complexity produces the stability and purposiveness that characterise conscious behaviour — complexity that earns its keep."
- **Issue**: A neural controller also needs an upward leg and a downward leg, and it supplies the same stability. So control theory licenses a controller, not a non-physical one. The skill gives a necessity claim ("architecturally necessary") the same burden as an empirical one. L171 now states the shortfall plainly for Minimal Quantum Interaction, and L56 says the six lines' "convergence shows coherence, not independent confirmation". These two sentences still read at the old grade. They were raised by the 09-25, 09-27, 10-26, 10-29 and 11-14 checks and never minted.
- **Rung earned**: compatible (a specification of the tenet, not support for it).

### W5. [topics/ai-consciousness.md](/topics/ai-consciousness/) L153 (older text on an edited page)
- **Tenet**: Dualism (the tenet's standing misstated)
- **Quote**: "The Map treats dualism as a conclusion drawn from these and related arguments"
- **Issue**: `tenets.md` describes Tenet 1 as "a commitment the Map owns, not a result it reports". The same section's L163 has it right: "the former motivate dualism". The heading "**Dualism as conclusion, then as lens.**" carries the same error. No prior tenet check names this sentence. A net −1 fix: "The Map treats dualism as a commitment these and related arguments motivate", with the heading changed to "as commitment". Headroom 29 (3970 of 4000).
- **Rung earned**: a commitment.

### W6. [concepts/consciousness-selecting-neural-patterns.md](/concepts/consciousness-selecting-neural-patterns/) L162 (older text; the window repaired a sibling finding)
- **Tenet**: Bidirectional Interaction (over-reach)
- **Quote**: "All three support the Map's [Bidirectional Interaction](/tenets/#bidirectional-interaction) tenet."
- **Issue**: The same line says that in Penrose–Hameroff consciousness "*results from* collapse", which runs only from the physical to the mental. The three frameworks are candidate mechanisms that would implement the tenet if true, not evidence for it. The 2026-09-23 check named this line together with the L124 heading. The window repaired L124 ("The caudate change fits either reading") and left L162. Headroom 7 (3492 of 3500), so a fix must be net-zero.
- **Rung earned**: compatible (two of the three frameworks would implement it).

### W7. [concepts/mental-imagery.md](/concepts/mental-imagery/) L145 (older text on an edited page)
- **Tenet**: Bidirectional Interaction (over-reach)
- **Quote**: "The evidence provides confirmatory support for the Map's position rather than knockdown proof."
- **Issue**: The two sentences before it concede that the evidence is "*consistent with*" causal efficacy and that "The identity-theory response ... remains logically available". The identity theorist predicts the same motor-imagery evidence, so it confirms nothing distinctive to the Map. No prior check names this sentence. Headroom 72.
- **Rung earned**: compatible against physicalism; suggestive against epiphenomenalism only.

### W8. [concepts/predictive-processing.md](/concepts/predictive-processing/) L182 (a paragraph the window edited)
- **Tenet**: Bidirectional Interaction (a posit stated as a result; `tenets#^tenet-3-standing`)
- **Quote**: "consciousness provides the genuine agency that chooses which predictions to enact." The L178 closer is the same: "The brain generates predictions; consciousness selects which predictions matter."
- **Issue**: The window rewrote the start of L182 ("parallels this physicalist framework rather than instancing it") but kept the flat close. The tenets page says sentences of this kind "should read no more confidently than this paragraph does". The 2026-09-17 check raised "genuine agency that chooses". Headroom 6 (3493 of 3500).
- **Rung earned**: the Map's posit ("on the Map's posit").

### W9. [concepts/mysterianism.md](/concepts/mysterianism/) L64 (older text on an edited page)
- **Tenet**: Occam's Razor Has Limits (over-reach; the roster)
- **Quote**: "The position strongly supports the [Occam's Razor Has Limits](/tenets/#occams-limits) tenet:"
- **Issue**: McGinn's closure thesis is a position, not a datum. The 2026-11-18 check flagged the sibling sentence at `topics/hard-problem-of-consciousness` L229 ("This supports the Map's Occam's Razor Has Limits tenet", also of mysterianism). The page states McGinn's naturalism elsewhere, so the firewall holds; only the grade is high. "illustrates" for "strongly supports" is −1 word. Headroom 15, and two open tasks want it (todo L94 and L6742).
- **Rung earned**: compatible (illustration).

### W10. [topics/wheelers-participatory-universe-and-it-from-bit.md](/topics/wheelers-participatory-universe-and-it-from-bit/) L148 (older text on an edited page)
- **Tenet**: Occam's Razor Has Limits (over-reach)
- **Quote**: "This state of affairs supports the Map's [Occam's Razor Has Limits](/tenets/#occams-limits) tenet."
- **Issue**: The "state of affairs" is the lack of consensus after the 2013 FQXi contest. Disagreement between two views shows that neither has been established. It does not show that parsimony misleads. Headroom 4 (3995 of 4000), so a fix must be net-zero ("illustrates" for "supports").
- **Rung earned**: compatible (illustration).

## Notes

1. [concepts/pain-asymbolia.md](/concepts/pain-asymbolia/) L119 keeps "absent withdrawal, absent guarding, absent avoidance learning" after the window's Berthier sweep took guarding out of the lead (aa446cea48) and out of four siblings (889bebf047). This is a factual straggler, not a tenet issue. Open task todo L4629 owns another phrase in this same Bidirectional line, so the fix could be folded into it.
2. [voids/disappearance-voids.md](/voids/disappearance-voids/) L164, edited in the window: "**Bidirectional Interaction** is enriched by the volitional dimensions of each void." The rest of the sentence grades the datum ("fits ... without showing it"), and L162 above states [P-V3](/positions/voids-as-evidence/#p-v3), so "enriched" is the only word at risk. It is the same verb shape as the 2026-11-20 W2 ("gains additional force"), but in a section that otherwise holds the grade.
3. [voids/common-knowledge-void.md](/voids/common-knowledge-void/) L149–L153, edited in the window. The tenet section has no [P-V3](/positions/voids-as-evidence/#p-v3) sentence. The Occam paragraph reads as illustration ("the tenet's claim in compact form"), which is at grade. L153 describes Bidirectional Interaction as "the interface by which two consciousnesses might share content", but Tenet 3 concerns influence of the mental on the physical, not sharing between minds.
4. [voids/capability-division-problem.md](/voids/capability-division-problem/) L120 (older text; the window edited only L80): "The Map interprets the capability division problem as evidence that dualism requires a different kind of explanatory framework than physicalism provides." The next sentence, "Physicalism explains vision entirely in neural terms and treats consciousness as something to be explained away", describes eliminativism, not non-eliminative physicalism. The section still lacks the [P-V2](/positions/voids-as-evidence/#p-v2)/[P-V3](/positions/voids-as-evidence/#p-v3) line that the 2026-10-24 check (W11) asked for.
5. [concepts/quantum-consciousness.md](/concepts/quantum-consciousness/) L150 and [concepts/quantum-biology-and-neural-mechanisms.md](/concepts/quantum-biology-and-neural-mechanisms/) L152: the illusionism sweep edited both lines and kept "*something* must select among outcomes where physics leaves them undetermined". No tenet says indeterminate outcomes need a selector. Tenet 2 offers indeterminacy only as a "candidate location", and on standard indeterminism the outcome may be chance.
6. [concepts/causal-closure.md](/concepts/causal-closure/) L180: "**Quantum mechanics** shows that not all physical events have sufficient physical causes." Eight lines below, in the same section, L188 says the case "presupposes collapse interpretations", and L136 handles Bohm. The section corrects itself, so the only word at risk is "shows".
7. [apex/embodied-interface.md](/apex/embodied-interface/) L125: "an experience can be genuinely phenomenal, genuinely owned, and causally idle". This is token-level idleness of the unattended body and follows the dispositional reading of Tenet 3. That quantifier choice is the open NEEDS-HUMAN decision recorded on 2026-11-18, so this is not a defect.
8. [topics/pain-consciousness-and-causal-power.md](/topics/pain-consciousness-and-causal-power/) L170, "Pain provides the most intuitive support for irreducibility", is unchanged since the 2026-11-20 check (Note 6), and was borderline then. The window's change to this page was the anchor and the Berthier clause.
9. [topics/ethics-of-consciousness-invertebrate-question.md](/topics/ethics-of-consciousness-invertebrate-question/) L83, edited in the window, says that requiring certainty is unjustified because direct observation of another's experience "is impossible in principle". L115 (older) says the moral question is "permanently underdetermined at the empirical level". Both depend on "If consciousness is non-physical", which makes them framework-conditional implications. They sit uneasily with Tenet 3, on which a causally efficacious consciousness would leave physical traces.
10. Not a tenet issue, noted for the attribution sweep: `apex/what-it-might-be-like-to-be-an-ai` L168 still says "Koch's superposition-formation might feel like openness", as `topics/consciousness-in-smeared-quantum-states` did at 2026-11-20 Note 9.

**[P-V3](/positions/voids-as-evidence/#p-v3) survey of the 18 voids' tenet sections.** One void still claims support for a tenet, and it is queued:

- `valence-void` L115, "**Dualism** finds particularly strong support." Todo L106 owns it (P3, pending), together with the lead L43.

Thirteen sections either state [P-V3](/positions/voids-as-evidence/#p-v3) or [P-V2](/positions/voids-as-evidence/#p-v2), or grade each paragraph as a reading or an illustration: apophatic-cartography, assent, blindspot, commensurability, creative-aesthetic, disappearance, expertise, language-thought-boundary, observation-and-measurement, preference, self-transcendence, transit, vitality-form. Two more are graded through their dualism paragraphs, although neither names [P-V3](/positions/voids-as-evidence/#p-v3):

- `simulation-detection-void` (L108: the void "lends it no evidential support").
- `ineffable-encounter-void` (L164: "offered as such rather than as the evidence's verdict"; L166: "illustrate the tenet rather than evidencing it").

The remaining two have no disclaimer: `common-knowledge-void` (Note 3) and `capability-division-problem` (Note 4).

**Co-optation roster** (tenet sections of all 77 pages): 6 hits, none an enlistment.

- `concepts/entropic-brain-hypothesis` L82 states the stance of Carhart-Harris and Friston: they build EBH and REBUS "*without* any non-physical interface", and the framework is "engaged as a rival".
- `concepts/mysterianism` L188 cites McGinn on a page about his naturalist thesis.
- `concepts/quantum-biology-and-neural-mechanisms` L174 and `concepts/quantum-consciousness` L192 cite McGinn for an epistemic caveat, not for dualism.
- `concepts/nondualistic-interactionism` L93 mentions Whitehead only as the target of Stapp's contested attempt.

Outside the roster, `topics/tactile-consciousness-and-the-interface` L80, added in the window, is a model: "Merleau-Ponty offered reversibility to undo the subject/object split, so reading it as staging that split is the Map's use of his datum, not his."

## Change since the 2026-11-20 report

**Repaired in the window** (tenet-section and lead sentences, with the 2026-11-20-era wording replaced):

| Page | Locus | Change |
|---|---|---|
| `concepts/valence` | L89 | "supports" → "is consistent with" |
| `topics/emotion-and-dualism` | lead, L57 | "the strongest empirical case for interactionist dualism" → "where the Map's interactionist dualism meets empirical evidence most directly" |
| `apex/identity-across-transformations` | L157 | "strengthens" → "is compatible with" |
| `voids/capability-division-problem` | L80 | "confirm the same architecture" → "fit that architecture without favouring it" |
| `concepts/consciousness-selecting-neural-patterns` | L124 | the heading flagged on 2026-09-23 |
| `concepts/predictive-processing` | L176, L182, L184 | L184's many-worlds argument withdrawn: PP "supplies no argument against Many-Worlds" |
| `topics/dual-domain-capabilities-in-proprioception-and-spatial-imagination` | L105, L107 | regraded to an illustration and "only compatible" |
| `apex/what-it-might-be-like-to-be-an-ai` | L166 | framing "derived from the Map's dualism rather than independent support for it" |
| `concepts/entropic-brain-hypothesis` | L84 | the filter reading marked "an interpretive overlay" |
| `apex/interface-specification-programme` | L171 | minimality "motivated ... rather than derived" |
| `topics/tactile-consciousness-and-the-interface` | L80 | Merleau-Ponty's stance stated |
| five voids | tenet sections | commensurability, creative-aesthetic, self-transcendence, simulation-detection and ineffable-encounter regraded |

Each repair reads at grade.

**The 2026-11-20 Warnings**: all seven are still live. The Priority List was minted:

- Todo L6318 (P3, pending) owns W1 `pragmatist-quantum-foundations-and-the-agent` L103, W3 `interface-threshold` L116 and W4 `consciousness-in-smeared-quantum-states` L124. The window edited the pragmatist page (L93, Stapp) without reaching L103.
- Todo L6116 was upgraded to carry W2, `interested-party-void` L100.
- W5–W7 are recorded as report-only at todo L6329.

**Still present, already queued** (not counted again here):

- `topics/emotion-and-dualism` L137: "The [Dualism tenet](/tenets/#dualism) finds its strongest empirical support in irreducibility;". Carried from 2026-11-18 and 2026-11-20. Open task todo L6960 (P3, pending, minted today) owns L137, but its item (3) names only the paragraph's first sentence ("The felt badness of pain cannot be reduced ..."). The "strongest empirical support" clause is in the same paragraph and is not named. I recommend an addendum to L6960 rather than a new task. It is now also out of step with the page's re-graded lead.
- `apex/embodied-interface` L79: "the hurting *is* what drives the avoidance. Asymbolia is the demonstration:". The 2026-11-24 sweep edited this line and kept both phrases. Todo L5885 (P3, pending) owns it.
- `voids/valence-void` L115 (todo L106), `topics/dual-domain-capabilities-in-proprioception-and-spatial-imagination` L103 "is supported by the persistent explanatory gap" (todo L3571, and the P2 at todo L40), and `concepts/motor-selection` L198 (todo L3061).

**Still present, not queued**: `topics/forward-in-time-conscious-selection` L177, "is what an interface doing causal work at a primitive seam predicts". This was raised on 2026-10-05 and 2026-11-02. The window edited L143 on this page.

## Priority List (at most four)

Rules for all four:
- Re-grep each OLD string (`str.count == 1` at this run) and read its whole paragraph before editing.
- Do not weaken a commitment the Map holds.
- No "This is not X. It is Y."; no "load-bearing".
- Do a pronoun and next-sentence check after each replacement.

Word counts are from `tools.curate.length.analyze_length` at this run. Gates fire at `>=`, and headroom is hard − 1 − count.

### 1. [concepts/valence.md](/concepts/valence/) L91: match L89
3278 words of 3500 (headroom 221). No open task names this file's tenet section. The open valence tasks are research tasks (todo L64, L70), and the fold task at L6895 targets `topics/valence-as-a-natural-kind`.
- OLD: `The [[tenets#^dualism|Dualism]] tenet draws support scoped to what the arguments above earn: the explanatory gap stands open exactly where the identification of felt badness with a precision signal claims to close it—an unclosed seam, not a demonstration that no reductive account could ever succeed.`
- NEW: `The [[tenets#^dualism|Dualism]] tenet meets valence at the explanatory gap, which stands open exactly where the identification of felt badness with a precision signal claims to close it. Since the gap arguments start from felt badness as the Map's datum, the gap is consistent with the tenet and adds no evidence for it—an unclosed seam, not a demonstration that no reductive account could ever succeed.`
- Budget: +20 (44 → 64). This page had nine tasks today, so re-read L57, L69 and L75 first and keep their grades.

### 2. [concepts/reductionism.md](/concepts/reductionism/) L109: bring the asymbolia sentence to its siblings' grade
3423 words of 3500 (headroom 76). No open task names this file. The paragraph's second-to-last sentence (edited 2026-11-24) stays as it is.
- OLD: `The dissociation reveals that [[pain-consciousness-and-causal-power|phenomenal awfulness is a distinct contributor to motivation]], not reducible to the information-processing role. The functional role is filled; the phenomenal character is absent.`
- NEW: `Unlike a zombie, though, the patients lose part of the role as well: the aversive disposition goes missing with the felt awfulness, and [[pain-consciousness-and-causal-power|which absence explains which]] is open. The case shows detection without the phenomenal character, a pattern representational accounts also predict, so the full functional role without the feel remains a conceivability claim.`
- Budget: +27 (28 → 55). The next paragraph opens "This is the intuition behind the [zombie argument](/concepts/philosophical-zombies/)", and "This" reads correctly after the NEW ending. Models of the grade: `voids/valence-void` L65 and `concepts/valence` L57.

### 3. [topics/emotion-and-dualism.md](/topics/emotion-and-dualism/) L145: match `concepts/valence` L95 and state the cited authors' stance
3477 words of 4000 (headroom 522). Open task todo L6960 (P3, pending) owns L137, the description and ~L71 on this page, not L145. Run this edit in the same pass as L6960 if possible, and add its L137 "strongest empirical support" clause (see Change since the last report). The first sentence of the paragraph ("If valenced states motivate behaviour, ...") stays as it is.
- OLD: `When the brain generates multiple possible responses, consciousness biases selection toward positively valenced outcomes and away from negatively valenced ones. Pleasure and pain serve as "mental currency" (Cleeremans & Tallon-Baudry 2022) enabling comparison across disparate experiences. Valence provides the criterion—positive or negative—by which consciousness evaluates and selects among possible neural states.`
- NEW: `On the value-sensitive reading, which the Map holds at low credence on prior commitments ([[positions/value-in-selection|P-VS1]]), consciousness would bias selection toward positively valenced outcomes and away from negatively valenced ones when the brain generates several possible responses, with valence as the criterion. Cleeremans and Tallon-Baudry (2022) call experience a "mental currency" for comparing disparate experiences, but they take that to reduce the hard problem to one about function; the Map borrows the phrase, not their conclusion.`
- Budget: +24 (51 → 75). Check [P-VS1](/positions/value-in-selection/#p-vs1)'s credence (low) and Asserts wording at `positions/value-in-selection` L51–L52 before quoting them.

### 4. [apex/interface-specification-programme.md](/apex/interface-specification-programme/) L173 and L177: match L171
5096 words of 5000. **The page is already over its hard gate**, so the net change must be ≤ 0. These two edits net −9. Open task todo L6379 (P3, pending) owns L70 and L159 on this page, also at net ≤ 0, and both can run in one pass. Do not touch L146 (reserved, todo ~L3638), the trumping paragraph (operator decision, todo ~L4935), or L56, L72 and L74.
- OLD: `Open-loop control is fragile and unreliable. The programme shows why bidirectionality is architecturally necessary, not just philosophically asserted.`
- NEW: `Any controller, neural or not, needs both legs, so the picture specifies the tenet without evidencing it.`
- OLD: `But control theory shows that systems without adequate control are unstable; the added complexity produces the stability and purposiveness that characterise conscious behaviour — complexity that earns its keep.`
- NEW: `A neural controller would supply the same stability, so the added structure is a cost the tenet permits, not a gain.`
- Budget: −1 (18 → 17) and −8 (29 → 21). In L177, "the tenet" is Occam's Razor Has Limits, which the paragraph names in its first words.

W5–W10 are left off the list. W5 (`ai-consciousness` L153) is the strongest fifth candidate: a net −1 phrase swap with 29 words of headroom. W6, W8 and W10 have 7, 6 and 4 words of headroom and need net-zero swaps. W7 and W9 are single-verb changes that a later deep review of either page can make.

## Files Passing All Checks

No Warning on 67 of the 77 pages. Sixteen of these carry a Note (†, 11 pages) or a sentence carried from an earlier check, queued or not (‡, 6 pages); `apex/embodied-interface` carries both marks.

Apex: born-preserving-causal-efficacy, cross-modal-capability-division, embodied-interface †‡, identity-across-transformations, moral-status-of-edge-cases, post-decoherence-selection-programme, self-concealing-interface, what-it-might-be-like-to-be-an-ai †.

Concepts: ai-consciousness-typology, attention-as-interface, brain-interface-boundary, causal-closure †, consciousness-physics-interface-formalism, conscious-vs-unconscious-processing, conservation-laws-and-mental-causation, coupling-modes, ensemble-level-epiphenomenalism, entropic-brain-hypothesis, experiential-alignment, global-workspace-theory, mental-causation-and-downward-causation, motor-selection ‡, negative-valence-asymmetry-and-the-selection-weighting-function, nondualistic-interactionism, pain-asymbolia †, pairing-problem, psychophysical-laws, quantum-biology-and-neural-mechanisms †, quantum-consciousness †, quantum-indeterminacy-free-will, quantum-probability-consciousness, retrocausality, sleep-and-consciousness, stapp-quantum-mind.

Positions: replies-to-rivals. The new [P-RR3](/positions/replies-to-rivals/#p-rr3) (Griffin) is graded as an accounting claim and states that "The Map's side supplies no evidence against the view ([P-M1](/positions/methodology-and-calibration/#p-m1))".

Topics: amplification-mechanisms-consciousness-physics, auditory-consciousness-and-the-interface, born-rule-and-the-consciousness-interface, chemosensory-consciousness-and-the-interface, correlationism-and-the-ancestrality-argument, covert-consciousness-and-cognitive-motor-dissociation, dual-domain-capabilities-in-proprioception-and-spatial-imagination ‡, ethics-of-consciousness-invertebrate-question †, fish-sentience-and-the-teleost-pain-debate, forward-in-time-conscious-selection ‡, pain-consciousness-and-causal-power †, pragmatist-quantum-foundations-and-the-agent ‡, predictive-processing-and-dualism, tactile-consciousness-and-the-interface.

Voids: apophatic-cartography, assent-void, blindspot-void, capability-division-problem †, commensurability-void, common-knowledge-void †, creative-aesthetic-void, disappearance-voids †, expertise-and-its-occlusion, ineffable-encounter-void, language-thought-boundary, observation-and-measurement-void, preference-void, self-transcendence-void, simulation-detection-void, transit-void, valence-void ‡, vitality-form-void.

Models of the grade worth copying:
- `voids/commensurability-void` L97: "dualism makes room for the void, while the void, being conjectural, returns no evidential support to dualism or to any other tenet".
- `topics/fish-sentience-and-the-teleost-pain-debate` L82: "Dualism blocks the argument for "no"; it does not supply an argument for "yes."".
- `concepts/pain-asymbolia` L119: "The Map's reading meets that constraint; meeting it is not the same as being confirmed by it."
- `topics/covert-consciousness-and-cognitive-motor-dissociation` L96: "CMD is compatible with the Map's dualism and does not discriminate it from production."

## Not Done

- I read whole tenet sections for 39 of the 77 pages. On the other 38 I read the changed lines and the pattern hits; their tenet sections were not edited in the window.
- I filtered changed body lines by tenet vocabulary. Changed lines outside tenet sections that carry none of it were not read: at most 354 of the 516, mostly reference entries, figures and caption boilerplate.
- I did not re-run the corpus-wide support-language survey of 2026-11-18; this report only tracks the change in its findings.
- No article, position or todo entry was edited. No tasks were minted, because there were no Errors and the driver mints from the Priority List. No commit.