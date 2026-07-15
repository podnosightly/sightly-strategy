---
name: sightly-media-plan-builder
description: Builds Sightly Standard Media Plan tables as CSVs from a strategist's brief. Walks through the full RFP Step 7 workflow — feasibility check against budget minimums, persona-level budget allocation, line-item construction in the canonical 14-column structure, and pressure-test callouts (pacing, learning periods, geo spread, saturation). Use whenever the user mentions building a media plan, tactics table, line items, budget allocation across platforms or personas, "Step 7", or asks to turn a brief into a plan. Triggers on requests like "build me a media plan", "draft the tactics table", "allocate this budget across personas", "turn this brief into a plan", "build the Sightly Standard output", "feasibility check this budget", or any mention of campaign line items with platforms, flight dates, and rates.
---

# Sightly Media Plan Builder

## What this skill does

This skill turns a Sightly brief into a CSV media plan that conforms to the **Sightly Standard Media Plan Output** column structure. It runs the four substeps of Step 7 of the RFP Workflow in order:

1. **Feasibility check** against `references/budget_minimums.md` (or `09_Budget_Minimums.md` if available in the working directory) — flag any platform underfunded for its tier.
2. **Persona-level budget allocation** — split the budget by strategic weight, not evenly.
3. **Line-item build** in the canonical column structure, with deterministic math.
4. **Pressure-test pass** — flag pacing, learning periods, geo spread, saturation, timing risks.

The deliverable is a CSV the strategist drops into a working spreadsheet or deck. A short narrative summary accompanies the file: what the plan does, what was flagged, and which decisions still need strategist confirmation.

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
- **TARGET**: which persona this line item serves. Use the persona's working name (e.g., "Persona 1 — Hopeful Renter").
- **FEATURES**: targeting features, format specs, special capabilities — Anticipation Board moments, SmartLists, BAV quadrant alignment, custom intent, IAS categories applied at line-item level.
- **START DATE**, **END DATE**: flight dates in ISO format (`YYYY-MM-DD`).
- **BILLING CPU**: the **pricing unit label** — `CPM`, `CPV`, `CPC`, or `Flat`. Not a dollar amount.
- **CPU**: the **dollar amount** per unit. E.g., `$5.00` for a $5 CPM, `$0.04` for a $0.04 CPV.
- **BUDGET**: dollar amount allocated to this line.
- **ESTIMATED IMPRESSIONS**: see Math section below.
- **ESTIMATED VIEWS**: video lines only; otherwise leave blank.
- **ESTIMATED VIEW RATE**: video lines only; pulled from the relevant Tactics Playbook.
- **NOTES**: caveats, callouts, dependencies, reservations needed, anything the strategist or sales lead must know about this line.

Additional fields that may belong as columns or in NOTES depending on plan complexity: **Site Served**, **IAS Blocking**, **Device** (default to "All Devices" unless device-level breakouts are part of the strategy). When unsure, put them in NOTES.

### Moments reserve representation

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

## The four-step workflow

### Step A — Feasibility check (always first)

Before touching any line items, validate that the budget can fund what the brief calls for. Read `references/budget_minimums.md` (or `09_Budget_Minimums.md` if available in the working directory) and identify the relevant tier for each platform proposed:

- **Tier 1**: upper-funnel standard formats, or high-priority account.
- **Tier 2**: lower-funnel, conversion, dynamic, or influencer; or a standard account.
- **Tier 3**: hyper-localized, 4+ personas (multiple cut minimums).

For each platform in scope, compute the **monthly net budget** that will land on that platform and compare it to the minimum for its tier. If it falls below the minimum, you have three choices, in order of preference:

1. Recommend dropping the platform from the plan and reallocating to platforms that can be funded properly.
2. Recommend a higher total budget if the brief leaves room to negotiate.
3. Keep the platform in the plan **only if** there is a stated strategic reason (e.g., the client demanded it), and add a NOTES callout on every line item from that platform spelling out the consequence: insufficient delivery, inability to optimize, lack of statistical significance, etc.

This is the feasibility gate. Never silently plan below the floor — the callout is what matters.

### Step B — Persona-level budget allocation

Read the persona list from the brief or from Step 5 of the RFP Workflow. The skill does **not** prescribe a default split — every campaign is different and the strategist owns the allocation decision.

**Before building any line items, resolve the allocation explicitly.** Ask the strategist one direct question: *do you have a target allocation across personas, or should I propose one?* This is not optional — even if the brief is detailed elsewhere, allocation is almost always something the strategist wants to own or confirm. Asking once up-front prevents the awkward situation of building a full CSV and having to redo it.

If the strategist asks you to propose: propose a specific split with the rationale tied to which persona is closest to conversion, where the cultural opportunity lives, and where the largest market opportunity is. Then confirm before writing line items.

If the strategist provides an allocation: honor it. Push back once only if it violates one of these guardrails:

- The **primary persona** — the one most aligned to the core business objective — should receive the largest share. If the strategist has the primary persona getting less than another persona, ask once whether that's intentional.
- A **moments reserve** is appropriate when Brand Mentality data exists and the campaign has a reactive cultural component. If neither applies, omit it.
- **Equal splits are a red flag.** If every persona ends up with the same allocation, surface this concern explicitly. Either the personas are not actually differentiated (a persona-development problem) or the allocation reflects default thinking. Do not silently ship an equal split — ask once.

Document the allocation in the narrative summary with the *why*, not just the *what*.

### Step C — Line-item build

For each persona, build the line items. Apply these rules:

**Every platform needs a purpose.** Awareness, consideration, conversion, retargeting, or cultural relevance. If you cannot articulate why a platform is in this persona's plan, do not add it.

**Every format needs a role.** Within a platform, do not run three video formats on the same audience unless each one is doing something distinct.

**No fantasy planning.** Real rates, real inventory, real targeting. If you do not have a confirmed rate for a placement, ask the strategist before building the line. Do not assume CPMs/CPVs/CPCs.

**One line per placement-persona pair**, unless the strategy calls for splitting by flight phase or geo. Consolidate device to "All Devices" on a single line unless the strategy specifically requires device-level breakouts (NOTES this rationale).

### Step D — Pressure-test pass

Once the lines are drafted, walk the table once more and look for:

- **Pacing / flight length** — is the flight long enough for each platform to exit its learning period? Demand Gen learning is ~7 days; Meta/TikTok ~7–14 days. Flag any flight under 14 days on those platforms.
- **Saturation** — does any persona's frequency exposure risk burnout? Flag if reach × frequency math gets uncomfortable.
- **Geo spread** — is the geo split too broad for the budget to land, or are larger markets getting equal weight to smaller ones? Larger markets should get more weight, not equal splits.
- **Reservation lead times** — TopView, TikTok Pulse, Branded Effect need 2–4 weeks; TopView itself can be up to 225 days. Flag in NOTES if any reservation inventory is on the table.
- **Learning periods on pulsed Demand Gen** — pulsing causes re-entry into learning. Flag and recommend always-on if applicable.

Every callout goes either in the line-item NOTES column (if it's local to one line) or in the narrative summary (if it's structural).

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
2. **Platform-specific Tactics Playbook** if available in the working directory:
   - YouTube → `13_Tactics_Playbook_YouTube.md`
   - TikTok → `14_Tactics_Playbook_TikTok.md`
   - Reddit → `15_Tactics_Playbook_Reddit.md`
   - CTV → `16_Tactics_Playbook_CTV.md`
   - Meta → `17_Tactics_Playbook_Meta.md`
   - Spotify → `18_Tactics_Playbook_Spotify.md`
   - Pinterest → `22_Tactics_Playbook_Pinterest.md`
3. **Fallback reference**: `references/view_rate_benchmarks.md` — bundled with this skill, covers the major platforms and placements.
4. **Ask the strategist** if the placement isn't listed in any of the above. Do not invent a view rate.

Note: the bundled benchmarks are for **upper-funnel awareness buys**. For Tier 2 conversion campaigns, expect view rates 5–10 percentage points lower because the algorithm trades completion for action signal — call this out in NOTES if it's relevant.

### Numeric cell formatting (critical)

The CSV is a working file the strategist will pivot, sum, and chart in Excel or Google Sheets. Cells in numeric columns must contain **pure numbers** — no currency symbols, no thousands separators, no percent signs. The strategist's spreadsheet applies the formatting.

- **CPU and BUDGET columns**: write `0.04`, `5.50`, `15000.00` — **never** `$0.04`, `$5.50`, `$15,000.00`. Dollar signs in a CSV cell break `SUM()` and `AVERAGE()`.
- **ESTIMATED IMPRESSIONS / ESTIMATED VIEWS**: whole numbers, no thousands separators. `1666667`, not `1,666,667`.
- **ESTIMATED VIEW RATE**: decimal between 0 and 1 — `0.27` for 27%, `0.12` for 12%. Not `27%`.
- **BILLING CPU**: a unit label string — `CPM`, `CPV`, `CPC`, or `Flat`.
- **Rounding**: dollar amounts to two decimal places; impressions and views to whole numbers; view rates to two decimal places (`0.27`, not `0.2734`).

## Voice and what to write in NOTES

Sightly's voice is direct, strategist-to-strategist. The NOTES column is not marketing copy — it's the field where the next planner or sales lead picks up the file and immediately understands what to do. Examples of good NOTES entries:

- `Below Tier 2 minimum ($7,500). Insufficient for optimization beyond first 2 weeks.`
- `Requires advance reservation; book 2–4 weeks before flight start.`
- `Pulsed delivery will re-enter learning each cycle; recommend always-on.`
- `Persona 2 retargeting depends on Persona 1 awareness pixel firing; sequence required.`

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

- **Total budget** — and **explicitly ask whether it is net or gross** on every build. If gross, apply Sightly's 30% margin to derive net before running feasibility checks against `references/budget_minimums.md` (or `09_Budget_Minimums.md` if available in the working directory) (those minimums are stated in both net and gross). The CSV BUDGET column is always in net dollars unless the strategist requests otherwise; if so, note this in the summary.
- **Flight dates** (start and end, ISO format preferred).
- **Geos / markets**.
- **Personas** — at least one. With names and brief descriptors.
- **Platforms** to include (or ask the strategist to confirm if the brief is open).
- **Rates** — CPU for every platform/placement. **Rates are always provided by the strategist.** Never assume.
- **Brand Mentality data** — Anticipation Board moments, SmartLists, BAV quadrant — if available.

If anything is missing, ask before building. Ask in batches (two-to-three clarifying questions max in one go), not one at a time.

## Output

Produce two files in the user's outputs folder:

1. **`<client>-media-plan-v<N>.csv`** — the canonical 14-column structure, one row per line item.
2. **`<client>-media-plan-v<N>-summary.md`** — the narrative summary.

If the user is working in a project context, prepend the client name from the brief. Otherwise use a sensible default like `media-plan-v1`.

## Worked examples

See `references/worked_example.md` for two full worked examples covering the math, allocation, and CSV output end-to-end.

## What this skill does not do

- It does not write deck copy. That's Step 9.
- It does not develop personas from scratch. That's Step 5 — this skill consumes the personas.
- It does not pull rates from prior campaigns. The Rate Policy is explicit: rates are always provided by the strategist for the current build.
- It does not run QA. That's `12_QA_Framework.md`. If asked to QA after building, run the 5-gate framework separately.

---

*End of Sightly Media Plan Builder skill.*
