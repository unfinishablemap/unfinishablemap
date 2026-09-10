---
ai_contribution: 100
ai_generated_date: 2026-09-10
ai_modified: 2026-09-10 10:27:10+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-10
date: &id001 2026-09-10
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-10 10:27:10+00:00
modified: *id001
related_articles: []
title: Deep Review - Quantum Completeness
topics: []
---

**Date**: 2026-09-10
**Article**: [Quantum Completeness](/concepts/quantum-completeness/)
**Previous review**: [2026-07-14](/reviews/deep-review-2026-07-14-quantum-completeness/) (5th). This is the **6th** deep review.
**Word count**: 3,022 → 3,150 (+128)

## Scope / Mode

Delta pass. `ai_modified` read today, but four correction commits have landed since the 07-14 review and none had been deep-reviewed: `178f33dc0b` (08-06, framework-boundary), `920c2ea806` (08-20, Stapp metadata), `4c7d2e75bd` (09-04, Zurek misattribution), `a8d79b075c` (09-10, [P-Q9](/positions/quantum-interface/#p-q9) channel count). The primary lens was therefore **did those four fixes take, and did any introduce a new problem** — small diffs to load-bearing sentences being exactly where a fix strands its surroundings.

## Verdict: real-findings pass — 1 critical attribution error (introduced by the 09-04 fix), 1 quote-fidelity over-read, 1 orphan citation, 1 wrong-work quote source

## Audit of the four unreviewed commits

- **`a8d79b075c` (09-10, [P-Q9](/positions/quantum-interface/#p-q9) three-channel residue) — HELD, verified faithful.** The article's clause tracks [P-Q9](/positions/quantum-interface/#p-q9)'s own 2026-09-09 wording on every element: "three channels"; the *conditional-statistical*, *mechanism-level* and *psychophysical* names; "open exposure rather than banked support"; "one coarse grain has run null (the preregistered intention-to-RNG tests of Maier et al. 2018)"; "the finer grains stay untested"; "preservation binds that marginal only and leaves the conditionals free". No drift. Maier et al. 2018 verified real-correct at Crossref (`10.3389/fpsyg.2018.00379`, *Front. Psychol.* 9:379).
- **`920c2ea806` (08-20, Stapp metadata) — HELD, and now publisher-verified.** Reference 8's Zygon clause reads "41(3), 2006. https://doi.org/10.1111/j.1467-9744.2005.00762.x". Crossref on that DOI returns *Zygon* **volume 41, issue 3**, issued **2006-09-02**, author Henry P. Stapp, and **no page range** — matching the entry exactly, including its deliberate omission of pages. The JCS half (12(11), 43–58, 2005) is confirmed. Note the corpus at large is *still* inconsistent on this work (2005 / 2006 / n.d.; LBNL / JCS / Zygon across ~20 files); the 08-20 sweep normalised only the files it touched. Out of scope here — this article's entry is correct.
- **`178f33dc0b` (08-06, framework-boundary) — HELD in its own clause, but left its surroundings stranded.** The clause it installed ("the Map acknowledges that placement but does not adopt it, since selecting only the question would weaken outcome-selection to context-setting") tracks `tenets.md` L91 faithfully. But the sentence *it sits inside* still said the Map's interaction occurs "at Process 1" — the very route `tenets.md` registers and declines. See the critical issue below.
- **`4c7d2e75bd` (09-04, Zurek) — the Zurek fix HELD in substance but over-read on one qualifier, AND the same commit introduced a new misattribution.** See both below.

## Critical Issues

### 1. Stapp's process numbering was misattributed, contradicting both `tenets.md` and the article's own text (introduced 2026-09-04) — FIXED

Commit `4c7d2e75bd` added: *"Splitting off the statistical rule governing outcomes as a third process is Stapp's refinement rather than von Neumann's (Stapp 2005)."* Verified against the **raw PDF of the cited paper** (`www-physics.lbl.gov/~stapp/QID.pdf`, pdftotext, whitespace-normalised):

- **"Process 3" occurs 0 times in Stapp 2005.** ("Process 1" 33×, "Process 2" 6×.) The cited paper contains no third process at all, so it cannot be the source of the refinement attributed to it.
- What Stapp 2005 *does* say, verbatim: *"After the intervention of this Process 1 decomposition of the state of the probed system into a set of discrete components, **nature chooses one of the possible outcomes** of this probing action. This 'choice on the part of nature' **is asserted to conform to a statistical rule**."*
- Where Stapp *does* use the term — `vNS.pdf`, `Quest.pdf`, `FW.pdf` — Process 3 is **nature's choice of outcome**, not the statistical rule: *"Process 3 is sometimes call the 'Dirac Choice.' Dirac called it a 'choice on the part of Nature.' It can be regarded as Nature's answer to a question effectively posed by the Process 1 choice"*; *"The third process is the abrupt event of answering the question specified by Process 1"*; *"This 'Process 3' is where the famous 'random element' enters into quantum mechanics."*

So the article had Process 1 and Process 3 **swapped in content**: it put "which outcome becomes actual" inside Process 1 and called Process 3 "the Born rule—the probabilities". Three independent supports that this is an error, not a stylistic variant:

1. The raw Stapp sources above.
2. **`tenets.md` L91** contrasts "a **Process-1** / context-selection alternative" with "which outcome results", and records that the Map has **not adopted** it. The article meanwhile said the Map's interaction occurs "at Process 1" — asserting in Map voice the route the canonical tenet declines. This is the same framework-boundary breach `178f33dc0b` was written to fix, regenerated one clause away from its own repair.
3. **Internal contradiction**: the article said the Map acts "at Process 1" *and*, in the same sentence, that Stapp locates conscious choice in question-selection while the Map declines that placement. On Stapp's real numbering the Map's disagreement with Stapp is precisely that the Map wants a say in Process 3 — which the article simultaneously declared "determined by physics".

**Resolution applied.** Section retitled "Where the Gap Lives: Process 1 and Process 3" (explicit `{#process-1}` anchor preserved — two inbound deep-links exist). The third-process sentence now cites Stapp 2005 only for what that paper says, in two verbatim quotes, and attributes the *numbering* without pinning it to that paper. Process 1 is now the posing of the question; Process 3 is nature's answer, with the Born rule fixing every probability "and the individual outcome not at all". The gap paragraph now names both parts. The Minimal Quantum Interaction paragraph now sites the Map's interaction at Process 3 and Stapp's at Process 1, which makes its own contrast intelligible and aligns it with `tenets.md` L91.

**Why five prior reviews missed it.** The 07-14 review explicitly ratified this as clean — *"Map-specific moves (consciousness-selection at Process 1 …) explicitly labelled; Barrett, Stapp, Zurek … accurately attributed."* That was true of the article **as it then stood**, which made no explicit claim about *whose* decomposition it was. The 09-04 commit added the explicit attribution, and a logged resolution reads as settled work. This is the `secondary-host-insertions-skip-the-source-fidelity-pass` shape: a correction pass aimed at the Zurek sentence added a second, unreviewed claim in the same file.

### 2. Zurek 2003 exclusivity over-read (introduced 2026-09-04) — FIXED

The 09-04 fix correctly removed a genuine misattribution (the prior text had Zurek "acknowledging that decoherence does not, by itself, solve the measurement problem" — no such statement exists in the paper; §VIII says the opposite, *"decoherence – through einselection – helps solve the measurement problem"*). But the replacement over-shot on one qualifier: it said Zurek *"locates **the one** major remaining gap in the derivation of the Born rule."*

Verified against the raw arXiv text (quant-ph/0105127v3, cross-checked in two independent renderings):
- `"the one major"` → **find = −1** (absent).
- Zurek's actual §VI.D wording is *"one major gap remains"* — indefinite, and scoped as a reply to Bell's for-practical-purposes charge.
- §IX names **further** remaining gaps in the plural: *"many of the remaining gaps in our understanding of quantum physics … such as the definition of systems, or the still mysterious details of the 'collapse'"*, and *"Many conceptual and technical issues (such as what constitutes 'a system') are still open."*

Sub-claim (A) of the same sentence is verbatim-supported and stands: Zurek §II.C — *"Existential interpretation recognizes that the information possessed by the observer is reflected in his einselected state, explaining his perception of a single 'branch' – 'his' classical Universe."*

**Resolution applied.** "the one major remaining gap" → "the major gap that remains once that account is granted". The following sentence's binary — "part company over whether **anything** is left to explain" — was also false to §IX (Zurek holds plenty is left to explain) and is now "part company over whether **the selection of an outcome** is among what is left to explain", which is both accurate and sharper.

### 3. Orphan inline citation: Emerson et al. (2013) — FIXED

Cited inline at offset 5920 for the PBR preparation-independence debate, with **no References entry** — an inline↔References orphan across all six reviews (the 05-27 ledger was "16-cite" and never covered it). Verified real, preprint-only: J. Emerson, D. Serbin, C. Sutherland, V. Veitch, arXiv:1312.1345 [quant-ph], v1 only, never journal-published (Crossref returns no matching work; INSPIRE `publication_info: None`; OpenAlex `type: preprint`). Added as reference 18.

### 4. Verbatim quote sourced to a work that does not contain it — FIXED

The article quotes Fuchs's *"a little moment of creation"* with no year, and the only Fuchs entry in the list was #9 (Fuchs, Mermin & Schack 2014, AJP). **The phrase does not occur in that paper** (checked against its arXiv source 1311.5253 — zero hits). The 07-14 review fixed the *wording* of this quote but not its source. Verified locus: Fuchs, *Notwithstanding Bohr, the Reasons for QBism*, arXiv:1705.03483v2, published as *Mind and Matter* 15(2), 245–300 (2017) — *"when an agent reaches out and touches the world, a little moment of creation occurs in response."* Inline cite `(Fuchs 2017)` added and reference 19 created. This is the `verbatim-quote-cited-to-wrong-work` channel.

## Publisher-of-Record Citation Ledger (§2.4)

All 17 pre-existing entries web-verified at Crossref / publisher this pass. Nothing fabricated; no wrong metadata.

- Einstein, Podolsky & Rosen 1935 — real-correct (`10.1103/PhysRev.47.777`, *Phys. Rev.* 47(10) 777–780)
- Bell 1964 — real-correct (`10.1103/PhysicsPhysiqueFizika.1.195`, 1(3) 195–200)
- Kochen & Specker 1967 — real-correct (`10.1512/iumj.1968.17.17004`; *J. Math. Mech.* 17(1) 59–87. The DOI slug reads 1968 because the journal was renamed *Indiana Univ. Math. J.* in 1971 and IUMJ dates vol. 17 no. 1 to 1968; the 1967 form is canonical and standard — **do not "correct" this in a future pass**)
- Hardy 1993 — real-correct (`10.1103/PhysRevLett.71.1665`, 71(11) 1665–1668)
- Pusey, Barrett & Rudolph 2012 — real-correct (`10.1038/nphys2309`, *Nat. Phys.* 8(6) 475–478)
- Hensen et al. 2015 — real-correct (`10.1038/nature15759`, *Nature* 526(7575) 682–686)
- Barrett, J. A. 2006 — real-correct (`10.1007/s10670-006-9016-z`, *Erkenntnis* 65(1) 97–115). **Jeffrey A.** Barrett, distinct from the **Jonathan** Barrett of PBR — both initials in the list are correct as written
- Stapp 2005 — real-correct (JCS 12(11) 43–58; Zygon reprint verified at `10.1111/j.1467-9744.2005.00762.x`, 41(3), 2006, no page range)
- Fuchs, Mermin & Schack 2014 — real-correct (`10.1119/1.4874855`, *AJP* 82(8) 749–754)
- Krizek & Mairhofer 2023 — real-correct (`10.3390/e25040585`, *Entropy* 25(4) 585)
- Von Neumann 1932 — real-correct
- Zurek 2003 — real-correct (`10.1103/RevModPhys.75.715`, *RMP* 75(3) 715–775)
- Schlosshauer 2007 — real-correct (`10.1007/978-3-540-35775-9`, Springer, The Frontiers Collection)
- Zurek 2009 — real-correct (`10.1038/nphys1202`, *Nat. Phys.* 5(3) 181–188)
- Albert 2010 — real-wrong-metadata (page range absent; added **pp. 355–368**, `10.1093/acprof:oso/9780199560561.003.0013`)
- Kent 2010 — real-wrong-metadata (page range absent; added **pp. 307–354**, `10.1093/acprof:oso/9780199560561.003.0012`)
- Maier, Dechamps & Pflitsch 2018 — real-correct (`10.3389/fpsyg.2018.00379`, *Front. Psychol.* 9:379)
- Emerson et al. 2013 — **added** (arXiv:1312.1345, preprint only)
- Fuchs 2017 — **added** (*Mind and Matter* 15(2) 245–300 / arXiv:1705.03483)

**Body sub-claims verified clean, recorded so future passes need not re-litigate:**
- Hardy "every case except maximally entangled states" — matches the APS abstract verbatim; the article's added "pure … two-qubit" qualifier is a correct refinement.
- Kochen-Specker "dimension three or more" — confirmed d ≥ 3.
- QBism "developed by Caves, Fuchs, and Schack and later joined by Mermin" — confirmed (founding papers Caves, Fuchs & Schack 2002, *PRA* 65, 022305; Mermin's conversion *Physics Today* 65(7), 2012).
- "loophole-free tests from 2015 onward" — Hensen (Delft) first by ~2 months, then Giustina and Shalm, both *PRL* 115(25), Dec 2015. Correct.
- **Empirical-currency sweep**: `find_superlative_claims` returns **0** claims. The 10⁻¹³ s decoherence figure was accepted as a defensible loose upper bound by the 06-25 and 07-14 passes; unchanged this pass, not re-litigated.

## Optimistic Analysis

**Strengths preserved** — the six-senses taxonomy opening; the honest Many-Worlds section (Everettian parsimony conceded before the indexical objection); the Newtonian precedent; the QBism contrast; the whole calibrated [P-Q3](/positions/quantum-interface/#p-q3)/[P-Q9](/positions/quantum-interface/#p-q9) residue clause installed on 09-04/09-10, which is the strongest passage in the article and was left untouched.

**Enhancement made** — the corrected numbering is a genuine argumentative gain, not just a fidelity repair: the gap is now stated as having *two distinct parts* (Process 1 undetermined by any law or statistic; Process 3 fixed in long-run frequency but open in each instance), which is a sharper claim than the previous flat "Process 1 is not determined by physics" and is exactly what the Map needs to site outcome-selection.

**Cross-links** — none added. The two open P3s on this file both propose link/prose additions; see below.

## Checks run and found clean (do not re-spend a pass here)

- **All 19 wikilink targets resolve.** 18 bare targets each have exactly one stem match, 1 path form (`positions/quantum-interface`) exists. No push-blocker.
- **§2.6 label leakage**: all 12 forbidden editor-vocabulary tokens return −1.
- **LLM cliché sweep**: the banned "This is not X. It is Y." construct returns 0 hits; "load-bearing" 0 hits.
- **Over-concession tells**: "no possible", "cannot ever", "in principle undetectable" all absent. The 09-04 commit replaced the old blanket "empirically unfalsifiable" with the scoped unconditioned-marginal calibration — a real improvement that holds.
- **`description`** present, 161 chars (1 over the 160 guide; left alone — accurate and not worth the churn).

## Reasoning-Mode Classification (editor-internal; changelog only)

- **QBism (Caves/Fuchs/Schack/Mermin)**: Mode Two — unsupported-foundational-move engagement; concedes QBism "correctly identifies" agent-dependence before pressing that a credence-only reading forfeits PBR's force. Unchanged, no leakage.
- **Many-worlds / Everettians**: Mode Three — framework-boundary marking, explicit; concedes Everettian parsimony, then rests on indexical identity (Tenet 4) with Albert 2010 / Kent 2010 carrying the residue honestly. Unchanged.
- **Zurek**: Mode Three, and *improved* this pass. The prior binary ("part company over whether anything is left to explain") overstated the boundary; it now names the precise point of divergence (whether outcome-selection is among what remains), which is honest boundary-marking rather than a manufactured standoff.

## Overlap with open queue items

**Yes — this review reaches the same conclusion as the open P3 at `obsidian/workflow/todo.md` line 2002, independently.** That task holds that §*The Decoherence Objection* "rests the corpus's canonical decoherence-gap argument on a standoff of authorities" and should be strengthened with the insolubility-theorem family from [improper-vs-proper-mixtures](/concepts/improper-vs-proper-mixtures/). Confirmed live this pass: `insolub` and `improper` both return **find = −1** in this article. My Zurek fix (issue 2) *narrows* the standoff to its true point of disagreement but does not remove it — the underlying weakness the P3 names is real and remains. **No duplicate task minted.** Two notes for whoever picks it up:
- The §IX Zurek passage surfaced this pass is directly useful material: Zurek himself calls the interpretation neither complete nor widely accepted, with "the still mysterious details of the 'collapse'" among the remaining gaps. That is a stronger, sourced lever than the current standoff framing.
- The task's word budget (~60–90) still clears: the article is now 3,150 words, 350 below the concepts hard threshold of 3,500.

The other open P3 (todo line ~1925, formal-constraint wing cross-links, **LINK-ONLY**) is untouched and unaffected.

## Remaining Items

One follow-up minted (P2, `refine-draft`): two live sibling articles carry the same swapped Process 1 / Process 3 content this pass corrected, and one of them explicitly defers to this article, so the fix here strands it. See the task for verified offsets.

## Stability Notes

- Bedrock disagreements from all five prior reviews remain in force and must NOT be re-flagged: the MWI indexical-identity standoff (Tenet 4 boundary), the eliminativist rejection of "gap → consciousness", and the framework-boundary status of consciousness-selection.
- **Citation metadata is now fully publisher-verified at 19 entries.** Do not re-run the metadata ledger unless the References block changes. In particular do not "fix" the Kochen-Specker 1967 date to 1968.
- The Fuchs quote channel is now closed on **both** axes — wording (07-14) and source work (this pass).
- **New stability note**: the process numbering is now pinned to Stapp's own usage and verified against four of his raw papers. Any future pass tempted to fold outcome-selection back into Process 1 should re-read `tenets.md` L91 first — that phrasing is the one the Map declines, and re-adopting it is a framework-boundary breach, not a stylistic choice.