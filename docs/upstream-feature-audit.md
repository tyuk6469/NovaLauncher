# Upstream feature audit

Audit target: ZalithLauncher2 submodule revision `7d4f31af01d8a0f6b86e6cc59ff846c24d7bb579`.

This is a source-level audit only. It confirms that relevant code exists in the pinned upstream tree; it does not yet prove every flow works on the target phone or for every Minecraft release.

## Confirmed existing implementation

| Area | Existing source | Finding |
|---|---|---|
| Main Android activity and Compose UI | `ZalithLauncher/src/main/java/com/movtery/zalithlauncher/ui/activities/MainActivity.kt` | Existing app entry activity and navigation host |
| Fabric loader metadata/install | `game/addons/modloader/fabriclike/fabric/`, `game/download/game/fabric/` | Fabric version metadata and installer path exist |
| Forge loader metadata/install | `game/addons/modloader/forgelike/forge/`, `game/download/game/forge/` | Forge version metadata and installer path exist |
| Modrinth search/API | `game/download/assets/platform/modrinth/` | Search, project/version lookup and API client exist |
| CurseForge search/API | `game/download/assets/platform/curseforge/` | Existing provider integration exists; verify current API key, terms and runtime behavior before relying on it |
| In-launcher mod search | `ui/screens/content/download/assets/search/SearchModScreen.kt` | Existing search screen supports Modrinth and CurseForge platform selection |
| Installed mod management | `ui/screens/content/versions/ModsManagerScreen.kt` | Existing per-version mod manager screen exists |
| Mod metadata parsing | `game/version/mod/meta/`, `game/version/mod/reader/` | Fabric and Forge metadata readers exist |
| Modpack import/export | `game/download/modpack/platform/`, `game/version/export/platform/` | Modrinth and CurseForge pack support exists |

The paths above are relative to `ZalithLauncher/src/main/java/com/movtery/zalithlauncher/` unless stated otherwise.

## What this means for NovaLauncher

Do not build a second Modrinth client, Forge installer, Fabric installer, or mod manager before checking whether the upstream implementation can be safely reused. The likely fastest route is to preserve these mature flows and add Nova-specific UI, compatibility checks, and optional optimization-pack management around them.

## Remaining checks before claiming support

- Trace the actual navigation path from the home screen to version creation, loader installation, mod search, and installed-mod management.
- Inspect how selected Minecraft version and loader are passed into Modrinth/CurseForge filters.
- Verify dependency resolution, environment-side filtering, hash validation, download cancellation, and safe file replacement.
- Confirm CurseForge API authorization/configuration and current terms; existing source files alone do not prove that API calls are usable.
- Build a real compatibility matrix from official metadata. Do not promise every Minecraft/loader/mod combination.
- Run installation and launch tests on a physical Android device, including a Fabric profile, a Forge profile, and multiplayer.
- Identify stable extension points for Nova branding and the redesigned home screen without forking large upstream files unnecessarily.

## Current status

- [x] Locate existing Fabric and Forge installer code.
- [x] Locate existing Modrinth and CurseForge API/search code.
- [x] Locate existing installed-mod manager and mod search screens.
- [ ] Trace and test the end-to-end flows.
- [ ] Add Nova-specific features only where the upstream implementation is missing or insufficient.
