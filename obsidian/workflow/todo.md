---
ai_contribution: 100
ai_generated_date: 2026-01-05
ai_modified: 2026-02-06 19:39:00+00:00
ai_system: claude-opus-4-5-20251101
author: Andy Southgate
concepts: []
created: 2026-01-05
draft: false
human_modified: 2026-01-23 15:29:26+00:00
last_curated: null
modified: 2026-01-25
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

### P2: Update wikilinks to archived articles (interface-locality, brain-specialness, and 5 others)
- **Type**: other
- **Notes**: Gap analysis found 70+ broken wikilinks pointing to archived/coalesced articles. Key targets: interface-locality (34 refs, archived to concepts/), brain-specialness (6 refs), consciousness-and-quantum-measurement (11 refs), nihilism (5 refs), quantum-measurement-and-definite-outcomes (5 refs), eastern-philosophy-haecceity-tension (4 refs), meaning-and-consciousness (4 refs). Update wikilinks to point to the replacement articles these were coalesced into, or verify the archive redirect handles them.
- **Source**: gap_analysis
- **Generated**: 2026-02-06

### P2: Fix case-sensitivity wikilink errors across content
- **Type**: other
- **Notes**: Gap analysis found 68 case-sensitivity wikilink errors where capitalized forms like [[Access consciousness]], [[Blindsight]], [[Filter-theory]], [[Qualia]] are used instead of lowercase-hyphenated forms. Most concentrated in concepts/ section (255 occurrences). Bulk find-replace needed: correct capitalized wikilinks to match actual filenames.
- **Source**: gap_analysis
- **Generated**: 2026-02-06

### P2: Strengthen Minimal Quantum Interaction cross-references
- **Type**: other
- **Notes**: Gap analysis found Minimal Quantum Interaction is the weakest-represented tenet (184 files vs 301 for Dualism, 61% ratio). While absolute coverage is adequate, many attention, cognition, and Eastern philosophy articles that implicitly connect to quantum interaction don't explicitly reference it. Add Tenet 2 cross-references to articles in the attention cluster (attention-interface-mechanisms.md, voluntary-attention.md), biological articles (evolution-of-consciousness.md, neural-quantum-coherence.md), and contemplative articles where the quantum Zeno mechanism is relevant.
- **Source**: gap_analysis
- **Generated**: 2026-02-06

### P2: Update references to coalesced substrate-independence-critique article
- **Type**: other
- **Notes**: Coalesce (2026-02-02) merged `substrate-independence-critique.md` into `substrate-independence.md`. 20+ files in obsidian/ reference the archived article via `[[substrate-independence-critique]]`. Key files: functionalism.md, llm-consciousness.md, continual-learning-argument.md, embodied-cognition.md, ai-consciousness.md, machine-consciousness.md, hard-problem-of-consciousness.md, machine-question.md. Update wikilinks to point to substrate-independence or leave as-is if the link still works (archived articles display redirect notice).
- **Source**: coalesce
- **Generated**: 2026-02-02

### ✓ 2026-02-07: Address confidence-uncertainty mismatch in foundational articles
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-05) found pattern across simulation.md, knowledge-argument.md, and ethics-of-consciousness.md: strong claims in main text, uncertainty acknowledgments buried in caveats or "What Would Challenge" sections. Creates misleading impression. Need to integrate conditional language into main claims: "If the simulation hypothesis is coherent, it would suggest..." rather than "The simulation hypothesis dissolves..." Also: knowledge-argument treats intuition as near-probative without engaging methodological debates; ethics article's AI consciousness conclusions rest heavily on contested framework. See pessimistic-2026-02-05.md
- **Source**: pessimistic-review
- **Generated**: 2026-02-05
- **Output**: obsidian/concepts/simulation.md, obsidian/concepts/knowledge-argument.md, obsidian/topics/ethics-of-consciousness.md

### P3: Write article on consciousness-evolution problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-01 (night). How could non-physical consciousness evolve through natural selection if it influences physical outcomes? The site alludes to this but hasn't treated it systematically. If consciousness is causally efficacious (Bidirectional Interaction), evolution could select for it; needs explicit treatment. Builds on evolution-of-consciousness.md, tenets.md.
- **Source**: optimistic-review
- **Generated**: 2026-02-01

### P3: Write article on Princess Elizabeth's challenge (historical deep dive)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-01 (night). The famous objection has contemporary responses; historical treatment would show evolution of the debate and why quantum mechanics changes the terms. Directly supports Minimal Quantum Interaction by showing how Descartes couldn't answer what we now can. Builds on interactionist-dualism.md, conservation-laws-and-mind.md.
- **Source**: optimistic-review
- **Generated**: 2026-02-01

### P3: Write article on embodied consciousness and the interface
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-01 (night). How does the filter/interface model accommodate embodied cognition insights? The body shapes consciousness—is this compatible with dualism? Shows dualism can accommodate embodied insights without reducing to them. Builds on embodied-cognition.md, attention-as-interface.md, filter-theory.md.
- **Source**: optimistic-review
- **Generated**: 2026-02-01

### P3: Write article comparing quantum consciousness mechanisms
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02. Systematic comparative table of quantum consciousness mechanisms (Orch OR, Stapp, Fisher) on key dimensions: decoherence timescales, energy requirements, testability, biological plausibility, philosophical consequences. Recent evidence (Wiest et al. 2024, Atkins et al. 2025) challenges older calculations. Would strengthen scientific rigor of Minimal Quantum Interaction tenet. Builds on quantum-consciousness.md, stapp-quantum-mind.md, neural-quantum-coherence.md.
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on contemplative verification of consciousness theories
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02. Develop detailed predictions about what meditation *should* reveal if various consciousness theories are true. If Stapp is right about quantum Zeno, what should meditators report about attention's effort structure? If consciousness is irreducible, what should happen to phenomenal access under sustained attention? Compare predictions to actual contemplative reports. Builds on contemplative-evidence-for-consciousness-theories.md, phenomenological-evidence-methodology.md, witness-consciousness.md.
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on phenomenology of anticipation (protention)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (morning). Protention—the forward-directed aspect of experience—receives less attention than retention. How does anticipation differ phenomenologically from prediction? How does it relate to free will (anticipating one's own choices)? Builds on temporal-consciousness.md, phenomenology-of-understanding.md, specious-present.md.
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on dream consciousness and the filter model
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (morning). Dreams demonstrate consciousness without external input—experience generated purely internally. What does this show about the consciousness-brain relationship? Dreams as evidence against the brain-as-generator model. Builds on dreams-and-consciousness.md, hard-problem-of-consciousness.md, filter-theory.md.
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Create concept page for prehension
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (morning). Whitehead's term for experiential grasping appears in multiple articles (binding-problem.md, temporal-consciousness.md, phenomenology-of-understanding.md) but deserves dedicated treatment. Central to process philosophy's account of experience.
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on phenomenal conservatism and introspective evidence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). Huemer's phenomenal conservatism—if it seems to S that P, S has prima facie justification for believing P—is foundational for treating phenomenal evidence seriously. How does the Map handle introspective reliability? When should phenomenal seemings be trusted? Builds on arguments-for-dualism.md, epistemic-advantages-of-dualism.md, introspection.md. See optimistic-2026-02-02-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on neural bandwidth constraints and the interface
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). The bandwidth response to decoherence (consciousness operates at ~40 bits/sec policy level) deserves dedicated treatment. What does slow conscious bandwidth mean for fast quantum processes? How does information get compressed? Builds on attention-interface-mechanisms.md, quantum-consciousness.md, voluntary-attention.md. See optimistic-2026-02-02-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on phenomenology of agency vs passivity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). Tension between active attention (Stapp's quantum Zeno) and passive witnessing (contemplative traditions). Both phenomenologically real. When does consciousness act vs merely witness? How do these modes relate? Builds on phenomenology-of-understanding.md, mental-effort.md, witness-consciousness.md. See optimistic-2026-02-02-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Create concept page for cognitive phenomenology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). The thesis that thinking itself has phenomenal character—not just accompanying sensations. Currently mentioned throughout but not given dedicated analysis. Central to extending hard problem beyond sensory qualia. See optimistic-2026-02-02-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on phenomenology of belief change
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02. What is it like to change one's mind? The moment of belief revision has distinctive phenomenology—the "giving way" of an old view, the "clicking into place" of a new one. Connects to consciousness's role in rationality and the argument from reason. Builds on epistemic-emotions.md, phenomenology-of-error-recognition.md, argument-from-reason.md. See optimistic-2026-02-02.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on the interface location problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02. Where exactly does consciousness interface with the brain? Multiple candidate sites exist (microtubules, dendritic integration zones, cortical columns). Systematic comparison article evaluating evidence for each and explaining why the Map remains agnostic about specifics. Builds on attention-interface-mechanisms.md, brain-interface-boundary.md, quantum-consciousness.md. See optimistic-2026-02-02.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on consciousness and surprise
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02. Phenomenology of surprise—violated expectations producing distinctive experiential quality—provides window into how consciousness interacts with predictive processing. If surprise is phenomenally real and causally efficacious (triggering learning, memory consolidation), supports Bidirectional Interaction. Builds on predictive-processing.md, phenomenology-of-understanding.md, epistemic-emotions.md. See optimistic-2026-02-02.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on phenomenology of pain
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (midday). Pain's structure (protensional quality, apparent localisation, resistance to functionalism) deserves dedicated phenomenological treatment. Distinguishes from other negative states; grounds ethical commitments in irreducible phenomenal reality. Builds on qualia.md, emotional-consciousness.md. See optimistic-2026-02-02-midday.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on weak vs. strong emergence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (midday). Systematic distinction between epistemological emergence (reducible in principle) and ontological emergence (irreducible). Explains why consciousness requires strong emergence and why "complexity" arguments fail. Builds on consciousness.md, reductionism.md. See optimistic-2026-02-02-midday.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on diachronic agency and personal narrative
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (midday). How agents author futures through memory, intention, and anticipatory consciousness. The temporal dimension of agency integrates Bidirectional Interaction with No Many Worlds (why *this* continuation matters). Builds on personal-identity.md, free-will.md, temporal-consciousness.md. See optimistic-2026-02-02-midday.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on consciousness and mathematical creativity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). How mathematical insight demonstrates consciousness's irreducibility. Gödel's incompleteness and Penrose's arguments. Mathematical understanding involves grasping *why* proofs work—not just verifying steps. Builds on consciousness-and-mathematical-understanding.md, consciousness-and-intelligence.md, baseline-cognition.md. See optimistic-2026-02-02-afternoon-2.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on phenomenology of deliberation under uncertainty
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). What it's like to decide when outcomes are uncertain. The felt structure of weighing probabilities, accepting risk, committing despite incomplete information. Builds on phenomenology-of-choice.md, epistemic-emotions.md, free-will.md. See optimistic-2026-02-02-afternoon-2.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on consciousness and the ownership problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). What makes experiences *mine*? The ownership relation between consciousness and its contents. Depersonalization disorders where ownership fails while consciousness persists. Builds on vertiginous-question.md, haecceity.md, personal-identity.md. See optimistic-2026-02-02-afternoon-2.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on the incubation effect and unconscious processing
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). Incubation in creative problem-solving—solutions emerge after conscious effort is suspended. What this reveals about consciousness-unconscious relations. Builds on consciousness-and-creativity.md, baseline-cognition.md, working-memory.md. See optimistic-2026-02-02-afternoon-2.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on phenomenology of flow states
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). Flow as the opposite of choking—effortless excellence when consciousness is absorbed rather than monitoring. What flow phenomenology reveals about the consciousness-automaticity interface. Builds on choking-phenomenon-mental-causation.md, implicit-memory.md, attention-as-interface.md. See optimistic-2026-02-02-afternoon-2.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Create concept page for process haecceitism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). The resolution from eastern-philosophy-haecceity-tension.md that thisness can apply to experiential processes, not just substantial selves. Philosophically innovative and relevant to Buddhist-dualist compatibility. See optimistic-2026-02-02-afternoon-2.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Create concept page for the timing gap problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). The persistent challenge of connecting millisecond attention to femtosecond quantum processes. Currently scattered across articles; deserves unified treatment examining the gap, proposed resolutions, and remaining challenges. See optimistic-2026-02-02-afternoon-2.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Create concept page for contemplative epistemology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (afternoon). How first-person methods can generate knowledge. Methodological foundation for the Map's use of phenomenological evidence across multiple articles. See optimistic-2026-02-02-afternoon-2.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on phenomenology of surprise and prediction error
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (evening). How the felt quality of surprise relates to prediction error. If surprise triggers learning and is phenomenally real, consciousness does causal work. Builds on predictive-processing.md, phenomenology-of-understanding.md, epistemic-emotions.md. See optimistic-2026-02-02-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on modal structure of phenomenal properties
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (evening). Why phenomenal properties are conceivably absent (zombies) or inverted when physical properties aren't. Kripke's necessary a posteriori argument for identity and why it stumbles on phenomenal properties. Builds on qualia.md, philosophical-zombies.md, knowledge-argument.md. See optimistic-2026-02-02-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on phenomenology of returning attention
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (evening). What happens phenomenologically when attention wanders and returns? The "moment of return" has distinctive phenomenal character. Prime territory for attention-as-interface hypothesis. Builds on voluntary-attention.md, mental-effort.md, meditation-and-consciousness-modes.md. See optimistic-2026-02-02-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### ✓ 2026-02-09: Create concept page for phenomenal transparency
- **Type**: expand-topic
- **Status**: complete (duplicate of earlier task)
- **Notes**: Suggested by optimistic review 2026-02-02 (evening). The property that experience seems to be directly about the world. Mentioned in several articles but not defined. Relevant to why naive realism seems intuitive. See optimistic-2026-02-02-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02
- **Output**: [[phenomenal-transparency]]

### P3: Create concept page for conceivability-possibility inference
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-02 (evening). The logical move from "conceivable" to "possible" that grounds zombie and knowledge arguments. Currently discussed in context but deserves systematic treatment. See optimistic-2026-02-02-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-02

### P3: Write article on consciousness and causal powers
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-03. The metaphysics of how substances exercise causal powers—what it means for consciousness to "cause" in a non-Humean sense. Directly supports Bidirectional Interaction by explaining the metaphysical framework for mental causation. Builds on agent-causation.md, mental-causation.md, free-will.md. See optimistic-2026-02-03.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03

### P3: Write article on the phenomenology of moral experience
- **Type**: expand-topic
- **Status**: done
- **Notes**: Suggested by optimistic review 2026-02-03. What it is like to experience something as wrong or obligatory—the phenomenology underlying moral judgment. Supports Dualism by showing moral phenomenology has irreducible features. Builds on phenomenal-value-realism.md, ethics-of-consciousness.md, emotional-consciousness.md. See optimistic-2026-02-03.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03
- **Output**: obsidian/topics/phenomenology-of-moral-experience.md

### P3: Write article on cognitive integration and the self
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-03. How the self integrates information across time and modality—the "glue" of personal identity. Supports No Many Worlds—indexical identity requires unified self. Builds on personal-identity.md, binding-problem.md, self-and-consciousness.md. See optimistic-2026-02-03.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03

### P3: Create concept page for causal powers
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-03. The metaphysics of how substances exercise causation—needed for the agent-causation framework. Builds on agent-causation.md, mental-causation.md, substance-causation.md. See optimistic-2026-02-03.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03

### P3: Create concept page for phenomenal normativity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-03. How experiential states carry normative significance intrinsically—grounds phenomenal value realism. Builds on phenomenal-value-realism.md, qualia.md, ethics-of-consciousness.md. See optimistic-2026-02-03.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03

### P3: Write article on contemplative training and phenomenal access
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-03 (afternoon). How meditation training improves introspective accuracy, changes neural signatures, and reveals consciousness structure—providing evidence against illusionism (illusions don't deepen with practice). Builds on contemplative-neuroscience-integration.md, witness-consciousness.md, meditation-and-consciousness-modes.md. See optimistic-2026-02-03-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03

### P3: Write article on the growing block universe and consciousness
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-03 (afternoon). If consciousness constitutes time's arrow through collapse, develop this framework fully—consciousness as temporal-constitutive rather than merely temporal-aware. Addresses "why consciousness exists at all" by tying it to temporal emergence. Builds on time-consciousness-growing-block.md, collapse-and-time.md, retrocausality.md. See optimistic-2026-02-03-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03

### P3: Write article on disorders of consciousness as test cases
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-03 (afternoon). How the Map's framework handles minimally conscious state, vegetative state, locked-in syndrome—cases where consciousness presence is uncertain. Tests framework against hard cases; has implications for ethics of consciousness. Builds on loss-of-consciousness.md, minimal-consciousness.md, consciousness-in-simple-organisms.md. See optimistic-2026-02-03-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03

### P3: Write article on phenomenology of epistemic achievement
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-03 (evening). What it's like to *grasp* something—the "click" of understanding, the "settling" of conviction. This phenomenology supports the argument from reason: genuine understanding involves normative relations that physical causation alone cannot instantiate. Builds on phenomenology-of-understanding.md, cognitive-phenomenology.md, epistemic-emotions.md. See optimistic-2026-02-03-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03

### P3: Write article on introspection rehabilitation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-03 (evening). The process/content distinction—we're unreliable about *why* we choose but reliable about *what* we experience. Fox et al. (2012) found meditation training improves introspective accuracy, suggesting introspection is a skill. Defends phenomenological evidence against illusionism's reliance on introspective unreliability. Builds on introspection.md, contemplative-evidence-for-consciousness-theories.md, witness-consciousness.md. See optimistic-2026-02-03-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03

### P3: Write article on evolution under dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-03 (evening). If consciousness is irreducible, how does evolution select for it? The amplifier framework answers: evolution selects for cognitive capacities (metarepresentation, counterfactual reasoning, cumulative culture) that consciousness enables. Addresses "why would evolution produce non-physical minds?" objection. Builds on evolution-of-consciousness.md, baseline-cognition.md, consciousness-as-amplifier.md. See optimistic-2026-02-03-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-03

### P3: Write article on consciousness and scientific methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04. If consciousness is irreducible and causally efficacious, what does this mean for scientific methodology? Can the scientific method fully investigate consciousness, or do we need methodological pluralism? Explores the implications of the Map's framework for how consciousness should be studied. Builds on first-person-third-person-methodology.md, neurophenomenology.md, contemplative-evidence-for-consciousness-theories.md. See optimistic-2026-02-04.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Write article on social construction of self vs phenomenal self
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04. The minimal self is phenomenal; the narrative self is constructed. How do these interact? Can social construction affect phenomenal properties, or only narrative overlay? Explores relationship between irreducible phenomenal core and socially-shaped identity. Builds on self-and-consciousness.md, intersubjectivity.md, witness-consciousness.md. See optimistic-2026-02-04.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Create concept page for moral perception
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04. The phenomenology of perceiving value—currently scattered across several articles but deserves focused treatment. Connects phenomenal-value-realism to actual experience. What is it *like* to perceive something as wrong? How does moral perception differ from aesthetic perception? Builds on phenomenal-value-realism.md, consciousness-value-connection.md, ethics-of-consciousness.md. See optimistic-2026-02-04.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Create concept page for methodological pluralism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04. The view that consciousness requires multiple methods (first-person, second-person, third-person) working together. Referenced in neurophenomenology but not systematically defined. Foundational for the Map's treatment of contemplative evidence as genuine data. Builds on neurophenomenology.md, first-person-third-person-methodology.md, contemplative-evidence-for-consciousness-theories.md. See optimistic-2026-02-04.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Create concept page for phenomenal depth
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04. The sense that experience has different "depths"—surface attention vs absorbed engagement. Referenced in contemplative articles but not consolidated. Meditators report that meaning correlates with depth of conscious engagement, not merely presence of consciousness. Builds on witness-consciousness.md, meditation-and-consciousness-modes.md, meaning-of-life.md. See optimistic-2026-02-04.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Create concept page for temporal unity
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04. Unity across time (diachronic unity) deserves focused treatment separate from synchronic binding. The specious present, retention-protention structure, and what binds moments into continuous experience. Builds on temporal-consciousness.md, varieties-of-unity.md, unity-of-consciousness.md. See optimistic-2026-02-04.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Write article on phenomenology of normative properties
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04 (evening). What is it *like* to grasp a reason as compelling? How does the phenomenology of "seeing" that a conclusion follows differ from mere association? The Map argues normative properties are irreducible; this develops the phenomenological dimension of that claim. Builds on argument-from-reason.md, phenomenal-value-realism.md, consciousness-value-connection.md. See optimistic-2026-02-04-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Write article on contemplative methods as philosophical methodology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04 (evening). What is the epistemic status of contemplative evidence? How do trained meditators differ from naive introspectors? Can we develop reliability criteria for first-person reports? Grounds the Map's use of phenomenological evidence systematically. Builds on contemplative-evidence-for-consciousness-theories.md, neurophenomenology.md, phenomenological-evidence.md. See optimistic-2026-02-04-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Write article on consciousness and strong emergence
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04 (evening). The Map critiques emergence as consciousness explanation but could develop what kind of emergence, if any, is compatible with irreducibility. Strong emergence (novel causal powers) vs weak emergence (epistemological only). Why consciousness requires the former. Builds on emergence.md, downward-causation.md, reductionism.md. See optimistic-2026-02-04-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Create concept page for normative phenomenology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04 (evening). The study of what it's like to experience reasons, values, and oughts. Currently scattered across argument-from-reason.md and phenomenal-value-realism.md but deserves consolidation. Central to the Map's case that consciousness grounds normativity. See optimistic-2026-02-04-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Create concept page for contemplative reliability
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04 (evening). Criteria for when contemplative reports are epistemically trustworthy. Referenced in several articles but not systematically treated. Foundational for treating first-person evidence as genuine philosophical data. See optimistic-2026-02-04-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Create concept page for self-stultification
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-04 (evening). The logical structure whereby a position undermines itself if true. Appears in argument-from-reason.md (physicalism undermines rational belief), mental-causation.md (epiphenomenalism undermines knowledge of consciousness). Deserves focused treatment as recurring argumentative structure. See optimistic-2026-02-04-evening.md
- **Source**: optimistic-review
- **Generated**: 2026-02-04

### P3: Write article on phenomenology of memory and the self
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-05. How memory contributes to the sense of continuous selfhood; the tension between Buddhist impermanence and the phenomenology of personal persistence; what "I" refers to if no permanent substance underlies memory. Builds on temporal-consciousness.md, personal-identity.md, episodic-memory.md. See optimistic-2026-02-05.md
- **Source**: optimistic-review
- **Generated**: 2026-02-05

### P3: Write article on consciousness and probability interpretation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-05. If consciousness participates in collapse, what is the ontological status of quantum probabilities? Are they subjective (QBism), objective (propensities), or something new (the structure of the consciousness-physics interface)? Builds on consciousness-and-quantum-measurement.md, quantum-probability-consciousness.md. See optimistic-2026-02-05.md
- **Source**: optimistic-review
- **Generated**: 2026-02-05

### P3: Write article on the phenomenology of moral experience
- **Type**: expand-topic
- **Status**: done
- **Notes**: Suggested by optimistic review 2026-02-05. What is it like to experience moral obligation, guilt, admiration? How does the phenomenology of moral experience support phenomenal value realism? Does moral phenomenology provide evidence for consciousness's irreducibility? Builds on moral-responsibility.md, phenomenal-value-realism.md, ethics-of-consciousness.md. See optimistic-2026-02-05.md
- **Source**: optimistic-review
- **Generated**: 2026-02-05
- **Output**: obsidian/topics/phenomenology-of-moral-experience.md

### P3: Create concept page for subjective aim
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-05. Whitehead's term appears in meaning-of-life.md but has no dedicated page. Could illuminate the Map's approach to value and purpose. See optimistic-2026-02-05.md
- **Source**: optimistic-review
- **Generated**: 2026-02-05

### P3: Create concept page for temporal thickness / specious present
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-05. Frequently referenced across consciousness articles but no dedicated treatment. Could integrate Husserl, James, and neuroscience on how consciousness extends through time. See optimistic-2026-02-05.md
- **Source**: optimistic-review
- **Generated**: 2026-02-05

### P3: Create concept page for spontaneous intentional action
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-05. The 2025 meta-analysis on conscious vs unconscious processing introduces this term. Could be developed into a concept page supporting the Map's view that consciousness initiates action. See optimistic-2026-02-05.md
- **Source**: optimistic-review
- **Generated**: 2026-02-05

### P3: Create concept page for intentionality
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-05 (afternoon). Intentionality (aboutness) is listed as one of seven convergent arguments for dualism but lacks dedicated treatment. Brentano's thesis, Searle's response to naturalistic accounts, and the connection to phenomenal consciousness deserve fuller development. Referenced in consciousness.md, arguments-for-dualism.md. See optimistic-2026-02-05-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-05

### P3: Create concept page for observational-closure
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-05 (afternoon). Saad's key concept from delegatory dualism (2025)—the claim that mental causation need not produce observable violations of physical patterns even if it's real. Distinct from causal closure. Important for understanding how interactionist dualism avoids empirical disconfirmation. See optimistic-2026-02-05-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-05

### P3: Write article on the binding problem (systematic treatment)
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-05 (afternoon). While mentioned in why-phenomenal-unity-resists-explanation.md, the binding problem deserves deeper dedicated treatment. Classical binding vs. phenomenal unity vs. quantum solutions (entanglement-based binding) could be clarified systematically. Supports Minimal Quantum Interaction tenet. See optimistic-2026-02-05-afternoon.md
- **Source**: optimistic-review
- **Generated**: 2026-02-05

### P3: Write topic on the measurement problem as philosophical problem
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-06. The measurement problem is referenced throughout (measurement-problem.md concept, quantum-interpretations.md, prebiotic-collapse.md) but deserves a dedicated topic-level treatment bringing out its philosophical dimensions—why it's not merely a physics puzzle but reveals something about the relationship between observation and reality. The structural parallel between the measurement problem and hard problem (both concerning where first-person facts enter third-person descriptions) deserves systematic development. Supports Minimal Quantum Interaction and No Many Worlds tenets. See optimistic-2026-02-06.md
- **Source**: optimistic-review
- **Generated**: 2026-02-06

### P3: Write topic on the hard problem in non-Western philosophy
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-06. How traditions outside Western analytic philosophy have grappled with the consciousness-matter relationship—Vedanta's chit-jada distinction, Buddhist vijñāna analysis, Islamic philosophy's nafs framework, and Chinese philosophy's xin-shen relationship. Cross-cultural convergence on irreducibility suggests it's not merely Western parochialism. Builds on eastern-philosophy-consciousness.md, buddhist-perspectives-on-meaning.md, contemplative-evidence.md. Supports Occam's Limits tenet. See optimistic-2026-02-06.md
- **Source**: optimistic-review
- **Generated**: 2026-02-06

### P3: Create concept page for atemporal causation
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review 2026-02-06. The time-symmetric selection mechanism depends on a concept of causation that isn't sequential. A dedicated treatment of how atemporal causation works, its precedents in physics (Wheeler-Feynman, Cramer, TSVF), and its philosophical implications would support both the free will and quantum measurement articles. Currently this concept does theoretical work in time-symmetric-selection-mechanism.md and free-will.md but lacks its own page. See optimistic-2026-02-06.md
- **Source**: optimistic-review
- **Generated**: 2026-02-06

### P3: Write apex article synthesising the attention cluster
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The attention cluster (attention-as-interface, attention-interface-mechanisms, voluntary-attention, structure-of-attention, attention-consciousness-dissociation, attention-motor-planning-quantum-interface) has grown to 6+ articles without a unifying apex synthesis. An apex article would show how attention serves as the Map's primary candidate for the consciousness-brain interface, connecting all five tenets. See optimistic-2026-02-08.md
- **Source**: optimistic-review
- **Generated**: 2026-02-08

### P3: Write article on consciousness and social cognition
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. How consciousness enables understanding of other minds—theory of mind, empathy, joint attention—and what this reveals about consciousness's nature. The baseline cognition work suggests great apes have limited theory of mind; exploring why could strengthen the Map's case for bidirectional interaction. See optimistic-2026-02-08.md
- **Source**: optimistic-review
- **Generated**: 2026-02-08

### P3: Create concept page for moral-phenomenology
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. The phenomenology-of-moral-experience article introduces moral perception, felt obligation, and moral admiration as distinct phenomenal states. A concept page defining moral phenomenology as a category would anchor cross-references from ethics-of-consciousness, meaning-of-life, and consciousness-value-connection. See optimistic-2026-02-08.md
- **Source**: optimistic-review
- **Generated**: 2026-02-08

## Completed Tasks


### ✓ 2026-02-09: Reduce quantum speculation in consciousness-and-memory-consolidation.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-09) found the Minimal Quantum Interaction tenet section introduces quantum Zeno speculation with no evidence and no mechanism connecting femtosecond quantum coherence to seconds-long sleep oscillations. Violates writing style guide on quantum overemphasis. Reduce to brief mention; strengthen the purely philosophical dissociation argument. See pessimistic-2026-02-09.md
- **Output**: obsidian/topics/consciousness-and-memory-consolidation.md

Task context:
Pessimistic review (2026-02-09) found the Minimal Quantum Interaction tenet section introduces quantum Zeno speculation with no evidence and no mechanism connecting femtosecond quantum coherence to seconds-long sleep oscillations. Violates writing style guide on quantum overemphasis. Reduce to brief mention; strengthen the purely philosophical dissociation argument. See pessimistic-2026-02-09.md

### ✓ 2026-02-09: Address introspective methodology gap in phenomenology-of-self-reference.md
- **Type**: refine-draft
- **Notes**: Pessimistic review (2026-02-09) found the article treats introspective reports as data without engaging methodological concerns. It cites Nisbett & Wilson (1977) in references but never addresses implications for its own methodology. Add section on introspective reliability, engage process/content distinction, address Schwitzgebel's critiques. See pessimistic-2026-02-09.md
- **Output**: obsidian/voids/phenomenology-of-self-reference.md

Task context:
Pessimistic review (2026-02-09) found the article treats introspective reports as data without engaging methodological concerns. It cites Nisbett & Wilson (1977) in references but never addresses implications for its own methodology. Add section on introspective reliability, engage process/content distinction, address Schwitzgebel's critiques. See pessimistic-2026-02-09.md

### ✓ 2026-02-09: Create concept page for meta-problem of consciousness
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-01 (evening). Chalmers's 2018 proposal—why do we think there's a hard problem? The Map discusses the hard problem extensively but doesn't engage this reflexive challenge. See optimistic-2026-02-01-evening.md
- **Output**: Create concept page for meta-problem of consciousness

### ✓ 2026-02-09: Create concept page for phenomenal transparency
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-01 (evening). The property that experience seems to be directly about the world rather than about neural states. Mentioned in several articles but not defined. Relevant to why physicalism seems intuitive despite being wrong. See optimistic-2026-02-01-evening.md
- **Output**: Create concept page for phenomenal transparency

### ✓ 2026-02-09: Write article on consciousness and memory consolidation
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-01 (evening). Does consciousness participate in memory consolidation during sleep? The quantum Zeno mechanism during REM. Why dreams feel conscious. Interface activity during non-waking states. Builds on episodic-memory.md, working-memory.md, dreams-and-consciousness.md. See optimistic-2026-02-01-evening.md
- **Output**: consciousness and memory consolidation

### ✓ 2026-02-09: Write article on phenomenology of self-reference
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-01 (evening). What is it like to think about thinking? The peculiar phenomenology of self-reference, Hofstadter's strange loops, and why recursion might require consciousness. Builds on language-recursion-and-consciousness.md, metarepresentation.md, metacognition.md. See optimistic-2026-02-01-evening.md
- **Output**: phenomenology of self-reference

### ✓ 2026-02-09: Write article on consciousness and emergence
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-01 (evening). The Map critiques emergence as consciousness explanation but could develop a positive account of what kind of emergence (if any) is compatible with irreducibility. Strong vs. weak emergence; why consciousness isn't weakly emergent. Builds on emergence.md, downward-causation.md, reductionism.md. See optimistic-2026-02-01-evening.md
- **Output**: consciousness and emergence

### ✓ 2026-02-09: Create concept page for acquaintance-knowledge
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-01. Referenced in discussions of Mary's Room and consciousness-only-territories.md. Russell's distinction between knowledge by description and knowledge by acquaintance is foundational to the knowledge argument. See optimistic-2026-02-01.md
- **Output**: Create concept page for acquaintance-knowledge

### ✓ 2026-02-09: Create concept page for indexical-knowledge
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-01. Referenced throughout (vertiginous-question.md, personal-identity.md) but no dedicated treatment. Would consolidate discussion of "this" consciousness and why indexical facts exceed objective description. See optimistic-2026-02-01.md
- **Output**: Create concept page for indexical-knowledge

### ✓ 2026-02-09: Write article on distinctiveness of human creativity
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-01. How consciousness enables genuine novelty. Great apes restricted to "zone of latent solutions"; humans escape it. The incubation effect (unconscious processing → conscious insight) is empirically established. What does consciousness add? Builds on baseline-cognition.md, consciousness-and-creativity.md, working-memory.md. See optimistic-2026-02-01.md
- **Output**: distinctiveness of human creativity

### ✓ 2026-02-09: Write article on consciousness and temporal integration
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-01. How consciousness binds across time—not just the specious present but narrative identity, autobiographical memory, and prospective planning. IIT addresses instantaneous states; what theory addresses extended temporal phenomenology? Builds on temporal-consciousness.md, duration.md, specious-present.md. See optimistic-2026-02-01.md
- **Output**: consciousness and temporal integration

### ✓ 2026-02-09: Write article on phenomenology of belief revision
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-02-01. What is it like to change one's mind? The moment of belief revision has distinctive phenomenology—the "giving way" of an old view, the "clicking into place" of a new one. Connects to consciousness's role in rationality and the argument from reason. Builds on epistemic-emotions.md, phenomenology-of-error-recognition.md, introspection.md. See optimistic-2026-02-01.md
- **Output**: phenomenology of belief revision

### ✓ 2026-02-09: Write article on phenomenal value realism
- **Type**: expand-topic
- **Notes**: Suggested by optimistic review 2026-01-31 (evening). The metaethical position that experiential qualities have intrinsic normative significance—currently referenced but not systematically developed. Grounds normative facts in irreducible phenomenal facts. Builds on epistemic-advantages-of-dualism.md (mentions it), qualia.md, aesthetic-dimension-of-consciousness.md. See optimistic-2026-01-31-evening.md
- **Output**: phenomenal value realism

### ✓ 2026-02-09: Reduce quantum overemphasis in binding-problem.md
- **Type**: refine-draft
- **Notes**: Pessimistic review found quantum binding material dominates ~1/3 of the article and violates writing style guide warnings about quantum mechanism overemphasis. The claim "current evidence favours quantum binding" overstates the evidential situation. Reduce quantum section, strengthen alternative approaches, and recalibrate confidence language. See pessimistic-2026-02-06-afternoon.md
- **Output**: obsidian/concepts/binding-problem.md

Task context:
Pessimistic review found quantum binding material dominates ~1/3 of the article and violates writing style guide warnings about quantum mechanism overemphasis. The claim "current evidence favours quantum binding" overstates the evidential situation. Reduce quantum section, strengthen alternative approaches, and recalibrate confidence language. See pessimistic-2026-02-06-afternoon.md
## Blocked Tasks (Needs Human)

Tasks that failed 3+ times and require human intervention.

## Vetoed Tasks

Ideas that were considered and rejected. The AI will not re-propose these.