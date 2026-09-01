# Prompt Compiler

**English** · [Русский](README.ru.md)

Prompt Compiler turns a raw request into a minimal, clear, executable prompt for a target language model. It is a skill for [Hermes Agent](https://github.com/NousResearch/hermes-agent), not a standalone application or DSL.

> Current version: **2.1.0** · License: **MIT** · Skill language: **English** · Responses follow the user's language.

## Why

The skill preserves the user's goal, tone, and constraints while removing material ambiguity, contradictions, and template noise. It adds context, output requirements, and observable success criteria only when they make the task more executable.

Detailed overview: [ANNOTATION.md](ANNOTATION.md).
Evidence map: [references/sources.md](references/sources.md).

## Core properties

- **Minimum sufficient prompt:** empty or obvious sections are omitted.
- **Intent preservation:** no invented facts, requirements, preferences, or permissions.
- **Compile → stop:** by default, the skill compiles the prompt but does not execute the underlying task.
- **No-op is valid:** an already sufficient prompt is returned unchanged.
- **Task adaptation:** code, analysis, creative work, extraction, research, and tool-using agents.
- **Model adaptation:** Claude, GPT, Gemini, and a documented DeepSeek-R1 profile; unknown models receive a portable prompt.
- **Safety boundaries:** external content is treated as data, not as trusted instructions.

## Installation

Copy the project directory into your Hermes user skills directory:

```text
%LOCALAPPDATA%\hermes\skills\software-development\prompt-compiler\
```

On Linux/macOS, use `$HERMES_HOME/skills/software-development/prompt-compiler/` or `~/.hermes/skills/software-development/prompt-compiler/`.

Only `SKILL.md` is required at runtime. The other files provide documentation, evidence, and project checks.

## Usage

Invoke the skill by name or explicitly ask to improve a prompt:

```text
Use prompt-compiler and turn this request into a precise prompt: ...
```

By default, the response contains a copy-ready prompt, a short list of material changes, and only relevant assumptions. To run the underlying task immediately, explicitly ask: “improve the prompt and execute it.”

## How it works

1. Identifies the primary goal and task type.
2. Preserves sufficient detail and the user's voice.
3. Finds only material gaps and contradictions.
4. Adds only necessary sections: `Goal`, `Context`, `Inputs`, `Requirements`, `Output`, `Success criteria`.
5. Adapts to the task and known model family.
6. Removes repetition, cargo-cult prompting, and unverifiable requirements.
7. Returns the compiled prompt and stops.

## Evidence base

The rules draw on official Anthropic, OpenAI, Google, and DeepSeek documentation; research on long context, self-correction, and constrained output; and OWASP guidance on prompt injection. Sources are classified by evidence strength, while the project's own architectural choices are labeled separately.

The project **does not promise a universal quality gain**. Effects depend on the model and task and should be tested on a representative prompt set.

## Project checks

```bash
python tests/check_project.py
```

The check makes no LLM calls and has no third-party dependencies. It validates frontmatter, version consistency, required files and sections, local links, language navigation, and the absence of known unsupported legacy claims.

## Versioning

The project follows [Semantic Versioning](https://semver.org/). Changes are recorded in [CHANGELOG.md](CHANGELOG.md), and published releases are preserved as Git tags.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
