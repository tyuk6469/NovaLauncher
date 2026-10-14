# NovaLauncher - repository instructions for coding agents

## Goal
Develop NovaLauncher, an Android Minecraft Java launcher based on the ZalithLauncher2 upstream, with a distinct identity and a home screen inspired by the reference in docs/home-screen-design.md.

## Work rules
- Inspect the existing code and current build configuration before editing. Do not assume a feature exists because it is mentioned in a plan.
- Make small, testable changes. Build and run the narrowest relevant tests after each change.
- Never report a build or test as successful unless its command actually completed successfully. Include the command and a concise result in the final summary.
- If blocked, report the exact blocker and next actionable step instead of pretending the work is done.
- Prefer changes in the repository over long planning documents when implementation is feasible.
- Do not replace working launcher functionality with a static mockup. UI controls must connect to real app navigation/state.
- Preserve existing Minecraft version, loader, account, installation, log, and settings behavior unless the task explicitly changes it.
- Treat Minecraft versions and Fabric/Forge/NeoForge compatibility as exact constraints. Verify compatibility from trusted metadata before choosing dependencies.
- Do not download or install every optimization mod indiscriminately. Follow docs/hidden-optimization-mods.md: curated allowlist, correct loader/game version, dependencies, conflict checks, license checks, hashes where available, background downloads, clear errors, opt-out and removal.
- Keep pack-managed optimization mods distinguishable internally from manually installed mods. Never hide manually installed mods.
- Use the NovaLauncher name and branding. Do not imply that this is the official Zalith Launcher. Preserve required upstream license, attribution, and branding notices.
- Never commit secrets, signing keys, passwords, access tokens, or local machine credentials.
- Avoid destructive git history changes and do not force-push.
- Prefer a branch and pull request for substantial changes. Do not merge or publish releases without explicit user approval.

## Priority order
1. Make the pinned upstream Android build reproducible.
2. Import/manage upstream source in a maintainable way and verify an arm64 debug APK build.
3. Implement the responsive NovaLauncher home screen from docs/home-screen-design.md using the real app architecture.
4. Implement a curated, optional background Optimization Pack, starting with Fabric.
5. Add loader-aware Modrinth discovery/install flows and tests.
6. Improve performance only with measurements and compatibility checks.

## Final response format
Summarize: changed files, actual tests/build commands and outcomes, known limitations, and the next step. Be concise and honest.
