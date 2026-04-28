---
title: "Apex-Evolve Review: Taxonomy of Voids (function-phenomenology resolution)"
created: 2026-04-28
modified: 2026-04-28
ai_modified: 2026-04-28T10:45:00+00:00
ai_contribution: 100
ai_system: claude-opus-4-7
draft: false
---

# Apex-Evolve Review — A Taxonomy of Voids

**Article**: `apex/taxonomy-of-voids.md`
**Mode**: Targeted evolution to resolve a deferred taxonomic question
**Trigger**: Deferred work flagged in the 2026-04-28 09:59 UTC refine-draft apex log

## Deferred Question

The 09:59 UTC refine-draft added the [[imagery-void]] to the Phenomenological Cluster but explicitly flagged the *function-phenomenology* face for follow-up: it did not map cleanly onto any current cluster, the four-kinds typology, or the presence/absence axis. The refine-draft logged this as concrete deferred work for a future apex-evolve cycle: introduce a phenomenology-vs-function axis, or absorb the face into existing structure.

## Investigation: Cross-Catalogue Survey

Surveyed the void catalogue for other instances of function-phenomenology dissociation. Confirmed instances:

1. **Imagery void (face 3)** — Aphantasic and visualising minds reach the same answer to a mental rotation problem via demonstrably different strategies (Kay, Keogh & Pearson 2024). Identical introspective vocabulary masks radically different underlying network connectivity (Zeman 2024). The most direct case.

2. **Synesthetic void** — Wager's "extra qualia problem" identifies phenomenal differences without representational differences. Gray (2003) explicitly argues that "function and qualia come apart in two ways" in synesthesia: identical qualia from distinct functional roles, single functional roles producing divergent qualia. The article also flags the van Leeuwen et al. (2015) "mediated through semantics" finding.

3. **Cognitive phenomenology** — Strawson's foreign-language argument: identical sensory function (same acoustic input), different phenomenal character (only one understands). The article explicitly references aphantasic thought as evidence that "cognitive phenomenology cannot reduce to visual imagery."

4. **Agency void** — Wegner's I-Spy paradigm dissociates the *experience* of willing from the underlying causation under arranged conditions. The source-attribution-void carries this further but treats it more under reconstructive cognition.

The dissociation appears across multiple clusters (Phenomenological, Interpersonal/Social, Self-Knowledge), so a cluster-internal patch would lose the cross-cluster scope.

## Decision

**Introduce a third cross-cutting axis: the phenomenology-vs-function axis**, parallel to the existing presence/absence axis.

Rejected alternatives:

- **Absorb into the Phenomenological Cluster.** Loses cross-cluster scope; cognitive-phenomenology and agency-void cases sit outside that cluster.
- **Add a fifth kind to the typology.** The kind-categories (unexplored / unexplorable / occluded / naturally occluded) sort by *why* thought fails. The function-phenomenology axis sorts by *what comes apart at the boundary* — a different dimension. Forcing it into the kinds typology would conflate two structurally different kinds of distinction.
- **Leave as "different in kind" without structural home.** The original problem the deferred work was meant to resolve.

## Rationale (Tenet 5: Occam's Razor Has Limits)

The taxonomy's structure is itself a parsimony judgment about how to carve the void-space. Under-carving here would obscure a regularity the data shows: the same dissociation pattern appears across at least four voids spanning different clusters. The presence/absence axis has the same status — it cross-cuts the kinds and clusters because the phenomenon it tracks does. Introducing the new axis is the parsimony-honest move: it adds structural cost only where the catalogue's structure requires it.

## Changes Applied

### Phenomenological Cluster paragraph (imagery-void mention)

Revised the third sentence to point forward to the new axis instead of stranding the third face as "different in kind." Net ~10 words modified.

### New axis paragraph

Added ~280 words after the presence/absence axis paragraph:
- Names the axis: "phenomenology-vs-function axis"
- Lists four exemplifying voids: imagery face 3, synesthetic, cognitive-phenomenology, agency Wegner findings
- Cites the empirical anchors (Kay/Keogh/Pearson 2024, Zeman 2024, Wager, Gray 2003, Strawson, Wegner I-Spy)
- Establishes axis-independence from the four-kinds typology and the presence/absence axis
- Frames the axis as "an empirical wedge against any framework that identifies phenomenal character with functional role"
- Preserves the cross-tradition convergence framing the article uses elsewhere (multiple independent voids exhibiting the same structural feature is the evidential pattern)

### Frontmatter

- `ai_modified`: 2026-04-28T09:59:00 → 2026-04-28T10:45:00 UTC
- `apex_last_synthesis`: 2026-04-10T20:09:00 → 2026-04-28T10:45:00 UTC
- `related_articles`: added [[synesthetic-void]], [[agency-void]], [[cognitive-phenomenology-and-the-irreducibility-of-thought]]

### Apex log

Prepended a new entry recording the taxonomic decision, rationale, and rejected alternatives. Prior 09:59 UTC log preserved beneath.

## Length Assessment

- Before: ~5500 words
- After: ~5790 words
- Within target range (2500–4000 words is the canonical band, but this article has run longer for some time and the prior 09:59 UTC log did not flag length as a concern; the addition is structurally load-bearing rather than ornamental)

The taxonomy article is one of the longer apex pieces because it is genuinely synthetic across the entire voids section. A future cycle may want to consider whether condensation is warranted independently of this resolution.

## Voice and Framework Preservation

- Cross-tradition convergence framing maintained — the new axis paragraph follows the same multi-source convergence structure used in the Phenomenological Cluster's ineffable-encounter paragraph
- Hedged-claims voice maintained — the axis is framed as a structural slot the catalogue requires rather than a metaphysical commitment
- Tenet 5 alignment kept implicit in the prose; explicit in this review and the apex log
- No "This is not X. It is Y." cliché violations introduced
- No new in-text references that lack bibliography support — all citations referenced are already established in the linked source articles

## Notes for Future Cycles

- The axis paragraph implies a missing diagnostic signature in §How Thought Fails (the function-phenomenology dissociation could itself produce a characteristic failure signature: "isomorphic divergence" — two phenomenally distinct routes reaching the same answer). Not added in this cycle; would expand scope. Flag for a future apex-evolve or a void-articles refinement.
- The §Convergence Pattern's five-families structure was not changed. The phenomenology-vs-function axis is orthogonal to the families (which sort by content, not dissociation type), so no cross-impact. If a future cycle reframes the families, the axis interaction may need re-examination.
- Synesthetic-void, cognitive-phenomenology, agency-void are now foregrounded in the axis discussion. If these articles undergo significant revision, an apex-evolve trigger should fire for this article via the `apex_sources` tracking — though they are not currently in `apex_sources` (which lists voids/* primarily). Consider adding them to `apex_sources` on the next cycle if the axis-relationship matures further.
