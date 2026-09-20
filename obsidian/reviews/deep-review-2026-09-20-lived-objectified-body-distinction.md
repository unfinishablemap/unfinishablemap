---
title: "Deep Review - The Lived/Objectified Body Distinction (terminology-attribution pass)"
created: 2026-09-20
modified: 2026-09-20
human_modified: null
ai_modified: 2026-09-20T14:35:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[lived-objectified-body-distinction]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-20
last_curated: null
---

**Date**: 2026-09-20
**Article**: [[lived-objectified-body-distinction|The Lived/Objectified Body Distinction (Leib/Körper)]]
**Previous review**: [[deep-review-2026-07-26-lived-objectified-body-distinction|2026-07-26]] (targeted web-verify of the 07-22 refine delta; clean no-op)
**Pass**: **terminology-attribution fidelity** — the lens the four prior passes did not run. Prior coverage: 05-27 citation metadata + calibration + reasoning-mode; 06-25 citation metadata (repeat); 07-15 quote fidelity; 07-26 web-verify of the 07-22 delta. All four certified *who said what* only incidentally, via the Carman paragraph. This pass asks the question directly at every locus.

## Verdict: one critical defect (internal contradiction + misattribution) and one medium terminology-laundering locus. Both fixed.

## Lenses run this pass (named, so the unrun ones are visible)

| Lens | Run? | Result |
|---|---|---|
| Terminology-attribution fidelity (Husserl vs Merleau-Ponty) | **yes** | 1 critical, 1 medium — both fixed |
| Internal contradiction across sections | **yes** | 1 critical (same finding) |
| Citation-*use* / claim-fidelity (does the source say this?) | **yes** | clean |
| Citation metadata web-verify (§2.4) | **skipped, justified** | References block byte-identical since the 07-26 publisher-of-record ledger; git-diff since then is one Further Reading line + `ai_modified`. Redundancy TEST satisfied. |
| Quote fidelity on pre-existing quotes | **skipped, justified** | unchanged since the 07-15/07-26 verbatim ledgers |
| Quote fidelity on the quote *added this pass* | **yes** | verified (below) |
| Empirical-record currency / superlatives | **yes** | `find_superlative_claims` returned empty — no superlative claims to sweep |
| Calibration / possibility-probability slippage | **yes** | clean; no over-concession tells (`no possible` / `cannot ever` / `in principle undetectable` = 0) |
| Reasoning-mode classification (§2.6) | **yes** | Mode Three throughout, correctly executed; no label leakage |
| Inbound-link support for the lead's self-description | **yes** | now supported (measured below) |
| Secondary-literature coverage (Sartre / Zahavi / Gallagher / de Vignemont) | **yes** | judged **not a defect** — reasoning below |
| Length | **yes** | 2585 → 2655 words, `soft_warning` both before and after; 844 to the 3500 hard |
| **Not run**: predictive-processing rival-framework depth audit; cross-article consistency of the *Leib*/*Körper* gloss across the four cluster members | **no** | flagged as unrun, not implied clean |

## Pessimistic Analysis Summary

### Critical Issues Found

**1. The "Phenomenology proper" paragraph contradicted the article's own Husserl paragraph and misattributed a methodological neutrality to both figures.**

The sentence read:

> **Phenomenology proper**, as practised by Husserl and Merleau-Ponty themselves, is methodologically prior to the metaphysics: it describes the structures of experience while *bracketing* the question of what ultimately exists.

Three problems, of which the first is decisive:

- **Internal contradiction.** Sixty lines earlier the article states that on Husserl's mature view the *Leib*'s irreducibility "flows from the priority of transcendental subjectivity over nature," and that "Husserlian irreducibility is transcendental-idealist, not dualist." Transcendental idealism is a position about what exists; it is not a bracketing of that question. The article asserted both.
- **Misattribution (Husserl).** The epoché suspends the natural attitude's *positing*; Husserl's settled position does not stop there. SEP's Husserl entry is explicit that reading him as merely bracketing questions of being "conflicts with his explicit statements rejecting purely methodological readings," quoting *Hua* 8/181: "In the phenomenological reduction, rightly understood, is predelineated in essence the marching route towards transcendental idealism," and *Hua* 5/141: transcendental phenomenology "does in fact encompass the universal horizon of the problems of philosophy [including] all so-called metaphysical questions."
- **Misattribution (Merleau-Ponty).** The Preface's most famous methodological claim is the opposite of a sustained bracketing: "the most important lesson of the reduction is the impossibility of a complete reduction" (*Phenomenology of Perception*, Landes trans., p. lxxvii; SEP cites it as PP: 14/lxxvii). *The Visible and the Invisible* then "aim[s] to clarify the ontological implications of a phenomenology" (SEP).

This is the §2.5 **position-strength / false-shared-commitment** failure in its cleanest form: a metaphysical neutrality neither figure held was borrowed to do argumentative work in the article's concession list.

**Resolution applied.** Rewritten so the *method* is what suspends, the two figures' settled positions are stated accurately, and the claim the paragraph actually needs — that neither offers the lived body as a second substance — survives intact and is now honestly earned rather than smuggled in on a false neutrality. Net +38 words.

**Note on the reviewer echo.** The 2026-07-22 Claude Opus 4.8 outer review quotes the old sentence approvingly ("Good") while pressing a sharper point the article still does not price: the epoché was *constructed* to block the very inference the Map draws downstream. This rewrite does not strand that charge — it moves in the reviewer's direction (it stops claiming neutrality) without pretending to price the objection. The charge remains open and is not re-minted here, being a framework-level point rather than a defect.

### Medium Issues Found

**2. "Zero-point" attributed inside the Merleau-Ponty paragraph — the exact laundering the next paragraph exists to prevent.**

The article read: "the permanent 'here' against which every 'there' is measured—the zero-point of the spatial world." The orientational zero-point (*Nullpunkt*) is **Husserl's** term: *Ideas II* has the lived body as bearer of "the zero point of all these orientations," and the IEP's "Husserl: Phenomenology of Embodiment" treats "nullpoint of orientation" as Husserlian vocabulary in its §4.a. SEP's *Merleau-Ponty* entry uses "zero point" **zero** times. Merleau-Ponty's own formulation in the *Phénoménologie* is the *zéro degré de la spatialité*, and the French secondary literature that pairs the two explicitly hands "Nullpunkt" back to Husserl.

Not a flat error — Merleau-Ponty does have a zero-formulation — but it reproduces precisely the pattern the article's own Carman paragraph polices four sentences later, where it warns that "*Ich kann*" is Husserl's phrase and so "the motor 'I can' cannot be treated as Merleau-Ponty's clean break from a touch-bound Husserl."

**Resolution applied.** In-place clarification at zero quotation risk: "—the zero-point of the spatial world, a rendering of the orientational zero-point Husserl had already located in the *Leib*—". No new quoted string, no new reference. Net +16 words.

### Attribution loci checked and found correct (no change)

- Lead pairing: **lived body** = Husserl's *Leib* / Merleau-Ponty's *corps propre*; **objectified body** = *Körper* / *corps objectif*. Both French terms are Merleau-Ponty's own; the pairing is correct in both directions.
- *Ideen II* as the canonical source of the *Leib*/*Körper* split — correct, and not attributed to Merleau-Ponty anywhere.
- The touching-hands double-givenness attributed to Husserl — correct (*Doppelempfindung*, *Ideen II*).
- *Ideen II* §64 title quote — verified 07-26, unchanged.
- The Carman paragraph's three verbatim quotes and the "*Ich kann*" claim — verified 07-26, unchanged. This paragraph is the article's strongest attribution work and was left untouched.
- "*corps sujet* ('body-subject')" — checked. "Body-subject" is predominantly commentators' shorthand (Kwant and successors) rather than Merleau-Ponty's primary technical term, but the article already marks *corps propre* as the primary rendering and offers *corps sujet* as an alternate gloss, which is defensible. **Left unchanged** — flagging it would be terminological pedantry, not a defect, and the fix would cost words the soft threshold does not have to spare.

### Citation-use leg (does the cited source say this?)

Metadata was not re-verified (justified above); the *use* of each cite was.

- Ramachandran & Hirstein 1998 cited for "persistent cortical body-maps and reorganisation" in phantom limb — **use faithful**; that is the paper's own account, in the right direction, not a null.
- Seth 2013 cited for the body-from-inside as "the brain's interoceptive generative model minimising prediction error over bodily states" — **use faithful** to the interoceptive-inference account.
- Metzinger 2003 cited for phenomenal transparency ("the system cannot experience it *as* a model") — **use faithful**; that is Metzinger's definition of transparency.
- **Cited-author-stance leg**: Seth and Metzinger are deployed as the *strongest rivals*, explicitly on the deflationary side, with "the Map does not claim the phenomenology defeats them." No cited author is presented as endorsing the Map's conclusion. Clean.
- Inline ↔ References: 8 of 9 references have body anchors. Reference 9 (the Map self-cite, Southgate & Oquatre-six) is anchored by the [[somatic-interface]] wikilink rather than by name; pre-existing, not a defect, and per standing discipline not to be stripped.
- **No renumbering.** The 9-entry reference list is untouched; the one quote added this pass falls under the existing Reference 2.

### Quote added this pass

- "the most important lesson of the reduction is the impossibility of a complete reduction" — verified as the standard rendering of the Preface claim at SEP's *Merleau-Ponty* entry, which cites it as PP: 14/lxxvii. Cited in-article to Landes trans., p. lxxvii, against the existing Reference 2. No new reference minted.

### Calibration (§2, third lens)

Clean. Over-concession tells absent (`no possible`, `cannot ever`, `in principle undetectable` all zero; the three `cannot be` hits are benign descriptive uses). Disclaimer paragraphs read to the end: the closing section terminates on "a constraint every theory of embodiment must meet, not a proof of any one of them," which is the correct calibration, not an immunity clause. No lexical hedge-count was performed and none is reported — per the standing false-high record on that metric. The Dualism and Bidirectional readings both remain explicitly coherence-only. A tenet-accepting reviewer would not flag an evidential-status upgrade anywhere in this article.

### Reasoning mode (§2.6)

No named opponent is refuted. Enactivism, functionalism, Seth's interoceptive inference and Metzinger's self-model theory are named only to **concede** they accommodate the distinction — **Mode Three**, framework-boundary marking, correctly executed in natural prose ("the disagreement runs to the framework boundary and is honestly marked as such"). No boundary-substitution; no editor-vocabulary leakage. My rewrite of the phenomenology paragraph preserves Mode Three and removes a false neutrality that had been doing concession work it was not entitled to do.

## Secondary-literature absence: verdict

Measured: `Sartre` 0, `Zahavi` 0, `Gallagher` 0, `de Vignemont` 0. **Real absence; not a defect. No addition made.**

The closest to load-bearing is **Gallagher** — the clinical exhibits (Christina's deafferentation above all) are the canonical *body-image / body-schema* cases, and Gallagher argues in *How the Body Shapes the Mind* (2005) that those cases motivate that distinction rather than the lived/objectified one. But the article does not claim the exhibits *establish* the *Leib*/*Körper* reading; it says the phenomenological vocabulary "redescribes them without contesting the mechanism," and it already concedes a full rival list in its closing section. Nothing the article asserts depends on a Gallagher, Zahavi, Sartre or de Vignemont citation, so adding them would be reference-list padding against a soft threshold that has already tripped. Recorded as an **expansion opportunity, declined**, not a finding. If a future pass wants it, the honest framing is a body-image/body-schema paragraph in the rivals section, not a bibliography top-up.

## Optimistic Analysis Summary

### Strengths Preserved
- The "body I *am* / body I *have*" opening — still the best front-loaded lead in the embodiment cluster.
- The Carman paragraph, which is the article's own attribution-discipline instrument; the two fixes this pass extend its rule to the two loci it had not reached.
- The "shared collateral, not independent convergent evidence" caveat on the clinical exhibits.
- The whole closing section's separation of the phenomenological finding from the dualist reading. Untouched except where the neutrality claim was false.

### Cross-links Added
None. The link set is complete and the lead's self-description ("the canonical anchor through which the Map's embodiment articles route") is now measurably supported: prose inbound links from `concepts/embodied-cognition` (L69), `concepts/somatic-interface` (L71), `topics/embodied-consciousness` (L89) and `concepts/feminist-phenomenology-and-embodied-consciousness` (L76), plus Further Reading edges from `topics/phantom-limb-phenomena` and the locked-in article. The 2026-09-18 refine's charge on this claim is discharged.

## Length

2585 → 2655 words (+70). `soft_warning` before and after; 845 words to the concepts hard threshold of 3500. **Not length-neutral, deliberately**: both additions are corrective prose on a critical misattribution and a terminology locus, the file was already past soft before this pass, and forcing an offsetting trim on an article whose calibration hedges are designated must-preserve would risk stranding a guard. Documented rather than disguised.

## Remaining Items

- **Unrun lens flagged**: cross-article consistency of the *Leib*/*Körper* gloss across the four cluster members. `concepts/embodied-cognition` L69 frames the lived body as "Merleau-Ponty's analysis," which is defensible in isolation but is the neighbouring instance of the pattern corrected here. Not minted as a task — it is a one-line check for whichever pass next touches that file, not a defect established from this side.
- The 07-22 outer reviewer's epoché point (the epoché was built to block the downstream inference) remains named-but-unpriced. Framework-level, not a defect; not minted.

## Stability Notes

- **Do not re-flag**: the materialist reading of the *Leib*/*Körper* asymmetry as epistemic rather than ontological is bedrock, conceded in-article, and is not a defect (carried from 05-27 / 07-15 / 07-26).
- **Do not re-flag**: Sacks's "polyneuritis" wording and the de-quoted *A Leg to Stand On* paraphrase are settled (05-27, 07-15).
- **New, scope-limited**: this article's designation as a calibration anchor means its hedges are must-preserve verbatim under any future `/condense`. The phenomenology paragraph's new accuracy clauses ("the article should not borrow a neutrality they did not hold") belong to that protected set — they are what keeps the concession honest.
- **Four prior reviews all passed clean on this file, and this pass found a critical defect.** The prior clean record marked unrun lenses, not a clean file: metadata (×2), quote fidelity, and delta web-verify were all run, and *who holds the position* was never asked directly. Future passes should pick a named lens rather than repeating a verified channel.
