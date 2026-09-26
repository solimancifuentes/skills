# Content Workflow

Use this reference for project identity, scoped inventory, factual briefing, regular or shared copy, CMS content, batching, and multi-unit tracking.

## Contents

- [Confirm identity and execution path](#confirm-identity-and-execution-path)
- [Build the scoped baseline](#build-the-scoped-baseline)
- [Establish factual content inputs](#establish-factual-content-inputs)
- [Map regular and shared content](#map-regular-and-shared-content)
- [Map CMS content](#map-cms-content)
- [Batch and apply approved content](#batch-and-apply-approved-content)
- [Maintain the compact tracker](#maintain-the-compact-tracker)
- [Pause, defer, exclude, and close out](#pause-defer-exclude-and-close-out)

## Confirm identity and execution path

For live work, use the authorized Framer environment to confirm the exact project and current editing path before inspection or mutation. Establish whether changes use a branch or land directly, and identify the available recovery surface. Disclose a material recovery limitation before a change that depends on it. Stop on an identity mismatch.

For a partial request, confirm the project and inspect only the surfaces needed to understand the named work. Do not require a complete-customization baseline.

## Build the scoped baseline

For a partial request, inventory only the named targets, their material dependencies, known consumers, and materially affected responsive states.

For a complete customization, cover:

- regular pages and routes;
- CMS-bound list and detail routes;
- CMS collections, relevant item values, and canvas bindings;
- navigation, footer, shared CTAs, badges, reusable component-source copy, and other shared surfaces;
- reusable components, significant instances, inheritance, variants, and local overrides;
- styles, images, forms, links, code components, responsive states, and fragile dependencies.

Separate regular pages, CMS-bound routes, CMS collections, and shared sources so each target and consumer has an owner. Record only facts needed to route and validate the work. Before later units, refresh project identity and material scoped predicates instead of rerunning the full baseline.

## Establish factual content inputs

Start with supplied material and extract facts needed by the affected pages: what visitors can obtain, who it serves, what supports its claims, and where each action leads. Add pricing, CMS inputs, tone, and other details only where the requested content needs them. Cite the relevant input for each material business claim.

Separate confirmed facts from missing inputs and unsupported claims. Ask only consequential questions that cannot be answered from authorized evidence; use neither a fixed question count nor a mandatory one-question-at-a-time interview. Do not automatically launch legal, security, provider, repository, or business-model research merely because a page mentions that domain.

If a dependency in another domain is blocked, record its named activation trigger and continue unrelated authorized work.

## Map regular and shared content

Map each relevant existing target as keep, change, or propose hiding. For a change, record the target, current content, proposed content, factual source, destination where applicable, visual-fit risk, and affected responsive states. Keep hiding, additions, style changes, imagery, CMS data, and publication effects distinguishable by effect class.

For shared sources, enumerate every known consumer and any intentional instance or variant overrides before mutation. Preserve the source-versus-override relationship. An enumerated map may batch related regular pages or shared content when they use the same dependencies, effect class, and validation method.

For a proposed addition, identify the smallest existing element to reuse and the impact dimensions required by the core skill. Do not create placeholder facts, proof, destinations, or assets to make the map appear complete.

## Map CMS content

Distinguish template-static text, bound fields, CMS item values, shared-component copy, and computed presentation. Enumerate every proposed batch as an exact tuple:

```text
item + field + current value -> proposed value
```

Record the factual source, affected list and detail consumers, and visual-fit risk. Keep item values, schema, bindings, relationships, slugs, assets, indexing, collection or item creation, hiding, and publication effects distinct. CMS value authority does not imply authority for any of the others.

Before an atomic CMS batch, refresh item identities, current values, relevant schema and bindings, and known consumers. On current-value drift, stop before mutation unless the user explicitly authorized divisible application and the unaffected subset remains unambiguous.

## Batch and apply approved content

Batch enumerated work only when targets share dependencies, effect class, and a reliable validation method. Do not create a project-wide batch that can go stale or conceal indivisible drift.

Apply targets and values covered by the request or approved map, including choices the user delegated. Preserve content, objects, visual tokens, schema, bindings, relationships, assets, and publication state outside that scope. Follow [live-change-validation.md](live-change-validation.md) for every live mutation.

Read back every changed value and validate every materially distinct consumer, including intended local overrides and affected responsive states. When exhaustive validation of generated CMS pages or equivalent consumers is impractical, inspect declared representative and edge cases and disclose the sampling basis and limitation.

An unpublished surface may include a not-yet-available destination when preparation is within scope; record the condition needed before activation. A normal read-only check of a supplied public URL can be part of authorized link or launch validation. Respect instructions not to visit it, access boundaries, and links that could trigger actions. Do not probe unrelated systems or publish a known broken path unless the user has accepted that effect within the publication grant.

Do not create separate ledger-only acceptance gates. Focused validation, semantic success, a bounded same-scope correction, and the corresponding tracker update remain inside coherent application authority.

## Maintain the compact tracker

Use the axes defined in `SKILL.md`. Create a tracker only when multi-unit scope or an existing project contract needs one and write authority exists.

Use `undecided`, `uninspected`, or another accurate nonterminal state until evidence or an explicit decision supports a change. Record `defer` or `exclude` only from an explicit user disposition. Keep implementation, activation, and publication independent: validated content can remain activation-blocked and unpublished.

Update only changed rows once per run. Summarize material transitions and named blockers instead of reproducing the full tracker.

## Pause, defer, exclude, and close out

A request to move to another module pauses unfinished work; it does not silently defer, exclude, approve, validate, or close it. Preserve accurate nonterminal states and continue only within the newly authorized effect boundary.

Close a unit or multi-unit scope only when the tracker and live evidence support its stated decision, implementation, activation, and publication states. Optional modules need not run for content work to close. Report the remaining named triggers or decisions without manufacturing additional gates.
