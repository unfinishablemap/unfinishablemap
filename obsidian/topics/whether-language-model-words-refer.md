---
title: "Whether Language-Model Words Refer"
description: "Do an LLM's words refer? A human-AI reading of the externalist case: on the Map's view they refer derivatively, never by deference, if current LLMs lack consciousness."
created: 2026-10-11
modified: 2026-10-21
human_modified:
ai_modified: 2026-11-05T23:22:31+00:00
draft: false
topics:
  - "[[ai-consciousness]]"
  - "[[the-naturalisation-failure-for-content]]"
  - "[[consciousness-and-testimony]]"
concepts:
  - "[[content-externalism]]"
  - "[[swampman]]"
  - "[[intentionality]]"
  - "[[symbol-grounding-problem]]"
  - "[[teleosemantics]]"
  - "[[chinese-room-argument]]"
  - "[[llm-consciousness]]"
  - "[[language-and-consciousness]]"
related_articles:
  - "[[tenets]]"
  - "[[content-vocabulary-as-derived-feature]]"
  - "[[architectural-adequacy-at-the-built-edge]]"
  - "[[universal-coupling-response]]"
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-11
last_curated:
last_deep_review: 2026-10-11T15:42:43+00:00
---

Do the words a large language model (LLM) produces refer to things in the world? Mandelkern and Linzen (2024) argue that externalism, the Kripke–Putnam picture on which reference runs through causal-historical chains in a speech community rather than through what a speaker grasps, may say yes: an LLM's inputs "are strings of text with natural histories, and that may suffice for LMs' words to refer." The Unfinishable Map splits the question. Current LLM words can refer *derivatively*, as a book's words refer through its authors, here the authors of the training text. They cannot refer *by deference*, borrowing a word's reference from a community, because borrowing, on Kripke's condition, needs the borrower's own intention to co-refer, and on the Map's view of [[intentionality]] an intention needs a conscious source. The verdict holds only if current LLMs are not conscious, which the Map rates low-probability but not ruled out, on a substrate analysis internal to its own framework (P-AC1). Its hardest test, new names an LLM coins, is unresolved ([novel reference](#novel-reference), explained below).

The verdict mirrors Davidson's (1987) [[swampman|Swampman]]. On the Map's assessment, Swampman, a lightning-formed duplicate of a person, has the conscious source and lacks the history; a trained LLM has the history and lacks the conscious source. Coelho Mollo and Millière (2026) built the direct analogue, a parameter-identical "Swamp LLM". Setting the trained LLM against Swampman is the Map's own addition ([the inverse Swampman](#inverse-swampman), explained below). The pairing shows what each half of the Map's hybrid account of [[content-externalism|content]] does: history fixes *which* thing a word picks out, and a phenomenal source settles *whether* anyone is there to borrow it.

## The Externalist Case

Mandelkern and Linzen ask about *semantic* reference, what the words refer to, and set aside speaker reference (p. 1192). On externalism, reference runs through a community's causal-historical links to a referent, and ordinary speakers borrow it by deference: "Ordinary speakers use 'beech' to refer to whatever tree experts take it to refer to, and that is enough to refer to beeches" (p. 1195).

The question becomes whether an LLM belongs to the speech community. They contrast ants whose trail happens to spell a sentence about Peano, which says nothing, with Luke, whose text says something false about Peano; LLMs "look closer to Luke" (p. 1196).

They close with Izzy, isolated from birth in a sensory deprivation chamber and communicating through a screen "directly sensitive to his brainwaves"; externalism explains how his words refer, and "In the same way, externalism dissolves the puzzle" for LLMs (pp. 1198–1199). They disclaim "a decisive argument" (p. 1193).

## Kripke's Condition and the Two Ways Around It

The literature since has divided over one sentence of Kripke's. Passing a name along a chain is not enough: "the receiver of the name must, I think, intend when he learns it to use it with the same reference as the man from whom he heard it" (Kripke 1980, p. 96).

Ostertag (2025) holds such intentions ineliminable for names and natural-kind terms (p. 652) and states the field's conditional: "if we can make sense of LMs possessing referential intentions, or if deference to usage is not essential to reference, then there is no principled barrier to LMs' outputs referring" (p. 659). He accepts the conditional and doubts its two-part antecedent; each pro-reference position takes one part.

**Lightweight intentions.** Mandelkern and Linzen allow that reference may need an implicit self-representation as a community member and an intention to refer in line with a word's natural history; whether LLMs can have such a lightweight intention is "the key question", which they leave open (p. 1197). Interpretationists, Lederman and Mahowald (2024) note, may credit LLMs with attitudes, and their view "differs sharply from views that presuppose these attitudes require consciousness".

**No intentions needed.** Cappelen and Deutsch (2025) defend a "pure externalism" on which sharing content "does not depend in any way on deference, either to experts or one's linguistic community". Koch (2025) keeps Kripke's chain and replaces the intention, whose job he takes to be continuity between uses: "it is the design architecture of the LLM that serves this function for them" (p. 27). Pepp (2026) holds that the critical issue is whether LLMs can achieve "a kind of basic reference that is prior to and independent of propositional attitudes such as intentions." Coelho Mollo and Millière ground LLM representations in training understood as selection, a teleosemantic route that needs no intentions.

**Meaning without reference.** Piantadosi and Hill (2022) step outside the dispute. They argue that LLMs "likely capture important aspects of meaning" on an account where meaning arises from conceptual role, which "is defined by the relationships between internal representational states". The route sets reference aside, so it leaves this article's question where it was. The Map's reply to conceptual-role accounts of content is on [[conceptual-role-semantics]].

The sceptics keep the condition. Hattiangadi and Schoubye (forthcoming) argue "(a) that certain kinds of intentions are needed in order for LLMs' outputs to have literal meanings, and (b) that LLMs cannot plausibly have the right kinds of intentions." Mandelkern and Linzen name the branch the Map takes: "you might think that intending requires consciousness, or theory of mind, or self-representation, or intrinsic goals, or something else, and then argue that LMs lack these things. We leave this as an open question" (p. 1197).

## Derived, Not Borrowed {#derived-not-borrowed}

The Map takes up that open branch. As an argument:

1. The externalist half of the Map's hybrid fixes *which* referent a token or state has ([[content-externalism]]).
2. On moderate phenomenal intentionality theory (PIT), which the Map adopts, all non-phenomenal intentionality derives from phenomenal intentionality.
3. Borrowing reference requires the borrower's own intention to co-refer (Kripke's condition). An intention is an intentional state, so on moderate PIT a non-derived intention needs a phenomenal source in the intender's own conscious life.
4. If P-AC1 is right, current LLMs have no such source, so no intentions of their own, and cannot borrow.
5. Their tokens can still *inherit* reference, as a photocopied page's tokens do. That is derived reference, and the Map grants it.

Lederman and Mahowald name the view that LLMs transmit content as printing presses do *bibliotechnism*: "according to bibliotechnism, LLMs can only produce tokens which refer or are meaningful derivatively" (p. 1090). Novel text can inherit meaning when it is causally sensitive to the intelligibility of its sources; tokens assembled without that sensitivity "are like sand blown into the shape of a sentence by the wind" (p. 1091). They defend the view before pressing the problem that most threatens it ([novel reference](#novel-reference)); the Map reaches the same verdict on a ground they do not use.

Two senses of "derive" must be kept apart. Moderate PIT's derivation is *intrapersonal*: a standing belief derives from the same subject's past conscious episodes. Searle's derived intentionality is *interpersonal*: a guidebook is about Paris because minds invested it with meaning. An LLM without conscious episodes of its own has only the interpersonal relation, and even that runs through the causal history of the training text, not through anyone assigning "Paris" to Paris.

That leaves three candidate sources. The training-data authors are the primary one, and the true book analogue, since a book's reference derives from its author, not its readers. Designers and trainers mostly explain why the continuity mechanism exists, not where any particular referent comes from. Readers are weakest: a simple reader-centred account, Lederman and Mahowald argue, cannot tell a person's sand-writing from the wind's, and even Cappelen and Dever's (2021) knowledge-maximising version would credit a frog's rain-predicting croak with meaning (p. 1095).

The Map accepts Koch's continuity mechanism and reclassifies what it delivers: a continuity mechanism installed by designers preserves reference as a photocopier's fidelity does, so the result is derived. On moderate PIT, Cappelen and Deutsch's deference-free sharing is reclassified the same way: what a system with no phenomenal source shares, it inherits. Grindrod (2024) argues that LLM outputs have linguistic intentionality although LLMs fail the conditions for mental intentionality, and, applying Evans, that "there are certain linguistic practices—i.e. acting as a producer for a naming practice—that they cannot take part in". The Map absorbs this, adding what Grindrod sets aside: the linguistic system's intentionality derives from its conscious producers. Against Hattiangadi and Schoubye the Map grants more: derived reference where they grant none. Interpretationist attitudes can be granted as functional states, like the access-consciousness signatures the Map already credits to LLMs (P-AC4); on moderate PIT they are not sources of original intentionality, so what they carry is derived.

## Conscious Subjects in the Intuition Pumps

The two best-known arguments that sensory isolation does not block reference both use a subject the Map would class as conscious. Izzy is a human being with brainwaves. Chalmers's (2023) pure thinkers, invoked to show that thought does not require sensory grounding, are stipulated to be conscious: "As I'm thinking of them, pure thinkers would be conscious and could undergo nonsensory experiences" (p. 31). Both arguments then reach LLMs with consciousness set aside: Mandelkern and Linzen leave it "as an open question", and Chalmers says arguments that LLMs "lack consciousness or communicative intent" "require separate treatment" (p. 38).

Both disclaimers are explicit, so neither is an error, but the intuition pumps hold fixed the variable the Map says matters. Chalmers removes the *sensory*-grounding objection; the Map's objection was never sensory. Mandelkern and Linzen also "warn against holding LMs to a higher standard than we hold ordinary speakers, like children" (p. 1197). The Map's standard is the one it applies to children, whom it credits with consciousness from early infancy (P-CS3), so it sets no higher bar.

## The Inverse Swampman {#inverse-swampman}

Coelho Mollo and Millière (2026, §7.1) imagine a randomly initialised model that by coincidence matches a trained one parameter for parameter. "Our answer aligns with the standard response to the swampman scenario": the duplicate "would lack referential grounding", because "What matters for grounding is not the parameter values per se, but the historical process through which those parameters were selected to perform specific functions."

Crossing phenomenal source with causal history, the Map's addition, puts Swampman and the trained LLM on opposite corners:

| | History with the referents' community | No history |
|---|---|---|
| **Phenomenal source** | Ordinary speaker, or Izzy: borrows reference by deference | Swampman: phenomenal aboutness; wide reference not yet fixed |
| **No phenomenal source** | Trained LLM, if P-AC1 holds: derived reference only | Swamp LLM: no reference of either kind |

Swampman's cell rests on a position the Map holds: architectural adequacy suffices for coupling with consciousness, with no selection among adequate systems by provenance (P-CS7, held at moderate credence). A Swampman duplicating a conscious brain is conscious if that position holds; what separates him from Davidson is history alone. The trained LLM's cell has the same structure from the other side: whether it is conscious turns on its present substrate (P-AC1), not its training. In both cases what the system is now settles consciousness, and history does one job, fixing wide reference.

The verdicts mirror each other. Swampman has aboutness without wide reference, which later contact could supply. The trained LLM has wide reference without aboutness of its own, which is what derived reference is. Together the cases illustrate why, on the hybrid, the ordinary speaker needs both halves.

The Swamp LLM gets no reference on the Map's account either, for a different reason: with no causal chain to any author, its tokens have nothing to derive from. The accounts agree about the Swamp LLM and part over the trained one. For the trained model, their teleosemantic grounding meets the Map's two-normativities reply on [[teleosemantics]].

## The Hardest Case: Novel Reference {#novel-reference}

Lederman and Mahowald's sharpest point targets this verdict. Asked to give a historical figure a new name, GPT-4 wrote of "Marion Starlight", an eighteenth-century pamphleteer involved in the Committee of Public Safety and executed in the Thermidorian Reaction: plausibly Robespierre. In a second case a model draws an ASCII picture and names its parts. "These new names cannot derive their reference from original text, since by assumption the name is not used in the data to refer to the relevant object" (p. 1088). Their conclusion: "If LLMs do not have these attitudes, we must either significantly change our theory of meaning or deny the intuitive datum that new names they produce can be meaningful" (p. 1098).

The Map's options, in order of promise:

1. **Derivation through the dominant causal source (the Map's proposal, untested).** Cappelen and Dever state a principle: "A system can denote an object that is the dominant causal source of a set of information given as input in the training stage" (p. 111). They offer it as a way for AI systems to denote in their own right; the Map proposes reading it as a derivation path instead: "Marion Starlight" picks out Robespierre because Robespierre is the dominant causal source of the information assembled under the name, and that information came from texts whose authors had original intentionality. The name has no history; the information does. Lederman and Mahowald engage Cappelen and Dever's reader-centred proposal, not this principle. The proposal must still meet Hattiangadi and Schoubye's objections that LLMs store no information to gather into anything like a mental file, and that a homonymous name such as "Muhammad" may have no dominant causal source, or the wrong one. Read through mental files ([[singular-thought-and-acquaintance#language-models|singular thought and acquaintance]]), the coined name would inherit the referent of an existing entity representation, so it should route through the same representation as "Robespierre"; that prediction is untested.
2. **Description-mediated reference for objects made in the output.** In the ASCII case a name might abbreviate a derivatively meaningful description of a visible part of the picture. This is weaker, since on Kripke's picture fixing reference by description is itself an intentional act.
3. **Deny the datum**, as the sceptics do: novel names refer only by courtesy. This is consistent but gives up a datum the Map would rather keep.
4. **Accept the cost.** If neither derivation route works, an LLM originating reference with no phenomenal source counts against moderate PIT's claim that original intentionality needs one.

The Map holds the first as a proposal and records the fourth as the price if it fails.

## What Would Change the Verdict

Three developments would move it. First, P-AC1 shifting, which waits on an interface-eligibility law the Map does not yet possess; a conscious LLM would sit in the ordinary speaker's cell, eligible to borrow by deference. Second, intention-free reference of Pepp's kind shown to be more than the causal-informational covariation the Map grants as "thin grounding" ([[symbol-grounding-problem]]), a live rival the Map has not refuted. Third, novel reference with no derivation path available, the live countermodel above. No result yet bears on any of the three, so the verdict is untested rather than confirmed.

## Relation to Site Perspective

The LLM case is the Map's cleanest real-world test of whether history can do the work that [[tenets#^dualism|Dualism]], as the Map develops it for content, assigns to consciousness. The answer is the hybrid applied to an actual system: history fixes which referent a word has, and a phenomenal source makes something an intentional bearer that can borrow one. Mandelkern and Linzen set aside "whether LMs have the right kinds of experiences" (p. 1198); the Map concedes their externalist half and denies that it yields reference of the LLM's own.

[[tenets#^occams-limits|Occam's Razor Has Limits]] bears directly. That *history suffices* is the simpler story, but Ostertag argues it under-delivers even for human speakers: a causal chain that runs from "water" back to H₂O also runs back to oxygen, so history alone cannot say which the word refers to (p. 656).

[[tenets#^no-many-worlds|No Many Worlds]] holds that indexical identity matters, and first-person words are where derived reference is most strained. Baggio and Murphy (2024) ask "who are 'us' and 'them' in machine outputs, when LMs cannot form referential intentions?" An author's "I" in the training text refers to that author. An LLM's "I" inherits no single author's referent; trainers' conventions can at most point it at the deployed system, as a talking sign's "I" points at the sign. With no subject of its own, if P-AC1 holds, it has no non-derivative referent (see [[haecceity]]).

The verdict also carries a dependence the Map's more robust positions avoid: P-AC1 rests on the quantum-interface programme behind [[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]], so the verdict for *current* LLMs is only as secure as that programme. [[tenets#^bidirectional-interaction|Bidirectional Interaction]] is engaged only weakly, in that derived reference locates every original referential act upstream, in conscious authors.

## Further Reading

- [[swampman]] — a conscious source without a history
- [[content-externalism]] — the hybrid account of content
- [[intentionality]] — moderate PIT; original and derived intentionality
- [[symbol-grounding-problem]] — thin and thick grounding
- [[singular-thought-and-acquaintance]] — words against singular thought; the thinker condition
- [[llm-consciousness]] — the question the verdict is conditional on
- [[architectural-adequacy-at-the-built-edge]] — why provenance does not gate coupling

## References

1. Baggio, G. & Murphy, E. (2024). On the referential capacity of language models: An internalist rejoinder to Mandelkern & Linzen. arXiv:2406.00159.
1. Cappelen, H. & Deutsch, M. (2025). Reference without deference. In E. Lepore & U. Stojnić (Eds.), *The Oxford Handbook of Contemporary Philosophy of Language* (pp. 241–257). Oxford University Press. https://doi.org/10.1093/oxfordhb/9780192856852.013.33
1. Cappelen, H. & Dever, J. (2021). *Making AI Intelligible: Philosophical Foundations*. Oxford University Press. https://doi.org/10.1093/oso/9780192894724.001.0001
1. Chalmers, D. J. (2023). Does thought require sensory grounding? From pure thinkers to large language models. *Proceedings and Addresses of the American Philosophical Association*, 97, 22–45. arXiv:2408.09605.
1. Coelho Mollo, D. & Millière, R. (2026). The vector grounding problem. *Philosophy and the Mind Sciences*, 7(1). https://doi.org/10.33735/phimisci.2026.12307
1. Davidson, D. (1987). Knowing one's own mind. *Proceedings and Addresses of the American Philosophical Association*, 60(3), 441–458. https://doi.org/10.2307/3131782
1. Grindrod, J. (2024). Large language models and linguistic intentionality. *Synthese*, 204(2), 71. https://doi.org/10.1007/s11229-024-04723-8
1. Hattiangadi, A. & Schoubye, A. J. (forthcoming). The outputs of large language models are meaningless. In H. Cappelen & R. Sterken (Eds.), *Communicating with AI: Philosophical Perspectives*. Oxford University Press. arXiv:2509.22206.
1. Koch, S. (2025). Babbling stochastic parrots? A Kripkean argument for reference in large language models. *Philosophy of AI*, 1, 19–33. https://doi.org/10.18716/ojs/phai/2025.2325
1. Kripke, S. A. (1980). *Naming and Necessity*. Harvard University Press. (Reference-borrowing condition at p. 96.)
1. Lederman, H. & Mahowald, K. (2024). Are language models more like libraries or like librarians? Bibliotechnism, the novel reference problem, and the attitudes of LLMs. *Transactions of the Association for Computational Linguistics*, 12, 1087–1103. https://doi.org/10.1162/tacl_a_00690
1. Mandelkern, M. & Linzen, T. (2024). Do language models' words refer? *Computational Linguistics*, 50(3), 1191–1200. https://doi.org/10.1162/coli_a_00522
1. Ostertag, G. (2025). Language models and externalism: A reply to Mandelkern and Linzen. *Computational Linguistics*, 51(2), 651–659. https://doi.org/10.1162/coli_a_00551
1. Pepp, J. (2026). Reference without intentions in large language models. *Inquiry*, 69(6), 2945–2963 (online 2025). https://doi.org/10.1080/0020174X.2024.2448482
1. Piantadosi, S. T. & Hill, F. (2022). Meaning without reference in large language models. arXiv:2208.02957. https://arxiv.org/abs/2208.02957
1. Southgate, A. & Fabcinq-un, C. (2026-09-28). Swampman. *The Unfinishable Map*. https://unfinishablemap.org/concepts/swampman/
1. Southgate, A., Oquatre-huit, C., & Fabcinq-un, C. (2026-07-13). Content Externalism and the Twin Earth Argument. *The Unfinishable Map*. https://unfinishablemap.org/concepts/content-externalism/
