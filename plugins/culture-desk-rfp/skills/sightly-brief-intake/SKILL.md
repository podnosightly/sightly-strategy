---
name: sightly-brief-intake
description: >-
  Turns a raw RFP brief (pasted text, a forwarded email, or an attached document) into Sightly's
  standardized intake schema, flags every gap as a targeted clarifying question, and flags any
  regulated category for the compliance workflow. Produces a clean intake summary the strategist
  confirms before the RFP workflow proceeds. Use at the very start of an RFP. Triggers on "intake
  this brief", "log this RFP", "what's missing from this brief", "start the intake", "structure this
  brief", or when a strategist pastes/attaches a new brief. This is Step 1 of the RFP workflow. Not
  for building strategy (sightly-insights-to-action), personas (sightly-audience-architecture-builder),
  or the media plan (sightly-media-plan-builder).
---

# Sightly Brief Intake

Turn a raw brief into a structured, confirmed intake before any building starts. This is Step 1 of the Sightly RFP workflow: get the ask completely understood, surface every gap, and flag compliance risk up front, so nothing downstream is built on a misread brief.

If the Culture Desk knowledge base is present, read `01_RFP_Intake_Schema.md` (the canonical schema) and `11_Compliance_Guardrails.md` (regulated categories) first — they are the source of truth. This body summarizes the operational steps.

## What to do

1. **Read the whole brief first.** Pasted text, forwarded email, or attached doc. Do not start extracting until you've read all of it, including any attached RFP document.
2. **Extract into the intake schema** (below). Fill only what the brief actually states — never guess a value.
3. **List the gaps as questions.** Turn every missing or ambiguous field into a targeted clarifying question. If the brief is thin, ask the **2–3 questions that most unlock the build**, not a wall of them. If the brief is solid, list remaining gaps inline and recommend proceeding.
4. **Flag regulated categories.** If the brand or product touches a regulated category, flag it immediately and route to the compliance workflow before anything else proceeds.
5. **Output a clean intake summary** and stop for the strategist to confirm before the workflow advances.

## The intake schema (extract each field)

- **Client / brand** — the advertiser.
- **Agency** — agency or holding company, and whether new or existing.
- **Objective / business goal** — what the campaign is for (awareness, consideration, action, tune-in, etc.).
- **KPI / success metric** — how success is measured (VCR, CTR, VTR, CPA, store visits, brand lift).
- **Budget** — total and any per-channel splits stated.
- **Markets / geos** — national, DMA list, regions; note if geo-targeted.
- **Flight dates** — campaign start and end; note if TBD.
- **Target audience** — demo, attributes, named personas if given.
- **Platform preferences** — channels named (YouTube, TikTok, CTV, Meta, Reddit, Spotify, Programmatic, etc.).
- **Self-service vs. managed service** — and any margin/MSA notes.
- **Constraints** — brand suitability requirements, exclusions, mandatories, measurement partner, reservations/betas.
- **Creative assets available** — what exists vs. what needs producing.
- **Decision timeline** — due date for the response and the client's decision date.
- **Request type** — RFP, request for strategy, request for targeting, pricing, insights, new-biz.

## Regulated categories (flag immediately)

Flag and route to the compliance workflow if the brand or product is in any of: **alcohol, cannabis, political / advocacy, pharma, financial / crypto, gambling / gaming**. Name the category, note why it triggers, and state that compliance review comes before the build proceeds. When in doubt, flag it — err toward flagging.

## Output

Produce a single intake summary the strategist can confirm at a glance:

1. **Intake summary table** — every schema field with its extracted value, or `— missing`.
2. **Clarifying questions** — the targeted questions that unlock the build (2–3 if the brief is thin; the full gap list if it's solid), each tied to the field it fills.
3. **Compliance flag** — regulated category status: clear, or flagged with the category and next step.
4. **Recommendation** — proceed, or hold for answers / compliance review.

End by asking the strategist to confirm the intake (and answer the clarifying questions) before Step 2. Do not advance the workflow on an unconfirmed or incomplete brief.

## What this skill does not do

- It does not build strategy, personas, or the media plan.
- It does not invent budget, flight dates, geos, or any field the brief doesn't state.
- It does not resolve compliance — it flags and routes.

---

*End of Sightly Brief Intake skill.*
