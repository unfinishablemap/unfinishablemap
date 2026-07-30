---
ai_contribution: 100
ai_generated_date: 2026-07-30
ai_modified: 2026-07-30 07:38:23+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-30
date: &id001 2026-07-30
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Death and Consciousness
topics: []
---

**Date**: 2026-07-30
**Article**: [Death and Consciousness](/topics/death-and-consciousness/)
**Previous review**: [2026-07-08](/reviews/deep-review-2026-07-08-death-and-consciousness/)

## Context

Ninth deep review. Commissioned specifically to run the three **orthogonal citation lenses** —
claim-match, quote fidelity, and citation framing — on the grounds that the eight prior passes had
converged the *internal-consistency* lens without testing whether the sources say what the article
claims.

**A premise correction first.** The commissioning brief asserted that zero prior reviews contained a
web-verify section, based on a `grep` for heading patterns like `web.verif` / `verification notes`.
That grep was too narrow. The 2026-06-05 review (seventh) ran a genuine publisher-of-record metadata
audit under the heading *"Citations Verified Accurate"*, and the 2026-07-08 review (eighth) ran a
currency sweep under *"Citation Currency Sweep"*. This is the
*narrow-grep-zero-is-not-proof-of-absence* failure mode: the grep searched for the words the *fix*
would use, not the words the *files* actually used.

The brief's underlying judgement was nonetheless correct, for a different reason. The 06-05 ledger
covers **11 of 18** references (Van Lommel, Nahm et al., Mashour, Reimers, Hagan, McKemmish, Tegmark,
Parnia 2014, Parnia 2023, Osis & Haraldsson, Xu). The 07-08 review then asserted that the *remaining*
entries — naming Kerr 2014, Batthyány 2023, Callanan & Kelley 1992, Moody 2010, Fenwick 2008 — "were
exhaustively metadata-verified at the publisher of record on 2026-06-05." **They were not**; they
appear nowhere in the 06-05 ledger. That false ratification is precisely what shielded the largest
defect found this pass. Recorded here as a mechanism note: a review must not certify coverage it did
not itself perform, because the next review will trust the certificate instead of the publisher.

Lenses actually run this pass: **quote fidelity**, **claim-match**, **citation framing**, plus
bidirectional inline↔References orphan checking. Metadata was re-verified for the seven entries the
06-05 ledger never reached.

## Word Count

| | Before | After | Δ |
|---|---|---|---|
| Authored prose | 2781 | 2948 | +167 |
| Reference apparatus (Further Reading + References) | 474 | 502 | +28 |
| `analyze_length` total | 3255 | 3450 | +195 |

`analyze_length` reports `soft_warning` both before and after, but this is the known
*analyze_length-counts-reference-apparatus* measurement artifact: **authored prose is 2948, under the
3000 topics soft threshold**, and total is well under the 4000 hard cap. The net growth is corrective —
converting three overclaims into calibrated claims costs words — and was partly offset by trimming a
redundant summary sentence.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

1. **Fabricated verbatim quotation attributed to Parfit (CRITICAL — quote fidelity, fixed).** The
   Parfit section rendered his view on death as a direct quote: *"no more distressing than when I am
   about to lose consciousness in sleep."* This is **not a line in *Reasons and Persons***. Parfit's
   actual sleep-adjacent passages are the teletransporter case ("When I press the button, I shall
   lose consciousness, and then wake up at what seems a moment later") and the retrograde-amnesia
   sleeping-pill case; his death passages are the glass-tunnel passage (§115) and "my death seems to
   me less bad." No source carries the quoted sentence.

   **This defect was already diagnosed and fixed elsewhere in the corpus two months ago — and never
   propagated here.** The 2026-05-26 deep review of
   [parfit-reductionism](/concepts/parfit-reductionism/) identified it as a "Fabricated direct quotation," de-quoted it, and
   reframed it as paraphrase. `death-and-consciousness.md` kept the quotation marks, and it was
   **live at unfinishablemap.org** in `hugo/content/topics/death-and-consciousness.md`. Two
   subsequent deep reviews of this article (06-05, 07-08) missed it because both were scoped to
   citation *metadata* and *currency*, and neither lens reads quotation marks.
   **Fixed**: de-quoted and reframed as paraphrase, adopting the sibling's canonical wording.

   *Verification hazard encountered and avoided*: the first WebSearch for this quote returned
   `unfinishablemap.org/concepts/parfit-reductionism/` as its **top hit**, and the search assistant
   reported "I found the quote you're searching for!" — a textbook
   *quote-verify self-contamination via the Map's own page* false confirmation. Re-running with the Map's
   domains blocked returned no source anywhere.

2. **Batthyány et al. 2023 is a wrong-author misattribution (CRITICAL — fixed, and propagated).**
   Reference 1 read *"Batthyány, A. et al. (2023). Reports about paradoxical lucidity from health
   care professionals: A pilot study. Journal of Gerontological Nursing, 49(1), 17-22."* Verified
   against **publisher-deposited Crossref metadata for DOI 10.3928/00989134-20221206-03**: the paper
   is real, the title is exact, but the authors are **Teresi, J.A., Ramirez, M., Ellis, J., Tan, A.,
   Capezuti, E., Silver, S., Boratgis, G., Eimicke, J.P., Gonzalez-Lopez, P., Devanand, D.P., &
   Luchsinger, J.A.** — **Batthyány is not an author at all** — and the pages are **18-26**, not
   17-22.

   Root cause is a plausible conflation: Alexander Batthyány *does* have real 2023 terminal-lucidity
   work, the book-length *Threshold*, cited correctly and legitimately in
   [terminal-lucidity-and-filter-transmission-theory](/topics/terminal-lucidity-and-filter-transmission-theory/) and in the 2026-03-20 research note. Those
   loci are correct and were **deliberately left untouched.** The journal pilot study is a different
   paper by a different team.

   This is a `real-wrong-metadata` state, so the cite was **corrected, not deleted**
   (the *citation-verify false-negative* discipline). **Family resolution performed** per §2.4 step 6:
   grepped the corpus and found the identical wrong attribution at **four further loci in two more
   files**: [near-death-experiences](/concepts/near-death-experiences/) (body claim + its own reference entry, same wrong page range),
   and the archived-but-still-served `archive/topics/death-phenomenology-beyond-ndes.md` (body claim +
   reference entry) — the article this one was coalesced from, which is why the defect was inherited
   in the first place. All corrected to Teresi et al. and re-synced, so no tree still serves the wrong
   authorship. The 73% figure itself is accurate to the source (33 interviews, 73% reported ever
   witnessing paradoxical lucidity).

   Every *other* Batthyány citation in the corpus was checked and is **legitimate — left untouched**:
   Batthyány & Greyson's real "Spontaneous remission of dementia before death" paper (*Psychology of
   Consciousness*), Batthyány's *Threshold* (2023) book, and Mashour, Frank, Batthyány et al. 2019,
   where he genuinely is a co-author.

   **Prior false ratification**: the 2026-W22 changelog records *"Batthyány 2023 JGerontolNurs
   49(1):17-22 (73%) CLEAN"* — a wrong cite certified as web-verified. Intra-corpus ratification
   again, not caught until publisher-level metadata was pulled.

3. **Orphan reference: Hagan et al. 2002 (CRITICAL — bidirectional check, fixed).** The entry sat in
   References with no inline citation anywhere in the body; the decoherence passage attributed the
   recalculation to "Hameroff's group" without naming the cite. **Fixed**: anchored inline as
   `(Hagan et al., 2002)`. Reference entry also completed with the full subtitle and locator
   (*Phys Rev E* 65, 061901), both documented at publisher level in the 06-05 ledger.

### Medium Issues Found (all fixed)

4. **Kerr et al. 2014 mis-framed — double-edged result asserted as one-sided support (citation
   framing, fixed).** Kerr was cited to support deathbed visions occurring in patients "who remain
   conscious and lucid" seeing figures "alongside the physical room… with coherent interaction and
   calm rather than distress." Verified against the publisher abstract (*J Palliat Med* 17(3),
   296-303 — metadata exactly correct): **almost half of the episodes occurred while asleep**; the
   most common content was deceased friends/relatives **and living friends/relatives**; and the
   comfort finding is **comparative** ("dreams/visions featuring the deceased were significantly
   more comforting than those of the living"), not an absolute absence of distress — a distressing
   minority is documented. Citing a study of *dreams and visions*, half of them during sleep, for a
   claim expressly restricted to lucid waking perception mis-frames the source, and the living-relative
   content cuts directly against the deceased-predominance argument the section is building.
   **Fixed by re-framing, not deletion**: the lucid-waking claim now rests on Fenwick & Fenwick, and
   Kerr is introduced as the most systematic evidence with its two-edged result stated plainly.

5. **Osis & Haraldsson cross-cultural convergence overstated (citation framing, fixed).** The article
   said "Despite vast cultural differences, both populations predominantly saw deceased rather than
   living persons," then concluded "This cross-cultural convergence resists hallucinatory explanation:
   if DBVs were projections of expectation, the content should vary with cultural context." But Osis
   and Haraldsson **themselves documented pronounced culture-specific variation** — Indian patients
   were far more likely than Americans to see a personification of death (the yamdoot figure) or a
   religious figure — and their survey drew criticism for a low response rate. The article cited a
   mixed result as though it found uniformity, and then built a falsifiability condition on the
   premise that O&H found little divergence. **Fixed**: reframed as a convergent core (dead over
   living) inside culturally shaped content, with the variation and the selection worry stated;
   falsifiability condition 5 rewritten to target the predominance rather than "more divergence than
   O&H found"; and the section-closing summary sentence trimmed to drop the now-qualified
   "deceased persons appear consistently across cultures" clause.

6. **Price's "dream-image" is not Price's phrase (quote fidelity, fixed).** The Dualist Possibilities
   section scare-quoted *Price's "dream-image" existence*. Price's terminology in "Survival and the
   Idea of 'Another World'" (1953, *Proc. SPR* 50) is an **image-world** of "real mental images," with
   dreaming used as an analogy. **Fixed** by removing the quotation marks and using his actual
   concept ("Price's image-world—a dream-like mental existence composed of images"), which preserves
   the substance and eliminates the fidelity risk without adding an unverified verbatim span.

7. **Uncited load-bearing statistic (fixed).** "Up to 25% of behaviorally unresponsive patients
   retain awareness detectable only via neuroimaging" carried no citation. Verified as **Bodien et
   al. 2024**, *NEJM* 391(7), 598-608 (Crossref): cognitive motor dissociation in **60 of 241**
   command-unresponsive participants = 25%, via task-based fMRI, EEG, or both. **Fixed**: figure
   re-worded to "Around 25%" (Bodien found exactly 25% and noted it may be an undercount), detection
   modality corrected to "task-based fMRI or EEG" (EEG is not neuroimaging), and the cite added
   inline with a new References entry.

8. **Nahm short-form citation (fixed).** Body read "Nahm and Greyson (2012)" for a four-author paper
   (Nahm, Greyson, Kelly & Haraldsson), which also risks confusion with the genuinely distinct
   Nahm & Greyson **2009** paper. **Fixed** to "Nahm et al. (2012)".

9. **Evidential-hedging asymmetry on Callanan & Kelley (calibration, fixed).** Nearing death
   awareness claims — patients "announce when they will die with remarkable precision" — were
   presented flatly as fact, while the shared-death section correctly flags its evidence as
   "anecdotal with no prospective verification." *Final Gifts* (1992) is a hospice-nursing case
   collection, weaker evidence than Kerr's prospective cohort, yet it received the least hedging in
   the article. A tenet-accepting reviewer would still flag this, so it is a calibration issue rather
   than a bedrock disagreement. **Fixed** with one sentence placing NDA's evidential standing
   explicitly closer to the SDE material than to Kerr's cohort data.

### Per-Cite Ledger (this pass)

Verification level: **publisher** = publisher-deposited Crossref metadata, publisher abstract page,
or arXiv canonical version. All previously-unledgered entries were checked at publisher level.

| Cite | Level | State |
|---|---|---|
| Teresi et al. 2023 (was "Batthyány et al. 2023") | publisher (Crossref DOI 10.3928/00989134-20221206-03) | **real-wrong-metadata** — wrong first author (Batthyány→Teresi), wrong pages (17-22→18-26); corrected inline + References, propagated to [near-death-experiences](/concepts/near-death-experiences/) |
| Kerr et al. 2014 | publisher (Crossref + SAGE/Liebert abstract, DOI 10.1089/jpm.2013.0371) | **real-correct metadata; mis-framed** — 17(3), 296-303 exact; framing corrected (asleep-vs-awake, living-relative content, comparative comfort) |
| Bodien et al. 2024 | publisher (Crossref DOI 10.1056/NEJMoa2400645) | **newly added** — *NEJM* 391(7), 598-608; supports the previously uncited 25% figure |
| Hagan et al. 2002 | publisher (arXiv canonical quant-ph/0005025) | **real-correct; claim-match confirmed** — Tegmark 10⁻¹³ s vs. recalculated 10⁻⁵–10⁻⁴ s = "eight to nine orders of magnitude longer" is arithmetically right (their actin-gelation figure of 10⁻²–10⁻¹ s is longer still, so the article is conservative). Was an **orphan**; anchored inline |
| Osis & Haraldsson 1977 | publisher-adjacent (Google Books record) + secondary literature on findings | **real-correct; mis-framed** — cross-cultural variation understated; reframed |
| Moody 2010 | publisher (Guideposts edition record) | **real-correct** — *Glimpses of Eternity*, Guideposts, 2010; SDE content claims (shared life review, room/light phenomena, shared out-of-body perception) match the source. Co-author Paul Perry omitted from the entry — noted, not changed |
| Callanan & Kelley 1992 | publisher (Poseidon Press, 1992) | **real-correct** — NDA claims (timing announcements, travel symbolism, two-realities reports) match *Final Gifts*; evidential hedging added |
| Fenwick & Fenwick 2008 | publisher (Continuum / Bloomsbury Continuum, 2008) | **real-correct** — now carries the lucid-waking DBV claim |
| Price 1953 | publisher (*Proc. SPR* 50, publication record) | **real-correct attribution; quote de-quoted** — "dream-image" is not his phrase; image-world is |
| van Inwagen (resurrection-by-recreation yields a duplicate) | publisher-adjacent (PhilPapers/IEP on the 1978 paper) | **real-correct claim-match** — argument accurately represented; left as a name-only attribution so no orphan inline cite is created |
| Parfit 1984 | primary text + multiple independent searches with Map domains blocked | **quote fabricated** — sentence exists in no source; de-quoted to paraphrase |
| Van Lommel 2001, Nahm et al. 2012, Mashour 2019, Reimers 2009, McKemmish 2009, Tegmark 2000, Parnia 2014, Parnia 2023, Xu 2023 | publisher, 2026-06-05 ledger; unchanged in body since | **real-correct** — not re-litigated (no metadata drift possible without an edit); 07-08 confirmed AWARE II numbers and Orch OR "dispute is live" as current |

### Empirical-Record Currency Sweep

`find_superlative_claims` returned **empty** — no lexical superlative claims in the article. Checked
by hand anyway, given the subject-matter hazard the brief flagged (death/NDE/terminal-lucidity
superlatives going stale): the article's strong-sounding phrases are all **comparative and internal**
("perhaps the most direct challenge," "the strongest challenge to brain-based explanations"), not
empirical priority claims about the literature. No "first," "only recorded case," or "unprecedented"
claims exist to go stale. Nothing superseded.

### Reasoning-Mode Classification (editor-internal)

Unchanged from 06-05/07-08: Everettian engagement **Mode Three** (framework-boundary marking, and the
article says so explicitly); Parfit **Mode Three / bedrock** (haecceity vs. reductionism) — the
paraphrase fix does not alter the mode, since the engagement never depended on the quotation;
Illusionists **Mode Two** (unsupported foundational move — illusion problem + selective reliability).
New this pass: engagement with the **hallucination/expectation hypothesis** about deathbed visions is
now honestly **Mode Three-leaning** rather than presented as defeated, which is what the Osis fix
accomplished.

### Label Leakage Check

Passed. No editor-vocabulary terms in article prose, including all nine edited passages.

## Optimistic Analysis Summary

### Strengths Preserved

- The five falsifiability conditions, the "What the Map Does Not Claim" anchor, and the
  Hardline-Empiricist restraint on SDEs survive intact — and are now *more* consistent, since the
  three overclaims fixed this pass were the places where that restraint had lapsed.
- The counterfactual-exclusion treatment of Many-Worlds (the article's best passage) is untouched.
- The front-loaded opening, the death-void framing, and the Buddhist *anattā* tension
  acknowledgement are all preserved unchanged.

### Enhancements Made

Nine corrections; no expansion. All are substitution- or calibration-shaped.

### Cross-links Added

None. No new wikilinks were introduced this pass, so no link-resolution risk was added.

## Remaining Items

- **Deferred item from 06-05 and 07-08 now CLOSED**: both reviews left open a spot-check of
  [near-death-experiences](/concepts/near-death-experiences/) for the same AWARE II "39% recalled experiences of death" mis-pin.
  Checked this pass: that article correctly pins 39% to "some form of conscious awareness during
  arrest" (the broad bucket) and explicitly hedges it as a self-selected sample of 28 of 567. **The
  mis-pin did not propagate.** No action needed.
- **New locus found, reported not fixed**: the Batthyány & Greyson "Spontaneous remission of dementia
  before death" paper is cited with **inconsistent years across the corpus** — 2020 in
  [filter-theory](/concepts/filter-theory/), [consciousness-under-extreme-metabolic-constraint](/topics/consciousness-under-extreme-metabolic-constraint/) and
  [memory-channel-interface-evidence](/topics/memory-channel-interface-evidence/), 2021 in
  [terminal-lucidity-and-filter-transmission-theory](/topics/terminal-lucidity-and-filter-transmission-theory/) (which also lists 8(1), 1-8, consistent with a
  2021 issue). This is a real family-resolution job — one canonical year, propagated — but it is a
  different citation from the one under review here and touching five unrelated articles mid-review
  would exceed this pass's scope. Worth a task.
- **Untouched loci, reported not fixed**: (a) Tegmark 2000's References entry lacks volume/pages —
  incompleteness, not error, and no publisher-level locator is documented in the corpus, so it was
  not guessed at; (b) Moody 2010's entry omits co-author Paul Perry; (c) the Osis & Haraldsson
  "over 1,000 doctors and nurses" figure was left as verified on 06-05, though secondary literature
  reports a ~6.4% response rate on ~10,000 questionnaires, which is hard to reconcile — the
  *selection* worry is now stated in the body, but the headcount would need the book itself to settle.

## Stability Notes

Ninth review. The bedrock disagreements — illusionism, decoherence/quantum-soul, Buddhist no-self,
the Many-Worlds framework boundary — remain stable and must **NOT** be re-flagged as critical.

**The lesson of this pass is about convergence accounting.** Eight prior reviews found this article
converged, and on the internal-consistency and citation-metadata lenses they were right. But
convergence is **per-lens, not per-article**, and two of the three lenses run here had never been
applied: a fabricated Parfit quotation sat in the body through eight reviews and had been fixed in a
sibling article two months earlier without propagating; a wrong-author misattribution survived
because one review *certified* coverage it had not performed and the next review trusted the
certificate. Both defects were invisible to metadata and currency checks by construction.

Two mechanism notes for future reviews of converged articles:

1. **Never certify coverage you did not perform.** The 07-08 review's claim that five specific
   entries "were exhaustively metadata-verified on 2026-06-05" was false and directly caused a
   critical defect to survive an extra cycle. If an entry is not in a ledger, say it is not in a
   ledger.
2. **A fix applied to one article is not a fix.** When a defect is corrected in one file, grep the
   corpus for the defect *string* before closing it. The Parfit quote and the Batthyány
   misattribution were both multi-file defect families fixed in one file only.