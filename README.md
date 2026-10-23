# NovaLauncher

NovaLauncher is a personal Android launcher project for Minecraft: Java Edition, built from a pinned upstream source snapshot.

## Current status

The repository now tracks the upstream ZalithLauncher2 source as a Git submodule at `upstream/ZalithLauncher2`. The submodule is pinned to a specific commit so builds are reproducible and upstream updates are deliberate rather than automatic.

The current CI workflow builds an **arm64 debug bootstrap APK** from that pinned source and sets the app label and build metadata to NovaLauncher. This is only an initial branded build: the main-screen unofficial-modification notice, custom home screen, and planned NovaLauncher features are not implemented yet.

## Build

A push to `main` starts the **Bootstrap Android APK** workflow automatically. You can also open the **Actions** tab, select the workflow, and press **Run workflow**.

When the run succeeds:
1. Open the completed workflow run.
2. Scroll to **Artifacts**.
3. Download `NovaLauncher-arm64-debug-bootstrap`.

The APK is a debug build and may install alongside other builds because the upstream project adds a debug application ID suffix.

## Upstream source and license

Source: https://github.com/ZalithLauncher/ZalithLauncher2  
Pinned revision: `7d4f31af01d8a0f6b86e6cc59ff846c24d7bb579`  
Local path: `upstream/ZalithLauncher2`

The upstream project is licensed under GPL-3.0 and includes additional branding requirements for modified redistributions. Before distributing a modified app, we must use a distinct name, clearly label it as an unofficial modified version on the startup or main screen, and preserve copyright notices.

## Development priorities

1. Confirm the NovaLauncher-labelled arm64 debug bootstrap builds reliably on CI.
2. Inspect the launcher architecture and identify safe integration points.
3. Implement NovaLauncher branding and the home screen.
4. Add loader installation and instance management improvements.
5. Add Modrinth search/install/update with compatibility checks.
6. Implement the optional optimization pack with clear ownership, dependency checks, and rollback-safe downloads.
7. Test installation, launch, and existing instances on real Android devices.

See [NOVALAUNCHER_SPEC.md](NOVALAUNCHER_SPEC.md) and [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md). Features will only be marked complete after implementation and verification.
