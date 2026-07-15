---
name: rfp-tracker-logger
description: >-
  Create a correctly-structured item in the Sightly Monday.com "RFP Tracker"
  board from an RFP email thread (or details the user provides). Use when
  someone asks to "log this RFP to Monday", "add this to the RFP Tracker",
  "create an RFP item", "record this RFP", or wants an emailed RFP entered on the
  board. Extracts brand, agency, dates, Salesforce link, and Managed/Self service
  and writes them to the right columns and group. Requires the Monday.com
  connector (and Gmail if pulling details from an email thread).
---

# RFP Tracker Logger (email thread → Monday item)

Goal: add a clean, correctly-structured item to the RFP Tracker so it matches
how existing items are logged.

## Board reference (verify with `get_board_info` first)
- Board: **"RFP Tracker"**, id **8288987600**, Strategy workspace.
- Submitted items live in the **"Submitted"** group: `new_group_mkmekpvn`
  (other groups: Proposal `topics`, Revisions `group_mkq8j4a6`).
- Column IDs:
  - Strategist (people): `person`
  - Brand Name (text): `short_text_mkmwncax`
  - Agency (text): `text_mkmd8tj8`
  - Submission Date (date): `date4`
  - Due Date (date): `date_1_mkmdere0`
  - Request Type (status): `color_mksv5r96` — labels: RFP, New Biz Request,
    Request for Strategy, Request for Targeting, Insights/Intelligence, Request for Pricing
  - Status (status): `status` — Working on it, Done, Stuck - More Information
    Needed, Revision, Not Started, Sent To Sales
  - Self or Managed Service (dropdown): `dropdown_mkmd326k` — "Self Service" / "Managed Service"
  - Salesforce Link (link): `link_mkmdej9m`
  - Campaign Start (date): `date_1_mkmd1cj9`; Campaign End (date): `date_1_mkmdnkjc`
  - Campaign Budget (numbers): `numeric_mkpv842e`; KPI (text): `text_mkmdvqa0`
  - Platforms (dropdown): `dropdown_mkmdhc59` — YouTube, Meta, TikTok, CTV, etc.

## Step 1 — Gather the fields
If given an email thread, read it (Gmail `get_thread`, FULL_CONTENT) and extract:
brand, agency, due date, the date the strategy/plan was actually sent
(= Submission Date), Salesforce opportunity link, self vs managed service, and any
campaign flight dates / budget / platforms / KPI mentioned. If details are
missing, ask the user rather than guessing.

## Step 2 — Confirm before writing
Show the user the item name and the fields you'll set, and confirm. Use a name
consistent with existing items — the board's Salesforce convention is
`Agency - Brand Campaign Name - Flight QY` (e.g. "Horizon - GoGo Squeez -
Everyday Campaign - Q1 25'"); shorter market-based names like "CSH Houston 2026"
are also used. Match sibling items for the same client.

## Step 3 — Create the item
Use `create_item` on board 8288987600, `groupId: new_group_mkmekpvn`.
`columnValues` is a JSON string. Formats that matter:
- people: `{"person":{"personsAndTeams":[{"id":<USER_ID>,"kind":"person"}]}}`
  (resolve `<USER_ID>` via `list_users_and_teams` name search)
- date: `{"date4":{"date":"2026-06-15"}}`
- status: `{"color_mksv5r96":{"label":"RFP"}}`, `{"status":{"label":"Done"}}`
- dropdown: `{"dropdown_mkmd326k":{"labels":["Managed Service"]}}`
- link: `{"link_mkmdej9m":{"url":"https://...","text":"Salesforce Opportunity"}}`
- text: `{"short_text_mkmwncax":"CommonSpirit Health"}`

Example (a submitted, managed-service RFP):
```
name: "CSH Tennessee Brand Transition 2026"
columnValues: {
  "person":{"personsAndTeams":[{"id":74572400,"kind":"person"}]},
  "short_text_mkmwncax":"CommonSpirit Health",
  "color_mksv5r96":{"label":"RFP"},
  "status":{"label":"Done"},
  "date4":{"date":"2026-06-15"},
  "date_1_mkmdere0":{"date":"2026-06-15"},
  "dropdown_mkmd326k":{"labels":["Managed Service"]},
  "link_mkmdej9m":{"url":"https://sightly.lightning.force.com/lightning/r/Opportunity/XXX/view","text":"Salesforce Opportunity"}
}
```
For an in-progress (not yet delivered) RFP, set `status` to "Working on it" and
leave `date4` empty.

## Step 4 — Confirm back
Report the created item name + URL. If several RFPs were in one email (e.g. "2
RFPs"), create a separate item per campaign. Offer to fill remaining detail
fields (budget, platforms, flight dates, KPI) if the user wants them complete.

## Guardrails
- Creating items is fine; do NOT change sharing/permissions, delete items, or
  send notifications/emails without explicit per-action approval.
- Verify column IDs with `get_board_info` before writing in case the board changed.
