# OpenAI and Codex Guidance

Read this adapter only when an OpenAI surface, model, reasoning, speed, lifecycle, subagent, permission, or context control materially affects the task.

## Discover the active controls

Identify the actual surface and authentication path, exposed tool schema, available models and efforts, context inheritance, concurrency controls, and usage accounting. Current official documentation establishes product behavior; the active contract establishes what this agent can execute. If they conflict, report the conflict and limit conclusions to the observed environment.

Resolve exact model identifiers and supported efforts from the active model list and [current model guidance](https://developers.openai.com/api/docs/guides/latest-model). Never invent a version or transfer API availability into Codex. Do not preserve dated model lists, prices, versions, ceilings, or entitlements in durable instructions.

Keep model, reasoning, speed, orchestration, lifecycle, permissions, and authority distinct. A control selection grants no project effect.

## Route native Codex work

When host policy and the exposed spawn tool permit model and effort selection, use those controls for individual workers. Keep the coordinator responsible for integrating their results. A stronger worker can answer a bounded difficult judgment or review; a lighter worker can handle clear extraction, exploration, or repeatable checks. A different worker model does not require switching the coordinator.

Check configuration precedence before claiming a selection took effect. Codex resolves model and effort from explicit spawn values, then corresponding `[agents]` defaults, then the parent. A custom agent file's explicit values override that resolution. Selecting a model through spawn or defaults with no explicit or configured effort uses that model's default effort; a custom file setting only `model` preserves the already-resolved effort. Verify that effort is supported. Inspect relevant configuration only; do not change user defaults to route one task. See [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Choose the smallest sufficient context using controls actually exposed. If `fork_turns` is available, follow its current schema: provide a self-contained packet for no history, enough recent turns for a partial fork, or full history when continuity is necessary. If full forks require inherited model and effort, omit overrides; use a permitted bounded fork for a different-model worker. Do not assume another client's fork controls exist here.

Use existing workers for closely related follow-ups, and inspect completion before consuming results. Where the tools distinguish them, messaging supplies information, follow-up assignment starts work, waiting receives updates, and interruption stops an active turn without deleting the worker. Interrupt obsolete work; close completed workers only when the host exposes that control. Avoid repeated unchanged polling.

Check available capacity across descendants and coordinate shared files or state. Subagents do not acquire additional task authority. Follow the active sandbox and approval contract; a role declaration alone does not prove enforced isolation.

## Separate API orchestration mechanisms

Choose only a mechanism provided by the selected runtime:

- **Responses Multi-agent beta:** hosted subagents share the request's model and tools. This establishes same-model parallel delegation, not per-child heterogeneous routing. Check current model eligibility and beta requirements. Concurrency caps active descendants, not total agents or aggregate usage. Automatic compaction operates independently per agent; standalone compaction, reasoning summaries, and `max_tool_calls` are unsupported in this mode. See [Responses Multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent).
- **Agents API:** the managed Codex harness coordinates separate subagent contexts with a shared environment when configured. Subagents inherit MCP, web search, and environment capabilities but do not support application function tools. Its guide does not establish child-model selection; verify an exposed selector before proposing heterogeneous workers. See [Agents API Multi-agent](https://developers.openai.com/api/docs/guides/agents-api/multi-agent).
- **Agents SDK:** application-defined specialists can use different models. Use agents-as-tools when the manager must retain integration and reply ownership; handoffs transfer conversation ownership to the specialist. These require application wiring, not merely a skill instruction. See [models and providers](https://developers.openai.com/api/docs/guides/agents/models) and [orchestration](https://developers.openai.com/api/docs/guides/agents/orchestration).
- **Sign in with ChatGPT:** plan-backed API/app-server routes have separate field and state restrictions. Do not infer support for API-paid Multi-agent or budget controls. See [preview limitations](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations).

## Choose controls by expected value

Retain a suitable active configuration unless a change offers a concrete quality, capability, isolation, or latency benefit. Honor explicit choices. Compare total successful-task usage, including coordinator and workers, reasoning, tools, retries, and integration effort. Smaller per-token prices and parallel execution do not prove lower task cost. Use available measurements; disclose estimates and missing accounting.

For subscription-backed Codex, verify applicable limits or credits rather than translating API rates into subscription consumption. For speed, distinguish faster inference from a different model or orchestration mode and inspect [current speed guidance](https://learn.chatgpt.com/docs/agent-configuration/speed). Do not add unavailable controls or extra approval gates.

## Preserve lifecycle and permission boundaries

Use Plan or Goal only when supported and permitted by the host's activation rules. Where Goal requires an explicit request, ordinary task authorization is insufficient. These modes, persistence, speed, and Auto-review grant no additional actions or retries.

Let eligible mechanical permission review operate inside the task envelope. It cannot enlarge authority or convert denial into permission. Continue through permitted native tools when a control is unavailable. See [agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security).

## Keep context and returns lean

Pass the outcome, necessary authoritative evidence, material constraints, done conditions, and concise expected return. Preserve evidence references and decisions across handoffs; omit unrelated history and repeated generic behavior.

For API workflows, maintain one primary continuation strategy to avoid duplicated history. Preserve stable reusable prefixes while keeping changing task material separate; caching reduces repeated input work, not total output or orchestration cost. Check runtime-specific compaction compatibility before pruning. See [SDK state](https://developers.openai.com/api/docs/guides/agents/running-agents), [prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching), and [compaction](https://developers.openai.com/api/docs/guides/compaction).
