# AI Slop Detector

Review writing for generic AI-style patterns and explain which ones cause a problem in context.

## Installation

```sh
npx skills add solimancifuentes/skills --skill ai-slop-detector
```

## Process

1. Read the passage, its purpose, and any supporting material. An original draft or voice reference is needed to assess fidelity.
2. Check all 57 patterns across eight editorial dimensions. Judge each pattern against the audience, genre, and intended effect.
3. Record supported problems with exact evidence, their consequences, and a repair direction. Account for contextual exceptions and missing evidence.
4. Return a concise report led by the findings that matter most. Expand the report or calculate an index when requested.

## What the report tells you

The default report explains the main problem and a few consequential findings. Serious grounding or fidelity failures stay visible even when the report is short. A detailed report includes the dimension ratings and accounts for every pattern check.

Report length and scoring are separate choices. A requested score is labeled **Rubric index (unvalidated)** and withheld when the assessment is ineligible. It cannot establish who wrote the text, verify facts, or measure the probability of AI authorship. Rewriting is a separate request.

## Tools and records

Optional Python 3 helpers validate assessment records and calculate the index. They use the standard library; the agent supplies the editorial judgment. Without code execution, the skill uses manual checks and reports that limitation.

Assessment records retain source text, including passages excluded from evaluation. Review and redact a separate copy before sharing; a concise report is not automatically safe to publish.

[Full instructions](SKILL.md) · [Pattern catalog](references/patterns.md) · [MIT license](LICENSE) · [Third-party notices](THIRD_PARTY_NOTICES.txt)
