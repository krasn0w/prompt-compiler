# Gemini profile (Google)

Last checked: 2026-10-07

Applies to: Gemini 3.x. Current generally available model: Gemini 3.8 Flash (`gemini-3.8-flash`). Also in service: Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, Gemini 3.1 Pro preview.

Sources:

- [Gemini latest model guide](https://ai.google.dev/gemini-api/docs/latest-model)
- [Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)

## Prompt text

- **Clear and specific:** state instructions, constraints, and the response format explicitly.
- **Examples:** few-shot examples work as a specification of the response pattern; add them only when they fix format or behavior.
- **No prefilled model turns:** remove them when migrating to Gemini 3.8 Flash.
- **Length on long tasks:** Gemini 3.8 Flash uses more tokens on long, complex tasks by design (smaller steps, verification along the way). For everyday tasks, lower the thinking level rather than prompting for brevity.

## Not re-verified

Earlier Gemini 3 guidance described short, direct instructions, terse answers by default (ask for detail explicitly), and one structuring style per prompt (XML or Markdown, not mixed). These points were not re-verified on the last check date. Treat them as hints, not rules.

## Runtime parameters

Mention these only in the output's runtime-parameters block.

- **thinking_level:** low, medium (default), high. `minimal` returns an error on Gemini 3.8 Flash. `thinking_budget` is replaced by `thinking_level`.
- **Sampling:** remove temperature, top_p, and top_k. `candidate_count` is not supported from Gemini 3.
