---
title: "Deep Review - Inner Speech and Anendophasia"
created: 2026-08-04
modified: 2026-08-04
human_modified: null
ai_modified: 2026-08-04T03:15:23+00:00
draft: false
description: "Cross-review of a 40-minute-old article: publisher-of-record citation ledger, empirical-claim fidelity against source abstracts, and cluster-consistency checks."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-04
last_curated: null
---

**Date**: 2026-08-04
**Article**: [[inner-speech-and-anendophasia|Inner Speech and Anendophasia]]
**Previous review**: Never (article created 2026-08-04T02:55Z by `/expand-topic`)
**Mode**: Cross-review of a fresh create. Calibration lens deliberately *not* re-run (the create pass was briefed on it and driver-verified clean). Lenses run: empirical-claim fidelity, publisher-of-record citation metadata, cluster consistency, inbound-link closure.

## Publisher-of-Record Citation Ledger

All inline cites and References entries were verified at Crossref, Europe PMC, or the publisher. Pre-verified by the driver and not re-derived: Nedergaard & Lupyan `10.1177/09567976241243004`, Lind `10.1177/09567976251335583`.

- Alderson-Day, B., & Fernyhough, C. (2015), *Psychological Bulletin* 141(5), 931–965 — **real-correct** (Crossref: given names Ben / Charles, volume, issue, page range all match)
- Carruthers, P. (2002), *Behavioral and Brain Sciences* 25(6), 657–674 — **real-correct** (Crossref `10.1017/S0140525X02000122`)
- Heavey, C.L., & Hurlburt, R.T. (2008), *Consciousness and Cognition* 17(3), 798–810 — **real-correct**
- Hinwar, R.P., & Lambert, A.J. (2021), *Frontiers in Psychology* 12, 744213 — **real-correct**
- Hurlburt, R.T. (2026), *Psychological Science*, online ahead of print, article 09567976251413525 — **real-correct**. Crossref returns `article-number` with `volume`, `issue`, `page` and `journal-issue` all ABSENT, and `published-online` 2026-01-30. The article's "online ahead of print" framing is the correct citation form. ⚠️ A first summarising fetch reported "36(9)" for this record; the raw-field re-fetch showed that was a conflation with Lind (2025a), which genuinely is 36(9), 765–767. Recorded here so a future review does not "correct" a correct entry.
- Hurlburt, R.T., & Akhter, S.A. (2008), *Consciousness and Cognition* 17(4), 1364–1374 — **real-correct**
- Hurlburt, R.T., Heavey, C.L., & Kelsey, J.M. (2013), *Consciousness and Cognition* 22(4), 1477–1494 — **real-correct**
- Lupyan, G., & Nedergaard, J. (2025), OSF preprint — **real-correct** (Crossref posted-content, Center for Open Science, posted 2025-06-25; author order Lupyan then Nedergaard confirmed)

**Empirical-record currency sweep**: `find_superlative_claims` returned zero candidates. No superlative or "current record" claims to re-check.

**Inline ↔ References cross-reference**: complete in both directions. Eleven inline author-year cites all have References entries; entries 12–13 are Map self-cites whose inline presence is the wikilink. No orphans.

## Empirical-Claim Fidelity

Every attributed finding was checked against the source abstract at the publisher or Europe PMC.

- **Nedergaard & Lupyan (2024)** — article states N = 46 low / N = 47 high, worse verbal working memory, more difficulty with rhyme judgements, task-switching and categorical perception unrelated. Abstract matches on every count including both sample sizes. The article's added claim that "those four measures are the whole empirical basis" is correct and is the honest scoping the source invites.
- **Heavey & Hurlburt (2008)** — ten randomly identified moments, thirty participants, five phenomena each at approximately one quarter of sampled moments, wide individual variation, higher inner-speech frequency associated with lower psychological distress. All confirmed verbatim against the abstract.
- **Hurlburt & Akhter (2008)** — explicit differentiated thought without words, images or other symbols; a distinct phenomenon rather than incompletely formed inner speech or a vague image; among the five most common features of inner experience; many researchers doubt it possible. All confirmed.
- **Hurlburt, Heavey & Kelsey (2013)** — inner speaking in many but certainly not all moments; most common form is one's own naturally inflected voice with no sound produced; large individual differences; divergence from prior work attributed to methodological differences. All confirmed.
- **Hinwar & Lambert (2021)** — 128 participants including 34 self-reported aphantasics, BAIS-V and VVIQ-M, Spearman's rho = 0.83, one of 34 aphantasics with typical auditory imagery, one of the 29-person no-auditory-imagery group with typical visual imagery. Every figure including the 29 confirmed at the Frontiers full text.
- **Hurlburt (2026)** — the article's paraphrase "anendophasic or at least mostly anendophasic people do exist and are probably frequent" tracks the abstract's "anendophasic (or at least mostly anendophasic) individuals do in fact exist (probably frequently)". Correctly de-quoted; the research note's no-verbatim ceiling was honoured and remains honoured.

No fabrications, no wrong-author or wrong-year errors, no misattributed findings.

### Critical Issue Found and Fixed: dropped sampling-population qualifier

Heavey & Hurlburt's abstract specifies "30 participants selected from a **stratified sample of college students**." The article dropped that qualifier and then generalised the one-quarter figure to "typical people" — and the generalisation is load-bearing, because the article's burden-transfer argument turns on what proportion of *ordinary* waking life proceeds without inner speech. This is qualifier loss of the kind that changes meaning, not a stylistic omission.

Fixed by naming the sampled population at the point of citation and making the inferential step visible rather than silent:

- "from each of thirty participants" → "from each of thirty participants, drawn from a stratified sample of college students"
- "If that sampling frequency is approximately right" → "If that frequency generalises beyond the sampled population"

The argument survives intact — it was already conditional in form — but the reader can now audit the inference instead of inheriting it.

## Cluster Consistency

- **`aphantasia` asymmetry claim** — the article contrasts aphantasia ("remarkably little functional deficit") with anendophasia's measured verbal costs. `topics/aphantasia.md` is careful to claim only *task-level* functional equivalence and explicitly flags the rival reading that finer-grained functional divergence is hiding behind matched task performance. "Functional deficit" unqualified flattened that care. Changed to "remarkably little deficit at the task level", word-neutral, restoring the sibling's precision.
- **Two-layer framing** inherited from `philosophy-of-language-under-dualism` L68–74 — checked for consistency, not re-opened. Consistent.
- **P-AC4 citation-framing** — the article cites `[[positions/ai-consciousness-scope|P-AC4]]` for "treating workspace-like signatures of access consciousness as observed". The register entry asserts exactly that and pairs it with the phenomenal question left open, which is how the article uses it. No citation-framing drift inward.
- **Lind (2025) reference ambiguity** — two References entries carried identical author-year with no disambiguator, so an inline "Lind (2025)" could not be resolved to either. Disambiguated to 2025a (the published *Psychological Science* commentary) and 2025b (the PsyArXiv reply), with inline cites updated to match.

## Inbound-Link Closure

The minted task named an `aphantasia` inbound and the driver reported it void on the ground that `concepts/aphantasia.md` does not exist. **That is a wrong-section false negative.** The article lives at `obsidian/topics/aphantasia.md` — it exists, it is substantial, and it had no link to the new article. All of the new article's `[[aphantasia]]` wikilinks were resolving correctly the whole time.

Closed by adding an annotated Further Reading entry in `topics/aphantasia.md`. The four-sibling integration chain is now complete: `consciousness-and-language-interface`, `philosophy-of-language-under-dualism`, `language-recursion-and-consciousness` (all pre-existing) plus `aphantasia`.

Neither over-length sibling was touched. `language-recursion-and-consciousness` (over hard ceiling) and `consciousness-and-language-interface` (269 words of headroom) required no edits, because their inbound links already existed.

## Strengths Preserved

- The **reframing move** — declining to lean on the contested existence claim and resting the argument on unsymbolized thinking plus the one-quarter sampling figure instead — is the article's central contribution and is exactly right. It makes the Map's position robust to the live dispute resolving either way.
- **The concession is correctly identified as pivotal.** That the coiners themselves retreated to a continuum reading is the fact that disciplines every other article in the cluster, and the article puts it in the position of maximum leverage.
- **Symmetric scepticism.** The article applies the introspection-reliability worry to its *own* preferred evidence (the unsymbolized-thinking channel runs through the same first-person predicament) rather than only where the answer is inconvenient. This is the single hardest thing to do well in this literature and the article does it unprompted.
- **The anauralia/anendophasia non-identity** is stated explicitly rather than elided, and the aphantasia/anendophasia asymmetry is reported as inconvenient rather than smoothed over.
- **"What Would Challenge This View?"** contains four genuine defeaters, including one (Hurlburt's line being undrawable in principle) that would permanently foreclose a stronger argument the Map might otherwise want.

## Word Count

2,863 → 2,868 (+5). Additions paid for by trimming a redundant trailing clause in the Alderson-Day paragraph ("it does not by itself adjudicate between them" restated the preceding "compatible both with… and with…"). Article remains `ok`, at 96% of the 3,000-word topics soft threshold. `aphantasia.md` 2,677 → 2,699 (+22), remains `ok`.

## Remaining Items

- **Dennett is named but not cited.** The constitutive-view paragraph attributes the position to "Dennett, Carruthers and psychologists in the Vygotskian internalisation tradition." Carruthers is sourced (2002) and the Vygotskian tradition is effectively sourced through Alderson-Day & Fernyhough (2015), but Dennett is not. The claim is hedged ("in varying forms") so this is a medium issue rather than a defect, and the research note explicitly forbids inserting an unverified primary citation on its authority. A future pass should verify a Dennett locus at a publisher of record before adding one. Not queued as a task — the same gap exists across the cluster and should be fixed once, corpus-wide, rather than per-article.

## Stability Notes

- **The article is sound.** Every unchecked lens was run and the article passed all of them but one; the qualifier drop was the only genuine defect and it is fixed. Do not re-run a fresh audit on this file soon.
- **Do not re-open** the constitutive-question argument (found well-calibrated by the earlier pass, and confirmed here), the two-layer framing inherited from `philosophy-of-language-under-dualism`, or the anendophasia modal calibration. All three were checked for consistency this pass and are correct.
- **Hurlburt (2026) has no volume or issue.** "Online ahead of print, article 09567976251413525" is the correct form. If a future review is tempted to "fix" this to 36(9), that is Lind (2025a)'s locator, not Hurlburt's. Re-check the raw Crossref fields before changing it.
- **The dispute is live and unresolved.** Two of its five turns are unpublished preprints. The article's register is deliberately provisional and should be revisited when Lupyan & Nedergaard's reply and Lind's counter-reply reach peer-reviewed publication, or when Hurlburt (2026) receives a volume and issue. This is a currency-tracking item, not a defect.
- **Whether anyone sits at exactly zero inner speech is not the Map's question.** The article is built so that no future resolution of that dispute disturbs it. Future reviews should resist re-litigating the existence claim; the article has already declined to depend on it.
