# NovaLauncher

NovaLauncher is a personal Android launcher project for Minecraft: Java Edition, based on a pinned ZalithLauncher2 source revision and developed with a distinct identity.

## Current status

The repository currently builds an **arm64 debug bootstrap APK** from the pinned upstream source. NovaLauncher applies a startup notice identifying it as an unofficial modified version. The current app is still the upstream launcher with a small branding patch; the redesigned Nova home screen and Nova-specific optimization features are not implemented yet.

A source-level audit found that the pinned upstream already contains:
- Fabric and Forge loader installation code.
- Modrinth and CurseForge provider/search code.
- An in-launcher mod search screen and installed-mod manager.
- Mod metadata readers and modpack import/export paths.

NovaLauncher should reuse and test these existing flows instead of reimplementing them blindly. See [docs/upstream-feature-audit.md](docs/upstream-feature-audit.md).

## Build

A push to `main` starts the **Bootstrap Android APK** workflow automatically. You can also open the [Actions tab](https://github.com/tyuk6469/NovaLauncher/actions), select the workflow, and press **Run workflow**.

When the run succeeds:
1. Open the completed workflow run.
2. Scroll to **Artifacts**.
3. Download `NovaLauncher-arm64-debug-bootstrap`.

The APK is a debug build. A successful CI build confirms compilation and artifact upload, not installation or runtime compatibility on a physical phone.

## Upstream source and license

Source: https://github.com/ZalithLauncher/ZalithLauncher2  
Pinned revision: `7d4f31af01d8a0f6b86e6cc59ff846c24d7bb579`  
Local path: `upstream/ZalithLauncher2`

The upstream project is licensed under GPL-3.0 and includes additional branding requirements for modified redistributions. Preserve copyright/license notices, use a distinct name, and clearly label modified builds as unofficial.

## Development priorities

1. Keep the pinned arm64 debug build reproducible.
2. Trace and test the existing home screen, version management, Fabric/Forge installation, and mod management flows.
3. Implement the Nova home screen and branding in the actual app.
4. Reuse existing Modrinth search/install and installed-mod management where they meet the specification; fill only verified gaps.
5. Verify CurseForge API authorization and terms before depending on it.
6. Add the optional Optimization Pack with compatibility checks, clear ownership, and rollback-safe downloads.
7. Test installation, launch, existing instances, and multiplayer on a real Android device.

See [NOVALAUNCHER_SPEC.md](NOVALAUNCHER_SPEC.md), [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md), and [docs/AI_COLLABORATION.md](docs/AI_COLLABORATION.md). Features are marked complete only after implementation and verification.
