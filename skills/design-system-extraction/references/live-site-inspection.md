# Live-site inspection

Use this reference when inspecting a rendered site. Adapt the sampling to the requested scope and available browser; no single tool or browser API is assumed.

## Establish coverage

Open the requested URL and identify distinct page types, shared navigation, repeated sections, and task-relevant interactions. Start with representative desktop and narrow mobile layouts using actual viewport sizes supported by the tool. Record those sizes. Add intermediate widths or boundary samples when a layout changes; do not assume familiar device widths are the site's breakpoints.

Check the page after relevant content and fonts have loaded. Record visible loading failures, consent overlays, authentication boundaries, and missing assets that affect observations. Stay within the inspected site or clearly related task scope; do not follow every link by default.

For a small site, one landing page and one different content/form page may establish useful coverage. For an application, prefer a representative flow and its shared elements. These are sampling examples, not completeness thresholds. Stop expanding when additional pages repeat the inspected patterns and remaining gaps do not materially affect the requested handoff. Briefly record discovered page families, samples, material omissions, and the stopping rationale. Record browser, locale, preferences, or other environment conditions when they materially affect findings.

## Inspect appearance and structure together

Use screenshots or direct visual inspection for hierarchy and composition, plus available DOM, computed-style, matched-rule, or stylesheet evidence for exact values. Scope queries to relevant elements; avoid dumping entire DOM trees or every computed property.

| Area | Evidence to collect and distinctions to preserve |
| --- | --- |
| Typography | Family stack and resources, size and unit basis (including root font size for `rem`), weight, line height, tracking, text measure, and wrapping. A declared/computed stack or loaded resource does not prove the face used per glyph; mark actual rendering unverified without suitable inspection. |
| Color | Text, surfaces, borders, accents, feedback, opacity, and state/theme changes. Preserve alpha and color space; distinguish declared color from a visually composited result. |
| Spacing and layout | Container widths, gutters, grid/flex behavior, gaps, padding, alignment, and section positions. Inspect how adjacent spacing combines into page rhythm; separate element dimensions from reusable rules. Retain unusual values when supported. |
| Shape and depth | Border widths/styles, radii, shadows, overlays, and stacking behavior where relevant. Rounded shapes do not establish one global radius. |
| Motion | Trigger or driver (time, scroll, state), changed properties, duration, easing, and reduced-motion behavior when accessible. Source rules establish declared motion, not observed animation. |
| Assets | References and roles; intrinsic bounds/aspect ratio, displayed size/crop, and baked-in treatment relevant to reuse. For logos, distinguish visible artwork from file bounds. For behavior-dependent media, record relevant player/loading dependencies and active/inactive behavior. Inventory without bulk downloads or assumed reuse rights. |

Computed values are snapshots of the cascade at a particular viewport, state, and environment. Where available, inspect the matching declaration to retain `rem`, `clamp()`, `calc()`, custom-property relationships, and media/container conditions. Do not infer an exact breakpoint from two screenshots. If a tool cannot resize or inspect rules, document only the observed layout and the limit.

## Components and interaction states

For representative components and assemblies, inspect how typography, containers, spacing, surfaces, assets, and content constraints work together. Collect enough context to describe reusable component contracts and page compositions, rather than cataloging every element. Record variants and responsive changes to anatomy, order, or behavior as well as size. A CSS class or HTML tag alone does not establish a reusable component API.

Check relevant focus, hover/press, disabled, selected, loading, error, and empty states, plus keyboard behavior, labels, text expansion, and reduced motion. This is a coverage check, not a requirement to invent or exercise every state on every component. Record the trigger, effect, persistence, and reversal where material; repeated or competing inputs may expose differences. Distinguish observed, declared-only, and unavailable states. A selected appearance does not establish a navigation or data effect.

Use supported UI interactions for behavioral verification. Do not inject a class, attribute, or DOM edit and report the result as the site's native behavior. Where interactions could send data or change an account, prefer non-submitting inspection and source evidence. Local fixtures explicitly provided for testing can be exercised within their stated scope.

For accessibility-related observations, name the check: keyboard navigation, visible focus, labels, semantics, or measured contrast with known foreground/background conditions. Do not turn those checks into a claim of full accessibility compliance. If focus or semantics were inspected only in source, say so.

## Themes, embeds, and limitations

- Keep light/dark modes and breakpoint-specific values distinct. A mode not reached is unverified even when its rules appear in CSS.
- Identify embedded services through evidence such as iframe origin, attribution, component boundaries, or supplied source. A visually different section alone does not prove third-party ownership.
- Catalog a third-party widget separately from the host system. Same-origin embedding does not make its styling a host design rule. Respect cross-origin tool limits.
- If a page is blocked or a state unavailable, record the actual response or visible condition. Do not invent a login screen, hidden content, or behavior beyond it.
- Reconcile source/deployment differences in the specification. Avoid inferring their cause, release version, or author intent without evidence.

Save screenshots only where they materially substantiate a finding; they are not a mandatory archive. Inspect captures for private account or customer data before adding them to deliverables. Keep necessary originals private and share a cropped or redacted view when it preserves the design evidence. Record asset identity without exposing signed URLs or downloading assets outside the requested scope.
