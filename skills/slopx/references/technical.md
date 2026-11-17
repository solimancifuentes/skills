# Technical writing: docs, READMEs, commit messages, PR descriptions, code comments

A reviewer or maintainer reads this text to decide what to do with code. Anything in it that they cannot verify against the code costs them time.

## Commit messages and PR descriptions

State what changed in behavior, where, and why. A good one names files, functions, issue numbers and the test that covers the change.

Remove:

- Titles made of general verbs: "Enhance robustness and improve overall code quality", "Refactor X to improve maintainability while preserving existing behavior".
- Claims with nothing behind them: "production-ready", "comprehensive", "robust", "all tests pass". Keep "tests pass" only if the user ran them, and then say which.
- Statements about what was not done: "preserved", "retained", "avoided", "ensured compliance with".
- Lists of benefits ("more scalable going forward") in place of a description of the change.
- Praise of the reviewer in replies: "You're absolutely right!" followed by no answer to the point.

Format:

- A commit message is plain text: a subject of about 50 characters, a blank line, then a body. No Markdown headings, bold or emoji (T2).
- Follow the convention the repository already uses for prefixes and issue references.
- Trailers such as `Co-Authored-By:` are disclosure. Leave them.

Never claim something the diff does not show. If the description says a test was added and you cannot see it, take the claim out and say so in the notes, so the author can put it back with the test's name (F1).

Example:

> Before: Refactored authentication module to enhance maintainability and ensure robust error handling while preserving existing functionality.
>
> After: auth: return 401 instead of 500 when the token is expired (#88)

The "After" is only possible if the user or the diff supplies the status codes and the issue number.

## Code comments

- Delete a comment that restates the line below it.
- Keep a comment that gives a reason the code cannot show: why this order, why this limit, which bug this works around.
- Do not change code, identifiers or string literals while editing comments (F2).

## Docs and READMEs

- Start with what the thing does and how to run it. Cut "Welcome to" and mission statements.
- Replace adjectives with behavior: "blazing fast" becomes the measured time, if there is one. If there is none, cut the claim.
- Commands, flags, paths, version numbers and code blocks are protected (F2). Check each one against the original after editing.
- Keep headings, lists and code fences where the docs are rendered as Markdown. They belong there.
- One name per concept (P5). Docs that call the same thing a "job", a "task" and a "run" make readers look for three things.
- Do not create summary or report files nobody asked for.

## Outside this file

Whether the code is correct, whether tests were weakened, and whether helpers are duplicated are code-review questions. This skill edits the words.
