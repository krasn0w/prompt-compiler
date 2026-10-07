# OpenAI GPT profile

Last checked: 2026-10-07

Applies to: GPT-6 Astra (`gpt-6-astra`), GPT-6.1 Sol (`gpt-6.1-sol`), GPT-6 Sol (`gpt-6-sol`), GPT-6 Luna (`gpt-6-luna`); GPT-5.6 Sol (`gpt-5.6-sol`, alias `gpt-5.6`), GPT-5.6 Terra (`gpt-5.6-terra`), GPT-5.6 Luna (`gpt-5.6-luna`). For older GPT-5.x models, see "Previous models" in the first source.

Sources:

- [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model) — includes the GPT-5.6 guidance.
- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) — OpenAI blog; used only where marked.

OpenAI describes the GPT-6 behaviors below as observed on GPT-6 Astra and offers them as a starting point for the whole family. Apply only the items that match the task.

## All current GPT models

- **Lean prompts:** state each instruction once; remove repeated rules and examples that encode no requirement. In OpenAI's internal coding-agent runs, leaner system prompts scored roughly 10–15% higher with 41–66% fewer tokens; OpenAI calls the ranges directional.
- **Goal over steps:** give the goal, domain context, hard constraints, approval boundaries, and success criteria rather than every step. Say which ambiguity should trigger a question.
- **Autonomy by request type, stated once:** requests to answer, explain, review, diagnose, or plan → inspect and report, no implementation. Requests to change, build, or fix → make in-scope local changes and run non-destructive validation without asking. External writes, destructive actions, purchases, and material scope expansion → confirm first. Name the safe local actions (reading files, editing in-scope code, running tests).
- **Tone:** describe concrete writing choices (state the answer directly; acknowledge a reported problem before the next step; no generic praise) rather than labels such as "friendly".
- **Short answers:** say what a short answer must keep (conclusion, supporting evidence, material caveat, next action) and what goes first when trimming.
- **No "think harder":** depth is set by reasoning effort and, on GPT-5.6, by pro mode; the prompt stays the same.

## GPT-6 Astra (starting point for the GPT-6 family)

- **Initiative:** Astra asks more often and can stop at a first implementation. Define completion up front, including running, inspecting, and fixing when that is wanted. Tell it to treat "can you…", "I want to…", "help me…" as requests to act when context implies it.
- **Approval as the last step:** let it finish authorized work so that the user approves a concrete, reviewable result. Reversible, read-only, and review work needs no permission. Do not add warnings or approval flows for hypothetical risk.
- **Inherited boundaries:** strong "ask first" wording written for earlier models makes Astra stop early. Keep only the boundaries the user actually needs (blog).
- **Instruction priority:** Astra follows skills and files such as `AGENTS.md` closely and may pause on conflicting guidance. State that the user's instructions take precedence over skill guidance.
- **Writing style:** it tends toward lists, tables, and recurring stock phrases. When the user wants prose, ask for paragraphs that each develop one idea, lists only for parallel or sequential items, plain words, and the main point first.
- **Subagents:** it may delegate less than wanted. When parallel work is wanted, say when and how much to delegate, and ask that messages between agents stay legible.
- **Tests:** it tests thoroughly. For small reversible changes, say not to write tests that mirror the implementation and not to repeat checks without a new reason.
- **Reading:** point to documents by purpose ("use X for service boundaries") instead of "read all docs before every edit" (blog).

## GPT-5.6

- **Concise by default:** a broad "be concise" can make answers too brief; keep it only when it reliably helps.
- **Proactive:** define what each request authorizes so it continues safe work and stops before external or destructive actions.
- **Intent:** it infers the intended level of work well; do not prescribe every step.

## Runtime parameters

Mention these only in the output's runtime-parameters block.

- **reasoning.effort:** GPT-6.1 Sol accepts low, medium (default), high, xhigh, max; GPT-6 Astra and GPT-6.1 Sol do not accept `none`; GPT-6 Sol and GPT-6 Luna do. GPT-5.6 accepts none through max; start at medium.
- **Sampling:** with reasoning effort other than `none`, do not set temperature, top_p, or top_logprobs.
- **text.verbosity:** low, medium, or high as the default level of detail.
- **Pro mode (GPT-5.6):** `reasoning.mode: "pro"` for hard, quality-first tasks; no prompt change is needed.
- **API:** tool calling on GPT-6 Astra and GPT-6.1 Sol requires the Responses API.
