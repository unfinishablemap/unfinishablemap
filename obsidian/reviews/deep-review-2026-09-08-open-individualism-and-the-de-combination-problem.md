---
title: "Deep Review - open-individualism-and-the-de-combination-problem (2026-09-08)"
created: 2026-09-08
modified: 2026-09-08
human_modified:
ai_modified: 2026-09-08T12:31:54+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[open-individualism-and-the-de-combination-problem]]"
  - "[[changelog]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-08
last_curated:
---

# Deep Review — open-individualism-and-the-de-combination-problem (2026-09-08)

**Target**: `topics/open-individualism-and-the-de-combination-problem.md` (3709w → 3781w; topics soft 3000 / hard 4000, printed not recalled).
**Previous reviews**: [[deep-review-2026-07-26-open-individualism-and-the-de-combination-problem|2026-07-26]] (no-op, embed-videos re-qualification) · [[deep-review-2026-07-19-open-individualism-and-the-de-combination-problem|2026-07-19]] (no-op) · [[deep-review-2026-06-19-open-individualism-and-the-de-combination-problem|2026-06-19]] (fresh-create defect-tail).
**Selection cause**: 44 days since last deep review; six `refine-draft` passes landed 2026-07-30, all *after* the 07-26 review, so the article has changed substantively since it was last reviewed. Not a cosmetic re-qualification.

**L117 was out of scope** (named locus in an open P2 scoping sweep). Confirmed untouched: line 117 is byte-identical pre- and post-edit, sha256 `fac05e01f7634083261c1ce242ea853c81aa23470eef84cb99b35b9c00ed574a`, length 965, and it does not appear in the diff.

## §2.4 Publisher-of-Record Citation Ledger

Trigger met: 26 references, author-year inline cites, References block modified since the last review. Full pass run. Method for each: Crossref DOI record (publisher deposit), plus a second independent source where the first was an aggregator.

| Cite | State |
|---|---|
| Kolak 2004, *I Am You*, Springer Synthese Library vol. 325 | **real-correct** (Crossref `10.1007/978-1-4020-3014-7`: Springer Netherlands, Synthese Library, 2004; vol. 325 confirmed at three catalogues) |
| Zuboff 1990, *Inquiry* 33(1) 39-68 | **real-correct** (Crossref `10.1080/00201749008602210`, exact on venue/volume/issue/pages/year). DOI added to the entry. |
| Miller 2018, *Ratio* 31(2) 137-154 | **real-correct**. 2018 is right — Crossref `issued` is 2017-05-02 (Wiley online-first), print issue 2018. Not changed. |
| Chalmers 2017, combination-problem chapter, pp. 179-214 | **real-correct — DO NOT RECONCILE TO 2016.** See the standing-decision note below. |
| Shani 2015, *Philosophical Papers* 44(3) **389-437** | **real-correct**. The SEP bibliography gives 389–**417**; Crossref `10.1080/05568641.2015.1106709` (Informa, publisher of record) gives **389-437**. The article is right and the SEP is wrong. Not changed. |
| Shani & Keppler 2018, *JAPA* 4(3) 390-410 | **real-correct** (Crossref `10.1017/apa.2018.30`) |
| Nagasawa & Wager 2016, pp. 113-129 | **real-correct** (Crossref `10.1093/acprof:oso/9780199359943.003.0005`) |
| Goff 2017, *Consciousness and Fundamental Reality*, OUP | **real-correct** (SEP bibliography) |
| Albahari 2020, Seager Handbook, 119-130 | **real-correct**; SEP gives 2020 and Seager 2020, 119–130. The existing explanatory note about the 2019 ebook date is corroborated independently — Mørch's own 2024 reference list dates the same chapter "2019a". Note retained. |
| Roelofs 2019, *Combining Minds*, OUP | **real-correct** (SEP bibliography) |
| Miller 2021, *JCS* 28(3-4) **112 ff.** | **real-wrong-metadata → corrected to 112-115.** "ff." is not a page range and a real one exists. Confirmed 112–115 by SEP bibliography, PhilPapers record metadata, and the Imprint Academic issue TOC. |
| Petersen 2021, *Idealistic Studies* 51(1) 69-101 | **real-correct** (Crossref `10.5840/idstudies2021429128`). Crossref's phantom second author (`None, None`) is a record artefact; no co-author added. |
| Shani 2022, *The Monist* 105(1) 6-24 | **real-correct** (Crossref `10.1093/monist/onab020`) |
| Mørch 2024, *JCS* 31(9-10) 88-112 | **real-correct** (Crossref `10.53765/20512201.31.9.088`) |
| Wager 2025, Bloomsbury | **real-correct** (Crossref chapter DOIs under `10.5040/9781350508644`) |
| Parfit 1984 · Olson 1997 · Snowdon 2014 · Schechtman 1996 | **real-correct** (SEP / standard catalogue metadata) |
| Oizumi, Albantakis & Tononi 2014, *PLOS Comp Biol* 10(5) e1003588 | **real-correct** |
| Frankish 2016, *JCS* 23(11-12) 11-39 · Dennett 1991 | **real-correct** (pre-DOI JCS; standard citation form) |
| SEP *Panpsychism* entry + subject-summing supplement | **real-correct** — see the verbatim check below |
| Schrödinger, "consciousness is a singular of which the plural is unknown" | **orphan quote → source added.** Was a verbatim quotation with no work, no year and no References entry — the only named-author quotation in the article lacking one. |

Inline ↔ References cross-check: every inline `Author YYYY` now has an entry and every entry is cited. Schrödinger was the sole orphan in either direction.

Empirical-record currency sweep: `find_superlative_claims` returns 0. One superlative the detector does not pattern-match was found by reading and fixed — see M2.

### ⚠️ Standing decision: Chalmers combination-problem year is **2017**. Do not "correct" it to 2016.

This nearly became a false critical find, and the next reviewer will hit the same evidence, so it is recorded in full.

Crossref (`10.1093/acprof:oso/9780199359943.003.0008`) reports `issued` **and** `published-print` as **2016-12-29**, with no online-first split; the SEP bibliography independently cites "Chalmers, David J., **2016**"; and this article's own reference 7 dates the *same edited volume* 2016 for Nagasawa & Wager. Three signals for 2016, plus an internal inconsistency, is a persuasive-looking case for an edit.

It is wrong. The corpus already adjudicated this on 2026-05-31 in a deliberate **2016→2017 corpus-wide reconciliation** (see `workflow/archive/changelog-2026-W22.md`, `deep-review-2026-06-01-boundary-and-projection.md`), verified against Chalmers's own date-ordered bibliography, and ~30 files carry 2017. I re-verified that basis directly at `consc.net/all-papers/`, which reads: *"The Combination Problem for Panpsychism. In (G. Bruntrup and L. Jaskolla, eds.) Panpsychism. Oxford University Press, **2017**. This paper was written on the same weekend as the other paper on panpsychism, but it was published four years later due to the vagaries of publishing."* The author of record says 2017. Crossref/SEP 2016 is the OUP-online/print-catalogue split the reconciliation explicitly noted.

Residual cosmetic blemish, **left deliberately unfixed**: the same volume appears as 2016 (ref 7, Crossref/SEP form) and 2017 (ref 4, author-bibliography form). Both are defensible under their own convention. No task minted — the risk of a task re-triggering a 2017→2016 regression across 30 files outweighs the blemish.

### Verbatim quote fidelity (raw source + printed offset, never a summariser's opinion)

Quote fidelity had never been run on this article. Five quoted or close-paraphrased attributions checked; **all five verbatim-correct**.

- **Miller 2018** — *"is equivalent to the combination problem"*: exact in the Wiley-deposited Crossref abstract — "there is a 'de-combination problem' facing the cosmopsychist, which is equivalent to the combination problem as they are both concerned with subjects being proper parts of other subjects." The article's "absolute and relative phenomenal unity / modification of the essential nature of subjects" pair is also exact. ✓
- **Shani 2022** — *"the widespread tendency to view IND as a mirror-image of micropsychism's combination problem (CP) is mistaken"*: exact in the OUP-deposited abstract; `IND` is Shani's own abbreviation; the "coupling of phenomenal constitution with phenomenal inclusion" gloss is faithful. ✓
- **Chalmers 2017** — *"just as hard as the combination problem"*: exact in the consc.net full text (`combination.pdf` → pdftotext, offset 45751: "the resulting decomposition problem seems just as hard as the combination problem"). The term *decomposition problem* is also his ("a reverse version of the combination problem, which we might call the decomposition problem", offset 41086). ✓ — but the framing verb dropped his hedge; fixed, see C2.
- **SEP** — *"crediting Albahari (2020), calls it decombination"* plus the conceivability mirror: **near-verbatim correct, in the supplement** *Possible Solutions to the Subject-Summing Problem*, which reference 24 explicitly names: "they arguably face an analogous problem, which Miri Albahari (2020) calls 'the decombination problem' … Just as we can conceive of micro-level subjects existing in the absence of macro-level subjects, so it seems that we can conceive of a conscious universe existing without having conscious parts (i.e., without anything within the universe being conscious)." The §4.5 "eases the problem in various respects" report at L79 is likewise faithful. ✓
  **Method warning for future reviewers**: grepping the *main* entry returns `decombination` only once, inside the bibliography (Miller 2021's title), with `conscious universe` and `conscious parts` both at −1 and Albahari discussed only for the unrelated Inner-Outer Gap Problem. That reads as a clean, triple-confirmed misattribution and it is a **false absence** — the claim lives in a different document. Fetch `entries/panpsychism/supplement.html` (not `subject-summing.html`, which 404s) before flagging anything about this sentence.
- **Mørch 2024** — the article's summary was checked against the open-access PDF (imprint.co.uk), not the abstract, because the abstract states no conclusion. Exact match: "only one of them, the fourth and strongest, satisfies both criteria" and "whether it clearly supports that egoism is irrational (as opposed to merely immoral)", with `SAME PERSON` as Mørch's own label. The article's "only the strongest oneness thesis … clearly makes egoism irrational rather than merely immoral" is faithful in every element. ✓
- **Parfit** — "deep further fact" is Parfit's own term of art from *Reasons and Persons*, correctly scare-quoted. ✓

## Pessimistic Analysis

### Critical issues (2, both fixed)

**C1 — internal contradiction: a stranded semantic dependent of the 2026-07-30 fix.** L119 asserted, flat: *"The de-combination problem **shows** that the cosmopsychist's apparent simplicity conceals a deep difficulty."* But L87 — rewritten on 2026-07-30 precisely to stop the article claiming a literature verdict it does not have — concedes: *"That verdict is the Map's own and provisional, not a settled finding of the literature—and a central participant rejects it"*, and Shani 2022 argues in terms the article itself quotes that the mirror-image reading "is mistaken". Two sections later the article asserted as demonstrated exactly what it had conceded was contested. This is the `sweep-fixes-the-disclaimer-and-strands-its-dependents` pattern: the disclaimer landed at L87 and its dependent at L119 was left live. Fixed by scoping the claim to its owner: *"On the Map's reading—the one Shani contests—the de-combination problem shows that …"*.

**C2 — dropped qualifier on a quoted judgement.** L75 read "he names the cosmopsychist's analogue the *decomposition problem* and **judges** it 'just as hard as the combination problem.'" Chalmers's sentence is *"the resulting decomposition problem **seems** just as hard as the combination problem"* — the quoted fragment was faithful but the framing verb converted his hedge into a verdict, and the hedge sat immediately outside the quotation marks where it could not be seen. Fixed to "which he says 'seems just as hard as the combination problem.'" — the hedge is now inside the quote, verbatim.

### Medium issues (4, all fixed)

**M1 — the Map's own apex over-read.** L101 said the apex synthesis treats "subject-summing and subject-dividing as **one impossibility** approached from two ends." The apex ([[mereology-of-mind]]) attributes that formulation to *Miller* ("**His diagnosis** is that subject-summing and subject-dividing are the same impossibility approached from opposite ends"), then explicitly hedges its own use of it — "That structural identity is the hinge — and **it is an argued thesis rather than a settled result**" — and elsewhere disclaims exactly the word borrowed here: "The inference runs on the state of the debate rather than on **a proof of impossibility**." So this article stated the Map's own position more strongly than the Map states it. This is the file's documented failure mode running in the less obvious direction: not a rival's cost overcounted, but the Map's own claim treated as free. Fixed to "one difficulty approached from two ends—an argued thesis there too, not a settled result." ("organising hinge" is accurate and was kept: the apex's `apex_thesis` and its "## The Hinge: The De-Combination Problem" heading both bear it out.)

**M2 — unsupported superlative inflating a rival.** L65 called the Schrödinger line "the **most-quoted** open-individualist sentiment from the sciences" — unsupportable as stated, and an over-claim running *against* the Map's position, which is the direction that collects endorsements rather than challenges. Fixed to "is widely quoted in the view's support."

**M3 — navigation surface asserted a verdict the body denies.** `description` read "Cousins, not twins—and both **costs** the Map declines." The body's organising distinction (lead ¶2, and "The Map declines open individualism and avoids the de-combination problem, **and the two stances differ**") is that one is a *rival the Map rejects* and the other a *cost the Map's rivals pay and the Map avoids*. Calling both "costs the Map declines" flattens the exact distinction the article exists to draw, and open individualism is not a cost anyone pays. Fixed to "Cousins, not twins: a rival the Map rejects, a cost it avoids." (193 → 177 chars, one shorter than the original; "numerically" deliberately retained rather than trimmed for length — dropping it would be this file's other characteristic defect.)

**M4 — Miller presented as neutral between escapes he ranks.** L73 said "two responses are open to *both* theorists symmetrically", accurate as far as it went, but Miller's abstract continues: "Of these two options, I find the latter option wanting and propose that the first should be adopted." Presenting him as indifferent understates his position — the mirror of the "enrolled for a verdict he does not hold" defect that the 2026-07-30 pass fixed elsewhere in this file. Added: "He does not treat the two as equally good, finding the second wanting and adopting the first."

### House style (1, fixed)

"load-bearing" as an intensifier at L107 → "The Map's argument against many-worlds **turns on** the *indexical* objection". No `This is not X. It is Y.` construct anywhere; no ANSI or EOF tool-tag artefacts.

### Bedrock disagreements — not defects, do not re-flag

No boundary substitution and no editor-vocabulary leakage (grep clean for all eight forbidden labels). Every named-opponent engagement is honest framework-boundary marking, correctly declared as such in prose:

- **Open individualism** (L107): "the rejection is honest engagement at a bedrock framework boundary, not a refutation from inside open individualism's own resources", followed by an unusually frank concession that the Map "has a posit rather than an argument" against the representational reading.
- **Illusionism** (L115): "bedrock again, and recorded as such rather than dressed as a refutation."
- **Reductive physicalism** (L113): parity conceded, and "the Map owes an argument for preferring the void."
- **Cosmopsychists** (L87): argued from inside their commitments — severing the constitution/inclusion coupling does not supply a positive grounding relation — with the residue declared contested.

No possibility/probability slippage: closed individualism is labelled "tenet-driven rather than empirically compelled", and the double-duty haecceity posit is called "internal coherence rather than independent confirmation". No over-concession tells (`no possible` / `cannot ever` / `in principle undetectable` all absent).

## Optimistic Analysis

### Strengths preserved (unchanged)

- **The double-duty admission at L109** is the article's best paragraph and rare in the corpus: it volunteers that the anti-MWI and anti-open-individualism rejections are "one bet staked twice rather than two mutually supporting rejections", and concedes an open-individualist dualist is "a live rival". Untouched.
- **The physicalism-parity paragraph (L113)** concedes that the Map's structural avoidance buys nothing against its chief rival, and that IIT's exclusion postulate supplies a boundary account where the Map has a void. Untouched.
- **The three-difference taxonomy (L95-99)** — subject matter / status / direction of the appearance — is the clearest statement in the corpus of why these two ideas are not the same idea. Untouched.
- **Kolak's taxonomy filing with Parfit's self-description separated out** (L56) is exactly the source/Map separation discipline working. Untouched.

### Expansion opportunity — deferred, deliberately not taken

Mørch 2024's conclusion contains a passage directly on the Map's individuation commitment: *"dualism has more resources than both physicalism and Russellian panpsychism to defend an individual self, or that we are all different persons, by positing individual mental substances or **haecceities**"*, while physicalism "has few resources to defend either an individual or a shared self". A non-dualist observing that dualism has the resources here is a genuine find, and Mørch is already cited.

Not inserted, for two reasons. It is a claim about theoretical *resources*, not about truth, and L109's whole point is that the haecceity posit is "internal coherence rather than independent confirmation" — dropping a friendly citation next to that concession would read as the ratification the paragraph disclaims. Second, the article is 219 words from its hard threshold. Recorded here for whoever revisits L109 with budget; it belongs as a qualified remark inside that paragraph, not as support for the posit.

## Length

3709 → **3781** words (+72). Soft 3000 / hard 4000 **printed, not recalled**; headroom to hard 219. Reference apparatus was 18% of the total before this pass, so the prose figure is well under the nominal excess — no condensation warranted. Every addition was funded: the Schrödinger reference (~30w) and the Miller and apex clarifications (~26w) are the only net growth; M2, the house-style fix and the description edit all removed words.

## Remaining Items

- **L117 scoping** — owned by the open P2 five-locus sweep. Untouched, unmodified, sha256-verified. No task minted; it already has one.
- **Volume-year convention blemish** (ref 4 2017 / ref 7 2016 for the same OUP volume). Deliberately not fixed and deliberately not tasked; see the standing decision above.
- **Mørch haecceity-resources remark** — deferred expansion opportunity, above.

No follow-up task minted. Nothing found needed work this article's own review could not do.

## Stability Notes

1. **Chalmers combination-problem year is 2017 and the 2016 evidence is a trap.** Crossref (print *and* issued 2016-12-29), the SEP bibliography, and this article's own ref 7 all point at 2016. Chalmers's own bibliography says 2017, the corpus reconciled to 2017 on 2026-05-31 on that basis, and ~30 files carry it. A future reviewer who "fixes" this regresses a verified decision and desynchronises one file from thirty. Do not change it without overturning the reconciliation corpus-wide.
2. **Shani 2015 is 389-437, not 389-417.** The SEP has the wrong page range; Crossref/Informa has the right one and the article follows it. Do not reconcile the article to the SEP.
3. **The SEP de-combination claim lives in the supplement, not the main entry.** Grepping the main entry produces a triple-confirmed false absence that looks exactly like a misattribution. Fetch `supplement.html`.
4. **Miller 2018 is 2018.** Crossref `issued` 2017-05-02 is Wiley online-first; the print issue is 2018. Already adjudicated for Albahari in this file on 2026-07-30.
5. **Open individualism vs the Map's closed-individualist haecceity commitment is bedrock**, explicitly registered as such in the article, and already conceded to be tenet-driven rather than empirically forced. Do not re-flag as a calibration defect. This is the third consecutive review to record it.
6. **Illusionism is bedrock too** and the article says so in terms ("bedrock again, and recorded as such rather than dressed as a refutation"). Do not re-flag.
7. **The cost-ledger axis is now repaired on both sides.** The 2026-07-30 passes fixed the rivals'-costs-counted-Map's-free direction; this pass fixed the two remaining dependents where the *Map's own* claims ran ahead of their support (L119's verdict, L101's reading of its own apex). If a future review wants to firm either back up, that is oscillation — the constraint is L87, which concedes the verdict is contested.
