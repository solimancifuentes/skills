# Atomic Analysis

Use this mode to evaluate one bounded candidate from one or more sources against one target project.

## Scope the candidate

1. Read the actual evidence for the mechanism using the shared coverage rules: complete bounded documents, or the relevant implementation and dependencies within a repository or large collection.
2. Identify distinct capabilities, implementations, and practices.
3. Keep an explicitly selected candidate even when the source contains others. Only if the intended candidate remains unclear, present a concise candidate list and ask which bounded thesis to evaluate.
4. If the user explicitly requests all candidates, produce a compact portfolio with a separate assessment for each. Issue an overall verdict only when the request names one bounded thesis that spans them.

Do not treat using a vendor as the candidate when the user is asking whether to reproduce one of its capabilities or practices. State the distinction explicitly.

## Build the evidence base

Identify:

- how the candidate actually works;
- the direct evidence for that mechanism;
- implicit prerequisites concerning scale, data, infrastructure, skills, team, process, economics, or maturity;
- subject claims, inferences, contradictions, and evidence gaps.

Apply the shared provenance and completion rules. Report inspected coverage and material omissions. Preserve supported findings when a source is inaccessible; a missing source blocks only conclusions that depend on it.

Inspect the target-project path before asking for context. Follow its declared read order where present and cite the files that establish current architecture, scope, authority, goals, and constraints. Ask only for missing facts that could change the assessment.

## Map candidate to project

Cross-reference every material prerequisite against verified project facts. Identify direct alignment and named adaptation; avoid generic learning-curve, complexity, security, or maintenance warnings that could apply to any project.

Compare adoption with the current approach and relevant simpler alternatives under the shared contract. Make the incremental value part of the recommendation, not just a list of potential benefits.

Classify the candidate under the shared evidence and decision contract. If the mechanism itself or a decision-critical project fact is unsupported, use `INSUFFICIENT EVIDENCE` rather than forcing a verdict.

## Write the report

Use these required sections and fields. Add concise subsections only when they improve traceability.

```markdown
## Decision
- **Candidate:** [bounded capability, implementation, mechanism, or practice]
- **Assessment Status:** [DECIDABLE | INSUFFICIENT EVIDENCE]
- **Verdict:** [ADOPT | ADAPT | REJECT | DEFER; omit when evidence is insufficient]
- **Confidence:** [HIGH | MEDIUM | LOW; omit when evidence is insufficient]
- **Rationale:** [2-3 decisive, project-specific sentences]

## Mechanism, Evidence & Prerequisites
- **Mechanism:** [how it works]
- **Supporting Evidence:** [traceable evidence and evidence states where material]
- **Evidence Scope and Provenance:** [inspected artifacts, material omissions, source dates/revisions when available, inspection date, and evidence cutoff]
- **Assumptions and Prerequisites:** [what must be true]
- **Evidence Limitations:** [material uncertainty, contradictions, or unknowns]

## Target-Project Fit
- **Relevant Project Facts:** [cited facts that control the decision]
- **Current Approach and Alternatives:** [verified baseline and relevant simpler alternatives; disclose unknowns]
- **Incremental Value:** [what adoption improves and whether it justifies the cost compared with those options]
- **Direct Alignment:** [the real project problem or opportunity addressed]
- **Necessary Adaptations:** [specific components, workflows, or operating changes]

## Trade-offs & Failure Modes
- **Costs and Trade-offs:** [specific financial, performance, complexity, or maintenance costs]
- **Risks, Edge Cases, and Failure Modes:** [where this candidate breaks in this project]

## Validation or Evidence Needed
- **Smallest Validation Step:** [smallest honest test; omit when evidence is insufficient]
- **Success and Stop Criteria:** [observable pass and failure conditions; omit when evidence is insufficient]
- **Missing Evidence:** [what would make the assessment decidable; include only when needed]
```

Make every section specific to the candidate and target project. When no useful validation can be performed safely or cheaply, say so instead of inventing a proof of concept.

## Deliver

Present the report inline. Do not save it by default. When the user asks for a file, use the supplied or previously confirmed exact directory and filename without asking again. If either is missing, propose a descriptive `<candidate-slug>-feasibility-analysis.md` path and resolve it before writing; independent authorized research may continue. If the exact destination already exists, preserve it and ask for a new destination rather than silently overwriting or renaming it.
