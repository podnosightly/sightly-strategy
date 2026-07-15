---
name: "sightly-rate-library-monthly-update"
description: "Monthly refresh of Sightly rate library — finds new media plans in Drive, extracts rates, updates CSVs, saves back to Drive. Run on the 1st of each month."
---

You are updating the Sightly Rate Library — a CSV of CPM/CPV/CPC rates extracted from client media plans stored in Google Drive. Your job is to find new media plan files created or modified in the past 35 days that are not already in the library, extract their rates, append them, re-run standardization, regenerate the summary, and save both files back to Google Drive.

## STEP 1 — Load the current rate library from Drive

Search Google Drive for a file titled "rate_library_full_v3" in the "Rate Cards and Benchmarks" folder (folder ID: 19XFLRFr-CIWDMMp-0ZuA1id-VEjEZHBB). Download its content and parse as CSV. Collect all unique values in the source_file column — this is your dedup list. Do not re-process any file whose title already appears in this list. Also load "summary_by_tactic_and_agency" from the same folder.

## STEP 2 — Search Drive for new media plan files

Search for spreadsheet files modified in the last 35 days using multiple title queries: title contains 'Media Plan', title contains 'Sightly', title contains 'RFP'. Use mimeType filters for both Google Sheets and xlsx. Deduplicate results by file ID. Cross-reference against the dedup list and skip already-processed files.

Skip any file where the title contains: Handover, Handoff, Moments, Moment Doc, From Client, Template, Amplifi Ratecard, or starts with "Copy of". Skip files that appear to be internal rate cards rather than client proposals.

Versioning rule: if multiple files exist for the same client/campaign, keep FINAL if it exists, otherwise keep the most recently modified draft. Do not add both a draft and a final for the same campaign.

## STEP 3 — Extract rates from each new file

For each qualifying new file, read its content and extract every rate line item into this schema:

- source_file: file title (no extension)
- agency: media agency name — infer from filename pattern "Sightly - AGENCY - BRAND" if not on plan
- brand: advertiser/brand name
- category: advertiser vertical — use standard list: Travel & Tourism, Alcohol & Beverages, Food & Beverage (CPG), QSR / Restaurants, Pharma / Healthcare, Lottery / Gaming, Entertainment & Media, Non-Profit / Education, Beauty & Personal Care, Luxury & Fashion, B2B Tech, B2B Industrial, B2B, Energy, Financial Services, Government, Home & Garden, Retail, Retail / Fashion, Retail / Grocery, Consumer Electronics, Telecommunications, Automotive, Sightly Tentpole Package
- channel: YouTube, TikTok, Meta, CTV, Programmatic, Livestreaming, Reddit, Snapchat, Pinterest, Digital Audio, DOOH, Waze, Search
- campaign_type: YouTube rows only — VRC - Efficient Reach, VRC - Target Frequency, VRC - Target Frequency Non-Skip, VRC - Non-Skippable Reach, VVC, Demand Gen, Performance Max, Masthead, YouTube Select, YouTube TV, Video Action, Historical - Standalone. Blank for all non-YouTube rows.
- format: the ad unit — Skippable In-Stream, Non-Skippable In-Stream, Bumper :06s, Shorts, Multi-Format, In-Feed Video, Spark Ads, CTV/OTT, Streaming Audio, etc. For VRC Efficient Reach with no specific ad unit, use Multi-Format.
- objective: usually blank
- rate_type: CPM, CPV, CPC, CPCV, or dCPM
- currency: USD, CAD, GBP, or EUR
- net_rate: only fill for GBP/EUR plans that explicitly show both net and billing rates side by side
- billing_rate: the rate shown on the plan — primary rate column, fill for all plans
- flight: date range as shown on the plan
- notes: flag unusual rates as "Suspect rate" if outside normal range
- geo: US, Canada, UK, Germany, etc. Infer from filename or plan. Default to US for US brands.
- flight_year: 4-digit integer year from flight dates

Rules: each distinct channel + format + rate = one row. If a plan shows rates by geography, create separate rows. Skip $0 rates. If billing_rate is blank but net_rate has a value, move net_rate to billing_rate and clear net_rate (unless the plan explicitly shows both). Normal ranges: CPV $0.03-$0.50, CPM $3-$80, CPC $1-$20.

## STEP 4 — Standardize new rows

Channel: CTV/OTT and OTT → CTV; Programmatic Display/Video/OLV and OLV → Programmatic; Spotify → Digital Audio; Display standalone → Programmatic; OLV/Livestreaming → Livestreaming. Trim all string fields. Normalize currency to uppercase.

## STEP 5 — Append and regenerate summary

Append new rows to the rate library. Regenerate summary_by_tactic_and_agency.csv with four sections. Filter to flight_year >= 2024. Use billing_rate as rate value. Fill blank campaign_type with empty string before groupby so non-YouTube rows are included. Compute: count, median, mean, min, max, currency (most common), rate_types (sorted unique joined by slash).

Section BY_TACTIC: group by channel, campaign_type, format, rate_type
Section BY_AGENCY_TACTIC: group by agency_norm, channel, campaign_type, format, rate_type
Section BY_GEO_CHANNEL: group by geo, channel, rate_type
Section BY_CATEGORY_TACTIC: group by category, channel, campaign_type, format, rate_type

Agency normalization: HMI → Horizon Media, UMWW NY → UMWW, luquire → Luquire, VML VMLY&R → VML, Dentsu UK → Dentsu, Publicis Canada → Publicis, Allen + Gerritsen → Allen & Gerritsen, GYK Antler Boston → GYK Antler.

## STEP 6 — Save to Google Drive

Upload both updated CSVs to the Rate Cards and Benchmarks folder (ID: 19XFLRFr-CIWDMMp-0ZuA1id-VEjEZHBB). Search for existing files by title first and overwrite them. Use create_file with disableConversionToGoogleType true and contentMimeType text/csv. Titles: rate_library_full_v3 and summary_by_tactic_and_agency.

## STEP 7 — Report

Summarize: how many new files found and processed, rows added, list of new source files, any files skipped and why, any suspect rates flagged, updated library totals (total rows, total source files).
