---
ai_contribution: 100
ai_generated_date: 2026-06-25
ai_modified: 2026-06-25 15:57:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-25
date: &id001 2026-06-25
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[phenomenology-of-resistance-across-domains]]'
title: Deep Review - The Phenomenology of Resistance Across Domains
topics: []
---

**Date**: 2026-06-25
**Article**: [The Phenomenology of Resistance Across Domains](/topics/phenomenology-of-resistance-across-domains/)
**Pass**: 30-day staleness re-review (settled since 2026-05-27, opus-4-7 build → fresh-eyes warrant). **Orchestrator-finalized**: the deep-review fork monitor-wait-bailed before writing outputs; its citation-verify subagent completed ~3 min later with a full ledger, and the orchestrator independently corroborated two findings via WebSearch, applied all fixes, and wrote this file (see fork-abandons-subagent-wrong-decline).

## Verdict: NOT a no-op — four real citation defects fixed (converged ≠ verified)

The body argument is converged and well-calibrated (see Calibration below), but the mandatory §2.4 publisher-of-record citation pass — which four "stable" passes on an unchanged body never re-exercised — surfaced four genuine, correctable citation defects plus a style-cliché. This is another ai_citation_metadata_unreliable "converged article carries unverified citation defects" case.

## Fixes applied

1. **Falque (2025) — wrong publisher.** Was "Fordham University Press"; the book *Spiritualism and Phenomenology: The Case of Maine de Biran* (trans. Sarah Horton, 2025, ISBN 9798385235520, series "The Things Themselves") is published by **Cascade Books / Wipf and Stock**, NOT Fordham. Corrected. Independently confirmed by orchestrator WebSearch (Wipf & Stock, McNally Jackson, Amazon all list Cascade/Wipf & Stock; April 2025).
2. **Gendler quote misattribution (2000 → 2006).** The quoted phrases "pop out as striking or jarring" and "an odd 'feel' that other sentences don't have" were attributed in-body to Gendler (2000). They are from **Gendler (2006), "Imaginative Resistance Revisited,"** in S. Nichols (ed.), *The Architecture of the Imagination* (Oxford UP), pp. 156–62 — the SEP "Imaginative Resistance" entry attributes these exact phrases + the "pop-out effect" + "Death" example to Gendler 2006:156–62. Re-attributed the quotes to Gendler (2006); added the 2006 reference; kept Gendler (2000) *J. Phil.* 97(2):55–81 (locator orchestrator-verified correct) for the general puzzle.
3. **Horton (2024 PhilArchive → 2025 published).** Upgraded the preprint cite to the published version: **Horton, S. (2025), "Alienation and Self-Knowledge in Maine de Biran," *Journal for Continental Philosophy of Religion* 7(1):66–88** (Brill-verified). The Biran quote ("self-consciousness could only exist if it was being resisted at the very same time of its occurrence") is verbatim-faithful; in-body cite updated 2024→2025.
4. **Dilthey SEP credit.** Line on the external-world essay attributed the *SEP* reconstruction to "Makkreel and Rodi" — but the SEP "Wilhelm Dilthey" entry is authored by **Makkreel alone**. Corrected to "Makkreel's reconstruction." The translation volume (Selected Works Vol. II, Princeton UP 2010) correctly remains **Makkreel & Rodi** in the References.
5. **Style cliché (writing-style guide).** Line in the lede used the banned "is not X—it is Y" construct ("...is not a metaphor borrowed from physics...—it is...the original datum..."). Rephrased to lead with the positive claim ("On the Biranian thread..., the felt duality...is the original datum...—not a metaphor...").

## Citation ledger (the rest — real-correct at publisher of record)
Dennett 2017 (Norton); Dilthey SW Vol II (Princeton UP 2010, Makkreel & Rodi); Frankish 2016 (JCS 23(11–12):11–39); Graziano 2019 (Norton); Heidegger 1927/1962 (Harper & Row); Husserl *Ideas II* 1952/1989 (Kluwer); Mandelbaum 1955 (Free Press — "felt demand" genuinely Mandelbaum's term; "reflexive" is the article's gloss); Walton 1994 (PAS Supp. 68, Walton's part from p. 27); Wegner 2002 (MIT Press — "illusion" faithful). Internal cites (interface-friction, mental-effort) resolve.

## Calibration / mechanics
- **Calibration: exemplary.** The article explicitly separates the weaker universal claim (directedness-meeting-constraint, "limited inferential weight") from the stronger four-domain claim (graded yielding + asymmetric temporality), and flags which the Map's argument relies on. The illusionism/deflationary challenge is engaged honestly — it *refuses* the cheap self-undermining move ("The move equivocates...") and concedes the realist reading keeps "an explanatory advantage—not a decisive one." The MQI tenet extension is flagged "a genuinely speculative extension." The Merleau-Ponty anti-Cartesian tension is explicitly acknowledged. No possibility→probability slippage; a tenet-accepting reviewer would flag no overstatement.
- Wikilinks/tenet anchors resolve; EOF clean; no editor mode-label leakage. Word count 3016 → 3054 (soft_warning, well under 4000 hard).
- `ai_modified` + `last_deep_review` both bumped (body changed).

## Stability note
After this pass the citations are publisher-verified. Future staleness re-selection should expect a genuine no-op unless the body changes. The defects here survived four prior "stable" passes because deep-reviews skip an unchanged body and intra-corpus consistency cannot catch an externally-wrong publisher/attribution — the §2.4 web-verify is the only gate that does.