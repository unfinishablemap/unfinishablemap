---
title: "Deep Review - The Phenomenology-vs-Function Axis"
created: 2026-07-29
modified: 2026-07-29
human_modified: null
ai_modified: 2026-07-29T15:20:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[phenomenology-vs-function-axis]]"
  - "[[synaesthesia]]"
  - "[[synesthetic-void]]"
  - "[[phenomenal-variation-within-a-species]]"
  - "[[functionalism]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-07-29
last_curated: null
---

**Date**: 2026-07-29
**Article**: [[phenomenology-vs-function-axis|The Phenomenology-vs-Function Axis]]
**Previous reviews**:
- [[deep-review-2026-06-01-phenomenology-vs-function-axis|2026-06-01 (6th pass: metadata web-verify)]]
- [[deep-review-2026-06-17-phenomenology-vs-function-axis|2026-06-17 (7th pass: Wager fix + Gray first-dissociation cross-corpus resolution)]]
- [[deep-review-2026-07-14-phenomenology-vs-function-axis|2026-07-14 (8th pass: verbatim quote-fidelity, no body edits)]]

**Mode**: 9th pass. The article re-qualified for selection because of a genuine body change: commit `3d4e2d27c` (2026-07-28) added a predictive-processing concession at the synaesthesia bullet. This pass verified that concession, then ran the one lens the 06-17 and 07-14 passes had not applied to the Gray material — **primary-source verification of the attributed argument itself**, as opposed to its citation metadata (06-17) or its short terms-of-art (07-14, explicitly "not re-litigated").

That lens found two real defects, both of which prior passes had inspected and consciously preserved.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Fabricated verbatim quote — `"function and qualia come apart in two ways"` attributed to Gray (2003).** FIXED (de-quoted), and propagated corpus-wide.

The phrase was quote-marked and attributed to Gray in five live files. Verification:
- The **PubMed abstract** (PMID 12757818) does not contain it. The abstract is about Hurley and Noë's cortical dominance/deference analysis.
- The **IEP Synesthesia entry** — the only findable source for the phrase — uses it in *its own* summarising voice with a bare page citation: *"J.A. Gray, as mentioned earlier, also thinks synesthesia (specifically, colored hearing) poses a broader challenge to functionalism, since it shows that function and qualia come apart in two ways (2003, p.194)."* No quotation marks. The same IEP passage *does* put quotation marks around genuine Gray quotes elsewhere (e.g. Gray calls the alien-colour persistence a `"major obstacle"`, 2003 p.193), which establishes that IEP marks quotation when it means quotation.
- Publisher-of-record body text was unreachable (cell.com and ScienceDirect both 403), so fabrication cannot be *proved*; but the balance of evidence is that the Map quote-marked a secondary source's paraphrase. Per `citation-verify-false-negative` the claim is preserved and only the quotation marks removed — this is the `quote-aggregator-ratification-corrupts-verbatim` and `coalesce-wraps-paraphrase-as-fabricated-verbatim-quote` pattern, and de-quoting is the correct minimal remedy.

**2. Attribution error — Gray's *second* dissociation is coloured hearing, not grapheme-recognition.** FIXED, and propagated corpus-wide.

The article rendered Gray's second dissociation as *"the same grapheme-recognition process generates colour experience in synaesthetes but not in non-synaesthetes"*, and at the "Mapping the Exemplars" bullet asserted that **"Gray (2003) explicitly identifies"** it. Per IEP, Gray's actual two arguments are both about **coloured hearing**:
1. *"seeing and hearing are functionally different, and yet either modality can result in exactly the same color experience"* — the Map's pattern (a). Already faithful; unchanged.
2. *"Hearing is governed by only one set of input-output relationships, but gives rise to both auditory and visual qualia in the colored-hearing synesthete"* — the Map's pattern (b). This is what the grapheme gloss displaced.

**This re-opens a resolution the 2026-06-17 review recorded as complete**, and does so under the skill's stated exception ("the resolution was actually incorrect or incomplete"). That review corrected the *first* dissociation from "grapheme-recognition" to "auditory" in two files on exactly this evidence, but its changelog entry explicitly **"preserved unchanged … the second-dissociation grapheme-recognition gloss (faithful instantiation of 'same function, different qualia')"**. The reasoning was half-right: the grapheme case *is* a faithful instantiation of the pattern, but it is not Gray's, and the article attributes it to him with "explicitly identifies". Correcting the first dissociation while leaving the second one grapheme-framed left the file internally inconsistent about which synaesthesia type Gray's argument concerns.

**3. Dropped hedge on Zeman (2024).** FIXED.
Article asserted that introspective vocabulary "masks radically different underlying frontoparietal-to-visual network connectivity". Zeman's review says *initial results suggest* that connectivity alterations *may provide* the neural substrate. A review-level "may" was rendered as established fact. Rewritten to carry Zeman's own evidential strength.

### Publisher-of-record citation ledger (§2.4)

References block unchanged since the 06-17 full metadata pass; this ledger records only the cites re-checked at the publisher this pass, on the *argument-fidelity* and *empirical-claim* axes rather than the metadata axis.

- **Gray, J.A. (2003), "How are qualia coupled to functions?"** — state: **real-wrong-metadata + attribution-corrected**. Author confirmed *Jeffrey Gray*; *TiCS* 7(5):192–194 (PubMed 12757818). Reference upgraded from `7,` to `7(5),`. Both dissociations re-attributed to coloured hearing; quote marks removed. Note for future passes: the 2003 item is a short commentary on Hurley & Noë; IEP cites p.194 for the two-ways challenge, so the 2003 cite is correct and needs no re-pointing to Gray et al. (2002).
- **Wager, A. (1999), "The Extra Qualia Problem"** — state: **real-correct**. IEP independently confirms Wager "dubs this the 'extra qualia' problem" (p.268) and the gloss "mental states can be the same representationally, but differ when it comes to experiential character". The Map's paraphrase is faithful. Metadata (*Philosophical Psychology* 12(3):263–281, author Adam) re-confirmed via PhilPapers.
- **Kay, Keogh & Pearson (2024)** — state: **real-correct, two paraphrase refinements applied**. Publisher abstract confirms "Both groups demonstrated classic linear increases in response time **and error-rate** as functions of angular disparity" (article said response time only — error rate added, since the shared task signature is what carries the task-level-grain argument) and "Control participants **generally favoured** using object-based mental rotation strategies" (article said controls "use" — qualifier restored). Main verbatim quote re-confirmed faithful.
- **Zeman, A. (2024)** — state: **currency/strength-corrected**. Citation faithful; the *claim* overstated the review's hedging. Fixed (issue 3 above).
- **van Leeuwen, Singer & Nikolić (2015)** — state: **real-correct, verb corrected**. *Frontiers in Psychology* 6:1850 confirmed. It is a **review**, and the semantics claim is one it argues for ("we draw attention to the role of semantics in synesthesia"); "find" changed to "argue".
- **Lennon (2023), Strawson (1994), Wegner & Wheatley (1999), Wegner (2002), Putnam (1967), Block & Fodor (1972)** — not re-litigated; metadata verified 06-17, Lennon quote verified verbatim 07-14.

### Empirical-record currency sweep

`find_superlative_claims` returns empty. N/A.

### Editor-vocabulary leakage scan

Clean. No forbidden labels in article prose.

### Medium Issues Found

**4. The predictive-processing concession was buried.** FIXED. The 07-28 edit installed the concession only in the "Mapping the Exemplars" bullet, leaving the exemplar section (where a top-down or truncated reader forms their view of the synaesthesia case) presenting the Wager/Gray dissociation with only the older van-Leeuwen hedge. Added a one-sentence forward pointer in the exemplar section. Truncation resilience is a stated style-guide requirement and the concession materially changes the case's strength.

**5. Downstream coherence with the new concession.** FIXED. "What the Axis Is Not" still illustrated successful single-case absorption with imagery alone ("as the multi-realizability move plausibly already does for imagery"). With predictive processing now conceded for synaesthesia, two of four exemplars have working single-case absorptions. Updated, with the note that this is what the axis's own prediction anticipates rather than a counterexample — while raising the bar the joint-set claim must clear.

### Counterarguments Considered

Unchanged and not re-flagged: functionalist absorption via multi-realizability and finer-grain individuation; the introspection-as-metacognitive-output second front; bedrock disagreements (eliminativist, Wegner's own illusionism, MWI branch-functionalism, Buddhist deconstruction).

### Attribution / Reasoning-Mode

Functionalist engagement remains Mixed (in-framework constraint + honest boundary-marking). No boundary-substitution; no label leakage. The predictive-processing concession *strengthens* the honesty of the engagement — it concedes a live absorption rather than deflecting it.

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded opening and the grain-commitment machinery ("Mapping the Exemplars to the Two Patterns") — still the best handling of the function-grain question in the corpus.
- Well-calibrated "Relation to Site Perspective". The §2 diagnostic test (would a tenet-accepting reviewer flag the dualism connection as overstated?) returns NO. No possibility/probability slippage.
- The 07-28 predictive-processing concession is a genuine improvement: it concedes a strong rival at the exact place the rival bites.

### Enhancements Made

- Gray's argument now stated in his own terms (coloured hearing, both directions), which is *clearer* than the previous mixed-modality rendering as well as more accurate.
- Zeman and van Leeuwen claims now carry their sources' actual evidential strength.

### Cross-links Added

None. Link density already strong; one low-value Further Reading entry removed for length neutrality ([[cognitive-phenomenology]], already present in frontmatter and reachable via the topic article entry).

## Length Management

3071 → 3101 words (124% of the 2500 soft threshold; hard threshold 3500). Length-neutral mode observed: the ~110 words of corrective additions were offset by trimming five redundancies — a filler transition in the imagery section, a duplicated cross-cluster-signal clause in the intro (restated verbatim under "Why the Axis Earns a Structural Slot"), a closing sentence in "Independence from presence/absence" that restated the lead, a wordy clause in "What the Axis Is Not", and one Further Reading entry. Net +30 words (<1%).

Also removed "load-bearing" as a default intensifier ("the axis's load-bearing prediction" → "central prediction") per the CLAUDE.md overused-words rule.

## Cross-corpus family resolution (§2.4 step 6)

Both defects were corpus-wide. Propagated the canonical form to every live file carrying them:

- `obsidian/concepts/phenomenology-vs-function-axis.md` (two loci: exemplar section, Mapping bullet)
- `obsidian/topics/synaesthesia.md` L104
- `obsidian/apex/phenomenal-variation-within-a-species.md` L103
- `obsidian/voids/synesthetic-void.md` L54, and L102 (the fine-grained-functionalist reply, which had built its argument on "same grapheme-recognition process … individuated coarsely as 'same grapheme'" — re-based onto the auditory input-output profile / "same heard word")

Verified after the sweep: no live file quote-marks the phrase; no live file attributes a grapheme example to Gray. Remaining grapheme references across these files are all legitimate (grapheme-colour synaesthesia as a phenomenon, Hubbard/Ramachandran neuroimaging, MacPherson's extraordinary feature, representationalist sub-individuation).

Family files got `ai_modified` bumped only — **not** `last_deep_review`, since they received a targeted correction, not a review.

## Remaining Items

- `obsidian/research/voids-synesthetic-void-2026-02-23.md:45` still carries the old quoted form and the pre-06-17 dissociation gloss. Left unchanged: it is a historical input record, out of standing-mandate scope — consistent with the 06-17 and 07-14 precedent on the same file.

## Stability Notes

The article is at firm convergence on structure and argument; the two defects found this pass were **inherited citation-fidelity errors, not structural ones**, and both had survived multiple passes precisely because intra-corpus consistency ratified them across five files.

The generalisable lesson, and the reason this pass was not a no-op: a prior review verifying a citation's *metadata* (06-17) and a later one verifying its *short quoted terms* (07-14) can both pass while the *attributed argument* is wrong. Verifying that Gray's paper exists, and that "extra qualia problem" is Wager's phrase, told us nothing about whether Gray's second dissociation concerns graphemes or hearing. That is a fourth axis alongside metadata, quote fidelity, and empirical-claim fidelity: **argument-attribution fidelity** — does the source actually make the argument in the form attributed to them?

Future reviews should:
- **NOT re-quote** "function and qualia come apart in two ways" — it is IEP's summary of Gray, not Gray's wording. If the TiCS body text ever becomes reachable and the phrase is found verbatim on p.194, restoring the quote marks is warranted; absent that, leave it de-quoted.
- **NOT re-introduce** grapheme-recognition into *either* of Gray's dissociations. His case is coloured hearing throughout. Grapheme-colour synaesthesia is legitimately used elsewhere in the corpus for MacPherson, Hubbard/Ramachandran and the representationalist reply — those are not the same claim.
- **NOT re-flag** the Wager citation (Adam Wager, *Philosophical Psychology* 12(3):263–281 — verified 06-17, IEP-corroborated 07-29), the Lennon quote (verbatim-faithful, 07-14), the dualism connection as evidential slippage (diagnostic returns NO), or the functionalist engagement as boundary-substitution.
- Treat the article as converged again. Absent a further body change or contesting research, it should be selection-EXCLUDED.
