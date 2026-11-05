# NovaLauncher development plan

## Milestones

1. [x] Pin ZalithLauncher2 source and establish a reproducible arm64 debug CI build.
2. [x] Add distinct NovaLauncher app metadata and an explicit unofficial-modification startup notice.
3. [x] Audit the pinned upstream source for reusable Fabric, Forge, Modrinth, CurseForge, and installed-mod-management features.
4. [ ] Trace the end-to-end flows from home screen through version creation, loader installation, mod discovery, and mod management.
5. [ ] Verify current CurseForge API authorization and terms; keep it disabled if requirements cannot be met.
6. [ ] Implement the Nova home screen using existing navigation and state rather than a disconnected mock screen.
7. [ ] Add Nova-specific compatibility safeguards and local JAR import improvements only where the upstream implementation has gaps.
8. [ ] Implement the optional Optimization Pack with a curated allowlist, per-instance ownership metadata, dependency checks, hashes, and rollback-safe downloads.
9. [ ] Test supported Minecraft versions, Fabric and Forge, mod installation, single-player, multiplayer, and existing instances on a physical Android device.

## Current implementation status

The app is currently a branded bootstrap based on the pinned ZalithLauncher2 submodule. The startup notice is injected by `scripts/apply-nova-branding.py` during CI. The main Nova home-screen redesign and Nova-specific Optimization Pack are not implemented yet.

The upstream source already includes substantial launcher functionality:
- Fabric and Forge loader metadata and installation paths.
- Modrinth and CurseForge search/API classes.
- Mod search and installed-mod management screens.
- Mod metadata readers and modpack import/export.

See [docs/upstream-feature-audit.md](docs/upstream-feature-audit.md). The audit confirms source files exist, not that every flow is bug-free or compatible with every Minecraft release. Reuse existing code where possible; avoid duplicate implementations.

## Build and verification

The workflow builds an arm64 debug APK from a pinned upstream revision and uploads it as a GitHub Actions artifact. A successful CI build verifies compilation and artifact upload only. It does not prove installation, game launch, mod compatibility, or multiplayer stability on a physical device.

## Performance and multiplayer

Profile before optimizing. Record average FPS, frame times/1% lows, per-core CPU use, memory, and thermals. Keep ordinary client-side optimizations separate from experimental engine/threading changes.

Never parallelize world ticks or shared game-state mutation without a proven thread-safe design and extensive compatibility tests. Preserve normal network protocol behavior and test on a private disposable server before recommending public-server use.

Detailed procedure: [docs/MULTITHREADING_EXPERIMENT.md](docs/MULTITHREADING_EXPERIMENT.md).

## AI collaboration

ChatGPT, Claude, Copilot, and other agents may work in parallel only on separate branches and non-overlapping tasks. Follow [docs/AI_COLLABORATION.md](docs/AI_COLLABORATION.md). The repository specification and actual source code are the source of truth.
