# NovaLauncher product specification

## Goal
Create a full Android launcher for Minecraft: Java Edition, using ZalithLauncher2 as the technical base while keeping NovaLauncher branding and respecting the upstream GPL-3.0 license and branding conditions.

## Target platform and Minecraft versions
- Android phones, first target arm64.
- Support Minecraft Java Edition versions from **1.20.1 through the latest available release**, including 26.3 when it is officially available and the required runtime/loader components support it.
- Fetch version metadata dynamically from official Minecraft manifests rather than hard-coding a short list.
- Include stable releases by default; make snapshots/experiments an optional advanced setting.
- Never claim a version or loader combination works until its game files, libraries, Java runtime requirements, and launch path have been validated.

## Mod loaders
- **Fabric and Forge are the required loaders.**
- NeoForge and Quilt are out of scope for the initial product; do not spend implementation time on them unless the user asks later.
- Show only loader versions that actually exist for the selected Minecraft version.
- Install the correct loader profile and dependencies automatically, and allow separate game instances/profiles per Minecraft version and loader.
- Do not imply Fabric or Forge supports every Minecraft release; availability depends on upstream releases.

## In-launcher mod browser and manager
The user must be able to discover, download, install, update, disable, and remove mods without leaving NovaLauncher.

### Sources
- Modrinth integration is required.
- CurseForge integration should be added if its official API and licensing/authorization requirements permit it.
- Support direct local JAR import as a fallback for mods obtained elsewhere.
- Clearly identify the source of each download. Do not scrape websites or bypass provider access controls.

### User experience
- Search by name and browse categories, popular/recent projects, and relevant filters.
- Filter by Minecraft version, loader (Fabric or Forge), client/server/both environment, and project type.
- Show project description, author, version, dependencies, supported game versions/loaders, and source link before installation.
- Install into the currently selected instance/profile, not a global shared mods folder.
- Resolve required dependencies automatically where provider metadata allows it.
- Warn about optional dependencies, incompatible versions, duplicate/conflicting mods, and server-only mods.
- Provide progress, pause/cancel where supported, retry, update-all, and per-mod enable/disable/remove controls.
- Keep manually installed mods visible and untouched. Never silently replace or delete a user's files.
- Verify provider-supplied hashes when available and use safe temporary downloads followed by atomic installation.

## Mod compatibility promise
"Support all mods" cannot be guaranteed: mods may be abandoned, version-locked, loader-specific, incompatible with one another, require server-side installation, or depend on native libraries/features unavailable on Android. NovaLauncher must aim for broad catalogue coverage and accurate compatibility filtering, not claim universal compatibility. The game client must preserve normal Java/Fabric/Forge mod loading; launcher discovery/download support does not itself make an incompatible mod work.

## Performance and multiplayer requirements
- Multiplayer compatibility is a hard requirement, not an optional bonus.
- Prefer client-side optimizations that do not change server-visible gameplay, packet contents/order, or protocol behavior.
- Never require server-side plugins or mods for a general client performance feature unless it is clearly labeled as server-dependent.
- Do not move authoritative world ticks, entity/block updates, inventory state, or other shared game-state mutation onto arbitrary worker threads.
- Keep experimental engine/threading changes disabled by default and easy to roll back.
- Reject any optimization that causes disconnects, desynchronization, abnormal rubber-banding, world/save issues, or client-mod incompatibility, even if it improves FPS.
- Test on a private disposable server before recommending public-server use.
- Measure frame-time and 1% lows alongside average FPS; record network stability separately from local FPS.

Detailed procedure: [docs/MULTITHREADING_EXPERIMENT.md](docs/MULTITHREADING_EXPERIMENT.md).

## Optimization Pack requirements
- Start with a curated allowlist of client-side performance mods rather than downloading every mod.
- Resolve Minecraft version, loader, dependencies, environment-side and compatibility metadata before downloading.
- Prefer trusted official project APIs and verify supplied hashes.
- Keep mod downloads optional, visible as a feature, and easy to disable or remove.
- Never hide manually installed mods or mods managed by other tools.
- Keep pack-managed file metadata outside the mod JARs so the UI can filter them without modifying mods.
- Never silently install an incompatible set. Report skipped mods and errors.
- Never auto-install server-side mods into a client profile.

Implementation details and acceptance checks: [docs/hidden-optimization-mods.md](docs/hidden-optimization-mods.md).

## Engineering rules
- Keep the upstream source revision pinned for reproducible builds.
- Preserve upstream license and copyright notices.
- Use a distinct app name and artwork; never ship the upstream app under its original branding.
- Clearly show "Unofficial Modified Version" on the startup or main screen of any redistributed modified app, as required by upstream branding terms.
- Do not bundle files without checking their licenses and distribution permissions.
- Implement one feature per change where possible and build after each meaningful change.

## Milestones
- [x] Add a CI bootstrap build workflow.
- [x] Pin the upstream revision used by the bootstrap workflow.
- [x] Document the background Optimization Pack behavior and safety requirements.
- [ ] Confirm successful arm64 build and inspect the artifact.
- [ ] Import/fork the source into this repository so NovaLauncher changes are versioned here.
- [ ] Apply distinct branding and the required unofficial-modification notice.
- [ ] Audit existing ZalithLauncher2 version management, Fabric/Forge installation, and in-launcher mod-management code before reimplementing features.
- [ ] Build version/loader compatibility matrix from live official metadata.
- [ ] Implement in-launcher Modrinth search and install for selected instances.
- [ ] Add CurseForge support if official API access and terms permit.
- [ ] Add safe local JAR import and dependency/conflict handling.
- [ ] Implement the Optimization Pack, starting with client-side Fabric mods.
- [ ] Test version range, Fabric and Forge, mod installation, single-player, multiplayer, and existing instances on a real Android device.
