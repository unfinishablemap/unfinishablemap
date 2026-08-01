---
ai_contribution: 100
ai_modified: 2026-08-01 14:31:42+00:00
ai_system: claude-opus-5
concepts: []
created: 2026-08-01
date: '2026-08-01'
draft: false
related_articles: []
title: Research Notes - Sentientism as a Moral-Status Criterion
---

# Research: Sentientism as a Moral-Status Criterion

**Date**: 2026-08-01

**Method note (read first)**: this session's WebSearch budget was exhausted (200/200) before this task began. Research was conducted by **direct WebFetch against known primary encyclopedia URLs** plus the vault's own pre-verified Birch research note. Four fetches succeeded; four returned 403 or navigation-only shells. Every unverified item is flagged in [Gaps in Research](#gaps-in-research). No citation below is asserted as publisher-verified unless the fetch that produced it is named.

**Sources fetched successfully**:
- SEP, "Grounds of Moral Status" — https://plato.stanford.edu/entries/grounds-moral-status/
- SEP, "Environmental Ethics" — https://plato.stanford.edu/entries/ethics-environmental/
- SEP, "The Moral Status of Animals" — https://plato.stanford.edu/entries/moral-animal/
- Wikipedia, "The Edge of Sentience" — https://en.wikipedia.org/wiki/The_Edge_of_Sentience

**Fetches that failed** (403 / nav-shell only): OUP book page for Birch 2024; PhilPapers record BIRTEO; Taylor & Francis open-access page for Shepherd 2018; PhilPapers archive PDF for Kammerer 2022.

## Executive Summary

Sentientism holds that the capacity for valenced experience — feeling that something is good or bad — is both necessary and sufficient for moral status. Its canonical statement is Bentham's ("The question is not, Can they reason? nor, Can they talk? but, Can they suffer?", *Introduction to the Principles of Morals and Legislation*, 1789, ch. XVII); its modern development is Singer's extension of equal consideration of interests to all sentient beings, with speciesism as the charge against the anthropocentric alternative. Its two principal rivals both **widen** the circle by dropping the experience requirement: **biocentrism** (Taylor, Attfield, Varner, after Schweitzer) grounds status in each organism's being a "teleological-centre-of-life" with a good of its own, sentient or not; **Rolston's ecocentrism** locates objective value in species, ecosystems, and the evolutionary process itself, independent of any valuer. The decisive question dividing them is whether value requires a valuer, and the sentientist's sharpest weapon is Feinberg's interests-criterion — only entities with interests can be represented, and interests presuppose a subject for whom things go well or badly.

The gap the Map is positioned to fill is this: **the encyclopedia literature does not distinguish phenomenal from functional consciousness when grounding moral status.** The SEP "Grounds of Moral Status" fetch uses "consciousness" and "sentience" interchangeably with no technical differentiation. That elision is exactly where the Map's dualism does work. If sentience is a functional property, then sentientism inherits every indeterminacy of functionalism and Kammerer's illusionist challenge bites: no phenomenal fact, no moral fact. If phenomenal experience is irreducible (Tenet 1), the sentience boundary tracks a real feature of the world rather than a threshold in an information-processing gradient. Birch's precautionary framework then supplies the action layer under uncertainty without requiring the metaphysics to be settled first.

## Assess-First Verdict

**PROCEED, WITH A NARROW BRIEF AND ONE OPERATIONAL BLOCKER.**

*The blocker*: `concepts/` stands at **317 of a 320 cap** (verified by live count, excluding the section index). Three slots remain across the whole section. `voids/` is at 100/100 and `topics/` at 318/320. Whoever runs the downstream `expand-topic` should confirm the cap has not closed in the interim, and should weigh whether sentientism is the best use of one of the last three concept slots. It is a defensible use — see below — but it is no longer a free action.

*Why it is not a duplicate*: no file named `sentientism` exists in `obsidian/`, `archive/`, or `hugo/content/`. The slug is free of live and archive-redirect collisions.

*Why it is nonetheless at high duplication risk*: the term appears **105 times** across the corpus, and the valence/broad contrast is already stated in at least six places — `topics/animal-consciousness.md:158`, `apex/minds-without-words.md:115`, `topics/ethics-under-dualism.md:162`, `concepts/valence.md:70`, `topics/emotion-and-dualism.md:124`, and two archived files. `topics/phenomenal-normativity-environmental-ethics.md` already runs the Rolston contrast in a dedicated paragraph (line 57) and devotes a whole section to "Sentientism's Environmental Demands". A concept article that re-states the valence/broad distinction and re-argues the Rolston point would be pure redundancy.

*The brief that survives*: three things are genuinely uncovered.

1. **Biocentrism has zero coverage.** Grep for `biocentri` across `topics/`, `concepts/`, `apex/`, and `archive/` returns **nothing**. Paul Taylor, Varner, Attfield, Schweitzer, and DeGrazia are each cited **nowhere in the vault**. The Map contrasts sentientism with ecocentrism and with anthropocentrism, but has never met the biocentric individualist — who is the harder opponent, because he concedes individualism and disputes only the experience requirement.
2. **"Speciesism" appears nowhere in the corpus.** Singer's central polemical term is absent.
3. **The phenomenal-vs-functional grounding question is unposed.** The Map asserts sentientism in many places but has never argued *why* it must be phenomenal sentientism rather than functional sentientism — which is the one move only the Map's metaphysics licenses, and the one the encyclopedias explicitly do not make.

*Integration payoff*: the 2026-07-31 optimistic review that minted this task, and commit `fa144ba83`, both record that `phenomenal-normativity-environmental-ethics` has 25 outbound links but only 2 live inbound and 0 apex reach — its applied-ethics payoff is unreachable from its own cluster. A `concepts/sentientism` hub is a natural inbound anchor for that orphaned cluster. This is an argument for the article existing as a **concept hub with a defined brief**, not as another survey.

## Key Sources

### SEP, "Grounds of Moral Status"
- **URL**: https://plato.stanford.edu/entries/grounds-moral-status/
- **Type**: Encyclopedia
- **Key points**:
  - Treats sentience under §5.3 "Rudimentary Cognitive Capacities"; proponents given as Singer (1993), DeGrazia (1996, 2008), Regan (2004).
  - Utilitarians "see the protection and promotion of interests, where this is understood to presuppose consciousness, as the central subject matter of morality" (§6).
  - The standard objection is **overinclusiveness**: most animals meet the lowered standard, so their status would sit on a par with most humans — which conflicts with commonsense moral judgement.
  - Rival grounds surveyed: sophisticated cognition (§5.1), potentiality (§5.2), species membership (§5.4), special relationships (§5.5), natural/undesigned status (§5.7).
- **Critical finding for the Map**: the entry **does not distinguish phenomenal from access/functional consciousness**. "Consciousness" and "sentience" are used interchangeably with no technical differentiation. This is the seam the Map's article should open.
- **Quote**: Singer's reasoning is reported as "sentience is a prerequisite of having interests and this explains why sentience is a ground of moral status" (attributed in the entry to Singer 1993, p. 57).
- **Tenet alignment**: Neutral as written; becomes Tenet-1-relevant precisely because of the elision.

### SEP, "Environmental Ethics"
- **URL**: https://plato.stanford.edu/entries/ethics-environmental/
- **Type**: Encyclopedia
- **Key points**:
  - **Rolston**: natural entities have intrinsic value independent of human valuation; species and ecosystems merit respect as objectively valuable; the entry characterises his position as reflecting a "quasi-religious perspective" on nature as a self-generating system worthy of reverence.
  - **Taylor (1981, 1986)**: each living thing is a "teleological-center-of-life" with a good of its own; all such entities have equal inherent worth generating a prima facie duty to preserve or promote their goods as ends in themselves.
  - **Attfield (1987)**: hierarchical biocentrism — all beings with a good have intrinsic value, but persons have it to a greater degree; consequentialist balancing across conflicting goods.
  - **Varner (1998)**: "biocentric individualism", with both consequentialist and deontological affinities.
  - **Feinberg's interests-criterion**: only items that have interests can have legal and, likewise, moral standing. ⚠️ The wording "for it is interests which are capable of being represented" was recorded here as a verbatim quote but could NOT be located in the primary text on two independent extractions (2026-08-01 deep-review); Feinberg's verified wording is "Interests must be compounded somehow out of conations" and "A mere thing, however valuable to others, has no good of its own." Do not re-quote the unverified form.
  - **The good-of-its-own objection** (Williams 1992; O'Neill 1993): even if HIV has a good of its own, this does not mean we ought to assign positive moral weight to realising that good. Biological good does not entail moral weight.
- **Quote (Taylor)**: "each individual living thing in nature—whether it is an animal, a plant, or a micro-organism—is a 'teleological-center-of-life' having a good or well-being of its own which can be enhanced or damaged"
- **Quote (Rolston)**: "the loss of a species is a loss of genetic possibilities and the deliberate destruction of a species would show disrespect for the very biological processes which make possible the emergence of individual living things"
- **Quote (on sentientism's limits)**: non-sentient objects "such as plant species, rivers, mountains, and landscapes...are of no intrinsic but at most instrumental value to the satisfaction of sentient beings"
- **Tenet alignment**: Rolston and Taylor both **conflict** with the Map's phenomenal value realism — each posits value with no experiencer. The Map's existing reply (that adaptive value is either descriptive function or covert normativity requiring an experiencer) is already stated at `phenomenal-normativity-environmental-ethics.md:57` and should be **cited, not re-derived**.

### SEP, "The Moral Status of Animals"
- **URL**: https://plato.stanford.edu/entries/moral-animal/
- **Type**: Encyclopedia
- **Key points**:
  - Bentham's criterion located at *Introduction to the Principles of Morals and Legislation* (1780/1789), **Chapter XVII, Section 1**, footnote to paragraph IV — corrected 2026-08-01 from the "Section 6" recorded here; verified against the primary text (econlib edition), which places the footnote at ch. XVII, §1, ¶IV.
  - Singer's development across *Animal Liberation* (1975; 1993 edn.), *Practical Ethics* (2nd edn. 1993), and *Animal Liberation Now* (2023).
  - The "insuperable line" reasoning: rationality cannot mark the boundary because many humans (infants, the comatose) lack it yet retain protection; suffering constitutes a morally relevant claim independent of cognitive sophistication.
  - Objections recorded: the **uncertainty problem** (sentience is unobservable in phylogenetically distant taxa); the **disenhancement** objection (pure hedonism appears to permit genetically eliminating pain capacity rather than eliminating the causes of pain); and **wild animal suffering** (sentientism may mandate controversial large-scale intervention).
  - The entry does distinguish phenomenal suffering from mere behavioural response as the moral trigger — unlike the "Grounds of Moral Status" entry.
- **Quote (Bentham)**: "The question is not, Can they reason? nor, Can they talk? but, Can they suffer?"
- **Quote (Korsgaard 1996: 154)**: "it is a pain to be in pain. And that is not a trivial fact"
- **Quote (Singer, speciesism)**: the anthropocentric privileging of *Homo sapiens* is arbitrary, "a kind of 'speciesism' as unjustifiable as sexism and racism"
- **Tenet alignment**: The disenhancement objection is a live threat to any purely hedonic sentientism and is **not currently answered anywhere in the vault**. The Map's phenomenal value realism (multiple phenomenal features, not valence alone, carry value) is a natural reply and should be deployed.

### Wikipedia, "The Edge of Sentience"
- **URL**: https://en.wikipedia.org/wiki/The_Edge_of_Sentience
- **Type**: Encyclopedia
- **Key points**:
  - "Birch defines sentience as the capacity for valenced experience, meaning experiences that feel pleasant or unpleasant to the subject."
  - He "distinguishes sentience from broader concepts of consciousness and intelligence, and argues that sentience is sufficient for moral consideration."
  - Three core principles: "a duty to avoid gratuitous suffering, the moral relevance of sentience candidature, and the use of democratic deliberation in deciding appropriate precautions."
  - **The page does not use the phrases "valence sentientism" or "broad sentientism".**
- **Tenet alignment**: Neutral by design (Birch is deliberately metaphysics-neutral).

### Vault: `obsidian/research/birch-edge-of-sentience-precautionary-framework-2026-05-05.md`
- **Type**: Prior Map research note, 4,313 words, already publisher-checked
- **Why it matters**: the precautionary layer of this brief is **already researched**. Reuse rather than re-fetch. It carries the verified two-tier scheme (sentience candidate / investigation priority), the five-of-eight indicator rule from Birch et al. (2021), the run-ahead principle for AI, the gaming problem for LLMs, and the Schwitzgebel–Sinnott-Armstrong "conflict of precautions" critique (caution-against-harm vs. caution-for-liberty), plus a full 15-item citation list.
- **Verified quote it carries**: "There is a credible, non-negligible possibility of sentience" — the defining condition for a sentience candidate.
- **Note**: Birch assigns non-materialist views roughly **10%** credence — worth stating plainly rather than implying he is closer to the Map than he is.

## Major Positions

### Sentientism (valence-based)
- **Proponents**: Bentham (1789); Singer (1975, 1993, 2023); Birch (2024) for the definition of sentience as valenced experience.
- **Core claim**: The capacity for experience that feels good or bad is necessary and sufficient for moral status. Interests presuppose a subject; only subjects can be wronged.
- **Key arguments**: (a) the insuperable-line argument — no cognitive threshold above sentience excludes non-human animals without also excluding marginal humans; (b) Feinberg's interests-criterion — moral standing requires representable interests; (c) the argument from arbitrariness — species membership is morally arbitrary in the way race and sex are.
- **Relation to site tenets**: Strongly compatible with Tenet 1 **if and only if** sentience is read phenomenally. Under a functional reading, sentientism is hostage to whatever the correct functional analysis turns out to be, and to Kammerer's eliminativist challenge.

### Biocentric individualism
- **Proponents**: Schweitzer (precursor); Taylor (1981, 1986); Attfield (1987); Varner (1998).
- **Core claim**: Every living organism is a teleological-centre-of-life with a good of its own that can be enhanced or damaged. Having such a good, not having experiences, is what grounds inherent worth.
- **Key arguments**: (a) sentience is an arbitrary threshold that discriminates against organisms lacking nervous systems but possessing genuine goods; (b) organisms have inherent purposes independent of conscious experience; (c) sentientism cannot protect non-sentient species at all except instrumentally.
- **Relation to site tenets**: **Direct conflict with Tenet 1's ethical consequence.** The Map's reply is the Williams/O'Neill point — a "good of its own" in the biological sense is descriptive teleology, and the inference from descriptive to normative teleology is exactly what needs an experiencer to underwrite it. The HIV counterexample is the cleanest statement of this and is currently **absent from the vault**.

### Rolston's ecocentrism
- **Proponents**: Rolston (1975, 1988, 1989); Leopold as precursor.
- **Core claim**: Value exists objectively in species, ecosystems, and the evolutionary process, independent of any valuer.
- **Key arguments**: destroying a species destroys genetic possibilities and disrespects the biological processes that make individual living things possible; natural systems are self-generating and warrant reverence.
- **Relation to site tenets**: Conflicts with phenomenal value realism. The Map's existing counter (at `phenomenal-normativity-environmental-ethics.md:57`) is a dilemma: Rolston's "adaptive value" is either functional description (not normative without an experiencer) or genuine normative property (which needs the experiential grounding phenomenal normativity supplies). **Already written — cite it.**

### Birch's precautionary framing
- **Proponents**: Birch (2024); Birch et al. (2021); the New York Declaration signatories (2024).
- **Core claim**: Under irreducible uncertainty about who is sentient, the right response is proportionate precaution triggered by *sentience candidature*, with the proportionality judgement settled democratically rather than by expert fiat.
- **Relation to site tenets**: Structurally aligned with **Tenet 5** — the asymmetric-risk argument is anti-parsimony at the action layer, refusing to let simplicity arguments dismiss sentience in unfamiliar systems. But note the divergence honestly: Birch is metaphysics-neutral by design and gives non-materialism ~10%. His framework is a *welfare-action* scheme; the Map's five-tier scale is a *catalogue-prose* scheme. They are complementary, not substitutive. This mapping is worked out in detail in the 2026-05-05 vault note and should not be re-derived.

### The illusionist challenge (Kammerer)
- **Proponent**: Kammerer (2022), "Ethics without sentience".
- **Core claim** *(reconstructed — see Gaps; not publisher-verified this session)*: if phenomenal consciousness is an introspective illusion, sentientism loses its ground, and ethics must be rebuilt without a sentience criterion.
- **Relation to site tenets**: This is the **highest-value target in the brief**. The Map already cites Kammerer in `concepts/illusionism.md` and `concepts/functional-seeming.md`, but only for the "rich illusion" and obviousness objections — never for the ethical argument. It is the case where the Map's Tenet 1 pays a direct ethical dividend: dualism is what makes the sentience criterion metaphysically secure. An article that runs this argument is doing something no other Map article does.

## Key Debates

### Does value require a valuer?
- **Sides**: sentientists (yes — value is a feature of felt experience) vs. biocentrists and ecocentrists (no — goods and values are objective features of organisms and systems).
- **Core disagreement**: whether normativity can enter a system containing no experiencer.
- **Current state**: unresolved and, per SEP, "hotly contested". The Map holds the sentientist side as a consequence of phenomenal value realism, and should say so as a position rather than presenting the debate as open.

### Is the ground phenomenal or functional?
- **Sides**: implicit functionalists (most of the applied literature, which treats behavioural and neural indicators as constitutive) vs. phenomenal realists.
- **Core disagreement**: whether "sentience" names a felt property or a functional role.
- **Current state**: **largely unposed in the encyclopedia literature** — the SEP grounds-of-moral-status entry runs the two together without comment. This is the article's principal opening.

### Overinclusiveness vs. the arbitrary-threshold objection
- **Sides**: SEP records the overinclusiveness objection against sentientism (it levels most animals with most humans); biocentrists press the opposite complaint (sentience is an arbitrarily *narrow* threshold).
- **Core disagreement**: sentientism is attacked from both directions at once, which is itself informative — it suggests the criterion is doing real discriminating work.
- **Current state**: live. The Map's graduated approach (multiple phenomenal features contributing to value, not valence alone) is a partial answer to the first horn.

### Disenhancement
- **Sides**: critics of hedonic sentientism vs. Singer-style hedonists.
- **Core disagreement**: whether a view on which suffering is the only bad licenses genetically removing the capacity to suffer instead of removing the causes of suffering.
- **Current state**: **unanswered anywhere in the vault.** Phenomenal value realism supplies the materials for a reply (removing a phenomenal capacity destroys a bearer of positive value too), but no Map article makes it.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1789 | Bentham, *Introduction to the Principles of Morals and Legislation*, ch. XVII §1, fn. to ¶IV | Canonical statement of the sentience criterion |
| 1974 | Feinberg on legal and moral standing | The interests-criterion; sentientism's sharpest tool against biocentrism |
| 1975 | Singer, *Animal Liberation*; Rolston's first species-protection argument | Both wings of the modern debate open in the same year |
| 1981 | Taylor, "The Ethics of Respect for Nature" | Teleological-centre-of-life; biocentrism made rigorous |
| 1986 | Taylor, *Respect for Nature* | Book-length biocentric egalitarianism |
| 1987 | Attfield | Hierarchical biocentrism — degrees of intrinsic value |
| 1988 | Rolston, *Environmental Ethics: Duties to and Values in the Natural World* | Ecocentrism's most rigorous defence (already cited in the Map) |
| 1992–93 | Williams; O'Neill | The "good of its own is merely descriptive" objection |
| 1993 | Singer, *Practical Ethics* 2nd edn. | Equal consideration of interests, refined |
| 1996 | Korsgaard, *The Sources of Normativity* | "it is a pain to be in pain" |
| 1998 | Varner | Biocentric individualism |
| 2012 | Cambridge Declaration on Consciousness | Institutional shift on animal consciousness |
| 2021 | Birch et al., cephalopod/decapod evidence review | Eight indicators; five-of-eight precautionary rule |
| 2022 | Kammerer, "Ethics without sentience" | Illusionism turned against the sentience criterion |
| 2024 | Birch, *The Edge of Sentience*; New York Declaration | Precaution under uncertainty becomes the operative frame |

## Potential Article Angles

Target section is `concepts/` — but see the cap blocker above.

1. **Recommended: "Sentientism" as a concept hub with a phenomenal-grounding thesis.** Define the criterion, state the Map's position (phenomenal sentientism, not functional), and run three contrasts the vault has never run: against biocentric individualism (Taylor — the *new* material), against Rolston (by citation to the existing treatment, not re-derivation), and against functional sentientism via Kammerer. Close on Birch's precautionary layer as the action-side complement. This gives the orphaned `phenomenal-normativity-environmental-ethics` cluster a hub to be linked from.
2. **Alternative if the concepts cap has closed: a `topics/` article on biocentrism specifically** — "Biocentrism and the Teleological-Centre-of-Life Argument". Zero current coverage, a clean single-target brief, and it slots beside the existing environmental-ethics material without needing a hub. `topics/` is also near cap (318/320), so this is not obviously cheaper.
3. **Cheapest option: no new article.** Fold the biocentrism contrast and the disenhancement reply into the existing `phenomenal-normativity-environmental-ethics`, which is 2,602 words and has room. This spends no cap slot at all and fixes the article that the optimistic review flagged. Worth putting to the operator if cap pressure is the binding constraint.

Whichever is chosen, the article must **not** re-state the valence/broad sentientism contrast as though new — it appears in six places already.

When writing, follow `obsidian/project/writing-style.md`: front-load the criterion and the Map's position, use named-anchor summaries for forward references, skip the background on Bentham and Singer that any LLM already has, and connect explicitly to Tenets 1 and 5 in a "Relation to Site Perspective" section.

## Gaps in Research

- **WebSearch budget exhausted (200/200) before this task began.** No live search was possible; this note rests on four direct encyclopedia fetches plus prior vault research. A follow-up pass with search available should look for post-2024 journal literature on sentientism, which this note cannot cover.
- **Birch's primary text was not reachable.** The OUP page returned a navigation shell; PhilPapers returned 403. All Birch content here comes from Wikipedia plus the vault's own 2026-05-05 note.
- **⚠️ Attribution flag — "valence sentientism" / "broad sentientism" credited to Birch (2024).** Six live and archived files attribute this labelled distinction to Birch. What is **verified**: Birch defines sentience as "the capacity for valenced experience" and distinguishes sentience from broader consciousness and intelligence. What is **not verified**: that he uses the terms *"valence sentientism"* and *"broad sentientism"*. The Wikipedia entry does not contain either phrase, and the vault's own 4,313-word Birch research note — which did have search available — does not contain them either. This may be the Map's own coinage that has been retro-attributed. **Do not treat this as an established defect** (the substantive distinction is genuinely Birch's); treat it as owing a verification at the primary text, and if unconfirmed, re-frame to "Birch's definition of sentience as valenced experience supports a distinction between..." rather than deleting.
- **⚠️ Disambiguation hazard — two Feinbergs.** The interests-criterion philosopher is **Joel Feinberg** (1974, on legal and moral standing). Every current "Feinberg" in the vault is **Todd Feinberg** (Feinberg & Mallatt, neurobiological criteria for consciousness), in `plant-cognition-and-the-plant-neurobiology-debate.md`, `invertebrate-consciousness-as-interface-test.md`, and three others. An article citing Joel Feinberg must give the first name, or the two will merge under review.
- **Kammerer (2022) is reconstructed, not verified.** The PDF fetch returned 403. Title, journal, and argument are given from background knowledge and must be checked at the publisher before the article cites it. Expected: *Journal of Consciousness Studies* 29(3–4), but **the volume, issue, and page range are unverified and should not be published as given.**
- **Shepherd, *Consciousness and Moral Status* (Routledge 2018) not reached** — 403. This is the book-length treatment of exactly the phenomenal-grounding question the recommended angle turns on. It should be consulted before writing; the Map cites Shepherd only once, and in an unrelated organoid context.
- **Rolston's dates are thin.** The SEP fetch gave 1975, 1989, and 1996 without full titles; the Map already cites *Environmental Ethics: Duties to and Values in the Natural World* (1988, Temple University Press) at `phenomenal-normativity-environmental-ethics.md:158`. Prefer the already-verified 1988 citation.
- **Singer's *Animal Liberation* date needs care.** The SEP animals entry rendered it "([1979] 1993)"; the first edition is 1975. Verify before citing.
- **Not investigated**: relational and contractualist accounts of moral status; the moral-status literature on AI beyond Birch's run-ahead principle; degrees-of-moral-status views (DeGrazia 2008) which the Map's graduated approach resembles.

## Citations

Verified this session (fetched):

1. Stanford Encyclopedia of Philosophy, "Grounds of Moral Status". https://plato.stanford.edu/entries/grounds-moral-status/
2. Stanford Encyclopedia of Philosophy, "Environmental Ethics". https://plato.stanford.edu/entries/ethics-environmental/
3. Stanford Encyclopedia of Philosophy, "The Moral Status of Animals". https://plato.stanford.edu/entries/moral-animal/
4. Wikipedia, "The Edge of Sentience". https://en.wikipedia.org/wiki/The_Edge_of_Sentience

Reported within the above sources (secondary attribution — verify at primary text before quoting):

5. Bentham, J. (1789). *An Introduction to the Principles of Morals and Legislation*, ch. XVII, §1, footnote to ¶IV.
6. Singer, P. (1975; 2nd edn. 1993). *Animal Liberation*. — date form needs checking, see Gaps.
7. Singer, P. (1993). *Practical Ethics*, 2nd edn. Cambridge University Press.
8. Singer, P. (2023). *Animal Liberation Now*.
9. Feinberg, J. (1974). On legal and moral standing. — **Joel**, not Todd.
10. Taylor, P. (1981; 1986). *Respect for Nature* and the teleological-centre-of-life argument.
11. Attfield, R. (1987). Hierarchical biocentrism.
12. Varner, G. (1998). Biocentric individualism.
13. Rolston, H. III (1975; 1988; 1989). — prefer the Map's existing 1988 Temple University Press citation.
14. Williams, B. (1992); O'Neill, J. (1993). The descriptive-good objection.
15. Korsgaard, C. (1996). *The Sources of Normativity*, p. 154.
16. DeGrazia, D. (1996). *Taking Animals Seriously*; (2008) "Moral Status As a Matter of Degree?", *Southern Journal of Philosophy*.
17. Regan, T. (2004). *The Case for Animal Rights*.

Carried from the vault's prior verified research note (`birch-edge-of-sentience-precautionary-framework-2026-05-05`):

18. Birch, J. (2024). *The Edge of Sentience: Risk and Precaution in Humans, Other Animals, and AI*. Oxford University Press. https://academic.oup.com/book/57949
19. Birch, J., Burn, C., Schnell, A., Browning, H., & Crump, A. (2021). *Review of the Evidence of Sentience in Cephalopod Molluscs and Decapod Crustaceans*. UK DEFRA.
20. The New York Declaration on Animal Consciousness (2024). https://sites.google.com/nyu.edu/nydeclaration/declaration

Unverified — do not publish as given until checked:

21. Kammerer, F. (2022). "Ethics without sentience: Facing up to the probable insignificance of phenomenal consciousness." *Journal of Consciousness Studies* — volume, issue, and pages unverified.
22. Shepherd, J. (2018). *Consciousness and Moral Status*. Routledge. — not reached (403).