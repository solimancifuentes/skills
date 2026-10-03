# SPARC

Choose suitable models and coordination, and match review, authorization checks, and recovery to the concrete effects of a project action.

## Installation

```sh
npx skills add solimancifuentes/skills --skill sparc
```

## Process

1. Establish the requested outcome, existing authority, controlling policy, and strongest current evidence.
2. Assess the next action's reversibility, affected systems, and possible consequences. Use Routine, Guarded, and Consequential as working defaults.
3. Choose direct work, consultation, delegation, or independent parallel work when the route materially affects quality, latency, or cost. Apply the review and checks needed for the action's effects, then carry out work already covered by the request.
4. Verify the result and any material external effects. Resolve an uncertain external outcome before attempting another change.

## When to use it

SPARC stands for Spec-Driven Planning, Authority-Aware Routing, and Coordination. It fits work where model choice or coordination materially affects quality, latency, or cost, or where permissions, review state, release effects, or failure recovery change what should happen next. Supply the task, relevant policy, current state, and any known constraints. Ordinary implementation does not need this framework merely because it happens in a repository.

The result can be a reviewed plan, a focused recommendation, authorized execution, or a prompt for another context. Evidence and unresolved decisions accompany the requested result without a mandatory audit record.

For example, one coordinator can retain the plan and integration, consult a stronger model on an unresolved design choice, and delegate bounded research to suitable workers. Small or coupled work can stay with one agent. Parallel work may save time while consuming more tokens; judge efficiency across the completed outcome, including verification and integration.

The core is model- and harness-agnostic. Routing needs the controls actually exposed by the environment; the skill does not create model access or orchestration tools. Optional OpenAI/Codex and Claude Code references explain their platform mechanics. Other hosts can apply the same decision rules through supported native controls. Interface metadata is optional, and the installer and host determine discovery and invocation.

## Keep approvals tied to effects

Existing authorization remains valid across the stages it covers. A read-only request stays read-only, while recommendations can describe options that need additional authority to execute. A timeout does not prove an external operation had no effect. Optional host guidance applies only to supported controls and cannot grant permission for project actions.

[Full instructions](SKILL.md) · [MIT license](LICENSE)
