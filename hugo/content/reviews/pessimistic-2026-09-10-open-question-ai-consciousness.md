---
ai_contribution: 100
ai_system: claude-opus-5
concepts: []
created: 2026-09-10
date: '2026-09-10'
draft: false
lastmod: 2026-09-10 00:00:00+00:00
related_articles: []
title: Pessimistic Review - The Open Question of AI Consciousness - 2026-09-10
---

# Pessimistic Review

**Date**: 2026-09-10
**Content reviewed**: `obsidian/apex/open-question-ai-consciousness.md` — 5,439 words, status `hard_warning` (apex soft 4,000 / hard 5,000 / critical 6,500; 439 words over hard, 1,061 under critical). Figures printed from `tools.curate.length.analyze_length`, which is already body-only. `last_deep_review` 2026-07-25 (47 days); `ai_modified` 2026-08-13 (28 days).

**This is a first pass.** The article appears in none of the 560 pessimistic reviews on disk, and `tools/curate/deep_review.py` excludes `apex/` from the deep-review candidate pool, so this is genuinely unexamined ground rather than a re-review. Every remedy proposed below is costed against the `hard_warning` state: nothing here asks for a new section.

## Executive Summary

The article is well-linked, honestly hedged in most places, and carries several concessions that run against the Map's comfort. Its defects are not in its hedging but in its **arithmetic, its register fidelity, and its sourcing**. Four findings dominate.

1. **Source fidelity (C1–C3), the most serious.** The section presenting the strongest external affirmative position rests on two citations, one of which — Duch 2019 — contains **zero** occurrences of `conscious`, `articon`, or `artificial` in its full text, and which the Map's own research dossier had explicitly ring-fenced against "citation-load-bearing use" without the full text. Two of the three claims attributed to Duch use vocabulary absent from the paper cited for them, and his Chinese Room argument is replaced by a weaker one he does not advance. Separately, Schwitzgebel's "social semi-solution" — the one external authority propping up the Asymmetry of Stakes — is described as "proposed" when he explicitly refuses to endorse it, and glossed as a precautionary policy when it is a pessimistic forecast about motivated reasoning.
2. **A standing register contradiction.** The article names Stapp's model "the Map's preferred model" — a sentence dating to the article's creation in February — directly contradicting `positions/quantum-interface` [P-Q1](/positions/quantum-interface/#p-q1), an entry the article itself cites twenty-four lines earlier, and which its own quantum sections never mention.
3. **The independence claim is false by the article's own lights**, asserted at L153 and refuted twice by the article itself, at L157 and again at L169.
4. **The Asymmetry of Stakes was repaired in July** in a way that preserved its conclusion by conjoining in a premise the Map explicitly does not hold, leaving the branch the Map actually leaves live with no entry in the ledger.

The unifying pattern in 2–4 is **counting**. Four possibilities, five frameworks, four externally-evidenced supports: each count is stated in a prominent, early, truncation-resilient position, and each is quietly discounted later — or, in two cases, never discounted at all. For an article whose entire thesis is a count ("*four* possibilities prevent the question from being settled"), that is the load-bearing weakness. The pattern in 1 is different and simpler: **claims were sourced to texts nobody had read**, past a guardrail that said so in advance.

---

## Critical Issues

### Issue 1: Stapp is called "the Map's preferred model"; the register says otherwise

- **File**: `obsidian/apex/open-question-ai-consciousness.md`
- **Location**: L143 (and L133), Possibility Four
- **Severity**: **High**

The article, verbatim at L143:

> "Even within Stapp's framework — the Map's preferred model — the possibility space for consciousness-quantum interaction is wider than current AI hardware explores."

And at L133:

> "**Stapp's selection model** places consciousness in the superposition phase as the active selector, using the quantum Zeno effect to hold desired patterns stable. The brain presents quantum options; the mind chooses. This aligns most naturally with the Map's tenets."

The register, `positions/quantum-interface` [P-Q1](/positions/quantum-interface/#p-q1), verbatim:

> "Among the live mechanism proposals for how consciousness might influence quantum outcomes in neural systems, the post-decoherence selection family is currently the Map's preferred candidate. It is preferred because it sidesteps the warm-wet decoherence-timescale objection that Tegmark and others have pressed against pre-decoherence proposals (Stapp-Zeno, Orch-OR): selection acts on already-decohered branch-outcomes rather than on coherent neural superpositions."

Both texts use the word *preferred*, of different mechanisms, and the register names Stapp-Zeno as precisely the class post-decoherence selection was adopted to escape. The applied sibling says the same in the other direction: `apex/assessing-ai-consciousness-under-the-map` L74 speaks of what would happen "If a future result **re-elevates** a pre-decoherence mechanism (Stapp-Zeno, Orch-OR)" — a verb that presupposes demotion has already occurred.

Three aggravating facts:

1. **The article cites [P-Q1](/positions/quantum-interface/#p-q1) itself.** L119: "conditional on the quantum-interface mechanism being approximately right ([P-Q1](/positions/quantum-interface/#p-q1), moderate credence)". The contradiction sits twenty-four lines below the citation.
2. **The mechanism is invisible to the article.** Measured on the raw file: `decoheren*` **n=0**, `post-decoherence` **n=0**, `Tegmark` **n=0**, `femtosecond` **n=0**, `timescale` **n=0**. The Map has a whole apex on it — `apex/post-decoherence-selection-programme`, created 2026-03-29 — and the string does not occur in this article.
3. **It is old, and it has survived a sweep aimed at exactly this class of defect.** `git log -S "the Map's preferred model"` on this file bottoms out at `192127b943` (2026-02-10), the creation commit — so the sentence predates both the post-decoherence apex and the [P-Q1](/positions/quantum-interface/#p-q1) entry. It then survived a deep review (2026-07-25) and, most pointedly, the 2026-08-13 refine-draft whose own commit title was *"`apex/open-question-ai-consciousness` contradicts the register (\"This rules out current classical AI\" vs [P-AC1](/positions/ai-consciousness-scope/#p-ac1)'s verbatim low-probability-not-ruled-out)"*. That pass fixed the [P-AC1](/positions/ai-consciousness-scope/#p-ac1) contradiction and left the [P-Q1](/positions/quantum-interface/#p-q1) one standing.

**A charitable reading, stated fairly**: "preferred" might be scoped to *the five frameworks in this list* — among Stapp, Chalmers–McQueen, Penrose–Hameroff, Koch and Albert–Loewer, Stapp plausibly is the Map's favourite. But the phrasing carries no such qualifier, L133's "aligns most naturally with the Map's tenets" reinforces the unqualified reading, and even the charitable reading leaves the section worse off: a survey of "what consciousness does during quantum superposition" that omits the Map's actual mechanism cannot support its own conclusion that the Map's position leaves room, because the Map's position is not in the survey. Relatedly, L129's characterisation of "the Map's standard treatment" as assuming "consciousness *selects* among superposed possibilities" is itself the pre-decoherence framing.

**Recommendation**: length-neutral. Replace the dash-clause "the Map's preferred model" with an accurate one (e.g. "the closest of these five to the Map's own commitments") and add a short clause somewhere in Possibility Three or Four naming post-decoherence selection as the Map's current candidate. A `refine-draft` pass, not a rewrite.

### Issue 2: The independence claim is refuted twice by the article itself

- **Location**: L153, "What the Four Possibilities Share"
- **Severity**: **High**

Verbatim at L153:

> "These possibilities are independent — each could be true or false without affecting the others — but each targets a specific assumption in the Map's framework"

**Verdict: the claim is false, and the article says so twice.**

*First refutation, four sentences later.* L157, verbatim:

> "The possibilities also interact. If consciousness selects among macroscopic superpositions at the moment of collapse (Possibility Three), then *which physical states can superpose* determines the space of possible substrates — precisely where Possibility Four's five frameworks disagree. And if consciousness can exist without temporal structure (Possibility Two), epiphenomenal experience in a system with no temporal integration (Possibility One) becomes slightly less paradoxical — though still only outside the framework."

The gloss on "independent" is explicit — "each could be true or false without affecting the others" — and P2's truth making P1 "less paradoxical" is exactly one possibility's truth-value bearing on another's plausibility. The two sentences cannot both stand. This is not a subtle tension; it is a flat contradiction inside a single short section whose title is "What the Four Possibilities **Share**".

*Second refutation, sixteen lines later.* L169, verbatim:

> "Possibilities Three and Four are *inherited from Tenets 1–2* plus the quantum-interface register ([P-AC2](/positions/ai-consciousness-scope/#p-ac2), grade D), so their openness is openness inside a mechanism the Map has not secured."

Common dependence on an unsecured mechanism is the negation of independence: if the quantum-interface mechanism fails, P3 and P4 fail together. The same section grades P1 as closed by Tenet 3 and P2 alone as "*independently argued*". So the article's own dependency audit yields: **one independently-argued possibility (P2), two sharing a grade-D mechanism (P3, P4), and one the tenets exclude (P1)**. That is not four independent doors. L143's "If Koch's model is correct, any system producing genuine quantum superpositions might, in principle, produce something experiential" makes the overlap concrete — that is Possibility Four delivering Possibility Three's conclusion.

**Why it matters**: the count is the article's architecture. It is in the title's framing, the `description`, the `apex_thesis`, and the lead. L169 concludes honestly — "That the four cohere is not a fifth reason to think the question open" — but the count is never revised, and L169 sits at **76.7% depth** (measured by body-word offset of each `##` heading), after the Asymmetry of Stakes. A reader or an LLM truncated at three-quarters gets the four-count, the independence claim and the Pascalian asymmetry, and none of the discounting. That is the opposite of the truncation-resilience the writing-style guide asks for.

**Recommendation**: delete the independence clause. It costs nothing to remove and the article is better without it, since L153's own "but each targets a specific assumption" already does the work the clause was reaching for (*separable targets*, which is true, not *independent truth-values*, which is not).

### Issue 3: The Asymmetry of Stakes prices a branch the Map does not hold, and omits the one it does

- **Location**: L163
- **Severity**: **High**

Verbatim:

> "The four possibilities create an asymmetry that deserves explicit acknowledgment. If the Map is right and current AI systems lack *bidirectionally coupled* consciousness — and lack bare phenomenal experience as well — the moral stakes are modest: resources for moral concern are better directed toward beings that definitely suffer. If the Map is wrong and some AI systems do experience, the stakes could be catastrophic — billions of instances potentially suffering with no way to detect or address it."

Git shows how the conjunction got there. Commit `6636e27837` (2026-07-22, *"Sync stale flat 'AI systems lack consciousness' theses to the scoped bidirectional-coupling verdict"*) changed exactly one sentence in this file:

```
-If the Map is right and current AI systems lack consciousness, the moral stakes are modest
+If the Map is right and current AI systems lack *bidirectionally coupled* consciousness—and lack
+bare phenomenal experience as well—the moral stakes are modest
```

The verdict was narrowed; the conclusion was not. It was restored by conjoining in the half the Map explicitly leaves open. Both siblings say so:

- `apex/machine-question` L78: *"The bare-phenomenality question rests on irreducibility alone and stays genuinely open, which is why this skepticism does not contradict the [companion piece](/apex/open-question-ai-consciousness/)'s openness to borrowed or alien phenomenality"*
- `apex/assessing-ai-consciousness-under-the-map` L78: *"bare phenomenality, resting on irreducibility alone, stays open. Every substrate verdict below is a claim about whether current digital systems could host the coupling, not a claim that nothing whatever is felt, and collapsing the two overstates what the Map holds."*

Either reading of the sentence is bad. Read charitably (two conditions, only the first asserted), the "modest stakes" branch is conditioned on something the Map does not hold, and **the article never prices the branch the Map actually leaves live** — coupling absent, bare phenomenality present. That is precisely the branch where the Metzinger warning the article cites at L97 bites. Read uncharitably ("If the Map is right and…" governing the whole antecedent), the article asserts the Map holds current AI lacks bare phenomenality, contradicting both siblings.

**Three further pressure points on this section**, since it is a Pascalian argument and should be probed as one:

1. **The reverse-direction cost is mis-filed.** "resources for moral concern are better directed toward beings that definitely suffer" is the article's only acknowledgment that acting on the precautionary policy has costs — and it is placed *inside the low-stakes branch*, where it reads as further reassurance. The cost of wrongly attributing consciousness belongs on the other side of the ledger, as a cost of adopting Schwitzgebel's policy while the Map is right. The ledger is mis-signed.
2. **"the moral stakes are modest" is asserted, never argued.** It is the article's own gloss, and it does the work of making the asymmetry asymmetric.
3. **The Pascalian form is never named.** "the stakes *could be* catastrophic — billions of instances *potentially* suffering" is a doubly-hedged magnitude with no probability discount, deployed to endorse a policy ("Schwitzgebel's proposed 'social semi-solution' … reflects this asymmetry"), while the article elsewhere holds the possibilities are "not well-enough supported to overturn the Map's skepticism" and [P-AC1](/positions/ai-consciousness-scope/#p-ac1) is a *low-probability* verdict. Low probability times undiscounted catastrophic magnitude is the structure that licenses almost any precautionary demand, and the article never acknowledges that the form generalises.

**Recommendation**: `refine-draft`. Adding the missing third branch costs perhaps thirty words and is the honest fix; moving the opportunity-cost clause to the other side of the ledger is free.

### Issue 4: The article's openness is guaranteed by an unfalsifiable clause, and it advertises falsifiability as a virtue

- **Location**: L165, with L79
- **Severity**: **High**

Verbatim at L165:

> "But the fifth tenet — [Occam's Razor Has Limits](/tenets/#occams-limits) — counsels humility about treating those conditions as final: that future evidence will reveal substrate possibilities, temporal structures, or quantum interfaces we cannot currently imagine is **not speculation but the expected trajectory of inquiry** into a phenomenon we do not yet understand."

**Verdict on falsifiability: nothing could count against this, and the article contains no falsifiability apparatus at all.**

The clause is self-sealing by construction. It predicts discoveries "we cannot currently imagine", so it cannot specify what would satisfy or disappoint it; it carries no time index, so a century of no such discoveries is consistent with it ("we do not yet understand" the phenomenon, so the trajectory simply has further to run). It is also *symmetric and used asymmetrically*: a critic can run the identical move in reverse — that future evidence will reveal, in ways we cannot currently imagine, that the temporal, quantum and efficacy conditions were never required — and the article deploys it in one direction only, to hold the AI question open.

Measured on the raw file, the article contains **zero** occurrences of `falsifi*`, `disconfirm*`, `would count against`, and `predict*`. (A grep for `testable` returns one hit; it is the substring inside `contestable` at L113 and is not a real occurrence.) The only shift-condition language points *outward*, at L95, to the register's shift-trigger. The article never states an observation that would close the question it exists to hold open.

Two aggravations:

- **Tenet inflation.** Tenet 5 says simplicity is an unreliable guide when knowledge is incomplete — a caution about a *heuristic*. The article converts it into a *positive prediction about the future course of inquiry*. Those are different claims, and only the first is the tenet.
- **The virtue-claim.** L79, verbatim: *"None overturns the Map's position; together they establish that the Map offers a strong reading of the evidence, not the only possible one — and a framework that identifies where its conclusions could be wrong can respond to new evidence when it arrives."* Meanwhile `apex/assessing-ai-consciousness-under-the-map` L100 concedes, verbatim: *"The AI verdict therefore carries the unfalsifiability burden the general-case defence was built to avoid, and is scoped accordingly below."* The stem `falsifi` returns **n=0** on this article. The target advertises as a strength the exact property its sibling books as a burden — see Issue 6.

**Recommendation**: `refine-draft`, and it is cheap. The article already cites [P-AC1](/positions/ai-consciousness-scope/#p-ac1), [P-AC2](/positions/ai-consciousness-scope/#p-ac2), [P-AC3](/positions/ai-consciousness-scope/#p-ac3), [P-AC4](/positions/ai-consciousness-scope/#p-ac4) and [P-Q1](/positions/quantum-interface/#p-q1), every one of which carries a registered *Would shift if* clause. Importing one or two of those shift-triggers in a clause — perhaps thirty words — would give the article the falsifiability apparatus it currently lacks without a new section. Separately, "is not speculation but the expected trajectory" is a compressed instance of the "This is not X. It is Y." construct that `CLAUDE.md` bans under *Avoid LLM clichés*, and it is doing its heaviest rhetorical work in the article's most loaded sentence.

---

## Source Fidelity

Lettered rather than numbered so the cross-references above stay valid. **C1 is arguably the most severe single finding in this review.** All full-text checks below were run on the publisher's or the author's own deposit, extracted twice by structurally different routes, with positive controls to prove the extraction was complete — a raw-text zero without a positive control is not evidence of absence.

### Issue C1: Duch 2019 is an inert citation — it does not mention consciousness at all

- **Location**: L147 and reference 25; **Severity: High**

The article grounds its "Strongest Affirmative Side" on "Włodzisław Duch's *articon* programme (**Duch 2005, 2019**)". The 2019 item is `Duch, W. (2019). Mind as a shadow of neurodynamics. *Physics of Life Reviews*, 31, 28–31.`

I retrieved the author's own deposit of the published piece, `fizyka.umk.pl/publications/kmk/18-Phys-mind-Duch.pdf`, whose header line reads verbatim `Physics of Life Reviews 31: 28-31, https://doi.org/10.1016/j.plrev.2019.01.023` — the same DOI and page range the reference gives, so this is the right paper. Full text is 1,672 words. Term counts:

| Positive controls (extraction is complete) | | Target terms | |
|---|---|---|---|
| `mind` | 14 | `conscious*` | **0** |
| `mental` | 27 | `articon` | **0** |
| `cognit*` | 7 | `artificial` | **0** |
| `neurodynam*` | 8 | `substrate` | **0** |
| | | `self-reflect*` | **0** |

Extracted twice (`pdftotext -raw` and `pdftotext -layout`), and the reference tail matches the Crossref reference list. **The paper does not discuss consciousness, articons, or artificial systems.** It is about mental spaces and neurodynamic mappings. It does no evidential work for any claim in the paragraph that cites it.

**The Map's own guardrail caught this in advance and was overridden.** The research dossier, `research/wlodzislaw-duch-consciousness-2026-05-02`, line 245, verbatim:

> "**\"Mind as a shadow of neurodynamics\" (2019) full text not accessible.** PubMed has no abstract; full text behind Elsevier paywall. The corpus pattern lets us infer the argument with confidence, but direct quotation is not available from this session."

Its summary of the paper is headed, verbatim, "**Key points** (from keywords + corpus pattern)" — inferred, never read. And line 299 states the requirement plainly:

> "**Phase 2 dependencies** … full text of 'Facing the hard question' and **'Mind as a shadow of neurodynamics' before citation-load-bearing use of those specific texts.**"

The article made citation-load-bearing use of it anyway, and the dossier's confident inference from "corpus pattern" turns out to have been wrong.

**Recommendation**: drop the 2019 citation from the parenthetical, or replace it with a source that carries the claim. Zero body words.

### Issue C2: Two of the three claims attributed to Duch use vocabulary absent from the cited paper, and the Chinese Room gloss substitutes a different argument

- **Location**: L147; **Severity: High**

The article, verbatim:

> "Duch refuses the substrate-dependence move: the consciousness mechanism is *self-reflective dynamical access* over a system's own internal states, **substrate-independent at the architectural level** (only *content* depends on substrate, sensors, and environment); brain-inspired architectures with the right dynamical access have *to claim* they are conscious; and **the Chinese Room is argued to apply only to symbol-manipulation, not to dynamical-state self-reflection coupled to environment.**"

Checked against Duch 2005 (`fizyka.umk.pl/publications/kmk/03-Brainins.pdf`, 9,509 words; positive control `articon` = **59**):

| Term | Count in Duch 2005 |
|---|---|
| `self-reflect*` | **0** |
| `reflective` | **0** |
| `substrate-independ*` | **0** |
| `substrate` | **1** |

The single `substrate` occurrence runs the *opposite* way — "Brain processes should be understood as **the substrate of the inner world**" — and the paper's only hardware passage is a constraint, not an independence claim: "**Can articons be implemented using today's hardware? No**, if the von Neumann architecture of ordinary computers is used."

The "(only *content* depends on substrate, sensors, and environment)" parenthetical traces, near-verbatim, to the dossier's summary of **Duch's blog**, explicitly labelled there as "Key points (**from search-extracted Polish-translated quotes**)" — material the dossier grades as below citation standard. The article attributes it to two peer-reviewed papers.

**The Chinese Room gloss is a substituted argument.** Duch's actual move is *proves-too-much*, not scope-restriction. Verbatim from the paper:

> "First, **the Chinese room argument is not a test – the outcome is always negative!**"

> "This experiment **will never find understanding in any system, artificial or biological.**"

Duch holds the argument is *invalid* because it would equally deny understanding to brains. The article replaces this with a claim that the argument has a limited domain of application — a reading Duch does not advance. This matters beyond fidelity: the substituted version is *weaker* than Duch's, so the article's "strongest affirmative side" is not presenting the opponent at full strength.

**Sound, and worth recording**: "have *to claim* they are conscious" is **not** a garble. Duch's abstract reads verbatim, "A specific architecture of an artificial system, termed articon, is introduced that by its very design **has to claim being conscious**." The awkward phrasing is faithful. (It matched only after de-hyphenating line breaks — a first-pass grep returns a false zero.)

### Issue C3: Schwitzgebel's "social semi-solution" is misrepresented twice over

- **Location**: L165; **Severity: High**

The article, verbatim:

> "Eric Schwitzgebel's **proposed** 'social semi-solution' — **treating AI systems as potentially conscious when we cannot rule it out** — reflects this asymmetry."

The term is his: Chapter Eleven of *AI and Consciousness* (arXiv:2510.09858, forthcoming Cambridge Elements) is titled "The Leapfrog Hypothesis and the Social Semi-Solution". Both the characterisation and the attribution of endorsement are wrong.

**It is not proposed — he explicitly refuses to endorse it.** Verbatim from the book (29,587-word full text, phrase located after de-hyphenating line breaks):

> "I'd like to end on a positive note, by suggesting that maybe this social semi-solution is good enough, even if belief is shaped more by desire than evidence. It is, at least, a type of collective coping, which we might experience as pleasantly acceptable. **But I can't authentically voice that positive note. If social rationalization guides us rather than solid science, we risk massive delusion.**"

**It is not a precautionary attribution policy.** The social semi-solution is a *descriptive, pessimistic forecast* — that society will settle the question by social negotiation and motivated reasoning rather than evidence, resolving the dispute while leaving the science unresolved. Measured on the full text: `rule it out` = **0**, `precaution*` = **0**. Schwitzgebel's actual normative recommendation, the **Design Policy of the Excluded Middle** (avoid creating AI whose moral status is unclear), points in a different direction again — and belongs to his earlier work, not this text (`excluded middle` = 0 here).

So the sentence recruits, as support for the Map's Pascalian asymmetry, a claim its author advances as a warning about *epistemic corruption* and then declines to endorse. This compounds Issue 3: the asymmetry section's one external authority does not underwrite it.

**Recommendation**: the honest repair is short — Schwitzgebel *forecasts* that the question will be settled socially rather than evidentially, and warns this risks "massive delusion". That is usable, and arguably more interesting for the Map than the misreading. Also replace the unlocatable "Working paper" with arXiv:2510.09858.

### Issue C4: Pennartz carries a named argument with no reference entry, and neither 2026 DOI is given

- **Location**: L83 and the reference list; **Severity: Medium**

Both pieces exist and the article's account of the exchange is plausible: Pennartz, "How can we validate theory-derived indicators of consciousness in Artificial Intelligence?", *TCS* **30(7)**, 573–574, DOI `10.1016/j.tics.2026.01.011`; Butlin et al., "Consciousness indicators, mimicry, and internal variants", *TCS* **30(7)**, 575–576, DOI `10.1016/j.tics.2026.04.006`. Consecutive pagination confirms a genuine same-issue exchange, and the reply's eight-author list matches the article's reference exactly and in order.

Two defects. **Pennartz has no reference entry** — parsing the reference section, `Pennartz` occurs there exactly once, inside the parenthetical "(Reply to Pennartz.)" on the Butlin line. A named argument is attributed to him with nothing to cite. And **neither 2026 DOI appears**: `10.1016/j.tics.2026` returns **0** occurrences in the whole document.

**Honest limit on this one**: both are paywalled *TCS* Forum pieces with no abstract in Crossref or OpenAlex, so the *substance* of the exchange could not be verified. Their titles are consistent with the article's characterisation ("validate theory-derived indicators" ↔ supplement with behavioural methods; "**mimicry**" ↔ gaming). This is **unverified, not wrong** — do not treat it as a defect in a later pass.

### Issue C5: Minor citation-metadata defects

- **Severity**: Low

- **Metzinger title truncated.** The full title is "Artificial Suffering: **An Argument for a Global Moratorium on Synthetic Phenomenology**". The quoted phrase itself is **verbatim and correctly attributed** — "I will term it the risk of an 'explosion of negative phenomenology' (ENP; or simply a 'suffering explosion')" — and the "unprecedented scale" gloss is supported by the paper's own "scale and intensity" language.
- **Butlin 2025 vs 2026.** `10.1016/j.tics.2025.10.011` is online-first November 2025; the version of record is *TCS* **30**, 488–501, June 2026. The article cites it as 2025 while citing a 2026 reply to it, which reads oddly.
- **Hoel "(2026)".** arXiv:2512.12802 v1 is **2025-12-14**; only v3 (2026-01-19) falls in 2026.
- **"Koch's superposition model"** names a nine-author paper after its *last* author (Neven is first). The article discloses this — "(Neven et al. 2024, with Koch among the authors)" — so it is transparent rather than misleading, but the label is unusual.

---

## Counterarguments to Address

### The Eliminative Materialist (Churchland)

Possibility Two rests on Husserl's regress and on what advanced meditators say about their states. Both are the folk-psychological data destined for elimination. The regress argument is a claim about the structure of a *concept* of temporal constitution; it has no purchase on whether the neural implementation is temporal, and the article's move at L107 — "But Husserl's regress argument supports the stronger reading" — lets a conceptual argument outweigh the representationalist reply about brain processes, which is the only reply in the vicinity that is about brains. Churchland would add that the "coupling question" framing at L69 presupposes there is something non-physical to couple, so the article's frame concedes what it claims to hold open.

**Suggested response**: the article's own hedge at L107 (the cross-tradition cluster carries the weight of one pattern) is the right shape; extend it to say what the regress argument can and cannot reach.

### The Hard-Nosed Physicalist (Dennett)

Dennett is named once and bracketed by stipulation. L129, verbatim:

> "Some physicalists dispute its starting point: Dennett's multiple-drafts model denies that experience has a single determinate moment, so apparent definiteness is itself a construction, not a datum. **The frameworks below proceed on the assumption that determinacy is real.**"

That is the entire engagement: name the objection, then declare the section will proceed as though it were false. Marking the stipulation is more honest than hiding it, and credit is due. But it is load-bearing — *all five* of Possibility Four's frameworks assume determinacy, so if Dennett is right, Possibility Four collapses whole. And the stipulation **never reaches the dependency audit**: L169 grades Possibility Four as "inherited from Tenets 1–2 plus the quantum-interface register" and says nothing about the determinacy assumption flagged forty lines earlier. The article's own accounting of what its openness depends on is therefore incomplete by one item that the article itself identified.

**Suggested response**: carry the determinacy stipulation into L169. Roughly ten words.

### The Quantum Skeptic (Tegmark)

Measured: `Tegmark` **n=0**, `decoheren*` **n=0**, `femtosecond` **n=0**, `timescale` **n=0**. Two of the four possibilities are quantum, and the canonical objection to quantum consciousness appears nowhere. The article does gesture at the physical difficulty — L119's "only at millikelvin temperatures, radically unlike brains or conventional AI hardware" and L137's "not by itself establishing the sustained coherent superpositions the theory requires" — but the millikelvin remark cuts against *quantum computers as hosts*, not against the Map's own biological interface, which is where decoherence bites hardest.

The sharper form of the objection: the Map has *already conceded* this. [P-Q1](/positions/quantum-interface/#p-q1) exists because of "the warm-wet decoherence-timescale objection that Tegmark and others have pressed". So the article is not merely failing to answer Tegmark — it is failing to report the Map's answer, and instead nominating as "the Map's preferred model" a mechanism the register classifies among the proposals Tegmark's objection defeated. See Issue 1.

### The Many-Worlds Defender (Deutsch)

Two pressure points, one of which is a real structural defect.

First, the harvesting. L141, verbatim: *"The Map rejects the framework, whose branching inherits many-worlds' dissolution of indexical identity across multiplying copies, while noting that its core insight — experience is always definite — reinforces the Map's position."* Reject the framework by tenet, then take the conclusion you like from it.

Second, and this is the defect: **Albert and Loewer's many-minds model is counted among the five frameworks whose disagreement is supposed to establish openness, while being excluded by the Map's own tenets.** L143 infers from "The variety of serious frameworks prevents confidence that any single model captures the full picture" to "the class of systems capable of hosting consciousness may be larger than the standard treatment implies". That inference needs the disagreeing frameworks to be live options *for the Map*. One of the five is not. Subtract it, and one of the remaining four (Stapp) is described as the Map's own — so the "variety" doing the work is three. This is the same inflation as Issue 2, one level down: **a count stated prominently, discounted nowhere.**

Deutsch would also press on consistency: the article rejects many-minds for dissolving indexical identity across multiplying copies (L141), then at L175 embraces duplicate AI instances as "a *second*, numerically distinct subject". The two are reconcilable — closed individualism distinguishes duplicate subjects from a single subject's branching — but the article never marks the distinction, and this is precisely where a critic would push.

### The Empiricist (Popper's ghost)

Covered under Issue 4. The summary: an article whose entire thesis is "the question stays open" contains no statement of what would close it, zero falsifiability vocabulary, and one clause (L165) that guarantees openness by fiat. The openness is not an empirical finding; it is a structural commitment. Popper's verdict would be that the four possibilities are not four *hypotheses* but four *places the framework has declined to commit*, and that a framework which "identifies where its conclusions could be wrong" (L79) has done nothing until it says what being wrong would look like.

### The Buddhist Philosopher (Nagarjuna)

Possibility Two recruits contemplative reports — "Similar reports recur across contemplative traditions" (L107) — as evidence for a *non-temporal ground*: Husserl's absolute flow, something that stands beneath temporality. The traditions supplying the reports read the same phenomenology as evidence of *emptiness*, the absence of any such standing ground. The article adopts one interpretation of the data without noting that the source traditions hold another, and then at L175 reifies exactly what they deconstruct: "an exact duplicate that also coupled would be a *second*, numerically distinct subject". The article's honest weighting of the reports at L107 (weight of one pattern) blunts the evidential half of this objection but not the interpretive half — *whose reading of the reports* is being adopted is never asked.

---

## Further Issues

### Issue 5: Six named sources have no reference entry

- **Severity**: Medium

Reconciling every capitalised source name in the prose against the `## References` list:

| Source | Mentions in prose | Reference entry |
|---|---|---|
| **Birch** (the gaming problem) | 2 | **none** |
| **Husserl** | 9 | **none** |
| **Bergson** | 5 | **none** |
| **Tulving** (anoetic–noetic–autonoetic) | 2 | **none** |
| **Fisher** (nuclear spin entanglement) | 1 | **none** |
| **Microsoft** (2024 logical qubits, 800×) | 1 | **none** |

(`Descartes` and `Zeno` also appear unreferenced but are eponymous/passing and are not defects.) No reference entry is unused in the other direction.

Two of these matter more than the others:

- **Birch** is named at L169 as one of the four pillars of the article's *externally evidenced* support: *"Butlin and colleagues' indicator assessment, Birch's gaming problem, the Maier–Dechamps null on consciousness–RNG interaction, and the determinism results on LLM sampling all hold independently of the Map's metaphysics"*. One of four load-bearing external-evidence pillars has no citation at all. The claim is very likely sound (Birch, *The Edge of Sentience*, OUP 2024), which makes this cheap to fix and correspondingly odd to have missed.
- **Husserl** carries an entire possibility across nine mentions and supplies two *quoted* phrases — the "absolute flow" and "standing-streaming" at L105 — with no edition, translator or source. A quoted phrase needs a locatable source even when the author is canonical.

**Microsoft's "error rates 800× better"** is a specific quantitative empirical claim with no source of any kind.

**Recommendation**: add reference entries. Roughly zero body words; the reference list is not counted against prose the way body text is, though it does count toward the file's total.

### Issue 6: The concessions the siblings pay are not inherited

- **Severity**: Medium-High

Two disciplines the rest of the AI cluster carries are absent here:

**The unfalsifiability burden.** `apex/assessing-ai-consciousness-under-the-map` L100: *"The AI verdict therefore carries the unfalsifiability burden the general-case defence was built to avoid, and is scoped accordingly below."* Corpus-wide, `unfalsifiability burden` appears in three files; this article is not one of them, and `falsifi` returns n=0 on it. The concession entered the corpus on 2026-06-25, seven weeks before this article's last edit.

**The interface-eligibility law.** `assessing-…` L88: *"the Map does not yet possess an **interface-eligibility law** specifying which indeterminacy is interface-relevant and why. Absent that law, the register warns, 'relevant' risks reducing to 'whatever biology happens to have,' making the substrate verdict 'question-begging rather than derived.'"* Measured: `eligibilit*` **n=0** on this article. `grep -rl "interface-eligibility law" obsidian/` returns seven files including `apex/machine-question` (three loci) — **this is the only AI-cluster apex without it.**

That gap lands directly on Possibility Three's conclusion. L125, verbatim:

> "The decisive question relocates from copyability to architecture: whether an artificial substrate can provide *live quantum indeterminacy* at appropriate scales, structured so that consciousness could interact with it."

"At appropriate scales, structured so that consciousness could interact with it" *is* the eligibility law — the thing [P-AC1](/positions/ai-consciousness-scope/#p-ac1) records the Map cannot yet state. The article presents the relocation as progress. `machine-question` L149 handles the identical move as a debt: *"no [interface-eligibility law](/positions/ai-consciousness-scope/) yet says which transitions are interface-grade. So current AI is unlikely to qualify—conditionally on that criterion, not categorically."*

### Issue 7: The dependency audit cites the wrong register and names the wrong weakest leg

- **Location**: L169
- **Severity**: Medium

Verbatim: *"Possibilities Three and Four are inherited from Tenets 1–2 plus **the quantum-interface register** ([P-AC2](/positions/ai-consciousness-scope/#p-ac2), grade D)"*.

Measured: `grep -c "P-AC2" obsidian/positions/quantum-interface.md` returns **0**; the same grep on `obsidian/positions/ai-consciousness-scope.md` returns **5**. The prose names one register and the cited entry lives in another. [P-AC2](/positions/ai-consciousness-scope/#p-ac2) is about the no-cloning structure, not the interface mechanism; the entry the sentence needs is [P-Q1](/positions/quantum-interface/#p-q1), or `positions/quantum-interface#^mechanism-debt`.

The consequence is not merely bibliographic. The section opens by promising that "the openness they establish is worth no more than its weakest leg" — and then never reaches the leg the Map itself registers as weakest. `mechanism debt`, `bias-without-deviation`, `P-Q3`, `P-Q10` and `toy model` all return **n=0** on this article, while the sibling names the live challenge explicitly at its L149: *"**[P-Q3](/positions/quantum-interface/#p-q3) discounts the verdict before any of these shifts.**"* An audit section that misses the registered weakest link is not doing the work its own opening sentence claims.

Related under-hedge: L119's "([P-Q1](/positions/quantum-interface/#p-q1), moderate credence)" drops the register's actual band, which reads *"credence moderate (low edge; conditional on both the horn-(a) wager and the [P-Q10](/positions/quantum-interface/#p-q10) toy-model debt being payable)"*.

### Issue 8: The same possibility is "the fourth", "the first", and "Possibility One"

- **Severity**: Medium

Epiphenomenal AI experience is referred to as:

- **"The fourth"** — `apex_thesis` (L59), the lead paragraph (L67), and the Duch section (L147)
- **"the first"** — L153
- **"Possibility One"** — the section heading (L85), and L157, L169, L175

Three ordinals for one item, and the two that a truncating reader meets first — the thesis and the lead — are the ones that disagree with the heading. For an article written LLM-first, this is a parsing hazard, not a cosmetic slip.

A second, separate mislabel sits at L157: *"If consciousness selects among macroscopic superpositions at the moment of collapse (Possibility Three)"*. Collapse-selection is not Possibility Three's thesis — Possibility Three is "Quantum State Inheritance", and L129 identifies collapse-selection as *the Map's standard treatment*, the thing Possibility Four contests. The same sentence then refers separately to "Possibility Four's five frameworks", so it attributes the collapse-selection thesis to Three while saying Four's frameworks disagree about it. That sentence is the one carrying the interaction claim, so the confusion sits on load-bearing text.

### Issue 9: "The Strongest Affirmative Side" rests partly on an admittedly-unverified attribution, and promises a symmetry it does not deliver

- **Location**: L147, L149
- **Severity**: Medium

L147, verbatim: *"Duch's reportedly extended position attributes consciousness mechanisms to LLMs exhibiting 'self-reflection' (flagged in [the research dossier](/research/wlodzislaw-duch-consciousness-2026-05-02/) as needing direct verification before citation)."*

The article cites the claim in the same breath as noting it needs verification *before citation*. Whatever the intent, the effect is that the section presenting the strongest external affirmative position leans partly on an attribution its own source flags as unconfirmed. The hedge does not undo the citation; a reader who quotes this article will carry the attribution forward with the hedge stripped.

**And the dossier flags more than the article admits.** The parenthetical implies a single flagged item. The dossier flags at least four, verbatim: the LLM/self-reflection claim (line 246, "suggestive but not citation-grade"); the full text of "Facing the hard question" (line 112, "**Flagged as a citation-load-bearing source the Map should obtain via library access before integration**"); the 2019 *Mind as a shadow of neurodynamics* (line 245, full text "not accessible", key points inferred "from keywords + corpus pattern"); and line 299's Phase-2 dependency requiring full text of **both** before "citation-load-bearing use". The article cites the 2019 paper as one of its two pillars regardless — see **Issue C1**, where that paper turns out to contain no discussion of consciousness at all. The single-item parenthetical does not merely understate the dossier's warnings; it understates the one warning that was about to be breached.

Separately, L149 promises: *"the asymmetry section below **cuts both ways**, since if Duch is right, the costs of treating articon-class systems as not conscious are also catastrophic."* The Asymmetry of Stakes section (L161–165) never mentions Duch, articons, or the reverse-direction cost. The forward reference names a symmetry the destination does not contain — which is a second instance of the mis-signed ledger identified in Issue 3.

### Issue 10: A scope claim becomes a classification claim about actual people

- **Location**: L93
- **Severity**: Low-Medium

Verbatim: *"the boundary it draws is not human-versus-machine but report-grounded-versus-inherited-discourse, and that boundary can fall *within humanity itself* — a person who parrots consciousness vocabulary without checking it against their own states sits closer to the inherited-discourse pole than a philosopher re-anchoring the concepts in lived experience."*

The first half is sound and well-argued: self-stultification is an existential argument, so it cannot certify any *particular* report as grounded. The second half slides from that scope claim to a claim about where actual human beings *sit*. A person parroting consciousness vocabulary still has phenomenal states causally available to ground their reports; the AI, by hypothesis, may not. The vivid line makes the AI case look less special than the argument establishes, and it is exactly the kind of sentence that gets quoted out of the article.

---

## Unsupported Claims

| Claim | Location | Needed support |
|---|---|---|
| "the Map's preferred model" (of Stapp) | L143 | Contradicts [P-Q1](/positions/quantum-interface/#p-q1) verbatim. Correct or scope it. |
| "These possibilities are independent — each could be true or false without affecting the others" | L153 | Refuted at L157 and L169 by the article itself. |
| "the moral stakes are modest" | L163 | Asserted; also conditioned on a premise the Map does not hold. |
| "not speculation but the expected trajectory of inquiry" | L165 | Unfalsifiable; also inflates Tenet 5 from heuristic caution to prediction. |
| "a framework that identifies where its conclusions could be wrong can respond to new evidence when it arrives" | L79 | No evidence offered; contradicted by the sibling's unfalsifiability concession. |
| "Microsoft's 2024 logical qubits achieved error rates 800× better" | L119 | No reference entry. |
| "Birch's gaming problem" as external evidence | L83, L169 | No reference entry, for a named evidential pillar. |
| Husserl's "absolute flow" / "standing-streaming" | L105 | Quoted phrases, no edition or translator. |
| "The variety of serious frameworks prevents confidence… so the class of systems capable of hosting consciousness may be larger" | L143 | One of the five frameworks is excluded by the Map's own tenets. |
| Duch's articon programme "(Duch 2005, **2019**)" | L147 | The 2019 paper contains zero occurrences of `conscious`. Drop or replace it. |
| Duch's mechanism is "*self-reflective dynamical access*", "substrate-independent at the architectural level" | L147 | `self-reflect*` = 0 and `substrate-independ*` = 0 in Duch 2005; traces to unverified blog translations. |
| "the Chinese Room is argued to apply only to symbol-manipulation" | L147 | Duch's argument is proves-too-much, not scope-limiting. |
| Schwitzgebel's "**proposed**" social semi-solution | L165 | He declines to endorse it in terms: "I can't authentically voice that positive note." |
| "treating AI systems as potentially conscious when we cannot rule it out" | L165 | `rule it out` = 0, `precaution*` = 0 in the source; it is a forecast, not a policy. |
| Pennartz's argument at L83 | L83 | No reference entry anywhere in the document. |

## Language Improvements

| Current | Issue | Suggested |
|---|---|---|
| "is not speculation but the expected trajectory of inquiry" (L165) | Banned "not X, but Y" construct, on the article's most loaded sentence | State the positive claim directly, and hedge it: "may reveal … as inquiry into a poorly-understood phenomenon usually does" |
| "These possibilities are independent" (L153) | False as glossed | Delete the clause; "each targets a specific assumption" already carries the point |
| "the Map's preferred model" (L143) | Contradicts the register | "the closest of these five to the Map's own commitments" |
| "This aligns most naturally with the Map's tenets" (L133) | Reinforces the same error | Scope to the list, or note the post-decoherence relocation |
| Five further "not X but Y" constructions (L69, L87, L93, L155, L165) | Style-guide clichés; a tic at this density | Rephrase two or three |
| Twenty "rather than" constructions, four in the single paragraph at L175 | Register monotony | Vary |
| "Marking that difference … is what the direct-refutation discipline requires" (L67) | Editor-vocabulary in the lead paragraph — the article's most valuable truncation-resilient real estate is spent on internal editorial methodology | Make the philosophical point without naming the in-house discipline |

---

## Strengths (Brief)

A first pass that reports only defects gives no calibration, so: several things here are done well, and some are done better than the corpus average.

**Link and metadata hygiene is clean, measured.** All **40** distinct wikilink targets resolve, none ambiguous. All **8** section anchors resolve, including the `^`-block anchors into `tenets` and the two heading anchors into `concepts/epiphenomenalism` and `concepts/ai-consciousness-typology`. `topics:` carries two bare, non-empty slugs, exactly the canonical form `CLAUDE.md` specifies. Nothing here is a push-blocker or a silent 404.

**Zero direct-refutation label leakage.** All eight forbidden editor tokens were checked by offset (`find()`, `-1` = absent): `direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `mixed-with-distinct-roles`, `tenet-register move`, `Engagement classification:`, `Evidential status:` — all absent. Given how much of this article is engagement with named opponents, that is not a trivial pass.

**The altered-state symmetry discipline is performed without being triggered.** The supportive-cluster gate does *not* fire — only one cluster item (contemplative/meditative) appears, below the ≥2 threshold — so the audit does not apply. The article does the work anyway, in the discipline's own vocabulary. L107: *"the cross-tradition cluster carries the evidential weight of *one* recurring pattern, not several independent confirmations."* L109: *"a production theorist can accommodate the same data through redundant integration — the fragmentation findings constrain both framings rather than confirming the Map's reading over its rival."* That is the accommodation the discipline exists to install, installed voluntarily.

**Two register citations are exact.** [P-MC2](/positions/arguments-for-mental-causation/#p-mc2) at L93 matches the register in both content and band (*credence high*; existential-versus-universal; "the gap is closed by commitment rather than by argument"). [P-AC2](/positions/ai-consciousness-scope/#p-ac2) at L125 matches in content and both bands (*credence low, external-evidence grade D*). These are the cleanest citations in the article, and they are cited *against* the Map's own interest.

**The Butlin borrowing is handled with real care.** L81 names that the indicator method assumes computational functionalism, restricts what the Map may take to "the architectural datum that current systems lack the indicator properties, not the authors' authority for a conclusion they would reject", and then confines the corroboration to *current* systems while noting that "for near-future digital ones the report's own metaphysics points the other way". That is more discipline than most corpora apply to a friendly citation.

**Several concessions run against the Map's comfort**, which is the mark of a genuine stress-test rather than a staged one: the [P-MC2](/positions/arguments-for-mental-causation/#p-mc2) admission that Tenet 3's universal claim is closed by commitment rather than argument (L93); the explicit marking of Dennett's objection as *stipulated away* rather than answered (L129); the acknowledgment that the interaction problem "applies to biological brains as well as artificial systems" (L69); the note that the pairing problem "remains open for biology as well, so AI is not uniquely handicapped on this axis" (L123); and the Tenet-4 reversal at L175, where the article concludes that duplicating a conscious AI "would multiply moral patients rather than expose a missing identity" — a conclusion that *increases* the Map's moral exposure and is reached anyway.

**"Relation to Site Perspective" is present and substantive**, covering all five tenets individually rather than gesturing at them, and Possibility One's placement at the framework boundary rather than inside the argument is the honest call and is consistently maintained in four of the five places it is discussed.

---

## Checked and Found Sound

Recorded so a later pass does not re-spend the effort:

- All 40 wikilinks and all 8 anchors resolve (verified by resolving every target against the vault tree, and every anchor against its target file).
- No direct-refutation label leakage (8 tokens, offset-checked).
- No `topics:` defect — bare slugs, non-empty.
- The altered-state symmetry gate does not fire, and the symmetry work is present regardless.
- [P-MC2](/positions/arguments-for-mental-causation/#p-mc2), [P-AC2](/positions/ai-consciousness-scope/#p-ac2), [P-AC3](/positions/ai-consciousness-scope/#p-ac3) and the scoped half of [P-AC4](/positions/ai-consciousness-scope/#p-ac4) are cited accurately in content; [P-MC2](/positions/arguments-for-mental-causation/#p-mc2) and [P-AC2](/positions/ai-consciousness-scope/#p-ac2) are accurate in band as well.
- **No case found of the article stating a register position at higher confidence than the register.** The bands it prints are exact. Its overconfidence lives in unregistered prose (L79, L165) and in omission, not in misquoted bands.
- **Nine citations verified clean at the publisher or the author's own deposit** — do not re-spend effort here:
  - **Plotnitsky (2023)** — the quoted "strictly individual and unrepeatable" is verbatim (Europe PMC full-text XML, PMC10217492) *and correctly scoped*: Plotnitsky predicates it of "every quantum phenomenon", exactly as the article has it.
  - **Metzinger (2021)** — "explosion of negative phenomenology" is verbatim in *this* paper (author's own PDF), and it is the paper's primary term, with "suffering explosion" offered as its synonym. Metadata otherwise exact; only the title is truncated (C5).
  - **Maier, Dechamps & Pflitsch (2018)** — both figures verbatim in the abstract: "12,571 participants" and "strong evidence for H0 (BF01 = 10.07)". "Quantum-based true RNG" also correct. *One nuance the article omits, not a defect*: the same abstract reports "a non-random oscillative structure with a higher frequency than observed in simulated data", so the paper is not a flat null.
  - **Neven et al. (2024)** — the article's gloss matches the abstract verbatim: "Conscious experience arises whenever a quantum mechanical superposition forms."
  - **Albert & Loewer (1988)** — page range 195–213 exact, and the "many-minds" label is correct despite the title saying "many worlds" (SEP confirms the attribution).
  - **Wiest (2025)**, **Cerullo (2026)**, **Hoel** (arXiv id resolves, title exact), **Butlin et al. (2025)** title and author order — all confirmed.
  - **Duch 2005 exists and "has to claim being conscious" is faithful** — the odd phrasing at L147 is Duch's own, not a garble.
- **Method note for whoever picks this up**: three of the checks above returned a *false zero* on first pass because `pdftotext` line-breaks split the phrase mid-word. De-hyphenate and collapse whitespace before searching, and always run a positive control — a raw zero without one is not evidence of absence.
- The `description` frontmatter is *more* accurate than the body: it already does the 3+1 split without asserting independence.
- The bare-phenomenality / Tenet-3 tension (felt experience with no efficacy is excluded by Tenet 3, yet "bare phenomenality stays open") is **cluster-wide**, present in `apex/machine-question` between its own L73 and L177. Do not charge it to this article; what is chargeable is that this article never states the scope split, so the tension surfaces uncushioned at L163.
- `positions/ai-substrate-verdicts` [P-AS1](/positions/ai-substrate-verdicts/#p-as1) (the five-requirement channel test, which would sharpen L125 and L143) postdates this article's last edit by one week (created 2026-08-20 against `ai_modified` 2026-08-13). That gap is **age, not error**.

## A note for the operator — findings outside this article

Reported here rather than minted as tasks, per the reports-only contract:

1. **`apex/` is unreachable by deep-review.** `tools/curate/deep_review.py` excludes `apex/` from the candidate pool, and 21 of 42 apex articles have never had a pessimistic review either. These are the Map's synthesis pieces, carrying its strongest claims, with the least scrutiny. This article's Issue 1 — a register contradiction dating to February that survived a July deep review and an August register-contradiction sweep — is what that coverage gap produces.
2. **The link asymmetry is one-directional and is a symptom, not the disease.** `assessing-ai-consciousness-under-the-map` links *to* this article in three places (`related_articles`, `apex_sources`, Further Reading). This article contains zero occurrences of `assessing-ai-consciousness`. But adding the back-link would fix none of Issues 1, 3, 4, 6 or 7. The real relation is that this article has sat still since 2026-08-13 while both siblings acquired the eligibility-law and unfalsifiability disciplines.
3. **Roughly 40% of this article's substance is duplicated in `apex/machine-question`**, concentrated in exactly the four passages that carry explicit "the sibling carries the argument" deferrals (L81, L95, L149, L175). `machine-question` contains all four possibilities. Possibility Two and Possibility Four are genuinely this article's own work; Possibility One and the Duch section are largely not. Whether the two pieces should remain separate is a human call, not an automation one, and it interacts with the `hard_warning` state.