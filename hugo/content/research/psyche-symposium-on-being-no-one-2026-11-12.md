---
ai_contribution: 100
ai_generated_date: 2026-11-12
ai_modified: 2026-11-12 17:40:50+00:00
ai_system: claude-fable-5-2
author: null
concepts: []
created: 2026-11-12
date: &id001 2026-11-12
description: 'Verified contents of the PSYCHE 11(5) symposium on Being No One and
  Metzinger''s eight 2006 replies: what each critic objected, what he conceded, and
  a fold plan for the SMT page.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-11-12 17:40:50+00:00
modified: *id001
recommended_action: fold
related_articles: []
target_section: concepts
target_slug: self-model-theory-of-subjectivity
title: Research Notes - The 2005 PSYCHE Symposium on Metzinger's Being No One
topics:
- '[[personal-identity]]'
- '[[philosophy-of-mind]]'
- '[[hard-problem-of-consciousness]]'
---

# Research: The 2005 PSYCHE Symposium on Metzinger's *Being No One*

**Date**: 2026-11-12
**Method**: `curl` of the publisher's PDFs, `pdftotext -layout`, whitespace collapsed and curly quotes normalised before every `grep`. One web search (to locate the missing reply to Gallagher). No browser tools.
**Search queries used**: `Metzinger "Reply to Gallagher" Psyche 12 2006 "Different conceptions of embodiment"`

## Executive Summary

All seventeen documents of the exchange were obtained and read: Metzinger's Précis, the eight commentaries (PSYCHE 11(5), June 2005) and his eight separate replies (PSYCHE 12, 2006). The eight names in the task brief are the complete and correct list. **Verdict: fold** into `concepts/self-model-theory-of-subjectivity`; both `topics/` and `concepts/` are at cap, and the material is a section, not a page.

This is a delta note against `research/self-model-theory-of-subjectivity-2026-07-11`, which cites only the Précis and names Zahavi as an unsourced lead. Nothing below is covered there. On the live site, `grep -rIl` over `obsidian/` and `archive/` (excluding `workflow/` and `reviews/`) finds Himma, Ghin and Livet nowhere, Legrand on one unrelated page, and Weisberg, Gallagher and Hobson only in connection with other works.

Three findings matter for the Map. (1) Himma's twin-earth argument is the Map's indexical question put to SMT in print, and Metzinger's answer is on record: which self-model is yours "is not a fact at all". (2) Metzinger repeatedly rejects the gloss that his claim is "the self is an illusion" and the gloss that "you are" a self-model. (3) Five of the eight critics reject the eliminative step, and all five do so while denying a substantial self. Zahavi, the Map's adopted ally on the minimal self, is one of them. The symposium supplies rivals' critics, and almost none of them is an ally of the Map's dualism.

## Verified Contents of the Symposium

Source for the list: the archived symposium page `psyche.cs.monash.edu.au/symposia/metzinger/` (Wayback Machine snapshot 20061108063454), which reads "PSYCHE 11 (5), June 2005 / Metzinger: Being No One / Managing Editor: Dorothée Legrand", cross-checked against the volume listings at `journalpsyche.org/archive/volume-11-2005/` and `/volume-12-2006/` and against each PDF's own header.

PSYCHE articles carry volume and issue only. There are no article numbers. Each PDF is paginated separately from 1; the page counts below are PDF page counts, given for identification, and should not be turned into a page range within an issue.

### PSYCHE 11(5), June 2005

| Author | Title (from PDF header) | File | PDF pages |
|---|---|---|---|
| Thomas Metzinger | Précis: Being No One | `journalpsyche.org/files/0xaad5.pdf` | 35 |
| Dan Zahavi | Being Someone | `0xaad8.pdf` | 20 |
| Josh Weisberg | Consciousness Constrained: A Commentary on *Being No One* | `0xaad9.pdf` | 22 |
| Allan Hobson | Finally Some One: Reflections on Thomas Metzinger's "Being No One" | `0xaada.pdf` | 8 |
| Shaun Gallagher | Metzinger's Matrix: Living the Virtual Life with a Real Body | `0xaadb.pdf` | 9 |
| Kenneth Einar Himma | The Problem of Explaining Phenomenal Selfhood: A Comment on Thomas Metzinger's Self-Model Theory of Subjectivity | `0xaadc.pdf` | 19 |
| Dorothée Legrand | Transparently Oneself | `0xaadd.pdf` | 19 |
| Marcello Ghin | What a Self Could Be | `0xaade.pdf` | 10 |
| Pierre Livet | What is Transparency? | `0xaadf.pdf` | 15 |

Ghin's PDF header omits the "PSYCHE 11 (5), June 2005" line the others carry; its page footers read "PSYCHE 2005: VOLUME 11 ISSUE 5".

### PSYCHE 12, 2006: Metzinger's replies

Metzinger chose "to reply to each author individually" and not "in a single piece" [raw, reply to Gallagher]. There is no consolidated "Author's Response".

| Reply | Title | Issue per PDF header | File | PDF pages |
|---|---|---|---|---|
| to Gallagher | Different conceptions of embodiment | 12 (4), August 2006 | Wayback only (see below) | 7 |
| to Ghin | Self-Sustainment on the Level of Global Availability | 12 (4), August 2006 | `0xaafb.pdf` | 2 |
| to Himma | Personal Identity and Cartesian Intuitions | 12 (4), August 2006 | `0xaafc.pdf` | 5 |
| to Hobson | Can there be a First-Person Science of Consciousness? | 12 (4), August 2006 | `0xaafd.pdf` | 5 |
| to Legrand | Content from the Inside Out | 12 (4), August 2006 | `0xaafe.pdf` | 6 |
| to Livet | Meta-abeyance? | 12 (4), August 2006 | `0xaaff.pdf` | 3 |
| to Weisberg | No direction home—searching for neutral ground | 12 (4), August 2006 | `0xab00.pdf` | 6 |
| to Zahavi | The Value of Historical Scholarship | **12 (2), May 2006** (header); footers say "VOLUME 12 ISSUE 4" | `0xaaf1.pdf` | 4 |

Two irregularities, both recorded so no writer "fixes" them by guessing:

- **The reply to Gallagher is absent from the `journalpsyche.org` volume-12 listing.** It was obtained from the Wayback Machine copy of the original host: `web.archive.org/web/20090912155423/http://psyche.cs.monash.edu.au/symposia/metzinger/reply_to_Gallagher.pdf`. Its header reads "PSYCHE 12 (4), August 2006". The other seven replies refer to it ("my reply to Gallagher"), and it opens the set: it carries the thanks to the editors.
- **The reply to Zahavi has an internally inconsistent issue number.** Its header says 12 (2), May 2006; its page footers say Volume 12 Issue 4; and it closes the set ("Let me close by thanking ... all the authors of the preceding commentaries"). Cite it as *PSYCHE* 12 and state the header's issue with this caveat, or give volume only.

**Not obtained**: PhilArchive/PhilPapers records (`philarchive.org/archive/METRTG-2` returned HTTP 403 to `curl`; not retried by other means). The Wayback CDX index was offline during the session, so the archived directory listing for the replies was not seen; the Gallagher reply was found by a direct availability query on its filename. Metzinger mentions "a number of very interesting critical commentaries which could not be included in this special issue" [raw, reply to Zahavi]; none was sought.

## Key Sources: Commentaries and Replies

Every quotation in this section is tagged. **[raw]** means `grep` count 1 in the fetched PDF's text after whitespace collapse. **[raw, across page break]** means the string is interrupted by a page footer in the PDF text and was confirmed by printing the surrounding context. Locators of the form "(p. N)" inside Metzinger's replies are his own references to the commentary PDFs and to BNO; they were not independently checked.

### Himma: the twin-earth argument (most relevant to the Map)

- **Own position**: not a declared dualist in this paper. He says that, compared with identity theories, he finds "substance dualism, with all its difficulties, ... a far more appealing approach" [raw], and in the same section that "None of the foregoing, of course, should be thought to imply that substance dualism is true" [raw]. His closing assessment is that "while no theory that does no more than explain subjectivity in terms of self-models can succeed, no theory that does not explain subjectivity in terms of such models can succeed either" [raw].
- **Objection 1 (me-ness)**: mineness presupposes a subject. "The idea that some entity or property is mine presupposes a me to whom that entity or property belongs" [raw]. He also asserts "it is not conceptually possible for a conscious mental state to occur that is not instantiated by a mental subject" [raw].
- **Objection 2 (twins)**: imagine a functionally and physiologically isomorphic twin on a duplicate planet. "one of these phenomenal selves is you and the other is not" [raw]. "From the standpoint of the self-model theory, it is utterly arbitrary that you (or your phenomenal self) are the subject of a stream of content brought about by physical stimulation of one of those bodies and not the other" [raw]. Invoking Nagel, the issue is "why one of these self-models is yours while another perfectly similar self-model is someone else's" [raw]. The difference "is not a simply a difference in number" [raw, sic]. He concludes the theory "fails to refute dualism" [raw].
- **Stated limits**: the argument and Nagel's formulation "assume, as noted above, that eliminative materialism and the various versions of identity theory are false" [raw]; and it may be that "as a matter of brute fact, there is a certain randomness involved in the generation of these phenomenal appearances" [raw, across page break].
- **Metzinger's reply**: the question is "ill posed: no one is identical to a particular phenomenal self" [raw]. "We are not phenomenal selves. We are systems transiently generating phenomenal selves. And as whole systems we have unique physical properties (space-time positions) that ground our individuality" [raw]. To assume selves and then ask about their relation to self-models "is simply a petitio principii in this context" [raw]. On Nagel: "This simply introduces a new entity, standing in an ownership relationship to the self-model" [raw]. The purported fact that one of the two self-models is you "is not an arbitrary fact. It is not a fact at all" [raw]. On the conceptual-necessity claim: "I must admit that I do not have this modal intuition" [raw]. He adds that the twins are not mentally identical, because "mental states are individuated by their intentional content" [raw]: "You would be phenomenological clones. But you would certainly not have identical self-knowledge" [raw].
- **What he grants**: that "in addition to phenomenal mineness, there is a more global phenomenal property, which he calls 'me-ness'" [raw; inner quotation marks normalised], which he then treats as a further layer of the self-model (temporal invariance, autobiographical memory, agency, social learning).
- **Tenet alignment**: Himma's twin question has the same structure as the indexical objection behind Tenet 4. It is not independent support: it rests on the same non-deflationary "I", and Himma says so. Metzinger's reply is the deflation that `tenets.md` already says the objection cannot neutrally exclude.

### Zahavi: "Being Someone"

- **Own position**: phenomenological minimal self; an "invariant dimension of first-personal givenness" [raw]. Not a defender of substantial selves: "a substantialist and reifying concept of self should be abandoned" [raw].
- **Objection**: Metzinger "remains committed to a rather classical conception of the self" [raw], denies that entity, and infers that no selves exist; "this conclusion would only be warranted if Metzinger's definition of the self were the only one available" [raw]. "What remains completely unconvincing to me is the eliminativist consequence drawn by Metzinger" [raw]. "the right conclusion to draw from Metzinger's account is not that there is no self, but that the self is not what some took it to be" [raw]. He also charges an "unrestrained scientism" [raw] and criticises the use of pathology and the unexplained use of "phenomenology" and "neurophenomenology".
- **Metzinger's reply**: mostly a list of agreements, with one substantive refusal. He doubts "that it is legitimate to speak of a non-conceptual sense of ownership strictly whenever we are phenomenally conscious" [raw] "because I want to take the phenomenology of psychiatric syndromes like full depersonalization or of certain spiritual experiences more seriously as well" [raw]. He says Zahavi "frequently just states how phenomenology's contribution consists in 'insisting' that a pre-reflective form of self-awareness exists" [raw; inner quotation marks normalised] where "new and original arguments to support our common case" [raw] were wanted. He concedes his "phenomenological approach to psychopathology in BNO most certainly was much too simplistic and facile" [raw]. His closing verdict on the whole debate: better to pursue detail questions "than to get lost in a competition of theories about what the appropriate weak notion of 'self' is" [raw; inner quotation marks normalised]; "Ontology and the big picture will eventually fall into place all by themselves" [raw].
- **Tenet alignment**: helps the Map's choice of the minimal self over SMT, and cuts against the Map in two places. Zahavi rejects substantial selves, which the Map's operative substance-leaning reading does not. And Metzinger's counter-evidence is depersonalisation and "certain spiritual experiences", ground the Map itself treats as contested.

### Gallagher: "Metzinger's Matrix"

- **Own position**: embodied, enactive, explicitly non-Cartesian. "What I call my 'self' is simply myself as a full-fledged embodied entity" [raw; inner quotation marks normalised]. "That there are real bodies means that there are real selves who experience themselves both as bodies and as more than bodies" [raw].
- **Objection**: "on a non-Cartesian concept of reality, the self should be considered something real, and not simply an illusion" [raw]. Treating ourselves as a self-model distinct from the body gives "a ghost in a machine" ontology [raw: "our ontology is that of a ghost in a machine"]. "there is no such thing as real disembodied experience" [raw].
- **Metzinger's reply**: concedes that "scientific realism is an implicit background assumption of BNO, and that I did not give an independent argument for it" [raw]. Introduces first-, second- and third-order embodiment (1E reactive physical system; 2E explicit self-representation as embodied; 3E that representation made conscious) and says "BNO is mainly about the relationship between 2E and 3E" [raw]. Denies a central reading: SMT "does not say (which is one of the most frequent, recurrent misunderstandings, also in other commentaries of this special issue) that 'you are' simply a self-model" [raw; inner quotation marks normalised]. "When you refer to yourself using 'I,' you refer to the system as a whole, including your brain, body, self-model, history, and social context" [raw; inner quotation marks normalised].
- **Tenet alignment**: conflicts with Tenet 1 from the other side. Gallagher's charge against Metzinger is residual Cartesianism; his self is the living body.

### Legrand: "Transparently Oneself"

- **Own position**: pre-reflexive bodily self-consciousness; she edited the symposium. "I agree with the Self-Model Theory of Subjectivity (SMT) that the self is not a substance" [raw]. She adds "I do not take the view I present here as being an argument against representationalism" [raw].
- **Objection**: "I disagree with SMT and argue that the self cannot be reduced to a phenomenal illusion" [raw]. "The self is not what is given by consciousness of the self, but the pre-reflexive subjective structure of phenomenal experience" [raw]. "transparency is not invisibility" [raw]: the self "is not invisible but transparent in that it reveals the world by hiding itself" [raw].
- **Metzinger's reply**: she makes "a mistake many people make", "namely misconstruing my claim as saying that the self is an 'illusion.'" [raw; inner quotation marks normalised]. At the subpersonal roots of the phenomenal self, "neither truth and falsity, nor knowledge and illusion exist in any philosophically interesting sense" [raw]. He says "I was not interested in demolishing classical theories of the self as a metaphysical substance" [raw] and blames the book's title for the distraction. Her inference from "SMT-systems exist" to "selves exist" "looks like a simple petitio to me" [raw]. One admission: "I also admit that I have no official position on the possibility of non-representational phenomenal character" [raw].
- **Tenet alignment**: orthogonal to dualism. Her point that transparency is compatible with a pre-reflexively present self bears on the Map's use of transparency, but she offers it inside a naturalist frame.

### Ghin: "What a Self Could Be"

- **Own position and thesis**: a friendly amendment. "there is a notion of self which is not only compatible with the SMT, but that the SMT also provides the theoretical framework for developing such a notion" [raw]: a self is an autocatalytic, self-sustaining system operating under a PSM. "The self-model theory of subjectivity makes it possible to argue that we are no one at one level and that we are someone at another level" [raw].
- **Metzinger's reply**: of the attempts to rescue a weaker concept of self, "Marcello Ghin's is clearly my favorite" [raw]. He objects to Jordan and Ghin's use of "emergence", "which in the end is not compatible with a naturalist world-view" [raw], and asks the question left open: "how exactly, in this theoretical model, would 2E lead to 3E?" [raw].
- **Tenet alignment**: neutral to conflicting. A reductionist retention of the word "self".

### Livet: "What is Transparency?"

- **Thesis**: "I suspect that transparency conflates different notions" [raw]. Revising any part of oneself requires that "we have to presuppose a self – the one which is revising- the possible incoherence of which is put in abeyance" [raw; dash normalised]. "Instead of saying that such entities do not exist, I would prefer to say that their mode of existence implies abeyance" [raw, across page break]. Selves cannot "prove their free inexistence, because this very last proof would require the activity of such things as selves" [raw].
- **Metzinger's reply**: charges several misreadings (an "extensionality equivocation") and writes "I have tried hard, but I am absolutely unable to understand what Pierre Livet's related, and central, concept of 'meta-abeyance' (p.3) actually means" [raw; inner quotation marks normalised]. He agrees "that we must begin distinguishing different types of phenomenal opacity relative to different types of access" [raw], and that "opacity increases the computational load on the system, whereas transparency is always the simpler solution" [raw].
- **Tenet alignment**: orthogonal. Livet's self-presupposition point resembles a performative argument but he draws no metaphysical conclusion from it ("does not imply that you do not exist (nor that you exist)" was read in context, not separately grep-counted: treat as [unverified] if quoted).

### Weisberg: "Consciousness Constrained"

- **Own position**: higher-order-thought sympathiser (he cites Rosenthal throughout). A methodological and friendly critique.
- **Thesis**: Metzinger's method "runs the danger of illicitly blending controversial theoretical assumptions directly into the explanandum of a theory of consciousness" [raw]. Global availability should be dropped as a mark of consciousness: "I contend that taken together, transparency and perspectivalness form a well-justified working concept of consciousness" [raw; the PDF breaks "well- justified" across a line]. So framed, SMT has "a strong affinity" with higher-order and same-order theories (he lists Rosenthal, Lycan, Gennaro, Van Gulick, Kriegel; read in context). "All told, the well-developed theory presented in Being No One compares favorably to its contemporary rivals" [raw].
- **Metzinger's reply**: "Unfortunately, I have to concede many of the points he intelligently makes" [raw]. He resists the amendment: "this concept would be circular: transparency is a property of phenomenal states only, and an unconscious state is neither transparent nor opaque" [raw]; and "If we followed Josh Weisberg's interesting line of argument, we would lose the globality of subjectivity" [raw]. He predicts that a future theory "will completely destroy these 'common-sense appearances'" [raw, across page break].
- **Tenet alignment**: orthogonal. Useful only for the cross-link between the SMT, SRT and HOT pages: a HOT-side reader placed SMT in the self-representational family in 2005.

### Hobson: "Finally Some One"

- **Own position**: sleep and dream neuroscientist; physicalist. "your self and your consciousness are no less real for being the subjective awareness of your brain states" [raw: "But your self and your consciousness are no less real for being the subjective awareness of your brain states"].
- **Objection**: "My quarrel with Metzinger concerns his refusal to call first person accounts data" [raw]. He quotes BNO p. 591, "My politically incorrect conclusion is that first person data do not exist" [raw in Hobson's text; not checked against the book]. A report's "content need only be proportional to the subjective experience itself to be scientifically valid and empirically useful" [raw]. He calls Metzinger "a third person half-some-one" [raw]. A second complaint: Metzinger is too accepting of Llinás's view that dreaming is waking minus input.
- **Metzinger's reply**: "I maintain that, strictly speaking, 'first-person data' do not exist" [raw; inner quotation marks normalised]. "if two meditators disagree about the content of their experience, there is no way to settle the dispute" [raw]. "Third-person science is driven by conflicting statements. First-person methods typically stop with existing conflicts" [raw]. He grants that "first-person approaches possess an enormous heuristic potential" [raw], and reports his own out-of-body experience and false awakening as an "autophenomenological anecdote".
- **Tenet alignment**: Metzinger's position here cuts against the Map wherever it uses contemplative or phenomenological report as evidence. Hobson defends first-person data as a physicalist and gives the Map no metaphysical support.

### The Précis itself

- Header: "PSYCHE 11 (5), June 2005". The 2026-07-11 research note dates it 2004 in five places; the live page correctly says 2005.
- The Précis says "No such things as selves exist in the world. For all scientific and philosophical purposes, the notion of a self – as a theoretical entity – can be safely eliminated" (read in context; "no such things as selves exist in the world" is [raw]). The second half of the familiar sentence, "Nobody ever was or had a self", has `grep` count 0 in the Précis. Zahavi and Gallagher both quote the full sentence from BNO with the locator "(p. 1)". The live page attributes it to the 2003 book, which is consistent.
- The word "illusion" has count 0 in the Précis (case-insensitive, with a positive control on "Cartesian").

## Who Helps the Map, Who Cuts Against It

| Paper | Bearing on the Map |
|---|---|
| Himma | States the Map's indexical question against SMT. Same premise as the Map, so no independent support. Disclaims the dualist conclusion. |
| Metzinger's reply to Himma | Cuts against: the cleanest statement of the deflation. Supplies SMT's replacement answer to "which one is me" (the whole system's space-time position), which the live page does not report. |
| Zahavi | Helps the minimal-self choice. Cuts against any substantial self. |
| Metzinger's reply to Zahavi | Cuts against: denies the universality of ownership, citing depersonalisation; says the phenomenologist "insists" where an argument is needed. |
| Gallagher, Legrand, Ghin, Livet | Reject elimination from embodied, pre-reflexive, systems-theoretic and epistemic directions. None defends a non-physical subject. Orthogonal to conflicting. |
| Weisberg | Orthogonal. A classification point for the self-modelling wing. |
| Hobson exchange | Metzinger's "no first-person data" cuts against the Map's evidential use of phenomenology. Hobson is a physicalist. |

## Fold Plan

**Host**: `obsidian/concepts/self-model-theory-of-subjectivity.md`. Measured by `analyze_length` during this session: **1,820** words, section `concepts`, soft 2,500, hard 3,500. Headroom to hard = 3,500 − 1 − 1,820 = **1,679**. Costs as drafted: Block A 404 words, Block B 78, and the nine reference entries about 180 (`analyze_length` counts the reference list). With the pending Zahavi task (+104) the page ends near 2,590: a little over the soft threshold, which gates nothing, and about 900 under the hard one. Re-measure first.

**Coordination**: `todo.md` already holds a pending P3 refine-draft on this file (source: optimistic-review 2026-11-12, self-modelling theories wing) that inserts three Zahavi quotations at L63, a Zahavi reference entry, and links to the SRT page. The blocks below do not repeat those quotations and reuse that reference entry. Run that task first, or merge; do not add a second Zahavi (2005) entry.

Other candidate hosts were measured and ruled out on length: `concepts/self-and-self-consciousness` 3,497 of 3,500; `concepts/mine-ness` 3,494 of 3,500; `topics/vertiginous-question` 3,996 of 4,000; `topics/indexical-identity-quantum-measurement` 3,417 of 4,000.

### Block A: new section, placed after "The no-self thesis and minimal phenomenal selfhood" and before "Relation to Site Perspective"

> ## The 2005–06 PSYCHE exchange
>
> *PSYCHE* printed Metzinger's Précis with eight commentaries in June 2005, and his eight separate replies the following year. Three results bear on how SMT should be read.
>
> **Metzinger rejects the "illusion" gloss.** Replying to Legrand, he calls it "a mistake many people make" to take him "as saying that the self is an 'illusion'": at the subpersonal roots of the phenomenal self, "neither truth and falsity, nor knowledge and illusion exist in any philosophically interesting sense" (2006e). Nor does SMT say that "'you are' simply a self-model": "When you refer to yourself using 'I,' you refer to the system as a whole, including your brain, body, self-model, history, and social context" (2006a).
>
> **Five critics kept the self and none of them kept the substance.** Zahavi, Gallagher, Legrand, Ghin and Livet each reject the eliminative conclusion, and each offers a deflated replacement: first-personal givenness, the lived body, "the pre-reflexive subjective structure of phenomenal experience" (Legrand 2005), a self-sustaining system operating under a self-model, an entity whose "mode of existence implies abeyance" (Livet 2005). Legrand writes, "I agree with the Self-Model Theory of Subjectivity (SMT) that the self is not a substance." Metzinger's verdict was that it is more fruitful to work on detail questions "than to get lost in a competition of theories about what the appropriate weak notion of 'self' is" (2006h). Against Zahavi he held one line firmly: he doubts that a sense of ownership is present "strictly whenever we are phenomenally conscious," citing "full depersonalization" (2006h).
>
> **Himma asked which self-model is mine.** Kenneth Himma imagines a functionally isomorphic twin on a duplicate planet. Then "one of these phenomenal selves is you and the other is not," and from SMT's standpoint "it is utterly arbitrary" which (Himma 2005). He adds that none of this "should be thought to imply that substance dualism is true." Metzinger answers that the question assumes what it must show: "We are not phenomenal selves. We are systems transiently generating phenomenal selves. And as whole systems we have unique physical properties (space-time positions) that ground our individuality." That one self-model is you "is not an arbitrary fact. It is not a fact at all" (2006c).
>
> He also made concessions. Scientific realism "is an implicit background assumption of BNO, and ... I did not give an independent argument for it" (2006a); and he has "no official position on the possibility of non-representational phenomenal character" (2006e).

Sentence-to-source map for Block A: every quoted string is tagged [raw] or [raw, across page break] in the Key Sources section above, under the paper named in its citation. "it is utterly arbitrary" occurs three times in Himma's text; the instance meant is the sentence quoted in full under Himma above. The ellipsis in the last paragraph elides "that"; the source reads "is an implicit background assumption of BNO, and that I did not give an independent argument for it". "citing 'full depersonalization'" abbreviates "psychiatric syndromes like full depersonalization or of certain spiritual experiences"; keep the abbreviation honest by not implying depersonalisation was his only example. The five one-phrase glosses of the critics' replacements are this note's paraphrases; only Legrand's and Livet's are quoted.

### Block B: addition to "Relation to Site Perspective", move 1

Anchor: the sentence ending "and the indexical objection weakens to whatever degree SMT's deflation of the subject succeeds." Insert after it:

> The exchange with Himma, reported above, is this disagreement in print. Himma's twin case puts the indexical question to SMT, and Metzinger's reply (which self-model is mine "is not a fact at all," individuality being fixed by the whole system's position in space-time) is the deflation the tenet cannot neutrally exclude. Himma's argument assumes, by his own statement, that eliminativism and identity theory are false, so it shares the Map's premise and adds no independent support for it.

"Puts the indexical question to SMT" is the Map's framing. Himma does not use the word "indexical" in the passages read and cites Nagel, not many-worlds. Check the following sentence ("So the engagement is a located disagreement ...") still reads on; its "So" now follows the inserted sentences, which suits it.

### Reference entries (add to the host; numbering to follow the existing list)

- Gallagher, S. (2005). Metzinger's matrix: Living the virtual life with a real body. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaadb.pdf
- Ghin, M. (2005). What a self could be. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaade.pdf
- Himma, K. E. (2005). The problem of explaining phenomenal selfhood: A comment on Thomas Metzinger's self-model theory of subjectivity. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaadc.pdf
- Legrand, D. (2005). Transparently oneself. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaadd.pdf
- Livet, P. (2005). What is transparency? *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaadf.pdf
- Metzinger, T. (2006a). Reply to Gallagher: Different conceptions of embodiment. *PSYCHE*, 12(4). https://web.archive.org/web/20090912155423/http://psyche.cs.monash.edu.au/symposia/metzinger/reply_to_Gallagher.pdf
- Metzinger, T. (2006c). Reply to Himma: Personal identity and Cartesian intuitions. *PSYCHE*, 12(4). https://journalpsyche.org/files/0xaafc.pdf
- Metzinger, T. (2006e). Reply to Legrand: Content from the inside out. *PSYCHE*, 12(4). https://journalpsyche.org/files/0xaafe.pdf
- Metzinger, T. (2006h). Reply to Zahavi: The value of historical scholarship. *PSYCHE*, 12. https://journalpsyche.org/files/0xaaf1.pdf
- Zahavi (2005): the entry the pending task adds. Do not duplicate.

The letter suffixes follow the alphabetical order of all eight replies (a Gallagher, b Ghin, c Himma, d Hobson, e Legrand, f Livet, g Weisberg, h Zahavi). If the host cites only four, re-letter them a to d and change the in-text citations to match.

## Corrections for Existing Pages

**The live SMT page misstates nothing about the Précis or the symposium.** Its reference 4 ("Metzinger, T. (2005). Précis: Being No One. *PSYCHE*, 11(5), 1-35") matches the PDF header and the 35-page PDF; "1-35" is the PDF's own pagination. `grep -c -F "Nobody ever was or had a self"` on the page = 1, attributed to the 2003 book, which agrees with Zahavi's and Gallagher's "(p. 1)".

One defect in a research note, and two leads on live pages that are not verified defects:

1. `obsidian/research/self-model-theory-of-subjectivity-2026-07-11.md` dates the Précis **2004** (`grep -c 2004` = 5 lines, including the Key Sources heading, the timeline row and the citation). The PDF header says June 2005. A research note, so low priority; do not let the 2004 date travel into an article.
2. **Lead, not a correction**: `obsidian/topics/social-construction-of-self-vs-phenomenal-self.md` (L103 at the time of reading) argues that "Metzinger's 'no one' who is fooled by the self-model is either no one at all (in which case there is no illusion) or someone". The page already marks the premise as a Map commitment. What it lacks is Metzinger's own published answer to this dilemma, which takes neither horn: the "illusion" description is one he rejects (2006e), and what self-refers is "the system as a whole" (2006a). Only the cut line was read here, not the whole page; a reviewer should read it in full before editing.
3. **Lead, not a correction**: `obsidian/concepts/self-and-self-consciousness.md` (L115) summarises "Metzinger: self-model dissolution removes the subject entirely." The 2006 replies distinguish the phenomenal self from the system that generates it ("We are systems transiently generating phenomenal selves"), so "the subject" there is ambiguous between the two. The page is at 3,497 of 3,500 words; any edit must be length-neutral.

## Binding Guards for Any Writer

**Author stances**

- **Himma does not argue for dualism.** He argues that SMT "fails to refute dualism" and explicitly denies that his argument implies substance dualism. His personal remark that substance dualism is "far more appealing" than identity theory is an aside and must not be reported as his thesis. Do not call him a dualist.
- **Zahavi rejects substantial selves** in the same paper the Map would cite for him. Do not present him as defending a subject of the kind Tenet 4's indexical objection needs; the minimal self is a structural feature of experience.
- **Gallagher, Legrand, Ghin and Livet are naturalist or naturalism-compatible critics.** None supports a non-physical subject. Gallagher's objection is that Metzinger is too Cartesian.
- **Hobson is a physicalist** defending first-person report as data. Weisberg is a higher-order-theory sympathiser offering a friendly amendment.
- **Metzinger did not concede the eliminative thesis** to anyone. His concessions are methodological (unargued scientific realism; facile psychopathology; many of Weisberg's points; no position on non-representational phenomenal character). Do not write that the symposium "forced a retreat".
- **Do not describe Metzinger's view as "the self is an illusion"** without recording that he calls this a misreading (replies to Legrand, Zahavi and Gallagher). The same goes for "you are your self-model".
- Rivals' critics are not the Map's allies. The only paper whose argument runs parallel to the Map's is Himma's, and it is parallel because it shares the premise.

**Quote status**

- Every string tagged [raw] had count 1 in the fetched text on 2026-11-12. Re-fetch and re-grep before publishing; collapse whitespace and normalise curly quotes and dashes first. Strings tagged "across page break" will count 0 unless page footers are stripped.
- "sic": Himma's "is not a simply a difference in number" is printed that way. Zahavi's abstract has "arguable" for "arguably"; Weisberg's has "ABSTRCT".
- Hobson's quotation of BNO p. 591 and all "(p. N)" locators for BNO are second-hand. The book was not opened.
- Paraphrases in this note marked "read in context" are not quotations.
- No page numbers within an issue exist. Cite volume and issue. Do not cite "PSYCHE 11(5), 1-20" style ranges for the commentaries unless the house style treats per-article pagination as a range (the live page does this for the Précis; be consistent or drop it).

**What was not read**

- *Being No One* itself; Zahavi's *Subjectivity and Selfhood* (which Metzinger's reply cites as 2006, the Map as 2005); Weisberg's 2003 JCS review; Jordan and Ghin (2006).
- The commentaries were read at the abstract, the argumentative core and the conclusion, with Himma's section 4 and Zahavi's sections 4 to 5 read closely. Livet's and Weisberg's middle sections and most endnotes were skimmed or skipped. The eight replies were read in full.
- Later literature on the exchange was not searched. Whether Himma, Zahavi or others published rejoinders is unknown.

## Gaps in Research

- No check of whether the indexical/twin argument against SMT has a later literature (Himma published related papers on phenomenal selfhood; unverified lead).
- The issue number of the reply to Zahavi is unresolved (header 12(2), footer 12(4)).
- PhilPapers metadata not obtained (403).

## Citations

- Gallagher, S. (2005). Metzinger's matrix: Living the virtual life with a real body. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaadb.pdf
- Ghin, M. (2005). What a self could be. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaade.pdf
- Himma, K. E. (2005). The problem of explaining phenomenal selfhood: A comment on Thomas Metzinger's self-model theory of subjectivity. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaadc.pdf
- Hobson, A. (2005). Finally some one: Reflections on Thomas Metzinger's "Being No One". *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaada.pdf
- Legrand, D. (2005). Transparently oneself. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaadd.pdf
- Livet, P. (2005). What is transparency? *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaadf.pdf
- Metzinger, T. (2005). Précis: Being No One. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaad5.pdf
- Metzinger, T. (2006a). Reply to Gallagher: Different conceptions of embodiment. *PSYCHE*, 12(4). https://web.archive.org/web/20090912155423/http://psyche.cs.monash.edu.au/symposia/metzinger/reply_to_Gallagher.pdf
- Metzinger, T. (2006b). Reply to Ghin: Self-sustainment on the level of global availability. *PSYCHE*, 12(4). https://journalpsyche.org/files/0xaafb.pdf
- Metzinger, T. (2006c). Reply to Himma: Personal identity and Cartesian intuitions. *PSYCHE*, 12(4). https://journalpsyche.org/files/0xaafc.pdf
- Metzinger, T. (2006d). Reply to Hobson: Can there be a first-person science of consciousness? *PSYCHE*, 12(4). https://journalpsyche.org/files/0xaafd.pdf
- Metzinger, T. (2006e). Reply to Legrand: Content from the inside out. *PSYCHE*, 12(4). https://journalpsyche.org/files/0xaafe.pdf
- Metzinger, T. (2006f). Reply to Livet: Meta-abeyance? *PSYCHE*, 12(4). https://journalpsyche.org/files/0xaaff.pdf
- Metzinger, T. (2006g). Reply to Weisberg: No direction home—searching for neutral ground. *PSYCHE*, 12(4). https://journalpsyche.org/files/0xab00.pdf
- Metzinger, T. (2006h). Reply to Zahavi: The value of historical scholarship. *PSYCHE*, 12 (header: issue 2, May 2006; footers: issue 4). https://journalpsyche.org/files/0xaaf1.pdf
- Weisberg, J. (2005). Consciousness constrained: A commentary on *Being No One*. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaad9.pdf
- Zahavi, D. (2005). Being someone. *PSYCHE*, 11(5). https://journalpsyche.org/files/0xaad8.pdf
- Symposium contents page: http://web.archive.org/web/20061108063454/http://psyche.cs.monash.edu.au:80/symposia/metzinger/ (Wayback Machine). Volume listings: https://journalpsyche.org/archive/volume-11-2005/ and https://journalpsyche.org/archive/volume-12-2006/