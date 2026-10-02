---
title: "Research: Type-A, Type-B and Type-C Physicalism"
created: 2026-10-02
modified: 2026-10-02
human_modified: null
ai_modified: 2026-10-02T11:40:42+00:00
draft: false
description: "Research notes on Chalmers's A/B/C taxonomy of physicalist replies to the epistemic gap: verified definitions, proponents, the Type-C collapse argument, which Map reply reaches which type, and the corpus pages that aim a reply at the wrong physicalist."
topics:
  - "[[arguments-against-materialism]]"
  - "[[hard-problem-of-consciousness]]"
  - "[[four-quadrant-dualism-taxonomy]]"
  - "[[parsimony-case-for-interactionist-dualism]]"
  - "[[modal-structure-of-phenomenal-properties]]"
concepts:
  - "[[materialism]]"
  - "[[explanatory-gap]]"
  - "[[phenomenal-concepts-strategy]]"
  - "[[zombie-master-argument]]"
  - "[[philosophical-zombies]]"
  - "[[inference-to-the-best-explanation-against-dualism]]"
  - "[[neural-correlates-of-consciousness]]"
  - "[[parsimony-epistemology]]"
  - "[[philosophy-of-science-under-dualism]]"
  - "[[illusionism]]"
  - "[[mysterianism]]"
  - "[[conceivability-possibility-inference]]"
  - "[[russellian-monism]]"
related_articles:
  - "[[tenets]]"
  - "[[evidential-status-discipline]]"
  - "[[positions/arguments-for-dualism]]"
  - "[[positions/methodology-and-calibration]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-02
last_curated: null
last_deep_review: null
---

# Research: Type-A, Type-B and Type-C Physicalism

**Date**: 2026-10-02
**Origin**: harvested P2 research-topic; source review `obsidian/reviews/optimistic-2026-10-02-evidence-and-licensing-wing.md` (Expansion Opportunities, High Priority; Priority item 4).
**Sources fetched and read in full** (every quotation attributed to a source was re-checked by script against these fetched files after whitespace and quote-mark normalisation; Yetter-Chappell is quoted from the OpenAlex abstract and corpus lines from the live files): Chalmers, "Consciousness and its Place in Nature" (consc.net author's version); Chalmers, "Moving Forward on the Problem of Consciousness" (consc.net); Chalmers, "Materialism and the Metaphysics of Modality" (consc.net); Chalmers, "Phenomenal Concepts and the Explanatory Gap" (consc.net PDF); Chalmers, "The Meta-Problem of Consciousness" (consc.net PDF, publisher typesetting); P. S. Churchland, "The Hornswoggle Problem" (author-uploaded JCS PDF); Weisberg, "Hard Problem of Consciousness" (IEP); Stoljar, "Physicalism" (SEP, revision of 16 Sep 2026); Kirk, "Zombies" (SEP); Russell, *Introduction to Mathematical Philosophy* (Project Gutenberg).
**Search queries used**: Dennett "Type A materialist" self-description; Churchland "The Hornswoggle Problem" JCS 3(5-6); Van Gulick 1993 "are we all just armadillos" pages; Balog "In Defense of the Phenomenal Concept Strategy" type-B. Metadata via Crossref and OpenAlex APIs (PhilPapers returned HTTP 403 to every request and was not usable).

## Verdict (assess-first)

**A new concept page is warranted, at the lower end of the requested band (about 2,200–2,400 words), on one condition: it must lead with the Map's own routing of replies to types and the tier each reply reaches, and compress the textbook definitions.** An LLM reader already knows Chalmers's taxonomy; it does not know which of the Map's arguments answer which physicalist, and the corpus currently gets that wrong on at least eleven pages.

Why a new page rather than a fuller section on an existing one (all measured 2026-10-02 with `tools.curate.length.analyze_length`, concepts hard gate 3,500, `>=`):

- `concepts/explanatory-gap` is 3,493 (6 words of headroom); `concepts/phenomenal-concepts-strategy` 3,477 (22); `concepts/philosophical-zombies` 3,475 (24); `topics/four-quadrant-dualism-taxonomy` 4,003 against a topics gate of 4,000 (already over). None can host a section.
- `concepts/materialism` (3,159; 340 headroom) could take a ~250-word definitional paragraph, but not the reply-routing map, the proponent caveats, the Type-C collapse and the tier table. Its "Varieties of Materialism" section sorts by a different axis (reductive / non-reductive / eliminative / illusionism), so the A/B/C axis would sit awkwardly there.
- `concepts/zombie-master-argument` (2,553; 946 headroom) already carries a "Physicalist Response Map" with Type-A, Type-B and a self-coined "Type-Q" section, and it is the page with the largest single error (see misassignment M5). It should be *corrected* whatever is decided, but it is keyed to the conceivability argument's premises, while the misroutings are mostly in the explanatory-gap, parsimony and philosophy-of-science pages, which that page does not govern.
- The cluster rule the source review cites ("one page as its source" when a cluster needs a taxonomy) applies: "Type-B" (hyphenated, word-bounded, case-insensitive) appears in 28 topic/concept/apex files and "Type-A" in 8, with no defining page; "Type-C" appears in 0 and "Type-Q" in 1.
- Concepts stand at **341/360** by `tools.evolution.state.count_section_files("concepts")` (measured 11:22Z), so a slot is available.

**If the page is declined**, the minimum is two refines: rewrite the zombie-master-argument response map (M5) and add a ~200-word A/B/C paragraph to `concepts/materialism` that names Type-C's collapse and links each type to its reply. The misassignment fixes below are needed either way.

## Executive Summary

The labels are Chalmers's, and they classify *materialists* by what they grant about the epistemic gap between physical and phenomenal truths. Type-A and type-B were introduced in "Moving Forward on the Problem of Consciousness" (JCS 1997); type-C (with types D, E, F and Q) first appears in "Consciousness and its Place in Nature" (in print 2002 in Chalmers's OUP anthology; the Blackwell Guide version of 2003 is the one usually cited). Chalmers writes "materialism"; "physicalism" is the corpus's and the secondary literature's equivalent, and the SEP entry on physicalism uses a different vocabulary again (a priori versus a posteriori physicalism).

The settled lead: **Chalmers does argue that type-C collapses, into type-A, type-B, type-D or type-F, and not into type-E.** The task brief's version ("A, B or F") omits D, and the source review's version ("A, B or D–F") wrongly includes E. One collapse route matters for the Map: if future physics closes the gap by "appealing to consciousness itself, in the way that some theorists hold that quantum mechanics does", the view becomes nonreductive, type-D or type-F. That is the Map's own category.

The routing finding: the Map's datum reply reaches only type-A; its promissory, Lakatosian, progress-trend and structure-and-dynamics replies reach only type-C, which on Chalmers's argument has "no separate space"; the replies that reach type-B are the primitive-identity cost, the two-dimensional/strong-necessity argument, Chalmers's master argument against the phenomenal-concepts strategy, and the queued second-order IBE. The corpus deploys type-C replies on at least nine pages and repeatedly presents them as answers to physicalism in general, or to type-B by name. Against type-B, the Map's evidential tier is *compatible*; it is *suggestive* against type-A only on the widened explanandum set, and *suggestive* against type-C only relative to type-C's rivals. It is *discriminating* against none.

## Terminology and Coinage

- **Chalmers's labels name materialisms.** The 2003 text: "A type-A materialist denies that there is the relevant sort of epistemic gap. A type-B materialist accepts that there is an unclosable epistemic gap, but denies that there is an ontological gap. And a type-C materialist accepts that there is a deep epistemic gap, but holds that it will eventually be closed." (§3, end; verified.) Quotations in any article must keep "materialism"; prose may say "physicalism".
- **First use of type-A/type-B: Chalmers 1997**, "Moving Forward": "The type-A materialist denies that there is a "hard problem" distinct from the "easy" problems; the type-B materialist accepts (explicitly or implicitly) that there is a distinct problem, but argues that it can be accommodated within a materialist framework all the same." (§2; verified.) Chalmers 1999 restates the pair: "there are two very different brands of materialism, which I call type-A and type-B materialism" (verified). Neither the 1997 nor the 1999 full text contains "type-C" (0 hits each). *The Conscious Mind* (1996) was not checked, so "first use 1997" is the earliest *verified* use, not a proven first.
- **The 1997 type-B is broader than the 2003 type-B.** In 1997 it covered any materialist accepting a distinct hard problem; the 2003 split carved the "closable in the limit" view out as type-C. Chalmers's own placement of P. S. Churchland moves accordingly: in 1997 her hornswoggle paper is answered under "Deflationary analogies (Dennett, Churchland)", the type-A section; in 2003 she is listed as apparently type-C-sympathetic and reclassified in a footnote as "either a type-B materialist or a type-Q materialist". Individual-to-type assignments are Chalmers's readings and can shift.
- **Type-Q is Chalmers's coinage too** (2003 §8): a Quinean who rejects the distinctions the taxonomy rests on. "We might call such a view type-Q materialism." (verified.) This bears directly on misassignment M5.
- **Alternative vocabularies.** SEP "Physicalism" (Stoljar, revision of 16 Sep 2026; full text): six occurrences of "a posteriori physicalism", two of "a priori physicalism", zero type-letter labels. SEP "Zombies" (Kirk, revision of 25 Mar 2023): zero type labels. IEP "Hard Problem of Consciousness" (Weisberg): "strong reductionism" for the type-A family and "weak reductionism" for type-B, citing the same type-B proponents Chalmers lists. An article should give the A/B/C labels as Chalmers's and mention the a priori / a posteriori equivalents once.
- **"Theft over honest toil" is Russell's phrase, not Chalmers's.** Chalmers uses it against type-B without attribution ("An opponent will hold that this move is more akin to theft than to honest toil"). The source is Russell 1919, ch. VII "Rational, Real, and Complex Numbers": "The method of "postulating" what we want has many advantages; they are the same as the advantages of theft over honest toil." (Gutenberg full text; verified; the page marker before it is [Pg 70].) An article that uses the phrase must credit Russell.

## Key Sources

### Chalmers, "Consciousness and its Place in Nature" (2003)
- **URL**: https://consc.net/papers/nature.html ; DOI 10.1002/9780470998762.ch5 (Crossref: Blackwell Guide to Philosophy of Mind, eds. Stephen P. Stich and Ted A. Warfield, pp. 102–142, issued 2003; the consc.net header misprints the second editor as "F. Warfield")
- **Type**: Book chapter (survey with original arguments)
- **Access**: full text (author's online version; section numbers from that version; print pagination not collated)
- **Key points**:
  - Defines A, B, C by response to the epistemic gap; maps them onto the conceivability argument's premises; D, E, F are the nonreductive options, sorted by their stance on microphysical causal closure.
  - Type-A footnote: "Type-A materialists include Dennett 1991, Dretske 1995, Harman 1990, Lewis 1988, Rey 1995, and Ryle 1949." Type-B footnote: "Type-B materialists include Block and Stalnaker 1999, Hill 1997, Levine 1983, Loar 1990/1997, Lycan 1996, Papineau 1993, Perry 2001, and Tye 1995."
  - Type-A's cost: "The obvious problem with type-A materialism is that it appears to deny the manifest."
  - Type-B's cost: the identity is epistemically primitive, so "the type-B materialist recognizes a principle that has the epistemic status of a fundamental law, but gives it the ontological status of an identity"; "By labeling these principles identities or necessities rather than laws, the view may preserve the letter of materialism; but by requiring primitive bridging principles, it sacrifices much of materialism's spirit."
  - Type-C collapses (see the next section but one).
  - Interlude verdict: "it looks like the only remotely viable options for the materialist are type-A materialism and type-B materialism", with costs "denying the manifest explanandum in the first case, and embracing primitive identities or strong necessities in the second case".
  - Type-D definition: "First, one could deny the causal closure of the microphysical, holding that there are causal gaps in microphysical dynamics that are filled by a causal role for distinct phenomenal properties: this is type-D dualism."
- **Tenet alignment**: Aligns with Tenet 1 (Chalmers's verdict against A and B is the Map's), and the type-D definition is the category Tenets 2 and 3 place the Map in. Chalmers himself does not endorse type-D over F; he says none of D, E, F "has obvious fatal flaws".

### Chalmers, "Moving Forward on the Problem of Consciousness" (1997)
- **URL**: https://consc.net/papers/moving.html
- **Type**: Journal article (reply to JCS symposium), *Journal of Consciousness Studies* 4(1): 3–46 (per the author's page and the 2003 bibliography; JCS 1997 has no Crossref DOI)
- **Access**: full text (author's version)
- **Key points**: the earliest verified use of the type-A/type-B labels; places Clark and Hardcastle as type-B; treats Dennett and both Churchlands under type-A deflationary analogies; contains no type-C.
- **Tenet alignment**: Neutral (terminological source).

### Chalmers, "Materialism and the Metaphysics of Modality" (1999)
- **URL**: https://consc.net/papers/modality.html ; DOI 10.2307/2653685 (Crossref: *Philosophy and Phenomenological Research* 59(2): 473–)
- **Type**: Journal article (reply to symposium on *The Conscious Mind*)
- **Access**: full text (author's version)
- **Key points**: "All of the commentators are type-B materialists": Hill & McLaughlin, Loar, Yablo; Shoemaker "endorses one element of the type-A materialist position". Verifies Hill & McLaughlin as type-B by Chalmers's assignment.
- **Tenet alignment**: Aligns with Tenet 1.

### Chalmers, "Phenomenal Concepts and the Explanatory Gap" (2007)
- **URL**: https://consc.net/papers/pceg.pdf ; DOI 10.1093/acprof:oso/9780195171655.003.0009 (Crossref: Alter & Walter (eds.), *Phenomenal Concepts and Phenomenal Knowledge*, OUP, pp. 167–194, issued 2007; the PDF header says 2006)
- **Type**: Book chapter
- **Access**: full text (author's PDF)
- **Key points**:
  - The phenomenal-concepts strategy is the type-B strategy: "many type-B materialists have turned to a different strategy for reconciling conceptual dualism and ontological monism"; Chalmers's target is "a type-B materialist who accepts that we are phenomenally conscious and that there is an epistemic gap between physical and phenomenal truths, and who aims to give a psychological explanation of the existence of this epistemic gap."
  - The name of the strategy is Stoljar's: "Following Stoljar (2005), we can call this the phenomenal concept strategy." Loar is the "locus classicus".
  - The master argument (§3): "(1) If P&~C is conceivable, then C is not physically explicable." "(2) If P&~C is not conceivable, then C cannot explain our epistemic situation." Crucially: "Here, again, we are assuming nothing about the relationship between conceivability and possibility." It needs only the conceivability of zombies, "an assumption that type-B materialists typically grant." (This settles misassignment M10.)
  - The type-A psychological-explanation strategy is set aside (examples cited: Dennett 1981; Jackson 2003).
- **Tenet alignment**: Aligns with Tenet 1.

### Chalmers, "The Meta-Problem of Consciousness" (2018)
- **URL**: https://consc.net/papers/metaproblem.pdf (publisher typesetting; header "Journal of Consciousness Studies, 25, No. 9–10, 2018, pp. 6–61")
- **Type**: Journal article
- **Access**: full text
- **Key points**: "The really distinctive illusionist approach to the mind–body problem is instead a version of type-A materialism, on which there is no epistemic gap." Weak, lower-order illusionism "is most naturally seen as a sort of type-B materialism about consciousness". "There is an illusionist (or ‘type-A’) version of the phenomenal concept strategy", which Chalmers says his 2007 critique does not threaten.
- **Tenet alignment**: Aligns with Tenet 1. Matters for the corpus because several pages treat the phenomenal-concepts critique as reaching illusionism, and one assigns a type-B formula to illusionism (M8).

### P. S. Churchland, "The Hornswoggle Problem" (1996)
- **URL**: https://joelvelasco.net/teaching/2300/hornswoggleprob.pdf (author-uploaded copy); Ingenta record https://www.ingentaconnect.com/content/imp/jcs/1996/00000003/f0020005/726
- **Type**: Journal article, *JCS* 3(5–6): 402–408 (PDF header); reprinted in Shear (ed.) 1997, which is the version Chalmers cites as "Churchland (1997)"
- **Access**: full text
- **Key points**: the type-C posture in the proponent's own words: "When not much is known about a domain of phenomena, our inability to imagine a mechanism is a rather uninteresting psychological fact about us, not an interesting metaphysical fact about the world." Chalmers 2003: "Churchland (1997) suggests that even if we cannot now imagine how consciousness could be a physical process, that is simply a psychological limitation on our part that further progress in science will overcome."
- **Tenet alignment**: Conflicts with Tenet 1; Tenet 5's caution about simplicity under incomplete knowledge cuts against her optimism and equally against any dualist confidence.

### Weisberg, "Hard Problem of Consciousness" (IEP)
- **URL**: https://iep.utm.edu/hard-problem-of-conciousness/ (the URL's misspelling is IEP's)
- **Type**: Encyclopedia
- **Access**: full text
- **Key points**: "weak reductionism" is the type-B family, citing Block 2002, Block & Stalnaker 1999, Hill 1997, Loar 1997/1999, Papineau 1993/2002, Perry 2001. Its justification for the identity is parsimony: "we can still identify consciousness with physical properties if the most parsimonious and productive theory supports such an identity"; and "Identities have no explanation: a thing just is what it is."
- **Tenet alignment**: Conflicts with Tenet 1; **this is where Tenet 5 actually meets type-B** (see Corpus Map, row B4).

### Supporting sources (verified at the level stated)
- **Yetter-Chappell, "Dissolving Type-B Physicalism"**, *Philosophical Perspectives* 31(1): 469–498 (2017), DOI 10.1111/phpe.12099 (Crossref). Abstract-only (OpenAlex): "The majority of physicalists are type-B physicalists"; argues that a suitably wired agent could derive the phenomenal-physical truths a priori, yielding "a type-A phenomenal concept strategy". A contemporary argument from the physicalist side that type-B is unstable in the direction of type-A.
- **Balog 1999**, *Phil. Review* 108(4): 497–, DOI 10.2307/2998286 (Crossref; abstract via OpenAlex): rejects Chalmers's a priori entailment thesis while defending physicalism. **Balog 2012**, "In Defense of the Phenomenal Concept Strategy", *PPR* 84(1): 1–23, DOI 10.1111/j.1933-1592.2011.00541.x (Crossref; online 2011): metadata-only. Balog is type-B by inference (PCS is type-B per Chalmers 2007); Chalmers assigns her no letter in the texts read. A search summariser reports that her 2012 paper contrasts type-B favourably with "Russellian physicalism"; that is a lead, not a verified reading.
- **Block & Stalnaker 1999**, *Phil. Review* 108(1): 1–46, DOI 10.2307/2998259; **Hill 1997**, *Phil. Studies* 87(1): 61–85, DOI 10.1023/A:1017911200883; **Hill & McLaughlin 1999**, *PPR* 59(2): 445–, DOI 10.2307/2653682; **Loar 1990**, *Phil. Perspectives* 4: 81–108, DOI 10.2307/2214188; **Papineau 1993**, *AJP* 71(2): 169–183, DOI 10.1080/00048409312345182; **Levine 1983**, *PPQ* 64(4): 354–361, DOI 10.1111/j.1468-0114.1983.tb00207.x; **Nagel 1974**, *Phil. Review* 83(4): 435–, DOI 10.2307/2183914; **McGinn 1989**, *Mind* 98(391): 349–366, DOI 10.1093/mind/XCVIII.391.349; **Stoljar 2005**, *Mind & Language* 20(5): 469–494, DOI 10.1111/j.0268-1064.2005.00296.x; **Smart 1959**, *Phil. Review* 68(2): 141–, DOI 10.2307/2182164. All metadata-only (Crossref); none read for this note. Their type assignments rest on Chalmers's verified footnotes, not on their own texts.
- **Van Gulick 1993**, "Understanding the phenomenal mind: Are we all just armadillos?", in Davies & Humphreys (eds.), Blackwell, pp. 137–154 (per a search summariser). Metadata-only and unresolved: Chalmers's bibliography gives the volume title as *Consciousness: Philosophical and Psychological Aspects*; the summariser gives *Consciousness: Psychological and Philosophical Essays*.
- **Lewis 1988**, "What Experience Teaches", *Proceedings of the Russellian Society* (Sydney). Metadata only from Chalmers's bibliography (no volume or pages given there); not independently verified.

## Major Positions

### Type-A (deny the epistemic gap)
- **Proponents (Chalmers's assignment, verified)**: Dennett 1991, Dretske 1995, Harman 1990, Lewis 1988, Rey 1995, Ryle 1949. Among representationalists only Dretske and Harman are type-A; Chalmers counts Dretske's externalist view as type-A because environmental relations are "part of functional role, broadly construed". Strong illusionism is type-A (Chalmers 2018). Jackson's later physicalism is cited in 2007 as an instance of the type-A strategy.
- **Core claim**: "According to type-A materialism, there is no epistemic gap between physical and phenomenal truths; or at least, any apparent epistemic gap is easily closed." Its mark is "the view that on reflection there is nothing in the vicinity of consciousness that needs explaining over and above explaining the various functions". It takes eliminativist and analytic-functionalist forms ("Type-A materialism sometimes takes the form of eliminativism"), and views that reject functionalism for neglecting biology or environment "may still be type-A views".
- **Against the arguments**: denies premise 1 of the conceivability argument (zombies are not conceivable on reflection); on the knowledge argument Mary "gains at most an ability" (Lewis's ability hypothesis).
- **Relation to tenets**: Contradicts Tenet 1 at the datum. Chalmers concedes the dispute "usually comes down to intuition", and a minority position: "even among materialists, type-A materialists are a distinct minority". The Map's own tenets page already locates the illusionist dispute at bedrock.

### Type-B (grant the epistemic gap, deny the ontological gap)
- **Proponents (Chalmers's assignment, verified)**: Block & Stalnaker 1999, Hill 1997, Levine 1983, Loar 1990/1997, Lycan 1996, Papineau 1993, Perry 2001, Tye 1995; Carruthers 2000 among higher-order theorists ("clearly a type-B materialist"), Rosenthal 1997 "either type-A or type-B"; the 1999 symposiasts Hill & McLaughlin, Loar and Yablo. By inference: Balog. Weak (lower-order) illusionism (Chalmers 2018).
- **Core claim**: "According to type-B materialism, there is an epistemic gap between the physical and phenomenal domains, but there is no ontological gap." Zombies are conceivable but impossible; Mary "learns old facts in a new way". The identity is a posteriori, on the water/H₂O model, and Kripke is the resource ("though it should be noted that Kripke himself denies this claim"). The type descends from "the identity theory of Place and Smart".
- **Against the arguments**: grants premise 1 ("to deny this would be to accept type-A materialism"); denies premise 2 (conceivability to possibility). The phenomenal-concepts strategy explains the gap now, and predicts its persistence.
- **Relation to tenets**: Contradicts Tenet 1 but grants the Map's datum. This is the live opponent: Chalmers's "only remotely viable" pair, and "the majority of physicalists" per Yetter-Chappell's abstract.

### Type-C (grant a deep gap now, hold it closable in principle)
- **Proponents ("apparently sympathetic", Chalmers 2003)**: Nagel 1974, P. S. Churchland 1996/1997, Van Gulick 1993, McGinn 1989, each reclassified except Van Gulick (next section).
- **Core claim**: "According to type-C materialism, there is a deep epistemic gap between the physical and phenomenal domains, but it is closable in principle." Zombies "are conceivable for us now, but they will not be conceivable in the limit"; "Zombies and the like are prima facie conceivable (for us now, with our current cognitive processes), but they are not ideally conceivable (under idealized rational reflection)."
- **Against the arguments**: denies premise 1 read as *ideal* conceivability, so its attack is on the same premise as type-A, deferred to the limit.
- **Relation to tenets**: Contradicts Tenet 1; it is the only physicalist who issues the promissory note the Map's Lakatosian and Kuhnian critiques target.

### Type-Q, and where D/E/F sit
- **Type-Q** is the Quinean who rejects the a priori/a posteriori distinctions the taxonomy uses. Chalmers argues it inherits the problems of whichever type its substantive view resembles: functions-explain-everything (Dennett "may be an example") → type-A problems; isomorphism-grounded identities (Paul Churchland "may be an example") → type-B problems; "Others may appeal to novel future sorts of explanation; if so, the problems of type-C materialism arise."
- **D/E/F** are the nonreductive options: D denies microphysical closure (interactionism), E accepts closure and denies phenomenal causal role (epiphenomenalism), F locates (proto)phenomenal properties in the intrinsic natures of the physical (Russellian monism). In the two-dimensional argument, F is the one exit that grants the zombie world's conceivability and still escapes the conclusion: "(3) If a world verifies P&~Q, then a world satisfies P&~Q or type-F monism is true."
- **The Map is type-D by Chalmers's definition.** Tenets 2 and 3 put consciousness's causal role in the gaps of microphysical dynamics, which is Chalmers's wording. The corpus never says this in so many words (the four-quadrant page calls Stapp "Type-D by relation" but not the Map).

## The Type-C Collapse (lead settled)

**Verified verbatim (2003 §7):** "Despite its appeal, I think that the type-C view is inherently unstable. Upon examination, it turns out either to be untenable, or to collapse into one of the other views on the table. In particular, it seems that the view must collapse into a version of type-A materialism, type-B materialism, type-D dualism, or type-F monism, and so is not ultimately a distinct option."

The four routes, each verified:

1. **Closure by better reasoning → type-A.** If the gap closes because we are now confused and better reasoning would show that explaining the functions explains everything, "I will count this position as a version of type-A materialism, not type-C materialism".
2. **Closure by new physics that invokes consciousness → type-D or type-F.** "One possibility is that instead of postulating novel properties, physics might end up appealing to consciousness itself, in the way that some theorists hold that quantum mechanics does. This possibility cannot be excluded, but it leads to a view on which consciousness is itself irreducible, and is therefore to be classed in a nonreductive category (type D or type F)."
3. **Closure by a "complete physics" that includes intrinsic natures → type-F** ("it is precisely the position discussed under type F").
4. **Materialism without an implication from physics to consciousness → type-B.**

The core argument: physical descriptions are structural-dynamical; "from structure and dynamics, one can infer only structure and dynamics"; consciousness is not structural-dynamical; and any appeal to an intermediate X (representation, information) "can only work by equivocation". Conclusion: "So in the end, there is no separate space for the type-C materialist." The footnote reclassifies the sympathisers: "I think McGinn is ultimately a type-F monist, Nagel is either a type-B materialist or a type-F monist, and Churchland is either a type-B materialist or a type-Q materialist (below)." Van Gulick is not reclassified.

**Consequences for the Map.**
- The task brief's lead ("A, B or F") omits D; the source review's ("A, B or D–F") includes E, which Chalmers does not list. The correct statement is *A, B, D or F*.
- On Chalmers's argument, defeating A and B suffices: the Map's large investment in anti-type-C replies answers an opponent that has no stable position of its own. Each type-C reply still has a use, which is to force the opponent to say which of A, B, D or F they are.
- Route 2 deserves a sentence in any article: the one way a type-C physicalist's future physics could close the gap without reducing consciousness is the kind of physics Tenet 2 posits, and Chalmers files that outcome under nonreductive views. This gives the Map no evidential gain (nothing has been found), but it is a dialectical point the corpus has not made.

## Key Debates

### What each type grants, and which argument premise it denies

| | Epistemic gap | Conceivability arg. P1 (P&~Q conceivable) | P2 (conceivable → possible) | P3 (possible → materialism false) | Mary | Predicts the gap's future |
|---|---|---|---|---|---|---|
| **A** | denies (or "easily closed") | denies | — | — | gains "at most an ability" | none to close |
| **B** | grants, "unclosable" | grants | **denies** | — | "old facts in a new way" | **persists** |
| **C** | grants "deep" gap now | denies under *ideal* conceivability | — | — | lacks information only now | **closes in principle** |
| **F** (not materialist) | grants | grants | grants | denies (the 2D argument's third premise) | — | — |

The last column is the crux of the corpus problem. **Persistence of the gap is evidence only against type-C** (and weakly, since type-C sets no deadline); type-B predicts persistence, and type-A denies there is a gap to persist. The NCC page already says so ("persistence decides nothing, since Type-B physicalism predicts it too", `concepts/neural-correlates-of-consciousness` L142).

### Which replies each type is exposed to
- **Type-A**: the manifest-datum reply ("appears to deny the manifest"); the first-person-warrant reply ("explaining the dispositions to report may remove the third-person warrant (based on observation of others) for accepting a further explanandum, but it does not remove the crucial first-person warrant (from one's own case)."); the vitalism and luminescence analogies are disanalogous; the meta-problem's burden. Not exposed to promissory-note critiques (it promises nothing), and only partly to the master argument (the type-A version of PCS escapes it, Chalmers 2018).
- **Type-B**: the primitive-identity cost (identity with the epistemic status of a law; Russell's "theft over honest toil"); the two-dimensional argument and "strong necessities" ("Ultimately, I think a type-B materialist must hold that the case of consciousness is special"); the loss of reductive explanation ("there is a sense in which any type-B materialist position gives up on reductive explanation"); the master argument against PCS; and, where the identity is adopted on simplicity grounds, Tenet 5. Not exposed to the promissory critique, the progress-trend argument, or the structure-and-dynamics argument (whose conclusion it accepts).
- **Type-C**: the collapse argument; the promissory/Lakatos critique; the progress-trend argument (weakly); the structure-and-dynamics argument. These are the only physicalists against whom the corpus's most frequent replies bite.

### Current state
Ongoing. The PCS debate is Chalmers's own "key area" (2003) and continues (the corpus's PCS page cites Sasaki 2025 and Zhou 2025). A newer line argues type-B is unstable toward type-A (Yetter-Chappell 2017, abstract-only). Whether type-C is "closed" depends on accepting Chalmers's structure-and-dynamics premise, which type-C sympathisers dispute; the Map should report the collapse as Chalmers's argument rather than as a settled result.

## Corpus Map: Which Map Reply Reaches Which Type

Loci verified on disk 2026-10-02 11:20–11:34Z. "Reaches" means the reply engages a premise that type holds; it says nothing about whether the reply succeeds.

| # | Map reply | Reaches | Representative loci |
|---|---|---|---|
| A1 | **Datum / mis-specified explanandum**: phenomenal character is a datum the rival omits | **A** only | `concepts/inference-to-the-best-explanation-against-dualism` L64 (first reply); `tenets` Tenet 1 rationale (illusionism at bedrock) |
| A2 | **Meta-problem / illusion problem**: the seeming needs explaining | **A** (strong illusionism) | `concepts/dualism` L138; `concepts/phenomenal-concepts-strategy` §The Illusionist Option |
| B1 | **Water/H₂O disanalogy**: zombie conceivability reflects acquaintance, not ignorance | **B** (its Kripkean model) | `concepts/zombie-master-argument` L74; `concepts/philosophical-zombies` L85; `concepts/supervenience` L89 |
| B2 | **Primitive identity = law in disguise** | **B** | `topics/parsimony-case-for-interactionist-dualism` L75 ("Whether called an identity or a law, this is a brute addition") — correct target, misdescribed (M7) |
| B3 | **Two-dimensional argument / coincidence of intensions** | **B** | `concepts/zombie-master-argument` L84–90; `concepts/kripke-a-posteriori-necessity-argument` L55 |
| B4 | **Tenet 5 against the simplicity-based identity inference** (IEP: identity adopted because "the most parsimonious and productive theory supports such an identity") | **B** | **No page runs this.** The IBE page's Tenet-5 reply targets the physicalist's IBE over seven explananda, close to but not the same as the identity inference. This is what `parsimony-epistemology` L90's fix should say instead of the promissory reply. |
| B5 | **Master argument against PCS** | **B** (PCS version only) | `concepts/phenomenal-concepts-strategy` L67–85; `concepts/materialism` L156–160; `concepts/explanatory-gap` L118–121 |
| B6 | **Second-order IBE**: dualism versus PCS as the lovelier explanation of the gap | **B** | queued P3 "Run the second-order IBE against the phenomenal-concepts strategy on the IBE page" (todo L1559) |
| C1 | **Promissory note / "future science" / Lakatosian degeneration / Kuhnian crisis** | **C** only | `concepts/philosophy-of-science-under-dualism` L100; `concepts/materialism` L140–144; `concepts/explanatory-gap` L123–127; `concepts/reductionism` L152–154; `topics/arguments-against-materialism` L81, L107–111; `topics/leibnizs-mill-argument` L113–115; `concepts/parsimony-epistemology` L90 |
| C2 | **Structure-and-dynamics argument** (Chalmers's own anti-type-C argument) | **C** (and A) — B accepts its conclusion | `topics/arguments-against-materialism` L73–79; `concepts/reductionism` L156–158 |
| C3 | **Progress-trend / persistence**: the gap has not narrowed, so the identity fails | **C** only (weakly) | `concepts/explanatory-gap` L135; `topics/modal-structure-of-phenomenal-properties` L83; `topics/arguments-against-materialism` L109 |
| F1 | **Mysterianism as "conceptual gap" debt** | **C** sympathiser whom Chalmers reclassifies as **F** | `topics/parsimony-case-for-interactionist-dualism` L79; `concepts/materialism` L162–166 |

**Distribution.** C-reaching replies appear on at least nine pages and B-reaching replies on about eight, but the B-reaching ones sit on modal and PCS pages, while the hub pages a reader meets first (explanatory-gap, materialism, arguments-against-materialism, philosophy-of-science) lead with C-reaching replies and draw physicalism-wide conclusions from them. Tenet 1's rationale itself motivates the tenet by the gap not having closed and names illusionism (type-A) as the opponent; it does not name type-B. This note does not count that as a defect, since the rationale is accurate and the tenets page is out of this task's scope, but an article should close the gap the rationale leaves.

## Misassignment Register

Severity: **high** = a hub or factual-source error; **moderate** = a named type given another type's thesis, or a reply aimed at the wrong type and drawn as general; **low** = an imprecise word. Headroom is hard gate − 1 − words (`analyze_length`, measured 2026-10-02).

**Already tasked (do not re-mint):**

- **M1. `concepts/parsimony-epistemology` L90** — "Type-B physicalists accept the gap but deny it is metaphysical, arguing future progress will close it without revising the ontology", answered as a "promissory note". Type-C described under the type-B label. *High.* Tasked: P3 "Correct parsimony-epistemology's description of Type-B physicalism" (todo L1586). This note supplies the missing half of that task: what parsimony says against the *correct* type-B is reply B4 (Tenet 5 against the simplicity-based identity inference) plus B2. **Same file, untasked, L146 (low):** the falsifier "A functional reduction of phenomenal consciousness that satisfied Type-B physicalists" asks for a type-A deliverable (a functional reduction is a priori), which a type-B physicalist neither offers nor needs. Batch it into the L90 task. Headroom 748.
- **M2. `concepts/philosophy-of-science-under-dualism` L100 and L118** — L100 aims the Lakatosian "degenerating" verdict at "the promise that physical description will eventually explain experience" (C1, type-C only) as a verdict on "the materialist consciousness programme"; L118's "Parsimony that requires denying the most certain datum we have" answers type-A only, in a paragraph about the parsimony preference generally. *High.* Tasked: P2 "Bring philosophy-of-science-under-dualism onto the evidence wing's register" (todo L1830, loci (d) and (e)). Headroom 801.

**Untasked (each verified on disk; no active todo task names these loci):**

- **M3. `concepts/explanatory-gap` L135** — "If consciousness were identical to physical processes, we would expect the identity to be explanatorily satisfying once we had the facts—as with water and H₂O. The persistent dissatisfaction suggests the identity doesn't hold." and "physicalists presuppose it can be closed; dualists deny it". Type-B denies the expectation, holding the identity epistemically primitive (a point Chalmers himself makes), and does not presuppose closure. The argument is C3 presented against physicalism generally, and it contradicts `neural-correlates-of-consciousness` L142. *High* (the hub page that should define the types). Headroom **6**: the fix must be word-neutral, e.g. "physicalists presuppose" → "promissory physicalists presuppose", funded by a cut, plus a scoping clause swapped for an existing one.
- **M4. `topics/modal-structure-of-phenomenal-properties` L83** — "The type-B physicalist responds that we may simply not yet grasp the a posteriori identity … will prove necessary once understood", answered by "fuller knowledge of neural correlates makes the absence of entailment more explicit". Type-C futurity under the type-B label, answered by C3. *Moderate.* Headroom 1,588.
- **M5. `concepts/zombie-master-argument` L34, L76–82** — (a) L78: "Chalmers's taxonomy covers Type-A and Type-B" is false; the 2003 taxonomy has A–F plus Q, and the response map omits type-C (which denies premise 1 under ideal conceivability). (b) L78: "'Type-Q' is not standard nomenclature" is false; "type-Q materialism" is Chalmers's own 2003 coinage for the Quinean. The page reuses the label for a different position. (c) That position ("accepts zombie possibility while resisting the dualist conclusion") is the denial of premise 3, which the two-dimensional argument assigns to **type-F monism**, a nonphysicalist option the corpus covers at `russellian-monism`. (d) L80's gloss, that zombies are possible yet consciousness "supervenes on the physical with metaphysical necessity even across possible worlds", is internally inconsistent: a possible zombie world is a failure of metaphysical supervenience. **The error was ratified by at least six reviews**: deep reviews 2026-03-07, 03-30 and 05-20 ("Type-Q correctly flagged as non-standard"), 07-25 ("Type-Q transparency note — untouched and intact"), pessimistic 07-08 ("good epistemic hygiene"), and optimistic 2026-03-14. The fixer must override those stability notes. Entered 2026-02-23 (commit d595fd6bdd, by `git log -S`). *High.* Headroom 946.
- **M6. `concepts/philosophical-zombies` L87–91 ("The Two-Dimensional Response")** — attributes two-dimensional semantics to "Sophisticated Type-B physicalists" and replies "If all truths about consciousness were deducible from physical truths, zombies wouldn't even be 'primarily conceivable'", which is a reply to type-A deducibility. In Chalmers 2003 §6 the two-dimensional argument is the weapon *against* type-B. *Moderate* (direction is clear; whether some type-B author does argue this way was not checked). Headroom **24**.
- **M7. `topics/parsimony-case-for-interactionist-dualism` L75 and L81** — L75 says of type-B that "Consciousness strongly emerges from physical processes"; type-B is an identity view and rejects emergence of a further kind (the cost argument that follows is the correct B2 reply, so keep it). L81 puts "the representationalist and higher-order theorists who follow them" under type-A; Chalmers's verified footnote splits them: Dretske and Harman type-A, Lycan and Tye type-B, Carruthers "clearly a type-B materialist", Rosenthal A-or-B. *Moderate.* Headroom 78 (word-neutral swaps).
- **M8. `topics/leibnizs-mill-argument` L111** — "The response concedes the explanatory gap while denying its metaphysical significance. [[illusionism]] … takes this path". That is the type-B formula; Chalmers 2018 classes distinctive (strong) illusionism as type-A, which denies the gap. *Moderate.* Headroom 984.
- **M9. `topics/arguments-against-materialism` L73–82 and L115** — the "Why Materialism Cannot Close the Gap" section runs C2 and C1, and L115 concludes that "physicalism—in all its forms from reductive identity theory to eliminativism to illusionism—cannot account for consciousness". Type-B agrees that materialism cannot *close* the gap and claims to *account for* it by identity. The page's only type-B engagement (L55) answers it by the convergence pattern alone. The page has 0 type-B mentions. *Moderate* (an overreach more than a mislabel). Headroom 913.
- **M10. `concepts/knowledge-argument` L84** — after stating Chalmers's dilemma against PCS, "Type-B physicalists deny that conceivability tracks possibility, so the debate remains open." The master argument assumes "nothing about the relationship between conceivability and possibility", so that type-B defence does not touch it. A type-B defence is aimed at an argument it cannot reach. (The page's paraphrase of the dilemma's horns also loosely tracks Chalmers's P&~C structure.) *Moderate.* Headroom **8** (word-neutral).
- **M11. `concepts/reductionism` L152** — "Materialists have a standard reply: … future science will close the gap" (C1), answered by "more data cannot close it because data is itself structural" (C2), a conclusion type-B accepts. The page names type-B as "the most serious objection" at L111, so L152 answers the weaker opponent without saying so. *Low.* Headroom 99 ("Materialists" → "Type-C materialists" is +0 net if a word is cut nearby).
- **M12. `concepts/epistemology` L57** — type-B characterised as holding the gap reflects "merely a limitation in our current concepts". "Current" is type-C; type-B locates the gap in the *permanent* distinctness of phenomenal and physical concepts. *Low.* Headroom **1**: delete "current" (−1).
- **M13. `topics/consciousness-defeats-explanation` L142** — "Physicalism must instead either treat the failure as temporary — a promissory note with no expiration date — or, with the mysterian, as permanent but epistemic." The main occupant of "permanent but epistemic" is type-B, and Chalmers reclassifies the mysterian (McGinn) as type-F. *Low.* Headroom 656.

**Borderline, not counted:** `topics/eliminative-materialism` L152 ("The eliminativist bets the explanatory gap will close once the right science arrives"). Chalmers classes eliminativism as type-A, but the Churchlandian eliminativist's future-neuroscience bet is the posture Chalmers lists as type-C-sympathetic, so the sentence is defensible for that eliminativist. `concepts/dualism` L140 ("this provides no positive account of *how*") is a fair compression of Chalmers's "gives up on reductive explanation".

**Correct and worth copying:** `concepts/neural-correlates-of-consciousness` L142 and L152; `concepts/inference-to-the-best-explanation-against-dualism` L64, L74, L80; `concepts/disguised-property-dualism` L45, L71–73; `concepts/kripke-a-posteriori-necessity-argument` L55.

## The Map's Tier Against Each Type

The ladder is the IBE page's (L62): evidence *compatible with* a tenet, *suggestive* of it, or *discriminating* in its favour over the physicalist rival. P-M1 governs throughout: a tenet removes a defeater but never upgrades the evidence.

| Type | Tier | Why |
|---|---|---|
| **A** | **Suggestive**, provisionally, and only on the widened explanandum set | The IBE page's verdict against "a physicalist who denies the datum". The widening is exactly what type-A rejects; Chalmers concedes the dispute "usually comes down to intuition", and the first-person warrant is not shareable evidence. The disagreement runs to bedrock, as Tenet 1's rationale already says. |
| **B** | **Compatible** | Type-B grants the datum and predicts every observation the Map cites: persistence, NCC opacity, the reports. The replies that reach it (B1–B5) are a priori and modal; they bear on plausibility, not on evidential tier. Suggestive only if the queued second-order IBE (B6) favours dualism by stated criteria, which the IBE page's verdict already makes conditional. |
| **C** | **Suggestive relative to type-C's rivals; compatible as between dualism and physicalism** | Persistence of the gap is mildly unexpected on type-C (a closure prediction with no deadline) and expected on dualism *and* on type-B. Evidence against type-C therefore moves credence toward B, D and F alike and does not discriminate dualism from physicalism. Its main defeat is dialectical (the collapse argument). |
| **any** | **Discriminating: nowhere** | Matches the IBE page's verdict. A discriminating result would have to come from the Tenet-3 channel (an intention-conditioned deviation), which neither type addresses. |

## Historical Timeline

| Year | Event / Publication | Significance |
|---|---|---|
| 1919 | Russell, *Introduction to Mathematical Philosophy* | "theft over honest toil", later turned on type-B by Chalmers |
| 1959 | Smart, "Sensations and Brain Processes" | identity theory; type-B's ancestor per Chalmers (with Place), though its topic-neutral analyses suggest type-A |
| 1974 | Nagel, "What Is It Like to Be a Bat?" | type-C-sympathetic; reclassified B or F |
| 1980 | Kripke, *Naming and Necessity* | a posteriori necessity, type-B's resource, which Kripke denies applies to mind |
| 1983 | Levine, "Materialism and Qualia: The Explanatory Gap" | names the gap; listed by Chalmers as type-B |
| 1988 | Lewis, "What Experience Teaches" | ability hypothesis; type-A |
| 1989 | McGinn, "Can We Solve the Mind–Body Problem?" | type-C-sympathetic; reclassified F |
| 1990 | Loar, "Phenomenal States" | locus classicus of PCS; type-B |
| 1991 | Dennett, *Consciousness Explained* | type-A |
| 1993 | Papineau (AJP); Van Gulick ("armadillos") | type-B; type-C-sympathetic |
| 1996 | P. S. Churchland, "The Hornswoggle Problem" | type-C posture in her own words |
| 1997 | Chalmers, "Moving Forward" (JCS 4(1)) | **earliest verified use of type-A / type-B** |
| 1999 | Chalmers (PPR); Block & Stalnaker; Hill & McLaughlin; Balog | type-B consolidated; "which I call type-A and type-B" |
| 2002/2003 | Chalmers, "Consciousness and its Place in Nature" | **adds type-C (with D, E, F, Q)**; the type-C collapse argument |
| 2005 | Stoljar, "Physicalism and Phenomenal Concepts" | names the "phenomenal concept strategy" |
| 2007 | Chalmers, "Phenomenal Concepts and the Explanatory Gap" | master argument; PCS = type-B strategy |
| 2012 | Balog, "In Defense of the Phenomenal Concept Strategy" | type-B defence |
| 2017 | Yetter-Chappell, "Dissolving Type-B Physicalism" | type-B unstable toward a type-A PCS |
| 2018 | Chalmers, "The Meta-Problem of Consciousness" | strong illusionism = type-A; weak = type-B |

## Potential Article Angles

1. **Recommended: "Which physicalist does each argument answer?" — concept page `type-a-type-b-and-type-c-physicalism`, target 2,200–2,400 words.** Lead (first ~150 words): the three types by what they grant about the gap; the live opponent is B; type-C collapses into A, B, D or F, so the Map's promissory replies answer an unstable position; the Map's tier against each (compatible against B, provisionally suggestive against A, discriminating against none). Then: (i) definitions with the premise table (compressed; quote Chalmers's three-sentence definition once, keeping "materialist"); (ii) proponents with the caveat that assignments are Chalmers's readings and shift (Churchland 1997 → 2003; representationalists split; illusionism strong/weak); (iii) the collapse argument, with route 2 as the Map-relevant point and Chalmers's type-D definition as the Map's own category; (iv) the routing table (the Corpus Map above, cut to one line per reply and linked to each hosting page); (v) the common misroutings as *patterns* (persistence-as-evidence against B; "future progress" in type-B's mouth; the type-B defence aimed at the master argument; illusionism given the type-B formula), without page-by-page shaming; (vi) tiers. Relation to Site Perspective: Tenet 1 (each argument for it is answered by a different type; the tenet's own rationale names A and implicitly C, not B), Tenet 5 (the correct Tenet-5 reply to type-B targets the simplicity-based identity inference, and binds the Map's abductions equally), Tenets 2–3 (the Map is type-D, which is where Chalmers files physics that appeals to consciousness). Credit Russell if "theft over honest toil" is used. Follow `obsidian/project/writing-style.md`: named-anchor forward references, no textbook background beyond the premise table.
2. **Alternative (if declined): two refines.** `concepts/materialism` gets a ~200-word paragraph in §The Materialist Response that names the three types and their replies; `concepts/zombie-master-argument` gets its response map corrected (M5).
3. **Not recommended:** a topics-section survey article. The material is a taxonomy, its value is routing, and concepts is the correct section.

## Articles That Should Later Cite It (measured 2026-10-02, `analyze_length`, body-only)

| Article | Words | Gates (soft / hard) | Status | Room |
|---|---|---|---|---|
| `concepts/zombie-master-argument` | 2,553 | 2,500 / 3,500 | soft_warning | Yes, and needs the M5 rewrite (≈ +60 net) |
| `concepts/materialism` | 3,159 | 2,500 / 3,500 | soft_warning | One sentence in §The Materialist Response |
| `concepts/dualism` | 2,665 | 2,500 / 3,500 | soft_warning | One sentence at L138–140 adding type-C and its collapse |
| `topics/arguments-against-materialism` | 3,086 | 3,000 / 4,000 | soft_warning | One sentence scoping §Misplaced Confidence in Future Science (M9) |
| `concepts/philosophy-of-science-under-dualism` | 2,698 | 2,500 / 3,500 | soft_warning | Via the tasked P2's L100/L118 edits |
| `concepts/parsimony-epistemology` | 2,751 | 2,500 / 3,500 | soft_warning | Via the tasked P3's L90 edit |
| `concepts/conceivability-possibility-inference` | 2,271 | 2,500 / 3,500 | ok | One sentence mapping premises to types |
| `concepts/kripke-a-posteriori-necessity-argument` | 2,227 | 2,500 / 3,500 | ok | Pipe the existing "type-B" at L55 |
| `topics/modal-structure-of-phenomenal-properties` | 2,411 | 3,000 / 4,000 | ok | Yes, with the M4 fix |
| `topics/leibnizs-mill-argument` | 3,015 | 3,000 / 4,000 | soft_warning | Yes, with the M8 fix |
| `concepts/inference-to-the-best-explanation-against-dualism` | 3,322 | 2,500 / 3,500 | soft_warning | Piped wikilink on the existing "Type-B physicalism" (L80); 177 headroom is reserved for the second-order IBE |
| `concepts/neural-correlates-of-consciousness` | 3,408 | 2,500 / 3,500 | soft_warning | Piped wikilink on "Type-A physicalist" at L152 only |
| `concepts/explanatory-gap` | 3,493 | 2,500 / 3,500 | soft_warning (6 below hard) | Piped wikilink only, plus the word-neutral M3 fix |
| `concepts/phenomenal-concepts-strategy` | 3,477 | 2,500 / 3,500 | soft_warning (22 below hard) | Piped wikilink only |
| `concepts/philosophical-zombies` | 3,475 | 2,500 / 3,500 | soft_warning (24 below hard) | Piped wikilink only, plus word-neutral M6 |
| `topics/parsimony-case-for-interactionist-dualism` | 3,921 | 3,000 / 4,000 | soft_warning (78 below hard) | Piped wikilink only, plus word-neutral M7 |
| `topics/four-quadrant-dualism-taxonomy` | 4,003 | 3,000 / 4,000 | hard_warning | Piped wikilink only, on the existing "Chalmers' Type-D vs Type-E vs Type-F" (L51) |
| `concepts/russellian-monism` | 2,949 | 2,500 / 3,500 | soft_warning | One clause: type-F is the two-dimensional argument's exit (supports M5) |

## Gaps in Research

- **The proponents' own texts were not read for type-B or type-A** (Block & Stalnaker, Hill, Loar, Papineau, Lycan, Tye, Perry, Dretske, Harman, Rey, Lewis): every assignment rests on Chalmers's verified footnotes. Cite them as "Chalmers classes X as type-B", not "X is a type-B physicalist", unless a later pass reads the proponent. Dennett's self-description as a "type-A" materialist was searched and **not found**; do not assert it.
- **Balog** is type-B by inference only; the summariser's report about her 2012 paper is a lead.
- **Van Gulick 1993**: metadata-only, with an unresolved volume-title variant.
- **The Conscious Mind (1996)** was not checked for the A/B labels; "first use 1997" is the earliest verified, not proven.
- **The 2002 OUP printing** of "Consciousness and its Place in Nature" is attested only by the author's page header; its pagination was not verified.
- **Russell's page**: the Gutenberg marker places the phrase after [Pg 70]; whether it falls on p. 70 or p. 71 was not settled. Cite the chapter.
- **Frankish's own classification** of illusionism relative to the A/B/C scheme was not checked; Chalmers 2018 is the source for "strong illusionism is type-A".
- **McGinn's own view** of whether his property P is physical was not checked; the parsimony-case page's "physicalism is true but human cognition cannot understand how" (L79) may overstate his physicalism, and Chalmers's type-F reading is one reading.
- **Whether any type-B author argues as M6 describes** (two-dimensional semantics with a contingent primary intension for phenomenal concepts) was not checked. Loar explicitly denies phenomenal concepts have contingent modes of presentation (per Chalmers's 2003 footnote summary), which makes M6 likely but not proven.
- **The corpus sweep** covered topics, concepts, apex, voids, positions and tenets for "type-a", "type-b", "type-c", "type-q", "promissory", "future science will close", "will/would close the gap" and "gap will close". It did not cover `archive/` or `arguments/`, and paraphrases such as "science will eventually explain" without those strings may hide further C-replies drawn as general.
- **"Master argument" names two different things in the corpus**: the zombie argument as a "master argument" (`zombie-master-argument`) and Chalmers's 2007 master argument against PCS. An article should disambiguate once.
- No source was found that applies the A/B/C taxonomy explicitly to *interactionist* dualism's evidential standing. The tier table is the Map's reconstruction from its own ladder and should be labelled as such.

## Citations

- Balog, K. (1999). Conceivability, possibility, and the mind-body problem. *Philosophical Review*, 108(4), 497–. https://doi.org/10.2307/2998286 [abstract-only; end page not in the Crossref record]
- Balog, K. (2012). In defense of the phenomenal concept strategy. *Philosophy and Phenomenological Research*, 84(1), 1–23. https://doi.org/10.1111/j.1933-1592.2011.00541.x [metadata-only]
- Block, N., & Stalnaker, R. (1999). Conceptual analysis, dualism, and the explanatory gap. *Philosophical Review*, 108(1), 1–46 (end page per Chalmers 2003's bibliography). https://doi.org/10.2307/2998259 [metadata-only]
- Chalmers, D. J. (1997). Moving forward on the problem of consciousness. *Journal of Consciousness Studies*, 4(1), 3–46. https://consc.net/papers/moving.html [full text]
- Chalmers, D. J. (1999). Materialism and the metaphysics of modality. *Philosophy and Phenomenological Research*, 59(2), 473–493 (end page per Chalmers 2003's bibliography; Crossref gives the first page only). https://doi.org/10.2307/2653685 [full text, author's version]
- Chalmers, D. J. (2003). Consciousness and its place in nature. In S. P. Stich & T. A. Warfield (Eds.), *The Blackwell Guide to Philosophy of Mind* (pp. 102–142). Blackwell. https://doi.org/10.1002/9780470998762.ch5 ; https://consc.net/papers/nature.html [full text, author's version; also in Chalmers (Ed.), *Philosophy of Mind: Classical and Contemporary Readings*, OUP, 2002]
- Chalmers, D. J. (2007). Phenomenal concepts and the explanatory gap. In T. Alter & S. Walter (Eds.), *Phenomenal Concepts and Phenomenal Knowledge* (pp. 167–194). Oxford University Press. https://doi.org/10.1093/acprof:oso/9780195171655.003.0009 [full text, author's PDF]
- Chalmers, D. J. (2018). The meta-problem of consciousness. *Journal of Consciousness Studies*, 25(9–10), 6–61. https://consc.net/papers/metaproblem.pdf [full text]
- Churchland, P. S. (1996). The hornswoggle problem. *Journal of Consciousness Studies*, 3(5–6), 402–408. Reprinted in J. Shear (Ed.), *Explaining Consciousness: The Hard Problem*, MIT Press, 1997. [full text, author-uploaded copy]
- Hill, C. S. (1997). Imaginability, conceivability, possibility and the mind-body problem. *Philosophical Studies*, 87(1), 61–85. https://doi.org/10.1023/A:1017911200883 [metadata-only]
- Hill, C. S., & McLaughlin, B. P. (1999). There are fewer things in reality than are dreamt of in Chalmers's philosophy. *Philosophy and Phenomenological Research*, 59(2), 445–. https://doi.org/10.2307/2653682 [metadata-only; end page not in the Crossref record]
- Kirk, R. (2023 revision). Zombies. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/zombies/ [full text; consulted for vocabulary only]
- Levine, J. (1983). Materialism and qualia: The explanatory gap. *Pacific Philosophical Quarterly*, 64(4), 354–361. https://doi.org/10.1111/j.1468-0114.1983.tb00207.x [metadata-only]
- Lewis, D. (1988). What experience teaches. *Proceedings of the Russellian Society* (University of Sydney). [metadata from Chalmers 2003's bibliography only]
- Loar, B. (1990). Phenomenal states. *Philosophical Perspectives*, 4, 81–108 (end page per Chalmers 2003's bibliography). https://doi.org/10.2307/2214188 [metadata-only]
- McGinn, C. (1989). Can we solve the mind–body problem? *Mind*, 98(391), 349–366. https://doi.org/10.1093/mind/XCVIII.391.349 [metadata-only]
- Nagel, T. (1974). What is it like to be a bat? *Philosophical Review*, 83(4), 435–. https://doi.org/10.2307/2183914 [metadata-only; end page not in the Crossref record]
- Papineau, D. (1993). Physicalism, consciousness and the antipathetic fallacy. *Australasian Journal of Philosophy*, 71(2), 169–183. https://doi.org/10.1080/00048409312345182 [metadata-only]
- Russell, B. (1919). *Introduction to Mathematical Philosophy*. George Allen & Unwin. Ch. VII. https://www.gutenberg.org/ebooks/41654 [full text]
- Smart, J. J. C. (1959). Sensations and brain processes. *Philosophical Review*, 68(2), 141–. https://doi.org/10.2307/2182164 [metadata-only; end page not in the Crossref record]
- Stoljar, D. (2005). Physicalism and phenomenal concepts. *Mind & Language*, 20(5), 469–494. https://doi.org/10.1111/j.0268-1064.2005.00296.x [metadata-only]
- Stoljar, D. (2026 revision). Physicalism. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/physicalism/ [full text; consulted for vocabulary only]
- Van Gulick, R. (1993). Understanding the phenomenal mind: Are we all just armadillos? In M. Davies & G. Humphreys (Eds.), *Consciousness* (pp. 137–154). Blackwell. [metadata-only; volume subtitle unresolved]
- Weisberg, J. (n.d.). Hard problem of consciousness. *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/hard-problem-of-conciousness/ [full text]
- Yetter-Chappell, H. (2017). Dissolving type-B physicalism. *Philosophical Perspectives*, 31(1), 469–498. https://doi.org/10.1111/phpe.12099 [abstract-only]
