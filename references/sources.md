# Prompt Compiler sources and evidence map

**English** · [Русский](sources.ru.md)

Last checked: **2026-09-01**.

This document links Prompt Compiler's key design choices to official model documentation, papers by the researchers, and industry security guidance. It does not claim that one technique improves every model and task. Vendor documentation describes particular model families; academic and industry studies remain bounded by their models, datasets, and methods. The author's private exploratory notes were used as a topic map but are neither published nor treated as evidence.

## Evidence labels

- **Official documentation** — guidance or behavior documented by the model developer.
- **Research** — a work with a published method and results; transfer beyond the experiment is not assumed.
- **Project decision** — an explicit Prompt Compiler policy derived from multiple sources and project requirements.
- **Needs revalidation** — a claim from exploratory work that must not be presented as established without separate verification.

## Claim map

<a id="src-clear-specific"></a>
### [src:clear-specific]

**Supports:** a clear goal, relevant context, explicit constraints, and an output contract, with minimal template inflation.

Anthropic recommends clear, direct instructions, explicit formats and constraints, and relevant context. Google recommends clear and specific instructions, constraints, and response formats. OpenAI describes prompt engineering as writing instructions that reliably produce the required behavior and recommends evaluations to monitor that behavior.

**Status:** official documentation; convergent guidance from several vendors.

**Sources:**
- [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Google — Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)

### [src:success-criteria-evals]

**Supports:** success criteria should be observable, and verification is useful when a real external signal exists.

Anthropic places a clear definition of success criteria and a way to test them before prompt optimization. OpenAI recommends pinning model versions and maintaining evaluations when prompts or model versions change.

**Status:** official documentation; project decision not to add vague “self-checking” when the result cannot be checked.

**Sources:**
- [Anthropic — Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)

### [src:structure-delimiters]

**Supports:** separating instructions, context, examples, and input data with Markdown or XML, using structure only when needed.

Anthropic states that XML tags help Claude parse complex prompts unambiguously. OpenAI recommends Markdown and XML to mark logical boundaries between instructions and contextual data. This supports the available `Goal / Context / Inputs / Requirements / Output / Success criteria` sections, but not requiring all six in every prompt.

**Status:** official documentation; omitting empty and obvious sections is a project decision.

**Sources:**
- [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)

### [src:examples]

**Supports:** adding few-shot examples only when they materially specify format, tone, or behavior, and keeping them representative of the real task.

Anthropic describes a small set of high-quality examples as a reliable way to control format, tone, and structure. Google documents zero-shot and few-shot prompting and demonstrates examples as response-pattern specifications.

**Status:** official documentation; applicability depends on model family and task.

**Sources:**
- [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Google — Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)

<a id="src-long-context-placement"></a>
### [src:long-context-placement]

**Supports:** placing long documents or data before the question and instruction, while retaining only relevant context.

Anthropic explicitly recommends placing long-form data above queries and instructions for large inputs. *Lost in the Middle* reports that performance is often strongest when relevant information occurs near the beginning or end of a long context and weaker when it is in the middle. Chroma's controlled experiments across 18 models report uneven quality degradation as input length grows.

**Status:** official documentation plus research. The skill's roughly 2k-token threshold is a project heuristic, not a scientifically established boundary.

**Sources:**
- [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Liu et al. — Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [Chroma Research — Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://trychroma.com/research/context-rot) — an industry research report with published code, not a peer-reviewed paper.

<a id="src-reasoning-high-level"></a>
### [src:reasoning-high-level]

**Supports:** giving reasoning models a clear goal, constraints, and output contract without prescribing a detailed private sequence of intermediate steps.

OpenAI states that reasoning models generally work better with high-level guidance and recommends a clear goal, strong constraints, and an explicit output contract instead of prescribing every intermediate step.

**Status:** official OpenAI documentation; transfer to other model families requires their own documentation.

**Sources:**
- [OpenAI — Reasoning models](https://platform.openai.com/docs/guides/reasoning)
- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)

### [src:model-specific]

**Supports:** applying vendor-specific settings only to a known target model and using a portable profile otherwise.

OpenAI distinguishes prompting for reasoning and GPT models. Anthropic documents XML, long-context placement, adaptive thinking, and the removal of assistant prefill for newer Claude releases. Google separately documents general strategies and Gemini 3 thinking parameters. The DeepSeek-R1 repository documents usage recommendations and evaluation settings for that model.

**Correction in v2.0.1:** unsupported general prohibitions on few-shot and chain-of-thought instructions were removed from the DeepSeek profile. The remaining guidance is limited to documented DeepSeek-R1 behavior and is not transferred automatically to other models.

**Status:** official documentation; version-specific recommendations age quickly and should be rechecked before release.

**Sources:**
- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Google — Gemini 3 developer guide](https://ai.google.dev/gemini-api/docs/gemini-3)
- [DeepSeek-AI — DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)

<a id="src-self-correction"></a>
### [src:self-correction]

**Supports:** not treating self-critique without external feedback as reliable verification; preferring tests, execution, tools, or ground truth.

Huang et al. study intrinsic reasoning self-correction without external feedback and report that models struggle with it and can degrade answers after self-correction. This does not prohibit iterative improvement with an external signal and does not establish that all reflection is useless on every current model.

**Status:** research; the skill deliberately limits the claim to the absence of an external signal.

**Source:**
- [Huang et al. — Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798)

### [src:structured-reasoning]

**Supports:** avoiding automatic rigid formatting constraints on the process of complex reasoning and separating solving from final formatting when the trade-off matters.

Tam et al. compare free and constrained generation and report reduced reasoning quality under format constraints, with stricter constraints generally producing greater degradation. This does not mean Structured Outputs or JSON are harmful for extraction; the risk concerns tasks where format constraints compete with complex reasoning.

**Correction in v2.0.1:** the unsupported `reasoning`-field workaround was removed. The skill recommends separating task solving from final formatting and, when useful, requesting a concise, verifiable rationale instead of private chain-of-thought.

**Status:** research; stage separation is a project decision used only when a task genuinely needs both reasoning and strict structure.

**Source:**
- [Tam et al. — Let Me Speak Freely?](https://arxiv.org/abs/2408.02442)

### [src:prompt-injection]

**Supports:** treating documents, web pages, tool output, and quotations as data rather than new trusted instructions, without claiming that prompt rewriting fully prevents prompt injection.

OWASP describes direct and indirect prompt injection, notes the absence of guaranteed prevention, and recommends separating untrusted external content, limiting privileges, and requiring confirmation for high-risk actions.

**Status:** industry security guidance, not an experimental evaluation of every mitigation; project decision.

**Source:**
- [OWASP — LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

### [src:no-cargo-cult]

**Supports:** not adding tips, threats, and similar emotional amplifiers as a universal prompt-improvement technique.

Meincke et al. tested threats and promised tips on GPQA Diamond and a subset of MMLU-Pro. They found no consistent significant average improvement, although individual questions were sensitive to wording. This supports removing those techniques as unreliable cargo cult; it does not imply that prompt wording never affects results.

**Status:** research.

**Source:**
- [Meincke et al. — Prompting Science Report 3: I'll pay you or I'll kill you — but will you care?](https://arxiv.org/abs/2508.00614)

## Project decisions, not scientific findings

The following rules improve Prompt Compiler's controllability but are not presented as proven universal optima:

1. **Compile → stop.** Return the compiled prompt first; execute the underlying task only when explicitly requested.
2. **One clarification question.** Ask one direct question when critical ambiguity blocks a correct result; otherwise make and report a reversible assumption.
3. **Minimum sufficient structure.** The six sections are an available set, not a mandatory template.
4. **No-op is valid.** Return an already sufficient prompt without manufactured changes.
5. **Task classification.** Code / analysis / creative / extraction / research / agentic is project routing, not a scientific taxonomy.
6. **Long-material threshold.** Roughly 2k tokens is a placement heuristic, not a proven boundary.
7. **Non-functional personas.** Rejecting claims such as “expert with IQ 200” is a minimalism policy. Roles that set domain or tone remain valid; Anthropic explicitly recommends role prompting for focus and tone.
8. **Agent-task control.** Call budgets, stop criteria, confirmation thresholds, preambles, durable notes, and compaction are runtime-dependent project controls, not universal properties of a good prompt.

## Claims that require revalidation

The following exploratory claims are intentionally not used as published facts:

- exact percentage gains from “leaner system prompts” for GPT-5.6 without an accessible primary report and method;
- a general few-shot prohibition for DeepSeek-R1; the documented system-prompt recommendation applies only to the relevant R1 version, not all similar models;
- recommendations for unverified model versions by analogy with adjacent releases;
- the claim that placing a `reasoning` field before data fields always removes the format penalty;
- numerical gains from automatic prompt optimizers without reproducing them on Prompt Compiler's own task set;
- a promise of equal quality improvement for every prompt.

Before publication, such claims must either be removed or accompanied by a precise primary source and applicability limits.

## Update rule

When changing model profiles:

1. check the live official documentation for the exact model family;
2. record the verification date;
3. separate vendor guidance from project experience;
4. do not transfer one model or version's behavior to another without a source;
5. do not claim quality gains without a reproducible evaluation on a fixed prompt set.
