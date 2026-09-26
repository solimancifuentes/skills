# Source inspection

Use this reference for supplied code, stylesheets, tokens, design files, or documentation such as rebuild prompts. Distinguish each source's revision and claims from the deployed result.

## Find the relevant definitions

Start with task instructions and the supplied source boundary. Use focused file searches for stylesheets, token/theme configuration, component libraries, font declarations, and the imports or entrypoints that connect them. Inspect nearby documentation when it clarifies naming or usage. Do not scan unrelated repositories or personal directories to find an imagined original system.

Follow the files that affect representative pages. Prefer source tokens and component definitions over deduplicating every literal from a generated bundle. Public stylesheets can supply exact declarations when repository source is absent. Minified or generated code may show implementation values without establishing original authoring structure.

A running site usually makes a build unnecessary. If the task requires a local preview, inspect project instructions and scripts first and follow existing authorization and environment rules. Do not execute arbitrary setup scripts, install a framework, or change application files solely to extract values.

## Recover definitions and usage separately

- Trace custom properties and token references through their declarations, scoped overrides, and consumers. Preserve established aliases; equal literals alone do not prove shared intent.
- Follow representative definition-to-instance and composition links in source or design files. Identify component anatomy, variants, defaults, states, and content/layout constraints; describe an API as observed only when its definition was inspected. Use these findings to describe portable contracts; source classes, DOM structure, framework props, and design-tool settings are evidence, not required implementation interfaces.
- Retain declared font stacks, font-face resources and descriptors, and variable-font axes when present. A listed font resource does not prove successful loading or rendered use.
- Preserve media/container queries, themes, fluid expressions, and override conditions. Resolve effective styles through the applicable cascade, state, and script-driven changes; source order alone is insufficient.

Distinguish verified use, defined but unverified use, and apparently unused definitions within the inspected scope. Keep unconsumed declarations and unreachable variants out of the active token baseline; mention material source-only findings. A limited search cannot establish that a token is unused everywhere.

Apply the token-admission rule to authored definitions too; do not copy an entire library merely because it is available. Preserve aliases needed by selected tokens. Prefer useful semantic source names, map implementation-specific names where necessary, and keep isolated values in local recipes instead of generating redundant alias layers.

## Reconcile with rendering

Use source/design definitions for authored relationships and browser evidence for deployed results. Reconcile conflicting prose, comments, design files, code, and runtime observations by recording their claims, contexts, and unresolved differences. A document's "canonical" label or acceptance checklist does not establish correctness or completed testing. Keep current-site tokens based on the site; when the user targets a source/design revision, identify that baseline and keep deployment differences separate.

Investigate inexpensive explanations supported by the available files, such as overrides, scope, or a different loaded stylesheet. Do not assert stale deployment, caching, a bug, or an intentional redesign merely because values differ.

Record useful file/line or design-node references when verified; for public CSS, use its URL and selector/property. In shareable output, prefer repository-relative paths or neutral source labels and remove credentials, signed parameters, and private account identifiers. Retain private source evidence separately when needed for traceability. Preserve source expressions in the specification when token JSON cannot represent them faithfully, without exporting unrelated confidential code.
