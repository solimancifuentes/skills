# Process debt audit

Find where a development or operational workflow creates avoidable effort, and propose changes that preserve controls with a clear purpose.

## Installation

```sh
npx skills add solimancifuentes/skills --skill process-debt-audit
```

## Process

1. Establish the outcome, workflow, and period being assessed. Use the operator's account alongside available project records, history, instructions, and tool output.
2. Reconstruct what actually happens. Trace repeated approvals, validation, handoffs, setup failures, and waiting to their causes.
3. Decide which controls to keep, automate, consolidate, apply only to relevant risks, or remove. Distinguish written requirements from agent interpretations and historical habits.
4. Propose the smallest workable transition, including who owns the remaining checks and the first real work item that should exercise the revised process.

## What to bring

Describe the delivery outcome and where work keeps getting stuck. Share the available evidence: conversation history, project files, recurring errors, process instructions, or the people and steps involved. The audit can proceed with partial evidence and states what it could not inspect.

Repositories, CI, pull requests, and agents are relevant when they are part of the workflow. They are not assumed requirements for an operational audit.

## What you get

The report connects observed friction to its likely causes, explains which controls still earn their cost, and recommends a proportionate workflow. Proposed fixes for recurring tool failures target project setup, command construction, or another layer supported by the evidence.

Diagnosis is read-only; implementing the recommendation is a separate request. This skill is for assessing a process, not ordinary implementation, routine code review, or a one-off build fix. Report size follows the evidence, without adding another reporting system.

[Full instructions](SKILL.md) · [MIT license](LICENSE)
