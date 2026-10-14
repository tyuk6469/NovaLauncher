# NovaLauncher

NovaLauncher is a personal Android launcher project for Minecraft: Java Edition.

## Status

The repository is being set up. The first workflow is a **bootstrap build only**: it builds the upstream ZalithLauncher2 source for arm64 so we can verify the build pipeline. This is not yet a NovaLauncher-branded release and should not be presented as one.

## Build a bootstrap APK

1. Open the **Actions** tab.
2. Select **Bootstrap Android APK**.
3. Press **Run workflow**.
4. When it finishes, open the run and download the `upstream-bootstrap-arm64-debug` artifact.

The APK is built from the upstream project at https://github.com/ZalithLauncher/ZalithLauncher2. The upstream project is licensed under GPL-3.0 and includes additional branding requirements for modified redistributions. Before distributing a modified app, we must use a distinct name, clearly label it as an unofficial modified version on the startup or main screen, and preserve copyright notices.

## Planned work

- Verify the Android arm64 build in GitHub Actions.
- Create the NovaLauncher branding and apply the upstream license requirements.
- Add and test launcher features in small, reviewable changes.
- Build and test the NovaLauncher APK.
