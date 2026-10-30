---
title: "Deep Review - Biological Naturalism"
created: 2026-10-30
modified: 2026-10-30
human_modified:
ai_modified: 2026-10-30T12:29:22+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-30
last_curated:
---

**Date**: 2026-10-30
**Article**: [[biological-naturalism|Biological Naturalism]]
**Previous review**: [[deep-review-2026-08-19-biological-naturalism|2026-08-19]] (fourth pass; earlier passes 2026-07-11 and 2026-07-19)
**Mode**: Selector pick (score 76, 72 days since last review). This pass checked the two edits that no deep review had seen. (a) `286eea9388` (2026-10-24, the expand-topic fork for `topics/blocks-harder-problem`) added a Block 2002 sentence to L82 and added reference 8. (b) `4a9b5f4f23` (2026-08-19 16:00Z) rewrote `## The Four Theses` *eight hours after* the 08-19 deep review. The brief said only (a) had moved; (b) had also never been reviewed.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Searle 2000 orphaned in References.** The 08-19 refine replaced "(Searle 1992; 2000; 2004; 2007)" with the 2004/2007 pins. That removed the only inline cite of reference 2. **Resolution**: the gloss on thesis 2 now cites it ("nothing non-biological is required (also Searle 2000)"). I fetched the 2000 *Annual Review* PDF (rctn.org copy) and grepped it this pass. Its abstract reads "Consciousness is entirely caused by neurobiological processes and is realized in brain structures", which supports the cite. I added a cite rather than deleting a correct reference.

### Medium Issues Found

- **The Block sentence (L82) under-reported Block's stance.** The quotes are verbatim, but the sentence framed Block as pressing an objection on Searle ("agrees … yet says …"). In fact Block writes as a fellow naturalist. His paragraph closes "The issue that I am raising here for naturalist phenomenal realism threatens my view as much as his". The agreement sentence the article quotes comes straight after a qualification it left out: "(However, I don't agree with Searle's view that the neural bases of conscious states 'cause' the conscious states in any normal sense of 'cause'.)" That qualification matters for this page, because it is a fellow naturalist rejecting Searle's thesis 2 framing. This is the immediate-qualification shape that the open P3 critic-completeness task names. **Resolution**: the sentence now calls Block "a fellow naturalist" and paraphrases his rejection of the causal framing. It also states that the harder problem is "a predicament for naturalism that he says threatens his own view as much as Searle's". All the additions are paraphrase without quotation marks, so they add no new quote-fidelity surface. The two quotations kept are byte-identical. "his harder problem" (ambiguous between Block and Searle) became "Block's harder problem". The new wording does not enlist Block for dualism.
- **Quote pinned to a work that does not contain it (L32).** "a modicum of scientific knowledge" sat under "(Searle 2004, pp. 113–114; restated in Searle 2007, pp. 327–328)". Grep of the 2004 full text: 0 hits. Grep of the 2007 Companion scan: 1 hit, on the page headed "BIOLOGICAL NATURALISM 329". **Resolution**: added "(Searle 2007, p. 329)" after the quotation.
- **Currency: Searle died on 17 September 2025.** The Guardian obituary (via inkl) gives "born 31 July 1932; died 17 September 2025". Semafor (30 Sep 2025), the Boston Globe (13 Oct 2025), MetaFilter (relaying his secretary's email) and Colin McGinn's post agree. The article had no present-tense *biographical* framing; its present tense describes his arguments, which is fine. **Resolution**: added "(1932–2025)" to the lead. A corpus sweep of Searle mentions for living-author framing ("Berkeley", "alive", "currently", "1932", etc.) found nothing to fix.

### Publisher-of-Record Citation Ledger (§2.4)

- Block 2002, "The Harder Problem of Consciousness", *Journal of Philosophy* 99(8), 391–425, DOI 10.2307/3655621. **real-correct.** Crossref gives Block, Ned; *The Journal of Philosophy*; vol. 99, issue 8; first page 391; issued 2002-08; Philosophy Documentation Center. The end page 425 matches the published range reported by the web search and the research note.
  - "that consciousness is a matter of the biology of the organism, not (just) its information processing": exact-count 1 in the Philosopher's Annual reprint text (pgrim.org). The JPhil page locator (pp. 405–406) comes from the research note; the reprint has no page numbers.
  - "we do not now have any conception of how it could be tested": exact-count 1, same source. Context checked: "it" refers to whether Commander Data is phenomenally conscious, which Block treats as Searle's "empirical question". The article's gloss is faithful.
  - Block's stance: "my naturalist phenomenal realist view is not that different from his"; naturalism means "default physicalism"; "I think the standard arguments against physicalism don't work". He argues as a physicalist and is not enlisted for dualism.
- Searle 2004, *Mind: A Brief Introduction*, pp. 113–114. **real-correct.** archive.org djvu text, page header 113 before the list and 114 after it. Each quotation has exact-count 1: "with their subjective, first-person ontology, are real phenomena in the real world"; "absolutely no life of their own, independent of the neurobiology"; "Because conscious states are real features of the real world, they function causally"; "would leave out the first-person ontology of consciousness" (OCR line-break hyphen only).
- Searle 2007, Blackwell Companion, print ch. 25. **real-correct.** The four theses are on pp. 327–328 and "a modicum of scientific knowledge" is on p. 329. That locator is now fixed in the text.
- Searle 2008, "Why I Am Not a Property Dualist" (northwestern.edu preprint). **real-correct.** "over and above" occurs 12 times, including "'Consciousness' does not name a distinct, separate phenomenon, something over and above its neurobiological base, rather it names a state that the neurobiological system can be in". That supports L42. Re-grepped this pass: "has no causal powers of its own" (2), "causally speaking, there is nothing there" (1), "a state the brain can be in" (1), "Try making a piston" (1).
- Searle 2000, *Annual Review of Neuroscience* 23, 557–578. **real-correct.** The PDF header reads "Annu. Rev. Neurosci. 2000. 23:557–578". It is now cited inline (see Critical).
- Searle 1992 p. 122, Kim 1998, Chalmers 1996: unchanged and not re-litigated (07-19 ledger). Kim and Chalmers are cited by name without a year, a convention earlier reviews accepted.
- Searle's replies at L82 (Brain Simulator: form vs causal powers; Many Mansions: abandons the specific claim). These are unquoted paraphrases, unchanged since 08-19 and consistent with the sibling `chinese-room-argument` L75. The 1980 primary was not re-fetched (cogprints copy returned 403).
- Currency sweep: no superlative claims.

### Counterarguments Considered

- Kim's causal exclusion and the Chalmers/Corcoran/Nagel collapse charge: bedrock, per the stability notes. Not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The 08-19 refine's four-thesis rewrite. I re-verified it at primary text this pass and found it faithful in content and order. It is the right shape for a rival-statement page.
- The Liquidity Disanalogy section, horn two's answer to the parity argument, the steelman paragraph, and the symmetric ensemble-level-epiphenomenalism concession. All untouched.

### Enhancements Made

- The Block sentence now shows a physicalist-leaning naturalist sharing the predicament instead of pressing it. That fits the Map's calibration: the harder problem shows up as an epistemic difficulty inside naturalism and is not offered as evidence for dualism. The added rejection of Searle's "cause" framing gives thesis 2 an outside naturalist's dissent at no quotation risk.

### Cross-links Added

- None. `topics/blocks-harder-problem` L142 already links back.

## Length

`analyze_length` 2,729 → 2,777 (+48). Concepts soft 2,500 / hard 3,500. The status stays `soft_warning`, within the +80 budget.

## Remaining Items

- None in this article. The open P3 cross-review of `topics/blocks-harder-problem` can rely on the Block reading recorded here. Block's "threatens my view as much as his" and his parenthetical rejecting Searle's "cause" framing are worth checking on other hosts that quote Block's agreement with Searle.

## Stability Notes

- Carried forward: the Kim and collapse charges are bedrock; the four-thesis list is verified at primary text, so do not reopen it.
- The 08-19 "no body delta" assumption failed again in a new way. A refine landed eight hours after that review and orphaned a reference. Future briefs should diff against `last_deep_review` with `git log --since`, and should not rely on recalled commit lists.
- Engagement classification (editor-internal): Block is reported exposition. The sentence marks him as a fellow naturalist sharing the predicament, so there is no engagement-mode claim. Kim is Mode One, unchanged; the collapse charge is Mode Mixed, unchanged. No editor labels leak into the prose.
