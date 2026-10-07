# Prompt Compiler sources and evidence map

**English** · [Русский](sources.ru.md)

Last checked: **2026-10-07**.

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

Anthropic recommends placing long-form data above queries and instructions for inputs of 20k+ tokens and reports that queries at the end improved response quality by up to 30% in its tests. *Lost in the Middle* reports that performance is often strongest when relevant information occurs near the beginning or end of a long context and weaker when it is in the middle. Chroma's controlled experiments across 18 models report uneven quality degradation as input length grows.

**Status:** official documentation plus research. The vendor threshold is 20k+ tokens; the skill applies the same order from roughly 2k tokens as a low-cost project default, not a scientifically established boundary.

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

Since v3.0.0 the profiles live in `references/models/`, each with its own sources and check date. OpenAI distinguishes prompting for reasoning and GPT models. Anthropic documents XML, long-context placement, adaptive thinking, and the removal of assistant prefill for newer Claude releases. Google separately documents general strategies and Gemini 3 thinking parameters. The DeepSeek-R1 repository documents usage recommendations and evaluation settings for that model.

**Correction in v2.0.1:** unsupported general prohibitions on few-shot and chain-of-thought instructions were removed from the DeepSeek profile. The remaining guidance is limited to documented DeepSeek-R1 behavior and is not transferred automatically to other models.

**Changes in v3.0.0:** the Claude profile covers Claude 5.x; the OpenAI profile covers GPT-6 and GPT-5.6; the Gemini profile covers Gemini 3.x and keeps earlier style hints apart as unverified; the DeepSeek profile is split into V4 and the legacy R1 section.

**Status:** official documentation; version-specific recommendations age quickly and should be rechecked before release.

**Sources:**
- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Google — Gemini 3 developer guide](https://ai.google.dev/gemini-api/docs/gemini-3)
- [DeepSeek-AI — DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)
- [Anthropic — Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- [OpenAI — Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)
- [Google — Gemini latest model guide](https://ai.google.dev/gemini-api/docs/latest-model)
- [DeepSeek API — Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode/)

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

<a id="src-action-level"></a>
### [src:action-level]

**Supports:** stating the requested action level (inform, plan, or change) with an explicit imperative.

Anthropic notes that Claude reads "can you suggest some changes" literally and only suggests, and recommends an imperative when action is wanted. OpenAI describes GPT-6 Astra as more likely to ask before acting on an unclear request, and its GPT-5.6 guidance ties each request type (answer, review, plan; change, build, fix; external or destructive action) to what it authorizes. Anthropic's Sonnet 5.5 guide reports that open-ended requests can lead the model to start building when only ideas were wanted.

**Status:** official documentation from two vendors; the three-level split is a project decision.

**Sources:**
- [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Anthropic — Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)
- [OpenAI — Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)

<a id="src-stop-policy"></a>
### [src:stop-policy]

**Supports:** for agentic prompts, an observable finish line, a short list of situations that justify stopping to ask, and an instruction to continue otherwise.

Anthropic reports that Claude Opus 5.5 sometimes ends a long turn with a report instead of the next action, and that it follows instructions naming both unwanted and wanted stops. It advises keeping confirmation for risky actions and leaving "keep going" instructions out of human-in-the-loop applications. OpenAI reports that GPT-6 Astra can stop after a first implementation, recommends defining completion before the work starts, and recommends making user approval the final step on a concrete, reviewable result.

**Status:** official documentation from two vendors; the vendor blogs restate it for Claude Code and Codex.

**Sources:**
- [Anthropic — Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- [Anthropic blog — Getting the most out of Opus 5.5](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)
- [OpenAI — Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)
- [OpenAI blog — Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)

<a id="src-thinking-always-on"></a>
### [src:thinking-always-on]

**Supports:** not adding "think carefully" or "think step by step", removing such lines for models that always reason, and controlling depth with API parameters.

Anthropic states that Claude Opus 5.5 thinks before every reply; in a chat product, removing a "think carefully" line made replies start sooner without a clear drop in quality; lowering effort reduces thinking more reliably than prompt instructions; on Sonnet 5.5 a request to think less does not reliably reduce thinking. OpenAI states that pro mode needs no "think harder" instruction. One documented exception: on Sonnet 5.5, a line asking the model to think the problem through raised accuracy on reasoning tasks with JSON output.

**Status:** official documentation; model-specific, so details live in the profiles.

**Sources:**
- [Anthropic — Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- [Anthropic — Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)
- [OpenAI — Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)

<a id="src-reasoning-extraction"></a>
### [src:reasoning-extraction]

**Supports:** replacing requests to write out reasoning in the response with a request for a short rationale.

Anthropic documents a `reasoning_extraction` refusal category and states that prompts asking Claude Fable 5.x, Opus 5.5, Opus 5, or Sonnet 5.5 to write out their reasoning may be declined, while short explanations and summaries of actions remain allowed. DeepSeek V4 returns its reasoning in a separate field.

**Status:** official documentation; making the replacement a general rule is a project decision, because it costs nothing on other models. Models without thinking keep the documented visible-reasoning fallback through their profile.

**Sources:**
- [Anthropic — Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [DeepSeek API — Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode/)

<a id="src-verification-calibration"></a>
### [src:verification-calibration]

**Supports:** naming a real, proportionate check instead of generic self-checking, and adding verification instructions only when the task or the model calls for them.

Anthropic states that Claude Opus 5 verifies its own work and that carried-over verification instructions cause over-verification, and that Sonnet 5.5 at low effort can report a change as done without a real check. OpenAI states that GPT-6 Astra tests thoroughly and can over-test small changes, while earlier models needed encouragement.

**Status:** official documentation; directions differ by model, so details live in the profiles.

**Sources:**
- [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Anthropic — Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)
- [OpenAI — Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)

<a id="src-lean-prompts"></a>
### [src:lean-prompts]

**Supports:** stating each requirement once and removing repetition.

OpenAI's GPT-5.6 guidance recommends leaner prompts, stating each instruction once, and keeping approval rules in one place, because repeated "ask first" rules cause unnecessary approval requests. It reports that leaner system prompts improved internal coding-agent evaluation scores by roughly 10–15% while cutting total tokens by 41–66%, and calls the ranges directional.

**Status:** official vendor statement; the numbers come from internal evaluations without a published method and are cited as directional only.

**Source:**
- [OpenAI — Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)

<a id="src-sampling-params"></a>
### [src:sampling-params]

**Supports:** not setting temperature or top_p for reasoning models, and keeping such settings out of prompt text.

OpenAI asks to remove temperature, top_p, and top_logprobs when reasoning effort is not `none`. Google asks to remove temperature, top_p, and top_k for Gemini 3.8 Flash. DeepSeek's thinking mode does not support temperature, top_p, presence penalty, or frequency penalty.

**Status:** official documentation from three vendors.

**Sources:**
- [OpenAI — Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)
- [Google — Gemini latest model guide](https://ai.google.dev/gemini-api/docs/latest-model)
- [DeepSeek API — Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode/)

<a id="src-pasted-content"></a>
### [src:pasted-content]

**Supports:** marking text the user pasted from elsewhere when the target is Claude.

Anthropic reports that Claude Opus 5.5 resists instructions inside pasted content when each pasted block is wrapped in tags carrying the same random id and the system prompt explains the tags. The tags can be imitated, so the pattern is one guardrail among others.

**Status:** official documentation for Claude; not transferred to other vendors.

**Source:**
- [Anthropic — Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)

<a id="src-design-negative-list"></a>
### [src:design-negative-list]

**Supports:** listing specific design patterns to avoid, taken only from the user's own words.

Anthropic reports that without design direction Claude Opus 5.5 falls back on a few default styles, that a general instruction to avoid a generic look swaps one default for another, and that a list of specific patterns, refined over iterations, works better.

**Status:** official documentation; taking the list only from the user is a project decision that follows the Core Contract.

**Sources:**
- [Anthropic — Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- [Anthropic blog — Getting the most out of Opus 5.5](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)

<a id="src-research-uncertainty"></a>
### [src:research-uncertainty]

**Supports:** asking research prompts to mark what could not be confirmed, and not discouraging search.

Anthropic's blog recommends asking Opus 5.5 to mark anything it could not confirm and to say where it looked. Anthropic's Sonnet 5.5 guide recommends removing wording that discourages tool use from knowledge-work prompts, because the model may otherwise answer from training data where details have changed.

**Status:** vendor blog plus official documentation.

**Sources:**
- [Anthropic blog — Getting the most out of Opus 5.5](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)
- [Anthropic — Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)

<a id="src-tone-concrete"></a>
### [src:tone-concrete]

**Supports:** expressing tone as concrete writing choices and stating what a short answer must keep.

OpenAI recommends describing the writing choices that define a tone instead of labels such as "friendly", and specifying what a short answer must preserve. It also notes that GPT-5.6 is more concise by default, so broad brevity instructions can make answers too short. Anthropic notes that Claude Opus 5 runs long by default and responds to a short length instruction.

**Status:** official documentation; model directions differ.

**Sources:**
- [OpenAI — Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)
- [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

<a id="src-skill-structure"></a>
### [src:skill-structure]

**Supports:** a short skill description, model profiles loaded on demand, and explicit precedence of user instructions over the skill.

OpenAI's blog advises skill descriptions that are as short as possible while saying clearly when the skill applies, warns that over-emphasized descriptions cause needless loading, and recommends a minimal root document that routes to supporting files. OpenAI's GPT-6 guide recommends stating that user instructions take precedence over skills. Hermes Agent documents loading a file from a skill's `references/` directory with `skill_view(name, file_path)`.

**Status:** vendor blog and documentation. Some skill-authoring guidance favors more emphatic descriptions against under-triggering; this skill keeps a short description with one exclusion because over-triggering (compiling instead of executing) is the costlier failure here. That trade-off is a project decision.

**Sources:**
- [OpenAI blog — Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
- [OpenAI — Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)
- [Hermes Agent — Work with skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)

## Project decisions, not scientific findings

The following rules improve Prompt Compiler's controllability but are not presented as proven universal optima:

1. **Compile → stop.** Return the compiled prompt first; execute the underlying task only when explicitly requested.
2. **One clarification question.** Ask one direct question when critical ambiguity blocks a correct result; otherwise make and report a reversible assumption.
3. **Minimum sufficient structure.** The six sections are an available set, not a mandatory template.
4. **No-op is valid.** Return an already sufficient prompt without manufactured changes.
5. **Task classification.** Code / analysis / creative / extraction / research / agentic is project routing, not a scientific taxonomy.
6. **Long-material threshold.** Roughly 2k tokens is a placement heuristic, not a proven boundary; the vendor guidance it extends targets 20k+ tokens.
7. **Non-functional personas.** Rejecting claims such as “expert with IQ 200” is a minimalism policy. Roles that set domain or tone remain valid; Anthropic explicitly recommends role prompting for focus and tone.
8. **Agent-task control.** Call budgets, stop criteria, confirmation thresholds, preambles, durable notes, and compaction are runtime-dependent project controls, not universal properties of a good prompt.
9. **Action levels.** Inform / plan / change is project routing built on vendor guidance, not a vendor taxonomy.
10. **Runtime-parameters block.** API settings go into an optional output block instead of the prompt text.
11. **Model findings stay in profiles.** A behavior documented for one model is not applied to another without its own source.
12. **Profiles on demand.** Profiles are loaded only for a known target; the portable profile is used otherwise or when loading fails.
13. **Short description with one exclusion.** Chosen because compiling an ordinary request instead of executing it is the costlier failure for this skill.

## Claims that require revalidation

The following exploratory claims are intentionally not used as published facts:

- earlier Gemini 3 style hints (short direct instructions, terse answers by default, no mixed XML and Markdown), kept in the Gemini profile only as unverified hints;
- a special system prompt for a DeepSeek V4 maximum-reasoning mode, reported by third-party sites but not found on the official page;
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
