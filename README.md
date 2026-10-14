# NovaLauncher

NovaLauncher is a personal Android launcher project for Minecraft: Java Edition.

## Current status

The repository currently contains a **bootstrap CI workflow**, not a finished launcher fork. The workflow checks out a pinned ZalithLauncher2 revision, builds an arm64 debug APK, and uploads it as a GitHub Actions artifact. It intentionally does not rename the upstream app or claim to be a NovaLauncher release.

## Build

A push to `main` starts the **Bootstrap Android APK** workflow automatically. You can also open the **Actions** tab, select the workflow, and press **Run workflow**.

When the run succeeds:
1. Open the completed workflow run.
2. Scroll to **Artifacts**.
3. Download `upstream-bootstrap-arm64-debug`.

The APK is a debug build and may install alongside other builds because the upstream project adds a debug application ID suffix.

## Upstream source and license

Source: https://github.com/ZalithLauncher/ZalithLauncher2  
Pinned revision: `7d4f31af01d8a0f6b86e6cc59ff846c24d7bb579`

The upstream project is licensed under GPL-3.0 and includes additional branding requirements for modified redistributions. Before distributing a modified app, we must use a distinct name, clearly label it as an unofficial modified version on the startup or main screen, and preserve copyright notices.

## Planned work

See [NOVALAUNCHER_SPEC.md](NOVALAUNCHER_SPEC.md) and [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md).

The next critical step is to bring the upstream source into this repository so code changes, NovaLauncher branding, loader support, and Modrinth integration can be implemented and reviewed here. Until then, the CI artifact is only an upstream bootstrap build.
