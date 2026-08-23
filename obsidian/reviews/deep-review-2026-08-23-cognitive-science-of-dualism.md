---
title: "Deep Review - Cognitive Science of Dualism (Post-Coalesce Merged-Unit Pass)"
created: 2026-08-23
modified: 2026-08-23
human_modified: null
ai_modified: 2026-08-23T00:15:20+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-23
last_curated: null
---

**Date**: 2026-08-23
**Article**: [[cognitive-science-of-dualism|Cognitive Science of Dualism]]
**Previous review**: [[deep-review-2026-07-17-cognitive-science-of-dualism|2026-07-17]] (pre-merge)
**Review type**: First review of the merged unit after the 2026-08-21 coalesce (`f653fb2295`) absorbed `concepts/intuitive-dualism` (1982w) into this article (2189w → 3629w).

## Verdict

**NOT a no-op. One CRITICAL empirical-fidelity defect found and fixed, and it was corpus-level: a fabricated participant count and a fabricated population list for Barrett et al. (2021) that had survived sixteen prior deep reviews across the two merged articles and had been positively ratified as "publisher-of-record verified" by three separate citation ledgers.**

The merge itself was clean — every repair the absorbed article's eight reviews had made was carried forward intact. The defect predates the merge and was inherited by it from both parents.

## PRIMARY LENS — did the merge carry the absorbed article's fixes forward?

Checked each repair from the three most recent `intuitive-dualism` reviews against the merged prose, using `archive/concepts/intuitive-dualism.md` (the post-fix text) as the diff baseline.

| Fix | Review | Status in merged text |
|---|---|---|
| Barrett quote: restore dropped word "tested" | 2026-07-12 | **LIVE** — merged prose reads "all cultures tested"; now paraphrase rather than quotation, so the non-source italic on "not" is moot |
| Richert & Harris 2008 — wrong venue/volume/pages (3 errors) corrected to *Journal of Cognition and Culture* 8(1-2):99-115 | 2026-06-24 | **LIVE** — References entry correct |
| Berent 2024 — misleading "et al." → "Berent, I., & Sansiveri, A."; *Open Mind* 8:84-101; inline mentions corrected | 2026-06-24 | **LIVE** — References and both inline/table mentions correct |
| Bering 2002 — restore full title | 2026-06-24 | **LIVE** |
| Chudek et al. 2018 — restore subtitle | 2026-06-24 | **LIVE** |
| Tallis inline↔References orphan | 2026-06-24 | **N/A, correctly** — the merge delegated the whole illusionism engagement to [[illusionism]] and dropped both the inline mention and the References entry together, so no orphan was created |

**One fix was regressed by the merge, and it is small:** Bloom's "natural-born dualists" was a verbatim-verified attributed phrase in *both* parents (verified at the 2026-07-12 pass as a genuine Bloom phrase and the title of his Edge.org essay). The merge converted it into an unquoted bold run-in head, so the article asserted the phrase in its own voice. **Restored to quotation with attribution to Bloom** (not pinned to *Descartes' Baby* specifically, since the exact string's home is the Edge essay).

**Content dropped by the merge that is NOT a lost fix** (checked, no action needed): the archived article's Frankish/Tallis illusionism passage, its Schwartz et al. 2005 OCD citation, and its `quantum-neural-timing-constraints` 280–300 ms material. The illusionism material is superseded by a fuller and better-calibrated treatment already live at [[illusionism]] (which carries the bare-regress-marks-a-boundary framing and the Tallis reply); the other two were section-local to the absorbed article's tenet block and the merged article's own tenet paragraphs cover the same ground. The ~542-word shortfall the driver brief flagged is accounted for by this legitimate deduplication.

**The inverse hazard (two halves disagreeing, one side wrong) did not materialise on the merge seam** — but it did materialise one level up, in the shared citation ledger. See below.

## CRITICAL — Barrett et al. (2021) sample fabricated (publisher-of-record verified)

**The article said:** "recruited over 2,000 participants across six populations (North Americans, Ecuadorians, Fijians, Ghanaians, Thai Buddhists, Vanuatu Islanders)".

**The paper says** (published PDF, *Cognitive Science* 45(6) e12992, §3.2 and Table 1 — retrieved as a raw artefact and grepped, not asked-about):

> "We administered our questionnaire to **260 participants** across six different study populations"

| Population | Country | N |
|---|---|---|
| Chicago evangelical Christian congregation | USA | 27 |
| Emory students | USA | 24 |
| Marajó Islanders | Brazil | 61 |
| Shuar | Ecuador | 35 |
| Storozhnitsa | Ukraine | 48 |
| Wesleyan students | USA | 65 |
| **Total** | | **260** |

So the participant count was overstated **~8×**, and **four of the six named populations do not appear in the paper at all**. Only "North Americans" (three of the six samples) and "Ecuadorians" (the Shuar) were right. The real sixth-population set is half US and includes Brazil and Ukraine — countries the article never mentioned.

**Fix applied**: the sentence now names the six populations correctly with N = 260, replaces the false impressiveness of "over 2,000" with a real and more telling datum (70% of the Chicago evangelical congregation — recruited for their membership, reporting universal explicit afterlife belief — gave no continued-existence responses at all, verified verbatim in the PDF), and adds a calibration paragraph registering the sample's actual limits in the authors' own words.

### Why this is a calibration error, not a bedrock disagreement

Applying the §2 diagnostic test: a reviewer who fully accepts the Map's tenets would still flag this. The inflated sample was doing evidential work *in the Map's favour* — Barrett's intuitive-materialism finding is what lets the article answer the "dualism is just folk error" dismissal, and "over 2,000 participants across six cultures" made that answer sound far better evidenced than 260 participants, half of them American undergraduates and churchgoers, can support. That is possibility/probability slippage in the over-confident direction, and correctable inside the Map's own framework.

The added paragraph therefore also re-scopes what the study licenses: the **negative** claim (afterlife judgements do not evidence *universal* intuitive dualism) rather than a positive demonstration that materialism is the human default. The lead paragraph's "the field has reversed itself" was softened to "the field has lost confidence in its original claim" for the same reason.

### How it survived sixteen reviews — the ledger ratification chain

This is a textbook `citation-ledger-ratifies-the-reading-not-just-the-metadata` case, compounded by `convergence-can-be-false-two-reviewers-wrong-one-right`. The metadata was always right (H. Clark Barrett; *Cognitive Science* 45(6) e12992; six populations), and every review checked the metadata. **Nobody checked the sample.** Worse, three ledgers positively asserted the fabricated list as verified:

1. `deep-review-2026-05-26-intuitive-dualism` — earliest ledger locus; states the fabricated identities and "~2,000 participants" as "VERIFIED correct".
2. `deep-review-2026-06-02-the-convergence-argument-for-dualism` — repeats the list as "VERIFIED CLEAN".
3. `deep-review-2026-06-20-cognitive-science-of-dualism` — the strongest ratification: asserts that **Wiley, PubMed, the gwern PDF, ORA Oxford and PhilPapers "all confirm"** the list. None of those sources says it; the gwern PDF it names contains Table 1, which refutes it.

Then `deep-review-2026-07-17` skipped web-verify by design on the strength of that ledger, and the coalesce carried the text forward. Three "independent confirmations" of the same fabrication looked like corroboration. Note the count "six" was itself the subject of an earlier six→eight→six flip-flop (`barrett-2021-eight-vs-six-propagated`); that episode drew all subsequent scrutiny onto the number, and the identities travelled underneath it unexamined.

**All four stale ledgers annotated inline** (the documented remedy) so the step-1.5 "read prior reviews" rule cannot re-seed the fabrication.

### Corpus propagation sweep

Swept `obsidian/` live sections, `archive/`, and `hugo/content/` for `over 2,000 participants`, `Ghanaians`, `Thai Buddhists`, `Vanuatu Islanders`:

- **One live article carried it** — this one.
- **One archived article carried it** — `archive/concepts/intuitive-dualism.md`. Archived pages serve full bodies at preserved URLs and are read by chatbots (`noindex-does-not-suppress-the-machine-metadata-surface`), so the fabricated sentence was live. **Corrected surgically** — one sentence, nothing else touched.
- Other live articles citing Barrett (`epistemology-of-convergence-arguments`, `the-convergence-argument-for-dualism`, `cross-cultural-convergence-on-mental-causation`, research note `cognitive-science-dualism-2026-01-15`) say only "six populations" with no N and no identities — **all correct, no change needed**.
- Post-fix sweep of both trees returns **zero hits** outside immutable review/changelog history.

## Citation Web-Verify Ledger (§2.4)

Barrett was verified at the publisher of record this pass; the rest of the References block is unchanged since the 2026-06-20 metadata ledger, which stands on metadata.

- **Barrett, H. C., et al. 2021** (*Cognitive Science* 45(6) e12992) — **real-wrong-empirical-claim**. Metadata real-correct (verified: authors Barrett, Bolyanatz, Broesch, Cohen, Froerer, Kanovsky, Schug, Laurence; DOI 10.1111/cogs.12992; six study populations). Sample size and population identities corrected as above.
- **Barrett 2021 quoted span 1** — "a possible mode of thought enabled by evolved human psychology" — **VERIFIED verbatim**, grepped against the raw abstract retrieved from the publisher record (EuropePMC core record for DOI 10.1111/cogs.12992) and confirmed again in the PDF. This span had never been verbatim-checked by any prior review of either article.
- **Barrett 2021 quoted span 2** — "does not constitute a default mode of thought" — **VERIFIED verbatim**, same method. Also never previously checked. The article's stitch (eliding "such thinking" outside the quotation marks) is faithful.
- **Barrett 2021 quoted span 3 (new this pass)** — "is in no way intended to capture the full range of human societies and afterlife beliefs" — **VERIFIED verbatim** in the abstract and body.
- **Bloom, "natural-born dualists"** — real-correct, re-quoted (see above); verbatim status inherited from the 2026-07-12 pass.
- Richert & Harris 2008, Berent & Sansiveri 2024, Bering 2002/2006, Chudek et al. 2018, Barlev & Shtulman 2021, Clark 2013, Hohwy 2013, McGinn 1989, Chalmers 1995, Fox et al. 2012, Whitehead 1929, Willard & Norenzayan 2013 — **real-correct**, unchanged since the 2026-06-20 / 2026-06-24 ledgers.
- **Inline ↔ References cross-check**: complete in both directions. No orphans. (Friston is named inline without a year and has no References entry — pre-existing, accepted at the 2026-06-20 pass, not a new defect.)
- **Empirical-record currency sweep**: `find_superlative_claims` returns 0. No superlative claims.

## Other Pessimistic Findings

### Medium — fixed
- "Early cross-cultural work supported him" headed a paragraph covering Chudek et al. (cross-cultural) *and* Richert & Harris (developmental, not cross-cultural). Reworded to "Early developmental and cross-cultural work".

### Reasoning-Mode Classification (editor-internal)
- Genetic-fallacy materialist — **Mode One**: the inference from "we can explain the belief" to "the belief is false" is invalid by the materialist's own logical standards, and the article shows it cuts symmetrically against intuitive materialism.
- Behavioural-output physicalist ("reports are just motor responses") — **Mode Two**: the objection is turned using the physicalist's own commitment to the study's explanatory value, followed by an honest underdetermination concession.
- Vitalism-parallel materialist — **Mode One**: the dis-analogy is drawn inside the materialist's own framing (life-functions are functions; experience is not).
- Illusionist — **Mode Three**, delegated: the article declines to adjudicate and points to [[illusionism]], retaining only the one empirical point (Fox et al. 2012) that belongs to this article's subject matter. Honest.
- **No label leakage.** Grepped for all forbidden editor-vocabulary strings: zero hits.

### Style
- No "This is not X. It is Y." construct (grepped). No "load-bearing" intensifier. Named-anchor forward references resolve (`#intuitive-mind-body-reasoning-is-variable`, `#the-genetic-fallacy-in-both-directions`).

## Optimistic Analysis Summary

### Strengths preserved
- Methodological-circularity argument (neural-correlate studies depend on first-person report as irreducible data) — untouched.
- The thermometer/radio-waves and thermometer/pressure analogies — untouched.
- The vitalism dis-analogy ("nothing it is like to metabolise; something it is like to see red") — untouched.
- The 2026-06-09 underdetermination concession — untouched.
- The genetic-fallacy-cuts-both-ways symmetry — untouched, and now rests on an accurately described study.
- The merge's own good work: the four-condition "What Would Challenge This View?" section and the declined haecceity inference in the No-Many-Worlds paragraph are both strong, and both are new since the last review of this file.

### Enhancement made
- The Chicago-congregation datum (70% of explicit afterlife believers giving no continued-existence responses) is a stronger and more surprising piece of evidence than the fabricated headcount it replaces, and it is the paper's own "most surprising" finding.

### Cross-links
- None added. Link set is dense and correct post-merge.

## Length

3629 → **3753 words** (+124). `topics/` thresholds 3000 soft / 4000 hard / 6000 critical — status `soft_warning`, **247 words of headroom to hard**.

Length-neutral mode was in force and I did not fully achieve neutrality. Both additions were defect-mandated: an accurate six-population list is unavoidably longer than the fabricated summary it replaces (+~50), and the calibration paragraph the corrected sample requires is ~75 words. Offsetting trims: dropped a generic neural-anatomy sentence in §Neural Correlates (~11 words, content LLMs already have per the style guide) and tightened the new caveat (~11). Naming what I declined to cut rather than cutting it silently: the Whitehead paragraph and the §Hard Problem / §What Would Challenge overlap are both trim candidates, but both are merge-preserved content, and trimming merged material in the very pass whose purpose is to check the merge for losses would be the wrong instinct. The article remains comfortably inside the hard threshold; a future `condense` pass can take those two if headroom tightens.

## Frontmatter

- `last_deep_review` was **empty** — the only such value in `topics/`, `concepts/`, `apex/` or `voids/`. The coalesce cleared it (it read `2026-07-17T18:37:59+00:00` before commit `f653fb2295`), presumably to mark the merged unit unreviewed. Now set to `2026-08-23T00:15:20+00:00`, `date -u`-checked and strictly past.
- `ai_modified` bumped to the same timestamp — a real fix was applied, not a no-op.
- `ai_system` left at `claude-opus-4-7+claude-opus-5`; this pass ran on claude-opus-5, already present in the string.

**Scoring note worth acting on**: an empty `last_deep_review` yields `days_since_review: -1` and a score of 29.7, ranking this article **32nd of 345** — *below* articles reviewed 28 days ago. An article that has never been reviewed as a merged unit therefore sorts beneath ordinary staleness. Clearing the field to signal "unreviewed" achieves the opposite of what it intends: `get_review_candidates` treats unknown as *fresher* than known-stale. The never-reviewed branch (base score 100) is keyed on the absence of a review *file*, not on an empty field, so a coalesced article with prior review files can never reach it. This defect was found only by inspecting coalesce commits, not by scoring.

## Remaining Items

- **The memory note `barrett-2021-eight-vs-six-propagated` carries the same fabricated population list** in its "Lessons" section ("US (Indiana), India (Karnataka), Vanuatu, Thailand, Peru (Shuar), Russia (Moscow)" — a *third* variant, also wrong, though it hedges that "secondary sources sometimes list a slightly different six-society set"). It should be corrected to the Table 1 list, since it is exactly the artefact a future reviewer consults when Barrett's populations come up. Flagged to the operator; not edited from this pass.
- Standing optional expansions from prior reviews (Iris Berent debunking work, eliminativist response, Libet/Chalmers meta-problem) remain optional, not defects — and there is now less length headroom for them.

## Stability Notes

Future reviews should NOT re-flag:

- **Barrett et al. (2021) = 260 participants across six study populations: Chicago evangelical Christian congregation (USA, 27), Emory students (USA, 24), Marajó Islanders (Brazil, 61), Shuar (Ecuador, 35), Storozhnitsa (Ukraine, 48), Wesleyan students (USA, 65).** Verified 2026-08-23 against §3.2 and Table 1 of the published PDF. If a future reviewer reads the 2026-05-26, 2026-06-02 or 2026-06-20 ledgers and sees "Fijians, Ghanaians, Thai Buddhists, Vanuatu Islanders" or "~2,000 participants", **those figures are fabricated** — each is annotated inline at source.
- Both Barrett quoted spans are verbatim-faithful as of 2026-08-23; do not re-alter them.
- The calibration paragraph limiting Barrett to the negative claim is a deliberate overclaim-reducing move. Do **not** revert it toward a stronger reading of the study, and do not restore "the field has reversed itself" in the lead.
- Bloom's "natural-born dualists" is a genuine attributed phrase and belongs in quotation marks; do not de-quote it again.
- All merge-preserved citation fixes from the absorbed article's 2026-06-24 pass are live and verified; no need to re-check them.

Bedrock disagreements (not fixable; do NOT flag as critical):

- Eliminative materialists deny the explanatory gap is a real explanandum — framework boundary.
- Functionalists hold future neuroscience closes the gap (the vitalism parallel) — the article's dis-analogy is its answer; the standoff stands at the boundary.
- A hardline empiricist may hold that even the corrected Barrett study is too small to support the negative claim the article now restricts it to. The article's own caveat paragraph concedes the sample's limits explicitly; further hedging would be over-concession.
