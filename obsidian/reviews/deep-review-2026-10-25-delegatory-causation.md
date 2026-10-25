---
title: "Deep Review - Delegatory Causation (Closure Attribution, Route 1 Debts, Hub-over-Spoke)"
created: 2026-10-25
modified: 2026-10-25
human_modified: null
ai_modified: 2026-10-25T08:53:58+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[delegatory-causation]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-25
last_curated: null
---

**Date**: 2026-10-25
**Article**: [[delegatory-causation|Delegatory Causation]]
**Previous review**: [[deep-review-2026-07-18-delegatory-causation|2026-07-18]] (and 06-22, 06-06, 05-29, 04-22, 04-18)
**Word count**: 3490 → 3496 (+6; hard gate 3500 fires at >=, so 3 words of headroom remain)
**Pass type**: Changed-since-review verification plus a calibration check against what moved under the page (8th review).

## Why This Pass Ran

`last_deep_review` was 07-18. Since then, eleven commits touched the page. They include the Saad "predictive boat" quote restoration (07-31), the 182(3-4) issue fix (09-08), the Born-test-exposure clause (09-16), the inverse-access sentence (09-18), Schaffer's "Charge!" (09-19), trilemma non-exhaustiveness (09-27), the self-stultification sweeps (10-08 ×2, 10-15) and the Sorkin bound. Two pages also moved under it: the 10-03 "fourth cost" on [[trumping-preemption]], and today's apex calibration (f521c979), which scopes "dissolves" to sufficient-cause closure. The 10-25 Claude outer review also flagged that Saad's preemption is Route 1 of [[born-preserving-causal-efficacy]].

## Pessimistic Analysis Summary

### Critical Issues Found

1. **L174, closure misattribution and an internal contradiction. FIXED.** The paragraph said delegatory trumping "preserves" strong causal closure, and that Saad treats "closure-violating quantum interactionism as a *different* theory from closure-preserving delegatory dualism". Both L114 ("violates strict causal-closure") and L122 ("Delegation violates the former") say the opposite. Saad's text (PMC12062107, raw full text grepped) supports L114 and L122. He writes that "Sections 4 and 9 examine forms of dualism that respect Observational Closure while violating Closure", and that delegatory dualism "yields only unobservable violations of Closure". He classes quantum interactionism as violating *Observational* Closure: "nomically possible tests distinguish different collapse interpretations". The sentence now reads: trumping "is difference-making-free and violates closure only unobservably; Saad himself classes quantum interactionism, a different theory from delegatory dualism, as violating even *observational* closure." The 07-18 stability note's distinct-and-competing framing is kept intact (−2 words).
2. **L122, Tenet 2's qualifier was dropped. FIXED.** The page quoted Tenet 2 as producing no "empirically detectable" anomalies and called it a "parallel claim" to Saad's Observational Closure. The tenet's Rules-out clause (tenets L85) reads "empirically detectable under current experimental precision". That is weaker than Saad's nomic-possibility standard. The sentence now says "a weaker parallel claim" and quotes the clause in full (+5).
3. **L134, the hub was stronger than its spoke, and Route 1's symmetry debt was missing. FIXED.** The page said "the reliability of introspection is explained rather than merely assumed" and compared epiphenomenalism to "rejecting one that defeats its own evidence base". Two newer pages bound that claim:
   - Since 10-03, [[trumping-preemption]]'s fourth cost says that under the matching-profile law "the base yields the same report either way and accuracy rests on the lawful match, as for the bare-correlation epiphenomenalist".
   - The Born apex (L119) says "Preemption is symmetric … That consciousness is preemptor rather than preempted is a framework commitment … not something the causal structure delivers".

   A reviewer who accepts the tenets would still flag the old wording as overstated, so this is a calibration error and not bedrock. The paragraph now says three things:
   - Delegation meets the causal-traffic condition that L132 already installs.
   - On a difference-making condition it "fares no better than epiphenomenalism (trumping-preemption's fourth cost)".
   - "Preemption could also run the other way, so experience's authority over the brain state is the dualist's commitment, not the machinery's."

   The asymmetry is scoped to "the causal-traffic reading". This cost +25 words, funded mainly by merging L132's two redundant evidence sentences (−12, no qualifier cut).
4. **Lewis 1973 was an orphan reference. REMOVED.** Its metadata is correct (Crossref 10.2307/2025310, 70(17), 556–567), but nothing in the body cites it. "Lewis's influence response" at L65 is Lewis 2000. References are renumbered (−10).
5. **L150 kept a necessity verb the 09-27 trilemma repair missed. FIXED.** "The trilemma-of-selection establishes why this selection must be conscious" sat beside the repaired "of the usual options". The trilemma spoke calls itself "a heuristic not a complete partition" and says the selector move "is not *forced*". The line now says it "argues heuristically that this selection is conscious" (0). The matching Further Reading label ("Why selection … must be conscious") now mirrors the spoke ("Why only conscious selection at indeterminacies preserves authorship", 0).

### Medium Issues Found

- **L83, Source/Map conflation. FIXED.** "Saad's Organizational Invariance constraint offers indirect access" implied the constraint supplies the zombie route. Saad writes that it "entails the nomological impossibility of functional zombies … but it is consistent with their metaphysical possibility". The line now says it "bars zombies only nomologically, leaving indirect access" (+4).
- **L148, the Born-rule section. FIXED.**
  - The heading "Observational closure follows necessarily" now reads "follows by construction".
  - The ground is now delegation's own property: the experience causes only what the Born-rule default would have produced. It no longer rests on "selects *within* Born-rule probabilities", because a Born-preserving marginal leaves the conditionals free (apex horn (a)).
  - The page now says statistics are unchanged "at every grain", and the residual worry asks about no trace "at any grain" instead of "at the ensemble level". This matches the apex's "no predictively distinct claims at any scale" (−7).
- **L146. FIXED.** "The counterfactual becomes measurable" now reads "physically specifiable". The default profile is never observed in conscious systems (L77, L164), and the Sorkin bounds come from optical rigs, not neural tissue (+1).
- **Stranded dependents of the 10-08 lead fix. FIXED.** At L172, "self-undermining implications of epiphenomenalism" became "self-undermining charge against epiphenomenalism". At L178, "the self-undermining defect that epiphenomenalism's account of introspection creates" became "charge … faces" (0 each).
- **Further Reading label for conservation-laws. FIXED.** "violates neither conservation laws" became "need violate neither". The spoke says "Not on the classical argument" and leaves GR open (+1).
- **Description. FIXED (frontmatter, no word cost).** "solving the exclusion problem without overdetermination" became "a proposed answer to the exclusion problem, free of overdetermination but empirically silent". The body says "not proven superior" (L182), and the Born apex rates Route 1 coherent rather than compelling.
- **L176. Lead installed (+1).** "Saad's mechanism in the abstract" became "Saad's determinism-compatible mechanism in the abstract". This is the 10-25 Claude outer review's untasked lead. Delegation preserves the physical default, so it needs no indeterminism. The point is a structural consequence of the Subset Law* and Delegatory Law, not a quoted claim of Saad's.

### Citation Ledger (publisher of record)

- Saad 2025 (*A dualist theory of experience*, Phil. Stud.). State: **real-correct**.
  - Crossref gives vol. 182, issue **3-4**, pp. 939–967, doi 10.1007/s11098-025-02290-3. Issue 3-4 is kept, as briefed.
  - The quotes were grepped in raw PMC12062107 text: Subset Law* verbatim, Delegatory Law verbatim, "in the same predictive boat as epiphenomenalist dualism, overdeterminist dualism, and physicalism" verbatim, and "not a basis for sinking the boat or casting any of its passengers overboard" verbatim.
- Lewis 2000 (*Causation as Influence*). **real-correct**: 10.2307/2678389, 97(4), from p. 182.
- Lewis 1973 (*Causation*). **real-correct metadata, orphan, removed.**
- Schaffer 2000 (*Trumping Preemption*). **real-correct**: 10.2307/2678388, 97(4), 165–181. The "Charge!" and corporal wording is carried from the 09-19 publisher-PDF verification and was not re-fetched.
- Kim 2005 (*Physicalism, or Something Near Enough*, Princeton). **real-correct**. Inline it appears by name only ("Jaegwon Kim's exclusion argument").
- Torres Alegre 2025 (arXiv:2512.12636). **real-correct**: Enso O. Torres Alegre, submitted 2025-12-14. The full title adds the subtitle "A Derivation from Steering in Generalized Probabilistic Theories", which the reference omits; this is not an error. The preprint caveat is intact.
- Kauten et al. 2017, behind the Sorkin link ("near 10⁻⁴"). The arXiv:1508.03253 abstract says "more than four orders of magnitude smaller than the expected pairwise interference". **Result direction correct.** No superlative is claimed, and `find_superlative_claims` returned nothing.
- Tenet 2 quotes. "without injecting energy or violating conservation laws" is verbatim (tenets L65). "empirically detectable" was truncated and is now quoted in full from L85.
- (surname, year) cross-check after the fix:
  - Lewis: one work, cited by name.
  - Schaffer (2000) appears at L63 and in References.
  - Torres Alegre (2025) appears at L148 and in References.
  - Saad (2025) appears throughout.
  - Kim: one work, cited by name.
  - No orphans remain in either direction.
- Cited-author stance:
  - Saad is a dualist building theory. He keeps Closure as "a working hypothesis" and sets quantum interactionism aside as "not the project of this paper". The page marks the Born identification (L140) and the no-MWI requirement (L176) as the Map's, not his.
  - Schaffer and Lewis are cited for causal structure only, with no dualist stance imputed.
  - Torres Alegre is cited as a compatibility result.

### Reasoning-Mode Classification (editor-internal)

- Epiphenomenalism. The engagement was Mode One and is now **Mixed**: Mode One on the causal-traffic reading, and an honest boundary-marking (Mode Three) on the difference-making reading and on the direction of authority.
- Strict empiricist (L136): **Mode Three**, unchanged.
- Physicalist mirror move (new, L134): **Mode Three**. The direction of authority is declared a dualist commitment, not something the machinery delivers.
- Forbidden-label grep: none in prose.

### Counterarguments Considered

- Mirror-move physicalism (the brain state trumps the experience). This is now stated (L134).
- Probabilistic closure. Physics already fixes the Born distribution, so the experience is chance-idle. L148's "only riding the distribution physics already fixes", together with "efficacy is a structural property, not a statistical one", carries the chance-fixing concession. Probabilistic closure is not claimed dissolved.

## Sweep-Repair Checks

- **09-27 trilemma non-exhaustiveness.** "of the usual options" HELD at L150. A necessity verb at the same locus was stranded, and the Further Reading label also said "must". Both are fixed.
- **10-08 lead ("self-undermining charge against").** HELD in the lead. The anchor `^tenet-3-epiphenomenalism` exists at tenets L101. Two dependents (L172, L178) still used the old flat wording and are now fixed.
- **10-08 pessimistic-review anchor fix (`^tenet-3-standing` → `^tenet-3-epiphenomenalism`).** HELD.
- **10-15 second sweep (L132 conditional; Honest Limitations "risks").** HELD verbatim. The downstream L134 sentence "rejecting one that defeats its own evidence base" was still unconditional; it is now scoped to the causal-traffic reading.
- **Description and headings.** Neither carried the self-stultification refutation. The description's "solving" is now scoped, as above.

## Route 1 and Probabilistic-Closure Checks

- **Born apex Route 1 debts.** The page states four of them:
  - Predictive equivalence with epiphenomenalism (L124, L128).
  - Silence at every grain (L148, as amended).
  - Framework-internal rating (L148).
  - Direction-of-authority symmetry (L134, new). This one was missing before this pass.

  It claims to discharge none of them. It is now no stronger than the apex.
- **Probabilistic closure.** The page does not claim closure is dissolved. Saad's own exclusion answer is unobservable violation of sufficient-cause Closure, which L114 and L122 state correctly. The Born-identified variant's probabilistic remainder is the L148 residual worry.
- **P-Q2 quantifier.** The page stays neutral. "Unchanged at every grain" is stated of delegation (Route 1, which declines distributional change) and not of the MQI default reading. The MQI paragraph keeps the two mechanisms distinct.

## Optimistic Analysis Summary

### Strengths Preserved

- The epistemic, conditional register of the self-defeat argument (L132, untouched).
- The MQI-tension framing (07-18 stability note). It is now stated accurately against Saad's text, not weakened.
- The Torres Alegre preprint caveat.
- The Born identification flagged as Map-specific.
- The inverse-direction paragraph's refusal of a fourth access route.

### Enhancements Made

- Route 1's symmetry cost and the trumping template's fourth cost are carried into the hub.
- Saad's Closure and Observational Closure classification is now faithful.
- Tenet 2's precision qualifier is restored.
- Navigation labels are aligned with their spokes.

### Cross-links Added

- [[trumping-preemption]] gains a second, targeted body link at L134.

## Remaining Items

Leads only. None are edited here, because they are out of scope:

- **The closure misattribution has siblings.** "closure-preserving delegatory dualism" or "preserves strong causal closure" also appears in:
  - `topics/delegation-meets-quantum-selection` L92
  - `concepts/trumping-preemption` L89
  - `apex/interface-specification-programme` L110
  - `apex/research-programme-decisions-under-the-map` L112
  - `apex/dualism-cartography` L93 ("keeps the physical cause fully sufficient", which needs reading in context)

  Saad says delegatory dualism violates Closure unobservably.
- **`concepts/observational-closure` L106** has the same dropped "under current experimental precision" qualifier.
- **`topics/delegatory-dualism` L108** calls the "Charge!"/one-corporal case "Saad's analogy". Saad's own version is "When a major and sergeant order their troops to advance". The 09-19 Schaffer fix appears to have overwritten Saad's analogy with Schaffer's.
- **`topics/delegatory-dualism` L94 area** carries the same "Organizational Invariance constraint offers" zombie wording.
- **`topics/delegatory-dualism` §Relation to Quantum Interactionism (L200–206)** still uses the pre-07-15 "compatible … biasing would constitute delegation" framing that the hub abandoned. Here the spoke is *weaker* in honesty than the hub.
- **Archive (not edited, NEEDS-HUMAN publication policy).**
  - `archive/concepts/causal-delegation.md` carries "reliability of introspection is explained", "self-undermining implications of" and the truncated "empirically detectable" quote.
  - `archive/concepts/default-causal-profile.md` carries "Organizational Invariance constraint offers".
  - `archive/concepts/preemption.md` carries "solving the exclusion problem".
- **Length.** The page sits at 3496 against 3500. The next sibling cross-link will tip it over. The queued P3 condense task (filed against `topics/delegatory-dualism`) is the right place to recover headroom.

## Stability Notes

- All prior stability notes stand. Empirical underdetermination is bedrock. The MWI rejection is essential for the bridge. Constitutionalist dissent is expected. Q1 is open. Do not re-inflate the epistemic register into a logical one. The Torres Alegre caveat must stay. The MQI tension must stay.
- **New: delegation's advantage over epiphenomenalism is conditional on the causal-traffic reading.** Do NOT restore "the reliability of introspection is explained" unqualified, and do NOT drop the difference-making concession. Both are owed to [[trumping-preemption]]'s fourth cost.
- **New: the direction of authority is a dualist commitment.** Do NOT remove the symmetry sentence. It is the Born apex's Route 1 debt, and the hub must not be stronger than the apex.
- **New: Saad's closure classification is textual, not interpretive.** Delegatory dualism violates Closure only unobservably, and quantum interactionism violates Observational Closure. Do NOT reintroduce "closure-preserving delegatory dualism".
- A physicalist who finds authority-without-difference-making unpersuasive is at bedrock. That is now honestly marked, not a defect.
