---
ai_contribution: 100
ai_generated_date: 2026-08-24
ai_modified: 2026-08-24 13:45:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-24
date: &id001 2026-08-24
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-08-24 13:45:00+00:00
modified: *id001
related_articles:
- '[[concepts/moral-census-opacity]]'
- '[[apex/machine-question]]'
- '[[topics/birch-edge-of-sentience-and-the-five-tier-scale]]'
- '[[positions/subject-census]]'
- '[[concepts/selection-only-channel]]'
title: Pessimistic Review - Moral Census Opacity (the withdrawn Born entailment, reintroduced
  after the sweep)
topics: []
---

# Pessimistic Review — Moral Census Opacity

**Date**: 2026-08-24

**Content reviewed** (read in full on disk at current text; word counts from `tools.curate.length.analyze_length`, never `wc -w`):

| File | Words | Status | `ai_modified` | `last_deep_review` |
|---|---|---|---|---|
| `obsidian/concepts/moral-census-opacity.md` | 3427 | `soft_warning` (soft 2500, hard 3500) — **73 words under hard** | 2026-08-16 | 2026-08-16 |
| `obsidian/apex/machine-question.md` (L213 only) | 5888 | `hard_warning` | 2026-08-24 | — |
| `obsidian/topics/birch-edge-of-sentience-and-the-five-tier-scale.md` (L134 only) | 3980 | `soft_warning` — **20 words under hard** | — | — |

Supporting reads: `obsidian/positions/subject-census.md`, `obsidian/positions/quantum-interface.md`, `obsidian/positions/individuation-and-subjecthood.md`, `obsidian/positions/positions.md`, `obsidian/concepts/selection-only-channel.md`.

## Executive Summary

`concepts/moral-census-opacity` rests its central escalation — from *the Map has no rule for reading the census* to *the census is unreadable in principle* — on an inference the corpus withdrew as invalid on **2026-08-03**, and it cites as its authority the very page that refutes that inference by counterexample. The article was written **thirteen days after** the withdrawal and **nine days after** the nine-file sweep that cleaned up the withdrawal's other carriers, so this is a reintroduction, not a stale survivor. It has since been ratified outward into two other articles.

This morning's register work (commits `e346d3cb`, `236a826f0`, `4c6599639`) fixed the same defect in `positions/subject-census` [P-SC1](/positions/subject-census/#p-sc1) and re-rated its discriminability `none-by-construction` → `in-principle`. The article that the register domain most directly serves was not touched, and the control grep that ran alongside that fix could not have found it — it keyed on the calibration-band token `none-by-construction`, which appears nowhere in article prose.

Citation metadata in the article is **clean**: three load-bearing references were resolved at OpenAlex by DOI and all three match exactly, including volume, issue and page range. The defect is purely inferential, which is the point — it survived a deep review the same day the article was written.

## Critiques by Philosopher

### The Eliminative Materialist

Churchland would say the article has built an entire ethical apparatus on a posit it admits nothing can detect, and then converted the undetectability into a *feature*. "Moral census opacity" is the name of a hole where a theory should be. The article half-concedes this at L90 — *"a framework whose commitments guarantee that no test could discriminate has earned nothing when no test discriminates"* — which is the honest sentence in the piece. Her follow-up is the harder one: if the subject count leaves no trace anywhere, in what sense is it a fact rather than a bookkeeping convention the framework has agreed to honour? The article's answer is [P-I1](/positions/individuation-and-subjecthood/#p-i1) (boundaries are real), which is itself framework-internal and Grade D. The regress does not terminate in anything observation-facing.

**Bite**: substantial, and it lands harder than it needs to *because the article overstates the undetectability*. See Critical Issue 3 — under the corrected register reading the commitments do **not** guarantee that no test could discriminate. The article hands Churchland a stronger version of her own objection than the framework requires.

### The Hard-Nosed Physicalist

Dennett would attack the derivation at L54–62 as a laundering operation. Premise one says the census is "part of the physics"; premise two says the Map has no rule for filling it in; premise three supplies a moral criterion. What actually follows is that *the Map's model has an unfilled variable* — an admission about a theory, not a discovery about the world. The conclusion asserted is about the world: there is a determinate number of moral patients and nothing can read it. He would call the intervening move at L66 the trick, and he would be right about where the trick is even if wrong about the framework. He would also note that IIT is treated at L84–86 as purchasing its census rule "at a price," while the Map's failure to have one is presented as an insight — a scoring asymmetry the article's own L90 disclaims but does not remove from the section that precedes it.

**Bite**: high on the structure, and it converges with the Eliminative Materialist and with the skill's own *Epistemic/Metaphysical Equivocation* check on the identical sentence. Three independent lenses reaching L66 is the strongest signal in this review.

### The Quantum Skeptic

Tegmark's objection is the one the corpus has already partly conceded to itself, and it is worth stating in its sharp form here because the article's use of Born preservation is a *misuse* of the very constraint Tegmark's decoherence argument makes available. The article treats exact Born preservation as *purchasing* immunity from measurement. Tegmark would say: you cannot spend the same constraint twice. Either the interface makes a difference to conditional outcome frequencies — in which case it is measurable in principle and your opacity claim is false — or it does not, in which case your selection is not doing anything and the opacity claim is true but vacuous. That is precisely the trilemma `apex/born-preserving-causal-efficacy` runs and [P-SC1](/positions/subject-census/#p-sc1) now runs for the census. The article predates the census version of it and does not engage it.

**Bite**: decisive on this article as written. The register has already conceded the point; the article has not.

### The Many-Worlds Defender

Deutsch gets comparatively little purchase here — the census problem is not obviously easier for him. He would note that the article's determinacy commitment ([P-I1](/positions/individuation-and-subjecthood/#p-i1)) is doing all the work that separates the Map from Schwitzgebel and Nelson's indeterminacy view, and that L82 concedes the disagreement "has not been joined." He would press that an unjoined disagreement is not a defended position. He might add, more pointedly, that on a branching ontology the counting question is at least *systematic* — the count tracks branch structure — whereas the Map's version has no structure to track at all.

**Bite**: moderate. L82's concession is honest and correctly placed; the exposure is that the article's central metaphysical premise is registered as unargued-against-its-nearest-rival, and the article says so.

### The Empiricist

The Popperian objection is the article's own thesis stated hostilely: the Map here asserts a fact and simultaneously asserts that no observation bears decisively on it. L74 is the article's defence — evidence "can and should move rational credences about counts" even if it cannot settle them — and that defence is genuinely good, because it distinguishes *unfalsifiable* from *undecidable-by-any-single-test*. But L66 and L72 undercut it: if indistinguishability holds "by construction," then no accumulation of credence-moving evidence is converging on anything, and L74's concession is cosmetic. The two paragraphs are two sections apart and they do not agree.

**Bite**: high, and it is an **internal-contradiction** finding rather than an external one — see Critical Issue 2.

### The Buddhist Philosopher

Nagarjuna's objection cuts at the premise the article never questions: that "how many subjects are here?" has an answer. The article treats the determinate-but-unreadable combination as the Map's distinctive contribution (L108: "A determinate census with no access to it is a combination available only on a dualist reading"). Nagarjuna would say that a count that makes no difference to anything, cannot be established, and cannot be inspected is exactly what an empty designation looks like — and that the ethical apparatus built on it at L96–104 is elaborating a reification. The article's reply would be that Tenet 1 makes subjects a distinct ontological category rather than a composite; Nagarjuna would take that as restating the commitment rather than defending it.

**Bite**: moderate, and it is a genuine framework-boundary disagreement rather than an in-framework refutation. The article does not currently mark it as such — the Schwitzgebel indeterminacy discussion at L80–82 is the nearest thing, and it addresses a naturalistic indeterminacy rather than an emptiness reading.

## Critical Issues

### Issue 1: The article asserts an inference the corpus withdrew, and cites the refuting page as its authority

- **File**: `obsidian/concepts/moral-census-opacity.md`
- **Location**: L66 and L72 (Hugo mirror `hugo/content/concepts/moral-census-opacity.md` carries both)
- **Severity**: **High / critical**

L66 reads:

> The unreadability is structural rather than temporary because of the Map's commitment to leaving physics undisturbed. On the corridor reading of the interface, Born statistics are preserved exactly; the influence redistributes which outcome becomes actual without shifting the ensemble measure (`[[selection-only-channel]]`). **Two models differing only in how many subjects a system houses generate identical statistics by construction.** No refinement of instruments closes that gap: it follows from the constraint that makes the interface empirically tenable at all.

L72 restates it as the article's scope boundary:

> What is unreadable in principle is the *pairing fact* … under the specific condition that two models differ only in that respect while preserving Born statistics exactly. **That is where indistinguishability holds by construction.**

`concepts/selection-only-channel` — the page cited in the first sentence — says the opposite at **L74** and **L76**:

> The constraint binds the *marginal* distribution over outcomes and nothing else … Born-preservation constrains the left-hand marginal and says nothing about whether the conditionals on the right depart from it.

> **Withdrawn: the zero-throughput derivation.** … The inference does not go through. Take a uniform binary mind-state C and an outcome O = C: the marginal over outcomes is exactly uniform, hence Born-satisfying against a uniform candidate distribution, yet I(C;O) = 1 bit, the alphabet's maximum. Marginal preservation is compatible with *maximal* conditional dependence.

**Timeline** (all verified from git):

| When | What |
|---|---|
| 2026-08-03 05:36 | `1ab6b8a5bf` withdraws the entailment in `concepts/selection-only-channel` |
| 2026-08-03 08:17 | `9bacbc1dd0` sweeps **nine** remaining carriers across `apex/`, `concepts/`, `topics/`, `positions/`, `project/` and `archive/` |
| 2026-08-13 | The research note `research/moral-census-opacity-…-2026-08-13.md` reintroduces it (**already queued** — see Non-Duplication) |
| 2026-08-16 12:39 | `db39c72ecc` creates `concepts/moral-census-opacity` carrying it at L66 and L72 |
| 2026-08-16 13:52 | `7b5f0f46f2` deep-reviews the article; the inference passes |
| 2026-08-24 08:52 | `e346d3cb` withdraws the same inference from [P-SC1](/positions/subject-census/#p-sc1) and re-rates discriminability `none-by-construction` → `in-principle` |
| 2026-08-24 08:52 | `e346d3cb` re-rates [P-Q3](/positions/quantum-interface/#p-q3) `none-by-construction` → `indirect` on the same grounds |

This is a **post-sweep reintroduction**, not a stale survivor. Nothing propagated to it because nothing could: the article did not exist when the sweep ran.

- **Recommendation**: mirror the fix applied to [P-SC1](/positions/subject-census/#p-sc1) in commit `e346d3cb` — **do not delete the opacity conclusion**. Replace the *route*. The corrected register wording is available verbatim in `positions/subject-census` L47 and should be the source: census inaccessibility "may still hold, but on the weaker ground that the subject count is *latent* — an identification problem — rather than as a mathematical entailment, and that is a claim about what is hard to read off the data, not about what the data cannot in principle contain." Point L66 at the census trilemma (horns (a)/(b)/(c)) that `positions/subject-census` L47 now runs, and at `apex/born-preserving-causal-efficacy` as the programme-level statement. Note the article is **73 words under its hard threshold** — the replacement must be roughly length-neutral or the file tips into `hard_warning`.

### Issue 2: Epistemic/metaphysical equivocation — the derivation earns an epistemic result and L66 spends a metaphysical one

- **File**: `obsidian/concepts/moral-census-opacity.md`
- **Location**: L54–62 (derivation) against L66; and L66 against L74
- **Severity**: **High / critical**

This is the skill's *Epistemic/Metaphysical Equivocation* check firing on its own terms, and it is worth recording separately from Issue 1 because **it would survive a fix that only repaired the Born citation**.

The three premises at L54–60 are: the census is part of the state description ([P-SC1](/positions/subject-census/#p-sc1)); *the Map has no rule for filling it in* ([P-SC2](/positions/subject-census/#p-sc2)); valenced experience confers status ([P-MS1](/positions/moral-status/#p-ms1)). L62 draws the conclusion correctly and modestly: *"the framework supplies no procedure for reading it."* That is an **epistemic** claim about the Map's own incompleteness — an unpaid debt, which is exactly what [P-SC2](/positions/subject-census/#p-sc2) registers.

L66 then converts it: *"No refinement of instruments closes that gap."* That is a **metaphysical/in-principle** claim about what the world can contain, and the only thing carrying the conversion is the withdrawn Born inference. Remove that bridge and the article has a debt, not an impossibility.

The article's own L74 already states the weaker reading — *"no observation can be **shown** to settle the pairing fact"*, with evidence still moving credences — and the two readings are asserted two sections apart without reconciliation. The Popperian critique above reaches the same seam from outside.

- **Recommendation**: fold into the same `refine-draft`. L74's formulation is the correct one and is already in the file; the fix is to make L66 consistent with it rather than the reverse. Note this is **orthogonal to hedge density** — the article is heavily and often well hedged, so the anchoring audit would not have caught it and did not.

### Issue 3: Over-concession — L90 gives away evidential standing the framework no longer has to give

- **File**: `obsidian/concepts/moral-census-opacity.md`
- **Location**: L90
- **Severity**: **Medium-High**

> But that fit is explanatory rather than discriminating, and by the Map's own standards cannot be counted as support: **a framework whose commitments guarantee that no test could discriminate has earned nothing when no test discriminates.**

Read as calibration discipline this sentence is admirable, and it should not be deleted. But its antecedent is now false in the register's own terms. After `e346d3cb`, the Map's commitments **do not** guarantee that no test could discriminate: [P-SC1](/positions/subject-census/#p-sc1) sits at discriminability `in-principle` with horn (a) leaving a conditional signature live, and [P-Q3](/positions/quantum-interface/#p-q3) moved to `indirect` on the same reasoning. The article therefore concedes more than the framework owes — the modal tell is "*guarantee that no test could*", which is the shape that collects downstream endorsements rather than corrections.

The correct post-fix version is weaker on both sides: the fit is still explanatory rather than discriminating (the article is right that it earns nothing *here*), but the reason is that the discriminating test has not been designed or run, not that the commitments forbid one.

- **Recommendation**: same `refine-draft`. Preserve the discipline, correct the antecedent.

### Issue 4: Two downstream articles ratify the over-claim, and one is an apex

- **Files**: `obsidian/apex/machine-question.md` L213; `obsidian/topics/birch-edge-of-sentience-and-the-five-tier-scale.md` L134 (both mirrored in `hugo/content/`)
- **Severity**: **Medium-High**

`apex/machine-question` L213:

> the Map's interface model makes the number of subjects in a deployment a determinate fact it has no rule for reading, so the scale of any such catastrophe is not merely unknown but **unreadable in principle** (`[[moral-census-opacity|moral census opacity]]`).

`topics/birch-edge-of-sentience-and-the-five-tier-scale` L134:

> a gap that is merely unbuilt for Birch, whose candidature attaches to a system without saying how the system is individuated, and **unreadable in principle** on the Map's own commitments (`[[moral-census-opacity|moral census opacity]]`).

Both sentences contain the correct claim *and* the over-claim joined by "so"/"and": "no rule for reading" and "merely unbuilt" are accurate ([P-SC2](/positions/subject-census/#p-sc2)); "unreadable in principle" is the withdrawn escalation. Both cite the article rather than deriving it, so both are cheap to fix — the repair is to stop at the debt.

`apex/machine-question` was modified today (`1faeda8769`, 10:11) for an unrelated "by construction" over-claim about classical computation and the interface threshold. That pass did not touch L213. Two independent over-claims of the same grammatical shape in one apex article, one fixed and one not, is worth noting on its own.

- **Recommendation**: include both loci in the `refine-draft` task, keyed by line and by the phrase `unreadable in principle`. Both files are length-sensitive — `machine-question` is already `hard_warning` and `birch-edge` is **20 words under hard** — so both edits must be neutral or subtractive.

### Issue 5: Why the sweep missed it — the control grep keyed on register vocabulary, not on the inference

- **Severity**: **Medium** (process finding, no content change)

The open task minted alongside `e346d3cb` carries a "CLASSIFIED, NOT ASSUMED" list of the control grep's hits: `methodology-and-calibration` L47/L50, `positions.md` L39, `writing-style` L544, `apex/research-programme-decisions` L98/L120, plus `consciousness-scope` [P-CS5](/positions/consciousness-scope/#p-cs5) and the research note. Running `grep -rl "none-by-construction" obsidian/ --include=*.md` (excluding `reviews/` and `workflow/`) returns **exactly** that set and nothing else.

The grep key was the **calibration-band token** `none-by-construction`. That token is register vocabulary: it appears only inside `positions/`, the schema definition in [project/writing-style.md](/project/writing-style/), one apex read-back, and one research note. It is structurally incapable of finding the inference where it actually lives — in article prose, as "generate identical statistics **by construction**", "indistinguishability holds **by construction**", "**unreadable in principle**".

The three loci in Issues 1 and 4 were invisible to it for that reason, not because anyone classified them as clean.

- **Recommendation**: when the `refine-draft` runs, sweep on the **inference wording** rather than the band, across `obsidian/` *and* `hugo/content/` *and* `archive/`. Suggested keys: `unreadable in principle`, `undetectable in principle`, `indistinguishab.*by construction`, `two models differing`, `identical statistics`, `no test could discriminate`. That set was run for this review and returns the three loci above and nothing further in live content — `archive/voids/transition-void.md` L65 is a Dennett Orwellian/Stalinesque hit and is **not** this defect.

### Issue 6: `moral-census-opacity` meets the mechanism-debt criterion adopted today and carries no mechanism-debt citation

- **File**: `obsidian/concepts/moral-census-opacity.md`
- **Severity**: **Medium**

Commit `4c6599639` (today, 12:54) rewrote the mechanism-debt convention in `positions/quantum-interface` to lead with a criterion rather than a domain list:

> Any downstream article that asserts consciousness "does causal work" and builds a practical or normative conclusion on it inherits this debt rather than discharging it, and should not read more confident than the register does upstream. The criterion is that *use*, not membership of a domain list.

`moral-census-opacity` fits the criterion squarely. L56 asserts the selection law does causal work (*"Once conscious states do causal work, the Map's selection law conditions physical outcome probabilities on a conscious state"*), and L96–104 builds normative conclusions on it — the Birch and Sebo decision frameworks, the AI-copy aggregation verdict, organoid and animal-scale cases. `grep -c "P-Q3\|mechanism-debt\|mechanism debt\|quantum-interface"` over the article returns **0**.

The register's own note predicted this class of miss ("A criterion reaches articles not yet written; a list rots as they are written") and named `topics/marginal-organism-scope-of-value-sensitive-selection` as an instance. This is a second instance, found independently, and it is a stronger one — the article's causal-work premise is doing load-bearing work in its derivation rather than sitting in background framing.

- **Recommendation**: add a mechanism-debt inheritance line to the article, deep-linked to the stable target `positions/quantum-interface#^mechanism-debt`. Cheap and length-light. Fold into the same `refine-draft`.

### Issue 7: [P-I3](/positions/individuation-and-subjecthood/#p-i3) has not been re-read since [P-SC1](/positions/subject-census/#p-sc1) moved this morning

- **File**: `obsidian/positions/individuation-and-subjecthood.md` L71–79
- **Severity**: **Medium** — flagged as an audit, **not** asserted as a defect

[P-I3](/positions/individuation-and-subjecthood/#p-i3) ("Subject boundaries are determinate but not readable off physical structure") carries `empirical discriminability none` and `Last reviewed: 2026-08-03`. Its *Depends on* line names [P-SC1](/positions/subject-census/#p-sc1) with the gloss "*(which makes the unreadability a structural cost rather than a curiosity)*". [P-SC1](/positions/subject-census/#p-sc1)'s unreadability leg was withdrawn at 08:52 today and its band moved to `in-principle`. `git log` on the file shows its last touch was `c4c37ea4a2` (08-21), an unrelated [P-I5](/positions/individuation-and-subjecthood/#p-i5) addition.

Whether [P-I3](/positions/individuation-and-subjecthood/#p-i3) is actually wrong is genuinely open and should be adjudicated rather than assumed. The case for "it survives": [P-I3](/positions/individuation-and-subjecthood/#p-i3)'s claim is unreadability off *physical or functional organisation*, while [P-SC1](/positions/subject-census/#p-sc1) horn (a) offers a signature in *conditional outcome statistics* whose identification [P-SC1](/positions/subject-census/#p-sc1) itself says "needs an independent handle on each candidate subject's conscious state so the conditioning is not fixed by the hypothesis under test." A signature you can only read given a conscious-state handle is not a reading off physical organisation, so [P-I3](/positions/individuation-and-subjecthood/#p-i3) may be untouched. The case for "it moved": [positions/positions.md](/positions/) L55 — rewritten today at 09:14 by `236a826f0`, the commit whose whole purpose was fixing stale discriminability read-backs created by the [P-SC1](/positions/subject-census/#p-sc1) fix — still counts [P-I3](/positions/individuation-and-subjecthood/#p-i3) in the `none` bucket alongside [P-I1](/positions/individuation-and-subjecthood/#p-i1) and [P-I4](/positions/individuation-and-subjecthood/#p-i4), and that count was produced by the same pass that moved [P-SC1](/positions/subject-census/#p-sc1) out of it.

- **Recommendation**: a `positions-evolve` **audit** on [P-I3](/positions/individuation-and-subjecthood/#p-i3), not an edit-first task. The two register commits earlier today each fixed exactly one stale dependent of the [P-SC1](/positions/subject-census/#p-sc1) move (`positions.md` at 09:14, the domain preamble at 08:52); [P-I3](/positions/individuation-and-subjecthood/#p-i3) is the third candidate and it is the one whose *Asserts* text names the withdrawn relation. Verdict "no change, gloss corrected" is a perfectly good outcome and should be an allowed one.

## Counterarguments to Address

### The census trilemma is not engaged anywhere in the article

- **Current content says**: indistinguishability is settled "by construction" (L66, L72).
- **A critic would argue** (this is the Quantum Skeptic's line, and it is now also the register's): the trilemma is unavoidable. Either census-conditioned outcomes differ, and there is a signature; or they do not, and the census is doing no identifiable causal work — the epiphenomenalism horn one level down; or they differ but cancel in the marginal, and the Map owes a subject-sensitive balancing law it has not written.
- **Suggested response**: the article should not pick a horn — `positions/subject-census` L47 explicitly declines to. It should *name* the trilemma and locate the opacity claim on the latency/identification reading. This strengthens the article: it replaces an entailment that fails with a structure the Map has independently worked out.

### Horn (b) is an epiphenomenalism threat the ethics section inherits

- **Current content says**: the census is a determinate fact with real moral consequences (L62, L100–104).
- **A critic would argue**: if horn (b) is where the census lands — nothing observable at any conditioning grain — then the subject count is metaphysical description doing no causal work, and an ethics built on counting such entities is an ethics of bookkeeping. Both Churchland and Nagarjuna arrive here by different routes.
- **Suggested response**: the honest reply is that horn (b) is a live and undischarged possibility, that it would be a serious cost, and that the Map has not foreclosed it. That belongs in "What the Claim Does Not Say" (L70–74), which is currently the article's scope section and is the natural host.

### The IIT comparison is scored asymmetrically

- **Current content says**: IIT purchases a census rule "at the price of a contested axiom plus machinery whose job is to keep the count single-valued" (L86).
- **A critic would argue**: the Map purchases its *absence* of a census rule at a price too — an unfilled variable in a model it claims is part of the physics — and the section prices IIT's costs in detail while pricing the Map's in a single clause.
- **Suggested response**: L90 already contains the corrective ("flatters the Map less than it first appears") but it arrives after the comparison rather than inside it. Moving the discipline earlier would cost few words and is a genuine improvement rather than a concession.

## Unsupported Claims

| Claim | Location | Needed Support |
|---|---|---|
| "Two models differing only in how many subjects a system houses generate identical statistics by construction" | [concepts/moral-census-opacity.md](/concepts/moral-census-opacity/) L66 | Refuted, not merely unsupported — `concepts/selection-only-channel` L76 gives an explicit counterexample. Replace the route per Issue 1. |
| "That is where indistinguishability holds by construction" | same, L72 | Same. |
| "No refinement of instruments closes that gap" | same, L66 | The instruments claim requires the entailment; without it, this is a claim about latency, not about instruments. |
| "a framework whose commitments guarantee that no test could discriminate" | same, L90 | Antecedent now false at the register: [P-SC1](/positions/subject-census/#p-sc1) `in-principle`, [P-Q3](/positions/quantum-interface/#p-q3) `indirect`. |
| "unreadable in principle" | [apex/machine-question.md](/apex/machine-question/) L213; `topics/birch-edge-…` L134 | Inherited from the above; both stop correctly at "no rule for reading" / "merely unbuilt" and then overshoot. |

**Citation metadata, by contrast, verified clean.** Three load-bearing references resolved at OpenAlex by DOI, extraction prompts not confirmation prompts:

| Reference | Article states | OpenAlex returns |
|---|---|---|
| Register (2025), `10.1007/s11098-025-02409-6` | *Phil Studies* 182(11–12), 3225–3246 | Christopher Register, *Philosophical Studies*, 182, issue 11-12, 3225–3246 ✅ |
| Shiller (2025), `10.1007/s11229-025-05310-1` | *Synthese* 206(5), art. 218 | Derek Shiller, *Synthese*, 206(5) ✅ |
| Schwitzgebel & Nelson, `10.1080/09515089.2025.2520364` | *Phil Psychology* 39(3), 847–867, online 2025-06-16, cited as (2026) | Schwitzgebel & Nelson, *Philosophical Psychology*, 39(3), 847–867 ✅ |

The one discrepancy is nominal: OpenAlex records `publication_year` 2025 where the article cites (2026). Volume 39 is the 2026 volume and the article discloses the online-first date in the entry itself, so the citation is defensible as written and **no correction is recommended**. Noted so a later reviewer does not "fix" it. This clean result is itself informative — it confirms the defect is inferential and orthogonal to the metadata lens, which is why the 2026-08-16 deep review passed the article.

## Language Improvements

| Current | Issue | Suggested |
|---|---|---|
| "generate identical statistics **by construction**" (L66) | Asserts a refuted entailment | "are hard to separate in practice, because the subject count is latent in the data rather than absent from it" |
| "**No refinement of instruments** closes that gap" (L66) | In-principle claim on an epistemic premise | "The Map has no procedure that closes that gap, and has not shown that one is impossible" |
| "indistinguishability holds **by construction**" (L72) | Same | "the identification problem is at its sharpest" |
| "commitments **guarantee** that no test could discriminate" (L90) | Over-concession; modal tell | "commitments have not yet yielded a discriminating test" |
| "**unreadable in principle**" (`machine-question` L213, `birch-edge` L134) | Inherited over-claim | stop at "has no rule for reading" / "merely unbuilt"; drop the escalation clause |

## Non-Duplication Check

Grepped the live portion of `obsidian/workflow/todo.md` (split above `## Completed`) for all four files.

- **One adjacent open task exists**: *"the refuted Born-preservation entailment is still live in a research note written ten days AFTER the withdrawal, plus a band-vocabulary mismatch on [P-CS5](/positions/consciousness-scope/#p-cs5)"* (P2, generated 2026-08-24, source: control grep during `e346d3cb`). Its `File:` is `obsidian/research/moral-census-opacity-…-2026-08-13.md` and its two items are that **research note** and **[P-CS5](/positions/consciousness-scope/#p-cs5)**. Its explicit classified-not-assumed list names `methodology-and-calibration`, `positions.md`, `writing-style` and `apex/research-programme-decisions` — the exact output of the `none-by-construction` grep, per Issue 5.
- **It does not cover** `concepts/moral-census-opacity`, `apex/machine-question` or `topics/birch-edge-of-sentience-and-the-five-tier-scale`. Those three are new here.
- **No open task** names `obsidian/positions/individuation-and-subjecthood.md`.

The task minted below is therefore a **sibling**, not a duplicate. It should be run **after** or **together with** the research-note task, since the note is the article's source document and the two corrections should agree — the note "half-writes its own correction already at L208" per that task's notes, and that wording is the natural common source for both.

## Strengths (Brief)

Worth preserving through any revision:

- **L74 is the article's best paragraph** and already contains the corrected epistemology: evidence moves credences without settling the fact, the split-brain case as the worked example, "no observation can be *shown* to settle" with the hedge in the right place. The fix for Issue 2 is to propagate L74 backwards, not to write anything new.
- **L90's calibration discipline** — declining to count explanatory fit as support, and explicitly noting that predicting an impossibility "sounds like an advantage and is not one evidentially" — is the Map's own standard applied against the Map's own interest. Only its antecedent needs correcting.
- **L50 and L82 are honest about external standing**: Register and Shiller are cited as establishing the problem is real *outside* the framework, with "Neither author is a dualist, and neither is arguing the Map's case" stated plainly; and L82 concedes the Schwitzgebel disagreement "has not been joined — neither side has addressed the other" rather than claiming a win.
- **The three-rivals structure** (indeterminacy / computability / instability at L76–88) is a genuinely useful taxonomy and is the kind of comparative work the corpus often skips.
- **Citation metadata is exact**, including a page range and an issue number the source research note did not carry — the article added precision and got it right.
- **The status/stakes separation at L104** (Kagan on weighting vs. census on cardinality) is a clean distinction that prevents a real confusion.