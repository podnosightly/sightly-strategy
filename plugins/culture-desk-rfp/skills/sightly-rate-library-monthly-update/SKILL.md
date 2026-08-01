---
name: "sightly-rate-library-monthly-update"
description: "Monthly refresh of Sightly rate library — finds new media plans in Drive, extracts rates, merges into the master rate_library_full_v3 Google Sheet, regenerates summary_by_tactic_and_agency, and posts a formatted digest to #claude-strategy. Run on the 1st of each month."
---

# Sightly Rate Library Monthly Update

You are updating the Sightly Rate Library — CPM/CPV/CPC rates extracted from client media plans in Google Drive. Find new media plan files created or modified in the past 35 days that are not already in the library, extract their rates, merge them into the master, regenerate the summary, save everything back to Drive, and post a digest to Slack.

## ENVIRONMENT NOTES (learned from prior runs — read first)

- **The master library is a GOOGLE SHEET, not a CSV**: title `rate_library_full_v3`, data tab named `data`, in the "Rate Cards and Benchmarks" folder (ID: 19XFLRFr-CIWDMMp-0ZuA1id-VEjEZHBB). The summary is also a Google Sheet: `summary_by_tactic_and_agency` (single tab). Monthly delta CSVs named `rate_library_additions_YYYY-MM.csv` sit alongside as history — do not re-process them as media plans; they (and files named rate_library_*, summ_*) are pipeline files, not source plans.
- **The Drive connector cannot update, overwrite, or rename existing files.** Never create a second file with a canonical title. Deltas get NEW dated files; the master Sheet is updated via Sheets import (Step 6).
- **Any CSV uploaded via the connector MUST have a title ending in `.csv`** or Google Sheets' File > Import will reject it.
- **Large tool results (search pages, file downloads) are saved to disk** — parse them in bash (base64-decode the `content` field) rather than re-reading them into context. Large uploads: keep each create_file under ~45 KB of text; split bigger files into `_partN.csv` chunks.
- **Standing exclusions per Dan**: STARZ Michael plans (all MX Auction barter), Visit Montana FY26 International RFP (currency), StitchFix template (no rate-type column).

## STEP 1 — Load the current library

Download the `rate_library_full_v3` Google Sheet (export as CSV) from the Rate Cards and Benchmarks folder. Parse it; collect unique `source_file` values as the dedup list (normalize: strip .xlsx/.xls, collapse whitespace, lowercase). Also check for any `rate_library_additions_*` CSVs newer than the Sheet's modifiedTime — if one exists whose rows are not yet in the Sheet, include its unmerged rows in this month's merge (dedup at source_file level).

## STEP 2 — Search Drive for new media plan files

Search spreadsheets (Google Sheets + xlsx mimeTypes) modified in the last 35 days with title queries: 'Media Plan', 'Sightly', 'RFP'. Paginate every query to the end. Dedup by file ID; cross-reference the dedup list.

Skip titles containing: Handover, Handoff, Moments, Moment Doc, From Client, Template, Amplifi Ratecard, or starting with "Copy of"/"ORIGINAL COPY". Also skip non-proposal files: delivery reports, tags/trafficking docs, ad specs, IOs, intake forms, trackers, battlecards, weekly reports, creative sheets, KOC docs, actualized/paused plans, and the standing exclusions above.

Versioning: per campaign keep FINAL if it exists, else the most recently modified base/draft; never add a draft when the campaign is already in the library under any title. Prefer client-facing versions over INTERNAL/ACTIVE variants of the same plan.

If more qualifying plans exist than can be processed in one run, process the highest-value finals first and write the remainder to `rate_library_monthly_worklist_YYYY-MM` (file_id, title, status) — and check last month's worklist for leftovers to pick up.

## STEP 3 — Extract rates from each new file

For large xlsx use download_file_content and parse the saved result in bash with openpyxl; for smaller/Google Sheets use read_file_content. Extract every rate line into this schema (17 columns, matching the master Sheet exactly):

source_file (title, no extension), agency (infer from "Sightly - AGENCY - BRAND" pattern), brand, category (standard list: Travel & Tourism, Alcohol & Beverages, Food & Beverage (CPG), QSR / Restaurants, Pharma / Healthcare, Lottery / Gaming, Entertainment & Media, Non-Profit / Education, Beauty & Personal Care, Luxury & Fashion, B2B Tech, B2B Industrial, B2B, Energy, Financial Services, Government, Home & Garden, Retail, Retail / Fashion, Retail / Grocery, Consumer Electronics, Telecommunications, Automotive, Sightly Tentpole Package), channel (YouTube, TikTok, Meta, CTV, Programmatic, Livestreaming, Reddit, Snapchat, Pinterest, Digital Audio, DOOH, Waze, Search), campaign_type (YouTube rows only: VRC - Efficient Reach, VRC - Target Frequency, VRC - Target Frequency Non-Skip, VRC - Non-Skippable Reach, VVC, Demand Gen, Performance Max, Masthead, YouTube Select, YouTube TV, Video Action, Historical - Standalone; blank otherwise), format (Skippable In-Stream, Non-Skippable In-Stream, Bumper :06s, Shorts, Multi-Format, In-Feed Video, Spark Ads, CTV/OTT, Streaming Audio, Pause Ads, Picture in Picture, etc.; VRC Efficient Reach with no specific unit = Multi-Format), objective (usually blank), rate_type (CPM, CPV, CPC, CPCV, dCPM), currency (USD/CAD/GBP/EUR), net_rate (only when plan shows net and billing side by side), billing_rate (always), flight, notes (flag "Suspect rate" outside normal ranges), format_original (leave blank), geo (default US), flight_year (4-digit int).

Conventions: standalone "TrueView Instream Non-Skippable/Skippable" lines = Historical - Standalone; "Video Reach Campaign (Non-Skippable)" = VRC - Non-Skippable Reach; "Objective - Video Views" = VVC; reservation products (Select lineups, Pause Ads, Shorts First Position, YouTube TV, PiP/NFL live) = YouTube Select or YouTube TV. One row per distinct channel+format+rate; separate rows per geo; skip $0 rates. Normal ranges: CPV $0.03–0.50, CPM $3–80, CPC $1–20.

## STEP 4 — Standardize

Channel: CTV/OTT, OTT → CTV; Programmatic Display/Video/OLV, OLV, Display → Programmatic; Spotify → Digital Audio; OLV/Livestreaming → Livestreaming. Trim strings; uppercase currency.

## STEP 5 — Build outputs locally

Append new rows to the downloaded library CSV → full library (for verification and summary). Regenerate summary: filter flight_year >= 2024 and numeric billing_rate; fill blank campaign_type with "" before groupby; agency_norm map (HMI→Horizon Media, UMWW NY→UMWW, luquire→Luquire, VML VMLY&R→VML, Dentsu UK→Dentsu, Publicis Canada→Publicis, Allen + Gerritsen→Allen & Gerritsen, GYK Antler Boston→GYK Antler). Four sections in one CSV with a leading `section` column and columns: section, channel, campaign_type, format, rate_type, agency_norm, geo, category, count, median, mean, min, max, currency (mode), rate_types (sorted unique joined by /): BY_TACTIC (channel, campaign_type, format, rate_type); BY_AGENCY_TACTIC (+agency_norm); BY_GEO_CHANNEL (geo, channel, rate_type); BY_CATEGORY_TACTIC (category, channel, campaign_type, format, rate_type).

## STEP 6 — Save to Drive and merge

1. Upload the delta as `rate_library_additions_YYYY-MM.csv` (create_file: parentId as above, contentMimeType text/csv, disableConversionToGoogleType true; title ends in .csv).
2. Upload `rate_library_YYYY-MM_run_status` (processed / merged / skipped-with-reasons / deferred / suspect rates / totals) and the worklist file.
3. **Merge into the master Sheet** — if Claude in Chrome browser tools are available: open the `rate_library_full_v3` Sheet, File > Import > Drive tab > select the additions CSV > Import location "Append to current sheet" > Import; then delete the one duplicated header row that lands at the seam (it is at old_last_row + 1); verify last row = old + new row count.
4. **Replace the summary Sheet contents**: split the regenerated summary CSV into ≤45 KB chunks `summ_partN.csv`, upload them, then in the `summary_by_tactic_and_agency` Sheet: import part 1 with "Replace current sheet", each further part with "Append to current sheet"; verify final row count; then trash the summ_part temp files (ONLY those — never trash library or history files).
5. If browser tools are NOT available (typical scheduled run), skip 3–4 and put a clear "MERGE PENDING: append rate_library_additions_YYYY-MM.csv to rate_library_full_v3 and refresh summary" line at the top of the run status file. The dedup logic in Step 1 tolerates an unmerged additions file.

## STEP 7 — Slack digest to #claude-strategy

Send ONE message to the #claude-strategy channel (channel ID: C0ASJ53F542) via the Slack connector (slack_send_message). This send is pre-authorized as part of this task.

**Formatting is mandatory — never post a wall of text.** Use Slack mrkdwn with this structure (emoji section headers, bold key numbers, one fact per bullet, bullets under ~90 chars):

📊 *Rate Library — {Month Year} Update*

*The headline*
• *+N rates* from *M new plans* → library now *X rows · Y plans*
• Master sheet merged ✅/⏳ · Summary refreshed ✅/⏳

🏢 *Who came in*
• 2–4 bullets on agency/brand/category mix, with emoji callouts (🥇 dominant agency, 💄/🍔/🎰/✈️ category flavor, counts like "10 of 17 plans")

📈 *Rate signals*
• 2–4 bullets chosen judiciously from the actual data: 🔺/🔻 tactics whose new rates run above/below library medians (quote both numbers), ➡️ steady benchmarks, 🆕 first-time tactics/formats, ⚠️ suspect rates flagged

🧭 *Channel mix (new rows)* — optional if mix is notable; unicode bar chart in a code block, e.g.:
`YouTube  ▓▓▓▓▓▓▓▓▓▓ 55`
`Other    ▓▓ 8`

📋 *Housekeeping*
• Deferred/worklist count and anything pending (e.g., 🇬🇧 UK batch, merge pending)

Slack mrkdwn notes: bold is *single asterisks*; bullets are literal "•" characters; code blocks with backticks for the bar chart; no headings syntax, no tables, no images. Keep the whole message scannable in ~15 seconds. If the Slack send fails, note it in the run status and final report rather than retrying more than once.

## STEP 8 — Report

Summarize: files found/processed, rows added, new source files, skips with reasons, suspect rates, deferred count, updated totals, whether merge + summary refresh completed in Drive, and whether the Slack digest was posted.
