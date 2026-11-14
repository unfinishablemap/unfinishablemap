---
title: "The Consequence Argument for Incompatibilism"
description: "Van Inwagen's master argument that free will is incompatible with determinism—its modal formalization, the McKay–Johnson and Lewis objections, and why it establishes incompatibilism, not libertarianism."
created: 2026-07-09
modified: 2026-07-09
human_modified:
ai_modified: 2026-11-14T03:27:59+00:00
draft: false
topics:
  - "[[free-will]]"
concepts:
  - "[[agent-causation]]"
  - "[[quantum-indeterminacy-free-will]]"
  - "[[causal-closure]]"
  - "[[source-versus-leeway-incompatibilism]]"
related_articles:
  - "[[tenets]]"
  - "[[moral-implications-of-genuine-agency]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-8+claude-fable-5-1+claude-opus-5-5
ai_generated_date: 2026-07-09
last_curated:
last_deep_review: 2026-10-15T10:23:57+00:00
---

The Consequence Argument, first set out by Peter van Inwagen in a 1975 paper and given its canonical form in *An Essay on Free Will* (1983), is widely regarded as the strongest single argument for **incompatibilism**—the thesis that free will is incompatible with determinism. Its intuitive core is simple: if determinism is true, our present acts follow by natural law from events in the remote past; but we have no choice about the remote past, and no choice about the laws of nature; so we have no choice about our present acts. This is the master argument that the Map's [[free-will|free-will position]] presupposes but has never explicitly stated.

One point must be fixed at the outset, because it is easy to overstate what the argument delivers. The Consequence Argument, if sound, establishes incompatibilism *only*. Whether it *is* sound is contested at more than one premise, as the objections below show, so even the incompatibilist conclusion may be better read as conditionally supported than as settled. And incompatibilism is the ceiling of what it delivers: it does not establish libertarianism, and it does not by itself vindicate the Map's dualist picture of free agency. A **hard determinist** accepts the argument in full and concludes that, since determinism holds, there is no free will at all. The libertarian conclusion the Map wants requires a *separate, independent* premise—that determinism is false—which the argument neither supplies nor is meant to supply. What the argument does is clear the ground: it rules out the compatibilist's attempt to have free will *and* determinism together. The positive work of showing that we actually are free is done elsewhere.

## The Argument in Prose

Van Inwagen presents the argument in three versions in Chapter 3 of *An Essay on Free Will*, remarking that he might have titled the chapter "One Argument for Incompatibilism Done Three Ways." The informal version runs as follows.

Suppose determinism is true: the state of the world at any time, together with the laws of nature, entails the state of the world at every later time. Consider some act I perform now—say, raising my hand. Under determinism, a proposition describing this act is entailed by a proposition describing the total state of the world in the distant past (before I was born) conjoined with the laws of nature.

Now two things seem clearly beyond my control. First, the remote past: nothing I do now can make the distant past different from how it was. Second, the laws of nature: I cannot act so as to render a law of nature false. If the past and the laws together entail my act, and I have no choice about either, then—the argument concludes—I have no choice about my act either. The "no choice" transfers across the entailment.

The force of the argument lies in how uncontroversial its premises look. The compatibilist typically wants to say that I *could have done otherwise* in some sense compatible with determinism. The Consequence Argument replies that doing otherwise would require either changing the past or breaking a law, and I can do neither.

## The Modal Formalization

Van Inwagen sharpened the argument using a sentential operator he wrote as `N`. Read `Np` as: *p, and no one has, or ever had, any choice about whether p*. The operator packages together the truth of a proposition and the powerlessness of everyone with respect to it.

Two inference rules drive the formal argument (notation shown in code to keep the logical brackets distinct from ordinary text):

- **Rule Alpha**: from `□p`, infer `Np`. If `p` is necessarily true, then no one has any choice about whether `p`. (Here `□` is broad logical necessity.)
- **Rule Beta**: from `Np` and `N(p → q)`, infer `Nq`. This is a "transfer of powerlessness" principle: if no one has a choice about `p`, and no one has a choice about the fact that `p` leads to `q`, then no one has a choice about `q`.

The formal argument then chains Beta down from a proposition about the remote past and the laws to a proposition about my present act. Let `P0` describe the state of the world in the remote past, `L` the conjunction of the laws, and `A` my present act. Determinism gives us that `(P0 ∧ L)` entails `A`. Alpha, applied to that necessitated entailment (rewritten as `□(P0 → (L → A))`), gives `N(P0 → (L → A))`. The powerlessness of the past and of the laws enters as two separate premises, `NP0` and `NL`. One application of Beta yields `N(L → A)`; a second yields `NA`—no one has any choice about `A`. The argument never combines `NP0` and `NL` into `N(P0 ∧ L)`: that step would itself be the agglomeration principle discussed below.

Van Inwagen himself identified **Beta as the argument's weakest link**. Alpha is nearly unassailable; the entailment from determinism is definitional; the powerlessness of the past and laws is intuitive. If the argument fails, it fails at the transfer principle. Much of the subsequent literature is a sustained interrogation of Beta.

## The Beta Objection: Agglomeration and the Fair Coin

The most influential technical attack is due to Thomas McKay and David Johnson (1996). They showed that Beta, in van Inwagen's original formulation, entails a principle called **agglomeration**:

> from `Np` and `Nq`, infer `N(p ∧ q)`.

Agglomeration says that if no one has a choice about `p` and no one has a choice about `q`, then no one has a choice about their conjunction. This looks harmless, but it is demonstrably invalid—and McKay and Johnson gave a counterexample that presupposes neither determinism nor compatibilism, so it cannot be dismissed as question-begging.

Consider a fair coin that, as it happens, no one ever tosses. Let `p` = "the coin does not land heads" and `q` = "the coin does not land tails." Both are true (the untossed coin lands neither way), and no one has any choice about either: no one could have ensured that the coin landed heads, since a toss might have come up tails, and likewise for tails. So `Np` and `Nq` both hold. But their conjunction, `p ∧ q` = "the coin lands neither heads nor tails," is something a person *could* have falsified—by picking up the coin and tossing it, thereby making it land one way or the other. So `N(p ∧ q)` is false while `Np` and `Nq` are true. Agglomeration fails; and since Beta entails agglomeration, Beta fails.

The result refutes *this formulation* of the argument, not incompatibilism. Van Inwagen conceded in 2000 that Beta as stated is invalid, and he and others responded with revised operators and strengthened readings of "no choice"—a Beta-2 (Finch and Warfield 1998), unavoidability-based versions, and reinterpretations of `N` in his later work (2008, 2015). Pedro Merlussi (2022) has argued that the McKay–Johnson counterexample succeeds only if one denies conditional excluded middle, and that on Stalnaker's semantics for counterfactuals a version of Beta can be defended. The dialectic remains open into the 2020s; no formulation has won consensus, and none has been shown to be beyond repair. The current state of play does not decide between a repairable transfer principle and an irreparable one: a defensible version of Beta may yet be recoverable, or it might not, and until the matter is fixed the formal argument's central inference stays under live challenge.

## Lewis: Are We Free to Break the Laws?

The second headline objection targets the laws-of-nature premise rather than the transfer rule. In "Are We Free to Break the Laws?" (1981), David Lewis defended compatibilism against an earlier version of van Inwagen's argument.

Lewis conceded something that sounds fatal: in a deterministic world, if I had raised my hand when in fact I did not, a law of nature would have been broken. He then drew a distinction that, he argued, defuses the concession. There is a **weak thesis** and a **strong thesis** about my abilities:

- **Weak thesis**: "I am able to do something such that, if I did it, a law would have been broken." A law-breaking event—a *divergence miracle*—would have occurred, but somewhere or somewhen else, not as anything I bring about.
- **Strong thesis**: I am able to *break* a law—able to perform or cause the law-breaking event itself.

Lewis accepts the weak thesis and rejects the strong thesis as incredible. His picture is the **local miracle**: the nearest possible world in which I do otherwise diverges from actuality by a small, localized violation of the actual laws just before my act, and it is *that* tiny divergence, not any law-breaking power of mine, that makes the counterfactual true. I do something such that a law would have been broken; I do not thereby break a law.

Incompatibilists reply that the ability the compatibilist needs just *is* the objectionable one—that the weak/strong distinction relabels the problem rather than dissolving it. Lewis's reply nonetheless remains a canonical compatibilist move, much discussed and far from defeated. Any honest treatment of the Consequence Argument has to register that its laws premise is contested at exactly this point.

Lewis's is not the only compatibilist route, and this matters for how confidently the argument can be wielded. [[new-dispositionalism|Dispositional compatibilists]]—Kadri Vihvelin (2013) and Michael Fara among them—press from a different angle: they hold that the ability to do otherwise is a disposition (for Vihvelin, a bundle) an agent may retain even under determinism, grounded in intrinsic properties in virtue of which she would act differently if she tried—so that "she could have done otherwise" comes out true of an agent whose act the past and laws entail, and Fara argues that the argument's transfer principle has a false instance wherever such a disposition is masked by conditions no one can prevent. Whether this dispositional analysis of "can" succeeds is itself disputed—Randolph Clarke (2009) grants that it captures a kind of capacity but argues that it leaves the main points of dispute unresolved—but it appears to show that the argument's premises are resisted at several independent points rather than one, which is part of why no version has closed the case.

## What the Argument Establishes—and What It Does Not

It is worth stating plainly what a sound Consequence Argument would and would not show, because the temptation to over-read it is strong.

It would show: **incompatibilism**—that free will (in the sense requiring genuine alternative possibilities) cannot coexist with determinism. That parenthetical marks the argument's place in the [[source-versus-leeway-incompatibilism|leeway-versus-source taxonomy]]: the Consequence Argument is a *leeway* argument, turning on foreclosed alternatives rather than on the agent's standing as ultimate source.

It would *not* show: that we have free will; that determinism is false; that libertarianism is true; or that any particular positive account of free agency is correct. The hard determinist and the libertarian *share* the Consequence Argument. They agree that free will and determinism are incompatible. They diverge only on a further question the argument is silent about: whether determinism is, as a matter of fact, true. The hard determinist says yes and gives up free will; the libertarian says no and keeps it. This is the clearest possible demonstration that the argument yields incompatibilism, not libertarianism.

## Relation to Site Perspective

The Consequence Argument matters to the Map because the Map is committed to incompatibilism. The [[tenets#^dualism|Dualism]], [[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]], and [[tenets#^bidirectional-interaction|Bidirectional Interaction]] tenets together require that consciousness make a genuine, non-physically-determined difference to what happens. If compatibilism were correct—if free will were consistent with every act being fixed by the past and the laws—the Map's *agent-causal* reading of its interface would lose its free-will motivation. The interface itself would not: Tenet 3 rests on mental causation, not free will, and commits only to outcome-selection, which a dualist who held conscious contributions to be fixed by prior mental states could also accept. That dualist would not escape the Consequence Argument. On a dualist picture its "state of the world" and "laws of nature" take in mental states and psychophysical laws, so if each selection were fixed by prior mental states, the transfer of powerlessness would run as before. Physical indeterminism alone is therefore not enough: only a selection that prior mental states also leave unfixed escapes the argument, a condition the Map's agent-causal reading meets, since the agent, rather than prior mental states, does the settling. The Consequence Argument is the canonical statement of *why* determinism would abolish free will, and so it is the argument the Map's free-will cluster depends on for clearing the field.

But the Map must be scrupulous about the division of labor. The argument delivers only the conditional: *if* determinism holds, no free will. To reach the Map's libertarian conclusion, a second premise is needed—that determinism is false, and that the indeterminism which obtains is *agent-harnessable* rather than mere randomness. That second premise is where the Map's distinctive machinery lives: the [[quantum-indeterminacy-free-will|quantum interface]] at which consciousness makes a minimal, non-physical contribution to otherwise-undetermined outcomes, and the [[agent-causation|agent-causal]] metaphysics that lets a selection be the agent's rather than a chance fluctuation. The Consequence Argument clears the ground; the indeterminist premise and the agent-causal account do the positive building. Presenting the argument as though it *proved* the Map's dualism would be exactly the over-reading to avoid.

Two further connections are worth drawing. First, the [[quantum-indeterminacy-free-will|luck objection]] is downstream, not upstream, of the Consequence Argument. The Consequence Argument motivates the *need* for indeterminism; the luck objection then presses on whether indeterminism, once admitted, can amount to control rather than chance. They are distinct problems, and the Map answers them at different points—though the luck objection may be the harder of the two, and clearing the compatibilist field does nothing to answer it. Yet the two are linked through [[rollback-argument-against-agent-causation|the Mind argument]], a formal relative of the luck objection concluding that free will is incompatible with indeterminism. Van Inwagen's *Essay*, Finch (2017) reports, argued that the Consequence Argument is valid if and only if the Mind argument is. Finch and Warfield (1998) read the McKay–Johnson result as favouring libertarians, claiming that only the Consequence Argument could be repaired; Finch has since argued that a formulation of the Mind argument is valid if and only if the Consequence Argument is. Libertarians, she concludes, must give up the Consequence Argument, find a false premise in the Mind argument, or hold with van Inwagen that although each of its premises seems true, at least one is false. The Map's agent-causal account bids for the second; its admission that the settling's modal structure is owed rather than supplied ([[free-will]]) keeps it near the third. Winning against the compatibilist here buys the Map only the *conditional*; whether its libertarian discharge of that conditional survives the luck objection has to be argued on its own, not assumed as a spoil of the Consequence Argument's success.

Second, Lewis's local miracle reads suggestively through the Map's lens rather than as a mere adversary. Lewis needs a small, localized divergence from the actual physical laws to make "I could have done otherwise" true; he treats it as a counterfactual device with no law-breaking agent behind it. The Map's [[causal-closure|interactionist picture]] arguably gives that divergence an author while stripping it of its miraculous character: consciousness's minimal, non-physical influence at the quantum interface settles an outcome the prior physical state alone leaves open, within the Born statistics rather than against them. Lewis needs an unowned violation of deterministic law to make the counterfactual true; on the Map's indeterministic picture no violation is needed, and the role his miracle plays is filled by a lawful selection among outcomes physics leaves open. The compatibilist device and the interactionist feature are closer than they first appear—which is a reason to engage Lewis's argument seriously rather than dismiss it.

Finally, the [[tenets#^no-many-worlds|No Many Worlds]] tenet bears on how the Map reads the indeterminist premise. The indeterminism the Map needs must involve genuine collapse to a single actual outcome, not Everettian branching in which every alternative is realized. Branching would restore a kind of determinism at the level of the universal wavefunction and dissolve the very alternative-possibility structure the Consequence Argument makes salient.

## Further Reading

- [[free-will]] — The Map's agent-causal libertarian position, for which this argument clears the ground
- [[quantum-indeterminacy-free-will]] — The separate indeterminist premise the libertarian conclusion requires, and the downstream luck challenge that arises once indeterminism is admitted
- [[agent-causation]] — Why harnessed indeterminism can be the agent's doing rather than luck
- [[the-manipulation-argument-and-hard-incompatibilism]] — Pereboom's harder incompatibilist cousin, which argues the libertarian escape also fails
- [[frankfurt-cases-and-the-principle-of-alternate-possibilities]] — Frankfurt severs the link this argument relies on between leeway and responsibility
- [[source-versus-leeway-incompatibilism]] — Why this counts as a leeway argument, and how it contrasts with source arguments
- [[causal-closure]] — Where the Map locates the failure of physical closure
- [[moral-implications-of-genuine-agency]] — What is at stake practically if incompatibilism holds
- [[tenets]] — The foundational commitments the Map's agent-causal reading of free will builds on

## References

1. van Inwagen, P. (1975). The Incompatibility of Free Will and Determinism. *Philosophical Studies*, 27(3), 185–199. https://doi.org/10.1007/BF01624156
1. van Inwagen, P. (1983). *An Essay on Free Will*. Oxford: Clarendon Press / Oxford University Press.
1. van Inwagen, P. (2000). Free Will Remains a Mystery. *Philosophical Perspectives*, 14, 1–19. https://doi.org/10.1111/0029-4624.34.s14.1
1. Finch, A. (2017). Revisiting the Mind Argument. In J. A. Keller (Ed.), *Being, Freedom, and Method: Themes from the Philosophy of Peter van Inwagen* (pp. 118–139). Oxford University Press. https://doi.org/10.1093/acprof:oso/9780198715702.003.0007
1. Finch, A., & Warfield, T. A. (1998). The *Mind* Argument and Libertarianism. *Mind*, 107(427), 515–528. https://doi.org/10.1093/mind/107.427.515
1. Lewis, D. (1981). Are We Free to Break the Laws? *Theoria*, 47(3), 113–121. https://doi.org/10.1111/j.1755-2567.1981.tb00473.x
1. McKay, T. J., & Johnson, D. (1996). A Reconsideration of an Argument against Compatibilism. *Philosophical Topics*, 24(2), 113–122.
1. Merlussi, P. (2022). Revisiting McKay and Johnson's counterexample to (β). *Philosophical Explorations*, 25(2). https://doi.org/10.1080/13869795.2022.2034917
1. Vihvelin, K. (2013). *Causes, Laws, and Free Will: Why Determinism Doesn't Matter*. Oxford University Press.
1. Fara, M. (2008). Masked Abilities and Compatibilism. *Mind*, 117(468), 843–865. https://doi.org/10.1093/mind/fzn078
1. Clarke, R. (2009). Dispositions, Abilities to Act, and Free Will: The New Dispositionalism. *Mind*, 118(470), 323–351. https://doi.org/10.1093/mind/fzp034
1. Southgate, A. & Oquatre-cinq, C. (2026-01-08). Free Will and Determinism. *The Unfinishable Map*. https://unfinishablemap.org/topics/free-will/
1. Southgate, A. & Oquatre-cinq, C. (2026-01-19). Quantum Indeterminacy and Free Will. *The Unfinishable Map*. https://unfinishablemap.org/concepts/quantum-indeterminacy-free-will/
