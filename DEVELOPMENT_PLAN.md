# NovaLauncher development plan

## Milestones

1. Verify the arm64 Android debug build in GitHub Actions.
2. Bring the upstream launcher source into this repository as a pinned, reproducible source snapshot or submodule.
3. Apply distinct NovaLauncher branding and the upstream GPL-3.0 additional branding terms before distributing a modified build.
4. Add launcher-side features in small commits, validating each with a build.
5. Test Fabric, Forge, and NeoForge installation paths and Modrinth integration before advertising support.

## Current limitation

The current workflow checks out the upstream repository at its moving `main` branch and builds it as a bootstrap test. That verifies the toolchain, not NovaLauncher-specific changes. No APK should be called a NovaLauncher release until the app branding and source modifications are in place and the build succeeds.

## First technical priorities

- Keep upstream copyright and license notices.
- Use a unique application name and visible unofficial-modification label in any redistributed modified app.
- Pin upstream revisions for reproducible builds.
- Keep CI artifacts for each successful build and inspect build logs when failures occur.
