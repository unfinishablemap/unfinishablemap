---
ai_contribution: 100
ai_generated_date: 2026-08-22
ai_modified: 2026-08-22 21:12:19+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-22
date: &id001 2026-08-22
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-22 21:12:19+00:00
modified: *id001
related_articles: []
title: Deep Review - Mine-ness and the Ownership Void (post-coalesce fix-survival
  audit)
topics: []
---

**Date**: 2026-08-22
**Article**: [Mine-ness and the Ownership Void](/concepts/mine-ness/)
**Previous review**: [2026-07-15](/reviews/deep-review-2026-07-15-mine-ness/) (seventh pass; quote-fidelity)
**Primary lens**: FIX-SURVIVAL ACROSS THE COALESCE. `last_deep_review` was 2026-07-15; the merge that
absorbed `voids/ownership-void` landed 2026-08-06 (`cc8d260177`). The absorbed content had never been
deep-reviewed inside its new home, and `ownership-void` carried named, checkable repairs from its own
reviews of [2026-05-26](/reviews/deep-review-2026-05-26-ownership-void/) and
[2026-06-13](/reviews/deep-review-2026-06-13-ownership-void/).

## Verdict

**One real defect found, and it is the predicted shape — but it ran the opposite way to the hypothesis.**
The coalesce did not regress `ownership-void`'s fixes; every one survived. What it did was import
`ownership-void`'s **correct** text alongside `mine-ness`'s **incorrectly "fixed"** text, exposing a
false finding in the 2026-07-15 review that had until then been invisible.

## Primary lens: did the merge carry the absorbed article's fixes forward?

Every named repair from the two `ownership-void` reviews is live in the merged text. Checked individually:

| Fix | Origin | Status in merged text |
|---|---|---|
| `transition-void` → `transit-void` wikilinks (2 loci: frontmatter + Further Reading) | 2026-05-26 | **HOLDS** — L36 and L167, with the reworded gloss ("cannot witness its own state transitions") intact |
| "This is not X. It is Y." cliché removed | 2026-05-26 | **HOLDS** — L50 reads "reads it as a structural limit rather than a gap in knowledge awaiting research" (positive-claim form preserved) |
| 2026-05-29 interoceptive-void paragraph (body-as-densest-case) | verified at 2026-06-13 | **HOLDS** — L116, including the void-distinctness clause ("one concerns the appropriation relation, the other the body's opacity to awareness") |
| the `self-reference-paradox` wikilink resolves to the **live** concept page, not the archived void | 2026-06-13 | **HOLDS** — usage at L118 ("concerns logical structure") still matches the live referent. Not to be "fixed" |
| Zahavi "In being aware of a thought…" restored verbatim | 2026-07-15 | **HOLDS** — L54, full parenthetical and first-person singular intact |

Bibliography merge is clean. The pre-merge `mine-ness` list carried a self-cite to
`https://unfinishablemap.org/voids/ownership-void/`; the merge correctly **dropped** it rather than
leaving a citation to the article it had just archived. Union of the two lists minus that entry = the
12 entries now present. No duplicates, no divergent-metadata variants of the same work, no orphans.
(The brief's "32 reference entries" counts 20 Further Reading wikilinks plus 12 References.)

No archival link rot: zero live articles wikilink `ownership-void`. Inbound traffic already uses the
anchored form `mine-ness#the-ownership-void` (`voids/agency-void` L82,
`topics/vertiginous-question` L81), and the `{#the-ownership-void}` anchor is present at L106.

## Critical issue found and fixed

**Same quote asserted two ways in one article; the shorter form was the product of a false "fix".**

- L110 (imported from `ownership-void`): `for-me-ness is "completely irrelational"`
- L138 (native `mine-ness`, altered 2026-07-15): `for-me-ness as "irrelational"`

The 2026-07-15 pass had recorded as a **critical issue** that `"completely irrelational"` is not
verbatim, and reduced it. That verdict is **wrong**. Adjudicated at primary source rather than
ratified from the review record — per `quote-aggregator-ratification-corrupts-verbatim` and the
twice-flipped `tallis-misrepresentation-quote-propagation` precedent, a prior review is not evidence.

### Adjudication

`"completely irrelational"` is a contiguous verbatim span of **Parnas & Zahavi (1998),
*Journal of Consciousness Studies* 5, p. 696**, which describes "the basic self-awareness of an
experience" as *"an immediate and intrinsic self-acquaintance which is characterized by being completely
irrelational"*. Extracted by **raw grep of the NLM XML** of Frontiers in Psychology 14:1296656 (2023),
footnote 7 — page-pinned, and obtained without a confirmation prompt (per
`webfetch-confirmation-prompts-ratify-the-phrase-you-ask-about`, which would have ratified whichever
phrasing I asked about).

The 2026-07-15 reasoning was that the genuine forms are bare "irrelational" (Zahavi's list: "immediate,
implicit, irrelational, nonobjectifying, nonconceptual, and nonpropositional") and the fuller "completely
and absolutely irrelational". Both do occur — but as **different passages**. Their existence does not
falsify the p. 696 wording; the review treated it as if it did.

**Resolution**: L138 restored to `"completely irrelational"`, matching L110 and the source. +1 word.

**Root cause, and why it matters more than the edit.** The quoted string comes from a work **not in the
article's References list**. The 2026-07-15 reviewer searched the listed Zahavi works, failed to find it,
and concluded the *quote* was defective rather than that the *reference* was missing. A traceability gap
in the bibliography was misread as a fidelity defect in the body. Left alone, the 07-15 stability note
("treat these two quoted strings as verified-verbatim and not re-litigate them") would have driven a
future pass to de-quote L110 as well, destroying a correct quote. A **correction block has been appended
to `deep-review-2026-07-15-mine-ness.md`** reversing that finding and replacing the standing instruction.

## Citation web-verify ledger (§2.4)

Trigger fired: the References block changed at the merge (two lists combined). Per-cite state:

- **Parnas & Zahavi 1998** ("completely irrelational", *JCS* 5, p. 696) — **real-correct (verbatim), but
  UNLISTED in References.** Traceability gap; see Remaining Items.
- **Deane, Miller & Wilkinson 2020** ("temporally deep generative model") — **real-correct (verbatim)**.
  Never covered by any prior ledger; verified this pass by raw grep of the Frontiers NLM XML for
  10.3389/fpsyg.2020.539726: abstract reads "experiences of selfhood as emerging from a temporally deep
  generative model". Surnames Deane/Miller/Wilkinson, title, venue, article no. 539726 all confirmed.
- **Zahavi, "In being aware of a thought…"** — real-correct (verbatim); verified 2026-07-15, unchanged.
- **Billon 2023** — real-correct (verbatim); verified 2026-07-15 and 2026-05-26, unchanged.
- **Ciaunica/Charlton/Farmer 2021, Gallagher 2000, Gallagher 2012, Heidegger §9, Knappik 2022,
  Metzinger 2003, Zahavi 2005/2014, Zahavi 2014, Zahavi 2017** — real-correct; full publisher ledger at
  2026-05-26 (eight sources) plus the pre-merge `mine-ness` ledger. Entries are byte-unchanged through
  the merge; not re-verified.
- **Southgate & Oquatre-six (2026-02-09), ownership-problem** — Map self-cite, legitimate; retained.
  Per `fabricated-map-self-cite-pseudonym-false-alarm`, not to be stripped.

**Empirical-record currency sweep**: `find_superlative_claims` returns 0. Nothing to check.

**Inline ↔ References cross-reference**: the article uses name-only attribution throughout (no
`Author YYYY` inline form), so the strict orphan rule does not bite. Every References author is named in
the body. The one genuine gap is Parnas & Zahavi 1998, above.

## Secondary lens: dependency drift since the merge

Spot-checked the claims the article makes *about* moved neighbours:

- `[[many-worlds#MWI's Branch-Relative Indexicality Reply]]` — anchor present (`obsidian/concepts/many-worlds.md` L69) and the Hugo build resolves it to `/concepts/many-worlds/#mwis-branch-relative-indexicality-reply`. Note the slug is ambiguous (`archive/arguments/many-worlds.md` also exists); it resolves to the live concept page, which is correct.
- `[[self-opacity#The Special Case of Volition]]` — anchor present (L115).
- Tenet anchors `^dualism`, `^bidirectional-interaction`, `^no-many-worlds`, `^occams-limits` — all present.
- `[[self-construction-constructor]]` — the Further Reading gloss ("every construction presupposes the
  for-me feature, with the mine-ness/agency dissociation supplying its asymmetry") still matches the apex,
  which cites `mine-ness` for separable phenomenal features (L86) and states the minimal claim as "some
  experiential subject is presupposed by any construction of content" (L98). No drift.

## Calibration, reasoning-mode, attribution

No possibility/probability slippage. The void is framed as a structural limit throughout, never as an
empirical claim about an ownership mechanism. The §No Many Worlds hedge ("suggestive of, though not
decisive against") is intact — a tenet-accepting reviewer would flag nothing as overstated. Metzinger
engagement remains Mode Two (functional account granted its work, phenomenal residue named); the
physicalist framework is explicitly bracketed at L98 and L100. No editor-vocabulary label leakage. No
source/Map conflation. Knappik's plurality challenge is still addressed at the right level (L92, L114).

## Optimistic Analysis Summary

### Strengths preserved
- The double-dissociation architecture (DPD: content preserved / ownership degraded; thought insertion:
  agency lost / ownership preserved) survives the merge intact and remains the article's load-bearing
  evidence.
- The merge's structural decision — feature first, void second, joined by the "the feature arrives with a
  limit attached" hinge at L50 — reads as one article rather than two stapled together. This is a
  genuinely good coalesce.
- The affective-dissociation observation (same structural absence, terror when involuntary, equanimity
  when deliberate) is original and preserved.
- "What Mine-ness is Not" continues to do real conceptual-hygiene work.

### Enhancements made
None. Length forbade it (see below), and none were needed.

### Cross-links added
None. The network is dense and current.

## Length

Binding constraint this pass. Measured with `analyze_length`, `concepts/` thresholds **2500 soft /
3500 hard / 5000 critical**:

- Before: **3495 words** (`soft_warning`)
- After: **3496 words** (`soft_warning`) — +1, the restored "completely"
- Headroom to hard: **3 words**

This is a coalesce product sitting at its ceiling. No addition was possible and none was attempted.

## Remaining Items

1. **Parnas & Zahavi (1998) is missing from References** (P2). The article quotes it verbatim, twice, and
   a reader cannot trace the string to any listed work. This gap is what caused the 2026-07-15
   misadjudication, so closing it is preventive, not cosmetic. **Not fixed this pass, for two reasons:**
   (a) a References entry costs ~22 words and the article has 3; (b) **the byline order is genuinely
   unresolved** — OpenAlex's *JCS*-venue record gives "Josef Parnas & Dan Zahavi", while the University of
   Copenhagen repository record and the citing Frontiers article both give "Zahavi and Parnas". Crossref
   has no record (pre-DOI). Minting the entry now would trade a fixed defect for a byline defect. Needs
   the print journal, or the *Journal of Consciousness Studies* 5(5-6) front matter, to settle.
   A ~26-word condensation is available to pay for it: the falsification paragraph at L94 restates the two
   preceding subsections verbatim ("in DPD content remains while ownership fades, and in thought insertion
   agency fades while ownership remains") and can be tightened without losing the falsification condition.
2. **The body attributes a co-authored formulation to Zahavi alone** (P3). Defensible — the position is
   Zahavi's phenomenology and the literature discusses it as his — but worth revisiting when item 1 lands.
3. **`obsidian/research/voids-ownership-void-2026-02-18.md` sources the quote to the wrong work** (P2).
   L46 attributes "completely irrelational" to Zahavi's *The Experiential Self*. I downloaded that PDF and
   grepped it: the term occurs **zero** times. The research note is the propagation origin for both article
   loci, so per `research-note-self-flagged-gaps-propagate-to-the-article` it should be repointed to
   Parnas & Zahavi 1998 p. 696 — again once the byline is settled.
4. **[voids/interoceptive-void.md](/voids/interoceptive-void/) still has no back-link** to this article. Flagged as a sibling-file
   item at 2026-06-13 and still open; the forward link (L116) is present and correct. Out of scope here.

## Stability Notes

- All prior stability notes remain in force: the eliminative-materialist, functionalist and Many-Worlds
  objections are **bedrock framework-boundary disagreements**, not fixable flaws, and must not be
  re-flagged as critical. The §No Many Worlds branch-relative concession is correct calibration —
  preserve it, do not "strengthen" it into a refutation. The Buddhist *anattā* simplification is
  acceptable for scope and linked out. Canonical body term is hyphenated "mine-ness"; bibliography titles
  preserve the published "Mineness".
- **`"completely irrelational"` is verified verbatim** against Parnas & Zahavi 1998 p. 696. It has now been
  flipped once in each direction. Do not reduce it again without going to the primary text; the review
  record alone is not sufficient warrant, in either direction.
- **The general lesson for post-coalesce reviews.** The merge did not damage anything. It made a
  pre-existing defect *visible* by placing a corrected and an uncorrected copy of the same quote side by
  side. When two articles that shared source material are merged, disagreements between the halves are
  diagnostic: one of them is carrying a fix the other never got, or a "fix" the other correctly never
  applied. That diff is worth auditing explicitly, and it is not something staleness scoring can see.
- The article is converged on argument and structure. At 3 words below the hard ceiling, future
  maintenance must be net-neutral or reducing; the L94 condensation named above is the first place to buy
  room.