---
title: "Deep Review - Consciousness and the Epistemic Condition on Moral Responsibility"
created: 2026-10-23
modified: 2026-10-23
human_modified: null
ai_modified: 2026-10-23T13:48:48+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-23
last_curated: null
---

**Date**: 2026-10-23
**Article**: [[consciousness-and-the-epistemic-condition-on-responsibility|Consciousness and the Epistemic Condition on Moral Responsibility]]
**Previous review**: Never (the article was created 2026-10-23 at about 12:07Z from [[research/consciousness-and-the-epistemic-condition-on-responsibility-2026-10-23]])
**Length** (analyze_length, body): 3,198 → 3,227 (+29; topics soft 3,000, hard 4,000). The net comes almost entirely from the Smith correction (+28). Offsets: the L60 duplicate cut (−10), the p. 38 splice repair (−5) and the forward-reference tidy (−4).

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Smith 2012 gloss spliced and its hedge dropped (attribution / qualifier).**
   - The article read: Smith reads "subconscious racist reactions co-existing alongside consciously endorsed egalitarian views" as compatible with her view (2012, n. 11).
   - The raw text (mit.edu JSTOR copy, pdftotext grep) shows the following.
     - n. 11 says "My thesis is fully compatible with these findings", meaning *Haidt's* findings. The racist-reactions phrase refers back to "the possibility broached in the previous footnote". That note then says: "I don't think we (yet?) have convincing experimental evidence that can settle this question one way or another."
     - Smith's actual verdict is in **n. 10**: "a person may consciously hold egalitarian views and yet still find herself taking the fact of a person's race as a reason not to trust her or not to hire her. In these cases, I think an answerability demand directed toward her racist reactions still makes perfect sense".
   - **Fix**: the sentence now gives the n. 10 verdict, quoted verbatim, and n. 11's concession that experimental evidence cannot yet settle whether such reactions embody evaluative judgments.
   - The research note cleared n. 11 but not n. 10. The n. 10 quotation was verified at the primary source in this pass.

2. **p. 38 subject splice (driver's judgement call 2).**
   - The article had "Levy's account, he writes, 'makes it easy to see why the hard problem is not our problem'". The verified snippet has no grammatical subject, so "Levy's account" was a subject the source does not give.
   - Google Books search-within was retried; its control query ("global workspace") returned 10 hits once and then 0, so the endpoint was throttled.
   - **Fix**: "Levy holds that 'the hard problem is not our problem'". This uses only the verbatim span, and the stance it states is faithful.

3. **"*Noûs* abstract" framing (quote-status guard).** The article said "The abstract of his *Noûs* paper (2014b), as given on its Oxford seminar page". That presents the seminar abstract as the *Noûs* abstract, which the research note says is unchecked. **Fix**: "An Oxford seminar abstract under the title of his *Noûs* paper (2014b) concedes…".

4. **Superlative missed by the helper.** The lede said Levy 2014 is "*the* leading defence". This is an exclusivity claim the research note does not license; King & Carruthers 2022 say "one leading defense". **Fix**: "a leading defence". `find_superlative_claims` returned nothing for this file, so the pattern is outside its lexicon.

### Medium Issues Found

- **Semler overstated.** "argues against any phenomenal requirement" became "casts doubt on a phenomenal requirement", Semler's own verb (V-abs).
- **Coiner-adjacent wording.** "He introduced the label for Scanlon and Smith" became "He applies it to Timothy Scanlon and Angela Smith". The JESP text does introduce the volitionist/attributionist pair ("Call these accounts volitionist and attributionist"), but coinage of the word is not established. The lead's "what Levy (2005) calls attributionism" is unchanged.
- **First cost overclaimed.**
  - Before: "it separates no ordinary case… personal availability and phenomenal presence co-occur, so every standard excuse…".
  - After: "it separates none of the standard cases… largely co-occur, so the standard excuses…".
  - Block's overflow argument disputes full co-occurrence. The research note says not to overclaim either way.
- **Blindsight inference (driver's judgement call 1).** It now reads as the Map's: "On the Map's reading, blindsight information arguably fails personal availability too." "Surfaces only under forced-choice guessing" became "typically surfaces", because blindsight also shows up in unprompted behaviour such as obstacle avoidance. "Often cited" became "often offered".
- **Host currency (gradient edited at about 12:07Z).**
  - Gradient L57 now says its lapse verdict "sides with the capacitarians against Levy", and L69 now says "'Phenomenally available' is this article's term".
  - The article's "without reconciling them" read as if the gradient were silent. It now reads: "That verdict is capacitarian, Sher's rather than Levy's, as the gradient itself states", and "neither page reconciles them".
  - Re-read host lines: moral-responsibility L83 ("requires consciousness"; "necessary for that standing without conferring it") and L89 (self-knowledge clause); gradient L57/L61/L69/L108; AI page L86; reasons-responsiveness L80. All are quoted accurately.
- **Absence claim scoped.** "None of the authors surveyed argues for dualism" became "None of the texts surveyed". Several works, Madva among them, were read at abstract level only.
- **Duplicate.** L60's "His notion is informational, and he sets the hard problem aside" repeated the lead's "Levy sets the hard problem aside", so it was cut. The guard wording survives in the lead.

### Per-cite ledger (§2.4, publisher of record)

Crossref API was used for metadata; OpenAlex `abstract_inverted_index` for abstract quotes. Primary PDFs were grepped for Levy 2005 (jesp.org) and Smith 2012 (mit.edu), and the raw SEP HTML was grepped.

- **Arpaly 2003** (*Unprincipled Virtue*): real-correct (OSO online 2002-12, print 2003). The Huck quote is SEP-secondary, quoted as such, and is verbatim in raw SEP §3.3 next to "(Arpaly 2003: 77)".
- **Hahn et al. 2014** (JEP:G 143(3) 1369–1392): real-correct. Both quotes are verbatim in the abstract.
- **Holroyd 2012** (JSP 43(3) 274–306): real-correct. The quote is verbatim in the abstract.
- **King & Carruthers 2012** (JMP 9(2) 200–228): real-correct. Both quotes are verbatim. They are reported as conditional, as the guard requires.
- **King & Carruthers 2022** (OHMR 448–467): real-correct. The quote is verbatim.
- **Kurdi et al. 2019** (Am Psych 74(5) 569–586): real-correct. "most studies were vastly underpowered" is verbatim. The direction "stronger relations under favourable designs" matches r = .37 against .02 in the research note.
- **Levy 2005** (JESP 1(2) 1–16): real-correct. "both of whom argue that responsibility-as-attributability is all the responsibility there is" was grepped in the full PDF.
- **Levy 2014a** (OUP): real-correct.
  - Abstract quotes verified for the book and chs. 1, 2, 5 and 6 (chapter DOIs .003.0001/2/5/6).
  - Page quotes (pp. vii, 29, 30, 33, 34, 38, 96, 102) rest on the research note's Google Books snippets. They could not be re-run (endpoint throttled).
- **Levy 2014b** (*Noûs* 48(1) 21–40): real-correct metadata. The quotes rest on the seminar page only, and are now framed as the seminar abstract.
- **Madva 2019**: **real-wrong-metadata**.
  - Was "PhilArchive record MADERF (journal venue unconfirmed)".
  - Corrected to *Journal of Consciousness Studies* 26(5–6), 117–140, with the Ingenta URL `/content/imp/jcs/2019/00000026/f0020005/art00005`.
  - Evidence: the Ingenta landing path (vol. 26, issue f0020005 = nos. 5–6, art. 5), an OpenAlex location labelled JCS, and the PhilArchive listing "26 (5-6):117-40". The Ingenta page itself sits behind a bot challenge, so the page range rests on the listing plus the Ingenta search result.
  - Abstract quotes verbatim. No other live page cites Madva, so no family propagation was needed.
- **Oswald et al. 2013** (JPSP 105(2) 171–192): real-correct. The quote is verbatim.
- **Rosen 2004** (*Phil Perspectives* 18(1) 295–313): real-correct.
- **Rudy-Hiller 2018/2022** (SEP): real-correct.
  - Dates verbatim ("First published Wed Sep 12, 2018; substantive revision Tue Oct 4, 2022").
  - Verbatim quotes: the §1.1 three-question quote, "is disjunctive (Sher 2009: 87)", the should-and-could disjunct, and the forgetting-a-birthday line.
  - The Hot Dog / border collie case is present.
  - SEP lists "Levy 2013: 167; 2014: 34" among the dispositionalists, confirming the article's "classes his 2014 view as dispositionalist".
- **Semler 2024** (CJP 54(5) 403–422, DOI 10.1017/can.2025.10008): real-correct. Crossref gives issue 2024-07. All three quotes are verbatim.
- **Shepherd & Levy 2020** (OHPC 653–672, ed. Kriegel): real-correct. The quote is verbatim.
- **Sher 2009** (*Who Knew?*): real-correct. No direct Sher quote is used; the article uses the SEP's formulation, as the guard requires.
- **Smith 2005** (*Ethics* 115(2) 236–271): real-correct. The 2012 restatement is attributed to 2012.
- **Smith 2012** (*Ethics* 122(3) 575–589): real-correct metadata. The main-text quotes ("the rational relations view", "just in case F bears a rational connection…", "patterns of awareness and many unintentional omissions") are verbatim in the PDF. **n. 10/11 gloss corrected** (Critical 1).
- **Strawson 1962** (PBA 48, 187–211): real-correct. An offprint description gives "Pp. (2), 187–211"; the corpus mostly uses this range. "He hadn't realized" also appears in reactive-attitudes L40.
- **Washington & Kelly 2016** (*Implicit Bias and Philosophy* v.2, 10–36): real-correct. Both quotes are verbatim; the abstract uses curly quotes around "in the head".
- **Zimmerman 1997** (*Ethics* 107(3) 410–426): real-correct.
- **Inline ↔ References**: no orphans in either direction, keyed on (surname, year). Levy 2005/2014a/2014b, King & Carruthers 2012/2022 and Smith 2005/2012 are each distinct and each is cited.

### Result-direction and author-stance legs

- **Result direction.** Hahn (accurate self-prediction, against unconsciousness), Oswald (poor prediction), Kurdi (design-dependent), Holroyd ("sometimes" blameworthy) and Washington & Kelly (responsible) are all reported in the direction their abstracts give.
- **Author stance.**
  - Levy: informational, sets the hard problem aside; never enlisted, never called physicalist.
  - Madva: capacity thesis with no stated metaphysics; not presented as dualist.
  - King & Carruthers: conditional.
  - Semler: rival named at the AI-page seam.
  - Smith: quality of will (rational relations).
  - Sher: capacitarian; never "attributionist".
  - Shepherd & Levy: "failed to settle", quoted rather than asserted.

### Reasoning-mode classification (editor-internal)

- **Levy**: Mode Three. The Map declares its phenomenal reading an extension with stated costs and claims no refutation.
- **King & Carruthers; Semler**: Mode Three. Reported and named as rivals. The AI-page seam concedes that the epistemic condition does not support the exclusion.
- **Sher against Levy**: exposition. The Map's synthesis is labelled as its own.

No boundary-substitution was found. No editor-vocabulary leaked into the prose (0 hits for the forbidden labels).

### Counterarguments Considered

- **Dennett / functionalist** ("the duplicate lacks nothing"): already handled in the second cost, which notes that the verdict has force only inside a framework on which such a duplicate is possible. This is bedrock.
- **Churchland / King & Carruthers**: reported as conditional; there are no conscious attitudes to rest on. Not refuted, honestly.
- **Popper**: the extension separates none of the standard cases. The article states this as a cost rather than hiding it.
- **Epiphenomenalist**: the necessary-condition point is preserved, and Tenet 3 says "fits without evidencing". The quantifier is recorded as open, matching `concepts/epiphenomenalism` L130–132.
- **Tegmark, Deutsch, Nagarjuna**: not engaged. No quantum, MWI or self-metaphysics claims are made.

## Optimistic Analysis Summary

### Strengths Preserved

- The lead front-loads Levy's informational reading and the Map's extension, and keeps the on-Map absence claim out of the lead and description.
- "The Map's extension and its costs" is a model of the "tenet-coherent, not evidence-elevating" pattern. The Hardline Empiricist (Birch) persona would praise it.
- The tension section names a real inconsistency in the Map's own pages and labels the reconciliation as the Map's synthesis, with its costs.
- The implicit-bias test case is held fixed conceptually, so nothing rests on IAT effect sizes (Hahn 2014 is used against the unconsciousness assumption).
- The "a necessary condition need not be a cause" limit keeps the phenomenal requirement from being misused against epiphenomenalism.

### Enhancements Made

- Smith's verdict is now quoted from its actual locus (n. 10), with her own empirical hedge (n. 11).
- The blindsight inference is marked as the Map's.
- The first cost is calibrated.
- The Madva venue is confirmed.

### Cross-links Added (zero-cost piped links)

- [[phenomenal-consciousness]] (lead)
- [[access-consciousness]] ("akin to what Ned Block calls…")
- [[philosophical-zombies]] (p. 38 remark)
- [[reactive-attitudes-and-strawsonian-responsibility]] (Madva's Strawson route)

## Remaining Items

- **Google Books re-verification of Levy 2014 page quotes.** The quotes cover pp. vii, 29, 30, 33, 34, 38, 96 and 102. The endpoint `books.google.co.uk/...id=V6zSAgAAQBAJ...&jscmd=SearchWithinVolume2` passed its control once and then returned 0, so it was throttled. The quotes stand on the research note's V-GB snippets.
- **Whether Levy himself discusses blindsight** could not be checked. If he does, the Map-reading sentence may under-credit him, though it would not misattribute anything to him.
- None blocking.

### Host-side findings for the P3 cross-review (not edited)

- **`concepts/blindsight` L129** says Block treats blindsight as "the paradigm case of information reaching cognitive systems (partial access) without phenomenal awareness". As recalled, not verified this pass, Block (1995) argues that actual blindsight lacks A-consciousness too. On that reading, his A-without-P case is the hypothetical "superblindsight". **LEAD only**: verify against Block 1995 *BBS* before any edit.
- The gradient (L57/L69) and moral-responsibility (L43 piped link) are already integrated. The AI page L86, reasons-responsiveness L80, alief (noticing-condition section) and reactive-attitudes L40 still lack a link to this article.
- On the AI page, Semler 2024 should be named wherever the culpability gap is touched, per the research note's guard.

## Stability Notes

- **Bedrock**: functionalists and Levy will hold that a phenomenally empty duplicate satisfies the epistemic condition. The article records this as the extension's second cost. Future reviews should not re-flag "functionalist finds the extension unmotivated" as critical.
- **Calibration settled this pass**:
  - "a leading defence" (not "the");
  - Semler "casts doubt";
  - "largely co-occur" / "none of the standard cases";
  - blindsight "On the Map's reading… arguably".
  
  Do not re-strengthen any of these without new evidence.
- **Smith n. 10/n. 11**: the n. 10 quote and n. 11 hedge were verified in the raw PDF this pass. The old "compatible with her view" gloss was a splice of n. 11's "compatible", which refers to Haidt's findings. Do not restore it.
- **p. 38**: quote only the subjectless span "the hard problem is not our problem" until a snippet shows the sentence's subject.
- **Madva venue**: JCS 26(5–6) 117–140 is confirmed via the Ingenta path and the PhilArchive listing. Do not revert it to "unconfirmed".
- **Host currency**: the tension section now reflects the gradient's 12:07Z self-description. If the gradient or moral-responsibility later adds its own reconciliation, "neither page reconciles them" must be updated. That would be a genuine change under the article, not cosmetic.
- **Length**: 3,227 against soft 3,000. Any further additions should be length-neutral.
