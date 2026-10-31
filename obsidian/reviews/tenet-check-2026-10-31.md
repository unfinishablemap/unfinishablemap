---
title: Tenet Alignment Check - 2026-10-31
created: 2026-10-31
modified: 2026-10-31
human_modified:
ai_modified: 2026-10-31T16:08:00+00:00
draft: false
description: "Tenet check 158, a delta check: no Errors and no over-correction in 76 changed pages. Nine Warnings, mostly felt estimation, effort or temporal flow still offered as evidence where a rival predicts it, plus one No Many Worlds reading."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: Andy Southgate
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-31
last_curated:
last_deep_review:
---

# Tenet Alignment Check

**Date**: 2026-10-31. This is check 158. The previous one, `reviews/tenet-check-2026-10-29.md`, was check 157. Its findings and those of check 156 (`reviews/tenet-check-2026-10-26.md`) are not re-raised here unless they are still live on a page that changed in this window.

**Files checked**: 76. This is every content file in `topics/` (32), `concepts/` (30), `apex/` (8), `voids/` (3), `positions/` (1) and `tenets/` (2) changed since 2026-10-29T00:00Z (`git log --since=2026-10-29T00:00Z --name-only`, deduplicated). The window runs over 53 commits, from `a9d21eccc9` (10-29 00:38Z) to `d91a875fe9` (10-31 12:19Z). Nothing in those directories changed after that, and no uncommitted content changes existed at scan time. The first two commits (`a9d21eccc9`, `899ef6ad19`) were already in check 157's window and are spot-checked only.
- **Read in full (2).** The new pages `topics/clinical-insight-presented-and-judged-unreality` and `voids/molyneux-void`.
- **Diff-scoped (76).** Every non-frontmatter added line, read against its removed line (`git diff -U0 0a75af5f59 HEAD`, 648 substantive added lines).
- **Relation to Site Perspective read in full (19).** The pages the brief named or that today's recalibrations touched: trilemma-of-selection (L40–L135), phenomenology-of-deliberation-under-uncertainty (L42–L144), consciousness-and-skill-acquisition, skill-delegation, stapp-quantum-mind, emotion-regulation-and-the-timing-of-control, evaluative-qualia (L40–L130), apex/process-and-consciousness (L127–L179), colour-ontology, auditory, chemosensory, hempels-dilemma, sellars-manifest, grain-mismatch, capgras, first-quantum-free-will-wave, where-the-substance-commitment-enters, and the two new pages.
- **Comparison texts read at the cited lines.** `tenets.md` L53–L55 (Tenet 1 as a commitment), L67–L69 (Tenet 2 as of 10-29: "no detectable Born-statistics deviation"), L85, L93 (Tenet 3 "not as a directly introspectible datum"), L95 (^tenet-3-standing), L97 (the common-substrate counter: "corroborates the tenet rather than establishing it"), L101–L103, L117–L123 (L121 as edited 10-30), L145–L147, L170–L172 ("definite qualia within each branch"). Also `positions/agency-and-will` P-A4 (L91: "no agent can certify its own causal efficacy by introspection"); `concepts/mental-effort` L80 (Calibration), L88 (Modulation), L100 ("The Map cannot dispatch this reading by phenomenal evidence alone"); `concepts/process-philosophy` L160 ("compatibility only"); `concepts/phenomenology-of-choice-and-volition` L147; the co-optation roster (`project/writing-style.md` L207–L213).
- **Prior reviews read before flagging.** These are today's deep reviews of phenomenology-of-deliberation, consciousness-and-skill-acquisition and grain-mismatch. Their stability notes are honoured. Where a finding below goes past one, the reason is given in place.
- **Sweeps.** These were run with Python, because ugrep silently rejects long `.{0,n}` windows ("exceeds complexity limits") and returned false zeros twice before the switch. They covered: the Born-violation wording family in all its forms, corpus-wide (positive control: the 11 live "no detectable Born-statistics deviation" hosts); effort-calibration-as-evidence wording, corpus-wide (61 hits); over-correction and concession wording in the added lines (23 hits); and every many-worlds or branch hit in the added lines (27 hits).
- **Quote checks.** Every quotation below was confirmed by script (`str.count` = 1 at the line given). Word deltas come from `tools.curate.length.count_words` on the frontmatter-stripped body after the replacement, applied in order. Totals come from `analyze_length`. Headroom means hard − 1 − count (topics hard 4,000; concepts 3,500; apex 5,000).

**Errors**: 0

**Warnings**: 9, on 8 window files plus 1 out-of-window file. All are over-reach, or a repair that did not reach a sibling sentence. No page contradicts a tenet.

**Notes**: 12

## Summary

**Lens (a), over-correction: none found.** Today's "fits, not evidence" regrades kept the Map's reading as the Map's reading and kept Tenet 3 as a commitment on every page checked. The clearest models are `clinical-insight` L130 ("That is no concession that experience is causally idle; the tenet's case rests elsewhere."), `emotion-regulation` L37 ("nor that consciousness is idle where an explicit goal is held") and L105 ("the article gives it a location rather than support", with the standing note cited), `affective-forecasting-gap` L94 ("nor should it narrow the tenet into near-epiphenomenalism"), `first-quantum` L83 ("rather than conceding epiphenomenalism"), and `skill-delegation` L38 (the 10:25Z lede, where physically implemented learning and control "fit them equally well" and the Map's reading is still stated as its own). `molyneux-void` L99 ("finds a congenial pattern and no evidence") and `hempels-dilemma` L117 confine the no-evidence verdict to their own subject. Neither generalises it to the tenet. The one watch item is Note 7.

**Lens (b), residual over-claim: the main finding.** Three in-window pages still offer phenomenology as evidence where a rival predicts the same datum, each next to a sentence the same day's pass got right.
- `phenomenology-of-deliberation-under-uncertainty` L128 and L138 (W1). Felt estimation is offered as the page's evidence against epiphenomenalism, and the bold claim "Estimation does causal work" opens with the coincidence framing. Two paragraphs later the same deep review correctly graded felt commitment (L130: "fits this third claim without supplying evidence for it").
- `trilemma-of-selection` L113 and L115 (W3). Effort's calibration to difficulty is offered as what illusion "requires explaining". The resource-monitoring rival stated in the same paragraph predicts that calibration, and `mental-effort` L80/L88/L100 concede it.
- `consciousness-and-skill-acquisition` L176 (W4), carried from check 157 W13. Flow's vividness is offered as "a pattern dualism predicts but materialism must explain away", next to a sentence that is false of the page's own plasticity evidence.

`evaluative-qualia` L40/L110/L130 (W5) is the same shape on a page that conceded at L114 that "the recurrence cannot tell basic from constructed".

**Lens (c), Tenet 4.** Read off experience once: `apex/process-and-consciousness` L135, "This phenomenology is what collapse *feels like* from the inside". The same page also has L129 ("strongly supports") and L177 ("supports rejecting many-worlds"; durée "presupposes one globally unique self") (W2). The 10-29 P1 (`b1aedbe5c9`) fixed "dissolves" and "illusory" on this page and left these lines. Its own L131 now says the Everettian successor "keeps a local durée of its own", and the concept sibling `process-philosophy` L160 grades the same sentence "compatibility only". Every other window instance of Tenet 4 passes: `dualist-perception` L166 (check 157 Priority 1, landed), `smeared-states` L90, `deliberation` L142, `agency-and-will` P-A2 L62, `tenets` L121, `stapp` L164, `where-the-substance` L50, `skill-acquisition` L180 (cost named).

**Lens (d), Tenet 5.** Six window-touched Relation sections still turn the tenet outward in the tiebreaker form (W9). All are recorded against the NEEDS-HUMAN at todo L94, not tasked. One is new: trilemma's 10-30 L115 ("it bars both preferring Horn 3 for its richness") now contradicts its own L135. Controls: `molyneux` L93, `clinical-insight` L132, `capgras` L99, `colour-ontology` L105, `emotion-regulation` L111, `hempels` L117, `trilemma` L115.

**Lens (e), enlistment.** Whitehead (on the process roster) is credited at `process-and-consciousness` L129 with a framework that "strongly supports" rejecting many-worlds (W2). Every other window author carries a stance sentence: Planck and MacKay ("Neither author is an ally", trilemma L115), Sellars (L63), Steward, O'Connor and Potter & Mitchell (where-the-substance L42), Chalmers & McQueen (smeared L122, landed), Searle and Block (biological-naturalism L28/L82), Barwich (chemosensory L84), Friston (clinical-insight L128), Green (molyneux L95), Musacchio (philosophy-of-language L110), Onof (evaluative L106), and Lewis (quantum-probability L94, "a physicalist's formal allowance, not an endorsement"). Sosa at evaluative L102 is a lead only (Note 10).

**Check 157 Priority List: landed.**
- P1 `dualist-perception` L160/L166 (`0ba9461119`) landed as written.
- P2, the Born-violation family on six files (`6a7dcd011c`), landed. Ensemble L59 has a variant tail ("a constraint the corridor meets by construction").
- P3 Chalmers & McQueen (`38c7853429`) landed. Comparing L114 reads "Satisfies five, one conditionally" where the report prescribed "Satisfies four" (Note 2).
- P4 `metacognition` is queued at todo L3504 (pending) and is not in this window.
- The ten-host sweep (`251a753f9e`) landed on all ten.
- Two members of the Born family survive both sweeps (W6).

## Method: families, violations and on-page controls

| # | Family (brief lens) | Violations in window | Compliant instances found (controls) |
|---|---|---|---|
| a | Over-correction: concede epiphenomenalism, or state Tenet 3 unsupported | 0 (Note 7 is a watch item) | clinical-insight L130, emotion-regulation L37/L79/L105, affective-forecasting L90/L94, first-quantum L83, skill-delegation L38/L134, skill-acquisition L116/L178 (common cause conceded, commitment kept), molyneux L99, hempels L117, capgras L83/L97, sellars L71 |
| b | Phenomenology offered as evidence for a tenet | W1 (deliberation L128/L138), W3 (trilemma L113/L115), W4 (skill-acquisition L176), W5 (evaluative L40/L110/L130), W8 (stapp L142) | deliberation L68/L130/L142, trilemma L78/L115 (openness), returning-attention L111, thermal L85/L89, auditory L79/L81, chemosensory L84–L92, colour L103, capgras L35/L97, emotion-regulation L79/L93, philosophy-of-language L100/L110/L124, interface-spec L153 |
| c | Tenet 4 read off experience | W2 (process-and-consciousness L129/L135/L177) | dualist-perception L166, smeared L90, deliberation L142, agency-and-will L62, tenets L121, stapp L164, where-the-substance L50, preference-void L116, skill-acquisition L180 |
| d | Tenet 5 against an opponent | W9 (six loci; todo L94) | molyneux L93, clinical-insight L132, capgras L99, colour L105, emotion-regulation L111, hempels L117, trilemma L115, where-the-substance L81 (defensive) |
| e | Author enlisted for dualism | W2 (Whitehead, L129); Note 10 (Sosa, lead) | the stance sentences listed in the Summary |
| 4 | Tenet 2 Born wording (carried family) | W6 (emotion-regulation L107; probability-interpretation L97, out of window); W7 (skill-delegation L136, bandwidth) | the 11 hosts now reading "no detectable Born-statistics deviation"; memory-channel L154; neurological-dissociations L198; spontaneous-collapse L117 |

The keyword counts are lexical upper bounds. The violation column holds only what survived reading in context.

## Errors

None.

## Warnings

### W1. `topics/phenomenology-of-deliberation-under-uncertainty` L128 and L138: felt estimation offered as the evidence against epiphenomenalism
- **Tenet**: 3 (tenets L93: held "not as a directly introspectible datum"; L97: the common-substrate counter makes such evidence corroborate "rather than establishing it"; P-A4).
- **Quotes** (each once): L128 "**Estimation does causal work.** If the felt sense of "this is the right call" were epiphenomenal—causally disconnected from judgment quality—then its systematic improvement with expertise would be coincidental." and "sits uncomfortably with this prediction"; L138 "The alternative is that expert intuition's phenomenal character is epiphenomenal, which sits uneasily with the systematic relationship between phenomenal experience and judgment quality."
- **Issue**:
  - L128 opens with the coincidence framing. The page's next sentence grants the common neural cause, and on that cause the improvement is no coincidence.
  - The datum then set against the epiphenomenalist is introspective testimony that experts "*rely on*" the felt sense. P-A4 holds that no agent can certify its own efficacy by introspection, and on the rival the common cause produces the testimony too.
  - L138 restates the systematic relationship as telling against epiphenomenalism, though tenets L97 grants that the same substrate yields it.
  - Today's deep review (`2a66b1919f`) graded this the page's "one remaining evidential claim … hedged against the common-cause reply" and recorded the reply as "Mode Three". The hedge concedes the reinterpretation and still lets the testimony count. That is the residue lens (b) targets, so this finding goes past that stability note. The note on felt openness is untouched.
- **Rung earned**: compatible. **Tasked (Priority 1).** 2,886/4,000.

### W2. `apex/process-and-consciousness` L129, L135, L177: No Many Worlds read off temporal phenomenology and process commitments
- **Tenets**: 4 (tenets L117/L121/L123; L170: global exclusion is a further posit; L172: definite qualia within each branch), with Family 10 and the process roster (Whitehead).
- **Quotes** (each once): L129 "yet his framework strongly supports this rejection"; L135 "supports this picture" and "This phenomenology is what collapse *feels like* from the inside."; L177 "supports rejecting many-worlds" and "Durée's interpenetrating flow presupposes one globally unique self".
- **Issue**:
  - The 10-29 P1 (`b1aedbe5c9`, from check 157's upgraded list) rescoped L131/L133 and made the objection "conditional on that subject". It left three support claims standing.
  - L135 reads collapse off how temporal experience feels. The same paragraph then concedes that "each branch-self would experience exactly this continuity".
  - L177 states as flat fact what L131 now labels "on the Map's reading" ("each successor keeps a local durée of its own, so what branching removes is global uniqueness, not continuity").
  - The concept sibling `process-philosophy` L160 carries the corrected sentence: "so the fit is compatibility only; the rejection remains the Map's own commitment".
  - Whitehead, a process monist on the roster, is credited at L129 with a framework that "strongly supports" a rejection of a theory he never met. An Everettian can grant each branch its own definite occasions.
  - L179 is the Tenet-5 tiebreaker form (W9).
- **Rung earned**: compatible. **Tasked (Priority 2).** 4,170/5,000.

### W3. `topics/trilemma-of-selection` L113 and L115: effort's calibration offered as the discriminator the rival predicts
- **Tenet**: 3, lens (b).
- **Quotes** (each once): L113 "Dismissing the pattern as illusion requires explaining why the illusion is so precisely calibrated to what selection would actually involve."; L115 "The systematic pattern above answers for effort alone".
- **Issue**:
  - The objection L113 states, "Perhaps effort is just the brain monitoring resource allocation", predicts effort calibrated to difficulty. That is what a cost signal is.
  - The Map's own effort page concedes this at `mental-effort` L88 (Kurzban; Inzlicht's process model) and L100 ("The Map cannot dispatch this reading by phenomenal evidence alone"). It shows at L80 that felt effort is subtractable while control stays intact (Naccache 2005).
  - `phenomenology-of-choice-and-volition` L147 says outright that "felt effort is not precisely calibrated to demand".
  - The pattern's second element, willed-versus-automatic circuitry, is what the page's own L78 says "needs no non-physical contributor".
  - Today's 06:10Z pass (`0ae010d345`) removed depletion from this paragraph and left the calibration claim. L115 (10-30) then leans on it: the pattern "answers" Planck and MacKay "for effort alone".
  - The open P3 at todo L3724, "Effort over-grading left by the 10-31 depletion fix", owns L54 and testing-the-map L134/L220 on the same file and family. These two lines are its natural scope addition.
- **Rung earned**: compatible. **Tasked (Priority 3, to fold into todo L3724).** 3,402/4,000.

### W4. `topics/consciousness-and-skill-acquisition` L176: flow offered as "a pattern dualism predicts", beside a false sentence (carried from check 157 W13)
- **Tenet**: 1 (tenets L55: a commitment the Map owns, not a result it reports).
- **Quotes** (each once): "Two bodies can be physically identical yet phenomenologically different" and "a pattern dualism predicts but materialism must explain away".
- **Issue**:
  - A pianist's body is not physically identical to a non-pianist's. The page's own body-schema, consolidation and myelination sections document the physical difference.
  - Transient hypofrontality is Dietrich's neural account of flow, so the rival explains the pattern rather than explaining it away.
  - Check 157 recorded this (W13) without tasking it. Today's deep review (`b888c0f110`) conceded the common-cause reply at L116/L162/L166/L178 and did not reach the Dualism paragraph.
  - L178's "the Map's strongest empirical case against epiphenomenalism" sits awkwardly with that review's own stability note ("The Map's objection to epiphenomenalism goes through self-stultification, not through this covariation"). It is recorded as a lead only, because L178 goes on to say "corroborates the tenet rather than establishing it".
- **Rung earned**: compatible. **Tasked (Priority 4).** 3,754/4,000.

### W5. `topics/evaluative-qualia-phenomenal-normativity-across-traditions` L40, L110, L130: convergence counted as burden-shifting after L114 concedes it cannot discriminate
- **Tenets**: 1, 5.
- **Quotes** (each once): L40 "reads this cross-traditional pattern as evidence for [[interactionist-dualism|dualism]]" and "a reading the evidence is compatible with rather than one it forces"; L110 "but it shifts the burden of proof"; L114 "so the recurrence cannot tell basic from constructed"; L130 "requires explaining away the cross-traditional recurrence as shared cognitive bias".
- **Issue**:
  - Within L40 the page calls the pattern "evidence for" dualism and also "compatible with rather than" forcing it.
  - L110 says the physicalist "must explain why" three lineages converged. L114, installed by the 10-30 deep review (`fb37e5af2a`), then shows that the interoceptive-construction account predicts exactly that convergence.
  - L130 recasts the rival's explanation as "shared cognitive bias", but its explanation is shared architecture. What survives, the hard problem "applied to value", is independent of the convergence.
- **Fix, priced** (not tasked): L130 OLD "Eliminating evaluative qualia in favour of a simpler physicalist ontology requires explaining away the cross-traditional recurrence as shared cognitive bias." → NEW "A construction account explains the cross-traditional recurrence by shared architecture, as conceded above, so the recurrence does not count against the simpler ontology." (+3). L40 and L110 want the same grade, "compatible, burden unshifted on the basic-versus-constructed question".
- **Headroom**: 3,351/4,000. Below the cap. First candidate when a slot opens.

### W6. Born-violation wording: two hosts both sweeps missed
- **Tenet**: 2 (tenets L69 "no detectable Born-statistics deviation", L85).
- **Quotes** (each once): `topics/emotion-regulation-and-the-timing-of-control` L107, in the window file's Relation section, "no Born-statistics or conservation violation". `topics/consciousness-and-probability-interpretation` L97, out of window, "since it involves no Born-statistics violation" (this derives the corridor from "the tenet's empirical-constraint minimality", the family check 157 W2 tasked).
- **Issue**: the ten-host sweep matched the verbatim triad, and the six-sentence family matched "ruling out Born-statistics violation". Neither saw the "or conservation" interpolation or the "involves no" form. A Python variant sweep found no further tenet-gloss hosts. The remaining "Born-exact" and "without violating Born statistics" hits (about 40) describe the corridor reading itself, which P-Q2 states, and are correct.
- **Fix, priced** (not tasked):
  - L107: OLD "(no detectable energy injection, no Born-statistics or conservation violation)" → NEW "(no detectable energy injection, no detectable Born-statistics deviation, no conservation violation)" (+2; 3,604/4,000).
  - L97: OLD "since it involves no Born-statistics violation," → NEW "since it involves no detectable Born-statistics deviation," (+1; 3,259/4,000).
  - Add no quantifier, per the sweeps' Coordination line.

### W7. `concepts/skill-delegation` L132 and L136: the Relation section the 10:25Z fix and todo L3760 did not reach
- **Tenets**: 1, 2.
- **Quotes** (each once): L132 "is irreducible to neural description"; L136 "the interface is too minimal for that".
- **Issue**:
  - L132 states the felt control/automaticity difference as irreducible, flat, on a page whose L38 now says physical learning and control "fit them equally well".
  - L136 reads Tenet 2's minimality as low bandwidth ("The Map's low-bandwidth quantum interface explains *why* delegation is efficient"). The siblings repaired in this window say the reverse: `memory-channel` L154 "its minimality bounds detectability, not channel width", and `neurological-dissociations` L198 "throughput is not interface bandwidth".
  - Todo L3760 owns the body loci (L74/L88/L104/L110/L118) and not these lines.
- **Fix, priced** for L136 (scope addition to L3760): OLD "The Map's low-bandwidth quantum interface explains *why* delegation is efficient. Consciousness cannot micromanage every neural event—the interface is too minimal for that." → NEW "On the Map's reading, a low-bandwidth interface would explain *why* delegation is efficient: consciousness could not micromanage every neural event. The bandwidth is the interface hypothesis, not the tenet's minimality, which bounds detectability." (+11). 2,462/3,500.

### W8. `concepts/stapp-quantum-mind` L142 and L138: the bare seeming-regress against illusionism, and the common cause called "pre-established harmony"
- **Tenet**: 3 (L101/L103: illusionism is met "at a framework boundary").
- **Quotes** (each once): L142 "Illusionism faces a regress—the *seeming* to feel effort must be explained."; L138 "pre-established harmony (implausible—why invest in non-functional phenomenology?)".
- **Issue**:
  - Today's 10:56Z edit (`1cdeb494cf`) rewrote L142's second sentence. The adepts now "still draw the effort/effortlessness distinction, their reports tracking PCC activity". It kept the bare regress, which its siblings retired. Reports tracking neural activity are what illusionism predicts.
  - L138 (unchanged since 05-27) is hedged in its last sentence ("constrains epiphenomenalism without establishing the causal reading"). It still files the common-cause reply as "pre-established harmony", the same mislabel the open P3 at todo L1913 owns on `epiphenomenalism` L154.
- **Disposition**: scope additions to todo L3421 (bare-regress siblings) and L1913. The page is 3,991/3,500, over its gate, so any fix must be net-negative. Not tasked.

### W9. Tenet 5 turned outward in the tiebreaker form, six window-touched Relation sections
- **Tenet**: 5 (L145 "binds the Map's use of parsimony"; L147).
- **Quotes** (each once):
  - `phenomenology-of-deliberation` L144: "simplicity bought by ignoring data is selective blindness". The paragraph's second sentence self-binds. The first sentence still charges the expected-utility reduction with ignoring data the page's own L118 says a metacognitive model explains.
  - `process-and-consciousness` L179: "Materialist parsimony is achieved by excluding experience from the ontology."
  - `stapp-quantum-mind` L168: "trades parsimony for explanatory vacancy".
  - `skill-delegation` L138: "The simpler account covers the neural facts but not the phenomenal ones."
  - `evaluative-qualia` L130 (W5).
  - `trilemma-of-selection` L135: "that the more complex option (genuine mental causation) avoids". This is now contradicted on its own page by the 10-30 L115: "it bars both preferring Horn 3 for its richness".
- **Disposition**: recorded against the NEEDS-HUMAN at todo L94 (the tiebreaker rule), not tasked. Trilemma L135 is the instance to show the human, because the page now states both readings.

## Notes

1. **`concepts/grain-mismatch` L87, convergence counted across a leg a sibling calls non-discriminating.** "constitutes an informational grain mismatch" and "makes the programme collectively robust" count the throughput gap as a third leg. `neurological-dissociations` L198 calls the same throughput gap "a datum any account predicts". Today's deep review ratified L83's "The Map interprets this as evidence" label, and that is honoured. L87's leg count is a lead for the next pass.
2. **`topics/comparing-quantum-consciousness-mechanisms` L114.** "**Tenet alignment: Partial, on the Map's reading (IIT is not dualist).** Satisfies five, one conditionally". Check 157 P3(a) prescribed "Satisfies four". Listing all five beside the label "Partial" now reads inconsistently. Cosmetic, and the firewall is intact.
3. **`concepts/spontaneous-collapse-theories` L185.** "Consciousness-modulated collapse models preserve ontological distinction." is flat, two lines after L181 says reading the term as ontologically distinct "is the Map's addition". It is scoped by L181 and by L94 (IIT is not dualist).
4. **`phenomenology-of-deliberation` L98** ("commitment would feel like nothing … suggests that something more than computation is happening"). Today's deep review recorded "Do not re-flag it unless that frame is removed", and that is honoured. It is noted only because the window's L130 now grades the same felt commitment "fits … without supplying evidence for it", so the body and the Arguments section disagree.
5. **`phenomenology-of-deliberation` L136.** "Two systems could process identical uncertain decisions while one experiences vertigo and the other experiences nothing." is the conceivability premise stated flat (Family 8). The Map holds it, but L55 records it as contested.
6. **`concepts/quantum-probability-consciousness` L94** (10-30, `f24c30e6e9`). The first-person credence rule ends: "What belongs to the Map alone is a chance that shifts when an intention forms, with no physical change." Conditional on the intention, that is a departure from Born weight that is not publicly conditionable. It is consistent with P-Q2's "publicly conditionable" wording. It belongs with the blocked P-Q2 HUMAN DECISION at todo L1725 and is not a defect.
7. **Over-correction watch: `emotion-regulation` L93.** "Nor can the record disconfirm the placement, since a contribution found absent at one stage can be relocated earlier; the disagreement is one of framework." It is honest, and it concedes nothing about Tenet 3. A placement the timing record can neither confirm nor disconfirm is worth the human's eye as a falsifiability cost, not as a tenet fault.
8. **`topics/philosophy-of-language-under-dualism` L108.** "Under dualism, it is a structural prediction." (and "is expected"). The phenomenal-concept strategy the page names at L49 predicts the same ineffability. This is the same claim as L106, which the open P3 at todo L3769 owns, so it is a scope addition there.
9. **`concepts/mental-causation-and-downward-causation` L200.** The window's "Provides the mechanism" → "Names the proposed locus" edit kept "through biasing probabilities". That is the Family 3 wording the open sweep at todo L2415 owns, so it is a scope addition there.
10. **`evaluative-qualia` L102, Sosa.** "Sosa's "Two Forms of Dualism" (2011)" carries no statement of the author's own stance, and the paragraph's "a second front where physicalism fails" is the Map's conditional. Not verified, so this is a lead only, and the stance is not asserted here.
11. **`concepts/epiphenomenalism` L201.** "Epiphenomenalism's plausibility depends entirely on accepting strong causal closure of physics" overstates: some epiphenomenalists argue from exclusion or explanatory economy. Mild, and the sentence's second half (10-30 propagation) is correct.
12. **`apex/testing-the-map-from-inside` L220, a partial repair.** "The Map's framework predicts these features. Materialist frameworks must explain them away." survives today's 06:10Z fix of the paragraph's first sentence. It is owned by todo L3724 (pending, verified) and not re-raised.

## Bearing on the open items

- **todo L3724** (effort over-grading, trilemma L54 and testing L134/L220): W3's L113/L115 belong in the same pass (Priority 3), and W8's stapp L138 shares the claim.
- **todo L3760** (skill-delegation body loci): W7's L132/L136 are scope additions.
- **todo L3769** (philosophy-of-language): Note 8's L108.
- **todo L3421** (bare seeming-regress siblings) and **L1913** (common cause as "pre-established harmony"): W8.
- **todo L2415** (Family 3 "biasing probabilities"): Note 9.
- **todo L94** (Tenet 5 tiebreaker NEEDS-HUMAN): W9's six loci. Trilemma L115/L135 shows the conflict on one page.
- **todo L667** (Tenet 3 quantifier NEEDS-HUMAN): no new silent picks in this window.
- **todo L1725** (P-Q2 HUMAN DECISION): Note 6.
- **todo L3504** (check 157 Priority 4, metacognition): pending, and the page has not changed since check 157.
- **todo L3474** (trilemma Horn 3: L76/L95/L140): unchanged, and it does not overlap Priority 3 (L113/L115).
- **todo L3464** (first-quantum L89, Tenet 5 against Schlick): still live and pending. L89 is unchanged in this window: its diff touches only the Schlick table row, L70, and the Planck rows.
- **Check 157 W13 loci still live**: `skill-acquisition` L176 (now Priority 4). `self-maintained-cognitive-limits` L197 and `motor-selection` L198 are out of window and not re-checked.

## Files Passing All Checks

These 60 files carry no new Warning or Note:
- apex: `born-preserving-causal-efficacy`, `consciousness-and-agency`, `interface-specification-programme`, `living-with-the-map`, `phenomenology-mechanism-bridge`, `what-consciousness-tells-us-about-physics`;
- concepts: `affective-forecasting-gap`, `agent-causation`, `bi-aspectual-ontology`, `biological-naturalism`, `brain-interface-boundary`, `causal-consistency-constraint`, `cotard-delusion`, `coupling-modes`, `depersonalisation-nosology`, `ensemble-level-epiphenomenalism`, `interactionist-dualism`, `intrinsic-nature`, `materialism`, `mind-matter-interface`, `occasionalism`, `physics-as-disclosure`, `quantum-consciousness`, `rollback-argument-against-agent-causation`, `russellian-monism`, `sellars-manifest-and-scientific-images`, `sign-problem-for-conscious-observation`, `substance-property-dualism`, `where-the-substance-commitment-enters`;
- positions: `agency-and-will`;
- tenets: `tenets`, `background-commitments`;
- topics: `alief-and-acting-against-belief`, `auditory-consciousness-and-the-interface`, `bacterial-chemotaxis-and-minimal-biogenic-cognition`, `born-rule-and-the-consciousness-interface`, `capgras-delusion-and-the-affective-recognition-channel`, `chemosensory-consciousness-and-the-interface`, `clinical-insight-presented-and-judged-unreality` (new), `colour-ontology-and-the-secondary-quality-residue`, `consciousness-and-the-epistemic-condition-on-responsibility`, `consciousness-and-the-metaphysics-of-laws-and-dispositions`, `consciousness-in-smeared-quantum-states`, `dualist-perception`, `first-quantum-free-will-wave-1927-1940` (its L89 Tenet-5 sentence is already owned by the open P3 at todo L3464 and is not re-raised), `hempels-dilemma`, `instrumental-convergence`, `memory-channel-interface-evidence`, `multi-agent-born-preservation-problem`, `neural-refresh-rates-and-the-smoothness-problem`, `neurological-dissociations-as-interface-architecture`, `neuron-less-animals-sponges-placozoans-and-the-lower-bound-of-cognition`, `overdetermination-dissolution-under-selection-only-interactionism`, `phenomenology-of-returning-attention`, `the-cognitive-immune-system-and-immunological-selfhood`, `thermal-consciousness-and-the-interface`, `wheelers-participatory-universe-and-it-from-bit`;
- voids: `molyneux-void` (new), `perceptual-reality-monitoring-void`, `preference-void`.

Eight window files carry Warnings: deliberation (W1, W9), process-and-consciousness (W2, W9), trilemma (W3, W9), skill-acquisition (W4), evaluative-qualia (W5, W9), emotion-regulation (W6), skill-delegation (W7, W9), stapp (W8, W9). Eight carry Notes only: grain-mismatch, comparing, spontaneous-collapse, quantum-probability-consciousness, philosophy-of-language, mental-causation-and-downward-causation, epiphenomenalism, testing-the-map-from-inside. That makes 60 + 8 + 8 = 76.

## Priority List

Each OLD string below was confirmed by script to occur exactly once, at the line given. Deltas are `count_words` on the frontmatter-stripped body after the replacement, applied in the order listed. All four items are defects: each sentence offers a datum as evidence that its own page, or the tenets page, concedes the rival predicts.

1. **`topics/phenomenology-of-deliberation-under-uncertainty` L128 and L138 (W1). Tenet 3, lens (b).**
   - **Why it fails**: L128 opens with the coincidence framing the next sentence refutes. It then sets introspective testimony of "reliance" against epiphenomenalism, which P-A4 bars, since the common cause yields that testimony too. L138 counts the systematic relationship against epiphenomenalism, though tenets L97 grants the same substrate produces it.
   - **Length**: 2,886/4,000 (headroom 1,113).
   - (a) L128
     - OLD: `**Estimation does causal work.** If the felt sense of "this is the right call" were epiphenomenal—causally disconnected from judgment quality—then its systematic improvement with expertise would be coincidental. The epiphenomenalist can appeal to a common neural cause underlying both the phenomenology and the judgment quality. But this explanatory strategy predicts that the phenomenology should be eliminable without affecting performance: strip away the felt sense and the judgment should remain. The testimony of expert practitioners—that they *rely on* the felt sense, that it guides rather than merely accompanies their decisions (Dreyfus, 1997)—sits uncomfortably with this prediction, even if the epiphenomenalist can reinterpret such testimony as itself a product of the common cause.`
     - NEW: `**Estimation may do causal work.** On the Map's reading the felt sense of "this is the right call" guides judgment, which is why it improves with expertise. The epiphenomenalist's common neural cause predicts the same improvement, so on neither view is the match a coincidence. Expert practitioners report that they *rely on* the felt sense, that it guides rather than merely accompanies their decisions (Dreyfus, 1997), but the common cause would produce that testimony too, and no agent can certify its own efficacy by introspection ([[positions/agency-and-will#^p-a4|P-A4]]). The testimony fits the Map's reading without discriminating it.`
     - Delta: −16.
   - (b) L138
     - OLD: `The alternative is that expert intuition's phenomenal character is epiphenomenal, which sits uneasily with the systematic relationship between phenomenal experience and judgment quality.`
     - NEW: `The systematic relationship between phenomenal experience and judgment quality fits that reading, and the epiphenomenalist's common-cause reply predicts it too, so it corroborates the tenet without establishing it ([[tenets#^tenet-3-standing|Tenet 3's standing]]); the Map holds the tenet as a commitment, not as a result read off expert phenomenology.`
     - Delta: +24.
   - **Net**: +8 (2,886 → 2,894).
   - **Guards**:
     - The bold "**Estimation …**" is a paragraph lead, not a heading, so no anchor moves.
     - Keep L124's "three positive claims", L130 (graded today) and L142 (Tenet 4 control) untouched.
     - Never concede epiphenomenalism. The common cause is named as the rival's reply, and the Map's reading and the tenet's commitment stay stated.
     - Honour today's deep-review stability note on felt openness. Leave L98 to that note (Note 4).
     - Both link targets exist: `^p-a4` is at agency-and-will L89, and the `tenet-3-standing` anchor is at tenets L95.
2. **`apex/process-and-consciousness` L129, L135, L177 (W2). Tenet 4, lens (c), with Family 10 and the Whitehead roster.**
   - **Why it fails**: L135 reads collapse off how temporal experience feels, then concedes that every branch-self feels the same. L129 and L177 call process philosophy "support" for rejecting many-worlds where `process-philosophy` L160 grades it "compatibility only". L177 states durée's demand for global uniqueness as fact where the page's own L131 states it as "the Map's reading".
   - **Length**: 4,170/5,000 (headroom 829).
   - (a) L129
     - OLD: `Whitehead developed process philosophy before many-worlds was proposed, yet his framework strongly supports this rejection.`
     - NEW: `Whitehead developed process philosophy before many-worlds was proposed, and his framework is congenial to this rejection without arguing for it: an Everettian can grant each branch its own definite occasions, so the fit is compatibility only ([[process-philosophy]]).`
     - Delta: +22.
   - (b) L135, first sentence
     - OLD: `The [[temporal-consciousness|phenomenology of temporal experience]] supports this picture.`
     - NEW: `The [[temporal-consciousness|phenomenology of temporal experience]] fits this picture without deciding it.`
     - Delta: +3.
   - (c) L135, third sentence
     - OLD: `This phenomenology is what collapse *feels like* from the inside.`
     - NEW: `On the Map's reading, this phenomenology is what collapse *feels like* from the inside.`
     - Delta: +4.
   - (d) L177, first sentence
     - OLD: `Process philosophy's commitment to definite actualisation—occasions achieving particular form—supports rejecting many-worlds.`
     - NEW: `Process philosophy's commitment to definite actualisation—occasions achieving particular form—is compatible with rejecting many-worlds; the rejection remains the Map's own commitment.`
     - Delta: +9.
   - (e) L177, last sentence
     - OLD: `Durée's interpenetrating flow presupposes one globally unique self, not many locally continuous successors.`
     - NEW: `On the Map's reading, durée's interpenetrating flow demands one globally unique self rather than many locally continuous successors, a demand that bites only on the non-deflationary subject.`
     - Delta: +14.
   - **Net**: +52 (4,170 → 4,222).
   - **Guards**:
     - Keep L131 and L133 as the 10-29 P1 left them. The new L177 wording must match L131.
     - In L135, keep the sentence "Everettians respond that each branch-self would experience exactly this continuity, making the phenomenology compatible with branching." unchanged, because the next sentence's "this response" refers to it.
     - Leave L179 to the tiebreaker NEEDS-HUMAN (todo L94).
     - `[[process-philosophy]]` resolves uniquely to `concepts/process-philosophy`.
     - No Many Worlds stays a commitment, not a datum.
3. **`topics/trilemma-of-selection` L113 and L115 (W3). Tenet 3, lens (b). Fold into the open P3 at todo L3724 (same file, same family) rather than minting a sibling.**
   - **Why it fails**: the resource-monitoring rival L113 itself states predicts effort calibrated to difficulty. The Map's effort page concedes this (`mental-effort` L88, L100) and shows felt effort dropping out with control intact (L80). L115 then says the pattern "answers" Planck and MacKay for effort.
   - **Length**: 3,402/4,000 (headroom 597).
   - (a) L113, last sentence
     - OLD: `Dismissing the pattern as illusion requires explaining why the illusion is so precisely calibrated to what selection would actually involve.`
     - NEW: `A cost-signal reading of effort predicts the same calibration ([[mental-effort#modulation|the process models]]), and felt effort can drop out while control stays intact ([[mental-effort#calibration|calibration]]), so the pattern fits genuine selection without discriminating it.`
     - Delta: +12.
   - (b) L115
     - OLD: `The systematic pattern above answers for effort alone, about which the self-observation limit predicts nothing.`
     - NEW: `The self-observation limit predicts nothing about effort, though the cost-signal reading above predicts its pattern.`
     - Delta: 0.
   - **Net**: +12 (3,402 → 3,414). Combined with todo L3724's L54 edit, keep the file within that task's ±20.
   - **Guards**:
     - Do not touch L76/L95/L140 (todo L3474) or Horn 2 (todo L3326).
     - Keep L113's "which is what genuine causal engagement would look like on the Map's reading" so that the Map's reading stays stated. Never concede epiphenomenalism. L115's next sentence ("On openness the Map has no answer to Planck or MacKay; its one discriminator … is statistical and untested") stands.
     - Both anchors exist (`mental-effort` "### Modulation" L86 and "### Calibration" L78, the lowercase forms the corpus already uses).
     - Do not use "resource" in the new text: L113's previous sentence is about the failed resource model of depletion.
4. **`topics/consciousness-and-skill-acquisition` L176 (W4). Tenet 1, lens (b). Carried from check 157 W13.**
   - **Why it fails**: "physically identical" bodies is false of the trained body the page documents. Transient hypofrontality is Dietrich's own neural account, so flow is a pattern the rival explains, not one it "must explain away".
   - **Length**: 3,754/4,000 (headroom 245).
   - OLD: `**[[tenets#^dualism|Dualism]]**: Skill acquisition reveals a gap between physical description and lived experience that property dualism predicts. Two bodies can be physically identical yet phenomenologically different—one a pianist's body, the other a non-pianist's—because the body schema carries a history of conscious engagement that physical description does not capture. Flow deepens this gap: the most vivid form of consciousness coincides with reduced top-down neural control (Dietrich, 2004—transient hypofrontality), a pattern dualism predicts but materialism must explain away.`
   - NEW: `**[[tenets#^dualism|Dualism]]**: Skill acquisition displays the gap between physical description and lived experience that the Map reads as irreducibility. Neural accounts describe how a pianist's body differs from a non-pianist's (remapped body schema, consolidated routines, myelination) without saying why the trained body feels as it does from inside. Flow sharpens the contrast: the most vivid form of consciousness coincides with reduced top-down neural control (Dietrich, 2004—transient hypofrontality), a pattern the Map's reading accommodates and Dietrich's own neural account explains, so it illustrates the gap without favouring dualism over its rivals.`
   - **Delta**: +14 (3,754 → 3,768).
   - **Guards**:
     - Keep the bold tenet link that opens the paragraph.
     - Do not touch L178 or the concessions at L116/L162/L166, per today's deep-review stability notes.
     - Dualism stays the Map's commitment, the "gap" stays stated, and nothing is conceded to identity theory beyond "explains the pattern".
     - The next paragraph opens with a fresh bold tenet subject, so no pronoun is stranded.

**Not tasked here:**
- W5 (evaluative-qualia L130, +3) and W6 (emotion-regulation L107 +2; probability-interpretation L97 +1) carry priced one-line fixes and are the first candidates when a slot opens.
- W7 is a scope addition to todo L3760. W8 goes to L3421 and L1913 (stapp is over its gate: net-negative only). W9 is wholly the tiebreaker NEEDS-HUMAN's (todo L94).
- Notes 8 and 9 are scope additions to L3769 and L2415. The other Notes are leads.
