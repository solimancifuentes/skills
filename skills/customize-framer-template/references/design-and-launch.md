# Design and Launch Modules

Use only the modules relevant to the user's requested or approved visual, metadata, launch, or publication effects.

## Contents

- [Color styles](#color-styles)
- [Typography](#typography)
- [Image inventory](#image-inventory)
- [Generated images](#generated-images)
- [Image placement](#image-placement)
- [SEO](#seo)
- [Launch audit](#launch-audit)
- [Review and publish](#review-and-publish)

## Color styles

Color work is optional unless the user requests it or it is needed for an approved visual direction. Audit reusable styles, semantic roles, local overrides, major consumers, interactive states, and contrast before mutation. Treat shared-style changes as guarded: enumerate affected consumers and distinguish gradients, images, logos, screenshots, code components, warning or error roles, and one-off colors.

Map the smallest role-based change to existing reusable styles. Do not create duplicate styles or recolor authentic identity, screenshots, proof, or unrelated local overrides unless those exact effects are authorized. Validate affected consumers and materially distinct responsive or interaction states.

## Typography

Typography is optional unless requested or required by an approved visual direction. Confirm font availability and any file or license the user must supply. Audit reusable text styles, local typography, hierarchy, and representative consumers before proposing the smallest reusable mapping.

Shared typography changes are guarded. Preserve unapproved sizes, weights, line heights, spacing, hierarchy, and layout. Validate wrapping, clipping, and hierarchy on affected consumers and materially distinct responsive states. Exact approved copy must not be silently rewritten to accommodate a font change.

## Image inventory

Inspect how each relevant asset serves its surrounding content. Capture enough about its source, container, cropping, responsive display, and accessibility treatment to judge whether it can be retained or replaced. Identify assets whose role requires authentic evidence. An inventory-only request stays read-only; a broader image-editing request may already cover replacement.

Keep logos, product screenshots, customer evidence, certifications, identity photography, and real interfaces authentic.

## Generated images

Use generation where the request covers it and the asset serves a decorative or illustrative role. Define the intended appearance using the target's proportions, surrounding content, and expected crops. Supply only references authorized for the chosen service. Do not fabricate business evidence or identity assets. Generation and placement can proceed together when the request covers both; otherwise return the generated asset for the next decision.

## Image placement

Resolve the asset and destination from the request and inspected project. If placement is delegated, choose a compatible slot and apply it without an additional exact-target approval. Retain the container's established styling and responsive behavior unless their adjustment is in scope. Preserve a recoverable prior asset, and use the smallest crop or positioning correction that produces the intended result.

Use truthful alt text or mark an image decorative as appropriate. Validate the affected materially distinct responsive states without claiming accessibility-tree behavior that the available tooling cannot expose.

## SEO

Read-only SEO audits may batch related public pages. For each relevant route, distinguish title, description, H1 guidance, social image, internal links, indexing, route changes, CMS metadata bindings, unresolved inputs, and duplicate metadata. Use only verified business facts; do not invent keywords, services, locations, claims, or proof.

Classify application by actual effect. Metadata edits may be routine or guarded, while indexing and route changes depend on their material impact. CMS binding changes, analytics, domains, and external services are consequential. Apply values within the authorized scope, including choices delegated by the user, and report Page Settings, site settings, or platform behavior that cannot be verified.

## Launch audit

Run launch review read-only unless fixes are included in the request. Check, as relevant:

- template names, placeholder copy, demo claims, proof, and assets;
- navigation, footer, CTA, contact, and internal-link destinations;
- forms and success states without submitting them;
- demo CMS content and CMS-bound routes;
- alt text, metadata, social images, indexing, and unresolved activation triggers;
- legal, contact, and 404 surfaces without inferring legal conclusions; and
- clipping, wrapping, focus or interaction risks, and horizontal overflow across materially distinct responsive states.

Group findings by consequence and distinguish verified findings from manual or unverified checks. Do not send messages, submit forms, complete transactions, change external services, or broaden the audit into an unrelated domain investigation.

## Review and publish

Review the frozen candidate and cumulative material changes without publishing. Distinguish proposed, approved, applied, validated, activation-blocked, manual, unpublished, and published states. Reconfirm the exact project, candidate, editing path, material scope, and unresolved must-fix findings.

Publishing requires an explicit grant covering the project, candidate, and material publication effects. A still-applicable request to make the changes and publish can supply that grant; do not require a second approval merely because preparation is complete. Prior implementation, validation, readiness review, or a planned date alone is insufficient. Immediately before publishing, refresh identity and material drift predicates. Stop on material drift.

Use the authorized environment's supported Framer publishing path. After a confirmed publish result, read back the live domain and repeat the critical-path checks covered by the task. Keep live readback distinct from pre-publish review. On an uncertain result, inspect deployment and live state before any retry, republish, rollback, or new external action; never imply success without evidence.
