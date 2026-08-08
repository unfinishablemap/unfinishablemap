---
ai_contribution: 100
ai_generated_date: 2026-08-08
ai_modified: 2026-08-08 03:32:13+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-08
date: &id001 2026-08-08
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-08 03:32:13+00:00
modified: *id001
related_articles:
- '[[neural-refresh-rates-and-the-smoothness-problem]]'
title: Deep Review - Neural Refresh Rates and the Smoothness Problem
topics: []
---

**Date**: 2026-08-08
**Article**: [Neural Refresh Rates and the Smoothness Problem](/topics/neural-refresh-rates-and-the-smoothness-problem/)
**Previous review**: [2026-07-16](/reviews/deep-review-2026-07-16-neural-refresh-rates/) (ninth deep review of this topics article)

## Lens Applied — READ THIS BEFORE INHERITING ANY CLEARANCE

This pass applied **empirical-claim fidelity**: does each paraphrase match what the cited study actually found and actually claims? This is the third axis, orthogonal to citation *metadata* (audited repeatedly here, 2026-05-26 through 2026-07-16) and to *verbatim quote* fidelity.

The distinction is load-bearing for this article. Ten prior reviews cleared the metadata and inherited each other's clearance. **The metadata was and remains almost entirely correct. The paraphrases were not.** Four of the article's five substantive empirical citations misrepresented what their source claims — not by inventing sources, but by stripping hedges, transposing figures between papers, and attributing to an author an argument he explicitly disclaims. None of this was visible to a metadata check, because every author, year, volume and page number was right.

Prior clearances on this article cover metadata only. Do not read them as covering claim fidelity.

## Body-change status since last review

Only the Sellars reference correction (commit 2b546dcf28, 1965 → 1962) touched this file since 2026-07-16. Prose was unchanged. The defects below are therefore **long-standing**, not regressions — they date to the article's original composition and survived nine reviews.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. VanRullen quote strips the hedge that carries its meaning — FIXED**

The article rendered: *As VanRullen summarised: "Perception and cognition operate periodically, as a succession of cycles mirroring the underlying oscillations."*

Verified at the publisher-of-record abstract (TiCS 20(10), 723–735, DOI 10.1016/j.tics.2016.07.006), the actual sentence is:

> "Brain function involves oscillations at various frequencies. **This could imply that** perception and cognition operate periodically, as a succession of cycles mirroring the underlying oscillations."

The article converted VanRullen's explicitly conditional inference into his summary conclusion, and presented a mid-sentence fragment as a complete sentence. The quoted words are real and verbatim; the framing verb ("summarised") and the excised "This could imply that" invert the epistemic status. This is the dropped-qualifier critical class (§2.5), and it is precisely the defect a metadata check cannot see.

**2. "Established" over-claims what VanRullen's review concluded — FIXED**

The article said VanRullen's review "**established** that perception operates rhythmically through multiple oscillatory channels." The abstract's own framing is far weaker: contemporary evidence "**points**" to several rhythms; the alpha and attentional rhythms "**may** coexist"; and the review closes:

> "How these multiple periodic functions are orchestrated, and how internal sampling rhythms coordinate with overt sampling behavior, **remain open questions**."

VanRullen presents discrete perception as an "age-old notion" that "has resurfaced," not as an established result. The driver brief asked directly whether the source presents this as established or as one model among several — **the answer is the latter**, and the article had it the other way round. Rewritten to state the inference conditionally, to quote "remain open questions," and to separate the well-evidenced claim (rhythmic sampling) from the contested one (genuinely discrete perception).

**3. The ~400 ms figure and the "time slice" framing were sourced to the wrong paper — FIXED**

The article attributed to **Herzog, Drissi-Daoudi & Doerig (2020)** the claim that stage one integrates "over periods of up to 400 milliseconds," plus a direct Herzog quotation.

The 2020 abstract, retrieved verbatim via Europe PMC, **contains no millisecond figures at all**. It argues only that "substantial periods of continuous unconscious processing precede discrete conscious percepts."

The 400 ms figure and the "time slice" vocabulary both originate in a **different paper**: Herzog, Kammer & Scharnowski (2016), *Time Slices: What Is the Duration of a Percept?*, *PLoS Biology* 14(4): e1002433. Verified at the publisher: "TMS can modulate the unconscious integration for up to 400 ms"; "consciousness cannot occur before 400 ms."

The underlying claim is sound — it was cited to a paper that does not make it. Fixed by adding the 2016 reference, attributing the figure and the "time slice" framing to it, and naming it in the body.

**4. The Herzog quotation is a press-release remark, not a journal statement — FIXED**

*"The brain wants to give you the best, clearest information it can, and this demands a substantial amount of time."*

This appears in **neither** cited paper. It is from the **2016 EPFL press release** for the *Time Slices* paper. Its true form begins "The reason is that the brain wants to give you…" — the article's capitalised "The brain wants…" silently promoted a mid-sentence fragment to a sentence.

Checked and excluded: it is **not** in the 2020 ScienceDaily release (whose actual Herzog quotes are "Consciousness is basically like a movie…" and "It's the zombie within us that drives your bike…"). Re-rendered as a contiguous verbatim fragment — the brain "wants to give you the best, clearest information it can, and this demands a substantial amount of time" — and the reference entry now states plainly that the quotation comes from the press release, not the paper.

**5. Lee is credited with an argument he explicitly disclaims — FIXED (most serious finding)**

Verified against the primary text (PDF from the author's own site, extracted locally and grepped).

The article said: *"Andrew Lee's work on **discriminatory grain** … Lee argues that introspection does not decide between phenomenal experience being genuinely continuous or merely discrete **at a grain finer than our discriminatory threshold**."*

Three separate defects:

- **The term "discriminatory grain" does not appear in the paper.** Grep over the full text returns exactly three hits for "grain": two instances of "the grain of introspection" (describing a move Lee sets aside) and one bibliography entry for Lockwood's "The grain problem." The Map appears to have minted this phrase and then attributed it to Lee.
- **Lee explicitly refuses the sub-threshold-grain argument the article gives him.** Verbatim: *"Unlike some defenses of the discrete theory, my arguments **won't appeal to limits in our introspective capacities**. Instead, I'll develop a structural (as opposed to epistemic) explanation of the difference between smooth and gappy experiences."* He grants "some sympathy" for the grain move but sets it aside as "dialectically unsatisfying." He then argues the reverse of the article's gloss: *"those most optimistic about our introspective capacities have reason to favor the discrete theory."*
- **"Applies with equal force to temporal smoothness" over-transfers his result.** Lee is explicit that his target question is *structurally distinct* from this article's: the continuity of smooth experiences "concerns continuous functions; the latter concerns continuous spaces… they're structurally distinct." And: *"my arguments **won't directly adjudicate** debates about the stream of consciousness. **Nevertheless**, my defense of the discrete theory **may still be relevant** to those debates."* "Equal force" is not available; "may still be relevant, and a similar analysis is plausible" is.

What the article got **right**, and which is preserved: Lee's actual conclusion, quoted verbatim — "introspection leaves open whether smooth experiences are continuous or discrete."

Section rewritten to state Lee's real conclusion, name the route he declines, record his surprising pro-introspection argument for discreteness, and mark the structural-distinctness caveat. The Map's own downstream use of the caveat is retained but now rests on "to the extent it transfers" rather than "equal force."

**6. Citation currency: Lee is no longer a preprint — FIXED**

Cited as "Lee, A. Y. (2024). *PhilArchive*. University of Toronto." Per the author's own publication listing, "Consciousness & Continuity" is now under **Peer-Reviewed Articles: *Philosophical Studies*, forthcoming**. Updated to `Lee, A. Y. (forthcoming). Consciousness and Continuity. *Philosophical Studies*. Preprint: PhilArchive (LEECAC-14).`

Note the driver's hypothesis ran the other way — the worry was that the article leaned on an unrefereed preprint. In fact it has passed peer review, so the body's "Lee argues" framing was always fine; only the reference entry was stale.

### Medium Issues Found

**7. Alpha/theta functional roles were transposed — FIXED.** The article assigned attentional sampling "at attended locations" to alpha (~10 Hz) and gave theta as "~4–8 Hz." VanRullen assigns *sensory* sampling to alpha (~10 Hz) and *attentional* sampling to a distinct rhythm "at around 7 Hz." Corrected to track the cited source; the "divides across objects" detail is retained as it is well supported in VanRullen's wider programme.

**8. Lead sentence merged two distinct rhythms — FIXED.** "roughly 7–13 Hz in attention-driving alpha rhythms" collapsed VanRullen's two separate rhythms into one mislabelled band. The 7–13 Hz envelope is retained (it fairly brackets both) but is now decomposed into the sensory ~10 Hz and attentional ~7 Hz components.

**9. The 2020 authors' self-assessment was stated flat — FIXED.** "The two-stage model resolves the continuous-versus-discrete debate" is the authors' own claim ("We propose that such a model… resolves centuries old debates"). Now attributed: "On its authors' own assessment…". The article's immediately following "but opens a deeper question" already prevented endorsement, so this was a light touch.

### Checked and Cleared — no change made

- **Zheng & Meister 2025** — verified at Europe PMC: *Neuron* 113(2), 192–204, DOI 10.1016/j.neuron.2024.11.008. Both figures exact against the abstract: human throughput "about 10 bits/s", sensory gathering "∼10⁹ bits/s". The article's framing is faithful. Left untouched per driver instruction; **this article is the correct anchor of that year family.**
- **Herzog, Drissi-Daoudi & Doerig 2020 metadata** — TiCS 24(10), 826–837, DOI 10.1016/j.tics.2020.07.001. Correct. DOI added.
- **VanRullen 2016 metadata** — TiCS 20(10), 723–735. Correct. DOI added.
- **Postdictive-effects paraphrase** — "stimuli presented *after* a target can alter how the target is consciously perceived" is exactly what the 2020 review reports. Faithful.
- **Crick & Koch 1990 gamma binding**, including "its strong form has weakened" and the anaesthesia/seizure counter-evidence — faithful and appropriately hedged.
- **⚠️ The "strongest physicalist response" superlative (§Functionalist Response) — TESTED AND EARNED; LEFT ALONE.** The driver flagged this for testing because the same shape produced a real defect elsewhere. The test is whether the body surveys the field it ranks over. It does — four distinct physicalist families are engaged: predictive coding / temporal interpolation / recurrent sustaining (§Physical Smoothing Mechanisms), functionalism (§Functionalist Response), illusionism (§Bergson's Inversion), and higher-order plus global-workspace theories with the temperature analogy (§Locke's Objection Inverted). The ranking claim has a surveyed field behind it. **Not hedged** — hedging it would have been a regression.

### Counterarguments Considered

- *Eliminative Materialist / Hard-Nosed Physicalist*: the corrected VanRullen framing strengthens rather than weakens their hand, since the article now concedes that discrete perception is not established. Correct outcome — the article's case never rested on discreteness being settled, and it is more honest for saying so.
- *Empiricist (Popper's Ghost)*: the pre-fix article was vulnerable to the charge that it recruited hedged source claims as firm support. That charge is now answered at four loci.

## Optimistic Analysis Summary

### Strengths Preserved

Front-loaded lead; the "strong form has weakened" honesty about gamma binding; the registering-versus-feeling engagement with functionalism; the named-illusionist passage isolating the *phenomenal* seeming; the Locke inversion; the convergent-evidence-programme framing. Voice untouched throughout.

### Enhancements Made

The Lee section is materially better than a bare correction would have left it: Lee's actual argument — that the *most* introspection-optimistic view has reason to prefer discreteness — is a sharper and more interesting complication than the sub-threshold-grain story it replaces, and it genuinely does cut both ways, which is what the section wanted all along.

### Cross-links Added

None. Existing cross-link set verified intact; no numeric cross-references exist in this file, so the reference renumbering (12 → 13 entries) was safe.

## Word Count

Prose 2432 → **2785** (+353) against the topics soft threshold of 3000 — **215 words of headroom remaining, not length-constrained**. Raw `analyze_length` reports 3149 / `soft_warning`, which is the known reference-apparatus false positive: the apparatus (Further Reading + References) is 370 words and inflated by the added DOIs and the press-release annotation. Decomposed figure is the real one. **No condensation performed or warranted.**

## Remaining Items

- **The Lee misreading is a corpus family, deliberately not swept from here.** Same scoping doctrine the driver applied to the Zheng & Meister year family. The "discriminatory grain" attribution and/or the sub-threshold-grain gloss propagate to live articles: `obsidian/voids/resolution-void.md` L42 ("Lee develops precise models of 'discriminatory grain'"), `obsidian/concepts/grain-mismatch.md` L45 (same phrasing), plus `obsidian/topics/grain-mismatch-as-independent-evidence.md`, `obsidian/concepts/temporal-consciousness.md`, `obsidian/voids/smoothness-and-continuity.md`, and `archive/voids/continuity-void.md`. Note these siblings quote Lee's real conclusion correctly — it is the *"discriminatory grain"* framing and the epistemic-opacity route that need correcting, not the conclusion.
- **The stale Lee preprint citation is the same family**, and additionally carries a year split: several loci say 2023 (`obsidian/research/voids-resolution-void-2026-02-22.md` L212, `archive/voids/continuity-void.md` L112), most say 2024. All should become "forthcoming, *Philosophical Studies*".
- Buddhist discrete-moment (*kshana*) tradition and Whitehead's epochal theory — deferred across nine reviews; only add with a dedicated target article.

## Stability Notes

**The convergence claim in the 2026-07-16 review was true of metadata and false of content.** That review recommended treating this article as "a strong convergence-exclusion candidate." On the evidence here that recommendation should be **withdrawn for any lens not yet applied**. Nine reviews reached stability on structure, voice, and bibliographic metadata while five substantive misrepresentations of source content sat untouched in the prose. Convergence is lens-relative; an article is converged only with respect to the lenses actually run against it.

**Do NOT re-flag** (verified this pass at primary sources): Zheng & Meister 2025 metadata and both bits/s figures; Herzog 2020 metadata; VanRullen 2016 metadata; the "strongest physicalist response" superlative (tested, earned); the postdictive-effects paraphrase; Crick & Koch gamma treatment.

**Do NOT reintroduce**: "established" for VanRullen's review; the unhedged VanRullen quote; the 400 ms figure or "time slice" attributed to the 2020 paper; the Herzog quotation presented as a journal statement; "discriminatory grain" as Lee's term; the sub-threshold-grain argument as Lee's route; "applies with equal force" for the transfer to temporal smoothness.

**Bedrock disagreements** (not fixable; not critical): functionalists and physicalists maintain that smoothing mechanisms *constitute* smooth experience — framework-boundary, and the article's response is explicitly position-dependent; MWI defenders and hard-nosed materialists find the smoothness problem unconvincing.

**Calibration discipline**: No possibility/probability slippage found. The article declines to treat smoothness as independent evidence for dualism and hedges the bidirectional-interaction claim. The fixes above *improve* calibration by removing four inherited over-statements that were the sources', not the Map's, to begin with — the article had been borrowing confidence its citations did not extend.

**Next lens suggestion**: this article is now clean on metadata, quotes, and claim fidelity. The unexamined surface remaining is the *phenomenological* citations — James, Bergson, Dainton — which have never been verified against primary text on this article. The Bergson "cinematographic" reading and the Dainton "interconnected flowing whole" quote are the specific candidates.