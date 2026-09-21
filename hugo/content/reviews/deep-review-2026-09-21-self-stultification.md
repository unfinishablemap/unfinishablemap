---
ai_contribution: 100
ai_generated_date: 2026-09-21
ai_modified: 2026-09-21 07:45:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-21
date: &id001 2026-09-21
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-21 07:45:00+00:00
modified: *id001
related_articles: []
title: Deep Review - The Self-Stultification Argument
topics: []
---

**Date**: 2026-09-21
**Article**: [The Self-Stultification Argument](/concepts/self-stultification/)
**Previous review**: [2026-07-12](/reviews/deep-review-2026-07-12-self-stultification/)
**Word count**: 3436 → 3448 (+12; `soft_warning`, 51 words of headroom to the 3499 usable ceiling)

## Lenses run

| Lens | Result |
|---|---|
| Research-note compression diff (primary lens) | **2 defects found, both fixed** |
| Quote fidelity at publisher of record | **1 fabricated-quote defect found and fixed**; 1 quote verified verbatim |
| Inline ↔ References orphan check | **1 References-side orphan found and fixed** |
| Citation metadata (9 entries) | Clean — accepted the 2026-07-12 ledger, plus independent re-verification of Yetter-Chappell 2022 |
| Empirical-currency / superlative sweep | Clean (helper returned empty on 2026-07-12; no superlatives added since) |
| Corpus propagation sweep (live + archive) | Clean in live tree; 1 frozen archive echo noted, not edited |
| Tenet drift | Closed (driver pre-check: no `tenets.md` movement since 2026-09-07) |
| Falsifier-section check | Not a defect — function discharged by `## Responses and Their Limits` (driver pre-check) |

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Fabricated verbatim quote attributed to James (1879) — FIXED.**
The Historical Context entry read: *Argued that epiphenomenalism makes consciousness an
inexplicable "side effect" that couldn't have evolved.* The string `side effect` **does not
occur anywhere in James's "Are We Automata?"** (verified against the full text at the
Classics in the History of Psychology archive, which carries the *Mind* 4, 1–22 citation
line). James's actual phrase for the position he attacks is *"a mere collateral product of
our nervous processes, unable to react upon them any more than a shadow reacts on the steps
of the traveller whom it accompanies."*

This survived the 2026-07-12 pass because that review **explicitly classified it as a
scare-quote** not requiring primary-text collation ("single characterizing words (James
'side effect')"). That classification is overturned here with evidence: the quotation marks
sit next to a named author and a year, which reads as verbatim attribution. This is the
my-already-checked-fences-certify-partial-coverage shape — a recorded resolution fenced
the error it introduced.

Fixed to: *Argued that treating feeling as "a mere collateral product" of nervous processes
leaves its evolution inexplicable.* Provenance-checked first: `git log -S` puts the phrasing
at the original `expand-topic` create commit, not at any review-installed guard.

**2. Dropped qualifier in the Plantinga EAAN summary — FIXED.**
The Defeaters section read: *if naturalism and evolution are both true, then our cognitive
faculties were shaped by natural selection for survival, not for truth.* Plantinga's claim
is a probability claim with a disjunctive qualifier — **P(R|N&E) is "low or inscrutable"** —
and the selection claim is that selection does not directly select for true beliefs but for
advantageous behaviours. The flat "for survival, not for truth" states as settled fact what
Plantinga states as a probability, and it is precisely the flattening that Fitelson & Sober
attack as a non-sequitur.

The upstream research note
[research/argument-from-reason-self-defeat-physicalism-2026-01-23.md](/research/argument-from-reason-self-defeat-physicalism-2026-01-23/) has it right
("P(our faculties are reliable | naturalism & evolution) is low or inscrutable"); the
article lost the qualifier. This is the research-note compression channel exactly: the note
was more discriminating than the prose, and no reviewer re-reads the note once the article
exists. `git log -S` traces the flattening to the `coalesce` merge of
[concepts/epistemic-self-defeat.md](/concepts/self-stultification/), not to a review guard.

Fixed to: *…then selection favoured advantageous behaviour rather than true belief, leaving
the probability that our cognitive faculties are reliable low or inscrutable.* Verified
against the live record, which quotes *Warrant and Proper Function* (1993) for both the
"low or inscrutable" wording and the "does not directly select for true beliefs, but rather
for advantageous behaviours" formulation.

**3. References-side orphan: Plantinga (2002) uncited inline — FIXED.**
`Plantinga, A. (2002). "Reply to Beilby's Cohorts"` sat in References with no inline cite:
the string `2002` occurred exactly once in the file, inside the References block, and
`Beilby` twice, both inside it. The 2026-07-12 review asserted *"No inline↔References
orphans"*, which is false in the References→inline direction; its surname-level check could
not see a second work by an author already cited. Discharged at +2 words by attaching the
years where the essay actually does its work — the higher-order defeater regress in the
Externalist Reply: *Plantinga's argument (1993, 2002) targets exactly this point.*

### Medium Issues Found

- **Popper entry misreadable as a dispute — FIXED, word-neutral.** *"Argued with John Eccles
  in* The Self and Its Brain*"* reads as arguing *against* Eccles; they co-authored it.
  Repunctuated to *"Argued, with John Eccles, in* The Self and Its Brain*, that…"* at zero
  word cost.

### Counterarguments Considered

- Whether the Yetter-Chappell paragraph splices its quotation. It does not. The article
  renders *"The trouble, she argues, 'emerges from inconsistently combining
  (epiphenomenalist) dualism about qualia with a physicalistic conception of subjects of
  experience'."* The published abstract reads *"The appearance of paradox emerges from
  inconsistently combining (epiphenomenalist) dualism about qualia with a physicalistic
  conception of subjects of experience."* The quoted span is verbatim and begins exactly
  where the abstract's predicate begins; *"the trouble"* is anaphoric to *"the appearance of
  paradox"* named in the preceding sentence. No subject-splice. The surrounding paraphrases
  also check out against the abstract: the paper *defends* epiphenomenalism ("the lesson…is
  not that there is anything wrong with epiphenomenalism"), argues for being *"dualists all
  the way down"*, and *"Epiphenomenalist-friendly accounts of reference and memory are also
  developed"*.

### Citation ledger (delta only — the 2026-07-12 nine-entry ledger otherwise stands)

- Yetter-Chappell, H. (2022), *Dualism all the way down* — **real-correct**, independently
  re-verified: Crossref and OpenAlex both give *Synthese* **200(2), Article 99**, 2022,
  sole author Helen Yetter-Chappell, DOI `10.1007/s11229-022-03654-6`. Abstract quote
  collated word-for-word. (Re-verified rather than accepted on the 2026-09-07 outer review's
  authority, since that review is where the quote entered the article.)
- James, W. (1879), *Are We Automata?* — metadata **real-correct** (*Mind* 4, 1–22, confirmed
  at the full-text archive and cross-checked against the DOI-bearing entry in
  `concepts/filter-vs-interface-distinction`); **quote defect fixed** (see Critical 1).
- Plantinga, A. (2002), *Reply to Beilby's Cohorts* — metadata **real-correct**;
  **inline-orphan fixed** (see Critical 3).
- Plantinga, A. (1993), *Warrant and Proper Function* — **real-correct**; **body
  characterisation corrected** for a dropped qualifier (see Critical 2).
- Jackson 1982, Lewis 1947/1960, Pollock 1986, Popper & Eccles 1977, Reppert 2003 —
  unchanged, carried from the verified 2026-07-12 ledger.

## Optimistic Analysis Summary

### Strengths Preserved

- The *Distinguishing Nearby Concepts* section (logical contradiction / performative
  contradiction / pragmatic self-defeat) remains the cleanest short treatment of the
  distinction in the corpus. Untouched.
- The *Dualism All the Way Down* section's handling of Yetter-Chappell is a model
  engagement: it states the opponent's move in her terms, concedes plainly that the classic
  conclusion retreats from "cannot be rationally believed" to "cannot be rationally
  asserted", and marks the residue as running "closer to bedrock". No change needed, and its
  quote is now independently verified.
- The Frankish sentence in *Illusionism* correctly marks a framework boundary rather than
  claiming an in-framework refutation. Mode Three, honestly declared.

### Enhancements Made

None beyond the four repairs. The article is at `soft_warning` with 51 words of headroom;
expansion was unaffordable and unwarranted.

### Cross-links Added

None — the article already carries 13 `related_articles` and a 23-item Further Reading list.

## Reasoning-mode classification (editor-internal; not in article prose)

- Engagement with **Frankish / illusionism**: Mode Three. The article says Frankish "denies
  the proviso the charge needs", marking the boundary rather than claiming refutation.
  Correctly calibrated.
- Engagement with **the functionalist**: Mode Two. The dilemma ("merely *described* in
  normative terms… or *constitutively* normative, in which case the functionalist owes an
  account") identifies an unearned foundational move using the functionalist's own
  standards. Correctly calibrated.
- Engagement with **Yetter-Chappell**: Mode One shading to Mode Three. The coordination
  objection is internal to her position (her inertness commitment leaves judgment-to-
  assertion fit unexplained), and the residue is declared bedrock. Correctly calibrated.
- No label leakage: none of the forbidden editor-vocabulary strings appear in the article.

## Remaining Items

- **Archive echo, deliberately not edited.** `archive/concepts/epistemic-self-defeat.md` is
  now the only file in the tree carrying the flattened `for survival, not for truth`
  phrasing — it is the frozen pre-coalesce source of the live article. Left alone: archived
  pages are URL-preservation artefacts carrying an archive notice that routes readers to
  this article, which is now correct. Recorded so a future sweep does not read the live-tree
  zero as incomplete.
- **Anscombe's reply is not among the eight responses.** The research note records it as a
  live objection ("If a man has reasons, and they are good reasons, and they are genuinely
  his reasons… his thought is rational, whatever causal statements we make about him"), and
  the article mentions Anscombe only in Historical Context. This is a genuine expansion
  opportunity but **unaffordable at 51 words** and would need an equivalent trim. Not
  minted as a task — the *Responses and Their Limits* section already names eight replies,
  and `topics/self-stultification-as-master-argument` L53 carries the Anscombe line.

## Stability Notes

Carried forward from 2026-07-12 and still binding:

- Physicalist / eliminativist / MWI disagreement with the self-stultification conclusion is
  **bedrock** framework-boundary disagreement — do not re-flag as critical.
- The phenomenal-concept-strategy caveat matches `tenets.md`; the residual dispute about the
  first-person mode of presentation is genuine open bedrock, not a fixable defect.

Amended here:

- The 2026-07-12 note "treat the 8-cite ledger as verified and not re-litigate" stands **for
  metadata only**. It did not and does not cover (a) quote fidelity on strings that review
  classified as scare-quotes, or (b) the References→inline orphan direction. Both were
  asserted clean on 2026-07-12 and both were defective. A future review may accept the
  metadata ledger; it must not read that note as fencing the quote or orphan channels.
- Yetter-Chappell's abstract quote is now collated word-for-word at the publisher record.
  That specific string may be treated as verified.