---
title: "Deep Review - Transactional Interpretation of Quantum Mechanics"
created: 2026-08-02
modified: 2026-08-02
human_modified: null
ai_modified: 2026-08-02T20:05:00+00:00
draft: false
topics: []
concepts: [transactional-interpretation-of-quantum-mechanics]
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-02
last_curated: null
---

**Date**: 2026-08-02
**Article**: [[transactional-interpretation-of-quantum-mechanics|Transactional Interpretation of Quantum Mechanics]]
**Previous review**: [[deep-review-2026-07-13-transactional-interpretation-of-quantum-mechanics|2026-07-13]] (disposition: CONVERGED-CLEAN-NOW-PUBLISHER-VERIFIED)

The only body-affecting delta since the 2026-07-13 pass was commit `afaef915c`, a frontmatter
`topics: []` → three-slug fill. Prose was untouched, so this pass deliberately ran the **lenses the
prior citation-focused pass did not**: physics-paraphrase fidelity at the publisher, style-guide
compliance, editor-label leakage, and family-resolution of citation metadata across the corpus.

That reframing paid off. The prior review's ledger recorded Cramer 1986 as "real-correct
(page-pin confirmed)" at 647–688. **The page pin was wrong, and the prior review ratified it.**

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Cramer 1986 end-page wrong corpus-wide (real-wrong-metadata) — FIXED, 7 files / 26 loci.**

The canonical TI citation was printed as *Rev. Mod. Phys.* 58(3), **647–688**. The true range is
**647–687**. Confirmed at four independent publisher-of-record authorities:

| Authority | Value |
|---|---|
| Crossref (APS-deposited metadata) | 647-687 |
| APS registered DOI metadata (CSL content negotiation on `10.1103/RevModPhys.58.647`) | 647-687 |
| OpenAlex | 647-687 |
| INSPIRE-HEP | `page_start` 647, `page_end` 687 |

**Provenance of the error — this is the instructive part.** It was not a typo introduced at random.
The research note `research/transactional-interpretation-of-quantum-mechanics-2026-07-12.md` carried
an explicit *false verification claim* stating that the end page was 688 and that the task brief's
hint of "647-687" was "off by one." Its stated evidence was **Wikipedia, SciRP, and SciEPub reference
records plus intra-corpus consistency** — three aggregators and a self-reference. A W23 deep-review
then actively rewrote a correct `647-687` **to** `647-688` (logged in
`workflow/archive/changelog-2026-W23.md`), i.e. the corpus corrected itself *into* the error.
Kastner's own 2016 overview reference list also prints 688, which is how the typo entered the
secondary literature and made the aggregators agree.

This is a clean instance of the documented failure mode: **intra-corpus and aggregator consistency
ratifies wrong citations rather than catching them.** Only the publisher-deposited record caught it.

Loci corrected (obsidian + archive, then synced to hugo):
- `obsidian/concepts/transactional-interpretation-of-quantum-mechanics.md` (review target; DOI also added)
- `obsidian/apex/born-preserving-causal-efficacy.md`
- `obsidian/concepts/quantum-indeterminacy-free-will.md`
- `obsidian/topics/forward-in-time-vs-time-symmetric-selection.md`
- `obsidian/research/retrocausal-selection-consciousness-physics-2026-03-14.md`
- `obsidian/research/transactional-interpretation-of-quantum-mechanics-2026-07-12.md` (source of propagation)
- `archive/concepts/retrocausal-selection.md`

Four files already carried the correct 647–687 and were left alone
(`qm-interpretations-beyond-many-worlds`, `born-rule-and-the-consciousness-interface`,
`born-rule-derivation-limits-followup-2026-03-16`, `archive/topics/born-rule-interpretation-invariance-consciousness`)
— the corpus was split 26 wrong / 10 right, with the wrong value in the majority.

**Anti-oscillation guard installed.** Because the wrong value is the majority reading in the
secondary literature (including Kastner), this defect is a re-flip risk. The research note now
carries an explicit ⚠️ marker naming 688 as a known attractor, listing the four authorities, and
recording that aggregator agreement is *not* evidence here.

### Medium Issues Found

**2. LLM-cliché construct in the lead of the handshake section — FIXED.** Line 27 opened
"a quantum interaction is not a one-directional emission followed by a later detection. It is a
two-way exchange…" — the negation-then-correction pattern explicitly prohibited in both `CLAUDE.md`
and `project/writing-style.md` §"Overused Words and Constructions". Rewritten to lead with the
positive claim ("is a two-way exchange completed across the interval …, rather than a one-directional
emission followed by a later detection"), which also improves front-loading. Per the style guide's own
instruction ("a guide for *future* writing — no need to sweep existing uses"), this was fixed in the
article under review only; no corpus sweep.

### Considered and Rejected (asserted defects that proved false)

- **`description` length (192 chars vs the schema's "150-160")** — measured against the live corpus
  before acting: median 176, mean 184, 34% of concept/topic articles are ≥190. 192 is at norm. No edit.
- **"atemporal" in the Cramer section vs "only an actualized transaction is a spacetime event" in
  the Kastner section** — looks like an internal contradiction, is not. "Atemporal" is used in the
  weak sense (spanning the emission-absorption interval rather than sitting at an instant), which is
  compatible with Cramer's 3+1 spacetime ontology; the pre-spacetime claim is correctly quarantined
  to the Kastner section. No edit.
- **Maudlin year 1994 vs Kastner's "Maudlin (1996)"** — the article's 1994 Blackwell first edition is
  correct; 1996 is a reprint and Kastner cites the book inconsistently across her own works
  (elsewhere 2002). No edit.

### Publisher-of-Record Physics-Paraphrase Ledger (lens NOT run by the prior pass)

The prior pass verified bibliographic *metadata* and *framing*. It did not verify the article's
physics paraphrases. All now verified:

- **Born-rule gloss** ("the echo … has strength proportional to ψ times ψ\*, that is |ψ|²") —
  **real-correct**, and stronger than assumed: Cramer's own RMP abstract states TI "leads in a natural
  way to justification of the Heisenberg uncertainty principle and the Born probability law
  (P=ψψ\*)". The ψψ\* formulation is Cramer's own, not a secondary gloss. The research note's
  standing UNVERIFIED flag on this wording has been cleared.
- **Nonlocality + relativistic invariance** ("nonlocal (consistent with Bell-inequality violations)
  while remaining relativistically invariant and causally coherent") — **real-correct**, near-verbatim
  to the abstract: "explicitly nonlocal and thereby consistent with recent tests of the Bell
  inequality, yet is relativistically invariant and fully causal." Correctly attributed as *Cramer's
  argument* rather than asserted as settled fact.
- **Pseudotime gloss** ("a heuristic sequencing device …, explicitly *not* a claim that the handshake
  unfolds within ordinary time") — **real-correct**. Kastner's 2016 overview (arXiv:1608.00660):
  "Cramer used the term 'pseudotime' … but stressed that it was just a heuristic tool, and did not
  correspond to any real physical domain."
- **Wheeler–Feynman half-sum** ("the electromagnetic field is taken as *half the sum* of retarded and
  advanced solutions") — **real-correct**. Kastner: "A charge emits a field in the form of
  half-retarded, half-advanced solutions to the wave equation." Radiation-reaction claim is standard WF.
- **Cramer's hierarchy patch** ("Cramer added a hierarchy or ordering to pseudotime transaction
  formation") — **real-correct**. Kastner: "the dynamical hierarchical account of transactions that
  Cramer presents as a rebuttal to the Maudlin challenge."
- **Wheeler–Feynman page pins** (not cited in the article; the research note flagged them for
  verification) — **verified and flag cleared**: 1945 = RMP **17(2-3):157-181**; 1949 = RMP
  **21(3):425-433**. Kastner's overview misprints the 1945 range as 157-161; APS figures used.

### Empirical-Currency / Superlative Sweep
`find_superlative_claims` returned zero hits. No currency defect.

### Link / Slug Integrity
All 11 wikilink and `topics:`/`concepts:` slugs resolve to live files. The three newly-added
`topics:` entries are correctly **bare** per the topic-string canonical form and all three target
real articles in `topics/`. No broken references.

### Editor-Label Leakage (§2.6)
Clean — zero occurrences of editor-vocabulary terms in prose. The article engages Maudlin and the
physicalist reading in natural prose. Engagement with Cramer/Kastner physicalism: **Mode Three**
(framework-boundary marking) — correctly and honestly executed; the article states the Tenet 1
conflict outright and quarantines the borrowing. No boundary-substitution.

## Optimistic Analysis Summary

### Strengths Preserved
- Source/Map separation remains exemplary and was not touched.
- The Maudlin objection stays foregrounded with the reply flagged as contested.
- Tenet mapping (1 conflict acknowledged; 2/3 as borrowing rationale) remains concrete.

### Enhancements Made
- Lead sentence of the handshake section now front-loads the positive claim.
- Reference 1 now carries the DOI, making the canonical citation self-verifying at the publisher and
  harder to re-corrupt.

### Cross-links Added
None — the article is already densely and correctly integrated.

## Remaining Items

None for this article. **Corpus-level note for future passes**: the Cramer 1986 page-pin family is now
consistent at 647–687 across all three trees. Because 688 is the majority reading in the secondary
literature, any future "correction" back to 688 is a regression — see the ⚠️ guard in
`research/transactional-interpretation-of-quantum-mechanics-2026-07-12.md`.

## Stability Notes

- **Physicalism vs Tenet 1 is bedrock, not a flaw.** Carried forward from 2026-07-13 — do NOT re-flag.
- **The Maudlin↔Kastner↔Lewis debate is genuinely unsettled.** "The debate is unsettled" is the correct
  calibration; do not push toward "resolved by PTI" or "fatal to TI." Carried forward.
- **No possibility/probability slippage.** Re-checked this pass and still true: the article frames
  TI-based conscious selection as speculation throughout and never treats tenet-coherence as raising
  evidential status. A tenet-accepting reviewer would not flag an over-claim.
- **"Atemporal" (Cramer section) is not in tension with "actualized transaction is a spacetime event"
  (Kastner section).** Examined and cleared this pass — do not re-flag as an internal contradiction.
- **Methodological lesson worth propagating.** A prior review marked this article CONVERGED-CLEAN with
  a full per-cite publisher ledger, and a citation defect still survived — because the ledger checked
  that each *paper exists as described* but inherited one field from a note that had "verified" it
  against aggregators. Convergence on one lens is not convergence overall. The cheap discriminator
  that caught it: querying structured publisher-deposited metadata (Crossref / DOI content negotiation
  / INSPIRE) rather than reading a landing page, which also sidesteps APS's 403.
- **Disposition: NOT-CONVERGED-AS-PREVIOUSLY-BELIEVED; now corrected and family-resolved.**
  `ai_system` set to claude-opus-5 for this pass (real content edits made by this model).
