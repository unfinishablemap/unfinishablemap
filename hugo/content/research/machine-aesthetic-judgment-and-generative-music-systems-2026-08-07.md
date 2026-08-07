---
ai_contribution: 100
ai_modified: 2026-08-07 20:28:00+00:00
ai_system: claude-opus-5
concepts: []
created: 2026-08-07
date: '2026-08-07'
draft: false
lastmod: 2026-08-07 20:28:00+00:00
related_articles: []
title: Research Notes - Machine Aesthetic Judgment and Generative-Music Systems
---

# Research: Machine Aesthetic Judgment and Generative-Music Systems

**Date**: 2026-08-07
**Search queries used**:
- evaluation of computational creativity Ritchie criteria Colton creative tripod critique
- evaluating generative music systems listening study Turing test methodology weaknesses
- philosophy machine aesthetic judgment AI art Kant judgment of taste
- computational aesthetic evaluation distinct from generation, machine appreciation, self-evaluation
- music generation models long-range structure limitation coherence transformer
- do music generation models learn music theory, probing internal representations

## Scope Note (read first)

This note serves one specific, pre-verified gap. `obsidian/topics/phenomenology-of-musical-understanding.md` L127 lists, among the things that would *challenge* the Map's own view, the possibility that "AI systems demonstrated genuine musical understanding," and adds that "the difficulty is specifying what would count as genuine understanding versus sophisticated pattern matching." It routes the reader to `topics/machine-consciousness.md` and `concepts/ai-consciousness-typology.md` for that distinction.

**The pointer exists; the content behind it does not.** Both destination articles were checked on disk on 2026-08-07: each contains **zero** occurrences of "aesthetic" and **zero** of "music". The reader is directed somewhere real that is silent on the subject they were sent to learn about. That is the gap — not an absence of any destination.

**What this note deliberately does not do.** L127 states that the point "marks what would have to be true, not a verdict either way." Accordingly this note characterises **what would count as satisfying the challenge**, and reports **the state of the evaluation literature**. It does not settle whether generative systems understand music. A downstream article that returns a verdict would answer a question the Map left open on purpose.

**Collision control.** Boden's combinational/exploratory/transformational typology is *already* held by `concepts/creative-consciousness.md` (L71) and `topics/consciousness-and-cognitive-distinctiveness.md` (L115). A new article should cite that ground rather than re-lay it. The material genuinely absent from the corpus is the **evaluation** literature (Ritchie, Colton, Jordanous, and their critics) and the **production/judgement distinction**.

## Executive Summary

The field that has worked hardest on "what would count" is computational creativity evaluation, and its central finding is negative and well-documented: after two decades there is still no agreed criterion set, and the best-known criterion sets demonstrably fail to exclude systems nobody regards as creative. Music is the sub-domain where this failure was diagnosed earliest and most sharply — a 2002 meta-analysis found a "methodological malaise," and a 2009 paper argues the musical Turing test is structurally the wrong instrument. Meanwhile the empirical picture has moved: probing studies show music-theory concepts *are* linearly decodable from generative models' internal representations, which makes a flat "mere surface pattern matching" claim harder to sustain, while structure-modelling reviews report that long-range thematic development remains unsolved. The most useful philosophical move available, and the one the corpus most lacks, is the distinction between machine **production** and machine **aesthetic judgement**: computational aesthetic evaluation is a separate research programme from generation, and a system that produces plausible music need not make aesthetic judgements at all.

## The Operationalisation Problem (the note's centrepiece)

L127's difficulty — "specifying what would count as genuine understanding versus sophisticated pattern matching" — is not a gap in the Map's homework. It is the acknowledged open problem of an entire research field, and the field has documented its own failure with unusual candour.

Lamb, Brown and Clarke's ACM Computing Surveys tutorial states it flatly: **"As yet, there is no consensus on how to evaluate a creative system."** They add that "many attempts at computational creativity lack rigor, especially in evaluation," and that of the many theoretical proposals available, "the reliability and validity of many of these proposals are in question."

The sharpest result is a formal demonstration that a proposed criterion set fails to exclude pattern matching. Lamb et al. report Bown's (2014) objection that the Creative Tripod's terms are not given clear definitions and therefore "cannot be distinguished from trivial pseudo-versions of themselves," and then relay Ventura's (2008) thought experiment **RASTER**: a system that generates image pixels *at random* and outputs the result if a similar image can be found online. Ventura describes RASTER as meeting all three Tripod criteria — "imagination because it engages in random search, appreciation because it uses a (simplistic) fitness function, and skill merely because it produces images."

This is exactly the shape of the problem L127 names, and it is the most valuable single import for the Map: **a criterion that a random-search-plus-retrieval system satisfies is not a criterion that distinguishes understanding from pattern matching.** Any operationalisation the Map proposes must clear the RASTER bar.

Lamb et al.'s own conclusion is procedural rather than substantive — "if we have not specified just what we mean by each of our criteria, our evaluation becomes meaningless" — which is itself informative about how open the question remains.

### The main criterion sets, and what is wrong with each

- **Ritchie's criteria** (2001/2007) assess generated items for typicality and value against an inspiring set. Lamb et al. report the model "has fallen out of favor in recent years," that Jordanous found it "cumbersome to implement," and that Ritchie himself "is ambivalent about attempts to use his criteria." Its blind spot is that it ignores process entirely.
- **Colton's Creative Tripod** (2008) — skill, imagination, appreciation. Critically, Lamb et al. stress that "Colton's assertion is not that a creative system must possess these qualities, but that a creative system must *appear* to possess these qualities," and that much of Colton's programme concerns making machines *more persuasive*. The Tripod is thus explicitly a criterion of successful attribution, not of underlying fact.
- **Jordanous's SPECS** (2012) evaluates against 14 factors distilled from how humans define creativity. Lamb et al. note that "many are impossible to evaluate without knowledge of a program's inner workings" — making SPECS inapplicable to closed commercial music models as a matter of principle, not of effort.
- **Disagreement between frameworks is measurable.** Lamb et al. report that Jordanous found the FACE model "ranked musical improvisation systems in the opposite order to other evaluation methods." Two published frameworks, same music systems, inverted rankings. When frameworks disagree this badly, a passing score licenses very little.

## How Generative Music Is Actually Evaluated

**Ariza (2009)** is the key text arguing that the Turing test is the wrong instrument here. Title: "The Interrogator as Critic: The Turing Test and the Evaluation of Generative Music Systems," *Computer Music Journal* 33(2), 48–70. The argument, as summarised across the sources I could reach: musical judgements rest on subjective aesthetic evaluation rather than the objective reasoning the imitation game presupposes, so an interrogator in a musical Turing test is functioning as a *critic*, not as a detector — and indistinguishability is therefore not the success condition it is taken to be. ⚠️ **Verification limit — see "Gaps" below: I confirmed this paper's metadata but could not retrieve its full text or abstract.**

**Lerch et al. (2025)**, "Survey on the Evaluation of Generative Models in Music," is the current state-of-the-field review, accepted by *ACM Computing Surveys*. It offers (verbatim from the abstract) "an interdisciplinary review of the common evaluation targets, methodologies, and metrics… covering subjective and objective approaches, qualitative and quantitative approaches, as well as empirical and computational methods," examining "the benefits and limitations of these approaches from a musicological, an engineering, and an HCI perspective." That a 2025 survey is still cataloguing benefits and limitations across three disciplines rather than reporting a settled protocol is itself the relevant datum.

**Known weaknesses of listening studies**, per Lamb et al.:

- **Methodological malaise.** Pearce et al.'s (2002) meta-analysis of the music-generation literature found that most researchers "neither clearly specify a motivation nor choose an appropriate evaluation method." Pearce et al. also argue that a system built for artistic self-expression is *art and not science* and should not be assessed as though it were evidence about cognition — a distinction the Map should keep, since only the scientific use bears on L127.
- **Anti-computer bias is weaker than commonly claimed.** This one cuts *against* an easy defensive move for the Map. Lamb et al. report that Moffat and Kelly (2006) found bias against computer-generated music, "but their sample size is quite small, and other ways of analyzing their data did not yield this result," and that "other researchers have generally not reproduced" it — with Friedman and Taylor (2014), Norton et al. (2015) and Pasquier et al. (2016) finding "little overall bias against computational creativity in the general population." McGregor et al. (2016) found framing information does not significantly affect ratings. **An article must not lean on "listeners are just biased against machines" to discount favourable listening-study results.**
- **Judges do not share a definition.** Lamb et al. report evaluators "expressed confusion as to what definition of creativity to use, and admitted they were likely to conflate creativity with other factors."

## What Current Architectures Do and Do Not Represent

Two findings that must be held together, because taking either alone produces an overclaim.

**Against a flat "surface pattern matching" reading.** Wei, Freeman, Donahue and Sun (2024), "Do Music Generation Models Encode Music Theory?" (ISMIR 2024), built SynTheory — a synthetic dataset of tempos, time signatures, notes, intervals, scales, chords and chord progressions — and probed Jukebox and MusicGen. Verbatim from the abstract: "Our findings suggest that music theory concepts are discernible within foundation models and that the degree to which they are detectable varies by model size and layer." Structured musical abstractions are recoverable from internal representations. **This does not show phenomenal understanding, and the paper does not claim it does** — decodability by a probe shows information is present, not that the system uses it as a musician does, still less that anything is experienced. But an article cannot assert bare "pattern matching" without argument.

**Against an easy "they already understand" reading.** Bhandari and Colton (2024), "Motifs, Phrases, and Beyond: The Modelling of Structure in Symbolic Music Generation" (EvoMUSART 2024), review structure-modelling techniques and conclude that while progress exists in capturing motifs and repetitions, "modelling the nuanced development of themes across extended compositions in the style of human composers remains difficult." (Note the authorship: Simon Colton, of the Creative Tripod, co-authors the structure review — the evaluation and capability literatures are the same community.) Long-range thematic development — precisely the temporally extended achievement L127's durée argument concerns — is the acknowledged weak point.

The convergence is useful and non-obvious: **the capability that current systems least reliably exhibit is the one the Map's temporal-consciousness argument predicts should be hardest.** This is a genuine point of contact, and it is stated as a correspondence rather than a proof. It could be explained equally well by architectural limits with no bearing on consciousness, and an article should say so.

## Production Versus Judgement (the most useful distinction available)

This is the note's recommended organising contribution, because it is absent from the corpus and it dissolves a conflation L127 is exposed to.

**Generating music and judging music are different capacities, and the literatures are separate.** Computational aesthetic evaluation — systems making normative assessments of beauty and quality — is its own research programme, surveyed in Galanter's "Computational Aesthetic Evaluation: Past and Future" (in *Computers and Creativity*, 2012). A generative model optimised for next-token prediction over an audio corpus is not thereby an aesthetic evaluator; it has a loss function, not a verdict.

Why this matters for L127: the challenge asks whether a system could *understand* music. Understanding in the aesthetically relevant sense plausibly requires the capacity to **judge** — to find a passage apt or inert, resolved or unresolved — and not merely to **produce** passages that others judge apt. **A system that generates plausible music need not make aesthetic judgements at all.** So satisfying the challenge requires evidence about the judging capacity specifically, and listening studies of *output* are the wrong evidence for it: they measure the audience's judgement, not the system's.

Note that Colton's tripod already contains the relevant term — "appreciation," glossed by Smith et al. (2014) as "the ability to self-assess and produce something of worth" — and that this is precisely the leg RASTER satisfies with "a (simplistic) fitness function." The distinction is recognised in the field; what is contested is any non-trivial operationalisation of it.

On the philosophical side, Hullman, Holtzman and Gelman (2023), "Artificial Intelligence and Aesthetic Judgment," argue that "encounters with the outputs of modern generative AI models are mediated by the same kinds of aesthetic judgments that organize our interactions with artwork." Note this concerns *our* judgements of machine output rather than machine judgement itself — a distinction an article could easily blur.

## Relation to Site Tenets

- **Dualism.** Nothing found either supports or refutes the tenet. Wei et al.'s probing result shows structural representation without bearing on phenomenality — the functional/phenomenal distinction the Map already holds, arriving from a new direction.
- **Bidirectional Interaction.** Untouched; no source addresses whether aesthetic judgement is causally efficacious.
- **Occam's Razor Has Limits.** RASTER is a clean instance of the tenet's concern in a non-consciousness domain: a criterion set simple enough to state compactly admits an obviously uncreative system. Simplicity in criterion design bought a false positive.
- **Honest conflict.** The bias literature (Moffat and Kelly not replicated) removes a defence the Map might have wanted; the probing literature makes "mere pattern matching" harder to assert. Both cut against the Map's convenience and are recorded for that reason.

## Recommended Article

**Section: `concepts/`** — 5 true slots at last count, versus 1–2 in `topics/`. Suggested angle: *machine aesthetic judgement as distinct from machine music production*, organised around the operationalisation problem rather than a verdict. It should discharge L127's pointer by giving the understanding-versus-pattern-matching distinction a real destination, cite `concepts/creative-consciousness.md` for Boden rather than restating him, and preserve L127's explicit non-verdict framing. Inbound links should be added from `topics/machine-consciousness.md` and `concepts/ai-consciousness-typology.md`, and L127's routing updated to point at the new article.

## Gaps in Research — Read Before Inheriting Any Citation

These are flagged so they do not propagate as clean-looking prose.

1. **Ariza (2009) full text not retrieved.** Metadata is confirmed twice independently (Semantic Scholar returned DOI `10.1162/comj.2009.33.2.48`, DBLP key `journals/comj/Ariza09`, venue *Computer Music Journal*, 2009; a search result independently gave 33(2), 48–70). But MIT Press returned HTTP 403 and Semantic Scholar reported the abstract "elided by publisher." **My characterisation of Ariza's argument above rests on secondary summaries, not on the text.** An article quoting Ariza must obtain the paper first. Do not attribute a verbatim quotation to it on the strength of this note.
2. **Secondary citations relayed through Lamb et al.** Bown (2014), Ventura (2008)/RASTER, Ritchie (2001/2007), Colton (2008), Colton et al. (2014), Smith et al. (2014), Pearce et al. (2002), Moffat and Kelly (2006), Friedman and Taylor (2014), Norton et al. (2011/2015), Pasquier et al. (2016) and McGregor et al. (2016) are all reported **as characterised by Lamb, Brown and Clarke (2018)**, whose full text I did read. I did not read those primary sources. Attribute accordingly ("as Lamb et al. report") or verify before quoting directly.
3. **Jordanous (2012) and Galanter (2012) abstracts not retrieved.** Metadata verified via OpenAlex (DOIs `10.1007/s12559-012-9156-1` and `10.1007/978-3-642-31727-9_10`). The open-access KAR copy of Jordanous failed on a TLS certificate error; ACM returned 403. SPECS content above comes from Lamb et al.'s summary.
4. **Not investigated: non-Western music.** All evaluation frameworks found assume Western tonal categories — SynTheory is explicitly "Western music theory." Whether the understanding question looks different for traditions with other temporal organisation was not searched. This bears on the Map's cross-cultural claims elsewhere.
5. **Not investigated: improvisation specifically.** Real-time interactive systems raise the temporal question more directly than offline generation. Not covered.
6. **A zero I am not recording.** I did not search for philosophical work explicitly connecting *machine* aesthetic judgement to *temporal* phenomenology (specious present, durée). I therefore cannot say whether such work exists, and no article should claim the connection is unmade in the literature.

## Citations

- Ariza, C. (2009). "The Interrogator as Critic: The Turing Test and the Evaluation of Generative Music Systems." *Computer Music Journal* 33(2), 48–70. DOI: 10.1162/comj.2009.33.2.48 — *metadata verified; full text not retrieved (see Gaps 1).*
- Bhandari, K., & Colton, S. (2024). "Motifs, Phrases, and Beyond: The Modelling of Structure in Symbolic Music Generation." EvoMUSART 2024. arXiv:2403.07995 — *abstract verified at arXiv.*
- Galanter, P. (2012). "Computational Aesthetic Evaluation: Past and Future." In *Computers and Creativity*. Springer. DOI: 10.1007/978-3-642-31727-9_10 — *metadata verified via OpenAlex; abstract not retrieved.*
- Hullman, J., Holtzman, A., & Gelman, A. (2023). "Artificial Intelligence and Aesthetic Judgment." arXiv:2309.12338 — *abstract verified at arXiv.*
- Jordanous, A. (2012). "A Standardised Procedure for Evaluating Creative Systems: Computational Creativity Evaluation Based on What it is to be Creative." *Cognitive Computation* 4(3), 246–279. DOI: 10.1007/s12559-012-9156-1 — *metadata verified via OpenAlex; abstract not retrieved.*
- Lamb, C., Brown, D. G., & Clarke, C. L. A. (2018). "Evaluating Computational Creativity: An Interdisciplinary Tutorial." *ACM Computing Surveys* 51(2), Article 28, 34 pages. DOI: 10.1145/3167476 — **full text retrieved and read; all quotations above verified verbatim against it.**
- Lerch, A., Arthur, C., Bryan-Kinns, N., Ford, C., Sun, Q., & Vinay, A. (2025). "Survey on the Evaluation of Generative Models in Music." *ACM Computing Surveys*. arXiv:2506.05104. DOI: 10.1145/3769106 — *abstract verified at arXiv; ACM DOI confirmed via OpenAlex.*
- Wei, M., Freeman, M., Donahue, C., & Sun, C. (2024). "Do Music Generation Models Encode Music Theory?" ISMIR 2024. arXiv:2410.00872 — *abstract verified verbatim at arXiv.*