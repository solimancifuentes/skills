# Contributing

This repository collects the skills Soliman Cifuentes uses. The initial setup contains no skills; additions will be selected later.

## Add a skill

Create `skills/<skill-name>/SKILL.md`. Use a lowercase name with hyphens between words, and start the file with YAML frontmatter:

```yaml
---
name: skill-name
description: Explain what the skill does and when an agent should use it.
---
```

Follow the frontmatter with the instructions. State the task, the steps that matter, and how the agent should check its work. Document any required tools or services. Keep supporting references, scripts, and assets inside the skill's directory so they travel with it when installed.

Update the README with the skill's name and purpose. Check that the CLI can discover it:

```sh
npx skills add . --list
```

Try the skill on a representative task before publishing. For format details, see the [Agent Skills specification](https://agentskills.io/specification) and the [skills CLI documentation](https://github.com/vercel-labs/skills#creating-skills).

## Review public content

Everything committed here becomes public, including the Git history. Before committing:

- Review every file being added, including scripts, examples, attachments, and file metadata. Use invented example data instead of private source material.
- Remove credentials, access tokens, private keys, personal contact details, private URLs, account identifiers, and paths copied from a local machine. The maintainer's public name and GitHub username belong in the project documentation.
- Keep local configuration and credentials outside skill directories. Document the environment variables a skill needs without including their values.
- Check the staged changes with `git diff --cached` and the file list with `git diff --cached --name-only`. Run a secret scanner before publishing skill additions. Ignore rules and automated scans help catch mistakes, but neither replaces reading the files.
- Confirm that you have permission to publish every included file. Preserve any required attribution and license notices for third-party material.

If a credential is committed, revoke or rotate it immediately. Deleting it from the current files does not remove it from Git history.

## Write documentation

Explain what the skill does, when to use it, and what it requires. Use concrete examples and plain language. Describe limitations where they affect the result.

## License

Submit original contributions under the repository's [MIT license](LICENSE). Identify third-party material and its license before adding it.
