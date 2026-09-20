---
ai_contribution: 100
ai_generated_date: 2026-09-20
ai_modified: 2026-09-20 00:18:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-20
date: &id001 2026-09-20
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-20 00:18:00+00:00
modified: *id001
related_articles: []
title: 'Deep Review - Neuron-Less Animals: Sponges, Placozoans, and the Lower Bound
  of Cognition'
topics: []
---

**Date**: 2026-09-20
**Article**: [Neuron-Less Animals: Sponges, Placozoans, and the Lower Bound of Cognition](/topics/neuron-less-animals-sponges-placozoans-and-the-lower-bound-of-cognition/)
**Previous review**: [2026-08-03](/reviews/deep-review-2026-08-03-neuron-less-animals-sponges-placozoans-and-the-lower-bound-of-cognition/) (and 2026-07-19, 2026-07-08)
**Pass type**: SOURCE-FIDELITY, run against raw publisher text for every cite. The 08-03 pass ran a claim-has-no-cite lens and closed with "the body is otherwise converged"; this pass ran the orthogonal lens — *does each cited paper actually report what the sentence attributes to it?* — and found two attributions that three prior ledgers had certified as `real-correct` while checking only metadata. Both were confirmed against raw source text, not summaries.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Phantom co-author: "Leys and Anderson" (§The Sponge Floor, ×2; §The Sponge Floor closing paragraph, ×1; Reference [2]).** CRITICAL, fixed. Reference [2], DOI `10.1242/jeb.110817`, is **single-author Sally P. Leys**. Verified three independent ways: Crossref (`AUTHORS: Leys, Sally P.`), Europe PMC core record (PMID 25696821, `authorString: "Leys SP."`), and Semantic Scholar (`authors: [S. Leys]`). The review's own abstract is written in the first person singular — *"Here, **I** examine the elements of the sponge neural toolkit"* — which independently confirms it. P. A. V. Anderson is a real cnidarian neurobiologist but is not an author of this paper. The article named him three times in body prose and once in the reference entry.
  - **Fix applied**: "Leys and Anderson, reviewing… describe" → "Leys, reviewing… describes"; "Leys and Anderson read this as" → "Leys reads the sponge toolkit as"; "Leys and Anderson describe *elements*" → "Leys describes *elements*"; reference [2] author string corrected.
  - **Why three ledgers missed it**: a fabricated co-author is invisible to a DOI-resolves check. The 07-19 ledger recorded "11/11 real-correct, fully publisher-verified" and the 08-03 pass carried it forward unre-fetched. This is the metadata-ledger analogue of citation-ledger-ratifies-the-reading-not-just-the-metadata: the ledger certified that the paper *exists*, never that the author string matches it.
  - **Root cause traced**: the research note `research/neuron-less-animals-…-2026-07-08.md` carries the same phantom co-author at two loci, stamped **[VERIFIED — publisher]**. The error entered at research time and was inherited, not introduced in synthesis (the inverse of the 08-03 case). Both loci corrected in the note, with the correction dated in place so the note stays an honest record.

- **Misattributed headline finding: the post-synaptic parts-list is Sakarya 2007, not Srivastava 2010 (§The Parts-List Precedes the Machine).** CRITICAL, fixed. The article read: *"Srivastava and colleagues' draft genome … found a **nearly complete set of post-synaptic protein orthologues** — the parts-list for a synapse — in an animal that has no synapses [1]."* Verified against the raw Srivastava 2010 text (PMC3130542, NFKC-normalised, offsets 36720 / 37084 / 37523): the 2010 paper does **not** report this. It reports that *Amphimedon* "possesses homologues of bilaterian proteins involved in nervous system development …, pre- and post-synaptic organization (for example, synaptotagmin)" and then states the reverse-direction result the article omitted — **"Some key synaptic genes are conspicuously missing from *Amphimedon* …, including the ionotropic glutamate receptor family"**. Srivastava's own footnote 42 for the post-synaptic material is **Sakarya, O. et al. (2007), "A post-synaptic scaffold at the origin of the animal kingdom", *PLoS ONE* 2(6):e506**, whose abstract reads *"the genome of the demosponge Amphimedon queenslandica possesses a **nearly complete set of post-synaptic protein homologs**"* — a near-verbatim match to the article's wording, which fingerprints the true source exactly as the 08-03 Senatore case did.
  - **Fix applied**: the finding is reattributed to Sakarya and colleagues (new reference [19]); Srivastava [1] now carries the claim it does make — confirmation of the toolkit plus its bound, with the conspicuously-missing iGluR family quoted. Net effect is a *strengthening*: the parts-list is demonstrably incomplete, which is a sharper version of the section's own thesis than the flat "nearly complete" claim was.
  - **Not propagated**: the same wording appears at [apex/competency-without-felt-experience.md](/apex/competency-without-felt-experience/) L75, but there it is unattributed ("The demosponge genome carries a nearly complete set of post-synaptic protein orthologues"), which is *true* of Sakarya's finding. No defect; left alone.

- **False universal: "rather than action potentials" (§The Sponge Floor).** CRITICAL, fixed. The article generalised across Porifera: *"Conduction is tissue-based: slow, epithelial, driven by metabotropic cascades rather than action potentials."* Glass sponges falsify the universal. Verified at Europe PMC: **Leys, Mackie & Meech (1999), "Impulse conduction in a sponge", *J. Exp. Biol.* 202(9):1139–1150** — *"All-or-none propagated electrical impulses were recorded from the hexactinellid sponge Rhabdocalyptus dawsoni"*, propagating at **0.27 ± 0.1 cm s⁻¹**, calcium-dependent (blocked by Co²⁺, Mn²⁺, nimodipine; Na⁺-deficient solutions had little effect), conducted by the syncytial trabecular reticulum, with the feeding current arrested after each impulse. Same first author as the review the article cites for the generalisation, so this is not an obscure exception.
  - **Fix applied**: the claim is scoped to demosponges, and the hexactinellid case is added with its measured figures and new reference [18]. This too strengthens the article — electrical impulse conduction in an animal with no nerve cells is a better instance of "competence without neural substrate" than the false universal was.
  - **Consequent fix**: the section heading "The Sponge Floor: Coordination Without Conduction" was now self-contradictory and became "…Coordination Without a Nervous System". Checked for inbound anchors in both dialects (corpus-uses-two-anchor-dialects-so-a-slug-check-false-zeros) — `sponge-floor` and `Coordination Without Conduction` both return zero referrers outside the file and its Hugo mirror, so the rename breaks nothing.

### Medium Issues Found

- **Wong 2019 overstated, and in the article's own disfavour (§The Parts-List Precedes the Machine).** Fixed. The article said the synaptic genes "are even *co-expressed* in coordinated modules". The paper's abstract reports only *partial* co-regulation — vesicle trafficking, calcium regulation and post-synaptic receptor scaffolding co-expressed in adult choanocytes and during metamorphosis — and its headline negative is the opposite of "even": *"total synaptic gene co-expression profiles do not support the existence of a functional synapse in A. queenslandica"*. Rewritten to carry both halves; the negative result is direct support for the section's "parts-list is not a machine" discipline.
- **Cell-count currency: "six cell types" against the article's own [15] (lead, §Placozoans).** Fixed. Najle et al. 2023, cited in the same article, opens *"these small disc-shaped animals not only have **nine** morphologically described cell types and no neurons"*. The lead now reads "nine morphological cell types"; the §Placozoans sentence keeps six but marks it as the count of the day ("an animal then credited with six cell types"), which is what Varoqueaux 2018 was working from.
- **Smith 2015 sequence inverted (§Placozoans).** Fixed. The article had the animal pausing *after* lipophil secretion; the paper's order is cilia stop → lipophils "simultaneously" secrete → "the animal pauses while the algal content is ingested, and then resumes gliding". "Simultaneously" in the paper modifies the ciliary arrest, not the lipophils with respect to one another.
- **Smith 2019 mechanism misdescribed (§Placozoans).** Fixed. "Emerges from local cilia coordination plus chemical cues" inverts the model's claim: the cells are *not* coordinated with one another. The paper models "ciliated epithelial cells, each independently sensing and responding to a chemoattractant gradient" and concludes an animal "can move coherently in search of food **without any need for chemical signaling between cells**". Also added the experimental half of the paper the article omitted (*Trichoplax* demonstrably chemotaxes toward algae in agar). The corrected version is the stronger statement of the article's own point.
- **Varoqueaux 2018 dropped list member.** Fixed. Three behavioural types are "(1) crinkling, (2) turning, and (3) flattening **and churning**" — the article had truncated type 3 to "flattening". Also restored "eleven different peptides" and "neuropeptide-like molecules" (the paper's own hedge) and "three layers".

### Counterarguments Considered

- **Bechtel & Bich "eating is cognition"** — bedrock, per three prior stability notes. NOT re-flagged. Abstract re-verified this pass via Crossref JATS: *"it constitutes a cognitive activity"*, *"cognition is fundamentally grounded in chemical signaling and processing"*, cases = Porifera and Placozoa. The article's statement of their position is accurate and stated at full strength.
- **Adding hexactinellid action potentials does not concede a nervous system.** The conducting tissue is a syncytium, not neurons; the addition widens the range of non-neural competence rather than narrowing the article's claim.

### Web-verify ledger (§2.4)

Every inline cite re-verified this pass against Crossref and Europe PMC core records, and — where the claim was a paraphrase of a *result* rather than a metadata fact — against raw full text (Europe PMC `fullTextXML` or PMC HTML, NFKC-normalised, tag-stripped, offsets recorded).

- Srivastava et al. 2010 (*Amphimedon queenslandica* genome) — *Nature* 466(7307):720–726. state: **real-correct (metadata) + claim reassigned** (see critical issue 2). Full text read at PMC3130542.
- Leys 2015 (Elements of a 'nervous system' in sponges) — *J. Exp. Biol.* 218(4):581–591. state: **real-wrong-metadata (was "Leys, S. P. & Anderson, P. A. V.", corrected to "Leys, S. P.")**. Publisher full text is behind Cloudflare (403 on both `jeb.biologists.org` PDF and `journals.biologists.com` article page; per webfetch-survives-websearch-exhaustion a 403 is not an absence) — author string and abstract verified at three independent registries instead; the claims drawn from it ("elements", no true nervous system, early specialisation for suspension feeding rather than a lost neural system) are all verbatim-traceable to the publisher abstract.
- Kornder et al. 2022 (Sponges sneeze mucus…) — *Curr. Biol.* 32(17):3855–3861.e3. state: **real-correct + page range completed** (article previously gave volume only). Claim check at PMC9473484: "against the direction of its internal water flow", "from its seawater inlet pores (ostia)" — verbatim; **"tens of minutes" verified at offset 6059**: "waves of coordinated contractions … **for 20–50 min** (n = 16)", recurring "each 3–8 h". The article's "not explained by the paracrine chemistry so far characterised" is also supported: the paper's own highlight reads "Mucus travels too slowly for known ciliary transport, suggesting a novel mechanism" and its conclusion "It is unclear how the movement of mucus … is achieved". `find_superlative_claims` flagged the "so far" here; checked against the 2025 literature and it still holds. state: **not superseded**.
- Ho, Goss & Leys 2025 (ATP and glutamate coordinate contractions) — *J. Exp. Biol.* 228(3):JEB248010. state: **real-correct**. Full text PMC11883242: "sneeze" appears 34 times for *E. muelleri* ("We follow previous researchers in referring to this as a 'sneeze'", offset 16604), so the article's use of the term for this paper is the paper's own. Added the verified downstream relation: "PPADS prevented both glutamate- and ATP-triggered contractions, suggesting that ATP works downstream of glutamate."
- Varoqueaux et al. 2018 — *Curr. Biol.* 28(21):3495–3501.e2. state: **real-correct + paraphrase corrected** (dropped "and churning"; see medium issues).
- Smith, Pivovarova & Reese 2015 — *PLoS ONE* 10(9):e0136098. state: **real-correct + sequence corrected**.
- Smith, Reese, Govezensky & Barrio 2019 — *PNAS* 116(18):8901–8908. state: **real-correct + mechanism corrected**.
- Bechtel & Bich 2024 — *Biological Theory*, doi 10.1007/s13752-024-00464-6 (online-first; no volume/pages assigned, so the article's entry is complete as it stands). state: **real-correct**; abstract verified via Crossref JATS.
- Keijzer, van Duijn & Lyon 2013 — *Adaptive Behavior* 21(2):67–85. state: **real-correct**. Abstract via Crossref JATS confirms the skin-brain paraphrase: "early nervous systems evolved to organize a new multicellular effector: muscle tissue" and "this input–output interpretation is not the most fundamental feature".
- Wong et al. 2019 — *Sci. Rep.* 9:15781. state: **real-correct + claim scoped** (see medium issues).
- Jin et al. 2024 — *Nat. Commun.* 15:8626. state: **real-correct**; "regulate its negative taxis behavior" re-confirmed verbatim in the abstract.
- Senatore, Reese & Smith 2017 — *J. Exp. Biol.* 220(18):3381–3390. state: **real-correct**; the showed/proposed split installed on 08-03 re-checked against the abstract and preserved unchanged per that pass's stability note.
- Najle et al. 2023 — *Cell* 186(21):4676–4693.e29. state: **real-correct**. Abstract supports "pre-synaptic scaffold", "progenitor cells with neurogenesis signatures", and "earlier-branching animals like sponges and ctenophores lacked this conserved expression". Its "nine morphologically described cell types" is what drove the cell-count fix above.
- Sachkova, Modepalli & Kittelmann 2025 — *Annu. Rev. Neurosci.* 48(1):311–329. state: **real-correct (metadata)**; **content paraphrase unverified** — the record is OA-hybrid but Unpaywall lists no retrievable PDF and there is no PMC deposit, so the two claims drawn from it (ctenophore-sister implies neurons lost in sponges or evolved twice; placozoan peptidergic cells read as non-neuronal secretory cells closely related to neuronal ones) could not be checked against full text. Both are consistent with the publisher abstract ("neuron-like cells in nerveless placozoans, sponges … may prompt a redefinition of what constitutes a neuron"), and the "secondarily neuron-less" alternative is independently attested in Leys 2015's abstract ("or represents the remnants of a more complex signalling system and sponges have lost cell types"). Left in place; flagged here so a future pass with publisher access can close it rather than re-litigate it.
- Nikitin et al. 2023 — *Front. Neurosci.* 17:1125624. state: **real-correct**. Full text PMC10133484: glutamate/glycine/GABA/ATP directions verbatim in the abstract; "volume transmission" appears 7 times (first at offset 4085), so the article's volume-transmission framing is the paper's own.
- **New**: Leys, Mackie & Meech 1999 — *J. Exp. Biol.* 202(9):1139–1150, doi 10.1242/jeb.202.9.1139. state: **real-correct**, Crossref + Europe PMC; all figures in the new sentence taken from the abstract.
- **New**: Sakarya et al. 2007 — *PLoS ONE* 2(6):e506, doi 10.1371/journal.pone.0000506, PMID 17551586. state: **real-correct**, full nine-author string matched character-for-character against Crossref (`Onur Sakarya; Kathryn A. Armstrong; Maja Adamska; Marcin Adamski; I-Fan Wang; Bruce Tidor; Bernard M. Degnan; Todd H. Oakley; Kenneth S. Kosik`).
- Inline ↔ References cross-check re-run after the additions: inline markers `[1]`–`[12]`, `[15]`–`[19]` all resolve; `[13]`/`[14]` remain the uncited Map self-cites retained per site convention. No renumbering was needed — the new entries were appended as 18 and 19, since the list has never been in citation order.

## Optimistic Analysis Summary

### Strengths Preserved

- The Tenet 5 close ("no purchase on the question either way") and the lead's scoped quantifier — untouched, as the 07-08 and 08-03 stability notes require.
- The Tenet 2 scoping paragraph (minimality is a constraint on *magnitude*, not a parsimony heuristic about distribution) — untouched, and re-checked against `tenets#^minimal-quantum-interaction`. No possibility/probability slippage found anywhere in the article: every Map-favouring move is marked framework-relative.
- The W32-installed honesty passage ("The account is not yet a closed one, and the sources say so") — preserved verbatim; `git log -S` traces it to commit `af048b53df`, a review-driven refine, so it is not redundancy to trim.
- The Senatore showed/proposed split from 08-03 — preserved verbatim.

### Enhancements Made

Every fix in this pass was a correction that also strengthened the argument, which is the pattern to expect when an article's paraphrases have drifted *toward* the headline claim of each source: the incomplete parts-list, the absent functional synapse, and the independently-acting cilia are all better evidence for "toolkit presence is not functional presence, and functional presence is not experience" than the overstatements they replace. The one genuinely new datum — hexactinellid action potentials — extends the floor rather than raising it.

### Cross-links Added

None. All nine existing wikilink targets re-verified as live.

## Remaining Items

- Sachkova et al. 2025 content paraphrase remains unverified against full text (publisher-gated; see ledger). Not a flagged defect — an open verification, to be closed opportunistically.

## Stability Notes

- **Ledger-carry-forward is now a known failure mode for this article.** Three passes certified reference [2] as `real-correct` while carrying a fabricated co-author, because each re-checked only that the DOI resolved. A future pass should re-read the *author string* against a registry at least once whenever it touches the References block, and should treat "verified in a prior ledger" as covering metadata that was actually printed, not metadata that was assumed.
- **Do not reattribute the post-synaptic parts-list back to Srivastava 2010.** The finding is Sakarya et al. 2007 [19]; Srivastava [1] is the *bounding* cite and its "conspicuously missing" quote is verified verbatim in the paper's text.
- **Do not re-broaden "In demosponges, conduction is tissue-based…" to all sponges.** The hexactinellid exception is real and measured; the scoping is deliberate.
- **Do not collapse the Wong sentence back to "even co-expressed".** The paper's negative result (no support for a functional synapse) is the half that does the work in that section.
- **"Six cell types" is not simply wrong** — it is the count Varoqueaux 2018 worked from, which is why §Placozoans keeps it with a date-marker while the lead carries the current nine. Do not harmonise them to one number.
- **Bechtel & Bich remains bedrock.** Fourth pass, still not a defect.
- **Length margin is now thin**: 2757 → 2986 words against a 3000 soft threshold. A future pass adding anything substantive should operate length-neutral.