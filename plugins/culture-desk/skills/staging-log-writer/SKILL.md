---
name: "staging-log-writer"
description: "Writes a Culture Desk staging entry straight into the Staging Log folder on Google Drive in one step. It drafts the entry in the V4 seven-field template, names it entry_[YYYY-MM-DD]_[short-title].md with no number (numbers are assigned at review), writes it, and verifies it landed. Use whenever a knowledge base gap, error or rule change surfaces (\"add this to the staging log\", \"add this to the KB\", \"that's wrong, update it\", \"make a note for the knowledge base\", \"log that\"), and offer it proactively whenever something in the knowledge base turns out to be wrong, outdated or missing. Also handles backlogged entries in batch."
---

# Staging Log Writer

Write a Culture Desk staging entry directly into the Drive folder the team reviews. One step, no download, no manual filing.

**Why this exists.** The documented protocol asked the strategist to stop mid-deliverable, generate a file, download it, and drop it in Drive. Four actions against a deadline. Across 90 days, 53 knowledge base corrections were identified in conversation and the overwhelming majority were never filed. Corrections that persisted were the ones a tool wrote directly. This skill removes the human filing step.

**How this relates to the V4 instructions.** The Culture Desk instructions ("When the knowledge base is wrong") have Claude produce the entry as a downloadable file that the strategist saves to the Staging Log folder. This skill uses the same file name, the same seven-field template and the same unnumbered rule. The one difference is that it writes the file to the folder itself, for the reason above.

---

## The destination

**Folder:** `Staging Log - Culture Desk Updates`
**Folder ID:** `1jJB8KXgyyyj8XC6g6y_LTumV8NhtQJPc`
**Path:** Strategy Team → Culture Desk → Staging Log - Culture Desk Updates

Write with the Google Drive connector's `create_file`, passing:

- `parentId`: `1jJB8KXgyyyj8XC6g6y_LTumV8NhtQJPc`
- `title`: `entry_[YYYY-MM-DD]_[short-title].md`
- `textContent`: the entry
- `contentMimeType`: `text/markdown`
- `disableConversionToGoogleType`: `true`

**That last flag matters.** Without it Drive silently converts the file to a Google Doc. Two entries in the folder are already Google Docs rather than `.md`, which breaks the convention the review process expects.

---

## Step 1: name the file and check the folder

**Entries are unnumbered.** Numbers are assigned at review. Never add a number, and never use a placeholder such as `NEXT`.

Name the file `entry_[YYYY-MM-DD]_[short-title].md`, using today's date. Slug rule for the short title: lowercase, hyphens between words, 3 to 6 words, and it describes the change rather than the client. Write `entry_2026-11-17_tiktok-daily-minimum-increase.md`, and avoid `entry_2026-11-17_popeyes.md`.

Before writing, list the folder once:

```
search_files: parentId = '1jJB8KXgyyyj8XC6g6y_LTumV8NhtQJPc'
```

If a file with the same name already exists, append `-2` to the short title, then `-3` and so on: `entry_2026-11-17_tiktok-daily-minimum-increase-2.md`. If the existing file is about the same correction, tell the strategist in one line and ask whether to file a second entry.

The folder also holds older numbered entries. Leave them as they are; do not rename or renumber anyone's entries.

---

## Step 2: draft the entry and confirm before writing

Use the template exactly. It is the template in the Culture Desk instructions, and the review process reads entries in a batch and depends on the shape.

```
Title: [short title of the change]
Submitted by: [strategist name]
Date: [YYYY-MM-DD]
What is wrong or missing, and what it should say: [Plain language. Name the platform, the term, the number, the rule. Quote the correcting instruction verbatim where one exists, because the reviewer needs to see what was actually said.]
File(s) affected: [V4 file name and section, for example `05_Budget_Minimums_and_Feasibility.md` (Sightly's recommended monthly minimums)]
Source: [Where this came from: platform announcement, client conversation, rep confirmation, an error caught mid-build, a colleague's correction. Name the person and date if a person said it.]
Not verified: [Anything in the entry that has not been confirmed against a published or dated source. Write "Nothing" if everything is confirmed.]
```

**File(s) affected uses the V4 file names:** `01_Hard_Rules.md`, `02_Voice_and_Terminology.md`, `03_Sightly_Capabilities.md`, `04_Platform_Reference.md`, `05_Budget_Minimums_and_Feasibility.md`, `06_Media_Planning_Principles.md`, `07_Persona_Standards.md`, `08_Proof_Points_and_Battle_Cards.md`, `09_Compliance.md`, `10_Brand_Lift_and_Measurement.md`, `11_Reading_Brand_Mentality_Data.md`, `12_Format_Specs.md`, `13_When_Asked_to_Build.md`, `14_Open_Items.md`, or the Culture Desk project instructions. The numbers 04, 06, 12 and 13 belonged to different files in the older knowledge base, so check the full name before citing one.

**Present the draft and wait for confirmation before writing.** One round trip. Do not write silently, and do not ask more than once.

Three things that make an entry usable at review, learned from ones that weren't:

- **Quote the correction.** "Dan said the plan always sums to the budget" is weaker than the verbatim line. Reviewers need to judge the instruction, not your summary of it.
- **Name what it contradicts.** If the KB currently says something different, say so and cite the file and section. An entry that doesn't name the conflict reads as an opinion.
- **Mark unverified facts as unverified.** If a platform term came from a rep in conversation and hasn't been confirmed against published documentation, write that into the Not verified field. Do not launder a hallway conversation into a fact.

---

## Step 3: write it, then verify

After `create_file`, read the file back with `read_file_content` on the returned ID. Confirm it's there and the content is intact.

Report to the strategist in two lines: the file name and title, and the Drive link. Nothing more.

**If the write fails**, say so plainly and offer the fallback: save to the outputs folder so nothing is lost, then retry. If the strategist doesn't have write access to the folder, give them the entry as a downloadable file under the same name and ask them to save it to the folder, which is the flow in the Culture Desk instructions. Never report success you haven't verified.

---

## Batch mode

When several entries need filing at once — a backlog sweep, or a session that surfaced multiple gaps — do not write them one at a time with a confirmation each.

1. List the folder once and check every planned file name for a same-day duplicate.
2. Present all drafts together as a list with one-line summaries: title, affected file and file name.
3. Get one confirmation for the batch, or let the strategist strike individual items.
4. Write them all, then verify all, then report a single table of what landed.

If the strategist wants to file a large backlog, ask whether to file everything at once or the most pressing items first. Volume at review is its own cost.

---

## When to offer this without being asked

The Culture Desk instructions say to flag knowledge base problems proactively. This skill is how that flag becomes durable. Offer it when:

- A figure, rate, minimum, platform spec or terminology rule in the knowledge base turns out to be wrong or stale.
- A colleague or platform rep supplies a fact the knowledge base doesn't carry.
- The strategist overrides a documented rule in practice. **This is the highest-value case and the easiest to miss** — the rule stays wrong in writing while everyone works the new way, which is exactly how a documented rule and actual practice drift apart.
- A proof point is found to be unusable, confidential, misattributed, or below-average.
- A gap is hit repeatedly across briefs, such as a vertical with no case study or a product with no published price.
- The strategist says any of: add this to the staging log, add this to the KB, that's wrong, make a note for the knowledge base, we should change how you handle X going forward, log that.

Offer in one line. Draft on a yes.

If "how you handle X" is about how a skill or plugin behaves, it is not a staging entry. See below.

---

## What this skill does not do

- It does not edit knowledge base files. Entries are proposals; they are applied, and numbered, at review.
- It does not number, rename or modify entries already in the folder.
- It does not invent the substance of an entry. If the correction isn't clear enough to write down, ask what changed rather than guessing.
- It does not file conversation-specific working information. A rate confirmed for one deal is not a staging entry; a discovery that the recorded minimum is wrong is.
- It does not file fixes to a skill's or plugin's behavior. Those go to the skill's owner, who edits the skill directly. For Dan's personal skills and the culture-desk-rfp plugin, that is Dan. Staging entries cover the knowledge base files and the project instructions.

---

## In-session behavior

A correction applies immediately for the rest of the session so work continues on accurate information. It is not permanent until the entry is written, reviewed and applied. Say both things once, then move on.
