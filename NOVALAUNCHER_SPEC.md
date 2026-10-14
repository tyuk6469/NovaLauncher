# NovaLauncher product specification

## Goal
Create an Android launcher for Minecraft: Java Edition, using ZalithLauncher2 as the technical base while keeping NovaLauncher branding and respecting the upstream GPL-3.0 license and branding conditions.

## Target
- Android phones, first target arm64.
- Build and test debug APKs through GitHub Actions.
- Do not call an upstream bootstrap APK a NovaLauncher release.

## Requested capabilities
1. Minecraft Java version management and launch.
2. Mod loader support: Fabric, Forge, and NeoForge, limited to versions actually supported by the selected Minecraft version.
3. Modrinth browsing/download integration where API and project compatibility permit.
4. Performance-oriented settings, with clear descriptions and safe defaults.
5. An optional Optimization Pack that downloads a curated set of compatible performance mods in the background, hides only pack-managed mods from the normal mod list, and provides a separate status/disable/remove screen.
6. Mobile-friendly interface and useful install/build diagnostics.

## Optimization Pack requirements
- Start with Fabric and a curated allowlist rather than downloading every mod.
- Resolve Minecraft version, loader, dependencies, environment-side and compatibility metadata before downloading.
- Prefer trusted official project APIs and verify supplied hashes.
- Keep mod downloads optional, visible as a feature, and easy to disable or remove.
- Never hide manually installed mods or mods managed by other tools.
- Keep pack-managed file metadata outside the mod JARs so the UI can filter them without modifying mods.
- Never silently install an incompatible set. Report skipped mods and errors.

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
- [ ] Confirm a successful arm64 build and inspect the artifact.
- [ ] Import/fork the source into this repository so NovaLauncher changes are versioned here.
- [ ] Apply distinct branding and the required unofficial-modification notice.
- [ ] Add or verify loader and Modrinth workflows.
- [ ] Implement the Optimization Pack, starting with Fabric.
- [ ] Test on an Android device and publish a clearly labeled APK artifact.
