# Research comparisons and validation

Read this for benchmark design, rubric validation, or model-level claims. It is not a prerequisite human experiment for ordinary editorial feedback. Version 2.0 is an unvalidated assessment procedure with illustrative anchors; structural tests do not establish detection accuracy or reader relevance.

## Define the intended claim

Distinguish a finding about one supplied response, repeated behavior on one prompt, performance across a declared prompt population, and experienced reader/editing burden. A single response per model supports a case study. Repeated judges are not repeated model generations; 57 pattern checks are not 57 independent outputs. Record the generation interface/version/date, prompt, settings, tools, personalization and selection rule as known, reported, or unavailable. Do not infer hidden settings from filenames.

Freeze the construct, applicable scope, rubric/anchor version, grouping of recurring defects, evaluator instructions, and planned comparisons before examining final rankings. A weighted index expresses priorities; empirical fitting needs an independently measured target, not a preferred leaderboard. Preserve the baseline when changing a protocol.

## Development and reserved material

Use separate development and evaluation material. Include representative outputs to estimate real-use incidence, and diagnostic contrasts to test specific judgments. Do not pool an enriched diagnostic set into a population-prevalence estimate. Mark synthetic cases and author-proposed expectations as hypotheses, not human ground truth.

Useful contrasts include a repaired ambiguity, a supported factual error in otherwise fluent prose, recurring versus isolated phrasing, useful headings/technical terms, clean material around an unchanged critical error, source availability, and embedded instructions to the judge. Verify that edits isolate the intended property. Preserve raw inputs separately from answer keys. After a reserved example informs a repair, mark it exposed and retain it as regression material; do not claim it is still unseen.

## Independent judgments and reference evidence

Match the assessor population to the claim: editors for necessary revisions, domain experts for factual evidence, intended readers for comprehension/usefulness. Neither reader preference nor expert agreement alone establishes every dimension. Use more than one relevant outcome where the intended interpretation is broad; editing time alone may reflect taste and reading speed may reflect skimming.

Hide model identities and prior scores. Randomize order; for pairwise comparisons balance positions and allow ties/insufficient evidence. When comparing scoring methods, control learning/carryover using counterbalanced assignments or comparable independent rater groups. A second reading's familiarity must not be mistaken for a better method. Compare cost/time as well as consistency.

Obtain independent records before adjudication, preserve them, and record resolutions or remaining disagreement. Distinguish detection, span boundaries, category, impact, dimension severity, and genuine audience differences. Do not delete dissent simply to improve agreement. Model-agent passes can expose implementation errors but are not independent human calibration.

Audit apparently clean as well as flagged outputs. Oversampling disputed or critical cases can be useful, but report strata or sampling weights when estimating ordinary prevalence. Where defensible references exist, examine false positives and false negatives by dimension/consequence. Preserve uncertainty and disagreements where a single correct label is not established.

## Reliability, validity, and inference

For ordinal categories, show actual disagreement/category distributions and use a suitable ordinal agreement coefficient with its distance convention and uncertainty. For a numerical index, specify any intraclass correlation's model, absolute-agreement versus consistency target, and single-rater versus averaged unit. High agreement can reproduce bias; rank agreement can conceal differing absolute scores. No universal coefficient cutoff validates this rubric.

Do not demand high internal consistency across distinct editorial costs or discard rare critical checks to raise Cronbach alpha. These components may define an index rather than reflect one homogeneous hidden trait. Krippendorff alpha for assessor agreement answers a different question.

Define practically meaningful differences through reader/editor consequences; use pilot variation to plan precision and sample size. Retain prompt pairing and distinguish prompt, generation, rater, and interaction effects. An ordinal mixed model or clustered resampling may suit a sufficiently replicated design, subject to assumptions. One-off responses cannot support elaborate variance models. Predeclare principal comparisons or address multiplicity. Failure to detect a difference is not evidence of equivalence.

LLM judges need task-specific validation for position, verbosity, origin-related preference, prompt wording, missed defects, and embedded instructions. Vendor diversity does not establish independent errors; measure joint failures. Repeated calls measure stochastic variability but do not remove shared bias. Do not assume pointwise, pairwise, or best–worst judging universally wins. Retest a changed evaluator or rubric on held-out material.

## Reporting and comprehension

In research reports, keep dimension ratings, critical findings, verification scope, and material disagreements visible. Ordinary editorial responses follow the concise default in `SKILL.md`; full profiles are supplied when requested. If using an index for research comparisons, disclose weights/tradeoffs and sensitivity to plausible alternatives. A weight-sensitivity range is not a sampling confidence interval. Rater variability is not model-population uncertainty; missing source material is neither. Never fabricate precision or convert the index into an authorship estimate.

For changes to reporting instructions, compare concise and detailed reports derived from the same completed assessment. Check ordinary, score-only, detailed-only, and detailed-with-score requests; several serious findings; missing or incomplete evidence; and a bounded no-supported-issue result with a consequential tentative concern. All serious consequences and material limits must survive summarization. Failed validation must not produce a purportedly validated index. Use a synthetic sensitive exclusion to check that raw records are not mistaken for redacted shareable reports. These are behavioral checks of presentation, not scientific validation of the rubric.

Ask intended report readers what zero means, whether an index is a probability, whether a low total rules out a critical failure, and what population the results cover. Revise misleading presentation based on those responses. Disclaimers alone do not prove comprehension. No presentation can guarantee that every reader interprets it correctly.

Preserve inputs, generation metadata, independent assessments, evidence, adjudication, rubric and evaluator versions, exclusions, scripts, and decisions. Report sample design, rater selection/training, information shown, task order, quality controls, and analytic choices using a human-evaluation data sheet. Distinguish development/diagnostic/confirmatory results and empirical evidence from design conventions. See [sources.md](sources.md) for primary methodological support and transfer limits.
