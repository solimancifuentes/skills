# OpenAI and Codex Guidance

Read this reference only when an OpenAI surface or Codex model, reasoning, speed, Plan, Goal, subagent, permission, or prompt-capacity control materially affects the task.

## Refresh current controls

Treat the active product UI and current official OpenAI documentation as controlling. Availability varies by surface, account, workspace, organization, region, and rollout. Do not preserve dated model lists, prices, versions, limits, control labels, or entitlements in durable project instructions.

Use current official sources, including:

- https://developers.openai.com/api/docs/guides/latest-model
- https://developers.openai.com/api/docs/guides/model-selection
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/agent-configuration/speed
- https://learn.chatgpt.com/docs/agent-approvals-security
- https://learn.chatgpt.com/docs/changelog

If visible behavior conflicts with documentation, report the conflict and limit the conclusion to the observed environment.

## Choose controls by expected value

Apply SPARC's expected-value rule. Use the active surface when its continuity and tools are sufficient. Change surface, model, reasoning, speed, permissions, or lifecycle mode only for a concrete capability, isolation, latency, quality, or artifact need.

For API comparisons, use total workflow usage and applicable pricing, including reasoning tokens, caching, tools, and retries where billed. Per-token price alone does not establish cost per successful task. For subscription-backed Codex use, verify the applicable usage limits or credits; do not translate API rates into subscription consumption or treat included access as unlimited. Availability in the API does not establish availability in Codex or the selected harness. When cost, latency, or quality evidence is missing, state what the recommendation depends on without inventing measurements.

Keep model, reasoning, speed, lifecycle state, orchestration, permissions, and authority distinct. A control selection never grants a project effect.

## Use lifecycle and permission controls correctly

Use Plan when currently supported, permitted by the host's activation rules, and useful for investigation or approach review before edits. Use Goal only when supported and authorized under those rules, after the approach, authority, and completion conditions are settled. Where Goal requires an explicit user request, ordinary task authorization is insufficient; do not activate it automatically. Plan, Goal, persistence, speed, and Auto-review do not grant retries or external actions.

Let eligible mechanical permission review operate within the current task envelope when the host provides it. It cannot enlarge the envelope, override higher policy, convert a denial into permission, or authorize a human-reserved effect. If a lifecycle or review control is unavailable, continue through permitted native tools without claiming that control was used.

## Keep prompts lean

Start with the outcome, task-specific authoritative context, material constraints, and done conditions. Do not repeat generic Codex behavior, every visible setting, or undocumented capacity limits. Mention controls only when the destination must act on them.
