# Brand Mentality® Agent — Operating Manual & Prompt Library

*For Dan Podnos / Sightly strategy team. Rebuilt 16 September 2026 from the agent's own capability audit; Execution Protocol (breadth + depth enforcement) added 17 September 2026 — skill v1.6.0.*

**Source of truth.** Everything here comes from your capability audit — the agent describing its own live tool surface. Sightly's older knowledge-base docs describe an earlier, more limited agent; where they and your audit disagree, your audit wins and this manual follows it. The agent runs its own research pulls end to end, within the window it can see — there is no external hand-off step. This manual assumes the current agent, not the old one.

**How to read it.** Two markers only, and both come straight from the audit:

- **Agent runs this** — you can prompt the agent to do it in chat.
- **UI-only** — a real feature, but the agent has no tool for it. You do it in the app; asking the agent won't work. Knowing these is half the point of the manual.

**How to use the prompts.** The authoritative, paste-whole standard is **Part 0** (the Execution Protocol + the full 8-point preamble + all Part B elements); Worked example 1 there is a complete prompt to model. The shorter blocks in Parts 1–5 are the capability reference and scaffolds — assemble the real prompt to the Part 0 standard rather than pasting them as-is, and note that the report, job and ops blocks in Parts 3 and 5 are forms filled per their fields. One warning: replace `<BRAND>` before you paste — a leftover `<BRAND>` is how the wrong brand ends up in a pull.

**The one framing rule.** The agent is a self-sufficient research instrument. The only hard limits worth memorizing are the ~1 January 2026 data floor and the enumerated coverage caps in Part 6. It will not fabricate — its own constraint is that every number, chart and claim traces to a real tool result — so the way to get depth is to ask real questions and make it show its counts, not to hedge the question in advance. Breadth is a separate discipline: the agent under-searches by default, so the **Execution Protocol (Part 0, Part A0)** forces the full tool sweep, a six-variation term floor, full-body reads, and a coverage self-audit before it can conclude — that is how you stop it answering a landscape question with one thin pull.

---

## PART 0 — THE PROMPT STANDARD (AUTHORITATIVE)

Every **research prompt** handed to the Mentality Agent is built like this and pasted whole. **This standard supersedes the shorter blocks in Parts 1–5** — treat those as scaffolds. A research read expands to this full standard (the Execution Protocol + 8-point preamble + all Part B elements) before running; the report, job and ops blocks in Parts 3 and 5 are **forms**, not research reads — fill their fields and carry the rigor into the `intent` / config, they do not take the research preamble. Terseness is the failure mode; specificity is the product.

**Why Part A0 exists.** The 8-point preamble *asks* the agent to "exhaust the tool surface," but an aspiration has no forcing function — left to itself the agent runs one narrow query, skips tools like `get_news_moments`, reads snippets instead of full bodies, and reports thin results as a finding instead of widening. Part A0 converts the aspiration into procedure: a tool-sweep checklist, a six-variation term floor, a full-body read rule, a thin-is-a-trigger stopping rule, and a coverage self-audit the agent must print before it is allowed to conclude. It sits at the top of every research prompt, above Part A.

**Part A0 — the Execution Protocol, verbatim, at the top of every prompt:**

```
EXECUTION PROTOCOL — run all of this. It is procedure, not suggestion.

- RUN THE FULL SWEEP (a checklist, not a vibe). Before searching, list every tool
  that could bear on this question and commit to calling each; you account for all
  of them in the self-audit at the end. Start broad, then narrow — open with wide
  framings to survey the landscape before drilling into specifics. Unless a tool is
  genuinely irrelevant (and you say why), you call: get_news_articles AND
  get_news_moments (moments cluster stories articles scatter; run both sort_by=size
  and sort_by=recency); get_social_media_posts AND get_social_media_narratives,
  pulled PER PLATFORM, not five platforms lumped into one call; get_trends for the
  macro shape; get_tiktok_hashtags to DISCOVER the vernacular (feeds the term rule
  below); get_youtube_videos / get_youtube_channels where a creator/content
  landscape is in scope; and search_web + read_web_pages + find_similar_pages +
  answer_from_web for anything the above don't reach. One tool or one call is not a
  search. A tool you did not call is a gap to report, not a step to skip.

- VARY THE TERMS (a floor of six, not a ceiling of one). A single obvious phrase
  misses most of the conversation, because people don't all use your words. Per
  sub-question, run AT LEAST SIX term variations spanning: (a) the literal term;
  (b) synonyms and alternate phrasings; (c) the community/vernacular term people
  actually use — discover it with get_tiktok_hashtags, don't guess it; (d) proper
  nouns / entities involved (people, titles, events, brands); (e) the adjacent or
  umbrella category; (f) the critic or backlash framing, so you capture the whole
  conversation and not only the flattering half. A single call caps at 3
  search_terms, so this is several calls per tool. That is expected.

- READ FULL BODIES BEFORE YOU QUOTE OR CHARACTERIZE. Snippets truncate at ~2,000
  characters and drop the specifics. On the top items, pull the full article body
  (the full-content option on get_news_articles) and run read_web_pages on the
  actual URLs for verbatim quotes and named detail. Never quote or characterize a
  specific claim from a snippet alone.

- THIN IS A TRIGGER, NOT A FINDING. Do not call a topic small, limited, quiet or
  absent until the recall floor is met: every applicable tool called, six+ term
  variations across two+ tools, full bodies read on the top items, and at least one
  reformulation using vernacular found in the data. "Limited results" means widen
  and re-run. Only after the floor is met may you report thinness — and then as a
  stated coverage limit naming the terms and tools you tried, never as a conclusion
  about the world.

- CLOSE WITH A COVERAGE SELF-AUDIT. Before any findings, print this table, one row
  per tool. No conclusions until it is complete:
    | Tool | Called? | Terms / params used | Volume returned | Gap or next step |
    | get_news_articles | | | | |
    | get_news_moments | | | | |
    | get_social_media_posts | | | | |
    | get_social_media_narratives | | | | |
    | get_trends | | | | |
    | get_tiktok_hashtags | | | | |
    | get_youtube_videos / channels | | | | |
    | open web (search / read) | | | | |
  Any row empty or thin: widen and re-run before writing the conclusion, not after.
```

**Part A — the full 8-point rigor preamble, verbatim, in every prompt:**

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

**Part B — the structured request, every element (below the preamble):**

- **Brand context:** profile name + channels in scope + geo, in one line.
- **The task:** one sentence — what to map, find, or size.
- **Numbered sub-questions / verticals**, so nothing is skipped and the output comes back structured.
- **Per-item tool usage:** for each sub-question, the exact tools and the params that matter (`exclude_kids_content` to split buyable vs. made-for-kids; `get_trends` search-term based, not brand/person filters; both TikTok date buckets; `include_total_statistics` for aggregate counts).
- **Inline constraints that bite here:** the ~2026-01-01 floor; the caps in play (YouTube 180-day stats, TikTok 25 countries / four buckets, trends top-10); the coverage caveats (social country tags ~half, shares ~a quarter, enrichment only us/gb/ca/au/jp) — each stated where it applies.
- **Decision this serves:** one line.
- **In the output, give:** total volume with its date window; the count of distinct channels/videos/authors behind it; a named number of real example URLs where relevant; any split the task needs (buyable vs. kids, fandom vs. gift); and the denominator behind every percentage.

A prompt missing any Part B element is not finished — and a prompt without Part A0 (the Execution Protocol) at the top, or its closing coverage self-audit, is not finished either.

### Worked example 1 — content landscape (SmartList seeding)

```
EXECUTION PROTOCOL — run all of this. It is procedure, not suggestion.

- RUN THE FULL SWEEP (a checklist, not a vibe). Before searching, list every tool
  that could bear on this question and commit to calling each; you account for all
  of them in the self-audit at the end. Start broad, then narrow — open with wide
  framings to survey the landscape before drilling into specifics. Unless a tool is
  genuinely irrelevant (and you say why), you call: get_news_articles AND
  get_news_moments (moments cluster stories articles scatter; run both sort_by=size
  and sort_by=recency); get_social_media_posts AND get_social_media_narratives,
  pulled PER PLATFORM, not five platforms lumped into one call; get_trends for the
  macro shape; get_tiktok_hashtags to DISCOVER the vernacular (feeds the term rule
  below); get_youtube_videos / get_youtube_channels where a creator/content
  landscape is in scope; and search_web + read_web_pages + find_similar_pages +
  answer_from_web for anything the above don't reach. One tool or one call is not a
  search. A tool you did not call is a gap to report, not a step to skip.

- VARY THE TERMS (a floor of six, not a ceiling of one). A single obvious phrase
  misses most of the conversation, because people don't all use your words. Per
  sub-question, run AT LEAST SIX term variations spanning: (a) the literal term;
  (b) synonyms and alternate phrasings; (c) the community/vernacular term people
  actually use — discover it with get_tiktok_hashtags, don't guess it; (d) proper
  nouns / entities involved (people, titles, events, brands); (e) the adjacent or
  umbrella category; (f) the critic or backlash framing, so you capture the whole
  conversation and not only the flattering half. A single call caps at 3
  search_terms, so this is several calls per tool. That is expected.

- READ FULL BODIES BEFORE YOU QUOTE OR CHARACTERIZE. Snippets truncate at ~2,000
  characters and drop the specifics. On the top items, pull the full article body
  (the full-content option on get_news_articles) and run read_web_pages on the
  actual URLs for verbatim quotes and named detail. Never quote or characterize a
  specific claim from a snippet alone.

- THIN IS A TRIGGER, NOT A FINDING. Do not call a topic small, limited, quiet or
  absent until the recall floor is met: every applicable tool called, six+ term
  variations across two+ tools, full bodies read on the top items, and at least one
  reformulation using vernacular found in the data. "Limited results" means widen
  and re-run. Only after the floor is met may you report thinness — and then as a
  stated coverage limit naming the terms and tools you tried, never as a conclusion
  about the world.

- CLOSE WITH A COVERAGE SELF-AUDIT. Before any findings, print this table, one row
  per tool. No conclusions until it is complete:
    | Tool | Called? | Terms / params used | Volume returned | Gap or next step |
    | get_news_articles | | | | |
    | get_news_moments | | | | |
    | get_social_media_posts | | | | |
    | get_social_media_narratives | | | | |
    | get_trends | | | | |
    | get_tiktok_hashtags | | | | |
    | get_youtube_videos / channels | | | | |
    | open web (search / read) | | | | |
  Any row empty or thin: widen and re-run before writing the conclusion, not after.

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

Before any findings, print the coverage self-audit table from the Execution Protocol
— every tool row filled — and if any vertical is thin, widen and re-run before you
write it up.
```

### Worked example 2 — TikTok hashtag targeting

```
EXECUTION PROTOCOL — run all of this. It is procedure, not suggestion.

- RUN THE FULL SWEEP (a checklist, not a vibe). Before searching, list every tool
  that could bear on this question and commit to calling each; you account for all
  of them in the self-audit at the end. Start broad, then narrow — open with wide
  framings to survey the landscape before drilling into specifics. Unless a tool is
  genuinely irrelevant (and you say why), you call: get_news_articles AND
  get_news_moments (moments cluster stories articles scatter; run both sort_by=size
  and sort_by=recency); get_social_media_posts AND get_social_media_narratives,
  pulled PER PLATFORM, not five platforms lumped into one call; get_trends for the
  macro shape; get_tiktok_hashtags to DISCOVER the vernacular (feeds the term rule
  below); get_youtube_videos / get_youtube_channels where a creator/content
  landscape is in scope; and search_web + read_web_pages + find_similar_pages +
  answer_from_web for anything the above don't reach. One tool or one call is not a
  search. A tool you did not call is a gap to report, not a step to skip.

- VARY THE TERMS (a floor of six, not a ceiling of one). A single obvious phrase
  misses most of the conversation, because people don't all use your words. Per
  sub-question, run AT LEAST SIX term variations spanning: (a) the literal term;
  (b) synonyms and alternate phrasings; (c) the community/vernacular term people
  actually use — discover it with get_tiktok_hashtags, don't guess it; (d) proper
  nouns / entities involved (people, titles, events, brands); (e) the adjacent or
  umbrella category; (f) the critic or backlash framing, so you capture the whole
  conversation and not only the flattering half. A single call caps at 3
  search_terms, so this is several calls per tool. That is expected.

- READ FULL BODIES BEFORE YOU QUOTE OR CHARACTERIZE. Snippets truncate at ~2,000
  characters and drop the specifics. On the top items, pull the full article body
  (the full-content option on get_news_articles) and run read_web_pages on the
  actual URLs for verbatim quotes and named detail. Never quote or characterize a
  specific claim from a snippet alone.

- THIN IS A TRIGGER, NOT A FINDING. Do not call a topic small, limited, quiet or
  absent until the recall floor is met: every applicable tool called, six+ term
  variations across two+ tools, full bodies read on the top items, and at least one
  reformulation using vernacular found in the data. "Limited results" means widen
  and re-run. Only after the floor is met may you report thinness — and then as a
  stated coverage limit naming the terms and tools you tried, never as a conclusion
  about the world.

- CLOSE WITH A COVERAGE SELF-AUDIT. Before any findings, print this table, one row
  per tool. No conclusions until it is complete:
    | Tool | Called? | Terms / params used | Volume returned | Gap or next step |
    | get_news_articles | | | | |
    | get_news_moments | | | | |
    | get_social_media_posts | | | | |
    | get_social_media_narratives | | | | |
    | get_trends | | | | |
    | get_tiktok_hashtags | | | | |
    | get_youtube_videos / channels | | | | |
    | open web (search / read) | | | | |
  Any row empty or thin: widen and re-run before writing the conclusion, not after.

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

Now the request:

Brand context: P&G Star Wars Crossover — self-service, United States, with TikTok
Trend Targeting in scope.

Identify the TikTok hashtags this campaign could target to reach Star Wars fans
and parents shopping Star Wars for their kids, and tell me which are rising versus
evergreen.

- Use get_tiktok_hashtags for the United States. This tool browses by category and
  fixed time buckets, not free-text search — so pull the top hashtags in the
  relevant categories (for example Entertainment, Gaming, Family or Parenting, and
  Toys, matching the tool's category list), for both the 30-day and 120-day
  buckets, and from those isolate (a) Star Wars fandom hashtags and (b) parenting,
  gift, and toy hashtags that intersect with Star Wars. Report each hashtag with
  its view or volume figure and which time bucket it came from, and compare the
  30-day against the 120-day to show what is rising.
- Cross-check with get_social_media_narratives and get_social_media_posts on TikTok
  and Instagram for the same themes, to confirm the hashtags reflect a real
  conversation and its sentiment.

Only use data from 2026-01-01 onward. Roughly half of social posts carry no country
tag and share counts populate on only about a quarter of posts — state that caveat
with any engagement figure and don't present U.S.-only counts as complete.

Decision this serves: the TikTok Trend Targeting hashtag set for the campaign,
split into always-on fandom tags and reactive tentpole or gift tags.

In the output, give each hashtag with its volume, its time bucket, and whether it
is rising or steady; the sample size behind any sentiment read; and a clear split
between fandom hashtags and parenting or gift hashtags.

Before any findings, print the coverage self-audit table from the Execution Protocol
— every tool row filled, TikTok buckets and per-platform social cross-checks shown —
and if a hashtag set looks thin, widen the categories and re-run before writing it up.
```

---

## PART 1 — HOW TO GET A RIGOROUS READ

Everything the agent does well on a research question comes from one well-built prompt. The block below is a **compressed scaffold** — the authoritative, paste-whole form is the **Part 0 standard** (the Execution Protocol + the full 8-point preamble + all Part B elements), and Worked example 1 there is a complete model. Use the scaffold as a quick shape, then expand it to the Part 0 standard — Execution Protocol included — before running.

### The master research prompt

```
Run a full-rigor read for the question at the bottom. Hold to these standards for
the whole response, not just the first tool call:

- USE EVERY RELEVANT TOOL, not one — a checklist you complete and report against, not
  a suggestion. Start broad, then narrow. Run get_news_articles + get_news_moments for
  press coverage and clustering; get_social_media_posts + get_social_media_narratives
  for social sentiment and narrative clustering, PER PLATFORM not lumped; get_trends for
  the macro shape; get_tiktok_hashtags where TikTok matters (use it to DISCOVER the
  vernacular, not just to confirm tags I already named); get_youtube_videos /
  get_youtube_channels for the creator and content landscape; and search_web /
  read_web_pages / answer_from_web for anything the others don't cover. Run AT LEAST SIX
  search-term variations per sub-question (literal / synonym / vernacular from
  get_tiktok_hashtags / entities / adjacent category / critic framing) — a call caps at
  3 terms, so that is several calls per tool — and pull FULL article bodies (the
  full-content option + read_web_pages on the URLs) before quoting or characterizing any
  specific claim.
- SHOW THE NUMBERS. Surface the real counts from the results — total volume, the
  date / platform / publisher / sentiment distributions, sample sizes. Every
  percentage carries its denominator; every volume carries its window. If a set is
  thin or one-sided, say so, and re-run it another way before calling a
  conversation small.
- CITE EVERYTHING, INVENT NOTHING. Every figure, quote and claim traces to a
  specific tool result with its source (URL / publisher / platform / date). If the
  tools return nothing on a sub-question, say "no data found" — do not fill the gap
  from general knowledge.
- DATA FIRST, THEN INFERENCE. Give what the sources literally say, then a clearly
  separate section for interpretation, naming the data points each read rests on.
- BRAND LENS. Read every finding through <BRAND>'s Brand Profile and name which
  cultural dimension it implicates (risk tolerance, humor risk, harm sensitivity,
  irony fluency, cultural speed, activism, polarization, institutional trust,
  expressiveness). If there is no Brand Profile, say so and apply a stated category
  lens instead.
- SHOW THE ARC with dates — rising, falling, plateauing, and whether sentiment is
  moving. Call out inflection points.
- CROSS-CHECK across tools. Say where two tools converge; report divergence as a
  finding rather than smoothing it over; never merge figures from two tools into
  one number.
- MIND THE FLOOR: these tools do not reach before ~1 January 2026. If the question
  needs anything earlier, tell me it is out of range instead of approximating it.
- SELF-AUDIT BEFORE YOU CONCLUDE: print a tool-by-tool coverage table — tool | called? |
  terms used | volume | gap. Thin is a trigger to widen and re-run, never a finding: do
  not call a conversation small until the full sweep, the six term variations, and the
  full-body reads are all done, and then report the thinness as a coverage limit.
- END WITH THE CALL: lean-in / lean-away / stay-informed / ignore, tied to the decision below.

BRAND: <BRAND>
DECISION THIS SERVES: <one sentence — the actual RFP or insights question>
WINDOW: <e.g. 1 Jan 2026 – today, plus a trailing 90-day "what is live now" cut>

THE QUESTION:
<your research question, in full>
```

Expanded to the Part 0 standard, that covers any ad-hoc read. Parts 2–5 are the capability reference — what each source returns and what to ask it for, as scaffolds and output-field notes, not finished prompts.

---

## PART 2 — THE DATA SOURCES IT READS

Six families. All share the ~1 January 2026 floor. For each: what it returns, its parameters, its bounds. Where a source is used differently enough to deserve its own block, the block is right there.

### 2.1 News — `get_news_articles`, `get_news_moments`  *(Agent runs this)*

`get_news_articles` returns individual articles; `get_news_moments` returns clustered stories (a moment is a cluster of related articles).

- **Articles:** 1–3 parallel `search_terms`, or pure browse by date / category / publisher / entity / language / `publisher_location` (22 supported countries). `limit` ≤ 50 per term. Full article body optional; without it, body truncates at ~2,000 characters. Returns population stats — publisher, category, location and date distributions — unless you disable them.
- **Moments:** same filter set. `limit` ≤ 20 per term. `sort_by` is `size` (article-count first) or `recency`, and is mutually exclusive with `search_terms`.
- **Bounds:** floor ~1 Jan 2026, no upper bound beyond now, sub-day (hour/minute) precision on both.

Returns press-coverage volume and shape, the distributions above, the news arc, and moment clustering. Read it as press, not conversation — a news count is not a social count.

### 2.2 Social — `get_social_media_posts`, `get_social_media_narratives`  *(Agent runs this)*

`get_social_media_posts` returns raw posts; `get_social_media_narratives` returns clustered narratives and adds a sentiment filter and cluster-level engagement floors.

- **Posts params:** `platform` — X, Reddit, Truth Social, Pinterest, Instagram, Bluesky, TikTok, Threads (max 5 per call). `theme` — 31 fixed values only: discounts, purchase, appearance, churn, cost, ads, experience, craftmanship, transaction, criminal, loyalty, stock, taste, temperature, ambiance, delivery, fit, injury, knowledge, leadership, comfort, access, illness, location, restrooms, speed, satisfaction, wait times, cleanliness, durability, friendliness, selection (your audit labels these "31 fixed values" but the list runs to 32 items — confirm the exact count against the live enum). Engagement floors — `min_likes`, `min_comments`, `min_shares`, `min_author_followers`. `language_code` — ISO 639-1, max 5. `country` — ISO 3166-1 alpha-2, max 5 (best coverage: us, th, gb, in, br, fr, tr, mx). Up to 3 `search_terms`. No sentiment filter at post level.
- **Narratives, additional:** `sentiment` — very_positive → very_negative. Cluster-level engagement floors. `sort_by` (size or recency) is mutually exclusive with `search_terms`.
- **Coverage to state alongside figures:** ~half of posts carry no country tag; share counts populate on only ~a quarter of posts; the fullest enrichment (themes, entities, follower counts) is limited to us/gb/ca/au/jp. These are data-quality notes to put next to the number, not reasons to avoid the pull.

Returns theme mix, platform mix, sentiment (via narratives), community vocabulary, named posts and creators, and the conversation arc inside the window.

### 2.3 TikTok hashtags — `get_tiktok_hashtags`  *(Agent runs this)*

A discovery surface — the top trending hashtags by category, country and date. Use it to find vernacular you would not have guessed, not to confirm tags you already named (searching it for your own guesses is how you get false positives).

- **Params:** `category_name` from a ~70-value enum. `country` limited to 25 codes: US GB CA DE ES TR ZA NG CN IN PH TH MX BR AR FR IT NL PL AU AE JP PT KR VN. `date_range` fixed to four buckets — 1DAY / 7DAY / 30DAY / 120DAY, no custom range. `limit` ≤ 200.

**Discovery block:**

```
Discover the actual TikTok vernacular around <topic> before we measure anything.
Run get_tiktok_hashtags across the relevant category_name value(s), country <code>,
date_range <1DAY|7DAY|30DAY|120DAY>. Surface the trending tags I would NOT have
guessed — do not just confirm tags I name. Then tell me which of these are worth
measuring with the social tools, and which look like noise.
```

### 2.4 Cultural trends — `get_trends`  *(Agent runs this)*

A composite of moments and narratives over longer horizons — synthesized trends, not raw hits.

- **Params:** brand and person filters are restricted to the **top 10 brands / people** the underlying data tracks (max 5 each per call). `limit` capped at 5 per term. Floor ~1 Jan 2026.

Returns the macro, longitudinal shape and whether a tracked brand/person is rising or falling. If `<BRAND>` is outside the tracked top-10 set, the agent should say so rather than substitute.

### 2.5 YouTube — `get_youtube_videos`, `get_youtube_channels`  *(Agent runs this)*

Surfaces videos and channels with filtering, sitting on Sightly's video-level YouTube access.

- **Params:** `is_short`, `iab_category` (videos only, max 5), `exclude_kids_content`, `min_views`, `min_subscribers`, `min_video_count`, `language` / `country` (max 5 each).
- **The window trade-off:** statistics-enabled queries are capped at a **180-day** window. Omit `start_date` for "most recent 180 days" with aggregate distributions, or set `include_total_statistics=false` to search full history back to 2005-02-14 — but then you lose the aggregate distributions. Depth of history or aggregate stats, not both.
- **YouTube has no sentiment field.** These tools return the content and creator landscape, not audience sentiment. Read sentiment from the social tools (§2.2), whose platform set does **not** include YouTube — don't ask for a YouTube sentiment split the tools don't measure.

**Creator-landscape block:**

```
Build the creator and content landscape for <topic> for <BRAND>. Run
get_youtube_channels and get_youtube_videos with iab_category <up to 5>,
exclude_kids_content as appropriate, and sensible min_views / min_subscribers
thresholds. Default to the most-recent-180-day window with aggregate stats ON; if
I need older history, tell me first that turning stats off is the cost. Return the
NAMED channels and videos with their metrics, not just counts, and note for each
why it is talking about this. This is for vetting creators against the Brand
Profile — not a talent roster.
```

### 2.6 Open web — `search_web`, `read_web_pages`, `find_similar_pages`, `answer_from_web`  *(Agent runs this)*

- `search_web` (optional category: company, research paper, news, pdf, github, tweet, personal site, linkedin profile, financial report). `read_web_pages` (full extraction from named URLs). `find_similar_pages` (similarity from a seed URL). `answer_from_web` (a single synthesized, cited factual answer — not open browsing).
- No fixed time window; reflects what is publicly indexed now; no completeness guarantee.

For third-party benchmarks, company facts, and verifying a claim against the open record.

### 2.7 Signals — `get_signals`, `get_signal_details`  *(Agent runs this)*

A signal is a trend, moment or theme pulled from the wider conversation, tied to your brand, carrying a title, a summary, and a recommendation — target, block, no action, or monitor. Acting on a signal (pushing target/block live) happens through the Activation Job and your connected platforms; reading and explaining signals is the agent's job in chat.

**Signals-read block:**

```
Pull the current signals for <BRAND> with get_signals, then get_signal_details on
the top few. For each, give the title, the summary, and its recommendation
(target / block / no action / monitor), and name which cultural dimension of the
Brand Profile it implicates. Do not attribute a recommendation the signal itself
does not carry.
```

### Competitor territory scan (uses the reads above)

```
Scan the conversation territory for <BRAND>'s named category competitors: <list>.
For EACH competitor, run separate competitor-seeded pulls across news, social and
YouTube — do not slice a <BRAND>-seeded pull. Characterise the territory each one
owns: dominant themes, the platforms carrying it, the narrative, and sentiment
direction with denominators. Keep every figure attributed to its own competitor
and tool; never pool across competitors. Cite everything; where a competitor is
thin in the data, say so rather than inferring. Close with where the open territory
is for <BRAND>.
```

---

## PART 3 — THE REPORTS AND JOBS IT CAN RUN

Five productized outputs. Each has its own self-contained kickoff block. All render in the brand's style guide.

### 3.1 Insights Report — `show_form kind=INSIGHTS`  *(Agent runs this)*

The deep, one-off cultural research run — this is the productized version of a full conversation-landscape read, so use it rather than hand-assembling one. Not recurring: one run, one document.

- **Fields:** `report_title`; `intent` (one sentence, and it shapes every search, so make it the real decision); `window_days` (default 90, range 1–365 — but don't set a window that reaches before the ~1 January 2026 floor; from today that is roughly the last 260 days, so the field's 365 max crosses the floor); `flight_window`; `media_budget_usd`; `include_media_direction` (off by default).
- **What it does internally:** establishes brand context (site + inferred-vs-confirmed competitors), runs three passes (competitor scan, category/culture scan, flashpoint sweep — each broadens then narrows to what the data surfaced, then re-validates the top findings against engagement thresholds), reconciles against named gaps, then writes. Every search shows live as its own card with its terms and counts.
- **What it outputs:** a headline position + 3–7 takeaways; a coverage section; tabs in fixed order (scan; brand/industry/competitors; 1–3 non-repeating deep dives; planning last); a ranked signal table with evidence ratings (Strong / Directional / Limited, defined at first use); a competitor leaderboard by territory; linked real posts, articles, videos and hashtags as proof; a planning section (target / monitor / avoid, plus channel notes and a watchlist); optional media direction (a starting point, not a final plan); and a glossary pinned across tabs.

**Kickoff block:**

```
Run an Insights Report (kind=INSIGHTS) for <BRAND>.
- report_title: <title>
- intent: <ONE precise sentence — this shapes every search, so make it the actual
  decision, e.g. "Establish whether <BRAND> should lean into <topic> for a Q4
  flight, and which competitors own that territory">
- window_days: <90 default, 1–365>
- flight_window: <dates>
- media_budget_usd: <if relevant>
- include_media_direction: <on only if you want a starting-point plan, and treat it
  as a starting point, not final>
Show each search live, and end with the ranked signal table (Strong / Directional /
Limited) and the planning section.
```

### 3.2 Highlights Report — `show_form kind=HIGHLIGHTS`  *(Agent runs this)*

A client-facing one-pager PDF, up to **6 targeted-signal cards** per run. If more than 6 were targeted in the window, the newest are proposed and a reviewer picks the final set. Each card: title, date targeted, thumbnail (the signal's own video/article/moment imagery, else a standard engagement tile), and its original description.

- **Modes:** `once` — `window_start` / `window_end`, default last 7 complete days, max **62-day** span. `schedule` — `interval_days` 1–90, each run looking back exactly that many days, running until `ends_on` (defaults to the deal's end date).
- **Review gate:** on by default (named reviewers sign off before send); can be turned off to auto-send.
- **Delivery:** emailed as a PDF attachment. Every run is its own entry in the Jobs list. Cancelling a schedule also cancels any report still awaiting review, unsent.
- **Editing:** you cannot edit a Highlights job in place — cancel and recreate. You cannot change the deal it is tied to — create a new job. Pause / resume / cancel is a Jobs-list action (UI-only).

**Kickoff block:**

```
Set up a Highlights Report (kind=HIGHLIGHTS) for deal <deal_id>.
- mode: <once | schedule>
- once: window_start / window_end (default last 7 complete days, max 62-day span)
- schedule: interval_days <1–90>, ends_on <default deal end date>
- review gate: <on, named reviewers | off, auto-send>
- recipients: <emails>
Up to 6 signal cards per run; if more than 6 were targeted, propose the newest and
let the reviewer pick the final set.
```

### 3.3 Reporting Job — `show_form kind=REPORTING`  *(Agent runs this)*

A recurring performance-data export tied to a deal. This is the only way to get spend / CPM / CTR performance numbers — there is no live performance dashboard the agent can query.

- **Fields:** `name`; `deal_id`; `recipients` (comma-separated emails); `report_format` (XLSX default, or CSV); `schedule_starts_at`; `repeat_period` (DAY / WEEK / MONTH) + `repeat_interval`; `days_of_week` (when weekly); `ends_at` (required at submit).
- Keeps the timezone it was created in, so delivery time never drifts.

**Kickoff block:**

```
Create a Reporting Job (kind=REPORTING) for deal <deal_id>.
- name: <name>
- recipients: <comma-separated emails>
- report_format: <XLSX | CSV>
- schedule_starts_at: <datetime>
- repeat_period: <DAY | WEEK | MONTH>, repeat_interval: <n>
- days_of_week: <if weekly>
- ends_at: <required>
This is how we get spend / CPM / CTR out — there is no live dashboard to query.
```

### 3.4 Activation Job — `show_form kind=ACTIVATION`  *(Agent runs this)*

A recurring job that watches a topic for a deal and turns findings into live targeting or blocking on connected platforms.

- **Fields:** `name`; `deal_id`; `topic` (what it searches each run); `interval_hours` (1–24, also the per-run lookback); `starts_at`; `ends_at`; `allowed_actions` (TARGET and/or BLOCK).
- The schedule always fits inside the deal's date range. A run is **skipped, not failed**, when the deal lacks data it needs: no campaigns mapped, no reporting timezone set, or (if targeting is allowed) no personas mapped to its campaigns — all fixable in Deal Builder, after which the next run proceeds.
- **Removals are always performance-driven.** The review shows the deal, the KPI goal, the target threshold, and the actual performance that triggered removal, tied to the `removal_kpi` you set at link time (5.4). If no KPI was recorded, the agent says the context wasn't captured rather than guessing a cause.

**Kickoff block:**

```
Create an Activation Job (kind=ACTIVATION) for deal <deal_id>.
- name: <name>
- topic: <what it searches each run>
- interval_hours: <1–24, also the per-run lookback>
- starts_at / ends_at: <inside the deal's date range>
- allowed_actions: <TARGET and/or BLOCK>
First confirm the deal has campaigns mapped, a reporting timezone set, and — if
targeting — personas mapped to its campaigns; otherwise runs skip rather than fail.
Any removal must cite the recorded KPI and threshold; if none, say so.
```

### 3.5 HTML Artifacts — `read_artifact_spec`, `write_html_artifact`, `read_html_artifact`, `revise_html_artifact`, `show_html_artifact`  *(Agent runs this)*

A persisted, brand-styled document — distinct from ordinary in-chat UI that only lives in the conversation. Use it when a read should outlive the thread.

- **Build:** research first (real tool results only) → `read_artifact_spec` → `write_html_artifact` (title < 120 chars; full body markup; no doctype / head / style tags) → later, `read_html_artifact` + `revise_html_artifact` for exact passage swaps, each a new version → `show_html_artifact` reopens on request.
- **In the app:** artifacts live in a library scoped to the active brand, grouped by kind, newest first, visible to anyone with brand access, credited to whoever made them. Renamed/deleted via a card menu (delete removes all versions). Every revision is kept with a version picker once more than one exists; a version still being written shows as a draft.
- **Author lock (UI-only for others):** "Edit in chat" reopens the originating session, but only for the person who created it. The agent can read a teammate's artifact and produce a new one; it cannot resume their authoring session. If the original session is gone, editing is unavailable but reading persists.

**Build block:**

```
Build an HTML artifact for <BRAND>: <what it is>. Research first with real tool
results only, then read_artifact_spec and write_html_artifact. Title under 120
characters. Everything in it traces to a tool result — no filler charts. Render in
the brand style guide. This will persist in the brand's artifact library.
```

---

## PART 4 — WHAT IT RENDERS

So you know what to ask a report, artifact or in-chat answer to show. Every chart needs real numeric arrays from a tool result — there is no illustrative filler, by design.

**Charts — 9 render types.** BarChart (grouped/stacked); HorizontalBarChart (grouped/stacked, best for long labels and ranked lists); LineChart (linear/natural/step); AreaChart (linear/natural/step); RadarChart (multi-variable comparison); PieChart (pie/donut, circular/semiCircular); RadialChart; ScatterChart (x/y/z, correlation and clustering); SingleStackedBarChart (single stacked composition bar).

**Object cards — one per real Sightly record.** SignalCard, ArticleCard, SocialPostCard, NarrativeCard, MomentCard, TrendCard, YoutubeVideoCard, YoutubeChannelCard, TiktokHashtagCard, StyleGuide, BrandProfileProgress. Each field maps 1:1 to a tool-result field — a card can't be populated without first calling the tool it represents, and required fields (like imageUrl) must be real, vetted URLs.

**Structural primitives.** Stack, Card (card/sunk/clear), CardHeader, Tabs/TabItem, Accordion/AccordionItem, Carousel, Steps/StepsItem, Table/Col, TagBlock/Tag, Callout/TextCallout, CodeBlock, Image/ImageBlock/ImageGallery, Separator, Icon (Phosphor, 5 weights, 5 semantic variants), IconText, Logo (by entity domain), Citation (source pill), FollowUps/FollowUpItem.

**Layout and semantic rules.** Max 3 items side-by-side, and only for single-metric content; anything list-like beyond 3 becomes a Table or a bar chart. Color variants (success / warning / danger / info / neutral) always map to real data meaning, never decoration. A real report closes with a sunk-card disclaimer citing the Brand Mentality / Sightly dataset and the date.

**How to prompt for a visual.** Describe the shape of the answer, not the component — "a ranked horizontal bar of theme volume," "the sentiment split as a donut with denominators" — and the agent maps it from real arrays. Ask for a chart of data the tools didn't return and you get nothing.

---

## PART 5 — BRAND SETUP & MEDIA PLUMBING IT MANAGES

The config surface. Each with its self-contained block. All of it operates inside the currently active brand — the agent cannot switch brands (that is UI-only).

### 5.1 Brand & User Profile  *(Agent runs this)*

The Brand Profile is the standing context the agent reads on every request, and the source of the cultural-dimension scores the brand lens uses — so a thin profile weakens every read.

- **`update_brand_profile`:** category, tagline, mission_statement, core_products, core_values, competitive_brands, primary_market, harmful_exclusions, safe_harbor_list, kids_content_stance, onboarding_complete, plus 9 cultural dimensions (risk_tolerance, humor_risk, harm_sensitivity, irony_fluency, cultural_speed, activism, polarization, institutional_trust, expressiveness), each 1–10 with a rationale. Hard character caps per field (255 / 500 / 1000 depending on field); oversized text is rejected wholesale, not truncated.
- **`get_brand_profile_progress`:** exact completion percentages by section, never a field count.
- **`update_user_profile`:** job_title, role_and_responsibilities, use_cases, onboarding_complete — follows you across every brand.
- Both are also editable in the app (pencil-edit) — a parallel path, same result.

```
Run get_brand_profile_progress for <BRAND> and tell me exact completion by section
and what's missing. Then, for the fields I give you, run update_brand_profile,
including any cultural-dimension scores (1–10 with a rationale each). Respect the
character caps — if I hand you something too long, flag it rather than letting the
update get rejected wholesale.
```

### 5.2 Brand Style Guide  *(Agent runs this)*

Every Insights Report, Highlights Report and HTML Artifact renders in this guide's colors and type, so the style guide is upstream of how all rendered deliverables look.

- **`derive_brand_style`:** renders the brand's homepage (or a named page), takes a couple of minutes, rejects non-public-site URLs; captures colors by role, heading/body type, spacing/radius, logo.
- **`get_brand_style`:** current guide + provenance (source URL, version, whether it fell back to a default house style, last editor).
- **`update_brand_style`:** full-replace on whichever of colors / typography / layout / component_tokens / radii / shadows / logo_url you pass; each edit a new version.
- **`revert_brand_style`:** discards manual edits, restores the last derived version.
- Style never changes unless asked — the agent never silently re-derives after a rebrand. If a site can't be read in time, the brand gets a labeled default house style and you can retry any time.

```
Run get_brand_style for <BRAND> and show the current guide plus provenance (source
URL, version, whether it fell back to house style, last editor). If it is on a
default house style and we have a real public site, derive_brand_style from
<homepage or named page> — but confirm with me first, do not re-derive silently.
```

### 5.3 Deals  *(Agent runs this)*

A deal is the container that groups campaigns, their flights (run windows) and personas, and it is the unit that Reporting and Activation Jobs attach to — no deal, no job.

- **`create_deal` / `update_deal` / `list_brand_deals`** (status filter: all / active / upcoming / past). Deal names unique per brand; end_date ≥ start_date. Renaming or date changes are blocked if they'd conflict with a linked campaign's overlap elsewhere.

```
Create a deal for <BRAND>: name <unique per brand>, start <date>, end <date>. Then
list_brand_deals to confirm it's there. Flag any conflict with a linked campaign's
overlap before you write.
```

### 5.4 Campaigns & Flights  *(Agent runs discovery + linking; flight editing is UI-only)*

- **Discovery:** `list_brand_google_ads_customers`, `list_brand_tiktok_advertisers`, `list_google_ads_customer_campaigns`, `list_google_ads_customer_ad_groups`, `list_google_ads_campaign_ad_groups`, `list_tiktok_advertiser_campaigns`, `list_tiktok_advertiser_ad_groups`, `list_tiktok_campaign_ad_groups`, `list_deal_campaigns`. (Your audit compressed the two customer/advertiser-level `…_ad_groups` tools with slash notation — confirm both exist against the live tool set before relying on them.)
- **Linking:** `link_google_ads_campaigns_to_deal` / `link_tiktok_campaigns_to_deal`. Rejects a campaign already linked with an overlapping date range elsewhere. Sets the deal's timezone from the campaigns — all campaigns on one deal must share a timezone. Seeds one default full-coverage flight. Requires one `removal_kpi` + `removal_threshold` per call, and the agent asks you for these, never assumes them:
  - Google Ads: CPM, CTR, CPV, VIEW_RATE, CPC, VCR
  - TikTok: CTR, CPC, CPM, CPV, VCR, VIEW_RATE, ENGAGEMENT_RATE
- **Unlinking:** `unlink_google_ads_campaigns_from_deal` / `unlink_tiktok_campaigns_from_deal`. Idempotent; ignored campaigns reported back. Unlinking the last campaign clears the deal's timezone.
- **Flights:** linking seeds one default full-coverage flight. Adjusting individual flight windows beyond that is done in the deal's detail panel (UI-only).

```
For deal <deal_id>: discover campaigns with the list_* tools, then link the
<Google Ads | TikTok> campaigns <ids>. Ask me for the removal_kpi and
removal_threshold before you link — do not assume them. Confirm the timezone the
link sets from the campaigns, and that all campaigns on this deal share it.
```

### 5.5 Personas & audience targeting  *(Agent runs this)*

- **`add_persona`** — hard cap **5 per brand**; remove one to add past the cap. **`update_persona`** — the demographics sub-object is full-replace (age_range, genders, household_income, parental_status), so resend anything you want kept. **`remove_persona`**.
- **Linking to media:** `link_campaigns_to_persona` / `unlink_campaigns_from_persona` / `list_persona_campaigns`. A campaign can hold at most one persona per deal — unlink from the other persona first.
- **Targeting guidance:** `get_audience_targeting`, one call per platform: Programmatic, YouTube, Pinterest, LinkedIn, TikTok, Snapchat, Meta, X, Reddit, Spotify, Search.
- Personas belong to the brand and are reusable across deals; each deal's campaign list shows which persona it currently targets.

```
For <BRAND>: show current personas (max 5). If we need a sixth, tell me — we remove
one first, we do not silently merge. For persona <name>, run get_audience_targeting
per platform <Programmatic / YouTube / Pinterest / LinkedIn / TikTok / Snapchat /
Meta / X / Reddit / Spotify / Search> and give me the targeting guidance. If I
update demographics, resend the full sub-object — it is full-replace.
```

### 5.6 Connections & brand switching  *(UI-only)*

Ad platforms that link: Google Ads and TikTok, each with connected / not-connected status. Connecting or disconnecting an account, and switching the active brand, are UI actions — the agent can't do either. Once a platform is connected, the agent reads it via the discovery tools in 5.4.

---

## PART 6 — THE HARD LIMITS (EXHAUSTIVE)

Every boundary in one place, from your audit.

**Data window / geography**
- News, social, TikTok hashtags, trends: nothing before **~1 January 2026**. Every year-over-year or "same window last year" question reaches before the floor and can't run — the agent should say out of range, not approximate.
- YouTube statistics mode: **180-day** cap. Full history back to 2005-02-14 only if you set `include_total_statistics=false` and give up aggregate distributions.
- TikTok hashtag country filter: **25 codes only**. TikTok `date_range`: four fixed buckets (1/7/30/120 DAY), no custom range.
- News publisher-location filter: **22 countries**.
- Social: ~half of posts carry no country tag; share counts on ~a quarter; fullest enrichment only on us/gb/ca/au/jp. State these next to the figure.
- Trends: brand/person filters limited to the **top 10 tracked** each (max 5 per call).

**Structural / account**
- **5-persona cap** per brand.
- Hard character caps on every brand-profile text field; oversized input is rejected outright, not truncated.
- A campaign links to **one persona per deal**, and to **one deal** for any given date range.
- All campaigns linked to a deal in one call share **one removal KPI/threshold** and **one timezone**.

**Reporting / jobs**
- No live performance dashboard — spend / CPM / CTR come only from a scheduled Reporting Job.
- No raw platform error / diagnostic data in any client-facing surface, including Highlights and activation removals.
- Activation jobs: **1–24 hour** cadence. Highlights schedules: **1–90 day** cadence. A Highlights one-off window: **at most 62 days**.
- You cannot edit a Highlights job in place (cancel + recreate). You cannot change the deal a job is tied to (create a new job). Pause / resume / cancel is a Jobs-list action (UI-only).

**Session / scope**
- No memory across sessions beyond what's saved in the Brand Profile, User Profile, personas and deals. Within a session, `get_chat_history` recovers up to 100 prior messages.
- No image or asset generation — it only vets real URLs already in hand or found via search.
- No legal, financial, medical or tax advice.
- Every number, chart, card or claim traces to an actual tool result in the conversation. Nothing brand-, performance- or signal-specific is filled from general knowledge — which is exactly why you ask it real questions and make it show counts.

**UI-only (the agent has no tool — you do these in the app)**
- Connect / disconnect ad-platform accounts.
- Switch the active brand.
- Invite or manage Team members and roles.
- Pause / resume / cancel any job; edit a Highlights job in place; change a job's deal.
- Adjust individual flight windows beyond the default seeded on link.
- Resume a teammate's artifact authoring session (author-locked).
- In-app pencil-edit of the Brand / User Profile (parallel to the agent's update tools).

---

## PART 7 — COMPREHENSIVENESS SELF-AUDIT

Against your checklist, answered from the audit.

- **All limitations?** Yes — Part 6 consolidates the window floor, the YouTube 180-day trade-off, TikTok's 25 countries and 4 buckets, news' 22 countries, social's coverage caveats, trends' top-10 restriction; the account caps; the job constraints; the session limits; and the full UI-only set.
- **All insights and reports?** Yes — Insights Report (3.1), Highlights Report (3.2), Reporting Job (3.3), Activation Job (3.4), each with fields and rules, plus the ad-hoc reads in Parts 1–2.
- **Artifacts?** Yes — 3.5, full lifecycle, versioning, draft state, author lock.
- **All visualizations?** Yes — Part 4: nine chart types, the object cards, structural primitives, the max-3 rule, semantic and citation rules.
- **All time periods?** Yes — the ~1 Jan 2026 floor; YouTube's 180-day-vs-full-history trade-off and its 2005-02-14 back-stop; TikTok's four fixed buckets; sub-day precision on news and social; the web's "now."
- **All features?** Yes — reads, all three job types, Insights, Artifacts, Deals, Campaigns/Flights, Personas + targeting, Signals, Brand & User Profile, Style Guide, Connections, and the UI-only features named as such rather than implied available.
- **All sources?** Yes — news, social, TikTok hashtags, trends, YouTube, open web, plus the Brand Profile (including cultural-dimension scores) as the lens applied on top.

---

*If a live call ever contradicts a bound in here, that mismatch is the signal to re-verify against the live tool surface — not proof the manual is wrong. Re-confirm and update the affected part.*
