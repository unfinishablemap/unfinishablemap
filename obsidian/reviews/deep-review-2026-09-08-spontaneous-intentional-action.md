---
title: "Deep Review - Spontaneous Intentional Action"
created: 2026-09-08
modified: 2026-09-08
human_modified:
ai_modified: 2026-09-08T16:27:27+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-08
last_curated:
---

**Date**: 2026-09-08
**Article**: [[spontaneous-intentional-action|Spontaneous Intentional Action]]
**Previous review**: [[deep-review-2026-07-06-spontaneous-intentional-action|2026-07-06]]
**Trigger**: Scheduled rotation, rank 2 / 375, score 45.7, 64 days since last review. Seventh review.
**Word count**: 2434 → 2497 (+63; soft 2500, hard 3500; status `ok` before and after)

## Headline: six prior "clean" reviews ratified a Tenet 5 violation

The six previous passes (2026-02-17, 03-20, 03-21, 04-27, 06-01, 07-06) all reported
*no critical issues*, the last three explicitly recommending the article be held out of
rotation as "fully converged". This pass found **three critical defects**, two of them in
prose those six reviews read and passed. The convergence recommendation was wrong, and the
reason is instructive: each prior review checked link integrity, attribution and slippage
against *the article's own vocabulary*, and the article never used the word "parsimony" at
the offending locus — it said "simpler". Intra-corpus and intra-article consistency
ratified the defect rather than catching it.

## Pessimistic Analysis Summary

### Critical Issues Found

**C1. Offensive parsimony appeal, forbidden by Tenet 5's own "Rules out" clause (§Relation, Bidirectional Interaction).**
The paragraph closed: *"The Map's framework provides a **simpler explanation**: consciousness
selects, and sometimes selects immediately."* Three independent authorities converge against it:

1. `tenets/tenets.md` **Rules out** clause: *"…and—internally—any Map argument that leans on
   parsimony as if this tenet did not apply to it."*
2. Tenet 5 **Application to the Map's own arguments**: *"The discipline is symmetric:
   parsimony cannot decide for or against a framework when the relevant knowledge is
   incomplete."*
3. The tenet-inheritance matrix records anti-parsimony as **Defensive** for the Agency row
   (`[[topics/free-will]]`, `[[agent-causation]]`, `[[concepts/moral-responsibility]]`) — this
   article's cluster. The matrix's own "hidden-inheritance failures" list names the exact
   pattern: *"**Parsimony asymmetry**: an article invokes parsimony defensively in one
   direction while letting Tenet 5's self-binding lapse in the other."* That is precisely
   this article — defensive and correct in its Tenet 5 paragraph, lapsed and offensive two
   paragraphs earlier.

This is a calibration error, not a bedrock disagreement: a reviewer who fully accepts the
Map's tenets flags it, because Tenet 5 *is* one of the tenets. **Fixed.** The replacement
states the Map's advantage as explanatory directness and cites the self-binding explicitly:
*"This is explanatory directness rather than simplicity; by Tenet 5 the Map may no more argue
from parsimony in its own favour than its critics may argue from parsimony against it."*

**The Tenet 5 paragraph itself was NOT touched** — verified. Its parsimony use is the
permitted *defensive* one (rebutting the materialist's simplicity argument *against* the Map:
"the apparent simplicity of the neural-only account hides real costs"). Confirmed byte-identical
in the diff.

**C2. Strawman of epiphenomenalism — the "coincidence" charge begs the question (same paragraph).**
The article argued that an epiphenomenal consciousness *"would require the unconscious brain
to generate precisely the actions that consciousness would endorse, every time, **by
coincidence**"*, concluding that spontaneous actions *"would be impossible as described"*.

**Verdict on the driver's question: yes, this begs the question**, and decisively.
Epiphenomenalism holds that the physical determines the mental. The very same neural process
that produces the action produces the endorsement-experience — so the match is *common
causation*, not coincidence. There is no independent variable left over to be coincidentally
aligned. The argument only works against a position nobody holds (parallelism with no
explanation of the parallel), and "would be impossible as described" claims a refutation the
argument has not earned inside the opponent's framework. Per §2 a strawman is critical
regardless of severity elsewhere. **Fixed** by conceding the common-cause reply outright and
relocating the burden to where it actually survives: *why* the phenomenology of authorship
attaches to exactly the contextually apt, novel actions and not to reflexes or tics — a
distribution the brain-only account must derive rather than assume. That is a genuine
explanatory debt rather than a charge of coincidence.

Note the article already contains the *valid* version of this move, in the Wegner passage:
authorship phenomenology is strongest where deliberation is absent, the opposite of what
confabulation predicts. That one is an empirical prediction mismatch and stands untouched.

**C3. Coinage misattribution to James, verified against the primary text (§Contemplative Perspectives).**
The article read *"what James (1890) called the "ideo-motor" readiness of the whole self"*.
James does use "ideo-motor action" (10 occurrences, *Principles of Psychology* vol. 2, ch. XXVI
"Will"), but he explicitly disclaims the coinage:

> "Dr. Carpenter, who first used, I believe, the name of ideo-motor action, placed it, if I
> mistake not, among the curiosities of our mental life."

Separately, *"readiness of the whole self"* is not James's concept and not in his text — it is
the Map's gloss, presented inside a "what James called" attribution. Source/Map conflation.

**Fixed**, and the fix strengthens the article: James's actual doctrine is a *better* fit for
the thesis than the vague gloss was. Ideo-motor action is movement following the bare idea of
it with no separate fiat of will intervening — which is Searle's intention-in-action without a
prior intention, reached independently. The new text credits Carpenter and quotes James
verbatim.

**Method (per the false-negative discipline)**: pulled the raw Gutenberg text of *Principles*
vol. 2 (ebook 57634, 1,704,117 bytes) and grepped in Python, printing offsets. Raw offsets —
"ideo-motor" ×10, first body occurrence 1234892; quoted phrase 1235060. My first search for the
Carpenter sentence returned **−1**, a false absence caused by a line break inside the phrase in
the raw file; re-running on whitespace-normalised text located it at offset 1221567, with the
quoted phrase at 1221186. Reporting that −1 would have manufactured a claim that James never
credited Carpenter. Both strings confirmed present.

### Publisher-of-Record Citation Ledger (§2.4)

Trigger met (8 References entries, inline `Author YYYY` cites, and the block had not been
web-verified in any prior pass — the 06-01 and 07-06 reviews invoked the "unchanged since last
review" skip, which means the block has never actually been checked at a publisher).

All 8 inline↔References cross-references resolve; no orphans in either direction. Bergson and
Merleau-Ponty are named inline without a year, which the entries legitimately support.

- **Bergson 1889**, *Time and Free Will* — state: **real-wrong-metadata**. English title dated
  to the 1889 French original (*Essai sur les données immédiates de la conscience*) with no
  publisher or translation marker. Family-resolved to the corpus's dominant and
  previously-certified form: `(1889/2001) … Dover.`
- **Dreyfus 2002**, *Intelligence without representation* — state: **real-correct**. Crossref
  DOI 10.1023/a:1021351606209: Dreyfus, Hubert L.; *Phenomenology and the Cognitive Sciences*;
  vol 1, issue 4, pp. 367–383; issued 2002-12. Article matches on every field. (Crossref carries
  a subtitle, "The relevance of phenomenology to scientific explanation", which the article
  omits — acceptable short form, not a defect.)
- **James 1890**, *The Principles of Psychology*, Henry Holt — state: **real-correct** as
  metadata; the *use* was defective (C3).
- **Lutz, Slagter, Dunne & Davidson 2008** — state: **real-correct**. Crossref DOI
  10.1016/j.tics.2008.01.005: all four authors in the cited order, *Trends in Cognitive
  Sciences* 12(4) 163–169, issued 2008-04. Exact match on every field.
- **Merleau-Ponty 1945** — state: **real-wrong-metadata**. The article paired the *English*
  title with **Gallimard**, which published the *French* original. Gallimard 1945 =
  *Phénoménologie de la perception*; the English text is Routledge (Smith 1962 / Landes 2012).
  Family-resolved to the corpus's dominant form (13 instances, one previously certified
  real-correct): `(1945/2012). *Phenomenology of Perception*. Trans. D. A. Landes. Routledge.`
- **Searle 1983**, *Intentionality*, CUP — state: **real-correct**. Also checked the *use*: the
  intention-in-action / prior-intention distinction is stated faithfully.
- **Suzuki 1959**, *Zen and Japanese Culture* — state: **real-wrong-metadata**. The 1959 first
  edition was **Pantheon Books** (Bollingen Series LXIV, 478 pp., Paul Rand cover); Princeton
  University Press editions follow its 1967 acquisition of the Bollingen Series (1970 paperback,
  2010 reissue). "1959 … Princeton University Press" pairs a year with the wrong publisher.
  Corrected to `Bollingen Series LXIV. Pantheon Books.` **This article is the corpus's only
  instance of this citation**, so no family to propagate to; the corrected form is now canonical.
- **Wegner 2002**, *The Illusion of Conscious Will*, MIT Press — state: **real-correct**. Use is
  also correct: presented as the *target* of a counterexample, not endorsed.

**Empirical-record currency sweep**: `find_superlative_claims` returns **0** — no superlative
claims to age-check. Contra the driver's suggestion, no currency defect exists here. The article
reports Wegner's and Libet's theses without claiming either is the current state of the field,
and routes detail to `[[libet-experiments]]`. The 18-year-old newest citation is not itself a
defect: five of eight entries are canonical primary texts where the original date is the point.

### Reasoning-Mode Classification (§2.6)

- **Hard determinist** (§Against Hard Determinism): **Mode One** — argues on the determinist's own
  terms, forcing a disjunction (deny intentionality, or explain authored novelty without
  authoring). Unchanged, sound.
- **Libet / Wegner**: **Mode One** — turns the confabulation thesis against itself. Unchanged, sound.
- **Pure-deliberation theorist** (§Against Pure Deliberation Models): **Mode One** — internal
  reductio; if freedom requires deliberation, jazz improvisation is unfree, which the opponent
  does not want. Unchanged, sound.
- **Epiphenomenalist** (§Relation): was **boundary substitution dressed as refutation**; now
  **Mixed (Mode Two → Mode Three)** — identifies an unmet explanatory burden the opponent's own
  standards recognise, then declines to claim refutation. See C2.
- **Label leakage**: none. No editor-vocabulary term appears anywhere in article prose (checked
  the full forbidden list). The new prose introduces none.

### Medium / Low Issues Addressed

- **"exactly what "minimal" predicts"** (§Relation, Minimal Quantum Interaction) treated Tenet 2's
  minimality as a graded *predictor*. `tenets.md` is explicit that Tenet 2's minimality is
  *empirical-constraint* minimality, not truth-tracking: it fixes a corridor, it does not predict
  that easier selections use less interaction. Rephrased to "sits comfortably within the empirical
  corridor Tenet 2 fixes", which is both accurate and shorter.
- **"which confirms that spontaneous action remains under conscious governance"** — preserved veto
  capacity is evidence of, not confirmation of, conscious governance. "confirms" → "indicates".
- **"they are clearly not mere neural automatisms"** — "clearly" mildly begs the question at issue.
  Cut.
- **"contextually perfect response"** → "contextually apt" (de-overclaim, in the rewritten James
  sentence).
- **Heading precision**: "Against Determinism" → "**Against Hard Determinism**". The body's first
  words are "Hard determinists typically argue", and the argument does not touch compatibilist
  determinists. Under LLM-first truncation resilience the heading is what a truncating reader
  keeps, so it should carry the accurate scope. Verified safe: `grep` for
  `spontaneous-intentional-action#` across the whole repo returns **zero** anchor references to
  any heading in this article, so no cross-reference breaks.

### Length-Neutral Offsets

The article was 66 words below soft, and the C1–C3 fixes add net prose. Rather than cross the soft
threshold I offset them against genuine redundancy — the article stated its central thesis
("effort tracks difficulty, not presence, of selection") **four** times:

- Cut "Easy selection feels effortless but is still selection." — fully entailed by the preceding
  sentence.
- Cut the Minimal Quantum Interaction paragraph's closing "The mechanism is the same; only the
  difficulty varies." — verbatim restatement of the §For the Selection Framework close.
- Shortened the `[[mental-effort]]` Further Reading gloss, which restated it a fourth time.
- Merged the three-sentence No Many Worlds paragraph into one; cut the fourth restatement of the
  definitional quartet in §Spontaneity and Creativity; trimmed two mildly redundant clauses
  (Dreyfus, authenticity).

Trajectory: 2434 → 2526 (over soft) → 2497 (`ok`). No wikilink target was removed anywhere; every
Further Reading and body link present before is present after. `scripts/validate.py` passes.

### Counterarguments Considered

- The six adversarial personas' framework-boundary positions (eliminativist, physicalist, MWI,
  Buddhist no-self) remain bedrock standoffs documented across six prior reviews. **Not re-flagged**
  — see [[bedrock-clash-vs-absorption]].
- The **epiphenomenalist** objection is the one that was *not* bedrock and was being mishandled as
  though a strawman disposed of it. Now engaged honestly (C2).

## Optimistic Analysis Summary

### Strengths Preserved (untouched)

Opening three concrete examples and front-loaded definition; the four-fold negative definition
(not habitual / deliberate / reflexive / accidental); the four-component volitional framework with
its veto-preservation argument; the Bergson *durée* depth passage ("intelligent because it is
*deep*"); the Zen *mushin* / Daoist *wu wei* cross-traditional material; the "What Would Challenge
This View?" falsifiability section; all five tenet connections; the Wegner counterexample, which is
the article's single best argumentative move.

### Enhancements Made

- The epiphenomenalist engagement is now a real argument instead of a strawman, and is stronger for
  conceding the common-cause reply first.
- The James material now carries his actual doctrine (no fiat between idea and movement) and links
  it explicitly back to the Searle distinction the article opens with — a spine the article
  previously left implicit.
- Tenet 5's self-binding is now stated in the section that was violating it, making the article
  self-policing at the point of maximum temptation.

### Cross-links Added

None new. One internal reference added (`[[tenets#^occams-limits|Tenet 5]]` inside the
Bidirectional Interaction paragraph) — target and anchor already in use elsewhere in the article.

## Where the Driver's Brief Was Wrong

Recorded because two of its four framings would have produced bad edits:

1. **"House style bans the 'not X but Y' family"** — overstated. The style guide bans *"This is not
   X. It is Y."*, the negation-then-**correction** construct. "not just functional but experiential"
   is concessive-**additive**: it affirms functionality and adds experience, replacing nothing. The
   same guide section also says explicitly, *"This is a guide for future writing — there is no need
   to sweep existing uses out of the corpus."* **No change made.**
2. **"§Relation has five paragraphs and not one self-limits" — presented as a defect in itself.** The
   zero-hit measurement is correct (independently reproduced: all six markers at offset −1). The
   *inference* does not hold. Only **44 of 307** concepts articles with a §Relation section carry any
   such marker (14%), so this is a minority practice, not a house convention. More decisively, the
   tenet matrix says a section should mark itself as coherence commentary when it covers a **not
   invoked** cell — and for the Agency row *no cell is "not invoked"*; the tenets this article draws
   on are **Required**, where the stated obligation is to "locally re-derive or explicitly cite the
   dependency", which it does via `[[tenets#^...]]` anchors. I added calibration at the **one** place
   the matrix does constrain — the Defensive parsimony cell — rather than padding five paragraphs.
3. **"L130 'cannot capture' is a modal over-claim"** — declined. That sentence states Tenet 1's
   content applied to this case. By the §2 diagnostic test, a tenet-accepting reviewer does *not*
   flag it, because irreducibility is the tenet they accept. This is bedrock, and rewriting it would
   be the oscillation the skill warns against.
4. **Currency** — the driver flagged Wegner 2002 and Lutz 2008 as legs that "could genuinely have
   moved". The superlative helper returns 0 and neither claim is framed as current-state-of-field, so
   there is nothing to re-scope. The driver was right to warn that median-year is a false signal here;
   the conclusion is that there is no currency defect at all, not that a narrower one exists.

The driver was **right**, and valuably so, on: the L132 parsimony contradiction (the session's most
important find, and correct in every particular including which paragraph *not* to touch); the
coincidence argument being worth grading (it does beg the question); flagging quote fidelity as
never-run on a James-citing article (it yielded C3); the arithmetic warning about not
double-subtracting frontmatter; and the instruction not to calibrate effort to how tidy the file
looks — six clean reviews had made this file look finished.

## Remaining Items

- **Heading-vs-body over-claim question: answered NO.** Checked each of the three §Why the Category
  Matters headings against its body. "Against Hard Determinism" ends in a burden-shifting disjunction;
  "Against Pure Deliberation Models" runs an internal reductio and genuinely is against
  pure-deliberation models; "For the Selection Framework" is supported by "handles this naturally",
  which is explanatory fit and correctly hedged. These are ordinary argumentative signposts whose
  bodies do not exceed them. **No change beyond the "Hard" scope fix.** Deliberately not touched — a
  reviewer looking for over-claim here would be inventing one.
- Long-deferred expansion items (developmental angle, somatic markers, Gallagher/Zahavi
  agency/ownership distinction) remain low priority and length-blocked. Not actionable.

## Stability Notes

- **The "fully converged, hold out of rotation" recommendation carried by the 06-01 and 07-06 reviews
  should not be honoured, and its reasoning should be distrusted generally.** Three criticals sat in
  this article across six passes that each concluded there were none. Clean-streak length is not
  evidence of correctness; two of the three defects were invisible to every check those reviews ran,
  because they were defects of *reasoning* and *external fact* rather than of links, timestamps or
  internal consistency — and the article's internal consistency actively concealed C1.
- **Generalisable lever**: C1 was findable only by reading the article's claim against
  `tenets.md`'s "Rules out" clause and the inheritance matrix's Defensive/Required cell, and the
  article never used the trigger word "parsimony" at the offending locus. Any Agency-cluster article
  asserting its own account is "simpler", "more economical", "more natural" or "avoids needless
  posits" is a candidate for the same defect, and grepping for "parsimony" will not find it. Suggested
  sweep terms: `simpler explanation`, `more economical`, `needless`, `unnecessary posit`.
- **Bedrock, do NOT re-flag**: eliminativist, physicalist, MWI-defender and Buddhist no-self
  disagreements; the Tenet 1 irreducibility claim at §Relation/Dualism; the "not just functional but
  experiential" phrasing (style guide explicitly does not require retro-sweeping).
- **Do NOT re-litigate**: the three §Why the Category Matters headings (checked, sound); the Tenet 5
  paragraph's defensive parsimony use (correct as written — a future reviewer seeing "parsimony" there
  should read to the end of the paragraph before acting).
- The eight-entry References block has now been web-verified at the publisher of record for the first
  time; three of eight carried metadata defects. The per-cite ledger above is the record — future
  reviews may rely on it while the block is unmodified.
