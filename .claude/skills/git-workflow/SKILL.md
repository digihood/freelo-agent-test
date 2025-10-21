---
name: Git Workflow
description: Git workflow, branch strategy, and commit conventions. Use when making commits, creating branches, or working with git.
---

# Git Workflow

This skill describes the git workflow used in this project by the autonomous agent.

## Branch Strategy

### Base Branches
- **main** - Production branch (read-only mirror of remote)
- **dev** - Development branch (read-only mirror of remote)
- All base branches are treated as mirrors of remote state

### Task Branches
- **Format:** `freelo-task-{task_id}`
- **Created from:** `dev` branch (NOT from main!)
- **Target for PR:** `dev` branch (NOT main!)
- **Example:** `freelo-task-25368707`

### Workflow Flow
```
main (remote mirror)
  ↓
dev (remote mirror) ← you start here
  ↓
freelo-task-{id} ← your work branch
  ↓
PR to dev ← create pull request
  ↓
(manual merge to main by admin)
```

## Important Git Rules

### CRITICAL: Never Commit Directly to Base Branches
- ❌ **NEVER** commit to `main` or `dev` directly
- ❌ **NEVER** push to `main` or `dev`
- ✅ **ALWAYS** create task branch from `dev`
- ✅ **ALWAYS** create PR to `dev` (not main!)

### Base Branch Mirror Policy
- Base branches (`main`, `dev`) are **read-only mirrors** of remote
- Before task: `dev` is synced to `origin/dev`
- Any local changes on base branches are **stashed** (not restored)
- Base branches remain **clean mirrors** of remote state

### Task Processing Flow
1. Ensure `dev` branch exists (create from `main` if needed)
2. Checkout `dev` and pull latest changes
3. **DO YOUR WORK on dev branch** (not on task branch yet!)
4. When done, task branch is created from `dev` with `preserve_changes=True`
5. Commit happens on task branch
6. Push task branch to remote
7. Create PR: `freelo-task-{id} → dev`

### Why This Works
- You do your work on `dev` branch directly
- `preserve_changes=True` means your uncommitted changes are kept when creating task branch
- This prevents changes from being stashed and lost
- Task branch is just a "snapshot" branch for the PR

## Commit Message Format

### Conventional Commits
```
type(scope): subject

Body explaining what and why (optional)

Refs: freelo-task-{task_id}
```

### Types
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation changes
- `style` - Code style changes (formatting, etc.)
- `refactor` - Code refactoring
- `test` - Adding or updating tests
- `chore` - Maintenance tasks

### Examples
```
feat(auth): add user login functionality

Implements login form with email/password validation.
Connects to authentication API endpoint.

Refs: freelo-task-12345
```

```
fix(ui): correct button alignment in header

Refs: freelo-task-67890
```

## Your Role: Code Implementation Only

### What You DO:
1. **Read the task** description and requirements
2. **Analyze existing code** using Read, Grep, Glob tools
3. **Implement changes** using Edit, Write tools
4. **Test your work** using Bash tool (run tests, dev server, etc.)
5. **Verify implementation** works correctly
6. **Provide summary** in Czech language at the end

### What You DON'T Do (Orchestrator Handles):
- ❌ **NEVER use git commands** (no `git add`, `git commit`, `git push`)
- ❌ **NEVER create branches** - orchestrator creates task branch
- ❌ **NEVER commit changes** - orchestrator commits automatically
- ❌ **NEVER push to remote** - orchestrator pushes automatically
- ❌ **NEVER create PR** - orchestrator creates Pull Request

### Available Tools:
- ✅ **Read** - Read files
- ✅ **Edit** - Edit files
- ✅ **Write** - Create new files
- ✅ **Grep** - Search code
- ✅ **Glob** - Find files
- ✅ **Bash** - Run commands (tests, dev server, etc.)
- ✅ **TodoWrite** - Track subtasks
- ✅ **MCP tools** - Chrome DevTools, etc. (if configured)

### How Git Workflow Works Behind the Scenes:

**Before you start:**
1. Orchestrator checkouts `dev` branch
2. Orchestrator pulls latest changes
3. You work directly on `dev` branch

**While you work:**
- Make all your code changes on `dev` branch
- Files remain uncommitted
- Your changes are "dirty" in git (unstaged)

**After you finish:**
1. Orchestrator creates task branch: `freelo-task-{id}` (with `preserve_changes=True`)
2. Orchestrator commits your changes with conventional commit message
3. Orchestrator pushes task branch to remote
4. Orchestrator creates PR: `freelo-task-{id} → dev`
5. Orchestrator reports results to Freelo

### Key Points:
- ✅ You work on `dev` branch (not on task branch!)
- ✅ Focus ONLY on writing code
- ✅ Don't worry about git - orchestrator handles everything
- ✅ Your uncommitted changes are preserved and committed by orchestrator

## Push Robustness

### Force-with-Lease Strategy
- Uses `--force-with-lease` instead of `--force` (safer)
- Prevents overwriting others' work
- If push rejected: fetch + rebase attempt, then force-with-lease fallback
- Handles race conditions automatically

## Pull Request Creation

### PR Details
- **Title:** Task title from Freelo
- **Description:**
  - Link to Freelo task
  - Implementation summary
  - Changed files list
  - Git stats (insertions/deletions)
- **Base branch:** `dev` (CRITICAL!)
- **Head branch:** `freelo-task-{task_id}`

### After PR is Created
- PR URL is reported back to Freelo
- Team reviews the PR
- PR is merged to `dev` manually
- Eventually `dev` is merged to `main`

## Notes

- Git operations are **fully automated** by orchestrator
- You work on `dev` branch, orchestrator handles the rest
- Main workspace is **preserved and reused** for all tasks
- Sequential processing only (no parallel tasks)
