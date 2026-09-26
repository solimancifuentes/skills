# Applied feasibility analysis

Evaluate whether an external capability, implementation, or business practice is worth adopting for a specific project.

## Installation

```sh
npx skills add solimancifuentes/skills --skill applied-feasibility-analysis
```

## Process

1. Define the candidate and the decision it needs to support. Choose one bounded idea or a portfolio from selected business areas of a company or product.
2. Inspect the source evidence and the target project's current state. Separate observed mechanisms, vendor claims, inferences, and missing facts.
3. Compare the candidate with the current approach and relevant simpler alternatives. Identify prerequisites, adaptations, costs, and failure modes that matter to this project.
4. Give each supported candidate an `ADOPT`, `ADAPT`, `REJECT`, or `DEFER` verdict, with confidence and a validation step where useful. Use `INSUFFICIENT EVIDENCE` when a missing fact prevents a decision.

## What to provide

Supply the source material or company identity, a target project path or enough project context, and the question you need answered. For a company or product portfolio, name the business areas you want to study. Research stays within that objective rather than expanding into a general company profile.

## What you get

Atomic analysis returns an inline report for one bounded candidate. Business surface analysis returns a dated dossier by default, or an inline portfolio when requested. File output uses an agreed destination and preserves existing analyses.

Each decision includes its evidence, project fit, alternatives, and unresolved questions. Separate candidates keep separate verdicts; there is no averaged company score. The result is an analysis, with implementation handled as a separate task.

[Full instructions](SKILL.md) · [MIT license](LICENSE)
