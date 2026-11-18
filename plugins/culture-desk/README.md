# Culture Desk (v2) — RFP Workflow

The complete Sightly Culture Desk skills pack behind the **Sightly RFP Guide**.
Installing this plugin drops all 19 workflow skills into Cowork at once, so the
trigger phrases in the guide actually do something. It is the V4-aligned successor to
`culture-desk-rfp` (1.7.0); install one or the other, not both, or every skill appears twice.

## The orchestrator

- **sightly-rfp-orchestrator** — walks the full 9-step RFP workflow, routing to
  the right skill at each step and confirming before advancing. The strategist sets the order and
  scope, and steps can be skipped or reordered. It runs brief intake itself at Step 1. Say
  *"start an RFP"* or paste a brief.

## Skills by workflow step

| Step | Skill(s) |
|------|----------|
| 1 · Brief intake | sightly-rfp-orchestrator |
| 2 · Comparable plan (pricing and history) | sightly-rate-recommender (its comparable-plans step) |
| 3a · Brand Mentality acquisition | sightly-mentality-prompt-builder |
| 3b · Brand Mentality interpretation | sightly-insights-to-action, sightly-claim-integrity |
| 4 · Narrative arc | sightly-insights-to-action |
| 5 · Personas | sightly-audience-architecture-builder, sightly-persona-overlap-analyzer |
| 6 · Platform roles | sightly-platform-role-planner |
| 7 · Media plan | sightly-rate-recommender, sightly-media-plan-builder |
| 8 · Timing/geo/feasibility | sightly-media-plan-builder |
| 9 · Deck, QA & handoff | sightly-selfservice-deck-builder (or the personal sightly-deck-build where installed), sightly-brand-voice, sightly-visual-brand, sightly-qa-gate (the quick check before handover; skipped when sightly-deck-build has run its own QC), sightly-strategy-email (the seller handoff) |
| Every step with client-facing copy | sightly-claim-integrity |

## Supporting skills

sightly-brand-check, sightly-strategy-email (seller handoffs and client notes),
staging-log-writer (knowledge-base corrections to the Staging Log), rfp-tracker-logger,
rfp-reconciliation-audit, rfp-proposal-drive-filer.

## Before it all works

See **SETUP.md** — connect Monday.com and load the Culture Desk V4 knowledge base (live 17 November 2026).
