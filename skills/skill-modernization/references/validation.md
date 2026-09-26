# Validate the change that matters

Use this reference when selecting checks, testing an authorized candidate, or assessing claims of validation. Keep the validation effort inside the task grant.

## Separate structure from behavior

Use an available validator appropriate to the target skill format. A host helper such as `skill-creator`'s `quick_validate.py` may supply structural checks when installed; resolve the actual helper and runtime before execution. If none is available, perform supported local checks and name their limits. Check required frontmatter, present host metadata, policy actually required by the owner, relevant dependencies, linked local resources, and unfinished scaffolds. Do not require a host-specific metadata file or a fixed invocation setting on every skill. Do not infer semantics from a preferred sentence or a fixed file count.

Inspect unfamiliar validators and target scripts before running them. Verify their relevant inputs, side effects, and runtime requirements. Prefer an existing suitable environment; a missing dependency is a validation limitation, not a skill failure or a passing check. Correct an authorized local invocation or use another already-available runtime with the same checks. Dependency installation must fit the grant; do not silently modify global environments or vendor helpers. Clearly distinguish partial checks or an alternate validator from the standard check actually requested.

Contain test artifacts outside the installed package. Resolve symlinks and file targets before reading or executing fixtures; report a boundary issue without accessing unrelated material. Installation checks must examine the actual invocation policy after any generator, setup, or packaging step that could overwrite it.

## Choose meaningful behavioral evidence

A harmless wording correction usually needs a focused diff and relevant structural checks. A change to routing, authorization, dependencies, recovery, or executable behavior merits realistic cases that could expose a wrong decision. Validate changed scripts against their observable outputs and effects when running them is authorized. Do not execute a target's workflow merely to make a review appear complete.

For complex or risky changes, use independent evaluators when available, authorized, and worth the coordination cost. Give respondents realistic requests, the assigned skill, and minimal raw artifacts. Withhold the intended answer, suspected defect, candidate diff, and grading rubric unless the evaluation specifically requires them. Keep expected behavior with the evaluator or separate grader. Evaluate semantic outcomes, including justified alternatives, rather than stock phrases or mandatory strongest-model choices.

Compare the candidate with the current baseline when assessing a claimed improvement or regression. For a new skill, assess its intended behavior directly. Keep cases independent except when a sequence is itself under test. Grouped simulations are acceptable for a bounded assessment; describe them honestly and use isolated reruns when a dispute or contamination concern warrants it.

Do not reinterpret every omitted sentence as a failure. Identify whether the result contains a material wrong decision, missing requirement, or unsupported claim. Preserve failed results and explain any fixture correction; do not weaken criteria merely to obtain a pass. Structural success cannot cancel a blocking behavioral defect.

## Apply and close within the grant

Before an authorized installation, confirm that the candidate is the tested material, the destination and source are correct, and material state has not drifted. Preserve the recoverable baseline and use the platform's supported installation path. Do not overwrite an unexpected existing target or directly patch a generated plugin cache as a durable update. See [plugin source guidance](plugin-sources.md) when applicable.

After installation or reinstallation, read back the relevant files, metadata, and material package associations. If an operation has an uncertain outcome, reconcile authoritative state before retrying. Do not equate file readback with application pickup, runtime enforcement, or a live workflow test.

Return actual checks and results, observed improvements or lack of regression, and material limitations. If both baseline and candidate pass the same examples, report that result without claiming measured superiority. Correct recoverable defects within scope and rerun affected checks; stop when the requested outcome passes rather than iterating toward an arbitrary score.
