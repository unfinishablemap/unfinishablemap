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
- computational creativity evaluation: Ritchie criteria, Colton creative tripod, critiques
- generative music evaluation: listening studies, Turing tests, methodological weaknesses
- machine aesthetic judgment; computational aesthetic evaluation vs generation
- music models: long-range structure limits; probing for encoded music theory

## Scope Note (read first)

This note serves one specific, pre-verified gap. `obsidian/topics/phenomenology-of-musical-understanding.md` L127 lists, among the things that would *challenge* the Map's own view, the possibility that "AI systems demonstrated genuine musical understanding," adding that "the difficulty is specifying what would count as genuine understanding versus sophisticated pattern matching." It routes the reader to `topics/machine-consciousness.md` and `concepts/ai-consciousness-typology.md` for that distinction.

**The pointer exists; the content behind it does not.** Both destinations were checked on disk on 2026-08-07: each contains **zero** occurrences of "aesthetic" and **zero** of "music". The reader is sent somewhere real that is silent on the subject — that is the gap, not an absence of any destination.

**What this note deliberately does not do.** L127 states the point "marks what would have to be true, not a verdict either way." So this note characterises **what would count as satisfying the challenge** and reports **the state of the evaluation literature**. A downstream article that returned a verdict would answer a question the Map left open on purpose.

**Collision control.** Boden's combinational/exploratory/transformational typology is *already* held by `concepts/creative-consciousness.md` (L71) and `topics/consciousness-and-cognitive-distinctiveness.md` (L115) — cite it rather than re-lay it. What is genuinely absent is the **evaluation** literature (Ritchie, Colton, Jordanous and their critics) and the **production/judgement distinction**.

## Executive Summary

The field that has worked hardest on "what would count" is computational creativity evaluation, and its central finding is negative: after two decades there is no agreed criterion set, and the best-known sets demonstrably fail to exclude systems nobody regards as creative. Music is where this was diagnosed earliest — a 2002 meta-analysis found a "methodological malaise," and a 2009 paper argues the musical Turing test is the wrong instrument. The empirical picture has meanwhile moved: probing studies show music-theory concepts *are* decodable from generative models' internal representations, making a flat "surface pattern matching" claim harder to sustain, while structure-modelling reviews report long-range thematic development still unsolved. The most useful move available, and the one the corpus lacks, is the distinction between machine **production** and machine **aesthetic judgement**.

## The Operationalisation Problem

L127's difficulty — "specifying what would count as genuine understanding versus sophisticated pattern matching" — is not a gap in the Map's homework. It is the acknowledged open problem of an entire research field.

Lamb, Brown and Clarke's ACM Computing Surveys tutorial states it flatly: **"As yet, there is no consensus on how to evaluate a creative system."** They add that "many attempts at computational creativity lack rigor, especially in evaluation," and that "the reliability and validity of many of these proposals are in question."

The sharpest result is a demonstration that a proposed criterion set fails to exclude pattern matching. Lamb et al. report Bown's (2014) objection that the Creative Tripod's terms lack clear definitions and therefore "cannot be distinguished from trivial pseudo-versions of themselves," then relay Ventura's (2008) thought experiment **RASTER**: a system that generates image pixels *at random* and outputs the result if a similar image can be found online. Ventura describes RASTER as meeting all three Tripod criteria — "imagination because it engages in random search, appreciation because it uses a (simplistic) fitness function, and skill merely because it produces images."

This is exactly the shape of the problem L127 names, and it is the most valuable single import for the Map: **a criterion that a random-search-plus-retrieval system satisfies is not a criterion that distinguishes understanding from pattern matching.** Any operationalisation the Map proposes must clear the RASTER bar. Lamb et al.'s own conclusion is procedural rather than substantive — "if we have not specified just what we mean by each of our criteria, our evaluation becomes meaningless" — which itself indicates how open the question remains.

### The main criterion sets, and what is wrong with each

- **Ritchie's criteria** (2001/2007) assess generated items for typicality and value against an inspiring set. Lamb et al. report the model "has fallen out of favor," that Jordanous found it "cumbersome to implement," and that Ritchie himself "is ambivalent about attempts to use his criteria." It ignores process entirely.
- **Colton's Creative Tripod** (2008) — skill, imagination, appreciation. Critically, Lamb et al. stress that "Colton's assertion is not that a creative system must possess these qualities, but that a creative system must *appear* to possess these qualities," much of the programme being about making machines *more persuasive*. The Tripod is thus a criterion of successful attribution, not of underlying fact.
- **Jordanous's SPECS** (2012) evaluates against 14 factors distilled from how humans define creativity. Lamb et al. note that "many are impossible to evaluate without knowledge of a program's inner workings" — making SPECS inapplicable to closed commercial music models as a matter of principle, not of effort.
- **Disagreement between frameworks is measurable.** Lamb et al. report that Jordanous found the FACE model "ranked musical improvisation systems in the opposite order to other evaluation methods." Two published frameworks, same music systems, inverted rankings. When frameworks disagree this badly, a passing score licenses very little.

## How Generative Music Is Actually Evaluated

**Ariza (2009)**, "The Interrogator as Critic: The Turing Test and the Evaluation of Generative Music Systems," *Computer Music Journal* 33(2), 48–70, is the key text arguing the Turing test is the wrong instrument here. The argument, per the sources I could reach: musical judgements rest on subjective aesthetic evaluation rather than the objective reasoning the imitation game presupposes, so the interrogator functions as a *critic*, not a detector — and indistinguishability is not the success condition it is taken to be. ⚠️ **Verification limit — metadata confirmed, text not retrieved; see Gaps 1.**

**Lerch et al. (2025)**, "Survey on the Evaluation of Generative Models in Music," is the current state-of-the-field review, accepted by *ACM Computing Surveys*. It offers (verbatim) "an interdisciplinary review of the common evaluation targets, methodologies, and metrics," examining "the benefits and limitations of these approaches from a musicological, an engineering, and an HCI perspective." That a 2025 survey still catalogues benefits and limitations rather than reporting a settled protocol is itself the datum.

**Known weaknesses of listening studies**, per Lamb et al.:

- **Methodological malaise.** Pearce et al.'s (2002) meta-analysis of the music-generation literature found most researchers "neither clearly specify a motivation nor choose an appropriate evaluation method." They also argue a system built for artistic self-expression is *art and not science* — worth keeping, since only the scientific use bears on L127.
- **Anti-computer bias is weaker than commonly claimed.** This cuts *against* an easy defensive move for the Map. Moffat and Kelly (2006) found bias against computer-generated music, "but their sample size is quite small, and other ways of analyzing their data did not yield this result," and "other researchers have generally not reproduced" it — Friedman and Taylor (2014), Norton et al. (2015) and Pasquier et al. (2016) found "little overall bias against computational creativity in the general population." **An article must not lean on "listeners are just biased against machines" to discount favourable listening-study results.**
- **Judges do not share a definition.** Evaluators "expressed confusion as to what definition of creativity to use, and admitted they were likely to conflate creativity with other factors."

## What Current Architectures Do and Do Not Represent

Two findings must be held together; either alone produces an overclaim.

**Against a flat "surface pattern matching" reading.** Wei, Freeman, Donahue and Sun (2024), "Do Music Generation Models Encode Music Theory?" (ISMIR 2024), built SynTheory — a synthetic dataset of tempos, time signatures, notes, intervals, scales, chords and chord progressions — and probed Jukebox and MusicGen. Verbatim: "Our findings suggest that music theory concepts are discernible within foundation models and that the degree to which they are detectable varies by model size and layer." **This does not show phenomenal understanding, and the paper does not claim it does** — probe decodability shows information is present, not that the system uses it as a musician does, still less that anything is experienced. But an article cannot assert bare "pattern matching" without argument.

**Against an easy "they already understand" reading.** Bhandari and Colton (2024), "Motifs, Phrases, and Beyond: The Modelling of Structure in Symbolic Music Generation" (EvoMUSART 2024), review structure-modelling techniques and conclude that while progress exists in capturing motifs and repetitions, "modelling the nuanced development of themes across extended compositions in the style of human composers remains difficult." (Note that Simon Colton, of the Creative Tripod, co-authors this — the evaluation and capability literatures are one community.) Long-range thematic development, precisely the temporally extended achievement L127's durée argument concerns, is the acknowledged weak point.

The convergence is useful: **the capability current systems least reliably exhibit is the one the Map's temporal-consciousness argument predicts should be hardest.** State this as a correspondence, not a proof: architectural limits with no bearing on consciousness explain it equally well.

## Production Versus Judgement

The note's recommended organising contribution: absent from the corpus, and it dissolves a conflation L127 risks.

**Generating music and judging music are different capacities, and the literatures are separate.** Computational aesthetic evaluation — systems making normative assessments of beauty and quality — is its own research programme, surveyed in Galanter's "Computational Aesthetic Evaluation: Past and Future" (in *Computers and Creativity*, 2012). A generative model optimised for next-token prediction over an audio corpus is not thereby an aesthetic evaluator; it has a loss function, not a verdict.

Why this matters for L127: the challenge asks whether a system could *understand* music. Understanding in the aesthetically relevant sense plausibly requires the capacity to **judge** — to find a passage apt or inert, resolved or unresolved — not merely to **produce** passages others judge apt. Satisfying the challenge therefore requires evidence about the judging capacity specifically, and listening studies of *output* are the wrong evidence: they measure the audience's judgement, not the system's.

Colton's tripod already contains the relevant term — "appreciation," glossed by Smith et al. (2014) as "the ability to self-assess and produce something of worth" — and this is precisely the leg RASTER satisfies with "a (simplistic) fitness function." The distinction is recognised in the field; what is contested is any non-trivial operationalisation of it.

Hullman, Holtzman and Gelman (2023), "Artificial Intelligence and Aesthetic Judgment," argue that "encounters with the outputs of modern generative AI models are mediated by the same kinds of aesthetic judgments that organize our interactions with artwork." This concerns *our* judgements of machine output rather than machine judgement itself — a distinction an article could easily blur.

## Relation to Site Tenets

- **Dualism.** Nothing found supports or refutes the tenet. Wei et al.'s probing result shows structural representation without bearing on phenomenality — the functional/phenomenal distinction the Map already holds, arriving from a new direction.
- **Bidirectional Interaction.** Untouched; no source addresses whether aesthetic judgement is causally efficacious.
- **Occam's Razor Has Limits.** RASTER instantiates the tenet's concern in a non-consciousness domain: a criterion set simple enough to state compactly admits an obviously uncreative system.
- **Honest conflict.** The bias literature (Moffat and Kelly not replicated) removes a defence the Map might have wanted; the probing literature makes "mere pattern matching" harder to assert. Both cut against the Map's convenience and are recorded for that reason.

## Recommended Article

**Section: `concepts/`** — 5 true slots, versus 1–2 in `topics/`. Angle: *machine aesthetic judgement as distinct from machine music production*, organised around the operationalisation problem rather than a verdict. Give the understanding-versus-pattern-matching distinction a real destination, cite `concepts/creative-consciousness.md` for Boden rather than restating him, and preserve L127's non-verdict framing. Add inbound links from `topics/machine-consciousness.md` and `concepts/ai-consciousness-typology.md`, and repoint L127 at the new article.

## Gaps — Read Before Inheriting Any Citation

Flagged so they do not propagate as clean-looking prose.

1. **Ariza (2009) full text not retrieved.** Metadata confirmed twice independently (Semantic Scholar: DOI `10.1162/comj.2009.33.2.48`, DBLP key `journals/comj/Ariza09`, 2009; a search result independently gave 33(2), 48–70). But MIT Press returned HTTP 403 and Semantic Scholar reported the abstract "elided by publisher." **My characterisation of Ariza's argument rests on secondary summaries, not the text.** Obtain the paper before quoting it.
2. **Secondary citations relayed through Lamb et al.** Bown (2014), Ventura (2008)/RASTER, Ritchie (2001/2007), Colton (2008), Colton et al. (2014), Smith et al. (2014), Pearce et al. (2002), Moffat and Kelly (2006), Friedman and Taylor (2014), Norton et al. (2011/2015), Pasquier et al. (2016) and McGregor et al. (2016) are reported **as characterised by Lamb, Brown and Clarke (2018)**, whose full text I read. I did not read those primaries. Attribute accordingly ("as Lamb et al. report") or verify before quoting.
3. **Jordanous (2012) and Galanter (2012) abstracts not retrieved.** Metadata verified via OpenAlex (DOIs `10.1007/s12559-012-9156-1`, `10.1007/978-3-642-31727-9_10`); the open-access KAR copy of Jordanous failed on a TLS certificate error. SPECS content above comes from Lamb et al.'s summary.
4. **Not investigated: non-Western music.** Every framework found assumes Western tonal categories — SynTheory is explicitly Western music theory. Whether the question looks different for traditions with other temporal organisation was not searched; this bears on the Map's cross-cultural claims.
5. **Not investigated: improvisation.** Real-time interactive systems raise the temporal question more directly than offline generation.
6. **A zero I am not recording.** I did not search for philosophical work connecting *machine* aesthetic judgement to *temporal* phenomenology (specious present, durée). I therefore cannot say whether such work exists, and no article should claim the connection is unmade in the literature.

## Citations

Key: **[full text]** read in full · *[abstract]* verified at source · *[metadata]* record verified, abstract not retrieved.

- Ariza, C. (2009). "The Interrogator as Critic: The Turing Test and the Evaluation of Generative Music Systems." *Computer Music Journal* 33(2), 48–70. DOI: 10.1162/comj.2009.33.2.48 — *[metadata]*, see Gaps 1.
- Bhandari, K., & Colton, S. (2024). "Motifs, Phrases, and Beyond: The Modelling of Structure in Symbolic Music Generation." EvoMUSART 2024. arXiv:2403.07995 — *[abstract]*
- Galanter, P. (2012). "Computational Aesthetic Evaluation: Past and Future." In *Computers and Creativity*. Springer. DOI: 10.1007/978-3-642-31727-9_10 — *[metadata]*
- Hullman, J., Holtzman, A., & Gelman, A. (2023). "Artificial Intelligence and Aesthetic Judgment." arXiv:2309.12338 — *[abstract]*
- Jordanous, A. (2012). "A Standardised Procedure for Evaluating Creative Systems: Computational Creativity Evaluation Based on What it is to be Creative." *Cognitive Computation* 4(3), 246–279. DOI: 10.1007/s12559-012-9156-1 — *[metadata]*
- Lamb, C., Brown, D. G., & Clarke, C. L. A. (2018). "Evaluating Computational Creativity: An Interdisciplinary Tutorial." *ACM Computing Surveys* 51(2), Article 28. DOI: 10.1145/3167476 — **[full text]**; all quotations above checked verbatim against it.
- Lerch, A., Arthur, C., Bryan-Kinns, N., Ford, C., Sun, Q., & Vinay, A. (2025). "Survey on the Evaluation of Generative Models in Music." *ACM Computing Surveys*. arXiv:2506.05104. DOI: 10.1145/3769106 — *[abstract]*; ACM DOI confirmed via OpenAlex.
- Wei, M., Freeman, M., Donahue, C., & Sun, C. (2024). "Do Music Generation Models Encode Music Theory?" ISMIR 2024. arXiv:2410.00872 — *[abstract]*