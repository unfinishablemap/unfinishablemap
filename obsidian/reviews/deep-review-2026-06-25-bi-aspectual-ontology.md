---
title: "Deep Review - Bi-Aspectual Ontology"
created: 2026-06-25
modified: 2026-06-25
human_modified: null
ai_modified: 2026-06-25T18:23:13+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[bi-aspectual-ontology]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-25
last_curated: null
---

**Date**: 2026-06-25
**Article**: [[bi-aspectual-ontology|Bi-Aspectual Ontology]]
**Pass**: 30-day staleness re-review (settled since 2026-05-27, opus-4-6 build → fresh-eyes warrant; Tenet 1 load-bearing). **Orchestrator-finalized**: the deep-review fork applied 4 edits then monitor-wait-bailed before its citation subagent returned; the subagent completed ~3.5 min later with a publisher-of-record ledger, the orchestrator independently web-verified the major value-flips, applied the confident fixes, held one ambiguous one, and finalized (see [[fork-abandons-subagent-wrong-decline]]).

## Verdict: real-findings pass — 3 citation/attribution fixes + 3 fork inline-attribution/link fixes; 1 cite HELD (Pautz, ambiguous)

Another converged-≠-verified case: this "settled" Tenet-1 article carried multiple citation-metadata defects under an unchanged body.

## Fixes applied
**From the review fork (kept — verified):**
1. Added inline attributions to three existing References: "(Chalmers 1996)" on the hard problem, "(Tononi 2008)" on IIT, "(Fuchs 2017)" on QBism — all matching the correct References entries.
2. Reference #11 archival-link-rot fix: "Psychophysical Coupling" (2026-03-05, `/concepts/psychophysical-coupling/`) → "Psychophysical Laws and Coupling" (2026-01-16, `/concepts/psychophysical-laws/`). Verified: `psychophysical-coupling.md` is ARCHIVED; `psychophysical-laws.md` is LIVE (title + 2026-01-16 created date confirmed); the in-body `[[psychophysical-laws]]` wikilink (×5) already pointed at the live article.

**From the citation subagent + orchestrator web-verify (publisher-of-record):**
3. **Velmans — full citation corrected.** Was "(2009). Reflexive Monism. *JCS* 16(2-3), 209-236" → **(2008). *JCS* 15(2), 5-50** (independently confirmed via PhilPapers/Goldsmiths/Wikipedia — the paper titled exactly "Reflexive monism" is JCS 15(2):5-50, 2008; the cited year/vol/issue/pages were all wrong).
4. **Cutter — end page off-by-one.** "109-130" → **109-129** (subagent cross-checked SEP bibliography + Wiley + PhilPapers; all agree 109-129).
5. **Le Bihan (2019) in-body attribution corrected (Claim C).** The article said "Le Bihan (2019) challenges whether 'aspect' vocabulary does genuine explanatory work" — but Le Bihan's "Aspects in Dual-Aspect Monism and Panpsychism: A Rejoinder to Benovsky" *defends* a **realist** reading of aspects *against* the deflationary/anti-realist worry; the article had it backwards (attributing the skeptical challenge to Le Bihan, when that worry is the target he rebuts). Re-worded: the deflationary worry is now presented as the live challenge the Map must answer, with Le Bihan correctly cast as defending realist aspects against it. (The self-critical challenge is retained; only the attribution is fixed.)

## HELD — needs careful resolution (NOT changed this pass)
- **#6 Pautz (2017).** The subagent recommended changing to "2015, *Consciousness in the Physical World: Perspectives on Russellian Monism* (Alter & Nagasawa, eds., OUP)." The container volume IS real (OUP, ISBN 9780199927357) and the cite's short title "Russellian Monism" is at minimum incomplete. BUT orchestrator WebSearch surfaced a genuine ambiguity: "How Is Constitutive Russellian Monism (or Panpsychism) Better than Dualism?" appears to be a **2017 reply to Roelofs**, possibly a *separate* piece from the 2015 volume's Pautz chapter ("A Dilemma for Russellian Monists about Consciousness"). Applying the subagent's 2015-retitle could be wrong if these are different pieces. Per the [[citation-verify-false-negative]] / Lee-Bergson discipline (do not apply an unverified citation flip), this is LEFT UNCHANGED and flagged for a future careful pass to confirm WHICH Pautz piece the article intends before correcting year/container-title. The content attribution (Pautz pressing that constitutive Russellian monism needs the same brute linking principles as dualism) is faithful to both candidate pieces, so the body claim is sound regardless.

## Citation ledger (rest real-correct, publisher-verified by subagent)
Spinoza 1677 *Ethics*; Della Rocca 2008 (Routledge); Chalmers 1996 (OUP); Atmanspacher & Rickles 2022 (Routledge); Le Bihan 2019 *Phil. Investigations* 42(2):186-201 (entry correct; in-body attribution fixed above); Gleason 1957 *J. Math. Mech.* 6(6):885-893 (dim≥3 Born-rule-uniqueness caveat in-body is faithful); Zheng & Meister 2025 *Neuron* 113(2):192-204; Tononi 2008 *Biol. Bulletin* 215(3):216-242; Fuchs 2017 *Mind and Matter* 15(2):245-300. Content claims A (Gleason/Born) and B (Pautz/Cutter instability) faithful.

## Mechanics
- Calibration clean; no possibility→probability slippage; dual-aspect monism / Russellian monism / IIT / QBism correctly distinguished as Tenet-1 foils (the Map argues against each). No cliché; no mode-label leakage; wikilinks/tenet anchors resolve. 2663 → 2699 words (soft_warning, under concepts 3500 hard). `ai_modified` + `last_deep_review` both bumped (body changed). EOF clean.

## Stability note
Citations now largely publisher-verified (Velmans/Cutter fixed, Le Bihan attribution fixed). The one open item is Pautz #6 (year/container-title — flagged above); a future pass should resolve which Pautz piece is intended before editing it.
