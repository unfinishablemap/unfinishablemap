---
title: "Deep Review - The Phenomenology of Musical Understanding"
created: 2026-11-09
modified: 2026-11-09
human_modified: null
ai_modified: 2026-11-09T13:36:30+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-11-09
last_curated: null
---

**Date**: 2026-11-09
**Article**: [[phenomenology-of-musical-understanding|The Phenomenology of Musical Understanding]]
**Previous review**: [[deep-review-2026-07-25-phenomenology-of-musical-understanding|2026-07-25]] (also 2026-07-08, 2026-06-15, 2026-04-24, 2026-03-20, 2026-02-21)

## Context

Seventh deep review. Three commits changed the article since the 07-25 verification pass, and each introduced citation-bearing text the 06-15 / 07-25 ledgers never saw: (1) 2026-08-08 `4ca2b7c3b2` rewrote the `description` to carry the "on the Map's reading" attribution; (2) 2026-08-21 `99e1a823a1` consumed `research/machine-aesthetic-judgment-and-generative-music-systems-2026-08-07`, adding two quoted findings (Wei et al. 2024; Bhandari & Colton 2024) and three section-anchor links to falsifier 2; (3) 2026-10-14 `4658ea3d5e` gave body attributions to the five previously orphaned References (Husserl 1991, Scruton 1997: 1–96, Levinson 1997, Kivy 1989, Davies 1994: 221–67 and 279–307) and added the resemblance/contagion paragraph with a `#The Paradox of Tragedy` anchor. This pass therefore re-opens the citation channel for the new material only; the four monograph entries plus Fritz / Huron / Koelsch / Vuust stand on the 06-15 ledger (References lines unchanged since). Length at entry: 3,150 words (topics hard 4,000; headroom 849); length-neutral mode.

## Pessimistic Analysis Summary

### Critical Issues Found
None.

### Quotation Fidelity (32 quoted strings)
Of the quoted strings in the body, only two are attributed quotations; the rest are scare-quotes, hypothetical labels ("sad", "wistful", "same", "space") or the article's own gloss of a literature tendency ("explains the functional role of surprise" / "explains what surprise feels like" — unattributed paraphrase, not a quotation). No quotation is attributed to a Map page, so no internal-quote staleness check arises.

- Wei et al. 2024, "music theory concepts are discernible within foundation models and that the degree to which they are detectable varies by model size and layer" — **verbatim** in the arXiv 2410.00872 abstract (export API, fetched this pass).
- Bhandari & Colton 2024, "modelling the nuanced development of themes across extended compositions in the style of human composers remains difficult" — **verbatim** in the arXiv 2403.07995 abstract.

### Publisher-of-Record Citation Web-Verify (§2.4) — new material only
- Wei, Freeman, Donahue & Sun 2024 (Do Music Generation Models Encode Music Theory?) — state: **real-correct**. arXiv comment field: "Accepted at ISMIR 2024"; authors and title match; probing of Jukebox and MusicGen against the SynTheory dataset (tempos, time signatures, notes, intervals, scales, chords, progressions) matches the body's description. Result-direction leg: the paper reports *positive* decodability varying by model size and layer — same direction as the article's use.
- Bhandari & Colton 2024 (Motifs, Phrases, and Beyond) — state: **real-correct**. arXiv comment: "Accepted to … EvoMUSART 2024"; the body's "reviewing structure-modelling techniques" matches a literature review. Result-direction: the paper's own concluding caveat is quoted, not inverted.
- Levinson 1997 (*Music in the Moment*) — attribution **faithful**: SEP "The Philosophy of Music" states concatenationism as "basic musical understanding consists in following the musical and emotional qualities of passages of music, and transitions between them, that are short enough to be apprehended as a single experience", against architectonicism — the article's wording.
- Scruton 1997: 1–96 — attribution **faithful**: SEP cites "Scruton (1983; 1997: 1–96)" for the claim that experiences of musical space and movement "are irreducibly metaphorical, since they involve the application of spatial concepts to that which is not literally spatial". Page range is SEP's.
- Kivy 1989; Davies 1994: 221–67 — attribution **faithful**: SEP cites exactly "Kivy 1989 … S. Davies 1994: 221–67" for resemblance / contour / appearance theories, "the resemblance between [music's] dynamic character" and expressive human behaviour. Kivy 1989 is not credited with the no-felt-emotion thesis (that is later Kivy, not in References) — correct restraint, as the 10-14 changelog recorded.
- Davies 1994: 279–307 — attribution **faithful**: SEP cites "S. Davies 1994: 279–307" for emotional contagion / mirroring responses, adding that such a mood "is not about some intentional object" — the article's "moods take no object". A second secondary source (a philosophy-of-music paper) cites the same range for contagion.
- Husserl 1991 (Brough trans., Kluwer) — **real-correct** (Collected Works IV); the retention/protention sentence is a standard reading.
- Fritz 2009, Huron 2006, Koelsch 2014, Vuust 2022, Bergson, James — not re-opened; References lines unchanged since the 06-15 ledger.

Cited-author-stance leg: Kivy, Davies, Scruton and Levinson are all presented as offering a "naturalistic answer" or an aesthetic claim, not as endorsing dualism; Huron / Koelsch / Vuust are presented as functionalism's strongest case. No stance misrepresentation.

Cross-reference inline ↔ References: 13 References entries, 13 body surname mentions (Bergson 3, Husserl 1, James 1, Scruton 1, Levinson 1, Kivy 1, Davies 2, Fritz 2, Huron 2, Koelsch 1, Vuust 2, Wei 1, Bhandari 1); zero orphans in either direction. Every body (surname, year) token resolves to a References line.

### Empirical-Currency Sweep
No superlative claims; the one drift-susceptible claim (Fritz et al. 2009 cross-cultural recognition) remains hedged exactly as the 07-08 currency check approved. The two 2024 machine-music findings are themselves the currency update for falsifier 2 and are framed as constraining "in opposite directions" — not as a verdict.

### Calibration (lenses 3)
"Musical Qualia and the Hard Problem": the strong sentences ("resist functional analysis with particular force", "as immediate and irreducible as the redness of red", "the learning must latch onto a phenomenal quality") are framework claims a tenet-accepting reviewer would accept; the inverted-qualia paragraph closes on "suggests", and the Fritz paragraph hedges the major/minor mapping. "The Binding Achievement": "the binding is not computational aggregation but experiential unity" is the Map's register, stated inside the framework; no evidential-tier label is attached, so no possibility/probability slippage. "What Would Challenge This View?" still names three live falsifiers, and falsifier 2 ends on "what would have to be true, not a verdict either way". The Predictive-Coding Challenge remains the Mode Two engagement the 07-25 review classified (grants the mechanics, identifies the slide between functional and phenomenal explanation, marks the boundary). No `positions/` entry cites this page (grep of `obsidian/positions` returned none), so no register consistency check applies.

### Style
No "load-bearing"; no "This is not X. It is Y." construct; front-loaded lead; "Relation to Site Perspective" substantive across four tenets.

### Wikilinks
All 25 distinct targets resolve to exactly one live file (bare slugs; `concepts/functionalism` and `topics/phenomenal-value-realism` path-qualified and live). All seven section anchors resolve: `the-sublime-and-negative-aesthetics#The Paradox of Tragedy` (L62), `creative-consciousness#Why Machine-Creativity Criteria Fail to Discriminate` (L112), `ai-consciousness-typology#Producing and Judging Are Separate Capacities` (L145), and the four `tenets#^…` block ids (L51, L89, L113, L131).

### Medium / Low Issues Found
None.

## Optimistic Analysis Summary

### Strengths Preserved
All preserved unchanged: front-loaded opening; C-after-G vs C-after-F interpenetration example; inverted musical-qualia thought experiment; the 10-14 resemblance/contagion paragraph, which concedes the strongest naturalistic reply to "grief *about what*?" and relocates rather than denies the gap; the two-sided 2024 machine-music calibration in falsifier 2; MWI "unity-within-a-branch vs distribution of significance" distinction; the anti-epiphenomenalist explanatory-instability argument. Hardline-Empiricist read: the article grants functionalism its best case and claims only that musical phenomenology fits dualism, not that it evidences it.

### Enhancements Made
One zero-word integration. The new sibling [[vitality-form-void]] (created 2026-11-09) lists this page in its `topics:` and Further Reading ("the practice with a notation for the *how*"); its subject — the dynamic shape of an action or experience (surging, fading), read in gait and bearing — is what the resemblance theory's "dynamic shape" names. L103 `its dynamic shape` → `its [[vitality-form-void|dynamic shape]]`. Host sentence verified true of the target page (its §"A borrowed lexicon" and the Kim 2013 reference concern musical dynamic shape).

### Cross-links Added
- [[vitality-form-void]] (piped reciprocal on existing text, +0 words)

## Remaining Items
None. The pending cross-review task for `voids/vitality-form-void` may consider a second host at L116 ("Dynamic contour — loudness and its changes") but one reciprocal suffices.

## Stability Notes

- The article remains **converged** (seventh review, sixth consecutive with no critical issue). Word count 3,150 → 3,150 (+0).
- **Ledger now covers the post-07-25 citations**: Wei 2024 and Bhandari & Colton 2024 quotes verbatim at arXiv; Levinson 1997, Scruton 1997: 1–96, Kivy 1989, Davies 1994: 221–67 and 279–307 attributions match SEP "The Philosophy of Music" wording and page ranges. Future passes need not re-verify these unless the sentences change.
- **Bedrock disagreements, NOT to re-flag as critical**: eliminative-materialist / hard-nosed-physicalist rejection of qualia realism; Buddhist rejection of intrinsic natures; Dennett-style zombie-conceivability rejection.
- The tenet-section quantum-interaction reference is a legitimate tenet-level invocation, not unwarranted speculation.
- The "explains the functional role of surprise" / "explains what surprise feels like" pair is the article's own paraphrase of a literature tendency, not a quotation — do not hunt for a source.
