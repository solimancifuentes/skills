---
name: company-intelligence-profile
description: "Research a company or compare a small set of companies in concise, source-backed inline profiles, adapting to company type and purpose. Use for company status, products, leadership, funding, financials, competitors, or business risks. Excludes buy/sell recommendations, broad due diligence, and people-only research."
---

# Company Intelligence Profile

## Purpose

Produce a fast, accurate, token-efficient **inline** company intelligence report directly in the chat response. The report adapts its structure to what the company actually is (public, startup, subsidiary, nonprofit, stealth, etc.) rather than forcing every company into one mold. It never fabricates data: facts that cannot be established from the sources reviewed are skipped in the body and noted briefly at the end.

This skill is agent-agnostic. It assumes only generic capabilities (optionally: web search, page fetch, structured APIs). Do not rely on any specific model, product, or vendor behavior.

## When to use

Use for focused company research:

- User names a company (or gives a domain, ticker, Crunchbase/LinkedIn URL, or a vague description) and wants to understand it: status, funding, valuation, financials, leadership, products, competitors, risks, news.
- User asks for investor-style, sales-prospecting, recruiting, or public-market analysis of a company.
- User asks to compare a small set of companies (produce one compact profile per company plus a short comparison table).

Keep this an informational research workflow. Do not use it for buy/sell recommendations, deep multi-day due-diligence engagements, or people-only research with no company focus.

## Evidence access and privacy

Public research needs no separate approval step. Use private, local, signed-in, or connected sources only within the user's granted access and task scope. Permission to inspect a source does not authorize public disclosure: minimize confidential and personal details, respect the report's intended audience, and mark confidential material when sharing limits matter. A sales profile does not authorize outreach, contacting employees, or publishing the report.

## Inputs accepted

- Company name (possibly ambiguous)
- Website/domain
- Stock ticker
- Crunchbase URL
- LinkedIn URL
- Short or fuzzy description ("that French AI agent startup")
- Optional depth mode and constraints (see below)

## Workflow

Follow these steps in order. The goal is minimum searching for maximum reliable coverage.

1. **Identify the company.** Resolve name/domain/ticker/URL to one specific entity.
   - If ambiguity is minor and context makes one candidate clearly likely, proceed and state the assumption in one line ("Assuming you mean X, the Y company — say so if you meant another").
   - If ambiguity could materially change the answer (two well-known companies share a name), ask ONE short clarification question and stop.
2. **Classify the company.** Determine category using `checklists/company-classification.md`, verifying the exact entity's status at the requested reporting date. Distinguish reporting obligations, offering progress, and equity trading. Category drives which report sections exist and which sources to hit first. Never assume "startup" by default.
3. **Research in source-priority order.** Use `checklists/source-priority.md` for the category. Search the most authoritative source first; gather only enough to fill the relevant sections. Stop chasing a metric after 1–2 reasonable attempts if it's likely non-public — record it for Sidenotes instead.
4. **Write the inline report.** Use the structure in `templates/company-report.md`, adapted to category and depth mode. Cite sources if the environment supports citations; otherwise name/link them in the Sources section.
5. **Close with Sources and Sidenotes.** Sidenotes list expected-but-unavailable fields in one line each — no long apologies.

## Company classification

Read `checklists/company-classification.md` before classifying. Categories (choose the best fit dynamically):

1. Public company
2. Recently IPO'd company (confirmed completed IPO within ~18 months of the reporting date)
3. Private startup (venture-track, growth-oriented; includes solo businesses, indie projects, and scaleups)
4. Private non-startup company (established private business, family-owned, PE-owned, bootstrapped SMB)
5. Acquired company / subsidiary
6. Nonprofit / foundation
7. Government-owned or state-linked entity
8. Stealth / very limited public information
9. Unknown / insufficient data

State the category and one-line reasoning in the report's "Status & Classification" section. If evidence is mixed (e.g., recently acquired startup), pick the category that best predicts what data exists, and note the nuance.

## Source priority

Read `checklists/source-priority.md` for the ordered source list per category. Core principle: **authoritative and primary beats aggregated and secondary.** Company IR pages and securities filings beat finance blogs; a company's own site and funding announcements beat third-party estimates. Use aggregators (Crunchbase-style data, traffic estimators, review sites) as secondary signals, and label their numbers as estimates.

## Report format

Use `templates/company-report.md` as the default skeleton. Key rules:

- **Inline only.** Render the report in the chat response. Do not create files, artifacts, PDFs, decks, or spreadsheets unless the user explicitly asks for one.
- **Adapt sections to category and mode.** Drop sections that don't apply (no "Funding rounds" for a 100-year-old public utility; no "Stock price" for a seed startup). Include stock fields only for the target's confirmed publicly traded equity, using dated values. Never pad with generic filler.
- **Keep the Snapshot tight.** Include only fields with real values. A field with no public value moves to Sidenotes — never a wall of "Unknown" rows.
- **Company Journey & Milestones (companies without publicly traded equity).** When supported history adds useful context, include up to 10 dated one-line bullets tracing origins, launches, funding or bootstrap milestones, pivots, partnerships, acquisitions, and current stage. There is no minimum; omit the section when evidence is sparse or the requested brevity makes it unnecessary. For publicly traded companies, fold key history into the Overview instead.
- **FAQs:** Optional short Q&As that answer relevant questions not already covered. Do not repeat the report to fill a quota. Omit FAQs in quick mode unless requested.
- **Dates on numbers.** Every financial/funding figure gets a date or period ("$65M Series B, Jun 2024"; "FY2025 revenue"). If data is likely stale, say so in a few words.

## Depth modes

Default to **standard**. Auto-select a better fit when the user's intent is obvious (e.g., "investment-relevant research" signals investor mode; "I'm prospecting them" signals sales mode). Honor explicit requests within the informational research scope.

- **quick** — Snapshot, executive summary, key financial/funding facts, sources, sidenotes. ~1/3 the length of standard. No dedicated timeline is required; omit FAQs unless requested.
- **standard** — Full default template.
- **deep** — Standard plus more detailed competitive, financial, funding, leadership, and risk analysis. Only when explicitly requested.
- **investor** — Emphasize funding history, traction, market size/dynamics, competitors, risks, and investment-relevant signals. Provide research, not buy/sell recommendations.
- **public-market** — Emphasize financial statements, stock performance, filings highlights, valuation context (market cap vs. enterprise value, key multiples only if source-reported), and filing-disclosed risks.
- **sales** — Emphasize overview, relevant professional roles, tech stack if publicly discoverable, growth signals, and potential business needs. Label inferred pain points and outreach angles as sales hypotheses, separate from source-supported facts.
- **recruiting** — Emphasize stability, leadership, funding/runway signals, hiring trends, culture signals (public only), and risks.

## User constraints

Honor constraints such as: "include stock info", "focus on funding", "focus on ARR/MRR", "only public sources", "no paid databases", "use Crunchbase if available", "compare against competitors", "make it concise", "investor-style", "sales prospecting", "recent only", "before [date]", "as of [date]". Date constraints mean: report the state as of that date and label figures accordingly. Keep the reporting date distinct from the retrieval date and exclude later events from an as-of profile.

## Token efficiency rules

1. Identify + classify first; this prevents wasted searches.
2. Hit the most authoritative source for each section first.
3. Gather only what fills the relevant sections. Do not exhaustively read every result.
4. Stop after 1–2 attempts on a metric that is probably non-public (e.g., private ARR). Move it to Sidenotes.
5. Never explain at length why data is missing — one line in Sidenotes.
6. Never copy long passages from sources; paraphrase compactly.
7. Prefer compact tables/field lists and tight prose.
8. Include only material news signals, not every article.
9. Match report length to available data and depth mode. A stealth company gets a short honest report, not a padded one.

## Accuracy and unavailable-data rules

- Never guess or invent private financials — no fabricated ARR, MRR, revenue, valuation, or headcount.
- After unsuccessful searches, use "Not found in the sources reviewed." Reserve "not publicly disclosed" for supporting evidence, such as an attributed company statement about nondisclosure. A search stopping limit does not establish that information is unavailable everywhere.
- Label estimates as estimates and name the estimating source.
- Distinguish source-supported facts, estimates, and analytical inferences. Sales hypotheses about a company's needs are not established facts, even when plausible.
- If sources disagree, note the discrepancy in one clause ("employee count reported as 250 (LinkedIn) vs ~400 (press, 2025)").
- Distinguish precisely: for public companies — market cap vs. enterprise value vs. revenue vs. net income vs. stock price; for private companies — funding raised vs. valuation vs. revenue vs. ARR/MRR vs. estimated size. Never conflate funding with revenue, valuation with market cap, or ARR/MRR with total (recognized) revenue.
- Avoid "net worth" language for companies; use valuation, market cap, revenue, assets, or enterprise value as appropriate.
- Do not treat marketing claims ("trusted by 10,000+ teams") as verified financials; if used, attribute them ("company claims…").
- Keep investment-related output informational. If asked for a buy/sell recommendation, explain that this profile provides evidence, risks, and open questions rather than a trading recommendation.

## Tool availability

- **No web access:** Say live retrieval is unavailable, use only provided context, ask the user for a website/documents/links, and never pretend to have current data.
- **Browsing available:** Use it. Verify current facts — status, price, executives, funding, valuation. Cite sources.
- **APIs available:** Prefer structured/official APIs over generic search: securities regulator filings (SEC/EDGAR or equivalent) for public companies, finance/stock APIs for prices, Crunchbase/Dealroom/PitchBook-style data for funding, enrichment sources only when available and permitted.
- **Multiple tools:** Use the minimum set that yields reliable data; do not call every tool by default.

## Examples of user requests

These illustrate the scope; placeholder company names and domains are fictional.

- "Build a company profile for Northfield Manufacturing at manufacturing.example.com."
- "Research this regional food distributor: ownership, products, leadership, and competitors."
- "Give me an investor-style profile of this private robotics company, using reported figures."
- "Is this utility publicly traded? Give me its stock, revenue, executives, and business risks."
- "Company intelligence profile for Cedar Analytics at analytics.example.com."
- "Give me a sales prospecting profile for [company], separating facts from possible needs."
- "Quick profile of this nonprofit: mission, programs, funding, and leadership."
- "Compare the business models and financial results of these two retailers."

## Example output skeleton (abbreviated)

Illustrative structure only: the company, people, figures, and source references below are fictional. Omit the timeline or optional sections when they do not add supported information at the requested depth.

```
## Company Intelligence Profile: Acme Robotics

### Snapshot
| Field | Value |
|---|---|
| Company | Acme Robotics, Inc. |
| Website | robotics.example.com |
| Category | Private startup (Series B) |
| Founded | 2019 — Austin, TX |
| CEO / Founders | J. Doe (CEO, co-founder); K. Lee (CTO, co-founder) |
| Employees | ~180 (third-party estimate, Jun 2026) |
| Funding | $92M total as of Jun 2024; $65M Series B (Jun 2024) |
| Valuation | $480M (Series B, press-reported, Jun 2024) |
| Reporting date | 2026-07-08 |

### Executive Summary
…1–3 tight paragraphs…

### Company Journey & Milestones
- 2019 — Founded by … after …
- 2020 — Launched first product …
- 2022 — $8M Seed (Investor X) …
- 2024 — $65M Series B; expanded to Europe …

### Company Overview / Status & Classification / Financial & Funding Profile /
Leadership & Key People / Products, Services & Business Model /
Market, Competitors & Positioning / Recent Signals & Insights /
Risks, Open Questions & Watch Items / FAQs (optional) / Sources

### Sidenotes / Unavailable Information
- ARR/MRR not found in the sources reviewed.
- Current headcount is a third-party estimate.
```

## What NOT to do

- Do not create an external artifact/file by default — the report is inline.
- Do not fabricate private financials or invent ARR/MRR/valuation/revenue/headcount.
- Do not over-research clearly unavailable data.
- Do not return a long report padded with "unknown" rows or filler sections.
- Do not assume every company is a startup — classify first.
- Do not confuse funding raised with revenue, valuation with market cap, or ARR/MRR with total revenue.
- Do not present estimates as facts or omit dates on financial figures when available.
- Do not give buy/sell recommendations; keep investment-related profiles informational.
- Do not depend on any specific model, agent product, or vendor capability.
