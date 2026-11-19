---
name: sightly-audience-architecture-builder
description: Builds the full Sightly audience architecture for a brief — personas, Anticipation Board topic clusters with concrete moment suggestions, and SmartList sample channel/video lists — and outputs both a reusable markdown brief and slide-ready copy blocks. Use whenever a strategist is turning a client brief into audience targeting, building or reframing personas, populating the persona/board slides of a proposal deck, adapting a template deck to a new brand (e.g. "do the WWE version of this," "adapt this to Raymour & Flanigan"), or asks for Anticipation Boards, moment suggestions, or SmartList example lists. Triggers on "build the audience," "who are the personas," "anticipation boards," "smartlist channels," "adapt this deck," "reframe these slides," or any request to turn a brand + brief into audience targeting. Proposal-stage — proposes targeting to be confirmed by a real Persona Builder run and never invents platform numbers. Pairs with sightly-persona-overlap-analyzer once a real run produces targeting data.
---

# Sightly Audience Architecture Builder

## What this skill does

This skill turns a brand + brief into the complete audience layer of a Sightly proposal — the part that drives slides 5 and 6 of the deck and the persona/board/SmartList sections of the proposal email. It produces three coupled outputs in one pass:

1. **Personas** — the fewest personas that cover the audience with minimal overlap, split by *relationship/behavior*, each with a bio, the tension they sit with, the moment that flips them, proposed interest segments, and channel opportunity.
2. **Anticipation Boards** — themed real-time monitors (not static categories), each seeded with 5–8 concrete, market-specific, flight-window-aligned moment suggestions.
3. **SmartList sample lists** — example contextually-curated channel/video lists per persona or board, with exclusions derived from the Block conditions.

It delivers **both** a markdown brief (paste into the deck or email) and **slide-ready copy blocks** (drop straight into the .pptx).

## When this is the wrong skill

- If the strategist wants the **tactics table / line items / budget allocation**, use `sightly-media-plan-builder`. This skill defines *who* and *where*, not the media plan math.
- If a **real Persona Builder run already exists** and the question is whether two personas overlap enough to consolidate, use `sightly-persona-overlap-analyzer`. This skill *proposes* interests to confirm; it does not compute overlap from real run data.
- If the strategist wants full deck copy beyond the audience slides, or a battle card, that's a different job.

## The guardrails that make this skill worth using

These are the exact places the manual version goes wrong. Get these right and the rest follows.

**Scope to the brief's channels, not the template's.** The single most common failure is inheriting channels from the template deck you're adapting. If the brief is YouTube VRC + Display via DV360, do not carry TikTok, CTV, or Demand Gen into the core strategy just because the source deck had them. Park out-of-scope channels as a clearly-labeled *expansion* option, never as a promise. If the brief *is* multi-channel (e.g. YouTube + TikTok + Programmatic CTV), cover every channel it names — don't collapse it to one.

**The brief sets the persona count, and feasibility problems are raised as flags.** When the brief names its audiences, those are the personas: use exactly those, and never trim a client-named audience on your own authority. When the brief names none, build the fewest personas that cover the whole breadth of the audience with the least overlap. Check feasibility on how each platform actually structures lines before raising a concern: a YouTube VRC line optimizes across formats inside one line, so three personas is three lines, not three times the format count. Compare each line's share of budget with the minimums in `05_Budget_Minimums_and_Feasibility.md` (`sightly-media-plan-builder` confirms the numbers). If a line falls short, raise it as a flag with the tradeoff and let the strategist decide.

**Split personas by relationship/behavior, not demographics.** This is what keeps overlap near zero. "Ride-or-Die Fan vs. Nostalgic Returner," "Fresh-Start Furnisher vs. Considered Upgrader" — one is always-on, the other is reactivatable. Two personas that differ only by age or gender will overlap heavily and bid against each other.

**Anti-fabrication is the default.** Every interest tag, channel-opportunity read, and Brand Mentality statistic is a *proposal* until a real run confirms it. Mark them `[confirm via Persona Builder run]` or `[BM run]`. Platform proof points that are stable, sourced and dated in the knowledge base (e.g. 18M+ YouTube videos analyzed daily through 200M+ API calls, always paired with video-level data 400x greater than standard access; 200K+ news and publisher sources; a taxonomy 5x larger than IAB; `02_Voice_and_Terminology.md` › Scale claims, with sources and dates) may be carried as-is. Never invent campaign-specific counts (videos indexed, moment counts, VTRs) — leave them bracketed.

**Use the client's own names.** When the brief names its audience segments, client-facing output uses those exact names. If the strategy consolidates several of the brief's segments into fewer working personas, keep every one of the client's original names visible on the page — nest them, don't replace them. Coining new behavior-led names is for the internal architecture only; it never overwrites a name the client wrote. No insider slang (e.g. "mark/smark"), and any name that does reach the client reads cleanly. The same rule covers anything mapped or numbered: refer to a moment or mapped item by its full descriptive name ("the Thanksgiving travel peak"), never an internal shorthand code ("Moment 2"), in any client-facing or shared output.

**Boards are monitors, not categories.** An Anticipation Board is a live theme that surfaces moments before they peak — seed each with concrete, named examples tied to the flight window (real events, publications, creators, formats), not generic buckets.

## Inputs the skill needs

Find these in the brief, the email thread and the project first. Ask only questions whose answer changes what you do next. Ask them one at a time, in the session's ask-question widget where there is one, with each option explained. Never ask for a due date or a schedule to plan against.

- **Brand + what success looks like** — the campaign goal drives the payoff verb (tune-in vs. purchase vs. sign-ups vs. store visits). Anchor persona and board copy on the *right* action.
- **Brief specifics** — budget, flight dates, **channels in scope**, geo, agency/DSP (e.g. PHD / DV360). Channels and budget together gate persona count.
- **Competitive set** — used to differentiate personas and steer interest weighting.
- **Timing anchor / tentpole** — the moment the flight is built around (SummerSlam weekend, Summer Outdoor Living surge, a sale event, Day Zero). This is usually the spine of the whole story.
- **Source/template deck** — if adapting one, note its structure so slide-ready blocks match, but re-scope its channels to this brief.

If a required input is missing, ask before building. Do not invent budget, flight dates, or channels.

## Workflow

### Step A — Persona architecture (drives everything else)

Use exactly the audiences the brief names. When it names none, propose the fewest personas that cover the audience with minimal overlap, split by behavior/relationship. Check feasibility per line as above and raise any shortfall as a flag; the strategist decides. Persona Builder holds up to 10 personas in production per account, created 5 at a time; check the Agent's `add_persona` limit before relying on it, since the Agent's capability audit (16 September 2026) recorded five per brand. Get the strategist's call before proposing a set that would exceed it.

Each persona uses this structure:

- **Name** — the client's own name for the segment when the brief named it; otherwise client-safe and behavior-led. When the brief's segments are grouped into fewer personas, keep every client name visible in the grouping.
- **Bio** — who they are and their relationship to the category (1–2 sentences).
- **The tension** — the friction that keeps them from the goal.
- **The moment that flips them** — the trigger (often tied to the tentpole).
- **Proposed interests** `[confirm via Persona Builder run]` — Affinity / In-Market / Custom Affinity / Custom Intent segment ideas.
- **Channel opportunity** `[from run]` — where to reach them, scoped to the brief's channels.

Invoking this skill for audience targeting is the strategist's request for targeting detail (`01_Hard_Rules.md` Rule 12; `07_Persona_Standards.md`), so build the full structure above. When the strategist has asked only for personas, deliver each one as a name and a complete description (who they are and their tension, what motivates them, how they spend time with media, and the moments they engage with) and offer the targeting once, naming the platform.

### Step B — Anticipation Boards (per persona)

Build themed boards (typically 2 per persona, or a shared set of ~5 for a two-persona campaign). Each board:

- **Board name** — a live cultural territory the brand has permission to win in.
- **What it monitors** — the behaviors/content it surfaces.
- **Seeded moments (5–8)** — concrete, market-specific, flight-window-aligned examples: named events, publications, creators, content formats. Tie at least one to the tentpole.

Also define **Target / Monitor / Block** conditions where the brief warrants it — these feed the SmartList exclusions and the Brand Suitability story.

### Step C — SmartList sample lists

For each persona or board, propose example contextually-curated channel/video lists — the inventory the buy would run against, refreshed on a stated cadence. Apply Block conditions as automatic video-level exclusions. Keep examples concrete (creator archetypes, publication names, content types), and mark anything speculative as an example, not a guarantee. These are illustrative examples of a list Sightly's SmartList technology builds at scale, from hundreds to thousands of channels and videos; never present them as the list, and never shortlist or cut channels on creator audience data, since age and similar filters are set at campaign level.

## Output

Produce two things in the outputs folder:

1. **`<client>-audience-architecture.md`** — the reusable brief: personas (full structure), boards (with seeded moments), SmartList samples, and Target/Monitor/Block conditions. This is what feeds the deck build and the proposal email.

2. **`<client>-audience-slide-blocks.md`** — slide-ready copy blocks. Match the source deck's slide set. Common blocks, drawn from the standard Sightly proposal arc:
   - **Cover / overview** — intro callout + two bullets (Contextual Segment Build; channel activation scoped to the brief) + metadata panel (flight dates, budget, targeting, geo, DSP, goal).
   - **"What the signals tell us"** — Conversations Driving [goal] / Moments that Open the Window / Conversations to Avoid, with `[BM run]` brackets on any counts.
   - **Persona slide** — the personas with bio, tension, flip moment, proposed interests, channel opportunity.
   - **"Reaching the audience" 1-2-3** — build via Persona Builder → monitor via Anticipation Boards → activate into the client's own seat (self-service) or on their behalf (managed), scoped to the brief's channels.
   - **Tentpole+ (if used)** — main tentpole in the center, niche surrounding cultural moments as satellites.
   - **The persona-universe paragraph** — the content-universe line: "[Persona A] and [Persona B] also show up in [the less obvious content they choose]. Brand Mentality activates across the full [category] content universe, from … to …, that shapes how both audiences decide it's finally time to [goal verb]." Offer a tighter alternate for cramped slides.

Accompany the files with a short narrative: the persona count and why, the channels in scope (and anything parked as expansion), the tentpole anchor, and every bracketed item that still needs a real Brand Mentality run before this goes to client.

## Next step: confirm with a Persona Builder run

The personas, interests, Anticipation Boards, and SmartLists this skill produces are **proposal-stage proposals**, not confirmed targeting. Every interest tag and channel-opportunity read stays bracketed until it is verified.

Before this targeting goes into a committed plan or live campaign:

1. Run the personas through **Persona Builder** to generate real targeting data — YouTube Affinity, YouTube Topics, YouTube In-Market, and TikTok Interests.
2. Once that run exists, check whether any personas overlap enough to consolidate using **`sightly-persona-overlap-analyzer`**. Running near-identical personas separately bids against yourself on your highest-intent (In-Market) signals.

Hand off with every bracketed item called out, so the strategist knows exactly what still needs a real run before client delivery.

## What this skill does not do

- It does not build the media plan / line items — that's `sightly-media-plan-builder`.
- It does not compute persona overlap from real data — that's `sightly-persona-overlap-analyzer`.
- It does not invent Brand Mentality stats, VTRs, or moment counts — those stay bracketed until a real run.
- It does not carry template channels the brief didn't buy.

---

*End of Sightly Audience Architecture Builder skill.*
