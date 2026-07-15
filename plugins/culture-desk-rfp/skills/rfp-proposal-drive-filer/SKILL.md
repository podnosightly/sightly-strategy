---
name: rfp-proposal-drive-filer
description: >-
  File a Sightly strategist's RFP proposal files (deck + media plan) into the
  correct Google Drive Sales Drive location — the Agency ▸ Brand ▸ Campaign ▸
  Proposal folder — copying them out of the strategist's personal My Drive when
  needed. Use when someone asks to "file my proposals to the drive", "save these
  decks to the sales drive", "make sure my proposals are in the right folder",
  "put this proposal in its Proposal folder", "reconcile my drive proposals", or
  after an RFP audit when the decks/plans need to be filed. Non-destructive
  (copies by default). Requires the Google Drive connector. Pairs with
  rfp-reconciliation-audit (which finds the submissions).
---

# RFP Proposal → Sales Drive Filer

Goal: for each submitted proposal, make sure its **final deck and media plan**
live in the correct **Agency ▸ Brand ▸ Campaign ▸ Proposal** folder in the Sales
Drive, copying out of the strategist's personal drive when they're loose there.

## Before you start — clarify with the user
1. **Which proposals?** (a list, or the output of an rfp-reconciliation-audit run).
2. **Copy or move?** Default **copy** (non-destructive; leaves the My Drive
   original). Only move if they explicitly ask.
3. **Which versions?** Default: the clean **Google-native final** (Slides deck /
   Sheets plan). Skip `.pptx`/`.xlsx` working drafts and dupes unless told.
4. **Create missing folders?** Default yes — build the Agency▸Brand▸Campaign▸
   Proposal chain as needed.

## Key facts about this environment
- The strategist's personal **My Drive** root = `0AFRN_-IJLSxGUk9PVA` (for Dan
  Podnos). A file whose parent chain leads here is "on personal drive" and needs
  copying into the Sales Drive. Confirm the current user's My Drive id if different.
- Sales Drive hierarchy: **Agency ▸ Brand ▸ Campaign ▸ {Prep, Proposal}**. Final
  proposals go in the campaign's **Proposal** subfolder (briefs/working docs go in **Prep**).
- Agencies root (where agency folders live) = `11sDjjhwm3EzCm2iXNwVa-4s5MTokvI_u`.
- Proposal files are titled like `Sightly - <Brand> - <Strategy|Media Plan|...>`.
- Self-service proposals are often **deck-only** (client runs the buy) — that
  still counts; file the deck.

## Step 1 — Find each proposal's files
For each proposal, `search_files` by brand keyword, e.g.
`title contains 'Burger King' or title contains 'Montblanc'`.
- Prefer 2026 files created/modified near the submission date.
- Prefer Google-native (Slides `...presentation`, Sheets `...spreadsheet`) as the
  canonical final; treat `.pptx`/`.xlsx` and "v2/v3"/"Copy of" as working drafts.
- Capture: title, fileId, mimeType, owner, and current `parentId`.

## Step 2 — Determine current location
`get_file_metadata` on the file's `parentId`, and walk up parents as needed:
- Parent (or ancestor) = My Drive root → **on personal drive** (needs copying).
- Parent titled "Proposal" whose ancestry matches the campaign → **already filed** (skip).
- Parent titled "Prep" or the brand/campaign root → **misfiled** (copy into the Proposal folder).
- Parent under a *different* campaign's Proposal folder → **misfiled** (copy to the right one; flag the stray).

## Step 3 — Find or create the target Proposal folder
1. Search folders: `mimeType = 'application/vnd.google-apps.folder' and title contains '<Brand>'`
   and `... title contains 'Proposal'`; use `get_file_metadata` on candidates'
   parents to confirm the Agency▸Brand▸Campaign path.
2. **If the agency/brand home is ambiguous** (multiple candidates, legacy
   2017–2023 folders, etc.), STOP and ask the user which folder is correct — do
   NOT guess. Getting the agency wrong scatters files.
3. **If folders are missing**, create the chain with `create_file`
   (`contentMimeType: 'application/vnd.google-apps.folder'`, `title`, `parentId`),
   one level at a time, capturing each new id for the next level. Name the
   **Campaign** folder to match the Monday RFP Tracker item (e.g. "Soho Sneaker",
   "Self Service 2026", "FIFA World Cup 2026"); mirror existing sibling campaigns
   for that brand.

## Step 4 — Copy the files in
`copy_file(fileId, parentId=<Proposal folder id>, title=<original title>)`.
- ALWAYS pass `title` = the original file title, or the copy is named "Copy of …".
- Copy is non-destructive; the My Drive original stays. Note leftover working
  drafts/dupes on My Drive but don't touch them unless asked.

## Step 5 — Report
List, per proposal: what was already correctly filed, what you copied and into
which Proposal folder (with links), any campaigns whose folders you created, and
anything you held for the user (ambiguous home, missing file, misfiled stray to
delete). Provide folder URLs so the strategist can verify.

## Guardrails
- Copy, don't move/delete, unless explicitly told. Never overwrite.
- Don't guess an ambiguous agency/brand home — ask.
- Don't invent a "final" version — if only working drafts exist, ask which is final.
