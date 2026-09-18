---
ai_contribution: 100
ai_generated_date: 2026-09-18
ai_modified: 2026-09-18 05:59:19+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-18
date: &id001 2026-09-18
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-18 05:59:19+00:00
modified: *id001
related_articles: []
title: Deep Review - Plant Cognition and the Plant-Neurobiology Debate - 2026-09-18
topics: []
---

**Date**: 2026-09-18
**Article**: [Plant Cognition and the Plant-Neurobiology Debate](/topics/plant-cognition-and-the-plant-neurobiology-debate/)
**Previous review**: [2026-08-01](/reviews/deep-review-2026-08-01-plant-cognition-and-the-plant-neurobiology-debate/) (and [2026-07-15](/reviews/deep-review-2026-07-15-plant-cognition-and-the-plant-neurobiology-debate/), [2026-07-08](/reviews/deep-review-2026-07-08-plant-cognition-and-the-plant-neurobiology-debate/))
**Trigger**: cycle-slot deep-review. Top two candidates (`concepts/ai-ensoulment-hypothesis`, `topics/cross-architecture-llm-introspection`) skipped per driver instruction — both edited today. This was the next eligible candidate at score 49.
**Disposition**: NOT a no-op. Three critical claim-fidelity defects and one unsupported claim fixed; four citations corrected to version-of-record. Word count 2798 → 2977 (+179; 99% of the 3000 soft threshold, so **no** length-neutral constraint applied, but the next pass will be at the ceiling).

## Why the prior stability note did not cover this article

The 08-01 review closed with three stability notes, one of which read: *"Do not re-run the metadata or quote lenses. Metadata verified 07-08 (11 cites) and 08-01 (12 cites incl. the new Feinberg & Mallatt entry); quotes verified 07-15."*

That note was accurate when written and is now **the record of a lens not run on material that did not yet exist**. Two `refine-draft` commits landed after it:

- `be02ae525f` — *"plant-cognition Tier 1 — the skeptic case is broader than neural necessity"*, which added the whole closing paragraph of Relation to Site Perspective (Calvo et al. 2021, Mallatt et al. 2021, Segundo-Ortin & Calvo) including **three inline quotations**.
- `9cdab58615` — *"Update plant-cognition citations — the debate ran on for six more years than the article shows (0 cites after 2020)"*, which added the 2024 *Protoplasma* historiography exchange (Kingsland & Taiz, Trewavas, Minorsky).

That is **six new citations and three new quotations, none of which any deep review had ever verified.** The 08-01 note's cite count (12) is itself the tell: the article now carries 19. A ledger's coverage is bounded by the article as it stood, and a refine-draft pass does not inherit it.

## Citation ledger — §2.4 publisher-of-record web-verify

Verified at Crossref REST and Europe PMC REST (independent records, full field print — no truncated reads). The six post-08-01 cites are the focus; the pre-existing ones were spot-checked.

- Calvo, Baluška & Trewavas 2021 (*Integrated information as a possible basis for plant consciousness*) — **real-correct**. BBRC 564, 158–165, DOI 10.1016/j.bbrc.2020.10.022. Authors and pages match exactly.
- Mallatt, Taiz, Draguhn, Blatt & Robinson 2021 (*Integrated information theory does not make plant consciousness more convincing*) — **real-correct**. BBRC 564, 166–169. All five author surnames and both page numbers match.
- Segundo-Ortin & Calvo (*Consciousness and cognition in plants*) — **real-wrong-metadata** (year was 2021, corrected to 2022). WIREs Cog Sci 13(2), e1578. The article paired a 2021 year with the 13(2) volume/issue, which is the **March 2022** print issue. Europe PMC `pubYear=2022`, `printPublicationDate=2022-03-01`, `firstPublicationDate=2021-09-23`. Corrected in both the body ("Segundo-Ortin and Calvo (2022)") and reference 15, with the online-first date retained parenthetically.
- Kingsland & Taiz (*Plant "intelligence" and the misuse of historical sources as evidence*) — **real-wrong-metadata** (year 2024 → 2025; issue number added). *Protoplasma* 262(2), 223–246. Europe PMC `pubYear=2025`, print 2025-03-01, online 2024-09-14. Same year/volume mismatch: volume 262 is the 2025 volume.
- Trewavas (*Plant intelligence dux*) — **real-wrong-metadata** (year 2024 → 2025; issue added). *Protoplasma* 262(2), 255–266. Pages were already correct.
- Minorsky (*Matthew 7:3 — a response to Kingsland and Taiz (2024)*) — **real-wrong-metadata** (year 2024 → 2025; issue added). *Protoplasma* 262(2), 267–275. Pages already correct. The "(2024)" inside the **title** is part of the title and was left verbatim.
- Suda et al. 2020 (*Calcium dynamics during trap closure visualized in transgenic Venus flytrap*) — **newly added**, verified real-correct. *Nature Plants* 6(10), 1219–1224, DOI 10.1038/s41477-020-00773-1, PMID 33020606. See critical issue 4.
- Böhm et al. 2016 — **real-correct**, and see the false-positive note below.
- Toyota et al. 2018 — **real-correct**. *Science* 361(6407), 1112–1115, DOI 10.1126/science.aat7744. First two authors Toyota, M. and Spencer, D. confirmed in order.
- Biegler 2018 — **real-correct**. *Oecologia* 186(1), 33–35, DOI 10.1007/s00442-017-4012-3. Title verbatim including the "Response to Gagliano et al. (2014)" tail.
- Gagliano et al. 2014 — **real-correct**. *Oecologia* 175(1), 63–72, four authors in the order given.

**Superlative/currency sweep** (§2.4 step 4): `find_superlative_claims` returns **0**. No empirical-record superlatives to re-scope.

**Body↔References cross-check** (the lens that produced both 08-01 defects): run again, per-surname, with literal counts in both directions. All 16 cited surnames present in both body and reference list; no orphans in either direction. The only reference-side-only entries are the two Map self-cites (`Oquatre-*`), which are legitimate and were correctly left alone — cf. the standing `fabricated-map-self-cite-pseudonym-false-alarm` note. Reference numbering re-verified sequential 1–20 after insertion; the body cites by author-year only, so the renumber breaks no cross-reference.

## Critical Issues Found

### 1. Attribution error — a ground Trewavas applies elsewhere was attached to the fake-quotations rebuttal (FIXED)

The body read: *"Trewavas replied in the same volume that the charge of 'fake quotations' rests on faulty reasoning and **unfamiliarity with the literature**."*

Trewavas's abstract (PMID 39505772) says: *"Their claim of fake quotations is shown to result from faulty reasoning and **lack of understanding of practical biology**."* The "unaware of the extensive literature" charge is a **separate** complaint in the same abstract, levelled at Kingsland and Taiz's general position rather than at the fake-quotations argument. The article had merged two distinct charges and substituted the ground for one with the ground for the other — the dropped/substituted-qualifier failure mode §2.5 calls critical.

Fixed by quoting Trewavas directly: *"their 'claim of fake quotations is shown to result from faulty reasoning and lack of understanding of practical biology'"*. Verbatim-verified against the Europe PMC abstract.

### 2. Misstated enumeration — Lamarck dropped from Kingsland & Taiz's list of historical sources (FIXED)

The body listed the misused historical sources as *"Darwin, Sachs, Went, Thimann, McClintock and Bose."*

Kingsland & Taiz's abstract (PMID 39276228) gives: *"writings by Charles Darwin, Julius von Sachs, F. W. Went, K. V. Thimann, Barbara McClintock, and **J. B. Lamarck**."* **Lamarck was omitted**, and **Bose was wrongly folded into the same list** — the paper treats Bose separately and differently, as the claimed forerunner of plant neurobiology whose suppression the programme attributes to racism. The article presented a closed six-name enumeration that misreported which six.

Fixed: Lamarck restored, "Sachs" made "von Sachs", Bose moved into its own clause as "the forerunner the programme claims."

### 3. Mischaracterisation — Minorsky's reply is not "in defence of Bose" (FIXED)

The body read: *"and Minorsky replied separately **in defence of Bose**."*

Minorsky's abstract (PMID 39560739) shows the paper is a defence of **his own prior article** and specifically of **his charge of racism against Daniel T. MacDougal**, Bose's adversary: *"The charge of racism that I have levelled at Bose's most powerful and well-connected botanical adversary in the 1920s, Daniel T. MacDougal, is irrefutable."* Kingsland & Taiz had argued the contrary — that *"there were legitimate scientific reasons for questioning his interpretations."*

"In defence of Bose" is not false but it is thin to the point of misdirection: it loses the actual matter in dispute and implies Minorsky is defending plant intelligence, which he is not. Fixed with a precise characterisation that also marks what he is *not* defending.

### 4. Unsupported claim — the decaying-calcium counting mechanism is not Böhm's result (FIXED)

The body asserted, inside a paragraph whose only citation is Böhm et al. 2016: *"The counting rests on a decaying cytosolic calcium signal. If the second touch comes too late, the trace from the first has faded and the count resets."*

**Böhm et al. 2016 does not report this.** Its full text (PMC4751343, retrieved and grepped) covers AP counts, jasmonate signalling, hydrolase expression and DmHKT1-mediated sodium uptake. Cytosolic calcium appears once, as a citation to prior work: *"gland cells that receive a series of at least three APs increase their cytoplasmic calcium level [5]."* The decay-and-reset mechanism the article describes is the result of **Suda et al. 2020**: *"Because [Ca2+]cyt gradually decreased after the first stimulus, the [Ca2+]cyt increase induced by the second stimulus was insufficient to meet the putative threshold for movement after about 30 s."*

A real, correct, load-bearing claim was sitting uncited under a citation that does not support it — the `quote-fails-against-listed-refs-may-mean-missing-reference` pattern, where the defect is the *missing reference*, not the claim. Fixed by stating the mechanism in Suda's own terms with the threshold and the ~30 s window, and adding reference 10.

## False positive caught before it was published

**The "around five or more" AP figure is CORRECT. Do not "fix" it.** Böhm's *abstract* says *"more than three APs are required to trigger an expression of genes encoding prey-degrading hydrolases"*, which reads as a direct contradiction of the article's "around five or more." Working from the abstract alone I would have filed a critical factual error.

The full text says otherwise, twice: *"with five APs necessary for significant gene expression"* and *"to achieve a significant differential expression of the hydrolases and nutrient and sodium transporters, **about five APs were required**."* The abstract's "more than three" and the body's "about five" describe the same dose-response curve at different thresholds of stringency, and the article tracks the body. Verified by retrieving the Europe PMC full-text XML and grepping with printed character offsets rather than reading a truncated extract.

Recording this explicitly because the failure it nearly caused is the expensive one: an abstract-only check would have manufactured a defect in a correct sentence and "corrected" the article into error.

## Reasoning-Mode Classification (§2.6)

- **Taiz et al. 2019 — Mixed (Mode Two → Mode Three), unchanged.** The 08-01 upgrade stands and was not re-litigated. The in-framework objection (Feinberg & Mallatt's method establishes commonality, not necessity; neural necessity is not entailed by physicalism) still precedes the honest boundary declaration.
- **Mallatt et al. 2021 — Mode Three, sharpened.** This engagement arrived with commit `be02ae525f` and had never been classified. It was honest boundary-marking already, but it **over-conceded**: it called the IIT-internal objection *"a live countermodel the Map has not answered."* It is not a countermodel to the Map at all. Mallatt et al. argue that IIT fails to establish plant consciousness — a conclusion the Map **shares**. The Map holds plant consciousness at very low credence and does not use the IIT route, so it owes no answer here. Rewritten to say what is actually true and is genuinely less comfortable for the Map: the skeptics' bottom line does not depend on neural necessity, so declining that premise costs their conclusion less than the two preceding objections suggest. Tells from `over-concession-gets-ratified-not-merely-missed` (*"cannot ever"*, *"in principle"*, *"has not answered"*) apply here.
- **Calvo et al. 2021 — exposition, not reply.** Claim-to-source checked: the article's *"proposed a route to plant consciousness that is explicitly non-neural, grounding it in integrated information theory"* is faithful to the abstract (*"using a bottom up evolutionary approach and a leading theory of consciousness, Integrated Information Theory, we... find evidence that indicates that plant meristems act in a conscious fashion"*). The article omits the meristem specificity; not a defect, noted for future condensing.
- **"the same skeptic bloc"** — checked, fair. Four of Mallatt et al.'s five authors (Taiz, Draguhn, Blatt, Robinson) are Taiz et al. 2019 co-authors.
- **Label leakage** — grepped the full forbidden set (`direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `mixed-with-distinct-roles`, `tenet-register`, `Engagement classification`, `Evidential status:`, `direct-refutation-discipline`): **all zero**. Clean.

## Optimistic Analysis Summary

### Strengths preserved
- The split verdict — siding with the deflationists' conclusion while rejecting their reason — remains the article's best move and is untouched in substance. Critical issue 3 and the Mode Three sharpening both make it *more* honest rather than stronger.
- "Everyone broadly agrees on the behaviour, and disagrees about which words it earns" as the frame for the terminology war.
- The missing-rung argument: plants as multicellular-and-non-neural, behaviourally richer than *Physarum* yet no more plausible as experiencers. The Hardline Empiricist persona has nothing to object to here — the article declines the tenet-as-evidence-upgrade move throughout.
- The Gagliano/Markel replication failure as a worked calibration example, with the correct verdict ("unreplicated and widely doubted") rather than either inflation or dismissal.

### Enhancement made
- The flytrap counting mechanism is now mechanistically specific (threshold, decay, ~30 s window) instead of gestural, and correctly sourced. This is the Quantum Mind Theorist's and Phenomenologist's best passage and it now carries its own evidence.

### Cross-links
No new wikilinks added. The article already links eight internal targets and sits 23 words below the soft threshold; `hub-articles-accrete-crosslink-length` applies. No orphan risk — inbound links exist from the apex synthesis and the marginal-organism ladder.

## Calibration check

No possibility/probability slippage. Plant consciousness is held at "very low credence" on evidential grounds throughout, and nowhere upgraded on tenet-load. The Tenet-5 both-directions guard (parsimony licenses neither dismissal nor attribution) is intact at the close. Applying the §2 diagnostic test — *would a reviewer who fully accepts the Map's tenets still flag any claim as overstated?* — the answer is no. The one over-confidence found this pass ran in the **opposite** direction: the article conceded more to the skeptics than the source warranted (Mode Three item above), which is the mirror of the usual failure and was corrected as such.

## Remaining Items

None blocking. One note for a future pass: the article is 23 words below its 3000-word soft threshold, so the next deep-review or refine-draft on it operates in **length-neutral mode** — every addition needs a matching cut. The Calvo et al. meristem detail is the cheapest available trim target if room is needed.

No follow-up task minted.

## Stability Notes

- **The four corrected citation years are version-of-record and must not drift back.** Segundo-Ortin & Calvo is **2022**, 13(2), e1578 (online 2021). The three *Protoplasma* papers are **2025**, 262(2) (online 2024). Note the trap: Trewavas's and Minorsky's own texts cite Kingsland & Taiz as "(2024)" — Minorsky's *title* contains it — because they were written against the online-first version. Those in-title and in-quote "2024"s are correct as quoted material and must not be swept.
- **`Böhm et al. 2016` supports "about five APs" — verified in the full text. The abstract's "more than three APs" is not a contradiction and is not grounds for a correction.** Any future pass that flags this sentence from the abstract alone is repeating a false positive that was caught and documented here.
- **The decaying-calcium claim belongs to Suda et al. 2020 (reference 10), not Böhm.** Do not consolidate the two cites.
- **The Taiz/Map disagreement remains bedrock at its core** — neural necessity is declined under Tenet 1. Do NOT re-flag. Unchanged from 08-01.
- **The Mallatt et al. 2021 IIT objection is not a countermodel the Map must answer.** Its conclusion aligns with the Map's. A future review that re-flags this as an unanswered objection is re-installing the over-concession removed this pass.
- **Scope of this ledger, stated so the next pass can trust it precisely.** Lenses actually run: publisher-of-record metadata on all 19 cites (Crossref + Europe PMC, both queried); verbatim quote fidelity on the three Mallatt quotes and the Trewavas quote; full-text retrieval and grep for Böhm; abstract-level claim-to-source for Calvo et al., Kingsland & Taiz, Trewavas, Minorsky, Suda; body↔references bidirectional cross-check; superlative sweep; §2.6 classification and label-leakage grep; calibration. Lenses **not** run: full-text (as opposed to abstract) claim-to-source for the *Protoplasma* trio and the two BBRC papers — the abstracts were decisive for every claim the article makes from them, but a future pass wanting the historiography detail should fetch the Trewavas and Minorsky full texts, both of which are open access in Europe PMC.