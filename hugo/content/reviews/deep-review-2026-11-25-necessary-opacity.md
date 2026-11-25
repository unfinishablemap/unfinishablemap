---
ai_contribution: 100
ai_generated_date: 2026-11-25
ai_modified: 2026-11-25 18:01:42+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-25
date: &id001 2026-11-25
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-25 18:01:42+00:00
modified: *id001
related_articles: []
title: Deep Review - Necessary Opacity
topics: []
---

**Date**: 2026-11-25
**Article**: [Necessary Opacity](/voids/necessary-opacity/)
**Previous review**: [2026-07-06](/reviews/deep-review-2026-07-06-necessary-opacity/) (also 2026-06-01, 2026-04-25, 2026-04-22, 2026-04-01; predecessors' reviews 2026-03-14 and 2026-02-01 destabilizing-self-knowledge, 2026-02-25 transparency-void)

This is the 6th deep review and the first full source pass. The driver selected the page because thirteen void pages built from early-2026 research notes have each turned up critical quotation or source-reporting defects since 2026-11-16. The five prior reviews kept no verbatim ledger. Their verdicts were not treated as binding. Their Stability Notes were read and kept (see the last section). Every attributed quotation and every attributed claim was checked at source, and every quoted span in the final text was grep-verified by script against raw source text after whitespace collapse (`scratchpad/bin/qcheck.py`; all source quotations hit).

**Sources and editions used.** Metzinger, *Being No One* (MIT 2003), archive.org djvu text. Alston 1986, JSTOR scan of *PPR* 47(1). Sellars, *EPM*, Harvard 1997 edition (Rorty/Brandom), archive.org text. Metzinger 2024, MIT Press open-access PDF text (archive.org). Letheby & Gerrans 2017, full PMC XML (PMC6007152, `efetch db=pmc`). James 1902, Project Gutenberg #621. Bostrom 2011, nickbostrom.com PDF (journal pagination header). Abstracts via OpenAlex `abstract_inverted_index`: Battaglia et al. 2025, Deane 2020, Deane, Miller & Wilkinson 2020, Ciaunica et al. 2021, Hoffman 2016, Berke et al. 2022. Hoffman, Singh & Prakash 2015, author manuscript (UCI). Prakash et al., 2017 preprint (UCI) plus PubMed record. Gerrans & Letheby, Aeon 2017 (control search only).

## Pessimistic Analysis Summary

### Critical Issues Found (15)

Each entry gives before → after and the research-note line that seeded it. DSK = `research/voids-destabilizing-self-knowledge-2026-01-27`; TV = `research/voids-transparency-void-2026-02-09`.

1. **Metzinger misquote (words altered inside quote marks).** Before: the subject "looks right through" it. "looks right through" is absent from *Being No One*. Metzinger, *Being No One* p. 1 (§1.1), writes of the *self-model*: "you look right through it. You don't see it. But you see with it." The "right through" in the transparency literature Metzinger quotes is Shoemaker's ("one sees right through it", BNO's Moore/Shoemaker passage). After: the verbatim quote, scoped to the self-model, with a page number. *Seed*: TV L50 (also DSK L70, `we look "right through it"`).
2. **String absent from the cited work.** Before: ego dissolution weakens "the power of models built by prior experience". The string has zero hits in the full text of Letheby & Gerrans 2017 (the positive control "Cartesian fiction" hits). It also has zero hits in their 2017 Aeon essay ("Model hallucinations") and in REBUS (Carhart-Harris & Friston 2019, PMC6588209). Its origin was not found. After: replaced with verified L&G wording ("enabling subjects to experience cognition not bound by self-models"). *Seed*: DSK L80. That note files the phrase under the L&G URL.
3. **Idea credited to the wrong work.** Before: "a collapse in the temporal depth of self-representation", which by sentence and reference list falls to L&G. The idea is Deane (2020), *PhiMiSci* 1(I): ego dissolution as "a collapse in the 'temporal thickness' of an agent's deep temporal model" (abstract). The page did not cite Deane. After: credited to Deane (2020), and the reference is added. *Seed*: DSK L81. That note puts Deane's phrase under the L&G entry, while Deane is its own citation 12.
4. **Source's outcome framing reversed.** Before: "The results split: some report profound insight…; others experience terror, dissolution, psychotic breaks." The cited source says the anxiety and dysphoria "sometimes attend ego dissolution experiences (albeit relatively rarely in controlled settings)". It draws a disclosing moral: as the self-model's coherence degrades "we become aware that our normal experience of unity depends on a modelling process". No source on the page supports "psychotic breaks". After: L&G's actual moral and frequency are given in their words. *Seed*: DSK L83 ("beautiful awakening"/"falling apart", unsourced). Also DSK L85, a blog-register quote filed under the L&G URL. The 10-01 repair had already removed a sibling quote ("I know I am me", DSK L94) from this section.
5. **Dropped clause that reverses James.** Before: "the insights often do not survive… when the self reconstitutes, they cannot articulate what they knew". In James (Lectures XVI–XVII, "Noetic quality") mystical states are "all inarticulate though they remain", so the inarticulacy is intrinsic and not a loss on return. As a rule they "carry with them a curious sense of authority for after-time", so the conviction *does* survive. After: "What survives is conviction rather than content", with both James clauses quoted verbatim. *Seed*: DSK L136 ("The insight dissolves when the self reconstitutes"), L154.
6. **Term absent from the cited work.** Before: "Nick Bostrom's taxonomy of information hazards includes 'cognitohazards'". The term has zero hits in Bostrom 2011 (34-page PDF; the control "information hazard" has 27 hits). After: Bostrom's own "neuropsychological hazard" is quoted verbatim ("might have negative effects on our psyches because of the particular ways in which our brains are structured, effects that would not arise in more 'idealized' cognitive architectures"), with a note that "cognitohazard" is not his term. The heading is now "Information Hazards"; no inbound anchors exist. *Seed*: DSK L102–103. L103 also wrongly says information hazards "harm others", but Bostrom's typology includes harms to the knower.
7. **Alston's inference reversed.** Before: "No basic cognitive source… can be justified without relying on premises drawn from that source." Alston 1986 concludes that with basic sources "one may still justify, and be justified in, the reliability claim". The result "puts no limits whatever on the beliefs that can be justified" and "lends no aid or comfort to any of the more familiar forms of skepticism". What epistemic circularity blocks is non-circular argument and "fully reflective justification" ("FRJ is a pipe dream"), leaving us "without a cosmic guarantee of success" (p. 30). After: Alston's definition of a basic source, his non-sceptical moral, and the missing-guarantee point that the void actually needs. *Seed*: TV L73 and L151. Both are the IEP encyclopedia's gloss ("no way to justify"), credited to Alston.
8. **Sellars's inference half-reversed.** Before: the Myth of the Given "reinforces the point… even data we might use to test the framework is already filtered through it". EPM §38 (Harvard ed. p. 79): empirical knowledge is rational "not because it has a foundation but because it is a self-correcting enterprise which can put any claim in jeopardy, though not all at once." TV L85 recorded this, but the coalesced page dropped it. After: Sellars's moral is stated, and the void's point is narrowed to "self-correction runs inside the system and cannot certify it from outside". *Seed*: TV L153 ("making independent verification impossible").
9. **A question stated as a finding, and the note's gloss credited to the paper (Battaglia, Servajean & Friston 2025).** Before: perception and introspection "yield formulations that cannot be harmonised". The abstract says "evidence supporting one formulation does not necessarily support the other". The DSK note's own quote is a *question* ("To what extent does our inability to harmonize…"). The next sentence, with "studied brain"/"studying brain" in quote marks and "the observation changes the observed state", read as the paper's claim. It is the research note's own "Neuroimaging paradox" evidence item. After: the abstract's wording is quoted. The alteration point is labelled "The Map extends the point" and the quote marks are gone. *Seed*: DSK L48 (and L52), L134.
10. **A repair installed a label.** Before: the Relation section called the paradox "(a predictive-processing result)". Nothing in the abstract says so. The label was installed by the 2026-09-28 refine-draft repair `aebfc92ff7`, not by a research note. After: removed.
11. **Theorem credited to three of its five authors.** Before: "Hoffman, Singh, and Prakash's Fitness-Beats-Truth theorem". The theorem is Prakash, Stephens, Hoffman, Singh & Fields (2021). The 2015 Hoffman–Singh–Prakash paper does not name it (0 hits in the manuscript). After: "of Prakash et al. (2021)". The theorem statement itself is faithful: Theorem 4 of the 2017 preprint reads "Over all possible fitness functions and a priori measures… at least (|X| − 3)/(|X| − 1)". *Seed*: the 09-28 repair `aebfc92ff7` (earlier text: "Donald Hoffman's"). Ultimately TV L236, which gives a wrong author order and a wrong venue ("*Evolution and Cognition* (2020)").
12. **Calibration error: the empirical-support claim is contradicted by the page's own sources.** Before: the lead said piercing yields "typically dysfunction rather than enlightenment". The closing said "Current evidence does not meet these conditions. Convergent patterns across psychedelic research, contemplative traditions, clinical pathology… support structural rather than contingent limits." Metzinger 2024 (listed in References but never cited) reports meditators for whom awareness of awareness "has often been described as… gradually beginning to see the window pane itself", with clarity and connectedness that a depersonalisation link "would seem to exclude". L&G (item 4) report dysphoria as rare in controlled settings. The sibling [depersonalisation](/concepts/depersonalisation/) page already cites Deane, Miller & Wilkinson (2020) for "selfless" experiences being "highly sought after". DSK L220 itself records condition 5 (cross-cultural) as an unresearched gap. A tenet-accepting reviewer would flag this. After: a new subsection, "The Contemplative Counter-Case" (with Metzinger's "disconnectedness" hedge and his "none of this touches… valid insight" limit). The lead now reads "often… and even benign piercings return conviction rather than verifiable insight". The closing says condition 1 is partly met, 2–4 are unmet and 5 is untested, and rests the structural reading on circularity. *Seed*: DSK L93/L95 ("not enlightenment but dysfunction"), L140, L164.
13. **Map-internal gloss misstates its sibling.** Before: imagery-opacity failures "surface three times… Galton's 1880 survey, the Würzburg School…, the post-2015 aphantasia rediscovery", and this "supplies independent evidence". The Further Reading gloss read "(Würzburg → behaviourism → aphantasia)". [imagery-void](/voids/imagery-void/) L93 counts the recurrence *twice* (Würzburg–aphantasia). Galton belongs to its intersubjective face, and behaviourism is what Würzburg ushered in, not an instance. After: matched to the sibling. The transfer to this void is marked "suggestive rather than independent". *Seed*: neither note. Installed by the cross-link commit `6fa67f0324` (2026-04-28).
14. **Map-internal gloss: wrong count.** Before: the Further Reading line for [amplification-void](/voids/amplification-void/) said "five-regime amplification chain". The sibling has four regimes (quantum, molecular, cellular, network; its L99 says "at least four"), and the apex triple-screen says four. After: four. *Seed*: neither note.
15. **Orphan references (§2.4 step 5).** Metzinger 2024 and Nagel 1986 were never cited in the body. Hoffman 2016 and Ciaunica et al. had no inline cite. After: Metzinger 2024 is now used (item 12). Nagel 1986 is removed; the View-from-Nowhere passage was dropped at the 2026-03-28 coalesce. Hoffman 2016 is attached to the desktop-icon analogy (its abstract: "space-time is the desktop of the interface and physical objects are icons on the desktop"), and Ciaunica, Charlton & Farmer (2021) is attached to the cracked-window image. *Seed*: DSK cite 11 (L248), TV L88–96 and L239.

### Medium Issues Found

- "AI can inspect its own weights": weights are read by external interpretability tools, not by the model. Fixed. *Seed*: TV L193.
- "This snap-back is itself evidence for Metzinger's transparency mechanism" was changed to "fits". Metzinger does not discuss the snap-back. *Seed*: TV L163.
- Occam paragraph: "reveals this as systematically misleading: the preference for simplicity is itself shaped by the evolutionary pressure…" is unsupported, since FBT concerns perception, not theory choice. Rewritten so the void *illustrates* the tenet. A [P-V3](/positions/voids-as-evidence/#p-v3) line was added: "As a catalogue entry this void adds no weight to any tenet; the connections below are readings." *Seed*: TV L205.
- Stale Further Reading aliases ("Defended Territory", "The Phenomenology of the Edge", "The Calibration Void", "The Intersubjective Void") were replaced with live titles.
- "Whether transparency is functionally necessary becomes evident from…" was changed to "is tested by…", after the counter-case.

### Per-cite ledger (publisher of record)

- Alston 1986 (*PPR* 47(1): 1–30): real-correct metadata (JSTOR scan: Vol. XLVII, No. 1, Sept. 1986, last page 30). The body's inference was reversed and is fixed (item 7).
- Battaglia, Servajean & Friston 2025 (*Phys. Life Rev.* 52: 197–204, doi 10.1016/j.plrev.2024.12.009): real-correct metadata (Crossref/OpenAlex). The body overstated the paper (items 9–10). **Full text not read**: Cloudflare 403 at ScienceDirect and at the unibo repository, and the Elsevier API was rate-limited. The page now asserts only what the abstract says.
- Bostrom 2011 (*Rev. Contemp. Phil.* 10: 44–79): real-correct. The term was absent (item 6).
- Hoffman 2016 (*CDPS* 25(3): 157–161): real-correct. Was an orphan; now cited inline.
- Hoffman, Singh & Prakash 2015 (*PBR* 22(6): 1480–1506): real-correct. "Veridical perceptions escape extinction only if fitness varies monotonically with truth" (author manuscript) supports the "monotonic boundary" clause.
- Prakash, Stephens, Hoffman, Singh & Fields 2021 (*Acta Biotheor.* 69(3): 319–341, epub 2020): real-correct. The theorem statement was checked in the 2017 preprint; the published text is behind a Springer challenge (not read). Attribution fixed (item 11).
- Berke, Walter-Terrill, Jara-Ettinger & Scholl 2022 (*Cog. Sci.* 46(10): e13195): real-correct. The abstract supports "veridicality returning" ("as the number of independent utility functions increases, the distinction… dissolves").
- James 1902 (*Varieties*, Lectures XVI–XVII): real-correct. Paraphrase fixed (item 5).
- Letheby & Gerrans 2017 (*Neurosci. Conscious.* 2017(1), nix016): real-correct metadata. Misquote and misframing fixed (items 2, 4).
- Metzinger 2003 *Being No One*: real-correct. Quote fixed (item 1).
- Metzinger 2003, "Phenomenal transparency and cognitive self-reference" (*PCS* 2(4): 353–393): real-correct (OpenAlex). Not quoted.
- Metzinger 2024, *The Elephant and the Blind* (MIT, open access), ch. 19 "Witnessing", pp. ~209–212: real-correct. Was an orphan, now cited. The "more than 500" figure is verified ("For this book, I selected more than 500 of them").
- Nagel 1986: an orphan, removed (metadata not re-verified).
- Sellars 1956 (*Minnesota Studies* 1: 253–329): real-correct. The Harvard 1997 edition's note confirms vol. 1 and 1956 (eds. Feigl & Scriven); the page range is confirmed by the HSP 2015 bibliography.
- Ciaunica, Charlton & Farmer 2021 (*PCS* 20(1): 1–19, online 2020): real-correct (OpenAlex). The 10-01 repair holds.
- **New:** Deane 2020 (*PhiMiSci* 1(I): 1–27, doi 10.33735/phimisci.2020.I.39) and Deane, Miller & Wilkinson 2020 (*Front. Psychol.* 11: 539726). Both abstract-verified; every quoted span is from the abstract.

**Result-direction leg.** Berke (veridical wins as goals multiply), HSP 2015 (monotonic exception) and FBT (generic dominance) were each checked in direction. L&G's direction was reversed on the page and is fixed (item 4).

**Cited-author-stance leg.** Metzinger is a naturalist ("no such things as selves exist", BNO p. 1); Letheby & Gerrans are physicalist ("the self does not exist"); Deane and Deane et al. use active inference; Friston et al. are physicalist; Alston is a reliabilist and non-sceptical; Sellars is a naturalist and non-sceptical; Hoffman is a conscious realist, used here only for FBT. None is presented as endorsing dualism. The Dualism paragraph already concedes that physicalism explains the opacity equally well.

**Superlative sweep.** `find_superlative_claims` returned nothing.

### Engagements (editor-internal)

- Physicalist explanation of the opacity (Dualism paragraph): Mode Three, honestly marked. Unchanged.
- MWI branch-relative indexicality: Mode Three with Map-canonical cost framing. Compressed, not changed in substance.

### Counterarguments Considered

- Buddhist and contemplative persona: seeing through the self-construct is liberating, not pathological. Previously unaddressed and now answered with sources (item 12). This was a calibration issue, not bedrock.
- Physicalist, MWI and eliminativist disagreements remain bedrock and were not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The front-loaded lead; the "snap-back" and "dissolving insight" vocabulary; the five-condition falsifiability list; the desktop-icon analogy.
- The layered medium/operation/subject/causal distinction, and the causal-versus-representational bullet with the triple-screen anchor (all untouched).
- The calibrated Dualism and Bidirectional paragraphs from the 09-28 repair. The FBT statement (verified faithful).

### Enhancements Made

- The Contemplative Counter-Case subsection splits the thesis into a self-protecting half (weakened) and a self-concealing half (stands). This sharpens the void rather than diluting it.
- Alston and Sellars now carry their own non-sceptical morals, which makes the "missing cosmic guarantee" the precise void.
- Bostrom's "neuropsychological hazard" fits the page better than the misattributed term, because it is architecture-relative, which links to the AI paragraph.

### Cross-links

- None added. The `#the-contemplative-counter-case` internal anchor is new. Five Further Reading entries duplicated by the Distinguishing list were removed (mutation, transit, erasure, witnessing, expertise); their body links are untouched.

## Length

Before: 2670 words (`analyze_length`, soft_warning). After: 2951 (soft_warning, +281, below the 3000 hard gate). The corrections ran to about 3167 words. That was brought back by compressing Further Reading glosses, removing five duplicated Further Reading entries, folding the redundant "Destabilisation anxiety" paragraph into "Vertigo", shortening the MWI paragraph, and dropping one L&G quote. No calibration qualifier or rival's reply was cut.

## Remaining Items

- **Unverified**: the Battaglia et al. full text (abstract only). Whether the paper itself discusses observation altering the studied brain, or uses active-inference framing, is unknown. The page no longer depends on it.
- **Unverified**: the origin of "the power of models built by prior experience". It is not in L&G 2017, Aeon 2017 or REBUS 2019. Deane 2020's full text was behind a bot wall.
- **Not re-verified**: the many-worlds canonical claim that the Deutsch–Wallace derivation "requires" a cross-branch *personal-identity* relation (the page links to the canonical statement).
- **Sibling, noticed and not verified**: [depersonalisation](/concepts/depersonalisation/) L69 quotes Ciaunica et al. as "reveals the presence of an unnoticed window". Their abstract reads "may indicate the presence of an unnoticed window". The body text may differ (the Springer full text was not reachable). This is not this page's string, so no task was minted; it is worth a check at the next depersonalisation pass.
- Follow-ups minted (P3 refine-draft): one per archived predecessor, and one for dated Correction lines in the two research notes. A live-corpus grep found no live sibling carrying this page's defective strings, so no sibling task.

## Stability Notes

- Kept from 07-06: the bedrock disagreements (MWI indexicality, eliminativist framing, physicalist alternatives) are not to be re-flagged. Keep the layered-void distinction. Reference #2 is vol. 52; vol. 54 is the reply.
- **Amended from 07-06.** "The necessity claim is calibrated honestly… do NOT pressure it toward… weaker contingency" protected a *framework* reading. It also shielded an *empirical-support* claim (contemplative convergence) that the page's own references contradicted. The structural claim now rests on epistemic circularity, a verification limit no experiential report can touch. The *self-protecting* (destabilisation) half is held as weakened by contemplative evidence. Future reviews should not re-strengthen the lead's "dysfunction" generalisation without new evidence, and should not demote the verification limit.
- Alston and Sellars are non-sceptics. Do not re-install "cannot be justified" or "reinforces the point" phrasings.
- Five prior reviews certified this page without a verbatim ledger and missed 15 critical defects. The ledger above is the first; quote-level re-checks should start from it.