# Project Information

## Repository Structure

```
/
├── src/                # Source code
├── tests/              # Test files
├── .claude/            # Claude Code configuration
│   └── skills/         # Project-specific skills
└── CLAUDE.md           # This file
```

## Technology Stack

- **Language**: (to be specified per project)
- **Framework**: (to be specified per project)
- **Testing**: (to be specified per project)
- **Linting**: (to be specified per project)

## Development Commands

### Testing
```bash
# Run tests
pytest                  # Python projects
npm test                # Node.js projects
# Add project-specific test commands here
```

### Linting & Formatting
```bash
# Format code
black .                 # Python
prettier --write .      # JavaScript/TypeScript
# Add project-specific commands here
```

### Build
```bash
# Build project (if applicable)
# Add project-specific build commands here
```

## Coding Conventions

- Follow language-specific best practices
- Maintain existing code style
- Add tests for new features
- Update documentation when changing APIs

## Git Workflow

### Branch Strategy
- Base branch: `dev`
- Feature branches: `freelo-task-{task_id}` (auto-created)
- Pull requests target: `dev` branch

### Commit Message Format
```
type(scope): subject

Body (optional)

Refs: freelo-task-{task_id}
```

Types: feat, fix, docs, style, refactor, test, chore

## Notes

- Git operations (commit, push, PR) are handled automatically by orchestrator
- This workspace is shared across tasks (main workspace strategy)
- CLAUDE.md can be customized per project - add project-specific context below

---

## Project-Specific Context

(Add project-specific details here: architecture notes, important patterns,
domain knowledge, external dependencies, deployment info, etc.)
