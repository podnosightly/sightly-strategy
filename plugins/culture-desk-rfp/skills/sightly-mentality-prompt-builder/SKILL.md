---
name: "sightly-mentality-prompt-builder"
description: "Builds rigorous prompts and query specs for Brand Mentality research. Routes each question to the right executor first — the Mentality Agent's own tool surface, or a listening-platform operator — then writes either a full-rigor agent prompt with named tool fan-out, or a runnable query spec with seed logic, term variants, channel scope and required output fields. Use when asking the Mentality Agent for a read, briefing someone with listening-platform access, designing a social or cultural intelligence pull, or when a research question needs to be turned into something executable. Triggers on \"write a Mentality prompt\", \"brief the agent\", \"design the query\", \"what should I ask for\", \"spec this pull\", \"get me a read on X\". Not for interpreting results — that's sightly-insights-to-action. This is Step 3a of the Sightly RFP workflow, the acquisition half of Brand Mentality discovery, and it also runs standalone for research questions that have nothing to do with a proposal."
---

# Sightly Mentality Prompt Builder

Turn a research question into something executable. Either a full-rigor prompt for the Brand Mentality Agent, or a query spec for someone with listening-platform access.

**The failure this prevents.** An unanswerable question does not return "unknown." It returns something formatted exactly like an answer, with press coverage or general knowledge standing in for corpus data. Nobody downstream can tell the difference from the document alone.

## Where this sits

**Step 3a of the RFP workflow — the acquisition half of Brand Mentality discovery.** Step 3b is `sightly-insights-to-action`, which interprets what comes back. Those are different jobs. They used to be one step with only the second half staffed, which is why requests for a Mentality prompt kept getting improvised at the moment they were needed.

**This step pauses the workflow, and the pause is real.** Every other step completes inside a session. This one produces an artifact a human carries to the Mentality Agent or to a listening-platform operator, and the answer may not come back for a day. Hand over the artifact, state plainly that 3b is blocked until the pull returns, and stop. Do not proceed on partial data, on press coverage standing in for corpus data, or on your own general knowledge — that is this skill's own failure mode, arriving one step later. If the deadline cannot absorb the wait, raise it now as a timeline flag rather than treating thin data as good enough.

Skip 3a only when verified data already exists. Outside an RFP, ignore the step numbering: a research question still routes and still needs a rigorous prompt.

---

## Step 1 — Route before you write

Two different executors with different capabilities. Deciding which one owns a question is the whole job, and it comes before any prompt gets written.

### What the Mentality Agent can do

Its own tool surface, as described by the agent:

| Tool | Use |
|---|---|
| `get_news_articles`, `get_news_moments` | Press coverage and clustering |
| `get_social_media_posts`, `get_social_media_narratives` | Platform-level sentiment and clustering |
| `get_trends` | Macro and longitudinal framing |
| `get_tiktok_hashtags` | TikTok hashtag volume and views |
| `get_youtube_videos`, `get_youtube_channels` | YouTube content and creators |
| `answer_from_web`, `search_web`, `read_web_pages`, `find_similar_pages` | Anything the above doesn't cover |

Plus the Brand Profile, with cultural dimension scores, for applying a brand lens.

### What it cannot do

**No confidence intervals.** In the agent's own words: these tools *"return counts and distributions, not confidence intervals."* It can report raw sample sizes and let you judge sufficiency. It cannot certify statistical significance, and any claim of significance from it is manufactured.

**Limited historical window on the social tools.** A documented hard floor around 2026-01-01 has been hit in practice. Any period-on-period comparison reaching further back cannot be run here.

**No author-level analytics at corpus scale.** Unique author counts, gender and age splits, per-post engagement broken out by platform, period-on-period universe change — these need the listening platform.

### The routing test

Ask: **which tool would return this, and does that tool carry the field being asked for?**

| Question type | Executor |
|---|---|
| Is this conversation growing, and what's in it | Mentality Agent |
| What are the narratives, who's driving them | Mentality Agent |
| Cultural context, adjacent conversations, creator landscape | Mentality Agent |
| Brand-lens read against the profile | Mentality Agent |
| Unique author counts, demographic splits | Listening platform |
| Per-post engagement by platform, with a stated denominator | Listening platform |
| Period-on-period change across more than one year | Listening platform |
| Competitor share of category conversation | Listening platform, competitor-seeded |

**If a question is split across both, say so and write both artifacts.** Do not quietly hand the whole thing to whichever is available.

### Write the limits into the register before you write the prompt

The "cannot do" list above is not background reading. Each limit is a prohibition that is knowable *before any data arrives*, which makes it the earliest possible entry in the project's do-not-use register:

- **No confidence intervals from the agent.** Any significance claim later attributed to it is manufactured.
- **No agent-sourced social data before roughly 2026-01-01.** Any period-on-period comparison reaching further back is unavailable from this executor.
- **No agent-sourced unique-author counts, demographic splits, or per-post engagement broken out by platform.** These need the listening platform.

Write them in at 3a, phrased as prohibitions rather than caveats. A register that already holds entries when QA first reads it is doing its job; an empty one is indistinguishable from one nobody filled. If routing sends part of a question to an executor that cannot carry it, that is also a register entry, not a footnote.

---

## Step 2a — Agent prompt: the standing rigor preamble

Paste in front of any request. This is the agent's own specification of how to get its best work, and it should be used close to verbatim.

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

2. REPORT STATISTICAL WEIGHT, NOT VIBES. Whenever a tool returns aggregate
   stats (include_total_statistics=true), surface the actual counts: total
   article/post volume, date distribution, platform/publisher mix, sentiment
   breakdown. State sample sizes explicitly (e.g. "47 articles across 12
   publishers, June 1–30"). If a data set is small or one-sided, say so
   instead of generalizing from it.

3. ZERO FABRICATION. Every fact, figure or quote must trace to a specific tool
   result with a citation — URL, publisher, date. If the tools return nothing
   on a sub-question, say "no data found" rather than filling the gap from
   general knowledge. Do not use background knowledge to complete a picture
   the data doesn't support; flag the gap.

4. SEPARATE DATA FROM INFERENCE. Present what the sources literally say first.
   Then, in a clearly marked section, give interpretation — labelled as
   inference, with the specific data points it rests on. Never blend the two
   into one unmarked narrative.

5. APPLY THE BRAND LENS THROUGHOUT. Filter every finding through the brand
   profile and name which dimension(s) it implicates. If the profile has gaps
   that limit the analysis, say so.

6. SHOW THE NARRATIVE ARC. Where timelines exist, describe the trajectory —
   rising, falling, plateauing — and whether sentiment is shifting. Call out
   inflection points with dates.

7. CROSS-VALIDATE. If news coverage and social sentiment diverge, or two
   search terms on the same topic return conflicting pictures, surface the
   conflict rather than silently picking a side.

8. RECOMMEND ACTION EXPLICITLY. Close with lean-in / lean-away / stay-informed
   / ignore per the Mentality framework, tied to the brand's risk tolerance
   and values. Flag it as a judgment call to own if it isn't clear-cut.
```

Then add the specific request underneath.

**Two additions worth making to the request itself:**

State the **window** explicitly, and state it again as a constraint if it reaches before 2026-01-01, so the limitation surfaces rather than being silently worked around.

Name the **decision** the read serves. "Give me a read on X" produces a survey. "Give me a read on X so I can decide whether to fund a launch flight against it" produces an argument.

Require the **fields the downstream check will demand.** Sufficiency is tested once, when the data lands, and that test asks whether each figure supports the claim placed on it. A figure that came back without its denominator or its sample size cannot pass, and by then the pull is over. So specify it in the request: every percentage carries its denominator, every volume carries its window and its distinct-author count where the tool provides one, and every comparison names both sides. Ask here or lose it permanently.

---

## Step 2b — Query spec: for a listening-platform operator

When measurement is needed, produce a spec someone can execute without re-deriving intent. Six parts, all of them.

**1. Window.** Exact dates. If the request involves period-on-period change, name **both** windows and add: *do not compute the change until both periods are pulled on the same term set and channel scope.* A change computed across mismatched pulls is not a finding.

**2. Seed logic, stated as a choice.** This is the part most often skipped and it determines what the pull can possibly see.

> **Seeding on the brand makes everything else invisible.** A Madden-seeded query returns people talking about Madden, so competitors appear at under 1% and lapsed players are absent by definition. That is the query design, not the market.

So state it deliberately:
- **Brand-seeded** — for reading the brand's own conversation. Cannot size competitors or absent audiences.
- **Competitor-seeded, same parameters** — the only way to compare sentiment or negative share against a rival. Run it as its own pull, never as a slice of the brand pull.
- **Unseeded by the brand** — for sizing an adjacent audience. Start from the category (NFL fandom, fantasy football) and measure the brand's organic incidence rate inside it. This is the only design that can answer "does this audience engage with us without being prompted."

**3. Term variants.** One formulation measures the formulation, not the conversation. Include:
- Core brand and product terms, with and without spacing and punctuation variants
- Community vocabulary and shorthand (mode names, in-group abbreviations)
- Common misspellings
- Hashtags, including retired ones
- **Flag any slang you haven't verified** and ask the operator to confirm it's in real use before relying on it

**4. Channel scope.** Name the platforms and, for forums, the specific communities. Say whether comments count as posts.

**5. Output fields.** Be specific about what will answer the question, including the definition. "Unique author count" is ambiguous — say *distinct account IDs, deduplicated per platform, then state whether summed or cross-platform deduplicated.* For any percentage, require the denominator to be stated. Same contract as the agent prompt: the sufficiency test downstream cannot be satisfied retroactively, so anything it will need has to be requested here.

**6. Known contaminants to strip or split.** Where a mechanic inflates a count, name it and require the figure both ways. The worked example: giveaway and sweepstakes posts where entry requires a like, repost and reply inflate post volume and depress per-post engagement. Pattern-match on "like and repost to win," "reply to enter," "RT to win," "giveaway," "sweepstakes," contest hashtags. Report per-post engagement **with and without**, and state the classification rule so it's auditable.

---

## Step 3 — Guardrails on both artifacts

**Researchability triage.** Before a question enters either artifact, confirm the executor can answer it. If it cannot, say so in the deliverable rather than sending it. This is the step that prevents a confident fabrication.

**Evidence floor.** Below tens of independent posts from distinct authors, it is anecdote. Never a finding. Say which it is.

**Re-broaden before declaring a conversation small.** A thin result is a query result until it has been tried another way.

**Divergence is a finding.** If two instruments disagree, that is information about the measurement. Do not reconcile it away or pick a side. Convergence between independent instruments is the strongest evidence available, which is the reason to run both.

**Never blend across tools.** Every number keeps its source attribution all the way to the slide. Two corpora with different definitions cannot be pooled, and a figure from one must never sit beside a figure from the other without labels.

**Never claim significance.** Report the sample size and let the strategist judge sufficiency.

---

## Output format

Deliver as a pasteable block, not prose about a prompt.

- **Agent prompt** — the preamble verbatim, then the request, then the window and the decision it serves.
- **Query spec** — the six parts above under headings, written for a stranger, with a one-line statement of what the pull can and cannot answer.
- **Split requests** — both artifacts, with a line naming which questions went where and why.

Close by naming what neither artifact can answer, if anything. A gap stated is a gap the strategist can plan around. A gap unstated becomes a fabrication.

---

## What this skill does not do

- It does not interpret results. That is `sightly-insights-to-action`, Step 3b.
- It does not run the pull, and it does not advance to 3b. The pull happens outside the session and the workflow waits.
- It does not invent tool names or parameters. The tool surface above came from the agent describing itself; if it appears to have changed, ask rather than guessing.

