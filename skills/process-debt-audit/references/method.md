# Process Debt Audit Method

Use this reference only for a complex, disputed, or cross-project audit. The main skill is sufficient for smaller assessments.

The repository, CI, release, pull-request, and agent examples describe software delivery. Apply them only where the audited workflow has those activities; operational audits may have different evidence, owners, and controls.

## Evidence map

Build the minimum useful map; do not create a data-collection project.

| Evidence | What it can establish | Common limitation |
|---|---|---|
| Operator account | Friction, cognitive load, waiting, repetition, and actual human effort | Recall is qualitative unless time records exist |
| Current conversation | Decisions, prompts, approvals, failures, and agent behavior in context | May omit work in other threads or tools |
| Prior task history | Recurring patterns, rework, stop conditions, and evolving policy | Access may be partial or summarized |
| Repository/directory | Product size, tests, governance surfaces, automation, and current rules | Lines and files do not measure labor |
| Version-control history | Change categories, churn, sequencing, and concentration over time | Commits differ in size and squash merges compress work |
| Issues and pull requests | Handoffs, reviews, status tracking, and duplicated records | Recorded activity may not reflect operator time |
| CI and release tooling | Automated gates, duplication, timing, artifacts, and retry behavior | Hosted configuration may be inaccessible |
| Skills, prompts, and policies | Explicit workflow requirements and authority boundaries | Usage does not prove causation |

State which evidence was directly inspected. Separate exact counts from estimates and inferences.

## Root-cause taxonomy

Use the smallest set that explains the observed debt.

### Risk misclassification

Low-risk changes inherit the controls for credentials, publication, platform compatibility, or other worst-case changes. A checksum change, documentation edit, or dev-only dependency may trigger full release validation without a causal path to the affected risk.

### Duplicated validation

The same property is checked by local commands, CI, manual review, host testing, and evidence reconciliation without each layer catching a distinct failure class.

### Evidence duplication

Issues, comments, checklists, matrices, payload files, hashes, reports, and chat summaries reproduce the same state. Evidence is maintained for its own sake rather than to support a decision or recovery need.

### Workflow fragmentation

One coherent change is split across stages, prompts, workspaces, issues, or agents. Context transfer and state reconciliation cost more than the isolation prevents.

### Approval granularity

Humans approve reversible commands, deterministic checks, or every stage transition. Authority is narrower than the risk requires, creating queues and repeated prompt construction.

### Failure amplification

A test, audit, shell, network, or candidate-build failure becomes terminal even though state is reversible and a correction would be safe. Fail-closed reasoning is applied before an irreversible action exists.

### Toolchain and dependency gaps

Agents repeatedly encounter the same missing module, executable, runtime, plugin, environment variable, configuration, or incompatible version because the prerequisite is undeclared or stored only in operator knowledge. The recurring workaround costs more than making setup reproducible.

### Late gates

Security, dependency, packaging, compatibility, or release checks run only after expensive downstream validation, causing avoidable invalidation and rework.

### Artifact and documentation coupling

Volatile prose is bundled into or otherwise changes a distributable artifact, so wording changes trigger new identities and validations unrelated to runtime behavior.

### Automation gap

Humans repeatedly perform deterministic checks or transfer evidence because CI, release workflows, or repository policy do not encode the desired behavior.

### Skill or prompt amplification

A skill, prompt, or agent converts a useful principle—such as founder authority or exact identity—into universal ceremony. Confirm whether the written instruction required the behavior or whether the agent extrapolated it.

### Stale or conflicting governance

Historical specifications, templates, policies, and new instructions remain simultaneously active. Agents satisfy all of them, producing the strictest combined workflow.

## Recurring-error analysis

Group errors by verified root cause rather than superficial message text. Redact secrets and customer data from any reported signature.

| Question | Decision value |
|---|---|
| How many independent tasks or attempts show the failure? | Distinguishes recurrence from a one-off event |
| Does it fail in development, CI, release tooling, or only one agent environment? | Identifies the correct remediation scope |
| Is the prerequisite already declared or installed elsewhere? | Separates missing setup from path/runtime selection errors |
| Is the version or command supported by the current tool? | Prevents installing a package to mask incompatible syntax |
| Does the project normally require this capability? | Distinguishes a durable prerequisite from an audit-only convenience |
| Is the failure deterministic or transient? | Avoids permanent dependencies for network or service incidents |
| What new maintenance or supply-chain cost would the fix introduce? | Tests whether prevention is proportionate |

Choose the remediation layer deliberately:

- **Project-local dependency:** The code, tests, build, or standard project tooling requires it. Declare it in the correct dependency class and lock it through the native package manager.
- **Project setup or environment definition:** Contributors and agents need a runtime, system tool, service, or configuration not represented by the language package manifest.
- **CI or reusable environment:** Only automation requires the capability, or a standardized image eliminates repeated setup drift.
- **Skill or agent instruction:** The tool exists, but agents repeatedly choose unsupported syntax, the wrong runtime, or an unavailable execution boundary.
- **User-level tool:** The capability serves many projects and is intentionally managed outside them. Recommend this only when project-local declaration is unsuitable.
- **Upstream fix:** A tool or skill has an undeclared dependency or defect. Prefer fixing the owning component over contaminating every project that uses it.
- **No permanent change:** The failure is transient, non-recurring, or cheaper to handle with a bounded retry.

For each proposed fix, state the observed evidence, confidence, installation or configuration target, expected benefit, side effects, validation, and whether separate mutation authority is required. Do not install or update anything during diagnosis-only work.

## Causal attribution rubric

For each major source of friction, record:

1. **Observed behavior:** What repeatedly happened?
2. **Operator cost:** Waiting, prompts, handoffs, rework, cognitive burden, or blocked delivery.
3. **Stated purpose:** What risk was the control intended to reduce?
4. **Actual risk path:** How could omitting it cause material harm?
5. **Origin:** Project rule, user instruction, skill requirement, agent inference, tool constraint, or legacy practice.
6. **Strength:** Directly caused, amplified, enabled, correlated, or uncertain.
7. **Lean disposition:** Keep, automate, consolidate, risk-tier, or remove.

Do not attribute direct causation without evidence connecting the origin to the behavior.

## Measurement options

Choose only metrics that affect a decision.

### Effort and composition proxies

- Product/runtime, tests, packaging, documentation, governance, and maintenance file or line counts.
- Primary-purpose change counts, with an explicit classification rule.
- Change churn by category.
- Conversation or task volume by activity when accessible.

Do not convert these directly into labor percentages. Present an uncertainty range if estimating effort, and explain the assumptions.

### Flow metrics

- Lead time from request to merged change or released outcome.
- Active work time versus waiting or coordination time.
- Human approvals, handoffs, workspaces, and durable records per change.
- Validation steps repeated for the same revision.
- Rework caused by late gates.
- Routine changes receiving sensitive-change treatment.

### Target-state metrics

Prefer two to five measures:

- Median lead time by risk tier.
- Human interventions per routine and sensitive change.
- Percentage of effort spent on direct product work.
- CI reruns caused by real defects versus process construction errors.
- Recurring prerequisite or tool failures per change.
- Manual host validations per release and the risk that triggered them.
- Duplicate records or canonical process surfaces.

Metrics should validate whether the process is improving, not become another reporting obligation.

## Minimum-sufficient design test

For each proposed gate, ask:

1. What credible failure does it prevent or detect?
2. Is that failure material for this change class?
3. Is another control already detecting it?
4. Can automation perform it reliably?
5. Must it happen on every change, only on sensitive deltas, or only at release?
6. Is the action reversible before a human decision is needed?
7. What is the cost to the operator and delivery time?

Remove or redesign a gate when no concrete answer supports it.

## Quality floor

A lean workflow must not remove controls blindly. Preserve, when applicable:

- Focused tests for changed behavior and one dependable integration gate.
- Security, privacy, credential, and customer-data checks at the affected boundary.
- Platform checks when platform-specific behavior or claims change.
- Production dependency and build-pipeline security appropriate to what ships.
- Exact identity and provenance for a final distributable artifact.
- User authorization or applicable standing authority for irreversible publication, destructive actions, external communication, or unresolved material tradeoffs. Reuse existing grants.

Apply these controls only at the stage and risk tier where they have decision value.

## Target workflow construction

Draft the target from zero:

1. Define ordinary delivery in the fewest steps.
2. Add automated validation for common defects.
3. Add sensitive tiers only for identified boundaries.
4. Add a release path only if the project distributes something.
5. Where an unresolved material decision requires human authorization, place that gate immediately before the action it controls; do not duplicate an existing grant.
6. Give the agent standing authority for routine, reversible work when policy permits.
7. Keep one canonical description and remove or supersede conflicts.

Compare the current and target workflows by steps, handoffs, approvals, manual checks, and expected failure recovery.

## Compact reporting template

Adapt rather than mechanically reproduce this structure:

```text
Judgment
<What is overbuilt, what is justified, and confidence.>

Evidence and limits
<What was inspected, operator evidence, estimates, and unavailable sources.>

Root causes
<Ranked causal chain with attribution.>

Recurring errors and preventive fixes
<Verified repeated failures, correct remediation layer, benefit, and cost.>

Control decisions
Keep: ...
Automate: ...
Consolidate: ...
Risk-tier: ...
Remove: ...

Lean target flow
<Routine path, sensitive path, release path if relevant, and human authority.>

Transition
<Immediate stops, bounded implementation, first real use, and rollback.>

Measures
<Two to five low-overhead outcome metrics.>
```

End with one concrete next move and say where it should be executed. Do not generate an implementation authorization unless the user asks for one.
