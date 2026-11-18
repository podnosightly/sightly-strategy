---
name: rfp-reconciliation-audit
description: >-
  Audit which Sightly RFPs a strategist actually submitted (via the
  rfp@sightly.com Gmail alias) but never logged in the Monday.com "RFP Tracker"
  board. Use when someone asks to "reconcile RFPs", "which RFPs aren't logged",
  "audit the RFP tracker", "cross-check RFP submissions", "find missing RFPs in
  Monday", "which of my RFPs didn't get logged", or wants to compare RFP emails
  against the RFP Tracker for a given strategist and time window. After finding
  gaps, it can interactively confirm each missing RFP's details with the
  strategist and log it to the board. Requires the Gmail and Monday.com connectors.
---

# RFP Reconciliation Audit (Gmail alias ↔ Monday RFP Tracker)

Goal: produce the list of RFPs a strategist **submitted** (sent a strategy deck
and/or media plan) that are **missing** from the Monday.com RFP Tracker.

## Before you start — clarify with the user
1. **Which strategist?** (default: the person asking). Get their exact name.
2. **Time window?** e.g. "last 30 days", "since <date>", or "all available".
3. **How is a submission matched in Monday?** Default: the **Strategist**
   (people) column = that person. Confirm.
State these back, then proceed. Ask before finalizing if anything is ambiguous.

## Key facts about this environment
- RFP requests arrive to the alias **rfp@sightly.com** from salespeople.
- Gmail label **"RFP Alias"** = id `Label_1482903974438226112` (verify via
  `list_labels`; label-ID search can be flaky, so prefer the `to:/cc:` query below).
- Monday board: **"RFP Tracker"**, board id **8288987600**, in the **Strategy**
  workspace. Always call `get_board_info` first to confirm columns haven't changed.
  Relevant columns:
  - Strategist (people): `person`
  - Submission Date (date): `date4`
  - Due Date (date): `date_1_mkmdere0`
  - Brand Name (text): `short_text_mkmwncax`
  - Agency (text): `text_mkmd8tj8`
  - Request Type (status): `color_mksv5r96` (RFP, New Biz Request, Request for
    Strategy, Request for Targeting, Insights/Intelligence, Request for Pricing)
  - Status (status): `status`
  - Groups: Proposal `topics`, Revisions `group_mkq8j4a6`, Submitted `new_group_mkmekpvn`

## Step 1 — Pull the RFP alias threads (Gmail)
- Query: `(to:rfp@sightly.com OR cc:rfp@sightly.com) after:YYYY/MM/DD` using the
  window's start (subtract a day; `after:` is exclusive).
- Page through with `pageSize: 50` + `pageToken`. Threads sort by most-recent
  message, so stop once a page's newest messages fall before the window start.
- Responses are large and get saved to a temp file. **Parse with `jq` in the
  shell** — find the saved file under the tool-results directory (e.g.
  `find /sessions/*/mnt/.claude/projects -name '*search_threads*'`). Dedupe
  threads across pages by `.id`.
- Use the default view (not `THREAD_VIEW_MINIMAL`) — minimal can drop
  sender/subject/date fields.

## Step 2 — Identify QUALIFYING threads (an actual submission)

> **CRITICAL — `search_threads` truncates long threads.** The search response
> only includes the *first few* messages of each thread. The strategist's actual
> deck/plan usually comes *late* in the thread, so it is often NOT in the search
> payload — relying on the search subset produces false negatives (real
> submissions look like "assigned but never delivered"). Do NOT judge delivery
> from `search_threads` snippets alone. Use BOTH signals below, then confirm with
> the full thread:
>
> 1. **Alias sweep** (Step 1) gives the universe of RFP threads + who was assigned
>    ("@<Strategist> will lead/handle" appears early, so it survives truncation).
> 2. **Sent-delivery sweep** — separately search the strategist's own sent mail:
>    `from:<strategist>@sightly.com after:YYYY/MM/DD (deck OR "media plan" OR
>    "strategy deck" OR "plan attached" OR "plan linked" OR "plans attached" OR
>    "plan is ready")`. Gmail matches on full message content, so the returned
>    **thread IDs** are a reliable set of "the strategist sent a delivery here",
>    even though the snippets are still truncated. Collect the thread subjects/IDs.
> 3. **Confirm each candidate** by fetching the FULL thread (`get_thread`,
>    FULL_CONTENT, parsed with `jq` from the saved file) and reading the
>    strategist's own messages end-to-end. Only then decide delivered vs intake.
>    Long threads (e.g. "2 RFPs" in one email) may contain multiple separate
>    deliveries on different dates — capture each.

A thread qualifies only if the strategist **delivered** a strategy and/or media
plan in-thread. For each thread, find messages where `sender` is the strategist AND:
- EXCLUDE calendar noise: subjects starting `Accepted:|Declined:|Invitation:|Canceled:|Synced`,
  or snippets containing "has accepted this invitation", "Join with Google Meet",
  "This event has been", "keeps the event up to date".
- EXCLUDE intake/coordination only: "I'm on it", "confirming we're good", "jumping
  in for", scheduling/logistics, "do we have a due date". These mean assigned, **not** submitted.
- INCLUDE real deliveries: language like "Deck linked/attached", "media plan
  attached", "Strategy Deck", "Strategy proposal", "plan is ready", "options attached".
- The pattern usually is: salesperson → alias, then a reply "@<Strategist> will
  lead/handle", then the strategist's deck/plan email.
Example `jq` skeleton (adjust the strategist regex):
```
jq -r '.threads[]
 | select(any(.messages[]; (.sender|test("STRATEGIST_EMAIL";"i"))
     and ((.subject//""|test("^(Accepted:|Declined:|Invitation:|Canceled:|Synced)"))|not)
     and ((.snippet//""|test("Join with Google Meet|has accepted this invitation|has declined this invitation"))|not)))
 | {subject: .messages[0].subject, dan:[.messages[]|select(.sender|test("STRATEGIST_EMAIL";"i"))|{d:.date[0:10],s:.snippet[0:140]}]}'
```
Then read the matched snippets and keep only those with a real deck/plan delivery.
Dedupe to distinct RFPs (a follow-up Q&A thread is the same RFP as its original).
Present borderline/excluded threads to the user for confirmation rather than dropping silently.

## Step 3 — Pull the strategist's Monday submissions
1. Resolve the strategist's Monday user id: `list_users_and_teams` with `name`.
2. `get_board_items_page` on board 8288987600, filter:
   `[{"columnId":"person","compareValue":["person-<USER_ID>"],"operator":"any_of"}]`
   - People filter values MUST use the `person-<id>` prefix.
   - Use `limit: 100` (500 exceeds Monday's request-complexity cap). Paginate via cursor.
   - Request only needed columns: `person, status, date4, date_1_mkmdere0,
     short_text_mkmwncax, text_mkmd8tj8, color_mksv5r96`.
3. Filter items to the same window using **Submission Date (`date4`)**.

## Step 4 — Cross-check and report
- Match Gmail-qualifying RFPs to Monday items by **brand + campaign name** (and
  roughly by date). Names won't match exactly (e.g. Gmail "Sightly Follow up –
  Rob / Hilton WC" ↔ Monday "Hilton UK World Cup 2026"), so match on the brand/campaign.
- For any Gmail submission with no Monday item, also do a **board-wide** check
  (`search` searchType ITEMS by brand) to distinguish "not logged at all" from
  "logged under a different strategist".
- Report: the missing RFPs with submission date, due date, and a one-line note on
  what was delivered; then the ones correctly logged; then any excluded/borderline
  threads and assumptions. Cite the Monday board URL and the Gmail subjects.

## Common gotchas
- Both a `from:<strategist>` search and the alias search may report the same
  inflated `resultCountEstimate` — ignore it; page until dates leave the window.
- Bulk backfills of the board are common — anything submitted *after* the last
  backfill date is the most likely to be missing.
- Don't count assigned-but-not-yet-delivered RFPs as submissions (surface them separately).

## Step 5 — Interactive logging of missing RFPs (confirm, then create)
After presenting the missing list, ASK the strategist whether they want to log
them now. If yes, handle them **one RFP at a time** in an interactive loop — do
not batch-create silently.

For each missing RFP:
1. **Draft the item from the email thread.** Read the source thread
   (Gmail `get_thread`, FULL_CONTENT) and propose values for:
   - Name (follow the board convention `Agency - Brand Campaign - Flight QY`;
     mirror existing items for that client)
   - Strategist (`person`), Brand Name (`short_text_mkmwncax`),
     Agency (`text_mkmd8tj8`)
   - Primary Sales Contact Name (`dropdown_mkpw9zq9`) = the salesperson who sent
     the RFP to the alias (the forwarder/requester). ALWAYS populate this. If the
     person's name isn't already a dropdown label, add it with
     `createLabelsIfMissing: true` — do NOT map them onto a similar-looking
     existing label (e.g. don't assume "Emily Kernin" = "Emily Korengold").
   - Submission Date (`date4`) = **the date the RFP email was received to the
     alias** (i.e. "date submitted by the seller"), NOT the date the strategist
     sent the deck back. Use the first alias message date of the thread.
   - Due Date (`date_1_mkmdere0`) = **the date the salesperson needs the
     submission back by** (from the request, e.g. "due EOD 7/1"). If the request
     gives no explicit deadline, ask the strategist; some teams set it to the date
     the work was actually sent back.
   - Request Type (`color_mksv5r96`, usually "RFP"), Status (`status`, usually "Done")
   - Self/Managed (`dropdown_mkmd326k`), Salesforce Link (`link_mkmdej9m`)
   - If present in the thread: Campaign Start/End, Budget, Platforms, KPI.
2. **Show the proposed values and ask the strategist to confirm or correct.**
   Present them clearly (a labeled list). Explicitly flag anything you inferred or
   couldn't find, and ask for those (e.g. missing Salesforce link, budget). Use a
   quick multiple-choice confirm where it helps, but let them free-type corrections.
3. **Wait for confirmation.** Apply any edits they give and re-show if the change
   was material. Do NOT create until they say it's correct.
4. **Create the item** with `create_item` (board 8288987600, group
   `new_group_mkmekpvn`). `columnValues` value formats:
   - people: `{"person":{"personsAndTeams":[{"id":<USER_ID>,"kind":"person"}]}}`
   - date: `{"date4":{"date":"YYYY-MM-DD"}}`
   - status: `{"color_mksv5r96":{"label":"RFP"}}`, `{"status":{"label":"Done"}}`
   - dropdown: `{"dropdown_mkmd326k":{"labels":["Managed Service"]}}`
   - Primary Sales Contact Name: `{"dropdown_mkpw9zq9":{"labels":["Andrew Carson"]}}`
     — pass `createLabelsIfMissing: true` on the create call if the name is new.
   - link: `{"link_mkmdej9m":{"url":"https://...","text":"Salesforce Opportunity"}}`
   - text: `{"short_text_mkmwncax":"Brand Name"}`
5. **Confirm back** with the new item name + URL, then move to the next RFP.

Loop guidance:
- If several campaigns were in one email (e.g. "2 RFPs"), create a separate item
  per campaign, confirming each.
- Let the strategist skip any RFP ("skip this one"), or say "log them all as-is"
  to accept your drafts without per-field review (still show the drafts first).
- For an RFP that was assigned but not actually delivered yet, offer to log it as
  Status "Working on it" with `date4` empty instead of "Done".

## Guardrails
- Creating items is fine. Do NOT change sharing/permissions, delete items, or send
  notifications/emails without explicit per-action approval from the strategist.
- Only create after explicit confirmation. Never invent a Salesforce link, budget,
  or dates — ask if unknown.

## Optional follow-up
Offer to schedule this audit to run monthly (e.g. 1st of the month) and report new
unlogged RFPs.
