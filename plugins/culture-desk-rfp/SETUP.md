# Setup — what the pack can't carry

Installing the plugin gives you the skills. Two things live outside the plugin
and each person sets them up once:

## 1. Connectors

Several skills act on live tools. Authorize these in your Cowork/claude.ai
connector settings:

- **Monday.com** — required for the guide's "My open RFPs" panel and for
  rfp-tracker-logger / rfp-reconciliation-audit (RFP Tracker board).
- **Google Drive** — comparable-plan-finder, the rate library, and the
  proposal-drive-filer read/write here.
- **Gmail** — rfp-reconciliation-audit reads the rfp@ alias.

Until a connector is authorized, its skill will say so rather than run.

## 2. Culture Desk knowledge base

The skills reference the Culture Desk knowledge files (brand voice, hard rules,
budget minimums, QA framework, etc.). Load the Culture Desk project / knowledge
base in Cowork so those references resolve.

## 3. The guide artifact

`sightly-rfp-guide.html` is the interactive walkthrough. Open it in a browser,
or import it as a Cowork artifact. Its live panels (skill finder, "My open RFPs")
only run when it's open inside Cowork with the connectors above authorized.
