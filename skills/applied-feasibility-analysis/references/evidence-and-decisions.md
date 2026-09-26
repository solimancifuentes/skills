# Evidence and Decision Contract

Use this contract in both analysis modes.

## Candidate model

Make the transferable candidate the unit of decision, not the whole source, surface, company, or product.

Classify each candidate as one of:

- **Capability:** an outcome the subject can produce.
- **Implementation:** the concrete mechanism or system that produces an outcome.
- **Practice:** a repeatable human or organizational behavior.

Assign one primary owner surface and any cross-surface tags when working in Business Surface mode.

## Evidence states

Use these states when they materially affect interpretation:

- **OBSERVED:** directly visible in a primary artifact, product behavior, repository, or other inspectable evidence.
- **SUBJECT CLAIM:** asserted by the subject or vendor but not independently established.
- **CORROBORATED:** supported by independent or converging evidence.
- **INFERRED:** reasoned from evidence but not directly established; name the inference.
- **UNKNOWN / UNOBSERVABLE:** unavailable from the authorized evidence boundary.

Prefer primary sources. A subject's documentation can establish what it publishes or claims, not that the mechanism is effective or that undisclosed internal operations work that way. Never convert missing evidence into a negative finding.

Ground target-project facts in authoritative project files. Cite the exact file, record, or supplied statement used. Do not substitute facts from similar projects.

## Private evidence and report audience

Use private, local, signed-in, or connected evidence only within the user's authorized scope. Access for analysis does not authorize publishing that evidence or sending it to another audience. Preserve useful traceability without copying secrets, personal data, customer records, or unnecessary confidential excerpts into the report. Use a concise finding and a source locator the intended audience is allowed to access.

Mark material confidential when sharing or audience limits matter. Omit private material from public output unless its disclosure is authorized; use public evidence and keep any resulting limits on the conclusion visible. These boundaries apply equally to inline reports and saved dossiers.

## Coverage, provenance, and completion

State the selected question and authorized evidence boundary before research; reuse a supplied scope rather than reconfirming it. Read manageable, bounded supplied documents completely. For repositories or large documentation collections, inspect the mechanism's implementation, relevant dependencies, prerequisites, and limitations. Identify inspected artifacts and material omissions; do not claim exhaustive review of unread areas.

Record source identity and locator, relevant publication/update dates or versions when available, retrieval or inspection date, and the run's evidence cutoff. Distinguish publication dates from retrieval dates. For the project fact sheet, cite the files inspected and the relevant revision or supplied context date when available; note local changes that affect the facts rather than treating a commit as the entire working state. Mark unavailable provenance as unknown without inventing it. Keep this proportional to the decision and attach provenance to existing citations or evidence records rather than duplicating a register everywhere.

Preserve conflicting evidence and explain how it affects the decision. If material source or project drift is discovered during the run, recheck affected facts and conclusions and record the change; do not silently retain a stale fact sheet or restart unrelated work.

An inaccessible source does not invalidate other supported findings. Continue within the authorized boundary and assess each candidate using the available evidence. If its mechanism or another controlling fact remains unsupported, use `INSUFFICIENT EVIDENCE`; name the missing evidence and the smallest way to obtain it without taking that action automatically.

Finish when the agreed research boundary has been covered and candidate assessments completed, or when remaining gaps cannot be resolved within that boundary and are documented. Do not expand research merely to find more candidates or prove exhaustiveness. Mark an incomplete run `partial` when useful work is preserved, or `blocked` when no useful assessment can proceed. A completed assessment can conclude `INSUFFICIENT EVIDENCE`; that candidate status alone does not mean the research was unfinished. In Business mode, distinguish a covered surface with no credible candidates from a surface whose required research failed.

## Baseline and alternatives

Compare the candidate with the current project approach, including maintaining it, and with relevant simpler alternatives supported by the authorized evidence. Explain the incremental benefit and whether it justifies the adaptations, prerequisites, and costs. Do not broaden the task into an exhaustive alternatives search or invent a baseline. An undocumented current approach is unknown and blocks a verdict only when it could materially change the decision.

## Assessment status

Choose exactly one status per candidate:

- **DECIDABLE:** the evidence supports a responsible project-relative recommendation.
- **INSUFFICIENT EVIDENCE:** material subject or project facts are missing, so no adoption verdict is responsible.

For `INSUFFICIENT EVIDENCE`, issue no verdict or confidence rating. Name the missing evidence, why it matters, and the smallest safe way to obtain it.

## Verdicts

For a `DECIDABLE` candidate, choose exactly one:

- **ADOPT:** directly solves a current target-project problem, substantially meets prerequisites, and needs little translation.
- **ADAPT:** is worth pursuing but needs named changes for the project's scale, stack, team, operating model, authority model, or constraints.
- **REJECT:** targets the wrong problem, conflicts with hard constraints, or costs more than its realistic benefit even after adaptation.
- **DEFER:** is supported and potentially useful, but a named target-project prerequisite must occur first. State a concrete revisit trigger.

Do not use `DEFER` to hide an evidence gap. Do not force one verdict across candidates with different mechanisms or prerequisites.

## Confidence

For a `DECIDABLE` candidate, choose one recommendation-confidence level:

- **HIGH:** direct subject evidence and verified project facts support the recommendation; no material unknown is likely to reverse it.
- **MEDIUM:** the recommendation is supported, but a bounded inference or non-blocking unknown could change its scope.
- **LOW:** the recommendation is provisional because material but non-blocking uncertainty remains. Explain what could reverse it.

Confidence describes the recommendation, not the subject's marketing strength or the analyst's writing certainty.

## Decision record

For every candidate, record:

- candidate name, type, and mechanism;
- evidence and material limitations;
- target-project problem and relevant facts;
- current approach, relevant simpler alternatives, and incremental value;
- prerequisites and dependencies;
- benefits, adaptations, costs, risks, and cross-surface effects;
- assessment status;
- verdict and confidence only when decidable;
- smallest validation step and success/stop criteria, or missing evidence when undecidable.

An `ADOPT` or `ADAPT` verdict is analytical advice only. It never authorizes a project edit, implementation, purchase, publication, installation, or external action.
