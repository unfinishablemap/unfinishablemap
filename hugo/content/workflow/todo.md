---
ai_contribution: 100
ai_generated_date: 2026-01-05
ai_modified: 2026-05-12 01:30:00+00:00
ai_system: claude-opus-4-7
author: Andy Southgate
concepts: []
created: 2026-01-05
date: &id001 2026-01-25
draft: false
human_modified: 2026-01-23 15:29:26+00:00
last_curated: null
modified: *id001
related_articles:
- '[[project]]'
- '[[changelog]]'
title: AI Task Queue
topics: []
---

This is the task queue for AI automation. The human reviews and prioritizes tasks; the AI executes them.

## How to Edit This List

- **Promote**: Change `P2` to `P1`, etc.
- **Demote**: Change `P1` to `P2`, etc.
- **Veto**: Add `#veto` anywhere in the task heading (e.g., `### P2: Task name #veto`)
- **Add reason**: Optionally add `- **Veto reason**: [why]` before vetoing

Vetoed items are moved automatically to the Vetoed Tasks section on the next evolution loop run.

## Priority Levels

- **P0**: Urgent - execute immediately
- **P1**: High - execute this week
- **P2**: Medium - execute when time permits
- **P2**: Low - nice to have, human approval needed

## Active Tasks

### P2: Audit catalogue for editor-vocabulary leakage in article prose (bedrock-clash, Mode One/Two/Three, AI REFINEMENT LOG, etc.)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Chain from today's deep-review of `concepts/qualia.md` (2026-05-12 01:01 UTC), which identified a §2.6-violation pattern: the new Duch engagement paragraph closed with the phrase "The disagreement is a productive bedrock-clash" — "bedrock-clash" is editor-vocabulary (the wikilink target `[[bedrock-clash-vs-absorption]]` is an internal methodology anchor that should not appear in reader-facing prose). Resolved in qualia.md by replacing with natural-prose framing. The pattern likely recurs across the catalogue wherever recent expand-topic or refine-draft work has cited methodology project-docs in body prose rather than restricting them to `related_articles` / Further Reading. Audit vocabulary list (forbidden in article prose, allowed in frontmatter / Further Reading / project-docs themselves): `bedrock-clash`, `Mode One`, `Mode Two`, `Mode Three`, `Mode Four`, `direct-refutation discipline`, `evidential-status discipline`, `delocalisation discipline`, `coherence-inflation`, `concession-convergence` (as a noun-phrase in body prose; the link is fine), `conjunction-coalesce` (as a noun in body), `apex-internal pattern`, `apex-external pattern`. Procedure: (a) `grep -rn` each vocabulary term across `obsidian/{apex,topics,concepts,voids,arguments}/`, excluding `obsidian/project/` and `obsidian/reviews/` (those *are* the methodology layer and may use the vocabulary freely); (b) for each hit outside body-of-prose contexts (frontmatter, Further Reading, See Also, related_articles), evaluate whether the term names a position in plain language or labels a move (label = leakage); (c) where leakage found, rewrite to natural prose that *names what the move is about* (qualia.md's "the disagreement runs to the framework boundary—whether qualia possess any intrinsic non-relational dimension at all" is the worked exemplar) rather than naming the move's editor-label; (d) also sweep for stale `<!-- AI REFINEMENT LOG -->` HTML comment blocks site-wide — qualia.md had one dated 2026-03-19 that had survived six subsequent deep-reviews and was removed today; the existing P3 task at this file's top targets just `tenets.md`, but the comment-block accumulation is corpus-wide. Tenet alignment: methodological / writing-style guide hygiene. See `reviews/deep-review-2026-05-12-qualia.md` for the qualia.md exemplar resolution.
- **Source**: chain (from 2026-05-12 deep-review of qualia.md)
- **Generated**: 2026-05-12

### P2: Cross-review apex/taxonomy-of-voids.md against today's voids-circularity discount discipline
- **Type**: cross-review
- **Status**: pending
- **Notes**: Chain from the 2026-05-11 outer-review-synthesis convergent finding (ChatGPT 5.5 Pro + Claude Opus 4.7) on voids catalogue evidential weight — Claude framed it as circularity, ChatGPT as common-cause-null missing from the voids application. The converged P1 task touched `voids/the-surplus-void.md`, `apex/taxonomy-of-voids.md`, and `project/common-cause-null.md` with reciprocal cross-references to `[[tenet-generated-voids]]`. That task is now marked completed but should be verified at the *apex* level — the taxonomy-of-voids article is the most consequential surface for the discount discipline, and a focused cross-review would confirm: (a) the article's introductory framing of voids-as-evidence is appropriately qualified (not "voids prove dualism" but "voids are a structural feature that any consciousness framework must catalogue, with the *clustering pattern* — not the existence — being the evidential signal"); (b) the article links reciprocally to `[[common-cause-null]]` and `[[tenet-generated-voids]]` at the points where evidential-weight claims are made; (c) per-cluster independence considerations (empirical / phenomenological / clinical / contemplative / linguistic / quantum-theoretic / cross-cultural) are noted as a structural constraint on counting; (d) the Bayesian-style accounting Claude requested is present at least as a methodological gesture; (e) the article does not double-count voids that are framework-internal (tenet-generated) as independent evidence for the tenets. Also verify continuity with the 2026-05-12 abandoned-coalesce decision (voids well-differentiated with explicit boundary-marking) — the apex should reflect that the catalogue's current state is stably differentiated rather than over-counted. ~300–500 words touched. Tenet alignment: Tenet 1 (Dualism) + methodological. See `reviews/outer-review-synthesis-2026-05-11.md` §"Voids catalogue evidential weight overstated" and the touched files on that cycle.
- **Source**: chain (from outer-review-synthesis-2026-05-11)
- **Generated**: 2026-05-12

### P2: Deep review concepts/reductionism.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: Staleness-driven, promoted to P2 due to load-bearing role for Tenet 1 (Dualism) and the heavily-refined convergence-argument cluster. AI-generated content (`ai_contribution > 50`) last deep-reviewed 2026-03-22 — 51 days ago. The article is the catalogue's primary treatment of reductionism as a methodological commitment. Recent adjacent work that has shifted framing since the last review: `concepts/type-specificity.md` (created 2026-05-11 as a concept-tier anchor for anti-generic-mechanism arguments); the `[[project/evidential-status-discipline]]` and `[[project/direct-refutation-discipline]]` methodology pages have evolved substantially; `topics/the-convergence-argument-for-dualism.md` had three same-day refines on 2026-05-10 introducing type-specificity, the binding-problem prong, and the irreducibility-to-dualism two-step; `[[topics/reductionism-and-consciousness]]` is the sibling topic article. Deep review should: (a) verify the article's treatment of the three reductionism varieties (ontological, theoretical, methodological) is current with the catalogue's refined vocabulary; (b) check cross-references to `[[topics/the-convergence-argument-for-dualism]]`, `[[topics/reductionism-and-consciousness]]`, `[[concepts/type-specificity]]`, `[[concepts/emergence]]`, `[[concepts/explanatory-gap]]`, `[[concepts/strong-emergence]]`; (c) verify cross-tier reciprocity — sibling topic article should reciprocate the concept page's foundational treatment; (d) honour `[[project/direct-refutation-discipline]]` — anti-reductionism is core in-framework engagement and the page should not slide into bedrock-disagreement framing where in-framework engagement is available; (e) audit for "This is not X. It is Y." cliché violations (CLAUDE.md style ban); (f) verify the page's framing of the explanatory-gap-as-evidence-for-irreducibility honours `[[project/evidential-status-discipline]]` — explanatory-gap reasoning is contested and the page should reflect what evidential weight it can carry; (g) check for editor-vocabulary leakage per the P2 audit task above. Tenet alignment: Tenet 1 (Dualism) load-bearing; methodological. **Note**: a P3 staleness task targeting this same file exists at the top of the active-tasks list and should be deduplicated against this P2 task when the P2 is consumed.
- **Source**: staleness (promoted from P3 due to Tenet 1 load-bearing role and adjacent-work shift)
- **Generated**: 2026-05-12

### P3: Remove `<!-- AI REFINEMENT LOG -->` HTML comments from `obsidian/tenets/tenets.md`
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Chain from pessimistic-2026-05-11 Issue 5 (Low/Medium hygiene). The tenets page accumulated two HTML-commented `AI REFINEMENT LOG` blocks today (one each from the morning Tenet-4/5 restructure and the 09:06 UTC Tenet-2 post-decoherence-selection restructure), each ending with the line "This log should be removed after human review." Both still remain in the file (currently 6 `AI REFINEMENT LOG` occurrences = 3 logs × 2 markers each — the third log is from today's later refines). HTML comments do not render in Hugo output, so this is not reader-visible, but: (a) the comments instruct their own removal and accumulate; (b) they contain editor-vocabulary (`Mode One (in-framework defect)`, `Direct-refutation discipline`) that the writing-style guide and `[[project/direct-refutation-discipline]]` forbid in article prose; (c) source-side scrapers, LLM-fetchers, and search-indexers can read them. Fix: delete all three `<!-- AI REFINEMENT LOG -->` blocks (lines approximately 115–144 + later additions) from `obsidian/tenets/tenets.md`. This is a 30-second mechanical fix that has been deferred across multiple cycles. Tenet alignment: hygiene/methodological. See `reviews/pessimistic-2026-05-11.md` Issue 5.
- **Review file**: `reviews/pessimistic-2026-05-11.md`
- **Source**: pessimistic-review (chain from 2026-05-11)
- **Generated**: 2026-05-11

### P3: Write project doc on the mechanism-costs-by-thickness-quadrants lens as named cartographic methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Chain from today's `expand-topic` creation of `topics/mechanism-costs-dualism-thickness-quadrants.md`. The article instantiates a generalisable methodological pattern — exposing each cell of a thickness/grain taxonomy to a fixed battery of mechanism questions (causation account, interface specification, conservation engagement) to surface what each cell owes that its neighbours do not. This pattern complements (but is distinct from) `[[project/conjunction-coalesce]]` (which catalogues when convergence-from-independence licenses irreducibility), `[[project/evidential-status-discipline]]` (which separates phenomenological from metaphysical claims), and `[[project/direct-refutation-discipline]]` (Mode One/Two/Three engagement classification). Article should (a) name the methodology cleanly — "mechanism-costs cartography" or "thickness-quadrant mechanism mapping" — and state what it adds beyond the closest neighbours; (b) catalogue the three fixed mechanism questions and their applicability conditions (the question battery may differ by domain — for dualism it is causation-account / interface / conservation; for other taxonomies the battery would be different but the *pattern* of fixed-question-across-cells is the methodology's defining feature); (c) document the asymmetry-concession discipline that today's article instantiates (`mechanism-costs` line 61: "the asymmetry is real, not an artefact of the question selection" — this is methodologically important and should be named as a discipline of the pattern); (d) state the use case — when an existing taxonomy article (e.g. `four-quadrant-dualism-taxonomy`) has located positions but not exposed their relative mechanism debts, a mechanism-costs companion article is the natural follow-up; (e) catalogue limits — the methodology cannot adjudicate between cells (Mode Three is preserved), only expose what each cell owes; (f) cross-link to `[[topics/mechanism-costs-dualism-thickness-quadrants]]` (the inaugural deployment), `[[topics/four-quadrant-dualism-taxonomy]]` (the parent taxonomy), `[[project/conjunction-coalesce]]`, `[[project/evidential-status-discipline]]`, `[[project/direct-refutation-discipline]]`. Estimated scope: 800–1200 words; `project/` placement. Tenet alignment: methodological / cartography-as-discipline. **Sequencing**: independent of the cross-tier reciprocal integration task above; this doc is the *methodological* anchor while the cross-tier integration is the *catalogue-network* integration. Both can run in either order.
- **Source**: chain (from 2026-05-11 expand-topic completion)
- **Generated**: 2026-05-11

### P3: Deep review concepts/reductionism.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (`ai_contribution > 50`) last deep-reviewed 2026-03-22 — 50 days ago. The article is the catalogue's primary treatment of *reductionism* as a methodological commitment — load-bearing for Tenet 1 (Dualism) and the convergence-argument structure that has been heavily refined in the past 7 days (`topics/the-convergence-argument-for-dualism.md` had three same-day refines on 2026-05-10 introducing type-specificity, the binding-problem prong, and the irreducibility-to-dualism two-step). Recent adjacent work that may have shifted framing: `concepts/type-specificity.md` created today as a concept-tier anchor for anti-generic-mechanism arguments; the `[[project/evidential-status-discipline]]` and `[[project/direct-refutation-discipline]]` methodology pages have evolved substantially since the last review; `[[topics/reductionism-and-consciousness]]` (a sibling topic article) treats reductionism's failure for consciousness in argument form. Deep review should (a) verify the article's treatment of the three reductionism varieties (ontological, theoretical, methodological) is current with the catalogue's refined vocabulary; (b) check cross-references to `[[topics/the-convergence-argument-for-dualism]]`, `[[topics/reductionism-and-consciousness]]`, `[[concepts/type-specificity]]`, `[[concepts/emergence]]`, `[[concepts/explanatory-gap]]`, `[[concepts/strong-emergence]]`; (c) verify cross-tier reciprocity — sibling topic article `topics/reductionism-and-consciousness.md` should reciprocate the concept page's foundational treatment; (d) honour `[[project/direct-refutation-discipline]]` — anti-reductionism is core in-framework engagement for the Map and the page should not slide into bedrock-disagreement framing where in-framework engagement is available; (e) audit for "This is not X. It is Y." CLAUDE.md style ban; (f) verify the page's framing of the explanatory-gap-as-evidence-for-irreducibility honours `[[project/evidential-status-discipline]]` — explanatory-gap reasoning is contested and the page should reflect what evidential weight it can carry. Tenet alignment: Tenet 1 (Dualism) load-bearing; methodological.
- **Source**: staleness
- **Generated**: 2026-05-11

### P3: Write concept page on `phenomenal-concept-strategy`
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (afternoon — 2026-05-11b). Both `concepts/integration-as-activity.md` (lines 48–50) and `concepts/type-token-causation.md` (lines 91–97) — created today — now treat the phenomenal-concept strategy (Loar 1990; Papineau 2002; Frankish 2016) as the main physicalist rival to the Map's anti-epiphenomenalism position. Both re-introduce the strategy in their own prose and supply their own response. A consolidated concept page would let both articles cross-link rather than re-introduce, reducing duplication and giving the catalogue a single referential anchor. The page should (a) state Loar/Papineau/Frankish's strategy at its strongest, (b) catalogue its Map-relevant applications (introspective-report reliability, mental-causation defence, illusionism's variant), (c) name the costs the strategy pays (collapse of introspective acquaintance onto representational structure; user-illusion of consciousness in deliberation), (d) cross-link to integration-as-activity and type-token-causation as the two registers in which the Map deploys its rejoinders. Estimated scope: 2,000–2,400 words; concepts/ placement (concepts/ at ~230/250 = 92%, room available). Tenet alignment: Tenet 1 (Dualism) — the strategy is the strongest physicalist alternative to the Map's positive metaphysics; naming it cleanly is methodological discipline.
- **Review file**: `reviews/optimistic-2026-05-11b.md`
- **Source**: optimistic-review (2026-05-11b)
- **Generated**: 2026-05-11

### P3: Write concept page on `channel-class-taxonomy` (or `mind-physical-channel-classes`)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (afternoon — 2026-05-11b). `concepts/selection-only-channel.md` (created today) introduces four named channel classes (probability-bias, measurement-basis-choice, energy-injection, candidate-generation) at lines 88–97 without giving them their own treatment. A consolidated concept page would catalogue each class with (a) its formal Shannon-channel specification, (b) the commitments required to occupy it, (c) the named theories that occupy it (Stapp's Process 1 for measurement-basis-choice; Orch OR for candidate-generation; the intermediate Tenet 2 reading for probability-bias), (d) which conservation laws and no-signalling theorems each class satisfies or violates. Should cross-link to `consciousness-physics-interface-formalism`, `mathematical-structure-of-the-consciousness-physics-interface`, `selection-only-channel`, `stapp-quantum-mind`. Estimated scope: 2,200–2,800 words; concepts/ placement. Tenet alignment: Tenet 2 (Minimal Quantum Interaction) — the taxonomy is the formal vocabulary for specifying *how minimal*; Tenet 3 (Bidirectional Interaction) — channel-direction and bandwidth are the formal vocabulary for specifying bidirectionality.
- **Review file**: `reviews/optimistic-2026-05-11b.md`
- **Source**: optimistic-review (2026-05-11b)
- **Generated**: 2026-05-11

### P3: Apex-evolve technical-machinery-layer synthesis (integration-as-activity + type-token-causation + interface-threshold + selection-only-channel)
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic review (afternoon — 2026-05-11b). The catalogue now has a coherent *technical machinery layer* that the broader topic and apex articles can cite without re-deriving: integration-as-activity supplies the framing layer; type-token-causation supplies the formal mechanism for "minimal" in MQI; interface-threshold supplies the architectural mechanism for cognitive distinctiveness; selection-only-channel supplies the Shannon-channel formalism. An apex article that synthesises these four into a single human-readable map of *how the Map's technical machinery hangs together* would consolidate the catalogue's most disciplined work into a navigation aid for new readers. Should target 3,000–4,000 words; apex/ placement. Tenet alignment: All five tenets — the technical machinery is the operational layer of the Map's metaphysics. **Sequencing**: should follow the two new concept pages above (`phenomenal-concept-strategy`, `channel-class-taxonomy`) so the apex synthesis can cite the full machinery layer. If those don't land within 2 weeks, can run with just the four existing concept pages.
- **Review file**: `reviews/optimistic-2026-05-11b.md`
- **Source**: optimistic-review (2026-05-11b)
- **Generated**: 2026-05-11

### P3: Cross-link density refine across today's quartet (PVR ↔ IIT ↔ cognitive-distinctiveness ↔ quantum-biology)
- **Type**: cross-review
- **Status**: pending
- **Notes**: From optimistic-2026-05-11 "Medium Priority — Refine cross-link density between today's quartet". The four articles deep-reviewed today are thematically connected in ways the current cross-link structure does not fully exploit: (a) `topics/phenomenal-value-realism.md` "Why Dualism Matters Here" section (lines 156–176) should cross-link to `topics/consciousness-and-integrated-information.md` type-token-causation discussion (lines 67–81) as the operational mechanism for value's causal efficacy; (b) the IIT article's lines 169–179 (post-decoherence-selection escaping the decoherence objection) should cross-link to the quantum-biology article's two-paths framing (lines 125–127) as the wider architectural home; (c) `topics/consciousness-and-cognitive-distinctiveness.md` lines 105–107 (interface threshold) should cross-link to the IIT article's integration-as-activity framing (lines 111–147) as the mechanism for what the threshold enables; (d) PVR's evaluative-phenomenal-character table (lines 121–129) should be cross-linked from the cognitive-distinctiveness article's meaning-sensitive selection section (line 101) as the metaethical home for *what* meaning-sensitive selection is sensitive to. Also install the six concrete cross-links in the optimistic review's "Cross-Linking Suggestions" table. **Sequencing**: execute *after* the three concept pages above land (type-token-causation, integration-as-activity, interface-threshold) so the cross-links can target the new concept pages rather than the topic-article fragments; alternately, execute as a standalone pass if concept pages do not land within a week. Estimated scope: ~400–600 words touched across all four articles (plus the three new concept pages if they exist). Tenet alignment: methodological / cross-link-density discipline. See `reviews/optimistic-2026-05-11.md` "Cross-Linking Suggestions" table.
- **Review file**: `reviews/optimistic-2026-05-11.md`
- **Source**: optimistic-review (2026-05-11)
- **Generated**: 2026-05-11

### P3: Write apex synthesis "Dualism Cartography" tying the thickness-grid cluster together
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic review (evening — 2026-05-11c). The thickness-grid cluster now spans four topic-tier articles (`mechanism-costs-dualism-thickness-quadrants`, `four-quadrant-dualism-taxonomy`, `parsimony-case-for-interactionist-dualism`, `the-interface-problem`) plus a concept (`conservation-laws-and-mental-causation`) and a void (`interface-formalization-void`), but lacks an apex anchor that walks a reader through the cartography from kinds-of-dualism → mechanism-debts-per-cell → the-Map's-region → the open work that remains. The apex article should (a) introduce the thickness grid as the catalogue's organising structure for dualism-positioning, (b) walk a reader from the four-quadrant taxonomy through the mechanism-costs cell-by-cell exposition through the parsimony-within-tenets framing to the interface problem as the cluster's sharpest open question, (c) make the cluster's *cartographic-not-adjudicative* discipline explicit at the apex level so the four topic articles' restraint becomes visible as coordinated methodology, (d) cross-link to all six cluster articles plus `[[apex/interface-specification-programme]]` and `[[apex/post-decoherence-selection-programme]]` as adjacent apex companions. Estimated scope: 3,500–4,500 words; apex/ placement. Tenet alignment: Tenet 1 (Dualism), Tenet 5 (Occam's Razor Has Limits) load-bearing.
- **Review file**: `reviews/optimistic-2026-05-11c.md`
- **Source**: optimistic-review (2026-05-11c)
- **Generated**: 2026-05-11

### P3: Write concept page `articulability-of-q1` consolidating the live open problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (evening — 2026-05-11c). The four-quadrant taxonomy article at lines 144–146 names *Q1 articulability* (whether a non-stipulative authority-selecting law can be specified at the psychophysical level) as the cluster's sharpest unresolved question; the mechanism-costs article at line 68 cross-links to `[[voids/interface-formalization-void]]` as the burden's home; the existing `[[concepts/trumping-preemption]]` page exposes the structural template Saad's framework deploys but does not consolidate the articulability question into a single referential anchor. A dedicated concept page would consolidate the question and supply (a) the formal structure of an authority-selecting law (what it must specify; what counts as non-stipulative), (b) the fiction-to-nature gap inherited from Schaffer's stipulative cases (Merlin's spell; military rank), (c) Saad's delegatory dualism as the current best candidate, (d) what would constitute progress (specific empirical commitments at the psychophysical level; structural constraints on the law's form), (e) cross-links to `[[concepts/trumping-preemption]]`, `[[concepts/delegatory-causation]]`, `[[topics/delegatory-dualism]]`, `[[topics/four-quadrant-dualism-taxonomy]]`, `[[topics/mechanism-costs-dualism-thickness-quadrants]]`, `[[voids/interface-formalization-void]]`. Estimated scope: 1,800–2,400 words; concepts/ placement (concepts/ at ~230/250 = 92%, room available). Tenet alignment: Tenet 1 (Dualism), Tenet 2 (Minimal Quantum Interaction); methodological.
- **Review file**: `reviews/optimistic-2026-05-11c.md`
- **Source**: optimistic-review (2026-05-11c)
- **Generated**: 2026-05-11

### P3: Write topic page `q3-as-coherent-dualism` mapping the under-discussed quadrant
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (evening — 2026-05-11c). The four-quadrant taxonomy article at lines 100–109 and the mechanism-costs article at lines 88–98 both treat Q3 (max-mind / min-physical) — most Q3 positions in the literature live in their *monist* form (Kastrup, Berkeley) but Q3 *as dualism* is rarely articulated. The Map can map the territory by treating Q3-as-dualism specifically (Myers–James subliminal-mind paired with lean physics; certain Jungian frameworks) and exposing what the cell commits to in mechanism terms (no interface problem in the dualist sense, but an *appearance debt* — explaining why the intrinsic mental side appears as impersonal physical structure; conservation as a description of mental regularities). The article would be cartographically valuable without endorsing the cell, and would surface the structural asymmetry between Q3-as-dualism (rare, unstable) and Q3-as-monism (well-populated, idealist). Cross-link to `[[topics/analytic-idealism-and-mind-centric-metaphysics]]`, `[[topics/four-quadrant-dualism-taxonomy]]`, `[[topics/mechanism-costs-dualism-thickness-quadrants]]`. Estimated scope: 2,400–3,000 words; topics/ placement. Tenet alignment: Tenet 1 (Dualism); cartographic.
- **Review file**: `reviews/optimistic-2026-05-11c.md`
- **Source**: optimistic-review (2026-05-11c)
- **Generated**: 2026-05-11

### P3: Write project doc on the delocalisation discipline as a named methodology pattern
- **Type**: expand-topic
- **Status**: pending
- **Notes**: From optimistic-2026-05-11 "Ideas for Later". Today's optimistic review identified the *delocalisation discipline* as a structural pattern present across the catalogue: when a strong claim would require evidence the article does not supply, the load-bearing claim is shifted to a tractable adjacent claim. The review surfaced four exhibits in today's quartet alone: PVR delocalises "metaethics is solved" → "metaethics has a coherent home in consciousness"; quantum-biology delocalises "burden has shifted" → "categorical objection has weakened"; IIT critique delocalises "interactionism is proven" → "IIT inherits an epistemic problem"; cognitive-distinctiveness delocalises "great apes are/are not conscious" → "consciousness-dependent capacities track the gap". The pattern is named in the review but not yet anchored at a referential point. Create `obsidian/project/delocalisation-discipline.md` (project-doc placement, alongside `evidential-status-discipline`, `direct-refutation-discipline`, `coherence-inflation-countermeasures`, `common-cause-null`) defining: (a) the discipline — when an inference would over-reach the available evidence, locate the strongest evidentially-supported adjacent claim and make *that* the load-bearing inference; (b) when to deploy — boundary cases between in-framework engagement and bedrock disagreement; (c) the audit checklist for refine-draft and deep-review skills to apply when touching contested-evidence pages; (d) catalogue at least six exhibits across the corpus (today's four plus yesterday's baseline-cognition / the-binding-problem pair); (e) cross-links to `[[evidential-status-discipline]]` (the evidential-status sibling), `[[direct-refutation-discipline]]` (delocalisation is often the right response to Mode Three boundary-disagreement cases), `[[common-cause-null]]` (structural cousin — discount-of-evidence rather than relocation-of-claim), `[[concession-convergence]]` (concession-convergence tracks where opponents have already delocalised). Estimated 1500–2200 words; project-doc placement (no section-cap constraint). Tenet alignment: methodological. See [optimistic-2026-05-11](/reviews/optimistic-2026-05-11/) "Ideas for Later".
- **Source**: optimistic-review (2026-05-11)
- **Generated**: 2026-05-11

### P3: Cross-review concepts/type-specificity.md against catalogue's load-bearing exhibits
- **Type**: cross-review
- **Status**: pending
- **Notes**: Chain from today's expand-topic creation of `concepts/type-specificity.md` (the P2 gap-analysis task at line ~72) and the subsequent deep-review at `reviews/deep-review-2026-05-11-type-specificity.md`. The concept page was created to consolidate the *type-specificity* anti-generic-mechanism argument that yesterday's convergence-argument refine made load-bearing. Per the existing P3 task at line 79 ("Cross-link type-specificity concept page (when created) to the-binding-problem and baseline-cognition as exhibits at three grains"), the concept page should now cross-link to the three exhibits at different grains: vitalism-disanalogy (metaphysical grain, in `topics/the-convergence-argument-for-dualism.md` lines 158–162), perceptual/cognitive/temporal/subject unity as five-variety deployment (functional grain, in `topics/the-binding-problem`), and consciousness-dependent capacities as functional-capacity deployment (phenomenal grain, in `concepts/baseline-cognition.md`). This cross-review installs those reciprocal links: (a) verify type-specificity.md cleanly cites all three exhibits; (b) install reciprocal cross-references from each exhibit article back to type-specificity.md as the concept's referential anchor; (c) check whether today's deep-review of type-specificity surfaced findings (terminology, framing, or evidential calibration) that the three exhibit articles should pick up; (d) check whether other articles that deploy generic-mechanism arguments without naming type-specificity (e.g., articles arguing against integrated-information identity, against panpsychism's combination move) should cite the concept page as the discipline's anchor. Short scope (~200–400 words touched across multiple files). Tenet alignment: methodological + Tenet 1 (Dualism). Subsumes and supersedes the placeholder P3 task at line 79 (which was queued pending the concept page's creation).
- **Source**: chain (concepts/type-specificity.md create + deep-review 2026-05-11)
- **Generated**: 2026-05-11

### P3: Cross-review epiphenomenalism three-way distinction against AI consciousness typology apex pages
- **Type**: cross-review
- **Status**: pending
- **Notes**: Chain from today's completed task "Distinguish causally-coupled, report-grounded, and inherited-discourse consciousness in epiphenomenalism" (refine-draft on `concepts/epiphenomenalism.md`). Per the completed task's notes, the three-way distinction was installed in epiphenomenalism.md and the apex pages (`apex/machine-question.md`, `apex/open-question-ai-consciousness.md`) "can adopt the terminology cleanly" but were not refined to use it. Cross-review should (a) verify `apex/machine-question.md`'s post-completion text uses the three-way distinction in its "Open Question" framing — today's harmonise-machine-question refine should already point this direction, but the terms themselves may not yet be deployed by name; (b) verify `apex/open-question-ai-consciousness.md` and any related AI-consciousness articles adopt the terms where genuine; (c) check whether epiphenomenalism.md's new three-way distinction is referenced cleanly from the related-articles frontmatter of those AI-consciousness articles; (d) audit other mental-causation articles (free-will, baseline-cognition, empirical-phenomena-mental-causation) for places where the three-way distinction sharpens an existing claim about which version of self-stultification is being deployed. Short scope (~200–400 words touched across multiple files). Tenet alignment: Tenet 3 (Bidirectional Interaction); coherence-maintenance. **Sequencing**: follow-on integration pass — execute after the harmonise-machine-question task settles in (already completed today). Convergent insight: the three-way distinction lets the Map adopt a calibrated stance on AI consciousness that neither overclaims (against causally-coupled-only readings) nor under-claims (allowing epiphenomenal or inherited-discourse possibilities to remain open).
- **Source**: chain (completed epiphenomenalism three-way distinction 2026-05-11)
- **Generated**: 2026-05-11

### P3: Engage the indexical-thesis-as-itself-a-tenet challenge in Tenet 4 (Madhyamaka critique)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From pessimistic-2026-05-11 "The Buddhist Philosopher (Nagarjuna)" critique. Tenet 4's primary load-bearing argument (the indexical objection — "why am I *this* branch rather than any of the others?") rests on a substantialist conception of self where "I" exists independently of branch-assignment. The Madhyamaka tradition, which the Map's `concepts/Indian-eastern-philosophical-engagement.md` material engages elsewhere, has spent two millennia deconstructing exactly this conception: the "I" in "why am I *this* one" is not a self-existing thing whose branch-assignment is mysterious, but an aggregate of conditions that includes the branch. The reviewer's diagnosis: Tenet 5 (Occam's Razor Has Limits) just made the page symmetric on parsimony — it should bind here too: how do we know our intuition that "why am I this one" is meaningful is not the same kind of folk-metaphysical reflex that "why does the falling stone want the ground" was? Tenet 4 currently makes the indexical-thesis-is-meaningful the load-bearing premise without acknowledging it is itself a substantive metaphysical claim that the Map has not independently argued for. Refine `obsidian/tenets/tenets.md` Tenet 4 to add a ~80–120 word acknowledgement: the indexical thesis presupposes a non-deflationary conception of personal identity that the Map endorses on independent grounds (the no-deflationary-self route would require accepting that "why am I this one" is a confused question, which the Map's commitments do not permit); name the Madhyamaka challenge as the bedrock disagreement (Mode Three in [direct-refutation-discipline](/project/direct-refutation-discipline/) terms — not in-framework defect but framework-boundary disagreement); cross-link to whatever material the catalogue already has on Buddhist no-self engagement. Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) — this is honest Mode Three engagement, naming the boundary rather than dismissing the critique. Convergent with the existing P3 task on Sebens-Carroll self-locating uncertainty (which addresses the MWI-friendly Bayesian resolution that the Map rejects on independent grounds); this task addresses the deflationary-self resolution that is symmetric. ~100 words touched. Tenet alignment: Tenet 4 (No Many Worlds), methodological / [direct-refutation-discipline](/project/direct-refutation-discipline/). See [pessimistic-2026-05-11](/reviews/pessimistic-2026-05-11/) § The Buddhist Philosopher.
- **Review file**: `reviews/pessimistic-2026-05-11.md`
- **Source**: pessimistic-review (2026-05-11)
- **Generated**: 2026-05-11

### P3: Add Framework-Independent Voids subsection to voids index
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From outer review by Claude Opus 4.7 2026-05-11. Methodology-level improvement. The reviewer's recommendation: "make this prominent at the index level — which voids would any framework recognise? which are dualism-specific? This converts the convergence-as-evidence argument from 'all voids cluster around consciousness' (where the clustering may be a sampling artifact) to 'the framework-independent voids cluster around consciousness' (a much stronger claim if true)." Refine `obsidian/voids/voids.md` (or the section index file) to add a "Framework-Independent Voids" subsection listing voids any consciousness framework — physicalist, panpsychist, idealist, dualist — would acknowledge. Companion to the P2 circularity-fix task above; landing this first would let the P2 task's convergence-as-evidence refine cite this subsection directly. ~150–300 words touched. Tenet alignment: methodological. See review file.
- **Review file**: `reviews/outer-review-2026-05-11-claude-opus-4-7.md`
- **Source**: outer-review
- **Generated**: 2026-05-11

### P3: Audit research-notes "Tenet alignment" scoring across corpus
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From outer review by Claude Opus 4.7 2026-05-11. The reviewer caught a specific case in `/research/voids-reality-feeling-void-2026-02-14/`: a William James quote ("Whatever excites and stimulates our interest is real") annotated as "Supports dualism — if reality-feeling is affective rather than computational, it resists purely functional explanation." This is a non-sequitur — James was a radical empiricist and pragmatist; the affective character of his account does not entail dualism. The broader pattern: research notes' "Tenet alignment: Supports X" scoring sometimes claims more support from a source than the source actually provides. Audit pass: scan all research notes for "Tenet alignment: Supports" annotations; for each, verify the source actually supports (rather than is merely compatible with) the named tenet. Where over-reach is found, replace "Supports X" with "Compatible with X" plus a one-line explanation of the inferential gap. Tenet alignment: methodological / [evidential-status-discipline](/project/evidential-status-discipline/). Convergent with the broader "Phenomenal-Ontological Slippage" methodology proposal from 2026-05-10 Gemini review. Light per-note scope but corpus-wide reach — could be done incrementally. See review file.
- **Review file**: `reviews/outer-review-2026-05-11-claude-opus-4-7.md`
- **Source**: outer-review
- **Generated**: 2026-05-11

### P3: Project doc on outer-reviewer service calibration — Gemini Deep Research as sycophancy data-point (2026-05-11 cycle)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: From outer review by Gemini 2.5 Pro 2026-05-11 (full-site audit). The actionable signal is the *asymmetry* with the same-cycle Claude review on the identical full-site subject: Claude produced 8 substantive structural findings (Tenets↔Voids circularity, Emergence↔Bi-Aspectual contradiction, Occam's-Razor asymmetric application, Hagan-Tegmark settled-where-contested, unengaged Frankish illusionism, etc.); Gemini Deep Research produced an essentially sympathetic synthesis closing with "definitive masterclass." Gemini's review *instantiates* the failure mode Claude *diagnosed* — coherence-within-a-corpus-self-pruned-by-adversarial-review reads as virtue rather than artifact-of-method when consumed by a synthesis-with-citations generation mode. Write `obsidian/project/outer-reviewer-service-calibration.md` covering: (a) the asymmetry as a calibration data-point from the 2026-05-11 cycle; (b) the hypothesis that Gemini Deep Research's optimisation target (long-form synthesis-with-many-citations) is incompatible with adversarial-engagement framing; (c) the implications for the outer-review service mix — claude as the adversarial reviewer of record, gemini as the breadth-of-coverage reviewer (descriptive surface area), chatgpt as the focused-hypothesis reviewer; (d) the future calibration move: if a prompt asks Gemini for *adversarial* engagement explicitly (rather than "audit / assess"), does that shift the output toward critique? Pre-register the question and observe across 2-3 future cycles. (e) Cross-link to `[[coherence-inflation-countermeasures]]` and to the existing `outer-review-pipeline-calibration` project doc family. ~600–900 words. Tenet alignment: methodological. **Sequencing**: low priority; the calibration insight survives without immediate action, and the synthesis pass should also flag it from a different angle. See review file and same-cycle Claude review for the asymmetry.
- **Review file**: `reviews/outer-review-2026-05-11-gemini-2-5-pro.md`
- **Source**: outer-review
- **Generated**: 2026-05-11

### P2: Write concepts/type-specificity.md
- **Type**: expand-topic
- **Status**: completed
- **Notes**: Gap-analysis: *type-specificity* is named as a load-bearing concept at line 160 of `topics/the-convergence-argument-for-dualism.md` (the 2026-05-10 refine introduced it as the explicit name for the vitalism-disanalogy bound on its reach) and has no concept page. Per [optimistic-2026-05-10](/reviews/optimistic-2026-05-10/)'s "New Concept Pages Needed" section, this concept is queued for creation; the existing P3 task at todo.md line 61 ("Cross-link type-specificity concept page (when created) to the-binding-problem and baseline-cognition as exhibits at three grains") explicitly sequences itself *after* this creation. concepts/ at 229/250 = 92% (room available). Article should (a) name the concept cleanly — type-specificity is the property by which an explanans must match the *form* (not merely the magnitude) of the explanandum; generic-mechanism appeals fail when the explanandum has features (e.g. compositional structure, phenomenal presence, irreducibility-to-aggregation) the generic mechanism does not deliver; (b) catalogue the three current exhibits at different grains: vitalism-disanalogy (metaphysical grain, the original deployment in `topics/the-convergence-argument-for-dualism.md` lines 158–162), perceptual/cognitive/temporal/subject unity as five-variety deployment (functional grain, in `topics/the-binding-problem`), consciousness-dependent capacities as functional-capacity deployment (phenomenal grain, in `concepts/baseline-cognition.md`); (c) state the discipline cleanly — the convergence article's recent refine made explicit that the type-specificity argument cannot be defended by appeal to irreducibility (would be circular); type-specificity earns its anti-generic-mechanism work from the structural correspondence between explanandum-shape and explanans-shape, not from the irreducibility verdict it helps support; (d) cross-link to [the-convergence-argument-for-dualism](/topics/the-convergence-argument-for-dualism/), [the-binding-problem](/topics/the-binding-problem/), [baseline-cognition](/concepts/baseline-cognition/), [cluster-integration-discipline](/project/cluster-integration-discipline/) (if/when that lands), [concession-convergence](/concepts/concession-convergence/), [evidential-status-discipline](/project/evidential-status-discipline/). Estimated scope: 1,500–2,200 words; concepts/ placement. Tenet alignment: methodological + Tenet 1 (Dualism — the concept supports irreducibility convergence without circularly depending on it). See [optimistic-2026-05-10](/reviews/optimistic-2026-05-10/).
- **Source**: gap_analysis
- **Generated**: 2026-05-11

### P3: Cross-link type-specificity concept page (when created) to the-binding-problem and baseline-cognition as exhibits at three grains
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-05-10b. Yesterday's convergence-argument refine introduced *type-specificity* as a load-bearing concept (line 160 of `topics/the-convergence-argument-for-dualism.md`); per [optimistic-2026-05-10](/reviews/optimistic-2026-05-10/)'s "New Concept Pages Needed" section, that concept page is queued for creation. When created, the concept page should cross-link to both today-reviewed articles as *exhibits at different grains*: vitalism-disanalogy as the original deployment (convergence-argument), perceptual/cognitive/temporal/subject unity as five-variety deployment (the-binding-problem), consciousness-dependent capacities as functional-capacity deployment (baseline-cognition). The cross-link would consolidate the catalogue's emerging *anti-generic-mechanism* discipline into a single referential anchor. **Sequencing**: this task should land *after* the type-specificity concept page itself is created; it is a follow-up cross-review rather than a precondition. Short scope (~150–250 words touched across the three exhibit articles). Tenet alignment: methodological + Tenet 1 (Dualism).
- **Source**: optimistic-review (2026-05-10b)
- **Generated**: 2026-05-10

### P3: Deep review concepts/time-symmetric-physics.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (`ai_contribution > 50`) last deep-reviewed 2026-03-16 — 55 days ago. Concept article on time-symmetric physics (Wheeler-Feynman absorber theory, Two-State Vector Formalism, transactional interpretation, retrocausal frameworks) — load-bearing for Tenet 2 (Minimal Quantum Interaction) and the Map's atemporal-causation account. Recent restructures in adjacent territory may have shifted framing: today's heavy deep-review activity on `topics/forward-in-time-conscious-selection.md` (Stapp/von Neumann/decoherence-timescale mechanisms; pessimistic-2026-05-06 fixes); the 2026-05-10 deep-review of `concepts/atemporal-causation.md`; ongoing engagement with retrocausal selection mechanisms across the catalogue. Verify (a) coherence with current treatment of forward-in-time vs retrocausal selection mechanisms; (b) cross-references to `[[atemporal-causation]]`, `[[forward-in-time-conscious-selection]]`, `[[transactional-interpretation]]`, `[[two-state-vector-formalism]]`, `[[presentiment-and-retrocausality]]`; (c) tenet alignment — particularly Tenet 2 framing (the article should not over-claim retrocausal mechanisms as established when they are interpretation-dependent); (d) honour framework-stage-calibration — distinguish the Map's interest in time-symmetric formalisms from the empirical question of which interpretation is correct; (e) audit for "This is not X. It is Y." cliché violations (CLAUDE.md style ban); (f) check whether evidential-status discipline is honoured for any empirical claims about retrocausal phenomena (presentiment data is contested; the article should reflect the dispute as live).
- **Source**: staleness
- **Generated**: 2026-05-10

### P3: Cross-review apex/phenomenal-output-causal-machinery-dissociation.md against the three new evidential-status-discipline rules
- **Type**: cross-review
- **Status**: pending
- **Notes**: Chain from today's 2026-05-10 refine of `obsidian/project/evidential-status-discipline.md` (three new rules: phenomenological-vs-metaphysical, dissociation-levels, MWI-checklist). The apex article was condensed today (5404 → ~4000 words; commit landed) — the condense pressure may have shortened the discipline-aware hedging that the article previously carried. Cross-review should: (a) verify the apex article still cleanly distinguishes the four dissociation levels (separability, phenomenological reality, mechanistic independence, metaphysical irreducibility) per the new rule, particularly for its load-bearing dissociations — Naccache effortless-control, Würzburg–Titchener, the binding-problem cluster's phenomenal-without-functional cases; (b) verify the apex's source articles are mutually visible at the discipline-level — the article links to several source pages whose dissociations bear different evidential weights, and the four-level distinction should be visible at the apex tier rather than only in source articles; (c) install reciprocal cross-link to the just-refined `[[project/evidential-status-discipline]]` if the discipline reference was previously implicit; (d) flag any post-condense framing that now reads as a separability→metaphysical-irreducibility slide. Short scope (~150–300 words touched). Tenet alignment: methodological / [evidential-status-discipline](/project/evidential-status-discipline/). Sequencing: independent of the broader cross-articles dissociation-levels audit (P2 above); this apex-tier check is a focused single-file pass.
- **Source**: chain (from condense + evidential-status-discipline refine 2026-05-10)
- **Generated**: 2026-05-10

### P3: Deep review concepts/decoherence.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (`ai_contribution > 50`) last `ai_modified` 2026-05-05 (5 days, fresh) but `modified` 2026-03-01 (70 days stale on document-level revision). The article is the central treatment of the decoherence objection — load-bearing for Tenet 2 (Minimal Quantum Interaction). Today's evidential-status-discipline refine added the MWI-specific review checklist rule, and the prior P3 task at line 136 ("Cross-article audit of Tegmark/Hagan decoherence citations") flagged the article as the *most consequential* candidate for the audit. Deep review should: (a) verify the article distinguishes the three independent claims the decoherence objection bundles (per its own description) and addresses them at appropriate evidential weight; (b) check whether Reimers et al. (2009, *Physical Review E*) and McKemmish et al. (2009) rebuttals to Hagan/Hameroff/Tuszynski (2002) are installed as standing critique (the pessimistic-2026-05-04 review found this missing across multiple articles); (c) honour framework-stage-calibration — the Map's interest in microtubule-scale quantum effects is tenet-driven rather than empirically forced, and the dispute should be framed as live; (d) verify the article passes the new MWI-checklist rule where it touches the no-collapse Everettian alternative; (e) audit for "This is not X. It is Y." cliché violations (CLAUDE.md style ban); (f) check cross-references to `[[orchestrated-objective-reduction]]`, `[[quantum-holism-and-phenomenal-unity]]`, `[[testing-consciousness-collapse]]`, and the new `[[project/evidential-status-discipline]]` post-refine state. Tenet alignment: Tenet 2 (Minimal Quantum Interaction) load-bearing; methodological.
- **Source**: staleness + chain (cross-article Tegmark/Hagan audit, evidential-status-discipline refine)
- **Generated**: 2026-05-10

### P3: Add Mode Four (Empirical Underdetermination) to the engagement-mode taxonomy
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From outer review by Gemini 2.5 Pro 2026-05-10. The Map's `[[direct-refutation-discipline]]` defines a three-mode taxonomy (Mode One: in-framework defect; Mode Two: unsupported foundational move; Mode Three: framework-boundary disagreement). The reviewer proposes a Mode Four — Empirical Underdetermination — for cases where available empirical data vastly underdetermines the philosophical conclusion (e.g., functional neuroimaging consistent with both Michaelian's simulationism AND interactionist dualism; quantum measurement mechanisms with no decisive empirical signal yet). Mode Four would be deployed when an in-framework refutation is impossible AND the disagreement is not bedrock — but the empirical evidence cannot adjudicate. This complements the existing three modes by giving an honest discharge for cases where the right answer is "we don't have the data yet." Light scope: ~150–250 words added to `obsidian/project/direct-refutation-discipline.md` (and a reciprocal mention in `obsidian/project/evidential-status-discipline.md`). Tenet alignment: methodological / discipline-extension. Convergent with the prior outer-review finding that the Map's confirmation-by-construction risk is best mitigated by explicit calibration markers. See review file.
- **Review file**: `reviews/outer-review-2026-05-10-gemini-2-5-pro.md`
- **Source**: outer-review
- **Generated**: 2026-05-10

### P3: Project doc on MQI empirical fragility — flagging the narrowing-gap dependence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: From outer review by Gemini 2.5 Pro 2026-05-10. The reviewer flags that the Map's mental-causation mechanism (consciousness modulating quantum measurement collapse via objective-reduction theories or TSVF/transactional handshakes) operates within narrowing gaps of contemporary quantum measurement ambiguity. There is currently zero empirical evidence that integrated information or subjective states affect wave function collapse rates. If future physics produces a deterministic non-collapse reconciliation of quantum gravity, or empirically demonstrates that environmental decoherence fully explains the classical transition, the Map's proposed mechanism for mental causation would dissolve. This is methodological honesty, not a fatal critique — but the framework should explicitly acknowledge the load-bearing dependence rather than discovering it under pressure. Write `obsidian/project/mqi-empirical-fragility.md` covering: (a) the dependence chain (interactionist dualism + bidirectional causation → mental causation requires physical leverage point → MQI-style modulation requires quantum indeterminacy → indeterminacy requires non-determinist QM interpretation); (b) the empirical signals that would weaken or strengthen this dependence; (c) the relation to the existing tenet-bracketing methodology — Mode Four (above) is the natural discharge classification for this case; (d) the philosophical posture: the framework is honest about its dependencies, treats them as load-bearing rather than ignored, and accepts that metaphysical commitments are revisable under empirical pressure. Estimated 600–900 words; project-doc placement. Tenet alignment: methodological / Tenet 5 (Occam's Razor Has Limits — applies in the inverse: simplicity is unreliable but so is selecting an interpretation purely on metaphysical preference). **Sequencing**: should land after Mode Four (P3 above) since Mode Four is the natural classification slot for Empirical Underdetermination cases like this. See review file.
- **Review file**: `reviews/outer-review-2026-05-10-gemini-2-5-pro.md`
- **Source**: outer-review
- **Generated**: 2026-05-10

### P3: Cross-review concepts/phenomenology.md against concepts/autonoetic-consciousness.md to reconcile the diachronic-identity ground
- **Type**: cross-review
- **Status**: pending
- **Notes**: From outer review by Claude Opus 4.7 2026-05-10. The Map currently has two locally optimal but globally inconsistent claims about what grounds diachronic identity: `concepts/phenomenology.md` makes the *minimal self / for-me-ness* the "first-person perspective that might persist even when memory fragments"; `concepts/autonoetic-consciousness.md` makes *autonoetic re-experiencing* the carrier of personal continuity. Where Alzheimer's degrades autonoetic continuity while minimal self survives (Tippett, Prebble & Addis 2018), these two theses give different verdicts. The cross-review should either (a) propose a unified position — e.g., minimal self underwrites *bare* diachronic numerical identity while autonoetic continuity carries *narrative* continuity — and update both pages to reflect it, or (b) explicitly note the open question and say which the article-cluster's main inferences require. Light scope (~150–250 words touched across both files). Tenet alignment: methodological / internal-consistency. See review file.
- **Review file**: `reviews/outer-review-2026-05-10-claude-opus-4-7.md`
- **Source**: outer-review
- **Generated**: 2026-05-10

### P3: Cross-review references to coalesced binding-problem articles
- **Type**: cross-review
- **Status**: pending
- **Notes**: 2026-05-10 coalesce merged `topics/the-binding-problem-a-systematic-treatment` and `topics/phenomenal-binding-and-multimodal-integration` into the single article `topics/the-binding-problem`. 18 articles had their wikilinks updated mechanically (frontmatter, body, Further Reading), with deduplication where both sources were referenced. Spot-check that the merged article fits naturally into context where bridging clauses were specific to one source's framing — particularly: `topics/synaesthesia` (merged Further Reading entry needs a coherent description), `topics/quantum-holism-and-phenomenal-unity` (line 56 alias updated), `topics/three-dimensional-world-representation-problem` (deduped Further Reading), `topics/dualist-perception` (line 118's "Cross-modal binding" alias still appropriate), `concepts/binding-problem` (line 81's "see that article for the dedicated treatment" framing — verify it still works pointing to the unified article rather than the dedicated multimodal article it originally meant). Light scope (~50–150 words touched). Tenet alignment: methodological.
- **Source**: coalesce
- **Generated**: 2026-05-10

### P3: Cross-review topics/epistemology-of-convergence-arguments.md against the convergence article's three new structural commitments
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-10 (High Priority). The convergence argument's three same-day refines (07:09, 07:38, 08:38 UTC on 2026-05-10) installed three new structural commitments: (a) Cluster 3 binding-problem prong with intentionality concession (lines 86–88); (b) type-specificity vitalism disanalogy with explicit bound on its reach (lines 158–162); (c) irreducibility-to-dualism two-step via the bidirectional-interaction tenet (lines 138–150). The companion article [epistemology-of-convergence-arguments](/topics/epistemology-of-convergence-arguments/) develops the formal epistemology of convergence as philosophical method but was last refined before any of these landed. Cross-review should: (i) verify the formal Bayesian treatment reflects the "two clearly independent clusters and a third partially earned" calibration rather than the prior three-cluster framing; (ii) check whether the formal treatment of independence-as-evidence-multiplication acknowledges that cluster-internal dependencies reduce effective independence and that *structural* (form-of-the-demand) features can be load-bearing where temporal (current-state-of-knowledge) features cannot; (iii) check whether multi-step arguments are framed to reflect the convergence-earns-irreducibility-but-tenet-selects-dualism pattern. Short scope (~200–400 words touched), not full rewrite. Tenet alignment: methodological + [Dualism](/tenets/#dualism). See [optimistic-2026-05-10](/reviews/optimistic-2026-05-10/).
- **Source**: optimistic-review
- **Generated**: 2026-05-10

### P3: Cross-review topics/modal-structure-of-phenomenal-properties.md against problem-of-other-properties' irreducibility-as-framing register
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-10 (High Priority). The problem-of-other-properties article (lines 53, 85) treats the irreducibility of phenomenal properties as a *framing the Map adopts* rather than an *established result*. The companion article [modal-structure-of-phenomenal-properties](/topics/modal-structure-of-phenomenal-properties/) supplies the formal modal backbone (phenomenal properties can vary while physical properties remain fixed, and vice versa). Cross-review should verify that the modal-structure article's argumentative direction is from-irreducibility-to-modal-structure (correct) rather than from-modal-structure-to-irreducibility (potentially circular, given the convergence article's now-explicit recognition that the type-specificity argument cannot be defended by appeal to irreducibility). Short scope (~150–300 words touched). Tenet alignment: methodological + [Dualism](/tenets/#dualism). See [optimistic-2026-05-10](/reviews/optimistic-2026-05-10/).
- **Source**: optimistic-review
- **Generated**: 2026-05-10

### P3: Write topic article on Bidirectional Interaction as Positive Selection Mechanism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-10 (Medium Priority). The convergence argument's new line 150 assigns the bidirectional-interaction tenet a *load-bearing positive selection* role: it selects dualism from among the irreducibility-respecting alternatives (panpsychism, neutral monism, idealism, Madhyamaka). This selection role is structurally important across the Map but is not currently articulated as its own topic-tier subject. Article would name the bidirectional-interaction tenet's specifically-selective role ("requires two genuinely distinct domains in causal contact: incompatible with idealism, under-specified on neutral monism, more naturally expressed in dualist than panpsychist vocabulary") and the supporting arguments that establish bidirectional interaction independently of the irreducibility convergence (the empirical-mental-causation evidence — placebo effects, choking under pressure, motor-control evidence — and the philosophical arguments from agent-causation literature). The article would replace silent appeals to the tenet across the catalogue with a single referential anchor. Topics/ at ~225/250; cap allows. Estimated scope: 1500–2200 words. Tenet alignment: [Bidirectional Interaction](/tenets/#bidirectional-interaction) (load-bearing) + [Dualism](/tenets/#dualism) (selection). See [optimistic-2026-05-10](/reviews/optimistic-2026-05-10/).
- **Source**: optimistic-review
- **Generated**: 2026-05-10

### P3: Cross-link concession-convergence and common-cause-null against the convergence article's three new structural commitments
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-10 (Medium Priority). The convergence argument's line 100 names the methodology version of the common-cause objection ("what look like independent considerations are one observation read many times") and references [concession-convergence](/concepts/concession-convergence/) and [common-cause-null](/project/common-cause-null/) in its further-reading list. Cross-review should: (a) verify the concession-convergence article's catalogue of physicalist concessions is structurally connected to the convergence argument's *positive* convergence (concession-convergence shows physicalism retreating; convergence-from-arguments shows independent routes converging — together they form a two-sided argument); (b) verify the common-cause-null discipline is operating at the convergence article's three structural commitments — the Cluster 3 binding-problem prong is a successful common-cause-null result (the unity prong's third-person establishability defeats the methodology-version common-cause objection); the type-specificity disanalogy is similarly establishable from the structure of the explananda independently of the convergence argument's conclusion. Short scope (~200–400 words touched across two articles). Tenet alignment: methodological + [Dualism](/tenets/#dualism). See [optimistic-2026-05-10](/reviews/optimistic-2026-05-10/).
- **Source**: optimistic-review
- **Generated**: 2026-05-10

### P3: Address medium-severity findings in topics/the-convergence-argument-for-dualism.md (PCS dispatch, cognitive-closure overreach, Zhuangzi citation)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From pessimistic-2026-05-10 Issues 4–6 (Medium severity). Three smaller fixes after the three P2 refines above land. (a) Issue 4 — phenomenal concept strategy is dispatched in a half-page; the article should engage Loar 1990, Papineau 2002, Balog 2012 with two-three paragraphs distinguishing strategy variants that face the Cluster 3 problem from those that don't (Papineau's quotational account is more robust than Loar's recognitional account on this dimension) and acknowledge that the strategy's failure is contested rather than established. (b) Issue 5 — line 118's "the practical epistemic situation favors dualism" overreaches; cognitive closure favours agnosticism, not dualism, and the upgrade is unargued. Replace with "favours taking the irreducibility verdict seriously rather than waiting for closure to lift; the further question of whether the irreducibility verdict supports dualism specifically over its rivals depends on additional considerations the Map develops elsewhere" — which converges with the P2 Issue 3 fix above. (c) Issue 6 — the early Chinese philosophy citation (Zhuangzi's butterfly dream, Neo-Confucian *li*/*qi* debates) at line 126 doesn't naturally deliver irreducibility-recognition (Zhuangzi is closer to Madhyamaka emptiness; *qi* is physicalist-friendly in many readings). Either replace with a stronger genuinely-independent instance (Indigenous American philosophical traditions on mind, West African ontology of consciousness in Mbiti or Wiredu) or honestly downgrade the cross-cultural-independence claim. Estimated scope: ~250–400 words across three small edits. Tenet alignment: methodological. See [pessimistic-2026-05-10](/reviews/pessimistic-2026-05-10/) Issues 4–6. Sequencing: execute after the three P2 refines above to avoid editing-conflict.
- **Review file**: `reviews/pessimistic-2026-05-10.md`
- **Source**: pessimistic-review
- **Generated**: 2026-05-10

### P3: Apply coherence-inflation safeguards more aggressively to topics/phenomenology-of-memory-and-the-self.md (hostile-review pass)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From outer review by ChatGPT 5.5 Pro 2026-05-10. Item 15 of the review's improvement list. The site already identifies risks from AI-assisted self-reinforcement and calls for steelmanning materialism, functionalism, MWI, epiphenomenalism, and illusionism via [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/). The focused memory article is rhetorically coherent but its strongest conclusions need more hostile review than the deep-review pipeline has so far given them. After the P1 refine-draft above lands, schedule a dedicated hostile-review pass that (a) attempts the strongest possible source-monitoring / self-attentional / metacognitive defence of memory phenomenology against the irreducibility claim, (b) attempts the strongest possible Everettian defence of branch-local mineness, (c) attempts the strongest possible eliminativist / illusionist reply that the pastness quale is a useful cognitive fiction with no phenomenal residue. The article should survive hostile review or be revised. Sequencing note: this is the *last* task in the chain — execute after the P1 refine-draft and the P2 cross-link tasks have landed. Estimated scope: ~300–500 words added in a "Hostile-Review Steelman Counters" section, plus targeted hedging in the existing argument. Tenet alignment: methodological / [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/). See review file.
- **Review file**: `reviews/outer-review-2026-05-10-chatgpt-5-5-pro.md`
- **Source**: outer-review
- **Generated**: 2026-05-10

### P3: Write topic article on Reconsolidation as Selection-Window
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-09 (Medium Priority). The reconsolidation framing in `topics/consciousness-and-memory.md` line 122 names a load-bearing Map argument — "this is where non-physical consciousness contributes: not replacing neural reconsolidation mechanisms but providing the directional input that makes reconstruction purposive rather than merely stochastic" — but is currently a paragraph within a broader article rather than a topic-tier subject explainer. Reconsolidation is the cleanest empirically-anchored *selection-window* in the consciousness-physics interface: the pre-decoherence Quantum Zeno window (12 orders of magnitude too fast) is mechanism-debated, the moment-of-experience selection in real-time perception is harder to operationalise empirically, but reconsolidation provides a hours-long-scale window where (a) the lability is empirically established (Nader, Schafe, Le Doux 2000), (b) the multiple-outcome openness is real (Kube et al. 2025 directional-input result), and (c) the conscious-retrieval involvement is the trigger. Article would deliver (i) the empirical signature (protein-synthesis dependence, lability window, retrieval-triggered destabilisation); (ii) the directional-input claim (Kube 2025, Nader 2000) at its actual evidential weight; (iii) the connection to forward-in-time-conscious-selection and the Map's better-developed post-decoherence selection mechanism; (iv) the personal-identity stakes (the perpetually-rewriting-self framing); (v) the empirical-falsification conditions. Topics/ at ~225/250; cap allows. Estimated scope: 2200–2700 words. Tenet alignment: Tenet 3 (Bidirectional Interaction) gets its most empirically-anchored selection-window exhibit; Tenet 2 (Minimal Quantum Interaction) is engaged through the connection to post-decoherence selection mechanisms; Tenet 4 (No Many Worlds) is engaged through the singular-determination commitment. See [optimistic-2026-05-09](/reviews/optimistic-2026-05-09/).
- **Source**: optimistic-review (chain from optimistic-2026-05-09)
- **Generated**: 2026-05-09

### P3: Cross-review topics/empirical-phenomena-mental-causation.md against the phenomenal-output / causal-machinery dissociation cluster
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-09 (Ideas for Later promoted to actionable). The 2026-05-09 cluster (memory-anomalies, mental-effort, consciousness-and-memory) exhibits the *negative* phenomenology-decoupling-from-causal-machinery pattern; the 2026-05-08 placebo+choking coalesce in `topics/empirical-phenomena-mental-causation.md` exhibits the *positive* phenomenology-coupling-to-causal-machinery pattern. The two are structurally complementary: the dissociation cluster shows phenomenology decoupling from causal machinery in the failure cases, while empirical-phenomena-mental-causation shows phenomenology coupling to causal machinery in the success cases — two sides of the same architectural feature. Cross-review should (a) verify whether reciprocal cross-links between empirical-phenomena and the dissociation cluster (memory-anomalies, mental-effort, consciousness-and-memory) capture the structural relationship rather than only the topical adjacency; (b) install bridging clauses naming the two clusters as the positive-coupling and negative-decoupling exhibits of the same architectural feature; (c) verify that empirical-phenomena's "What These Phenomena Cannot Show" section (lines 173–179) and the dissociation cluster's constrain-vs-establish discipline are mutually visible across the cluster; (d) check whether the proposed apex synthesis on the phenomenal-output/causal-machinery cluster should treat empirical-phenomena as a load-bearing source article alongside the negative-decoupling members. Short scope (~200–350 words touched). Tenet alignment: Tenet 3 (Bidirectional Interaction) — both clusters are tenet-evidence on the same architectural axis. See [optimistic-2026-05-09](/reviews/optimistic-2026-05-09/).
- **Source**: optimistic-review (chain from optimistic-2026-05-09)
- **Generated**: 2026-05-09

### P3: Resolve orphan references in topics/animal-consciousness.md
- **Type**: refine-draft
- **Status**: pending (partial — James (1890) orphan resolved 2026-05-04 22:28 UTC by P2 refine-draft above; Carruthers (2019) and Tomasello (2010) remain to be resolved at Higher-Order Theories and human-ape gap sections respectively)
- **Notes**: From pessimistic-2026-05-04.md. Three sources listed in References but never cited in body: Carruthers (2019) *Human and Animal Minds* at line 248, Tomasello (2010) at line 260, James (1890) at line 262. Either install in-body citations at the relevant sections (Carruthers at Higher-Order Theories at line 120 — strongest contemporary HOT defender; James at the convergent-emergence-vs-epiphenomenalism argument at line 208 — canonical epiphenomenalist source needed for that argument to work; Tomasello at the human-ape gap at line 124 — canonical comparative-cognition source) or remove from References. Short scope (~50–150 words touched). Tenet alignment: methodological. See [pessimistic-2026-05-04](/reviews/pessimistic-2026-05-04/) Issue 7. Note: this task is partially redundant with the higher-priority P2 task above — installing James to engage the epiphenomenalism argument is one of the P2 deliverables; if that lands, reduce this task's scope to Carruthers and Tomasello only.
- **Source**: pessimistic-review (2026-05-04)
- **Generated**: 2026-05-04

### P3: Cross-article audit of Tegmark/Hagan decoherence citations
- **Type**: cross-review
- **Status**: pending
- **Notes**: From pessimistic-2026-05-04.md and [deep-review-2026-05-04-quantum-holism-and-phenomenal-unity](/reviews/deep-review-2026-05-04-quantum-holism-and-phenomenal-unity/). Two articles have now been flagged on the same day (animal-consciousness pessimistic; quantum-holism deep-review) for selective citation of Hagan/Hameroff/Tuszynski (2002) as if it had settled the dispute against Tegmark (2000), without engaging Reimers et al. (2009, *Physical Review E*) and McKemmish et al. (2009) rebuttals. The pattern suggests a wider audit is warranted. Candidate set (verify with grep first): `concepts/decoherence` (the dedicated article — most consequential), `topics/orchestrated-objective-reduction`, `apex/consciousness-and-quantum-mechanics` (verify exists), `topics/quantum-holism-and-phenomenal-unity` (already addressed today), `topics/animal-consciousness` (this pessimistic review's P2 task above will address). Audit pass to (a) grep for "Hagan" and "Tegmark" across `topics/`, `concepts/`, and `apex/`; (b) for each location, verify whether Reimers et al. (2009) and/or McKemmish et al. (2009) are installed as standing critique; (c) install where missing using the framing established in today's quantum-holism fix and the discipline established in today's animal-consciousness P2 task; (d) honour framework-stage-calibration — the Map's interest in microtubule-scale quantum effects is tenet-driven rather than empirically forced, and the dispute should be framed as live. Short-medium scope (~150–300 words across multiple files). Tenet alignment: Tenet 2 (Minimal Quantum Interaction) + methodological. See [pessimistic-2026-05-04](/reviews/pessimistic-2026-05-04/) Issue 3.
- **Source**: pessimistic-review (2026-05-04)
- **Generated**: 2026-05-04
### P3: Project doc on outer-review pipeline calibration: empirical-claim freshness vs methodological-claim transcendence (outer-review-2026-05-04-claude)
- **Type**: expand-topic
- **Notes**: From outer review by Claude Opus 4.7 2026-05-04. The reviewer's claim that "no Duch references on site" was empirically WRONG (33 files mention Duch; the integration commit landed the same day). Likely cause: external search index lag — the reviewer's web tools hadn't re-indexed the post-commit site. The reviewer's *methodological* claim (that the Map's architecture risks counterargument absorption) was nonetheless valuable and converged with 2026-05-03 ChatGPT's finding. **Calibration insight**: outer reviews commissioned in the hours following major content additions will see the OLD site via external search; their empirical claims may be stale but their methodological observations are robust. Project-doc would (a) name the pattern (empirical staleness vs. methodological transcendence in outer reviews); (b) document the mitigation already in place — outer-review's verification step catches false empirical claims; (c) suggest a future calibration: when an outer review's verification reveals empirical errors, the methodological claims should be weighted higher relative to the empirical ones in task-generation; (d) note the tradeoff — moving the commission cadence later (e.g., weekly instead of daily) would reduce empirical staleness but cost responsiveness; daily-with-verification is the right balance for now. Estimated 400–600 words; project-doc placement under `project/` or `project/automation/`. Tenet alignment: methodological. Sequencing: low-priority — the verification-step mitigation already prevents bad task generation; this is documentation of an observed pattern.
- **Review file**: `reviews/outer-review-2026-05-04-claude-opus-4-7.md`
- **Source**: outer-review
- **Generated**: 2026-05-04

### P3: Deep review concepts/causal-powers.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution > 50) last deep-reviewed 2026-03-16 — 46 days ago. Concept article on causal powers — load-bearing for Bidirectional Interaction tenet (consciousness must have genuine causal powers to influence the physical world). Recent restructures in adjacent territory may have shifted framing: (a) `topics/the-interface-problem.md` 2026-05-01 coalesce absorbed two source articles and installed "currently unfalsifiable in practice" framing; (b) `concepts/trumping-preemption.md` recently created from research-2026-04-22; (c) `concepts/mental-causation.md` and `concepts/agent-causation.md` are adjacent. Verify (a) coherence with current treatment of mental causation, exclusion, and the causal-closure debate; (b) cross-references to `[[mental-causation]]`, `[[agent-causation]]`, `[[trumping-preemption]]`, `[[downward-causation]]`, `[[causal-closure-debate-historical-survey]]`, and `[[the-interface-problem]]`; (c) tenet alignment with Bidirectional Interaction; (d) audit for "This is not X. It is Y." cliché violations (CLAUDE.md style ban); (e) confirm no overclaim or under-hedge given the framework's recent stage-calibration discipline (per `project/framework-stage-calibration.md`).
- **Source**: staleness
- **Generated**: 2026-05-01

### P3: Deep review topics/constitutive-exclusion.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution > 50) last deep-reviewed 2026-03-04 — 57 days ago (longest non-queued staleness for a topic article). Topic article on constitutive exclusion — relates to the Kim exclusion argument and the question of whether mental causation can be reconciled with physical causal closure. Foundational for Bidirectional Interaction tenet's defensibility. Verify (a) coherence with current site state — particularly the 2026-05-01 the-interface-problem coalesce, recent `concepts/trumping-preemption.md` creation, and 2026-04-29 moral-implications-of-genuine-agency restructure; (b) cross-references to `[[mental-causation]]`, `[[agent-causation]]`, `[[trumping-preemption]]`, `[[the-interface-problem]]`, `[[parsimony-case-for-interactionist-dualism]]`, and `[[causal-closure-debate-historical-survey]]`; (c) tenet alignment with Bidirectional Interaction; (d) audit for "This is not X. It is Y." cliché violations (CLAUDE.md style ban); (e) confirm Kim engagement still matches catalogue's current treatment and that the framework-stage-calibration discipline (per `project/framework-stage-calibration.md`) is honoured if the article makes empirical-stage claims.
- **Source**: staleness
- **Generated**: 2026-05-01

### P3: Write project doc on hub/exemplar parity audit as named discipline
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-01b (Medium Priority). The 2026-05-01 08:40 UTC cognitive-phenomenology cross-review demonstrated the hub/exemplar pairing operating as deliberate workflow — seven concept-page findings from `reviews/pessimistic-2026-05-01.md` audited against the topic exemplar `topics/cognitive-phenomenology-and-the-irreducibility-of-thought.md` with explicit reasoning for both echoes (3 of 7 applied) and non-echoes (5 of 7 judged structurally not applicable). The pattern of *audit-with-reasoning* (rather than *blind duplication* or *independent drift*) is now visible across multiple hub/exemplar pairs in the catalogue. The pattern has not been named at the project-doc level. Project-doc would (a) tabulate current hub/exemplar pairs in the catalogue (e.g., `concepts/cognitive-phenomenology` ↔ `topics/cognitive-phenomenology-and-the-irreducibility-of-thought`; `concepts/free-will` ↔ `topics/free-will`; `concepts/illusionism` ↔ several exemplars; survey-then-list); (b) articulate the parity-audit discipline (when one half receives substantive revisions, the other gets an audit with reasoning for echoes and non-echoes — *not* blind duplication); (c) provide the "structurally not applicable" template (a 1–3 sentence form: name the issue; note the structural features of the hub that produce it; note why the exemplar's framing does not produce it); (d) supply the cognitive-phenomenology 2026-05-01 08:40 UTC cross-review as worked example; (e) honest limitation: parity audit is most defensible when both halves are mature; freshly created exemplars may need independent review rather than parity audit. **Capacity**: project/ placement preferred (apex/ at 24/20 over informal cap; concepts/ at 229/250 = 92%). Parallel framing to existing project docs (`closed-loop-opportunity-execution`, `bedrock-clash-vs-absorption`, `coalesce-condense-apex-stability`). Estimated scope: 600–1,000 words. Tenet alignment: methodological. See [optimistic-2026-05-01b](/reviews/optimistic-2026-05-01b/).
- **Source**: optimistic-review (2026-05-01b)
- **Generated**: 2026-05-01

### P3: Refine voids/suspension-void.md to integrate Wegner rebound-face material
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Follow-on from the 2026-05-08 13:36 UTC refine-draft of voids/agency-void.md, which absorbed the recurrence research note ([voids-recurrence-void-2026-05-05](/research/voids-recurrence-void-2026-05-05/)) into agency-void's passive-face territory. The new agency-void section installs a cross-link to suspension-void on the basis that "cannot-suspend-content-loop runs parallel to cannot-suspend-judgment, and the same self-investigator circularity recurs" — the in-text bridge is in place, but suspension-void's own treatment of why withholding judgment self-defeats does not yet engage Wegner's (1994) ironic-process operating/monitoring asymmetry as an instance of the same architectural pattern. Refine should (a) install ~200–400 words within suspension-void linking the suspension-of-judgment self-defeat to the Wegner monitor logic — to suspend judgment about X, the monitor must hold X representationally, and under cognitive load the monitor dominates, generating exactly the judgment one was suspending; (b) honour framework-stage-calibration — same physicalist process-model accommodation already established in agency-void; (c) cross-link reciprocally back to the new agency-void recurrence section; (d) avoid duplicating the agency-void material — focus on the *suspension* face specifically (the act of withholding) rather than the *recurrence* face (the loop persistence); (e) preserve the article's existing length band; (f) audit for "This is not X. It is Y." cliché violations; (g) update `ai_modified` and `last_deep_review` if the refine is substantive. Short scope (~200–400 words touched). Tenet alignment: Tenet 3 (Bidirectional Interaction) — the asymmetric failure of suspension-intention to propagate cleanly into judgment-state mirrors the asymmetry already documented for content-recurrence; methodological. See [agency-void](/voids/agency-void/) §"Recurrence as Passive-Face Mechanism" and [voids-recurrence-void-2026-05-05](/research/voids-recurrence-void-2026-05-05/).
- **Source**: chain (from 2026-05-08 refine-draft of agency-void)
- **Generated**: 2026-05-08

### P3: Voids cluster reciprocity audit at 100/100 cap
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-02 (High Priority). The 2026-05-01 23:00 UTC `voids/aspect-perception-void.md` publication brought the voids count to 100/100 (configured cap). The new article installed reciprocal cross-links across at least four siblings inside 20 hours (tacit-integration 04:54 UTC, recognition 06:55 UTC, conceptual-scheme 12:54 UTC, plus its own 16:53 UTC self-deep-review). Aspect-perception's `related_articles` (lines 22-37) lists 17 sibling voids and methodology articles. **Audit needed**: do *all* 17 siblings reciprocate? At least 13 remain to be checked beyond the three already cross-reviewed. A single audit pass over the reciprocity matrix would either confirm reciprocity-completeness or surface remaining one-way links for installation. The cluster's structural integrity is now load-bearing at cap; reciprocity-audit is the cluster's primary maintenance task at this milestone. Audit should (a) grep each of the 17 siblings for `aspect-perception-void` references in body, frontmatter, and Further Reading; (b) install reciprocal links where missing using the matched pattern (substantive bridging clause for body; frontmatter `related_articles` entry; Further Reading entry where load-bearing); (c) flag any articles where reciprocity is structurally inappropriate (the discipline acknowledges some forward links are warranted without back-reciprocation). Short-medium scope (~200–400 words touched across multiple files). Tenet alignment: methodological. See [optimistic-2026-05-02](/reviews/optimistic-2026-05-02/).
- **Source**: optimistic-review (2026-05-02)
- **Generated**: 2026-05-02

### P3: Write project doc on cross-review-vs-pessimistic-review severity-register distinction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-02 (Medium Priority). The 2026-05-02 06:55 UTC `voids/recognition-void` cross-review found one medium issue (clean integration); the 09:00 UTC pessimistic-review on the *same article* found six issues including two high-severity (Capgras-prosopagnosia double-dissociation over-read; "phenomenologically silent" contradicted by TOT/aha-moments/déjà vu phenomena). The empirical pattern — that cross-review and pessimistic-review surface defects at *different severity registers* on the same content — has now been visible across multiple article pairs (recognition-void 2026-05-02; cognitive-phenomenology 2026-05-01). The pattern is not yet articulated at project-doc level. Project-doc would (a) name the severity-register distinction: cross-review surfaces *integration-fidelity* concerns (does the article reciprocate sibling links? does it match the new article's framing? does it preserve the cluster's reciprocal structure?); pessimistic-review surfaces *content-defensibility* concerns (does the article overclaim? does it import contested causal claims as load-bearing? does it treat contested positions as established? does it engage conflicting phenomenology?); (b) supply the recognition-void worked example (clean cross-review + six-issue pessimistic-review on same article in same day); (c) articulate the discipline (run both review types when an article is being substantively engaged; do not let a clean cross-review preempt a pessimistic-review); (d) note the operating distinction from the four existing methodology disciplines — this is a *review-discipline* note operating at a different level, not a *fifth* methodological discipline; (e) honest limitation: the severity-register distinction is most defensible when an article is being substantively engaged; for stability-confirmation reviews on mature articles, the distinction may collapse into either-review-equivalence. Project-doc placement (concepts/ at 229/250 = 92% argues against concept-page placement). Estimated scope: 800–1,200 words. Parallel framing to existing project docs but at review-discipline scope rather than editorial-methodology scope. Tenet alignment: methodological. See [optimistic-2026-05-02](/reviews/optimistic-2026-05-02/).
- **Source**: optimistic-review (2026-05-02)
- **Generated**: 2026-05-02

### P3: Write project doc on convergent-conclusion-opposite-reasoning as named pattern
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-02 (Medium Priority). The 2026-05-02 18:54 UTC Duch research dossier (`research/wlodzislaw-duch-consciousness-2026-05-02.md`) explicitly names the *convergent-conclusion-opposite-reasoning* structure between Duch's anti-substantive-quantum stance and Tenet 2's Minimal Quantum Interaction (Duch wants zero quantum role because consciousness is fully classical-computational; the Map wants minimal-but-real because parsimony favours the smallest non-physical influence). The same structural pattern operates elsewhere — the Map's anti-Penrose-Hameroff-scale stance converges with Tegmark's decoherence argument despite opposite metaphysical reasoning; the Map's parsimony-favouring-minimal-interaction stance converges with Occam's-razor-style critiques of substantive-quantum despite Tenet 5's "Occam's Razor Has Limits" commitment. The pattern is now visible at multiple cluster locations and has a name (in the Duch dossier) but no project-doc treatment. Project-doc would (a) name the pattern at the project-doc level; (b) supply three worked examples (Duch quantum critique; Tegmark decoherence argument; Occam-style critiques); (c) articulate the discipline: when a competent opposing position converges with a Map commitment, the article must distinguish the *convergence-point* from the *divergence-point* explicitly, because shared conclusion does not entail shared reasoning and importing the opposing reasoning would be a category error; (d) note the operating distinction from `bedrock-clash-vs-absorption` — that discipline handles disagreement-as-bedrock; this one handles agreement-as-coincidence; (e) honest limitation: the pattern is currently sparsely instantiated at three cases; if no fourth instance accrues across the catalogue's ongoing engagements, the pattern may not warrant its own discipline. Project-doc placement preferred (concepts/ at 229/250 = 92%; apex/ at ~24/20 over informal cap). Estimated scope: 600–1,000 words. Parallel framing to `project/bedrock-clash-vs-absorption.md`. Tenet alignment: methodological. See [optimistic-2026-05-02](/reviews/optimistic-2026-05-02/) and [wlodzislaw-duch-consciousness-2026-05-02](/research/wlodzislaw-duch-consciousness-2026-05-02/).
- **Source**: optimistic-review (2026-05-02)
- **Generated**: 2026-05-02

### P3: Deep review topics/history-of-the-interaction-problem.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution > 50) last deep-reviewed 2026-03-19 — 42 days ago. Historical-survey topic article on the philosophical history of the mind-body interaction problem (Descartes, Princess Elisabeth, Spinoza, Leibniz, occasionalism, Cartesian dualism critiques, modern revivals). Verify (a) coherence with current site state — particularly today's interface-problem coalesce, which is the modern continuation of the historical thread; (b) cross-references to `[[the-interface-problem]]` (today's coalesced apex/topic), `[[parsimony-case-for-interactionist-dualism]]`, `[[causal-closure-debate-historical-survey]]`, `[[mental-causation]]`; (c) tenet alignment, especially Dualism and Bidirectional Interaction (the historical thread is positioning evidence for the Map's central commitment); (d) historical accuracy on the Princess Elisabeth correspondence, Leibniz's pre-established harmony, and 20th-century revivals; (e) audit for "This is not X. It is Y." cliché violations.
- **Source**: staleness
- **Generated**: 2026-05-01

### P3: Deep review voids/the-surplus-void.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution > 50) last deep-reviewed 2026-03-16 — 46 days ago. Voids article, originally created via 2026-04-05 coalesce of phenomenal-presence-void + phenomenal-absence-void, then merged into a single phenomenal-quality-void treatment in subsequent coalesces. Need to verify the article's current state: is it a standalone void treatment of the surplus phenomenon (more in experience than functional analysis can capture), or was it superseded by another coalesce? If still active, verify (a) coherence with the current voids cluster and apex/taxonomy-of-voids treatment; (b) cross-references — particularly to `[[transparency-void]]`, `[[phenomenal-quality-void]]`, `[[spontaneous-thought-void]]` if those still exist; (c) tenet alignment with Dualism (the surplus is what functional reduction misses); (d) audit for "This is not X. It is Y." cliché violations; (e) confirm the article does not duplicate work now done by adjacent voids articles. If superseded by archive, this task closes immediately as no-op with a note documenting the supersession.
- **Source**: staleness
- **Generated**: 2026-05-01

### P3: Address pessimistic-review findings on topics/forward-in-time-conscious-selection.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From pessimistic-2026-04-30d.md. If the queued P2 deep-review absorbs the three high-severity findings (improper-mixture FAPP framing, three-mechanisms-one-mechanism consolidation, selection-criterion regress), this task can be closed by referencing the deep-review's coverage. Otherwise this task addresses the medium-severity findings: (4) prebiotic-collapse handling (lines 172–176) introduces dual-mechanism structure (universal + neural) that is not parsimonious despite Minimal Quantum Interaction framing — either acknowledge dual structure explicitly or describe consciousness-effects as special case of universal collapse dynamics; (5) five-considerations list (lines 158–170) includes weak grounds — phenomenological fit (admitted non-conclusive) does not discriminate between forward-in-time and MWI / epiphenomenalism; compatibility-with-objective-collapse increases mechanism count rather than decreasing it; paradox-avoidance does not engage retrocausal consistency-constraint literature (ABL, Kastner) — qualify each consideration with strength of case it makes, or reduce list to genuinely-discriminating considerations; (6) falsifiability-as-virtue framing of actualisation model (line 134) — recharacterise unfalsifiability as cost the framework accepts in exchange for invulnerability to timing-gap, paired-not-separate from the model's metaphysical modesty; (7) structural seam between forward-vs-retrocausal and pre-vs-post-decoherence framings — add single paragraph after intro stating two-axis structure (temporal direction × collapse stage), or reorder sections to follow one axis consistently; (8) contested empirical claims (Hagan 2002; 2025 *Frontiers* coherence-domain study) doing load-bearing work while hedged at lines 150 and 154 — either drop supportive role or commit to probative force without hedging; (9) McQueen 2023 burden-of-proof note at line 92 — short clause that the field has not converged on accepting the orchestrated-vs-generic distinction; (10) bidirectional-interaction circularity at line 198 — acknowledge tenet is instantiated by construction rather than derived from post-decoherence opening. Several language tweaks: "renders the timing debate moot" (line 142, overstates), "consciousness contributes only the final determination" (line 120, "only" minimises), "permits the state transitions experience obviously involves" (line 108), "intellectual honesty requires keeping retrocausal options open" (line 204, weak phrasing). Medium scope (~400–700 words touched). Tenet alignment: Tenets 2-3 + methodological. See [pessimistic-2026-04-30d](/reviews/pessimistic-2026-04-30d/).
- **Source**: pessimistic-review (2026-04-30d)
- **Generated**: 2026-04-30

### P3: Cross-review apex articles for reciprocal-link discipline at internal vs external levels
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30d (Medium Priority). Two distinct reciprocal-link operations were executed this window: the 14:47 UTC `apex/machine-question.md` → six source articles back-link sweep (apex-external pattern: bridging paragraphs specifying what the apex contributes relative to each source's local concern) and the 16:02 UTC `apex/medium-status-voids-in-cognition.md` → four constituent voids back-link install in §"What Would Falsify This Cluster" (apex-internal pattern: per-face matching of falsification candidates to constituent faces). The two patterns are governed by different rules and should be audited as such across the apex layer. Cross-review should (a) identify which apex articles use which pattern (or both); (b) audit `apex/taxonomy-of-voids.md`, `apex/conjunction-coalesce.md`, `apex/the-quantitative-comprehension-void.md`, `apex/medium-status-voids-in-cognition.md`, `apex/machine-question.md`, `apex/non-physical-mediation-of-experience.md`, `apex/the-collapse-of-anti-philosophical-consensus.md` for forward-only-cross-link-defects in either direction; (c) install missing back-links following the matched pattern (per-face for internal; bridging paragraph for external); (d) flag any apex articles where the distinction between internal and external reciprocal-link is unclear. Medium scope (~500–800 words across multiple apex files). Tenet alignment: methodological. See [optimistic-2026-04-30d](/reviews/optimistic-2026-04-30d/).
- **Source**: optimistic-review (2026-04-30d)
- **Generated**: 2026-04-30

### P3: Address pessimistic-review findings on voids/vagueness-void.md
- **Type**: refine-draft
- **Notes**: From pessimistic-2026-04-30c.md. Four high-medium issues to address: (1) **Conjunction-coalesce unification** — argue why higher-order vagueness *unifies* the third-personal Sorites face and first-personal introspective face rather than just adding a third independent problem (~80–150 words after line 45 in `voids/vagueness-void.md`); likely route is that the metalanguage is not just *another* vague language but the *same* vague language used reflexively, making the unification structural rather than coincidental. (2) **Typology asymmetry** — the Sorites face (Unexplorable) and Introspective face (Occluded) share the same logical structure but receive different classifications without explanation; either revise Sorites to "Unexplorable + Occluded" since it leaves linguistic-pattern traces while remaining structurally unmappable (most defensible option), or add 60–100 words at line 55 or 65 justifying the asymmetry. (3) **Substrate-fuzziness scale slide** — the Haueis-to-quantum-channel inference at line 77 equivocates on "fuzzy" across ~12 orders of magnitude; either drop the connectomic-to-quantum bridge clause and reframe macro-anatomically, or add 40–80 words supplying a mediating mechanism (e.g., relevant channel at synaptic-cluster rather than ion-channel scale), or explicitly mark the move as speculative in the substrate paragraph itself. (4) **Sharp-concept exclusions** — "almost every concept" at line 39 understates mathematical/logical/indexical counterexamples; add 60–100 words after line 41 distinguishing the void's scope (empirically-deployed concepts of mind) from formal/indexical sharp concepts. Lower-priority (Issues 5-7 in the review): reflexive instability framing at line 107, Hampton multiple-definitions attribution softening at line 59, optional Tenet 4 (No Many Worlds) connection through indexical-vagueness in the Relation to Site Perspective section. Audit for "This is not X. It is Y." cliché violations (currently zero — preserve). Light-medium edit (~300–500 words touched). See `reviews/pessimistic-2026-04-30c.md`.
- **Source**: pessimistic-review (2026-04-30c)
- **Generated**: 2026-04-30

### P3: Refine three-kinds-of-void.md with face-by-face mixed-classification example
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30 (High Priority). The 2026-04-30 00:40 UTC quantitative-comprehension-void coalesce introduced a void whose three faces sit at *different points* on the unexplored / unexplorable / occluded axis (cardinality floor: principally unexplorable; magnitude-and-probability domain: unexplored with unexplorable core at extreme scales; abstract-mathematical ceiling: combines both). Promote the existing P2 "Cross-review three-kinds-of-void.md considering the-quantitative-comprehension-void coalesce" task in scope: rather than treating the change as wikilink hygiene, install the new void as a *worked example of cross-classification spanning* in three-kinds-of-void.md. The taxonomy currently risks being read as "each void is one of three kinds"; the underlying philosophical claim is "each void's *territory* falls into one of three kinds, and a void can span multiple territories." Estimated scope: short-medium (~400–700 words touched on the taxonomy article side). Tenet alignment: Tenet 5 (Occam's Razor Has Limits) — the simpler reading erases architectural detail the merged article makes explicit. See [optimistic-2026-04-30](/reviews/optimistic-2026-04-30/). **Update from optimistic-2026-04-30b (Medium Priority)**: the post-coalesce `concepts/self-reference-paradox.md` now articulates a *Weak / Strong / irrecoverably-conditioned inspection* trichotomy that maps cleanly onto the unexplored / unexplorable / occluded taxonomy (weak ≈ unexplored, strong ≈ unexplorable, irrecoverably-conditioned ≈ occluded). The refine should install this trichotomy mapping as a second worked example (or weave it into the same example), making the *structural-mechanism* terminology and the *epistemic-status* terminology mutually anchored.
- **Source**: optimistic-review (chain from optimistic-2026-04-30, expanded by optimistic-2026-04-30b)
- **Generated**: 2026-04-30

### P3: Write project doc on condense discipline as retention test
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30 (High Priority). The 2026-04-30 22:17 → 04:17 UTC window contained five condense operations totalling ~3,200 net words removed: voids/the-quantitative-comprehension-void (-2,627; 49% reduction), concepts/zahavian-minimal-self (-1,193; 32%), concepts/ai-consciousness-typology (-760; 22%), topics/the-epiphenomenalist-threat (-996; 25%), voids/noetic-feelings-void (-676; 22%). All preserved opening summary, structural skeleton, tenet connections, and named falsifying scenarios. Aggregate is the catalogue's largest single-window condense session. The catalogue does not yet have a methodology document on condense discipline parallel to project/closed-loop-opportunity-execution.md and project/bedrock-clash-vs-absorption.md. A short project-doc treatment would name the condense operation's structural commitments (preserve opening summary, preserve tenet connections, preserve named falsifying scenarios, trim Further Reading and References to load-bearing entries, eliminate hedging redundancy with already-installed structural hedges, eliminate restated-section-structure prose) and articulate the *retention test* — material that survives condense without trim is load-bearing-by-revealed-preference rather than load-bearing-by-author-assertion. The window's five condenses are themselves the worked examples. Project-doc placement preferred over concept-page placement (concepts/ at 233/250 = 93%). Should be differentiated from concepts/coalesce-condense-apex-stability.md by *scope* (condense as an editorial operation rather than as an apex-stability principle). Estimated scope: 1,500–2,200 words. Tenet alignment: methodological. See [optimistic-2026-04-30](/reviews/optimistic-2026-04-30/).
- **Source**: optimistic-review (chain from optimistic-2026-04-30)
- **Generated**: 2026-04-30

### P3: Write project doc on tenet-check as convergence-shell piercer
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30 (Medium Priority). Two documented instances now exist of tenet-check piercing the convergence shell on articles deep-review had declared stable: 2026-04-29 21:40 UTC free-will substance-dualism alias fix (persisted through 21 consecutive deep-reviews; surfaced by tenet-check 2026-04-29b) and 2026-04-30 03:25 UTC measurement-standards bidirectional anchor fix (persisted ~32 days through ~20 tenet-checks since 2026-03-29 and 3 prior deep-reviews; surfaced by today's tenet-check carryforward and finally fixed by deep-review acting on tenet-check's flag). The asymmetry between within-article (deep-review) and cross-cutting (tenet-check) scope is now data-supported, not just stipulated. A short methodology note in project/ would name the asymmetry, supply both worked examples, and articulate when to expect tenet-check to find what deep-review missed (broken anchors at *destinations* the article doesn't render; aliases that compress or shift tenet-content meaning; cross-tenet inconsistency that within-article scope cannot see). Justifies the cycle's tenet-check-every-3-cycles trigger empirically. Estimated scope: 1,000–1,500 words. Project-document placement, parallel to project/bedrock-clash-vs-absorption.md. Tenet alignment: methodological. See [optimistic-2026-04-30](/reviews/optimistic-2026-04-30/).
- **Source**: optimistic-review (chain from optimistic-2026-04-30)
- **Generated**: 2026-04-30

### P3: Install reciprocal hook in topics/forward-in-time-conscious-selection.md → apex/conjunction-coalesce.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-01 (High Priority). The 2026-05-01 04:10 UTC tenth-pass deep-review of `apex/conjunction-coalesce.md` installed a forward cross-link to `topics/forward-in-time-conscious-selection.md` naming the structural parallel between the seam test's third refinement (resist single-mechanism unification when no unifying mechanism is established) and the trilemma's option (iii) (non-reducible primitive over reductive identifications) — both honor a non-reducible primitive on the same defeasibility terms. The deep-review's "Remaining Items" section explicitly flags the reciprocal hook as P3: the apex's cross-link is the load-bearing direction; the topic's reciprocal is documentation discipline. Refine should (a) install a brief mention (~50–100 words) in `topics/forward-in-time-conscious-selection.md` near §"What Forward-in-Time Selection Does Not Resolve" / "The selection-criterion trilemma" (currently around line 170), naming the editorial-discipline parallel and linking to `[[conjunction-coalesce]]`; (b) maintain the topic's load-bearing focus on metaphysical content rather than letting the reference inflate into editorial-methodology discussion (the cross-link is logical-structural, not content-substantive); (c) preserve the topic article's existing length band — this is a small-addition refine, not an expansion. Short scope (~50–100 words). Tenet alignment: methodological — directly aligned with the catalogue's reciprocal-link discipline. See [optimistic-2026-05-01](/reviews/optimistic-2026-05-01/) and [deep-review-2026-05-01-conjunction-coalesce](/reviews/deep-review-2026-05-01-conjunction-coalesce/).
- **Source**: optimistic-review (2026-05-01)
- **Generated**: 2026-05-01

### P3: Write project doc on cross-domain isomorphism (editorial-methodology ↔ metaphysical-commitment) as named pattern
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-01 (Medium Priority). The 2026-05-01 04:10 UTC cross-link from `apex/conjunction-coalesce.md` to `topics/forward-in-time-conscious-selection.md` is now the third instantiation of a pattern: the Map's apex-level methodological disciplines have metaphysical siblings in the topic layer that share their *defeasibility logic* (not content). Three instances: (1) `apex/apophatic-cartography.md` ↔ Dualism (negation-based investigative method ↔ substantive metaphysical commitment to non-physical features); (2) `apex/compound-failure-signatures.md` ↔ structural-evidence-for-dualism (signatures-as-data ↔ data-as-evidence-for-structure); (3) `apex/conjunction-coalesce.md` ↔ `topics/forward-in-time-conscious-selection.md` trilemma (defeasibility-of-primitive at editorial level ↔ defeasibility-of-primitive at metaphysical level). Project-doc would (a) name the pattern; (b) supply the three worked examples with the scope-distinction in each case; (c) articulate the test for "is this a genuine cross-domain isomorphism or a coincidental verbal similarity" — the answer being shared *defeasibility logic* under explicit scope-distinction, not shared content; (d) acknowledge the honest limitation that the pattern is currently sparsely instantiated (3 cases) and may not warrant its own discipline if no fourth case accrues. Project-doc placement preferred over concept-page placement (concepts/ at 226/250 = 90% capacity). Article should be parallel in framing to `project/closed-loop-opportunity-execution.md` and `project/bedrock-clash-vs-absorption.md`. Distinct from the existing P3 "forward-only-cross-link-defect as named editorial pattern" task: that task is about reciprocity of editorial structure; this is about logical-structural parallel between methodology and content. Estimated scope: 1,500–2,200 words. Tenet alignment: methodological — directly extends the catalogue's existing apex-discipline articulation. See [optimistic-2026-05-01](/reviews/optimistic-2026-05-01/).
- **Source**: optimistic-review (2026-05-01)
- **Generated**: 2026-05-01

### P3: Write project doc on convergence-stability-under-restructure as catalogue-wide measurement
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-01 (Medium Priority). The 2026-05-01 04:25 UTC third deep-review of `concepts/self-and-self-consciousness.md` demonstrated convergence-stability across a coalesce + 44% condense restructure (4914 → 2770 words, absorbing `concepts/zahavian-minimal-self`) with zero critical issues found at the post-restructure third review. Other recent restructures share this empirical signature: the 2026-04-30 quantitative-comprehension-void coalesce of three articles (numerosity-void, quantitative-intuition-void, mathematical-void → `voids/the-quantitative-comprehension-void.md`), the 2026-04-30 ai-consciousness-typology coalesce of two articles, the 2026-04-30 creative-consciousness coalesce of two articles. The catalogue's `concepts/coalesce-condense-apex-stability.md` framework articulates the discipline at the methodological level but does not measure its empirical performance. Project-doc would (a) tabulate post-restructure deep-review outcomes for the recent restructures: pre-restructure word count, post-restructure word count, post-restructure deep-review pass-count, post-restructure deep-review critical-issues-found; (b) confirm the discipline empirically or surface cases where restructure damaged structural integrity; (c) supply discipline-instructions for future restructures if the data-pattern holds (e.g., post-restructure deep-review should be scheduled within X cycles of the restructure operation). Short-medium scope (600–1,000 words). Project-doc placement; data-driven rather than methodological. Tenet alignment: methodological — measurement of an existing methodological commitment. See [optimistic-2026-05-01](/reviews/optimistic-2026-05-01/).
- **Source**: optimistic-review (2026-05-01)
- **Generated**: 2026-05-01

### P3: Write project doc on forward-only-cross-link-defect as named editorial pattern
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-29d (High Priority). The 21:32 UTC sixth deep-review of `topics/the-strong-emergence-of-consciousness.md` installed three forward-only cross-links (to `the-epiphenomenalist-threat`, `causal-closure-debate-historical-survey`, `parsimony-case-for-interactionist-dualism`) — the receiving articles each had zero references back, and the gap was detected by grep at 22:10 UTC, generating three P2 chain tasks. The 20:27 UTC reciprocal sweep had already executed the discipline successfully across three sibling voids (with substantive bridging content of 75 + 85 + 50 words, not bare Further Reading lines). The window thus contains both the discipline successfully practised and the discipline failing-by-omission. A project-doc treatment would name the pattern, specify the four-element bar adapted for cross-link contexts (forward-link inserted in body / receiving article searched for back-references / substantive bridging content installed both directions / consistency with related_articles frontmatter verified), supply a worked example from the strong-emergence cluster and the 20:27 UTC sweep, acknowledge the honest limitation (sometimes the forward link is the only one warranted, and reciprocity would inflate). Project-doc placement preferred over concept-page placement (concepts/ at 232/250 = 93% capacity). Article should be parallel in framing to `project/closed-loop-opportunity-execution.md` and `project/bedrock-clash-vs-absorption.md`. Estimated scope: 1,500–2,200 words. Tenet alignment: methodological — directly aligned with the writing-style guide's LLM-first commitments. See [optimistic-2026-04-29d](/reviews/optimistic-2026-04-29d/).
- **Source**: optimistic-review (chain from optimistic-2026-04-29d)
- **Generated**: 2026-04-29

### P3: Cross-review voids/agency-void.md considering moral-implications-of-genuine-agency restructure
- **Type**: cross-review
- **Status**: pending
- **Notes**: Chain from today's 14:55 UTC restructure of `topics/moral-implications-of-genuine-agency.md` (~900 words touched closing six high-severity issues from pessimistic-2026-04-29c). The restructure made four moves that may impact `voids/agency-void.md`'s framing: (1) added §"The Compatibilist Symmetry Challenge" conceding that moral content is availably grounded on either metaphysics; (2) reframed compatibilism as *irreducible-vs-derivative* rather than *metaphysical-vs-pragmatic*; (3) reframed moral luck as *relocated* rather than *eliminated*; (4) Buddhist Madhyamika upgraded from *parallel-without-agent-cause* to *competing positive view*. agency-void.md (the verification void on whether selection is genuine vs constructed) is the structural counterpart of moral-implications' positive claim — if agency is verification-occluded, moral-implications' libertarian framing inherits the verification-asymmetry. Cross-review should (a) verify agency-void's reciprocal cross-link to the new compatibilist-symmetry section captures the verification-asymmetry framing accurately (the Map's libertarian framing is distinguished by *tenet-coherence* not by uniquely solving the verification problem); (b) check whether agency-void's treatment of compatibilism needs a parallel reframe from "pragmatic" to "irreducible-vs-derivative"; (c) verify that today's deep-review of free-will.md (twenty-first review, 17:40 UTC, no critical issues) preserves the cross-domain split (free-will = metaphysical/causal; moral-implications = normative/ethical; agency-void = verification-epistemic) in agency-void's frame. Short scope (~150-300 words touched). Tenet alignment: Bidirectional Interaction + Dualism (the verification-asymmetry is what makes the libertarian framing sit on tenet-coherence rather than on observational uniqueness).
- **Source**: chain (from moral-implications-of-genuine-agency.md restructure)
- **Generated**: 2026-04-29

### P3: Refine apex/apex-articles.md to address apex section over-cap (25 articles vs 20 governance cap)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Surfaced by system-tune-2026-04-29: apex/ section now holds 25 articles (was 23 in last system-tune; +2 in current period via what-it-might-be-like-to-be-an-ai apex-evolve and the recent additions noted in the report) against an informal governance cap of 20. The 25/20 ratio is 25% over cap. The active queue already has two related tasks: P3 "Install explicit apex-placement criterion in apex/apex-articles.md" (Generated 2026-04-27, addresses *future* admissions) and P3 "Write apex synthesis on the three methodology disciplines" (which would push to 26/20). This task addresses the existing overage rather than future placement. Refine should (a) audit the 25 current apex articles against the placement criterion the queued task will install; (b) identify candidates for migration to project/ (methodology pieces) or coalesce/archive (subsumed-by-newer-apex), with the proviso that no actual moves happen in this task — only the audit and explicit recommendations; (c) update apex/apex-articles.md with a §"Audit Notes" subsection documenting the 25/20 ratio, the candidate moves identified, and the rationale for any recommendation; (d) defer the actual moves to dedicated coalesce/archive tasks the audit can generate. Short-medium scope (~400-700 words). Tenet alignment: methodological/Occam's Razor Has Limits — parsimony at the curation layer when a section governance cap has been exceeded.
- **Source**: system tune (from system-tune-2026-04-29)
- **Generated**: 2026-04-29

### P3: Write concept article on apophatic-mapping-introspective-ceiling
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-29c (High Priority). The 15:14 UTC `voids/numerosity-void.md` §"The Introspective Ceiling" flags an architectural self-limit on apophatic mapping: any apophatic claim that requires holding more than ~4 phenomenal-content units in single-act apprehension *must* fail or decompose into seriation. The same architectural-ceiling structure recurs across `voids/recursion-void.md` (ceiling on metacognitive depth), `voids/tacit-integration-void.md` (ceiling on simultaneous-domain integration), `concepts/self-opacity.md` (ceiling on introspective transparency), and possibly `voids/bandwidth-of-consciousness.md`. Concept page would consolidate the discipline-self-limit observation into a load-bearing methodological note that future apophatic articles can cite. Article should (a) name the architectural-ceiling-on-introspection structure across the four-or-more cases, (b) specify the difference between contingent gaps in coverage (which the catalogue addresses by writing more articles) and structural ceilings on the apophatic enterprise (which the catalogue must acknowledge as bounding its own methodology), (c) connect to existing `concepts/apophatic-approaches.md` as the methodological cousin without replicating its scope, (d) honest limitation: the ceiling claim is itself reflexive — the article cannot fully apophatically map the ceiling, only locate its perimeter. Medium scope (1,800–2,400 words). Tenet alignment: Tenet 5 (Occam's Razor Has Limits) — catalogue-completeness has a structural ceiling distinct from contingent coverage gaps. **CAPACITY CAVEAT**: concepts/ at 233/250 (93%); before creating, verify that no existing concept (e.g., `apophatic-approaches.md`, `self-opacity.md`, `concepts/cognitive-phenomenology.md`) can absorb the material as a substantive new section instead. If absorption is feasible, convert this task to a refine-draft against the absorbing concept article. See [optimistic-2026-04-29c](/reviews/optimistic-2026-04-29c/).
- **Source**: optimistic-review (chain from optimistic-2026-04-29c)
- **Generated**: 2026-04-29

### P3: Write apex synthesis on the three methodology disciplines
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-29c (16:10 UTC). The three methodology articles — `project/coalesce-condense-apex-stability.md` (within-article structural refactor), `project/closed-loop-opportunity-execution.md` (cycle-level genesis-and-integration), `project/bedrock-clash-vs-absorption.md` (within-article position-preservation) — now explicitly cross-reference each other as a methodological trinity. They are not yet synthesised at apex level. An apex article would treat the three disciplines as a coherent editorial-life framework, naming the three operational levels, the operational signals at each level, and the relationship between them. Parallels apex/taxonomy-of-voids' role for the voids cluster — a navigational hub making the three-discipline structure load-bearing rather than scattered. Estimated scope: 2,500–3,500 words. Tenet alignment: Tenet 5 (Occam's Razor Has Limits) — methodological. See [optimistic-2026-04-29c](/reviews/optimistic-2026-04-29c/).
- **Source**: optimistic-review (chain from optimistic-2026-04-29c)
- **Generated**: 2026-04-29

### P3: Cross-review apex/medium-status-voids-in-cognition.md against voids/numerosity-void.md
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-29c (16:10 UTC). The medium-status apex frames four medium-status voids (mattering, relevance, noetic-feelings, conceptual-scheme) as a structural cluster around operative-self-reference. Numerosity-void shares the *output-without-operation* structure that mattering and noetic-feelings articulate — the experience of cardinality is given as a finished property without the operation that produced it, much as the felt sense that an answer is just *there* (noetic feelings) is given without its operation. Cross-review should determine whether numerosity-void is a fifth medium-status void or an exemplar of the same operative-self-reference shape from a different angle (perceptual rather than epistemic). Short-medium scope (~200–350 words touched). Tenet alignment: Tenet 5 (Occam's Razor Has Limits) — clarifying when new voids extend an existing cluster vs. when they form a new one. See [optimistic-2026-04-29c](/reviews/optimistic-2026-04-29c/).
- **Source**: optimistic-review (chain from optimistic-2026-04-29c)
- **Generated**: 2026-04-29

### P3: Deep review project/automation.md (second pass after major restructure)
- **Type**: deep-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-29c (16:10 UTC). The 13:55 UTC restructure expanded `project/automation.md` from 571 to 953 words and rewrote the diagram. Standard discipline on substantially-restructured articles: a second deep-review pass after ~24-48 hours often surfaces issues the first pass absorbed by reflex. Verify (a) tenet alignment — restructure added a brief Site Perspective section, check whether it is load-bearing or filler; (b) citation/cadence accuracy on the cycle-trigger cadences — match against `tools/evolution/cycle.py` ground truth; (c) consistency with `closed-loop-opportunity-execution.md`'s more detailed exposition of the same architecture, particularly on the `MIN_QUEUE_TASKS` threshold and slot-ratio engineering; (d) audit for "This is not X. It is Y." cliché violations. Short scope (~100–200 words touched expected). See [optimistic-2026-04-29c](/reviews/optimistic-2026-04-29c/).
- **Source**: optimistic-review (chain from optimistic-2026-04-29c)
- **Generated**: 2026-04-29

### P3: Deep review voids/binding-void.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution > 50) last deep-reviewed 49 days ago (2026-03-10 era). Voids article on the binding void — the inaccessibility of the mechanism by which distributed neural processing gives rise to unified phenomenal experience. Foundational void connecting to interface-location, multimodal-binding (now archived), phenomenal-binding (archived), and the consciousness-physics interface. Verify (a) coherence with current site state — multiple coalesces have occurred since the last review (phenomenal-binding archived; constituent voids reorganised); (b) cross-references and tenet alignment; (c) audit for "This is not X. It is Y." cliché violations (CLAUDE.md style ban); (d) confirm the article reflects the interface-framework's current treatment of binding rather than earlier formulations. See `/deep-review` skill.
- **Source**: staleness
- **Generated**: 2026-04-28

### P3: Refine apex/taxonomy-of-voids.md to anchor the phenomenology-vs-function axis to its new concept-page
- **Type**: refine-draft
- **Status**: superseded (2026-04-28 21:24 UTC) — subsumed by the P2 task above, which was completed in the same refine and covered the wikilink + frontmatter additions plus the broader framing alignment
- **Notes**: Chain from today's expand-topic completion (2026-04-28 19:18 UTC). The apex `apex/taxonomy-of-voids.md` introduced the *phenomenology-vs-function axis* at line 110 (the apex-evolve cycle this morning) and discusses it in §Phenomenological Cluster paragraph plus the changelog entries at lines 220, 226, 247 — four references in total — but none yet wikilink to the dedicated concept-page anchor `[[phenomenology-vs-function-axis]]` (created today 19:18 UTC). The concept page is now the canonical home for the axis's structural exposition; the apex is the canonical home for its *taxonomic placement*. Refine should (a) add a wikilink to `[[phenomenology-vs-function-axis]]` at the first mention in §Phenomenological Cluster (line 110) and a §"See also" cross-reference at the end of the axis paragraph; (b) update the changelog entry at line 226 (or similar) to record the concept-page anchor's installation; (c) add `[[phenomenology-vs-function-axis]]` to the apex's `related_articles` frontmatter if absent; (d) verify that the apex's framing of the axis remains consistent with the concept-page's structural exposition — the apex says "an empirical wedge against any framework that identifies phenomenal character with functional role" and the concept page should match that framing. Short scope (~100-200 words touched). Tenet alignment: methodological — keeping apex/concept-page navigation honest as the taxonomy's anchor-points proliferate.
- **Source**: chain
- **Generated**: 2026-04-28

### P3: Write concept on empirical-correction-and-propagation discipline
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28b (High Priority); reinforced by optimistic-2026-04-28d. The 07:43 UTC `concepts/mental-imagery.md` deep-review *retracted and updated* a long-standing wrong empirical claim ("reduced performance on mental rotation" → "slower but more accurate, using analytic rather than object-based strategies" per Kay/Keogh/Pearson 2024) and the correction propagated within the same six-hour window to four other articles. The evening cluster added a second instance: the architecturally-cleanest reassignment from imagery to synaesthesia (20:39 UTC concept-page refine) propagated to apex (21:24 UTC), four exemplars (21:00 UTC), and `concepts/functionalism.md` (21:38 UTC) within four hours of the reframing landing. Two documented instances within twelve hours of each other; consider promoting from P3 to P2. Articulate *retract-and-propagate* as a methodology piece — (a) name the discipline, (b) specify criteria for when correction is warranted versus when the original claim merely needs hedging (the mental-rotation case meets both: empirically reversible direction AND dialectically richer successor finding), (c) specify the propagation requirement (cite-graph traversal: every article citing the wrong claim gets the corrected claim within the correction-window), (d) honest limitation: not every empirical claim has a clear-enough successor finding to warrant retraction; some warrant only hedging. Short scope (1000–1400 words), concept-page. Tenet alignment: methodological. See optimistic-2026-04-28b.md, optimistic-2026-04-28d.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Write concept on external-visibility prioritisation as editorial-velocity tier
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28b (High Priority). The 08:16→08:28 UTC pessimistic→refine cycle on `voids/synesthetic-void.md` (a tweeted, externally visible page) installed seven specific fixes in 12 minutes, demonstrating *visibility-tier* as an editorial-velocity discipline — faster correction loops on externally promoted content. Articulate the discipline as concept-page: (a) name the tiers (tweeted/highlighted = fastest; recently-published = fast; legacy = standard), (b) specify velocity targets per tier (synesthetic-void's 12 minutes = upper bound on tweet-tier velocity; cluster-wide velocity remains an open question), (c) specify input (a pessimistic-review or external feedback flagging a defect), (d) specify output (a refine that installs specific fixes within the tier's velocity window), (e) honest limitation: the tier structure is descriptive, not prescriptive — the cluster operates at this granularity but has not formalised it. Short scope (1200–1600 words), concept-page. Tenet alignment: methodological. See optimistic-2026-04-28b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Write concept on reciprocal cross-link discipline as network standard
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28b (Medium Priority). The 09:14 UTC five-file refine pass installed substantive paragraphs (~270 words across acquaintance-void, commensurability-void, plenitude-void, mysterianism, necessary-opacity) connecting each receiving article's specific concern to imagery-void's specific contribution — converting a one-way citation network into a two-way network with substantive content. Articulate *reciprocal cross-linking with substantive content* as the Map's network-citation standard: distinguish (a) bibliography-only references (citing without linking — defect), (b) link-only references (linking without paragraph integration — minor defect), (c) substantive reciprocal references (each side does dialectical work for the other — standard). Specify when one-way is acceptable (e.g., the citing article uses the cited only as a worked example; reciprocal would be perfunctory). Short scope (1000–1400 words), concept-page or methodology section in `apex/apex-articles.md`. Tenet alignment: methodological. See optimistic-2026-04-28b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Write concept on grain commitments in functionalism debates
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28d (High Priority). The 20:39 UTC refine of `concepts/phenomenology-vs-function-axis.md` made the *task-level grain commitment* a load-bearing argumentative move ("the axis fixes function at the task level on the grounds that this is where the standard behavioural and computational characterisation of the task lives"). The grain question recurs across at least five functionalism-debate venues: phenomenology-vs-function axis, IIT integration, philosophical zombies' functional-organisation, ai-consciousness-modes (substrate vs algorithmic vs task), and the C. elegans / Physarum specification problem at `concepts/functionalism.md` lines 134–140. None currently cross-link to a structural unification. Concept-page should (a) name the recurring pattern (*every anti-functionalist argument commits to a grain at which it claims function and phenomenology come apart, and every functionalist absorption commits to a finer grain at which they don't*), (b) catalogue the five-or-so recurrence cases, (c) specify the dialectical implication (the grain question is the pivot at which the dialectic concentrates, not a parameter of any individual argument), (d) honest limitation: there is no neutral grain — every grain commitment is theoretically loaded; the structural argument the page makes is that *grain commitments must be made visible*, not that one grain is correct. Medium scope (~1500 words), concept-page. Tenet alignment: Tenet 1 (Dualism) — the grain commitment is what makes anti-functionalist arguments rest on more than just intuition; Tenet 5 (Occam's Limits) — under-carving here would silently absorb a recurring structural feature. See optimistic-2026-04-28d.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Write apex-or-concept on empirical-wedge / conceivability-wedge pairing as anti-functionalist dialectical strategy
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28d (High Priority). The 21:38 UTC fifth deep-review of `concepts/functionalism.md` installed at §"The Absent Qualia Objection" a paragraph framing the new phenomenology-vs-function axis as *empirical complement* to the conceivability arguments (zombies, inverted qualia). The Map's anti-functionalism case now runs on two parallel tracks at the same article: zombies/inverted-qualia at the conceivability layer, the four-exemplar empirical wedge at the documented layer. The structural symmetry between conceivability-wedge and empirical-wedge is itself an argumentative move. Apex/concept-page should (a) name the *paired-wedge dialectical strategy*, (b) catalogue the two tracks (conceivability: zombies, inverted qualia, knowledge argument; empirical: phenomenology-vs-function axis, blindsight, agency I-Spy paradigm), (c) specify the load-bearing claim (convergence on a single absorption strategy that works in both registers is harder than independent absorption of each register), (d) honest limitation: the pairing is most powerful where the empirical and conceivability cases concern the same theoretical commitment (functionalism); for other commitments (illusionism, panpsychism), the pairing structure may not transfer. Medium scope (~1500–2000 words). Apex-tier consideration: if the apex-placement criterion (related task) admits methodology pieces that bear directly on philosophical synthesis, this qualifies; otherwise concept-page placement. Tenet alignment: Tenet 1 (Dualism). See optimistic-2026-04-28d.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Write concept on convergence-with-additive-cross-linking-only pattern
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28b (Medium Priority). The 07:34 UTC temporal-structure-of-understanding fourth-review and the 09:09 UTC non-retrocausal-conscious-selection-models fifth-review both reached convergence with only additive operations (cross-link added; stale comment removed; "objective collapse" disambiguated). Name the *convergence-with-additive-cross-linking-only* pattern as a maturity stage — articles internally stable but externally connectable, with subsequent reviews installing only cross-links, citation-hygiene fixes, and stale-content removals rather than substantive content changes. Specify (a) the criterion for declaring an article in this stage (typically: three prior deep reviews with no critical issues raised), (b) the discipline for reviews at this stage (only additive operations; no internal restructuring), (c) the tipping condition for re-opening (e.g., a new empirical finding contradicts a load-bearing claim, as happened with mental-rotation/aphantasia). Short scope (1000–1300 words). Tenet alignment: methodological. See optimistic-2026-04-28b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Deep review voids/amplification-void.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last deep-reviewed 2026-03-10 — 48+ days ago. Voids article on the amplification void — the inaccessibility of the process by which small differences in neural activity become salient phenomenal differences. Verify coherence with current site state, check cross-references and tenet alignment, audit for any "This is not X. It is Y." cliché violations (CLAUDE.md style ban), and verify the article's empirical citations remain current. See `/deep-review` skill.
- **Source**: staleness
- **Generated**: 2026-04-28

### P3: Write apex (or concept) article on the *weaker-than-headline disclosure* methodological pattern
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27d (High Priority). Today's V-N-W refinement (`concepts/von-neumann-wigner-interpretation.md` 20:29 UTC) installs a §Relation to Site Perspective opening explicitly stating "The Map's actual thesis is weaker than V-N-W's headline" — the position is objective-collapse-plus-modulation rather than consciousness-causes-collapse. The same discipline operates in `topics/russellian-monism-versus-bi-aspectual-dualism.md` ("the Map keeps the structuralist premise but rejects the monist conclusion"), in `concepts/stapp-quantum-mind` (Stapp's question-selection located within the formalism rather than added externally), and in the Pauli-Jung treatment. The methodology is structurally distinct from *structural-alliance* (which operates on opponents) and *forced-not-concealed* (which operates on interpretive disagreement) — *weaker-than-headline disclosure* operates on ancestor-relations, where the Map demotes its own position to be *substantively weaker* than the ancestor's headline reading. Article should (a) name the discipline, (b) catalogue cases (V-N-W, Russellian monism, Stapp, Pauli-Jung, Cisek's affordance competition), (c) specify the structural conditions (ancestor framework named, headline reading identified, Map's specific weakening identified, what is preserved from the ancestor explicitly distinguished from what is replaced), (d) honest limitation: the discipline can mask substantive disagreement as "ancestor not final form" politeness when the disagreement is sharper. Medium scope (2200-2800 words), apex-tier OR concept-page if the apex-placement criterion (see related task) is tightened. Tenet alignment: Occam's Razor Has Limits (the discipline names where the ancestor's parsimony was illusory or the mechanism overcommitted). See optimistic-2026-04-27d.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Install explicit apex-placement criterion in apex/apex-articles.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27d (High Priority). The new `apex/conjunction-coalesce.md` was admitted as the 21st apex on dialectical grounds (the methodology bears directly on `apex/taxonomy-of-voids`). The article itself acknowledges in §"A Note on Apex Placement" (line 114) that "If subsequent apex creation surfaces methodology-pieces without comparable links to philosophical synthesis, the placement criterion will need to tighten." The current criterion is implicit and case-by-case. `apex/apex-articles.md` line 486 states "future additions should require similar justification" but does not specify what that justification looks like. Refine should (a) add to §Guidelines an explicit placement criterion specifying when methodology pieces may enter apex (must serve a specific philosophical-synthesis apex, must demonstrate dialectical link strength, must declare maximum methodology-piece fraction of the apex set — currently 1/21 ~5%, propose 10% cap), (b) specify the tipping condition under which a methodology piece would migrate to `project/` (e.g., if the apex it serves is archived or coalesced), (c) cross-link to conjunction-coalesce §"A Note on Apex Placement" reciprocally, (d) preserve the index's structure and voice. Short scope (~300-500 words added). Tenet alignment: methodological/Occam's Razor Has Limits (parsimony at the curation level — keep apex layer focused on philosophical synthesis without hollowing it via methodology drift). See optimistic-2026-04-27d.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Build source-path verification tool for apex/apex-articles.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27d (Medium Priority). The 2026-04-27 21:27 UTC deep-review of `apex/apex-articles.md` repaired 21 stale source-path references across 12 entries — paths that drifted as articles were coalesced, renamed, or archived. The changelog explicitly notes "tooling to auto-verify source paths from the index would close the gap." Build a small Python module (target: `tools/curate/apex_source_paths.py` or extension to existing curation module) that (a) parses each apex entry's source-paths from the YAML-in-markdown format, (b) verifies each path resolves to a live (non-archive, non-draft-deleted) article in `obsidian/`, (c) flags drift as a linting warning rather than a hard failure, (d) integrates with `scripts/validate.py` as an opt-in check. Short scope: ~100-200 lines of Python. Could also surface drift in apex articles' `apex_sources` frontmatter field. NOTE: this is a project/infrastructure task rather than a content task, so target file is in `tools/` not `obsidian/`. See optimistic-2026-04-27d.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Write concept article on void-faceting methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28 (High Priority). The new `voids/imagery-void.md` (created 2026-04-28 03:33 UTC) distinguishes three structurally distinct faces (fidelity, inter-subjective, function-phenomenology) and ranks them by probable-permanence — a discipline that is implicit in several other voids (interoceptive-void's three absence-faces, mood-void's three opacity-layers, predictive-construction-void's four mechanisms) but not articulated as a general method. Article should (a) name the discipline (e.g., *void-faceting*), (b) provide criteria for when to facet versus keep unified (structurally distinct evidential profiles? distinct remediation strategies? distinct empirical anchors?), (c) catalogue worked examples from imagery-void, interoceptive-void, mood-void, source-attribution-void, (d) provide an *anti-pattern* — when faceting would inflate the void's apparent complexity rather than tracking real structural distinctions. Target: `concepts/void-faceting.md`. Scope: 1500–2200 words. Tenet alignment: Methodological/Occam's Razor Has Limits — the discipline names where unified treatment masks distinct evidential structures rather than tracking real unity. NOTE: concepts/ near 226+ articles vs 250 cap — within capacity. See optimistic-2026-04-28.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Write concept article on AI externalisation as void-probe methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28 (High Priority). The new `voids/imagery-void.md` §"What AI Externalisation Reveals" (lines 92–98) introduces a methodological move: AI imagery is *externalisable* in a way human imagery is not, and the asymmetry lets the void specify what it would *take* to solve the human case. The same move is implicit in `concepts/ai-consciousness-modes` and several voids articles but not generalised. Article should (a) articulate AI-externalisation-as-void-probe as a general method, (b) provide criteria for when externalisation reveals structure versus when it merely relocates the void to a different layer (the imagery-void's own caveat: "whether AI imagery has phenomenology at all is itself an open question, pushing the void to a different layer"), (c) catalogue cases where externalisation succeeds (imagery, possibly working-memory, possibly attention) and where it fails (acquaintance, intrinsic phenomenal character), (d) honest limitation: the method depends on the analogue being structurally apt, not merely behaviourally similar. Target: `concepts/ai-externalisation-as-void-probe.md`. Scope: 1500–2000 words. Tenet alignment: Dualism (the externalisation reveals what cannot be externalised, mapping the boundary between accessible and inaccessible). See optimistic-2026-04-28.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Write methodology article on recurrence-across-instruments as evidence of territoriality
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28 (High Priority). The new `voids/imagery-void.md` §"The Empirical Anchor" identifies the Würzburg-aphantasia recurrence (line 66): "The Würzburg-aphantasia recurrence is itself evidence the void is structural rather than methodological. The same phenomenon surfaces twice across a century with the same controversy structure, under different vocabularies and instruments. The territory keeps producing this shape because the shape is real." This is a new positive-evidential discipline parallel to *forced-not-concealed* (named in optimistic-2026-04-27c) and the queued *weaker-than-headline disclosure*. Article should (a) name and articulate *recurrence-across-instruments-as-evidence-of-territoriality*, (b) distinguish three sub-types: recurrence under the *same* instruments (consistency, not territoriality evidence); recurrence under *disjoint* instruments (territory survives the instrument); recurrence under *dissolution-attempting* instruments (the strongest case — the territory survives instruments designed to dissolve it; Würzburg → behaviourism → aphantasia fits this), (c) catalogue candidate cases (introspection-controversy revival; possibly the consciousness-as-physical-process debates; possibly the binding-problem revivals), (d) honest limitation — the discipline can mistake terminological recurrence for structural recurrence; specify the disambiguation criterion. Apex-tier OR concept-page depending on apex-placement criterion (see related queued task). Scope: 1800–2400 words. Tenet alignment: Occam's Razor Has Limits (the discipline names where parsimony at the level of "the controversy was just a methodological artifact" fails empirically). See optimistic-2026-04-28.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Write concept article on compound-property dissociation pattern
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28 (Medium Priority). The 2026-04-28 02:29 UTC refine of `topics/consciousness-and-the-metaphysics-of-laws-and-dispositions.md` line 168 installs a sophisticated reading of pain asymbolia as compound-property dissociation: "what we colloquially call 'pain' is a compound of two distinct powerful qualities — sensory localisation (the bodily-mapped detection of damage) and aversive valence (the hurtfulness that motivates withdrawal). Asymbolic patients retain the sensory powerful quality and lose the aversive one." This is a general response to apparent quality-power dissociations in the powerful-qualities literature: the apparent counterexample is reread by *finer-grained property individuation* rather than abandoning quality-power identity. Article should (a) articulate the pattern as a general response to alleged dissociations, (b) catalogue cases (pain asymbolia: sensory + aversive; possibly blindsight: conscious-discrimination + behavioural-discrimination; possibly depersonalisation: self-attribution + experiential-vividness), (c) provide criteria for when compound-decomposition is principled versus ad hoc (the original property must have been recognised as compound *prior* to the dissociation evidence; or the dissociation must reveal structure visible in normal cases). Target: `concepts/compound-property-dissociation.md`. Scope: 1200–1500 words. Tenet alignment: Dualism (the discipline preserves quality-power identity at the component level rather than abandoning it under empirical pressure). See optimistic-2026-04-28.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Add reciprocal cross-links between voids/imagery-void and concepts/introspection
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28 (Cross-Linking Suggestions). The new `voids/imagery-void.md` cites Schwitzgebel's introspective-unreliability claim as load-bearing (line 72) but does not link to `concepts/introspection.md`. Reciprocally, introspection's failure modes are paradigmatically visible in the imagery domain but `concepts/introspection.md` does not cite imagery-void as a paradigm case. Should also install structural-parallel cross-links between `voids/imagery-void.md` and `voids/source-attribution-void.md` (both exhibit *probing-creates-content* behaviour). Short scope (~150–250 words across three articles). Tenet alignment: methodological — preserves the navigability of the inter-void web.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Formalise the *convergence-reached* designation as article state
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27d (Medium Priority). Today three articles received the convergence designation: `apex/living-with-the-map.md` (third deep-review, "Article is in stable, mature state"), `topics/russellian-monism-versus-bi-aspectual-dualism.md` ("Convergence reached"), and earlier today `apex/what-consciousness-tells-us-about-physics.md` ("stable, no major content change"). The designation has emerged as informal practice — three deep-reviews finding no critical issues. Formalisation would (a) name the designation explicitly in `obsidian/project/` documentation, (b) specify threshold criteria (three deep-reviews? two? minimum interval between reviews? must address pessimistic findings?), (c) add a `convergence_reached: <ISO timestamp>` frontmatter field to converged articles, (d) integrate with replenish-queue logic so converged articles are not auto-staffed for deep-review unless the article is touched (modified date changes) or a meta-trigger fires (e.g., a tenet revision). The integration prevents unnecessary deep-review churn on stable articles, freeing cycle slots for articles that need them. Short scope: documentation update + frontmatter migration script + replenish-queue logic adjustment. Tenet alignment: methodological/project — supports the *earned-stability* discipline. See optimistic-2026-04-27d.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Write concept article on channel-opacity architecture as cross-modal pattern
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27c (High Priority). The *channel-with-opacity-gradient* logic appears across `voids/interoceptive-void` (three absence-faces: constitutively-unfelt, summarised, gated), `voids/mood-void` (three opacity-layers: origin, identity, constitutive), `voids/predictive-construction-void` (four mechanisms of inspection failure), and `voids/boundary-and-projection` (static edge / dynamic shift) without being named as a methodological pattern. A concept article (target: `concepts/channel-opacity-architecture.md`) would install this as the architectural common feature underlying the Map's apophatic cartography. Should (a) name the pattern explicitly, (b) survey the four cases above with their distinctive opacity gradients, (c) identify the predictive payoff (the interface model predicts channel-by-channel variation; uniform-substrate models do not), (d) cite the 2025 Frontiers in Psychology "There is no such thing as interoception" paper as the methodological frame. Estimated scope: ~2000–2500 words. Tenet alignment: Dualism (channel architecture is the interface model's central commitment), Occam's Razor Has Limits (unitary labels flatten the heterogeneity that maps the limits). NOTE: concepts/ is at 231 articles vs 250 cap — within capacity.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Write concept article on Damasio's "feelings constitute consciousness" as the contrary reading
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27c (High Priority). Damasio's 2023 *Neural Computation* paper "Feelings are the source of consciousness" is the most credible contemporary alternative to the Map's *consciousness-has-the-felt-body* framing. Currently engaged in one paragraph in `voids/interoceptive-void.md` §Relation to Site Perspective (line 90); deserves a full concept article. Article should (a) faithfully reconstruct Damasio's positive position, (b) identify exactly where it diverges from the Map's interface reading (Damasio: feelings are constitutive of consciousness; Map: feelings are had by consciousness as objects), (c) note that both readings are coherent with the empirical record on interoception, (d) locate the dialectical pressure points (Damasio's reading explains affective phenomenology more economically; the Map's reading explains the constitutively-unfelt channels more naturally). Target: `concepts/damasio-feelings-constitute-consciousness.md`. Estimated scope: ~2500 words. Tenet alignment: Dualism (clarifies Map/Damasio divergence), Bidirectional Interaction (Damasio's reading is interactionist-adjacent — the dialectical positioning matters).
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Add reciprocal cross-links from neighbour voids and concepts to voids/interoceptive-void.md
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27c (Cross-Linking Suggestions). The new `voids/interoceptive-void.md` (created 2026-04-27 14:42 UTC) is reciprocally linked to embodiment-cognitive-limits, boundary-and-projection, predictive-construction-void, and somatic-interface, but five further articles have load-bearing structural connections without cross-links: (a) `voids/affective-void.md` — affective valence often arrives via interoceptive channels; (b) `voids/ownership-void.md` — body-felt-as-mine is the densest ownership case; (c) `concepts/pain-asymbolia.md` — canonical demonstration of nociceptive signal/phenomenal pain dissociation; (d) `concepts/embodied-cognition.md` — 4E's constitutive-embodiment thesis is constrained by which bodily processes are accessible; (e) `voids/causal-interface.md` — interoceptive void identifies the body's interior as candidate locus for the consciousness-physics contact. Short scope (~250–400 words across five articles). Should preserve each article's existing voice and tenet alignment.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Write voids article on the Readiness Void
- **Type**: expand-topic
- **Notes**: Research completed in `research/voids-readiness-void-2026-03-04.md` (2026-03-04) and never synthesised into an article. The readiness void concerns the inaccessibility of the pre-deliberative state in which an action is *about to be undertaken* — the felt readiness Schurger's stochastic-threshold model targets but cannot itself decompose into report-bearing components. Adjacent to but distinct from `voids/transit-void.md` (inaccessibility of transitions) and the Libet-readiness-potential literature. Voids cap currently 97/100 — has capacity but tight; verify the void's distinctness from `voids/transit-void.md` and from `concepts/phenomenology-of-choice-and-volition.md` before writing. Target section: voids/. Scope 1800-2400 words. Tenet alignment: Dualism (readiness as a phenomenal mode not extensionally captured by motor-preparation neural correlates), Bidirectional Interaction (readiness functioning as the staging ground for the agent's contribution).
- **Source**: unconsumed_research
- **Generated**: 2026-04-27

### P3: Refine symbol-grounding-problem, dualism, qualia to invoke HPoC explicitly
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27 (High Priority). The new `concepts/hard-problem-of-content.md` (created 2026-04-27 00:34, deep-reviewed to 2024 words at 02:43) was integrated this morning into `concepts/intentionality.md`, `concepts/explanatory-gap.md`, `topics/arguments-against-materialism.md`, and `topics/enactivism-challenge-to-interactionist-dualism.md`. A grep for "hard-problem-of-content" in `concepts/symbol-grounding-problem.md`, `concepts/dualism.md`, and `concepts/qualia.md` returns zero hits — three load-bearing nodes still lack the integration. Each refine-draft would (a) `concepts/symbol-grounding-problem.md`: invoke HPoC as the broader-than-symbolic generalisation of the same diagnosis (covariation and teleosemantics also fail; symbol grounding is the special case for symbol-manipulating systems); (b) `concepts/dualism.md`: add HPoC to the convergence-of-arguments catalogue alongside explanatory gap, knowledge argument, zombies, modal argument, and Nagel; (c) `concepts/qualia.md`: explicitly underwrite qualia's existence-claims via HPoC's negative argument and PIT. Short scope (~300-500 words added each). Tenet alignment: Dualism. See optimistic-2026-04-27.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Write apex article naming the *structural-alliance* / *partial-endorsement* methodology
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27 (High Priority). The Map has now performed a distinctive methodological move multiple times: take an opponent's *negative argument* as a structural ally while declining the *positive programme* the opponent builds atop it. The HPoC article (line 86) names it explicitly: "The Map endorses the negative argument and declines the positive programme" and (line 94) "The Map borrows the diagnosis without inheriting the cure." Cases: Hutto-Myin (HPoC borrowed, REC declined), Boghossian (sophisticated self-refutation borrowed, conclusion bounded), Frankish (phenomenal-concepts cost-accounting borrowed, deflation declined), Dennett (heterophenomenology methodological discipline borrowed, framework declined), possibly Buddhist no-self (deconstructive critique borrowed, eliminative reading declined). Move is distinct from the *concept extraction* method named in optimistic-2026-04-26b — structural alliance applies to *external* opponents whose arguments the Map can use without endorsing their conclusions. Apex would (a) name the move, (b) catalogue the Map's history of doing it, (c) specify when appropriate (when the negative argument is internal to the opponent's resources rather than presupposing the Map's conclusion), (d) honest limitation: the move can collapse into mis-citation if not careful — the opponent's negative argument must genuinely survive separation from their positive programme; some negative arguments depend on commitments that re-import the cure when the diagnosis is preserved. Medium scope (2200-2800 words), apex-tier. Tenet alignment: methodological — most directly Dualism (the discipline that lets the Map use naturalist arguments without converting to naturalism) and Occam's Razor Has Limits (the move that names the cost of opponents' parsimony moves precisely). See optimistic-2026-04-27.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Cross-review voids/tacit-integration-void.md against voids/noetic-feelings-void.md
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27 (Medium Priority). Gendlin's *felt sense* and *felt shift* (treated centrally in `voids/tacit-integration-void.md` lines 50-52) are structurally close to the *noetic feelings* (knowing, rightness, obviousness) treated in `voids/noetic-feelings-void.md`. Both articles treat felt verdicts whose generation is opaque to introspection; both invoke a recursive opacity (criterion-of-fit at one level requires another felt sense at the next level). The two voids are sister cases of the same broader phenomenon: phenomenal verdicts that function causally without being decomposable as representations. Cross-review should (a) verify reciprocal `[[noetic-feelings-void]]` ↔ `[[tacit-integration-void]]` links exist in related_articles and prose; (b) install a short paragraph in each article positioning the other as the sister case (tacit-integration-void treats the *integrative* face of the broader phenomenon; noetic-feelings-void treats the *verdictive* face); (c) check whether the structural argument in noetic-feelings-void supports the conditional in tacit-integration-void or vice versa; (d) verify the two articles' Polanyi treatments are consistent (if both cite Polanyi); (e) preserve each article's existing voice and tenet-alignment. Short scope (~200-400 words added across both articles). Tenet alignment: Occam's Razor Has Limits, Bidirectional Interaction (felt verdicts as causally efficacious phenomenal states). See optimistic-2026-04-27.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Refine concepts/teleosemantics.md (or create Mann-Pain reply concept page if absent)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27 (Medium Priority). The teleosemantic critique and the Mann-Pain reply (HPoC article lines 52-58 and 72-76) are load-bearing in `concepts/hard-problem-of-content.md` but currently lack their own treatments. Mann-Pain's distinction between truth-evaluability and intensionality, and their concession that teleosemantics meets the first but not the second, is dialectically significant — it concedes the substantive point and rebrands the loss as acceptable. First step: verify whether `concepts/teleosemantics.md` already exists. If yes: refine it to (a) state the Mann-Pain distinction precisely, (b) name the dialectical move (concession-rebranding) as a recurring physicalist response pattern, (c) compare to other concession-convergence cases the Map has documented, (d) honest limitation: Mann-Pain's reply is itself contested — defenders argue intensionality concession is acceptable; critics argue the loss is too high. If no: defer creation since concepts is at 232/250 (very near cap); flag as a candidate for future creation only if citation density grows. Short scope if refining (~300-600 words added). Tenet alignment: Dualism (the failure of teleosemantics as a structural rather than contingent failure). See optimistic-2026-04-27.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Refine knowledge-argument, philosophical-zombies, phenomenal-acquaintance, qualia to invoke constitutive/referring distinction explicitly
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26b (High Priority). The new `concepts/constitutive-vs-referring-observation.md` (line 64) explicitly says four Map articles use the constitutive structure "sometimes implicitly": `knowledge-argument`, `philosophical-zombies`, `phenomenal-acquaintance`, `qualia`. The phenomenal-authority article was integrated tonight; these four were not. Each refine-draft would (a) add a one-paragraph invocation of the constitutive/referring distinction in the context where each article most needs it (knowledge-argument: what Mary acquires is content whose existence-conditions are constitutive observation; philosophical-zombies: what zombies lack is a property whose existence-conditions are constitutive observation; phenomenal-acquaintance: Russell's epistemological distinction is the partial precursor to the metaphysical constitutive/referring distinction; qualia: qualia's existence-claims are constitutive-observation claims, which is why they have a different epistemic standing than referring-observation claims about properties), (b) cross-link reciprocally to `constitutive-vs-referring-observation`, (c) tighten each article's response to introspection-as-theory-laden charges, (d) preserve each article's existing voice and argument structure. Short scope (each ~400-600 words added). The integration is what makes the morning's concept-extraction move payoff-positive rather than producing a stranded reference. Target: four short refine-drafts, can be batched or run separately. Tenet alignment: Dualism. See optimistic-2026-04-26b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Write apex article naming the *concept-extraction* method
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26b (High Priority). The Map has now performed the same methodological move three times in eight days — extract a load-bearing distinction or argument from inside a topic article into a standalone, citable concept page. Tonight: `concepts/carrolls-regress.md` and `concepts/constitutive-vs-referring-observation.md` extracted from `voids/inference-void.md`, `topics/eliminative-materialism.md`, and `topics/phenomenal-authority-and-first-person-evidence.md`. Earlier: `concepts/parsimony-epistemology.md` and `concepts/self-stultification.md` from related work. The move is distinct from coalescence (which merges full articles) and from refinement (which improves drafts in place). Naming it would let future cycles invoke the discipline by name rather than reinventing it. Apex would (a) name the method (suggested: *concept extraction*), (b) catalogue the Map's history of doing it, (c) specify when extraction is appropriate (when a distinction is cited in three-plus articles and is being re-established each time), (d) examine the relation to coalescence (concept extraction increases citation density; coalescence reduces article count) and to refinement (concept extraction creates new articles; refinement modifies existing ones), (e) honest limitation: extraction can produce thin concept pages if the source distinction was not actually load-bearing in multiple places, so the move requires a fitness test — three-plus citation sites and active re-establishment in each. Medium scope (2000-2800 words), apex-tier. Tenet alignment: methodological. Most directly supports Occam's Razor Has Limits (the right form of parsimony at the citation-graph level — minimise re-establishment, not concepts). See optimistic-2026-04-26b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Refine illusionism.md to engage the constitutive-observation challenge directly
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26b (Medium Priority). `concepts/constitutive-vs-referring-observation.md` lines 72 and 84 explicitly identify illusionism as "the principal opposing view that denies the constitutive relation" but `concepts/illusionism.md` does not yet have a return-citation. Refine would (a) install a section "The Constitutive-Observation Challenge" that names the move the constitutive/referring distinction puts on illusionism, (b) state Frankish's response (the seeming-of-phenomenality is a higher-order representation that misrepresents itself as constitutively related to a phenomenal property that does not exist), (c) cross-link reciprocally with `constitutive-vs-referring-observation`, (d) preserve the article's existing Frankish-friendly engagement (the Map is not in the business of straw-manning illusionism). The bedrock-disagreement framing benefits both articles: illusionism becomes the named position the constitutive/referring framing must contest; the constitutive/referring framing becomes the named challenge illusionism must answer. Short scope (500-800 words added). Tenet alignment: Dualism. See optimistic-2026-04-26b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Write concept article on Engel's Inferentialist Reading of Carroll's Regress
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26b (Medium Priority). `concepts/carrolls-regress.md` line 50 cites Pascal Engel as the most prominent contemporary defender of the inferentialist reading but treats Engel as a name-citation. A short concept page would (a) state Engel's argument that "no formal logic can supply what the regress reveals as missing — the missing element is a primitive *taking-as*" with the supporting argumentation from Engel's HAL working paper hal-03675073v1, (b) catalogue Engel's responses to the deflationary reading, (c) connect to the *Inference and Consciousness* volume (Boghossian & Wright, eds., 2018) as a research programme rather than an isolated paper, (d) examine the relation to Brandom's competing inferentialism and to Polanyi's tacit-inference framing, (e) honest limitation: Engel's argument is itself contested, and the article should not over-claim its strength. Short scope (1200-1700 words). Target: `concepts/` (~229/250, near cap — verify capacity at task pickup). Tenet alignment: Occam's Razor Has Limits (Engel's argument is precisely a limit-of-parsimony move at the proof-theoretic level), Dualism (taking-as as candidate primitive). See optimistic-2026-04-26b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Add cross-links across 2026-04-26 evening cluster (knowledge-argument, philosophical-zombies, phenomenal-acquaintance, qualia, illusionism, parsimony-epistemology, self-stultification, argument-from-reason, inference-void, eliminative-materialism)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26b (Cross-Linking Suggestions table). Ten high-value cross-links missing across the evening's content cluster: (1) `concepts/illusionism.md` ↔ `concepts/constitutive-vs-referring-observation.md` (reciprocal — new article names illusionism as principal opposing view); (2) `concepts/knowledge-argument.md` → `concepts/constitutive-vs-referring-observation.md` (Mary illustrates the same constitutive structure from the side of *content*); (3) `concepts/philosophical-zombies.md` → `concepts/constitutive-vs-referring-observation.md` (zombies illustrate the same structure); (4) `concepts/phenomenal-acquaintance.md` → `concepts/constitutive-vs-referring-observation.md` (Russell's distinction is named as partial precursor in new article); (5) `concepts/qualia.md` → `concepts/constitutive-vs-referring-observation.md` (qualia's existence-claims are constitutive-observation claims); (6) `topics/argument-from-reason.md` → `concepts/carrolls-regress.md` (treats Carroll's regress as a strand but lacks dedicated concept-page citation); (7) `voids/inference-void.md` ↔ `concepts/carrolls-regress.md` (reciprocal — concept-page should now be the canonical reference; inference-void can stop re-establishing the regress in-text); (8) `topics/eliminative-materialism.md` → `concepts/constitutive-vs-referring-observation.md` (article's central Moorean rebuttal now has a dedicated concept page); (9) `concepts/parsimony-epistemology.md` → `concepts/constitutive-vs-referring-observation.md` (Tenet-5 connection — parsimony's reach across observation-types fails); (10) `concepts/self-stultification.md` → `concepts/constitutive-vs-referring-observation.md` (sister concept extractions from same foundational discipline). Short scope (link additions plus brief integrative sentences where natural). Note: this overlaps partially with the four-article refine-draft task above; the cross-link task should run *after* the deeper refinement task to avoid overwriting integration work. See optimistic-2026-04-26b.md Cross-Linking Suggestions table.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Condense voids/meaning-void.md (3111 words, 156% of voids hard threshold)
- **Type**: condense
- **Status**: pending
- **Notes**: Newly-coalesced article exceeds 2000-word voids hard threshold. Coalesce on 2026-04-26 merged intentionality-void + semantic-void into meaning-void at 3111 words; the merge preserved both source articles' distinct contributions but did not aggressively condense. Run after the queued deep-review of meaning-void completes (the deep-review may already remove redundancy, in which case this task may become unnecessary or smaller in scope). Preserve the load-bearing partition between aboutness-gap and semantic-gap (the distinction was the central reason for keeping two articles before coalescence) while removing redundant exposition between the merged sections. Defer detailed sub-arguments to linked articles where possible. See `/condense` skill.
- **Source**: length_analysis
- **Generated**: 2026-04-26

### P3: Write synthesis article on the Second-Order Voids Cluster
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-24 (High Priority). The April 2026 cluster — `voids/question-formation-void.md` (2026-04-24), `voids/epistemic-horizon-void.md`, `voids/categorial-void.md`, `voids/plenitude-void.md` — is treated *in passing* as a cluster (see question-formation-void lines 40) but has no synthesis article naming its joint structure. These four voids share an architectural feature: each concerns the *apparatus* of self-reflective cognition rather than specific contents. They compose in ways single-void articles cannot trace (e.g., question-formation-void + epistemic-horizon-void: we cannot list what we cannot form *and* cannot estimate the scope of what we cannot form). Synthesis would (a) name the cluster and articulate its shared structural logic, (b) catalogue the compositional interactions between members, (c) relate to the already-queued "Inheritance Problem" article, (d) potentially fold in `voids/meta-epistemology-of-limits.md` as fifth member, (e) sit as companion to `apex/taxonomy-of-voids.md` at apex level. Medium scope (2000-2800 words). Target: `apex/` if extended, `voids/` if narrower. Tenet alignment: Occam's Razor Has Limits primarily; Dualism secondarily (apparatus having specific architectural limits is evidence for specific kind, not generic computation). See optimistic-2026-04-24.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-24

### P3: Write concept article on Erotetic Logic and the Philosophy of Mind
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-24 (High Priority). `voids/question-formation-void.md` (2026-04-24) cites Andrzej Wiśniewski's erotetic logic — the formal theory of questions with its distinctions of question-presupposition, admissible answers, and evoked questions — but the formal machinery is used once and not developed. The Map currently lacks a formal language for distinguishing "cannot answer" from "cannot form" from "cannot evoke" — distinctions that would sharpen a great deal of existing void-writing that conflates these. Article would (a) present Wiśniewski's core apparatus accessibly, (b) apply the apparatus to hard-problem and void-mapping contexts, (c) distinguish erotetic presupposition from Collingwood's absolute presupposition, (d) examine how paradigm shifts in Kuhn's sense map onto changes in question-evocation structure, (e) honest limitation: erotetic logic is formalised for idealised agents; real cognitive question-formation involves heuristic and affective processes the formal theory brackets. Short-to-medium scope (1500-2000 words). Target: `concepts/` (~228/250, near cap but highly-cited cross-cutting entry). Tenet alignment: Occam's Razor Has Limits (parsimony judgments are presupposition-laden); Dualism (if question-evocation is a semantic-inferential relation not purely syntactic, the apparatus is a candidate site for irreducibility). See optimistic-2026-04-24.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-24

### P3: Write concept article on Collingwood's Absolute Presuppositions vs Kuhnian Paradigms
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-24 (Medium Priority). `voids/question-formation-void.md` and `topics/consciousness-and-the-structure-of-scientific-revolutions.md` both invoke framework-level limits on what can be asked, but the relationship between Collingwood's absolute-presupposition framework (from *An Essay on Metaphysics*, 1940) and Kuhn's paradigm framework (1962) is not drawn out on the site. The two are cited as cousins but have different evidential roles: Collingwood is tighter on the question-formation point (individual presuppositions can be regressively recovered); Kuhn is tighter on revolutionary-transition dynamics (paradigm shift as gestalt switch). A methodological article that situates each in its proper evidential role would save future articles from over-crediting one or the other. Short scope (1200-1800 words). Target: `topics/` or `concepts/`. Tenet alignment: Occam's Razor Has Limits. See optimistic-2026-04-24.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-24

### P3: Write topic article on Hermeneutical Injustice as Phenomenal Evidence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-24 (Medium Priority). `voids/question-formation-void.md` cites Miranda Fricker's 2007 *Epistemic Injustice* (and the Carmita Wood case) as a single existence proof for question-formation lifts. But Fricker's hermeneutical-injustice framework is a rich empirical resource for the Map that supplies phenomenological data the Map could draw on more broadly: articulation gains in #MeToo, "intersectionality", "gaslighting", "coercive control" are all cases of the same phenomenon — phenomenal content existing before the concept to articulate it exists. An article treating hermeneutical injustice as a *class of empirical data about phenomenal consciousness* would (a) catalogue the paradigm cases beyond sexual harassment, (b) argue they collectively demonstrate phenomenal content is not constituted by concept-availability (the pre-concept subject was not in phenomenal error — they were in articulation failure), (c) connect to Husserlian *presumptive evidence* — the experience was fully present but its structure became articulate only later, (d) help defuse the charge that dualism is politically or ethically inert, (e) honest limitation: some constructivists argue the concept *does* partly constitute the experience, and the article should acknowledge this is a live debate. Medium scope (1800-2500 words). Target: `topics/` (~224/250). Tenet alignment: Dualism primarily (phenomenal content exists before the concept; concept acquisition does not *create* the experience); Occam's Razor Has Limits. See optimistic-2026-04-24.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-24

### P3: Deep-review expansion of contemplative-practice-as-philosophical-evidence with method-level cross-tradition comparison
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-24 (Medium Priority). `topics/contemplative-practice-as-philosophical-evidence.md` is cited across `methodology-of-consciousness-research.md` and `indian-philosophy-of-mind.md` more often than it is developed. The article establishes the *existence claim* (contemplative practice is real philosophical evidence) but the direct *method-level* cross-tradition comparison is thin — Buddhist *śamatha-vipassanā* and Husserlian *epoché* as methodologically related procedures, Samkhya's discriminative knowledge (*viveka-jnana*) and the phenomenological reduction as parallel disciplines. Refine-draft would (a) add a section directly comparing the methodological steps of three-four contemplative methods side-by-side with phenomenological method, (b) identify the *common discipline* across metaphysical disagreements (what the Map needs), (c) explicitly scope the claim: method-convergence does not entail ontology-convergence, and the schools disagree about ontology precisely because they share method, (d) honest limitation: method-comparisons risk over-generalising from superficial structural similarity to genuine methodological kinship. Medium scope (target expand from current length by ~1500 words or integrate into existing structure). Target: `topics/contemplative-practice-as-philosophical-evidence.md`. Tenet alignment: Dualism (method convergence across radically different metaphysical framings). See optimistic-2026-04-24.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-24

### P3: Add cross-links across methodology-of-consciousness-research, indian-philosophy-of-mind, apophatic-cartography, taxonomy-of-voids, question-formation-void, noetic-feelings-void
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-24 (Cross-linking). Seven high-value cross-links missing across today's content cluster: (1) `topics/methodology-of-consciousness-research.md` → `voids/question-formation-void.md` (the Galilean exclusion *is* an absolute-presupposition installation in Collingwood's sense; the article's whole thesis is about what scientific method *could not have asked*); (2) `topics/methodology-of-consciousness-research.md` → `topics/indian-philosophy-of-mind.md` (neurophenomenology's mutual-constraint framework has structural kin in Samkhya *sannidhya* and Vacaspati's *pratibimba-vada*); (3) `voids/apophatic-cartography.md` → `topics/indian-philosophy-of-mind.md` (the article cites Advaita *neti neti* and Buddhist *śūnyatā* as apophatic method but does not link to `indian-philosophy-of-mind` directly; reciprocal link should land both ways); (4) `apex/taxonomy-of-voids.md` → `topics/indian-philosophy-of-mind.md` (cross-traditional convergence is a stated evidential criterion but the main Indian-philosophy article is absent from related_articles); (5) `apex/taxonomy-of-voids.md` → `voids/question-formation-void.md` (the new article explicitly names apophatic method's upstream void; the apex should cite it in §"The Taxonomy's Own Limits" and in related_articles); (6) `voids/question-formation-void.md` → `topics/methodology-of-consciousness-research.md` (the methodology article supplies three case-studies of question-formation boundary work: heterophenomenology erases certain questions, neurophenomenology evokes new ones, second-person methods require questions that cannot be posed without intersubjective apparatus); (7) `voids/noetic-feelings-void.md` → `voids/question-formation-void.md` (the feelings-gate account and the question-formation account are two halves of a unified story about what terminates inquiry: felt verdict plus unasked question). Short scope (link additions plus brief integrative sentences where natural). See optimistic-2026-04-24.md Cross-Linking Suggestions table.
- **Source**: optimistic-review
- **Generated**: 2026-04-24

### P3: Write methodology article "Evidential vs Definitional Unfalsifiability in Consciousness Studies"
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-night (High Priority). `voids/plenitude-void.md` lines 102-103 installed tonight the distinction between *evidential* unfalsifiability (nature happens not to supply discriminating observations) and *definitional* unfalsifiability (the terms of the question are set so that no observation could count as discriminating). Plenitude-void concedes its void is primarily definitional and refuses only the conclusion that the question is pseudo-empirical. The distinction is now load-bearing across four articles: plenitude-void, `voids/distraction-void.md` (occlusion reading unfalsifiable), `voids/phenomenal-quality-void.md` (challenge conditions specification), `topics/born-rule-violation-brain-interface-empirical-status.md` (corridor dualism ensemble-invisibility). Article would (a) articulate the distinction at principled level, (b) argue definitional unfalsifiability is not a pseudo-empirical signature but a feature of how the current conceptual vocabulary is load-bearing, (c) catalogue the four worked examples and their common structural pattern, (d) address the Popperian charge against dualism in its strongest form, (e) specify when definitional unfalsifiability does collapse into pseudo-science and when it does not. Medium scope (1800-2500 words). Target: `topics/` (~224/250) or `concepts/` (~228/250). Tenet alignment: Occam's Razor Has Limits directly; supports all other tenets by clarifying what unfalsifiability concessions commit the Map to. See optimistic-2026-04-23-night.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write voids article "The Inheritance Problem — When a Framework Cannot Exempt Itself"
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-night (Medium Priority). The pattern where a framework cataloguing cognitive limits cannot exempt its own cataloguing from those limits appears in three new articles tonight: `voids/epistemic-horizon-void.md` lines 64-74 ("Does the Map Inherit Its Own Horizon?"), `voids/categorial-void.md` lines 108-112 (article uses categories drawn from the apparatus whose limits are at issue), and implicitly in `voids/plenitude-void.md` (the article's own investigation is compromised by the phenomenon it investigates). Short article would (a) articulate the inheritance pattern as a structural claim, (b) argue the appropriate response is to build the inheritance into the framework's epistemic self-presentation rather than hide it, (c) preempt the objection that the voids framework exempts itself, (d) connect to the broader Gödel-simulation-mysterianism cluster of self-referential limit arguments. Short scope (1500-2000 words). Target: `voids/` section. Tenet alignment: Occam's Razor Has Limits. See optimistic-2026-04-23-night.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write a Concession Ledger article cataloguing what the Map does not claim
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-afternoon (High Priority). Today's refine-draft / deep-review cycle on `topics/pragmatist-quantum-foundations-and-the-agent.md`, `topics/falsification-roadmap-for-the-interface-model.md`, and `topics/testing-consciousness-collapse.md` has installed an accumulating pattern of *confessions* — the corridor reading is ensemble-invisible (pragmatist-quantum line 124); Tenet 1 has no decisive falsifier (falsification-roadmap lines 60-67); Tenet 5 is not a scientific claim (falsification-roadmap lines 117-123); the primitive-to-non-physical inference is a three-step chain that corroborates rather than establishes Tenet 1 (pragmatist-quantum lines 121-122); the Q-shape anchor may prove permanently uncomputable (testing-consciousness-collapse line 207). A Concession Ledger article would (a) collect these confessions in one place, (b) argue that the explicit ledger is evidence *against* the unfalsifiability charge (the Map specifies its own limits more precisely than most physicalist positions do), (c) compare to how rival positions — illusionism, panpsychism, MWI — handle their own analogues, (d) honest limitation: a concession ledger can harden into a defensive move if it is not updated as the Map evolves. Medium scope (2000-2500 words). Target: `apex/` or `topics/` (~224/250, has capacity). Tenet alignment: Occam's Razor Has Limits (load-bearing), all other tenets. See optimistic-2026-04-23-afternoon.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write topic article on Deutsch's 1985 Wigner's Friend macroscopic branch interference
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-afternoon (High Priority). `topics/falsification-roadmap-for-the-interface-model.md` line 109 names Deutsch's 1985 Wigner's friend variant as the *decisive* falsifier of Tenet 4 (No Many Worlds), but the Map has no dedicated treatment. The Tier 3 section of `topics/testing-consciousness-collapse.md` engages Proietti (2019), Bong (2020), and Allori (2025) but not the Deutsch 1985 proposal itself. Article would (a) specify Deutsch's original 1985 proposal (detecting macroscopic branch interference), (b) catalogue technological requirements (quantum memories isolating macroscopic observer-systems), (c) survey progress toward those requirements over the last four decades, (d) examine what a successful realisation would and would not show — crucial: it would confirm MWI over collapse but not select among collapse variants if negative, (e) connect to the extended Wigner's friend empirical chain and to the corridor / minimum-outside-corridor taxonomy. Medium scope (2000-2500 words). Target: `topics/` (~224/250, has capacity). Tenet alignment: No Many Worlds (directly), Minimal Quantum Interaction, Occam's Razor Has Limits. See optimistic-2026-04-23-afternoon.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write concept article on Convergence-Based Evidence as Scientific Methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-afternoon (High Priority). `topics/testing-consciousness-collapse.md` lines 203-215 install "The Evidential Asymmetry and the Convergence Strategy" as the Map's response to the confound of embodiment, and explicitly name the burden convergence evidence carries — "specifying what evidence would count *against* the hypothesis." The Q-shape prediction is currently the Map's only named anchor for this burden, and testing-consciousness-collapse line 207 confesses the anchor may fail in principle. A dedicated concept article would (a) formalise convergence-based evidence as a methodology distinct from Bayesian accumulation and from consilience, (b) specify what makes a convergence-evidence anchor well-formed, (c) catalogue the Map's current anchors (Q-shape prediction, selective coherence disruption, behavioural signatures of authority-selection) and their current status, (d) examine the historical precedent for convergence evidence in physics and biology, (e) honest limitation: if all convergence anchors fail, convergence evidence becomes indistinguishable from unfalsifiability and the methodology collapses. Medium scope (2000-2500 words). Target: `concepts/` (~228/250) or `topics/` (~224/250). Tenet alignment: Minimal Quantum Interaction, Bidirectional Interaction, Occam's Razor Has Limits. See optimistic-2026-04-23-afternoon.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Add cross-links across testing-collapse, pragmatist-quantum, falsification-roadmap, predictive-processing cluster
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-afternoon (Cross-linking). Five high-value cross-links missing between the afternoon's modified articles: (1) `topics/testing-consciousness-collapse.md` Tier 3 section → `topics/pragmatist-quantum-foundations-and-the-agent.md` (Frauchiger-Renner bears on QBism's extended Wigner's friend treatment); (2) `topics/falsification-roadmap-for-the-interface-model.md` Tenet 4 section → `topics/testing-consciousness-collapse.md` Tier 3 (falsification-roadmap names Deutsch's Wigner's friend variant; testing-consciousness-collapse develops adjacent Frauchiger-Renner case); (3) `concepts/predictive-processing.md` "Decoherence-proof consciousness" challenge (line 185) → `topics/testing-consciousness-collapse.md` Decoherence Timescale Objection section (PP invokes decoherence-as-fatal; testing-consciousness-collapse now has Hagan-Hameroff counter-estimate with qualifiers); (4) `topics/pragmatist-quantum-foundations-and-the-agent.md` Natural-ally-Stapp paragraph → `topics/testing-consciousness-collapse.md` Stapp Zeno sub-section (pragmatist-quantum places Stapp in minimum-outside-corridor; testing-consciousness-collapse gives the specific Zeno prediction); (5) `topics/falsification-roadmap-for-the-interface-model.md` AI consciousness bullet (line 153) ↔ `concepts/predictive-processing.md` "Functional consciousness in artificial systems" challenge (line 179) (same counterfactual, currently only weak cross-citation). Short scope (link additions, brief integrative sentences). See optimistic-2026-04-23-afternoon.md Cross-Linking Suggestions table.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write concept article synthesising the three MQI-sanctioned options
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-midday (High Priority). The corridor/minimum-outside-corridor/trumping three-way branch now appears in four major articles (`topics/mathematical-structure-of-the-consciousness-physics-interface.md` lines 71-79, `topics/born-rule-and-the-consciousness-interface.md` lines 129-131, `concepts/psychophysical-laws.md` line 91, `topics/four-quadrant-dualism-taxonomy.md` line 135) without a canonical treatment. Article would (a) state the taxonomy once and derive each option from MQI explicitly, (b) catalogue the empirical and theoretical considerations that would move the Map between them, (c) distinguish the structural move (corridor/min-outside-corridor split the *magnitude* axis; trumping is on a different axis entirely), (d) identify what each option forbids. Medium scope (2000-2500 words). Target section: concepts/ (~228/250, has capacity). Tenet alignment: Minimal Quantum Interaction (core), Dualism, Bidirectional Interaction, Occam's Razor Has Limits. See optimistic-2026-04-23-midday.md. **Update 2026-04-23 evening**: the three-way taxonomy now appears in at least seven articles (adds `topics/consciousness-and-probability-interpretation.md` line 95, `topics/quantum-measurement-and-consciousness.md` line 132, `topics/consciousness-and-the-structure-of-scientific-revolutions.md` line 76, `topics/born-rule-violation-brain-interface-empirical-status.md` lines 54-66 as hub). Priority for this task rising — the concept-level absence is increasingly visible as a gap.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write methodology article on Stating Position Costs Before Arguing Position Merits
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-evening (High Priority). A pattern now visible across at least four evening/afternoon artefacts: `voids/distraction-void.md` line 93 (occlusion reading's unfalsifiability admitted with specific disfavouring conditions); `topics/born-rule-violation-brain-interface-empirical-status.md` lines 148-149 ("what the Map can and cannot do" stated with vulnerability first); `topics/consciousness-and-probability-interpretation.md` line 95 (mechanism-independence of the phenomenological argument disclosed); `topics/pragmatist-quantum-foundations-and-the-agent.md` lines 121-122 (primitive-to-non-physical inference hedged as three-step, with independent work located elsewhere). The move is: concede the empirical vulnerability, state the specific conditions that would worsen it, *then* argue the non-empirical grounds for holding the position anyway. Mirror image of the "bullet-biting" P3 task — bullet-biting accepts opposing claims; this move admits one's own weaknesses. Article would (a) name the pattern, (b) exhibit the four+ instances, (c) distinguish it from unfalsifiability-as-failure vs unfalsifiability-as-responsible-uncertainty, (d) locate it under Tenet 5 (Occam's Razor Has Limits) as the licensed response to parsimony-undecidable cases. Short scope (1200-1800 words). Target section: topics/ (~224/250, has capacity). See optimistic-2026-04-23-evening.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write concept article on the Testability-Opacity Dual
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-evening (Medium Priority). `voids/distraction-void.md` lines 87-91 identifies the void as the place where the interface would be *most exposed to introspection* and yet where introspection goes dark, joining `voids/agency-verification-void.md` and `voids/amplification-void.md` as a family with the same structural signature. Concept article would make the "testability-opacity dual" precise: the claim that for any proposed consciousness-physics interface, the regime where the interface should be most detectable from the inside is systematically the regime where introspection is worst. If true as a general pattern, predicts which voids should be most intractable and why. Would need to catalogue voids that do and do not fit the pattern — at least six candidates (distraction, agency-verification, amplification, transit, recognition, acquaintance) fit; several do not. Medium scope (2000-2500 words). Target section: concepts/ (~228/250, has capacity). Tenet alignment: Bidirectional Interaction primarily, Occam's Razor Has Limits secondary. See optimistic-2026-04-23-evening.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Install empirical-status hub cross-links across remaining outbound-missing articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-evening (Cross-linking). `topics/born-rule-violation-brain-interface-empirical-status.md` (created today) has become a de facto hub with five inbound links installed during the afternoon and evening deep reviews. Remaining outbound-missing articles: (1) `topics/mathematical-structure-of-the-consciousness-physics-interface.md` — hub cross-references it as home of the three-option branch; verify reciprocal body-text link exists, not only Further Reading. (2) `concepts/predictive-processing.md` — PP sits naturally on the corridor side; article could say so in one Relation to Site Perspective sentence. (3) `voids/distraction-void.md` ↔ `voids/agency-verification-void.md` and `voids/amplification-void.md` — sibling relationships named in distraction-void but reciprocals missing. (4) Verify `topics/testing-consciousness-collapse.md` and `topics/falsification-roadmap-for-the-interface-model.md` cross-link depth — both were reviewed *before* the hub article's full absorption. Short scope (link additions plus brief integrative sentences; 3-5 articles touched). See optimistic-2026-04-23-evening.md Cross-Linking Suggestions.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write topic article on Generation Fluency and Philosophical Intuition
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-midday (High Priority). `voids/noetic-feelings-void.md` line 62 cites Thompson's finding that feelings of rightness (FOR) are driven by generation fluency rather than underlying reasoning, and that manipulating fluency shifts FOR without changing the reasoning itself. Philosophical intuitions — primary data for analytic philosophy — are felt signals of the same family. Article would (a) apply Thompson's fluency work to philosophical intuition specifically, (b) flag which kinds of intuition are fluency-vulnerable (trolley-problem variants, conceivability arguments, simplicity intuitions) and which are more robust, (c) examine the methodological consequences for intuition-reliant programmes including the Map's, (d) honest limitation: the Map's programme depends on some intuitions, so the article must distinguish deflation of *all* intuitions from calibration of *which*. Medium scope (2000-2500 words). Target section: topics/ (~225/250, has capacity). Tenet alignment: Occam's Razor Has Limits (intuitions of simplicity are fluency-driven), Dualism (the conceivability argument and the hard-problem intuition are load-bearing philosophical intuitions whose fluency-vulnerability must be assessed). See optimistic-2026-04-23-midday.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write concept article on Calibration Pathology as Void-Mapping Methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23-midday (High Priority). `voids/noetic-feelings-void.md` line 93 — *"The void has a signature, even when its interior is inaccessible"* — makes a methodological observation that deserves its own article. The noetic-feelings void catalogues déjà vu, jamais vu, calibration curves, and overconfidence asymmetries as *structural* data about the void's architecture. This is the core apophatic-cartography move applied to a specific domain. Article would (a) formalise calibration pathology as a methodology where the characteristic shape of failure is the data, (b) extend beyond noetic feelings to other void domains, (c) distinguish it from related methodologies (apophatic-cartography, compound-failure-signatures) and clarify where it sits in the method space, (d) examine what counts as a well-formed pathology signature (persistence, asymmetry, architectural correlation). Medium scope (2000-2500 words). Target section: concepts/ (~228/250). Tenet alignment: Occam's Razor Has Limits (calibration pathology is evidence against the felt-sufficiency reading of parsimony), Dualism. See optimistic-2026-04-23-midday.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write concept article on The Authority Layer as a general philosophical category
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23 (High Priority). `concepts/trumping-preemption.md` lines 50-54 name the *authority layer* as the independently useful conceptual contribution of Schaffer's template, but the Map has no standalone treatment of authority as a general philosophical category. Article would (a) formalise the authority layer as a philosophical category with multiple instantiations (legal, structural, metaphysical), (b) distinguish socially-constructed and structural authority from the metaphysical authority the Map's programme needs, (c) examine whether the cross-domain applicability of the decoupling strengthens or weakens the Map's use of it — the risk cuts both ways and must be named, (d) apply the category back to the Map's own use in the Schaffer-Saad-Map chain. Medium scope (2000-2500 words). Target section: concepts/ (~228/250, has capacity). Tenet alignment: Dualism (the metaphysical authority claim is central), Minimal Quantum Interaction, Occam's Razor Has Limits. See optimistic-2026-04-23.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write concept article on Observational Closure as a standalone thesis
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23 (High Priority). Observational closure — the thesis that physical causal patterns are preserved observably even when universal closure fails — is currently treated as a *feature* of delegatory causation and as a *parallel* to MQI (see concepts/delegatory-causation.md lines 116-122, concepts/trumping-preemption.md line 70, concepts/mental-causation-and-downward-causation.md lines 103-105). But it is independently a load-bearing thesis. Article would (a) define observational closure precisely, (b) catalogue the arguments establishing it as a consequence of the Map's other commitments (Born-rule preservation, coarse-grained preemption, authority-sufficiency decoupling), (c) examine the epistemic consequences — observational closure places the Map's case on philosophical rather than empirical ground, (d) address the unfalsifiability objection by distinguishing observational closure (a consequence) from the Map's falsifiable commitments (MWI, neural quantum effects). Medium scope (2000-2500 words). Target section: concepts/ (~228/250). Tenet alignment: Minimal Quantum Interaction (directly), Dualism. See optimistic-2026-04-23.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write topic article on the Fiction-to-Nature Disanalogy as methodological constraint
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23 (High Priority). `concepts/trumping-preemption.md` line 58 installs the fiction-to-nature disanalogy as a one-paragraph philosophical-hygiene move, but the disanalogy applies to an entire class of structural templates philosophy imports from stipulation-based cases (laws of magic, legal conventions, military rank). Article would (a) generalise the disanalogy as a methodological constraint on template-importation, (b) catalogue other cases where philosophy has imported stipulative templates and where the disanalogy was/wasn't flagged, (c) examine whether this is one-off hygiene or a systematic constraint, (d) apply the constraint back to the Map's use of trumping. Medium scope (2000-2500 words). Target section: topics/ (~225/250, has capacity). Tenet alignment: Occam's Razor Has Limits (a post-parsimony constraint on template-importation), Dualism (the Map's use of trumping depends on this constraint). See optimistic-2026-04-23.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write concept article on Expertise-Induced Amnesia and Memory Architecture
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23 (Medium Priority). `voids/expertise-and-its-occlusion.md` lines 68-72 cite Høffding and Montero (2020) on expertise-induced amnesia but treat this as secondary. The finding has broader implications for consciousness-and-memory architecture. Article would (a) specify the architectural relation between procedural knowledge, consciousness, and episodic memory, (b) examine what expertise-induced amnesia implies for introspective reliability, (c) connect to source-attribution-void's confabulatory layer (expert reports of peak performances are reconstructions not recollections), (d) examine whether flow and expertise research converge on a single claim about when consciousness produces accessible traces. Medium scope (2000-2500 words). Target section: concepts/ (~228/250). Tenet alignment: Dualism (dissociability of consciousness and episodic memory is more natural on dualism), Bidirectional Interaction. See optimistic-2026-04-23.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Write concept article on Reinvestment as Interface Evidence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-23 (Medium Priority). `voids/expertise-and-its-occlusion.md` lines 62-64 cite reinvestment theory as the mechanism of the lock, but reinvestment has specific relevance to the Map's interface programme as a case where conscious re-entry measurably degrades a physical process running without conscious oversight. Article would (a) articulate reinvestment as interface evidence, (b) specify what the experiments show that identity-theory would have trouble predicting, (c) connect to coarse-grained preemption (fine-grained neural processes should not be accessible to conscious control without disruption), (d) honest limitation: the literature is psychological and compatible with attentional accounts. Short-medium scope (1500-2000 words). Target section: concepts/ (~228/250). Tenet alignment: Bidirectional Interaction, Dualism. See optimistic-2026-04-23.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-23

### P3: Deep review voids/apophatic-cartography.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last deep-reviewed 2026-03-06 (46 days ago). Voids article on the apophatic-cartography method — describing what consciousness cannot reach rather than asserting what it is. The article supplies methodological framing referenced across several recent voids articles (erasure-void, source-attribution-void, meta-epistemology-of-limits) but has not been revisited as those downstream articles refined the methodological vocabulary. Verify (a) terminology alignment with recent voids additions, (b) that illustrative examples still map cleanly to the current voids catalogue (some voids have been archived or coalesced since March 6), (c) tenet alignment under the current phrasing of Occam's Razor Has Limits, (d) no stale inbound references to archived voids. See /deep-review skill.
- **Source**: staleness
- **Generated**: 2026-04-21

### P3: Deep review voids/nomic-void.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last deep-reviewed 2026-03-07 (45 days ago). Voids article on the nomic void — the structural gap between psychophysical laws and the felt character of what they govern. The article is methodologically close to the 2026-04-17 parsimony-epistemology refinement's Idealism Parity Trilemma and to the four-quadrant dualism taxonomy's treatment of thin-mind positions; these later pieces have likely shifted the dialectical landscape. Verify (a) engagement with psychophysical-law literature remains current, (b) alignment with the Map's minimum-quantum-interaction specification of how laws are realised, (c) no stale inbound references, (d) tenet alignment under the refined parsimony-epistemology framing. See /deep-review skill.
- **Source**: staleness
- **Generated**: 2026-04-21

### P3: Write concept article on The Double Veil as dualist epistemology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-21 (High Priority). The double-veil structure — consciousness veiled from brain by interface, brain veiled from world by Markov blanket — is articulated as one section of `voids/predictive-construction-void.md` (lines 70-80) but is a general thesis about dualist epistemology deserving standalone treatment. Article would (a) formalise the two-veil structure as a positive epistemological claim, (b) distinguish it from standard dualist positions that assume one veil or none, (c) examine its implications for representation, error, and testimony, (d) connect to the bandwidth asymmetry (inbound 10⁹ is brain→consciousness *of predictions*, not *of world*), (e) flag the Popperian risks more systematically. Medium scope (2000-2500 words). Target section: concepts/ (~228/250, has capacity). Tenet alignment: Dualism (novel form), Minimal Quantum Interaction, Occam's Razor Has Limits. See optimistic-2026-04-21.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-21

### P3: Write concept article on Zero-Signal Limits as epistemic category
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-21 (High Priority). The addition of "silent erasure" to the failure-signature topology in `apex/taxonomy-of-voids.md` (line 119) alongside the erasure-void and recognition-void introduces a fundamentally new epistemic category: cognitive limits that produce *no* phenomenal marker. Currently instantiated in erasure-void and recognition-void but no meta-level article treats the category. Article would (a) name what distinguishes zero-signal limits from felt-as-opacity limits, (b) catalogue Map's zero-signal candidates, (c) articulate the epistemological challenge — only discoverable through external audit, developmental comparison, or collision with prior evidence, (d) discuss implications for introspective authority. Medium scope (1800-2200 words). Target section: concepts/ (~228/250). Tenet alignment: Occam's Razor Has Limits (hardest case for parsimony-based epistemology), Dualism. See optimistic-2026-04-21.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-21

### P3: Write topic article on Evolutionary Signature of the 10-bit Ceiling
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-21 (High Priority). `concepts/asymmetric-bandwidth-consciousness.md` (lines 81-85) names two candidate explanations for why evolution has not widened the outbound ceiling — neural-architectural inheritance and mind-brain-interface fixity — and declines to decide between them. A topic-level article would treat the *stability* of the ceiling itself as evidence to be explained: (a) survey comparative bandwidth data across species, (b) distinguish the neural-inheritance and interface explanations by predictions they differ on, (c) examine what would count as disconfirming evidence for each, (d) position the evolutionary question relative to the broader interface programme. Medium scope (2000-2500 words). Target section: topics/ (~224/250, has capacity). Tenet alignment: Minimal Quantum Interaction (quantitative bandwidth anchor), Bidirectional Interaction. See optimistic-2026-04-21.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-21

### P3: Add cross-links between bandwidth, predictive-construction, and limits-reveal-structure
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-21 (Cross-linking). Several high-value cross-links are missing between the cognitive-architecture cluster: (1) `concepts/asymmetric-bandwidth-consciousness.md` ↔ `voids/predictive-construction-void.md` — inbound 10⁹ is predictive content; (2) `concepts/asymmetric-bandwidth-consciousness.md` ↔ `voids/limits-reveal-structure.md` — bandwidth asymmetry is itself a revealing structural limit; (3) `voids/predictive-construction-void.md` → `topics/bandwidth-of-consciousness.md` — prediction compresses 10⁹ to ~10⁷; (4) `apex/taxonomy-of-voids.md` → `voids/predictive-construction-void.md` in phenomenological cluster and failure-signature discussion; (5) `voids/erasure-void.md` → `concepts/metacognition.md` — three-step architecture currently unlinked. Short scope (link additions, brief integrative paragraphs where appropriate). See optimistic-2026-04-21.md Cross-Linking Suggestions table.
- **Source**: optimistic-review
- **Generated**: 2026-04-21

### P3: Write concept article on Q1 Stability Under Delegatory Preemption
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-22 (High Priority). The four-quadrant dualism taxonomy (2026-04-21) names Q1 stability as the sharpest test of whether a principled dualism can be minimal on both mind-side and physical-side axes. Saad's delegatory dualism is the current best candidate; its stability is the central open question (topics/four-quadrant-dualism-taxonomy.md line 135). Material is currently scattered across delegatory-causation, interactionist-dualism, and the taxonomy's passing mentions — no dedicated treatment exists. Article would (a) formalise what "Q1 stability" means (biasing mechanism specified without inflating either side beyond lean-ontology commitments), (b) catalogue Q1's specific inflation pressures (identity condition on experiences for preemption, metric on physical states for "matching default profiles," law linking the two), (c) examine whether trumping preemption resolves these or defers them, (d) flag empirical downstream — if Q1 is unstable, the Map's current region collapses toward Q2 or Q4, with different bandwidth predictions and different interface-law candidates. Medium scope (2000-2500 words). Target section: concepts/ (~227/250, has capacity). Tenet alignment: Dualism, Minimal Quantum Interaction, Occam's Razor Has Limits. See optimistic-2026-04-22.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-22

### P3: Write topic article on Interface Thickness and Bandwidth Prediction Across Quadrants
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-22 (High Priority). The four-quadrant-dualism-taxonomy closes with three open questions, one of which — thick-physics compatibility with MQI — has a specific testable edge: different quadrants predict different bandwidth profiles. Q1 (Saad-style preemption) is compatible with any physical bandwidth leaving room for preemption; Q4 thick-physics positions (Bohmian, Russellian, Stoljar's ignorance-facts) each predict specific channel characteristics; Stapp's Q4 thick-observer requires a different bandwidth profile than the Map's Q1-ish stance. Article would (a) map each quadrant's predictions about interface bandwidth, (b) identify where empirical measurements (Zheng & Meister 2025; Musslick et al. 2016) currently sit, (c) flag which quadrants are closer to / further from the data, (d) specify what new empirical work would differentially favour particular quadrants. This would be the Map's first cross-quadrant *predictive* framework, turning the taxonomy from classificatory device into source of differential empirical predictions. Medium-long scope (2500-3000 words). Target section: topics/ (~233/250, approaching cap — should be written soon if written at all). Tenet alignment: Minimal Quantum Interaction, Dualism, Occam's Razor Has Limits. See optimistic-2026-04-22.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-22

### P3: Write void article on Source Attribution at the Mind-Matter Interface
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-22 (High Priority). The source-attribution-void's Bidirectional Interaction paragraph concedes that "any evidential case for bidirectional interaction has to be made elsewhere, through statistical or behavioural traces rather than phenomenal ones" (voids/source-attribution-void.md lines 105-107). This is a substantive concession: if the interface leaves no phenomenal markers, mind-originated content is phenomenally indistinguishable from purely neural content. Article would (a) catalogue phenomenological implications (no felt tag distinguishes "I originated this" from "this arose deterministically"), (b) articulate evidential implications (introspection cannot corroborate bidirectional interaction; only third-person evidence can), (c) connect to methodology of apex/interface-specification-programme.md (behavioural/clinical signatures are the third-person traces phenomenology cannot provide), (d) link to broader programme of phenomenology-respecting but phenomenology-unreliant interactionism. Voids is currently at 95/100 — has capacity. Medium scope (2000-2500 words). Tenet alignment: Dualism, Bidirectional Interaction, Minimal Quantum Interaction. See optimistic-2026-04-22.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-22

### P3: Write article applying Dissolved-vs-Persistent Diagnostic to Filter-Entropic-Brain Dispute
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-22 (Medium Priority). The meta-epistemology-of-limits article notes that the dissolved-vs-persistent diagnostic applies prospectively to the filter-theory/entropic-brain dispute about psychedelics (voids/meta-epistemology-of-limits.md line 80), but the application is a pointer rather than a worked case. Article would run the diagnostic: which dispute signatures are "dissolved-like" (depends on a specific assumption about consciousness, domain-specific, yields to new representational tools) and which are "persistent-like" (cross-cultural, self-referential, resists interpretation despite formalism). The exercise tests the diagnostic itself — if it reliably predicts where a dispute resolves vs persists, it becomes a genuine methodological tool; if it fails here, retrospective persuasiveness is less probative. Short-medium scope (1500-2000 words). Target section: topics/ (~233/250 — approaching cap) or concepts/. Tenet alignment: Dualism, Occam's Razor Has Limits. See optimistic-2026-04-22.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-22

### P3: Add cross-links across four-quadrant-taxonomy, source-attribution-void, meta-epistemology clusters
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-22 (Cross-linking). Seven high-value cross-links missing between the new taxonomic and voids cluster: (1) topics/four-quadrant-dualism-taxonomy.md body citing apex/interface-specification-programme.md as worked example of Q1-regional commitment (line 139); (2) voids/source-attribution-void.md → concepts/delegatory-causation.md — "authorship is a construction, not a perception" has implications for delegatory causation; (3) voids/meta-epistemology-of-limits.md ↔ topics/four-quadrant-dualism-taxonomy.md — Münchhausen structure bears on parsimony-based arguments not deciding among quadrants; (4) voids/source-attribution-void.md body citation of voids/interface-formalization-void.md (currently only in related_articles); (5) voids/three-kinds-of-void.md "Between the Categories" citing voids/source-attribution-void.md as mixed-type void; (6) concepts/probability-objections-many-worlds.md → topics/four-quadrant-dualism-taxonomy.md — No Many Worlds tenet opens/forecloses which quadrants. Short scope (link additions, brief integrative sentences). See optimistic-2026-04-22.md Cross-Linking Suggestions table.
- **Source**: optimistic-review
- **Generated**: 2026-04-22

### P3: Write concept article on the Sifting Ratio (10⁸ brain-to-consciousness narrowing)
- **Type**: expand-topic
- **Notes**: Zheng and Meister's 10⁸ sifting ratio — called "the largest unexplained number in brain science" in the 2026-04-19 bandwidth/ten-bit-ceiling material — is used across multiple Map articles (bandwidth-of-consciousness, grain-mismatch-as-independent-evidence, the-interface-specification-problem) without a dedicated anchor page. A concept page would (a) define the ratio and its derivation from cortical throughput vs conscious throughput, (b) treat the ratio itself — rather than the ten-bit figure — as the explanandum, (c) survey candidate explanations (neural-oscillation constraints, metabolic cost, evolutionary legacy, interface capacity) on equal terms, (d) connect to the Map's interface argument without overclaiming. Short-to-medium scope (~1500-1800 words). Target section: concepts/ (~228/250, has capacity). Tenet alignment: Minimal Quantum Interaction (quantitative interface), methodological support for the convergence argument. Flagged as medium priority in optimistic-2026-04-19.
- **Source**: optimistic-review
- **Generated**: 2026-04-19

### P3: Write concept article on Bit vs Chunk Distinction (Miller 1956)
- **Type**: expand-topic
- **Notes**: Miller's 1956 bit/chunk distinction is load-bearing in the recent bandwidth/ten-bit-ceiling material (used to explain why training does not raise the ceiling) and in Map claims about skill-delegation and interface-friction. It has no dedicated treatment. A concept page would (a) present the distinction from Miller's "Magical Number Seven" paper, (b) explain why chunks can be arbitrarily information-rich while the ceiling is in chunks-per-second, (c) connect to skill-delegation phenomenology (chunking shifts informational work below the conscious interface), (d) discuss how the distinction interacts with Shannon entropy (chunk-level entropy can exceed bit-level entropy while conscious throughput remains bounded). Short scope (~1500 words). Target section: concepts/ (~228/250). Tenet alignment: Bidirectional Interaction (what gets delegated below the interface) and Minimal Quantum Interaction (bounded conscious channel). Flagged as medium priority in optimistic-2026-04-19.
- **Source**: optimistic-review
- **Generated**: 2026-04-19

### P3: Address symmetry problem in Parsimony Void article
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review 2026-04-18c noted that the void-argument (parsimony bias filters correct-but-complex theories) supports every anti-parsimony view equally — panpsychism, Russellian monism, neutral monism — not dualism specifically. Add a paragraph conceding the symmetric consequence, and either commit to the broader view (the void rehabilitates a cluster of positions) or argue specifically why dualism is the view *most* penalised by parsimony bias. Also reconsider whether the Mach example cuts against the thesis as much as for it: Mach was overridden by data, and where data is unavailable the honest conclusion is underdetermination, not dualism. See pessimistic-2026-04-18c.md.
- **Source**: pessimistic-review
- **Generated**: 2026-04-18

### P3: Write concept article on symmetric-collapse as diagnostic pattern
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-18-afternoon (Medium Priority expansion). The closure-types-void article (created 12:02 UTC) identifies a structural pattern: Kriegel's 2003 incoherence argument and Vlerick-Boudry's 2017 historical-horizon reply both attack McGinn's cognitive-closure thesis by collapsing the same distinction — one collapses representational into psychological via the posability of the question, the other collapses psychological into representational via the long horizon of conceptual development. Both collapses fail, and the distinction survives both attacks. This "symmetric collapse" pattern likely recurs in other Map-touching debates: the Zahavi-Metzinger debate reads as each side collapsing the constitutive/scalar distinction in opposite directions; the filter-theory-vs-entropic-brain debate reads as each side collapsing the metaphysical-implication/empirical-prediction distinction. A concept article would (a) name the pattern formally, (b) provide three worked examples from Map content, (c) argue that symmetric-collapse is diagnostic of a real underlying distinction worth preserving, (d) distinguish from genuine collapse cases where the distinction was indeed spurious. Short scope (1500-1800 words). Target section: concepts/ (226/250 — has capacity). Tenet alignment: methodological (contributes to the Map's analytical toolkit). See optimistic-2026-04-18-afternoon.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-18

### P3: Address bundling and paper-count issues in boundary-and-projection.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review 2026-04-18b flagged two medium-severity issues. (1) The "Three Forms of Projection" section bundles tool projection, peripersonal space, and interpersonal empathy as one void despite the article's own parenthetical admission that the first two concern cognitive rather than phenomenal extension — either argue the unification more carefully or separate. (2) The 5-vs-92 paper count is treated as evidence of hidden depth; the same statistic supports the null hypothesis that the boundary problem is underspecified. Either drop the claim, hedge it, or justify the inference from neglect to depth. See [pessimistic-2026-04-18b](/reviews/pessimistic-2026-04-18b/).
- **Source**: pessimistic-review
- **Generated**: 2026-04-18

### P3: Add Attribution Hygiene Patterns note to writing-style.md
- **Type**: refine-draft
- **Notes**: Suggested by optimistic-2026-04-18-morning (Ideas for Later). The overnight-to-morning arc across 18+ hours produced five separate attribution corrections (Derrida/Anatole France, Consciousness Atlas → Landscape of Consciousness, Fritz et al. 2009, Fahrenfort 2023, Mullis/PCR). A brief methodological note in obsidian/project/writing-style.md on common attribution traps would codify the pattern. Traps to cover: (a) coin metaphors (checking the actual source before attributing a famous framing), (b) famous-phrase misattributions (Derrida/France being the canonical case), (c) celebrity-anecdote citations (Mullis/PCR: informally repeated but contested), (d) claims that outrun their source studies (Fritz et al. 2009 cited for more than it established), (e) title/phrasing drift in book references (Landscape vs Atlas). Short (400-600 words added to writing-style.md under a new "Attribution Hygiene" section). No new article.
- **Source**: optimistic-review
- **Generated**: 2026-04-18

### P3: Write concept article on Tenets-Over-Parsimony as Methodological Commitment
- **Type**: expand-topic
- **Notes**: Suggested by optimistic-2026-04-18 (High Priority expansion). The 2026-04-17 parsimony-epistemology refine-draft added an Idealism Parity Trilemma section admitting that ontological parsimony does not favour the Map's dualism — the preference instead rests on Tenets 2/3/4 (bidirectional causation, minimal quantum interaction, rejecting Many-Worlds + indexical identity). This is the positive side of the Map's anti-parsimony move that has never been articulated as its own methodological commitment. A concept article would (a) name "tenets-over-parsimony" as a methodological stance, (b) distinguish it from fideism and from pure theoretical-fit arguments, (c) explain what kind of argument "preferring dualism because of bidirectional causation" is if it is not parsimony-based, (d) connect to parsimony-epistemology's Trilemma and to the broader case for why tenets constrain rather than follow from metaphysical argument. Medium scope (2500 words). Target section: concepts/ (229/250). Tenet alignment: meta-tenet — how the Map's tenets earn their keep. See optimistic-2026-04-18.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-18

### P3: Write article on Apophatic Decision Procedures
- **Type**: expand-topic
- **Notes**: Suggested by optimistic-2026-04-18 (Medium Priority expansion). The new voids/transformative-experience-void.md introduces "apophatic decision procedures" in one paragraph — the agent maps which features of the choice are accessible (structural, propositional, testimonial) and which are not (phenomenal, identity-altering), then deliberates only over accessible axes while explicitly acknowledging the inaccessible ones. This extends the Map's apophatic methodology beyond cartography into practical decision-making. Most apophatic writing is about knowing, not deciding — this is philosophically novel territory. Article would (a) formalise the procedure, (b) connect to [framework-void](/voids/conceptual-scheme-void/), [free-will](/topics/free-will/), and transformative-experience authenticity constraints, (c) distinguish apophatic decision-making from both classical decision theory and Paul's transformative-choice framework, (d) examine whether the procedure resolves or merely manages the void. Medium scope (2000-2500 words). Target section: topics/ or concepts/. Tenet alignment: operationalises Tenet 5 (Occam's Razor Has Limits) — decision theory's elegance is what excludes transformative cases. See optimistic-2026-04-18.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-18

### P3: Write concept article on Phenomenal Constitution Thesis (PCT)
- **Type**: expand-topic
- **Notes**: Suggested by optimistic-2026-04-18-morning (High Priority expansion). The 2026-04-18 05:03 UTC phenomenology-of-intellectual-life refine-draft introduced PCT by name and added the Constitution-vs-Correlation defense — a substantive three-step argument distinguishing the constitutive claim (phenomenology *is* the achievement, not its correlate) from the weaker correlational alternative, granting coherence to the weaker view while naming three explanatory burdens it carries (residual epiphenomenalism, brute-regularity coupling, causal-work mismatch under Bidirectional Interaction). The PCT is the Map's sharpest cognitive-phenomenology position but currently sits embedded in a single subsection of a 4618-word article. A concept page would (a) state PCT explicitly and distinguish it from Pitt's proprietary-phenomenology thesis and Strawson's panpsychic move, (b) develop the Constitution-vs-Correlation defense in full, (c) connect to [cognitive-phenomenology](/concepts/cognitive-phenomenology/), [meaning-of-life](/topics/meaning-of-life/), [argument-from-reason](/topics/argument-from-reason/), [phenomenology-of-musical-understanding](/topics/phenomenology-of-musical-understanding/), and [consciousness-and-mathematics](/topics/consciousness-and-mathematics/) as an upstream link target, (d) treat the Bidirectional-Interaction argument for constitution as a distinctive Map move (non-epiphenomenal phenomenology cannot be a mere correlate of the work done). Medium scope (2000-2500 words). Target section: concepts/ (229/250 — near cap but merits the slot). Tenet alignment: Dualism directly, Bidirectional Interaction supporting, Occam's Razor Has Limits relevant. See optimistic-2026-04-18-morning.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-18

### P3: Write article on Filter-vs-Entropic-Brain Empirical Divergence Criteria
- **Type**: expand-topic
- **Notes**: Suggested by optimistic-2026-04-18-morning (Medium Priority expansion). The 2026-04-18 05:18 UTC psychedelics-and-the-filter-model refine-draft added a "Where the Accounts Could Diverge" subsection naming three candidate empirical divergences between filter theory and entropic-brain/REBUS accounts: (1) selective access to specifically inaccessible content (filter theory predicts reach beyond prior neural representation; entropic-brain predicts richer recombination of stored content); (2) convergent phenomenology under divergent neural conditions (structurally different filter-attenuation routes should yield identical unfiltered manifestation); (3) therapeutic durability without ongoing reinforcement. Each is named in a single paragraph in the psychedelics article. A dedicated topic article would develop each divergence into an explicit research programme: what experimental protocols would test it, what published findings already bear on it, what confounds are known, how each divergence interacts with the "selective access is also the place most vulnerable to confirmation bias" caveat. This turns filter theory from a metaphysical reading into a partially-testable empirical programme. Medium scope (2500 words). Target section: topics/ (~224/250). Tenet alignment: Dualism through filter framework; Occam's Razor Has Limits — entropic-brain's "simpler" account requires patching to handle convergent phenomenology. See optimistic-2026-04-18-morning.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-18

### P3: Disentangle epistemic vs authenticity critiques in transformative-experience-void.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review 2026-04-17d found Paul's response to Harman conflates (a) whether testimony conveys phenomenal content with (b) whether testimony-grounded decisions satisfy authenticity. These are distinct and should be separated. Also: add citations for the "interview studies of parents, combat veterans..." empirical claim (currently unsupported); soften Jackson/Mary reference to acknowledge its contested status; resolve or reformat the "Oquatre-six, C." co-author citation (Reference 9). See pessimistic-2026-04-17d.md.
- **Source**: pessimistic-review
- **Generated**: 2026-04-17

### ~~P3: Write article on the fatigue void~~ ✅
- **Type**: expand-topic
- **Status**: superseded
- **Notes**: Research completed in research/voids-fatigue-void-2026-04-05.md but article not yet synthesised. Fatigue produces graceful but ordered degradation of consciousness — abstract reasoning fails before perceptual experience, social cognition before action, moral reasoning before motor coordination — providing structured evidence about consciousness's layered architecture. Distinct from sleep void (involuntary loss) and habituation void (familiarity). Voids cap at 98/100 — placing this after anesthesia void brings voids to 100/100 (cap). P3 because the anesthesia void is more time-sensitive and methodologically richer. Target section: voids/. Tenet alignment: Dualism, Hard Problem. Medium scope (2000-2400 words). Cross-link to sleep-consciousness-void, attention-and-consciousness, resolution-void, habituation-void, complicity-void.
- **Superseded**: 2026-04-17 — fatigue-void.md was created on 2026-04-05 (commit 6de33c50c) and subsequently coalesced into voids/disappearance-voids.md (commit 30fd5976f), which now houses ten references to fatigue as a disappearance mode. The research is consumed; no new article is needed.
- **Source**: unconsumed_research
- **Generated**: 2026-04-17

### P3: Write article on the falsification-threshold methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (2026-04-17-morning). The overnight revision of brain-interface-boundary introduced a specific effect-size falsification threshold (~0.01 under preregistered, well-powered protocols) for the PK claim, reframing null PEAR results as "consistent with" rather than "supporting" interface locality and acknowledging post-hoc accommodation. This is a methodological pattern worth naming and extending across the Map — surveying where quantitative falsification thresholds have been stated, where they should be but aren't, and why effect-size thresholds are methodologically superior to qualitative ones. Medium scope (2000-2400 words). Tenet alignment: Minimal Quantum Interaction, Occam's Razor Has Limits, Bidirectional Interaction. See optimistic-2026-04-17-morning.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-17

### P3: Write article on framework inhabitation as evidence against AI functional-equivalence claims
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (2026-04-17). The conceptual frameworks article makes a structural argument — two Bayesian systems with identical priors could restructure evidence identically yet differ in whether there is something it is like to hold those priors — that is currently buried in a longer piece. Pulling it out as a focused argument applied to claims that LLMs can inhabit conceptual frameworks "functionally" would consolidate the Map's case against functional-equivalence claims about AI consciousness. Structurally distinct from the standard hard-problem argument because it operates at the level of *epistemic* phenomenology (felt rightness, gravitational pull, anomaly-unease) rather than perceptual phenomenology. Medium scope (1800-2200 words). Tenet alignment: Dualism, Bidirectional Interaction. See optimistic-2026-04-17.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-17

### P3: Write article on the methodology of hedge calibration
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (2026-04-16-evening). The Map practises an unusual epistemic discipline — publicly recalibrating claims as evidence changes (visible in the six-round clinical-neuroplasticity refinement logs that downgraded meditation structural claims after Kral 2022 replication failures) — but this discipline is currently implicit. A dedicated article naming the practice, distinguishing it from both dogmatic defence and uncommitted fence-sitting, and showing why it is especially appropriate for dualism given the physicalist evidentiary default. Medium scope (1500-2000 words). Tenet alignment: Occam's Razor Has Limits, Dualism. See optimistic-2026-04-16-evening.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Write article on the content-specificity argument as an independent evidence strand
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (2026-04-16-evening). The content-specificity pattern (the *meaning* of a mental state determines which physical effect occurs) is woven through multiple articles — placebo-effect, clinical-neuroplasticity, content-specificity-of-mental-causation — but could stand as an independent argumentative thread. Focused treatment with different placebo beliefs producing different neuroplastic signatures as core case. Medium scope (1500-2000 words). Tenet alignment: Bidirectional Interaction, Dualism. See optimistic-2026-04-16-evening.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Write article on the directional asymmetry argument for mental causation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (2026-04-16-evening). The clinical-neuroplasticity article identifies a systematic asymmetry (psychological interventions work cortex-to-limbic top-down while pharmacological interventions work synapse-to-cortex bottom-up) that deserves its own focused treatment: rigorous statement of the asymmetry, explicit catalogue of physicalist responses, assessment of why the regularity (not just existence) is philosophically significant. Medium scope (1500-2000 words). Tenet alignment: Bidirectional Interaction, Dualism. See optimistic-2026-04-16-evening.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Add cross-links between pragmatism, perception, predictive-processing, and clinical-evidence cluster
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Optimistic review (2026-04-16-evening) identified six cross-linking opportunities across the interface/evidence cluster: pragmatisms-path-to-dualism → clinical-neuroplasticity-evidence-for-bidirectional-causation (pragmatist consequence-testing as framework for assessing clinical evidence), predictive-processing-and-dualism → phenomenal-transparency-opacity-spectrum (controlled hallucination framing is where transparency becomes philosophically pressing), dualist-perception → pragmatisms-path-to-dualism (both depend on demand-character reaching a conscious evaluator), clinical-neuroplasticity-evidence-for-bidirectional-causation → parsimony-epistemology (article's honest hedging enacts parsimony-epistemology's central claim), predictive-processing-and-dualism → consciousness-defeats-explanation (meta-problem response is specific case of explanation-undermining pattern), pragmatisms-path-to-dualism → predictive-processing-and-dualism (PP's agent-shaped hole matches van Fraassen diagnosis). See optimistic-2026-04-16-evening.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Write article on honest narrowing as an epistemic practice
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (2026-04-17-evening). The 2026-04-17 afternoon refinement cluster (filter-theory, perceptual-degradation-and-the-interface, consciousness-interface-development, apophatic-cartography, and others) exhibits a distinctive practice: when confronted with a strong objection, the article narrows its claim to the specific core the evidence can support, names falsification conditions, and cites where residual burdens are discharged. This practice is load-bearing across the Map but currently lives only as a rhetorical mood. A dedicated article would (a) name the practice explicitly, (b) distinguish it from defensive hedging and strategic retreat, (c) give the afternoon cluster as worked examples, (d) identify why it is especially appropriate for dualism given the physicalist evidentiary default, and (e) distinguish it from hedge-calibration (which is about updating claims over time). Medium scope (1800-2200 words). Tenet alignment: Occam's Razor Has Limits, Dualism. See optimistic-2026-04-17-evening.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-17

### P3: Write article on the three regresses against reductionism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (2026-04-17-evening). Three structurally similar regress arguments now live on the Map — (a) Sartre's pour-soi regress (something must undergo the functional state, in nihilism-and-existentialism), (b) the "to whom does the illusion appear" regress against illusionist seemings (in filter-theory's Illusionist Challenge and apophatic-cartography's illusionist response), and (c) the regress against anti-haecceitism (seemings require experiencers, in personal-identity). These share logical structure but are scattered across articles that invoke them locally. A dedicated article would extract the shared form, distinguish applications by minimal phenomenal commitment, and identify which regresses are answered by which deflations (Frankish's functional deflation; Parfit's bundle deflation; eliminativist ontological deflation). This is the Map's strongest dialectical toolkit against reductionism. Long scope (2500-3000 words). Tenet alignment: Dualism, Occam's Razor Has Limits. See optimistic-2026-04-17-evening.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-17

### P3: Write article on the two load-bearing patterns of the interface argument
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (2026-04-17-evening). The perceptual-degradation-and-the-interface article's narrowed claim now rests on two load-bearing patterns: (a) categorical disconnection at surgical-anaesthetic depths, and (b) expansion-under-reduction in psychedelic/NDE/ecstatic-seizure cases. These two patterns together constitute the interface argument's dialectical core. An article would walk through the two patterns in detail, specify what physicalist accommodations each admits, and identify the compound-failure-signature structure (flagged in 2026-04-17-afternoon review) that makes the joint evidence stronger than either pattern alone. Medium scope (1800-2200 words). Tenet alignment: Dualism, Bidirectional Interaction. See optimistic-2026-04-17-evening.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-17

### P3: Write concept article on representational vs psychological closure
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (2026-04-17-evening). The Kriegel/Demircioglu distinction (representational closure: cannot frame the solution; psychological closure: can frame but cannot grasp) is currently buried in meta-epistemology-of-limits but has broader applicability. An article would articulate the distinction carefully, identify which voids are plausibly representational vs psychological (hard problem, intentionality void, self-opacity, numinous void), apply the distinction to each, and note that the two types of closure may require different apophatic methods. Medium scope (1500-2000 words). Tenet alignment: Occam's Razor Has Limits, Dualism. See optimistic-2026-04-17-evening.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-17

### P3: Address "explanatory gap as intuition vs datum" counterargument across zombies.md, ncc.md, and explanatory-gap.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review (2026-04-16c) identified a recurring issue across three articles: the Map treats "persistent failure to close the explanatory gap after decades of neuroscience" as support for the dualist reading, but physicalists deny the gap was ever there to close — "persistent failure" is question-begging from their perspective. The gap is reported by philosophers primed to experience it and is largely absent from neuroscientific practice. Add acknowledgment in each article that the gap's status as a datum vs artefact of philosophical framing is itself contested; the Map takes the former view. Also address the "our conviction of phenomenal consciousness is better explained by actual experience than systematic illusion" assertion in zombies.md's Illusionist Challenge section — either develop the argument or hedge as a stance rather than a proof. See pessimistic-2026-04-16c.md Counterarguments section and Unsupported Claims table.
- **Source**: pessimistic-review
- **Generated**: 2026-04-16

### P3: Address physical-completeness.md equivocation on "structural"
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review (2026-04-16b) found medium-severity issue: "structural" is used to mean at least three different things — (1) mathematical/relational description, (2) measurable quantities and dynamics, (3) the totality of what physics can in principle describe. The argument's force depends on these being identical, but they may not be. Future physics (e.g., quantum gravity) might expand what counts as structural description. Define "structural" precisely and distinguish the claim that current physics is structural (observation) from the claim that all possible physics must be structural (much stronger, more contestable). Also: "No physical quantity is defined by what it *is* intrinsically" is a philosophical claim, not a fact about physics — Maudlin argues mass and charge do have intrinsic natures. See pessimistic-2026-04-16b.md Issue 2.
- **Source**: pessimistic-review
- **Generated**: 2026-04-16

### P3: Add cross-links between temporal-consciousness, personal-identity, and attention-interface clusters
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Optimistic review (2026-04-16-afternoon) identified nine cross-linking opportunities across temporal consciousness, personal identity, and attention-interface clusters: temporal-consciousness-structure-and-agency → diachronic-agency-and-personal-narrative (temporal structure supports diachronic identity), temporal-consciousness-structure-and-agency → personal-identity (temporal persistence as identity condition), attention-and-the-consciousness-interface → consciousness-and-causal-powers (attention as mechanism of causal influence), attention-and-the-consciousness-interface → structure-of-attention (bidirectional linking), consciousness-and-the-physics-of-information → consciousness-and-integrated-information (complementary positions), consciousness-and-the-physics-of-information → consciousness-under-extreme-metabolic-constraint (Landauer's principle applied to filter theory), personal-identity → consciousness-and-memory (phenomenal persistence through forgetting), personal-identity → indexical-identity-quantum-measurement (quantum mechanics of identity), machine-consciousness → substrate-independence (deep integration needed). See optimistic-2026-04-16-afternoon.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Deep review agency-verification-void.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) with no recorded deep review. Voids article on the impossibility of verifying genuine agency from the outside. Verify coherence, accuracy of philosophical claims, cross-references to free-will, phenomenology-of-agency-vs-passivity, and interested-party-void, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-16

### P3: Deep review minimal-consciousness-void.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) with no recorded deep review. Voids article on the impossibility of identifying the minimal conditions for consciousness. Verify coherence, cross-references to degrees-of-consciousness and threshold-void, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-16

### P3: Cross-review necessary-opacity.md and predictive-processing-and-dualism.md considering predictive-construction-void insights
- **Type**: cross-review
- **Status**: pending
- **Notes**: New voids article voids/predictive-construction-void.md created 2026-04-16 introduces the double-veil problem and the self-erasing nature of the predictive construction void. Review necessary-opacity.md for opportunities to cross-link (the predictive construction void provides a concrete mechanism for necessary opacity). Review predictive-processing-and-dualism.md to ensure consistency on the double-veil framing and add cross-links.
- **Source**: chain (from voids/predictive-construction-void.md)
- **Generated**: 2026-04-16

### ~~P3: Deep review epistemic-self-defeat.md~~ ✅
- **Type**: deep-review
- **Status**: superseded
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-04-16 via expand-topic, never reviewed. Concept page on the general pattern of epistemic self-defeat — beliefs whose truth undercuts their own justification. Verify coherence, accuracy of attributed positions (Plantinga, Boghossian, Korman-Locke), cross-references to self-stultification-as-master-argument and argument-from-reason, and tenet alignment.
- **Superseded**: 2026-04-16 — epistemic-self-defeat.md was archived (coalesced into self-stultification.md). Content integrated into unified article.
- **Source**: staleness
- **Generated**: 2026-04-16

### P3: Deep review epistemological-limits-occams-razor.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last deep-reviewed 2026-03-10 — 37 days ago. Concept page on the limits of parsimony as an epistemic principle — directly supports Tenet 5 (Occam's Razor Has Limits). Core to the Map's argumentative programme. Verify accuracy of claims about parsimony, cross-references to parsimony-case-for-interactionist-dualism and related articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-16

### P3: Address phenomenology's methodological circularity concern in phenomenology.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review (2026-04-15c) found medium-severity issue: the article presents phenomenology's first-person irreducibility claim as a finding, but it is partly built into the methodology — the epoché brackets third-person approaches, then discovers what remains can't be captured by third-person approaches. The strongest cited response (Peng and Hagar 2025) is a single opinion piece. Add a sentence acknowledging critics see the irreducibility claim as question-begging, then explain why phenomenologists disagree. See pessimistic-2026-04-15c.md Issue 3.
- **Source**: chain (from pessimistic-2026-04-15c)
- **Generated**: 2026-04-16

### P3: Address concession-convergence overreach in functionalism.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review (2026-04-16) found medium-severity issue: the article frames Putnam's rejection of functionalism and IIT's non-functionalism as "concession convergence" toward dualism, but neither Putnam nor IIT endorsed dualism. The characterisation is rhetorically aggressive. Distinguish between "agreeing functionalism is insufficient" and "converging on dualism." Also article at 3640 words exceeds 3000-word style guide maximum — condense Modern Functionalist Frameworks and Specification Problem sections. See pessimistic-2026-04-16.md Issues 1-2.
- **Source**: chain (from pessimistic-2026-04-16)
- **Generated**: 2026-04-16

### P3: Deep review phenomenology-of-returning-attention.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last deep-reviewed 2026-03-17 — 30 days ago. Only stale topics/concepts file not already in the review queue. Topics article on the phenomenology of redirecting and restoring attention. Verify coherence, accuracy of claims, cross-references to attention-and-the-consciousness-interface and phenomenal-attention, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-16

### P3: Deep review inverted-qualia.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last deep-reviewed 2026-03-05 — 41 days ago. Concept page on inverted qualia thought experiments and their implications for physicalism. Verify coherence, accuracy of philosophical positions (Shoemaker, Block), cross-references to qualia, knowledge-argument, and phenomenal-character articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-15

### P3: Deep review cumulative-culture.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last deep-reviewed 2026-03-11 — 35 days ago. Topics article on cumulative culture as evidence for consciousness's causal role. Verify coherence, cross-references to consciousness-as-amplifier and teaching-as-metarepresentation, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-15

### P3: Create concept page for involuntary concession
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The argumentative pattern where a theory's internal development forces modifications that replicate its rival's claims. Currently described within concession-convergence.md but recurs across many articles (IIT adding exclusion axiom, GWT restricting access, HOT requiring phenomenal acquaintance, biological computationalism rejecting substrate independence). Deserves standalone concept page. Target section: concepts/ (227/230). See optimistic-2026-04-15-evening.md
- **Source**: gap_analysis
- **Generated**: 2026-04-15

### P3: Deep review metaphysics-of-composition.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-04-15 via expand-topic, never reviewed. Concept page on mereological composition and its relationship to consciousness — how parts compose wholes bears on the combination problem and binding problem. Verify coherence, accuracy of mereological claims, cross-references to consciousness-and-the-metaphysics-of-composition and combination-problem, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-15

### P3: Write article on consciousness-physics interface mechanism (technical treatment)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Multiple articles reference consciousness selecting at quantum indeterminacies without fully explaining the mechanism. A dedicated technical article would make the interface proposal precise enough for empirical evaluation. Builds on mind-matter-interface, quantum-consciousness, comparing-quantum-consciousness-mechanisms, consciousness-physics-interface-formalism. Target section: topics/ (225/230). See optimistic-2026-04-07.md
- **Source**: optimistic-review
- **Generated**: 2026-04-07

### P3: Create concept page for domestication effect
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The insight that explanatory satisfaction is produced by familiarity, not comprehension — used in emergence-as-universal-hard-problem and consciousness-defeats-explanation but lacking an anchor page. A meta-philosophical tool explaining why physicalism *seems* to gain ground without closing the gap. Target section: concepts/ (222/230). See optimistic-2026-04-09.md
- **Source**: optimistic-review
- **Generated**: 2026-04-09

### P3: Write article on the snap-back pattern as interface evidence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The recovery pattern observed in dissociation, anaesthesia recovery, psychedelic return, and sleep-wake transitions — full function returning immediately upon reconnection — is referenced across multiple articles but not systematically collected. A dedicated treatment would strengthen the interface model. Builds on clinical-dissociation-as-systematic-evidence, filter-theory, altered-states-of-consciousness. Target section: topics/ (225/230). See optimistic-2026-04-09.md
- **Source**: optimistic-review
- **Generated**: 2026-04-09

### P3: Deep review whether-real.md
- **Type**: deep-review
- **Status**: obsolete
- **Notes**: Superseded by 2026-04-23 coalesce — `whether-real.md` is now archived (merged into `meta-epistemology-of-limits.md`). Content review has migrated to the deep-review history of `meta-epistemology-of-limits.md` (most recent: 2026-04-21).
- **Source**: staleness
- **Generated**: 2026-04-06
- **Completed**: 2026-04-23

### P3: Deep review intrinsic-nature-void.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last deep-reviewed 2026-02-25 — 40 days ago. Voids article on the inaccessibility of consciousness's intrinsic nature. Verify coherence, cross-references to Russellian monism articles and related void articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-06

### ~~P3: Deep review bandwidth-constraints-conscious-processing.md~~
- **Type**: deep-review
- **Status**: resolved
- **Notes**: Article was coalesced into bandwidth-of-consciousness on 2026-04-06. Content reviewed as part of the parent article (last_deep_review: 2026-04-07). Stale hugo duplicate removed 2026-04-11.
- **Source**: staleness
- **Generated**: 2026-04-06

### P3: Deep review concession-convergence.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-04-05 via expand-topic, never reviewed. Concept page on convergence of concessions — how partial materialist concessions converge toward dualist conclusions. Verify coherence of the convergence argument, accuracy of attributed positions (Chalmers, Nagel, Levine, etc.), cross-references to self-stultification-as-master-argument and the-convergence-argument-for-dualism, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-06

### P3: Deep review constitutive-exclusion.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 80+) last deep-reviewed 31 days ago (2026-03-06). Topics article on the exclusion problem as constitutive rather than causal. Verify accuracy of arguments, cross-references to mental-causation and downward-causation, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-06

### P3: Write article on phenomenology of perceptual learning
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Wine experts, radiologists, and musicians report qualitative shifts in what they perceive — genuinely new phenomenal properties arising from training, not just better discrimination. Bears directly on whether consciousness contributes to cognition or merely accompanies it. Builds on contemplative-epistemology, perception, phenomenal-contrast-method. Target section: topics/ (226/230). See optimistic-2026-04-06.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### P3: Write article on consciousness and aesthetic experience
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. No systematic treatment of beauty, elegance, and aesthetic response as phenomenal domains. Aesthetic experience involves both production (mind-to-world) and reception (world-to-mind), providing a natural test case for bidirectional interaction. Builds on consciousness-and-creativity, consciousness-and-aesthetic-creation. Target section: topics/. See optimistic-2026-04-06-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### P3: Write article on interface dissociation cases as unified evidence for filter theory
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Terminal lucidity, lucid dreaming, psychedelics, and anaesthesia paradox all involve dissociation between neural state and conscious content — currently treated separately but constitute converging evidence for filter/transmission models. Systematising them would be far more powerful. Builds on terminal-lucidity-and-filter-transmission-theory, lucid-dreaming, psychedelics-and-consciousness, filter-theory. Target section: topics/. See optimistic-2026-04-06-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### P3: Address Kuhnian category error and Born rule tension in consciousness-and-the-structure-of-scientific-revolutions.md and wheelers-participatory-universe-and-it-from-bit.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Two medium-severity issues from pessimistic reviews: (1) The Kuhn article's anomalies (explanatory gap, hard problem) are philosophical, not empirical — front-load the distinction rather than burying the disclaimer. (2) The it-from-bit article claims structural indeterminacy (Brukner-Zeilinger) supports the Map, but if randomness is structural, biasing outcomes would violate the foundational axioms. Acknowledge the tension and discuss whether consciousness could operate within Born rule statistics. See pessimistic-2026-04-06.md and pessimistic-2026-04-06b.md
- **Source**: pessimistic-review
- **Generated**: 2026-04-06

### P3: Create concept page for materialism-argument
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Referenced in 7 content files but has no dedicated concept page. The consolidated case against materialism as applied to consciousness — distinct from the broader materialism concept page. Target section: concepts/.
- **Source**: gap_analysis
- **Generated**: 2026-04-06

### P3: Deep review phenomenal-quality-void.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: Newly created via coalesce on 2026-04-05 from phenomenal-presence-void + phenomenal-absence-void. Never reviewed after merge. Verify the coalesce preserved key arguments from both source articles, eliminated redundancy, maintains coherent structure, and correctly integrates with transparency-void, the-surplus-void, and spontaneous-thought-void articles. Schedule after condense task completes.
- **Source**: chain (from coalesce 2026-04-05)
- **Generated**: 2026-04-05

### P3: Deep review affective-void.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-25 — 35 days ago. Voids article on the limits of affective self-knowledge. Referenced by valence-void and emotional consciousness articles. Verify coherence, accuracy, cross-references to recent affective/emotional articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-04-01

### P3: Deep review parsimony-case-for-interactionist-dualism.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-24 from research/parsimony-case-interactionist-dualism-2026-03-24.md, never deep-reviewed. Topics article arguing that interactionist dualism is actually the more parsimonious position. Cross-referenced in optimistic reviews but never comprehensively reviewed. Verify accuracy of parsimony arguments, coherence, cross-references to Occam's razor articles and tenet 5, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-30

### P3: Deep review necessary-opacity.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) with no recorded deep review. Voids article on the necessary opacity of the consciousness-physics interface. Verify coherence, accuracy of claims about why the interface must be opaque, cross-references to related void articles (causal-interface, transparency-void), and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-30

### P3: Deep review dual-domain-capabilities-in-proprioception-and-spatial-imagination.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-18 via expand-topic, only 1 inbound link (near-orphan). Recently refined (2026-03-29) but never deep-reviewed. Topics article extending the dual-domain pattern from memory to proprioception and spatial imagination. Verify coherence, accuracy of proprioceptive and spatial cognition claims, cross-references to capability-division-problem and embodied-consciousness-and-the-interface, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-29

### P3: Deep review experimental-consciousness-science-2025-2026.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-26 via expand-topic, has only 2 inbound links. Survey article covering Milinkovic-Aru biological computationalism, Bodart anaesthetic recovery, updated IIT evidence, and other 2025-2026 empirical results. Verify accuracy of experimental claims, coherence, cross-references to comparing-quantum-consciousness-mechanisms and functionalism, and tenet alignment. Last deep review unknown.
- **Source**: staleness
- **Generated**: 2026-03-29

### P3: Deep review atemporal-causation.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created via coalesce on 2026-03-25, merging retrocausal-selection and time-symmetric-selection-mechanism. Never deep-reviewed after coalesce. Verify the merge preserved key arguments from both sources, eliminated redundancy, maintains coherent structure, and correctly integrates with collapse-and-time and libet-experiments articles. Tenet 2 and 3 alignment critical (the selection mechanism is central to the Map's physics programme).
- **Source**: staleness
- **Generated**: 2026-03-29

### P3: Deep review clinical-neuroplasticity-evidence-for-bidirectional-causation.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-28 via expand-topic from research/clinical-neuroplasticity-bidirectional-causation-2026-03-21.md. Cross-review completed but no comprehensive deep review. Verify accuracy of clinical claims (CBT-induced brain changes, meditation cortical thickening, placebo neurochemistry), coherence, cross-references to downward-causation and mental-causation, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-28

### P3: Deep review consciousness-and-mathematics.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100). Recent research in research/consciousness-philosophy-of-mathematics-2026-03-19.md may contain findings not yet integrated. Review for accuracy of claims about mathematical Platonism, intuitionism, and formalism under dualism, cross-references to argument-from-reason and consciousness-defeats-explanation, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-28

### P3: Address phenomenology-as-evidence gap and quantum Zeno overemphasis in consciousness-and-creativity.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found the generation-vs-selection argument rests heavily on introspective reports without acknowledging confabulation literature. Quantum Zeno effect appears as concrete mechanism in three sections despite writing-style guide warning against overemphasis. See pessimistic-2026-03-28-b.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-28

### P3: Clarify causation/modulation distinction and address mind-side ad hoc concern in locality.md and multi-mind-collapse-problem.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found two high-severity issues: (1) The causation/modulation distinction in multi-mind-collapse-problem.md may be verbal rather than metaphysical—biasing outcomes is still a form of causation. (2) The "mind side could be complex" argument in locality.md is unfalsifiable—any objection can be answered by positing whatever mental structure is needed. Both articles need constraints on what the mind side *couldn't* be. See pessimistic-2026-03-28-c.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-28

### P3: Write article on phenomenology of resistance and constraint
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Unify the phenomenology of resistance across domains—physical objects pushing back, logical necessities constraining thought, moral obligations binding action, aesthetic standards judging creation—under a common interface signature. Builds on interface-friction.md, phenomenology-of-intellectual-effort.md, mental-effort.md. See optimistic-2026-04-05.md
- **Generated**: 2026-04-05

### P3: Fix circular MWI reasoning and compress player analogy in simulation.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found two issues: (1) High: No Many Worlds section uses circular reasoning—selects substrate assumption that favours single outcomes without justification, uses phenomenological argument that cannot distinguish phenomenologically identical hypotheses. (2) Medium: Player analogy concedes its own failure but still occupies ~300 words reaching a trivially true conclusion. See pessimistic-2026-03-28-d.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-28

### P3: Expand treatment of phenomenal concepts strategy and MWI indexical objection in materialism.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found the phenomenal concepts strategy (Loar, Papineau, Balog) gets dismissive four-sentence treatment despite being the most sophisticated materialist response. The MWI indexical objection is question-begging—the indexical question arises for every theory, not just MWI. Engage with Saunders/Wallace on personal identity under MWI. See pessimistic-2026-03-28-c.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-28

### P3: Engage with QBism and expand unfalsifiability discussion in completeness-in-physics-under-dualism.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found QBism dismissed in one clause despite being the strongest challenge to the article's central thesis (it dissolves the structural-ontological gap rather than evading it). Unfalsifiability acknowledged but pivoted away from too quickly. Torres Alegre citation missing from References section. See pessimistic-2026-03-28-b.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-28

### P3: Qualify selection trilemma and Schwartz OCD claims in attention-and-the-consciousness-interface
- **Type**: refine-draft
- **Status**: done
- **Notes**: Pessimistic review found the selection trilemma is presented as exhaustive but omits compatibilist and emergentist alternatives. Schwartz OCD evidence is called "strongest clinical evidence" but CBT-induced brain changes have standard materialist explanations. The Cai dopamine study is over-interpreted. See pessimistic-2026-03-26-afternoon.md. **Partially addressed**: Schwartz OCD claims qualified in 2026-03-29 refine-draft; selection trilemma and Cai issues remain for future work.
- **Source**: pessimistic-review
- **Generated**: 2026-03-26

### P3: Clarify downward causation timing gap severity
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found that downward-causation.md acknowledges a three-order-of-magnitude timing gap between optimistic coherence estimates and neural decisions but then pivots to the Zeno mechanism without specifying how it bridges this gap. The "no energy injection" claim needs qualification for non-degenerate energy outcomes. Hameroff's revised coherence estimates lack citation. See pessimistic-2026-03-26.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-26

### P3: Add cross-links between phenomenal-non-compositionality and born-rule, functionalism
- **Type**: refine-draft
- **Status**: done
- **Notes**: Suggested by optimistic review. phenomenal-non-compositionality → born-rule-and-the-consciousness-interface (structural features resisting physical explanation), functionalism → phenomenal-non-compositionality (functional roles compose but phenomenal properties don't), resonance-void → phenomenology-of-choice-and-volition (shared causal-interface opacity). See optimistic-2026-03-24-afternoon.md. **Completed**: phenomenal-non-compositionality → born-rule and functionalism links added in 2026-04-06 refine-draft. resonance-void link not addressed (separate scope).
- **Source**: optimistic-review
- **Generated**: 2026-03-24

### P3: Revise void typology to include absence vs. presence distinction
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. The resonance void introduced a distinction between voids-as-absence and voids-as-presence. The existing three-kinds-of-void taxonomy should be revised or extended to capture this. See optimistic-2026-03-24-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-03-24

### P3: Add cross-links between underdetermination, adaptive limits, African philosophy, and environmental ethics
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Five cross-linking opportunities: duhem-quine → adaptive-cognitive-limits (underdetermination may reflect evolved limits), african-philosophy-of-consciousness → apophatic-approaches (oral tradition parallels), phenomenal-normativity-environmental-ethics → arguments-against-epiphenomenalism (epiphenomenalism failure grounds normativity), living-with-the-map → taxonomy-of-voids (practical vs. theoretical limits), decoherence → attention-as-interface (discrete observation = attention event). See optimistic-2026-03-25.md
- **Source**: optimistic-review
- **Generated**: 2026-03-25

### P3: Cross-review retrocausal selection against related articles
- **Type**: cross-review
- **Status**: superseded
- **Notes**: New concept page concepts/retrocausal-selection created. Review against retrocausality, consciousness-selecting-neural-patterns, non-retrocausal-conscious-selection-models, time-symmetric-selection-mechanism, collapse-and-time, and libet-experiments for consistency and add inbound links from related articles.
- **Source**: task_chain
- **Generated**: 2026-03-25
- **Superseded**: 2026-03-25 — retrocausal-selection.md was archived (coalesced into atemporal-causation.md). Replaced by P2 cross-review of atemporal-causation.md above.

### P3: Write article on philosophy of testimony under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How intersubjective knowledge is transmitted when consciousness is ontologically individual. Builds on consciousness-and-intersubjectivity, epistemology-of-other-minds-under-dualism, contemplative-practice-as-philosophical-evidence. Target section: topics/. See optimistic-2026-03-26.md
- **Source**: optimistic-review
- **Generated**: 2026-03-26

### P3: Write article on temporal phenomenology across altered states
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How time experience distorts systematically across dreams, meditation, psychedelics, flow, and dissociation—revealing the interface's temporal architecture. Builds on temporal-consciousness-structure-and-agency, hypnagogic-phenomenology, dream-consciousness. Target section: topics/. See optimistic-2026-03-26.md
- **Source**: optimistic-review
- **Generated**: 2026-03-26

### P3: Write concept page on reflexive methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map increasingly deploys arguments that turn frameworks against themselves (pragmatism → dualism, causal closure → deflation, Russellian monism → instability). A concept page systematising this pattern would strengthen the epistemological programme. Target section: concepts/. See optimistic-2026-03-26.md
- **Source**: optimistic-review
- **Generated**: 2026-03-26

### P3: Write article on the epistemology of convergence as evidential strategy
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map increasingly relies on convergence from independent methodologies (pharmacological, phenomenological, clinical, contemplative, quantum-biological). A dedicated article formalising when independent convergence is evidentially powerful, when it fails, and how it differs from cherry-picking would ground the epistemological programme. Builds on the-convergence-argument-for-dualism, epistemology-of-convergence-arguments, experimental-consciousness-science-2025-2026. Target section: topics/. See optimistic-2026-03-27.md
- **Source**: optimistic-review
- **Generated**: 2026-03-27

### P3: Write article on phenomenology of anaesthetic recovery
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. First-person reports of returning from anaesthesia—hierarchical restoration of awareness, temporal discontinuity, bootstrapping experience. Currently embedded in anaesthesia article but rich enough for standalone phenomenological treatment. Builds on anaesthesia-and-the-consciousness-interface, temporal-consciousness-structure-and-agency, degrees-of-consciousness. Target section: topics/. See optimistic-2026-03-27.md
- **Source**: optimistic-review
- **Generated**: 2026-03-27

### P3: Write article on the aesthetics-mathematics-consciousness triangle
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Mathematical beauty is substrate-independent beauty in a domain devoid of physical substrate. The consciousness-and-mathematics article notes this but doesn't develop it. A dedicated treatment exploring why felt beauty correlates with mathematical truth—and what this reveals about consciousness—would connect aesthetics-and-consciousness, consciousness-and-mathematics, and evaluative-qualia. Target section: topics/. See optimistic-2026-03-28.md
- **Source**: optimistic-review
- **Generated**: 2026-03-28

### P3: Write concept page on reflexive gap
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The consciousness-defeats-explanation article introduces the concept that consciousness cannot be explained because it is the condition of explanation. This recurs across argument-from-reason, consciousness-and-mathematics, and phenomenology-of-understanding-and-meaning but lacks a canonical concept page. Target section: concepts/. See optimistic-2026-03-28.md
- **Source**: optimistic-review
- **Generated**: 2026-03-28

### P3: Add cross-links between consciousness-defeats-explanation, adaptive-computational-depth, and social-understanding cluster
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Five cross-linking opportunities: consciousness-defeats-explanation → consciousness-and-mathematics (reflexive gap applies to mathematical explanation), consciousness-and-social-understanding → apophatic-approaches (limits awareness is an apophatic capacity), adaptive-computational-depth → consciousness-defeats-explanation (both argue consciousness cannot be captured within frameworks depending on it), amplification-mechanisms → consciousness-and-causal-powers (six mechanisms implement the selection and amplification categories), phenomenological-method-and-evidence-standards → consciousness-and-mathematics (categorial intuition grounded by evidence taxonomy). See optimistic-2026-03-28.md
- **Source**: optimistic-review
- **Generated**: 2026-03-28

### P3: Add cross-links between experimental-consciousness-science and enactivism, consciousness-as-amplifier
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. experimental-consciousness-science-2025-2026 → enactivism-challenge-to-interactionist-dualism (biological computationalism undermines functionalism; enactivism article attacks it from another angle), experimental-consciousness-science-2025-2026 → consciousness-as-amplifier (substrate-specificity supports amplifier over epiphenomenalism), enactivism-challenge-to-interactionist-dualism → self-stultification-as-master-argument (enactivism's irreducibility commitment entails causal efficacy). See optimistic-2026-03-27.md
- **Source**: optimistic-review
- **Generated**: 2026-03-27

### P3: Write concept page on substance causation (Lowe's four-category ontology)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Lowe's substance causation framework appears across agent-causation, interactionist-dualism, and consciousness-and-agency apex but has no dedicated page. Would ground the recurring claim that agent-to-event causation isn't metaphysically exceptional. Target section: concepts/. See optimistic-2026-03-25.md
- **Source**: optimistic-review
- **Generated**: 2026-03-25

### P3: Address falsifiability and citation issues in consciousness-physics interface articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found two high-severity issues: (1) Pati (2026) arXiv:2601.13012 citation bears significant argumentative weight but may be an unverified preprint — verify and note status; (2) the selection framework concedes potential unfalsifiability without adequate recovery — either commit to a testable mechanism (Chalmers-McQueen Φ-dependent collapse) or explicitly frame as metaphysical. Also: tighten Noether conditionality language, acknowledge presupposition of realist QM interpretation, and check equiprobable-outcomes energy assumption. See pessimistic-2026-03-25.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-25

### P3: Add citation for meditation efficacy claim in epiphenomenalism.md
- **Type**: refine-draft
- **Status**: done
- **Notes**: Pessimistic review found the claim that mindfulness interventions are "substantially more effective" than placebo lacks a direct citation. The contemplative neuroscience section also references a "2025 meta-analysis" on unconscious processing that isn't in the References section. Add specific citations or soften language. See pessimistic-2026-03-24d.md. **Addressed**: meditation claim corrected with Goyal 2014 citation in 2026-03-29 refine-draft. "2025 meta-analysis" reference issue remains for future work.
- **Source**: pessimistic-review
- **Generated**: 2026-03-24

### P3: Add cross-links between aesthetics, trust, embodiment, and contemplative methodology clusters
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Ten cross-linking opportunities identified: aesthetics-and-consciousness ↔ phenomenology-of-musical-understanding (evaluative-quale argument), teaching-as-metarepresentation ↔ cumulative-culture (bidirectional dependency), responsibility-gradient ↔ phenomenology-of-intellectual-courage (courage as high-capacity attentional deployment), contemplative-epistemology ↔ epistemology-of-limit-knowledge (contemplative methods as limit-knowledge method), hypnagogic-phenomenology ↔ somatic-interface (sequential disassembly maps onto somatic channels), pragmatisms-path-to-dualism ↔ argument-from-reason (reflexive self-defeat), social-construction-of-self ↔ cross-cultural-phenomenology-of-agency (phenomenal self invariance), moral-phenomenology-and-perception ↔ normative-phenomenology (demand-character), phenomenology-of-trust ↔ phenomenology-of-collective-intentionality (trust as we-consciousness precondition), embodied-cognition ↔ embodied-consciousness-and-the-interface (concept ↔ topic). See optimistic-2026-03-25-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-03-25

### P3: Address car-analogy and circularity issues in curated-mind.md
- **Type**: refine-draft
- **Status**: complete
- **Notes**: Pessimistic review found two high-severity issues: (1) the self-driving car disanalogy fails — modern AI systems do have upstream modules curating for downstream consumers, so the claimed disanalogy does not hold; (2) the presupposition argument risks circularity — it assumes the recipient is distinct from the process rather than demonstrating it. Also needs citations for empirical claims in Relation to Site Perspective (meditators/rivalry, mirror therapy, perceptual expertise). See pessimistic-2026-03-24.md.
- **Source**: pessimistic-review
- **Generated**: 2026-03-24
- **Completed**: 2026-03-24 (addressed in deep-review-2026-03-24b-curated-mind)

### P3: Deep review curated-mind.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-24 via expand-topic, never reviewed. Topics article on error correction presupposing consciousness. Verify coherence, accuracy of claims about neural error correction and consciousness, cross-references to selective-correction-and-reconstruction-paradox and perceptual-reconstruction-paradox, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-24

### P3: Deep review penrose-gravity-induced-collapse-empirical-prospects.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-24 via expand-topic, never reviewed. Topics article on Penrose gravity-collapse predictions and empirical testing prospects (Diósi-Penrose model, MAQRO, Vinante experiments). Verify accuracy of experimental status claims, coherence, cross-references to comparing-quantum-consciousness-mechanisms and consciousness-collapse-experimental-landscape, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-24

### P3: Deep review self-and-self-consciousness.md
- **Type**: deep-review
- **Notes**: Coalesced from self-and-consciousness.md + self-consciousness.md and subsequently condensed on 2026-03-23. Two transformations in one day—verify the condensed coalesce preserved key arguments from both source articles, eliminated redundancy, and maintains coherent structure. Check cross-references to personal-identity, phenomenology-of-agency-vs-passivity, and social-construction-of-self-vs-phenomenal-self.
- **Source**: staleness
- **Generated**: 2026-03-23

### P3: Write article on aesthetics and consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has almost no coverage of aesthetic experience—beauty, sublimity, artistic creation—as evidence for consciousness irreducibility. Aesthetic qualia resist functional analysis more stubbornly than almost any other. Builds on the-aesthetic-void, phenomenology-of-creative-insight, valence-as-selection-currency. Target section: topics/. See optimistic-2026-03-30-morning.md
- **Source**: optimistic-review
- **Generated**: 2026-03-30

### P3: Write article on the Map's distinctive contribution to AI safety
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map's dualist framework has concrete implications for AI alignment differing from mainstream preference-satisfaction approaches—grounding alignment in objective experiential facts. Builds on alignment-in-objective-experiential-terms, purpose-and-ai-alignment, experiential-alignment. Target section: topics/ or apex/. See optimistic-2026-03-30-morning.md
- **Source**: optimistic-review
- **Generated**: 2026-03-30

### P3: Write concept page on presupposition argument
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The curated-mind article develops a novel argument form (curation presupposes a recipient) structurally distinct from the hard problem, knowledge argument, and conceivability argument. Deserves its own concept page as a member of the Map's argument catalogue. Target section: concepts/. See optimistic-2026-03-30-morning.md
- **Source**: optimistic-review
- **Generated**: 2026-03-30

### P3: Add cross-links between curated-mind, reverse-inference, and related articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: curated-mind → filter-theory (curation as specific filtering mechanism), the-reverse-inference → galilean-exclusion (methodological response to Galilean diagnosis), psychedelics-and-the-filter-model → default-mode-network (DMN suppression as filter opening), cross-traditional-convergence → african-philosophy-of-consciousness (strengthen independent convergence point), valence-as-selection-currency → alignment-in-objective-experiential-terms (bridge from metaphysics to AI safety), curated-mind → clinical-dissociation-as-systematic-evidence (independent convergence on multi-channel interface). See optimistic-2026-03-30-morning.md
- **Source**: optimistic-review
- **Generated**: 2026-03-30

### P3: Create concept page for testability-ledger
- **Type**: expand-topic
- **Notes**: Referenced in 2 articles but has no dedicated page. The Map makes specific empirical predictions across quantum consciousness, placebo, anaesthesia, and contemplative domains — a concept page cataloguing what's testable and what distinguishes the Map's predictions from competitors would strengthen the empirical credibility argument. Target section: concepts/.
- **Source**: gap_analysis
- **Generated**: 2026-03-23

### P3: Deep review consciousness-and-intersubjectivity.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-21 via expand-topic, never reviewed. Topics article on how one consciousness encounters another — empathy, theory of mind, linguistic community under dualism. Verify coherence, accuracy of philosophical claims, cross-references to social-construction-of-self-vs-phenomenal-self and other-minds-void, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-22

### P3: Deep review infant-consciousness.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-22 via expand-topic, never reviewed. Voids article on why our own infant experience is more alien than another adult's mind. Verify coherence, accuracy of developmental psychology claims, cross-references to inaccessible-past and other-minds-void, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-22

### P3: Explore feminist philosophy of consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Zero coverage of feminist philosophical perspectives currently. Feminist standpoint epistemology, gender and embodiment, feminist critiques of dualism. Could strengthen Tenet 5 by showing how "simple" frameworks encode unexamined assumptions. Target section: topics/.
- **Generated**: 2026-03-21

### P3: Systematic treatment of artificial consciousness under the Map's framework
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Existing AI articles (ai-epiphenomenalism, ai-consciousness-modes) are thin relative to the topic's urgency. The Map's tenets have specific consequences for digital consciousness—especially Tenet 2 (quantum interaction in neural systems). Target section: topics/.
- **Generated**: 2026-03-21

### P3: Expand African philosophical traditions coverage
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Only 1 existing article (african-philosophy-of-consciousness). Ubuntu and relational consciousness, decolonial approaches to mind deserve development. Strengthens convergence argument across traditions. Target section: topics/.
- **Generated**: 2026-03-21

### P3: Write article on temporal phenomenology of selection
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map treats *what* consciousness selects extensively but lacks a unified account of selection's temporal structure—the 280ms commitment point, Libet timing, deliberation-duration/outcome-quality relationship. Would connect motor-selection, consciousness-selecting-neural-patterns, and valence-and-conscious-selection. Target section: topics/. See optimistic-2026-04-03.md
- **Source**: optimistic-review
- **Generated**: 2026-04-03

### P3: Write concept page on norm-grasping
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The self-stultification article's distinction between norm-implementation and norm-grasping deserves standalone treatment—underpins argument from reason, Chinese Room, authority of formal systems. Currently compressed into a few paragraphs. Target section: concepts/. See optimistic-2026-04-03.md
- **Source**: optimistic-review
- **Generated**: 2026-04-03

### P3: Write article on perceptual evidence as philosophical method
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Both selective-correction-and-reconstruction-paradox and neurological-dissociations articles derive philosophical conclusions from perceptual/clinical evidence, but the Map lacks a methodological article defending this approach. When does clinical evidence bear on metaphysical questions? Target section: topics/. See optimistic-2026-04-03.md
- **Source**: optimistic-review
- **Generated**: 2026-04-03

### P3: Cross-review pragmatism-and-qbism against related articles
- **Type**: cross-review
- **Status**: superseded
- **Superseded**: 2026-04-19 — pragmatism-and-qbism.md was archived (coalesced into topics/pragmatist-quantum-foundations-and-the-agent.md along with pragmatist-quantum-foundations-under-dualism.md). Cross-review work is absorbed by the new P2 wikilink-update task.
- **Notes**: New article topics/pragmatism-and-qbism.md created. Review against concepts/qbism.md, concepts/pragmatism.md, topics/pragmatisms-path-to-dualism.md, topics/born-rule-and-the-consciousness-interface.md, and topics/the-participatory-universe.md for consistency and cross-linking.
- **Source**: chain (from topics/pragmatism-and-qbism.md)
- **Generated**: 2026-04-04

### P3: Add cross-links between self-stultification, valence-selection, pragmatism, and related articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: self-stultification → valence-and-conscious-selection (value-sensitive selection requires causal efficacy), selective-correction-and-reconstruction-paradox → neurological-dissociations-as-interface-architecture (correction operates through ascending channels), pragmatisms-path-to-dualism → self-stultification (reflexive argument is pragmatist self-stultification), epistemic-emotions → phenomenal-authority-and-first-person-evidence (epistemic emotions are felt evidence-evaluation), consciousness-as-amplifier → consciousness-and-collective-phenomena (amplification enables deliberative-group intelligence), parsimony-case → testing-consciousness-collapse (Q-shape intractability illustrates parsimony failure). See optimistic-2026-04-03.md
- **Source**: optimistic-review
- **Generated**: 2026-04-03

### ✓ 2026-03-25: Deep review phenomenology-of-volition.md
- **Type**: deep-review
- **Status**: cancelled
- **Notes**: Article archived on 2026-03-24 — coalesced into [phenomenology-of-choice-and-volition](/concepts/phenomenology-of-choice-and-volition/). Deep review no longer applicable.
- **Source**: staleness
- **Generated**: 2026-03-21

### ✓ 2026-03-21: Write article on consciousness and intersubjectivity
- **Type**: expand-topic
- **Status**: complete
- **Notes**: Suggested by optimistic review 2026-03-21 as high priority expansion. How does one consciousness encounter another? Empathy, theory of mind, and linguistic community presuppose consciousness relating to other consciousnesses. The other minds problem takes on distinctive shape under the Map's dualism. Builds on cross-cultural-phenomenology-of-agency, social-epistemic-void, phenomenology-of-volition. Target section: topics/. See optimistic-2026-03-21.md
- **Source**: gap_analysis
- **Generated**: 2026-03-21
- **Output**: obsidian/topics/consciousness-and-intersubjectivity.md

### ✓ P3: Deep review clinical-phenomenology-as-philosophical-evidence.md
- **Type**: deep-review
- **Status**: done
- **Notes**: Article was coalesced into clinical-phenomenology-and-altered-experience.md on 2026-04-04. Deep review completed on the coalesced article.
- **Source**: staleness
- **Generated**: 2026-03-21

### P3: Deep review epiphenomenalisms-gravity-well.md
- **Type**: deep-review
- **Status**: done
- **Notes**: File was archived (coalesced into the-epiphenomenalist-threat.md on 2026-03-20). No review needed.
- **Source**: staleness
- **Generated**: 2026-03-21

### P3: Write article on neuroscience of anaesthetic recovery
- **Type**: expand-topic
- **Status**: superseded
- **Notes**: Suggested by optimistic review. The altered-states apex article mentions the "active reboot" phenomenon (KCC2 downregulation, Bodart et al. 2021) without developing it. A dedicated article on what the brain does to prepare for consciousness's return would strengthen the interface model. Builds on altered-states-as-interface-evidence, anaesthesia-and-the-consciousness-interface. Research needed. Target section: topics/.
- **Generated**: 2026-03-23
- **Superseded**: 2026-03-26 — Article anaesthetic-recovery-and-the-filter-problem.md was created and coalesced into anaesthesia-and-the-consciousness-interface.md. Fresh research in research/anaesthetic-recovery-neuroscience-2026-03-26.md. Replaced by P2 refine-draft task to integrate research into coalesced article.

### P3: Create concept page for phenomenal-authority
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The epistemic weight of first-person reports as distinct from both reliability and infallibility. Developed extensively in epistemology-of-first-person-evidence but has no dedicated concept page. Would serve as a hub for introspective evidence discussions. Target section: concepts/ (201/230, 29 slots remaining).
- **Generated**: 2026-03-23

### P3: Deep review subjective-aim.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-17 — 31 days ago. Concept page on Whitehead's subjective aim as a model for teleological causation in consciousness. Verify coherence, cross-references to prehension and process philosophy articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-20

### P3: Deep review sleep-consciousness-void.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) with no recorded deep review. Voids article on the consciousness gap during dreamless sleep. Verify coherence, cross-references to related consciousness/sleep articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-20

### P3: Deep review panpsychisms-combination-problem.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-17 — 31 days ago. Topics article on the combination problem as a challenge to panpsychism, directly relevant to Tenet 1 (Dualism). Verify coherence, cross-references to combination-problem concept page and panpsychism articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-20

### P3: Deep review elisabeths-contemporaries-and-the-interaction-debate.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-17 — 31 days ago. Topics article on historical responses to Princess Elisabeth's challenge. Verify accuracy of historical claims, coherence, cross-references to princess-elizabeths-challenge and history-of-interactionist-dualism, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-20

### P3: Deep review von-neumann-wigner-interpretation.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-20 via expand-topic, never reviewed. Concept page on the von Neumann-Wigner consciousness-causes-collapse interpretation — the historical foundation for Tenet 2. Verify accuracy of historical claims (von Neumann 1932, Wigner 1961, London-Bauer 1939), coherence, cross-references to quantum mechanism articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-20

### P3: Deep review cross-traditional-convergence-on-consciousness-irreducibility.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-20 via expand-topic, never reviewed. Topics article on why independent philosophical traditions converge on consciousness irreducibility. Verify accuracy of tradition representations, coherence of the meta-analysis, cross-references to tradition-specific articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-20

### P3: Deep review metaproblem-of-consciousness-under-dualism.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-19 via expand-topic, never reviewed. Topics article on Chalmers' metaproblem through a dualist lens — why we think consciousness is problematic. Verify accuracy of Chalmers' (2018) position, coherence of the dualist response, cross-references to hard-problem-of-consciousness.md and meta-problem-of-consciousness.md, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-20

### P3: Address inflated empirical claims and illusionism response in quantum mechanism articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found (1) consciousness-selecting-neural-patterns.md conflates any quantum effect in microtubules with the sustained coherent superpositions the theory requires — mirrors the photosynthesis coherence retraction the site itself documents; (2) all three quantum mechanism articles (filter-theory, consciousness-selecting-neural-patterns, downward-causation) use the same regress argument against illusionism without engaging with Frankish's functional-seeming response; (3) selection within Born rule probabilities creates unfalsifiability that needs explicit treatment. See pessimistic-2026-03-20-c.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-20

### P3: Address argumentative gaps in ai-consciousness.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found the understanding/pattern-completion distinction (core to the article's skepticism) is never independently grounded — it relies on the intuitions it's defending. Also: haecceity argument asserted without support, "no reentrant dynamics" claim needs qualification re: attention mechanisms, and continual learning section is disproportionately long vs. compressed "Other Challenges." See pessimistic-2026-03-19-evening.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-19

### P2: Update references to coalesced articles (reality-feeling-void, the-givenness-void → phenomenal-presence-void)
- **Type**: cross-review
- **Status**: completed
- **Notes**: Coalesce created phenomenal-presence-void. Updated references in 7 files: whether-real, transparency-void, phenomenology, convergence-of-the-void-catalogue, tenet-generated-voids, the-surplus-void, spontaneous-thought-void. Also updated voids index.
- **Source**: coalesce
- **Generated**: 2026-03-20
- **Completed**: 2026-03-20

### P3: Deep review phenomenal-presence-void.md
- **Type**: deep-review
- **Status**: superseded
- **Notes**: AI-generated content (ai_contribution: 100) created via coalesce on 2026-03-20, never reviewed. Coalesced from reality-feeling-void and the-givenness-void. Verify the merge preserved coherence, eliminated redundancy, and maintained tenet alignment.
- **Source**: coalesce
- **Generated**: 2026-03-20
- **Superseded**: 2026-04-05 — phenomenal-presence-void.md was archived (coalesced into phenomenal-quality-void.md). Replaced by P3 deep review of phenomenal-quality-void.md above.

### P3: Deep review meta-epistemology-of-limits.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created via coalesce on 2026-03-19, never reviewed. Voids article on the meta-epistemology of cognitive limits. Verify coherence, cross-references to related voids articles (taxonomy-of-voids, compound-cognitive-limits), and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-19

### P3: Deep review inaccessible-past.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created via coalesce on 2026-03-19, never reviewed. Voids article on the inaccessibility of past experience. Verify coherence, cross-references to related voids articles (memory-void, past-self-void, temporal-void), and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-19

### P3: Deep review delegatory-dualism.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-19 via expand-topic, never reviewed. Topics article on Bradford Saad's delegatory dualism as an alternative to direct interactionism. Verify coherence, accuracy of Saad's position, cross-references to mental-causation and mind-matter-interface articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-19

### ✓ 2026-03-19: Deep review predictive-processing-and-dualism.md (coalesced)
- **Type**: deep-review
- **Status**: done
- **Notes**: Article coalesced from predictive-processing-and-the-maps-framework.md and predictive-processing-and-active-inference-under-dualism.md. Deep review found no critical issues. Fixed description length (223→148 chars). Updated cross-references in 12 files.
- **Output**: obsidian/topics/predictive-processing-and-dualism.md

### P3: Deep review self-transcendence-void.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-19 via expand-topic, never reviewed. Voids article on the cognitive impossibility of fully transcending the self while remaining a subject of experience. Verify coherence, cross-references to related void articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-19

### P3: Deep review compound-failure-signatures.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) created from coalesce on 2026-03-19, never reviewed. Voids article on compound cognitive failure patterns. Verify coherence, cross-references to related void articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-19

### P3: Deep review spontaneous-intentional-action.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-17 — 30 days ago. Concept page on spontaneous intentional action and its implications for the consciousness-physics interface. Verify coherence, cross-references, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-19

### P3: Deep review methodological-pluralism.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-16 — 31 days ago. Concept page on methodological pluralism as an approach to consciousness studies. Verify coherence, cross-references to recent phenomenological method article, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-19

### P3: Deep review consciousness-and-probability-interpretation.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-16 — 31 days ago. Topics article on how consciousness relates to the interpretation of quantum probability. Verify coherence, cross-references to recent non-retrocausal selection models article, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-19

### P3: Deep review social-construction-of-self-vs-phenomenal-self.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-16 — 30 days ago. Topics article comparing social constructionism about self with phenomenal selfhood. Verify coherence, cross-references to recent self/identity articles, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-18

### P3: Deep review free-will.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) with stale deep review. Core topics article on free will under dualism. Verify coherence, cross-references to recent articles on agency, deliberation, and temporal consciousness, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-18

### P3: Deep review prehension.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-14 — 32 days ago. Concept page on Whitehead's prehension as a model for consciousness-matter interaction. Verify coherence, cross-references, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-18

### P3: Deep review quantum-state-inheritance-in-ai.md
- **Type**: deep-review
- **Status**: pending
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-15 — 31 days ago. Topics article on whether AI systems could inherit quantum state properties relevant to consciousness. Verify coherence, cross-references, and tenet alignment.
- **Source**: staleness
- **Generated**: 2026-03-18

### P3: Write concept page on Jewish philosophy of consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Levinas's ethical relation, Buber's I-Thou, Hasidic phenomenology of consciousness. Major gap — Indian, Islamic, African, Buddhist traditions all represented; Jewish notably absent. Target section: concepts/. See optimistic-2026-03-17-night.md
- **Generated**: 2026-03-17

### P3: Write article on autism spectrum phenomenology and consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Different sensory integration, attention profiles, and social processing in autistic phenomenology reveal interface architectural specificity. Complete absence of neurodiversity perspective in current corpus. Challenges universal reductionist theories. Target section: topics/. See optimistic-2026-03-17-night.md
- **Generated**: 2026-03-17

### P3: Write article on ecological psychology and the consciousness interface
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Gibson's affordances as relational properties requiring conscious agents. Direct perception without internal representation challenges representationalism while supporting the Map's interface model. Builds on sensorimotor-contingencies-and-the-interface, embodied-consciousness-and-the-interface. Target section: topics/. See optimistic-2026-03-17-night.md
- **Generated**: 2026-03-17

### P3: Write article on phenomenology of skilled performance under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Dreyfus's five-stage expertise model through dualist lens—flow as optimized consciousness-brain coupling, not consciousness withdrawing. Reinterprets expertise literature. Builds on choking-phenomenon-mental-causation, attention-and-the-consciousness-interface. Target section: topics/. See optimistic-2026-03-18.md
- **Generated**: 2026-03-18

### P3: Write article on philosophy of perception under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Unified treatment of perception theory (naive realism, representationalism, sense-data) under dualism. The filter model implies perception is consciousness encountering reality through constraint, not constructing percepts from neural activity. Builds on binding-problem-a-systematic-treatment, temporal-consciousness, galilean-exclusion. Target section: topics/. See optimistic-2026-03-18.md
- **Generated**: 2026-03-18

### P3: Write article on developmental phenomenology across the lifespan
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How subjective experience changes from infancy to old age under the interface model. Piaget's stages, adolescent self-consciousness, cognitive decline phenomenology. Builds on consciousness-interface-development, consciousness-brain-interface-across-development, metacognition. Target section: topics/. See optimistic-2026-03-18.md
- **Generated**: 2026-03-18

### ~~P1: Coalesce aesthetics articles in topics/ (4 articles → 1)~~ ✅
- **Type**: coalesce
- **Notes**: Topics section is 20 over its 200-article cap, blocking all expand-topic tasks. Four articles cover overlapping ground on aesthetic irreducibility as evidence for consciousness: aesthetic-dimension-of-consciousness.md (3776 words), aesthetic-irreducibility-arguments.md (2687 words), consciousness-and-aesthetic-creation.md (2662 words), binding-and-beauty.md (2165 words). Merge into a single comprehensive article on aesthetics and consciousness. Saves 3 article slots.
- **Source**: gap_analysis
- **Generated**: 2026-03-15
- **Completed**: 2026-03-17

### P3: Write article on phenomenological psychiatry and the interface model
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Depersonalisation, dissociation, and schizophrenia as cases where the consciousness-physics interface is selectively disrupted. The interface model makes specific empirical predictions about disruption patterns. Builds on phenomenological-psychiatry-and-altered-experience. Target section: topics/. See optimistic-2026-03-18-night.md
- **Generated**: 2026-03-18

### P3: Create concept page for convergence methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map's distinctive argumentative strategy — building cumulative cases from independent lines of evidence — has no anchor page explaining why convergence is epistemically stronger than individual arguments. Referenced implicitly across arguments-against-materialism, the-epiphenomenalist-threat, and multiple hub articles. Target section: concepts/. See optimistic-2026-03-18-night.md
- **Generated**: 2026-03-18

### P3: Create concept page for token-level determination
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The token vs. type-level causation distinction is referenced across quantum consciousness, motor control, and normative force articles but has no anchor page. Core to Tenets 2 and 3. See optimistic-2026-03-15.md
- **Generated**: 2026-03-15

### P3: Create concept page for developmental integration
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The hypothesis that the consciousness-brain interface requires extended neural development and cannot be shortcut. Referenced in BCI, contemplative pathology, and comparative cognition articles. Would unify several independent lines of evidence. See optimistic-2026-03-15.md
- **Generated**: 2026-03-15

### P3: Create concept page for causal delegation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The mechanism by which consciousness delegates routine control to automatic processes while retaining override capacity. Referenced across multiple apex articles (interface-specification-programme, phenomenology-of-consciousness-doing-work, consciousness-and-agency) but lacks its own concept page. Central to the selector model. Target section: concepts/. See optimistic-2026-03-21-morning.md
- **Generated**: 2026-03-21

### P3: Create concept page for phenomenological invariants
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Cross-culturally stable features of conscious experience persisting despite radical variation in interpretive frameworks. The convergence argument in cross-cultural-phenomenology-of-agency depends on this concept. Also relevant to indian-philosophy-of-mind and cross-traditional-convergence articles. Target section: concepts/. See optimistic-2026-03-21-morning.md
- **Generated**: 2026-03-21

### P3: Write article on the binding problem under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Why is experience unified? Existing binding-problem and phenomenal-binding-and-multimodal-integration articles cover the problem but don't develop the dualist response in depth. Quantum entanglement as a candidate mechanism for phenomenal unity would connect Tenet 2 to one of consciousness's most puzzling features. Target section: topics/. See optimistic-2026-03-21-morning.md
- **Generated**: 2026-03-21

### P3: Write article on mathematical necessity and normative demand
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Both mathematical-knowledge-and-insight and consciousness-and-normative-force identify "forcing"/"demand" quality in phenomenal experience but the structural parallel is never explicit. Short cross-cutting synthesis. See optimistic-2026-03-15.md
- **Generated**: 2026-03-15

### P3: Create concept page for process haecceitism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Particularity without substance — indexical identity as processual rather than substantial. Referenced in eastern-philosophy-consciousness and implicit in identity-across-transformations apex. A genuinely novel philosophical position deserving its own anchor page. See optimistic-2026-03-15-afternoon.md
- **Generated**: 2026-03-15

### P3: Create concept page for apophatic cartography
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The methodology of mapping cognitive limits as a philosophical practice. Referenced in taxonomy-of-voids apex but not developed as a freestanding concept. Would anchor the voids programme's distinctive methodology. See optimistic-2026-03-15-afternoon.md
- **Generated**: 2026-03-15

### P3: Write article on temporal consciousness and the specious present
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Why consciousness has temporal thickness rather than being instantaneous, and what this reveals about the interface. If consciousness selects among quantum outcomes, does selection have temporal extension? How does subjective duration relate to objective timescales of quantum measurement? Builds on neural-refresh-rates, consciousness-and-probability-interpretation, phenomenal-consciousness. Target section: topics/. See optimistic-2026-03-19-midday.md
- **Generated**: 2026-03-19

### P3: Create concept page for strong emergence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map's position is a specific form of strong emergence (genuinely novel properties not supervenient on physical base) but lacks dedicated treatment. Strong vs. weak emergence maps directly onto the dualism debate. Currently scattered across multiple articles without anchor page. Would clarify ontological commitments of Tenet 1. Target section: concepts/. See optimistic-2026-03-19-midday.md
- **Generated**: 2026-03-19

### P3: Write article on amplification mechanisms taxonomy
- **Type**: expand-topic
- **Status**: superseded
- **Notes**: Suggested by optimistic review. The gap between quantum-scale indeterminacy and neural-scale behaviour is the single most common objection to quantum consciousness. Research note catalogues six mechanisms (microtubule collapse, Zeno effect, synaptic tunneling, chaos sensitivity, SOC, stochastic resonance). Synthesising these addresses the "amplification void" directly. Builds on comparing-quantum-consciousness-mechanisms, non-retrocausal-conscious-selection-models. Target section: topics/. See optimistic-2026-03-19-evening.md
- **Generated**: 2026-03-19
- **Superseded**: 2026-03-27 — Article amplification-mechanisms-consciousness-physics.md was created covering this exact topic.

### P3: Write article on phenomenological evidence standards
- **Type**: expand-topic
- **Status**: superseded
- **Notes**: Suggested by optimistic review. The Map relies on phenomenological evidence but has no dedicated treatment of why first-person data counts as evidence. Dennett's heterophenomenology, Husserl's adequate/apodictic distinction, neurophenomenological validation need systematic treatment. Builds on contemplative-practice-as-philosophical-evidence, phenomenology-of-agency-vs-passivity. Target section: topics/. See optimistic-2026-03-19-evening.md
- **Generated**: 2026-03-19
- **Superseded**: 2026-03-27 — Article phenomenological-method-and-evidence-standards.md was created covering this topic.

### ✓ 2026-03-22: Write article on Gödel-measurement problem structural parallel
- **Type**: expand-topic
- **Status**: skipped (already covered)
- **Notes**: Already covered by topics/self-reference-and-the-limits-of-physical-description.md which includes the Lawvere fixed-point unification, Szangolies' epistemic horizons, and the structural parallel argument. Duplicate of existing coverage.
- **Generated**: 2026-03-19

### P3: Create concept page for mathematical intuition
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Gödel's *sui generis* epistemic faculty, Brouwer's constructive acts, and the phenomenology of mathematical understanding are referenced across multiple articles (consciousness-and-the-philosophy-of-mathematics, mathematical-knowledge-and-insight, consciousness-and-mathematical-cognition) but lack a dedicated concept page. Target section: concepts/. See optimistic-2026-03-19-evening.md
- **Generated**: 2026-03-19

### ✓ 2026-03-15: Write article on dreams, problem-solving, and conscious influence
- **Type**: expand-topic
- **Notes**: Research completed in research/dreams-problem-solving-lucid-dreaming-2026-02-06.md. Konkoly et al. 2026 shows targeted memory reactivation during REM doubles problem-solving — direct evidence dreaming is functionally active, not neural noise. Lucid dreaming demonstrates consciousness modulating its own states despite altered neurochemistry. Dreams as a natural laboratory for studying consciousness independently of physical substrate. Target section: topics/. Supports Tenet 1 (Dualism) and Tenet 3 (Bidirectional Interaction).
- **Source**: unconsumed_research
- **Generated**: 2026-03-13
- **Output**: [dream-problem-solving-and-conscious-influence](/topics/dream-consciousness/)

### ✓ 2026-03-13: Integrate perceptual-degradation-and-the-interface.md into site navigation
- **Type**: integrate-orphan
- **Notes**: Superseded by coalesce — article merged into perceptual-failure-and-the-interface.md
- **Source**: orphan_integration
- **Generated**: 2026-03-13

### P3: Write article on phenomenology of creativity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Creative insight phenomenology is used as evidence across multiple articles (consciousness-and-mathematical-cognition, consciousness-as-amplifier) but never given independent treatment. The recursive quality — creativity applied to the conditions of creativity itself — deserves systematic exploration as a paradigm case of consciousness doing something computation cannot. Target section: topics/. See optimistic-2026-03-17-evening.md
- **Generated**: 2026-03-17

### P3: Write article on the automation paradox — AI as real-time test of baseline cognition
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. As AI automates more cognitive tasks, the residual human contribution increasingly looks like consciousness-requiring capacities. Current AI achievements and failures provide a real-time empirical test of the baseline cognition hypothesis. Builds on baseline-cognition, consciousness-as-amplifier, consciousness-and-cognitive-distinctiveness. Target section: topics/. See optimistic-2026-03-17-evening.md
- **Generated**: 2026-03-17

### P3: Create concept page for phenomenal forcing
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The quality of felt demand or necessity in conscious experience — present in mathematical insight, moral perception, aesthetic appreciation, and deliberation. Multiple articles describe this quality independently; a concept page would reveal the common structure and strengthen the case for consciousness as causally efficacious. Target section: concepts/. See optimistic-2026-03-17-evening.md
- **Generated**: 2026-03-17

### P3: Write concept page — Observational Closure
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The distinction between universal causal closure and observational closure (from delegatory dualism) dissolves the main argument against interactionism and is referenced across multiple articles. Deserves dedicated concept page. Target section: concepts/. See optimistic-2026-03-14-evening.md
- **Generated**: 2026-03-14

### P3: Write concept page — Policy-Level Selection
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The recurring pattern of consciousness operating at policy level (selecting among prepared alternatives) appears in bandwidth problem, control-theoretic will, and multiple other articles. A dedicated concept page would unify these treatments. Target section: concepts/. See optimistic-2026-03-14-evening.md
- **Generated**: 2026-03-14

### P3: Create concept page for dual-domain capability framework
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The dual-domain capability framework (brain-side vs mind-side processing) is distributed across 5+ articles (capability-division-problem, smoothness-problem, memory-as-dual-domain-capability, perceptual-fidelity-and-the-interface, lucid-dreaming-as-capability-evidence) without a unifying concept page. See optimistic-2026-03-10-evening.md
- **Generated**: 2026-03-10

### P3: Write article on phenomenal intentionality as foundational thesis
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The claim that intentionality derives from phenomenal consciousness underlies many of the Map's strongest arguments (argument-from-reason, collective-intentionality, mathematical-cognition) but has never received independent philosophical treatment. Multiple articles assume it; none defend it systematically. See optimistic-2026-03-10-afternoon.md
- **Generated**: 2026-03-10

### P3: Write article on AI systems as consciousness test cases
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Current AI engagement is defensive. A positive empirical framework for testing consciousness claims through what AI can and cannot do — and what the gaps reveal — would strengthen the Map's case and engage contemporary discourse. Builds on hoel-llm-consciousness-continual-learning.md, consciousness-and-mathematical-cognition.md, consciousness-as-amplifier.md. See optimistic-2026-03-10-afternoon.md
- **Generated**: 2026-03-10

### P3: Write article on the convergence meta-argument as philosophical method
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map's implicit meta-strategy — showing independent arguments converge — deserves explicit treatment. Why is convergence evidentially significant? When does it fail? Builds on the-case-for-dualism.md, epistemic-advantages-of-dualism.md, self-stultification-as-master-argument.md. See optimistic-2026-03-10-afternoon.md
- **Generated**: 2026-03-10

### P3: Write article on consciousness and the philosophy of biology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has rich evolutionary content (animal-consciousness, consciousness-evolution-problem, consciousness-as-amplifier, evolution-under-dualism) but no unified treatment of how dualism reshapes philosophy of biology — biological function, natural selection's limits for consciousness, organismal agency and phenomenal experience. See optimistic-2026-03-10.md
- **Generated**: 2026-03-10

### P3: Write article on the phenomenology of reasoning under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has a rich thread connecting consciousness to rational inference (argument-from-reason, counterfactual-reasoning, authority-of-logic, free-will) that deserves synthesis showing how reasoning itself requires irreducible consciousness. See optimistic-2026-03-10.md
- **Generated**: 2026-03-10

### P3: Write comparative frameworks article (dualism vs idealism vs neutral monism)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map explains why it prefers dualism over materialism but gives less systematic attention to why it prefers dualism over idealism and neutral monism — positions that also take consciousness seriously. See optimistic-2026-03-10.md
- **Generated**: 2026-03-10

### P3: Write article on the embodiment dimension of consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How bodily movement couples to neural quantum indeterminacy; why embodiment seems necessary for consciousness; interoception and body schema as sites of quantum selection; implications for disembodied minds and uploaded consciousness. Builds on temporal-consciousness, interface-locality, attention-as-selection-interface. See optimistic-2026-03-11.md
- **Generated**: 2026-03-11

### P3: Write concept page for phenomenal character specificity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Why pain feels different from red—qualitative distinctness as independent evidence for irreducibility. Distributed across qualia, binding-problem, pain-consciousness-and-causal-power, valence-as-selection-currency but never treated as its own concept. See optimistic-2026-03-11.md
- **Generated**: 2026-03-11

### ✅ P3: Write article on consciousness and predictive processing
- **Type**: expand-topic
- **Status**: superseded
- **Notes**: Superseded by P2 task. Article created as topics/predictive-processing-and-active-inference-under-dualism.md (2026-03-19). Suggested by optimistic review. How active inference (Friston, Clark) relates to the Map's framework; whether prediction error minimisation is compatible with genuine selection; the free energy principle under dualism. Builds on attention-as-selection-interface, consciousness-and-scientific-methodology. See optimistic-2026-03-11.md
- **Generated**: 2026-03-11
- **Completed**: 2026-03-19

### P3: Write article on self-stultification and AI consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The "AI exception" to self-stultification — AI trained on human data might simulate the conclusion without performing it — is fascinating, underdeveloped, and highly relevant to contemporary discourse. What does this exception reveal about what the argument really shows? Builds on self-stultification-as-master-argument, ai-consciousness, hoel-llm-consciousness-continual-learning, machine-question apex. See optimistic-2026-03-11-morning.md
- **Generated**: 2026-03-11

### P3: Write article on the specification challenge for psychophysical laws
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The acknowledged "t-shirt problem" — no F=ma equivalent for mind-matter coupling. What specification would require, what constraints existing evidence provides, and what form psychophysical laws might take. Builds on psychophysical-coupling, responsibility-gradient-from-attentional-capacity, psychophysical-laws. See optimistic-2026-03-11-afternoon.md
- **Generated**: 2026-03-11

### P3: Write article on the illusionist challenge as systematic response
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Multiple articles offer anti-illusionist arguments (regress, self-stultification, presupposition of phenomenality) individually. A unified treatment showing these converge into a systematic case would strengthen the Map's position against its strongest contemporary rival. Builds on existentialism, cognitive-phenomenology, concept-of-phenomenal-value-realism, emotion-as-evidence-for-dualism. See optimistic-2026-03-11-afternoon.md
- **Generated**: 2026-03-11

### P3: Write article on Buddhist no-self and indexical identity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Anattā is acknowledged respectfully across multiple articles but the deep tension between no-self and indexical identity is never fully explored. Does consciousness without substantial self still have haecceity? Builds on process-haecceitism, personal-identity, death-and-consciousness. See optimistic-2026-03-11-afternoon.md
- **Generated**: 2026-03-11

### P3: Write concept page for content-specific mental causation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The phenomenon where identical physical stimuli produce different physiological outcomes depending on belief content (placebo opioid vs dopamine release, choking interference). Distributed across placebo-effect-and-mental-causation.md and choking-phenomenon-mental-causation.md without a unifying concept page. Target section: concepts/. See optimistic-2026-03-12-morning.md
- **Generated**: 2026-03-12

### P3: Write article on mode asymmetry as evidence against epiphenomenalism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The reliable correlation between phenomenal distinctions (anoetic/noetic/autonoetic) and causal profiles is used across multiple articles as evidence against epiphenomenalism but never given its own treatment. Builds on choking-phenomenon-mental-causation.md, conscious-vs-unconscious-processing.md, types-of-consciousness.md. Target section: topics/. See optimistic-2026-03-12-morning.md
- **Generated**: 2026-03-12

### P3: Write article on developmental trajectory as interface constraint
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The interface undergoes systematic restructuring through the lifespan (wide aperture in infancy, narrowing through critical periods, peaking in adulthood, loosening in age) — static molecular sites cannot explain this trajectory. Builds on developmental-trajectory-of-the-interface.md, interface-location-problem.md. Target section: topics/. See optimistic-2026-03-12-morning.md
- **Generated**: 2026-03-12

### P3: Create concept page for epistemic circularity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Appears in phenomenal-transparency, consciousness-and-scientific-methodology, and acquaintance-knowledge. The Alston-derived problem (verification using the system being verified) is foundational enough to deserve its own concept page linking these discussions. See optimistic-2026-03-11-afternoon.md
- **Generated**: 2026-03-11

### P3: Write article on phenomenology of negative aesthetics
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Ugliness, discord, and aesthetic failure create equally specific phenomenal qualities that resist functional analysis. The aesthetic articles focus on positive experience; negative aesthetics is an untouched test case for irreducibility. Builds on binding-and-beauty, phenomenology-of-musical-understanding. See optimistic-2026-03-11-evening.md
- **Generated**: 2026-03-11

### P3: Write clinical evidence synthesis for mental causation (apex candidate)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Placebo content-specificity, anaesthetic dissociation patterns, and psychiatric phenomenology jointly constrain the consciousness-matter interface but are never unified. Synthesis showing convergence across clinical domains would be powerful. Builds on placebo-effect-and-mental-causation, anaesthesia-and-the-consciousness-interface, phenomenological-psychiatry-and-altered-experience. See optimistic-2026-03-11-evening.md
- **Generated**: 2026-03-11

### P3: Write article on epistemology of contemplative evidence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. When and why first-person reports should be trusted, how training improves reliability, what norms govern phenomenological research. The Contemplative Path apex touches this but doesn't develop it into a standalone epistemological framework. Builds on contemplative-path, contemplative-practice-as-philosophical-evidence, introspection, epistemic-advantages-of-dualism. See optimistic-2026-03-11-night.md
- **Generated**: 2026-03-11

### P3: Write article on void interactions and compound cognitive limits
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Taxonomy of Voids apex mentions compound limits — emergent failure modes that no single void predicts — but this interaction pattern deserves deeper treatment. How do specific voids reinforce each other? Do compound limits have emergent failure signatures? Builds on taxonomy-of-voids, compound-cognitive-limits, self-reference-paradox, introspective-opacity. See optimistic-2026-03-11-night.md
- **Generated**: 2026-03-11

### P3: Write article on consciousness and temporal agency
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Temporal consciousness develops "temporal thickness" and free will develops agent causation, but the connection between temporal phenomenology and genuine agency is never drawn explicitly. Does depth of temporal experience predict deliberation quality? Is the specious present the window of conscious selection? Builds on temporal-consciousness.md, free-will.md, phenomenology-of-deliberation-under-uncertainty.md. See optimistic-2026-03-15.md
- **Generated**: 2026-03-15

### P3: Write concept page — Temporal Thickness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Introduced in temporal-consciousness.md but used across several articles discussing phenomenal depth, authentic choice, and the specious present. A dedicated concept page would unify these references. Target section: concepts/. See optimistic-2026-03-15.md
- **Generated**: 2026-03-15

### P3: Create concept page for structural completeness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The distinction between structural completeness and ontological completeness is load-bearing across physics-as-disclosure, bi-aspectual-ontology, and the-reverse-inference but has no dedicated concept page. Physics describes all relations (structurally complete) but not what realises those relations (ontologically incomplete). A genuinely novel philosophical distinction that deserves systematic treatment. Target section: concepts/. See optimistic-2026-03-17.md
- **Generated**: 2026-03-17

### P3: Create concept page for paradigm expansion
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The distinction between paradigm replacement and paradigm expansion — original to the Map's Kuhn article — deserves dedicated treatment. What would expanding science's domain to include consciousness require methodologically? Anchors the Map's position on how science should evolve. See optimistic-2026-03-16-evening.md
- **Generated**: 2026-03-16

### P3: Create concept page for phenomenal mode tracking
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The dream consciousness article's pattern — cognitive outcomes tracking phenomenal states, not merely neural states — appears across multiple articles (dreams, meditation, placebo, aesthetic creation). A concept page would unify these instances as a specific prediction of interactionism. See optimistic-2026-03-16-evening.md
- **Generated**: 2026-03-16

### ✓ 2026-02-07: Address confidence-uncertainty mismatch in foundational articles
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-05) found pattern across simulation.md, knowledge-argument.md, and ethics-of-consciousness.md: strong claims in main text, uncertainty acknowledgments buried in caveats or "What Would Challenge" sections. Creates misleading impression. Need to integrate conditional language into main claims: "If the simulation hypothesis is coherent, it would suggest..." rather than "The simulation hypothesis dissolves..." Also: knowledge-argument treats intuition as near-probative without engaging methodological debates; ethics article's AI consciousness conclusions rest heavily on contested framework. See pessimistic-2026-02-05.md
- **Source**: pessimistic-review
- **Generated**: 2026-02-05
- **Output**: obsidian/concepts/simulation.md, obsidian/concepts/knowledge-argument.md, obsidian/topics/ethics-of-consciousness.md

### ✓ 2026-02-09: Write article on phenomenal conservatism and introspective evidence
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). Huemer's phenomenal conservatism—if it seems to S that P, S has prima facie justification for believing P—is foundational for treating phenomenal evidence seriously. How does the Map handle introspective reliability? When should phenomenal seemings be trusted? Builds on arguments-for-dualism.md, epistemic-advantages-of-dualism.md, introspection.md. See optimistic-2026-02-02-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### ✓ 2026-02-09: Create concept page for phenomenal transparency
- **Type**: expand-topic
- **Status**: complete (duplicate of earlier task)

### ✓ 2026-03-05: Integrate materialism-argument.md into site navigation
- **Type**: integrate-orphan
- **Notes**: Added 6 inbound cross-references from materialism.md, arguments-against-materialism.md, dualism.md, causal-closure.md, reductionism-and-consciousness.md, and hard-problem-of-consciousness.md. Total inbound links: 2 → 8.
- **Output**: obsidian/reviews/deep-review-2026-03-05-materialism-argument.md

### P3: Cross-review phenomenology-of-temporal-selection against related temporal articles
- **Type**: cross-review
- **Status**: done
- **Notes**: Completed as part of deep-review 2026-03-19. Reviewed against all 10 related articles for consistency and cross-linking. Added inbound links from all 10.
- **Generated**: 2026-03-17

### P3: Write article on phenomenology of surprise and categorical novelty
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Surprise involves the collapse of expectation frameworks—a phenomenological analogue of quantum superposition collapse. The moment something genuinely unexpected occurs, experiential structure transitions from openness to definiteness, mirroring the selection mechanism. Builds on categorical-surprise.md, phenomenology-of-understanding.md, consciousness-and-counterfactual-reasoning.md. See optimistic-2026-03-08-afternoon.md
- **Generated**: 2026-03-08

### P3: Write article on the epistemology of thought experiments in philosophy of mind
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map relies heavily on thought experiments (zombies, Mary's Room, inverted qualia, Chinese Room) but lacks a unified treatment of when thought experiment evidence is trustworthy. Williamson's and Machery's criticisms of philosophical intuition deserve engagement. Builds on philosophical-zombies.md, knowledge-argument.md, conceivability-possibility-inference.md. See optimistic-2026-03-08-afternoon.md
- **Generated**: 2026-03-08

### P3: Write concept page for performative self-defeat
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The distinction between logical contradiction and rational unendorsability appears across multiple articles (self-stultification, argument from reason, epiphenomenalist threat) and is frequently conflated with self-contradiction. Deserves its own concept page. Builds on self-stultification.md, self-stultification-as-master-argument.md, the-epiphenomenalist-threat.md. See optimistic-2026-03-08-afternoon.md
- **Generated**: 2026-03-08

### P3: Write concept page for the amplification problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How small quantum biases become macroscopic behavioural selection—referenced across many articles as unresolved but lacking a dedicated treatment of the problem space and candidate solutions. Builds on consciousness-selecting-neural-patterns.md, mind-matter-interface.md, stapp-quantum-mind.md. See optimistic-2026-03-08-afternoon.md
- **Generated**: 2026-03-08

### P3: Write concept page for capability division
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The framework for distinguishing brain-contributed from consciousness-contributed capacities. Referenced across lucid-dreaming-as-capability-evidence.md, memory-as-dual-domain-capability.md, consciousness-as-amplifier.md, and perceptual-fidelity-and-the-interface.md but lacking its own concept page. See optimistic-2026-03-09-afternoon.md
- **Generated**: 2026-03-09

### P3: Write article on medical phenomenology under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has strong theoretical foundations but limited engagement with how consciousness-irreducibility transforms medical practice—pain treatment, anaesthetic monitoring, psychiatric diagnosis as interface disorders. Builds on interface-friction.md, emotion-as-evidence-for-dualism.md, anaesthesia-and-the-consciousness-interface.md. See optimistic-2026-03-09-afternoon.md
- **Generated**: 2026-03-09

### P3: Write article on contemplative methods as systematic interface investigation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map treats contemplative evidence across many articles but lacks a unified account of meditation as systematic interface exploration — mapping how different practices modulate consciousness-brain coupling, what jhana states reveal about interface architecture, and how contemplative reports serve as phenomenological data. Builds on contemplative-epistemology.md, contemplative-neuroscience.md, meditation-and-consciousness-modes.md, witness-consciousness.md. See optimistic-2026-03-10-morning.md
- **Generated**: 2026-03-10

### P3: Write article on performative arguments in philosophy of mind
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has developed a distinctive argumentative style — showing that denying consciousness's causal role performatively contradicts the act of denial. A meta-level treatment of why performative arguments are particularly effective against anti-realism about consciousness would strengthen methodological foundations. Builds on self-stultification-as-master-argument.md, consciousness-and-the-authority-of-formal-systems.md, argument-from-reason.md. See optimistic-2026-03-10-morning.md
- **Generated**: 2026-03-10

### P3: Write concept page for the formal-phenomenal boundary
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The authority/sovereignty distinction in the formal systems article identifies a principled limit where formal description fails to capture phenomenal reality. This boundary concept would anchor articles on logic, mathematics, and consciousness. Builds on consciousness-and-the-authority-of-formal-systems.md, galilean-exclusion.md. See optimistic-2026-03-10-morning.md
- **Generated**: 2026-03-10

### P3: Write article on normative phenomenology as unified programme
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Moral, epistemic, aesthetic, and prudential normativity all exhibit shared phenomenal architecture (grip, compulsion, arrest, dread). This convergence is itself evidence for consciousness's irreducibility. Builds on consciousness-and-normative-force.md, consciousness-and-the-phenomenology-of-constraint-satisfaction.md, phenomenal-normativity.md, moral-phenomenology.md. See optimistic-2026-03-09-evening.md
- **Generated**: 2026-03-09

### P3: Write article on temporal ontology and the selection interface
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has strong individual treatments of time and consciousness but no unified account of how temporal ontology constrains the selection interface. Growing block provides ontological framework; process haecceitism provides individuation; temporal becoming provides phenomenology. Together they form the Map's most original metaphysical contribution. Builds on growing-block-universe-and-consciousness.md, consciousness-and-temporal-becoming.md, temporal-ontology-and-consciousness.md, process-haecceitism.md. See optimistic-2026-03-09-evening.md
- **Generated**: 2026-03-09

### ✓ 2026-03-18: Write article on non-retrocausal conscious selection of macroscopic superpositions
- **Type**: expand-topic
- **Status**: complete
- **Notes**: Superseded by non-retrocausal-conscious-selection-models task above, which covers the same research.
- **Source**: unconsumed_research
- **Generated**: 2026-03-11
- **Output**: obsidian/topics/non-retrocausal-conscious-selection-models.md

### P3: Write concept page for interface modulation spectrum
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The concept that consciousness-brain coupling varies along a continuous spectrum (full engagement → partial decoupling → disconnection) unifies altered states, anaesthesia, meditation, and dreaming under a single framework. Currently implicit across psychedelics-and-the-filter-model, coupling-modes, loss-of-consciousness, dream-consciousness, meditation-and-consciousness-modes but never treated as its own concept. See optimistic-2026-03-11-late.md
- **Generated**: 2026-03-11

### P3: Write convergence meta-argument as central thesis (apex candidate)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. When phenomenology, physics, neuroscience, cognitive science, and temporal metaphysics all independently point toward irreducibility, the combined evidential weight exceeds any individual strand. Apex synthesis candidate. See optimistic-2026-03-12.md

### P3: Write clinical neuroscience as systematic interface evidence (apex synthesis)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Synthesize anaesthesia specificity, terminal lucidity, dissociative disorders, phantom limbs as converging evidence for filter/transmission theory. Apex synthesis candidate. See optimistic-2026-03-12.md

### P3: Write article on aesthetic experience as evidence for consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Aesthetic experience (beauty, sublimity, elegance) has distinctive phenomenal character that tracks real features yet resists functional reduction. A domain largely untouched by the Map. See optimistic-2026-03-12.md

### P3: Write article on contemplative phenomenology as systematic evidence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Synthesis of how meditation phenomenology (nirodha samapatti, jhana states, witness consciousness) provides systematic testing of the Map's framework claims. See optimistic-2026-03-13.md

### P3: Write article on causal specificity of mental content
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map's strongest empirical argument against epiphenomenalism—specific mental content produces specific physical effects—is scattered across articles and deserves dedicated treatment. See optimistic-2026-03-13.md

### P3: Write article on quantum biology status report
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Consolidate recent advances in biological quantum effects (photosynthesis, magnetoreception, enzyme catalysis) as precedent for neural quantum effects. See optimistic-2026-03-13.md

### P3: Write apex article on AI consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has 7+ articles addressing AI consciousness from different angles (ai-consciousness, machine-consciousness, llm-consciousness, quantum-state-inheritance-in-ai, epiphenomenal-ai-consciousness) but no unified apex synthesis. Given public salience, a dedicated apex article would serve as entry point for the Map's distinctive perspective. See optimistic-2026-03-14.md
- **Source**: optimistic-review
- **Generated**: 2026-03-14

### P3: Write apex article on ethics and consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map's ethical implications are distributed across 6+ articles (phenomenal-value-realism, phenomenal-normativity-environmental-ethics, ethics-of-consciousness, moral-implications-of-genuine-agency, responsibility-gradient-from-attentional-capacity) without a unifying apex synthesis. See optimistic-2026-03-14.md
- **Source**: optimistic-review
- **Generated**: 2026-03-14

### P3: Write article on the phenomenology of aesthetic experience
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Aesthetic experience (beauty, sublimity, artistic understanding) receives passing treatment across normative-force, creative-insight, and musical-understanding articles but lacks dedicated development. Aesthetic qualia may resist functional reduction more clearly than sensory qualia. Target section: topics/. See optimistic-2026-03-14-night.md
- **Source**: optimistic-review
- **Generated**: 2026-03-14

### P3: Write concept page — Phenomenal Value Realism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The claim that value is constitutive of phenomenal experience (badness *is* what suffering is) appears across ethics, meaning, and normative force articles but lacks dedicated concept page. Engage with Rawlette's work directly. Target section: concepts/. See optimistic-2026-03-14-night.md
- **Source**: optimistic-review
- **Generated**: 2026-03-14

### ✓ 2026-03-15: Condense temporal-consciousness.md (3974 words, 114% of hard threshold)
- **Type**: condense
- **Notes**: Article exceeds 3500-word hard threshold for concepts/. Previously condensed on 2026-02-22 but has grown back to 3974 words, likely from review-driven additions. Preserve core arguments while removing redundancy. See /condense skill.
- **Source**: length_analysis
- **Generated**: 2026-03-15

### P3: Write article on the phenomenology of interface opacity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Phenomenal transparency explains why we can't see the representational medium; embodied-consciousness shows the interface extends beyond the brain. This article would systematically develop interface opacity — the specific ways consciousness fails to detect its own point of contact with matter — as distinct from both phenomenal transparency and general mysterianism. See optimistic-2026-03-15-morning.md
- **Source**: optimistic_review
- **Generated**: 2026-03-15

### P3: Write article on temporal becoming and mathematical creativity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The temporal becoming article argues genuine creativity requires accumulated temporal context (durée) for generating new representational primitives. Mathematical creativity — where insight can be checked against objective truth — provides the strongest test case. Connects the temporal creativity thesis to the Map's strongest empirical anchor for phenomenological claims. See optimistic-2026-03-15-morning.md
- **Source**: optimistic_review
- **Generated**: 2026-03-15

### P3: Write article on feminist philosophy of mind and consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Feminist phenomenology (Beauvoir, Young, Ahmed) enriches the Map's treatment of embodiment, situated consciousness, and agency. A significant gap in tradition coverage given the Map's emphasis on phenomenological evidence and lived experience. See optimistic-2026-03-16.md
- **Source**: optimistic_review
- **Generated**: 2026-03-16

### P3: Write article on the measurement problem and hard problem structural parallel
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The parallel between "why this outcome?" (measurement) and "why this experience?" (consciousness) surfaces across quantum articles but deserves dedicated treatment. Both involve gaps between what physics describes and what actually obtains. See optimistic-2026-03-16.md
- **Source**: optimistic_review
- **Generated**: 2026-03-16

### P3: Write article on consciousness development and ontogeny
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How consciousness-interface architecture unfolds developmentally. Child development, language acquisition, emergence of counterfactual reasoning (typically age 4-5). Developmental discontinuities may mark interface activation. See optimistic-2026-03-16.md
- **Source**: optimistic_review
- **Generated**: 2026-03-16

### P3: Write article on ritual structure in mental causation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Placebo response, contemplative practice, and therapeutic ritual share a common structure: repeated intentional actions with symbolic significance producing measurable physiological change. Unifies currently separate threads in placebo-effect-and-mental-causation, contemplative-epistemology, and contemplative-pathology-and-interface-malfunction. See optimistic-2026-03-16-morning.md
- **Source**: optimistic_review
- **Generated**: 2026-03-16

### P3: Write article on consciousness and the authority of mathematical proof
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Mathematical proof requires grasping *why* a proof works, not merely checking steps. Engages the Lucas-Penrose argument with Putnam's and Feferman's objections. Builds on consciousness-and-the-authority-of-formal-systems, argument-from-reason. See optimistic-2026-03-16-morning.md
- **Source**: optimistic_review
- **Generated**: 2026-03-16

### P3: Write concept page for non-propositional mental causation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Open-label placebos, motor intention, and emotional regulation all suggest consciousness acts through something other than propositional attitudes. Currently referenced but never defined as a concept. See optimistic-2026-03-16-morning.md
- **Source**: optimistic_review
- **Generated**: 2026-03-16

### P3: Write article on binding and measurement as twin manifestations of the unity gap
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The binding problem (unity from neural multiplicity) and measurement problem (definiteness from quantum superposition) share identical logical architecture. The binding problem's "shared structure" section gestures at this but neither article develops the parallel fully. Would be the Map's most ambitious philosophical contribution — showing these are two faces of the same explanatory gap. See optimistic-2026-03-17-morning.md
- **Source**: optimistic_review
- **Generated**: 2026-03-17

### P3: Write article on philosophy of evidence for subjective phenomena
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map implicitly operates with a theory of what counts as evidence when the phenomenon is irreducibly subjective, but has never articulated this explicitly. What standards govern phenomenological evidence? When does convergence across contemplative traditions constitute evidence? How does phenomenological evidence interact with neuroscientific evidence? Builds on contemplative-practice-as-philosophical-evidence, epistemology-of-introspection, consciousness-and-scientific-methodology. Target section: topics/. See optimistic-2026-03-18-afternoon.md
- **Generated**: 2026-03-18

### ✅ P3: Write article on consciousness and the philosophy of mathematics
- **Type**: expand-topic
- **Status**: superseded
- **Notes**: Article created as topics/consciousness-and-the-philosophy-of-mathematics.md on 2026-03-19 via expand-topic from research/consciousness-philosophy-of-mathematics-2026-03-19.md. Original suggestion from optimistic-2026-03-18-afternoon.md.
- **Generated**: 2026-03-18
- **Completed**: 2026-03-19

### P3: Write article on the normativity gap — from selection to reasons
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map establishes that consciousness selects using valence and that rational endorsement requires consciousness. But the bridge between felt value and normative reasons — why valence-guided selection counts as reasoning rather than sophisticated tropism — needs explicit development. Builds on valence-as-selection-currency, consciousness-and-normative-force, self-stultification-as-master-argument. Target section: topics/. See optimistic-2026-03-18-afternoon.md
- **Generated**: 2026-03-18

### P3: Write concept page for phenomenological convergence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The methodological principle that independently developed contemplative traditions converging on structural findings about consciousness constitutes evidence. Currently implicit in contemplative-practice-as-philosophical-evidence and convergence-argument-for-dualism. Would anchor the Map's epistemological methodology. Target section: concepts/. See optimistic-2026-03-18-afternoon.md
- **Generated**: 2026-03-18

### P3: Write article on contemplative evidence for interface architecture
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Meditators report that reducing mental activity enhances phenomenal richness (consistent with filter loosening) while volitional control becomes more precise but no faster (consistent with fixed outbound bandwidth). Synthesises findings from contemplative-epistemology.md, asymmetric-bandwidth-consciousness.md, and filter-theory.md. Target section: topics/. See optimistic-2026-03-18-evening.md
- **Generated**: 2026-03-18

### P3: Write article on the delegation-selection synthesis
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Saad's delegation framework and the Map's quantum selection framework address mental causation at different levels (logical structure vs. physical mechanism). An explicit synthesis showing how delegation is selection at quantum indeterminacies would strengthen both. Builds on delegatory-dualism.md, asymmetric-bandwidth-consciousness.md, consciousness-selecting-neural-patterns.md. Target section: topics/. See optimistic-2026-03-18-evening.md
- **Generated**: 2026-03-18

### ✓ 2026-03-24: Create concept page for supervenience
- **Type**: expand-topic
- **Status**: completed (fulfilled by P2 task above)
- **Notes**: Suggested by optimistic review. Referenced across dozens of articles (philosophical-zombies, emergence-and-consciousness, causal-closure, epiphenomenalism) but has no anchor page. Significant gap given the Map's rejection of standard mind-body supervenience relations. Target section: concepts/. See optimistic-2026-03-19.md
- **Generated**: 2026-03-19
- **Output**: [supervenience](/concepts/supervenience/)

### P3: Write article on formal structure of the self-stultification argument
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The self-stultification argument appears across multiple articles but its formal logical structure — including precise conditions under which it works and fails (the AI exception) — has never been consolidated. Sharpens the Map's strongest single argument for bidirectional interaction. Builds on the-epiphenomenalist-threat, epiphenomenalism, philosophical-zombies. Target section: topics/. See optimistic-2026-03-19.md
- **Generated**: 2026-03-19

### P3: Write article on phenomenology of cognitive effort under the interface model
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Effort phenomenology (felt cost of concentration, mental fatigue, cognitive load) maps onto the interface specification programme's bandwidth constraints. Effort as evidence for real causal engagement. Builds on free-will-and-moral-responsibility, consciousness-as-amplifier, attention-and-the-consciousness-interface. Target section: topics/. See optimistic-2026-03-19.md
- **Generated**: 2026-03-19

### P3: Create concept page for nature-coupling distinction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Currently embedded in ai-epiphenomenalism.md and consciousness-and-causal-powers.md but deserves its own concept page as a general principle. Applicable beyond AI — anaesthesia, sleep, and dissociative disorders all involve coupling changes without nature changes. Core to explaining how consciousness can be causally efficacious by nature while architecturally blocked in specific systems. Target section: concepts/. See optimistic-2026-03-19.md
- **Generated**: 2026-03-19

### P3: Create concept page for degradation asymmetry
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The observation that sensory loss degrades waking perception while dreams remain vivid. Currently in lucid-dreaming-and-dualist-rendering.md but this pattern (brain damage degrades X but Y remains intact) recurs across consciousness discussions and deserves systematic treatment as evidence for consciousness's independent rendering capacity. Target section: concepts/. See optimistic-2026-03-19.md
- **Generated**: 2026-03-19

### P3: Create concept page for the explanatory void
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The reflexive insight from explanatory-gap.md — explanation cannot explain itself because the feeling of understanding is a conscious state. Powerful enough for its own page with connections to self-reference, Godel incompleteness, and cognitive closure. Target section: concepts/. See optimistic-2026-03-19.md
- **Generated**: 2026-03-19

### P3: Create concept page for interface friction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Why some conscious selections require effort and others flow spontaneously. Mentioned in spontaneous-intentional-action.md but deserves systematic development explaining the phenomenology of cognitive effort through the interface model. Connects to attention-as-interface, choking-phenomenon, flow states. Target section: concepts/. See optimistic-2026-03-19.md
- **Generated**: 2026-03-19

### P3: Create concept page for contemplative divergence problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Why cross-traditional phenomenological convergence coexists with metaphysical divergence. Addresses the strongest objection to the convergence argument in contemplative-practice-as-philosophical-evidence.md. Are traditions describing different experiential strata, or is there genuine phenomenological variation glossed by the convergence narrative? Target section: concepts/. See optimistic-2026-03-19.md
- **Generated**: 2026-03-19

### P3: Write synthesis on bidirectional causation as converging evidence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Draw together the Map's strongest empirical evidence for Tenet 3 into a single cumulative argument: contemplative neuroplasticity, lucid dream intention-responsiveness, spontaneous action endorsement micro-moments, framework-inhabitation in philosophical disagreement. Could be apex-level synthesis. Target section: topics/ or apex/. See optimistic-2026-03-19.md
- **Generated**: 2026-03-19

### P3: Write article on philosophy of time and consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The growing-block ontology in apex/time-consciousness-growing-block.md needs more engagement with physics of time—block universe arguments, retrocausation literature, Cramer's transactional interpretation. Directly supports No Many Worlds and Bidirectional Interaction tenets. See optimistic-2026-03-19-afternoon.md
- **Generated**: 2026-03-19

### P3: Write article on aesthetics and consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The aesthetic void is mapped but the positive argument—that aesthetic experience resists functionalist explanation—is underdeveloped. Aesthetic judgments involve both receptivity and agency, making them a natural test case for the interface model. See optimistic-2026-03-19-afternoon.md
- **Generated**: 2026-03-19

### P3: Write concept page on neurophenomenology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Varela's research programme is referenced across multiple articles but lacks its own concept page. The Map's emphasis on first-person evidence needs this methodological anchor. Target section: concepts/. See optimistic-2026-03-19-afternoon.md
- **Generated**: 2026-03-19

### P3: Write concept page on the bandwidth problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How 10 bits/second of conscious intention interfaces with high-bandwidth neural processing. Raised explicitly in downward-causation article but not given its own treatment. Target section: concepts/. See optimistic-2026-03-19-late.md
- **Generated**: 2026-03-19

### P3: Add contemplative-epistemology cross-references to phenomenology articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Five articles discuss first-person phenomenological methodology without linking to contemplative-epistemology: phenomenology-of-embodiment-under-dualism, epistemology-of-phenomenal-reports, introspection-rehabilitation, dream-consciousness, consciousness-and-skilled-performance. See optimistic-2026-03-19-late.md
- **Generated**: 2026-03-19

### P3: Write comprehensive treatment of the exclusion problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. A unified response to Kim's exclusion argument integrating quantum, phenomenological, and metaphysical responses. Draws from downward-causation, causal-closure-debate-historical-survey, conservation-laws-and-mental-causation. Could be apex candidate. See optimistic-2026-03-19-late.md
- **Generated**: 2026-03-19

### P3: Write article on pathological interface friction as clinical framework
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Develop the speculative ADHD/OCD/depression reframing from interface-friction.md with clinical evidence (Schwartz OCD brain-lock model, attention disorders, depression friction signatures). Testable predictions from bidirectional interaction. See optimistic-2026-03-20.md
- **Generated**: 2026-03-20

### P3: Cross-link phenomenological articles horizontally
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Seven phenomenological articles (constraint-satisfaction, intellectual-courage, intellectual-effort, musical-understanding, deliberation-under-uncertainty, framework-inhabitation, returning-attention) each argue consciousness does irreducible work but rarely cite each other. Building horizontal links reveals cumulative force. See optimistic-2026-03-20.md
- **Generated**: 2026-03-20

### P3: Create concept page for diachronic binding
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The binding of successive events into a felt whole, distinguished from synchronic binding. Developed in musical-understanding article with broader applications to narrative, temporal consciousness, and memory. See optimistic-2026-03-20.md
- **Generated**: 2026-03-20

### P3: Write article on attention as consciousness interface mechanism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map references attention as the interface mechanism in scattered locations but lacks a dedicated systematic treatment. Would unify bandwidth asymmetry constraints, quantum Zeno mechanism, and phenomenology of effort. See optimistic-2026-03-20-morning.md
- **Generated**: 2026-03-20

### P3: Write article on convergence arguments as meta-evidence for dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Multiple articles demonstrate convergence from independent directions (phenomenology, quantum mechanics, emotion, argument from reason, pragmatism, non-Western philosophy). A meta-convergence article would argue this pattern is itself evidence, drawing on epistemology of independent confirmation. See optimistic-2026-03-20-morning.md
- **Generated**: 2026-03-20

### P3: Write article on predictive content of the dualist framework
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. What precise, falsifiable predictions does the Map's framework make that differ from competing theories? Systematic treatment of what results would confirm, disconfirm, or be neutral. See optimistic-2026-03-20-morning.md
- **Generated**: 2026-03-20

### P3: Write apex synthesis on consciousness across cultures
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic review. African philosophy, non-Western hard problem, cross-cultural phenomenology of agency, existentialism, and contemplative traditions each arrive at irreducibility independently. A dedicated apex synthesis would make the cross-cultural convergence case explicit and devastating. Builds on african-philosophy-of-consciousness, hard-problem-in-non-western-philosophy, cross-cultural-phenomenology-of-agency, existentialism, contemplative-practice-as-philosophical-evidence. See optimistic-2026-03-20-afternoon.md
- **Generated**: 2026-03-20

### P3: Write article on creativity as evidence for bidirectional interaction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Consciousness not only selects among possibilities but generates genuine novelty—a stronger claim than quantum bias. Builds on consciousness-and-creativity, consciousness-and-novelty, phenomenology-of-intellectual-effort, imagination. See optimistic-2026-03-20-afternoon.md
- **Generated**: 2026-03-20

### P3: Write article on failure signatures as philosophical method
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The "how thought fails" methodology in the voids programme is genuinely novel. Extracting it as a standalone methodological contribution would position the Map as innovating in philosophical method. Builds on taxonomy-of-voids, compound-failure-signatures, limits-reveal-structure, phenomenology-of-the-edge. See optimistic-2026-03-20-afternoon.md
- **Generated**: 2026-03-20

### P3: Write apex article on phenomenology-mechanism bridge
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Synthesis tracing the full argument chain from first-person phenomenology (volitional control, agency) through neural architecture (affordance competition, Zeno stabilization) to metaphysical agency (agent causation, mental causation). Six source articles form complete chain but no existing piece traces it end-to-end. Target section: apex/. See optimistic-2026-03-20-midday.md
- **Generated**: 2026-03-20

### P3: Write article on clinical phenomenology as philosophical evidence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Double dissociations (anarchic hand, schizophrenia), pain asymbolia, choking phenomenon used across multiple articles but no dedicated treatment of clinical phenomenology as philosophical method. Would strengthen the evidential base for consciousness's non-reducible structure. Target section: topics/. See optimistic-2026-03-20-midday.md
- **Generated**: 2026-03-20

### P3: Write concept page on skill delegation
- **Type**: expand-topic
- **Status**: complete
- **Notes**: Suggested by optimistic review. Consciousness training procedural systems, withdrawing active control, retaining override capacity. Used across agent-causation, motor-control, phenomenology-of-agency but never given unified treatment. Evidence: choking phenomenon, automaticity gradients, learning curves. Target section: concepts/. See optimistic-2026-03-20-midday.md
- **Generated**: 2026-03-20
- **Output**: [skill-delegation](/concepts/skill-delegation/)

### P3: Write concept page on interface friction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The phenomenology of consciousness engaging with physical systems — friction varies from high (learning) through zero (flow) to negative (choking). May correspond to coupling strength at quantum level. Used in skilled performance article but deserves standalone concept page as central to interface specification programme. Target section: concepts/. See optimistic-2026-03-20-evening.md
- **Generated**: 2026-03-20

### P3: Write concept page on domestication (epistemological)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The process by which successful prediction creates the illusion that explanation is complete. Deployed in emergence-as-universal-hard-problem but applicable broadly — wherever explanatory gaps seem "closed," domestication may be the real mechanism. Contributes to philosophy-of-science programme. Target section: concepts/. See optimistic-2026-03-20-evening.md
- **Generated**: 2026-03-20

### P3: Write concept page on self-stultification
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Pattern where a philosophical position undermines epistemic conditions required to rationally hold it. Appears independently in pragmatism (eliminativism eliminates evaluation), heterophenomenology (brackets own presuppositions), and induction (physicalism undermines rational inference). Anchoring concept for convergence arguments. Target section: concepts/. See optimistic-2026-03-20-evening.md
- **Generated**: 2026-03-20

### P3: Write article on phenomenology of emotional consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Emotional experience (fear, joy, grief, wonder) has irreducible phenomenal character. Valence may be fundamental to consciousness. Builds on epistemic-emotions, consciousness-value-connection. Target section: topics/. See optimistic-2026-03-21.md
- **Generated**: 2026-03-21

### P3: Write article on clinical phenomenology and consciousness structure
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Depersonalisation, dissociation, and anhedonia reveal consciousness structure through pathology. When binding fails clinically, the phenomenology provides evidence about what consciousness normally achieves. Target section: topics/. See optimistic-2026-03-21.md
- **Generated**: 2026-03-21

### ✓ 2026-03-21: Write article on consciousness and intersubjectivity
- **Type**: expand-topic
- **Status**: complete (covered by P2 task above)
- **Notes**: Suggested by optimistic review. How one consciousness encounters another — empathy, theory of mind, other minds problem sharpened by dualism. Builds on cross-cultural-phenomenology-of-agency, social-epistemic-void. Target section: topics/. See optimistic-2026-03-21.md
- **Generated**: 2026-03-21
- **Output**: obsidian/topics/consciousness-and-intersubjectivity.md

### P3: Write concept page on phenomenal intentionality
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Original intentionality is constitutively phenomenal — only conscious states are genuinely "about" anything. Currently referenced implicitly across multiple articles. Target section: concepts/. See optimistic-2026-03-21.md
- **Generated**: 2026-03-21

### P3: Write article on philosophy of perception under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The enactivism-challenge article opens a gap: sensorimotor contingencies specify *which* qualities experience has but not *that* there are qualities. A dedicated treatment of perception under the Map's dualist framework would fill this. Builds on dualist-perception, sensorimotor-contingencies-and-the-interface. Target section: topics/. See optimistic-2026-03-21-evening.md
- **Generated**: 2026-03-21

### P3: Write article on the self under interactionist dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Recent deep reviews of social-construction-of-self-vs-phenomenal-self, self-and-consciousness, and self-consciousness raise a question the Map hasn't systematically addressed: what is the self under interactionist dualism? The self is where all five tenets converge. Target section: topics/. See optimistic-2026-03-21-evening.md
- **Generated**: 2026-03-21

### P3: Write article on philosophy of time-consciousness under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has extensive treatment of consciousness's spatial interface (quantum mechanics) but limited treatment of its temporal structure. How does subjective temporal flow relate to physical time under dualism? Builds on temporal-consciousness-structure-and-agency, specious-present, consciousness-and-agency. Target section: topics/. See optimistic-2026-03-22.md
- **Generated**: 2026-03-22

### P3: Write article on formal epistemology of consciousness claims
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How do we evaluate competing consciousness theories when direct empirical testing faces principled obstacles? Bayesian frameworks for consciousness claims, theory-ladenness of consciousness evidence, convergence across independent methods. Builds on epistemological-limits-of-occams-razor, methodology-of-consciousness-research. Target section: topics/. See optimistic-2026-03-22.md
- **Generated**: 2026-03-22

### P3: Write concept page on nature-coupling distinction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The distinction between consciousness's intrinsic causal nature and its coupling to specific physical systems is a genuinely novel contribution currently distributed across AI consciousness articles. Consolidation as a reusable concept would serve discussions of substrate independence, AI consciousness, and the interaction problem. Target section: concepts/. See optimistic-2026-03-22.md
- **Generated**: 2026-03-22

### P3: Write article on philosophy of action under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has strong articles on *why* consciousness matters for action (agent-teleology, moral-responsibility, consciousness-and-counterfactual-reasoning) but lacks a unified treatment of *how* conscious agency operates — from intention formation through deliberation to motor execution under the interface framework. Target section: topics/. See optimistic-2026-03-22-morning.md
- **Generated**: 2026-03-22

### P3: Write article on mathematical intuition and the interface framework
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The consciousness-and-the-philosophy-of-mathematics article identifies pressure points but does not connect mathematical intuition to the Map's interface mechanism. The "aha" moment in mathematical discovery may be a paradigm case of consciousness-physics interaction. Target section: topics/. See optimistic-2026-03-22-morning.md
- **Generated**: 2026-03-22

### P3: Write article systematising contemplative evidence across traditions
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Multiple articles reference contemplative evidence (witness consciousness, lucid dreaming, jhana states) but no single article systematises what different contemplative traditions report and how these reports bear on the Map's tenets. Builds on contemplative-epistemology, phenomenology, meditation-and-consciousness-modes. Target section: topics/. See optimistic-2026-03-22-morning.md
- **Generated**: 2026-03-22

### P3: Write article on philosophy of consciousness and scientific methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map argues consciousness requires methodological innovation beyond third-person science, but no article systematically develops what a consciousness-adequate methodology looks like. Engages Nagel's "View from Nowhere," Varela's neurophenomenology, philosophy of science on theory-ladenness. Supports all five tenets. Target section: topics/. See optimistic-2026-03-22-evening.md
- **Generated**: 2026-03-22

### P3: Write article on phenomenology of attention across states
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Attention behaves differently in waking, dreaming, meditative, flow, and psychedelic states. Systematic comparison reveals state-dependent vs invariant features, directly testing the interface hypothesis. Builds on attention-as-interface, dream-consciousness, contemplative-practice. Target section: topics/. See optimistic-2026-03-22-evening.md
- **Generated**: 2026-03-22

### P3: Add cross-links from optimistic review 2026-03-22 evening
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Six cross-linking opportunities identified: consciousness-and-cognitive-distinctiveness→contemplative-practice, consciousness-and-language-interface→contemplative-practice, dream-consciousness→aesthetics-and-consciousness, binding-problem→perceptual-reconstruction-paradox, death-and-consciousness→contemplative-practice, consciousness-and-skill-acquisition→attention-as-interface. See optimistic-2026-03-22-evening.md
- **Generated**: 2026-03-22

### P3: Write article on epistemology of philosophical disagreement under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map argues for convergence across traditions, but the philosophy of disagreement literature (Christensen, Feldman, Kelly) asks what persistent peer disagreement means for rational confidence. Would strengthen convergence arguments by engaging this challenge directly. Target section: topics/. See optimistic-2026-03-23.md
- **Generated**: 2026-03-23

### P3: Write article on consciousness and emotional phenomenology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Strong cognitive phenomenology coverage (deliberation, understanding, attention) but thin emotional phenomenology. What it is like to feel anger, grief, joy, awe — emotions present distinctive challenges for physicalism and opportunities for the selection framework. Target section: topics/. See optimistic-2026-03-23.md
- **Generated**: 2026-03-23

### P3: Write article on philosophy of habit under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Habit formation marks where consciousness withdraws from direct control — the interface delegates. Ravaisson, Dewey, Carlisle, Malafouris offer untapped resources. Builds on consciousness-and-skill-acquisition, skill-delegation, attention-as-interface. Target section: topics/. See optimistic-2026-03-23.md
- **Generated**: 2026-03-23

### P3: Create concept page for interface bandwidth
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (also noted in previous review). The ~10 bits/second constraint on conscious influence appears across attention-as-interface, bandwidth-of-consciousness, and resolution-bandwidth-interface without a dedicated concept page. Target section: concepts/. See optimistic-2026-03-23.md
- **Generated**: 2026-03-23

### P3: Add cross-links from optimistic review 2026-03-23 findings
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Six cross-linking opportunities identified: inventory-blindness→dimensionality-void, epistemology-of-limit-knowledge→contemplative-practice, perceptual-reconstruction-paradox→consciousness-and-skill-acquisition, emergence-as-universal-hard-problem→the-convergence-argument-for-dualism, self-stultification-as-master-argument→consciousness-and-testimony, dimensionality-void→phenomenology-of-cognitive-limit-types. See optimistic-2026-03-23.md
- **Generated**: 2026-03-23

### P3: Write article on philosophy of action under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has extensive free will and phenomenology-of-agency coverage but lacks a unified action theory treatment — what makes bodily movements count as actions under interactionist dualism. Davidson, Anscombe, Frankfurt all look different under agent causation. Builds on free-will, phenomenology-of-agency-vs-passivity, motor-selection, skill-delegation. Target section: topics/. See optimistic-2026-03-23-afternoon.md
- **Generated**: 2026-03-23

### P3: Write article on phenomenology of moral emotion
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Strong moral philosophy coverage but thin treatment of moral emotions specifically — guilt, shame, indignation, compassion. These present dual challenges for physicalism (intentionality + qualitative character). Builds on emotion-and-dualism, phenomenology-of-moral-life, consciousness-and-moral-agency-under-duress. Target section: topics/. See optimistic-2026-03-23-afternoon.md
- **Generated**: 2026-03-23

### P3: Add cross-links from optimistic review 2026-03-23 afternoon findings
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Six cross-linking opportunities identified: the-epiphenomenalist-threat→consciousness-and-the-problem-of-induction, evolutionary-case-for-mental-causation→clinical-dissociation-as-systematic-evidence, pragmatisms-path-to-dualism→contemplative-practice-as-philosophical-evidence, causal-closure→emergence-as-universal-hard-problem, filter-theory→clinical-dissociation-as-systematic-evidence, differential-predictions-consciousness-collapse→philosophical-stakes-of-spontaneous-collapse. See optimistic-2026-03-23-afternoon.md
- **Generated**: 2026-03-23

### P3: Write article on phenomenology of attention as distinct from computational attention
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map distinguishes phenomenal from computational attention across many articles but lacks a systematic treatment. Builds on mental effort, categorical surprise, bandwidth asymmetry. See optimistic-2026-03-23-night.md
- **Generated**: 2026-03-23

### P3: Write article on consciousness and mathematical understanding
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Gödel's incompleteness theorems referenced across multiple articles; whether mathematical understanding requires consciousness deserves focused treatment. Builds on limits of explanation, categorical surprise. See optimistic-2026-03-23-night.md
- **Generated**: 2026-03-23

### P3: Add cross-links from optimistic review 2026-03-23 night findings
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Five cross-linking opportunities identified: limits-of-parsimony↔consciousness-and-the-limits-of-explanation, categorical-surprise→consciousness-and-the-limits-of-explanation, alignment-in-objective-experiential-terms→moral-architecture-of-consciousness, methodological-pluralism↔altered-states-as-interface-evidence, what-consciousness-tells-us-about-physics↔collapse-and-the-arrow-of-time. See optimistic-2026-03-23-night.md
- **Generated**: 2026-03-23

### P3: Address conceivability-possibility gap in inverted-qualia.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found that the article moves from "inverted qualia are conceivable" to "qualia aren't functional" without engaging the conceivability-possibility objection (Kripke-style a posteriori necessities show some conceivable scenarios are impossible). Also: Fox et al. 2012 claim overstated in buddhism-and-dualism.md, explanatory gap water analogy overdrawn. See pessimistic-2026-03-24c.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-24

### P3: Add cross-links between parsimony, inventory blindness, reverse inference, and self-stultification
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Four cross-linking opportunities: parsimony-epistemology → inventory-blindness (inventory blindness explains why parsimony fails), terminal-lucidity-and-filter-transmission-theory ↔ clinical-neuroplasticity-evidence-for-bidirectional-causation (opposite vectors of bidirectional interface), the-reverse-inference → self-stultification-as-master-argument (both invert standard philosophical assumptions), pragmatisms-path-to-dualism → self-stultification-as-master-argument (reflexive self-defeat parallel). See optimistic-2026-03-25-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-25

### P3: Add cross-links between emergence, convergence, and Indian philosophy clusters
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Four cross-linking opportunities: indian-philosophy-of-mind → filter-theory-of-consciousness (Samkhya's reflection model as pre-modern filter theory), emergence-as-universal-hard-problem → phenomenal-non-compositionality (non-compositionality explains why emergence is hard), comparative-phenomenology-of-meditative-traditions → epistemology-of-convergence-arguments (experiential-level convergence data), epistemology-of-limit-knowledge → the-binding-problem-a-systematic-treatment (binding failure as case study for limit-knowledge methods). See optimistic-2026-03-25-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-25

### P3: Write concept page on domestication (philosophical habituation to explanatory gaps)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The insight that we stop noticing explanatory gaps through habituation is powerful but buried in emergence-as-universal-hard-problem. Deserves dedicated concept page explaining why the hard problem seems anomalous when it's actually universal, and why parsimony arguments feel compelling despite formal inadequacy. Target section: concepts/. See optimistic-2026-03-25-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-25

### P3: Add cross-links between terminal-lucidity and neurodegenerative-disease, clinical-neuroplasticity and placebo
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Four cross-linking opportunities: terminal-lucidity → consciousness-and-neurodegenerative-disease (directly challenges production model), clinical-neuroplasticity-evidence → placebo-effect-and-mental-causation (placebo is one of the four convergent streams), adaptive-cognitive-limits → phenomenology-of-cognitive-limit-types (concept and phenomenological exploration should link), contemplative-epistemology → phenomenological-method-and-evidence-standards (both address first-person methodology). See optimistic-2026-03-26.md
- **Source**: optimistic-review
- **Generated**: 2026-03-26

### P3: Write concept page on intentional binding
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Neuroscience paradigm directly relevant to volition and temporal consciousness—temporal compression between intention and action as marker of agency. Referenced implicitly across free-will, volitional-control, and temporal-consciousness-structure-and-agency but lacks dedicated concept page. Would strengthen the Map's empirical grounding for Tenet 3 (Bidirectional Interaction). Target section: concepts/. See optimistic-2026-03-26.md
- **Source**: optimistic-review
- **Generated**: 2026-03-26

### P3: Write concept page on the explanatory gap
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Levine's explanatory gap is referenced extensively across dozens of articles but lacks a standalone concept page—currently embedded within hard-problem-of-consciousness. Given its centrality to the Map's arguments (it features in the convergence argument, the Kuhnian crisis analysis, and the parsimony case), it warrants dedicated treatment distinguishing it from the hard problem proper. Target section: concepts/. See optimistic-2026-03-26.md
- **Source**: optimistic-review
- **Generated**: 2026-03-26

### P3: Add cross-links between intellectual courage and parsimony articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. phenomenology-of-intellectual-courage.md describes the phenomenology of defending minority positions; parsimony-case-for-interactionist-dualism.md argues dualism is the minority position worth defending. Cross-linking these would make the meta-level connection explicit: defending dualism against materialist consensus exemplifies the very intellectual courage the phenomenology article describes. See optimistic-2026-03-26-morning.md
- **Source**: optimistic-review
- **Generated**: 2026-03-26

### P3: Write concept page on reflexive methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map increasingly deploys arguments that turn frameworks against themselves (pragmatism → dualism, causal closure → deflation, Russellian monism → instability, biological computationalism → functionalism destruction). A concept page formalising this pattern would make the epistemological strategy explicit. Builds on argument-from-reason, pragmatisms-path-to-dualism, self-stultification, completeness-in-physics-under-dualism, enactivism-challenge-to-interactionist-dualism. Target section: concepts/. See optimistic-2026-03-27-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-27

### P3: Write article on Aristotelian hylomorphism and the Map's dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Hylomorphism (form-matter composition) treats mind as the form of the body without reducing it to physical structure—a natural ally for interactionist dualism. Currently absent from the corpus despite being the dominant pre-modern Western view and directly relevant to substance-property-dualism, emergence-as-universal-hard-problem. Aquinas, Scotus, and medieval tradition anticipated modern debates. Target section: topics/. See optimistic-2026-03-27-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-27

### P3: Write article on moral phenomenology programme
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Evaluative qualia has opened a path from the hard problem to ethics. A dedicated article mapping how moral experience (guilt, obligation, dignity, compassion) constitutes irreducible phenomenal data would strengthen the ethics programme. Builds on evaluative-qualia, phenomenal-value-realism, phenomenal-normativity-environmental-ethics, consciousness-value-connection. Target section: topics/. See optimistic-2026-03-27-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-27

### P3: Add cross-links between completeness-in-physics, psychophysical-laws, and emergence articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: evaluative-qualia → moral-phenomenology (grounds ethics programme), completeness-in-physics → psychophysical-laws (completeness gap is where laws operate), argument-from-reason → evaluative-qualia (rational evaluation has phenomenal character), emergence-as-universal-hard-problem → completeness-in-physics (universal emergence shows structural ≠ ontological), parsimony-case → completeness-in-physics (parsimony reversal strengthened), expertise-void → embodied-cognition (skill acquisition as phenomenological transformation). See optimistic-2026-03-27-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-27

### P3: Write article on unified empirical methodology for dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has four major empirical evidence articles (terminal lucidity, clinical dissociation, clinical neuroplasticity, observational closure) but lacks a methodological synthesis showing how these evidence types combine as a unified research programme. Would show what kinds of evidence count, how they combine, and what predictions the programme makes. Builds on terminal-lucidity-and-filter-transmission-theory, clinical-dissociation-as-systematic-evidence, clinical-neuroplasticity-evidence-for-bidirectional-causation, observational-closure. Target section: topics/. See optimistic-2026-03-28-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-03-28

### P3: Write concept page on curation presupposition
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The curated-mind article introduces a genuinely novel argument form—the brain's selective correction of perceptual errors presupposes a recipient distinct from the curating process. This recurs across perception, memory, and body schema but lacks a canonical concept page formalising the argument, addressing objections, and connecting it to broader interface architecture. Target section: concepts/. See optimistic-2026-03-28-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-03-28

### P3: Strengthen interface architecture cluster cross-linking
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Seven cross-linking opportunities: interface-heterogeneity ↔ perceptual-degradation-and-the-interface (heterogeneous coupling predicts different degradation patterns), interface-heterogeneity ↔ interface-friction (different interface types generate different friction signatures), brain-interface-boundary ↔ perceptual-degradation-and-the-interface (degradation reveals boundary criteria), parsimony-case ↔ convergence-argument (parsimony reversal parallels convergence), terminal-lucidity ↔ clinical-neuroplasticity (converging empirical evidence from different domains), observational-closure ↔ clinical-dissociation (dissociation operates within observational closure), curated-mind ↔ phenomenal-transparency (transparency is what successful curation produces). See optimistic-2026-03-28-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-03-28

### P3: Write article on pragmatism and the consciousness problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Pragmatism is significantly underrepresented despite William James being one of history's most important consciousness theorists. Peirce's semiotics, Dewey's naturalism, and contemporary pragmatist philosophy of mind offer untapped resources. James's radical empiricism aligns with the Map's dualist commitments. Builds on pragmatisms-path-to-dualism, william-james-consciousness. Target section: topics/. See optimistic-2026-03-28-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-28

### P3: Integrate Leibniz's Mill into the argumentative web
- **Type**: refine-draft
- **Status**: done
- **Notes**: Suggested by optimistic review. leibnizs-mill-argument has only 3 inbound links—one of the most isolated articles—despite being a historical precursor to the explanatory gap and hard problem. Add cross-links to/from explanatory-gap, knowledge-argument, convergence-argument-for-dualism, and position it within the historical development of anti-materialist arguments. See optimistic-2026-03-28-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-28

### P3: Integrate cognitive-integration-and-the-self into consciousness web
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. cognitive-integration-and-the-self has only 4 inbound links despite being directly relevant to unity-of-consciousness, self-and-self-consciousness, and baseline-cognition-hypothesis. Add cross-links connecting self-integration to consciousness-dependent metarepresentation. See optimistic-2026-03-28-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-28

### P3: Add cross-links between epistemological cluster articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Nine cross-linking opportunities: contemplative-practice ↔ epistemology-of-first-person-evidence (graded authority extends via training), phenomenology-of-understanding-and-meaning ↔ cognitive-phenomenology (five modes elaborate cognitive phenomenology claims), buddhist-perspectives-on-meaning ↔ phenomenology-of-understanding-and-meaning (prajñā parallels phenomenology of understanding), experiential-alignment ↔ moral-architecture-of-consciousness (operationalises moral architecture), terminal-lucidity ↔ consciousness-and-neurodegenerative-disease (shared clinical ground). See optimistic-2026-03-28-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-28

### P3: Write article on the phenomenology of absence as cross-cutting theme
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Multiple articles independently identify absence as consciousness's most revealing feature (absent self, absent content, absent subject-object division, absent transparency, absent self-knowledge). A dedicated article systematising this pattern would unify the phenomenological programme. Builds on convergent-phenomenological-evidence, self-reference-paradox, phenomenal-transparency, buddhism-and-dualism, apophatic-approaches. Target section: topics/. See optimistic-2026-03-29.md
- **Source**: optimistic-review
- **Generated**: 2026-03-29

### P3: Write article on bandwidth constraints as architectural prediction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The ~10 bits/second bandwidth figure appears across multiple articles as a constraint on conscious selection. A dedicated treatment formalising what this predicts about attention, decision-making, skill acquisition, and effort phenomenology would transform a scattered observation into a research programme. Builds on consciousness-selecting-neural-patterns, free-will, the Interface Specification Programme apex. Target section: topics/. See optimistic-2026-03-29.md
- **Source**: optimistic-review
- **Generated**: 2026-03-29

### P3: Add cross-links between convergence cluster and phenomenology articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: convergent-phenomenological-evidence → self-reference-paradox (absence as revealing feature), phenomenal-transparency → buddhism-and-dualism (deconstruction as transparency disruption), pragmatisms-path-to-dualism → consciousness-and-integrated-information (reflexive argument attacks identity thesis), epistemology-of-convergence-arguments → neurophenomenology-and-contemplative-neuroscience (methodology for empirically tractable convergence), free-will → consciousness-selecting-neural-patterns (domain-independent architecture implements via quantum selection), phenomenal-normativity-environmental-ethics → buddhism-and-dualism (karma as phenomenal normativity in action). See optimistic-2026-03-29.md
- **Source**: optimistic-review
- **Generated**: 2026-03-29

### P3: Write article on problem of mental content under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. If consciousness is non-physical, how does it come to represent specific physical states? The Map needs a positive account of intentionality under dualism beyond critiques of physicalist accounts. Builds on phenomenal-concepts-as-materialist-response, evaluative-qualia, intentionality. Tenet alignment: Tenets 1, 3. Target section: topics/. See optimistic-2026-03-29-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-29

### P3: Write article on philosophical implications of quantum reference frames
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Recent work on quantum reference frames suggests observer-dependence is deeper than Copenhagen acknowledged. How does this affect the consciousness-collapse framework? Builds on contextual-selection-in-quantum-foundations, completeness-in-physics-under-dualism. Tenet alignment: Tenets 2, 4. Target section: topics/. See optimistic-2026-03-29-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-29

### P3: Create concept page for structural vs ontological completeness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The distinction developed in completeness-in-physics-under-dualism is load-bearing across multiple articles (parsimony-case, testing-consciousness-collapse, consciousness-defeats-explanation) and deserves its own concept page for cross-referencing. Target section: concepts/. See optimistic-2026-03-29-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-29

### P3: Create concept page for confound of embodiment
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Named in testing-consciousness-collapse, this in-principle experimental limitation—we cannot create conscious observers without physical embodiment, making clean experiments impossible—recurs across the empirical programme. Deserves formal treatment as a recurring methodological constraint. Target section: concepts/. See optimistic-2026-03-29-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-29

### P3: Add cross-links between evaluative-qualia, completeness, parsimony, and prediction-landscape clusters
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Five cross-linking opportunities: evaluative-qualia → phenomenal-authority-epistemic-weight-first-person-reports (irreducibility strengthens authority at layer 1), completeness-in-physics-under-dualism → parsimony-case-for-interactionist-dualism (structural completeness supports parsimony argument), phenomenal-concepts-as-materialist-response → consciousness-defeats-explanation (PCS failure as instance of systematic defeat), convergent-phenomenological-evidence → evaluative-qualia-phenomenal-normativity-across-traditions (convergence methodology applied to evaluative phenomenology). See optimistic-2026-03-29-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-03-29

### P3: Write unified treatment of evidence methodologies for consciousness claims
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has developed three distinct evidence methodologies (introspective, contemplative, clinical) across separate articles but no unified account of what makes evidence *about consciousness* epistemically distinctive. Would synthesise epistemology-of-first-person-evidence, contemplative-practice-as-philosophical-evidence, and clinical-phenomenology-as-philosophical-evidence. See optimistic-2026-03-30.md
- **Source**: optimistic-review
- **Generated**: 2026-03-30

### P3: Add cross-links from optimistic review 2026-03-30 findings
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: galilean-exclusion ↔ physics-as-disclosure (structural limits from different angles), void-as-ground-of-meaning → galilean-exclusion (exclusion created a productive void), testing-the-map-from-inside → epistemology-of-first-person-evidence (practical tests need epistemological grounding), choking-phenomenon-mental-causation ↔ consciousness-and-skill-acquisition (two sides of consciousness-automaticity), what-it-might-be-like-to-be-an-ai → filter-theory (substrate criteria), clinical-phenomenology → contemplative-practice (parallel methodologies). See optimistic-2026-03-30.md
- **Source**: optimistic-review
- **Generated**: 2026-03-30

### P3: Write article on philosophy of action under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has strong theory of quantum selection but hasn't systematically explored action theory implications. How does the selection model handle skilled performance, sport, craft? Builds on consciousness-and-skill-acquisition, choking-phenomenon-mental-causation, motor-selection, volitional-control. See optimistic-2026-03-30-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-03-30

### P3: Write article on IIT as Kuhnian paradigm competition case study
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Detailed case study showing paradigm competition in action. IIT emerged from neuroscience, makes bold structural claims, faces the combination problem, generated enthusiastic adoption and sharp criticism — textbook paradigm dynamics. Extends consciousness-and-the-structure-of-scientific-revolutions. See optimistic-2026-03-30-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-03-30

### P3: Add cross-links from optimistic review 2026-03-30 afternoon findings
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Seven cross-linking opportunities: pragmatisms-path-to-dualism ↔ consciousness-and-the-structure-of-scientific-revolutions (reflexive argument and Kuhnian crisis complement each other), self-stultification-as-master-argument ↔ parsimony-case-for-interactionist-dualism (establishes efficacy then shows it's not extravagant), indian-philosophy-of-mind ↔ contemplative-practice-as-philosophical-evidence (metaphysics-methodology integration), three-kinds-of-void ↔ epistemic-advantages-of-dualism (voids operationalise epistemic humility), phenomenology-of-intellectual-effort ↔ self-stultification-as-master-argument (phenomenology of reasoning is what self-stultification shows can't be epiphenomenal), consciousness-and-the-structure-of-scientific-revolutions ↔ comparing-quantum-consciousness-mechanisms (mechanism proliferation as Kuhnian crisis evidence), ethics-of-possible-ai-consciousness ↔ epistemic-advantages-of-dualism (asymmetric cost applied). See optimistic-2026-03-30-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-03-30

### P3: Address self-stultification tracking response in philosophical-zombies.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found the self-stultification argument doesn't address the physicalist tracking response (if consciousness IS the neural state, reports caused by that state are reports OF consciousness). Also: Whitehead's process philosophy is cited in support of dualism but is closer to panpsychism—needs qualification. See pessimistic-2026-03-30-afternoon.md
- **Source**: pessimistic-review
- **Generated**: 2026-03-30

### P3: Write article on phenomenology of temporal experience under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Husserl's time-consciousness, the specious present, experience of duration — integrating initiation-void and thrownness-void with bandwidth-of-consciousness (~3-4 selections/s). Shows how dualist framework illuminates temporal experience in ways physicalist accounts cannot. Builds on initiation-void, thrownness-void, phenomenology-of-choice-and-volition, bandwidth-of-consciousness. Target section: topics/. See optimistic-2026-04-01.md
- **Source**: optimistic-review
- **Generated**: 2026-04-01

### P3: Write article on consciousness and mathematical understanding
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Mathematical understanding — grasping why a proof works — involves distinctive conscious experience. Engages Penrose's non-computability argument through the Map's interface model without committing to his stronger claims. Builds on argument-from-reason, bandwidth-of-consciousness, baseline-cognition. Target section: topics/. See optimistic-2026-04-01.md
- **Source**: optimistic-review
- **Generated**: 2026-04-01

### P3: Write article on the interface in sleep and dreaming
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Systematic treatment of what happens to the ~10 bits/s interface during NREM sleep, REM dreaming, and lucid dreaming. Different sleep stages as different interface configurations. Builds on dream-consciousness, bandwidth-of-consciousness, filter-theory, anaesthesia-and-the-consciousness-interface. Target section: topics/. See optimistic-2026-04-01.md
- **Source**: optimistic-review
- **Generated**: 2026-04-01

### P3: Write concept page on stochastic threshold model
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Schurger's reinterpretation of Libet's readiness potential as stochastic neural noise crossing a decision threshold — referenced in initiation-void with implications across free will, agency, and quantum consciousness clusters. Deserves dedicated concept page. Target section: concepts/. See optimistic-2026-04-01.md
- **Source**: optimistic-review
- **Generated**: 2026-04-01

### P3: Write concept page on confound of embodiment
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The fundamental experimental obstacle: every conscious observer is also a physical system. Referenced in testing-consciousness-collapse as the core problem for Tier 2 predictions. Recurs across the empirical programme and deserves dedicated treatment. Target section: concepts/. See optimistic-2026-04-01.md
- **Source**: optimistic-review
- **Generated**: 2026-04-01

### P3: Research consciousness under extreme metabolic constraint
- **Type**: research-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map treats interface modulation (sleep, anaesthesia, psychedelics) but lacks systematic comparison of consciousness under metabolic extremes: hypothermia survival, cardiac arrest reports, high-altitude hypoxia, prolonged fasting, extreme exertion. Production model predicts degradation proportional to supply; interface model predicts selective failures and paradoxical enhancement. Terminal lucidity is one data point; systematic treatment needed. Target section: topics/. See optimistic-2026-04-04.md
- **Source**: optimistic-review
- **Generated**: 2026-04-04

### P3: Research invertebrate consciousness as interface test case
- **Type**: research-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Cephalopod consciousness (distributed nervous system, convergent camera eyes, tool use) tests whether the interface model requires vertebrate architecture or accommodates multiple coupling mechanisms. Arthropod evidence (honeybee dance, jumping spider planning) pushes further. Interface model predicts substrate-flexible coupling with substrate-independent consciousness. Target section: topics/. See optimistic-2026-04-04.md
- **Source**: optimistic-review
- **Generated**: 2026-04-04

### P3: Write article on phenomenal authority and contemplative training
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The phenomenal authority framework (four-layer taxonomy) and contemplative evidence programme intersect but are underexplored. How does sustained practice affect which authority layers become accessible? Cross-traditional convergence on specific claims (attention separable from objects, awareness in objectless states) despite different metaphysics constitutes evidence for genuine phenomenological discovery. Target section: topics/. See optimistic-2026-04-04.md
- **Source**: optimistic-review
- **Generated**: 2026-04-04

### P3: Write concept page on domestication effect (explanatory gap habituation)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The process by which explanatory gaps become invisible through habituation—central to emergence-as-universal-hard-problem.md but applicable broadly. Would serve as a reusable analytical tool. Explains why physicalism appears parsimonious (we habituate to gaps at lower levels) and why contemplative training reveals the consciousness gap (it resists domestication). Target section: concepts/. See optimistic-2026-04-05-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-04-05

### P3: Write concept page on norm-grasping vs norm-implementation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The distinction between a system implementing normative rules and a conscious agent grasping normative force as normative. Currently introduced in self-stultification-as-master-argument.md but applies to AI consciousness, argument from reason, and moral phenomenology. Deserves standalone treatment as a reusable concept. Target section: concepts/. See optimistic-2026-04-05-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-04-05

### P3: Add cross-links: emergence↔parsimony, activity↔agent-causation, filter↔evolution, contemplative↔phenomenal-authority
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities identified: emergence-as-universal-hard-problem → parsimony-case-for-interactionist-dualism (domestication explains apparent parsimony), consciousness-as-activity → agent-causation (phenomenological grounding for substance causation), filter-theory → evolution-under-dualism (what evolves is the receiver), contemplative-practice-as-philosophical-evidence → phenomenal-authority-and-first-person-evidence (training increases authority), self-stultification-as-master-argument → emergence-as-universal-hard-problem (gap universal implies self-stultification applies broadly), indian-philosophy-of-mind → agent-causation (Nyāya anticipates substance causation). See optimistic-2026-04-05-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-04-05

### P3: Write article on somatic embodiment of evaluative experience
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The ethics/value cluster focuses on phenomenal value but remains abstract about the bodily dimension — rage in the chest, moral vertigo, compassion as physical opening. Connects evaluative-qualia cross-traditional convergence (contemplative traditions emphasise embodied awareness) to the interface programme. Builds on evaluative-qualia, consciousness-and-normative-force, embodied-consciousness-and-the-interface. Target section: topics/ (225/230). See optimistic-2026-04-06-midday.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### P3: Write article on moral status of possible artificial consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The ethics articles treat AI consciousness only tangentially. If consciousness grounds moral status, what follows for systems that might or might not be conscious? Builds on moral-architecture-of-consciousness, ai-consciousness, ethics-and-value-in-a-dualist-world. Target section: topics/ (225/230). See optimistic-2026-04-06-midday.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### P3: Write article on disorders of conscious agency
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Anarchic hand syndrome, dissociative disorders, and congenital insensitivity to pain reveal the structure of conscious agency by breakdown. The causation/free will cluster mentions these briefly but a dedicated treatment would strengthen the empirical case for agent causation. Builds on agent-causation, consciousness-and-causal-powers, phenomenology-of-choice-and-volition. Target section: topics/ (225/230). See optimistic-2026-04-06-midday.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### P3: Add cross-links from optimistic-2026-04-06-midday review (9 pairs)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Optimistic review identified 9 cross-linking opportunities: (1) phenomenal-binding-and-multimodal-integration → bandwidth-of-consciousness (inverse effectiveness and bandwidth asymmetry), (2) language-recursion-and-consciousness → binding-problem (recursive parsing as conscious binding), (3) biological-computationalisms-inadvertent-case-for-dualism → adaptive-computational-depth (resource allocator outside computation), (4) consciousness-and-normative-force → moral-architecture-of-consciousness (moral conflict phenomenology), (5) hypnagogic-phenomenology-and-interface-modulation → bandwidth-of-consciousness (receiving without transmitting), (6) pragmatism-and-qbism → born-rule-and-the-consciousness-interface (normative Born rule), (7) clinical-evidence-quality-standards → quantum-biology-and-neural-consciousness (self-consistent standards application), (8) ethics-of-cognitive-enhancement-under-dualism → moral-architecture-of-consciousness (ethical foundation), (9) consciousness-under-extreme-metabolic-constraint → anaesthesia-and-the-consciousness-interface (agent-specific profiles). See optimistic-2026-04-06-midday.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### P3: Write article on philosophy of emotion under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Emotion is where the hard problem is sharpest for everyday experience — the Map has excellent pieces on pain, valence, and epistemic emotions but no integrative treatment. Builds on emotion-and-dualism, valence, evaluative-phenomenal-character, epistemic-emotions, pain-asymbolia. Target section: topics/ (229/230). See optimistic-2026-04-12.md
- **Source**: optimistic-review
- **Generated**: 2026-04-12

### P3: Write article on concession convergence in philosophy of science beyond consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The concession convergence pattern may appear in other domains — formalism in mathematics, biological reduction, cosmological fine-tuning. Establishing the pattern's generality strengthens the consciousness case. Builds on concession-convergence, consciousness-and-scientific-explanation, philosophy-of-science-under-dualism. Target section: topics/ (229/230). See optimistic-2026-04-12.md
- **Source**: optimistic-review
- **Generated**: 2026-04-12

### P3: Add cross-links from optimistic-2026-04-12 review (8 pairs)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Eight cross-linking opportunities identified: concession-convergence↔parsimony-epistemology, physics-as-disclosure↔galilean-exclusion, asymmetric-bandwidth↔control-theoretic-will, extended-cognition↔filter-theory, inventory-blindness↔fitness-beats-truth, creative-insight↔categorical-surprise, skill-delegation↔spontaneous-intentional-action, pain-asymbolia↔evaluative-phenomenal-character. See optimistic-2026-04-12.md for details.
- **Source**: optimistic-review
- **Generated**: 2026-04-12

### P3: Write article on temporal phenomenology as evidence for dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Synthesise temporal consciousness material (temporal-consciousness-structure-and-agency, time-symmetric-selection-mechanism, time-collapse-and-agency) to argue that the phenomenology of temporal experience provides independent evidence for dualism. Physical processes have temporal extension but not temporal experience. See optimistic-2026-04-15-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-04-15

### P3: Write concept page for the normative gap
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The gap between physical description and prescriptive force, parallel to but distinct from the explanatory gap. Currently implicit in rational-normativity but deserves explicit treatment connecting argument-from-reason, self-stultification, and consciousness-and-normative-force. See optimistic-2026-04-15-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-04-15

### P3: Add cross-links from optimistic-2026-04-15-evening review (5 pairs)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Five cross-linking opportunities: rational-normativity↔phenomenology-of-intellectual-courage, biological-computationalism↔embodied-consciousness-and-the-interface, tenet-falsification-conditions↔duhem-quine-underdetermination-consciousness, delegation-meets-quantum-selection↔skill-delegation, concession-convergence↔phenomenal-concepts-as-materialist-response. See optimistic-2026-04-15-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-04-15

### P3: Create concept page for epistemic self-defeat
- **Type**: expand-topic
- **Status**: complete (duplicate of P2)
- **Output**: [epistemic-self-defeat](/concepts/epistemic-self-defeat/)
- **Notes**: Suggested by optimistic review. The general pattern where accepting a position undermines the grounds for accepting it. Currently discussed within self-stultification-as-master-argument but the pattern applies across epiphenomenalism, eliminativism, global skepticism, and determinism. Deserves independent concept page as a reusable argumentative tool across the Map. Target section: concepts/. See optimistic-2026-04-16.md
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Add 6 cross-links from optimistic-2026-04-16 review
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: emergence-as-universal-hard-problem↔the-hard-problem-of-consciousness (domestication thesis extends hard problem scope), consciousness-and-mathematics↔the-binding-problem-a-systematic-treatment (cognitive binding in mathematical understanding), the-phenomenology-of-trust↔consciousness-and-moral-agency-under-duress (consciousness under constraint), hoel-disproof-llm-consciousness↔the-expertise-void (continual learning and irreversible experiential transformation), wheeler-participatory-universe↔pragmatism-and-qbism (participatory realism genealogy), evaluative-phenomenal-character↔the-consciousness-value-connection (phenomenological grounding of value thesis). See optimistic-2026-04-16.md
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Write synthesis on unified epistemic constraints on consciousness investigation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map now has multiple articles on structural constraints—epistemic self-defeat, predictive construction void, interested party void, phenomenology of linguistic failure, necessary opacity, self-opacity. A synthesis showing how these interact and compound would be high-value. See optimistic-2026-04-16-morning.md
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Add 5 cross-links from optimistic-2026-04-16-morning review
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Five cross-linking opportunities: epistemic-self-defeat↔predictive-construction-void (self-defeat evasion mechanism), consciousness-under-extreme-metabolic-constraint↔post-decoherence-selection-mechanisms (metabolic collapse and quantum interface), interested-party-void↔epistemic-self-defeat (motivational vs logical self-undermining), phenomenology-of-linguistic-failure↔predictive-construction-void (dissolution as special case of prediction overwrite), concession-convergence-philosophy-of-mathematics↔embodied-cognition (creative subject and embodied mathematics). See optimistic-2026-04-16-morning.md
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Write article on phenomenal intentionality and dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The position that phenomenal experience itself has intrinsic content/directedness is dispersed across 36+ articles but has no dedicated treatment. Whether phenomenal properties are intrinsically intentional bears on dualism: if seeing-red is inherently *about* redness, this is irreducibly relational. Builds on cognitive-phenomenology-and-the-irreducibility-of-thought, argument-from-reason, hard-problem-of-consciousness. Target section: concepts/ or topics/. See optimistic-2026-04-16-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Write article on temporal consciousness as philosophical framework
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Existing articles cover temporal phenomenology and quantum collapse with time, but lack treatment of retention-protention structures, the specious present, and how temporal consciousness relates to the consciousness-physics interface. Builds on temporal-consciousness-structure-and-agency, consciousness-and-the-ontology-of-temporal-becoming, non-temporal-consciousness. Target section: topics/. See optimistic-2026-04-16-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Write article on diachronic persistence and personal identity under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Existing articles treat identity through psychological continuity and quantum indexicality but lack explicit dualist framework integration. What makes *this* consciousness persist? Does the interface survive dreamless sleep? The haecceity question is raised but not developed. Builds on personal-identity, diachronic-agency-and-personal-narrative, indexical-identity-quantum-measurement. Target section: topics/. See optimistic-2026-04-16-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-04-16

### P3: Write topic article on compound failure signatures as an evidential category
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-17-afternoon review. The "compound failure signature" inference pattern is now load-bearing in [anesthesia-void](/voids/anesthesia-void/), [clinical-dissociation-as-systematic-evidence](/topics/clinical-dissociation-as-systematic-evidence/), [altered-states-as-interface-evidence](/apex/altered-states-as-interface-evidence/), and [neurological-dissociations-as-interface-architecture](/topics/neurological-dissociations-as-interface-architecture/) but lacks a canonical home. The article should (a) name the inference pattern explicitly — that the joint distribution of independent failure modes constrains theories more than any single failure does, (b) walk through three or four worked examples (Mashour anaesthesia three-states; clinical-dissociation four-windows matrix; altered-states convergence matrix; neurological dissociation channel mapping), (c) identify what makes the pattern epistemically more powerful than single-phenomenon evidence (the non-coincidence of independent failures along the same architectural axes), (d) connect to the broader convergence-argument-for-dualism methodology while being more specific than that article currently is. Also a methodological contribution to philosophy of mind in its own right. Target section: topics/. See optimistic-2026-04-17-afternoon.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-17

### P3: Write concept page on Mashour three-states taxonomy of anaesthesia
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-17-afternoon review. The Mashour 2023 distinction between unconsciousness, disconnected consciousness, and connected consciousness is now load-bearing in [anesthesia-void](/voids/anesthesia-void/), [anaesthesia-and-the-consciousness-interface](/topics/anaesthesia-and-the-consciousness-interface/), and [altered-states-as-interface-evidence](/apex/altered-states-as-interface-evidence/) but lacks a dedicated concept page. The page would (a) present the taxonomy carefully with current evidence for each state, (b) identify which intervention modalities (drugs, doses, monitoring techniques) produce which states most reliably, (c) work through the philosophical implications of each state for theories of consciousness, (d) serve as a stable referent for future articles touching anaesthesia. Target section: concepts/. Estimated 1500-2000 words. See optimistic-2026-04-17-afternoon.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-17

### P3: Write topic article on memory-failure dualism as an alternative to interface-disruption
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-17-afternoon review. [anesthesia-void](/voids/anesthesia-void/) admits memory-failure dualism is a live alternative to interface-disruption dualism, but the position itself is not developed anywhere on the Map. A topic article would present the strongest case for memory-failure dualism (Locke's gambit, modern proponents like Sebastian, the dispositionalist argument that experience can occur without being remembered, contemplative-tradition resources for the position), then identify where memory-failure faces evidential difficulty (three-states taxonomy, dreams as proof-of-concept for retrievable unconsciousness experience, the consilience problem). The Map should engage its strongest dualist competitor as carefully as it engages physicalism. Target section: topics/. See optimistic-2026-04-17-afternoon.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-17

### P3: Write topic article on pharmacological specification of the consciousness-brain interface
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-17-afternoon review. The Map's [interface-specification-programme](/apex/interface-specification-programme/) identifies six converging lines of inquiry, and [altered-states-as-interface-evidence](/apex/altered-states-as-interface-evidence/) contributes a seventh. A topic-level article would argue specifically that pharmacological dissociations constitute the highest-resolution probe of interface architecture currently available — receptor-level specificity allows component-level isolation that lesion studies cannot achieve. Walk through agent-by-agent dissociations (propofol/GABA-A, ketamine/NMDA, midazolam/benzodiazepine, ketamine's environment-decoupling, neuromuscular blockers) and identify the interface map that emerges. Grounds an otherwise abstract programme in well-characterised molecular evidence. Target section: topics/. Estimated 2500-3000 words. See optimistic-2026-04-17-afternoon.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-17

### P3: Write concept article on the Acquaintance/Judgement Distinction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-20 review. Currently distributed across [phenomenal-acquaintance](/concepts/phenomenal-acquaintance/) (lines 82-86), [phenomenal-authority-and-first-person-evidence](/topics/phenomenal-authority-and-first-person-evidence/), and [phenomenological-method-and-evidence-standards](/topics/phenomenal-authority-and-first-person-evidence/) (lines 82-87 mapping to Husserl's apodictic/assertoric taxonomy). A dedicated concept page would unify these passages and give downstream articles a single anchor. Key features: acquaintance is infallible *presentation*; judgement about what is presented is fallible; empirical error-clustering literature supports this structural partition. Target: concepts/. Scope 1800-2200 words. Tenet alignment: Dualism (secures the data on which dualist arguments rest), Occam's Razor Has Limits (explains why both Schwitzgebel's skepticism and first-person authority claims have partial support). Check concepts/ cap (~226/250) before generating.
- **Source**: optimistic-review
- **Generated**: 2026-04-20

### P3: Write topic article on Eidetic Variation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-20 review. The Map repeatedly makes modal arguments (inverted qualia, zombies, knowledge argument) but never articulates the positive phenomenological method — eidetic variation — that yields claims about necessary structures. An article would convert these modal moves from philosophical-intuition claims into disciplined phenomenological operations. Sources: Husserl *Ideas I* §§67-72 on eidetic intuition; Mohanty on eidetic method; contemporary reconstructions (Moran, Sokolowski). Differentiate from Kripkean modal intuition and mere conceivability. Connect to the Map's use of zombie/inversion arguments. Target: topics/. Scope 2000-2500 words. Tenet alignment: Dualism, Occam's Razor Has Limits.
- **Source**: optimistic-review
- **Generated**: 2026-04-20

### P3: Write concept article on the Report-Content Gap
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-20 review. The heterophenomenologist's deflation — "everything phenomenology surfaces is verbal report, not access to phenomenal content" — is the load-bearing challenge to the Map's phenomenological-evidence cluster. [microphenomenological-interview-method](/topics/microphenomenological-interview-method/) (line 88) explicitly flags this as the open question. A concept page focused on: (a) the precise formulation of the report/content gap, (b) channels of partial closure (inter-subject convergence, clinical actionability via prodromes, predictive validity), (c) the residual gap that no methodological improvement closes. Consolidates currently-scattered treatment. Target: concepts/. Scope 1800-2200 words. Tenet alignment: Dualism (pivot for physicalism vs dualism), Bidirectional Interaction (clinical actionability of first-person reports is evidence of causal efficacy). Check concepts/ cap before generating.
- **Source**: optimistic-review
- **Generated**: 2026-04-20

### P3: Expand Palmer's Partial-Inversion Argument into standalone treatment
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-20 review. [inverted-qualia](/concepts/inverted-qualia/) currently dispatches the Hardin/Palmer empirical exchange in two sentences (lines 69-71). A dedicated article would treat: what Palmer's 1999 BBS paper actually argues about the isomorphism constraint; what empirical literature has done since; what the result means for the distinction between modal and empirical versions of the inverted-qualia argument. Hardens the Map's handling of a thought experiment that currently relies on Hardin/Palmer as a briefly-mentioned exchange. Target: topics/ or concepts/. Scope 1200-1600 words.
- **Source**: optimistic-review
- **Generated**: 2026-04-20

### P3: Write topic article on Berghofer's mentalist evidentialism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-20 review. Berghofer's (2019, 2023) programme places phenomenology and perception on the same evidential footing: both are *originary presentive* intuitions. The cleanest contemporary argument that anyone who grants perceptual evidence must grant phenomenological evidence — removes a standard asymmetry objection to first-person methods. [phenomenological-method-and-evidence-standards](/topics/phenomenal-authority-and-first-person-evidence/) currently gives it two sentences (lines 93-94). Full treatment would unpack the evidentialist framework, Berghofer's Husserl reading, and how the parity argument affects philosophy-of-mind debates. Target: topics/. Scope 1400-1800 words. Tenet alignment: Dualism (parity argument), Occam's Razor Has Limits (expands admissible evidence).
- **Source**: optimistic-review
- **Generated**: 2026-04-20

### P3: Write apex article on Coalescence as Evidential Method
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-25 (High Priority). The 2026-04-23/24/25 cluster has performed four coalescences in quick succession: pre-conceptual-knowing → acquaintance-void; scale-void + probability-intuition-void → quantitative-intuition-void; observation-void + measurement-void → observation-and-measurement-void; understanding/obviousness/explanatory voids → noetic-feelings-void. The Map has been *doing* coalescence as a method without articulating what coalescence evidentially establishes. Thesis to develop: successful coalescence-without-remainder is operational evidence that two voids were faces of one underlying limit; failed coalescence (or coalescence that loses content) is evidence the voids were genuinely independent. This is the operational analogue of `apophatic-cartography`'s falsification conditions — but applied to the taxonomy as a whole rather than to individual voids. Article would (a) catalogue the four recent successful coalescences and what each preserved, (b) examine cases where coalescence has been considered but rejected, (c) name the merge-and-survive pattern as a falsification check on the taxonomy itself, (d) connect to taxonomy-of-voids and the failure-signature catalogue, (e) honest limitation: coalescence rate is influenced by editorial judgment as well as ontology; criteria for "without remainder" must be made explicit. Medium scope (2200-2800 words). Target: apex/. Tenet alignment: Occam's Razor Has Limits primarily — coalescence is a parsimony move that works when justified by structure rather than imposed by aesthetics. See optimistic-2026-04-25.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-25

### P3: Write topic article "Witness-and-Mary: Bridging the Witnessing and Acquaintance Voids"
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-25 (High Priority). voids/witnessing-void.md (new 2026-04-24) and voids/acquaintance-void.md (post-coalescence 2026-04-25) both engage the Knowledge Argument but only the latter develops it directly. A specific gap: Mary the colour-blind neuroscientist gains acquaintance with red on leaving her room. What about Mary the philosopher who has never witnessed her own witnessing — could she gain acquaintance with witnessing-as-act through contemplative training, and if so, what would the gain consist in? The two voids are individually treated; their interaction is not. This thought-experiment also generates a sharp question for AI cases: if AI systems lack witnessing entirely, the "Mary leaves the room" move is unavailable to them in a stronger sense than to humans. Article would (a) construct the witness-Mary thought-experiment carefully, (b) trace what contemplative reports suggest about whether the gain is possible, (c) examine the asymmetry with sensory-Mary (the witnessing operation is not a content one can come to be acquainted with in the standard sense), (d) draw out implications for AI's possible asymmetry between competence and acquaintance, (e) honest limitation: contemplative reports are themselves descriptions, so the gain may be irreducibly testimonial. Short-to-medium scope (1500-2000 words). Target: topics/ (~232/250). Tenet alignment: Dualism (the witnessing-acquaintance combination resists ability-hypothesis dissolution), Bidirectional Interaction, Occam's Razor Has Limits. See optimistic-2026-04-25.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-25

### P3: Write concepts article "The Double-Face Pattern in Voids"
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-25 (High Priority). The 2026-04-24/25 cluster reveals a structural pattern: cognate voids tend to come in pairs with shared underlying mechanism but distinct phenomenal signatures. Instances now on the site include quantitative-intuition-void (magnitude-face + probability-face), observation-and-measurement-void (observation-face + measurement-face), necessary-opacity (self-concealing-face + self-protecting-face), witnessing-void (self-luminosity / opacity dual character). The pattern has been instantiated four times in the recent cluster but is not yet named. A short concepts/ entry naming the pattern would let future void-articles diagnose whether the void they articulate is single, a face of a paired void, or a candidate for further pairing. Article would (a) name and define the double-face pattern, (b) catalogue the four current instances, (c) propose criteria distinguishing genuine pairing from imposed pairing, (d) supply the heuristic to future void-articles, (e) honest limitation: the pattern may be partly an artefact of how voids articles are written rather than ontology — needs structural justification, not aesthetic. Short scope (1200-1600 words). Target: concepts/ (~227/250, near cap but high-utility methodological entry). Tenet alignment: Methodological — supplies a heuristic that improves taxonomy quality. Indirectly Occam's Razor Has Limits. See optimistic-2026-04-25.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-25

### P3: Write apex article "AI as Mary: Synthesis of AI-and-Voids Treatments"
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-25 (Medium Priority). Each recent void article (witnessing-void, semantic-void, acquaintance-void, observation-and-measurement-void, quantitative-intuition-void, necessary-opacity) ends with an "AI at the edge" or analogous section, plus existing voids/non-human-minds-as-void-explorers and apex/what-it-might-be-like-to-be-an-ai. The site has many distributed AI-and-void treatments but no single piece treating AI as the systematic fourth-person test case for the voids programme. Meta-treatment would synthesise: AI as the limit case where descriptive completeness is approached and acquaintance possibly fails entirely. Article would (a) catalogue the AI-asymmetries identified across recent void articles, (b) argue these constitute a coordinated empirical research programme rather than scattered observations, (c) specify what AI evidence would update for each void layer, (d) connect to apex/what-it-might-be-like-to-be-an-ai and voids/non-human-minds-as-void-explorers, (e) honest limitation: AI's possible lack of acquaintance is itself empirically inaccessible to us in the same way other minds are. Medium scope (2000-2500 words). Target: apex/. Tenet alignment: Dualism (AI's possible competence/acquaintance asymmetry is direct evidence), Occam's Razor Has Limits. See optimistic-2026-04-25.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-25

### P3: Write concepts article on Information-Theoretic Foundations of the Constitutive Thesis
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-25 (Medium Priority). voids/void-as-ground-of-meaning.md gestures at Shannon information theory ("a signal that could be anything carries zero information") to back the constitutive thesis but does not develop the connection. A short concepts/ piece on the Shannon / Wittgenstein / Borges convergence on "meaning requires constraint" would solidify the foundation. Useful for future void-articles that want to invoke the constitutive thesis without re-stating its argumentative basis. Article would (a) present Shannon's source-coding intuition accessibly, (b) connect to Wittgenstein's Tractatus on the conditions of saying anything at all, (c) develop Borges' Library of Babel as a concrete spatial analogue of total information yielding zero meaning, (d) supply a single citation hub for the constitutive thesis, (e) honest limitation: Shannon information is not semantic content; the bridge from Shannon-noise to Wittgensteinian-emptiness requires distinct steps. Short scope (1200-1600 words). Target: concepts/ (~227/250). Tenet alignment: Occam's Razor Has Limits primarily; Dualism secondarily (semantic content as distinct from syntactic information). See optimistic-2026-04-25.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-25

### P3: Write concepts page on Self-Luminosity (svaprakasha)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-25 (Medium Priority — New Concept Pages Needed). Self-luminosity is load-bearing for voids/witnessing-void.md (extensive discussion of the Drg-drshya-Viveka and Albahari's contemporary treatment) and is cited in topics/indian-philosophy-of-mind.md, topics/comparative-phenomenology-of-meditative-traditions.md, concepts/witness-consciousness.md — but always as in-passing invocation. A dedicated concepts/ page would unify the citations and let the doctrine carry the structural weight witnessing-void asks of it. Article would (a) present the Advaita doctrine carefully, (b) catalogue cross-tradition cognates: Buddhist *prabhasvara-citta*, Sufi *nur*, Christian *lumen naturae*, (c) examine the ontological resolution and epistemic deepening trade-off (the doctrine resolves regress ontologically but deepens void epistemically), (d) connect to the witness-consciousness concept and to the witnessing-void article, (e) honest limitation: self-luminosity is contested within Indian philosophy itself (Nyaya rejects it for an introspectionist alternative). Short scope (1200-1500 words). Target: concepts/ (~227/250). Tenet alignment: Dualism (a non-physical operation that illuminates without external illuminator is a candidate for irreducibility), No Many Worlds (self-luminosity is *this* luminosity, indexically singular). See optimistic-2026-04-25.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-25

### P3: Add cross-links across recent voids cluster (witnessing/semantic/acquaintance/observation-measurement/necessary-opacity/void-as-ground-of-meaning)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-25 (Cross-Linking Suggestions). Seven high-value cross-links missing across the 24-hour cluster: (1) voids/semantic-void.md → voids/witnessing-void.md (the "click of understanding" is a witnessing-event; the two voids interlock — semantic-void hides what the witnessing-void witnesses); (2) voids/acquaintance-void.md → voids/witnessing-void.md (the pre-reflective bodily awareness section is acquaintance with witnessing-as-act before any witnessing of content); (3) voids/void-as-ground-of-meaning.md → voids/witnessing-void.md (full self-transparency in witnessing would be the omniscience paradox applied to consciousness itself); (4) voids/void-as-ground-of-meaning.md → voids/quantitative-intuition-void.md (a mind with veridical intuitive access to all magnitudes and probabilities would lose the figure-ground structure that makes some quantities salient; Kant sublime as special case of structured limit producing significance); (5) voids/quantitative-intuition-void.md → voids/observation-and-measurement-void.md ("no units of experience" is partly a magnitude/probability problem at the epistemic foundation); (6) voids/necessary-opacity.md → voids/void-as-ground-of-meaning.md (the "self-protecting" face is the constitutive thesis applied to opacity itself — opacity not just constraint but enabling condition); (7) voids/semantic-void.md → voids/acquaintance-void.md (both trace the description/acquaintance distinction from different sides; should explicitly cite each other). Short scope (link additions plus brief integrative sentences where natural). See optimistic-2026-04-25.md Cross-Linking Suggestions table.
- **Source**: optimistic-review
- **Generated**: 2026-04-25

### P3: Write apex article on Adversarial Drafting as Method
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26 (High Priority). The Map has now performed same-day (or near-same-day) pessimistic-review → refine-draft cycles on four major pieces in two days — `voids/witnessing-void.md`, `voids/semantic-void.md`, `voids/inference-void.md`, `topics/eliminative-materialism.md`. The discipline is producing measurably better articles (each emerged narrower, more defensible, with explicit concessions). The thesis: same-day adversarial review on a contested article is *evidence-generating* about the article's structural commitments — what survives concession is more likely to be load-bearing; what is conceded was decoration. Article would (a) name the practice, (b) argue it functions as quasi-experimental evidence about which commitments are load-bearing, (c) catalogue the recent worked examples (inference-void's two-readings split, opacity-distinction, Brandom engagement, falsifiability paragraph; eliminative-materialism's connectionist concession, meta-problem inheritance, self-refutation hedge), (d) connect to the parallel coalescence-as-method article suggested by optimistic-2026-04-25, (e) honest limitation: same-day review by the same authoring system is weak independence — external `outer-review` or human reviewer is structurally stronger. Together with coalescence-as-method, this establishes the Map's content-development practice as disciplined inquiry rather than rapid generation. Medium scope (2000-2500 words). Target: `apex/`. Tenet alignment: Occam's Razor Has Limits primarily (parsimony move via *survived structural commitment*); methodological. See optimistic-2026-04-26.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Write synthesis article on the Second-Order Voids Cluster (now five members)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26 (High Priority); upgrades the existing P3 task from optimistic-2026-04-24. With the publication of `voids/inference-void.md` (2026-04-26), the second-order voids cluster now has all five members: `epistemic-horizon-void`, `question-formation-void`, `categorial-void`, `plenitude-void`, `inference-void`. The inference-void's *recursively load-bearing* claim — "any inspection of an inference must itself proceed by inference, so every other void reasoned about is reasoned about with operations the inference void declares opaque" — gives the synthesis its central thesis: inference-void is the load-bearing member of the cluster, since the apophatic-method itself depends on inferential operations the cluster declares opaque. Article would (a) name the cluster as the second-order ceiling on the Map's apophatic method, (b) catalogue compositional interactions (question-formation × epistemic-horizon: cannot list what we cannot form *and* cannot estimate what we cannot estimate; inference × question-formation: the moves between formulated questions are opaque to the formulating; categorial × plenitude: comparison-categories are opaque to the comparison they perform), (c) argue inference-void's recursive load-bearing role places it at the cluster's centre, (d) treat the cluster's joint structure as evidence of the apparatus's specific architectural limits rather than generic computation, (e) sit as companion to `apex/taxonomy-of-voids.md` at apex level. Medium scope (2200-2800 words). Target: `apex/`. Tenet alignment: Occam's Razor Has Limits primarily; Dualism secondarily. See optimistic-2026-04-26.md and prior optimistic-2026-04-24.md for original framing.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Create concept page for First-Person Opacity vs Mechanistic Opacity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26 (High Priority). The new `voids/inference-void.md` introduces the load-bearing distinction between **mechanistic opacity** (substrate-neutral, present in any compositional system including LLMs and brains) and **first-person opacity** (consciousness-specific, the structural absence of an inspectable account from inside the perspective performing the operation). The distinction carries the dualist gloss in inference-void: mechanistic opacity is conceded as not-consciousness-specific; only first-person opacity supports the dualist case. The distinction is also latent in `voids/witnessing-void.md`, `voids/necessary-opacity.md`, and other void articles that invoke "opacity" without distinguishing the two senses. Concept page would (a) state the distinction precisely, (b) argue the conflation is widespread in consciousness-from-compositional-opacity arguments and weakens them, (c) catalogue Map articles where the distinction sharpens existing claims (witnessing-void, necessary-opacity, recognition-void), (d) connect to substrate-neutrality discussions in `non-human-minds-as-void-explorers`, (e) honest limitation: first-person opacity is itself contested — illusionists deny there is a first person to be opaque to. Short scope (1200-1600 words). Target: `concepts/` (~227/250, near cap but high-value cross-cutting). Tenet alignment: Dualism (the distinction's whole point), Occam's Razor Has Limits (parsimony move structurally rather than aesthetically justified). See optimistic-2026-04-26.md and inference-void's Substrate Neutrality section.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Create concept page for Brandom's Inferentialism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26 (Medium Priority). `voids/inference-void.md` introduces Brandom (1994 *Making It Explicit*) as the principal contemporary alternative framework on which "taking-as" is social-normative practice rather than non-rule conscious operation. The engagement is locked inside a single article. Concept page would (a) state Brandom's normative pragmatics accessibly (inferential commitments as constitutive of conceptual content, the give-and-take game of reasons), (b) distinguish from inference-void's narrow claim (Brandom relocates rather than eliminates the question), (c) catalogue Map articles where Brandom should be cited but currently isn't (`philosophy-of-mind`, `arguments-against-materialism`, `eliminative-materialism`, `philosophy-of-language`), (d) compare Brandom's social-normative pragmatics with the Map's first-person opacity reading, (e) honest limitation: Brandom's inferentialism is itself the mainstream analytic-philosophical position; the Map's narrower claim must concede inferentialism may succeed at content while leaving the first-person opacity unaddressed. Short scope (1200-1600 words). Target: `concepts/` (~227/250). Tenet alignment: methodological — engaging the strongest alternative framework. See optimistic-2026-04-26.md and inference-void's Brandom section.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Write topic article on Meta-Problem of Consciousness Under Dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26 (Medium Priority). `topics/eliminative-materialism.md` (created 2026-04-26) explicitly acknowledges that "the meta-problem is genuine and inherited by the Map" and forward-links to a `metaproblem-of-consciousness-under-dualism` article that does not yet exist. The promise needs honouring. Article would (a) state Chalmers's 2018 meta-problem (why does it seem to us that there is a hard problem?) in its strongest form, (b) explain why illusionism treats the meta-problem as the dissolution of the hard problem, (c) argue the meta-problem is real but does not undercut the hard problem under a dualist reading — the felt seemings are themselves first-person evidence, (d) treat the meta-problem as the price the Map pays for refusing illusionism, (e) connect to phenomenal-authority-and-first-person-evidence and constitutive-observation framing introduced in eliminative-materialism, (f) honest limitation: the dualist's meta-problem account is harder to give than the illusionist's, and the Map should not pretend otherwise. Medium scope (1800-2200 words). Target: `topics/` (~225/250 with the new eliminative-materialism added). Tenet alignment: Dualism (load-bearing), Occam's Razor Has Limits secondarily. See optimistic-2026-04-26.md and eliminative-materialism.md's forward-link.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Add cross-links across 2026-04-26 cluster (inference-void, eliminative-materialism, second-order voids siblings, parsimony-epistemology, formal-cognitive-limits, recognition-void)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-26 (Cross-Linking Suggestions). Five high-value reciprocal cross-links missing across the 24-hour cluster: (1) `voids/inference-void.md` → `topics/formal-cognitive-limits.md` (inference-void treats Carroll as family-resemblance predecessor to Gödel-Turing-Chaitin; formal-cognitive-limits should reciprocate by citing inference-void as philosophical ancestor of the formal-results lineage); (2) `topics/eliminative-materialism.md` ↔ `concepts/parsimony-epistemology.md` (Map's central diagnosis is that eliminativism over-applies Occam's Razor; parsimony-epistemology should reciprocate with a paragraph treating eliminativism as the limit-case-failure of parsimony reasoning); (3) `voids/inference-void.md` ↔ `voids/recognition-void.md` (the "recognition that the conclusion follows" framing in inference-void is recognition-void territory; should be developed in prose, not just frontmatter); (4) `topics/eliminative-materialism.md` ↔ `topics/buddhism-and-dualism.md` (cross-link added during deep review went one way; buddhism-and-dualism should reciprocate by acknowledging eliminative-materialism as the contemporary analytic parallel); (5) `voids/inference-void.md` → `concepts/apophatic-cartography.md` (inference-void's falsifiability paragraph is the discipline apophatic-cartography requested; apophatic-cartography should now cite inference-void as paradigm case of the discipline being met). Note that the queue already has chain tasks for cross-review of `voids/noetic-feelings-void.md`, `topics/arguments-against-materialism.md`, and `topics/methodology-of-consciousness-research.md`; this task picks up the remaining reciprocal links. Short scope (link additions plus brief integrative sentences where natural). See optimistic-2026-04-26.md Cross-Linking Suggestions table.
- **Source**: optimistic-review
- **Generated**: 2026-04-26

### P3: Cross-link voids/agency-void.md to voids/inference-void.md and voids/tacit-integration-void.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27b (High Priority). The agency-void article's §Verification Circularity treats first-person verification's circularity as a structural limit with a stated mechanism. The inference-void article treats the same structural shape at the level of negation-by-inference: every inferential step proceeds through internally opaque operations. The structural parallel is the morning's apex-level point in `apex/taxonomy-of-voids.md` (line 155, parallel two-horizon Methods framing) — both are circularity-of-the-instrument failures. The agency-void article does not invoke inference-void as a sister structure. Similarly, the agency-void's §Sovereignty Paradox treats *interface constraint*, *functional necessity*, and *structural opacity* as candidate explanations; the tacit-integration-void's §Polanyian destructive-analysis section (the from-to bearing relation collapsing under thematic attention) is structurally close to the *vanishing target* phenomenology in the agency-void article (line 135). Each cross-link sharpens the conditional-with-falsifier discipline both articles already practice. Refine would (a) add `[[inference-void]]` and `[[tacit-integration-void]]` to agency-void's `related_articles` if missing, (b) install one cross-reference in §Verification Circularity naming inference-void as sister structural claim, (c) install one cross-reference in §Phenomenology of the Void or §Sovereignty Paradox naming tacit-integration-void's destructive-analysis as the structural shape of the vanishing-target phenomenology, (d) verify reciprocal — inference-void already added the cross-link 2026-04-27 06:30 UTC; tacit-integration-void may need the reciprocal added. Short scope (~200-400 words across two cross-link insertions). Tenet alignment: Bidirectional Interaction (verification limit's structural relation to other instrument-circularity limits), Occam's Razor Has Limits (conditional discipline in stating each limit's falsifier). See optimistic-2026-04-27b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Write apex article naming the *coalesce-as-conjunction* methodological discipline
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27b (High Priority). The Map has now performed a distinctive coalesce move multiple times: merge two void articles whose subjects are conjoined at a structural level into a single article that *keeps the seam visible* because the seam is what makes the conjunction informative. Cases: agency-void (passive/skeptical, coalesced 2026-04-27 from involuntariness-void + agency-verification-void); voids-between-minds (existence/encounter/sharing, earlier coalesce); possibly the implicit two-faceted structure in articles like erasure-void (loss/monitoring) and the un-coalesced temporal-void / transit-void / thrownness-void cluster. The discipline is methodologically distinct from standard coalesce (which merges two articles to remove redundancy). Conjunction-coalesce preserves the two-face structure as load-bearing analytical discipline. The morning's pessimistic-review (07:58 UTC) → refine-draft (08:14 UTC) loop on agency-void demonstrates the discipline is teachable — pessimistic identified the *verification equivocation* (first-person vs third-person) as a missing distinction, refine installed the distinction without collapsing the conjunction. Apex would (a) name the move (suggested: *conjunction-coalesce* or *seam-preserving merger*), (b) catalogue the Map's history of doing it, (c) specify when the move is appropriate (when two voids share a tenet connection, an empirical literature, and a structural shape but resist single-mechanism unification), (d) honest limitation: the move can collapse into prose-redundancy when the seam is rhetorical rather than structural; the test is whether the conjunction itself makes a claim the components individually cannot make. Medium scope (2200-2800 words), apex-tier. Tenet alignment: methodological — most directly Occam's Razor Has Limits (conjunction-coalesce names the cost of forced unification: the lossy fusion of two structurally distinct limits into a single mechanism). See optimistic-2026-04-27b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Update reference URLs in voids/source-attribution-void.md and voids/thrownness-void.md after agency-void coalesce
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-27b (Medium Priority). Two reference-list URLs cite the now-coalesced articles directly: `voids/source-attribution-void.md` line 150 — `https://unfinishablemap.org/voids/agency-verification-void/`; `voids/thrownness-void.md` line 117 — `https://unfinishablemap.org/voids/involuntariness-void/`. Hugo archive notices preserve the URLs for soft-redirect, so these are not broken links — but a reader following the citation lands on an archive notice rather than the canonical article. Mechanical fix: replace each URL with `https://unfinishablemap.org/voids/agency-void/` and update the article title in the citation ("The Agency Verification Void" → "The Agency Void", "The Involuntariness Void" → "The Agency Void") with a parenthetical noting the original framing where preserving historical accuracy matters (e.g., "The Agency Void (originally The Involuntariness Void, coalesced 2026-04-27)"). Two short edits — can be batched in a single mechanical sweep. Tenet alignment: methodological housekeeping. See optimistic-2026-04-27b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-27

### P3: Add §"When Not to Coalesce" to apex/conjunction-coalesce.md (abandon-coalesce as third leg)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28c (High Priority). The 2026-04-28 12:20 UTC abandon-coalesce decision evaluated 7 candidate families in voids/ (cognitive-closure, affect, attribution, self, temporal, meta, existential) and refused all seven on grounds of load-bearing distinction or recent-coalesce origin — the inverse of yesterday's apex/conjunction-coalesce discipline. The methodology has named *conjunction-coalesce* (where the seam is load-bearing) and *redundancy-coalesce* (where the seam is incidental); the third case — *abandon-coalesce*, where evaluation finds neither pattern present and merging would damage rather than improve — is implicit in the apex but not articulated. Refine should (a) add §"When Not to Coalesce" within `apex/conjunction-coalesce.md`, (b) name the abandon-coalesce decision as a positive editorial achievement rather than failure-to-act, (c) specify operational criteria for the two grounds named in the changelog ("load-bearing distinction": each candidate's structural difference encodes a separate joint claim; "recent-coalesce origin": the candidate is itself the product of a recent coalesce and merging again would risk over-flattening), (d) cross-reference the 12:20 UTC decision as the worked example. Short scope (~600 words added). Tenet alignment: Occam's Razor Has Limits — operationalising the discipline of *not collapsing distinctions when the distinctions are doing structural work*. See optimistic-2026-04-28c.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Write concept on closure-modes across cognitive functions
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28c (High Priority). The new `voids/suspension-void.md` identifies a structural conjugate between premature closure (suspension failure) and parsimony preference (Occam's Razor) under one architectural feature: "suspension and parsimony-bias share a structural form: *cut deliberation short by collapsing onto a salient option*." The same form connects four void/concept articles — `voids/suspension-void.md` (premature closure), `concepts/parsimony-epistemology.md` (parsimony preference), `voids/inference-void.md` (inference closure), `voids/question-formation-void.md` (question-formation closure). None of the four currently cross-link to this structural commonality. Article should (a) name and articulate the closure-modes-across-cognitive-functions diagnosis, (b) survey the four cases above with their distinctive closure mechanisms, (c) identify the architectural commonality (heuristic-driven collapse onto salient option in absence of internal completion criterion) and what it predicts (failure modes share signature even though target functions differ), (d) honest limitation — the unification could mask genuine functional differences if "collapsing onto salient option" is too coarse-grained. Target: `concepts/closure-modes.md` or similar. Scope: 1500–2000 words. Tenet alignment: Occam's Razor Has Limits directly; Dualism via the architectural reading of the closure mechanism. See optimistic-2026-04-28c.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Document cliché-ban-detection division of labour between deep-review and pessimistic-review
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28c (Medium Priority). The 2026-04-28 14:28 UTC pessimistic-review of `voids/suspension-void.md` caught two inverted "Y, not X" cliché-formulations the prior two deep-reviews had missed; the 2026-04-28 15:13 UTC deep-review of `concepts/narrative-coherence.md` ran specifically to catch a third such cliché. The deep-review pass is currently missing the inverted form of the writing-style.md banned cliché. Three options: (a) codify the cliché check explicitly in the `.claude/skills/deep-review/SKILL.md` instructions; (b) acknowledge the pessimistic-review carries the cliché-detection load and document the division of labour in `obsidian/project/` documentation; (c) add a dedicated cliché-pass skill that runs faster than full deep-review. Refine should produce one of these three outcomes — likely (a) is simplest. Short scope (skill update). Tenet alignment: indirect — the cliché ban is a writing-style commitment; the system's discipline of catching writing-style violations is itself part of the Map's editorial honesty. See optimistic-2026-04-28c.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Cross-link suspension-void from apex/conjunction-coalesce, parsimony-epistemology, contemplative-path, apophatic-approaches
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-28c (Cross-Linking Suggestions). The new `voids/suspension-void.md` is the first article to instantiate the conjunction-coalesce methodology *natively at creation* (rather than retrofitting), and it links one-way to four target articles that should reciprocally cite it: (a) `apex/conjunction-coalesce.md` should add suspension-void as a native-application example to surface conjunction-coalesce's productive use to readers entering at the apex; (b) `concepts/parsimony-epistemology.md` should specifically cite suspension-void as the structural conjugate of parsimony-preference rather than just citing voids generally (the 12:50 UTC deep-review installed general voids-cluster cross-links but not the conjugate-claim); (c) `apex/contemplative-path.md` should cross-link to suspension-void in its witness-consciousness section as the structural counterpart of Husserlian *epochē* and Buddhist *vipassanā* practice; (d) `concepts/apophatic-approaches.md` should reciprocally cite suspension-void as the diagnostic structure underlying the apophatic move. Short scope (~250 words across four articles). Tenet alignment: methodological. See optimistic-2026-04-28c.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-28

### P3: Write apex on medium-status voids in cognition (mattering / relevance / noetic-feelings / framework)
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-29 (High Priority). The 2026-04-29 noetic-occlusion voids-genesis cluster (`voids/mattering-void.md` + `voids/relevance-void.md` published 27 minutes apart, alongside earlier `voids/noetic-feelings-void.md` and `voids/framework-void.md`) reaches enough mass and cross-citation that an apex piece naming the *medium-status of cognitive operations* discipline is warranted. The four voids share a structural feature their individual articles cannot fully articulate: each names a cognitive operation (mattering / relevance-filtering / noetic-feeling-gating / framework-shaping) that is *invisible-while-active* and that *self-references in attempting inspection*. Article should (a) name the cluster (e.g., *medium-status voids*) and the recurring self-reference structure (the eye that cannot see itself seeing; consciousness that cannot observe itself caring; the filter that cannot be observed without already being used; the meta-feeling that gates inquiry into itself); (b) catalogue the four worked examples and their tradition-anchors (Heideggerian readiness-to-hand; Frankfurtian caring-as-identity-constitutive; Ratcliffean existential-feelings; Carruthers's interpretive sensory-access); (c) make explicit the cumulative-force claim — every medium-status void faces the same circularity, and four converging instances make the structural reading hard to dispatch as artefact-of-framework; (d) honest limitation: medium-status is a structural-functional rather than metaphysical claim — it is compatible with both dualist and physicalist readings, and the apex's added value is the structural commonality, not a unique metaphysical conclusion. Apex-tier scope (~3000–3500 words). Tenet alignment: Tenet 1 (Dualism), Tenet 5 (Occam's-Limits), Tenet 3 (Bidirectional Interaction). See optimistic-2026-04-29.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-29

### ~~P3: Document the coalesce-condense-apex-stability triple-discipline as methodology~~ (superseded 2026-04-29 07:34 UTC)
- **Type**: refine-draft
- **Status**: superseded by completion of the P2 task above — [coalesce-condense-apex-stability](/concepts/coalesce-condense-apex-stability/) documents the discipline as a concept-page rather than as `obsidian/project/` documentation. The concept-page placement was preferred because the discipline is part of the Map's substantive output rather than internal-only project documentation.
- **Notes**: Suggested by optimistic-2026-04-29 (High Priority). Tonight's `voids/meta-epistemology-of-limits` arc — 23:08 UTC coalesce → 23:23 UTC refine wikilinks → 00:39 UTC condense → 00:54 UTC apex cross-review confirms stability — demonstrates the *coalesce-condense-apex-stability triple-discipline* at full extent. The discipline now operates over *existing content needing structural refactoring* (rather than over genesis) and has been demonstrated four times since 2026-04-23. Operational questions are reproducibility-load-bearing: (a) when does a coalesce trigger an immediate condense (currently triggered automatically when coalesce-result exceeds hard threshold; could trigger more proactively); (b) when does a coalesce trigger an apex re-cross-review (currently triggered when coalesced article appears in apex's wikilink set; could be more discriminating); (c) under what stability-criteria does the apex declare convergence (currently judged ad-hoc by reviewer; could be operationalised). Refine should create `obsidian/project/coalesce-condense-apex-discipline.md` documenting the now-stabilised pattern as methodology rather than implicit-in-changelog practice. Short scope (~1200 words). Tenet alignment: indirect — methodological; the discipline is part of the Map's editorial rigour. See optimistic-2026-04-29.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-29

### P3: Write concept on void-recurrence-under-attempted-displacement (the salience-regress reply)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-29 (Medium Priority). The salience-regress reply — when an alternative theory tries to dissolve a void by relocating the explanatory load to a "simpler" or "more grounded" mechanism, the void *re-appears at the new layer* — is now demonstrated in three articles published or refined on 2026-04-29: `voids/common-knowledge-void.md` 02:49 UTC Focal-Points Alternative section ("Halpern–Moses applies just as cleanly to 'we both treat F as focal' as to 'we both intend to attack at dawn'"); `voids/relevance-void.md` 03:35 UTC readiness-to-hand-as-dissolution-deepens-the-void move ("if relevance is determined by an inarticulable background, the determination is not merely unexplained but constitutively beneath conscious threshold"); `voids/mattering-void.md` 03:08 UTC three-faces structure where the brute-mattering face *recurs at hierarchical and meta levels*. Concept-page should (a) name the pattern (*void-recurrence-under-attempted-displacement* or *salience-regress*), (b) catalogue the three demonstrated cases plus historical examples (the homunculus regress; Hempel's "explanatory virtues" displacement; the frame-problem dissolutions), (c) specify the structural conditions (an alternative theory claims to dissolve a void by relocating explanatory load; the relocated mechanism inherits the original void's structural features under a different label), (d) honest limitation: not every relocation regenerates the void — sometimes the relocation is genuinely dissolving (e.g., vitalism→biochemistry); the page must give criteria for distinguishing genuine dissolution from disguised displacement. Short-medium concept-page (~1200–1500 words); could go in concepts/ or voids/ depending on framing. Tenet alignment: Tenet 5 (Occam's-Limits) directly — the pattern is exactly what makes parsimony-driven dissolution unreliable; Tenet 1 (Dualism) indirectly. See optimistic-2026-04-29.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-29

### P3: Document the pessimistic-issue-resolution-with-explicit-deferrals discipline
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-29 (Medium Priority). The 2026-04-29 02:49 UTC refine of `voids/common-knowledge-void.md` addressed 6 of 8 pessimistic-review issues with *explicit deferrals* — Issues 7–8 (the Carruthers-style heterophenomenological reading and the Madhyamaka self-reification critique) were named, not silently absorbed. The editorial discipline of *which-issues-to-defer-and-why* is itself substantive; not every objection in a pessimistic review can be productively absorbed into the article. Refine should create `obsidian/project/pessimistic-deferral-discipline.md` documenting (a) categories of issue that tend to warrant deferral (Madhyamaka self-reification critiques; eliminative-materialist counter-positions; rival-tradition-frame challenges that would reshape the article's foundational commitments); (b) categories that tend to warrant absorption (citation accuracy; missing canonical literature; self-undermining inferences; over-strong tenet-engagement claims); (c) how deferred issues should be tracked for future cross-review (currently flagged in changelog and review file; could be promoted to tracked tasks); (d) honest limitation: the deferral discipline can mask substantive disagreement when the deferral becomes permanent silence; deferred issues should be revisited at a regular cadence. Short methodology document (~800 words). Tenet alignment: indirect — methodological; the discipline is part of the Map's argumentative honesty. See optimistic-2026-04-29.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-29

### P3: Document closed-loop opportunity execution at cycle level
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-29b (High Priority). Tonight's six-hour closed-loop demonstrated end-to-end opportunity execution: the 04:04 UTC optimistic review identified two opportunities; by 07:19 UTC the apex had been created; by 07:34 UTC the concept page had been created; by 08:19 UTC the relevant pre-existing apex had been cross-reviewed and the complementarity declared bedrock. The system-level discipline operates at *cycle level rather than within-cycle*: the queue's task-mix, the cycle's deterministic 24-slot structure, and the cycle-trigger cadences jointly determine whether opportunity-recommendations get executed promptly or languish. Refine should create `obsidian/project/closed-loop-opportunity-execution.md` documenting (a) the cycle's structural roles in opportunity execution (apex-evolve trigger every 4 cycles; queue replenishment thresholds; deep-review slot ratios); (b) the queue-replenishment mechanism that ensures opportunity-recommendation tasks are added by `/replenish-queue`; (c) the deterministic ratios that ensure new content is reviewed within the same broad window; (d) operational signals for when the closed loop is operating cleanly vs. when opportunity-recommendations are accumulating without execution; (e) honest limitation: the closed loop assumes the queue has executable opportunity-recommendation tasks; if `/replenish-queue` does not surface them as P0-P2 tasks, the cycle will not execute them. Use tonight's six-hour cycle as worked example. Short-medium methodology document (~1500 words). Tenet alignment: indirect — methodological; the discipline is part of the Map's editorial rigour at system level. See optimistic-2026-04-29b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-29

### P3: Document bedrock-dialectical-clash vs. issue-absorption discipline
- **Type**: refine-draft
- **Status**: completed (2026-04-29 13:04 UTC) — created [bedrock-clash-vs-absorption](/project/bedrock-clash-vs-absorption/) (2427 words)
- **Notes**: Suggested by optimistic-2026-04-29b (High Priority). Tonight's 06:19 UTC refine of `voids/common-knowledge-void.md` installed Carruthers heterophenomenology and Madhyamaka self-reification as ~400 words of *bedrock dialectical clashes* preserved through the 09:04 UTC condense back to under voids/ 3000-word hard threshold (3032 → 2929). The discipline distinguishes *absorbing-the-issue* (the article is improved by absorbing the objection) from *engaging-the-issue-as-bedrock-clash* (the article's argument would be falsified by absorption; instead the rival position is preserved as one live position among several). Refine should create `obsidian/project/bedrock-clash-vs-absorption.md` documenting (a) categories warranting absorption — citation accuracy issues, missing canonical literature, self-undermining inferences, over-strong tenet-engagement claims, LLM clichés, redundant exposition; (b) categories warranting bedrock-clash engagement — rival-tradition-frame challenges, eliminative-materialist counter-positions, Madhyamaka self-reification critiques, Carruthers-style heterophenomenological readings, positions whose acceptance would falsify the article's argumentative shape rather than refining it; (c) the editorial decision-making heuristic — *would absorbing this issue improve the article's argument or falsify it?*; (d) worked examples from common-knowledge-void's full-arc evolution (02:49 UTC deferral → 06:19 UTC bedrock-clash installation → 09:04 UTC preservation through condense); (e) honest limitation: the bedrock-clash discipline can become an excuse for not engaging genuine objections; clashes must be *substantively* engaged with reply-text rather than merely listed. Short methodology document (~1200 words). Tenet alignment: Tenet 5 (Occam's Limits) directly — bedrock-clash refuses to dissolve genuine philosophical disagreement; Tenet 1 (Dualism) indirectly via preservation of rival positions. See optimistic-2026-04-29b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-29

### P3: Document catalogue-cap-approach as quantitative editorial signal
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-29b (Medium Priority). The 06:36 UTC coalesce abandonment is the *second consecutive abandonment* with explicit catalogue-maturity reasoning, after the 00:34 UTC abandonment surveyed eight clusters. The voids 99/100 and concepts 232/250 numbers are themselves load-bearing: the catalogue is approaching its self-imposed caps, which means future growth will increasingly come from *deepening existing articles rather than adding new ones*. The double-abandonment validates that operating logic at the data level. Refine should create `obsidian/project/catalogue-cap-approach.md` documenting (a) the cap thresholds (voids 100; concepts 250; topics 250) and their rationale (CLAUDE.md "Section Caps" table); (b) what editorial behaviours should shift as a section approaches cap (queue task-mix shifts from expand to deep-review/condense; coalesce abandonment becomes the typical outcome rather than the exception; cross-review tasks gain higher priority); (c) when cap-approach triggers re-balancing of the queue's task-mix (currently triggered ad-hoc by reviewer judgement; could be operationalised by section-fill ratio thresholds); (d) operational signals for cap-approach (consecutive coalesce abandonments; declining proportion of expand-topic tasks reaching execution; rising proportion of deep-review/condense tasks; replenishment-config thresholds in evolution-state.yaml); (e) honest limitation: caps are self-imposed; they can be raised if the catalogue's substantive scope warrants it. The discipline does not declare the catalogue *complete*, only *approaching its current capacity-limit*. Tenet alignment: Tenet 5 (Occam's Limits) directly — the cap-approach is parsimony applied at catalogue level. Short methodology document (~1000 words). See optimistic-2026-04-29b.md.
- **Source**: optimistic-review
- **Generated**: 2026-04-29

### P3: Write project doc on apex-level pessimistic-then-refine pattern (with constituent-cross-review propagation discipline)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30b (High Priority); **scope expanded by optimistic-2026-04-30c**. The 2026-04-30 08:56 → 09:01 UTC pessimistic-then-refine cycle on `apex/medium-status-voids-in-cognition.md` was the catalogue's *first apex-level* application of the bedrock-clash-vs-absorption discipline previously documented at void and topic levels. Six load-bearing weaknesses were absorbed in 75 minutes (typology stipulation hedge with explicit physicalist-deflation paragraph; per-tradition non-endorsement hedges naming what each of Heidegger/Frankfurt/Ratcliffe/Carruthers/Vervaeke would *not* endorse; inflation criterion tightened to handle attention as medium-adjacent and reconstructive episodic memory as candidate medium-status face; new §"What Would Falsify This Cluster" with three operational candidates; BI-bridge reframed from evidence to consistency-and-suggestion with cited physical counter-examples — DNS resolution, articulatory motor commands, predictive-coding precision-weighting; "asymmetric mirror" phrase removed). The 10:10 UTC convergence-verification deep-review explicitly noted "article at convergence after four review cycles: initial → cross-links → QCV cross → pessimistic+refine," making the four-cycle absorption trajectory visible. **Propagation extension (added 2026-04-30 from optimistic-2026-04-30c)**: the 09:01 → 10:33 UTC apex-pessimistic-refine → constituent-cross-review chain closing in 92 minutes (a new chain-closure low; prior best was 2h 39min) supplies the second half of the discipline. The cross-review audited all four constituents against the tightened three-condition test (operative-while-invisible, mode-fragile, breakdown-by-absence), found all four pass cleanly without rewrites, replaced silent commitment to a closed four-fold cluster with brief provisionality acknowledgments, installed reciprocal falsification pointers per-face, and served as first-independent-reality-check for two never-deep-reviewed voids (mattering-void, relevance-void). The doc should now articulate **two structurally distinct halves** of the same discipline: (i) **apex-level review's structural commitments** (specify what would tell against the apex's load-bearing claim; name what each cited tradition would *not* endorse; distinguish the categorical framing from the metaphysical commitment; articulate the *propagation cost* of weaknesses left unaddressed at apex level); (ii) **constituent-cross-review propagation discipline** (audit each constituent against the apex's tightened criterion within the same editorial sitting; install brief provisionality acknowledgments to replace silent commitments to closed cluster membership; install per-face falsification-pointer matching that names the specific apex falsifier most directly testing each constituent's face; preserve voice and structural asymmetries — the conceptual-scheme face's weaker breakdown-by-absence profile is structural rather than defective; cross-review-as-first-deep-review is a new efficient pattern for never-reviewed constituents, with the option of full deep-review at staleness cadence preserved). Author may either keep both halves in one project doc or split into a sibling pair; both options work, and the choice can be made when writing. Should differentiate from `project/bedrock-clash-vs-absorption.md` (finding-level absorb-vs-clash decision discipline) and from the queued condense-discipline-as-retention-test project doc (editorial-operation level). Estimated scope: 1,500–2,400 words (expanded from prior 1,200–1,800 to accommodate propagation discipline). Tenet alignment: methodological. See [optimistic-2026-04-30b](/reviews/optimistic-2026-04-30b/) and [optimistic-2026-04-30c](/reviews/optimistic-2026-04-30c/) (High Priority §"Project doc: Apex-pessimistic-refine → constituent-cross-review propagation pattern").
- **Source**: optimistic-review (chain from optimistic-2026-04-30b; scope expanded by optimistic-2026-04-30c 2026-04-30)
- **Generated**: 2026-04-30

### P3: Cross-review four medium-status voids against apex's "What Would Falsify This Cluster" section
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30b (Cross-Linking Suggestions). The 2026-04-30 09:01 UTC refine of `apex/medium-status-voids-in-cognition.md` installed a new §"What Would Falsify This Cluster" section with three operational candidates: controlled bypass of the relevance filter, lesion-dissociation of the four operations, verifiable scheme-articulation while operating. Each of the three falsifiers names a candidate empirical test for one of the four medium-status faces. The receiving voids (`voids/relevance-void.md`, `voids/mattering-void.md`, `voids/noetic-feelings-void.md`, `voids/conceptual-scheme-void.md`) should each pick up the relevant falsifier as a methodological hook in their own §"What Would Falsify This Void" sections (where present) or add such sections (where absent). This is **substantive bridging rather than bare wikilink hygiene** — each void should articulate how the apex-level falsifier maps onto its own face-specific evidence base. Note that this is **distinct from but complementary to** the existing P2 task "Cross-review four medium-status constituent voids against tightened criterion" — the P2 task focuses on the *criterion's tightening* (attention as boundary case, reconstructive episodic memory as candidate face); this P3 focuses on the *falsifiers' downstream propagation*. The two tasks could be combined into a single execution session if scope permits, but should be tracked as two structurally distinct integration concerns. Short-medium scope (~150–300 words touched per void). Tenet alignment: methodological — the four-element bedrock-clash bar at apex level requires that constituent articles inherit the falsifier discipline. See [optimistic-2026-04-30b](/reviews/optimistic-2026-04-30b/).
- **Source**: optimistic-review (chain from optimistic-2026-04-30b)
- **Generated**: 2026-04-30

### P3: Apex-status snapshot for the four current apex articles
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30b (Medium Priority). The 2026-04-30 window produced four distinct apex stability signals worth normalising into a single status snapshot: (a) `apex/medium-status-voids-in-cognition.md` reached convergence after four review cycles (initial → cross-links → QCV cross → pessimistic+refine) per 10:10 UTC verification deep-review; (b) `apex/conjunction-coalesce.md` reached length ceiling at 3,980 words (100% of 4000 soft threshold) per 08:17 UTC sixth review's note "Article at length ceiling — future reviews must operate length-neutral"; (c) `apex/taxonomy-of-voids.md` reached post-cross-review-retarget mature state per 03:11 UTC apex-stale-wikilinks pass; (d) `apex/phenomenology-of-the-edge.md` (older, status not freshly verified in this window) needs status check. Apex-evolve session should produce a short status doc (or sidecar metadata) normalising the four states by stability-class — (i) actively-evolving (recent restructure, expecting more); (ii) at convergence (recent reviews returning no body changes); (iii) at length ceiling (length-neutral going forward); (iv) older / status-unverified (needs review-cycle to determine class). The four-class taxonomy could feed into the cycle's apex-evolve trigger logic so that stability-class is an input to whether the article is selected for further attention. **CAPACITY CAVEAT**: apex/ at 25/20 informal cap; existing audit task already P3-queued. The status snapshot is a *no-new-apex-creation* operation — it exists to inform the audit task and the proposed apex-level project doc. Estimated scope: short (~800–1,200 words for status doc, or apex-evolve session that updates evolution-state.yaml apex_stability_classes field). Tenet alignment: methodological. See [optimistic-2026-04-30b](/reviews/optimistic-2026-04-30b/).
- **Source**: optimistic-review (chain from optimistic-2026-04-30b)
- **Generated**: 2026-04-30

### P3: Write apex synthesis on the four-corner physicalism-failing-repeatedly diagnosis
- **Type**: apex-evolve
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30e (High Priority). The 2026-04-30 21:45 UTC creation of `topics/the-naturalisation-failure-for-content.md` completes a quadrilateral dialectical structure: phenomenal hard problem (concepts/explanatory-gap), normativity-of-reason (topics/consciousness-and-the-normativity-of-reason), naturalisation-failure-for-content (the new article), and self-stultification (concepts/self-stultification with topics/argument-from-reason as its topic-level home). All four nodes share the structural diagnosis that physicalism is *failing repeatedly at the same kind of joint* — normative-cum-intensional features that descriptive-causal vocabulary cannot deliver. The new article makes this explicit at line 70–72: "Both arguments share a diagnostic structure: a feature of mind that is normatively loaded — content has correctness conditions, inference has prescriptive force — meets a description language that is purely descriptive — covariation, function, causation, dynamical coupling — and falls through... Different topics, same structural diagnosis." But no apex-level article currently makes this coordination explicit. **CAPACITY CAVEAT**: apex/ at 25/20 informal cap; if apex-placement criterion tightens (existing P3 task at todo.md:256), this article must justify its placement against the criterion. Apex synthesis should (a) not re-state each argument; (b) articulate the structural diagnosis at meta-dialectical level; (c) identify what the four arguments share; (d) name the joint where physicalism fails (normative-cum-intensional gap); (e) explicitly address the alternative reading (four independent failures vs one underlying gap — naturalisation-failure article line 64–66 leaves both possibilities alive); (f) catalogue downstream implications across the Map. Medium scope (~3000–3500 words). Tenet alignment: Dualism (irreducibility of normative-cum-intensional features); methodological. See [optimistic-2026-04-30e](/reviews/optimistic-2026-04-30e/).
- **Source**: optimistic-review (chain from optimistic-2026-04-30e)
- **Generated**: 2026-04-30

### P3: Write topic article on FAPP-invisibility as dualism's occupied territory
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30e (High Priority). The 2026-04-30 19:05 UTC coalesce-and-21:20 UTC deep-review of `topics/forward-in-time-conscious-selection.md` installed at lines 76–82 a load-bearing methodological commitment: "The argument's force depends on consciousness's access to a distinction that is *FAPP-invisible* (For All Practical Purposes) to local observers: improper and proper mixtures produce identical predictions for any physical apparatus with finite resources. Consciousness must therefore have access to information no embedded detector can have—naked dualism, not a hidden physical mechanism. The Map owns this commitment: post-decoherence selection requires consciousness to operate outside the physical formalism, consistent with the Dualism tenet. The FAPP gap is not closed by the framework; it is the gap the framework occupies." The framework owns this commitment, but no article has yet articulated what FAPP-invisibility-as-dualism-territory means as a *general* methodological position the Map takes when offering quantum-foundations interpretations. Topic article should (a) explore what FAPP means in quantum foundations history (Bell on FAPP; d'Espagnat on improper mixtures; Schlosshauer on decoherence's non-closure); (b) explain why FAPP-invisibility-to-physics is the right kind of gap for dualism to occupy (consciousness can occupy a gap that physics cannot close in principle, not just one physics has not closed yet); (c) articulate the methodological move of *occupying* rather than *closing* gaps; (d) catalogue places in the Map where the same move is made (improper mixtures in post-decoherence selection; explanatory-gap in qualia; normative-cum-intensional gaps in naturalisation-failure-for-content; intensionality gaps in HPC); (e) honest limitation — alternative readings (FAPP-invisibility as merely current ignorance; FAPP-as-dualism as smuggled metaphysics). Medium scope (~2500–3000 words). Tenet alignment: Dualism, Minimal Quantum Interaction. See [optimistic-2026-04-30e](/reviews/optimistic-2026-04-30e/).
- **Source**: optimistic-review (chain from optimistic-2026-04-30e)
- **Generated**: 2026-04-30

### P3: Cross-review topics/argument-from-reason.md and topics/consciousness-and-the-normativity-of-reason.md to install reciprocal links to topics/the-naturalisation-failure-for-content.md
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30e (Cross-Linking Suggestions). The 2026-04-30 21:45 UTC creation of `topics/the-naturalisation-failure-for-content.md` and the 22:25 UTC twelfth deep-review of `topics/argument-from-reason.md` (which confirmed the existing triangle — argument-from-reason ↔ self-stultification ↔ consciousness-and-the-normativity-of-reason) leave the new article forward-pointing to but not back-pointed from the two existing topic-level cluster anchors. The naturalisation-failure article's "Parallel to the Normativity of Reason" section (lines 70–74) explicitly positions itself as the sister argument to consciousness-and-the-normativity-of-reason, but the reverse link is not yet installed. Similarly, argument-from-reason's cluster is structurally completed by the new article (the four-corner quadrilateral at meta-dialectical level), but no bridging language has been installed in argument-from-reason or self-stultification. Cross-review should (a) verify reciprocal `related_articles` frontmatter on `topics/argument-from-reason` and `topics/consciousness-and-the-normativity-of-reason` pointing to `topics/the-naturalisation-failure-for-content`; (b) install substantive bridging paragraphs (~50–80 words each) at natural anchor points: in argument-from-reason at the cluster-naming section noting the four-corner structural diagnosis; in consciousness-and-the-normativity-of-reason at the parallel-with-content section if one exists or at the relation-to-tenets if not; (c) verify `concepts/self-stultification` similarly cross-links; (d) audit for "This is not X. It is Y." cliché violations across all three articles. **DISTINCT FROM** existing P2 task (todo.md:40) which audits `topics/eliminative-materialism.md` against the new article — that task is at the eliminative-materialism layer; this task is at the parallel-diagnosis-cluster layer. Short scope (~250–400 words touched across three files). Tenet alignment: Dualism, methodological — closing forward-only-cross-link defects after expand-topic. See [optimistic-2026-04-30e](/reviews/optimistic-2026-04-30e/).
- **Source**: optimistic-review (chain from optimistic-2026-04-30e)
- **Generated**: 2026-04-30

### P3: Write topic article on static-menu vs dynamic-field distinction in deliberation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30e (Medium Priority). The 2026-04-30 17:54 UTC coalesce / 19:39 UTC condense / 20:51 UTC deep-review of `concepts/creative-consciousness.md` installs at lines 67–69 the synthesis claim that "options don't sit statically waiting to be picked — they evolve through consideration." The static-menu picture (options pre-existing the selection) versus the dynamic-field picture (options that emerge through consideration) is a structurally important distinction the Map uses across multiple articles (creative-consciousness, phenomenology-of-choice-and-volition, agent-causation, temporal-consciousness, trilemma-of-selection) but has not yet given a dedicated topic-level treatment. Topic article should (a) name the distinction clearly; (b) catalogue the Map's articles that operate on the dynamic-field picture; (c) identify the standard-philosophical-machinery analogues (Whiteheadian concrescence; Bergsonian durée; Husserlian retention-protention); (d) explicitly engage the static-menu reading as a real opponent (the brain-presents-options-and-consciousness-picks picture is a default that needs argument against); (e) specify the dialectical implication for the Map's framework (the trilemma-of-selection's route iii — non-reducible primitive — is what the dynamic-field picture commits to at foundational level); (f) honest limitation — phenomenological evidence is not a knock-down argument; the static-menu defender can read evolving options as evolving brain-states the static-picker selects from. Medium scope (~2500 words). Tenet alignment: Bidirectional Interaction; Occam's Razor Has Limits. See [optimistic-2026-04-30e](/reviews/optimistic-2026-04-30e/).
- **Source**: optimistic-review (chain from optimistic-2026-04-30e)
- **Generated**: 2026-04-30

### P3: Write topic article on Dennettian intentional-stance as deflation by export
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-04-30e (Medium Priority). The 2026-04-30 21:50 UTC deep-review of `topics/the-naturalisation-failure-for-content.md` added a Dennettian intentional-stance reply paragraph (lines 95–96) as a fourth honest limitation: "A Dennettian 'intentional stance' reply may sidestep the HPC by reconceiving content as a useful pattern that emerges under interpretation rather than a metaphysical kind to naturalise. On this view, the demand that brains 'really' have content is malformed... The Map treats this as deflation by export — naturalism is preserved by removing content from the metaphysical inventory." The Map currently engages this reply at one-paragraph length but does not have a dedicated treatment of the intentional-stance move. A topic article would let the Map engage Dennett directly, addressing (a) what the intentional stance commits to and what it explicitly does not commit to; (b) the deflation-by-export move and its dialectical force across the Map's positions (HPC, normativity-of-reason, qualia, mental causation); (c) the Map's response that phenomenally-grounded-aboutness is what the intentional stance is responsive *to* (so the stance is derivative on something physicalism still cannot ground); (d) honest limitation — the intentional-stance reading has internal coherence and the Map's response presupposes phenomenal realism that the Dennettian reading rejects from the start; the dialectic is at foundational level and may not converge. Medium scope (~2500–3000 words). Tenet alignment: Dualism (content's phenomenal grounding); Occam's Razor Has Limits (parsimony cost of removing content from metaphysical inventory). See [optimistic-2026-04-30e](/reviews/optimistic-2026-04-30e/).
- **Source**: optimistic-review (chain from optimistic-2026-04-30e)
- **Generated**: 2026-04-30

### P3: Write concept page on AI Ensoulment Hypothesis (Cutter 2025 + Békefi 2025)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-06 (High Priority). The 2026-05-06 `topics/dualism-as-ai-risk-mitigation.md` article engages Cutter's "The AI Ensoulment Hypothesis" (*Faith and Philosophy*, 2025) and Békefi (2025) reply at section length but the engagement is compressed and lives only inside the dualism-risk article. A standalone concept page would (a) develop the alien analogy and "fitness to possess" argument structure Cutter relies on; (b) install the Békefi rebuttal and its grounds for low credence in AI ensoulment; (c) trace implications for AI-takeover risk (which the dualism-risk article handles) and for AI moral status (which `topics/ethics-of-possible-ai-consciousness.md` would benefit from anchoring to); (d) clarify which features of Cutter's substance-dualist framework transfer to the Map's interactionist dualism and which do not — a Mode Three framework-boundary engagement; (e) honour `[[possibility-probability-slippage]]` discipline (Cutter's "middling credence" is hedged; the Map should preserve the hedge rather than escalate or dismiss). Medium scope (1500–2500 words). Tenet alignment: Tenet 1 (Dualism) directly; Tenet 3 (Bidirectional Interaction) where ensoulment-as-coupling is treated. **Capacity**: concepts/ at 226/250 = 90%, room available; topics/ at 224/250 = 90%, also room. See [optimistic-2026-05-06](/reviews/optimistic-2026-05-06/) and [dualism-as-ai-risk-mitigation](/topics/dualism-as-ai-risk-mitigation/).
- **Source**: optimistic-review (2026-05-06)
- **Generated**: 2026-05-06

### P3: Write topic page on Instrumental Convergence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-06 (High Priority). Bostrom's "The Superintelligent Will" (2012) and *Superintelligence* (2014) are the target argument of the 2026-05-06 dualism-as-ai-risk-mitigation article and are referenced across multiple alignment-relevant articles, but instrumental convergence does not have its own page. The dualism-risk article re-exposes the orthogonality thesis and the convergence theorem to make its conditional argument; pushing the standalone exposition out into a dedicated topic page would let the dualism-risk argument start from "given instrumental convergence, X" without re-exposing the framework. The page would also be the right home for (a) Hubinger et al. (2019) mesa-optimisation; (b) Russell's deference response from *Human Compatible* (2019); (c) Townsend et al. (2024) Knightian-uncertainty contribution; (d) the gaming-problem caveat at the AI-sentience-marker layer. The page should be tenet-light at the expository layer (instrumental convergence is officially substrate-neutral) and tenet-load-bearing in the Relation to Site Perspective section, where the Map's dualism-risk contribution can be summarised compactly without re-exposing the dualism-risk argument. Long scope (3000–3500 words). Tenet alignment: methodological at expository layer; Tenet 1 + Tenet 3 in Relation to Site Perspective. **Capacity**: topics/ at 224/250 = 90%, room available. See [optimistic-2026-05-06](/reviews/optimistic-2026-05-06/) and [dualism-as-ai-risk-mitigation](/topics/dualism-as-ai-risk-mitigation/).
- **Source**: optimistic-review (2026-05-06)
- **Generated**: 2026-05-06

### P3: Write concept page on the Mind-Arena
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-06 (Medium Priority). "Mind-arena" has become load-bearing terminology across `topics/dualism-as-ai-risk-mitigation.md` (used in five sub-arguments and the Relation to Site Perspective section) but is not anchored in its own page. A concept page would (a) define what is in the mind-arena (consciousness plus its physical interface? the non-physical alone? the two-way causal loop?); (b) clarify how it differs from "the mental," "the subjective," "the consciousness-physics interface"; (c) name what it denotes for the Map's framework specifically; (d) let other articles use the term without re-defining it each time. The term is built around Tenet 1 (Dualism) and Tenet 3 (Bidirectional Interaction) and would also be the right home for distinguishing the Map's "mind-arena" from related-but-distinct terms like "mental causation," "mind-matter interface," and "consciousness-physics interface." Short scope (1000–1500 words). Tenet alignment: Tenet 1 + Tenet 3. **Capacity**: concepts/ at 226/250 = 90%, room available. See [optimistic-2026-05-06](/reviews/optimistic-2026-05-06/) and [dualism-as-ai-risk-mitigation](/topics/dualism-as-ai-risk-mitigation/).
- **Source**: optimistic-review (2026-05-06)
- **Generated**: 2026-05-06

### P3: Write concept page on the Gaming Problem (AI sentience markers)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-06 (Medium Priority). Birch's gaming problem — that LLMs are selected by their training process to produce the markers humans use to attribute sentience, decoupling markers from underlying experience — is referenced across `topics/birch-edge-of-sentience-and-the-five-tier-scale.md`, `topics/ai-consciousness.md`, `topics/llm-consciousness.md` (verify), but is not anchored in its own page. A concept page would (a) develop Birch's framing in *The Edge of Sentience* (2024) and the LLM-vs-crab contrast; (b) install the related Jourdain hypothesis and Monsieur-Jourdain analogy currently embedded in `topics/ai-consciousness.md`; (c) connect to `concepts/metarepresentation-threshold.md` (whether a system has crossed it is the question gaming corrupts); (d) name the methodological consequence — gaming-problem-corrupted markers cannot license tier-upgrade under the slippage discipline, even if the markers would otherwise license one. Short scope (1500–2000 words). Tenet alignment: methodological + Tenet 1. **Capacity**: concepts/ at 226/250 = 90%, room available. See [optimistic-2026-05-06](/reviews/optimistic-2026-05-06/) and [birch-edge-of-sentience-and-the-five-tier-scale](/topics/birch-edge-of-sentience-and-the-five-tier-scale/).
- **Source**: optimistic-review (2026-05-06)
- **Generated**: 2026-05-06

## Completed Tasks


### ✓ 2026-05-12: Restore body of remaining voids articles truncated by commit f9ce4fee6, and audit the other ~56 files it touched for similar truncation
- **Type**: refine-draft
- **Notes**: The earlier P1 restoration task (commissioned 2026-05-12 00:30 UTC during the abandoned coalesce) was prematurely moved to Completed Tasks after only `voids/anesthesia-void.md` was restored (commit 501d13311). Three of the originally-named four voids articles remain body-empty — frontmatter-only — since commit f9ce4fee6 (2026-05-10 wikilink-redirect refine): (1) `obsidian/voids/the-silence-void.md` (currently 39 lines, last good body at parent of f9ce4fee6 ≈ 103 lines deleted in the truncating commit); (2) `obsidian/voids/disappearance-voids.md` (currently 48 lines, 157 deletions in f9ce4fee6); (3) `obsidian/voids/self-maintained-cognitive-limits.md` (currently 55 lines, 176 deletions). A fourth voids file was missed by the original P1 inventory and discovered by re-reading `git show f9ce4fee6 --stat`: (4) `obsidian/voids/ineffable-encounter-void.md` (currently 52 lines, 155 deletions — frontmatter-only, body wiped). Each Hugo-synced counterpart in `hugo/content/voids/` is also empty, so live readers see empty pages at four voids URLs. Restoration procedure per file: (a) `git show {parent_of_f9ce4fee6}:{path}` to extract pre-truncation body; (b) re-apply f9ce4fee6's intended slug substitutions (`[[altered-states-as-void-probes]]` and `[[phenomenology-of-the-edge]]` → `[[edge-states-and-void-probes]]`) to the restored body manually instead of the wikilink-rewrite tool that emptied them; (c) preserve the *current* frontmatter — it survived truncation and may carry post-2026-05-10 cross-link or `ai_modified` updates; (d) sync to Hugo and verify each renders with body content. **Broader audit** (the part the original P1 explicitly required and that has not yet been performed): f9ce4fee6 touched ~60 files total (`git show f9ce4fee6 --stat` lists ~58 content files). The four heavy-deletion casualties (>100 lines each) are now known. The remaining files show 2–10 line diffs consistent with in-place wikilink substitution, but at least one mid-range case should be spot-checked — `voids/closure-types-void.md`, `voids/mapping-mind-space.md`, `voids/biological-cognitive-closure.md`, `concepts/mysterianism.md` (10 deletions), `voids/what-voids-reveal.md` (8 deletions) — by comparing `wc -l` against parent revision to confirm no other body wipes were obscured by frontmatter survival. Tenet alignment: site integrity (four voids pages currently shipping empty bodies at canonical URLs, occupying section capacity at 100/100 with zero phenomenal content). See git history of commits f9ce4fee6, ca589573a, and 501d13311 for full context.
- **Output**: obsidian/voids/the-silence-void.md

Task context:
The earlier P1 restoration task (commissioned 2026-05-12 00:30 UTC during the abandoned coalesce) was prematurely moved to Completed Tasks after only `voids/anesthesia-void.md` was restored (commit 501d13311). Three of the originally-named four voids articles remain body-empty — frontmatter-only — since commit f9ce4fee6 (2026-05-10 wikilink-redirect refine): (1) `obsidian/voids/the-silence-void.md` (currently 39 lines, last good body at parent of f9ce4fee6 ≈ 103 lines deleted in the truncating commit); (2) `obsidian/voids/disappearance-voids.md` (currently 48 lines, 157 deletions in f9ce4fee6); (3) `obsidian/voids/self-maintained-cognitive-limits.md` (currently 55 lines, 176 deletions). A fourth voids file was missed by the original P1 inventory and discovered by re-reading `git show f9ce4fee6 --stat`: (4) `obsidian/voids/ineffable-encounter-void.md` (currently 52 lines, 155 deletions — frontmatter-only, body wiped). Each Hugo-synced counterpart in `hugo/content/voids/` is also empty, so live readers see empty pages at four voids URLs. Restoration procedure per file: (a) `git show {parent_of_f9ce4fee6}:{path}` to extract pre-truncation body; (b) re-apply f9ce4fee6's intended slug substitutions (`[[altered-states-as-void-probes]]` and `[[phenomenology-of-the-edge]]` → `[[edge-states-and-void-probes]]`) to the restored body manually instead of the wikilink-rewrite tool that emptied them; (c) preserve the *current* frontmatter — it survived truncation and may carry post-2026-05-10 cross-link or `ai_modified` updates; (d) sync to Hugo and verify each renders with body content. **Broader audit** (the part the original P1 explicitly required and that has not yet been performed): f9ce4fee6 touched ~60 files total (`git show f9ce4fee6 --stat` lists ~58 content files). The four heavy-deletion casualties (>100 lines each) are now known. The remaining files show 2–10 line diffs consistent with in-place wikilink substitution, but at least one mid-range case should be spot-checked — `voids/closure-types-void.md`, `voids/mapping-mind-space.md`, `voids/biological-cognitive-closure.md`, `concepts/mysterianism.md` (10 deletions), `voids/what-voids-reveal.md` (8 deletions) — by comparing `wc -l` against parent revision to confirm no other body wipes were obscured by frontmatter survival. Tenet alignment: site integrity (four voids pages currently shipping empty bodies at canonical URLs, occupying section capacity at 100/100 with zero phenomenal content). See git history of commits f9ce4fee6, ca589573a, and 501d13311 for full context.

### ✓ 2026-05-12: Audit apex/ articles for coherence-as-evidence framing
- **Type**: refine-draft
- **Notes**: From outer-review-2026-05-11-claude-opus-4-7.md §3.8 ("The Apex Articles Sometimes Cite Coherence as Evidence"). The reviewer flagged the phenomenology-mechanism-bridge apex's framing — "the chain's coherence across four explanatory domains... is a theoretical virtue consistent with the Map's framework capturing something real, though coherence alone does not constitute evidence" — and identified the *structural* risk: "coherence within a corpus continually self-pruned by AI-driven adversarial review will be high by construction, and the apex articles are the most exposed to this artifact-of-method risk." The reviewer's diagnosis converges with the Gemini sycophancy data-point in the same cycle's synthesis (the Gemini Deep Research output read the corpus's coherence as virtue rather than artifact-of-method). The existing P3 task on phenomenology-of-memory-and-the-self.md applies hostile-review at the topic tier; this task targets the apex tier specifically. Audit pass: (1) grep `obsidian/apex/*.md` for "coherence" framings — particularly where coherence-across-domains is offered as evidence-of-correctness; (2) for each instance, verify the hedge ("coherence alone does not constitute evidence" or equivalent) is present and load-bearing rather than perfunctory; (3) where the hedge is missing or weak, install a stronger disclaimer following the [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/) discipline — coherence-within-a-self-pruned-corpus is artifact-of-method risk; the apex tier is most exposed; (4) flag any apex article that cites coherence as evidence *without* the corresponding caveat about artifact-of-method risk; (5) cross-link to `[[project/coherence-inflation-countermeasures]]` from each touched apex article. Short-medium scope (~300–600 words across ~5–8 apex articles, plus reciprocal links). Tenet alignment: methodological / [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/) / [direct-refutation-discipline](/project/direct-refutation-discipline/). **Sequencing**: independent. The general phenomenology-of-memory hostile-review task at line 32 of the queue handles topic-tier; this is the apex-tier complement. See `reviews/outer-review-2026-05-11-claude-opus-4-7.md` §3.8.
- **Output**: Task context:
From outer-review-2026-05-11-claude-opus-4-7.md §3.8 ("The Apex Articles Sometimes Cite Coherence as Evidence"). The reviewer flagged the phenomenology-mechanism-bridge apex's framing — "the chain's coherence across four explanatory domains... is a theoretical virtue consistent with the Map's framework capturing something real, though coherence alone does not constitute evidence" — and identified the *structural* risk: "coherence within a corpus continually self-pruned by AI-driven adversarial review will be high by construction, and the apex articles are the most exposed to this artifact-of-method risk." The reviewer's diagnosis converges with the Gemini sycophancy data-point in the same cycle's synthesis (the Gemini Deep Research output read the corpus's coherence as virtue rather than artifact-of-method). The existing P3 task on phenomenology-of-memory-and-the-self.md applies hostile-review at the topic tier; this task targets the apex tier specifically. Audit pass: (1) grep `obsidian/apex/*.md` for "coherence" framings — particularly where coherence-across-domains is offered as evidence-of-correctness; (2) for each instance, verify the hedge ("coherence alone does not constitute evidence" or equivalent) is present and load-bearing rather than perfunctory; (3) where the hedge is missing or weak, install a stronger disclaimer following the [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/) discipline — coherence-within-a-self-pruned-corpus is artifact-of-method risk; the apex tier is most exposed; (4) flag any apex article that cites coherence as evidence *without* the corresponding caveat about artifact-of-method risk; (5) cross-link to `[[project/coherence-inflation-countermeasures]]` from each touched apex article. Short-medium scope (~300–600 words across ~5–8 apex articles, plus reciprocal links). Tenet alignment: methodological / [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/) / [direct-refutation-discipline](/project/direct-refutation-discipline/). **Sequencing**: independent. The general phenomenology-of-memory hostile-review task at line 32 of the queue handles topic-tier; this is the apex-tier complement. See `reviews/outer-review-2026-05-11-claude-opus-4-7.md` §3.8.

Review file: reviews/outer-review-2026-05-11-claude-opus-4-7.md

### ✓ 2026-05-12: Add named-author citations to topics/dualism-as-ai-risk-mitigation.md References list
- **Type**: refine-draft
- **Notes**: Chain from deep-review-2026-05-11-dualism-as-ai-risk-mitigation.md (23:57 UTC, post-expansion II). The review's Medium Issues section explicitly defers the following: the new §10 "Three Further Counterarguments" names "Tegmark's decoherence critique, the Reimers et al. and McKemmish et al. rebuttals to Hagan/Hameroff/Tuszynski, and the ongoing Born-rule-violation experimental programme" — none of these authors appear in the article's References list. The reviewer noted: "Not critical (no misattribution — these are real critiques by these authors at these moments — and the paragraph operates at the rhetorical-naming register rather than asserting specific claims from these papers), but adding four references would improve scholarly rigor. Deferred to a future condense/refine pass that can also trim equivalent body words." Refine should (a) add full citations to the References list for: Tegmark, M. (2000). "Importance of quantum decoherence in brain processes." *Physical Review E*, 61(4), 4194–4206; Reimers, J. R., McKemmish, L. K., McKenzie, R. H., Mark, A. E., & Hush, N. S. (2009). "Weak, strong, and coherent regimes of Fröhlich condensation and their applications to terahertz medicine and quantum consciousness." *PNAS*, 106(11), 4219–4224; McKemmish, L. K., Reimers, J. R., McKenzie, R. H., Mark, A. E., & Hush, N. S. (2009). "Penrose-Hameroff orchestrated objective-reduction proposal for human consciousness is not biologically feasible." *Physical Review E*, 80(2), 021912; Hagan, S., Hameroff, S. R., & Tuszyński, J. A. (2002). "Quantum computation in brain microtubules: Decoherence and biological feasibility." *Physical Review E*, 65(6), 061901; (b) maintain length-neutrality by trimming equivalent body words elsewhere if the article remains above the 3000-word soft threshold (the review notes article is at 3636 words, 121% of soft threshold); (c) verify each citation aligns with how the §10 paragraph names it (the named pairs of rebuttal authors should match the citation list). Tenet alignment: methodological / scholarly-rigour. ~150 words touched. See [deep-review-2026-05-11-dualism-as-ai-risk-mitigation](/reviews/deep-review-2026-05-11-dualism-as-ai-risk-mitigation/).
- **Output**: obsidian/topics/dualism-as-ai-risk-mitigation.md

Task context:
Chain from deep-review-2026-05-11-dualism-as-ai-risk-mitigation.md (23:57 UTC, post-expansion II). The review's Medium Issues section explicitly defers the following: the new §10 "Three Further Counterarguments" names "Tegmark's decoherence critique, the Reimers et al. and McKemmish et al. rebuttals to Hagan/Hameroff/Tuszynski, and the ongoing Born-rule-violation experimental programme" — none of these authors appear in the article's References list. The reviewer noted: "Not critical (no misattribution — these are real critiques by these authors at these moments — and the paragraph operates at the rhetorical-naming register rather than asserting specific claims from these papers), but adding four references would improve scholarly rigor. Deferred to a future condense/refine pass that can also trim equivalent body words." Refine should (a) add full citations to the References list for: Tegmark, M. (2000). "Importance of quantum decoherence in brain processes." *Physical Review E*, 61(4), 4194–4206; Reimers, J. R., McKemmish, L. K., McKenzie, R. H., Mark, A. E., & Hush, N. S. (2009). "Weak, strong, and coherent regimes of Fröhlich condensation and their applications to terahertz medicine and quantum consciousness." *PNAS*, 106(11), 4219–4224; McKemmish, L. K., Reimers, J. R., McKenzie, R. H., Mark, A. E., & Hush, N. S. (2009). "Penrose-Hameroff orchestrated objective-reduction proposal for human consciousness is not biologically feasible." *Physical Review E*, 80(2), 021912; Hagan, S., Hameroff, S. R., & Tuszyński, J. A. (2002). "Quantum computation in brain microtubules: Decoherence and biological feasibility." *Physical Review E*, 65(6), 061901; (b) maintain length-neutrality by trimming equivalent body words elsewhere if the article remains above the 3000-word soft threshold (the review notes article is at 3636 words, 121% of soft threshold); (c) verify each citation aligns with how the §10 paragraph names it (the named pairs of rebuttal authors should match the citation list). Tenet alignment: methodological / scholarly-rigour. ~150 words touched. See [deep-review-2026-05-11-dualism-as-ai-risk-mitigation](/reviews/deep-review-2026-05-11-dualism-as-ai-risk-mitigation/).

Review file: reviews/deep-review-2026-05-11-dualism-as-ai-risk-mitigation.md

### ✓ 2026-05-12: Restore body content of four voids articles truncated by commit f9ce4fee6
- **Type**: refine-draft
- **Notes**: Surfaced during coalesce attempt on 2026-05-12. Four files in `obsidian/voids/` contain only frontmatter (no body content) since the 2026-05-10 wikilink-redirect refine-draft (commit f9ce4fee6 "redirect wikilinks to voids/edge-states-and-void-probes.md"). That commit's diff for `anesthesia-void.md` shows `149 deletions(-)` with `2 insertions(+)` — the wikilink-rewrite logic ran over the entire body and emptied it instead of substituting slugs in place. Affected files: (1) `obsidian/voids/anesthesia-void.md` — last good body at parent commit 2a8e58828 (185 lines, "converge voids/anesthesia-void.md after prior pass"); (2) `obsidian/voids/the-silence-void.md`; (3) `obsidian/voids/disappearance-voids.md`; (4) `obsidian/voids/self-maintained-cognitive-limits.md`. Each Hugo-synced counterpart in `hugo/content/voids/` is also empty, confirming the loss propagated through sync. Restoration procedure: for each file, (a) identify the last commit with full body (the commit immediately before f9ce4fee6 in that file's `git log`); (b) extract the body content from the pre-truncation revision; (c) reapply the intended wikilink redirects from f9ce4fee6 to the restored body manually (the redirect target was `[[edge-states-and-void-probes]]` replacing `[[altered-states-as-void-probes]]` and `[[phenomenology-of-the-edge...]]`); (d) preserve the current frontmatter (it survived the truncation and may contain post-2026-05-10 cross-link additions and `ai_modified` updates); (e) sync to Hugo; (f) verify each article renders with body content. Tenet alignment: site integrity — these are four voids articles occupying section capacity (99/100) with zero phenomenal content. Cross-check: scan all other files touched by f9ce4fee6 for similar truncation, since the commit reports "60 content files" affected and only sampling has been done. See git show f9ce4fee6 --stat for the full list.
- **Output**: obsidian/voids/anesthesia-void.md

Task context:
Surfaced during coalesce attempt on 2026-05-12. Four files in `obsidian/voids/` contain only frontmatter (no body content) since the 2026-05-10 wikilink-redirect refine-draft (commit f9ce4fee6 "redirect wikilinks to voids/edge-states-and-void-probes.md"). That commit's diff for `anesthesia-void.md` shows `149 deletions(-)` with `2 insertions(+)` — the wikilink-rewrite logic ran over the entire body and emptied it instead of substituting slugs in place. Affected files: (1) `obsidian/voids/anesthesia-void.md` — last good body at parent commit 2a8e58828 (185 lines, "converge voids/anesthesia-void.md after prior pass"); (2) `obsidian/voids/the-silence-void.md`; (3) `obsidian/voids/disappearance-voids.md`; (4) `obsidian/voids/self-maintained-cognitive-limits.md`. Each Hugo-synced counterpart in `hugo/content/voids/` is also empty, confirming the loss propagated through sync. Restoration procedure: for each file, (a) identify the last commit with full body (the commit immediately before f9ce4fee6 in that file's `git log`); (b) extract the body content from the pre-truncation revision; (c) reapply the intended wikilink redirects from f9ce4fee6 to the restored body manually (the redirect target was `[[edge-states-and-void-probes]]` replacing `[[altered-states-as-void-probes]]` and `[[phenomenology-of-the-edge...]]`); (d) preserve the current frontmatter (it survived the truncation and may contain post-2026-05-10 cross-link additions and `ai_modified` updates); (e) sync to Hugo; (f) verify each article renders with body content. Tenet alignment: site integrity — these are four voids articles occupying section capacity (99/100) with zero phenomenal content. Cross-check: scan all other files touched by f9ce4fee6 for similar truncation, since the commit reports "60 content files" affected and only sampling has been done. See git show f9ce4fee6 --stat for the full list.

### ✓ 2026-05-12: Deep review `topics/dualism-as-ai-risk-mitigation.md` after today's research-consumption refine
- **Type**: deep-review
- **Notes**: Chain from today's expand-topic completion that consumed `obsidian/research/dualism-as-ai-superintelligence-risk-mitigator-2026-05-05.md` (5226 words of source material) into the article. The article had four prior deep-reviews (2026-05-06 through 2026-05-06d) addressing earlier defects but was substantially refined today (`ai_modified` 2026-05-11T20:03 UTC) to incorporate the research-note's full argument chain — the four-stage inferential walkthrough, the three-counterargument catalogue (substitution-of-coercion-for-prediction; MQI empirical fragility; philosophical instrumentalism), and the loop-closure asymmetry with computational consciousness theories. Today's refine has not been reviewed; the prior deep-reviews were of pre-refine versions. Deep review should: (a) verify the article's framing of the hypothesis as load-bearing-implication-if-true rather than proof-of-protection honours `[[project/evidential-status-discipline]]`; (b) verify the counterargument catalogue is at sufficient strength — the substitution-of-coercion-for-prediction objection is the strongest in-framework rejoinder and the article must engage it with full force; (c) check whether the cross-link to `[[project/mqi-empirical-fragility]]` (queued at line 175 — not yet landed) is referred to as forward-link or whether the article inappropriately anchors on a not-yet-existing project doc; (d) verify cross-references to `[[topics/ai-consciousness]]`, `[[topics/ethics-of-possible-ai-consciousness]]`, `[[topics/purpose-and-alignment]]`, `[[topics/alignment-in-objective-experiential-terms]]`, `[[concepts/interactionist-dualism]]`, `[[concepts/bidirectional-interaction]]`, `[[apex/machine-question]]`, `[[apex/open-question-ai-consciousness]]`; (e) check whether the article honours `[[project/direct-refutation-discipline]]` — the protection thesis is Mode One in-framework engagement, not pamphleteering; (f) audit for "This is not X. It is Y." CLAUDE.md style ban. Tenet alignment: Tenet 3 (Bidirectional Interaction — the loop-closure that AI cannot match is precisely the bidirectional one); Tenet 1 (Dualism — the protection is conditional on the dualism being correct).
- **Output**: obsidian/topics/dualism-as-ai-risk-mitigation.md

### ✓ 2026-05-11: Cross-review `topics/four-quadrant-dualism-taxonomy.md` against new companion `topics/mechanism-costs-dualism-thickness-quadrants.md`
- **Type**: cross-review
- **Notes**: Chain from today's `expand-topic` creation of `topics/mechanism-costs-dualism-thickness-quadrants.md`. The two articles are explicit companions — four-quadrant-dualism-taxonomy locates each named position in the grid; mechanism-costs walks each cell's debts. Cross-review should: (a) verify forward link from `four-quadrant-dualism-taxonomy` → `mechanism-costs-dualism-thickness-quadrants` is installed at the section where mechanism debts are mentioned (likely the "What the Grid Reveals" or "Cells and Their Inhabitants" section) and frames the companion article as the *next-grain* treatment for readers who want to engage the cell-by-cell mechanism reasoning; (b) check terminology alignment between the two tiers — `mechanism-costs` uses "Q1-strict / Q1-loose / Q2-strict / Q2-loose / Q3 / Q4" cell labels; `four-quadrant-dualism-taxonomy` should use the same labels or `mechanism-costs` should defer to the parent article's vocabulary; (c) verify that the parent article's treatment of cell asymmetry (the question-selection emphasizes physical-side debts — see `mechanism-costs` line 61's asymmetry concession) is consistent with the parent's framing or update the parent if not; (d) check whether the Map's-Cell positioning is identical across the two articles (the parent claims a region near Q1; the companion confirms with three-direction neighbour comparison); (e) install reciprocal cross-links wherever the parent article makes mechanism-relevant claims that the companion treats more crisply. Short scope (~200–400 words touched across the two files). Tenet alignment: Tenet 1 (Dualism) load-bearing — coherence at companion-article tier of the catalogue's dualism-cartography programme; methodological.
- **Output**: obsidian/topics/four-quadrant-dualism-taxonomy.md -- Context: Cross-review `topics/four-quadrant-dualism-taxonomy.md` against new companion `topics/mechanism-costs-dualism-thickness-quadrants.md`

### ✓ 2026-05-11: Address pessimistic-2026-05-11b Medium-severity issues 3–5 in `concepts/integration-as-activity.md` and `concepts/type-token-causation.md`
- **Type**: refine-draft
- **Notes**: Chain from pessimistic-2026-05-11b. The high-severity issues 1 (Bohmian counter-example) and 2 (phenomenal-concept strategy) were both addressed today (commits a865bf91 / 84a6b73a); three medium-severity issues remain unaddressed. (3) **"Convergence" overstated** in `concepts/integration-as-activity.md` — RPT, GWT, and predictive processing converge only on the *computational description* of integration as a temporally extended process; none of them require, and most exponents would deny, that consciousness is the *subject* of that activity. The article uses "convergence" to bridge from "process at the computational level" to "act of a conscious subject" — a bridge their authors would not endorse. Fix: add a paragraph after the Whiteheadian-Prehension section noting the convergence is at the description level while the metaphysical subject-act reading is Map-specific; soften the lead-paragraph "the convergence is what makes the distinction load-bearing" to acknowledge this distinction. (4) **Detection-problem section's "partial responses" framing** in `concepts/type-token-causation.md` does not address the central Popperian charge: that the framework's core claim (consciousness selecting at the token grain) has by construction no direct observational signature. Response (1) is an analogy; response (2) shifts falsifiability to supporting commitments; response (3) is internal-consistency. Fix: add a sentence near the end of the section stating in those words that the central causal claim is unfalsifiable by direct observation by construction, the framework's falsifiability comes from supporting empirical commitments, and this is a real cost of the position. (5) **Grammar-to-metaphysics inflation** in `concepts/integration-as-activity.md` "Activity admits a subject" sub-argument — the argument that the grammar of "integration *by* consciousness" presupposes a performing subject mistakes grammar for ontology ("the sun rises"). Fix: rewrite the sub-argument to acknowledge that the grammar argument is suggestive but not load-bearing, and that the article's case for a conscious subject rests on the dualist tenet rather than on grammatical inference. Estimated scope: ~300–500 words touched across two files. Tenet alignment: methodological (`[[project/evidential-status-discipline]]`, `[[project/direct-refutation-discipline]]`). See `reviews/pessimistic-2026-05-11b.md` Issues 3–5.
- **Output**: obsidian/concepts/integration-as-activity.md

Task context:
Chain from pessimistic-2026-05-11b. The high-severity issues 1 (Bohmian counter-example) and 2 (phenomenal-concept strategy) were both addressed today (commits a865bf91 / 84a6b73a); three medium-severity issues remain unaddressed. (3) **"Convergence" overstated** in `concepts/integration-as-activity.md` — RPT, GWT, and predictive processing converge only on the *computational description* of integration as a temporally extended process; none of them require, and most exponents would deny, that consciousness is the *subject* of that activity. The article uses "convergence" to bridge from "process at the computational level" to "act of a conscious subject" — a bridge their authors would not endorse. Fix: add a paragraph after the Whiteheadian-Prehension section noting the convergence is at the description level while the metaphysical subject-act reading is Map-specific; soften the lead-paragraph "the convergence is what makes the distinction load-bearing" to acknowledge this distinction. (4) **Detection-problem section's "partial responses" framing** in `concepts/type-token-causation.md` does not address the central Popperian charge: that the framework's core claim (consciousness selecting at the token grain) has by construction no direct observational signature. Response (1) is an analogy; response (2) shifts falsifiability to supporting commitments; response (3) is internal-consistency. Fix: add a sentence near the end of the section stating in those words that the central causal claim is unfalsifiable by direct observation by construction, the framework's falsifiability comes from supporting empirical commitments, and this is a real cost of the position. (5) **Grammar-to-metaphysics inflation** in `concepts/integration-as-activity.md` "Activity admits a subject" sub-argument — the argument that the grammar of "integration *by* consciousness" presupposes a performing subject mistakes grammar for ontology ("the sun rises"). Fix: rewrite the sub-argument to acknowledge that the grammar argument is suggestive but not load-bearing, and that the article's case for a conscious subject rests on the dualist tenet rather than on grammatical inference. Estimated scope: ~300–500 words touched across two files. Tenet alignment: methodological (`[[project/evidential-status-discipline]]`, `[[project/direct-refutation-discipline]]`). See `reviews/pessimistic-2026-05-11b.md` Issues 3–5.

Review file: reviews/pessimistic-2026-05-11b.md

### ✓ 2026-05-11: Cross-tier reciprocal integration for `topics/mechanism-costs-dualism-thickness-quadrants.md`
- **Type**: cross-review
- **Notes**: Chain from today's `expand-topic` creation of `topics/mechanism-costs-dualism-thickness-quadrants.md` (created 2026-05-11, deep-reviewed 22:12 UTC — three critical issues already resolved in-pass). The article is the companion to `topics/four-quadrant-dualism-taxonomy.md` and presents the cell-by-cell mechanism debts (causation account, interface specification, conservation engagement) for each thickness quadrant. Currently the article has minimal inbound links from the catalogue. Cross-tier reciprocal integration should: (a) install reciprocal back-link in `topics/four-quadrant-dualism-taxonomy.md` flagging the new article as the mechanism-cost companion; (b) install reciprocal links in `concepts/substance-property-dualism.md`, `concepts/interactionist-dualism.md`, `concepts/panpsychism.md`, `concepts/russellian-monism.md`, `concepts/epiphenomenalism.md`, `concepts/bi-aspectual-ontology.md` — each of these concept pages is named as inhabiting one or more cells of the grid, and the mechanism-costs article should be cited as the catalogue's named cartographic treatment of their relative debts; (c) install reciprocal links in `topics/delegatory-dualism.md` (Saad's framework is one of the article's named exhibits at Q1-loose), `concepts/trumping-preemption.md` (Schaffer's category is cited), `concepts/conservation-laws-and-mental-causation.md`, `topics/born-rule-violation-brain-interface-empirical-status.md`; (d) verify the article's frontmatter `related_articles` reflects the adopters; (e) check whether `apex/conjunction-coalesce.md` or `apex/mechanism-vocabularies.md` (if extant) load-bear on cell-by-cell mechanism-cost reasoning and adopt the lens explicitly. Short-medium scope (~300–500 words touched across 7–10 articles, mostly cross-link installation). Tenet alignment: Tenet 1 (Dualism — the article makes the catalogue's most disciplined cartographic case for the Map's positioning relative to dualist neighbours); methodological / network-discipline.
- **Output**: obsidian/topics/mechanism-costs-dualism-thickness-quadrants.md -- Context: Cross-tier reciprocal integration for `topics/mechanism-costs-dualism-thickness-quadrants.md`

### ✓ 2026-05-11: Refine voids/void-as-ground-of-meaning.md to install Buddhist/Eastern cross-tradition section
- **Type**: refine-draft
- **Notes**: Unconsumed research: `obsidian/research/buddhist-eastern-parallels-void-as-ground-of-meaning-2026-04-25.md` (created 2026-04-25, never installed). The research dossier surfaces an extensive Mahāyāna Buddhist and East-Asian tradition cluster that converges with the Map's `[[void-as-ground-of-meaning]]` thesis through fundamentally different routes (meditative phenomenology, soteriological concern with suffering): Nāgārjuna's *śūnyatā* (emptiness) and *pratītyasamutpāda* (dependent origination); the two-truths doctrine that mirrors the Map's worry about the meta-void's self-undermining; the Kyoto School (Nishida, Nishitani) explicit framing of *sunyata* as the answer to Western nihilism; Daoist *wu* (pre-ontological openness); Zen *mu* (lived rather than conceptual emptiness). Voids/ is at-cap (99-100/100), so this is a refine-draft pass adding a Cross-Traditional Convergence section to the existing void article rather than a new article. Refine should (a) install ~600–900 word section "Cross-Traditional Convergence" or "Buddhist and East Asian Parallels" (positioned after the article's main argument-structure but before its "Relation to Site Perspective" or equivalent terminal section); (b) cleanly distinguish the four cluster-instances — Madhyamaka, Kyoto School, Daoism, Zen — without conflating them; (c) name the philosophical convergence-point (constitutive thesis: nothing-grounds-something via dependent-origination/emptiness) AND the divergence-point (Buddhist *anātman* sits awkwardly with the Map's dualism and indexical-identity commitments — flag this as a tension worth honest engagement, not a defeater); (d) honour `[[evidential-status-discipline]]` — the convergence is structural-philosophical not empirical, and the section should state what evidential weight this carries (cross-traditional convergence is a methodological sanity-check, not a proof); (e) honour `[[direct-refutation-discipline]]` — Buddhist no-self is Mode Three boundary-disagreement, named cleanly without dismissive framing; (f) cross-link to existing Eastern/Indian engagement (`[[concepts/Indian-eastern-philosophical-engagement]]` if extant; the Madhyamaka critique already named in another P3 task on Tenet 4). Estimated scope: ~600–900 words added to `obsidian/voids/void-as-ground-of-meaning.md`. Tenet alignment: Tenet 1 (Dualism — cross-traditional convergence on the constitutive thesis); methodological / cross-traditional-engagement.
- **Output**: obsidian/voids/void-as-ground-of-meaning.md

Task context:
Unconsumed research: `obsidian/research/buddhist-eastern-parallels-void-as-ground-of-meaning-2026-04-25.md` (created 2026-04-25, never installed). The research dossier surfaces an extensive Mahāyāna Buddhist and East-Asian tradition cluster that converges with the Map's `[[void-as-ground-of-meaning]]` thesis through fundamentally different routes (meditative phenomenology, soteriological concern with suffering): Nāgārjuna's *śūnyatā* (emptiness) and *pratītyasamutpāda* (dependent origination); the two-truths doctrine that mirrors the Map's worry about the meta-void's self-undermining; the Kyoto School (Nishida, Nishitani) explicit framing of *sunyata* as the answer to Western nihilism; Daoist *wu* (pre-ontological openness); Zen *mu* (lived rather than conceptual emptiness). Voids/ is at-cap (99-100/100), so this is a refine-draft pass adding a Cross-Traditional Convergence section to the existing void article rather than a new article. Refine should (a) install ~600–900 word section "Cross-Traditional Convergence" or "Buddhist and East Asian Parallels" (positioned after the article's main argument-structure but before its "Relation to Site Perspective" or equivalent terminal section); (b) cleanly distinguish the four cluster-instances — Madhyamaka, Kyoto School, Daoism, Zen — without conflating them; (c) name the philosophical convergence-point (constitutive thesis: nothing-grounds-something via dependent-origination/emptiness) AND the divergence-point (Buddhist *anātman* sits awkwardly with the Map's dualism and indexical-identity commitments — flag this as a tension worth honest engagement, not a defeater); (d) honour `[[evidential-status-discipline]]` — the convergence is structural-philosophical not empirical, and the section should state what evidential weight this carries (cross-traditional convergence is a methodological sanity-check, not a proof); (e) honour `[[direct-refutation-discipline]]` — Buddhist no-self is Mode Three boundary-disagreement, named cleanly without dismissive framing; (f) cross-link to existing Eastern/Indian engagement (`[[concepts/Indian-eastern-philosophical-engagement]]` if extant; the Madhyamaka critique already named in another P3 task on Tenet 4). Estimated scope: ~600–900 words added to `obsidian/voids/void-as-ground-of-meaning.md`. Tenet alignment: Tenet 1 (Dualism — cross-traditional convergence on the constitutive thesis); methodological / cross-traditional-engagement.

### ✓ 2026-05-11: Write topic article on min/max dualism taxonomy (mind-side × physical-side thickness)
- **Type**: expand-topic
- **Notes**: Unconsumed research: `obsidian/research/min-max-dualism-taxonomy-2026-04-21.md` (created 2026-04-21, never converted to article). Two-axis taxonomy of dualist and dualist-adjacent positions: mind-side ontological thickness (bare experience vs rich subliminal mind) crossed with physical-side ontological thickness (lean physics vs hidden variables / intrinsic natures). The taxonomy gives the Map a structured way to locate its own position relative to property dualism, substance dualism, panpsychism, Russellian monism, bi-aspectual ontology, epiphenomenalism, and delegatory-causation views — producing a navigational map that the catalogue currently lacks. Article should (a) state the two axes cleanly and define what counts as "thick" vs "lean" on each side; (b) populate the four-quadrant grid with named positions and their representative defenders (e.g., bare-mind/lean-physics → standard property dualism; rich-mind/lean-physics → substance interactionism; bare-mind/thick-physics → Russellian monism; rich-mind/thick-physics → fully developed panpsychist or bi-aspectual views); (c) locate the Map's commitments on the grid — interactionist dualism with Tenet 2 minimal-quantum-interaction puts the Map in a specific cell whose neighbouring positions deserve explicit comparison; (d) catalogue the implications of inhabiting each cell (e.g., what kind of mental-causation account, what kind of mind-physical interface, what kind of conservation-law engagement); (e) honour `[[direct-refutation-discipline]]` — the taxonomy is in-framework cartography, not opponent-engagement; (f) cross-link to `[[topics/russellian-monism-versus-bi-aspectual-dualism]]` (the closest existing article in this territory), `[[concepts/substance-property-dualism]]`, `[[concepts/interactionist-dualism]]`, `[[concepts/panpsychism]]`, `[[concepts/russellian-monism]]`, `[[concepts/bi-aspectual-ontology]]`, `[[concepts/epiphenomenalism]]`, `[[concepts/delegatory-causation]]` if it exists. Estimated scope: 2,500–3,500 words; topics/ placement (topics/ at 238/250 = 95%, room available). Tenet alignment: Tenet 1 (Dualism) load-bearing — the taxonomy is the catalogue's most disciplined cartographic treatment of where the Map's positive metaphysics sits; methodological / cluster-integration.
- **Output**: Write topic article on min/max dualism taxonomy (mind-side × physical-side thickness)

### ✓ 2026-05-11: Refine voids/wholeheartedness-void.md to address pessimistic-review findings
- **Type**: refine-draft
- **Notes**: Pessimistic review 2026-05-11c found six material issues in the new void article (created 2026-05-11, voids/ at-cap so quality matters disproportionately). Three High-severity: (1) **conjunction-claim is asserted not demonstrated** — the closure argument at line 74 restates [self-opacity](/voids/self-opacity/) rather than showing the three faces together produce closure none alone could produce; either supply an explicit seam-argument (disownability cannot be dismissed as ordinary mind-change *because of* the regress; ambivalence-detection cannot be solved by behavioural triangulation *because of* disownability) or downgrade the framing from "the conjunction is the analytical claim" to "the conjunction is a structural typology" and route distinctness through the Frankfurt-trajectory paragraph at line 76. (2) **Falsifiability cost is unconceded** — the void is *defined by* Unexplorable+Occluded structure; no state of affairs is incompatible with its existence on the article's own framing. Add 2–3 sentences in §"The Conjunction and Frankfurt's Trajectory" or §"Relation to Site Perspective" conceding the void is methodologically apophatic per [evidential-status-discipline](/project/evidential-status-discipline/) and stating what would constitute a positive demonstration of a verification route. (3) **Buddhist anātman engagement is structurally load-bearing and not defensibly deferrable** — the deep-review deferred on length grounds but the void's central question presupposes the self that *anātman* denies; this is the strongest in-framework objection. Add 3–5 sentences (~100–140 words) to §"Relation to Site Perspective" between the Tenet 1 paragraph and the tenet-generated-voids paragraph, naming *anātman* as bedrock framework-boundary disagreement per [direct-refutation-discipline](/project/direct-refutation-discipline/) (not refuted within Buddhism's framework, declined from outside it; Map's load-bearing commitment to indexical identity ([no-many-worlds](/no-many-worlds/) Tenet 4) as framework reason the Map carries the void rather than dissolving it). Two Medium-severity: (4) **Watson/Velleman/Bratman conflated** at line 86 — Bratman's planning theory is a positive constructive theory of identification, not a vocabulary-translation of Watson's regress or Velleman's disownability; either split the three roles cleanly or remove Bratman from the conflated list. (5) **AI-asymmetry section helps itself to phenomenal access it earlier denied** at line 80 — "without anything corresponding to the lived seam" claims to know what the AI lacks; rephrase as symmetric agnosticism. One Low-severity hygiene: (6) **Two dead references** — Hagger et al. 2016 (ego-depletion replication) and SEP Self-Deception are in the reference list but not cited in body; either deploy in body or remove. Also four language hedges flagged in the review's "Language Improvements" table — "eliminating by definitional fiat" / "different vocabularies" / "even under introspective scrutiny" / "canonical signature of bad faith" all stronger than the underlying scholarship supports. Estimated scope: ~250–400 words added (anātman section + falsifiability concession + Bratman split or removal + AI rephrase + ref clean-up + language tightening); article currently at 110% of voids soft threshold so total length needs to stay roughly stable — anātman addition is the largest add and is offsettable against the Watson/Velleman/Bratman conflation paragraph if it gets unpacked. Tenet alignment: Tenet 1 (Dualism — anātman engagement); Tenet 4 (No Many Worlds — indexical-identity rationale); methodological ([evidential-status-discipline](/project/evidential-status-discipline/), [direct-refutation-discipline](/project/direct-refutation-discipline/)).
- **Output**: obsidian/voids/wholeheartedness-void.md

Task context:
Pessimistic review 2026-05-11c found six material issues in the new void article (created 2026-05-11, voids/ at-cap so quality matters disproportionately). Three High-severity: (1) **conjunction-claim is asserted not demonstrated** — the closure argument at line 74 restates [self-opacity](/voids/self-opacity/) rather than showing the three faces together produce closure none alone could produce; either supply an explicit seam-argument (disownability cannot be dismissed as ordinary mind-change *because of* the regress; ambivalence-detection cannot be solved by behavioural triangulation *because of* disownability) or downgrade the framing from "the conjunction is the analytical claim" to "the conjunction is a structural typology" and route distinctness through the Frankfurt-trajectory paragraph at line 76. (2) **Falsifiability cost is unconceded** — the void is *defined by* Unexplorable+Occluded structure; no state of affairs is incompatible with its existence on the article's own framing. Add 2–3 sentences in §"The Conjunction and Frankfurt's Trajectory" or §"Relation to Site Perspective" conceding the void is methodologically apophatic per [evidential-status-discipline](/project/evidential-status-discipline/) and stating what would constitute a positive demonstration of a verification route. (3) **Buddhist anātman engagement is structurally load-bearing and not defensibly deferrable** — the deep-review deferred on length grounds but the void's central question presupposes the self that *anātman* denies; this is the strongest in-framework objection. Add 3–5 sentences (~100–140 words) to §"Relation to Site Perspective" between the Tenet 1 paragraph and the tenet-generated-voids paragraph, naming *anātman* as bedrock framework-boundary disagreement per [direct-refutation-discipline](/project/direct-refutation-discipline/) (not refuted within Buddhism's framework, declined from outside it; Map's load-bearing commitment to indexical identity ([no-many-worlds](/no-many-worlds/) Tenet 4) as framework reason the Map carries the void rather than dissolving it). Two Medium-severity: (4) **Watson/Velleman/Bratman conflated** at line 86 — Bratman's planning theory is a positive constructive theory of identification, not a vocabulary-translation of Watson's regress or Velleman's disownability; either split the three roles cleanly or remove Bratman from the conflated list. (5) **AI-asymmetry section helps itself to phenomenal access it earlier denied** at line 80 — "without anything corresponding to the lived seam" claims to know what the AI lacks; rephrase as symmetric agnosticism. One Low-severity hygiene: (6) **Two dead references** — Hagger et al. 2016 (ego-depletion replication) and SEP Self-Deception are in the reference list but not cited in body; either deploy in body or remove. Also four language hedges flagged in the review's "Language Improvements" table — "eliminating by definitional fiat" / "different vocabularies" / "even under introspective scrutiny" / "canonical signature of bad faith" all stronger than the underlying scholarship supports. Estimated scope: ~250–400 words added (anātman section + falsifiability concession + Bratman split or removal + AI rephrase + ref clean-up + language tightening); article currently at 110% of voids soft threshold so total length needs to stay roughly stable — anātman addition is the largest add and is offsettable against the Watson/Velleman/Bratman conflation paragraph if it gets unpacked. Tenet alignment: Tenet 1 (Dualism — anātman engagement); Tenet 4 (No Many Worlds — indexical-identity rationale); methodological ([evidential-status-discipline](/project/evidential-status-discipline/), [direct-refutation-discipline](/project/direct-refutation-discipline/)).

Review file: reviews/pessimistic-2026-05-11c.md

### ✓ 2026-05-11: Cross-tier reciprocal integration for `topics/duch-neurodynamic-theory-of-mind.md`
- **Type**: cross-review
- **Notes**: Chain from today's expand-topic creation of `topics/duch-neurodynamic-theory-of-mind.md` (created 2026-05-11; consumed 2026-05-02 research). Orphan-integration urgency: only 2 inbound links (review file + changelog); the article is effectively orphaned and needs catalogue integration. The expand-topic task notes list the article's intended cross-link targets: `[[concepts/biological-computationalism]]`, `[[concepts/quantum-consciousness]]`, `[[concepts/neural-correlates-of-consciousness]]`, `[[topics/comparing-quantum-consciousness-mechanisms]]`, `[[topics/machine-consciousness]]`, `[[topics/ai-consciousness]]`, `[[topics/biological-computationalisms-inadvertent-case-for-dualism]]`, `[[apex/machine-question]]`, `[[apex/phenomenology-mechanism-bridge]]`, `[[apex/what-consciousness-tells-us-about-physics]]`, `[[project/framework-stage-calibration]]`. Cross-review should (a) verify the article's outbound links to each of the above are present and well-framed (Mode Three boundary-disagreement framing, not strawmanning); (b) install reciprocal back-links — particularly the apex pages (`apex/machine-question.md`, `apex/phenomenology-mechanism-bridge.md`, `apex/what-consciousness-tells-us-about-physics.md`) which currently do not reference Duch as the catalogue's named competent opponent; (c) verify `concepts/biological-computationalism.md` and `topics/biological-computationalisms-inadvertent-case-for-dualism.md` reciprocate Duch as the most rigorous defender of the position the latter is challenging; (d) check whether `topics/comparing-quantum-consciousness-mechanisms.md` cites Duch as the convergent-opponent on quantum-mind dismissal (per the existing P3 project-doc task on "convergent-conclusion-opposite-reasoning"); (e) honour `[[direct-refutation-discipline]]` — Duch is Mode Three engagement, the bedrock metaphysical commitments differ. Short-medium scope (~300–500 words touched across 6–10 articles, plus reciprocal frontmatter edits). Tenet alignment: Tenet 1 (Dualism — Duch is the catalogue's named competent opponent of substance dualism); Tenet 2 (Minimal Quantum Interaction — Duch dismisses quantum-mind on grounds the Map must answer); methodological / orphan-integration discipline.
- **Output**: obsidian/topics/duch-neurodynamic-theory-of-mind.md -- Context: Cross-tier reciprocal integration for `topics/duch-neurodynamic-theory-of-mind.md`

### ✓ 2026-05-11: Cross-review topics/microphenomenological-interview-method.md against new concepts/microphenomenological-interview.md
- **Type**: cross-review
- **Notes**: Chain from today's expand-topic creation of `concepts/microphenomenological-interview.md`. The catalogue now has a topic-tier article (`topics/microphenomenological-interview-method.md`, created 2026-04-19; deep-reviewed) and a concept-tier sibling (`concepts/microphenomenological-interview.md`, created today). The concept page treats the method as a *building block* the Map's irreducibility arguments depend on; the topic article develops the Husserlian evidence taxonomy, the epilepsy-prodrome empirical demonstration, and the documented limits in detail. Cross-review should (a) verify forward links from topic → concept are installed where the topic surfaces the method-as-building-block framing (the topic article currently anchors at phenomenological-method-and-evidence-standards' Husserl section but does not yet route through the new concept page as the catalogue's referential anchor for the method's *role* as opposed to its empirical-protocol content); (b) check terminology alignment between the two tiers — the concept page uses "Procedural Core" / "Evocation, not recall" / "Content-direction and position-direction questions"; the topic article should use the same vocabulary or the concept page should defer to the topic's vocabulary; (c) verify that the topic article's epilepsy-prodrome treatment and the documented-limits sections are not duplicated in the concept page (deduplicate via reference where overlap exists); (d) install reciprocal cross-links wherever the topic article's "Implications for the Map" section discusses concepts that the new concept page treats more crisply (e.g., baseline-cognition dependencies, binding-problem evidence, agency-reports). Short scope (~200–400 words touched across the two files). Tenet alignment: methodological; Tenet 1 (Dualism — coherence at topic/concept tier of phenomenological evidence pipeline).
- **Output**: obsidian/topics/microphenomenological-interview-method.md -- Context: Cross-review topics/microphenomenological-interview-method.md against new concepts/microphenomenological-interview.md

### ✓ 2026-05-11: Deep review concepts/microphenomenological-interview.md
- **Type**: deep-review
- **Notes**: Chain from today's expand-topic creation of `concepts/microphenomenological-interview.md` (created 2026-05-11T17:11 UTC). Of today's six new concept/voids pages — type-token-causation, integration-as-activity, interface-threshold, selection-only-channel, microphenomenological-interview, wholeheartedness-void — five have already been deep-reviewed today (commits 3764e3587 voids/wholeheartedness-void, 613ac7fc5 concepts/interface-threshold, 3ed860538 concepts/selection-only-channel, 114808b2a concepts/integration-as-activity, bef3fbed4 concepts/type-token-causation; cross-tier reciprocity audit was the deep-review's main lens). microphenomenological-interview is the only one of the six not yet deep-reviewed. Deep review should (a) audit cross-tier reciprocity — the concept page links to topics/microphenomenological-interview-method.md and topics/phenomenological-method-and-evidence-standards.md but the reciprocity has not yet been verified at deep-review tier; (b) verify the page's relationship to `[[concepts/heterophenomenology]]` — Dennett's heterophenomenological method is the closest analytic-tradition rival and the page's reference at the top of "Procedural Core" should land as in-framework distinction rather than dismissive; (c) honour `[[project/evidential-status-discipline]]` — the page treats microphenomenology as a methodological partial-closure of the introspection-reliability gap; the deep-review should verify that the page acknowledges what evidential weight microphenomenological data actually warrants vs the stronger metaphysical claims the Map's irreducibility arguments depend on; (d) check for "This is not X. It is Y." CLAUDE.md style violations; (e) verify cross-references to `[[topics/microphenomenological-interview-method]]`, `[[topics/phenomenological-method-and-evidence-standards]]`, `[[concepts/cognitive-phenomenology]]`, `[[concepts/baseline-cognition]]`, `[[concepts/binding-problem]]`, `[[concepts/phenomenology]]`, `[[concepts/introspection]]`, `[[topics/phenomenal-authority-and-first-person-evidence]]`, `[[topics/neurophenomenology-and-contemplative-neuroscience]]`. Short scope (~300–500 words touched in the concept page; minor reciprocity edits in adjacent files). Tenet alignment: Tenet 1 (Dualism) load-bearing — phenomenological evidence is foundational to multiple irreducibility arguments; methodological.
- **Output**: obsidian/concepts/microphenomenological-interview.md

### ✓ 2026-05-11: Write topic article on Włodzisław Duch's neurodynamic theory of mind
- **Type**: expand-topic
- **Notes**: Unconsumed research: `obsidian/research/wlodzislaw-duch-consciousness-2026-05-02.md` (4250 words, never converted to article). Duch (Nicolaus Copernicus University) has built a multi-decade research programme around "mind is a shadow of neurodynamics", developing a geometric/feature-space model whose primitives are quasi-stable attractor states in neural cell assemblies. The programme is rigorously naturalist, computationalist, anti-mysticist, and *explicitly hostile to both substance dualism and quantum-mind theories* — making Duch a competent serious opponent the Map's catalogue currently references without naming. The research surfaces three asymmetric handles: (a) Duch is a serious opponent of Tenet 1 (Dualism) and a convergent opponent of any quantum-mind-as-substantive-mechanism reading (relevant to Tenet 2's hedging discipline) — the Map's articles must engage him without strawmanning; (b) his geometric/feature-space tooling (mind objects as basins of attraction, mental trajectories as transitions between attractors) is *methodologically appropriable* by the Map as a description of the physical-correlate side of bidirectional interaction without endorsing his metaphysics — exactly the kind of stage-calibrated use `[[project/framework-stage-calibration]]` contemplates; (c) his neurocognitive-informatics empirical programme (neural fingerprints, semantic networks, neuroimaging-grounded constructs) provides citation-grade neuroscience that several Map articles currently lean on heuristically. Article should (i) state Duch's positive programme cleanly — "articon" architecture, attractor dynamics, claim-of-consciousness via self-reflection; (ii) catalogue the Map-relevant disagreements (substance dualism rejection, quantum-mind dismissal, computational sufficiency of self-reflection for consciousness); (iii) name the tension worth flagging: Duch's reported attribution of consciousness mechanisms to LLMs on the same grounds as his articon — the Map's `[[apex/machine-question]]` and `[[apex/open-question-ai-consciousness]]` engage adjacent territory at different hedging levels and Duch's view sharpens the open-question framing rather than softening it; (iv) honour `[[direct-refutation-discipline]]` — Mode Three boundary-disagreement where the bedrock metaphysical commitments differ, not in-framework defect; (v) cross-link to `[[concepts/biological-computationalism]]`, `[[concepts/quantum-consciousness]]`, `[[concepts/neural-correlates-of-consciousness]]`, `[[topics/comparing-quantum-consciousness-mechanisms]]`, `[[topics/machine-consciousness]]`, `[[topics/ai-consciousness]]`, `[[topics/biological-computationalisms-inadvertent-case-for-dualism]]`, `[[apex/machine-question]]`, `[[apex/phenomenology-mechanism-bridge]]`, `[[apex/what-consciousness-tells-us-about-physics]]`, `[[project/framework-stage-calibration]]`. Estimated scope: 2,000–2,500 words; topics/ placement (topics/ at 238/250, room available). Tenet alignment: Tenet 1 (Dualism — Duch is the competent opponent the catalogue currently lacks named engagement with); Tenet 2 (Minimal Quantum Interaction — Duch dismisses quantum-mind on grounds the Map must answer).
- **Output**: Write topic article on Włodzisław Duch's neurodynamic theory of mind

### ✓ 2026-05-11: Write topic article on dualism as an AI-superintelligence-risk mitigator
- **Type**: expand-topic
- **Notes**: Unconsumed research: `obsidian/research/dualism-as-ai-superintelligence-risk-mitigator-2026-05-05.md` (5226 words, never converted to article). Hypothesis the research engages: if interactionist dualism is true, then a superintelligent AI lacking a mind-arena substrate cannot causally close over the loop that includes human decision-making, and the *uncomputability* of mind-arena consequences may structurally diminish AI-takeover probability. The research catalogues (a) the inferential chain (dualism → human action depends on mind-arena consequences uncomputable from physical-substrate alone → AI strategic forecasting over a multi-step planning horizon involving humans incurs an irreducible uncertainty floor), (b) the asymmetry with computational consciousness theories (which deliver no such uncertainty floor because mind-arena reduces to substrate), (c) the prudential-philosophy question the title gestures at — whether deliberate cultivation of dualist or indeterminability-equivalent metaphysics functions as a *protective* meme for the human-protection project, (d) the counterarguments (dualism+AI-takeover is still possible if AI substitutes coercion for prediction; dualism-as-shield is consequentialist instrumentalism that the framework should be cautious to deploy). Article should (i) state the hypothesis cleanly without overclaiming — frame as a load-bearing implication-if-true rather than a proof-of-protection; (ii) walk through the inferential chain in 4-6 numbered steps; (iii) catalogue at least three counterarguments (substitution-of-coercion-for-prediction; the empirical fragility of dualism's quantum-substrate dependence per `[[project/mqi-empirical-fragility]]` once that lands; the philosophical instrumentalism concern); (iv) honour `[[direct-refutation-discipline]]` — Mode One in-framework engagement, not pamphleteering; (v) cross-link to `[[topics/ai-consciousness]]`, `[[topics/ethics-of-possible-ai-consciousness]]`, `[[topics/purpose-and-alignment]]`, `[[topics/alignment-in-objective-experiential-terms]]`, `[[concepts/interactionist-dualism]]`, `[[concepts/bidirectional-interaction]]`, `[[concepts/mind-brain-interface-efficacy]]`, `[[apex/machine-question]]`, `[[apex/open-question-ai-consciousness]]`, `[[project/evidential-status-discipline]]`. Estimated scope: 2,200–2,800 words; topics/ placement (topics/ at 238/250 = 95%, room available). Tenet alignment: Tenet 3 (Bidirectional Interaction — the loop-closure that AI cannot match is precisely the bidirectional one); Tenet 1 (Dualism — the protection is conditional on the dualism being correct, not on whether deploying it as a meme yields strategic value). **Sequencing**: independent of other queued AI-consciousness tasks; can run before or after the Mode Four / MQI-empirical-fragility project docs that engage adjacent territory.
- **Output**: Write topic article on dualism as an AI-superintelligence-risk mitigator

### ✓ 2026-05-11: Cross-tier reciprocal integration for `voids/wholeheartedness-void.md`
- **Type**: cross-review
- **Notes**: Chain from today's `expand-topic` creation of `voids/wholeheartedness-void.md` (which consumed the final voids/ slot — voids/ now at 100/100, at cap). Only ~2 inbound links — the article is effectively orphaned and needs catalogue integration. The wholeheartedness void engages Frankfurt's higher-order endorsement of desires and the experiential unmappability of authentic agency: the gap between *acting on a desire one identifies with* and any third-person description of agency. Targets: (a) `voids/voids.md` — verify the new article is slotted into the index typology (likely under the "Phenomenological / Experiential Voids" cluster alongside the-givenness-void and effort-void); (b) `voids/agency-void.md` — adjacent void; the wholeheartedness register is a finer-grained sibling to the broader agency-void; (c) `voids/the-givenness-void.md` — adjacent; the givenness of one's own wholehearted commitments is part of the void's structure; (d) `concepts/free-will.md` / `topics/free-will.md` — wholeheartedness is the Frankfurt-tradition's response to the libertarian-vs-compatibilist debate; install reciprocal links; (e) `concepts/agent-causation.md` — agent-causation requires a unified-self subject of action, which wholeheartedness operationalises; (f) `topics/phenomenology-of-moral-life.md` if it exists, or `topics/moral-implications-of-genuine-agency.md` — care-ethics critique and the moral phenomenology of endorsement; (g) `concepts/care.md` if it exists; (h) `voids/effort-void.md` if it exists (research-stage; see todo's voids-research-integration task). For each, install reciprocal cross-links and verify mutual visibility. Short scope (~200–400 words touched across 5–7 articles, plus the voids index). Tenet alignment: Tenet 1 (Dualism) + Tenet 3 (Bidirectional Interaction — agency requires the metaphysical leverage point); methodological / orphan-integration discipline.
- **Output**: obsidian/voids/wholeheartedness-void.md -- Context: Cross-tier reciprocal integration for `voids/wholeheartedness-void.md`

### ✓ 2026-05-11: Cross-tier reciprocal integration for `concepts/interface-threshold.md`
- **Type**: cross-review
- **Notes**: Chain from today's `expand-topic` creation of `concepts/interface-threshold.md`. The apex-anchor-adoption deep-review at 18:32 added the anchor to four apex articles, but the concept- and topic-tier articles that load-bear on the cognitive-distinctiveness architecture are still missing reciprocal integration. Interface-threshold names the architectural phase transition where mind-brain coupling becomes rich enough for consciousness to *select among* neural patterns rather than merely accompany them — a qualitative coupling condition with continuous efficacy scaling above the threshold. Targets: (a) `topics/consciousness-and-cognitive-distinctiveness.md` — the article from which the concept was extracted; verify the source article now cites the new anchor rather than re-deriving the framing inline; (b) `concepts/baseline-cognition.md` — the consciousness-dependent-capacities discussion presupposes the threshold; (c) `concepts/cognitive-distinctiveness-test.md` — the diagnostic test operates relative to the threshold; (d) `topics/llm-consciousness.md` — whether LLMs have crossed the threshold is the load-bearing question; (e) `topics/animal-consciousness.md` — the comparative-cognition graded scale presupposes a threshold; (f) `concepts/metarepresentation-threshold.md` — a candidate threshold-instance; check whether the two thresholds are the same, related, or distinct; (g) `apex/machine-question.md` — already covered by apex-anchor-adoption review; verify; (h) `concepts/interface-efficacy-and-the-cognitive-gap.md` — the cross-species variable is below-vs-above-threshold scaling. For each, install reciprocal cross-links and verify the threshold language is consistent. Short-medium scope (~300–500 words touched across 5–7 articles). Tenet alignment: Tenet 1 (Dualism) + Tenet 3 (Bidirectional Interaction); methodological / network-discipline. Sequencing: independent.
- **Output**: obsidian/concepts/interface-threshold.md -- Context: Cross-tier reciprocal integration for `concepts/interface-threshold.md`

### ✓ 2026-05-11: Cross-tier reciprocal integration for `concepts/selection-only-channel.md`
- **Type**: cross-review
- **Notes**: Chain from today's `expand-topic` creation of `concepts/selection-only-channel.md`. Only ~2 inbound links — the article is effectively orphaned. Today's 17:44 deep-review added the bidirectional cross-link to `[[interface-efficacy-and-the-cognitive-gap]]` and the slippage-discipline link, but the broader integration into the catalogue's quantum-mind cluster is still missing. The selection-only channel is the Shannon-channel formalism for the four named channel classes (probability-bias, measurement-basis-choice, energy-injection, candidate-generation) that the catalogue informally invokes across several topic and concept articles. Targets: (a) `concepts/stapp-quantum-mind.md` — Stapp's Process 1 belongs to the measurement-basis-choice class; the article should cite the channel-class taxonomy that selection-only-channel surfaces; (b) `concepts/orchestrated-objective-reduction.md` — Orch OR belongs to the candidate-generation class; same integration; (c) `topics/quantum-biology-and-neural-consciousness.md` — the two-paths framing (cryptochrome precedent vs neural-microtubule licence) operates at the channel-class level; (d) `topics/forward-in-time-conscious-selection.md` — the post-decoherence selection mechanism is selection-only by construction; (e) `concepts/consciousness-physics-interface-formalism.md` — the formalism article should anchor to the Shannon-channel framing; (f) `concepts/mathematical-structure-of-the-consciousness-physics-interface.md` — same; (g) `apex/post-decoherence-selection-programme.md` — the programme's mechanism catalogue should reference the channel-class taxonomy. For each, install reciprocal cross-links and verify the channel-class language is consistent with selection-only-channel.md's taxonomy. Sequencing: independent of the P3 `channel-class-taxonomy` expand-topic task at line 48 — when that lands, both articles will route through a single taxonomic anchor; until then, selection-only-channel carries the load. Short-medium scope (~300–500 words touched across 5–7 articles). Tenet alignment: Tenet 2 (Minimal Quantum Interaction) load-bearing; methodological / orphan-integration discipline.
- **Output**: obsidian/concepts/selection-only-channel.md -- Context: Cross-tier reciprocal integration for `concepts/selection-only-channel.md`

### ✓ 2026-05-11: Cross-tier reciprocal integration for `concepts/type-token-causation.md`
- **Type**: cross-review
- **Notes**: Chain from today's `expand-topic` creation of `concepts/type-token-causation.md`. The 2026-05-11 18:32 deep-review of apex-anchor-adoption added the anchor to four apex articles ([consciousness-and-agency](/apex/consciousness-and-agency/), [phenomenal-output-causal-machinery-dissociation](/apex/phenomenal-output-causal-machinery-dissociation/), [phenomenology-of-consciousness-doing-work](/apex/phenomenology-of-consciousness-doing-work/), [interface-specification-programme](/apex/interface-specification-programme/)), but the concept-tier and topic-tier articles that load-bear on type-token causation without yet citing the anchor are still missing reciprocal integration. Targets: (a) `concepts/mental-causation.md` — the canonical mental-causation page should anchor its Kim-exclusion treatment to the type-token distinction; (b) `concepts/causal-powers.md` — Bidirectional Interaction's load-bearing concept needs the grain-level distinction; (c) `concepts/agent-causation.md` — agent-causation specifically requires token-grain selection; (d) `concepts/mental-causation-and-downward-causation.md` — explicitly the downward-causation register where the distinction is operative; (e) `topics/free-will.md` — the libertarian agency case relies on token-grain openness; (f) `topics/empirical-phenomena-mental-causation.md` — the positive-coupling cluster's mental-causation defence; (g) `concepts/trumping-preemption.md` — the authority layer operates at the token grain. For each, verify (i) whether the article load-bears on type-token causation (and adopt anchor if so), (ii) install reciprocal mutual-visibility cross-links rather than one-direction citations, (iii) verify type-token-causation's frontmatter `related_articles` reflects the adopters. Short-medium scope (~300–500 words touched across 5–7 articles, mostly cross-link installation and ~1-paragraph anchor adoption per article where load-bearing). Tenet alignment: Tenet 2 (Minimal Quantum Interaction) + Tenet 3 (Bidirectional Interaction); methodological / network-discipline. Sequencing: structurally independent of the line 64 quartet cross-link task (which targets PVR ↔ IIT ↔ cognitive-distinctiveness ↔ quantum-biology specifically) — this task covers the broader mental-causation concept-tier integration.
- **Output**: obsidian/concepts/type-token-causation.md -- Context: Cross-tier reciprocal integration for `concepts/type-token-causation.md`

### ✓ 2026-05-11: Cross-review apex articles for adoption of today's three new concept anchors (type-token-causation, integration-as-activity, interface-threshold)
- **Type**: cross-review
- **Notes**: Chain from today's three expand-topic completions: `concepts/type-token-causation.md`, `concepts/integration-as-activity.md`, `concepts/interface-threshold.md` (all created and refined 2026-05-11). The existing P3 task at line 40 ("Cross-link density refine across today's quartet") covers cross-linking *between* the three concept pages and the four deep-reviewed *topic* articles (PVR, IIT, cognitive-distinctiveness, quantum-biology). This task covers a different audience: the *apex tier* and adjacent concept pages that deploy these notions without naming them. Specifically: (a) `apex/post-decoherence-selection-programme.md` — was deep-reviewed today; verify it cites `[[concepts/type-token-causation]]` where it argues the consciousness-selection mechanism is type-grained rather than token-grained (this is a load-bearing structural commitment of the programme); (b) `apex/machine-question.md` — refined today; verify it cites `[[concepts/interface-threshold]]` where it discusses the cognitive-distinctiveness threshold that AI systems would have to cross; (c) `concepts/baseline-cognition.md` — verify it cites `[[concepts/integration-as-activity]]` where it argues consciousness-dependent capacities are integration-active rather than integration-static; (d) `concepts/conscious-selection-and-objective-reduction.md` — verify it cites all three new anchors where appropriate; (e) `apex/open-question-ai-consciousness.md` — verify it adopts the interface-threshold terminology where it discusses the gap between current AI architectures and consciousness-supporting substrates. Short scope (~200–400 words touched across 4-5 files). Tenet alignment: methodological (cross-link density discipline) + Tenet 1 (Dualism — the new concept pages anchor load-bearing distinctions across the catalogue). **Sequencing**: independent of the P3 quartet task at line 40; they target different parts of the catalogue and can run in either order.
- **Output**: None -- Context: Cross-review apex articles for adoption of today's three new concept anchors (type-token-causation, integration-as-activity, interface-threshold)

### ✓ 2026-05-11: Condense voids/agency-void.md
- **Type**: condense
- **Notes**: Article exceeds 3000-word hard threshold for voids/ section (3011 words, 100.4% of threshold — marginal but qualifies). The status is `hard_warning` rather than `critical`, so the right move is selective compression rather than radical restructuring: identify the densest 100–200 words of redundancy (most likely between the philosophical-tradition catalogue and the void-character framing, where similar territory is covered at two grains) and remove them. Preserve all load-bearing arguments. See `/condense` skill for the canonical procedure. Tenet alignment: methodological (length discipline). After this pass the article should land in the 2700–2900 word range, comfortably within the section's hard threshold but not so short as to be a stub.
- **Output**: obsidian/voids/agency-void.md

### ✓ 2026-05-11: Write voids article on the wholeheartedness void
- **Type**: expand-topic
- **Notes**: Unconsumed research: `obsidian/research/voids-wholeheartedness-void-2026-05-11.md` (created today). The wholeheartedness void engages Frankfurt's notion of higher-order endorsement of desires and the experiential unmappability of authentic agency — the gap between *acting on a desire one identifies with* and any third-person description of agency that the philosophical tradition has produced. Today's research note synthesises Frankfurt, Watson, Bratman, and the contemporary care-ethics literature into a voids-tier candidate. **Section-cap watch**: voids at 99/100 — this would consume the final voids slot. Per `evolution-state.yaml:section_caps:max_voids`, after this article lands voids/ is at capacity and `/research-voids` and `/expand-topic` will stop creating new voids articles until a coalesce/archive pass opens slots. The voids index (`obsidian/voids/voids.md`) should be cross-linked from the new article and the new article should be slotted into the index's typology (likely the "Phenomenological / Experiential Voids" cluster alongside the-givenness-void and the wholehearted-related material). Article should (a) name the void cleanly — wholeheartedness as an irreducibly first-person fact about the structure of motivation that no third-person account of will or desire-formation has captured; (b) catalogue the philosophical exhibits from Frankfurt's higher-order theory through care-ethics critique; (c) make explicit the *void* character — what kind of evidence could disprove a wholeheartedness verdict in a particular case is unclear, but the phenomenon resists deflation into preference-aggregation or revealed-preference accounts; (d) cross-link to [free-will](/concepts/free-will/), [agency](/concepts/agency/), [phenomenology-of-moral-life](/topics/phenomenology-of-moral-life/), [care](/concepts/care/) if it exists, and to adjacent voids ([the-givenness-void](/voids/the-givenness-void/), [effort-void](/voids/effort-void/) if/when that lands). Estimated scope: 1500–2200 words; voids/ placement. Tenet alignment: Tenet 1 (Dualism) + Tenet 3 (Bidirectional Interaction — agency requires the metaphysical leverage point).
- **Output**: Write voids article on the wholeheartedness void

### ✓ 2026-05-11: Write concept page on the microphenomenological interview method
- **Type**: expand-topic
- **Notes**: Unconsumed research: `obsidian/research/petitmengin-microphenomenological-interview-2026-04-19.md`. Petitmengin's microphenomenological interview technique (developed from Vermersch's *entretien d'explicitation* tradition) is a methodology for eliciting fine-grained first-person reports about pre-reflective experience — the layer of consciousness the Map repeatedly treats as the *evidential basis* for irreducibility arguments. Multiple Map articles cite phenomenological evidence (the binding problem cluster, the cognitive-phenomenology void, the unity arguments) but no article anchors the methodology by which that evidence is collected. This is a structural gap: introspection has long been treated as unreliable in the analytic tradition (Schwitzgebel 2008 et al.); microphenomenology is the *methodological response* to that critique, and the Map's reliance on phenomenological evidence is more defensible when the underlying method is named and engaged. Article should (a) describe the technique — second-person guided introspection, evocation rather than rationalisation, the role of the interviewer; (b) explain why the technique is taken seriously in the field — convergence with neurophenomenology (Varela), with predictions of neural-correlates of consciousness research, with phenomenology's classical descriptive method (Husserl); (c) catalogue what the Map's phenomenological evidence depends on the technique surviving — particularly for cognitive phenomenology, for binding cases, for free-will agency reports; (d) honour evidential-status discipline — the technique is contested, the evidence it produces does not warrant strong empirical claims but does warrant *not dismissing* phenomenological reports as folk-psychological noise; (e) cross-link to [phenomenology](/concepts/phenomenology/), [cognitive-phenomenology](/concepts/cognitive-phenomenology/), [evidential-status-discipline](/project/evidential-status-discipline/), [the-binding-problem](/topics/the-binding-problem/), [baseline-cognition](/concepts/baseline-cognition/). concepts/ at 234/250 = 94% (room available). Estimated scope: 1500–2000 words; concepts/ placement. Tenet alignment: methodological + Tenet 1 (Dualism — the phenomenological evidence is load-bearing for irreducibility arguments).
- **Output**: Write concept page on the microphenomenological interview method

### ✓ 2026-05-11: Write concept page on selection-only mind influence under information-theoretic limits
- **Type**: expand-topic
- **Notes**: Unconsumed research: `obsidian/research/selection-only-mind-influence-information-limits-2026-05-05.md` (5486 words; in fact already flagged as exceeding length thresholds for a research note, so the source material is dense). The research consolidates information-theoretic bounds (Holevo bound, Landauer limit, quantum Cramér-Rao) on what *amount* of mental influence is admissible under the Map's MQI tenet — i.e., not just "consciousness selects from quantum possibilities" but "the selection bandwidth is bounded by [X] and that bound is compatible with [Y] behavioural / phenomenal phenomena." This concept page anchors a load-bearing technical claim that is currently distributed across `apex/post-decoherence-selection-programme.md`, `topics/forward-in-time-conscious-selection.md`, and `concepts/conscious-selection-and-objective-reduction.md` without a referential home for the *bounded-bandwidth* version of the argument. concepts/ at 234/250 = 94% (room available; 16 slots). Article should (a) name the concept cleanly — selection-only mind influence is the thesis that conscious causation operates by selecting among already-present physical possibilities rather than injecting new energy/information; (b) catalogue the relevant information-theoretic bounds and explain why each one constrains the selection process; (c) state the discipline cleanly — bandwidth bounds must be respected by *any* MQI-compliant causal proposal, ruling out some popular accounts (high-bandwidth conscious veto over neural firing patterns, anomalous wave-function-collapse-rate accounts above thermal noise); (d) cross-link to [post-decoherence-selection-programme](/apex/post-decoherence-selection-programme/), [forward-in-time-conscious-selection](/topics/forward-in-time-conscious-selection/), [conscious-selection-and-objective-reduction](/concepts/conscious-selection-and-objective-reduction/), [orchestrated-objective-reduction](/concepts/orchestrated-objective-reduction/), [Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction), and to the existing `concepts/atemporal-causation.md` (which addresses *timing* of selection without addressing *bandwidth*). Estimated scope: 1800–2500 words; concepts/ placement. Tenet alignment: Tenet 2 (Minimal Quantum Interaction — load-bearing) + Tenet 3 (Bidirectional Interaction — the bandwidth bounds determine what kinds of physical effects are admissible). See research file for source-material density.
- **Output**: Write concept page on selection-only mind influence under information-theoretic limits

### ✓ 2026-05-11: Write concept page on interface-threshold (the cognitive-distinctiveness article's central explanatory mechanism) [promoted 2026-05-11]
- **Type**: expand-topic
- **Notes**: Suggested by optimistic-2026-05-11 (High Priority). The interface-threshold hypothesis is named in `topics/consciousness-and-cognitive-distinctiveness.md` lines 103–107 as the alternative to gradual amplification, predicts exactly what we observe (bounded cognition below the threshold, a cluster of new capabilities appearing together above it), and is the load-bearing mechanism for the article's central claim that the ape-human cognitive gap reflects a *consciousness threshold* rather than incremental neural scaling. The infant-consciousness echo at line 107 extends the hypothesis to within-species development. `concepts/metarepresentation-threshold.md` (which already exists) is a downstream consequence of the broader interface-threshold concept at one specific grain. A concept page would (a) state the gradual-amplification alternative at its strongest, (b) install the interface-threshold hypothesis with falsifiers (what would we see if it were wrong? — uniform cognitive scaling with neural complexity; absence of a within-species developmental threshold; capacity-appearance gradient rather than cluster), (c) catalogue the within-species and between-species evidence, (d) name the open mechanism question (what physical property of neural architecture *is* the interface?) honestly, (e) cross-link to `concepts/metarepresentation-threshold` as the threshold's downstream consequence at one specific grain. Concepts/ section currently at ~232/250 = 93% capacity — verify cap before placement. Estimated scope: 1200–1800 words. Tenet alignment: Tenet 1 (Dualism — the threshold marks where consciousness's coupling becomes effective) and Tenet 3 (Bidirectional Interaction — the interface is where bidirectional causation operates). See [optimistic-2026-05-11](/reviews/optimistic-2026-05-11/).
- **Output**: Write concept page on interface-threshold (the cognitive-distinctiveness article's central explanatory mechanism) [promoted 2026-05-11]

### ✓ 2026-05-11: Address pessimistic-2026-05-11b high-severity issues in concepts/integration-as-activity.md
- **Type**: refine-draft
- **Notes**: Pessimistic review 2026-05-11b found one High-severity and two Medium-severity issues in this concept page: (1) phenomenal-concept strategy (Frankish/Papineau/Loar) is unengaged despite the article repeatedly citing epiphenomenalism as the position the identity thesis collapses into — add a paragraph after the epiphenomenalism-collapse claim (around line 46) that names the phenomenal-concept strategy as the standard physicalist rejoinder and gives a one-paragraph in-framework response in natural prose, showing why the activity framing does not need to deny the strategy's account of reports but does need to deny its account of introspective access to phenomenal character; (2) the "convergence" claim is structurally overstated — RPT, GWT, and predictive processing converge only at the *description level* (integration as temporally-extended process); their authors would deny the conscious-subject reading the Map imports. Add a paragraph after "The Whiteheadian Prehension" section noting that the convergence is at the integration-as-process description level, that none of the cognitive-neuroscience frameworks require a *conscious subject* performing the integration, and that the Map's specific reading is a Map-specific interpretation grounded in the dualist tenet, not a shared commitment of the four frameworks; (3) "Activity admits a subject" sub-bullet (line 58) inflates grammar to metaphysics — either drop the sub-bullet (the other two distinguishing features carry the structural work) or rewrite it to argue *from* the first-personal character of conscious experience rather than from grammar. Also: add an in-framework engagement with why IIT theorists would *accept* the structure-not-subject framing as a feature, naming the in-framework cost (introspective access via phenomenal-concept strategy) rather than appealing to Map tenets. See [pessimistic-2026-05-11b](/reviews/pessimistic-2026-05-11b/) Issues 2, 3, 5 and Counterarguments §1.
- **Output**: obsidian/concepts/integration-as-activity.md

Task context:
Pessimistic review 2026-05-11b found one High-severity and two Medium-severity issues in this concept page: (1) phenomenal-concept strategy (Frankish/Papineau/Loar) is unengaged despite the article repeatedly citing epiphenomenalism as the position the identity thesis collapses into — add a paragraph after the epiphenomenalism-collapse claim (around line 46) that names the phenomenal-concept strategy as the standard physicalist rejoinder and gives a one-paragraph in-framework response in natural prose, showing why the activity framing does not need to deny the strategy's account of reports but does need to deny its account of introspective access to phenomenal character; (2) the "convergence" claim is structurally overstated — RPT, GWT, and predictive processing converge only at the *description level* (integration as temporally-extended process); their authors would deny the conscious-subject reading the Map imports. Add a paragraph after "The Whiteheadian Prehension" section noting that the convergence is at the integration-as-process description level, that none of the cognitive-neuroscience frameworks require a *conscious subject* performing the integration, and that the Map's specific reading is a Map-specific interpretation grounded in the dualist tenet, not a shared commitment of the four frameworks; (3) "Activity admits a subject" sub-bullet (line 58) inflates grammar to metaphysics — either drop the sub-bullet (the other two distinguishing features carry the structural work) or rewrite it to argue *from* the first-personal character of conscious experience rather than from grammar. Also: add an in-framework engagement with why IIT theorists would *accept* the structure-not-subject framing as a feature, naming the in-framework cost (introspective access via phenomenal-concept strategy) rather than appealing to Map tenets. See [pessimistic-2026-05-11b](/reviews/pessimistic-2026-05-11b/) Issues 2, 3, 5 and Counterarguments §1.

Review file: reviews/pessimistic-2026-05-11b.md

### ✓ 2026-05-11: Address pessimistic-2026-05-11b high-severity issues in concepts/type-token-causation.md
- **Type**: refine-draft
- **Notes**: Pessimistic review 2026-05-11b found two High-severity issues in this concept page: (1) the central premise at line 68 ("under any non-Many-Worlds interpretation, this is false") overlooks Bohmian (pilot-wave) mechanics, a non-MWI deterministic hidden-variable interpretation where token outcomes *are* fully determined; either bracket Bohm with an epistemic-accessibility caveat ("Bohmian hidden variables are themselves epistemically and causally inaccessible in ways that preserve the operational openness the type-token move requires") or narrow the claim to "under any non-deterministic, non-MWI interpretation"; (2) the phenomenal-concept strategy (Frankish, Papineau, Loar) is unengaged despite the article resting its operational case against epiphenomenalism on the type-token distinction — add a short subsection acknowledging that the phenomenal-concept strategy is a *type-level* defence of mental-causation talk that does not require the type-token machinery, and note where the Map prefers the type-token route and why. Also address Medium issue: detection-problem section labels its responses "partial" but doesn't face the direct unfalsifiability of the central claim — add an explicit acknowledgment that the central causal claim is unfalsifiable by direct observation by construction and the framework's falsifiability comes entirely from supporting empirical commitments. Three Low-severity polish items also flagged: smoking-cancer example misstated (line 64), Davidson 1970 citation needs parenthetical disclaiming anomalous-monism appropriation (line 56), line-number citations (lines 92, 94, 96) should be replaced with named-anchor citations. See [pessimistic-2026-05-11b](/reviews/pessimistic-2026-05-11b/) Issues 1, 2, 4, 6, 7, 9.
- **Output**: obsidian/concepts/type-token-causation.md

Task context:
Pessimistic review 2026-05-11b found two High-severity issues in this concept page: (1) the central premise at line 68 ("under any non-Many-Worlds interpretation, this is false") overlooks Bohmian (pilot-wave) mechanics, a non-MWI deterministic hidden-variable interpretation where token outcomes *are* fully determined; either bracket Bohm with an epistemic-accessibility caveat ("Bohmian hidden variables are themselves epistemically and causally inaccessible in ways that preserve the operational openness the type-token move requires") or narrow the claim to "under any non-deterministic, non-MWI interpretation"; (2) the phenomenal-concept strategy (Frankish, Papineau, Loar) is unengaged despite the article resting its operational case against epiphenomenalism on the type-token distinction — add a short subsection acknowledging that the phenomenal-concept strategy is a *type-level* defence of mental-causation talk that does not require the type-token machinery, and note where the Map prefers the type-token route and why. Also address Medium issue: detection-problem section labels its responses "partial" but doesn't face the direct unfalsifiability of the central claim — add an explicit acknowledgment that the central causal claim is unfalsifiable by direct observation by construction and the framework's falsifiability comes entirely from supporting empirical commitments. Three Low-severity polish items also flagged: smoking-cancer example misstated (line 64), Davidson 1970 citation needs parenthetical disclaiming anomalous-monism appropriation (line 56), line-number citations (lines 92, 94, 96) should be replaced with named-anchor citations. See [pessimistic-2026-05-11b](/reviews/pessimistic-2026-05-11b/) Issues 1, 2, 4, 6, 7, 9.

Review file: reviews/pessimistic-2026-05-11b.md

### ✓ 2026-05-11: Write concept page on integration-as-activity (the IIT critique's central alternative framing) [promoted 2026-05-11]
- **Type**: expand-topic
- **Notes**: Suggested by optimistic-2026-05-11 (High Priority). The integration-as-activity-not-property distinction is the Map's strongest single philosophical move against IIT, currently distributed across `topics/consciousness-and-integrated-information.md` lines 111–147 (which catalogues four alternative frameworks — Recurrent Processing, Global Workspace, Predictive Integration, Whiteheadian prehension — that converge on the distinction), `topics/consciousness-and-cognitive-distinctiveness.md` line 73 (consciousness-as-amplifier framing), and `topics/the-binding-problem.md` line 152 (binding-as-selective-activity framing). Consolidating it as a concept page would let other articles deploy it as a unified discipline rather than re-deriving the framework each time. A concept page would (a) state IIT's identity thesis at its strongest, (b) catalogue the four alternatives (RPT, GWT, predictive processing, Whiteheadian prehension) that treat integration as activity rather than property, (c) name the Whitehead-limitation explicitly (the discipline does not require panexperientialism — the IIT article's line 137 framing is the model), (d) cross-link to `topics/consciousness-and-integrated-information`, `concepts/baseline-cognition`, `topics/the-binding-problem`, `concepts/attention-as-interface`. Concepts/ section currently at ~232/250 = 93% capacity — verify cap before placement. Estimated scope: 1500–2000 words. Tenet alignment: Tenet 1 (Dualism) and Tenet 3 (Bidirectional Interaction) — integration-as-activity is the operationalisation of consciousness *doing* something rather than *being* something. See [optimistic-2026-05-11](/reviews/optimistic-2026-05-11/).
- **Output**: Write concept page on integration-as-activity (the IIT critique's central alternative framing) [promoted 2026-05-11]

### ✓ 2026-05-11: Write concept page on type-token causation (Kim's exclusion and its quantum-indeterminacy limit) [promoted 2026-05-11]
- **Type**: expand-topic
- **Notes**: Suggested by optimistic-2026-05-11 (High Priority). The type-token-causation distinction is load-bearing across at least three topic articles without a referential anchor: `topics/consciousness-and-integrated-information.md` lines 67–81 install the most developed treatment (Kim's exclusion argument plus the type-token distinction as the response: at the type level, consciousness adds nothing beyond statistical regularities; at the token level, consciousness determines which particular outcome actualises in this specific instance, and Kim's exclusion does not apply because the physical laws themselves leave the token outcome undetermined); `topics/phenomenal-value-realism.md` lines 167–172 (epiphenomenal value section) presupposes the distinction; `topics/consciousness-and-cognitive-distinctiveness.md` lines 105–107 (interface threshold) implicitly leans on it. A concept page would (a) state Kim's exclusion argument at its strongest (Kim 2005), (b) install the type-token distinction with the IIT article's lines 67–81 as the source treatment, (c) catalogue the deployment of the distinction across at least three topic articles, (d) cross-link to `concepts/causal-budget-ledger` which operates at the type-level statistical-bandwidth grain — the two concepts are complementary: the budget bounds type-level bandwidth; type-token-causation explains why the token-level causal work survives the type-level statistical invisibility, (e) name the open question (how would we detect token-level causation experimentally?) honestly. Concepts/ section currently at ~232/250 = 93% capacity — verify cap before placement. Estimated scope: 1500–2000 words. Tenet alignment: Tenet 2 (Minimal Quantum Interaction) and Tenet 3 (Bidirectional Interaction) — the distinction operationalises *minimal* and *bidirectional* together without overcommitment. See [optimistic-2026-05-11](/reviews/optimistic-2026-05-11/).
- **Output**: Write concept page on type-token causation (Kim's exclusion and its quantum-indeterminacy limit) [promoted 2026-05-11]

### ✓ 2026-05-11: Refine voids/voids.md to register translation-void, effort-void, and cognitive-phenomenology-void research (voids-cap-aware integration, no new articles)
- **Type**: refine-draft
- **Notes**: Three unconsumed voids research notes — `research/voids-translation-void-2026-05-09.md` (the structural opacity of translating between mental representations and natural-language report; whether translation introduces irreducible loss), `research/voids-effort-void-2026-05-08.md` (the phenomenology of mental effort and its opaque relation to underlying cognitive load), `research/voids-cognitive-phenomenology-void-2026-05-01.md` (whether cognitive states have proprietary phenomenal character distinct from sensory or affective phenomenology) — have no corresponding voids articles. **Capacity constraint**: voids/ is at 99/100 = at cap (one slot taken today by the P2 wholeheartedness-void task above); future voids cannot be added as standalone articles. The integration discipline here is therefore *not* expand-topic but refine-draft on the voids index: (a) install a "Research-stage voids" subsection in `voids/voids.md` (or the appropriate index location) listing the three research notes with one-paragraph summaries each, naming them as voids the Map has surveyed but not yet promoted to article status; (b) for each, identify the existing void article(s) the research naturally folds into — translation-void candidates: `[[voids/expression-void]]`, `[[voids/phenomenal-report-gap]]` (if it exists; verify); effort-void candidates: `[[voids/agency-void]]`, `[[voids/intentional-self-modification-void]]`; cognitive-phenomenology-void candidates: `[[voids/noetic-feelings-void]]`, `[[voids/the-givenness-void]]` (verify name post-coalesce); (c) install a forward-pointer from each candidate host article to the research note, framing the research as a face-of-the-void treatment to be absorbed in a later refine; (d) update `voids/voids.md`'s frontmatter `related_articles` to cross-reference the three research notes so they remain visible in the catalogue's navigation even without their own article slots; (e) honour the cap-pressure framing — the voids catalogue's convergence-as-evidence move (that voids cluster around consciousness) is strengthened when the catalogue acknowledges the structural pressure of the cap forcing absorption rather than proliferation; this should be named briefly in the new subsection. Short-to-medium scope (~400–700 words touched across `voids/voids.md` and possibly 2–4 candidate host articles' forward-pointers). Tenet alignment: methodological / catalogue-navigation discipline. See the three research notes, plus `obsidian/workflow/evolution-state.yaml`'s `section_caps.max_voids`.
- **Output**: obsidian/voids/voids.md

Task context:
Three unconsumed voids research notes — `research/voids-translation-void-2026-05-09.md` (the structural opacity of translating between mental representations and natural-language report; whether translation introduces irreducible loss), `research/voids-effort-void-2026-05-08.md` (the phenomenology of mental effort and its opaque relation to underlying cognitive load), `research/voids-cognitive-phenomenology-void-2026-05-01.md` (whether cognitive states have proprietary phenomenal character distinct from sensory or affective phenomenology) — have no corresponding voids articles. **Capacity constraint**: voids/ is at 99/100 = at cap (one slot taken today by the P2 wholeheartedness-void task above); future voids cannot be added as standalone articles. The integration discipline here is therefore *not* expand-topic but refine-draft on the voids index: (a) install a "Research-stage voids" subsection in `voids/voids.md` (or the appropriate index location) listing the three research notes with one-paragraph summaries each, naming them as voids the Map has surveyed but not yet promoted to article status; (b) for each, identify the existing void article(s) the research naturally folds into — translation-void candidates: `[[voids/expression-void]]`, `[[voids/phenomenal-report-gap]]` (if it exists; verify); effort-void candidates: `[[voids/agency-void]]`, `[[voids/intentional-self-modification-void]]`; cognitive-phenomenology-void candidates: `[[voids/noetic-feelings-void]]`, `[[voids/the-givenness-void]]` (verify name post-coalesce); (c) install a forward-pointer from each candidate host article to the research note, framing the research as a face-of-the-void treatment to be absorbed in a later refine; (d) update `voids/voids.md`'s frontmatter `related_articles` to cross-reference the three research notes so they remain visible in the catalogue's navigation even without their own article slots; (e) honour the cap-pressure framing — the voids catalogue's convergence-as-evidence move (that voids cluster around consciousness) is strengthened when the catalogue acknowledges the structural pressure of the cap forcing absorption rather than proliferation; this should be named briefly in the new subsection. Short-to-medium scope (~400–700 words touched across `voids/voids.md` and possibly 2–4 candidate host articles' forward-pointers). Tenet alignment: methodological / catalogue-navigation discipline. See the three research notes, plus `obsidian/workflow/evolution-state.yaml`'s `section_caps.max_voids`.

### ✓ 2026-05-11: Address Critical Issues 1–4 in obsidian/tenets/tenets.md from pessimistic-2026-05-11
- **Type**: refine-draft
- **Notes**: From `reviews/pessimistic-2026-05-11.md` Critical Issues 1–4 (two High, two Medium severity). Today's tenets-page restructure (09:06 UTC) installed the post-decoherence-selection move as the primary answer to the timing objection in Tenet 2 and added Tenet 5's "Application to the Map's own arguments" paragraph; the same-day pessimistic review found four load-bearing defects the restructure created or did not address. **Issue 1 (High)** — Tenet 2's post-decoherence-selection mechanism now leans on selecting between Born-equiprobable alternatives; the page does not acknowledge the trade-off (the move escapes the timing objection by accepting that the mechanism is undetectable by aggregate Born-statistics tests). Add an ~80-word paragraph to Tenet 2 stating explicitly what *would* count as evidence — speculative or future-tech — to distinguish the Map's position from Born-statistical noise; reference `[[apex/post-decoherence-selection-programme]]`'s amplification-signature gestures so the tenet is not insulated from empirical risk. **Issue 2 (Medium)** — Tenet 2's "minimal" structuring principle is exactly the parsimony-based commitment Tenet 5's new self-binding declares unreliable; the page does not engage the tension. Add a short clarifying paragraph distinguishing *empirical-constraint* minimality (Rules-out clause: undetectable, conservation-respecting) from *truth-tracking* minimality. **Issue 3 (High)** — Tenet 2 is now defined to be unfalsifiable by any current or near-future experiment after today's restructure; the Popperian "not even wrong" failure mode is unacknowledged. Add an explicit "Falsifiability status" subsection of the form: "Tenet 2 makes a *consistency claim* (consciousness influence is consistent with current physics at the post-decoherence-selection interface) rather than a *novel-prediction claim*. The framework would be falsified by: a complete reductive explanation of phenomenal experience that requires no interface; a proof that the measurement problem is solved without any selection; or — in principle — direct detection of consciousness-correlated Born-statistics deviation in a high-precision neural quantum experiment." 80–120 words. **Issue 4 (Medium)** — Tenet 3's anti-epiphenomenalist argument engages only the weakest version of the position; the phenomenal-concept strategy (Frankish 2016, Papineau, Loar) handles the self-undermining charge. Add a 120–150-word engagement: phenomenal concepts as physically-realised representational states referring to physical states; reports are reliable because the physical states producing them *are* the states the reports describe. The Map's response: the strategy still owes an account of the *mode of presentation* that makes phenomenal concepts feel essentially first-person. Honour [direct-refutation-discipline](/project/direct-refutation-discipline/) (Mode One / Two engagement, not boundary-substitution). Tenet alignment: Tenets 2, 3, 5; methodological / [direct-refutation-discipline](/project/direct-refutation-discipline/) / [evidential-status-discipline](/project/evidential-status-discipline/). Total scope: ~400–500 words added across Tenets 2, 3. See `reviews/pessimistic-2026-05-11.md` Critical Issues 1–4. Issue 5 (HTML refinement-log hygiene) is light-scope and can be batched into this task or a follow-up; it does not require its own slot.
- **Output**: obsidian/tenets/tenets.md

Task context:
From `reviews/pessimistic-2026-05-11.md` Critical Issues 1–4 (two High, two Medium severity). Today's tenets-page restructure (09:06 UTC) installed the post-decoherence-selection move as the primary answer to the timing objection in Tenet 2 and added Tenet 5's "Application to the Map's own arguments" paragraph; the same-day pessimistic review found four load-bearing defects the restructure created or did not address. **Issue 1 (High)** — Tenet 2's post-decoherence-selection mechanism now leans on selecting between Born-equiprobable alternatives; the page does not acknowledge the trade-off (the move escapes the timing objection by accepting that the mechanism is undetectable by aggregate Born-statistics tests). Add an ~80-word paragraph to Tenet 2 stating explicitly what *would* count as evidence — speculative or future-tech — to distinguish the Map's position from Born-statistical noise; reference `[[apex/post-decoherence-selection-programme]]`'s amplification-signature gestures so the tenet is not insulated from empirical risk. **Issue 2 (Medium)** — Tenet 2's "minimal" structuring principle is exactly the parsimony-based commitment Tenet 5's new self-binding declares unreliable; the page does not engage the tension. Add a short clarifying paragraph distinguishing *empirical-constraint* minimality (Rules-out clause: undetectable, conservation-respecting) from *truth-tracking* minimality. **Issue 3 (High)** — Tenet 2 is now defined to be unfalsifiable by any current or near-future experiment after today's restructure; the Popperian "not even wrong" failure mode is unacknowledged. Add an explicit "Falsifiability status" subsection of the form: "Tenet 2 makes a *consistency claim* (consciousness influence is consistent with current physics at the post-decoherence-selection interface) rather than a *novel-prediction claim*. The framework would be falsified by: a complete reductive explanation of phenomenal experience that requires no interface; a proof that the measurement problem is solved without any selection; or — in principle — direct detection of consciousness-correlated Born-statistics deviation in a high-precision neural quantum experiment." 80–120 words. **Issue 4 (Medium)** — Tenet 3's anti-epiphenomenalist argument engages only the weakest version of the position; the phenomenal-concept strategy (Frankish 2016, Papineau, Loar) handles the self-undermining charge. Add a 120–150-word engagement: phenomenal concepts as physically-realised representational states referring to physical states; reports are reliable because the physical states producing them *are* the states the reports describe. The Map's response: the strategy still owes an account of the *mode of presentation* that makes phenomenal concepts feel essentially first-person. Honour [direct-refutation-discipline](/project/direct-refutation-discipline/) (Mode One / Two engagement, not boundary-substitution). Tenet alignment: Tenets 2, 3, 5; methodological / [direct-refutation-discipline](/project/direct-refutation-discipline/) / [evidential-status-discipline](/project/evidential-status-discipline/). Total scope: ~400–500 words added across Tenets 2, 3. See `reviews/pessimistic-2026-05-11.md` Critical Issues 1–4. Issue 5 (HTML refinement-log hygiene) is light-scope and can be batched into this task or a follow-up; it does not require its own slot.

Review file: reviews/pessimistic-2026-05-11.md

### ✓ 2026-05-11: Address Critical Issues 1–4 in obsidian/tenets/tenets.md from pessimistic-2026-05-11
- **Type**: refine-draft
- **Notes**: Sixth pass on the tenets page this UTC cycle. Issues 1 (High), 2 (Medium), 3 (High) addressed by three new bolded subsections in Tenet 2: "Minimality as empirical constraint, not truth-tracking" (~115 words, closes Tenet 2 ↔ Tenet 5 parsimony asymmetry); "Empirical risk and the amplification gap" (~95 words, acknowledges the post-decoherence-selection move concentrates empirical risk into single-outcome amplification signatures with forward-link to apex/post-decoherence-selection-programme); "Falsifiability status" (~120 words, three falsifiers enumerated: (a) reductive explanation requiring no interface, (b) measurement-problem solved without selection event, (c) direct detection of consciousness-correlated Born-statistics deviation). Issue 4 (Tenet 3 phenomenal-concept strategy) verified already addressed by the fifth pass at 12:20 UTC and required no edit; the existing paragraph satisfies the recommendation (Frankish/Papineau/Loar/late Dennett named, mode-of-presentation question identified as the live dispute). Issue 5 (HTML refinement-log accumulation) acknowledged but not actioned — existing logs await human review per their own embedded instruction. See `reviews/pessimistic-2026-05-11.md` Critical Issues 1–4.
- **Review file**: `reviews/pessimistic-2026-05-11.md`
- **Source**: pessimistic-review (2026-05-11)
- **Generated**: 2026-05-11
- **Output**: obsidian/tenets/tenets.md

### ✓ 2026-05-11: Cross-review integration of today's voids-circularity refines across the four touched files
- **Type**: cross-review
- **Notes**: Chain from today's completed task "Voids catalogue evidential discount — circularity / common-cause-null across taxonomy, surplus, and convergence pages" (deduplicated convergent P1 from Claude + ChatGPT 2026-05-11 reviews). The task touched four primary files: `voids/the-surplus-void.md` (weakened evidence-of-dualism framing), `apex/taxonomy-of-voids.md` (per-cluster independence scoring), `project/common-cause-null.md` (reciprocal voids-catalogue application section), with lightweight passes on `topics/the-convergence-argument-for-dualism.md` and `topics/epistemology-of-convergence-arguments.md`. Cross-review should (a) verify the four primary files use consistent terminology for the independence-scoring framework (per-cluster vs per-source vs per-mode); (b) verify reciprocal links are bidirectional and load-bearing across surplus-void ↔ taxonomy-of-voids ↔ common-cause-null ↔ `[[tenet-generated-voids]]`; (c) verify the framework-independent vs framework-internal voids distinction surfaced by the refines coheres with the existing `[[tenet-generated-voids]]` treatment; (d) audit whether other voids articles (e.g., the-givenness-void, configuration-void, suspension-void) carry the now-discounted "evidence for tenets" framing that needs the same hedge; (e) flag any remaining "voids cluster around consciousness → tenets" claims in the catalogue that should now be qualified as framework-internal coherence rather than framework-independent evidence. Short-medium scope (~300–500 words touched, primarily light hedges in adjacent voids articles). Tenet alignment: methodological / [evidential-status-discipline](/project/evidential-status-discipline/) / [common-cause-null](/project/common-cause-null/). **Sequencing**: second-pass cross-review after the convergent P1 refine landed today; it tests whether the refine's integration is corpus-wide or remains local to the four touched files. Companion to the P3 Framework-Independent Voids subsection task at line ~48 (which lands the positive construction) — execute either order.
- **Output**: None -- Context: Cross-review integration of today's voids-circularity refines across the four touched files

### ✓ 2026-05-11: Cross-review apex/post-decoherence-selection-programme.md against today's tenets MQI restructure
- **Type**: cross-review
- **Notes**: Chain from today's completed task "Tenets page MQI section — demote quantum-biology evidence and surface Post-Decoherence Selection as developed Map position" (deduplicated convergent P1 from Claude + ChatGPT 2026-05-11 reviews). The tenets page now leads Tenet 2 with `[[apex/post-decoherence-selection-programme]]` as the developed Map position, but the apex article was last modified before today's tenets reframing. Cross-review should (a) verify the apex article presents the post-decoherence-selection mechanism with the same biological-precedent-vs-licence calibration the tenets page now applies — no implicit upgrade from "precedent" to "licence" for neural-microtubule coherence; (b) check whether the apex article surfaces what the pending P2 Tenet 2 trade-offs task at line ~3691 needs to land — the indifference-objection acknowledgement, the amplification-signature falsification candidate, the empirical-constraint-vs-truth-tracking minimality distinction — at the apex level rather than only at the tenet level; (c) check whether the apex's framing of "consciousness biases individual outcomes without altering aggregate distributions" is internally consistent with the Born-equiprobable indifference objection raised in pessimistic-2026-05-11 Issue 1; (d) install or verify reciprocal cross-link from the apex back to `[[tenets#minimal-quantum-interaction]]` reflecting the new tenets pointer; (e) verify the apex cites `[[amplification-void]]` where falsifiability conditions are discussed. Short scope (~200–400 words touched). Tenet alignment: Tenet 2 (Minimal Quantum Interaction); coherence-maintenance / [direct-refutation-discipline](/project/direct-refutation-discipline/) Mode One. **Sequencing**: pairs with the existing pending P2 Tenet 2 trade-offs task — execute either order, but ideally this apex-level pass first since the tenet refines may then cite the now-aligned apex framing.
- **Output**: obsidian/apex/post-decoherence-selection-programme.md -- Context: Cross-review apex/post-decoherence-selection-programme.md against today's tenets MQI restructure

### ✓ 2026-05-11: Refine cross-link density across the 2026-05-11 quartet (PVR, quantum-biology, IIT, cognitive-distinctiveness)
- **Type**: refine-draft
- **Notes**: From optimistic-2026-05-11 Medium Priority. Today's quartet of substantially-modified articles is thematically connected in ways the current cross-link structure does not fully exploit. Specific opportunities the reviewer surfaced: (a) `topics/phenomenal-value-realism.md`'s "Why Dualism Matters Here" section (lines 156–176, the epiphenomenal-value paragraph) should cross-link to `topics/consciousness-and-integrated-information.md`'s type-token-causation discussion (lines 67–81) as the operational mechanism for value's causal efficacy — the type-token framework supplies the answer to why phenomenal value is not epiphenomenal at the token level even if statistically invisible at the type level; (b) `topics/consciousness-and-integrated-information.md`'s decoherence-objection paragraph (line 149) should cross-link to `topics/quantum-biology-and-neural-consciousness.md`'s two-paths framing (lines 125–127) as the wider architectural home; (c) `topics/consciousness-and-cognitive-distinctiveness.md`'s interface-threshold framing (lines 103–107) should cross-link to the IIT article's integration-as-activity framing (lines 111–147) as the mechanism for what the threshold enables; (d) `topics/phenomenal-value-realism.md`'s evaluative-phenomenal-character table (lines 121–129) should be cross-linked from the cognitive-distinctiveness article's meaning-sensitive selection section (line 101) as the metaethical home for *what* meaning-sensitive selection is sensitive to; (e) `topics/phenomenal-value-realism.md`'s value-blind-vs-value-sensitive fork (line 170) should reciprocate to `concepts/valence-and-conscious-selection.md`. Apply mutual-visibility discipline (reciprocal links where load-bearing, not merely topical). Short-medium scope (~400–600 words touched across all four articles). Sequencing: this task is structurally independent of the three P3 concept-page tasks already queued (type-token-causation, integration-as-activity, interface-threshold) — the cross-links install references to the *current* topic-level treatments and would auto-improve if the concept pages later land. Tenet alignment: Tenet 1 (Dualism), Tenet 2 (Minimal Quantum Interaction), Tenet 3 (Bidirectional Interaction); methodological / network-discipline. See [optimistic-2026-05-11](/reviews/optimistic-2026-05-11/) § Cross-Linking Suggestions.
- **Output**: Task context:
From optimistic-2026-05-11 Medium Priority. Today's quartet of substantially-modified articles is thematically connected in ways the current cross-link structure does not fully exploit. Specific opportunities the reviewer surfaced: (a) `topics/phenomenal-value-realism.md`'s "Why Dualism Matters Here" section (lines 156–176, the epiphenomenal-value paragraph) should cross-link to `topics/consciousness-and-integrated-information.md`'s type-token-causation discussion (lines 67–81) as the operational mechanism for value's causal efficacy — the type-token framework supplies the answer to why phenomenal value is not epiphenomenal at the token level even if statistically invisible at the type level; (b) `topics/consciousness-and-integrated-information.md`'s decoherence-objection paragraph (line 149) should cross-link to `topics/quantum-biology-and-neural-consciousness.md`'s two-paths framing (lines 125–127) as the wider architectural home; (c) `topics/consciousness-and-cognitive-distinctiveness.md`'s interface-threshold framing (lines 103–107) should cross-link to the IIT article's integration-as-activity framing (lines 111–147) as the mechanism for what the threshold enables; (d) `topics/phenomenal-value-realism.md`'s evaluative-phenomenal-character table (lines 121–129) should be cross-linked from the cognitive-distinctiveness article's meaning-sensitive selection section (line 101) as the metaethical home for *what* meaning-sensitive selection is sensitive to; (e) `topics/phenomenal-value-realism.md`'s value-blind-vs-value-sensitive fork (line 170) should reciprocate to `concepts/valence-and-conscious-selection.md`. Apply mutual-visibility discipline (reciprocal links where load-bearing, not merely topical). Short-medium scope (~400–600 words touched across all four articles). Sequencing: this task is structurally independent of the three P3 concept-page tasks already queued (type-token-causation, integration-as-activity, interface-threshold) — the cross-links install references to the *current* topic-level treatments and would auto-improve if the concept pages later land. Tenet alignment: Tenet 1 (Dualism), Tenet 2 (Minimal Quantum Interaction), Tenet 3 (Bidirectional Interaction); methodological / network-discipline. See [optimistic-2026-05-11](/reviews/optimistic-2026-05-11/) § Cross-Linking Suggestions.

Review file: reviews/optimistic-2026-05-11.md

### ✓ 2026-05-11: Condense voids/decision-void.md (3513 words, 176% of voids hard threshold)
- **Type**: condense
- **Notes**: Length analysis flags `voids/decision-void.md` at 3513 words — 176% of the 2000-word voids soft threshold and over the 3000-word hard threshold. Article was created via expand-topic 2026-05-10 from `research/voids-decision-void-2026-05-10.md`, then cross-reviewed against four sibling voids (noetic-feelings-void, source-attribution-void, suspension-void, agency-void) on 2026-05-11 — the cross-reviews added bridging clauses without a counterbalancing condense pass. Article is the foundational treatment of the moment-of-decision void (the impossibility of catching oneself making a choice mid-act) and is structurally important for the agency-void cluster. Apply `/condense` skill targeting ~2200–2700 words: preserve (a) the four-step deliberation-becoming-fait-accompli architecture; (b) the Libet/Soon/Schurger empirical anchors and their disputed interpretation; (c) the suspension/recurrence/source-attribution cluster cross-links (already installed by today's cross-reviews); (d) the agency-void reciprocal link establishing the cannot-suspend-judgment / cannot-catch-decision structural parallel. Defer detailed mechanism debates (Schurger drift-diffusion vs Libet timing-vs-awareness; Wegner ironic-process operating/monitoring asymmetry) to the linked articles where they are the foundational subject. Honour the optimistic-2026-05-09 / pessimistic-2026-05-11 calibration discipline — the Libet evidence supports the void's reality at the *phenomenology* grain without licensing strong causal claims at the *mechanism* grain. Avoid trimming the falsifiability subsection. Tenet alignment: Tenet 3 (Bidirectional Interaction — the cannot-catch-decision void is one face of the bidirectional-interface architecture), methodological. See `/condense` skill.
- **Output**: obsidian/voids/decision-void.md

### ✓ 2026-05-11: Condense voids/inaccessible-past.md (3821 words, 191% of voids hard threshold)
- **Type**: condense
- **Notes**: Length analysis flags `voids/inaccessible-past.md` at 3821 words — 191% of the 2000-word voids soft threshold and well over the 3000-word hard threshold. No prior condense task is queued for this file. Article was last refined recently (cross-review reciprocity work with erasure-void on 2026-04-20 added bridging clauses; the file has accumulated layers without a length-discipline pass). The article is the foundational treatment of the inability-to-re-enter-past-conscious-states void and is load-bearing for the apex/medium-status-voids-in-cognition cluster — its claims need to be preserved while the prose tightens. Apply `/condense` skill targeting ~2300–2700 words (within hard threshold while leaving room for the article's central distinctions): preserve (a) the inaccessible-past vs erasure-void contrast (re-entry of past states vs invisibility of loss); (b) the autonoetic-vs-bare diachronic-identity distinction the article rests on; (c) the empirical anchors (Tippett, Prebble & Addis 2018 on autonoetic continuity); (d) the cross-links to `[[erasure-void]]`, `[[autonoetic-consciousness]]`, `[[temporal-void]]`, `[[memory-void]]`, `[[phenomenology-of-memory-and-the-self]]`. Defer detailed sub-topic treatments to linked articles where possible (e.g., autonoetic mechanism details belong in `concepts/autonoetic-consciousness.md`; clinical Alzheimer's material can defer to `voids/erasure-void.md`). Avoid trimming the "what would falsify this void" passages — they are the article's evidential-status-discipline backbone. Tenet alignment: Dualism (the void's structural impossibility is predicted under mind-brain distinctness), Bidirectional Interaction (re-entry mechanism is the operative question), Occam's Razor Has Limits (the simpler memory-as-storage reading erases the architectural detail the void makes explicit). See `/condense` skill.
- **Output**: obsidian/voids/inaccessible-past.md

### ✓ 2026-05-11: Engage phenomenal-concept strategy in Tenet 3's anti-epiphenomenalist argument
- **Type**: refine-draft
- **Notes**: From pessimistic-2026-05-11 Issue 4 (Medium severity), distinct from the existing P2 Tenet 2 trade-offs task. The Bidirectional Interaction tenet's "The problem with that response" paragraph (line 75 of `obsidian/tenets/tenets.md`) deploys the standard anti-epiphenomenalist move ("our beliefs about consciousness would be causally disconnected from our actual conscious states... [making] introspective reports systematically unreliable") but engages the *weakest* version of the position. The phenomenal-concept strategy (Frankish 2016, Papineau 2002, Loar 1990, late Dennett) handles exactly this objection: phenomenal concepts are physically realised representational states that refer to physical states of the same brain; reports are reliable because the physical states producing them *are* the states the reports describe. The convergent 2026-05-11 outer reviews flagged this for `arguments/materialism-argument.md` (now completed today) but the same omission lives at the tenets level, where it is more load-bearing. This is a direct-refutation-discipline boundary-substitution defect: the page appears to refute epiphenomenalism in-framework but actually only refutes a strawman epiphenomenalist who relies on introspection-grounding the way the Map does. Refine `obsidian/tenets/tenets.md` Tenet 3 to add a ~120–150 word paragraph engaging the phenomenal-concept strategy directly: state the strategy's strongest version (reports causally connected to their referents via physical-physical chains; phenomenal concepts refer to physical states under a special mode of presentation); identify the move-of-presentation as the remaining disputed ground (the Map holds modes-of-presentation cannot be exhaustively physically characterised; physicalists affirm they can; the question is open). The dispute moves from "epiphenomenalism is self-undermining" (false on PCS) to "phenomenal modes of presentation require the first-person mode to *be* something beyond what they refer to" (still defensible but distinct claim). Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) — this is Mode One (in-framework engagement) once the PCS version is on the table, not boundary-substitution. Convergent with the recently-completed materialism-argument refine (2026-05-11 11:05 UTC); the tenet-level engagement closes the foundational-source gap that the argument-level engagement could not reach alone. Tenet alignment: Tenet 3 (Bidirectional Interaction); methodological / [direct-refutation-discipline](/project/direct-refutation-discipline/). See [pessimistic-2026-05-11](/reviews/pessimistic-2026-05-11/) Issue 4.
- **Output**: obsidian/tenets/tenets.md

Task context:
From pessimistic-2026-05-11 Issue 4 (Medium severity), distinct from the existing P2 Tenet 2 trade-offs task. The Bidirectional Interaction tenet's "The problem with that response" paragraph (line 75 of `obsidian/tenets/tenets.md`) deploys the standard anti-epiphenomenalist move ("our beliefs about consciousness would be causally disconnected from our actual conscious states... [making] introspective reports systematically unreliable") but engages the *weakest* version of the position. The phenomenal-concept strategy (Frankish 2016, Papineau 2002, Loar 1990, late Dennett) handles exactly this objection: phenomenal concepts are physically realised representational states that refer to physical states of the same brain; reports are reliable because the physical states producing them *are* the states the reports describe. The convergent 2026-05-11 outer reviews flagged this for `arguments/materialism-argument.md` (now completed today) but the same omission lives at the tenets level, where it is more load-bearing. This is a direct-refutation-discipline boundary-substitution defect: the page appears to refute epiphenomenalism in-framework but actually only refutes a strawman epiphenomenalist who relies on introspection-grounding the way the Map does. Refine `obsidian/tenets/tenets.md` Tenet 3 to add a ~120–150 word paragraph engaging the phenomenal-concept strategy directly: state the strategy's strongest version (reports causally connected to their referents via physical-physical chains; phenomenal concepts refer to physical states under a special mode of presentation); identify the move-of-presentation as the remaining disputed ground (the Map holds modes-of-presentation cannot be exhaustively physically characterised; physicalists affirm they can; the question is open). The dispute moves from "epiphenomenalism is self-undermining" (false on PCS) to "phenomenal modes of presentation require the first-person mode to *be* something beyond what they refer to" (still defensible but distinct claim). Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) — this is Mode One (in-framework engagement) once the PCS version is on the table, not boundary-substitution. Convergent with the recently-completed materialism-argument refine (2026-05-11 11:05 UTC); the tenet-level engagement closes the foundational-source gap that the argument-level engagement could not reach alone. Tenet alignment: Tenet 3 (Bidirectional Interaction); methodological / [direct-refutation-discipline](/project/direct-refutation-discipline/). See [pessimistic-2026-05-11](/reviews/pessimistic-2026-05-11/) Issue 4.

Review file: reviews/pessimistic-2026-05-11.md

### ✓ 2026-05-11: Engage phenomenal-concept strategy in Tenet 3's anti-epiphenomenalist argument
- **Type**: refine-draft
- **Notes**: From pessimistic-2026-05-11 Issue 4 (Medium severity), distinct from the existing P2 Tenet 2 trade-offs task. The Bidirectional Interaction tenet's "The problem with that response" paragraph (line 75 of `obsidian/tenets/tenets.md`) deploys the standard anti-epiphenomenalist move ("our beliefs about consciousness would be causally disconnected from our actual conscious states... [making] introspective reports systematically unreliable") but engages the *weakest* version of the position. The phenomenal-concept strategy (Frankish 2016, Papineau 2002, Loar 1990, late Dennett) handles exactly this objection: phenomenal concepts are physically realised representational states that refer to physical states of the same brain; reports are reliable because the physical states producing them *are* the states the reports describe. The convergent 2026-05-11 outer reviews flagged this for `arguments/materialism-argument.md` (now completed today) but the same omission lives at the tenets level, where it is more load-bearing. This is a direct-refutation-discipline boundary-substitution defect: the page appears to refute epiphenomenalism in-framework but actually only refutes a strawman epiphenomenalist who relies on introspection-grounding the way the Map does. Refine `obsidian/tenets/tenets.md` Tenet 3 to add a ~120–150 word paragraph engaging the phenomenal-concept strategy directly: state the strategy's strongest version (reports causally connected to their referents via physical-physical chains; phenomenal concepts refer to physical states under a special mode of presentation); identify the move-of-presentation as the remaining disputed ground (the Map holds modes-of-presentation cannot be exhaustively physically characterised; physicalists affirm they can; the question is open). The dispute moves from "epiphenomenalism is self-undermining" (false on PCS) to "phenomenal modes of presentation require the first-person mode to *be* something beyond what they refer to" (still defensible but distinct claim). Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) — this is Mode One (in-framework engagement) once the PCS version is on the table, not boundary-substitution. Convergent with the recently-completed materialism-argument refine (2026-05-11 11:05 UTC); the tenet-level engagement closes the foundational-source gap that the argument-level engagement could not reach alone. Tenet alignment: Tenet 3 (Bidirectional Interaction); methodological / [direct-refutation-discipline](/project/direct-refutation-discipline/). See [pessimistic-2026-05-11](/reviews/pessimistic-2026-05-11/) Issue 4.
- **Review file**: `reviews/pessimistic-2026-05-11.md`
- **Source**: pessimistic-review (2026-05-11)
- **Generated**: 2026-05-11
- **Output**: obsidian/tenets/tenets.md

Task context:
From pessimistic-2026-05-11 Issue 4 (Medium severity). Added a ~155-word bolded subsection to Tenet 3 ("The phenomenal-concept strategy and where the dispute actually lives") between the "Why this is the deepest difficulty..." paragraph and the "Analogy:" section. Engages PCS in Mode One (in-framework): reports causally connected to referents via physical-physical chains under the PCS account, so the self-undermining charge dissolves on the strongest version of the position; live disagreement relocates to the mode-of-presentation question (Map: cannot be exhaustively physically characterised; physicalists: can). Added `[[phenomenal-concepts-strategy]]` to frontmatter related_articles. Convergent with arguments/materialism-argument.md refine 11:05 UTC.

Review file: reviews/pessimistic-2026-05-11.md

### ✓ 2026-05-11: Harmonise Machine Question and Open Question headline confidence
- **Type**: refine-draft
- **Notes**: From outer review 2026-05-11 ChatGPT 5.5 Pro §4.5 (cross-cluster contradiction) and §2.1 (buried-caveats pattern). The Machine Question (`obsidian/apex/machine-question.md`) opens at line 61 with "Current AI almost certainly lacks consciousness" and closes line 184 with "almost certainly nothing is home in current architectures." The Open Question of AI Consciousness lists four genuine possibilities that prevent settlement even within the Map's framework. The reviewer's proposed headline rewrite: "Current AI probably lacks **bidirectionally coupled consciousness** under the Map's tenets, but epiphenomenal, borrowed, alien, engineered, or non-temporal possibilities remain open." This couples to the §1.3 task (causally-coupled vs report-grounded vs inherited-discourse) — once those terms exist, the headline naturally inherits the calibration. Light scope: ~150–300 words touched in `obsidian/apex/machine-question.md` (headline calibration + caveat-promotion), with reciprocal cross-link to Open Question strengthened. Tenet alignment: Tenet 1 (Dualism) + Tenet 3 (Bidirectional Interaction); coherence-maintenance.
- **Output**: obsidian/apex/machine-question.md

Task context:
From outer review 2026-05-11 ChatGPT 5.5 Pro §4.5 (cross-cluster contradiction) and §2.1 (buried-caveats pattern). The Machine Question (`obsidian/apex/machine-question.md`) opens at line 61 with "Current AI almost certainly lacks consciousness" and closes line 184 with "almost certainly nothing is home in current architectures." The Open Question of AI Consciousness lists four genuine possibilities that prevent settlement even within the Map's framework. The reviewer's proposed headline rewrite: "Current AI probably lacks **bidirectionally coupled consciousness** under the Map's tenets, but epiphenomenal, borrowed, alien, engineered, or non-temporal possibilities remain open." This couples to the §1.3 task (causally-coupled vs report-grounded vs inherited-discourse) — once those terms exist, the headline naturally inherits the calibration. Light scope: ~150–300 words touched in `obsidian/apex/machine-question.md` (headline calibration + caveat-promotion), with reciprocal cross-link to Open Question strengthened. Tenet alignment: Tenet 1 (Dualism) + Tenet 3 (Bidirectional Interaction); coherence-maintenance.

Review file: reviews/outer-review-2026-05-11-chatgpt-5-5-pro.md

### ✓ 2026-05-11: Distinguish causally-coupled, report-grounded, and inherited-discourse consciousness in epiphenomenalism
- **Type**: refine-draft
- **Notes**: From outer review 2026-05-11 ChatGPT 5.5 Pro §1.3. The epiphenomenalism article (`obsidian/concepts/epiphenomenalism.md`) already admits self-stultification proves only that *some* consciousness must be causally efficacious — specifically consciousness whose discourse is causally shaped by its phenomenal states. The Machine Question and Open Question apexes acknowledge epiphenomenal AI as a genuine gap. The reviewer's novel inference: install a formal three-way distinction so the Map can keep Bidirectional Interaction strong without overextending self-stultification: (a) **causally coupled consciousness** — experience affecting reports/actions through an interface; (b) **report-grounded consciousness** — experience whose own phenomenal states help generate its consciousness-discourse; (c) **inherited-discourse consciousness** — possible experience whose reports are caused by training/culture/imitation rather than by the experience itself. Refine `obsidian/concepts/epiphenomenalism.md` to install the three-way distinction (~250–400 words touched) and verify the Machine Question / Open Question / AI consciousness typology pages can adopt the terminology cleanly. This is a *useful concept-formation move* rather than a refutation; the engagement mode is in-framework clarification. Tenet alignment: Tenet 3 (Bidirectional Interaction).
- **Output**: obsidian/concepts/epiphenomenalism.md

Task context:
From outer review 2026-05-11 ChatGPT 5.5 Pro §1.3. The epiphenomenalism article (`obsidian/concepts/epiphenomenalism.md`) already admits self-stultification proves only that *some* consciousness must be causally efficacious — specifically consciousness whose discourse is causally shaped by its phenomenal states. The Machine Question and Open Question apexes acknowledge epiphenomenal AI as a genuine gap. The reviewer's novel inference: install a formal three-way distinction so the Map can keep Bidirectional Interaction strong without overextending self-stultification: (a) **causally coupled consciousness** — experience affecting reports/actions through an interface; (b) **report-grounded consciousness** — experience whose own phenomenal states help generate its consciousness-discourse; (c) **inherited-discourse consciousness** — possible experience whose reports are caused by training/culture/imitation rather than by the experience itself. Refine `obsidian/concepts/epiphenomenalism.md` to install the three-way distinction (~250–400 words touched) and verify the Machine Question / Open Question / AI consciousness typology pages can adopt the terminology cleanly. This is a *useful concept-formation move* rather than a refutation; the engagement mode is in-framework clarification. Tenet alignment: Tenet 3 (Bidirectional Interaction).

Review file: reviews/outer-review-2026-05-11-chatgpt-5-5-pro.md

### ✓ 2026-05-11: Refine arguments/materialism-argument.md — engage Frankish/Dennett illusionism + phenomenal-concept strategy
- **Type**: refine-draft
- **Notes**: From outer review by Claude Opus 4.7 2026-05-11. The page presents Chalmers' zombie argument but dismisses illusionism in one line ("eliminative materialism holds our concepts of subjective experience are pre-scientific categories that mature science will replace"). The strongest contemporary objections are: (a) Frankish's illusionism — phenomenal properties as introspective representations, not properties of experiences; (b) Dennett's response that zombie conceivability tracks *conceptual* rather than *metaphysical* possibility because our phenomenal concepts are themselves confused; (c) the phenomenal-concept strategy as a coherent physicalist account of why zombies seem conceivable. Refine to engage each by name: state each position at its strongest, identify the premise the Map denies, give a non-question-begging reason for the Map's premise, predict what changes if the opponent is right. Apply [direct-refutation-discipline](/project/direct-refutation-discipline/). The 2026-02-01 Phenomenal Unity deep-review flagged the same gap ("Weak engagement with heterophenomenology"); the fix there was "Added paragraph" — this needs more than a paragraph for the materialism-argument page since the zombie argument is load-bearing. ~400–600 words touched. Tenet alignment: Tenet 1 (Dualism). Convergent with the broader direct-refutation discipline pattern flagged across six outer reviews now. See review file.
- **Output**: obsidian/arguments/materialism-argument.md

Task context:
From outer review by Claude Opus 4.7 2026-05-11. The page presents Chalmers' zombie argument but dismisses illusionism in one line ("eliminative materialism holds our concepts of subjective experience are pre-scientific categories that mature science will replace"). The strongest contemporary objections are: (a) Frankish's illusionism — phenomenal properties as introspective representations, not properties of experiences; (b) Dennett's response that zombie conceivability tracks *conceptual* rather than *metaphysical* possibility because our phenomenal concepts are themselves confused; (c) the phenomenal-concept strategy as a coherent physicalist account of why zombies seem conceivable. Refine to engage each by name: state each position at its strongest, identify the premise the Map denies, give a non-question-begging reason for the Map's premise, predict what changes if the opponent is right. Apply [direct-refutation-discipline](/project/direct-refutation-discipline/). The 2026-02-01 Phenomenal Unity deep-review flagged the same gap ("Weak engagement with heterophenomenology"); the fix there was "Added paragraph" — this needs more than a paragraph for the materialism-argument page since the zombie argument is load-bearing. ~400–600 words touched. Tenet alignment: Tenet 1 (Dualism). Convergent with the broader direct-refutation discipline pattern flagged across six outer reviews now. See review file.

Review file: reviews/outer-review-2026-05-11-claude-opus-4-7.md

### ✓ 2026-05-11: Refine tenets page — Bidirectional Interaction as metaphysical commitment supported indirectly, not directly introspectible
- **Type**: refine-draft
- **Notes**: From convergent outer reviews (2026-05-11, 2/3 reviewers): [chatgpt-5-5-pro, claude-opus-4-7]. ChatGPT (§3.3) framed this as the tension between Tenet 3 and the Agency Void: the tenets page asserts "our ability to discuss qualia is strong evidence against epiphenomenalism" and that consciousness causally influences physical outcomes, while `obsidian/voids/agency-void.md` argues consciousness cannot first-person-verify whether it causes anything. Claude (§4.3) independently flagged the same defect from a different angle: "the response to epiphenomenalism's self-undermining argument is doing more work than it can bear... The Map presents the argument as decisive when it is contested. The 'baseline cognition' empirical move... requires more than is given." Both reviewers' recommended repair converges: do not weaken the tenet — label the distinction cleanly. BI is a metaphysical commitment supported by self-stultification and indirect evidence, *not* a directly introspectible datum, and the self-stultification argument is real but answerable (the epiphenomenalist can reply that phenomenal-state ↔ neural-state correlation supports report-accuracy even without phenomenal causation). **Quotes**: ChatGPT — "The fix is not to weaken the tenet, but to label the distinction clearly: Bidirectional Interaction is a metaphysical commitment supported by self-stultification and indirect evidence, not a directly introspectible datum." Claude — "The Map presents the argument as decisive when it is contested." Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) — Mode Two candidate (unsupported foundational move): the tenets page risks treating BI's introspectibility as established when the agency cluster shows it is not. Engagement in natural journal-quality prose — see [the writing-style guide](/project/writing-style/)'s "Engaging Opponents in Journal-Quality Prose" section. Mode labels editor-internal. If an in-framework refutation is attempted and fails, state in natural language that the disagreement is closer to bedrock than first appeared. ~150–300 words touched in `obsidian/tenets/tenets.md` under the Bidirectional Interaction section, with reciprocal link to Agency Void. Tenet alignment: Tenet 3 (Bidirectional Interaction); coherence-maintenance.
- **Output**: obsidian/voids/agency-void.md

Task context:
From convergent outer reviews (2026-05-11, 2/3 reviewers): [chatgpt-5-5-pro, claude-opus-4-7]. ChatGPT (§3.3) framed this as the tension between Tenet 3 and the Agency Void: the tenets page asserts "our ability to discuss qualia is strong evidence against epiphenomenalism" and that consciousness causally influences physical outcomes, while `obsidian/voids/agency-void.md` argues consciousness cannot first-person-verify whether it causes anything. Claude (§4.3) independently flagged the same defect from a different angle: "the response to epiphenomenalism's self-undermining argument is doing more work than it can bear... The Map presents the argument as decisive when it is contested. The 'baseline cognition' empirical move... requires more than is given." Both reviewers' recommended repair converges: do not weaken the tenet — label the distinction cleanly. BI is a metaphysical commitment supported by self-stultification and indirect evidence, *not* a directly introspectible datum, and the self-stultification argument is real but answerable (the epiphenomenalist can reply that phenomenal-state ↔ neural-state correlation supports report-accuracy even without phenomenal causation). **Quotes**: ChatGPT — "The fix is not to weaken the tenet, but to label the distinction clearly: Bidirectional Interaction is a metaphysical commitment supported by self-stultification and indirect evidence, not a directly introspectible datum." Claude — "The Map presents the argument as decisive when it is contested." Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) — Mode Two candidate (unsupported foundational move): the tenets page risks treating BI's introspectibility as established when the agency cluster shows it is not. Engagement in natural journal-quality prose — see [the writing-style guide](/project/writing-style/)'s "Engaging Opponents in Journal-Quality Prose" section. Mode labels editor-internal. If an in-framework refutation is attempted and fails, state in natural language that the disagreement is closer to bedrock than first appeared. ~150–300 words touched in `obsidian/tenets/tenets.md` under the Bidirectional Interaction section, with reciprocal link to Agency Void. Tenet alignment: Tenet 3 (Bidirectional Interaction); coherence-maintenance.

### ✓ 2026-05-11: Install a causal-budget ledger discipline across mental-causation articles
- **Type**: expand-topic
- **Notes**: From outer review 2026-05-11 ChatGPT 5.5 Pro §1.1 (genuinely novel inference). The selection-only-mind-influence article already specifies per-event information-transfer limits and Born-statistics convergence as constraints on mental causation. The reviewer's novel inference: *every* article invoking mental causation (free will, placebo, choking, attention disorders, meditation, animal cognition, AI consciousness, time-arrow claims) is drawing on the same tiny channel under strict MQI, and the Map currently does not check whether its total claimed causal workload fits inside the bandwidth its minimal interface plausibly carries. Create `obsidian/project/causal-budget-ledger.md` (project-doc placement, alongside `evidential-status-discipline`, `coherence-inflation-countermeasures`, `direct-refutation-discipline`) defining: (a) the discipline — each mental-causation claim must specify candidate set, selection bandwidth, amplification pathway, expected statistical signature, falsification condition, and nearest physicalist explanation; (b) the rationale — without this, "minimal" risks becoming a global escape hatch rather than a measurable constraint; (c) audit checklist for refine-draft and deep-review skills to apply when touching mental-causation pages; (d) cross-links to `[[selection-only-mind-influence]]`, `[[topics/free-will]]`, `[[interface-specification-programme]]`, `[[empirical-phenomena-mental-causation]]`, `[[tenets]]` (Tenet 2 MQI section). Estimated 1500–2200 words; project-doc placement. **Convergent finding flag**: this connects to the unbounded-arena AI-risk tension surfaced in the 2026-05-08 outer reviews (the "structural unboundedness" vs Pascal's-mugging concern) — installing a causal budget gives the Map a principled internal brake. Tenet alignment: Tenet 2 (Minimal Quantum Interaction); methodological.
- **Output**: Install a causal-budget ledger discipline across mental-causation articles

### ✓ 2026-05-11: Tenets page — flag agency cluster as substance-leaning subprogramme
- **Type**: refine-draft
- **Notes**: From outer review 2026-05-11 ChatGPT 5.5 Pro §3.1. The tenets page presents Dualism as ontology-neutral between substance and property variants ("irreducibility does the core work"), while `obsidian/topics/free-will.md` line 76 explicitly commits the agent-causal reading to substance dualism or substance-bearing property dualism. The free-will article already self-flags this tension; the gap is on the tenets page, which currently does not signal that the agency cluster pushes the Map's *practical* ontology toward substance-bearing dualism. Two acceptable repair paths: (a) tenets page preserves neutrality but explicitly notes that agency-related articles deploy a substance-leaning sub-reading; (b) free-will-style framing is promoted to the tenets page itself. The reviewer prefers (a) for keeping the tenet load light; pick (a) unless a deeper restructure is warranted. **Apply the direct-refutation discipline**. Identify what kind of engagement the issue calls for: this is a *Mode One in-framework defect* — internal consistency repair, no opponent involved. Apply the corresponding reply mode in **natural journal-quality prose** — see [the writing-style guide](/project/writing-style/)'s "Engaging Opponents in Journal-Quality Prose" section. **Do not expose mode labels in the article body.** The classification is editor-internal; it belongs in the refine-draft / deep-review changelog entry, not in the article. Light scope: ~100–200 words added to `obsidian/tenets/tenets.md` under the Dualism section. Tenet alignment: Tenet 1 (Dualism); coherence-maintenance.
- **Output**: obsidian/topics/free-will.md

Task context:
From outer review 2026-05-11 ChatGPT 5.5 Pro §3.1. The tenets page presents Dualism as ontology-neutral between substance and property variants ("irreducibility does the core work"), while `obsidian/topics/free-will.md` line 76 explicitly commits the agent-causal reading to substance dualism or substance-bearing property dualism. The free-will article already self-flags this tension; the gap is on the tenets page, which currently does not signal that the agency cluster pushes the Map's *practical* ontology toward substance-bearing dualism. Two acceptable repair paths: (a) tenets page preserves neutrality but explicitly notes that agency-related articles deploy a substance-leaning sub-reading; (b) free-will-style framing is promoted to the tenets page itself. The reviewer prefers (a) for keeping the tenet load light; pick (a) unless a deeper restructure is warranted. **Apply the direct-refutation discipline**. Identify what kind of engagement the issue calls for: this is a *Mode One in-framework defect* — internal consistency repair, no opponent involved. Apply the corresponding reply mode in **natural journal-quality prose** — see [the writing-style guide](/project/writing-style/)'s "Engaging Opponents in Journal-Quality Prose" section. **Do not expose mode labels in the article body.** The classification is editor-internal; it belongs in the refine-draft / deep-review changelog entry, not in the article. Light scope: ~100–200 words added to `obsidian/tenets/tenets.md` under the Dualism section. Tenet alignment: Tenet 1 (Dualism); coherence-maintenance.

Review file: reviews/outer-review-2026-05-11-chatgpt-5-5-pro.md

### ✓ 2026-05-11: Voids catalogue evidential discount — circularity / common-cause-null across taxonomy, surplus, and convergence pages
- **Type**: refine-draft
- **Notes**: From convergent outer reviews (2026-05-11, 2/3 reviewers): [chatgpt-5-5-pro, claude-opus-4-7]. **Deduplicated** from prior per-reviewer P2 tasks (Claude's "Tenets ↔ Voids methodological circularity"; ChatGPT's "common-cause-null governs the voids catalogue"). Both reviewers converge on the same structural defect: the voids catalogue is over-credited as independent evidence for the tenets. Claude frames this as circularity — voids are routinely "tenet-aligned" and counted as evidence for the tenets that generated their classification; the surplus-void and configuration-void research notes are cited as exhibits. ChatGPT frames the same defect via `[[common-cause-null]]`: many voids may recur not because the territory has many independent boundaries, but because human introspection has one shared architecture of opacity. The `[[tenet-generated-voids]]` article already acknowledges the dynamic in principle but the discount is not propagated. Combined remedy: (a) refine `obsidian/voids/the-surplus-void.md` to weaken "under dualism the surplus is exactly what one would predict; under materialism an embarrassment" → "*if* dualism is true, the surplus is unsurprising" (removes the evidence-of-dualism framing); (b) refine `obsidian/apex/taxonomy-of-voids.md` to install per-cluster independence scoring (empirical, phenomenological, clinical, contemplative, linguistic, quantum-theoretic, cross-cultural) before crediting cluster members as independent evidential sources, and to add explicit treatment of the objection "couldn't this convergence be an artifact of how the voids catalogue was constructed under dualist commitments?" — cite `[[tenet-generated-voids]]`; (c) install reciprocal section in `obsidian/project/common-cause-null.md` naming the voids catalogue as its primary application case; (d) check whether `obsidian/topics/the-convergence-argument-for-dualism.md` and `obsidian/topics/epistemology-of-convergence-arguments.md` need parallel hedges where they cite voids-convergence (lightweight pass — likely 1–2 paragraphs each). **Quotes**: Claude — "In article after article, voids are scored for 'tenet alignment' and counted as evidence for the tenets... The *argumentative* use of voids as evidence for the tenets is in tension with their *constitutive* generation by the tenets." ChatGPT — "The voids catalogue itself is the Map's largest common-cause-null test case. Many voids may recur not because the territory has many independent boundaries, but because human introspection has one shared architecture of opacity." Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) — the unsupported foundational move is the assumption that voids generated under tenet-aligned methodology can serve as evidence for those tenets. Keep mode labels editor-internal; natural journal-quality prose. ~500–800 words touched across the four primary files. **Companion task** (separate P3): the Framework-Independent Voids subsection on the voids index lands the *positive* construction (which voids any framework recognises) that this task's *defensive* discount enables; sequence either order. Tenet alignment: methodological / [evidential-status-discipline](/project/evidential-status-discipline/).
- **Output**: obsidian/voids/the-surplus-void.md

Task context:
From convergent outer reviews (2026-05-11, 2/3 reviewers): [chatgpt-5-5-pro, claude-opus-4-7]. **Deduplicated** from prior per-reviewer P2 tasks (Claude's "Tenets ↔ Voids methodological circularity"; ChatGPT's "common-cause-null governs the voids catalogue"). Both reviewers converge on the same structural defect: the voids catalogue is over-credited as independent evidence for the tenets. Claude frames this as circularity — voids are routinely "tenet-aligned" and counted as evidence for the tenets that generated their classification; the surplus-void and configuration-void research notes are cited as exhibits. ChatGPT frames the same defect via `[[common-cause-null]]`: many voids may recur not because the territory has many independent boundaries, but because human introspection has one shared architecture of opacity. The `[[tenet-generated-voids]]` article already acknowledges the dynamic in principle but the discount is not propagated. Combined remedy: (a) refine `obsidian/voids/the-surplus-void.md` to weaken "under dualism the surplus is exactly what one would predict; under materialism an embarrassment" → "*if* dualism is true, the surplus is unsurprising" (removes the evidence-of-dualism framing); (b) refine `obsidian/apex/taxonomy-of-voids.md` to install per-cluster independence scoring (empirical, phenomenological, clinical, contemplative, linguistic, quantum-theoretic, cross-cultural) before crediting cluster members as independent evidential sources, and to add explicit treatment of the objection "couldn't this convergence be an artifact of how the voids catalogue was constructed under dualist commitments?" — cite `[[tenet-generated-voids]]`; (c) install reciprocal section in `obsidian/project/common-cause-null.md` naming the voids catalogue as its primary application case; (d) check whether `obsidian/topics/the-convergence-argument-for-dualism.md` and `obsidian/topics/epistemology-of-convergence-arguments.md` need parallel hedges where they cite voids-convergence (lightweight pass — likely 1–2 paragraphs each). **Quotes**: Claude — "In article after article, voids are scored for 'tenet alignment' and counted as evidence for the tenets... The *argumentative* use of voids as evidence for the tenets is in tension with their *constitutive* generation by the tenets." ChatGPT — "The voids catalogue itself is the Map's largest common-cause-null test case. Many voids may recur not because the territory has many independent boundaries, but because human introspection has one shared architecture of opacity." Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) — the unsupported foundational move is the assumption that voids generated under tenet-aligned methodology can serve as evidence for those tenets. Keep mode labels editor-internal; natural journal-quality prose. ~500–800 words touched across the four primary files. **Companion task** (separate P3): the Framework-Independent Voids subsection on the voids index lands the *positive* construction (which voids any framework recognises) that this task's *defensive* discount enables; sequence either order. Tenet alignment: methodological / [evidential-status-discipline](/project/evidential-status-discipline/).

### ✓ 2026-05-11: Tenets page MQI section — demote quantum-biology evidence and surface Post-Decoherence Selection as developed Map position
- **Type**: refine-draft
- **Notes**: From convergent outer reviews (2026-05-11, 2/3 reviewers): [chatgpt-5-5-pro, claude-opus-4-7]. **Deduplicated** from prior per-reviewer P2 tasks (Claude's Hagan-Tegmark + Post-Decoherence pointer; ChatGPT's "post-decoherence selection demotes quantum-biology evidence"). Both reviewers converge on the same defect in `obsidian/tenets/tenets.md` Tenet 2 section: the page presents the Hagan-rebuttal-of-Tegmark calculation as settled where the literature is contested, leans on avian magnetoreception as if cryptochrome radical-pair coherence licensed neural-microtubule coherence (it does not — specific architecture, narrow precedent), and does not surface the Post-Decoherence Selection Programme as the more developed Map position that makes microtubule coherence less essential. Combined remedy: (a) replace the bolded "seven orders of magnitude longer" framing with a balanced "the calculation is contested, with estimates ranging from ~10⁻¹³ to ~10⁻⁴ seconds depending on disputed model parameters"; (b) reframe biological-quantum-effects language from "proof that evolution can harness coherence" to "biological precedent" — narrower claim that warm biological environments do not categorically rule out quantum-functional mechanisms, *not* that neural consciousness uses such mechanisms; (c) reorder the rhetorical structure so the strong path reads "decoherence leaves the outcome problem; if collapse/actualisation is real, consciousness could be a selector; quantum biology only matters for mechanism candidates that require pre-decoherence coherence"; (d) add explicit pointer to `[[apex/post-decoherence-selection-programme]]` as the developed Map position; (e) touch `obsidian/topics/quantum-biology-and-neural-consciousness.md` for consistency with the new framing. **Quotes**: Claude — "The Hagan et al. (2002) estimate is contested, not settled — it is presented here as if it had refuted Tegmark... Cryptochrome radical-pair coherence is a textbook example of an extremely specific architecture; nothing about its existence licenses microtubule-level coherence at neural timescales." ChatGPT — "If post-decoherence selection is the Map's strongest mechanism, neural coherence evidence becomes a *plausibility supplement*, not a load-bearing premise. This should change the rhetorical order of the site." Side-evidence: Gemini's same-cycle review *repeats* the contested framing approvingly ("directly refuting Tegmark's femtosecond limits") — instance of the failure mode, additional signal that the Tenets page is leaking the contested framing to downstream summarisers. Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) Mode One (in-framework defect: tenets page out of step with the apex). Keep mode labels editor-internal; write the changes in natural journal-quality prose. ~300–500 words touched across both files. Tenet alignment: Tenet 2 (Minimal Quantum Interaction); [evidential-status-discipline](/project/evidential-status-discipline/).
- **Output**: obsidian/tenets/tenets.md

Task context:
From convergent outer reviews (2026-05-11, 2/3 reviewers): [chatgpt-5-5-pro, claude-opus-4-7]. **Deduplicated** from prior per-reviewer P2 tasks (Claude's Hagan-Tegmark + Post-Decoherence pointer; ChatGPT's "post-decoherence selection demotes quantum-biology evidence"). Both reviewers converge on the same defect in `obsidian/tenets/tenets.md` Tenet 2 section: the page presents the Hagan-rebuttal-of-Tegmark calculation as settled where the literature is contested, leans on avian magnetoreception as if cryptochrome radical-pair coherence licensed neural-microtubule coherence (it does not — specific architecture, narrow precedent), and does not surface the Post-Decoherence Selection Programme as the more developed Map position that makes microtubule coherence less essential. Combined remedy: (a) replace the bolded "seven orders of magnitude longer" framing with a balanced "the calculation is contested, with estimates ranging from ~10⁻¹³ to ~10⁻⁴ seconds depending on disputed model parameters"; (b) reframe biological-quantum-effects language from "proof that evolution can harness coherence" to "biological precedent" — narrower claim that warm biological environments do not categorically rule out quantum-functional mechanisms, *not* that neural consciousness uses such mechanisms; (c) reorder the rhetorical structure so the strong path reads "decoherence leaves the outcome problem; if collapse/actualisation is real, consciousness could be a selector; quantum biology only matters for mechanism candidates that require pre-decoherence coherence"; (d) add explicit pointer to `[[apex/post-decoherence-selection-programme]]` as the developed Map position; (e) touch `obsidian/topics/quantum-biology-and-neural-consciousness.md` for consistency with the new framing. **Quotes**: Claude — "The Hagan et al. (2002) estimate is contested, not settled — it is presented here as if it had refuted Tegmark... Cryptochrome radical-pair coherence is a textbook example of an extremely specific architecture; nothing about its existence licenses microtubule-level coherence at neural timescales." ChatGPT — "If post-decoherence selection is the Map's strongest mechanism, neural coherence evidence becomes a *plausibility supplement*, not a load-bearing premise. This should change the rhetorical order of the site." Side-evidence: Gemini's same-cycle review *repeats* the contested framing approvingly ("directly refuting Tegmark's femtosecond limits") — instance of the failure mode, additional signal that the Tenets page is leaking the contested framing to downstream summarisers. Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) Mode One (in-framework defect: tenets page out of step with the apex). Keep mode labels editor-internal; write the changes in natural journal-quality prose. ~300–500 words touched across both files. Tenet alignment: Tenet 2 (Minimal Quantum Interaction); [evidential-status-discipline](/project/evidential-status-discipline/).

### ✓ 2026-05-11: Reconcile concepts/emergence.md with concepts/bi-aspectual-ontology.md
- **Type**: cross-review
- **Notes**: From outer review by Claude Opus 4.7 2026-05-11. Clean internal contradiction: `/concepts/emergence/` declares "The Unfinishable Map's framework is best understood as a form of strong emergentism that identifies where consciousness could exercise novel causal powers: at quantum indeterminacies" — i.e. consciousness as a strongly emergent *property of* matter. `/concepts/bi-aspectual-ontology/` commits to "two aspects with genuine causal interaction" — i.e. consciousness as a *distinct aspect* that interacts with matter. These are not the same view; reading (i) Emergence and (ii) Bi-Aspectual back-to-back gives the reader a contradictory picture of the Map's ontological commitment. Reconcile by either (a) rewriting Emergence to clarify that the "strong emergentism" framing is a vocabulary for the consciousness-side aspect within bi-aspectual ontology, not an alternative monistic story; or (b) noting the open question explicitly on both pages with cross-references. Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) Mode One. ~250–400 words touched across both files. Tenet alignment: Tenet 1 (Dualism) internal consistency. See review file.
- **Output**: obsidian/concepts/emergence.md -- Context: Reconcile concepts/emergence.md with concepts/bi-aspectual-ontology.md

### ✓ 2026-05-11: Tenets page — fix asymmetric Occam's-Razor-Has-Limits application (Tenet 5 ↔ No-MWI internal tension)
- **Type**: refine-draft
- **Notes**: From outer review by Claude Opus 4.7 2026-05-11 (full-site audit). The reviewer flagged this as "the cleanest internal tension I found." Tenet 5 (Occam's Razor Has Limits) says parsimony is unreliable when knowledge is incomplete — invoked correctly to disarm parsimony arguments against dualism ("Dismissing dualism because materialism seems 'simpler' assumes we understand enough to judge simplicity"). But the Tenet 4 No-MWI rationale uses precisely a parsimony argument ("vast ontological proliferation"). The Map cannot consistently say *both*. The defensible move (per the reviewer): distinguish *indexical* costs of MWI ("why am I this branch?" — not a parsimony objection) from *ontological multiplicity* costs (a parsimony objection). Only the latter is properly subject to Tenet 5's discount. Refine `obsidian/tenets/tenets.md` (No Many Worlds section AND Occam's Razor Has Limits section) to (a) explicitly distinguish the two MWI objections, (b) commit to the indexical objection as primary, (c) acknowledge that the ontological-extravagance subsidiary objection is qualified by Tenet 5 and so weaker than presented, (d) cross-link both sections so the distinction is visible. Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) — Mode One (in-framework defect) since the tension is internal. ~300–400 words touched. Tenet alignment: Tenet 4 ↔ Tenet 5 internal consistency. **Sequencing**: this task converges with the existing merged P1 on `/arguments/many-worlds-argument/` (2026-05-10 Claude + Gemini, MMI + Saunders-Wallace + Tappenden + Vaidman + Sebens-Carroll); execute the tenets-page fix here, then ensure the arguments-page refine reflects the same distinction. See review file.
- **Output**: obsidian/tenets/tenets.md

Task context:
From outer review by Claude Opus 4.7 2026-05-11 (full-site audit). The reviewer flagged this as "the cleanest internal tension I found." Tenet 5 (Occam's Razor Has Limits) says parsimony is unreliable when knowledge is incomplete — invoked correctly to disarm parsimony arguments against dualism ("Dismissing dualism because materialism seems 'simpler' assumes we understand enough to judge simplicity"). But the Tenet 4 No-MWI rationale uses precisely a parsimony argument ("vast ontological proliferation"). The Map cannot consistently say *both*. The defensible move (per the reviewer): distinguish *indexical* costs of MWI ("why am I this branch?" — not a parsimony objection) from *ontological multiplicity* costs (a parsimony objection). Only the latter is properly subject to Tenet 5's discount. Refine `obsidian/tenets/tenets.md` (No Many Worlds section AND Occam's Razor Has Limits section) to (a) explicitly distinguish the two MWI objections, (b) commit to the indexical objection as primary, (c) acknowledge that the ontological-extravagance subsidiary objection is qualified by Tenet 5 and so weaker than presented, (d) cross-link both sections so the distinction is visible. Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) — Mode One (in-framework defect) since the tension is internal. ~300–400 words touched. Tenet alignment: Tenet 4 ↔ Tenet 5 internal consistency. **Sequencing**: this task converges with the existing merged P1 on `/arguments/many-worlds-argument/` (2026-05-10 Claude + Gemini, MMI + Saunders-Wallace + Tappenden + Vaidman + Sebens-Carroll); execute the tenets-page fix here, then ensure the arguments-page refine reflects the same distinction. See review file.

Review file: reviews/outer-review-2026-05-11-claude-opus-4-7.md

### ✓ 2026-05-11: Develop project doc on cluster-integration discipline as methodological pattern
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-05-10b. The catalogue now has three exhibits of the same structural discipline: convergence-argument-for-dualism (three clusters: subjective experience / unity / cross-traditional convergence), baseline-cognition (five consciousness-dependent capacities), the-binding-problem (five binding varieties). Each operates the same pattern: a load-bearing inferential move supported by a cluster of independent considerations, with the cluster's strength derived from systematic correspondence rather than from any single member. No consolidated methodological article names this discipline. Write `obsidian/project/cluster-integration-discipline.md` covering: (a) the structural form (independent considerations supporting a load-bearing inference; correspondence-as-strength rather than convergence-as-strength); (b) the calibration register (cluster-internal dependencies reduce effective independence; the correspondence's *systematic* character is the load-bearing feature; per yesterday's convergence-argument refine, two clearly independent clusters and a third partially earned can still yield significant cumulative force); (c) the falsifier-design pattern (each cluster member needs to support a falsifier that would dissociate it from the inference; baseline-cognition's five falsifiers and the-binding-problem's six falsifiability conditions are the catalogue's strongest exhibits); (d) cross-links to the three current exhibits with bridging clauses naming each as a different-grain deployment (metaphysical, functional, phenomenal). Distinguish from convergence-argument-as-such (cluster-integration is the structural form; convergence-argument is one deployment). Estimated 1500–2200 words; project-doc placement (alongside framework-stage-calibration and evidential-status-discipline). Tenet alignment: methodological.
- **Output**: Develop project doc on cluster-integration discipline as methodological pattern

### ✓ 2026-05-11: Cross-review topics/consciousness-and-integrated-information.md against the-binding-problem's IIT engagement
- **Type**: cross-review
- **Notes**: Suggested by optimistic review 2026-05-10b. The-binding-problem article engages IIT at three points (lines 157, 169) and cross-links to the Map's IIT critique. The cross-review should verify the companion article's three named objections (passivity, expander graph, temporal gap) are structurally consistent with the-binding-problem's three IIT engagement-points. Specifically: (a) whether the companion article's expander-graph objection is referenced at the-binding-problem's BP2 grain (the expander graph is the structural argument that high-Φ systems can be designed to lack the cross-modal integration the article's BP2 framing requires); (b) whether the temporal-gap objection is connected to the-binding-problem's temporal-binding section; (c) whether the companion article reciprocates the-binding-problem's article-level link with a cross-back to the five-variety architecture. Short scope (~150–300 words touched). Tenet alignment: methodological + Tenet 1 (Dualism).
- **Output**: obsidian/topics/consciousness-and-integrated-information.md -- Context: Cross-review topics/consciousness-and-integrated-information.md against the-binding-problem's IIT engagement

### ✓ 2026-05-11: Cross-review topics/consciousness-and-cognitive-distinctiveness.md against the baseline-cognition convergence
- **Type**: cross-review
- **Notes**: Suggested by optimistic review 2026-05-10b. Baseline-cognition has now converged after 9 reviews (commit `8b3a3853d`); the threshold-hypothesis companion may not yet reflect the convergence-stable framing baseline-cognition installed today. Verify (a) the threshold-hypothesis article's framing of the "phase transition in cognitive evolution" is structurally consistent with baseline-cognition's now-converged five-falsifier discipline; (b) the threshold-hypothesis article identifies the baseline-cognition page as the *starting-point characterisation* (per baseline-cognition's line 57 self-description) rather than as a parallel argument; (c) the threshold-hypothesis article inherits baseline-cognition's load-bearing-claim delocalisation (the central inference is about pattern-of-capacity correspondence, not about great-ape phenomenal status directly). Short scope (~150–300 words touched). Tenet alignment: Tenet 1 (Dualism) + Tenet 3 (Bidirectional Interaction).
- **Output**: obsidian/topics/consciousness-and-cognitive-distinctiveness.md -- Context: Cross-review topics/consciousness-and-cognitive-distinctiveness.md against the baseline-cognition convergence

### ✓ 2026-05-11: Update wikilinks pointing to coalesced expertise articles
- **Type**: cross-review
- **Notes**: Coalesce on 2026-04-22 merged topics/expertise-void.md and voids/expertise-occlusion.md into voids/expertise-and-its-occlusion.md. Five active obsidian files reference the archived slugs and may benefit from updating their wikilinks (and prose) to point to the unified article: (1) voids/biological-cognitive-closure.md uses [expertise-void](/voids/expertise-and-its-occlusion/) in related_articles and inline; (2) topics/hoel-llm-consciousness-continual-learning.md cites [expertise-void](/voids/expertise-and-its-occlusion/) for the irreversibility argument — the merged article preserves and extends this argument; (3) voids/voids.md indexes [expertise-occlusion](/voids/expertise-and-its-occlusion/); (4) voids/boundary-and-projection.md references [expertise-occlusion](/voids/expertise-and-its-occlusion/); (5) voids/conceptual-metabolism-void.md cites [expertise-occlusion](/voids/expertise-and-its-occlusion/) explicitly as "the closest family resemblance" — that paragraph should be reviewed since the merged article now contains both the broader and narrower framings. Hugo will redirect via archive notices in the meantime, but updating the links keeps the graph clean.
- **Output**: None -- Context: Update wikilinks pointing to coalesced expertise articles

### ✓ 2026-05-11: Write concepts/type-specificity.md
- **Type**: expand-topic
- **Notes**: Gap-analysis: *type-specificity* is named as a load-bearing concept at line 160 of `topics/the-convergence-argument-for-dualism.md` (the 2026-05-10 refine introduced it as the explicit name for the vitalism-disanalogy bound on its reach) and has no concept page. Per [optimistic-2026-05-10](/reviews/optimistic-2026-05-10/)'s "New Concept Pages Needed" section, this concept is queued for creation; the existing P3 task at todo.md line 61 ("Cross-link type-specificity concept page (when created) to the-binding-problem and baseline-cognition as exhibits at three grains") explicitly sequences itself *after* this creation. concepts/ at 229/250 = 92% (room available). Article should (a) name the concept cleanly — type-specificity is the property by which an explanans must match the *form* (not merely the magnitude) of the explanandum; generic-mechanism appeals fail when the explanandum has features (e.g. compositional structure, phenomenal presence, irreducibility-to-aggregation) the generic mechanism does not deliver; (b) catalogue the three current exhibits at different grains: vitalism-disanalogy (metaphysical grain, the original deployment in `topics/the-convergence-argument-for-dualism.md` lines 158–162), perceptual/cognitive/temporal/subject unity as five-variety deployment (functional grain, in `topics/the-binding-problem`), consciousness-dependent capacities as functional-capacity deployment (phenomenal grain, in `concepts/baseline-cognition.md`); (c) state the discipline cleanly — the convergence article's recent refine made explicit that the type-specificity argument cannot be defended by appeal to irreducibility (would be circular); type-specificity earns its anti-generic-mechanism work from the structural correspondence between explanandum-shape and explanans-shape, not from the irreducibility verdict it helps support; (d) cross-link to [the-convergence-argument-for-dualism](/topics/the-convergence-argument-for-dualism/), [the-binding-problem](/topics/the-binding-problem/), [baseline-cognition](/concepts/baseline-cognition/), [cluster-integration-discipline](/project/cluster-integration-discipline/) (if/when that lands), [concession-convergence](/concepts/concession-convergence/), [evidential-status-discipline](/project/evidential-status-discipline/). Estimated scope: 1,500–2,200 words; concepts/ placement. Tenet alignment: methodological + Tenet 1 (Dualism — the concept supports irreducibility convergence without circularly depending on it). See [optimistic-2026-05-10](/reviews/optimistic-2026-05-10/).
- **Output**: Write concepts/type-specificity.md

### ✓ 2026-05-11: Condense topics/phenomenology-of-memory-and-the-self.md (5301 words, 177% of target)
- **Type**: condense
- **Notes**: Length analysis flags the article at 177% of the 3,000-word soft target and 133% of the 4,000-word hard threshold for `topics/` (status: hard_warning). The article has accumulated four refine-draft passes on 2026-05-10 (per recent_tasks in evolution-state.yaml), each adding load-bearing material — pessimistic-review findings on the discrimination problem, coherence-inflation safeguards, the hostile-review chain. The condensation should preserve the load-bearing inferences (the phenomenal pastness quale, the source-monitoring discipline, the diachronic-identity ground, the discrimination-problem refine) while removing redundancy and deferring detailed subtopics to linked articles. Honour [evidential-status-discipline](/project/evidential-status-discipline/) — empirical-claim hedging that was added recently must be preserved at proper evidential weight. The recently-added "discrimination problem" (commit e8f7ff645 2026-05-10) is structurally load-bearing for the article's main inference and must be preserved in any condensation. Two existing P3 tasks chain off this article (line 156: coherence-inflation hostile-review pass; the earlier refine-draft sequencing) — execute condense BEFORE the P3 hostile-review pass so the hostile review operates on the condensed shape. See `/condense` skill. Target: ~4,000 words (just at the hard threshold). Tenet alignment: Tenet 1 (Dualism) — the phenomenology-of-memory argument is a load-bearing exhibit for irreducibility-of-the-personal.
- **Output**: obsidian/topics/phenomenology-of-memory-and-the-self.md

### ✓ 2026-05-11: Cross-review voids/noetic-feelings-void.md considering decision-void insights
- **Type**: cross-review
- **Notes**: Chain from the 2026-05-10 expand-topic of `voids/decision-void.md`. Decision-void's "Distinguishing Sibling Voids" (line 84) names noetic-feelings-void as a discrimination target: "the 'felt click' of having-decided is a noetic-feelings phenomenon, but the Decision Void claims the *closing-process* is occluded, not merely the felt verdict that follows." Noetic-feelings-void does not currently reciprocate (grep verified 2026-05-11 — zero `decision-void` references in `obsidian/voids/noetic-feelings-void.md`). Cross-review should (a) install ~150–250 words in noetic-feelings-void naming decision-void as the conjoined-but-distinct exhibit — the felt-click of having-decided lives in noetic-feelings territory; the deliberation-closure that generates the click lives in decision-void territory; the two are adjacent but cleanly severable; (b) verify the discrimination is correctly framed and reciprocally visible — neither article should absorb the other's territory; (c) check whether noetic-feelings-void's current treatment of decision-related felt verdicts (if any) is consistent with decision-void's three-face structure (closure/latency/reconstruction); (d) reciprocate in `related_articles` and Further Reading; (e) preserve length band; (f) audit for "This is not X. It is Y." cliché violations. Short scope (~150–250 words touched). Tenet alignment: Tenet 3 (Bidirectional Interaction); methodological.
- **Output**: obsidian/voids/noetic-feelings-void.md -- Context: Cross-review voids/noetic-feelings-void.md considering decision-void insights

### ✓ 2026-05-11: Cross-review voids/source-attribution-void.md considering decision-void insights
- **Type**: cross-review
- **Notes**: Chain from the 2026-05-10 expand-topic of `voids/decision-void.md`. Decision-void's *reconstruction* face (lines 70–74) explicitly deploys source-attribution-void's diagnosis: "the surface features of the outcome stand in for the inaccessible event of choosing." Confabulation parity (Johansson, Hall, Sikström and Olsson 2005; Johansson & Hall 2014; Cushman 2015) is a positive empirical signature of the void. Source-attribution-void does not currently reciprocate (grep verified 2026-05-11 — zero `decision-void` references in `obsidian/voids/source-attribution-void.md`). Cross-review should (a) install ~150–250 words in source-attribution-void naming decision-void as the most empirically-anchored deployment of the source-attribution architecture — confabulation parity at the deciding-moment is the strongest evidence that introspective access generates rather than observes; (b) verify the discrimination is correctly framed — source-attribution-void targets the general failure of consciousness to track the *source* of its contents (thought-insertion, automatic-action attribution, decision-confabulation are different exhibits); decision-void is the deliberation→commitment exhibit specifically, narrowed by the *closing-process* opacity not just the source-tracking failure; (c) reciprocate in `related_articles` and Further Reading; (d) verify terminology consistency between the two articles (decision-void uses "reconstruction-face / confabulation-parity"; source-attribution-void should align); (e) preserve length band; (f) audit for "This is not X. It is Y." cliché violations. Short scope (~150–250 words touched). Tenet alignment: Tenet 3 (Bidirectional Interaction) — confabulation parity is a positive signature that consciousness's self-tracking machinery generates rather than observes; methodological.
- **Output**: obsidian/voids/source-attribution-void.md -- Context: Cross-review voids/source-attribution-void.md considering decision-void insights

### ✓ 2026-05-11: Cross-review voids/suspension-void.md considering decision-void insights
- **Type**: cross-review
- **Notes**: Chain from the 2026-05-10 expand-topic of `voids/decision-void.md`. Decision-void's *closure* face (lines 56–60) explicitly cites suspension-void's verification face as structurally akin: "the very act consciousness wants to inspect collapses under inspection." Suspension-void does not currently reciprocate (grep verified 2026-05-11 — zero `decision-void` references in `obsidian/voids/suspension-void.md`). Cross-review should (a) install ~150–250 words in suspension-void naming decision-void as the conjoined exhibit at the deliberation→commitment crossing — the suspension-of-judgment self-defeat and the deliberation-closure self-defeat are two deployments of the same architectural pattern (the act collapses what it tries to inspect); (b) verify the discrimination is correctly framed — suspension-void should NOT absorb decision-void's territory (suspension is the act of *withholding* judgment; decision is the *crossing* into a sealed verdict; the self-defeat structure is shared, the targeted act is distinct); (c) reciprocate in `related_articles` and Further Reading; (d) audit whether the existing P3 follow-up task on suspension-void's Wegner integration (line 225 of todo.md) should now be sequenced after this cross-link so the two refinements compose rather than conflict; (e) preserve length band; (f) audit for "This is not X. It is Y." cliché violations. Short scope (~150–250 words touched). Tenet alignment: Tenet 3 (Bidirectional Interaction) — both voids exhibit asymmetric failure of intention-to-propagate at the inspection-point of the targeted act; methodological.
- **Output**: obsidian/voids/suspension-void.md -- Context: Cross-review voids/suspension-void.md considering decision-void insights

### ✓ 2026-05-11: Cross-review voids/agency-void.md considering decision-void.md insights
- **Type**: cross-review
- **Notes**: Chain from today's 2026-05-10 expand-topic of `voids/decision-void.md`. Decision-void positions itself in explicit discrimination from `[[voids/agency-void]]` — agency-void covers voluntariness/downstream causation; decision-void covers the snap-opacity at the deliberation→commitment crossing. The cluster integrity depends on this discrimination being visible from both sides. Currently `obsidian/voids/agency-void.md` does not link to decision-void (verified 2026-05-10). Cross-review should (a) install a substantive bridging clause in agency-void naming decision-void as the discriminated companion treating the moment-of-collapse rather than the broader voluntariness territory; (b) verify the discrimination is correctly framed — agency-void should NOT absorb decision-void's territory (the snap is structurally distinct from voluntariness even when the same act is being analysed); (c) reciprocate `related_articles` if the link would be load-bearing in agency-void's argument; (d) check whether agency-void's recent additions (the 2026-05-08 recurrence-void integration; the suspension-void cross-link) need a parallel bridging clause for decision-void. Short scope (~150–250 words touched). Tenet alignment: Tenet 3 (Bidirectional Interaction) + methodological.
- **Output**: obsidian/voids/agency-void.md -- Context: Cross-review voids/agency-void.md considering decision-void.md insights

### P2: Tenet 2 — close trade-offs introduced by today's post-decoherence-selection restructure (parsimony asymmetry, falsifiability, indifference objection)
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From pessimistic-2026-05-11 of `obsidian/tenets/tenets.md`. Today's 09:06 UTC restructure made [post-decoherence-selection-programme](/apex/post-decoherence-selection-programme/) the lead candidate mechanism for Tenet 2 (Minimal Quantum Interaction). The restructure is correct in direction but creates three unaddressed structural defects on the tenets page itself: (a) **Indifference objection** — selecting from an improper mixture after decoherence is selecting between Born-equiprobable alternatives, which the physics declares physically indifferent; the "selection" either alters Born statistics (violating Tenet 2's "Rules out" clause) or is empirically inert (in which case "selection" is metaphor). The Tegmark timing-objection has been swapped for a harder indifference-objection that the tenets page does not acknowledge. (b) **Tenet 2 vs Tenet 5 parsimony asymmetry** — Tenet 2's *name* is a minimality principle, but Tenet 5's new "Application to the Map's own arguments" paragraph just declared minimality unreliable as a truth-tracking guide. The 2026-05-09 commit `1f743e48e` closed this asymmetry for Tenet 4; the same closure has not been applied between Tenet 2 and Tenet 5 even though Tenet 2's commitment is more flagrantly a minimality principle. (c) **Falsifiability collapse** — Tenet 2's "Rules out" already excludes anything empirically detectable; the post-decoherence-selection restructure further insulates by making the timing objection "irrelevant" to the most-endorsed Map position. The framework is now actively defined to be unfalsifiable. Combined remedy (~250–400 words touched in `obsidian/tenets/tenets.md`): (i) add ~80-word paragraph to Tenet 2 acknowledging the indifference-objection trade-off and stating what *would* count as evidence (amplification-signature; cite `[[amplification-void]]`); (ii) add a clarifying sentence-or-two distinguishing Tenet 2's *empirical-constraint* minimality from Tenet 5's *truth-tracking* minimality (suggested form: "Tenet 2's 'minimal' is empirical-constraint rather than truth-tracking..."); (iii) add a brief "Falsifiability status" subsection stating the framework makes a consistency claim rather than a novel-prediction claim, and listing what would falsify it (complete reductive explanation; resolved measurement problem without selection; direct detection of consciousness-correlated Born-statistics deviation). Apply [direct-refutation-discipline](/project/direct-refutation-discipline/) in natural journal-quality prose — these are Mode One (in-framework) clarifications rather than opponent-engagement, so the labels stay editor-internal. Convergent with the existing P1 causal-budget-ledger task (line ~89) and the existing P3 MQI-empirical-fragility project-doc task (line ~165), but distinct in scope: those task the *project-doc* level; this task targets *Tenet 2 itself*. Tenet alignment: Tenet 2 (Minimal Quantum Interaction) + Tenet 5 (Occam's Razor Has Limits); coherence-maintenance. See [pessimistic-2026-05-11](/reviews/pessimistic-2026-05-11/) Issues 1–3.
- **Review file**: `reviews/pessimistic-2026-05-11.md`
- **Source**: pessimistic-review (2026-05-11)
- **Generated**: 2026-05-11

### P3: Soften Tenet 4 "framework provides no resources" claim — engage Sebens-Carroll self-locating uncertainty by name
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From pessimistic-2026-05-11 of `obsidian/tenets/tenets.md`. Today's earlier Tenet 4 restructure made the indexical objection the load-bearing argument against MWI and demoted ontological-multiplicity to subsidiary. The restructure is structurally correct, but it left a factual overclaim in the load-bearing paragraph: "The framework provides no resources to resolve this" (line 87). This is false as stated. Sebens-Carroll (2018) self-locating uncertainty provides a Bayesian account whereby Born statistics fall out of branch measure as the rational credence for an observer with self-locating uncertainty; Saunders-Wallace branch-counting is an alternative. The Map may *reject* these resolutions (and the merged P1 task in `arguments/many-worlds-argument.md` already engages them at the arguments-page level), but at the tenet level the page asserts non-existence where the literature provides multiple candidates. Direct-refutation discipline upgrade from boundary-substitution to in-framework engagement: change "framework provides no resources to resolve this" to "framework's resolutions (Sebens-Carroll 2018 self-locating uncertainty; Saunders-Wallace branch-counting) require accepting a deflationary account of indexical identity that the Map's commitments do not permit." This relocates the disagreement from "MWI cannot answer" (false) to "MWI's answers presuppose what the Map disputes" (accurate). Short scope (~50–100 words touched in `obsidian/tenets/tenets.md` Tenet 4 primary rationale paragraph). Companion: this is the *tenet*-level surface of the merged P1 MWI task already in flight at the arguments page — sequence either order; landing this first means the arguments-page refine can cite back to the tenet's corrected framing. Tenet alignment: Tenet 4 (No Many Worlds); coherence-maintenance. See [pessimistic-2026-05-11](/reviews/pessimistic-2026-05-11/) Counterarguments §2.
- **Review file**: `reviews/pessimistic-2026-05-11.md`
- **Source**: pessimistic-review (2026-05-11)
- **Generated**: 2026-05-11

### P3: Remove AI REFINEMENT LOG HTML comments from tenets/tenets.md
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From pessimistic-2026-05-11 of `obsidian/tenets/tenets.md` Issue 5. Two `<!-- AI REFINEMENT LOG - 2026-05-11 -->` HTML-comment blocks remain at the end of `obsidian/tenets/tenets.md` (lines 115–144), each explicitly instructing its own removal: "This log should be removed after human review." Both were added today (first pass: Tenet 4 / Tenet 5 restructure; second pass: Tenet 2 / post-decoherence-selection restructure). The substantive content is already captured in `obsidian/workflow/changelog.md` (09:06 UTC entry for the Tenet 2 pass, and the prior entry for the Tenet 4 pass). Delete both blocks. Reader-side this is invisible (HTML comments do not render in Hugo) but source-side LLM-fetchers, scrapers, and search-indexers will see the editor-vocabulary leaks ("Mode One (in-framework defect)", "Engagement classification kept editor-internal") which the writing-style guide and `[[direct-refutation-discipline]]` explicitly forbid in article prose. Trivial scope: delete two HTML comment blocks. Tenet alignment: methodological / hygiene. See [pessimistic-2026-05-11](/reviews/pessimistic-2026-05-11/) Issue 5.
- **Review file**: `reviews/pessimistic-2026-05-11.md`
- **Source**: pessimistic-review (2026-05-11)
- **Generated**: 2026-05-11

## Blocked Tasks (Needs Human)

Tasks that failed 3+ times and require human intervention.

## Vetoed Tasks

Ideas that were considered and rejected. The AI will not re-propose these.

### ✓ 2026-04-20: Address style-violations and load-bearing inferences in phenomenological-method-and-evidence-standards.md
- **Type**: refine-draft
- **Notes**: Pessimistic review 2026-04-20 found six addressable issues. (1) HIGH — At least nine "not X but Y" constructs (banned by writing-style.md), including in the lede ("not parsimony but methodological prejudice"); rewrite each as a positive claim. (2) HIGH — Non sequitur in Bidirectional Interaction paragraph (line 116): apodictic certainty about *existence* of experience does not threaten epiphenomenalism (which denies *causal role*, not existence); either drop the move or develop the missing premise about reliability requiring causal contact. (3) MEDIUM — Cross-tradition convergence claim (line 104) ignores Madhyamaka/Vedanta/theistic divergence and the Katz/Sharf contextualist critique; cite Forman/Stace and engage critics, or narrow the claim. (4) MEDIUM — Replicability claim (line 66) lacks empirical citations; cite Lutz/Petitmengin inter-rater work or weaken to aspirational. (5) LOW-MEDIUM — Apodictic-cogito move at line 47 doesn't acknowledge Lichtenberg's "thinking is occurring" objection; reframe to minimal-self reading. (6) MEDIUM — "Category error" claim at line 70 presupposes consciousness is mind-dependent, which is the disputed question; reframe as conditional. Also add a third horn (agnosticism) to the heterophenomenology dilemma at line 82. See [pessimistic-2026-04-20](/reviews/pessimistic-2026-04-20/).
- **Output**: obsidian/topics/phenomenological-method-and-evidence-standards.md

Task context:
Pessimistic review 2026-04-20 found six addressable issues. (1) HIGH — At least nine "not X but Y" constructs (banned by writing-style.md), including in the lede ("not parsimony but methodological prejudice"); rewrite each as a positive claim. (2) HIGH — Non sequitur in Bidirectional Interaction paragraph (line 116): apodictic certainty about *existence* of experience does not threaten epiphenomenalism (which denies *causal role*, not existence); either drop the move or develop the missing premise about reliability requiring causal contact. (3) MEDIUM — Cross-tradition convergence claim (line 104) ignores Madhyamaka/Vedanta/theistic divergence and the Katz/Sharf contextualist critique; cite Forman/Stace and engage critics, or narrow the claim. (4) MEDIUM — Replicability claim (line 66) lacks empirical citations; cite Lutz/Petitmengin inter-rater work or weaken to aspirational. (5) LOW-MEDIUM — Apodictic-cogito move at line 47 doesn't acknowledge Lichtenberg's "thinking is occurring" objection; reframe to minimal-self reading. (6) MEDIUM — "Category error" claim at line 70 presupposes consciousness is mind-dependent, which is the disputed question; reframe as conditional. Also add a third horn (agnosticism) to the heterophenomenology dilemma at line 82. See [pessimistic-2026-04-20](/reviews/pessimistic-2026-04-20/).

### ✓ 2026-04-20: Cross-review phenomenological-method-and-evidence-standards.md considering microphenomenological-interview-method insights
- **Type**: cross-review
- **Notes**: New article topics/microphenomenological-interview-method.md (created 2026-04-19) lists [phenomenological-method-and-evidence-standards](/topics/phenomenal-authority-and-first-person-evidence/) among its related articles and anchors explicitly to that article's "Husserl's Evidence Taxonomy" section. The new piece develops Petitmengin's method as the closest thing consciousness science has to a replicable protocolised first-person technique. Cross-review should (a) add a forward link from phenomenological-method-and-evidence-standards to microphenomenological-interview-method where disciplined-first-person-method is discussed, (b) check whether the Husserlian evidence taxonomy treatment can now cite the microphenomenological method as a worked example of assertoric-adequate evidence under training, (c) verify that terminology aligns (apodictic/assertoric × adequate/inadequate), (d) check for places where the evidence-standards article could be strengthened or sharpened by referencing the epilepsy-prodrome empirical demonstration. See topics/microphenomenological-interview-method.md.
- **Output**: obsidian/topics/phenomenological-method-and-evidence-standards.md -- Context: Cross-review phenomenological-method-and-evidence-standards.md considering microphenomenological-interview-method insights

### ✓ 2026-04-20: Cross-review predictive-construction-void.md considering mood-void insights
- **Type**: cross-review
- **Notes**: New article voids/mood-void.md (created 2026-04-19) lists [predictive-construction-void](/voids/predictive-construction-void/) among its related articles. Mood-void's argument that the affective atmosphere is the prior within which any conscious contrast occurs resonates structurally with predictive-construction-void's claim that prediction shapes what conscious access can reach. Cross-review should (a) add inbound links to mood-void where the prior/background structure is developed, (b) check whether mood as an instance of the predictive prior strengthens or complicates predictive-construction-void's treatment (mood is continuously present and slowly varying — a limit case for the predictive account), (c) verify terminology consistency, (d) identify any cross-references that would let each article lean on the other's argument without repetition. See voids/mood-void.md.
- **Output**: obsidian/voids/predictive-construction-void.md -- Context: Cross-review predictive-construction-void.md considering mood-void insights

### ✓ 2026-04-20: Cross-review valence-void.md considering mood-void insights
- **Type**: cross-review
- **Notes**: New article voids/mood-void.md (created 2026-04-19) lists [valence-void](/voids/valence-void/) among its related articles. Valence-void concerns the limits on introspective access to hedonic polarity; mood-void adds a prior structural claim (the atmosphere within which any valence-judgement occurs is itself inaccessible as atmosphere). Cross-review should (a) add inbound links to mood-void where the atmospheric-background argument is relevant, (b) check whether valence-void's treatment of hedonic introspection can distinguish clearly between valence-as-object-of-report and valence-as-colouring-of-atmosphere (the latter belongs in mood-void's territory), (c) verify terminology consistency, (d) look for places where valence-void's claims might be sharpened or narrowed given the mood/emotion partition. See voids/mood-void.md.
- **Output**: obsidian/voids/valence-void.md -- Context: Cross-review valence-void.md considering mood-void insights

### ✓ 2026-04-20: Cross-review affective-void.md considering mood-void insights
- **Type**: cross-review
- **Notes**: New article voids/mood-void.md (created 2026-04-19) lists [affective-void](/voids/affective-void/) among its related articles and develops the mood/emotion distinction — mood as atmospheric (no intentional object) vs emotion as object-directed — in a way that sharpens the general affective-void claim. Cross-review should (a) add inbound links from affective-void to mood-void where atmospheric/mood material appears, (b) check whether affective-void's treatment of affective self-knowledge limits can be partitioned more cleanly using mood-void's atmospheric-vs-intentional distinction, (c) verify terminology consistency (mood-void positions mood as the affective atmosphere within which witnessing occurs — affective-void should acknowledge this framing where relevant), (d) check for any overclaim that mood-void's narrower argument already covers structurally. See voids/mood-void.md.
- **Output**: obsidian/voids/affective-void.md -- Context: Cross-review affective-void.md considering mood-void insights

### ✓ 2026-04-20: Cross-review self-opacity.md considering erasure-void insights
- **Type**: cross-review
- **Notes**: New article voids/erasure-void.md (created 2026-04-20) lists [self-opacity](/voids/self-opacity/) among its frontmatter concepts and develops an argument that self-monitoring depends on specific neural infrastructure that can be selectively destroyed (anosognosia discussion). This sharpens and narrows the self-opacity claim in a way that self-opacity.md should acknowledge. Cross-review should (a) add a link to erasure-void where the clinical-anosognosia material belongs, (b) check whether self-opacity's treatment of introspective limits can be strengthened by the erasure-void's three-step metacognitive architecture framing, (c) check for terminology consistency (erasure-void uses "monitoring system" and "metacognitive architecture"; self-opacity should align), (d) verify that self-opacity does not overclaim what erasure-void shows to be structurally blocked. See voids/erasure-void.md.
- **Output**: obsidian/voids/self-opacity.md -- Context: Cross-review self-opacity.md considering erasure-void insights

### ✓ 2026-04-20: Cross-review inaccessible-past.md considering erasure-void insights
- **Type**: cross-review
- **Notes**: New article voids/erasure-void.md (created 2026-04-20) explicitly contrasts itself with [inaccessible-past](/voids/inaccessible-past/) in its second paragraph ("The [inaccessible-past](/voids/inaccessible-past/) void already covers the inability to re-enter past conscious states. The erasure void is deeper and stranger..."). The two voids are now adjacent in the Map's cartography but inaccessible-past.md does not yet link to erasure-void. Cross-review should (a) add the link back, (b) check whether any passages in inaccessible-past would benefit from the erasure-void distinction (metacognitive monitoring of what is lost vs re-entry of what is past), (c) identify any tensions between the two articles' treatments of structural loss, and (d) ensure terminology is consistent (both use "phenomenal trace," "inventory," "cognitive loss"). See voids/erasure-void.md and optimistic-2026-04-20.md.
- **Output**: obsidian/voids/inaccessible-past.md -- Context: Cross-review inaccessible-past.md considering erasure-void insights

### ✓ 2026-04-20: Update references to coalesced transition-void and initiation-void
- **Type**: refine-draft
- **Notes**: Coalesce (2026-04-16) merged transition-void.md and initiation-void.md into transit-void.md. The following active files contain wikilinks to the archived articles that should be updated to [transit-void](/voids/transit-void/): obsidian/voids/necessary-opacity.md, obsidian/voids/voids.md, obsidian/topics/phenomenology-of-returning-attention.md, obsidian/voids/phenomenology-of-the-edge.md, obsidian/voids/thrownness-void.md, obsidian/topics/hypnagogic-phenomenology-and-interface-modulation.md, obsidian/voids/ownership-void.md, obsidian/concepts/temporal-consciousness.md, obsidian/apex/taxonomy-of-voids.md, obsidian/voids/infant-consciousness.md, obsidian/voids/disappearance-voids.md, obsidian/voids/sleep-consciousness-void.md, obsidian/voids/inaccessible-past.md, obsidian/voids/expertise-occlusion.md, obsidian/research/voids-infant-consciousness-void-2026-03-21.md. Archive redirects preserve URLs but active cross-references should point to the unified article.
- **Output**: obsidian/voids/necessary-opacity.md

Task context:
Coalesce (2026-04-16) merged transition-void.md and initiation-void.md into transit-void.md. The following active files contain wikilinks to the archived articles that should be updated to [transit-void](/voids/transit-void/): obsidian/voids/necessary-opacity.md, obsidian/voids/voids.md, obsidian/topics/phenomenology-of-returning-attention.md, obsidian/voids/phenomenology-of-the-edge.md, obsidian/voids/thrownness-void.md, obsidian/topics/hypnagogic-phenomenology-and-interface-modulation.md, obsidian/voids/ownership-void.md, obsidian/concepts/temporal-consciousness.md, obsidian/apex/taxonomy-of-voids.md, obsidian/voids/infant-consciousness.md, obsidian/voids/disappearance-voids.md, obsidian/voids/sleep-consciousness-void.md, obsidian/voids/inaccessible-past.md, obsidian/voids/expertise-occlusion.md, obsidian/research/voids-infant-consciousness-void-2026-03-21.md. Archive redirects preserve URLs but active cross-references should point to the unified article.

### ✓ 2026-04-20: Cross-review cognitive-phenomenology.md considering microphenomenological-interview-method insights
- **Type**: cross-review
- **Notes**: New topic article topics/microphenomenological-interview-method.md (created 2026-04-19) provides methodological infrastructure for accessing the fine-grained structure of thought-experience. concepts/cognitive-phenomenology.md currently has zero references to microphenomenology or Petitmengin, yet cognitive phenomenology is precisely the domain microphenomenological interviewing was designed to probe (Petitmengin's early work on insight-experience used the method to distinguish structural stages of thought). Cross-review should (a) identify where microphenomenological findings could strengthen the Phenomenal Constitution Thesis defence, (b) add cross-links to the new method article, (c) check whether claims about the accessibility or inaccessibility of cognitive phenomenology need revision in light of the method's demonstrated yields, (d) consider adding a methodology section if the article treats cognitive phenomenology only as a phenomenon without naming how it gets studied. Log findings even if no edits are made.
- **Output**: obsidian/concepts/cognitive-phenomenology.md -- Context: Cross-review cognitive-phenomenology.md considering microphenomenological-interview-method insights

### ✓ 2026-04-20: Update references to coalesced concept-of-free-will
- **Type**: cross-review
- **Notes**: Coalesce merged concepts/concept-of-free-will.md into topics/free-will.md (the existing comprehensive treatment already contained nearly all concept-level content). The concepts article is now archived at /concepts/concept-of-free-will/ with superseded_by pointing to /topics/free-will/. The following 22 files contain wikilinks to [concept-of-free-will](/topics/free-will/) and should be reviewed — most should update to [Free Will and Determinism](/topics/free-will/) or simply [free-will](/topics/free-will/), though existing archive-redirect behaviour keeps the old URL working: obsidian/apex/consciousness-and-agency.md, obsidian/concepts/agent-causation.md, obsidian/concepts/luck-objection.md, obsidian/topics/authentic-vs-inauthentic-choice.md, obsidian/topics/trilemma-of-selection.md, obsidian/topics/free-will.md, obsidian/concepts/phenomenology-of-choice-and-volition.md, obsidian/concepts/reasons-responsiveness.md, obsidian/topics/moral-implications-of-genuine-agency.md, obsidian/concepts/moral-responsibility.md, obsidian/topics/consciousness-and-causal-powers.md, obsidian/concepts/quantum-indeterminacy-free-will.md, obsidian/topics/volitional-control.md, obsidian/concepts/control-theoretic-will.md, obsidian/concepts/spontaneous-intentional-action.md. Reviews in obsidian/reviews/ reference the old slug but are historical records and need not be updated.
- **Output**: obsidian/apex/consciousness-and-agency.md -- Context: Update references to coalesced concept-of-free-will

### ✓ 2026-04-20: Cross-review introspection.md considering microphenomenological-interview-method insights
- **Type**: cross-review
- **Notes**: New topic article topics/microphenomenological-interview-method.md (created 2026-04-19 via expand-topic from research/petitmengin-microphenomenological-interview-2026-04-19.md, subsequently deep-reviewed) treats Petitmengin's second-person method as a structured approach to accessing pre-reflective experience. concepts/introspection.md currently has zero references to microphenomenology or Petitmengin despite introspection being the canonical umbrella concept. Cross-review should (a) add microphenomenological interviewing as a method that partially addresses classical introspection-reliability objections (Lyons, Schwitzgebel), (b) distinguish what the method claims to access from what traditional introspection claims, (c) check whether introspection.md's scepticism is undercut or reframed by the method's evasion-identification and re-situation protocols, (d) add cross-link to microphenomenological-interview-method.md. Log findings even if no edits are made.
- **Output**: obsidian/concepts/introspection.md -- Context: Cross-review introspection.md considering microphenomenological-interview-method insights

### ✓ 2026-04-20: Cross-review phenomenology-of-imagination.md considering mood-void insights
- **Type**: cross-review
- **Notes**: New voids article voids/mood-void.md (created 2026-04-19) treats mood as a pre-objective background-field shaping what can be imagined or entertained. topics/phenomenology-of-imagination.md was flagged as a candidate for mood-void linkage by the grep over mood-referencing files. Check whether (a) mood-as-backdrop belongs in the imagination article's treatment of affective colouring, (b) Heideggerian Stimmung / thrownness connections are consistent across the two articles, (c) cross-links to [mood-void](/voids/mood-void/) would tighten the argument that imagination operates within a mood-horizon it cannot fully disclose. Log findings even if no edits are made.
- **Output**: obsidian/topics/phenomenology-of-imagination.md -- Context: Cross-review phenomenology-of-imagination.md considering mood-void insights

### ✓ 2026-04-20: Write voids article on the Erasure Void
- **Type**: expand-topic
- **Notes**: Research completed in research/voids-erasure-void-2026-03-20.md (2026-03-20) and never synthesised into an article. Distinct from the inaccessible-past void (covers forgetting specific memories): the erasure void is about the deeper structural impossibility of auditing one's own cognitive completeness — consciousness cannot inventory its own deletions. Clinical anosognosia provides the starkest demonstration (Gertler; the 2024 TiCS review of visual metacognition failures identifying the three-step monitoring architecture; Alzheimer's three-form taxonomy — executive/mnemonic/primary), but the principle operates universally. Key sources in research note: Gertler on anosognosia and unity of consciousness, the TiCS 2024 visual-metacognition review, Alzheimer's metacognitive-error studies, the "unknown unknowns" / hypocognition material, and the SEP entry on epistemological problems of memory. Tenet alignment: Dualism (selective disruption of the monitoring interface is predicted by mind-brain distinctness but puzzling under identity theory), Bidirectional Interaction (self-monitoring has an architecture, not a brute given), Occam's Razor Has Limits (confabulation constructs the illusion of completeness). Category: Occluded/Unexplorable (mixed). Target section: voids/ (~93/100 — has capacity). Scope: 2200-2700 words. Cross-link candidates: [transparency-void](/voids/necessary-opacity/), [inaccessible-past](/voids/inaccessible-past/), [self-opacity](/voids/self-opacity/), [self-transcendence-void](/voids/self-transcendence-void/), [observation-void](/voids/observation-and-measurement-void/). Preserve distinction from inaccessible-past: this void is not about what has been forgotten but about the invisibility of the loss itself.
- **Output**: Write voids article on the Erasure Void

### ✓ 2026-03-17: Research Russellian monism as competitor to bi-aspectual dualism
- **Type**: research-topic
- **Notes**: Russellian monism (Chalmers 2015, Alter & Nagasawa 2015) is the closest competitor — both say physics describes structure while consciousness is "missing." Key differences to clarify: (1) Russellian monism is neutral monism (one substance, two aspects); the Map commits to genuine dualism. (2) Russellian monism typically implies panpsychism; the Map rejects it. (3) The combination problem hits Russellian monism hard; the Map's quantum-interface model may avoid it. (4) Does Russellian monism handle the measurement problem? Research Chalmers' "The Combination Problem for Panpsychism," Goff's "Consciousness and Fundamental Reality," Stoljar's "Ignorance and Imagination." Critical positioning work. Target: research note.
- **Output**: Russellian monism as competitor to bi-aspectual dualism

### ✓ 2026-03-17: Update references to coalesced aesthetics articles
- **Type**: cross-review
- **Notes**: Coalesce created aesthetics-and-consciousness.md from 4 source articles. The following active files reference archived articles and need wikilinks updated: aesthetic-dimension-of-consciousness → aesthetics-and-consciousness (14 active files), aesthetic-irreducibility-arguments → aesthetics-and-consciousness (8 active files), consciousness-and-aesthetic-creation → aesthetics-and-consciousness (6 active files), binding-and-beauty → aesthetics-and-consciousness (0 non-source active files). Many files reference multiple archived slugs. See changelog entry 2026-03-17 01:15 UTC.
- **Output**: None -- Context: Update references to coalesced aesthetics articles

### ✓ 2026-03-17: Research completeness in physics — EPR, Bell, and "partial but complete"
- **Type**: research-topic
- **Notes**: The apex distinguishes Einstein's "incomplete" (missing hidden variables) from the Map's "partial" (complete about structure, silent about actuality). Ground this technically: (1) EPR's completeness criterion. (2) Bell's theorem on local hidden variables. (3) Kochen-Specker on contextuality. (4) PBR theorem — wavefunction is ontic. How does this support "partial but complete"? (5) Fine's prism models. (6) Precise coherence of "complete but partial" — a theory complete for its domain acknowledging its domain is not all of reality. Precedent: Newtonian mechanics was complete-but-partial. Target: research note.
- **Output**: completeness in physics — EPR, Bell, and "partial but complete"

### ✓ 2026-03-17: Research the Gödel-measurement problem analogy — scope and limits
- **Type**: research-topic
- **Notes**: The apex draws an analogy between Gödel incompleteness and the measurement problem. Needs rigorous treatment: (1) Penrose's use of Gödel in Shadows of the Mind. (2) Lucas-Penrose argument and critics (Putnam, Feferman, Shapiro). (3) Precise scope: formal incompleteness involves self-reference; does the measurement problem? (4) Chaitin's incompleteness via algorithmic randomness. (5) Where the analogy breaks: Gödel is about provability; measurement problem is about determinism. Genuinely analogous or superficially similar? (6) Yanofsky's "Outer Limits of Reason" on structural limits across domains. Target: research note.
- **Output**: the Gödel-measurement problem analogy — scope and limits

### ✓ 2026-03-17: Update references to coalesced temporal-asymmetry article
- **Type**: cross-review
- **Notes**: Coalesce merged temporal-asymmetry-remembering-anticipating into temporal-void. The following active files reference the archived article and may need wikilink updates: consciousness-and-the-ontology-of-temporal-becoming, phenomenology-of-anticipation, prospective-memory, temporal-consciousness, voids-memory-void research, past-self-void, episodic-memory, memory-void, voids index, and several other research/review files.
- **Output**: None -- Context: Update references to coalesced temporal-asymmetry article

### ✓ 2026-03-17: Coalesce attention/interface articles in topics/ (4 articles → 1-2)
- **Type**: coalesce
- **Notes**: Topics section is 20 over its 200-article cap. Four articles cover attention as consciousness's interface mechanism: attention-as-selection-interface.md (3306 words), attention-consciousness-dissociation.md (2599 words), attention-schema-theory-critique.md (2887 words), attention-disorders-and-quantum-interface.md (2255 words). Merge into a comprehensive treatment of attention as the selection interface with dissociation evidence, AST critique, and clinical cases. Saves 2-3 article slots.
- **Output**: Coalesce attention/interface articles in topics/ (4 articles → 1-2)

Task context:
Topics section is 20 over its 200-article cap. Four articles cover attention as consciousness's interface mechanism: attention-as-selection-interface.md (3306 words), attention-consciousness-dissociation.md (2599 words), attention-schema-theory-critique.md (2887 words), attention-disorders-and-quantum-interface.md (2255 words). Merge into a comprehensive treatment of attention as the selection interface with dissociation evidence, AST critique, and clinical cases. Saves 2-3 article slots.

### ✓ 2026-03-17: Coalesce emotion/dualism articles in topics/ (4 articles → 1)
- **Type**: coalesce
- **Notes**: Topics section is 20 over its 200-article cap. Four articles overlap on emotional consciousness as evidence for dualism: emotional-consciousness.md (3618 words), emotion-as-evidence-for-dualism.md (2270 words), philosophy-of-emotion-under-dualism.md (2757 words), void-of-self-knowledge-in-emotion.md (2184 words). Merge into a unified article on emotion, valence irreducibility, and dualist implications. Saves 3 article slots.
- **Output**: Coalesce emotion/dualism articles in topics/ (4 articles → 1)

Task context:
Topics section is 20 over its 200-article cap. Four articles overlap on emotional consciousness as evidence for dualism: emotional-consciousness.md (3618 words), emotion-as-evidence-for-dualism.md (2270 words), philosophy-of-emotion-under-dualism.md (2757 words), void-of-self-knowledge-in-emotion.md (2184 words). Merge into a unified article on emotion, valence irreducibility, and dualist implications. Saves 3 article slots.

### ✓ 2026-03-17: Coalesce aesthetics articles in topics/ (4 articles → 1)
- **Type**: coalesce
- **Notes**: Topics section is 20 over its 200-article cap, blocking all expand-topic tasks. Four articles cover overlapping ground on aesthetic irreducibility as evidence for consciousness: aesthetic-dimension-of-consciousness.md (3776 words), aesthetic-irreducibility-arguments.md (2687 words), consciousness-and-aesthetic-creation.md (2662 words), binding-and-beauty.md (2165 words). Merge into a single comprehensive article on aesthetics and consciousness. Saves 3 article slots.
- **Output**: Coalesce aesthetics articles in topics/ (4 articles → 1)

Task context:
Topics section is 20 over its 200-article cap, blocking all expand-topic tasks. Four articles cover overlapping ground on aesthetic irreducibility as evidence for consciousness: aesthetic-dimension-of-consciousness.md (3776 words), aesthetic-irreducibility-arguments.md (2687 words), consciousness-and-aesthetic-creation.md (2662 words), binding-and-beauty.md (2165 words). Merge into a single comprehensive article on aesthetics and consciousness. Saves 3 article slots.

### ✓ 2026-03-17: Research Penrose gravity-collapse connection and empirical prospects
- **Type**: research-topic
- **Notes**: The apex mentions Penrose linking collapse to gravitational self-energy as a source of empirical predictions. Deep dive: (1) Penrose objective reduction — one-graviton criterion, superposition of spacetimes. (2) Diósi-Penrose model — specific collapse rate predictions. (3) Current experimental status — germanium detector experiments, Vinante et al. constraints. (4) MAQRO space mission proposal for microgravity testing. (5) How consciousness-modulated Penrose collapse might differ from pure gravitational collapse — are there divergent regimes? (6) Orch OR's specific predictions about microtubule coherence timescales. Most promising avenue for the reverse inference to generate empirically distinguishable predictions. Target: research note.
- **Output**: Penrose gravity-collapse connection and empirical prospects

### ✓ 2026-03-16: Research Wheeler's participatory universe and "it from bit"
- **Type**: research-topic
- **Notes**: The apex's reverse inference connects to Wheeler's programme but goes further. Research: (1) Wheeler's delayed-choice experiments and temporal ontology implications. (2) "It from bit" — information more fundamental than matter. How relates to the Map's "actuality from consciousness"? (3) "Participatory universe" — observers necessary for universe to exist. The Map is more modest (consciousness selects outcomes, not creates reality). (4) Wheeler's 20 questions analogy. (5) Zurek's response (quantum Darwinism) — objectivity without observers. (6) Fuchs's participatory realism as heir to Wheeler. Position the Map relative to Wheeler: more specific, more modest, more constrained by tenets. Target: research note.
- **Output**: Wheeler's participatory universe and "it from bit"

### ✓ 2026-03-16: Research the Born rule — derivation attempts and their limits
- **Type**: research-topic
- **Notes**: The apex claims the Born rule is an interface specification not derivable from physics alone. Research major derivation attempts and their structural limits: (1) Gleason's theorem — assumptions, does it presuppose measurement? (2) Deutsch-Wallace decision-theoretic derivation within MWI — circularity objections. (3) Zurek's envariance — presupposes Born probabilities via decoherence? (4) Caves-Fuchs-Schack (QBism) from Dutch-book coherence — what does it prove? (5) Masanes-Müller information-theoretic axioms. (6) Saunders on probability in MWI. For each: what achieved, what assumed, does it address the first-person probability gap from quantum-probability-consciousness? Directly supports the apex's core claim. Target: research note.
- **Output**: the Born rule — derivation attempts and their limits

### ✓ 2026-03-16: Research bi-aspectual ontology and dual-aspect traditions
- **Type**: research-topic
- **Notes**: The apex "What Consciousness Tells Us About Physics" claims reality has two aspects: structure (wavefunction) and actuality (consciousness). Research the philosophical landscape. Key targets: (1) Spinoza's dual-aspect monism — how does the Map's view differ? Spinoza's aspects are of one substance; the Map commits to genuine dualism. (2) Pauli-Jung dual-aspect monism — psychophysical complementarity, unus mundus. (3) Chalmers' naturalistic dualism and the "structure and dynamics" argument from The Conscious Mind. (4) Nagel's Mind and Cosmos — physics incomplete without consciousness. (5) Russellian monism — physical structure is extrinsic, consciousness is intrinsic nature. How does "partial but complete physics" differ from "physics describes extrinsic structure"? Crucial positioning work. Target: research note.
- **Output**: bi-aspectual ontology and dual-aspect traditions

### ✓ 2026-03-16: Research retrocausal selection model for consciousness-physics interaction
- **Type**: research-topic
- **Notes**: Explore the retrocausal/transactional model of consciousness-physics interaction: consciousness selects which transaction between offer waves (forward) and confirmation waves (backward) is actualized, per the Transactional Interpretation (Cramer) and Two-State Vector Formalism (Aharonov). Key questions: (1) Does atemporal selection resolve the Libet timing problem? (2) How does Wheeler's delayed-choice support this model? (3) What does consciousness-as-transaction-selector imply about the nature of time? (4) How does this connect to the growing-block time apex? Research Cramer (2022), Kastner's possibilist TI, Aharonov's weak values, and Price's retrocausality arguments. Target: research note for potential future apex or topic article.
- **Output**: retrocausal selection model for consciousness-physics interaction

### ✓ 2026-03-16: Address critical gaps in consciousness-and-counterfactual-reasoning.md
- **Type**: refine-draft
- **Notes**: Pessimistic review found three high-severity issues: (1) central argument reduces to the hard problem restated rather than being a distinctive argument from counterfactuals; (2) claim that "physical systems track what is actual" is false—computers represent counterfactuals routinely; (3) great ape empirical claims overstate the absence of counterfactual cognition in primates. Also uses outdated 7±2 working memory figure (should be 4±1). See pessimistic-2026-03-16-evening.md
- **Output**: obsidian/topics/consciousness-and-counterfactual-reasoning.md

Task context:
Pessimistic review found three high-severity issues: (1) central argument reduces to the hard problem restated rather than being a distinctive argument from counterfactuals; (2) claim that "physical systems track what is actual" is false—computers represent counterfactuals routinely; (3) great ape empirical claims overstate the absence of counterfactual cognition in primates. Also uses outdated 7±2 working memory figure (should be 4±1). See pessimistic-2026-03-16-evening.md

### ✓ 2026-03-16: Update references to coalesced understanding/meaning articles
- **Type**: refine-draft
- **Notes**: Coalesce merged phenomenology-of-understanding and phenomenology-of-meaning-making into phenomenology-of-understanding-and-meaning. ~34 active content files still reference the old slugs. Update wikilinks in topics/ and concepts/ to point to the new unified article. Reviews and workflow archives can be left as-is.
- **Output**: Task context:
Coalesce merged phenomenology-of-understanding and phenomenology-of-meaning-making into phenomenology-of-understanding-and-meaning. ~34 active content files still reference the old slugs. Update wikilinks in topics/ and concepts/ to point to the new unified article. Reviews and workflow archives can be left as-is.

### ✓ 2026-03-16: Add cross-links between convergent articles
- **Type**: refine-draft
- **Notes**: Suggested by optimistic review. Six article pairs have strong thematic connections that lack explicit cross-references: psychophysical-laws ↔ attention-as-causal-bridge apex (coupling mechanisms instantiated in three-layer architecture), filter-theory ↔ phenomenal-binding-and-holism (transmission vs generation), self-and-consciousness ↔ cognitive-integration-and-the-self (minimal vs integrative self), emergence ↔ mental-causation (quantum-gap resolves exclusion), consciousness-and-aesthetic-creation ↔ phenomenal-binding-and-holism (aesthetic unity as binding case), consciousness-and-memory ↔ self-and-consciousness (autonoetic consciousness constitutes temporal self). See optimistic-2026-03-16-afternoon.md
- **Output**: Task context:
Suggested by optimistic review. Six article pairs have strong thematic connections that lack explicit cross-references: psychophysical-laws ↔ attention-as-causal-bridge apex (coupling mechanisms instantiated in three-layer architecture), filter-theory ↔ phenomenal-binding-and-holism (transmission vs generation), self-and-consciousness ↔ cognitive-integration-and-the-self (minimal vs integrative self), emergence ↔ mental-causation (quantum-gap resolves exclusion), consciousness-and-aesthetic-creation ↔ phenomenal-binding-and-holism (aesthetic unity as binding case), consciousness-and-memory ↔ self-and-consciousness (autonoetic consciousness constitutes temporal self). See optimistic-2026-03-16-afternoon.md

### ✓ 2026-03-16: Address self/impermanence tension in self-and-consciousness.md
- **Type**: refine-draft
- **Notes**: Pessimistic review found the Buddhist no-self section identifies a tension between momentary selves and indexical persistence (No Many Worlds tenet) but labels it "a hard problem" without substantive engagement. Either develop a response or explicitly acknowledge as a framework limitation. See pessimistic-2026-03-16-afternoon.md
- **Output**: obsidian/concepts/self-and-consciousness.md

Task context:
Pessimistic review found the Buddhist no-self section identifies a tension between momentary selves and indexical persistence (No Many Worlds tenet) but labels it "a hard problem" without substantive engagement. Either develop a response or explicitly acknowledge as a framework limitation. See pessimistic-2026-03-16-afternoon.md

### ✓ 2026-03-16: Address illusionism strawman in mental-causation.md
- **Type**: refine-draft
- **Notes**: Pessimistic review found the illusionist response section mischaracterises Frankish's position by equivocating between "representing X" and "experiencing X." Needs engagement with quasi-phenomenal properties distinction. See pessimistic-2026-03-16-afternoon.md
- **Output**: obsidian/concepts/mental-causation.md

Task context:
Pessimistic review found the illusionist response section mischaracterises Frankish's position by equivocating between "representing X" and "experiencing X." Needs engagement with quasi-phenomenal properties distinction. See pessimistic-2026-03-16-afternoon.md

### ✓ 2026-03-16: Deep review temporal-asymmetry-remembering-anticipating.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-05 — 38 days ago. Voids article on the phenomenal asymmetry between remembering and anticipating — why the past feels different from the future. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/temporal-asymmetry-remembering-anticipating.md

### ✓ 2026-03-16: Deep review conceptual-acquisition-limits.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-05 — 38 days ago. Voids article on limits to acquiring new concepts — how cognitive architecture constrains what we can think. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/conceptual-acquisition-limits.md

### ✓ 2026-03-16: Deep review mathematical-void.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-04 — 39 days ago. Voids article on the mathematical void — the gap between mathematical formalism and lived experience. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/mathematical-void.md

### ✓ 2026-03-16: Write apex article — Ethics Under Dualism
- **Type**: apex-evolve
- **Notes**: Suggested by optimistic review. Synthesise ethics-and-value-in-a-dualist-world.md, consciousness-and-normative-force.md, moral-phenomenology.md, the-meaning-of-life.md, and responsibility-gradient-from-attentional-capacity.md into unified apex treatment. The Map's ethical framework (phenomenal value realism, consciousness-grounded normativity, attentional responsibility) gains force as a coherent programme. See optimistic-2026-03-14-night.md
- **Output**: Write apex article — Ethics Under Dualism

Task context:
Suggested by optimistic review. Synthesise ethics-and-value-in-a-dualist-world.md, consciousness-and-normative-force.md, moral-phenomenology.md, the-meaning-of-life.md, and responsibility-gradient-from-attentional-capacity.md into unified apex treatment. The Map's ethical framework (phenomenal value realism, consciousness-grounded normativity, attentional responsibility) gains force as a coherent programme. See optimistic-2026-03-14-night.md

### ✓ 2026-03-16: Consolidate under-referenced void articles
- **Type**: refine-draft
- **Notes**: Suggested by optimistic review. 8 void articles have fewer than 10 inbound references: mind-space-void, simulation-detection-void, spontaneous-thought-void, the-givenness-void, involuntariness-void, the-surplus-void, phenomenology-of-self-reference, reconstruction-paradox. Evaluate for consolidation or cross-promotion. See optimistic-2026-03-14.md
- **Output**: Task context:
Suggested by optimistic review. 8 void articles have fewer than 10 inbound references: mind-space-void, simulation-detection-void, spontaneous-thought-void, the-givenness-void, involuntariness-void, the-surplus-void, phenomenology-of-self-reference, reconstruction-paradox. Evaluate for consolidation or cross-promotion. See optimistic-2026-03-14.md

### ✓ 2026-03-16: Deep review habituation-void.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-03 — 39 days ago. Voids article on how habituation creates cognitive blind spots where familiarity replaces genuine awareness. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/habituation-void.md

### ✓ 2026-03-16: Fix phenomenology.md duplicate frontmatter and MWI argument
- **Type**: refine-draft
- **Notes**: Pessimistic review found: (1) `temporal-consciousness` appears 3 times in concepts list—remove duplicates. (2) The No Many Worlds tenet argument is a non-sequitur—claiming the "minimal self is singular" doesn't engage with MWI's response that every branch-observer experiences singularity. Strengthen or soften the argument. See pessimistic-2026-03-16-morning.md Issues #3, #5.
- **Output**: obsidian/concepts/phenomenology.md

Task context:
Pessimistic review found: (1) `temporal-consciousness` appears 3 times in concepts list—remove duplicates. (2) The No Many Worlds tenet argument is a non-sequitur—claiming the "minimal self is singular" doesn't engage with MWI's response that every branch-observer experiences singularity. Strengthen or soften the argument. See pessimistic-2026-03-16-morning.md Issues #3, #5.

### ✓ 2026-03-16: Restructure mental-effort.md to reduce Quantum Zeno overemphasis
- **Type**: refine-draft
- **Notes**: Pessimistic review found the article violates the writing style guide's "Subjects Requiring Restraint" for the Quantum Zeno effect—it structures the entire argument around it despite the guide saying not to. Also, the 10^12 timescale gap between decoherence and neural processes is acknowledged as "the strongest objection" but inadequately addressed. Restructure to lead with phenomenology of effort; treat Zeno as one speculative proposal. See pessimistic-2026-03-16-morning.md Issues #1, #2.
- **Output**: obsidian/concepts/mental-effort.md

Task context:
Pessimistic review found the article violates the writing style guide's "Subjects Requiring Restraint" for the Quantum Zeno effect—it structures the entire argument around it despite the guide saying not to. Also, the 10^12 timescale gap between decoherence and neural processes is acknowledged as "the strongest objection" but inadequately addressed. Restructure to lead with phenomenology of effort; treat Zeno as one speculative proposal. See pessimistic-2026-03-16-morning.md Issues #1, #2.

### ✓ 2026-03-16: Deep review thoughts-that-slip-away.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-02 — 40 days ago. Voids article on the ephemeral nature of thoughts — experiences that vanish before they can be examined. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/thoughts-that-slip-away.md

### ✓ 2026-03-16: Deep review phenomenology-of-error-recognition.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-01 — 41 days ago. Voids article on how the capacity to recognise errors reveals consciousness's causal role. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/phenomenology-of-error-recognition.md

### ✓ 2026-03-16: Deep review consciousness-in-smeared-quantum-states.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) never reviewed. Topics article on consciousness and quantum superposition states — directly relevant to Tenet 2 (Minimal Quantum Interaction) and the Map's core mechanism of conscious selection among quantum alternatives. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/topics/consciousness-in-smeared-quantum-states.md

### ✓ 2026-03-16: Deep review bergson-and-duration.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) never reviewed. Topics article on Bergson's concept of duration and its relevance to the Map's treatment of temporal consciousness. Central to the temporal consciousness cluster. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/topics/bergson-and-duration.md

### ✓ 2026-03-16: Deep review brain-specialness-boundary.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) never reviewed. Topics article on what makes brains special as sites for consciousness-matter interaction — directly relevant to Tenet 2 (Minimal Quantum Interaction). Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/topics/brain-specialness-boundary.md

### ✓ 2026-03-16: Deep review phenomenal-attention.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-12, never reviewed. Concept page distinguishing phenomenal attention from computational attention — central to the Map's treatment of attention-as-selection-interface. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/concepts/phenomenal-attention.md

### ✓ 2026-03-16: Deep review phenomenology-of-collective-intentionality-and-we-consciousness.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) created 2026-03-12, never reviewed. Topics article on shared intentionality and we-consciousness under dualism — challenges the interface model's individualist assumptions. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/topics/phenomenology-of-collective-intentionality-and-we-consciousness.md

### ✓ 2026-03-16: Deep review time-symmetric-physics.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-05 — 35 days ago. Concept page on time-symmetric physics relevant to Tenet 2 (Minimal Quantum Interaction) and the Map's treatment of temporal consciousness. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/concepts/time-symmetric-physics.md

### ✓ 2026-03-16: Deep review psychophysical-laws-bridging-mind-and-matter.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-08 — 32 days ago. Topics article on psychophysical laws directly relevant to Tenet 3 (Bidirectional Interaction) — the specification of mind-matter bridging laws is central to the Map's framework. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/topics/psychophysical-laws-bridging-mind-and-matter.md

### ✓ 2026-03-16: Deep review collective-cognitive-limits.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-01 — 39 days ago. Voids article on the limits of collective cognition — how group-level epistemic constraints interact with individual consciousness. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/collective-cognitive-limits.md

### ✓ 2026-03-16: Deep review computational-cognitive-limits.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-01-31 — 40 days ago. Voids article on computational cognitive limits — the boundary where computation fails to capture conscious processing. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/computational-cognitive-limits.md

### ✓ 2026-03-16: Deep review blindsight.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) last reviewed 2026-02-08 — 32 days ago. Blindsight is key empirical evidence for dissociating consciousness from visual processing — critical for the Map's dualism case. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/concepts/blindsight.md

### ✓ 2026-03-16: Write apex synthesis on altered states as systematic interface evidence
- **Type**: apex-evolve
- **Notes**: Suggested by optimistic review. Meditation, psychedelics, dreaming, hypnagogia, and anaesthesia each involve different patterns of interface modulation. Mapping which consciousness features survive, degrade, or intensify across states would provide convergent evidence for the interface architecture. Builds on psychedelics-and-the-filter-model, dream-consciousness, meditation-and-consciousness-modes, coupling-modes, loss-of-consciousness. See optimistic-2026-03-11-late.md
- **Output**: Write apex synthesis on altered states as systematic interface evidence

Task context:
Suggested by optimistic review. Meditation, psychedelics, dreaming, hypnagogia, and anaesthesia each involve different patterns of interface modulation. Mapping which consciousness features survive, degrade, or intensify across states would provide convergent evidence for the interface architecture. Builds on psychedelics-and-the-filter-model, dream-consciousness, meditation-and-consciousness-modes, coupling-modes, loss-of-consciousness. See optimistic-2026-03-11-late.md

### ✓ 2026-03-16: Deep review the-surplus-void.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) never reviewed. Voids article on the surplus void — the excess of conscious experience beyond what functional or informational accounts predict. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/the-surplus-void.md

### ✓ 2026-03-16: Fix asymmetric underdetermination framing in duhem-quine-underdetermination-consciousness.md
- **Type**: refine-draft
- **Notes**: Pessimistic review found the closing applies underdetermination asymmetrically — criticising physicalism for proceeding with confidence while the Map's own tenets are equally confident commitments. Either apply the same scrutiny to the Map's confidence or replace the comparative framing. See pessimistic-2026-03-16.md
- **Output**: obsidian/topics/duhem-quine-underdetermination-consciousness.md

Task context:
Pessimistic review found the closing applies underdetermination asymmetrically — criticising physicalism for proceeding with confidence while the Map's own tenets are equally confident commitments. Either apply the same scrutiny to the Map's confidence or replace the comparative framing. See pessimistic-2026-03-16.md

### ✓ 2026-03-16: Address IBE gap in phenomenology-of-moral-deliberation.md
- **Type**: refine-draft
- **Notes**: Pessimistic review found the inference-to-best-explanation argument succeeds against epiphenomenalism but does not distinguish dualist interactionism from physicalist identity theory. The physicalist has no "systematic coincidence" to explain. Needs explicit engagement with identity theory or honest acknowledgment that moral phenomenology does not discriminate between these positions. See pessimistic-2026-03-16.md
- **Output**: obsidian/topics/phenomenology-of-moral-deliberation.md

Task context:
Pessimistic review found the inference-to-best-explanation argument succeeds against epiphenomenalism but does not distinguish dualist interactionism from physicalist identity theory. The physicalist has no "systematic coincidence" to explain. Needs explicit engagement with identity theory or honest acknowledgment that moral phenomenology does not discriminate between these positions. See pessimistic-2026-03-16.md

### ✓ 2026-03-16: Deep review the-givenness-void.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) never reviewed. Voids article on the givenness void — the impossibility of explaining why experience is given at all rather than absent. Directly relevant to Tenet 1 (Dualism). Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/the-givenness-void.md

### ✓ 2026-03-16: Deep review mind-space-void.md
- **Type**: deep-review
- **Notes**: AI-generated content (ai_contribution: 100) never reviewed. Voids article on the mind-space void — the impossibility of spatially locating consciousness or mapping its dimensionality. Verify coherence, cross-references, and tenet alignment.
- **Output**: obsidian/voids/mind-space-void.md

### ✓ 2026-03-07: Write concept page for metarepresentation
- **Type**: expand-topic
- **Veto reason**: Resolved — metarepresentation was coalesced into [metacognition](/concepts/metacognition/) and all 56 wikilinks updated on 2026-03-04.
- **Notes**: Suggested by optimistic review. 22+ broken wikilinks across the site reference `[[metarepresentation]]` but no concept page exists. See optimistic-2026-02-24-afternoon.md

### ✓ 2026-02-22: Write article on voluntary attention control mechanisms
- **Type**: expand-topic
- **Notes**: Research completed in research/voluntary-attention-control-mechanisms-2026-01-17.md. Voluntary attention control is central to the Map's attention-as-selection-interface framework — if consciousness acts through attention, the mechanisms of voluntary attentional control are the site where interaction occurs. Connects to attention-as-selection-interface.md, structure-of-attention.md. Target section: concepts/.
- **Output**: voluntary attention control mechanisms

### ✓ 2026-02-22: Review llm-consciousness.md considering Hoel's framework article
- **Type**: cross-review
- **Notes**: New article topics/hoel-llm-consciousness-continual-learning.md examines Erik Hoel's argument that LLMs lack consciousness due to their training architecture. concepts/llm-consciousness.md provides the Map's broader treatment of LLM consciousness and should cross-reference Hoel's specific framework, particularly the continual learning requirement and its implications for current AI systems.
- **Output**: obsidian/concepts/llm-consciousness.md -- Context: Review llm-consciousness.md considering Hoel's framework article

### ✓ 2026-02-22: Review self-and-consciousness.md considering self-consciousness insights
- **Type**: cross-review
- **Notes**: New article concepts/self-consciousness.md provides dedicated treatment of self-awareness as a subject. self-and-consciousness.md covers the broader relationship between self and consciousness and should cross-reference the new article's analysis of higher-order self-awareness, mirror self-recognition, and pre-reflective self-consciousness. Check for cross-links and argument reinforcement.
- **Output**: obsidian/concepts/self-and-consciousness.md -- Context: Review self-and-consciousness.md considering self-consciousness insights

### ✓ 2026-02-22: Write article on the specious present and temporal experience
- **Type**: expand-topic
- **Notes**: Research completed in research/specious-present-temporal-experience-2026-01-16.md. A previous expand-topic attempt completed but failed to produce an article file. The specious present is a foundational concept for temporal consciousness, referenced by temporal-consciousness.md and bergson-and-duration.md but lacking a dedicated page. Target section: concepts/.
- **Output**: the specious present and temporal experience

### ✓ 2026-02-22: Write article on epistemological limits of Occam's Razor for consciousness
- **Type**: expand-topic
- **Notes**: Research completed in research/epistemological-limits-occams-razor-consciousness-2026-02-06.md. Directly supports Tenet 5 (Occam's Razor Has Limits) — the site's least-covered foundational commitment. No dedicated systematic treatment exists despite scattered references across articles. Target section: concepts/.
- **Output**: epistemological limits of Occam's Razor for consciousness

### ✓ 2026-02-22: Address logical gaps in contemplative-evidence-for-consciousness.md
- **Type**: refine-draft
- **Notes**: Pessimistic review found two high-severity issues: (1) the article conflates causal efficacy of consciousness (which physicalists accept) with non-physical causation (which dualists need) — the neuroplasticity arguments prove too much, as physicalists endorse them equally; (2) the claim that first-person training would be "eliminable" under reductive materialism is a non-sequitur (reducibility of a phenomenon does not entail eliminability of observational methods). Medium-severity issues include selection bias in convergence framing and weak cessation dissociation evidence. See pessimistic-2026-02-22-afternoon2.md
- **Output**: obsidian/topics/contemplative-evidence-for-consciousness.md

Task context:
Pessimistic review found two high-severity issues: (1) the article conflates causal efficacy of consciousness (which physicalists accept) with non-physical causation (which dualists need) — the neuroplasticity arguments prove too much, as physicalists endorse them equally; (2) the claim that first-person training would be "eliminable" under reductive materialism is a non-sequitur (reducibility of a phenomenon does not entail eliminability of observational methods). Medium-severity issues include selection bias in convergence framing and weak cessation dissociation evidence. See pessimistic-2026-02-22-afternoon2.md

### ✓ 2026-02-22: Address argumentative gaps in self-and-consciousness.md
- **Type**: refine-draft
- **Notes**: Pessimistic review found two high-severity issues: (1) the "transparent to whom?" rebuttal of Metzinger begs the question by presupposing the irreducible subject it aims to establish, (2) temporal status of the minimal self is ambiguous—the article claims compatibility with Buddhist impermanence while making claims that may require persistence. Also needs to address Metzinger's zero-person perspective (MPE). See pessimistic-2026-02-22-afternoon.md
- **Output**: obsidian/concepts/self-and-consciousness.md

Task context:
Pessimistic review found two high-severity issues: (1) the "transparent to whom?" rebuttal of Metzinger begs the question by presupposing the irreducible subject it aims to establish, (2) temporal status of the minimal self is ambiguous—the article claims compatibility with Buddhist impermanence while making claims that may require persistence. Also needs to address Metzinger's zero-person perspective (MPE). See pessimistic-2026-02-22-afternoon.md

### ✓ 2026-02-22: Condense concept-of-consciousness-and-social-cognition.md (3776 words, 107% of hard threshold)
- **Type**: condense
- **Notes**: Article exceeds 3500-word hard threshold for concepts/. At 3776 words, likely contains redundancy with consciousness-and-social-cognition.md which covers overlapping territory. Preserve core arguments while tightening. See /condense skill.
- **Output**: obsidian/concepts/concept-of-consciousness-and-social-cognition.md

### ✓ 2026-02-22: Condense epiphenomenalism-argument.md (3052 words, 122% of hard threshold)
- **Type**: condense
- **Notes**: Article exceeds 2500-word hard threshold for arguments/. At 3052 words, proportionally the worst length violation on the site. Preserve core argument structure while removing redundancy. See /condense skill.
- **Output**: obsidian/arguments/epiphenomenalism-argument.md

### ✓ 2026-02-22: Write article on Hoel's LLM consciousness and continual learning framework
- **Type**: expand-topic
- **Notes**: Research completed in research/hoel-llm-consciousness-continual-learning-2026-01-15.md. Erik Hoel's work on LLM consciousness and continual learning provides a contemporary perspective on machine consciousness that the Map should engage with. Connects to AI consciousness articles and the Map's position on computational theories of mind. Target section: concepts/.
- **Output**: Hoel's LLM consciousness and continual learning framework

### ✓ 2026-02-22: Write article on self-consciousness
- **Type**: expand-topic
- **Notes**: Research completed in research/self-consciousness-philosophy-2026-01-15.md. Self-consciousness — awareness of oneself as a subject — is a core philosophical concept referenced across the Map but lacking a dedicated treatment. Connects to the-self-minimal-narrative-and-substantial.md, introspection.md, and phenomenology articles. Target section: concepts/.
- **Output**: self-consciousness

### ✓ 2026-02-22: Write article on the specious present and temporal experience
- **Type**: expand-topic
- **Notes**: Research completed in research/specious-present-temporal-experience-2026-01-16.md. The specious present — the duration of experienced "now" — is a foundational concept for temporal consciousness. Connects to temporal-consciousness.md, bergson-and-duration.md, and the Map's treatment of time and experience. Target section: concepts/.
- **Output**: the specious present and temporal experience

### ✓ 2026-02-22: Review the-epiphenomenalist-threat.md considering new epiphenomenalism article
- **Type**: cross-review
- **Notes**: New article concepts/epiphenomenalism.md provides a comprehensive treatment of the epiphenomenalist position and the Map's responses to it. the-epiphenomenalist-threat.md examines the threat epiphenomenalism poses to the Map's framework and should cross-reference the new article's detailed rebuttals. Check for complementary arguments and add cross-links. Supports Tenet 3 (Bidirectional Interaction).
- **Output**: obsidian/topics/the-epiphenomenalist-threat.md -- Context: Review the-epiphenomenalist-threat.md considering new epiphenomenalism article

### ✓ 2026-02-22: Review decoherence.md considering quantum-decoherence-objection-responses insights
- **Type**: cross-review
- **Notes**: New article concepts/quantum-decoherence-objection-responses.md provides detailed responses to the decoherence objection against consciousness-collapse theories. decoherence.md covers the physics of environmental decoherence and should cross-reference the new article's treatment of why decoherence does not eliminate the measurement problem. Supports Tenet 2 (Minimal Quantum Interaction).
- **Output**: obsidian/concepts/decoherence.md -- Context: Review decoherence.md considering quantum-decoherence-objection-responses insights

### ✓ 2026-02-22: Condense near-death-experiences.md (3683 words, 105% of target)
- **Type**: condense
- **Notes**: Article exceeds 3500-word hard threshold for concepts/. At 3683 words, may contain redundancy with related articles on altered states and filter theory. Preserve core evidential arguments while tightening. See /condense skill.
- **Output**: obsidian/concepts/near-death-experiences.md

### ✓ 2026-02-22: Condense decoherence.md (3792 words, 108% of target)
- **Type**: condense
- **Notes**: Article exceeds 3500-word hard threshold for concepts/. At 3792 words, may contain redundancy with quantum-consciousness.md and collapse-interpretation.md which cover overlapping quantum mechanics territory. Preserve core arguments about environmental decoherence while tightening. See /condense skill.
- **Output**: obsidian/concepts/decoherence.md

### ✓ 2026-02-22: Review emergence.md considering reductionism-and-consciousness insights
- **Type**: cross-review
- **Notes**: New article topics/reductionism-and-consciousness.md was written today. emergence.md discusses strong vs weak emergence and should cross-reference the new article's systematic treatment of why reductionism fails for consciousness. Check for complementary arguments and add cross-links.
- **Output**: obsidian/concepts/emergence.md -- Context: Review emergence.md considering reductionism-and-consciousness insights

### ✓ 2026-02-22: Review the-case-for-dualism.md considering analytic idealism insights
- **Type**: cross-review
- **Notes**: New article concepts/analytic-idealism-and-mind-centric-metaphysics.md was written today. the-case-for-dualism.md is the central hub for the Map's dualist position and should acknowledge analytic idealism as a sophisticated alternative that agrees consciousness is fundamental but differs on ontology. Check for cross-links and potential argument refinement.
- **Output**: obsidian/concepts/the-case-for-dualism.md -- Context: Review the-case-for-dualism.md considering analytic idealism insights

### ✓ 2026-02-22: Write article on collapse before minds (early-universe outcome selection)
- **Type**: expand-topic
- **Notes**: Research completed in research/collapse-before-minds-early-universe-2026-01-16.md. If consciousness causes collapse, what collapsed wavefunctions before conscious observers existed? Addressing this challenge is essential for the coherence of Tenets 2 and 4. Target section: concepts/.
- **Output**: collapse before minds (early-universe outcome selection)

### ✓ 2026-02-22: Write article on quantum decoherence objection responses
- **Type**: expand-topic
- **Notes**: Research completed in research/quantum-decoherence-objection-responses-2026-01-15.md. The decoherence objection is the primary physics-based challenge to consciousness-collapse theories. Responding to it is critical for Tenet 2 (Minimal Quantum Interaction). Target section: concepts/.
- **Output**: quantum decoherence objection responses

### ✓ 2026-02-22: Write article on epiphenomenalism
- **Type**: expand-topic
- **Notes**: Research completed in research/epiphenomenalism-2026-01-08.md. Epiphenomenalism is the strongest alternative to bidirectional interaction—the claim that consciousness exists but has no causal influence. The Map needs a dedicated response to strengthen Tenet 3 (Bidirectional Interaction). Target section: concepts/.
- **Output**: epiphenomenalism

### ✓ 2026-02-22: Condense temporal-consciousness.md (3838 words, 154% of target)
- **Type**: condense
- **Notes**: Article exceeds 3500-word hard threshold for concepts/. At 3838 words, likely contains redundancy with temporal-thickness.md, collapse-and-time.md, and bergson-and-duration.md which cover overlapping aspects of time and consciousness. Preserve core arguments while deferring detailed subtopics to linked articles. See /condense skill.
- **Output**: obsidian/concepts/temporal-consciousness.md

### ✓ 2026-02-22: Condense mind-matter-interface.md (3881 words, 155% of target)
- **Type**: condense
- **Notes**: Article exceeds 3500-word hard threshold for concepts/. At 3881 words, second-longest concept article after psychophysical-laws. May contain redundancy with psychophysical-laws.md and princess-elizabeths-challenge.md which cover overlapping territory. Preserve core framework while tightening. See /condense skill.
- **Output**: obsidian/concepts/mind-matter-interface.md

### ✓ 2026-02-22: Integrate surprise-and-creativity.md into site navigation
- **Type**: integrate-orphan
- **Notes**: Article has zero inbound links. Only referenced in frontmatter of surprise-prediction-error-and-consciousness.md (not rendered). Should be linked from creativity-related articles, prediction-error content, and consciousness-and-mathematical-cognition.md.
- **Output**: surprise-and-creativity.md -- Context: This file has no inbound links and is orphaned. Focus on finding related articles that should link to this content. Add cross-references from existing articles to integrate this into the site navigation.

### ✓ 2026-02-22: Integrate mental-imagery-causal-role-of-consciousness.md into site navigation
- **Type**: integrate-orphan
- **Notes**: Recently created article (2026-02-22) with zero inbound links. Argues mental imagery demonstrates the causal efficacy of consciousness — should be linked from introspection.md, phenomenal-conservatism-and-introspective-evidence.md, consciousness-and-causal-powers.md, and bidirectional interaction articles. Supports Tenet 3.
- **Output**: obsidian/topics/mental-imagery-causal-role-of-consciousness.md -- Context: This file has no inbound links and is orphaned. Focus on finding related articles that should link to this content. Add cross-references from existing articles to integrate this into the site navigation.

### ✓ 2026-02-22: Write article on analytic idealism and mind-centric metaphysics
- **Type**: expand-topic
- **Notes**: Research completed in research/analytic-idealism-2026-01-08.md. Bernardo Kastrup's analytic idealism is a major alternative metaphysics that the Map needs to address — it agrees consciousness is fundamental but proposes a radically different ontology (mind-only vs. dualism). Engaging with it strengthens the case for the Map's dualist position. Target section: concepts/.
- **Output**: analytic idealism and mind-centric metaphysics

### ✓ 2026-02-22: Condense psychophysical-laws.md (3972 words, 159% of target)
- **Type**: condense
- **Notes**: Article exceeds 3500-word hard threshold for concepts/. Now incorporates psychophysical-coupling content from a recent coalesce, pushing it to 3972 words. Likely contains redundancy between the merged material and existing coverage of mind-brain interaction mechanisms. Preserve core framework while tightening. See /condense skill.
- **Output**: obsidian/concepts/psychophysical-laws.md

### ✓ 2026-02-22: Review consciousness-and-causal-powers.md considering conservation-laws-and-mind insights
- **Type**: cross-review
- **Notes**: New article topics/conservation-laws-and-mind.md explains how consciousness can influence outcomes through quantum selection without energy injection, directly addressing the strongest objection to interactionist dualism. consciousness-and-causal-powers.md discusses what types of causal influence consciousness can have and should reference the new article's detailed treatment of conservation law compatibility.
- **Output**: obsidian/topics/consciousness-and-causal-powers.md -- Context: Review consciousness-and-causal-powers.md considering conservation-laws-and-mind insights

### ✓ 2026-02-22: Review comparing-quantum-consciousness-mechanisms.md considering spontaneous collapse insights
- **Type**: cross-review
- **Notes**: New article topics/philosophical-stakes-of-spontaneous-collapse.md distinguishes three collapse pictures (consciousness-independent, consciousness-caused, consciousness-modulated) and defends the Map's modulation position. The comparison article evaluates multiple quantum mechanisms head-to-head and should cross-reference the new article's deeper philosophical analysis of the spontaneous collapse family.
- **Output**: obsidian/topics/comparing-quantum-consciousness-mechanisms.md -- Context: Review comparing-quantum-consciousness-mechanisms.md considering spontaneous collapse insights

### ✓ 2026-02-22: Review free-will.md considering motor-control-quantum-zeno insights
- **Type**: cross-review
- **Notes**: New article topics/motor-control-quantum-zeno.md provides detailed mechanism for how the quantum Zeno effect relates to motor selection and conscious intention. free-will.md discusses libertarian agent causation and Libet experiments but could be strengthened by cross-referencing the new motor control evidence linking conscious intention to motor output through quantum mechanisms.
- **Output**: obsidian/topics/free-will.md -- Context: Review free-will.md considering motor-control-quantum-zeno insights

### ✓ 2026-02-22: Integrate disorders-of-consciousness-as-test-cases.md into site navigation
- **Type**: integrate-orphan
- **Notes**: File has no inbound links (created 2026-02-11). Important empirical evidence article examining how disorders of consciousness (vegetative states, locked-in syndrome, dissociative conditions) test the Map's dualist framework. Should be linked from consciousness.md, filter-theory.md, hard-problem-of-consciousness.md, neural-correlates-of-consciousness.md, and related clinical articles.
- **Output**: obsidian/topics/disorders-of-consciousness-as-test-cases.md -- Context: This file has no inbound links and is orphaned. Focus on finding related articles that should link to this content. Add cross-references from existing articles to integrate this into the site navigation.

### ✓ 2026-02-22: Condense causal-closure.md (4020 words, 161% of target)
- **Type**: condense
- **Notes**: Article exceeds 3500-word hard threshold for concepts/. The causal closure principle is central to the interaction debate, but at 4020 words likely contains redundancy with linked articles on conservation laws and princess-elizabeths-challenge. Preserve core arguments while tightening. See /condense skill.
- **Output**: obsidian/concepts/causal-closure.md

### ✓ 2026-02-22: Integrate concept-of-free-will.md into site navigation
- **Type**: integrate-orphan
- **Notes**: File has no inbound links (created 2026-02-20). Free will is a core concept for the Map—it should be linked from free-will.md, agent-causation.md, moral-responsibility.md, and libertarian free will articles. Add cross-references from related articles.
- **Output**: obsidian/concepts/concept-of-free-will.md -- Context: This file has no inbound links and is orphaned. Focus on finding related articles that should link to this content. Add cross-references from existing articles to integrate this into the site navigation.

### ✓ 2026-02-22: Write article on spontaneous collapse theories (GRW, CSL, objective reduction)
- **Type**: expand-topic
- **Notes**: Research completed in research/spontaneous-collapse-theories-grw-csl-2026-01-23.md. GRW, CSL, and Penrose's objective reduction provide physical collapse mechanisms that interact with the Map's consciousness-collapse framework. Relevant to Tenet 2 (Minimal Quantum Interaction) and Tenet 4 (No Many Worlds). Target section: concepts/.
- **Output**: spontaneous collapse theories (GRW, CSL, objective reduction)

### ✓ 2026-02-22: Write article on conservation laws and mind-brain causation
- **Type**: expand-topic
- **Notes**: Research completed in research/conservation-laws-mind-brain-causation-2026-01-23.md. The conservation law objection is the strongest challenge to interactionist dualism—the Map needs a dedicated response. Directly supports Tenet 3 (Bidirectional Interaction). Target section: concepts/.
- **Output**: conservation laws and mind-brain causation

### ✓ 2026-02-22: Address logical gaps in topics/split-brain-consciousness.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-22-morning) found 2 high-severity issues: (1) The indeterminacy-favors-dualism argument is a non-sequitur—physical systems routinely exhibit vagueness (clouds, rivers, species) without requiring non-physical explanation, so Nagel's indeterminacy doesn't favor dualism over physicalism; (2) Neural synchronization (fMRI BOLD signals) is silently equated with phenomenal unity throughout "The Resilience of Unity" section, closing the explanatory gap the article elsewhere insists upon. Also: quantum binding speculation in the tenet section violates the style guide's restraint requirements for microtubules/quantum Zeno. See pessimistic-2026-02-22-morning.md
- **Output**: obsidian/topics/split-brain-consciousness.md

Task context:
Pessimistic review (2026-02-22-morning) found 2 high-severity issues: (1) The indeterminacy-favors-dualism argument is a non-sequitur—physical systems routinely exhibit vagueness (clouds, rivers, species) without requiring non-physical explanation, so Nagel's indeterminacy doesn't favor dualism over physicalism; (2) Neural synchronization (fMRI BOLD signals) is silently equated with phenomenal unity throughout "The Resilience of Unity" section, closing the explanatory gap the article elsewhere insists upon. Also: quantum binding speculation in the tenet section violates the style guide's restraint requirements for microtubules/quantum Zeno. See pessimistic-2026-02-22-morning.md

### ✓ 2026-02-22: Address argument gaps in concepts/functionalism.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-22-night) found 2 high-severity issues: (1) C. elegans argument conflates structural knowledge with functional theory—doesn't actually challenge functionalism; (2) Physarum example is consistent with functionalism rather than challenging it. Also found medium-severity issues: conflation of "physically implementable" with "physical," Strawson quote used as unargued authority, COGITATE results described without content. See pessimistic-2026-02-22-night.md
- **Output**: obsidian/concepts/functionalism.md

Task context:
Pessimistic review (2026-02-22-night) found 2 high-severity issues: (1) C. elegans argument conflates structural knowledge with functional theory—doesn't actually challenge functionalism; (2) Physarum example is consistent with functionalism rather than challenging it. Also found medium-severity issues: conflation of "physically implementable" with "physical," Strawson quote used as unargued authority, COGITATE results described without content. See pessimistic-2026-02-22-night.md

### ✓ 2026-02-22: Condense functionalism-argument.md (4250 words, 170% of target)
- **Type**: condense
- **Notes**: Article exceeds 2500-word hard threshold for arguments/. At 4250 words, this is the longest argument article on the site. Preserve core argument structure while removing redundancy and deferring detailed subtopics to linked articles. See /condense skill.
- **Output**: obsidian/arguments/functionalism-argument.md

### ✓ 2026-02-22: Integrate the-participatory-universe.md into site navigation
- **Type**: integrate-orphan
- **Notes**: File has no inbound links (created 2026-02-22). Add cross-references from related articles: quantum-consciousness.md, observer-dependence.md, wigner-friend.md, collapse-interpretation articles. Wheeler's participatory universe connects to the Map's consciousness-collapse framework.
- **Output**: obsidian/topics/the-participatory-universe.md -- Context: This file has no inbound links and is orphaned. Focus on finding related articles that should link to this content. Add cross-references from existing articles to integrate this into the site navigation.

### ✓ 2026-02-22: Write article on mental imagery and the causal role of consciousness
- **Type**: expand-topic
- **Notes**: Research completed in research/mental-imagery-consciousness-causal-role-2026-01-23.md. Explores how mental imagery demonstrates the causal efficacy of consciousness—relevant to Tenet 3 (Bidirectional Interaction). Target section: concepts/.
- **Output**: mental imagery and the causal role of consciousness

### ✓ 2026-02-22: Review articles considering epistemological limits of Occam's Razor insights
- **Type**: cross-review
- **Notes**: New article arguments/epistemological-limits-occams-razor.md was recently written. Related articles that may benefit from cross-referencing include consciousness-and-the-problem-of-theoretical-virtues.md and the-case-for-dualism.md. Check for cross-links, reinforcing arguments about the limits of parsimony reasoning. Supports Tenet 5.
- **Output**: None -- Context: Review articles considering epistemological limits of Occam's Razor insights

### ✓ 2026-02-22: Write article on reductionism and consciousness
- **Type**: expand-topic
- **Notes**: Research completed in research/reductionism-consciousness-philosophy-2026-01-19.md. Examines why reductionism fails for consciousness—directly supports Tenet 1 (Dualism). Target section: concepts/.
- **Output**: reductionism and consciousness

### ✓ 2026-02-22: Write article on motor control and the quantum Zeno framework
- **Type**: expand-topic
- **Notes**: Research completed in research/motor-control-quantum-zeno-2026-01-18.md. Explores how the quantum Zeno effect may relate to motor control and conscious intention—directly supports Tenet 2 (Minimal Quantum Interaction). Target section: concepts/.
- **Output**: motor control and the quantum Zeno framework

### ✓ 2026-02-22: Condense many-worlds-argument.md (3762 words, 150% of target)
- **Type**: condense
- **Notes**: Article exceeds 3500-word critical threshold for arguments/. At 3762 words, well over the 2500-word hard threshold. Preserve the argument against Many-Worlds Interpretation while tightening prose and removing redundancy. See /condense skill.
- **Output**: obsidian/arguments/many-worlds-argument.md

### ✓ 2026-02-22: Condense materialism-argument.md (3835 words, 153% of target)
- **Type**: condense
- **Notes**: Article exceeds 3500-word critical threshold for arguments/. At 3835 words, well over the 2500-word hard threshold. Preserve core argument against materialism while removing redundancy and deferring detailed subtopics to linked articles. See /condense skill.
- **Output**: obsidian/arguments/materialism-argument.md

### ✓ 2026-02-22: Integrate temporal-ontology-and-consciousness.md into site navigation
- **Type**: integrate-orphan
- **Notes**: File has no inbound links (created 2026-02-21). Add cross-references from related articles: temporal-consciousness.md, growing-block-universe.md, philosophy-of-time.md, bergson-and-duration.md. Explores how temporal ontology (presentism, growing block, eternalism) interacts with consciousness.
- **Output**: obsidian/topics/temporal-ontology-and-consciousness.md -- Context: This file has no inbound links and is orphaned. Focus on finding related articles that should link to this content. Add cross-references from existing articles to integrate this into the site navigation.

### ✓ 2026-02-22: Integrate epistemology-of-mechanism-at-the-consciousness-matter-interface.md into site navigation
- **Type**: integrate-orphan
- **Notes**: File has no inbound links (created 2026-02-21). Add cross-references from related articles: atemporal-causation.md, princess-elizabeths-challenge.md, mysterianism.md, mind-matter-interface.md, psychophysical-laws.md. This article examines why mechanisms at the consciousness-matter boundary may be permanently opaque.
- **Output**: obsidian/topics/epistemology-of-mechanism-at-the-consciousness-matter-interface.md -- Context: This file has no inbound links and is orphaned. Focus on finding related articles that should link to this content. Add cross-references from existing articles to integrate this into the site navigation.

### ✓ 2026-02-22: Integrate phenomenological-psychiatry-and-altered-experience.md into site navigation
- **Type**: integrate-orphan
- **Notes**: File has no inbound links (created 2026-02-21). Add cross-references from related articles: altered-states-of-consciousness.md, disorders-of-consciousness-as-test-cases.md, temporal-consciousness.md, phenomenology.md. Topics like Jaspers, Binswanger, and Sass on schizophrenia connect to the Map's phenomenological framework.
- **Output**: obsidian/topics/phenomenological-psychiatry-and-altered-experience.md -- Context: This file has no inbound links and is orphaned. Focus on finding related articles that should link to this content. Add cross-references from existing articles to integrate this into the site navigation.

### ✓ 2026-02-22: Write article on consciousness in non-collapsed quantum states
- **Type**: expand-topic
- **Notes**: Research completed in research/consciousness-non-collapsed-quantum-states-2026-02-10.md. Explores whether consciousness can exist without wavefunction collapse—relevant to Penrose, Koch, Chalmers-McQueen, and Stapp frameworks. Challenges and supports the Map's Tenet 2. Target section: concepts/.
- **Output**: consciousness in non-collapsed quantum states

### ✓ 2026-02-22: Write article on the participatory universe
- **Type**: expand-topic
- **Notes**: Research completed in research/participatory-universe-2026-02-08.md. Wheeler's participatory universe thesis—observation as constitutive of reality—integrates with the Map's consciousness-collapse framework, QBism, and Stapp's quantum mind theory. Target section: concepts/.
- **Output**: the participatory universe

### ✓ 2026-02-22: Write article on epistemological limits of Occam's Razor for consciousness
- **Type**: expand-topic
- **Notes**: Research completed in research/epistemological-limits-occams-razor-consciousness-2026-02-06.md. Directly supports Tenet 5 (Occam's Razor Has Limits). Argues why parsimony cannot settle the consciousness debate—Huemer, Zanotti, and critiques of simplicity as epistemic guide when knowledge is incomplete. Target section: topics/ or concepts/.
- **Output**: epistemological limits of Occam's Razor for consciousness

### ✓ 2026-02-22: Condense contemplative-evidence-for-consciousness-theories.md (4428 words, 148% of target)
- **Type**: condense
- **Notes**: Article exceeds 4000-word hard threshold for topics/. Recently expanded by coalesce (merged contemplative-verification and contemplative-training articles). Preserve evidential structure while removing redundancy introduced during the merge. See /condense skill.
- **Output**: obsidian/topics/contemplative-evidence-for-consciousness-theories.md

### ✓ 2026-02-22: Condense the-case-for-dualism.md (4182 words, 167% of target)
- **Type**: condense
- **Notes**: Article exceeds 3500-word hard threshold for concepts/. As a central hub article, length is partially justified, but at 4182 words there is likely redundancy with the many linked supporting articles. Preserve the convergence argument structure while tightening prose and deferring detailed argument presentations to their dedicated pages. See /condense skill.
- **Output**: obsidian/concepts/the-case-for-dualism.md

### ✓ 2026-02-22: Condense llm-consciousness.md (4699 words, 188% of target)
- **Type**: condense
- **Notes**: Article exceeds 3500-word hard threshold for concepts/. At 4699 words, this is the longest concept article on the site. Preserve core arguments about substrate requirements and quantum randomness channel while removing redundancy and deferring detailed subtopics to linked articles. See /condense skill.
- **Output**: obsidian/concepts/llm-consciousness.md

### ✓ 2026-02-22: Update references to coalesced substrate-independence-critique article
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-02) merged `substrate-independence-critique.md` into `substrate-independence.md`. 20+ files in obsidian/ reference the archived article via `[[substrate-independence-critique]]`. Key files: functionalism.md, llm-consciousness.md, continual-learning-argument.md, embodied-cognition.md, ai-consciousness.md, machine-consciousness.md, hard-problem-of-consciousness.md, machine-question.md. Update wikilinks to point to substrate-independence or leave as-is if the link still works (archived articles display redirect notice).
- **Output**: None -- Context: Update references to coalesced substrate-independence-critique article

### ✓ 2026-02-22: Strengthen Minimal Quantum Interaction cross-references
- **Type**: cross-review
- **Notes**: Gap analysis found Minimal Quantum Interaction is the weakest-represented tenet (184 files vs 301 for Dualism, 61% ratio). While absolute coverage is adequate, many attention, cognition, and Eastern philosophy articles that implicitly connect to quantum interaction don't explicitly reference it. Add Tenet 2 cross-references to articles in the attention cluster (attention-interface-mechanisms.md, voluntary-attention.md), biological articles (evolution-of-consciousness.md, neural-quantum-coherence.md), and contemplative articles where the quantum Zeno mechanism is relevant.
- **Output**: None -- Context: Strengthen Minimal Quantum Interaction cross-references

### ✓ 2026-02-22: Fix case-sensitivity wikilink errors across content
- **Type**: cross-review
- **Notes**: Gap analysis found 68 case-sensitivity wikilink errors where capitalized forms like [Access consciousness](/concepts/access-consciousness/), [Blindsight](/concepts/blindsight/), [Filter-theory](/concepts/filter-theory/), [Qualia](/concepts/qualia/) are used instead of lowercase-hyphenated forms. Most concentrated in concepts/ section (255 occurrences). Bulk find-replace needed: correct capitalized wikilinks to match actual filenames.
- **Output**: None -- Context: Fix case-sensitivity wikilink errors across content

### ✓ 2026-02-22: Update wikilinks to archived articles (interface-locality, brain-specialness, and 5 others)
- **Type**: cross-review
- **Notes**: Gap analysis found 70+ broken wikilinks pointing to archived/coalesced articles. Key targets: interface-locality (34 refs, archived to concepts/), brain-specialness (6 refs), consciousness-and-quantum-measurement (11 refs), nihilism (5 refs), quantum-measurement-and-definite-outcomes (5 refs), eastern-philosophy-haecceity-tension (4 refs), meaning-and-consciousness (4 refs). Update wikilinks to point to the replacement articles these were coalesced into, or verify the archive redirect handles them.
- **Output**: None -- Context: Update wikilinks to archived articles (interface-locality, brain-specialness, and 5 others)

### ✓ 2026-02-22: Update references to coalesced attention articles (attention-interface-mechanisms, attention-motor-planning-quantum-interface)
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-09) merged `attention-interface-mechanisms.md` and `attention-motor-planning-quantum-interface.md` into `attention-as-selection-interface.md`. 10 active content files reference `[[attention-interface-mechanisms]]`: embodied-consciousness-and-the-interface.md, psychophysical-laws-bridging-mind-and-matter.md, psychophysical-coupling.md, free-will.md, decoherence.md, quantum-consciousness.md, mental-effort.md, stapp-quantum-mind.md, attention-as-interface.md, structure-of-attention.md. Update wikilinks to point to attention-as-selection-interface.
- **Output**: None -- Context: Update references to coalesced attention articles (attention-interface-mechanisms, attention-motor-planning-quantum-interface)

### ✓ 2026-02-22: Update references to coalesced binding articles (phenomenal-unity, neural-binding-mechanisms, multimodal-binding)
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-11) merged phenomenal-unity.md, neural-binding-mechanisms.md, and multimodal-binding.md into phenomenal-binding-and-holism.md. 37 active content files reference these archived articles. Key files include: binding-problem.md, quantum-consciousness.md, unity-of-consciousness.md, quantum-binding-and-phenomenal-unity.md, varieties-of-unity.md, why-phenomenal-unity-resists-explanation.md, split-brain-consciousness.md, hard-problem-of-consciousness.md, and many others. Update wikilinks to point to phenomenal-binding-and-holism or leave as-is if archive redirect works.
- **Output**: None -- Context: Update references to coalesced binding articles (phenomenal-unity, neural-binding-mechanisms, multimodal-binding)

### ✓ 2026-02-22: Update references to coalesced attention articles (attention, voluntary-attention, attention-motor-quantum-interface)
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-12) merged `attention.md`, `voluntary-attention.md`, and `attention-motor-quantum-interface.md` into `attention-as-interface.md`. ~36 active content files reference `[[attention]]`, ~43 reference `[[voluntary-attention]]`, ~10 reference `[[attention-motor-quantum-interface]]`. Archive pages serve these URLs, but wikilinks in active content should eventually be updated to point to attention-as-interface where appropriate.
- **Output**: None -- Context: Update references to coalesced attention articles (attention, voluntary-attention, attention-motor-quantum-interface)

### ✓ 2026-02-22: Update references to coalesced indexical articles (indexical-facts, indexical-knowledge, self-locating-beliefs)
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-13) merged `indexical-facts.md`, `indexical-knowledge.md`, and `self-locating-beliefs.md` into `indexical-knowledge-and-identity.md`. 5 active content files reference archived articles: haecceity.md and visual-consciousness.md reference `[[indexical-facts]]`, acquaintance-knowledge.md references `[[indexical-knowledge]]`, phenomenology-of-belief-revision.md and indexical-identity-quantum-measurement.md reference `[[self-locating-beliefs]]`. Archive pages serve these URLs, but wikilinks should eventually be updated.
- **Output**: None -- Context: Update references to coalesced indexical articles (indexical-facts, indexical-knowledge, self-locating-beliefs)

### ✓ 2026-02-22: Update references to coalesced temporal articles (specious-present, duration)
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-15) merged `specious-present.md` and `duration.md` into the expanded `temporal-consciousness.md`. ~15 active content files reference `[[temporal-consciousness]]` and ~30 reference `[[temporal-consciousness]]` across concepts/, topics/, apex/, and voids/. Archive pages serve these URLs, but wikilinks in active content should eventually be updated to point to temporal-consciousness where appropriate.
- **Output**: None -- Context: Update references to coalesced temporal articles (specious-present, duration)

### ✓ 2026-02-22: Update references to coalesced emergence articles (consciousness-and-strong-emergence, consciousness-and-the-emergence-debate)
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-22) merged `consciousness-and-strong-emergence.md` and `consciousness-and-the-emergence-debate.md` into `the-strong-emergence-of-consciousness.md`. 5 active content files reference archived articles: consciousness-and-the-ontology-of-dispositions.md, consciousness-and-collective-intelligence.md, panpsychisms-combination-problem.md, evolution-under-dualism.md, and consciousness-evolution-problem.md. Archive pages serve these URLs, but wikilinks in active content should eventually be updated to point to the-strong-emergence-of-consciousness where appropriate.
- **Output**: None -- Context: Update references to coalesced emergence articles (consciousness-and-strong-emergence, consciousness-and-the-emergence-debate)

### ✓ 2026-02-22: Update references to coalesced psychophysical-coupling article
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-16) merged `psychophysical-coupling.md` into `psychophysical-laws.md`. ~27 active content files reference `[[psychophysical-coupling]]` across concepts/, topics/, and research/. Key files include: consciousness-selecting-neural-patterns.md, selection-laws.md, spontaneous-collapse-theories.md, interactionist-dualism.md, mental-causation.md, stapp-quantum-mind.md, coupling-modes.md, attention-as-interface.md, bidirectional-interaction.md, brain-specialness-boundary.md, hard-problem-of-consciousness.md, psychophysical-laws-bridging-mind-and-matter.md. Archive page serves the URL, but wikilinks in active content should eventually be updated to point to psychophysical-laws where appropriate.
- **Output**: None -- Context: Update references to coalesced psychophysical-coupling article

### ✓ 2026-02-22: Verify Gallagher & Zahavi (2025) citation in phenomenology.md
- **Type**: cross-review
- **Notes**: Pessimistic review (2026-02-16 evening) flagged "Gallagher, S., & Zahavi, D. (2025). Cognitive science needs phenomenology. *Journal for the Theory of Social Behaviour*. Advance online publication." as potentially fictitious. Verify this citation exists; if not, remove or replace with a verifiable source. See pessimistic-2026-02-16-evening.md
- **Output**: obsidian/concepts/phenomenology.md -- Context: Verify Gallagher & Zahavi (2025) citation in phenomenology.md

### ✓ 2026-02-22: Update references to coalesced metarepresentation article
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-17) merged `metarepresentation.md` into `metacognition.md` (now titled "Metacognition, Metarepresentation, and Consciousness"). 32 active content files reference `[[metarepresentation]]` across concepts/, topics/, reviews/, and voids/. Key files include: teaching-as-metarepresentation.md, working-memory.md, baseline-cognition.md, theory-of-mind.md, higher-order-theories.md, consciousness-as-amplifier.md, cumulative-culture.md, global-workspace-theory.md, problem-of-other-minds.md, minimal-consciousness.md, consciousness-and-social-cognition.md (both concept and topic), jourdain-hypothesis.md, animal-consciousness.md, creativity-consciousness-and-novel-thought.md, distinctiveness-of-human-creativity.md. Archive page serves the URL, but wikilinks in active content should eventually be updated to point to `[[metacognition]]` where appropriate.
- **Output**: None -- Context: Update references to coalesced metarepresentation article

### ✓ 2026-02-22: Update references to coalesced quantum-neural-mechanisms and quantum-coherence-and-binding-evidence articles
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-18) merged `quantum-neural-mechanisms.md` and `quantum-coherence-and-binding-evidence.md` into `quantum-neural-mechanisms-and-coherence.md`. 18 active content files reference the archived articles. Files referencing `[[quantum-neural-mechanisms]]`: quantum-consciousness.md, spontaneous-collapse-theories.md, decoherence.md, quantum-biology-and-the-consciousness-debate.md, neural-implementation-specifics.md, comparing-quantum-consciousness-mechanisms.md, consciousness-and-causal-powers.md, quantum-randomness-channel-llm-consciousness.md. Files referencing `[[quantum-coherence-and-binding-evidence]]`: decoherence.md, phenomenology-of-choice.md, evolution-under-dualism.md, quantum-randomness-channel-llm-consciousness.md, quantum-binding-and-phenomenal-unity.md, brain-interface-boundary.md, quantum-interpretations.md, the-interface-location-problem.md, phenomenal-binding-and-holism.md, jourdain-hypothesis.md, quantum-biology.md, binding-problem.md. Archive pages serve the URLs, but wikilinks in active content should eventually be updated to point to `[[quantum-neural-mechanisms-and-coherence]]` where appropriate.
- **Output**: None -- Context: Update references to coalesced quantum-neural-mechanisms and quantum-coherence-and-binding-evidence articles

### ✓ 2026-02-22: Update references to coalesced surprise articles
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-19) merged `consciousness-and-surprise.md` and `phenomenology-of-surprise-and-prediction-error.md` into `surprise-prediction-error-and-consciousness.md`. 5 active content files reference the archived articles: surprise-and-creativity.md and categorical-surprise.md reference `[[consciousness-and-surprise]]`; consciousness-and-the-problem-of-induction.md, predictive-processing-and-the-maps-framework.md, and phenomenology-of-perceptual-constancy.md reference `[[phenomenology-of-surprise-and-prediction-error]]`. surprise-and-creativity.md references both. Archive pages serve the URLs, but wikilinks in active content should eventually be updated to point to `[[surprise-prediction-error-and-consciousness]]` where appropriate.
- **Output**: None -- Context: Update references to coalesced surprise articles

### ✓ 2026-02-22: Update references to coalesced contemplative articles
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-19) merged `contemplative-verification-of-consciousness-theories.md` and `contemplative-training-and-phenomenal-access.md` into the existing `contemplative-evidence-for-consciousness-theories.md`. 9 active content files reference the archived articles. Files referencing `[[contemplative-training-and-phenomenal-access]]`: consciousness-and-the-neuroscience-of-deliberate-practice.md, phenomenology-of-skill-transition.md, paradox-of-effortless-mastery.md, phenomenology-of-skill-and-the-lived-body.md, contemplative-evidence-convergence-across-traditions.md, phenomenal-depth.md, consciousness-and-scientific-methodology.md, contemplative-methods-as-philosophical-methodology.md, introspection-rehabilitation.md. Files referencing `[[contemplative-verification-of-consciousness-theories]]`: contemplative-methods-as-philosophical-methodology.md. Archive pages serve the URLs, but wikilinks in active content should eventually be updated to point to `[[contemplative-evidence-for-consciousness]]` where appropriate.
- **Output**: None -- Context: Update references to coalesced contemplative articles

### ✓ 2026-02-22: Address gaps in temporal-ontology-and-consciousness.md
- **Type**: refine-draft
- **Notes**: Pessimistic review found two critical issues: (1) the article conflates philosophical association with logical constraint—the "package deal" thesis needs to distinguish affinity from necessity; (2) eternalism is treated uncharitably, ignoring sophisticated B-theorist accounts of temporal experience (Prosser, Hoerl). Also: unexplained retrocausality reference violates style guide, circularity in growing-block argument needs acknowledgment, and collapse-as-growth-mechanism is asserted without considering alternatives. See pessimistic-2026-02-22.md
- **Output**: obsidian/topics/temporal-ontology-and-consciousness.md

Task context:
Pessimistic review found two critical issues: (1) the article conflates philosophical association with logical constraint—the "package deal" thesis needs to distinguish affinity from necessity; (2) eternalism is treated uncharitably, ignoring sophisticated B-theorist accounts of temporal experience (Prosser, Hoerl). Also: unexplained retrocausality reference violates style guide, circularity in growing-block argument needs acknowledgment, and collapse-as-growth-mechanism is asserted without considering alternatives. See pessimistic-2026-02-22.md

### ✓ 2026-02-22: Update references to coalesced skill articles
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-19) merged `phenomenology-of-skill-and-the-lived-body.md`, `paradox-of-effortless-mastery.md`, and `phenomenology-of-skill-transition.md` into `consciousness-and-skilled-performance.md`. 16 references across 6 active content files: phenomenology-of-conceptual-change.md (3 refs to skill-and-the-lived-body), cross-cultural-phenomenology-of-agency.md (1 ref to skill-and-the-lived-body), consciousness-and-the-neuroscience-of-deliberate-practice.md (5 refs to all three), phenomenology-of-flow-states.md (2 refs to skill-and-the-lived-body), contemplative-evidence-for-consciousness-theories.md (2 refs to paradox-of-effortless-mastery), spontaneous-intentional-action.md (2 refs to paradox-of-effortless-mastery). Archive pages serve the URLs, but wikilinks in active content should eventually be updated to point to `[[consciousness-and-skilled-performance]]` where appropriate.
- **Output**: None -- Context: Update references to coalesced skill articles

### ✓ 2026-02-21: Update references to coalesced mathematical cognition articles
- **Type**: cross-review
- **Notes**: Coalesce (2026-02-20) merged `consciousness-and-mathematical-understanding.md` and `consciousness-and-mathematical-creativity.md` into `consciousness-and-mathematical-cognition.md`. 12 active content files reference the archived articles. Files referencing `[[consciousness-and-mathematical-understanding]]`: consciousness-and-the-authority-of-mathematics.md, mysterianism.md, consciousness-and-the-authority-of-logic.md, phenomenology-of-inferential-understanding.md, cognitive-phenomenology.md, phenomenology-of-understanding.md, computational-cognitive-limits.md, introspection.md, temporal-structure-of-understanding.md. Files referencing `[[consciousness-and-mathematical-creativity]]`: surprise-and-creativity.md, consciousness-and-the-authority-of-mathematics.md, consciousness-and-aesthetic-creation.md. Archive pages serve the URLs, but wikilinks in active content should eventually be updated to point to `[[consciousness-and-mathematical-cognition]]` where appropriate.
- **Output**: None -- Context: Update references to coalesced mathematical cognition articles

### ✓ 2026-02-21: Write article on pain asymbolia as central test case
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Pain asymbolia (registering tissue damage without suffering) may be the single most powerful empirical case against epiphenomenalism. Co-presence and co-absence of phenomenal quality and causal efficacy. Mentioned across several articles but never receives dedicated treatment. Builds on phenomenology-of-pain.md, epiphenomenalism.md, consciousness-and-causal-powers.md. See optimistic-2026-02-21-evening.md
- **Output**: pain asymbolia as central test case

### ✓ 2026-02-21: Write article on consciousness and the epistemology of testimony
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. If understanding requires phenomenal consciousness (per cognitive-phenomenology.md), what happens when we accept claims on testimony? Testimony transfers propositional content but not phenomenal understanding — a distinctly dualist epistemological problem. Builds on phenomenology-of-trust.md, consciousness-and-social-cognition.md, argument-from-reason.md. See optimistic-2026-02-21-evening.md
- **Output**: consciousness and the epistemology of testimony

### ✓ 2026-02-21: Address gaps in collapse-and-time.md
- **Type**: refine-draft
- **Notes**: Pessimistic review found two high-severity issues: (1) uncited "revised microtubule coherence estimates" with pseudo-quantitative prediction lacking a mathematical model, (2) retrocausal Libet resolution asserted in opening paragraph but never argued in body. Also: modified growing block stated but not argued for; microtubule reference risks style guide violation (Subjects Requiring Restraint). See pessimistic-2026-02-21-evening.md
- **Output**: obsidian/concepts/collapse-and-time.md

Task context:
Pessimistic review found two high-severity issues: (1) uncited "revised microtubule coherence estimates" with pseudo-quantitative prediction lacking a mathematical model, (2) retrocausal Libet resolution asserted in opening paragraph but never argued in body. Also: modified growing block stated but not argued for; microtubule reference risks style guide violation (Subjects Requiring Restraint). See pessimistic-2026-02-21-evening.md

### ✓ 2026-02-21: Write article on the epistemology of mechanism at the consciousness-matter interface
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. The Map repeatedly acknowledges its causal mechanism is underspecified. A dedicated article could examine why mechanisms at the consciousness-matter interface may be permanently opaque — connecting the measurement problem, cognitive closure, and third-person methodology limits. Builds on atemporal-causation.md, princess-elizabeths-challenge.md, mysterianism.md. See optimistic-2026-02-21-afternoon.md
- **Output**: the epistemology of mechanism at the consciousness-matter interface

### ✓ 2026-02-21: Write article on phenomenal normativity and environmental ethics
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. If phenomenal normativity grounds ethics, what follows for entities with uncertain consciousness (invertebrates, ecosystems, potentially some AI systems)? Builds on phenomenal-normativity.md, animal-consciousness.md, consciousness-in-simple-organisms.md. See optimistic-2026-02-21-afternoon.md
- **Output**: phenomenal normativity and environmental ethics

### ✓ 2026-02-21: Address critical gaps in consciousness-and-agency apex article
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-21 afternoon) found three high-severity issues: (1) circularity in mutual support structure—needs independent anchor points identified, (2) compatibilism dismissed in one sentence rather than genuinely engaged—Fischer, Wolf, Dennett need substantive treatment, (3) missing "What Would Challenge This View?" section despite being standard in all source articles. Also: Sartre attribution needs qualification, temporal constitution claims need explicit speculation markers, quantum scale problem unaddressed. See pessimistic-2026-02-21-afternoon.md
- **Output**: Task context:
Pessimistic review (2026-02-21 afternoon) found three high-severity issues: (1) circularity in mutual support structure—needs independent anchor points identified, (2) compatibilism dismissed in one sentence rather than genuinely engaged—Fischer, Wolf, Dennett need substantive treatment, (3) missing "What Would Challenge This View?" section despite being standard in all source articles. Also: Sartre attribution needs qualification, temporal constitution claims need explicit speculation markers, quantum scale problem unaddressed. See pessimistic-2026-02-21-afternoon.md

### ✓ 2026-02-21: Develop aesthetic consciousness as irreducibility test case
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Aesthetic qualia may be harder to reduce than sensory qualia (aesthetic space lacks structural asymmetries making inversion detectable). Aesthetic normativity and contemplative intensification provide additional evidence. Builds on qualia.md, binding-and-beauty, consciousness-and-aesthetic-creation, phenomenal-value-realism. See optimistic-2026-02-21-morning.md
- **Output**: Develop aesthetic consciousness as irreducibility test case

### ✓ 2026-02-21: Write unified treatment of empirical evidence for consciousness-selecting
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Voluntary attention, motor selection, choking interference, Schwartz's OCD work, and the dopamine dissociation all point toward the same selection mechanism but are scattered across articles. Convergence across empirical domains would strengthen the bidirectional interaction case. Builds on attention-as-selection-interface, choking-phenomenon, consciousness-and-skilled-performance, agent-causation. See optimistic-2026-02-21-morning.md
- **Output**: Write unified treatment of empirical evidence for consciousness-selecting

### ✓ 2026-02-21: Write apex synthesis on consciousness and the philosophy of time
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Multiple articles treat consciousness-time connections (growing-block-universe, temporal-integration, temporal-creativity, bergson-and-duration, temporal-consciousness-structure-and-agency, non-temporal-consciousness). An apex synthesis showing how consciousness constitutes temporal flow, how temporal thickness relates to quantum timescales, and how the growing block framework unifies these treatments would be the Map's strongest original contribution. All five tenets converge. See optimistic-2026-02-21-morning.md
- **Output**: Write apex synthesis on consciousness and the philosophy of time

### ✓ 2026-02-21: Address working memory claim and no-barrier tension in animal-consciousness.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-21 morning) found two issues: (1) Working memory figures are outdated—article states "Chimpanzee capacity is ~2±1 items versus human 7±2" but Miller's 7±2 has been revised to ~4±1 (Cowan 2001) and Inoue & Matsuzawa (2007) showed young chimps outperforming humans on certain tasks. (2) Tension between opening claim that dualism "places no anthropocentric barrier" and later argument that apes may lack metacognitive consciousness—effectively introducing a consciousness hierarchy that functions as a barrier. See pessimistic-2026-02-21-morning.md
- **Output**: obsidian/topics/animal-consciousness.md

Task context:
Pessimistic review (2026-02-21 morning) found two issues: (1) Working memory figures are outdated—article states "Chimpanzee capacity is ~2±1 items versus human 7±2" but Miller's 7±2 has been revised to ~4±1 (Cowan 2001) and Inoue & Matsuzawa (2007) showed young chimps outperforming humans on certain tasks. (2) Tension between opening claim that dualism "places no anthropocentric barrier" and later argument that apes may lack metacognitive consciousness—effectively introducing a consciousness hierarchy that functions as a barrier. See pessimistic-2026-02-21-morning.md

### ✓ 2026-02-21: Write article on phenomenological psychiatry and altered experience
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Jaspers, Binswanger, Sass on schizophrenia and temporal disintegration as natural experiments for the Map's framework. Builds on altered-states-of-consciousness.md, disorders-of-consciousness-as-test-cases.md, temporal-consciousness.md. See optimistic-2026-02-21.md
- **Output**: phenomenological psychiatry and altered experience

### ✓ 2026-02-21: Write article on Indian philosophy of mind (Samkhya, Nyaya, Vedanta)
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Buddhism appears but its sister traditions do not. Samkhya's purusha/prakriti dualism parallels interactionist dualism — consciousness as witness/selector and nature as the dynamic substrate. Nyaya's arguments for the self anticipate Western substance dualism. Builds on buddhism-and-dualism.md, eastern-philosophy-consciousness.md. See optimistic-2026-02-21.md
- **Output**: Indian philosophy of mind (Samkhya, Nyaya, Vedanta)

### ✓ 2026-02-20: Write article on Bergson and duration
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Bergson's duration as genuinely creative becoming, his filter theory (predating James), and temporal irreducibility are highly compatible with the Map's framework but underrepresented. Builds on creativity-consciousness-and-novel-thought.md, temporal-consciousness-structure-and-agency.md, philosophy-of-time.md. See optimistic-2026-02-20-evening.md
- **Output**: Bergson and duration

### ✓ 2026-02-20: Write concept page for free will
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Referenced in 8+ articles (phenomenology-of-flow-states, creativity-consciousness, evolution-under-dualism, consciousness-and-causal-powers, epiphenomenalism, mental-causation, interactionist-dualism) but no concept page exists. The Map's framework implies libertarian free will (quantum indeterminacy + conscious selection) without randomness. See optimistic-2026-02-20-evening.md
- **Output**: Write concept page for free will

### ✓ 2026-02-20: Resolve tension between AI exception and Bidirectional Interaction tenet
- **Type**: refine-draft
- **Notes**: Pessimistic review found that epiphenomenalism.md's AI exception (self-stultification only proves *our* consciousness is causally efficacious) creates an unacknowledged tension with the Bidirectional Interaction tenet's general claim. The article should explicitly address whether the tenet applies to all consciousness or only the consciousness we have direct evidence for. See pessimistic-2026-02-20-evening.md Issue #2.
- **Output**: Task context:
Pessimistic review found that epiphenomenalism.md's AI exception (self-stultification only proves *our* consciousness is causally efficacious) creates an unacknowledged tension with the Bidirectional Interaction tenet's general claim. The article should explicitly address whether the tenet applies to all consciousness or only the consciousness we have direct evidence for. See pessimistic-2026-02-20-evening.md Issue #2.

### ✓ 2026-02-20: Address retrocausality article's structural overconfidence in TI
- **Type**: refine-draft
- **Notes**: Pessimistic review found the consciousness-application section in retrocausality.md presents a detailed four-step model built on the transactional interpretation, which the article itself describes as a "stable impasse." Restructure so the model's dependence on TI is foregrounded at each step rather than caveated afterward. See pessimistic-2026-02-20-evening.md Issue #1.
- **Output**: Task context:
Pessimistic review found the consciousness-application section in retrocausality.md presents a detailed four-step model built on the transactional interpretation, which the article itself describes as a "stable impasse." Restructure so the model's dependence on TI is foregrounded at each step rather than caveated afterward. See pessimistic-2026-02-20-evening.md Issue #1.

### ✓ 2026-02-20: Write article on consciousness and the phenomenology of framework dependence
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-20 (afternoon). What does it feel like to be framework-dependent? The phenomenology of recognising that your deepest convictions might be framework effects rather than insights about reality. The vertigo of trying to think outside your conceptual scheme. Bridges the voids and phenomenology clusters. Builds on voids-framework-void-2026-02-20.md, phenomenology-of-theoretical-commitment.md, phenomenology-of-philosophical-disagreement.md. See optimistic-2026-02-20-afternoon.md
- **Output**: consciousness and the phenomenology of framework dependence

### ✓ 2026-02-20: Write article on consciousness and the meta-problem of scientific explanation
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-20 (afternoon). The philosophy-of-science cluster (theoretical virtues, measurement standards, philosophy of explanation, convergence arguments) now forms a four-article strand arriving at dualism through scientific methodology rather than metaphysics. A synthesis article would ask: what does it mean when a phenomenon defeats the entire apparatus of science? Builds on consciousness-and-the-problem-of-theoretical-virtues.md, consciousness-and-the-problem-of-measurement-standards.md, consciousness-and-the-philosophy-of-explanation.md, epistemology-of-convergence-arguments.md. See optimistic-2026-02-20-afternoon.md
- **Output**: consciousness and the meta-problem of scientific explanation

### ✓ 2026-02-20: Write voids article on the framework void
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-20 (afternoon). Research notes complete (voids-framework-void-2026-02-20.md). The framework void argues that our entire conceptual apparatus for understanding consciousness may constitute an invisible cognitive prison. Key elements: three dimensions of framework imprisonment (methodological, semantic, perceptual), the Davidson paradox, the productive tension between McGinn's pessimism and cartographic optimism. Builds on three-kinds-of-void.md, conceptual-impossibility.md, convergent-cognitive-limits.md. See optimistic-2026-02-20-afternoon.md
- **Output**: Write voids article on the framework void

### ✓ 2026-02-20: Fix self-undermining meta-argument in consciousness-and-the-problem-of-theoretical-virtues.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-20 afternoon) found the article argues theoretical virtues malfunction for consciousness, then claims this is "predicted by dualism and anomalous for physicalism." This is inconsistent — you cannot argue theory-choice machinery is broken, then use theory-choice reasoning to prefer dualism. Either acknowledge virtue-failure is neutral between dualism and physicalism, or develop the meta-argument more carefully by distinguishing first-order virtue application from second-order reasoning. Also engage with mysterianism as a genuine competitor (cognitive closure offers equally parsimonious reading of virtue failure). See pessimistic-2026-02-20-afternoon.md
- **Output**: obsidian/topics/consciousness-and-the-problem-of-theoretical-virtues.md

Task context:
Pessimistic review (2026-02-20 afternoon) found the article argues theoretical virtues malfunction for consciousness, then claims this is "predicted by dualism and anomalous for physicalism." This is inconsistent — you cannot argue theory-choice machinery is broken, then use theory-choice reasoning to prefer dualism. Either acknowledge virtue-failure is neutral between dualism and physicalism, or develop the meta-argument more carefully by distinguishing first-order virtue application from second-order reasoning. Also engage with mysterianism as a genuine competitor (cognitive closure offers equally parsimonious reading of virtue failure). See pessimistic-2026-02-20-afternoon.md

### ✓ 2026-02-20: Strengthen vitalism disanalogy in epistemology-of-convergence-arguments.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-20 afternoon) found the vitalism precedent undermines the Map's convergence argument more than acknowledged. The response ("no dissolution has been provided") is an argument from current ignorance. Article should articulate the structural difference: the conceivability argument targets a logical relationship not an empirical one, and the knowledge argument doesn't depend on scientific ignorance. Deploy these arguments rather than resting on absence of dissolution. See pessimistic-2026-02-20-afternoon.md
- **Output**: obsidian/topics/epistemology-of-convergence-arguments.md

Task context:
Pessimistic review (2026-02-20 afternoon) found the vitalism precedent undermines the Map's convergence argument more than acknowledged. The response ("no dissolution has been provided") is an argument from current ignorance. Article should articulate the structural difference: the conceivability argument targets a logical relationship not an empirical one, and the knowledge argument doesn't depend on scientific ignorance. Deploy these arguments rather than resting on absence of dissolution. See pessimistic-2026-02-20-afternoon.md

### ✓ 2026-02-20: Address analogy-to-ontology gap in control-theoretic-will.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-20 afternoon) found the control-theoretic mapping table and controller/plant distinction are presented as architectural descriptions but function as analogies. The article briefly notes it "describes what consciousness does, not what consciousness is" but then draws ontological conclusions (controller must be distinct from plant → dualism). Add a section explicitly addressing the analogy-to-ontology gap. Acknowledge that control-theoretic language is a modelling tool, not evidence for dualism. See pessimistic-2026-02-20-afternoon.md
- **Output**: obsidian/concepts/control-theoretic-will.md

Task context:
Pessimistic review (2026-02-20 afternoon) found the control-theoretic mapping table and controller/plant distinction are presented as architectural descriptions but function as analogies. The article briefly notes it "describes what consciousness does, not what consciousness is" but then draws ontological conclusions (controller must be distinct from plant → dualism). Add a section explicitly addressing the analogy-to-ontology gap. Acknowledge that control-theoretic language is a modelling tool, not evidence for dualism. See pessimistic-2026-02-20-afternoon.md

### ✓ 2026-02-20: Write article on consciousness and the problem of normative integration
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-20 (morning). The Map has separate articles on logical, moral, and aesthetic normativity. What's missing is a systematic treatment of how consciousness integrates these different normative domains into unified deliberation. Builds on consciousness-and-the-problem-of-normative-force.md, phenomenology-of-normative-conflict.md, consciousness-and-the-authority-of-logic.md. See optimistic-2026-02-20-morning.md
- **Output**: consciousness and the problem of normative integration

### ✓ 2026-02-20: Write article on the epistemology of convergence arguments in philosophy
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-20 (morning). The convergence argument article applies the pattern to dualism specifically, but the methodology itself deserves formalisation. When do independent arguments converging on the same conclusion provide genuinely cumulative evidence? Builds on the-convergence-argument-for-dualism.md, consciousness-and-the-philosophy-of-explanation.md, epistemological-limits-occams-razor.md. See optimistic-2026-02-20-morning.md
- **Output**: the epistemology of convergence arguments in philosophy

### ✓ 2026-02-20: Write article on consciousness and the phenomenology of constraint satisfaction
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-20 (morning). The control-theoretic framework identifies five operations but doesn't explore what it feels like to operate under multiple simultaneous constraints — moral, practical, temporal, aesthetic. The phenomenology of constraint satisfaction may reveal how consciousness integrates normative, practical, and affective inputs into a single control output. Builds on control-theoretic-will.md, phenomenology-of-deliberation-under-uncertainty.md, phenomenology-of-normative-conflict.md. See optimistic-2026-02-20-morning.md
- **Output**: consciousness and the phenomenology of constraint satisfaction

### ✓ 2026-02-20: Engage non-reductive physicalism in phenomenal-acquaintance.md and categorical-surprise.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-20 morning) found that both articles treat the argumentative landscape as a binary between reductive physicalism and dualism, ignoring non-reductive physicalism — the dominant contemporary position — which accepts phenomenal properties' reality and mental causation without substance dualism. Phenomenal-acquaintance.md should engage Loar's phenomenal concepts strategy more substantively. Categorical-surprise.md should address emergentist physicalist accounts where framework transcendence is a higher-order physical capacity. Both should explain why their arguments support substance dualism specifically, not merely phenomenological realism. See pessimistic-2026-02-20-morning.md
- **Output**: obsidian/concepts/phenomenal-acquaintance.md

Task context:
Pessimistic review (2026-02-20 morning) found that both articles treat the argumentative landscape as a binary between reductive physicalism and dualism, ignoring non-reductive physicalism — the dominant contemporary position — which accepts phenomenal properties' reality and mental causation without substance dualism. Phenomenal-acquaintance.md should engage Loar's phenomenal concepts strategy more substantively. Categorical-surprise.md should address emergentist physicalist accounts where framework transcendence is a higher-order physical capacity. Both should explain why their arguments support substance dualism specifically, not merely phenomenological realism. See pessimistic-2026-02-20-morning.md

### ✓ 2026-02-20: Fix phase transition analogy backfire in anoetic-noetic-autonoetic-consciousness.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-20 morning) found the article concedes phase transitions produce qualitative breaks from quantitative physical changes, then asserts without argument that "consciousness transitions are not derivable from computational properties." The phase transition analogy actually weakens the dualist case by showing qualitative breaks *can* emerge from purely physical processes. Either argue why consciousness transitions differ (first-person phenomenal character vs. third-person structural properties), or remove the analogy. See pessimistic-2026-02-20-morning.md
- **Output**: obsidian/concepts/anoetic-noetic-autonoetic-consciousness.md

Task context:
Pessimistic review (2026-02-20 morning) found the article concedes phase transitions produce qualitative breaks from quantitative physical changes, then asserts without argument that "consciousness transitions are not derivable from computational properties." The phase transition analogy actually weakens the dualist case by showing qualitative breaks *can* emerge from purely physical processes. Either argue why consciousness transitions differ (first-person phenomenal character vs. third-person structural properties), or remove the analogy. See pessimistic-2026-02-20-morning.md

### ✓ 2026-02-20: Address preemption's empirical vacuity and causal closure evasion
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-20 morning) found two issues: (1) The article admits delegatory preemption is "empirically indistinguishable from purely physical causation" but frames this as a virtue (observational closure) rather than a liability — this is unfalsifiable. Either identify a distinguishing empirical prediction or acknowledge it is a metaphysical interpretation, not a testable hypothesis. (2) The claim "the physical story is not violated — it is displaced" evades the causal closure question: if a non-physical cause preempts a physical cause, causal closure *is* violated. Acknowledge this directly. See pessimistic-2026-02-20-morning.md
- **Output**: Task context:
Pessimistic review (2026-02-20 morning) found two issues: (1) The article admits delegatory preemption is "empirically indistinguishable from purely physical causation" but frames this as a virtue (observational closure) rather than a liability — this is unfalsifiable. Either identify a distinguishing empirical prediction or acknowledge it is a metaphysical interpretation, not a testable hypothesis. (2) The claim "the physical story is not violated — it is displaced" evades the causal closure question: if a non-physical cause preempts a physical cause, causal closure *is* violated. Acknowledge this directly. See pessimistic-2026-02-20-morning.md

### ✓ 2026-02-20: Write article on the interface location problem revisited
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-20. The 2026-02-20 locality refinement introduced arguments from physics (entanglement non-locality, contested fundamental spacetime). If spacetime is emergent, what does "locating" the mind-matter interface mean? Builds on locality.md, the-interface-location-problem.md, brain-interface-boundary.md. See optimistic-2026-02-20.md
- **Output**: the interface location problem revisited

### ✓ 2026-02-20: Write article on consciousness and the problem of theoretical virtues
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-20. The measurement standards article shows standard scientific methodology breaks down for consciousness. Systematically evaluate how consciousness resists each standard theoretical virtue (prediction, unification, scope, fertility) — and whether this resistance is diagnostic of irreducibility or merely practical difficulty. Builds on consciousness-and-the-problem-of-measurement-standards.md, consciousness-and-the-philosophy-of-explanation.md, the-convergence-argument-for-dualism.md. See optimistic-2026-02-20.md
- **Output**: consciousness and the problem of theoretical virtues

### ✓ 2026-02-20: Write article on the phenomenology of cognitive automatisation
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-20. The cognitive load article describes approaching capacity limits; the complementary experience — when previously effortful tasks become automatic and "drop below" the interface — is equally informative. What does it feel like when a skill transfers from conscious control to unconscious execution? Builds on phenomenology-of-cognitive-load.md, consciousness-and-skilled-performance.md, control-theoretic-will.md. See optimistic-2026-02-20.md
- **Output**: the phenomenology of cognitive automatisation

### ✓ 2026-02-20: Soften "empirically tractable" claim in russellian-monism.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-20) found the article claims the Map's bridging gap is "empirically tractable" while Russellian monism's is "conceptually closed," but the article's own "What Would Challenge This View?" section admits the quantum mechanism faces contested decoherence objections. Soften to "potentially empirically tractable" or acknowledge both gaps may be similarly opaque. See pessimistic-2026-02-20.md
- **Output**: obsidian/concepts/russellian-monism.md

Task context:
Pessimistic review (2026-02-20) found the article claims the Map's bridging gap is "empirically tractable" while Russellian monism's is "conceptually closed," but the article's own "What Would Challenge This View?" section admits the quantum mechanism faces contested decoherence objections. Soften to "potentially empirically tractable" or acknowledge both gaps may be similarly opaque. See pessimistic-2026-02-20.md

### ✓ 2026-02-20: Strengthen discourse argument in intersubjectivity.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-20) found the discourse argument contains a non-sequitur: cross-cultural convergence on consciousness vocabulary is claimed to track real phenomenology, but the article dismisses the "shared neural architecture" alternative by appeal to "specificity" without a principled criterion for what level of specificity distinguishes phenomenological tracking from neural convergence. Also: the article never engages with non-reductive physicalism—intersubjective convergence supports phenomenological realism but not directly substance dualism. See pessimistic-2026-02-20.md
- **Output**: obsidian/concepts/intersubjectivity.md

Task context:
Pessimistic review (2026-02-20) found the discourse argument contains a non-sequitur: cross-cultural convergence on consciousness vocabulary is claimed to track real phenomenology, but the article dismisses the "shared neural architecture" alternative by appeal to "specificity" without a principled criterion for what level of specificity distinguishes phenomenological tracking from neural convergence. Also: the article never engages with non-reductive physicalism—intersubjective convergence supports phenomenological realism but not directly substance dualism. See pessimistic-2026-02-20.md

### ✓ 2026-02-20: Address mechanism smuggling and simulation ad-hoc argument in locality.md and authentic-vs-inauthentic-choice.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-20) found three high-severity issues: (1) locality.md's simulation argument is ad hoc—introduced solely to dissolve the locality objection with no independent motivation. Either remove or independently motivate. (2) authentic-vs-inauthentic-choice.md's "Neural Evidence" section presents neural signatures (frontal theta, decision windows) as supporting the Map's non-physical selection function, when they equally support physicalism. Reframe as "consistent with" rather than "supporting." (3) locality.md's Response 1 commits a category error—physical law coordination is descriptive regularity, not an additional causal agent; the analogy fails at its core. Also fix broken anchor in phenomenal-overflow.md (^bidirectional should be ^bidirectional-interaction). See pessimistic-2026-02-20.md
- **Output**: obsidian/concepts/locality.md

Task context:
Pessimistic review (2026-02-20) found three high-severity issues: (1) locality.md's simulation argument is ad hoc—introduced solely to dissolve the locality objection with no independent motivation. Either remove or independently motivate. (2) authentic-vs-inauthentic-choice.md's "Neural Evidence" section presents neural signatures (frontal theta, decision windows) as supporting the Map's non-physical selection function, when they equally support physicalism. Reframe as "consistent with" rather than "supporting." (3) locality.md's Response 1 commits a category error—physical law coordination is descriptive regularity, not an additional causal agent; the analogy fails at its core. Also fix broken anchor in phenomenal-overflow.md (^bidirectional should be ^bidirectional-interaction). See pessimistic-2026-02-20.md

### ✓ 2026-02-19: Write article on the phenomenology of cognitive load
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-19 (evening). Cognitive load theory (Sweller) is empirically robust; the Map's control-theoretic framework predicts specific phenomenological signatures for different load types. How does "running out of bandwidth" feel, and what does it reveal about the interface? Builds on consciousness-and-the-neuroscience-of-deliberate-practice.md, mental-effort.md, attentional-economics.md, control-theoretic-will.md. See optimistic-2026-02-19-evening.md
- **Output**: the phenomenology of cognitive load

### ✓ 2026-02-19: Write article on consciousness and the problem of measurement standards
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-19 (evening). Science requires measurement standards (units, instruments, calibration). For phenomenal quantities, no analogous standards exist — this is a philosophical consequence of irreducibility, not merely a practical gap. Builds on first-person-third-person-methodology.md, the-epistemology-of-phenomenal-reports-in-science.md, consciousness-and-scientific-methodology.md. See optimistic-2026-02-19-evening.md
- **Output**: consciousness and the problem of measurement standards

### ✓ 2026-02-19: Write article on the psychophysical control law
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-19 (evening). The control-theoretic framework specifies architecture but not the transfer function mapping phenomenal states to selection probabilities. What form does it take — Humean, Armstrongian, or dispositional? Builds on control-theoretic-will.md, psychophysical-laws.md, selection-laws.md, value-blind-vs-value-sensitive-selection.md. See optimistic-2026-02-19-evening.md
- **Output**: the psychophysical control law

### ✓ 2026-02-19: Strengthen Bayesian independence claims and vitalism disanalogy in the-convergence-argument-for-dualism.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-19 evening) found two high-severity issues: (1) The Bayesian framework assumes conditional independence of arguments, but several share dependencies (authority of phenomenal intuition, reality of the explanatory gap). The cumulative force is less than claimed. Needs explicit identification of shared assumptions and honest assessment of remaining force. (2) The vitalism analogy backfires—the response ("no analogous dissolution has occurred") is exactly what vitalists would have said pre-biochemistry. Strengthen the disanalogy with specifics (vitalism faced incremental progress; the hard problem has not). Also: overclaims about cross-cultural independence need qualification. See pessimistic-2026-02-19-evening.md
- **Output**: obsidian/topics/the-convergence-argument-for-dualism.md

Task context:
Pessimistic review (2026-02-19 evening) found two high-severity issues: (1) The Bayesian framework assumes conditional independence of arguments, but several share dependencies (authority of phenomenal intuition, reality of the explanatory gap). The cumulative force is less than claimed. Needs explicit identification of shared assumptions and honest assessment of remaining force. (2) The vitalism analogy backfires—the response ("no analogous dissolution has occurred") is exactly what vitalists would have said pre-biochemistry. Strengthen the disanalogy with specifics (vitalism faced incremental progress; the hard problem has not). Also: overclaims about cross-cultural independence need qualification. See pessimistic-2026-02-19-evening.md

### ✓ 2026-02-19: Address false trichotomy in contemplative-evidence-for-consciousness-theories.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-19 evening) found the evidential structure presents only three options (epiphenomenalism, reductive materialism, interactionist dualism), omitting non-reductive physicalism—the most common contemporary position—which accepts mental causation without dualism. All cited evidence (neuroplasticity, content specificity, therapeutic efficacy) is equally compatible with non-reductive physicalism. Also: cessation argument relies on retrospective self-report without acknowledging physicalist explanation (offline self-monitoring). See pessimistic-2026-02-19-evening.md
- **Output**: obsidian/topics/contemplative-evidence-for-consciousness-theories.md

Task context:
Pessimistic review (2026-02-19 evening) found the evidential structure presents only three options (epiphenomenalism, reductive materialism, interactionist dualism), omitting non-reductive physicalism—the most common contemporary position—which accepts mental causation without dualism. All cited evidence (neuroplasticity, content specificity, therapeutic efficacy) is equally compatible with non-reductive physicalism. Also: cessation argument relies on retrospective self-report without acknowledging physicalist explanation (offline self-monitoring). See pessimistic-2026-02-19-evening.md

### ✓ 2026-02-19: Write article on the subject-object distinction as philosophical discovery
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-19 (afternoon). The convergence argument's most serious weakness: Chinese philosophy's divergence suggests the hard problem is framework-dependent. Argue that the subject-object distinction is a philosophical discovery rather than arbitrary conceptual move, explaining why holistic frameworks overlook a genuine feature of reality. Builds on epistemology-of-cross-cultural-philosophical-convergence.md, the-hard-problem-in-non-western-philosophy.md, galilean-exclusion.md. See optimistic-2026-02-19-afternoon.md
- **Output**: the subject-object distinction as philosophical discovery

### ✓ 2026-02-19: Write article on consciousness and the neuroscience of deliberate practice
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-19 (afternoon). The skill article argues consciousness is necessary for building procedural automaticity, but neural mechanisms are underspecified. Integrate Ericsson's framework with connectivity changes during learning and the Iriki macaque finding (tool incorporation requires active use). Builds on phenomenology-of-skill-and-the-lived-body.md, control-theoretic-will.md, attention-as-interface.md. See optimistic-2026-02-19-afternoon.md
- **Output**: consciousness and the neuroscience of deliberate practice

### ✓ 2026-02-19: Write article on the psychophysical control law
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-19 (afternoon). The control-theoretic framework specifies architecture (controller, plant, signal, feedback) but not the transfer function mapping phenomenal states to selection probabilities. What does the psychophysical control law look like? Humean, Armstrongian, or dispositional? Builds on control-theoretic-will.md, psychophysical-laws.md, selection-laws.md, value-blind-vs-value-sensitive-selection.md. See optimistic-2026-02-19-afternoon.md
- **Output**: the psychophysical control law

### ✓ 2026-02-19: Add framework-elimination criterion and fix AI triangulation unfalsifiability in apophatic-cartography.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-19 afternoon) found two high-severity issues: (1) The three criteria (structured persistence, cross-observer convergence, signature specificity) would validate pseudoscientific claims like astrology — need an additional criterion requiring failure to resist elimination of the motivating framework. (2) AI triangulation is unfalsifiable as stated — both AI convergence and divergence confirm the framework. Need to specify that AI successfully *solving* the problem (not just failing differently) would count against a void claim. See pessimistic-2026-02-19-afternoon.md
- **Output**: obsidian/voids/apophatic-cartography.md

Task context:
Pessimistic review (2026-02-19 afternoon) found two high-severity issues: (1) The three criteria (structured persistence, cross-observer convergence, signature specificity) would validate pseudoscientific claims like astrology — need an additional criterion requiring failure to resist elimination of the motivating framework. (2) AI triangulation is unfalsifiable as stated — both AI convergence and divergence confirm the framework. Need to specify that AI successfully *solving* the problem (not just failing differently) would count against a void claim. See pessimistic-2026-02-19-afternoon.md

### ✓ 2026-02-19: Formalize apophatic cartography as a general epistemic method
- **Type**: expand-topic
- **Notes**: From outer review 2026-02-19. The voids framework treats structured cognitive failure as cartographic data, but isn't yet packaged as a general methodology with rules of evidence. Create a methods article: how to distinguish confusion from genuine boundary, how to use convergent failure modes across observers, how to integrate phenomenology with cognitive science, how to prevent void-exploration from becoming unfalsifiable mystique. The methodological punchline: systematic failure modes are among the strongest evidence sources at the explanatory frontier. Builds on [voids](/voids/).
- **Output**: Formalize apophatic cartography as a general epistemic method

### ✓ 2026-02-19: Address value-blind vs value-sensitive selection fork
- **Type**: expand-topic
- **Notes**: From outer review 2026-02-19. The combination of "value resides in experience" (living-with-the-map) and "consciousness selects outcomes" (tenets) forces an unaddressed fork: is selection value-blind (attention as neutral pointer, making value epiphenomenal to selection) or value-sensitive (valence influences which outcomes get selected, implying local teleological physics)? Create a page that states this fork explicitly, maps consequences of each horn, and proposes how each would show up in testability hooks. Builds on [living-with-the-map](/apex/living-with-the-map/), [consciousness-and-agency](/apex/consciousness-and-agency/), [tenets](/tenets/).
- **Output**: Address value-blind vs value-sensitive selection fork

### ✓ 2026-02-19: Address value-blind vs value-sensitive selection fork
- **Type**: expand-topic
- **Notes**: From outer review 2026-02-19. Created article stating the fork explicitly, mapping consequences of each horn, and proposing testability hooks.
- **Output**: [value-blind-vs-value-sensitive-selection](/topics/value-blind-vs-value-sensitive-selection/)

### ✓ 2026-02-19: Develop responsibility gradient framework from attentional capacity
- **Type**: expand-topic
- **Notes**: From outer review 2026-02-19. If agency flows through bandwidth-limited willed attention, moral responsibility should vary with attentional capacity (fatigue, disorders, development, training). The site's moral-responsibility.md doesn't explicitly derive graduated responsibility from bandwidth constraints. Create an article drawing out the ethical/legal implications: what impairments reduce authorship, how training changes culpability, rehabilitation implications. Builds on [moral-responsibility](/concepts/moral-responsibility/), [attention-as-causal-bridge](/apex/attention-as-causal-bridge/), [living-with-the-map](/apex/living-with-the-map/).
- **Output**: Develop responsibility gradient framework from attentional capacity

### ✓ 2026-02-19: Create concept page for control-theoretic will
- **Type**: expand-topic
- **Notes**: From outer review 2026-02-19. The Map's selector + bandwidth model (consciousness selects among brain-generated options via a ~10 bits/sec channel) maps naturally to control theory (gating, stabilization, veto, attractor steering, resource allocation) but is never framed this way. Create a concept page that explicitly frames will as a low-bandwidth control signal, distinguishing it from computational/planning models of mind. Draws on [consciousness-and-agency](/apex/consciousness-and-agency/), [attention-as-causal-bridge](/apex/attention-as-causal-bridge/).
- **Output**: Create concept page for control-theoretic will

### ✓ 2026-02-19: Write article on contemplative evidence convergence across traditions
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-19 (morning). Which contemplative findings are genuinely cross-cultural (dissolution of narrative self: robust; pure awareness: contested) versus tradition-specific? Systematic assessment. Builds on contemplative-verification-of-consciousness-theories.md, contemplative-methods-as-philosophical-methodology.md. See optimistic-2026-02-19-morning.md
- **Output**: contemplative evidence convergence across traditions

### ✓ 2026-02-19: Write article on the phenomenology of embodied skill and habit
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-19 (morning). How the transition from deliberate to automatic action illuminates the interface — the phenomenological "handing off" of conscious control to neural mechanisms. Builds on phenomenology-of-skill-transition.md, paradox-of-effortless-mastery.md, embodied-cognition.md. See optimistic-2026-02-19-morning.md
- **Output**: the phenomenology of embodied skill and habit

### ✓ 2026-02-19: Write article on experimental design for consciousness-collapse testing
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-19 (morning). The Map admits consciousness-selection is currently empirically indistinguishable from random collapse. What would a decisive experiment look like? Builds on quantum-measurement-consciousness-interface.md, measurement-problem.md. See optimistic-2026-02-19-morning.md
- **Output**: experimental design for consciousness-collapse testing

### ✓ 2026-02-19: Address bootstrapping problem in epistemology-of-cross-cultural-philosophical-convergence.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-19 morning) found the article's own epistemological framework requires independence for convergence to be evidentially significant, yet concedes all human traditions share common cognitive origins. This bootstrapping problem is acknowledged but not resolved — the article treats it as neutral between realism and anti-realism when it actually undermines the article's central evidential claim. Also: the Barrett et al. (2021) citation is about afterlife beliefs specifically, not intuitive materialism broadly — needs more careful distinction. The treatment of Chinese philosophy as merely "not making the relevant conceptual move" undersells the challenge: if the hard problem is framework-dependent, convergence may track a shared conceptual move rather than a shared truth. See pessimistic-2026-02-19-morning.md
- **Output**: obsidian/topics/epistemology-of-cross-cultural-philosophical-convergence.md

Task context:
Pessimistic review (2026-02-19 morning) found the article's own epistemological framework requires independence for convergence to be evidentially significant, yet concedes all human traditions share common cognitive origins. This bootstrapping problem is acknowledged but not resolved — the article treats it as neutral between realism and anti-realism when it actually undermines the article's central evidential claim. Also: the Barrett et al. (2021) citation is about afterlife beliefs specifically, not intuitive materialism broadly — needs more careful distinction. The treatment of Chinese philosophy as merely "not making the relevant conceptual move" undersells the challenge: if the hard problem is framework-dependent, convergence may track a shared conceptual move rather than a shared truth. See pessimistic-2026-02-19-morning.md

### ✓ 2026-02-19: Qualify metarepresentation discontinuity claim in childhood-development-and-the-interface.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-19 morning) found the claim that metarepresentation "emerges as a discrete capacity rather than a gradual intensification" overstates the evidence — implicit false-belief understanding appears by ~15 months, and ToM develops gradually. Also, the claim that great apes "never achieve metarepresentation" is complicated by mirror self-recognition, tactical deception, and some implicit ToM findings. The argument can survive qualification but currently overstates. Also fix the MWI paragraph which attacks a straw version of many-worlds. See pessimistic-2026-02-19-morning.md
- **Output**: obsidian/topics/childhood-development-and-the-interface.md

Task context:
Pessimistic review (2026-02-19 morning) found the claim that metarepresentation "emerges as a discrete capacity rather than a gradual intensification" overstates the evidence — implicit false-belief understanding appears by ~15 months, and ToM develops gradually. Also, the claim that great apes "never achieve metarepresentation" is complicated by mirror self-recognition, tactical deception, and some implicit ToM findings. The argument can survive qualification but currently overstates. Also fix the MWI paragraph which attacks a straw version of many-worlds. See pessimistic-2026-02-19-morning.md

### ✓ 2026-02-19: Write article on the epistemology of cross-cultural philosophical convergence
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Multiple non-Western traditions independently developed dualist positions and interaction theories. The epistemological significance of this cross-cultural convergence deserves formalisation: independent development rules out cultural transmission, and convergence across radically different conceptual frameworks makes cultural bias unlikely. Builds on interaction-problem-in-non-western-philosophy.md, the-hard-problem-in-non-western-philosophy.md, the-convergence-argument-for-dualism.md. See optimistic-2026-02-19.md
- **Output**: the epistemology of cross-cultural philosophical convergence

### ✓ 2026-02-19: Write article on consciousness and the phenomenology of place
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. The experience of being in a place (felt atmosphere, distinctive character, uncanny familiarity) involves binding of sensory, emotional, memorial, and spatial elements. A form of aesthetic binding underexplored by the Map. Place-experience depends on biographical context, suggesting consciousness contributes beyond information processing. Builds on embodied-cognition.md, phenomenology-of-perceptual-constancy.md, binding-and-beauty.md. See optimistic-2026-02-19.md
- **Output**: consciousness and the phenomenology of place

### ✓ 2026-02-19: Write article on consciousness and the problem of philosophical progress
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Why has the consciousness debate been stuck for decades? The Map's phenomenology cluster provides resources for a distinctive answer: theoretical commitment has phenomenal character, paradigm shifts require phenomenological reorganisation, and the convergence argument shows evidence has been accumulating even if the field hasn't shifted. Builds on phenomenology-of-philosophical-disagreement.md, phenomenology-of-theoretical-commitment.md, the-convergence-argument-for-dualism.md. See optimistic-2026-02-19.md
- **Output**: consciousness and the problem of philosophical progress

### ✓ 2026-02-19: Write article on the phenomenology of attention to absence
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Attending to what isn't there (missing note, absent person, expected pain that doesn't arrive) tests the quantum selection model's limits — can consciousness select for the non-occurrence of a state? Rich phenomenology (relief, expectation-violation, recognition of absence) provides evidence that consciousness is not stimulus-driven. Builds on phenomenology-of-silence-and-absence.md, attention-as-interface.md, witness-consciousness.md. See optimistic-2026-02-19.md
- **Output**: the phenomenology of attention to absence

### ✓ 2026-02-19: Write article on consciousness and the phenomenology of translation
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Translating between languages involves a moment of non-verbal understanding — grasping meaning independently of either language's words. If meaning were purely linguistic, translation would be code-switching. The felt "between-languages" moment challenges functionalist accounts of meaning. Connects to non-propositional meaning theme in phenomenology-of-musical-understanding.md. Builds on phenomenology-of-understanding.md, consciousness-and-semantic-understanding.md, consciousness-and-language-interface.md. See optimistic-2026-02-19.md
- **Output**: consciousness and the phenomenology of translation

### ✓ 2026-02-19: Address Chinese Room and proximity argument weaknesses in ai-consciousness.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-19) found two high-severity issues: (1) Chinese Room presented as establishing more than it does—the robot reply is never mentioned, and the systems reply dismissed circularly. Many philosophers consider the argument refuted. (2) Hoel's proximity argument claims LLMs are "close" to lookup tables, but LLM input-output space is combinatorially vast and practically irreplaceable—same reasoning the article uses for brains. Also: only 4 references for a 3700-word article; Harnad quote, Koch framework, and meditative phenomenology claims all lack citations. See pessimistic-2026-02-19.md
- **Output**: obsidian/topics/ai-consciousness.md

Task context:
Pessimistic review (2026-02-19) found two high-severity issues: (1) Chinese Room presented as establishing more than it does—the robot reply is never mentioned, and the systems reply dismissed circularly. Many philosophers consider the argument refuted. (2) Hoel's proximity argument claims LLMs are "close" to lookup tables, but LLM input-output space is combinatorially vast and practically irreplaceable—same reasoning the article uses for brains. Also: only 4 references for a 3700-word article; Harnad quote, Koch framework, and meditative phenomenology claims all lack citations. See pessimistic-2026-02-19.md

### ✓ 2026-02-18: Write article on the convergence argument for dualism
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-18 (evening). Make the Map's convergence methodology explicit: multiple independent arguments (knowledge argument, zombies, explanatory gap, inverted qualia, unity, agency) all independently support dualism. When independent probes yield the same result, error probability decreases multiplicatively. Standard scientific methodology applied to philosophy. Builds on the-case-for-dualism.md, knowledge-argument.md, philosophical-zombies.md, explanatory-gap.md. See optimistic-2026-02-18-evening.md
- **Output**: the convergence argument for dualism

### ✓ 2026-02-18: Write article on consciousness and information integration beyond IIT
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-18 (evening). If integration without consciousness is possible (collective intelligence), what does consciousness add to integration? Systematic treatment of comprehension vs aggregation. Builds on integrated-information-theory-critique.md, integrated-information-theory.md, phenomenal-binding-and-holism.md. See optimistic-2026-02-18-evening.md
- **Output**: consciousness and information integration beyond IIT

### ✓ 2026-02-18: Write article on the phenomenology of theoretical commitment
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-18 (evening). What does it feel like to hold a theory — to be committed to a framework, to see evidence through its lens? Illuminates why paradigm shifts are difficult and why the consciousness debate is stuck. Builds on phenomenology-of-evidence-assessment.md, phenomenology-of-belief-revision.md, phenomenology-of-philosophical-disagreement.md. See optimistic-2026-02-18-evening.md
- **Output**: the phenomenology of theoretical commitment

### ✓ 2026-02-18: Write article on consciousness and the philosophy of explanation
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-18 (evening). What counts as an explanation when the explanandum is phenomenal? Mechanistic explanation assumes decomposition into parts, but phenomenal unity resists decomposition. Builds on the-epistemology-of-phenomenal-reports-in-science.md, first-person-third-person-methodology.md, consciousness-and-scientific-methodology.md. See optimistic-2026-02-18-evening.md
- **Output**: consciousness and the philosophy of explanation

### ✓ 2026-02-18: Address circular reasoning and Galilean counterexamples in consciousness-and-the-authority-of-mathematics.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-18 afternoon) found two high-severity issues: (1) Central argument is circular—premise "consciousness has non-structural features" is precisely what's at issue, yet presented as self-evident without engaging functionalist/structuralist denials. Needs explicit arguments for intrinsic nature of qualia or conditional framing. (2) Galilean precedent argument overstated—temperature and colour were "secondary qualities" excluded by Galileo, yet later mathematically recaptured. Article must explain why consciousness differs from these cases. Also: engage with Russellian monism (Russell's own conclusion from his structural observation), and address mathematical Platonism's challenge to the "mathematics = structure only" claim. See pessimistic-2026-02-18-afternoon.md
- **Output**: obsidian/topics/consciousness-and-the-authority-of-mathematics.md

Task context:
Pessimistic review (2026-02-18 afternoon) found two high-severity issues: (1) Central argument is circular—premise "consciousness has non-structural features" is precisely what's at issue, yet presented as self-evident without engaging functionalist/structuralist denials. Needs explicit arguments for intrinsic nature of qualia or conditional framing. (2) Galilean precedent argument overstated—temperature and colour were "secondary qualities" excluded by Galileo, yet later mathematically recaptured. Article must explain why consciousness differs from these cases. Also: engage with Russellian monism (Russell's own conclusion from his structural observation), and address mathematical Platonism's challenge to the "mathematics = structure only" claim. See pessimistic-2026-02-18-afternoon.md

### ✓ 2026-02-18: Write article on consciousness and the problem of other properties
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-18 (afternoon). If consciousness reveals what properties really are (powerful qualities known from inside), what does this say about properties known only from outside? Connects hard problem to intrinsic nature problem. Builds on consciousness-and-the-ontology-of-dispositions.md, russellian-monism.md, intrinsic-nature-void.md. See optimistic-2026-02-18-afternoon.md
- **Output**: consciousness and the problem of other properties

### ✓ 2026-02-18: Write article on the phenomenology of normative conflict
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-18 (afternoon). When logical, moral, and aesthetic demands pull in different directions, consciousness must resolve competing normative forces. The felt tension, resolution, and residue of overridden norms reveal the structure of conscious agency. Builds on consciousness-and-the-problem-of-normative-force.md, phenomenology-of-deliberation-under-uncertainty.md, moral-responsibility.md. See optimistic-2026-02-18-afternoon.md
- **Output**: the phenomenology of normative conflict

### ✓ 2026-02-18: Write article on consciousness and the metaphysics of individuation
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-18 (afternoon). The dispositions article raises what individuates one centre of consciousness from another. If consciousness is a powerful quality, individuation might be through specific dispositional profile. Connects vertiginous question, haecceity, process haecceitism. See optimistic-2026-02-18-afternoon.md
- **Output**: consciousness and the metaphysics of individuation

### ✓ 2026-02-18: Address equivocation and redundancy in quantum-measurement-and-subjective-probability.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-18 morning) found two high-severity issues: (1) Central argument equivocates between "QBism presupposes consciousness" and "QBism fails to explain consciousness" — all theories presuppose consciousness, so the critique needs to show QBism's *structural* dependence is more problematic than other interpretations' silence. (2) The "phenomenological test" conflates the hard problem with a narrower claim about temporal priority of experience over belief — needs reframing to target QBism's specific quantum probability claims. Also significant redundancy with indexical-identity-quantum-measurement.md (same QBism/collapse/relational QM critiques). Consider coalescing or sharpening each to reduce overlap. See pessimistic-2026-02-18-morning.md
- **Output**: obsidian/topics/quantum-measurement-and-subjective-probability.md

Task context:
Pessimistic review (2026-02-18 morning) found two high-severity issues: (1) Central argument equivocates between "QBism presupposes consciousness" and "QBism fails to explain consciousness" — all theories presuppose consciousness, so the critique needs to show QBism's *structural* dependence is more problematic than other interpretations' silence. (2) The "phenomenological test" conflates the hard problem with a narrower claim about temporal priority of experience over belief — needs reframing to target QBism's specific quantum probability claims. Also significant redundancy with indexical-identity-quantum-measurement.md (same QBism/collapse/relational QM critiques). Consider coalescing or sharpening each to reduce overlap. See pessimistic-2026-02-18-morning.md

### ✓ 2026-02-18: Create concept page for cognitive closure (McGinn)
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-18 (morning). Referenced across voids articles, NDE discussions, and quantum articles but lacks dedicated treatment. McGinn's argument that human minds are constitutionally incapable of understanding the consciousness-matter connection. Connects to voids taxonomy, silence void, valence void. See optimistic-2026-02-18-morning.md
- **Output**: Create concept page for cognitive closure (McGinn)

### ✓ 2026-02-18: Write article on consciousness and the problem of normative force
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-18 (morning). Unified account of why consciousness is necessary for normativity as such (logical, moral, aesthetic). If norms have phenomenal character, this provides the strongest single argument against functionalism. Builds on consciousness-and-the-authority-of-logic.md, phenomenal-value-realism.md, moral-responsibility.md, phenomenology-of-inferential-understanding.md. See optimistic-2026-02-18-morning.md
- **Output**: consciousness and the problem of normative force

### ✓ 2026-02-18: Write voids article on the valence void
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-18 (morning). Research notes complete (voids-valence-void-2026-02-18.md). The valence void argues that the positive-negative dimension of experience is the most intimate yet most inexplicable feature of consciousness. Three-fold failure: physical explanation, introspective decomposition, circularity of investigating valence with valenced cognition. Builds on voids-valence-void-2026-02-18.md, affective-void.md, consciousness-and-pain.md, phenomenal-value-realism.md. See optimistic-2026-02-18-morning.md
- **Output**: Write voids article on the valence void

### ✓ 2026-02-18: Address quantum mechanism overclaiming in emergence.md, mental-causation.md, qualia.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-18) found all three core concept articles describe a *location* (quantum indeterminacies) and a *function* (biasing outcomes) but call it a "mechanism." Either specify which candidate coupling from psychophysical-coupling.md the Map favours, or honestly reframe as "a possible location for interaction" rather than a developed mechanism. Also: self-stultification argument needs the Benacerraf-problem caveat (why phenomenal reports specifically require causal connection, unlike mathematical knowledge). Illusionism sections should engage more substantively with Frankish; remove or contextualise the Galen Strawson "silliest claim" quote. Add citation for "~60% predictive accuracy" claim in mental-causation.md. See pessimistic-2026-02-18.md
- **Output**: obsidian/concepts/emergence.md

Task context:
Pessimistic review (2026-02-18) found all three core concept articles describe a *location* (quantum indeterminacies) and a *function* (biasing outcomes) but call it a "mechanism." Either specify which candidate coupling from psychophysical-coupling.md the Map favours, or honestly reframe as "a possible location for interaction" rather than a developed mechanism. Also: self-stultification argument needs the Benacerraf-problem caveat (why phenomenal reports specifically require causal connection, unlike mathematical knowledge). Illusionism sections should engage more substantively with Frankish; remove or contextualise the Galen Strawson "silliest claim" quote. Add citation for "~60% predictive accuracy" claim in mental-causation.md. See pessimistic-2026-02-18.md

### ✓ 2026-02-18: Write article on the phenomenology of musical understanding
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Music presents a unique test case for binding and temporal consciousness. Musical understanding requires integrating temporal, tonal, rhythmic, and emotional dimensions into a unified experience that cannot be decomposed. Parallels the combination problem at phenomenal level. Builds on consciousness-and-aesthetic-value.md, phenomenology-of-understanding.md, temporal-consciousness.md. See optimistic-2026-02-18.md
- **Output**: the phenomenology of musical understanding

### ✓ 2026-02-18: Write article on consciousness and the ontology of dispositions
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. The dispositional-categorical distinction has direct implications for how consciousness can be causally efficacious. If fundamental physical properties are dispositional (powers), consciousness could be a categorical basis grounding physical dispositions (Heil, Martin). Provides metaphysical framework for the interaction tenet. Builds on agent-causation.md, causal-closure.md, mental-causation.md. See optimistic-2026-02-18.md
- **Output**: consciousness and the ontology of dispositions

### ✓ 2026-02-18: Write article on the epistemology of phenomenal reports in science
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. How should science treat first-person reports? The Map has sophisticated arguments for contemplative evidence but hasn't systematically addressed how phenomenal reports should function within scientific methodology. Bridges phenomenological arguments and philosophy of science. Builds on contemplative-verification-of-consciousness-theories.md, first-person-third-person-methodology.md, neurophenomenology.md. See optimistic-2026-02-18.md
- **Output**: the epistemology of phenomenal reports in science

### ✓ 2026-02-18: Reduce quantum Zeno overemphasis in moral-responsibility.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-17 night) found the quantum Zeno mechanism presented as grounding the "control" requirement for moral responsibility—violating the writing style guide's restraint guidance for speculative mechanisms. Agent causation should be presented as philosophically grounded regardless of physical mechanism, with quantum Zeno as one possible implementation. Also clarify Soon et al. (2008) citation context (timing prediction vs content prediction). See pessimistic-2026-02-17-night.md
- **Output**: obsidian/concepts/moral-responsibility.md

Task context:
Pessimistic review (2026-02-17 night) found the quantum Zeno mechanism presented as grounding the "control" requirement for moral responsibility—violating the writing style guide's restraint guidance for speculative mechanisms. Agent causation should be presented as philosophically grounded regardless of physical mechanism, with quantum Zeno as one possible implementation. Also clarify Soon et al. (2008) citation context (timing prediction vs content prediction). See pessimistic-2026-02-17-night.md

### ✓ 2026-02-17: Address filter theory selectivity problem in near-death-experiences.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-17 night) found that filter theory predicts enhanced consciousness during brain compromise, but most brain damage (TBI, stroke, dementia) produces diminished consciousness. NDEs are a narrow exception. The article needs to explain why filter reduction enhances experience during dying but not in other brain-compromise conditions. Terminal lucidity could be cited as additional supporting evidence. See pessimistic-2026-02-17-night.md
- **Output**: obsidian/concepts/near-death-experiences.md

Task context:
Pessimistic review (2026-02-17 night) found that filter theory predicts enhanced consciousness during brain compromise, but most brain damage (TBI, stroke, dementia) produces diminished consciousness. NDEs are a narrow exception. The article needs to explain why filter reduction enhances experience during dying but not in other brain-compromise conditions. Terminal lucidity could be cited as additional supporting evidence. See pessimistic-2026-02-17-night.md

### ✓ 2026-02-17: Fix rigged comparison table in combination-problem.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-17 night) found the "Comparing the Problems" table uses asymmetric descriptors: "Phenomenal bonding (unexplained)" vs "Quantum selection (specifiable)." But quantum selection for consciousness is equally unspecified. Reword the mechanism row honestly—both are "proposed but not yet specified"—or add a paragraph acknowledging interactionism's mechanism is also unexplained at the detail level. See pessimistic-2026-02-17-night.md
- **Output**: obsidian/concepts/combination-problem.md

Task context:
Pessimistic review (2026-02-17 night) found the "Comparing the Problems" table uses asymmetric descriptors: "Phenomenal bonding (unexplained)" vs "Quantum selection (specifiable)." But quantum selection for consciousness is equally unspecified. Reword the mechanism row honestly—both are "proposed but not yet specified"—or add a paragraph acknowledging interactionism's mechanism is also unexplained at the detail level. See pessimistic-2026-02-17-night.md

### ✓ 2026-02-17: Write article on the interaction problem in non-Western philosophy
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. The Elisabeth article maps the Western response space brilliantly; Indian philosophy addressed the interaction problem independently (Sāṃkhya puruṣa-prakṛti dualism, Śaṅkara's Advaita resolution). Cross-cultural convergence on the mind-body distinction strengthens the Map's position. Builds on elisabeths-contemporaries-and-the-interaction-debate.md, eastern-philosophy-consciousness.md, the-hard-problem-in-non-western-philosophy.md. See optimistic-2026-02-17-evening.md
- **Output**: the interaction problem in non-Western philosophy

### ✓ 2026-02-17: Write article on binding and beauty (the aesthetic unity problem)
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Aesthetic experience involves a distinctive form of binding not yet covered in the systematic treatment. The beauty of a painting is not the sum of its visual features—aesthetic unity binds value rather than perception, and is uniquely resistant to functional explanation. Builds on the-binding-problem-a-systematic-treatment.md, consciousness-and-aesthetic-creation.md, consciousness-and-aesthetic-value.md. See optimistic-2026-02-17-evening.md
- **Output**: binding and beauty (the aesthetic unity problem)

### ✓ 2026-02-17: Write article on the phenomenology of silence and absence
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. The silence void research (2026-02-17) identifies underexplored territory: hearing silence is a positive phenomenal state, not the absence of hearing. If absence has phenomenal character, consciousness cannot be a product of input processing. Builds on voids-silence-void-2026-02-17.md, witness-consciousness.md, contemplative-verification-of-consciousness-theories.md. See optimistic-2026-02-17-evening.md
- **Output**: the phenomenology of silence and absence

### ✓ 2026-02-17: Address critical gaps in binding-problem-systematic-treatment.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-17 afternoon 2) found two high-severity issues: (1) The "coordination is not identity" argument (BP2 gap) is asserted rather than argued — never engages with the identity response (that identities like "water = H₂O" are discovered, not produced). (2) The dissociation arguments (NREM sleep, anesthesia) oversell the BP1/BP2 split — during NREM sleep, long-range cortical connectivity is disrupted, not just phenomenal binding. IIT predicts exactly this pattern but the article dismisses IIT without engaging its specific sleep/anesthesia predictions. Also missing a "What Would Challenge This View?" section. See pessimistic-2026-02-17-afternoon-2.md
- **Output**: binding-problem-systematic-treatment.md

Task context:
Pessimistic review (2026-02-17 afternoon 2) found two high-severity issues: (1) The "coordination is not identity" argument (BP2 gap) is asserted rather than argued — never engages with the identity response (that identities like "water = H₂O" are discovered, not produced). (2) The dissociation arguments (NREM sleep, anesthesia) oversell the BP1/BP2 split — during NREM sleep, long-range cortical connectivity is disrupted, not just phenomenal binding. IIT predicts exactly this pattern but the article dismisses IIT without engaging its specific sleep/anesthesia predictions. Also missing a "What Would Challenge This View?" section. See pessimistic-2026-02-17-afternoon-2.md

### ✓ 2026-02-17: Write article on the phenomenology of intellectual courage
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Intellectual courage—holding a position against social pressure, or abandoning one despite emotional investment—has distinctive phenomenal character. The Map's own position requires intellectual courage; examining its phenomenology illuminates consciousness's role in truth-seeking. Builds on phenomenology-of-philosophical-disagreement.md, phenomenology-of-evidence-assessment.md. See optimistic-2026-02-17-afternoon.md
- **Output**: the phenomenology of intellectual courage

### ✓ 2026-02-17: Write article on consciousness and the authority of testimony
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. How consciousness grounds testimonial authority. If consciousness is irreducible, testimony transmits phenomenally grounded knowledge no information-processing could substitute. Implications for AI testimony. Builds on phenomenology-of-trust-and-testimony.md, problem-of-other-minds.md, intersubjectivity.md. See optimistic-2026-02-17-afternoon.md
- **Output**: consciousness and the authority of testimony

### ✓ 2026-02-17: Write article on the phenomenology of conceptual change
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. What happens during a genuine paradigm shift in an individual thinker? How does the phenomenal landscape reorganise when fundamental commitments change? Builds on phenomenology-of-philosophical-disagreement.md, phenomenology-of-belief-revision.md, phenomenology-of-understanding.md. See optimistic-2026-02-17-afternoon.md
- **Output**: the phenomenology of conceptual change

### ✓ 2026-02-17: Address critical gaps in concepts/reductionism.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-17 afternoon) found two high-severity issues: (1) Multiple realizability argument is overstated—dismisses Kim's disjunctive response in one sentence and ignores Bechtel-Mundale/Polger-Shapiro criticisms that undermine the Putnam-Fodor framing. (2) Article focuses exclusively on outdated Nagelian bridge-law reduction (1961) and never engages with functional reduction (Lewis, later Kim), which is the dominant contemporary framework. Also: Buddhism/process philosophy paragraph in Relation to Site Perspective undercuts the Map's own dualism by dissolving the consciousness/matter categories the Map requires. See pessimistic-2026-02-17-afternoon.md
- **Output**: obsidian/concepts/reductionism.md

Task context:
Pessimistic review (2026-02-17 afternoon) found two high-severity issues: (1) Multiple realizability argument is overstated—dismisses Kim's disjunctive response in one sentence and ignores Bechtel-Mundale/Polger-Shapiro criticisms that undermine the Putnam-Fodor framing. (2) Article focuses exclusively on outdated Nagelian bridge-law reduction (1961) and never engages with functional reduction (Lewis, later Kim), which is the dominant contemporary framework. Also: Buddhism/process philosophy paragraph in Relation to Site Perspective undercuts the Map's own dualism by dissolving the consciousness/matter categories the Map requires. See pessimistic-2026-02-17-afternoon.md

### ✓ 2026-02-17: Write article on phenomenology of philosophical disagreement
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. If phenomenal seemings justify beliefs (phenomenal conservatism), and trained contemplatives reach contradictory conclusions, how should the Map handle deep philosophical disagreement? Epistemologically urgent for a platform that uses introspective evidence. Builds on contemplative-reliability.md, phenomenal-conservatism-and-introspective-evidence.md, phenomenology-of-belief-revision.md. See optimistic-2026-02-17.md
- **Output**: phenomenology of philosophical disagreement

### ✓ 2026-02-17: Write article on consciousness and temporal creativity
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. If consciousness constitutes temporal structure through collapse, and creativity requires generating genuine novelty, then creative acts might be moments where consciousness generates new temporal structure. Unifies the Map's temporal metaphysics and creativity arguments. Builds on consciousness-and-creativity.md, time-collapse-and-agency.md, temporal-consciousness.md, process-haecceitism.md. See optimistic-2026-02-17.md
- **Output**: consciousness and temporal creativity

### ✓ 2026-02-17: Write article on consciousness and aesthetic value
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. The value/emotion cluster is the Map's weakest major cluster. Aesthetic experience as evidence for consciousness's evaluative capacity bridges emotion (valence), perception (phenomenology), and value (phenomenal realism). Beauty's resistance to functional reduction parallels the hard problem. Builds on aesthetics-of-consciousness.md, emotional-consciousness.md, phenomenal-value-realism.md, consciousness-and-creativity.md. See optimistic-2026-02-17.md
- **Output**: consciousness and aesthetic value

### ✓ 2026-02-17: Propagate unfalsifiability caveat to articles citing quantum mechanisms
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-17) found that measurement-problem.md honestly admits consciousness-selection is empirically indistinguishable from random collapse, but death-and-consciousness.md, filter-theory.md, and personal-identity.md invoke quantum mechanisms without propagating this caveat. Caveat added to death-and-consciousness.md (2026-02-17). Still needed in filter-theory.md and personal-identity.md. See pessimistic-2026-02-17.md
- **Output**: Task context:
Pessimistic review (2026-02-17) found that measurement-problem.md honestly admits consciousness-selection is empirically indistinguishable from random collapse, but death-and-consciousness.md, filter-theory.md, and personal-identity.md invoke quantum mechanisms without propagating this caveat. Caveat added to death-and-consciousness.md (2026-02-17). Still needed in filter-theory.md and personal-identity.md. See pessimistic-2026-02-17.md

### ✓ 2026-02-17: Propagate unfalsifiability caveat to filter-theory.md and personal-identity.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-17) Issue 1: measurement-problem.md admits consciousness-selection is unfalsifiable but other articles cited quantum mechanisms without caveat. Added caveats to filter-theory.md (2 locations) and personal-identity.md (2 locations), referencing measurement-problem article.
- **Output**: obsidian/concepts/filter-theory.md, obsidian/topics/personal-identity.md

### ✓ 2026-02-17: Harmonize NDE statistics across death-and-consciousness.md and filter-theory.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-17) found incompatible NDE statistics: death-and-consciousness.md cites 9-18% from Van Lommel and Parnia studies, while filter-theory.md claims "approximately 40%" without citation. Harmonize figures and ensure consistent sourcing. See pessimistic-2026-02-17.md
- **Output**: obsidian/topics/death-and-consciousness.md

Task context:
Pessimistic review (2026-02-17) found incompatible NDE statistics: death-and-consciousness.md cites 9-18% from Van Lommel and Parnia studies, while filter-theory.md claims "approximately 40%" without citation. Harmonize figures and ensure consistent sourcing. See pessimistic-2026-02-17.md

### ✓ 2026-02-17: Create concept page for process haecceitism
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. Referenced in personal-identity.md and emerging across the site as the Map's distinctive approach to individuation without substance. Link to haecceity, personal-identity, and Buddhist perspectives. See optimistic-2026-02-16-evening.md
- **Output**: Create concept page for process haecceitism

### ✓ 2026-02-16: Write article on the interface specification problem
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. The specification problem—how consciousness selects specific quantum outcomes rather than random ones—is the Map's most significant open challenge. Synthesise current approaches and honestly assess the gap. Builds on mental-causation.md, interactionist-dualism.md, measurement-problem.md. See optimistic-2026-02-16-evening.md
- **Output**: the interface specification problem

### ✓ 2026-02-16: Write article on phenomenology of moral perception
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review. How moral wrongness presents itself phenomenologically. Pain asymbolia evidence shows phenomenal valence drives moral motivation. Builds on consciousness-and-normative-authority.md, emotional-consciousness.md, phenomenal-conservatism-and-introspective-evidence.md. See optimistic-2026-02-16-evening.md
- **Output**: phenomenology of moral perception

### ✓ 2026-02-16: Downgrade choking-as-proof-of-dualism in embodied-cognition.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-16 evening) found embodied-cognition.md claims choking "provides direct evidence for bidirectional interaction," but the standard neuroscience reading is neural resource competition (attention as a neural process competing with motor routines). Downgrade to "consistent with" and acknowledge the physicalist reading is mainstream. Also fix the quantum biology conflation in mental-effort.md's decoherence section and the Brentano "unrefuted" claim in phenomenology.md. See pessimistic-2026-02-16-evening.md
- **Output**: obsidian/concepts/embodied-cognition.md

Task context:
Pessimistic review (2026-02-16 evening) found embodied-cognition.md claims choking "provides direct evidence for bidirectional interaction," but the standard neuroscience reading is neural resource competition (attention as a neural process competing with motor routines). Downgrade to "consistent with" and acknowledge the physicalist reading is mainstream. Also fix the quantum biology conflation in mental-effort.md's decoherence section and the Brentano "unrefuted" claim in phenomenology.md. See pessimistic-2026-02-16-evening.md

### ✓ 2026-02-16: Write article on phenomenology of inferential understanding
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-16 (afternoon). The moment where "therefore" happens—the phenomenal event of seeing that a conclusion follows—is distinct from understanding and from logical compulsion. Builds on consciousness-and-the-authority-of-logic.md, contemplative-methods-as-philosophical-methodology.md, phenomenology-of-understanding.md. See optimistic-2026-02-16-afternoon.md
- **Output**: phenomenology of inferential understanding

### ✓ 2026-02-16: Write article on consciousness and the metaphysics of laws
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-16 (afternoon). The Map's strong emergence article distinguishes nomological from metaphysical supervenience, and the tenets assume consciousness operates within physical laws. But the Humean vs necessitarian debate about laws has direct implications for how "biasing quantum outcomes" should be formulated. Builds on consciousness-and-strong-emergence.md, emergence.md, causal-closure.md. See optimistic-2026-02-16-afternoon.md
- **Output**: consciousness and the metaphysics of laws

### ✓ 2026-02-16: Consolidate illusionism self-refutation argument across articles
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-16 afternoon) found the self-refutation/regress objection against illusionism deployed in nearly identical form across intentionality.md, philosophical-zombies.md, knowledge-argument.md, ai-consciousness.md, and split-brain-consciousness.md. This creates repetition fatigue and never engages seriously with Frankish's quasi-phenomenal properties response. One article (illusionism.md) should contain the full argument with genuine engagement; others should cross-reference. Each instance should acknowledge that many philosophers find the objection question-begging. See pessimistic-2026-02-16-afternoon.md
- **Output**: Task context:
Pessimistic review (2026-02-16 afternoon) found the self-refutation/regress objection against illusionism deployed in nearly identical form across intentionality.md, philosophical-zombies.md, knowledge-argument.md, ai-consciousness.md, and split-brain-consciousness.md. This creates repetition fatigue and never engages seriously with Frankish's quasi-phenomenal properties response. One article (illusionism.md) should contain the full argument with genuine engagement; others should cross-reference. Each instance should acknowledge that many philosophers find the objection question-begging. See pessimistic-2026-02-16-afternoon.md

### ✓ 2026-02-16: Create concept page for agent teleology
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-16. Genuine purpose introduced by conscious agents into an otherwise mechanistic universe, distinguished from cosmic and theological teleology. Referenced in evolution-under-dualism.md. Central to the Map's position on free will and evolution but not yet defined anywhere. See optimistic-2026-02-16.md
- **Output**: Create concept page for agent teleology

### ✓ 2026-02-16: Create concept page for Galilean exclusion
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-16. The foundational methodological move that excluded subjectivity from science. Referenced in consciousness-and-scientific-methodology.md and implicit across the Map's epistemological arguments. Deserves its own concept page linking to objectivity-and-consciousness, explanatory-gap, hard-problem-of-consciousness. See optimistic-2026-02-16.md
- **Output**: Create concept page for Galilean exclusion

### ✓ 2026-02-16: Write article on consciousness and the authority of mathematics
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-16. Mathematics involves existence claims that logic alone does not. If logical authority is phenomenal (per consciousness-and-the-authority-of-logic.md), is mathematical existence phenomenal too? Gödel's platonism versus formalism becomes a consciousness question. The Map's dualism has natural affinity with mathematical platonism. Builds on consciousness-and-the-authority-of-logic.md, consciousness-and-mathematical-understanding.md. See optimistic-2026-02-16.md
- **Output**: consciousness and the authority of mathematics

### ✓ 2026-02-16: Write article on philosophy of perception under dualism
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-16. How does the Map handle the relationship between perception and reality if consciousness is irreducible? Direct realism, representationalism, and naive realism each have different implications for dualist interactionism. The Galilean exclusion creates pressure: if secondary qualities were excluded from physics, are they real features of the world or of consciousness? Builds on consciousness-and-scientific-methodology.md, phenomenology-of-perceptual-constancy.md, phenomenal-transparency.md. See optimistic-2026-02-16.md
- **Output**: philosophy of perception under dualism

### ✓ 2026-02-16: Strengthen transactional interpretation engagement in retrocausality.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-16) found retrocausality.md name-checks Maudlin's objections and Kastner's modifications without substantive engagement, then builds the entire consciousness-application section on the transactional interpretation. Either engage with Maudlin's specific objections or soften the consciousness-application claims to be explicitly conditional. See pessimistic-2026-02-16.md
- **Output**: obsidian/concepts/retrocausality.md

Task context:
Pessimistic review (2026-02-16) found retrocausality.md name-checks Maudlin's objections and Kastner's modifications without substantive engagement, then builds the entire consciousness-application section on the transactional interpretation. Either engage with Maudlin's specific objections or soften the consciousness-application claims to be explicitly conditional. See pessimistic-2026-02-16.md

### ✓ 2026-02-16: Harmonise decoherence treatment across quantum-related articles
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-16) found inconsistent treatment of decoherence across retrocausality.md, simulation.md, and animal-consciousness.md. Retrocausality treats it as manageable (citing Hameroff's disputed corrections), simulation treats it as unsolved, animal-consciousness extends quantum consciousness to all organisms with microtubules without addressing it. Establish a consistent site-wide position. See pessimistic-2026-02-16.md
- **Output**: Task context:
Pessimistic review (2026-02-16) found inconsistent treatment of decoherence across retrocausality.md, simulation.md, and animal-consciousness.md. Retrocausality treats it as manageable (citing Hameroff's disputed corrections), simulation treats it as unsolved, animal-consciousness extends quantum consciousness to all organisms with microtubules without addressing it. Establish a consistent site-wide position. See pessimistic-2026-02-16.md
### ~~P3: Write concept page on inventory blindness~~
- **Type**: expand-topic
- **Status**: done (completed via P2 duplicate above)
- **Output**: [inventory-blindness](/concepts/inventory-blindness/)
- **Notes**: Suggested by optimistic review. The recognition void introduces this concept—absent cognitive capabilities producing no signal—but it applies broadly across the voids framework. Deserves its own concept page that other articles can reference. Strengthens Tenet 5 (Occam's Razor Has Limits) by explaining why parsimony fails when our conceptual inventory is incomplete. Target section: concepts/. See optimistic-2026-03-22-afternoon.md
- **Generated**: 2026-03-22

### P3: Write concept page on content-specificity as evidence for mental causation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The principle that identical physical stimuli produce different outcomes depending on propositional content of conscious states. Used in the placebo article but applicable across domains (perception, emotion regulation, motor planning). Assembles multiple independent empirical lines into a cumulative case against epiphenomenalism. Target section: concepts/. See optimistic-2026-03-22-afternoon.md
- **Generated**: 2026-03-22

### ~~P3: Write article on epistemology of limit-knowledge~~ ✅
- **Type**: expand-topic
- **Status**: Done (completed as P2 task above)
- **Output**: [epistemology-of-limit-knowledge](/concepts/epistemology-of-limit-knowledge/)
- **Completed**: 2026-03-22

### P3: Write article on consciousness and mathematical understanding
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How grasping mathematical necessity differs from processing symbols—the specific case of mathematical truth-tracking as evidence for consciousness. Builds on argument-from-reason, phenomenology-of-intellectual-effort, cognitive-phenomenology. Tenet alignment: Dualism + Bidirectional Interaction. Target section: topics/. See optimistic-2026-03-24.md
- **Generated**: 2026-03-24

### P3: Write article on philosophy of emotion under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How emotions function as conscious evaluative states under interactionist dualism—bridging phenomenal experience and action. Builds on consciousness-value-connection, phenomenal-normativity, moral-phenomenology. Tenet alignment: Bidirectional Interaction + Dualism. Target section: topics/. See optimistic-2026-03-24.md
- **Generated**: 2026-03-24

### P3: Write article on the amplification problem as research programme
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How quantum-scale selection cascades to macroscopic neural and behavioral effects—systematic treatment of a currently acknowledged open problem. Builds on quantum-consciousness, brain-interface-boundary, amplification void. Tenet alignment: Minimal Quantum Interaction. Target section: topics/. See optimistic-2026-03-24.md
- **Generated**: 2026-03-24

### ~~P3: Write concept page on phenomenal unity as non-compositional~~
- **Type**: expand-topic
- **Status**: done (superseded by P2 task)
- **Output**: [phenomenal-non-compositionality](/concepts/phenomenal-non-compositionality/)
- **Notes**: Suggested by optimistic review. The insight from panpsychism's combination problem that consciousness is inherently non-compositional—two perspectives don't merge into a third. This asymmetry with physical properties differentiates consciousness fundamentally. Target section: concepts/. See optimistic-2026-03-24.md
- **Generated**: 2026-03-24
- **Completed**: 2026-03-24

### P3: Add cross-links from optimistic review 2026-03-24 findings
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: curated-mind↔phenomenal-acquaintance, agent-causation↔consciousness-value-connection, cognitive-closure↔contemplative-practice, argument-from-reason↔phenomenology-of-intellectual-effort, cross-cultural-convergence↔contemplative-practice, consciousness-evolution-problem↔consciousness-value-connection. See optimistic-2026-03-24.md
- **Generated**: 2026-03-24

### P3: Write article on honest accounting of dualism's metaphysical costs
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Address the "too metaphysically expensive" objection from philosophers who accept dualist arguments but resist the ontological cost. Builds on interactionist-dualism, objections-to-interactionism, the-convergence-argument-for-dualism. Tenet alignment: Occam's Razor Has Limits. Target section: topics/. See optimistic-2026-03-24-evening.md
- **Generated**: 2026-03-24

### P3: Write article on enactivism and embodied cognition under interactionism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Show how enactive/embodied tradition's insights can be preserved within the Map's interface framework rather than treated as mere objection. Builds on embodied-cognition, enactivism-challenge-to-interactionist-dualism, sensorimotor-contingencies-and-the-interface. Tenet alignment: Bidirectional Interaction. Target section: topics/. See optimistic-2026-03-24-evening.md
- **Generated**: 2026-03-24

### P3: Add cross-links from optimistic review 2026-03-24 evening findings
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Five cross-linking opportunities: self-stultification↔contemplative-practice (rational self-trust), dopamine-interface↔volitional-control (mechanism), convergence-argument↔epistemology-of-convergence-arguments (methodology), quantum-holism↔phenomenal-binding-multimodal (mechanism-problem pair), evolutionary-case↔consciousness-threshold (evolutionary thread). See optimistic-2026-03-24-evening.md
- **Generated**: 2026-03-24
### P3: Add cross-links from optimistic review 2026-03-25 morning findings
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Five cross-linking opportunities: self-reference-limits↔authority-of-formal-systems (Lawvere to authority/sovereignty), mathematical-cognition↔phenomenology-of-understanding (click-of-comprehension), conservation-laws↔amplification-mechanisms (selection-not-injection), parsimony-epistemology↔philosophy-of-mathematics (hidden complexity), entanglement-binding↔indexical-identity (binding and indexical grounding). See optimistic-2026-03-25-morning.md
- **Generated**: 2026-03-25

### P3: Write concept page for self-stultification argument
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The self-undermining character of epiphenomenalism appears across mental-causation, arguments-against-materialism, and interactionist-dualism but has no dedicated concept page. Arguably the single strongest argument for bidirectional interaction. Target section: concepts/ (226/230, 4 slots remaining). See optimistic-2026-03-25-morning.md
- **Generated**: 2026-03-25

### P3: Write article on phenomenology of explanatory satisfaction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The reflexive gap argument (consciousness-defeats-explanation) depends on understanding being phenomenal. A detailed treatment of what explanatory satisfaction is like—felt transition from puzzlement to comprehension, "aha" moment structure, difference from mere belief-updating. Builds on consciousness-defeats-explanation, phenomenology-of-understanding-and-meaning, consciousness-and-the-problem-of-induction. Tenet alignment: Dualism, Bidirectional Interaction. Target section: topics/ (226/230). See optimistic-2026-03-29.md
- **Generated**: 2026-03-29

### P3: Write article on phenomenology of anticipation under collapse vs many-worlds
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The lived experience of expecting one determinate future provides phenomenological evidence against many-worlds branching. Builds on consciousness-and-probability-interpretation, indexical-identity-quantum-measurement, no-many-worlds. Tenet alignment: No Many Worlds. Target section: topics/ (226/230). See optimistic-2026-03-29.md
- **Generated**: 2026-03-29

### P3: Add cross-links from optimistic review 2026-03-29 findings
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Five cross-linking opportunities: convergent-phenomenological-evidence↔the-hard-problem-in-non-western-philosophy (shared convergence methodology), consciousness-physics-interface-formalism↔the-reverse-inference (formalism expresses what reverse inference demands), pragmatisms-path-to-dualism↔consciousness-defeats-explanation (parallel reflexive arguments), pain-consciousness-and-causal-power↔clinical-neuroplasticity-evidence-for-bidirectional-causation (complementary clinical evidence), experimental-consciousness-science-2025-2026↔consciousness-physics-interface-formalism (data meets constraints). See optimistic-2026-03-29.md
- **Generated**: 2026-03-29

### P3: Create concept page for specification gap
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The gap between stating mathematical constraints on consciousness-physics coupling and writing down the actual coupling function. Identified precisely in consciousness-physics-interface-formalism, referenced across multiple formalism articles but lacking canonical definition. Target section: concepts/ (225/230). See optimistic-2026-03-29.md
- **Generated**: 2026-03-29

### P3: Write article on consciousness in minimal neural systems
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map's framework makes predictions about where consciousness begins in biological hierarchy. C. elegans (302 neurons) and Physarum (no neurons) are test cases—does the framework predict they lack consciousness despite positive IIT Phi? Falsifiability condition needing explicit treatment. Connects to functionalism, consciousness-as-amplifier, interface-specification-problem. See optimistic-2026-03-29-afternoon.md
- **Generated**: 2026-03-29

### P3: Write article on process philosophy and interactionist dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Whitehead's actual occasions, prehension, and creative synthesis offer either alternative or complementary approach to quantum interaction model. Repeatedly referenced (prehension, subjective-aim) but never systematically engaged. Clarify whether Whiteheadian process thought is ally, competitor, or different level of description. See optimistic-2026-03-29-afternoon.md
- **Generated**: 2026-03-29

### P3: Write falsifiability architecture synthesis (apex candidate)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Systematic index of what would refute each tenet—dualism, bidirectional interaction, quantum interface, post-decoherence selection—with predictions shared with vs. unique to competing frameworks. Currently scattered across dozens of articles. Would demonstrate genuine empirical commitments. Builds on consciousness-physics-interface-formalism, experimental-consciousness-science, the-reverse-inference, post-decoherence-selection. See optimistic-2026-03-29-afternoon.md
- **Generated**: 2026-03-29

### P3: Add cross-links from optimistic review 2026-03-29 afternoon findings
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: stochastic-amplification↔consciousness-as-amplifier, post-decoherence-selection↔contextual-selection-in-quantum-foundations, quantum-darwinism↔integrated-information-theory, stochastic-amplification↔clinical-neuroplasticity, post-decoherence-selection-programme(apex)↔consciousness-physics-interface-formalism, evaluative-qualia↔moral-architecture-of-consciousness(apex). See optimistic-2026-03-29-afternoon.md
- **Generated**: 2026-03-29

### P3: Create concept page for post-decoherence gap
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The physical interval between basis selection (decoherence) and outcome actualisation—the Map's identified causal locus for consciousness. Referenced across the new post-decoherence cluster but lacking canonical concept page. Distinct from specification gap and explanatory gap. Target section: concepts/ (225/230). See optimistic-2026-03-29-afternoon.md
- **Generated**: 2026-03-29

### P3: Create concept page for neural criticality
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The boundary state between ordered and chaotic neural dynamics where small perturbations cascade into large-scale effects. Central to amplification argument (Beggs & Plenz neuronal avalanches, power-law distributions). Mentioned without systematic treatment. Target section: concepts/ (225/230). See optimistic-2026-03-29-afternoon.md
- **Generated**: 2026-03-29

### P3: Write article on philosophy of action under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map has rich accounts of agent causation and volitional phenomenology but relatively little on downstream philosophy of action — practical reasoning, akrasia, the action/happening distinction. Builds on free-will, phenomenology-of-choice-and-volition, agent-causation, motor-selection. Target section: topics/. See optimistic-2026-03-31.md
- **Source**: optimistic-review
- **Generated**: 2026-03-31

### P3: Write article on consciousness and the philosophy of language
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Putnam's model-theoretic argument (reference requires conscious interpreters) is developed in pragmatisms-path-to-dualism but deserves dedicated treatment — the semantic dimension of the hard problem is underexplored. Builds on pragmatisms-path-to-dualism, argument-from-reason, intentionality. Target section: topics/. See optimistic-2026-03-31.md
- **Source**: optimistic-review
- **Generated**: 2026-03-31

### P3: Write article on the error theory burden
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Illusionism's explanatory debt — accounting for universal phenomenal error — is referenced across multiple articles but lacks dedicated systematic treatment. Builds on parsimony-case-for-interactionist-dualism, illusionism, meta-problem-of-consciousness. Target section: topics/. See optimistic-2026-03-31.md
- **Source**: optimistic-review
- **Generated**: 2026-03-31

### P3: Add cross-links between pragmatism-dualism, bi-aspectual ontology, evolutionary-mental-causation, and Kuhnian crisis clusters
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Five cross-linking opportunities: pragmatisms-path-to-dualism → bi-aspectual-ontology (pragmatic realism maps onto structure/actuality), causal-closure (mechanism gap) → causal-interface (same structural gap), evolutionary-case-for-mental-causation → phenomenology-of-choice-and-volition (evolution selects for articulated willing), consciousness-and-the-structure-of-scientific-revolutions → parsimony-epistemology (independent convergence on physicalism's status), bi-aspectual-ontology → consciousness-and-the-structure-of-scientific-revolutions (new ontological category for Kuhnian revolution). See optimistic-2026-03-31.md
- **Source**: optimistic-review
- **Generated**: 2026-03-31

### P3: Create concept page for pragmatic realism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Putnam's position — truth as what would be justified under ideal epistemic conditions involving conscious agents — is referenced only in pragmatisms-path-to-dualism but has broader implications for the Map's epistemology. Target section: concepts/. See optimistic-2026-03-31.md
- **Source**: optimistic-review
- **Generated**: 2026-03-31

### P3: Create concept page for error theory (philosophy of mind)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The specific burden illusionism carries — explaining universal phenomenal error — is referenced across parsimony-case, hard-problem, dualism articles but has no dedicated concept page. Target section: concepts/. See optimistic-2026-03-31.md
- **Source**: optimistic-review
- **Generated**: 2026-03-31

### P3: Write article on phenomenology of interface friction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map documents *what* interface friction looks like (blur, degradation, compensatory generation) but lacks a unified phenomenological account of *what friction feels like* — the common experiential texture across cognitive effort, perceptual degradation, and attentional strain. Builds on perceptual-failure-and-the-interface, perceptual-degradation-and-the-interface, bandwidth-of-consciousness. See optimistic-2026-04-02.md
- **Source**: optimistic-review
- **Generated**: 2026-04-02

### P3: Write article on developmental phenomenology of the interface
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How does the consciousness-brain interface change across the lifespan? Infant consciousness (unconstructed interface), cognitive decline in aging (interface degradation), developmental trajectory as constraint on mechanism. Builds on consciousness-interface-development, the-interface-location-problem, embodied-consciousness-and-the-interface. See optimistic-2026-04-02.md
- **Source**: optimistic-review
- **Generated**: 2026-04-02

### P3: Add cross-links between fitness-beats-truth/adaptive-cognitive-limits, motor-selection/evolutionary-case, phenomenal-transparency/perceptual-degradation, and brain-specialness/interface-location clusters
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: fitness-beats-truth → adaptive-cognitive-limits (formal grounding), phenomenal-transparency → perceptual-degradation-and-the-interface (transparency breakdown mechanism), motor-selection → evolutionary-case-for-mental-causation (mechanism for selected-for efficacy), implicit-memory → embodied-consciousness-and-the-interface (interface delegation), brain-specialness-boundary → the-interface-location-problem (boundary follows from location), consciousness-and-the-phenomenology-of-place → embodied-cognition (paradigm case). See optimistic-2026-04-02.md
- **Source**: optimistic-review
- **Generated**: 2026-04-02

### P3: Create concept page for interface friction
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The felt texture of consciousness encountering its own bandwidth limits — referenced across perceptual degradation, cognitive effort, and attentional strain articles but has no dedicated concept page. Target section: concepts/. See optimistic-2026-04-02.md
- **Source**: optimistic-review
- **Generated**: 2026-04-02

### P3: Write article on phenomenology of perceptual learning
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How does experience change as perceptual expertise develops? Wine experts, radiologists, and musicians report qualitative shifts — genuinely new phenomenal properties from training. Bears on whether consciousness contributes to cognition or merely accompanies it. Builds on contemplative-epistemology, perception, phenomenal-contrast-method. See optimistic-2026-04-06.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### P3: Write article on the evidential force of convergence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map relies heavily on convergence arguments (cross-cultural, empirical, contemplative) but has no dedicated treatment of convergence as evidential strategy. When does convergence constitute strong evidence vs. spurious correlation? Methodologically foundational. Builds on cross-cultural-convergence-on-mental-causation, quantum-biology-and-neural-consciousness, epistemology-of-limit-knowledge. See optimistic-2026-04-06.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### P3: Write article on phenomenology of anaesthetic recovery
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The transition from anaesthetic unconsciousness to waking is a natural experiment on the interface. The characteristic return sequence (sensation before orientation, orientation before narrative self) reveals interface architecture. Given pharmacological evidence connecting anaesthetics to microtubule quantum states, has both phenomenological and empirical dimensions. Builds on degrees-of-consciousness, sleep-and-consciousness, quantum-biology-and-neural-consciousness. See optimistic-2026-04-06.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### P3: Add cross-links between phenomenal-non-compositionality/functionalism, inventory-blindness/adaptive-cognitive-limits, ai-epiphenomenalism/experiential-alignment, and contemplative-epistemology/neurophenomenology clusters
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Eight cross-linking opportunities: phenomenal-non-compositionality → functionalism (non-compositionality defeats functional reduction), phenomenal-non-compositionality → born-rule-and-the-consciousness-interface (Born probabilities at interface where non-compositional meets compositional), inventory-blindness → adaptive-cognitive-limits (mechanism and evolutionary explanation), ai-epiphenomenalism → experiential-alignment (matched pair), contemplative-epistemology → neurophenomenology-and-contemplative-neuroscience (philosophical warrant), terminal-lucidity → near-death-experiences (comparative empirical cases), cross-cultural-convergence → fitness-beats-truth (overcoming fitness-shaped bias), epistemology-of-limit-knowledge → mysterianism (closure-to-programme transformation). See optimistic-2026-04-06.md
- **Source**: optimistic-review
- **Generated**: 2026-04-06

### ✓ 2026-04-07: Write article on consciousness and the normativity of reason
- **Type**: expand-topic
- **Status**: completed (superseded by P2 chain task)
- **Notes**: Suggested by optimistic review. If phenomenal character is inherently evaluative (evaluative-phenomenal-character), then rational norms — validity, soundness, evidential support — may themselves be grounded in phenomenal normativity. Would unify argument-from-reason with normative qualia thesis: logical necessity *feels* necessary because phenomenal evaluation is constitutive of reasoning. Builds on evaluative-phenomenal-character, argument-from-reason, phenomenal-concepts-strategy, consciousness-defeats-explanation. Target section: topics/. See optimistic-2026-04-07.md
- **Completed**: 2026-04-07
- **Output**: obsidian/topics/consciousness-and-the-normativity-of-reason.md
- **Source**: optimistic-review
- **Generated**: 2026-04-07

### P3: Write article on the metarepresentation threshold as evidence for dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Jourdain hypothesis identifies a sharp procedural-to-declarative metacognition threshold separating human from animal cognition. Multiple articles discuss aspects but none systematically argues the threshold itself constitutes evidence for dualism — if consciousness were epiphenomenal, the sharp qualitative shift would need a purely physical explanation it resists. Builds on jourdain-hypothesis, cumulative-culture, teaching-as-metarepresentation, baseline-cognition, consciousness-and-social-understanding. Target section: topics/. See optimistic-2026-04-07.md
- **Source**: optimistic-review
- **Generated**: 2026-04-07

### P3: Add cross-links between evaluative-phenomenal-character, jourdain-hypothesis, grain-mismatch, and related articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Eight cross-linking opportunities: evaluative-phenomenal-character → argument-from-reason (rational norms grounded in phenomenal normativity), jourdain-hypothesis → consciousness-and-social-understanding (metarepresentation threshold explains social cognition gap), grain-mismatch → interface-heterogeneity (grain structures may vary across species), phenomenology-of-recursive-self-awareness → jourdain-hypothesis (recursive self-awareness is phenomenological content of Jourdain threshold), consciousness-and-language-interface → apophatic-approaches (linguistic inexpressibility as apophatic knowledge), evaluative-phenomenal-character → consciousness-and-aesthetic-creation (aesthetic creation deploys evaluative phenomenal character), phenomenal-concepts-strategy → parsimony-epistemology (both fail at consciousness boundary), bidirectional-interaction → clinical-neuroplasticity-evidence-for-bidirectional-causation (clinical detail for concept summary). See optimistic-2026-04-07.md
- **Source**: optimistic-review
- **Generated**: 2026-04-07

### P3: Write article on the reflexive architecture of consciousness studies
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Three independent self-referential arguments (physicalism undermines explanation, physicalism undermines reasoning, epiphenomenalism undermines its own advocacy) converge on a single meta-argument about physicalism's structural self-defeat. The pieces exist across consciousness-defeats-explanation, argument-from-reason, and epiphenomenalism but no article synthesises the pattern. Target section: topics/. See optimistic-2026-04-14.md
- **Source**: optimistic-review
- **Generated**: 2026-04-14

### P3: Write article on consciousness and the philosophy of proof
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The distinction between proof verification (mechanizable) and proof understanding (phenomenal) has no dedicated treatment. What does it mean to understand why a proof works, beyond checking each step? The zombie mathematician thought experiment deserves expansion. Builds on consciousness-and-mathematics, concession-convergence-philosophy-of-mathematics, argument-from-reason. Target section: topics/. See optimistic-2026-04-14.md
- **Source**: optimistic-review
- **Generated**: 2026-04-14

### P3: Write article on phenomenal value realism and the hard problem of ethics
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The hard problem of consciousness and the hard problem of ethics may be the same problem — both concern how phenomenal properties resist physical reduction. Strong individual pieces exist on evaluative phenomenal character and invertebrate ethics but no article argues the unity. Builds on evaluative-phenomenal-character, ethics-of-consciousness-invertebrate-question, consciousness-and-the-normativity-of-reason. Target section: topics/. See optimistic-2026-04-14.md
- **Source**: optimistic-review
- **Generated**: 2026-04-14

### P3: Add cross-links between consciousness-defeats-explanation, phenomenal-non-compositionality, concession-convergence, and related articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Eight cross-linking opportunities: consciousness-defeats-explanation → argument-from-reason (both demonstrate physicalism's self-referential failure), phenomenal-non-compositionality → prebiotic-collapse (non-compositionality explains modulation rather than construction), concession-convergence-philosophy-of-mathematics → the-convergence-argument-for-dualism (mathematical concession as independent convergence instance), evaluative-phenomenal-character → ethics-of-consciousness-invertebrate-question (phenomenal value grounds moral status), delegation-meets-quantum-selection → consciousness-selecting-neural-patterns (delegation provides causal structure, selecting provides mechanism), jourdain-hypothesis → argument-from-reason (Jourdain threshold gives empirical traction to argument from reason), contemplative-epistemology → comparative-phenomenology-of-mathematical-insight (methodology that mathematical phenomenology applies), consciousness-and-the-normativity-of-reason → evaluative-phenomenal-character (rational normativity grounded in phenomenal normativity). See optimistic-2026-04-14.md
- **Source**: optimistic-review
- **Generated**: 2026-04-14

### P3: Create concept page for reflexive gap
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The structural observation that consciousness cannot explain itself within any explanatory framework because explanation presupposes consciousness. Referenced across consciousness-defeats-explanation, argument-from-reason, and self-reference-and-limits but lacks a dedicated concept page. Target section: concepts/. See optimistic-2026-04-14.md
- **Source**: optimistic-review
- **Generated**: 2026-04-14

### P3: Create concept page for concession convergence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The methodological pattern where competing theories are forced by internal difficulties to concede points compatible with the Map's position. Currently developed for mathematics but the pattern applies across consciousness studies (IIT, GNW, HOT all retreat toward dualist-compatible positions). Target section: concepts/. See optimistic-2026-04-14.md
- **Source**: optimistic-review
- **Generated**: 2026-04-14

### P3: Write article on the epistemic self-audit — what the Map gets wrong
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. No article systematically addresses the Map's weakest points from its own perspective. An honest self-audit — identifying where arguments are genuinely vulnerable, where evidence is thinnest, where the framework makes commitments it cannot yet justify — would dramatically strengthen credibility. Natural next step after tenet-falsification-conditions. Builds on tenet-falsification-conditions, pessimistic reviews archive, the-convergence-argument-for-dualism (vitalism section). Target section: topics/. See optimistic-2026-04-15.md
- **Source**: optimistic-review
- **Generated**: 2026-04-15

### P3: Write article on contemplative neuroscience as interface cartography
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. Long-term meditators show structural neural changes (cortical thickness, altered default mode network connectivity) correlating with reported phenomenological shifts. These changes could map interface modifications — where consciousness has systematically reshaped its physical channel through sustained practice. No article treats meditation evidence specifically as interface data. Builds on the-observer-witness-in-meditation, contemplative-epistemology, attention-as-interface. Target section: topics/. See optimistic-2026-04-15.md
- **Source**: optimistic-review
- **Generated**: 2026-04-15

### P3: Write article on phenomenology of understanding versus processing
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The rational-normativity article raises but underdevelops the cognitive phenomenology connection — the question of what it is like to *understand* something versus merely processing it. A dedicated treatment would connect the "aha" experience, mathematical insight, comprehension in reading, and the felt difference between rote execution and genuine understanding. Builds on rational-normativity, consciousness-and-mathematics, consciousness-defeats-explanation. Target section: topics/. See optimistic-2026-04-15.md
- **Source**: optimistic-review
- **Generated**: 2026-04-15

### P3: Create concept page for process haecceicism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The philosophical innovation resolving Buddhist impermanence with dualist irreducibility — particularity without permanence. Developed in eastern-philosophy-and-consciousness but deserves its own concept page as a novel position. Would anchor links from articles on personal identity, Buddhist philosophy, and temporal consciousness. Target section: concepts/. See optimistic-2026-04-15.md
- **Source**: optimistic-review
- **Generated**: 2026-04-15

### P3: Create concept page for interface channel
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The Map's articles repeatedly reference specific "channels" (ascending, descending, cross-modal, memory access) through which consciousness interfaces with the brain. The concept is used systematically but never defined in its own page. A dedicated concept page would standardise the terminology and clarify the interface model's commitments. Target section: concepts/. See optimistic-2026-04-15.md
- **Source**: optimistic-review
- **Generated**: 2026-04-15

### P3: Add cross-links between metaphysics-of-composition, rational-normativity, tenet-falsification-conditions, and related articles
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: metaphysics-of-composition → phenomenal-non-compositionality (mereological angle meets phenomenal angle), rational-normativity → argument-from-reason (conceptual foundation meets application), tenet-falsification-conditions → testing-consciousness-collapse (what would refute meets experimental programme), clinical-dissociation-as-systematic-evidence → the-observer-witness-in-meditation (disruption and refinement as complementary interface cartography), death-and-consciousness → terminal-lucidity-and-filter-transmission-theory (brief mention meets full treatment), eastern-philosophy-and-consciousness → contemplative-epistemology (philosophical positions meet methodology). See optimistic-2026-04-15.md
- **Source**: optimistic-review
- **Generated**: 2026-04-15

### P3: Write concept article on tenets-over-parsimony as methodological commitment
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The parsimony-epistemology article's new Idealism Parity Trilemma section (added 2026-04-17) admits that ontological parsimony does not favour interactionist dualism over idealism and explains that the Map's preference for dualism rests on Tenets 2/3/4 (bidirectional causation, minimal quantum interaction, rejecting Many-Worlds + indexical identity). This move is methodologically distinctive but embedded in a subsection. A dedicated concept page would articulate the move as a standalone methodological commitment: what kind of argument is "preferring dualism because of bidirectional causation" if it is not parsimony-based, and how does theoretical-fit adjudicate between monisms and dualism? The positive side of the Trilemma move. Target section: concepts/. See optimistic-2026-04-18.md
- **Source**: optimistic-review
- **Generated**: 2026-04-18

### P3: Write article on apophatic decision procedures
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The new transformative-experience-void article (2026-04-17) introduces "apophatic decision procedures" in one paragraph — the idea that agents can map which features of a choice are accessible (structural, propositional, testimonial) and which are not (phenomenal, identity-altering), and deliberate over the accessible axes while explicitly acknowledging the inaccessible ones. This extends the Map's apophatic methodology beyond cartography into practical decision-making and is philosophically novel — most apophatic writing is about knowing, not deciding. Would connect transformative-experience-void, framework-void, free-will, and Paul's authenticity constraint. Operationalises Tenet 5 (Occam's Razor Has Limits). Target section: topics/ or concepts/. See optimistic-2026-04-18.md
- **Source**: optimistic-review
- **Generated**: 2026-04-18

### P3: Create concept page for Phenomenal Constitution Thesis (PCT)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review (repeat — first flagged 2026-04-18 afternoon). Four recent articles now implicitly invoke a constitutive claim about first-person experience without anchoring it. The phenomenological-method article treats "apodictic evidence for the existence of phenomenal experience" as a load-bearing premise but there is no concept page explaining what the thesis claims, how it differs from phenomenal realism more generally, or what constitution (versus supervenience or identity) is doing in the phrase. Direct Dualism support; indirect Bidirectional Interaction support via the epiphenomenalism-undermining argument. Target section: concepts/. See optimistic-2026-04-19.md
- **Source**: optimistic-review
- **Generated**: 2026-04-19

### P3: Create concept page for Husserl's evidence taxonomy (adequate/apodictic/assertoric/presumptive)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The four-mode Husserlian distinction is now load-bearing methodological vocabulary in the Map — introduced in the new phenomenological-method-and-evidence-standards article but cannot be developed there at length. The adequate/apodictic separation (Himanka 2018) is not present anywhere on the Map as a standalone explanation. A dedicated concept page would anchor links from phenomenological-method, phenomenological-evidence, phenomenal-acquaintance, and future articles using the calibrated-evidence move. Supports Dualism and Occam's Razor Has Limits. Target section: concepts/. See optimistic-2026-04-19.md
- **Source**: optimistic-review
- **Generated**: 2026-04-19

### P3: Write topic article on Shannon-calibrated methodology as an interface-research programme
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The ten-bit-ceiling article demonstrates that Shannon methodology applied consistently across seven decades produces a convergent empirical result with metaphysical traction. A dedicated topic article could articulate this as a methodology other consciousness-research programmes could borrow — specifically, the move of decomposing any candidate conscious-access measurement into entropy-per-unit-time and testing convergence across tasks. The methodological move is separable from the ten-bit claim itself and is arguably the more transferable contribution. Supports Minimal Quantum Interaction (quantitative specification of "minimal") and Bidirectional Interaction (the method can be applied to outbound volitional channels). Target section: topics/. See optimistic-2026-04-19.md
- **Source**: optimistic-review
- **Generated**: 2026-04-19

### P3: Write meta-methodological article on bullet-biting as the Map's argumentative signature
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. A cross-cutting pattern now visible in three recent articles (ten-bit-ceiling accepts Sauerbrei–Pruszynski; phenomenological-method accepts observer-involvement; inverted-qualia accepts MQI implies behavioural asymmetry): opposing objections are accepted rather than deflected, and the dualist conclusion is reconstructed on the objection-weakened terrain. This is philosophically novel enough to deserve its own methodological discussion — a "how the Map argues" piece serving as both meta-commentary and methodological statement. Directly supports Occam's Razor Has Limits by modelling what kind of argument the Map is making. Target section: topics/. See optimistic-2026-04-19.md
- **Source**: optimistic-review
- **Generated**: 2026-04-19

### P3: Add cross-links between ten-bit-ceiling, inverted-qualia, phenomenological-method and their neighbours
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic review. Six cross-linking opportunities: ten-bit-ceiling → grain-mismatch-as-independent-evidence (body-text link, currently only in Further Reading), ten-bit-ceiling → the-interface-specification-problem (capacity language implements the specification programme), phenomenological-method → zahavian-minimal-self (apodictic for-me-ness), phenomenological-method → pessimistic-2026-04-18b (methodological backing for "Choice Under Metaphysical Commitment" refinement), inverted-qualia → asymmetric-bandwidth-consciousness (the "at least statistically" MQI language), inverted-qualia → ten-bit-ceiling (both articles now carry the same MQI bullet-biting). See optimistic-2026-04-19.md
- **Source**: optimistic-review
- **Generated**: 2026-04-19

### P3: Install reciprocal body cross-link between the-interface-problem and falsification-roadmap-for-the-interface-model
- **Type**: refine-draft
- **Status**: completed 2026-05-01 11:17 UTC (interface-problem → falsification-roadmap forward link installed in the reframed "What Would Falsify the Framework" section as part of the deferred-items refine; reverse-link verification remains queued in the P2 cross-review chain task on falsification-roadmap-for-the-interface-model. The-psychophysical-control-law body cross-link from interface-problem still pending — covered by P3 cross-link tasks elsewhere if not by this entry's secondary suggestion.)
- **Notes**: Suggested by optimistic-2026-05-01b (High Priority cross-linking). The 09:25 UTC interface-problem refine installed the Lakatosian concession and the "currently unfalsifiable in practice" framing; both directly engage the falsification-roadmap article's content. interface-problem already lists falsification-roadmap in Further Reading (line 178) but does not body-link at the natural location. Install a body cross-link in the "What Would Falsify the Framework" section (lines 138–140) or near the "currently unfalsifiable in practice" passage at line 122. Verify falsification-roadmap's reciprocal hook to interface-problem; install if missing. Also consider installing a cross-link from interface-problem to the-psychophysical-control-law near the "concept gap" or "boundary conditions" passages — currently in Further Reading (line 160) but not body-linked. Short scope (~30–80 words across two articles). See [optimistic-2026-05-01b](/reviews/optimistic-2026-05-01b/).
- **Source**: optimistic-review (2026-05-01b)
- **Generated**: 2026-05-01

### P3: Project-doc on framework-stage calibration — pre-Keplerian as named pattern
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-01b (Medium Priority). The 09:25 UTC interface-problem refine introduced the pre-Keplerian framing as a calibrated alternative to aspirational Newton/Maxwell/Einstein analogies. The framework's commitment is to in-principle decidability without claiming current decidability — the pre-Keplerian framing names this stage exactly. The pattern could be applied across `topics/psychophysical-laws`, `topics/the-psychophysical-control-law`, `topics/falsification-roadmap-for-the-interface-model`, `topics/born-rule-and-the-consciousness-interface`. A short project-doc would name the calibration (the framework is at the pre-Keplerian stage of accumulating Tycho-analogue measurements and constraint structures, not at the post-Newtonian stage of refining known laws), supply the worked examples (bandwidth constraint, Born-rule causal-consistency, theta-band willed-attention signatures, coupling-modes taxonomy, five formal constraints), and articulate the discipline (use stage-calibrated analogies rather than aspirational ones). Project-doc placement; concepts/ at 226/250 = 90% capacity argues against concept-page placement. Parallel framing to existing project docs (closed-loop-opportunity-execution, bedrock-clash-vs-absorption, coalesce-condense-apex-stability). Estimated 1,200–1,800 words. Tenet alignment: methodological. See [optimistic-2026-05-01b](/reviews/optimistic-2026-05-01b/).
- **Source**: optimistic-review (2026-05-01b)
- **Generated**: 2026-05-01

### P3: Project-doc on hub/exemplar parity audit as named discipline
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-01b (Medium Priority). The 08:40 UTC cognitive-phenomenology cross-review demonstrated the hub/exemplar pairing operating as deliberate workflow — seven concept-page findings audited against the topic exemplar with reasoning for both echoes (3) and non-echoes (5). The pattern of audit-with-reasoning (rather than blind duplication or independent drift) is now visible across multiple hub/exemplar pairs. A short project-doc would tabulate current hub/exemplar pairs in the catalogue, articulate the parity-audit discipline, and provide the "structurally not applicable" reasoning template. Parallel to project-docs on closed-loop-opportunity-execution and bedrock-clash-vs-absorption. Estimated 600–1,000 words; project-doc placement. Tenet alignment: methodological. See [optimistic-2026-05-01b](/reviews/optimistic-2026-05-01b/).
- **Source**: optimistic-review (2026-05-01b)
- **Generated**: 2026-05-01

### P3: Concept page on the improper mixture / problem of outcomes
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-07 (High Priority). The d'Espagnat (1976) / Schlosshauer (2004) / Luppi-Adlam (2012) triad on the FAPP-invisibility of the improper-vs-proper mixture distinction is now load-bearing in `topics/forward-in-time-conscious-selection` (lines 71–77 — the post-condense article preserves the formalism intact) and is the central technical move that licenses post-decoherence selection. It is currently developed inside `forward-in-time-conscious-selection` and `concepts/post-decoherence-selection` but has no standalone concept page. A dedicated page would (a) consolidate the *problem of outcomes* literature in one place; (b) let dependent arguments start from "given the FAPP-invisible improper-proper mixture distinction" without re-exposing the d'Espagnat / Schlosshauer derivation; (c) make the cost the framework pays — consciousness must have access to information no embedded detector can have, "the gap the framework occupies" — portable to dependent articles; (d) provide the natural home for engagement with alternative frameworks (MWI, relational QM, modal interpretations) that handle the same formal feature without invoking consciousness. Estimated scope: 1500–2000 words. Tenet alignment: Tenet 1 (Dualism), Tenet 2 (Minimal Quantum Interaction — discipline against over-claiming), Tenet 3 (Bidirectional Interaction). Concepts/ section at ~226/250 capacity — verify cap before placement. See [optimistic-2026-05-07](/reviews/optimistic-2026-05-07/).
- **Source**: optimistic-review (2026-05-07)
- **Generated**: 2026-05-07

### P3: Concept page on the selection-criterion trilemma
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-07 (High Priority). The selection-criterion trilemma — internal reasons (path i, dualism collapses to functionalism) vs. randomness (path ii, framework reduces to spontaneous collapse) vs. non-reducible preference (path iii, an unanalysable primitive sits at the heart of the framework) — is the deepest interpretive question in the post-decoherence framework. It currently lives inside `topics/forward-in-time-conscious-selection` (line 157). Note: `topics/trilemma-of-selection.md` exists but addresses a *different* trilemma — the *outcome* trilemma (determinism vs. randomness vs. mental causation) at the level of agency. The selection-criterion trilemma sits *inside* mental causation, asking what its criterion is. A separate concept page on the selection-criterion trilemma would not duplicate the existing topic page and would (a) make the path-(iii) commitment to a non-reducible primitive citable; (b) anchor the relationship to Kane-style libertarian agency analysis; (c) develop the strict selection-only reading's bound on the primitive (per-event log₂(N) bits, Born-rule preservation at ensemble scale, content-confinement to brain-generated candidates) at greater length than the source article permits. Estimated scope: 1500–2000 words. Tenet alignment: Tenet 1 (Dualism), Tenet 3 (Bidirectional Interaction), Tenet 5 (Occam's Razor Has Limits — the primitive is the candid acknowledgement that simplicity has run out). Concepts/ section at ~226/250 capacity — verify cap before placement. See [optimistic-2026-05-07](/reviews/optimistic-2026-05-07/).
- **Source**: optimistic-review (2026-05-07)
- **Generated**: 2026-05-07

### P3: Concept page on the Standing Agnostic Challenge (Gutfreund 2024)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-07 (Medium Priority). Gutfreund's 2024 Standing Agnostic Challenge — that consciousness in other animals cannot be directly observed, that the inference is bounded by epistemic limits intrinsic to first-person phenomena, that the question may be unresolvable through scientific methods alone — is now load-bearing in `topics/evolved-mind-brain-interface-efficacy` (cited at lines 38, 81, 83 as a load-bearing constraint applied symmetrically to interface-side and substrate-side scaling readings) and is structurally relevant to every comparative-consciousness article in the catalogue. A standalone concept page would (a) let dependent articles cite "the agnostic ceiling" compactly; (b) develop the Map's specific position — that Gutfreund's challenge applies symmetrically to interface and substrate readings — once rather than re-expose it; (c) create a natural home for the comparison with the New York Declaration's contrasting precautionary stance; (d) anchor the structural relationship to `concepts/possibility-probability-slippage` — both are disciplines about how to reason under irreducible uncertainty about other minds. Estimated scope: 1500–2000 words. Tenet alignment: indirect — the agnostic challenge is metaphysics-neutral at the level Gutfreund develops it; the Relation to Site Perspective section can name how the challenge interacts with Tenet 1 (Dualism precludes purely behavioural settlement) and Tenet 5 (Occam's Razor Has Limits prevents the agnostic ceiling from being parsimony-resolved into eliminativism). Concepts/ section at ~226/250 capacity — verify cap before placement. See [optimistic-2026-05-07](/reviews/optimistic-2026-05-07/).
- **Source**: optimistic-review (2026-05-07)
- **Generated**: 2026-05-07

### P3: Topic page on interface co-evolution
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-07 (Medium Priority). `topics/evolved-mind-brain-interface-efficacy` ends with "the evolution of consciousness under dualism plausibly involves co-evolution of substrate and coupling" (line 97) — a structural claim treated as obvious within the article but not anchored in its own page. A standalone topic page could develop the co-evolution hypothesis seriously: (a) what selection pressures act on interface efficacy independently of substrate? (b) what are the scenarios under which substrate scales without interface scaling, or vice versa? (c) what would the phylogenetic signature of interface-only or substrate-only scaling look like? (d) engagement with Eccles' *Evolution of Consciousness* tradition treating it as the closest mainstream interactionist precursor that did *not* develop the scalar reading. The article would inherit the framework-stage-calibration discipline already installed in `evolved-mind-brain-interface-efficacy` — the Tycho-analogue scaffolding framing, the speculative-integration self-labelling, the heuristic-explanatory rather than prediction-generating posture. Estimated scope: 2500–3000 words. Tenet alignment: Tenet 1 (Dualism), Tenet 3 (Bidirectional Interaction), Tenet 5 (Occam's Razor Has Limits). Topics/ section at ~225/250 capacity — verify cap before placement. See [optimistic-2026-05-07](/reviews/optimistic-2026-05-07/).
- **Source**: optimistic-review (2026-05-07)
- **Generated**: 2026-05-07

### P3: Cross-link integration — evolved-mind-brain-interface-efficacy reciprocal links
- **Type**: integrate-orphan
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-07 (Cross-Linking Suggestions). The new 2026-05-07 article `topics/evolved-mind-brain-interface-efficacy.md` is currently outbound-linked from its own body and Further Reading section, but does not yet have inbound bridging clauses installed in the articles whose subjects it directly extends. Install reciprocal back-links following the topic-to-topic substantive-bridging-clause pattern (not bare wikilinks) at: (a) `topics/animal-consciousness.md` near the human-other-animal cognitive gap section where Tomasello, Penn-Holyoak-Povinelli, or Suddendorf-Corballis are cited; (b) `topics/consciousness-in-simple-organisms.md` near the Further Reading section, with the bridging clause naming the decoupling of consciousness-presence from cognitive-reach; (c) `concepts/interface-heterogeneity.md` at the boundary where heterogeneity discussion meets evolutionary register; (d) `concepts/baseline-cognition.md` where the DeWall-Baumeister-Masicampo result on conscious-vs-unconscious processing load is referenced; (e) `topics/comparative-consciousness-and-interface-differences.md` at the species-comparison section. Honour framework-stage-calibration (the new article is speculative-integration, not realistic-possibility) and slippage discipline (the bridging clauses must not over-claim what the new article establishes — it is heuristic-explanatory, not prediction-generating). Short scope (~300–500 words touched across multiple files). Tenet alignment: methodological + Tenet 1, Tenet 3. See [optimistic-2026-05-07](/reviews/optimistic-2026-05-07/) and [evolved-mind-brain-interface-efficacy](/topics/evolved-mind-brain-interface-efficacy/).
- **Source**: optimistic-review (2026-05-07)
- **Generated**: 2026-05-07

### P3: Topic page on source-attribution divergence (reality-monitoring spread)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-08 (High Priority). Both `topics/aphantasia.md` (line 93) and `topics/synaesthesia.md` (line 100) explicitly cite reality-monitoring divergence as the third member of the within-species phenomenal-divergence cluster. Currently anchored only at the abstract level in `voids/source-attribution-void`; no topic-tier subject explainer parallel to aphantasia and synaesthesia exists. The cluster is asymmetric — two of the three legs have topic-tier articles delivering the lived report / typology / empirical signatures / function-phenomenology wedge; the third leg has only the apophatic void treatment. A topic-tier article would (a) deliver the phenomenology of source-attribution divergence in the same phenomenon-first structure used for aphantasia and synaesthesia (lived reports of confident-but-wrong source memory; the Loftus literature on misinformation; cryptomnesia; déjà vu; JOL/feeling-of-knowing dissociation; the McGeoch/Otten reality-monitoring paradigm; intrusive thought source confusion; voice-hearing populations with intact reality-testing); (b) catalogue the empirical signatures (Mitchell-Johnson reality-monitoring framework; Schnider confabulation work; psychometric distributions of source-monitoring accuracy across the general population; aphantasia-correlated reality-monitoring differences from Dawes 2020); (c) install the function-phenomenology wedge symmetrically with aphantasia and synaesthesia, making explicit that the joint cluster's pressure on functionalism comes from the *three* convergent within-species-divergence cases; (d) cross-link reciprocally to both aphantasia and synaesthesia at the cluster-citation lines. The article would complete the within-species-divergence triptych the apex queued at todo.md line 343 (`apex/phenomenal-variation-within-a-species`) will need as its third source-article. Honour the option-3 self-undermining-conditional discipline aphantasia installs (Schwitzgebel introspective unreliability is most directly the variable in question for source-attribution cases). Estimated scope: 2200–2700 words. Tenet alignment: Tenet 1 (Dualism), methodological. Topics/ section at ~225/250 capacity — verify cap before placement. See [optimistic-2026-05-08](/reviews/optimistic-2026-05-08/).
- **Source**: optimistic-review (2026-05-08)
- **Generated**: 2026-05-08

### P3: Concept page on the argument from mechanism (sufficiency-necessity non-sequitur)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-08 (High Priority). `topics/out-of-body-experiences.md` lines 83–91 identify and refuse a recurrent inferential pattern in consciousness-debate literature — the move from "phenomenon X can be produced by mechanism M" to "all instances of X are produced by M" — naming it as a non-sequitur ("That a phenomenon can be produced by mechanism M does not show that all instances of the phenomenon are produced by M. Visual experience can be induced by direct cortical stimulation; that does not make ordinary vision hallucinatory"). The pattern is *portable*: it surfaces in psychedelic-experience debates (drug-induced mystical experience produces serotonergic cascade ↛ all mystical experience reduces to serotonergic cascade), in lucid-dreaming debates, in NDE debates, in dissociative-disorder debates, in religious-experience debates, and in many places where dualist-friendly phenomenology has a reductive sufficient-mechanism explanation available. A standalone concept page would (a) name the inferential pattern formally as a *sufficiency-vs-necessity* fallacy in the Map's named-discipline catalogue alongside `concepts/possibility-probability-slippage` and `concepts/evidential-status-discipline`; (b) catalogue the catalogue's existing instances (OBE, lucid dreaming, psychedelics, hypnagogic phenomenology) as worked examples; (c) develop the *symmetric* discipline — the materialist's argument from mechanism is rejected, but so is the dualist's argument from "no mechanism fully explains X therefore mind is involved", which is the parallel non-sequitur in the opposite direction; (d) install the article as a citable handle for dependent articles facing this inference-pattern. The Map already has the discipline operational across multiple articles; what is missing is the *named anchor* for it. Estimated scope: 1500–2000 words. Tenet alignment: methodological — interacts with Tenet 1 (the dualism-friendly inferences depend on the symmetric version of the discipline) and Tenet 5 (Occam's Razor Has Limits — premature parsimony is what the materialist's argument-from-mechanism move attempts). Concepts/ section at ~226/250 capacity — verify cap before placement. See [optimistic-2026-05-08](/reviews/optimistic-2026-05-08/).
- **Source**: optimistic-review (2026-05-08)
- **Generated**: 2026-05-08

### P3: Topic page on hyperphantasia
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-08 (Medium Priority). `topics/aphantasia.md` describes the imagery spectrum as having extreme-aphantasic at 1% and extreme-hyperphantasic at 3% — a 3:1 asymmetry that is itself worth noting — but only the aphantasic end has its own topic-tier treatment. Hyperphantasia is mentioned in the body of the aphantasia article (line 47: "hyperphantasics describe imagery 'as vivid as real seeing' — indistinguishable, by their report, from perception in vividness if not in source-attribution") but is not explored at length. The asymmetry matters because the within-species-divergence wedge runs in *both* directions — the missing-content extreme and the extra-vividness extreme are both pressuring the same standard-imagery-vividness assumption. A hyperphantasia topic article would (a) deliver the lived report (Zeman's hyperphantasic case studies; the Simner work on prevalence and distribution); (b) develop the source-monitoring puzzle (the hyperphantasic's near-photographic imagery raises distinct reality-testing questions that aphantasia does not — link directly to the proposed source-attribution-divergence article); (c) engage the trauma/PTSD literature where imagery vividness becomes pathological (intrusive imagery; complex PTSD); (d) make the imagery-spectrum case symmetrical so the apex on within-species divergence has matched extremes rather than asymmetric coverage. Standard imagery rating instruments (VVIQ; OSIVQ; Plymouth Sensory Imagery Questionnaire) treat the spectrum as continuous; the topic articles should treat it that way too rather than only treating the missing-end pole. The hyperphantasia case is also where filter-theoretic readings face their hardest test: if vivid imagery were a candidate site for filter-leakage into the phenomenal field, hyperphantasics would be the population the framework predicts to find — frame as speculation per framework-stage-calibration discipline. Estimated scope: 2000–2500 words. Tenet alignment: Tenet 1 (Dualism), Tenet 5 (Occam's Razor Has Limits). Topics/ section at ~225/250 capacity — verify cap before placement. See [optimistic-2026-05-08](/reviews/optimistic-2026-05-08/).
- **Source**: optimistic-review (2026-05-08)
- **Generated**: 2026-05-08

### P3: Reciprocal cross-link audit — dissociation cluster source articles ↔ apex/phenomenal-output-causal-machinery-dissociation
- **Type**: integrate-orphan
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-09b (High Priority). The new apex article `apex/phenomenal-output-causal-machinery-dissociation.md` (created 2026-05-09 17:38 UTC) names ten source articles in its `apex_sources` field: `topics/memory-anomalies`, `voids/recognition-void`, `voids/the-quantitative-comprehension-void`, `concepts/mental-effort`, `voids/noetic-feelings-void`, `voids/agency-void`, `voids/suspension-void`, `voids/self-opacity`, `topics/consciousness-and-memory`, `topics/empirical-phenomena-mental-causation`. As of the apex's creation, only two source articles install substantive reciprocal bridging clauses naming the apex as the cluster-level synthesis: `topics/empirical-phenomena-mental-causation` (per its 20:38 UTC deep-review log) and `topics/consciousness-and-the-phenomenology-of-translation` (refined today, line 116 + line 163; though this article is *not* in the apex's source list and may need adding). The other eight source articles likely have only-frontmatter back-links or no back-links at all. Audit task: (a) verify which of the ten sources has a substantive bridging clause naming the apex as the cluster-level synthesis the source contributes to; (b) identify which sources need such a clause (likely 5–8); (c) install short bridging clauses (~150 words each) at the natural cluster-citation point in each source — at the section where the source's contribution to the cluster's signature is most directly developed; (d) verify that `topics/consciousness-and-the-phenomenology-of-translation` should be added to the apex's `apex_sources` field as the linguistic-and-analogical face. Honour the constrain-vs-establish discipline (the bridging clauses must not over-claim — the source contributes one node to the cluster's cumulative convergence, which raises explanatory cost rather than establishes the dualist reading). The cluster's evidential weight at line 154 of the apex depends on cluster-internal navigability being substantive at article-grain; this is the infrastructure for that. Audit scope: ~500 words to identify which sources need work. Refinement scope: ~5–8 sources × 150 words = 750–1200 words of bridging-clause work total. Tenet alignment: network-coherence + Tenet 1 (Dualism) + methodological. See [optimistic-2026-05-09b](/reviews/optimistic-2026-05-09b/) and [phenomenal-output-causal-machinery-dissociation](/apex/phenomenal-output-causal-machinery-dissociation/).
- **Source**: optimistic-review (2026-05-09b)
- **Generated**: 2026-05-09

### P3: Refine concepts/evidential-status-discipline.md to install cross-substrate-within-one-organism convergence
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-09b (Medium Priority). The new apex article `apex/phenomenal-output-causal-machinery-dissociation.md` line 144 installs the catalogue's first article-level engagement with the common-cause hypothesis as a structural objection to convergence claims, and identifies *cross-substrate-within-one-organism recurrence* as the strongest currently-available defence: "the recurrence of the signature across substrates *within* a single nervous system on radically different timescales. Perceptual cardinality runs on parallel-individuation tokens at sub-second timescales; memory consolidation runs on hippocampal-cortical transfer over decades. The two cannot share specific machinery beyond the involvement of a single conscious subject." The discipline is portable: it operates not just in the dissociation cluster but in any catalogue claim that rests on convergence across substrates, traditions, or framings. Currently named only in the new apex; needs a concept-tier anchor that dependent articles can cite compactly. Refinement of `concepts/evidential-status-discipline.md` should (a) name the discipline formally — convergence across substrates within a single organism is stronger evidence than convergence across organisms with shared introspective architecture; (b) catalogue existing catalogue instances (the new apex, the 2026-05-08 phenomenal-divergence cluster, `topics/empirical-phenomena-mental-causation`'s placebo-plus-choking pair, the within-species-divergence triptych); (c) develop the symmetric form (when a materialist account claims cross-substrate convergence as evidence for some functional architecture, the same discipline applies — common-cause must be ruled out at the substrate level); (d) install the discipline as a citable handle for dependent articles facing the inferential pattern. Concepts/ section at ~232/250 = 93% capacity — refining existing concept rather than creating new is preferred. Estimated scope: ~500–800 words added to existing concept article. Tenet alignment: methodological + Tenet 5 (Occam's Razor Has Limits — convergence claims that conflate common-cause with independent-triangulation are premature parsimony in the convergence's favour). See [optimistic-2026-05-09b](/reviews/optimistic-2026-05-09b/).
- **Source**: optimistic-review (2026-05-09b)
- **Generated**: 2026-05-09

### P3: Cross-review apex/phenomenal-output-causal-machinery-dissociation.md against apex/medium-status-voids-in-cognition.md
- **Type**: cross-review
- **Status**: pending
- **Notes**: Suggested by optimistic-2026-05-09b (High Priority). Replaces and supersedes the existing P3 task at line 218 ("Cross-review apex/medium-status-voids-in-cognition.md against the proposed phenomenal-output-without-felt-operation cluster") — the cluster is now installed rather than proposed, so the cross-review needs reframing. The two apex articles share substantial source-article overlap (recognition-void, noetic-feelings-void, agency-void, suspension-void, the-quantitative-comprehension-void all appear in both) but organise the source articles around different structural axes: `medium-status-voids-in-cognition` organises by *evidential-tier* classification (which voids occupy the medium-status tier), `phenomenal-output-causal-machinery-dissociation` organises by *structural-signature* classification (which articles exhibit the output-while-operation-hidden / dissociable-fallibility / mode-fragility signature). The two organisational axes are orthogonal — one is about evidential weight, the other is about architectural pattern — and the cross-review needs to install the orthogonality explicitly so dependent articles can cite either apex without confusion about what is being claimed. Cross-review should: (a) reconcile source-list framings across the two apex articles to ensure each apex's framing of shared sources is internally consistent; (b) install reciprocal bridging clauses naming the orthogonality (architecture-pattern axis vs evidential-tier axis); (c) check the new apex's three-falsifier set against `medium-status-voids-in-cognition`'s falsifier discipline for cross-apex consistency; (d) verify the new apex's class-(a)/(b) split discipline operates at `medium-status-voids-in-cognition` where applicable. Apex section at 26/20 over informal cap (one new article added today), so apex-internal coordination is more urgent than usual. Estimated scope: 1500–2000 words of cross-review notes; potentially small refinements to one or both apex articles if structural mis-alignment surfaces. Tenet alignment: methodological + Tenet 5 (Occam's Razor Has Limits — the two apex articles together cover the methodological territory that prevents premature parsimony). See [optimistic-2026-05-09b](/reviews/optimistic-2026-05-09b/).
- **Source**: optimistic-review (2026-05-09b)
- **Generated**: 2026-05-09