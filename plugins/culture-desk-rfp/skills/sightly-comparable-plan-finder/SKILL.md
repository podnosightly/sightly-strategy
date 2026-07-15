---
name: sightly-comparable-plan-finder
description: >-
  Finds past Sightly decks and media plans in Google Drive that share structural DNA with a new
  brief — similar vertical, budget tier, platform mix, audience profile, or narrative challenge —
  and recommends which one to use as the structural template. This is Step 2 of the RFP workflow
  (comparable plan retrieval). Triggers on "find a comparable plan", "what past deck should I model
  this on", "any similar RFPs we've done", "find a template for this brief", "comparable plan
  retrieval", or "what have we done like this before". Requires the Google Drive connector. Not for
  building the new strategy, personas, or plan.
---

# Sightly Comparable Plan Finder

Find the closest past Sightly work to a new brief and recommend it as the structural template. We rarely build from scratch — reusing a proven arc from a similar win is faster and keeps quality consistent. This is Step 2 of the RFP workflow, run after brief intake.

Requires the **Google Drive connector** (the Sales/Strategy campaign folders and past decks live there). If it isn't authorized, say so and stop — do not guess at past work.

## What to do

1. **Take the brief's DNA** from the confirmed intake: vertical/industry, budget tier, platform mix, audience profile, objective, geo, and the core narrative challenge.
2. **Search Drive** for past decks, wrap decks, and media plans that match on those dimensions. Prioritize matches in this order: (a) same vertical + similar budget tier + overlapping platform mix, (b) same narrative challenge (e.g. tentpole activation, always-on access, new-biz reframe), (c) same audience profile. Search the campaign folders, agency folders, and any exemplar-deck library.
3. **Rank the candidates** and present the top 2–3 with, for each: the client/campaign, why it matches, its budget tier and platform mix, and a link.
4. **Recommend one** as the structural template, and name explicitly what the new brief does *differently* so the strategist knows what to change when adapting it.

## Guardrails

- **Match on structure, not just brand.** A footwear deck may be the wrong template for another footwear brand if the budget tier and platform mix differ; a different-vertical deck with the same narrative challenge and platform mix may be the better model.
- **Never invent a past campaign.** Only recommend work you actually found in Drive. If nothing is a strong match, say so and recommend the closest partial match plus what to build fresh.
- **Respect confidentiality.** Reference past work for internal structural reuse only; do not carry another client's specific data, rates, or names into the new proposal.
- **Hand off cleanly.** The output feeds `sightly-audience-architecture-builder` (which can "adapt this deck") and the deck builder. Note the chosen template's slide arc so downstream steps match it.

## Output

- **Top matches** — 2–3 candidates, each with client/campaign, match rationale, budget tier, platform mix, and Drive link.
- **Recommendation** — the single best structural template and why.
- **What differs** — the specific ways the new brief diverges from the template, so adaptation is deliberate.

## What this skill does not do

- It does not build the new audience, strategy, plan, or deck.
- It does not copy another client's data or rates into the new work.
- It does not fabricate past campaigns when no real match exists.

---

*End of Sightly Comparable Plan Finder skill.*
