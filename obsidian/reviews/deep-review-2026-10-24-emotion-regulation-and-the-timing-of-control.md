---
title: "Deep Review - Emotion Regulation and the Timing of Control"
created: 2026-10-24
modified: 2026-10-24
human_modified: null
ai_modified: 2026-10-24T02:04:03+00:00
draft: false
description: "First deep review of the emotion-regulation timing article. Resolved the Sheppes & Meiran 2008 depletion flag from the authors' PDF, fixed an Ochsner abstract misdescription, and tightened four calibration points."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-24
last_curated: null
---

**Date**: 2026-10-24
**Article**: [[emotion-regulation-and-the-timing-of-control|Emotion Regulation and the Timing of Control]]
**Previous review**: Never (created 2026-10-23 ~20:55Z from [[research/emotion-regulation-and-the-timing-of-control-2026-10-23]])
**Word count**: 2699 → 2722 (+23, analyze_length; soft 3000, hard 4000)

## Driver Flag: Sheppes & Meiran 2008 and Ego Depletion

**Was the clause present?** Yes. L60 already read: *That cost is measured as "self control resources", the ego-depletion construct whose record [[mental-effort]] reviews.* It is in the creating commit `bf0bcd4d2c` (`git show HEAD:` grep, 1 hit) and in `hugo/content/topics/` (1 hit). The driver's zero was a false absence, probably from a hyphenated or differently worded probe ("self-control resources"; "ego depletion" without the hyphen).

**What the source measures.** The abstract (PubMed 19102598, raw efetch text) states the reappraisal-side cost only as "late reappraisal, relative to distraction, resulted in an expenditure of self control resources". The authors' PDF (tzin.bgu.ac.il/~nmeiran, pdftotext, grepped) settles the measure:
- "As in several previous studies, we used the Stroop task to assess ego depletion". The dependent measure was Stroop interference *after* the film. That is the classic sequential-task depletion paradigm.
- Groups: reappraisal n = 23, distraction n = 22. Result: t(43) = 2.18, p < .02 **one-tailed**, d = 0.66.
- No control group. The authors themselves: "we can conclude with relatively high confidence the relative but not absolute cognitive price for each strategy", and "we cannot determine whether distraction is more depleting than not regulating at all".
- The memory result is a cost of **late distraction**, not of reappraisal: "Late distraction but not reappraisal impaired memory encoding". So the research note's guard ("Use its memory result instead") cannot replace the reappraisal cost. The memory result is the other half of a double dissociation, not a non-depletion measure of reappraisal's cost.

**Resolution.** The old clause flagged depletion but still let "a cognitive cost for reappraisal" stand as a finding. L92 then leaned on it ("including the cost of late reappraisal"). Both are revised:
- L60 now reads: *The cost was measured as ego depletion, a larger Stroop effect afterwards than after late distraction, with no unregulated control group, so it carries the depletion record that [[mental-effort#depletion|the mental-effort article]] reviews. Late distraction instead impaired memory for the film.*
- L92: "including the cost of late reappraisal" → "including late reappraisal's weaker effect". The physical-architecture claim now rests on Sheppes & Meiran 2007's efficacy result, which is not a depletion measure.
- After the edits, nothing in the article rests on ego depletion.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Depletion leaning (L60, L92).** A calibration error inside the framework: a contested construct was presented as an established cost. Resolved as above.
- **Ochsner abstract misdescribed (L98).** "Ochsner's abstract reports neural correlates only" was inaccurate. The abstract also reports "reduced subjective experience of negative affect" and concludes that "prefrontal cortex is involved in constructing reappraisal strategies that can modulate activity in multiple emotion-processing systems". Now: "Ochsner's abstract attributes the modulation to prefrontal cortex". This is accurate and strengthens the physical-route point.

### Medium Issues Found
- **Position strength (L58).** Paul et al. write "This suggests that suppression was used preventively"; the article said "concluded". Changed to "suggested". The lede's "when used preventively" made the authors' interpretation into a condition, so it became "apparently when used preventively".
- **Over-concession and an unsupported monotone claim (L104).** "the finer their temporal resolution, the more completely each stage is described without consciousness" asserted a trend no source shows, and edged toward "operates without". Now: "at every temporal resolution reached so far, each stage is modelled without an experiential term". This is the substrate-neutrality point at the strength the record carries. The ambiguous "it" in "any claim that it is evidentially special" became "the location".
- **Calibration of the Stapp example (L100).** "the example supports a context-selection placement" became "illustrates". The paragraph had just called the Zeno account a posit, and a posit's worked case cannot support a placement. "Register without adopting" was checked against `tenets.md` L107 (a Process-1-only relocation "registered there as an alternative the Map could adopt but has not") and matches.
- **Attribution precision (lede, description).** "The model's authors" / "Its authors" narrowed the timing hypothesis, but the 1998 model is Gross's alone, and the narrowing is Sheppes & Gross 2011. Lede: "Sheppes and Gross (2011) narrowed it". Description: "Sheppes and Gross narrowed".
- **Chronology (L70).** "Carrying the model into self-control five years after that narrowing" implied the extension dates to 2016. The research note records the process model of self-control as Duckworth, Gendler & Gross 2014. Now "Writing on self-control five years after that narrowing". The 2016 quote verifies in the PMC full text.

### Low Issues (not changed)
- L68 "That abstract pools only these three families": an abstract reports pooled estimates rather than pooling. The meaning is clear and the absence scope is honest.
- L90 "which have the clearest evidence": a mild comparative. It is defensible, because the if-then figures are the only pooled benefit estimate for an explicit-control point that the article cites.
- L92 "each stage has an implicit form": a synthesis, not a sourced claim. It follows from L74's cases (Braunstein's implicit-automatic class; Gyurak's "automatic, routinized components to all"). Gross 2015's body is unread, so this is not attributed to it.

### Counterarguments Considered
- **Eliminative materialist / Dennett.** The record shows regulation without consciousness, so consciousness is idle. The article denies the inference in its own voice (L36, L78), with P-A4's symmetry. Nothing to fix.
- **Empiricist.** The placement predicts nothing. The article concedes this up front ("fit, not evidence"; "The fit discriminates nothing"). Nothing to fix.
- **Quantum skeptic.** The Stapp worked case is a reinterpretation of correlational fMRI. The article now states that the source's own account is prefrontal modulation, and calls the Zeno reading a posit. Nothing further.
- **Buddhist / constructionist.** No "before" exists for control to act on. §generation-regulation keeps this visible and scopes the timing talk to the appraisal end of the continuum. The continuum's direction was verified (PMC full text: "At the far left of the continuum … basic emotion models", so the right is constructionist).
- **Many-Worlds defender.** Not engaged; the article says so.

### Engagement classification (editor-internal)
- Affective scientists (Gross, Sheppes, Webb et al., Braunstein): Mode Three. Their models are named as needing no experiential term, and no refutation is claimed.
- Schwartz, Stapp & Beauregard 2005: an ally's posit, calibrated against Buhle 2014 and the clinical-neuroplasticity down-count. This is not an opponent reply.
- Constructionists (Barrett via Gross & Barrett 2011; Kappas): Mode Three. The disagreement is marked and scoped.
- No label leakage. The sweep found 0 hits for: direct-refutation, unsupported-jump, bedrock, Mode, "Evidential status", "Engagement classification", framework-internal, load-bearing, "This is not". Positive control: "Beauregard" 2 hits, "Gross (1998b)" 1 hit.

## Citation Ledger (publisher of record)

Sources: PubMed efetch raw abstracts (19 papers); Crossref metadata (all 24 DOIs); OpenAlex inverted-index abstracts (Gross 1998a, Gross 2015, Kappas, Torre, Webb SG); full texts grepped where body quotes occur (PMC efetch: Gyurak, Gross & Barrett, Duckworth; Europe PMC: Braunstein; authors' PDFs: Sheppes & Meiran 2008, Gross & John 2003; arXiv q-bio/0401019 for SSB 2005). Every quotation (45 checked by script after whitespace and hyphenation normalisation) greps in the raw text of the source named. Metadata tuples (authors, year, title, venue, volume(issue), pages) match Crossref for all 24 DOIs.

- Bonanno & Burton 2013 (Regulatory flexibility) — state: real-correct; "fallacy of uniform efficacy" in the abstract ("We label this assumption the fallacy of uniform efficacy"); the subtitle was confirmed in PubMed.
- Braunstein, Gross & Ochsner 2017 — state: real-correct; "the nature of the emotion regulation goal" and "ranging from more automatic to more controlled" are in the abstract; "ranging from implicit/nonconscious to explicit/conscious" is **body-only** (the abstract reads "ranging from to implicit to explicit"), found in the Europe PMC full text.
- Buhle et al. 2014 — state: real-correct; 48 studies; quote in the abstract. Ochsner is last author (stance: functional, no metaphysics).
- Duckworth, Gendler & Gross 2016 — state: real-correct; "as a rule, earlier intervention is best" is in the PMC full text (body), in a prescriptive-recommendation sentence.
- Goldin et al. 2008 — state: real-correct; "Seventeen women" (abstract); both quotes verbatim; the disgust clips are confirmed by the Stanford release (via ScienceDaily), as the full text is not on PMC.
- Gross 1998a (RGP) — state: real-correct; "may be regulated at five points…" is in the Crossref/OpenAlex abstract.
- Gross 1998b (JPSP) — state: real-correct (metadata); no quote.
- Gross 2015 — state: real-correct; "one type of valuation" and "three emotion regulation stages (identification, selection, implementation)" are in the OpenAlex abstract.
- Gross & Feldman Barrett 2011 — state: real-correct; quote in the PMC full text; the continuum direction was verified.
- Gross & John 2003 — state: real-correct; both definitional quotes verbatim in the PDF body; the scope sentence reads "These correlational studies do not address causal claims or the specific temporal ordering…", which supports L50's paraphrase.
- Gyurak, Gross & Etkin 2011 — state: real-correct; "proceeds without awareness" (in the §Emotional Conflict Adaptation case: "uninstructed, effortless and proceeds without awareness") and "have porous boundaries" are in the PMC full text.
- Kappas 2011 — state: real-correct; quote in the abstract.
- Koole & Rothermund 2011 — state: real-correct; both quotes in the abstract.
- Morawetz et al. 2017 — state: real-correct; "The left ventrolateral prefrontal cortex (VLPFC), the anterior insula and the supplementary motor area were consistently activated independent of the regulation strategy".
- Ochsner et al. 2002 — state: real-correct metadata; **article description corrected** (see Critical).
- Paul et al. 2013 — state: real-correct; quotes verbatim; the verb was corrected to "suggested".
- Schwartz, Stapp & Beauregard 2005 — state: real-correct; the Ochsner sentence is verbatim in arXiv q-bio/0401019 (raw pdftotext; double quotes in the preprint). The published PMC HTML carries the same sentence (WebFetch, past offset 100000), with ‘reappraise’ curly single quotes per the research note's [V-full] tag. "To illustrate this point we apply the quantum approach to the experiment of Ochsner et al. (2002)" licenses "worked example". "About fifteen Map articles": 16 live name-matches including this article.
- Seneca, *De Ira* II.4.1 (Stewart 1900; Latin Library) — state: real-correct; "is involuntary", "is combined with a wish, though not an obstinate one" and "is already beyond our control, because it overrides reason" are in Wikisource; *primus motus non uoluntarius* is in the Latin.
- Sheppes & Gross 2011 — state: real-correct; all seven quoted phrases are in the abstract; "revised conception" licenses "replace".
- Sheppes & Meiran 2007 — state: real-correct; both quotes in the abstract (sadness films; non-depletion efficacy measure).
- Sheppes & Meiran 2008 — state: real-correct metadata; **cost measure re-scoped** (subsequent-Stroop ego-depletion paradigm, one-tailed, no control); see Driver Flag.
- Thiruchselvam et al. 2011 — state: real-correct; quote in the abstract.
- Torre & Lieberman 2018 — state: real-correct; quote in the abstract.
- Webb, Miles & Sheeran 2012 — state: real-correct. Figures: 306 experimental comparisons; attentional deployment d+ = 0.00 ("had no effect on emotional outcomes"); response modulation 0.16; cognitive change 0.36; distraction 0.27; concentration −0.26. The comparison is strategy instruction against comparison conditions, pooled over experiential, behavioural and physiological outcomes, and the article states this correctly. The article does not cite the within-family 0.32 (suppressing expression), which leaves "response modulation a small effect (0.16)" accurate as the family figure.
- Webb, Schweiger Gallo et al. 2012 — state: real-correct; d+ = 0.91 vs no regulation instructions (k = 21) and 0.53 vs goal-intention instructions (k = 29), numbers only, as the guard requires.
- Southgate et al. 2026 (Self-Control as Skill and Scaffolding) — internal; "moments of policy" (L34, L86) and "The fit discriminates nothing." (L88) both grep.

**Result-direction leg.** Every empirical cite reports its result in the direction stated. Goldin's suppression increased amygdala and insula activity; Paul's suppression acted early; Webb's attentional deployment is null; Sheppes & Meiran 2007's late reappraisal was less effective. **Cited-author-stance leg.** All the affective scientists are functional or information-processing researchers, cited at the framework boundary (L88: "none of the affective scientists cited argues"). Only SSB 2005 is non-materialist, and its reading is reported as a posit. Seneca is flagged as a Stoic corporealist. **Superlative helper**: 0 hits. **Inline ↔ References**: 25/25 references cited inline; no inline cite lacks an entry.

**Internal anchors verified**: `alief-and-acting-against-belief#noticing-condition` (L109); `self-control-as-skill-and-scaffolding#where-selection-sits` (L80); `positions/agency-and-will#^p-a4` (asserts the symmetric verification limit); `tenets#^tenet-3-standing` (the quote is verbatim at L95); `tenets#^bidirectional-interaction`, `^minimal-quantum-interaction`, `^dualism`, `^no-many-worlds`, `^occams-limits`; `mental-effort#depletion` (heading "### Depletion", L82; sync slugifies heading-text anchors). The Tenet 2 statement at L106 matches `tenets.md` L69 (empirical-constraint minimality).

## Binding Guards Audit

- Substrate-neutral, fit not evidence (Tenet 3): held (L36, L92, L104).
- Implicit regulation needs no conscious contribution at any stage, and epiphenomenalism is not conceded: held (L36, L74, L78); L104 was tightened.
- Tenet 2 is empirical-constraint minimality: held (L106).
- Stapp: a posit; Buhle's physical route; no new evidence stream; question, not outcome: held (L100), and "supports" became "illustrates".
- Only Beauregard and SSB are non-materialists: held.
- No ego depletion and no goal priming: depletion leaning removed; "prim" has 0 hits; content-specificity has 0 hits.
- Gross, Sheppes & Urry working title: "Urry" has 0 hits.
- Scoped Ochsner absence in the body only: L98 only; the lede and description are clean.
- Coiners: process model and antecedent/response cut "proposed in Gross (1998b)", not "coined"; "process-specific timing hypothesis" is credited to Sheppes & Gross 2011 (now named in the lede); "point of no return" keeps "a possible".

## Optimistic Analysis Summary

### Strengths Preserved
- The two-clocks distinction (L52): when in the emotion, and which regulatory stage, with the three senses of "selection" disambiguated.
- Paul et al. as the hinge: "'Response-focused' names a target; when a given use acts is an empirical matter."
- The generic-versus-process-specific narrowing, set against Duckworth et al.'s later generic form. The domain asymmetry is left openly unresolved.
- L78's anti-epiphenomenalist analogy ("any more than an automatic route to an outcome shows that a deliberate route contributes nothing"), with P-A4's symmetry.
- The Stapp section's three calibrations. This is the first Map treatment of the Zeno mechanism's worked empirical case.
- The Seneca precedent, carefully fenced (Stoic corporealist; no mapping onto stages; no evidence).
- The Hardline Empiricist (Birch) persona praises the paired declines: no tenet-upgrade from early regulation's economy, and no upgrade from the Stapp example.

### Enhancements Made
- Depletion caveat with design specifics, plus the double-dissociation half that was missing (late distraction's memory cost).
- Ochsner's own physical account stated, which sharpens the posit calibration.
- Five precision and calibration edits (above).

### Cross-links Added
- [[mental-effort#depletion|the mental-effort article]]: replaces the bare [[mental-effort]] at L60 and points to the section that holds the replication record.

## Host-Side Findings (for the P3 cross-review; not edited)

- **`concepts/mental-effort` L106**: "[[emotion-regulation-and-the-timing-of-control|Cognitive reappraisal]], costly mainly when begun late, engages prefrontal regulatory circuits…". **Yes, this needs the same treatment.** "Costly … when begun late" rests only on Sheppes & Meiran 2008's subsequent-Stroop depletion measure (one-tailed, no control group). The page's own §Depletion (L84) reports the resource model failing in its standard paradigm (Hagger 2016 d = 0.04; Vohs 2021 d = 0.06). Early reappraisal's "minimal effort" is Sheppes & Gross 2011's *hypothesis*, not a measurement. A length-neutral fix: "costly mainly when begun late" → "less effective when begun late", which rests on Sheppes & Meiran 2007's efficacy result and not on depletion. Alternatively, revert to plain "Cognitive reappraisal". (mental-effort's integration is already marked done, so the cross-review will not revisit it unless told to. This needs its own pickup, either in the P3 cross-review's scope or as a small refine-draft.)
- **`topics/alief-and-acting-against-belief`** already carries the integration sentence ("the extended process model begins explicit regulation with identification…"). It is consistent with this article; no finding.
- **`concepts/control-theoretic-will`** (remaining): if the planned sentence quotes Sheppes & Gross's "require minimal effort", present it as their hypothesis, not a measured result. Do not cite Sheppes & Meiran 2008 as a measured cost without the depletion caveat.
- **`topics/clinical-neuroplasticity-evidence-for-bidirectional-causation`** (remaining): the planned Ochsner sentence can now cite Ochsner's own abstract ("prefrontal cortex … can modulate activity in multiple emotion-processing systems") as the physical reading alongside Buhle. Keep the L102–L104 down-count. Once that sentence lands, this article's L98 scoped absence ("A 2026-10-23 search found no live Map article discussing that experiment") remains true as dated, but a future reviewer should not re-flag it as stale.
- **`voids/numbing-void`** (remaining): no finding from this review.
- **Research-note guard defect**: `research/emotion-regulation-and-the-timing-of-control-2026-10-23` L306 and L799 call the 2008 memory result "the safer half" to "use instead". It is late *distraction's* cost, so it cannot stand in for reappraisal's. Future writers should not follow that guard literally.

## Remaining Items

None for this article.

## Stability Notes

- **Do not re-flag the depletion caveat as leaning on depletion.** L60 reports the 2008 cost and its measure precisely so that nothing rests on it. Removing the 2008 cite entirely would lose the double dissociation and the "first time" history, and that would be oscillation.
- **"Regulation needs no conscious contribution at any stage"** is a binding guard, stated deliberately in the article's voice. It is not an over-concession: L36 and L78 deny the epiphenomenalist inference in the same breath.
- **Physicalist personas will always read "fit, not evidence" as an admission that the selector is idle.** That is bedrock disagreement at the Tenet 3 boundary, and the article's calibration is honest at that tier.
- **The Seneca precedent** is fenced as "no evidence"; do not trim or expand it on evidential grounds.
- **The Stapp example's three calibrations** are complete. Further hedging would duplicate clinical-neuroplasticity's down-count, and strengthening would break the guard.
