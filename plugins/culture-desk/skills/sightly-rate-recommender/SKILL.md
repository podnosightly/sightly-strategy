---
name: sightly-rate-recommender
description: >-
  Finds comparable past Sightly plans in Google Drive and turns them and the monthly rate library into
  confirmed, strategist-owned rates before a media plan is built. Pulls billing rates and history from
  the closest past plans (same agency, deal, formats, vertical, budget size), then walks tactic by
  tactic through every rate-library cut (overall, agency, category, geo) with median, range and sample
  size so the strategist decides each rate. Covers Steps 2 and 7 of the RFP workflow. Use for "find a
  comparable plan", "what have we charged for this before", "any similar RFPs we've done", "comparable
  plan retrieval", "help me price this RFP", "set rates for this brief", "what's our benchmark CPM for
  TikTok", "is $28 a reasonable CPM here". Feeds sightly-media-plan-builder. Not for updating the
  library, building the plan CSV (sightly-media-plan-builder) or
  setting a deck's structure.
---

# Sightly Rate Recommender

## What this skill does and why it exists

Sightly maintains a rate library — historical CPM/CPV/CPC/CPCV rates pulled from real client media plans, refreshed on the 1st of each month by a maintenance run outside this plugin and stored in Google Drive. The media plan builder deliberately refuses to guess rates: every rate follows the rate hierarchy (the deal's rate card, delivered rates from a comparable campaign, prior Sightly plans and the rate library, then a cited external benchmark labeled as a comparison; Rule 17 and `06_Media_Planning_Principles.md` › Where rates come from) and is confirmed by the strategist. That leaves a gap. Somebody has to turn the library's evidence into a confirmed number for each line before the plan gets built.

This skill fills that gap. It is a decision partner, not an autopilot. It lays the historical evidence in front of the strategist — for each tactic, every relevant benchmark cut with its sample size — and lets the strategist decide. The output is a confirmed rate card that becomes the strategist-confirmed rates the media plan builder consumes. The rate hierarchy stays intact, because by the time the builder runs, nothing is assumed — every rate was confirmed by a human against real data.

It also finds the closest past Sightly plans to a new brief and pulls what they tell the new work: the rates Sightly has billed for the same tactics, and the history worth citing. That is Step 2 of the RFP workflow (comparable plan retrieval), and those rates sit next to the library cuts when the strategist decides each rate at Step 7. Comparable plans inform pricing and historical framing only. Deck structure comes from elsewhere (the RFP's required sections, the strategist's example deck or the deck builder's layout).

The evidence here is Sightly's own historical deal data, so this is legitimate internal decision support. But the raw benchmark numbers are internal. Never let a distribution, a range, or a sample count land in a client-facing document — only the single confirmed rate belongs in a plan.

## The two source files (both Google Sheets in Drive)

Both live in the **Rate Cards and Benchmarks** folder (folder ID `19XFLRFr-CIWDMMp-0ZuA1id-VEjEZHBB`). Both are **Google Sheets** (export/download as CSV to parse). Match titles exactly — the folder also contains dated pipeline files (`rate_library_additions_YYYY-MM.csv`, run-status and worklist files) that are history, not sources.

**`summary_by_tactic_and_agency`** — the primary source. A single table (one tab) where every row carries a leading **`section`** column identifying which grouping it belongs to. Columns, in order: `section, channel, campaign_type, format, rate_type, agency_norm, geo, category, count, median, mean, min, max, currency, rate_types`. Group columns not used by a row's section are blank. Filter by `section`:

- `BY_TACTIC` — grouped by channel, campaign_type, format, rate_type. The overall market rate for a tactic.
- `BY_AGENCY_TACTIC` — adds agency_norm. What a specific agency has historically paid.
- `BY_GEO_CHANNEL` — grouped by geo, channel, rate_type. Regional pricing.
- `BY_CATEGORY_TACTIC` — adds category. What an advertiser vertical has historically paid.

`count` is sample size; `currency` is the group's most common currency; `rate_types` is the slash-joined set present in the group. The summary covers flight_year ≥ 2024 only.

**`rate_library_full_v3`** — the raw line items behind the summary, on the tab named **`data`**. Columns (17, in order): `source_file, agency, brand, category, channel, campaign_type, format, objective, rate_type, currency, net_rate, billing_rate, flight, notes, format_original, geo, flight_year`. Load this only when you need a tighter filter than the summary offers (e.g., "just this agency in this category since 2024") or the strategist wants to see the actual deals behind a benchmark.

**Freshness check:** the monthly update runs on the 1st. If the folder contains a `rate_library_additions_YYYY-MM.csv` dated *after* the master Sheet's last-modified time, that month's rows may not be merged yet — load it too and include its rows when computing cuts (or at minimum tell the strategist the benchmarks predate it).

Rates in the library are **`billing_rate`** — billing (gross). Label everything this skill proposes as a billing rate. If the strategist starts from a net or client-provided rate, record which, and show the margin applied to reach billing. Neither this skill nor the media plan builder nets a budget down.

## Inputs you need before you start

Collect these from the brief or the conversation. Ask in one batch if missing — don't interrogate one at a time.

- **Tactics** — the channel + format + rate_type for each line the plan will include (e.g., "YouTube VRC Efficient Reach, Multi-Format, CPV"; "TikTok Spark Ads, CPM"). This is the list you'll walk through.
- **Agency** — so you can pull the `BY_AGENCY_TACTIC` cut. If none, say so and skip that cut.
- **Brand category** — one of the standard verticals, for the `BY_CATEGORY_TACTIC` cut.
- **Geo** — for the `BY_GEO_CHANNEL` cut. Default to US if not stated.
- **Currency** — default USD; if CAD/GBP/EUR, filter benchmarks to that currency so you're not mixing.
- **For comparable plans, the rest of the pricing profile** from the confirmed intake: deal structure, budget size, rate types, flight timing, objective and audience.

If the strategist hasn't named the tactics yet, that's fine — help them assemble the tactic list first, then price it.

## The workflow

### Step 1 — Find comparable plans (Step 2 of the RFP workflow)

Requires the **Google Drive connector** (the Sales and Strategy campaign folders and past decks live there). If it isn't authorized, say so and stop. Do not guess at past work. At Step 2 of the RFP workflow, run only this step and stop: the tactic walk runs at Step 7, once the platform lineup exists.

1. **Search Drive** for past media plans (and their decks or wrap reports) that match the pricing profile. Prioritize (a) the same agency or deal structure with the same platforms and formats, (b) the same vertical and budget size, (c) the same objective or audience. Search the campaign folders, agency folders and proposal folders.
2. **Rank the candidates** and present the top 2–3, each with the client and campaign, plan date, why it matches, budget size, platform mix, the billing rate per tactic, and a link.
3. **Summarize what the matches tell the new plan:** the rate range per tactic with plan names and dates, carried into the tactic walk below; any past results or relationship history worth citing, each checked against the do-not-use list; and how the new brief differs (budget size, flight, geo, formats), so the strategist knows how far each comparable applies.

Rules for comparable plans:

- **Match on what moves price.** We price on agency, platform and format, rate type, budget size, geo and flight timing; a brand name alone tells us little. A different-vertical plan with the same agency and formats can be the better rate comparable.
- **Never invent a past campaign.** Only cite work you actually found in Drive. If nothing is a strong match, say so and name the closest partial match. A null result is valid: record it and price from the library.
- **Screen the rates.** Leave out barter and managed-exchange inventory rates, which the knowledge base excludes from Sightly standard rates, and keep MX/Horizon agency rows, which aren't barter and stay in the library (`06_Media_Planning_Principles.md` › What counts as a Sightly standard rate). Check whether an MX row records the client-facing IO rate, which is grossed up for the 27% discount. Check each rate's currency against its geo.
- **Rank the evidence by the rate hierarchy** (`06_Media_Planning_Principles.md` › Where rates come from). Delivered rates from a comparable campaign's performance or wrap report come second in that order and outrank the billing rates in its plan, which come third, alongside the rate library. A prior plan counts as a source. Label each rate with which it is.
- **Keep other clients internal.** Another client's name, data and results stay internal. A past result goes client-facing only as a proof point listed in `08_Proof_Points_and_Battle_Cards.md` or confirmed by the strategy team, after checking the do-not-use list there (Rule 16).

Output of this step, internal only: the top matches (client and campaign, plan date, match rationale, budget size, platform mix, Drive link); rates by tactic (billing or delivered rate, rate type, plan and date for every tactic the new brief uses); history worth citing, which goes to the narrative once checked; and what differs. Each rate carries its source plan and date.

### Step 2 — Load the library

Load `summary_by_tactic_and_agency` from Drive and split it into the four sections by the `section` column. Note the freshness (the monthly update runs on the 1st; check for an unmerged additions CSV as described above) so you can tell the strategist how current the data is. If the file can't be found, stop and say so — do not fall back to invented or externally-researched numbers, which would break the rate hierarchy (Rule 17) and the anti-fabrication discipline.

### Step 3 — Walk tactic by tactic (show all cuts, no default)

This is the core loop. Go through the tactics **one at a time** — present the evidence for a tactic, get the strategist's decision, then move to the next. Deliberate beats fast here; a rate that's off by a dollar compounds across a whole plan.

For each tactic, pull and display **every relevant cut side by side** — do not pre-pick a winner. The strategist decides which cut to weight. Present it like this:

```
YouTube · VRC Efficient Reach · Multi-Format · CPV
  Overall (BY_TACTIC)        median $0.042   range $0.030–$0.065   n=41
  Horizon Media (AGENCY)     median $0.038   range $0.032–$0.045   n=7
  Travel & Tourism (CATEGORY) median $0.045  range $0.035–$0.060   n=12
  US (GEO_CHANNEL)           median $0.043   range $0.030–$0.070   n=58
  Comparable plans (Step 1)  [plan name, date]: $0.040; [plan name, date]: $0.044

  Your call for this line?
```

Guidance to surface alongside the numbers, because it changes how much to trust each cut:

- **Sample size is everything.** A cut with n=3 is a rumor, not a benchmark. Call out thin samples explicitly ("agency cut is only n=3 — treat as directional") and steer weight toward cuts with more history.
- **The agency and category cuts are usually the most decision-relevant** — they reflect what this buyer / this vertical actually pays — but only when the sample supports it. When agency n is thin, the category or overall cut is the better anchor.
- **Flag divergence.** If the cuts disagree a lot (agency well below overall, say), name it and offer the likely reason (this agency negotiates hard, or these were older/smaller deals) so the strategist decides with eyes open.
- **Currency and geo consistency.** Never show a GBP benchmark next to a USD decision. Filter first. Known library defects (`06_Media_Planning_Principles.md` › Reading a library median, rate library check of 12 November 2026): Vodafone DE rows are tagged EUR when they're GBP; one plan (Assist Health, Q2 2025) appears about seven times, one copy under a different brand; some sources record net rates in the billing column; CPM and CPV rates sit under the same skippable format; and the skippable-on-CPM and bumper-and-skippable medians run higher with Horizon and HMI rows included. If a cut's median looks out of range, check the raw rows' `geo`, `currency` and `source_file` before using it.
- **Auction vs. reservation.** Reservation products (YouTube Select lineups, Pause Ads, Shorts First Position, YouTube TV, live-sports PiP) price on a different curve than auction tactics and their rates are subject to change at booking — don't blend the two when anchoring.
- **Masthead.** The library's "Masthead" rows may pool reserved homepage takeovers with lines that only carry the label; a client line has been priced off a $17 Masthead median while reserved mastheads ran $65–98. Until the rows are classified, don't price a reserved Masthead off a library median. Use only rows the monthly update has labeled as reserved, and say so.
- **The knowledge base's reference median.** Where `06_Media_Planning_Principles.md` › Reference CPMs from the rate library lists the tactic, show its 2026 median and typical range next to the cuts, marked internal. `06` counts each plan once in those medians and corrects them for the defects above. For the tactics `06` says have no reliable library figure (TikTok TopView, Meta Carousel and Lead Gen, mobile banner, DCO, high-impact display), say so and price from the deal or a comparable plan.

Record the strategist's decision for the line: the confirmed rate, which cut (if any) it was anchored to, and a one-line reason if they overrode the evidence. If they want to see the raw deals behind a number, pull the matching rows from `rate_library_full_v3` and show `source_file, agency, brand, billing_rate, flight, geo` — and screen out rows whose `notes` flag a suspect rate before presenting them as evidence.

If the strategist asks for a recommendation on a specific line, give one with reasoning ("I'd anchor to the category median of $0.045 — the agency cut is only n=4 and skews old"), but keep the decision theirs.

### Step 4 — Assemble the confirmed rate card

Once every tactic has a confirmed rate, produce a compact rate card the media plan builder can consume directly. Save it to the outputs folder as `<client>-confirmed-rates.csv` with these columns:

```
NETWORK, PLACEMENT, RATE TYPE, CONFIRMED RATE, ANCHOR CUT, SAMPLE SIZE, NOTES
```

- **NETWORK / PLACEMENT** map to the builder's NETWORK and PLACEMENT columns.
- **RATE TYPE** is the unit label — CPM, CPV, CPC, CPCV, Flat — matching the builder's BILLING CPU.
- **CONFIRMED RATE** is the dollar amount (pure number, no `$`, so it drops straight into the builder's CPU column).
- **ANCHOR CUT / SAMPLE SIZE / NOTES** are the internal audit trail — where the number came from and why. These are internal only; they exist so the decision is defensible in a QA pass, not for any client doc.

Also write a short markdown summary, `<client>-confirmed-rates-summary.md`: which rates were set, what they anchored to, any lines where the strategist overrode the data and why, and any tactics where the library had thin or no coverage (so the strategist knows those rates rest on judgment, not history).

### Step 5 — Offer the handoff (don't auto-run)

With the rate card confirmed, offer to hand off:

> "Rates are locked. Want me to run `sightly-media-plan-builder` with these pre-loaded as the strategist-confirmed rates? I'll still need the budget, flight dates, geos and the persona split for it."

Do not auto-invoke the builder — the strategist owns when the plan gets built, and the builder needs inputs this skill doesn't collect (budget, personas, allocation). If they say go, pass the confirmed rates through as the CPU for each matching NETWORK/PLACEMENT line so the builder never has to assume a rate.

## Sourcing and anti-fabrication discipline

Every number this skill shows must trace to the rate library or to a comparable plan found at Step 1 (named and dated). If a tactic has no coverage in any cut, say so plainly — "no library history for Reddit conversation ads; this rate will be your judgment call" — and never paper over the gap with an invented figure or an external "industry standard." If the strategist wants a comparison benchmark from outside the library, that's a separate research task, and any external number must be framed as an external benchmark, not a Sightly deal rate. **Other internal benchmark source:** Plan › Benchmarking (Sightly OS) can be cited as an internal benchmark. TikTok country cuts there reflect the targeted country, which can differ from where delivery landed; check the single-brand flag before quoting a country; the Programmatic clearing-price tab is internal only.

## What this skill does not do

- It does not update the rate library. That's the monthly maintenance run, outside this plugin.
- It does not build the plan CSV, allocate budget across personas, or run feasibility checks — that's `sightly-media-plan-builder`, which this skill feeds.
- It does not put benchmark distributions, ranges, or sample counts into client-facing materials — only the single confirmed rate travels downstream.
- It does not build the new audience, strategy or deck, and it does not set a deck's structure or arc.
- It does not put another client's name, data or results into client-facing work, and it does not fabricate a past campaign when no real match exists.
- It does not net down a budget. Margin appears only when converting a net or agency-discounted rate to billing, using the deal's formula.
