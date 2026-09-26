# Consequential Work

Read this reference only after SPARC classifies a concrete action **Consequential**, or when controlling policy explicitly requires these safeguards. Do not load it merely because a request says candidate, release, security, production, exact, failure, externally visible, one-shot, or no-retry.

## Bind the material contract

Before consequential execution, record only what is needed to control the action:

- exact outcome, target, and destination;
- allowed and prohibited effects;
- authoritative inputs and invariants;
- validation and authoritative postflight;
- conflict and stop conditions;
- retry rule;
- residual risk requiring human acceptance.

Confirm that the predicates are mutually satisfiable, independently observable, executable through the selected path, and realistic about unavoidable platform effects. Redesign an infeasible contract before mutation.

Do not add byte identity, hashing, timing, environment, attempt, or evidence-record requirements unless the authorization target, governing policy, or a demonstrated risk needs them. When authority binds an exact artifact, revision, payload, or digest, preserve that identifier. Validate mutable external records through scoped semantic checks and authoritative readback; use a bounded diff only when proving that no other location changed is material.

## Qualify only material execution boundaries

Use the direct native path by default. Qualify a wrapper, PTY, persistent session, transport, service, or other special boundary only when the native path cannot satisfy a concrete requirement and the action depends on that boundary behaving correctly.

Exercise generated commands, parsers, and predicates before a non-repeatable mutation when a mechanical defect could waste the only safe attempt. Verify only the syntax, dialect, data boundary, result semantics, and side effects that can affect execution.

Apply SPARC's task-bound stage rule. Treat these as distinct evidence boundaries only when useful; a result at one boundary neither proves a later result nor authorizes an effect outside the grant.

## Protect public publication and release

Immediately before an authorized public publication or release:

1. Reverify the exact publication target, destination or channel, and the still-applicable human grant.
2. For a versioned artifact release, reverify the exact version and artifact identity using the platform's authoritative identifiers. Verify tag targets, release classifications, and digests when the platform, artifact contract, controlling policy, or demonstrated substitution risk makes them material. Preserve any exact identifier bound by the grant; an unavailable required digest or unprovable artifact identity is a blocker, while absence of an inapplicable Git tag or digest facility is not.
3. Detect an existing conflicting target, tag, release, artifact, or channel state and stop on mismatch.
4. Identify unavoidable automatic effects and stop if any falls outside the grant.
5. Use the platform's native mutation path with one stateful owner.
6. Perform authoritative readback of the resulting public target and every material applicable association, classification, or automatic effect.

Candidate, validated, published, deployed, and released remain distinct states. Internal preparation never implies publication authority, and publication does not by itself prove deployment or production readiness.

## Recover without blind retry

After a failed consequential external operation:

- if authoritative reconciliation proves zero effect, retry the identical action when the original grant remains applicable;
- if state is partial, conflicting, or unknown, reconcile and stop before another mutation;
- if the correction changes the target, scope, predicate, or material effect, obtain the authority appropriate to that change.

No-retry or consumed-attempt behavior applies only when controlling policy says so, a valid explicit task instruction imposes it within the user's authority, or an intrinsically non-repeatable operation creates harmful duplication or partial-state risk. A task-specific no-retry control expires with that task. When such a boundary applies, define exactly when the attempt is consumed. Do not infer consumption from candidate allocation, a label, a failed validation, or an aggregate nonzero exit.

## Keep evidence decision-useful

Record a consequential action's environment only when a material boundary depends on it—for example, platform-specific packaging, native dependency behavior, production identity, credential environment, publication channel, or a qualified special boundary. Otherwise rely on SPARC's operator-evidence rule.

Apply SPARC's smallest-useful evidence rule. Do not require lifecycle issues, attempt identifiers, evidence comments, hashes, checkbox transitions, command counts, poll counts, byte offsets, or full mutation inventories unless controlling policy or the concrete risk makes them material.

After failure, report only the substantive predicate or unresolved boundary, observed result, confirmed effects, retry status, and supported next action. Protect secrets, credentials, raw environments, customer data, and unrelated logs.

For a consequential prompt, include the material contract, native or qualified path, stop and reconciliation conditions, and required authoritative readback. Ask for evidence, not hidden reasoning or ceremonial proof.
