# Company Classification Checklist

Classify BEFORE deep research — the category determines which sources to hit and which report sections exist. Verify the exact entity and its status at the requested reporting date, using the cheapest decisive evidence first. A ticker or filing is a research lead, not a conclusion; one or two targeted checks may settle the status, but unresolved evidence must remain qualified.

## Decision path

1. **Publicly traded equity confirmed for this entity at the reporting date?** Check dated exchange, OTC market, or company evidence that identifies the security and trading status. If confirmed → **Public company**. Use **Recently IPO'd** only when a completed IPO date is confirmed within ~18 months of the reporting date. An OTC quotation can establish public trading; a direct listing is not necessarily an IPO. A proposed, historical, or parent-company ticker does not establish the target's current status.
2. **Only reporting or offering evidence found?** A 10-K, 20-F, or equivalent can establish reporting obligations without establishing public trading in common shares. A filed or effective S-1 does not by itself establish a completed IPO or first trading day; a pending S-1 also does not establish that an already-public issuer is private. Check the relevant ownership, offering, and trading evidence, then use the best-supported existing category with a brief qualification about reporting obligations or offering progress. If equity-trading status remains unverified, say so and omit unsupported stock fields. Keep a proposed offering price distinct from a traded stock price.
3. **Acquisition announced and closed?** (acquirer press release, filing, credible news) → **Acquired / subsidiary**. If it operates as an independent brand, still classify here but describe brand/integration status.
4. **Nonprofit signals?** (.org + mission language, 501(c)(3)/charity registration, Form 990 or equivalent, "foundation"/"institute" naming with grant activity) → **Nonprofit / foundation**. Beware: some companies use .org while being for-profit — registration/filings decide, not the domain.
5. **Government/state ownership?** (state is majority owner, statutory body, SOE listings, government ministry parent) → **Government-owned / state-linked**.
6. **Private with venture/growth signals?** (funding rounds announced, accelerator alumni, VC investors listed, rapid hiring, "we're building X" positioning, or a small indie/solo operation with growth intent) → **Private startup**. This bucket spans solo businesses and indie projects through scaleups — note the sub-stage:
   - Solo/indie: one or few founders, no institutional funding, product-led.
   - Pre-seed/Seed: first institutional money, early product.
   - Series A–B: product-market fit signals, scaling team.
   - Series C+/scaleup/growth: large rounds, expansion, possible pre-IPO.
   Infer stage only from evidence (round names, headcount, age); if unclear, say "stage not clearly inferable."
7. **Private without venture-track signals?** (decades old, family/PE/employee-owned, bootstrapped SMB, professional services firm) → **Private non-startup company**.
8. **Almost nothing public?** (bare landing page, no team page, "stealth" on LinkedIn, unexplained funding rumor) → **Stealth / limited info**.
9. **Can't even confirm the entity exists or which one is meant?** → **Unknown / insufficient data** — report what was checked and ask one clarifying question.

## Edge cases

- **Recently acquired startup:** classify as Acquired/subsidiary (predicts available data better); include supported startup milestones when useful at the requested depth.
- **Subsidiary of a public parent:** Acquired/subsidiary unless the target itself has publicly traded equity. A parent's ticker or market capitalization is not the subsidiary's. Use parent filings for separately reported information, labeling segment figures as such.
- **Public company that was taken private:** Use Private non-startup or Acquired/subsidiary according to the confirmed ownership; do not assume PE ownership. Note the completed transaction and relevant trading/delisting dates. A historical ticker does not establish current public trading.
- **Suspended or delisted shares:** Verify ownership and any continuing OTC trading. Suspension or exchange delisting alone does not establish a completed take-private transaction.
- **Dual entities (nonprofit + capped-profit / for-profit arm):** classify by the entity the user most likely means; note the structure explicitly.
- **Shut down / defunct:** keep the best-fit historical category, set Status = "ceased operations (date)".
- **Rebrand / renamed:** profile the current entity; note former names in the overview.

## Evidence quality

Prefer: filings > official announcements (company/acquirer/exchange) > structured databases > reputable press > social profiles > rumors. Never classify on a rumor alone; if only rumors exist, say so.

For the US distinction between reporting obligations, registered offerings, and exchange or OTC trading, see the [SEC's Public Companies guidance](https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/public-companies). Apply the relevant jurisdiction's evidence to the target.
