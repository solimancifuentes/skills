# Claude Code Guidance

Read this reference only when Claude Code is the selected or proposed destination and its current controls materially affect the task.

## Refresh current controls

Treat the active picker, installed version, provider configuration, organization policy, and current official Anthropic documentation as controlling. Do not preserve dated model lists, aliases, capacity, price, versions, or UI labels in durable instructions.

Use current official sources, including:

- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/common-workflows
- https://code.claude.com/docs/en/changelog

If active behavior differs from documentation, report the difference and limit the conclusion to the observed environment.

## Choose controls by expected value

Apply SPARC's expected-value rule to model, effort, speed, permission mode, Plan, and orchestration. Use exact visible supported choices and do not infer an alias resolution, entitlement, or equivalence with another provider.

Use the selected provider's actual billing or subscription-usage rules when comparing task cost. Include measured workflow usage, retries, and review effort where relevant; do not infer subscription consumption from API token prices or assume included access is unlimited. State material gaps in cost, latency, or quality evidence.

Use Plan when the current host supports it, its activation is permitted, and exploration or approach review should precede edits. Permission mode controls tool prompting, not project-owner authority. Speed changes latency, not scope or safety. If a named control is unavailable, use supported native behavior and describe the limitation without inventing an equivalent.

## Package only task-specific guidance

Keep prompts focused on the outcome, authoritative project context, material constraints, validation, stop conditions, and required return. Do not add a settings table unless the operator must act on those settings. When current support or syntax cannot be verified, describe the intended behavior without inventing a command or control.
