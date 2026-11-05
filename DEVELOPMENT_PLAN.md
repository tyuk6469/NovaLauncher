# NovaLauncher development plan

## Milestones

1. Verify the arm64 Android debug build in GitHub Actions.
2. Bring the upstream launcher source into this repository as a pinned, reproducible source snapshot or submodule.
3. Apply distinct NovaLauncher branding and the upstream GPL-3.0 additional branding terms before distributing a modified build.
4. Add launcher-side features in small commits, validating each with a build.
5. Test Fabric, Forge, and NeoForge installation paths and Modrinth integration before advertising support.
6. Profile Minecraft on Android and investigate safe, measurable improvements to worker-thread usage without moving authoritative game-state updates off their owning thread.

## Current limitation

The current app is a branded bootstrap based on a pinned ZalithLauncher2 submodule. It is not a rewritten Minecraft engine. Launcher-side changes alone cannot make Minecraft's game loop multithreaded.

The successful CI run verifies that the arm64 debug APK can be built and uploaded. It does not verify installation or runtime behavior on a physical phone.

## First technical priorities

- Keep upstream copyright and license notices.
- Use a unique application name and visible unofficial-modification label in any redistributed modified app.
- Pin upstream revisions for reproducible builds.
- Keep CI artifacts for each successful build and inspect build logs when failures occur.
- Establish repeatable FPS, frame-time, per-core CPU, memory, and thermal baselines before performance changes.
- Prefer supported configuration and existing asynchronous task boundaries before attempting engine-level patches.
- Never parallelize world ticks or shared game-state mutation without a proven thread-safe design and extensive compatibility tests.
- Keep experimental changes optional and easy to disable or revert.

## Multithreading experiment

The research-first procedure and safety gates are documented in [docs/MULTITHREADING_EXPERIMENT.md](docs/MULTITHREADING_EXPERIMENT.md). No Minecraft game-loop code has been changed yet.
