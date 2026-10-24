---
title: "Deep Review - Memory Anomalies: Déjà Vu, Jamais Vu, Cryptomnesia"
created: 2026-10-24
modified: 2026-10-24
human_modified: null
ai_modified: 2026-10-24T16:38:39+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[memory-anomalies]]"
  - "[[deep-review-2026-07-13-memory-anomalies]]"
  - "[[deep-review-2026-06-20-memory-anomalies]]"
  - "[[deep-review-2026-06-02-memory-anomalies]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-24
last_curated: null
---

**Date**: 2026-10-24 16:38 UTC
**Article**: [[memory-anomalies|Memory Anomalies: Déjà Vu, Jamais Vu, Cryptomnesia]]
**Previous review**: [[deep-review-2026-07-13-memory-anomalies|2026-07-13]] (attribution framing and quote fidelity). Earlier: [[deep-review-2026-06-20-memory-anomalies|06-20]], [[deep-review-2026-06-02-memory-anomalies|06-02]] (metadata only), 05-09c, 05-09b, 05-09.
**Pass type**: Source-fidelity pass on the 10-23 disputed-memory paragraph, then the first **result-direction** pass over the empirical citations (§2.4 step 7), and a hub-over-spoke check against the apex.
**Word count**: 3533 → 3598 (`analyze_length`; topics hard gate 4000, gate `>=`). +65 net: three references added, one removed, and the body trimmed to pay for the corrections.

## Delta since the last review

`git diff b880facf..HEAD`: the only body change was the 10-23 refine-draft paragraph "Cryptomnesia has a converse" plus the two Sheen, Kemp & Rubin references. The rest of the page was unchanged since 07-13.

## L100 fidelity (the priority lens)

- **Sheen, Kemp & Rubin 2001.** State: real-correct. Crossref: "Twins dispute memory ownership: A new false memory phenomenon", *Memory & Cognition* 29(6): 779–788, DOI 10.3758/bf03196407. Authors Mercedes Sheen, Simon Kemp, David Rubin.
- **Sheen, Kemp & Rubin 2006.** State: real-correct. Crossref: "Disputes over memory ownership: What memories are disputed?", *Genes, Brain and Behavior* 5(S1): 9–13, DOI 10.1111/j.1601-183x.2006.00189.x.
- **Quotes.** All four are verbatim. The skirt sentence was checked in the PubMed abstract (PMID 11716051). The two body quotes were checked in the full text: "good agreement on most aspects of the memory except who the protagonist was" (p. 784) and "the measures of memory quality provide no indication" (p. 783). The full text is the DukeSpace copy (hdl 10161/10137), grepped after normalising hyphens and whitespace. The 2006 quote is in its PubMed abstract (PMID 16417612).
- **Figures.**
  - "Most twins tested reported at least one": 70% of twin sets in Exp. 1 and 65% of respondents in Exp. 2. Supported.
  - "Far fewer": 8% of respondents with siblings within two years of age, against 65% of twins (Table 5, p. 785). Supported.
  - "77 such memories": in the 2006 abstract, 71 of them from twins. Supported.
  - Higher reliving and imagery ratings: in the 2001 abstract. Supported.
- **One fix.** "Close siblings" is the authors' term for siblings within two years of age, but a reader would take it as emotional closeness. Changed to "siblings close in age and same-sex friends", which matches the abstract.
- **Considered and left.** The text gives the "no indication" quote's object as "of which twin was wrong", where the source says "of this", meaning partial fabrication. The gloss sits outside the quote marks, and the 2006 paper (p. 12) says detail "does not actually help resolve memory ownerships". Left as is.
- **Inference.** The paragraph frames disputed memory as a source-monitoring error about *whose* memory it is. It treats the IEM question as conditional, and it makes no consciousness or dualism claim. Its IEM verdict matches the spoke `concepts/immunity-to-error-through-misidentification` L44 (Shoemaker's de facto immunity; Evans's dispute), so the hub is not stronger than the spoke.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

1. **Result-direction inversion, TLE (L78).** The page said that Illman et al. 2012 and Martin et al. 2012 show "recollection is impaired, but familiarity appears largely spared". Martin et al. 2012 (PMID 22841992; the finding is in its title) report the reverse. TLE patients with déjà vu have interictal deficits "limited to familiarity-based responses", and these "spared their ability to engage recollective processes". Patients without déjà vu are impaired more broadly. Illman et al. 2012 (PMID 22957231) propose a "decoupled familiarity" account with a parahippocampal locus. The page's gloss "familiarity firing without the recollection channel available to check it" also contradicted Spatt 2002, whose abstract credits normal hippocampal and prefrontal function with déjà vu's "perplexing" quality. The paragraph was rewritten to report both papers' actual findings and Spatt's division. The inversion was seeded by `research/memory-anomalies-2026-05-08` L93 and survived five reviews, because those reviews checked metadata only.
2. **Wrong figure, Brown 2003 (L64).** The page said "Roughly two-thirds of healthy adults". The publisher abstract (PMID 12784936) says "About 60% of the population". The 05-09b review had certified the figure because it matched the research note, which is intra-corpus ratification. Now "About 60% of people report having had déjà vu (Brown 2003)".
3. **Result misattribution, cryptomnesia mechanism (L64, L74).**
   - The page said cryptomnesia "is robustly produced by dividing attention away from source-monitoring" and that "Marsh and Bower's puzzle-task paradigm suggests that subjects under cognitive load reliably claim previously-presented items".
   - Neither paper manipulates attention or load. Marsh & Bower 1993 (abstract via OpenAlex) varied retention interval and degree of encoding. Brown & Murphy 1989 found plagiarism in all three tasks of every experiment, "greater under more complex generation sequences".
   - Both sentences now describe the actual turn-taking paradigms. The load point now rests on Brown & Murphy's complexity finding.
   - "Source-monitoring is metabolically expensive" (uncited physiology) became "effortful".
   - Macrae, Bodenhausen & Calvini 1999 (*Social Cognition* 17(3): 273–297) does test cognitive distraction. It was **not** cited, because its abstract does not state the direction and the secondary sources conflict.
4. **Inline cite with no reference, plus the premonition result credited to the wrong paper (L72).**
   - "Cleary's gestalt familiarity hypothesis (2008, 2012)" had no 2012 reference entry.
   - The configural virtual-reality result is Cleary, Brown, Sawyer et al. 2012, *Consciousness and Cognition* 21(2): 969–975 (PMID 22322010). Its abstract says déjà vu reports were "higher", which does not support "reliably report".
   - The premonition finding is Cleary & Claxton 2018, *Psychological Science* 29(4): 635–644 (PMID 29494276): "increased feelings of knowing the direction of the next turn" with no "above-chance ability to predict". It was not cited anywhere on the page.
   - Both references were added, the passage was rewritten, and L104's paranormal deflation now cites 2018 for the authors' own hedged explanation ("metacognitive bias … may explain"). Before the fix, L104 asserted that the match "equally well-explained" both feelings.
5. **Misattribution, the CSDT cluster (L70).** The page presented "Wixted and Mickes's continuous-signal-detection account" as holding that familiarity and recollection are "*quantitatively* different rather than *qualitatively* distinct processes". In fact:
   - Wixted & Mickes 2010 (PMID 20836613) propose a model that "does not deny … the validity of dual-process theory".
   - Wixted 2007 (PMID 17227185) is a "dual-process version of signal-detection theory" in which decisions "are not process pure".
   - Wixted & Squire 2010 (PMID 20412819) argue the medial temporal lobe is organised "in terms unrelated to" the distinction.
   - Only Cohen et al. 2008 (one-dimensional model preferred; PMID 18926982) and Pratte & Rouder 2012 ("single mnemonic process"; PMID 22563630) go to a single dimension.

   The sentence was rewritten to give each position to its author. The architecture-independence argument that follows is unchanged.
6. **Hub stronger than the apex, and an inverted conditional (L118, Further Reading L135).**
   - The page said "the cluster-level move reaches the strongly-supported tier only conditional on the common-cause-null *surviving* the discrimination tests". That is logically inverted: the null surviving defeats the move.
   - The apex [[phenomenal-output-causal-machinery-dissociation]] also changed under this page. Apex-evolve on 09-14 (commit 0f794c58b3) added that the dissociation catalogue, "the déjà vu family" included, "is also the predicted null of mainstream cognitive architecture". The apex now holds that "Compatibility is not support", and its strong-rival section grants that predictive-processing introspection "absorbs the whole shape". No apex text now holds out a strongly-supported tier.
   - L118 was rewritten to the apex's position: the move sits at *live hypothesis*, and even a defeated null would leave the unified rival. The Further Reading annotation repeated the inversion and was cut down to a pointer.
7. **Hub stronger than the apex (L110).** "The trio cleanly exhibits the irreducibility the tenet asserts" was stronger than the apex, and it clashed with the paragraph's own "not by itself evidence for or against dualism". Now "locates, at small scale, the residue the tenet's case turns on". The close cites the apex concession that the pattern is the mainstream prediction and that what stays open is why the verdict is felt.
8. **Bergson compatibility used as evidence (L112).** "the rarity of déjà vu given the contemporaneity of memory and perception is one piece of indirect evidence" took a consequence of Bergson's hypothesis as evidence for the filtering reading. Now: "that rarity is a consequence of his hypothesis, not independent evidence for it". The Tenet 3 close now reads "fits the tenet without evidencing it", and the quantifier is left unresolved.
9. **Misattribution, "reducing valve" (L88).** The page said "the mind acts as a 'reducing valve'" as Bergson's picture. The phrase is Huxley's, and Huxley's valve is the brain. That is how `concepts/filter-theory` L77 and `voids/edge-states-and-void-probes` L83 have it. Rewritten, with a piped link to [[filter-theory|filter theory]].
10. **Orphan reference with wrong authors.** The page listed "Sutton, J., & Cassam, Q. 'Memory.' SEP". The live SEP entry (citation_author meta) is by **Kourken Michaelian and John Sutton**, first published 2017, and the page never cited it inline. Removed.

### Medium Issues Found

- **Stimulation claim (L78) was uncited and partly wrong.** The page said "perirhinal and parahippocampal cortices … on demand". Bartolomei et al. 2004 (*Neurology* 63(5): 858–864, PMID 15365137) associate déjà vu with entorhinal stimulation and reminiscence with perirhinal stimulation. Now "rhinal cortex, especially entorhinal cortex", with "on demand" dropped and the reference added. Also dropped: "reliably produces" became "Some patients … consistently experience", in Martin et al.'s wording, and the uncited "right-side" laterality went.
- **Production language (brief calibration).** "a brain substrate produces the signal" became "is implicated in"; "mechanical stimulation produces the felt pastness" became "electrical stimulation can elicit"; and "the signal-pattern that *produces* felt pastness" became "*triggers*". Stimulation eliciting an experience is brain-to-mind causation that interactionism accepts, so no epiphenomenalist concession was introduced.
- **Perrin, Moulin & Sant'Anna gloss (L80).** "a malfunction of episodic remembering as a competence" did not match their abstract. They argue recollection "is not involved in déjà vécu … as an actual mental state", and on their "ability view" déjà vécu "involves the feeling that one could recollect past occurrences". Rewritten to match.
- **"Inadvertent plagiarism" (L96)** is Brown & Murphy's title phrase. Marsh & Bower's title says "unconscious plagiarism". Reattributed.
- **Necessity heading.** "Cryptomnesia and the Necessary Opacity of Source" was stronger than its own body, which says "may not be able to have". It became "…and the Opacity of Source". No anchor links pointed at it. L96 was hedged in the same way: "requires" became "draws on", and "would be unable" became "might be unable".
- **Style and redundancy.** The Bergson "candidate, not commitment" caveat appeared twice in the second lead paragraph and again at L90. One instance was kept in the lead, and L86 still carries it. Three "load-bearing" intensifiers were removed. The one that remains (L70) marks a real premise.

### Counterarguments Considered

- Physicalist / predictive-processing absorption of the whole pattern is the apex's strong rival. L110 and L118 now concede it in the apex's terms. This is bedrock at the felt-character residue. It is not something to fix.
- Paranormal readings: the reply is Mode One, defeated on the evidence (Cleary & Claxton 2018). This is now cited correctly.

### Citation ledger (result-direction leg done for every empirical cite)

- Bartolomei et al. 2004 — real-correct; added (supports the stimulation sentence)
- Bergson 1908 — real-correct (07-13)
- Brown 2003 — real-correct metadata; **figure wrong** (two-thirds → 60%, fixed)
- Brown & Murphy 1989 — real-correct metadata; **result misdescribed** (divided attention → turn-taking paradigm; complexity effect, fixed)
- Cleary 2008 — real-correct
- Cleary et al. 2012 — real; **inline orphan** (reference added)
- Cleary & Claxton 2018 — real; **missing source for the premonition result** (added)
- Cohen, Rotello & Macmillan 2008 — real-correct; direction faithful once reattributed
- Flournoy 1900 / Jung 1905 — real-correct (07-13 framing)
- Illman et al. 2012 — real-correct metadata; **result misdescribed** (fixed)
- Marsh & Bower 1993 — real-correct metadata; **result misdescribed** (load, fixed)
- Martin et al. 2012 — real-correct metadata; **result inverted** (fixed)
- Moulin et al. 2021 — real-correct; the overstated "reliably" at L61/L64 is **owned by the queued P3** (see Remaining Items)
- Perrin, Moulin & Sant'Anna 2024 — real-correct (online 2023, issue 2024); gloss corrected
- Pratte & Rouder 2012 — real-correct; direction faithful
- Sheen, Kemp & Rubin 2001, 2006 — real-correct; quotes verbatim; figures supported
- Spatt 2002 — real-correct; now cited for the division it actually draws
- Sutton & Cassam (SEP "Memory") — **real-wrong-metadata** (Michaelian & Sutton 2017) **and orphan** — removed
- Wixted 2007; Wixted & Mickes 2010; Wixted & Squire 2010 — real-correct metadata; **position misattributed** (fixed)
- Superlative helper: not run separately. The page's only superlative ("the most useful empirical fact in the entire literature") is marked as the Map's own reading.

### Cited-author stance

- Wixted, Squire, Cohen, Pratte and Rouder are mainstream memory scientists, with no metaphysical commitment in these papers.
- Cleary is a cognitive psychologist who explains premonition as metacognitive bias, which is deflationary.
- Perrin, Moulin and Sant'Anna are philosophers of memory with no dualist commitment.
- Bergson is a spiritualist dualist in his own right. He is recorded as a candidate and never enlisted as evidence; the apex likewise counts him "a parallel proposer rather than a witness".
- No author is presented as endorsing the Map's conclusion.

## Optimistic Analysis Summary

### Strengths Preserved

- The architecture-independence move in the CSDT paragraph. It is now stronger, because the contest it insulates against is described accurately.
- The déjà vu / déjà vécu distinction.
- The Cleary premonition point as the page's key exhibit, now correctly sourced.
- The cryptomnesia section. The disputed-memory converse is a good addition and passed fidelity.
- The common-cause self-reference honesty block, recalibrated rather than removed.

### Enhancements Made

Fixes were made in place rather than by expansion: one piped cross-link and three references. Trims elsewhere paid for them: the duplicated Bergson caveat, the Further Reading annotations, the cluster-list redundancy, and the source-attribution-divergence pointer.

### Cross-links Added

- [[filter-theory]] (piped, L88)

## Hub-over-spoke results

- source-attribution-void: the spoke is **stronger** than the hub ("Humans cannot retain it even with effort"; "not a difficulty better training could overcome", L112–114). The hub's "may not be able to have" is weaker. That is fine for the hub, but it is a lead for the spoke (below).
- immunity-to-error-through-misidentification L44 and quasi-memory L102: consistent with the hub's L100.
- apex phenomenal-output-causal-machinery-dissociation: the hub **was stronger** at L110 and L118. Fixed (items 6 and 7).
- recognition-void, noetic-feelings-void and memory-channel-interface-evidence appear only in Further Reading. The hub states no verdict there that they own.

## Remaining Items

- **L61 and L64 jamais-vu "reliably" claims: left untouched.** They are owned by the queued P3 "Fold semantic satiation into `concepts/phenomenal-constitution-thesis`…", part (3).
  - The research note's replacement text (`research/semantic-satiation-and-felt-meaning-2026-10-15` L171) targets the **L64** sentence, though the P3 labels it L61. L61 ("a reliable inducer") is a second instance.
  - A sentence saying so was appended to that P3's Notes line. `parse_tasks` counts are unchanged (215 active).
- "Selective recall plus retrofitting … plausibly accounts for many 'precognitive dream' reports" is still uncited. It was softened from "most".
- Jung's Nietzsche age ("eleven"): Jung's 1902 dissertation gives twelve to fifteen, and later accounts give about eleven. Left, since it matches the 1905 essay as secondary sources report it.

## Leads for other pages

- **`topics/source-attribution-divergence` L117** has the **same inverted conditional** ("strongly-supported tier only conditional on the common-cause-null surviving the discrimination tests"). The same 05-19 refine (3e1997691e) installed both. It is stale against the post-09-14 apex in the same way.
- **`research/memory-anomalies-2026-05-08` L93** carries the inverted TLE claim ("recollection is impaired but familiarity is largely spared"). It is a historical note, but any future article mined from it inherits the inversion.
- **`voids/source-attribution-void` L112–114** ("Humans cannot retain it even with effort"; "not a difficulty better training could overcome") needs a permanent-void calibration check. Its own L98 cites subliminal-encoding evidence, so the claim may be scoped. Not verified here.

## Stability Notes

- Carried forward, do not re-flag: the physicalist/heterophenomenological dissolution, the eliminativist denial of the explanandum, and the empiricist unfalsifiability objection are all bedrock. So is the predictive-processing unified rival, now conceded at the apex's level.
- Do not restore "two-thirds" (Brown 2003's abstract says 60%), "recollection impaired, familiarity spared" (the inverse of Martin et al. 2012), or the divided-attention attribution to Brown & Murphy / Marsh & Bower.
- Do not cite Macrae et al. 1999 for a distraction direction without a full-text check of its Exp. 2.
- Do not reinstate the strongly-supported conditional at L118 unless the apex itself grants a tier.
- 07-13 notes still hold: the Marsh paraphrase stays de-quoted; Flournoy coined and Jung developed; the "The the the the" title is real.
