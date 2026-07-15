# Culture Desk — RFP Workflow

The complete Sightly Culture Desk skills pack behind the **Sightly RFP Guide**.
Installing this plugin drops all 19 workflow skills into Cowork at once, so the
trigger phrases in the guide actually do something.

## The orchestrator

- **sightly-rfp-orchestrator** — walks the full 9-step RFP workflow, routing to
  the right skill at each step and confirming before advancing. Say *"start an RFP."*

## Skills by workflow step

| Step | Skill(s) |
|------|----------|
| 1 · Brief intake | sightly-brief-intake |
| 2 · Comparable plan | sightly-comparable-plan-finder |
| 3 · Brand Mentality discovery | sightly-insights-to-action |
| 4 · Narrative arc | sightly-insights-to-action |
| 5 · Personas | sightly-audience-architecture-builder, sightly-persona-overlap-analyzer |
| 6 · Platform roles | sightly-platform-role-planner |
| 7 · Media plan | sightly-rate-recommender, sightly-media-plan-builder |
| 8 · Timing/geo/feasibility | sightly-media-plan-builder |
| 9 · Deck, QA & handoff | sightly-proposal-deck-builder, sightly-selfservice-deck-builder, sightly-brand-voice, sightly-visual-brand, sightly-qa-gate |

## Supporting skills

sightly-brand-check, sightly-rate-library-monthly-update, rfp-tracker-logger,
rfp-reconciliation-audit, rfp-proposal-drive-filer.

## Before it all works

See **SETUP.md** — connect Monday.com and load the Culture Desk knowledge base.
