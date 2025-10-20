---
name: Project Workflow
description: Git workflow, coding standards, and testing requirements for this project. Use when writing code, making commits, or reviewing changes.
---

# Project Workflow

This skill contains project-specific guidelines and standards.

## Git Workflow

### Branch Naming
- Feature branches: `task-{task_id}` (automatically created)
- Main branch: `main`

### Commit Messages
Follow conventional commits format:
```
type(scope): subject

Body explaining what and why (not how)

Refs: task-{task_id}
```

Types: feat, fix, docs, style, refactor, test, chore

### Pull Requests
- Title: Task title from Freelo
- Description: Includes task link and implementation notes
- Target branch: `main`

## Coding Standards

### Code Quality
- Write clean, readable code
- Add comments for complex logic
- Follow DRY principle
- Keep functions small and focused

### Testing
- Write tests for new features
- Ensure existing tests pass
- Aim for meaningful test coverage

## Project Structure

```
workspaces/
  {repo-name}/              # Shared main workspace
    .git/                   # Repository
    .claude/skills/         # This skill directory
    worktrees/
      task-{id}/            # Task-specific worktree
```

## Common Tasks

### Implementing Features
1. Understand requirements from task description
2. Check existing code for patterns
3. Write implementation
4. Add/update tests
5. Verify all tests pass

### Fixing Bugs
1. Reproduce the issue
2. Identify root cause
3. Implement fix
4. Add regression test
5. Verify fix works

## Notes

- This skill is automatically discovered by Claude Code
- Update this file to add project-specific guidelines
- Keep it focused and actionable
