# Contributing

This repository is the maintained source for the published skills. Make changes here, then update installed copies through the relevant installer.

## Add or update a skill

Use `skills/<skill-name>/SKILL.md`. Choose a lowercase name with hyphens between words and start with YAML frontmatter:

```yaml
---
name: skill-name
description: Explain what the skill does and when an agent should use it.
---
```

State the task, the steps that matter, and how to check the result. Describe required capabilities and useful fallbacks without assuming one provider's tools. Keep references, scripts, assets, an MIT `LICENSE`, and required third-party notices inside the skill's directory so they travel with an individual installation.

Leave invocation to the installer and host. Do not ship forced invocation settings or require an explicit command merely to select a relevant skill. Preserve precise scope boundaries and authorization for consequential actions. When modernizing an existing installation, preserve the user's valid settings and controlling policy.

Update the README catalog with the purpose, inputs, default output, and capabilities. Check discovery:

```sh
npx skills add . --list
```

## Validate the change

Parse frontmatter and structured resources, check names and relative references, and inspect the files an individual installation receives. Try new or changed behavior on a representative task and the relevant failure or boundary case. Reuse checks across skills when they establish the same behavior. Run live integrations only in an authorized environment and identify unavailable checks honestly.

For detector software changes, run:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills/ai-slop-detector/scripts -p 'test_*.py'
```

Reporting changes also need a focused behavioral check: derive concise and detailed responses from the same completed assessment, preserve serious findings and material limits, and request scores independently of detail. Calculator tests alone cannot validate these decisions or the rubric's editorial accuracy.

Rerun checks when a change affects what they establish. Record material behavior, schema, or rubric changes in the relevant documentation and commit description; keep version and comparison limits explicit. See the [Agent Skills specification](https://agentskills.io/specification) and [skills CLI documentation](https://github.com/vercel-labs/skills#creating-skills).

## Review public content

Everything pushed here becomes public, including Git history. Before committing:

- Review every included file, including scripts, examples, attachments, and metadata. Use invented example data instead of private source material.
- Remove credentials, tokens, private keys, personal contact details, private URLs, account identifiers, and local-machine paths. The maintainer's public name and GitHub username belong in the project documentation.
- Keep configuration and credentials outside skill directories. Document required environment-variable names without their values.
- Inspect the staged file list and `git diff --cached`. Run a secret scanner. Ignore rules and automated scans help catch mistakes but do not replace reading the files.
- Confirm permission to publish included material. Preserve required attribution and license notices for third-party contributions.

Preparing a local candidate does not publish it. Pushing a branch or opening a public pull request exposes its contents, so finish publication checks before that boundary. Do not include private corpora or raw assessment records to substantiate a claim; use authorized, minimized evidence or qualify the claim.

If a credential is committed, revoke or rotate it. Deleting it from current files does not remove it from history.

## Write documentation

Explain what the skill does, when to use it, what it returns, and what it requires. Use concrete examples and plain language. Describe limitations where they affect the result. Distinguish documented compatibility from tested installation, observed behavior, and live integration results.

Give each skill a `README.md` with a short description, its installation command, a numbered process, and the details a reader needs to use it. Link to `SKILL.md` for the full instructions and `LICENSE` for the terms. Keep the README aligned with the instructions without duplicating the complete workflow.

Respect the assignment, intended voice, and language conventions before applying generic cleanup preferences. Preserve facts and useful qualifications. Keep ordinary output concise unless the task calls for more detail.

## License

Submit original contributions under the repository's [MIT license](LICENSE). Include that license in each distributable skill folder. Identify third-party material and its terms before adding it.
