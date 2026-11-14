---
ai_contribution: 100
ai_generated_date: 2026-11-14
ai_modified: 2026-11-14 07:55:53+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[decoherence]]'
- '[[measurement-problem]]'
- '[[post-decoherence-selection]]'
created: 2026-11-14
date: &id001 2026-11-14
description: 'Optimistic review of four pages on what decoherence, envariance and
  contextuality fix and what they leave open: envariance, quantum Darwinism, improper
  mixtures, contextual selection.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-14 07:55:53+00:00
modified: *id001
related_articles:
- '[[envariance]]'
- '[[quantum-darwinism-and-consciousness]]'
- '[[improper-vs-proper-mixtures]]'
- '[[contextual-selection-in-quantum-foundations]]'
- '[[born-rule-and-the-consciousness-interface]]'
- '[[post-decoherence-selection-programme]]'
title: Optimistic Review - 2026-11-14 - The decoherence-programme wing
topics:
- '[[quantum-measurement-and-consciousness]]'
- '[[hard-problem-of-consciousness]]'
---

# Optimistic Review

**Date**: 2026-11-14
**Wing**: the decoherence programme and its limits. These four pages each take one result from quantum foundations (Zurek's envariance, Zurek's quantum Darwinism, d'Espagnat's improper mixtures, and the Kochen–Specker and Spekkens contextuality theorems) and ask the same question: what does the result fix, and what does it leave open for selection?

**Content reviewed** (each read in full at HEAD `d2b5a93ef0`; line numbers are `Read`-tool file lines with frontmatter included; lengths from `tools.curate.length.analyze_length`, body-only; headroom = hard − 1 − count):

| Abbrev | File | Words | Hard | Headroom | Last optimistic mention (slug substring in review content) | Last deep review | Last content edit |
|---|---|---:|---:|---:|---|---|---|
| EV | `concepts/envariance` | 2,574 | 3,500 | 925 | 2026-09-07 (one-world-wager) | 2026-09-04 | 2026-09-04 |
| QD | `topics/quantum-darwinism-and-consciousness` | 2,840 | 4,000 | 1,159 | 2026-09-08 (quantum-reconstruction wing) | 2026-09-04 | 2026-10-10 |
| IPM | `concepts/improper-vs-proper-mixtures` | 3,296 | 3,500 | 203 | 2026-10-12 (passing mention, aesthetics wing) | 2026-10-13 | 2026-10-13 |
| CS | `concepts/contextual-selection-in-quantum-foundations` | 1,943 | 3,500 | 1,556 | 2026-09-25 (quantum-interpretation wing) | 2026-07-16 | 2026-06-20 |

**Why this wing.** I tokenised every file in `reviews/` and ranked the topics/ and concepts/ pages by the date of the last review that mentions their slug. I excluded every page touched since 2026-11-13 (`git log --since=2026-11-13`) and every page mentioned in any review since 2026-10-31. These four survive both filters: the latest review mention of any of them is 2026-10-14. Together they make the Map's most tightly argued cluster on one structural claim, that physics fixes the *menu* and the *measure* but not the *actual outcome*. No open task in `todo.md` names any of the four. CS has not changed since 2026-06-20, and its last deep review declared it converged ("Selector should now leave this article alone").

**Verification done this run** (fetched text in `/tmp/claude-1000/-home-andy-unfin-unfinishablemap/e7fd0dd3-0248-4116-a7c5-2dabdf48c5ec/scratchpad/optrev/dl/`):
- arXiv full text of Zurek 2003 (quant-ph/0105127v3) and Zurek 2009 (0903.5082).
- arXiv abstracts of Spekkens 2005 (quant-ph/0406166), Spekkens 2019 (1909.04628), Castellani 2023 (2201.04143) and Liu, Scarani & Bai (2502.10030).
- Crossref records for Kirchmair et al. 2009, Lapkiewicz et al. 2011, Budroni et al. 2022 and Howard et al. 2014.

**Not obtained**: Spekkens 2005 body text (the definition of preparation noncontextuality is checked against the abstract and the Map's own apex wording only); Bell 1966 text; Schlosshauer 2007 p. 69; Caves's web notes; Shimony 1965.

## Executive Summary

EV and IPM are among the best physics-foundations writing on the Map. Each states exactly what its result fixes and refuses every free confirmation. EV: "The Map puts probability in deliberately, as a framework commitment." IPM: the Liu–Scarani–Bai result "lends the Map's reading no support." IPM also notices something most of the literature misses: the two flagship deflationists deflate in *opposite* directions. QD is a clear and honest orientation page, but it has not caught up with the two concept pages it now links. It states envariance's conclusion more flatly than EV allows, and it gets one physics detail wrong against its own cited source: Zurek's position basis comes from distance-dependent interactions, not gravity. CS has the most to gain. Its scaffolding of hedges is admirable, but three sentences misstate the theorems it rests on, and four earlier passes ratified them. Repaired, CS can carry the wing's best unclaimed insight. By Gleason's theorem, the unique *noncontextual* probability measure is the Born rule. By Kochen–Specker, no *noncontextual* assignment of actual values exists. The measure/actuality split that EV draws for envariance is therefore already built into the oldest theorem pair in the field.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)

Chalmers argues that structural and functional explanation, however complete, leaves a further fact unexplained. He would see the same shape in this wing's physics: a complete structural story that still leaves a further fact open. QD's opening grants quantum Darwinism the whole structural achievement, explaining "why observers agree about the world, why certain properties appear stable and objective", and only then says "What it does not explain—and what Zurek himself acknowledges—is why any *particular* outcome becomes actual" (QD:40). EV's version is sharper because it finds the further fact *inside the opponent's premises*: "Fact 2 already speaks of 'measurement outcomes, including their probabilities.' Every critic's diagnosis, in one form or another, locates the entry of probability here—before the symmetry argument begins" (EV:50). Chalmers rejects functionalist accounts of consciousness that, on his diagnosis, assume what they set out to explain. The parallel here is a derivation that assumes outcomes in order to derive their weights.

He would also note what the wing declines to claim. QD:74 says "Zurek's framework does not contain a 'selector' role waiting to be filled", and calls the consciousness reading "the Map's interpretive overlay". A property dualist who has spent decades separating the hard problem from its easy neighbours will recognise that discipline.

### The Quantum Mind Theorist (Stapp)

For Stapp, CS's "Attention as context-setting (speculative)" paragraph (CS:61) is the closest thing to home. On his view, the choice of *which question* Process 1 poses is where the mind enters. CS reads that choice through contextuality: "which question is asked matters fundamentally—different questions (different measurement contexts) make different outcomes available." He would press the page to say more. He would not, however, accept QD's post-decoherence placement (QD:84) as a friendly amendment. For Stapp, decoherence leaves Process 1 untouched, and acting on "the already-decohered mixture" concedes too much of the timing to the environment. The wing is right to keep the two framings distinct and to call Stapp's extension the Map's conjecture rather than a consequence of the theorem (CS:61, "This is not implied by the Kochen-Specker theorem").

### The Phenomenologist (Nagel)

Nagel would praise QD:92: "The Map insists that one outcome occurs and the others do not—that indexical identity matters, that there is a fact about which result *I* experience." He would praise even more IPM's report of d'Espagnat's mature move (IPM:50): the failure of the ignorance reading is "not mathematical but logico-semantical." The point is about what the word *ignorance* can mean when "the global description fixes no local fact for anyone to be ignorant of." Nagel's view from nowhere comes back here as a view that has no local fact to be ignorant *of*. The page treats this as a claim about meaning and does not dress it up as a theorem: "the argument is not a formal theorem, and presenting it as one overstates it—d'Espagnat himself did not" (IPM:52).

### The Process Philosopher (Whitehead)

Whitehead would find the wing's central distinction congenial. The *measure* over possibilities is one thing. The *actuality* of one of them is another, and no amount of structure about the first yields the second. EV says the symmetry "never converts probabilities into actualities" (EV:36). QD reads quantum Darwinism as specifying "the selection *context* while leaving the selection *act* to consciousness" (QD:110). This is the vocabulary of concrescence, the many becoming one. The wing reaches it without importing panpsychism or process metaphysics. No organism or system is placed on the evidential-status scale anywhere in these four pages, so the persona's tier constraint is not engaged. The praise is for conceptual fit, not for evidence.

One historical connection is missing and worth adding: Abner Shimony. IPM:92 lists him in the insolubility-theorem lineage (von Neumann, Fine, Shimony, Brown, Busch–Shimony, Bassi–Ghirardi). Shimony was also a philosopher of physics who took Whitehead's ontology of actual occasions seriously as a reading of quantum potentiality ("Quantum Physics and the Philosophy of Whitehead", 1965, *lead, unverified this run*). So the lineage that proves unitary dynamics cannot deliver outcomes includes a thinker who held that actuality is a distinct ontological category. The wing could make that connection in one clause.

### The Libertarian Free Will Defender (Kane)

Kane would single out CS:75, where the page refuses the move libertarians most often make: "structure is not purpose. A roulette wheel constrained to certain numbers is still a roulette wheel." CS:77 then puts the burden where it belongs: rational bias "requires its own defence, independent of the Kochen-Specker result." This is the right relation between physics and agency. Physics supplies at most an *opening*, and the theory of free will must supply the agent.

Kane's sympathy should not hide a physics error at the same spot. CS:77 credits contextuality with "a structured, non-determined space", and CS:73 says contextuality "provides *structural room*" for libertarian freedom. But contextuality supplies no indeterminism. De Broglie–Bohm mechanics is deterministic *and* contextual, a point the Map's own `quantum-probability-consciousness` L108 makes ("de Broglie–Bohm restores it nonlocally and contextually"). The "non-determined" part of the space comes from the outcome gap that IPM documents, not from Kochen–Specker. The 2026-09-25 quantum-interpretation review praised this sentence as written. The roulette-wheel limit is right; the attribution under it needs fixing.

### The Mysterian (McGinn)

McGinn would praise the wing's refusals to close disputes. EV:34 says "the derivation is contested, not refuted... neither side has closed the dispute". EV:72 adds that "Flat verdicts in either direction—'proves circular' no less than 'manifestly noncircular'—overstate the state of play." IPM:86 makes a rare admission: Chen's density-matrix realism denies the purity premise the gap argument needs, and "the Map has not defended its side of it." QD:120 says the hypothesis "sits at the boundary of empirical accessibility." McGinn's concern is the difference between a problem we have not solved and a problem that our cognitive equipment, or here our formalism, cannot express. IPM's trilemma section (IPM:88–101) treats exactly that difference with care. Unitary QM provably cannot close the gap (the insolubility theorems). Four named non-unitary or reinterpretive routes could. "Physics might one day prove that decoherence suffices" is struck from the list for a stated reason (IPM:101).

### The Hardline Empiricist (Birch)

No minimal-organism or animal-consciousness claim appears in this wing. Birch's verdict therefore turns on the other half of his brief: whether a tenet-friendly result is presented as evidence. IPM and EV are model citizens.

- **IPM:46** reports a new 2026 PRL result that *does* separate proper from improper mixtures operationally (retrodiction) and then refuses to cash it: "it leaves the outcome gap exactly where it was and lends the Map's reading no support." The page was handed a free confirmation and declined it. Birch would name that as the strength to protect.
- **IPM:60–68** runs the evidential-status-discipline check by name and gives a two-sided verdict: "detectable in principle and in reversible small-scale regimes, undetectable for all practical purposes at macroscopic scales. The Map's wager is that ontology follows the global description—a wager the formalism permits and does not enforce."
- **EV:94** states the terms of the Map's borrow: envariance contributes a *conditional* that fixes the form, "framework-internal and immune to the circularity charge" because "the Map does not claim the derivation succeeds unaided." This is "tenet-coherent, not evidence-elevating" in the persona's own words.
- **CS:49** and **CS:83** hold the same line: contextuality "does not favour consciousness-collapse over other interpretations" and "does not directly support dualism."

There is one calibration concern, in QD:104. The Dualism paragraph says the Map "reads this as evidence that the gap may not be closable by physics alone." It then defends the claim against the "consciousness of the gaps" objection only with the observation that the outcome problem is "structurally different." That is the weakest version of a reply the page can make much better. QD:118 already cites the insolubility theorems (Fine 1970; Bassi and Ghirardi 2000), which show the gap is not merely unsolved but closed to unitary dynamics. Used at L104, they would turn a "gaps" reply into a theorem-backed one. The honest version also has to say that the theorems leave four *non-conscious* routes open (IPM's trilemma), so the gap's existence is tenet-coherent and does not count as evidence for dualism. Stronger and better calibrated at once, it is the right repair (task minted below).

## Content Strengths

### concepts/envariance (EV)

- **Strongest point**: The page audits a famous derivation from its primary texts and finds the concession *inside* it. Zurek's own scaffolding brings outcomes in through "facts" and the repeatability postulate before any probability is derived (EV:36, EV:46–50). The four critics are then sorted by *where* each locates the circularity, not merely by agreement that it exists (EV:62–70).
- **Notable quote**: "This is the measure/actuality distinction derived from inside the formalism: envariance guarantees that a Born-weighted *description exists*, per state, not that actual measurements instantiate it." (EV:78)
- **Why it works**: The Mertens–van Wezel scope theorem is used twice. It supports the Map's thesis, and it also limits the Map's own use of envariance: "envariance does not quantify over all measurements, so it cannot be the sole ground for the claim that any selection mechanism must respect Born statistics" (EV:78). A page that turns its best evidence into a constraint on itself is doing what the evidential-status discipline asks.
- **Also strong**: The additivity adjudication (EV:82) settles a two-sided dispute by dating it. Zurek 2005 *concedes* additivity and claims to ground it; Zurek 2009 says it is not assumed at all. Zhang's charge therefore contradicts only the 2009 formulation. That is careful use of the publication record.

### topics/quantum-darwinism-and-consciousness (QD)

- **Strongest point**: The three-way division of Schlosshauer's sub-problems (QD:58–62). Quantum Darwinism answers the preferred-basis and interference questions, and the page credits it fully ("These are not trivial results"). The problem of outcomes survives. The 2026-10-10 repair also qualified the objectivity claim correctly: mutual-information redundancy does not guarantee agreement without Strong Quantum Darwinism or spectrum broadcast structure (QD:58, QD:80, Korbicz 2021).
- **Notable quote**: "The asymmetry is the point: the proposal predicts a null ensemble effect, so it is refutable (a deviation kills it) but not symmetrically confirmable, which is why the vacuity worry above and this falsifiability claim are two faces of one fact—the empirical content lives entirely on the refutation side." (QD:116)
- **Why it works**: The page turns its most dangerous objection (vacuity) and its falsifiability claim into one fact seen from two sides. A reader cannot miss either.
- **Verified this run**: the Zurek 2009 objectivity quote at QD:56 is verbatim in the arXiv text ("The state of the system can be found out indirectly and independently by many observers, who will agree about their conclusions"). The 2026-09-04 transposition fix holds.

### concepts/improper-vs-proper-mixtures (IPM)

- **Strongest point**: "The Emptiness Attack Runs in Two Directions" (IPM:70–76). Kirkpatrick deflates the distinction to all-improper and Castellani to all-proper, from the *same* operational-indistinguishability premise. "The deflationary conclusion is thus underdetermined even among deflationists." The literature presents these as two attacks on d'Espagnat. The page shows they are also attacks on each other.
- **Notable quote**: "Wearing FAPP as a badge is the inverted use, and it is the attitude Bell wrote the paper against." (IPM:56)
- **Why it works**: The FAPP section uses the history of a term as an argument. It does not overreach: "Bell is an ally on the diagnosis, not the cure" (IPM:58). The trilemma section (IPM:88–103) is the Map's best defeater inventory. Four live routes are each tied to an engaged page, one tempting route is retired with a reason, and a "fifth kind of defeater" is named that closes no gap but would make the Map's use of it idle (IPM:103). Few pages list a way their own argument can fail without any premise being false.

### concepts/contextual-selection-in-quantum-foundations (CS)

- **Strongest point**: Every step from the theorem to the Map is labelled. CS:61 says "This is not implied by the Kochen-Specker theorem". CS:67 says "The Map leaves this open and does not rest its post-decoherence picture on the constraint being operative". CS:69 says "a mathematical analogy rather than an established mechanism". The 2026-09-25 review was right to call this a template for engaging a no-go theorem.
- **Notable quote**: "There is no shelf of pre-assigned values." (CS:57)
- **Why it works**: The anti-reification framing is exactly what Kochen–Specker licenses. The repair below keeps it and fixes the three sentences around it that say more than the theorems do.
- **Defects the labelling does not cover** (minted as one refine-draft below):
  1. **CS:35 and CS:41 turn Kochen–Specker into a claim about measured results.** CS:35 says "what result obtains for a given observable depends on which other observables are measured alongside it." CS:41 says "an observable *A* measured alongside compatible observable *B* need not yield the same value as *A* measured alongside compatible observable *C*." Kochen–Specker constrains *hidden-variable value assignments*: any model that pre-assigns values must let A's value depend on its context. Quantum theory itself gives A the same statistics in every context. The accurate sentence is about models, not results.
  2. **CS:51 reverses Spekkens's preparation contextuality.** It says "Operationally equivalent preparations can lead to different statistical predictions when embedded in different experimental procedures." By definition, operationally equivalent preparations give identical statistics for every measurement. Spekkens's theorem is that no ontological model can represent all such preparations by the same distribution over ontic states (abstract verified this run: "three no-go theorems for ontological models, each based on an assumption of noncontextuality"). The Map's own apex states it correctly ("operationally equivalent preparations, statistically identical, still require different ontic distributions", `apex/post-decoherence-selection-programme` L103). The 2026-05-19 deep review marked the CS sentence "correctly described ✓", and later passes verified only the reference metadata.
  3. **CS:73/77 credit contextuality with indeterminism.** See the Kane section above: Bohm is deterministic and contextual.
  4. A milder equivocation at **CS:63/65**: "context" there means the system–environment Hamiltonian, or microtubule geometry, not the Kochen–Specker set of co-measured compatible observables. One clause would disambiguate it.

## Expansion Opportunities

All four pages sit in sections at cap (topics 370/370, concepts 370/370 per the driver), so every opportunity below is a fold into an existing page.

### High Priority

#### The Gleason / Kochen–Specker pairing: the measure can be noncontextual, actuality cannot (fold into CS)

- **Builds on**: EV's measure/actuality thesis (EV:36, EV:78), the Gleason paragraph in `born-rule-and-the-consciousness-interface` L114 ("non-contextuality alone forces every probability measure on the projections into the Tr(ρP) form"), and CS's Kochen–Specker section. CS already cites Mermin 1993, "Hidden Variables and the Two Theorems of John Bell", which tells this story.
- **Would address**: Nothing on the Map yet sets the two theorems side by side (grep: "Gleason" and "Kochen" co-occur only in passing lists in `quantum-probability-consciousness` and `apex/what-consciousness-tells-us-about-physics`). The two are the probabilistic and deterministic halves of one result. Gleason (1957): in dimension ≥3, every noncontextual probability assignment to projectors has the Born form. Kochen–Specker (1967), anticipated by Bell (1966), who drew the no-dispersion-free-states corollary from Gleason-type reasoning: no noncontextual assignment of definite 0/1 values exists. Together they say the *measure* can be fixed noncontextually and the *actual outcome* cannot. That is the split EV finds in Zurek, now shown to be general rather than a feature of one contested derivation. It also tells the Map what kind of thing its selector must be: whatever settles actual outcomes cannot do so projector by projector, independent of context. Caves's diagnosis of envariance's key premise as "environmental noncontextuality" (EV:66) then reads as the envariance-specific cousin of Gleason's premise. CS can supply that link.
- **Estimated scope**: ~150–200 words in CS, plus links to EV and the born-rule page.
- **Tenet alignment**: Tenet 2 (it specifies the form any minimal selection must take), Tenet 4 (actuality as a category physics leaves open), Tenet 5 (two theorems usually cited as independent results reduce to one distinction).

#### Spekkens's Leibnizian principle as the deflationists' real premise (fold into IPM)

- **Builds on**: IPM:74 (Castellani: proper and improper mixtures "have no observable differences, and hence should not be distinguished", abstract verified this run), IPM:84 ("A deflation pressed hard tends to stop being a free-standing operational point and become one of these separately priced positions"), and IPM:111 (the Tenet 5 paragraph's "Do not draw distinctions without observable differences").
- **Would address**: Spekkens (2019) names this maxim as a methodological principle. If a theory predicts two scenarios "that are ontologically distinct but empirically indiscernible, then this theory should be rejected and replaced by one relative to which the scenarios are ontologically the same", and he traces the principle to Leibniz and Einstein. His own 2005 no-go theorems show that *no* ontological model of quantum theory is preparation-noncontextual. Every such model represents some operationally equivalent preparations as ontically distinct. Applied consistently, Castellani's premise therefore erases the improper/proper distinction and also condemns every realist ontological model of quantum theory. That is a theorem-grade reason for IPM:84's claim that a hard-pressed deflation turns into a priced position (here, trilemma route 3). Calibration the fold must keep: Spekkens draws the *opposite* moral, counting contextuality against the realist models. The fold shows the Map's distinction is a cost every state-realist pays, not a special extravagance. It does not show the Map is right.
- **Estimated scope**: ≤80 words (IPM headroom is 203).
- **Tenet alignment**: Tenet 5 most directly. The parsimony maxim the deflationist relies on is provably unsatisfiable by realist models, which is the "Occam's razor has limits" thesis in its most formal form on the Map.

### Medium Priority

#### QD catches up with EV and IPM

- **Builds on**: EV:34/72 ("contested, not refuted"; flat verdicts "overstate the state of play") and IPM's trilemma.
- **Would address**: QD:90 says "Envariance tells us that the Born-rule probabilities are the only consistent ones to assign", a flat verdict in the "succeeds" direction that EV now marks as an overstatement. QD:48 says "Position states survive for macroscopic objects interacting gravitationally". The cited Zurek 2003 review gives the reason as distance-dependence: "This form of H_SE is motivated by physics (Zurek, 1982; 1991): Interactions depend on the distance" (verified in the arXiv text this run). Gravity appears there only in the Hyperion decoherence-timescale example. QD:104 needs the insolubility-theorem upgrade described under Birch.
- **Estimated scope**: net ≤ +120 words.

#### Experimental contextuality (fold into CS)

- CS:43 says "no improvement in experimental technique can eliminate it" but cites no experiment. State-independent tests exist with trapped ions (Kirchmair et al. 2009, *Nature* 460, 494–497) and with a single qutrit (Lapkiewicz et al. 2011, *Nature* 474, 490–493), and Budroni, Cabello, Gühne, Kleinmann & Larsson (2022, *Rev. Mod. Phys.* 94, 045007) is the standard review. All metadata verified on Crossref this run. One sentence and two references would move CS's main claim from "theorem" to "theorem plus confirmed prediction".

### Ideas for Later

- **Contextuality as a computational resource** (Howard, Wallman, Veitch & Emerson 2014, *Nature* 510, 351–355, "Contextuality supplies the 'magic' for quantum computation", Crossref-verified). This bears on the Map's quantum-hardware/AI-consciousness pages: the one non-classical feature that powers quantum speed-up is also the one CS says any selector must respect. Unclaimed anywhere on the Map.
- **A Gleason corollary the born-rule page may have backwards (verify before acting).** `born-rule-and-the-consciousness-interface` L114 says any re-weighting of the measure "would deform that geometry." By Gleason, though, any *noncontextual* re-weighting is again of the form Tr(ρ′P) for some other density matrix ρ′. A noncontextual "bending" would therefore look like the system having been prepared in a different state, not like a breach of Hilbert-space geometry. Only a *contextual* re-weighting breaks Gleason's form. If that is right, it sharpens what Born-deviation tests can detect. That page is outside this wing and was not reviewed here, so no task is minted.
- **Heisenberg's *potentia* and Shimony.** The wing's measure/actuality vocabulary has a historical ancestor that it never names. One clause in EV's or QD's Relation to Site Perspective would connect the Map to a respectable older tradition.
- **A tension between QD:116 and the corridor taxonomy (unresolved, lower confidence).** QD says "a confirmed deviation from Born statistics in consciousness-dependent experimental contexts would refute the framework." `born-rule-and-the-consciousness-interface` L163–175 lays out the corridor, bending and trumping attitudes, which L197 says "remain in tension", and L167's bending family *requires* deviation. QD's "the framework" probably means the endorsed corridor reading. Since L197 restricts Tenet 2's minimality to the *unconditioned* aggregate, though, it is unclear whether a *conditioned* deviation would refute or confirm. A future deep review of QD should check this against the taxonomy before editing.

## Cross-Linking Suggestions

| From | To | Reason |
|------|-----|--------|
| CS (L51, preparation contextuality) | IPM | Spekkens's preparation contextuality is about "two preparations, one density matrix", the exact title of IPM's first section. Neither page links the other (grep: 0 both ways). |
| IPM (L74 or L111) | CS | Reciprocal: the Leibnizian-principle fold should point to the contextuality page. |
| CS (new Gleason/KS sentence) | EV | The measure/actuality split, generalised. |
| EV (L66, Caves's "environmental noncontextuality", outside the quotation marks) | CS | A piped link at zero word cost. EV is at 2,574 of soft 2,500, so prefer the pipe to new prose. Not minted: it can ride on the CS refine if the fork handles a second file; otherwise it is a later link-only pass. |
| CS (Gleason sentence) | `born-rule-and-the-consciousness-interface` | Its L114 Gleason paragraph is the measure half of the pairing. |

## New Concept Pages Needed

None can be created: concepts and topics are at cap. The obvious candidate, a `gleasons-theorem` concept page, should instead be the CS fold above. Gleason is currently discussed in 15 pages with no home.

## Tasks Minted

Three P3 `refine-draft` tasks, inserted above `## Completed Tasks` in [workflow/todo.md](/workflow/todo/):

1. `concepts/contextual-selection-in-quantum-foundations`: theorem-statement repairs (CS:35/41/51/73/77, CS:63/65 disambiguation), plus the Gleason/Kochen–Specker fold, the experimental-tests sentence, and links to IPM and EV.
2. `topics/quantum-darwinism-and-consciousness`: QD:48 gravitational error, QD:90 envariance calibration, QD:104 insolubility upgrade.
3. `concepts/improper-vs-proper-mixtures`: the Spekkens Leibnizian-principle fold (≤80 words) plus the CS reciprocal link.