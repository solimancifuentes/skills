# Change Lifecycle

Read this reference only when work involves a review object, readiness mutation, integration, deletion, synchronization, or dependent follow-on work.

## Use the project's native lifecycle

Identify the actual system and terminology. A project may use pull requests, merge requests, change reviews, direct canonical changes, a non-Git revision system, a document workflow, or no integration object. Do not invent branches, remotes, revisions, readiness states, or review URLs.

For a review object, verify only facts that can change the requested action: project and object identity; source and destination; changed material; required checks or reviews; unresolved blockers; and configured automatic effects. Include predecessor or dependency state only when it creates a concrete risk.

Generated platform objects are not independent blockers unless their revision binding, enforcement, result, lifecycle effect, or contractual relevance can change the decision.

## Separate effects without multiplying approvals

Assessment, readiness mutation, integration, source deletion, synchronization, and dependent work are different effects. Apply SPARC's single-grant stage rule: a grant may cover several when it names or clearly includes them, but one effect never implies an ungranted later effect.

A read-only assessment may report readiness without changing state. Plan approval is a quality finding, not implementation or integration authority. A request that explicitly covers a focused change, validation, commit, task-branch push, and review-object creation may proceed through that sequence without extra gates. Do not infer integration, deletion, synchronization, publication, deployment, or dependent work from review readiness.

## Integrate only the reviewed target

Before authorized canonical or protected-state integration:

1. Reverify the exact project, destination, reviewed revision, and required integration method.
2. Confirm required checks and reviews apply to that same revision.
3. Identify unavoidable effects such as deletion, deployment, publication, issue closure, or downstream automation.
4. Stop if the target drifted or an unavoidable effect lies outside the grant.
5. Integrate only the verified target and method through the native path.
6. Read back the resulting canonical revision and material automatic effects.

Preserve source branches, workspaces, changelists, and equivalent state unless deletion is authorized or controlling policy includes it. Read-only postflight proves the integration result; it does not authorize another mutation.

## Synchronize only when material

Enter synchronization handling only when synchronization was requested, controlling policy requires it, it is an unavoidable effect, or unresolved synchronization state creates a material risk to the current outcome. Do not start a synchronization-facts lane merely because integration completed.

Before an authorized synchronization, verify project identity, exact target, safe working state, actual canonical source, current revision, and the safe transition to the expected revision. Stop when drift, local changes, ambiguity, or a target mismatch threatens preservation, target identity, or the authorized transition. Unrelated local changes do not block a transition that is verified to preserve them; do not stash, discard, or rewrite them merely to obtain a clean state. Honor stricter controlling policy or explicit task constraints. Synchronization authority does not create authority for a new workspace, branch, review object, or follow-on task.

## Support non-Git systems

Map project identity, revision, review, integration, and synchronization to concepts the native system actually exposes. When no review object exists, validate the direct change against its governing contract without fabricating one.

## Return proportionately

Return the requested lifecycle result, validation, material automatic effects, unexpected residual state, and unresolved gates. Include identifiers only when they establish the result or enable the next authorized action. Do not expand an integration-only return into a synchronization audit.
