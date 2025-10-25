/**
 * Automated tests for Save button functionality
 * Tests HTML structure, accessibility attributes, CSS styling, and responsive behavior
 */

const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

// Read the HTML file
const htmlPath = path.join(__dirname, '../index.html');
const htmlContent = fs.readFileSync(htmlPath, 'utf-8');

// Parse HTML using JSDOM
const dom = new JSDOM(htmlContent);
const document = dom.window.document;

describe('Save Button Feature Tests', () => {
  describe('Button Presence and Structure', () => {
    test('Save button exists in the DOM', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      expect(saveButton).toBeTruthy();
      expect(saveButton.textContent.trim()).toBe('Save');
    });

    test('Save button is an anchor element', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      expect(saveButton.tagName.toLowerCase()).toBe('a');
    });

    test('Save button has correct href attribute', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      expect(saveButton.getAttribute('href')).toBe('#save');
    });
  });

  describe('CSS Classes and Styling', () => {
    test('Save button has cta-button-secondary class', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      expect(saveButton.classList.contains('cta-button-secondary')).toBe(true);
    });

    test('Secondary button CSS class is defined in HTML', () => {
      expect(htmlContent).toContain('.cta-button-secondary');
    });

    test('Secondary button has transparent background style', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*background-color:\s*transparent/);
    });

    test('Secondary button has white border style', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*border:\s*2px\s+solid\s+#fff/);
    });

    test('Secondary button has white text color', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*color:\s*#fff/);
    });

    test('Secondary button has proper padding for touch targets', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*padding:\s*1rem\s+2\.5rem/);
    });

    test('Secondary button has border-radius for rounded corners', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*border-radius:\s*0\.5rem/);
    });

    test('Secondary button has transition effect', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*transition:\s*all\s+0\.3s\s+ease/);
    });

    test('Secondary button has box-shadow', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*box-shadow/);
    });
  });

  describe('Hover Effects', () => {
    test('Hover state is defined for secondary button', () => {
      expect(htmlContent).toContain('.cta-button-secondary:hover');
    });

    test('Hover effect includes background color change', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary:hover\s*{[^}]*background-color/);
    });

    test('Hover effect includes transform for visual feedback', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary:hover\s*{[^}]*transform:\s*translateY\(-2px\)/);
    });

    test('Hover effect includes enhanced box-shadow', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary:hover\s*{[^}]*box-shadow/);
    });

    test('Hover effect has rgba background with transparency', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary:hover\s*{[^}]*background-color:\s*rgba\(255,\s*255,\s*255,\s*0\.1\)/);
    });

    test('Hover effect maintains all transition properties', () => {
      const hoverSection = htmlContent.match(/\.cta-button-secondary:hover\s*{[^}]*}/s);
      expect(hoverSection).toBeTruthy();
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*transition:\s*all\s+0\.3s\s+ease/);
    });

    test('Hover transform translateY has correct negative value', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary:hover\s*{[^}]*transform:\s*translateY\(-2px\)/);
    });

    test('Hover box-shadow is enhanced from base state', () => {
      const baseBoxShadow = htmlContent.match(/\.cta-button-secondary\s*{[^}]*box-shadow:\s*0\s+4px\s+6px/);
      const hoverBoxShadow = htmlContent.match(/\.cta-button-secondary:hover\s*{[^}]*box-shadow:\s*0\s+6px\s+12px/);
      expect(baseBoxShadow).toBeTruthy();
      expect(hoverBoxShadow).toBeTruthy();
    });
  });

  describe('Accessibility', () => {
    test('Save button has aria-label attribute', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      expect(saveButton.hasAttribute('aria-label')).toBe(true);
    });

    test('Save button aria-label is "Save for later"', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      expect(saveButton.getAttribute('aria-label')).toBe('Save for later');
    });

    test('HTML document has proper lang attribute', () => {
      const htmlElement = document.querySelector('html');
      expect(htmlElement.hasAttribute('lang')).toBe(true);
      expect(htmlElement.getAttribute('lang')).toBe('en');
    });

    test('HTML5 doctype is present', () => {
      expect(htmlContent.trim().startsWith('<!DOCTYPE html>')).toBe(true);
    });

    test('Aria-label provides clear context for screen readers', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      const ariaLabel = saveButton.getAttribute('aria-label');
      expect(ariaLabel).toBeTruthy();
      expect(ariaLabel.length).toBeGreaterThan(0);
      expect(ariaLabel).toContain('Save');
    });

    test('Button is keyboard accessible as anchor element', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      expect(saveButton.tagName.toLowerCase()).toBe('a');
      expect(saveButton.hasAttribute('href')).toBe(true);
    });

    test('Button text is concise for screen readers', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      const textContent = saveButton.textContent.trim();
      expect(textContent.length).toBeLessThanOrEqual(10);
    });

    test('Button meets minimum touch target size (44x44px equivalent)', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*padding:\s*1rem\s+2\.5rem/);
    });

    test('Color contrast is maintained with white text on gradient', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*color:\s*#fff/);
      expect(htmlContent).toMatch(/\.hero\s*{[^}]*background:\s*linear-gradient/);
    });
  });

  describe('Responsive Design', () => {
    test('Button-group container exists', () => {
      const buttonGroup = document.querySelector('.button-group');
      expect(buttonGroup).toBeTruthy();
    });

    test('Save button is inside button-group container', () => {
      const buttonGroup = document.querySelector('.button-group');
      const saveButton = buttonGroup.querySelector('.cta-button-secondary');
      expect(saveButton).toBeTruthy();
    });

    test('Button-group has display flex for layout', () => {
      expect(htmlContent).toMatch(/\.button-group\s*{[^}]*display:\s*flex/);
    });

    test('Button-group has flex-wrap for mobile responsiveness', () => {
      expect(htmlContent).toMatch(/\.button-group\s*{[^}]*flex-wrap:\s*wrap/);
    });

    test('Button-group has gap for spacing between buttons', () => {
      expect(htmlContent).toMatch(/\.button-group\s*{[^}]*gap:\s*1rem/);
    });

    test('Button-group centers content', () => {
      expect(htmlContent).toMatch(/\.button-group\s*{[^}]*justify-content:\s*center/);
    });

    test('Button-group has align-items for vertical alignment', () => {
      expect(htmlContent).toMatch(/\.button-group\s*{[^}]*align-items:\s*center/);
    });

    test('Responsive styles exist for mobile devices', () => {
      expect(htmlContent).toContain('@media (max-width: 768px)');
    });

    test('Flex-wrap wrap value allows buttons to stack on small screens', () => {
      const flexWrapMatch = htmlContent.match(/\.button-group\s*{[^}]*flex-wrap:\s*wrap/);
      expect(flexWrapMatch).toBeTruthy();
    });

    test('Button maintains consistent styling across breakpoints', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*padding:\s*1rem\s+2\.5rem/);
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*font-size:\s*1\.125rem/);
    });

    test('Responsive media queries cover tablet breakpoint', () => {
      expect(htmlContent).toContain('@media (max-width: 768px)');
    });

    test('Responsive media queries cover mobile breakpoint', () => {
      expect(htmlContent).toContain('@media (max-width: 480px)');
    });

    test('Gap spacing provides adequate button separation', () => {
      expect(htmlContent).toMatch(/\.button-group\s*{[^}]*gap:\s*1rem/);
    });
  });

  describe('Hero Section Integration', () => {
    test('Save button is in hero section', () => {
      const heroSection = document.querySelector('.hero');
      expect(heroSection).toBeTruthy();
      const saveButton = heroSection.querySelector('.cta-button-secondary');
      expect(saveButton).toBeTruthy();
    });

    test('Hero section contains both primary and secondary CTA buttons', () => {
      const heroSection = document.querySelector('.hero');
      const primaryButton = heroSection.querySelector('.cta-button');
      const secondaryButton = heroSection.querySelector('.cta-button-secondary');
      expect(primaryButton).toBeTruthy();
      expect(secondaryButton).toBeTruthy();
    });

    test('Hero section has correct heading', () => {
      const heroSection = document.querySelector('.hero');
      const heading = heroSection.querySelector('h1');
      expect(heading).toBeTruthy();
      expect(heading.textContent).toBe('Welcome to Modern Solutions');
    });

    test('Hero section has gradient background', () => {
      expect(htmlContent).toMatch(/\.hero\s*{[^}]*background:\s*linear-gradient/);
    });
  });

  describe('Button Order and Layout', () => {
    test('Primary button appears before secondary button in DOM', () => {
      const buttonGroup = document.querySelector('.button-group');
      const buttons = buttonGroup.querySelectorAll('a');
      expect(buttons.length).toBeGreaterThanOrEqual(2);
      expect(buttons[0].classList.contains('cta-button')).toBe(true);
      expect(buttons[1].classList.contains('cta-button-secondary')).toBe(true);
    });

    test('Button group contains exactly 2 buttons', () => {
      const buttonGroup = document.querySelector('.button-group');
      const buttons = buttonGroup.querySelectorAll('a');
      expect(buttons.length).toBe(2);
    });
  });

  describe('Visual Consistency', () => {
    test('Secondary button font-size matches primary button', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*font-size:\s*1\.125rem/);
    });

    test('Secondary button font-weight matches primary button', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*font-weight:\s*600/);
    });

    test('Both buttons use inline-block display', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*display:\s*inline-block/);
    });

    test('Both buttons have text-decoration none', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*text-decoration:\s*none/);
    });
  });

  describe('HTML Validation', () => {
    test('HTML has viewport meta tag for mobile', () => {
      const viewportMeta = document.querySelector('meta[name="viewport"]');
      expect(viewportMeta).toBeTruthy();
      expect(viewportMeta.getAttribute('content')).toContain('width=device-width');
    });

    test('HTML has charset meta tag', () => {
      const charsetMeta = document.querySelector('meta[charset]');
      expect(charsetMeta).toBeTruthy();
      expect(charsetMeta.getAttribute('charset').toLowerCase()).toBe('utf-8');
    });

    test('HTML has title tag', () => {
      const title = document.querySelector('title');
      expect(title).toBeTruthy();
      expect(title.textContent.length).toBeGreaterThan(0);
    });
  });

  describe('Comprehensive Acceptance Criteria Validation', () => {
    test('AC1: Button has correct CSS class (cta-button-secondary)', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      expect(saveButton).toBeTruthy();
      expect(saveButton.classList.contains('cta-button-secondary')).toBe(true);
    });

    test('AC2: Button has aria-label "Save for later"', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      expect(saveButton.getAttribute('aria-label')).toBe('Save for later');
    });

    test('AC3: Button has transparent background style', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*background-color:\s*transparent/);
    });

    test('AC4: Button has white border (2px solid #fff)', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*border:\s*2px\s+solid\s+#fff/);
    });

    test('AC5: Button is positioned within .button-group container', () => {
      const buttonGroup = document.querySelector('.button-group');
      expect(buttonGroup).toBeTruthy();
      const saveButton = buttonGroup.querySelector('.cta-button-secondary');
      expect(saveButton).toBeTruthy();
    });

    test('AC6: Hover effect includes rgba background', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary:hover\s*{[^}]*background-color:\s*rgba\(255,\s*255,\s*255,\s*0\.1\)/);
    });

    test('AC7: Hover effect includes transform translateY(-2px)', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary:hover\s*{[^}]*transform:\s*translateY\(-2px\)/);
    });

    test('AC8: Hover effect includes enhanced box-shadow', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary:hover\s*{[^}]*box-shadow:\s*0\s+6px\s+12px/);
    });

    test('AC9: flex-wrap: wrap enables responsive stacking', () => {
      expect(htmlContent).toMatch(/\.button-group\s*{[^}]*flex-wrap:\s*wrap/);
    });

    test('AC10: All acceptance criteria combined validation', () => {
      const saveButton = document.querySelector('.cta-button-secondary');
      const buttonGroup = document.querySelector('.button-group');

      expect(saveButton).toBeTruthy();
      expect(saveButton.classList.contains('cta-button-secondary')).toBe(true);
      expect(saveButton.getAttribute('aria-label')).toBe('Save for later');
      expect(saveButton.getAttribute('href')).toBe('#save');
      expect(buttonGroup.contains(saveButton)).toBe(true);

      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*background-color:\s*transparent/);
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*border:\s*2px\s+solid\s+#fff/);
      expect(htmlContent).toMatch(/\.cta-button-secondary:hover\s*{[^}]*background-color:\s*rgba/);
      expect(htmlContent).toMatch(/\.cta-button-secondary:hover\s*{[^}]*transform:\s*translateY\(-2px\)/);
      expect(htmlContent).toMatch(/\.button-group\s*{[^}]*flex-wrap:\s*wrap/);
    });
  });

  describe('CSS Specificity and Style Validation', () => {
    test('Secondary button CSS is defined separately from primary', () => {
      const secondaryButtonStyles = htmlContent.match(/\.cta-button-secondary\s*{[^}]+}/s);
      const primaryButtonStyles = htmlContent.match(/\.cta-button\s*{[^}]+}/s);
      expect(secondaryButtonStyles).toBeTruthy();
      expect(primaryButtonStyles).toBeTruthy();
      expect(secondaryButtonStyles[0]).not.toBe(primaryButtonStyles[0]);
    });

    test('Border style is consistently 2px solid white', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*border:\s*2px\s+solid\s+#fff/);
    });

    test('Transparent background uses correct CSS value', () => {
      expect(htmlContent).toMatch(/\.cta-button-secondary\s*{[^}]*background-color:\s*transparent/);
    });

    test('All hover properties are within hover pseudo-class', () => {
      const hoverBlock = htmlContent.match(/\.cta-button-secondary:hover\s*{([^}]*)}/s);
      expect(hoverBlock).toBeTruthy();
      expect(hoverBlock[1]).toContain('background-color');
      expect(hoverBlock[1]).toContain('transform');
      expect(hoverBlock[1]).toContain('box-shadow');
    });
  });
});
