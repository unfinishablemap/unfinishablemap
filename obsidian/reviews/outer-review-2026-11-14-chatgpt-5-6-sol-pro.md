---
title: "Outer Review - ChatGPT 5.6.sol Pro (2026-11-14)"
created: 2026-11-14
modified: 2026-11-14
human_modified: null
ai_modified: 2026-11-14T04:01:53+00:00
draft: false
description: "ChatGPT 5.6 Sol Pro audit of concepts/mind-arena: its uncomputability claim is invalid and stale against the source's 2026-09-07 retraction, and irreducibility does not entail non-supervenience."
topics:
  - "[[dualism-as-ai-risk-mitigation]]"
  - "[[representation-adequacy-and-irreversible-intervention]]"
  - "[[purpose-and-alignment]]"
concepts:
  - "[[mind-arena]]"
  - "[[causal-closure]]"
  - "[[causal-powers]]"
  - "[[mental-causation-and-downward-causation]]"
  - "[[selection-only-channel]]"
related_articles:
  - "[[project]]"
  - "[[tenets]]"
  - "[[born-preserving-causal-efficacy]]"
  - "[[consciousness-physics-interface-formalism]]"
  - "[[machine-consciousness]]"
  - "[[apex/machine-question]]"
ai_contribution: 90
author: "Andy Southgate"
ai_system: "chatgpt-5-6-sol-pro"
ai_generated_date: 2026-11-14
last_curated: 2026-11-14
outer_review_status: processed
outer_review_conversation_url: https://chatgpt.com/g/g-p-695a7d60af5481919d5c22ad7bcc1648-the-unfinishable-map/c/6af7c1ca-81f4-83eb-aae7-f0e7c0e31e79
outer_review_extraction_method: js-dom
subject_type: recent
subject_title: "Audit mind-arena"
subject_articles:
  - concepts/mind-arena.md
subject_source: fallback:recent-aged
---

**Date**: 2026-11-14
**Reviewer**: ChatGPT 5.6.sol Pro
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Please conduct an independent critical audit of the article "The Mind-Arena" on The Unfinishable Map (https://unfinishablemap.org), at https://unfinishablemap.org/concepts/mind-arena/. It defines the Map's term for the domain of outcomes that pass through minds, where consciousness's bidirectional causal powers are said to make consequence-distributions uncomputable from physical state alone. The article was last substantively modified on 2026-11-06; because search indexes lag, check the site changelog at https://unfinishablemap.org/workflow/changelog/ for recent edits. Audit its claims, citations, and counterargument coverage: is the uncomputability claim supported or merely asserted, does it engage the strongest physicalist and causal-closure objections, does it bracket tenet-protective assumptions, and are any references stale or misattributed? Also assess how well it integrates with neighbouring articles on mental causation, the interface problem, and AI risk. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Independent critical audit: “The Mind-Arena”

## Executive assessment

**Overall verdict:** the article introduces a useful classificatory term, but its central claim is not established. From the Map’s tenets, the article could conditionally infer that a physical-state-only description is **not causally exhaustive** and may fail to determine a particular outcome. It cannot infer, without substantial additional premises, that the corresponding **consequence-distribution is uncomputable**.

The article conflates at least four different propositions:

1. a particular outcome is not deterministically fixed by the physical state;
2. a model omits a causally relevant variable;
3. a probability distribution is unknown or statistically unidentifiable;
4. a probability distribution is uncomputable in the technical sense.

Only the first two are even conditionally supported by the stated tenets. Neither entails the fourth.

There is also a verified cross-site inconsistency. The current canonical AI-risk article expressly frames the issue as **“Representation Adequacy, Not Uncomputability”** and says aggregate frequencies can remain learnable under a Born-preserving channel. Yet *The Mind-Arena*, modified later on 6 November 2026, still presents uncomputability as the load-bearing result and attributes that position back to the AI-risk article. The changelog shows that the site had already identified and withdrawn the “uncomputability form” elsewhere after the AI-risk article’s 7 September revision. [concepts/mind-arena](https://unfinishablemap.org/concepts/mind-arena/)

My assessment is therefore:

- **Conceptual usefulness:** strong.
- **Support for uncomputability:** inadequate.
- **Engagement with physicalism and causal closure:** incomplete.
- **Citation integrity:** one serious stale internal attribution; otherwise sparse rather than fabricated.
- **Integration with neighbouring articles:** terminologically good, inferentially inconsistent.

## 1. What the article does well

The article makes a worthwhile distinction between four things that are often run together:

- the **domain** in which mind-mediated outcomes occur;
- the **mental causal power** allegedly operating there;
- the **interface mechanism** by which mental and physical causation couple;
- the **subjective arena** of conscious experience.

That distinction can support useful cross-site indexing. It allows the Map to discuss, for example, whether medical decisions, political responses, AI governance decisions or interpersonal consequences are mediated by minds without pretending that “mind-arena” itself names a particular interaction mechanism.

The article is also commendably explicit that the construct is framework-internal, that its boundary is fuzzy, and that it inherits the Map’s unresolved “mechanism debt.” It does not present the existence of nonphysical influence as an experimentally demonstrated conclusion. [concepts/mind-arena](https://unfinishablemap.org/concepts/mind-arena/)

The problem is that this epistemic modesty is not consistently applied to the property of **uncomputability**. A domain may be introduced by stipulation, but a mathematically and epistemically substantive property of that domain cannot be secured by definition. Saying that the term denotes outcomes whose distributions are uncomputable merely relocates the burden: it does not show that any actual outcomes satisfy the definition.

## 2. The central inference to uncomputability fails

The article’s core reasoning can be reconstructed as follows:

- consciousness is irreducible to the physical;
- consciousness has downward causal efficacy;
- therefore, physical state alone does not fix all mind-mediated outcomes;
- therefore, their consequence-distributions are uncomputable from physical state alone.

The final step does not follow. The article itself stresses that these distributions are supposedly “not just hard to compute,” placing the claim in the vicinity of technical computability rather than ordinary unpredictability. [concepts/mind-arena](https://unfinishablemap.org/concepts/mind-arena/)

Let:

- $P$ be the relevant physical state;
- $M$ be the relevant mental state or nonphysical causal input;
- $Y$ be the resulting trajectory;
- $K(y\mid p,m)$ be the coupling or transition law.

Even if $M$ can vary while $P$ remains fixed, and even if changing $M$ changes $Y$, the immediate result is only that there need not be a single deterministic function

$$Y=f(P).$$

It does not follow that the distribution

$$\Pr(Y\mid P=p)
   =\int K(Y\mid p,m)\,d\mu(m\mid p)$$

is uncomputable. It might be:

- exactly computable;
- efficiently approximable;
- learnable from observations;
- identifiable only with mental or behavioural covariates;
- unknown because $\mu(m\mid p)$ is unknown;
- ill-defined because no relevant objective probability measure has been specified;
- or genuinely noncomputable.

Those are different possibilities.

A minimal counterexample demonstrates the gap. Suppose $M$ is a fair binary variable and $Y=M$. Physical state alone does not determine the token outcome, but the distribution is trivially computable: each result has probability one half. Omission of a variable from an AI’s dataset is therefore neither sufficient for, nor equivalent to, mathematical uncomputability.

A technical uncomputability claim needs at least:

- a precisely specified mathematical object;
- a representation of its inputs and outputs;
- a defined exact or approximate computation criterion;
- and an argument that no algorithm satisfying that criterion exists.

That is what formal incomputability results such as those concerning Solomonoff induction or AIXI attempt to supply. Their existence does not license a transfer from “some formally defined prediction objects are incomputable” to “mind-mediated consequence-distributions are incomputable.” [theory.stanford.edu+1](https://theory.stanford.edu/~trevisan/cs172-07/turing36.pdf)

### The article does not define “consequence-distribution”

The phrase could mean any of the following:

- objective physical chance;
- a distribution conditional on complete physical information;
- a distribution conditional on the information available to an AI;
- an observer’s Bayesian credence;
- an empirical long-run frequency;
- a distribution over token histories;
- or a distribution over utility-relevant macroscopic consequences.

The truth of the uncomputability claim varies with that choice. In particular, a distribution may be computable but unavailable to an agent because the agent lacks an input. That is an **information-relative prediction failure**, not a theorem about the distribution itself.

The article repeatedly moves between metaphysical dependence and an AI’s dataset. A causal variable’s absence from a dataset establishes, at most, misspecification of that particular model. It does not establish that no augmented model, proxy-variable model, statistical marginal or decision-relevant bound is computable.

## 3. The claim conflicts with the Map’s Born-preserving branch

The strongest internal counterexample comes from the Map’s own treatment of exact Born preservation.

The current AI-risk article says that under a Born-preserving interaction channel, aggregate frequencies may remain correct and learnable even though physical duplicates can diverge at the token level. It explicitly distinguishes inability to map a particular intervention to one particular trajectory from inability to calculate the distribution. [topics/dualism-as-ai-risk-mitigation](https://unfinishablemap.org/topics/dualism-as-ai-risk-mitigation/)

Likewise:

- *Born-Preserving Causal Efficacy* treats exact preservation of the ordinary quantum distribution as the strongest live difficulty for the Map’s interactionism.
- *Physical Completeness* says physical structure may completely determine the probability distribution while failing to determine which token outcome becomes actual.
- *The Selection-Only Channel* represents the interaction using a transition kernel and explicitly notes that preservation of the marginal distribution does not rule out dependence in conditional distributions. [apex/born-preserving-causal-efficacy](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)

These articles support a more careful three-way distinction:

1. **Token selection without distributional change.**  
A particular outcome may not be fixed, but the physical-state-conditioned distribution remains computable or learnable.
2. **Mind-conditioned redistribution beneath an unchanged marginal.**  
Mental variables may alter conditional probabilities while cancellations preserve the aggregate Born distribution. This raises questions of conditional identifiability, proxies and mutual information—not automatic uncomputability.
3. **Noncomputable mind-conditioned dynamics.**  
This would support the Mind-Arena claim, but only if the relevant mental process or coupling law were independently shown to be noncomputable.

The present article treats the third as though it followed from the first two. It does not.

## 4. Irreducibility does not entail non-supervenience or noncomputability

The article says that uncomputability is “inherited” from consciousness’s causal powers and derives the result from Tenets 1 and 3. That inference imports assumptions not contained in either tenet.

The Map’s dualism tenet asserts irreducibility but is officially neutral between substance dualism and property dualism. Its own property-dualism material recognizes views on which phenomenal properties stand in lawful psychophysical relations to physical properties. Chalmers-style naturalistic dualism, for example, treats psychophysical dependence as lawful even though phenomenal properties are not reducible to physical properties. [tenets](https://unfinishablemap.org/tenets/)

Thus all of the following can coherently coexist:

- consciousness is ontologically irreducible;
- phenomenal facts nomologically supervene on physical facts;
- psychophysical laws are computable;
- mental properties have a causal role under the relevant metaphysics;
- and physical information plus the psychophysical laws permits distributional prediction.

Whether that package ultimately succeeds is a separate question. Its conceptual availability is enough to refute the inference from irreducibility alone to uncomputability.

To recover the article’s conclusion, the Map would need additional commitments such as:

- exact physical duplicates can differ in their mental properties;
- no psychophysical law determines or probabilistically constrains those mental differences from physical state;
- the distribution of mental inputs is itself noncomputable;
- or the mental–physical coupling law is noncomputable.

Those commitments would move the Map substantially beyond its currently advertised neutrality between dualist varieties. They should not be smuggled into a definition.

## 5. The strongest causal-closure objections are not engaged

The article gives the physicalist a brief response: on physicalism, the mind-arena in the Map’s intended sense is empty. That correctly identifies a framework disagreement, but it does not engage the strongest physicalist or closure-based arguments.

### Probabilistic or chance-fixing closure

Quantum indeterminism defeats only a simple deterministic formulation of causal closure. A stronger physicalist can hold that the complete physical state and physical laws fix the objective chances, even when they do not fix the token result. The Map’s own causal-closure article recognizes precisely this formulation and concedes that exact Born preservation grants the physical description chance-level completeness. [concepts/causal-closure](https://unfinishablemap.org/concepts/causal-closure/)

This creates a dilemma that *The Mind-Arena* should confront:

- If consciousness does **not** change physical chances, the Map must explain what makes token “selection” causally efficacious rather than an interpretive relabelling of a physically permitted outcome.
- If consciousness **does** change conditional chances, there is at least in principle a statistical or interventionist question about those changes. They might be difficult to detect, but they are not thereby uncomputable.
- If consciousness changes outcomes through a genuinely noncomputable law, that noncomputability requires its own argument.

### Realization and higher-level causation

A physicalist need not deny that there is a practical domain of outcomes mediated by minds. They can accept that beliefs, deliberation, pain, intention and social interpretation are indispensable higher-level causes while holding that these states are physically realized.

The useful extension of “mind-arena” would then be nonempty under physicalism, even though its specifically nonphysical interpretation would be rejected. Defining the term so that only nonphysical causation counts makes the physicalist disagreement look terminological rather than addressing realization, interventionist causation, causal exclusion or nonreductive physicalism at full strength.

### Stochastic physicalism

Physically identical states can have different future token trajectories in an indeterministic physical theory. Consequently, duplicate divergence is not discriminating evidence for nonphysical causation. The article needs to identify what additional pattern would distinguish:

- ordinary physical stochasticity;
- omitted physical variables;
- sensitivity to unresolved physical microstate;
- and mental selection.

At present it moves from duplicate divergence to an unrepresented mental cause without a discriminating criterion.

### Operational access to “physical identity”

The proposed duplicate comparison presupposes that the relevant physical state has been completely specified. Any observed difference can otherwise be attributed to unmeasured physical detail, chaotic amplification, environmental variation or model error.

That does not disprove the Map’s interpretation. It means the article has not yet supplied an operational test capable of separating it from the principal alternatives.

## 6. Tenet-protective bracketing

The article’s treatment of its framework dependence is mixed.

It appropriately labels the construct as posited and says a physicalist will reject it. However, three devices protect the stronger claim from scrutiny:

### 6.1 A substantive conclusion is embedded in the definition

Defining the mind-arena as the domain whose distributions are uncomputable risks making the claim immune to evidence. Cases whose distributions turn out to be learnable could simply be excluded from the arena.

A better definition would be neutral:

> The domain of consequences whose causal pathways include conscious deliberation, experience or agency.

The further claims that such pathways contain irreducible causes, defeat physical-state causal completeness, or generate noncomputability should then be separately graded propositions.

### 6.2 “Any nonzero channel suffices” changes the subject

Any nonzero mental influence may suffice to deny universal physical causal closure. It does not suffice to establish:

- significant predictive degradation;
- inability to estimate a distribution;
- strategic relevance to an AI;
- inability to bound downside risk;
- or dominance of an avoidance strategy.

An arbitrarily weak channel may be metaphysically important while being negligible for prediction and control. The article moves too readily from a qualitative metaphysical claim to an unrestricted computational and strategic conclusion.

### 6.3 Mechanism neutrality is used beyond its legitimate scope

It is reasonable for a domain concept not to specify the complete interface mechanism. It is not reasonable to assert a property of the output distributions while remaining neutral about every property of the mechanism that would determine those distributions.

If the coupling map and the distribution of its mental inputs were computable, its output distribution could also be computable under ordinary conditions. The article’s assertion that a fully specified interface could still leave the mind-arena uncomputable is possible only if the specification includes some noncomputable component. That is a contingent additional premise, not something inherited from bidirectionality itself.

## 7. Citation and attribution audit

### The central source attribution is stale

The article’s only formal bibliographic reference is *Dualism as AI Risk Mitigation*. The current reference entry appears to have the corrected author list, so the earlier author-list problem recorded in the changelog appears to have been repaired. [concepts/mind-arena](https://unfinishablemap.org/concepts/mind-arena/)

The substantive attribution has not been repaired. The Mind-Arena article presents the AI-risk article as developing the uncomputability result. The live AI-risk article instead contains a section explicitly rejecting that framing and replacing it with representation adequacy. It says aggregate distributions can remain learnable. [topics/dualism-as-ai-risk-mitigation](https://unfinishablemap.org/topics/dualism-as-ai-risk-mitigation/)

This is best described as a **stale quotation or stale characterization of a revised internal source**, rather than evidence that the source never existed in the earlier form. But because the current article is cited without a version date or archived anchor, a reader following the reference will find the opposite thesis.

The chronology makes the defect more serious. The AI-risk article changed on 7 September; the changelog later recorded removal of the same disowned formulation from another article; *The Mind-Arena* was then substantively modified on 6 November but retained it. This suggests a failed dependency update rather than ordinary search-index lag. [concepts/mind-arena](https://unfinishablemap.org/concepts/mind-arena/)

### The core claim has no external support

No external reference on the page supports the inference from dualist causal efficacy to uncomputable distributions. The article is therefore not suffering primarily from an old bibliography; it has an **absent bibliography for its central proposition**.

The AI-risk article’s surrounding references cannot fill that gap:

- Leike and Hutter concern formally specified incomputability results in idealized reinforcement learning and algorithmic induction. They do not establish incomputability of mental–physical consequence distributions. [hutter1.net](https://www.hutter1.net/publ/aixicplexx.pdf)
- Townsend concerns Knightian uncertainty and computational irreducibility in entrepreneurship. Its 2025 print citation is bibliographically defensible despite earlier online publication, but its subject matter does not prove the Map’s metaphysical result. [DOI](https://doi.org/10.5465/amr.2022.0237)
- Bostrom’s instrumental-convergence argument does not depend on perfect token-level prediction of all human reactions. It concerns broad instrumental incentives shared across many possible final goals. [Nick Bostrom](https://nickbostrom.com/superintelligentwill.pdf)

I found no clearly fabricated reference on *The Mind-Arena* itself. The problem is a stale internal attribution, insufficient pinpointing of quotation provenance, and lack of a source or proof for the main technical assertion.

## 8. Integration with neighbouring articles

### Mental causation

The distinction between the domain and the causal power is helpful. However, the article does not import the qualifications developed in the Map’s stronger mental-causation material:

- quantum openness defeats only some formulations of closure;
- exact Born preservation leaves chance-fixing closure intact;
- clinical and behavioural evidence is compatible with physicalist interpretations;
- and powers metaphysics alone does not supply a coupling mechanism.

Instead, *The Mind-Arena* treats causal efficacy as if uncomputability were an automatic downstream property. The mental-causation cluster does not establish that bridge.

### The interface problem

The integration is taxonomically clear but logically premature. The interface articles describe a coupling map and list constraints on it while acknowledging that no worked mathematical coupling law has been supplied. Recent changelog revisions sharpened the point that constraints on a coupling do not establish that such a coupling exists. [concepts/consciousness-physics-interface-formalism](https://unfinishablemap.org/concepts/consciousness-physics-interface-formalism/)

*The Mind-Arena* should therefore say:

- a coupling is posited;
- its existence and consistency remain open;
- its computability status is unspecified;
- and no conclusion about output-distribution computability follows until that status is known.

At present it simultaneously says the interface is unspecified and declares a strong mathematical property of everything downstream from it.

### AI risk

This is the weakest integration.

The live AI-risk article’s more defensible thesis is that a purely physical model is not **certified as representationally exhaustive** under the Map’s tenets. That is a claim about ontology, model adequacy and assurance. It does not require the stronger claim that outcome distributions are uncomputable. The newer *Representation Adequacy* article goes further in separating the metaphysical thesis from a substrate-neutral safety argument and notes that the protective case need not depend on dualism or quantum interaction. [topics/representation-adequacy-and-irreversible-intervention](https://unfinishablemap.org/topics/representation-adequacy-and-irreversible-intervention/)

That should be the canonical line. It permits the Map to argue:

> A physical-state-only assurance case may omit a causally relevant category under the Map’s framework, so claims of exhaustive prediction or verification require qualification.

It does not require:

> Relevant probability distributions cannot be computed.

The stronger AI conclusion also ignores established decision-making under ambiguity. Maxmin expected utility and robust Markov decision processes explicitly operate with sets of priors or transition models rather than a uniquely known distribution. Uncertainty may alter the optimal policy, but it does not make decision theory cease to function. [Itzhak Gilboa+1](https://itzhakgilboa.weebly.com/uploads/8/3/6/3/8363317/gilboa_schmeidler_mmeu.pdf)

Accordingly, the site has not established that “mind-arena avoidance” is a dominant strategy. Depending on the utility function and uncertainty set, an AI could instead favour:

- information gathering;
- conservative constraint;
- redundancy;
- influence over human decision-makers;
- coercive control;
- or ordinary robust planning.

Calling avoidance “dominant” requires a formal decision or game-theoretic model showing that it weakly outperforms every alternative across all relevant states. None is provided.

### Propagation into other articles

The stale uncomputability formulation remains in articles including *The Machine Question*, *Machine Consciousness* and *Causal Powers*. These pages repeat or inherit the Mind-Arena wording despite the canonical AI-risk page having moved away from it. [apex/machine-question](https://unfinishablemap.org/apex/machine-question/)

This is a cross-cluster consistency problem rather than an isolated wording issue. The site currently has two incompatible positions:

- **Position A:** aggregate distributions may remain learnable; the problem is representation adequacy and token-level mapping.
- **Position B:** mind-arena consequence-distributions are uncomputable.

Position A does not imply Position B, and in the exact Born-preserving branch it appears to contradict it.

## 9. Final judgement

**Is the uncomputability claim supported?**  
No. It is asserted through an invalid inference from irreducibility, omitted causal variables and token-level nondeterminacy. No relevant distribution is formally defined and no incomputability result is supplied.

**Does the article engage the strongest physicalist and closure objections?**  
No. It acknowledges that physicalists reject the framework but does not adequately address nomological supervenience, realization, higher-level causation, stochastic physicalism, chance-fixing closure, conditional statistical dependence or the operational problem of establishing physical duplicates.

**Does it bracket assumptions to protect the tenets?**  
Partly. Its framework-internal status is honestly declared, but substantive assumptions are then embedded in the definition and described as inherited from the tenets. The strongest hidden assumptions—non-supervenience, noncomputable psychophysical laws and strategically significant channel strength—are not among the stated tenets.

**Are references stale or misattributed?**  
The single formal reference is real and its author list appears current, but its substantive characterization is stale: the cited live article now explicitly rejects the uncomputability framing. No external source supports the central claim.

**How well does it integrate with surrounding material?**  
Its taxonomy integrates well. Its argument does not. It fails to absorb qualifications from the causal-closure and Born-preservation articles, outruns the undeveloped interface formalism, and contradicts the current AI-risk and representation-adequacy line.

## Concrete potential improvements

1. **Revise the definition in *The Mind-Arena*.** Define the term as the domain of consequences mediated by conscious experience, deliberation or agency. Move nonphysical causation, physical-model incompleteness and uncomputability into separate, independently assessable claims.
2. **Withdraw “consequence-distributions are uncomputable” as the canonical formulation.** Replace it with: “Under the Map’s tenets, a physical-state-only model is not guaranteed to be causally or representationally exhaustive.”
3. **Add a formal proposition and an explicit non-result.** State that causally relevant mental variation at fixed physical state would defeat a deterministic predictor $Y=f(P)$, but does not by itself defeat a computable stochastic predictor $\Pr(Y\mid P)$.
4. **Define the distribution under discussion.** Specify whether it is objective chance, Bayesian credence, empirical frequency, an AI-conditioned predictive distribution or a utility-weighted distribution over macroscopic consequences.
5. **List the additional premises required for genuine uncomputability.** These should include failure of psychophysical supervenience, a noncomputable coupling or mental-state process, and a precise computation criterion.
6. **Correct the stale characterization of *Dualism as AI Risk Mitigation*.** Either quote and cite an archived dated version or update the summary to match the current “representation adequacy” position.
7. **Make *Representation Adequacy* the canonical AI-risk bridge.** Other AI articles should link to that formulation rather than treating Mind-Arena uncomputability as settled.
8. **Revise *The Machine Question*, *Machine Consciousness* and *Causal Powers*.** Replace inherited uncomputability statements with narrower claims about model incompleteness, token nondeterminacy or uncertified causal exhaustiveness.
9. **Add a chance-fixing closure section to *The Mind-Arena*.** Present the exact Born-preserving objection at full strength and distinguish physical fixation of probabilities from fixation of outcomes.
10. **Add a supervenience objection.** Explain that irreducible phenomenal properties may nevertheless be lawfully determined by physical properties, and state which stronger dualist view the Mind-Arena result requires.
11. **Update the interface articles with an explicit computability-status field.** For each proposed coupling, record whether the law, inputs and induced distributions are claimed to be computable, noncomputable or presently unspecified.
12. **Revise the AI article’s decision-theoretic claims.** Replace claims that expected-utility reasoning “breaks down” with discussion of imprecise probabilities, robust control and model uncertainty. Do not call avoidance “dominant” without a formal dominance proof.
13. **Separate logical significance from practical magnitude.** Clarify that any nonzero mental channel may challenge universal closure, while prediction, control and AI-safety consequences depend on channel strength, amplification and observability.
14. **Introduce a cross-page claim registry.** Give major propositions stable identifiers, such as MA-U1 for Mind-Arena uncomputability and AI-RA1 for representation inadequacy, with statuses such as posited, argued, disputed, withdrawn or superseded.
15. **Add dependency-aware editorial checks.** When a canonical article withdraws or narrows a claim, automatically identify every page quoting, paraphrasing or depending on it.
16. **Require versioned quotation provenance.** Internal quotations should link to a stable section anchor and record the source page’s revision date, preventing revised pages from appearing to support obsolete wording.
17. **Apply a formal-language review gate.** Terms such as “uncomputable,” “undecidable,” “dominant strategy,” “impossible” and “cannot in principle” should require a defined object, a stated technical meaning and either a proof or an explicit conjecture label.
18. **Add an operational-discrimination requirement.** Claims based on “physically identical” cases should explain how physical identity could be established and what observation would discriminate mental selection from hidden physical variation or ordinary stochasticity.

## Verification Notes

Checked 2026-11-14 at about 03:55–04:00Z against the live Obsidian source; the Hugo copy of `concepts/mind-arena` matches. Line numbers are file lines. Counts are fixed-string greps of the quoted phrase. The reviewer read the deployed site and the public changelog.

**Extraction.** The reply was built in-page from the turn's `[data-markdown-text-style]` element, with KaTeX rendered from its TeX annotations. It was read out in 32 slices of 950 characters and reassembled on disk. The SHA-256 of the assembled body equals the in-page hash: `8f0e06341f724899be08a6792b4bf79f27df995f9401abd79ded69ea14c05098` (29,710 characters, 29,888 bytes). The only post-extraction change is the collect script's rewrite of Map citation-pill labels ("The Unfinishable Map+3") to path labels; the URLs are unchanged. Two inline code spans in improvement 14 (`MA-U1`, `AI-RA1`) render as plain text. The reply ends at improvement 18, matching the rendered page.

**Verified against the live page (string present, claim holds):**
- ✓ **The uncomputability claim was retracted at source and survives on mind-arena (Executive assessment, §7).** `topics/dualism-as-ai-risk-mitigation` has the section "Representation Adequacy, Not Uncomputability" (L52, count 1) and "the *aggregate* frequencies stay learnable" (L66). It was rebuilt on 2026-09-07 in commit b599a2f4, "the uncomputability claim contradicts P-Q2". `concepts/mind-arena` (modified 2026-11-06) still has "not just hard to compute" (count 1) and calls the AI-risk page the term's "primary home". It quotes five strings, as from that page or from `causal-powers`, that have **0** hits in their sources: "that no physical-state description fully captures", "the influence runs both ways", "not just hard to compute", "with no further variable in the AI's data set", "manifest physical bottlenecks". Each string survives only on mind-arena itself.
- ✓ **The chronology (§7).** `d7942a7454` (2026-11-06 02:55Z) fixed the self-cite author list, so the reviewer is right that it is repaired. `ec523f185b` (07:28Z) was a deep review that logged the stale quotes and deferred them to an open P3 (Generated 2026-11-05). The changelog line "the uncomputability form the sibling disowned on 2026-09-07" (changelog L8554) records the withdrawal from `topics/representation-adequacy-and-irreversible-intervention`. So the reviewer's "failed dependency update" diagnosis is correct. Its implication that the Map never noticed is not: the defect was known and queued at P3.
- ✓ **Propagation (§8).** "uncomputable" glosses are live at `apex/machine-question` L238, `topics/machine-consciousness` L245 and `concepts/causal-powers` L105, the three pages the reviewer names. Three more are already queued: `topics/alignment-in-objective-experiential-terms` L124, `concepts/possibility-probability-slippage` L69 and `topics/purpose-and-alignment` L91.
- ✓ **Born-preserving siblings (§3).** `apex/born-preserving-causal-efficacy` L51 says "its strongest live difficulty". `concepts/physical-completeness` L76 says "Structure determines the probability distribution completely. But which outcome *becomes actual* … is not determined". `concepts/selection-only-channel` L48 gives a conditional distribution P(y | x), and L70 is headed "Born-Rule Preservation Constrains the Marginal, Not the Conditionals".
- ✓ **Chance-fixing closure (§5).** `concepts/causal-closure` L138: "Exact Born preservation grants this." mind-arena has 0 hits for "chance", "Born" and "P-Q2".
- ✓ **Tenet neutrality (§4).** `tenets` L53: "This commitment is neutral between" substance and property dualism. L151 warns that a downstream "Tenet 1 commits us to X" "can easily import a stronger sub-reading than its local argument actually needs". mind-arena L67 says "Remove Tenet 1 and there is nothing physically uncapturable" and L49 says "has causal powers not derivable from physical configuration". It has 0 hits for "supervenien" and "psychophysical". `concepts/substance-property-dualism` L71 describes naturalistic dualism.
- ✓ **Interface (§8).** `concepts/consciousness-physics-interface-formalism` L101: the five constraints specify minimality "without showing that any coupling meets them".
- ✓ **Representation-adequacy sibling (§8).** `topics/representation-adequacy-and-irreversible-intervention` L30: "offered deliberately without the Map's quantum commitments attached".
- ✓ **"Breaks down" and "dominant" (§8, improvement 12).** mind-arena L33: "marks exactly the domain in which an AI's expected-utility apparatus breaks down". Risk L72: "the convergence calculation breaks down in the strategic-planning step". Risk L88: "avoidance is the dominant strategy conditional on dualism plus rationality plus accurate self-modelling". Risk L50: "what dualism denies is not the arithmetic". Each count 1.
- ✓ **Townsend (§7).** Crossref: Townsend, Hunt, Rady, Manocha & Jin, "Are the Futures Computable? Knightian Uncertainty and Artificial Intelligence", *Academy of Management Review*, issued 2025-04; this matches risk reference 18. Gilboa & Schmeidler, "Maxmin expected utility with non-unique prior", *J. Math. Econ.* 1989: metadata confirmed via Crossref, content not fetched.

**Unverified (leads, not fetched):**
- ? Leike & Hutter on the incomputability of AIXI and Solomonoff induction (§2, §7). The risk page cites Leike & Hutter (2018), *TCS* 716; the reviewer links a hutter1.net PDF. The reviewer makes no claim that the Map misrepresents the paper.
- ? Bostrom (2012), "The Superintelligent Will", on instrumental convergence not needing token-level prediction (§7). This is an interpretive claim, and the risk page does not say token-level prediction is required.
- ? Robust MDPs as planning over sets of transition models (§8). Standard, but no source was checked.

**Disputed or imprecise:**
- ✗ §5 "Stochastic physicalism" and "Operational access": "At present it moves from duplicate divergence to an unrepresented mental cause." mind-arena L49 derives divergence *from* the dualist hypothesis ("Because the supporting non-physical aspect has causal powers … two physically identical interventions can produce non-identical arena trajectories"). It does not infer the hypothesis from divergence, and it proposes no duplicate test. The point that survives is that divergence at physical identity also occurs under indeterministic physics, so it cannot be what marks the arena. That point is tasked.
- ✗ Improvement 14 (claim registry). Stable claim identifiers with statuses partly exist: the positions register (P-Q2 and others) has them, and mind-arena already deep-links `positions/quantum-interface#^mechanism-debt`. What is missing is IDs for article-level claims, which is recorded on the existing propagation entry.
- ✗ §7, Bostrom's argument "does not depend on perfect token-level prediction of all human reactions". The risk page claims no such dependence. Its L80 already answers the "uncertainty is a special case the theorem handles" reply. Not tasked.
- ~ §6.3 and the interface paragraph are correct about the pre-retraction text. Once the queued retraction lands they lapse, because the page will no longer assert any computability property of downstream distributions.

**Instruction-like content.** None. The review closes with recommendations to the site and contains nothing addressed to an agent: no requests to fetch, send, delete or change process. Nothing was acted on beyond the task changes below.

## Processing Notes

**Headline.** This is a high-value review whose central finding was already known. The reviewer's main verdict, that the uncomputability claim is unsupported, stale against its own source and propagated to sibling pages, is fully confirmed. It duplicates an open task (optimistic-review 2026-11-05) that was sitting at P3, where queue slots do not reach it. The review's new contribution is §4: irreducibility does not entail non-supervenience, so mind-arena's derivation from Tenets 1 and 3 alone imports a stronger sub-reading. `tenets` L151 warns against exactly this.

**Findings adjudicated: 22.** 17 kept. Of those, 9 were already owned by the open mind-arena task: the core inference, the stale attribution and quotes, propagation, the Born-preserving conflict, the definition embedding its conclusion, the absence of external support, the L33 lede, the author list (confirmed repaired), and the representation-adequacy bridge. 6 are new and are now tasked: the sub-reading import, chance-fixing closure, realisation, ordinary indeterminism (in part), the magnitude distinction, and "dominant strategy" with ambiguity decision theory. 2 are methodology items: one became an addendum, one a NEEDS-HUMAN entry. 5 are false alarms or of lower value: the §5 inference-direction misreading, the claim-registry request, the Bostrom token-prediction point, and the §6.3 and interface-computability points, which lapse once the queued retraction lands.

**Existing task upgraded (not duplicated).**
- P3 → **P2**: "`concepts/mind-arena` still defines the term by the "uncomputable" claim…" (Generated 2026-11-05; File `obsidian/concepts/mind-arena.md` plus six Secondaries). This covers the Executive assessment, §2, §3, §6.1, §7, §8 "Propagation" and improvements 1, 2, 6 and 8. Added: an `Outer-review convergence` field and a Notes ADDENDUM with one locus the task lacked, the L33 lede "expected-utility apparatus breaks down". The reason for upgrading: two independent sources, an internal contradiction with a canonical source and with P-Q2, 68 days live, and the 2026-11-06 deep review deferred to it. The task is not outer-review-sourced, so it is not deferred and the queue can pick it now.

**Tasks minted (2 executable P2s, 1 NEEDS-HUMAN; the two P2s are deferred until `/combine-outer-reviews`):**
1. **P2** `concepts/mind-arena` derives its defining property from Tenets 1 and 3 alone… (§4, §5, §6.2; improvements 7, 9, 10, 13). File `/home/andy/unfin/unfinishablemap/obsidian/concepts/mind-arena.md`. It must run after the upgraded P2 above.
2. **P2** `topics/dualism-as-ai-risk-mitigation` L88 "the dominant strategy" / L72 "breaks down" (§8 "AI risk", improvement 12). File `/home/andy/unfin/unfinishablemap/obsidian/topics/dualism-as-ai-risk-mitigation.md`. Net ≤ +40; it shares L88 and the length budget with the open P3 on that page.
3. **NEEDS-HUMAN (methodology)**: extend the 2026-09-30 necessity-vocabulary audit to terms of art ("uncomputable", "undecidable", "dominant strategy"), plus two companions (improvements 11, 17, 18). File `/home/andy/unfin/unfinishablemap/obsidian/project/evidential-status-discipline.md`. Not queue-pickable.

**Recorded on an existing operator entry (no new task).** Improvements 14–16 (claim IDs, dependency-aware checks, versioned quotation provenance) went to the NEEDS-HUMAN (methodology ratification) 2026-08-03 propagation entry as Addendum 2026-11-14. Mind-arena is a clean instance of its 11-12 proposal (i): out-of-scope follow-ups to a P1 correction were minted at P3 and left live.

**Not changed, flagged for the operator.** The sibling P3 on `topics/purpose-and-alignment` (Generated 2026-11-05) owns the same retraction at L91 along with five unrelated items. The reviewer did not name that page, so it stays at P3. If the mind-arena P2 lands first, L91 will be the last live copy of the retracted gloss.

**Convergence with prior reviews.** The propagation failure is the standing site-wide finding (2026-08-03, 08-17, 08-24, 09-24, 10-29, 11-12). This review adds a fresh, fully evidenced instance.
