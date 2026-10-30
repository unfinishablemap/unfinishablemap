---
title: "Deep Review - Neural Refresh Rates and the Smoothness Problem"
created: 2026-10-30
modified: 2026-10-30
human_modified: null
ai_modified: 2026-10-30T10:44:45+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[neural-refresh-rates-and-the-smoothness-problem]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-30
last_curated: null
---

**Date**: 2026-10-30
**Article**: [[neural-refresh-rates-and-the-smoothness-problem|Neural Refresh Rates and the Smoothness Problem]]
**Previous review**: [[deep-review-2026-09-10-neural-refresh-rates|2026-09-10]] (full). The 2026-10-24 pass ([[deep-review-2026-10-24-neural-refresh-rates-and-the-smoothness-problem-integration|integration]]) only retargeted inbound links and did not review the host's body.

## Scope

The article is converged on its older text after fourteen deep reviews, so this was a delta review only: `git diff f19eb1a772 HEAD` (+45/−19). Three changes landed after the 09-10 review:

- (a) the 2026-10-11 **coalesce** of `voids/smoothness-and-continuity` into `## The Continuity Void` (L95–105), plus the lead sentence, description and frontmatter that came with it;
- (b) the 2026-10-19 **refine** (d9776b46b7), which added the Hesse et al. 2026 content-stability paragraph (L115) and reference 7;
- (c) the 2026-09-27 **refine** (aeac8ddf84), which changed "discreteness" to "rhythmicity" or "periodic" in five places, the Relation section at L145 among them.

Settled passages were not re-litigated.

## Pessimistic Analysis Summary

### Critical Issues Found

None.

### Medium Issues Found

- **L145 tier mismatch left over from the 09-27 fix. FIXED.** The 09-27 refine corrected the subject of the sentence (from "the discreteness of neural processing" to "the rhythmicity of neural sampling") but kept the predicate "is empirically established". The page's evidence sections say "well evidenced" twice, using the same words (lead L51, "That the sampling is rhythmic is well evidenced"; L55, "The rhythmicity of sampling is well evidenced"). So the Relation section, where the dualism tenet is being supported, stated the finding one tier higher than the article's own evidence sections. The surface to harmonise toward is the tested one. The evidence also supports the lower tier: rhythmic perceptual sampling is substantially evidenced but not settled (see the Brookshire 2022 currency finding under Remaining Items).
  - Old: "…because the rhythmicity of neural sampling is empirically established, making the gap particularly precise."
  - New: "…because the rhythmicity of neural sampling is well evidenced, making the gap particularly precise."
  - Net 0 words. The next line starts a new paragraph, so no pronoun is affected.

### (a) Coalesce check: The Continuity Void (L95–105) against `archive/voids/smoothness-and-continuity.md`

I compared the merged section with the archived void sentence by sentence. The coalesce was careful. Every known overclaim on the void was left behind:

| Archived-void defect | Imported? |
|---|---|
| L57 "Neuroscience has established that neural processing is fundamentally punctuated" | No |
| L59 "Psychophysical evidence confirms this — the flash-lag effect…" (Cottier 2025 refutes the flash-lag inference) | No |
| L63 colour phi "impossible under purely continuous models" | No |
| L67 Dainton "interconnected flowing whole" in quotation marks (publisher's synopsis, not Dainton's prose); Husserl "retained in grasp" quote | No |
| L73–75 "Lee demonstrates… Lee shows that this feeling is precisely what cannot be trusted" | No. Merged L103 uses the host's calibrated "Lee's result, to the extent it transfers, leaves open" |
| L95 "the difficulty is likely in the territory rather than the explorer" | No |
| L117 "precisely what Lee's analysis undermines" | No. Recast as above |

No hedge was dropped in the merge. The framework-relative verdict from the void's lead is kept at L105: circularity and non-convergence are framework-independent, the permanent-limit reading is dualism-specific, and under the common-cause null the void adds coherence, not confirmation. The [[apex/taxonomy-of-voids#void-clustering-audit|void clustering audit]] anchor resolves (heading at apex L175). The audit gives the origin-class method and does not single out this void, which is how L105 uses it ("see"). The section contains no direct quotations, so there was nothing to verify verbatim. It does not quote any other Map page.

What did change in the merge:

- The specious-present range is now "a fraction of a second to several seconds", with no citation. It was "…to 1.5 seconds (Lockwood 1989)", with the Strawson and Lockwood references, which were dropped. The new range is accurate (the subjective-present literature runs to roughly 2–3 s, and James allowed longer), and the dropped references are not orphaned because nothing cites them. Left as is.
- Bergson's warning about spatialised time (L101) is the *Time and Free Will* thesis, but the host's only Bergson reference is *Creative Evolution*, ch. 4. The attribution is faithful as a paraphrase, and the cinematographic chapter makes the same point. Low priority. A reference costs about 8 words the page does not have.

### (b) Hesse et al. 2026, verified at the publisher of record

- **Hesse, Lanfranchi, McGrory, Shi, Engel & Tsao (2026), *Rapid alternation of conscious and suppressed stimulus representations in the primate brain*, bioRxiv v1. State: real-correct.** The bioRxiv API record for doi:10.64898/2026.10.15.759299 matches title, all six authors, v1, posted 2026-10-16, `published: NA`. Crossref gives `type: posted-content / preprint`, publisher openRxiv. The PDF footer reads "which was not certified by peer review".
- **Claim fidelity, checked against the full text** (v1 PDF, 35 pp., extracted with `pdftotext`; I grepped it myself and did not rely on a summariser):
  - "two macaques": "Data were recorded from two monkeys" ✓
  - "The monkeys reported nothing": they passively fixated and were rewarded "for maintaining fixation"; trials were kept only with fixation held for ≥90% of the trial ✓
  - "percept labels come from 14 human observers": "across all 14 human participants", who "reported by button press" left eye, right eye or mixed ✓
  - "latency near 0.86 s": "Because button reports lag stimulus presentation… (0.86 ± 0.05 s, mean latency ± s.e.m.)" ✓
  - "about half the time": "state 1 and state 2 were occupied about equally" ✓
  - "runs of about 60 ms": "median dwell time plateaued around ~60 ms" ✓
  - "nearly pure form": the abstract says "a pure signal of conscious perception was present", so the page's "nearly" is the more cautious wording ✓
  - "more weakly, prefrontal": "Reconstructions were of lower quality than in inferotemporal cortex" ✓
  - "the study treats that percept as steady": "during a constant stimulus and percept" ✓
  - "untested physicalist reply, routing…": "One possibility is that this signature determines whether a sensory representation is dynamically routed to downstream systems…", and the authors "set aside the 'hard problem'" ✓
- **Labelled unrefereed**: yes. The body says "A 2026 preprint… the preprint is unreplicated", and reference 7 says "*bioRxiv* preprint, v1 (not peer-reviewed)". The "15 Hz" switching rate does not appear anywhere on the page, which is correct. It is a Markov switching rate, not a rhythm.
- **Result direction**: as reported. Calibration: offered as sharpening an explanatory target, with no tenet upgrade. The question it raises ("why a face carried half the time is experienced as unbroken") is scoped to "those who reject the functionalist dissolution".
- Considered and not changed: "Human report, with a latency near 0.86 s, cannot resolve 60 ms structure". An Empiricist could object that latency is not resolution, since temporal-order judgements resolve tens of ms despite long RTs. In this paradigm, though, the report is a three-way button press that lags the display, and the paper itself shifts its human analysis window by that latency. The conclusion stands, and a rewrite would cost words without making it more accurate.

### (c) The 2026-09-27 Relation fix

The fix survived: "discreteness of neural" now has 0 hits. Its predicate left the tier mismatch fixed above.

### Coalesce-regression checks (substring greps, `grep -ciF`)

- `confirm`: 1 hit, at L105 "independent confirmation of them" (benign). Neither "confirms discrete sampling" nor "Psychophysical evidence confirms" is present ✓
- `flash-lag`: 1 hit, at L59, inside the Cottier et al. 2025 calibration ("found no correlation with any") ✓. `wagon`, `reveal periodic` and `all reveal` have 0 hits ✓
- `empirically established`: 1 hit before this pass (L145, the leftover fixed above), 0 after.
- `could imp`: 1 hit, at L55. The VanRullen quotation was **re-verified verbatim** against the Europe PMC abstract of VanRullen 2016 (*TICS* 20(10), doi 10.1016/j.tics.2016.07.006): "This could imply that perception and cognition operate periodically, as a succession of cycles mirroring the underlying oscillations", and "remain open questions" also appears verbatim. The host had this wording before 10-11. The 10-11 repair named in the P3 task near todo L1583 was made to the void copy.
- James: `described consciousness` has 0 hits, and the rainbow sentence is still attributed to *the specious present* ✓. Dainton: the "interconnected flowing whole" phrasing appears only as paraphrase plus the reference-4 provenance note ✓

### Other sweeps

- Over-concession tells: `no possible`, `cannot ever`, `can never` and `impossible` have 0 hits. `in principle` appears once, at L123 ("could, in principle, differ"), which is settled and benign.
- Editor-label leakage: all forbidden labels have 0 hits. "This is not X. It is Y." has 0 hits; the one `It is not` match is a false positive on James's "It is nothing jointed". `load-bearing` has 0 hits.
- Epiphenomenalism: nothing concedes it. The Relation section's bidirectional-interaction paragraph and its new self-referential continuity-void sentence (L147) are both hedged ("one possibility", "If consciousness also helps set…").

### Reasoning-Mode Classification (editor-internal)

- **Hesse authors' routing reply** (L115): Mode Two, by reference. It "joins the mechanisms above", and the page's functionalist section supplies the unsupported-move identification. The scope is honest ("For those who reject the functionalist dissolution").
- **Dennett's Multiple Drafts** (L103): described, not rebutted ("the fourth denies that the predictions describe anything real"). The coalesce dropped the void's reply instead of keeping it, so there is no boundary-substitution risk.
- Functionalism, illusionism and higher-order/GWT engagements are unchanged since the 09-10 classifications (Mode Two, Mode Two, Mode Three).

## Optimistic Analysis Summary

### Strengths Preserved

- The coalesce is a model of how to merge: a 2,535-word void reduced to a 373-word section of three named obstacles (circularity, non-convergence, underdetermination), with every calibration the void had earned through its own reviews kept and every overclaim left in the archive.
- The Hesse paragraph keeps its claims within what the data show. It says what the monkeys did not do, where the labels come from, that the result is unreplicated, and that the routing reply is the authors' own and untested. It then ties the data to the continuity void without claiming they support it.
- The lead's new sentence front-loads the void with the right hedge ("may be unable to tell from the inside").

### Enhancements Made

One calibration harmonisation (L145). Nothing was added; the article is 9 words under the hard gate.

### Cross-links Added

None.

## Length

`analyze_length`: **3,991 → 3,991** (topics 3,000 soft / 4,000 hard, gate `>=`), status `soft_warning`. Net 0.

## Remaining Items

- **Empirical-record currency, minted as P3 refine-draft in todo.md.** The lead's own-voice "a slower attentional rhythm near 7 Hz" (L51) and L57's "Reaction times fluctuate rhythmically" do not mention **Brookshire, G. (2022)**, "Putative rhythms in attentional switching can be explained by aperiodic temporal structure", *Nature Human Behaviour* 6, 1280–1291, doi 10.1038/s41562-022-01364-0. I verified it from the Europe PMC abstract and Crossref. Re-analysing published datasets, it finds "no evidence for behavioural rhythms in attentional switching after accounting for aperiodic temporal structure". Its scope is behavioural evidence only. It does not reach the alpha-phase detection findings, the attentional blink, or neural recordings, and the page's report of VanRullen 2016 is still faithful to that review. The corpus cites it nowhere. It falls outside this delta and its +8 budget. The task also lists two leads I have not read: Ruzzoli et al. 2019 (*Cortex* 120) and Keitel et al. 2022 (*EJN*).
- **Navigation surface, low priority, not edited.** `voids/voids.md` L196 describes the section as showing "why consciousness cannot determine its own temporal grain", which is unhedged against the section's own "may be unanswerable from inside". I am noting this here instead of editing the index from a host review.
- A *Time and Free Will* reference for the spatialised-time warning at L101 is low priority and needs about 8 words.

## Stability Notes

- **Do NOT re-flag**: the Hesse et al. 2026 metadata and the ten claim-fidelity points above, all verified against the v1 full text; the coalesced Continuity Void section's calibrations; the VanRullen "could imply" quotation, re-verified verbatim; and everything on the 09-10 do-not-re-flag list.
- **Do NOT reintroduce**: "empirically established" for neural rhythmicity (the evidence sections say "well evidenced"); any of the archived void's overclaims listed in the table above; "15 Hz" in the rhythm list.
- **Bedrock, not defects**: the claim that the three temporal-consciousness models "predict identical phenomenology" (L103) is the Map's underdetermination reading, and their proponents contest it. Dainton, for one, holds that the cinematic model cannot accommodate experienced change. This is a framework-level philosophical claim carried over unchanged from the void's reviewed text, not a calibration error. Functionalists and illusionists will continue to read the smoothing mechanisms as constituting smooth experience.
- If the Hesse preprint is revised or published, re-check reference 7 (the version number and the venue) and the figures in the L115 paragraph.
