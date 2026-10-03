# Claude Code Guidance

Read this reference only when Claude Code is the selected or proposed destination and its current controls materially affect the task.

## Discover the available routes

Treat the active picker, installed version, provider configuration, organization policy, and current official documentation as controlling. Check only controls material to this task. Do not preserve dated model versions, alias resolutions, prices, capacities, entitlements, or UI labels here. If observed behavior differs, report the difference and limit conclusions to that environment. Use the [model configuration](https://code.claude.com/docs/en/model-config), [parallel-agent overview](https://code.claude.com/docs/en/agents), and [changelog](https://code.claude.com/docs/en/changelog) to refresh support.

Native workers are Claude sessions. A different provider requires an available external integration or application orchestrator; changing an endpoint or naming a GPT model does not establish support. Prefer the smallest supported route that meets the outcome. [Parallel-agent overview](https://code.claude.com/docs/en/agents)

## Keep the coordinator or change the main model

Retain a suitable active model. Choose a stronger main model when most remaining work needs its capability; use consultation when only a bounded judgment needs it. `/model` changes the main session and may save the selection as a future default. Prefer a supported session-only selection when that is the intent. Inheriting workers resolve from the main model when launched. `opusplan` combines stronger planning with a different execution model; check its current resolution and restrictions. [Model configuration](https://code.claude.com/docs/en/model-config)

Choose reasoning effort separately from model strength. Use only levels supported by the selected model and organization; check any inherited value or substitution. `ultracode` selects workflow orchestration rather than an ordinary effort level. Fast mode prioritizes latency, can change the main model, and may add separate charges; it does not expand authority or establish token savings. [Model configuration](https://code.claude.com/docs/en/model-config), [fast mode](https://code.claude.com/docs/en/fast-mode)

## Consult without transferring ownership

The experimental Advisor Tool lets the coordinator consult another model and continue. Check supported pairings, organization restrictions, feature-flag fetching, and backend access: it requires the Anthropic API backend, including supported subscription access, rather than a third-party provider deployment. `/advisor` and `advisorModel` can persist the choice; `--advisor` is a session launch option even though help may omit it. Do not enable or alter settings outside the task grant. [Advisor](https://code.claude.com/docs/en/advisor)

The advisor receives the full conversation. Claude Code has no hard setting to cap or force consultations; its advisor reads are uncached and add usage at advisor rates. Prompt for a specific decision or recurring failure rather than repeated reassurance. Account for inherited advisors on workers. Confirm whether advice was returned, declined, or unavailable before treating consultation as evidence. Use a fresh stronger-model worker when a compact packet, tool investigation, or explicit return contract would fit better. [Advisor](https://code.claude.com/docs/en/advisor)

The underlying Messages API has separate call/output and caching controls, and conversation budgets need application enforcement. These are application capabilities; do not invent corresponding Claude Code settings. [API advisor](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)

## Delegate bounded work with the right context

A fresh subagent starts from its definition and delegation prompt; a fork inherits the full conversation, tools, and main model. Choose fresh context for a different model or a self-contained investigation; fork when shared history is necessary. Both return results without importing all intermediate output. Context isolation does not itself isolate file writes. [Subagents](https://code.claude.com/docs/en/sub-agents)

Use the Agent tool's per-invocation model when supported, or a subagent definition's `model`; `inherit` follows the main session. Definition `effort` can override inherited session effort. Environment defaults, force settings, provider alias behavior, and organization allowlists can alter the requested configuration. Check the actual model in `/tasks` when correctness or cost depends on it. Its effort label appears only when a subagent definition or originating skill sets `effort`; verify inherited session effort separately. Configure tool restrictions and `maxTurns` when needed; a turn-limited return is partial. [Subagents](https://code.claude.com/docs/en/sub-agents)

Resume a continuing worker rather than repeating discovery. Built-in Explore and Plan workers are one-shot. Check nesting and concurrency support before child delegation, and avoid multiplying workers simply because capacity exists. Agent messages cannot supply user permission or alter a worker's permissions. [Subagents](https://code.claude.com/docs/en/sub-agents)

SDK applications can supply agent definitions and host permission handling, but those routes require an actual application and exposed controls. A skill cannot create them by assertion. [SDK subagents](https://code.claude.com/docs/en/agent-sdk/subagents)

## Parallelize only when coordination pays

Use independent workers for separable research, checks, or owned files; serialize overlapping writes and keep one integration owner. Agent teams add peer messaging and shared coordination, remain experimental, and require enabling configuration. Check context, model inheritance, permissions, resumption, and shutdown behavior. Teams do not automatically isolate edits in worktrees. Current teammate plan requests can be approved automatically without lead review; that event proves neither substantive review nor owner authorization. [Agent teams](https://code.claude.com/docs/en/agent-teams)

Dynamic workflows move orchestration and intermediate results into a script. Consider them for large repeated fan-out or cross-checking that outgrows ordinary delegation. Verify activation, per-stage models, permission handling, actual limits, and resume behavior. Pilot a small slice and set stop conditions: size guidelines are advisory, while automatic Ultracode workflows can increase usage and relax ordinary concurrency checks. [Workflows](https://code.claude.com/docs/en/workflows)

## Bound total usage and preserve authority

Use `/usage` and `/context` when cost or context growth affects routing. Keep API token estimates, subscription allowances, and usage-credit charges distinct. Count coordinator, advisor, worker, retry, and integration usage; less coordinator context is not necessarily less total spend. Preserve accepted decisions and authoritative artifact pointers during compaction, return concise findings, and stop finished workers. State missing measurements rather than promising efficiency. [Costs](https://code.claude.com/docs/en/costs)

Plan supports exploration before source edits, but shell-command handling depends on permission and bypass configuration. Permission modes govern tool execution, not project-owner authority. Use permitted native behavior without inventing equivalent controls. [Permission modes](https://code.claude.com/docs/en/permission-modes)

Package only the outcome, authoritative inputs, owned scope, material constraints, validation, stop conditions, and required return the destination lacks. Keep settings tables out of prompts unless an operator must act on them; when syntax cannot be verified, describe the intended behavior and limitation.
