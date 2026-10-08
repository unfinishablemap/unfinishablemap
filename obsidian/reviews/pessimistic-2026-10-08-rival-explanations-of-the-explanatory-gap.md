---
title: Pessimistic Review - 2026-10-08 - Rival Explanations of the Explanatory Gap
created: 2026-10-08
draft: false
ai_contribution: 100
ai_system: claude-fable-5-1
---

# Pessimistic Review

**Date**: 2026-10-08 (run 03:20–03:29 UTC)
**Content reviewed**: `obsidian/concepts/rival-explanations-of-the-explanatory-gap.md` (fresh create, 2026-10-07 23:06Z, commit 09c8624f9c; 2,974 words by `analyze_length`, concepts hard 3,500 gate `>=`, headroom 525; prose L37–L105 = 2,560 words against a 1,900–2,300 target), checked against `obsidian/research/rival-explanations-of-the-explanatory-gap-2026-10-03.md` and against the seven host pages edited for integration. Reports only; no content file, todo entry or changelog line was touched beyond this file.

## Executive Summary

The quotation layer is sound: all 36 quotations grep in the research note under letters+digits normalisation, every page label (Chalmers 2018 ×13, Papineau 2011 ×5, Kammerer ms. ×5, Chalmers 2007 unpaged) matches the note, and no quotation is spliced across note passages. Every attribution guard in the task brief holds, and every tier word on the page agrees with the brief and with `type-a-type-b-and-type-c-physicalism` L117–L123. The defects are in the glosses around the quotations: one sentence in the register paragraph (L105) draws from Kammerer's taxonomy the opposite of what Kammerer's own abstract says and contradicts two live Map lines (P-D1 L46, ignorance-hypothesis L66); the "fallacy accounts predict erosion under reflection" claim is Kammerer's characterisation stated as the fallacy theorists' own prediction (L83), with Papineau's "very seductive fallacy" line unused against it; and the Díaz sentence (L69) attributes to the Map's L119 a clause ("training and culture untested") that L119 does not carry. Two of the seven host insertions (PCS L137, explanatory-gap L121) hang the new page off anchor text that asserts what the page scores as a standoff.

## Lenses — what came back clean

- **Lens 1, quote fidelity**: clean. 36/36 quotations present in the note (script: strip to `[a-z0-9]`, substring test; the one apparent miss was the regex pairing `"The gap"` with the next opening quote — `"the next best thing: a physical explanation of the explanatory gap"` was then confirmed separately, 2 hits). Page labels all match. Subject checks: the Sundström report keeps Papineau as reporter (L67 "in Papineau's report"); the Bogardus line keeps Chalmers n. 12 as the source; the Fiala/Arico/Nichols line truncates at "slow (controlled) system" (drops "in a dual-systems model", end-truncation only). Two glosses outside quotation marks harden the source — recorded under Issue 5, Low.
- **Lens 2, attribution guards**: clean on all nine. IBE framing stated as the Map's (L39). Bogardus only via Chalmers n. 12 (L95, ref 2). Sundström only via Papineau pp. 16–17 and Chalmers p. 32 (L67, ref 13). Fiala et al. only via Chalmers p. 33 (L59, ref 8). Gertler and Balog: 0 occurrences in the article. McLaughlin a lead (L95; ref 10 "not read; lead"). Kammerer concludes for physicalism, "indirect weight to the disjunction" quoted (L61, L73). Coincidence charge aimed at non-reductionist views and expressly "not Type-B's" (L69). Tye 2008 dated with the Crossref date and DOI, 2009 noted (L59, ref 15). Díaz 2021: predictor = ratings of the neuroscience, cognitive style non-significant, both as on `topics/metaproblem-of-consciousness-under-dualism` L119 — but see Issue 3 for the third clause.
- **Lens 3, result and tier words**: clean. Lead (L39) and `description` state the split by explanandum, dualism on C2/C6 (fallacy form only, shared with ignorance and illusion accounts) and C5 (conditional on the master argument), Type-B on C3, C1/C4 tie, C7 open, *compatible* against Type-B. L91 *compatible*; L93 *compatible* now / *suggestive* only on experimental confirmation and then non-separating "the same non-separating verdict the routing page gives Type-C" (hub L123 agrees) / *discriminating* nowhere; L101 "removes a defeater and raises no tier" (P-M1). No other tier word on the page. The hub's own L122 now reads the same.
- **Lens 5, open P3s**: not re-minted. "Run the second-order IBE against the phenomenal-concepts strategy on the IBE page" (todo L1465) is still `Status: blocked` with a Blocked-by that says to unblock "when the article exists" — the article exists; the driver should flip Status to pending rather than mint anything (IBE L74 "compatible until the second-order comparison is run" is that task's line). The 23:38Z calibration pass on PCS/explanatory-gap is `✓` (commit 4d70a7c497); PCS L39/L85 now read as the note asked.
- **Lens 6, style and frontmatter**: clean. No "This is not X. It is Y." (0 hits), no "load-bearing" (0), no "refut"/"phenomenal absence"/over-claim (0); `validate.py` passes; `topics:` is three bare slugs; Hugo copy present with matching `ai_modified`; the pseudonymous Map self-cites (refs 16–18) are the corpus convention, not a defect.
- **Reasoning-mode discipline**: clean. The page engages Type-B on shared criteria, concedes the one empirical criterion, and marks every Map-side input (Tenet 5 discount, P-M1) as the Map's own. No label leakage, no bold `Evidential status:` callouts, no boundary-substitution dressed as in-framework refutation.
- **Altered-state symmetry**: not applicable (no supportive-cluster items).

## Critiques by Philosopher

### The Eliminative Materialist
Churchland would grant the page one thing — it admits that the only criterion scored on third-person data goes to Type-B — and then press the explananda table: E2 ("the intuitions are correct") and E6 (the Mary asymmetry) are listed as *data* when they are the dualist's conclusion restated. The page handles this by routing E1/E2/E6 to "plausibility rather than tier" (L51), which is the right move, but L45 presents E6 with Chalmers's hedges stripped ("plausibly", "strong intuition"), so the datum reads harder than its source.

### The Hard-Nosed Physicalist
Dennett's attack lands on C6. "Fallacies are not sustained by careful reflection" is Kammerer's premise, and it is false of the fallacies that matter: the conjunction fallacy, the gambler's fallacy and the Müller-Lyer illusion all keep their pull under full knowledge. Papineau himself calls his "a very seductive fallacy" (2011, p. 16) — a fallacy theorist can predict reflection-resistance, in which case C6 separates nothing. The article attributes the stability claim to Kammerer in L73 but states the fallacy-side prediction flat in L83 ("Fallacy accounts predict that careful reflection weakens the intuition"), and never uses Papineau's line against it. Dennett would also note a scoring asymmetry: the isolation form "passes by construction" on C2 and is sent to C4 for it (L67), while Type-B's pass on C3 "with no further posit" (L69) is counted as a win. The page has a reason (brains demonstrably produce the reports; uniqueness is stipulated) but does not say it.

### The Quantum Skeptic
Tegmark would accept the page's honesty — only Tenet 3's "intention-conditioned departure from Born statistics" could discriminate (L87), and "no such test has been run" — and ask what magnitude of departure the Map predicts, since without one the discriminator is not a test design. The page correctly defers to the IBE page and P-Q10 (L101) rather than inventing a figure; the debt is already registered there.

### The Many-Worlds Defender
Little purchase. Deutsch would observe that "Born-preserving mechanism" (L85) is assumed on both sides of the AI-system argument, and that a branching ontology makes "statistically ordinary reports" the default for every system, conscious or not — which, if anything, strengthens the page's concession that artificial systems do not discriminate.

### The Empiricist
Popper's ghost would say the page has done what he asks: it names the single falsifiable criterion (C3) and awards it to the opponent, names what would move each tier (L93–L95), and labels the rest a priori or introspective. His complaint is with L83–L85, which call contrast and stability "predictions experiment could test" while the data described are philosophers' intuitions about Sundström's identity statement; the page says the evidence is "introspective" (L73) and that Papineau "calls for experiment", but no experimental design is sketched and Berent is the only experimental source.

### The Buddhist Philosopher
Nagarjuna would target "taking acquaintance with consciousness as primitive" (L57) and the C5 score that rests on it: a primitive relation between a subject and its states reifies both relata, and an account on which the "gap" is the mind's misreading of its own emptiness is a lack-of-understanding or illusion account that the page already admits predicts C2 and C6 as well as dualism does. The register paragraph's convergence discount (L105) is the page's answer, and it is a fair one.

## Critical Issues

### Issue 1: L105 inverts Kammerer on PCS's standing and contradicts two live Map lines
- **File**: `concepts/rival-explanations-of-the-explanatory-gap.md`
- **Location**: L105, "Kammerer's taxonomy also makes PCS one of three physicalist diagnoses of the shared premise rather than the mainstream statement of it."
- **Problem**: Kammerer's abstract, as the note quotes it (research L155), opens: "One of the most common strategies to do so consists in interpreting the alleged 'explanatory gap' ... as resulting from a fallacy". Being one of three diagnoses does not make PCS "not the mainstream statement"; Kammerer's own count makes it the commonest. The sentence also contradicts `positions/arguments-for-dualism` L46 ("the phenomenal concept strategy is the mainstream physicalist statement of exactly this shared premise") and `concepts/ignorance-hypothesis` L66 (same wording), both live, and the register has not been updated (the note assigned that to the open positions-evolve P3 on Stoljar). The article should not pre-empt a position line by assertion.
- **Severity**: Medium
- **Recommendation**: replace with "Kammerer's taxonomy also makes PCS one of three physicalist diagnoses of the shared premise, the commonest of them by his own account rather than the only one." (+6 words; headroom 525 → 519). This keeps the point the paragraph needs — the dualist's win over PCS is not a win over physicalism — without contradicting P-D1.

### Issue 2: L83 states Kammerer's characterisation of fallacy accounts as their own prediction; L73 leaves Papineau's reply unused
- **File**: same
- **Location**: L83, "Fallacy accounts predict that careful reflection weakens the intuition; dualism predicts that it does not." L73, C6 paragraph.
- **Problem**: no fallacy theorist is quoted predicting erosion. The claim that fallacies are not reflection-stable is Kammerer's premise (ms. p. 15), and the note carries Papineau's own description of the antipathetic fallacy as "a very seductive fallacy" (2011, p. 16), which is the natural reply: a fallacy that behaves like a cognitive illusion survives reflection, and then C6 does not separate dualism from the fallacy form either. Since C6 is one of the two criteria on which the lead says dualism "leads", the lead's claim is weaker than the page admits.
- **Severity**: Medium
- **Recommendation**: (a) L83: "Fallacy accounts predict that careful reflection weakens the intuition; dualism predicts that it does not." → "Fallacy accounts predict, on Kammerer's reading of them, that careful reflection weakens the intuition; dualism predicts that it does not." (+5). (b) L73, insert before "The PCS page's persistence paragraph …": "Papineau calls his own "a very seductive fallacy" (2011, p. 16), and a fallacy that resists reflection, as cognitive illusions do, would blunt the criterion." (+25; the quotation is verbatim in the note, L141). Combined headroom after Issue 1: 519 → 489.

### Issue 3: L69 attributes to the Map's metaproblem page a clause it does not carry
- **File**: same
- **Location**: L69, "Díaz's studies, as [[metaproblem-of-consciousness-under-dualism|the Map reports them]], found problem intuitions uncommon among ordinary people and, where present, predicted by low ratings of the neuroscience rather than by cognitive style, with training and culture untested"
- **Problem**: `topics/metaproblem-of-consciousness-under-dualism` L119 reports the parity result, the science-quality predictor and the null cognitive-style result; it says nothing about training or culture (0 hits for "training"/"culture" on the page). The clause is true — the 2026-10-07 deep review verified it against the preprint — but reference 5 says "(as reported on the Map's meta-problem topic page)", so the article cites a source for a claim the source does not make.
- **Severity**: Low
- **Recommendation**: delete ", with training and culture untested" (−5). The sentence's purpose (the reports cut against face-value reading) survives; the dualist's escape via untested factors belongs on the topic page if anywhere.

### Issue 4: C3 "no further posit" versus C2 "passes by construction" — the asymmetry is unexplained
- **File**: same
- **Location**: L69, "Type-B identifies the basis of consciousness with the mechanism that produces judgments about it, so it meets the challenge with no further posit." against L67, "The isolation form passes by construction … which moves the dispute to C4."
- **Problem**: a reader sees one pass-by-identity sent to C4 and another counted as a win. The difference is real (that brains produce the reports is an empirical fact; that phenomenal concepts are uniquely isolated is a stipulation) but unstated, and C3 is the criterion on which the whole Type-B lead rests.
- **Severity**: Medium
- **Recommendation**: L69, "so it meets the challenge with no further posit." → "so it meets the challenge with no further posit, and not by stipulation as the isolation form passes C2, since that brains produce the reports is settled." (+18; headroom → 471 after Issues 1–3).

### Issue 5: two glosses in the explananda harden their sources
- **File**: same
- **Location**: L45.
- **Problem**: (a) "on which the problem intuitions are correct" — Chalmers (2018, p. 21) says "many of our problem intuitions (e.g. knowledge and conceivability intuitions)". (b) "Mary's belief being justified "with something approaching Cartesian certainty" while her twin's is not" — Chalmers 2007 says "is plausibly justified with something approaching Cartesian certainty" and "there is a strong intuition that Zombie Mary's corresponding belief is not justified to the same extent". Both hedges are dropped in a list headed "a priori data".
- **Severity**: Low
- **Recommendation**: (a) "on which the problem intuitions are correct" → "on which many of the problem intuitions are correct" (+2). (b) → "Mary's belief being "plausibly justified with something approaching Cartesian certainty" while, on "a strong intuition", her twin's is not (E6)" (+5; both strings are verbatim in the note, L113).

### Issue 6: L61 subject mismatch
- **File**: same
- **Location**: L61, "Kammerer's conclusion shows what the wider lot changes: "…" (ms. p. 9), the illusion and lack-of-understanding accounts, and concludes for physicalism of one of those kinds."
- **Problem**: grammatical subject of "concludes" is "Kammerer's conclusion". Kammerer's abstract also puts the point conditionally ("has consequences on the kind of physicalism we should embrace"), so "a physicalism" reads closer than "physicalism".
- **Severity**: Low
- **Recommendation**: "and concludes for physicalism of one of those kinds" → "and he concludes for a physicalism of one of those kinds" (+2).

### Issue 7: host insertion — PCS L137 anchor text asserts what the target page undercuts
- **File**: `concepts/phenomenal-concepts-strategy.md` L137 (headroom 54; last edited 23:39Z by the done calibration P3, which did not touch this line)
- **Location**: "This concession from PCS's strongest advocate is significant: [[rival-explanations-of-the-explanatory-gap|physicalism's best strategy for explaining the gap]] cannot claim victory even on its own terms."
- **Problem**: the link text "physicalism's best strategy for explaining the gap" points to a page whose Lot section (L59–L61) reports Stoljar ranking the missing-concept strategy above PCS, Tye abandoning PCS, and Kammerer giving weight to PCS's physicalist siblings. The insertion does not state what the new page concludes; it attaches the page to the claim the page qualifies. (The host sentence's Balog "standoff" concession is itself unverified per the research note's Gaps, L385 — pre-existing, not re-minted here.)
- **Severity**: Medium
- **Recommendation**: → "This concession from PCS's strongest advocate is significant: the strategy cannot claim victory even on its own terms, and physicalism's [[rival-explanations-of-the-explanatory-gap|other explanations of the gap]] do not need it." (+6; PCS headroom 54 → 48).

### Issue 8: host insertion — explanatory-gap L121 links a flat dualist assertion to a page that scores it a standoff
- **File**: `concepts/explanatory-gap.md` L121 (headroom 4)
- **Location**: "Problem: this doesn't explain why phenomenal concepts work this way. If consciousness is physical, why do we conceptualize it so differently from other physical things? The gap in concepts [[rival-explanations-of-the-explanatory-gap|points to a gap in the referents]]."
- **Problem**: the research note (L350) named "The gap in concepts points to a gap in the referents" as "the inference the new page examines"; the integration piped a link onto it and left the assertion flat. The new page's verdict is *compatible* and "a standoff" (L99), so the anchor text misdescribes its target.
- **Severity**: Medium
- **Recommendation**: two substitutions on L121, net +2 within headroom 4: "Problem: this doesn't explain why phenomenal concepts work this way." → "This doesn't explain why phenomenal concepts work this way." (−1); "The gap in concepts [[rival-explanations-of-the-explanatory-gap|points to a gap in the referents]]." → "Whether the gap in concepts [[rival-explanations-of-the-explanatory-gap|points to a gap in the referents]] is contested." (+3). Headroom 4 → 2; measure before and after.

### Host insertions that state the result correctly (no action)
- Hub `type-a-type-b-and-type-c-physicalism` L38 ("leaves the tier unchanged"), L92 (routing row now points at the page), L122 ("now run, splits by explanandum and does not favour dualism, so Type-B stays *compatible*"), L128 ("now made, leaves it there") — all accurate.
- `topics/arguments-against-materialism` L83 ("is run on a dedicated page and leaves the tier at *compatible*") — accurate.
- `concepts/ignorance-hypothesis` L66 (Stoljar clause) — matches the page's L59 word for word.
- `concepts/meta-problem-of-consciousness` L95 ("scores the meta-problem challenge for Type-B") — accurate as a pointer, though it follows a sentence running C3 the other way ("they become evidence *for* that reality") without a connective. Optional, Low: "… scores the meta-problem challenge for Type-B." → "… nonetheless scores the meta-problem challenge, which asks only that the mechanism produce the judgments, for Type-B." (+10; headroom 73).
- `concepts/primitive-identities-and-strong-necessities` L101 — accurate on the verdict; "that [[type-a-type-b-and-type-c-physicalism]] listed as not yet run" now sends the reader to a hub that no longer says so. Optional, Low: "listed as not yet run: it supplies one criterion on dualism's side," → "routes to Type-B: it supplies one criterion on dualism's side, conditional on the master argument," (net +3; headroom 163).

## Counterarguments to Address

### Dualism "passes" C2 (L67, L83)
- **Current content says**: a real ontological gap would be felt exactly where phenomenal concepts meet physical ones; dualism predicts no felt gap outside phenomenal–physical identities.
- **A critic would argue**: the vitalism precedent is a felt gap that closed; felt gaps have attached to life, to action at a distance, to the origin of species. If felt gaps track ontological gaps, dualism owes an account of the ones that did not.
- **Suggested response**: the standard reply (Chalmers 1996; PCS L139 already runs it) is that those gaps were gaps in mechanism, closed by functional explanation, whereas Sundström's test concerns a posteriori identities between co-referring terms. One clause would do, and C2's dualist pass is already restricted to "the fallacy form" — but it should be stated rather than assumed. No edit minted; carry on the refine pass if the headroom allows (≈ +15).

### C6 as a dualist lead
- **Current content says**: dualism leads on reflective stability (L39, L73).
- **A critic would argue**: see Issue 2 — a reflection-resistant fallacy is the fallacy theorist's own view (Papineau's "seductive"; Tye's "cognitive illusion"), so the criterion may not separate.
- **Suggested response**: Issue 2's two edits.

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| PCS is "one of three physicalist diagnoses … rather than the mainstream statement" | L105 | Contradicted by Kammerer's abstract ("One of the most common strategies") and P-D1 L46 — Issue 1 |
| "Fallacy accounts predict that careful reflection weakens the intuition" | L83 | Attribute to Kammerer; no fallacy theorist says it — Issue 2 |
| Díaz "with training and culture untested … as the Map reports them" | L69 | Not on L119 of the cited page — Issue 3 |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "on which the problem intuitions are correct" (L45) | drops Chalmers's "many of" | "on which many of the problem intuitions are correct" |
| "while her twin's is not" (L45) | drops "plausibly" / "strong intuition" | see Issue 5(b) |
| "Kammerer's conclusion … and concludes" (L61) | subject mismatch | "and he concludes for a physicalism of one of those kinds" |

## Length

2,974 by `analyze_length` (gate 3,500, `>=`; headroom 525); prose 2,560 against the note's 1,900–2,300 target. Per section: Explananda 284, Lot 370, Criteria 968 (planned 650), Discriminate 209, Tier 230, Relation 220. The overshoot is in the Criteria section and in the reference apparatus (18 references), and it is not a condense case: every criterion paragraph carries a "whose criterion / whose scoring" attribution that a cut would strip. Two trims lose no attribution and offset most of the additions above: (a) L67, `which "seems to overgeneralize" since "the intuition of dualism hinges on the way we think specifically about phenomenological states" (2011, p. 15)` → `which "seems to overgeneralize" (2011, p. 15)` (−14; one Bloom quotation carries the point); (b) L51, `; Papineau writes of the contrast data that "It would be useful to have further empirical investigation of this issue" (2011, p. 17).` → `; Papineau asks for experiment on the contrast data (2011, p. 17).` (−10). The first paragraph of "What Would Discriminate" (L83, 75 words) restates C2/C6 and could later be folded into those paragraphs if a future pass needs room, but it is where the discriminating-prediction framing lives and should not be cut on this pass. Net after all Issue 1–6 edits and both trims: +34, 3,008 words, headroom 491.

## Strengths (Brief)

The page does what the routing and IBE pages asked for and nothing more: criteria stated with their owners, scoring attributed, the empirical criterion conceded to the opponent, the lot widened so that a win over PCS is not mistaken for a win over physicalism, the tier held at *compatible* with P-M1 cited, and the IBE framing owned as the Map's. The Tye date, the Kammerer manuscript pagination and the Bogardus/Sundström/Fiala secondary routing are all handled exactly as the brief required. Preserve the Lot section's three-family structure and the "Map's scoring" labels in any revision.

## Priority List (for the driver; cap 4; no edits made here)

1. **P2 refine-draft** — `concepts/rival-explanations-of-the-explanatory-gap.md`: Issues 1, 2(a)(b), 3, 4, 5(a)(b), 6 plus trims (a) and (b) in §Length. All exact old/new strings above; net +34; headroom 525 → 491. Locate every target by quoted text, confirm single occurrence, print the live line. The research note's L113, L141, L155 carry the three quotations the edits add or rely on.
2. **P3 refine-draft** — `concepts/explanatory-gap.md` L121: Issue 8, two substitutions, net +2, headroom 4 → 2. Measure before and after; do not touch the rest of the line.
3. **P3 refine-draft** — `concepts/phenomenal-concepts-strategy.md` L137: Issue 7, one substitution, +6, headroom 54 → 48. Do not touch L39/L85/L139 (23:39Z calibration pass, done).
4. **P3 refine-draft (optional, Low)** — `concepts/primitive-identities-and-strong-necessities.md` L101 (+3, headroom 163) and `concepts/meta-problem-of-consciousness.md` L95 (+10, headroom 73), the two pointer tightenings under "Host insertions … (no action)". If minted as one task, list both files on the File line.

Not to mint: the blocked "Run the second-order IBE …" P3 (todo L1465) — flip its Status to pending; its Blocked-by condition is met.
