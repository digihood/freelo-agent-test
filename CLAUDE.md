# Project: Test Freelo Agent - HTML Pages

## Tech Stack
- HTML5
- CSS3 (Tailwind CSS)
- Vanilla JavaScript (if needed)
- GitHub Pages for deployment

## Git Repository
- URL: https://github.com/digihood/freelo-agent-test
- Branch: main
- Always test HTML locally before committing

## Development Commands
```bash
# View HTML locally
python -m http.server 8000
# or
open index.html
```

## Git Guidelines
- Use conventional commits (feat:, fix:, docs:, style:)
- Write descriptive commit messages
- Always test HTML before pushing
- Include screenshot/preview in PR description

## Code Style
- Use semantic HTML5 tags
- Keep CSS organized (utility-first with Tailwind)
- Add comments for complex sections
- Ensure accessibility (alt texts, ARIA labels)

## Agent Instructions

### Before Starting
1. Read the task description carefully
2. Check existing files in the repository
3. Plan the HTML structure
4. Choose appropriate semantic tags

### During Implementation
1. Write clean, semantic HTML
2. Use Tailwind CSS utility classes
3. Ensure mobile-first responsiveness
4. Add meta tags for SEO
5. Test locally before committing

### Testing Checklist
- [ ] HTML validates (https://validator.w3.org/)
- [ ] Responsive on mobile (320px+)
- [ ] Responsive on tablet (768px+)
- [ ] Responsive on desktop (1024px+)
- [ ] All links work
- [ ] Forms have proper validation
- [ ] No console errors
- [ ] Smooth scroll works
- [ ] Images have alt text

### Git Workflow
1. Make changes in the workspace
2. Test HTML locally
3. Commit with descriptive message
4. Push to main branch

### Common Pitfalls
- Don't forget ``
- Always include viewport meta tag
- Use semantic HTML (header, main, footer, section)
- Test on multiple screen sizes
- Ensure contrast ratio for accessibility