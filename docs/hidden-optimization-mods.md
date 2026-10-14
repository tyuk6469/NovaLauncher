# Hidden optimization mod bundle

## User-facing behavior
- Add an optional feature called **Optimization Pack** in NovaLauncher settings.
- When enabled, download compatible optimization mods automatically in the background for the selected Minecraft instance.
- Do not list pack-managed mods in the ordinary Mods screen. Show a separate "Optimization Pack" status page with enabled/disabled state, versions, compatibility, download progress, and errors.
- Always let users disable the pack and inspect or remove its managed files.
- Do not hide manually installed mods or mods installed by another tool.

## Compatibility and safety requirements
1. Only download from trusted official project APIs/pages (for example Modrinth API) and verify download URLs, hashes when supplied, and licenses.
2. Resolve versions against the exact Minecraft version, loader (Fabric/Forge/NeoForge), and Java/runtime requirements of the instance.
3. Do not install every mod indiscriminately. Build a curated, versioned allowlist of performance mods and their dependencies.
4. Avoid incompatible or overlapping mods. For example, do not combine Sodium with another renderer replacement that conflicts with it. Treat Lithium, FerriteCore, ImmediatelyFast, Entity Culling, ModernFix, and similar projects as candidates only when the project's compatibility metadata confirms support.
5. Respect required dependencies, optional dependencies, environment-side restrictions, and loader-specific files.
6. Never download from unofficial reuploads, never bundle files without checking redistribution permissions, and never silently modify the user's instance without an opt-out.
7. Download in the background with resumable/progress-aware jobs where possible, use network constraints chosen by the user, and do not block launching Minecraft.
8. Cache downloads and revalidate the pack when Minecraft version or loader changes. On incompatibility, stop and explain instead of silently installing a broken set.
9. Mark pack-managed mods with metadata outside the mod JARs, so the UI can filter them without changing the files. Keep a recovery/removal path.

## Suggested first release
- Fabric first, since the initial target and user's prior mod use is Fabric.
- Add a small curated list, not "all optimization mods".
- Preview the planned set before first activation, then allow automatic background updates.
- Provide an exclusions list and a "show managed mods" toggle for debugging.

## Acceptance checks
- Compatible selected mods download without blocking the UI.
- Incompatible versions are skipped with a visible reason.
- Managed mods are hidden from the ordinary list by default, but remain inspectable/removable in Optimization Pack settings.
- Turning the feature off stops future automatic downloads and offers to remove managed mods.
- A network failure does not corrupt the instance or prevent launching with already-installed mods.
