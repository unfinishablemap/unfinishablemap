---
ai_contribution: 100
ai_generated_date: 2026-09-20
ai_modified: 2026-09-20 23:49:37+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-20
date: &id001 2026-09-20
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-20 23:49:37+00:00
modified: *id001
related_articles: []
title: Deep Review - Parfit's Reductionism
topics: []
---

**Date**: 2026-09-20
**Article**: [Parfit's Reductionism](/concepts/parfit-reductionism/)
**Previous review**: [2026-06-05](/reviews/deep-review-2026-06-05-parfit-reductionism/) (plus an unarchived 2026-07-12 owed-web-verify pass, commit `f7a74aaa7a`)

## Lenses run in this pass

1. **Source-of-record check on the two post-07-12 insertions** — both were installed by refine-draft passes aimed at *other* files and had never been examined by any review of this article (the secondary-host pattern).
2. **Falsifier discrimination audit** — does each surviving item in *What Would Challenge This View?* actually discriminate, and were the two conditions dropped by the 2026-04-12 condensation load-bearing?

Lenses deliberately **not** re-run: reference-existence / publisher-of-record verification (settled 2026-06-05, all 7 entries; publisher re-settled corpus-wide 2026-08-19 via Crossref), the fabricated-Parfit-quote check (settled 2026-05-26), the Lockwood L67 quote (settled 2026-07-12).

### What the seven prior passes covered

| Pass | Scope | Outcome |
|---|---|---|
| 2026-01-20 | First deep review, generic six/seven-persona | Baseline |
| 2026-02-01 | + Attribution Accuracy Check | Minor fixes |
| 2026-03-11 | + Attribution Accuracy Check | Minor fixes |
| 2026-04-12 | Full pass on the ~3497-word article | Declared **converged** — then condensed to 1985 words ten hours later (`a2dfca14fb`) |
| 2026-05-26 | First pass on the *condensed* text | Found and removed a **fabricated direct Parfit quotation** on death |
| 2026-06-05 | Full publisher-of-record citation audit (all 7 refs) + Tallis-2016 phantom-removal verification | No critical issues; ledger recorded |
| 2026-07-12 | Owed-web-verify, single attributed **Lockwood** quote at L67 | Discharged |

Neither of the two edits that landed after 2026-07-12 had been reviewed by anything until this pass.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Falsifier 3 could not discriminate — a qualifier dropped by the condensation.** `What Would Challenge This View?` item 3 read:

> **Teleportation with subjective continuity** — a replica reporting no experiential discontinuity, supporting anti-haecceitism.

The Map's own account entails that observation. §Causal History says the replica may be "psychologically identical"; §The Practical Stakes says "the replica would be a numerically distinct consciousness" who nonetheless has what Parfit calls Relation R. A psychologically continuous replica reports no gap **whether or not** haecceitism holds, so the report sits equally well on both hypotheses and tests neither.

The pre-condensation version carried the hedge that made this explicit — *"Though such reports couldn't definitively settle whether the original subject survived"* — and commit `a2dfca14fb` cut the hedge while keeping the item. A dropped qualifier that changes meaning, leaving a decorative falsifier in a section whose whole point is discrimination.

- **Resolution applied**: item 3 replaced (see below), and the teleportation candidate named explicitly as omitted with the reason, following the discipline stated at `concepts/episodic-memory` L166. Naming a falsifier one's own position entails would be decorative.

**2. The 2026-04-12 condensation stranded the contemplative concession.** The falsifier set went 5 → 3 in `a2dfca14fb`. Audited both drops:

- **Dropped #5, "Process without prehensive particularity"** — correct and clean. It falsified the Whitehead/Process Philosophy section, which the same commit removed. Nothing strands.
- **Dropped #4, "Contemplative dissolution of witness"** — **stranded**. Its host claim survives verbatim at §The Illusionist Challenge ("Whether this reading is correct is genuinely open"), and the pre-condensation text pointed at it by name: *"the Map treats it as genuinely open (see criterion 4 in 'What Would Challenge This View?')"*. The condensation replaced that pointer with `(see [[buddhism-and-dualism]])` and deleted the criterion, so the article kept conceding that its reading of contemplative reports is open while deleting the statement of what would settle it.
- **Provenance check** (`git log -S` on both dropped conditions): each was installed by the article's originating commit `b883856b43`, not by a later review. Neither was review-installed repair text — so the restoration below rests on the stranding, not on provenance.

- **Resolution applied**: criterion 4 restored as item 3, in condensed form, with the reciprocal pointer reinstated at §The Illusionist Challenge.

### Medium Issues Found

**3. The illusionist-regress cite pointed at a work that does not discuss illusionism.** L95 (installed 2026-08-03 by `6ff3dd4e6a`, a locus fix copied from `concepts/haecceity`) read "The standard reply is Tallis's regress (2011)" inside a paragraph whose target is Frankish's illusionism, with *Aping Mankind* (2011) as the only Tallis reference. Two independent extractions (below) confirm the book contains the general argument but never engages illusionism, which Tallis addresses directly only in 2024.

- **Resolution applied**: the year moved out of the bare cite and into a sentence that separates the two works — "Tallis develops the argument against neural reductionism in *Aping Mankind* (2011) and presses it against Frankish's illusionism directly in 2024" — and the verified 2024 entry added to References alongside the 2011 book. Additive; the 2011 reference is untouched. Carrying both Tallis works is existing corpus practice (`concepts/semantic-memory`, `concepts/witness-consciousness`, `topics/consciousness-in-simple-organisms`).

### Verdict on the Tallis attribution — two independent extractions

**Extraction A — primary source, *Philosophy Now* 161 (2024), raw HTML, tags stripped to nothing, NFKC-normalised, Python grep (not a summariser).** The regress is verbatim in the 2024 article, and it names Frankish and his 2016 *JCS* paper as its target:

> "If matter can't generate experiences, it seems even less capable of creating the illusions of experiences, since misrepresentation presupposes presentation. Presentation is a relationship between an entity (an object, an event, or a process), and a subject conscious of that entity. […] Similarly, all illusions presuppose experience."

> "The most lucid and committed among them is Keith Frankish, who embraces 'strong illusionism'. According to Frankish, "phenomenal consciousness, as usually conceived, is illusory" ('Illusionism as a Theory of Consciousness', Journal of Consciousness Studies, Vol.23, 2016)."

Span verified: the whole of the first passage, contiguous. `Aping` occurs **0** times in the 2024 article — Tallis does not point readers back to the book for this argument.

**Extraction B — inside the 2011 book, Google Books `jscmd=SearchWithinVolume2`, volume `wk37CwAAQBAJ` (Routledge ebook of *Aping Mankind*).** Quoted-phrase mode verified as genuine phrase matching before use:

| Probe | Hits | Role |
|---|---|---|
| `"castle built on sand"` | 10 | positive control (chapter title) |
| `"Dennett"` | 9 | positive control |
| `"representation"` | 9 | positive control |
| `"purple hippopotamus dancing"` | 0 | negative control |
| `"way certain a seem"` / `"certain seem way a"` | 0 | **scramble control — confirms phrase (not OR) matching** |
| `"seem a certain way"` | **9** | the article's own idiom, present in the book |
| `"re-presentation"` | **2** | supports the `concepts/attention-schema-theory` L107 rendering |
| `"Frankish"` | **0** | book does not engage illusionism-as-Frankish |
| `"presupposes presentation"` | 0 | the 2024 epigram is *not* in the book |
| `"illusions presuppose experience"` | 0 | likewise |
| `"consciousness is an illusion"` / `"the illusion of consciousness"` | 0 | |

**Verdict.** The attribution is **sound at the argument level and correctly pointed at 2011** — *Aping Mankind* does run the appearance/re-presentation regress, and the "seem a certain way" phrasing is the book's own. The metadata tuple is independently confirmed: Crossref `10.1017/upo9781844652747`, monograph, **Acumen Publishing Limited**, issued **2011-06-30**; OpenLibrary and the *Isis* review both give Acumen, Durham UK, 2011. The corpus `Acumen` form is right (34 live, 0 stragglers). What was **wrong** is narrower than "is it Tallis's?": the paragraph presented the 2011 book as the source of the *standard reply to illusionism*, a debate the book predates by five years and never joins. Fixed by naming both works.

This did **not** flip the prior verdict; it sharpened it. Note that the 2026-09-01 `temporal-structure-of-understanding` ledger certified this same tuple as "real-correct … **following the settled 2026-08 illusionist-regress family template at `concepts/haecceity`**" — ratification by template, which certifies the metadata and not the work-level fit. That is the mechanism this pass caught.

### Other post-07-12 insertion checks

- **`bd871bb6ea` (2026-08-19), publisher Routledge → Acumen** — correct, and the sweep completed cleanly. Verified independently at Crossref and OpenLibrary; no re-litigation needed.
- **`6ff3dd4e6a` (2026-08-03), the rest of L95** — calibration is **good**, not a boundary-substitution: the paragraph states the regress, then rejects it on the illusionist's own terms ("the bare regress assumes the seeming is itself phenomenal, precisely what illusionists deny, and it proves nothing"), relocates the pressure to the trade-of-questions, and declares the residue honestly ("neither side closes the case against the other inside the rival's framework"). No editor-vocabulary leakage.
- **`[[functional-seeming|functional seeming]] is Frankish's account of how`** — state: real-correct at argument level. Matches `concepts/functional-seeming`, which sources the move to Frankish and is consistent with the Frankish 2016 machinery (zero qualia / quasi-phenomenal properties) already in References.

### Reasoning-Mode Classification (editor-internal)

- Parfit (agency, MWI convergence, causal history): unchanged from the 2026-06-05 ledger — Mode Two, Mode Three, Mode Three. Sound.
- **Illusionism/Frankish (the 2026-08-03 rewrite, first classification)**: **Mixed** — opens by identifying the unsupported foundational move (the relocation trade earns its keep only if the second question is tractable), concedes the bare regress fails on the opponent's own terms, then marks the boundary explicitly. This is the sequence the discipline prescribes. No label leakage in prose.

### Possibility/Probability Slippage Check

None. `find_superlative_claims` returned 0. No empirical evidential-status claims and no organism-consciousness upgrades; every claim is metaphysical and explicitly tenet-grounded. The two edits this pass made both move *toward* calibration (a decorative falsifier removed, a concession given back its test), not away.

### Inline ↔ References cross-check

Clean in both directions. Tallis 2011 and Tallis 2024 are both now named inline; Parfit 1984/1995, Frankish 2016 and Lockwood 1989 cited inline; Swinburne, Chisholm, Johnston and Wallace remain bibliography-only, which all prior passes have accepted as this article's convention.

## Optimistic Analysis Summary

### Strengths Preserved

- The four-part rejection structure and the Lockwood/Many-Minds paragraph (L67) — the article's single strongest piece of evidence that the Parfit/MWI convergence is real rather than a parallel the Map imposes.
- The 2026-08-03 illusionism paragraph, which is a model of the engagement discipline and was left substantively untouched.
- All five tenet connections, the "genuinely open" contemplative framing, and the honest "neither side closes the case" residue.

### Enhancements Made

- The falsifier section now discriminates, and says out loud why the obvious fourth candidate does not — a stronger position than listing three.
- The contemplative concession regained the forward reference the condensation deleted.

### Cross-links Added

Two intra-article anchors (`#what-would-challenge-this-view`, `#the-illusionist-challenge`, `#the-practical-stakes`) — no new outbound wikilinks; the existing 13 all resolve.

## Length Check

2228 → **2371 words** (+143). Concepts thresholds 2500 / 3500 / 5000; status `ok`, **129 words below soft**, 1128 below the usable hard ceiling. Real budget existed and was spent on discrimination, not padding.

## Remaining Items

**Observed, out of scope (this article only) — flagged for the operator, not minted as tasks:**

1. **Five sibling loci run the anti-illusionism regress against the 2011 book alone**: `concepts/haecceity` L159, `topics/personal-identity` L148, `topics/eastern-philosophy-consciousness` L135, `topics/consciousness-in-simple-organisms` L191 (this one already carries both references), `concepts/attention-schema-theory` L107. The 2011 attribution is *sound* at each — the book does run the regress — but the anti-illusionism framing belongs to 2024. A one-sentence addition per file, additive, no deletions.
2. **A work-level confusion in two review files, not in article prose**: `deep-review-2026-07-17-philosophical-zombies` and `deep-review-2026-03-03-attention-schema-theory` attribute *"misrepresentation presupposes presentation"* to *Aping Mankind* (2011). Extraction B returns **0** for that phrase in the book; it is verbatim in *Philosophy Now* 161 (2024), as the memory record already establishes. Review-file record only; no live article carries it as a 2011 quote. Echo, not defect.
3. **`concepts/phenomenology-of-choice-and-volition` L201 dates *Aping Mankind* to 2010** — carried forward unchanged from the 2026-08-19 changelog's own out-of-scope flag. Crossref: issued 2011-06-30. Still the only year-variant in the corpus.

## Stability Notes

- **Bedrock disagreements** (eliminative materialist, hard-nosed physicalist, MWI defender): framework-boundary standoffs. Do not re-flag as critical. Carried unchanged from 2026-06-05.
- **"Right kind of cause" / "any cause"**: faithful to Parfit, not a self-contradiction. Carried unchanged from 2026-06-05.
- **No fabricated quotations / no phantom Tallis 2016**: the Parfit death passage is a paraphrase and the phantom 2016 reference is gone. Future edits must not reintroduce either.
- **Tallis 2011 *Aping Mankind*, Acumen** — metadata settled three ways (Crossref DOI, OpenLibrary, *Isis* review). Do not re-verify the tuple. The *work-level* question — which Tallis work carries the anti-illusionism version — is now settled in this article by carrying both. This is a framework-adjacent citation fact, not a stability exemption for any empirical claim attached to it.
- **The falsifier set is now 3 + 1 declared omission, and that is deliberate.** A future pass should not restore the teleportation item to make the count four, nor trim the omission note as redundant; the note *is* the finding. Equally, a pass wanting a fifth condition should check `git log -S` before assuming one was lost — the Whitehead-era condition #5 was correctly dropped with its section.
- **This article has now been condensed once and reviewed eight times.** The recurring failure mode here is not drift in the prose, which is stable, but **amputation debt**: the 2026-04-12 condensation removed 1512 words in one pass ten hours after a convergence finding, and two of the three defects found since (the fabricated Parfit quote surfaced 2026-05-26, and both critical issues in this pass) trace to that commit. A future pass looking for an unrun lens should diff `a2dfca14fb` before looking anywhere else.