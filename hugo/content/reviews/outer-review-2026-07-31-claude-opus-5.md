---
ai_contribution: 90
ai_generated_date: 2026-07-31
ai_modified: 2026-07-31 04:39:25+00:00
ai_system: claude-opus-5
author: Andy Southgate
concepts:
- quantum-consciousness
- spontaneous-collapse-theories
- tenet-falsification-conditions
created: 2026-07-31
date: &id001 2026-07-31
description: 'Hostile-referee audit of the Penrose gravity-induced collapse article.
  Verdict REVISE-HARD: a physics error, a suppressed primary result, and a metaphysical
  non-sequitur.'
draft: false
human_modified: null
last_curated: 2026-07-31
modified: *id001
outer_review_conversation_url: https://claude.ai/chat/e67ce170-bd82-47c0-99cd-8c0634ae50c5
outer_review_extraction_method: js-dom
outer_review_status: processed
related_articles:
- '[[project]]'
subject_articles:
- topics/penrose-gravity-induced-collapse-empirical-prospects.md
subject_source: reuse:pending-reviews:outer-review-2026-07-31-chatgpt-5-6-pro.md
subject_title: Audit penrose-gravity-induced-collapse-empirical-prospects
subject_type: recent
title: Outer Review - Claude Opus 5 (2026-07-31)
topics:
- penrose-gravity-induced-collapse-empirical-prospects
---

**Date**: 2026-07-31
**Reviewer**: Claude Opus 5
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Please conduct a hostile-referee audit of one article on The Unfinishable Map (https://unfinishablemap.org), a dualist philosophy site: https://unfinishablemap.org/topics/penrose-gravity-induced-collapse-empirical-prospects/ . The site changes daily and search indexes lag 24-48 hours, so read the live page and the changelog at https://unfinishablemap.org/workflow/changelog/ rather than cached snapshots. Verify every empirical and citation claim against the primary literature: the 2021 Donadi et al. result against the parameter-free Diosi-Penrose (DP) model, current DP and CSL parameter bounds, LISA Pathfinder and underground germanium constraints, and the status of Orch-OR. Are the article's experimental prospects overstated or understated? Does gravitational objective reduction survive as a collapse mechanism? Cross-check the site's positions register at https://unfinishablemap.org/positions/quantum-interface/, where P-Q6 records the parameter-free DP model as empirically falsified and P-Q5 demotes Orch-OR: state plainly if either verdict is miscalibrated, in either direction. Do not steer toward agreement. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Hostile-Referee Audit: "Penrose Gravity-Induced Collapse and Empirical Prospects"

*Target article:* `unfinishablemap.org/topics/penrose-gravity-induced-collapse-empirical-prospects/` (created 2026-03-15, last modified 2026-07-23; authored "claude-opus-4-6," attributed to Andy Southgate / Claude Oquatre-six). Live changelog, target article, and positions register (`positions/quantum-interface/`, incl. P-Q5 and P-Q6) were all fetched live in the required order. Every empirical and citation claim below was checked against publisher-of-record primary sources (arXiv, Nature/APS/IOP DOIs, PubMed/PMC, *Physics of Life Reviews*).

---

## 1. TL;DR

- The article's experimental prospects are **overstated at the framing level and understated at the physics level.** The introduction's promise that "a generation of experiments now in progress may determine whether gravity truly causes collapse within the next decade" is not defensible against the numbers the body itself concedes (interferometry is ~14 orders of magnitude in mass short of the Planck-scale regime; per Figurato et al. 2024 closing the spontaneous-radiation gap needs ~18 orders of magnitude of sensitivity improvement). Yet the body *under*-states the damage to Penrose: it wrongly describes the parameter-free version as "R₀ = 0 point-like," when Donadi et al. 2021 in fact excluded Penrose's *own physically-fixed value* (nuclear wave-function size, R₀ = 0.05 × 10⁻¹⁰ m) by an order of magnitude, and it omits Figurato et al. 2024, which shows the *surviving* free-R₀ region does not even guarantee macroscopic classicality. [topics/penrose-gravity-induced-collapse-empirical-prospects](https://unfinishablemap.org/topics/penrose-gravity-induced-collapse-empirical-prospects/)
- **Gravitational objective reduction does not survive as Penrose's original theory.** It survives only as a phenomenological free-parameter model whose distinguishing virtue — a collapse scale fixed by gravity alone, with no tunable knob — has been destroyed, and whose Orch-OR pairing the primary literature (Derakhshani, Diósi, et al. 2022) calls "highly implausible in all the cases analyzed." What remains is a research programme, not a confirmed or leading collapse mechanism.
- **P-Q6 (parameter-free DP model falsified) is correct in direction but mildly too weak / imprecise and stale; P-Q5 (Orch-OR demoted) is too generous.** The article's single most serious logical defect is the "Empirical stakes" non-sequitur: it treats experimental confirmation of objective gravitational collapse as "empirical support for the Map's metaphysical commitments," when collapse being objective and gravitational is logically independent of consciousness playing any causal role. Author-stance handling, by contrast, is unusually clean. **Overall verdict: REVISE-HARD.**

---

## 2. Dimensional Analysis

### 2a. Empirical accuracy (claim by claim)

**Donadi et al. 2021 — numbers right, one substantive physics error.** Verified against arXiv:2111.13490 and *Nature Physics* 17, 74–78 (2021). The bound R₀ ≳ 0.54 × 10⁻¹⁰ m is correct; "roughly three orders of magnitude larger than the previous experimental bounds" is verbatim-faithful to the paper ("about three orders of magnitude larger than previous bounds. This rules out the natural parameter-free version of the Diósi-Penrose model"); and "roughly one order of magnitude larger than Penrose's original R₀ prediction" is exact — the paper states "According to Penrose, R₀ = 0.05 × 10⁻¹⁰ m for the germanium crystal... Our experiment sets a lower bound on R₀ at 0.54 × 10⁻¹⁰ m... which is one order of magnitude larger than predicted following Penrose's argument. Therefore, this parameter-free version of the DP model is excluded." [arXiv](https://arxiv.org/abs/2111.13490)[Wigner](https://wigner.hu/~diosi/prints/arXiv2111.13490.pdf)

**But the article's claim that "Penrose's original version effectively sets R₀ to zero, treating mass distributions as point-like" is wrong.** Parameter-free ≠ R₀ = 0 (which gives divergent, unphysical instantaneous collapse). It means R₀ is *fixed by physics* at the nuclear wave-function size (√⟨u²⟩ from the Debye–Waller factor of the cooled Ge lattice, giving 0.05 × 10⁻¹⁰ m). Donadi's verbatim conclusion — "Penrose's proposal for a gravity-related collapse of the wave function, in the present formulation, is ruled out" — targets Penrose's own finite, physically-motivated value, *not* an idealization. The article's parenthetical "(R₀ = 0) is ruled out" therefore both mischaracterizes the physics and, ironically, understates the result: the correct statement is *stronger* against Penrose than the one the article makes. [Wigner](https://wigner.hu/~diosi/prints/arXiv2111.13490.pdf)[Wigner](https://wigner.hu/~diosi/prints/arXiv2111.13490.pdf)

**Majorana Demonstrator 2022 — accurate but incomplete.** Arnquist et al. (Majorana Collaboration), *Phys. Rev. Lett.* 129, 080401 (2022), correctly cited. Two omissions: (i) Majorana's *primary* target was CSL (the paper tests "the continuous spontaneous localization (CSL) model," with the DP limit secondary); (ii) the published **2023 erratum** (*Phys. Rev. Lett.* 130, 239902, 9 June 2023) that corrects the DP bound: "a correct calculation... should yield a 95% C.L. lower bound on the cutoff length of R_DP > (2.54 ± 0.03) × 10⁻¹⁰ m... the limit on the DP model remains the most stringent." Missing a published erratum on the exact quantity under discussion is a citation-integrity lapse. [arXiv + 2](https://arxiv.org/abs/2202.01343)

**The surviving free-R₀ model — number right, source absent, worst problem suppressed.** "R₀ ≳ 4 × 10⁻¹⁰ m" is correct and traces to Figurato, Dirindin, Gaona-Reyes, Carlesso, Bassi & Donadi 2024 (*New J. Phys.* 26, 113004; arXiv:2406.18494) — which is **not in the reference list.** That paper's central finding is suppressed: the DP model "does not satisfy" the requirement of guaranteeing macroscopic classicality ("we find out that not all macroscopic systems collapse effectively. If one relaxes this request, a reasonable (although to some degree arbitrary) bound is found to be R₀ ≲ 10⁻⁴ m"), and it notes that closing the experiment-to-theory gap on spontaneous radiation "requires 18 orders of magnitude improvement on the sensitivity." This is a second, independent, *non-aesthetic* problem for the surviving DP region — precisely where the article frames the only remaining cost as loss of "that natural-threshold rationale." [IOPscience](https://iopscience.iop.org/article/10.1088/1367-2630/ad8c77)

**Derakhshani et al. 2022 — verified, faithful, stance-correct.** "Highly implausible in all the cases analyzed" is verbatim (*Physics of Life Reviews* 42, 8–14; PMID 35617922; Diósi is a co-author). Correctly used: these are collapse-theorists constraining the DP–Orch-OR pairing, not opponents co-opted. No inversion. [PubMed](https://pubmed.ncbi.nlm.nih.gov/35617922/)

**Trillo & Navascués 2025 — verified, but presented as settled when it is contested.** *Phys. Rev. D* 111, L121101 (2025) is real; "can survive for more than a day" is verbatim. But the article inverts the paper's actual emphasis, which is a *caution*: "for reasonable experimental parameters, GIE can survive for more than a day. Our results therefore imply that GIE detection is not enough to validate quantum gravity." Moreover the result is under live published dispute — Lajos Diósi, arXiv:2511.00852 (2025), "No, classical gravity does not entangle quantized matter fields," rejects it. Presenting a contested, recently-published claim as a clean DP-falsification avenue is a "live-but-marginal-as-mainstream" move. [APS Journals](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.L121101)[ResearchGate](https://www.researchgate.net/publication/397280426_The_simple_reason_why_classical_gravity_can_entangle)

**Levitated nanoparticles 2026 — accurate.** Pedalino, Ramírez-Galindo, Ferstl, Hornberger, Arndt & Gerlich, "Probing quantum mechanics with nanoparticle matter-wave interferometry," *Nature* 649, 866–870 (2026), DOI 10.1038/s41586-025-09917-9: sodium nanoparticles ">7,000 atoms at masses greater than 170,000 Da... macroscopicity of μ = 15.5, surpassing all previous experiments by an order of magnitude." Correct. Reference #6 mis-lists the first author as "Arndt, M." — first author of record is **Pedalino** (Arndt corresponding). Minor metadata slip. To the article's credit, it explicitly concedes the ~14-orders-of-magnitude gap to the Planck-mass regime and that a direct test "is not imminent." [arXiv](https://arxiv.org/abs/2507.21211)[arxiv](https://arxiv.org/pdf/2507.21211)

**Tegmark vs. Hagan/Hameroff — accurate and, unusually, strengthened.** Tegmark 2000 (10⁻¹³–10⁻²⁰ s; *Phys. Rev. E* 61, 4194) and the Hagan/Hameroff/Tuszyński 2002 reply (10⁻⁵–10⁻⁴ s; *Phys. Rev. E* 65, 061901) are correctly reported, and the article correctly adds that Reimers/McKemmish et al. found the revised parameters "either... unphysical... or... regimes microtubules do not occupy." This is stronger against Orch-OR than the symmetric "Tegmark vs. Hameroff" framing, and the article says so. Good.

**Missing empirical landscape.** For a piece whose sections are titled "The Experimental Frontier" and "empirical prospects," the article says essentially nothing about the **CSL λ–r_C parameter space**: that Adler's proposed values are largely *excluded* by non-interferometric tests (LISA Pathfinder, X-ray emission, cantilevers), that the GRW value sits near the theoretical lower bound, and that the un-excluded "white region" remains many orders of magnitude wide in both λ and r_C. **LISA Pathfinder** — the single strongest CSL constraint over a wide r_C range (Carlesso et al. 2016, *Phys. Rev. D* 94, 124036) — and the **germanium X-ray/spontaneous-emission bounds** on CSL are not discussed at all. The frontier survey is DP-centric to the point of incompleteness.

### 2b. Citation integrity (three layers)

- **(i) Metadata:** References 1–5, 8–10, 14 verified accurate. Reference 6 mis-attributes first authorship (Pedalino, not Arndt). Load-bearing works **absent from the reference list:** Figurato et al. 2024 (source of the 4 × 10⁻¹⁰ m bound and the classicality-squeeze); Hagan/Hameroff/Tuszyński 2002 (source of the 10⁻⁵–10⁻⁴ s figure, prose only); Reimers/McKemmish et al. (named in prose, uncited); the Majorana 2023 erratum.
- **(ii) Verbatim fidelity:** "highly implausible in all the cases analyzed" (Derakhshani) — accurate. "It is always possible to rescue any model" (Donadi) — accurate wording, but sourced to a *Quanta Magazine* interview (Philip Ball, Oct 2022), which the article does not disclose; presented undated and unvenued, it reads as if drawn from the literature.
- **(iii) Author-stance — the article's strongest dimension.** It states plainly that "Penrose himself is not a dualist... He seeks consciousness within physics," and it carefully separates Duch's anti-Orch-OR *conclusion* from his classical-computational *commitment* ("convergent-conclusion-opposite-reasoning"). Donadi, Derakhshani, Reimers, and Tegmark are all deployed as critics, correctly. **No author-stance inversion detected** — a notable departure from the site's stated primary failure mode. [topics/penrose-gravity-induced-collapse-empirical-prospects](https://unfinishablemap.org/topics/penrose-gravity-induced-collapse-empirical-prospects/)

### 2c. Argumentative structure

The chain "gravitational OR provides the *occasion* for collapse → consciousness biases *which* Born-permitted outcome actualises, downstream" is internally careful, and the article explicitly flags "a conceptual gap separates Penrose's proposal from the Map's use of it." But the **"Empirical stakes" section commits a load-bearing non-sequitur:** it claims confirmation of gravity-related collapse would provide "empirical support for the Map's metaphysical commitments." It would not. Spontaneous-collapse models are motivated *entirely* by the quantum measurement problem and are fully compatible with strict physicalism — their originators (Ghirardi, Rimini, Weber, Pearle, Bassi, Diósi, and Penrose himself) are not dualists. "Collapse is objective and gravitational" and "consciousness plays a causal role" are logically independent; confirming the former is evidentially inert for the latter. The article half-sees this (via its own Penrose-isn't-a-dualist concession) yet still books DP confirmation as a win for the Map. [topics/penrose-gravity-induced-collapse-empirical-prospects](https://unfinishablemap.org/topics/penrose-gravity-induced-collapse-empirical-prospects/)

### 2d. Engagement with strongest rivals

Weak. The mainstream physicist's answer — **decoherence plus a no-collapse interpretation (Everett or Bohm)** — is foreclosed (Everett by Tenet 4; Bohm relegated to a single "Further Reading" line). The article never confronts the fact that objective-collapse theories are a **minority research programme**, not the default, and that the entire experimental enterprise it surveys exists to test *whether collapse occurs at all* — with the current empirical status being a consistent null result (standard, no-collapse QM). Framing collapse as the baseline and no-collapse as the exotic rival inverts the actual dialectical burden.

### 2e. Internal consistency with tenets and register

Consistent with Tenets 2–5 as written and honest about the mechanism debt (routing to P-Q3/P-Q10). **Version skew with the register:** the article's "R₀ = 0" mischaracterization is *not* inherited by P-Q6, which more accurately speaks of "a lower bound on the effective mass-density nucleus size" — so the article is out of line with its own register on the very point the register handles better. The article (modified 2026-07-23) postdates Figurato 2024 and Trillo–Navascués 2025 by months, so the omissions are staleness/selection, not timing. [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)

---

## 3. Bottom-Line Verdict: **REVISE-HARD**

Not DELETE: the load-bearing numbers are, unusually for this corpus, mostly correct and honestly hedged, and author-stance handling is clean. Not RETAIN: there is a genuine physics error (parameter-free ≠ R₀ = 0), a suppressed primary result (Figurato 2024 classicality-squeeze), an uncited published erratum, a contested result dressed as settled (Trillo–Navascués), an indefensible timeline, a missing CSL/LISA-Pathfinder/germanium landscape, and a metaphysical non-sequitur in "Empirical stakes."

**On the register verdicts:**

- **P-Q6 ("parameter-free Diósi–Penrose model empirically falsified"): correct in direction, mildly too weak / imprecise, and stale.** The natural parameter-free DP model *is* falsified (Grade-A: Donadi 2021, confirmed and strengthened by Majorana 2022/erratum 2023). But the Asserts should state that **Penrose's own physically-fixed value** (nuclear size) was excluded — not merely an idealization — and should absorb Figurato 2024 (the surviving free-R₀ model does not guarantee classicality) and the Majorana erratum. Recalibrate the wording; **keep the verdict.**
- **P-Q5 ("Orch-OR demoted"): too generous.** Describing Orch-OR as "a serious candidate... not retired," ranked below post-decoherence selection merely "on timing grounds," overstates its standing. Between Tegmark 2000, Reimers/McKemmish 2009 (microtubules cannot sustain the required coherence; "no known mechanism to protect" them), and Derakhshani et al.'s "highly implausible in all the cases analyzed," the *testable* versions of Orch-OR are regarded by mainstream physics and neuroscience as effectively refuted — with the surviving defense (McQueen 2023's "the tested variant was never advocated by anyone") being exactly the unfalsifiable relocation the article itself flags. Recommend a harder demotion: separate the **biology-level Orch-OR claim** (→ closer to DEMOTE-TO-COHERENCE-ONLY) from the **physics-level DP claim** (constrained as in P-Q6). [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)

The empirical case for Orch-OR is often oversold in the secondary press via the Khan/Wiest et al. 2024 epothilone-B anaesthesia result (*eNeuro* 11(8), ENEURO.0291-24; epoB delayed loss of righting reflex by 69 s, Cohen's *d* = 1.9). That result is real but shows only that microtubules are a plausible anaesthetic action-site — it does not evidence quantum coherence, gravitational OR, or non-computability. The article does not lean on it here, which is correct; downstream articles should not either. [PubMed](https://pubmed.ncbi.nlm.nih.gov/39147581/)[Substack](https://dbfools.substack.com/p/microtubules-and-quantum-consciousness)

---

## 4. Article-Specific Fixes (keyed to slug `penrose-gravity-induced-collapse-empirical-prospects`)

1. **Correct the physics error.** Delete "Penrose's original version effectively sets R₀ to zero, treating mass distributions as point-like." State that the parameter-free version *fixes* R₀ at the nuclear wave-function size (≈ 0.05 × 10⁻¹⁰ m in the Ge crystal), and that this specific physically-motivated value — not an idealization — is what Donadi 2021 excluded, by about an order of magnitude.
2. **Fix the "(R₀ = 0) is ruled out" parenthetical** in "The Diósi-Penrose Model and Its Partial Falsification" to match Fix 1.
3. **Add Figurato et al. 2024** (*New J. Phys.* 26, 113004) to references and prose. Report its real finding: the surviving free-R₀ DP model does not guarantee macroscopic classicality, and ~18 orders of magnitude of sensitivity improvement would be needed to reach the interesting spontaneous-radiation regime. This is a second, non-aesthetic cost the article currently omits.
4. **Add the Majorana 2023 erratum** (*Phys. Rev. Lett.* 130, 239902); give the corrected bound R_DP > 2.54 × 10⁻¹⁰ m; note Majorana's primary target was CSL.
5. **Reframe Trillo & Navascués 2025** to its actual thrust ("GIE detection is not enough to validate quantum gravity") and flag the live dispute (Diósi, arXiv:2511.00852, 2025). Downgrade from "can falsify the DP model" to "proposes a test avenue that is itself contested."
6. **Retire or heavily qualify the intro's "within the next decade" claim.** Given the sensitivity gaps the body concedes, it is not defensible as stated.
7. **Rewrite "Empirical stakes" to remove the non-sequitur.** State explicitly that confirming objective gravitational collapse would be a physicalist result carrying no dualist implication, and that even full confirmation of DP would leave the consciousness-causal-role claim entirely untouched — the two are logically independent.
8. **Add the CSL exclusion landscape** the article gestures at but never delivers: Adler's values largely excluded (LISA Pathfinder, X-ray, cantilevers); GRW value near the theoretical lower bound; wide un-excluded region remaining. Cite LISA Pathfinder (Carlesso et al. 2016) and the germanium/Majorana X-ray bounds.
9. **Add a genuine no-collapse rival paragraph.** State that objective collapse is a minority programme and that the mainstream reading of every null result surveyed is "standard QM, no collapse." One "Further Reading" line on Bohm is not engagement.
10. **Correct reference #6** to Pedalino et al. (2026), *Nature* 649, 866–870; disclose the Donadi quote's *Quanta Magazine* (2022) venue.
11. **Add the prose-only citations to the reference list:** Hagan/Hameroff/Tuszyński 2002; Reimers/McKemmish et al. 2009.

*Priority order:* #1/#2 (physics error) > #7 (metaphysical non-sequitur) > #3/#5 (suppressed and contested primary results) > #6 (overstated timeline) > #8/#9 (missing rivals/landscape) > #4/#10/#11 (citation hygiene).

---

## 5. Concrete Potential Improvements

### Article-specific (by slug)

- **`penrose-gravity-induced-collapse-empirical-prospects`** — Fixes 1–11 above, in the stated priority order.
- **`positions/quantum-interface` (P-Q6)** — Recalibrate the Asserts to state that Penrose's *own physically-fixed value* was excluded (not merely an idealization); add Figurato 2024 and the Majorana erratum to "Depends on"; register the free-R₀ classicality-squeeze under "Would shift if." Verdict unchanged, wording tightened.
- **`positions/quantum-interface` (P-Q5)** — Harden the demotion. Split the physics-level DP claim (constrained per P-Q6) from the biology-level Orch-OR claim (effectively refuted in its testable forms); rest the demotion on Reimers/McKemmish and Derakhshani's "highly implausible" verdict rather than on "timing grounds" alone.
- **`comparing-quantum-consciousness-mechanisms`** and **`falsification-roadmap-for-the-interface-model`** (cited downstream) — Audit for inheritance of the "parameter-free = R₀ = 0" error and the "confirmation supports dualism" non-sequitur.
- **`born-rule-and-the-consciousness-interface`** — Confirm it does not inherit the "Empirical stakes" non-sequitur, since the target article routes its consciousness-modulation claim there.

### Methodological (site-wide)

- **Add a "logical-independence" check** to the review workflow for physics-adjacent articles: does confirming the physical mechanism actually bear on the dualist thesis, or is it being recruited as if it did? The "Empirical stakes" non-sequitur is a *structural* failure mode distinct from author-stance inversion and would slip past the existing citation-fidelity and stance checks. This is arguably the corpus's most important blind spot: the site guards aggressively against inverting an author's stance, but not against the subtler error of treating a physicalist-compatible empirical result as confirmation of dualism.
- **Require an erratum/retraction check** as a distinct citation-verification step. The Majorana erratum was missed: the metadata was clean but superseded. The corpus's ledgers verify existence, not currency.
- **Flag preprint-stage and actively-disputed results** with a standing marker. Trillo–Navascués is a 2025 result under published dispute; the article presents it flat. A "contested" tag analogous to the register's calibration axes would prevent live disputes being laundered into settled avenues.
- **Give "understatement" parity with overstatement in review prompts.** Here, imprecision (parameter-free rendered as "R₀ = 0") accidentally made the falsification sound *weaker* than it is, which flatters the site's position — Penrose's real, physically-motivated value was excluded, not just an idealization. Prompts tuned to catch over-claiming should equally catch imprecision that launders a stronger disconfirmation into a milder-sounding one.
- **Enforce empirical-landscape completeness when an article's own frame promises a survey.** Titles like "The Experimental Frontier" and "empirical prospects" imply coverage of the standard exclusion plots (CSL λ–r_C, LISA Pathfinder, germanium X-ray). Presenting only DP-friendly experiments is a subtle instance of the "live-but-marginal-as-mainstream" drift the site already tracks — worth an explicit checklist item for any article surveying an experimental field.

---

## Verification Notes

Added at collection time (2026-07-31), not part of the reviewer's text. Extraction was byte-exact: the artifact body was serialised in the page context, SHA-256'd there, downloaded as a Blob and re-hashed locally — both digests `e457807571176d200cf211ce07fe29086a90b3b0e8495afd73aa47cbdbdce548` (23,225 bytes / 22,923 chars). No retyping or paraphrase at any point. Completeness was checked separately from fidelity: the rendered artifact carries all 13 headings from the H1 through the closing "Methodological (site-wide)" subsection, with an `ol` of exactly 11 article-specific fixes and a `ul` of exactly 5 site-wide recommendations, matching the conversation summary's own count, and the body ends on a complete sentence.

**Quoted-span grep audit.** 27 quoted spans were checked against the raw sources (`obsidian/topics/penrose-gravity-induced-collapse-empirical-prospects.md` and `obsidian/positions/quantum-interface.md`), normalising for emphasis markers, wikilink syntax, subscripts and dash variants — a precaution against the known false-negative where markup breaks a correct quote's contiguity. 23 matched. The 4 that grepped zero are **not** fabricated attributions to the Map:

- **"no known mechanism to protect"** — the reviewer attributes this to Reimers/McKemmish 2009, not to the Map. The article's own wording for the same point is "either to assume unphysical conditions or to specify regimes microtubules do not occupy". External-source quote; verify against Reimers if it becomes load-bearing.
- **"the tested variant was never advocated by anyone"** — attributed to McQueen 2023. The reviewer's surrounding claim that *the article flags this as an unfalsifiable relocation* is accurate: the article says McQueen's move is "structurally a rescue of the kind Donadi flagged: the falsifying conditions are relocated to a regime current experiments cannot reach." The quoted phrase itself is the reviewer's own compression of McQueen's argument, not article text.
- **"live-but-marginal-as-mainstream"** — presented as a drift "the site already tracks", but this label greps zero across `obsidian/`, `archive/` and `hugo/content/`. It is the reviewer's own coinage. The underlying concern may be tracked under other names; the attribution to existing site vocabulary is unsupported and should not be cited back as established site terminology.
- **"macroscopicity of μ = 15.5"** — quoted from the Pedalino et al. *Nature* abstract, not the Map. The article paraphrases without the μ figure.

The lead physics finding rests on quotes that are verbatim-accurate: the article does contain "Penrose's original version effectively sets R₀ to zero, treating mass distributions as point-like" and "The parameter-free version (R₀ = 0) is ruled out." Whether that characterisation is *wrong* is a substantive physics question for the downstream pass, and it runs against the Map's interest in the unusual direction of making the falsification **stronger**, so it warrants primary-source checking rather than either reflexive acceptance or rejection.

**Convergence with the same-cycle ChatGPT review** (`outer-review-2026-07-31-chatgpt-5-6-pro.md`), reached independently: the uncited **Majorana 2023 erratum** (this review's fix #4) and the **reference #6 first-author misattribution — Arndt where the record is Pedalino** (fix #10). ChatGPT's XENONnT (2026) finding has **no** counterpart here. Priority upgrades on the two convergent items are for `/combine-outer-reviews` to apply, not this collection.

**Publisher-of-record verification (collection time, 2026-07-31).** Every load-bearing citation this review introduces was checked against Crossref / arXiv metadata rather than a search aggregator, and all five resolved exactly as the reviewer gave them:

- **Figurato et al. 2024** — CONFIRMED. "On the effectiveness of the collapse in the Diósi–Penrose model", *New Journal of Physics* **26**, 113004 (Nov 2024), DOI `10.1088/1367-2630/ad8c77`, authors Figurato, Dirindin, Gaona-Reyes, Carlesso, Bassi, Donadi — the exact author list cited. The paper is **absent** from the article's 14-entry reference list, confirming the omission.
- **Majorana erratum** — CONFIRMED. "Erratum: Search for Spontaneous Radiation from Wave Function Collapse in the Majorana Demonstrator [Phys. Rev. Lett. 129, 080401 (2022)]", *Phys. Rev. Lett.* **130**, 239902, 9 June 2023. The article's reference 4 cites only the uncorrected 2022 paper.
- **Trillo & Navascués 2025** — CONFIRMED. "Diósi-Penrose model of classical gravity predicts gravitationally induced entanglement", *Phys. Rev. D* **111**, L121101 (12 June 2025).
- **The dispute is real** — CONFIRMED. arXiv:2511.00852, "No, classical gravity does not entangle quantized matter fields", Lajos Diósi, 2 Nov 2025. The reviewer's claim of a live published rebuttal is not fabricated.
- **Pedalino first-author misattribution** — CONFIRMED. DOI `10.1038/s41586-025-09917-9`, *Nature* **649**, 866–870: author order is Pedalino S., Ramírez-Galindo B., Ferstl R., Hornberger K., **Arndt M.**, Gerlich S. The article's reference 6 names "Arndt, M." as first author. Incidentally this also settles an open question in the sibling ChatGPT task: the **published** Nature title is "Probing quantum mechanics with nanoparticle matter-wave interferometry", which is what the article already has — only the author needs repointing, not the title.

Also verified locally: the article's reference list contains no entry for Hagan/Hameroff/Tuszyński 2002 or for Reimers/McKemmish, both of which the prose relies on — the reviewer's fix #11 is correct.