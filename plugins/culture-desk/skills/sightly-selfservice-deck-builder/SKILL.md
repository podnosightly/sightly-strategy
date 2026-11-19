---
name: sightly-selfservice-deck-builder
description: >
  Builds the Sightly self-service proposal deck: renders a confirmed Insights-to-Action strategy
  into the built-in five-slide self-service proposal layout (intelligence intro, strategic
  approach, proposal cover, personas, and content universe). The physical layout is fixed and baked into the skill, so nothing needs
  pasting; the narrative arc is built fresh from the live conversation and data each time and
  mapped into the fixed slides. Static build, fluid story. Use whenever a strategist has locked a
  strategy in the conversation and wants to turn it into the deck, build the proposal copy, or "do
  the [brand] version." Triggers on "build the deck," "turn this into the deck," "build the
  proposal," "write the deck copy," "turn the strategy into slides," or a request for slides after
  an Insights-to-Action run. Produces slide-ready copy in the fixed layout; hand to the pptx skill
  for a built .pptx. Not for building the strategy (use sightly-insights-to-action first) or a
  media-plan CSV.
---

# Sightly Self-Service Deck Builder

Turn a confirmed strategy into deck copy. This is the slide-building half of the Insights-to-Action handoff: the strategy is already locked in the conversation, and this skill renders it into the built-in five-slide self-service proposal layout, one slide or a few at a time.

The one idea that governs everything: static physical build, fluid narrative arc. The five-slide layout is fixed and baked into the skill, defined in `references/slide_layout.md`, so nothing gets pasted and the output always drops into the deck in the same shape. What is built fresh every time is the narrative: the story the deck tells, the emphasis, the order of argument, the spine. That narrative is derived from this client's brief and data and mapped into the fixed slides. The containers hold, the story poured through them is bespoke. The spine you rebuild is the story logic, a single-tentpole idea that does not fit an always-on product, never the physical layout.

## Before you start

**Required input: the confirmed Insights-to-Action lock file** for this client (`<brand>_insights_to_action_CONFIRMED.md`), holding at minimum the positioning tension, the personas (one per cluster), the priority moments, and the chosen argument. If it doesn't exist, stop and route to `sightly-insights-to-action` to write it. Do not invent strategy inside a slide.

**The layout is built in, not pasted.** The five-slide physical build lives in `references/slide_layout.md`. Read it before writing. The strategist does not need to paste a template. If they choose to paste a different template or ask for a different structure for a specific deck, follow that for that deck; otherwise the built-in layout is the build every time.

If the Culture Desk knowledge base is in the project, these govern the copy and must be read first: `01_Hard_Rules.md`, `02_Voice_and_Terminology.md`, `08_Proof_Points_and_Battle_Cards.md`, `07_Persona_Standards.md` and `13_When_Asked_to_Build.md` › Decks and proposal copy. The rules below summarize what matters most for deck copy, but the knowledge base is the source of truth if present.

## Grounding gate: look at the real deck before you write (required)

If there is an existing deck in play (the live deck you are revising, extending or adapting for "do the [brand] version", or a template the strategist pointed to), look at it before writing a word of copy. A text dump of a deck (markitdown, an export, a paste) drops the layout, the visual emphasis, what each element actually is, and whether a number is a hero stat or a footnote. Treating "I have the text" as "I understand the slide" is the specific failure this gate exists to stop, and it is what produces an invented deck arc, a wrong format, and copy that does not match what is already built.

The gate, in order:

1. Render every slide of the existing deck to an image and actually view it. In this environment that means exporting or rendering to PNG (or opening the live deck in present mode) and looking at the images.
2. Write a one-line-per-slide inventory before any copy: for each slide, what it is (its role) and what it is doing (the job it performs in the argument). Note which slides already carry the moments, personas, proof, and any tentpole or section content, so you extend what the deck already carries. Capture the real visual system too (background, gradient, accent marks, fonts) so any new slide matches what is already there. Check any template or exemplar for retired terms (YTMP language, a trademark symbol after SmartLists) and report a defect against the template.
   Count every slot on each slide (bullets, cards, tiles, fields) and its length, and write to exactly that count and length. If a slide's structure doesn't fit the content (a one-persona slide when there are two personas), flag it so the strategist can supply the right template slide; don't cram the content in.
3. Only after that inventory exists do you write or revise copy. No copy before the inventory. If you cannot render the deck, say so and have the strategist confirm the slide-by-slide reality before you write. Do not proceed from a text dump alone.

This is the same discipline as the anchor-inventory pass below, pointed at the existing artifact instead of the strategy: ground in what is actually there before you produce.

## Guardrails that apply to every slide

**Build the narrative from the tension, do not inherit a default spine.** The fixed layout is a set of containers, not a story. The most common failure is letting a prior campaign's story logic ride along in those containers. A spine built for a single-tentpole appointment product (one big live moment, a weekly tune-in cycle) will fight an always-on access product, and the reverse is also true. Build the story logic fresh from this client's tension and argument, and when a carried-over spine does not fit, replace it. This is a narrative operation inside the fixed slides, never a change to the layout. Name the replacement to the strategist so they can sanction it.

**Every line traces to the confirmed strategy or the verified data.** No new claims invented at the slide stage. If a line needs a figure that is not in the data, flag the gap rather than filling it. Be ready to show the anchor for any line: which persona, moment, pillar, or data point it rests on.

**Scope copy to the actual buy.** If the buy is display only, strip video, CTV, and YouTube activation copy from the template even when the template leads with it. If a channel is not in the plan, it is not in the copy. Let the format the strategist confirmed decide what stays.

**Trust the data, then test what it is being asked to prove.** Stats the strategist provides from Brand Mentality outputs are pre-verified as real and correctly measured. Use them directly; do not hold them out or hedge them. Two things still have to happen. **Attribution:** when a figure is third-party in origin (viewership numbers, subscriber counts, platform view counts, external research that Brand Mentality surfaced rather than generated), carry its source label on the slide so it holds up under a skeptical agency read. **Sufficiency:** before a figure goes on a slide, check that it supports the specific claim the slide makes with it, because a real number can still fail to carry the sentence built on it. Run that check once; whatever passes is settled and is not re-opened. Sightly's own proof points carry their own attribution, but check each against the project's do-not-use register rather than treating any as drop-in ready; the current approved set and the do-not-use list are in `08_Proof_Points_and_Battle_Cards.md`, and the `sightly-brand-voice` reference is a portable copy that follows `08` where they differ. Never invent a figure or a source; if a line needs a number that was not provided, flag the gap rather than filling it.

**Case studies and platform images.** Case-study slides draw on Sightly's Case Study Matrix sheet (https://docs.google.com/spreadsheets/d/1VSndHvH3CuEek2zExrfcrYF2pHuPiyTWberQiYCnMLA). Images from Sightly's own platform (moment cards, thumbnails, SmartList and Persona Builder screenshots) go in unaltered and never blurred; Sightly has every right to show them.

**Placeholders for pending inputs.** Budget, CPM, and unconfirmed dates get a bracketed placeholder such as `[Budget: TBD pending confirmation]`, never a guessed value. Rates come from the rate hierarchy and are confirmed by the strategist.

**Results and pricing.** When the strategist uploads a wrap report for results, follow `13_When_Asked_to_Build.md` › Results from wrap reports. Label bid guidance and self-service fees as `02_Voice_and_Terminology.md` › Bid guidance and self-service fees are different things sets out, with figures from `08_Proof_Points_and_Battle_Cards.md` › Self-service bid guidance and › Self-service pricing (internal reference only).

**Hard Rules terminology, every slide.** SmartLists and Anticipation Software always plain, with no trademark symbol or ®. Brand Mentality® once, at its first mention in the proposal (the Intelligence Intro opener in `references/slide_layout.md`, unless a slide placed before it names Brand Mentality; that slide then carries the ® and the opener is plain), and plain everywhere after (Rule 24). "Brand Suitability" as the default; "brand safety" is permitted where the client or RFP uses it or where it is the clearer word; otherwise match the client's language and don't volunteer it. YouTube = "Google Premier Partner" with "Non-Public API Access", never "YTMP" or "YouTube Measurement Program". "Social Intelligence" not "social listening." No GARM references. Never name **Sightly's** competitors (Pixability, Channel Factory, Zefr, OpenSlate, VuePlanner, CreatorIQ, Tubular Labs, Wizdeo, Sprinklr and other ad-tech, suitability, contextual, measurement or social intelligence vendors) in client-facing work; use "other offerings in the market." IAS and DoubleVerify can be named as third-party verification integrations that Sightly works alongside, never as competitors (Rule 9). This does not apply to the advertiser's own category competitors: name them in sentiment analysis, Brand Mentality pulls, share-of-voice, competitive-landscape and conquesting work, internal or client-facing. Never name white-label partners. Never use "programmatic" in Spotify materials. IRIS.TV and Spectrum Reach can be named, always leading with Sightly. Transmit Live is a white-label partner and is never named client-facing. Never frame Sightly's size as a limitation. Never position Sightly as insight-only; it is always activation-led. Never describe a one-click SmartLists push into DV360: the one-click destinations are Google Ads, OpenX and Media.net.

**Voice, every slide.** Lead with the point in the first sentence. One job per sentence. Specific beats generic. Bullets are full sentences, and any bold sits on a real data point or named behavior inside the sentence, never as a front label. Strategy and persona slides run roughly 80 to 130 words; cut past 140, and thin under 40 is too light for the argument. No AI tells: no em dashes for rhythm, no negation-pivots in any form (including "not just X but Y," "it's not X, it's Y," "X, not Y", "X rather than Y" and the version split across two sentences), no "that's why / that's how" pivots, no triplet headlines, no throat-clearing openers, and no small section label (an eyebrow) above a slide title. **Every sentence carries a specific:** a grammatical, on-voice sentence that names no mechanism, number, behavior, or consequence is filler, and it survives precisely because it trips no banned pattern. Cut it or rewrite it to name the actual point.

**Consistency with the approved strategy.** The persona set, the channel weighting, and the argument on the slides match what was locked in Insights-to-Action. If a template tempts a change to any of them, raise it rather than quietly drifting.

---

## Data-Faithfulness Gate: anchor every slide to Insights-to-Action (run before and after each build)

The one failure this prevents: a clean visual idea quietly overriding what the data established. A punchy hook is worth nothing if it changes the finding. The strategy is the master and the slide serves it. This gate is separate from the no-orphan rule below, which checks lines. This gate checks the whole slide's framing.

**Before proposing any slide concept:**

1. Open the confirmed Insights-to-Action lock file for this client (`<brand>_insights_to_action_CONFIRMED.md`, kept by `sightly-insights-to-action` from Phase 1 and complete at Phase 3; look in the project first). If it does not exist, stop and get it written first. Build from the file. Memory drifts; the file does not.
2. Restate, one line each, the load-bearing structure the deck must honor: the positioning tension, the exact cluster/persona count with each one's name and motivation, the priority moments, and the chosen argument. This restatement opens the anchor inventory below; show both to the strategist together, before any concept, at the one stop in "Plan the narrative".
3. Test the concept against that restatement. The concept must express the full structure. If the concept only works by changing the count, or by collapsing, merging, or renaming clusters or personas, that is a strategy change. Stop and flag it; do not ship it.

**Count integrity (the specific trap).** The number of personas, clusters, or segments a slide shows must equal the confirmed count. If a headline or metaphor reduces several motivations to one, or expands one into several, it has drifted, even if it reads well. A metaphor or single-number hook is allowed only if the underlying count and definitions stay intact. If you have to bend the data to make the hook land, cut the hook.

**After building each slide, check the slide as well as its lines.** Re-check the whole slide's framing against the lock file. Ask whether the story the slide tells matches the finding or a cleaner-sounding version of it; a slide can have zero orphan lines and still misrepresent the structure. In the "what changed and what to check" note, name what you checked the slide against and any point where the concept was tempted to drift and was pulled back.

**Worked examples of the drift this catches:**

- Hook "it's one man" for an audience the data defines as three distinct motivational clusters. Reads well, wrong finding. Fix: show three people plus the crossover as a layer, matching the three-cluster structure.
- Describing a confirmed "3 clusters + layer" architecture as "2 clusters + layer" after a persona was reclassified. Quietly changes the count. Fix: re-read the lock file and keep the count the strategy locked.

If this gate conflicts with a copy or design instinct, the data wins. Rewrite the slide and keep the finding.

---

## Plan the narrative before you build any slide

Do this first, before writing a single slide. Writing slide by slide with no plan is how the most important points end up vaguely referenced or dropped, and how orphaned claims slip onto slides. This pass is where the fluid part of the work happens: the narrative arc, the story the deck tells across the fixed five slides. It is built off this client's strategy and data, not carried over from a prior campaign.

**1. Confirm the build, then design the arc inside it.** The five slides in `references/slide_layout.md` are the fixed core of a self-service proposal, in this order: never drop or reorder them. A self-service proposal runs longer than five slides, and the rest of its structure comes from the RFP's required sections or the strategist's example deck (`13_When_Asked_to_Build.md` › Where the structure comes from); add a slide only where one of those calls for it, and confirm each addition with the strategist. The design work is the narrative arc that runs through them: what the throughline is, where the argument escalates, which tension and moments lead, how slide 1 sets up what slide 5 lands. That arc is bespoke each time. Build it from the confirmed strategy, not from how a previous deck happened to tell its story. The narrative arcs in `13_When_Asked_to_Build.md` › Narrative arcs (answer-first, Challenger, moment-led, proof-led, problem-solution) are useful reference for the story; recommend one with its reason and let the strategist pick.

**2. Build the anchor inventory.** List the load-bearing elements from the confirmed Insights-to-Action output before writing anything:

- The tension, the spine every slide serves
- The chosen argument and its runners-up
- Each persona, with its defining tension and mapped moments
- The priority moments, primary and reactive, not the full list
- The specific data points and proof points that carry weight, each with its anchor, and its source label if the figure is third-party in origin

Rank each element must-include, supporting, or appendix. The must-include set is what the deck has to land. The appendix set is what explicitly does not get slide space, carried over from the Insights-to-Action appendix discipline. Ranking now is what stops an important point from being reduced to a vague gesture later.

**3. Map each must-include element into the five fixed slides.** Decide the cumulative argument: how the story builds across the five slides so the reader arrives at the recommendation, not a pile of facts. Assign every must-include element to the slide where it lands hardest, using each slide's job from `references/slide_layout.md`. This is where the narrative arc gets built, inside the fixed layout. If the must-include set genuinely will not fit five slides, do not silently add a sixth. Surface it to the strategist as a decision: tighten the set, or add a slide by choice.

**4. Run the coverage check, before writing.** Two directions:

- Every must-include element has a home in the five slides. If an important point has no home, or would only be vaguely referenced, fix the mapping before writing copy, not after.
- Every one of the five slides has a clear job in the story. If a slide has no strong content to carry in this campaign, do not drop it. Flag it to the strategist, since changing the fixed build is theirs to decide, not the skill's.

Present the mapping plan and the anchor inventory to the strategist and stop here. The strategist confirms which points land on which of the five slides, and the must-include set, before slide building starts. Confirming the plan first is what keeps the build a fast, predictable step rather than a rework.

### The no-orphan rule

Every line of slide copy must trace to a specific element in the anchor inventory: a persona, a moment, the tension, the argument, or a named data point. A line with no anchor is an orphan. Cut it, or ground it in the data. Never leave a claim on a slide that nothing supports. Check this twice: once while mapping the arc, to confirm every important point is covered, and again after writing each batch, to confirm every line has an anchor. The second pass checks at the line level that each slide earns its place, and it is where a sentence that reads well but rests on nothing gets caught.

"Not vaguely referenced" has teeth. Name the actual moment, the actual behavior, the actual figure. "Around the season's key moments" is a vague gesture. "The MLB postseason into the World Series, inside this flight" is anchored. Specific beats generic, on every line.

---

## The five slides

The physical layout, the fixed lines, section headers, field labels, and per-slide copy logic, is defined in full in `references/slide_layout.md`. Read it before building. In short, the five slides in order are the Intelligence Intro (what Brand Mentality surfaces and what it unlocks), the Strategic Approach (three moves plus the intent-peak and Sightly supply lines), the Proposal Cover (title, frame paragraph, spec block, build and activation bullets), the Personas (one block each on tension, the flipping moment, and where to reach them), and the Content Universe (the full content world the audiences engage). Build each one to the fixed structure in the reference, filling it with this campaign's narrative.

---

## Working process

Build the five slides in order, one or a few at a time, so the strategist can review as you go. Build the slides for the confirmed plan; do not jump ahead of what has been confirmed.

After each batch, always end with a "What changed and what to check" note beneath the copy. This note is mandatory, not optional, because it is how the strategist keeps control of the narrative decisions the skill made. List every material move: each spine that was replaced and why, any channel or DSP copy scoped to the buy, every placeholder standing in for a pending input (budget, CPM, dates), any third-party figure carried onto a slide with its source label, and any must-include point that could not be placed or any line cut as an orphan. If none of these occurred in a batch, say so in one line rather than dropping the note.

Deliver the copy as clean, slide-ready blocks in the chat by default, matching the fixed structure so it drops into the deck without reformatting. This skill produces copy, not a file.

---

## Final step: the check before handover (required)

Before the copy is handed off, run the quick check before handover in `13_When_Asked_to_Build.md` › The check before handing it over: one pass over the brief, numbers, rules and voice, and feasibility, fixing what a client would notice and putting two or three lines in the handover. Use that check by default. When the strategist asks for the full on-brand pass, run steps 1 to 3 below after the slide copy and layout are produced.

**1. Written voice — run the copy through `sightly-brand-voice`.** Check all slide copy (and the client-facing email if one was drafted) against the codified written voice: tone, the enforced copy rules, banned patterns (no em dashes for rhythm, no negation-pivots in any form, no eyebrow labels, no pipeline words, no triplet headlines, no throat-clearing openers, no bold-label bullets), approved vs. prohibited terminology (Brand Suitability as the default, "brand safety" only where the client uses it or it is the clearer word, Google Premier Partner never YTMP, Social Intelligence not "social listening," SmartLists and Anticipation Software plain, Brand Mentality® once at its first mention in the proposal and plain after, no GARM, no names of Sightly's own competitors or white-label partners (IAS and DoubleVerify may be named as verification integrations); the advertiser's category competitors are named), and that every claim traces to a citable proof point.

**2. Visual system — run the visual output through `sightly-visual-brand`.** Check the deck's design against the canonical tokens: brand colors (Sightly Blue #00AEEF, the steel/slate surfaces, the accent purple/orange/teal), the signature hero-sweep gradients, the Inter type scale, and the recurring components (stat callout, persona block, content universe). Flag any off-canon color (for example a near-duplicate cyan), any non-Inter font, or any off-system component. Every deck is in dark mode, including decks for existing clients. Flag any eyebrow label above a slide title.

**3. Report violations with fixes, then hand off.** Produce a short pass/fail list: each violation found, the rule it breaks, and the corrected version. Do not hand off until the copy and visuals pass, or the strategist has explicitly signed off on each exception.

If `sightly-brand-voice` and `sightly-visual-brand` are not installed in this session, apply the equivalent rules directly from `02_Voice_and_Terminology.md` and the Sightly design tokens, and say so in the report.

---

## Handoff to a built deck

This skill ends at slide-ready copy in the fixed five-slide structure, cleared through the check above. When the strategist wants the built deck, build it as a Slides artifact if the session offers that type, so they can edit it and export .pptx or PDF; otherwise hand to the `pptx` skill. Apply polish fixes (corner radii, alignment, spacing) as part of the build; don't offer them as follow-ups. Hand off with the confirmed copy and the Sightly design tokens from `sightly-visual-brand` (`references/design-tokens.json`: dark mode on #000000 / #111111, Sightly Blue #00AEEF, Mentality Purple #7B61FF, Mentality Teal #6FEABC, Sightly Orange #FF6F07, Inter, 16:9; 720 x 405 pt for .pptx), and note that the copy is locked so the deck build is layout and formatting, not a rewrite.

---

## Example: spine replacement inside the fixed layout

The layout holds; the story logic gets rebuilt. Same slide, same slot (the intent-peak line on the Strategic Approach slide), different spine.

**Carried-over spine (single-tentpole tune-in product):**
Intent peaks around live events. For wrestling, that peak is SummerSlam weekend, live inside this flight.

**Rebuilt for an always-on access product:**
Intent peaks around live games and access breakdowns. Across this flight, that means the season opener, the postseason, and every blackout or out-of-market moment in between.

The structural line is identical, the intent-peak line the layout always carries. What changed is the story underneath: one dated peak became a recurring, moment-triggered rhythm, rebuilt on the moment map rather than pointed at a single tentpole this client does not have.
