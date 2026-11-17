# slopx

Edit or review a draft so that it says something specific and true, with every fact intact. slopx works on substance first (the point, what each sentence carries, whether anything was made up) and on phrasing last.

## Installation

Use an inspected local copy of this repository at a revision you choose. Copy the whole `skills/slopx` directory into your agent's local skills directory, keeping `SKILL.md`, `references/`, `scripts/` and `agents/` together.

The installed files contain the editing instructions and helper script. The helper uses Python's standard library and makes no network requests. Optional citation checks use the agent's read-only web tools under the content-handling rules in `SKILL.md`.

## Process

1. Work out who reads the text and what they need, and read the reference file for its kind: work, social, technical, academic or fiction.
2. List the protected facts: numbers, names, dates, quotations, links, citations and code.
3. Fix substance. Lead with the point, cut sentences that carry nothing, say each thing once, and cut whole passages first when the text must be shorter.
4. Handle gaps without inventing anything. Ask the user, or cut the vague sentence and list what is missing. Check the draft against itself, and report hidden characters and citations that could not be checked.
5. Fix structure, then phrasing.
6. Compare the protected facts with the draft again, then return the edit followed by short notes that cite rule ids.

## What to provide

Supply the draft and say where it will go. Say if it must be shorter or ready to send as it is. When the draft lacks a fact, slopx asks for it or lists it instead of making one up.

The default output is the edited text, then three short sections: changes, what the edit still needs from you, and a fact check. Ask whether a draft is slop, or ask for a review, to get findings without a rewrite.

## Helper script

`scripts/check.py` needs Python 3.8 or later and no packages.

- `python3 scripts/check.py scan FILE` lists the protected facts, hidden characters, chat leftovers, pattern counts per 1,000 words, and shape measures such as paragraph length and dash density.
- `python3 scripts/check.py diff BEFORE AFTER` shows facts that an edit removed or introduced, and exits 1 when it finds any.
- `python3 scripts/check.py selftest` runs the built-in checks.

The script is a net, not a guarantee. It misses a name that only ever opens a sentence and numbers written as words, so the instructions also ask for a manual list. Without Python, the skill does the comparison by hand.

## Limits

slopx is an editor, not an AI detector or a humanizer, and it never judges who wrote a text. It does not review what code does or judge visual design.

It was tried on eight invented drafts: a status email, an incident write-up, a LinkedIn post, a Medium article, an X article, a website blog post, LinkedIn comments and X replies. Each case ran once per version and was graded by the authoring model, not by human editors, so the results show behavior on those drafts and not general accuracy. The check of a draft against itself still misses some contradictions.

## Related skills

[anti-slop-editor](../anti-slop-editor/README.md) is a lighter edit that returns only the revision. [ai-slop-detector](../ai-slop-detector/README.md) gives structured, scored audits. slopx is a fuller edit with fact protection and notes, plus a review mode without scores.

[Full instructions](SKILL.md) · [MIT license](LICENSE)
