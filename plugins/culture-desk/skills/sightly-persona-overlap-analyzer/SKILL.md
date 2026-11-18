---
name: "sightly-persona-overlap-analyzer"
description: "Computes Jaccard overlap between Sightly personas from real Persona Builder targeting data. Two modes. Pair mode (2-3 personas) compares YouTube Affinity, Topics, In-Market and TikTok Interests, weights In-Market most heavily, and returns a merge / keep-separate / merge-with-split-creative recommendation. Matrix mode (a persona set) builds an N x N overlap matrix with percentages, the core segments every persona carries, and each persona's unique segments with a unique %, from Persona Builder categories, genres, CTV and OLV segments, plus optional content-inventory overlap. Use when a strategist asks \"do these overlap,\" \"should we consolidate these personas,\" \"overlap matrix,\" \"what makes each audience different,\" \"unique segments,\" or wants an efficiency or differentiation case. Requires real run data."
---

# Sightly Persona Overlap Analyzer

## What this skill does

Given the real targeting data for two or more personas, this skill measures how much they overlap and tells the strategist whether to run them as separate campaigns, merge them, or merge the targeting but keep the creative split. The core metric is **Jaccard similarity** (size of intersection ÷ size of union) computed per targeting dimension, plus an average.

It exists because two personas that look distinct in a deck can be statistically almost the same *buyer* — and running them separately means bidding against yourself on the highest-intent signals you have.

## Inputs required (real Persona Builder run data only)

This skill runs **only** on real Persona Builder export data — the actual segment lists produced by a run, for each persona:

- **YouTube Affinity** audiences
- **YouTube Topics**
- **YouTube In-Market** audiences
- **TikTok Interests**

If all that exists are proposed or bracketed interests (`[confirm via run]`) and no real run has happened yet, stop — you cannot compute a real overlap. Route the strategist to **`sightly-audience-architecture-builder`** to define or refine the personas, get a Persona Builder run, then return here with the exported lists. Never fabricate targeting lists to force a number.

## When this is the wrong skill

**This skill requires real Persona Builder run data.** If the personas only have proposed/bracketed interests (`[confirm via run]`), you cannot compute a real overlap — say so, and point the strategist to `sightly-audience-architecture-builder` to build the personas, then back here once a run exists. Do not fabricate targeting lists to force a number.

If the task is defining personas from a brief, that's `sightly-audience-architecture-builder`. If it's the media plan, that's `sightly-media-plan-builder`.

## Inputs the skill needs

For each persona, the actual segment lists from the run, across as many of these dimensions as available:

- **YouTube Affinity** audiences
- **YouTube Topics**
- **YouTube In-Market** audiences
- **TikTok Interests**

At minimum two personas with at least one shared dimension. If only some dimensions exist, compute on what's present and note the missing ones. Ask for the lists if they weren't provided — don't guess them.

## How to run the analysis (use the bundled script — don't do the math by hand)

The set math is deterministic, so it lives in a bundled script rather than being redone each run. Doing it by hand invites counting errors on numbers that end up in a client recommendation.

1. Put each persona's lists into a small JSON file. Shape (include whichever dimensions you have):

```json
{
  "personas": {
    "K-Beauty Skintellectual": {
      "yt_affinity":     ["Beauty Mavens", "Green Living Enthusiasts"],
      "yt_topics":       ["Skin Care", "Cosmetics"],
      "yt_in_market":    ["Skin Care Products", "Face Lotions"],
      "tiktok_interests":["Skincare", "Ingredients"]
    },
    "Dupe Hunter": {
      "yt_affinity":     ["Beauty Mavens", "Bargain Hunters"],
      "yt_topics":       ["Cosmetics", "Shopping"],
      "yt_in_market":    ["Skin Care Products", "Makeup & Cosmetics"],
      "tiktok_interests":["Skincare", "Deals"]
    }
  }
}
```

2. Run it:

```bash
python scripts/jaccard.py input.json
# add --json to also write overlap_result.json for reuse
```

The script normalizes segment names (case, spacing, punctuation, `&` vs `and`) before comparing, prints a per-dimension Jaccard table with the average, flags the In-Market row as the highest-intent signal, and lists the exact shared In-Market segments. It handles more than two personas by reporting every pair.

## Matrix mode: a persona set (overlap matrix, core, unique segments)

Use this when the question is how different a set of audiences is, not whether to merge two. Built on the Campbell's always-on deck (7 personas, Nov 2026), whose overlap and differences slides it reproduces exactly.

**Inputs.** For each persona, the Persona Builder output on the client's Brand Profile: programmatic categories (`pb_categories`), genres (`pb_genres`), CTV segments (`pb_ctv`) and OLV segments (`pb_olv`). The YouTube and TikTok keys also work. Add a `source` line (Brand Profile, persona IDs, read date). Optionally add `content`: each persona's page, channel and video URLs from its content inventory, after the drop list.

```bash
python scripts/jaccard.py input.json --matrix --json --csv
```

**What it returns.**

- **Overlap matrix:** one cell per pair, segments both carry divided by segments either carries, pooled across all segment types. Each segment is keyed by its type, so CTV "Cooking" and OLV "Cooking" count separately. Range and the three most-overlapping pairs are printed under it.
- **By segment type:** the lowest and highest pair for each type, to show where the overlap sits.
- **Core:** segments every persona carries. Recommend running these in one line rather than in every persona's line.
- **Unique segments:** per persona, the segments no other persona carries, listed by type, with Unique % = unique count / that persona's own count. Pick the slide examples from this list by hand: the ones that say most about life outside the category (Comfort Cravers: Soap Opera TV, Pop Culture, Audiobooks), never kids or parenting segments.
- **Content overlap** (if given): every page, channel or video in two personas' inventories.
- `overlap_result.json` and `overlap_matrix.csv` for the slide build.

Percentages round half-up (12.5% shows as 13%).

**Reading it.** Segment overlap describes the targeting lists, not measured audiences; say so in the slide notes. Persona Builder builds segments from the description we type, so similar descriptions produce similar lists. Low content overlap with moderate segment overlap is the usual pattern and argues for one SmartList per persona: the segments overlap, the pages don't.

**Slide notes must carry:** the definition of a cell, the segment types pooled, the Brand Profile and persona IDs with the read date, the range with its two pairs, the core list, and the Unique % definition.

## Interpretation

Treat these as judgment aids, not hard cutoffs — always read the segments, not just the number.

- **In-Market is the signal that matters most.** It reflects people actively researching and about to buy. High In-Market overlap means both personas are chasing the same purchase-intent categories, so separate campaigns bid against each other on your most valuable signals. Weight it heavily in the recommendation and call out how many In-Market audiences are identical.
- **Affinity and Topics overlap** describe shared interests/content, not intent — informative but lower-stakes.
- Higher average overlap strengthens the consolidation case; compare against prior pairs where useful for context (state them as comparisons, not benchmarks).

## The recommendation (three outcomes)

1. **Keep separate** — low overlap, especially low In-Market. The personas are genuinely different buyers.
2. **Merge** — high overlap across the board and the same creative would work for both.
3. **Merge targeting, split creative** — the sophisticated case, and often the right one: the personas are statistically the *same buyer* (high In-Market overlap) but *psychologically different customers* who convert on different messages. Recommend one unified campaign to capture targeting efficiency, run with distinct creative variants per mindset. This avoids bidding against yourself while preserving message precision — and it's a stronger client story: "both your audiences are shopping for the same products at the same time; rather than compete against yourself, run one campaign that speaks to each mindset differently."

Always name the tension explicitly when recommending option 3 (e.g. one wants ingredient/science credibility, the other wants trend/value proof).

## Output

Matrix mode adds `<client>-persona-overlap-matrix.md` (the script output plus the reading) and the JSON and CSV files.

Two things in the outputs folder:

1. **`<client>-persona-overlap.md`** — the Jaccard table(s), the shared-segment lists, the interpretation, and the recommendation with rationale.
2. **`<client>-persona-overlap-slide.md`** — slide-ready copy: the overlap headline (e.g. the In-Market %), the "same buyer, different mindset" framing, and the one-campaign-two-creatives recommendation as client-facing language.

## What this skill does not do

- It does not invent targeting data — real run required.
- It does not define personas or build boards — that's `sightly-audience-architecture-builder`.
- It does not build the media plan — that's `sightly-media-plan-builder`.

---

*End of Sightly Persona Overlap Analyzer skill.*

