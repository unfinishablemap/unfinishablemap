---
title: "Deep Review - Constitution vs Causal Work"
created: 2026-09-09
modified: 2026-09-09
human_modified:
ai_modified: 2026-09-09T10:21:07+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-09
last_curated:
---

**Date**: 2026-09-09
**Article**: [[constitution-vs-causal-work|Constitution vs Causal Work]]
**Previous review**: [[deep-review-2026-07-18-constitution-vs-causal-work|2026-07-18]] (third review; also [[deep-review-2026-06-04-constitution-vs-causal-work|2026-06-04]])
**Word count**: 1,566 → 2,019 (+453); status `ok` throughout (81% of the 2500 `concepts/` soft threshold)

This pass was not a no-op, and the reason matters for how future passes read the
two prior "stability" verdicts. The 2026-07-18 review closed with *"Article has
reached stability: two reviews, no content-level defects surviving the web-verify
pass. Future passes should expect no-ops absent a substantive edit to the body."*
The body was indeed not substantively edited. Three defects were nevertheless
live, because **two of them were never in the body's gift**: they are properties
of the article's relationship to sources that moved underneath it, and the third
had been mis-certified as clean by both prior reviews.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Stranded dependent of the 2026-09-05 asymbolia-localisation sweep.** The
article asserted, as flat fact and with no clinical source anywhere in its
reference list, that "insular and anterior-cingulate damage disrupts valence-prior
assignment while sensory cortex stays intact." That sentence is inherited
near-verbatim from [[pain-asymbolia]]. On 2026-09-05, commit `e6ae985948`
(`auto(refine-draft)`) corrected "**two live loci**" that "state pain asymbolia's
*insula* localisation more confidently than the primary literature supports."
Its two loci were `concepts/pain-asymbolia` and
`topics/pain-consciousness-and-causal-power`. A corpus-wide grep for the sentence
finds **three** obsidian loci; this article was the third, and the sweep never
touched it. In `pain-asymbolia` the sentence now sits downstream of an explicit
paragraph recording that the localisation "rests on a thinner record than textbook
summaries suggest" — Feinstein et al. (2016): *"No studies have replicated the
original finding of pain asymbolia following insula damage"*, with the classic
lesions extending into parietal operculum, secondary somatosensory cortex and
supramarginal gyrus. Here the sentence stood bare, with the qualifier stripped and
no route to it.

Note the direction: the claim is the *rival's* story, so overstating its
anatomical cleanliness is an **over-concession**, not a Map-favourable overclaim.
That is why it collected two clean bills of health rather than being challenged —
the over-concession-gets-ratified pattern. It is a defect
either way: the anatomy was doing real argumentative work (it is what made the
rival *predict the same dissociation*) on an unsourced empirical premise.

*Resolution*: the anatomy is now scoped as the weaker part of the rival's story,
sourced to Feinstein et al. (2016) with the lesion-extent record, routed to
[[pain-asymbolia]] for the full account, and — the substantive point — the
argument is explicitly detached from it. Both readings need only that valence-prior
assignment and stimulus detection come apart *somewhere*. **This hedge is an
empirical-fidelity fix carrying a citation, not anchoring padding**; it does not
touch the 2026-06-04 stability note about the anchoring register artifact, which
still stands.

**2. Quote cited to a source that no longer contains it; dependency account
drifted.** The catalogue entry for [[consciousness-and-causal-powers]] said the
bridge formulation "appears as the Map's *'actual disagreement with PP,'*"
distinguishing architecture from implementation. `find('actual disagreement')` in
that article returns **−1**. This is drift, not fabrication: `git log -S` shows the
phrase originated in this article's own creation commit (`777a5eee98`, 2026-06-04),
lived in `consciousness-and-causal-powers` until `5001936a30` (2026-09-07,
`auto(refine-draft)` discharging six defects from the 2026-09-07 ChatGPT outer
review), and died there. The 2026-07-18 review checked this exact string and
correctly found it present; it went stale 51 days later.

The rewrite did more than delete a phrase. It replaced the generic PP rival with
predictive processing's most demanding form — Laukkonen, Friston and Chandaria's
(2025) beautiful-loop account — so **the constitution side of the bridge is now
occupied by *the recursion*, not by computational role in general**. This page is
the bridge's definitional home; its account of the strongest rival's own
formulation of that bridge was a version behind.

*Resolution*: dead quote removed; entry rewritten to state the current
formulation, name the September 2026 revision, and mark that the locus is
unchanged while what sits on the constitution side has been sharpened.

**3. Catalogue incomplete — the full-strength engagement was missing.**
[[predictive-processing-and-dualism]] (4,957 words, created 2026-09-05) steelmans
the beautiful-loop account in its own vocabulary and contains the catalogue's most
explicit statement of what the causal-work reading claims: the recursion
*"specifies but does not generate"* the felt side, with the residue marked a
framework boundary "rather than a refutation either way." On a page that says
"Cataloguing the deployers is part of what this page is for," its absence was a
defect of the article's stated function. Added as a deployer, to Further Reading,
and to `related_articles`.

**4. Orphan references, mis-certified clean by both prior reviews.** Clark (2016)
and Hohwy (2013) sat in the reference list and were **never cited inline** —
`find('Clark')` in the body returned −1. I checked all four commits in the file's
history: they have been orphans since creation. Both the 2026-06-04 and 2026-07-18
ledgers recorded *"Inline ↔ References cross-reference: clean."* Neither check was
performed against the body. This is the
already-checked-fence pattern: a prior certification made the defect
un-look-at-able.

*Resolution*: the fix converges with issue 1 — Clark and Hohwy are now cited
inline at exactly the claim they underwrite (affective valence entering as a
separate hierarchical prior), which discharges the orphan and sources the rival's
framework in one edit.

### §2.4 Publisher-of-Record Citation Web-Verify Ledger

Verified at Crossref this pass (not carried over from the prior ledger):

- **Saad, B. (2025). *A dualist theory of experience*. *Philosophical Studies*.** — **real-correct**. Crossref `10.1007/s11098-025-02290-3` returns volume **182**, issue **3-4**, pages **939-967**, author Bradford Saad. ⚠️ **This adjudicates a live corpus-wide inconsistency in the minority form's favour.** The corpus carries three forms — ~142 × `182(3)`, ~45 × `182(3-4)`, ~18 × `182(3–4)` (en-dash). The **publisher of record says `3-4`**, so this file's form is right and the 142-locus majority is wrong. The 2026-07-18 ledger recorded `182(3)` as "real-correct"; that entry was mistaken on the issue field. Per the driver's scope fence I changed nothing and minted no task, but the sweep, when it happens, should normalise **toward** `3-4`, not away from it.
- **Feinstein, J. S., Khalsa, S. S., Salomons, T. V., Prkachin, K. M., Frey-Law, L. A., Lee, J. E., Tranel, D., & Rudrauf, D. (2016; online first 2015).** — **real-correct**, newly added. Crossref `10.1007/s00429-014-0986-3`: *Brain Structure and Function* **221**(3), 1499–1511, online 2015-01-11. Eight authors, order verified. Matches [[pain-asymbolia]]'s existing entry.
- **Laukkonen, R. E., Friston, K. J., & Chandaria, S. (2025).** — **real-correct**, newly added. Crossref `10.1016/j.neubiorev.2025.106296`: *Neuroscience & Biobehavioral Reviews* **176**, article 106296, issued 2025-09. (Crossref's bibliographic search surfaces only the PsyArXiv preprints `10.31234/osf.io/daf5n*`, one of which omits Friston — the journal DOI is the record to cite.) Form matches the two sibling articles that already cite it.
- **Clark, A. (2016). *Surfing Uncertainty*. OUP** — **real-correct**; no longer an orphan.
- **Hohwy, J. (2013). *The Predictive Mind*. OUP** — **real-correct**; no longer an orphan.
- Map self-cites (pseudonyms Oquatre-six / Sonquatre-cinq / Oquatre-sept) — in-house convention, never strip.
- Superlative-claim currency sweep: `find_superlative_claims` returns **0**. Not applicable.
- Inline ↔ References cross-reference: **clean as of this pass** — and, unlike the two prior assertions of this, actually measured against the body text.

### Quote-Fidelity Checks (all strings grep-verified in raw sources)

| Quoted string | Source | Offset |
|---|---|---|
| "is shared explanandum" | `concepts/pain-asymbolia` | 13914 |
| "would commit exactly the calibration error" | `topics/co-optimization-reply-to-the-correlation-problem` | 14838 |
| "without qualification" | `topics/predictive-processing-and-dualism` | 19343 |
| "specifies but does not generate" | `topics/predictive-processing-and-dualism` | 14185 |
| "actual disagreement with PP" | `topics/consciousness-and-causal-powers` | **−1 → removed** |

Catalogue entries independently verified against each deployer: `delegatory-causation`
carries "default causal profile" (qualifier intact — the dropped-qualifier check
passes); `bidirectional-interaction` and `phenomenal-transparency-opacity-spectrum`
both carry "doing causal work"; `pain-asymbolia`'s verbatim bridge quote is
faithful; `co-optimization-reply`'s "equally consistent" characterisation is
faithful. All bare wikilink targets confirmed present in `build_content_index`
with no slug collisions.

### Medium Issues Found

**"The discipline this page installs forbids that."** A page cannot forbid a move
by declaring it forbidden, and the sentence also contradicted the article's own
self-description three times over — the lead calls the page a "named **dialectical
locus**," and §"The Move Is…" itself calls constrain-vs-establish "the companion
discipline." The article does not install a discipline; it defines a locus.

The underlying constraint does exist and is enforced, just not here. I traced it:
[[evidential-status-discipline]] §"Compatibility vs. Support at the Rival-Model
Interface" installs the independent-discriminator requirement, and §"The Diagnostic
Test" is implemented verbatim in the `/deep-review` skill's own §2. So the fix was
to reattribute rather than delete. I also ran the empirical question the section
invited — *has any Map article actually used relocation the way this section calls
illegitimate?* — against the deployer list. **No.** Every deployer concedes the
shared explanandum in its own text, and three do so quotably. Those concessions are
now cited in the section, converting an unearned promise into a checkable audit
trail. Resolved.

### Counterarguments Considered

**"The claimed symmetry is unearned — the Map gains precision from relocation; what
does the rival gain?"** *Discarded, on evidence.* The article's symmetry claim is
not about equal gains; it is about the discipline blocking each side's
characteristic over-claim, and that bidirectionality is explicitly installed by the
companion discipline. [[evidential-status-discipline]] §"Constrain vs. Establish"
carries a subsection titled **"The symmetric form"**: *"The dualist must not treat
phenomenological evidence… as if it had established dualism… The materialist must
not treat neural-correlate or stimulation evidence as if it had established the
reduction… The asymmetry the discipline guards against is the tendency for the
house perspective — whichever it is — to silently treat constraint as
establishment when the evidence runs in its favour."* The article's framing
restates a rule the discipline genuinely holds bidirectionally, and its closing
verdict ("the evidence constrains the field of readings without discriminating
between the two that survive") is the correct compatibility-not-support label. No
change warranted; recorded below so future passes do not re-litigate it.

**Six adversarial personas.** No new critical findings. The Eliminative
Materialist's and Hard-Nosed Physicalist's objections land at the tenet boundary,
where the article already declines to adjudicate; the Quantum Skeptic and
Many-Worlds Defender have no purchase on a page that posits no mechanism and makes
no indexical claim; Popper's Ghost is answered by the article's own refusal to
treat the dissociation as discriminating evidence. Nagarjuna's charge — that
"constitution" and "causal work" may be a distinction without a difference once
inherent existence is dropped — is the sharpest available, and it is bedrock: it
denies the framework in which the bridge is a question at all.

**Possibility/probability slippage — diagnostic test applied.** Would a reviewer
who fully accepts the Map's tenets still flag any claim here as overstated relative
to the five-tier scale? **No.** The article grades its own reading as a "live
hypothesis," states that the tenets "*motivate*… and *remove* the standard
physicalist reason to default to constitution — but they do not, by themselves,
supply positive evidence," and declines to declare the dispute resolved. Calibration
is honest at its tier. The one place slippage could have hidden — the Map-favourable
clause inside a concession structure, which this entire article is — was the
"forbids that" sentence, now fixed.

## Optimistic Analysis Summary

### Strengths Preserved

- The lead's front-loaded three-clause definition (dissociation / methodological rule / bridge) is truncation-resilient and was left untouched.
- "Defining a battlefield is not the same as declaring a winner" — the article's best line, and its thesis in nine words.
- §"The Distinction"'s two-reading structure, and the observation that the distinction "is structural… silent about *which* mechanism is operative and silent about *whether* the surplus… is real." Preserved verbatim.
- The §"Relation to Site Perspective" derivation of the bridge from Tenets 1 and 3, including the epiphenomenalism consequence — substantive tenet engagement, not boilerplate. Untouched.
- The article's willingness to pre-empt the charge against itself in a dedicated section. That section needed a correction, not removal.

### Enhancements Made

- The rival's own account is now sourced (Clark; Hohwy) rather than asserted, which strengthens the steelman the relocation argument depends on.
- The "audit trail" turn in §"The Move Is…" gives the page a function it previously only claimed: the catalogue is now evidence that the constraint is observed, not a list of places the move appears.
- The catalogue now tracks the rival's strongest current form rather than a superseded generic version.

### Cross-links Added

- [[predictive-processing-and-dualism]] — as deployer, in Further Reading, and in `related_articles`
- [[pain-asymbolia]] — second inbound link, now carrying the localisation record
- [[co-optimization-reply-to-the-correlation-problem]] — promoted from catalogue-only to a cited concession

## Remaining Items

None for this article. One corpus-level item recorded but deliberately not
actioned, per the driver's scope fence: the Saad (2025) issue-number inconsistency
(~205 loci across three forms) now has a publisher-of-record answer — **`182(3-4)`**
— which points the eventual sweep in the opposite direction from the corpus
majority. No task minted.

## Stability Notes

- **The 2026-06-04 anchoring note still stands**: the anchoring under-hedge flag is a register artifact for this definitional page. The hedge added this pass is a *sourced empirical correction*, not a response to that flag. Do not read it as licence to pad.
- **Map self-cite pseudonyms are the in-house convention — never strip.**
- **The symmetry objection is settled, not open.** It was raised and discarded on evidence this pass (see Counterarguments). It is backed by [[evidential-status-discipline]] §"Constrain vs. Establish" → "The symmetric form". Do not re-flag.
- **Nagarjuna's distinction-without-a-difference charge is bedrock.** It denies the framework in which the bridge is a question. Not a fixable defect.
- **Correction to the two prior stability verdicts.** Both said the article had converged and future passes should expect no-ops "absent a substantive edit to the body." That inference does not hold for this page, and the reason generalises: **this article is a catalogue of other articles and a quoter of their prose, so its correctness is a function of its dependencies, not of its own diff.** A dependency rewrite 51 days later killed a quote it cites; a sibling's sweep stranded a claim it inherited; a new 4,957-word deployer appeared and went uncatalogued. None of that shows in this file's `git log`. **Future passes on this page should diff the dependencies since `last_deep_review`, not this file** — the two high-movement ones this pass were `topics/consciousness-and-causal-powers` (8 commits, and the subject of the 2026-09-07 three-way outer review) and `concepts/pain-asymbolia`, and both had in fact drifted. Convergence damping should be applied to this page with that caveat in mind.
- **Two prior "cross-reference clean" certifications were false.** Clark and Hohwy were orphan references from creation through both reviews. Assert that check against the body text, not from the prior ledger.
