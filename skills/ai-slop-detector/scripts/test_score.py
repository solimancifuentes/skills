"""Software invariants for version 2; these tests do not validate editorial ratings."""

import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest

import score


RUBRIC = score.read_json(score.DEFAULT_RUBRIC)
PATTERNS = {"substance": "P03", "grounding": "P05", "diction": "P21", "rhetoric": "P06",
            "rhythm": "P18", "clarity": "P29", "fidelity": "P51", "presentation": "P37"}
CONDITIONAL = ("P48", "P49", "P50", "P51", "P52", "P54", "P55", "P56", "P57")


def assessment(words=220, index_requested=True):
    """Explicitly reviewed synthetic fixture, not a detector or human annotation."""
    return {
        "rubric_version": "2.0", "index_requested": index_requested,
        "text": " ".join(f"w{index:03d}" for index in range(words)),
        "context": {"genre": "synthetic test fixture", "audience": "test", "language": "English",
                    "purpose": "Exercise calculator invariants only", "scope": "complete fixture",
                    "word_count_reliable": True},
        "materials": {}, "exclusions": [],
        "pattern_checks": {pattern: {"status": "not_assessable", "reason": "No comparison record supplied"}
                           if pattern in CONDITIONAL else {"status": "reviewed"} for pattern in RUBRIC["patterns"]},
        "findings": [],
        "dimensions": {dimension: {
            "status": "not_assessable" if dimension == "fidelity" else "assessed",
            "scope": "none" if dimension == "fidelity" else "restricted" if dimension == "grounding" else "full",
            "rating": None if dimension == "fidelity" else 0,
            "reason": "Fixture rationale", "finding_ids": [],
            **({} if dimension == "fidelity" else {"impact_summary": "No supported fixture defect.",
                                                   "extent_summary": "No extent to establish."}),
        } for dimension in RUBRIC["dimensions"]},
        "evaluation": {"assessor_id": "synthetic-fixture", "assessor_type": "model", "assessment_stage": "single_assessor",
                       "verification": {"mode": "not_performed", "description": "Synthetic tokens; not fact checked."},
                       "provenance": "Unit-test author; no independent rating or empirical validation.",
                       "limitations": ["Artificial fixtures test software only."], "counterevidence": []},
    }


def finding(data, dimension="substance", rating=2, quote="w000", confidence="high", pattern=None):
    finding_id = f"F{len(data['findings']) + 1}"
    item = {"id": finding_id, "patterns": [pattern or PATTERNS[dimension]], "primary_dimension": dimension,
            "impact": rating, "confidence": confidence, "evidence": [{"source": "text", "quote": quote}],
            "explanation": "A specific fixture defect with a reader-facing consequence.",
            "improvement": "Repair the particular defect identified by this fixture.",
            "extent": {"scope": "local", "recurrence": "single", "coverage": "illustrative",
                       "explanation": "One supporting location; no extrapolation beyond it."}}
    data["findings"].append(item)
    if confidence != "low":
        data["dimensions"][dimension].update({"status": "assessed", "rating": rating,
                                             "scope": "restricted" if dimension in ("grounding", "fidelity") else "full",
                                             "impact_summary": "Supported fixture consequence.",
                                             "extent_summary": "One local supporting passage."})
        data["dimensions"][dimension]["finding_ids"].append(finding_id)
    return item


def original(data):
    data["materials"]["original"] = "The original retains a key qualifier."
    for pattern in ("P48", "P49", "P50", "P51", "P52"):
        data["pattern_checks"][pattern] = {"status": "reviewed"}


def unassess(data, dimension, status="not_assessable"):
    data["dimensions"][dimension] = {"status": status, "scope": "none", "rating": None,
                                    "reason": "Insufficient scope for a holistic rating.", "finding_ids": []}


def pattern_row(result, pattern):
    return next(row for row in result["pattern_matrix"] if row["id"] == pattern)


def dimension_row(result, dimension):
    return next(row for row in result["dimensions"] if row["id"] == dimension)


class CalculatorTests(unittest.TestCase):
    def invalid(self, data, fragment):
        with self.assertRaisesRegex(score.AssessmentError, fragment):
            score.assess(data)

    def no_index_numbers(self, result):
        self.assertIsNone(result["index"]["value"])
        self.assertIsNone(result["index"]["unrounded_value"])
        self.assertTrue(all(row["index_points"] is None for row in result["dimensions"]))
        self.assertNotIn("score_percent", result)
        self.assertNotIn("unrounded_score", result)

    def test_weighted_arithmetic_and_contributions(self):
        data = assessment()
        finding(data, "substance", 3, "w000")
        finding(data, "grounding", 2, "w010")
        finding(data, "diction", 1, "w020")
        result = score.assess(data)
        self.assertEqual(result["dimension_weight_coverage"]["assessed_weight"], 90)
        self.assertEqual(result["index"]["value"], 32)
        self.assertAlmostEqual(result["index"]["unrounded_value"], 25 * 115 / 90)
        self.assertAlmostEqual(sum(row["index_points"] or 0 for row in result["dimensions"]),
                               result["index"]["unrounded_value"])
        self.assertEqual(len(result["dimensions"]), 8)
        self.assertEqual(len(result["pattern_matrix"]), 57)

    def test_profiles_default_and_explicit_false_never_emit_index_numbers(self):
        for request in ("absent", False):
            data = assessment()
            finding(data, "grounding", 4)
            if request == "absent":
                del data["index_requested"]
            else:
                data["index_requested"] = request
            result = score.assess(data)
            self.no_index_numbers(result)
            self.assertEqual(result["index"]["status"], "not_requested")
            self.assertFalse(result["index"]["requested"])
            self.assertEqual(result["critical_findings"], ["F1"])
            self.assertEqual(dimension_row(result, "grounding")["rating"], 4)

    def test_half_up_rounding(self):
        data = assessment()
        for index, dimension in enumerate(("substance", "diction", "rhetoric")):
            finding(data, dimension, 1, f"w{index:03d}")
        result = score.assess(data)
        self.assertEqual(result["index"]["unrounded_value"], 12.5)
        self.assertEqual(result["index"]["value"], 13)

    def test_extremes_and_multitag_findings_do_not_add_penalties(self):
        data = assessment()
        self.assertEqual(score.assess(data)["index"]["value"], 0)
        for index, dimension in enumerate(key for key in RUBRIC["dimensions"] if key != "fidelity"):
            finding(data, dimension, 4, f"w{index:03d}")
        data["findings"][0]["patterns"].append("P21")
        self.assertEqual(score.assess(data)["index"]["value"], 100)

    def test_existing_tradeoff_arithmetic_is_preserved(self):
        data = assessment()
        finding(data, "grounding", 4)
        self.assertEqual(score.assess(data)["index"]["value"], 22)
        data = assessment()
        for index, dimension in enumerate(key for key in RUBRIC["dimensions"] if key != "fidelity"):
            finding(data, dimension, 1, f"w{index:03d}")
        self.assertEqual(score.assess(data)["index"]["value"], 25)

    def test_sample_thresholds_and_unreliable_count(self):
        for words, status in ((79, "withheld"), (80, "provisional"), (199, "provisional"), (200, "reported")):
            with self.subTest(words=words):
                data = assessment(words)
                finding(data)
                result = score.assess(data)
                self.assertEqual(result["index"]["status"], status)
                self.assertEqual(result["assessed_word_count"], words)
                if words < 80:
                    self.no_index_numbers(result)
        data = assessment()
        finding(data)
        data["context"]["word_count_reliable"] = False
        result = score.assess(data)
        self.no_index_numbers(result)
        self.assertIn("not reliable", result["index"]["reasons"][0])

    def test_coverage_cutoff_and_zero_coverage(self):
        data = assessment()
        unassess(data, "substance")
        self.assertEqual(score.assess(data)["dimension_weight_coverage"]["coverage_percent"], 70)
        self.assertEqual(score.assess(data)["index"]["value"], 0)
        unassess(data, "presentation")
        self.no_index_numbers(score.assess(data))
        for dimension in data["dimensions"]:
            unassess(data, dimension)
        result = score.assess(data)
        self.assertEqual(result["dimension_weight_coverage"]["assessed_weight"], 0)
        self.no_index_numbers(result)

    def test_unchecked_pattern_and_dimension_withhold_index(self):
        data = assessment()
        finding(data)
        data["pattern_checks"]["P54"] = {"status": "not_checked", "reason": "Review incomplete."}
        result = score.assess(data)
        self.no_index_numbers(result)
        self.assertIn("Patterns not checked: P54", " ".join(result["index"]["reasons"]))
        data = assessment()
        unassess(data, "presentation", status="not_checked")
        result = score.assess(data)
        self.no_index_numbers(result)
        self.assertIn("Dimensions not checked", " ".join(result["index"]["reasons"]))

    def test_unreviewed_scaffold_is_valid_but_no_false_clean_states(self):
        data = assessment(index_requested=False)
        for pattern in data["pattern_checks"]:
            data["pattern_checks"][pattern] = {"status": "not_checked", "reason": "Awaiting review."}
        for dimension in data["dimensions"]:
            unassess(data, dimension, "not_checked")
        result = score.assess(data)
        self.no_index_numbers(result)
        self.assertEqual(result["pattern_coverage"]["not_checked"], 57)
        self.assertTrue(all(row["maximum_supported_local_impact"] is None and row["outcome"] == "not_reviewed"
                            for row in result["pattern_matrix"]))

    def test_exclusions_reduce_count_and_cannot_overlap(self):
        data = assessment(80)
        data["exclusions"] = [{"quote": "w000", "reason": "Quoted external example"}]
        result = score.assess(data)
        self.assertEqual(result["assessed_word_count"], 79)
        self.no_index_numbers(result)
        data["exclusions"].append({"quote": "w000 w001", "reason": "Second excluded example"})
        self.invalid(data, "overlaps another exclusion")

    def test_partial_word_exclusions_preserve_sample_thresholds(self):
        for words, status in ((79, "withheld"), (80, "provisional"), (199, "provisional"), (200, "reported")):
            with self.subTest(words=words):
                data = assessment(words - 1)
                data["text"] += " foo[aside]bar"
                finding(data)
                data["exclusions"] = [{"quote": "[aside]", "reason": "Inline annotation"}]
                result = score.assess(data)
                self.assertEqual(result["assessed_word_count"], words)
                self.assertEqual(result["index"]["status"], status)
                if words < 80:
                    self.no_index_numbers(result)

    def test_exclusions_preserve_original_word_boundaries(self):
        cases = (
            ("foo[aside]bar", "[aside]", 1),
            ("foo [aside] bar", " [aside] ", 2),
            ("foo\t[aside]\nbar", "\t[aside]\n", 2),
            ("foo\u00a0[aside]\u2003bar", "\u00a0[aside]\u2003", 2),
            ("abc def", "bc d", 2),
            ("prefixword", "prefix", 1),
            ("wordsuffix", "suffix", 1),
            ("[aside]", "[aside]", 0),
        )
        for text, quote, expected in cases:
            with self.subTest(text=text, quote=quote):
                data = assessment()
                data["text"] = text
                data["exclusions"] = [{"quote": quote, "reason": "Excluded fixture content"}]
                result = score.assess(data)
                self.assertEqual(result["assessed_word_count"], expected)
                self.no_index_numbers(result)

    def test_touching_exclusions_are_order_independent(self):
        cases = (
            ("foo[one][two]bar tail", ("[one]", "[two]"), 2),
            ("foobar tail", ("foo", "bar"), 1),
        )
        for text, quotes, expected in cases:
            for order in (quotes, quotes[::-1]):
                with self.subTest(text=text, order=order):
                    data = assessment()
                    data["text"] = text
                    data["exclusions"] = [{"quote": quote, "reason": "Excluded fixture content"}
                                          for quote in order]
                    result = score.assess(data)
                    self.assertEqual(result["assessed_word_count"], expected)

    def test_evidence_may_not_overlap_excluded_text(self):
        data = assessment()
        finding(data, quote="w000 w001")
        data["exclusions"] = [{"quote": "w001", "reason": "Excluded example"}]
        self.invalid(data, "overlaps excluded")

    def test_nonexistent_and_ambiguous_quotes(self):
        data = assessment()
        item = finding(data, quote="invented quotation")
        self.invalid(data, "does not occur exactly")
        data["text"] += " w000"
        item["evidence"][0]["quote"] = "w000"
        self.invalid(data, "required because the quote occurs 2 times")
        item["evidence"][0]["occurrence"] = 2
        result = score.assess(data)
        self.assertEqual(result["findings"][0]["evidence"][0]["start"], data["text"].rfind("w000"))
        item["evidence"][0]["occurrence"] = 3
        self.invalid(data, "only 2 occurrence")

    def test_unicode_offsets_and_lines_are_exact(self):
        data = assessment()
        data["text"] = "éclair\nA target.\n" + data["text"]
        finding(data, quote="A target.")
        loc = score.assess(data)["findings"][0]["target_evidence_locations"][0]
        self.assertEqual((loc["start"], loc["end"], loc["line_start"], loc["line_end"]), (7, 16, 2, 2))

    def test_duplicate_findings_and_primary_dimension_ids(self):
        data = assessment()
        item = finding(data)
        data["findings"].append(copy.deepcopy(item))
        self.invalid(data, "duplicate finding ID")
        data["findings"].pop()
        item["patterns"] = ["P58"]
        self.invalid(data, "unknown pattern")
        item["patterns"] = ["P21"]
        self.invalid(data, "must match at least one")
        item["primary_dimension"] = "unknown"
        self.invalid(data, "unknown dimension")

    def test_unknown_and_missing_keys_are_errors(self):
        data = assessment()
        data["dimensions"].pop("rhythm")
        self.invalid(data, "missing keys: rhythm")
        data = assessment()
        data["probability"] = 99
        self.invalid(data, "unknown keys: probability")
        data = assessment()
        del data["pattern_checks"]["P57"]
        self.invalid(data, "missing keys: P57")
        data = assessment()
        data["pattern_checks"]["P58"] = {"status": "reviewed"}
        self.invalid(data, "unknown keys: P58")

    def test_version_one_gets_explicit_migration_error(self):
        data = {"rubric_version": "1.0", "unassessable_patterns": {}}
        self.invalid(data, "explicit version-2 reassessment")

    def test_required_purpose_and_metadata_validation(self):
        data = assessment()
        del data["context"]["purpose"]
        self.invalid(data, "missing keys: purpose")
        for purpose in ("", " \n", None, False, 3, []):
            data = assessment()
            data["context"]["purpose"] = purpose
            self.invalid(data, "context.purpose: must be a nonempty string")
        for key in ("assessor_id", "provenance"):
            data = assessment()
            data["evaluation"][key] = ""
            self.invalid(data, "must be a nonempty string")
        for key, bad in (("assessor_type", "automatic"), ("assessment_stage", "consensus"),
                         ("limitations", [""]), ("counterevidence", "none")):
            data = assessment()
            data["evaluation"][key] = bad
            self.invalid(data, "evaluation")
        data = assessment()
        data["evaluation"]["verification"]["mode"] = "verified"
        self.invalid(data, "evaluation.verification.mode")

    def test_evaluation_is_preserved_without_independence_claim(self):
        for stage in ("single_assessor", "independent", "adjudicated"):
            data = assessment()
            data["evaluation"]["assessment_stage"] = stage
            data["evaluation"]["counterevidence"] = ["A deliberate stylistic exception."]
            result = score.assess(data)
            self.assertEqual(result["evaluation"], data["evaluation"])
            self.assertEqual(result["validation_status"], "unvalidated")
            self.assertIn("assessor independence", " ".join(result["limitations"]))

    def test_pattern_coverage_and_verification_are_separate(self):
        result = score.assess(assessment())
        self.assertEqual(result["dimension_weight_coverage"]["coverage_percent"], 90)
        self.assertEqual(result["pattern_coverage"]["reviewed"], 48)
        self.assertEqual(result["pattern_coverage"]["not_assessable"], 9)
        self.assertAlmostEqual(result["pattern_coverage"]["reviewed_percent_of_all_patterns"], 4800 / 57)
        self.assertEqual(result["evaluation"]["verification"]["mode"], "not_performed")
        self.assertEqual(sum(result["pattern_coverage"][status] for status in score.PATTERN_STATUSES), 57)

    def test_pattern_states_require_reasons_and_cannot_support_findings(self):
        for state in ("not_applicable", "not_assessable", "not_checked"):
            data = assessment()
            data["pattern_checks"]["P03"] = {"status": state}
            self.invalid(data, "pattern_checks.P03.reason")
            data["pattern_checks"]["P03"]["reason"] = "Scope limitation."
            finding(data)
            self.invalid(data, "must have status reviewed")
        data = assessment()
        data["pattern_checks"]["P03"]["status"] = "clean"
        self.invalid(data, "must be one of")

    def test_dimension_references_and_supported_findings(self):
        data = assessment()
        data["dimensions"]["substance"]["rating"] = 1
        self.invalid(data, "positive rating requires supported findings")
        finding(data)
        data["dimensions"]["substance"]["finding_ids"] = ["F99"]
        self.invalid(data, "unknown finding ID")
        data["dimensions"]["substance"]["finding_ids"] = []
        data["dimensions"]["substance"]["rating"] = 0
        self.invalid(data, "must cite every supported finding")
        data["dimensions"]["substance"]["finding_ids"] = ["F1"]
        self.invalid(data, "rating zero must have no supported findings")

    def test_dimension_status_scope_and_summaries_are_consistent(self):
        for key in ("impact_summary", "extent_summary"):
            data = assessment()
            del data["dimensions"]["substance"][key]
            self.invalid(data, key)
        data = assessment()
        data["dimensions"]["grounding"]["scope"] = "full"
        self.invalid(data, "full scope cannot include")
        data = assessment()
        data["dimensions"]["fidelity"]["rating"] = 0
        self.invalid(data, "unassessed dimensions require null rating")
        data = assessment()
        data["dimensions"]["substance"]["scope"] = "none"
        self.invalid(data, "assessed dimensions require full or restricted")
        data = assessment()
        unassess(data, "fidelity", "not_applicable")
        self.invalid(data, "all assigned patterns to be not_applicable")

    def test_genuinely_inapplicable_checks_can_coexist_with_full_scope(self):
        data = assessment()
        for pattern in ("P48", "P49", "P50", "P51", "P52"):
            data["pattern_checks"][pattern] = {"status": "not_applicable", "reason": "No rewriting task."}
        unassess(data, "fidelity", "not_applicable")
        for pattern in ("P54", "P55", "P56", "P57"):
            data["pattern_checks"][pattern] = {"status": "not_applicable", "reason": "No relevant factual claim in fixture."}
        data["dimensions"]["grounding"]["scope"] = "full"
        result = score.assess(data)
        self.assertEqual(result["index"]["value"], 0)
        self.assertEqual(result["pattern_coverage"]["not_applicable"], 9)
        self.assertIsNone(pattern_row(result, "P54")["maximum_supported_local_impact"])

    def test_all_nonreviewed_dimension_cannot_be_zero(self):
        data = assessment()
        for pattern, dimension in RUBRIC["patterns"].items():
            if dimension == "rhythm":
                data["pattern_checks"][pattern] = {"status": "not_assessable", "reason": "Insufficient sample."}
        data["dimensions"]["rhythm"]["scope"] = "restricted"
        self.invalid(data, "every assigned pattern is non-reviewed")

    def test_cross_dimension_evidence_is_not_counted_twice(self):
        data = assessment()
        finding(data)
        data["dimensions"]["diction"]["rating"] = 2
        data["dimensions"]["diction"]["finding_ids"] = ["F1"]
        self.invalid(data, "belongs to another primary dimension")

    def test_overlap_requires_distinct_defect_explanations(self):
        data = assessment()
        first = finding(data, quote="w000 w001")
        second = finding(data, "diction", quote="w001")
        self.invalid(data, "each needs overlap_reason")
        first["overlap_reason"] = "This finding concerns the claim's specificity."
        second["overlap_reason"] = "This finding concerns a separate imprecision within that claim."
        self.assertEqual(len(score.assess(data)["findings"]), 2)

    def test_tentative_findings_never_score_and_are_not_presented_as_clean(self):
        data = assessment()
        finding(data, rating=4, confidence="low")
        result = score.assess(data)
        self.assertEqual(result["index"]["value"], 0)
        row = pattern_row(result, "P03")
        self.assertEqual(row["maximum_supported_local_impact"], 0)
        self.assertEqual(row["outcome"], "tentative")
        self.assertEqual(row["finding_ids"], [])
        self.assertEqual(row["tentative_finding_ids"], ["F1"])
        self.assertEqual(dimension_row(result, "substance")["evidence_outcome"], "tentative")
        data["dimensions"]["substance"]["finding_ids"] = ["F1"]
        self.invalid(data, "tentative finding F1 must not support")

    def test_supported_and_tentative_states_remain_distinct(self):
        data = assessment()
        finding(data, quote="w000", rating=2)
        finding(data, quote="w010", confidence="low", rating=4)
        result = score.assess(data)
        row = pattern_row(result, "P03")
        self.assertEqual(row["outcome"], "supported_and_tentative")
        self.assertEqual(row["maximum_supported_local_impact"], 2)
        self.assertEqual(row["finding_ids"], ["F1"])
        self.assertEqual(row["tentative_finding_ids"], ["F2"])

    def test_critical_findings_survive_low_index_and_exclude_tentative(self):
        for dimension in ("grounding", "fidelity"):
            data = assessment()
            if dimension == "fidelity":
                original(data)
            supported = finding(data, dimension, rating=4, quote="w000")
            tentative = finding(data, dimension, rating=4, quote="w001", confidence="low")
            if dimension == "fidelity":
                for item in (supported, tentative):
                    item["evidence"].append({"source": "original", "quote": "retains a key qualifier"})
            data["dimensions"][dimension]["rating"] = 1
            result = score.assess(data)
            self.assertLess(result["index"]["value"], 10)
            self.assertEqual(result["critical_findings"], ["F1"])

    def test_critical_findings_survive_withheld_aggregate(self):
        for words in (79, 220):
            data = assessment(words)
            finding(data, "grounding", rating=4, quote="w000")
            finding(data, "grounding", rating=4, quote="w001", confidence="low")
            finding(data, "substance", rating=4, quote="w002")
            if words == 220:
                for dimension in data["dimensions"]:
                    unassess(data, dimension)
            result = score.assess(data)
            self.no_index_numbers(result)
            self.assertEqual(result["critical_findings"], ["F1"])

    def test_unassessed_dimension_keeps_qualitative_findings(self):
        data = assessment()
        finding(data, rating=3)
        unassess(data, "substance")
        result = score.assess(data)
        self.assertEqual(result["index"]["value"], 0)
        self.assertEqual(pattern_row(result, "P03")["maximum_supported_local_impact"], 3)
        self.assertEqual(dimension_row(result, "substance")["supported_finding_ids"], ["F1"])
        self.assertIsNone(dimension_row(result, "substance")["rating"])

    def test_repeated_and_distributed_claims_require_separated_evidence(self):
        for key, value in (("recurrence", "repeated"), ("scope", "distributed")):
            data = assessment()
            item = finding(data, quote="w000 w001")
            item["extent"][key] = value
            self.invalid(data, "two nonoverlapping target evidence spans")
            item["evidence"].append({"source": "text", "quote": "w001"})
            self.invalid(data, "two nonoverlapping target evidence spans")
            item["evidence"].append({"source": "text", "quote": "w010"})
            result = score.assess(data)
            self.assertEqual(result["findings"][0]["nonoverlapping_target_evidence_location_count"], 2)
            self.assertEqual(len(result["findings"][0]["target_evidence_locations"]), 3)

    def test_source_excerpt_cannot_supply_second_target_recurrence(self):
        data = assessment()
        original(data)
        item = finding(data)
        item["extent"]["recurrence"] = "repeated"
        item["evidence"].append({"source": "original", "quote": "key qualifier"})
        self.invalid(data, "two nonoverlapping target evidence spans")

    def test_recurrence_extent_and_pattern_count_do_not_multiply_score(self):
        data = assessment()
        item = finding(data)
        baseline = score.assess(data)["index"]["value"]
        item["extent"].update({"scope": "distributed", "recurrence": "repeated", "coverage": "complete"})
        item["evidence"].append({"source": "text", "quote": "w050"})
        item["patterns"].extend(["P01", "P02"])
        result = score.assess(data)
        self.assertEqual(result["index"]["value"], baseline)
        self.assertEqual(result["findings"][0]["extent"], item["extent"])

    def test_document_omission_can_use_relevant_passage_without_invented_absence_quote(self):
        data = assessment()
        original(data)
        item = finding(data, "fidelity", pattern="P51")
        item["extent"].update({"scope": "document", "recurrence": "not_established",
                              "explanation": "Source-required qualifier is absent from the whole target; contextual judgment is declared."})
        item["evidence"].append({"source": "original", "quote": "key qualifier"})
        result = score.assess(data)
        self.assertEqual(result["findings"][0]["nonoverlapping_target_evidence_location_count"], 1)

    def test_extent_schema_is_required_and_validated(self):
        data = assessment()
        item = finding(data)
        del item["extent"]
        self.invalid(data, "missing keys: extent")
        for key, value in (("scope", "global"), ("recurrence", True), ("coverage", "all"), ("explanation", "")):
            data = assessment()
            finding(data)["extent"][key] = value
            self.invalid(data, "extent")

    def test_duplicate_evidence_cannot_inflate_locations(self):
        data = assessment()
        item = finding(data)
        item["evidence"].append(copy.deepcopy(item["evidence"][0]))
        self.invalid(data, "duplicates another evidence span")

    def test_missing_conditional_material_cannot_be_reviewed(self):
        for pattern in CONDITIONAL:
            data = assessment()
            data["pattern_checks"][pattern] = {"status": "reviewed"}
            self.invalid(data, "cannot be reviewed without its required")

    def test_original_evidence_is_required_and_exact(self):
        data = assessment()
        original(data)
        item = finding(data, "fidelity", pattern="P51")
        self.invalid(data, "P51 requires original evidence")
        item["evidence"].append({"source": "original", "quote": "An invented source quotation."})
        self.invalid(data, "does not occur exactly")
        item["evidence"][-1]["quote"] = "retains a key qualifier"
        self.assertEqual(score.assess(data)["dimension_weight_coverage"]["coverage_percent"], 100)

    def test_voice_reference_only_supports_voice_patterns(self):
        data = assessment()
        data["materials"]["voice_reference"] = "A known example of the author's voice."
        for pattern in ("P48", "P49"):
            data["pattern_checks"][pattern] = {"status": "reviewed"}
        item = finding(data, "fidelity", pattern="P48")
        self.invalid(data, "P48 requires original or voice_reference evidence")
        item["evidence"].append({"source": "voice_reference", "quote": "known example"})
        self.assertEqual(score.assess(data)["dimension_weight_coverage"]["coverage_percent"], 100)
        data["pattern_checks"]["P50"] = {"status": "reviewed"}
        self.invalid(data, "cannot be reviewed without its required")

    def test_contextual_grounding_requires_non_target_excerpt(self):
        data = assessment()
        data["materials"]["source_article"] = "The record describes correlation only."
        data["pattern_checks"]["P56"] = {"status": "reviewed"}
        item = finding(data, "grounding", pattern="P56")
        self.invalid(data, "requires an excerpt from a contextual material")
        item["evidence"].append({"source": "source_article", "quote": "describes correlation only"})
        self.assertEqual(score.assess(data)["findings"][0]["status"], "supported")
        item["evidence"].pop(0)
        self.invalid(data, "requires at least one excerpt from text")

    def test_contextual_grounding_cannot_use_only_a_link(self):
        for url in ("https://example.com/article", "<https://example.com/article>", "[Source](https://example.com/article)"):
            data = assessment()
            data["materials"]["source_article"] = url
            data["pattern_checks"]["P56"] = {"status": "reviewed"}
            item = finding(data, "grounding", pattern="P56")
            item["evidence"].append({"source": "source_article", "quote": url})
            self.invalid(data, "not merely a link")

    def test_empty_text_and_boolean_numeric_fields_are_rejected(self):
        for text in ("", " \n\t"):
            data = assessment()
            data["text"] = text
            self.invalid(data, "text: must be a nonempty string")
        for key in ("rating", "impact", "occurrence"):
            data = assessment()
            item = finding(data)
            if key == "rating":
                data["dimensions"]["substance"][key] = True
            elif key == "impact":
                item[key] = True
            else:
                item["evidence"][0][key] = True
            self.invalid(data, "booleans are not integers")
        for key in ("word_count_reliable", "index_requested"):
            data = assessment()
            if key == "index_requested":
                data[key] = 1
            else:
                data["context"][key] = 1
            self.invalid(data, "must be a boolean")

    def test_cli_json_stdout_and_clean_error_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "assessment.json"
            path.write_text(json.dumps(assessment()), encoding="utf-8")
            stdout, stderr = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                self.assertEqual(score.main([str(path)]), 0)
            self.assertEqual(json.loads(stdout.getvalue())["index"]["value"], 0)
            self.assertEqual(stderr.getvalue(), "")
            for invalid_json in ('{"text":"one", "text":"two"}', '{"value": NaN}', "not JSON"):
                path.write_text(invalid_json, encoding="utf-8")
                stdout, stderr = io.StringIO(), io.StringIO()
                with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                    self.assertEqual(score.main([str(path)]), 1)
                self.assertEqual(stdout.getvalue(), "")
                self.assertTrue(stderr.getvalue().startswith("error: "))


if __name__ == "__main__":
    unittest.main()
