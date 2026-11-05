# NovaLauncher - repository instructions for coding agents

## Goal
Develop NovaLauncher, an Android Minecraft Java launcher based on the pinned ZalithLauncher2 upstream, with distinct branding and a Nova-specific home screen.

## Required reading
Before editing, read:
- `NOVALAUNCHER_SPEC.md`
- `DEVELOPMENT_PLAN.md`
- `docs/upstream-feature-audit.md`
- Relevant UI/architecture docs and source files.

## Work rules
- Inspect the existing code and current build configuration before editing. Do not assume a feature exists because it is mentioned in a plan.
- The pinned upstream already contains Fabric/Forge installer code, Modrinth/CurseForge search code, a mod search screen, and an installed-mod manager. Trace and test these before reimplementing anything.
- Make small, testable changes. Build and run the narrowest relevant tests after each change.
- Never report a build or test as successful unless the command actually completed successfully. Include the command and a concise result in the final summary.
- Prefer real app changes over additional planning documents when implementation is feasible.
- Do not replace working launcher functionality with a static mockup. UI controls must connect to real app navigation/state.
- Preserve existing Minecraft version, loader, account, installation, log, and settings behavior unless the task explicitly changes it.
- Fabric and Forge are required for initial NovaLauncher scope. NeoForge and Quilt are out of scope unless the owner asks later.
- Treat Minecraft versions and loader compatibility as exact constraints. Verify metadata before claiming support.
- Do not download/install every optimization mod indiscriminately. Follow `docs/hidden-optimization-mods.md`: curated allowlist, correct loader/game version, dependencies, conflicts, license checks, hashes where available, opt-out, and removal.
- Keep pack-managed optimization mods distinguishable internally from manually installed mods. Never hide manually installed mods.
- Use the NovaLauncher name and branding. Do not imply this is the official Zalith Launcher. Preserve upstream license, attribution, and branding requirements.
- Never commit secrets, signing keys, passwords, access tokens, or local machine credentials.
- Avoid destructive git history changes and do not force-push.
- Prefer a branch and pull request for substantial changes. Do not merge or publish releases without explicit owner approval.
- For multi-agent work, follow `docs/AI_COLLABORATION.md` and avoid editing files assigned to another agent.

## Priority order
1. Keep the pinned upstream Android build reproducible.
2. Trace and test existing loader, mod search, and mod manager flows.
3. Implement the Nova home screen in the real app architecture.
4. Add the optional Optimization Pack.
5. Improve performance only with measurements and compatibility checks.

## Final response format
Summarize: changed files, actual tests/build commands and outcomes, known limitations, and the next step. Be concise and honest.
