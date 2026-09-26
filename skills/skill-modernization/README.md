# Skill modernization

Review existing skills against current evidence, preserve guidance that works, and make focused updates when the request authorizes them.

## Installation

```sh
npx skills add solimancifuentes/skills --skill skill-modernization
```

## Process

1. Locate the requested skills and distinguish their maintained source, installed copies, and generated caches.
2. Check the instructions against relevant documentation, available capabilities, and realistic usage. Separate demonstrated defects from suggestions and unresolved claims.
3. Recommend the smallest useful correction, or edit the maintained source when changes are authorized.
4. Run available structural checks and behavioral evaluations appropriate to the change. Report actual results and verification limits.

## What to provide

Identify the skills, their intended users or outcomes, and whether you want a review or updates. Relevant usage failures can help define evaluation cases. The default is review and recommendations; a supported no-change result is valid.

The report explains each material finding, its practical effect, and the proposed or completed correction. It distinguishes prepared source, installed files, and runtime behavior. A successful file check cannot establish that the host loaded the update.

## Source and settings stay under your control

Reading a target skill does not run its workflow or setup. The skill preserves pinned versions, owner-selected invocation settings, and unrelated metadata. Editing, installation, hook changes, and publication stay within your authorization. Host-specific helpers are optional, and missing validators are reported as limitations. Private conversations and raw evaluation evidence stay out of shared reports unless needed and authorized.

[Full instructions](SKILL.md) · [MIT license](LICENSE)
