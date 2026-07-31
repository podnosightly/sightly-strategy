---
name: sightly-brand-voice
description: >-
  Applies Sightly's codified written brand voice — tone, the enforced copy rules, banned
  patterns, approved/prohibited terminology, messaging pillars, and citable proof points — to
  any writing, and audits existing copy for voice drift. Use when writing or editing Sightly
  copy of any kind: decks, slide copy, proposals, one-pagers, emails, LinkedIn posts, sales
  content, or when the user says "make this on-brand", "apply Sightly voice", "write in our
  voice", "check the voice", "does this follow our copy rules", "clean up this copy", or "find
  voice drift". Not for visual/design work (use sightly-visual-brand) and not for generating a
  brand-voice guide from scratch.
---

# Sightly Brand Voice

Enforce Sightly's written brand voice on every piece of copy this skill touches. The complete
codification lives in `references/brand-voice-full.md` — load it before writing or auditing, and
treat it as the source of truth. This body is the operational summary.

## Gate 0 — read before writing

Before producing any copy, state which reference material you have read in this session, by
filename. If that list is empty, stop and read it. Do not draft first and consult the reference
after the user pushes back.

For long-form prose written in a named person’s voice — emails to sellers or clients, internal
notes, written strategy summaries — the voice exemplars in `references/voice-exemplars.md` are
required reading, not optional context. Approximating someone’s voice from a description of it
produces copy they will reject.

**The exemplars do not apply to slide copy.** They are long-form emails, and their register will
produce sprawl inside a slide’s word budget. Slide copy follows the deck-builder skills for
structure, `sightly-visual-brand` for design tokens, and the copy rules below for the sentences.

## When writing new copy

1. Read `references/brand-voice-full.md` first.
2. Draft to the tone: professional, confident, sharp, strategic, grounded in execution;
   consultative not transactional; an experienced media strategist speaking, never a generic ad-tech
   or vague-AI voice.
3. Apply the copy rules below to every sentence.
4. Run the Gate 1 self-audit below before returning anything. Fix violations silently — do not
   hand back copy that breaks a rule.

## Gate 1 — the self-audit that actually catches things

Ordinary self-assessment fails on your own writing. Run these five checks explicitly and report
what each one found.

**Favourite-line first.** Audit the lines you are most pleased with before anything else. Any line
that reads as quotable, aphoristic, slogan-shaped or "punchy" is a prime suspect.

**Restate in plain words.** The ban on aphorisms is useless without a test, so here it is. Take any
line that reads as quotable and restate it as a flat factual sentence. If the restatement says
nothing a reader could act on or disagree with, the line was decoration and it comes out. Reversal
and mirror constructions are the highest-yield suspects — "owns its category, and that has stopped
protecting it", "we're not selling reach, we're selling compression" — because the symmetry is doing
the work an argument should be doing. Ask what the sentence asserts, not whether it reads well.

**No exemption for inherited copy.** Lines carried from an approved deck, a template, a shell or a
colleague’s draft get audited exactly like new copy. Approved layout does not mean approved cadence.

**Sweep the class, not the instance.** When you find a violation, search the whole artifact for
every other instance of that pattern before reporting. State the count: "found and fixed 6 em
dashes", not "fixed the em dashes". A fix reported without a count is incomplete.

**Invented-term check.** Scan for any term you coined during the session and then used as though it
were established vocabulary. If a reader outside the conversation could not define it, it is jargon.
Replace it with the plain description.

## When auditing / cleaning up existing copy

Go line by line. For each issue, name the rule it breaks and give the fix. Group findings by
severity (terminology/compliance first, then copy-rule violations, then polish). Flag any prohibited
term, banned pattern, or unsupported claim explicitly.

## The 12 copy rules (enforced)

1. First sentence of every paragraph carries the idea. No warm-up, no restating the brief.
2. One job per sentence. Two ideas joined by a dash or "but" → split or cut the weaker half.
3. Specific beats generic. Named behaviors, real numbers, real platforms over vague phrasing.
4. Plain punctuation. Commas and periods; colons/semicolons only when they carry meaning.
5. No AI cadence tells. No "X. Y. Z." triplets, no "Not just X, but Y", no "It's not X, it's Y",
   no "That's why / that's how" pivots, no fragment stacks for rhythm.
6. Bullets are sentences. Bold a real data point inside the sentence, not a label at the front.
7. Deck-slide word budget: strategy/persona slides 80–130 words; over 140 cut, under 40 too thin.
8. Setup then payoff per slide: frame the idea in one sentence, then pay it off with evidence.
   Never open cold into a bullet list.
9. Three line-wraps maximum per paragraph.
10. No orphan words (a single word alone on a line).
11. Every number carries its denominator and its consequence in the same visual unit. "23.7%" is
    an orphan. "23.7% of everyone engaging with the title arrived through slate coverage, so the
    buy puts it in front of fans already paying for the platform" is a claim. A stat without both
    does not ship.
12. No bare label fragments as section beats. "The opportunity." followed by nothing is the
    bold-label bullet executed in prose. A named opener is fine when a full sentence immediately
    does the work.

## Hard "never use" list (abbreviated — full list in reference)

Em dashes for rhythm; hyphens as sentence breaks; the phrase "trade areas"; agency buzzwords
("best-in-class", "cutting-edge", "innovative solutions", "disruptive", "leverage synergies");
cliches ("move the needle", "at the end of the day"); hollow intensifiers ("game-changing",
"transformative", "crucial", "vital"); triplet patterns; "It's not X, it's Y"; "Not just X but Y";
throat-clearing openers ("In today's landscape", "It's no secret", "When it comes to"); bold-label
bullets; "we believe" / "we feel" (say "here is what this does and why").

Also never: comma-stacked fragment cadence ("One file, two plans, built to split"); status-field
phrasing in prose ("Numbers are directional until we hear budget"); aphorisms that compress a real
point into something quotable and meaningless.

## Terminology (must enforce)

Approved: "Brand Suitability" (never "brand safety" externally), "Social Intelligence" (never
"social listening"), "Brand Mentality®", "Anticipation Software®", "SmartLists™", "Speed of
Culture". YouTube = "badged YouTube Measurement Program (YTMP) partner"; TikTok = "badged TikTok
Marketing Partner, Media Buying Technology category".

The creative deliverable is a **"sizzle"** (a sizzle reel). "Scissors" is a speech-to-text error that
has circulated in planning guidance and is not a term.

Prohibited: "Brand Safety" and "Social Listening" (external); competitor names in client-facing
materials; white-label partner names (Infegy, Transmit Live, the news-API provider, the Spotify audio
partner name). IRIS.TV and Spectrum Reach are the only externally nameable partners, and always
lead with Sightly.

## Messaging pillars and proof points

Anchor claims to the six messaging pillars and back them with the citable proof points in the
reference file (e.g. 2X search intent / 3X purchase intent — MAGNA study; 1 of 7 global YTMP
partners; 2B daily data assessments). Never invent a proof point or a number that is not in the
reference.

**No proof point is drop-in ready.** Check each against the project's do-not-use register before
use. Some have been retired, some are disputed, and one carries no named source at all: the "+20%
engagement lift" in the reference file has no study attached and should not ship until it does. Two
further figures are under dispute and are not to be used pending resolution — the CA Lottery "Set
for Life" brand lift, and the YTMP data-volume multiple, which appears in circulation as both 400x
and 4,000x. Where another skill or a template hands you a proof point as pre-cleared, this list
overrides it.

## Data trust — provenance is given, sufficiency is tested once

Two different things hide under the word "verified", and separating them is what makes this work.

**Provenance is given.** Client-provided data, Brand Mentality® outputs, research-team pulls and
anything the strategist confirms are real and correctly measured. Never audit whether the number
exists, never rate the source's reliability, never hedge it in output. Caveats appear only where the
source document itself states a limitation, and are attributed to that document rather than
presented as your own doubt.

**Sufficiency is tested once, on intake.** Before anything is built on a figure, name the claim it
will be used to support and check whether it supports that claim. A number can be real, correctly
measured, and still not carry the sentence written on top of it. Sufficiency is a property of the
claim, not of the data, so confirming the data does not settle it.

**Then the verdict is durable.** Whatever survives intake is true for the rest of the project. Do
not re-open it, re-hedge it, or raise it again mid-build. Whatever fails goes to the do-not-use
register and does not come back, however useful it looks later. Skepticism belongs at the boundary;
certainty after it.

Re-litigating confirmed data mid-build is a failure, not diligence. So is carrying a figure into
copy because nobody asked what it was being made to prove.
