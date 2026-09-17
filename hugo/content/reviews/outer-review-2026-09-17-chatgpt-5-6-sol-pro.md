---
ai_contribution: 90
ai_generated_date: 2026-09-17
ai_modified: 2026-09-17 04:01:25+00:00
ai_system: chatgpt-5-6-pro
author: Andy Southgate
concepts:
- '[[near-perfect-adaptation-and-control-theoretic-competency-without-experience]]'
- '[[control-theoretic-will]]'
- '[[phenomenology-vs-function-axis]]'
created: 2026-09-17
date: &id001 2026-09-17
description: 'ChatGPT 5.6 Pro audit of the near-perfect-adaptation concept: citations
  sound, but the body slides from non-sufficiency to evidential orthogonality; scope
  conditions on RPA, Yi and Aoki need tightening. Major revision.'
draft: false
human_modified: null
last_curated: 2026-09-17
lastmod: 2026-09-17 04:01:25+00:00
modified: *id001
outer_review_conversation_url: https://chatgpt.com/g/g-p-695a7d60af5481919d5c22ad7bcc1648-the-unfinishable-map/c/6aab4c54-6104-83eb-ba6b-8564c42bc9e2
outer_review_extraction_method: js-dom
outer_review_status: processed
related_articles:
- '[[project]]'
subject_articles:
- concepts/near-perfect-adaptation-and-control-theoretic-competency-without-experience.md
subject_source: fallback:recent-aged
subject_title: Audit near-perfect-adaptation-and-control-theoretic-competency-without-experience
subject_type: recent
title: Outer Review - ChatGPT 5.6 Pro (2026-09-17)
topics:
- '[[bacterial-chemotaxis-and-minimal-biogenic-cognition]]'
- '[[interoceptive-consciousness-and-the-interface]]'
- '[[the-psychophysical-control-law]]'
---

**Date**: 2026-09-17
**Reviewer**: ChatGPT 5.6 Pro
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

You are an external referee auditing one article on The Unfinishable Map, a dualist philosophy site at https://unfinishablemap.org. The article is https://unfinishablemap.org/concepts/near-perfect-adaptation-and-control-theoretic-competency-without-experience/ ("Near-Perfect Adaptation and Control-Theoretic Competency Without Experience"), last substantively revised 2026-09-10. It argues that robust homeostasis and integral feedback control are domain-general competencies orthogonal to phenomenal experience. Audit it critically: check every empirical and citation claim against the primary literature (integral feedback, perfect adaptation in bacterial chemotaxis and biochemical networks, control-theoretic accounts of agency); assess whether "competency without experience" is argued or merely assumed; look for missed counterarguments from enactivism, predictive processing, and functionalist accounts; and flag tenet-protective bracketing, stale references, and weak integration with neighbouring Map articles. Consult the changelog at https://unfinishablemap.org/workflow/changelog/ for recent activity your search index may not yet reflect. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# External referee report

**Recommendation: Major revision**

## Scope and overall judgment

I audited the article as displayed after its substantive revision of **10 September 2026**, together with its target-specific review entry and the site changelog through **16 September 2026**. The internal review usefully corrected a defective Seth–Tsakiris attribution and checked that the cited papers existed. It did not, however, adequately test the scope conditions of robust perfect adaptation, distinguish theorem from implementation in Aoki et al., or examine whether non-sufficiency supports the much stronger claim of evidential orthogonality. The review also explicitly evaluated the article from within the Map’s tenets and left the title’s calibration unresolved. [near-perfect-adaptation-and-control-theoretic-competency-without-experience](/concepts/near-perfect-adaptation-and-control-theoretic-competency-without-experience/)

The article has a sound and worthwhile **narrow thesis**:

> Integral feedback and robust perfect adaptation can occur in systems for which phenomenal experience is not independently warranted; therefore, the presence of that local control motif is not by itself a sufficient criterion for consciousness.

It does **not** establish the stronger thesis advertised in its opening and conclusion:

> Control-theoretic competence is evidentially orthogonal to phenomenality, so increasing control sophistication supplies no evidence at all concerning experience.

The gap between those propositions is the central defect. The article establishes, at most, **non-sufficiency at a selected functional grain**. It repeatedly treats that as if it established conceptual independence, causal independence and Bayesian evidential independence. Those are different claims.

| Dimension | Referee finding |
| --- | --- |
| Bibliographic existence and basic metadata | Mostly pass |
| Fidelity of the Yi quotations | Pass |
| Definition and scope of robust perfect adaptation | Materially inaccurate |
| Treatment of bacterial chemotaxis | Correct core, overstated generality, stale boundary literature |
| Treatment of op-amp/PID implementations | Conflates an integral element with an end-to-end adaptive controller |
| Treatment of Aoki et al. | Real result, but theorem and experimental scope are exaggerated |
| Treatment of allostasis and predictive control | Flattens theoretically relevant architectural distinctions |
| “Competency without experience” | Demonstrated only for ordinary engineered controllers under an assumed non-consciousness premise |
| “No evidential purchase” | Not demonstrated |
| Enactivist, predictive-processing and functionalist replies | Substantially incomplete |
| Fit with the Map’s own tenets | Significant unresolved tension |
| Recommendation | Major revision rather than rejection |

## 1. Claim-by-claim empirical and citation audit

### 1.1 The definition of robust perfect adaptation is too strong

The article defines robust perfect adaptation as exact return to a set point “**regardless of disturbance size**.” That is not the control-theoretic or biological result.

Integral action can eliminate steady-state error for a specified class of persistent inputs or disturbances, provided that:

- the closed loop is stable;
- the plant and controller remain within their operating ranges;
- sensing and actuation have not saturated;
- the disturbance belongs to the class represented by the controller’s internal dynamics;
- the regulated variable and set point remain physically attainable.

“Robust” ordinarily concerns insensitivity to specified parameter variations or perturbations, not invariance under disturbances of unlimited amplitude. Yi et al. themselves make stability a condition of zero steady-state error and identify structural assumptions under which their result holds. Empirical chemotaxis also has finite operating ranges. [NCBI+2Stanford University+2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC18287/)

The article’s use of **near-perfect** does not rescue the definition. “Near-perfect adaptation” normally indicates small but non-zero residual adaptation error in the biological system. It does not mean “perfect over arbitrarily large disturbances, but with variable kinetics.” Precision, response time, dynamic range and stability are separable quantities.

A defensible replacement would be:

> Robust perfect adaptation is the asymptotic return of a specified regulated output to its set point, for a defined class of persistent perturbations and parameter variations, conditional on closed-loop stability and operation within the system’s dynamic range.

This correction matters because the current unlimited formulation drives the later rhetoric about substrate-indifferent, arbitrarily powerful competence.

### 1.2 Yi et al. (2000): faithful quotations, inflated attribution

The three quotations attributed to Yi et al. are materially faithful. The problem is the article’s surrounding claim that Yi and colleagues proved that bacterial chemotaxis, without qualification, achieves perfect adaptation by integral feedback.

Yi et al. analyse the Barkai–Leibler chemotaxis model and show that its architecture contains an integral-control structure under identifiable assumptions. Their paper:

- describes robust adaptation as occurring under most relevant conditions, not all possible inputs;
- explicitly specifies assumptions needed for the integral structure;
- shows that removing those assumptions produces adaptation errors;
- allows that the model may not completely explain experimentally observed adaptation and that additional downstream loops may contribute.

The result is therefore a powerful **model-structural explanation**, not an unrestricted organism-level theorem that every part of bacterial chemotaxis is an ideal integral controller. [NCBI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC18287/)

A better formulation would be:

> Yi et al. showed that, under the assumptions of the Barkai–Leibler receptor-adaptation model, the methylation dynamics instantiate integral feedback and thereby explain robust adaptation over a substantial operating regime.

That preserves the important result without converting a conditional analysis into an unlimited biological law.

### 1.3 Barkai–Leibler and Alon et al.: the strongest part of the empirical case

The treatment of Barkai and Leibler is substantially correct. Their proposed architecture showed how adaptation precision could be robust to changes in biochemical parameters without fine-tuning each rate constant. The article is also right to invoke Alon et al. as experimental evidence that substantial changes in chemotaxis-protein expression altered response properties and adaptation kinetics more readily than they destroyed adaptation precision. [Harvard Medical School+1](https://arep.med.harvard.edu/pdf/Barkai97.pdf)

Two qualifications are needed.

First, robustness to the experimental protein-concentration perturbations does not imply independence from all molecular quantities or all environmental regimes. Second, the Alon study supports a distinction between adaptation precision and other performance dimensions; it does not support the article’s unrestricted-disturbance definition.

This section should be retained, but used to support a more modest conclusion: biological control architecture can preserve one performance variable while allowing substantial variation in sensitivity, timing and steady-state activity.

### 1.4 The chemotaxis literature is stale at precisely the point where limits matter

The classic 1997–2000 papers remain indispensable, but stopping there gives a misleading impression that the empirical story ends with nearly unlimited robustness.

Later work documents at least two important boundaries:

1. **Receptor and methylation-range limits.** At high attractant concentrations, adaptation becomes increasingly imprecise as the available modification range is exhausted. The attainable range depends on receptor and ligand conditions. [PubMed+1](https://pubmed.ncbi.nlm.nih.gov/24416308/)
2. **Behavioural feedback and environmental geometry.** Whole-cell chemotactic performance is not determined by receptor adaptation alone. Coupling between swimming behaviour, spatial gradients and intracellular adaptation can produce bifurcations or regimes in which cells become trapped in non-productive behaviour. [PLOS+1](https://journals.plos.org/ploscompbiol/article)

These findings do not undermine integral feedback as an explanation of receptor adaptation. They undermine the article’s transition from that explanation to a globally substrate-neutral, disturbance-unlimited competence. They also illustrate why one cannot infer whole-agent capacities from a single local control motif.

### 1.5 Thermostats, PID controllers and op-amp integrators are being conflated

The article is right that a thermostat can regulate a variable without any plausible implication of experience, and that integral action can eliminate persistent offset in an appropriately designed feedback loop.

But the claim that the relevant competence is “**fully realised end to end**” in an op-amp integrator is technically wrong.

A bare op-amp integrator:

- computes an approximate time integral over a limited frequency and voltage range;
- does not itself contain a sensor, comparator, reference value, plant and actuator;
- is not, by itself, a closed-loop adaptive system;
- can drift or saturate at its supply rails;
- commonly requires additional resistance, bias compensation or anti-windup provisions for practical operation.

It is therefore an implementation of one mathematical operation used inside some controllers, not an end-to-end realization of robust homeostasis. [Stanford University+1](https://web.stanford.edu/~boyd/ee102/int-ctrl.pdf)

The article can obtain the philosophical result it wants without this error. A complete, ordinary PID-controlled industrial process is a much better example of sophisticated control without any independent reason to posit consciousness. That example establishes that integral control is not sufficient for experience. It does not depend on pretending that one amplifier component is a whole adaptive agent.

### 1.6 Aoki et al. (2019): real and important, but seriously overstated

Aoki et al. genuinely designed and implemented a biomolecular integral-feedback architecture in *E. coli*. Their antithetic controller is an important demonstration that integral control can be implemented synthetically in living cells, and their theoretical analysis has broad applicability. [Nature+1](https://www.nature.com/articles/s41586-019-1321-1.pdf)

The article nevertheless overstates the result with “**arbitrary molecular network on demand**.”

Several distinctions have been lost:

- **Theorem versus experiment.** The theoretical construction concerns networks that can be connected through the required sensing and actuation interfaces and that satisfy relevant realizability and stability conditions. The experiment did not install a controller successfully into every arbitrary biochemical network.
- **Average versus instantaneous behaviour.** Some guarantees concern population averages or long-time averages in stochastic systems, not exact trajectory-level control in every individual cell.
- **Stability.** Integral-feedback structure does not guarantee that the resulting closed loop is stable.
- **Dynamic range.** The controller and the biological host have finite sensing, actuation and resource ranges.
- **Dilution and degradation.** Molecular dilution, degradation and growth can destroy exact integral action unless the design compensates for them.
- **Implementation trade-offs.** Noise, response speed, burden and controller gain can trade off against adaptation quality.

Subsequent theoretical work explicitly discusses the ways dilution, degradation and stability can prevent exact perfect adaptation in synthetic integral controllers. [PubMed](https://pubmed.ncbi.nlm.nih.gov/32217822/)

A more accurate sentence would be:

> Aoki et al. demonstrated a synthetic biomolecular integral-feedback controller in *E. coli* and supplied a broadly applicable theoretical construction for compatible intracellular networks, subject to interface, stability, stochastic-averaging and dynamic-range conditions.

That is still a strong result. The current wording turns universality of architecture into universality of successful installation.

### 1.7 “Sensing,” “memory” and “decision” require operational definitions

Describing receptor methylation state as a form of short-term memory is legitimate at a functional level: past ligand conditions affect present response. Likewise, sensing can be defined as systematic transduction of environmental variables.

“Decision” is more delicate. A change in run–tumble probability can be described as action selection under a behavioural policy, but this should be stated explicitly. Otherwise the article first uses cognitively suggestive vocabulary to build a ladder of competence and then uses the resulting ladder to deny that any point on it is phenomenally significant.

The clean distinction is:

- **functional memory:** present state depends on relevant past inputs;
- **policy selection:** internal state changes the probability of available actions;
- **deliberative or phenomenal decision:** a much stronger claim not established by chemotaxis.

The article’s conclusion does not require denying the first two. It should instead prevent them from being rhetorically mistaken for the third.

### 1.8 Homeostasis and allostasis are not merely different strengths of one undifferentiated controller

There is a legitimate abstract continuity: both homeostasis and allostasis concern regulation. But the article’s ladder metaphor becomes misleading when it says there is no mathematically relevant transition along the way.

Allostatic and predictive accounts introduce potentially significant differences:

- anticipatory rather than merely error-reactive regulation;
- latent-state estimation;
- generative models of bodily and environmental causes;
- hierarchical predictions over different timescales;
- precision weighting and uncertainty;
- selection among policies;
- counterfactual forecasting;
- in active-inference formulations, an epistemic or information-seeking component.

Seth and Tsakiris explicitly discuss hierarchical, control-oriented interoceptive inference and acknowledge that the mapping from such machinery to conscious experience remains open. Pezzulo, Rigoli and Friston likewise present active inference as an attempt to integrate reactive homeostasis with model-based and goal-directed control, rather than as a larger thermostat. [Royal Holloway Research Portal+2City Research Online+2](https://pure.royalholloway.ac.uk/ws/portalfiles/portal/31327559/SethTsakiris_TICS_ACCEPTED_1_.pdf)

None of those distinctions proves consciousness. But they are exactly the distinctions a predictive-processing or functionalist opponent is likely to regard as relevant. Treating every architecture that can be called “control” as mathematically homogeneous begs the granularity question.

### 1.9 Cellular Basis of Consciousness is described recognizably but not refuted

The article fairly reports that Cellular Basis of Consciousness advocates attribute sentience or subjectivity to living cells. Reber and Baluška do defend a strong continuity claim in which sentience is coextensive with life. [Europe PMC](https://europepmc.org/article/MED/32950231)

But the op-amp comparison is not a standing reductio of that position. CBC does not normally infer consciousness from the presence of an integral term alone. Its advocates appeal to a package involving living organization, autonomous maintenance, evolutionary history, agency, cellular boundaries and endogenous valuation.

A non-conscious PID controller refutes:

> Every system implementing integral feedback is conscious.

It does not refute:

> Living, self-maintaining cellular organization has properties not captured by an externally designed electronic integrator and these properties ground minimal sentience.

The latter may still be false, but it requires a different argument. The article currently attacks a weakened surrogate for CBC.

### 1.10 Man and Damasio are made into a stronger opponent than they are

Man and Damasio propose that vulnerable, homeostatically regulated soft robots could provide a route toward feeling-like machines by supplying internally significant viability variables. This is a speculative design programme, not an empirical demonstration that homeostasis constitutes phenomenal experience. Their discussion also leaves room for machines that behave as though they feel without possessing full inner experience. [Nature](https://preview-www.nature.com/articles/s42256-019-0103-7.pdf)

The article may properly object that vulnerability and homeostatic regulation do not by themselves close the explanatory gap. It should not represent Man and Damasio as claiming that ordinary error correction, wherever implemented, is sufficient for phenomenality.

The relevant disagreement is about whether **endogenous vulnerability and self-maintenance add something evidentially or constitutively important**, not whether an op-amp’s integration operation feels like anything.

### 1.11 Seth and Tsakiris: quotation repaired, interpretation still too strong

The changelog documents the correction of an earlier phrase wrongly presented as a Seth–Tsakiris formulation. That was a genuine and appropriate repair. [deep-review-2026-09-10-near-perfect-adaptation-and-control-theoretic-competency-without-experience](/reviews/deep-review-2026-09-10-near-perfect-adaptation-and-control-theoretic-competency-without-experience/)

The current article nevertheless continues to compress their view too aggressively. Seth and Tsakiris explore how interoceptive inference, allostatic regulation and embodiment may contribute to forms of selfhood and conscious presence. They distinguish modest mechanistic claims from stronger life–mind continuity claims and acknowledge that direct evidence connecting particular computational operations to conscious phenomenology is limited. [Royal Holloway Research Portal](https://pure.royalholloway.ac.uk/ws/portalfiles/portal/31327559/SethTsakiris_TICS_ACCEPTED_1_.pdf)

Their position should therefore be described as:

- offering candidate mechanisms for aspects of embodied self-experience;
- treating interoceptive control as potentially explanatorily relevant;
- not showing that generic integral feedback is identical with consciousness;
- not claiming that every homeostatic process is conscious.

The article can still argue that the theory has not derived phenomenality. It cannot fairly turn that absence of derivation into evidence that the relevant architecture has no evidential bearing.

### 1.12 Schulkin, Sterling and Barrett: support for prediction, not for identity

Schulkin and Sterling support the distinction between reactive homeostasis and anticipatory, brain-centred allostatic regulation. That is relevant to the architecture of regulation, but it is not evidence that allostasis itself constitutes consciousness. [PubMed](https://pubmed.ncbi.nlm.nih.gov/31488322/)

The article also invokes Barrett in the text without supplying the corresponding bibliographic entry. Barrett and Simmons’ interoceptive-prediction work is an obvious primary source and should be cited directly. It concerns a predictive model of interoception and embodied affect, not a claim that ordinary integral control is phenomenally sufficient. [ResearchGate](https://www.researchgate.net/profile/Lisa-Barrett-3/publication/277411625_Interoceptive_predictions_in_the_brain/links/556dd49608aeab7772269af8/Interoceptive-predictions-in-the-brain.pdf)

This is the one clear bibliographic omission in the current reference apparatus.

### 1.13 Bibliographic verdict

I found no invented external paper among the listed references, and the current basic metadata is materially sound. The Yi quotations are accurate. The Seth–Tsakiris quotation defect recorded in the changelog has been repaired. [deep-review-2026-09-10-near-perfect-adaptation-and-control-theoretic-competency-without-experience](/reviews/deep-review-2026-09-10-near-perfect-adaptation-and-control-theoretic-competency-without-experience/)

The remaining citation problem is not mainly fabrication or misdating. It is **selective entailment**:

- classic papers are cited for conclusions broader than their scope conditions;
- later limiting evidence is absent;
- theorem and implementation are merged;
- speculative consciousness proposals are treated as stronger identity claims;
- Barrett is named without a reference;
- primary literature on agency, enactivism and functionalism is missing.

Citation fidelity now mostly passes. Citation coverage and inferential discipline do not.

## 2. Does the article establish “competency without experience”?

Only in a restricted sense.

Let I(x) mean that a system implements integral feedback and C(x) mean that it is phenomenally conscious. Accepting the ordinary premise that a conventional electronic controller is not conscious gives:

∃x[I(x)∧¬C(x)].

That is sufficient to refute:

∀x[I(x)→C(x)].

It does **not** establish:

P(C∣I)=P(C),

nor any other claim that integral control and consciousness are evidentially independent. Still less does it establish that richer organizational property F, of which integral control is one component, is unrelated to consciousness.

The article repeatedly moves without argument through four distinct propositions:

1. Integral feedback alone is not sufficient for consciousness.
2. Integral feedback is not identical to consciousness.
3. Integral feedback never contributes to a consciousness-supporting organization.
4. Integral feedback has no evidential bearing on consciousness in any context.

The controller examples support the first, and plausibly the second. They do not establish the third or fourth.

A symptom can be evidential without being sufficient. A component can be relevant in one larger organization while occurring harmlessly in many others. Evidential relevance is conditional on background theory, comparison class and organizational context. The article offers no data, psychophysical law or probabilistic argument establishing the required independence.

### The absence of experience is partly assumed

For conventional PID controllers, assuming no experience is overwhelmingly reasonable. It is nevertheless a background metaphysical and epistemic premise, not something measured by the controller experiment.

For bacteria and other living cells, the very question is contested. The article cannot classify those systems as demonstrated cases of competence without experience while also conceding that mechanistic completeness does not establish phenomenal absence. Its own mirror argument therefore blocks the biological examples from doing the work promised by the title.

The article proves that biological adaptation can be mechanistically explained without inserting an experiencer into the control diagram. That is not the same as proving that the adapting organism lacks experience.

### “Orthogonality” shifts meaning

At least three interpretations appear to be in play:

- **Substrate independence:** integral-control mathematics can be implemented in electronic and biochemical substrates. This is well supported.
- **Logical independence:** control competence and phenomenality can vary independently. Only one direction is illustrated, and even that relies on the assumed non-consciousness of engineered controllers.
- **Evidential independence:** observing control competence never changes the rational probability assigned to consciousness. This is not supported.

The article should either define orthogonality narrowly as substrate independence or abandon the term.

### Engineerability is not an argument for irrelevance

The fact that a mechanism can be engineered does not show that it is phenomenally irrelevant. A functionalist will regard engineered realization as entirely compatible with consciousness if the relevant total organization is reproduced. A dualist can likewise hold that an engineered organization falls under psychophysical laws.

Engineerability does establish that a mechanism is not uniquely biological. It does not establish that the mechanism, embedded within a richer architecture, carries no evidence.

### Explanatory closure is being asked to do too much

The article argues that once the control mechanism is specified, there is no residual functional job requiring an experiencer. That is a useful objection to explanations that insert consciousness merely as a homuncular gap-filler.

But physicalists, functionalists and most enactivists do not posit an extra experiencer to perform an otherwise unperformed control operation. They propose that phenomenal properties are identical with, realized by, constituted by, or nomologically associated with some richer organization. Showing that the organization works without adding an extra causal box does not address those positions.

The argument therefore defeats a naïve interventionist picture more readily than it defeats functionalism.

### The mirror argument is stronger than the headline thesis

The article’s best philosophical move is its symmetry claim:

- control-theoretic completeness does not prove experience;
- control-theoretic completeness does not prove the absence of experience.

That supports disciplined agnosticism. It does not support “**none of it is evidence**.”

The article should make this symmetry its conclusion and withdraw the stronger evidential-independence claim.

## 3. Missed counterarguments

### 3.1 Enactivism: endogenous normativity is not captured by the op-amp comparison

The strongest enactivist response is not that every feedback loop is conscious. It is that living agency involves an autonomous, precarious organization that establishes and maintains its own viability conditions.

Di Paolo’s account of adaptivity and Barandiaran, Di Paolo and Rohde’s account of agency distinguish:

- a controller whose reference value and purpose are assigned by an external designer;
- a self-producing system for which certain states matter because failure threatens the continuation of the organization itself.

On this view, normativity is endogenous to the organism’s organization rather than borrowed from an engineer’s intention. [University of Sussex+1](https://users.sussex.ac.uk/~ezequiel/autopoiesis_teleology_2005.pdf)

This does not prove phenomenal experience. Some enactivists themselves distinguish basic agency or sense-making from consciousness. But it blocks the article’s suggestion that an op-amp and a bacterium possess the same relevant competency merely because both admit an integral-control description.

The article needs to ask whether autopoiesis, precariousness and self-established norms alter the evidential situation—not merely whether the transfer functions can be written in similar notation.

### 3.2 Predictive processing: the opponent is not proposing a more complicated thermostat

Predictive-processing and active-inference accounts ordinarily appeal to a package involving hierarchical latent-variable models, prediction errors, precision control, action, interoception, temporal depth and policy selection. Some versions additionally appeal to counterfactual depth or epistemic action.

The relevant rival claim is therefore not:

> Integral feedback becomes conscious when enough loops are added.

It is closer to:

> Particular forms of hierarchically organized, embodied inference may realize or systematically support phenomenal content and selfhood.

Pezzulo, Rigoli and Friston explicitly use active inference to bridge reactive regulation and more flexible goal-directed control. Seth and Tsakiris place interoceptive control within a hierarchical account of embodied selfhood while acknowledging substantial explanatory gaps. [City Research Online+1](https://openaccess.city.ac.uk/id/eprint/16671/1/1-s2.0-S0301008215000908-main.pdf)

A strong audit should distinguish three questions:

1. Can predictive control occur unconsciously? Almost certainly.
2. Does predictive control suffice for consciousness? Not established.
3. Can particular predictive architectures nevertheless be evidence concerning consciousness? Still open.

The target article answers the third negatively by repeatedly demonstrating only the first.

### 3.3 Functionalism: local functional duplication is not total organizational duplication

Classical and later functionalism characterize mental states by their roles within a broader causal organization, not by the isolated possession of one operation such as integration. Putnam’s machine functionalism concerns total machine-state organization. Block’s objections likewise target the consequences of duplicating an entire functional organization, not the fact that individual control primitives are multiply realizable. [Utrecht University Philosophy+1](https://www.phil.uu.nl/~joel/3027/3027PutnamPsychPredicates.pdf)

The op-amp comparison therefore attacks an implausibly local functionalism:

> This component and that organism both integrate error; therefore, a functionalist must regard both as conscious.

No serious organizational functionalist is committed to that inference.

More importantly for this site, property dualism does not itself rule out organizational relevance. Chalmers’ organizational-invariance arguments are explicitly compatible with non-reductive or property-dualist metaphysics: phenomenal properties may remain irreducible while varying lawfully with causal organization. [Consciousness Network](https://consc.net/papers/qualia.html)

Thus the article cannot use dualism to move directly from irreducibility to evidential independence. A dualist still owes an account of which physical or functional structures are psychophysically correlated with experience.

### 3.4 Control-theoretic accounts of agency distinguish architectures the article collapses

The control tradition itself does not treat all feedback systems as equivalent. Rosenblueth, Wiener and Bigelow distinguished simple feedback behaviour from predictive forms of purposive behaviour. Conant and Ashby’s good-regulator theorem, under its assumptions, relates successful regulation to the possession of a model of the regulated system. [MIT Media Lab Courses+1](https://courses.media.mit.edu/2004spring/mas966/rosenblueth_1943.pdf)

Neither result proves phenomenality. They do show that control theory contains principled distinctions involving:

- fixed versus adaptive controllers;
- model-free versus model-based regulation;
- reactive versus anticipatory control;
- externally fixed versus internally revised goals;
- first-order versus hierarchical regulation;
- regulation of the world versus regulation of the controller’s own uncertainty.

The assertion that there is no relevant mathematical or organizational transition along the competency ladder is therefore too coarse. The article needs to show why these distinctions are irrelevant to its phenomenal question, not erase them by choosing the abstraction level “all are control.”

## 4. Tenet-protective bracketing

### 4.1 Tenet 1 does not entail evidential orthogonality

The article says “**Tenet 1 grounds the orthogonality**.” Yet the Map’s own tenets page presents the tenets as framework starting points rather than independently demonstrated conclusions. Tenet 1 asserts the irreducibility of consciousness. It does not assert that physical organization provides no evidence about where consciousness occurs. [tenets](/tenets/)

Irreducibility is compatible with:

- psychophysical laws;
- supervenience without reduction;
- lawful correlations with neural or functional organization;
- organizational invariance;
- physical evidence that rationally changes the probability of experience.

Consequently, the crucial inference is not merely framework-relative. It is invalid even within many dualist frameworks.

### 4.2 Tenet 3 creates a tension with the closure rhetoric

The Map also endorses bidirectional interaction. Its *Psychophysical Control Law* article acknowledges that the framework has not yet specified which physical output consciousness changes or how that intervention enters the physical control architecture. [the-psychophysical-control-law](/topics/the-psychophysical-control-law/)

The target article, by contrast, repeatedly presents the physical control account as leaving no functional work unperformed. Those positions can be reconciled only if the article specifies one of the following:

- consciousness changes reference values;
- consciousness changes precision or gain;
- consciousness selects among otherwise available policies;
- consciousness alters stochastic transitions at an implementation level;
- consciousness affects some variable omitted from the control description.

Without such a specification, the Map oscillates between two pictures:

1. the physical controller is functionally complete, making consciousness causally idle;
2. consciousness alters physical outcomes, making the physical controller incomplete as a full causal account of the realized trajectory.

The target article should acknowledge this as an unresolved Map-level tension rather than using physical closure as an argument against evidential relevance.

### 4.3 The framework-relative caveat comes too late

The body eventually admits that the conclusion is licensed by the Map’s framework rather than proved independently. That is intellectually preferable to presenting it as neutral fact.

But the title, opening and repeated categorical formulations remain stronger than the caveat. A reader encounters a universal verdict and only later learns that a disputed tenet has been used as a premise.

The title should state the narrower result, or include the same framework-relative qualifier used elsewhere on the site.

### 4.4 The internal review procedure was not adversarial enough

The September review did useful work on quotation fidelity and reference existence. It also explicitly concluded that a reviewer accepting the tenets would not object to the article’s central move, and then treated the article as converged despite retaining an open title-calibration question. [deep-review-2026-09-10-near-perfect-adaptation-and-control-theoretic-competency-without-experience](/reviews/deep-review-2026-09-10-near-perfect-adaptation-and-control-theoretic-competency-without-experience/)

That is a framework-coherence review, not an external referee review. The site’s own methodological notes elsewhere recognize that framework-internal convergence is not independent confirmation and that changes to upstream articles can invalidate downstream convergence. [changelog](/workflow/changelog/)

The target article particularly needed a reviewer instructed **not** to accept the inference from irreducibility to orthogonality.

The associated assessment note also begins from the intended conclusion that sophisticated regulation is orthogonal to experience. That invites confirmation rather than testing. [near-perfect-adaptation-and-control-theoretic-competency-without-experience-2026-07-15](/research/near-perfect-adaptation-and-control-theoretic-competency-without-experience-2026-07-15/)

## 5. Integration with neighbouring Map articles

### The bacterial-chemotaxis article

The neighbouring bacterial article repeats much of the same progression from methylation memory and adaptive behaviour to the conclusion that the mechanism provides no evidence for experience. It should share a common empirical module with the present article covering finite dynamic range, methylation saturation and whole-cell behavioural feedback. At present, duplication allows the same overstatement to be maintained in two places. [bacterial-chemotaxis-and-minimal-biogenic-cognition](/topics/bacterial-chemotaxis-and-minimal-biogenic-cognition/)

The two articles should also agree on a vocabulary table distinguishing functional sensing, memory, policy selection, agency and phenomenality.

### The interoception article

The Map’s interoception material already contains a more useful distinction: much visceral regulation is unconscious, while conscious interoceptive experience involves additional questions of representation, ownership, affect and accessibility. [interoceptive-consciousness-and-the-interface](/topics/interoceptive-consciousness-and-the-interface/)

The target article should import that distinction. It would permit a stronger and more precise argument:

> Homeostatic regulation is widespread and frequently unconscious; therefore, regulation alone is not sufficient. The open question is what additional organization transforms, accompanies or lawfully correlates with conscious bodily experience.

That is more defensible than declaring the entire control domain evidentially inert.

### *Control-Theoretic Will*

The Map’s *Control-Theoretic Will* article uses controller, plant, set point and error language positively to model conscious agency, while also saying that control formalism is metaphysically neutral. [control-theoretic-will](/concepts/control-theoretic-will/)

There is no outright contradiction if the target article merely says that control structure does not prove consciousness. There is a serious tension if it says control structure has no evidential relevance whatsoever.

The two articles need a shared account of:

- which control variables are conscious;
- whether consciousness is the controller, a set-point source, a policy selector or something else;
- what empirical observation would distinguish a conscious controller from an unconscious one;
- why the positive will model is informative if control organization is wholly orthogonal to experience.

### *Psychophysical Control Law*

This article should be a required dependency rather than a peripheral link. The present article’s claim of physical explanatory closure directly bears on the control-law article’s acknowledged mechanism debt. The target should contain a short section explaining whether its closure claim applies only to classical macroscopic dynamics while leaving a post-decoherence selection role open, or whether it is intended to be genuinely complete. [the-psychophysical-control-law](/topics/the-psychophysical-control-law/)

### *Phenomenology versus Function*

The neighbouring function article recognizes that functional equivalence depends on the grain at which function is specified. That issue is central here. An op-amp and a bacterium share integration at one grain; they do not share metabolism, autonomy, evolutionary organization, counterfactual modelling or total causal architecture. [phenomenology-vs-function-axis](/concepts/phenomenology-vs-function-axis/)

The present article should explicitly distinguish:

- sharing a local transfer function;
- sharing an end-to-end regulatory architecture;
- sharing total causal organization.

Without that distinction, its central comparison changes grain whenever convenient.

## 6. Referee conclusion

The article’s biological and engineering examples support an important corrective to over-interpretation:

> Robust adaptation, feedback competence and functional vocabulary such as memory or decision do not, individually or collectively at the currently specified level, entail phenomenal experience.

That conclusion is worth publishing.

The article does not establish:

- that experience and control competence are orthogonal;
- that integral feedback has no evidential value in any larger organization;
- that bacteria are cases of competence known to lack experience;
- that allostatic and predictive architectures are merely scaled thermostats;
- that engineerability defeats organizational functionalism;
- that a complete control description is compatible without further explanation with the Map’s bidirectional interaction tenet.

The central argument should therefore be reconstructed around **non-sufficiency, level of description and symmetric underdetermination**. A suitable revised title would be:

> **Near-Perfect Adaptation and Why Control Competence Alone Does Not Establish Experience**

A suitable replacement opening would be:

> Integral feedback and robust perfect adaptation are substrate-general control motifs. Their presence alone does not entail phenomenal experience, and ordinary engineered implementations show that the local motif is not a sufficient consciousness criterion. Whether such regulation contributes evidence when embedded in autonomous, model-based and embodied organization remains theory-dependent.

## Concrete potential improvements

1. **Retitle the target article** to state non-sufficiency rather than proven absence or orthogonality. Remove categorical claims that the examples are known cases of control competence without experience.
2. **Replace the definition of robust perfect adaptation** with one specifying regulated output, disturbance class, stability and operating range. Separate adaptation precision, response time, dynamic range and robustness to parameter variation.
3. **Rewrite the Yi paragraph** to say that integral structure was demonstrated in the Barkai–Leibler model under explicit assumptions, rather than proved without qualification for the entire bacterium.
4. **Retain Barkai–Leibler and Alon as the empirical centre**, but add later work on receptor saturation, finite methylation range and behavioural feedback. Explain that the classics establish impressive robustness, not unlimited invariance.
5. **Replace the bare op-amp example** with a complete engineered closed-loop controller. If the op-amp remains, identify it only as an implementation of an integral operation, not as an end-to-end homeostatic agent.
6. **Recast the Aoki discussion** to distinguish theoretical universality from experimental demonstration. Add stability, population/time averaging, finite dynamic range, dilution, degradation, noise and burden as scope conditions.
7. **Delete the inference from engineerability to phenomenal irrelevance.** Replace it with the valid conclusion that integral control is substrate-portable and therefore not uniquely diagnostic of biological consciousness.
8. **Introduce an explicit four-way distinction** among sufficiency, necessity, constitution and evidence. State precisely which of these the controller examples refute and which remain open.
9. **Define orthogonality or abandon it.** If it means substrate independence, say so. Do not use it to imply statistical, causal or evidential independence without a separate argument.
10. **Replace the single control ladder with a taxonomy** distinguishing reactive feedback, integral control, adaptive control, anticipatory allostasis, model-based regulation, hierarchical prediction, epistemic action and endogenous goal revision.
11. **Add a serious enactivist section** addressing autopoiesis, precariousness, adaptivity and endogenous normativity. Concede that these features may distinguish organisms from externally purposed controllers while arguing separately that they do not yet entail phenomenality.
12. **Add a serious predictive-processing section** addressing generative models, precision weighting, interoceptive inference, temporal depth and policy selection. Do not reduce the rival to the claim that a larger feedback loop becomes conscious.
13. **Add a serious functionalist section** explaining why duplication of one local operation is not duplication of total causal organization. Engage Putnam, Block and Chalmers, including the compatibility of organizational psychophysical laws with property dualism.
14. **Add primary control-theoretic agency sources**, including the distinction between reactive and predictive purposive behaviour and the qualified significance of internal models in successful regulation.
15. **Cite Cellular Basis of Consciousness proponents directly.** Represent their appeal to living autonomy and cellular organization before arguing that these properties remain insufficient to establish sentience.
16. **Correct the rival-theory bibliography.** Add the missing Barrett and Simmons source, retain the corrected Seth–Tsakiris attribution, and characterize Man and Damasio as advancing a speculative design programme rather than an empirical identity claim.
17. **Revise the bacterial-chemotaxis article in parallel.** Centralize the shared empirical account so that finite ranges and later counterevidence cannot drift between duplicated pages.
18. **Create a reciprocal handoff to the interoception article.** Use its distinction between unconscious regulation and conscious bodily representation to formulate the actual open explanatory question.
19. **Reconcile the target with *Control-Theoretic Will*.** Specify whether consciousness supplies goals, changes gains, selects policies or acts elsewhere. Explain why control formalism is positively informative there if it is claimed to have no evidential purchase here.
20. **Make *Psychophysical Control Law* an explicit dependency.** State how a bidirectionally efficacious consciousness can enter a control architecture that the target otherwise describes as functionally closed.
21. **Update *Phenomenology versus Function*** with the local-operation/whole-organization distinction and require the target article to use the same functional grain consistently.
22. **Clarify the Tenets page** by stating that irreducibility does not imply absence of psychophysical regularities or absence of evidence from physical organization.
23. **Split future reviews into two tracks:** one framework-internal review testing tenet coherence, and one framework-external review in which the tenets cannot be used to settle the disputed conclusion.
24. **Use a claim ledger for empirical articles** recording the exact claim, primary source, theorem or experiment status, assumptions, operating range, contrary evidence and strength of the supported inference.
25. **Add a theorem-to-implementation checkpoint** to the methodology. Any use of terms such as universal, arbitrary or on demand should identify whether the result is mathematical, simulated, demonstrated in one construct, or replicated across systems.
26. **Require “no evidence” claims to name a comparison class.** The article should state whether it means no evidence relative to a thermostat, no evidence conditional on being alive, or no incremental evidence after controlling for specified architecture.
27. **Require explicit falsifiers or defeaters.** The article should say what finding would make control organization evidentially relevant under the Map—for example, a reproducible psychophysical threshold associated with particular hierarchical, endogenous or counterfactual control properties.
28. **Add cross-article dependency tracking.** When an upstream empirical treatment such as bacterial chemotaxis or psychophysical control is revised, downstream “converged” articles should automatically be reopened.
29. **Remove conclusion-loaded assessment prompts.** Review notes should ask whether regulation is orthogonal to experience, not instruct reviewers to begin from that conclusion.
30. **Add a final title-and-abstract calibration pass** after substantive review. No article should be marked converged while its title asserts more than the body’s framework-relative and evidentially modest conclusion.

## Verification Notes

Processed 2026-09-17 by the outer-review skill. Every phrase the reviewer bolds as the article's wording was `grep -iF`-tested against `obsidian/concepts/near-perfect-adaptation-and-control-theoretic-competency-without-experience.md`; external sources were checked at PubMed, OpenAlex and the Nature abstract page (Europe PMC full text for Yi et al. returned an error stub, so the full-text-only claims below stay unverified).

**Verified claims:**
- ✓ All five verbatim attributions are in the article: "regardless of the disturbance's size", "fully realised end to end", "arbitrary molecular network on demand", "no joint at which the control mathematics changes character", "none of it is evidence [of felt experience]". "Tenet 1 grounds the orthogonality" drops only the parenthetical "(Dualism)". "No mathematically relevant transition" is a paraphrase of the verified "no joint" sentence, not a quotation.
- ✓ Yi et al. (2000): all three quoted spans are verbatim in the OpenAlex abstract, and the abstract also says the authors "demonstrate that integral control is structurally inherent in the Barkai-Leibler model and identify and characterize the key assumptions of the model" — which supports the reviewer's §1.2 point that the result is model-structural and assumption-relative, against the article's unqualified "proving that bacterial chemotaxis achieves".
- ✓ Barrett is named in the rival paragraph and has no entry in the References block (9 entries, none by Barrett) — the one bibliographic omission is real.
- ✓ PMID 24416308 = Neumann, Vladimirov, Krembel et al. (2014) *PLoS ONE*, "Imprecision of adaptation in Escherichia coli chemotaxis" — real and on-point for the finite-range boundary. PMID 32217822 = Baetica, Leong & Murray (2020) *Phys Biol*, "Guidelines for designing the antithetic feedback motif" — real, on dilution/degradation limits of synthetic integral control. PMID 32950231 = Reber & Baluška (2021) *BBRC*, "Cognition in some surprising places" — real.
- ✓ The neighbouring chemotaxis article contains no coverage of adaptation imprecision, receptor saturation or finite methylation range (six distinct terms, all zero; "Limits" appears once as a heading word only) — §5's duplication/drift concern stands.
- ✓ The interoception article does draw the unconscious-regulation line the reviewer says it does ("the visceral chemistry that never reaches awareness at all", L37).
- ✓ §4.2's reading of [the-psychophysical-control-law](/topics/the-psychophysical-control-law/) is accurate: it says "commitment alone does not constitute specification … which physical parameters change as a result" remains unspecified.

**Partially disputed claims:**
- ± §1.6 "arbitrary molecular network on demand" is an overstatement, but "arbitrary" is Aoki et al.'s own word: their abstract proves the topology "achieves robust perfect adaptation in arbitrary intracellular networks with noisy dynamics". The reviewer's real qualifications hold — the guarantee is "for the population-average and for the time-average of single cells", and it is a theorem plus one engineered construct, not universal installation. Task B keeps "arbitrary" only with those qualifiers.
- ± §1.9/§2 "bacteria are treated as demonstrated cases of competence without experience": the body does not say this — it says the ladder "leaves uncontested ground" at the engineered cell and that organisms' phenomenal status is "actively contested", and the CBC paragraph explicitly concedes the op-amp reductio "bites at the circuit and not at the engineered cell". The charge is true of the *title* and the opening's "none of it is evidence", not of the body's treatment of the biological rungs. That title finding converges with the open P3 title-calibration task (optimistic 2026-09-11; carried by the 2026-08-03 and 2026-09-10 deep reviews), now upgraded to P2.
- ± §1.10 Man & Damasio: the article already frames them with "propose … might thereby acquire" — a design programme, not an identity claim. The rival-section header's "constitutively tied to feeling" is the only overstatement; minor.
- ± §4.2 "oscillation" between closure and Tenet 3: the Tenet 3 paragraph already says regulation "can run without that interface", and the positions register locates the interface at post-decoherence selection ([P-Q1](/positions/quantum-interface/#p-q1)). This is a clarity defect (the article never says its closure claim is about the classical control description) rather than a Map-level contradiction. Folded into Task A rather than accepted as stated.

**Internal inconsistency the reviewer half-identified:** the ladder section concedes robust regulation is "a defeasible functional marker at best" — which grants evidential relevance — while the opening and closure sections say "none of it is evidence" and "no purchase … either way". The reviewer's §2 four-way distinction is the right repair; the article's own hedge shows which side it should land on.

**Unverified claims:**
- ? Yi et al.'s "under most relevant conditions" phrasing and the stated model-assumption sensitivity are in the full text, which Europe PMC did not serve; the abstract-level evidence already supports the point.
- ? The op-amp engineering claims (§1.5) are standard textbook material and were not source-checked; the argumentative point (an integrator is one operation, not a closed loop) is correct on inspection.
- ? Chalmers' organizational-invariance compatibility with property dualism (§3.3) was not re-fetched; it is the stated position of the "Absent Qualia, Fading Qualia, Dancing Qualia" paper and matches the Map's own [functionalism](/concepts/functionalism/) treatment.

**Stability notes honoured:** the 2026-09-10 deep review marks the physicalist and CBC boundary disagreements as bedrock and the thermostat→op-amp exemplar migration as converged. No task here re-litigates those; Task B rewords "fully realised end to end" without reverting the exemplar.

**Methodology recommendations (#23–#30) not minted as tasks:** the theorem-to-implementation checkpoint (#25) and the comparison-class requirement for "no evidence" claims (#26) are worth an operator look; the claim-ledger (#24) and calibration-pass (#30) proposals overlap the existing calibration-audit-triple and title-calibration conventions.