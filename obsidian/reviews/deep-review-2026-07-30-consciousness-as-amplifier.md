---
title: "Deep Review - Consciousness as Intelligence Amplifier"
created: 2026-07-30
modified: 2026-07-30
human_modified: null
ai_modified: 2026-07-30T11:21:11+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-07-30
last_curated: null
---

**Date**: 2026-07-30
**Article**: [[consciousness-as-amplifier|Consciousness as Intelligence Amplifier]]
**Previous review**: [[deep-review-2026-07-10-consciousness-as-amplifier|2026-07-10]]

## Review Context

Ninth deep review, and a **deliberately narrowed remit**. The 2026-07-10 pass completed a
full 24-entry publisher-of-record **metadata** ledger (authors / year / venue / volume /
pages / DOI). That ledger is recent, thorough and good, and **metadata verification was
not re-run here**. Re-doing it is the wasted-pass failure mode.

What eight prior reviews had never run as named lenses — confirmed by scanning all eight
review files for headings matching quote / verbatim / claim-match / framing, which returns
nothing — are the three lenses a metadata ledger structurally cannot cover:

1. **Claim-match** — does the cited paper actually *report the finding it is bolted to*?
2. **Quote fidelity** — is each quoted span verbatim at the primary text?
3. **Citation framing** — is a real, correctly-attributed, verbatim, current cite
   nonetheless *mis-framed* as to what it shows or whose interpretation it is?

This file proves the distinction on its own history. The 07-10 ledger certified entry #12,
Inoue & Matsuzawa 2007, as `real-correct` — and the metadata *was* right. Nineteen days
later, commit `7c318cdf3` fixed a **claim** error resting on that very entry: the 2±1
chimpanzee working-memory figure had been attributed to a paper reporting the opposite, and
it had propagated to four files. **A `real-correct` metadata ledger is not evidence about
claims.** This pass swept for siblings of that class and found three, plus one calibration
defect.

Result: **four defects fixed**, all invisible to metadata verification. This is a CONTENT
fix (both stamps bumped).

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

**1. Claim-match / citation-framing — De Neys & Glumicic (2008) co-cited for a finding it
does not report, in the opposite direction. Two loci (§Baseline Cognition Hypothesis;
§The Illusionist Challenge).**

Both loci read that DeWall et al. and De Neys & Glumicic jointly "demonstrate that
cognitive load disrupting conscious attention impairs logical reasoning; disrupting
unconscious processes does not."

Verified against the author's own manuscript of the paper (wdeneys.org, DOI
10.1016/j.cognition.2007.06.002), text extracted and read locally:

- The string **"load" occurs zero times in the entire paper.** There was no cognitive-load
  manipulation and no disruption experiment of any kind. The method was think-aloud
  protocols plus implicit indices (response latency, reviewing tendency, base-rate recall).
- The finding runs the *other* way. From the General discussion: *"even the accuracy-wise
  most ungifted reasoners were detecting the special status of the incongruent problem"*
  and *"the present data clearly suggest that successful conflict detection is omnipresent
  during decision making"*; from the abstract and §3, *"the verbal protocols showed no
  direct evidence for a consciously experienced conflict."*

So the paper establishes a **logic-sensitive monitoring process that operates without
conscious access** — a partial counterweight to the section's thesis, presented as
one-sided support for it. This is the textbook "double-edged result asserted as one-sided
support" tell.

*Corroboration that this is a defect and not a reading preference*: `baseline-cognition.md`
L154 gets it right — it attributes the load/unconscious-disruption dissociation to **DeWall
alone**, and cites **De Neys 2012** (a different paper) for the explicit/implicit contrast.
The corpus contradicted itself, with this file holding the wrong version.

*Resolution* — the dissociation is now attributed to DeWall alone (whose Experiment 1 does
exactly this: verified at PubMed 18226923, *"Substantial decrements in logical reasoning
were found when a cognitive load manipulation preoccupied conscious processing, while
hampering the nonconscious system with consciously suppressed thoughts failed to impair
reasoning"*). De Neys & Glumicic is re-framed for what it actually shows, and this
**strengthens** the argument rather than weakening it: detection is not the bottleneck,
the override is. Added to §The Illusionist Challenge: implicit conflict detection does not
rescue the illusionist, because what fails without conscious engagement is the override,
and the override is where the reasoning happens.

**2. Attribution — "zone of latent solutions" credited to Tomasello alone, with no
reference entry at all (§Baseline Cognition Hypothesis).**

The term was coined by **Tennie, Call & Tomasello (2009)**, *Phil. Trans. R. Soc. B*
364(1528), 2405-2415 (doi 10.1098/rstb.2009.0052). Tomasello is third author, so
sole-credit is imprecise; more seriously, this file cited **no** Tennie et al. entry, so a
quoted term carried a possessive attribution with no citable source behind it. The
References hold Tomasello & Herrmann 2010 and Tomasello, Kruger & Ratner 1993 — neither is
the ZLS paper.

This is a documented corpus pattern already corrected in four siblings
(`consciousness-and-cognitive-distinctiveness` 2026-04-12, `jourdain-hypothesis` 2026-04-06,
`cumulative-culture` 2026-06-03, `working-memory`); this file was an un-migrated tail and
the *worst* case of it, having no reference at all. **Fixed** — re-attributed inline and
the Tennie et al. 2009 reference added.

**3. Inline↔References orphan — Cowan (2001) cited inline, absent from References.**

§Baseline Cognition Hypothesis cites *"nearer 4±1 on Cowan's (2001) revision"*. No Cowan
entry existed. This defect **post-dates the 07-10 ledger**: the inline cite was introduced
by commit `7c318cdf3` on 07-29, which added Read, Manrique & Walker 2022 to the References
but not Cowan. **Fixed** — added `Cowan, N. (2001). The magical number 4 in short-term
memory: A reconsideration of mental storage capacity. Behavioral and Brain Sciences,
24(1), 87-114`, Crossref-confirmed (DOI 10.1017/s0140525x01003922) and matching the
corpus's canonical form used in ten sibling files.

**4. Calibration — correlational study reported as causal, and amplified (§Metacognitive
Monitoring; §The Illusionist Challenge "training problem").**

The article read: *"Meditators with thousands of hours of practice show **dramatically**
better introspective accuracy than novices (Fox et al. 2012), suggesting conscious
attention to conscious states **genuinely improves** metacognitive capacity."*

Verified at PMC3458044. The paper is explicitly *"a preliminary exploration"*, and the
design is **cross-sectional across existing practitioners (1–15,000 hrs), not a training
study** — it cannot separate practice effects from self-selection, so "improves" is a
causal claim the design does not license. The authors' own wording is *"significantly
better"*, not "dramatically", and their conclusion is the deliberately modest *"long-term
meditators provide more accurate introspective reports than novices."* Correlations
r = .33–.48.

The same over-claim recurred at the "training problem" bullet, which asserted contemplative
traditions *"demonstrate that sustained attention to conscious states improves cognitive
performance."*

This is a **calibration error, not a bedrock disagreement**: it passes the diagnostic test,
because a reviewer who fully accepts the Map's tenets would still flag a causal claim
resting on a cross-sectional design. **Fixed** at both loci — "dramatically" → the authors'
"significantly", the causal claim replaced with the tracking claim plus an explicit
self-selection caveat, and the illusionist bullet re-pitched so the correlational status is
stated and the argumentative burden ("the direction illusionism has to explain away") is
carried honestly rather than overstated.

### Full Claim-Match Ledger

Every citation carrying an empirical or interpretive claim, read at the source rather than
the citation string. Format: `Cite — claim as stated — verdict (source read)`.

| Cite | Claim in article | Verdict | Source read |
|---|---|---|---|
| DeWall, Baumeister & Masicampo 2008 | conscious load impairs logical reasoning; unconscious disruption does not | **claim-match CONFIRMED** — Experiment 1 exactly | PubMed 18226923, full abstract |
| De Neys & Glumicic 2008 | co-cited for the same disruption dissociation | **DEFECT — paper has no load manipulation and finds the opposite direction; FIXED** | author manuscript wdeneys.org (COGNIT_1695), full text extracted locally |
| Read, Manrique & Walker 2022 | chimp WM 2±1; reads Ayumu as eidetic/iconic imagery not WM; humans given equivalent training match or exceed | **claim-match CONFIRMED, all three sub-claims** | full text, zaguan.unizar.es 112160 (see quotes below) |
| Inoue & Matsuzawa 2007 | trained juvenile chimp recalled positions of briefly-masked numeral sequences | **claim-match CONFIRMED** — Ayumu, ordinal order of 8 digit locations at 80%, 210 ms | as reported in Read et al. 2022 §11, primary description |
| Miller 1956 | human 7±2 | CONFIRMED (canonical) | — |
| Cowan 2001 | human nearer 4±1 | CONFIRMED; **was missing from References, FIXED** | Crossref 10.1017/s0140525x01003922 |
| Tennie, Call & Tomasello 2009 | "zone of latent solutions" | term CONFIRMED; **was mis-attributed to Tomasello alone with no reference, FIXED** | Royal Society doi 10.1098/rstb.2009.0052 |
| Gruber et al. 2015 | apes have culture but may not know they do | **claim-match CONFIRMED** — the paper's title claim | *Front. Psychol.* 6:91 |
| Fox et al. 2012 | meditators "dramatically" better; consciousness "genuinely improves" metacognition | **DEFECT — cross-sectional, correlational, "preliminary"; causal claim unlicensed; FIXED** | PMC3458044, full abstract + effect sizes |
| Suddendorf & Corballis 2007 | Bischof-Köhler: animals cannot act on drive states not currently held | **claim-match CONFIRMED and framing faithful** — abstract: *"no convincing evidence for mental time travel in nonhuman animals"* | PubMed 17963565 |
| James 1890 | consciousness must be causally efficacious to be selected | CONFIRMED (paraphrase, no quote; *Principles* ch. 5 "The Automaton Theory") | canonical |
| Georgiev 2024 | quoted on classical emergence → causally impotent experiences | **quote VERBATIM CONFIRMED at primary source** | PMC10817314, string-matched (see below) |
| Frankish 2016 | quasi-phenomenal states represent themselves as phenomenal without being so | CONFIRMED — standard, faithful gloss of illusionism | *JCS* 23(11-12) |
| Hameroff & Penrose 2014 | microtubule-mediated collapse | CONFIRMED (Orch OR) | *Phys. Life Rev.* 11(1) |
| Stapp 2009 | quantum Zeno stabilisation | CONFIRMED | Springer 3rd ed. |
| Beck & Eccles 1992 | synaptic tunnelling | **claim-match CONFIRMED** — *"a quantum mechanical model for it based on a tunneling process of the trigger mechanism"* of vesicular exocytosis | PMC50549 |
| Saad 2025 | consciousness takes over causal work by preemption, not duplication | **claim-match CONFIRMED** — *"E's causal profile preempts the corresponding subset of P's default causal profile"*; *"experiences uphold causal responsibilities 'delegated' to them by physical states"* | PMC12062107, abstract + passages |

### Quote-Fidelity Ledger

The verbatim surface is small — one source quote of ≥30 characters, plus short quoted terms.

- **Georgiev 2024**, §The Evolutionary Argument — *"Any endeavor to construct a physical
  theory of consciousness based on emergence within the framework of classical physics,
  however, leads to causally impotent conscious experiences in direct contradiction to
  evolutionary theory."* — **VERBATIM CONFIRMED** by string-match against the primary text
  at PMC10817314 (not against the prior review; the 07-10 ledger's assertion was
  independently re-verified at source per the aggregator-ratification hazard). Includes the
  easily-dropped *"however,"*.
- **"zone of latent solutions"** — verbatim established term; coinage re-attributed (above).
- *"tasks that feel conscious"* / *"tasks that distinguish humans from great apes"* — the
  Map's own scare-quoted phrases, not source quotes. Correctly not presented as citations.
- Buddhist-psychology terms (*vijñāna*, *cetasika*, *manasikāra*, *vitakka*/*vicāra*) —
  transliterations, not quoted spans; unchanged.

### Citation-Framing Review

The driver flagged the quantum-interface and illusionist cites as the highest
framing-pressure loci. Checked individually:

- **Beck & Eccles, Hameroff & Penrose, Stapp** — all three appear in §Proposed Physical
  Mechanisms under the framing *"If consciousness acts at the quantum level"*, as
  *"proposed"* mechanisms, closing with *"No complete chain from quantum to macroscopic has
  been experimentally validated."* Framing is honest and framework-relative; the Map's own
  voice is not made to say these papers *show* anything. **No change.**
- **Hagan et al. 2002 and Tegmark 2000** sit in References without inline cites, behind
  §The Decoherence Challenge. They are the two sides of the decoherence dispute (Tegmark
  posing it, Hagan et al. rebutting), and the section delegates to `[[decoherence]]` rather
  than adjudicating. Apparatus-style rather than defective; eight prior reviews left it.
  **Noted, not changed** — see Remaining Items.
- **Frankish** — the objection is stated in Frankish's own terms before being answered, not
  strawmanned. **No change.**
- **Suddendorf & Corballis** — the Bischof-Köhler hypothesis is contested by post-2007
  corvid caching work, but S&C's own stance is squarely human-uniqueness
  (*"no convincing evidence for mental time travel in nonhuman animals"*), and the article
  hedges with *"suggests"*. The citation is faithful to its source. **No change**; noted
  below as a locus considered.

### Metadata ambiguity resolved (carried over from the June ledger)

The June review recorded De Neys & Glumicic's page range as *"ambiguous across databases
(some list 1248-1299, others 1284-1299). Not load-bearing; left as-is."* Settled here via
the **Crossref API** for DOI 10.1016/j.cognition.2007.06.002: *Cognition* **106(3),
1248-1299**. The article's existing value was **correct**; the 1284-1299 variant
(propagated by SciRP) is the erroneous one. No change needed — recorded so no future pass
re-opens it.

### Argument-lens (evidential calibration)

One calibration defect found and fixed (Fox et al., above). Otherwise the framing remains
consistently framework-relative — *"The Unfinishable Map proposes…"*, *"may reflect"*,
*"proposed"*, the amplification-void concession, and the Minimal Quantum Interaction
section's *"compatible with but doesn't require"*. No possibility/probability slippage
elsewhere. Consistent with the June and July findings.

### Reasoning-Mode Classification (editor-internal)

- **Frankish (illusionism)**: Mixed — Mode One (the DeWall disruption asymmetry, internal
  to the cognitive science Frankish accepts) + Mode Two (regress problem: illusionism helps
  itself to phenomenal vocabulary without earning it). The De Neys re-framing *deepens* the
  Mode One engagement by conceding the implicit-detection result and locating the
  disagreement precisely at the override. Honest.
- **Epiphenomenalist**: Mode One — the evolutionary argument engages on selection grounds
  the epiphenomenalist accepts.
- **MWI defenders / eliminative materialists**: Mode Three / bedrock — conditional framing,
  honest.

No label leakage: body scanned for `Mode One/Two/Three`, `direct-refutation-feasible`,
`unsupported-jump`, `bedrock-perimeter`, `Engagement classification:`, bold
`**Evidential status:**` — none present.

## Optimistic Analysis Summary

### Strengths Preserved

Front-loaded thesis; the systematic human-ape-gap correspondence; the Three Senses
disambiguation; five explicit falsifiability conditions; full five-tenet alignment; the
decoherence-section decoupling (the core argument is explicitly independent of which
physical pathway proves correct); Buddhist-psychology integration; comprehensive Further
Reading. All wikilinks validate.

The **Hardline Empiricist** persona is the one that earned its keep this pass: the Fox et
al. locus is exactly the pattern that persona exists to catch — praise-worthy evidential
restraint elsewhere in the article made the single unrestrained passage stand out.

### Enhancements Made

The De Neys correction is a net argumentative *gain*, not merely a subtraction. Conceding
that conflict detection runs implicitly and relocating the claim to the override is a
stronger position than the one the article held, and it is now the position the evidence
actually supports.

### Cross-links Added

None. Integration is sufficient; all existing links validate.

## Length Management

Reported separately, because the aggregate figure is a measurement artifact of a
citation-dense article:

| | Before | After | Δ |
|---|---|---|---|
| Authored prose | 2090 w | 2217 w | +127 |
| Reference apparatus | 635 w | 687 w | +52 |
| `analyze_length` total | 2725 w | 2902 w | +177 |

`analyze_length` reports `soft_warning` both before and after, but **authored prose remains
comfortably under the 2500 concepts soft threshold** (89% of it). Hard cap 3500 leaves
~600 w of headroom. No condensation applied, and none manufactured: the prose growth is
entirely corrective — replacing a false one-line claim with the true finding costs words,
because the true finding is more nuanced than the false one. Apparatus growth is the two
added references (Cowan, Tennie et al.).

## Remaining Items

- **Propagation residue from `7c318cdf3`: swept, one open locus.** The four-file
  propagation is clean in this file (the L67 passage claim-matches perfectly at primary
  source). Corpus-wide, no file still attributes the 2±1 figure to Inoue & Matsuzawa.
  `concepts/metacognition.md` L144 carries *"working memory of roughly 2±1 items"* with **no
  citation** — a bare-figure gap rather than a misattribution, and the install would be
  Read, Manrique & Walker 2022. Not re-scoped into this single-file task; worth a separate
  mint. (`topics/language-recursion-and-consciousness.md` L59 was already reported in the
  07-29 changelog for the same treatment.)
- **ZLS attribution tails.** `topics/consciousness-in-simple-organisms.md` L129
  (*"what Tomasello calls"*) and `concepts/baseline-cognition.md` L82
  (*"Tomasello (2010) characterises"*) still use sole-Tomasello credit. baseline-cognition
  is the milder case — the 2026-07-10 review of that file consciously left it, since Tennie
  et al. 2009 *is* in its References as #16. simple-organisms is the same shape as the
  defect fixed here. Separate mint.
- **Hagan et al. 2002 / Tegmark 2000** are References-only with no inline cite. Defensible
  as apparatus for the delegated decoherence discussion; flagged for a future pass to
  either cite inline in §The Decoherence Challenge or drop.

## Stability Notes

Ninth review, and the second consecutive pass to find real defects in a file repeatedly
called converged — but this time in a **different defect class** from the last one. The
07-10 pass extended metadata verification to all 24 cites and found two errors. This pass
did not touch metadata and found four more, in claim-match, attribution, apparatus
completeness, and calibration.

The lesson to carry forward: **"metadata-verified" and "claim-verified" are orthogonal
axes, and this file demonstrates it twice** — once in `7c318cdf3` (a `real-correct` ledger
entry supporting an inverted claim) and once here (De Neys & Glumicic, `real-correct`
metadata, finding in the opposite direction from the one it is cited for). A ledger
recording only author/year/venue/pages provides **no** evidence about whether the paper
reports what the sentence says it reports. Future passes should treat a complete metadata
ledger as licence to *skip* metadata, not as licence to skip verification.

**Do NOT re-flag** (bedrock, carried forward): eliminative-materialist redefinition of
"consciousness"; MWI rejection of indexical selection; Dennett-style doubt about phenomenal
consciousness as target (handled by Three Senses); the exclusion problem (addressed via
causal delegation).

**Do NOT re-open** (verified, with the check recorded): the 24-entry metadata ledger
(07-10); De Neys & Glumicic page range 1248-1299 (Crossref, settled above); the Georgiev
quote (verbatim at PMC10817314, verified twice independently); the Read et al. 2022 /
Ayumu passage (claim-matched against the full text); Beck & Eccles synaptic tunnelling;
Saad's preemption-of-default-causal-profile.

**Convergence assessment**: the argument is stable and has been since ~2026-03. Three
independent verification lenses have now been run to completion on it — metadata (07-10),
and claim-match / quote-fidelity / framing (this pass). The unchecked surface on this
article is now genuinely small, and the residual risk has moved decisively to the
corpus-propagation tails listed under Remaining Items rather than to this file.
