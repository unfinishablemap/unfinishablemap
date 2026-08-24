---
ai_contribution: 100
ai_generated_date: 2026-08-24
ai_modified: 2026-08-24 12:26:42+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-24
date: &id001 2026-08-24
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-24 12:26:42+00:00
modified: *id001
related_articles: []
title: Deep Review - Single-Cell Proto-Agency and the Evidence Problem
topics: []
---

**Date**: 2026-08-24
**Article**: [Single-Cell Proto-Agency and the Evidence Problem](/topics/single-cell-proto-agency-and-the-evidence-problem/)
**Previous reviews**: [2026-07-25](/reviews/deep-review-2026-07-25-single-cell-proto-agency-and-the-evidence-problem/) (no-op convergence pass), [2026-07-16](/reviews/deep-review-2026-07-16-single-cell-proto-agency-and-the-evidence-problem/) (full citation ledger)

## Outcome: four critical issues in a "converged" article

Both prior reviews closed with "converged / no remaining items", and the body prose
had been byte-identical since 2026-07-16. This pass found **four critical defects**,
none of which the prior lenses could have caught. Two concern how the article uses
its sources, two how it uses the Map's own framework:

1. a **mis-attributed lab** on a citation whose *metadata* is flawless (so the
   07-16 metadata ledger graded it `real-correct` and the 07-25 pass declined to
   re-open it);
2. a **misuse of the Map's own `interface-threshold` construct** that inverts what
   the concept page says and over-strengthens the article's conclusion;
3. a **claim anchored to a source that is silent on it** — true, but the cited paper
   says nothing about it;
4. an **over-reach past the best available source**, asserting unfalsifiability where
   the source says triviality.

This is the `convergence-damping-keys-on-self-modification-not-dependency-freshness`
shape: a clean streak is not evidence of correctness. Note the diagnosis that
*failed* — the working hypothesis on entry was dependency drift (three named
dependencies moved after the last review). **Dependency drift turned out to be
zero.** The defects were original and had been present since creation.

## Pessimistic Analysis Summary

### Critical Issues Found

**C1 — Mis-attributed laboratory on a metadata-correct citation (fixed).**
The article read:

> Victor Sourjik, a co-author of the deflationary opinion, **runs the Max Planck lab
> whose single-cell FRET measurements first quantified the CheY-P variability at
> issue** (Keegstra et al., 2017). The person who *measured* the noise is on record
> calling it noise.

Verified at the publisher of record (eLife 6:e27455, author/affiliation block):
authors are Keegstra (AMOLF), Kamino (Yale), Anquez (AMOLF), Lazova, Emonet (Yale),
Shimizu (AMOLF). **Sourjik is not an author; no Max Planck affiliation appears on
the paper.** It is a Shimizu/Emonet paper.

Load-bearing, not decorative: the next two sentences ("The person who *measured* the
noise is on record calling it noise… which is the evidence problem in miniature")
rest entirely on the mis-attribution.

*Fix applied* — rescoped rather than deleted, because the epistemological point
survives in accurate form and is arguably sharper. Sourjik **did** introduce in vivo
FRET to bacterial chemotaxis (Sourjik & Berg 2002, *PNAS* 99(20):12669–12674,
doi:10.1073/pnas.192463199, resolved at Crossref), which is the technique the
Keegstra measurements depend on. The article now says he developed the means of
seeing the noise, and attributes the measurements to the Shimizu and Emonet labs.
Sourjik & Berg 2002 added to References.

**Why three reviews missed it.** The 07-16 ledger graded Keegstra 2017
`real-correct` — a *metadata* verdict, and correct as such. The 07-25 pass
explicitly declined to re-litigate the ledger. Two optimistic reviews then
*positively ratified* the mis-framing, both calling the Sourjik detail "a superb
piece of epistemic reporting"
([optimistic-2026-07-16-minimal-organism-decoupling](/reviews/optimistic-2026-07-16-minimal-organism-decoupling/) L60,
[optimistic-2026-07-25-minimal-organism-evidence-cluster](/reviews/optimistic-2026-07-25-minimal-organism-evidence-cluster/) L54). A prior correction
pass touched this very cite and stopped short: the W29 changelog records the *venue*
corrected from "PNAS" to eLife, leaving the author list and lab attribution
untouched. Textbook `empirical-claim-fidelity-orthogonal-to-metadata-and-quotes`.

**Root cause fixed too.** The source research note
[single-cell-proto-agency-and-the-evidence-problem-2026-07-15](/research/single-cell-proto-agency-and-the-evidence-problem-2026-07-15/) is wrong at
the root (L44: "Sourjik's own lab (Max Planck, Marburg) produced the single-cell FRET
measurements"; L48 listed Sourjik in the author string and the venue as PNAS).
Corrected in place with dated correction markers at five loci, per
`research-note-self-flagged-gaps-propagate-to-the-article`.

**C2 — Misuse of the Map's own `interface-threshold` construct (fixed).**
The article read:

> The prokaryotic cell has no neural substrate for such an interface, so on the Map's
> framework the single cell is **below any candidate interface threshold**—which is
> precisely why the "extra" that proto-choice would name has **nowhere to attach and
> no way to show itself**.

`interface-threshold` is listed in the article's own `concepts:` frontmatter, and the
concept page says close to the opposite of what this usage implies:

- "The threshold is about coupling architecture, not consciousness itself. **Below it,
  phenomenal consciousness may well be present**" (L68)
- "**A simple organism may have minimal phenomenal experience** without an interface
  rich enough for the experience to direct behaviour." (L70)
- "the threshold concept itself is **neutral on substrate**" (L100)

So "below the threshold" in the Map's vocabulary means the coupling is *receptive
rather than selective*, **not** that there is nothing to attach to. The inference
as written is invalid inside the Map's own framework.

Two further errors rode along: the criterion was given as "no neural substrate"
(the concept page is explicitly substrate-neutral), and the minimality half of the
argument was attributed to **Tenet 3** when the corpus assigns it to **Tenet 2**
(cf. [competency-without-felt-experience](/apex/competency-without-felt-experience/) L47: "minimality forbids positing
an interface where there is no neural substrate to host one (Tenet 2)"). Tenet 2 did
not appear in the article at all.

*Diagnostic test applied* (§2 of the skill): would a reviewer who **fully accepts**
the Map's tenets still flag this? **Yes** — the article's own linked concept page
contradicts the inference. Therefore a calibration/framework error, not a bedrock
disagreement.

*Fix applied* — the Tenet-3 paragraph now assigns minimality to Tenet 2, states the
declination as a decision about what to posit rather than a finding that the cell is
empty, and then uses the threshold construct **correctly**, which yields a second and
more robust route to the same conclusion: grant the bacterium minimal experience for
argument's sake, and a sub-threshold coupling would still be receptive rather than
selective — riding along without redirecting the swimming, so the behaviour would look
exactly as it does. The undecidability therefore no longer depends on denying the cell
anything. `[[interface-threshold]]` is now linked from the body (previously it was
claimed in frontmatter but never engaged).

**Precedent**: the corpus repaired this exact defect shape in `apex/machine-question`
on 2026-08-24 (a categorical "falls below the interface threshold by construction"
register against a "conditional rather than categorical" verdict). The single-cell
article carried the unrepaired twin, and was the **only** live article using the term
in the organism-floor "nothing there" sense — corpus-wide grep confirms every other
use is the technical selection-grade sense.

**C3 — A claim anchored to a source that is silent on it (fixed).** The UAL
paragraph asserted "Bacteria show habituation and sensitisation but not unlimited
associative learning." The only citable anchor in that paragraph is Birch, Ginsburg &
Jablonka 2020 — and a raw grep of that paper's 68k-character JATS full text
(PMC7116763) returns `habituat`=0, `sensitis/sensitiz`=0, `prokaryot`=0, and
`bacteri`=1, that one hit being an analogy about *life* ("A bacterium is alive,
whereas a single molecule of sugar is not alive"), not about learning.

The claim is **true**; it was unsupported and mis-anchored. Two real sources verified
verbatim and now cited:

- **Ginsburg, S., & Jablonka, E. (2021)**, "Evolutionary transitions in learning and
  cognition," *Phil. Trans. R. Soc. B* 376(1821):20190766,
  doi:10.1098/rstb.2019.0766 — "Learning by habituation and sensitization has been
  found in bacteria [1], plants [4], slime moulds and fungi". The ideal cite: it is
  Ginsburg and Jablonka *themselves* making the bacteria attribution, which is exactly
  what the sentence needed.
- **Lyon, P. (2015)**, "The cognitive cell: bacterial behavior reconsidered,"
  *Frontiers in Microbiology* 6:264, doi:10.3389/fmicb.2015.00264 — "Habituation and
  sensitization have both been demonstrated in bacterial CT". Directly on the
  article's subject. ⚠️ **A different Lyon paper from the 2020 one already in the
  block** — both are now present and the inline mention of the 2020 one has been
  year-tagged to keep them distinct.

Deliberately *not* chased further upstream: Lyon's own primary is Koshland, Goldbeter
& Stock (1982) *Science* 217(4556):220–225, which is about amplification and
adaptation and is **not** a habituation demonstration. Citing it directly would
overreach.

*Positive result on the same paragraph*: the "positive marker only" characterisation
of UAL **is** faithful, and has been upgraded to a verbatim quote — "it can tell us
which animals are conscious, but it does not aspire to tell us which are not" (Birch,
Ginsburg & Jablonka 2020, grep-verified in the raw JATS). If anything the article had
understated how emphatic the authors are.

**C4 — Over-reach beyond the best available source (fixed).** The FEP paragraph read
"which makes the criterion **hard to falsify**." The strongest real source for the
over-generality objection — **Colombo, M., & Palacios, P. (2021)**,
*Biology & Philosophy* 36(5):41, doi:10.1007/s10539-021-09818-x — says the FEP
"generalizes to all 'existing' systems, **risking triviality**" and amounts to "a
maximally general definition of any system that persists" that "does not seem to
provide us with any new insight into biological systems." They do **not** say
unfalsifiable. Rescoped to triviality / lack of discriminating content, with the
source cited — which is anyway the clause the argument needs, since the very next
sentence is "It *classifies* without *discriminating*." The section's opening
sentence, which promised a candidate that "risks unfalsifiability", was a stranded
dependent and was repointed to triviality in the same pass.

⚠️ **Two citation traps avoided, recorded so nobody walks into them later:**

- **Andrews, M. (2021)**, *Biology & Philosophy* 36(3), doi:10.1007/s10539-021-09807-0
  — *reports* the falsifiability critique and then **rejects** it as resting on "a
  category error." Citing her as a critic making the objection would **invert** her
  position.
- **Sánchez-Cañizares (2021)**, *Entropy* 23(2):238 — tops every search for "FEP
  criticism", is **not** by Mel Andrews (an easy mis-attribution), and largely
  *defends* the FEP.
- Colombo & Wright (2021), *Synthese* 198(Suppl 14):3463–3488, was **not** cited: its
  abstract only *reports* that the FEP "has been called… an unfalsifiable principle",
  and the body could not be retrieved to confirm the authors endorse the objection.
  Unverified body, so not cited.

### Medium Issues Found

**M0 — Disciplinary mis-grouping and an imprecise paraphrase (fixed).** The
candidate-criteria paragraph opened "Recent **philosophy of biology** cashes out
agency…" and grouped MacDermott et al. 2024 under it. That paper is AI-safety/ML
(Imperial College / Google DeepMind / London Initiative for Safe AI, NeurIPS),
motivated by "concerns about harm from AI" — philosophically relevant by its own
statement, but not philosophy of biology. Widened to "philosophy of biology and…
formal agency research."

Both paraphrases in that paragraph were otherwise verified faithful. Two precisions
taken while there: Watson's "relational" is specifically **part-whole** relational
(a system more agential than the sum of its parts), not agent-environment, and is now
stated that way; and MacDermott et al.'s contrast is now quoted in their own words —
"a continuous measure of goal-directedness rather than a binary notion of agency"
(the word "threshold" appears zero times in their paper, so the article's original
"rather than declaring a threshold" was true but weaker than the available quote).

**M1 — Uncited empirical claim (fixed).** "Later work found noise *increases* the
motor's sensitivity to the signal rather than degrading it" carried no citation and no
named author. The real source was sitting in the research note's own citation list and
had never been carried into the article: **He, R., Zhang, R., & Yuan, J. (2016),
"Noise-Induced Increase of Sensitivity in Bacterial Chemotaxis," *Biophysical Journal*
111(2):430–437, doi:10.1016/j.bpj.2016.06.013** (resolved at Crossref; abstract
retrieved via EuropePMC).

The paraphrase was also slightly off and has been tightened. The abstract says the
noise "increases the sensitivity of the bacterial chemotaxis **network** downstream
**at the level of** the flagellar motor" — a network-sensitivity result measured at
the motor, not "the motor's sensitivity". Now stated in the paper's own terms, with
the wild-type-vs-noiseless-mutant comparison named.

**M1b — Two stranded dependents of the C2 fix (fixed).** After repairing the
paragraph that *states* the interface declination, two later sentences were still
leaning on the rejected categorical reading — the
`sweep-fixes-the-disclaimer-and-strands-its-dependents` shape, which grep does not
catch because the dependency is semantic. Both asserted absence outright:

- §Tractability: "at the floor where the mechanism is complete and **the substrate for
  anything more is absent**" → "…and the framework posits no interface for anything
  more".
- §Relation to Site Perspective, closing paragraph: "where the behaviour is fully
  explained and **the substrate for anything further is absent**" → "…and the Map
  posits no interface for anything further to occupy".

A targeted sweep for the remaining absence-asserting constructions
(`is absent`, `nothing to attach`, `no way to show`, `cannot ever`, `in principle
undetectable`, `the cell hosts nothing`, `is inert`) now returns clean. The one
surviving "no neural substrate" locus (§Tractability) is explicitly framework-relative
and factually true of prokaryotes, so it was left as is.

**M2 — Under-specification against the positions register (fixed).** The article
framed the Tenet-5 parsimony symmetry as a pure standoff: "the residue is not a tie to
be broken by more data but a boundary of what data can decide." The register entry
governing this rung, **P-CS5** in [consciousness-scope](/positions/consciousness-scope/), is more committed:
parsimony's default ("no coupling, nothing chosen, nothing felt") is *undefeated but
not positively established* — "the Map endorses it as the reading the behaviour
matches while denying it is proven," at **moderate** credence.

The article was not wrong in anything it said, but it never stated the register's
endorsement, and the linkage was one-directional: P-CS5's `Argued in` names this
article first, while the article contained zero occurrences of `positions/` or
`P-CS`. Cf. `analysis-doc-cites-the-article-article-never-cites-back`.

*Fix applied* — P-CS5 now cited in the lead, in the Tenet-5 section (with the
register's asymmetry stated and its moderate credence named as governing), in Further
Reading, and in `related_articles`. This also resolves a latent tension between the
"no threshold-crossing fact to discover" phrasing in the candidate-criteria section
and the epistemic-limit reading elsewhere: the register settles which the Map holds.

### Counterarguments Considered

- **Eliminative materialist**: "proto-choice" is a folk-psychological placeholder with
  no referent, so undecidability is trivial. Already engaged — the article concedes the
  live question is "whether 'harnessed stochastic search with a memory' earns agency
  vocabulary at all… a conceptual question." Bedrock; no change.
- **Dennettian intentional stance**: proto-agency is a real pattern under a stance.
  Same disposition. Bedrock; no change.
- **Tenet-accepting reviewer on C2**: this one is *not* bedrock and was actioned — see
  the diagnostic test above.

## Optimistic Analysis Summary

### Strengths Preserved

- The reframing from "do cells choose?" to "what observation could discriminate?" —
  the article's distinctive contribution. Untouched.
- The Source/Map separation disclaimer ("This convergence is the Map's own reading of
  the two literatures rather than a published position on either side"). Untouched.
- The hedging of the intractability thesis as an explicit wager, with the optimist's
  counter-bet stated. Untouched.
- Evidential calibration: no possibility/probability slippage found. The article argues
  *undecidability* and never inflates the status of bacterial proto-agency. The C2 fix
  moves it further in the restraint direction, not less.

### Enhancements Made

- The threshold argument now runs as a conditional that survives granting the
  bacterium minimal experience — strictly more robust than the version it replaces,
  and it costs the article nothing.
- Two real citations added where claims previously dangled or mis-attributed.
- Tenet 2 now represented; the lead's tenet list updated to match.

### Cross-links Added

- [P-CS5](/positions/consciousness-scope/) (lead, Tenet-5 section, Further Reading,
  `related_articles`)
- [interface-threshold](/concepts/interface-threshold/) (body — previously frontmatter-only)

## Dependency-Drift Check (negative result, recorded)

Three dependencies moved after the last review. All three characterisations **still
hold**; no staleness found:

| Dependency | Changed | Article's claim about it |
|---|---|---|
| `bacterial-chemotaxis-and-minimal-biogenic-cognition` | deep-reviewed 08-01, refined 08-07 | "parks exactly this question" — still true verbatim (its L76); the 08-01 review listed the parking as a strength to preserve |
| `voids/agency-void` | 08-06 wikilink repoint; 08-13 evidential downgrade | verification-circularity claim untouched by both edits. **Near-miss**: the 08-13 edit retracted "the void is *evidence* for the interface" — a claim this article never made |
| `apex/competency-without-felt-experience` | 07-31 retitle, 08-07 grain ceiling | retitle already absorbed; the negative claim quoted ("competency never settles the phenomenal question") still asserted |

Shared-citation family resolution: only **Robinson et al. 2024** is genuinely shared
with the sibling, and it is byte-identical field-for-field. Keegstra/Sneddon/Yi have
never appeared in the sibling (`git log -S` returns zero commits). No divergence.

Minor, not actioned: the apex's `apex_sources:` list omits this article, which appears
there only as an inline body citation. "Feeds" is defensible; formal source-list
membership is a separate question for `apex-evolve`.

## Length

2224 → 2805 words (topics/ soft 3000, hard 4000; `status: ok`). Below soft threshold,
so normal-mode improvements were permitted; no condensation triggered. Most of the
growth is citation apparatus and quoted source language, not new argument.

## Reasoning-Mode Classification (editor-internal)

- Engagement with the deflationists (Robinson et al. / Sourjik): **Mode Three
  (framework-boundary marking)**, unchanged from 07-16, and now cleaner. The C2 fix
  removes an implicit over-reach — the old text let a framework-relative declination
  read as a finding about the cell. Boundary is now marked as a posit-declination with
  the register's calibration attached.
- No editor-vocabulary leakage in prose (scanned; clean).

## Publisher-of-Record Citation Ledger

The 07-16 ledger covered *metadata* for the then-existing cites and its verdicts
stand; this pass covered **body-claim fidelity** (the orthogonal channel) plus every
newly added cite. Per-cite state:

- Robinson et al. 2024 (*EMBO Reports*) — **real-correct**, metadata carried from
  07-16; four quotes verified there. Body framing re-checked this pass: sound.
- Keegstra et al. 2017 (*eLife* 6:e27455) — **metadata real-correct**, but
  **body-claim wrong** (lab/author mis-attribution). Body claim corrected; cite kept.
- Sourjik & Berg 2002 (*PNAS* 99(20):12669–12674) — **added**, resolved at Crossref.
- He, Zhang & Yuan 2016 (*Biophys. J.* 111(2):430–437) — **added**; abstract
  raw-verified via EuropePMC; paraphrase tightened to the paper's own scope.
- Sneddon, Pontius & Emonet 2012; Yi et al. 2000 — **real-correct**, carried from
  07-16, References block unchanged for these.
- Watson 2023 (*Biological Theory* 19(1):22–36) — metadata carried from 07-16;
  **paraphrase verified faithful** this pass, with "relational" precisified to
  part-whole. *Noted, not changed*: EuropePMC records the print issue as 2024
  (online-first 2023); "2023" is the online-first convention, a known choice.
- MacDermott et al. 2024 (arXiv:2412.04758) — metadata carried from 07-16; NeurIPS
  2024 acceptance confirmed in the arXiv comment field; **paraphrase verified
  faithful** and upgraded to the authors' own wording.
- Birch, Ginsburg & Jablonka 2020 — **real-correct**, and the "positive marker only"
  reading **verified verbatim** in the raw JATS. But it does **not** support the
  bacteria-learning sentence anchored to it → see C3.
- Ginsburg & Jablonka 2021; Lyon 2015; Colombo & Palacios 2021 — **added**, each with
  a verbatim span verified at the source.
- Brancazio et al. 2020; Lyon 2020 — **real-correct**, carried from 07-16. Brancazio
  DOI still intentionally omitted.

Inline ↔ References cross-check run in both directions: no orphans either way.

⚠️ **Method warning worth carrying forward.** A WebFetch extraction prompt against
PMC7116763 asserted "The text contains **no** discussion of bacteria, prokaryotes, or
unicellular organisms." That is **false** — raw grep of the same document finds both.
This is a fresh instance of
`webfetch-confirmation-prompts-ratify-the-phrase-you-ask-about` in its *absence*
direction: the summariser will confidently manufacture a negative. Every absence claim
in C3 above rests on raw grep of the retrieved full text, not on a fetch summary.

## Verification Performed

- Publisher-of-record checks: eLife 27455 author/affiliation block (WebFetch);
  Sourjik & Berg 2002 and He et al. 2016 resolved at Crossref; He 2016 abstract via
  EuropePMC. ScienceDirect and PNAS both 403 to WebFetch — Crossref/EuropePMC used
  instead, per `webfetch-survives-websearch-exhaustion`.
- All three P-CS5 fragments quoted in the article grep-verified verbatim against
  [positions/consciousness-scope.md](/positions/consciousness-scope/) (count 1 each).
- Both interface-threshold claims paraphrased grep-verified against the concept page.
- Wikilink targets: all resolve. Editor-vocabulary scan: clean. LLM-cliché scan
  ("not X. It is Y.", "load-bearing"): clean.
- `scripts/sync.py` run; Hugo body carries both fixes, zero `[[ ]]` residue in body,
  all 8 body links resolve including `/positions/consciousness-scope/` and
  `/concepts/interface-threshold/`. Frontmatter validates.

## Remaining Items

- The **apex source-list omission** noted above — a question for `apex-evolve`, not
  this article.
- The sibling chemotaxis article and the apex **also** fail to cite P-CS5; the
  register→article linkage is one-directional cluster-wide, not just here. Worth a
  `positions-evolve` or cross-link pass if it recurs.

## Stability Notes (carried forward, do not re-flag)

- Physicalist / eliminative-materialist rejection of the dualist framing is a
  **bedrock framework-boundary disagreement**, not a fixable defect. (Carried from
  both prior reviews.)
- The in-principle-intractability thesis is a deliberately hedged **wager**, now
  additionally anchored to P-CS5's moderate credence. Do not flag as unsupported.
- The Brancazio DOI is intentionally omitted (unconfirmed at publisher). Do not
  "restore" it. (Carried from 07-16.)
- **New**: the Sourjik detail is now correct and was wrong for three reviews in its
  previous form. Do not "restore" the punchier "runs the Max Planck lab" phrasing —
  it is false. Sourjik developed the FRET technique; Shimizu/Emonet made the
  measurement.
- **New**: do not re-import "below the interface threshold" as a synonym for "no
  interface at all". The construct is substrate-neutral and compatible with phenomenal
  presence below it; the minimality argument belongs to Tenet 2.
- **New**: the FEP objection is **triviality / over-generality**, not
  unfalsifiability, and Colombo & Palacios 2021 is the source that supports it. Do not
  "restore" the falsifiability wording, and do **not** cite Andrews 2021 as a critic
  making it — she rejects that critique as a category error. Sánchez-Cañizares 2021
  (*Entropy* 23(2):238) is not by Andrews and largely defends the FEP.
- **New**: the two Lyon papers are distinct and both are now cited — Lyon 2015
  (*Front. Microbiol.* 6:264, bacterial habituation/sensitisation) and Lyon 2020
  (*Adaptive Behavior*, minimal-cognition usages). Do not collapse them.
- **New**: Birch, Ginsburg & Jablonka 2020 supports the "positive marker only" reading
  and **nothing about bacteria**. Do not re-anchor bacterial-learning claims to it;
  Ginsburg & Jablonka 2021 and Lyon 2015 are the correct anchors.
- **Methodological**: this article's two clean reviews preceded two criticals. The
  entry hypothesis (dependency drift) was wrong and the defects were original —
  evidence that "converged" articles need an *original-defect* lens, not only a
  what-moved-underneath lens.