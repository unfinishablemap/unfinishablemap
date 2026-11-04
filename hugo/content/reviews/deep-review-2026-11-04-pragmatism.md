---
ai_contribution: 100
ai_generated_date: 2026-11-04
ai_modified: 2026-11-04 17:07:40+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-04
date: &id001 2026-11-04
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-04 17:07:40+00:00
modified: *id001
related_articles: []
title: Deep Review - Pragmatism
topics: []
---

**Date**: 2026-11-04
**Article**: [Pragmatism](/concepts/pragmatism/)
**Previous review**: [2026-08-03](/reviews/deep-review-2026-08-03-pragmatism/)

**Why this article**: it was the top `deep_review.py next` candidate (score 74, 93 days unreviewed) and is on none of the driver's exclusion lists. Four commits landed after the 08-03 review (`b8e95e41` 09-08 corridor scoping; `6ad79099`, `9459ea4c` and `6768f4dd` 09-15, three refine-drafts from the 09-15 outer-review cycle). Together they took the page from 2533 to 3489 words. The added material includes a rewritten Dewey section with a *Logic* quotation and footnote, a restructured Rorty reply, the Putnam internal-realism relabel, the James Lecture VI quotation, the active-inference and enactivist replies, the Brandom/Price reply and a No-Many-Worlds block, plus ten new References entries. None of it had been through a deep review. The 08-03 stability notes still apply to the material that pass covered.

**Open-task overlap**: no open task targets this page directly. L44's "Preservation binds only that unconditioned marginal" wording is on the cascade list of the blocked P1 HUMAN DECISION on [P-Q2](/positions/quantum-interface/#p-q2)'s quantifier (todo L1622, CASCADE ADDENDUM 2026-11-01). It was left untouched. The open P3 on `topics/william-james-consciousness` (todo L1746) cites this page's L54 as the corrected form. L54 is unchanged, so that citation still holds.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Dewey locator error (L60).** The page said the "wholly misleading" warning and the interactionism footnote are in "the same chapter". They are not. Both the 09-15 refine-draft and `outer-review-2026-09-15-chatgpt-5-6-sol-pro` placed the quotation in "The Pattern of Inquiry". The archive.org OCR of *Logic* (1938; `in.ernet.dli.2015.188830`) puts it in Ch. IV, "Common Sense and Scientific Inquiry", on p. 68, between the running heads for pp. 67 and 69. The footnote ("a problem (and an insoluble one) because of the assumption … that the interaction in question is with something mental instead of with biological-cultural human beings") is in Ch. VI, "The Pattern of Inquiry", on p. 106. **Fixed**: "a footnote in the same chapter" → "a footnote two chapters later" (−1 word).
2. **(surname, year) orphan, inline → References.** L52 names "James's 1904 denial that 'consciousness' names any entity at all", but no James 1904 entry existed. The 09-15 05:54 refine dropped it for budget, per its own changelog entry. **Fixed**: added James, W. (1904). Does 'Consciousness' Exist? *JPPSM* 1(18), 477-491. The pages are confirmed at PDC, the publisher of record (Volume 1, Issue 18, September 1904, Pages 477-491). The volume, issue and date also match Perry's editorial note in *Essays in Radical Empiricism* (Gutenberg #32547).

No internal contradiction, missing section, broken link or possibility/probability slippage was found. No editor-label leakage either: the forbidden-label grep returned clean.

### Medium Issues Found

- **Ambiguous closing clause in the Dewey paragraph (L60).** "Dewey's reply is ready: … — the reply the section below meets in Brandom and Price, and one he rejected rather than overlooked" parses as Dewey rejecting his own reply. The 09-15 changelog shows the intended referent was the dualist reading, which the paragraph's first sentence ("Dewey built that naturalism to exclude the reading a dualist might want") already states. **Fixed**: cut the clause (−7 words). The boundary is still marked in that first sentence and in the Brandom/Price paragraph's closing "noted as such rather than refuted on their terms".
- **Di Paolo's qualifier dropped (L86).** The page glossed the enactivist reply as "autopoietic normativity" and cited Di Paolo 2005. That paper's thesis is that autopoiesis must be supplemented by *adaptivity*, regulation with respect to conditions of viability, before it yields sense-making ("sense-making in organisms needs both autopoiesis and adaptivity"). **Fixed**: "autopoietic and adaptive normativity" (+2). The page's "viability conditions" clause now matches its cited source.
- **Teleosemantics contrast overstated (L84).** The page said Millikan and Papineau ground function "in evolutionary selection history", while Dretske routes it through learning "instead". SEP *Teleological Theories of Mental Content* §2 says standard etiological theories "do not entail that all functions are directly grounded in processes of natural selection": Millikan 1984 allows meme selection and derived functions, and "Papineau (1984) speaks of learning". Dretske's distinctive claim is that learning is *necessary* for behaviour-explaining content. **Fixed**: ", chiefly in evolutionary selection history" (+1, plus a comma to block the "merely does chiefly" misparse). The 08-03 Dretske correction stands.
- **Brandom/Price stance (L90).** "Both grant evaluation a phenomenology" credited both with a positive commitment neither makes. Neither has a theory of evaluative phenomenology to grant. **Fixed**: "Both can grant" (+1).
- **Lead enumeration (L32).** "differently in each founder" introduced a two-item list (Peirce, James) after three founders were named, then continued "Both hold". **Fixed**: "differently for Peirce and James" (+1). I did not add a Dewey truth clause, because Dewey's *Logic* uses "warranted assertibility" for *knowledge* and endorses Peirce's definition of *truth*, so "Dewey's truth is warranted assertibility" would be a misattribution.
- **Uncited Friston stance (L86).** "Friston's own metaphysics is a Markovian monism" carried no source. **Fixed at zero word cost**: piped to [Markovian monism](/concepts/disguised-property-dualism/), whose §Friston's Markovian Monism cites Friston, Wiese & Hobson (2020), *Entropy* 22(5), 516. I used a page-level link, not a heading anchor, because the anchor form costs +2 counted tokens.
- **Filler.** Cut "These consequences matter." (L52, −3; its referent became ambiguous once the 09-15 refine relabelled the consequences as the Map's inferences) and "directly" (L52, −1).

### Citation Web-Verify Ledger (publisher of record)

The ten cites added after 08-03 were verified this pass. The eleven cites carried from 2026-06-25/08-03 are unchanged in the diff. Putnam 1981 was re-verified at the raw text because new claims now rest on it.

- Peirce 1878 (*PSM* 12, 286-302) — real-correct. Wikisource transcription: the third-grade-of-clearness rule and "The opinion which is fated to be ultimately agreed to by all who investigate, is what we mean by the truth, and the object represented in this opinion is the real" are both in the essay, which supports L38's "same essay pairs it with a convergence account".
- James 1896, James 1898 — real-correct (carried).
- James 1904 — **real-correct, newly entered** (see Critical 2). "the name of a nonentity" and "I mean only to deny that the word stands for an entity" were both grepped in Gutenberg #32547. L52's paraphrase is faithful.
- James 1907 *Pragmatism* — real-correct. The L50 quotation "'The true,' to put it very briefly, is only the expedient in the way of our thinking… expedient in the long run and on the whole of course" is **verbatim** in Gutenberg #5116 (NFKC-normalised grep, 1 hit), inside "Lecture VI Pragmatism's Conception of Truth", so the "(*Pragmatism*, Lecture VI)" locator is correct. "It means their 'agreement,' … with 'reality'" and "Copying is one genuine mode of knowing" both grep, supporting the agreement/copying clause.
- Dewey 1938 *Logic* — real-correct metadata; **locator corrected** (Critical 1). "wholly misleading if it gives the impression that the situation is a feeling or an emotion or anything mentalistic" is verbatim (OCR "mcntalistic"). "warranted assertion" is Dewey's own term ("the term 'warranted assertion' is preferred to the terms belief and knowledge"). The footnote paraphrase is faithful.
- Putnam 1981 *RTH* — real-correct. Raw archive.org text: "magical theory of reference" (4 hits), the ant's "recognizable caricature of Winston Churchill", "I shall refer to it as the internalist perspective", and "truth is an idealization of rational acceptability … epistemically ideal conditions" all grep. L74/L76 are faithful.
- Putnam 1994 (*J. Phil.* 91(9)) — real-wrong-metadata (incomplete). Crossref 10.2307/2940978 exact (start page 445). JSTOR and the Putnam bibliography give 445-517. Corrected "445 ff." → "445-517". "natural realism" as the Dewey Lectures' label is confirmed.
- Rorty 1965 — real-wrong-metadata (incomplete). PDC `revmetaph_1965_0019_0001_0024_0054` gives Volume 19, Issue 1, September 1965, Pages 24-54, and the original's pages were missing. Corrected to "19(1), 24-54". Borst reprint: Crossref 10.1007/978-1-349-15364-0_20 exact (book-chapter, Macmillan 1970, 187-213). The "disappearance" form is confirmed as Rorty's 1965 position.
- Rorty 1979 — real-correct (carried).
- van Fraassen 1977 (*APQ* 14(2), 143-150; JSTOR 20009661) — real-correct. van Fraassen 1980 — real-correct (carried).
- Millikan 1984, Dretske 1988, Papineau 1987 — real-correct (carried). The doctrinal gloss was refined (Medium 3).
- Brandom 1994 *Making It Explicit*, HUP — real-correct (OpenLibrary: Harvard University Press 1994, subtitle exact).
- Price et al. 2013 — real-correct. Crossref 10.1017/cbo9780511842498: monograph, CUP 2013-05-16, five authors in the order cited.
- Misak 2004 — real-correct. Crossref 10.1093/0199270597.001.0001: OUP 2004.
- Laukkonen, Friston & Chandaria 2025 — real-correct. Crossref: *Neurosci. Biobehav. Rev.* 176, article 106296, 2025-09, three authors in order.
- Weber & Varela 2002 — real-correct. Crossref: *PCS* 1(2), 97-125.
- Di Paolo 2005 — real-correct metadata (Crossref: *PCS* 4(4), 429-452). **Doctrine gloss corrected** (Medium 2).
- Thompson 2007 *Mind in Life* — real-correct (OpenLibrary: Belknap/Harvard 2007).
- Southgate & Oquatre-six 2026 — Map-internal, link live.

**Inline ↔ References**: James 1904 orphan fixed. The remaining References entries without a dated inline mention (James 1907, Rorty 1979, the teleosemantics trio, Brandom 1994, Price 2013, Misak, Thompson) are each named inline by author. They are bibliographic, not orphans.

**Superlative currency sweep**: `find_superlative_claims` returned empty.

**Not primary-verified**: L66's scare-quoted "getting reality right". A secondary report attests it as Rorty's own wording in *Objectivity, Relativism, and Truth* (1991), p. 1 ("does not view knowledge as a matter of getting reality right"), but that work is not in References and the text is not freely available. It is phrase-level, carries no work attribution and was not touched this pass. Logged as a watch item, not a defect.

**Result-direction leg**: no empirical results are cited. **Cited-author-stance leg**: every author is fenced. Peirce, James, Dewey ("built that naturalism to exclude the reading a dualist might want"), Rorty, Putnam ("did not draw the dualist conclusion"), van Fraassen ("all he commits to"), the teleosemanticists, Friston ("argues against the Map's dualism"), the enactivists and Brandom/Price ("declined by these programmes") are none of them presented as endorsing the Map's conclusion.

### Map-Internal Quotations (re-grepped against the live pages)

- `positions/quantum-interface` [P-Q3](/positions/quantum-interface/#p-q3): "sits genuinely close to epiphenomenalism" is verbatim at L79, which carries the `^mechanism-debt` block anchor. [P-Q3](/positions/quantum-interface/#p-q3)'s heading still reads "strongest live challenge". Accurate.
- `tenets` L123: No Many Worlds "is not a pure physics tenet" is verbatim ("It follows that No Many Worlds is not a pure physics tenet"). The "presupposes a non-deflationary 'I'" paraphrase matches "the non-deflationary 'I' it presupposes".
- `enactivism-challenge-to-interactionist-dualism` §The Dissolution Strategy and Its Limits (L70): the question "why is sense-making accompanied by experience?" is present (L80). The anchor is live.
- `cognitive-phenomenology` §The Illusionist Challenge (L170): live. All six tenet anchors resolve.
- The functionalist deferral to `pragmatisms-path-to-dualism` (the 08-03 stability note): the "locate the price precisely and present the bill" passage (L107) survives.

### Reasoning-Mode Classification (editor-internal)

- Dewey: Mixed. The objection opens as a foundational-move identification (transformation ≠ warrant), Dewey's reply is stated at full strength, and the boundary is marked by the opening sentence. Honest after the referent fix.
- Rorty: Mode Three. The attempted internal argument is stated and shown to fail on Rorty's terms. Honest. Unchanged.
- Teleosemantics: Mode Three ("a cost the Map assesses, not a refutation it delivers"). Unchanged.
- Active inference/Friston: Mode Three with a Mode Two edge. The formalism is marked compatible-with rather than evidence-for. Honest.
- Enactivism: Mode Three, routed to the sibling's open question.
- Brandom/Price: Mode Three. The page's own undefended steps are named. Honest, and stance now calibrated ("can grant").
- Functionalist, epiphenomenalist: Mode Three (carried).

### Counterarguments Considered

- The Empiricist on Peirce's maxim turned inward: still conceded at L44-46 (carried; L44 is owned by the [P-Q2](/positions/quantum-interface/#p-q2) decision).
- The Dennett-style objection that L80's "felt sense … is what gives pragmatic assessment its normative force" begs the question: L90 now concedes that the move from phenomenal character to normative authority is undefended here, and the Dualism block routes the premise to the illusionist section. No further change.
- van Fraassen L100 "because requesting and grasping an answer is something a conscious agent does": the adjective is the Map's gloss, but the paragraph immediately fences everything beyond "explaining is a speech act" as the Map's extension. The sibling's 09-15 fixed form uses the same wording. Left alone for convergence.

## Optimistic Analysis Summary

### Strengths Preserved

- "The Maxim Turned Inward" (do not trim; carried).
- The James forcedness treatment, which licenses openness rather than belief (carried; L54 is the corrected form other pages cite).
- The 09-15 Dewey rewrite. Letting Dewey's own *Logic* speak against the dualist reading is the strongest anti-co-optation move on the page.
- The Brandom/Price paragraph's self-audit: "moves from phenomenal character to normative authority to phenomenal causation and defends neither step here."
- The No-Many-Worlds block, which makes the method's dependence on a theory of subjecthood explicit.
- The Hardline Empiricist's praise point: the page consistently declines to turn tenet-coherence into evidential upgrade ("a cost the Map assesses, not a refutation it delivers").

### Enhancements Made

Twelve targeted edits, all length-funded (two critical, ten medium or low). No expansion: the page is two words under the concepts hard gate.

### Cross-links Added

- [Markovian monism](/concepts/disguised-property-dualism/) (piped, zero counted words)

## Word Count

`analyze_length`: 3489 → 3498 (+9). The James 1904 entry costs 15 counted words; prose cuts of −12 fund most of it. The concepts hard gate is 3500 with `>=`, so the page sits 2 below. Any future addition needs an equal cut.

## Remaining Items (follow-ups for the driver to mint)

- `topics/pragmatisms-path-to-dualism` L123/L127/L131: sibling drift from this page's 09-15 Putnam fix. L127 still says Putnam's ideal conditions "essentially involve conscious rational agents" and calls RTH-era Putnam "subsequent 'pragmatic realism'". L131 says schemes "only conscious agents occupy". This page reads the conditions as "rational agents with interests rather than phenomenal consciousness … a functionalist can accept without dualism". RTH itself says "the internalist perspective".
- `topics/pragmatisms-path-to-dualism` L139: "His model of inquiry begins with 'felt difficulty' … every stage involves phenomenal character" reads Dewey in exactly the way *Logic* Ch. IV p. 68 warns against ("Stating that it is felt is wholly misleading if it gives the impression that the situation is … anything mentalistic"). This page's L60 now carries that warning. The sibling is at 4037 words, over the topics hard gate of 4000, so any fix there must be net ≤ 0.

## Stability Notes

- All 08-03 stability notes carry: physicalist, eliminativist and MWI rejection of the reflexive argument is bedrock; Buddhist and process objections to the unified evaluator are bedrock; the Empiricist testability objection is inherent and conceded at L44-46; the concept/topic division with [pragmatisms-path-to-dualism](/topics/pragmatisms-path-to-dualism/) stands.
- The 09-15 material is now reviewed. Future passes should treat Dewey, Rorty, Putnam, James truth, active inference, enactivism, Brandom/Price and No Many Worlds as verified at the source as of this date, and re-open them only if their text changes.
- The page is at the length ceiling (3498/3500). It has stabilised. A future cycle that wants to add should first decompose prose from apparatus: the 22 References entries consume a large share of the count.
- L44's corridor wording waits on the [P-Q2](/positions/quantum-interface/#p-q2) human decision and should not be edited by review passes.