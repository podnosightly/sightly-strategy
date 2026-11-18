---
name: sightly-brand-check
description: >-
  A single, self-contained skill that reviews anything against Sightly's approved brand guidelines
  and then fixes it. Takes copy, a slide or a full deck, an image or graphic, or HTML/web content,
  figures out which guidelines apply, reports what's off-brand with specific fixes, and offers to
  APPLY the fixes (rewrite copy on-voice, rebuild slides/HTML to the design tokens) or recreate the
  asset on-brand. It reads the written-voice reference from sightly-brand-voice and the visual design
  system from sightly-visual-brand, which ship in the same plugin. Use when someone shares something and asks "is this
  on-brand", "brand check this", "review this against our guidelines", "make this on-brand", "fix
  this to our style", "clean this up to our brand", or drops a deck / image / copy / link for review.
  Not for building strategy or a media plan.
---

# Sightly Brand Check

Review any asset against Sightly's approved guidelines, report what's off-brand, and offer to fix or
recreate it. One front door for "make this on-brand": detect the input, apply the right guidelines,
critique it, and correct it.

**Where the guidelines live.** This skill keeps no copies of its own. It reads the references that
ship with its two sibling skills in this plugin, at these paths relative to this file:

- `../sightly-brand-voice/references/brand-voice-full.md` — the complete written voice: tone, the
  copy rules, banned patterns, approved / prohibited terminology, messaging pillars, and citable proof
  points.
- `../sightly-visual-brand/references/design-tokens.json` — the exact visual tokens: colors, the
  hero-sweep and named brand gradients, the Inter type scale (with Inter Black as the display
  weight), and components.
- `../sightly-visual-brand/references/design-system-spec.md` — the plain-language visual design
  system and its complete official palette.

Load the reference(s) relevant to the input before reviewing. If a path doesn't resolve, load the
`sightly-brand-voice` or `sightly-visual-brand` skill and read the same file from its `references/`
folder; never review from memory. (If the Culture Desk knowledge base is present, treat it as the live
source of truth and reconcile: `01_Hard_Rules.md`, `02_Voice_and_Terminology.md` and
`08_Proof_Points_and_Battle_Cards.md`.)

## Step 1 — Identify the input and which guidelines apply

- **Copy / text** (email, slide copy, one-pager, post, headline) → `brand-voice-full.md`.
- **Image / photo / graphic / logo lockup** → `design-tokens.json` + `design-system-spec.md`.
- **Slide or full deck** (Google Slides, .pptx, exported images) → **both** — copy *and* visual.
- **HTML / web / artifact** → **both**.
- If given a link or file, open it and **view it visually** — render slides and images and read what
  is actually there. Never judge design or layout from a text dump or from assumptions.

State up front what you detected and which guideline sets you're applying.

## Step 2 — Review against the guidelines

Load the relevant references and check against them. Cite the specific rule for every finding.

**Written voice (from `brand-voice-full.md`):**

- Tone: professional, confident, consultative, evidence-grounded; "speed of culture" where it fits.
- Copy rules: lead with the point; one job per sentence; specific beats generic; plain punctuation
  (no em dashes or hyphens used for rhythm/drama); no AI tells (no triplet headlines, no "not just X
  but Y", no "it's not X, it's Y", no "that's why / that's how" pivots); bullets are sentences with
  the bold on a real data point, never a front label; setup then payoff per slide.
- Terminology: **Brand Suitability** as the default; "brand safety" is permitted where the client or
  RFP uses it or where it is the clearer word; otherwise match the client's language and don't
  volunteer it (a volunteered use is a positioning note, never a violation); **Social Intelligence**,
  never "social listening"; **SmartLists** always plain (a trademark symbol on SmartLists is a violation);
  **Brand Mentality®** once, at its first mention in a proposal, and plain everywhere else (a second ® is a
  violation); **Anticipation Software** always plain (an ® is a violation);
  YouTube = "Google Premier Partner" with "Non-Public API Access" (never "YTMP" or "YouTube
  Measurement Program"); TikTok = "badged TikTok Marketing Partner, Media Buying Technology
  category"; no names of **Sightly's** own competitors (Pixability, Channel Factory, Zefr, OpenSlate,
  VuePlanner, CreatorIQ, Tubular Labs, Wizdeo, Sprinklr and other ad-tech, suitability, contextual, measurement or social intelligence vendors); IAS and DoubleVerify may be named as third-party verification integrations, never as competitors; the advertiser's category competitors are
  named whenever the work calls for it; no white-label partner names; no GARM references.
- Proof points: every stat traces to a citable proof point in the reference and has been checked
  against the project's do-not-use list, and the same claim uses the same number everywhere in the
  asset (watch for a claim stated with different figures). Named events, openings and launches carry
  a date and a source the client could find.

**Visual (from `design-tokens.json` + `design-system-spec.md`):**

- Colors match the canonical tokens (Sightly Blue `#00AEEF`, Sightly Slate `#333D47`, base darks
  `#000000`/`#111111`, purple `#7B61FF`, etc.). Flag drift — near-duplicate cyans that aren't
  `#00AEEF`, off-orange that isn't `#FF6F07`, greys off `#D4D9D9`/`#A0A3A3`, the Google-Docs link
  blue `#1A73E8`.
- Type is **Inter** (flag Open Sans / Roboto / Arial creep); **Inter Black (900)** for hero stats.
- Gradients use the hero sweep or the named brand gradients (Blue, Grey, Purple, Teal, Mentality
  Tri-Gradient), not ad-hoc fills.
- Layout uses the recurring components (title, section divider, stat callout, comparison columns,
  data table) on the dark base with organic-blob + hero-sweep treatment.
- No small section label (an eyebrow) above a slide title; the title carries the slide.
- HTML: the hero glow sits on the full-width section, edge to edge; a glow clipped to a centered content wrapper is a finding.

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

The references are a snapshot. When the brand voice changes, update
`sightly-brand-voice/references/brand-voice-full.md`; when the design tokens change, update the files in
`sightly-visual-brand/references/`. This skill picks up the change with no edit of its own.

## What this skill does not do

- It does not build strategy, personas, or a media plan.
- It does not apply changes without confirmation.
- It does not redefine or invent brand guidelines.

---

*End of Sightly Brand Check skill.*
