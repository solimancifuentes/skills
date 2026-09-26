# Deliverables

Turn evidence into a compact implementation specification. Keep `design-system.md` authoritative for usage, composition, behavior, responsive rules, and exceptions; keep `tokens.json` authoritative for exported values. Treat them as a paired handoff. Avoid duplicating the full token catalog in prose.

## Size and organization

For one coherent website design system with a base theme, use these editorial heuristics:

| Measure | Target or review threshold |
| --- | --- |
| Named design tokens | Typically 50–100; review and justify expansion beyond 150. |
| Core `design-system.md` | Target 3,000–5,000 language-model tokens. |
| Complete package loaded into AI context | Review for compression or selective loading around 10,000–12,000 language-model tokens. |

These are not minimums, completeness caps, research-backed attention limits, or model capacity limits. Smaller systems should stay smaller. More themes or application complexity may justify expansion; do not discard essential rules to meet a budget. Count every emitted token object containing `$value`, including primitives and aliases, with each composite counted once and separately emitted theme variants counted separately. Also measure serialized text size: token count alone hides composite complexity and verbose descriptions. Use an available tokenizer and identify it; otherwise report words/bytes and label any language-model token estimate as approximate. Do not install dependencies solely to count tokens.

Remove repetition before splitting files. Retain the two-file default; use optional, clearly linked supplements only for genuinely distinct systems or specialist scope. Keep an entry point explaining what to read for a task. Selective token loading must include referenced dependencies and applicable context values; a supplement is not an excuse to inflate the total package.

## Design specification

Use a predictable, scannable structure covering the following areas; combine sections when that saves repetition. Briefly mark unsupported categories rather than filling them with defaults.

| Area | Minimum useful content |
| --- | --- |
| Identity and baseline | Target URL/source, inspection date, intended scope, and a few concrete, evidence-grounded principles about hierarchy, density, emphasis, or other distinctive choices. Label inferred principles. |
| Foundations | Color roles and foreground/background pairings; typography roles and styles; spacing; borders, radii, depth, and relevant motion. Reference tokens and explain use. |
| Layout | Containers, gutters, text measure, grids, vertical rhythm, and responsive transformations, including meaningful conditions and fluid expressions. |
| Components | Purpose, anatomy, token references, supported variants, relevant states, behavior, content constraints, and responsive changes. |
| Composition | A few representative recipes explaining how components form sections and pages, including hierarchy, spacing relationships, content variation, and narrow-layout behavior. |
| Assets | Font dependencies and fallbacks; logo, icon, and image treatment, references, and material availability constraints. |
| Implementation rules | Context/theme selection, platform adaptation points, accessibility expectations, and how to extend the system consistently. |
| Evidence and readiness | Compact coverage/methods, material mappings and exceptions, source conflicts, checks performed, and unresolved implementation decisions. |

Write component and composition recipes as reusable contracts. Reference shared rules instead of repeating them for every component. Source classes, DOM structure, framework props, and design-tool settings are not required interfaces. Describe layout and interaction intent precisely; retain web-specific expressions where needed and identify how units, fonts, input methods, and accessibility semantics require platform adaptation. Portable JSON alone does not establish portable behavior.

For relevant components, cover focus, hover/press, disabled, selected, loading, error, and empty states, along with keyboard behavior, labels, text expansion, and reduced motion. Not every state applies to every component. Distinguish extracted behavior, proposed additions, and unresolved requirements. Missing accessibility support must not be silently invented or described as verified compliance.

Tell future implementers to reuse existing tokens and recipes first, add a variant only for a distinct need, and admit new tokens through the criteria below. Keep meaningful one-off exceptions local. Material changes to values or behavior are adaptations; identify them and their scope instead of presenting them as observed. Do not turn the extraction into a speculative redesign.

Put shared evidence and Observed/Inferred labeling at the relevant section or group scope; state which findings and token groups they cover. Add token-level notes only where meaning, provenance, or context differs. Every exported token must remain traceable through this scope or a specific reference. Keep material original-to-output mappings and coverage limits, without repeating evidence boilerplate or inventing confidence percentages. Sanitize evidence references before sharing: omit access-bearing query strings, private account data, personal source paths, and confidential screenshots. A neutral evidence label may point to a private original without copying that original into the handoff.

## Token output

Default to the stable [DTCG Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/) and its [Color Module](https://www.designtokens.org/tr/2025.10/color/). This is a Community Group specification, not a W3C Recommendation. Honor a requested consumer format; identify it and its checks explicitly.

Admit a token only for an evidenced shared decision, recurring design intent, or distinctive property needing centralized control. Check whether existing tokens or compositions express the same intent first. An authored token's availability alone does not justify exporting it. Incidental positioning, illustration geometry, and isolated adjustments usually belong in local recipes.

Prefer shared foundations and stable semantic roles; use component-specific tokens only for distinct decisions that need to vary independently. Do not generate primitive-to-semantic-to-component aliases for every property. Preserve useful authored names and necessary alias dependencies; reconstruct portable names with material mappings when the source names obscure meaning. Equal values alone do not establish shared intent.

Group tokens to reflect supported relationships and separate contexts. Keep the same semantic role across themes where supported, with context-specific values; avoid duplicating unaffected categories. State how consumers select and combine contexts. Group names do not implement theme switching or establish a runtime resolver.

Use `$value` and a resolvable `$type`. Add `$description` where it clarifies usage, non-obvious meaning, or an exception to the specification's shared evidence/context notes; do not repeat boilerplate on every token. Supported common forms include:

| Type | Value shape |
| --- | --- |
| `color` | Color object: `colorSpace`, `components`, optional `alpha` and `hex`; not a bare CSS color string. |
| `dimension` | Object with numeric `value` and `unit` of `px` or `rem`, including zero. |
| `fontFamily` | Single family string or ordered array of family strings. |
| `fontWeight` | Numeric weight from 1 through 1000 or a specified weight keyword. |
| `duration` | Numeric `value` plus `unit` of `ms` or `s`. |
| `number` | A finite JSON number; useful for unitless line height or opacity. |
| `cubicBezier` | Four numbers; the first and third are between 0 and 1. |

For colors, preserve the measured color space and alpha. In sRGB, RGB components use normalized values; any optional hex must agree with the components. Do not silently reduce wide-gamut values to sRGB. Convert only when the relevant conversion and its effect are established.

Whole-token aliases use `{group.token}`. Resolve targets, types, and cycles. Token/group names cannot start with `$` or contain `{`, `}`, or `.`. If using composites or property references, read their relevant normative sections and validate their exact shapes.

This synthetic example illustrates output structure, not values to reuse:

```json
{
  "spacing": {
    "card-padding": {
      "$type": "dimension",
      "$value": { "value": 20, "unit": "px" },
      "$description": "Card inner spacing; does not control gaps between cards."
    }
  }
}
```

Keep proposals out of `tokens.json`. Do not add placeholder tokens for unknown values. Keep `clamp()`, percentages, viewport-relative dimensions, `auto`, unresolved variables, layout expressions, and other values without a faithful supported representation in the specification. Explain these omissions. A measured snapshot may be exported only with its context explicit, never as the replacement for a fluid rule.

A name or relationship can be inferred while its value is observed; preserve that distinction through scoped evidence or a specific note. Shared roles supported by recurring usage are inferred reconstruction. Changed values or added behavior are proposed adaptations and stay outside the default token baseline. Never round values into an invented scale to reduce the token count.

## Validation and handoff

Parse the JSON with an available parser. Check the types actually emitted against the relevant specification sections: value shape, units/ranges, inherited types, names, and alias targets/cycles. Check nested references as well as whole-token aliases if present. A JSON parse alone does not establish DTCG validity. Do not add a dependency or claim validator coverage that was not exercised.

Compare representative values, compositions, and behaviors with cited evidence in matching page, viewport, theme, and state contexts. Check fidelity-sensitive relationships such as text wrapping, logo scale, and accumulated spacing when material. Keep specification/token names, units, baseline, and exclusions consistent.

Walk through one representative new page using only the deliverables: identify the tokens, components, composition, responsive rules, and relevant states it would use. Resolve contradictions, missing references, and major decisions that can be answered from the evidence. List substantive decisions still requiring implementation judgment or additional evidence. This is a specification exercise, not permission to build, an invented observed page, or proof of rendered fidelity.

Run a final compression pass: remove redundant aliases, repeated prose/values, unneeded component entries, and tokens not supporting the handoff, while retaining required alias dependencies. Preserve essential rules and distinctive exceptions; justify budget overruns or link genuinely separate scope. Token validity, specification readiness, visual agreement, functional behavior, and coverage are separate claims. Structural conformance to DTCG, a passing build, or absence of overflow does not prove rendered fidelity.

Fix failed outputs and rerun the affected checks; report checks that could not run. Deliver file links and the consequential gaps. For a requested build handoff, state the intended fidelity and adaptations, and explicitly request browser comparison when visual matching is required. Keep this in the specification; extra formats or previews are optional requested outputs.
