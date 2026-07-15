---
name: sightly-rate-recommender
description: "Turns the monthly Sightly rate library into confirmed, strategist-owned rates before a media plan is built. Loads summary_by_tactic_and_agency and rate_library_full_v3 from the Rate Cards and Benchmarks folder in Google Drive, and for each tactic shows every relevant benchmark cut — overall, agency, category, geo — with median, range, and sample size, walking tactic by tactic so the strategist decides each rate against real evidence. Use whenever a strategist needs to set, sanity-check, benchmark, or decide pricing: 'help me price this RFP', 'set rates for this brief', 'what's our benchmark CPM for TikTok', 'decide the rates before the media plan', 'is $28 a reasonable CPM here'. Runs BEFORE sightly-media-plan-builder and feeds it the confirmed rates. Not for updating the library (that's sightly-rate-library-monthly-update) or building the plan CSV (that's sightly-media-plan-builder)."
---

# Sightly Rate Recommender

## What this skill does and why it exists

Sightly maintains a rate library — historical CPM/CPV/CPC/CPCV rates pulled from real client media plans, refreshed monthly by `sightly-rate-library-monthly-update` and stored in Google Drive. The media plan builder deliberately refuses to guess rates: its Rate Policy says rates are *always provided by the strategist, never assumed*. That leaves a gap. Somebody has to turn the library's evidence into a confirmed number for each line before the plan gets built.

This skill fills that gap. It is a decision partner, not an autopilot. It lays the historical evidence in front of the strategist — for each tactic, every relevant benchmark cut with its sample size — and lets the strategist decide. The output is a confirmed rate card that becomes the strategist-provided rates the media plan builder consumes. The Rate Policy stays intact, because by the time the builder runs, nothing is assumed — every rate was confirmed by a human against real data.

The evidence here is Sightly's own historical deal data, so this is legitimate internal decision support. But the raw benchmark numbers are internal. Never let a distribution, a range, or a sample count land in a client-facing document — only the single confirmed rate belongs in a plan.

## The two source files (both in Drive)

Both live in the **Rate Cards and Benchmarks** folder (folder ID `19XFLRFr-CIWDMMp-0ZuA1id-VEjEZHBB`).

**`summary_by_tactic_and_agency`** — the primary source. Pre-aggregated benchmarks with `count, median, mean, min, max, currency, rate_types` for each group, in four sections:

- `BY_TACTIC` — grouped by channel, campaign_type, format, rate_type. The overall market rate for a tactic.
- `BY_AGENCY_TACTIC` — grouped by agency_norm, channel, campaign_type, format, rate_type. What a specific agency has historically paid.
- `BY_GEO_CHANNEL` — grouped by geo, channel, rate_type. Regional pricing.
- `BY_CATEGORY_TACTIC` — grouped by category, channel, campaign_type, format, rate_type. What an advertiser vertical has historically paid.

**`rate_library_full_v3`** — the raw line items behind the summary. Columns: `source_file, agency, brand, category, channel, campaign_type, format, objective, rate_type, currency, net_rate, billing_rate, flight, notes, geo, flight_year`. Load this only when you need a tighter filter than the summary offers (e.g., "just this agency in this category since 2024") or the strategist wants to see the actual deals behind a benchmark.

Rates in the library are **`billing_rate`** — gross/billing side. The media plan builder handles net-vs-gross and the 30% margin separately, so label everything this skill proposes as a billing rate and don't try to net it down here.

## Inputs you need before you start

Collect these from the brief or the conversation. Ask in one batch if missing — don't interrogate one at a time.

- **Tactics** — the channel + format + rate_type for each line the plan will include (e.g., "YouTube VRC Efficient Reach, Multi-Format, CPV"; "TikTok Spark Ads, CPM"). This is the list you'll walk through.
- **Agency** — so you can pull the `BY_AGENCY_TACTIC` cut. If none, say so and skip that cut.
- **Brand category** — one of the standard verticals, for the `BY_CATEGORY_TACTIC` cut.
- **Geo** — for the `BY_GEO_CHANNEL` cut. Default to US if not stated.
- **Currency** — default USD; if CAD/GBP/EUR, filter benchmarks to that currency so you're not mixing.

If the strategist hasn't named the tactics yet, that's fine — help them assemble the tactic list first, then price it.

## The workflow

### Step 1 — Load the library

Load `summary_by_tactic_and_agency` from Drive and parse the four sections. Note the freshness (the monthly update runs on the 1st) so you can tell the strategist how current the data is. If the file can't be found, stop and say so — do not fall back to invented or externally-researched numbers, which would violate the Rate Policy and the anti-fabrication discipline.

### Step 2 — Walk tactic by tactic (show all cuts, no default)

This is the core loop. Go through the tactics **one at a time** — present the evidence for a tactic, get the strategist's decision, then move to the next. Deliberate beats fast here; a rate that's off by a dollar compounds across a whole plan.

For each tactic, pull and display **every relevant cut side by side** — do not pre-pick a winner. The strategist decides which cut to weight. Present it like this:

```
YouTube · VRC Efficient Reach · Multi-Format · CPV
  Overall (BY_TACTIC)        median $0.042   range $0.030–$0.065   n=41
  Horizon Media (AGENCY)     median $0.038   range $0.032–$0.045   n=7
  Travel & Tourism (CATEGORY) median $0.045  range $0.035–$0.060   n=12
  US (GEO_CHANNEL)           median $0.043   range $0.030–$0.070   n=58

  Your call for this line?
```

Guidance to surface alongside the numbers, because it changes how much to trust each cut:

- **Sample size is everything.** A cut with n=3 is a rumor, not a benchmark. Call out thin samples explicitly ("agency cut is only n=3 — treat as directional") and steer weight toward cuts with more history.
- **The agency and category cuts are usually the most decision-relevant** — they reflect what this buyer / this vertical actually pays — but only when the sample supports it. When agency n is thin, the category or overall cut is the better anchor.
- **Flag divergence.** If the cuts disagree a lot (agency well below overall, say), name it and offer the likely reason (this agency negotiates hard, or these were older/smaller deals) so the strategist decides with eyes open.
- **Currency and geo consistency.** Never show a GBP benchmark next to a USD decision. Filter first.

Record the strategist's decision for the line: the confirmed rate, which cut (if any) it was anchored to, and a one-line reason if they overrode the evidence. If they want to see the raw deals behind a number, pull the matching rows from `rate_library_full_v3` and show `source_file, agency, brand, billing_rate, flight, geo`.

If the strategist asks for a recommendation on a specific line, give one with reasoning ("I'd anchor to the category median of $0.045 — the agency cut is only n=4 and skews old"), but keep the decision theirs.

### Step 3 — Assemble the confirmed rate card

Once every tactic has a confirmed rate, produce a compact rate card the media plan builder can consume directly. Save it to the outputs folder as `<client>-confirmed-rates.csv` with these columns:

```
NETWORK, PLACEMENT, RATE TYPE, CONFIRMED RATE, ANCHOR CUT, SAMPLE SIZE, NOTES
```

- **NETWORK / PLACEMENT** map to the builder's NETWORK and PLACEMENT columns.
- **RATE TYPE** is the unit label — CPM, CPV, CPC, CPCV, Flat — matching the builder's BILLING CPU.
- **CONFIRMED RATE** is the dollar amount (pure number, no `$`, so it drops straight into the builder's CPU column).
- **ANCHOR CUT / SAMPLE SIZE / NOTES** are the internal audit trail — where the number came from and why. These are internal only; they exist so the decision is defensible in a QA pass, not for any client doc.

Also write a short markdown summary, `<client>-confirmed-rates-summary.md`: which rates were set, what they anchored to, any lines where the strategist overrode the data and why, and any tactics where the library had thin or no coverage (so the strategist knows those rates rest on judgment, not history).

### Step 4 — Offer the handoff (don't auto-run)

With the rate card confirmed, offer to hand off:

> "Rates are locked. Want me to run `sightly-media-plan-builder` with these pre-loaded as the strategist-provided rates? I'll still need budget (net or gross), flight dates, geos, and the persona split for it."

Do not auto-invoke the builder — the strategist owns when the plan gets built, and the builder needs inputs this skill doesn't collect (budget, personas, allocation). If they say go, pass the confirmed rates through as the CPU for each matching NETWORK/PLACEMENT line so the builder never has to assume a rate.

## Sourcing and anti-fabrication discipline

Every number this skill shows must trace to the rate library. If a tactic has no coverage in any cut, say so plainly — "no library history for Reddit conversation ads; this rate will be your judgment call" — and never paper over the gap with an invented figure or an external "industry standard." If the strategist wants a comparison benchmark from outside the library, that's a separate research task, and any external number must be framed as an external benchmark, not a Sightly deal rate.

## What this skill does not do

- It does not update the rate library — that's the monthly `sightly-rate-library-monthly-update`.
- It does not build the plan CSV, allocate budget across personas, or run feasibility checks — that's `sightly-media-plan-builder`, which this skill feeds.
- It does not put benchmark distributions, ranges, or sample counts into client-facing materials — only the single confirmed rate travels downstream.
- It does not net down billing rates or apply margin — the builder owns that.
