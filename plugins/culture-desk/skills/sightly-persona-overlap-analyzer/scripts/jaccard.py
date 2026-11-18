#!/usr/bin/env python3
"""
Sightly Persona Overlap Analyzer: Jaccard calculator.

Deterministic set math for persona overlap. Two modes:

  pair (default)  Per-pair tables by dimension, with the In-Market read.
                  Built for the merge / keep-separate question on 2-3 personas.
  --matrix        For a persona SET (3+): one N x N overlap matrix, per-dimension
                  matrices, the core every persona carries, and each persona's
                  unique segments with the share of its own list they make up.
                  Built for "how different are these audiences" slides.

Usage:
    python jaccard.py input.json                 # pair mode
    python jaccard.py input.json --matrix        # matrix mode
    python jaccard.py input.json --matrix --json # also write overlap_result.json
    python jaccard.py input.json --matrix --csv  # also write overlap_matrix.csv

Input JSON (include whichever dimensions you have real data for):
{
  "source": "Sightly Persona Builder, <Brand> Brand Profile, persona IDs, read <date>",
  "personas": {
    "Persona A": {"pb_categories": [...], "pb_genres": [...], "pb_ctv": [...], "pb_olv": [...]},
    "Persona B": {...}
  },
  "content": {                       # optional: content-inventory overlap
    "Persona A": ["https://page", "youtube.com/channel/...", ...],
    "Persona B": [...]
  }
}

Known dimension keys: yt_affinity, yt_topics, yt_in_market, tiktok_interests
(YouTube / TikTok targeting) and pb_categories, pb_genres, pb_ctv, pb_olv
(Persona Builder programmatic categories, genres, CTV segments, OLV segments).
Any other key is accepted and labelled from its name.

Definitions (state them on the slide notes):
- Pair overlap (matrix cell) = segments both carry / segments either carries,
  pooled across all dimensions, with each segment keyed by its dimension so a
  CTV "Cooking" and an OLV "Cooking" count as two segments.
- Core = segments every persona in the set carries.
- Unique segments = segments only that persona carries. Unique % = unique count /
  that persona's own segment count.
Segment names are normalized (case, spacing, punctuation, & vs and) first.
"""

import csv
import json
import re
import sys
from itertools import combinations

DIMENSIONS = [
    ("yt_affinity", "YT Affinity"),
    ("yt_topics", "YT Topics"),
    ("tiktok_interests", "TikTok Interests"),
    ("yt_in_market", "YT In-Market"),
    ("pb_categories", "Categories"),
    ("pb_genres", "Genres"),
    ("pb_ctv", "CTV segments"),
    ("pb_olv", "OLV segments"),
]
LABEL = dict(DIMENSIONS)

ALIASES = {
    "affinity": "yt_affinity", "youtube_affinity": "yt_affinity",
    "topics": "yt_topics", "youtube_topics": "yt_topics",
    "in_market": "yt_in_market", "inmarket": "yt_in_market", "youtube_in_market": "yt_in_market",
    "tiktok": "tiktok_interests", "interests": "tiktok_interests",
    "categories": "pb_categories", "programmatic_categories": "pb_categories",
    "genres": "pb_genres",
    "ctv": "pb_ctv", "ctv_segments": "pb_ctv",
    "olv": "pb_olv", "olv_segments": "pb_olv",
}


def normalize(name):
    s = name.strip().lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def canonical_key(k):
    k2 = k.strip().lower().replace(" ", "_").replace("-", "_")
    return ALIASES.get(k2, k2)


def label(key):
    return LABEL.get(key, key.replace("_", " ").title())


def dim_order(personas):
    keys = {k for d in personas.values() for k in d}
    known = [k for k, _ in DIMENSIONS if k in keys]
    return known + sorted(keys - set(known))


def load(path):
    with open(path) as f:
        data = json.load(f)
    raw = data.get("personas", data)
    personas = {}
    for pname, dims in raw.items():
        personas[pname] = {}
        for k, vals in dims.items():
            personas[pname][canonical_key(k)] = {normalize(v): v for v in vals}
    content = {p: {normalize(u): u for u in v} for p, v in data.get("content", {}).items()}
    return personas, content, data.get("source", "")


def jaccard(a_map, b_map):
    a, b = set(a_map), set(b_map)
    if not a and not b:
        return None, [], 0, 0
    inter, union = a & b, a | b
    return len(inter) / len(union), sorted(a_map[k] for k in inter), len(inter), len(union)


def pct(x, dp=1):
    """Percent with half-up rounding (12.5% -> 13%), matching how slides are read."""
    if x is None:
        return "n/a"
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(1).scaleb(-dp) if dp else Decimal(1)
    return f"{Decimal(str(x * 100)).quantize(q, rounding=ROUND_HALF_UP)}%"


# ---------------- pair mode (unchanged behaviour) ----------------

def analyze_pair(dims_a, dims_b, order):
    rows, scores, shared = [], [], {}
    for key in order:
        a_map, b_map = dims_a.get(key, {}), dims_b.get(key, {})
        if not a_map and not b_map:
            continue
        score, sh, n_i, n_u = jaccard(a_map, b_map)
        rows.append((label(key), score, n_i, n_u))
        scores.append(score)
        shared[label(key)] = sh
    return rows, (sum(scores) / len(scores) if scores else 0.0), shared


def pair_report(personas):
    order = dim_order(personas)
    out = ["# Persona Overlap Analysis (Jaccard)\n"]
    for a, b in combinations(personas, 2):
        rows, avg, shared = analyze_pair(personas[a], personas[b], order)
        out += [f"\n## {a}  ×  {b}\n", "| Dimension | Jaccard | Shared / Union |", "|---|---|---|"]
        for lab, score, n_i, n_u in rows:
            flag = "  ← highest-intent signal" if lab == "YT In-Market" else ""
            out.append(f"| {lab}{flag} | {pct(score)} | {n_i} / {n_u} |")
        out.append(f"| **Average** | **{pct(avg)}** | |")
        im = next((r for r in rows if r[0] == "YT In-Market"), None)
        if im:
            out.append(f"\n**In-Market read:** {im[2]} of {im[3]} in-market audiences are identical "
                       f"({pct(im[1])}). This is the bid-against-yourself risk — "
                       f"the two personas are chasing the same purchase-intent categories.")
            if shared.get("YT In-Market"):
                out.append("\nShared In-Market segments: " + ", ".join(shared["YT In-Market"]) + ".")
        out.append("\n_Recommendation is a strategist call — read the shared segments, not just "
                   "the number. High In-Market overlap + different convert-me messaging usually "
                   "points to: merge the targeting, split the creative._")
    return "\n".join(out), None


# ---------------- matrix mode ----------------

def pooled(dims, order):
    m = {}
    for k in order:
        for n, disp in dims.get(k, {}).items():
            m[f"{k}:{n}"] = (k, disp)
    return m


def matrix_report(personas, content, source):
    names, order = list(personas), dim_order(personas)
    P = {n: pooled(personas[n], order) for n in names}
    res = {"source": source, "definitions": {
        "pair": "segments both carry / segments either carries, pooled across dimensions",
        "unique_pct": "segments only this persona carries / this persona's segment count"},
        "dimensions": [label(k) for k in order], "pairs": {}, "per_dimension": {}, "core": {}, "unique": {}}

    out = ["# Persona Overlap Matrix (Jaccard)\n"]
    if source:
        out.append(f"Source: {source}\n")
    out.append("Segment counts per persona:\n")
    out += ["| Persona | " + " | ".join(label(k) for k in order) + " | Total |",
            "|---|" + "---|" * (len(order) + 1)]
    for n in names:
        out.append(f"| {n} | " + " | ".join(str(len(personas[n].get(k, {}))) for k in order) + f" | {len(P[n])} |")
    missing = [(n, label(k)) for n in names for k in order if not personas[n].get(k)]
    if missing:
        out.append("\nOne thing to flag: missing lists, scored as empty: " +
                   "; ".join(f"{n} {d}" for n, d in missing) + ".")

    # pooled matrix
    M = {}
    for a, b in combinations(names, 2):
        s, _, n_i, n_u = jaccard(P[a], P[b])
        M[(a, b)] = M[(b, a)] = s
        res["pairs"][f"{a} | {b}"] = {"jaccard": round(s, 4), "shared": n_i, "union": n_u}
    out += ["\n## Overlap matrix (all segment types pooled)\n",
            "| | " + " | ".join(names) + " |", "|---|" + "---|" * len(names)]
    for a in names:
        out.append(f"| **{a}** | " + " | ".join("—" if a == b else pct(M[(a, b)], 0) for b in names) + " |")
    ranked = sorted(((M[(a, b)], a, b) for a, b in combinations(names, 2)), reverse=True)
    lo, hi = ranked[-1], ranked[0]
    out.append(f"\nRange: {pct(lo[0], 0)} ({lo[1]} and {lo[2]}) to {pct(hi[0], 0)} ({hi[1]} and {hi[2]}).")
    out.append("\nMost-overlapping pairs: " + "; ".join(f"{a} and {b} {pct(s, 0)}" for s, a, b in ranked[:3]) + ".")

    # per-dimension
    out.append("\n## By segment type (pair range)\n")
    out += ["| Segment type | Lowest pair | Highest pair |", "|---|---|---|"]
    for k in order:
        sc = []
        for a, b in combinations(names, 2):
            s, *_ = jaccard(personas[a].get(k, {}), personas[b].get(k, {}))
            if s is not None:
                sc.append((s, a, b))
                res["per_dimension"].setdefault(label(k), {})[f"{a} | {b}"] = round(s, 4)
        if sc:
            sc.sort()
            out.append(f"| {label(k)} | {pct(sc[0][0], 0)} ({sc[0][1]} / {sc[0][2]}) | "
                       f"{pct(sc[-1][0], 0)} ({sc[-1][1]} / {sc[-1][2]}) |")

    # core
    core = set.intersection(*(set(P[n]) for n in names))
    first = P[names[0]]
    out.append(f"\n## Core: segments all {len(names)} carry ({len(core)})\n")
    for k in order:
        items = sorted(first[c][1] for c in core if first[c][0] == k)
        if items:
            out.append(f"- {label(k)}: " + ", ".join(items))
            res["core"][label(k)] = items
    if not core:
        out.append("- None.")

    # unique
    out.append("\n## Unique segments (carried by no other persona)\n")
    out += ["| Persona | Unique | Own total | Unique % |", "|---|---|---|---|"]
    detail = []
    for n in names:
        others = set().union(*(set(P[m]) for m in names if m != n))
        u = set(P[n]) - others
        share = len(u) / len(P[n]) if P[n] else 0
        out.append(f"| {n} | {len(u)} | {len(P[n])} | {pct(share, 0)} |")
        by = {}
        for c in u:
            by.setdefault(P[n][c][0], []).append(P[n][c][1])
        res["unique"][n] = {"count": len(u), "total": len(P[n]), "pct": round(share, 4),
                            "segments": {label(k): sorted(by[k]) for k in order if k in by}}
        detail.append(f"\n**{n}**")
        for k in order:
            if k in by:
                detail.append(f"- {label(k)}: " + ", ".join(sorted(by[k])))
        if not by:
            detail.append("- None.")
    out += detail

    # content overlap
    if content:
        out.append("\n## Content overlap (pages, channels, videos)\n")
        shared_any = False
        res["content"] = {}
        for a, b in combinations([n for n in names if n in content], 2):
            inter = set(content[a]) & set(content[b])
            if inter:
                shared_any = True
                items = sorted(content[a][i] for i in inter)
                res["content"][f"{a} | {b}"] = items
                out.append(f"- {a} and {b}: {len(items)} shared: " + "; ".join(items))
        if not shared_any:
            out.append("- No item appears in two personas' inventories.")

    out.append("\n_Segment overlap describes the targeting lists, not measured audiences._")
    return "\n".join(out), (res, names, M)


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return
    personas, content, source = load(args[0])
    if len(personas) < 2:
        print("Need at least two personas to compare.")
        sys.exit(1)
    if "--matrix" in args:
        text, (res, names, M) = matrix_report(personas, content, source)
        print(text)
        if "--json" in args:
            json.dump(res, open("overlap_result.json", "w"), indent=2)
            print("\n[wrote overlap_result.json]")
        if "--csv" in args:
            with open("overlap_matrix.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow([""] + names)
                for a in names:
                    w.writerow([a] + ["" if a == b else round(M[(a, b)], 4) for b in names])
            print("[wrote overlap_matrix.csv]")
    else:
        text, _ = pair_report(personas)
        print(text)


if __name__ == "__main__":
    main()
