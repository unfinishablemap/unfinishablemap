---
ai_contribution: 100
ai_generated_date: 2026-09-21
ai_modified: 2026-09-21 11:33:59+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-21
date: &id001 2026-09-21
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-21 11:33:59+00:00
modified: *id001
related_articles: []
title: Deep Review - Basal and Bioelectric Cognition - 2026-09-21
topics: []
---

**Date**: 2026-09-21
**Article**: [Basal and Bioelectric Cognition: Levin's Morphogenetic Agency and Xenobots](/topics/basal-and-bioelectric-cognition/)
**Previous review**: [2026-08-03](/reviews/deep-review-2026-08-03-basal-and-bioelectric-cognition/); before that 2026-07-19 (full-persona no-op) and 2026-07-08 (citation-metadata no-op)

**Verdict**: **one critical issue found and fixed, one medium, one low — plus the 08-03 owed item discharged.** Word count 3993 → 3995 (prose 3293 → 3295; apparatus unchanged at 718). Status `soft_warning` throughout; 4 words remain under the 3999 usable ceiling.

## Change since last review

Eight `refine-draft` commits on 2026-09-09 discharged the two same-day outer reviews
([outer-review-2026-09-09-claude-opus-5](/reviews/outer-review-2026-09-09-claude-opus-5/), [outer-review-2026-09-09-chatgpt-5-6-sol-pro](/reviews/outer-review-2026-09-09-chatgpt-5-6-sol-pro/)),
which had charged a **co-optation firewall failure**: the article previously claimed Levin
"brackets phenomenal sentience" and converted that silence into evidence for the decoupling.
The article now states the opposite and correct thing — the decoupling is drawn *against*
Levin, whose own gradualism runs the other way — and quotes TAME's continuum-of-consciousness
passages to prove it. Those findings are **discharged, not re-flaggable**. The same pass added
the four rival criteria (Laukkonen, Butlin, Birch, Seth), fixed "offspring" → "regenerates",
and replaced the Pai corrigendum DOI with the research-article DOI.

**The critical issue found this pass is in that new material** — the `fresh-create-defect-tail`
pattern. The Birch engagement was written on 2026-09-09 and has never been reviewed.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Birch's sentience-candidate bar restated in threshold vocabulary he does not use, with his
qualifier dropped (FIXED).**

The article read:

> Birch (2024) sets a deliberately inclusive bar—a "sentience candidate" is a system for which
> sentience is a credible, **non-negligible** possibility, assessed case by case—and presses
> exactly where this article stops, asking whether "very low rather than exactly zero" is
> **negligible**. On his own bar it is, here: …

Verified against the open-access book text (OAPEN mirror of the OUP CC edition, 977k chars,
grep-verifiable). Birch's actual definition, which occurs twice verbatim:

> A system S is a sentience candidate if there is an evidence base that: (a) implies **a
> realistic possibility of sentience in S that it would be irresponsible to ignore when making
> policy decisions that will affect S**, and (b) is rich enough to allow the identification of
> welfare risks and the design and assessment of precautions.

Two defects, both in §2.5 classes:

- **Dropped qualifier that changes meaning.** Birch's (a) is not a bare probabilistic threshold.
  It is an *action-guiding* one: the possibility must be realistic **and irresponsible to ignore
  in policy decisions**. The article compressed this to "credible, non-negligible possibility,
  assessed case by case", which removes the policy clause entirely and converts a normative bar
  into a probabilistic one.
- **Misattributed term of art.** `"non-negligible"` occurs **0 times** in Birch's book.
  `"negligible"` occurs exactly **twice**, both in an unrelated passage (Test 2: Adequacy, on
  whether a *response* renders a *risk* negligible). The article then built its verdict on that
  imported word — "asking whether … is negligible. On his own bar it is" — putting a
  negligibility test in Birch's mouth that he never runs.

The load-bearing conclusion survives: the article's gloss of condition **(b)** ("evidence rich
enough to identify a welfare risk and design a precaution around it") is *exact*, and (b) is
what actually defeats planarian candidature. Only the (a) gloss was wrong.

**Family resolution (§2.4 step 6) — this article is the sole locus.** Grepped `non-negligible`
across `obsidian/topics|concepts|apex|voids|positions` and `archive/`: 7 occurrences in 6 files.
The Map's own dedicated Birch article, [birch-edge-of-sentience-and-the-five-tier-scale](/topics/birch-edge-of-sentience-and-the-five-tier-scale/) L88,
**gets it right** and supplies the canonical form — it quotes *"realistic possibility of
sentience... that it would be irresponsible to ignore"* verbatim, with the qualifier intact, and
uses "non-negligible" only as its own clearly-marked gloss on the probability flavour. The other
four loci (`amplification-mechanisms-consciousness-physics`,
`reinforcement-learning-reward-signals-and-machine-valence`,
`apex/post-decoherence-selection-programme`, `archive/stochastic-amplification-and-neural-selection`)
use "non-negligible" in unrelated senses — criticality probability, AI-welfare precaution — and
none attributes it to Birch. **Not a family defect.** The corpus otherwise uses Birch's real term
of art: `realistic possibility` appears in 20+ live articles.

**Fix applied** — aligned with the sibling's canonical wording, **word-neutral (71 → 71 words)**:

> Birch (2024) sets a deliberately inclusive bar—a "sentience candidate" is a system whose
> evidence base implies "a realistic possibility of sentience... that it would be irresponsible
> to ignore"—and presses exactly where this article stops, at "very low rather than exactly
> zero". The bar is still not met: candidature also requires evidence rich enough to identify a
> welfare risk and design a precaution around it, which the planarian case does not supply.

Provenance-checked before rewriting: `git log -S non-negligible` shows the phrase entered this
file in `e9bc8e5d86` (2026-09-09 refine that installed the rival-criteria section). It is not a
guard installed by any review.

### Medium Issues Found

**2. "Levin separates this from panpsychism" understates his self-location (FIXED, +2 words).**

TAME's sentence is *"**Unlike other panpsychist views**, TAME does not claim that mind is
inevitably baked in regardless of physical implementation or structure."* Levin is distinguishing
TAME from *other members of the panpsychist family*, not from panpsychism as such. The article's
"separates this from panpsychism" reads him as standing outside the family — which runs in
exactly the co-optation direction the 2026-09-09 outer reviews flagged (understating Levin's
phenomenal commitments). Changed to "separates this from **other panpsychist views**". The
article's existing rebuttal ("that distinction concerns *which* systems qualify") is unaffected
and now sits on an accurate premise.

### Low Issues Found

**3. "the same sentence promises to 'return to this issue at the end'" (FIXED, word-neutral).**

In TAME the bracketing announcement and the promise are **consecutive sentences**, not one:
*"…not on phenomenal or access consciousness [in the sense of the "Hard Problem" (Chalmers,
2013)]. **However, I return to this issue at the end**, discussing…"* Changed "the same sentence"
→ "the next sentence".

### Non-findings (checked, article is correct)

- **"dramatically raise the replication yield"** (Kriegman 2021). Verified: spheroid progenitors
  max **2** rounds, AI-designed semitoroids max **4**; offspring diameter **+149%** (P < 0.05).
  The intensifier is defensible. The paper's own term is "semitorus/semitoroid"; `"C"-shape` is
  verbatim from the Fig. 2A caption ("asymmetrical semitoroid (C-shape; pink)"). "Pac-Man-like"
  is the article's own unquoted gloss for a semitorus with a single narrow mouth — accurate, and
  original to the expand-topic commit `3fd3f788ba`, not a review guard.
- **Butlin "five theories"**. Mildly loose — the AE-1 agency indicator is *not* derived from the
  five named theories but from a separate agency/embodiment category ("supported by midbrain and
  UAL theories, and to some extent by GWT, PRM and PP"). The claim "their list does include
  agency" is true and the abstract does name five theories. Left unchanged; not worth the churn.
- **"very low rather than exactly zero"** at L87 is the *article's own* phrase (self-quote from
  L77), not attributed to Birch. Reads correctly in context.

## §2.4 Publisher-of-Record Citation Web-Verify — per-cite ledger

`WebSearch` was exhausted (200/200) for the session; **all verification below was done by direct
fetch of raw source text and grep**, never via a summariser. Sources: EuropePMC full-text XML,
arXiv PDF, OAPEN OA book PDF, OSF preprint PDF, Crossref, live publisher pages.

**Metadata (12 DOIs resolved at Crossref / EuropePMC):**

- Levin 2022, TAME, *Front. Syst. Neurosci.* 16, 768201 — **real-correct** (PMC8988303, PMID 35401131)
- Levin 2019, *Front. Psychol.* 10, 2688 — **real-correct** (Crossref; title incl. the "Self" quotes)
- Kriegman et al. 2020, *PNAS* 117(4) 1853–1859 — **real-correct** (PMC6994979, PMID 31932426; author order exact)
- Kriegman et al. 2021, *PNAS* 118(49) e2112672118 — **real-correct** (PMC8670470)
- Durant et al. 2017, *Biophys. J.* 112(10) 2231–2243 — **real-correct** (PMC5443973; six authors, order exact)
- Pai et al. 2012, *Development* 139(2) 313–323 — **real-correct** (research-article DOI, not the corrigendum; fix from `79e432051d` holds)
- Fields, Glazebrook & Levin 2021, *Neurosci. Conscious.* 2021(2) niab013 — **real-correct** (PMC8327199)
- Blackiston et al. 2021, *Sci. Robotics* 6(52) eabf1571 — **real-correct** (PMID 34043553; six authors, order exact)
- Bischof et al. 2020, *Dev. Biol.* 467(1-2) 51–65 — **real-correct**
- Grodstein & Levin 2022, *Bioelectricity* 4(1) 18–30 — **real-correct**
- Lyon, Keijzer, Arendt & Levin 2021, *Phil. Trans. R. Soc. B* 376(1820) 20190750 — **real-correct** (PMC7935032; four authors, order exact)
- Chis-Ciure & Levin 2025, *Synthese* 206(5) 257 — **real-correct** (Crossref; issued 2025-11-06)
- Laukkonen, Friston & Chandaria 2025, *Neurosci. Biobehav. Rev.* 176, 106296 — **real-correct** (Crossref: Ruben Laukkonen, Karl Friston, Shamil Chandaria). Note the OSF preprint `daf5n` has only **two** authors (Laukkonen & Chandaria); the article correctly cites the three-author published version.
- DiFrisco & Gawne 2025, *J. Evol. Biol.* 38(2) 143–156 — **real-correct**
- Butlin, Long et al. 2023, arXiv:2308.08708 — **real-correct** (v3, 22 Aug 2023; Birch confirmed in the author list, which is what the article's "not two independent votes" claim rests on)
- Birch 2024, *The Edge of Sentience*, OUP — **real-correct** (OA, DOI 10.1093/9780191966729.001.0001)
- Seth 2021, *Being You*, Dutton — **metadata correct; characterisation not verbatim-verified this pass** (no quoted material attributed to it, so no quote-fidelity exposure). See Remaining Items.

**Quote fidelity — 21 quoted spans grep-verified in raw source:**

*Levin 2022 (TAME), EuropePMC full text, all 10 verbatim:*
- "is definitely incompatible with binary views that cut off consciousness at a particular sharp line" — **verbatim**, subject "TAME" preserved
- "the focus of most of the discussion below is on ways to think about cognitive function, not on phenomenal or access consciousness" — **verbatim**
- "return to this issue at the end" — **verbatim** (but see Low issue 3 on which sentence)
- "accompanies specific types of cognitive processes which exert energy toward goals" — **verbatim**; source subject is "consciousness", and the article's "Consciousness, on that account, …" preserves it (checked against the predicate/subject-splice trap)
- "no principled way to restrict consciousness to 'human-like, full-blown sophisticated brains'" — **verbatim**; source uses double quotes for the inner phrase, article correctly switches to single for nesting
- "suggests that whatever consciousness is, some variant and degree thereof has to be present very widely across autopoietic systems" — **verbatim**
- "contains a true '0' or only infinitesimal levels for very modest agents" — **verbatim** (same nesting convention; contiguous span, the elided "of cognition (and consciousness)" falls before the quote opens)
- "TAME does not claim that mind is inevitably baked in regardless of physical implementation or structure" — **verbatim**; *framing corrected* — see Medium issue 2
- "diverse intelligences" — **verbatim**
- "cognitive light cone" — **verbatim**

*Kriegman et al. 2020 (PMC6994979), all 3 verbatim:*
- "manually shaped by subtraction" — **verbatim**; the article's "microsurgery forceps and a cautery electrode" matches "microsurgery forceps and a 13-μm wire tip cautery electrode"
- "self-maintain their externally imposed configuration" — **verbatim**
- "emergent spontaneous coordination among the cardiac muscle cells" — **verbatim**; the article's "spontaneous aggregation of scattered debris" matches "spontaneously and collectively aggregate detritus littered within their shared environment", and "self-repair that automatically closes lacerations" matches "automatically closing lacerations"

*Others:*
- "stably override genome-default target morphology" (Durant 2017, PMC5443973) — **verbatim**; the article's "constant *ratio* of two-headed to normal" matches "a constant ratio of regenerates with two heads to regenerates with normal morphology"
- "arise by cellular self-organization and do not require scaffolds or microprinting" (Blackiston 2021) — **verbatim** in the publisher abstract; "navigate aqueous environments, heal after damage, and show emergent group behaviour" matches the abstract clause for clause
- "sensing/perception, memory, valence, learning, decision making, communication" (Lyon et al. 2021, PMC7935032) — **verbatim**; source prefixes "e.g.", and the article claims no exhaustiveness. "separately studiable" matches "each element of which can be studied relatively independently"
- "scale-free characterization of consciousness and cognition" + "from the molecular scale upwards" (Fields et al. 2021, PMC8327199) — **both verbatim**; joined from adjacent abstract sentences whose shared referent is the same minimal-physicalist approach. Fair join.
- "indicator properties" (Butlin et al. 2023, arXiv PDF) — **verbatim**
- "learning from feedback and selecting outputs so as to pursue goals, especially where this involves flexible responsiveness to competing goals" (Butlin AE-1) — **verbatim** modulo sentence-initial capital L, lowercased for mid-sentence integration
- "sentience candidate" (Birch 2024) — **verbatim**; the surrounding gloss was not — see Critical issue 1
- "pressure points" and "real"/"as-if" goals (Levin & Dennett, Aeon) — **verbatim; see below**

**§2.4 step 7, result-direction / null-result leg.** Ran on every empirically cited paper. No
inversions found. Specifically: Durant's two-headedness is a *constant ratio*, not full
penetrance, and the article says so; Pai's ectopic-eye yield is a *minority* (~20% partial /
7.5% complete) and the article says so; Kriegman 2021's yield gain is 2→4 rounds and +149%
diameter, consistent with "dramatically raise"; **DiFrisco & Gawne's direction is exactly as the
article reports** — the abstract reads "We show that this idea is theoretically **unsound**",
"**no empirical evidence** that the agency perspective has the potential to advance experimental
research", and the phenomena "are **better explained** using the well-established idea that
complex multiscale feedback mechanisms evolve through natural selection". The article's "Their
target is the thesis that agency resists explanation by mechanism or selection" matches the
abstract's "Proponents … have claimed that agency is not explainable by physiological or
developmental mechanisms, or by adaptation via natural selection" **exactly**.

**§2.4 step 8, cited-author-stance leg.** Discharged by the 2026-09-09 repairs and re-checked
here. Levin's stance is stated *against* the Map throughout (lede: "drawn against Levin rather
than with him"; "Levin's programme therefore supplies measured competency plus an inference the
Map rejects"; Rouleau & Levin's multiple-realizability-of-sentience position named as "his own"
and as "a live rival"). Dennett's intentional stance is used descriptively and flagged as "an
instrumentalist licence for agency-talk that pointedly does *not* smuggle in phenomenality".
Laukkonen et al. are explicitly noted to "cut against the Map". No author is presented as
endorsing the Map's conclusion.

**§2.4 step 4, empirical-record currency sweep.** `find_superlative_claims` returns **empty** —
no superlative claims to age-check. (Kriegman 2021's "distinct from any known animal or plant
reproduction" is the source's own framing and remains current.)

**Reference 15 parenthetical — verified, no change needed.** The article notes "(A 2025 *Trends
in Cognitive Sciences* version adds further authors including D. Chalmers.)" **Confirmed** at
Crossref: *"Identifying indicators of consciousness in AI systems"*, **DOI
10.1016/j.tics.2025.10.011**, 20 authors — Butlin, Long, Bayne, Bengio, Birch, **Chalmers**,
Constant, Deane, Elmoznino, Fleming, Ji, Kanai, Klein, Lindsay, Michel, Mudrik, Peters,
Schwitzgebel, Simon, VanRullen. Recorded here because **the journal version has a different
title from the arXiv preprint**, which is exactly the shape that generates future false
"cannot find it" reports. Print issue is 2026-06; the DOI and online-first are 2025, so "2025"
is defensible.

## Owed item from 2026-08-03 — DISCHARGED

The 08-03 review left one Remaining Item: verbatim-verify `"pressure points"` against the
Levin & Dennett Aeon essay, and confirm the hard-linked URL slug resolves. It was blocked then
by aeon.co HTTP 429 and an exhausted WebSearch budget; the research note later closed it against
Internet Archive captures only.

**Closed this pass at the live publisher.** `aeon.co` returned **HTTP 200** for the exact slug in
Reference 3 (37.5k chars of body, title *"How to understand cells, tissues and organisms as
agents with agendas | Aeon Essays"*, byline "Michael Levin & Daniel C Dennett", dated
**13 October 2020** — matching Reference 3's "(2020, Oct 13)"). Grep of the raw page:

- **"pressure points" — verbatim.** Source: *"…this kind of teleophobia significantly holds back
  the ability to predict and control complex systems because it prevents discovery of their most
  efficient internal controls or pressure points."* The article states the contrapositive
  (attributing goal-directedness *reveals* them); faithful.
- **"real" / "as-if" goals — verbatim.** Source: *"We reject a simplistic essentialism where
  humans have 'real' goals, and everything else has only metaphorical 'as if' goals."* The
  article hyphenates "as-if"; the essay uses both `'as if' goals` and `'as-if' cognition`, so the
  hyphen is an orthographic variant the source itself licenses. No defect.

## Second lens — research-note compression diff — CLEAN

Diffed the article's factual and attributional claims against
[the source research note](/research/basal-and-bioelectric-cognition-levins-morphogenetic-agency-and-xenobots-2026-07-08/)
in the note → article direction, looking for places where the note is *more* discriminating than
the prose. **Found none. The gradient runs the other way throughout** — the article is uniformly
more careful than the note it was written from:

- Note: planaria "continue producing two-headed **offspring**". Article: "**regenerates**" —
  correct, and the paper never uses "offspring" (fixed in `1008007ebe`).
- Note: "Reversible with ion-channel/pump modulation — the memory **is** a stable attractor state
  of the voltage circuit." Article: resettable "**though stochastically**", and "*Stable
  attractor* is a **model** of the voltage circuit (Grodstein & Levin 2022), **not a demonstrated
  mechanism**."
- Note: Pai induces "well-formed *ectopic* eyes". Article adds the minority yields (~20% partial,
  7.5% complete with RPE, retina and lens).
- Note's central "Map-critical point" — *"**Levin explicitly brackets phenomenal sentience**"* —
  has been **reversed** in the article, correctly, following the 2026-09-09 outer reviews. The
  note is now stale against the article; that is the healthy direction and no article change is
  owed.
- The note's own flagged gap ("Critics: only lightly sampled… a balanced article should cite a
  peer-reviewed critical treatment, not just popular pushback") is **discharged** — DiFrisco &
  Gawne 2025 is now cited and, per the ledger above, correctly characterised.

## §2.6 Reasoning-mode classification (editor-internal)

- **Levin / TAME gradualism — Mode Three (framework-boundary marking).** The article declines the
  phenomenal inference and says so plainly ("takes the measurements and declines the inference"),
  without claiming to refute Levin inside his own framework. Honest.
- **Laukkonen, Friston & Chandaria — Mode Two (unsupported foundational move).** "All three
  conditions are conditions on representational structure, and the step from structure so
  organised to anything felt is assumed rather than argued." Correctly declines to claim victory:
  "leaves a debt, not a refutation."
- **Butlin et al. — Mode Three.** "the method returns this article's verdict on grounds Tenet 1
  rejects" — boundary marked.
- **Birch — Mode One (defective on its own terms / in-framework).** The article argues from
  Birch's *own* condition (b). This is the strongest available mode and, after the fix, rests on
  his actual wording.
- **Seth — Mode One, correctly hedged.** Consistency pressure from Seth's own viability
  imperative reaching to the single cell; the article calls it "pressure rather than refutation".
- **DiFrisco & Gawne — absorbed, not opposed.** The article correctly notes their target is a
  thesis the Map never asserts, and that the deflation *strengthens* the decoupling.

**Label leakage: none.** All nine forbidden editor-vocabulary strings return 0.

## Optimistic Analysis Summary

### Strengths Preserved
- The 2026-09-09 co-optation repair is genuinely good work and was left untouched. The lede's
  "drawn against Levin rather than with him" is a rare instance of an article naming its own
  source as an opponent, and the TAME quote block that backs it is now fully verbatim-certified.
- The reference apparatus is, at the metadata layer, the cleanest this reviewer has measured:
  **15 of 15 externally-published cites resolved real-correct at the publisher of record, with
  zero corrections needed.** Author orders, volumes, issues, page ranges and DOIs all exact.
- Hardline-Empiricist-praised restraint is intact and structural rather than lexical: "decisive
  nowhere on their own, though not therefore worthless"; "very low rather than exactly zero";
  "a claim about what such language *fails* to show". The `anchoring_audit_exempt` note's
  reasoning still holds after this pass.
- "What the Decoupling Reaches, and What It Does Not" is the section doing the most work — it
  volunteers four criteria the argument does *not* defeat, two of which it concedes are not
  competency criteria at all. The Birch fix makes that concession *stronger*, because it now
  turns on Birch's real condition (b) rather than an imported negligibility threshold.

### Enhancements Made
- Critical fix 1 replaces an invented threshold with Birch's own words and brings the article
  into line with the Map's dedicated Birch article — a corpus-consistency gain as well as a
  fidelity one.
- Medium fix 2 removes the last residue of the co-optation pattern the outer reviewers flagged:
  Levin is no longer positioned outside panpsychism.

### Cross-links Added
None. The 07-16 sibling-cluster links plus the 2026-09-09 rival-criteria additions saturate the
relevant connections; the Further Reading block already carries 12 targets.

## Remaining Items

- **Seth 2021 (*Being You*) characterisation not verbatim-verified.** The article attributes to
  Seth a grounding of selfhood in "predictive control of the body's own viability" and a lean
  "without committing" toward consciousness being possible only in living things. No quoted
  material is attributed, so there is no quote-fidelity exposure, but the *characterisation* rests
  on an unverified reading. The book is not open access and was not fetchable this pass. Low
  priority; queue only if a Seth-focused pass comes up.
- **Butlin "five theories" / AE-1 provenance.** AE-1 is a separate agency-and-embodiment indicator,
  not derived from the five named theories. Declined as unaffordable-and-not-worth-the-churn at a
  4-word budget; a future length-neutral pass could tighten it.

## Stability Notes

- **The 2026-09-09 outer-review findings are discharged.** Eight refine commits repaired the
  co-optation firewall failure, the rival-criteria omissions, the "offspring"/"regenerates" error
  and the Pai corrigendum DOI. Future reviews must not re-flag "the article misrepresents Levin
  as bracketing sentience" — the article now argues the *opposite*, explicitly and in its lede.
- **The phenomenal/functional decoupling is bedrock**, rejected wholesale by eliminativist and
  hard-functionalist personas. Carried forward from 07-19 and 08-03; not a fixable flaw.
- **Quantum Skeptic and Many-Worlds personas have no purchase** — no quantum or branching content.
  Carried forward.
- **Lens ledger (convergence is per-lens, not per-visit).** Lenses now run on this file:
  external citation metadata (07-08, and again 09-21 at full strength), full persona/argument
  (07-19), inward citation-framing (08-03), quote fidelity — *partial* (08-03), **quote fidelity
  at the publisher of record — complete, 21/21 spans (09-21)**, **result-direction/null-result
  (09-21)**, **research-note compression diff (09-21)**, **reasoning-mode + label leakage (09-21)**.
  The 08-03 review's warning that damping should damp *repeat lenses, not repeat visits* is
  vindicated again: this pass was the fourth visit and still found a critical issue — because the
  defect lived in material created *after* the third visit.
- **`"non-negligible"` is not Birch's word.** If it reappears anywhere as a gloss on the
  sentience-candidate bar, that is a regression. The canonical form is the one in
  [birch-edge-of-sentience-and-the-five-tier-scale](/topics/birch-edge-of-sentience-and-the-five-tier-scale/) L88.
- The valence-currency framing remains pinned to [value-in-selection](/positions/value-in-selection/) [P-VS1](/positions/value-in-selection/#p-vs1)
  (credence low, grade D). If that position's calibration moves, this article's L73 paragraph is
  a dependent locus and should move with it. Unchanged from 08-03.