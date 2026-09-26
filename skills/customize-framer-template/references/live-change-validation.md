# Live Change Validation

## Purpose

Use this reference before every live mutation. Prove the approved effective outcome while protecting authored state outside scope. Treat raw tool output as evidence, not automatically as the success predicate.

## Define the material projection

Before mutation, define the smallest projection that can prove success and detect material drift. It should normally include only:

- stable target identity;
- authored values in scope;
- effective inherited or bound values;
- protected authored fields;
- affected consumers; and
- materially distinct variants, breakpoints, or local overrides.

Exclude by default computed rectangles, timestamps, tool metadata, volatile ordering, serialization formatting, unrelated descendants, and command hashes or counts. Raw hashes are appropriate only for an actual byte-identity contract, deterministic export, immutable asset, or incident diagnosis.

## Preflight

Refresh the exact project, editing path, scoped targets, current values, known consumers, and material projection immediately before mutation. Confirm that the current authority covers the observed effect class. Stop on identity mismatch, stale target values that invalidate an atomic change, changed consumers, expanded blast radius, or missing authority.

Classify relevant values as local authored, inherited, variant-specific, bound, or computed. Identify intentional overrides and protected fields before applying a shared-source change.

Probe capabilities only when the proposal depends on behavior that current project context and owning documentation do not establish. Prefer read-only probes. A mutation probe needs its own exact target, authority, success predicate, recovery path, and readback; do not use speculative writes for routine discovery.

## Recovery proportional to impact

Use recovery mechanics supported by the current Framer environment and editing path. Routine local reversible work does not require an automatic project duplicate or recovery rehearsal. For broad guarded or consequential changes, verify an appropriate branch, snapshot, duplicate, immutable source asset, or other recoverable state before mutation.

Do not claim recovery merely because a candidate, preview, or history surface exists. Verify the recovery target and what it covers. Unknown recovery for a difficult-to-reverse effect is a stop condition.

## Apply and read back

Apply the inspected targets and values within the authority envelope, including choices delegated by the user. Keep related changes coherent when splitting them would create false intermediate failures, but do not conceal independent targets or drift inside a batch.

Immediately read back every changed authored value, its effective result, protected fields, and materially distinct consumers or overrides. For an uncertain write, inspect current state before retrying, correcting, rolling back, deleting, or publishing. Never repeat an exact-once or external action merely because the first response was unclear.

## Normalize effective state

Distinguish:

1. raw tool output;
2. property-specifically normalized authored value;
3. local authored state;
4. inherited, variant, or bound effective state;
5. computed presentation state; and
6. the protected material projection.

Use property-specific normalization only when it preserves meaning. For example, a serialized visibility value of `"false"` may be semantically equivalent to Boolean `false` when the owning platform evidence confirms the effective hidden state. Do not require a redundant local value when inheritance already produces the approved result.

Unknown, lossy, or contradictory normalization cannot manufacture a pass. Preserve raw evidence needed to explain the decision and stop when effective state cannot be established safely.

## Validate affected presentation

Define success in terms of the approved effective outcome and unchanged protected authored state, not expected local-write counts or whole-tree equality. Validate exact copy where wording was fixed, intended inheritance and overrides, bindings, destinations, layout and interaction effects, and every materially distinct affected responsive state.

Validate every materially distinct consumer of a changed shared source. When exhaustive validation is impractical, name the sampled equivalence classes and edge cases and disclose what remains unverified. Computed reflow alone is not an authored change, but clipping, overflow, hierarchy damage, lost interaction, or an unexplained material difference is not harmless serialization noise.

Canvas visibility does not prove accessibility-tree removal, focus exclusion, indexing, or publication state. Verify each through an appropriate observable surface or report it as manual or unverified.

## Bounded corrective pass

After readback, a corrective pass remains inside the original authority only when the project and target match, the approved outcome is unchanged, partial state is observable and unambiguous, the cause is understood, and the remaining reversible correction affects only authorized targets or enumerated overrides.

The correction must introduce no new object, dependency, external action, destructive action, publication effect, or higher effect class. Apply only the proven remainder and immediately re-read the final and protected states. Report the partial-write incident and correction.

## Stop conditions

Stop before further mutation when:

- project or target identity differs;
- a material current-value, consumer, schema, binding, relationship, or scope predicate drifted;
- partial state or prior external effect is unknown;
- normalization would be lossy or contradictory;
- recovery is uncertain for the observed effect;
- the required correction expands targets or effect class;
- a material visual, interaction, responsive, or accessibility problem persists; or
- consequential authority is absent.

Do not stop solely because equivalent serialization differs, an inherited value lacks local materialization, computed geometry reflows without an authored change, or a transient warning is absent from final state.

## Evidence and reporting

Keep enough raw evidence to support the semantic conclusion, then report concisely:

- exact authorized and observed targets;
- values or effective outcomes applied;
- protected state checked;
- consumers and materially distinct responsive states validated;
- normalization used and why it was sound;
- sampling, manual checks, and remaining uncertainty;
- any partial-write incident and bounded correction; and
- activation and publication state.

Do not report command counts, whole-tree hashes, or exhaustive screenshots unless the actual contract requires them. Keep private raw evidence separate from shared summaries. This reference defines semantic predicates; use the current Framer environment and official documentation for platform-specific decoding and mechanics. Do not invent a parser to explain undocumented output.
