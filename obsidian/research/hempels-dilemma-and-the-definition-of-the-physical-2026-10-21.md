---
title: "Research Notes - Hempel's Dilemma and the Definition of the Physical"
created: 2026-10-21
modified: 2026-11-06
human_modified: null
ai_modified: 2026-11-06T01:41:31+00:00
draft: false
description: "Hempel's dilemma read at source and in its later literature: the horns, the six standard responses, whether it binds dualists, and what it requires of Tenet 1. A theory-relative problem, not evidence for dualism."
topics:
  - "[[causal-closure-debate-historical-survey]]"
  - "[[completeness-in-physics-under-dualism]]"
  - "[[testing-consciousness-collapse]]"
concepts:
  - "[[intrinsic-nature]]"
  - "[[causal-closure]]"
  - "[[physical-completeness]]"
  - "[[russellian-monism]]"
  - "[[ignorance-hypothesis]]"
  - "[[type-a-type-b-and-type-c-physicalism]]"
  - "[[panpsychism]]"
  - "[[concepts/materialism]]"
  - "[[ontic-structural-realism]]"
  - "[[psychophysical-laws]]"
related_articles:
  - "[[tenets]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-21
last_curated: null
last_deep_review: null
recommended_action: article
target_section: concepts
target_slug: hempels-dilemma
---

# Research: Hempel's Dilemma and the Definition of the Physical

**Date**: 2026-10-21
**Origin**: harvested P3 research-topic (todo L40), from `reviews/outer-review-2026-10-21-chatgpt-5-6-sol-pro.md` §4 and §9.4, with the convergent finding in `reviews/outer-review-synthesis-2026-10-21.md` clusters 1 and 5. Claude Opus 5.5's review (M4) raised the same complaint independently.
**Sources fetched raw and read** (every quotation below was checked by script against these files, after normalising whitespace and quote marks):
- SEP "Physicalism" (Stoljar, substantive revision of 16 Sep 2026): full HTML, §§4.1–4.7 and the bibliography.
- Montero, "Varieties of Causal Closure" (2003): newdualism.org HTML, fetched with a browser User-Agent and Accept header.
- Wilson, "On Characterizing the Physical": the **draft of 31 Mar 2005** hosted by BGSU. The published 2006 version was not read.
- Gyenis (2025), arXiv author version 2507.19834.
- Cea Jacques, *Análisis Filosófico* 39(2), 2019: redalyc PDF.
- Rorty's NDPR review of van Fraassen, *The Empirical Stance* (2002.07.07).
- The Routledge catalogue page for Stoljar, *Physicalism* (2010).
- OpenAlex and Semantic Scholar abstracts or first-page text for Crane & Mellor 1990, Stoljar 2001, Ney 2008b, Tiehen 2016, Msimang 2015, Crook & Gillett 2001, Firt, Hemmo & Shenker 2021 and Gyenis 2025.
- Crossref metadata for every paper cited.
- *Added 2026-11-06*: Montero & Papineau (2005), the English text. The source is the open PDF at Zenodo record 849905 (https://zenodo.org/records/849905/files/article.pdf). The file is the publisher's 5-page 2005 PDF, about 1,750 words by pdftotext, and it shows the journal pagination: running heads 233–237 and the footer "Analysis 65.3, July 2005, pp. 233–37". Crossref (doi:10.1093/analys/65.3.233) confirms *Analysis* 65(3): 233–237. The quotations in [Via negativa sources](#sources) were grepped in the extracted text. Quote marks and whitespace were normalised first, and the running heads were removed.

**Search queries used**:
- Wilson "On Characterizing the Physical" "no fundamental mentality".
- Crane Mellor "There is no question of physicalism".
- Ney "Physicalism as an attitude".
- Montero "The Body Problem".
- Gillett Witmer "A Physical Need".
- Hempel 1980 "Comments on Goodman's Ways of Worldmaking".
- van Fraassen "The Empirical Stance" materialism stance.
- Stoljar *Physicalism* Hempel's dilemma.
- Melnyk 1997 abstract.
- Buzaglo "Two construals of Hempel's dilemma".
- Brown 2022 NFM; Alter 2024 NFM.
- Montero & Papineau 2005 via negativa; Montero "Post-Physicalism".
  - *2026-11-06*: the English text of Montero & Papineau 2005 has since been read at Zenodo record 849905 (see the sources list above).

**Not usable**:
- PhilPapers and PhilArchive returned Cloudflare challenges or HTTP 403 to every request.
- Springer article pages returned a JavaScript challenge.
- PhilSci-Archive (Jalloh) returned a bot wall.
- The Internet Archive copy of the 1969 Nagel Festschrift is lending-restricted, and search-inside is unavailable.
- Hempel's own texts of 1969 and 1980 were therefore **not read**.

## Verdict (assess-first) {#verdict}

**Write the article: a concept page, `concepts/hempels-dilemma`, titled "Hempel's Dilemma", at about 2,300–2,600 words by `analyze_length`.**

Why a standalone page:

- **No live page treats the dilemma and its responses** (corpus counts, 11:50Z, across topics/concepts/apex/voids/positions/tenets):
  - "Crane and Mellor": 0.
  - "no fundamental mentality": 0.
  - "Firt" and "Buzaglo": 0.
  - "theory-based" (in the definitional sense): 0.
  - "post-physicalism": 0.
  - Every live use of "via negativa" (8 files) is apophatic or theological except one bibliography line (`causal-closure-debate-historical-survey` ref. 4).
  - The dilemma appears in three pages (`intrinsic-nature` L61–L65, `causal-closure` L108, `causal-closure-debate-historical-survey` L99), each in a few sentences and each borrowing Montero 2003.
- **Both 2026-10-21 outer reviewers convicted the Map's use of the dilemma.** Each faulted the inference the Map drew from it, not its existence, so the corpus needs one page that says what the dilemma does and does not license and that the three borrowing pages can point to.
- **The subject bears on the Map's own foundations, not only on physicalism.** Tenet 1 is stated in physics terms ("cannot be fully explained by physics alone", tenets L53), so the dilemma's second horn applies to it (see [the dualist's version](#dualist-version)). No page currently says so.
- **Section caps**: concepts at **362/370** by `tools.evolution.state.count_section_files("concepts")` (11:41Z). The slug `hempels-dilemma` is free in concepts (`scripts/check_slug.py`), with no archive file or redirect.

**Why not fold it into `intrinsic-nature`**:

- Its headroom is 534 words (2,965 against a hard gate of 3,500), and two P1 tasks are queued on that page.
- The dilemma is not about quiddities. Housing it there is exactly the conflation both reviewers objected to.
- The intrinsic-nature section should *shrink* to a short paragraph pointing here (see [integration](#integration)).

## Executive Summary

**What the dilemma is.**
- Hempel's dilemma is a challenge to defining "physical" by reference to physical theory.
- In the SEP's reconstruction, physicalism defined over contemporary physics is false, and physicalism defined over a future or ideal physics is "trivial".
- The SEP gives the conclusion as no clear concept of the physical, "or at least no concept that is clear enough to do the job that philosophers of mind want the physical to play".

**Where it came from.**
- Hempel raised it (1969; 1980). On Gyenis's reading (2025), the original target was the Vienna Circle's *linguistic* physicalism, not a metaphysical thesis.
- The metaphysical version, the one philosophers of mind discuss, runs through Chomsky (1968, 1986) and Hellman (1985), per Wilson's draft, and through Crane & Mellor (1990) and Melnyk (1997), whom Gyenis names as its usual sources.
- Ney (2008b) calls it "an important puzzle now frequently referred to as 'Hempel's Dilemma'".

**Not one objection but at least three.** The second horn carries different charges in different hands:
- indeterminate content (Hempel, per Wilson; Melnyk; Montero's "impossibly vague");
- triviality (SEP; Crane & Mellor's "no non-vacuous interpretation");
- Wilson's reading: a future physics might posit fundamentally mental entities, so a physics-relative definition cannot keep physicalism opposed to dualism.

**The six standard responses** (detailed in [Major Positions](#positions)):
1. Take the first horn (Melnyk's currentism).
2. Use an object-based conception (Stoljar's distinction).
3. Use the via negativa or a no-fundamental-mentality constraint (Spurrett & Papineau; Montero; Wilson; Tiehen).
4. Use a structuralist, logico-mathematical-causal-nomological vocabulary (Alter, Chalmers, Goff; criticised by Stoljar).
5. Treat physicalism as an attitude or stance (van Fraassen; Ney).
6. Deflate the dilemma: failure of one style of analysis is not failure of the concept (Stoljar, in the SEP and in *Physicalism* 2010).

**Calibration, binding on any article.**
- The dilemma is a problem for theory-relative definitions of "physical".
- It is **not** evidence for dualism, for quiddities, or against causal closure.
- Montero, the Map's main source, judges it "alone, is not fatal to definitions of the physical in terms of physics".

**What it means for the Map** (developed in [the dualist's version](#dualist-version)).
- Firt, Hemmo & Shenker (2021) argue that the dilemma "also applies to mind–body dualistic theories". Buzaglo (2024) replies that dualism largely escapes.
- For the Map the dilemma cuts both ways. Tenet 1 inherits the second horn: if a future physics wrote consciousness into its dynamics, "cannot be fully explained by physics alone" would become false by definition while the Map's interactionism stayed true.
- The Map's best move is the one Montero recommends: state the thesis in mental/non-mental terms. **Consciousness is a fundamental, non-derivative feature of reality, and it makes a causal difference to physical outcomes.** That thesis is determinate whatever physics becomes, and it is what the Map's tenets need.

## Terminology and Coinage {#coinage}

- **The dilemma is Hempel's, but his two texts (1969, 1980) were not read.**
  - The SEP credits the "classic formulation" to "Hempel (cf. Hempel 1969, see also Crane and Mellor 1990)".
  - Montero 2003 cites Hempel 1980, *Synthese* 45: 193–194.
  - Wilson's 2005 draft cites the 1980 piece as "Hempel, Carl, 1979" ("Comment at a Symposium on Nelson Goodman's *Ways of Worldmaking*", APA meeting). The 1979 date is the symposium; *Synthese* 45(2) is the 1980 print.
- **Hempel's target was linguistic.** Gyenis 2025 (arXiv, verified): "Even though the dilemma was christened after Carl Hempel, his original argument was neither mounted against a metaphysical thesis nor was understood as a challenge to fixing what is 'physical' by choosing a theory of physics."
  - Gyenis identifies the target as the Neurath–Carnap claim that physics' language can serve as a unitary language of science (Hempel 1980, 194–195).
  - Wilson's draft adds, in fn. 2, that Hempel "clearly had the first reading in mind": indeterminate content, not triviality.
  - An article should say Hempel posed it against the unity-of-science physicalism of the Vienna Circle, and that the metaphysical version is a later adaptation.
- **Who named it is unsettled. Do not credit the label to anyone.**
  - A search summary of the PhilArchive abstract of Melnyk 1997 says the paper "introduces the term 'Hempel's Dilemma'". That abstract was seen only through the summariser and is **not raw-verified**. The OpenAlex abstract (French, Philosopher's-Index style) says only that Melnyk proposes to resolve "le dilemme de Hempel".
  - Montero 2003 writes "what has come to be known as Hempel's dilemma" (verified).
  - Ney 2008b writes "now frequently referred to as 'Hempel's Dilemma'" (verified).
  - Safe wording: "what has come to be called Hempel's dilemma".
- **"Via negativa" in this debate.**
  - Spurrett & Papineau (1999) offered the move: define "physical" as "non-mental" in answer to Hempel (Cea Jacques 2019, p. 113, verified, in Spanish).
  - The earliest appearance of the *label* found is the title of Gillett & Witmer 2001, "A 'Physical' Need: Physicalism and the Via Negativa". That paper is a critique.
  - The SEP calls it "the so-called Via Negativa (see e.g. Montero and Papineau 2005, Wilson 2006, Fiorese 2016)".
  - *2026-11-06, from the English text*: Montero & Papineau 2005 credit the move to Spurrett & Papineau, who "have suggested that physicalists can respond by equating 'physical' with 'non-mental'" (p. 233). When they report Gillett & Witmer's objection, they put the label in quotation marks: "Hempel's Dilemma bites just as strongly against the 'via negativa' reading" (p. 233). That fits the finding above that Gillett & Witmer 2001 is the earliest print use found. It does not settle who coined the label.
  - Credit the *idea* to Spurrett & Papineau (1999) and Montero (1999, 2001). Credit no one with coining the label.
- **"No fundamental mentality" (NFM) is Wilson's label.** The SEP: "what Wilson 2006 calls the 'no fundamental mentality' constraint".
  - Her 2005 draft says she had endorsed the account in prior work: "Wilson forthcoming", which is "Supervenience-based Formulations of Physicalism", *Noûs*.
  - Cite Wilson 2006 for the developed account and the label.
- **"Theory-based" and "object-based" conception.** Stoljar drew the distinction and named it (2001, *PPR* 62(2): 253–281; abstract verified).
  - The *object-based* conception itself is older. The SEP lists "Meehl and Sellars 1956 and Feigl 1967" as its best examples and Jackson 1998 as a recent defender.
  - Do not call the object-based conception "Stoljar's view" without saying he systematised a distinction he did not originate.
- **"Stoljar's dilemma"** is Fiorese's label (2016 title) for a modal variant: "a dilemma that is similar to Hempel's but which casts the issue in modal rather than temporal terms, see Stoljar 2010" (SEP, verified).
- **"Physicalism as an attitude"** is Ney's title (2008a). The SEP pairs it with van Fraassen 2002, who argues that *materialism* is a stance. Van Fraassen is an empiricist critic of materialism, not a physicalist.

## Key Sources {#sources}

### SEP, "Physicalism" (Stoljar), §§4.1–4.7
- **URL**: https://plato.stanford.edu/entries/physicalism/ (substantive revision 16 Sep 2026)
- **Type**: Encyclopedia.
- **Verified quotations**:
  - §4.3: "if physicalism is defined via reference to contemporary physics, then it is false — after all, who thinks that contemporary physics is complete? — but if physicalism is defined via reference to a future or ideal physics, then it is trivial — after all, who can predict what a future physics contains? Perhaps, for example, it contains even mental items."
  - §4.3: "The conclusion of the dilemma is that one has no clear concept of a physical property, or at least no concept that is clear enough to do the job that philosophers of mind want the physical to play."
  - §4.3, the deflationary response: "what it shows, if it shows anything, is that a particular proposal about how to define a physical property — namely, via reference to physics at a particular stage of its development — is mistaken."
- **Objections the entry runs**:
  - **Against currentism (§4.3)**: whether a theory is true is contingent, but whether a property is physical is not. Impetus physics is false, yet impetus is a physical property, and a world described by impetus physics would make physicalism true.
  - **The panpsychism problem for the object-based conception (§4.4).**
  - **Against the via negativa (§4.5)**:
    - élan vital is neither mental nor physical;
    - an identity theory makes pain both mental and physical;
    - against the NFM version: a world whose fundamental properties are "both mental and physical" "doesn't seem to be impossible" and should not be ruled out "simply as a matter of the definition of the words".
  - **Structuralism (§4.6)** "provides an answer to Hempel's dilemma" but is "overly stringent", because physics talks of mass, energy and electrons, not only topic-neutral structure.
  - **Attitude views (§4.7)**: the attitude is neither necessary (Democritus had no physics to defer to) nor sufficient (Ney's own year-3000 scenario, in which physicists introduce irreducible mental entities).
- **Bibliographic flags**:
  - Hempel 1980's pages are misprinted as "139–199". The correct range is 193–199 (Crossref, OpenAlex).
  - Montero 2015 "Russellian Physicalism" is in Alter & Nagasawa (eds), pp. 209–223.
- **Author stance**: Stoljar is a physicalist of a kind (the [[ignorance-hypothesis]]). His "Hempel's dilemma is a mistake" thesis is the AJP reviewer's summary of *Physicalism* (2010), quoted on the Routledge page (raw). Chapter 5 of that book is titled "Hempel's Dilemma".
- **Tenet alignment**: neutral on the dilemma. §4.5's objection to NFM matters for the Map (see [dualist's version](#dualist-version)).

### Montero (2003), "Varieties of Causal Closure"
- **URL**: https://www.newdualism.org/papers/B.Montero/Varieties-of-Causal-Closure.htm
- **Type**: Chapter, in Walter & Heckmann (eds), *Physicalism and Mental Causation* (Imprint Academic).
- **Verified quotations**. The HTML copy encodes apostrophes as the cp1252 byte 0x92, which can render as "Hempels"; normalise them.
  - The horns: "if we define the physical in terms of current physics we are left with a theory we cannot defend; for according to such a view if a new particle is discovered next week it will not be physical. However, on the other hand, if we define the physical in terms of future physics we are left with a theory that is impossibly vague; for who knows what future physics will bring."
  - "Hempel's dilemma states that physicalism is not a well-formulated thesis."
  - Fn. 25: "As I see it, this dilemma, alone, is not fatal to definitions of the physical in terms of physics. For further discussion and strengthenings of Hempel's dilemma see Montero (1999)".
  - Her preferred notion: "the only useful notion of the physical, and that is, the fundamentally nonmental. For what is at stake in the debate over the mind-body problem is not whether physics or science in general can provide the fundamental building blocks of the mental, but rather whether the mental is a fundamental feature of the world."
  - On physiology's evidence for closure: "here I think the answer is not entirely clear, since it is not clear that lack of evidence for the fundamentally mental amounts to evidence that the fundamentally mental does not exist."
  - Her one "vacuous" concerns quantum events falling outside closure's scope ("CC becomes vacuously true of a large part, perhaps the whole part, of the world"). It does **not** concern completed physics.
- **Key points**:
  - Gillett & Witmer (2001) turn the dilemma on Papineau's physiological argument.
  - Montero replies that an argument stated over current *and past* physiology escapes the first horn. It still need not succeed.
  - Her alley-cat analogy (a daytime walker's lack of evidence for a night-time cat) is presented as what anti-physicalists "might argue". It is not her own verdict.
- **Tenet alignment**: congenial in framing (the mind–body question is about fundamental mentality) but **neutral in verdict**. Montero is not a dualist: she writes as a critic of how physicalism is formulated, and she has defended "Russellian Physicalism" (2015; SEP bibliography). Do not recruit her.

### Wilson, "On Characterizing the Physical" (draft of 31 Mar 2005; published *Phil. Studies* 131(1): 61–99, 2006)
- **URL (draft)**: https://WWW.BGSU.EDU/content/dam/BGSU/college-of-arts-and-sciences/philosophy/documents/conferences/2005/characterizing.pdf
- **Type**: Paper (draft read; published version unread).
- **Key points (draft)**:
  - She separates three readings of the second horn: indeterminate content (Hellman 1985), triviality (Crook & Gillett 2001, crediting Chomsky), and her own.
  - She argues that the first two are not genuine worries, because "physics" has determinate features: it is a scientific theory of effectively fundamental entities.
  - The real worry is that future physics might posit "entities that are fundamentally mental (e.g., conscious sub-atomic particles) or that bestow fundamental mentality (e.g., fundamental mental forces or interactions)" (draft p. 5).
  - Her remedy is the physics-based NFM account: physical entities are those treated, approximately accurately, by current or future physics, *and* not fundamentally mental.
  - The motivation is that physicalism must stay incompatible with panpsychism, proto-psychism *and* emergentism.
  - Her criticism of Melnyk: the Standard Model and general relativity are mutually inconsistent, so current physics is strictly false. It "makes no sense" to call a false theory "more likely than its relevant rivals", so his SR attitude cannot be the realist's attitude.
  - She resists Montero's (1999) proposal to replace "physical" with "fundamentally non-mental", because physics gives "some concrete handle" on what physicalism is about.
- **Do-not-quote**: everything above is from the draft. The often-quoted gloss "do not individually possess or bestow mentality" appears in the draft as "physical entities do not individually either possess or bestow mentality". Quote neither form as Wilson 2006 unless the published text is read. Paraphrase.
- **Tenet alignment**: Wilson is a physicalist. Her NFM is the cleanest statement of the contrast the Map needs: physicalism is false if there is fundamental mentality.

### Crane & Mellor (1990), "There Is No Question of Physicalism"
- **Type**: Paper. *Mind* 99(394): 185–206, doi:10.1093/mind/xcix.394.185 (Crossref).
- **Verified (OpenAlex first-page text)**:
  - "Physicalists believe that everything is physical: more precisely, that all entities, properties, relations, and facts are those which are studied by physics or other physical sciences."
  - "they all grant physical science a unique ontological authority: the authority to tell us what there is."
  - "We will argue both that physicalism lacks a clear and credible definition, and that in no non-vacuous interpretation is it true."
- **Key points**: secondary summaries (unverified) add that the paper argues psychology cannot be principledly separated from the physical sciences. A short reply is Robinson 1991, *Mind* 100: 135–136 (Crossref). PhilArchive lists a reprint with an added postscript (seen only via a search summary; unverified).
- **Tenet alignment**: the paper attacks *physicalism's formulation* and its claim to ontological authority. Neither author defends dualism in it. Do not cite them as dualist allies.

### Melnyk (1997), "How to Keep the 'Physical' in Physicalism"
- **Type**: Paper. *J. Phil.* 94(12): 622–637, doi:10.2307/2564597.
- **Key points**:
  - He takes the first horn: physicalism is formulated over current physics.
  - A physicalist takes the "SR attitude" toward it: regard it as true or false in virtue of the mind-independent world, and as more probable than its *relevant rivals*, not as probably true.
  - Sources: OpenAlex French abstract (raw); SEP §4.3 (raw); and Wilson's draft, which quotes pp. 623–632.
  - The book version is *A Physicalist Manifesto* (CUP 2003).
- **Do-not-quote**: Melnyk's wording reached us only through Wilson's draft.

### Firt, Hemmo & Shenker (2021), "Hempel's Dilemma: Not Only for Physicalism"
- **Type**: Paper. *Int. Stud. Phil. Sci.* 34(2): 101–129, doi:10.1080/02698595.2022.2041969. The issue year is 2021 and the DOI dates the online version 2022; Gyenis cites it as 2022.
- **Verified (abstract)**:
  - "to the extent that Hempel's Dilemma applies to physicalism it equally applies to any theory that gives a deep-structure and changeable account of our experience or of high-level theories. In particular, we will show that it also applies to mind–body dualistic theories."
  - "it is a special case of a general sceptical argument against changeable deep-structure theories in and outside science."
- **Tenet alignment**: a direct challenge to the Map. The Map posits deep-structure, changeable theory: [[psychophysical-laws]] and outcome selection at quantum indeterminacy. Full text unread.

### Buzaglo (2024), "Two construals of Hempel's dilemma: a challenge to physicalism, not dualism"
- **Type**: Paper. *Eur. J. Phil. Sci.* 14(2), article 26, doi:10.1007/s13194-024-00590-9 (Crossref).
- **Key points (PhilArchive abstract, seen only via a search summariser; NOT raw-verified)**:
  - There are two versions of the dilemma. The general-sceptical one rests on the pessimistic induction and hits all changeable deep-structure theories. The non-sceptical one rests on the specific instability of current physics and hits mainly unstable theories with *exclusionary ambitions*.
  - Dualism largely escapes both, because theories of the mental are stable and non-exclusionary.
  - Physicalism is uniquely exposed.
- **Do-not-quote**: everything. Paraphrase only, and say the paper is a reply to Firt et al.
- **Tenet alignment**: congenial in conclusion, but see [the dualist's version](#dualist-version). The Map is *not* the non-exclusionary dualism Buzaglo describes.

### Gyenis (2025), "Empirical structure physicalism and realism, Hempel's dilemma, and an optimistic meta-induction"
- **Type**: Paper. *Synthese* 206(2), doi:10.1007/s11229-025-05160-x. The arXiv author version 2507.19834 was read in full; the published text was not.
- **Key points**:
  - "Empirical structure physicalism": the current special sciences supervene on current and on future physics, in a defined sense of empirical structure. Gyenis argues it avoids both horns (abstract verified).
  - §6.2 distinguishes *empirical structure dualism* (current mental theories do not supervene on physics) from *metaphysical dualism*.
  - He concedes that metaphysical dualism is logically compatible with his physicalism. He assigns their conjunction low confidence by an "Occam's Contrastive Razor", which he defines in §6.2.
- **Bibliographic flag**: his reference list misdates Hempel 1969 into the 1949 Feigl & Sellars *Readings* (pp. 373–384). Do not copy it.
- **Tenet alignment**:
  - Tenet 5 resists the contrastive razor.
  - Tenet 3's outcome selection is the point where the Map must say whether conscious influence shows up as an empirical-content difference at the physical level. If it does, empirical structure physicalism is false. If it never does, Gyenis's razor applies. See [[testing-consciousness-collapse]].

### Stoljar (2001), "Two Conceptions of the Physical"
- **Type**: Paper. *PPR* 62(2): 253–281, doi:10.1111/j.1933-1592.2001.tb00056.x.
- **Verified (abstract)**:
  - The debate "can be seen as concerning an inconsistent tetrad of theses".
  - "on the theory‐based conception, it is plausible that (2) is true and (3) is false; on the object‐based conception, it is plausible that (3) is true and (2) is false."
- **Key point**: the categorical properties of physical objects count as physical on the object-based conception but not on the theory-based one (SEP §4.1). That is the formal root of *Russellian physicalism*.
- **Tenet alignment**: this directly undercuts any Map sentence implying that quiddities are non-physical by definition.

### Ney (2008a), "Physicalism as an Attitude", and Ney (2008b), "Defining Physicalism"
- **Type**: Papers.
  - 2008a: *Phil. Studies* 138(1): 1–15, doi:10.1007/s11098-006-0006-4 (online 2006).
  - 2008b: *Phil. Compass* 3(5): 1033–1048, doi:10.1111/j.1747-9991.2008.00163.x.
- **Key points**:
  - 2008a holds that physicalism is an attitude, a commitment to form one's ontology by physics. The SEP quotes it at p. 9 and notes she means current physics. The text was unread.
  - 2008b's abstract (verified) surveys the responses to "an important puzzle now frequently referred to as 'Hempel's Dilemma'".
- **Do-not-quote**: Ney's own words, except as "quoted in the SEP".

### van Fraassen (2002), *The Empirical Stance* (Yale UP)
- **Type**: Book (ISBN 0-300-08874-4).
- **Key points** (Rorty's NDPR review, raw):
  - Materialism is a stance, not a factual thesis.
  - Defining "matter" as whatever current science talks about is pointless.
  - Materialism and empiricism are both stances, attending respectively to the content and to the procedures of science.
  - Rorty sums up van Fraassen's charge against such metaphysics as "either parochialism or triviality". **These are Rorty's words**; do not quote them as van Fraassen's.
- **Tenet alignment**: van Fraassen writes as an empiricist critic of materialism, not as a dualist, and his stance view relocates the dilemma rather than answering it.

### Via negativa sources (Spurrett & Papineau 1999; Montero & Papineau 2005; critics)
- **Spurrett & Papineau (1999)**, "A note on the completeness of 'physics'", *Analysis* 59(1): 25–29, doi:10.1093/analys/59.1.25.
- **Gillett & Witmer (2001)**, "A 'physical' need: physicalism and the via negativa", *Analysis* 61(4): 302–309, doi:10.1093/analys/61.4.302.
- **Montero & Papineau (2005)**, "A defence of the via negativa argument for physicalism", *Analysis* 65(3): 233–237, doi:10.1093/analys/65.3.233.
  - **English text open (2026-11-06)**: Zenodo record 849905 (https://zenodo.org/records/849905) holds the publisher's 2005 PDF with the journal pagination. It was read in full; see the sources list at the top of this note.
- **Content**:
  - The via negativa recasts closure as closure of the non-mental. Gillett & Witmer object that the appeal to a completed physiology falls back into the dilemma.
    - *2026-11-06, more exactly*: Gillett & Witmer run both horns on a "Physiological Thesis" (PT). Stated over present physiological theory, PT "is likely to be false". Stated over a future or ideal theory, it "is unacceptably vague and indeterminate". Montero & Papineau quote these words at p. 235 from Gillett & Witmer 2001: 306. Credit them to Gillett & Witmer.
  - Montero & Papineau reply (p. 235, quoted in Spanish by Cea Jacques 2019) that the appeal to physiology only directs attention to the failure of empirical research to find sui generis mental causes. From that failure an inductive inference concludes they probably do not exist.
    - *Checked against the English text, 2026-11-06*: **confirmed**, including the page (p. 235), with three qualifiers.
      - (i) It is offered as a *reading* of Spurrett & Papineau, and it is narrower than "empirical research": the appeal "can be read as simply serving to direct attention to the fact that certain kinds of empirical research have so far failed to uncover evidence of sui generis mental causes" (p. 235).
      - (ii) The induction is ascribed to Spurrett & Papineau: "On the basis of this failure, Spurrett and Papineau then infer, via scientific induction, that most likely there are no such sui generis mental causes" (p. 235).
      - (iii) The paper widens the evidence beyond physiology, "The essential point is not so much that physiology has failed to find mental causes, but that no type of empirical investigation has" (p. 236), and it declines to vindicate the induction (quoted below).
  - ~~**Do-not-quote**: the English wording of Montero & Papineau. Paraphrase.~~ *Withdrawn 2026-11-06*: the English text is open at Zenodo record 849905. The quotations below were verified there and may be quoted with their pages.
- **Verified quotations (2026-11-06; Zenodo 849905, journal pagination)**:
  - p. 233: CP is "the Completeness of Physics (CP)": "Every physical event is determined, in so far as it is determined at all, by preceding physical conditions and laws."
  - p. 233, the dilemma put to CP: "if 'physical' means what is recognized by current physics, then CP is likely to be false, for historical form suggests that future research will substantially correct the ontology of current physics; on the other hand, if 'physical' is understood to refer to some future, ideal physics, then CP is irredeemably vague, since we cannot predict what future physics will bring (Hempel 1980)."
  - p. 233, the via negativa move: Spurrett & Papineau convert CP into "the Completeness of the Non-Mental (CNM)", with physicalism as the thesis that "everything that has a non-mental effect must itself be non-mental".
  - p. 234 n. 1: "we need to understand 'non-mental' as not-sui-generis-mental, and not as not-mental-at-all".
  - pp. 236–237, the scope disclaimer: "The point of this note was not to vindicate this inductive argument, which would be a substantial empirical task, but merely to establish the far more modest point that Hempel's Dilemma does not undermine the via negativa and the associated appeal to physiological evidence." The page break falls after "substantial", so "a substantial empirical task" straddles the two pages. Cite it as pp. 236–37, not p. 237 alone.
  - p. 236: the doubt about inferring absence from lack of evidence is put with the same kind of analogy as Montero 2003's alley cat: "the fact that I've never seen bats in my cellar is not good evidence that there are none, if I've only been in my cellar during the day". Their answer is the "no type of empirical investigation" widening.
- **The paper states both closure horns itself** (p. 233). It puts Hempel's Dilemma directly to CP: over current physics CP "is likely to be false", over a future, ideal physics it "is irredeemably vague". Its second-horn charge is vagueness, not triviality. Its first-horn reason is historical, that future research will correct current physics' ontology, and has nothing to do with mind. The authors use the dilemma to motivate CNM and argue that it does not reach CNM. So `concepts/intrinsic-nature` L65 now cites Montero and Papineau (2005) for the closure extension and no longer marks it as the Map's own; the 2026-10-21 deep review made that change.
- **Author stance (2026-11-06)**: both write here as defenders of the via negativa argument *for* physicalism, against the dilemma only. Do not cite the paper as endorsing the induction, and do not recruit Montero from it.
- **Critics and refiners**:
  - Worley 2006, *Phil. Studies* 131(1): 101–126.
  - Judisch 2008, "Why 'non-mental' won't work", *Phil. Studies* 140(3): 299–318.
  - Tiehen 2016, *PPR* 93(1): 3–24. The abstract (verified) defines the physical as "neither fundamentally mental nor possibly realized by a fundamentally mental property" and argues against Wilson's NFM.
  - Brown 2022, *Synthese* 201, "Quantum computation and the untenability of a 'No fundamental mentality' constraint on physicalism". Crossref only; content **unread**.
  - Alter 2024, *Synthese* 204(2), "Physicalism and fundamental mentality". The search-summarised abstract says it clarifies and defends NFM; not raw-verified.
- **Cea Jacques (2019)**, "Cierre causal de lo físico, neurofisiología y causas mentales", *Análisis Filosófico* 39(2): 111–142 (redalyc, verified). It attacks Papineau's physiological evidence using Penfield, Eccles and Libet. Cite it only as a critic of the inductive argument.

### Structuralist definitions (SEP §4.6)
- Russell 1927 restricts physical vocabulary to logic and mathematics. Contemporaries allow logical, mathematical, causal and nomological vocabulary: Alter 2016 (*Noûs* 50(4): 794–815), Chalmers 2020 (*Noûs*), Goff 2017 (*Consciousness and Fundamental Reality*, OUP). Stoljar 2020, "Chalmers v Chalmers" (*Noûs*), is the critic.
- **Author stance, and the point to make**: Alter, Chalmers and Goff are *anti-physicalists*. The structuralist definition answers Hempel's dilemma, and it is the very definition on which their structure-and-dynamics argument says physicalism is **false**. A determinate definition and a refutable physicalism come together.

## Major Positions {#positions}

### Take the first horn (currentism)
- **Proponents**: Smart 1978, Lewis 1994, Melnyk 1997, 2003 (SEP §4.3). Vicente 2011 (*BJPS* 62(2): 393–416) defends a broad construal of "current physics" (per a search summary; unread).
- **Core claim**: define the physical over current physics, and hold physicalism as the best available hypothesis even if it is probably false.
- **Objections**:
  - Contingency: whether a property is physical should not depend on which physics happens to be true (SEP).
  - Inconsistency: current physics is strictly false (Wilson).
- **Relation to tenets**: the Map in effect uses current physics as a reference in Tenet 2 ("the smallest deviation from standard quantum mechanics"). That use is legitimate as a *benchmark* and does not commit the Map to currentism about the physical.

### Object-based conception
- **Proponents**: Meehl & Sellars 1956; Feigl 1967; Jackson 1998. Stoljar 2001 and 2010 named and systematised the theory/object distinction.
- **Core claim**: a property is physical if it is "the sort of property had by paradigmatic physical objects and their constituents" (SEP).
- **Problem**: the panpsychism problem. If rocks were fundamentally conscious, physicalism on this definition could come out true.
- **Relation to tenets**: this conception licenses Russellian physicalism and makes quiddities physical. It is why `intrinsic-nature` must not treat "physical" as synonymous with "structural".

### Via negativa / no fundamental mentality
- **Proponents**:
  - Spurrett & Papineau 1999; Montero 1999, 2001, 2003; Montero & Papineau 2005.
    - *2026-11-06*: Montero & Papineau 2005 defend the via negativa *against Hempel's Dilemma only* and decline to vindicate the induction (pp. 236–237). They gloss "non-mental" as "not-sui-generis-mental" (p. 234 n. 1).
  - Wilson 2006 (physics-based NFM).
  - Tiehen 2016 (non-mental-and-not-realised-by-the-mental).
  - Fiorese 2016; Alter 2024 (defence).
- **Core claim**: whatever else "physical" means, a physical property or entity is not fundamentally mental. Montero goes furthest: drop "physical" and pose the mind–body problem as mental versus non-mental.
- **Objections**:
  - élan vital (neither mental nor physical);
  - identity theory (both);
  - a fundamental-level world that is both mental and physical, ruled out by fiat (SEP §4.5);
  - Judisch 2008;
  - Gillett & Witmer 2001 (the dilemma returns via completed physiology);
  - Brown 2022 (unread).
- **Relation to tenets**: the best fit for stating the Map's dualism, though it has costs (see [below](#dualist-version)).

### Structuralist / causal-nomological conception
- **Proponents**: Alter, Chalmers, Goff (as anti-physicalists); Russell 1927 as precursor.
- **Core claim**: physical theory is theory couched in logical, mathematical, causal and nomological vocabulary.
- **Objection**: overly stringent. "Electron" and "mass" are not obviously topic-neutral (Stoljar 2020; SEP).
- **Relation to tenets**: the conception behind [[physical-completeness]] and [[intrinsic-nature]]. It answers the dilemma by making physicalism determinate, and on Alter's, Chalmers's and Goff's arguments it makes physicalism false.

### Physicalism as attitude / stance
- **Proponents**: Ney 2008a; van Fraassen 2002 (who argues materialism is a stance, as a critic).
- **Core claim**: physicalism is a commitment to let physics settle ontology, not a truth-apt thesis.
- **Objections**:
  - It is neither necessary nor sufficient for being a physicalist (SEP).
  - The dilemma recurs over *which* physics the attitude defers to.
- **Relation to tenets**: by parity the Map could call dualism a stance. It should not. The tenets are stated as truth-apt commitments ("a commitment the Map owns", tenets L55).

### Deflation
- **Proponents**: Stoljar (SEP §4.3; *Physicalism* 2010, ch. 5).
- **Core claim**: the failure of one analysis does not show that there is no concept. We understand many concepts we cannot analyse.
- **Relation to tenets**: deflation concedes the Map nothing, and also takes nothing from it.

## Key Debates {#debates}

### Does the dilemma bind dualism too? {#dualist-version}
- **Sides**: Firt, Hemmo & Shenker 2021 (yes, wherever dualism offers deep-structure, changeable theory) against Buzaglo 2024 (dualism largely escapes).
- **The Map's position (this note's analysis, drawn by none of these authors).** The Map is exposed on two fronts that bare dualism is not.

**(a) Tenet 1's wording takes the second horn.**
- Tenet 1 says consciousness "is not reducible to physical processes" and that something "cannot be fully explained by physics alone" (tenets L53).
- **Over current physics** this is trivially true and says little: current physics also fails to "fully explain" a great deal that no one thinks non-physical.
- **Over a future physics** it risks being falsified by definition. Suppose a successor theory wrote consciousness into its dynamics, as consciousness-collapse proposals try to do (Chalmers & McQueen 2022; [[testing-consciousness-collapse]]). Consciousness would then be "explained by physics" on the theory-based conception, while the Map's interactionism stayed exactly as true as before.
- Ney's year-3000 scenario (SEP §4.7) and Chalmers's fourth collapse route for type-C (a physics "appealing to consciousness itself", [[type-a-type-b-and-type-c-physicalism]] L73) are the same case seen from the physicalist side. Chalmers files the result as type-D or type-F, with consciousness irreducible, whatever label physics gives it.
- **The repair** is to state the tenet in mental/non-mental terms. Consciousness is fundamentally mental, a non-derivative feature of reality, and it makes a causal difference to physical outcomes.
  - This is Montero's framing of what is "at stake in the debate over the mind-body problem".
  - It is also the contrast Wilson's NFM exists to protect.
  - So stated, the thesis is determinate whatever physics becomes.

**(b) The Map's mechanism claims are the deep-structure, changeable kind Firt et al. target.**
- Outcome selection at quantum indeterminacy, [[psychophysical-laws]], and the rejection of Everett all tie the Map to the volatile part of fundamental physics, the measurement problem.
- They also carry *exclusionary* ambitions: no strong closure, no many worlds.
- These are exactly the features Buzaglo says spare ordinary dualism. The Map is therefore *not* entitled to Buzaglo's conclusion for its mechanism layer, even if the bare Tenet 1 is.
- Honest wording: bare dualism, stated as a claim about fundamental mentality, escapes the dilemma. The Map's specific interface hypotheses face the general-sceptical version as much as any physical theory does. That cost is acceptable because the tenets hold them as revisable (tenets L65–L67, "the smallest deviation").

**(c) Costs of the NFM restatement for the Map.**
- It counts panpsychism and emergentism as non-physicalist. The Map should accept that, and already treats panpsychism as a rival to physicalism ([[panpsychism]]).
- It cannot by definition accommodate a world whose fundamental properties are both mental and physical (SEP §4.5). Dual-aspect and Russellian views live exactly there ([[russellian-monism]], [[bi-aspectual-ontology]], [[disguised-property-dualism]]).
- The Map should say that NFM *classifies* such views as non-physicalist rather than *refuting* them. Whether they are dualisms in disguise is argued elsewhere, not settled by a definition.

**(d) Dowell's integrated-fundamental-theory account** (reported only in Wilson's draft, §4.1; the 2006 papers are unread).
- On it, physics is the science with the hallmarks of scientific theory, among them a unified pattern of laws, whose subject matter is the most fundamental elements.
- Anything that can neither be explained and predicted nor figure in explanation and prediction counts as non-physical.
- For the Map this cuts sharply. A *law-governed* conscious influence (a psychophysical law) could count as physical on Dowell's account. A *lawless* free selection would count as non-physical.
- The Map's two strands (lawful psychophysical laws versus agent-causal selection) therefore land on different sides of this definition. This is a LEAD, to be verified at Dowell 2006a/b before use.

### Does the dilemma tell against causal closure? {#closure}
- **Sides**: no author found argues that it does.
  - *2026-11-06*: Montero & Papineau 2005 come closest. They put the dilemma to CP itself (p. 233; quoted in [Via negativa sources](#sources)), but as a reason to restate closure as the Completeness of the Non-Mental, and they argue that the dilemma does not reach that restatement. This supports the calibration below: the dilemma bears on closure stated over "physical", not on closure of the non-mental.
- Montero argues something narrower. Closure has many formulations, and the version stated over the "fundamentally nonmental" is the one that matters. Whether physiology supports it is "not entirely clear".
- Papineau (Spurrett & Papineau 1999; Montero & Papineau 2005) holds that a century of physiology supports it inductively.
  - *Qualified 2026-11-06 against the English text*: this holds for Spurrett & Papineau 1999, whom the 2005 paper quotes at p. 234 ("especially in the form of nineteenth- and twentieth-century physiological research, now weighs strongly against such irreducible mental causes"). The 2005 paper itself sets the inductive argument out and defends it against the dilemma. It widens the evidence to "no type of empirical investigation" (p. 236), and it declines "to vindicate this inductive argument, which would be a substantial empirical task" (pp. 236–237). Cite 2005 for the defence against the dilemma, not for the induction's success.
- **Current state**: open, and empirical in character.
- **Calibration**:
  - Closure stated over current physics is probably false, for reasons that have nothing to do with mind: current physics is incomplete about gravity and dark matter.
  - That falsity gives dualism nothing.
  - The live question is whether the *non-mental* is causally closed. The Map denies it, and that denial is a determinate thesis, not a vacuous one.

### Is the second horn vagueness, triviality or something else?
- **Sides**: Hellman 1985 and Melnyk 1997 (content undeterminable now); the SEP and Crook & Gillett 2001, crediting Chomsky (trivial); Crane & Mellor (no non-vacuous true interpretation); Wilson (admits fundamental mentality); Montero ("impossibly vague").
  - *2026-11-06*: add Montero & Papineau 2005 to the vagueness side. Over a future, ideal physics, CP "is irredeemably vague, since we cannot predict what future physics will bring" (p. 233).
- **Current state**: unresolved. Any article must pick a charge and attribute it. It must not run two together, as `intrinsic-nature` once did ("unfalsifiable" at L59 and "vacuous" at L61), per Claude Opus 5.5's review, M4.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1956 | Meehl & Sellars, "The Concept of Emergence" | Best early example of the object-based conception (SEP) |
| 1967 | Feigl, *The "Mental" and the "Physical"* | physical₁, which the SEP relates to the theory-based conception; Feigl is also an object-based example |
| 1969 | Hempel, "Reduction: Ontological and Linguistic Facets", in Morgenbesser, Suppes & White (eds), *Philosophy, Science, and Method: Essays in Honor of Ernest Nagel* (St Martin's), pp. 179–199 | First formulation (unread; SEP, IA metadata) |
| 1979/80 | Hempel, "Comments on Goodman's *Ways of Worldmaking*", APA symposium 1979; *Synthese* 45(2): 193–199 (1980) | The text usually cited; target was linguistic physicalism (Gyenis) |
| 1985 | Hellman, "Determination and Logical Truth", *J. Phil.* 82 | Content-indeterminacy reading (per Wilson draft) |
| 1990 | Crane & Mellor, *Mind* 99 | The metaphysical version; "no non-vacuous interpretation" |
| 1995 | Chomsky, "Language and Nature", *Mind* 104: 1–61 | Chomsky's critique of the notion of body; Montero 2003 fn. 15 pairs it with Montero 1999 |
| 1997 | Melnyk, *J. Phil.* 94 | Currentism; SR attitude |
| 1999 | Montero, "The Body Problem", *Noûs* 33(2): 183–200; Spurrett & Papineau, *Analysis* 59 | Via negativa enters |
| 2001 | Stoljar, *PPR* 62; Montero, "Post-Physicalism", *JCS* 8(2): 61–80; Gillett & Witmer, *Analysis* 61; Crook & Gillett, *CJP* 31 | Theory/object distinction; mental/non-mental reframing; first critiques |
| 2002 | van Fraassen, *The Empirical Stance* | Materialism as stance |
| 2003 | Montero, "Varieties of Causal Closure"; Melnyk, *A Physicalist Manifesto* | Dilemma applied to closure; "not fatal" |
| 2005 | Montero & Papineau, *Analysis* 65 | ~~Defence of the inductive via negativa argument~~ *(qualified 2026-11-06)* Defence of the via negativa against Hempel's Dilemma only. States both horns against CP (p. 233) and declines to vindicate the induction (pp. 236–237) |
| 2006 | *Phil. Studies* 131(1): Dowell ×2, Wilson, Worley, Melnyk | NFM; the integrated-theory account |
| 2008 | Ney ×2; Judisch | Attitude view; survey; anti-via-negativa |
| 2010 | Stoljar, *Physicalism* (Routledge), ch. 5 | Deflation; modal variant ("Stoljar's dilemma") |
| 2016 | Tiehen, *PPR* 93; Fiorese, *Erkenntnis* 81; Alter, *Noûs* 50 | Via negativa refined; structuralist definitions |
| 2018 | Elpidorou (ed.), *Topoi* 37(3) special issue | "The Character of Physicalism" |
| 2021 | Firt, Hemmo & Shenker, *ISPS* 34(2) | Dilemma extended to dualism |
| 2024 | Buzaglo, *EJPS* 14; Alter, *Synthese* 204 | Dualism largely escapes (Buzaglo); NFM defended (Alter) |
| 2025 | Gyenis, *Synthese* 206 | Empirical structure physicalism avoids both horns |

## Potential Article Angles

1. **Recommended: "Hempel's Dilemma" (concepts).** Proposed order:
   1. A lead stating the dilemma, its origin and the Map's verdict.
   2. The horns, and the three second-horn charges.
   3. The six responses, compressed and each attributed.
   4. "Does it bind the dualist?" (Firt et al. against Buzaglo).
   5. "What it asks of the Map", covering Tenet 1's restatement, the mechanism layer's exposure, and closure.
   6. "What the dilemma cannot do": not evidence for dualism, quiddities or the failure of closure.
   7. Relation to Site Perspective.

   Front-load the verdict for LLM readers. They know the dilemma; they do not know that it cuts against the dualist's own formulation, or how the Map answers.
2. **Alternative: a narrower topics page**, "Defining the non-physical", taking Tenet 1's formulation as its subject. Rejected because the dilemma itself needs the canonical page, and the restatement fits inside it.

When writing the article, follow `obsidian/project/writing-style.md`: named-anchor summaries, background only when framed for the Map, explicit tenet connections, no "This is not X. It is Y." construction.

## Guards for the Article Writer {#guards}

**Calibration (binding).**
- The dilemma is a problem for **theory-relative definitions of "physical"**. Never present it as evidence for:
  - dualism;
  - quiddities, or the claim that physics omits categorical natures;
  - permanent physical ignorance;
  - the failure of causal closure.
- Montero judges it "alone, is not fatal". The SEP's deflationary reply should be stated fairly.
- Do not write that closure over current physics being false helps dualism. The missing causes could be non-mental.
- Do not say any response "refutes" the dilemma, or that the dilemma "refutes" physicalism. Each response has a cost; give it.
- State the dualist's version symmetrically. Firt et al.'s challenge must appear, not only Buzaglo's reply.

**Author stances.**
- Montero: not a dualist. Her "post-physicalism" reframes the question, and she judges the physiological evidence "not entirely clear". Do not recruit her.
  - *2026-11-06*: the "not entirely clear" is from Montero 2003 (0 hits in the 2005 text). In 2005 she co-defended the via negativa argument *for* physicalism against the dilemma, while declining to vindicate its induction (pp. 236–237).
- Do not attribute to her an "explanatory gap" argument. That phrase has 0 hits in the 2003 text, and a P3 todo task (L2786) is open on exactly this misattribution.
- Wilson, Papineau, Melnyk, Ney, Stoljar, Tiehen, Gyenis: none is a dualist. Papineau, Melnyk, Stoljar (the [[ignorance-hypothesis]]) and Tiehen defend physicalism outright.
- Crane & Mellor: critics of physicalism's *formulation*, not dualists.
- van Fraassen: an empiricist critic of materialism, not a dualist.
- Alter, Chalmers, Goff: anti-physicalists. Goff is a panpsychist. Alter writes in the Russellian-monist programme. Chalmers stays neutral among type-D, type-E and type-F, and has co-developed a consciousness-collapse model (with McQueen); do not call him an ally of the Map's specific interface.
- Firt, Hemmo & Shenker: none writes as a dualist. Hemmo & Shenker defend "flat physicalism" (*Theoria* 88(4), 2022; Crossref).
- Buzaglo: argues dualism escapes. Present this as one author's argument, from an abstract only.

**Quote status.**
- VERIFIED: every quotation in Key Sources, against the raw source named in its entry.
- Montero's HTML encodes apostrophes as cp1252 0x92; normalise.
- Gyenis is quoted from the arXiv version; cite it as such.

**Do-not-quote list.**
- Hempel 1969 and 1980: no wording, including the Wikipedia sentence "it is quite unclear what is to be understood here by a physical phenomenon …", which is secondhand. Paraphrase via the SEP or Gyenis.
- Wilson's NFM gloss, in either form. Draft only.
- Melnyk's wording (via Wilson's draft).
- Hellman 1985, Loewer 2001 and Papineau 2001 (all via Wilson's draft).
- Ney's wording, except "as quoted in the SEP".
- ~~Montero & Papineau 2005 (known only in Spanish translation).~~ *Withdrawn 2026-11-06*: the English text is open at Zenodo record 849905, with the journal pagination, and was read in full. The verified quotations in [Via negativa sources](#sources) may be quoted with their pages: p. 233 for both horns ("CP is likely to be false"; "CP is irredeemably vague"), and pp. 236–237 for "a substantial empirical task". Words they quote from Gillett & Witmer 2001 or Spurrett & Papineau 1999 stay credited to those authors.
- Buzaglo 2024 (abstract seen only via a summariser).
- Alter 2024 and Brown 2022 (unread).
- "Either parochialism or triviality" is Rorty's phrase, not van Fraassen's.
- "Materialist metaphysicians want to side with physics, but not to take sides within physics": this opens Crook & Gillett 2001 but is one of their epigraph passages, almost certainly van Fraassen. Do not quote it as Crook & Gillett, and do not quote it as van Fraassen without reading him.

**Coiner and populariser.**
- The dilemma is Hempel's, posed against *linguistic* physicalism.
- The metaphysical version belongs to Hellman, Crane & Mellor and Melnyk.
- The label's coiner is unsettled. Write "what has come to be called Hempel's dilemma".
- The via negativa *idea* belongs to Spurrett & Papineau and Montero. The label appears in print at least by Gillett & Witmer 2001.
- "No fundamental mentality" is Wilson's label.
- The theory/object distinction is Stoljar's. The object conception predates him (Meehl & Sellars; Feigl; Jackson).
- "Stoljar's dilemma" is Fiorese's label.

**Bibliographic traps.**
- Hempel 1980's pages are **193–199**. The SEP's 139–199 is a misprint.
- Hempel 1969 is in the **Nagel Festschrift**, not in Feigl & Sellars *Readings*. Gyenis's bibliography conflates them.
- Ney 2008a has online date 2006 and print 2008.
- Firt et al.: give 2021 for the issue, with the DOI as is.
- Wilson 2006: the draft's content may differ from the print version. Cite 2006 only for the label and the general account (via the SEP).

**Section-specific.**
- Do not manufacture a Tenet 4 connection. The dilemma has none.
- Tenet 5 bears only through Gyenis's "Occam's Contrastive Razor", and only if the article discusses Gyenis.
- Keep [the closure discussion](#closure) brief and link [[causal-closure]] and [[causal-closure-debate-historical-survey]] for depth.
- Do not restate `intrinsic-nature`'s structural/categorical material. Link to it.

## Integration (for the expand-topic writer and later refines) {#integration}

Lengths below were measured 2026-10-21 11:45Z by `analyze_length`. Headroom is hard gate − 1 − count.

- **`concepts/intrinsic-nature`** (2,965; headroom 534): the section `## Hempel's Dilemma and What "Physical" Means` (L61–L65) should shrink to about 60 words plus a link, once its two P1 tasks have landed. Re-read the file first. **Fold** target.
- **`concepts/causal-closure`** (3,493; headroom **6**): at L108, turn the existing words "Hempel's dilemma" into a piped wikilink to the new `hempels-dilemma` page, at zero word cost. Nothing else.
- **`topics/causal-closure-debate-historical-survey`** (3,538 against a topics gate of 4,000; headroom 461): at L99, pipe "Hempel's dilemma" to the new page.
- **`concepts/physical-completeness`** (2,728; headroom 771): at L90, the "further modal premise" about any future physics is the second horn in all but name. Add one sentence and a link.
- **`concepts/type-a-type-b-and-type-c-physicalism`** (2,913; headroom 586): at L73, route 4 is the second-horn case. Add a link.
- **`concepts/ignorance-hypothesis`** (3,026; headroom 473): at L110, the "fourth route" sentence. Add a link.
- **`tenets/tenets`** L53: **NEEDS-HUMAN**. Restating Tenet 1 in fundamental-mentality terms is a tenet change and must not be done by automation. The article should *propose* the reading as how the Map's tenet is best understood; at most, flag a human-decision task.

## Gaps in Research

- **Hempel 1969 and 1980 were not read.** Every claim about Hempel's own argument rests on the SEP, Gyenis and Wilson's draft.
- Melnyk 1997, Crane & Mellor (beyond p. 1), Montero 1999 and 2001, Ney 2008a, Stoljar 2010, Dowell 2006a/b, Judisch 2008, Worley 2006, Vicente 2011 and Fiorese 2016 were known through abstracts, the SEP or Wilson's draft only.
- Buzaglo 2024, Brown 2022 and Alter 2024 are unread. All three bear directly on whether NFM can carry the Map's restated Tenet 1, and Brown's title suggests a quantum-computation argument against NFM that may touch Tenet 2. **Highest-value follow-up.**
- The published Wilson 2006 should be checked against the draft before any page relies on its details.
- Chalmers & McQueen 2022 is cited here only as the standard example of a consciousness-involving collapse dynamics. Its details live in [[testing-consciousness-collapse]].

## Citations

- Alter, T. (2016). The structure and dynamics argument against materialism. *Noûs* 50(4): 794–815.
- Alter, T. (2024). Physicalism and fundamental mentality. *Synthese* 204(2), art. 50. doi:10.1007/s11229-024-04697-7
- Brown, C. D. (2022). Quantum computation and the untenability of a "No fundamental mentality" constraint on physicalism. *Synthese* 201, art. 10. doi:10.1007/s11229-022-04015-z
- Buzaglo, D. (2024). Two construals of Hempel's dilemma: a challenge to physicalism, not dualism. *European Journal for Philosophy of Science* 14, art. 26. doi:10.1007/s13194-024-00590-9
- Cea Jacques, I. (2019). Cierre causal de lo físico, neurofisiología y causas mentales. *Análisis Filosófico* 39(2): 111–142. https://www.redalyc.org/articulo.oa?id=340062680003
- Chalmers, D. J. & McQueen, K. J. (2022). Consciousness and the collapse of the wave function. In S. Gao (ed.), *Consciousness and Quantum Mechanics*, pp. 11–63. OUP.
- Crane, T. & Mellor, D. H. (1990). There is no question of physicalism. *Mind* 99(394): 185–206. doi:10.1093/mind/xcix.394.185
- Crook, S. & Gillett, C. (2001). Why physics alone cannot define the 'physical'. *Canadian Journal of Philosophy* 31(3): 333–359. doi:10.1080/00455091.2001.10717571
- Dowell, J. L. (2006a). Formulating the thesis of physicalism: an introduction. *Philosophical Studies* 131(1): 1–23. doi:10.1007/s11098-006-6641-y
- Dowell, J. L. (2006b). The physical: empirical, not metaphysical. *Philosophical Studies* 131(1): 25–60. doi:10.1007/s11098-005-5983-1
- Fiorese, R. (2016). Stoljar's dilemma and three conceptions of the physical: a defence of the via negativa. *Erkenntnis* 81(2): 201–229. doi:10.1007/s10670-015-9735-0
- Firt, E., Hemmo, M. & Shenker, O. (2021). Hempel's dilemma: not only for physicalism. *International Studies in the Philosophy of Science* 34(2): 101–129. doi:10.1080/02698595.2022.2041969
- Gillett, C. & Witmer, D. G. (2001). A 'physical' need: physicalism and the via negativa. *Analysis* 61(4): 302–309. doi:10.1093/analys/61.4.302
- Gyenis, B. (2025). Empirical structure physicalism and realism, Hempel's dilemma, and an optimistic meta-induction. *Synthese* 206(2), art. 76. doi:10.1007/s11229-025-05160-x (arXiv:2507.19834)
- Hempel, C. G. (1969). Reduction: ontological and linguistic facets. In S. Morgenbesser, P. Suppes & M. White (eds), *Philosophy, Science, and Method: Essays in Honor of Ernest Nagel*, pp. 179–199. New York: St Martin's Press.
- Hempel, C. G. (1980). Comments on Goodman's *Ways of Worldmaking*. *Synthese* 45(2): 193–199. doi:10.1007/BF00413558
- Judisch, N. (2008). Why 'non-mental' won't work: on Hempel's dilemma and the characterization of the 'physical'. *Philosophical Studies* 140(3): 299–318 (online 2007). doi:10.1007/s11098-007-9142-8
- Melnyk, A. (1997). How to keep the 'physical' in physicalism. *Journal of Philosophy* 94(12): 622–637. doi:10.2307/2564597
- Melnyk, A. (2003). *A Physicalist Manifesto: Thoroughly Modern Materialism*. Cambridge University Press.
- Montero, B. (1999). The body problem. *Noûs* 33(2): 183–200. doi:10.1111/0029-4624.00149
- Montero, B. (2001). Post-physicalism. *Journal of Consciousness Studies* 8(2): 61–80.
- Montero, B. (2003). Varieties of causal closure. In S. Walter & H.-D. Heckmann (eds), *Physicalism and Mental Causation*. Imprint Academic. https://www.newdualism.org/papers/B.Montero/Varieties-of-Causal-Closure.htm
- Montero, B. & Papineau, D. (2005). A defence of the via negativa argument for physicalism. *Analysis* 65(3): 233–237. doi:10.1093/analys/65.3.233. Open English text: https://zenodo.org/records/849905 (read 2026-11-06).
- Msimang, P. M. (2015). Problems with the 'physical' in physicalism. *South African Journal of Philosophy* 34(3): 336–345. doi:10.1080/02580136.2015.1069662
- Ney, A. (2008a). Physicalism as an attitude. *Philosophical Studies* 138(1): 1–15. doi:10.1007/s11098-006-0006-4
- Ney, A. (2008b). Defining physicalism. *Philosophy Compass* 3(5): 1033–1048. doi:10.1111/j.1747-9991.2008.00163.x
- Rorty, R. (2002). Review of van Fraassen, *The Empirical Stance*. *Notre Dame Philosophical Reviews* 2002.07.07. https://ndpr.nd.edu/reviews/the-empirical-stance/
- Spurrett, D. & Papineau, D. (1999). A note on the completeness of 'physics'. *Analysis* 59(1): 25–29. doi:10.1093/analys/59.1.25
- Stoljar, D. (2001). Two conceptions of the physical. *Philosophy and Phenomenological Research* 62(2): 253–281. doi:10.1111/j.1933-1592.2001.tb00056.x
- Stoljar, D. (2010). *Physicalism*. London: Routledge.
- Stoljar, D. (2026). Physicalism. *Stanford Encyclopedia of Philosophy* (substantive revision 16 Sep 2026). https://plato.stanford.edu/entries/physicalism/
- Tiehen, J. (2016). Physicalism requires functionalism: a new formulation and defense of the via negativa. *Philosophy and Phenomenological Research* 93(1): 3–24. doi:10.1111/phpr.12279
- van Fraassen, B. C. (2002). *The Empirical Stance*. New Haven: Yale University Press.
- Vicente, A. (2011). Current physics and 'the physical'. *British Journal for the Philosophy of Science* 62(2): 393–416. doi:10.1093/bjps/axq033
- Wilson, J. (2006). On characterizing the physical. *Philosophical Studies* 131(1): 61–99. doi:10.1007/s11098-006-5984-8 (draft of 31 Mar 2005 read at BGSU)
- Worley, S. (2006). Physicalism and the via negativa. *Philosophical Studies* 131(1): 101–126. doi:10.1007/s11098-005-5985-z
