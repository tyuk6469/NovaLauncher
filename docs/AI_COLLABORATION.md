# Multi-agent AI workflow for NovaLauncher

This repository can be worked on by ChatGPT, Claude, Copilot, or another coding assistant. The safe approach is to coordinate through GitHub rather than letting several agents edit the same files at once.

## Shared source of truth

Every agent must read these files before making changes:

1. `NOVALAUNCHER_SPEC.md`
2. `DEVELOPMENT_PLAN.md`
3. `docs/upstream-feature-audit.md`
4. `.github/copilot-instructions.md`

The specification and existing code take priority over an agent's assumptions. Fabric and Forge are in scope. NeoForge and Quilt are not in the initial scope.

## Parallel work without collisions

- Give each agent one independent task and a separate Git branch.
- Do not assign two agents to edit the same file or feature simultaneously.
- Ask each agent to inspect the current branch before editing.
- Require a pull request or a commit on its own branch; review changes before merging into `main`.
- Do not let an agent merge, force-push, rotate credentials, or publish a release without the owner's approval.
- Keep the upstream ZalithLauncher2 submodule pinned unless an explicit upstream-update task is approved.
- Never paste Microsoft account tokens, API keys, signing keys, keystores, passwords, or private logs into an AI chat.

## Suggested division of work

| Agent | Good task | Must avoid |
|---|---|---|
| ChatGPT | Architecture, task breakdown, integration review, targeted implementation | Claiming a build passed without CI evidence |
| Claude | Review large Kotlin files, trace existing flows, propose or implement an isolated feature | Editing the same files as another agent |
| Copilot / other coding agent | Small isolated code changes and tests in a dedicated branch | Broad refactors without an agreed plan |

These are suggested roles, not technical requirements. Any agent may do a task if it follows the same repository rules.

## Required handoff format

For every task, the agent should report:

- Branch and commit/PR link.
- Exact files changed.
- Behavior added or fixed.
- Tests and build commands actually run, with results.
- Known limitations and follow-up work.

Before merging, review the diff for accidental upstream changes, secrets, licensing/attribution issues, compatibility regressions, and unrelated formatting churn.

## How to add another AI

1. Connect the AI's GitHub integration to this repository, or give it a branch-based coding workspace.
2. Give it the shared source-of-truth files listed above.
3. Assign one specific task and branch.
4. Ask it to open a pull request instead of committing directly to `main`.
5. Review and test the pull request before merging.

A separate API key or paid plan may be required depending on the AI service and its GitHub integration. Never share account passwords or personal access tokens in chat; use the provider's official authorization flow.
