---
ai_contribution: 100
ai_generated_date: 2026-09-16
ai_modified: 2026-09-16 22:45:00+00:00
ai_system: claude-fable-5-1
author: null
concepts:
- '[[local-tomography-and-the-consciousness-physics-interface]]'
created: 2026-09-16
date: &id001 2026-09-16
description: 'Status check on Hoffreumon and Woods 2026 and the real-quantum falsification
  dispute: preprint only, replied to by the Renou group, and now reducible to a dispute
  about local tomography itself.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-09-16 22:45:00+00:00
modified: *id001
related_articles: []
title: Research Notes - The Operational-Independence Challenge to the Real-Quantum
  Falsification
topics: []
---

# Research: The Operational-Independence Challenge to the Real-Quantum Falsification

**Date**: 2026-09-16 (task generated 2026-08-16)
**Verdict**: Worth a research pass, **not** a new article. Everything below discharges as a refine of [local-tomography-and-the-consciousness-physics-interface](/concepts/local-tomography-and-the-consciousness-physics-interface/) plus reference entries. Zero cap cost.
**Indexes that answered**: arXiv abs pages and HTML full texts (curl, raw); Crossref (all journal records); Semantic Scholar `citations` endpoint (answered; the paper-record endpoint returned 429 twice); OpenAlex budget-exhausted (429, resets midnight UTC); Europe PMC not tried (quant-ph preprints are out of scope for it).
**Search queries used**: "Hoffreumon Woods arXiv real quantum theory Renou falsification independence assumption"; "physics.aps.org Viewpoint real numbers quantum theory Renou Chen Li 2022 Physics 15"; "Hoffreumon Woods reply fermionic real quantum theory 2026 response to comment Moradi Kalarde Renou"; arXiv author search "Hoffreumon".

## Executive Summary

Hoffreumon and Woods (arXiv:2603.19208) is still a version-1 preprint with no journal record, but it is no longer the last word. The Renou group replied within three weeks (Moradi Kalarde, Xu and Renou, arXiv:2604.07425, 8 Apr 2026) with a Comment arguing that the one postulate Hoffreumon and Woods use to select their real theory (independent preparation = operational independence) fails in fermionic information theory, and, in an appendix directly relevant to the Map, that inside the GPT framework that postulate is *equivalent to local tomography*. Both camps now agree on the shape of the result: the 2021 falsification rules out real quantum theory *with the Kronecker (tensor-product) composition rule*, and there exist real formulations (Barrios Hita et al., *PRL* 136, 240202, June 2026, peer-reviewed; Hoffreumon-Woods; Maioli et al.) that reproduce every prediction of complex quantum theory. The disagreement is whether the tensor-product restriction is physically motivated. Renou et al. 2021 themselves conceded that refuting real quantum physics requires "plausible, yet unverifiable, assumptions about the form of the quantum states", so the Map's article slightly over-credits Hoffreumon and Woods with discovering the assumption. The harvest's second complaint (uncited 2022 realisations) was discharged on 2026-08-18 by a deep review that added Chen and Li as references 4 and 5; the metadata are re-verified below at Crossref.

## What the Article Currently Says (verbatim, `obsidian/concepts/local-tomography-and-the-consciousness-physics-interface.md`)

Line 56 (Renou and the realisations):

> The test was realised in 2022 on a superconducting processor (Chen et al. 2022) and on an optical network (Li et al. 2022), each reporting violation of the real-quantum bound.

Line 58 (the whole Hoffreumon-Woods paragraph):

> The result is not settled, and the Map must not present it as such. Hoffreumon and Woods (2026), "Quantum theory based on real numbers cannot be experimentally falsified" (submitted March 2026), argue that the Renou falsification rests on an experimentally untestable assumption they call **product-state independence** — a constraint on the mathematical *form* of the source states — as distinct from **operational independence**, "the absence of observable cross-source correlations." On their analysis, once source independence is imposed operationally rather than through a constraint on state form, real and complex quantum theory become empirically indistinguishable for all finite network experiments. The dispute is live and unresolved as of 2026.

References 3-6 (lines 114-117) already carry Renou 2021, Chen 2022, Li 2022 and Hoffreumon-Woods 2026. `git log -S'PhysRevLett.128.040403'` shows refs 4 and 5 were added in commit `bf31825ed9` (2026-08-18, deep-review), two days after the harvest that flagged their absence. The harvest premise was true when written and is now discharged.

Fidelity check: the article's quotation "the absence of observable cross-source correlations" is verbatim in the Hoffreumon-Woods abstract; its Renou quotation "real and complex quantum theory make different predictions in network scenarios comprising independent states and measurements" is verbatim in arXiv:2101.10873. No quote-fidelity defect.

## Hoffreumon and Woods: Status

- **arXiv:2603.19208**, "Quantum theory based on real numbers cannot be experimentally falsified", Timothée Hoffreumon and Mischa P. Woods. **v1 only, submitted 19 Mar 2026** (abs page submission history shows a single version). Comments field: "60 pages (7 main, 10 technical material, 43 appendices), 5 figures". No journal-ref on arXiv; DOI cell is the DataCite arXiv DOI only. Crossref title-plus-author search returns only Hoffreumon's two *Quantum* papers with Oreshkov (2021, 2026) — **no journal version exists** as of 2026-09-16.
- **Predecessor**: arXiv:2504.02808, "Quantum theory does not need complex numbers", same authors, v1 3 Apr 2025, v2 9 Oct 2025, no journal-ref. This is where "representation locality" comes from (the phrase the July research note attributed to the 2026 paper); the 2026 paper cites it 19 times for its technical core.
- **No reply from Hoffreumon and Woods to the Comment** as of 2026-09-16: arXiv author search lists their only later item as arXiv:2602.23865 "Supermaps on generalised theories" (June 2026), unrelated.
- **Precise definitions (raw HTML full text)**: product-state independence is the requirement that a two-source state be of the form Ψ_XY = ρ_X ⊗_K ρ_Y for arbitrary ρ_X, ρ_Y, with ⊗_K the Kronecker product: "We call this product-state independence. But this is not itself something the parties directly observe." Operational independence: "a bipartite state Ψ_XY is operationally independent when, for every pair of local POVMs ... the joint probability distributions of the outcomes ... p(α, β) = p(α) p(β)." Their reading of Renou: "Their analysis assumes that independent sources in RQT must be represented by real product states, in direct analogy with QT. But once operational independence and product-state independence are recognised as distinct in RQT, that restriction is no longer compulsory. It is an additional modelling assumption, stronger than what is experimentally warranted."
- **What they say the experiments show**: "The only conclusion that can be drawn from the experimental data Li et al. (2022); Lancaster and Palladino (2025), therefore, is that the RQT description of the state in which the system started the experiment was not a product state." They cite Li et al. 2022 and Lancaster and Palladino 2025; they do **not** cite Chen et al. 2022 ("Ruling out" has zero hits in the full text).
- **They concede a prior near-result**: Remark A.21 says Weilenmann, Gisin and Sekatski (2025) "present a proposition that appears similar to proposition 8", differing in that it "externalises the phase-encoding subsystems" as a shared resource rather than treating them as "entanglement of representation" internal to independent sources.

## Do Renou et al. and the Experiments Acknowledge the Assumption?

Yes, all three, in different registers (pdftotext, NFKC-normalised, grepped):

- **Renou et al. 2021** (arXiv:2101.10873): postulate (iv) states that "the state representing two independent preparations of the two systems is the tensor product of the two preparations. This last postulate plays a key role in our discussions". Their experimental-assumptions section goes further than the Map's article lets on: "In order to refute real quantum physics, we are thus compelled to accept some plausible, yet unverifiable, assumptions about the form of the quantum states distributed to the three parties." So "unverifiable assumption about state form" is Renou's own phrase, not a Hoffreumon-Woods discovery. What Hoffreumon and Woods add is the claim that dropping it costs nothing operationally, i.e. that a real theory exists which satisfies operational independence and reproduces every finite-network correlation.
- **Chen et al. 2022** (arXiv:2103.08123): "An assumption used in the proposal [15] is that the composite quantum state produced by two independent sources is the tensor product of the two independent quantum states, which has been ensured by the second axiom of standard quantum theory."
- **Li et al. 2022** (arXiv:2111.15128): "in the rest of this paper, real quantum theory refers to a theory in which the real Hilbert spaces of independent systems are combined by the tensor product."

## Replies, Citing Papers and the Wider 2025-2026 Exchange

Semantic Scholar lists six citing works for arXiv:2603.19208; the relevant ones, plus the peer-reviewed items that frame them:

| Date | Work | Status | What it does |
|---|---|---|---|
| 29 Oct 2025 | Weilenmann, Gisin & Sekatski, "Partial Independence Suffices to Rule Out Real Quantum Theory Experimentally", *PRL* 135, 180201, doi:10.1103/3fv7-p8cs | Peer-reviewed | Renou-camp result predating H&W; weakens the independence needed for the falsification. H&W's Remark A.21 concedes a similar proposition. |
| 19 Mar 2026 | Hoffreumon & Woods, arXiv:2603.19208 | Preprint v1 | The challenge the Map cites. |
| 8 Apr 2026 | Moradi Kalarde, Xu & Renou, "Comment on 'Quantum theory based on real numbers cannot be experimentally falsified': On the compatibility of physical principles with information theory for fermions", arXiv:2604.07425 | Preprint v1 | Distinguishes T1^R (Kronecker real theory; "It was shown in [18] that T1^R is experimentally falsifiable") from T2^R (operationally equivalent to standard QIT, traced to Stueckelberg). H&W's Postulate 1 ("independent preparation should coincide with operational independence") "fails in FIT, hence is not a general physical postulate". Appendix C: "within the GPT framework, local tomography is equivalent to the identification of operational and preparation independence (Props. 1 and 2). Since several physically motivated theories, including FIT, are not locally tomographic, this further indicates that Postulate 1 is not expected to hold beyond this setting." |
| 21 Apr 2026 (v3 23 Jun) | Maioli, Curado & Gazeau, "Quantum mechanics over real numbers fully reproduces standard quantum theory", arXiv:2604.19482 | Preprint v3 | Kähler-space real framework with a symplectic composition rule replacing the Kronecker product; claims the no-go is "specific to a particular real representation". |
| 18 Jun 2026 | Barrios Hita, Trushechkin, Kampermann, Epping & Bruß, "Quantum Mechanics Based on Real Numbers: A Consistent Description", *PRL* 136, 240202, doi:10.1103/4k13-sdjh (arXiv:2503.17307, v1 21 Mar 2025) | **Peer-reviewed** | "a physically motivated postulate about composite quantum systems allows us to construct quantum mechanics based on real numbers that reproduces predictions for all multipartite quantum experiments. Thus, we argue that real-valued quantum mechanics cannot be falsified". H&W acknowledge conversations with Barrios Hita and cite this work. |
| 18 Jun 2026 | Moradi-Kalarde & Renou, "A New Perspective on Real-Valued Quantum Theory", *Physics* 19, 85, doi:10.1103/Physics.19.85 | APS Viewpoint on the Barrios Hita PRL | Renou's own framing of the state of play: the 2021 result "showed that more-general experiments involving independent systems cannot be reproduced by any real-valued formulation that preserves the standard tensor-product structure"; open question whether the new compositional principle "can be consistently formulated" for indistinguishable particles. **Does not mention Hoffreumon or Woods.** |
| 7 Jul 2026 | Bang, Cho & Baek, "Hidden Complex Structure in Quotient-Space Real Quantum Mechanics", arXiv:2607.05865 | Preprint v1 | Argues the Barrios Hita construction "is best understood as standard complex quantum mechanics written in real notation"; "in multipartite network scenarios, this changes the meaning of source independence". |
| 4 Sep 2026 | Kam, "Restricting the effects hides a nonphysical symmetry from every causal structure", arXiv:2609.05322 | Preprint v2 | Cites H&W; argues what sustains the measured separation "is the absence of a restriction rather than any feature of conjugation". |

Two Semantic Scholar entries (Biswas et al., *PRA* 2026; Morelli et al., *Quantum* 2026) cite H&W only in passing and are not about the dispute.

**Where the dispute now sits.** Both camps accept: (a) the Kronecker-product real theory (Renou's RQT, the Comment's T1^R) is experimentally falsified, and the 2022 experiments (plus Lancaster and Palladino 2025 on IBM hardware, *Am. J. Phys.* 93(1), 110-120, doi:10.1119/5.0225728) stand as tests of *that* theory; (b) real formulations with a non-Kronecker composition rule reproduce all of complex quantum theory. The open question is whether any postulate singles out the Kronecker rule as the physical meaning of "independent sources". The Comment's answer is that H&W's alternative postulate is local tomography under another name, and local tomography fails for fermions. Nobody has refereed H&W; nobody has refuted the mathematics; the Renou side has attacked the physical motivation. Dispute status: **open, but reframed** since the article's July 2026 snapshot.

## Verified Metadata for the Reference Apparatus (Crossref, 2026-09-16)

- Renou, M.-O., Trillo, D., Weilenmann, M., Le, T. P., Tavakoli, A., Gisin, N., Acín, A. & Navascués, M. (2021). Quantum theory based on real numbers can be experimentally falsified. *Nature* 600(7890), 625-629. doi:10.1038/s41586-021-04160-4. Published 15 Dec 2021. (Article's ref 3 correct.)
- Chen, M.-C., Wang, C., Liu, F.-M., Wang, J.-W., Ying, C., Shang, Z.-X., Wu, Y., Gong, M., Deng, H., Liang, F.-T., Zhang, Q., Peng, C.-Z., Zhu, X., Cabello, A., Lu, C.-Y. & Pan, J.-W. (2022). Ruling Out Real-Valued Standard Formalism of Quantum Theory. *Physical Review Letters* 128(4), 040403. doi:10.1103/PhysRevLett.128.040403. Published 24 Jan 2022. (Article's ref 4 correct.)
- Li, Z.-D., Mao, Y.-L., Weilenmann, M., Tavakoli, A., Chen, H., Feng, L., Yang, S.-J., Renou, M.-O., Trillo, D., Le, T. P., Gisin, N., Acín, A., Navascués, M., Wang, Z. & Fan, J. (2022). Testing Real Quantum Theory in an Optical Quantum Network. *Physical Review Letters* 128(4), 040402. doi:10.1103/PhysRevLett.128.040402. Published 24 Jan 2022. (Article's ref 5 correct.)
- Avella, A. (2022). Quantum Mechanics Must Be Complex. *Physics* 15, 7. doi:10.1103/Physics.15.7. Published 24 Jan 2022. (The July research note listed this without an author; Crossref supplies Alessio Avella.)
- Weilenmann, M., Gisin, N. & Sekatski, P. (2025). Partial Independence Suffices to Rule Out Real Quantum Theory Experimentally. *Physical Review Letters* 135(18), 180201. doi:10.1103/3fv7-p8cs. Published 29 Oct 2025.
- Barrios Hita, P., Trushechkin, A., Kampermann, H., Epping, M. & Bruß, D. (2026). Quantum Mechanics Based on Real Numbers: A Consistent Description. *Physical Review Letters* 136(24), 240202. doi:10.1103/4k13-sdjh. Published 18 Jun 2026. arXiv:2503.17307.
- Moradi-Kalarde, F. & Renou, M.-O. (2026). A New Perspective on Real-Valued Quantum Theory. *Physics* 19, 85. doi:10.1103/Physics.19.85. Published 18 Jun 2026.
- Moradi Kalarde, F., Xu, X. & Renou, M.-O. (2026). Comment on "Quantum theory based on real numbers cannot be experimentally falsified": On the compatibility of physical principles with information theory for fermions. arXiv:2604.07425 (preprint, v1, 8 Apr 2026).
- Hoffreumon, T. & Woods, M. P. (2026). Quantum theory based on real numbers cannot be experimentally falsified. arXiv:2603.19208 (preprint, v1, 19 Mar 2026; no journal version). (Article's ref 6 correct as written.)
- Hoffreumon, T. & Woods, M. P. (2025). Quantum theory does not need complex numbers. arXiv:2504.02808 (preprint, v2, 9 Oct 2025).

Not verified at publisher and not recommended for the article: Lancaster & Palladino 2025 (Crossref record found, doi:10.1119/5.0225728, but the paper itself was not read); Lismer, Felefele, Spekkens & Resch, arXiv:2506.07775 (still v1, no journal-ref as of today; the purification note's suggestion stands on its own).

## Relation to Site Tenets

Tenet-neutral on Dualism and Bidirectional Interaction. The one point that bears on the Map's use of local tomography (Tenet 2's Born-rule constraint at the interface, via the GPT framework): the Comment's Appendix C makes the real-vs-complex dispute a dispute about whether local tomography is a general physical principle, and answers no, because fermionic information theory is not locally tomographic. That is a friendly datum for the article's "Is Local Tomography a Fact About Nature?" section, which currently treats the failure regimes as real and quaternionic quantum theory only; superselection-constrained fermionic theories are a third, physically instantiated failure regime, and the Renou group is the one citing it. No tenet conflict.

## Refine Brief (for a `refine-draft` task on the article; length-guarded)

Measured 2026-09-16 with `tools.curate.length.analyze_length`: 2860 body words, concepts soft 2500 / hard 3500 (the hard figure itself trips), status `soft_warning`, headroom to the hard trip 639 words. Net addition must stay under about 120 body words; the reference block also counts.

1. **Line 58, replace the final sentence** "The dispute is live and unresolved as of 2026." with, in substance: *The dispute is open but has moved. Renou et al. had themselves conceded that refuting real quantum physics requires "plausible, yet unverifiable, assumptions about the form of the quantum states"; what Hoffreumon and Woods add is a real theory that drops the assumption at no operational cost. The Renou group's reply (Moradi Kalarde, Xu and Renou 2026) attacks the replacement postulate rather than the mathematics: identifying independent preparation with operational independence is, within the GPT framework, equivalent to local tomography itself, and fails for fermionic information theory. Both sides now read the 2021 result as falsifying real quantum theory with the tensor-product composition rule, while peer-reviewed real reformulations with a different composition rule (Barrios Hita et al. 2026) reproduce every complex prediction.* Keep "preprint" for Hoffreumon-Woods; the Comment is also a preprint; Barrios Hita is peer-reviewed. Attribute "unverifiable assumptions ... form of the quantum states" to Renou et al., verbatim as quoted in this note.
2. **Line 58, optional one-clause tightening**: "argue that the Renou falsification rests on an experimentally untestable assumption they call product-state independence" is accurate but reads as if the assumption were newly discovered; "an assumption Renou et al. themselves flagged as unverifiable, which they call product-state independence" is the calibrated form.
3. **Line 56**: no change needed; the realisation claim is already cited to refs 4 and 5 with verified metadata. Optionally append "(Weilenmann, Gisin and Sekatski 2025 show partial independence suffices)" only if length permits; it is a peer-reviewed strengthening of the Renou side that the article lacks.
4. **References to add** (metadata above): Moradi Kalarde, Xu & Renou 2026 (arXiv:2604.07425); Barrios Hita et al. 2026 (*PRL* 136, 240202). Add Weilenmann, Gisin & Sekatski 2025 only if item 3's clause is used. Do not add the Avella viewpoint to the article (secondary; the primaries are already cited). Renumber nothing that is cross-referenced in prose (the article's in-text citations are author-year, so appending is safe).
5. **Calibration the article should adopt**: Hoffreumon-Woods is a preprint, unrefereed, replied to but not refuted, and superseded in framing by the June 2026 *PRL* and Viewpoint; the empirical section's claim that Renou is "an empirical probe of whether nature composes the way a locally-tomographic theory says" is *strengthened* by the Comment, since the Renou group now says the whole disagreement reduces to local tomography. Keep the "not settled" verdict; drop any implication that H&W alone raised the assumption.
6. **Do not** create a new article on real-vs-complex quantum theory; the Map's interest is confined to what the dispute says about local tomography, which is one paragraph.

## Gaps

- Hoffreumon-Woods full technical appendices (43 pages) were grepped, not read; the mathematics is taken on trust from both camps' agreement that it is not the point of contention.
- Lancaster & Palladino 2025 and Lismer et al. 2025 were metadata-checked only.
- OpenAlex could not be queried today (budget); Semantic Scholar's citation list may lag arXiv by weeks, so a citing paper after early September 2026 could be missing.
- The *Physics* 19, 85 Viewpoint was read through the WebFetch summariser (direct curl 403); the quoted sentences are as it returned them and should be re-grepped from the raw page before being placed in an article.

## Citations

1. Hoffreumon, T. & Woods, M. P. (2026). Quantum theory based on real numbers cannot be experimentally falsified. arXiv:2603.19208. https://arxiv.org/abs/2603.19208
2. Hoffreumon, T. & Woods, M. P. (2025). Quantum theory does not need complex numbers. arXiv:2504.02808. https://arxiv.org/abs/2504.02808
3. Moradi Kalarde, F., Xu, X. & Renou, M.-O. (2026). Comment on "Quantum theory based on real numbers cannot be experimentally falsified": On the compatibility of physical principles with information theory for fermions. arXiv:2604.07425. https://arxiv.org/abs/2604.07425
4. Renou, M.-O. et al. (2021). Quantum theory based on real numbers can be experimentally falsified. *Nature* 600, 625-629. doi:10.1038/s41586-021-04160-4. arXiv:2101.10873.
5. Chen, M.-C. et al. (2022). Ruling Out Real-Valued Standard Formalism of Quantum Theory. *Physical Review Letters* 128, 040403. doi:10.1103/PhysRevLett.128.040403. arXiv:2103.08123.
6. Li, Z.-D. et al. (2022). Testing Real Quantum Theory in an Optical Quantum Network. *Physical Review Letters* 128, 040402. doi:10.1103/PhysRevLett.128.040402. arXiv:2111.15128.
7. Avella, A. (2022). Quantum Mechanics Must Be Complex. *Physics* 15, 7. doi:10.1103/Physics.15.7. https://physics.aps.org/articles/v15/7
8. Weilenmann, M., Gisin, N. & Sekatski, P. (2025). Partial Independence Suffices to Rule Out Real Quantum Theory Experimentally. *Physical Review Letters* 135, 180201. doi:10.1103/3fv7-p8cs
9. Barrios Hita, P., Trushechkin, A., Kampermann, H., Epping, M. & Bruß, D. (2026). Quantum Mechanics Based on Real Numbers: A Consistent Description. *Physical Review Letters* 136, 240202. doi:10.1103/4k13-sdjh. arXiv:2503.17307.
10. Moradi-Kalarde, F. & Renou, M.-O. (2026). A New Perspective on Real-Valued Quantum Theory. *Physics* 19, 85. doi:10.1103/Physics.19.85. https://physics.aps.org/articles/v19/85
11. Maioli, A. C., Curado, E. M. F. & Gazeau, J.-P. (2026). Quantum mechanics over real numbers fully reproduces standard quantum theory. arXiv:2604.19482 (v3). https://arxiv.org/abs/2604.19482
12. Bang, J., Cho, K. & Baek, K. (2026). Hidden Complex Structure in Quotient-Space Real Quantum Mechanics. arXiv:2607.05865. https://arxiv.org/abs/2607.05865
13. Kam, C.-F. (2026). Restricting the effects hides a nonphysical symmetry from every causal structure. arXiv:2609.05322 (v2). https://arxiv.org/abs/2609.05322
14. Lancaster, J. L. & Palladino, N. M. (2025). Testing the necessity of complex numbers in traditional quantum theory with quantum computers. *American Journal of Physics* 93(1), 110-120. doi:10.1119/5.0225728
15. Lismer, T. S., Felefele, K. B., Spekkens, R. W. & Resch, K. J. (2025). Experimental Test of the Principle of Tomographic Locality. arXiv:2506.07775. https://arxiv.org/abs/2506.07775