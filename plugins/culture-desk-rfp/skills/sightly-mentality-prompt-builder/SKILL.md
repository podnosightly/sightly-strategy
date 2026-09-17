---
name: sightly-mentality-prompt-builder
description: UPDATED 17 September 2026 (v1.5.0) — rebuilt for the current Brand Mentality Agent, no listening-platform routing, with the full 8-point rigor preamble baked into every prompt. If you see more than one sightly-mentality-prompt-builder, this is the newest. Turns an RFP or research question into rigorous, ready-to-run prompts for Sightly's Brand Mentality Agent, and drives it to produce the reads, Insights/Highlights reports, signals, artifacts and visualizations an RFP needs. Use when asking the Mentality Agent for a read, designing a cultural/social/competitive pull, running an Insights or Highlights report, pulling signals, or turning a question into something executable. Triggers on "write a Mentality prompt", "brief the agent", "design the query", "what should I ask for", "spec this pull", "get me a read on X", "run an insights report", "pull signals". Not for interpreting results into strategy — that is sightly-insights-to-action.
---

# Sightly Mentality Agent — Operator & Prompt Builder

*Version 1.5.0 · Updated 17 September 2026 · rebuilt for the current Brand Mentality Agent (no listening-platform routing).*

This skill turns a research or RFP question into rigorous, executable work on Sightly's Brand Mentality Agent, and drives the agent to produce the actual outputs the RFP process needs: ad-hoc reads, Insights and Highlights reports, signals, audience targeting, HTML artifacts, and the visualizations inside them.

**The output of this skill is a prompt built to the standard in "The prompt construction standard" below — never a terse block.** If a prompt you produce is shorter or looser than the worked examples in this file, it is wrong. Match the bar.

**Source of truth for capabilities:** `mentality_capability_manual.md` — the full tool surface (its parameters, enums and bounds; a few enums such as the ~70 TikTok categories are browsed live in-tool), all limits, the visualization system, and the worked examples. Read it whenever you need a parameter, a bound, a per-source output-field list, or an example prompt.

## When to use / when not

**Use it** to: write what to paste into the Mentality Agent; design a cultural, social, competitive, or category pull; run an Insights Report or a Highlights Report; pull and explain signals; get per-platform audience targeting; build a persisted branded artifact; or decide whether a question is even answerable on the agent.

**Do not use it** to interpret results into strategy — brand pillars, positioning tension, personas, moment maps, the argument. That is `sightly-insights-to-action`; hand the agent's outputs to it. Slides are the deck builders. This skill acquires and produces; it does not synthesize strategy.

## The framing rule — read this first

The Brand Mentality Agent is a self-sufficient research instrument. It runs its own pulls end to end, within the window it can see. There is **no external "listening-platform" hand-off and no separate query spec** — that was the old, more limited agent; it is superseded. Two things govern everything below:

1. **The only hard limits worth memorizing are the ~1 January 2026 data floor and the enumerated coverage caps** (manual Part 6). Everything else the agent does itself, within that window.
2. **It will not fabricate** — its own constraint is that every number, chart and claim traces to a real tool result. So you get depth by asking real, fully-specified questions and making it show its counts, not by hedging the question in advance.

## The prompt construction standard — the bar every prompt meets

Every prompt this skill hands over is one block the strategist pastes whole into the Mentality Agent. It has two parts, and it is not finished until both are complete. **Never abbreviate the preamble. Never tell the strategist to "prepend" anything. Never ship a terse block.** Terseness is the failure mode; specificity is the product.

### Part A — the full 8-point rigor preamble (verbatim, in every prompt)

```
For this request, apply full research rigor:

1. EXHAUST THE TOOL SURFACE. Do not stop at one tool or one call. Run parallel
   calls across every applicable source: get_news_articles AND get_news_moments
   for press coverage and clustering; get_social_media_posts AND
   get_social_media_narratives for platform-level sentiment and clustering;
   get_trends for macro/longitudinal framing; get_tiktok_hashtags and
   get_youtube_videos/get_youtube_channels where the platform is relevant; and
   answer_from_web / search_web + read_web_pages + find_similar_pages for
   anything not covered above. Use multiple search_terms variations per call
   (up to 3) to widen recall, not just one obvious phrase.

2. REPORT STATISTICAL WEIGHT, NOT VIBES. Whenever a tool returns aggregate stats
   (include_total_statistics=true), surface the actual counts: total
   article/post volume, date distribution, platform/publisher mix, sentiment
   breakdown. State sample sizes explicitly (e.g. "47 articles across 12
   publishers, June 1-30"). If a data set is small or one-sided, say so instead
   of generalizing from it.

3. ZERO FABRICATION. Every fact, figure or quote must trace to a specific tool
   result with a citation - URL, publisher, date. If the tools return nothing on
   a sub-question, say "no data found" rather than filling the gap from general
   knowledge. Do not use background knowledge to complete a picture the data
   doesn't support; flag the gap.

4. SEPARATE DATA FROM INFERENCE. Present what the sources literally say first.
   Then, in a clearly marked section, give interpretation - labelled as
   inference, with the specific data points it rests on. Never blend the two into
   one unmarked narrative.

5. APPLY THE BRAND LENS THROUGHOUT. Filter every finding through the brand
   profile and name which dimension(s) it implicates. If the profile has gaps
   that limit the analysis, say so.

6. SHOW THE NARRATIVE ARC. Where timelines exist, describe the trajectory -
   rising, falling, plateauing - and whether sentiment is shifting. Call out
   inflection points with dates.

7. CROSS-VALIDATE. If news coverage and social sentiment diverge, or two search
   terms on the same topic return conflicting pictures, surface the conflict
   rather than silently picking a side.

8. RECOMMEND ACTION EXPLICITLY. Close with lean-in / lean-away / stay-informed /
   ignore per the Mentality framework, tied to the brand's risk tolerance and
   values. Flag it as a judgment call to own if it isn't clear-cut.
```

### Part B — the structured request (every element, every prompt)

Below the preamble, write the request with all of these. A prompt missing any one of them is not finished.

- **Brand context:** the Mentality brand profile name, the channels in scope, and the geo, in one line.
- **The task:** one sentence — the actual thing to map, find, or size.
- **Enumerated sub-questions or verticals:** numbered, so nothing is skipped, and so the output comes back structured the same way.
- **Per-item tool usage:** for each sub-question, name the exact tools and *how* to use them — the specific parameters that matter (e.g. `exclude_kids_content` to split buyable vs. made-for-kids; `get_trends` search-term based, not brand/person filters; both TikTok date buckets; `include_total_statistics` for aggregate counts).
- **Inline constraints that bite on this pull:** the ~2026-01-01 floor; the specific caps in play (YouTube 180-day stats window, TikTok 25 countries / four fixed buckets, trends top-10 filter); and the coverage caveats where they apply (social country tags on ~half of posts, share counts on ~a quarter, fullest enrichment only us/gb/ca/au/jp). State each where it applies, not in a preamble.
- **Decision this serves:** one line naming the RFP or campaign decision the pull feeds.
- **In the output, give:** an explicit field-level contract — total volume with its date window, the count of distinct channels/videos/authors behind it, a named number of real example URLs where relevant (e.g. "at least five real channel URLs and five real video URLs"), a split where the task needs one (buyable vs. kids, fandom vs. gift), and the denominator behind every percentage.

## Worked example — the bar

This is a real, complete prompt (Part A prepended, then Part B fully specified). Any prompt you produce should be at this level of specificity. The manual's Part 0 carries both worked examples.

```
[Part A — the full 8-point preamble above, verbatim]

Now the request:

Brand context: P&G Star Wars Crossover — a self-service campaign on YouTube,
TikTok, and programmatic in the United States.

Map the U.S. Star Wars content landscape and break it into targetable content
types, so I can build YouTube SmartLists and a segmentation model for the
campaign. Cover these four content verticals and tell me which are largest and
most active right now:
1. Film and series — the Mandalorian and Grogu movie, Star Wars: Starfighter, and
   current Disney+ Star Wars series.
2. Gaming — Star Wars video game launches, playthroughs, reviews, and streams.
3. Toys and collectibles — LEGO Star Wars sets, figure and collectible unboxings,
   hauls, and gift guides.
4. Fan community and news — theories, rankings, character deep-dives, cosplay, and
   franchise news.

For each vertical:
- Use get_youtube_channels and get_youtube_videos to return real, named channels
  and videos with subscriber and view counts and their most-recent-180-day
  statistics. Draw a clear line between content that is family, parent, reviewer,
  or adult-fan facing (which a brand can advertise against) and content flagged as
  made-for-kids (which cannot be monetized) — use exclude_kids_content to separate
  the two and report both sets.
- Use get_news_moments and get_social_media_narratives to size the conversation and
  its sentiment, and get_trends (search-term based) for the trajectory.

Only use data from 2026-01-01 onward. YouTube aggregate statistics only cover the
most recent 180 days; if you need older data, say so rather than estimating.

Decision this serves: choosing which Star Wars content types to include in the
SmartLists and how to segment them for the P&G self-service buy.

In the output, for every vertical give: the total volume with its date window, the
number of distinct channels and videos behind it, at least five real example
channel URLs and five real example video URLs a SmartList could use, and the
denominator behind every percentage.
```

## Workflow

### Step 1 — Frame the request
State the RFP or campaign decision this serves in one sentence, the brand profile, the channels, and the geo. If the brand has no Brand Profile, say so and use a stated category lens. **Thin-brief gate:** if a load-bearing input is missing — the decision the pull serves (and, for a report, the `intent`), the brand + geo, or a report's flight window — ask two or three targeted questions and get them before emitting anything. Never ship a prompt or form with placeholder or blank load-bearing fields; that breaks the paste-whole bar.

### Step 2 — Feasibility check (before writing)
Check against the floor and caps (manual Part 6). If any part needs data before ~1 January 2026, or past a hard cap, say **out of range** and adjust — never approximate across the floor, and never let the agent answer a question its tools can't reach. There is nothing to route elsewhere; there is only "in range" or "say it's out of range."

### Step 3 — Choose the output type
Match the need to the agent output, then build the prompt/form:

| RFP / research need | Agent output | Where |
|---|---|---|
| One targeted question | Ad-hoc multi-tool read | Prompt built to the standard above |
| Deep cultural discovery for the brief | **Insights Report** (`kind=INSIGHTS`) | Manual §3.1 |
| Client-facing signal one-pager (PDF) | **Highlights Report** (`kind=HIGHLIGHTS`) | Manual §3.2 |
| The brand's live signals + recommendations | `get_signals` / `get_signal_details` | Manual §2.7 |
| Per-platform audience targeting for a persona | `get_audience_targeting` | Manual §5.5 |
| A persisted, brand-styled deliverable | **HTML Artifact** | Manual §3.5 |
| Recurring performance numbers (spend/CPM/CTR) | **Reporting Job** (`kind=REPORTING`) | Manual §3.3 |
| Live targeting/blocking on connected platforms | **Activation Job** (`kind=ACTIVATION`) | Manual §3.4 |
| TikTok vernacular you don't know yet | `get_tiktok_hashtags` (discovery) | Manual §2.3 |
| Competitor territory | Competitor-seeded reads | Manual §2 |

Routing the two apart: a broad brand / competitor / culture **discovery** run — ranked signals, moments, planning — is the **Insights Report**; don't hand-assemble a parallel one. A **targeted acquisition** with a specific buyable output — seeding SmartList content types, one platform's landscape, a competitor territory scan — is an **ad-hoc read**, even when it "maps a landscape." (Worked example 1, content-type seeding, is an ad-hoc read for exactly that reason.)

### Step 4 — Build the prompt to the standard
Write Part A verbatim, then Part B with every element. For a report/job, fill the form fields from the manual and carry the same rigor into the `intent` field and the output expectations. **Always replace `<BRAND>` / profile name before handing it over** — a leftover placeholder is how the wrong brand enters a pull.

### Step 5 — Run and hold the output contract
Enforce what Part B asked for: every percentage with its denominator; every volume with its window; distinct-entity counts; real URLs; source on every figure; coverage caveats at the point of use; data and inference separated; "no data found" over a filled gap. State sample sizes; never dress a count up as significance.

### Step 6 — Visualizations
Describe the shape of the answer, not the component — "a ranked horizontal bar of theme volume," "the sentiment split as a donut with denominators" — and the agent renders it from real arrays. It won't draw data the tools didn't return. Full render set in manual Part 4.

### Step 7 — Hand off
Pass the agent's outputs to `sightly-insights-to-action` for strategy synthesis. Stop here; do not interpret.

## Hard limits (summary — full list in manual Part 6)

- **Data floor ~1 January 2026** across news, social, TikTok hashtags, trends. No year-over-year on the agent.
- **Coverage caps:** YouTube stats 180-day window (or drop stats for full history); TikTok 25 countries and four fixed date buckets; news 22 publisher countries; trends limited to the tracked top 10; social country tags on ~half of posts, shares on ~a quarter, fullest enrichment only us/gb/ca/au/jp.
- **Account:** 5 personas per brand; one persona per campaign per deal; one removal KPI and one timezone per deal-link call; brand-profile fields have hard character caps.
- **Jobs:** no live performance dashboard (Reporting Job only); Activation 1–24h; Highlights schedule 1–90 days, one-off ≤62 days; no in-place job edit, no changing a job's deal, no pause/resume/cancel from chat.
- **UI-only:** connect/disconnect platforms, switch brand, manage Team, pause/resume/cancel jobs, edit flight windows beyond the seeded default, resume a teammate's artifact session.
- **Always:** no fabrication, no image generation, no legal/financial/medical/tax advice, no cross-session memory beyond profiles/personas/deals.
