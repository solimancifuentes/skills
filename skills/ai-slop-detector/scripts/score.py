#!/usr/bin/env python3
"""Validate a version-2 editorial profile and an optional unvalidated rubric index.

This helper does not detect linguistic patterns, verify claims, or infer authorship.
"""

import argparse
import json
from fractions import Fraction
from pathlib import Path
import re
import sys


VERSION = "2.0"
PATTERN_STATUSES = ("reviewed", "not_applicable", "not_assessable", "not_checked")
DIMENSION_STATUSES = ("assessed", "not_applicable", "not_assessable", "not_checked")

DEFAULT_RUBRIC = Path(__file__).resolve().parents[1] / "references" / "rubric.json"


class AssessmentError(ValueError):
    """An input contradicts the assessment contract."""


def fail(path, message):
    raise AssessmentError(f"{path}: {message}")


def object_fields(value, path, required, optional=()):
    if not isinstance(value, dict):
        fail(path, "must be an object")
    missing = set(required) - value.keys()
    unknown = value.keys() - set(required) - set(optional)
    if missing:
        fail(path, "missing keys: " + ", ".join(sorted(missing)))
    if unknown:
        fail(path, "unknown keys: " + ", ".join(sorted(unknown)))


def string(value, path):
    if not isinstance(value, str) or not value.strip():
        fail(path, "must be a nonempty string")
    return value


def array(value, path, nonempty=False):
    if not isinstance(value, list) or (nonempty and not value):
        fail(path, "must be " + ("a nonempty array" if nonempty else "an array"))
    return value


def integer(value, path, minimum, maximum=None):
    if type(value) is not int or value < minimum or (maximum is not None and value > maximum):
        bound = f"{minimum}–{maximum}" if maximum is not None else f"at least {minimum}"
        fail(path, f"must be an integer {bound}; booleans are not integers")
    return value


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            fail("JSON", f"duplicate object key {key!r}")
        result[key] = value
    return result


def reject_constant(value):
    fail("JSON", f"nonstandard numeric constant {value!r}")


def read_json(path):
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=no_duplicate_keys, parse_constant=reject_constant)


def quote_span(item, source_text, path):
    quote = string(item["quote"], path + ".quote")
    positions = []
    cursor = source_text.find(quote)
    while cursor != -1:
        positions.append(cursor)
        cursor = source_text.find(quote, cursor + 1)
    if not positions:
        fail(path + ".quote", "does not occur exactly in its source")
    if "occurrence" in item:
        occurrence = integer(item["occurrence"], path + ".occurrence", 1)
        if occurrence > len(positions):
            fail(path + ".occurrence", f"source has only {len(positions)} occurrence(s)")
    elif len(positions) > 1:
        fail(path + ".occurrence", f"required because the quote occurs {len(positions)} times")
    else:
        occurrence = 1
    start = positions[occurrence - 1]
    end = start + len(quote)
    return {
        "quote": quote,
        "occurrence": occurrence,
        "start": start,
        "end": end,
        "line_start": source_text.count("\n", 0, start) + 1,
        "line_end": source_text.count("\n", 0, end - 1) + 1,
    }


def overlaps(left, right):
    return left["start"] < right["end"] and right["start"] < left["end"]


def link_only(value):
    return re.fullmatch(r"(?:https?://\S+|<https?://[^>]+>|\[[^\]]*\]\(https?://\S+\))",
                        value.strip(), flags=re.IGNORECASE) is not None


def validate_rubric(rubric):
    object_fields(rubric, "rubric", {
        "version", "minimum_words", "provisional_below_words", "minimum_coverage", "dimensions", "patterns"
    })
    string(rubric["version"], "rubric.version")
    integer(rubric["minimum_words"], "rubric.minimum_words", 1)
    integer(rubric["provisional_below_words"], "rubric.provisional_below_words", rubric["minimum_words"])
    integer(rubric["minimum_coverage"], "rubric.minimum_coverage", 1, 100)
    dimensions = rubric["dimensions"]
    if not isinstance(dimensions, dict) or len(dimensions) != 8:
        fail("rubric.dimensions", "must define exactly eight dimensions")
    for dimension, definition in dimensions.items():
        object_fields(definition, f"rubric.dimensions.{dimension}", {"label", "weight"})
        string(definition["label"], f"rubric.dimensions.{dimension}.label")
        integer(definition["weight"], f"rubric.dimensions.{dimension}.weight", 1, 100)
    if sum(item["weight"] for item in dimensions.values()) != 100:
        fail("rubric.dimensions", "weights must sum to 100")
    patterns = rubric["patterns"]
    if not isinstance(patterns, dict) or set(patterns) != {f"P{i:02d}" for i in range(1, 58)}:
        fail("rubric.patterns", "must define P01 through P57 exactly once")
    for pattern, dimension in patterns.items():
        if not isinstance(dimension, str) or dimension not in dimensions:
            fail(f"rubric.patterns.{pattern}", "unknown dimension")


def choice(value, path, values):
    if not isinstance(value, str) or value not in values:
        fail(path, "must be one of: " + ", ".join(values))
    return value


def string_array(value, path):
    for index, item in enumerate(array(value, path)):
        string(item, f"{path}[{index}]")


def nonoverlapping_locations(spans):
    """Maximum number of disjoint supplied spans, not independent incidents."""
    end = -1
    count = 0
    for span in sorted(spans, key=lambda item: (item["end"], item["start"])):
        if span["start"] >= end:
            count += 1
            end = span["end"]
    return count


def outcome(supported, tentative, reviewed=True):
    if not reviewed:
        return "not_reviewed"
    if supported and tentative:
        return "supported_and_tentative"
    if supported:
        return "supported"
    if tentative:
        return "tentative"
    return "no_supported_finding"


def assess(data, rubric=None):
    """Validate evidence and return all profiles; only calculate a requested index."""
    if isinstance(data, dict) and data.get("rubric_version") == "1.0":
        fail("rubric_version", "version-1 assessments require an explicit version-2 reassessment with "
             "pattern states, purpose, extent, dimension scope, and evaluator metadata; no automatic migration")
    rubric = read_json(DEFAULT_RUBRIC) if rubric is None else rubric
    validate_rubric(rubric)
    if rubric["version"] != VERSION:
        fail("rubric.version", f"this helper requires version {VERSION!r}")
    object_fields(data, "assessment", {
        "rubric_version", "text", "context", "materials", "exclusions",
        "pattern_checks", "findings", "dimensions", "evaluation"
    }, {"index_requested"})
    if data["rubric_version"] != rubric["version"]:
        fail("rubric_version", f"must be {rubric['version']!r}")
    requested = data.get("index_requested", False)
    if type(requested) is not bool:
        fail("index_requested", "must be a boolean")
    text = string(data["text"], "text")
    context = data["context"]
    object_fields(context, "context", {"genre", "audience", "language", "scope", "purpose", "word_count_reliable"})
    for key in ("genre", "audience", "language", "scope", "purpose"):
        string(context[key], "context." + key)
    if type(context["word_count_reliable"]) is not bool:
        fail("context.word_count_reliable", "must be a boolean")

    evaluation = data["evaluation"]
    object_fields(evaluation, "evaluation", {
        "assessor_id", "assessor_type", "assessment_stage", "verification", "provenance", "limitations", "counterevidence"
    })
    for key in ("assessor_id", "provenance"):
        string(evaluation[key], "evaluation." + key)
    choice(evaluation["assessor_type"], "evaluation.assessor_type", ("human", "model", "mixed"))
    choice(evaluation["assessment_stage"], "evaluation.assessment_stage", ("single_assessor", "independent", "adjudicated"))
    object_fields(evaluation["verification"], "evaluation.verification", {"mode", "description"})
    choice(evaluation["verification"]["mode"], "evaluation.verification.mode", ("not_performed", "supplied_only", "external_sources"))
    string(evaluation["verification"]["description"], "evaluation.verification.description")
    for key in ("limitations", "counterevidence"):
        string_array(evaluation[key], "evaluation." + key)

    materials = data["materials"]
    if not isinstance(materials, dict):
        fail("materials", "must be an object mapping source names to supporting text strings")
    for source, material in materials.items():
        string(source, "materials source name")
        if source == "text":
            fail("materials.text", "the target source name 'text' is reserved")
        string(material, "materials." + source)
    sources = {"text": text, **materials}
    pattern_dimensions = rubric["patterns"]
    checks = data["pattern_checks"]
    object_fields(checks, "pattern_checks", set(pattern_dimensions))
    for pattern, check in checks.items():
        path = "pattern_checks." + pattern
        object_fields(check, path, {"status"}, {"reason"})
        choice(check["status"], path + ".status", PATTERN_STATUSES)
        if check["status"] != "reviewed" or "reason" in check:
            string(check.get("reason"), path + ".reason")
    conditional_unavailable = set()
    if "original" not in materials:
        conditional_unavailable.update(("P50", "P51", "P52"))
        if "voice_reference" not in materials:
            conditional_unavailable.update(("P48", "P49"))
    if not materials:
        conditional_unavailable.update(("P54", "P55", "P56", "P57"))
    for pattern in sorted(conditional_unavailable):
        if checks[pattern]["status"] == "reviewed":
            fail("pattern_checks." + pattern, "cannot be reviewed without its required supporting material")

    exclusions = []
    for index, exclusion in enumerate(array(data["exclusions"], "exclusions")):
        path = f"exclusions[{index}]"
        object_fields(exclusion, path, {"quote", "reason"}, {"occurrence"})
        reason = string(exclusion["reason"], path + ".reason")
        span = {**quote_span(exclusion, text, path), "reason": reason}
        if any(overlaps(span, previous) for previous in exclusions):
            fail(path, "overlaps another exclusion")
        exclusions.append(span)

    findings = {}
    for index, finding in enumerate(array(data["findings"], "findings")):
        path = f"findings[{index}]"
        object_fields(finding, path, {
            "id", "patterns", "primary_dimension", "impact", "confidence", "evidence", "explanation", "improvement", "extent"
        }, {"overlap_reason"})
        finding_id = string(finding["id"], path + ".id")
        if finding_id in findings:
            fail(path + ".id", f"duplicate finding ID {finding_id!r}")
        patterns = array(finding["patterns"], path + ".patterns", nonempty=True)
        seen_patterns = set()
        for pattern in patterns:
            if not isinstance(pattern, str) or pattern not in pattern_dimensions:
                fail(path + ".patterns", f"unknown pattern {pattern!r}")
            if pattern in seen_patterns:
                fail(path + ".patterns", f"duplicate pattern {pattern!r}")
            if checks[pattern]["status"] != "reviewed":
                fail(path + ".patterns", f"{pattern} must have status reviewed to support a finding")
            seen_patterns.add(pattern)
        primary = string(finding["primary_dimension"], path + ".primary_dimension")
        if primary not in rubric["dimensions"]:
            fail(path + ".primary_dimension", "unknown dimension")
        if primary not in {pattern_dimensions[pattern] for pattern in patterns}:
            fail(path + ".primary_dimension", "must match at least one listed pattern")
        integer(finding["impact"], path + ".impact", 1, 4)
        choice(finding["confidence"], path + ".confidence", ("high", "medium", "low"))
        for key in ("explanation", "improvement"):
            string(finding[key], path + "." + key)
        if "overlap_reason" in finding:
            string(finding["overlap_reason"], path + ".overlap_reason")
        extent = finding["extent"]
        object_fields(extent, path + ".extent", {"scope", "recurrence", "coverage", "explanation"})
        choice(extent["scope"], path + ".extent.scope", ("local", "distributed", "document"))
        choice(extent["recurrence"], path + ".extent.recurrence", ("single", "repeated", "not_established"))
        choice(extent["coverage"], path + ".extent.coverage", ("complete", "illustrative"))
        string(extent["explanation"], path + ".extent.explanation")
        evidence = []
        for evidence_index, item in enumerate(array(finding["evidence"], path + ".evidence", nonempty=True)):
            evidence_path = f"{path}.evidence[{evidence_index}]"
            object_fields(item, evidence_path, {"source", "quote"}, {"occurrence"})
            source = string(item["source"], evidence_path + ".source")
            if source not in sources:
                fail(evidence_path + ".source", f"unknown source {source!r}")
            span = {"source": source, **quote_span(item, sources[source], evidence_path)}
            if any(span["source"] == previous["source"] and span["start"] == previous["start"]
                   and span["end"] == previous["end"] for previous in evidence):
                fail(evidence_path, "duplicates another evidence span in this finding")
            if source == "text" and any(overlaps(span, excluded) for excluded in exclusions):
                fail(evidence_path, "overlaps excluded target text")
            evidence.append(span)
        evidence_sources = {item["source"] for item in evidence}
        if "text" not in evidence_sources:
            fail(path + ".evidence", "requires at least one excerpt from text")
        for pattern in patterns:
            if pattern in ("P48", "P49") and not evidence_sources.intersection({"original", "voice_reference"}):
                fail(path + ".evidence", f"{pattern} requires original or voice_reference evidence")
            if pattern in ("P50", "P51", "P52") and "original" not in evidence_sources:
                fail(path + ".evidence", f"{pattern} requires original evidence")
            if pattern in ("P54", "P55", "P56", "P57"):
                contextual = [item for item in evidence if item["source"] != "text"]
                if not contextual:
                    fail(path + ".evidence", f"{pattern} requires an excerpt from a contextual material")
                if not any(not link_only(item["quote"]) and not link_only(sources[item["source"]])
                           for item in contextual):
                    fail(path + ".evidence", f"{pattern} requires a contextual excerpt, not merely a link")
        target_locations = [item for item in evidence if item["source"] == "text"]
        location_count = nonoverlapping_locations(target_locations)
        if (extent["recurrence"] == "repeated" or extent["scope"] == "distributed") and location_count < 2:
            fail(path + ".extent", "repeated or distributed claims require at least two nonoverlapping target evidence spans")
        findings[finding_id] = {
            **finding, "evidence": evidence,
            "status": "tentative" if finding["confidence"] == "low" else "supported",
            "target_evidence_locations": target_locations,
            "nonoverlapping_target_evidence_location_count": location_count,
        }

    finding_list = list(findings.values())
    for index, finding in enumerate(finding_list):
        target_spans = finding["target_evidence_locations"]
        for other in finding_list[index + 1:]:
            other_spans = other["target_evidence_locations"]
            if any(overlaps(left, right) for left in target_spans for right in other_spans):
                if not finding.get("overlap_reason") or not other.get("overlap_reason"):
                    fail("findings", f"{finding['id']} and {other['id']} share target-text spans; "
                         "each needs overlap_reason explaining the distinct defect")

    dimensions = data["dimensions"]
    object_fields(dimensions, "dimensions", set(rubric["dimensions"]))
    for dimension, assessment in dimensions.items():
        path = "dimensions." + dimension
        object_fields(assessment, path, {"status", "scope", "rating", "reason", "finding_ids"},
                      {"impact_summary", "extent_summary"})
        choice(assessment["status"], path + ".status", DIMENSION_STATUSES)
        choice(assessment["scope"], path + ".scope", ("full", "restricted", "none"))
        string(assessment["reason"], path + ".reason")
        assessed = assessment["status"] == "assessed"
        rating = assessment["rating"]
        if assessed:
            integer(rating, path + ".rating", 0, 4)
            if assessment["scope"] == "none":
                fail(path + ".scope", "assessed dimensions require full or restricted scope")
        elif rating is not None or assessment["scope"] != "none":
            fail(path, "unassessed dimensions require null rating and none scope")
        for key in ("impact_summary", "extent_summary"):
            if assessed or key in assessment:
                string(assessment.get(key), path + "." + key)
        assigned_statuses = [checks[pattern]["status"] for pattern, assigned in pattern_dimensions.items()
                             if assigned == dimension]
        if assessed and "reviewed" not in assigned_statuses:
            fail(path, "cannot be assessed when every assigned pattern is non-reviewed")
        if assessment["scope"] == "full" and any(status in ("not_assessable", "not_checked") for status in assigned_statuses):
            fail(path + ".scope", "full scope cannot include not_assessable or not_checked patterns; use restricted scope")
        if assessment["status"] == "not_applicable" and any(status != "not_applicable" for status in assigned_statuses):
            fail(path, "not_applicable dimensions require all assigned patterns to be not_applicable")
        refs = array(assessment["finding_ids"], path + ".finding_ids")
        seen_ids = set()
        for finding_id in refs:
            if not isinstance(finding_id, str) or finding_id not in findings:
                fail(path + ".finding_ids", f"unknown finding ID {finding_id!r}")
            if finding_id in seen_ids:
                fail(path + ".finding_ids", f"duplicate finding ID {finding_id!r}")
            seen_ids.add(finding_id)
            finding = findings[finding_id]
            if finding["primary_dimension"] != dimension:
                fail(path + ".finding_ids", f"{finding_id} belongs to another primary dimension")
            if finding["status"] == "tentative":
                fail(path + ".finding_ids", f"tentative finding {finding_id} must not support a rating")
        if rating == 0 and refs:
            fail(path, "rating zero must have no supported findings")
        if assessed and rating > 0 and not refs:
            fail(path, "a positive rating requires supported findings")
        if assessed:
            expected = {fid for fid, finding in findings.items()
                        if finding["primary_dimension"] == dimension and finding["status"] == "supported"}
            if expected != seen_ids:
                fail(path + ".finding_ids", "must cite every supported finding in this assessed dimension")

    assessed_weight = sum(rubric["dimensions"][key]["weight"] for key, value in dimensions.items()
                          if value["status"] == "assessed")
    assessed_text = list(text)
    for exclusion in exclusions:
        assessed_text[exclusion["start"]:exclusion["end"]] = " " * (exclusion["end"] - exclusion["start"])
    word_count = len("".join(assessed_text).split())
    ineligibility_reasons = []
    if not context["word_count_reliable"]:
        ineligibility_reasons.append("Whitespace-delimited word count is not reliable for this passage.")
    if word_count < rubric["minimum_words"]:
        ineligibility_reasons.append(f"Only {word_count} assessed words; at least {rubric['minimum_words']} required.")
    if assessed_weight < rubric["minimum_coverage"]:
        ineligibility_reasons.append(f"Dimension-weight coverage is {assessed_weight}%; at least {rubric['minimum_coverage']}% required.")
    unchecked = [pattern for pattern, check in checks.items() if check["status"] == "not_checked"]
    if unchecked:
        ineligibility_reasons.append("Patterns not checked: " + ", ".join(sorted(unchecked)) + ".")
    unchecked_dimensions = [dimension for dimension, item in dimensions.items() if item["status"] == "not_checked"]
    if unchecked_dimensions:
        ineligibility_reasons.append("Dimensions not checked: " + ", ".join(unchecked_dimensions) + ".")
    publish_index = requested and not ineligibility_reasons
    dimension_results = []
    raw_index = Fraction(0)
    for dimension, definition in rubric["dimensions"].items():
        assessment = dimensions[dimension]
        rating = assessment["rating"]
        contribution = None
        if publish_index and rating is not None:
            contribution = Fraction(25 * definition["weight"] * rating, assessed_weight)
            raw_index += contribution
        supported = [item["id"] for item in finding_list if item["primary_dimension"] == dimension and item["status"] == "supported"]
        tentative = [item["id"] for item in finding_list if item["primary_dimension"] == dimension and item["status"] == "tentative"]
        dimension_results.append({
            "id": dimension, **definition, **assessment,
            "supported_finding_ids": supported, "tentative_finding_ids": tentative,
            "evidence_outcome": outcome(supported, tentative, reviewed=("reviewed" in [checks[pattern]["status"]
                                        for pattern, assigned in pattern_dimensions.items() if assigned == dimension])),
            "index_points": None if contribution is None else float(contribution),
        })
    value = None if not publish_index else (2 * raw_index.numerator + raw_index.denominator) // (2 * raw_index.denominator)
    matrix = []
    for pattern, dimension in pattern_dimensions.items():
        supported = [item for item in finding_list if pattern in item["patterns"] and item["status"] == "supported"]
        tentative = [item["id"] for item in finding_list if pattern in item["patterns"] and item["status"] == "tentative"]
        reviewed = checks[pattern]["status"] == "reviewed"
        matrix.append({
            "id": pattern, "dimension": dimension, **checks[pattern],
            "outcome": outcome(supported, tentative, reviewed),
            "maximum_supported_local_impact": max((item["impact"] for item in supported), default=0) if reviewed else None,
            "finding_ids": [item["id"] for item in supported], "tentative_finding_ids": tentative,
        })
    status_counts = {status: sum(check["status"] == status for check in checks.values()) for status in PATTERN_STATUSES}
    limitations = [
        "This rubric and its numerical conventions are unvalidated; software checks do not establish measurement validity.",
        "Checks validate supplied structure and exact quotations, not factual truth, editorial interpretation, assessor independence, or reader cost.",
        "Pattern review and verification scope are assessor declarations, not helper-verified review or truth.",
        "A zero rating or local impact means no supported finding in the reviewed scope, not verified correctness; tentative findings remain unresolved.",
        "Dimension-weight coverage includes restricted assessments and does not measure completeness of factual verification.",
        "Evidence-location counts are not independent incident counts or estimates of textual prevalence.",
        "Comparisons require matching rubric version, purpose and genre, assessed dimensions, actual pattern and verification scope, and exclusions.",
    ]
    limitations.extend(evaluation["limitations"])
    return {
        "rubric_version": rubric["version"], "validation_status": "unvalidated",
        "notice": "Evidence and dimension profiles are primary. An optional rubric index is not an authorship probability, "
                  "verified-fact percentage, publication-readiness decision, or ratio scale of experienced burden.",
        "context": context, "evaluation": evaluation,
        "index": {
            "requested": requested,
            "label": "Rubric index (unvalidated)",
            "status": "not_requested" if not requested else "withheld" if ineligibility_reasons else
                      "provisional" if word_count < rubric["provisional_below_words"] else "reported",
            "value": value, "unrounded_value": float(raw_index) if publish_index else None,
            "reasons": (["An index was not explicitly requested."] + ineligibility_reasons) if not requested else ineligibility_reasons,
        },
        "assessed_word_count": word_count, "word_count_reliable": context["word_count_reliable"],
        "dimension_weight_coverage": {"assessed_weight": assessed_weight, "total_weight": 100, "coverage_percent": assessed_weight},
        "dimensions": dimension_results, "findings": finding_list, "exclusions": exclusions,
        "critical_findings": [item["id"] for item in finding_list
                              if item["status"] == "supported" and item["impact"] == 4
                              and item["primary_dimension"] in ("grounding", "fidelity")],
        "pattern_coverage": {"total": len(pattern_dimensions), **status_counts,
                             "reviewed_percent_of_all_patterns": 100 * status_counts["reviewed"] / len(pattern_dimensions),
                             "supported_patterns": sum(bool(row["finding_ids"]) for row in matrix),
                             "tentative_patterns": sum(bool(row["tentative_finding_ids"]) for row in matrix)},
        "pattern_matrix": matrix,
        "location_convention": "Zero-based character start, exclusive end; one-based lines and occurrences. Location counts are not incident counts.",
        "limitations": limitations,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assessment", help="UTF-8 assessment JSON file")
    args = parser.parse_args(argv)
    try:
        result = assess(read_json(args.assessment))
    except (AssessmentError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
