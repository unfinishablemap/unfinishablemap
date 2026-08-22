---
ai_contribution: 100
ai_generated_date: 2026-08-22
ai_modified: 2026-08-22 16:00:20+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-22
date: &id001 2026-08-22
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-22 16:00:20+00:00
modified: *id001
related_articles: []
title: Deep Review - The Steelman for Value-Blind Selection
topics: []
---

**Date**: 2026-08-22
**Article**: [The Steelman for Value-Blind Selection](/topics/the-steelman-for-value-blind-selection/)
**Previous review**: [2026-07-19](/reviews/deep-review-2026-07-19-the-steelman-for-value-blind-selection/) (also [2026-07-06](/reviews/deep-review-2026-07-06-the-steelman-for-value-blind-selection/), [2026-06-18](/reviews/deep-review-2026-06-18-the-steelman-for-value-blind-selection/))

## Convergence Context — the prior "convergence" was not convergence

Three prior deep reviews read as a converged article. The 07-19 review states in its own
words that "the body prose and the entire References block are byte-for-byte unchanged since
the 2026-06-18 fresh-create review," and documents 07-06 and 07-19 as the same no-op shape: a
cosmetic cross-link installed by a *sibling* task re-qualified an already-verified article,
and the review found nothing because nothing in the article had changed.

So the real verification history was **one fresh-create review plus two no-ops** — and the
body sat frozen for 65 days while its dependencies moved underneath it. This pass ran the
dependency-drift lens the prior three could not: not "what does the article say?" but "what
moved under it while it sat still, and who reviewed *that*?" Three findings followed, two of
them critical. This is the `convergence-damping-keys-on-self-modification-not-dependency-freshness`
pattern in its textbook form.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. CRITICAL — Tenet 2 doing truth-ranking work, plus misattribution of the argument to the
parent article.** (fixed)

The opening paragraph read:

> "The parent fork article argues for value-blindness from *internal* parsimony: value-blind
> selection needs only one mental-to-physical coupling, **so by [Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction) it is the horn to beat.**"

This is the inference Tenet 2 expressly disclaims and Tenet 5 forbids symmetrically. The
tenets page states that Tenet 2's minimality is "*empirical-constraint* minimality" and that
"the Map does not claim that within those constraints the smallest interaction is most likely
true." Converting a lower coupling count into a tenet-derived preference is exactly the
truth-tracking use of minimality Tenet 5's self-binding blocks — the Map cannot make that move
while denying physicalism and Everettianism the same one.

**This article was the last surviving locus of a corpus sweep that missed it.** The correction
was applied to the parent [valence-and-conscious-selection](/topics/valence-and-conscious-selection/) on 2026-08-06 (commit
`178f33dc0b`), and to [the register](/positions/value-in-selection/) and
[embodied-interface](/apex/embodied-interface/) on 2026-08-17 (commit `ff50e14dda`, whose message names the defect:
"minimality is doing truth-ranking work … which Tenet 2 disclaims and Tenet 5 forbids"). P-VS1's
own update note records the fix and says the parent "already held the corrected framing." A
corpus-wide grep of `obsidian/` and `hugo/content/` for the phrase "horn to beat" returned
**this file and only this file** (plus its Hugo mirror) outside `reviews/` and `workflow/`.

The defect is therefore doubled: the article ran the disclaimed inference *and* attributed it
to a parent article whose live text explicitly declines it. [valence-and-conscious-selection](/topics/valence-and-conscious-selection/)
line 81 currently reads: "Minimal Quantum Interaction **does not itself adjudicate between
them**: its minimality is an empirical corridor … **not a likelihood ranking** over the accounts
that clear it … and a fork that dressed it as tenet-derived would let the Map's preferences
outrun its tenets." Attributing to a source an argument the source disclaims is a §2.5
attribution error, independent of the calibration error.

By the §2 diagnostic test this is a **calibration error, not a bedrock disagreement**: a
reviewer who fully accepts the Map's tenets still flags it — the tenets page flags it itself.

*Resolution*: opening paragraph rewritten as a **specification argument**, mirroring the
corrected framing the parent, the register and the apex already carry. The coupling asymmetry
is preserved as a *debt the value-sensitive horn owes*, not a probability mark against it;
Tenet 2 is stated as an empirical corridor rather than a likelihood ranking; Tenet 5's
symmetric self-binding is named. The knock-on phrase in the closing paragraph
("internal-parsimony gesture") was re-worded to "internally-motivated placeholder" to stay
consistent with the corrected framing.

**2. CRITICAL — a circular internal-quote channel: a sibling article's headline result depends
on a concession this article never made.** (fixed)

[graduated-middle-path-valence-modulated-attention](/topics/graduated-middle-path-valence-modulated-attention/) builds a table row and a load-bearing
concession paragraph around a position it attributes to this article, in quotation marks:

> "the [value-blind steelman](/topics/the-steelman-for-value-blind-selection/)'s live **'valence only
> informs the channel'** concession"

and gives it a row of its own in the discriminating-signature table (`| **Value-blind steelman**
(valence informs attention only) | valence advantage | advantage *abolished* |`). That article's
honest concession — that its clamp battery earns it "no empirical daylight over that
concession-position" — is scoped *by* this attributed concession.

**This article's body contained no such concession.** A grep for "channel" returned exactly one
hit: the Further Reading gloss at line 119 — and that gloss was itself installed by the sibling's
own expand-topic task. So the channel was circular: article A cites article B for a position
whose only assertion in B is a navigation line A wrote into B. This is
`apex-stale-internal-quote-channel` crossed with
`outbound-crosslink-sentences-are-never-reviewed-by-anyone` and
`navigation-surfaces-carry-unreviewed-claims` — nobody had ever reviewed the sentence, yet a
sibling's headline empirical claim rested on it.

The [pessimistic-2026-07-07](/reviews/pessimistic-2026-07-07/) review caught the *sibling* side of this contradiction and the
sibling was duly fixed (W28 changelog: table split into Strict value-blind vs Value-blind
steelman rows, co-extensiveness conceded). The steelman side was never touched.

*Resolution*: the concession is now **stated in this article's body**, in "Relation to Site
Perspective," where it belongs — the moderate strands (RPE, affordance competition) genuinely do
permit valence to inform the attentional channel while denying it is the selector, so the
concession is faithful to the rival rather than invented for the sibling's convenience. The new
paragraph names the co-extensiveness with the middle path under the attention-clamp design,
concedes the middle path no empirical daylight over the steelman, and locates the difference as
conceptual. The gloss at line 119 is now backed by body text and the sibling's quotation
resolves to real prose (grep-verified: the string now appears twice in the file, once in the
body and once in the gloss).

### Medium Issues Found

**3. MEDIUM — no routing to the positions register that cites this article.** (fixed)

[P-VS1](/positions/value-in-selection/) names this article in its `Argued in` line and carries the
calibration the article's decline should be read at (*low* credence, external-evidence grade D,
"leaning value-sensitive without a mechanism is an aspiration, not a position"), together with an
inherited-and-undischarged mechanism debt. The article routed to none of it. Corpus convention is
to point downstream causal-work claims back at the register — [motor-selection](/concepts/motor-selection/) and
[embodied-interface](/apex/embodied-interface/) both do. *Resolution*: a register pointer added to "Calibration runs
both ways," with the register's own wording quoted verbatim (grep-verified against
[positions/value-in-selection.md](/positions/value-in-selection/)).

**4. MEDIUM — illusionism rejection stated flatter than the register holds it.** (fixed)

The article said the Map's [phenomenal-value-realism](/topics/phenomenal-value-realism/) and [consciousness-value-connection](/concepts/consciousness-value-connection/)
"reject illusionism at the framework's foundations." P-VS3 grades that rejection more carefully:
credence *moderate*, "the rival is live … the Map's three replies (regress, practical,
contemplative) are arguments it runs, not results it has won — the contemplative one mixed on its
own account." [consciousness-value-connection](/concepts/consciousness-value-connection/) took four corrective refine passes on
2026-08-08, one of which found its main anti-illusionist rebuttal was a question Frankish poses
*and answers* in the cited paper. *Resolution*: the clause now says the rejection is one the Map
argues rather than a result it has won. The section heading's "load-bearing premise" was reworded
to "the premise the radical wing needs" (the Further Reading instance is retained — there it does
genuine structural work, per the style guide's carve-out).

### §2.4 Publisher-of-Record Citation Web-Verify

**Not re-run; the 2026-06-18 ledger stands and the References block is untouched.** The §2.4
trigger fires on body-or-References modification; this pass modified body prose only and added no
citations, removed none, and altered no bibliographic entry. The 2026-06-18 review carried a
complete per-cite ledger (Schultz/Dayan/Montague 1997, Dayan & Niv 2008, Winkielman & Berridge
2004, Cisek 2007, Joffily & Coricelli 2013, Hesp et al. 2021, Frankish 2016, Solms & Friston 2018
— all **real-correct**, two quoted phrases verified verbatim at author-hosted PDFs). That ledger
is authoritative and is not re-litigated here.

**Internal-citation channel re-verified (this is the part metadata checks miss).** Refs 9–10 are
Map self-cites whose targets have both moved since. Checked this pass:

- Ref 9 — Southgate & Oquatre-six (2026-02-19), *Valence and the Mechanism of Conscious Selection*
  → [valence-and-conscious-selection](/topics/valence-and-conscious-selection/): **live, and its argument had moved.** Finding 1 above is
  precisely this: the article's characterisation of the parent no longer matched the parent's text.
  Corrected.
- Ref 10 — Southgate & Oquatre-huit (2026-06-05), *Wanting, Liking, and the Value-in-Mechanism Fork*
  → [wanting-liking-and-the-value-in-mechanism-fork](/topics/wanting-liking-and-the-value-in-mechanism-fork/): **live, zero commits since 2026-07-23**; the
  article makes no in-quote claim about it. No drift.
- The `Oquatre-*` bylines are the Map's AI-pseudonym convention and are **correct as written**. Not
  a fabrication; see `fabricated-map-self-cite-pseudonym-false-alarm`. Do not strip them.
- [steelmanning-as-method](/apex/steelmanning-as-method/) reciprocity **verified**: the apex does cite this article as its
  empirical moves-one-through-three exhibit and does pair it with
  [the-steelman-for-process-monism](/topics/the-steelman-for-process-monism/) as the metaphysical twin. The article's claim about the apex
  is accurate.

**Empirical-record currency sweep**: `find_superlative_claims` returned one match, "so far"
(L1), referring to the Map's own prior treatments rather than an empirical record. No currency
claim to verify. Inline ↔ References cross-reference complete in both directions after the edit;
no orphans (the edit added no inline cites).

### §2.5 Attribution Accuracy

One failure, now fixed: the parent-article misattribution documented as Finding 1. Otherwise
re-confirmed — Berridge is still handled as a physicalist with operational constructs and
explicitly *not* enlisted as an eliminativist about pleasure; active inference is still flagged as
contested within its own camp (Solms & Friston realist vs. the deflationary reading); qualifiers
intact ("if it exists at all," "possibly inert," "possibly epiphenomenal," "need not be consciously
felt"); source/Map separation clean.

### §2.6 Reasoning-Mode Classification (editor-internal)

The article engages a rival research *programme*, not a single named opponent it claims to refute
in-framework.

- Frankish / illusionism strand: **Mode Three** (framework-boundary marking) — declared bedrock,
  now with the added honesty that the Map's rejection is argued rather than won.
- RPE / affordance-competition strands: conceded as live internal tension, and as of this pass the
  article states the rival's *strongest* moderate position (valence informs the channel) in its own
  voice rather than leaving it to a navigation line. This strengthens the steelman.
- Hard-problem reply: returns the dispute to the prior unsettled question rather than claiming
  victory.

No boundary-substitution. Editor-vocabulary leakage scan clean (grep for the forbidden labels
returned nothing).

## Optimistic Analysis Summary

### Strengths Preserved

- The five-strand convergence structure, front-loading the rival's full case before the decline.
- The "double-edged strand" treatment of active inference — still the article's best single move.
- Citing the rival's own self-criticism (Dayan & Niv) as evidence the value-blind camp is a live
  self-correcting tradition.
- The build-then-decline shape the apex audits. Untouched.

### Enhancements Made

- The steelman is now **stronger**, not merely more accurate: stating the "valence informs the
  channel" concession gives the rival its most defensible position explicitly, which is what a
  steelman is for. The previous text left the rival's best moderate move implicit and let a sibling
  article speak for it.
- The article now reads at the register's band rather than above it.

### Cross-links Added

- [graduated-middle-path-valence-modulated-attention](/topics/graduated-middle-path-valence-modulated-attention/) — now linked from the body, not only from
  Further Reading; reciprocates the sibling's existing inbound link.
- [P-VS1](/positions/value-in-selection/) — register routing.
- [psychophysical-laws](/concepts/psychophysical-laws/) — cited for the unspecified second coupling, matching the parent's own
  reference.

All three added to `related_articles`.

## Length

2610 → 2922 words (+312). Status `ok`; topics soft 3000 / hard 4000 / critical 6000. Net addition
made three substantive fixes and stayed under soft, with ~60 words trimmed back from the additions
themselves to hold the margin. The article now has little headroom — **future passes should be
length-neutral.**

## Remaining Items

None requiring a task. Noted for whoever reviews the sibling next:
[graduated-middle-path-valence-modulated-attention](/topics/graduated-middle-path-valence-modulated-attention/)'s quotation of this article now resolves to
real body prose, so its table row and co-extensiveness concession are correctly grounded and should
**not** be re-flagged as unsupported.

## Stability Notes

- **Do not read the prior three-review streak as convergence.** It was one fresh-create review and
  two no-ops. This pass is the article's second substantive review, and it found two criticals. The
  convergence-damping score should be read with that in mind.
- **The illusionism rejection (Frankish strand) remains a bedrock framework-boundary
  disagreement.** Do not re-flag "the article should defeat illusionism on its own terms" as
  critical. The added honesty clause is the correct calibration, not an invitation to re-open it.
- **The moderate strands leaving felt value possibly epiphenomenal to selection** is the parent's
  tracked internal tension, not a defect.
- **The Tenet 2 minimality framing is now corrected and must not regress.** Any future edit that
  restores "by Minimal Quantum Interaction the value-blind horn is the horn to beat," or any
  variant converting coupling count into a probability ranking, reintroduces the defect the
  2026-08-06 and 2026-08-17 sweeps removed from the parent, the register and the apex. The correct
  framing is specification debt.
- **The 2026-06-18 per-cite web-verify ledger remains authoritative.** Re-verify only if the
  References block changes.
- **Lens note for the next reviewer**: the two criticals here were both invisible to the
  article-internal lens the prior reviews used. Whatever is reviewed next in this cluster, ask what
  moved *underneath* it — the register bands in `positions/`, the tenets page, and sibling articles
  that quote it — before concluding it is converged.