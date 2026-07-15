---
name: sightly-brand-check
description: >-
  A single, self-contained skill that reviews anything against Sightly's approved brand guidelines
  and then fixes it. Takes copy, a slide or a full deck, an image or graphic, or HTML/web content,
  figures out which guidelines apply, reports what's off-brand with specific fixes, and offers to
  APPLY the fixes (rewrite copy on-voice, rebuild slides/HTML to the design tokens) or recreate the
  asset on-brand. It carries the full written-voice codification and the visual design system in its
  own references, so it works on its own. Use when someone shares something and asks "is this
  on-brand", "brand check this", "review this against our guidelines", "make this on-brand", "fix
  this to our style", "clean this up to our brand", or drops a deck / image / copy / link for review.
  Not for building strategy or a media plan.
---

# Sightly Brand Check

Review any asset against Sightly's approved guidelines, report what's off-brand, and offer to fix or
recreate it. One front door for "make this on-brand": detect the input, apply the right guidelines,
critique it, and correct it.

**This skill is self-contained.** The full guidelines live in its own `references/`:

- `references/brand-voice.md` — the complete written voice: tone, the copy rules, banned patterns,
  approved / prohibited terminology, messaging pillars, and citable proof points.
- `references/design-tokens.json` — the exact visual tokens: colors, the hero-sweep and named brand
  gradients, the Inter type scale (with Inter Black as the display weight), and components.
- `references/design-system-spec.md` — the plain-language visual design system and its complete
  official palette.

Load the reference(s) relevant to the input before reviewing. Everything needed is bundled — no
other skill is required. (If the Culture Desk knowledge base is present, treat it as the live source
of truth and reconcile.)

## Step 1 — Identify the input and which guidelines apply

- **Copy / text** (email, slide copy, one-pager, post, headline) → `brand-voice.md`.
- **Image / photo / graphic / logo lockup** → `design-tokens.json` + `design-system-spec.md`.
- **Slide or full deck** (Google Slides, .pptx, exported images) → **both** — copy *and* visual.
- **HTML / web / artifact** → **both**.
- If given a link or file, open it and **view it visually** — render slides and images and read what
  is actually there. Never judge design or layout from a text dump or from assumptions.

State up front what you detected and which guideline sets you're applying.

## Step 2 — Review against the guidelines

Load the relevant references and check against them. Cite the specific rule for every finding.

**Written voice (from `references/brand-voice.md`):**

- Tone: professional, confident, consultative, evidence-grounded; "speed of culture" where it fits.
- Copy rules: lead with the point; one job per sentence; specific beats generic; plain punctuation
  (no em dashes or hyphens used for rhythm/drama); no AI tells (no triplet headlines, no "not just X
  but Y", no "it's not X, it's Y", no "that's why / that's how" pivots); bullets are sentences with
  the bold on a real data point, never a front label; setup then payoff per slide.
- Terminology: **Brand Suitability** not "brand safety"; **Social Intelligence** not "social
  listening"; marks on **Brand Mentality®**, **Anticipation Software®**, **SmartLists™**; YouTube =
  "badged YouTube Measurement Program (YTMP) partner"; TikTok = "badged TikTok Marketing Partner,
  Media Buying Technology category"; no competitor names; no white-label partner names.
- Proof points: every stat traces to a citable proof point in the reference, and the same claim uses
  the same number everywhere in the asset (watch for a claim stated with different figures).

**Visual (from `references/design-tokens.json` + `design-system-spec.md`):**

- Colors match the canonical tokens (Sightly Blue `#00AEEF`, Sightly Slate `#333D47`, base darks
  `#000000`/`#111111`, purple `#7B61FF`, etc.). Flag drift — near-duplicate cyans that aren't
  `#00AEEF`, off-orange that isn't `#FF6F07`, greys off `#D4D9D9`/`#A0A3A3`, the Google-Docs link
  blue `#1A73E8`.
- Type is **Inter** (flag Open Sans / Roboto / Arial creep); **Inter Black (900)** for hero stats.
- Gradients use the hero sweep or the named brand gradients (Blue, Grey, Purple, Teal, Mentality
  Tri-Gradient), not ad-hoc fills.
- Layout uses the recurring components (title, section divider, stat callout, comparison columns,
  data table) on the dark base with organic-blob + hero-sweep treatment.

## Step 3 — Report the findings

Return a structured review, not just a verdict:

- Group findings by **Voice**, **Visual**, and **Terminology / Hard Rules**.
- For each: quote or point to the exact spot, name the rule it breaks, mark severity — **Blocker**
  (prohibited term, off-brand color, wrong / inconsistent proof point), **Should-fix** (copy-rule or
  color drift), **Polish** — and give the corrected version or the precise change.
- Lead with blockers. If the asset is already on-brand, say so plainly.

## Step 4 — Offer to fix or recreate (always confirm first)

After the report, offer the applicable options and wait for a yes before changing anything:

- **Apply copy edits** — rewrite the flagged copy on-voice, preserving meaning; show before/after.
- **Rebuild the design** — for a slide, HTML, or graphic, produce a corrected version using the
  canonical tokens, gradients, Inter, and components; output it as a file.
- **Images (raster)** — you can't edit pixels directly. Give precise art-direction changes, and if an
  image-generation tool is available, offer to regenerate on-brand; otherwise hand the fix list off.
- **Recreate from scratch** — if the asset is far off, offer to rebuild it to spec rather than patch.

Show the corrected artifact for approval; don't silently overwrite the original.

## Rules

- View visuals before judging them — render, don't assume.
- Confirm before applying any change.
- Cite the rule behind every fix; never invent a brand rule, color, or proof point.
- When rewriting copy, keep the author's meaning and specifics intact.
- The bundled references (and the knowledge base, if present) are the source of truth.

## Keeping it current

The references are a snapshot. When the brand voice or the design tokens change, update the matching
file in `references/` and re-share the skill.

## What this skill does not do

- It does not build strategy, personas, or a media plan.
- It does not apply changes without confirmation.
- It does not redefine or invent brand guidelines.

---

*End of Sightly Brand Check skill.*
