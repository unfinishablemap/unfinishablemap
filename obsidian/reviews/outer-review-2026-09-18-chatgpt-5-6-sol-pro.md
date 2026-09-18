---
title: "Outer Review - ChatGPT 5.6 Pro (2026-09-18)"
created: 2026-09-18
modified: 2026-09-18
human_modified: null
ai_modified: 2026-09-18T04:27:00+00:00
draft: false
description: "ChatGPT 5.6 Pro refereeing Philosophical Stakes of Spontaneous Collapse: the lede contradicts the Map's own Tier-1/Tier-2 separation, Chalmers-McQueen is misrepresented as a scalar-Phi model, and XENONnT 2026 has not propagated from the Penrose article."
topics:
  - "[[philosophical-stakes-of-spontaneous-collapse]]"
  - "[[testing-consciousness-collapse]]"
  - "[[penrose-gravity-induced-collapse-empirical-prospects]]"
concepts:
  - "[[spontaneous-collapse-theories]]"
  - "[[post-decoherence-selection]]"
  - "[[many-worlds]]"
  - "[[integrated-information-theory]]"
related_articles:
  - "[[project]]"
ai_contribution: 90
author: "Andy Southgate"
ai_system: "chatgpt-5-6-pro"
ai_generated_date: 2026-09-18
last_curated: 2026-09-18
outer_review_status: processed
outer_review_conversation_url: https://chatgpt.com/g/g-p-695a7d60af5481919d5c22ad7bcc1648-the-unfinishable-map/c/6aac9d6b-c5c4-83ed-a4f3-e9329b3ca9e1
outer_review_extraction_method: js-dom
subject_type: recent
subject_title: "Audit philosophical-stakes-of-spontaneous-collapse"
subject_articles:
  - topics/philosophical-stakes-of-spontaneous-collapse.md
subject_source: fallback:recent-aged
---

**Date**: 2026-09-18
**Reviewer**: ChatGPT 5.6 Pro
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Act as a rigorous external referee for one article on The Unfinishable Map, a dualist philosophy site: https://unfinishablemap.org/topics/philosophical-stakes-of-spontaneous-collapse/ It argues that the choice between GRW, CSL, and Penrose objective reduction determines whether consciousness is causally connected to physical reality, and that the site's position (consciousness modulating a collapse that would occur anyway) depends on getting the physics right. Assess: (1) whether its characterisations of GRW, CSL, and Diosi-Penrose match current experimental bounds, including recent underground and cryogenic tests; (2) whether it treats no-collapse alternatives such as Bohmian mechanics and Everettian accounts fairly, or brackets them to protect its dualist commitments; (3) stale, misattributed, or unverifiable citations; (4) counterarguments it omits, especially decoherence-based ones; (5) how well it integrates with neighbouring articles. Web search indexes lag 24-48 hours, so consult the changelog at https://unfinishablemap.org/workflow/changelog/ for recent activity; the site root is https://unfinishablemap.org . End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# External referee report

## Recommendation: **major revision**

The article has a valuable organising idea: distinguish consciousness-independent collapse, consciousness-caused collapse, and consciousness-modulated collapse, then ask which physical theory could host the third. Its ontology section is also useful, and the closing admission that there is no worked neural toy model and that exact Born preservation creates a serious dilemma is commendably explicit.

Its central thesis nevertheless outruns both the physics and the Map’s own better-qualified articles. **The choice between GRW, CSL and gravity-related collapse determines the form of a possible physical collapse process; it does not determine whether consciousness is causally connected to physics.** Pure GRW, pure CSL and a gravitational-collapse law can each be complete, consciousness-independent stochastic theories. Mental causation enters only through an additional psychophysical law. The Map’s testing article states this correctly: evidence for Tier‑1 objective collapse would not establish Tier‑2 consciousness involvement. The target’s headline claim, by contrast, says that the choice among collapse models “determines” whether minds matter physically. [topics/philosophical-stakes-of-spontaneous-collapse](https://unfinishablemap.org/topics/philosophical-stakes-of-spontaneous-collapse/)

That is not a merely verbal problem. It causes the article repeatedly to slide between:

1. objective collapse exists;
2. objective collapse creates indeterminism;
3. indeterminism leaves a causal vacancy;
4. consciousness can occupy that vacancy;
5. consciousness actually does occupy it.

Only the first two follow from GRW or CSL. The remainder require a new theory.

## 1. Audit of the physics and experimental status

### Overall finding

The elementary descriptions of discrete GRW and continuous CSL are broadly serviceable. The treatment of Diósi–Penrose and Penrose OR is much less secure, and the experimental-status section is materially obsolete as of September 2026.

The sentence asking whether the 2022 “whisker-width margin survives” is no longer an open question in the form presented. On 23 March 2026, XENONnT published world-leading spontaneous-radiation bounds, excluding for the first time CSL parameter values in the range originally proposed by GRW. At the nominal point rC​=10−7m,λ=10−16s−1, the result differs from the best fit by 9.1σ. [APS Journals+1](https://link.aps.org/doi/10.1103/2jm3-4976)

### Model-by-model assessment

| Model | What the article gets right | What requires correction |
| --- | --- | --- |
| **GRW** | Discrete Poisson-distributed localisations, Gaussian position localisation and macroscopic amplification are correctly identified. | “GRW survived by a whisker” is a stale 2022 summary. The nominal GRW parameter point is now excluded when embedded in the mass-proportional, Markovian white-noise CSL radiation model used by XENONnT. This does **not** by itself prove that every discrete-GRW implementation, noise spectrum or modified collapse law is excluded. The article must state both halves of that result. [arXiv+1](https://arxiv.org/html/2506.05507) |
| **CSL** | Continuous stochastic evolution coupled to smeared mass density is characterised reasonably well. | The article gives no current exclusion landscape. XENONnT reports λ/rC2​<3.0×10−3s−1m−2 at 90% confidence under its Markovian CSL assumptions, improving previous spontaneous-radiation bounds by roughly two orders of magnitude. Coloured and dissipative CSL extensions remain less constrained, so “CSL” cannot be treated as one experimentally uniform target. [APS Journals+2arXiv+2](https://link.aps.org/doi/10.1103/2jm3-4976) |
| **Diósi–Penrose** | The gravitational self-energy timescale τ∼ℏ/EG​ is correctly identified as the central idea. | The target conflates Penrose’s heuristic instability argument, Diósi’s stochastic dynamics, regularised DP models and Orch OR. The natural parameter-free DP prescription was ruled out by the Gran Sasso experiment; regularised versions survive only with an adjustable smearing scale. XENONnT now gives R0​>4.9×10−10m at 90% confidence, or 4.5×10−10m at 95%. [Nature+1](https://www.nature.com/articles/s41567-020-1008-4) |
| **Penrose OR** | It is fair to say that Penrose seeks a deeper gravitational motivation rather than simply inserting the GRW numbers phenomenologically. | “Penrose derives collapse from quantum gravity” and “No free parameters” are too strong. There is no accepted underlying quantum-gravity derivation, unique stochastic law, unique mass-density regularisation or settled relativistic dynamics. Even the atomistic paper cited by the article notes a free numerical factor in the gravitational self-energy prescription. [topics/penrose-gravity-induced-collapse-empirical-prospects](https://unfinishablemap.org/topics/penrose-gravity-induced-collapse-empirical-prospects/) |
| **Orch OR** | It is relevant to consciousness and uses the Penrose timescale. | Proto-consciousness should be attributed to the Penrose–Hameroff Orch OR programme, not silently built into gravitational objective reduction as such. A gravity-driven collapse law need contain no phenomenal property at all. |

### The underground experiments

The article compresses several importantly different results into “the Gran Sasso germanium-detector null result of 2020 and its confirmation that August by the Majorana Demonstrator.”

That wording is defective in four ways.

First, the Donadi et al. paper was published online in 2020 but appears bibliographically as *Nature Physics* 17, 74–78 (2021). Calling it a “2020 result” is understandable, but citing it as Donadi et al. 2021 is the standard form.

Second, it specifically ruled out the **natural parameter-free version** of the Diósi–Penrose model. It did not refute every theory that Penrose might describe as gravitational objective reduction. [Nature](https://www.nature.com/articles/s41567-020-1008-4)

Third, the Majorana result was published on **16 August 2022**, not in the same August as the Gran Sasso paper. It was an independent and substantially stronger null search, primarily formulated as a white-CSL test, with a DP reinterpretation. It improved comparable spontaneous-radiation sensitivity by factors of roughly 40–100. “Confirmation” obscures the change of model, dataset and numerical bound. [APS Journals+1](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.129.080401)

Fourth, XENONnT has now superseded both as the central spontaneous-radiation result. The article’s neighbouring Penrose page knows this and gives the 2026 bound, while the audited page still presents the literature as awaiting an answer. [topics/penrose-gravity-induced-collapse-empirical-prospects](https://unfinishablemap.org/topics/penrose-gravity-induced-collapse-empirical-prospects/)

### Cryogenic and low-frequency tests

The article omits the complementary mechanical-noise literature. Vinante et al.’s layered microcantilever operated down to 100 mK, found motion consistent with thermal noise and improved the previous mechanical CSL bound by more than an order of magnitude near rC​=10−7m, challenging the Adler-motivated region. [APS Journals+1](https://link.aps.org/doi/10.1103/PhysRevLett.125.100404)

More recently, the 2025 analysis of LISA Pathfinder’s rotational noise produced a stronger CSL constraint than the earlier translational analysis. Although not a cryogenic laboratory measurement, it is important precisely because low-frequency mechanical-noise bounds probe a different part of model space from X-ray searches. [APS Journals](https://link.aps.org/doi/10.1103/PhysRevA.111.L020203)

This complementarity matters. X-ray exclusions are exceptionally strong for white, high-frequency noise, but coloured or dissipative models can suppress high-frequency radiation while retaining low-frequency effects. The article currently treats “bounds tightening” as one-dimensional, when the experimental landscape is strongly model- and frequency-dependent. [arXiv](https://arxiv.org/html/2506.05507)

### Direct interferometry

The article should also incorporate the January 2026 sodium-nanoparticle result: interference was demonstrated for clusters containing more than 7,000 atoms and exceeding 170,000 Da, with reported macroscopicity μ=15.5. This does not approach every gravity-collapse target and is not by itself the strongest CSL bound, but it is the current direct-superposition frontier and belongs in any article claiming current experimental coverage. [Nature+1](https://www.nature.com/articles/s41586-025-09917-9)

### Two additional physics errors

The statement that objective collapse provides facts such as “this atom is here, that particle has this momentum” is misleading. GRW and standard CSL localise position or mass density; stronger position localisation broadens momentum. They do not generally produce simultaneous sharp position and momentum values.

The language of branches being “physically destroyed” and states becoming straightforwardly “genuinely definite” also suppresses the **tails problem**. Gaussian localisation does not set all disfavoured amplitudes exactly to zero. Primitive-ontology versions of GRW can defend macroscopic definiteness, but that defence must be made rather than assumed. The tails literature is directly relevant to the article’s contrast with Everett, because some versions of the objection ask whether low-amplitude structured branches remain. [arXiv+1](https://arxiv.org/abs/1501.05778)

## 2. Does collapse supply a route for mental causation?

### The article mistakes stochasticity for causal incompleteness

A stochastic law need not contain a causal gap. A physically exhaustive Markov process can be just as closed as a deterministic process: it specifies conditional probabilities rather than unique trajectories. GRW and CSL were devised as autonomous physical dynamics. Their randomness does not mean that the realised event is waiting for an additional mind to choose it.

Accordingly, the article’s claim that collapse provides “openness” for consciousness should be rewritten as:

> Objective stochasticity supplies a mathematical location at which an additional psychophysical law might be inserted.

That is a weaker but defensible claim. It neither implies that the insertion is coherent nor supplies evidence that it occurs.

### The Born-preserving bias problem is sharper than the article admits

Suppose ordinary collapse gives

P(i∣ψ)=∣ci​∣2.

If conscious state C really biases outcome i, then for at least some C,

P(i∣ψ,C)=∣ci​∣2.

If the Map requires the Born rule to hold exactly for every conscious condition C, the proposed bias disappears. If it requires only the unconditional average over conscious conditions to remain Born-distributed, the causal effect can still appear in correlations between C and outcomes, unless compensating effects are engineered. Such compensation would require its own law and risks becoming fine-tuned.

The article recognises a “bias-without-deviation dilemma” near its conclusion, but earlier sections repeatedly speak as if selecting within Born probabilities were automatically harmless. It is not. “Selecting an allowed result” is not probability-neutral when the selection is systematic.

The same model must prove that its ensemble evolution respects no-signalling. Generic state-dependent nonlinear modifications can make different decompositions of the same density matrix physically distinguishable and thereby enable superluminal signalling. Collapse theories avoid this only through carefully constrained stochastic dynamics. A consciousness-conditioned rule cannot inherit that protection without showing the relevant ensemble equation. [APS Journals](https://link.aps.org/doi/10.1103/PhysRevLett.87.170405)

### Conservation laws do not settle causal closure

The claim that conscious bias can leave “causal closure intact at the level of conservation laws” conflates two questions.

- A process may conserve average energy while still violate physical causal closure.
- Standard collapse noise can itself generate heating or diffusion.
- A consciousness-conditioned term might conserve energy and yet introduce a non-physical cause.
- Conversely, tiny energy nonconservation would not by itself establish mental causation.

The article therefore needs a separate accounting of energy, momentum, no-signalling and causal completeness rather than treating “no obvious energy transfer” as sufficient.

### Chalmers–McQueen is misrepresented

This is the clearest source-fidelity error in the article.

The target says that differences in scalar integrated information, Φ, between conscious states determine collapse rates. Chalmers and McQueen explicitly reject a Φ-only model: qualitatively different conscious states can have the same Φ, so such a model would fail to collapse crucial superpositions. Their developed proposal uses the much richer **IIT Q-shape**, represented through multiple Q-shape collapse operators. [arXiv+2arXiv+2](https://arxiv.org/pdf/2105.02314)

The article also omits the authors’ own central qualification: simple consciousness-collapse versions are falsified by the quantum Zeno effect, while more complicated versions remain a speculative research programme rather than an established solution. [arXiv](https://arxiv.org/pdf/2105.02314)

Nor is their proposal a worked version of the Map’s preferred mechanism. Chalmers–McQueen alter collapse dynamics using consciousness-related operators, yielding potentially measurable deviations. The Map instead proposes token-outcome bias while preserving exact Born statistics. Borrowing the former’s “architecture” does not supply an equation for the latter.

Finally, the Chalmers–McQueen model does not show that intentions or conscious reasons **select** neural outcomes. It gives consciousness-correlated Q-shape a role in suppressing certain superpositions. That is causal efficacy of a kind, but it is not yet agent-guided selection.

## 3. Treatment of Bohmian and Everettian alternatives

### Bohmian mechanics: not exactly strawmanned, but seriously under-engaged

The article initially acknowledges Bohmian mechanics, then largely drops it. Its phrase “empirically equivalent at current precision” is misleading. Standard Bohmian mechanics in quantum equilibrium recovers ordinary quantum statistics by construction and derivation; its agreement is not merely an artefact of insufficient instrumental precision. Detectable departures require additional non-equilibrium or modified-dynamics hypotheses. [arXiv](https://arxiv.org/pdf/quant-ph/0308039.pdf)

Bohmian mechanics also shows why the sentence “the measurement problem forces a choice … something selects” begs the question. In Bohmian mechanics:

- the universal wavefunction does not collapse;
- the actual configuration always has one definite value;
- decoherence gives subsystems effective wavefunctions associated with the occupied branch;
- there is no stochastic outcome-selection event for consciousness to commandeer.

The Map may reject this because determinism provides no obvious locus for its preferred intervention. That is a legitimate statement about **fit with the Map’s tenets**, not an objection to Bohmian mechanics as a solution to definite outcomes.

A telling omission occurs in the article’s account of what remains if collapse is falsified: it lists decoherence-only views, Everett and QBism, but not Bohmian mechanics, despite having mentioned Bohm at the outset. That makes the conclusion look artificially narrow. [topics/philosophical-stakes-of-spontaneous-collapse](https://unfinishablemap.org/topics/philosophical-stakes-of-spontaneous-collapse/)

### Everett: conditional caveat followed by tenet-protective overstatement

The article does make one fair concession: it says the consequences of objective collapse remain conditional because present data do not force a collapse reading. That should be retained.

But later it asserts that the measurement problem “demonstrates” unitary quantum mechanics is incomplete. That is precisely the point Everettian, relational, pragmatist and some consistent-histories accounts deny. The Map’s own decoherence article acknowledges that the demand for a further selector is decisive only within single-outcome frameworks, not a universal theorem. [topics/philosophical-stakes-of-spontaneous-collapse](https://unfinishablemap.org/topics/philosophical-stakes-of-spontaneous-collapse/)

The target also presents Everettian probability as suffering “deep circularity problems” without conveying the status of the dispute. The Map’s dedicated many-worlds page is more responsible: it describes decision-theoretic, self-locating and envariance strategies, records serious objections, but says explicitly that their success remains contested rather than closed. [concepts/many-worlds](https://unfinishablemap.org/concepts/many-worlds/)

The appropriate formulation is therefore:

> The Map rejects Everett because it rejects global branching, branch-relative identity and the assumptions used in leading Born-rule reconstructions.

The present formulation instead suggests that collapse physics has already adjudicated the philosophical dispute. That is tenet-protective bracketing.

### Fairness verdict

The article does not wholly ignore no-collapse theories, so “strawman” would be too strong. But it evaluates them primarily by whether they leave room for the Map’s desired mental causation. It does not comparably present how each theory claims to solve or dissolve the outcome problem on its own terms.

**Assessment: partial procedural fairness, inadequate substantive fairness.**

## 4. Citation audit

### Verified and basically sound

The foundational GRW, Pearle and Ghirardi–Pearle–Rimini references are real and appropriate. Allori et al. 2008, Carlesso et al. 2022, Tomaz et al. 2024 and the Carlesso–Donadi 2025 preprint are also verifiable.

### Material citation defects

| Citation or attribution | Finding |
| --- | --- |
| **Chalmers & McQueen 2022** | Materially misrepresented. Their developed model uses Q-shapes, not simply differences in scalar Φ; they explicitly reject the latter as insufficient. Their quantum-Zeno falsification of simple models is omitted. [arXiv+2arXiv+2](https://arxiv.org/pdf/2105.02314) |
| **Penrose 1994** | Real, but insufficient as the sole technical source for the collapse-timescale claim and current DP model. Add Penrose’s 1996 paper, Diósi’s dynamical papers and current experimental work. XENONnT itself cites Penrose 1996 as the relevant technical source. [APS Journals](https://link.aps.org/doi/10.1103/2jm3-4976) |
| **“No free parameters”** | Unverifiable as an unqualified claim. The experimentally testable DP dynamics require regularisation and a convention-dependent numerical factor; the cited Tomaz paper itself discusses such a factor. [RSCJ](https://rscj.silverchair-cdn.com/rscj/content_public/journal/cp/26/31/10.1039_d4cp02364a/1/d4cp02364a.pdf) |
| **Penrose and proto-consciousness** | Should be attributed specifically to Penrose–Hameroff/Orch OR, not presented as a consequence of all Penrose-style gravitational collapse. |
| **Ball 2022** | Real but now unsuitable as the article’s empirical anchor. It is secondary journalism and predates XENONnT’s decisive update. |
| **Donadi result** | Discussed without a direct reference. Standard citation year is 2021, although the paper appeared online in 2020. Add doi:10.1038/s41567-020-1008-4. [Nature](https://www.nature.com/articles/s41567-020-1008-4) |
| **Majorana result** | Discussed without a direct reference and misleadingly called a “confirmation.” Add the 2022 PRL and its 2023 erratum; identify it as an independent white-CSL search with a DP reinterpretation. [APS Journals+1](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.129.080401) |
| **XENONnT 2026** | Omitted entirely from the target’s references despite directly superseding its empirical verdict. [APS Journals](https://link.aps.org/doi/10.1103/2jm3-4976) |
| **Tomaz, Mattos & Barbatti 2024** | Real and correctly authored, but “opened new channels” is too vague. The paper develops atomistic collapse-time calculations and possible experimental regimes; it does not reverse the underground exclusions or furnish a completed collapse dynamics. [Royal Society of Chemistry Publications+1](https://pubs.rsc.org/cp/article/26/31/20785/843511/Gravitationally-induced-wave-function-collapse) |
| **Bell/Tumulka and GRW ontologies** | The text names Bell and Tumulka but supplies no direct ontology references. Allori et al. is relevant background but should not silently bear every historical attribution. |
| **Carlesso & Donadi 2025** | Real and useful as a review preprint, but citing a review cannot substitute for citing the 2026 experimental paper that changed the status. |

There are no obvious fabricated references in the bibliography. The more serious problem is **claim-to-source mismatch**: real sources are used to support stronger or different propositions than they actually defend.

## 5. Important omitted counterarguments

### 5.1 The tails problem

As noted above, Gaussian collapse suppresses rather than literally deletes the disfavoured components. The article cannot base its contrast with Everett on exact branch annihilation without addressing this literature. [Springer+1](https://link.springer.com/article/10.1007/BF00763475)

### 5.2 Decoherence does not produce a menu awaiting selection

The Map’s own post-decoherence article correctly warns that an improper mixture is not a classical list of already-real alternatives from which a mind can simply choose. “Selection” must be a new dynamical transition from the entangled state, not the reading-off of one pre-existing member. [concepts/post-decoherence-selection](https://unfinishablemap.org/concepts/post-decoherence-selection/)

The audited article nevertheless repeatedly speaks of consciousness selecting “among outcomes the physics leaves open.” That language recreates the menu picture its neighbouring article rejects. A mathematically adequate account must specify:

- the total entangled state;
- the collapse operators;
- the phenomenal or psychophysical variable;
- the altered stochastic differential equation;
- the resulting ensemble master equation;
- the amplification from the collapse basis to a behaviourally relevant neural difference.

Without this, “post-decoherence” functions as a label for an unknown process, not an identified physical stage.

### 5.3 There may be no clean temporal post-decoherence stage

In realistic open systems, decoherence and any hypothesised collapse act continuously and on overlapping timescales. There need not be a moment at which decoherence has completed, presented a stable menu, and then handed the system to consciousness. A model must derive a regime in which that sequencing is a valid approximation.

### 5.4 The preferred-basis problem returns at the psychophysical level

Mass-density collapse distinguishes spatial mass distributions. Conscious experience distinguishes colours, pains, intentions, valences and reasons. The article offers no law mapping phenomenal contrasts onto eigenspaces of smeared mass-density or Q-shape operators.

This is more than the generic hard problem. Two phenomenally distinct intentions may correspond to highly overlapping mass distributions, while two microscopically distinct mass configurations may carry the same experience. A collapse model needs a principled equivalence relation between physical configurations and phenomenal contents.

### 5.5 Randomness is not control

Indeterminism may remove deterministic exclusion, but it does not provide reasons-responsiveness, authorship or control. A random GRW hit is not more agentive than radioactive decay. The article links collapse stochasticity to libertarian freedom too quickly. The missing bridge is a law relating reasons or intentions to altered outcome probabilities—and that is precisely where Born preservation and no-signalling become difficult.

### 5.6 Positive collapse evidence would not support dualism by itself

A detected CSL-like noise spectrum would establish new physical dynamics. The default inference would be that the noise is another physical field or stochastic law. It could actually strengthen a physicalist solution to the measurement problem by showing that nature collapses wavefunctions without minds.

The article’s own testing companion states this Tier‑1/Tier‑2 separation correctly. The target should make it the organising principle of the whole discussion, not a late qualification. [topics/testing-consciousness-collapse](https://unfinishablemap.org/topics/testing-consciousness-collapse/)

### 5.7 Relativistic completion remains open

Theories that modify collapse dynamics must confront relativistic covariance, hypersurface dependence and nonlocal correlations. Work on relativistic generalisations remains active in 2026, which is evidence that the issue is not closed. A mind-conditioned collapse rule would inherit the difficulty in a sharper form because “when consciousness intervenes” may be frame-dependent unless the law is covariantly formulated. [APS Journals+1](https://link.aps.org/doi/10.1103/g7xn-bwfs)

### 5.8 Collapse irreversibility does not by itself explain the thermodynamic arrow

The article does hedge this, which is good. It should nevertheless state the main problem explicitly: a time-asymmetric stochastic law does not by itself explain the universe’s low-entropy initial condition or derive ordinary thermodynamic irreversibility. Collapse may contribute an arrow, accompany it, or presuppose boundary conditions that do most of the explanatory work.

## 6. Integration with neighbouring Map articles

### What works

The article links extensively and does not conceal its strongest internal difficulty. In particular:

- the testing article supplies a good Tier‑1/Tier‑2/Tier‑3 framework;
- the post-decoherence article distinguishes improper mixtures from classical menus;
- the Penrose article contains a much more current empirical discussion;
- the many-worlds article offers a more balanced account of live Everettian responses;
- the testability ledger distinguishes tenet coherence from empirical support and mechanism failure from tenet failure. [topics/testing-consciousness-collapse](https://unfinishablemap.org/topics/testing-consciousness-collapse/)

### What fails

The links do not reliably transmit the neighbouring articles’ conclusions.

#### 1. Tier separation is not propagated

The testing article says explicitly that confirming objective collapse would not confirm consciousness involvement. The target nevertheless opens by saying the model choice determines whether consciousness is causally connected. [topics/testing-consciousness-collapse](https://unfinishablemap.org/topics/testing-consciousness-collapse/)

#### 2. Experimental updates are not propagated

The Penrose article records XENONnT’s March 2026 result and the exclusion of the nominal GRW range, while both the target and the general spontaneous-collapse article retain the 2022 “survived by a whisker” verdict. [topics/penrose-gravity-induced-collapse-empirical-prospects](https://unfinishablemap.org/topics/penrose-gravity-induced-collapse-empirical-prospects/)

#### 3. Tenet calibration is not propagated

On 14 September 2026, the changelog records edits to the general collapse article replacing “requires” with “favours,” “the minimal design” with “one minimal design,” and “preserve the causal connection” with “leave room for the causal connection.” The audited article, last modified three days earlier, retains the stronger phrases “provide the minimal design” and “preserve the ontological distinction.” [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)

This is direct evidence of cluster-level semantic drift.

#### 4. The improper-mixture warning is not propagated

The post-decoherence article says an improper mixture is not a menu. The target nevertheless uses outcome-selection language that naturally invites exactly that interpretation. [concepts/post-decoherence-selection](https://unfinishablemap.org/concepts/post-decoherence-selection/)

#### 5. Everettian calibration is not propagated

The dedicated many-worlds article says probability derivations remain disputed rather than closed. The target presents “deep circularity” and unitary incompleteness as settled consequences. [concepts/many-worlds](https://unfinishablemap.org/concepts/many-worlds/)

### Integration verdict

**Link integration: strong.  

Argument integration: weak.  

Empirical-status integration: currently unreliable.**

The article cluster behaves more like a set of individually revised essays than a shared model whose dependencies update together.

## Final assessment

The article contains a worthwhile philosophical question but presently states its answer too strongly. Objective collapse could provide a physical architecture in which a psychophysical coupling law is formulated. It would not, by itself:

- demonstrate dualism;
- show that stochastic events are causally open to minds;
- establish agent-guided outcome selection;
- preserve exact Born statistics under such selection;
- solve the no-signalling and conservation constraints;
- distinguish consciousness modulation from another physical noise source.

Its empirical section also fails the user-facing promise of currentness. The decisive XENONnT result was available first as a 2025 preprint and as a peer-reviewed PRL from March 2026; the site’s own neighbouring article incorporates it. Carrying forward a 2022 journalistic verdict in September 2026 is therefore not merely ordinary publication lag.

The appropriate recommendation is **major revision, not rejection**. The conceptual trichotomy and ontology discussion are useful, but the page should be rebuilt around the distinction between:

1. **baseline collapse physics**;
2. **interpretive consequences of that physics**;
3. **compatibility with dualism**;
4. **a specific psychophysical coupling law**;
5. **evidence for that coupling law**.

At present those levels are repeatedly merged.

# Concrete potential improvements

## To specific articles

1. **Philosophical Stakes of Spontaneous Collapse:** Replace the opening thesis with the narrower claim that collapse theories determine the architecture and constraints of a possible mind–physics coupling, not whether consciousness is causally efficacious.
2. **Philosophical Stakes of Spontaneous Collapse:** Replace the 2022 experimental-status paragraphs with a dated model-by-model table covering Donadi 2021, Majorana 2022 plus its erratum, Vinante 2020, LISA Pathfinder 2025, Pedalino et al. 2026 and XENONnT 2026. State confidence levels, noise assumptions and parameter conventions.
3. **Philosophical Stakes of Spontaneous Collapse:** Separate five presently conflated items: original discrete GRW, mass-proportional Markovian CSL, regularised stochastic DP, Penrose’s heuristic instability criterion, and Orch OR.
4. **Philosophical Stakes of Spontaneous Collapse:** Remove “No free parameters” and “derives collapse from quantum gravity.” Replace them with language about a physically motivated timescale whose conversion into a complete stochastic theory requires additional choices.
5. **Philosophical Stakes of Spontaneous Collapse:** Correct the Chalmers–McQueen section. Explain why they reject scalar-Φ collapse, describe Q-shape operators, include the quantum-Zeno result, and state that their dynamics is not the Map’s exact-Born token-selection mechanism.
6. **Philosophical Stakes of Spontaneous Collapse:** Add a tails section and replace exact “branch destruction” language with a discussion of effective macroscopic definiteness under a specified primitive ontology.
7. **Philosophical Stakes of Spontaneous Collapse:** Add steelman subsections for Bohmian mechanics and Everett. Distinguish empirical objections from incompatibility with the Map’s tenets. Restore Bohmian mechanics to the list of no-collapse alternatives.
8. **Philosophical Stakes of Spontaneous Collapse:** Add an explicit model-desiderata box requiring a collapse operator, psychophysical variable, neural substrate, stochastic law, Born-rule derivation, no-signalling proof, energy budget, relativistic formulation and proposed discriminator.
9. **Spontaneous Collapse Theories:** Remove the still-current 2022 “survived by a whisker” verdict and synchronise its bounds with the Penrose article and XENONnT.
10. **Spontaneous Collapse Theories:** Correct the claim that physical GRW/CSL leave an actuality gap for consciousness. Standard GRW/CSL intend their stochastic law to determine the complete physical probabilities and realised collapse; adding consciousness creates a new model.
11. **Penrose Gravity-Induced Collapse and Empirical Prospects:** Retain its valuable convention and scope qualifications, but distinguish even more explicitly between the Diósi stochastic model tested experimentally and Penrose’s heuristic OR argument.
12. **Testing Consciousness-Collapse:** Promote the sentence that Tier‑1 evidence does not cascade to Tier 2 into a reusable warning displayed automatically on every collapse-and-consciousness page.
13. **Decoherence:** Move its interpretation-relative caveat into the summary and qualify later universal claims that “something must select.” The present page first concedes the framework dependence and then reasserts the single-outcome conclusion without qualification.
14. **Post-Decoherence Selection:** Require an explicit dynamical equation before describing post-decoherence selection as a physical locus. Explain that decoherence and collapse need not form two temporally sequential stages.
15. **Many Worlds:** Ensure that summaries imported elsewhere preserve its own verdict that Everettian probability programmes are contested, not refuted.
16. **Bohmian-mechanics articles:** Add reciprocal links from every collapse article and distinguish standard quantum-equilibrium equivalence from speculative non-equilibrium extensions.
17. **Free Will and Agent Causation:** Add a shared section separating indeterminism, causal efficacy, reasons-responsiveness and control. Collapse supplies at most the first without further theory.

## To the site’s methodology

1. Create a **machine-readable empirical-bounds ledger** recording model variant, governing equation, parameter convention, confidence level, publication date, DOI, assumptions and every dependent Map page.
2. Trigger a **dependency-wide review** whenever that ledger changes. A new XENONnT result should automatically flag all pages containing “GRW,” “CSL,” “DP,” “whisker,” R0​, λ or rC​.
3. Display a separate **“primary literature checked through” date**. An article’s AI-modified date is not evidence that its empirical claims are current.
4. Require a four-part template for physics–philosophy articles: **physical result; interpretive consequence; compatibility with a tenet; unsupported bridge still required**.
5. Extend citation review from metadata verification to **claim–source fidelity**. A reference being real does not validate the proposition attached to it; the Chalmers–McQueen Φ/Q-shape error illustrates the difference.
6. Require primary sources for every quantitative experimental verdict. Reviews and journalism may supply context but should not carry current bounds.
7. Add automated warnings for load-bearing phrases such as **“determines,” “demonstrates,” “requires,” “no free parameters,” “confirmed,” “ruled out”** and **“preserves causal connection.”**
8. Treat framework-boundary disagreements as permanent objects of review rather than reasons to stop reconsidering rivals. Each rival should receive its best ontology, dynamics and probability account before being judged incompatible with the Map.
9. Add a **cross-article contradiction test** that compares proposition strength, not merely links and keywords—for example, “determines” versus “leaves room,” or “the minimal design” versus “one possible design.”
10. Make the Tier‑1/Tier‑2 distinction a formal site-wide dependency: no empirical collapse result should be described as support for consciousness causation unless an independently discriminating Tier‑2 prediction is supplied.

## Verification Notes

Checked against the audited article's own text, the neighbouring Map articles the
reviewer invokes, and (for the source-fidelity charge) the primary source. Greps
used `grep -iF` with counts printed, per the corpus convention on false zeros.

**Verified — the audited article says what the reviewer quotes:**

- ✓ **The lede overclaim is verbatim.** `topics/philosophical-stakes-of-spontaneous-collapse`
  opens: "It determines whether consciousness is causally connected to physical reality
  at the deepest level." `topics/testing-consciousness-collapse` states the opposite in
  its own voice: "confirming that collapse is real would not confirm that consciousness
  drives it." This is a genuine internal contradiction between two live articles, not a
  matter of emphasis.
- ✓ **Chalmers–McQueen is misrepresented, confirmed at the primary source.** The article
  says "differences in integrated information (Φ) between superposed conscious states
  determine collapse rates." Chalmers & McQueen (arXiv:2105.02314) explicitly reject
  exactly that model: "A collapse model base[d] only on Φ would fail to collapse this
  superposition, despite it being a superposition of conscious states." Their developed
  proposal collapses "onto Q-shape" (the term occurs 151 times in the paper; it occurs
  0 times in the Map's article). The paper's abstract also states "Simple versions of the
  theory are falsified by the quantum Zeno effect" — a qualification the Map's account
  omits. **This is the strongest finding in the review and it survives primary-source
  checking.**
- ✓ **XENONnT is absent from the audited article (0 hits) and from
  `concepts/spontaneous-collapse-theories` (0 hits), while
  `topics/penrose-gravity-induced-collapse-empirical-prospects` carries it 5 times**,
  including "XENONnT has since set R₀ > 4.5 × 10⁻¹⁰ m at 95% confidence" and "XENONnT
  excluded it non-interferometrically in 2026." The reviewer's bound matches our own
  article's figure, so this is corroborated internally rather than taken on trust. The
  cluster-drift diagnosis is correct.
- ✓ **The Majorana dating error is real.** The article reads "the Gran Sasso germanium-detector
  null result of 2020 and its confirmation that August by the Majorana Demonstrator."
  Majorana published 16 August **2022**, not the August of the 2020 result. "Confirmation"
  also obscures that it was an independent white-CSL search with a DP reinterpretation.
- ✓ **Tenet-calibration drift is real and one-sided.** `concepts/spontaneous-collapse-theories`
  now reads "one minimal design" and "leave room for the causal connection" (the calibrated
  forms). The audited article still reads "provide the minimal design" and "preserve the
  ontological distinction." The sibling was calibrated; the target was not.
- ✓ **Bohmian mechanics is dropped from the falsification branch.** The lede names it as a
  live no-collapse alternative, but the "if collapse theories are experimentally falsified"
  paragraph narrows the field to "decoherence-only interpretations, many-worlds, epistemic
  readings like QBism—or something yet unknown." The omission is as described.
- ✓ **The tails problem and no-signalling are absent** (0 substantive hits each); the only
  "tails" match is an unrelated link line.

**Partly right — the reviewer's framing overstates one charge:**

- ~ **"Carrying forward a 2022 journalistic verdict" understates the article's existing
  hedging.** The article already flags its own staleness: "The most-quoted verdict on GRW
  dates from 2022, not from the present," and "whether the whisker-width margin survives
  the intervening results is a question the current bounds literature has to answer, not
  one the 2022 verdict settles by being carried forward." The defect is narrower than the
  reviewer implies — the article poses the right open question; the fix is to supply the
  answer our own Penrose article already holds, not to install a calibration the article
  lacks.

**Unverified — accepted as leads only, not as grounds for a claim:**

- ? The 9.1σ figure and the specific λ/r_C² bound attributed to XENONnT were not checked at
  the publisher. The R₀ bound was corroborated internally; these two were not.
- ? The January 2026 sodium-nanoparticle interferometry result (>7,000 atoms, >170,000 Da,
  macroscopicity μ = 15.5) and the 2025 LISA Pathfinder rotational-noise analysis were not
  independently verified. Any article edit citing them must verify at the publisher first.
- ? "Pedalino et al. 2026" appears only in the reviewer's recommendation list, with no
  citation given anywhere in the report. Treat as an unresolved lead.

**Not minted as tasks — re-carry candidates.** The review is long and its genuinely
verified core is narrower than its finding count. Left unqueued, in rough order of merit:
the tails problem and the no-signalling constraint as explicit omissions (5.1, and the
ensemble-equation demand in section 2); the preferred-basis problem recurring at the
psychophysical level (5.4); "randomness is not control" (5.5); relativistic completion
(5.7); and the methodology proposals, of which the empirical-bounds dependency ledger has
the strongest support — this is the second time an empirical update has failed to propagate
across this cluster.
