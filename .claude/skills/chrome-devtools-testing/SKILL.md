---
name: Chrome DevTools Testing
description: Browser automation and UI testing guidelines using chrome-devtools MCP server. Use when testing user interfaces, taking screenshots, or automating browser interactions.
---

# Chrome DevTools Testing

This skill provides guidelines for testing user interfaces using Chrome DevTools MCP server.

## When to Use This Skill

**CRITICAL: Use Chrome DevTools MCP tools when:**
- Testing user interface implementation
- Verifying visual changes (buttons, forms, layouts)
- Taking screenshots for documentation or verification
- Testing form submissions and interactions
- Checking console errors or performance
- Any task mentioning "test UI", "verify page", "screenshot", or "browser"

**DO NOT use when:**
- Writing backend API code (no UI)
- Database operations only
- File processing without browser

## Available MCP Tools (27 total)

Chrome DevTools MCP provides comprehensive browser automation across 6 categories.

### 1. Input Automation (7 tools)

**Clicking & Dragging:**
- `mcp__chrome-devtools__click` - Click element by UID
- `mcp__chrome-devtools__drag` - Drag element to target position

**Form Interaction:**
- `mcp__chrome-devtools__fill` - Fill input field with value
- `mcp__chrome-devtools__upload_file` - Upload file to input element

**Mouse & Dialog:**
- `mcp__chrome-devtools__hover` - Hover over element
- `mcp__chrome-devtools__accept_dialog` - Accept browser dialog (alert/confirm)
- `mcp__chrome-devtools__dismiss_dialog` - Dismiss browser dialog

### 2. Navigation Automation (7 tools)

**Page Management:**
- `mcp__chrome-devtools__create_page` - Create new browser tab/page
- `mcp__chrome-devtools__select_page` - Switch to specific page
- `mcp__chrome-devtools__close_page` - Close browser page

**URL Navigation:**
- `mcp__chrome-devtools__navigate_page` - Navigate to URL
  ```json
  {"url": "http://localhost:3000/page"}
  ```

**History & Loading:**
- `mcp__chrome-devtools__go_back` - Browser back button
- `mcp__chrome-devtools__go_forward` - Browser forward button
- `mcp__chrome-devtools__wait_for_page` - Wait for page load/state

### 3. Emulation (3 tools)

**Performance Testing:**
- `mcp__chrome-devtools__set_cpu_throttling` - Simulate slow CPU (rate: 1-100)
- `mcp__chrome-devtools__set_network_throttling` - Simulate slow network (3G, 4G, etc.)
- `mcp__chrome-devtools__set_viewport` - Resize viewport (width, height)

### 4. Performance Analysis (3 tools)

**Profiling:**
- `mcp__chrome-devtools__start_performance_trace` - Start recording performance
- `mcp__chrome-devtools__stop_performance_trace` - Stop and analyze trace (Core Web Vitals)
- `mcp__chrome-devtools__measure_performance` - Get performance metrics

### 5. Network Monitoring (2 tools)

**Request Tracking:**
- `mcp__chrome-devtools__get_network_requests` - Get all HTTP requests since navigation
- `mcp__chrome-devtools__monitor_network` - Real-time network monitoring

### 6. Debugging (5 tools)

**Screenshots:**
- `mcp__chrome-devtools__take_screenshot` - Capture page/element screenshot
  ```json
  {
    "filePath": "/tmp/screenshot.jpg",
    "format": "jpeg",
    "quality": 70,
    "fullPage": false
  }
  ```

**Console & JavaScript:**
- `mcp__chrome-devtools__list_console_messages` - Get all console logs
- `mcp__chrome-devtools__get_console_message` - Get specific console message
- `mcp__chrome-devtools__execute_javascript` - Run JavaScript on page

**Accessibility:**
- `mcp__chrome-devtools__snapshot_accessibility_tree` - Generate a11y tree snapshot

## Testing Workflow

### Standard UI Testing Flow

**1. Start Development Server**
```bash
# Start local dev server first (e.g., npm run dev)
# Wait for server to be ready before navigating
```

**2. Navigate to Page**
```json
{
  "tool": "mcp__chrome-devtools__navigate_page",
  "args": {
    "url": "http://localhost:3000/feature"
  }
}
```

**3. Take Initial Screenshot**
```json
{
  "tool": "mcp__chrome-devtools__take_screenshot",
  "args": {
    "filePath": "/tmp/before.jpg",
    "format": "jpeg",
    "quality": 70
  }
}
```

**4. Interact with UI**
```json
// Fill form
{
  "tool": "mcp__chrome-devtools__fill",
  "args": {"uid": "email_input", "value": "test@example.com"}
}

// Click button
{
  "tool": "mcp__chrome-devtools__click",
  "args": {"uid": "submit_button"}
}

// Wait for result
{
  "tool": "mcp__chrome-devtools__wait_for",
  "args": {"uid": "success_message", "timeout": 3000}
}
```

**5. Verify Result**
```json
{
  "tool": "mcp__chrome-devtools__take_screenshot",
  "args": {
    "filePath": "/tmp/after.jpg",
    "format": "jpeg",
    "quality": 70
  }
}
```

**6. Check Console**
```json
{
  "tool": "mcp__chrome-devtools__list_console_messages"
}
```

**7. Review Screenshots**
Use `Read` tool to view screenshots and verify UI changes.

## Critical Best Practices

### Screenshots

**✅ ALWAYS DO:**
- Use `filePath` parameter to save to disk
- Use `"format": "jpeg"` or `"webp"` (NOT PNG!)
- Set `quality: 60-80` for balance
- Use `fullPage: false` for viewport only
- Read screenshot with Read tool after capture

**❌ NEVER DO:**
- Don't omit `filePath` (causes buffer overflow!)
- Don't use PNG format (too large, >5MB)
- Don't use `quality: 100` (unnecessary size)
- Don't capture full page if not needed

**Example:**
```json
{
  "filePath": "/tmp/test_page.jpg",
  "format": "jpeg",
  "quality": 70,
  "fullPage": false
}
```

### Element Selection

**Finding Elements:**
1. Navigate to page first
2. Page snapshot shows element UIDs
3. Use UIDs in `click`, `fill`, `wait_for` calls

**Example:**
```
Page snapshot shows: <button uid="submit_123">Submit</button>
Use: {"uid": "submit_123"} in click tool
```

### Error Handling

**Check Console for Errors:**
```json
{
  "tool": "mcp__chrome-devtools__list_console_messages"
}
```

Look for:
- JavaScript errors
- Network failures (404, 500)
- React/Vue warnings
- Performance issues

## Common Testing Scenarios

### Scenario 1: Test New Form

```
1. Navigate to form page
2. Screenshot initial state
3. Fill all form fields
4. Click submit
5. Wait for success message
6. Screenshot final state
7. Check console for errors
8. Read both screenshots to verify
```

### Scenario 2: Test Button Click

```
1. Navigate to page
2. Screenshot before
3. Click button
4. Wait for state change (wait_for tool)
5. Screenshot after
6. Compare screenshots
```

### Scenario 3: Test Dark Mode Toggle

```
1. Navigate to page
2. Screenshot light mode
3. Click dark mode toggle
4. Screenshot dark mode
5. Verify visual difference
```

### Scenario 4: Performance Testing

```
1. Navigate to page
2. Start performance trace
3. Perform actions (clicks, form fills)
4. Stop trace
5. Analyze metrics
```

## Task Examples

### Example 1: "Test login form"
```
✅ MUST use Chrome DevTools:
1. npm run dev (start server)
2. navigate_page to http://localhost:3000/login
3. take_screenshot (before.jpg)
4. fill username field
5. fill password field
6. click submit button
7. wait_for success message
8. take_screenshot (after.jpg)
9. list_console_messages (check errors)
10. Read both screenshots to verify UI
```

### Example 2: "Verify button styling"
```
✅ MUST use Chrome DevTools:
1. Start dev server
2. navigate_page to feature page
3. take_screenshot of button
4. Verify colors/size/position in screenshot
5. Check console for CSS warnings
```

### Example 3: "Test responsive layout"
```
✅ MUST use Chrome DevTools:
1. Navigate to page
2. Screenshot desktop view
3. Resize viewport (if supported)
4. Screenshot mobile view
5. Compare layouts
```

## Integration with Testing

### Combined with Unit Tests

```bash
# Run unit tests first
npm test

# Then do UI testing with Chrome DevTools
# (navigate, screenshot, interact, verify)
```

### Documentation

When documenting UI changes:
1. Take before/after screenshots
2. Save to `/tmp/screenshots/`
3. Reference in PR description
4. Include in Freelo comment

## Troubleshooting

### Server Not Running
```
Error: Failed to navigate to http://localhost:3000

Solution:
1. Check dev server is running (npm run dev)
2. Wait for server startup (check logs)
3. Verify port number (3000, 8080, etc.)
```

### Element Not Found
```
Error: Element with uid "button_123" not found

Solution:
1. Navigate to page first
2. Check page snapshot for correct UID
3. Wait for element to load (wait_for)
```

### Screenshot Buffer Overflow
```
Error: Response too large

Solution:
✅ Use filePath parameter!
{
  "filePath": "/tmp/screenshot.jpg",
  "format": "jpeg",
  "quality": 70
}
```

### Console Errors
```
React warnings or errors showing up

Solution:
1. Fix errors in code
2. Re-test
3. Verify console is clean
```

## Notes

- Chrome DevTools MCP server is configured per-project in tasklists.json
- Tools are automatically available when server is enabled
- Always start dev server before testing
- Screenshots are temporary (/tmp/) - copy to workspace if needed
- Claude automatically discovers this skill when relevant to task
