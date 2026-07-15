# Sightly Strategy — Claude Plugins

This folder is a "shelf" that holds a Claude plugin so the Sightly team can install it. You don't need to open or change anything inside it. It just needs to sit on GitHub (a free website for storing folders). Once it's there, teammates point their Claude at it and get the plugin.

## What's on the shelf

- **culture-desk-rfp** — the Sightly Culture Desk plugin: the full RFP workflow (brief intake all the way through the deck and QA), plus the Sightly brand voice and design tools.

## How a teammate gets it

You give them one thing: the web address of this folder on GitHub. It looks like:

`podnosightly/sightly-strategy`

In their Claude, they open plugin settings, paste that address to add the shelf, and click **Install** next to **culture-desk-rfp**. Behind the scenes, their Claude just reads this folder off the internet and installs the plugin. That's the whole thing.

*(If a teammate uses the developer tool "Claude Code" instead of the regular app, the shortcut is to type `/plugin marketplace add podnosightly/sightly-strategy`, then `/plugin` to install. Same result.)*

## How you update it later (the payoff)

When a skill gets improved:

1. Replace the `plugins/culture-desk-rfp` folder here with the new version.
2. Change the version number in two small text files (`.claude-plugin/marketplace.json` and the plugin's own `.claude-plugin/plugin.json`) — just nudge the last number up.
3. Save it back to GitHub.

Teammates get the update by refreshing in their plugin settings. You never re-send files to anyone.

---

*Not sure what to do with any of this? Ask Claude to walk you through it one step at a time — that's what it's for.*
