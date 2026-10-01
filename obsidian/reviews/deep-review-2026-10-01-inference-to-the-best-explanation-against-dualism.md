---
title: "Deep Review - Inference to the Best Explanation Against Dualism"
created: 2026-10-01
modified: 2026-10-01
human_modified: null
ai_modified: 2026-10-01T22:33:01+00:00
draft: false
topics: []
concepts:
  - "[[inference-to-the-best-explanation-against-dualism]]"
related_articles:
  - "[[pessimistic-2026-10-01-inference-to-the-best-explanation-against-dualism]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-01
last_curated: null
---

**Date**: 2026-10-01
**Article**: [[inference-to-the-best-explanation-against-dualism|Inference to the Best Explanation Against Dualism]]
**Previous review**: Never deep-reviewed. Prior passes: created 08:05Z; cross-reviewed 08:41Z; [[pessimistic-2026-10-01-inference-to-the-best-explanation-against-dualism|pessimistic review]] 16:22Z, whose priority items were applied by three refines (17:53Z items 1 and 3; 18:08Z item 2; 21:54Z item 4).
**Research note**: [[research/inference-to-the-best-explanation-against-dualism-2026-10-01]]
**Word count**: 3,331 → 3,322 by `analyze_length` (−9; concepts hard gate 3,500 `>=`, so 177 words of headroom remain for the queued P3 second-order IBE paragraph, capped at ~150). Line numbers below are from the edited file, which is 2 lines longer at the top because of the new frontmatter keys. Former L30 is now L32, and so on.

## Method

- The pessimistic review was read in full, and so were the changelog entries for the three refines.
- The research note's Gaps section was read to its end. Its "Weir 2021b unresolved" line is the known ditto-mark false zero. The page already describes 2021b correctly, and a separate P3 corrects the note.
- `tenets.md` was read at L51–55 (Tenet 1 rationale), L63–69 (Tenet 2 and the minimality clause), L89–107 (Tenet 3, `^tenet-3-standing`, outcome-selection) and L131 (Tenet 5).
- `project/evidential-status-discipline` was read at L78, L100, L112–122 and L214, plus the Decorative-Falsifier Rule.
- External sources were fetched fresh this session with curl and grepped after whitespace and quote normalisation: the Farmakis–Hartmann NDPR review, Gertler's preprint, the Swinburne 2009 author PDF, SEP "Abduction", SEP "Dualism", SEP "Physicalism", the Lycan abstract (OpenAlex), and Crossref records for every DOI.
- Sibling Map pages were read where the article quotes or characterises them.
- Per the brief, these were not re-verified because the 21:54Z refine had already verified them: the Henderson abstract spans, Stoljar's "seems", Douven on Harman, and the Witmer NDPR.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **The quoted source's referent was misdescribed (L42).** The page said the NCC page's "NCC findings are compatible with all three" covers "identity, epiphenomenalism and interaction". The NCC page's list at L73–75 is **Identity, Emergence, Interaction**. Its only "all three" is L77, and epiphenomenalism is not in the list. *Fixed*: "epiphenomenalism" → "emergence" (0 words).
2. **The 17:53Z refine left an internal contradiction (L42).** That refine changed "compatibility is a claim about likelihoods" to "…about consistency" but left the next sentence, "'Both are compatible' answers a likeliness challenge and leaves the loveliness challenge untouched". That sentence now contradicts both its own premise (consistency does not answer a likeliness challenge) and L58, which concedes that "part of the physicalist's loveliness is a likelihood advantage". This is a fix that stranded its dependent. *Fixed*: "answers a likeliness challenge and leaves the loveliness challenge untouched:" → "answers neither challenge: consistency falls short of equal likelihood, and" (0 words). The lead's "answers a different challenge from the one it poses" now matches it.
3. **The corridor was described in absolute terms that contradict the page's own disconfirmer (L70 vs L82).** L70 said the corridor "is built to leave no independently measurable non-physical input". L82's rise clause (written by the same 17:53Z refine) relies on an intention-conditioned departure that would be exactly such an input. `tenets.md` L107 keeps that conditional deviation "live (P-Q3)", and `apex/born-preserving-causal-efficacy` horn (a) puts the corridor's exposure there. Read literally, L70 would make L82's rise clause decorative. *Fixed*: "…no independently measurable non-physical input" → "…no non-physical input measurable in aggregate" (+1), and "A posit tuned to leave no trace" → "…no aggregate trace" (+1). The seventh explanandum ("the absence, so far, of…") is still accommodated, because aggregate nulls are null by construction and the conditional tests have not been run. The tier and "the idleness objection at full force" are unchanged, since no gain in strength has been shown.

### Medium Issues Found

4. **The grain was overstated (L82).** The page said "at a grain [the conditional-signature analysis] specifies". The apex formalises the test (P(O | do(C), X) ≠ q(O | X)) but names no grain. It says the corridor "is untested at every grain" (L89) and that exposure lives "in whether it asserts (2) at some specifiable grain" (L109). *Fixed*: "at some grain, as … formalises" (+1).
5. **Content determinacy was in the lead's widened set (L32).** That set listed content determinacy as data that "the strongest physicalist rival grants … and explains through phenomenal concepts". The phenomenal-concepts strategy is not an account of content determinacy, and Quinean physicalists deny the datum. The body never runs reply 1 on it: content determinacy appears only in the lead and in L84, where it is the explanandum of the Map's own PCT bet. Counting it in the lead counts that bet twice, which the pessimistic review's (a) assessment noted. The 18:08Z refine also recorded it as a residual. *Fixed*: the widened set is now "phenomenal character and the acquaintance asymmetry" (−2). Lead and body now name the same set.
6. **The tier vocabulary disagreed with the ladder (L62).** The page said "evidence that *supports* it" while every tier tag on the page says *suggestive*. The discipline's ladder is compatible / suggestive / discriminating (L100), and its rival-model section reserves *support* for cases with a named discriminator (L112). The middle rung was therefore labelled with the top rung's word. *Fixed*: "evidence *suggestive* of it" (0).
7. **The reply-1 tag lacked the qualifier (L64).** "Tier reached: *suggestive*, and only on the widened set" left out the "provisionally" that the lead, the Verdict and L80 all carry. *Fixed*: "*suggestive*, provisionally, and only on the widened set" (+1).
8. **Tenet 5 was over-read in Relation to Site Perspective (L92).** The paragraph opens "blunts the inference without defeating it", and reply 3 ends at "partly unlicensed" because Tenet 5 reaches only the simplicity component, not unification. Yet the same paragraph said Tenet 5 "gives reason to withhold belief from the physicalist's conclusion", which is defeat-strength. *Fixed*: "and so lowers the confidence the physicalist's conclusion can claim" (−1).
9. **Lycan's stance was ambiguous (L86, cited-author-stance leg).** Lycan was quoted in the paragraph that opens "Among the dualist texts retrieved", but he is a materialist. The corpus says so at `topics/parsimony-case-for-interactionist-dualism` L59 and `apex/dualism-cartography` L115 ("a committed materialist of over forty years"). His abstract concedes answerability. It does not endorse dualism. *Fixed*: "The materialist William Lycan's 2009 abstract" (+2).

### Low Issues Found

10. **McLaughlin absence claim was too strong (Ref 8, L44).** "No abstract exists" claimed more than the evidence shows. Crossref and OpenAlex hold no abstract. Semantic Scholar returns `abstract: null` with the notice "The following paper fields have been elided by the publisher: {'abstract'}". Wiley's landing page returned a Cloudflare 403. *Fixed*: Ref 8 → "(not consulted; sole author, no abstract served, per three metadata services)", and L44 "none holds an abstract" → "none serves an abstract" (0). McLaughlin 2010 stays a LEAD: not paraphrased and not linked to Melnyk.
11. **Swinburne metadata was resolved (Ref 14).** Crossref has `10.5840/faithphil200926551`: *Faith and Philosophy* 26(5), 501–513. The issue number is now verified, so "issue number unverified" was dropped and the DOI added (−2).
12. **A redundant clause was trimmed (L84).** "The Map's abductions are subject to the same objections," repeated the previous sentence. It was cut (−9). The named tier ("blunted exactly as far as the physicalist's", from the 18:08Z refine) is kept.

### Publisher-of-Record Citation Ledger (§2.4)

- Douven 2025 (SEP "Abduction") — real-correct. `citation_author` is Douven, Igor. The entry reads "First published Wed Mar 9, 2011; substantive revision Wed Jun 18, 2025".
- Farmakis & Hartmann 2005 (NDPR) — real-correct. "Reviewed by Lefteris Farmakis … and Stephan Hartmann … 2005.06.01". The review gives Lipton as Routledge 2004, 2nd ed.
- Gertler 2020 — real-correct. Crossref: "Dualism" with subtitle "How Epistemic Issues Drive Debates about the Ontology of Consciousness", editor Kriegel, pp. 276–300, OUP.
- Harman 1965 — real-correct. *Philosophical Review* 74(1), first page 88 (Crossref). The page range 88–95 is standard.
- Henderson 2014 — real-correct. BJPS 65(4) 687–715. The spans were verified by the 21:54Z/17:53Z refines and not redone.
- Lipton 2004 — real-correct. Crossref dates the 10.4324 e-book record 2003-10-04, while the NDPR header and print edition give 2004, which is the conventional citation year.
- Lycan 2009 — real-correct. AJP 87(4) 551–563. OpenAlex dates it 2008 (online first). Stance recorded: materialist.
- McLaughlin 2010 — real-correct metadata. *Philosophical Issues* 20(1) 266–304, sole author at Crossref, OpenAlex and S2. The label was corrected (item 10).
- Melnyk 2003 — real-correct (CUP).
- Okasha 2000 — real-correct. SHPS A 31(4) 691–710. Douven places it with Lipton ch. 7 among views on which explanatory considerations bear on priors and likelihoods, which supports L58's description.
- Papineau 2001 — real-correct. *Physicalism and its Discontents* pp. 3–36. The 2002 work has no DOI, as the research note already says.
- Robinson & Weir 2025 (SEP "Dualism") — real-correct (verified by the 21:54Z refine).
- Stoljar 2026 (SEP "Physicalism") — real-correct (verified by the 21:54Z refine).
- Swinburne 2009 — real-wrong-metadata (label only; issue verified, DOI added).
- van Fraassen 1989 — real-correct (OUP 10.1093/0198248601.001.0001).
- Witmer 2004 (NDPR) — real-correct (D. Gene Witmer per the 21:54Z refine; 2004.06.04 confirmed on the fetched page).
- The Map self-cites (ensemble-level-epiphenomenalism, created 2026-05-27; closure survey, created 2026-03-19) — real-correct. Dates match the frontmatter; the pseudonymous co-author form is the house convention.

**(Surname, year) orphan check, both directions.** Every reference is cited in the body: refs 1–16 by surname or "the *Stanford Encyclopedia* entry on dualism" (ref 12), and refs 17–18 by wikilink. Every body citation with a year has an entry. "Weir 2021b" appears in the body as the SEP entry's own attribution and is covered by ref 12's label ("Weir 2021b not consulted"). The bibliographic identity comes from the entry's own list, per the 21:54Z refine. Names without years are mentions, not citations: E. J. Lowe (via SEP), "Hasker, Lowe's monographs and Robinson's own" (not searched), and "Chalmers's master argument" (a pointer to the PCS page, which carries it at L79/L187). No orphans.

**Superlative / currency sweep.** No empirical superlatives. "Strongest argument the physicalist has" is the page's argued thesis (L38–44), not an empirical record claim.

**Result-direction leg.** The page has no empirical results, only philosophical sources. The direction of each source's claim was checked under the quote ledger below.

### Quote-Fidelity Ledger (spans not verified by the refines)

All verbatim unless noted:

- Outer review (`reviews/outer-review-2026-10-01-chatgpt-5-6-sol-pro` L272–280). The seven explananda match the bulleted list. Wording differs only outside quotation marks ("changes"/"change", "nonphysical"/"non-physical"). The conclusion "The dualist must either produce additional predictive success or explain why the extra psychophysical ontology is not explanatorily idle." is at L280.
- Farmakis & Hartmann on Lipton:
  - "inference to the *loveliest* explanation, not inference to the *likeliest* explanation" matches, including the `<i>` italics on both words. These are the reviewers' words for Lipton's characterisation, and the page attributes them via the review.
  - "the one that, if correct, provides the most understanding" (p. 59) matches.
  - "ultimately concludes that if IBE is a reasonable model … coextensive" (p. 61) matches.
  - The van Fraassen span, "not only does IBE not guarantee … the converse most likely holds", matches. The reviewers call it "van Fraassen's charge".
  - Context the page does not report: the same paragraph says Lipton's response is "considerably forceful" and argues the charge is inconsistent. The page presents the two positions side by side without adjudicating, so this is not a misrepresentation.
- Gertler 2020 preprint:
  - "need not include special fundamental laws linking structural-dynamic phenomena to consciousness" matches. Gertler calls this dimension *elegance*; "fewer basic kinds of things" is *parsimony*. Both labels match the page.
  - "simplicity concerns guide theory choice only when the theories being compared accommodate the data equally well" matches.
  - "we should be wary of taking the perceived threat to simplicity as grounds for skepticism about the data used to support dualism" matches.
- Swinburne 2009 (author PDF, 13 pp.): 0 hits for "expla" and 0 for "explain". Positive controls: "soul" 19, "substance" 77, "dualism" 14. The negative control holds.
- Lycan 2009 (OpenAlex abstract): "that no convincing case has been made against substance dualism, and that standard objections to it can be credibly answered" matches.
- Douven (SEP Abduction): "may well lead us to believe "the best of a bad lot" (van Fraassen 1989, 143)" matches. It is said of ABD1, the comparative rule, so "rival-ranking schema" is a fair gloss.
- SEP Dualism (Robinson & Weir):
  - "breaches ordinary standards of theory choice by sacrificing simplicity for no gain in strength" matches.
  - "This principle would lead us to favour epiphenomenalism over Lowe's proposal (Weir 2021b)" matches.
  - The entry describes Lowe's proposal as invisible to scientific observation, which matches the page.
- SEP Physicalism (Stoljar): "it is rational to be guided in one's metaphysical commitments by the methods of natural science" matches. It is the first premise of what Stoljar calls "the argument from methodological naturalism", his second argument after closure. The page's "alongside closure" is correct.
- Closure survey L91: the rendered text "given how systematically … the best explanation is that there is nothing further to find" matches. A piped link back to this page sits inside the span, and the page correctly says "in the Map's words". The survey's L87–89 support "inductive two-strand argument from the physiological and physical records".
- PCT L80: "an *abductive bet*" matches. The page's gloss (IBE of content determinacy and understanding across deflationism, weak liberalism and PCT) matches PCT L80–86.
- NCC L77: "NCC findings are compatible with all three" matches in rendered text, but the referent was wrong (Critical 1).
- parsimony-epistemology L88: "a tie-breaker between theories that explain the same phenomena equally well" matches in rendered text (piped link inside).
- ensemble-level-epiphenomenalism:
  - "touches the physical world only in ways the physical world's own statistics already account for" (L39) matches.
  - "hidden idleness" appears only in that page's frontmatter description (L3), not its body, which says "*de facto* idleness". It is verbatim page text, so it was accepted, and the source location is recorded here.
- tenets.md:
  - "a commitment the Map owns, not a result it reports" (L55) matches.
  - "without showing it to be *actual*" (L95) matches.
  - "is therefore a posit the interface argument leaves open, not a result it secures" (L95) matches.
  - The P-Q10 toy-model sentence (L95) is accurate paraphrase.
  - Tenet 5, "is not a reliable guide to truth when knowledge is incomplete" (L131), matches.
  - Tenet 2 "fixes its minimality by this very record" accurately paraphrases L69.
- Discipline:
  - "a tenet may remove a defeater but may not upgrade the evidence" accurately paraphrases L78.
  - "what would lower, leave unchanged and raise confidence" accurately paraphrases L214.
- Other Map characterisations:
  - "dualism's ledger of explanatory debts is at least as good as physicalism's" is a fair gloss of parsimony-case L122 ("closer to a draw than a clean win", with a residual asymmetry in dualism's favour) and its description ("it does not favour physicalism").
  - The "acquaintance asymmetry" label matches philosophy-of-science-under-dualism L82–84.
- Not re-verified at a source this pass: that Harman 1965 *coined* the name. Douven does not state it. This is the standard attribution and agrees with the paper's title.

### Counterarguments Considered

- **Type-B physicalist (Papineau, Loar, Balog).** Addressed by the provisional tier, now on every surface. The second-order comparison remains owed (the open P3), and this review did not do it.
- **Bayesian (Henderson).** L58's likelihood-advantage concession stands. A dualist reply is available: Type-B *a posteriori* identities are also fitted to the correlations. That would narrow the concession, and the page's "part of" is the right hedge for it. This is recorded as a stability note, not an edit.
- **Quantum skeptic (Tegmark).** The coherence precondition the pessimistic review flagged is now partly moot. `tenets.md` L91 makes the post-decoherence outcome-selection variant (b) the most strongly endorsed path, and that variant sidesteps the coherence-survival requirement. No edit.
- **Eliminativist and Dennettian double-counting objections.** Already answered by the identity-hypothesis qualifier at L64 (18:08Z). Bedrock.

### Reasoning-Mode Classification (editor-internal)

- Physicalist IBE vs reply 1: Mode Two against Type-A (the explanandum set omits phenomenal character without argument) and Mode Three against Type-B (provisional; comparison unrun).
- Reply 2: Mode Three (tenet-bounded; non-idleness owed).
- Reply 3: Mode One, narrowed. It uses Lipton's own coextension bridge and van Fraassen's critique, which are internal to IBE methodology, and is limited to the simplicity component.
- Reply 4: Mode Three. It secures neutrality only toward the fitted variant, and the Lowe/Weir idleness objection is conceded at full force.
- Reply 5: Mode One, symmetric.
- No label leakage. "Tier reached:" is licensed because the tier ladder is the page's subject (pessimistic review, Language table).

## Optimistic Analysis Summary

### Strengths Preserved

- The front-loaded verdict now agrees on every surface: lead L32, reply tags L64–L70, Verdict L74, costs L80 and Relation L90–94. The agreed tiers are compatible on the seven explananda, suggestive and provisional on the widened set against Type-B, and discriminating nowhere. "Accommodates" is used throughout, and the page contains no "predicts" claim for the Map (grep confirms).
- The honest McLaughlin handling: a lead, never paraphrased, never attributed to Melnyk.
- The labelled Map reconstructions (the levels claim, the Bayesian reading, the Stoljar equivalence).
- The positive and negative controls on the dualist-literature absence claim.
- The rise / unchanged / fall disconfirmer. It is now consistent with L70 and with the apex.
- The symmetric bad-lot treatment of the Map's own abductions (reply 1 and PCT).
- Hardline Empiricist (Birch): this is a model page for declining a tenet-as-evidence upgrade. It concedes a likelihood advantage to the rival, which its anchor concept page does not.
- Mysterian (McGinn): reply 5's "constrains the opponent's inference, and the Map's own abductions in the same way" is a clean statement of cognitive-closure humility without overreach.
- Process Philosopher (Whitehead) vs Hardline Empiricist: no tension to resolve. The page grants no upgrade from tenet-coherence.

### Enhancements Made

- Calibration and consistency only (items 1–12). No expansion, because the page is in length-neutral mode.

### Cross-links Added

- None. Headroom is reserved for the P3.

## Anchoring Audit

`evaluate_anchoring` flagged the page against `concepts/neural-correlates-of-consciousness` on two checks:

- hedge_density: 2.10/kw against a 2.46/kw target.
- underdetermination_markers: 0 against the anchor's 1.

The anchor's single marker is "NCC data is compatible with either reading".

The flag was confirmed **lexical**. The page states its calibration structurally:

- the explicit tier ladder, with "Tier reached: *compatible*" three times;
- "provisional" against Type-B;
- "discriminating nowhere";
- "a prior the evidence does not raise";
- "owed, not shown";
- "No such test has been run";
- access labels on all 18 references.

It is also stricter than its anchor, because it concedes a likelihood advantage to physicalism. No calibration gap was found that hedges would fix; the real sentence-level gaps (items 3, 4, 8) were fixed directly. `anchoring_audit_exempt: true` was added with a dated YAML comment at byte offset 383, inside the 1,500-byte window. A re-run of `evaluate_anchoring` returns `[]`.

## Remaining Items

- **Owned P3, not done here (by brief):** run the second-order IBE against the phenomenal-concepts strategy, ~150 words. There is 177 words of headroom.
- **Would-mint (cross-page seam, outside this page):** `concepts/philosophy-of-science-under-dualism` L104–106 says Bayesian confirmation "cannot" adjudicate, because "where two programmes are genuinely empirically equivalent … the likelihood ratio is one". The IBE page (via Henderson 2014) now holds that generic dualism pays a likelihood cost for bridge laws fitted to the evidence. The two claims are reconcilable, since the likelihood ratio is one only once the auxiliaries are fixed, but the philosophy-of-science page never says so. Suggested task: a P3 refine-draft adding one sentence there that scopes the claim to auxiliary-fixed hypotheses and links the IBE page's Bayesian section. Cost about +25 words; that page was at 2,699 when the research note measured it.
- **Would-mint (owed on the host, carried from the pessimistic review, not yet queued as far as this review saw):** `concepts/parsimony-epistemology` L90 still describes Type-B with a Type-C description ("arguing future progress will close it"). Not checked against todo.md, which this review did not read or write. The driver should dedupe.
- **Optional, not applied:** the Verdict could state that *compatible* on the seven explananda holds for dualism with bridge laws fitted to them (~+8 words). The body already says this at L58 and L70. The register's *compatible* tier means "fits both", which is true of the fitted variant, so the Verdict as written is not miscalibrated. Leave it unless headroom remains after the P3.

## Stability Notes

- **The likelihood-advantage concession (L58) is calibrated, not over-conceded.** A dualist can reply that Type-B identities are as fitted as bridge laws. The page's "part of" already absorbs that. Future reviews should neither strengthen nor delete the concession without new argument.
- **"Hidden idleness" quotes ensemble-level-epiphenomenalism's frontmatter description (L3), not its body.** This is verbatim and intended; do not re-flag it as a false quote.
- **"Tier reached:" tags are licensed vocabulary on this page.** The tier ladder is its subject. Do not re-flag them as label leakage.
- **The corridor is built to leave no aggregate trace.** Conditional signatures stay live, per `tenets.md` L107 and apex horn (a). Any future edit that restores an absolute "leaves no measurable input" re-creates the L70/L82 contradiction.
- **The widened set is phenomenal character plus the acquaintance asymmetry.** Content determinacy belongs to PCT's own abduction (L84) and should not be re-added to reply 1's set.
- **Eliminativist, Dennettian and Many-Worlds disagreements are bedrock** (as the pessimistic review also recorded).
