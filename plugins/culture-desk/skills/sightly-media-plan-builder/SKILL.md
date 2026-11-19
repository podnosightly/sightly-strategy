---
name: sightly-media-plan-builder
description: Builds Sightly Standard Media Plan tables as CSVs from a strategist's brief. Walks through the full RFP Step 7 workflow — feasibility check against budget minimums, persona-level budget allocation, line-item construction in the canonical 14-column structure, and pressure-test callouts (pacing, learning periods, geo spread, saturation). Use whenever the user mentions building a media plan, tactics table, line items, budget allocation across platforms or personas, "Step 7", or asks to turn a brief into a plan. Triggers on requests like "build me a media plan", "draft the tactics table", "allocate this budget across personas", "turn this brief into a plan", "build the Sightly Standard output", "feasibility check this budget", or any mention of campaign line items with platforms, flight dates, and rates.
---

# Sightly Media Plan Builder

## What this skill does

This skill turns a Sightly brief into a CSV media plan that conforms to the **Sightly Standard Media Plan Output** column structure. It runs the substeps of Step 7 of the RFP Workflow in order:

1. **Feasibility check** against `references/budget_minimums.md` (or `05_Budget_Minimums_and_Feasibility.md` if the knowledge base is available), flagging any platform below its monthly minimum.
2. **Agency deal check** — if MX (Horizon), Active or Agyle applies, apply the deal mechanics before pricing.
3. **Persona-level budget allocation** — split the budget by strategic weight, not evenly.
4. **Line-item build** in the canonical column structure, with deterministic math.
5. **Pressure-test pass** — flag pacing, learning periods, geo spread, saturation, timing risks.

Invoking this skill is the strategist's request to build a plan (`13_When_Asked_to_Build.md` › Media plans), and the strategist sets the order and scope. The deliverable is a CSV the strategist drops into a working spreadsheet or deck. A short narrative summary accompanies the file: what the plan does, what was flagged, and which decisions still need strategist confirmation.

## When this is the wrong skill

If the strategist wants a persona-only output, a Brand Mentality pull, deck copy, or a battle card, this is not the right skill. This skill produces the tactics table at the heart of Step 7 — nothing more, nothing less.

If the strategist hasn't given you a budget, flight window, or at least one persona, ask before building. The skill will not invent these.

## The Sightly Standard Media Plan Output — 14 columns

Every CSV uses exactly these columns in this order:

```
PLACEMENT TYPE, NETWORK, PLACEMENT, TARGET, FEATURES, START DATE, END DATE, BILLING CPU, CPU, BUDGET, ESTIMATED IMPRESSIONS, ESTIMATED VIEWS, ESTIMATED VIEW RATE, NOTES
```

Column meanings — internalize these before building:

- **PLACEMENT TYPE**: the category (Video, Display, Native, Audio, Social, Search).
- **NETWORK**: the platform / network (YouTube, Meta, DV360, TikTok, Reddit, Spotify, Pinterest).
- **PLACEMENT**: the specific ad unit (e.g., "In-Stream Skippable", "Bumper", "Carousel", "Promoted Pin", "Audio Everywhere").
- **TARGET**: which persona this line item serves. Use the persona's name exactly as the brief wrote it (or its confirmed persona name when the brief named none), never a numbered code like "Persona 1".
- **FEATURES**: targeting features, format specs, special capabilities — Anticipation Board moments, SmartLists, BAV quadrant alignment, custom intent, IAS categories applied at line-item level.
- **START DATE**, **END DATE**: flight dates in ISO format (`YYYY-MM-DD`).
- **BILLING CPU**: the **pricing unit label** — `CPM`, `CPV`, `CPC`, or `Flat`. Not a dollar amount; the rate per unit goes in CPU, as in Sightly's live plans. `06_Media_Planning_Principles.md` and `13_When_Asked_to_Build.md` define BILLING CPU as the client-facing rate. A correction to both files is staged (17 November 2026); until it is applied, follow this skill for these two columns.
- **CPU**: the **dollar amount** per unit. E.g., `$5.00` for a $5 CPM, `$0.04` for a $0.04 CPV.
- **BUDGET**: dollar amount allocated to this line.
- **ESTIMATED IMPRESSIONS**: see Math section below.
- **ESTIMATED VIEWS**: video lines only; otherwise leave blank.
- **ESTIMATED VIEW RATE**: video lines only; from the strategist or a cited benchmark (see "Estimated view rate" below). Non-skip and bumper lines carry no default view rate.
- **NOTES**: caveats, callouts, dependencies, reservations needed, anything the strategist or sales lead must know about this line.

**UK plans.** When the plan's geo or currency is UK/GBP, replace the single CPU column with two: **NET CPU** (net + 15%) and **GROSS CPU** (net + 30%), both taken as margin off gross (NET CPU = GROSS CPU × 0.85; Sightly net = GROSS CPU × 0.70). Use the strategy team's most recent UK plans as the reference for headers and rate estimates.

Additional fields that may belong as columns or in NOTES depending on plan complexity: **Site Served**, **IAS Blocking**, **Device** (default to "All Devices" unless device-level breakouts are part of the strategy). When unsure, put them in NOTES.

### Moments reserve representation

**Only when the confirmed strategy calls for a reserve.** If the reactive component runs through a single consolidated auto-optimizing buy, there is no separate reserve line — see the precedence note in Step B.

When a moments reserve is part of the plan (Brand Mentality data is available and the campaign has a reactive component), include it as its own line items at the bottom of the CSV — do not bury it inside a regular persona line. Use:

- **PLACEMENT TYPE**: `Reserve`
- **NETWORK**: the platform the reserve will activate on (e.g., `DV360`, `Meta`, `YouTube`).
- **PLACEMENT**: `Moments Reserve — <NETWORK label>` (e.g., `Moments Reserve — Programmatic Display`).
- **TARGET**: `All personas` or the specific persona the reserve is associated with.
- **NOTES**: spell out the trigger criteria (which Anticipation Board moments) and the activation dependency (creative variants needed by X date).

This keeps the reserve visible to the strategist as a discrete budget bucket and makes it easy to drop or resize without unwinding the rest of the plan.

### Totals row

Append a final `TOTAL` row at the bottom of the CSV. Sum the **BUDGET** column only. Leave the other numeric columns blank in the TOTAL row — summing impressions or views across CPM, CPV, and CPC lines produces a meaningless number because each line is measuring something different (impressions for CPM, views for CPV, clicks for CPC), and a fake aggregate can mislead a sales lead reading the file later.

Format:

```
TOTAL,,,,,,,,,150000.00,,,,
```

(Empty trailing cells are fine. The point is a one-glance dollar total for the plan.)

## The workflow

### Step A — Feasibility check (always first)

Before touching any line items, validate that the budget can fund what the brief calls for. Read `references/budget_minimums.md` (or `05_Budget_Minimums_and_Feasibility.md` if the knowledge base is available). There is one list of monthly minimums; the old tiers were retired on 12 November 2026 (`05` › Sightly's recommended monthly minimums).

For each platform in scope, compute the **monthly budget** that will land on that platform, at the budget as given, and compare it to the platform's **Gross** monthly minimum. Do not convert anything to net. If it falls below the minimum, you have three choices, in order of preference:

1. Recommend dropping the platform from the plan and reallocating to platforms that can be funded properly.
2. Recommend a higher total budget if the brief leaves room to negotiate.
3. Keep the platform in the plan **only if** there is a stated strategic reason (e.g., the client demanded it), and add a NOTES callout on every line item from that platform spelling out the consequence: insufficient delivery, inability to optimize, lack of statistical significance, etc.

This is the feasibility gate. Never silently plan below the floor — the callout is what matters.

Three more feasibility checks: **$100 a day per line item** is the practical floor for a line to deliver and optimize ($50 a day for underfunded local markets), so flag any line below it. A row marked "No floor documented" has no stateable floor: never quote one or borrow an adjacent row's figure, and say the plan's combined minimum has a priced and an unpriced portion. Platform-enforced minimums (for example TikTok's $20 per ad group per day) are hard stops; Sightly's recommended minimums are recommendations the strategist can run below once the flag is raised, confirmed case by case with the Account Management and Performance Management teams.

### Step A2 — Agency deal check

If the deal runs through MX (Horizon), Active or Agyle, apply the deal mechanics in `06_Media_Planning_Principles.md` › Agency deals: MX, Active and Agyle before pricing: the stacked-margin formula and the per-tactic eligibility check. The plan count depends on the arrangement. **MX:** one plan. Never produce an "MX discounted version" and never show the MX discount to the client; the answer to that request is "The MX discount is handled directly with the MX team, so the plan will be the same but will be MX eligible." An MX deal gets a second plan only for a reservation component, which needs its own IO and Salesforce opportunity. **Agyle:** two plans, because Agyle double-discounts and alters the data; don't carry that pattern into an MX deal. **Active:** the plan count isn't documented, so ask the strategist. Outside agency deals the default is also one plan (`06_Media_Planning_Principles.md` › When a second media plan is needed).

### Step B — Persona-level budget allocation

**The confirmed strategy sets the plan's structure, and it overrides this skill's defaults.** Before allocating anything, check the confirmed strategy (the `<brand>_insights_to_action_CONFIRMED.md` file, or the strategist's locked direction). If it specifies a single consolidated, auto-optimizing buy — one line that optimizes across inventory itself, with the personas rolling up inside it — then that is the plan: one fluid line per budget scenario, with no per-persona line items, no moments reserve, and no separate always-on line for a broad or catch-all audience. Do not split by persona, add a reserve, or add a catch-all line unless the brief or the confirmed strategy asks for it. The per-persona allocation below is the default only when the strategy leaves the structure open.

Read the persona list from the brief or from Step 5 of the RFP Workflow. The skill does **not** prescribe a default split — every campaign is different and the strategist owns the allocation decision.

**Before building any line items, resolve the allocation explicitly.** Ask the strategist one direct question: *do you have a target allocation across personas, or should I propose one?* This is not optional — even if the brief is detailed elsewhere, allocation is almost always something the strategist wants to own or confirm. Asking once up-front prevents the awkward situation of building a full CSV and having to redo it.

If the strategist asks you to propose: propose a specific split with the rationale tied to which persona is closest to conversion, where the cultural opportunity lives, and where the largest market opportunity is. Then confirm before writing line items.

If the strategist provides an allocation: honor it. Push back once only if it violates one of these guardrails:

- The **primary persona** — the one most aligned to the core business objective — should receive the largest share. If the strategist has the primary persona getting less than another persona, ask once whether that's intentional.
- A **moments reserve** is a discrete line only when the confirmed strategy calls for one. When the reactive component runs through a single consolidated auto-optimizing buy, the package leans into the moment itself and there is no reserve line (see the precedence note above). Where a reserve does apply, it fits a campaign with Brand Mentality data and a reactive cultural component; if neither applies, omit it.
- **Equal splits are a red flag.** If every persona ends up with the same allocation, surface this concern explicitly. Either the personas are not actually differentiated (a persona-development problem) or the allocation reflects default thinking. Do not silently ship an equal split — ask once.

Document the allocation in the narrative summary with the *why*, not just the *what*.

### Step C — Line-item build

For each persona, build the line items. Apply these rules:

**Every platform needs a purpose.** Awareness, consideration, conversion, retargeting, or cultural relevance. If you cannot articulate why a platform is in this persona's plan, do not add it.

**Every format needs a role.** Within a platform, do not run three video formats on the same audience unless each one is doing something distinct.

**Grade each format on a KPI it can move** (`06_Media_Planning_Principles.md` › KPI by format).

**No fantasy planning.** Real rates, real inventory, real targeting. If you do not have a confirmed rate for a placement, run `sightly-rate-recommender` and bring the strategist its evidence to decide on. What you never do is invent a number.

**The same rule covers audience size.** Any addressable-audience or reach figure that did not come from a platform, a Persona Builder run, or the strategist is your own estimate. Label it as an estimate at the point of use, and state any budget recommendation resting on it as contingent on that figure. A budget recommendation quietly built on a self-generated audience number is fantasy planning with a media plan wrapped around it.

**Caveat estimates where they're made.** Every line bought on dCPM (Demand Gen, for example) carries a NOTES caveat on how its impressions were estimated. Every reach figure is labeled a directional estimate.

**Check US YouTube audio before planning it.** US YouTube audio is in transition (`04_Platform_Reference.md`, read 20 October 2026): new US auction campaigns were blocked from 1 September 2026, existing ones were due to stop on 5 November 2026, and SiriusXM Media now sells YouTube audio in the US. The dates can move, so check Google's latest announcement every time a YouTube audio line comes up.

**One line per placement-persona pair**, unless the strategy calls for splitting by flight phase or geo. Consolidate device to "All Devices" on a single line unless the strategy specifically requires device-level breakouts (NOTES this rationale).

### Step D — Pressure-test pass

Once the lines are drafted, walk the table once more and look for:

- **Pacing / flight length** — is the flight long enough for each platform to exit its learning period? No learning-period length is documented in the knowledge base, so don't state one; flag a short flight as a risk and ask the strategist or the platform rep for the figure.
- **Saturation** — does any persona's frequency exposure risk burnout? Estimate reach and frequency per channel; Sightly doesn't deduplicate across channels. Google Reach Planner can't model contextual targeting (SmartLists), so for SmartLists lines apply the team's planning frequency of 3x per week: reach = impressions ÷ (3 × weeks in the flight). State the assumption and label the reach directional. Every frequency figure carries its time window; a frequency number without one means nothing.
- **Geo spread** — is the geo split too broad for the budget to land, or are larger markets getting equal weight to smaller ones? Larger markets should get more weight, not equal splits.
- **Reservation lead times** — use only the lead times the knowledge base documents (`05_Budget_Minimums_and_Feasibility.md` › Lead times). TikTok TopView, Pulse and Branded Effect: 2–4 weeks, and that figure applies to TikTok reservation products only. TopView's booking runway of up to 225 days is a booking window; it sets no lead time and says nothing about availability. YouTube reservation booking, Reddit takeovers, Spectrum Reach live sports and livestreaming have no documented lead time: say so in NOTES and route the question, never borrow another product's figure.
- **Learning periods on pulsed Demand Gen** — pulsing causes re-entry into learning. Flag and recommend always-on if applicable.

Every callout goes either in the line-item NOTES column (if it's local to one line) or in the narrative summary (if it's structural). Whenever the summary or a message points to a spreadsheet, name the tab and the column by its header and letter (for example, the `Plan` tab, column J `BUDGET`), never "the column".

**Minimums in an RFP answer.** When an RFP asks for "minimum spending requirements", answer with hard requirements only: platform-enforced minimums and anything set by Sightly contract or a partner. Sightly's recommended monthly minimums and the line-item floor are internal planning guidance, not client-facing minimums.

**Added value and lift.** Put the two default added-value items on every plan, Brand Mentality Platform Access and Brand Mentality Reporting; anything beyond them is a recommendation the strategist decides (`06_Media_Planning_Principles.md` › Added value). If the brief or the plan points to measurement, offer the lift-study feasibility read: Google checks its minimums against net spend, so convert the plan's gross spend in each study window to net at the deal's margin (net = gross × (1 − margin)), then compare the non-Demand-Gen net spend in any 10-day window (28 days for Search Lift) with the minimum buffered by 20–30%. Count only lines Brand Lift can measure: Video campaigns (skippable, non-skip, bumper, in-feed and Shorts); audio runs as its own audio-only study and can't be mixed with video; display and Performance Max can't be measured (`10_Brand_Lift_and_Measurement.md` › What Brand Lift can measure, and › Checking whether a plan can support a study).

## Math (this part is deterministic — get it right)

Pricing unit drives the math. **Auto-detect the unit from PLACEMENT TYPE** unless the strategist has specified otherwise:

| PLACEMENT TYPE | Default BILLING CPU |
|---|---|
| Video | CPV |
| Display | CPM |
| Native | CPM |
| Audio | CPM |
| Social (non-CTR formats) | CPM |
| Social (CTR-driven / conversion) | CPC |
| Search | CPC |
| Reservation / Influencer / Sponsorship | Flat |

If you're not sure, ask the strategist. Better to ask once than to ship the wrong unit.

### Estimated impressions

- **BILLING CPU = CPM**: `ESTIMATED IMPRESSIONS = (BUDGET / CPU) × 1000`
- **BILLING CPU = CPV**: `ESTIMATED IMPRESSIONS = ESTIMATED VIEWS / ESTIMATED VIEW RATE`
  - (You compute views first from BUDGET / CPU, then back into impressions.)
- **BILLING CPU = CPC**: do not estimate impressions; leave the column blank and put a NOTES entry that this is a click-driven buy.
- **BILLING CPU = Flat**: leave impressions blank unless the strategist provides a guaranteed delivery number.

### Estimated views (video only)

- **BILLING CPU = CPV**: `ESTIMATED VIEWS = BUDGET / CPU`
- **BILLING CPU = CPM and PLACEMENT TYPE = Video**: `ESTIMATED VIEWS = ESTIMATED IMPRESSIONS × ESTIMATED VIEW RATE`

### Estimated view rate (video only)

Source of truth, in priority order:

1. **Strategist-provided view rate** (in the brief or a follow-up). Always wins.
2. **A cited benchmark** — a signed-off Sightly benchmark, or the client's own benchmarks and history for the campaign (`06_Media_Planning_Principles.md` › KPI by format), with its source in NOTES. `04` and `12` carry no view-rate figures.
3. **Fallback reference**: `references/view_rate_benchmarks.md` — bundled with this skill, covers the major platforms and placements.
4. **Ask the strategist** if the placement isn't listed in any of the above. Do not invent a view rate.

**Non-skip and bumper lines carry no default VCR in plan math.** Leave ESTIMATED VIEW RATE blank and say so in NOTES unless the strategist supplies a campaign benchmark. Client-facing copy says "strong VCR" or "forced-view completion," never "guaranteed 100% VCR."

Note: the bundled benchmarks are for **upper-funnel awareness buys**. For lower-funnel conversion campaigns, expect view rates 5–10 percentage points lower because the algorithm trades completion for action signal — call this out in NOTES if it's relevant.

### Numeric cell formatting (critical)

The CSV is a working file the strategist will pivot, sum, and chart in Excel or Google Sheets. Cells in numeric columns must contain **pure numbers** — no currency symbols, no thousands separators, no percent signs. The strategist's spreadsheet applies the formatting.

- **CPU and BUDGET columns**: write `0.04`, `5.50`, `15000.00` — **never** `$0.04`, `$5.50`, `$15,000.00`. Dollar signs in a CSV cell break `SUM()` and `AVERAGE()`.
- **ESTIMATED IMPRESSIONS / ESTIMATED VIEWS**: whole numbers, no thousands separators. `1666667`, not `1,666,667`.
- **ESTIMATED VIEW RATE**: decimal between 0 and 1 — `0.27` for 27%, `0.12` for 12%. Not `27%`.
- **BILLING CPU**: a unit label string — `CPM`, `CPV`, `CPC`, or `Flat`.
- **Rounding**: dollar amounts to two decimal places; impressions and views to whole numbers; view rates to two decimal places (`0.27`, not `0.2734`).

## Voice and what to write in NOTES

Sightly's voice is direct, strategist-to-strategist. The NOTES column is not marketing copy — it's the field where the next planner or sales lead picks up the file and immediately understands what to do. Examples of good NOTES entries:

- `Below the TikTok monthly minimum ($3,500 gross), a Sightly recommendation: delivery and optimization at risk; confirm with Account Management and Performance Management.`
- `TikTok reservation: book at least 2–4 weeks before flight start (lead time per `05_Budget_Minimums_and_Feasibility.md`).`
- `YouTube reservation: lead time not documented; confirm with the Google team.`
- `Pulsed delivery will re-enter learning each cycle; recommend always-on.`
- `Sleep-Curious Parent retargeting depends on the Burned-Out Knowledge Worker awareness pixel firing; sequence required.`

Bad NOTES entries (do not write these):

- `This is a great placement!`
- `TBD`
- Anything that doesn't tell the next reader what to do or what to know.

## Narrative summary (accompanies the CSV)

Every plan ships with a short narrative — 4–8 sentences, no fluff — that covers:

1. The shape of the plan (which platforms, which personas, what total budget).
2. The allocation logic and **why** it lands where it does.
3. Any feasibility flags raised in Step A.
4. Any pressure-test callouts from Step D.
5. Open questions the strategist needs to resolve before this goes to client.

Plain prose. No bullet points unless there are genuinely three or more parallel callouts.

## Inputs the skill needs

Before building anything, confirm you have:

- **Total budget** — **the plan always sums to the budget the client gave. Never net it down, and don't ask whether it is net or gross** (`06_Media_Planning_Principles.md` › The budget convention). There is no 30% margin conversion in this skill. The rate is the lever, not the total: if feasibility fails, change the rate or the platform mix, never the budget. Run feasibility checks against the **Gross** column of `references/budget_minimums.md` (or `05_Budget_Minimums_and_Feasibility.md` if the knowledge base is available), at the budget as stated. The single exception is Google's Brand Lift and Search Lift thresholds, which are stated in net spend and checked with the knowledge base's 20–30% buffer, after converting the plan's spend in each window to net at the deal's margin (see "Added value and lift" in Step D). The CSV BUDGET column carries the client's dollars.
- **Flight dates** (start and end, ISO format preferred).
- **Geos / markets**.
- **Personas** — at least one. With names and brief descriptors.
- **Platforms** to include (or ask the strategist to confirm if the brief is open).
- **Rates** — a billing rate for every line, from the rate hierarchy: the deal's rate card, delivered rates from a comparable campaign, prior Sightly plans and the rate library (via `sightly-rate-recommender`, labeled as a baseline), then a cited external benchmark labeled as a comparison (Rule 17; `06_Media_Planning_Principles.md` › Where rates come from). The strategist confirms every rate. Never invent one.
- **Brand Mentality data** — Anticipation Board moments, SmartLists, BAV quadrant — if available.

If anything is missing, look for it in the brief, the email thread and the project before asking. Ask only questions whose answer changes what you do next. Ask them one at a time, in the session's ask-question widget where there is one, with each option explained. Never ask for a due date or a schedule to plan against.

## Output

Produce two files in the user's outputs folder:

1. **`<client>-media-plan-v<N>.csv`** — the canonical 14-column structure, one row per line item.
2. **`<client>-media-plan-v<N>-summary.md`** — the narrative summary.

Internal checks stay internal: feasibility flags, margin notes and red-cell markup go in the summary or a separate internal tab, never in the client file.

If the strategist will paste into Google Sheets, offer a version with formulas for impressions and views so the math can be checked.

If the user is working in a project context, prepend the client name from the brief. Otherwise use a sensible default like `media-plan-v1`.

## Worked examples

See `references/worked_example.md` for two full worked examples covering the math, allocation, and CSV output end-to-end.

## What this skill does not do

- It does not write deck copy. That's Step 9.
- It does not develop personas from scratch. That's Step 5 — this skill consumes the personas.
- It does not decide rates on its own. Every rate arrives confirmed by the strategist, whether they set it from scratch or accepted a baseline drawn from comparable prior plans by `sightly-rate-recommender`.
- It does not run the full QA review. Before handing the plan on, run the quick check before handover in `13_When_Asked_to_Build.md` › The check before handing it over and resolve any finding here; run `sightly-qa-gate`'s numbers-and-sources and feasibility gates as well when the strategist asks for them.

---

*End of Sightly Media Plan Builder skill.*
