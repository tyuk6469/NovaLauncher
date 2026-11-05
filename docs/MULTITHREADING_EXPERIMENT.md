# Multithreading experiment (research-first)

## Goal

Investigate whether NovaLauncher can improve Minecraft Java Edition performance on Android by reducing main-thread stalls and using available worker threads more effectively.

**Top priority: preserve compatibility with multiplayer servers.** A small FPS gain is not worth losing the ability to join ordinary servers or causing desynchronization, rubber-banding, broken interactions, or disconnects.

This is an experiment, not a promise that Minecraft can be made fully multithreaded. The launcher itself does not own Minecraft's game loop, and changing the launcher's thread count cannot automatically parallelize game logic.

## Non-negotiable rules

- Do not change the Minecraft network protocol, packet contents, packet order, connection handling, or server-side behavior.
- Do not alter authoritative world ticks, entity updates, block updates, inventory/container state, or other shared mutable game-state operations by moving them onto arbitrary threads.
- Preserve the existing client-thread handoff rules used by vanilla Minecraft and Fabric.
- Do not introduce client behavior that gives an unfair gameplay advantage or changes what the server sees.
- No experimental patch may be enabled by default. Keep a clean baseline and a one-step rollback path.
- If an optimization breaks multiplayer compatibility, it is rejected even if single-player FPS improves.

These operations have ordering and thread-affinity assumptions; changing them blindly can cause world corruption, desynchronization, crashes, and mod incompatibility.

## Staged approach

### Stage 0 - establish a baseline

- Use the same device, Minecraft version, loader, world/server, render distance, simulation distance, graphics settings, and mod set for every run.
- Record average FPS and frame-time percentiles (especially 1% lows), not only peak FPS.
- Record CPU usage per core, memory use, thermal state, and chunk-loading behavior.
- Repeat each run enough times to distinguish a real change from normal measurement noise.
- Compare a clean Fabric profile with the user's normal mod profile.
- Record connection stability and latency separately from local FPS.

### Stage 1 - inspect existing parallel work

Map which tasks already run away from the main thread in the pinned Minecraft/Fabric version and in the Android runtime. Inspect chunk IO, resource loading, asset preparation, and rendering boundaries before proposing changes.

Prefer existing supported configuration and upstream fixes over patches. Do not assume a task is safe to parallelize merely because it is CPU-heavy.

### Stage 2 - isolate a low-risk prototype

Only prototype work that is naturally independent and has clear ownership of its data, such as preprocessing immutable data or IO that is already asynchronous. Use bounded worker pools, explicit cancellation, and a defined handoff back to the owning thread.

Do not parallelize authoritative world-state mutation. Do not introduce a global "use all cores" switch. Avoid changing networking code entirely in the first prototype.

### Stage 3 - multiplayer compatibility gate

Every prototype must pass all of these before it can be considered:

1. Launches with the target Minecraft version and Fabric loader on Android ARM64.
2. Works in a fresh single-player world, including save, exit, and reload.
3. Joins a normal vanilla-compatible multiplayer server without requiring server-side plugins or mods.
4. Completes a sustained multiplayer session without unexpected disconnects, packet errors, desynchronization, or abnormal rubber-banding.
5. Correctly handles chunk loading/unloading, entity movement, inventory/container interactions, block interaction, dimensions, and respawn.
6. Does not change packet contents, packet order, or protocol compatibility.
7. Works with the baseline Fabric setup and then a small representative set of client-side mods.
8. Can be disabled cleanly to restore baseline behavior.

Test on a private test server first, then a public server only with permission and without risking valuable items or progress. Never use a valuable survival world as the first test.

### Stage 4 - decision

Keep a change only if repeatable measurements show a meaningful improvement in frame-time or stutter **and** all multiplayer checks pass. Otherwise revert it and document the result.

## Current scope and constraints

- NovaLauncher currently builds a branded bootstrap based on a pinned ZalithLauncher2 submodule; it is not a rewritten Minecraft engine.
- Launcher-side changes alone cannot safely change Minecraft's internal game-loop architecture.
- The first viable route is profiling plus supported optimizations. A deeper game-engine experiment would need a separate, version-specific client patch and could break Fabric mods or multiplayer compatibility.
- Horizon is a separate Rust implementation, not a drop-in multithreading patch for Minecraft 1.21.11 Fabric.

## Status

Research plan only. No Minecraft game-loop or networking code has been changed by this document.
