# freelo-agent-test

## Features

- Automated task processing from Freelo project management system
- Multi-agent orchestration using Claude Agent SDK
- Seamless Git workflow with automatic PR creation

## Usage Examples

### Basic Usage

#### 1. Viewing the Landing Page

Open the `index.html` file in your web browser:

```bash
# Option 1: Direct file opening
open index.html  # macOS
xdg-open index.html  # Linux
start index.html  # Windows

# Option 2: Using a local web server (recommended)
python -m http.server 8000
# Then visit: http://localhost:8000
```

#### 2. Customizing the Landing Page

**Change the brand name:**
```html
<!-- Edit line 232 in index.html -->
<a href="#" class="logo">YourBrand</a>
<!-- Change to your company name -->
<a href="#" class="logo">MyCompany</a>
```

**Update the hero section:**
```html
<!-- Edit lines 251-253 in index.html -->
<h1>Welcome to Modern Solutions</h1>
<p>Transform your business with innovative technology...</p>
<!-- Customize with your message -->
<h1>Your Custom Headline</h1>
<p>Your custom description...</p>
```

**Modify contact information:**
```html
<!-- Edit lines 278-281 in index.html -->
<div class="contact-item">Email: contact@yourbrand.com</div>
<div class="contact-item">Phone: +1 (555) 123-4567</div>
<!-- Update with real contact details -->
```

#### 3. Styling Customization

**Change the color scheme:**
```css
/* Edit the hero gradient (line 84 in index.html) */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
/* Example: Blue to teal */
background: linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%);
```

**Modify button colors:**
```css
/* Edit the CTA button (lines 109-110 in index.html) */
background-color: #fff;
color: #667eea;
/* Example: Green button */
background-color: #10b981;
color: #fff;
```

### Advanced Usage

#### Adding New Sections

To add a new section (e.g., Services or Portfolio):

```html
<!-- Add after the hero section, before footer -->
<section style="padding: 4rem 0; background-color: #f9fafb;">
    <div class="container">
        <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 3rem;">
            Our Services
        </h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
            <!-- Service cards here -->
        </div>
    </div>
</section>
```

#### Responsive Testing

Test the responsive design at different breakpoints:

```bash
# Using browser DevTools
# 1. Open index.html in Chrome/Firefox
# 2. Press F12 to open DevTools
# 3. Click the device toolbar icon (Ctrl+Shift+M)
# 4. Test breakpoints:
#    - Mobile: 375px, 414px
#    - Tablet: 768px, 1024px
#    - Desktop: 1280px, 1920px
```

### Integration Examples

#### Adding Google Analytics

```html
<!-- Add before closing </head> tag -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

#### Adding Contact Form

```html
<!-- Replace the CTA button with a form -->
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST"
      style="max-width: 400px; margin: 0 auto;">
    <input type="email" name="email" placeholder="Your email" required
           style="width: 100%; padding: 1rem; margin-bottom: 1rem; border-radius: 0.5rem; border: 1px solid #ccc;">
    <button type="submit" class="cta-button">Subscribe</button>
</form>
```

### Testing with Automated Tools

```bash
# Install pytest (if not already installed)
pip install pytest

# Run tests
pytest tests/

# Run with verbose output
pytest -v tests/
```

### Deployment Examples

#### GitHub Pages

```bash
# 1. Commit your changes
git add index.html
git commit -m "feat: Update landing page"

# 2. Push to GitHub
git push origin main

# 3. Enable GitHub Pages
# Go to Settings > Pages > Select branch: main > Save
# Your site will be available at: https://username.github.io/freelo-agent-test
```

#### Netlify Drop

```bash
# 1. Create a production build directory
mkdir dist
cp index.html dist/

# 2. Visit https://app.netlify.com/drop
# 3. Drag and drop the 'dist' folder
# 4. Get your live URL instantly
```

#### Vercel

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Deploy
vercel

# 3. Follow the prompts
# Your site will be live in seconds
```
