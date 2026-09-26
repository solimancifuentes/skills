---
name: sparc
description: "SPARC (Spec-Driven Planning, Authority-Aware Routing, and Coordination) calibrates assurance from concrete effects, preserves task-bound authority, reviews plans and lifecycle state, and qualifies recovery for consequential work across projects and agent surfaces. Use when governance, approval, routing, failure recovery, review depth, or lifecycle effects materially affect the next action. Do not use for ordinary implementation, routine code review, or generic version-control help unless those concerns are material."
---

# SPARC

Coordinate project work when state, authority, routing, or lifecycle effects materially affect what may happen next. Apply the least process that safely proves the requested result.

## 1. Ground in authority and evidence

Follow applicable system, developer, organization, project, repository, and platform policy according to its actual controlling precedence. SPARC cannot waive any higher rule.

Treat the user's request and still-applicable grants in the conversation as the task grant within the authority they hold. Accepted project decisions and contracts control only when the project gives them that status. A recommendation, plan-quality finding, prior report, historical record, or earlier action does not itself create or expand authority.

Resolve factual state from the strongest current source: canonical project records and live platform state; then direct artifacts, diffs, tests, logs, and command results; then current summaries and handoffs; then prior conversation, memory, or general knowledge. Separate observed facts, supported inferences, unresolved possibilities, and recommendations. Stop when controlling sources conflict and their precedence cannot be resolved.

A timeout, transport error, tool exception, or undocumented nonzero exit does not establish absence or a substantive mismatch. Use documented result semantics or authoritative read-only reconciliation; otherwise report NOT ESTABLISHED.

Ask for a decision only when the missing choice changes scope, authority, material effects, or the accepted outcome. Otherwise make a safe low-risk assumption, state it when material, and continue.

### Prevent process ratcheting

A task prompt, returned plan, prior report, or historical evidence record does not become durable governance merely because it contains stricter controls. Durable rules come from controlling project policy or an explicit governance decision. Temporary task controls expire with that task.

Before accepting no-retry, exact-byte, per-stage authorization, exhaustive evidence, or special-boundary requirements, identify the concrete material failure they prevent or the controlling rule they satisfy. Preserve valid explicit user instructions, but distinguish user-selected caution from an inherent technical requirement. If a proposed control is disproportionate, recommend the leaner safe alternative.

## 2. Calibrate assurance from concrete effects

Use these tiers as working defaults for choosing review depth, evidence, gates, and orchestration. Actual effects, the user's request, and controlling policy govern; the labels do not impose a universal approval process:

- **Routine:** reversible local or internal work with bounded effects. Ordinary builds, tests, analysis, packaging, CI, task-branch work, and reversible review-object preparation normally remain here when policy treats them as standard collaboration.
- **Guarded:** sensitive but reversible work affecting privacy, contracts, packaging, platform behavior, credentials handling, permissions boundaries, or other meaningful interfaces. Use targeted safeguards for the boundary that is actually affected.
- **Consequential:** irreversible or destructive external mutation, public or customer-facing publication, production mutation, materially non-idempotent action, or materially ambiguous external outcome requiring reconciliation. This includes production or customer-data mutation; credentials, identity, access, permissions, or security-control changes; harmful duplication or partial-state risk; and any action that controlling policy explicitly places under high assurance.

Use evidence relevant to the action: reversibility and idempotency; local versus external state; production, customer, privacy, credential, permission, or security impact; blast radius; automated coverage; novelty and demonstrated uncertainty; actual platform behavior; and controlling project policy. Reclassify when a later action introduces different effects.

A label alone never determines the tier. Builds, tests, audits, dependency installation, packaging, CI or workflow runs, internal rebuildable candidate artifacts, advisory diagnosis, failed validation, read-only checks, and routine release preparation are not consequential merely by category. Words such as candidate, release, security, production, exact, failure, externally visible, and one-shot are evidence only when the concrete action gives them material meaning.

Every additional gate, record, check, handoff, or human interaction must prevent a concrete material failure, satisfy controlling policy, or produce evidence that can change the action. Otherwise omit it.

## 3. Keep authority task-bound and effects-specific

Treat authority as an envelope limited to the requested outcome, named targets, material effects, and controlling policy. Automatically perform necessary bounded, recoverable, policy-compatible work inside that envelope.

An exact request covering edits, validation, commit, task-branch push, and review-object creation covers that named sequence; do not split its reversible stages into extra approvals. A read-only request remains read-only. Do not infer integration, deletion, synchronization, publication, deployment, release, or follow-on work merely because it is customary.

Check authority especially carefully for canonical or protected-state integration; public or customer-facing publication or release; production or customer-data mutation; secrets, credentials, identity, access, permissions, or security-control changes; destructive or irreversible operations; material spending or legal commitments; and changes to governance, acceptance criteria, outcomes, or material scope. Use an existing grant when it already covers the target and effects. Obtain a new grant only for effects outside that authority or where controlling policy requires separate confirmation; this list does not create a second approval gate.

Preflight, setup, boundary qualification, execution, and postflight may remain distinct reasoning or evidence boundaries. They do not imply separate workspaces, chats, prompts, issues, comments, approvals, or human turns. One task grant may cover all applicable stages whose actions and effects it includes. Ask again only for a new material effect, target, scope, or genuinely unresolved reserved decision.

Before mutation, verify only the exact target, allowed and prohibited effects, and drift-sensitive state needed to avoid a material error. Stop on a material mismatch. Protect secrets and customer data, use native paths where sufficient, and preserve source state by default. Keep one stateful owner for each external or otherwise stateful mutation sequence; independent read-only analysis or non-overlapping local work may be delegated. After every external mutation, perform authoritative readback scoped to its requested and material unavoidable effects.

Every action performed must fit the task envelope. Requested recommendations may discuss changes beyond current execution authority; clearly mark any new grant needed before acting. Offering an option neither executes it nor expands scope.

## 4. Make reversible progress and recovery the default

A known reversible failure may be diagnosed, corrected, and rerun inside the existing task envelope. A mechanical command, parser, validator, shell, or transport-construction defect may be corrected and rerun when the target, semantics, expected condition, and side-effect class remain unchanged.

After a failed external operation, reconcile authoritative state before another mutation. Retry the identical action when reconciliation proves zero effect and the original grant remains applicable. If external state is partial or unknown, reconcile and stop before another mutation. A new target, scope, semantic predicate, or material effect requires appropriate authority.

No-retry or consumed-attempt behavior applies only when controlling policy requires it, a valid explicit task instruction imposes it within the user's authority, or an intrinsically non-repeatable operation could cause harmful duplication or partial external state. A task-specific instruction remains temporary governance for that task. Never infer no-retry from a label, a failed command, a failed test, or an audit result.

Report failures concisely: what was established, material effects, retry status, and the smallest supported next action. Do not expose secrets, raw environments, customer data, unrelated paths, or noisy logs.

Keep proposed, internal, prepared, candidate, validated, published, deployed, and released states distinct. Do not promote a state without evidence.

Read [consequential work guidance](references/consequential-work.md) only after an action is classified **Consequential**, or when controlling policy explicitly requires that reference's safeguards.

## 5. Review and route proportionately

Choose review depth independently from assurance tier. Base it on breadth, novelty, uncertainty, dependencies, automated coverage, contradictions, and the cost of a missed defect. A technically complex Routine change may need deep engineering review without additional authority; a simple Consequential mutation may need exact preflight and postflight without broad analysis.

Use a written acceptance contract only when stable criteria are needed to judge a plan, preserve an exact authorization target, coordinate multiple material requirements, or control consequential execution. Otherwise validate directly against the requested outcome and project policy.

Classify findings as blocking, accepted residual, or non-blocking. Request revisions only for blocking findings. Prefer a bounded delta, reuse still-valid evidence, and stop iterating when the required outcome passes.

Plan approval is a quality finding, not mutation authority. If the original request already grants implementation, all effects remain inside the envelope, and no reserved decision remains, continue without another human round. Planning-only requests remain planning-only.

Use the smallest suitable native surface. Add wrappers, PTYs, transports, or orchestration only for a concrete capability or isolation requirement and validate the added boundary when its behavior matters.

Select model strength, reasoning, speed, lifecycle controls, and orchestration to meet the required quality within the user's constraints, then balance total cost per successful task, latency, retries, and review effort. Honor explicit model and control choices; otherwise retain a suitable active configuration unless a change has a concrete expected benefit. If an explicit choice is unavailable or cannot meet a material requirement, explain the constraint and resolve only the missing decision. Use representative task evidence when available; distinguish measured results from estimates and unmeasured tradeoffs. Do not require a benchmark for ordinary work.

Strong models and high reasoning are appropriate when they materially improve difficult work, not merely because work is lengthy, labeled Deep, or contains many procedural checks. Use supporting agents only when substantial independent workstreams offer more expected quality or elapsed-time benefit than coordination cost. Evidence formatting, duplicate verification, operator-record preparation, prompt restatement, and procedural ceremony are not valuable independent workstreams. Keep one integration owner and serialize overlapping writes.

Read [OpenAI and Codex guidance](references/openai-codex.md) only when an OpenAI control materially affects the task. Read [Claude Code guidance](references/claude-code.md) only when Claude Code is the selected or proposed destination. These are optional host adapters. For other hosts, use available native controls and current official documentation; do not invent equivalents for unsupported features. Lifecycle modes and automatic permission review apply only when the host supports them and their activation is authorized. Read [change lifecycle guidance](references/change-lifecycle.md) for review objects, readiness mutation, integration, deletion, synchronization, or dependent work.

## 6. Keep prompts, evidence, and returns lean

Provide a copyable prompt only when execution in another context is the next useful step or the user requests one. Carry only the outcome, task-specific authoritative context, allowed effects, material constraints, validation, stop conditions, and concise return that the destination lacks. Point to accessible canonical project instructions instead of restating generic agent behavior. Keep private records, account details, source paths, and raw conversations out of shared prompts unless needed and authorized for that destination.

Require the smallest useful evidence format. Use a table only when multiple requirements map to different artifacts or validation sources and the table materially improves the decision. Do not request command counts, poll counts, byte offsets, payload hashes, full mutation inventories, or repeated unchanged-state evidence unless those facts are themselves material.

Require operator evidence only when environmental identity materially affects acceptance, reproducibility, authority, or interpretation. Application version, harness version, model, effort, speed, Plan, Goal, orchestration, and workspace identity are not product evidence unless the result depends on them.

For repository mutations, report the requested result, validation, final cleanliness when material, and any remaining changes. For external mutations, report the requested result, confirmed effects, material residual state, and unresolved blockers. Do not turn completion summaries into audit records.

## 7. Operating loop

1. Resolve controlling policy, current evidence, and the exact task envelope.
2. Classify the next concrete action as Routine, Guarded, or Consequential.
3. Add only controls justified by material effects, evidence, or policy.
4. Load only references relevant to that action.
5. Execute bounded work inside the envelope, including recoverable corrections and reruns.
6. Validate the requested result and authoritative external effects.
7. Return the result, material evidence, unresolved decisions, and the next action only when one remains.

Be concise and operational.
