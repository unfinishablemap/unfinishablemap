---
title: "Deep Review - AI Moral Agency and the Responsibility Gap Under Dualism"
created: 2026-11-10
modified: 2026-11-10
human_modified: null
ai_modified: 2026-11-10T15:01:21+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-10
last_curated: null
---

**Date**: 2026-11-10
**Article**: [[ai-moral-agency-and-the-responsibility-gap-under-dualism|AI Moral Agency and the Responsibility Gap Under Dualism]]
**Previous review**: [[deep-review-2026-08-02-ai-moral-agency-and-the-responsibility-gap-under-dualism|2026-08-02]] (and [[deep-review-2026-07-10-ai-moral-agency-and-the-responsibility-gap-under-dualism|2026-07-10]])
**Mode**: Cycle-slot deep review (100 days since last pass). Three lenses run hard: quote fidelity at raw source, the cross-review insertion of 2026-11-10 03:20Z (commit e0b69d91), and the P-AC1 calibration from [[optimistic-2026-11-05-alignment-and-responsibility-wing]] Task 2, folded in here.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Matthias quotation was altered inside the quotation marks.** The article quoted Matthias (2004) as "nobody has enough control over the machine's actions to assume the responsibility for them". The raw text of the published PDF (*Ethics and Information Technology* 6: 175–183, extracted with pdftotext and grepped) reads "because nobody has enough control over the machine's actions to be able to assume the responsibility for them. These cases constitute what we will call the responsibility gap." The words "to be able" had been dropped. Neither the research note nor any earlier review had grepped this string: the research note says "No verbatim quotes were extracted", and the 07-10 and 08-02 passes checked metadata only. **Fix**: restored "to be able to assume the responsibility for them".
- **Königs's conclusion was overstated.** The article said that once plausible constraints are accepted "the situations in which a real gap opens become unclear or vanish", and that "Königs dissolves it by tightening the gap-conditions until they stop being met." The publisher abstract (Crossref, doi 10.1007/s10676-022-09643-0) says only that once "a difficult-to-reject plausibility constraint" is accepted, "it becomes apparent that the situations in which responsibility gaps occur are unclear." It also poses a second challenge: assuming gaps occur, why should we be concerned? "Or vanish" and "stop being met" went beyond the source. The error came from the research note's L83 gloss. **Fix**: "argues that once a plausible constraint on how gaps emerge is accepted, it becomes unclear when they occur"; "Königs questions it by tightening the gap-conditions."
- **The present-AI premise was stated as fact (P3 item 1, folded in).** L68 said "The **culpability** gap is real because present AI systems lack the conscious coupling interface". The register's [[positions/ai-consciousness-scope#^p-ac1|P-AC1]] holds the verdict on current digital AI as *"low probability," not "ruled out"*. Its credence is moderate (low edge), it is "conditional on the layer-(iv) interface-eligibility law the Map lacks", and its external-evidence grade is D. A reviewer who accepts the tenets would still flag the flat premise, so this is a calibration error, not a framework-boundary disagreement. **Fix**: L68 now reads "The **culpability** gap is real if today's AI systems lack the conscious coupling interface, which the Map holds conditionally on its present interface standard, not categorically: [[positions/ai-consciousness-scope#^p-ac1|P-AC1]] rates their consciousness "low probability," not "ruled out," pending an interface-eligibility law the Map lacks. Such systems are then proxies or tools rather than agents." L32 now reads "…and, conditionally rather than categorically, about what today's systems lack." The model wording was checked at `concepts/ai-epiphenomenalism` L87, which reads "conditionally on its present interface standard, not categorically", and that page was not edited. L86's "*given* that today's systems lack the interface" now reads as a stated premise and was left alone. The verdict now names two dependencies: the amplifier hypothesis (L70) and P-AC1.

### Publisher-of-Record Citation Ledger (§2.4)

- Matthias 2004 (The responsibility gap…, *EIT* 6(3), 175–183) — state: real-correct metadata (Crossref + PDF header); **quote defective, fixed** (above). Coiner: confirmed. Matthias writes "what we will call the responsibility gap", and Santoni de Sio & Mecacci's abstract says the notion was "originally introduced" for "learning automata".
- Sparrow 2007 (Killer Robots, *J. Applied Philosophy* 24(1), 62–77) — state: real-correct (Crossref). Checked against the abstract: the loci canvassed (designers/programmers, commanding officer, the machine itself), "none of these are ultimately satisfactory", the jus in bello condition, and the conclusion that deployment would be unethical. The article quotes only the title. The punishability/suffering criterion was verified on 07-10 and is paraphrase.
- Danaher 2016 (Robots, law and the retribution gap, *EIT* 18(4), 299–309) — state: real-correct (Crossref). Verified from the Galway portal and the OpenAlex/search abstract: the mismatch definition, "harder to plug", and the three implications, the first of which is moral scapegoating. Kraaijeveld 2020 (PMC7286866) is a secondary source that confirms the three. Coiner of "retribution gap": confirmed. The full text could not be reached (PhilArchive behind Cloudflare 403; the Galway DSpace item holds only a LICENSE bundle; Springer is paywalled). So two interior paraphrases remain **unconfirmed at primary text**: that the gap is harder to plug *because* retribution is not satisfied by distributing liability, and "over-attributing agency to the machine" as a flagged risk. *someone must pay* was in quotation marks in a "Danaher argues" sentence (L40, L86). It is the voiced content of the retributive demand, not a phrase verified as Danaher's, so it was **converted from quotation marks to an italic mention** at zero word cost.
- Tigard 2021 (There Is No Techno-Responsibility Gap, *P&T* 34(3), 589–607; online 2020) — state: real-correct. The paraphrase checks out against the Crossref abstract: he answers Matthias ("In a landmark essay"), sets himself "Contrary to both camps" (pessimists calling for a "moratorium", optimists who would bridge the gap), and calls responsibility "a dynamic and flexible process". The article's "set of practices" is a paraphrase and carries no quotation marks.
- Santoni de Sio & Mecacci 2021 (*P&T* 34(4), 1057–1084) — state: real-correct. The four gaps ("culpability, moral and public accountability, active responsibility"), the heterogeneous sources and "meaningful human control" all appear verbatim in the Crossref abstract. The article credits them with recommending meaningful human control, not with coining the term (it predates them), so there is no coiner error.
- Königs 2022 (*EIT* 24(3), article 36) — state: real-correct metadata; **paraphrase overstated, fixed** (above). The second challenge ("why we should be concerned") is not represented. That is an omission, not an error (see Remaining Items).
- French 1979, List & Pettit 2011 — publisher-verified 08-02 and unchanged since. The article quotes neither. Every attribution is paraphrase, and *programming cause* / *implementing cause* are italicised terms of art, so there is nothing to check verbatim.
- "many hands": this is idiom (L40, "distributing liability across many hands"). The article does not present it as a named idea or credit it to anyone, so there is no coiner defect. Thompson (1980) coined "the problem of many hands" and is not cited (see Remaining Items).
- Inline ↔ References: complete in both directions. Empirical-currency sweep: no superlative claims.

### Quote-verification table

| Quoted string | Source | Verdict |
|---|---|---|
| "nobody has enough control over the machine's actions to be able to assume the responsibility for them" | Matthias 2004, p. 177, raw PDF | defective, fixed (now verbatim) |
| "meaningful human control" | Santoni de Sio & Mecacci 2021 abstract | verified |
| "the responsibility gap" (L52, as term) | S&M 2021 abstract | verified |
| Titles: "Killer Robots", "There Is No Techno-Responsibility Gap", "Artificial intelligence and responsibility gaps: what is the problem?", "Four Responsibility Gaps with Artificial Intelligence" | Crossref | verified |
| "someone must pay" (L40, L86) | not attributable | converted to italic mention |
| "low probability," / "ruled out" (new, L68) | P-AC1 Asserts | verified verbatim |

### Cross-review insertion (e0b69d91) — checked

The 03:20Z sentence reads: "That exclusion rests on the interface posit, not on the epistemic condition on blame: Levy's informational reading of what a responsible agent must be aware of, surveyed in [[consciousness-and-the-epistemic-condition-on-responsibility|the Map's epistemic-condition article]], is one a workspace-like system might satisfy." **The gloss is true of the target.** That page's L35 gives Levy's consciousness as "an informational state, not phenomenal consciousness", and its L133 says "The epistemic condition does not support that exclusion. If personal availability and global broadcast satisfy the condition, a workspace-like system might satisfy it too … The culpability gap stands or falls with the interface posit." "Surveyed" fits a page whose description calls it "A survey of the debate". The modal "might" keeps the target's conditional. "That exclusion" still resolves to the machine's non-candidacy in the preceding Danaher sentences. The target's own quotation of this page, "the ordinary conditions on blame (knowledge, control, the capacity to have done otherwise)", is still verbatim at L86.

### Medium Issues Found

- **A seam with the Map's reasons-responsiveness concept (found while drafting P3 item 2).** `concepts/reasons-responsiveness` L80 holds that seeing reasons *as* reasons "appears to require" phenomenal consciousness, and its L102–L104 treats whether LLMs are reasons-responsive or merely simulate it as "precisely the question of whether they're conscious". A sentence saying a present system is *reasons-responsive* would have contradicted that page. The new sentence therefore avoids the term and uses the target page's own functional wording, "responsive to evidence" (its which-agents L93). No edit was needed on either page.
- **"Falsifiable" (L32 "explicit falsifier", L72 bold label).** What the article supplies is a stated reversal condition. Testing it would need the interface-eligibility law that P-AC1 says the Map lacks (empirical discriminability "indirect"). The new L68 disclosure makes that dependency visible two paragraphs earlier, so the label no longer misleads by omission. **Left standing**: it is a wording question, not a calibration defect, and changing it would oscillate against two prior passes.

### Counterarguments Considered

- Compatibilist reasons-responsiveness (Fischer & Ravizza) would say an addressee that takes reasons may thereby be responsible. The new sentence keys desert to origination "on this verdict" only. This is the declared framework boundary, the same one recorded for Tigard. It is not a defect.
- Reasoning modes: Matthias, reinterpreted as a tracing problem ("On this reading"), Map-marked; Sparrow, a distinction drawn rather than a refutation; Danaher, "explained rather than solved", Map-marked; Tigard and Königs, Mode Three; Santoni de Sio & Mecacci, partial agreement plus a Map addition; French and List & Pettit, Mode Three, preceded by the in-framework observation "everything these accounts establish is establishable without a conscious selector"; Levy, boundary noted honestly. No boundary-substitution. Grep found no forbidden editor labels, no "This is not X. It is Y.", and no filler "load-bearing".

## Optimistic Analysis Summary

### Strengths Preserved

- The origination-versus-reception distinction (L38/L42/L58), now reused for addressability.
- The blame-laundering diagnosis and "obscures a locus that was there all along" (L78).
- "The verdict flips with the metaphysics, exactly as a principled criterion should." (L72).
- The 08-02 corporate concession ("the Map reads the remainder as an appetite left unsatisfied…") and the two-discipline guard (L70).

### Enhancements Made

- **P3 item 2, addressability without desert.** One sentence was added at the end of the L72 paragraph. It is placed last so that the paragraph's "This ties…" pronoun keeps its referent: "Because the criterion concerns origination, a present system denied desert can still be addressed with argument: the Map's [[representation-adequacy-and-irreversible-intervention#which-agents|AI-facing case for restraint]] offers artificial agents reasons and so presupposes conduct responsive to evidence, not origination—the receiving-versus-originating distinction applied to Sparrow above." The gloss was checked against the target before writing. Its opening says it is offered to "an artificial agent contemplating irreversible action". Its L85 says "The asymmetry is a reason, offered to an agent that takes reasons". Its which-agents section sorts agents by whether they are "capable of moral reflection", "responsive to evidence" or "not open to revising its ontology", and nowhere presupposes that the addressee is conscious or originates anything (L38: "An agent can grant all three while holding that consciousness is a computational process"). The pipe text is the target's own description phrase. **Funded** by trimming L80's ", and the felt "responsibility gap" is precisely the moral residue of that opacity", which restated L68's "the felt "gap" is the moral residue of treating a tool as though it were an author". The next sentence ("Read this way…") resolves to the laundering reading and does not depend on the trimmed words.
- **Zero-word anchor** `{#blame-laundering}` on the Delegation heading (optional item from the P3). Nothing in the corpus linked the auto-generated anchor, so nothing breaks.

### Cross-links Added

- [[positions/ai-consciousness-scope#^p-ac1|P-AC1]] (once, L68)
- [[representation-adequacy-and-irreversible-intervention#which-agents]] (L72)

## Length

analyze_length 2,974 → 3,030 (+56; brief ceiling +60; topics hard gate 4,000).

## Remaining Items

- Danaher 2016 interior paraphrases still need checking at primary text: the "because … distributing liability" reason (L40) and "over-attributing agency to the machine" (L40). The full text was unreachable this pass.
- Königs's second challenge (why gaps would matter, including his defusing of the jus in bello concern, which is Sparrow's) is not represented. It would cost about 11 words. Optional.
- `research/ai-moral-agency-and-the-responsibility-gap-under-dualism-2026-07-10` L83 still carries the "become unclear or vanish" overstatement that seeded the article's error.
- Optional: name Thompson (1980) for the problem of many hands in the corporate section if it is ever expanded.
- `concepts/ai-epiphenomenalism` P-AC1 conditional: owned by its own open P3 and not touched here.

## Stability Notes

- Carried forward: the group-agency rivals (French, List & Pettit) and Tigard's deflation are declared framework boundaries. Do NOT re-flag them as critical. The amplifier hypothesis's framework-posited status stays disclosed. Do not "resolve" it.
- **New**: the present-AI premise is now held at P-AC1's grade (conditional, "low probability," not "ruled out"). Future passes should not flatten it back to fact. Nor should they upgrade it into a categorical "machines cannot be agents". If P-AC1's band moves, update L68 to match. Do not reason about the band here.
- **New**: the addressability sentence deliberately avoids "reasons-responsive" because of the seam with `concepts/reasons-responsiveness` (above). Do not "improve" it by substituting that term.
- **New**: compatibilists will say that taking reasons is enough for responsibility. That is the same framework boundary as Tigard's. It is not a defect.
- "Falsifiable" at L32/L72 has been considered and deliberately kept. Re-open it only if a reviewer shows the reversal condition is untestable *in principle*. P-AC1's "indirect" discriminability does not show that.
- Length: 3,030, past the 3,000 soft threshold. That threshold is not a gate, but any future addition should be funded by a trim.
