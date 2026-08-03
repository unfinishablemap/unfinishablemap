---
title: "Deep Review - Type-Identity Theory"
created: 2026-08-03
modified: 2026-08-03
human_modified: null
ai_modified: 2026-08-03T05:01:03+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-03
last_curated: null
---

**Date**: 2026-08-03
**Article**: [[type-identity-theory|Type-Identity Theory]]
**Previous review**: [[deep-review-2026-07-19-type-identity-theory|2026-07-19]]

## Scope note

The only delta since the 2026-07-19 review was **frontmatter-only**: the empty-`topics` remediation (afaef915c, 2026-08-02) filled `topics: []` with three bare slugs, and that bump re-qualified the article for selection. Body text was byte-identical. Under the convergence rule this pass should have been a near-no-op.

It was not. The 07-19 pass ran the §2.4 citation ledger against the References block and found it clean, and it was clean — every entry present was correct. What a References-block ledger structurally cannot see is a claim whose support is *absent* rather than wrong. Two such defects were sitting in the body, untouched by a review that verified everything actually listed. The lens that caught them was reading the body's attributions *forward* to the bibliography rather than the bibliography *back* to the body.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Misattribution — Putnam's multiple-realizability examples (fixed).**
The article read: "a mammal, a mollusc, and a hypothetical silicon-based Martian might all be in pain," presented as Putnam's own illustration ("pain being his example"). The silicon-based Martian is **not Putnam's**. Putnam's 1967 demand is that the identity theorist find one physical-chemical state possible for a mammalian brain, a reptilian brain and a mollusc's brain (octopuses his own case) and impossible for anything that cannot feel pain. Verified at SEP's *Multiple Realizability* entry, which lists Putnam's terrestrial candidates (humans, primates, mammals, birds, reptiles, amphibians, molluscs/octopi) and then explicitly marks "silicon-based androids... and Martians with green slime" as the **encyclopedia author's** science-fiction expansion, not Putnam's text. Silicon and Martian realisers are later additions to the literature; the Martian case is Lewis's, not Putnam's.

This is the §2.5 "claims author didn't make" class. Fixed by restoring Putnam's actual terrestrial list and explicitly relegating silicon/extraterrestrial realisers to "later hands," which also *strengthens* the argument — the point that Putnam did not need exotic cases is dialectically better than the version that leaned on one.

**Sibling sweep** (per fix-by-file discipline): grepped `Martian` across `obsidian/`, `archive/`, `hugo/content/`. One sibling, `obsidian/concepts/substrate-independence.md:62` — "if pain can be realized in octopuses, humans, and hypothetical Martians." **Not a defect**: it omits the silicon specificity and does not present the list as Putnam's own examples, and Putnam's paper does gesture at extraterrestrial realisers ("parallel evolution, all over the universe"). Left as-is deliberately; no task minted.

**2. Unsupported claims — the entire "Modern Retreat and Revival" section (fixed).**
Four substantive historiographical claims about contemporary defenders, all attributed to unnamed "some defenders" / "others," with **zero citations**, inside an article otherwise carrying a full bibliographic apparatus. Every claim turned out to be true and attributable; none was sourced. Now sourced to Kim (1992) for local/structure-relative reduction, Bechtel & Mundale (1999) plus Polger & Shapiro (2016) for the grain objection, and Jackson, Pargetter & Prior (1982) for the second-order move.

**3. Category slip in the second-order-identity claim (fixed).**
The article described a revival that "defends a 'second-order' identity: the mental type is the property of having *some* physical state that plays the relevant role." As written this describes the functionalist second-order property, which is the position type-identity theory is normally contrasted *with* — so the sentence read as listing functionalism among type-identity's revivals. The real position (Jackson, Pargetter & Prior 1982) is that the second-order property is **compatible with** type-type identity rather than a refutation of it; SEP's *mind-identity* entry makes exactly this linkage. Re-framed to state compatibility rather than a "second-order identity," and cited.

### Publisher-of-Record Citation Web-Verify (§2.4)

The pre-existing five external entries were verified in the 07-19 ledger against an unmodified References block and are not re-litigated. The six **new** entries were each verified before insertion. `WebSearch` budget was exhausted this session; verification ran through `WebFetch` against publisher-deposited metadata (Crossref), OpenAlex, and publisher landing pages, per the WebFetch-survives-WebSearch-exhaustion route.

- Jackson, F. 1982, "Epiphenomenal Qualia", *The Philosophical Quarterly* 32(127), 127–136, DOI 10.2307/2960077 — **real-correct**. Crossref confirms title/author/venue/volume/issue/first-page; full range 127–136 confirmed at the **publisher of record** (academic.oup.com), not inferred.
- Jackson, F., Pargetter, R. & Prior, E. 1982, "Functionalism and Type-Type Identity Theories", *Philosophical Studies* 42(2), 209–225, DOI 10.1007/BF00374035 — **real-correct** (Crossref: all three authors, full range deposited).
- Levine, J. 1983, "Materialism and Qualia: The Explanatory Gap", *Pacific Philosophical Quarterly* 64(4), 354–361, DOI 10.1111/j.1468-0114.1983.tb00207.x — **real-correct** (Crossref, full range deposited).
- Kim, J. 1992, "Multiple Realization and the Metaphysics of Reduction", *Philosophy and Phenomenological Research* 52(1), 1–26, DOI 10.2307/2107741 — **real-correct**. Crossref and OpenAlex both carry first-page-only (JSTOR-DOI deposit artifact: `1–1`); Wiley returned 402. End page corroborated independently at Semantic Scholar (`1-26`) and consistent with the Crossref first page. Range asserted only after that second source, not from recall.
- Bechtel, W. & Mundale, J. 1999, "Multiple Realizability Revisited: Linking Cognitive and Neural States", *Philosophy of Science* 66(2), 175–207, DOI 10.1086/392683 — **real-correct**. Note the DOI is the Chicago-era `10.1086/` form, correct for a 1999 *Philosophy of Science* paper (the `10.1017/psa.*` form applies only post-Cambridge migration).
- Polger, T.W. & Shapiro, L.A. 2016, *The Multiple Realization Book*, Oxford University Press, DOI 10.1093/acprof:oso/9780198732891.001.0001 — **real-correct** (Crossref). A first DOI guess (`...9780199732883...`) returned zero results and was discarded rather than published — worth recording as a near-miss.

Shapiro 2000, "Multiple Realizations", *J. Phil.* 97(12) (DOI 10.2307/2678460) was verified as real but **deliberately not cited**: its end page was unverifiable at publisher, and the Polger & Shapiro 2016 monograph covers the same claim without a page-range exposure.

No superlative empirical claims (currency helper returned empty). Inline↔References cross-reference now complete in both directions: the Jackson and Levine attributions previously had no bibliographic entry at all, and every new inline `Author YYYY` has a matching entry.

### Attribution Accuracy Check

Re-ran against the body rather than the bibliography. Place (composition/definition "is", phenomenological fallacy), Feigl (nomological danglers), Smart (topic-neutral analysis, parsimony motive) and Kripke (rigid designators, heat/molecular-motion appearance-relocation, and "C-fibre firing" as his own example) all remain correct — consistent with the 07-19 finding. Putnam was the single failure, now fixed. No dropped qualifiers, no exploratory→commitment inflation, no source/Map conflation.

### Medium Issues Found

None outstanding. The L57/L71 reuse of the "pain has no appearance/reality gap" point was assessed in the 07-19 review as reinforcement serving two distinct dialectical purposes; that assessment stands and is not re-opened.

### Reasoning-Mode Classification (editor-internal)

Engagement with the identity theorist: **Mixed**, unchanged from 07-19 and unaffected by this pass's edits. Mode Three is declared explicitly ("the Map does not pretend to refute the identity theory from within the identity theorist's framework"), then narrowed to Mode Two ("The substantive objection the Map presses is narrower and does work from inside the debate") — the asserted-not-explained charge, with the bruteness escape blocked by a modal asymmetry the opponent already concedes for heat. The scope shift is signposted in the prose, so the Mode Three disclaimer and the Mode Two argument do not conflict. No boundary-substitution. No editor-vocabulary leakage into article prose.

### Counterarguments Considered

- "Identities are brute, so demanding a 'why' misreads identity claims" — answered in-article via the appearance/reality-gap asymmetry.
- Physicalist/eliminativist rejection of Tenet 1 — bedrock framework-boundary disagreement, honestly marked; not a defect.
- Neither counterargument is affected by this pass's changes.

## Optimistic Analysis Summary

### Strengths Preserved

- The "present at full strength before dissenting" structure, and the Place/Feigl/Smart division of labour.
- The type/token distinction correctly scoping the Map's target to the strong type-type claim.
- The substrate-sensitivity vs substrate-dependence contrast, which pre-empts the likeliest misreading of the Map's interface commitment.
- The explicit refusal of multiple realizability as "not the Map's tool" — calibration the Hardline Empiricist persona reads as exemplary restraint, since the Map declines a rhetorically convenient argument that would not actually support its conclusion.

### Enhancements Made

- Putnam's argument restated from his own text, with the exotic-realiser cases correctly relegated to later literature — a stronger version of the argument, not merely a corrected one.
- "Modern Retreat and Revival" moved from unattributed survey to a sourced one; the section now names the actual positions and their defenders.
- Second-order-property claim re-framed from a mis-stated "revival" to its accurate compatibility form.

### Cross-links Added

None. All fifteen existing wikilink targets were checked and resolve to live files; `topics:` correctly uses bare slugs. Adding links was not indicated — the Further Reading block is already comprehensive.

## Remaining Items

None.

## Stability Notes

- Physicalist/eliminativist rejection of Tenet 1 remains a **bedrock framework-boundary disagreement**. Future reviews should not re-flag it.
- The citation ledger is now complete for all eleven external entries across the 07-19 and 08-03 passes. Future passes on an unmodified References block may skip re-verification.
- **Lesson for the selector, worth carrying**: this article was chosen by a frontmatter-only bump and *looked* like a guaranteed no-op — the convergence-damping heuristic would have been right to suppress it on the evidence available. The defects it surfaced were pre-existing and had survived a thorough prior pass, because a References-block ledger verifies what is *listed* and cannot see a body claim with no support behind it. Both directions are needed: bibliography→body catches wrong citations, body→bibliography catches missing ones. A cosmetic-bump selection is a weak signal about the *delta*, not about the article.
- Word count 2095 → 2322 (+227), 93% of the 2500 concept soft threshold. Still `ok`, but headroom is now thin; further expansion of this article should be length-neutral.
