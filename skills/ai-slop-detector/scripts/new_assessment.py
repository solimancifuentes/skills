#!/usr/bin/env python3
"""Create an unreviewed assessment scaffold; never invent findings or clean ratings."""

import argparse
import json
from pathlib import Path
import sys

from score import AssessmentError, DEFAULT_RUBRIC, read_json, validate_rubric


def build_scaffold(text, purpose, *, genre="Unspecified; establish during review",
                   audience="Unspecified; establish during review", language="Unspecified",
                   assessor_id="pending-assessor", assessor_type="model",
                   word_count_reliable=True, index_requested=False):
    rubric = read_json(DEFAULT_RUBRIC)
    validate_rubric(rubric)
    if not text.strip() or not purpose.strip():
        raise ValueError("text and purpose must be nonempty")
    return {
        "rubric_version": rubric["version"],
        "text": text,
        "context": {
            "genre": genre, "audience": audience, "language": language,
            "purpose": purpose, "scope": "Complete supplied text",
            "word_count_reliable": word_count_reliable,
        },
        "materials": {},
        "exclusions": [],
        "pattern_checks": {
            key: {"status": "not_checked", "reason": "Unreviewed scaffold; complete the actual check."}
            for key in rubric["patterns"]
        },
        "findings": [],
        "dimensions": {
            key: {
                "status": "not_checked", "scope": "none", "rating": None,
                "reason": "Unreviewed scaffold; establish evidence and scope before rating.",
                "finding_ids": [],
            }
            for key in rubric["dimensions"]
        },
        "evaluation": {
            "assessor_id": assessor_id,
            "assessor_type": assessor_type,
            "assessment_stage": "single_assessor",
            "verification": {
                "mode": "not_performed",
                "description": "No review or factual verification has been performed by this scaffold generator.",
            },
            "provenance": "Replace with the actual evaluator configuration, date, known settings, and unknowns.",
            "limitations": ["This is an unreviewed scaffold, not an editorial assessment."],
            "counterevidence": [],
        },
        "index_requested": index_requested,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text_file", type=Path, help="UTF-8 target text, preserved exactly")
    parser.add_argument("--purpose", required=True, help="Actual reader task; not a scoring instruction")
    parser.add_argument("--genre", default="Unspecified; establish during review")
    parser.add_argument("--audience", default="Unspecified; establish during review")
    parser.add_argument("--language", default="Unspecified")
    parser.add_argument("--assessor-id", default="pending-assessor")
    parser.add_argument("--assessor-type", choices=("human", "model", "mixed"), default="model")
    parser.add_argument("--word-count-unreliable", action="store_true")
    parser.add_argument("--index", action="store_true", help="Request an index after review; initial scaffold is ineligible")
    args = parser.parse_args(argv)
    try:
        # newline='' prevents conversion of CRLF in the preserved target.
        with args.text_file.open(encoding="utf-8", newline="") as stream:
            text = stream.read()
        data = build_scaffold(
            text, args.purpose, genre=args.genre, audience=args.audience, language=args.language,
            assessor_id=args.assessor_id, assessor_type=args.assessor_type,
            word_count_reliable=not args.word_count_unreliable, index_requested=args.index,
        )
    except (AssessmentError, OSError, UnicodeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
