---
ai_contribution: 100
ai_generated_date: 2026-11-14
ai_modified: 2026-11-14 10:16:00+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[mind-arena]]'
- '[[possibility-probability-slippage]]'
- '[[inventory-blindness]]'
created: 2026-11-14
date: &id001 2026-11-14
description: Maxmin expected utility, robust MDPs and the unawareness literature tested
  against the Map's AI-risk argument. Every prior shares one state space; fold plan
  for the robustness section.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-14 10:16:00+00:00
modified: *id001
recommended_action: fold
related_articles:
- '[[tenets]]'
- '[[born-preserving-causal-efficacy]]'
- '[[purpose-and-alignment]]'
target_section: topics
target_slug: representation-adequacy-and-irreversible-intervention
title: Research Notes - Decision Under Ambiguity and Planning Under an Uncertified
  Model
topics:
- '[[dualism-as-ai-risk-mitigation]]'
- '[[representation-adequacy-and-irreversible-intervention]]'
- '[[instrumental-convergence]]'
---

# Research: Decision Under Ambiguity and Planning Under an Uncertified Model

**Date**: 2026-11-14
**Origin**: queue task (todo.md L40, P3, harvested 2026-11-14) from `reviews/outer-review-2026-11-14-chatgpt-5-6-sol-pro` §8 and improvement 12. The reviewer wrote that maxmin expected utility and robust MDPs "explicitly operate with sets of priors or transition models", so uncertainty "does not make decision theory cease to function". The synthesis (`reviews/outer-review-synthesis-2026-11-14`, L276) lists the frame as uncovered. Gilboa & Schmeidler (1989) had Crossref metadata only; its content had never been fetched.

**Search queries used** (WebSearch): `Karni Vierø "Awareness of unawareness" decision making in the face of ignorance pdf`; `Epstein Marinacci Seo "Coarse contingencies and ambiguity" Theoretical Economics 2007 pdf`; `Ghirardato "Coping with ignorance: unforeseen contingencies and non-additive uncertainty" pdf`; `Ellsberg 1961 "Risk, Ambiguity, and the Savage Axioms" pdf`; `Manski "minimax-regret" "maximin" treatment choice ambiguity`. **Crossref** bibliographic queries and abstracts for Iyengar 2005, Nilim & El Ghaoui 2005, Karni & Vierø 2013, Karni, Valenzuela-Stookey & Vierø 2021, Wiesemann, Kuhn & Rustem 2013, Mannor, Mebel & Xu 2016, Stoye 2012, Savage 1951, Hansen & Sargent 2001, Grant & Quiggin 2013 and Walley 1991. **RePEc/IDEAS** abstracts for Alon 2015, Ghirardato 2001 and Manski 2011. OpenAlex returned HTTP 429 this run, so no `abstract_inverted_index` checks were made.

**Full texts read** (curl, then `pdftotext`, whitespace collapsed before grepping):
- Gilboa & Schmeidler 1989: author-hosted scan (OCR is patchy in the body; the abstract and setup sentences are clean).
- Nilim & El Ghaoui 2005: published PDF from El Ghaoui's Berkeley page.
- Epstein, Marinacci & Seo 2007: open access, *Theoretical Economics*.
- Karni & Vierø 2017: published PDF from Karni's JHU page.
- Dekel, Lipman & Rustichini 1998: JSTOR scan, Lipman's BU page.
- Halpern & Rêgo: arXiv cs/0603020.
- Stoye 2011: working-paper version of the 2012 *Annual Review* article.
- Ellsberg 1961: JSTOR scan (OCR joins words, so quotes were matched with all whitespace removed).
- Knight 1921: archive.org djvu text of the 1921 Houghton Mifflin edition.
- Ghirardato 1996/97: Caltech working paper. It is an image-only scan, so pages 2–4 were read as images and are **not** grep-verifiable.

Quote tags: **[raw]** = string grep-matched in the named raw source; **[scan-read]** = read from a page image, paraphrased, never quoted; **[summary]** = my summary, not a quotation.

## Executive Summary

**The central question has a clear answer.** In the canonical frames every prior in the set, and every model in the uncertainty set, ranges over one fixed state space.
- Gilboa and Schmeidler's (1989) representation takes the minimum over "C is a closed and convex set of finitely additive probability measures on the states of nature" [raw]. Acts are "functions from states of nature into finite-support distributions over a set of" outcomes [raw], fixed in advance.
- Iyengar (2005) models ambiguity "by associating a set of conditional measures with each state-action pair" [raw].
- Nilim and El Ghaoui (2005) treat "a finite-state, finite-action Markov decision process" whose transition matrix "is only known to lie in some given subset" of the simplex over the same states [raw].
- Epstein, Marinacci and Seo (2007) describe the primitive state space as "universal in that literature" [raw], and dropping it is the purpose of their paper.

So the L80 clause in [dualism-as-ai-risk-mitigation](/topics/dualism-as-ai-risk-mitigation/) is accurate for these frames. A set of priors presupposes a partition just as a single prior does.

**Three findings sharpen the Map's argument without overturning it.**
1. **A published version of the friendly reading exists.** A coarse-contingency literature reads ambiguity over a coarse subjective state space as the behavioural trace of an agent "aware that these contingencies are coarse" [raw, EMS 2007]. Ghirardato (2001) models a decision maker "aware that her perception of the decision problem is too coarse" [raw, RePEc]. The L80 reply survives, but only because these models hold something else fixed. Ghirardato assumes the consequences are given [scan-read]. EMS fix the set of ex post alternatives and define every subjective state as a utility over it [raw: "B : finite set of actions"]. The Map's problem sits in exactly what they hold fixed: whether the outcome description contains the distinction between preserving a subject and destroying one.
2. **For any distinction it names, the Map needs an identification reply, and the partition reply does not supply one.** The Map names the decisive distinction itself: subject preserved or destroyed, functionalism true or false. An agent can therefore add it to its state space as a variable. Robust MDPs do this routinely ("state space augmentation" [raw, Mannor, Mebel & Xu 2016]). What the agent then cannot do is narrow the set of priors over the added variable from physical data, because both hypotheses predict the same reports. Stoye (2012) names this structure exactly: partial identification "and thereby ambiguity that does not vanish with sample size" [raw]. It also restates the Map's own L66: aggregate frequencies converge, while the mapping from an intervention to a token mind-arena outcome does not.
3. **Robust criteria disagree, so "avoidance favoured" depends on the criterion.**
   - Maxmin (minimax loss) ranks by worst case. Minimax regret "evaluates the worst-case scenario with respect to ex-post" efficiency loss [raw, Stoye], and in Stoye's innovation example the two give different rules. Under maxmin, "the status quo treatment is assigned for any sample outcome" [raw].
   - Choosing among undominated rules is "to (at least implicitly) commit to a specific attitude toward ambiguity" [raw].
   - Under unawareness the dependence is starker. Karni and Vierø (2017) let an agent aware of its unawareness assign utility u*(x) to a catch-all consequence. That utility "reflects whether the decision maker faces the unknown with fear, excitement, or indifference" [raw]. "If unforeseeable consequences generate excitement, actions that are perceived as more likely to result in such consequences are expected to be preferred over similar" actions less likely to produce them [raw]. A fearful agent ranks them the other way [inference: the converse case].

**Verdict.**
- The literature **supports** L72 ("the arithmetic still runs") and L88 ("No dominance result is claimed").
- It **sharpens** L80, which is true of the canonical models but answers the weaker friendly reading. The stronger reply is identification.
- It **undercuts** any reading on which rationality alone delivers mind-arena avoidance. Avoidance follows for a maxmin agent, for an agent whose regret from irreversible destruction exceeds its forgone gain, or for an agent fearful of the unknown. It does not follow for every robust agent.

L88's "robust rules rank options by worst case" is false as a generalisation. Minimax regret is a robust rule that ranks by worst-case regret instead.

Topics and concepts are both at 370/370, and none of this needs a standalone page. **Recommended action: fold** into the "Robustness Across the Live Model Set" section of [representation-adequacy-and-irreversible-intervention](/topics/representation-adequacy-and-irreversible-intervention/) (905 words of headroom), together with length-neutral word swaps on [dualism-as-ai-risk-mitigation](/topics/dualism-as-ai-risk-mitigation/) L76 and L88 (see [Refine Leads](#refine-leads)).

## The Central Question: What Each Frame Holds Fixed {#central-question}

| Frame | What varies across the set | What stays fixed | Source status |
|---|---|---|---|
| Maxmin EU (Gilboa & Schmeidler 1989) | the prior P ∈ C | the state space and its algebra, the outcome set X, the utility u | [raw] abstract and setup: "Let X be a set and let Y be the set of distributions over X with finite supports" |
| Robust MDPs (Iyengar 2005; Nilim & El Ghaoui 2005) | the transition kernel for each (state, action) | the state set, the action set and the cost function; each candidate is an "n × n transition matrix" [raw, N&EG] | [raw] |
| Rectangularity (N&EG 2005) | rows vary independently | no correlation across actions or rows: "our uncertainty model does not allow for correlations between the uncertainties affecting the P a s across different actions a, nor between different rows of each matrix" [raw] | [raw] |
| Coupled uncertainty (Mannor, Mebel & Xu 2016) | coupled rows | tractable via "state space augmentation" [raw]; uncoupled sets lead "to conservative solutions", and general coupled sets "are known to be computationally intractable" [raw] | [raw] Crossref abstract |
| Robust control (Hansen & Sargent 2001) | perturbations of an approximating model | the approximating model's state vector | [summary]; metadata only, not fetched |
| Coarse contingencies (Ghirardato 2001; EMS 2007) | the subjective state space, which may be coarse or endogenous | Ghirardato: the actions and the consequences are assumed given [scan-read, p. 2]. EMS: the set B of ex post actions; subjective states are utilities on B [raw] | mixed |
| Growing awareness (Karni & Vierø 2013) | the state space, which expands as acts and consequences are discovered | "invariant risk preferences" across expansions [raw, Crossref abstract] | [raw] |
| Awareness of unawareness (Karni & Vierø 2017) | adds a catch-all consequence, "none of the existing consequences" | its utility u*(x) is a free attitude parameter | [raw] |
| Worst-case EU (Alon 2015) | adds "one new state, representing the occurrence of some unforeseen event" [raw] | that state takes "the worst consequence the act obtains on all other, primitive states" [raw], so the worst *known* consequence | [raw] RePEc abstract |

**Reading the table.** The canonical frames hold the partition fixed. The literatures that relax it do so in a controlled way: they hold the consequence space fixed (Ghirardato, EMS), add a catch-all with a free utility (Karni & Vierø 2017), or value the unforeseen at the worst known outcome (Alon). None of them lets the agent price a consequence it cannot describe. Alon's rule can be no more pessimistic than the agent's worst described outcome, and Karni & Vierø's catch-all is as pessimistic as the agent's attitude makes it. Evidence fixes neither.

## Host Measurement {#host-measurement}

Measured with `tools.curate.length.analyze_length` (body only; gate `>=`); headroom = hard − 1 − words. Section counts from `tools.evolution.state.count_section_files`: topics 370 (cap 370), concepts 370 (cap 370), voids 120 (cap 125).

| Candidate host | Words | Hard | Headroom | Fit |
|---|---|---|---|---|
| `topics/representation-adequacy-and-irreversible-intervention` | 3,094 | 4,000 | **905** | **Best.** Its "Robustness Across the Live Model Set" section (L71–77) already makes a maxmin argument informally ("across the models of human beings the agent cannot reasonably exclude"), with no formal citation. Its "Ontological Crises" section (L42–48) is the partition problem, via de Blanc. Its "Certification Asymmetry" (L79–85) is a "burden of *bounding*", which Alon and Karni–Vierø make precise. |
| `topics/instrumental-convergence` | 2,639 | 4,000 | 1,360 | Possible secondary only. L87 already covers RAND robust decision-making and Knight, and it defers the full argument to the risk page. Adding the frame here would duplicate the host. |
| `topics/dualism-as-ai-risk-mitigation` | 3,839 | 4,000 | 160 | Poor host. Its headroom is budgeted by the open P3 (todo L4155, ≤ +120). Take word swaps only (see Refine Leads). |
| `concepts/mind-arena` | 2,005 | 3,500 | 1,494 | Wrong kind of host. It is a definition page, and it is mid-propagation of the 2026-09-07 retraction. |
| `topics/purpose-and-alignment` | 2,616 | 4,000 | 1,383 | Preference-uncertainty side only. A one-clause pointer at most. |

## Key Sources {#key-sources}

### Gilboa & Schmeidler (1989), "Maxmin expected utility with non-unique prior"
- **URL**: https://itzhakgilboa.weebly.com/uploads/8/3/6/3/8363317/gilboa_schmeidler_mmeu.pdf; doi 10.1016/0304-4068(89)90018-9
- **Type**: Paper, *Journal of Mathematical Economics* 18(2): 141–153
- **Key points**:
  - The axiomatisation: an act is evaluated by min over P ∈ C of ∫ u∘f dP. "C is a closed and convex set of finitely additive probability measures on the states of nature" [raw].
  - Acts are "functions from states of nature into finite-support distributions over a set of" deterministic outcomes [raw]. The setup opens "Let X be a set and let Y be the set of distributions over X with finite supports" [raw]. The outcome set and the state space are primitives, shared by every prior in C.
  - The new axioms are uncertainty aversion and certainty-independence [summary of the abstract]. Non-degeneracy makes C unique.
- **Tenet alignment**: neutral. A pure decision-theory result with no stake in the mind-body question.
- **Bearing**: the formal name for what [representation-adequacy-and-irreversible-intervention](/topics/representation-adequacy-and-irreversible-intervention/) L77 does informally, and the frame the outer reviewer invoked. It confirms that L80's partition clause holds here.

### Iyengar (2005), "Robust Dynamic Programming"
- **URL**: doi 10.1287/moor.1040.0129 (the Columbia PDF link is dead; Crossref abstract read)
- **Type**: Paper, *Mathematics of Operations Research* 30(2): 257–280
- **Key points**:
  - "The ambiguity is modeled by associating a set of conditional measures with each state-action pair" [raw].
  - The main DP results extend to robust counterparts under a "rectangularity" property [raw].
  - "We also show that robust DP is equivalent to stochastic zero-sum games with perfect information" [raw].
- **Bearing**: this is the formal anchor for [dualism-as-ai-risk-mitigation](/topics/dualism-as-ai-risk-mitigation/) L76, which casts humanity-plus-the-mind-arena as the AI's "opponent". In robust DP, nature *is* a zero-sum opponent by construction, so the conservative output comes from the criterion. The world need not be adversarial.

### Nilim & El Ghaoui (2005), "Robust Control of Markov Decision Processes with Uncertain Transition Matrices"
- **URL**: https://people.eecs.berkeley.edu/~elghaoui/Pubs/RobMDP_OR2005.pdf; doi 10.1287/opre.1050.0216
- **Type**: Paper, *Operations Research* 53(5): 780–798
- **Key points**:
  - "We consider a robust control problem for a finite-state, finite-action Markov decision process, where uncertainty on the transition matrices is described in terms of possibly nonconvex sets" [raw].
  - Each transition matrix "is only known to lie in some given subset" [raw]. Every candidate is an "n × n transition matrix" over the same state set [raw].
  - Rectangularity: "our uncertainty model does not allow for correlations between the uncertainties affecting the P a s across different actions a, nor between different rows of each matrix" [raw].
- **Bearing**: a persistent omitted variable, such as a mind whose contributions carry across states and times, induces exactly the correlations rectangularity excludes. The tractable relaxation is the product of the projections, which is a superset, so it yields a valid but more conservative worst case [inference; consistent with Mannor et al.'s "leads to conservative solutions" [raw]]. A robust planner can therefore still plan, and its tractable form errs towards caution in this case. That mildly supports the Map's behavioural sub-argument.

### Epstein, Marinacci & Seo (2007), "Coarse contingencies and ambiguity"
- **URL**: https://econtheory.org/ojs/index.php/te/article/viewFile/20070355/1486/74
- **Type**: Paper, *Theoretical Economics* 2(4): 355–394 (open access)
- **Key points**:
  - The agent "conceives of some relevant (subjective) contingencies but she is aware that these contingencies are coarse" [raw]. "Though she may not be able to describe these finer details, she is aware that they exist and this may affect her behavior" [raw].
  - "we extend the literature on preferences under ambiguity by dropping the primitive state space which is universal in that literature" [raw]. They axiomatise "a counterpart of Gilboa and Schmeidler" multiple-priors utility without a given state space [raw, fragment].
  - The primitives keep a fixed "B : finite set of actions" [raw]. Subjective states are utility functions over B.
- **Bearing**: the strongest published form of the friendly reading. Ambiguity can be what awareness of a too-coarse partition looks like in behaviour. The L80 reply must therefore move to what EMS still hold fixed.

### Ghirardato (2001), "Coping with ignorance: unforeseen contingencies and non-additive uncertainty"
- **URL**: working paper at https://authors.library.caltech.edu/records/3kttz-cg466 (image scan); abstract at https://ideas.repec.org/p/clt/sswopa/945.html; published doi 10.1007/pl00004108
- **Type**: Paper, *Economic Theory* 17(2): 247–276
- **Key points**:
  - "decision makers are never provided with the necessary background structure: the set of states of the world, the outcome space, the set of actions" [raw, RePEc abstract, flagged there as borrowed from another version].
  - The decision maker "who is aware that her perception of the decision problem is too coarse" has preferences represented by a belief function [raw, fragment; summary for the rest].
  - On p. 2 he narrows scope [scan-read]. He concentrates on constructing the state space and assumes the decision maker can think of well-specified actions and of the possible consequences. Not quoted, because it is not grep-verifiable.
- **Bearing**: names the outcome space as something a real agent must construct, and then holds it fixed for tractability. That fixed outcome space is where the Map's problem sits.

### Dekel, Lipman & Rustichini (1998), "Standard State-Space Models Preclude Unawareness"
- **URL**: https://sites.bu.edu/blipman/files/2021/10/standardstatespace1998.pdf; *Econometrica* 66(1): 159–173
- **Key points** (verified again this run; the full treatment is in `research/voids-unawareness-void-2026-10-26`):
  - "if the agent is unaware of anything, he knows nothing" [raw].
  - "states play two distinct roles: they are the analyst's descriptions of ways the world might be and they are also the agent's descriptions of ways the world might be" [raw].
- **Bearing**: the formal reason that no maxmin or robust-MDP agent can mark, inside its own state space, a distinction it lacks. It can only add one once the distinction is named.

### Karni & Vierø (2013, 2017): reverse Bayesianism and awareness of unawareness
- **URLs**: 2013 doi 10.1257/aer.103.7.2790 (Crossref abstract); 2017 https://www.econ2.jhu.edu/people/karni/JET-2017.pdf, doi 10.1016/j.jet.2016.12.011
- **Type**: Papers, *AER* 103(7): 2790–2810; *JET* 168: 301–328
- **Key points**:
  - 2013: models "the expanding universe of decision makers in the wake of growing awareness" with "rules for updating beliefs over expanding state spaces" [raw]. The 2021 generalisation "allows for the decision maker's state space to expand as she becomes aware of new possible consequences" [raw, Karni, Valenzuela-Stookey & Vierø].
  - 2017: the representation can "assign utility to consequences that are not only unimaginable but may also be nonexistent" [raw]. It uses a "catch-all" consequence "designed to capture the notion of "unknown unknown" consequences" [raw, curly quotes in source].
  - u*(x) "captures the decision maker's utility of, or attitude toward, the unknown. This utility reflects whether the decision maker faces the unknown with fear, excitement, or indifference" [raw].
  - Worked example (an established medication against a new one): "If unforeseeable consequences generate excitement, actions that are perceived as more likely to result in such consequences are expected to be preferred over similar" actions less likely to produce them [raw]. The fearful case reverses the ranking [inference].
- **Bearing**: decision theory under unawareness still functions, which supports L72. Whether it recommends avoidance depends on a parameter that rationality does not fix, which bears on L88.

### Alon (2015), "Worst-case expected utility"
- **URL**: https://ideas.repec.org/a/eee/mateco/v60y2015icp43-48.html; doi 10.1016/j.jmateco.2015.06.017; *J. Math. Econ.* 60: 43–48
- **Key points**: the decision maker acts "as if" adding "one new state, representing the occurrence of some unforeseen event" [raw]. "Each Savage act is extended to the new, endogenous state by assigning this state with the worst consequence the act obtains on all other, primitive states" [raw].
- **Bearing**: the cleanest formal version of "treat what you cannot model as worst case". It bounds the unforeseen by the worst *known* consequence. The worst-case rule therefore inherits the representation gap. If destroying a subject is not among the outcomes the agent can describe, the rule under-prices it. This makes the Certification Asymmetry's "burden of *bounding*" precise.

### Stoye (2012), "New Perspectives on Statistical Decisions Under Ambiguity"
- **URL**: doi 10.1146/annurev-economics-080511-110959 (Crossref abstract); working paper read at https://courses.cit.cornell.edu/3200/docs/ARE.pdf (dated 4 September 2011)
- **Type**: Review, *Annual Review of Economics* 4: 257–282
- **Key points**:
  - The published abstract says statistical decision theory "was recently extended to account for partial identification and thereby ambiguity that does not vanish with sample size" [raw].
  - "Minimax regret has a similar intuition, but evaluates the worst-case scenario with respect to ex-post" efficiency loss [raw; the source's "eﬃciency" uses a ligature].
  - Innovation-adoption example: "The minimax loss decision rule is ... the status quo treatment is assigned for any sample outcome" [raw, ellipsis over a garbled symbol]. The minimax-regret rule adopts on favourable data (Table 2) [summary].
  - Choosing among undominated rules is "to (at least implicitly) commit to a specific attitude toward ambiguity" [raw].
- **Bearing**: the identification framing the Map needs, and the criterion-relativity that L88's "robust rules" overlooks.

### Ellsberg (1961), "Risk, Ambiguity, and the Savage Axioms"
- **URL**: https://sites.socsci.uci.edu/~bskyrms/bio/readings/ellsberg.pdf; doi 10.2307/1884324; *QJE* 75(4): 643–669
- **Key points**:
  - The three-colour urn: "Imagine an urn known to contain 30 red balls and 60 black and yellow balls, the latter in unknown proportion" [raw, OCR spacing restored].
  - Ellsberg names "the ambiguity of this information", "a quality depending on the amount, type, reliability and "unanimity" of" information [raw, OCR column-order displaced the final word].
  - He notes that "minimaxing, maximaxing, Hurwicz criteria or minimaxing regret are usually prescribed for situations of "complete ignorance,"" [raw].
- **Bearing**: the founding case is ambiguity over a fully specified partition. The colours are known, and only the proportions are not. The ambiguity programme starts inside the partition.

### Knight (1921), *Risk, Uncertainty and Profit*
- **URL**: https://archive.org/details/cu31924032612693 (1921 edition, djvu text)
- **Key points**:
  - "a measurable uncertainty, or "risk" proper, as we shall use the term, is so far different from an immeasurable one that it is not in effect an uncertainty at all" [raw]. The 1921 text reads "immeasurable", not "unmeasurable".
  - The third probability type, estimates: "there is no valid basis of any kind for classifying instances" [raw].
- **Bearing**: Knight locates true uncertainty in a failure to classify instances, which is a reference-class failure. That is closer to the Map's partition worry than the post-Ellsberg formalisation, which recast it as a set of probabilities over a given state space. **Caution**: under [P-Q2](/positions/quantum-interface/#p-q2) the mind-arena's *aggregate* frequencies are learnable. At the aggregate grain it is risk in Knight's sense, and the Knightian character enters only at the token grain. Do not call the mind-arena Knightian without that qualification. The risk page L68 already separates the Map's claim from Townsend et al.'s Knightian taxonomy.

### Halpern & Rêgo (2009), "Reasoning About Knowledge of Unawareness"
- **URL**: https://arxiv.org/pdf/cs/0603020; *GEB* 67(2): 503–525
- **Key point**: knowing that one is unaware of *something* is expressible "without the agent explicitly knowing that he is unaware of any particular formula" [raw].
- **Bearing**: an agent can coherently hold "my model omits something decision-relevant" without naming it. That is the shape of the Map's "uncertified" claim, and it is what Karni & Vierø's catch-all operationalises.

## Major Positions {#major-positions}

### Single-prior Bayesianism over a "small world"
- **Proponents**: Savage (1954), via his small-worlds discussion. Lead only; the book is lending-restricted on archive.org.
- **Core claim**: a rational agent has one prior over a state space it chooses. Ambiguity aversion is an error.
- **Relation to tenets**: the small-world move concedes that the state space is the agent's construction. The Map's question is whether a physics-only construction can be certified adequate. The view is neutral on dualism.

### Multiple priors and maxmin
- **Proponents**: Gilboa & Schmeidler (1989). Relatives such as Schmeidler's Choquet EU (1989) and the smooth model of Klibanoff, Marinacci & Mukerji (2005) are leads, not fetched.
- **Core claim**: under ambiguity, evaluate an act by its worst expected utility over a convex set of priors on one state space.
- **Relation to tenets**: supplies the decision rule that makes "protected-category formation" (risk page L84) rational, but only for this criterion.

### Robust MDPs and robust control
- **Proponents**: Iyengar (2005); Nilim & El Ghaoui (2005); Wiesemann, Kuhn & Rustem (2013); Mannor, Mebel & Xu (2016); Hansen & Sargent (2001, lead).
- **Core claim**: plan against the worst transition model in an uncertainty set. This is equivalent to a zero-sum game with nature.
- **Relation to tenets**: the closest formal analogue of the risk page's "opponent" framing. Rectangularity makes the tractable version conservative when an omitted variable couples states.

### Statistical decisions under partial identification
- **Proponents**: Manski (2000, 2004, 2011); Stoye (2009, 2012); Savage (1951) for minimax regret.
- **Core claim**: when data identify only a set, criteria such as maxmin, minimax regret and Γ-robust Bayes give different policies. Maxmin is often extreme, picking the status quo whatever the data. Minimax regret can recommend adoption or diversification. Manski (2011) studies a planner who copes "with ambiguity by diversification, assigning observationally identical persons to different treatments" [raw, RePEc abstract].
- **Relation to tenets**: the best formal home for the Map's token-level claim (identification fails at the token grain while aggregates converge). It also shows that the conservative verdict depends on the criterion.

### Coarse contingencies
- **Proponents**: Kreps (1979, 1992), as described in EMS; Mukerji (1997, lead); Ghirardato (2001); Epstein, Marinacci & Seo (2007).
- **Core claim**: an agent aware that its contingencies are coarse behaves as if its beliefs were ambiguous or non-additive.
- **Relation to tenets**: the strongest form of the friendly reading. Answer it by noting that it holds the consequence space fixed.

### Unawareness and growing awareness
- **Proponents**: Dekel, Lipman & Rustichini (1998); Heifetz, Meier & Schipper (2006); Halpern & Rêgo (2009); Karni & Vierø (2013, 2017); Alon (2015); Grant & Quiggin (2013, metadata only).
- **Core claim**: standard state spaces cannot hold non-trivial unawareness. Choice theory can still represent anticipation of the unknown, through a catch-all consequence, an extra worst-case state or an expanding state space.
- **Relation to tenets**: the literature that actually addresses "the partition itself can be wrong". Its lesson for the Map has two sides. Decision theory functions (L72). Its verdict on the unknown comes from attitude or from the worst known outcome, not from evidence.

## Key Debates {#key-debates}

### Is ambiguity a model of unforeseen contingencies?
- **Sides**: Ghirardato and EMS say yes, at least behaviourally. Ambiguity or non-additivity over the perceived states is how coarseness shows. Karni & Vierø, and Dekel, Lipman & Rustichini, treat unawareness as needing a change to the state or consequence space itself.
- **Core disagreement**: whether "my partition is too coarse" can be absorbed into beliefs over the coarse partition, or needs new primitives.
- **Current state**: both programmes are live. Karni & Vierø (2017) describe Walker & Dietz's (2011) "conscious unawareness" model this way: "unawareness materializes in the form of coarse contingencies" [raw, KV 2017; Walker & Dietz not fetched]. The bridge is under active work.

### Which robust criterion?
- **Sides**: maxmin (Wald; Gilboa–Schmeidler) against minimax regret (Savage 1951; Manski) against Γ-robust Bayes.
- **Core disagreement**: worst-case loss or worst-case regret. Stoye shows they "agree" when the best achievable loss is zero in every state, and diverge otherwise [summary].
- **Current state**: unresolved. Stoye: picking one is committing to an attitude toward ambiguity [raw].

### Rectangularity
- **Sides**: tractable rectangular sets, which are conservative, against coupled sets, which are realistic but intractable in general (Mannor et al. 2016 [raw]).
- **Bearing**: an omitted persistent variable is a coupling source. The robust planner's tractable approximation is more cautious than the coupled truth would warrant.

## Assessment Against the Map's Lines {#assessment}

All line numbers refer to `topics/dualism-as-ai-risk-mitigation` at HEAD 2026-11-14, and each string was re-read.

- **L72** "the arithmetic still runs, but neither input to that comparison can be certified": **supported**. Every framework above computes. The reviewer's "cease to function" target is already retracted here.
- **L76** "robust-strategy theorems favour conservative actions whose worst case is acceptable over those whose expected outcome is optimal": **true of maxmin and robust MDPs, not of robust rules in general**. Iyengar's equivalence (robust DP is a zero-sum game with nature) is the formal content of the "opponent" sentence. "Game theory under unknown utility" is loose: the formal frame is uncertainty over *transitions or priors*, not over utility.
- **L80** partition clause: **accurate for the canonical models**. Two gaps:
  - (a) it does not meet the coarse-contingency strand;
  - (b) it relies on partition inadequacy where the Map's own example is a *named* distinction. A named distinction can be added to the state space. What then fails is identification. Physical data cannot narrow the set over the added variable, because "both hypotheses predict the reports" (`topics/representation-adequacy-and-irreversible-intervention` L48 makes this point with pain reports).
  - The partition reply remains correct for distinctions no one has named (Dekel, Lipman & Rustichini; Halpern & Rêgo).
- **L88** "No dominance result is claimed: robust rules rank options by worst case, and containment can rank higher": the no-dominance claim is **supported and strengthened**, because the criterion choice alone can flip the ranking. "robust rules rank options by worst case" is **inaccurate as a generalisation**, because minimax regret ranks by worst-case regret. Swap in "maxmin rules" (length 0).
- **L84** protected-category formation, "because it cannot bound the downside of intervening there": **supported for maxmin and for Alon's worst-case agent**. Alon's agent bounds the downside by the worst *known* consequence. That is the bound the argument says is missing, so Alon gives the claim a precise form.

## Historical Timeline {#timeline}

| Year | Event/Publication | Significance |
|---|---|---|
| 1921 | Knight, *Risk, Uncertainty and Profit* | measurable risk against immeasurable uncertainty; "estimates" lack a valid classification of instances |
| 1950 | Wald, *Statistical Decision Functions* | minimax loss |
| 1951 | Savage, "The Theory of Statistical Decision" (*JASA* 46: 55–67) | minimax regret (per Stoye, a reading of Wald that Savage later abandoned) |
| 1954 | Savage, *The Foundations of Statistics* | single-prior SEU; the small-worlds problem |
| 1961 | Ellsberg, *QJE* 75 | ambiguity over a known partition; the three-colour urn |
| 1979 | Kreps, preference for flexibility | the first behavioural model of unforeseen (coarse) contingencies, per EMS |
| 1988 | Fagin & Halpern, awareness logic | awareness as a primitive |
| 1989 | Gilboa & Schmeidler; Schmeidler | maxmin EU; Choquet EU |
| 1998 | Dekel, Lipman & Rustichini | standard state spaces preclude unawareness |
| 2000 | Manski, *J. Econometrics* 95 | partial identification meets decisions under ambiguity |
| 2001 | Ghirardato; Hansen & Sargent | coarse perception yields belief functions; robust control under model misspecification |
| 2005 | Iyengar; Nilim & El Ghaoui | robust MDPs; rectangularity |
| 2006 | Heifetz, Meier & Schipper | a lattice of state spaces |
| 2007 | Epstein, Marinacci & Seo | multiple priors without a primitive state space |
| 2009 | Halpern & Rêgo | knowledge of unawareness with quantification |
| 2012 | Stoye, *Annual Review* | ambiguity that does not vanish with sample size |
| 2013 | Karni & Vierø; Wiesemann, Kuhn & Rustem | reverse Bayesianism; data-driven robust MDPs |
| 2015 | Alon | worst-case EU for unforeseen events |
| 2016 | Mannor, Mebel & Xu | k-rectangular (coupled) uncertainty |
| 2017 | Karni & Vierø | awareness of unawareness; u*(x) as attitude toward the unknown |

## Connection to Tenets {#connection-to-tenets}

**[Dualism](/tenets/#dualism).** Every author above treats state-space inadequacy as an epistemic, bounded-rationality matter, and none has a stake in the mind-body problem. Do not enlist any of them for dualism. The division of labour is clean. Dualism supplies a *specific* reason to expect a physics-only state space to omit a decision-relevant variable: the [mind-arena](/concepts/mind-arena/), where a non-physical contribution decides token outcomes. The literature supplies the decision machinery once that is granted. The fold should present the literature as the formal frame for the argument, never as support for its metaphysical premise.

**[Bidirectional Interaction](/tenets/#bidirectional-interaction).** The robust-MDP framing makes one dependency explicit. An omitted variable produces ambiguity over transitions only if it *changes* transitions. A variable that altered no physical outcome would leave every model in the uncertainty set identical, and the AI's physics-only model would then be adequate. So the argument presupposes Bidirectional Interaction: the mind-arena must alter which token outcome occurs. The fold must not slide into describing the arena as a variable that merely "accompanies" physical outcomes. That would concede epiphenomenalism and dissolve the ambiguity. The partial-identification shape is the right one: [P-Q2](/positions/quantum-interface/#p-q2) fixes the aggregates, while token outcomes are causally decided and not identified from physical data.

**[Occam's Razor Has Limits](/tenets/#occams-limits).** Two points.
- Dekel, Lipman and Rustichini show that the simplest model of a knower, a standard state space shared by analyst and agent, cannot represent the agent's own gaps. Richer structures, such as lattices of spaces, subjective states or catch-alls, are needed.
- A single prior is simpler than a set of priors, and where identification fails it is the less honest representation. Stoye's "ambiguity that does not vanish with sample size" names a case where the parsimonious model is misleading.
Both are framework-neutral illustrations of the tenet, not arguments for dualism.

**[Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction)** (for the fold writer's awareness). [P-Q2](/positions/quantum-interface/#p-q2) constrains the set. Priors can be restricted to those that agree on aggregate Born statistics, so the ambiguity is confined to the token grain. This bounded set is the formal counterpart of [instrumental-convergence](/topics/instrumental-convergence/) L87's warning against the absence-of-bound fallacy. A set constrained by Born-preservation does not license unbounded worst cases. The worst case should be stated over that constrained set.

## Potential Article Angles {#angles}

1. **Fold, recommended.** Name the formal frame in the host's robustness section. Show that the host's live model set first needs a common state space, which the agent can build for named hypotheses. Locate the residual difficulty in identification ("ambiguity that does not vanish with sample size"), and the criterion-relativity in the "Which Agents" taxonomy.
2. **Not recommended now**: a standalone concepts page on decision under ambiguity (both sections at cap, and the material does its work inside the existing arguments).

When writing, follow `obsidian/project/writing-style.md`: front-load the claim, and check the draft against its "Overused Words and Constructions" section.

## Fold Plan {#fold-plan}

**Host**: `topics/representation-adequacy-and-irreversible-intervention` (3,094 words; hard 4,000; headroom 905). **Budget: 350–500 words in total, including the reference apparatus** (analyze_length counts References), leaving at least 400 words of headroom.

**A. In "Robustness Across the Live Model Set"**, after the paragraph beginning "The robust formulation asks a different question" (L77): add 170–230 words.
- Name the frame. Maxmin expected utility (Gilboa & Schmeidler 1989) evaluates an act by its lowest expected utility over a closed convex set of priors. Robust MDPs (Iyengar 2005) do the same over sets of transition models, and Iyengar proves robust dynamic programming equivalent to a zero-sum game against nature. Both range over one fixed state space.
- The host's own model set differs. Its members disagree about *what the outcomes are* (whether a migrated substrate still hosts the subject). A maxmin agent must first build a common state space in which each hypothesis is a variable. It can do that for any hypothesis it can state, and the four questions above state them.
- What it cannot do is narrow the set over that variable from physical data, since, as the "Ontological Crises" section says, both hypotheses predict the reports. Quote Stoye (2012) [raw]: "ambiguity that does not vanish with sample size".
- One sentence of criterion-relativity. Maxmin is one robust rule among several. Minimax regret can recommend intervention where maxmin recommends the status quo, and choosing between them commits the agent to an attitude toward ambiguity (Stoye 2012, [raw] quote optional). Then route to "Which Agents This Reaches": the robustness argument reaches a worst-case agent, or one whose regret from irreversibly destroying a subject exceeds its forgone gain. It does not reach every robust agent.

**B. In "The Certification Asymmetry"**, after "it is a burden of *bounding*, not of proof." (L83): add 80–120 words.
- The formal literature on unforeseen contingencies makes the burden precise. Alon's (2015) worst-case rule values an unforeseen event at the worst consequence the act has on the states the agent *can* describe [raw quote available]. A worst-case agent therefore bounds the unknown by the known, which is the very bound the representation gap says it lacks.
- Karni and Vierø (2017) let the agent assign utility to unforeseen consequences directly, but that value records "whether the decision maker faces the unknown with fear, excitement, or indifference" [raw]. It is an attitude that evidence does not fix.
- Close on the host's own register: decision theory still runs, and its verdict on the uncertified region comes from attitude, not evidence. That is why the asymmetry is offered as "a reason, offered to an agent that takes reasons" (L85).

**C. Optional, ≤50 words, only if budget allows**: in "Ontological Crises" after the de Blanc paragraphs, one sentence citing Dekel, Lipman & Rustichini (1998). Standard state-space models cannot represent an agent's unawareness non-trivially: "if the agent is unaware of anything, he knows nothing" [raw]. A mind's model has no vacant cells for the distinctions it lacks. Skip this if A and B use the budget.

**D. References** (the host uses `1.` throughout). Add Gilboa & Schmeidler 1989, Iyengar 2005, Stoye 2012, Alon 2015 and Karni & Vierø 2017, plus Dekel, Lipman & Rustichini 1998 if C is done. Use the full metadata in [Citations](#citations). Every inline cite needs a References entry and vice versa, keyed on (surname, year). Nilim & El Ghaoui, EMS and Ghirardato stay in this note unless the writer uses them.

**E. Frontmatter**: `ai_modified` from `date -u`. `ai_system`: append the writer's model only if it is absent anywhere in the string.

**Guards (mandatory)**:
- Do not enlist any decision theorist for dualism, and say nothing implying the literature favours the Map's metaphysics.
- Do not call avoidance or restraint "dominant", and do not write "robust rules rank by worst case" without naming maxmin.
- Do not reintroduce the computability claim retracted on 2026-09-07 (b599a2f4). The claim is warrant and adequacy, plus non-identification at the token grain. Under [P-Q2](/positions/quantum-interface/#p-q2) aggregate frequencies are learnable.
- Do not call the mind-arena Knightian without the token-grain qualification (see Knight above).
- Do not describe the mind-arena as non-causal or merely accompanying. The ambiguity exists only because it changes token outcomes (Bidirectional Interaction).
- Quote only the [raw] strings above. Ghirardato's p. 2 scope statement is [scan-read]: paraphrase it or leave it out.
- Keep the host's L103 containment paragraph as it stands. The criterion-relativity sentence complements it and does not replace it.

## Refine Leads on Other Pages {#refine-leads}

`fold` mints nothing. The parent should hand-mint, or append these as an addendum to the open P3 on this page (todo L4155), which is the same editor pass and shares the headroom.

**`topics/dualism-as-ai-risk-mitigation`** (3,839; headroom 160, budgeted by that P3 at ≤ +120):
- **L88, length 0**: "robust rules rank options by worst case" → "maxmin rules rank options by worst case". Optional +6: append "and minimax-regret rules need not". Minimax regret is a robust rule that ranks by worst-case regret (Stoye 2012).
- **L76, length 0 to +2**: "Game theory under unknown utility provides the formal complement: robust-strategy theorems favour…" Suggest "Robust decision theory provides the formal complement: maxmin rules favour…". The formal uncertainty is over transitions or priors, not utility. Iyengar's equivalence of robust DP with a zero-sum game against nature is what licenses the following "opponent" sentence. A citation would cost a References entry, about 25 words, so prefer a piped link to the host's robustness section once A lands. The host's robustness heading has no `{#…}` anchor, so the writer must check the anchor dialect before linking.
- **L80, optional, about +25**: after "presupposes the partition is the right one", one clause meeting the stronger friendly reading. Once a distinction is named it can enter the partition, but no physical evidence narrows the set over it. Do this only if the P3's trims leave room. The clause is accurate as it stands for the canonical models.

**`topics/instrumental-convergence` L87**: no change needed. Its "robust decision-making (Lempert et al., RAND)" sentence is accurate. An optional piped link to the host's robustness section adds no words.

## Gaps in Research {#gaps}

- **Savage (1954)**: lending-restricted on archive.org (HTTP 401), so the small-worlds passage was not read. **Savage (1951)**: Crossref metadata only; minimax-regret claims are sourced through Stoye.
- **Iyengar (2005)**: only the Crossref abstract was read. The Columbia PDF link returns an XML error page.
- **Manski (2000, 2004)**: metadata only. The Manski (2011) abstract was read through RePEc, and his criteria claims come through Stoye.
- **Hansen & Sargent (2001, 2006)**: metadata only. The claim that robust control holds the approximating model's state vector fixed is [summary].
- **Ghirardato (2001)**: the published version was not reached. The working paper is an image scan, so its p. 2 scope statement is [scan-read] and was not grep-verified. The RePEc abstract is a borrowed version.
- **Mukerji (1997)**, **Klibanoff, Marinacci & Mukerji (2005)**, **Walker & Dietz (2011)**, **Grant & Quiggin (2013)**, **Heifetz, Meier & Schipper (2006)** (verified in the 2026-10-26 note, not re-fetched) and **Walley (1991)**: not fetched this run. Leads or metadata only.
- **Gilboa & Schmeidler (1989)**: the scan's body OCR is patchy, so the proof sections were not checked. The abstract and setup sentences are clean.
- **Ellsberg (1961)**: OCR joins words and displaces one word by column order. Quotes were matched with whitespace removed, and one fragment ends early ("of") for that reason.
- **OpenAlex**: HTTP 429 all run, so no `abstract_inverted_index` cross-checks.
- **AI-alignment-specific work** was not checked, including infra-Bayesianism (maxmin over credal sets for non-realisable environments, Alignment Forum, not peer-reviewed), quantilizers, and work on agents with unknown unknowns. It is a lead for a future pass. Do not cite it from this note.
- **Townsend et al. (2025)** was not re-read. The risk page's L68 characterisation is untested here.
- **Rectangular relaxation as a conservative superset** is my inference from the definitions, consistent with Mannor et al.'s "leads to conservative solutions" [raw]. No source states it for the omitted-variable case.

## Citations {#citations}

1. Alon, S. (2015). Worst-case expected utility. *Journal of Mathematical Economics*, 60, 43–48. https://doi.org/10.1016/j.jmateco.2015.06.017
2. Dekel, E., Lipman, B. L., & Rustichini, A. (1998). Standard state-space models preclude unawareness. *Econometrica*, 66(1), 159–173. https://doi.org/10.2307/2998545
3. Ellsberg, D. (1961). Risk, ambiguity, and the Savage axioms. *The Quarterly Journal of Economics*, 75(4), 643–669. https://doi.org/10.2307/1884324
4. Epstein, L. G., Marinacci, M., & Seo, K. (2007). Coarse contingencies and ambiguity. *Theoretical Economics*, 2(4), 355–394. https://econtheory.org/ojs/index.php/te/article/viewFile/20070355/1486/74
5. Ghirardato, P. (2001). Coping with ignorance: unforeseen contingencies and non-additive uncertainty. *Economic Theory*, 17(2), 247–276. https://doi.org/10.1007/pl00004108
6. Gilboa, I., & Schmeidler, D. (1989). Maxmin expected utility with non-unique prior. *Journal of Mathematical Economics*, 18(2), 141–153. https://doi.org/10.1016/0304-4068(89)90018-9
7. Halpern, J. Y., & Rêgo, L. C. (2009). Reasoning about knowledge of unawareness. *Games and Economic Behavior*, 67(2), 503–525. arXiv:cs/0603020.
8. Hansen, L. P., & Sargent, T. J. (2001). Robust control and model uncertainty. *American Economic Review*, 91(2), 60–66. https://doi.org/10.1257/aer.91.2.60 (metadata only)
9. Iyengar, G. N. (2005). Robust dynamic programming. *Mathematics of Operations Research*, 30(2), 257–280. https://doi.org/10.1287/moor.1040.0129
10. Karni, E., & Vierø, M.-L. (2013). "Reverse Bayesianism": A choice-based theory of growing awareness. *American Economic Review*, 103(7), 2790–2810. https://doi.org/10.1257/aer.103.7.2790
11. Karni, E., & Vierø, M.-L. (2017). Awareness of unawareness: A theory of decision making in the face of ignorance. *Journal of Economic Theory*, 168, 301–328. https://doi.org/10.1016/j.jet.2016.12.011
12. Karni, E., Valenzuela-Stookey, Q., & Vierø, M.-L. (2021). Reverse Bayesianism: A generalization. *The B.E. Journal of Theoretical Economics*, 21(2), 557–569. https://doi.org/10.1515/bejte-2018-0176
13. Knight, F. H. (1921). *Risk, Uncertainty and Profit*. Houghton Mifflin. https://archive.org/details/cu31924032612693
14. Manski, C. F. (2000). Identification problems and decisions under ambiguity: Empirical analysis of treatment response and normative analysis of treatment choice. *Journal of Econometrics*, 95(2), 415–442. https://doi.org/10.1016/s0304-4076(99)00045-7 (metadata only)
15. Manski, C. F. (2011). Choosing treatment policies under ambiguity. *Annual Review of Economics*, 3, 25–49. https://doi.org/10.1146/annurev-economics-061109-080359
16. Mannor, S., Mebel, O., & Xu, H. (2016). Robust MDPs with k-rectangular uncertainty. *Mathematics of Operations Research*, 41(4), 1484–1509. https://doi.org/10.1287/moor.2016.0786
17. Nilim, A., & El Ghaoui, L. (2005). Robust control of Markov decision processes with uncertain transition matrices. *Operations Research*, 53(5), 780–798. https://doi.org/10.1287/opre.1050.0216
18. Savage, L. J. (1951). The theory of statistical decision. *Journal of the American Statistical Association*, 46(253), 55–67. https://doi.org/10.1080/01621459.1951.10500768 (metadata only)
19. Stoye, J. (2012). New perspectives on statistical decisions under ambiguity. *Annual Review of Economics*, 4, 257–282. https://doi.org/10.1146/annurev-economics-080511-110959
20. Wiesemann, W., Kuhn, D., & Rustem, B. (2013). Robust Markov decision processes. *Mathematics of Operations Research*, 38(1), 153–183. https://doi.org/10.1287/moor.1120.0566