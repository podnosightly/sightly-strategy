---
name: sightly-platform-role-planner
description: >-
  Recommends the platform mix for a brief and defines the specific role each platform plays before
  the media plan is built — awareness, efficient reach, completion, contextual alignment,
  action-driving, or cross-platform reinforcement — with a rationale and format suggestions per
  platform. This is Step 6 of the RFP workflow (platform & format role definition), and it feeds
  sightly-media-plan-builder. Triggers on "what platforms should we use", "define the platform
  roles", "what's each channel doing", "recommend the platform mix", "platform and format roles",
  or "which channels for this brief". Not the media plan CSV itself (sightly-media-plan-builder) and
  not the audience build (sightly-audience-architecture-builder).
---

# Sightly Platform Role Planner

Decide what each platform does and why it earns its place — before the media plan math. Every platform on the plan should have a reason beyond "the client likes it." This is Step 6 of the RFP workflow: it takes the confirmed objective, budget, personas, and audience, and produces a justified platform-and-format lineup that `sightly-media-plan-builder` then costs out.

If the Culture Desk knowledge base is present, read `13_Platform_Quick_Reference.md` (platforms, when to recommend, the Sightly layer, suitability, minimums) first. For full format specs, defer to the Platform Reference Library / Tactics Playbooks.

## What to do

1. **Start from the objective and personas.** The funnel stage and the personas' behaviors decide which platforms belong. Awareness and reach goals, completion goals, action/conversion goals, and contextual-alignment goals each pull a different mix.
2. **Recommend the platform mix** scoped to the brief's budget and audience — never a laundry list. Include only platforms that earn a role.
3. **Define each platform's specific role** in one line: awareness, efficient reach, video completion, contextual alignment, action-driving, or cross-platform reinforcement. No two platforms should have the same undifferentiated job.
4. **Recommend formats per platform** with rationale (reference the Tactics Playbooks). Tie each to the role it serves.
5. **Flag weak or conflicting placements.** Call out any platform that is technically possible but strategically weak for this brief, and any conflict (e.g. a pulsed tactic re-entering its learning period, or two platforms competing for the same job).

## Guardrails

- **Role before math.** This skill defines roles and rationale; it does not allocate budget or build line items — that's `sightly-media-plan-builder`, which this feeds.
- **Scope to the brief's channels.** If the brief names specific channels, work within them (and flag if a named channel is a weak fit); if it's open, recommend the mix the objective justifies. Don't inherit channels from a template the brief didn't buy.
- **Every platform earns its place.** If a platform can't be given a distinct, defensible role, leave it out and say why.
- **Respect suitability and minimums.** Note where a platform's role depends on the Sightly Brand Suitability layer, and flag any platform likely to fall below its spend minimum at this budget (the media-plan builder confirms the numbers).

## Output

- **Recommended platform mix** — the platforms that earn a role, scoped to budget and audience.
- **Role table** — each platform, its single defined role, the format(s) recommended, and the rationale.
- **Flags** — strategically weak platforms, conflicts, learning-period or suitability considerations.
- **Handoff note** — the lineup is ready for `sightly-media-plan-builder` to allocate budget and build line items.

## What this skill does not do

- It does not build the media plan CSV or allocate budget (sightly-media-plan-builder).
- It does not define personas (sightly-audience-architecture-builder) or the strategy (sightly-insights-to-action).
- It does not set rates — those are strategist-provided via sightly-rate-recommender.

---

*End of Sightly Platform Role Planner skill.*
