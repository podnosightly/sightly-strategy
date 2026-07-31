---
name: sightly-claim-integrity
description: >-
  Tests whether individual claims hold before they enter a deliverable, using falsification,
  provenance and sufficiency checks, and maintains a per-project do-not-use register. Default mode
  spawns a clean-context verification subagent, because a checker with no conversational history
  cannot drift. Use when metabolizing someone else's data pull or report, at each Insights-to-Action
  phase gate, before any interpretive claim enters client-facing copy, when a session has produced
  an audit and is now switching to persuasive writing, or on request ("check these claims", "does
  this hold up", "verify this copy"). Complements the QA framework, which audits numbers, style,
  feasibility, terminology and narrative but never takes the claim as its unit.
---

# Sightly Claim Integrity

The Sightly QA framework has five gates whose units are sentence style, number, plan feasibility, terminology, and story. None takes a **claim** as its unit — an assertion joining evidence to a conclusion. That is the gap this skill fills.

A sourced number can carry an invalid inference. A stylistically clean sentence can assert nothing. Both pass QA as currently written.

---

## Default mode: spawn a clean-context verification agent

**This is the primary way to use this skill, and the reason is structural.**

A checker that has been present while the work was built cannot reliably check it. It watched the evidence get found, it knows why a line felt good, and it has momentum behind the argument. Over a long session, attention to any standing rule decays — including this one.

A subagent with a fresh context window has none of that. It never saw the figure land well. It has nothing to drift from, by construction.

So: **before any client-facing copy ships, spawn a verification agent.** Not once at the end of the workflow. Each time copy is written.

Hand it three things and nothing else:

1. The project's do-not-use register
2. The claim ledger, if one exists
3. The draft copy

Do **not** hand it the conversation history, the reasoning that produced the copy, or an explanation of why a claim is correct. Those are the contaminants.

### Verification agent prompt template

```
Verification pass. You have no context beyond what is below, and that is deliberate.

DO-NOT-USE REGISTER:
[paste register]

CLAIM LEDGER (if one exists):
[paste ledger]

DRAFT COPY UNDER REVIEW:
[paste draft]

Your job is to find violations, not to improve the writing. Report only
findings. Do not rewrite, do not compliment, do not summarise the draft.

Run these four checks on every assertion in the draft:

1. REGISTER CHECK. Does any figure, claim or phrasing in the draft appear
   on the do-not-use register, in any wording? This is a lookup. Report
   every hit with the register entry it matches.

2. FALSIFICATION. For each claim, what observation would make it false?
   If nothing would, it is not a claim. Quote it and say so. Watch for
   reversal constructions ("owns X, and that has stopped working"),
   category errors, tautologies, and unsupported superlatives (first,
   only, most, best, largest — each needs a comparison set).

3. SUFFICIENCY. For each claim resting on a number or a cited finding,
   state the weakest claim that evidence licenses. If the draft asserts
   something stronger, quote both and flag the gap.

4. LEDGER CONSISTENCY. Does anything labelled JUDGMENT in the ledger
   appear in the draft phrased as a finding? Judgment items ship as
   recommendations, never as findings.

Output format: a numbered list of findings. For each — the quoted text,
which check it fails, and why. If a check produces nothing, say so in one
line. Do not pad.
```

Then act on what comes back before anything ships. If the agent finds nothing, say that plainly rather than treating silence as endorsement.

---

## When this runs

Interpretive assertion is a narrow surface, and this skill is scoped to it.

- **Every time client-facing copy is drafted or revised.** Spawn the agent. This is the one that matters, because copy gets written on many turns and gates fire on few.
- **Each Insights-to-Action phase gate.** Present the claim ledger with the findings so the strategist signs off on epistemic status, not only on prose.
- **When metabolizing an external report, data pull, or research return.** The highest-risk moment: inherited claims arrive pre-formatted as findings and read as authoritative.
- **When a session has produced an audit or correction and is now switching to persuasive writing.** Re-read the audit before approving output.

**Not needed for:** rate cards, arithmetic, media plan line items, calendar dates with a URL, or anything where the output is a computation rather than an assertion.

---

## The three tests

### 1. Falsification

**What observation would make this false?**

If nothing would, it is not a claim. It is decoration wearing the grammar of analysis. Cut it or rewrite it as something checkable.

- **Reversal and mirror constructions.** "Owns the category, and that has stopped protecting it." "They report what happened; we act on what is happening." These read as analysis because the structure implies a discovered tension. Ask what the threat is, or what capability is claimed. If the sentence cannot answer, the structure was doing the work.
- **Category errors.** "Community ownership is real infrastructure." Ownership is not infrastructure. If the predicate does not apply to the subject, there is no claim underneath.
- **Tautologies.** "The window that converts a fan is the window in which the game is new."
- **Unsupported superlatives.** First, only, most, best, largest. Each needs a comparison set, and usually there isn't one.

### 2. Provenance

**Did I originate this, or inherit it?**

If inherited, name the source document, then ask:

- **Did the source hedge it?** Carry the hedge or drop the claim. Sources routinely hedge in one section and state flat in another. Executive summaries are where hedges go to die.
- **What tense and modality did the source use?** A conditional forward-looking risk ("if buyers spent their budget on X, they may defer Y") is not a retrospective causal finding. Promoting one to the other is common and invisible.

Inherited claims are the largest single source of error, because they arrive pre-formatted as findings.

### 3. Sufficiency

**Does the cited evidence support this claim, or only a weaker one?**

State the weakest version the evidence licenses, then check whether the argument still needs the stronger one. Usually it doesn't, and the weaker version is more defensible.

| Pattern | Example | What the evidence actually licenses |
|---|---|---|
| **Ordinal read as trajectory** | Annual sales rank fell from 3rd to 6th, therefore the title is declining | Only that other titles outsold it. Rank moves when the field moves |
| **Aggregate read as subset** | Ultimate Team is 29% of company revenue, therefore MUT is this title's revenue concentration | Only the aggregate. If the disclosure says "a substantial portion derived from [other franchise]," the subset is not knowable |
| **n=1 read as pattern** | Post A got 758 likes, post B got 198, therefore format A outperforms | Two observations |
| **Absence in one channel read as absence in reality** | Price barely appears in social, therefore not a pricing problem | Only that price is not discussed. Purchase behaviour is measured elsewhere |
| **Silence read as inactivity** | No conversation spike Oct–May, therefore the period is unworked | Only that no spike occurred. Check what the brand actually did |
| **Term velocity read as mechanic efficacy** | Mentions of "codes" fell 96%, therefore the giveaway mechanic is failing | Only that the language declined. Fewer campaigns produces the same signal |
| **Emotion classifier read as brand attitude** | "Trust" leads at 28%, therefore brand trust is strong | A linguistic tag distribution. Check expressed evaluation separately |
| **Broken dataset trusted selectively** | A 0.11pp entity-share gap treated as meaningful, in a dataset flagged as having a resolution error | Nothing. If resolution is broken enough to misfile a quarter of mentions, no fine distinction survives |

---

## Output: the claim ledger

Label every load-bearing claim.

- **SOURCED** — primary source with a URL. Name the source, not just "sourced."
- **COMPUTED** — arithmetic from confirmed inputs. Show the working so it can be re-run.
- **JUDGMENT** — a recommendation. State what it rests on and what breaks if it's wrong. **Never ships as a finding.** Ships as a recommendation with the strategist's name on it.
- **CUT** — removed, with the reason recorded. This bucket prevents recurrence.

Where a claim depends on a judgment input, say so. A frequency calculation built on an estimated audience pool inherits that estimate's status no matter how precise the arithmetic looks.

---

## The do-not-use register

**The highest-leverage part, because it is mechanical and does not degrade.**

A finding recorded in a document does not constrain anything. Findings sit in files; rules block output. Converting one into the other is the whole point.

Every project keeps `<client>-do-not-use-register.md` alongside its working files. When a claim is disqualified it goes in with three fields:

1. The claim or figure, verbatim
2. Why it is disqualified
3. What to say instead, if the underlying point still needs making

Then: **no output ships without checking against the register.** A lookup, not a judgment. That is what makes it hold under deadline pressure, which is when everything judgment-based fails.

Internal only. Never travels into client-facing material.

---

## The failure this exists to prevent

A confound is identified and written into an audit document. Twenty minutes later the same figure is used the same wrong way in client-facing copy, because the finding was never converted into a constraint, and because persuasive writing selects evidence on impact rather than validity.

Confounded evidence frequently has *more* rhetorical impact than clean evidence, since the confound is often what makes the number dramatic. The selection pressure in persuasive mode runs backwards. That is why the check has to be mechanical and external rather than remembered, and why the default mode is a clean-context agent.

---

## Working rule for the strategist

**Challenge any sentence that sounds quotable.** Compression into a memorable line is the exact condition that produces empty predicates and overreaching inferences. When a sentence lands well, that is the signal to test it, not to keep it.
