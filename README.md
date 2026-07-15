# Sightly Strategy — Plugin Marketplace

This is the Sightly Strategy Team's plugin marketplace. It currently offers one plugin:

- **culture-desk-rfp** — the full Culture Desk RFP workflow (brief intake → comparable plan → strategy → personas → platform roles → rates → media plan → deck build → brand check → QA), plus the codified Sightly brand voice and visual design system.

## For teammates: how to install

1. In Claude, add this marketplace once (ask whoever shared this for the exact `owner/repo` name):

   ```
   /plugin marketplace add <owner>/<repo-name>
   ```

2. Open the plugin menu and install **culture-desk-rfp**:

   ```
   /plugin
   ```

3. Later, to get the newest version after an update:

   ```
   /plugin marketplace update
   ```

## For the maintainer: how to publish an update

1. Replace the plugin folder at `plugins/culture-desk-rfp/` with the new version.
2. Bump the `version` for `culture-desk-rfp` in `.claude-plugin/marketplace.json` (and in the plugin's own `.claude-plugin/plugin.json`).
3. Save the changes to the repo. Teammates pick it up with `/plugin marketplace update`.

That's the whole point of a marketplace: you update it in one place, and everyone updates from it — no re-sending files.
