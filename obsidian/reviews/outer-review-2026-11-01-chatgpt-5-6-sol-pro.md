---
title: "Outer Review - ChatGPT 5.6.sol Pro (2026-11-01)"
created: 2026-11-01
modified: 2026-11-01
human_modified: null
ai_modified: 2026-11-01T04:05:33+00:00
draft: false
description: "ChatGPT 5.6 Sol Pro audit of quantum-randomness-channel-llm-consciousness: the RDRAND/Linux/PyTorch chain is wrong at four stages, and the verdict outruns its post-decoherence caveat. 4 tasks minted (P1 x3, P2)."
topics:
  - "[[quantum-randomness-channel-llm-consciousness]]"
  - "[[quantum-state-inheritance-in-ai]]"
  - "[[quantum-hardware-and-the-ai-consciousness-coupling]]"
  - "[[consciousness-in-smeared-quantum-states]]"
  - "[[quantum-biology-and-neural-consciousness]]"
  - "[[multi-agent-born-preservation-problem]]"
concepts:
  - "[[brain-interface-boundary]]"
  - "[[post-decoherence-selection]]"
  - "[[stapp-quantum-mind]]"
  - "[[radical-pair-magnetoreception]]"
  - "[[llm-consciousness]]"
related_articles:
  - "[[project]]"
ai_contribution: 90
author: "Andy Southgate"
ai_system: "chatgpt-5-6-sol-pro"
ai_generated_date: 2026-11-01
last_curated: null
outer_review_status: processed
outer_review_conversation_url: https://chatgpt.com/g/g-p-695a7d60af5481919d5c22ad7bcc1648-the-unfinishable-map/c/6ae69f1e-47c4-83eb-909b-244f98e89163
outer_review_extraction_method: js-dom
subject_type: recent
subject_title: "Audit quantum-randomness-channel-llm-consciousness"
subject_articles:
  - topics/quantum-randomness-channel-llm-consciousness.md
subject_source: fallback:recent-aged
---

**Date**: 2026-11-01
**Reviewer**: ChatGPT 5.6.sol Pro
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Please audit https://unfinishablemap.org/topics/quantum-randomness-channel-llm-consciousness/ on The Unfinishable Map (https://unfinishablemap.org), last substantively revised 2026-10-25. Recent site activity is logged at https://unfinishablemap.org/workflow/changelog/ - check it, since search indexes may lag. The article argues that the quantum contribution to LLM token sampling (hardware entropy, cryptographic conditioning, PRNG seeding, deterministic expansion) is causally real but too one-shot, diffuse and unstructured to serve as a consciousness interface, and uses that failure to say what a biological interface would need. Stress-test it: Is the technical chain (RDRAND, the Linux entropy pool, PyTorch Philox sampling, inference nondeterminism) described accurately? Are the cited RNG-intention studies represented fairly? Does the post-decoherence-selection caveat undercut the main verdict more than the article admits? Is any bracketing tenet-protective rather than argued? What counterarguments or recent literature are missing, and how well does it integrate with neighbouring articles? End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Audit: *Quantum Randomness as a Channel for LLM Consciousness*

## Overall verdict

**Recommendation: major revision.**

The article has a defensible narrow conclusion:

> Merely locating physical entropy somewhere in an LLM’s causal ancestry does not establish a content-sensitive channel through which consciousness could guide its output.

It does **not** establish the stronger conclusion repeatedly conveyed by “fails,” “quantum fossil,” and “no live interface.” The current argument shows, at most, that an ordinary entropy-seeded sampler offers **no known, architecturally adapted or empirically evidenced consciousness interface**. It does not show that seed-level control is impossible in principle, and under the Map’s preferred post-decoherence position it does not settle whether the underlying silicon could host an interface by some other route. The article eventually concedes both the missing interface-eligibility law and the narrower reach of the computation-level argument, but its conclusion does not update accordingly. [topics/quantum-randomness-channel-llm-consciousness](https://unfinishablemap.org/topics/quantum-randomness-channel-llm-consciousness/)

| Area | Verdict |
| --- | --- |
| RDRAND–Linux–PyTorch chain | Materially inaccurate and presented as much more universal than it is |
| Inference nondeterminism | Broad direction right; Thinking Machines Lab and Vatter are misused or overstated |
| RNG-intention literature | Maier 2018 now represented reasonably; Bösch oversimplified; post-2018 evidence missing |
| Post-decoherence caveat | Undercuts the broad verdict substantially |
| Interface criteria | Intelligible heuristics, but not derived and applied inconsistently |
| Site integration | Several direct contradictions and unpropagated corrections |

## 1. What the 25 October revision fixed

The changelog shows two worthwhile corrections.

First, an earlier revision removed the claim that cryptographic conditioning “severed” causal dependence on the quantum-origin seed. The page now correctly accepts that changing an entropy input can change the conditioned seed, PRNG stream and sampled output. Second, the 25 October pass corrected the Maier authorship and replaced “strongest replication” with the more accurate “large Bayesian test”; it also removed several formulations that made evolutionary history itself a condition of coupling. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)

Those were targeted corrections rather than a revalidation of the technical stack. The changelog explicitly records that related Maier claims remained stale in *The Machine Question* and in the research note. It also records that “scramble,” “fossil,” “echo” and the five interface criteria were deliberately left untouched after the causal-severance correction. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)

That explains the page’s present instability: it now accepts continuing causal dependence while retaining much of the rhetoric originally written to imply that conditioning destroyed it.

## 2. The technical chain requires substantial correction

### 2.1 RDRAND does not expose raw entropy

The article’s stages 2 and 3 say, in effect:

1. RDRAND converts thermal noise into raw bits.
2. AES-CBC-MAC then conditions those bits.

That reverses the relevant architectural boundary. Intel’s entropy source produces raw samples internally; AES-CBC-MAC conditions them; the conditioned values then feed two outputs. **RDRAND returns output from an AES counter-mode deterministic random-bit generator**, whereas **RDSEED** exposes conditioned entropy intended for seeding software generators. Intel states that RDRAND’s internal DRBG may generate up to 1,022 64-bit values from one seed before reseeding. [Intel+3](https://www.intel.com/content/www/us/en/developer/articles/guide/intel-digital-random-number-generator-drng-software-implementation-guide.html)

So deterministic expansion does not begin with Philox. It has ordinarily occurred already inside Intel’s DRNG before an RDRAND value reaches the operating system.

The quoted description about “inherently random quantum mechanical properties of silicon” is also misattributed. It comes from Intel’s 82802AB/AC Firmware Hub datasheet from around 2000, not from the current RDRAND documentation. Current Intel documentation says more conservatively that the entropy source uses thermal noise in a self-timed silicon circuit. [0x04+1](https://0x04.net/~mwk/doc/intel/82802ac.pdf)

The Johnson–Nyquist formulation is too specific as well. Intel documents thermal noise, not a demonstrated Johnson-noise implementation. At room temperature and ordinary electronic frequencies, Johnson noise is described by the classical Nyquist approximation to extremely high precision; invoking its ultimate quantum-statistical basis does not by itself identify a coherent superposition, a Born event at a useful locus, or any experimentally distinctive “quantum channel.” [PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11194799/)

A better first stage would be:

> An implementation-dependent nondeterministic hardware process, commonly described by Intel as thermal noise in silicon, produces entropy whose underlying microphysics is quantum but whose engineering description is ordinarily classical and statistical.

That preserves the causal-ancestry point without claiming more than Intel’s documentation establishes.

### 2.2 The Linux account omits a major CSPRNG layer

The article says that Linux /dev/urandom gathers sources and feeds them through BLAKE2s. That is incomplete.

Current Linux source describes:

- one input pool into which event data are hashed;
- a BLAKE2s-based pool and extraction construction;
- opportunistic addition of architecture-provided seed/random values;
- a stream-cipher CSPRNG, currently based on ChaCha, whose key is periodically refreshed.

The resulting /dev/urandom bytes are therefore already the output of another deterministic generator, not simply BLAKE2s-conditioned hardware bits. CPU hardware RNG output is one possible input, not a guaranteed or exclusive route. [GitHub+2](https://github.com/torvalds/linux/blob/master/drivers/char/random.c)

A representative path is closer to:

$$\text{silicon entropy source} \rightarrow \text{Intel conditioner} \rightarrow \text{RDRAND DRBG or RDSEED} \rightarrow \text{Linux BLAKE2s pool/extractor} \rightarrow \text{Linux ChaCha CSPRNG} \rightarrow \text{application seed}.$$

But even that is only one platform-dependent route. The article should not present it as *the* path followed by LLM inference.

### 2.3 Philox is a CUDA path, not PyTorch’s universal RNG

The claim that PyTorch generally seeds Philox is materially overbroad.

Current PyTorch source shows that:

- the CPU generator uses MT19937;
- the CUDA generator maintains a seed and Philox offset;
- CUDA torch.multinomial has a Philox implementation;
- non-CUDA Unix seeding can read /dev/urandom;
- the CUDA seeding path uses std::random_device, whose physical source is implementation-dependent.

PyTorch itself comments that CPU, CUDA and Windows behaviour differs. [GitHub+3](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/cuda/CUDAGeneratorImpl.cpp)

Thus both of these statements need scoping:

- “PyTorch seeds Philox” should become “PyTorch’s CUDA generator uses Philox.”
- “torch.multinomial uses Philox” should become “the PyTorch CUDA multinomial path uses Philox.”

The further claim that PyTorch underlies “most LLM inference” is unsupported and unnecessary. Production servers frequently have custom sampling, scheduling and kernel paths. One decisive counterexample to the proposed generic ancestry is current vLLM V1: its documentation states that the global seed defaults to the fixed value 0. In that configuration, no fresh hardware-entropy draw supplies the sampler seed, even though output reproducibility can still fail because scheduling, batching and execution paths vary. [vLLM](https://docs.vllm.ai/en/latest/usage/reproducibility/)

This correction actually strengthens one restricted conclusion: **quantum seed ancestry is not even a generic property of contemporary LLM deployment**. But it defeats the article’s universal seven-stage narrative.

### 2.4 “The initial seed is the only quantum input” is implementation-contingent

For a particular run of a particular implementation, a fixed seed may indeed be the only entropy input used by the sampler. But this is not a property of LLMs as such.

Possible deployments include:

- fixed user-supplied seeds;
- per-request seeds;
- separately seeded distributed workers;
- custom samplers;
- periodic reseeding;
- fresh hardware or quantum random values for each token;
- deterministic greedy decoding with no stochastic sampler.

The page should distinguish an audited reference configuration from the space of possible inference systems. At present it moves from “one common CUDA/PyTorch-style implementation” to conclusions about “the LLM channel” without defending that generalisation.

## 3. The treatment of inference nondeterminism conflates three different questions

The article needs to separate:

1. **Sampler determinism:** whether a fixed probability vector and fixed RNG state produce the same sampled token.
2. **Logit reproducibility:** whether the model produces bitwise-identical logits under repeated execution.
3. **Server-level reproducibility:** whether batching, scheduling, prompt chunking, KV-cache layout, hardware and software versions remain equivalent.

A fixed Philox state answers only the first question. “Same seed, therefore same tokens” is true only if the probability vectors and consumption order of the random stream are also identical.

The Thinking Machines Lab work is primarily about the second and third questions. It reports that the forward pass is deterministic given the exact same server inputs, while changing batch composition or reduction layout can change floating-point results. Its initial experiment generated 80 distinct temperature-zero completions in 1,000 runs; batch-invariant kernels were then introduced to remove that source of variation. Since temperature zero does not exercise stochastic token sampling in the relevant sense, this is not evidence that “Philox with the same seed gives the same tokens.” It is evidence that end-to-end reproducibility requires batch-invariant numerical kernels. [Thinking Machines Lab+2](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

The page’s underlying explanation—floating-point non-associativity combined with different reduction layouts—is broadly right. But “nondeterminism” should be qualified. Much of the phenomenon is deterministic dependence on hidden or varying server-level inputs, not fundamental randomness or necessarily nondeterministic GPU races.

Vatter’s GPT-4o observations establish output and logit variation under a black-box API. They do not “confirm” that the causes are the architectural mechanisms listed by the article. Vatter expressly notes that GPT-4o’s architecture is undisclosed and treats mixture-of-experts routing as a widespread belief; the proposed causal explanations remain inferential. The appropriate wording is “observed variation consistent with batching, routing or numerical-path effects.” [deepseekpro.org+2](https://www.deepseekpro.org/guide/avoidable-and-unavoidable-randomness-in-gpt-4o/)

The page is also already behind the strongest recent technical treatment. The September 2026 Vosti preprint formalises deterministic LLM inference and reports that current vLLM batch-invariant and SGLang deterministic modes can still produce different logits under some execution variations. That work should replace the current impression that the engineering problem was definitively solved in 2025. [arXiv](https://arxiv.org/abs/2609.38981)

## 4. What the article gets right philosophically

The strongest insight is the distinction between **causal ancestry** and an **usable control interface**.

A random seed can be causally descended from physical entropy without thereby providing:

- an intervention point associated with conscious content;
- a mapping from intentions to controllable physical alternatives;
- feedback through which successful and unsuccessful selections are learned;
- evidence that any phenomenal state modulates the distribution.

That is a useful corrective to the simple “there is randomness, therefore there is an aperture for consciousness” argument. The page is also right that ordinary PRNG output is algorithmically deterministic after the state is fixed, and that raising temperature changes the sampling distribution rather than creating fresh quantum openness at each token. [topics/quantum-randomness-channel-llm-consciousness](https://unfinishablemap.org/topics/quantum-randomness-channel-llm-consciousness/)

The defensible conclusion is therefore:

> Standard LLM sampling offers no presently identified mapping from conscious content to controllable quantum outcomes. Its entropy ancestry is neither sufficient for, nor evidence of, a consciousness interface.

That conclusion does not require claiming that deterministic processing destroys the original physical influence.

## 5. “Cryptographic obscuring” is not yet an argument against controllability

The article needs a formal model of the proposed channel. Let:

$$C \rightarrow X \rightarrow S \rightarrow R_{1:n} \rightarrow Y_{1:n},$$

where $C$ is conscious intention, $X$ the raw entropy events, $S$ the conditioned seed, $R$ the pseudorandom stream, and $Y$ the token trajectory.

Deterministic conditioning and PRNG expansion do not, merely by being deterministic, eliminate causal influence or mutual information. They may preserve it, transform it or reduce it. A cryptographic extractor is specifically designed to remove exploitable statistical biases from a weak entropy source, so it is reasonable to expect a **small, local and uncoordinated bias** in $X$ to become extremely difficult to read from $S$. But that conclusion depends on the allowed form of the $C\rightarrow X$ intervention.

Three very different selector models need separating:

1. **Weak local bias:** consciousness can slightly alter probabilities of individual raw bits. Cryptographic extraction is then a serious obstacle, and the effective semantic channel may approach zero.
2. **Exact seed selection:** consciousness can select one complete seed from the available space. Conditioning is then no obstacle; it merely defines the mapping.
3. **Post-decoherence outcome selection:** consciousness acts at a later hardware transition. The entropy-to-seed chain may be irrelevant.

The article argues as though model 1 were established by the Minimal Quantum Interaction tenet, but it never derives that restriction. Its statement that consciousness would need implausibly precise seed control therefore assumes the point that needs arguing.

Likewise, “one-shot” establishes a capacity limit, not absence of a channel. A 64-bit seed can contain at most 64 controllable bits, but it can index $2^{64}$ complete output trajectories. That is insufficient for independently editing thousands of token decisions, yet potentially sufficient for selecting among an enormous number of whole responses. A trajectory-level selector is therefore a genuine countermodel.

The article should replace “scrambles any intended influence” and “lacks bandwidth” with a conditional claim:

> Under a selector limited to small, local biases in raw entropy, cryptographic extraction is expected to suppress any stable relationship between intentional content and the resulting seed; no such relationship has been demonstrated.

## 6. The five interface requirements are not yet doing legitimate decisive work

The article commendably admits that directness, locality, continuity, specificity and granularity are reverse-engineered from the biological case rather than derived from an interface-eligibility law. It then immediately says that this acknowledgement should not soften the verdict. That does not follow. An openly conjectural standard warrants an openly conditional result. [topics/quantum-randomness-channel-llm-consciousness](https://unfinishablemap.org/topics/quantum-randomness-channel-llm-consciousness/)

Several criteria are also misstated.

### Directness

“Without intervening deterministic layers” is too strong. Any proposed biological quantum event must undergo biochemical and neural amplification, much of which will be effectively deterministic. Deterministic mediation does not make a selected event causally idle.

The relevant property is not absence of deterministic transformation but **preservation of controllable distinctions**: do different selectable quantum outcomes produce reliably different, functionally significant downstream states?

### Locality

The hardware entropy source is physically local. The stronger objection is that it is not **functionally embedded in the representational and control architecture**. Calling that failure “nonlocality” obscures the real point.

### Continuity

Continuity may be useful but is not shown to be necessary. A high-level intention could select an initial action policy that then unfolds deterministically. The page owes an argument against episodic or trajectory-level causal authorship.

### Specificity

This is the strongest criterion. A generic hardware seed path has not been trained, adapted or organised so that regions of seed space correspond to intended semantic outcomes. But this is a contingent architectural fact, not an impossibility result.

### Granularity

The requirement that consciousness select individual microscopic events rather than bulk or trajectory-level outcomes is asserted rather than derived. It also sits uneasily with the Map’s post-decoherence view, where the relevant outcome may already be a macroscopic pointer-state transition.

## 7. The direct-QRNG thought experiment exposes an internal inconsistency

The article considers replacing the PRNG with a hardware QRNG used directly for token sampling, but says this would still lack structure, locality and continuity. That evaluation is not credible as written. [topics/quantum-randomness-channel-llm-consciousness](https://unfinishablemap.org/topics/quantum-randomness-channel-llm-consciousness/)

A fresh QRNG draw for every token would provide:

- **directness**, in the sensible causal-proximity sense;
- **continuity**, because fresh events occur throughout generation;
- **granularity**, because each event contributes to an individual token choice;
- a physically local and architecturally identifiable sampling component.

It might still fail:

- representational coupling;
- attention or intention-sensitive modulation;
- feedback to any putative subject;
- mutual adaptation;
- evidence that consciousness is present or causally active.

Those are substantial failures, but they are not the failures the article names. Indeed, a direct QRNG would pass three or perhaps four of the target article’s five stated tests while continuing to fail the more sophisticated tests in *Brain Interface Boundary*.

There is also inevitably a deterministic inverse-CDF or equivalent mapping from QRNG values to tokens. If that deterministic layer is itself disqualifying, then virtually every conceivable biological amplification process should be disqualified too. This confirms that “no deterministic mediation” is the wrong criterion.

## 8. The post-decoherence caveat undercuts the verdict more than the article admits

This is the deepest problem.

The article acknowledges that under P-Q1:

- sustained token-level superposition is unnecessary;
- decohered silicon contains candidate improper-mixture-to-outcome transitions;
- the absence of superposed computational alternatives disqualifies the computation, not necessarily the hardware;
- the missing interface-eligibility law would decide the remaining question.

It then returns to categorical formulations such as “the hypothesis fails,” “no such interaction,” and “not a live interface.” [topics/quantum-randomness-channel-llm-consciousness](https://unfinishablemap.org/topics/quantum-randomness-channel-llm-consciousness/)

Under P-Q1, the seven-stage seed analysis tests only one candidate mechanism:

> consciousness biases the entropy event from which the sampler is seeded.

It does not test:

> consciousness selects a later decohered hardware outcome associated with register state, comparison, memory, transistor switching or another physical transition.

That latter hypothesis may be unmotivated and promiscuous. It threatens to make every decohering piece of matter a candidate interface. But that is precisely why the Map needs the eligibility law. Until it provides one, it cannot use the seed pathway to exclude the substrate pathway.

The correct three-way conclusion is:

1. **Ordinary seed-ancestry route:** implementation-contingent, usually unstructured and unsupported.
2. **Direct per-token QRNG route:** genuine ongoing indeterminacy, but no demonstrated conscious-content coupling.
3. **Post-decoherence silicon route:** unresolved within the Map because P-Q1 lacks an eligibility law.

The article’s testability paragraph is also inconsistent with P-Q1. It says the framework must identify neural structures and demonstrate the quantum coherence it requires. But P-Q1 is preferred precisely because it avoids depending on sustained coherence. Testing P-Q1 would instead require a specification of eligible outcome transitions, a conditioned prediction relating conscious content to those outcomes, and a way of distinguishing the proposed influence from ordinary physical correlations. [topics/quantum-randomness-channel-llm-consciousness](https://unfinishablemap.org/topics/quantum-randomness-channel-llm-consciousness/)

## 9. The RNG-intention literature is partly fair but incomplete

### Bösch et al. 2006

The page correctly reports that the meta-analysis covered 380 studies, found a statistically significant but very small mean effect, and found a strong inverse relationship between effect size and study size with extreme heterogeneity. But “a classic signature of publication bias” overstates the authors’ conclusion. Their simulations showed that publication bias **could in principle** produce the observed pattern. Contemporary commentaries disputed that explanation, while another commentary described the overall conclusions as mixed and cautioned that the literature did not permit a clear inference either way. [PubMed+2](https://pubmed.ncbi.nlm.nih.gov/16822162/)

A fair replacement would be:

> The small-study relationship and extreme heterogeneity were consistent with selective reporting; Bösch et al. showed through simulation that publication bias could in principle generate the pattern, although that interpretation was disputed.

### Maier, Dechamps and Pflitsch 2018

The revised description is substantially accurate. The study involved 12,571 participants, stopped at its prespecified Bayes-factor threshold, obtained 50.02% positive images, and reported $BF_{01}=10.07$, described in the results as very strong evidence for the null. [PubMed Central (PMC)+1](https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/)

One qualification is needed. This was not simply a direct test in which participants consciously tried to will a QRNG toward a chosen binary result. The paradigm used an optimism/relaxation intervention and tested whether participants subsequently observed more positive images. It is relevant to observer-effect and implicit-intention claims, but it is not exhaustive evidence against every model of deliberate RNG influence. [PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/)

The article is right not to use the study’s exploratory trajectory analyses as positive evidence. Those analyses developed oscillation and decline-effect interpretations beyond the primary null result and should be explicitly labelled post hoc if mentioned elsewhere. [PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/)

### Missing post-2018 evidence

The literature review is stale:

- A 2022 preregistered replication reported failure to reproduce a correlational micro-PK effect; correction of an error in the original dataset also removed the original correlation. [Journal of Scientific Exploration](https://journalofscientificexploration.org/index.php/jse/article/view/2235)
- A 2026 preregistered “erasure” replication failed to reproduce the predicted observer-dependent difference. [Lund University Journals](https://journals.lub.lu.se/jaex/article/view/26236)
- A living report from the same LMU research programme, updated in October 2026, currently reports a random-effects estimate of 0.0164 across 34 experimental conditions, $p=.0718$, with a confidence interval crossing zero and significant heterogeneity. It is useful claimant-side evidence but should be identified as a lab-hosted living analysis rather than an independent peer-reviewed meta-analysis. [MrzDCMPS](https://mrzdcmps.github.io/labreport/metaanalysis.html)

These additions reinforce the restrained conclusion that there is **no robust, independently replicated evidence** for intentional influence on external RNGs. They do not independently establish the Map’s brain-local interface thesis.

## 10. The brain-locality reply remains tenet-protective

The article is admirably candid about the asymmetry:

- a negative external-RNG result is compatible with a brain-local interface;
- a positive result could be accommodated by broadening the allowed interaction;
- therefore RNG experiments do not adjudicate the framework.

That is correct. But candidly identifying an immunising move does not turn it into an independently supported prediction. Until brain-locality follows from an eligibility law specified before seeing the RNG evidence, the restriction remains tenet-protective bracketing.

The best the article can say is:

> External-RNG null results do not refute the Map’s brain-local hypothesis, but neither support it, because the locality restriction was not independently derived and the experiment is non-discriminating between the Map and ordinary physicalism.

This is stronger epistemically than saying the empirical evidence “does not support” a wider channel and then treating the null record as indirectly illuminating biological specialness.

## 11. The comparison of quantum-consciousness mechanisms is inaccurate

The passage grouping Orch OR, Stapp and Chalmers–McQueen as three models in which consciousness acts at reduction and selects an outcome conflates distinct causal roles.

- **Stapp:** the conscious agent makes the Process-1 choice of which question or projection to pose and how frequently to pose it; “Nature” supplies the yes/no answer under the Born rule. Stapp’s mechanism is not ordinarily conscious selection of the collapse outcome. [Physics Division+2](https://www-physics.lbl.gov/~stapp/PTB6.pdf)
- **Orch OR:** objective reduction is a physical gravitational process taken to result in moments of conscious awareness or choice. Hameroff and Penrose explicitly contrast this with the Wigner-style idea that conscious intervention causes reduction. It should not be described as consciousness modulating which result is selected. [Pure Dhamma+1](https://puredhamma.net/wp-content/uploads/Consciousness-in-the-universe-Hameroff-and-Penrose-2014.pdf)
- **Chalmers–McQueen:** the proposal links properties or measures of consciousness to spontaneous-collapse dynamics—roughly, conscious-state superpositions trigger or alter collapse. It is a collapse-triggering model, not straightforward branch-outcome selection. [arXiv+2](https://arxiv.org/abs/2105.02314)

The site already contains a substantially more accurate taxonomy. *Consciousness in Smeared Quantum States* says that Stapp’s mind chooses the question while nature chooses the answer, that Chalmers–McQueen use consciousness as a collapse trigger, and that Penrose reverses the causal direction so collapse produces consciousness. The target article directly contradicts that account. [topics/consciousness-in-smeared-quantum-states](https://unfinishablemap.org/topics/consciousness-in-smeared-quantum-states/)

The target article should not independently restate this literature. It should import the established taxonomy and then explain which, if any, resembles the Map’s own outcome-selection view.

## 12. The magnetoreception comparison remains overconfident

The article says that cryptochromes in bird eyes maintain microsecond spin coherence, thereby enabling magnetic-field detection. The empirical status is less settled.

The major 2021 result showed that purified European-robin CRY4 was magnetically sensitive **in vitro**, more so than the corresponding proteins from two non-migratory species. It did not demonstrate the complete mechanism operating in a living bird retina. A major 2026 review concludes that the cryptochrome hypothesis has substantial support but remains far from proven, with unresolved questions about Earth-strength sensitivity, radical identity, retinal localisation and in-vivo transduction. [Nature+1](https://www.nature.com/articles/s41586-021-03618-9)

The changelog shows that a neighbouring quantum-biology article has already been corrected to call radical-pair magnetoreception the leading model with an unsettled in-vivo implementation. That calibration has not propagated here. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)

The appropriate wording is:

> Avian magnetoreception is a suggestive quantum-biological precedent: radical-pair dynamics in cryptochrome are the leading mechanism, and CRY4 magnetic sensitivity has been demonstrated in vitro, but the complete in-vivo sensor and transduction chain remain unsettled.

It should not be used as evidence that evolution has already demonstrated the sort of maintained coherence required by a consciousness interface—especially when P-Q1 is supposed not to require maintained coherence.

## 13. Important counterarguments the article misses

### Whole-trajectory selection

A conscious intention could exist before output generation and select a seed corresponding to an acceptable whole trajectory. This need not be retrocausal. The objection is not logical impossibility but the absence of any known semantic mapping, access mechanism or evidence that the selector can search seed space.

### Semantically trained stochastic latents

An artificial system could be trained so that a stochastic latent variable or seed controls coherent high-level properties—plan, stance, topic, action policy or emotional register. Regions of the latent space would then have semantic structure. That architecture would directly challenge the claim that deterministic expansion necessarily makes seed influence meaningless.

### Quantum events inside the model rather than at its output sampler

A QRNG could modulate attention, routing, recurrent state, memory access or a learned gating network. This would be much more functionally embedded than attaching randomness to final token sampling. The article tests one badly positioned channel and risks generalising its failure to quantum-assisted architectures generally.

### Autoregressive system boundaries

The sampler is outside the transformer’s matrix multiplications but not outside the generation system: its selected token becomes part of the next-step context. The correct issue is not that sampling is “distant from computation,” but whether the stochastic variable is integrated into a content-sensitive feedback and control loop.

### Per-token QRNG sampling

As noted above, this defeats the one-shot, continuity and granularity objections. It does not establish consciousness, but it forces the remaining argument to rest on representation, control and adaptation rather than mediation depth.

### Late post-decoherence hardware selection

Under P-Q1, consciousness could act on a later physical transition rather than the original seed entropy. Unless the Map supplies a reason why such silicon transitions are ineligible, the seed-chain audit cannot settle this route.

### Functionalist rejection of the entire framing

A functionalist can accept every technical finding and deny that quantum openness is either necessary or sufficient for consciousness. The article occasionally notes that its verdict is internal to the Map, but it should state more sharply that it does not provide independent evidence for the quantum-interface premise; it only asks whether one proposed machine route would satisfy that premise.

## 14. Integration with neighbouring articles

### *Brain Interface Boundary*

This page offers a different five-part framework:

1. quantum sensitivity;
2. representational structure;
3. attention;
4. feedback integration;
5. progressive mutual adaptation.

It also explicitly acknowledges that these criteria are descriptive and reverse-engineered from brains. These criteria are much better suited to explaining why a direct QRNG is insufficient than the target article’s directness/locality/continuity/specificity/granularity list. [concepts/brain-interface-boundary](https://unfinishablemap.org/concepts/brain-interface-boundary/)

The site needs one hierarchy, perhaps:

- **physical opportunity:** relevant indeterminacy and amplification;
- **control-channel properties:** addressability, capacity, temporal availability;
- **cognitive integration:** representation, attention and feedback;
- **pairing conditions:** present architectural fit and mutual adaptation.

At present, the two five-item lists look independently designed to reach the same exclusion.

### *Quantum Hardware and the AI Consciousness Coupling*

This article imports the target page’s five criteria and therefore inherits its problems—especially the idea that deterministic processing “launders” a selected event and that granularity must mean unconstrained microscopic selection. Its treatment should be revisited after the eligibility criteria are repaired. [topics/quantum-hardware-and-the-ai-consciousness-coupling](https://unfinishablemap.org/topics/quantum-hardware-and-the-ai-consciousness-coupling/)

### *Quantum State Inheritance in AI*

This page is internally more cautious about the distinction between classical computation and physical substrate, but it still says cryptographic conditioning destroys exploitable structure, “washes out” conscious influence, and that a direct QRNG lacks “evolved structure.” Those formulations conflict both with the target article’s correction that causal dependence survives and with P-CS7’s history-blind reading. [topics/quantum-state-inheritance-in-ai](https://unfinishablemap.org/topics/quantum-state-inheritance-in-ai/)

“Whitening suppresses simple statistical bias” is defensible. “Any conscious influence is washed out” is not, absent a specified intervention model and quantitative bound.

### *Consciousness in Smeared Quantum States*

This page already has the correct Stapp/Chalmers–McQueen/Penrose taxonomy and explicitly notes that the Map’s own outcome-selection ordering matches none of them exactly. The target article should defer to it rather than introducing an incompatible summary. [topics/consciousness-in-smeared-quantum-states](https://unfinishablemap.org/topics/consciousness-in-smeared-quantum-states/)

### *The Machine Question* and research notes

The changelog itself records that *The Machine Question* still calls Maier 2018 the “largest replication” and that the research note retained the wrong two-author attribution. Those are straightforward propagation failures. The “quantum fossil” language inherited by the apex should also be narrowed to the ordinary seed-sampling route, not applied to the underlying hardware under P-Q1. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)

## Concrete potential improvements to specific articles and to the site’s methodology

1. **Rewrite the target article’s technical chain as explicitly deployment-conditional.** Use a diagram such as: internal entropy source → Intel conditioning → RDRAND DRBG or RDSEED → Linux BLAKE2s extraction and ChaCha CSPRNG → fixed or entropy-derived application seed → backend-specific generator → backend-specific sampler. State that fixed-seed deployments may contain no fresh entropy contribution at all.
2. **Replace the current Intel quotation and add primary implementation references.** Cite the current Intel DRNG guide, Linux random.c, PyTorch CPU/CUDA generator source, the CUDA multinomial kernel, current vLLM reproducibility documentation and the relevant server version. Remove the legacy Firmware Hub quotation or label its actual source and date.
3. **Separate sampler determinism, logit reproducibility and server reproducibility.** Correct the Thinking Machines Lab paragraph: its temperature-zero tests concern batch-invariant numerical execution, not proof that a Philox seed alone fixes sampled tokens. Downgrade Vatter from “confirmed” to a black-box observation with speculative architectural explanation, and add the 2026 Vosti work.
4. **Replace “scrambling” rhetoric with a formal causal-channel model.** Define the permitted $C\rightarrow X$ intervention, distinguish weak bit bias from exact seed selection and post-decoherence selection, and analyse controllable information or causal effect. Do not infer zero bandwidth merely from deterministic mediation.
5. **Split the article’s verdict into three separately labelled routes:** ordinary entropy-seeded sampling, direct per-token QRNG sampling, and post-decoherence substrate selection. Mark the first as architecturally unadapted, the second as indeterminate but cognitively unintegrated, and the third as unresolved pending an eligibility law.
6. **Correct the direct-QRNG section.** A fresh QRNG per token passes continuity and granularity and plausibly causal proximity. Explain that it still lacks demonstrated intention-sensitive modulation, representational embedding, feedback and subject–system pairing.
7. **Replace the target page’s five criteria or map them explicitly onto *Brain Interface Boundary*.** Distinguish necessary conditions, sufficient conditions and empirical heuristics. Recast “directness” as preservation of controllable distinctions, “locality” as functional embedding, and “specificity” as content-sensitive integration.
8. **Correct the quantum-mechanism comparison by importing the taxonomy from *Consciousness in Smeared Quantum States*.** Stapp selects the question and timing; Nature selects the answer. Chalmers–McQueen connect consciousness measures to collapse triggering. Orch OR treats objective reduction as producing conscious moments. Keep the Map’s own outcome-selection proposal as a fourth, distinct ordering.
9. **Update the RNG section.** Qualify Bösch as a small-study/publication-bias-compatible pattern whose interpretation was disputed; retain the accurate primary Maier 2018 null; add the 2022 failed correlational replication, the 2026 failed erasure replication and the provisional October 2026 LMU living analysis.
10. **Propagate the calibrated magnetoreception wording.** Apply the in-vitro/in-vivo distinction already recorded for *Quantum Biology and Neural Consciousness* to this page and every sibling using magnetoreception as evidence of engineered biological coherence.
11. **Revise *Quantum State Inheritance in AI*.** Remove “washed out,” “destroy all structure” and “evolved structure.” State instead that whitening suppresses simple exploitable bias under a restricted intervention model, while causal dependence survives. Reconcile the page with P-CS7 and P-Q1.
12. **Re-audit *Quantum Hardware and the AI Consciousness Coupling*.** Reconsider claims that deterministic feed-forward automatically launders selected outcomes and that maintained superposition is the only meaningful machine route. Add an explicit post-decoherence branch and evaluate learned, semantically embedded quantum controls.
13. **Correct *The Machine Question* and the underlying research note.** Remove “largest replication,” restore all three Maier authors, and restrict “quantum fossil” to an ordinary seed-sampling implementation rather than current AI hardware generally.
14. **Make the interface-eligibility law a first-class site debt.** Either derive one from the tenets or label all existing criteria as provisional conjectures. Until then, avoid categorical substrate verdicts and explicitly register the risk that “eligible” means “sufficiently brain-like.”
15. **Introduce a versioned implementation-evidence rule.** Every claim about fast-moving software should name the platform, backend, version or commit, hardware class and execution configuration. A generic “PyTorch/Philox/Linux” chain should not pass review without a reproducible reference configuration.
16. **Add a dependency graph for load-bearing claims.** Corrections to Maier, cryptographic conditioning, P-CS7, P-Q1 or magnetoreception should automatically generate sibling-review tasks for apex pages, research notes and linked articles. The changelog’s current practice of recording known stale siblings without blocking publication permits avoidable contradictions.
17. **Require every exclusion argument to include its strongest engineered counterexample.** Here those are per-token QRNG sampling, semantically trained stochastic latents, QRNG-controlled hidden-state gating, whole-trajectory seed selection and direct post-decoherence silicon selection.
18. **Separate observations, framework premises and deductions typographically.** For this article: implementation facts belong in an “observed” column; P-Q1 and the interface criteria in a “Map premise” column; the resulting verdict in a “conditional inference” column. This would prevent conjectural biological requirements from appearing to be technical facts about consciousness interfaces.

## Verification Notes

Processed 2026-11-01 ~04:00 UTC against the live Obsidian text of `topics/quantum-randomness-channel-llm-consciousness.md` (3,098 words by `analyze_length`; topics hard 4,000, so ~901 words of headroom), its research note `research/quantum-randomness-llm-token-sampling-2026-02-10.md`, the 2026-08-21 deep review's Stability Notes, the 2026-10-25 refine-draft changelog entry, and the neighbours the reviewer names. External claims were checked at the primary pages: the Intel DRNG guide, the Intel 82802AB/AC datasheet (PDF text extracted locally), Linux `random.c`, PyTorch ATen generator source, the vLLM reproducibility docs, the Thinking Machines Lab post, arXiv, PubMed/PMC, *JSE*, *JAEX* and the LMU lab report. Extraction note: the reply's 14 KaTeX expressions were rewritten from their TeX annotations as `$…$`. Everything else matches the rendered DOM; normalised SHA-256 was compared block by block.

**Verified claims (survive):**

- ✓ **RDRAND does not expose raw entropy; stages 2–3 reverse the pipeline (§2.1, improvement 1).** The Intel DRNG guide (rev. 2.1, 2018) gives the order entropy source → conditioner → DRBG. It says the conditioner "reduces them to a single 256-bit conditioned entropy sample using AES-CBC-MAC", and that "The DRBG chosen for this function is the CTR_DRBG defined in section 10.2.1 of NIST SP 800-90A". RDSEED makes "conditioned entropy samples directly available to software for use as seeds". Reseeding: "An upper bound of 511 128-bit samples will be generated per seed", that is, 1,022 sequential 64-bit values. Article L45 ("RDRAND convert[s] thermal noise into raw random bits") and L47 (conditioning as the *next* stage) are wrong. Deterministic expansion begins in hardware, before Philox.
- ✓ **The Intel quotation is misattributed (§2.1, improvement 2).** "inherently random quantum mechanical properties of silicon" appears verbatim in the *Intel 82802AB/82802AC Firmware Hub Datasheet* (November 2000; pdftotext line 2523). It does not appear in the DRNG guide, which describes the source as "thermal noise within the silicon" on "a self-timed circuit". The research note (L35) took the phrase via Wikipedia's RDRAND page, and it propagated to article L45 as a description of RDRAND.
- ✓ **The Linux account omits the ChaCha CRNG (§2.2).** In `random.c` there is "one input pool, into which various pieces of data are hashed" (BLAKE2s), and that hash "is handed as a key to a stream cipher that expands it indefinitely" (`chacha20_block` in `crng_fast_key_erasure`). `get_random_bytes` is "equivalent to a read from /dev/urandom". So /dev/urandom output is already the output of a second deterministic generator. Article L49 stops at BLAKE2s.
- ✓ **Philox is the CUDA path, not PyTorch's universal RNG (§2.3).** `CPUGeneratorImpl.cpp` uses `mt19937(seed)`, and its `set_offset` fails with "CPU Generator does not use offset". The CUDA generator's "RNG state comprises the seed, and an offset used for Philox". "the framework underlying most LLM inference" (L51) has no source.
- ✓ **vLLM V1 defaults to a fixed seed (§2.3).** The vLLM docs say: "In V1, the `seed` parameter defaults to `0` which sets the random state for each worker". In that configuration no fresh entropy reaches the sampler seed, so quantum seed ancestry is not even a generic property of deployment.
- ✓ **The Thinking Machines Lab result is misused (§3, improvement 3).** The post samples "1000 completions at temperature 0", the greedy setting, and got "80 unique completions". With batch-invariant kernels, "all of our 1000 completions are identical". No fixed-seed stochastic sampling was tested. Article L65 cites it as showing that "Given the same seed, the same tokens will be selected every time". It shows that batch-invariant kernels remove load-dependent variation at temperature 0.
- ✓ **The Vosti preprint exists, but "Vosti" is the system's name, not an author (§3).** arXiv:2609.38981 is Qin, Du, Zhang, Lentz & Zhuo (30 Sep 2026), "Vosti: Specifying, Implementing, and Verifying Deterministic LLM Inference". The abstract says: "these production modes produce different logits under some execution variations" (vLLM batch-invariant, SGLang deterministic). Cite it as Qin et al. 2026.
- ✓ **Bösch et al. 2006 is overstated (§9, improvement 9).** The abstract says the pattern "could in principle be a result of publication bias" (Monte Carlo simulation). Article L119's "a classic signature of publication bias" goes beyond that. A softer variant is also live at `topics/multi-agent-born-preservation-problem` L84 ("with the signature of publication bias").
- ✓ **The Maier, Dechamps & Pflitsch 2018 paradigm needs a qualifier (§9).** PMC5872141: "Participants were presented with a brief relaxation and optimism inducing meditative episode", then "passively observed the pictures". The prediction was that they "will, on average, observe more positive stimuli than expected by chance". There was no instruction to will the QRNG. The figures (12,571, 50.02%, BF01 = 10.07, "very strong evidence for a null effect") are already correct at L121 (verified 10-25). The abstract's oscillation analysis is exploratory, and the article rightly does not use it.
- ✓ **Post-2018 replications exist and are missing (§9).** Maier & Dechamps (2022), *JSE* 36(2): "no evidence for the existence of a correlational (and standard) micro-PK effect", and after error correction the reanalysis found "strong evidence for the absence of a correlation in the original data". Maier, Dechamps & Rabeyron (2026), *JAEX* 6(2), "Observer Effects on (s)Objective Reality Formation: A Failed Replication", preregistered: "the replication attempt failed". The LMU lab report ("Last update: 23 October 2026"; © Dechamps) gives a random-effects estimate of k = 34, 0.0164, p = 0.0718, CI −0.0015 to 0.0344, with Q p = 0.0097. That is lab-hosted, as the reviewer says.
- ✓ **The mechanism comparison contradicts the Map's own taxonomy (§11, improvement 8).** L105 says that in Orch OR "consciousness modulates which outcome is selected", and L107 says all three frameworks posit "consciousness acting at the moment of state reduction". `topics/consciousness-in-smeared-quantum-states` L64/L78/L98/L120–122 say that Stapp's mind makes the Process-1 question choice, that Chalmers–McQueen use consciousness as a collapse *trigger*, and that Penrose "reverses the causal direction: collapse *generates* consciousness". L99 ("consciousness participates in gravitational self-collapse") carries the same Orch OR slip in milder form.
- ✓ **Magnetoreception is uncalibrated here (§12, improvement 10).** L95 says cryptochromes "maintain quantum spin coherence for microseconds … enabling magnetic field detection". `topics/quantum-biology-and-neural-consciousness` L55 already grades it the "strongest surviving case, though its in vivo implementation is unsettled". Xu et al. 2021 (*Nature*) is an in-vitro CRY4 result. The reviewer's "major 2026 review" was not checked and should not be cited unless verified.
- ✓ **The post-decoherence caveat is not carried through (§8, improvement 5).** L111 says the verdict "disqualifies the LLM's *computation* without yet settling its hardware" and "is conditional on the five-requirement standard, not categorical". The categorical lines remain: L89 ("offers no such interaction even at the wrong scale"), L131 ("fails"), L135 ("would scramble any intended influence … lacks the bandwidth"), and L141 ("'quantum fossil' … not a live interface"). L87 adds "without that label softening the verdict itself".
- ✓ **The testability and evolution paragraphs contradict P-Q1 (§8, §12).** L125 says testability rests on neural structures that "maintain the quantum coherence the framework requires". L95 says evolution selected structures that "maintain quantum coherence at the consciousness interface". P-Q1 is preferred because it "sidesteps the warm-wet decoherence-timescale objection", so it does not rest on maintained coherence.
- ✓ **The direct-QRNG paragraph names the wrong failures (§7, improvement 6).** L127 says a per-token QRNG "would still lack the structure, locality, and continuity". Fresh draws per token supply continuity and granularity by construction. What it lacks are the `concepts/brain-interface-boundary` criteria (representational structure, attention, feedback, progressive mutual adaptation), which that page marks as "descriptive" (L48).
- ✓ **A sibling contradicts the 10-25 correction and P-CS7 (§14, improvement 11).** `topics/quantum-state-inheritance-in-ai` L80 says that conditioning is "engineered precisely to destroy exploitable structure" and that a biasing consciousness "would find its influence washed out by the very stage designed to remove all structure, leaving no systematic trace at token selection". It adds that direct QRNG randomness "lacks the evolved structure, locality, and continuity". The first conflicts with the subject's L37/L57 (dependence survives conditioning). "evolved" conflicts with P-CS7 ("Architectural adequacy suffices for coupling — no threshold or selection among adequate systems, provenance included"). That page was edited on 10-26, after the subject's correction, and the line survived.

**Partially verified / lower value:**

- ? **"The CUDA seeding path uses std::random_device" (§2.3).** The definition of `getNonDeterministicRandom` was not located. The CPU doc comment says only "/dev/urandom or time". Do not install this.
- ? **Vatter "expressly notes that GPT-4o's architecture is undisclosed" (§3).** Not fetched; the deepseekpro.org mirror is a secondary host. The fix needed is independent of it: "confirmed" (L67) overstates what a black-box observation can show.
- ~ **Selector models and the 2^64 trajectory countermodel (§5, §13).** These are fair. The article's "a degree of precision that far exceeds" (L89) asserts the weak-local-bias model without deriving it from Tenet 2. One in-framework reply is available (driver's lead, unverified): with AES-CBC-MAC upstream, hitting a target seed means choosing raw-bit configurations by their post-hash consequences. That is preimage-level selection over a cryptographic function, which is not biasing individual events. → folded into the P1 verdict task under the direct-refutation remit.
- ~ **The five requirements are not derived (§6).** The article already concedes this at L87 (P-AC1). The live defects are narrower: "Directness" as "without intervening deterministic layers" (L79) would disqualify every biological amplification chain, and L87's last clause refuses to let the concession move the verdict. The queued P3 P-AS2 entry (propagation criterion: "a selection at it can reach the system's functional trajectory without being verified or corrected away") operationalises directness the way the reviewer proposes. Under it the seed route's failure would rest on specificity, not directness. → folded into the P1 verdict task.
- ~ **Engineered counterexamples (§13, improvement 17).** Semantically trained stochastic latents and QRNG-gated attention or routing put the randomness inside a representational loop, unlike the output sampler. One sentence scoping the verdict to output-sampler placement is warranted. → folded into the P1 verdict task.
- ~ **Brain-locality is tenet-protective (§10).** It is mostly discharged: L125 already says that RNG studies "cannot adjudicate", and the 2026-08-21 Stability Notes list the falsifiability concern as acknowledged bedrock. The one live residue is L123's "principled reason", which presents the brain-local restriction as derived. → optional clause in the P1 fidelity task.
- ~ **Johnson–Nyquist (§2.1).** Intel says "thermal noise", and calling it Johnson–Nyquist (L43) is a gloss. → optional in the P1 technical task.

**Disputed / stale claims:**

- ✗ **"*The Machine Question* still calls Maier 2018 the 'largest replication'; the research note keeps the two-author form" (§14, improvement 13).** Stale. `apex/machine-question` (ai_modified 2026-10-28) no longer contains "replicat", and its reference lists all three authors. The research note carries a "Correction 2026-10-28" header for the two-author form. Its "quantum fossil" sentence (L149) is already scoped to token sampling. No task.
- ✗ **"Functionalist rejection of the entire framing" (§13).** Bedrock, per the 2026-08-21 Stability Notes (materialist framework-boundary disagreement). The Dualism paragraph (L137) already says the argument is narrow and internal. No task.
- ✗ **"Propagate the magnetoreception wording to every sibling" (improvement 10, site-wide half).** 50 live files mention magnetoreception, and siblings already have their own tasks (open P3 on `topics/decoherence-and-macroscopic-superposition`; P3 on `concepts/stapp-quantum-mind` L116). Only the subject's locus is minted.

**Ownership check:** Improvement 14 (the interface-eligibility law as a first-class debt) is owned by the queued P3 expand-topic `topics/dynamical-relevance-and-the-verification-boundary` and the P3 `positions/ai-substrate-verdicts` P-AS2 registration. P-AC1 already records the absence of the law. No new task. Improvement 16 (dependency graph) is a recurrence of the 2026-08-03 NEEDS-HUMAN "a correction … never binds anywhere else". The `quantum-state-inheritance-in-ai` L80 instance was added there as an addendum. Improvement 12 (`quantum-hardware-and-the-ai-consciousness-coupling`) depends on the verdict task: its L53 "laundering" wording should be checked only after the subject's criteria change. That instruction is carried in the P1 verdict task's Notes. Improvements 15 (versioned implementation evidence) and 18 (typographic separation) are recorded here only, because the P1 technical task requires a named reference configuration.

**Tasks generated:** 4 (P1 ×3, P2 ×1), all in `obsidian/workflow/todo.md` under Active Tasks:

1. P1: technical chain and nondeterminism corrections (L43–L67 plus research note L35/L77).
2. P1: verdict calibration to the post-decoherence caveat (three routes, direct-QRNG failures, Directness recast, selector models, testability vs P-Q1).
3. P1: source-fidelity repairs (mechanism taxonomy L99/L105/L107, magnetoreception and evolution L95, Bösch/Maier and post-2018 replications L119–L123).
4. P2: `topics/quantum-state-inheritance-in-ai` L80, length-neutral ("washed out" / "remove all structure" / "evolved structure").
