---
name: sightly-qa-gate
description: >-
  When the RFP orchestrator or another skill hands over a finished RFP deliverable (deck copy, media
  plan, persona framing and client email), runs the quick check before handover from the Culture
  Desk knowledge base: one pass over the brief, numbers, rules and voice, and feasibility, fixing what
  it finds and telling the strategist in two or three lines what changed. When the strategist invokes
  it directly or asks for the QA gates, runs Sightly's full QA gates instead, with a pass or fail per
  gate and a fix for each finding; in a full run it holds handoff to sales on any failed gate. Triggers on "QA this proposal",
  "run the QA gates", "is this ready for handoff", "check this before sales", or "quality check this
  deck". Reads 13_When_Asked_to_Build.md, 01_Hard_Rules.md and 02_Voice_and_Terminology.md from the
  knowledge base if present. Not for writing the deck (sightly-selfservice-deck-builder) or
  building the plan (sightly-media-plan-builder).
---

# Sightly QA Gate

**Which run to use.** When the RFP orchestrator or another skill hands a deliverable over, run the quick check before handover in `13_When_Asked_to_Build.md` › The check before handing it over: one pass over the brief, numbers, rules and voice, and feasibility. Fix every instance of what a client would notice, and tell the strategist in two or three lines what changed, any assumption they need to confirm and any open decision. Use that check by default. When the strategist invokes this skill directly or asks for the QA gates, run the full gates below.

**The full gates.** Run every finished RFP deliverable through all five quality gates before it goes to sales. Each gate returns pass or fail with specific findings. **No gate can be skipped, and any failed gate blocks handoff** until the strategist resolves it.

## In a full run, this is not only a Step 9 skill

QA used to run once, at the end. That is too late. By the time a deliverable is finished, a wrong figure has already been written into a plan, a deck and an email, so fixing it means fixing three artifacts instead of one, and the version the strategist remembers is usually the wrong one. Run the gates that apply as each artifact is produced, then run all five before handoff.

- **Any step that produces a number** — rates, feasibility, allocation, audience size: run Gates 2 and 3 on it at that step.
- **Any step that produces client-facing copy** — strategy narrative, persona framing, slide copy, the client email: run Gates 1, 2 and 4 on it at that step.
- **Before handoff** — run all five across the whole set. Gate 5 is the only one that genuinely needs every artifact present.

A gate run mid-build reports and blocks exactly as it would at the end. An unresolved Gate 2 failure at Step 7 blocks Step 8; it does not get deferred to Step 9.

Inputs: the deck copy, the media plan, the persona framing, and the client-facing email — as complete as they exist. If the Culture Desk knowledge base is present, read `13_When_Asked_to_Build.md` › The check before handing it over, `02_Voice_and_Terminology.md`, `01_Hard_Rules.md` and `08_Proof_Points_and_Battle_Cards.md` (its do-not-use list) first as the source of truth; the checks below are the working checklist.

## Before the gates — read the do-not-use register

**Find the project's do-not-use register (`active-<brand>-do-not-use-register.md`, in the project or the outputs folder) and read it before running a single gate.** Ask for it only if you can't find it. State what it contains, by item. If there isn't one, say so explicitly and treat every figure in the deliverable as unverified for Gate 2 — an absent register does not mean nothing was ruled out.

Anything a session already flagged is a **prohibition, not context**. A figure ruled out in an audit does not become usable because the session has since moved on to persuasive writing. That switch from auditing to selling is the most common point of failure, and it is why this lookup runs first rather than inside a gate.

## How to run it

Run all five gates in order. For each, produce a **PASS** or **FAIL**, and for every issue: quote the offending text, name the rule it breaks, and give the corrected version so the strategist can approve the fix fast. Present findings to the strategist — not just a pass/fail indicator. End with an overall verdict and a blocked/clear-for-handoff call.

## The five gates

**Gate 1 — Voice & AI-tell.** Does the output follow `02_Voice_and_Terminology.md`? Check: no em dashes for rhythm, no triplet patterns, no negation-pivots in any form ("not just X but Y," "it's not X, it's Y," "X, not Y," "X rather than Y," and the version split across two sentences), no internal pipeline words in client copy ("the pull flagged," "discovery pass," "mid-window"), no eyebrow labels above slide titles, no throat-clearing openers, no "X. Y. Z." headlines, no fragment stacks, no bold-label bullets, no hollow intensifiers; strategy/persona slides within 80–130 words; setup-then-payoff on each slide; no orphan words; no "guaranteed 100% VCR" or "100% completion" on non-skip or bumper formats; "sizzle", never "scissors"; no client-facing point made by naming a limitation (state it from the gain side, keeping the mechanism or number). *Run the copy through `sightly-brand-voice` if installed.* Flag every instance with a fix.

**Gate 2 — Number, source & sufficiency.** Does every number trace to a source, does it support the claim attached to it, and does the plan hold up? Sourcing and sufficiency are separate tests and both can fail independently — a correctly-sourced figure can still fail to carry the sentence it has been placed under, and that is a Gate 2 failure, not a style note. For every number, state the claim it is being used to make and whether it carries that claim. Apply the same test to non-numeric assertions: any sentence asserting a state of affairs needs something behind it, and "owns its category" fails this check as surely as an unsourced percentage does. Check: every CPM, benchmark, persona stat, and tactic cites a source; numbers trace to the media plan or brief; no invented data points; CPM accuracy audit (rates realistic for platform/format/targeting); buying-methodology validation (auction vs. reservation, CPM/CPV/CPC correct per line); rates trace to the rate hierarchy (the deal's rate card, delivered rates, prior Sightly plans and the rate library, a cited external benchmark labeled comparison) and match what the strategist confirmed; impressions recompute as budget ÷ CPM × 1,000; dates, lead times and derived figures have a source or are labeled an assumption next to the figure; two-pass verification (check numbers, then re-check from a different angle). Check every figure against the do-not-use register before passing it. Flag every unsourced or off-looking number.

**Gate 3 — Brief alignment & feasibility.** Does it match the brief and can it run? Check: recommendation aligns to stated objectives; budget allocations supported by platform minimums; flight length supports the tactics; geo strategy realistic for the budget; all platforms/formats operationally feasible; nothing the structure can't support; every line clears $100 a day ($50 for underfunded local markets); no floor is quoted for a row with none documented; minimums are checked by kind, with platform-enforced minimums as hard stops and Sightly's recommended minimums flagged and confirmed case by case with Account Management and Performance Management; each format is graded on a KPI it can move (bumpers carry no VCR or CPCV; non-skip and VRC report VCR as a delivery metric, with unique reach against the target demo as the primary KPI); reservation lead times are documented or flagged as undocumented; any lift study is checked against the buffered net minimum, with the plan's spend in the window converted to net at the deal's margin, and the non-Demand-Gen spend in its 10-day window, counting only lines Brand Lift can measure (Video campaigns; audio runs as its own audio-only study; display and Performance Max can't be measured). State each misalignment and the specific constraint behind any feasibility failure.

**Gate 4 — Compliance & hard rules.** Have all hard rules been followed? Check: every rule in `01_Hard_Rules.md`, searched for one at a time; no white-label partner names client-facing; no names of Sightly's own competitors client-facing (the rule is scoped: the advertiser's category competitors are named whenever the work calls for it, and refusing to name them is the error; IAS and DoubleVerify named as third-party verification integrations are fine, and named or compared as competitors they are a violation); no retired YTMP language ("YouTube Measurement Program," "YTMP," "1 of 7 badged partners" are a hard fail); "brand safety" is not a violation, so raise it only as a positioning note where it is volunteered and Brand Suitability fits better; correct terminology throughout (Social Intelligence not "social listening"; SmartLists always plain, so a trademark symbol on SmartLists is a violation; Brand Mentality® exactly once, at its first mention in a proposal, and plain everywhere else, so a second ® is a violation; Anticipation Software always plain, so an ® on it is a violation; ASCII "(R)" is itself a violation); no GARM reference; no one-click SmartLists push into DV360; regulated categories flagged if applicable (`09_Compliance.md`); BAV language uses precise framework terms; internal feasibility flags, margin notes and red-cell markup stripped from client files; Transmit Live never named. Check the register for retired proof points and prohibited partner names or Sightly-competitor names. Cite the specific rule and instance for any violation. *Run the visuals through `sightly-visual-brand` for on-brand design compliance.*

**Gate 5 — Narrative arc & weakest point.** Does it tell one story and has its weakest point been fixed? Check: the deck tells one coherent story start to finish; there's a clear recommendation, not just information; each slide earns its place; the weakest point has been identified and strengthened; the work has been read as a skeptical agency reviewer would; **all artifacts tell the same story — media plan, deck copy, persona framing, and email are consistent with each other.** Name the narrative thread, flag any disconnected slide, and name the weakest point explicitly with what was done about it.

## Output

- **Quick check (the default):** the deliverable with the fixes made, and two or three lines for the strategist: anything fixed that changes what they will see, an assumption to confirm, and any open decision. Skip the list of checks.
- **Full run: gate-by-gate report** — PASS/FAIL for each of the five gates, with quoted findings and corrected versions.
- **Full run: overall verdict** — clear for handoff, or **blocked** with the list of failures the strategist must resolve first.

Never mark a deliverable clear for handoff while any gate is failing.

**After pushback.** When the strategist pushes back that copy didn't meet the bar, the revision runs the full chain before it goes back (brand voice, the AI-tell check, these gates and the clean-context claim check); don't offer it as optional.

**Decks.** Check deck copy on the rendered slides: view each slide, compare it with the template it came from (type sizes, weights, colors, alignment, slot counts), and fix polish issues such as mismatched corner radii, alignment and spacing directly. On-brand checks (Gates 1 and 4) should call `sightly-brand-voice` and `sightly-visual-brand` when available; otherwise apply their rules directly and say so.

## What this skill does not do

- It does not write the deck, plan or email. In the default quick check it fixes what it finds; in a full run it audits and flags with fixes for the strategist to approve.
- It does not set rates or build the plan.
- It does not clear a deliverable with an open gate failure.

---

*End of Sightly QA Gate skill.*
