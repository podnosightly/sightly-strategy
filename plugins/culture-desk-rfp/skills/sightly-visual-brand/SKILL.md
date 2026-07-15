---
name: sightly-visual-brand
description: >-
  Applies Sightly's codified visual design system — canonical brand colors and design tokens, the
  signature "hero sweep" gradients, the Inter type scale, and recurring slide components — when
  building or reviewing Sightly slides, decks, HTML, or branded assets; and can refresh or extend
  the tokens by extracting them directly from a deck. Use when the user says "build a Sightly
  slide/deck", "use our design tokens", "make this on-brand visually", "apply the brand colors /
  gradients", "what's the Sightly hero gradient", "check this deck is on-brand", "audit the colors",
  "codify this deck's design system", or "extract brand tokens from this deck". Not for written copy
  (use sightly-brand-voice).
---

# Sightly Visual Brand

Apply Sightly's visual design system to any asset this skill builds or reviews, using the exact
values in `references/design-tokens.json` (machine-readable) and `references/design-system-spec.md`
(plain-language explanation). Load `references/design-tokens.json` before building or auditing.

## Canonical values (quick reference — tokens file is authoritative)

Base darks: `#000000` and `#111111`. Body text: `#EEEEEE` (Light Grey) on dark; headlines
`#FFFFFF`. Brand cyan (Sightly Blue): **`#00AEEF`**. Accent purple (Mentality Purple): `#7B61FF`.
Accent orange (Sightly Orange): `#FF6F07`. Teal (Mentality Teal): `#6FEABC`. Steel surfaces: Sightly
Slate `#333D47`, Dark Grey `#455560`, Dark Blue `#295572`, Dark Blue v2 `#34546F`. Light Blue chip
`#BFE1FB`. Font: **Inter** (Regular 400 / Bold 700, Light 300).

Signature "hero sweep" gradient (blue version, vertical): a soft cyan glow that fades up out of
black — opacity ramps ~4% to ~88%, color near-constant cyan.

```css
background: linear-gradient(180deg,
  rgba(0,174,239,0.04) 0%,
  rgba(48,159,204,0.25) 25%,
  rgba(35,160,213,0.46) 50%,
  rgba(31,160,216,0.67) 75%,
  rgba(28,160,218,0.88) 100%);
```

Recolor the sweep per section by swapping the end color: dark `#333D47`, purple `#8F7EFF`, red
`#FF0000`, pink `#FF2D55`.

## When building slides / assets

1. Load `references/design-tokens.json`.
2. Background `#000000`; body copy Inter Regular ~15pt in `#EEEEEE`; headlines Inter Bold ~45pt in
   `#FFFFFF`.
3. Highlight key phrases inline in `#00AEEF` (cyan) or `#7B61FF` (purple).
4. Use the hero sweep for title/section backgrounds; use the recurring components in the spec
   (stat-callout bar, three-pillar comparison, moment grid, data table, section divider).
5. Only use canonical hexes. Do not introduce a new near-duplicate of an existing color.

## When auditing a deck / asset for drift

Compare every color used against the tokens file. For each off-value color, report the drift and the
canonical value to use. Known drift to catch: any cyan that is not `#00AEEF` (e.g. `#02B0F1`,
`#01AEEF`); orange `#EA430F` should be `#FF6F07`; `#DDDDDD` should be Medium Grey `#D4D9D9`;
`#A1A4A4` should be Mentality Grey `#A0A3A3`; `#BEE1FB` should be `#BFE1FB`; the Google-Docs link
blue `#1A73E8` is off-brand. Also flag non-Inter fonts (Open Sans / Roboto / Arial from pasted
content). See `references/design-system-spec.md` section 7 for the full cleanup logic.

## When extracting / refreshing tokens from a deck

Use this method (it produces exact values, not eyeballed ones):

1. Open the deck in the browser (Google Slides editor). Confirm the true slide count — the filmstrip
   virtualizes, so scroll it fully (using real mouse-wheel scroll, not programmatic scrollTop) to
   render every thumbnail before counting or extracting.
2. Read each slide's rendered SVG: exact `fill` hexes, `linearGradient`/`radialGradient` stops
   (offset, stop-color, stop-opacity) and gradient transform, and text `font-family` / `font-size`
   (font-size in px ÷ 1.3333 = pt) / `font-weight` / fill.
3. Aggregate across all slides: count each color, each font size, each weight; dedupe gradients.
4. Flag near-duplicate colors as drift and pick one canonical value per intended color.
5. Reconcile against the official brand palette (Sightly / BrandMentality): adopt official names,
   keep `official: true` values, mark `driftInDeck`.
6. Update `references/design-tokens.json` and `references/design-system-spec.md`, and write the
   result for a non-designer (name every color, explain the gradients, list the cleanup items).

## Rules

- The tokens file is the source of truth; this body is a summary.
- Never invent a color, gradient, or measurement that is not in the tokens file or read from a real
  artifact.
- Reds/pinks (`#CC0000`, `#FF2D55`) and section-gradient end colors are used in the deck but are not
  yet in the official brand palette — treat as deck-only until confirmed.
