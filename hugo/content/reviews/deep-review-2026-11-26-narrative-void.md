---
ai_contribution: 100
ai_generated_date: 2026-11-26
ai_modified: 2026-11-26 22:50:00+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-26
date: &id001 2026-11-26
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-26 22:50:00+00:00
modified: *id001
related_articles: []
title: Deep Review - The Narrative Void
topics: []
---

**Date**: 2026-11-26
**Article**: [The Narrative Void](/voids/narrative-void/)
**Previous review**: [2026-07-14](/reviews/deep-review-2026-07-14-narrative-void/)

**Scope**: A full re-verification of every quotation, attribution and empirical claim at source. The four prior reviews (2026-03-11, 05-17, 06-04, 07-14) had certified the original cluster as "real-correct" and "quote-faithful". That certification did not survive a grep of raw text. The seed note ([research/voids-narrative-void-2026-02-25.md](/research/voids-narrative-void-2026-02-25/)) drew on Wikipedia, IEP and secondary summaries for its quotations. Of its four quoted strings, the 05-17 review caught one (Ricoeur, which is actually IEP's paraphrase), the 07-14 review caught two (Strawson, Schechtman), and this pass caught the fourth (the Gazzaniga "glue" sentence). The 2026-08-06 per-trial detection-rate fix (0050e95de3) was read in git and preserved verbatim ("Most manipulated trials went undetected."). The video embed was not touched.

**Length** (`tools.curate.length.analyze_length`; voids soft 2,000, hard 3,000, gate `>=`): 2,342 → 2,547 (+205). The additions are calibration and attribution repairs. They were offset in part by cutting the Encoding-Void Further Reading gloss, which duplicated the body (about −65 words), the sub-cluster clause, and two Relation-section sentences. The article remains 453 words under hard.

## Pessimistic Analysis Summary

### Publisher-of-Record Citation Ledger

- **Nisbett & Wilson 1977** (*Psych. Rev.* 84(3), 231–259; DOI 10.1037/0033-295x.84.3.231). **State: real-correct** for metadata. **Dropped qualifier (CRITICAL, fixed).** The abstract (OpenAlex record of the publisher abstract) reads: "Evidence is reviewed which suggests that there may be little or no direct introspective access…". It also says: "This suggests that though people may not be able to observe directly their cognitive processes, they will sometimes be able to report accurately about them." The article had "landmark 1977 *study* *established* that people have 'little or no…'". It now reads "review concluded that the evidence 'suggests that there may be little or no…'", and the accurate-when-the-theory-fits condition is restored. **Result-direction leg**: confirmed. The Occam paragraph's "systematically wrong" contradicted the paper's own accuracy condition and was rewritten. The process/content sentence's "systematically unreliable" was replaced with the concept page's own word, "confabulation-prone".
- **Gazzaniga & LeDoux 1978**, *The Integrated Mind* (Plenum; Crossref DOI 10.1007/978-1-4899-2206-9). **State: real-correct; ADDED.** This is the originating report of the chicken-claw/snow-shovel run. The article had credited the demonstration only to Gazzaniga via the 1998 popular book, so co-originator LeDoux is now named.
- **Gazzaniga 1998**, *The Mind's Past* (UC Press). **State: real-correct** for metadata. **"Glue" quotation unverifiable (CRITICAL, de-quoted).** The string "the glue that keeps our story unified and creates our sense of being a coherent, rational agent" was not found anywhere searchable. The archive.org item `mindspast00gazz` is lending-restricted (inside-search returns 403 and the djvu text returns "Item not available"). It is absent from the full text of *The Ethical Brain* (archive.org; the only "glue" there is "the glue that keeps our species… from destroying itself") and from Gazzaniga 1998 *Sci. Am.* "The Split Brain Revisited". Three web searches found no primary text. The current Wikipedia article carries only a paraphrase ("the glue that attempts to hold the story together"). The seed note took the string from a secondary source with an obvious transcription error ("sense of being into"), which the 03-11 review corrected by conjecture and later reviews certified as "verbatim". The sentence is now an unquoted paraphrase attributed to "Gazzaniga's account". The 07-14 review's "confirmed verbatim" was false.
- **Chicken-shed quotation**: "you need a shovel to clean out the chicken shed" **appears verbatim in Gazzaniga's own retelling** (NPR, 2017-06-15, Gazzaniga quoting the patient: "Well, the chicken claw goes with the chicken, and you need a shovel to clean out the chicken shed."). *Sci. Am.* 1998 paraphrases ("It said the right hemisphere chose the shovel to clean out a chicken shed"). Retellings vary in their opening words, but the quoted substring is common to them. Kept in quotation marks. "Confabulated without hesitation" was replaced with "quickly supplied a reason", grounded in *Sci. Am.* 1998: "Yet it quickly made up an explanation. We dubbed this creative, narrative talent the interpreter mechanism."
- **Johansson, Hall, Sikström & Olsson 2005** (*Science* 310(5745), 116–119; DOI 10.1126/science.1111709). **State: real-correct.** The abstract was verified via OpenAlex. The "normal confidence" claim was checked against the authors' own LUCS summary: in Johansson et al. 2005 the authors compared manipulated and non-manipulated reports on "emotionality, specificity and certainty", and "no substantial differences… were found". The body now states exactly those three dimensions. "Demonstrated that people fail to notice" became "showed that people often fail to notice", matching the authors' summary wording ("participants often fail to notice glaring mismatches").
- **Pupillometry sentence (CRITICAL, currency and fidelity, fixed).** The article said "Pupillometric extensions of the paradigm sharpen the structural finding". Grassi, Hoeppe, Baytimur & Bartels 2025 (*Front. Psychol.* 16, 1598254; abstract verified via OpenAlex) conclude the opposite: "Our results cast doubt on the general validity of CB… suggest no failure of detection, but instead higher-level, cognitively or socially driven hesitance of reporting… participants are less introspectively blind than originally portrayed." Pärnamets, Johansson, Strandberg, Balkenius & Hall 2023 (PsyArXiv, DOI 10.31234/osf.io/v85sz; abstract verified) read the same dilation as "possibly indicating effortful rationalization" and "reject notions that participants are aware of, but fail to report". The sibling exhibit [pupillometry-behavioural-channel](/topics/pupillometry-behavioural-channel/) already carried this contest. This page had never been updated to match it. The sentence now presents the dispute, quotes Grassi's verbatim clause, and ADDS both references. The downstream sentence "If the original reading holds…" and "we *may* be blind to what we chose" were scoped to match.
- **Ricoeur 1984–1988**, *Time and Narrative* (U. Chicago Press). **State: real-correct** for metadata. The primary text is lending-restricted on archive.org (`timenarrative0001ricu`, 403). **Source/Map conflation (CRITICAL, fixed).** The article said "Ricoeur argued that experience is always already narratively structured". On IEP's account of the threefold mimesis, Ricoeur's mimesis₁ is a field of action "always already *prefigured*". That level lies beneath emplotment (mimesis₂). So "always already" attaches in Ricoeur to prefiguration, not to narration, and Ricoeur himself keeps a pre-emplotment level. The article now says Ricoeur argued that human time becomes intelligible through narrative and marks the strong "narrative is the very form of experience" reading as the Map's radicalisation of him. Editor label: *Map reconstruction*. IEP also confirms that the after/because-of wording the 05-17 review de-quoted is IEP's own paraphrase ("the relation of one thing because of another").
- **Schechtman 1996**, *The Constitution of Selves* (Cornell UP). **State: real-correct** for metadata. **Attribution overreach (CRITICAL, fixed).** The article attributed to Schechtman both the constitution thesis and the multiplicity claim ("but the narrative any person settles on is only one of many…") and then said "None has privileged access to what 'actually happened'". On SEP *Personal Identity and Ethics*, her view answers the "characterization question" (1996 ch. 4), not reidentification. A secondary source (PMC5895654, citing pp. 114 and 119) states her articulation constraint and her reality constraint, under which the narrative must "fundamentally cohere with reality". The multiplicity claim was never verified as hers. It is now marked as the Map's observation operating within her constraints, and the closing line now says the reality constraint cannot choose among reality-consistent stories.
- **Strawson 2004**, "Against Narrativity" (*Ratio* 17(4), 428–452). **State: real-correct.** The primary text was unreachable: trepo.tuni.fi is blocked by bot protection, philarchive returns 403, and the cuni.cz copy requires a Moodle login. A web-fetch agent confirmed all three. The quotation was grepped in a peer-reviewed reproduction (PMC6633324, Europe PMC full text): "I have absolutely no sense of my life as a narrative with form, or indeed as a narrative without form. Absolutely none." [p. 433]. **Dropped qualifier (fixed):** the same source has Strawson calling himself "fairly Episodic", and the article had "identifies himself as episodic". The quote now runs to the end of the sentence with a page cite (the article had closed it with a period mid-sentence). "Diachronic" and "Episodic" are capitalised, as in Strawson.
- **Damasio 1999**, *The Feeling of What Happens* (Harcourt). **State: real-correct.** **Cited-author-stance leg (fixed):** the article now notes that Damasio, a neurobiological naturalist, treats both the core and the autobiographical self as brain constructions. "Prior to narrative construction" became "prior to autobiographical narration", since Damasio's core self is not narrative-free in any sense the Map can borrow.
- **Yang et al. 2024** (*Science* 383(6690), 1478–1483; PMID 38547293). **State: real-correct.** **Dropped qualifier (species, fixed):** the abstract is explicitly "large-scale neural recordings in mice", and the article said nothing about species. Ripples occurred "during reward consumption" and decoded "trial blocks". The article's "particular experiences… during the pause after a rewarding event" is now "particular stretches of experience" "during reward consumption", prefixed "In mice".
- **Lindsey & Litwin-Kumar 2024** (*eLife* 12, RP90793; PMID 39023518). **State: real-correct.** The two-author fix from 06-04 holds. **Mischaracterisation (fixed):** the abstract says the model "prioritizes the storage of synaptic changes that are consistent with prior updates to the short-term system", and calls it a proposal. The article's "consistent with what is already stored" and its summary criterion "schema-fit" overstated this as schema-matching. The text now reads "consistency with prior short-term learning", and the summary criterion is "consistency".
- **Radvansky & Zacks 2017** (*Curr. Opin. Behav. Sci.* 17, 133–140; DOI 10.1016/j.cobeha.2017.08.006, Crossref). **State: real-correct** for metadata. **Currency (fixed):** McFadyen, Nolan, Pinocy, Buteri & Baumann 2021 (*BMC Psychology* 9, 41; abstract verified) found "no significant effect of doorways on forgetting" across four experiments, apart from an interference effect under working-memory load. They call into question "the generalisability and robustness of this effect". Added as "though not replicated robustly across paradigms", with a reference.
- **Ongchoco & Xu 2024** (*J. Vis.* 24(9), 9; PMID 39259169). **State: real-wrong-metadata (article number missing; was "24(9)", now "24(9), 9").** The abstract frames "memory flushing" as a hypothesis in scare quotes ("perhaps because event boundaries serve as cues to clear obsolete information") and reports "a consistent memory decrement for the first image encoded". The article had asserted "the working-memory buffer is *flushed*". It now reads "event boundaries may *flush* working memory… a decrement found even under active maintenance".
- **"At millisecond scale… below conscious access" (fixed).** Recall-gating is a model with no timescale, and event boundaries are consciously reportable (that is how segmentation is measured). The sentence now says the criteria are "applied automatically, without the subject choosing or monitoring it". The stability-protected closing clause ("without, on their own, settling what consciousness is") is preserved verbatim.

Inline ↔ References: all 15 References entries are named in the body (by author and year, or by author and work), and every inline author-year cite has an entry. The Mind's Past stays as the general source for "Gazzaniga's account" of the interpreter.

### Map-Internal Paraphrase Checks (re-grepped)

- **Independence-scoring exhibit (CRITICAL, internal contradiction, fixed).** The article said the exhibit "scores" the cluster and that "this void's anchors (Nisbett-Wilson, Gazzaniga, Johansson-Hall) contribute to the cluster's healthy-adult despite-commitments channel". The exhibit says it "assigns no graded score". It places Gazzaniga in the **patient-population** channel (L99) and Nisbett-Wilson and Johansson-Hall in the healthy-adult channel (L101), and classes all three as despite-commitments (L112). The text now reads "audits", with the correct channel split.
- [voids-circularity-discount](/project/voids-circularity-discount/) L123: the four criteria are "the calibration apparatus this discount operates **with**", where the article had "against". Corrected.
- [process-content-distinction](/concepts/process-content-distinction/) L37: "confabulation-prone", "higher evidential weight", "neither side is exempt from error". These now match.
- [narrative-coherence](/concepts/narrative-coherence/) L33: "the felt quality of a life making sense as a unified story" is verbatim. OK.
- [tenets](/tenets/) wording: Tenet 1 is "There is more than just matter involved in reality", with irreducibility as its definition. The "subject who *receives* the narrative" goes beyond Tenet 1 to background Posit One (a determinate, persisting subject; tenets.md L184 and L54). The Relation section now credits the rejection of Dennett to "its dualism and its background posit of a determinate subject, not… the confabulation data". It links [background-commitments](/tenets/background-commitments/).

### Tenet Calibration ([P-V3](/positions/voids-as-evidence/#p-v3): a void supports no tenet)

- **Dualism paragraph (CRITICAL as calibration, fixed).** [voids-as-evidence](/positions/voids-as-evidence/) [P-V1](/positions/voids-as-evidence/#p-v1) records that "illusionism predicts the introspection-architecture cluster". The article's rejection of Multiple Drafts read as if the void bore on the question. Grade: **compatible**, not suggestive or discriminating. The paragraph now says so in prose, and says the void on its own settles neither whether there is a self to know nor whether there is not. The old line "not evidence that there is no self to know" was itself one-sided.
- **Occam paragraph.** It was graded "illustrates". It now says outright that a physicalist draws the same lesson, so the case illustrates the tenet without supporting it.
- **Bidirectional paragraph.** Already modal ("might", "would then"), consistent with tenets.md ^tenet-3-standing. No change.

### Internal Consistency and Style

- The lead's "Consciousness constructs a running story" conflicted with the body (a physical interpreter constructs it) and with the Relation section (narrator versus audience left open). It now reads "The mind constructs". The "Unexplored" layer's "by which consciousness converts" was fixed the same way.
- "Every moment of conscious experience passes through narrative processing" contradicted the Episodic section and the conditional Ricoeur layer. It now reads "Much of conscious life".
- "Fabrication presents itself with the same phenomenological confidence as genuine memory" and "same phenomenological texture as genuine memories" claimed more than the evidence: Johansson et al. measured report dimensions, not phenomenology, and studied reasons, not memories. Both are now scoped to expressed certainty in the choice-blindness reports.
- Banned construct removed in four places: "This void is not merely an epistemic limitation. It is…", "This is not a pathology confined… The interpreter operates…", "This is not passive ignorance but active concealment", and "…not only about what the narrative loses or fabricates. It encompasses…". "The narration does not distort a signal; it may constitute the signal" became "Rather than distorting a signal, the narration may constitute it." No "load-bearing" in the article.
- "Reveals that narration is not given but built" became "plausibly built rather than given". "Demonstrates that the void has variable depth" became "suggests".
- Pronoun check: done after each replacement. "The reports feel like self-knowledge" (after the N&W rewrite) is fine. "It is a void in self-knowledge" was merged into the preceding sentence. "If the original reading holds, choice blindness extends…" replaces an ambiguous "This finding", whose antecedent had become the contested pupil sentence.

### Engagement Mode Classifications (editor-internal)

- Dennett (Multiple Drafts): **Mode Three**, now honest about evidential parity. The Map's rejection is labelled as framework-sourced, and the data are declared non-discriminating.
- Grassi et al. versus Pärnamets et al.: reported as an open empirical dispute. No Map-side adjudication.
- No label leakage.

### Counterarguments Considered

- Illusionist: the confabulation data predict "no self behind the story". The article now concedes evidential parity instead of implying the void favours the Map. This is a bedrock disagreement at the subject posit, and it is honestly marked.
- Covert-detection deflation (Grassi 2025): it may dissolve part of the "fabricates reasons for choices that never occurred" claim. Now presented as live.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-layer structure, "haunted by its unnarrated alternatives", "flash of groundlessness", the traveller-and-map close, and the Pre-Selected Material section's empirical/metaphysical boundary clause, verbatim, per the 06-04 stability note.
- The Hardline-Empiricist persona's praise now applies more widely. The page now shows, rather than merely avoids, the "tenet-coherent, not evidence-elevating" pattern in its Relation section.

### Enhancements Made

- Contested-evidence framing for choice blindness (the two pupillometry readings), the doorway-effect replication caveat, the species qualifier for the ripple finding, and an honest Ricoeur/Map boundary.

### Cross-links Added

- [background-commitments](/tenets/background-commitments/) (Posit One, the actual source of the "receiving subject").

## Remaining Items

None on this page. Cross-page follow-ups are listed in the driver report: siblings carrying a dropped Nisbett-Wilson "may be" and a word-order quote error, and the 28 live choice-blindness pages without the Grassi contest.

## Stability Notes

- The "glue" sentence is **not** a verifiable quotation. Do not restore quotation marks unless the 1998 text is grepped and the page cited.
- The chicken-shed substring is verified in Gazzaniga's own 2017 retelling. Do not re-flag it unless a scan of the 1978 or 1998 text shows a different substring.
- The Strawson quote is verified via PMC6633324 (p. 433). The primary text was unreachable on 2026-11-26.
- The choice-blindness interpretation is genuinely contested (Pärnamets 2023 versus Grassi 2025). Future reviews should update the framing if the Pärnamets preprint is published or a replication settles it, but should not restore "sharpen the structural finding".
- Dennett and illusionism: a bedrock disagreement at the subject posit (Mode Three). The page now states the evidential parity. Do not push it toward "the void favours dualism".