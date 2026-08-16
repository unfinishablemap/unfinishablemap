---
title: "Deep Review - The Agency Budget"
created: 2026-08-16
modified: 2026-08-16
human_modified:
ai_modified: 2026-08-16T20:02:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-16
last_curated:
---

**Date**: 2026-08-16
**Article**: [[concepts/agency-budget|The Agency Budget]]
**Previous review**: Never (created 2026-08-16 10:44 UTC; first review)

## Publisher-of-Record Citation Ledger

Every inline attribution was checked separately from its reference entry, and every
reference entry was checked for an inline home. Full texts were pulled where a quote
sat outside the abstract.

- **Schroeder de Witt, Sokota, Kolter, Foerster & Strohmeier 2023** (*Perfectly Secure
  Steganography Using Minimum Entropy Coupling*, ICLR 2023, arXiv:2210.14889) —
  **real-correct**. The article presents Theorem 1 and Theorem 2 as verbatim quotations,
  which is the highest-risk construction in the file, so both were checked against the
  v3 PDF rather than the abstract. Theorem 1 matches word for word. Theorem 2 matches
  word for word *including* the notation `f : X ⇝ C` and the semicolon in `I(M ; S)` —
  the abstract paraphrases both theorems in different words ("maximizes information
  throughput"), so an abstract-only check would have produced a false fabrication flag
  here. The Cachin ε-security definition and the gloss "Perfect security is a very
  strong notion of security, as it renders detection by statistical or human analysis
  impossible" are also verbatim. The ciphertext/private-key disanalogy the article
  flags at §The Coupling Result is accurate to the paper's protocol description.
- **Cachin 1998** (*An Information-Theoretic Model for Steganography*, in Aucsmith ed.,
  *Information Hiding*, 306–318, Springer) — **real-correct**; cited via the 2023 paper,
  which the article states openly. Given name "Christian" correct.
- **Kastner 2016** (*The Born Rule and Free Will*, in *Probing the Meaning of Quantum
  Mechanics*, World Scientific, 231–243, DOI 10.1142/9789813146280_0009) —
  **real-correct**; Crossref confirms author, title, container, publisher, year and page
  range. The article attributes nothing finer than the subtitle's thesis and says so
  explicitly, which correctly honours the source note's unretrieved-full-text gap.
- **Kovačević, Stanojević & Šenk 2015** (*On the entropy of couplings*, *Information and
  Computation* 242, 369–382) — **real-correct metadata, but orphaned**. Crossref confirms
  all three given names, journal, volume, year and pages. The entry had **zero inline
  presence** anywhere in the body. Fixed — see Critical Issues.
- **Landsman 2021** (*Indeterminism and Undecidability*, arXiv:2003.03554) —
  **real-correct**. Both quoted spans ("can be proved from Chaitin's follow-up to
  Goedel's (first) incompleteness theorem"; "a property called 1-randomness in logic,
  which is much stronger than uncomputability") are verbatim in the abstract. The
  article's declaration that Landsman's target is determinism and that the agency
  extension is the Map's own inference matches the source and the research note's flag.
- **Valentini 2002** (*Signal-Locality and Subquantum Information in Deterministic
  Hidden-Variables Theories*, in Placek & Butterfield eds., *Non-Locality and Modality*,
  81–103, Kluwer; arXiv:quant-ph/0112151) — **real-correct**. The quoted span "must
  predict the existence of instantaneous signals at the statistical level for
  hypothetical 'nonequilibrium ensembles'" is verbatim, and the article preserves the
  scope condition (deterministic hidden-variables theories only) that the abstract
  states — a qualifier that is easy to drop and was not dropped. Given name "Antony"
  correct, not "Anthony". The book title and page range match the arXiv published-as line.
- **Aaronson 2013** (*The Ghost in the Quantum Turing Machine*, arXiv:1306.0159) —
  **real-correct**, three spans checked. "a certain kind of in-principle physical
  unpredictability that goes beyond probabilistic unpredictability" and "tries to find
  scope for 'freedom' in the universe's boundary conditions rather than in the dynamical
  laws" are verbatim in the abstract, and the article's parenthetical claim that
  "examines" is the abstract's own verb is itself correct. The two body quotes sit
  outside the abstract and were verified in the full text: "A freebit is simply a qubit
  for which the most complete physical description possible involves Knightian
  uncertainty" and "they get permanently 'used up' whenever they are amplified to
  macroscopic scale". The finite-supply inference is faithful to the paper's holographic
  argument. One authorial-stance omission — see Medium Issues.
- **Southgate & Oquatre-sept / Oquatre-huit** (Map self-cites) — **real-correct** by Map
  convention; both are cited inline as wikilinks in the body.

**Superlative currency sweep**: one hit, "so far", and it falls inside a quotation of the
2026-08-13 review's charge rather than asserting an empirical record. No currency drift.

**Internal quote channel**: the two quotations from the 2026-08-13 ChatGPT outer review
("only a verbal conjunction of two desiderata"; "without achieving compatibility merely
by defining all observable consequences away") were re-grepped against the current
review file and match at lines 102 and 107. The deep-link
`positions/quantum-interface#^mechanism-debt` resolves to a live anchor. The article's
four-item characterisation of what a coupling would and would not deliver against the
toy-model desiderata was checked against `apex/born-preserving-causal-efficacy` lines
137–151 and is accurate on each item.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Orphan reference entry 4, compounded by an unattributed notion**: Kovačević,
  Stanojević & Šenk (2015) sat in the References with no inline citation anywhere, while
  the body used the term "minimum entropy coupling" repeatedly without ever sourcing the
  notion — leaving the impression that it is the 2023 paper's construct. It is not: the
  2023 paper itself credits it to Kovačević et al. 2015 ("minimal entropy couplings
  (MECs) (Kovačević et al., 2015)"). **Resolution applied**: a short passage in §The
  Coupling Result now attributes the notion to its originators and records the paper's
  NP-hardness result, which turned out to be load-bearing for the article's own
  argument rather than decorative. The article proposes a worked minimum-entropy
  coupling as a candidate for the P-Q10 toy model; that proposal now carries the
  qualification that the ceiling is set by an optimum nobody can compute efficiently,
  together with the countervailing fact — verified in the 2023 paper — that the standard
  fast approximations retain *exact* marginalisation and lose at most one bit of joint
  entropy. The conservation law therefore survives approximation even though maximal
  throughput does not, which costs the budget throughput rather than security.

### Medium Issues Found

- **Aaronson recruited slightly past his own verdict**: the article's "examines — the
  abstract's own verb" hedge is careful and correct about the *viewpoint's* provenance,
  but the paragraph closed by declaring the freebit allowance "defensible" without
  recording that Aaronson's abstract calls the resulting perspective one "of which I
  myself remain skeptical". The source research note had explicitly instructed that he
  be cited as offering a speculative possibility-proof; that instruction was half
  carried. **Resolution applied**: one clause added carrying his own verdict verbatim.
- **Notational collision on `C`**: the article's conservation law defines `C` as ranging
  over conscious states, while the quoted Cachin definition and the quoted Theorem 2 use
  `C` for the *covertext* — which under the article's own mapping is the Born side, the
  opposite side of the correspondence. The quotations cannot be altered, so the fix goes
  on the Map's side. **Resolution applied**: a one-sentence warning immediately after the
  quoted definition. The `C`-for-conscious-states notation is left intact, since it is
  shared with the source research note and the 2026-08-16 optimistic review and changing
  it here would fracture a small family.

### Counterarguments Considered

- **The zero-budget objection** (a channel whose only competent decoder already holds the
  mental facts is not obviously a mental-to-physical channel): the article states this
  as the sharpest rival and explicitly declines to claim an answer. No change needed —
  the concession is already at the right strength.
- **"Compatibility bought by defining the observable consequences away"**: the article
  quotes this charge against itself and concedes it is "uncomfortably close". Its reply —
  that the nil observable consequence is the corridor's antecedent constraint rather than
  an artefact of the construction — is honest and non-circular as stated.
- **Calibration check (§2 diagnostic test)**: the article never upgrades evidential status
  on tenet-coherence. It labels its own result "framework-internal coherence arithmetic
  and never as established mental causation", routes the reader to the mechanism-debt
  citation grade, and states plainly that the budget "does not convert either into a
  demonstration of efficacy". A tenet-accepting reviewer would not flag any claim here as
  overstated. No possibility/probability slippage.

### Reasoning-Mode Classification (§2.6)

No named opponent is refuted inside their own framework, so no boundary-substitution risk
arises. Engagement with the zero-budget reading: **Mode Three** — the disagreement is
declared open and unanswered rather than dressed as a reply. Engagement with Valentini:
**Mode Three**, read adversarially with its scope condition preserved. No editor-vocabulary
label leakage found in the prose.

## Optimistic Analysis Summary

### Strengths Preserved

- The two-qualification lead is unusually disciplined: it front-loads the result and then,
  before any development, states both that the mapping is the Map's own construction and
  that the theorem granting the budget also fixes its price. Untouched.
- The disanalogy paragraph (no third party, no key, so what survives is the mathematics
  and not the picture of a message successfully sent) is the kind of self-limiting move
  that citation reviews usually have to add. It was already there.
- Scope conditions on both bookend theorems are stated and defended rather than quietly
  inherited. Untouched.

### Enhancements Made

- Attribution of minimum entropy coupling to its originating paper, with the NP-hardness
  qualification and its exact-marginalisation counterweight.
- Aaronson's own stated skepticism recorded.
- Notational collision on `C` disambiguated.

### Cross-links Added

None. The article already carries six inbound links from live articles and its outbound
set is dense and accurate.

## Remaining Items

- **Reciprocal link to `concepts/sign-problem-for-conscious-observation`** — deliberately
  **not** done here. An open P3 refine-draft task already owns this work and names
  `agency-budget` as its second file; doing it in this pass would have duplicated that
  task's scope and produced a same-file pileup.
- **Opportunity, not a defect**: desideratum 5 in `apex/born-preserving-causal-efficacy`
  carries a rider — a selector "whose own distribution is fixed so as to reproduce the
  Born measure satisfies desideratum (2) trivially while supplying no reason-responsiveness
  at all" — which is the sharpest existing form of this article's own zero-budget rival,
  already written in a sibling. The zero-budget paragraph could connect to it. Not minted
  as a task, given the file's existing queue.

## Stability Notes

- The zero-budget reading's *idleness* horn is a bedrock disagreement, not a fixable flaw.
  The article answers the impossibility form and says explicitly that the idleness form
  stands. Future reviews should not re-flag this as a critical issue; the register is
  correct and the concession is already priced at coherence-only grade.
- The steganographic mapping is classical, and the article says so in its own voice. The
  absence of a quantum treatment is declared open territory rather than concealed, so
  "the theorems are classical" is not a finding against this article.
- Citation apparatus is now fully verified at the publisher of record as of 2026-08-16,
  with the per-cite ledger above. A future review should not re-verify these nine entries
  absent a body or reference change; the higher-yield target on this file is the
  empirical-claim and cross-link surface, not the bibliography.
