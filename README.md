# Skills

The central home for the AI agent skills I use, maintained by [Soliman Cifuentes](https://github.com/solimancifuentes). Each skill will contain instructions for a specific task, with supporting files where they help the agent do the work.

No skills have been added yet. I'll choose which ones to publish as the collection takes shape.

## Install

Once skills are available, install them with the [skills CLI](https://github.com/vercel-labs/skills). You'll need Node.js and npm, which provides `npx`.

```sh
npx skills add solimancifuentes/skills
```

To see the available skills without installing them:

```sh
npx skills add solimancifuentes/skills --list
```

These commands will report no skills until the first one is published. The CLI reads skills directly from this GitHub repository; this collection does not need a separate npm package.

## Repository layout

Published skills will live in `skills/`, with one directory per skill:

```text
skills/
└── skill-name/
    ├── SKILL.md
    ├── references/    # Optional supporting documentation
    ├── scripts/       # Optional executable helpers
    └── assets/        # Optional templates and other files
```

Each `SKILL.md` defines the skill's name, describes when to use it, and gives the agent its instructions. See [Contributing](CONTRIBUTING.md) for the format and publication checks.

## Discovery on skills.sh

According to the [skills.sh FAQ](https://skills.sh/docs/faq), skills are listed automatically when users install them through the CLI with telemetry enabled. Installation counts determine their ranking. Publishing this repository prepares it for that process; it does not create a listing by itself.

## License

[MIT](LICENSE). Copyright (c) 2026 Soliman Cifuentes.
