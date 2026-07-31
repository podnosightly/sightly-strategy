> **Correction note, read first.** The feasibility checks in these examples compare against the
> **NET** minimums, which is no longer how the gate runs. Feasibility now compares the budget as
> given against the **Gross** columns of `budget_minimums.md`, and nothing is converted to net. The
> method these examples demonstrate still holds; the specific minimum figures quoted in them do not.
> They have deliberately not been re-derived here, because changing them changes the worked
> conclusions, and that needs a strategist rather than a find-and-replace.

# Worked Examples — Sightly Media Plan Builder

Two end-to-end examples showing how the math, allocation, and CSV structure come together. Read these before building if you've never built a Sightly plan before.

---

## Example 1 — $50K monthly, 3 personas, YouTube + Meta + Display

### Brief (input)

- **Client:** A mid-market DTC sleep brand.
- **Budget:** $50,000 net per month, 90-day flight.
- **Flight:** 2026-06-01 to 2026-08-31.
- **Geos:** Top-10 US DMAs.
- **Personas (from Step 5):**
  - Persona 1 — Burned-Out Knowledge Worker (primary; closest to the conversion objective)
  - Persona 2 — Sleep-Curious Parent (secondary)
  - Persona 3 — Wellness Adjacent Gen Z (tertiary)
- **Platforms requested:** YouTube (auction), Meta, Programmatic Display via DV360.
- **Rates provided by strategist:**
  - YouTube In-Stream Skippable: $0.04 CPV
  - YouTube Bumper: $5.50 CPM
  - Meta Feed Video: $9.00 CPM
  - Meta Carousel: $1.20 CPC
  - DV360 Display: $4.50 CPM
- **View rates from Tactics Playbooks:**
  - YouTube In-Stream Skippable: 27%
  - Meta Feed Video: 20%

### Step A — Feasibility check

Per-platform net per month:
- YouTube — Tier 1 minimum: $2,450 net/mo ✓
- Meta — Tier 1 minimum: $3,500 net/mo ✓
- DV360 (Programmatic Display) — Tier 1 minimum: $2,450 net/mo ✓

All platforms clear the floor. No flags.

### Step B — Persona allocation

The skill proposes an allocation with rationale, the strategist confirms. For this brief:

- Persona 1 (Primary, conversion-proximate): $20,000 / mo
- Persona 2 (Secondary): $15,000 / mo
- Persona 3 (Tertiary): $10,000 / mo
- Moments reserve: $5,000 / mo

Rationale (goes in narrative summary): Persona 1 is closest to conversion intent and gets the largest share to reflect funnel proximity. Persona 2 carries the broadest reach opportunity (parents) and warrants more than the tertiary. Persona 3 is a longer-horizon culture play. Moments reserve held for Anticipation Board triggers around sleep/wellness cultural conversations (mid-summer heatwave coverage is on the board).

### Step C — Line items (CSV preview)

Note the formatting conventions: no dollar signs in CPU or BUDGET, view rate as decimal, Reserve as its own PLACEMENT TYPE at the bottom, TOTAL row at the end summing only BUDGET.

```
PLACEMENT TYPE,NETWORK,PLACEMENT,TARGET,FEATURES,START DATE,END DATE,BILLING CPU,CPU,BUDGET,ESTIMATED IMPRESSIONS,ESTIMATED VIEWS,ESTIMATED VIEW RATE,NOTES
Video,YouTube,In-Stream Skippable,Persona 1 — Burned-Out Knowledge Worker,Custom Intent + Affinity overlay; IAS standard,2026-06-01,2026-08-31,CPV,0.04,12000.00,1111111,300000,0.27,Primary persona — funnel-proximate; YouTube anchors awareness-to-consideration handoff.
Video,YouTube,Bumper,Persona 1 — Burned-Out Knowledge Worker,Frequency cap 3/wk per user,2026-06-01,2026-08-31,CPM,5.50,3000.00,545455,,,Bumper supports skippable for short-form recall; view-rate blank because bumpers do not have a comparable VTR.
Video,Meta,Feed Video,Persona 2 — Sleep-Curious Parent,Lookalike + interest stack; placement: Feed only,2026-06-01,2026-08-31,CPM,9.00,10000.00,1111111,222222,0.20,Secondary persona; Feed Video is the workhorse for parents.
Social,Meta,Carousel,Persona 2 — Sleep-Curious Parent,Product carousel; dynamic creative,2026-06-01,2026-08-31,CPC,1.20,5000.00,,,,Click-driven product showcase. Impressions left blank — CPC buy.
Display,DV360,Programmatic Display,Persona 3 — Wellness Adjacent Gen Z,Contextual + SmartList: wellness publishers,2026-06-01,2026-08-31,CPM,4.50,10000.00,2222222,,,Tertiary persona; contextual display for efficient reach. Pair with social retargeting in next iteration.
Reserve,DV360,Moments Reserve — Programmatic Display,All personas,Held for Anticipation Board triggers (mid-summer heatwave / sleep / wellness),2026-06-01,2026-08-31,CPM,4.50,5000.00,1111111,,,Activated reactively against sleep/wellness cultural moments per Brand Mentality board. Creative variants required by 2026-05-25.
TOTAL,,,,,,,,,45000.00,,,,
```

### Math walkthroughs (verifiable)

- YouTube In-Stream Skippable, $12,000 at $0.04 CPV:
  - Views = $12,000 / $0.04 = **300,000 views**
  - Impressions = 300,000 / 0.27 = **1,111,111 impressions**
- YouTube Bumper, $3,000 at $5.50 CPM:
  - Impressions = ($3,000 / $5.50) × 1000 = **545,455 impressions**
  - Bumpers don't have a view-rate in the same sense; leave VIEWS and VIEW RATE blank.
- Meta Feed Video, $10,000 at $9.00 CPM:
  - Impressions = ($10,000 / $9.00) × 1000 = **1,111,111 impressions**
  - Views = 1,111,111 × 0.20 = **222,222 views**
- Meta Carousel CPC: impressions blank, NOTES explains.
- DV360 Display, $10,000 at $4.50 CPM:
  - Impressions = ($10,000 / $4.50) × 1000 = **2,222,222 impressions**

### Step D — Pressure-test callouts

- Flight is 90 days — comfortable buffer past all learning periods. ✓
- 10-DMA geo split with $50K/mo lands sufficient weight in top-3 DMAs; smaller DMAs may underdeliver. Flag in narrative: consider concentrating to top-5 if delivery thins.
- Bumper + Skippable on same persona/platform is OK because formats serve distinct roles (recall vs. consideration).
- No reservation inventory — no lead-time risk.

### Narrative summary (output alongside CSV)

> 90-day, $150K total plan against three personas, anchored on YouTube + Meta with DV360 display rounding out reach. Persona 1 gets 40% as the conversion-proximate audience; secondary and tertiary scale down by funnel role. 10% moments reserve sits in DV360 to activate against the Anticipation Board's mid-summer sleep/wellness conversations.
>
> All platforms clear Tier 1 net minimums. No feasibility flags.
>
> One pressure-test callout: the 10-DMA spread thins delivery in lower-ranked markets. Recommend concentrating to top-5 DMAs if Week-2 delivery reports show under-pacing.
>
> Open question for strategist: confirm Persona 3 contextual SmartList is current — the wellness publisher list was last refreshed in Q1.

---

## Example 2 — $4K monthly, 1 persona, TikTok-only (UNDERFUNDED)

### Brief (input)

- **Client:** Small CPG brand testing TikTok.
- **Budget:** $4,000 net per month, 30-day flight.
- **Flight:** 2026-07-01 to 2026-07-30.
- **Geo:** US national.
- **Personas:** Persona 1 — Gen Z Snack Seeker.
- **Platforms requested:** TikTok only.
- **Rates provided:** TikTok In-Feed Video: $8.00 CPM, view rate (from Tactics Playbook 14): 12%.

### Step A — Feasibility check

TikTok Tier 1 minimum: $2,450 net/mo. $4,000 clears that. ✓

But the brief is testing TikTok specifically and 30 days is **at the edge** of the learning period. Flag in NOTES and narrative: 30-day flight risks exiting only just after learning stabilizes; delivery in Week 1 will be inefficient.

If the client had requested Tier 2 conversion optimization, the Tier 2 minimum jumps to $5,250 net/mo — this budget would be **below** that floor. Make sure the strategist confirms the campaign is upper-funnel (Tier 1), not conversion (Tier 2).

### Step B — Persona allocation

Single persona, so 100% goes to Persona 1. No moments reserve unless Brand Mentality data supports it (the brief doesn't reference any).

### Step C — Line items

```
PLACEMENT TYPE,NETWORK,PLACEMENT,TARGET,FEATURES,START DATE,END DATE,BILLING CPU,CPU,BUDGET,ESTIMATED IMPRESSIONS,ESTIMATED VIEWS,ESTIMATED VIEW RATE,NOTES
Video,TikTok,In-Feed Video,Persona 1 — Gen Z Snack Seeker,Interest stack + creator content; sound-on optimization,2026-07-01,2026-07-30,CPM,8.00,4000.00,500000,60000,0.12,30-day flight is at the edge of learning period (~7–14 days). Week 1 delivery will be inefficient. Confirm Tier 1 (awareness) framing — Tier 2 conversion at this budget would fall below the $5,250 net/mo minimum.
TOTAL,,,,,,,,,4000.00,,,,
```

Math:
- Impressions = (4000 / 8.00) × 1000 = 500,000
- Views = 500,000 × 0.12 = 60,000

### Step D — Pressure-test callouts

- Flight length flagged at the line level. Surfaced in narrative.
- Single-platform single-persona plan has no diversification — note this is a test-and-learn posture, not a scaled buy.

### Narrative summary

> Single-platform TikTok test, $4K net over 30 days against one Gen Z persona. The budget clears the Tier 1 (awareness) minimum but does not support Tier 2 (conversion) optimization at $5,250/mo.
>
> Flight length is the primary risk: 30 days is at the edge of TikTok's learning period. Expect inefficient Week 1 delivery; assess on Week 2 numbers, not Week 1.
>
> Open question for strategist: confirm this is a Tier 1 awareness test, not a conversion campaign. If the client expects conversion outcomes at this budget, recommend either (a) extending the flight to 60 days, or (b) raising budget to $5,250+ net/mo.

---

*End of worked examples.*
