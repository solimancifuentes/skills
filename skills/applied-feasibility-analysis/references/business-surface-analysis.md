# Business Surface Analysis

Use this mode to analyze one compound company/product subject across selected business surfaces and produce a target-project adoption portfolio.

## Intake and frozen brief

Reuse the user's supplied or confirmed outcome and scope. Inspect available context, then record one brief with the smallest useful scope before research. Ask only for consequential unresolved inputs; do not reconfirm a usable brief. Include:

- verified company and product identity;
- target project and cited project fact sheet;
- decision objective;
- selected surfaces, cross-cutting tags, and lenses;
- depth: **Focused**, **Expanded**, or explicitly requested **Full Scan**;
- public evidence plus any private, local, signed-in, or connected evidence the user explicitly authorizes;
- evidence cutoff date;
- output format: dossier by default, or inline when explicitly requested;
- exact dated dossier path for file output, when supplied or confirmed.

Use **Focused** by default. Use **Expanded** for necessary adjacent surfaces. Use **Full Scan** only when requested. Present the complete surface catalog when the user asks for it or provides no usable objective.

Apply the shared provenance rules to the brief and project fact sheet. Resolve a missing dossier path before writing; independent authorized research may continue. Inline output requires no path and creates no files.

## Surface routing map

1. Business model and economics
2. Product and customer experience
3. Technology, data, and product AI
4. Engineering, delivery, reliability, security, and releases
5. Organization, workforce, internal operations, and internal AI
6. Market, marketing, and growth
7. Sales, distribution, and partnerships
8. Customer success, support, and community
9. Brand, public presence, and communications
10. Corporate, finance, governance, legal, risk, and investor relations

Treat this as a routing map, not ten mutually exclusive truths about a business. Treat strategy, stakeholder type, channel, lifecycle stage, and analytical lens as cross-cutting dimensions. Examples include B2B/B2C/enterprise/developer/investor, website/docs/social/changelog, and descriptive/comparative/competitive/replication/adaptation lenses.

Use **Applied Transfer** as the default lens: mechanism, prerequisites, evidence, transferability, project fit, trade-offs, and recommended action.

## Choose delivery

For explicit inline output, present the brief and project facts, selected surface coverage, candidate records, synthesis, provenance, and evidence mapping in the conversation. Use the same analytical requirements below, but replace file references with inline sections and attach citations directly or use a compact evidence table. Do not create a dossier or ask for its path.

For dossier output, use the supplied or confirmed path without asking again and follow the layout below.

## Create the dossier safely

Use:

```text
<output-root>/
└── <subject-slug>/
    └── <YYYY-MM-DD>-<target-slug>-<scope-slug>[-NN]/
        ├── 00-scope-and-project-context.md
        ├── 10-<selected-surface>.md
        ├── ...
        ├── 90-synthesis.md
        └── 99-evidence-register.md
```

Create files only for selected surfaces in the agreed brief. Never overwrite an existing run. When the user authorizes an output root with generated run naming, add `-02`, `-03`, and so on for collisions. When the user supplies an exact run path, preserve any existing destination and ask for a new one; do not silently change the path. Record the prior run when the new run refreshes it.

In `00-scope-and-project-context.md`, record the brief, included and excluded surfaces, project fact sheet, evidence boundary, provenance and cutoff date, run status, and any unresolved input.

## Pass 1: discover and freeze candidates

Research only selected surfaces within the agreed brief. Use bounded runtime subagents when surfaces are materially independent and parallel research improves speed or quality; otherwise work sequentially.

Give every worker the same frozen brief, project fact sheet, evidence cutoff, authorized-source boundary, and return schema. Prohibit recursive delegation and file writes. Have workers return:

- surface and scoped question;
- observed facts and citations;
- subject claims, corroboration, inference, contradictions, and unknowns;
- candidate capabilities, implementations, and practices;
- evidence limitations and cross-surface tags;
- status: `complete`, `partial`, or `blocked`.

Keep the coordinator responsible for deduplication and every durable write. Assign each credible, distinct transfer candidate a stable `CAND-001`, `CAND-002`, and so on. Freeze the candidate set before feasibility judgments. Do not create candidates merely to fill a selected surface. Close discovery when the selected evidence boundary has been covered or remaining gaps are documented under the shared completion rules; do not continue searching solely to grow the portfolio.

## Pass 2: evaluate candidates

Automatically evaluate every credible frozen candidate against the same target-project fact sheet. Apply the shared evidence and decision contract separately to each candidate, including its baseline, relevant simpler alternatives, and incremental value. If material drift is discovered, update the affected facts and candidate conclusions and record the change.

Preserve contradictions and cross-surface dependencies. Do not average verdicts or confidence. Issue one overall verdict only when the frozen brief asks one bounded thesis; otherwise produce a portfolio.

Each selected surface section, or file in a dossier, must contain:

```markdown
# <Surface Name>

- **Status:** [complete | partial | blocked]
- **Scoped Question:** [...]

## Evidence Map
[Observed facts, claims, corroboration, inference, unknowns, and limitations]

## Transfer Candidates
[Separate shared-contract decision record for each CAND-###]

## Surface-Level Implications
[Dependencies, conflicts, and unresolved questions; no forced surface verdict]
```

Map material claims and candidate decisions to their sources, evidence states, and relevant provenance. Use `99-evidence-register.md` in a dossier, or direct citations and a compact evidence mapping inline.

## Synthesize and handle partial runs

Organize the synthesis, saved as `90-synthesis.md` for a dossier, as:

- adopt now;
- adapt or validate;
- defer with revisit triggers;
- reject;
- unresolved because of insufficient evidence;
- cross-surface dependencies and sequencing;
- run status: `complete`, `partial`, or `blocked`.

When required surface research fails, preserve completed work, mark the exact gap, and label the synthesis `partial`, or `blocked` if no useful assessment can proceed. A covered surface with no credible candidates is `complete` with that finding. A completed candidate assessment can be `INSUFFICIENT EVIDENCE`; distinguish that evidence outcome from unfinished research. Never omit a failed surface silently or synthesize it as though completed.

## Boundaries

Analyze only. Inline delivery creates no files; dossier writes stay inside the supplied or confirmed path. Do not edit the target project or execute any candidate recommendation. A later implementation requires separate, explicit authority and fresh project-state verification.
