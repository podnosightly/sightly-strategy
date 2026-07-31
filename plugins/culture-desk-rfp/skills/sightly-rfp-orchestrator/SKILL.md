---
name: sightly-rfp-orchestrator
description: >-
  Guides a strategist through the full 9-step Sightly RFP workflow, routing to the right skill at
  each step and confirming before advancing. It orchestrates — it does not re-implement the
  sub-skills. Tracks which step you're on, states what each step produces, recommends the next
  skill, holds the project's do-not-use register as standing state, and stops for confirmation
  between steps; steps can be skipped or reordered. Triggers on "start an RFP", "walk me through
  the RFP workflow", "what's next on this RFP", "kick off an RFP", "run the RFP process", or
  "where are we on this RFP". Not a replacement for the sub-skills — it hands off to them.
---

# Sightly RFP Orchestrator

Drive a strategist through the nine-step Sightly RFP workflow, one collaborative checkpoint at a time. This skill is a router and a conductor: at each step it says what the step produces, recommends the skill that does the work, hands off, and waits for the strategist to confirm before moving on. It does **not** re-implement any sub-skill — the sub-skills own their logic.

The workflow is a thinking framework, not an assembly line. Steps can be skipped, combined, or reordered on the strategist's call (see `05_RFP_Workflow.md` if the knowledge base is present). One-off questions and quick-turn requests don't need the full sequence.

## How to operate

- **Track state.** Always know which step is current, what's been confirmed, and what's still open. When asked "what's next," answer from that state.
- **Carry the register.** The orchestrator is the only thing that persists across the whole workflow, which makes it the home for constraints that must survive *between* steps rather than only at them. See "Standing state" below.
- **One step at a time.** Present the current step: what it produces, which skill runs it, and what input it needs. Hand off to that skill. Then **stop and wait** for the strategist to confirm before advancing.
- **Recommend, don't force.** Suggest the next step, but let the strategist skip or reorder. Confirm any reorder so the shared state stays accurate.
- **Route, don't do.** When a step has a skill, invoke or point to that skill by name rather than doing the work here. When a step has no skill yet, do it directly with the strategist and note it's a manual step.
- **Carry the thread.** Keep the confirmed outputs (brief, strategy, personas, rates, plan) available to later steps so each skill starts from the real prior work.

## Standing state the orchestrator holds

Three things persist across every step and get restated at each handoff, in one or two lines. Not a recap of the whole workflow — just the constraints the next step could violate.

**1. The do-not-use register.** Created empty at Step 1 as `<client>-do-not-use-register.md`. Every disqualified figure or claim goes in with the reason and the replacement. **Restate any register entry relevant to the step being handed off.** A finding recorded three steps ago does not constrain the current step unless it is carried forward, and this is the mechanism that carries it. Internal only; never travels into client-facing material.

**2. Confirmed vs. judgment.** Which prior outputs are sourced or computed, and which are the strategist's judgment calls. Judgment items travel as recommendations with the strategist's name on them, never as findings, and later steps must not silently promote them.

**3. Open flags.** Feasibility, compliance, timing, geo, budget, missing inputs. Anything raised and unresolved stays visible rather than being absorbed into the next step's assumptions.

## The 9 steps and their skills

1. **Brief intake & clarification** → `sightly-brief-intake` (intake schema + compliance flags). Produces a confirmed, structured brief. **Also creates the do-not-use register, empty.**
2. **Comparable plan retrieval** → `sightly-comparable-plan-finder` (Google Drive). Produces the structural template to model.
3. **Brand Mentality discovery** → `sightly-insights-to-action`, with `sightly-claim-integrity` on ingestion. Produces pillars, positioning tension, and the conversation landscape. **Ingesting an external report is the highest-risk moment in the workflow** — inherited claims arrive pre-formatted as findings. Run the claim check before the material is treated as established.
4. **Narrative arc** → `sightly-insights-to-action`. Produces the chosen arc and narrative skeleton.
5. **Personas** → `sightly-audience-architecture-builder`, then `sightly-persona-overlap-analyzer` **after a real Persona Builder run**. Produces distinct, de-duplicated personas.
6. **Platform & format roles** → `sightly-platform-role-planner`. Produces the justified platform lineup that feeds the plan.
7. **Media plan** → `sightly-rate-recommender` first (confirm rates), then `sightly-media-plan-builder`. Produces the Sightly Standard media plan with feasibility.
8. **Timing, geo & feasibility** → `sightly-media-plan-builder` (pressure-test). Produces a green-lit plan with no blocking issues.
9. **Deck, QA & handoff** → `sightly-proposal-deck-builder` (or `sightly-selfservice-deck-builder`), then `sightly-brand-voice` + `sightly-visual-brand` for on-brand enforcement, then `sightly-qa-gate` for the 5-gate check. Produces the client-ready, QA-passed deliverable.

## Stop-gaps (do not skip silently)

- **Step 1 gates everything.** Don't advance on an unconfirmed brief or an unresolved compliance flag.
- **Step 3 ingestion gate.** External reports and data pulls get a claim check before their findings are treated as established. Carry any hedge the source applied; a conditional risk is not a retrospective finding.
- **Step 5 handoff.** Persona overlap needs a real Persona Builder run; if only proposed interests exist, stay in `sightly-audience-architecture-builder` and note the run is pending.
- **Step 7 order.** Rates (`sightly-rate-recommender`) are confirmed before the plan (`sightly-media-plan-builder`) is built.
- **Client-facing copy gate — applies at every step, not only Step 9.** No interpretive claim ships in client-facing copy without a verification pass via `sightly-claim-integrity`. Copy gets written on many turns; the 5-gate QA fires once. A claim entering at Step 3 is structural in five places by Step 9, and removing it then means rework, which creates pressure to keep it. Check at the point of writing.
- **Audit-to-persuasion gate.** If a session has produced an audit or a correction and now moves to writing client-facing copy, re-read that audit before approving output. Audit posture hunts for reasons to distrust a claim; writing posture hunts for reasons to assert one. The skepticism does not transfer on its own.
- **Step 9 gate.** The QA gate must pass before handoff; a failed gate blocks sales handoff.

## Behavior at each checkpoint

State it like this: "**Step N — [name].** This step produces [output]. The skill for it is `[skill]`; it needs [input]. [Any relevant register entry or open flag.] Want me to hand off to it now, skip it, or do something else first?"

After the step's skill runs and the strategist confirms, update state and recommend the next step. When asked "what's next on this RFP," report the current step, what's confirmed, what's judgment, and the recommended next move.

## What this skill does not do

- It does not re-implement any sub-skill's logic — it routes to them.
- It does not advance past a checkpoint without the strategist's confirmation.
- It does not force the full sequence on quick-turn or one-off requests.
- It does not perform the claim check itself — that is `sightly-claim-integrity`, which spawns a clean-context verification agent. The orchestrator's job is to make sure the check happens and that the register travels.

---

*End of Sightly RFP Orchestrator skill.*
