# Worked Examples — Sightly Media Plan Builder

Two end-to-end examples showing how the math, allocation, and CSV structure come together. Read these before building if you've never built a Sightly plan before. Both follow the current rules: the plan sums to the client's budget as given, we check feasibility against the **Gross** monthly minimums at that budget (one list; the tiers are retired), every rate follows the rate hierarchy and is confirmed by the strategist, and the view rates here are supplied by the strategist.

---

## Example 1: $150,000 over three months (92 days), 3 personas, YouTube + Meta + Display

### Brief (input)

- **Client:** A mid-market DTC sleep brand.
- **Budget:** $150,000 gross for the 92-day flight ($50,000 a month).
- **Flight:** 2026-06-01 to 2026-08-31.
- **Geos:** Top-10 US DMAs.
- **Personas (from Step 5):**
  - Burned-Out Knowledge Worker (primary; closest to the conversion objective)
  - Sleep-Curious Parent (secondary)
  - Wellness Adjacent Gen Z (tertiary)
- **Platforms requested:** YouTube (auction), Meta, Programmatic Display via DV360.
- **Rates provided by the strategist:**
  - YouTube In-Stream Skippable: $0.04 CPV
  - YouTube Bumper: $5.50 CPM
  - Meta Feed Video: $9.00 CPM
  - Meta Carousel: $1.20 CPC
  - DV360 Display: $4.50 CPM
- **View rates provided by the strategist for this example:** skippable 0.27, Meta Feed Video 0.20.

### Step A — Feasibility check

Monthly budget per platform against the **gross** monthly minimum:
- YouTube: $20,000 a month vs. $3,500 ✓
- Meta: $15,000 a month vs. $5,000 ✓
- DV360 (Programmatic Display, including the moments reserve): $15,000 a month vs. $3,500 ✓

All platforms clear their gross monthly minimums. Every line also clears the $100-a-day line floor: we run the smallest line, the $12,000 bumper, at about $130 a day over the 92 days from 1 June to 31 August. No flags.

### Step B — Persona allocation

The skill proposes an allocation with rationale, the strategist confirms. Flight totals for this brief:

- Burned-Out Knowledge Worker (primary, conversion-proximate): $60,000 (40%)
- Sleep-Curious Parent (secondary): $45,000 (30%)
- Wellness Adjacent Gen Z (tertiary): $30,000 (20%)
- Moments reserve: $15,000 (10%)

Rationale (goes in narrative summary): Burned-Out Knowledge Worker is closest to conversion intent and gets the largest share to reflect funnel proximity. Sleep-Curious Parent carries the broadest reach opportunity and warrants more than the tertiary. Wellness Adjacent Gen Z is a longer-horizon culture play. We hold the moments reserve for Anticipation Board triggers around sleep and wellness conversations (mid-summer heatwave coverage is on the board).

### Step C — Line items (CSV preview)

Note the formatting conventions: BILLING CPU holds the pricing unit, CPU holds the rate, no dollar signs in CPU or BUDGET, view rate as decimal, Reserve as its own PLACEMENT TYPE at the bottom, TOTAL row at the end summing only BUDGET. The lines sum to the $150,000 budget, and each persona's lines sum to its allocation.

```
PLACEMENT TYPE,NETWORK,PLACEMENT,TARGET,FEATURES,START DATE,END DATE,BILLING CPU,CPU,BUDGET,ESTIMATED IMPRESSIONS,ESTIMATED VIEWS,ESTIMATED VIEW RATE,NOTES
Video,YouTube,In-Stream Skippable,Burned-Out Knowledge Worker,Custom Intent + Affinity overlay,2026-06-01,2026-08-31,CPV,0.04,48000.00,4444444,1200000,0.27,Primary persona. View rate supplied by strategist.
Video,YouTube,Bumper,Burned-Out Knowledge Worker,Frequency cap 3/wk per user,2026-06-01,2026-08-31,CPM,5.50,12000.00,2181818,,,No default view rate for bumpers.
Video,Meta,Feed Video,Sleep-Curious Parent,Lookalike + interest stack; Feed only,2026-06-01,2026-08-31,CPM,9.00,30000.00,3333333,666667,0.20,Secondary persona. View rate supplied by strategist.
Social,Meta,Carousel,Sleep-Curious Parent,Product carousel; standard creative,2026-06-01,2026-08-31,CPC,1.20,15000.00,,,,Click-driven buy; impressions not estimated.
Display,DV360,Programmatic Display,Wellness Adjacent Gen Z,Contextual + SmartList: wellness publishers,2026-06-01,2026-08-31,CPM,4.50,30000.00,6666667,,,Tertiary persona; contextual display for efficient reach.
Reserve,DV360,Moments Reserve — Programmatic Display,All personas,Anticipation Board triggers (heatwave / sleep / wellness),2026-06-01,2026-08-31,CPM,4.50,15000.00,3333333,,,Activated reactively; creative variants required by 2026-05-25 (assumed date).
TOTAL,,,,,,,,,150000.00,,,,
```

### Math walkthroughs (verifiable)

- YouTube In-Stream Skippable, $48,000 at $0.04 CPV:
  - Views = $48,000 / $0.04 = **1,200,000 views**
  - Impressions = 1,200,000 / 0.27 = **4,444,444 impressions**
- YouTube Bumper, $12,000 at $5.50 CPM:
  - Impressions = ($12,000 / $5.50) × 1000 = **2,181,818 impressions**
  - Bumpers carry no default view rate; leave VIEWS and VIEW RATE blank.
- Meta Feed Video, $30,000 at $9.00 CPM:
  - Impressions = ($30,000 / $9.00) × 1000 = **3,333,333 impressions**
  - Views = 3,333,333 × 0.20 = **666,667 views**
- Meta Carousel CPC: impressions blank, NOTES explains.
- DV360 Display, $30,000 at $4.50 CPM:
  - Impressions = ($30,000 / $4.50) × 1000 = **6,666,667 impressions**
- Moments reserve, $15,000 at $4.50 CPM:
  - Impressions = ($15,000 / $4.50) × 1000 = **3,333,333 impressions**
- Budget check: 48,000 + 12,000 + 30,000 + 15,000 + 30,000 + 15,000 = **150,000**.

### Step D — Pressure-test callouts

- Flight is 92 days, long enough that we raise no flight-length risk. ✓
- At $50,000 a month across 10 DMAs we land sufficient weight in the top-3 DMAs; smaller DMAs may underdeliver. Flag in narrative: consider concentrating to top-5 if delivery thins.
- Bumper + Skippable on the same persona and platform is OK because the formats serve distinct roles (recall vs. consideration).
- No reservation inventory, so no lead-time risk.

### Narrative summary (output alongside CSV)

> 92-day, $150,000 plan against three personas, anchored on YouTube + Meta with DV360 display rounding out reach. Burned-Out Knowledge Worker gets 40% as the conversion-proximate audience; secondary and tertiary scale down by funnel role. We hold a 10% moments reserve in DV360 to activate against the Anticipation Board's mid-summer sleep and wellness conversations.
>
> All platforms clear their gross monthly minimums. No feasibility flags.
>
> One pressure-test callout: the 10-DMA spread thins delivery in lower-ranked markets. Recommend concentrating to top-5 DMAs if Week-2 delivery reports show under-pacing.
>
> Open question for strategist: confirm the Wellness Adjacent Gen Z contextual SmartList is current; the wellness publisher list was last refreshed in Q1.

---

## Example 2: $4,000 over 30 days, 1 persona, TikTok-only

### Brief (input)

- **Client:** Small CPG brand testing TikTok.
- **Budget:** $4,000 gross for a 30-day flight.
- **Flight:** 2026-07-01 to 2026-07-30.
- **Geo:** US national.
- **Personas:** Gen Z Snack Seeker.
- **Platforms requested:** TikTok only.
- **Rates provided:** TikTok In-Feed Video: $8.00 CPM; view rate 0.12, supplied by the strategist.

### Step A — Feasibility check

TikTok gross monthly minimum: $3,500 (`05`, one list since 12 November 2026). At $4,000 a month we clear it. ✓

We run the line at about $133 a day, above the $100-a-day line floor.

The brief is testing TikTok over 30 days. No learning-period length is documented in the knowledge base, so we flag the short flight as a risk in NOTES and the narrative and ask the strategist whether the test can run longer.

### Step B — Persona allocation

Single persona, so 100% goes to Gen Z Snack Seeker. No moments reserve unless Brand Mentality data supports it (the brief doesn't reference any).

### Step C — Line items

```
PLACEMENT TYPE,NETWORK,PLACEMENT,TARGET,FEATURES,START DATE,END DATE,BILLING CPU,CPU,BUDGET,ESTIMATED IMPRESSIONS,ESTIMATED VIEWS,ESTIMATED VIEW RATE,NOTES
Video,TikTok,In-Feed Video,Gen Z Snack Seeker,Interest stack + creator content,2026-07-01,2026-07-30,CPM,8.00,4000.00,500000,60000,0.12,"30-day test flight: no learning-period length is documented, so the short flight is flagged as a risk. Clears the $3,500 gross TikTok monthly minimum."
TOTAL,,,,,,,,,4000.00,,,,
```

Math:
- Impressions = (4000 / 8.00) × 1000 = 500,000
- Views = 500,000 × 0.12 = 60,000

### Step D — Pressure-test callouts

- Flight length flagged at the line level. Surfaced in narrative.
- A single-platform, single-persona plan has no diversification; note that this is a test-and-learn posture.

### Narrative summary

> Single-platform TikTok test, $4,000 over 30 days against one Gen Z persona. At $4,000 we clear TikTok's gross monthly minimum of $3,500 and run the line at about $133 a day, above the $100-a-day line floor.
>
> Flight length is the main risk: in 30 days we have little time to optimize, and since no learning-period length is documented, we don't state one.
>
> Open question for strategist: can the test run longer? If the client expects conversion outcomes, we would recommend extending the flight to 60 days at $4,000 a month ($8,000 total) so TikTok has more time to optimize.

---

*End of worked examples.*
