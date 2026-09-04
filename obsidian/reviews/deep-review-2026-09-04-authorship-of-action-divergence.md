---
title: "Deep Review - Authorship-of-Action Divergence"
created: 2026-09-04
modified: 2026-09-04
human_modified:
ai_modified: 2026-09-04T20:13:03+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[authorship-of-action-divergence]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-04
last_curated:
---

**Date**: 2026-09-04
**Article**: [[authorship-of-action-divergence|Authorship-of-Action Divergence]]
**Previous reviews**: [[deep-review-2026-07-16-authorship-of-action-divergence|2026-07-16]], [[deep-review-2026-06-16-authorship-of-action-divergence|2026-06-16]], [[deep-review-2026-06-05-authorship-of-action-divergence|2026-06-05]], [[deep-review-2026-05-22-authorship-of-action-divergence|2026-05-22]]
**Mode**: Fifth pass. The 2026-07-16 pass introduced claim-match verification (check (i)) and caught the Pärnamets/Grassi mismatch, but ran it against the *pupillometric* leg. This pass ran claim-match against the **detection-rate** leg — the paradigm's own numbers, which four prior passes had never opened the primary sources to check — and found the article's headline comparative claim inverted relative to both papers cited for it.

## Why This Candidate

Score 45 after convergence damping (4 prior reviews). `last_deep_review` 2026-07-16; the only intervening commit was the 2026-07-27 Rebouillat surname fix (`Léonetti` → `Leonetti`), which touched the References block and so kept the §2.4 web-verify trigger live. "Converged ≠ verified" applied again, this time to the numbers rather than the metadata.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Claim-direction inversion — concurrent vs. retrospective detection (FIXED).** The "Concurrent vs. retrospective detection" paragraph asserted that "Concurrent detection … **is lower than** retrospective detection, where subjects given more time, or asked targeted questions, recover the mismatch at higher rates (Hall et al. 2010; Hall, Johansson, and Strandberg 2012)." **Both cited papers report the opposite ordering.**
  - *Hall, Johansson & Strandberg 2012* (PLOS ONE 7(9) e45457), verified against the publisher full text: "In condition one, about one third of the trials was concurrently detected, and 8% of the trials were claimed to have been detected afterwards. In condition two, the concurrent detection rate was close to 50%, but very few participants claimed afterwards to have felt that something was wrong." Concurrent exceeds retrospective by roughly 4:1 in condition one and far more in condition two.
  - *Johansson et al. 2005* (Science 310(5745)), verified against the primary PDF: "With a total of 354 M trials performed, only 46 (13%) were detected concurrently … Tallying all forms of detection across all groups revealed that no more than 26% of all M trials were exposed." Retrospective plus possible-retrospective channels therefore add roughly 13 points — comparable to, not greater than, the concurrent channel.
  - *Hall et al. 2010* (Cognition 117(1)) reports a total detection rate ("no more than a third of the manipulated trials were detected") and does not license a concurrent/retrospective ordering claim at all; it was cited for a comparison it does not make.
  - **Resolution**: rewrote the paragraph to state what the sources report — concurrent 13% of 354 trials rising to ≤26% across all channels with post-experimental questioning; retrospective probing as the *smaller* channel that nonetheless roughly *doubles* what the online window alone exposes; the ~one-third-vs-further-8% split from the 2012 self-transforming-survey variant. Re-sourced the "more time" clause, which the article had fused with retrospective probing: free rather than fixed deliberation time raises the *concurrent* rate (to ≤27%), a different mechanism, and belongs to Johansson et al. 2005. Re-homed Hall et al. 2010 onto the claim it does support (the paradigm generalises to jams and teas at the same ≤one-third rate), which keeps it from becoming an orphan reference.
  - **Note**: the paragraph's *conclusion* — "the original non-detection rate is not a fixed feature of the introspective architecture but a property of the specific online-detection window the paradigm constructs" — survives the correction intact and is now actually supported by the numbers above it (13% → 26% when the window is widened). The defect was in the supporting comparison, not the inference drawn from it.

- **Internal contradiction — sub-type ordinal (FIXED).** The lead called the article "the fourth sub-type catalogued at source-attribution divergence"; the Further Reading gloss called the same relation "its fifth sub-type." The parent typology at [[source-attribution-divergence#the-typology]] lists reality-monitoring → external-source → self-other → **authorship-of-action** → voice-hearing, and the parent's own Further Reading entry says "the fourth sub-type." Fourth is correct. This is *residue from the 2026-05-22 pass*, which found and corrected the "fifth" in the lead but left the string sibling in Further Reading live — the fix-by-locus-leaves-string-siblings pattern. Corrected to "fourth."

- **Wrong-year attribution (FIXED).** Further Reading described "the **post-2008** Schurger reanalysis." Schurger, Sitt & Dehaene is **2012** (PNAS 109(42), E2904–E2913), as the article's own References entry states; 2008 is Soon et al., the fMRI extension treated in [[libet-experiments]], not Schurger. Corrected to "the Schurger, Sitt, and Dehaene (2012) reanalysis," which also gives the otherwise inline-uncited Schurger reference an explicit anchor.

### Publisher-of-Record Citation Web-Verify (per-cite ledger)

Trigger live (References block modified 2026-07-27). This pass ran check (i) claim-match against the paradigm's *quantitative* claims, which prior passes had not opened primary sources for.

- Johansson, Hall, Sikström & Olsson 2005 (*Science* 310(5745), 116–119) — **real-correct metadata; claim-direction partially wrong at the citing site (fixed)**. Primary PDF retrieved and grepped. Verbatim: "only 46 (13%) were detected concurrently"; "no more than 26% of all M trials were exposed"; "a higher detection rate in the free compared to the fixed viewing time conditions"; "Not even when participants were given free deliberation time and a set of LS faces to judge were more than 27% of all trials detected this way." The article's *qualitative* uses of this paper were faithful; the comparative claim built on top of it was not.
- Hall, Johansson & Strandberg 2012 (*PLOS ONE* 7(9), e45457) — **real-correct metadata; real-wrong-claim at the citing site (fixed)**. Full text retrieved from the publisher; the concurrent/retrospective numbers quoted above directly contradict the ordering it was cited for.
- Hall, Johansson, Tärning, Sikström & Deutgen 2010 (*Cognition* 117(1), 54–61; DOI 10.1016/j.cognition.2010.06.010) — **real-correct metadata; wrong-claim attachment (fixed)**. Europe PMC abstract verified verbatim: "In total, no more than a third of the manipulated trials were detected." No concurrent/retrospective ordering claim in the paper. Re-attached to the generalisation claim.
- Grassi, Hoeppe, Baytimur & Bartels 2025 (*Frontiers in Psychology* 16, 1598254) — **real-correct**. Re-verified at Crossref (DOI 10.3389/fpsyg.2025.1598254): authors Grassi, Pablo R.; Hoeppe, Lena; Baytimur, Emre; Bartels, Andreas; volume 16; article 1598254; issued 2025-12-04. Metadata and claim-direction both hold from the July pass.
- Rebouillat, Leonetti & Kouider 2021 (*Neuroscience of Consciousness* 2021(1), niab004) — **real-correct**. Re-verified at Europe PMC (DOI 10.1093/nc/niab004): `authorString` is "Rebouillat B, Leonetti JM, Kouider S." The 2026-07-27 de-accenting fix is confirmed correct at the publisher of record; no regression.
- Kane 2024 (*The Complex Tapestry of Free Will*, OUP) — **real-correct**. Verified at Crossref (book, OUP New York, 2024) and at the OUP catalogue (ISBN 9780197751404). The article omits the subtitle, which sources render inconsistently ("A Philosophical Odyssey" / "A Free Will Odyssey"); omission is the safer form.
- Sagana, Sauerland & Merckelbach 2014 (*Frontiers in Psychology* 5, 449); Kane 1996 (OUP); Wegner & Wheatley 1999 (*American Psychologist* 54(7), 480–492); Wegner 2002 (MIT Press); Schurger, Sitt & Dehaene 2012 (*PNAS* 109(42), E2904–E2913) — **real-correct**, verified across the June/July passes and unchanged; claim-directions re-read and faithful. Not re-litigated.

**Empirical-record currency sweep**: `find_superlative_claims` returns 0 candidates. Nothing to currency-check.

**Inline ↔ References cross-reference**: complete. Grassi 2025 was out of alphabetical order (filed between Kane 2024 and Rebouillat 2021); moved to the head of the list. Schurger 2012 is now anchored by an explicit "(2012)" in the Further Reading gloss rather than a bare "post-2008" allusion. No orphans in either direction.

**Wikilink resolution**: all 24 distinct wikilink targets resolve against the vault, with no ambiguous stems. `[[libet-experiments]]` resolves to `concepts/libet-experiments.md` (not `topics/`) — the bare slug is correct and unambiguous; the sibling `research/libet-experiments-free-will-2026-01-07.md` has a different stem and does not collide.

### Medium Issues

- **Redundancy (FIXED, length-motivated).** The "despite-commitments anchor / not predicted by standard rationality-and-choice models" claim appeared twice in near-identical form (Within-condition-spread paragraph and the Integration section). Tightened the second instance, which recovered roughly the words the citation correction spent.
- **"Load-bearing" as default intensifier (partially fixed).** Three instances. The Post-2005-programme one dissolved in the rewrite ("matters methodologically"); the "What … Cannot Deliver" opener changed to "worth stating outright." Left the Integration-section instance, per the writing-style guide's explicit note that existing uses need not be swept.

### Counterarguments Considered

- Brain-on-its-own confabulation (Dennett-style), Wegner's strong illusory reading, materialist absorption of the finding: preserved as honest live readings and framework-boundary marking, per all four prior reviews. Bedrock; not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The three "cannot deliver" boundaries, the mutual-constraint-not-mutual-support Kane register, and the discovery-from-outside parallel with aphantasia/synaesthesia are untouched.
- The Wegner section's explicit refusal of the strong illusory reading, with the Map's pushback attributed to "broader grounds, not from the choice-blindness data," remains the article's cleanest piece of scope discipline.

### Enhancements Made

- The corrected detection paragraph is now *more* informative than the one it replaces: it carries the actual numbers (13% concurrent, ≤26% all channels, ≤27% under free deliberation, one-third vs. further-8% in the 2012 variant, ≤one-third in the jam/tea replication) where the original carried an unquantified — and inverted — comparison. This is the rare case where the citation fix strengthens rather than merely repairs the passage, because the quantities make the paragraph's own conclusion visible.
- Hall et al. 2010 now earns its reference slot by supporting the cross-modal generalisation, a genuinely relevant fact the article had not stated.

### Cross-links Added

- None. The cross-link fabric is dense and fully resolving; no gaps found.

## Reasoning-Mode Classification (editor-internal)

- Engagement with Wegner's strong illusory reading: **Mode Three** (framework-boundary marking) — unchanged and correct.
- Engagement with materialist absorption ("the data do not establish dualism"): **Mode Three**.
- Engagement with Kane's framework: **Mixed (Mode Three / scope-clarification)**.

No label leakage; no editor-vocabulary in article prose.

## Possibility/Probability Slippage Check

- Detection-rate variability at *strongly supported* — correct, and now better anchored by the quantities.
- Interface-failure reading at *live hypothesis*, "not upgraded by the present case alone" — correct.
- Pupillometric corroboration at *contested but real* — correct.
- A tenet-accepting reviewer would not flag any remaining claim as overstated relative to the five-tier scale. No slippage. Note the corrected paragraph *reduces* an inadvertent overclaim: "retrospective detection recovers the mismatch at higher rates" implied more recoverable authorship-monitoring access than the data show.

## Length Check

- 2806 → 2902 words (97% of the 3000 soft threshold, status `ok`). Net +96: roughly +115 for the quantified citation correction, −20 recovered from the redundancy trim. No condensation required.

## Remaining Items

None for this article. One transferable observation: the 2026-07-16 pass introduced claim-match verification and applied it to the *bibliographic* leg (does this paper make this claim?), but the defect surviving into this pass was on the *quantitative* leg (does this paper report this ordering?). Numbers and comparatives inside a cited claim are their own verification target, and intra-corpus consistency ratifies an inverted comparison exactly as readily as it ratifies a wrong author.

## Stability Notes

- The corrected detection-rate ordering, the "fourth sub-type" ordinal, and the Schurger 2012 year are now verified against primary sources. Future passes should NOT re-flag them, and should not "restore" the retrospective-higher-than-concurrent framing — it is contradicted verbatim by both papers.
- The Pärnamets/Grassi swap resolved on 2026-07-16 holds; do not re-litigate.
- Bedrock framework-boundary disagreements (materialist absorption; Wegner's strong illusory reading; the interface-vs-confabulation underdetermination; Kane mutual-constraint register) are honestly handled and must NOT be re-flagged as critical.
- Five passes in, the article's citation base has now been checked on metadata, claim-match, and quantitative-claim dimensions. A "no critical issues" verdict is the expected next outcome; convergence damping (÷2.5 at five priors) should push re-selection well out.
