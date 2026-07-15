#!/usr/bin/env python3
"""
Sightly Persona Overlap Analyzer — Jaccard calculator.

Deterministic set math for persona consolidation analysis. Given each persona's
real Persona Builder targeting lists, computes Jaccard similarity per dimension
(YouTube Affinity, YouTube Topics, YouTube In-Market, TikTok Interests), an
average across available dimensions, and the exact shared segments per pair.

Usage:
    python jaccard.py input.json
    python jaccard.py input.json --json          # machine-readable output too

Input JSON shape (include whichever dimensions you have real data for):
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

Notes:
- In-Market overlap is the highest-stakes signal (active purchase intent — the
  "bidding against yourself" risk). The report flags it explicitly.
- Segment names are normalized (trimmed, lowercased, punctuation/spacing
  collapsed) before comparison so trivial formatting differences don't
  understate real overlap.
"""

import json
import re
import sys
from itertools import combinations

# Canonical dimension keys -> human labels, in report order.
DIMENSIONS = [
    ("yt_affinity", "YT Affinity"),
    ("yt_topics", "YT Topics"),
    ("tiktok_interests", "TikTok Interests"),
    ("yt_in_market", "YT In-Market"),  # most decision-relevant; listed last so it reads just above the average
]

# Accept a few common aliases so input files are forgiving.
ALIASES = {
    "affinity": "yt_affinity",
    "youtube_affinity": "yt_affinity",
    "topics": "yt_topics",
    "youtube_topics": "yt_topics",
    "in_market": "yt_in_market",
    "inmarket": "yt_in_market",
    "youtube_in_market": "yt_in_market",
    "tiktok": "tiktok_interests",
    "interests": "tiktok_interests",
}


def normalize(name):
    """Lowercase, strip, collapse whitespace and punctuation for fair comparison."""
    s = name.strip().lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def canonical_key(k):
    k2 = k.strip().lower().replace(" ", "_").replace("-", "_")
    return ALIASES.get(k2, k2)


def load(path):
    with open(path) as f:
        data = json.load(f)
    personas = data.get("personas", data)  # allow top-level personas or bare dict
    cleaned = {}
    for pname, dims in personas.items():
        cleaned[pname] = {}
        for k, vals in dims.items():
            ck = canonical_key(k)
            # keep display->normalized map so we can show real segment names later
            norm_map = {}
            for v in vals:
                norm_map[normalize(v)] = v
            cleaned[pname][ck] = norm_map
    return cleaned


def jaccard(a_map, b_map):
    a, b = set(a_map), set(b_map)
    if not a and not b:
        return None, [], 0, 0
    inter = a & b
    union = a | b
    score = len(inter) / len(union) if union else 0.0
    # return shared segments using persona A's original display names
    shared = sorted(a_map[k] for k in inter)
    return score, shared, len(inter), len(union)


def analyze_pair(name_a, dims_a, name_b, dims_b):
    rows = []
    scores = []
    shared_by_dim = {}
    for key, label in DIMENSIONS:
        a_map = dims_a.get(key, {})
        b_map = dims_b.get(key, {})
        if not a_map and not b_map:
            continue
        score, shared, n_inter, n_union = jaccard(a_map, b_map)
        rows.append((label, score, n_inter, n_union))
        scores.append(score)
        shared_by_dim[label] = shared
    avg = sum(scores) / len(scores) if scores else 0.0
    return rows, avg, shared_by_dim


def pct(x):
    return f"{x * 100:.1f}%"


def report(personas):
    names = list(personas)
    out = []
    out.append("# Persona Overlap Analysis (Jaccard)\n")
    for a, b in combinations(names, 2):
        rows, avg, shared = analyze_pair(a, personas[a], b, personas[b])
        out.append(f"\n## {a}  ×  {b}\n")
        out.append("| Dimension | Jaccard | Shared / Union |")
        out.append("|---|---|---|")
        for label, score, n_inter, n_union in rows:
            flag = "  ← highest-intent signal" if label == "YT In-Market" else ""
            out.append(f"| {label}{flag} | {pct(score)} | {n_inter} / {n_union} |")
        out.append(f"| **Average** | **{pct(avg)}** | |")

        im = next((r for r in rows if r[0] == "YT In-Market"), None)
        if im:
            out.append(
                f"\n**In-Market read:** {im[2]} of {im[3]} in-market audiences are "
                f"identical ({pct(im[1])}). This is the bid-against-yourself risk — "
                f"the two personas are chasing the same purchase-intent categories."
            )
            if shared.get("YT In-Market"):
                out.append(
                    "\nShared In-Market segments: " + ", ".join(shared["YT In-Market"]) + "."
                )
        out.append(
            "\n_Recommendation is a strategist call — read the shared segments, not just "
            "the number. High In-Market overlap + different convert-me messaging usually "
            "points to: merge the targeting, split the creative._"
        )
    return "\n".join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    want_json = "--json" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)
    personas = load(args[0])
    if len(personas) < 2:
        print("Need at least two personas to compare.")
        sys.exit(1)
    print(report(personas))
    if want_json:
        blob = {}
        for a, b in combinations(list(personas), 2):
            rows, avg, shared = analyze_pair(a, personas[a], b, personas[b])
            blob[f"{a} x {b}"] = {
                "by_dimension": {r[0]: r[1] for r in rows},
                "average": avg,
                "shared_segments": shared,
            }
        with open("overlap_result.json", "w") as f:
            json.dump(blob, f, indent=2)
        print("\n[wrote overlap_result.json]")


if __name__ == "__main__":
    main()
