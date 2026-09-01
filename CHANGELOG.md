# Changelog

**English** · [Русский](CHANGELOG.ru.md)

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

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
