# Sightly Master Deck — Visual Design System

**Source:** Google Slides "Copy of Sightly Overview" (51 slides)
**Captured:** June 29, 2026
**How:** Every value below was read directly from the slides' underlying render — exact color codes, gradient definitions, font names and sizes — not estimated by looking at pixels. Companion file: `sightly-design-tokens.json` (the same values in machine-readable form for tools/AI).

---

## How to read this document

This is written for anyone, including people who have never opened a design tool. A few terms used throughout:

- **Hex code** — the six-character code (like `#00AEEF`) that names an exact color. Same code = same color, every time.
- **Gradient** — a smooth fade from one color (or transparency) to another.
- **Opacity** — how see-through something is, from 0% (invisible) to 100% (solid).
- **pt (point)** — the unit for font size. Bigger number = bigger text.
- **Token** — a named, reusable value (e.g. "brand cyan"). Naming a value lets everyone use the *same* one instead of guessing.

The deck is built on a **dark theme**: content sits on near-black backgrounds, with a bright cyan as the signature color and a few supporting accents.

---

## 1. The look in one paragraph

Every slide sits on **black**. The signature visual is a **soft cyan glow** that fades up out of the black (the "hero sweep"), often combined with large, soft **organic black blob shapes**. Text is **white and off-white** in the **Inter** typeface. One bright **cyan** (`#00AEEF`) carries the brand, supported by a **purple**, an **orange-red**, and occasional **green**. Section-break slides reuse the exact same glow, just recolored (purple, red, pink, etc.). Numbers and stats are shown big, in a **purple gradient**, with **hand-drawn cyan accent marks** (circles, underlines, arrows). It reads as modern, high-contrast, and tech-forward.

---

## 2. Colors

### 2.1 Core (use these constantly)

| Token | Hex | What it's for |
|---|---|---|
| Background — black (base dark) | `#000000` | The main slide background. Adopted as a **base dark** to match the deck's newer, blacker format. |
| Background — near-black (base dark) | `#111111` | Large dark panels and most slide bodies. The second **base dark**. |
| Surface — dark | `#2C2C2C` | Cards/panels raised slightly off the black. |
| Text — primary | `#FFFFFF` | Headlines, key labels, the logo. |
| Text — body | `#EEEEEE` | Default paragraph text. (This is the single most-used color in the whole deck.) |
| Text — muted | `#595959` | Secondary / de-emphasized text. |

> **Base darks vs. the official guide:** the official palette's darkest colors are **Sightly Black `#111619`** and **Sightly Black 02 `#121212`**. The deck now runs on pure **`#000000` and `#111111`** — blacker and flatter. Those two are the **base darks** going forward, and the official guide should be updated to include them.

### 2.2 Brand cyan (the signature)

| Token | Hex | What it's for |
|---|---|---|
| Brand cyan | `#00AEEF` | The Sightly color. Logo accent, highlights, hand-drawn marks, primary emphasis. |
| Cyan — deep | `#1CA0DA` | The saturated end of the hero glow. |
| Cyan — steel | `#295572` | Muted steel-cyan for table headers and data cards. |
| Cyan — pale tint | `#E9F8FF` | Very light fill for chips/cells (e.g. the moment-category grid). |
| Cyan — mid tint | `#BFE1FB` | A slightly deeper pale-cyan chip fill. |

### 2.3 Accents (use sparingly, for meaning)

| Token | Hex | What it's for |
|---|---|---|
| Purple *(Mentality Purple)* | `#7B61FF` | Emphasis text, big stat numbers, the "Understand Culture" pillar, the Appendix section. |
| Orange *(Sightly Orange)* | `#FF6F07` | The "Activate Smarter" pillar; energy / alert moments. **The deck uses `#EA430F` — that's drift; use `#FF6F07`.** |
| Teal *(Mentality Teal)* | `#6FEABC` | Positive / "available" highlights and glows. |
| Red | `#CC0000` | YouTube section; negative / decline. *(Not in the official palette.)* |
| Pink-red | `#FF2D55` | The TikTok section divider. *(Not in the official palette.)* |

### 2.4 Steel-blue surfaces (cards, tables, data panels)

A family of dark blue-grays used behind data: `#333D47` (primary), `#36434D`, `#455560`, `#5D7E95`, plus deep navy `#00354A` in gradient panels.

### 2.5 Light-mode neutrals (for the occasional light slide/card)

White `#FFFFFF`, then `#F9FAFB` → `#F5F5F5` → `#DDDDDD` as you go slightly darker, with slate-gray `#94A3B8` for secondary text on light.

> **Rule of thumb:** if you only remember five colors, remember **black `#000000`, off-white `#EEEEEE`, brand cyan `#00AEEF`, purple `#7B61FF`, and steel `#333D47`.**

### 2.6 Complete official palette (Sightly + BrandMentality)

Every color in the official brand guide, so nothing is missed:

- **Sightly — Primary:** Sightly Slate `#333D47` · Light Grey `#EEEEEE` · Dark Grey `#455560` · Sightly Blue `#00AEEF`
- **Sightly — Secondary:** Medium Grey `#D4D9D9` · Sightly Orange `#FF6F07` · Dark Blue `#295572` · Light Blue `#BFE1FB`
- **Sightly — Gradients / darks:** Dark Blue v2 `#34546F` · Sightly Black `#111619` · Sightly Black 02 `#121212` · Grey Gradient · Blue Gradient
- **BrandMentality — Primary:** Mentality Teal `#6FEABC` · Mentality Grey `#A0A3A3` · Mentality Purple `#7B61FF` · Light Grey `#EEEEEE`
- **BrandMentality — Secondary:** Sightly Slate `#333D47` · Sightly Blue `#00AEEF`
- **BrandMentality — Gradients:** Mentality Tri-Gradient (two stacked shapes) · Purple Gradient · Teal Gradient
- **BrandMentality — Specialty (rare):** Mentality Black `#282828` · Mentality Green `#36F518` · Text Color Over Mentality Teal `#065F46`

---

## 3. Gradients

### 3.1 The "hero sweep" — the signature gradient

This one gradient creates most of the deck's personality. It is **not** a simple two-color blend. It works like this:

> Take the section color and **fade it up out of the black** — it stays almost constant while its opacity climbs from near-zero to nearly solid, top to bottom.

The net effect is **a glow of color rising out of darkness**.

The same sweep is **recolored per section**, which is how the deck signals where you are:

| Section | Fades up to | 
|---|---|
| Title / brand | Cyan `#1CA0DA` |
| Neutral dark divider | Dark slate `#333D47` |
| Appendix / strategy | Purple `#8F7EFF` |
| YouTube | Red `#FF0000` |
| TikTok | Pink-red `#FF2D55` |

**CSS approximation (blue version):**

```css
background: linear-gradient(180deg,
  rgba(0,174,239,0.04) 0%,
  rgba(48,159,204,0.25) 25%,
  rgba(35,160,213,0.46) 50%,
  rgba(31,160,216,0.67) 75%,
  rgba(28,160,218,0.88) 100%);
```

To make any other section, keep the structure and swap the end color. Exact stop-by-stop values are in `sightly-design-tokens.json`.

### 3.2 Glow gradients (highlights)

- **Purple Gradient (BrandMentality)** — Mentality Purple `#4F46E5`→`#8F7EFF` at center fading to transparent. Behind featured elements / personas.
- **Teal Gradient (BrandMentality)** — Mentality Teal `#6FEABC` fading to transparent. Positive / "available" highlights.
- **Blue Gradient (Sightly)** — Sightly Blue `#00AEEF` fading to transparent. The cyan orb / swoosh accent.
- **Grey Gradient (Sightly)** — Light Grey `#EEEEEE` fading to white. Soft light panels / dividers.

### 3.3 Organic black blobs

Large, soft-edged black shapes are layered over the hero sweep on title and divider slides. They're built with black-to-transparent feathered edges (used as masks) so they melt into the background. This is what gives the title slides their distinctive "carved out of darkness" feel.

### 3.4 Official named gradients (brand guide)

Reference these by their brand-guide names:

- **Sightly:** **Grey Gradient**, **Blue Gradient**, plus the **hero sweep** and its section recolors.
- **BrandMentality:** **Mentality Tri-Gradient** — two stacked shapes blending Mentality Purple `#7B61FF` into Mentality Teal `#6FEABC` with a Sightly Blue `#00AEEF` transition — plus the **Purple Gradient** and **Teal Gradient**.

---

## 4. Typography

**Typeface: Inter** for everything. (Set fallbacks to `Inter, 'Helvetica Neue', Arial, sans-serif`.)

**Weights in use:** Light (300), Regular (400), and Bold (700) do most of the work, with **Inter Black (900) as the display weight** for hero stats and big headline numbers — used heavily (e.g. 244 runs in the Media Kit). Medium (500), SemiBold (600), and ExtraBold (800) appear occasionally. **Default pairing: Regular for body, Bold for headings/emphasis, Black (900) for hero stats.**

**Type scale (the intentional levels):**

| Level | Size (pt) | Use |
|---|---|---|
| Display XL | 75 (up to 88–111) | Giant hero stat numerals |
| Display | 60 | Large impact numbers |
| Title | 45 | Slide titles |
| Heading | 33 | Section / card-group headings |
| Subhead | 23 | Sub-headlines, pillar labels |
| Lead | 19 | Intro paragraph |
| Body | 15 | Default paragraph text |
| Body small | 13 | Dense body / card copy |
| Caption | 11 | Captions, labels |
| Fine | 9 | Footnotes, source lines |

> **Note:** the deck also contains a lot of tiny 4–10pt text. Almost all of that comes from **screenshots pasted into slides** (product UI, dense tables) — it's *content*, not part of the type system. Don't treat those sizes as type rules.

**Colored emphasis:** instead of only bolding, key phrases inside paragraphs are **colored inline** — usually **cyan `#00AEEF`** or **purple `#7B61FF`**. This is a recurring, on-brand habit worth keeping.

---

## 5. Shapes & layout

- **Slide size:** 16:9 widescreen.
- **Cards:** rounded corners (roughly 12–16px at full size), usually a **1px border colored to match the section accent** (cyan / purple / orange) over a dark steel or near-black fill.
- **Chips** (small labels, e.g. the moment grid): large/pill rounding, pale-cyan fill with cyan text; the featured chip is solid cyan.
- **Footer:** a small white Sightly logo sits in the lower-left of content slides.

---

## 6. Reusable components

These are the repeating building blocks. Reuse them rather than inventing new layouts.

1. **Title slide** — black + blue hero sweep + organic black blobs + centered white Sightly logo.
2. **Section divider** — same hero sweep recolored to the section, organic blob, a short title lower-left in white, small Sightly mark. (This is how the deck changes chapters — YouTube, TikTok, Appendix, etc.)
3. **Stat-callout bar** — a dark rounded panel holding a row of very large **purple-gradient numbers** (75pt+), each with a **hand-drawn cyan accent** (circle / underline / arrow / check) and a small label beneath. Used for headline metrics (e.g. 2B / 18M / 15k+ / 200k).
4. **Three-pillar comparison** — three columns with **italic colored headers** in the cyan / purple / orange triad; each column is a stack of rounded **bordered cards** (border matches the column color) with a bold white title and off-white body.
5. **Moment-category grid** — a cyan header pill above a grid of pale-cyan rounded chips; one featured chip is solid cyan.
6. **Dual-column bullets** — bulleted copy (with colored emphasis) on the left, a supporting visual/grid/screenshot on the right.
7. **Data table** — steel-blue header and rows, light text; for metrics and pricing.
8. **Case-study slide** — embedded product screenshots/photos on black with captions.
9. **Footer mark** — small white Sightly logo, lower-left.

---

## 7. QA — cleanup list (reconciled against the official brand palette)

Cross-checked against the official Sightly / BrandMentality palette. "Canonical" = the official value to keep; everything else is drift to replace.

**Resolved by the official palette — keep the official value:**

1. **Brand cyan — 5 versions** (`#00AEEF`, `#02B0F1`, `#01AEEF`, `#00ADEF`, `#02B1F1`). Official **Sightly Blue = `#00AEEF`**. Keep it, replace the other four. Biggest single cleanup.

2. **Light-blue chip — `#BFE1FB` vs `#BEE1FB`.** Official **Light Blue = `#BFE1FB`**; `#BEE1FB` is a one-digit typo.

3. **Purple — 4 versions** (`#7B61FF`, `#8F7EFF`, `#4F46E5`, `#5A42D2`). Official **Mentality Purple = `#7B61FF`**. Keep it; the rest are gradient/drift.

4. **Steel-blues map to official names:** `#333D47` = Sightly Slate, `#455560` = Dark Grey, `#295572` = Dark Blue, `#34546F` = Dark Blue v2. `#36434D` and `#5D7E95` are off-palette — consolidate them.

5. **"Mint green" is actually Mentality Teal `#6FEABC`** — corrected the name.

**New drifts the official palette exposes:**

6. **Orange is wrong.** Deck uses `#EA430F`; official **Sightly Orange = `#FF6F07`**. Replace.

7. **Greys drift:** deck `#DDDDDD` vs official **Medium Grey `#D4D9D9`**; deck `#A1A4A4` vs official **Mentality Grey `#A0A3A3`**.

8. **Off-brand greens:** `#2CA679`, `#6AA84F`, `#137333` aren't brand colors (likely chart defaults). Official greens are Mentality Teal `#6FEABC` and specialty Mentality Green `#36F518`.

9. **Stray link blue `#1A73E8`** (~51×) — the Google-Docs default, not in the palette. Restyle links to Sightly Blue.

**Not a palette issue (but still worth fixing):**

10. **Fonts:** Inter is the system font; **Open Sans / Roboto / Arial** appear from pasted content — normalize to Inter.

11. **Type-scale noise:** many 4–10pt sizes are embedded screenshots, not real text — ignore them and use the scale in Section 4.

**Update the official guide itself:**

12. **The darker format.** The guide's darkest values are Sightly Black `#111619` / `#121212`, but the deck now runs on pure **`#000000` and `#111111`**. These are adopted as the **base darks** here; add them to the official palette.

---

## 8. Quick-start defaults (if you're building a new slide right now)

- Background: `#000000`
- Body text: `#EEEEEE`, Inter Regular, ~15pt
- Headline: `#FFFFFF`, Inter Bold, ~45pt
- Highlight a phrase: color it `#00AEEF` (cyan) or `#7B61FF` (purple)
- Need a "wow" background: apply the **hero sweep** (Section 3.1)
- Starting a new section: use a **divider** with the sweep recolored
- Showing a big number: **stat-callout** style — big purple-gradient numeral + cyan hand-drawn accent
- Card: dark fill, 1px accent-colored border, rounded corners
