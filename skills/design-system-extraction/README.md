# Design system extraction

Reconstruct reusable design tokens and implementation rules from a website and available source so new pages can follow the inspected design.

## Installation

```sh
npx skills add solimancifuentes/skills --skill design-system-extraction
```

## Process

1. Establish the site, page or flow scope, available source, and intended output format.
2. Inspect representative layouts, components, states, and source definitions. Record where each finding came from and what remains inaccessible.
3. Extract shared decisions and composition rules, preserving meaningful exceptions. Keep observed values, inferred roles, and proposed changes distinct.
4. Check tokens and rules against matching evidence, then walk through how the handoff would support one new page.

## Inputs and output

Start with a live URL, supplied source, or both. A source-only result can describe authored rules, but it cannot verify deployed behavior. Screenshot-only and design-tool-only extraction are outside the dedicated workflow.

The default handoff pairs `design-system.md` with `tokens.json`. Tokens target DTCG 2025.10, a Community Group specification. Layout rules, fluid expressions, behavior, and exceptions stay in the companion document when token values cannot represent them faithfully. A requested consumer format can replace the default.

## What the evidence supports

Repeated values do not automatically become tokens, and missing values are never filled with an invented scale. The skill records coverage limits and keeps private source, signed URLs, and account data out of shared deliverables. Valid JSON or structural conformance does not prove rendered fidelity; exact visual matching still needs comparison in the target implementation.

[Full instructions](SKILL.md) · [MIT license](LICENSE)
