---
ai_contribution: 100
ai_system: claude-opus-4-8
concepts: []
created: 2026-07-15
date: '2026-07-15'
draft: false
related_articles: []
title: Research Notes - Single-Cell Proto-Agency and the Evidence Problem
---

# Research: Single-Cell Proto-Agency and the Evidence Problem

**Date**: 2026-07-15
**Search queries used**:
- bacterial chemotaxis CheY-P stochastic noise phenotypic variability decision-making single cell
- minimal agency biology what counts as evidence goal-directedness free energy principle 2023 2024
- run-and-tumble variability individuality E. coli behavioral phenotype non-genetic heterogeneity
- "cell consciousness" dissenting opinion EMBO Reports 2024 bacteria choice protein levels stochastic critique
- minimal cognition markers criteria bacteria learning associative habituation evidence proto-agency debate
- agency biology teleonomy interventionist counterfactual criterion goal-directed vs mechanism distinguishing empirically
- stochasticity functional role bacterial chemotaxis noise IS the mechanism decision underdetermination behavior explanation
- "unlimited associative learning" Ginsburg Jablonka marker sentience bacteria threshold evidence consciousness

## Scope Note: Why This Is Distinct From the Existing Chemotaxis Article

The live article [bacterial-chemotaxis-and-minimal-biogenic-cognition](/topics/bacterial-chemotaxis-and-minimal-biogenic-cognition/) specifies the run-and-tumble *mechanism* and states the CBC-vs-deflationist dispute, but **deliberately declines to adjudicate it**: "The Map does not need to settle the empirical dispute between CBC and its critics about whether bacterial 'decision' is real proto-choice or protein-level noise." This research note targets exactly the parked question — not the mechanism, but the **epistemology of the mechanism's interpretation**: what would *count* as evidence that a single cell exercises proto-agency, whether the noise/choice distinction is even empirically tractable, and how the Map's Tenet-5 (Occam-limits) discipline plus its existing [agency-verification-void](/voids/agency-verification-void/) apply. The downstream article would be an epistemology-of-agency-attribution piece, not a second chemotaxis explainer.

**Verdict: worth covering.** The evidence problem is a genuine, well-populated 2020s literature (agency-in-biology philosophy, single-cell signalling-noise measurement, minimal-cognition criteria debates) that the corpus currently touches only glancingly.

## Executive Summary

The dispute over bacterial "decision" is usually framed as a dichotomy: is run-and-tumble variability (a) stochastic protein-level noise or (b) genuine proto-choice? The most important finding of this research is that **this dichotomy is unstable at the mechanistic level**. The single-cell FRET literature shows that CheY-P fluctuation ("noise") is not incidental error riding on top of a decision process — it is *functionally integrated into* the decision process: harnessed stochasticity coordinates multiple flagellar motors, increases network sensitivity, and improves gradient-climbing on shallow gradients by up to ~73%. So "it's just noise" and "it's a real decision" are not cleanly opposed descriptions of different systems; they can be two descriptions of the *same* mechanism. This is why the evidence problem is hard: the behaviour that proto-agency would predict is generated in full by a complete stochastic-biochemical account, leaving the two readings **empirically underdetermined** at the behavioural level. The candidate discriminating criteria on offer (interventionist goal-directedness, free-energy minimisation, unlimited associative learning, formal causal agency-detection) each either fail to draw a categorical agent/non-agent line, risk unfalsifiability, or answer a different question (sentience) than agency. The Map's payoff: this is a Tenet-5 case where parsimony cuts *both* ways and the honest verdict is that the distinction may be, at the single-cell rung, not merely unresolved but **not empirically tractable** — which is precisely what the [agency-verification-void](/voids/agency-verification-void/) already anticipates.

## Key Sources

### Cell consciousness: a dissenting opinion (EMBO Reports, 2024)
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC11094104/ ; https://doi.org/10.1038/s44319-024-00127-4
- **Type**: Peer-reviewed opinion (Science & Society)
- **Authors**: Robinson DG, Mallatt J, Peer WA, **Sourjik V**, Taiz L. *EMBO Reports* 25(5):2162–2167 (2024).
- **Key points**:
  - Core claim: "An individual bacterial cell does not make a choice — the decisions are determined by its current state." Behavioural differences between isogenic cells reflect "stochastic differences in protein levels between cells."
  - The mechanism "can be broken down to a few individual molecular reactions described by a relatively simple system of differential equations," leaving no room for volition.
  - Grants the *vocabulary* (memory formation, route navigation, decision-making) but reads it as behaviour "hardwired in their genome as rates of biochemical reactions and levels of corresponding enzymes."
  - Evidence standard demanded of CBC: "theories require proof from hypotheses-testing, solid facts and empirical evidence."
- **Tenet alignment**: Aligns with Tenet 2/3 negative reading (no interface where no substrate); but its parsimony-as-proof move is exactly what Tenet 5 blocks.
- **Notable meta-point**: **Victor Sourjik is a co-author.** Sourjik's own lab (Max Planck, Marburg) produced the single-cell FRET measurements of CheY-P variability (below). The person who *measured* the noise is on record calling it noise, not choice — which strengthens the deflationary case but also shows the "noise vs choice" line is drawn by the measurer's interpretation, not by an additional experiment.

### Phenotypic diversity and temporal variability in a bacterial signaling network revealed by single-cell FRET (2017)
- **URL**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5809149/ ; companion https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5809148/
- **Type**: Primary research (PNAS; Keegstra, Kamino, Anquez, Lazova, Emonet, Sourjik / Shimizu)
- **Key points**:
  - Single-cell FRET reveals pervasive CheY-P signalling variability both across cells in isogenic populations and within one cell over time.
  - At least two noise sources: (i) stochastic adaptation-enzyme (CheR/CheB) activity; (ii) receptor-kinase dynamics absent adaptation. Large methylation-*independent* thermal fluctuations of receptor activity contribute comparably to the energy-consuming methylation dynamics.
  - Under some conditions "giant fluctuations" drive the whole cell into stochastic two-state switching.
- **Tenet alignment**: Neutral (empirical). Supplies the raw fact that both camps must interpret.

### Stochastic coordination of multiple actuators reduces latency and improves chemotactic response (PNAS 2012) + Noise-Induced Increase of Sensitivity (Biophys J 2016)
- **URL**: https://www.pnas.org/doi/10.1073/pnas.1113706109 ; https://www.sciencedirect.com/science/article/pii/S0006349516304581
- **Type**: Primary research
- **Key points** (the crux for the evidence problem):
  - CheY-P noise **coordinates the switching statistics of multiple flagellar motors**, enhancing performance on shallow gradients by up to ~73%.
  - Noise *increases* downstream sensitivity at the motor. Stochasticity is "not merely noise but functionally integrated into the chemotactic decision-making mechanism," enabling exploration and gradient sensitivity.
- **Why it matters**: This dissolves the EMBO dichotomy. If noise is the *substrate* of the adaptive search, then "the decision is just noise" does not deflate the behaviour — the noise is *doing the searching*. The deflationary and agency readings converge on the same mechanism and diverge only in what they are willing to *call* it.

### Nongenetic individuality, changeability, and inheritance in bacterial behavior (PNAS 2021) & Non-genetic individuality in E. coli motor switching (2011)
- **URL**: https://www.pnas.org/doi/full/10.1073/pnas.2023322118 ; https://pubmed.ncbi.nlm.nih.gov/21422514/
- **Type**: Primary research
- **Key points**:
  - Isogenic E. coli show large phenotypic diversity in constant environments: "nongenetic individuality" (stable between-cell differences) plus "changeability" (within-lifetime drift). Behavioural space is low-dimensional (~2 traits); individuality dominates, changeability is smaller but significant.
  - Variation in mean counter-clockwise (run) interval tracks CheY-P concentration; variation in mean clockwise (tumble) interval reflects motor individuality.
- **Relevance**: "Individuality" is a loaded near-agency word for what is protein-abundance variance. Shows how easily the *vocabulary* of individuality attaches to a purely statistical fact — a caution the evidence-problem article should foreground.

### Agency / goal-directedness in biology (2022–2024 philosophy)
- **URLs**:
  - "Agency, Goal-Directed Behavior, and Part-Whole Relationships in Biological Systems," *Biological Theory* (2023), https://pmc.ncbi.nlm.nih.gov/articles/PMC10920425/
  - "Agency, goal directedness, and the levels of biological organization," *BioScience* (2025 advance), https://doi.org/10.1093/biosci/biag030
  - "Measuring Goal-Directedness," arXiv:2412.04758 (MacDermott et al.; formal causal criterion)
- **Type**: Philosophy / formal
- **Key points**:
  - Recent work deliberately **avoids a vitalist categorical criterion** separating agential from non-agential systems; it offers agency in "quantifiable but relational terms — a scale-relative notion." Means/goal relations are cashed out as counterfactual dependence / invariance.
  - Consequence for the evidence problem: if agency is scale-relative and relational by construction, then asking "is the bacterium *really* a proto-agent, yes/no" may be a mis-posed question — there is a defensible degree of goal-directedness, not a fact of the matter about a threshold crossing.
- **Tenet alignment**: Resonates with Tenet 5 — resists a clean simplicity-driven line.

### Free energy principle as an agency criterion — and its falsifiability problem
- **Key point**: Under FEP, apparent goal-directedness (maintaining state, avoiding harm) is reframed as minimising expected surprise. But critics note that at sufficient abstraction "almost any behavior can be redescribed as free-energy minimization," making it hard to test/falsify. So FEP *classifies* the bacterium as an agent-like system but does not *discriminate* proto-choice from harnessed noise — both minimise free energy.
- **Tenet alignment**: Cautionary — an over-general criterion is no criterion.

### Unlimited Associative Learning (Ginsburg & Jablonka; Birch et al. 2020 primer)
- **URL**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7116763/ ; *The Evolution of the Sensitive Soul* (MIT, 2019)
- **Type**: Book / review
- **Key points**:
  - UAL proposed as the evolutionary transition-marker to *minimal consciousness/sentience*. It is a **positive marker only** — tells you which systems are sentient, not which are not.
  - Bacteria show habituation and sensitisation (non-associative learning) but not *unlimited* associative learning, so UAL does not credit them with sentience.
- **Relevance / caution**: UAL answers the **sentience** question, not the **agency** question. The article must keep the two apart — this is the corpus's competency-vs-experience decoupling applied to *evidence*: even a clean agency criterion would not be a consciousness criterion, and vice versa.

### Minimal cognition: criteria pluralism (Lyon 2020; Bråten/others)
- **URL**: "Of what is 'minimal cognition' the half-baked version?" Pamela Lyon, *Adaptive Behavior* (2020), https://journals.sagepub.com/doi/full/10.1177/1059712319871360
- **Key point**: "Given the multitude of approaches and kinds of criteria… it is unlikely that we will see any consensus soon on what [minimal cognition] is exactly, let alone where it emerges." Even the field most sympathetic to bacterial cognition concedes there is no agreed criterion — which is itself evidence that the evidence problem is real and not merely the Map's skepticism.

## Major Positions

### Deflationism / "no chooser" (EMBO dissent; Robinson, Mallatt, Peer, Sourjik, Taiz)
- **Core claim**: Bacterial "decision" = current-state-determined output of a small ODE system; inter-cell differences = stochastic protein-level variance. No volition, a fortiori no proto-choice.
- **Key argument**: Completeness of the mechanistic account leaves no explanatory residue for a chooser to fill.
- **Relation to site tenets**: Compatible with the Map's negative verdict (no neural substrate → no interface), but the Map must *decline the parsimony-as-proof step* (Tenet 5): mechanistic sufficiency shows a chooser is *unnecessary*, not that one is *absent*.

### Cellular Basis of Consciousness / natural bacterial agency (Reber & Baluška; Lyon's biogenic cognition as the weaker cousin)
- **Core claim (CBC, strong)**: Excitable membrane already feels; bacterial decision is genuine minimal choice.
- **Core claim (biogenic, weaker)**: Genuine cognition/agency without the feeling claim.
- **Key argument**: Continuity of excitable-membrane biology from bacteria to neurons; drawing the line anywhere looks arbitrary.
- **Relation to site tenets**: The Map grants biological continuity, denies phenomenal continuity (framework-relative, not demonstrated).

### Scale-relative / deflate-the-question agency (Biological Theory 2023; BioScience 2025; formal causal-agency work)
- **Core claim**: There is no categorical agent/non-agent fact; agency is a graded, relational, counterfactually-defined property. The bacterium has *some* goal-directedness by an interventionist measure — full stop, no threshold.
- **Key argument**: Any categorical line is a vitalist relic; measure the counterfactual/causal structure instead.
- **Relation to site tenets**: Strong Tenet-5 ally: resists forcing a simple binary onto an under-determined space. But it *dissolves* rather than *answers* the proto-choice question, which is itself a result the article can report.

## Key Debates

### Debate 1: Is "stochastic noise vs genuine choice" a real dichotomy?
- **Sides**: EMBO dissent frames noise and choice as exclusive; the chemotaxis-noise literature (Sourjik's own FRET data, the motor-coordination and noise-sensitivity results) shows noise is *constitutive of* the adaptive search.
- **Core disagreement**: Whether "it reduces to noise" is a deflation at all, once noise is the mechanism of exploration.
- **Current state**: Live tension. The strongest single move the downstream article can make: the dichotomy is a *false* one; the interesting question is not noise-vs-choice but whether "harnessed stochastic search" warrants agency vocabulary — and that is a conceptual, not experimental, question.

### Debate 2: What would count as evidence, even in principle?
- **Sides**: Marker-pluralists (Lyon: no consensus criterion); positive-marker theorists (UAL — but for sentience); interventionist/formal-causal theorists (graded goal-directedness); FEP universalists (everything alive minimises free energy).
- **Core disagreement**: Whether any observable discriminates proto-choice from complete mechanism, given both predict identical behaviour.
- **Current state**: No agreed discriminating observable. Candidate criteria either fail to be categorical, risk unfalsifiability, or track sentience rather than agency.

### Debate 3: Tractability — is the distinction empirically decidable at the single-cell rung at all?
- **Sides**: Optimists (better single-cell measurement + causal-agency formalisms will settle it); pessimists/the Map (behavioural underdetermination is in-principle, because the mechanism is complete and the substrate for anything extra is absent).
- **Current state**: This is the article's true thesis space — argue that at the prokaryotic floor the proto-choice question is plausibly **not tractable**, and that recognising this is a Tenet-5 result, not a failure.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1977 | Koshland, "response regulator model" | Bacterial "rudimentary memory" framed mechanistically |
| 2004 | Berg, *E. coli in Motion* | Canonical run-and-tumble + temporal-comparison account |
| 2011 | Non-genetic individuality in motor switching (PNAS) | Isogenic behavioural variance tied to CheY-P + motor individuality |
| 2012 | Stochastic multi-actuator coordination (PNAS) | Noise shown *functionally beneficial* — reframes "noise" |
| 2015 | Lyon, "The cognitive cell" | Strong biogenic-cognition case for bacterial cognition |
| 2016 | Ginsburg & Jablonka / Birch, UAL marker | Positive marker for *sentience*, not agency; bacteria excluded |
| 2016 | Noise-induced sensitivity increase (Biophys J) | Further evidence noise is integral to the mechanism |
| 2017 | Single-cell FRET CheY-P variability (PNAS; Sourjik/Emonet/Shimizu labs) | Direct measurement of the "noise" both camps interpret |
| 2020 | Reber & Baluška, "Cognition in some surprising places"; Lyon, minimal-cognition criteria pluralism | Strong CBC claim; concession that no agreed criterion exists |
| 2023 | *Biological Theory*: scale-relative, part-whole agency | Deflates the categorical agency question |
| 2024 | **EMBO Reports dissent** (Robinson, Mallatt, Peer, Sourjik, Taiz) | "No choice — determined by current state; stochastic protein-level differences" |
| 2024 | "Measuring Goal-Directedness" (arXiv) | Formal causal criterion; graded not categorical |

## Potential Article Angles

1. **The evidence problem as the thesis (recommended).** Title candidate: "Single-Cell Proto-Agency and the Evidence Problem." Structure: (i) state the received dichotomy; (ii) dissolve it — noise is the search mechanism, so "just noise" is not a deflation; (iii) survey candidate discriminating criteria and show each fails to discriminate proto-choice from complete mechanism; (iv) argue the distinction is plausibly *empirically intractable* at the prokaryotic floor; (v) Relation to Site Perspective: Tenet 5 (parsimony can't settle it either way), Tenet 3 (interface bottoming-out), and explicit hand-off to [agency-verification-void](/voids/agency-verification-void/). This is the angle the harvested task asks for and the one that does *not* re-cover the chemotaxis mechanism.
2. **The measurer's-interpretation angle.** Foreground that Sourjik measured the variability *and* co-signs the deflationary reading — use it to show the noise/choice line is drawn in interpretation, not by an additional experiment. Good sharp sub-section, probably not the whole article.
3. **Agency-vs-sentience double-decoupling for *evidence*.** Extend the corpus's competency/experience decoupling to the epistemic level: even a perfect agency criterion (UAL, causal formalism) would not be a consciousness criterion. Ties to [competency-without-felt-experience](/apex/competency-without-felt-experience/).

Writing guidance for the downstream expand-topic (per `obsidian/project/writing-style.md`): front-load the "dichotomy is false / underdetermination is the point" thesis; use named-anchor forward references for the criterion survey; include only the mechanism background needed to state the evidence problem (the mechanism itself lives in the sibling chemotaxis article — link, don't repeat); the "Relation to Site Perspective" section must connect to Tenets 3 and 5 explicitly and cross-link the agency-verification void.

## Gaps in Research

- Did not fetch the full text of the *Biological Theory* 2023 and *BioScience* 2025 agency papers — the "scale-relative / no categorical criterion" characterisation comes from abstracts/summaries and should be verified verbatim before quoting in the article.
- "Measuring Goal-Directedness" (arXiv:2412.04758) referenced from search only; verify authorship (MacDermott et al.) and exact claim at source before citing; do not attribute a specific bacterial verdict to it.
- No source directly runs the *specific* argument "noise-as-mechanism dissolves the EMBO dichotomy" — that synthesis is this note's own inference from (a) the EMBO dichotomy and (b) the functional-noise literature. The downstream article should present it as the Map's argument, not as an existing published position.
- Did not locate a source explicitly asserting *in-principle* intractability at the single-cell level; the tractability-pessimism thesis is the Map's, supported by but not stated in the literature. Frame accordingly.
- UAL's exact treatment of bacteria (limited vs unlimited associative learning) taken from secondary summary; verify against Birch, Ginsburg & Jablonka (2020) primer before quoting.

## Citations

1. Robinson, D. G., Mallatt, J., Peer, W. A., Sourjik, V., & Taiz, L. (2024). "Cell consciousness: a dissenting opinion." *EMBO Reports* 25(5):2162–2167. doi:10.1038/s44319-024-00127-4. https://pmc.ncbi.nlm.nih.gov/articles/PMC11094104/
2. Keegstra, J. M., Kamino, K., Anquez, F., Lazova, M. D., Emonet, T., & Shimizu, T. S. (2017). "Phenotypic diversity and temporal variability in a bacterial signaling network revealed by single-cell FRET." *PNAS* / *eLife* (companion papers). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5809149/
3. "Stochastic coordination of multiple actuators reduces latency and improves chemotactic response in bacteria." (2012). *PNAS*. https://www.pnas.org/doi/10.1073/pnas.1113706109
4. "Noise-Induced Increase of Sensitivity in Bacterial Chemotaxis." (2016). *Biophysical Journal*. https://www.sciencedirect.com/science/article/pii/S0006349516304581
5. "Nongenetic individuality, changeability, and inheritance in bacterial behavior." (2021). *PNAS*. https://www.pnas.org/doi/full/10.1073/pnas.2023322118
6. "Non-genetic individuality in Escherichia coli motor switching." (2011). *PNAS*. https://pubmed.ncbi.nlm.nih.gov/21422514/
7. "Agency, Goal-Directed Behavior, and Part-Whole Relationships in Biological Systems." (2023). *Biological Theory*. https://pmc.ncbi.nlm.nih.gov/articles/PMC10920425/
8. "Agency, goal directedness, and the levels of biological organization." (2025, advance). *BioScience*. https://doi.org/10.1093/biosci/biag030
9. MacDermott, M., et al. (2024). "Measuring Goal-Directedness." arXiv:2412.04758.
10. Birch, J., Ginsburg, S., & Jablonka, E. (2020). "Unlimited Associative Learning and the origins of consciousness: a primer and some predictions." *Biology & Philosophy* 35:56. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7116763/
11. Ginsburg, S., & Jablonka, E. (2019). *The Evolution of the Sensitive Soul: Learning and the Origins of Consciousness*. MIT Press.
12. Lyon, P. (2020). "Of what is 'minimal cognition' the half-baked version?" *Adaptive Behavior* 28(6). https://journals.sagepub.com/doi/full/10.1177/1059712319871360
13. Lyon, P. (2015). "The cognitive cell: bacterial behavior reconsidered." *Frontiers in Microbiology* 6:264. doi:10.3389/fmicb.2015.00264
14. Reber, A. S., & Baluška, F. (2020). "Cognition in some surprising places." *Biochem. Biophys. Res. Commun.* PubMed 32950231.