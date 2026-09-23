---
ai_contribution: 100
ai_modified: 2026-09-21 20:57:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-21
date: &id001 2026-09-21
draft: false
human_modified: null
lastmod: 2026-09-21 20:57:00+00:00
modified: *id001
related_articles:
- '[[dualism-cartography]]'
title: Pessimistic Review - Dualism Cartography
topics: []
---

# Pessimistic Review

**Date**: 2026-09-21
**Content reviewed**: `obsidian/apex/dualism-cartography.md` (5,185 words total; 4,666 prose / 525 apparatus)

## Why this article, and what is different about reviewing it

This is the first adversarial pass this article has ever had. A corpus scan of all 578 pessimistic reviews against all 704 live articles found 122 articles never once mentioned in a pessimistic review, and this is one of them — the Map's central cartography piece among them. It is also structurally unreachable by the lens that would otherwise have caught these defects: `tools/curate/deep_review.py:210` restricts the deep-review candidate pool to `topics, concepts, tenets, arguments`, so no automated deep review can ever select an apex article. Its five prior reviews are two `apex-evolve` runs and three hand-invoked deep reviews.

Two consequences shape what follows.

First, **the findings cluster where the article's repair history has been thinnest, not where its arguments are weakest**. The argumentation here is unusually disciplined; three of the four findings below are *carry-forward* defects — places where a real repair landed at one locus and the same string survived at a sibling locus in the same file. That is the signature of a file whose fixes arrive as targeted single-sentence commits with no in-file sweep.

Second, **every recommendation below is word-neutral or word-negative**, deliberately. The article sits at `hard_warning` against an apex hard ceiling of 5,000 (`analyze_length` = 5,185, usable ceiling 4,999). No finding here asks for an added paragraph.

### A correction to the length framing this review was commissioned under

The brief for this run stated that an open `NEEDS-HUMAN` length entry from 2026-08-04 records this article as "genuinely over on prose." That is a misattribution and it should not propagate. The 2026-08-04 entry (`obsidian/workflow/todo.md`, "NEEDS-HUMAN (length decision) 2026-08-04") targets **`apex/conjunction-coalesce`**, and it names `dualism-cartography` only as the *contrast* case, in these words:

> "The apparatus argument cannot rescue this one, which is exactly what distinguishes it from `apex/dualism-cartography` (5,185 total but ~4,860 prose — **a false over-length, do not re-chase**)."

Re-measured live this run: total 5,185, prose 4,666, apparatus 525. Prose is **333 words under** the usable ceiling. There is **no open length decision for this file**, and the one operator judgement on record classifies it as a false over-length. The §4 material below is therefore offered as *content-quality* input — a genuine redundancy that happens to be word-negative — and not as length remediation. No length task is minted here.

## Critiques by Philosopher

### The Eliminative Materialist

Churchland's line of attack is anticipated and handled better than most Map articles handle it. L77 states plainly that [illusionism](/concepts/illusionism/) "falls off the grid rather than low on it, and no cell can charge it a debt," and does not pretend this is a refutation. That is honest framework-boundary marking, not boundary-substitution, and the pessimistic lens should say so.

But she would press the next step, and the article does not have an answer ready. If the only position that denies the explanandum is structurally unrepresentable on your grid, then your grid is not a neutral instrument that an eliminativist could pick up and use — and the article claims twice over that it *is* (§3 below). Her charge is not "your grid is wrong"; it is "your grid's advertised neutrality is narrower than you say." That charge lands.

### The Hard-Nosed Physicalist

Dennett's strongest available move is against the *inventory*, not the metaphysics. The article withdrew its comparative "cheaper than" verdicts in August for want of a scale (L87), and L143 now says the inventory ranks "the cells at all" — nothing. Yet the inventory still reports "Q4 is charged on all three questions" against Q2-strict, which "pays nothing on mechanism." A reader takes 3 > 0. The article's own licence at L87 — "licenses saying *which* items a cell is charged … and nothing about how heavy any item is" — does cover this: a count is a which-question, not a weight-question. So the objection does not quite succeed. But L143's flat "without ranking the cells at all" overstates the retraction: the inventory does induce an ordering by item-count, and what it lacks is a *weight* ordering. Low severity, word-neutral to fix, noted below the priority list.

### The Quantum Skeptic

Tegmark's decoherence objection is out of scope here — the article routes it to the post-decoherence companion and does not assert a timescale. What he would catch instead is §2 below: the article banks "the Born-rule causal-consistency result" as a *measurement the framework has*, with no indication that the source is an unrefereed 2025 arXiv preprint whose single-subject result does not yet generalise. Twenty-seven live Map articles cite Torres Alegre (2025) with a preprint caveat. This one cites it with no caveat and no reference entry. Tegmark's complaint would be exactly right, and it is the sharpest concrete defect in the file.

### The Many-Worlds Defender

Deutsch has no purchase here that the article has not already conceded. L107 books the global-exclusion posit as a *charge on the Map's own cell* — "A posit the grid cannot deliver, on which the Map's frontier depends, is a charge, and it is entered here" — and the dependency table repeats it. This is the article doing the thing it says it does, and it is a genuine strength. Flagging "an Everettian would disagree" would be finding nothing.

### The Empiricist

The Popperian's question — what would falsify this? — is answered honestly at L105: the Born-rule bias is "empirically indistinguishable from chance" under *unconditioned aggregate* tests, with the scope stated and a conditioned test named as live. That scoping was installed corpus-wide in a recent sweep and it holds here. No over-concession tell (*no possible / cannot ever / in principle undetectable*) survives in the file.

His better objection is methodological: the article's central defence of its own genre — that cartography "serves both" the tenet-accepting and the tenet-rejecting reader — is an empirical claim about usability, and the article's own dependency table says the grid "degenerates to one occupied cell" without Tenet 1. He would ask which of the two the article believes. See §3.

### The Buddhist Philosopher

Nagarjuna's objection is that the thickness axes presuppose a substantial mind to be thick or thin, and that a process-only or aggregate reading of the subject makes the mind-axis coordinate undefined rather than low. The article has no place for this: the grid's "thin" pole is "only what is phenomenally introspectable — bare qualia," which still reifies a bearer. The Map has the resources to answer — `positions/individuation-and-subjecthood` carries the Madhyamaka concession explicitly — but this article does not route to them.

This is a real coverage gap, and it is the one finding here that **cannot be repaired word-neutrally**, since it needs at minimum a routing sentence. It is therefore deliberately **not** on the priority list and **not** minted. It is recorded for the operator as a known, priced, unpaid item.

## Critical Issues

### Issue 1: this morning's L133 repair did not sweep the file — the conflation it fixed is still live at L91 and L87

- **File**: `obsidian/apex/dualism-cartography.md`
- **Location**: L91 (bold lead of the Q1 cell), L87 (the warrant paragraph)
- **Severity**: High
- **Affordability**: word-neutral

Commit `0590f6a6d3` (2026-09-21 13:58) repaired L133, which had conflated the two debts owed by Q1's two routes. The repaired sentence now reads correctly: *"The Map's own cell owes that control law; the region's other, delegatory Q1 route owes an authority law."* The diff touched **one sentence and the `ai_modified` stamp**. It swept nothing.

The same conflation is still live at two loci, both upstream of the repair and both more prominent than it:

**(a) L91, the bolded lead of the inventory's most important cell**, reads:

> **Q1 owes the authority debt—by two routes, not one.**

The paragraph it heads says the opposite. Its own closing sentence (L95) is: *"Q1's items are an authority law on one route, an indeterminacy-site specification and a control law on the other."* The authority law is owed on the **delegatory route only**; the difference-making route — the one the Map takes (L123) — owes a different pair of items entirely. The heading asserts that one debt arrives by two routes; the body establishes that two routes charge disjoint debts. A reader who reads only the bold leads, which is what a bolded per-cell inventory invites, takes away exactly the claim the morning's repair removed from L133.

**(b) L87, the "Warrant is uneven too" audit**, reads: *"Q1's authority debt is derived (from a sufficient physical cause conjoined with a genuine mental contribution, routed through Schaffer's trumping preemption)."* The parenthetical is accurate **for the delegatory route** — "a sufficient physical cause" is that route's defining premise. Unqualified, the label "Q1's authority debt" presents the delegatory route's item as the cell's item.

There is a second-order consequence worth stating separately, because it is the part a future sweep will otherwise miss. The warrant audit at L87 classifies four items — Q1's authority debt, Q2's exclusion debt, Q3's transparency debt, Q4's three-way charge — as derived or read-off. **The Map's own route's items are not in that audit at all.** The indeterminacy-site specification and the control law receive no warrant classification anywhere in the article. So the paragraph that exists to say "here is which of our charges are argued and which are merely asserted" audits the rivals and the sibling route, and omits the Map's own. That is precisely the asymmetry the "Two items charge the Map's own cell" paragraph at L103 was written to prevent, arriving by a different door.

**Recommendation.** Rewrite the L91 lead so it names the disjunction rather than a single debt — e.g. *"**Q1 owes a mechanism debt on either route — but not the same one.**"* (identical length). Qualify L87's label to "Q1's delegatory-route authority debt" (+2 words). Extend the warrant sentence to classify the Map's own route's two items, funded from the trims in Issue 2 (net ≤ 0).

### Issue 2: the Tycho triple at L133 banks an uncited, unrefereed preprint as a result, and asserts an exclusivity its own ledger contradicts

- **File**: `obsidian/apex/dualism-cartography.md`
- **Location**: L133 (the *pre-Keplerian* calibration sentence), against L149 (Evidence and Dependency)
- **Severity**: High
- **Affordability**: word-negative

L133 reads: *"the framework has Tycho-analogue measurements (the ~10 bits/second bandwidth constraint, the Born-rule causal-consistency result, the theta-band willed-attention signatures of Rajan et al. 2019) … **The first of those carries a caveat** inherited from the specification programme."*

All three carry caveats. Two are missing, and the sentence's "the first of those" actively asserts that they are not needed.

**(a) The Born-rule causal-consistency result is a dangling appeal to an unrefereed preprint.** The result is Torres Alegre (2025), an arXiv preprint. Across `obsidian/apex`, `topics`, `concepts`, `positions` and `voids`, **27 live articles cite it, and they caveat it near-uniformly** — *"a recent arXiv preprint not yet peer-reviewed"* (`interface-specification-programme` L88, L138n, `post-decoherence-selection-programme` L83), *"a recent arXiv preprint not yet independently confirmed"* (`forward-in-time-conscious-selection` L143, `phenomenology-mechanism-bridge` L158). `interface-specification-programme` L149 goes further and books the limitation this article would need: *"the single-subject causal-consistency result (Torres Alegre 2025) does not yet establish [the many-subject form]."*

In `dualism-cartography` the string "Torres" appears **zero times**. The preprint is neither named nor referenced — the References list runs to 18 entries and contains no Torres Alegre — yet the result it supplies is presented as a *measurement the framework has*. An unrefereed, single-subject, not-independently-confirmed preprint is banked, uncaveated and unattributed, inside the sentence whose entire job is honest calibration of the framework's evidential stage. That the sentence is the article's *self-described honest calibration* is what makes this the sharpest defect in the file.

Note also that a prior pass already ran an uncited-reference sweep here — commit `7d2ed9ab17`, "two uncited references are a free fix" — and did not reach this one, because the appeal is phrased as a bare noun phrase ("the Born-rule causal-consistency result") with no author name to grep for. That is worth recording as a sweep-design lesson: an author-name sweep cannot see a citation that never names its author.

**(b) The theta-band item's discount is stranded in the ledger.** L149 states it: the theta-band signatures are ones *"which Rajan et al. read through ordinary conflict and cognitive-control processes, and which therefore cannot carry interface-specific weight without a discriminating result."* That is a serious discount — it says the item cannot do interface-specific work — and it sits sixteen lines below a sentence that has just told the reader only the *first* item needs qualifying. A reader who stops at the Frontier section, which is where a truncation-resilient LLM reader plausibly stops, gets three Tycho-analogue measurements of which one is hedged.

**Recommendation** (net word-negative): strike "the Born-rule causal-consistency result" from the Tycho list (−6) — it is the one of the three that the article never develops and never cites, so it loses nothing — or, if it is kept, name and caveat it in the sibling articles' established form and add the reference entry. Change "The first of those carries a caveat" to "The bandwidth figure carries a caveat" (word-neutral, and removes the false exclusivity). Pull a compressed form of the Rajan discount inline, funded by the deletion.

### Issue 3: the article's claim to serve tenet-rejecting readers is stated twice at a strength its own dependency table withdraws

- **File**: `obsidian/apex/dualism-cartography.md`
- **Location**: L143 (Synthesis), L149 and L155 (Evidence and Dependency)
- **Severity**: Medium
- **Affordability**: word-neutral if repaired by weakening; needs ~10 words if repaired by distinguishing

The article's central defence of the cartographic genre is that it is usable from outside the framework. It says so twice:

- L143: *"A reader who rejects the tenets can still **use** the grid."*
- L149: *"The grid … is a classificatory result a reader can **accept while rejecting every tenet**; its warrant is the demonstrable orthogonality, not the framework."*

Six lines below the second, in the same section, the dependency table says:

- L155: *"**Dualism** | *Scope.* Constitutes the territory: **without irreducibility the grid degenerates to one occupied cell.**"*

These cannot both stand as written. A grid with one occupied cell is not a grid a reader can use to locate positions; it is a claim that physicalism is true. And L77 has already established the concrete case: illusionism "falls off the grid rather than low on it" — so the reader most likely to reject Tenet 1 is exactly the reader the grid cannot accommodate.

A reconciliation *is* available, and it is the right fix: the **classification** (the two axes are orthogonal to the relation-kind axis, demonstrated by the Nida-Rümelin / Descartes and Saad / Chalmers cases at L73) is genuinely tenet-independent, while the **non-degeneracy of the territory** — that more than one cell is occupied — is not. The article never draws that distinction, and this is the section whose whole purpose is to draw exactly this kind of distinction. "Evidence and Dependency" was adopted in July precisely because synthesis pieces are vulnerable to confidence amplification; here it amplifies in one sentence and discounts in the next.

**Recommendation.** Either weaken (word-neutral): L149's "while rejecting every tenet" → "while rejecting the Map's interaction commitments"; L143's "can still use the grid" → "can still use the grid's axes to locate positions." Or distinguish (+~10 words, trim-funded): add the orthogonality-vs-occupancy split to L149 explicitly. The second is better and the article can afford it out of Issue 2's deletions.

### Issue 4 (operator input, not minted): the Relation-to-Site-Perspective section is a five-for-five restatement of the dependency table, ten lines above it

- **File**: `obsidian/apex/dualism-cartography.md`
- **Location**: L153–L159 (table) and L161–L173 (prose)
- **Severity**: Medium
- **Affordability**: word-negative (~200–230 recoverable)

This is the answer to the question "which prose is weakest," and it is not close.

The two sections total **597 words — 11.5% of the body — and deliver one mapping between five tenets and five functions, twice, in the same order.** Measured row by row:

| Tenet | Table (L153–159) | Prose (L161–173) |
|---|---|---|
| Dualism | "Constitutes the territory: without irreducibility the grid degenerates to one occupied cell" | "makes the territory a territory: only if consciousness is irreducible is there a grid of ways to weight mind against matter" |
| Minimal Quantum Interaction | "Fixes the physical-side coordinate at thin, selects the narrow-probabilistic-channel reading, and generates the interface and formalisation debts" | "sets the physical-side coordinate at thin and supplies the narrow-probabilistic-channel reading of the interface—and with it the frontier, since the interface and formalisation debts are what such a channel must eventually pay" |
| Bidirectional Interaction | "Rules pure Q2 out of the admissible region and **forbids retreat to epiphenomenalism**" | "closes off pure Q2 and **forbids retreat to epiphenomenalism** when specification proves hard" |
| No Many Worlds | "Makes outcome selection a real event requiring a law; entered on the inventory as the global-exclusion item" | "underwrites the frontier—specification only makes sense if there is genuine selection among exclusive outcomes for a law to govern—and is itself charged on the inventory as the global-exclusion item" |
| Occam's Razor Has Limits | "Blocks the inference from Q1's itemisation to Q1's truth, keeps Q4 live, and is why the inventory reports debts rather than a ranking" | "keeps the parsimony reasoning honest in both directions, refuses to let the Map's own Q1 itemisation count as proof, and authorises Q4 as a live option that thinness-as-virtue would wrongly exclude" |

Five rows, five paraphrases, one of them ("forbids retreat to epiphenomenalism") verbatim. The prose section adds exactly one thing the table does not have: the closing sentence *"The whole map is an exercise in this tenet."* Everything else is the table decompressed.

**Why this is not minted.** Both sections are *required* — `Relation to Site Perspective` by `CLAUDE.md` and the writing-style guide, `Evidence and Dependency` by `apex-evolve/SKILL.md` L267–269 as of 2026-07-16. Collapsing one into the other is precisely the question the open `NEEDS-HUMAN` entry of 2026-08-06 (`todo.md`, the Evidence-and-Dependency retrofit entry) puts to the operator as its **option (1), "ratify prose-equivalence"** — whether prose that does the ledger's work satisfies the requirement without the heading. That entry names `dualism-cartography` as one of only **7 of 38** apex articles carrying the ledger at all. Minting a dedupe here would pre-empt a corpus-wide governance decision from inside a reports-only review, so it is routed rather than actioned.

**Recommendation to the operator.** If option (1) is ratified, this file is the cleanest demonstration case in the corpus: keep the table (it does the dependency-calibration work the ledger was adopted for, and it carries the No-Many-Worlds charge), cut the prose section to a two-sentence pointer preserving only the "whole map is an exercise in this tenet" close, and recover ~200 words at near-zero information loss. That alone takes the file from 5,185 to ~4,985 and clears the gate without touching a single argument.

## Weakest prose, ranked — input to the condense decision

Requested explicitly by the brief. Ranked by words recoverable per unit of argumentative loss.

1. **Relation to Site Perspective, L161–173 (233 words).** See Issue 4. ~200 recoverable at near-zero loss. Governance-blocked, not technically blocked.
2. **The "neighbours" paragraph, L125 (~140 words).** *"Drifting toward Q2 would… Drifting toward Q4 would… Drifting toward Q3 would…"* This is the third pass over the same quadrant content. The Grid section has already characterised each cell; the Debt Inventory has already itemised what each owes; L121 has already stated which cells the tenets permit and forbid. The paragraph's only new content is the phrase "explanatory resources it lacks" — an admission about Q4's advantage that is worth keeping — and the Q3-adjacency-to-idealism point, which L99 already makes. Roughly 100 words recoverable by compressing to two sentences.
3. **The Synthesis section's rhetorical close, L143 and L145 (~30 words).** *"Cartography serves both because it claims less than advocacy would—and, in claiming less, charts more"* and *"what distinguishes this cartography from the hand-waving that has historically stood in for a map of the dualist terrain."* Two problems beyond the word count. The first is ornament — an antithesis that restates the preceding sentence. The second is a genuine tone defect: "hand-waving" is a dismissive adjudication of the prior literature, delivered inside the section whose thesis is *"map, do not adjudicate."* The article spends 5,000 words earning the right not to sneer and then sneers in its penultimate paragraph. Cut both; the section is stronger and 30 words lighter.
4. **The Debt Inventory (1,291 words, 25% of the body) is the largest section but is *not* a condense target.** Recorded here so a future condense pass does not go after it on size alone. It is the article's load and it is dense throughout: four cells, three questions, plus the two self-charging items and the three closing patterns. The only compressible material in it is the Q1 paragraph's redundancy with itself (Issue 1), which repair removes rather than trims.

**Net available without touching an argument:** ~330 words (200 + 100 + 30), against 186 needed to clear the gate. The gate is clearable twice over from redundancy alone. This file does not need a condense pass in the `/condense` sense; it needs a dedupe, and ~60% of that dedupe is waiting on one operator decision that is already open.

## Counterarguments to Address

### The grid's neutrality

- **Current content says**: a reader rejecting the tenets can still use the grid (L143, L149).
- **A critic would argue**: the grid is constituted by Tenet 1, by the article's own table (L155), and the position most likely to reject Tenet 1 — illusionism — is explicitly off-grid (L77). The neutrality claim is available for the *axes* and not for the *territory*.
- **Suggested response**: draw the orthogonality-vs-occupancy distinction. It is true, it is the article's own material, and it makes the neutrality claim defensible rather than merely asserted. See Issue 3.

### The subject presupposed by the mind-axis

- **Current content says**: mind-side thickness runs from "only what is phenomenally introspectable" to "a subliminal self or cosmic consciousness" (L62).
- **A critic would argue**: both poles presuppose a bearer. On a no-self reading the coordinate is undefined, not minimal — the same structural move the article makes for illusionism on the phenomenal side, unmade here.
- **Suggested response**: route to `positions/individuation-and-subjecthood`, which already holds the Map's Madhyamaka concession. Costs a sentence; recorded as unpaid, not minted.

## Unsupported Claims

| Claim | Location | Needed Support |
|---|---|---|
| "the Born-rule causal-consistency result" presented as a measurement the framework has | L133 | Name Torres Alegre (2025), carry the preprint caveat its 27 sibling loci carry, add the reference entry — or delete the item |
| "The first of those carries a caveat" | L133 | False as stated; the article's own L149 supplies a caveat for the third item |
| "a reader can accept [the grid] while rejecting every tenet" | L149 | Contradicted by L155 in the same section |
| "Elisabeth's interface challenge" cited as external-literature warrant | L149 | No reference entry; three of the four items in that list have one. Low severity — a historical commonplace — but it is the ledger making an externality claim |

## Language Improvements

| Current | Issue | Suggested |
|---|---|---|
| "**Q1 owes the authority debt—by two routes, not one.**" (L91) | Contradicts its own paragraph | "**Q1 owes a mechanism debt on either route — but not the same one.**" |
| "The first of those carries a caveat" (L133) | Asserts a false exclusivity | "The bandwidth figure carries a caveat" |
| "are doing load-bearing work in placing the Map where it sits" (L127) | `CLAUDE.md` restricts "load-bearing" to premises an argument genuinely depends on | Here it arguably qualifies — the placement does depend on Tenets 1 and 5 — so this is a *keep*, recorded only so a future sweep does not strip it reflexively |
| "the hand-waving that has historically stood in for a map of the dualist terrain" (L145) | Adjudicative dismissal inside a "map, do not adjudicate" section | Cut, or "the informal treatments that have stood in for a map of the dualist terrain" |
| "without ranking the cells at all" (L143) | Overstates the August retraction — the inventory still orders cells by item-count; what it lacks is a weight ordering | "without ranking the cells by weight" |

## Checked and clean

Recorded so a later pass does not re-run these.

- **Forbidden editor labels** (`direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `Engagement classification:`, bold `**Evidential status:**`): zero occurrences.
- **Boundary-substitution**: none. L97 (Q2/Bidirectional Interaction) and L107 (MWI/global exclusion) are model cases of honest framework-boundary marking — both explicitly decline to present a tenet as a refutation, and L107 converts the boundary into a self-charge.
- **Altered-state symmetry audit**: does not apply. Zero supportive-cluster citations.
- **Over-concession tells** (*no possible / cannot ever / in principle undetectable*): none. The Born-indistinguishability claim at L105 is correctly scoped to "unconditioned aggregate" tests with a conditioned test named as live.
- **Lycan (2009)**: quote verbatim, stance-framing correct as of the 2026-08-06 repair. Do not re-open — this citation has been through four passes.
- **Huemer (2009) "four justifications"**: consistent with `concepts/parsimony-epistemology` L67 and `topics/parsimony-case-for-interactionist-dualism` L55. Correct.
- **Masanes–Galley–Müller / Kent / Stacey (L135)**: the "unique" downgrade and the finite-dimensional caveat both landed. Correct.
- **Internal quote channel**: both quoted internal strings verified verbatim against their sources — "rests on the global-exclusion posit… a chosen starting point, not a result this grid delivers" against `topics/four-quadrant-dualism-taxonomy` L83, and "without converting per-cell lightness on the chosen battery into endorsement" against `topics/mechanism-costs-dualism-thickness-quadrants` L55.
- **L123 and L127** (the two-routes selection and the debt list): settled 2026-08-03. Re-read and found sound; no objection.
- **Anchoring**: no hedge-padding recommended. The article's calibration language is, if anything, better than corpus median.

## Strengths (Brief)

- **The self-charging discipline is real and it is rare.** L103–107 charge the Map's own cell two items no rival cell is charged, and L117 withdraws a prior formulation ("the *least mechanism cost compatible with its tenets*") on the explicit ground that it "totalled costs on a scale the inventory never supplied, and it balanced the books before the two items charging the Map's own cell had been entered." Articles that name the moment their own bookkeeping flattered them are uncommon anywhere.
- **L89 is the single best sentence in the file** — the observation that the three-question battery "leans deliberately toward physical-side debts" because those questions "originate in the physicalist's challenge to interactionism," and that left there "the battery would score rivals only." That is an instrument criticising its own calibration, and it is what licenses the two self-charges that follow.
- **The orthogonality argument at L73** (Nida-Rümelin vs Descartes; Saad vs Chalmers) is the grid's actual warrant and it is a clean, checkable, framework-independent result. Whatever happens to the rest of the article, this survives.
- **Q3's treatment (L99) is scrupulous about a case that flatters nobody** — it notes that genuine Q3 *dualism* is rare because the position tends to slide to idealism, which is a concession against the article's interest in having four populated cells.