# Changelog

**English** · [Русский](CHANGELOG.ru.md)

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [3.0.0] — 2026-10-07

### Added

- Model profiles loaded on demand from `references/models/` (Claude, OpenAI GPT, Gemini, DeepSeek), each with sources and a check date.
- Explicit action level (inform, plan, change) and an `Autonomy` section with a finish line and stop policy for agentic prompts.
- Replacement of requests to write out reasoning with a short rationale.
- Marking of user-pasted content for Claude targets.
- Design and research adaptations: user-named patterns to avoid; marking of unconfirmed findings.
- Optional runtime-parameters block in the output.
- Precedence of the user's explicit instructions over the skill.
- Regression case set in `tests/regression/cases.md`; deterministic checks for profiles and description length.

### Changed

- Shorter skill description with one exclusion.
- Claude profile updated for Claude 5.x; OpenAI profile for GPT-6 and GPT-5.6; Gemini profile for Gemini 3.x; DeepSeek profile split into V4 and legacy R1.
- Long-context placement attributes the 20k+ token threshold to vendor guidance and keeps ~2k tokens as the project default.
- Thinking and verification instructions are calibrated per model instead of added by default.
- Evidence map: twelve new claims; the GPT-5.6 lean-prompt figures moved from revalidation to a directional vendor claim.

### Removed

- Restating key constraints at the end of long prompts.
- "Consider / evaluate instead of think" as a general Claude rule; it remains only for Claude Opus 4.5 with thinking off.
- Sampling-parameter advice outside the legacy DeepSeek-R1 section.

### Migration

- Install the whole project directory: `SKILL.md` alone no longer carries the model profiles.

## [2.1.0] — 2026-09-01

### Added

- Full English and Russian documentation sets.
- Language navigation in README, annotation, changelog, and evidence map.
- Deterministic checks for bilingual file parity and navigation.

### Changed

- English is now the primary GitHub documentation language.
- Russian documentation remains a complete first-class version in `*.ru.md` files.

## [2.0.1] — 2026-09-01

### Added

- Public project documentation and annotation.
- A traceable evidence map with applicability limits.
- Deterministic project checks and GitHub Actions.

### Changed

- Authorship clarified as Nikolay Krasnov (`krasn0w`) and Hermes Agent.
- The DeepSeek-R1 profile was limited to documented recommendations; the unsupported few-shot prohibition was removed.
- Strict output formatting was separated from complex reasoning without requesting private chain-of-thought.

## [2.0.0] — 2026-08-02

### Added

- Seven-stage compilation pipeline.
- Adaptation by task type and target model.
- Default `compile → stop` behavior.
- Valid no-op for already sufficient prompts.
- Checks for critical ambiguity, contradictions, and prompt-injection boundaries.
