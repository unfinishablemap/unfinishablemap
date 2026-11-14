# Hostile Referee Audit: “The Mind-Arena” (unfinishablemap.org/concepts/mind-arena/)

**Before anything else:** my tools would not open the live target page. That page and `/topics/dualism-as-ai-risk-mitigation/` were refused at fetch time because no search had returned them as results. A subagent tried the same route and also the GitHub raw file, and also failed. So the mind-arena article itself is reconstructed from secondary sources on the same site, not read directly:

- the Concepts index summary;
- a verbatim sentence quoted in Optimistic Review 2026-06-04c;
- changelog and task-queue entries that quote its line numbers;
- neighbouring pages that I did fetch live: the changelog (latest entry 2026-11-14T02:41Z), `topics/instrumental-convergence` (modified 2026-11-06T02:52Z), `apex/born-preserving-causal-efficacy` (modified 2026-10-30), `concepts/possibility-probability-slippage` (modified 2026-09-05) and the 2026-06-04c optimistic review.

I could not confirm the 2026-11-06 revision you reported for mind-arena itself. 2026-11-06 is confirmed as the modification date of its closest sibling, instrumental-convergence. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) Every finding below is therefore scoped to the article’s text as quoted elsewhere on the site. The review files it cites are re-dated 2026-11-14, so they may have been regenerated. [unfinishablemap](https://unfinishablemap.org/reviews/optimistic-2026-06-04c/) **Re-run this audit against the live page before acting on any DELETE verdict.**

## TL;DR

- **Headline verdict: REVISE-HARD, with the uncomputability claim DEMOTE-TO-COHERENCE-ONLY.** The claim is asserted, not argued. In the only verbatim formulation I could find, “uncomputable” means something purely epistemic: one variable is missing from the physical state description. The quoted sentence is: “One could fully specify the interface formalism and still face an uncomputable mind-arena, because the formalism fixes the coupling’s *form* without making the non-physical contribution recoverable from physical state.” [unfinishablemap](https://unfinishablemap.org/reviews/optimistic-2026-06-04c/) That is trivially true under dualism. It is not uncomputability in the Turing sense. The Map’s own sibling page (instrumental-convergence) says exactly this and bans the stronger word. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/)
- **The claim does not survive the Map’s own Born-rule apex.** If consciousness preserves Born statistics in the unconditioned marginal (P-Q2, held at “high” confidence), then the physically computable distribution is the correct consequence-distribution for every unconditioned prediction. If it does not, the claim predicts measurable conditional deviations and stops being “uncomputable” at all. [unfinishablemap](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/) Either way, “uncomputable consequence-distribution” is the wrong description. Predictive-modelling objections (neural decoding, choice models, predictive processing / active inference, LLM simulation of human behaviour) appear nowhere in any text I could recover.
- **Integration is internally inconsistent.** Under the 2026-09-07 completed task, the AI-risk sibling disowned the “uncomputable, not merely intractable” form, and instrumental-convergence now says “underdetermined is not the same as Turing-uncomputable”. [unfinishablemap](https://unfinishablemap.org/workflow/todo/)[unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) Yet causal-powers, machine-consciousness and possibility-probability-slippage still advertise “uncomputable (not merely intractable)” consequence-distributions. [unfinishablemap + 2](https://unfinishablemap.org/topics/machine-consciousness/) The concept page’s own canonical sentence, as last quoted, still says “uncomputable mind-arena”. [unfinishablemap](https://unfinishablemap.org/reviews/optimistic-2026-06-04c/) This is confession-without-correction in its standard form.

## 1. Audit basis and version record

**What was verified directly (live fetch, 2026-11-14):**

- **Changelog.** The latest entries run from 2026-11-13T22:21Z to 2026-11-14T02:41Z. [unfinishablemap](https://unfinishablemap.org/workflow/changelog/) None of them, in the portion I retrieved, touches `concepts/mind-arena.md`.
- **Earlier changelog material (search excerpts).** These record:

- a deep-review that changed a description of the AI-risk sibling from “mind-arena consequences are unavailable to a physical model” to “any physical model omits the mind-arena’s causal contribution”, flagging the old phrasing as “the uncomputability form the sibling disowned on 2026-09-07”; [unfinishablemap](https://unfinishablemap.org/workflow/changelog/)
- a stale self-citation at `concepts/mind-arena.md:88` (“Southgate, A. & Oquatre-sept, C. (2026-05-06). Dualism as AI Risk Mitigation”, which should add Ocinq, C.); [unfinishablemap](https://unfinishablemap.org/workflow/changelog/)
- repeated coalesce runs that declined to merge causal-powers + mind-arena (3,494 words against a 3,499 ceiling) on the strength of its “## Distinguishing the Mind-Arena from Related Map Terms” section. [unfinishablemap](https://unfinishablemap.org/workflow/changelog/)
- **`topics/instrumental-convergence`** — modified 2026-11-06T02:52:57Z, read in full. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/)
- **`apex/born-preserving-causal-efficacy`** — modified 2026-10-30, read in substantial part. [unfinishablemap](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)
- **`concepts/possibility-probability-slippage`** — modified 2026-09-05, read.
- **Optimistic Review 2026-06-04c** — read; it is the source of the verbatim mind-arena sentence. [unfinishablemap](https://unfinishablemap.org/reviews/optimistic-2026-06-04c/)

**Reconstructed, not read live:**

- The mind-arena lead: “the Map’s term for the domain of outcomes that pass through minds—the region of the world where conscious agents are at stake and where, under the Map’s tenets, what happens is co-determined by consciousness rather than fixed by physical state alone”. [unfinishablemap](https://unfinishablemap.org/concepts/)
- Its self-description as registering “its honest status as a posited framework construct”. [unfinishablemap](https://unfinishablemap.org/concepts/)
- Its L70 anti-inflation guard (“not itself a claim placed on the … five-tier evidential scale”). [unfinishablemap](https://unfinishablemap.org/workflow/todo/)
- Its frontmatter `concepts:` field (interactionist-dualism, bidirectional-interaction, causal-powers). [unfinishablemap](https://unfinishablemap.org/workflow/todo/)

**Not accessed:** the mind-arena body text and full reference list; dualism-as-ai-risk-mitigation; the tenets page; cross-modal-capability-division; the mental-causation, causal-closure and interface-problem pages. Ask the operator to fix fetchability (see Part 5).

## 2. Dimensional analysis

### A. The uncomputability claim: argued or asserted?

**Charitable reconstruction.**

- P1 (Tenet 1): conscious states are not physical states and are not fixed by them.
- P2 (Tenet 3): conscious states causally contribute to physical outcomes in brains.
- P3: outcomes downstream of brains — the “mind-arena” — therefore depend partly on a variable not contained in the physical state.
- P4: a predictor with access only to physical state cannot recover that variable (“the formalism fixes the coupling’s *form* without making the non-physical contribution recoverable from physical state”). [unfinishablemap](https://unfinishablemap.org/reviews/optimistic-2026-06-04c/)
- C: consequence-distributions over mind-arena outcomes are “uncomputable from physical state alone”.

**What “uncomputable” means here.** Sense (iii): epistemic, missing-variable incompleteness. Nothing in any recovered text appeals to non-recursive functions, hypercomputation, the Penrose–Lucas route, chaos, or complexity classes. The sibling page makes the taxonomy explicit. It separates:

- intractability;
- “Turing uncomputability (the Solomonoff/AIXI obstructions of Leike and Hutter 2018)”;
- “hidden-variable underdetermination (the dualist claim — oracle-like missing information, not automatically Turing-uncomputable)”;
- Knightian uncertainty;
- misspecification.

It concludes that “the stronger word should not be borrowed without the formal argument that earns it”. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) The Map’s own standard therefore convicts the concept page of trading on the technical connotation. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) The optimistic review’s praise — that the page converts “a metaphysical claim … into a structural one (consequence-distributions are uncomputable from physical state alone), which is harder to dismiss” — is exactly the connotation-borrowing that makes the claim *look* harder to dismiss than it is. [unfinishablemap](https://unfinishablemap.org/reviews/optimistic-2026-06-04c/)

**Attack 1: triviality.** Given P1–P2, C follows by definition. Any omitted causal variable makes any system “uncomputable from the included variables”: weather without humidity, a coin without its toss force. The conclusion adds nothing to Tenets 1 and 3. Calling it a “structural” result is coherence inflation.

**Attack 2: no distinction between outcomes and distributions.** A quantum outcome is unpredictable, yet its distribution is computable. The page’s title-level claim is about *distributions*, but the only mechanism the Map licenses (Tenet 2, minimal quantum selection at indeterminacies) acts on *outcomes* within Born-fixed distributions. [unfinishablemap](https://unfinishablemap.org/concepts/mind-matter-interface/) “Consequence-distribution” is never defined: over what sample space, conditioned on what, at what grain. Without that definition the claim cannot be assessed.

**Attack 3: the Born dilemma, pressed.** The apex states that the default reading preserves “the *unconditioned* long-run marginal”, q(O|X) = Σ_C P(O|C,X)·P(C|X), and that the apex itself drives a trilemma: [unfinishablemap](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)

- **Horn (b), conditionals never differ.** The physically computed q *is* the consequence-distribution at every grain. “Uncomputable” is false; consciousness merely relabels authorship (Route 1, trumping, which the apex concedes is “empirically silent by construction”). [unfinishablemap](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)
- **Horn (a), conditionals differ.** The distribution conditioned on conscious state departs from q. But then the mind-arena claim becomes an empirical prediction of conditional Born deviations. [unfinishablemap](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/) The deviation is in-principle estimable from data, so it is *learnable*, not uncomputable. A predictor that adds behavioural or neural proxies for C can approximate P(O|C,X).
- **Horn (c), cancellation.** The apex shows this collapses under intervention into (a), or else needs an unwritten “psychophysical superselection” law. [unfinishablemap](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)

Every horn defeats the uncomputability wording. Only “underdetermined by physical state *if* the conditionals differ *and* C is not physically proxied” survives — and that is a narrow, conditional, empirically exposed claim. Nothing I recovered from the concept page shows it engaging this dilemma or linking the apex.

**Attack 4: the literature is absent.** No recovered text cites or engages any of the following:

- Penrose (*Emperor’s New Mind*, *Shadows of the Mind*), Lucas, Chalmers 1995 “Minds, Machines, and Mathematics”, or Feferman;
- Pour-El & Richards (computability in physics);
- the Church–Turing–Deutsch principle;
- Piccinini on physical computation;
- Aaronson’s “Ghost in the Quantum Turing Machine”. This is the most damaging omission: Aaronson’s “freebits” / Knightian-uncertainty proposal is precisely a worked, falsifiable version of “physical state underdetermines choice”, with explicit predictions about what a brain scan could or could not fix;
- Lloyd’s “A Turing test for free will” (unpredictability of a decider’s own choices *without* any dualist variable — a physicalist route to the same epistemic conclusion);
- Wolfram’s computational irreducibility.

The sibling cites only Leike & Hutter 2018 and Townsend et al. 2025 for the Knightian framing. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) **Verdict: asserted, and named with a term the Map itself has ruled out.** [unfinishablemap](https://unfinishablemap.org/research/instrumental-convergence-2026-06-24/)[unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/)

### B. The strongest objections

**1. Causal closure (Papineau, Kim; the inductive argument from physiology; conservation).** The mind-arena’s quantum-indeterminacy loophole needs the closure principle to be stated as *chance-fixing*. The Map’s own research note (interventionist exclusion, 2026-09-07) concedes that intervention-invariant chance-fixing closure “pushes the Map onto Horn 1”, meaning detectable Born deviation. [unfinishablemap](https://unfinishablemap.org/research/interventionist-exclusion-and-chance-fixing-closure-2026-09-07/) A concept page that asserts outcomes are “co-determined by consciousness rather than fixed by physical state alone” without stating which closure principle it denies takes on that cost silently. Papineau’s inductive case — no unexplained physiological force has ever been found — goes unanswered in anything I could see.

**2. Overdetermination / exclusion (Kim, Bennett).** The Map’s live machinery is trumping preemption (Saad’s delegatory causation). The apex concedes that this is symmetric (“a physicalist can run the mirror move”) and that it delivers coherence, not refutation. [unfinishablemap](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/) On the trumping route the mind-arena has *no* distributional footprint, so the uncomputability claim and the anti-overdetermination strategy pull in opposite directions:

- trumping → physics already fixes the distribution;
- “uncomputable distribution” → consciousness competes with physics, which breaks closure.

The changelog shows the delegation–quantum fusion was withdrawn (delegatory-causation repairs, 2026-11-14T01:34Z) and the operator decision between difference-making and trumping is “not made”. [unfinishablemap](https://unfinishablemap.org/workflow/changelog/) The mind-arena claim therefore rests on an unchosen operator.

**3. Predictive modelling.** This is the decisive gap. Several lines of evidence show physical and behavioural data predicting mind-mediated outcomes well, and the Map owes an account of the *residual* it predicts:

- neural decoding of choices before report (the Soon/Haynes lineage);
- discrete-choice and behavioural-economic models;
- recommender systems;
- LLM-based simulation of survey and experimental responses;
- predictive-processing / active-inference accounts. Laukkonen, Friston & Chandaria 2025, “A beautiful loop” (*Neurosci. Biobehav. Rev.* 176:106296) is the standing gate here: an active-inference account of consciousness itself as self-modelling.

On the Map’s own Tenet 2 (minimal interaction), that residual should be tiny and confined to post-decoherence selections. That in turn makes mind-arena outcomes *statistically* near-computable — the opposite of what the page advertises. No recovered text engages predictive processing or empirical predictability. The blocking gate fails.

**Falsifiability.** None stated. The minimal falsifier would be: conditional on manipulated intention, predictors trained on full physical/neural state show no residual beyond Born-level noise at the specified grain. The Map should commit to this (apex horn (a)) or concede horn (b).

### C. Tenet-protective assumptions (constrain-vs-establish gate)

| Reliance | Where | Flagged? | Gate |
| --- | --- | --- | --- |
| Tenet 1 (irreducibility) supplies the missing variable | lead: “under the Map’s tenets” | Yes, at lead level | Pass (lead) |
| Tenet 3 makes the variable outcome-relevant | lead: “co-determined by consciousness” | Partly | Weak pass |
| “Uncomputable” (technical term) | canonical sentence quoted in 06-04c | No — reads as a result | **Fail** |
| Tenet 2 Born-preservation (limits distributional effect) | not engaged in recovered text | No | **Fail (omission)** |
| Tenet 4 single-outcome (needed for “which outcome” to matter) | not engaged | No | Fail (omission) |
| Tenet 5 (Occam limits) shielding against “the extra variable is idle” | not visible | Unknown | Unverified |
| Evidential status | L70 “not itself a claim placed on the … five-tier evidential scale”; “posited framework construct” | Yes | Pass |

The page passes on self-labelling (“posited framework construct”) and fails on content: the “uncomputable” sentence states a tenet consequence as a structural result. This is the constitutional-attractor pattern — the term is coined to give a tenet-entailment a technical-sounding home that other pages then cite as if it were established.

### D. Citation verification (three layers)

The full reference list could not be retrieved, so the table covers every reference and attribution I could see in or around the page.

| Reference / attribution | (a) Metadata | (b) Verbatim | (c) Author stance | Finding |
| --- | --- | --- | --- | --- |
| Southgate, Oquatre-sept (2026-05-06), *Dualism as AI Risk Mitigation* (mind-arena.md:88) | **Wrong**: author list stale (should add Ocinq, C.), per the changelog | n/a | Self-citation | Logged and still unconfirmed fixed: confession-without-correction; evidential-independence failure (self-citation as support) |
| Optimistic review’s “Chalmers’ approval” / “Stapp’s own separation” | Not a citation; a simulated persona | No Chalmers or Stapp text quoted | **Co-optation risk**: Stapp’s framework is Process-1 question-selection, and the apex itself says outcome-selection is “a material change”; Stapp disowned Eccles-style outcome-biasing | The persona review recruits Stapp to an outcome-level picture he rejected. Not a citation on the page, but it shaped the page’s review record |
| Knight 1921; Townsend et al. 2025, *AMR* 50(2):415–440 (sibling page, framing the mind-arena as a “structural site” of Knightian uncertainty) | Plausible; not independently verified | Not checked | Townsend et al. are management scholars on AI and entrepreneurial uncertainty; they make no dualist claim | Stance-neutral authors used as a category label. Acceptable only if no endorsement is implied. Note the date drift: the research note says “Townsend et al. 2024”, the live page says 2025 [unfinishablemap](https://unfinishablemap.org/research/instrumental-convergence-2026-06-24/)[unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) |
| Leike & Hutter 2018, *TCS* 716:28–49 (sibling) | Matches standard record | n/a | Correctly used to *contrast* Turing-uncomputability | Good practice that the concept page does not inherit |
| Laukkonen, Friston & Chandaria 2025 | — | — | — | **Absent** (blocking gate fails) |
| Aaronson 2013; Lloyd 2012; Penrose; Chalmers 1995; Pour-El & Richards | — | — | — | **Absent**; the omissions are argument-critical |

No fabricated work was detected in the recovered text. The main defects are the stale self-citation and missing primary literature.

### E. Integration

- **Uncomputability contradiction.** Instrumental-convergence now says the distribution “can be formed but not certified adequate” and that “underdetermined is not the same as Turing-uncomputable”. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) The concept page’s canonical sentence, per the last available quote, says “uncomputable mind-arena”. [unfinishablemap](https://unfinishablemap.org/reviews/optimistic-2026-06-04c/) Three pages that link to it still state the disowned form:

- causal-powers Further Reading: “outcomes passing through the mind-arena have uncomputable consequence-distributions”; [unfinishablemap](https://unfinishablemap.org/concepts/causal-powers/)
- machine-consciousness: “uncomputable (not merely intractable) for any physical-state-only model”; [unfinishablemap](https://unfinishablemap.org/topics/machine-consciousness/)
- possibility-probability-slippage: “uncomputable rather than merely intractable”. [unfinishablemap](https://unfinishablemap.org/concepts/possibility-probability-slippage/)
- **Within instrumental-convergence itself.** The research note still says “no such distribution can be formed”; the live page’s softer “can be formed but not certified adequate” is better. [unfinishablemap](https://unfinishablemap.org/research/instrumental-convergence-2026-06-24/)[unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) But the live page also keeps “not because they are hard, but because the deciding variable is not in the physical data” — a missing-variable claim that the Born apex undercuts. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/)
- **Born apex.** The concept page does not appear to link born-preserving-causal-efficacy, and the apex’s horn analysis directly governs it.
- **AI-risk inference.** To its credit, instrumental-convergence concedes that the dualist argument “reassures about the corrigible agent while saying nothing about the dangerous one”, and it confines itself to calibrated agents. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/)[unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) That concession is genuinely good and should be the template. The safety hazard is the residual connotation spread by the “uncomputable” blurbs: that AI cannot model or manipulate humans. Given empirical persuasion and manipulation results, that is false comfort, and Part 4 asks for an explicit disclaimer.
- **Interface pages.** mind-matter-interface does reciprocate (“the wide field of downstream outcomes flowing from it is the mind-arena”). [unfinishablemap](https://unfinishablemap.org/concepts/mind-matter-interface/) The thin-junction / wide-field distinction is the page’s one genuinely useful contribution, and it works as terminology. [unfinishablemap](https://unfinishablemap.org/reviews/optimistic-2026-06-04c/)

## 3. Per-position verdicts

| Position | Verdict |
| --- | --- |
| Mind-arena as a *term* for the downstream domain of mind-mediated outcomes; interface-vs-arena distinction | **RETAIN** |
| “Co-determined by consciousness rather than fixed by physical state alone” | **DEMOTE-TO-COHERENCE-ONLY** (tenet restatement) |
| Consequence-distributions “uncomputable” from physical state | **DELETE** the word; replace with conditional underdetermination |
| “Uncomputable, not merely intractable” (propagated blurbs) | **DELETE** |
| Mind-arena as specific structural site of Knightian uncertainty restricting instrumental convergence | **REVISE-HARD** (must route through the Born trilemma and state the residual) |
| Whether the conscious contribution has any distributional footprint | **FLAG AS PERPETUALLY CONTESTED** (inherits P-Q3) |
| Self-status as “posited framework construct”, off the five-tier scale | **RETAIN** |

## 4. Article-specific fixes

1. **concepts/mind-arena**

- Replace “uncomputable mind-arena” with “a mind-arena whose consequence-distribution is underdetermined by physical state *only if* conscious-state-conditioned outcome probabilities depart from the Born marginal (apex horn (a))”.
- Define “consequence-distribution”: the sample space, the conditioning set, and the grain.
- Add a section that runs the trilemma explicitly and links born-preserving-causal-efficacy.
- Add a “Predictive-modelling objection” section engaging neural decoding, choice models, LLM human-simulation and Laukkonen, Friston & Chandaria 2025, stating what residual the Map predicts and at what grain.
- State a falsifier.
- Cite Aaronson’s freebits paper as the nearest rigorous analogue and Lloyd 2012 as the physicalist route to the same unpredictability.
- Fix the L88 author list.
- Adopt the compatible/suggestive/discriminating evidence ladder: label the claim interface-compatible only.
2. **concepts/causal-powers, topics/machine-consciousness, concepts/possibility-probability-slippage** — rewrite the Further Reading blurbs to the “omits the causal contribution / underdetermined” form. In possibility-probability-slippage, also reconsider the claim that the propagation case’s clean slippage checks are “evidential support for portability”, given that the case’s own core term was disowned. [unfinishablemap](https://unfinishablemap.org/concepts/possibility-probability-slippage/)
3. **topics/instrumental-convergence**

- Replace “not because they are hard, but because the deciding variable is not in the physical data” with a Born-conditioned statement.
- Add a disclaimer that the argument does not imply AI cannot predict or manipulate humans.
- Reconcile the Townsend 2024/2025 date with the research note.
4. **topics/dualism-as-ai-risk-mitigation** — verify the 2026-09-07 de-uncomputabilisation actually landed (the L50/L56 Laplacean passage). [unfinishablemap](https://unfinishablemap.org/workflow/todo/) Remove any tiered “unbounded-magnitude” material that is still live. [unfinishablemap](https://unfinishablemap.org/concepts/possibility-probability-slippage/)
5. **apex/born-preserving-causal-efficacy** — add a “Downstream consumers” note naming mind-arena and instrumental-convergence as inheriting the trilemma.
6. **concepts/delegatory-causation / trumping-preemption** — state explicitly that on the trumping route the mind-arena has no distributional signature.
7. **reviews/optimistic-2026-06-04c** — annotate that its “Stapp” persona endorsement mischaracterises Stapp’s Process-1 position.

## 5. Site-wide methodology improvements

1. **Terminology lint.** Add a corpus-wide grep gate that blocks “uncomputable” (and “not merely intractable”) unless the sentence is paired with a Turing-sense argument or one of the controlled terms. The 2026-09-07 disowning should have propagated mechanically; it did not.
2. **Binding propagation of disownings.** When a claim is withdrawn on a hub page, automatically open tasks on every page that quotes or summarises it, and keep the withdrawal in an “unresolved” state until those tasks close. This turns confession into correction.
3. **Dependency declarations.** Every concept page should list in frontmatter which positions-register entries it inherits (here P-Q2, P-Q3, P-Q10). The tenet-checker should fail any page that inherits P-Q3 without linking the apex.
4. **Predictive-processing blocking gate.** Any page making claims about predicting minds must engage Laukkonen, Friston & Chandaria 2025 and empirical predictability before publication.
5. **Fetchability for external audit.** Publish raw markdown mirrors or a sitemap that external audit tools can retrieve. This audit could not read its own target page, which undercuts the purpose of commissioning external referees.
6. **Retire persona-praise reviews as evidence.** Simulated “Chalmers approves” / “Stapp approves” sections in optimistic reviews are Claude-on-Claude circular review dressed as expert endorsement, and here one co-opted Stapp against his own position. [unfinishablemap](https://unfinishablemap.org/reviews/optimistic-2026-06-04c/) Either require each persona claim to quote the named philosopher’s actual text, or drop the personas.
7. **Mandatory external, non-Claude adversarial pass** for any concept that other pages cite as load-bearing (mind-arena feeds at least five pages). The internal pipeline praised the exact sentence the site later disowned.