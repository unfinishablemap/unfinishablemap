---
title: "Deep Review - The Thrownness Void"
created: 2026-11-27
modified: 2026-11-27
human_modified: null
ai_modified: 2026-11-27T08:56:31+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-27
last_curated: null
---

**Date**: 2026-11-27
**Article**: [[thrownness-void|The Thrownness Void]]
**Previous review**: [[deep-review-2026-07-19-thrownness-void|2026-07-19]]

Fifth deep review, chosen by the driver because `deep_review.py` never selects voids. The page was last edited on 2026-10-26, by three refine-draft commits (dc270a0d, b738359b, 8f5adb1c) made after the outer reviews of that date. Its stability notes from 2026-07-19 were superseded and did not bind this pass. Every quotation was re-verified against a raw primary text this run.

**Length** (`analyze_length`): 2,410 → 2,439 (+29), `soft_warning` before and after (voids soft 2,000, hard 3,000). The run was length-neutral in intent. Of the +29, about 18 words are reference metadata (Withy pages and DOI, the Knight revision note, the Heidegger pagination note, §46). The retention-protention paragraph was condensed by about 35 words to pay for the Husserl and occluded-face clauses.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **The Occam paragraph misstates the Map's own tenet and contradicts itself (RTSP, Tenet 5).**
   - OLD: "so the tenet, which constrains only the Map's own reasoning, brings no charge against it."
   - NEW: "so the tenet, which governs appeals to simplicity on either side, brings no charge against it."
   - Why: `tenets/tenets.md` L145 says "This tenet binds the Map's use of parsimony, *not only its critics'*", and its "Rules out" line begins "Using parsimony as a decisive argument against dualism". The very next sentence of the article says the tenet "bars parsimony alone from ruling the dualist reading out", which is a constraint on critics. So the clause contradicted both the tenet and the article.
   - Origin: commit 8f5adb1c (2026-10-26). The phrase is a research-note template, "Tenet 5 constrains only the Map's own reasoning (tenets L145)", which drops L145's "not only its critics'". It has spread to four other live pages (see Remaining Items).

2. **Sartre's facticity paraphrase attributed a list Sartre does not give.**
   - OLD: "Sartre identifies the given, inalterable aspects of one's situation — body, social class, past, world — as *facticity*. None of these were chosen."
   - NEW: "Sartre's *facticity* is the given of one's situation: place, body, past, and a position already marked out by others (*Being and Nothingness*, Part Four, ch. 1)."
   - Why: Barnes's translation gives the list as "my place, my body, my past, my position in so far as it is already determined by the indications of Others, finally my fundamental relation to the Other". "Social class" and "world" are not on it; the gloss came from the IEP-sourced research note. "None of these were chosen" fails for "my past", which for Sartre includes earlier free choices. "Inalterable" overstated "place".
   - Classed as an attribution error, since claims were put in Sartre's mouth. It is low in severity because the passage was not a quotation.

3. **The Augustine reference named the wrong text version.**
   - OLD: "Trans. Pilkington (1887)."
   - NEW: "Trans. Pilkington (1887), as revised by K. Knight for New Advent."
   - Why: the quotation "which I believe **in** the word of others" is verbatim at the cited New Advent URL, whose credit line reads "Revised and edited for New Advent by Kevin Knight". The 1887 Pilkington text in NPNF¹ vol. 1 (CCEL plain text) reads "which I believe **on** the word of others". The quotation matched the URL but not the edition named. Metadata now matches the text quoted.

### Medium Issues Found

- **The lead attached a gloss to Bayne et al. that the paper does not use.**
  - OLD: "a graded, multidimensional interval: Bayne et al. (2023) find no received view…"
  - NEW: "a graded, piecemeal interval: Bayne et al. (2023) find no received view of its timing or form, leave that question open, and argue…"
  - The PMC full text has 0 hits for "graded", "multidimensional" or "gradual". Its Outstanding Questions do ask "Is the transition from unconsciousness to consciousness sharp?" and "Does consciousness emerge piecemeal?". The new wording follows the paper.
- **The lineage sentence overgeneralised.**
  - OLD: "the structure recurs whenever this tradition analyses the subject's relation to its own ground"
  - NEW: "recurs across four analyses of…"
  - Four instances do not license "whenever". The P-M2 discount is otherwise intact: the lead and the tenet section make no convergence claim, and `apex/taxonomy-of-voids` L137 already says "within one Husserl–Heidegger lineage".
- **The occluded-face conjecture had a missing premise.** Epistemic opacity was said to protect against *revision*, but recollecting an onset would not confer power to undo it. Added: "The conjecture assumes that access would bring power to revise; merely recollecting an onset would not undo it." Its withdrawal condition (wide neural self-control) tests the revision premise, so the two now line up.
- **The Husserl framing was a source/Map conflation risk.** "glimpse the *contingency* of one's own cognitive constitution" read as Husserl's result. But *Ideas I* §46 sets "the thesis of my pure Ego… which is 'necessary'" against "the thesis of the world which is 'contingent'". Now: "one's own empirical make-up", plus "The use is the Map's: Husserl opposes the 'necessary' thesis of the pure ego to the 'contingent' thesis of the world (§46)."
- **The consent paradox overclaimed.** "the concept of pre-existential consent is incoherent" ignored hypothetical consent in procreative ethics. Now: "actual consent before existence is incoherent. Whether hypothetical consent can stand in for it, and whether non-consent wrongs anyone, are separate questions for procreative ethics." A doubled "logical / conceptual" statement was merged.
- **The apophatic line read as a contradiction.** "not conscious, not unconscious" became "not conscious, nor the unconsciousness of an existing subject".
- **The comparative-architecture line overclaimed.** "reveals which features… are contingent" became "could help show". Other minds' thrownness is not open from inside.
- **Reference 10 (McGinn 2014) was orphaned.** It was cited nowhere inline. The "naturalist thesis" sentence now cites "(McGinn 1989; 2014)". The 2014 post names the view "naturalistic mysterianism" and its mysteries "mysteries of nature, not 'mysteries of the supernatural'".
- **Heidegger pagination was ambiguous.** "p. 173" and "p. 330" are Macquarrie & Robinson English pages. Added "H. 134" and "H. 284" and a pagination note in Reference 1.
- **Low:** "This seamless quality is precisely how the void maintains its invisibility" (teleological) became "This seamlessness keeps the void invisible." The Sartre flourish "— a formulation that captures the paradox precisely" was cut for length. The second Sartre cite now gives its location, "(Part Three, ch. 2)".

### Verification Ledger

Sources were downloaded this run and whitespace was collapsed before grepping. Each line gives the state of the citation, then the evidence.

- **Heidegger, *Being and Time*, M&R 1962** (archive.org `being-and-time-martin-heidegger-1962` djvu text, Blackwell printing):
  - "the pure 'that it is' shows itself, but the 'whence' and the 'whither' remain in darkness": **real-correct**. Verbatim on M&R p. 173, §29 ("29. Being-there as State-of-mind"). The marginal H.135 follows the passage, so it is H. 134.
  - "as some event which has happened to Dasein": **real-correct**. Verbatim on p. 330, §58 ("58. Understanding the Appeal, and Guilt" begins p. 325), H. 284.
  - "Being-the-basis of a nullity": **real-correct**, pp. 329 and 331, §58.
  - The unquoted paraphrase "can never gain mastery over it" is faithful to "can never get that basis into its power" (p. 330).
  - The pages in the article are M&R English pages, not H-numbers. Both are now given.
- **Withy 2021**: **real-correct metadata, incomplete**. The Cambridge Core chapter page reads "By Katherine Withy, Edited by Mark A. Wrathall", pp. 753–756, DOI 10.1017/9780511843778.204. The Summary contains "Dasein's birth, origin, or ground" verbatim. A WebSearch summariser claimed the entry was Wrathall's; the publisher page refutes that. Pages and DOI added.
- **Sartre, *Being and Nothingness*, Barnes** (archive.org 2011 Barnes text):
  - "the contingent form which is taken up by the necessity of my contingency": **real-correct**, verbatim in Part Three, ch. 2 "The Body". The earlier wording, "assumed by", is a separate occurrence.
  - Facticity list: **corrected** (critical 2).
  - "Sartrean nausea is consciousness's taste of its own facticity" is an unquoted paraphrase. It is supported by "an insipid taste which I cannot place… this is what we have described elsewhere under the name of Nausea", and by Barnes's intro, "Nausea is the 'taste of my facticity'".
- **Levinas, *Existence and Existents*, Lingis, Kluwer 1978/1988** (full text hosted at mercaba.org; print pages taken from its TOC). The archive.org scan is lending-restricted (401).
  - "The bare fact of presence is oppressive; one is held by being, held to be": **real-correct**, ch. 4 §1 "Insomnia", p. 65. A WebSearch summariser said Lingis reads "held to being". That wording is a different sentence in the Introduction (on indolence). The insomnia sentence reads "held by being", exactly as quoted.
  - "encompasses things and consciousness": **real-correct**, same paragraph, p. 65. Its subject is "the universal fact of the there is", as the article says.
  - "exercises a mastery over the fatality of Being": **real-correct**, ch. 4 §2 "Position" (pp. 67–85), in "By hypostasis anonymous being loses its there is character. An entity… exercises a mastery over the fatality of Being, which has become its attribute."
  - "the fear of being to the fear of nothingness": **real-correct**, ch. 3 §2 "Existence without Existents" (pp. 57–64): "We are opposing, then, the horror of the night… to Heideggerian anxiety, the fear of being to the fear of nothingness." The direction (horror *against* anxiety) is right.
  - All four quotations are correctly attributed to *Existence and Existents*, none to *Time and the Other*.
- **Arendt, *The Human Condition*** (archive.org Chicago 2nd edition, same pagination as 1958): "can make itself felt in the world only because the newcomer possesses the capacity of beginning something anew, that is, of acting" is **real-correct**, p. 9. Page numbers are bracketed folios at the page foot. The footer convention was calibrated on Prologue p. 1 and Chapter I p. 7, and the quotation falls after "[ 8 ]" and before "[ 9 ]". "natality, and not mortality, may be the central category of political… thought" supports "recentres on birth".
- **Augustine, *Confessions* I.7.12**: **real-wrong-metadata, corrected** (critical 3). The author really is Augustine; the driver's suspicion of a different author is cleared. Chapter 7, §12 is confirmed by the section markers at New Advent. Augustine adds "in the darkness of my forgetfulness, it is like to that which I passed in my mother's womb", which fits "a case of forgetting".
- **Husserl, *Ideas I*, Boyce Gibson 1931, Allen & Unwin** (archive.org DLI scan): §31 "Radical Alteration of the Natural Thesis 'Disconnexion', 'Bracketing'" (p. 107) and §32 "The Phenomenological ἐποχή" are **real-correct**. The §46 "necessary"/"contingent" pairing was verified and is now cited.
- **Bayne, Frohlich, Cusack, Moser & Naci 2023**, *TiCS* 27(12), 1135–1149: **real-correct**. Crossref confirms the title, five authors, volume, issue and pages. PMC10660191 full text reads "no received view about when, and in what form, consciousness first emerges". The abstract says "arguing that recent research points in favor of early-onset accounts". The body adds "may even begin before birth", with the caveat that the evidence is "from late (third trimester) pregnancy, generally after 35 weeks".
  - Result-direction leg: the direction and hedges are faithful.
  - Cited-author stance: a neuroscience review with no metaphysical commitment, and not presented as endorsing dualism.
  - Gloss: **corrected** (medium).
- **McGinn 1989**, *Mind* 98(391), 349–366 (informationphilosopher PDF of the *Mind* text): **real-correct**.
  - "(i) there exists some property of the brain that accounts naturalistically for consciousness; (ii) we are cognitively closed with respect to that property" (p. 352).
  - "it certainly seems to me to be at least an open question whether the problem is absolutely insoluble" (pp. 361–362) supports "leaves open whether that closure is absolute".
  - Stance: naturalist, anti-dualist ("whatever it is it is not inherently miraculous"), correctly labelled "naturalist thesis".
- **McGinn 2014**, "Mysterianism Revisited" (colinmcginn.net, 2014-12-23): **real-correct**. It was an orphan and is now cited inline.
- **Lineage facts** (SEP, fetched): Sartre in Berlin "to study more closely Husserl's method and to familiarise himself with the works of his students, Heidegger and Scheler" (SEP *Sartre*). "1928–29: Levinas travels to Freiburg… he attends Heidegger's seminar" (SEP *Levinas*). "In 1924… she went to Marburg University to study with Martin Heidegger" (SEP *Arendt*). All **real-correct**.
- **Empirical-currency helper**: no superlative claims detected.
- **Map-internal**: every body wikilink and anchor resolves: `agency-void#what-cannot-be-controlled` (L85), `vertiginous-question` L74 and L185, `quantum-interface ^mechanism-debt`, all four tenet block IDs. The vertiginous-question RTSP does say "posit a non-physical principle of individuation or accept individuation as fundamental". `[[apophatic-approaches]]` renders to `/concepts/apophatic-approaches/`, which is the intended live concept.

### Counterarguments Considered

- **Physicalist (Dennett):** thrownness is trivially true of developing organisms. The RTSP already states the constitution view as the strongest rival and grades dualism's fit as "consistency, not support". This is framework-boundary marking (Mode Three), honestly done, with no straw man.
- **Popper's ghost:** the occluded conjecture was unfalsifiable as to its *epistemic* half. Fixed by stating the revision premise its withdrawal condition tests.
- **Nagarjuna:** the apophatic pair looked like a contradiction. Fixed by gloss.
- **Many-Worlds (Deutsch):** a branch observer meets the same void. The page already concedes that No Many Worlds "removes one escape route without deepening the void". Bedrock.
- **Tegmark:** the quantum-selection paragraph already says Tenet 3 "adds no asymmetry of its own" and books the selector's origin as a debt. Nothing to fix.

### Reasoning-mode classification (editor-internal)

- **Constitution-view physicalist:** Mode Three, framework-boundary marking. The rival "denies the presupposition"; dualism is said to owe more. Honest.
- **McGinn:** not opposed. He is separated as a naturalist thesis with its own commitments (Mode Three, by distinction).

## Optimistic Analysis Summary

### Strengths Preserved

- The narrow "secure core" in the lead, and the moment-or-interval framing tied to Bayne et al.
- The P-M2 lineage paragraph with its concrete biographical evidence, and "a shared ancestor can transmit a shared prejudice as readily as a shared insight".
- The amnesia distinction between absence at the limit point and forgetting of the earliest period. Augustine is the outside-lineage witness.
- Arendt's active dimension of natality, kept intact with its quotation.
- An RTSP that grades every tenet link at or below consistency and books dualism's extra obligations as the Map's own (P-V3).
- The three-moods sentence, which keeps Levinas's opposition to Heideggerian anxiety.

### Enhancements Made

Heidegger H-numbers, the Withy pages and DOI, Sartre's own facticity list with its location, the Husserl §46 contrast, the hypothetical-consent scope, the McGinn 2014 inline cite, and the Augustine revision credit.

### Cross-links Added

None (the page is in length-neutral mode and its cluster links are complete).

## Remaining Items (follow-ups; not edited, per driver)

1. **CORPUS (high): the template misreading "constrains only the Map's own reasoning" is live on four other pages.** All drop L145's "not only its critics'":
   - `concepts/rollback-argument-against-agent-causation` L110
   - `concepts/basic-argument-and-constitutive-luck` L135
   - `concepts/transparency-method-of-self-knowledge` L105
   - `topics/chain-of-thought-as-verbal-protocol` L120

   It also appears in research notes, among them `research/blocks-harder-problem-2026-10-24` L413 ("Tenet 5 constrains only the Map's own reasoning (tenets L145)"), and in `workflow/todo.md`. The intended point, that the tenet cannot refute a non-parsimony argument, is sound. The wording inverts the tenet. Suggested repair: "governs appeals to simplicity on either side" or "binds parsimony arguments, the Map's and its critics' alike". Fix the template wherever research notes are briefed.
2. **Research note `research/voids-thrownness-void-2026-03-30.md` defects** (not edited; historical record):
   - (a) L54 "We are never in control of our own being from the ground up" is given as a Heidegger "Quote", sourced to Wikipedia. M&R p. 330 reads "never to have power over one's ownmost Being from the ground up". The wording is a paraphrase in quotation marks. The same string is in `archive/voids/framework-void.md`, and the variant "in control of one's own being from the ground up" is in `research/voids-constitutive-exclusion-2026-03-04.md`. Check whether any live page carries it.
   - (b) L62/L65 Sartre: "the contingent form assumed by the necessity of one's contingency" and the spliced "The body is nothing other than the for-itself… the contingent form which is assumed by the necessity of one's contingency". Barnes has "my", not "one's", and the order is reversed (the "define the body" clause precedes "The body is nothing other than the for-itself").
   - (c) L61, the quoted "trapped in the facticity of its given bodies…", and L75, "against which consciousness has no power", are unverified secondary phrasings in quotation marks.
   - (d) L60, the facticity list "body, social class, past, world", is not Sartre's list (critical 2's source).
   - (e) L71 frames the il y a as "existence before any subject exists", a developmental stage, which the article rightly rejects.
   - (f) L86, the Arendt-sounding "We can never choose the time, the place, or the circumstances of our birth and life", comes from a PhilArchive secondary paper, not Arendt.
   - (g) L98, McGinn's cognitive-closure definition, is cited to the 2014 blog (0 hits there for "concept-forming" or "cognitively closed"). It is from McGinn 1989 p. 350, and the note silently drops "(or theory T)" and "(or an understanding of T)".
   - (h) L101/L208 "Radical Passivity": the URL is Hofmeyr (ed.) 2009, Springer (Crossref), but the Citations list Wall 1999 (SUNY). These are two different books.
   - (i) L87 "thrownness is absolute", L125 "bootstrapping problem is absolute", L127 "independent philosophical traditions" and L129/L141 "never a knower… not amnesia" are all overclaims the article has since corrected.
   - (j) `related_articles` carries the archived slugs `involuntariness-void` and `indexical-void`.
3. **Could not reach:** the Lingis *E&E* archive.org scan (401, lending), so the Levinas text was verified against the Kluwer-pagination digital text at mercaba.org instead. I did not check whether the Duquesne 2001 reissue repaginates (the Maynooth thesis cites the insomnia passage at p. 61). The article gives no Levinas page numbers, so nothing in it depends on this.

## Stability Notes

- **What was verified this run (2026-11-27), at raw source:** all 11 quoted strings (Heidegger ×3, Withy, Sartre, Levinas ×4, Arendt, Augustine); the Husserl §§31–32 and §46 headings; Bayne et al. metadata and full text; McGinn 1989 pp. 352 and 361–362; McGinn 2014; the three SEP lineage facts. The ledger above gives each source and location. Re-verify only a string that is edited, or any string newly added.
- The four-thinker recurrence is **one evidential move** under P-M2/P-V1. Do not restore "independent traditions" or "convergence" language. The lineage paragraph and its "recurs across four analyses" wording are the calibrated form.
- Tenet 5 binds parsimony arguments on **both** sides (tenets L145). Do not reintroduce "constrains only the Map's own reasoning".
- Constitution-view physicalism versus dualism over binding is bedrock, at the framework boundary. Do not re-flag it as critical. The page's "consistency, not support" grade is correct. Do not upgrade it.
- Arendt's active dimension stays. The retention-protention clarification is now condensed. Its substance (a different Husserl strand, cluster membership by shape, not literature) must stay; do not re-expand it.
- The occluded face is conjecture with a withdrawal condition and a stated premise. Do not upgrade it.
