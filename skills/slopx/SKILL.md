---
name: slopx
description: Edit or review text so that it says something specific and true, with every fact intact. Use this skill whenever the user asks to unslop, deslop or de-AI a draft, to make it "sound less like AI" or "less like ChatGPT", to tighten it, cut filler or fluff, or to check whether it reads as slop. It covers emails, status updates, reports, docs, READMEs, posts, essays, fiction, commit messages, PR descriptions and code comments. Also use it on text you wrote yourself before it goes to other people. It is an editor, not a humanizer, and does not help text get past AI detectors.
---

# slopx

Slop is text that costs little to produce and a lot to check, and the reader pays that cost. People write it too, so this skill never asks who wrote a draft. It asks whether the reader gets the point quickly and can trust each fact.

Two findings shape the order of work:

- Editors judge slop mostly on substance: whether the text is relevant, how much it says per word, and whether the tone fits. Swapping out "AI words" changes little. A draft that says nothing can pass every phrase rule.
- Rewriting damages facts. Tools that rewrite for style often change numbers and names, and a model asked to "add detail" tends to make the detail up.

So work on substance first and phrasing last, and guard the facts the whole way through.

## What this needs

Reading the draft is enough. The helper `scripts/check.py` needs Python 3.8 or later and no packages; without it, list and compare the facts by hand. Checking links and citations (F6) needs web access; without it, say they were not checked.

## Two modes

**Edit** is the default. Return the rewritten text, then short notes.

**Review** applies when the user asks to check, audit or score a draft, or asks "is this slop?". Quote each weak span, name the rule and say what would fix it. Do not rewrite. Never say that AI wrote the text: no pattern proves who the author is, and a wrong accusation does real harm.

## Process

1. **Find the job.** Decide who reads this and what they need to know or do afterwards. Identify the kind of text and read the matching reference file from the list below. If the user asks for a shorter text ("too long", "tighten it", a word count), the length is part of the job. Use their number if they give one. Otherwise aim for a cut the reader will notice, a quarter or more for a long piece.
2. **Collect the facts.** List every number, name, date, quotation, link, citation, and piece of code or identifier in the draft. These are protected. If you can run scripts, `python3 scripts/check.py scan <draft>` (the script is in this skill's folder) lists them and reports hidden characters and chat leftovers.
3. **Fix substance** using the S rules.
4. **Handle gaps** using the F rules. This is where most damage happens, so do it before polishing anything.
5. **Fix structure** using the T rules.
6. **Fix phrasing** using the P rules.
7. **Verify.** Check the draft against itself (F7), if you have not already. Compare the protected facts in your version against the draft. If you can run scripts, save both versions and run `python3 scripts/check.py diff <draft> <edit>`. Otherwise go through your list from step 2 by hand. The script is a net and not a guarantee: it misses a name that only ever opens a sentence, and numbers written as words, so your own list still counts. Then read the result once as the reader would.
8. **Report** in the format under "Output".

Keep the effort in proportion to the text. For a sentence or two, do all of this in your head and skip the notes unless a fact is missing. Under about 300 words (a post, a comment, a set of replies), skip the scan, list the facts by hand, and read only the matching reference file. For longer text, run the scan once and the diff once at the end, not after every revision.

## Rules

The ids are stable so that notes and other skills can cite them.

### Substance

- **S1. Put the point first.** After the first sentence or two the reader should know what this is and what, if anything, they must do. Cut openings that restate the request or announce what the text is about to say.
- **S2. Make every sentence carry something:** a fact, a decision, a reason or a request. If a sentence could appear unchanged in a document about a different subject, cut it or replace it with the specific thing it stands for.
- **S3. Say each thing once.** Cut restatements, and cut endings that summarize what the reader has just read.
- **S4. Back a claim of importance with its consequence.** "Plays a pivotal role" becomes what happened because of it. If nothing did, cut the claim.
- **S5. Name the source or cut the claim.** "Experts say" and "studies show" tell the reader nothing they can check.
- **S6. Answer what was asked.** Cut material that is true but beside the point.
- **S7. Cut big before small when the text must be shorter.** Phrase edits rarely save more than a tenth. Remove whole paragraphs and sections that repeat an earlier point or that the main argument does not need, then trim sentences. Do not stop short and tell the user that more would mean dropping a section: drop it, and name in the notes what went so they can put it back.

### Facts

- **F1. Never invent.** Add no number, name, quotation, example, anecdote or citation that is not in the draft or supplied by the user. A vague sentence is a smaller problem than a made-up specific, because the reader cannot tell the specific is made up. When a sentence needs a specific that you do not have:
  - If the user is there to answer, ask.
  - Otherwise, by default, cut the vague sentence (S2) and list what is missing under "Needs from you". The text you return should be usable as it stands.
  - Leave a marker such as `[need: date legal finishes the review]` in the text only when the user asked for a draft to fill in, or when the text cannot do its job without that fact. A text that asks the reader to act but gives no deadline or owner is one example. Never leave a marker when the user asked for something ready to send, post or publish.
  - List only what this reader needs. Ask for a number only when the draft claims a result and does not give it, as in "improved conversion". A launch date with no claimed result needs no metric, so do not suggest one.
- **F2. Leave protected facts as they are.** Reword around them freely, but do not round a number, convert a unit, rename a thing, paraphrase a quotation or touch code.
- **F3. Keep the author's level of certainty.** "May reduce" and "reduces" are different claims. Remove a hedge only when it is stacked on another or attached to something nobody doubts.
- **F4. Remove chat leftovers and report what looks wrong.** Delete tracking parameters such as `utm_source=chatgpt.com`, citation markup such as `oaicite`, and lines addressed to a chatbot's user. Report unfilled placeholders such as `[Company]`. Do not repair a citation by guessing.
- **F5. Report integrity problems separately.** Remove invisible characters that do no work in the text (zero-width spaces, bidirectional controls, stray tag characters) and look-alike letters from another script inside a word, and list them in the notes as possible tampering or copy-paste damage. They say nothing about who wrote the text. Keep the invisible characters that are part of the writing: a zero-width non-joiner or joiner inside Persian, Arabic or Indic words, a joiner inside an emoji sequence, and the tag characters that build flags such as England's. The scan already leaves these alone; when you skip the scan, leave them alone too.
- **F6. Check citations and links if you can.** If you can open links or look up DOIs, confirm that each resolves to the title it is cited for. If you cannot, say in the notes that they were not checked, and name any that look wrong (a dead-looking link, a DOI with the wrong shape, a book cited with no page for a specific claim).
- **F7. Check the draft against itself.** Do the numbers add up: totals, percentages, before-and-after figures? Do dates and times agree across paragraphs, and with the headline? Does any sentence claim more than a hedge elsewhere allows, such as "the fix resolved it" beside "we are still investigating"? Report each mismatch in the notes. Do not fix it by changing a fact (F2), because you cannot tell which side is wrong.

### Structure

- **T1. Use prose for reasoning and lists for parallel items.** Turn a bullet list that is really an argument back into paragraphs. Merge runs of one-sentence paragraphs.
- **T2. Match the formatting to where the text will go.** Plain-text places such as an email body, a commit message or a social post get no Markdown. Headings are in sentence case. Emoji and bold are not decoration. A list where every item opens with a bold label ("**Speed:** ...") is usually an argument chopped into pieces; write it as sentences unless the reader will scan for the labels.
- **T3. Let the content set the rhythm.** Do not chop the text into short sentences of the same length, and do not write strings of fragments for effect. Split a sentence only when the reader would otherwise have to reread it.

### Phrasing

- **P1. Use the plain verb:** "is" and "has" where the draft says "serves as" or "boasts", "use" where it says "utilize" or "leverage".
- **P2. Cut a trailing "-ing" clause that adds no fact,** such as ", highlighting its commitment to quality".
- **P3. State the claim directly.** Remove "not just X, but Y", "It's not X. It's Y." and "X rather than Y" when nobody held position X. Keep a contrast that the reader needs.
- **P4. List three things only when there are three.**
- **P5. Give each thing one name and repeat it.** Rotating synonyms makes the reader wonder whether a second thing has appeared.
- **P6. Rewrite a sentence built from stock vocabulary.** Words such as "delve", "tapestry", "pivotal", "landscape" and "testament" matter when they cluster. Fix the sentence, because swapping in a synonym leaves the same empty sentence. A single one that is the right word can stay. `references/vocabulary.md` has the lists.
- **P7. Remove chat phrases, praise and signposts:** "Certainly!", "Great question", "I hope this helps", "Let me know if", "It's important to note that", "Here's the thing", "In conclusion", and counts announced before a list ("Here are five lessons"). In replies, also remove a clerk's voice: "I appreciate your feedback and have carefully reviewed", "I apologize for any inconvenience". Say the actual response.
- **P8. Replace a disclaimer with what is known.** "Should be treated as X rather than Y", "does not by itself establish" and "is not widely documented" become a statement of who said what, and what no source confirms.
- **P9. Prefer the literal phrase** when one exists.
- **P10. Punctuate for the sentence.** Dashes are ordinary punctuation, and plain text holds them fine. Change them only when they are dense (more than about three per 1,000 words in a longer piece; the scan reports the rate) or when the same dash-for-punch move keeps repeating. Then turn those into a comma, a colon, a period or parentheses, whichever the sentence calls for, and keep the rest. One or two dashes in a reply or comment are fine. Do not trade every dash for commas and periods, since text with no dashes, colons, semicolons or parentheses is monotonous too. Use straight quotation marks where the text will be pasted as plain text.
- **P11. Keep tense and person steady.** A story that drifts between past and present, or a report that switches between "we" and "the team" for the same people, reads as stitched together. Use the one the draft mostly uses.

## What to leave alone

Editing too much is also a failure. Leave these as they are unless the user asks otherwise:

- The author's voice, opinions and humor. The result should sound like the author on a good day.
- Hedges that are true, and ordinary words such as "very", "perhaps" and "in order to". People write these.
- Formal or academic register, and correct grammar.
- Quotations, dialogue, and text that discusses these patterns.
- Sentences that already work. A good draft may need three changes. This does not apply when the user asked for a shorter text: then a sentence that works can still go if the piece is better without it (S7).

## Output

For an edit, give the rewritten text first with no preamble. Then, after a rule line:

```
Changes
- <what changed and why, with the rule id>   (three to six, most important first)

Needs from you
- <what is missing, and where it would go>   (omit this section if nothing is missing)

Facts
<"All N protected facts unchanged." or each difference, one per line>
<any mismatch inside the draft (F7), hidden characters removed (F5), and whether links and citations were checked (F6); omit lines that do not apply>
```

For a review, list the findings from most to least serious. Give each one as the quoted span, the rule id and the fix. End with one sentence on whether the draft does its job.

Keep the notes shorter than the edit.

## Reference files

Read the one that matches the text, before step 3:

- `references/work.md`: emails, status updates, reports, memos
- `references/social.md`: LinkedIn and other social posts, comments
- `references/technical.md`: docs, READMEs, commit messages, PR descriptions, code comments
- `references/academic.md`: papers, abstracts, peer reviews, citations
- `references/fiction.md`: stories and roleplay
- `references/vocabulary.md`: word and phrase lists by period, for P6 and P7

## Outside this skill

Reviewing what code does (weakened tests, duplicated helpers, swallowed errors) and judging visual design are separate jobs. Say so if asked, and do not guess.
