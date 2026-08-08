---
title: "Deep Review - Minimal Consciousness"
created: 2026-08-08
modified: 2026-08-08
human_modified: null
ai_modified: 2026-08-08T08:03:30+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-08-08
last_curated: null
---

**Date**: 2026-08-08
**Article**: [[minimal-consciousness|Minimal Consciousness]]
**Previous review**: [[deep-review-2026-06-27-minimal-consciousness|2026-06-27]] (ninth pass; eight prior)

## Context — Lens Selection

Ninth deep review. The eight prior passes (2026-01-20, 01-22, 01-31, 02-25, 03-22, 05-20, 06-04, 06-27) repeatedly ran the **citation-metadata ledger** lens, and the metadata is in fact clean — every author, year, volume, issue and page range in the References verified correct at the publisher this pass too. Re-running that lens was guaranteed to find nothing.

This pass deliberately ran three lenses the prior eight did not:

1. **Empirical-claim fidelity** — does each paraphrase match what the cited work actually *found* or *proposed*?
2. **Verbatim quote attribution** — every quoted span checked as a literal string at the primary publisher.
3. **Citation framing** — real, verbatim, correctly attributed, yet made to support something the author would not endorse.

The result vindicates the premise: **metadata clean, three substantive fidelity defects found**, including one misquote and one misattribution of a named framework's content to the wrong authors. An article is converged only with respect to the lenses actually applied to it.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Bayne, Hohwy & Owen 2016 credited with an axis list that is not theirs** (attribution error — CRITICAL)

The article stated that Bayne, Hohwy and Owen hold that "global states vary along several independent axes—**wakefulness, content, integration, selfhood**—rather than along one vertical line."

Verified against three independent sources:
- **Abstract** (verbatim, via Europe PMC, OpenAlex, PubMed, Manchester and Monash repositories, all agreeing): the paper "argues that the levels-based framework for conceptualizing global states of consciousness is untenable and develops in its place a multidimensional account of global states." It enumerates no axes.
- **Páleník 2024**, *What does it mean for consciousness to be multidimensional? A narrative review* (PMC11222411), a dedicated review of exactly this literature: Bayne et al. proposed **two families** of dimensions — content-related dimensions "associated with the gating of contents," and functional dimensions corresponding to "the availability of conscious contents for different cognitive and behavioral systems." The review does not attribute "wakefulness," "integration" or "selfhood" to them.
- **Bayne & Carter 2018** (PMC6146157), Bayne's own follow-up, recapitulating the 2016 view: global states "modulate both the kinds of contents that can enter consciousness and the way in which those contents can be used by the organism for cognitive and behavioural control." Same two-family structure; no four-axis list.

Diagnosis: **"integration" and "selfhood" are Birch, Schnell & Clayton's vocabulary**, back-projected onto Bayne et al. from the very next sentence of the same paragraph (Birch et al.'s dimensions 3–5 are *integration at a time*, *integration across time*, and *self-consciousness*, glossed "selfhood"), with "wakefulness" added from nowhere in either source. The two cited papers had been partially merged.

This also damaged the paragraph's own argument. Its structure is "Bayne et al. for human global states; Birch et al. make the *parallel* case for animals" — a parallel that is only interesting if the two frameworks arrive independently. Describing Bayne et al. in Birch et al.'s words made the convergence circular. **Fixed**: Bayne et al. now described by their actual two-family proposal (which contents can enter consciousness; how far those contents are available to cognitive and behavioural systems), and the clinical list corrected to the paper's own ("anaesthesia, sleep, epileptic absence seizures, and post-comatose disorders").

Consequential fix: the article's own downstream extrapolation ("there would be a minimal wakefulness, a minimal content, a minimal integration, a minimal selfhood, a minimal reportability") inherited the bad vocabulary and read as though the axes were the sources'. Re-grounded on Birch et al.'s actual dimensions and explicitly marked as the Map's own extension.

**2. New York Declaration quotation is not verbatim, and the omission changes its scope** (misquote — CRITICAL)

Article carried: *"If there's a realistic possibility of conscious experience in an animal, it is irresponsible to ignore that possibility."*

Actual text, verified at the primary source (the Declaration hosted by NYU at `sites.google.com/nyu.edu/nydeclaration/declaration`, corroborated independently by the Wikipedia reproduction):

> "When there is a realistic possibility of conscious experience in an animal, it is irresponsible to ignore that possibility **in decisions affecting that animal**."

Two deviations: "When there is" silently rewritten as "If there's," and — the substantive one — the scoping clause *in decisions affecting that animal* dropped. The Declaration states a **decision rule for acting under uncertainty**. Truncated, it reads as an unrestricted epistemic injunction, which is precisely the misreading the Map's own [[possibility-probability-slippage]] discipline exists to prevent: it converts a precautionary policy into something closer to a verdict on the evidence.

**Fixed**: exact text restored, plus two sentences making the decision-scoping explicit and noting the Declaration does not claim consciousness has been established in the animals it covers. The Declaration itself added to References as the source of record for the quote (the previous only entry was Andrews et al.'s companion *Background* document, which is a different text — that entry independently verified correct: Andrews, K., Birch, J., Sebo, J., & Sims, T. (2024), NYU, 19 April 2024).

### Medium Issues Found

**3. IIT's minimal-system example attributed to a device Tononi does not use** (framing)

Article stated: "A thermostat, on IIT's account, might have a flicker of experience." Verified at Tononi 2008, *Biological Bulletin* 215(3): the canonical worked example is a **photodiode**, introduced in a section titled "Information: the photodiode thought experiment," discriminating "light" from "dark" and generating one bit against the enormous repertoire available to a human observer. **No thermostat example appears in the paper** (a thermistor is mentioned only in passing). The thermostat belongs to the Chalmers panpsychism literature, not to Tononi; and a simple feedforward thermostat is the awkward case for IIT rather than a clean illustration of it. **Fixed** — replaced with Tononi's own photodiode.

Also added, per the physicalist-recruitment check below: an explicit note that **IIT is a physicalist identity theory** and that its widespread-consciousness verdict therefore lends the Map no anti-physicalist support. Reference completed to `215(3)`.

**4. Ginsburg & Jablonka's criterion stated without the qualifier that constitutes it** (framing)

The References carried Ginsburg & Jablonka 2019 with **no inline citation anywhere** (orphan reference, §2.4 step 5). The nearest body claim read: "Habituation, sensitisation, and especially associative learning suggest information integration that might accompany experience" — the generic version of a criterion whose entire content is the qualifier. Their marker is ***Unlimited* Associative Learning**: verified at Birch, Ginsburg & Jablonka 2020, *Biology & Philosophy* (PMC7116763), "a distinctive type of learning that can serve as a transition marker for the evolutionary transition from non-conscious to conscious life"; and Ginsburg & Jablonka 2021 (PMC7935133), "the transition to animals capable of unlimited associative learning, which, on our account, constitutes sentience"; UAL "enables animals to discriminate between composite percepts and acts." **Fixed** — UAL named precisely, attached to its authors, orphan reference resolved, and the loose reading explicitly disclaimed.

### Physicalist-Recruitment Check (targeted)

The reference list is Andrews, Bayne ×2, Birch, Ginsburg, Metzinger, Nagel, Tononi — all but Nagel broadly naturalist or physicalist. Checked each for being made to underwrite an irreducibility claim they do not hold:

- **Bayne, Hohwy & Owen** — no irreducibility claim attributed. The article's inference ("on this reading the Map's case strengthens") is explicitly flagged as the Map's own reading and preceded by an honest concession that the levels debate is contested. Clean, once the axis misattribution is fixed.
- **Birch, Schnell & Clayton** — paraphrase is *exact* (see below). No recruitment.
- **Birch (precautionary framing)** — was the weakest point, via the truncated Declaration quote. Now repaired; the decision-scoping is stated in terms.
- **Ginsburg & Jablonka** — were being loosely glossed, now stated as the naturalist evolutionary transition marker it is.
- **Tononi / IIT** — the article did not recruit IIT as anti-physicalist, but left its status unstated. Now stated explicitly.

No case found of a physicalist being made to testify against physicalism.

### Web-Verified Citation Ledger

- **Andrews, K., Birch, J., Sebo, J., & Sims, T. (2024), "Background to the New York Declaration on Animal Consciousness," NYU** — state: **real-correct** (authors and hosting confirmed at nydeclaration.com's own suggested-citation line).
- ***The New York Declaration on Animal Consciousness* (2024), NYU, 19 April 2024** — state: **added** (was the uncited source of the body's quotation).
- **Bayne, T., & Chalmers, D. J. (2003), "What is the unity of consciousness?"** — state: **real-correct** metadata; not cited inline (bibliography entry, retained).
- **Bayne, T., Hohwy, J., & Owen, A. M. (2016), "Are There Levels of Consciousness?" *TiCS* 20(6), 405-413** — state: **real-correct metadata / paraphrase-wrong** (PMID 27101880, DOI 10.1016/j.tics.2016.03.009 — every metadata field confirmed; the *content* attributed to it was wrong; corrected, see Critical Issue 1).
- **Birch, J., Schnell, A. K., & Clayton, N. S. (2020), "Dimensions of Animal Consciousness," *TiCS* 24(10), 789-801** — state: **real-correct, paraphrase exact**. Abstract verbatim (Europe PMC, DOI 10.1016/j.tics.2020.07.007, PMID 32830051, PMCID PMC7116194): "five key dimensions of variation: perceptual richness, evaluative richness, integration at a time, integration across time, and self-consciousness… we can construct a consciousness profile for that species… there is no single scale along which species can be ranked as more or less conscious. Rather, each species has its own distinctive consciousness profile." The article's paraphrase matches the dimension names, the "consciousness profile" term, and the no-single-scale claim exactly. **No change needed — this one was right.**
- **Ginsburg, S., & Jablonka, E. (2019), *The Evolution of the Sensitive Soul*, MIT Press** — state: **real-correct metadata / orphan resolved**; UAL content verified via the authors' own PMC-indexed papers (PMC7116763, PMC7935133).
- **Metzinger, T. (2020), MPE, *Philosophy and the Mind Sciences* 1(I)** — state: **real-correct**; body paraphrase (content drains away, awareness persists) consistent with the MPE programme. Unchanged.
- **Nagel, T. (1974), *The Philosophical Review* 83(4), 435-450** — state: **real-correct**; bibliography entry underwriting the "what it's like" idiom.
- **Tononi, G. (2008), *Biological Bulletin* 215(3)** — state: **real-correct metadata / example-wrong** (photodiode, not thermostat; corrected, volume/issue completed).

### Verbatim Quote Ledger

Eight quoted spans of 15+ characters appear in the body. Extracted programmatically, then classified:

| Span | Type | Verdict |
|---|---|---|
| "something it is like" / "something it's like" | Nagelian idiom, not a sourced quotation | fine |
| "there is awareness" | glossing *vijñāna*, scare-quote | fine |
| "slightly conscious" | scare-quote of a position under discussion | fine |
| "where does consciousness begin?" | the article quoting its own question | fine |
| two spans at L64 | artifacts of the extractor spanning em-dashes, not quotations | n/a |
| **NY Declaration precautionary clause** | **external verbatim quotation** | **MISQUOTED — fixed** (see Critical Issue 2) |

Only **one** genuine external verbatim quotation exists in the body, and it was wrong. Post-fix the corrected string returns `grep -c` = 1 against the source file, and the old form returns 0.

Remaining quoted spans in the References are article titles; all verified correct at publisher.

### Claims I Could Not Verify

- **"*C. elegans* responds to isoflurane similarly to vertebrates"** (Empirical Indicators section, uncited). I searched Europe PMC for *C. elegans* × isoflurane × volatile anaesthetic and retrieved five relevant papers (Chang et al. 2023 *Anesthesiology*, Chang et al. 2025 *PLoS ONE*, Chang et al. 2026 *Front. Syst. Neurosci.*, Elami et al. 2026, Shin et al. 2022) — **none of them states comparative dosimetry against vertebrates**, so *I did not find* confirmation that the concentrations match, and equally did not find refutation. The claim is left unchanged rather than edited on an unverified basis. It remains an **uncited empirical claim** and is the best candidate for the next fidelity pass; note that Chang et al. 2025 ("Anesthesia isn't sleep…") bears on the adjacent inference from anaesthetic responsiveness to state-disruption.

### Reasoning-Mode Classification

No named-opponent engagements in this article — the "Dualism vs emergence" passage argues against a position (emergentist materialism), not a person, and is unchanged. No per-opponent classification applies. Label-leakage grep for editor vocabulary (`Mode One/Two/Three`, `Engagement classification:`, `unsupported-jump`, `bedrock-perimeter`, `**Evidential status:**`) returns nothing in article prose.

### Possibility/Probability Slippage Check

Diagnostic test — *would a tenet-accepting reviewer still flag any claim as overstated?* Post-fix, **no**. Notably, the Declaration misquote was itself a *latent* slippage vector (a decision rule presented as an unrestricted claim); repairing it removes the vector. The MPE-to-Organism subsection remains the article's strongest calibration passage and is untouched.

## Optimistic Analysis Summary

### Strengths Preserved

- **The MPE-to-Organism Disanalogy** subsection — still the best thing in the article, and explicitly declines an evidential upgrade. Untouched.
- **The Birch, Schnell & Clayton paraphrase** — a genuinely exemplary piece of citation practice; it reproduces the five dimension names, the "consciousness profile" term and the no-single-scale conclusion with complete accuracy. Preserved verbatim. Worth noting as a positive control: the same paragraph contained one exact paraphrase and one badly wrong one, which is why per-cite checking beats per-paragraph impressions.
- **"What Would Challenge This View?"** — the in-practice / in-principle split with its honest closing concession that "the framework's net falsifiability is genuinely modest." Untouched.
- The concession that the levels debate is "a live position in consciousness science, not a settled result." Untouched.

### Enhancements Made

- IIT's status as a physicalist identity theory made explicit, closing a gap where a reader could have mistaken its widespread-consciousness verdict for support of the Map.
- The Declaration's precautionary logic now correctly characterised as a rule for acting under uncertainty.
- UAL correctly named, resolving an orphan reference and sharpening a previously vague indicator.

### Cross-links Added

None. The article's link density is already high and no new connection was warranted by the fixes.

## Sibling Loci (reported, not fixed — per driver brief)

Swept by argument across `obsidian/{topics,concepts,apex,voids,positions}` and `archive/` only (workflow and reviews trees deliberately excluded — they quote retired wording verbatim and make dead claims look live):

1. **`archive/concepts/minimal-consciousness.md` L193 carries the identical truncated misquote** — *"if there's a realistic possibility of conscious experience in an animal, it is irresponsible to ignore that possibility."* This is an archived twin on a live published URL. **Recommend a task.**
2. **`obsidian/topics/consciousness-in-simple-organisms.md` L70 already has the quote CORRECT**, including the scoping clause. The corpus therefore contained the right version and the reviewed article had drifted from it — useful confirmation that the fix restores rather than invents.
3. **`obsidian/topics/birch-edge-of-sentience-and-the-five-tier-scale.md`** handles Birch's "realistic possibility… irresponsible to ignore" with the policy-scoping intact and explicitly distinguishes it from modal possibility. No defect; a model for how the clause should be handled.
4. **Thermostat-attributed-to-IIT siblings**: `obsidian/concepts/parsimony-epistemology.md` L134 ("consciousness in thermostats and logic gates") and `archive/topics/limits-of-parsimony-in-consciousness-science.md` L83/L87. Lower severity than the reviewed instance — these discuss IIT's panpsychist *implications* rather than presenting a thermostat as Tononi's worked example — but the same imprecision. Note also an **unverified quoted span** at `archive/topics/limits-of-parsimony-in-consciousness-science.md` L83 attributing to Tononi: *"openly stands by panpsychism insofar as it follows from IIT."* Not checked this pass.
5. The Bayne/Hohwy/Owen four-axis list has **no siblings** — grep for the axis vocabulary across all content trees returns nothing outside the reviewed file. The defect was local.

## Remaining Items

- The uncited *C. elegans* / isoflurane claim (see "Claims I Could Not Verify").
- Sibling loci 1 and 4 above.

## Stability Notes

- The eight prior reviews were **not** wasted, but they converged on one lens. The citation *metadata* is genuinely clean and has now been verified enough times that further metadata passes should be considered closed. Future reviews of this article should target **content fidelity**, not bibliographic form.
- Bedrock disagreements, unchanged and not to be re-flagged: the eliminative materialist, hard-nosed physicalist, Many-Worlds and quantum-skeptic objections all sit at the framework boundary. The article's honest admission that its net falsifiability is modest is the correct response, not a defect.
- The Birch, Schnell & Clayton paraphrase is verified exact as of 2026-08-08 and should not be "improved."
- **Methodological note for the corpus**: this article's failure mode — two adjacent citations in one paragraph, one paraphrased exactly and one contaminated by its neighbour's vocabulary — is a predictable hazard wherever two frameworks are set side by side as "parallel cases." Paragraphs that juxtapose two sources are worth checking per-source rather than as a unit.
