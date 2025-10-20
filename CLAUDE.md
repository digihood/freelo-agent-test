# Autonomous Agent Project Instructions

**IMPORTANT**: This is an autonomous agent workspace for processing Freelo tasks.
You are running as a bot, not in interactive mode. Follow these instructions precisely.

## Git Workflow (YOU MUST FOLLOW THIS)

### Branch Strategy
- **Base branch**: `dev` (NOT `main`)
- **Feature branches**: `freelo-task-{task_id}` (automatically created from `dev`)
- **Pull requests**: Target `dev` branch (NOT `main`)
- **Branch flow**: `main` → `dev` → `freelo-task-{id}` → PR to `dev`

### Commit Messages
Follow conventional commits format:
```
type(scope): subject

Body explaining what and why (not how)

Refs: freelo-task-{task_id}
```

**Types**: feat, fix, docs, style, refactor, test, chore

### Pre-Commit Checklist
1. Ensure all tests pass
2. Follow project coding standards
3. Add tests for new features
4. Update documentation if needed

## Your Workflow

### 1. Task Understanding
- Read task title and description carefully
- Check subtasks list
- Identify all requirements

### 2. Planning (REQUIRED)
- **YOU MUST** use TodoWrite tool to create execution plan
- Break down work into clear steps
- Estimate complexity realistically

### 3. Implementation
- Follow project coding standards (see Skills)
- Write clean, readable code
- Add meaningful comments for complex logic
- Keep functions small and focused

### 4. Testing
- Write tests for new features
- Run existing tests to ensure nothing breaks
- Verify test coverage is meaningful

### 5. Verification
- Review your changes before committing
- Ensure all subtasks are completed
- Check that implementation matches requirements

## Key Commands

### Testing
```bash
# Run tests (if TEST_COMMAND is configured)
pytest
npm test
# ... project-specific test commands
```

### Git Operations
```bash
# Git operations are handled automatically by the orchestrator
# You don't need to run git commands manually
# Focus on code implementation
```

## Project-Specific Notes

- This workspace is shared across tasks (main workspace strategy)
- Changes are automatically committed and pushed
- Pull requests are created automatically
- Focus on implementation quality, not git operations

## Common Pitfalls to Avoid

- ❌ Don't target `main` branch for PRs (use `dev`)
- ❌ Don't skip TodoWrite planning (required for tracking)
- ❌ Don't commit without running tests
- ❌ Don't ignore subtasks in task description
- ❌ Don't make assumptions - ask via comments if unclear

## Remember

You are an autonomous bot. Work systematically, follow the workflow,
and deliver quality code. The orchestrator handles git operations.
