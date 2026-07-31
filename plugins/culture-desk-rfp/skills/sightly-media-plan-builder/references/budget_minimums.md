# Sightly Budget Minimums — Feasibility Reference

This is the feasibility gate the media plan builder consults in Step A. Embedded here so the skill works without needing the broader Sightly knowledge base. If `09_Budget_Minimums.md` is available in the working directory, prefer that — it's the source of truth and may be more recent.

## Tier definitions

| Tier | Description |
|---|---|
| **Tier 1** | Upper-funnel per ad format (standard ad formats, VCR, CTR, awareness KPIs) or high-priority account. |
| **Tier 2** | Lower-funnel per ad format (conversion, dynamic ad formats, influencer) or standard account. |
| **Tier 3** | Hyper-localized, 4+ personas (multiple cut minimums). |

## Which column to use

**Compare against the Gross columns.** The client's budget is a gross/billing figure and the plan
sums to it, so the gross minimums are the live gate. The NET columns are retained for reference
only — never convert a client budget to net in order to run this check.

Gross minimums were originally derived assuming a 30% margin. That derivation is history, not an
instruction: do not apply a 30% conversion to anything. All figures are **minimums per month**.

**Open item — the gross figures are approximate.** They assume roughly 30% margin, but real plans
have run nearer 15%. When a platform lands close to its floor, say that the floor itself is
approximate rather than reporting a clean pass or fail. Whether this table should carry a margin
range is an unresolved decision, not something to settle inside a build.

## Platform minimums

| Platform | Tier 1 NET/mo | Tier 1 Gross/mo | Tier 2 NET/mo | Tier 2 Gross/mo | Tier 3 NET/mo | Tier 3 Gross/mo |
|---|---|---|---|---|---|---|
| YouTube (Google Ads Auction) | $2,450 | $3,500 | $10,500 | $15,000 | $12,250 | $17,500 |
| YouTube (Google Ads Reservation) | Contact Strategy | Contact Strategy | Contact Strategy | Contact Strategy | Contact Strategy | Contact Strategy |
| YouTube (DV360 Ads Auction) | $2,450 | $3,500 | $10,500 | $15,000 | $12,250 | $17,500 |
| YouTube (DV360 Ads Reservation) | Contact Strategy | Contact Strategy | Contact Strategy | Contact Strategy | Contact Strategy | Contact Strategy |
| Programmatic (DV360 Auction) | $2,450 | $3,500 | $10,500 | $15,000 | $12,250 | $17,500 |
| Programmatic (DV360 Deal ID) | $2,450 | $3,500 | N/A | N/A | $12,250 | $17,500 |
| Meta | $3,500 | $5,000 | $7,000 | $10,000 | $17,500 | $25,000 |
| TikTok | $2,450 | $3,500 | $5,250 | $7,500 | $12,250 | $17,500 |
| Reddit | $3,500 | $5,000 | $7,000 | $10,000 | $17,500 | $25,000 |
| Pinterest | $3,500 | $5,000 | $7,000 | $10,000 | $17,500 | $25,000 |
| Snap | $5,250 | $7,500 | $8,750 | $12,500 | $26,250 | $37,500 |
| X (Twitter) | $5,250 | $7,500 | $8,750 | $12,500 | $26,250 | $37,500 |
| Livestreaming (24/7) | $5,000 | $7,142.86 | N/A | N/A | N/A | N/A |
| Livestreaming (Live Games) | Contact Strategy | Contact Strategy | Contact Strategy | Contact Strategy | Contact Strategy | Contact Strategy |

## Platform-specific minimums (additional)

- **TikTok**: Minimum $20/day per ad group. Account for this floor when splitting budget across multiple ad groups.
- **Spotify**: Minimum $250 per campaign. Managed-service threshold is $25K.

## Usage rules

1. **Always check minimums before building a plan.** This is the first feasibility gate.
2. **Always call out when a plan falls below minimums.** Include the specific platform and tier that is underfunded.
3. **Explain the consequence**, not just the number — insufficient delivery, inability to optimize, lack of statistical significance, learning-period risk.
4. **Client overrides are acceptable** when the callout has been made and acknowledged. The flag is what matters.
5. **Never silently plan below the floor.** An underfunded line that has been flagged and discussed is fine. One that was never mentioned is a planning failure.

## Tier detection cheat sheet

When deciding which tier applies to a line item:

- **Tier 1 cues**: awareness, reach, video views, brand lift, completion, upper-funnel, standard formats (Skippable, Bumper, Feed Video, standard Carousel, standard Display).
- **Tier 2 cues**: conversion, signup, purchase, lower-funnel, dynamic creative, dynamic product ads, lead-gen forms, influencer / creator partnerships, advanced shopping ads.
- **Tier 3 cues**: hyper-localized (single DMA, single ZIP cluster), 4 or more personas in scope, multi-cut creative requirements.

When a platform has both upper- and lower-funnel line items in the same plan, apply the relevant tier to each line independently.
