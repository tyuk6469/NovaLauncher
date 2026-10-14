# NovaLauncher home screen design

The main screen should closely follow the supplied Zalith Launcher reference, while using NovaLauncher branding.

## Layout
- Dark theme, near-black page background, charcoal cards, white primary text, muted gray secondary text.
- Top app bar: **NovaLauncher** at the left; downloads and settings icons at the right.
- Wide layout: split the screen into two columns. The left side contains stacked action cards; the right side contains the active account and selected game version with a prominent launch button.
- Narrow layout: rearrange the same content vertically without hiding actions.

## Left action cards
1. Launcher information / version.
2. Control layout management.
3. Open launcher game folder.
4. Launch a standalone .jar file.
5. Share launcher logs.

Use a simple leading icon, readable label, rounded dark-gray card, generous touch target, and consistent spacing for every row.

## Right account and instance panel
- Center the local/Microsoft account avatar, username, and account type.
- Show the selected Minecraft version and loader below the account area, with a gear icon for instance settings.
- Place a large **Launch Game** button at the bottom of the panel.
- Preserve clear loading, disabled, and error states for launching.

## Interaction requirements
- Downloads icon opens download/instance management.
- Top settings icon opens global launcher settings.
- Instance gear opens settings for the selected installation only.
- All action cards must open real screens/actions; do not ship decorative controls that do nothing.
- Use safe-area insets and responsive sizing for Android phones and tablets.

## Branding and implementation notes
- This is a visual target, not a claim that the UI has already been implemented.
- Use the NovaLauncher name and its own app icon; do not present the modified app as the official Zalith Launcher.
- Keep upstream license and attribution notices required by the upstream GPL-3.0 license and its additional branding terms.
- Implement against the actual imported launcher source and existing navigation/state architecture rather than building a disconnected mock screen.
