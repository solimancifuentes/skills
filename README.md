# Skills

The central home for the AI agent skills I use, maintained by [Soliman Cifuentes](https://github.com/solimancifuentes). These eleven skills cover writing, research, design, and agent workflows. Each folder contains a README with installation and usage details, the agent's instructions in `SKILL.md`, and any supporting resources.

## The collection

| Skill | Use it for | Inputs and default output | Capabilities |
| --- | --- | --- | --- |
| [ai-slop-detector](skills/ai-slop-detector/README.md) | Structured editorial audits | Text and relevant sources → concise findings; detailed reports and unvalidated scores are separate requests | Reference access; optional Python 3 helpers with a manual fallback |
| [anti-slop-editor](skills/anti-slop-editor/README.md) | Removing filler while preserving meaning | Draft and editing brief → revised prose | Text and context access |
| [applied-feasibility-analysis](skills/applied-feasibility-analysis/README.md) | Evaluating ideas or business practices for a project | Candidate, project evidence, and constraints → inline assessment, or a dossier for broader business analysis | Evidence access; browsing and file writing when relevant |
| [company-intelligence-profile](skills/company-intelligence-profile/README.md) | Sourced, dated company research | Company identity and research purpose → inline informational profile | Public research or supplied sources; current claims need current evidence |
| [customize-framer-template](skills/customize-framer-template/README.md) | Adapting an existing Framer template | Template and factual brief → content map or authorized changes | Authorized Framer connection for live work; optional component and image tools |
| [design-system-extraction](skills/design-system-extraction/README.md) | Extracting reusable design rules | Source files or a live site → Markdown specification and token JSON | Source access or a permitted browser; file writing for deliverables |
| [pragmatic-builder](skills/pragmatic-builder/README.md) | Concrete, candid nonfiction | Topic, draft, context, or evidence → original prose, revision, or requested feedback | Text and context access; optional research access |
| [process-debt-audit](skills/process-debt-audit/README.md) | Finding unnecessary process | Project history and operational evidence → read-only diagnosis and recommendations | Supplied records or authorized project access |
| [skill-modernization](skills/skill-modernization/README.md) | Reviewing and improving skills | Skill source and relevant evidence → findings or authorized revisions | Source access; editing, current documentation, and validation as needed |
| [sparc](skills/sparc/README.md) | Matching assurance to an action's effects | Task, effects, and authority → proportionate workflow and checks | Context access; operational tools only for authorized execution |
| [writing-style-profile](skills/writing-style-profile/README.md) | Describing and applying a writing style | Authorized samples and brief → profile, draft, or evaluation | Sample and reference access; optional file output |

The writing skills serve different tasks. An edit does not require a detector audit, and using an existing voice does not require extracting a new profile. When combining skills, the assignment and selected voice take precedence over generic cleanup preferences.

## Install

The [skills CLI](https://github.com/vercel-labs/skills) reads this repository directly; no separate npm package is needed. CLI 1.7.0 requires Node.js 22.20.0 or later and npm, which provides `npx`.

For a published revision:

```sh
npx skills add solimancifuentes/skills
```

List available skills or choose one:

```sh
npx skills add solimancifuentes/skills --list
npx skills add solimancifuentes/skills --skill anti-slop-editor
```

For an unpublished local checkout, inspect its contents with `npx skills add . --list`. To install that checkout, run `npx skills add /path/to/skills` from the project that should receive the skills. Remote commands can only see files already published on GitHub.

Installers and hosts determine discovery, automatic selection, and permissions. These packages do not impose an invocation policy. Optional `agents/openai.yaml` files provide interface metadata; the core instructions do not depend on them. Selecting a skill does not authorize publication, disclosure of private material, or unrelated external changes.

## Compatibility

The canonical format is a [standard skill folder](https://agentskills.io/specification): `SKILL.md`, relative resources, and a license. Provider-neutral instructions still need the capabilities listed above.

| Application | Distribution and limits |
| --- | --- |
| Codex, Cursor, Claude Code, Grok Build | Documented skill-folder support. The CLI supports agent-specific destinations. Tool access and behavior depend on each host. See [OpenAI](https://learn.chatgpt.com/docs/build-skills), [Cursor](https://prod.cursor.com/docs/skills), [Claude Code](https://code.claude.com/docs/en/skills), and [Grok Build](https://docs.x.ai/build/features/skills-plugins-marketplaces). |
| ChatGPT | Installation depends on the surface and its standalone-skill or plugin support. Follow [the current instructions](https://learn.chatgpt.com/docs/build-skills); `npx` is not a universal chat installer. |
| Claude chat | Supports custom uploads through its [skill workflow](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Runtime and network capabilities can differ from Claude Code. |
| Grok chat and Grok Bot | Saved skills are documented, but full multi-file import and helper execution for this collection are unverified. See [Grok skills](https://x.ai/news/grok-skills) and [Grok Bot](https://docs.x.ai/grok-bot/skills-routines-and-automations). |

These are documented integration routes, not a claim of equal behavior across models. Distinguish package installation, instruction behavior, and live tool execution when reporting compatibility. Missing capabilities must remain visible in the result.

Local checks on September 25, 2026 used skills CLI 1.7.0 and Node.js 24.14.1 to discover and copy all eleven packages into a temporary Codex project, including their licenses and references. The detector's 47 software tests passed with Python 3.14.7. Bounded GPT-6 Astra trials exercised reporting, invocation-setting preservation, read-only recommendations, writing-skill composition, and private report content. Other host runtimes and live integrations have not been tested for this release.

## Limits and private information

The detector is an unvalidated editorial aid, not an AI-authorship classifier. Its helper tests check software invariants; they do not establish detection accuracy. Style profiles and voice transfer also depend on the supplied evidence, language, genre, and evaluator.

Reports can contain the material used to produce them. Detector records retain source text and can retain excluded quotations. Exclusion from evaluation is not redaction. Review and minimize sensitive content before sharing reports, screenshots, profiles, or evidence records. Keep private source collections and generated assessments outside this repository.

## Contribute and maintain

See [Contributing](CONTRIBUTING.md) for package structure, publication checks, and focused validation. Maintain each skill here rather than allowing installed copies to become undocumented variants.

## Discovery on skills.sh

According to the [skills.sh FAQ](https://skills.sh/docs/faq), skills are listed automatically when users install them through the CLI with telemetry enabled. Installation counts determine ranking. Publishing the repository makes the skills available for that process; publication alone does not create a listing.

## License

[MIT](LICENSE). Copyright (c) 2026 Soliman Cifuentes. Every skill carries its own license so the notice travels with an individual installation. Retain applicable third-party notices, including the detector's [upstream notices](skills/ai-slop-detector/THIRD_PARTY_NOTICES.txt). Linked third-party works remain governed by their own terms.
