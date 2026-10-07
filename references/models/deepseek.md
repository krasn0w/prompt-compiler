# DeepSeek profile

Last checked: 2026-10-07

Applies to: DeepSeek V4 (`deepseek-v4-flash`, `deepseek-v4-pro`); DeepSeek-R1 in the legacy section.

Sources:

- [DeepSeek API — Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode/)
- [DeepSeek-AI — DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)

## DeepSeek V4

- **Prompt text:** no official prompting guide for V4 was found on the last check date. Use the portable profile from `SKILL.md` for the prompt text.
- **Thinking:** thinking mode is on by default with effort `high`. The reasoning comes back in a separate `reasoning_content` field, so do not ask for reasoning in the answer and do not add "think step by step".
- **Do not transfer R1 rules:** the R1 items below are not documented for V4.

## Runtime parameters

Mention these only in the output's runtime-parameters block.

- **Thinking toggle and effort:** `thinking.type` enabled or disabled, or `reasoning.effort` none, low, high, max (`none` disables thinking).
- **Sampling:** in thinking mode, temperature, top_p, presence_penalty, and frequency_penalty are not supported.
- **Tools in thinking mode:** the harness must pass `reasoning_content` back on later requests; this is an integration matter, not prompt text.

## Not re-verified

Third-party sites mention a special system prompt for a maximum-reasoning mode. It was not confirmed on the official page; do not apply it.

## DeepSeek-R1 (legacy)

These items apply only to DeepSeek-R1 as documented in its repository:

- No system prompt; put all instructions in the user turn.
- Temperature around 0.6 for sampled benchmark-style evaluation.
- For math, ask for the final answer in `\boxed{}`.
