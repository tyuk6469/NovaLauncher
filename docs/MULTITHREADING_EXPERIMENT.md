# Multithreading experiment (research-first)

## Goal

Investigate whether NovaLauncher can improve Minecraft Java Edition performance on Android by reducing main-thread stalls and using available worker threads more effectively.

This is an experiment, not a promise that Minecraft can be made fully multithreaded. The launcher itself does not own Minecraft's game loop, and changing the launcher's thread count cannot automatically parallelize game logic.

## Non-negotiable rule: preserve correctness

Do not move world ticks, entity updates, block updates, or other shared mutable game-state operations onto arbitrary threads. These operations have ordering and thread-affinity assumptions; changing them blindly can cause world corruption, desynchronization, crashes, and mod incompatibility.

No experimental patch may be enabled by default. Keep a clean baseline and a one-step rollback path.

## Staged approach

### Stage 0 - establish a baseline

- Use the same device, Minecraft version, loader, world, render distance, simulation distance, graphics settings, and mod set for every run.
- Record average FPS and frame-time percentiles (especially 1% lows), not only peak FPS.
- Record CPU usage per core, memory use, thermal state, and chunk-loading behavior.
- Repeat each run enough times to distinguish a real change from normal measurement noise.
- Compare a clean Fabric profile with the user's normal mod profile.

### Stage 1 - inspect existing parallel work

Map which tasks already run away from the main thread in the pinned Minecraft/Fabric version and in the Android runtime. Inspect chunk IO, resource loading, asset preparation, and rendering boundaries before proposing changes.

Prefer existing supported configuration and upstream fixes over patches.

### Stage 2 - isolate a low-risk prototype

Only prototype work that is naturally independent and has clear ownership of its data, such as preprocessing immutable data or IO that is already asynchronous. Use bounded worker pools, explicit cancellation, and a defined handoff back to the owning thread.

Do not parallelize authoritative world-state mutation. Do not introduce a global "use all cores" switch.

### Stage 3 - compatibility and regression checks

For every prototype:
- Build and launch on Android ARM64.
- Test a new disposable world before any existing world.
- Check save/reload, chunk borders, entities, redstone, dimensions, and multiplayer behavior where applicable.
- Test with no mods, Fabric API only, and a small representative mod set.
- Verify that disabling the experiment restores baseline behavior.
- Reject the change if correctness, stability, or mod compatibility regresses.

### Stage 4 - decision

Keep a change only if repeatable measurements show a meaningful improvement in frame-time or stutter without correctness or compatibility regressions. Otherwise revert it and document the result.

## Current scope and constraints

- NovaLauncher currently builds a branded bootstrap based on a pinned ZalithLauncher2 submodule; it is not a rewritten Minecraft engine.
- Launcher-side changes alone cannot safely change Minecraft's internal game-loop architecture.
- The first viable route is profiling plus supported optimizations. A deeper game-engine experiment would need a separate, version-specific client patch and could break Fabric mods.
- Horizon is a separate Rust implementation, not a drop-in multithreading patch for Minecraft 1.21.11 Fabric.

## Status

Research plan only. No Minecraft game-loop code has been changed by this document.
