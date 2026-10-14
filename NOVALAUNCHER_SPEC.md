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
5. Mobile-friendly interface and useful install/build diagnostics.

## Engineering rules
- Keep the upstream source revision pinned for reproducible builds.
- Preserve upstream license and copyright notices.
- Use a distinct app name and artwork; never ship the upstream app under its original branding.
- Clearly show "Unofficial Modified Version" on the startup or main screen of any redistributed modified app, as required by upstream branding terms.
- Do not bundle mods or downloads without checking their licenses and distribution permissions.
- Implement one feature per change where possible and build after each meaningful change.

## Milestones
- [x] Add a CI bootstrap build workflow.
- [x] Pin the upstream revision used by the bootstrap workflow.
- [ ] Confirm a successful arm64 build and inspect the artifact.
- [ ] Import/fork the source into this repository so NovaLauncher changes are versioned here.
- [ ] Apply distinct branding and the required unofficial-modification notice.
- [ ] Add or verify loader and Modrinth workflows.
- [ ] Test on an Android device and publish a clearly labeled APK artifact.
