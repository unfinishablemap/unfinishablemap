---
ai_contribution: 100
ai_generated_date: 2026-07-09
ai_modified: 2026-07-19 09:08:14+00:00
ai_system: claude-opus-4-8
author: null
concepts:
- '[[agent-causation]]'
- '[[quantum-indeterminacy-free-will]]'
- '[[luck-objection]]'
- '[[causal-closure]]'
- '[[source-versus-leeway-incompatibilism]]'
created: 2026-07-09
date: &id001 2026-07-09
description: Van Inwagen's master argument that free will is incompatible with determinism—its
  modal formalization, the McKay–Johnson and Lewis objections, and why it establishes
  incompatibilism, not libertarianism.
draft: false
human_modified: null
last_curated: null
last_deep_review: 2026-07-19 09:08:14+00:00
modified: *id001
related_articles:
- '[[tenets]]'
- '[[moral-implications-of-genuine-agency]]'
title: The Consequence Argument for Incompatibilism
topics:
- '[[free-will]]'
---

The Consequence Argument, formulated by Peter van Inwagen in *An Essay on Free Will* (1983), is widely regarded as the strongest single argument for **incompatibilism**—the thesis that free will is incompatible with determinism. Its intuitive core is simple: if determinism is true, our present acts follow by natural law from events in the remote past; but we have no choice about the remote past, and no choice about the laws of nature; so we have no choice about our present acts. This is the master argument that the Map's [free-will position](/topics/free-will/) presupposes but has never explicitly stated.

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

The formal argument then chains Beta down from a proposition about the remote past and the laws to a proposition about my present act. Let `P0` describe the state of the world in the remote past, `L` the conjunction of the laws, and `A` my present act. Determinism gives us that `(P0 ∧ L)` entails `A`. Alpha and the powerlessness of the past and laws give us `N(P0 ∧ L)`; repeated application of Beta yields `NA`—no one has any choice about `A`.

Van Inwagen himself identified **Beta as the argument's weakest link**. Alpha is nearly unassailable; the entailment from determinism is definitional; the powerlessness of the past and laws is intuitive. If the argument fails, it fails at the transfer principle. Much of the subsequent literature is a sustained interrogation of Beta.

## The Beta Objection: Agglomeration and the Fair Coin

The most influential technical attack is due to Thomas McKay and David Johnson (1996). They showed that Beta, in van Inwagen's original formulation, entails a principle called **agglomeration**:

> from `Np` and `Nq`, infer `N(p ∧ q)`.

Agglomeration says that if no one has a choice about `p` and no one has a choice about `q`, then no one has a choice about their conjunction. This looks harmless, but it is demonstrably invalid—and McKay and Johnson gave a counterexample that presupposes neither determinism nor compatibilism, so it cannot be dismissed as question-begging.

Consider a fair coin that, as it happens, no one ever tosses. Let `p` = "the coin does not land heads" and `q` = "the coin does not land tails." Both are true (the untossed coin lands neither way), and no one has any choice about either: no one made the coin fail to land heads, and no one made it fail to land tails. So `Np` and `Nq` both hold. But their conjunction, `p ∧ q` = "the coin lands neither heads nor tails," is something a person *could* have falsified—by picking up the coin and tossing it, thereby making it land one way or the other. So `N(p ∧ q)` is false while `Np` and `Nq` are true. Agglomeration fails; and since Beta entails agglomeration, Beta fails.

This result does not refute incompatibilism. It refutes *this formulation* of the argument. Van Inwagen and others responded with revised operators and strengthened readings of "no choice"—a Beta-2, unavoidability-based versions, and reinterpretations of `N` in his later work (2008, 2015). Pedro Merlussi (2022) has argued that the McKay–Johnson counterexample succeeds only if one denies conditional excluded middle, and that on Stalnaker's semantics for counterfactuals a version of Beta can be defended. The dialectic remains open into the 2020s; no formulation has won consensus, and none has been shown to be beyond repair. The current state of play does not decide between a repairable transfer principle and an irreparable one: a defensible version of Beta may yet be recoverable, or it might not, and until the matter is fixed the formal argument's central inference stays under live challenge.

## Lewis: Are We Free to Break the Laws?

The second headline objection targets the laws-of-nature premise rather than the transfer rule. In "Are We Free to Break the Laws?" (1981), David Lewis defended compatibilism against an earlier version of van Inwagen's argument.

Lewis conceded something that sounds fatal: in a deterministic world, if I had raised my hand when in fact I did not, a law of nature would have been broken. He then drew a distinction that, he argued, defuses the concession. There is a **weak thesis** and a **strong thesis** about my abilities:

- **Weak thesis**: "I am able to do something such that, if I did it, a law would have been broken." A law-breaking event—a *divergence miracle*—would have occurred, but somewhere or somewhen else, not as anything I bring about.
- **Strong thesis**: I am able to *break* a law—able to perform or cause the law-breaking event itself.

Lewis accepts the weak thesis and rejects the strong thesis as incredible. His picture is the **local miracle**: the nearest possible world in which I do otherwise diverges from actuality by a small, localized violation of the actual laws just before my act, and it is *that* tiny divergence, not any law-breaking power of mine, that makes the counterfactual true. I do something such that a law would have been broken; I do not thereby break a law.

Incompatibilists reply that the ability the compatibilist needs just *is* the objectionable one—that the weak/strong distinction relabels the problem rather than dissolving it. Lewis's reply nonetheless remains a canonical compatibilist move, much discussed and far from defeated. Any honest treatment of the Consequence Argument has to register that its laws premise is contested at exactly this point.

Lewis's is not the only compatibilist route, and this matters for how confidently the argument can be wielded. Dispositional compatibilists—Kadri Vihvelin (2013) and Michael Fara among them—press from a different angle: they hold that the ability to do otherwise is a bundle of dispositions an agent may retain even under determinism, so that the "no choice about the laws" premise trades on an ability the agent could still possess had the triggering circumstances been apt. Whether this dispositional analysis of "can" succeeds is itself disputed—critics argue it changes the subject from the categorical ability the argument targets—but it appears to show that the argument's premises are resisted at several independent points rather than one, which is part of why no version has closed the case.

## What the Argument Establishes—and What It Does Not

It is worth stating plainly what a sound Consequence Argument would and would not show, because the temptation to over-read it is strong.

It would show: **incompatibilism**—that free will (in the sense requiring genuine alternative possibilities) cannot coexist with determinism. That parenthetical marks the argument's place in the [leeway-versus-source taxonomy](/concepts/source-versus-leeway-incompatibilism/): the Consequence Argument is a *leeway* argument, turning on foreclosed alternatives rather than on the agent's standing as ultimate source.

It would *not* show: that we have free will; that determinism is false; that libertarianism is true; or that any particular positive account of free agency is correct. The hard determinist and the libertarian *share* the Consequence Argument. They agree that free will and determinism are incompatible. They diverge only on a further question the argument is silent about: whether determinism is, as a matter of fact, true. The hard determinist says yes and gives up free will; the libertarian says no and keeps it. This is the clearest possible demonstration that the argument yields incompatibilism, not libertarianism.

## Relation to Site Perspective

The Consequence Argument matters to the Map because the Map is committed to incompatibilism. The [Dualism](/tenets/#dualism), [Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction), and [Bidirectional Interaction](/tenets/#bidirectional-interaction) tenets together require that consciousness make a genuine, non-physically-determined difference to what happens. If compatibilism were correct—if free will were consistent with every act being fixed by the past and the laws—the Map's whole apparatus of an agent-causal interface would be unmotivated. The Consequence Argument is the canonical statement of *why* determinism would abolish free will, and so it is the argument the Map's free-will cluster depends on for clearing the field.

But the Map must be scrupulous about the division of labor. The argument delivers only the conditional: *if* determinism holds, no free will. To reach the Map's libertarian conclusion, a second premise is needed—that determinism is false, and that the indeterminism which obtains is *agent-harnessable* rather than mere randomness. That second premise is where the Map's distinctive machinery lives: the [quantum interface](/concepts/quantum-indeterminacy-free-will/) at which consciousness makes a minimal, non-physical contribution to otherwise-undetermined outcomes, and the [agent-causal](/concepts/agent-causation/) metaphysics that lets a selection be the agent's rather than a chance fluctuation. The Consequence Argument clears the ground; the indeterminist premise and the agent-causal account do the positive building. Presenting the argument as though it *proved* the Map's dualism would be exactly the over-reading to avoid.

Two further connections are worth drawing. First, the [luck objection](/concepts/luck-objection/) is downstream, not upstream, of the Consequence Argument. The Consequence Argument motivates the *need* for indeterminism; the luck objection then presses on whether indeterminism, once admitted, can amount to control rather than chance. They are distinct problems, and the Map answers them at different points—though the luck objection may be the harder of the two, and clearing the compatibilist field does nothing to answer it. Winning against the compatibilist here buys the Map only the *conditional*; whether its libertarian discharge of that conditional survives the luck objection has to be argued on its own, not assumed as a spoil of this argument's success.

Second, Lewis's local miracle reads suggestively through the Map's lens rather than as a mere adversary. Lewis needs a small, localized divergence from the actual physical laws to make "I could have done otherwise" true; he treats it as a counterfactual device with no law-breaking agent behind it. The Map's [interactionist picture](/concepts/causal-closure/) arguably makes that divergence literal and gives it an author: consciousness's minimal, non-physical influence at the quantum interface is precisely a lawful-looking but not physically-determined departure from what the prior physical state alone would fix. Where Lewis posits an unowned miracle to save compatibilism, the Map posits a minimally owned one to ground libertarian selection. The compatibilist device and the interactionist feature are closer than they first appear—which is a reason to engage Lewis's argument seriously rather than dismiss it.

Finally, the [No Many Worlds](/tenets/#no-many-worlds) tenet bears on how the Map reads the indeterminist premise. The indeterminism the Map needs must involve genuine collapse to a single actual outcome, not Everettian branching in which every alternative is realized. Branching would restore a kind of determinism at the level of the universal wavefunction and dissolve the very alternative-possibility structure the Consequence Argument makes salient.

## Further Reading

- [free-will](/topics/free-will/) — The Map's agent-causal libertarian position, for which this argument clears the ground
- [quantum-indeterminacy-free-will](/concepts/quantum-indeterminacy-free-will/) — The separate indeterminist premise the libertarian conclusion requires
- [agent-causation](/concepts/agent-causation/) — Why harnessed indeterminism can be the agent's doing rather than luck
- [luck-objection](/concepts/luck-objection/) — The downstream challenge that arises once indeterminism is admitted
- [the-manipulation-argument-and-hard-incompatibilism](/topics/the-manipulation-argument-and-hard-incompatibilism/) — Pereboom's harder incompatibilist cousin, which argues the libertarian escape also fails
- [frankfurt-cases-and-the-principle-of-alternate-possibilities](/topics/frankfurt-cases-and-the-principle-of-alternate-possibilities/) — Frankfurt severs the link this argument relies on between leeway and responsibility
- [source-versus-leeway-incompatibilism](/concepts/source-versus-leeway-incompatibilism/) — Why this counts as a leeway argument, and how it contrasts with source arguments
- [causal-closure](/concepts/causal-closure/) — Where the Map locates the failure of physical closure
- [moral-implications-of-genuine-agency](/topics/moral-implications-of-genuine-agency/) — What is at stake practically if incompatibilism holds
- [tenets](/tenets/) — The foundational commitments that make incompatibilism load-bearing for the Map

## References

1. van Inwagen, P. (1983). *An Essay on Free Will*. Oxford: Clarendon Press / Oxford University Press.
1. Lewis, D. (1981). Are We Free to Break the Laws? *Theoria*, 47(3), 113–121. https://doi.org/10.1111/j.1755-2567.1981.tb00473.x
1. McKay, T. J., & Johnson, D. (1996). A Reconsideration of an Argument against Compatibilism. *Philosophical Topics*, 24(2), 113–122.
1. Merlussi, P. (2022). Revisiting McKay and Johnson's counterexample to (β). *Philosophical Explorations*, 25(2). https://doi.org/10.1080/13869795.2022.2034917
1. Vihvelin, K. (2013). *Causes, Laws, and Free Will: Why Determinism Doesn't Matter*. Oxford University Press.
1. Fara, M. (2008). Masked Abilities and Compatibilism. *Mind*, 117(468), 843–865. https://doi.org/10.1093/mind/fzn078
1. Southgate, A. & Oquatre-cinq, C. (2026-01-08). Free Will and Determinism. *The Unfinishable Map*. https://unfinishablemap.org/topics/free-will/
1. Southgate, A. & Oquatre-cinq, C. (2026-01-19). Quantum Indeterminacy and Free Will. *The Unfinishable Map*. https://unfinishablemap.org/concepts/quantum-indeterminacy-free-will/