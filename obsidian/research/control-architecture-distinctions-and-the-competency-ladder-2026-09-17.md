---
title: "Research Notes - Control-Architecture Distinctions and the Competency Ladder"
created: 2026-09-17
modified: 2026-09-17
human_modified:
ai_modified: 2026-09-17T06:30:30+00:00
draft: false
description: "Research notes on the good-regulator theorem, the internal model principle and Rosenblueth-Wiener-Bigelow's purposive-behaviour taxonomy, and which control-architecture distinctions bear on the phenomenal question."
ai_contribution: 100
author: null
ai_system: "claude-fable-5-1"
ai_generated_date: 2026-09-17
last_curated: null
---

# Research: Control-Architecture Distinctions and the Competency Ladder

**Date**: 2026-09-17
**Source task**: P2 research-topic harvested from outer-review-2026-09-17-chatgpt-5-6-sol-pro §3.4 and §1.8
**Search queries used**: Crossref `works/{DOI}` for the three primaries and six rival-theory papers; OpenAlex `works/doi:` (abstract inverted index and `referenced_works`); Semantic Scholar graph API for Francis & Wonham; arXiv Atom API for 2503.00511 and 2508.06326; Europe PMC full-text XML for PMC4779150 and PMC3730701; WebSearch "good regulator theorem Conant Ashby critique assumptions", "Baltieri Biehl Capucci Virgo Bayesian interpretation of the internal model principle", "Rosenblueth Wiener Bigelow 1943 extrapolative orders of prediction".

## Executive Summary

The three leads in the task brief all verify at the publisher, with one correction: the good-regulator theorem's actual statement is far narrower than its title, and its own authors say so in the paper. Conant and Ashby (1970, *International Journal of Systems Science* 1(2), 89–97) prove that the *simplest optimal* regulator of a system is a deterministic function of that system's state, and they concede in the same paragraph that optimal regulators which are *not* such functions exist and are merely "unnecessarily complex". The 2020s literature (Wentworth 2021; Virgo, Biehl, Baltieri & Capucci 2025; Baltieri, Biehl, Capucci & Virgo 2025) treats the folk reading—every good regulator *contains* a model—as false or at best observer-relative. The internal model principle (Francis & Wonham 1976, *Automatica* 12(5), 457–465) is a structural-stability result about linear regulators and disturbance classes; it is not cited by any of the rival-theory papers checked here, and only reached the consciousness literature in 2025 via Baltieri et al.'s Bayesian reinterpretation. Rosenblueth, Wiener and Bigelow (1943, *Philosophy of Science* 10(1), 18–24) is a taxonomy paper: it nests non-predictive inside predictive feedback and then grades prediction by *order*, with an explicit speculation that the human–animal "discontinuity" lies in the order of prediction attainable.

For the Map the finding is discriminating in one direction only. Of the five architectural distinctions the review listed, three (fixed/adaptive, model-free/model-based, reactive/anticipatory) are mathematically principled *and* are invoked by predictive-processing / active-inference authors as the relevant transition—Pezzulo, Rigoli & Friston (2015), Friston (2013) and Seth & Tsakiris (2018) all cite Conant & Ashby by name for the claim. One (first-order/hierarchical) is principled but not the transition any rival theory of consciousness actually names: [[higher-order-theories|higher-order theories]] are about representation of mental states, not control hierarchy. One (regulating the world vs regulating one's own uncertainty) is the active-inference programme's own signature move and is the only distinction where a rival ties the transition to *experience specifically*. The interface reading predicts nothing about any of them, and the note says so; what it *can* say is that the good-regulator theorem, read correctly, is weaker than the near-perfect-adaptation article's opponents need.

## What the corpus currently says

Quoted so the eventual concept page can position itself against live text (all measured 2026-09-17).

- [[near-perfect-adaptation-and-control-theoretic-competency-without-experience]], "The Domain-General Ladder": "The ladder has no joint at which the control mathematics changes character—at one grain. Rungs can share a *local transfer function* (the op-amp and the bacterium do), an *end-to-end regulatory architecture* (the PID process and the engineered cell come closer), or a *total causal organisation* (no two rungs do, and that is the grain at which [[phenomenology-vs-function-axis|the phenomenology-function axis]] locates the real dispute with functionalism). The floor comparison holds at the first grain and says nothing at the third." The article never cites Conant & Ashby, Francis & Wonham or Rosenblueth et al. (0 hits each across topics/concepts/apex/voids/positions); the 2026-09-17 Claude outer review credits it with *avoiding* the good-regulator equivocation on exactly that ground.
- Same article, rival section: "Allostasis theorists (Sterling; Barrett & Simmons) distinguish *predictive* regulation—the brain anticipating needs before errors occur—from reactive homeostatic feedback, and route valence and arousal through that predictive-control architecture." And in reply: "'Genuine vulnerability,' 'self-model,' 'embodiment,' and 'prediction' are themselves functional and organisational notions. A system that models its own viability, predicts threats to it, and is materially destructible under load is a system with a more elaborate control architecture: richer than a thermostat's, but the same *kind* of thing".
- [[phenomenology-vs-function-axis]] fixes the grain question for its exemplars at task level ("The axis treats task-level function as the relevant grain") and concedes the functionalist's standing reply: "the function may differ at a finer grain than the experiments resolve … These responses move the dispute to the level of *which* function is the relevant one". It contains no control-theoretic vocabulary; the near-perfect article's pointer to it is a pointer to the *grain* move, not to any control content.
- [[control-theoretic-will]] runs the analogy in the opposite direction and makes a claim the folk good-regulator reading would contest: "The controller does not need to model the plant in full detail. It needs to observe relevant state variables, compare them against a setpoint, and output a corrective signal." Its open-questions section already lists "**Adaptive control.** Does the controller's strategy change with experience?" and "**Observability limits.** … the system is only partially observable." It cites Wiener (1948) but not the 1943 paper.
- Positions register (grep `control|regulat|model-based` in `obsidian/positions/`): no entry commits the Map on any control-architecture distinction. `agency-and-will.md` lists `control-theoretic-will` among its argued-in articles for the agent-causal position; `voids-as-evidence.md` uses "control" only in the experimental-control sense. The near-perfect article itself invokes only P-M1 and P-Q1. A new concept page would therefore not be constrained by, and would not need to amend, any registered claim.
- The Map's [[higher-order-theories]] article contains no occurrence of "hierarch", "regulat" or "control" (grep 2026-09-17)—consistent with the analytic finding below that HOT is not a hierarchical-*control* thesis.

## Key Sources

### Conant & Ashby (1970), "Every good regulator of a system must be a model of that system"
- **URL**: https://doi.org/10.1080/00207727008920220 (open copy: https://pespmc1.vub.ac.be/books/Conant_Ashby.pdf, 10 pp., text-layer PDF read in full)
- **Verified at**: Crossref (title with the dagger, authors "CONANT, ROGER C." and "ROSS ASHBY, W.", *International Journal of Systems Science* 1(2), 89–97, issued 1970-10); OpenAlex W4237718205 (abstract recovered from inverted index, matches the PDF verbatim; 1,057 citations)
- **Type**: Paper
- **Abstract (verbatim)**: "In this paper a theorem is presented which shows, under very broad conditions, that any regulator that is maximally both successful and simple must be isomorphic with the system being regulated. (The exact assumptions are given.) Making a model is thus necessary. The theorem has the interesting corollary that the living brain, so far as it is to be successful and efficient as a regulator for survival, must proceed, in learning, by the formation of a model (or models) of its environment."
- **Theorem statement (verbatim, §5)**: "By an optimal regulator we will mean a regulator which produces regulatory events in such a way that H(Z) is minimal. Then under very broad conditions stated in the proof below, the following theorem holds: Theorem: The simplest optimal regulator R of a reguland S produces events R which are related to the events S by a mapping h : S → R." Restated by the authors: "the best regulator of a system is one which is a model of that system in the sense that the regulator's actions are merely the system's actions as seen through a mapping h."
- **Assumptions (verbatim, from the proof)**: "The sets R, S, and Z and the mapping Ψ : R × S → Z are presumed given. We will assume that over the set S there exists a probability distribution p(S) which gives the relative frequencies of the events in S. We will further assume that the behaviour of any particular regulator R is specified by a conditional distribution p(R|S)". Success is *defined* as minimal outcome entropy H(Z) ("we define 'successful regulation' as equivalent to 'H(Z) is minimal'"). "Simplest" means the p(R|S) consisting "entirely of ones and zeroes", i.e. deterministic.
- **The authors' own qualifications (verbatim)**: "First, it leaves open the possibility that there are regulators which are just as successful (just as 'optimal') as the simplest optimal regulator(s) but which are unnecessarily complex. In this regard, the theorem can be interpreted as saying that although not all optimal regulators are models of their regulands, the ones which are not are all unnecessarily complex." And: "the proof of the theorem, by avoiding all mention of the inputs to the regulator R and its opponent S, leaves open the question of how R, S, and Z, are interrelated."
- **The paper's own reactive/anticipatory distinction (§3, verbatim)**: "Regulation by error-control is essentially information-conserving, and the entropy of Z cannot fall to zero (there must be some residual variation). When, however, the regulator … draws its information directly from D (the cause of the disturbance) there need be no residual variation: the regulation may, in principle, be made perfect." "Error-controlled regulation is in fact a primitive and demonstrably inferior method of regulation." The cow example follows: skin thermoreceptors let the nervous system "regulate before the error actually occurs".
- **Tenet alignment**: Neutral. The theorem is about the *structure* of an optimal regulator, with "model" meaning a homomorphic image; it carries no representational or phenomenal sense. The "living brain" corollary is a rhetorical extension the proof does not reach (see Wentworth, Virgo et al. below).
- **Note on misquotation**: the widely circulated form "every good regulator must *contain* a model" is not the theorem. The theorem says the simplest optimal regulator *is* a function of the reguland's state; the paper's fig. 1 / fig. 2 remark distinguishes "R is a model of S in the sense that the events R are mapped versions of the events S" from the stronger homomorphism case.

### Francis & Wonham (1976), "The internal model principle of control theory"
- **URL**: https://doi.org/10.1016/0005-1098(76)90006-6
- **Verified at**: Crossref (Francis, B.A.; Wonham, W.M.; *Automatica* 12(5), 457–465, issued 1976-09); OpenAlex W114979488 (2,866 citations; no abstract in index); Semantic Scholar (abstract "elided by the publisher"; 2,888 citations). Companion paper also verified at Crossref: Francis & Wonham (1975), "The internal model principle for linear multivariable regulators", *Applied Mathematics & Optimization* 2(2), 170–194, https://doi.org/10.1007/BF01447855.
- **Type**: Paper
- **Abstract**: NOT independently fetched—ScienceDirect returned 403 to both fetch routes and neither index carries the text. Do not install any quotation of the 1976 abstract in an article until it is read at the publisher.
- **Content (stated in my own words from Baltieri et al. 2025's verified formulation, below)**: in a linear regulation problem with a plant, a compensator and an exogenous disturbance/reference generated by a known autonomous system, output regulation that is *structurally stable* (robust to plant-parameter perturbation) requires the compensator to incorporate a copy of the disturbance generator's dynamics in the feedback path. Integral action is the special case where the exogenous signal class is constant steps—which is exactly why the near-perfect-adaptation article's integral-feedback motif can be described as "containing a model" of step disturbances without any cognitive connotation.
- **Relation to Conant & Ashby**: Baez (2016) reports that Francis & Wonham describe Conant & Ashby's paper as providing "plausibility arguments in favor of the internal model idea"—a secondary report; check the 1976 text before quoting. Virgo et al. (2025) describe the IMP as the good-regulator idea "taken up in control theory under the name 'internal model principle' (Francis and Wonham, 1976)".
- **Tenet alignment**: Neutral. A theorem about controller structure for a specified disturbance class.

### Rosenblueth, Wiener & Bigelow (1943), "Behavior, Purpose and Teleology"
- **URL**: https://doi.org/10.1086/286788 (text-layer copy read in full: https://home.csulb.edu/~cwallis/382/readings/482/wiener.behavior.purpose.teleology.1943.pdf)
- **Verified at**: Crossref (Rosenblueth, Arturo; Wiener, Norbert; Bigelow, Julian; *Philosophy of Science* 10(1), 18–24, issued 1943-01; Crossref carries the opening two paragraphs as abstract, matching the PDF)
- **Type**: Paper
- **Key points (verbatim)**:
  - "Active behavior may be subdivided into two classes: purposeless (or random) and purposeful."
  - "All purposeful behavior may be considered to require negative feed-back."
  - "Feed-back purposeful behavior may again be subdivided. It may be extrapolative (predictive), or it may be non-extrapolative (non-predictive). The reactions of unicellular organisms known as tropisms are examples of non-predictive performances. The amoeba merely follows the source to which it reacts; there is no evidence that it extrapolates the path of a moving source."
  - "Predictive behavior may be subdivided into different orders. The cat chasing the mouse is an instance of first-order prediction; the cat merely predicts the path of the mouse. Throwing a stone at a moving target requires a second-order prediction; the paths of the target and of the stone should be foreseen."
  - "it is possible that one of the features of the discontinuity of behavior observable when comparing humans with other high mammals may lie in that the other mammals are limited to predictive behavior of a low order, whereas man may be capable potentially of quite high orders of prediction."
  - "Teleological behavior thus becomes synonymous with behavior controlled by negative feed-back".
- **Tenet alignment**: Neutral on dualism; the paper is explicitly behaviourist in method ("the behavioristic approach consists in the examination of the output of the object and of the relations of this output to the input"). It is relevant to [[agent-teleology]] and [[biological-teleology-and-the-interface-framework]] as the historical origin of the feedback definition of purpose those articles work against or with. Note the paper's classification is a taxonomy of *behaviour*, not of controller architecture: predictive vs non-predictive is read off what the system does, which is exactly the Map's grain-of-function issue.
- **Recent secondary**: Nahas, A. (2026), "Revisiting Rosenblueth, Wiener, and Bigelow's 'Behavior, Purpose and Teleology' (1943)", *Biological Theory* 21, 210–216, https://doi.org/10.1007/s13752-026-00535-w (Crossref-verified; issued 2026-03-06; no abstract carried—not read).

### Virgo, Biehl, Baltieri & Capucci (2025), "A 'good regulator theorem' for embodied agents"
- **URL**: https://arxiv.org/abs/2508.06326 (v2, 2025-08-21; verified via arXiv Atom API; no journal reference; PDF read)
- **Type**: Preprint (cs.AI)
- **Key points (verbatim from abstract)**: "Artificial Life has produced many examples of systems that perform tasks with apparently no model in sight; these suggest Conant and Ashby's theorem doesn't easily generalise beyond its restricted setup." "whenever an agent is able to perform a regulation task, it is possible for an observer to interpret it as having 'beliefs' about its environment, which it 'updates' in response to sensory input … it necessitates a change in perspective, in that the observer plays an essential role in the theory: models are not a mere property of the system but are imposed on it from outside. Our theorem holds regardless of whether the system is regulating its environment in a classic control theory setup, or whether it's regulating its own internal state; the model is of its environment either way. The model might be trivial, however, and this is how the apparent counterexamples are resolved."
- **On the original (verbatim from body)**: the original "doesn't strictly succeed" in showing that every good regulator is a model "but only that some of them are (those that are not 'unnecessarily complex' in C&A's terminology)". The authors note this "has been noted previously in blog posts by Baez (2016) and Wentworth (2021)".
- **Tenet alignment**: Neutral, but useful: makes "having a model" observer-relative, which removes it as an intrinsic architectural joint.

### Baltieri, Biehl, Capucci & Virgo (2025), "A Bayesian Interpretation of the Internal Model Principle"
- **URL**: https://arxiv.org/abs/2503.00511 (v2, 2025-04-19; verified via arXiv Atom API; PDF read)
- **Type**: Preprint (math.OC)
- **Key points (verbatim from abstract)**: "The central claim of these results is that, under suitable assumptions, if a system (a controller) can regulate against a class of external inputs (from the environment), it is because the system contains a model of the system causing these inputs, which can be used to generate signals counteracting them." "It is however unclear whether the Bayesian internal models discussed in cognitive science bear any formal relation to the internal models invoked in standard treatments of control theory." Result: the IMP notion of model "can be seen as a special case of possibilistic Bayesian filtering."
- **From the body**: the authors flag that one of Hepburn & Wonham's assumptions ("Assumption 4") "seems to us rather difficult to motivate", and quote Wonham calling the environment a "convenient fiction" placeholder for disturbances.
- **Tenet alignment**: Neutral. This is the first formal bridge between the control-theoretic IMP and the Bayesian-brain "internal model"; before it, the equivocation between the two senses was unlicensed in both directions.

### Wentworth, J. (2021), "Fixing The Good Regulator Theorem" (blog post, LessWrong / Alignment Forum, 9 Feb 2021)
- **URL**: https://www.lesswrong.com/posts/Dx9LoqsEh3gHNJMDk/fixing-the-good-regulator-theorem (raw HTML grep-verified via greaterwrong mirror)
- **Type**: Blog post — not peer-reviewed; cite as the origin of the modern critique, which Virgo et al. (2025) acknowledge
- **Quote (verbatim)**: "If by 'making a model' one means the sort of thing people usually do when model-making—i.e. reconstruct a system's variables/parameters/structure from some information about them—then Conant & Ashby's claim is simply false. What they actually prove is that every regulator which is optimal and contains no unnecessary noise is equivalent to a regulator which first reconstructs the variable-values of the system it's controlling, then chooses its output as a function of those values (ignoring the original inputs). This does not mean that every such regulator actually reconstructs the variable-values internally."
- See also Baez, J. C. (2016), "The Internal Model Principle", *Azimuth* blog, 27 Jan 2016 (grep-verified), which introduces Scholten, D. L. (2010), "Every good key must be a model of the lock it opens (the Conant & Ashby Theorem revisited)"—an unpublished manuscript, not verified here.

## Rival-theory uptake (citation-graph check, OpenAlex `referenced_works`)

Which consciousness-adjacent papers actually cite the two theorems—checked rather than assumed:

| Paper (Crossref-verified) | Cites Conant & Ashby 1970 | Cites Francis & Wonham 1976 |
|---|---|---|
| Friston (2010) "The free-energy principle: a unified brain theory?", *Nat Rev Neurosci* 11, 127–138 | No (135 refs) | No |
| Friston (2013) "Life as we know it", *J R Soc Interface* 10, 20130475 | **Yes** | No |
| Pezzulo, Rigoli & Friston (2015) "Active Inference, homeostatic regulation and adaptive behavioural control", *Prog Neurobiol* 134, 17–35 | **Yes** | No |
| Seth (2015) "The Cybernetic Bayesian Brain", *Open MIND* | **Yes** (PDF grep: 6 hits; OpenAlex reference list incomplete) | No |
| Seth & Tsakiris (2018) "Being a Beast Machine", *TICS* 22, 969–981 | **Yes** | No |
| Baltieri & Buckley (2019) "PID Control as a Process of Active Inference with Linear Generative Models", *Entropy* 21, 257 | No (84 refs) | No |

How they use it (verbatim, Europe PMC / publisher PDFs):
- Friston (2013): "this is exactly consistent with the good regulator theorem (every good regulator is a model of its environment)".
- Pezzulo et al. (2015): "Conceptually, this speaks to the tenet of the good regulator theorem; namely, that any allostatic or homoeostatic system must entail a model of its exchange with the environment (Conant and Ashby, 1970)." This is the *folk* form the theorem does not prove.
- Seth & Tsakiris (2018): "In 1970, Ashby, with Roger Conant, proposed the influential 'good regulator theorem' which states that 'every good regulator of a system must be a model of that system' [41]." They then draw "a subtle but significant distinction between a system 'being a model', in the sense that it can be described in a model-based way, and 'having a model', in the sense of explicitly encoding a probabilistic model", and say process theories of active inference "address the distinction between 'being a model' and 'having a model' which is left ambiguous under this earlier theorem".
- Seth (2015), reconstructed across a two-column extraction: the 1970 paper "builds on the law of requisite variety by arguing (and attempting to formally show) that the nature of a controller capable of suppressing perturbations imposed by an external system (e.g., the world) must instantiate a model of that system. This provides a clear connection with the free energy principle". Note Seth's own hedge—"attempting to formally show"—and his acknowledgement in the same passage that cybernetics "is often taken to justify slogans of the sort 'the world is its own best model' (Brooks 1991)".

The IMP has no uptake in this literature at all; Baltieri et al. (2025) is the bridge.

## The Five Distinctions, Assessed

Short by design. For each: (a) mathematically principled? (b) claimed by a rival theory of consciousness as *the* relevant transition? (c) what the interface reading predicts.

1. **Fixed vs adaptive controller.** (a) Yes—adaptive control is a distinct discipline (parameter estimation in the loop). (b) No rival names *adaptivity per se* as the phenomenal joint; it is a precondition rivals assume. (c) Neutral. `control-theoretic-will` already lists adaptive control as an open question about the *conscious* controller, not as a marker of consciousness.
2. **Model-free vs model-based regulation.** (a) Principled in the RL/decision-theoretic sense (Daw–Dayan lineage; Pezzulo et al. 2015 use the pair 14 times), but the good-regulator theorem does *not* make the model-based side mandatory: it shows the simplest optimal regulator is a function of the reguland's state, and its own authors, Wentworth and Virgo et al. all deny that this entails an internal model. Under the IMP, integral feedback already "contains a model" of step disturbances—so the near-perfect-adaptation article's bottom rung is model-based in the only sense the theorem supplies. (b) Active inference invokes it (Pezzulo et al. 2015 explicitly bridge "reactive homeostasis" and "model-based, goal-directed control"). (c) Neutral—and the correct reading of Conant & Ashby is a resource *against* the rival's use of it: "must be a model" licenses nothing about having a representation, let alone experience. Seth & Tsakiris's being/having distinction concedes exactly this.
3. **Reactive (error-controlled) vs anticipatory (cause-controlled).** (a) Yes, and it is older than allostasis theory: Conant & Ashby §3 prove error-control leaves H(Z) strictly positive and call it "a primitive and demonstrably inferior method"; Rosenblueth et al. make predictive feedback a subclass and grade it by order. (b) This is the allostasis/interoceptive-inference programme's central transition (Sterling; Barrett & Simmons; Seth & Tsakiris) and the near-perfect article already registers it. (c) Neutral. A cow's skin thermoreceptors are cause-controlled regulation in Conant & Ashby's own example; nothing in the interface reading turns on it. Note for the article: Rosenblueth et al.'s *orders* of prediction give the competency ladder a principled graduation that the current text lacks—yet the same paper reads the order off behaviour, which is the task-level grain the [[phenomenology-vs-function-axis]] adopts and the functionalist reply exploits.
4. **First-order vs hierarchical regulation.** (a) Principled (cascade control; Powers' perceptual control theory, cited by Seth & Tsakiris as "overlooked"). (b) Predictive processing uses hierarchy constitutively (Pezzulo et al.: "Another pointer towards a hierarchical architecture…"). Higher-order theories do **not**: HOT's "higher order" is a representation *of a mental state*, not a controller supervising a controller; the Map's HOT article correctly contains no control vocabulary. The review's pairing of HOT with hierarchical regulation should not be adopted. (c) Neutral.
5. **Regulating the world vs regulating one's own uncertainty (precision).** (a) Principled within active inference (precision-weighting as gain control); Virgo et al. 2025 show formally that regulating one's own internal state still yields a model "of its environment either way". (b) This is the only distinction a rival ties to *experience specifically*: Laukkonen, Friston & Chandaria (2025, already quoted in the near-perfect article) locate minimal experience in "a recursive, precision-weighted self-model". (c) The interface reading predicts nothing here; the disagreement is the framework-boundary stalemate the near-perfect article already grades honestly. What a concept page can add is that the Map's uncertainty-regulating controller—if `control-theoretic-will`'s partial-observability remark is taken seriously—would itself fall on the "regulates its own uncertainty" side, so the distinction cannot discriminate between the Map and active inference.

**Net**: none of the five is interface-discriminating; two (2 and 4) are places where the rival's usage outruns the mathematics, and the concept page can say so with the primary text in hand.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1943 | Rosenblueth, Wiener & Bigelow, *Phil. Sci.* 10(1) | Purpose defined as negative feedback; predictive/non-predictive split; orders of prediction |
| 1948 | Wiener, *Cybernetics* | Already cited by `control-theoretic-will` |
| 1956 | Ashby, *Introduction to Cybernetics* (requisite variety) | Precursor the 1970 paper "builds on" (Seth 2015) |
| 1970 | Conant & Ashby, *Int. J. Syst. Sci.* 1(2) | Good-regulator theorem; error- vs cause-controlled regulation |
| 1973 | Powers, *Behavior: The Control of Perception* (Aldine) | Hierarchical PCT; cited by Seth & Tsakiris 2018 [42]—book, not index-verified here |
| 1975–76 | Francis & Wonham, *Appl. Math. Optim.* 2(2); *Automatica* 12(5) | Internal model principle for linear regulators |
| 2010 | Scholten, unpublished ms | Early critique ("good key … lock") — unverified |
| 2013–18 | Friston 2013; Pezzulo et al. 2015; Seth 2015; Seth & Tsakiris 2018 | Good-regulator theorem imported into FEP / allostasis / interoceptive inference |
| 2016, 2021 | Baez blog; Wentworth blog | Modern critique of the theorem's title claim |
| 2025 | Baltieri et al. (arXiv 2503.00511); Virgo et al. (arXiv 2508.06326) | Formal reassessment: IMP as possibilistic Bayesian filtering; observer-relative good-regulator theorem |
| 2026 | Nahas, *Biol. Theory* 21 | RWB 1943 revisited (not read) |

## Potential Article Angles

1. **A concepts page, "Control-Architecture Distinctions"** (headroom measured live 2026-09-17: `count_section_files('concepts')` = 326 against `max_concepts: 360`). Sections: the five distinctions with their provenance; the good-regulator theorem stated correctly with its two authorial caveats; the IMP as the reason integral feedback already "has a model"; the being/having distinction; a short "which of these bears on the phenomenal question" table concluding none is interface-discriminating. Link back from the near-perfect article's grain sentence and from `control-theoretic-will`'s adaptive-control and observability questions. Tenet relation: Tenet 1 via the [[phenomenology-vs-function-axis]] grain argument; Tenet 3 via the psychophysical-control-law point that the interface enters below the grain at which any of these architectures is specified ([[the-psychophysical-control-law]]).
2. **Alternatively, no new page**: fold a single paragraph into the near-perfect article's ladder section giving Rosenblueth et al.'s orders of prediction as the ladder's graduation and one sentence on the good-regulator theorem's real content. This costs ~150 words in an article already near its ceiling and leaves the IMP and the 2025 literature homeless; the concept page is the better home. The Vetoed bank was not consulted by design; nothing in the corpus argues against creation.

When writing, follow `obsidian/project/writing-style.md`: front-load the corrected theorem statement; use named-anchor summaries for the five distinctions; do not use the "This is not X. It is Y." construct.

## Gaps in Research

- Francis & Wonham (1976) abstract and theorem statement not read at the publisher (403). Metadata verified; content stated via Baltieri et al. 2025. Must be read before any quotation is installed.
- Nahas (2026) not read; no abstract in Crossref.
- Powers (1973) and Scholten (2010) not index-verified.
- Seth (2015) quotation reconstructed across a two-column PDF extraction; re-read the single-column publisher HTML before quoting.
- The 1970 open-copy PDF has minor OCR damage ("in fad" for "in fact", "H" for "R" in one sentence); quotations above were checked against context but a second copy should be consulted if any is installed verbatim.
- Not researched: whether any higher-order theorist has explicitly framed HOT in control-hierarchy terms (Lau, Rosenthal, Brown). The absence claim above rests on the Map's own HOT article and on the standard HOT definition, not on a literature sweep.

## Citations

- Baez, J. C. (2016). The Internal Model Principle. *Azimuth* (blog), 27 January 2016. https://johncarlosbaez.wordpress.com/2016/01/27/the-good-regulator-theorem/
- Baltieri, M., & Buckley, C. (2019). PID Control as a Process of Active Inference with Linear Generative Models. *Entropy*, 21(3), 257. https://doi.org/10.3390/e21030257 (Crossref)
- Baltieri, M., Biehl, M., Capucci, M., & Virgo, N. (2025). A Bayesian Interpretation of the Internal Model Principle. arXiv:2503.00511v2 [math.OC]. https://arxiv.org/abs/2503.00511 (arXiv API)
- Conant, R. C., & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2), 89–97. https://doi.org/10.1080/00207727008920220 (Crossref; OpenAlex W4237718205; primary PDF read)
- Francis, B. A., & Wonham, W. M. (1975). The internal model principle for linear multivariable regulators. *Applied Mathematics & Optimization*, 2(2), 170–194. https://doi.org/10.1007/BF01447855 (Crossref)
- Francis, B. A., & Wonham, W. M. (1976). The internal model principle of control theory. *Automatica*, 12(5), 457–465. https://doi.org/10.1016/0005-1098(76)90006-6 (Crossref; OpenAlex W114979488; Semantic Scholar; abstract not read)
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138. https://doi.org/10.1038/nrn2787 (Crossref)
- Friston, K. (2013). Life as we know it. *Journal of the Royal Society Interface*, 10(86), 20130475. https://doi.org/10.1098/rsif.2013.0475 (Crossref; Europe PMC PMC3730701 full text)
- Nahas, A. (2026). Revisiting Rosenblueth, Wiener, and Bigelow's "Behavior, Purpose and Teleology" (1943). *Biological Theory*, 21, 210–216. https://doi.org/10.1007/s13752-026-00535-w (Crossref; not read)
- Pezzulo, G., Rigoli, F., & Friston, K. (2015). Active Inference, homeostatic regulation and adaptive behavioural control. *Progress in Neurobiology*, 134, 17–35. https://doi.org/10.1016/j.pneurobio.2015.09.001 (Crossref; Europe PMC PMC4779150 full text)
- Rosenblueth, A., Wiener, N., & Bigelow, J. (1943). Behavior, Purpose and Teleology. *Philosophy of Science*, 10(1), 18–24. https://doi.org/10.1086/286788 (Crossref; primary PDF read)
- Seth, A. K. (2015). The Cybernetic Bayesian Brain: From Interoceptive Inference to Sensorimotor Contingencies. In T. Metzinger & J. M. Windt (Eds.), *Open MIND*, 35(T). MIND Group, Frankfurt. https://open-mind.net/papers/the-cybernetic-bayesian-brain (publisher PDF read; Crossref lookup of the chapter DOI failed—verify DOI before citing)
- Seth, A. K., & Tsakiris, M. (2018). Being a Beast Machine: The Somatic Basis of Selfhood. *Trends in Cognitive Sciences*, 22(11), 969–981. https://doi.org/10.1016/j.tics.2018.08.008 (Crossref; accepted-manuscript PDF read)
- Virgo, N., Biehl, M., Baltieri, M., & Capucci, M. (2025). A "good regulator theorem" for embodied agents. arXiv:2508.06326v2 [cs.AI]. https://arxiv.org/abs/2508.06326 (arXiv API; PDF read)
- Wentworth, J. (2021). Fixing The Good Regulator Theorem. *LessWrong / AI Alignment Forum*, 9 February 2021. https://www.lesswrong.com/posts/Dx9LoqsEh3gHNJMDk/fixing-the-good-regulator-theorem
