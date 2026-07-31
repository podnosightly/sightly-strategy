---
name: sightly-insights-to-action
description: >
  Runs Sightly's Insights-to-Action methodology on verified Brand Mentality data plus a client
  brief to produce a gated proposal strategy: brand pillars, the positioning tension, a
  conversation landscape classified Active/Emerging/Seasonal, motivation-based audience clusters,
  data-anchored personas, a moment map with always-on and reactive signals, the strongest
  argument, and slide-ready strategy narrative. Use whenever a strategist has Brand Mentality
  data, an Anticipation Board export, or social or competitive intelligence with an RFP or
  campaign brief and wants strategy, personas, moments, positioning, or narrative. Trigger on 'run
  insights to action', 'phase 1/2/3', 'turn this Brand Mentality data into strategy', or 'develop
  personas from this data', even if unnamed. Not for building a media-plan CSV or line items,
  checking existing Persona Builder lists for overlap, summarizing one document, or filling slide
  templates without first building the strategy. Stops at each phase, then requests slide
  templates.
---

# Sightly Insights-to-Action

Turn verified Brand Mentality® data and a client brief into a proposal strategy, one confirmed phase at a time, then hand off to slide building. This mirrors the Sightly execution chain: Brand Profile (Phase 1) → Anticipation Boards and SmartLists™ (Phase 2) → Activation Manager and media (Phase 3).

## Before you start

Confirm you have both inputs. If either is missing, ask for it rather than guessing.

**If the Brand Mentality data does not exist yet, do not just ask for it — go build the request.** That is Step 3a, `sightly-mentality-prompt-builder`, which routes the question to the right executor and writes either an agent prompt or a listening-platform query spec. This skill is Step 3b and cannot start until the pull returns. Improvising a read from press coverage or general knowledge while waiting is the exact failure both skills exist to prevent.

1. **Verified Brand Mentality® data** — Brand Profile output, Anticipation Board moments and narratives, social/competitive intelligence, targeting exports, or similar. The strategist should confirm the data is verified. Once confirmed, its provenance is settled — do not re-audit it or hedge it later. What that confirmation does *not* settle is sufficiency: whether a given figure supports the specific claim you build on it. Test that once, here, before Phase 1 proceeds, and record anything that fails.
2. **The client brief** — at minimum: client, brand(s), objective, budget, geos, flight dates, target audience, platform preferences or constraints, and any hard client asks (for example "self-service only", "anti-news", named partnerships).

If the Culture Desk knowledge base is available in the project, read these first; they govern everything downstream: `19_Insights_to_Action.md`, `04_Hard_Rules.md`, `02_Sightly_Brand_Voice.md`, `07_Persona_Standards.md`. The rules below are the working summary, but the knowledge base is the source of truth if it is present.

## Guardrails that apply the whole way through

**Anchor everything to the positioning tension from Phase 1A.** The tension is the spine. If a data point does not advance it, the data point goes in the appendix, not the narrative. State this discipline out loud and apply it in every phase.

**Every statement must be anchored in the actual provided data.** No industry-standard hand-waving, no borrowed claims. When you present findings, show the anchor: which specific figure, post count, narrative, or segment each claim rests on. If a needed number is not in the data, say so and flag the gap. This is the difference between strategy and decoration, and it is what the strategist will check first.

**Never fabricate.** No invented rates, CPMs, benchmarks, proof points, or competitive claims. Rates are deal-specific and strategist-provided; comparison benchmarks must be researched from current, cited sources and framed as benchmarks, not Sightly's deal rates. If a case study or proof point is requested and none exists in the data, flag it rather than inventing one.

**Hard Rules terminology for anything client-facing.** "Brand Suitability" not "brand safety"; "Social Intelligence" not "social listening"; Brand Mentality®, Anticipation Software®, SmartLists™ with their marks. Never name competitors in client-facing work (use "other offerings in the market"). Never name white-label partners. Never use "programmatic" in Spotify materials. IRIS.TV and Spectrum Reach can be named, always leading with Sightly. Transmit Live is a white-label partner and is never named client-facing. Never frame Sightly's size as a limitation, and never position Sightly as insight-only — it is always activation-led. If no BAV equity data is provided, frame the tension in plain strategic terms; do not invent a BAV quadrant.

**Stop at every phase gate, and label what you are asking them to approve.** Present the phase, then wait for the strategist to confirm or adjust before moving on. This is a partnership, not an assembly line. Do not race ahead to the next phase or to slides.

Every gate carries a short **claim ledger** so the strategist knows what kind of statement each one is before signing off. Mark every material claim as **sourced** (traceable to the data or the brief, with the source named), **computed** (derived from sourced inputs, with the derivation stated), or **judgment** (your strategic read, defensible but not evidenced). Sign-off is on epistemic status, not on prose. If a phase rests mostly on judgment, say so plainly rather than letting a confident register imply evidence that is not there.

**Flag before you deliver.** Budget feasibility, geo spread, flight timing, platform minimums, scope mismatches (for example a brief that names two brands but supplies data for one), and strategic flaws all get surfaced up front, not buried at the end.

**Re-read your own findings before you start persuading.** The moment this skill switches from analysing data to writing narrative, stop and re-read every flag, caveat and exclusion the session has already produced, then restate them. Findings do not survive a change of register on their own: a confound written into an audit file twenty minutes ago will not be remembered by the paragraph that wants the number. Before any narrative or slide copy is written, state the project's do-not-use list explicitly, read from the file if one exists rather than from memory of the conversation.

---

## Phase 1 — Insight Extraction and Synthesis

Objective: turn raw data into a structured intelligence picture. Stop after this phase.

**1A. Brand intelligence.** Distill the Brand Profile into 3-5 core brand pillars that will govern downstream targeting. Then name the positioning tension: where the brand sits today versus where it needs to move. This single statement becomes the anchor for the entire response. Map the brand's values to the content categories in Sightly's taxonomy that represent natural alignment, and note the categories that work against the tension.

**1B. Cultural and conversational landscape.** From the Anticipation Board moments and narratives plus any other intelligence, identify the top 5-8 active conversations relevant to this brand and objective. Classify each as **Currently Active**, **Emerging** (within 2-4 weeks), or **Predictable Seasonal**. Tie each one to the tension. Anything off-thesis goes to the appendix, named as such.

**1C. Audience clusters.** Identify the *fewest* clusters that cover the entire breadth of the target audience while minimizing overlap between them (usually 2-4). Build them on behavior and motivation, not demographics. A reliable test: if a candidate cluster is defined by an *occasion* (game day) or an *intent state* (on-the-go, hungry now) rather than an intrinsic motivation, it probably is not a standalone cluster. It overlaps everything and should be treated as a cross-cutting layer applied across the real clusters, not counted as one. For each cluster, note what they care about, how they consume content, and which content signals would reach them.

Present 1A, 1B, and 1C with the claim ledger, then stop for review.

---

## Phase 2 — Moment Identification and Opportunity Mapping

Objective: turn insights into targetable real-time moments and personas. Anchor everything to the Phase 1A tension. Stop after this phase.

**2A. Moment map.** Build 8-15 targetable moments organized by type: Cultural Events (scheduled), Trending Conversations (real-time), Seasonal Patterns (recurring), Competitive Windows (gaps in competitor activity), and Brand-Owned Moments (launches, milestones). For each: name it, classify it, estimate its timing window, map it to the audience clusters, and rate its priority (Primary, Secondary, Reactive). **Be time-aware:** check today's date and do not anchor the plan to a tentpole that has already passed or falls outside the flight. Name the near-term tentpole that actually lands in the window; if flight dates are unconfirmed, say so and leave the specific tentpole to confirm.

**2B. Personas.** Develop one persona per Phase 1C cluster using Sightly persona standards: name, short descriptor, motivations, behaviors, interests and affinities, content signals, and audience traits ready for activation. **Anchor persona names to the data** — do not assert a brand fact that is not in the dataset just because it is a well-known product truth. Map each persona to its primary and secondary moments.

**2C. Signals.** For each persona, define always-on signals (persistent targeting) and reactive signals (triggered when conversation hits roughly 2-3x baseline). Anchor the reactive triggers to the actual spike types the data shows, not invented events.

**Then name the argument.** State the single strongest strategic argument this data supports, plus two runners-up, each with its tradeoff. The strongest argument is usually the one that resolves the client's hardest explicit asks using the capability competitors cannot replicate (the real-time Anticipation Board → SmartLists → Activation Manager chain). Present it plainly, with the claim ledger. Stop for review.

---

## Phase 3 — Activation Strategy and Narrative

Objective: translate moments and personas into deployable strategy and slide-ready copy. Anchor everything to the Phase 1A tension; every data point must earn its place against the chosen argument, or it goes to the appendix. Stop after this phase.

Write three things:

1. **Strategy Overview narrative** (2-3 paragraphs) — the argumentative backbone of the deck.
2. **Channel-by-channel rationale** — one tight rationale per channel. **Weight channels by where the data actually shows engagement,** not by template habit. If the strongest signal is short-form social content, do not center the plan on live/CTV inventory just because a past deck did. Let each platform's role follow the data.
3. **Why Sightly** — positioning specific to this client, built on the activation chain, and on the self-service tooling if the brief is self-service. Tie it back to the client's hardest asks.

Flag any gaps honestly: missing case studies (do not invent them), rates to confirm, and the appendix list of data points that did not earn a place in the narrative. Stop for review with the claim ledger.

---

## Handoff — Slide Template Adaptation

Once Phase 3 is confirmed, the strategy is done and the deck build begins. **Do not invent a slide format.** Ask the strategist for their templates:

> "Strategy's locked. To build the deck, paste in the slide templates from a previous campaign you'd like to adapt, and I'll repurpose them for this client. Send one or a few at a time and I'll work through them."

When templates arrive, treat them as a **creative guide to the format, not a fill-in-the-blank.** Rebuild the content from this client's strategy and data. For every adapted slide:

- Anchor every statement in the actual data, and be ready to show the anchor for each line.
- Do not carry over the previous client's spine if it does not fit. A template built for one kind of product (say, a subscription channel with live-appointment tune-in) will impose logic that may not match this client. Rebuild from the tension and the argument, not from the old client's assumptions.
- Use client-facing language and the Hard Rules terminology.
- Avoid obvious AI tells: no em dashes, no "not just a" constructions.
- Keep the persona set and channel weighting consistent with the approved strategy.

This handoff is where the skill ends and interactive slide work begins.
