# SPARC

Match review, authorization checks, and recovery procedures to the concrete effects of a project action.

## Installation

```sh
npx skills add solimancifuentes/skills --skill sparc
```

## Process

1. Establish the requested outcome, existing authority, controlling policy, and strongest current evidence.
2. Assess the next action's reversibility, affected systems, and possible consequences. Use Routine, Guarded, and Consequential as working defaults.
3. Choose only the review depth, checks, and coordination needed for those effects, then carry out work already covered by the request.
4. Verify the result and any material external effects. Resolve an uncertain external outcome before attempting another change.

## When to use it

SPARC stands for Spec-Driven Planning, Authority-Aware Routing, and Coordination. It fits work where permissions, review state, release effects, or failure recovery change what should happen next. Supply the task, relevant policy, current state, and any known constraints. Ordinary implementation does not need this framework merely because it happens in a repository.

The result can be a reviewed plan, a focused recommendation, authorized execution, or a prompt for another context. Evidence and unresolved decisions accompany the requested result without a mandatory audit record.

## Keep approvals tied to effects

Existing authorization remains valid across the stages it covers. A read-only request stays read-only, while recommendations can describe options that need additional authority to execute. A timeout does not prove an external operation had no effect. Optional host guidance applies only to supported controls and cannot grant permission for project actions.

[Full instructions](SKILL.md) · [MIT license](LICENSE)
