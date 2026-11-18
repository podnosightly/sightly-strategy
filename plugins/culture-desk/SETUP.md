# Setup — what the pack can't carry

Installing the plugin gives you the skills. Two things live outside the plugin
and each person sets them up once:

## 1. Connectors

Several skills act on live tools. Authorize these in your Cowork/claude.ai
connector settings:

- **Monday.com** — required for the guide's "My open RFPs" panel and for
  rfp-tracker-logger / rfp-reconciliation-audit (RFP Tracker board).
- **Google Drive** — the rate recommender (comparable plans and the rate library) and
  the proposal-drive-filer read/write here.
- **Gmail** — rfp-reconciliation-audit reads the rfp@ alias.

Until a connector is authorized, its skill will say so rather than run.

## 2. Culture Desk knowledge base

The skills reference the Culture Desk V4 knowledge files (live 17 November 2026) by name. Load the
Culture Desk project / knowledge base in Cowork so those references resolve. Where a skill and the
knowledge base disagree, follow the knowledge base, with two deliberate exceptions:

- **The media plan builder's BILLING CPU and CPU columns.** `sightly-media-plan-builder` puts the
  pricing unit in BILLING CPU and the rate per unit in CPU, as in Sightly's live plans. A correction
  to the knowledge base's definitions in `06` and `13` is staged (17 November 2026); until it is
  applied, follow the skill for these two columns.
- **The full QC gates when a strategist asks for them.** By default the skills run the quick check
  in `13_When_Asked_to_Build.md` › The check before handing it over. When a strategist asks for the
  full gates, the skills run them.

| File | What the skills use it for |
|---|---|
| `01_Hard_Rules.md` | Every rule, numbered 1 to 26 |
| `02_Voice_and_Terminology.md` | Voice, copy rules, approved and prohibited terms, scale claims |
| `03_Sightly_Capabilities.md` | Products, partnerships, the Brand Mentality Agent and its limits |
| `04_Platform_Reference.md` | Platforms, formats, when to recommend |
| `05_Budget_Minimums_and_Feasibility.md` | Monthly minimums (one list), line-item floors, lead times |
| `06_Media_Planning_Principles.md` | Budget convention, rate hierarchy, reference CPMs, agency deals, KPI by format, added value |
| `07_Persona_Standards.md` | Persona names and descriptions; targeting on request |
| `08_Proof_Points_and_Battle_Cards.md` | Proof points and the do-not-use list |
| `09_Compliance.md` | Regulated categories |
| `10_Brand_Lift_and_Measurement.md` | Lift-study eligibility and minimums |
| `11_Reading_Brand_Mentality_Data.md` | Reading Brand Mentality data |
| `12_Format_Specs.md` | YouTube and Google, TikTok and Reddit specs |
| `13_When_Asked_to_Build.md` | Intake checklist, media plan columns, deck types and arcs, the quick check before handover |
| `14_Open_Items.md` | Unconfirmed figures; never quote them |

## 3. The guide artifact

`sightly-rfp-guide.html` is the interactive walkthrough. Open it in a browser,
or import it as a Cowork artifact. Its live panels (skill finder, "My open RFPs")
only run when it's open inside Cowork with the connectors above authorized.
