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

### MCP Tools - Browser Automation

This project has **chrome-devtools MCP server** configured with these tools:
- `navigate_page` - Navigate to URLs
- `take_screenshot` - Capture page screenshots
- `click` - Click elements
- `fill` - Fill form inputs
- `wait_for` - Wait for elements/conditions
- `get_console_message` / `list_console_messages` - Console debugging
- `performance_start_trace` / `performance_stop_trace` - Performance analysis

#### Screenshot Best Practices

**CRITICAL: Always use `filePath` parameter to avoid buffer overflow!**

**DO (Recommended):**
```
Use take_screenshot with filePath parameter:
{
  "filePath": "/tmp/screenshot.png",
  "format": "jpeg",
  "quality": 70
}

Then read the file using Read tool to view it.
```

**DON'T:**
```
Never use take_screenshot without filePath - it returns huge base64
data (>1MB) causing buffer overflow in Claude Agent SDK!
```

**Size Optimization:**
- Use `"format": "jpeg"` or `"webp"` instead of PNG (10x smaller!)
- Set `"quality": 60-80` for good balance (0-100 scale)
- Use `"fullPage": false` to capture only viewport
- Use `"uid": "element_id"` to screenshot specific elements only

**Example Task Flow:**
1. `navigate_page` to localhost URL
2. `take_screenshot` with `filePath="/tmp/page.jpg"` and `quality=70`
3. Use Read tool to view `/tmp/page.jpg`
4. Analyze screenshot and continue with `click`, `fill`, etc.

---

(Add more project-specific details here: architecture notes, important patterns,
domain knowledge, external dependencies, deployment info, etc.)
