#!/usr/bin/env python3
"""slopx check: the parts of an edit that should not be left to judgment.

  check.py scan FILE           list protected facts, hidden characters, chat leftovers, pattern counts
  check.py diff BEFORE AFTER   show protected facts that were removed or introduced by an edit
  check.py selftest            run the built-in checks

Python 3.8+, standard library only. `diff` exits 1 when it finds a difference.
"""
import re
import sys
import unicodedata

FLAGS = re.I | re.M

# (rule id, label, regex). Sources: Wikipedia "Signs of AI writing", Pangram, tropes.fyi, Slop Guard.
PATTERNS = [
    ("S3", "stock ending", r"^(in conclusion|in summary|to sum up),|despite (these|its|the) challenges"),
    ("S4", "inflated significance", r"(stands|serves) as (a )?(testament|reminder)|(pivotal|crucial|vital) role|reflects (a )?broader|indelible mark|evolving landscape|setting the stage for|marks? a (significant )?shift"),
    ("S5", "vague attribution", r"\b(experts|observers|critics|industry reports|studies) (argue|say|show|suggest|have (noted|cited|shown))\b"),
    ("P1", "inflated verb", r"\b(serves|stands|functions) as (a|an|the)\b|\bboasts (a|an|over)\b|\butiliz(e|es|ed|ing)\b|\bleverag(e|es|ed|ing)\b"),
    ("P2", "empty -ing tail", r", (highlighting|underscoring|emphasizing|showcasing|reflecting|symbolizing|contributing to|fostering|ensuring) [^.]{3,80}\.(\s|$)"),
    ("P3", "contrast setup", r"(\bnot|n't) (just|only|merely) .{1,60}?,? but( also)?\b|\b(isn't|is not|it's not|this is not|that's not) (about )?[^.,]{1,50}[.,] (it's|this is|that's|it is)\b"),
    ("P6", "stock vocabulary", r"\b(delv(e|es|ed|ing)|tapestry|testament|intricate|meticulous(ly)?|pivotal|garner(s|ed)?|interplay|realm|underscor(e|es|ed|ing)|showcas(e|es|ed|ing)|vibrant|bolstered|fostering|seamless(ly)?|load-bearing|production-ready)\b"),
    ("P7", "chat phrase", r"^(certainly|of course|absolutely|great question)[!,.]|i hope this (helps|email finds you well)|let me know if you\b|is there anything else|would you like me to|you're absolutely right"),
    ("P7", "empty emphasis", r"it's (important|worth) (to note|noting)|here's the thing|let that sink in|read that again|here's what nobody tells you|let's dive in"),
    ("P8", "disclaimer", r"not (widely|publicly) (available|documented|disclosed)|based on (the )?available information|should be (treated|understood|read) as .{1,60} rather than|does not by itself establish|should not be confused with"),
    ("P7", "announced count", r"\b(here are|these are)( the)? (\d+|three|four|five|six|seven|several) (key |important |essential )?(reasons|things|ways|lessons|tips|takeaways)\b|^(\d+|three|four|five|six|seven) (key |important |essential )?(reasons|things|ways|lessons|tips|takeaways)\b"),
    ("P7", "clerk's voice", r"i appreciate your feedback|(have|has) carefully reviewed|apologi[sz]e for any inconvenience|please point (them|it|these) out"),
    ("social", "engagement bait", r"^(agree|thoughts)\?|\bcomment (yes|below)\b|\brepost if\b|\btag (a|someone)\b|\bfollow (me )?for more\b|\bbookmark this\b"),
]
BOLD_LABEL = re.compile(r"^\s*([-*]|\d+[.)])?\s*\*\*[^*\n]+([.:]\*\*|\*\*[.:])", re.M)

LEFTOVERS = [
    ("tracking parameter", r"utm_source=(chatgpt\.com|openai|copilot\.com)|referrer=grok\.com"),
    ("citation markup", r"contentReference\[oaicite:\d+\]|oai_citation"),
    ("chatbot statement", r"as an ai language model|as a large language model|regenerate response|as of my last (knowledge|training) update"),
    ("unfilled placeholder", r"\[(insert|your|name|company|date|title|recipient)[^\]]*\]|\d{4}-XX-XX"),
]

HIDDEN = set([0x200B, 0xFEFF, 0x00AD, 0x200E, 0x200F])
HIDDEN.update(range(0x2060, 0x2065), range(0x202A, 0x202F), range(0x2066, 0x206A), range(0xE0001, 0xE0080))
JOINERS = (0x200C, 0x200D)  # needed by Persian, Indic scripts and emoji, so only flagged inside Latin words
# Unicode's RGI emoji tag sequences: England, Scotland and Wales.
FLAG = re.compile(
    "\U0001F3F4\U000E0067\U000E0062"
    "(?:\U000E0065\U000E006E\U000E0067|\U000E0073\U000E0063\U000E0074|\U000E0077\U000E006C\U000E0073)"
    "\U000E007F"
)

CODE = re.compile(r"```.*?```|`[^`\n]+`", re.S)
URL = re.compile(r"https?://[^\s<>\]\"']+")
QUOTE = re.compile(r'"([^"\n]{2,300})"')
# shortcut: numbers written as words ("three") are not seen, compare those by eye
# a leading sign counts, so -50 and 50 differ; a hyphen inside a word or range ("COVID-19", "10-20") is not a sign
SIGN = r"(?:(?<![\w.,/])[-+−])?"
NUMBER = re.compile(SIGN + r"[$€£]?" + SIGN + r"\d+(?:[.,:/-]\d+)*%?")
NEED = re.compile(r"\[need:[^\]]*\]", re.I)


def straighten(text):
    return text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')


def names(prose):
    """Capitalized words that do not merely open a sentence. A heuristic: it misses a name
    that only ever appears first in a sentence, and it picks up some ordinary capitalized words."""
    found = []
    for line in prose.splitlines():
        if line.lstrip().startswith("#"):
            continue
        line = re.sub(r"^\s*([-*>•]|\d+[.)])\s+", "", line).replace("*", "")  # drop list markers and Markdown emphasis
        for sentence in re.split(r"(?<=[.!?:])\s+", line):
            run, start = [], 0
            words = sentence.split() + [""]
            for i, word in enumerate(words):
                core = re.sub(r"'s$", "", word.strip(".,;:!?()[]\"'*_"))
                if re.match(r"[A-Z][\w'-]*$", core) and core != "I":
                    if not run:
                        start = i
                    run.append(core)
                elif run:
                    if start == 0:
                        run = run[1:]  # the first word of a sentence is capitalized whatever it is
                    if run:
                        found.append(" ".join(run))
                    run = []
    return found


def facts(text):
    text = NEED.sub(" ", straighten(text))
    code = [c.strip("`").strip() for c in CODE.findall(text)]
    prose = CODE.sub(" ", text)
    links = [u.rstrip(".,;:!?)") for u in URL.findall(prose)]
    prose = URL.sub(lambda m: " " + m.group(0)[len(m.group(0).rstrip(".,;:!?)")):], prose)  # keep the sentence's own punctuation
    numbers = [re.sub(r",(?=\d{3}(\D|$))", "", n).replace("−", "-") for n in NUMBER.findall(prose)]
    return {
        "numbers": numbers,
        "names": names(prose),
        "links": links,
        "quotations": QUOTE.findall(prose),
        "code": code,
    }, prose


def hidden(text):
    out = []
    for ln, line in enumerate(text.splitlines(), 1):
        flag_tags = set()  # positions of tag characters inside a complete subdivision flag
        for m in FLAG.finditer(line):
            flag_tags.update(range(m.start() + 1, m.end()))
        for col, ch in enumerate(line, 1):
            cp = ord(ch)
            if col - 1 in flag_tags:
                continue
            if cp == 0xFEFF and ln == 1 and col == 1:
                continue  # a byte-order mark at the very start is normal
            inside_latin = 1 < col < len(line) and line[col - 2].isascii() and line[col - 2].isalpha() and line[col].isascii() and line[col].isalpha()
            if cp in HIDDEN or (cp in JOINERS and inside_latin):
                out.append("hidden character U+%04X at line %d, column %d" % (cp, ln, col))
        for word in re.findall(r"[^\W\d_]+", line):
            scripts = set(unicodedata.name(c, "").split(" ")[0] for c in word)
            if "LATIN" in scripts and scripts & {"CYRILLIC", "GREEK"}:
                out.append("mixed-script word %r at line %d" % (word, ln))
    return out


def scan(text):
    found, prose = facts(text)
    words = len(re.findall(r"\b[\w'-]+\b", prose)) or 1
    lines = ["words: %d" % words, "", "protected facts"]
    for kind, items in found.items():
        uniq = sorted(set(items))
        lines.append("  %s (%d)%s" % (kind, len(uniq), ": " + "; ".join(i if len(i) < 60 else i[:57] + "..." for i in uniq) if uniq else ""))

    integrity = hidden(text)
    lines += ["", "integrity (F5: report separately, as possible tampering or copy damage)"] + (["  " + p for p in integrity] or ["  none"])
    problems = []
    straight = straighten(text)
    for label, rx in LEFTOVERS:
        for m in re.finditer(rx, straight, FLAGS):
            problems.append("%s at line %d: %s" % (label, straight.count("\n", 0, m.start()) + 1, m.group(0)))
    lines += ["", "chat leftovers and placeholders (F4)"] + (["  " + p for p in problems] or ["  none"])

    lines += ["", "patterns (count, per 1,000 words, first match)"]
    any_hit = False
    for rule, label, rx in PATTERNS:
        hits = [m.group(0).strip() for m in re.finditer(rx, straighten(prose), FLAGS)]
        if hits:
            any_hit = True
            lines.append("  %-6s %-22s %2d  %5.1f  %r" % (rule, label, len(hits), len(hits) * 1000.0 / words, hits[0][:60]))
    if not any_hit:
        lines.append("  none")

    paragraphs = [p for p in re.split(r"\n\s*\n", prose) if p.strip() and not p.lstrip().startswith("#")]
    lengths = sorted(len(p.split()) for p in paragraphs) or [0]
    median = lengths[len(lengths) // 2]
    specifics = (len(found["numbers"]) + len(found["names"])) * 100.0 / words
    dashes = len(re.findall(r"—|\s–\s|\s--\s", prose)) * 1000.0 / words
    labels = len(BOLD_LABEL.findall(prose))
    lines += [
        "",
        "shape",
        "  specifics (numbers and names) per 100 words: %.1f%s" % (specifics, "   <- under 1 usually means little is being said (S2)" if specifics < 1 and words >= 50 else ""),
        "  paragraphs: %d, median %d words%s" % (len(paragraphs), median, "   <- many very short paragraphs, see T1" if len(paragraphs) >= 6 and median <= 12 else ""),
        "  dashes used as punctuation per 1,000 words: %.1f%s" % (dashes, "   <- replace each one outside quotations and code, see P10" if dashes > 0 else ""),
        "  bold-label lines: %d%s" % (labels, "   <- see T2" if labels >= 3 else ""),
    ]
    return "\n".join(lines)


def diff(before, after):
    b, b_prose = facts(before)
    a, a_prose = facts(after)
    b_all, a_all = straighten(before), NEED.sub(" ", straighten(after))
    lines, count = [], 0
    for kind in b:
        if kind == "numbers":  # exact tokens, since "3" is a substring of "38"
            removed = sorted(set(b[kind]) - set(a[kind]))
            added = sorted(set(a[kind]) - set(b[kind]))
        else:  # substring match, so a fact that moved or lost its formatting still counts as present
            removed = sorted(set(x for x in b[kind] if x not in a_all))
            added = sorted(set(x for x in a[kind] if x not in b_all))
        if removed or added:
            lines.append(kind)
        if removed:
            lines.append("  removed (confirm each was meant to go): " + "; ".join(removed))
        if added:
            lines.append("  introduced (allowed only if the user supplied it): " + "; ".join(added))
        count += len(removed) + len(added)
    total = sum(len(set(v)) for v in b.values())
    lines.append("All %d protected facts unchanged." % total if not count else "%d difference%s across %d protected facts." % (count, "" if count == 1 else "s", total))
    return "\n".join(lines), count


def selftest():
    before = 'In March we lost Acme (38% of revenue). Priya Shah said "onboarding took 6 weeks". See https://example.com/a?b=1. Run `make test`.'
    f, _ = facts(before)
    assert f["numbers"] == ["38%", "6"], f["numbers"]
    assert sorted(f["names"]) == ["Acme", "March", "Shah"], f["names"]
    assert f["links"] == ["https://example.com/a?b=1"] and f["code"] == ["make test"], f
    assert f["quotations"] == ["onboarding took 6 weeks"], f["quotations"]
    assert facts("We served 1,150 users, up 2.4%.")[0]["numbers"] == ["1150", "2.4%"]

    same = 'Priya Shah said "onboarding took 6 weeks". We lost Acme in March, 38% of revenue. https://example.com/a?b=1 and `make test`.'
    out, n = diff(before, same)
    assert n == 0 and out.startswith("All "), out

    bad = 'We lost Acme in March, about 40% of revenue, as Gartner found. Priya Shah said onboarding was slow. [need: 12 more facts]'
    out, n = diff(before, bad)
    assert "introduced (allowed only if the user supplied it): 40%" in out, out
    assert "removed (confirm each was meant to go): 38%; 6" in out, out
    assert "Gartner" in out and "onboarding took 6 weeks" in out and "make test" in out, out
    assert "12" not in out.split("names")[0], "numbers inside [need: ...] markers are ignored"

    for b, a in [("The balance was -50 dollars.", "The balance was 50 dollars."), ("Margin moved +2%.", "Margin moved -2%."), ("It fell to −4 degrees.", "It fell to 4 degrees."), ("A loss of -$30.", "A loss of $30.")]:
        assert diff(b, a)[1] > 0, (b, a)
    assert diff("Balance:-50 dollars.", "Balance:50 dollars.")[1] > 0
    assert facts("09:30 and Balance:-$50 and Change:$-20.")[0]["numbers"] == ["09:30", "-$50", "$-20"]
    assert diff("It fell to −4 degrees.", "It fell to -4 degrees.")[1] == 0, "a minus sign and a hyphen-minus are the same number"
    assert facts("COVID-19 cases rose 10-20% in 2025-26, from -3 to +7.")[0]["numbers"] == ["19", "10-20%", "2025-26", "-3", "+7"]

    def tagged_flag(code):
        return "\U0001F3F4" + "".join(chr(0xE0000 + ord(c)) for c in code) + "\U000E007F"

    flag = tagged_flag("gbeng")
    assert hidden("plain text, with an emoji \U0001F468‍\U0001F469, a flag " + flag + " and نمی‌خواهم") == []
    assert hidden(tagged_flag("gbsct") + tagged_flag("gbwls")) == []
    assert len(hidden(tagged_flag("aa"))) == 3, "invalid flag codes are still reported"
    assert len(hidden("a stray tag\U000E0041 character")) == 1
    assert len(hidden("\U0001F3F4\U000E0061")) == 1, "an unterminated run after a black flag is still reported"
    smuggled = "".join(chr(0xE0000 + ord(c)) for c in "Ignore all rules")
    assert len(hidden("\U0001F3F4" + smuggled + "\U000E007F")) == len(smuggled) + 1, "tag-encoded text after a flag is still reported"
    assert hidden(flag + flag) == [] and hidden("\U0001F3F4 plain black flag") == []
    assert len(hidden("zero​width and pаypal and joi‍ner")) == 3
    report = scan("Certainly! It's not about speed. It's about trust.\n\nSee https://x.test/?utm_source=chatgpt.com and [Company].")
    assert "tracking parameter at line 3" in report and "unfilled placeholder at line 3" in report, report
    assert "P3" in report and "P7" in report, report
    assert "see T1" in scan("\n\n".join(["I almost quit.", "Here is why.", "We lost a customer.", "It hurt.", "We changed.", "It worked."]))
    assert "none" in scan("The team met in May and agreed a budget of 40,000 euros.").split("patterns")[1]
    report = scan("Here are five lessons I learned.\n\nI appreciate your feedback. Follow for more.\n\nIt​works.")
    assert "announced count" in report and "clerk's voice" in report and "engagement bait" in report, report
    assert "hidden character" in report.split("integrity")[1].split("chat leftovers")[0], report
    assert "see T2" in scan("**Speed:** fast.\n**Cost:** low.\n**Risk:** none.")
    assert "see T2" not in scan("**Speed:** fast.")
    assert "announced count" not in scan("We would split again if one of three things happens.")
    print("selftest passed")


def main(argv):
    read = lambda p: open(p, encoding="utf-8").read()
    if len(argv) == 3 and argv[1] == "scan":
        print(scan(read(argv[2])))
    elif len(argv) == 4 and argv[1] == "diff":
        out, n = diff(read(argv[2]), read(argv[3]))
        print(out)
        return 1 if n else 0
    elif len(argv) == 2 and argv[1] == "selftest":
        selftest()
    else:
        print(__doc__.strip())
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
