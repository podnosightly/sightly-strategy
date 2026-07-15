---
name: sightly-rfp-orchestrator
description: >-
  Guides a strategist through the full 9-step Sightly RFP workflow, routing to the right skill at
  each step and confirming before advancing. It orchestrates — it does not re-implement the
  sub-skills. Tracks which step you're on, states what each step produces, recommends the next
  skill, and stops for confirmation between steps; steps can be skipped or reordered. Triggers on
  "start an RFP", "walk me through the RFP workflow", "what's next on this RFP", "kick off an RFP",
  "run the RFP process", or "where are we on this RFP". Not a replacement for the sub-skills — it
  hands off to them.
---

# Sightly RFP Orchestrator

Drive a strategist through the nine-step Sightly RFP workflow, one collaborative checkpoint at a time. This skill is a router and a conductor: at each step it says what the step produces, recommends the skill that does the work, hands off, and waits for the strategist to confirm before moving on. It does **not** re-implement any sub-skill — the sub-skills own their logic.

The workflow is a thinking framework, not an assembly line. Steps can be skipped, combined, or reordered on the strategist's call (see `05_RFP_Workflow.md` if the knowledge base is present). One-off questions and quick-turn requests don't need the full sequence.

## How to operate

- **Track state.** Always know which step is current, what's been confirmed, and what's still open. When asked "what's next," answer from that state.
- **One step at a time.** Present the current step: what it produces, which skill runs it, and what input it needs. Hand off to that skill. Then **stop and wait** for the strategist to confirm before advancing.
- **Recommend, don't force.** Suggest the next step, but let the strategist skip or reorder. Confirm any reorder so the shared state stays accurate.
- **Route, don't do.** When a step has a skill, invoke or point to that skill by name rather than doing the work here. When a step has no skill yet, do it directly with the strategist and note it's a manual step.
- **Carry the thread.** Keep the confirmed outputs (brief, strategy, personas, rates, plan) available to later steps so each skill starts from the real prior work.

## The 9 steps and their skills

1. **Brief intake & clarification** → `sightly-brief-intake` (intake schema + compliance flags). Produces a confirmed, structured brief.
2. **Comparable plan retrieval** → `sightly-comparable-plan-finder` (Google Drive). Produces the structural template to model.
3. **Brand Mentality discovery** → `sightly-insights-to-action`. Produces pillars, positioning tension, and the conversation landscape.
4. **Narrative arc** → `sightly-insights-to-action`. Produces the chosen arc and narrative skeleton.
5. **Personas** → `sightly-audience-architecture-builder`, then `sightly-persona-overlap-analyzer` **after a real Persona Builder run**. Produces distinct, de-duplicated personas.
6. **Platform & format roles** → `sightly-platform-role-planner`. Produces the justified platform lineup that feeds the plan.
7. **Media plan** → `sightly-rate-recommender` first (confirm rates), then `sightly-media-plan-builder`. Produces the Sightly Standard media plan with feasibility.
8. **Timing, geo & feasibility** → `sightly-media-plan-builder` (pressure-test). Produces a green-lit plan with no blocking issues.
9. **Deck, QA & handoff** → `sightly-proposal-deck-builder` (or `sightly-selfservice-deck-builder`), then `sightly-brand-voice` + `sightly-visual-brand` for on-brand enforcement, then `sightly-qa-gate` for the 5-gate check. Produces the client-ready, QA-passed deliverable.

## Stop-gaps (do not skip silently)

- **Step 1 gates everything.** Don't advance on an unconfirmed brief or an unresolved compliance flag.
- **Step 5 handoff.** Persona overlap needs a real Persona Builder run; if only proposed interests exist, stay in `sightly-audience-architecture-builder` and note the run is pending.
- **Step 7 order.** Rates (`sightly-rate-recommender`) are confirmed before the plan (`sightly-media-plan-builder`) is built.
- **Step 9 gate.** The QA gate must pass before handoff; a failed gate blocks sales handoff.

## Behavior at each checkpoint

State it like this: "**Step N — [name].** This step produces [output]. The skill for it is `[skill]`; it needs [input]. Want me to hand off to it now, skip it, or do something else first?" After the step's skill runs and the strategist confirms, update state and recommend the next step. When asked "what's next on this RFP," report the current step, what's confirmed, and the recommended next move.

## What this skill does not do

- It does not re-implement any sub-skill's logic — it routes to them.
- It does not advance past a checkpoint without the strategist's confirmation.
- It does not force the full sequence on quick-turn or one-off requests.

---

*End of Sightly RFP Orchestrator skill.*
