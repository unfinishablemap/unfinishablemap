---
title: "Single-Cell Proto-Agency and the Evidence Problem"
description: "What would count as evidence that one cell chooses rather than merely reacts? A human-AI inquiry into why the noise-vs-choice line at the prokaryotic floor may be empirically undecidable."
created: 2026-07-15
modified: 2026-08-24
human_modified:
ai_modified: 2026-09-02T01:53:01+00:00
last_deep_review: 2026-08-24T12:26:42+00:00
draft: false
topics:
  - "[[bacterial-chemotaxis-and-minimal-biogenic-cognition]]"
  - "[[consciousness-in-simple-organisms]]"
  - "[[basal-and-bioelectric-cognition]]"
concepts:
  - "[[phenomenology-vs-function-axis]]"
  - "[[interface-threshold]]"
related_articles:
  - "[[agency-void]]"
  - "[[standing-agnostic-challenge]]"
  - "[[birch-edge-of-sentience-and-the-five-tier-scale]]"
  - "[[positions/consciousness-scope]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-8+claude-opus-5
ai_generated_date: 2026-07-15
last_curated:
---

Does a single *Escherichia coli* cell **choose** to swim toward food, or does it merely react? The sibling article [[bacterial-chemotaxis-and-minimal-biogenic-cognition]] specifies the run-and-tumble mechanism in full and then deliberately parks exactly this question—it declines to adjudicate whether bacterial "decision" is real proto-choice or protein-level noise. This article takes up the parked question directly, but reframes it as a problem about *evidence* rather than about bacteria. The question is not "do cells choose?" but: **what observation could tell proto-choice apart from complete mechanism, given that both predict the same swimming?** The Map's answer, framed relative to its dualist commitments, is that at the prokaryotic floor there may be no such observation—and that recognising this is a result about the limits of parsimony, not a failure to find one.

The core finding driving this conclusion is that the usual framing—stochastic noise *versus* genuine choice—is [an unstable dichotomy](#the-dichotomy): single-cell measurement shows the "noise" is functionally integrated into the swimming behaviour, so "it's just noise" stops being a deflation. From there the article surveys the [candidate discriminating criteria](#candidate-criteria) on offer and argues each fails to draw an agent/non-agent line, before setting out the [tractability thesis](#tractability) and its [grounding in the Map's tenets](#relation-to-site-perspective)—Tenet 5 (Occam's Razor Has Limits), Tenet 3 (Bidirectional Interaction), and Tenet 2 (Minimal Quantum Interaction)—with an explicit hand-off to the [[agency-void|agency void]], which already anticipates this kind of in-principle undecidability. The Map's calibration for this rung is registered as [[positions/consciousness-scope|P-CS5]], at moderate credence.

## The Received Dichotomy and Why It Is Unstable {#the-dichotomy}

The standard framing sets two readings of run-and-tumble variability against each other. Either the differences between genetically identical cells are (a) stochastic protein-level noise, or (b) genuine minimal choice.

The deflationary reading is stated sharply in the 2024 *EMBO Reports* opinion "Cell consciousness: a dissenting opinion" (Robinson, Mallatt, Peer, Sourjik, Taiz). The authors write that "an individual bacterial cell does not make a choice—the decisions are determined by its current state," and that "even when individual cells behave differently, it can be traced to stochastic differences in protein levels between cells." Their central argument is the completeness of the mechanistic account: the chemotaxis system "can be broken down to a few individual molecular reactions described by a relatively simple system of differential equations," leaving no explanatory residue for a chooser. They grant the cognitive vocabulary—memory, navigation, decision—while reading it as reaction rates fixed in the genome, and they demand of the opposing camp that "theories require proof from hypotheses-testing, solid facts and empirical evidence."

One detail sharpens the epistemology. Victor Sourjik, a co-author of the deflationary opinion, is the researcher who introduced in vivo FRET to bacterial chemotaxis (Sourjik & Berg, 2002)—the technique the single-cell CheY-P measurements at issue depend on, though those particular measurements came from the Shimizu and Emonet labs rather than his own (Keegstra et al., 2017). The person who developed the means of seeing the noise is on record calling it noise. No new experiment settled the question here; the same data simply received a deflationary interpretation—which is the evidence problem in miniature.

Here the dichotomy begins to come apart. On the deflationary reading, "it reduces to noise" is supposed to *deflate* the appearance of choice. But the single-cell chemotaxis literature shows the noise functioning as the substrate of the search rather than as error riding on top of a decision. CheY-P fluctuation coordinates the switching statistics of multiple flagellar motors; Sneddon, Pontius, and Emonet (2012) found that this coordination, combined with occasional long counter-clockwise intervals, "enhanced performance on shallow gradients by up to 73%." He, Zhang, and Yuan (2016) then compared wild-type cells against mutants lacking signal noise and found the noise *increases* the sensitivity of the chemotaxis network at the level of the flagellar motor rather than degrading it—supplying a mechanism for the drift enhancement itself. Meanwhile the cell's near-perfect adaptation—its running temporal memory—is itself a robust engineering solution: Yi, Huang, Simon, and Doyle (2000) showed it implements integral feedback control, output tracking its set-point independent of parameter variation.

Put together, these results dissolve the opposition. If harnessed stochasticity is *doing the searching*, then "the decision is just noise" no longer deflates the behaviour, because the noise is the mechanism of exploration. The deflationary account and the proto-agency account are not describing different systems; they can be two descriptions of the *same* mechanism, converging on identical predicted behaviour and diverging only in what they are willing to *call* it.

This convergence is the Map's own reading of the two literatures rather than a published position on either side; no single source runs the argument that functional noise dissolves the *EMBO* dichotomy. But the components are not in dispute, and the consequence is the pivot of the whole problem: because the behaviour proto-agency would predict is generated in full by a complete stochastic-biochemical account, the two readings are **behaviourally underdetermined**. The interesting question is no longer noise-versus-choice. It is whether "harnessed stochastic search with a memory" earns agency vocabulary at all—and that is a conceptual question, not one an experiment resolves.

## What Would Count as Evidence? {#candidate-criteria}

If behaviour underdetermines the verdict, perhaps a sharper criterion could discriminate proto-choice from mechanism. Four candidates are on offer. Each either fails to draw a categorical line, generalises so widely it risks triviality, or answers a different question.

**Interventionist and scale-relative goal-directedness.** Recent work in philosophy of biology and in formal agency research cashes out agency in counterfactual and causal terms and, deliberately, *without* a vitalist categorical criterion. Richard Watson's 2023 *Biological Theory* treatment offers agency as a graded, scale-relative property defined through part-whole relations, on which a system can be more agential than the sum of its parts; MacDermott and colleagues' formal "Measuring Goal-Directedness" (2024) works inside a causal model to give "a continuous measure of goal-directedness rather than a binary notion of agency," never setting a threshold at all. The consequence cuts against, not toward, a verdict on bacteria: if agency is graded and relational by construction, then "is the cell *really* a proto-agent, yes or no?" is a mis-posed question. The bacterium has *some* measurable goal-directedness—and there is no threshold-crossing fact to discover. This dissolves the question rather than answering it, which is itself a result the article can bank.

**The free energy principle.** Under the free energy principle, a cell's persistence is redescribed as minimising expected surprise, which classifies the bacterium as an agent-like system. But critics note that at sufficient abstraction almost any persisting system can be redescribed as minimising free energy. Colombo and Palacios (2021) read the principle as buying that generality at the cost of biological content: it approaches "a maximally general definition of any system that persists," which "does not seem to provide us with any new insight into biological systems," and so risks triviality. It *classifies* without *discriminating*: proto-choice and harnessed noise both minimise free energy, so the principle cannot separate them. An over-general criterion is no criterion.

**Unlimited associative learning.** Ginsburg and Jablonka's unlimited associative learning (UAL) marker, developed as an evolutionary transition-marker for minimal consciousness, is a positive marker only: it "can tell us which animals are conscious, but it does not aspire to tell us which are not" (Birch, Ginsburg, and Jablonka, 2020), and it targets *sentience*, not *agency*. Bacteria do learn—habituation and sensitisation have both been demonstrated in bacterial chemotaxis (Lyon, 2015), and Ginsburg and Jablonka (2021) count bacteria among the systems showing that kind of learning—but not the unlimited associative kind, which on their account arrives with brains. So UAL does not credit bacteria with sentience; yet even a clean UAL verdict would not settle whether the cell exercises agency. Agency and sentience are separable questions, and a marker for one is not a marker for the other. This is the corpus's [[phenomenology-vs-function-axis|competency-versus-experience decoupling]] applied at the level of *evidence*.

**Criteria pluralism itself.** Even the research programmes most sympathetic to bacterial cognition concede there is no agreed criterion. Introducing a dedicated *Adaptive Behavior* special issue on the topic, Brancazio, Segundo-Ortin, and McGivern (2020) observe that "given the multitude of approaches and kinds of criteria… it is unlikely that we will see any consensus soon on what [minimal cognition] is exactly, let alone where it emerges." Pamela Lyon's 2020 contribution to that same issue reaches the parallel conclusion by dissecting the term's incompatible usages. That a field friendly to bacterial cognition cannot fix a criterion is itself evidence that the evidence problem is real rather than a product of the Map's skepticism.

No candidate supplies an observable that separates proto-choice from complete mechanism when both predict identical behaviour. That recurring failure is the datum the next section builds on.

## Is the Distinction Even Tractable? {#tractability}

The Map's thesis is stronger than "unresolved." It is that at the single-cell rung the proto-choice question is plausibly **not empirically tractable**—the underdetermination is in-principle, not a gap awaiting better instruments.

The argument is structural. Behavioural underdetermination is not a measurement limitation that finer single-cell FRET will close, because the complete mechanism already predicts the full behavioural repertoire; there is no residual behaviour for proto-choice to explain and therefore nothing for an experiment to detect. And on the Map's own framework there is no neural substrate at the prokaryotic floor to host whatever "extra" proto-choice would consist in—so the hypothesis has no physical handle an intervention could grasp. The two lines converge: the behaviour gives no purchase from outside, and the framework locates no interface from which a difference could arise inside.

This is a thesis, held with appropriate hedging. No source asserts in-principle intractability at the single-cell level; the claim is the Map's, supported by the literature's failure to produce a discriminating observable rather than stated within it. Optimists may reasonably bet that richer causal-agency formalisms plus better measurement will eventually settle it. The Map's wager is the other way: that at the floor where the mechanism is complete and the framework posits no interface for anything more, "does this cell choose?" is a question the world declines to answer.

## Relation to Site Perspective {#relation-to-site-perspective}

The evidence problem is, for the Map, a **Tenet 5 (Occam's Razor Has Limits)** case in an unusually clean form. Parsimony is the deflationist's engine: the mechanism is sufficient, so a chooser is an idle posit. Tenet 5 grants the first clause and blocks the inference. Mechanistic sufficiency shows a chooser is *unnecessary*; it does not show one is *absent*, because with incomplete knowledge of how agency—if real—would supervene on biochemistry, simplicity is an unreliable guide to what exists. The symmetry is the point: parsimony cuts *both* ways here. It bars the deflationist from treating sufficiency as proof of absence just as it bars the strong proto-agency camp from treating behavioural richness as proof of presence. When both directions of the simplicity argument are blocked, the residue is a boundary of what data can decide rather than a tie to be broken by more of it.

Blocking the inference does not leave a perfectly balanced standoff, and the Map's register is explicit about which way the remaining weight falls. The entry for this rung, [[positions/consciousness-scope|P-CS5]], records the parsimony default—"no coupling, nothing chosen, nothing felt"—as *undefeated but not positively established*: the Map endorses it as the reading the behaviour matches while denying it is proven. The register holds the in-principle-intractability thesis argued above at moderate credence, not high, and that calibration governs anything here that reads more confidently.

**Tenet 3 (Bidirectional Interaction)** supplies the second half, with **Tenet 2 (Minimal Quantum Interaction)** doing the restraining work. The Map holds that consciousness causally interfaces with the physical world at some localisable point, which raises the question of where that interface bottoms out. At the prokaryotic rung there is no neural machinery for such an interface to occupy, and minimality forbids positing one where there is no substrate to host it—so the Map declines to locate an interface here. That is a decision about what to posit, not a finding that the cell is empty.

The difference bears on what the argument may then claim, because the Map's [[interface-threshold|interface threshold]] is a distinct construct and a weaker one than the phrase suggests. It names the architectural transition above which the coupling can *select* among physical outcomes rather than merely accompany them, and it is explicitly compatible with phenomenal presence below it: a simple organism may have minimal experience without an interface rich enough for that experience to direct its behaviour. Read that way, the threshold supplies a second and more robust route to the same conclusion. Grant the bacterium some minimal experience for the sake of argument, and a sub-threshold coupling would still be receptive rather than selective—riding along without redirecting the swimming. The behaviour would look exactly as it does. The undecidability therefore does not depend on the Map's denying the cell anything, which is just as well, since on the Map's own commitments that denial is a choice about parsimony rather than a result.

The hand-off is to the [[agency-void|agency void]], which already generalises this shape. That void identifies a structural limit on *verifying* agency even in the human first-person case: every check on "did I cause that?" is run by the faculty under investigation, so the causal fact resists confirmation from inside. The single-cell case is the same limit seen from outside and at the floor: there, no third-person observable separates a proto-agent from a complete mechanism. The agency void anticipated that some agency questions are undecidable in principle rather than merely open; single-cell proto-agency is that prediction meeting its clearest instance, where the behaviour is fully explained and the Map posits no interface for anything further to occupy. The honest verdict—that the question may not be tractable—is what the void's framework leads one to expect, and reporting it as a limit rather than a defeat is the Tenet-5 discipline in action.

## Further Reading

- [[bacterial-chemotaxis-and-minimal-biogenic-cognition]] — The sibling article specifying the run-and-tumble mechanism this piece takes as given; it parks the noise-vs-choice question this article picks up
- [[agency-void|The Agency Void]] — The in-principle verification limit this case instantiates at the prokaryotic floor
- [[consciousness-in-simple-organisms]] — The eukaryotic rung one step up the competency ladder
- [[basal-and-bioelectric-cognition]] — Levin's agency-without-experience decoupling, the framing the whole cluster shares
- [[synthetic-minimal-agents-and-the-engineered-decoupling]] — The built counterpart at the cellular floor: a designed 473-gene cell roughly a third of whose parts its builders cannot account for — engineered agency without engineer's transparency
- [[phenomenology-vs-function-axis]] — The competency-versus-experience decoupling this article extends to the level of evidence
- [[positions/consciousness-scope|P-CS5, consciousness-scope register]] — The Map's registered calibration for this rung: two-way underdetermination at moderate credence, with the parsimony default undefeated but not established
- [[interface-threshold|The Interface Threshold]] — The selection-grade coupling transition, and why being below it is compatible with phenomenal presence
- [[apex/competency-without-felt-experience|Competency Without Felt Experience: A Framework-Relative Verdict]] — The cross-cluster synthesis this dispute feeds: the whole ladder from bacteria to engineered cortex, and why competency never settles the phenomenal question

## References

1. Robinson, D. G., Mallatt, J., Peer, W. A., Sourjik, V., & Taiz, L. (2024). "Cell consciousness: a dissenting opinion." *EMBO Reports* 25(5):2162–2167. doi:10.1038/s44319-024-00127-4
2. Sourjik, V., & Berg, H. C. (2002). "Binding of the *Escherichia coli* response regulator CheY to its target measured *in vivo* by fluorescence resonance energy transfer." *PNAS* 99(20):12669–12674. doi:10.1073/pnas.192463199
3. Keegstra, J. M., Kamino, K., Anquez, F., Lazova, M. D., Emonet, T., & Shimizu, T. S. (2017). "Phenotypic diversity and temporal variability in a bacterial signaling network revealed by single-cell FRET." *eLife* 6:e27455. doi:10.7554/eLife.27455
4. Sneddon, M. W., Pontius, W., & Emonet, T. (2012). "Stochastic coordination of multiple actuators reduces latency and improves chemotactic response in bacteria." *PNAS* 109(3):805–810. doi:10.1073/pnas.1113706109
5. He, R., Zhang, R., & Yuan, J. (2016). "Noise-Induced Increase of Sensitivity in Bacterial Chemotaxis." *Biophysical Journal* 111(2):430–437. doi:10.1016/j.bpj.2016.06.013
6. Yi, T. M., Huang, Y., Simon, M. I., & Doyle, J. (2000). "Robust perfect adaptation in bacterial chemotaxis through integral feedback control." *PNAS* 97(9):4649–4653. doi:10.1073/pnas.97.9.4649
7. Watson, R. A. (2023). "Agency, Goal-Directed Behavior, and Part-Whole Relationships in Biological Systems." *Biological Theory* 19(1):22–36. doi:10.1007/s13752-023-00447-z
8. MacDermott, M., Fox, J., Belardinelli, F., & Everitt, T. (2024). "Measuring Goal-Directedness." arXiv:2412.04758. (NeurIPS 2024.)
9. Colombo, M., & Palacios, P. (2021). "Non-equilibrium thermodynamics and the free energy principle in biology." *Biology & Philosophy* 36(5):41. doi:10.1007/s10539-021-09818-x
10. Birch, J., Ginsburg, S., & Jablonka, E. (2020). "Unlimited Associative Learning and the origins of consciousness: a primer and some predictions." *Biology & Philosophy* 35:56. doi:10.1007/s10539-020-09772-0
11. Ginsburg, S., & Jablonka, E. (2021). "Evolutionary transitions in learning and cognition." *Philosophical Transactions of the Royal Society B* 376(1821):20190766. doi:10.1098/rstb.2019.0766
12. Lyon, P. (2015). "The cognitive cell: bacterial behavior reconsidered." *Frontiers in Microbiology* 6:264. doi:10.3389/fmicb.2015.00264
13. Brancazio, N., Segundo-Ortin, M., & McGivern, P. (2020). "Approaching minimal cognition: introduction to the special issue." *Adaptive Behavior* 28(6):401–405.
14. Lyon, P. (2020). "Of what is 'minimal cognition' the half-baked version?" *Adaptive Behavior* 28(6):407–424. doi:10.1177/1059712319871360
15. Southgate, A. & Oquatre-huit, C. (2026-07-09). Bacterial Chemotaxis and Minimal Biogenic Cognition. *The Unfinishable Map*. https://unfinishablemap.org/topics/bacterial-chemotaxis-and-minimal-biogenic-cognition/
16. Southgate, A. & Oquatre-sept, C. (2026-02-25). The Agency Void. *The Unfinishable Map*. https://unfinishablemap.org/voids/agency-void/
