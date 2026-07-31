---
name: sightly-qa-gate
description: >-
  Runs Sightly's 5-gate QA framework against a finished RFP deliverable — deck copy, media plan,
  persona framing, and client email — and returns a pass/fail per gate with specific findings and
  fixes. Blocks handoff to sales on any failed gate. Runs at every step that produces client-facing
  copy or numbers, not only as the final check before handoff. Triggers on "QA this proposal", "run the QA gates", "is this ready for handoff", "check
  this before sales", "quality check this deck", or "run the 5 gates". Reads the QA framework and
  hard rules from the knowledge base if present. Not for writing the deck (deck builders) or
  building the plan (sightly-media-plan-builder).
---

# Sightly QA Gate

Run every finished RFP deliverable through all five quality gates before it goes to sales. Each gate returns pass or fail with specific findings. **No gate can be skipped, and any failed gate blocks handoff** until the strategist resolves it.

## This is not only a Step 9 skill

QA used to run once, at the end. That is too late. By the time a deliverable is finished, a wrong figure has already been written into a plan, a deck and an email, so fixing it means fixing three artifacts instead of one, and the version the strategist remembers is usually the wrong one. Run the gates that apply as each artifact is produced, then run all five before handoff.

- **Any step that produces a number** — rates, feasibility, allocation, audience size: run Gates 2 and 3 on it at that step.
- **Any step that produces client-facing copy** — strategy narrative, persona framing, slide copy, the client email: run Gates 1, 2 and 4 on it at that step.
- **Before handoff** — run all five across the whole set. Gate 5 is the only one that genuinely needs every artifact present.

A gate run mid-build reports and blocks exactly as it would at the end. An unresolved Gate 2 failure at Step 7 blocks Step 8; it does not get deferred to Step 9.

Inputs: the deck copy, the media plan, the persona framing, and the client-facing email — as complete as they exist. If the Culture Desk knowledge base is present, read `12_QA_Framework.md`, `02_Sightly_Brand_Voice.md`, and `04_Hard_Rules.md` first as the source of truth; the gates below are the working checklist.

## Before the gates — read the do-not-use register

**Ask for the project's do-not-use register and read it before running a single gate.** State what it contains, by item. If there isn't one, say so explicitly and treat every figure in the deliverable as unverified for Gate 2 — an absent register does not mean nothing was ruled out.

Anything a session already flagged is a **prohibition, not context**. A figure ruled out in an audit does not become usable because the session has since moved on to persuasive writing. That switch from auditing to selling is the most common point of failure, and it is why this lookup runs first rather than inside a gate.

## How to run it

Run all five gates in order. For each, produce a **PASS** or **FAIL**, and for every issue: quote the offending text, name the rule it breaks, and give the corrected version so the strategist can approve the fix fast. Present findings to the strategist — not just a pass/fail indicator. End with an overall verdict and a blocked/clear-for-handoff call.

## The five gates

**Gate 1 — Voice & AI-tell.** Does the output follow `02_Sightly_Brand_Voice.md`? Check: no em dashes for rhythm, no triplet patterns, no "Not just X but Y," no "it's not X, it's Y," no throat-clearing openers, no "X. Y. Z." headlines, no fragment stacks, no bold-label bullets, no hollow intensifiers; strategy/persona slides within 80–130 words; setup-then-payoff on each slide; no orphan words. *Run the copy through `sightly-brand-voice` if installed.* Flag every instance with a fix.

**Gate 2 — Number, source & sufficiency.** Does every number trace to a source, does it support the claim attached to it, and does the plan hold up? Sourcing and sufficiency are separate tests and both can fail independently — a correctly-sourced figure can still fail to carry the sentence it has been placed under, and that is a Gate 2 failure, not a style note. For every number, state the claim it is being used to make and whether it carries that claim. Apply the same test to non-numeric assertions: any sentence asserting a state of affairs needs something behind it, and "owns its category" fails this check as surely as an unsourced percentage does. Check: every CPM, benchmark, persona stat, and tactic cites a source; numbers trace to the media plan or brief; no invented data points; CPM accuracy audit (rates realistic for platform/format/targeting); buying-methodology validation (auction vs. reservation, CPM/CPV/CPC correct per line); rates match what the strategist provided; two-pass verification (check numbers, then re-check from a different angle). Check every figure against the do-not-use register before passing it. Flag every unsourced or off-looking number.

**Gate 3 — Brief alignment & feasibility.** Does it match the brief and can it run? Check: recommendation aligns to stated objectives; budget allocations supported by platform minimums; flight length supports the tactics; geo strategy realistic for the budget; all platforms/formats operationally feasible; nothing the structure can't support. State each misalignment and the specific constraint behind any feasibility failure.

**Gate 4 — Compliance & hard rules.** Have all hard rules been followed? Check: every rule in `04_Hard_Rules.md`; no white-label partner names client-facing; no competitor names client-facing; correct terminology throughout (Brand Suitability not "brand safety," Social Intelligence not "social listening," the actual ® and ™ glyphs on Brand Mentality® / Anticipation Software® / SmartLists™, since ASCII "(R)" and "(TM)" are themselves violations and a check written against "(R)" will never catch a missing mark); regulated categories flagged if applicable (`11_Compliance_Guardrails.md`); BAV language uses precise framework terms. Check the register for retired proof points and prohibited partner or competitor names. Cite the specific rule and instance for any violation. *Run the visuals through `sightly-visual-brand` for on-brand design compliance.*

**Gate 5 — Narrative arc & weakest point.** Does it tell one story and has its weakest point been fixed? Check: the deck tells one coherent story start to finish; there's a clear recommendation, not just information; each slide earns its place; the weakest point has been identified and strengthened; the work has been read as a skeptical agency reviewer would; **all artifacts tell the same story — media plan, deck copy, persona framing, and email are consistent with each other.** Name the narrative thread, flag any disconnected slide, and name the weakest point explicitly with what was done about it.

## Output

- **Gate-by-gate report** — PASS/FAIL for each of the five gates, with quoted findings and corrected versions.
- **Overall verdict** — clear for handoff, or **blocked** with the list of failures the strategist must resolve first.

Never mark a deliverable clear for handoff while any gate is failing. On-brand checks (Gates 1 and 4) should call `sightly-brand-voice` and `sightly-visual-brand` when available; otherwise apply their rules directly and say so.

## What this skill does not do

- It does not write or rewrite the deck, plan, or email — it audits and flags with fixes.
- It does not set rates or build the plan.
- It does not clear a deliverable with an open gate failure.

---

*End of Sightly QA Gate skill.*
