# Assessment and scoring contract, version 2.0

This is an unvalidated editorial rubric. Evidence and dimension categories are primary; the numerical index is optional. Weights, category boundaries, minimum text lengths, and coverage cutoff remain design choices. The helper verifies submitted structure and quotations, not factual truth, actual review coverage, or editorial judgment.

## Assignment rules

| Category | Dimension anchor |
| --- | --- |
| 0 | Applicable scope reviewed; no supported defect after contextual exceptions. Consequential tentative concerns must remain visible; a zero does not resolve them. |
| 1 | Isolated or occasional minor issues with little reader cost. |
| 2 | Recurring issues or one substantial local defect reduces clarity, specificity, naturalness, or usefulness. |
| 3 | Widespread issues or multiple consequential defects materially impair the dimension. |
| 4 | A defect dominates the passage, or a demonstrated major breach changes its central meaning, evidence, or represented experience. |

Use [anchors.md](anchors.md) for dimension-specific examples and boundaries. These illustrate judgments; they are not calibrated ground-truth labels. Finding impact uses 1–4 for the local consequence; it need not equal the dimension category. Record **impact and extent separately**, then justify the holistic rating. For 3–4, provide separated evidence or explain the exceptional central consequence of one event. Do not multiply impact by confidence or recurrence.

One finding groups one distinct defect and consequence. Repeated locations show exposure; tags do not add penalties. Different findings sharing target text each require an `overlap_reason` explaining distinct consequences. Do not infer repetition from one excerpt. For a document-wide omission, cite the task requirement and relevant target evidence, describe whole-scope review, and never invent an absent quotation.

Confidence is qualitative evidence sufficiency (`high`, `medium`, `low`). Only high/medium findings support ratings; low remains tentative. It is not a probability. Contextual exceptions, useful terminology, necessary uncertainty, genuine alternatives, accessibility conventions, and purposeful rhetoric can prevent a finding.

## Scope and unavailable checks

| Pattern state | Meaning |
| --- | --- |
| `reviewed` | Applicable check performed; evidence determines supported, tentative, or no-supported-finding outcome. |
| `not_applicable` | Task genuinely does not involve this check; state why. |
| `not_assessable` | Relevant check requires unavailable evidence; identify what is missing. |
| `not_checked` | Not performed or outside the requested review; state why. Never imply a clean result. |

Assign a state to every P01–P57. The calculator derives outcomes but cannot prove a review occurred. A reviewed pattern without a supported finding has maximum supported local impact zero; tentative-only is not a clean result. Non-reviewed patterns have null impact.

When reasons overlap, use this order: first, mark a genuinely irrelevant comparison or phenomenon not applicable (for example, editing fidelity when no edit is involved). A user's choice to omit an otherwise applicable check does not make it irrelevant: mark it not checked, even if its required sources are also missing, and disclose both reasons. For an applicable check included in the review but blocked by missing evidence, use not assessable. Use reviewed only after performing the check. This scope rule can change index eligibility; it is an explicit operating convention, not an empirical finding.

Dimension status is `assessed`, `not_applicable`, `not_assessable`, or `not_checked`. Only assessed dimensions receive 0–4. Their scope is `full` or `restricted`; unassessed dimensions use `none`. Full scope permits inapplicable checks but cannot conceal unassessable/unchecked assigned checks. Restricted ratings describe only declared observable scope. Withhold a dimension if its requested conclusion depends on missing evidence. If every assigned check is non-reviewed, the dimension must be unassessed with a null rating. A not-applicable dimension requires every assigned check to be not applicable.

Fidelity needs an original or relevant voice reference. Without either, P48–P52 cannot be reviewed. A voice reference alone supports only P48/P49; P50–P52 require an original. Original composition may make fidelity not applicable; a requested rewrite audit lacking its original makes it not assessable. Do not invent a voice change.

P54–P57 need the specific contextual records described in the catalog. An unrelated material does not satisfy that need. Findings require meaningful non-target excerpts, not links alone. P56 requires the actual cited source; P57 requires the question and investigation record. Visible anonymous authority, scope overreach, and unsupported certainty can sometimes be assessed without fact-checking. Unverified ordinary claims are not thereby false. Do not silently browse for a style review. Requested verification preserves actual sources and declares its limits.

Read the whole requested scope and preserve exact text. Exclusions need explicit reasons; do not remove inconvenient prose to lower the result. Compare matching versions, purpose/genre, dimension sets, pattern/verification scope, and exclusions. A changed denominator alone is not improvement.

## Optional index

Set `index_requested: true` when the user asks for a score, index, or numerical comparison; omitted/false means no numerical index. Report detail is selected separately. Label an eligible index **Rubric index (unvalidated): N/100**. It summarizes weighted categories, not a measured fraction, authorship probability, factual reliability, or publication decision. Twice the index does not mean twice the slop.

For assessed dimensions A:

`index = round_half_up(100 * sum(weight[d] * rating[d] / 4 for d in A) / sum(weight[d] for d in A))`

Weights remain: substance 20, grounding 20, diction 15, rhetoric 10, rhythm 10, clarity 10, fidelity 10, presentation 5. Do not alter them within a run. Findings and pattern maxima are not summed. Missing dimensions are excluded, never zeroed; changing the assessed set changes the quantity summarized.

Withhold a requested index below 80 assessed whitespace-delimited words, below 70/100 assessed dimension weight, when word counts are unreliable, or when a pattern or dimension remains `not_checked`. From 80–199 words an otherwise eligible index is provisional. These are operational safeguards, not validated accuracy thresholds. Without an eligible requested index, totals **and** numeric contributions are null. Qualitative findings and profiles remain available.

Count each original whitespace-delimited word once if any of its characters remain in scope. A fully excluded word contributes zero. Exclusions preserve the original word boundaries: removing `[aside]` from `foo[aside]bar` leaves one word, while removing ` [aside] ` from `foo [aside] bar` leaves two. Exclusions cannot increase the word count.

Supported impact-4 grounding/fidelity findings appear in `critical_findings` regardless of index request, eligibility, or value. Put their consequences beside the principal result. Other consequential findings also deserve prominence. This list does not certify overall readiness or define all possible serious problems.

## Assessment JSON

Use UTF-8 and closed objects: unknown/duplicate keys are errors. `scripts/new_assessment.py` optionally creates an **unreviewed scaffold**, with all checks not checked and all ratings null. It does not evaluate the text. Complete and correct it using actual review; preserve the target exactly.

| Top-level key | Contract |
| --- | --- |
| `rubric_version` | `"2.0"`; version-1 records are rejected rather than silently migrated. |
| `text` | Exact nonempty target text. |
| `context` | Nonempty `genre`, `audience`, `language`, `purpose`, `scope`; boolean `word_count_reliable`. |
| `materials` | Source-name → full supporting text string. `text` is reserved; `original` and `voice_reference` have meanings above. |
| `exclusions` | Array of `{quote, reason, occurrence?}` against target text. |
| `pattern_checks` | Exactly P01–P57, each `{status, reason?}`; non-reviewed states require a nonempty reason. |
| `findings` | Evidence-led objects below. |
| `dimensions` | Exactly the eight rubric dimension IDs; objects below. |
| `evaluation` | Evaluator/verification declarations below. |
| `index_requested` | Optional boolean; default false. |

A finding example (replace excerpts and judgments with actual evidence):

```json
{
  "id": "F1",
  "patterns": ["P31"],
  "primary_dimension": "clarity",
  "impact": 2,
  "confidence": "high",
  "evidence": [{"source": "text", "quote": "Send it to her before approval."}],
  "explanation": "Two recipients and two documents remain possible; the instruction cannot be executed reliably.",
  "improvement": "Name the document, recipient, and approval stage.",
  "extent": {
    "scope": "local",
    "recurrence": "single",
    "coverage": "complete",
    "explanation": "One instruction is ambiguous; the remainder names its referents."
  }
}
```

Extent scope: `local`, `distributed`, or `document`; recurrence: `single`, `repeated`, or `not_established`; coverage of the supporting-location record: `complete` or `illustrative`; explanation nonempty. Repeated or distributed claims need at least two nonoverlapping target spans. Two snippets from one event do not establish recurrence. Complete location coverage does not assert that every possible defect was discovered.

Evidence items require `source`, exact nonempty `quote`, and optional 1-based `occurrence` (required when the quote repeats). Every finding needs target evidence. P48/P49 also need original/voice evidence, P50–P52 original evidence, P54–P57 meaningful contextual evidence. Excluded or duplicate spans are rejected. Optional `overlap_reason` becomes required on both findings sharing target text. Primary dimension must match at least one tag; all tagged checks must be reviewed.

An assessed dimension:

```json
{
  "status": "assessed",
  "scope": "full",
  "rating": 2,
  "reason": "One substantial local ambiguity prevents following the main instruction; the remainder is clear.",
  "finding_ids": ["F1"],
  "impact_summary": "The recipient and document cannot be identified.",
  "extent_summary": "One instruction; no repetition established."
}
```

Each dimension requires `status`, `scope`, `rating`, `reason`, `finding_ids`. Assessed dimensions also require nonempty `impact_summary` and `extent_summary`. Unassessed dimensions use null rating/none scope; their supported qualitative findings remain visible. Positive ratings need supported primary-dimension findings; assessed zero must have none. Every supported finding of an assessed dimension must be cited. Tentative findings never support ratings; cross-dimension tags cannot supply duplicate penalties.

Evaluation example:

```json
{
  "assessor_id": "assessor-A",
  "assessor_type": "model",
  "assessment_stage": "single_assessor",
  "verification": {
    "mode": "not_performed",
    "description": "Style and internal evidence only; ordinary factual claims were not independently checked."
  },
  "provenance": "Record the actual known evaluator/version/settings/date and unknowns here.",
  "limitations": ["No independent human assessment."],
  "counterevidence": ["The requested numbered steps provide useful navigation."]
}
```

Assessor type: `human`, `model`, `mixed`; stage: `single_assessor`, `independent`, `adjudicated`; verification mode: `not_performed`, `supplied_only`, `external_sources`. Strings must be nonempty. Limitations/counterevidence arrays may be empty but their members must be nonempty strings. Anonymous IDs suffice. These declarations do not prove independence/verification; sequential self-review is not independent human validation. Preserve raw independent records before adjudication for research.

## Output and interpretation

Run `python3 <skill-directory>/scripts/score.py <assessment.json>`. Success prints JSON; errors exit nonzero with diagnostics. No network is used. This is a structured assessment result for validation and reporting, not the default user-facing response. Derive either report format from the same completed assessment.

The assessment retains full target/supporting text. The result retains evidence and exclusion quotations: exclusions remove text from assessment scope and word counts, not from disclosure. Keep these records outside published files. A requested shareable report needs a separate minimized or redacted presentation; do not silently alter the exact evidence record. Describe omissions and prefer locations when an excerpt would expose unnecessary private information. A detailed report request does not request raw JSON.

- `index`: `requested`, `status`, `value`, `unrounded_value`, `reasons`, `label`. Status is `not_requested`, `withheld`, `provisional`, or `reported`. Values and per-dimension `index_points` appear only for an eligible requested index.
- `dimension_weight_coverage`: assessed weight out of 100. `pattern_coverage`: separate review-state counts. Neither is factual verification coverage; describe that in `evaluation.verification`.
- Pattern rows retain check `status`; add `outcome`, `maximum_supported_local_impact`, supported IDs, and tentative IDs. Outcomes distinguish supported, tentative, both, no supported finding, and not reviewed. Never sum maxima.
- Findings expose target evidence locations and a nonoverlapping count. These are locations, not inferred independent incidents or exhaustive prevalence. Legitimately different findings may share locations.
- Dimension evidence outcomes and supported/tentative ID lists keep unassessed qualitative findings and unresolved concerns visible.
- Critical IDs survive index omission/withholding. `validation_status` is unvalidated. Character starts are zero-based and ends exclusive; lines/occurrences are one-based.

Follow the concise or requested detailed report format in `SKILL.md`. Disclose restricted scope wherever a rating is shown, and always surface material limitations. A no-supported-finding result is limited to assessed scope, not proof of perfection. Output detail is independent of `index_requested`; concise scored and detailed unscored reports are both valid.

## Migration

Version 2.0 changes schema and default presentation, not calibrated distances or weights. To reassess version 1: preserve the original; supply actual purpose/provenance/verification; review pattern states; record extent and dimension scope/impact/extent summaries; explicitly choose the optional index. Do not infer those judgments mechanically or silently convert prior zeros to reviewed checks. Validate the new record and save it separately. Matching arithmetic alone does not establish comparable scope.

The public-release instructions make narrative reports concise by default. This presentation change does not alter the version-2 record schema, rubric, or calculator, and existing version-2 records need no migration for it.
