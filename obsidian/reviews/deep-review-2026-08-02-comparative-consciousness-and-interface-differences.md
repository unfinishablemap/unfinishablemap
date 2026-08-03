---
title: "Deep Review - Comparative Consciousness and Interface Differences"
created: 2026-08-02
modified: 2026-08-02
human_modified: null
ai_modified: 2026-08-02T10:16:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-02
last_curated: null
---

**Date**: 2026-08-02
**Article**: [[comparative-consciousness-and-interface-differences|Comparative Consciousness and Interface Differences]]
**Previous review**: [[deep-review-2026-06-24-comparative-consciousness-and-interface-differences|2026-06-24]]

## Verdict: Two citation defects fixed — first full publisher-of-record ledger for this article

This is the article's **eighth** deep review. The previous two passes (2026-06-02, 2026-06-24) both declared convergence and declined the §2.4 web-verify on "trigger condition not met" grounds, verifying only the single citation each pass's diff had touched. **A full publisher-of-record ledger had never been produced for this article's eleven references.** Running one this pass surfaced two real defects, both of which had already been diagnosed and corrected in *sibling* articles months ago while the copies here stayed live.

This is the `fix-by-file-leaves-string-siblings-live` pattern: a defect family gets resolved at the loci one review happened to look at, and the surviving siblings inherit an unearned presumption of correctness from the review record.

## Changed-Since Classification

The diff against the 2026-06-24 review commit (`0f106fb07`) shows exactly one non-frontmatter change, from `41d89c35e` (quote-fidelity sweep on the Map's own Tenet 2):

```
- the "smallest possible non-physical influence on quantum outcomes."
+ the "smallest possible non-physical influence on physical outcomes,"
+   which the tenet's definition locates at the quantum level.
```

**Verified**: `obsidian/tenets/tenets.md:62` reads "The smallest possible non-physical influence on physical outcomes." The corrected article text is now a contiguous verbatim substring; the "at the quantum level" gloss is carried outside the quotation marks where it belongs. The sweep's fix was correct.

Because the body was modified, the §2.4 trigger **was** met this pass — and unlike the last two passes, the ledger below covers every reference, not just the touched one.

## Citation Web-Verification Ledger (all 11 references)

WebSearch budget was exhausted this session; verification ran through Crossref and OpenAlex against publisher-of-record metadata (per ``webfetch-survives-websearch-exhaustion``).

- **Birch, J. (2024)** *The Edge of Sentience* (OUP) — **real-correct**.
- **Carhart-Harris, R. L. & Friston, K. J. (2019)** REBUS and the Anarchic Brain, *Pharmacological Reviews* 71(3), 316-344 — **real-correct** (DOI 10.1124/pr.118.017160; title, authors, venue, volume, issue, pages all confirmed).
- **Godfrey-Smith, P. (2016)** *Other Minds* (FSG) — **real-correct**.
- **Godfrey-Smith, P. (2024)** Inferring Consciousness in Phylogenetically Distant Organisms, *Journal of Cognitive Neuroscience* 36(8) — **real-wrong-metadata**. Page range was **1660-1672**; the published record is **1660-1666** (Crossref DOI 10.1162/jocn_a_02158, MIT Press). Corrected.
- **Hameroff, S. & Penrose, R. (2014)** Consciousness in the universe, *Physics of Life Reviews* — **real-correct but incomplete**. Title truncated and volume/pages absent. Completed to "Consciousness in the universe: A review of the 'Orch OR' theory", 11(1), 39-78 (DOI 10.1016/j.plrev.2013.08.002). Note the adjacent *Reply to seven commentaries* at 11(1), 94-100 is a distinct item and is **not** what the article cites.
- **McGinn, C. (1989)** Can We Solve the Mind-Body Problem?, *Mind* 98(391), 349-366 — **real-correct** (DOI 10.1093/mind/xcviii.391.349).
- **Metzinger, T. (2024)** "Minimal Phenomenal Experience: The ARAS-Model Theory", *Neuroscience of Consciousness* — **fabricated**. See the family resolution below. Replaced with the real record.
- **Nagel, T. (1974)** What Is It Like to Be a Bat?, *The Philosophical Review* 83(4), 435-450 — **real-correct** (canonical record; Crossref rate-limited on the confirming call, metadata matches the standard citation exactly).
- **New York Declaration on Animal Consciousness (2024)** — **real-correct**. The article cites it unattributed, so the "Andrews & Monsó" misattribution fixed elsewhere in the corpus does not arise here. Both quoted tiers are faithful: "strong scientific support" for mammals and birds, "realistic possibility" extending outward.
- **Stapp, H. P. (2007)** *Mindful Universe* (Springer) — **real-correct**, and correctly disambiguated: the body cites it for the quantum Zeno mechanism, which *Mindful Universe* does treat (cf. `[[stapp-2007-mindful-universe-vs-2005-qid-paper]]`).
- **Khan, S., ... Wiest, M. C. et al. (2024)** epothilone B, *eNeuro* 11(8), ENEURO.0291-24.2024 — **real-correct** (carried from the 2026-06-02 verification; PMID 39147581).

**Currency sweep**: `find_superlative_claims` returns empty. No superlative empirical claims to re-date.

## Family Resolution: the Metzinger MPE/ARAS citation

No publication titled "Minimal Phenomenal Experience: The ARAS-Model Theory" exists in any venue. Crossref and OpenAlex title searches return nothing; a full sweep of Metzinger's post-2022 output and of every work titled "minimal phenomenal experience" turns up no such paper, and *Neuroscience of Consciousness* (ISSN 2057-2107) has no Metzinger item at all.

The real record is:

> Metzinger, T. (2020). Minimal phenomenal experience: Meditation, tonic alertness, and the phenomenology of "pure" consciousness. *Philosophy and the Mind Sciences*, 1(I), 1-44. DOI 10.33735/phimisci.2020.i.46

Two distinct corrupt variants were live in the corpus, and **the second was itself an incorrect fix**:

1. `(2024) ... Neuroscience of Consciousness` — the original fabrication. Live at three source loci.
2. `(2020) ... Cognitive Neuropsychology, 37(3-4), 149-153` — installed by the 2026-03-17 review of [[interface-heterogeneity]] as a "correction". It is also wrong. Metzinger does have an item in *Cognitive Neuropsychology* 37(3-4), but it is **"Self-modeling epistemic spaces and the contraction principle", pp. 197-201** (DOI 10.1080/02643294.2020.1729110) — a different paper. Pages 142-153 of that volume belong to Davis, Altmann & Yee, who are not Metzinger. The 2026-07-15 review of the same article *spotted* this mismatch and explicitly punted it as "out of scope for this pass"; it has been live since.

Had I grepped only the string in front of me (`Neuroscience of Consciousness`), variant 2 would have survived — the `[[narrow-grep-zero-is-not-proof-of-absence]]` trap. Grepping the concept token `ARAS` across all three trees is what caught it.

All loci now carry the canonical form. The body claims are untouched and were always sound: every article invokes the *term* "minimal phenomenal experience" attributed to Metzinger generically, which is correct regardless of which paper the reference line named.

## Loci Corrected (both families, all three trees)

Godfrey-Smith page range 1660-1672 → **1660-1666**:
- `obsidian/topics/comparative-consciousness-and-interface-differences.md`
- `obsidian/apex/minds-without-words.md`
- `obsidian/research/animal-consciousness-2024-2025-literature-2026-05-19.md`
- `obsidian/research/consciousness-simple-organisms-2026-01-19.md`
- `archive/concepts/minimal-consciousness.md`

Metzinger MPE → canonical *Philosophy and the Mind Sciences* 1(I), 1-44:
- `obsidian/topics/comparative-consciousness-and-interface-differences.md`
- `obsidian/apex/minds-without-words.md`
- `obsidian/concepts/interface-heterogeneity.md` (the mis-corrected variant)
- `archive/concepts/minimal-consciousness.md`

Research notes were included per ``research-note-self-flagged-gaps-propagate-to-the-article``; `archive/` was included per ``defect-sweeps-must-include-archive-tree`` — it carries full serving bodies. Post-fix grep for `ARAS` and `1660-1672` across `obsidian/` and `archive/` returns zero. Hugo mirrors regenerate on sync.

## Pessimistic Pass

No critical issues beyond the citation defects above.

- **Possibility/probability slippage**: none. Calibration is intact and load-bearing throughout — "None of these has been established", "remain entirely speculative", "No quantum consciousness mechanism has been confirmed", "presupposes more knowledge than we possess on both fronts". The New York Declaration tiers are quoted at their declared evidential level. The psychedelics passage explicitly frames itself as "a speculative analogy within the Map's framework" and uses the subjunctive ("If the analogy held"). Applying the §2 diagnostic test — would a tenet-accepting reviewer flag anything as overstated? — the answer is no.
- **Attribution**: clean. Metzinger's "minimal phenomenal experience" is verbatim and correctly attributed; Block's P/A distinction, Panksepp's primary emotional systems, and Godfrey-Smith on independent origins are all faithfully characterised. The self-quote of Tenet 2 is now verbatim against `tenets.md`.
- **Reasoning-mode**: three named-opponent engagements — materialists (Relation to Site Perspective), functionalists (Meditation section), MWI (No Many Worlds). All **Mode Three**, framework-boundary marking in natural prose, each explicitly declaring the disagreement rather than dressing it as refutation. Appropriate: all three reject the Map's tenets outright, so no in-framework argument is available. No label leakage — grep for the full forbidden-vocabulary set returns zero.

## Optimistic Pass

Strengths intact and preserved: the nature-vs-coupling framework itself, the four-possibility matrix, the three coupling-modes taxonomy (active selection / passive witnessing / minimal presence), the "What Would Challenge This View?" falsifier section, and the sustained calibrated hedging. The article's network role is settled — it is the structural layer above [[interface-efficacy-and-the-cognitive-gap]]'s grade axis and [[interface-heterogeneity]]'s kind axis, tied upward to [[evolution-under-dualism]]'s three-model taxonomy.

No expansion attempted: the article sits at 116% of the topics soft threshold.

## Length

3454 → 3473 words (116% of the 3000-word soft threshold; below the 4000 hard ceiling). The +19 is entirely the completed Hameroff & Penrose title and the longer Metzinger subtitle. Length-neutral mode observed — no content expansion, no condensation required.

## Changes Applied

- Two citation metadata defects fixed in the target article; one reference completed.
- Family resolution propagated to four sibling files across `obsidian/` and `archive/`.
- `ai_modified` + `last_deep_review` set on the target; `ai_modified` bumped on each modified sibling.

## Remaining Items

None for this article. One observation for the operator: `obsidian/concepts/interface-heterogeneity.md` has now had a citation "corrected" to a wrong record once and flagged-then-punted once. Its reference block is worth a dedicated web-verify pass, since a review that installs a bad fix leaves the file *looking* verified.

## Stability Notes

Bedrock disagreements remain acknowledged and must NOT be re-flagged in future reviews:
- Eliminativist objections to consciousness as a coherent category
- Functionalist reinterpretation of contemplative reports
- MWI indexical objections

These are framework-boundary standoffs, not fixable defects.

The deferred Gutfreund "Standing Agnostic Challenge" integration (noted 2026-05-08) remains optional and length-gated.

**Scheduling note — revised.** The last two reviews treated this article as converged *on the body* and inferred that the citations were converged too. That inference was wrong: the body had been stable for four passes while two bad references sat in the References block the whole time. Convergence damping should key on the body; the citation ledger is a **separate surface** and stays owed until a pass actually produces one. This article's ledger is now complete, so the damping is legitimate from here.
