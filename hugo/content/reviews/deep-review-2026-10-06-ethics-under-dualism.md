---
ai_contribution: 100
ai_generated_date: 2026-10-06
ai_modified: 2026-10-06 01:44:15+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-10-06
date: &id001 2026-10-06
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-06 01:44:15+00:00
modified: *id001
related_articles:
- '[[ethics-under-dualism]]'
title: Deep Review - Ethics Under Dualism
topics: []
---

**Date**: 2026-10-06
**Article**: [Ethics Under Dualism](/topics/ethics-under-dualism/)
**Previous review**: [2026-08-02](/reviews/deep-review-2026-08-02-ethics-under-dualism/) (fifth pass; priors 05-15, 06-02, 07-14, 08-02)
**Word count**: prose 3360 → 3359 (−1, length-neutral); apparatus 397 → 449 (+52: three References entries, one page range)

## What Changed Since 2026-08-02 (scope of this pass)

Unlike the 08-02 pass, where every diff was a cross-link installed by another article, this time the article was edited on its own merits by five September refine-draft passes plus one inbound cross-link rewire:

- `0fdeabeb51` (09-05): criterion moved from "all conscious beings" to felt valence; the Chalmers Vulcan paragraph, [P-MS1](/positions/moral-status/#p-ms1) anchor, and falsifier #6 added.
- `e43e0c058c` (09-07): "elimination of causal luck" → "moral luck relocated rather than eliminated"; Frankfurt / Fischer & Ravizza / Wolf compatibilist nuance added.
- `5905e1129b`, `9b63cbeb6e` (09-20): categorical "AI lacks consciousness" → "probably lacks *bidirectionally coupled* consciousness; bare phenomenality stays open"; description re-scoped to the valence criterion.
- `966607deba` (10-01): covert-consciousness denominator fix; anchor into `covert-consciousness-and-cognitive-motor-dissociation#the-numbers-and-their-denominators`.

Prose crossed the 3000 topics soft threshold for the first time (2992 on 08-02 → 3360 now), so this pass ran **length-neutral on prose**, decomposed per the 08-02 instruction rather than taken from `analyze_length`'s total (3757).

**§2.4 trigger fired**: the References block changed (Chalmers added 09-05) and the body gained new attributions (three compatibilists) and a new empirical anchor. Web-verify was run on exactly those; the 06-02 ledger stands for everything else.

## Critical Issues Found

**1. Stale "forthcoming" on the article's newest and most argument-bearing cite — FIXED, with family resolution.**
Chalmers, "Sentience and Moral Status", was cited as *forthcoming* in Lee & Pautz (eds.), *The Importance of Being Conscious*, OUP. The volume was published 3 September 2026 (Google Books record, ISBN 9780198872924, 400 pp.; Kinokuniya lists the September 2026 release). Google Books' search-within index (volume id `v18EEgAAQBAJ`, control query passed) gives the table of contents: Part I, ch. 1 "Sentience and Moral Status", David J. Chalmers, p. 25; ch. 2 (Harman) begins p. 41 — so pp. 25–40. Entry updated to `(2026) … (pp. 25–40)`; inline `Chalmers (forthcoming)` → `Chalmers (2026)`. Propagated to the two live siblings carrying the identical entry — `concepts/sentientism` (References) and `concepts/consciousness-value-connection` (References + inline L130) — and to the same volume's Kriegel chapter (ch. 3, from p. 61) in `topics/the-experience-requirement-on-well-being` (References + inline L56). Classified **real-wrong-metadata** (status-stale), not a fabrication.

**2. Three new name-attributions with no years and no References entries — FIXED by citing, not deleting.**
The 09-07 refine added "Sophisticated compatibilists from Frankfurt to Fischer and Ravizza to Wolf ground desert in … (identification, mechanism-level reasoning, normative competence)" with no bibliographic anchor. The attributions are correct (identification → Frankfurt; moderate reasons-responsiveness of the mechanism → Fischer & Ravizza; normative competence / the Reason View → Wolf). Verified at Crossref and added: Frankfurt 1971 *J. Phil.* 68(1): 5–20 (DOI 10.2307/2024717); Fischer & Ravizza 1998 CUP (DOI 10.1017/cbo9780511814594); Wolf 1990 OUP (DOI 10.1093/oso/9780195056167.001.0001). Years added inline (+3 prose words).

## Medium Issues Found

**Mode-honesty tension between body and Relation section — FIXED.** The Illusionist Challenge section (L179) says the disagreement with Frankish "is a framework-boundary one, honestly noted, not a refutation either way"; the Dualism tenet paragraph (L198) said "the illusionist challenge *fails* because phenomenal consciousness … grounds value." The Relation section is tenet-conditional, so the second is defensible as framework-conditional, but the two sentences read as Mode Three and Mode One about the same opponent. Rewritten: "is turned back at the framework boundary rather than refuted". (+8 words.)

**Overstatement against a linked sibling — FIXED.** "editing its values raises autonomy concerns impossible for biological consciousness" — the article's own cross-linked `ethics-of-cognitive-enhancement-under-dualism` treats pharmacological and neural value-shaping interventions on biological subjects. "Impossible" → "with no clean biological analogue".

**Modal slip — FIXED.** Simulation ethics: "simulations *may* be incapable of it, so simulated 'suffering' *wouldn't* be real suffering" asserted the consequent flat after a hedged antecedent. → "in which case … would not be".

**Redundancy trimmed to pay for the above.** The AI-interface point was stated three times (taxonomy bullet, post-table paragraph, AI section). The post-table restatement (37 words) was reduced to a 24-word pointer at the criterion stated above; "Individual arguments … individual pillars" doubling in the Unity Argument cut (−5); a redundant "regardless" after "Either way" (−1). Net prose −1.

## Per-Cite Ledger (this pass)

- **Chalmers 2026** ("Sentience and Moral Status") — state: **real-wrong-metadata** (was *forthcoming*; corrected to 2026, pp. 25–40). Attribution leg: preprint text at consc.net, 7,375 words extracted and grepped — Vulcans "consciously perceive, think, and act, but they do not experience pain, pleasure, happiness, and suffering"; "I am extremely unsympathetic with affective sentientism (and I think it is near-obviously false)"; "Vulcans are conscious beings. Their lives matter." Published text p. 31 (Google Books snippet): "affective sentientism is false. It is not the case that affective consciousness is required to have moral status." Article's gloss ("Chalmers concludes that Vulcans have moral status and that affective sentientism is false") is faithful; falsifier #6's necessity-direction reading matches Chalmers' stated focus on the "only if" claim. Stance leg: Chalmers argues *against* the Map's criterion — the article presents him as the opponent whose bullet the Map bites, correctly.
- **Frankfurt 1971, Fischer & Ravizza 1998, Wolf 1990** — state: **real-correct**, newly added (were uncited name-drops). Stance leg: all three are compatibilists cited as the position the Map contrasts with, not as allies — correct.
- **Bodien et al. 2024** — body claim re-checked against the 10-01 anchor target: "60 of the 241 participants (25%) without an observable response to commands" matches "roughly a quarter of patients without observable command-following". Metadata unchanged since the 08-02 publisher check. Result-direction leg: positive, as claimed.
- **Kriegel 2026** (sibling file only) — state: real-wrong-metadata (status-stale), corrected; same volume, same source.
- All other entries — unchanged since the 06-02 publisher-of-record ledger; not re-litigated.

## Cross-Link Claims Checked (08-02 lesson applied)

Every anchor added since 08-02 resolves and its installed claim matches its target: `positions/moral-status#^p-ms1` (necessary-and-sufficient, phenomenal, Vulcan limb named there too); `consciousness-value-connection#Implications`; `covert-consciousness-and-cognitive-motor-dissociation#the-numbers-and-their-denominators`; `compatibilist-symmetry-challenge`; the AI section's "bidirectionally coupled / bare phenomenality stays open" wording mirrors `topics/ai-consciousness` L153 almost verbatim. No dropped qualifiers found this time.

## Engagement Modes (editor-internal)

- **Chalmers (Vulcans)**: Mode Three — the Map accepts the cost of denying Vulcan status on its own value-grounding; no internal-to-Chalmers refutation claimed. Honest.
- **Frankfurt / Fischer & Ravizza / Wolf**: Mixed — the article concedes their capacities are "metaphysically substantive" and locates the disagreement at irreducible-vs-derivative, deferring the "does it do additional work" question to the symmetry challenge. Honest; an improvement on the pre-09-07 "pragmatic convention" strawman.
- **Illusionism / Frankish**: Mixed → now consistently so after the Relation-section fix.
- All prior classifications unchanged (Mackie Mode One; Korsgaard Mode Two; Railton, Foot Mode One; Parfit Mode Three).

No editor-vocabulary label leakage in article prose (full forbidden-label set scanned); none introduced.

## Calibration Pass

Diagnostic test applied to the September additions. The valence-criterion paragraph is careful: "the narrower criterion changes no verdict here; it settles which property the verdicts track." The AI verdict moved *toward* calibration honesty (categorical → conditional on the interface criterion). No possibility/probability slippage. The patienthood table's "Insects — Low" sits below the New York Declaration's "realistic possibility" and Birch's candidate framing; this was accepted in earlier passes as the Map's own confidence assignment, and the invertebrate paragraph explicitly says even "Low" warrants precaution — not re-flagged.

## Optimistic Summary

Strengths preserved: the two-claim front-loaded lead (now valence-precise), the four-pillars architecture, the compatibilist paragraph's new honesty about Frankfurt/Fischer-Ravizza/Wolf (Libertarian persona notes it strengthens rather than weakens the irreducible-vs-derivative contrast), the Chalmers bullet-biting (Hardline Empiricist persona: the article names its strongest living opponent and the published page where he says the Map's criterion is "near-obviously false" — rare candour), and the six-item falsifier list. No expansion attempted: prose is over threshold.

## Remaining Items

- **[positions/moral-status.md](/positions/moral-status/) L55** still reads "Chalmers' Vulcan (forthcoming; Shepherd 2024 takes it up)". Not edited here: the register mandates a dated calibration-history note for any change, which is a `positions-evolve` job. One-line fix: `(forthcoming` → `(2026`.
- **Archived original** `archive/topics/ethics-of-consciousness.md:73` still carries the superseded 15–20% covert-awareness figure (flagged 08-02; convention call, unactioned).
- **Street / Darwinian-Dilemma gap** — human-deferred length decision, unchanged since 07-14. With prose now over the soft threshold the case for adding it has weakened further.

## Stability Notes

Convergence holds on everything the 06-02 / 07-14 / 08-02 passes settled; this pass added nothing to the stability list and removed nothing from it. Future reviews should NOT: re-run the publisher web-verify on the 17 entries unchanged since 06-02; re-flag illusionism, Many-Worlds, hard-physicalist rejection of agent causation, or Tegmark decoherence as critical; re-open the moral-realism presupposition; re-litigate the "Insects — Low" row; attempt the Street gap; or assume the article is under the prose threshold — it is now over it (3359), so additions need matching cuts.

Transferable lesson: **a "forthcoming" tag is a dated claim with a short shelf life.** Three live articles and one register entry carried the same forthcoming cite for a month after the volume shipped. A forthcoming cite older than ~6 months should be re-checked for publication on every pass that touches the file, and the check is cheap — one Google Books ISBN lookup plus the search-within endpoint gives year and page range without the quota-limited API.