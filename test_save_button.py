#!/usr/bin/env python3
"""
Automated tests for Save button feature
Tests HTML structure, accessibility attributes, and CSS styling
"""

import re
import json
from pathlib import Path


class TestResults:
    def __init__(self):
        self.tests = []
        self.passed = 0
        self.failed = 0
        self.failures = []

    def add_test(self, name, passed, error_msg="", triage_notes=""):
        self.tests.append({
            "name": name,
            "passed": passed,
            "error": error_msg
        })
        if passed:
            self.passed += 1
        else:
            self.failed += 1
            self.failures.append({
                "test_name": name,
                "test_file": "test_save_button.py",
                "failure_type": "assertion_error",
                "error_message": error_msg,
                "stack_trace": "",
                "triage_category": "test_issue",
                "triage_notes": triage_notes
            })


def test_save_button_exists(html_content, results):
    """Test 1: Verify Save button exists in HTML"""
    test_name = "Save button exists in HTML"

    # Look for the Save button with correct class and aria-label
    pattern = r'<a[^>]*class="cta-button-secondary"[^>]*aria-label="Save for later"[^>]*>Save</a>'

    if re.search(pattern, html_content):
        results.add_test(test_name, True)
        print(f"✓ {test_name}")
    else:
        # Try to find partial matches for better error reporting
        if 'Save' in html_content and 'cta-button-secondary' in html_content:
            error = "Save button found but attributes may not match expected pattern"
            triage = "Check that the button has class='cta-button-secondary' and aria-label='Save for later'"
        elif 'Save' in html_content:
            error = "Text 'Save' found but button class is missing or incorrect"
            triage = "Add class='cta-button-secondary' to the Save button"
        else:
            error = "Save button not found in HTML"
            triage = "Add Save button to index.html in the hero section"

        results.add_test(test_name, False, error, triage)
        print(f"✗ {test_name}: {error}")


def test_aria_label_attribute(html_content, results):
    """Test 2: Verify aria-label attribute is present"""
    test_name = "Save button has aria-label='Save for later'"

    if 'aria-label="Save for later"' in html_content:
        results.add_test(test_name, True)
        print(f"✓ {test_name}")
    else:
        error = "aria-label attribute missing or incorrect"
        triage = "Add aria-label='Save for later' attribute to the Save button at index.html:285"
        results.add_test(test_name, False, error, triage)
        print(f"✗ {test_name}: {error}")


def test_button_in_hero_section(html_content, results):
    """Test 3: Verify button is in hero section with correct heading"""
    test_name = "Save button is in hero section with 'Welcome to Modern Solutions' heading"

    # Extract hero section
    hero_match = re.search(r'<section class="hero">(.*?)</section>', html_content, re.DOTALL)

    if hero_match:
        hero_section = hero_match.group(1)
        has_heading = 'Welcome to Modern Solutions' in hero_section
        has_save_button = 'Save' in hero_section and 'cta-button-secondary' in hero_section

        if has_heading and has_save_button:
            results.add_test(test_name, True)
            print(f"✓ {test_name}")
        else:
            error = f"Hero section found but missing {'heading' if not has_heading else 'Save button'}"
            triage = "Ensure Save button is placed within the hero section alongside the heading"
            results.add_test(test_name, False, error, triage)
            print(f"✗ {test_name}: {error}")
    else:
        error = "Hero section not found"
        triage = "Check HTML structure - hero section should exist"
        results.add_test(test_name, False, error, triage)
        print(f"✗ {test_name}: {error}")


def test_button_group_container(html_content, results):
    """Test 4: Verify button-group container exists"""
    test_name = "Save button is in button-group container"

    # Check for button-group div containing both buttons
    pattern = r'<div class="button-group">.*?cta-button.*?cta-button-secondary.*?</div>'

    if re.search(pattern, html_content, re.DOTALL):
        results.add_test(test_name, True)
        print(f"✓ {test_name}")
    else:
        error = "button-group container missing or buttons not properly grouped"
        triage = "Wrap both CTA buttons in a div with class='button-group'"
        results.add_test(test_name, False, error, triage)
        print(f"✗ {test_name}: {error}")


def test_secondary_button_styling(html_content, results):
    """Test 5: Verify secondary button CSS styling exists"""
    test_name = "Secondary button CSS styling is defined"

    required_styles = [
        'background-color: transparent',
        'border: 2px solid #fff',
        'color: #fff'
    ]

    # Extract the cta-button-secondary style block
    style_match = re.search(r'\.cta-button-secondary\s*{([^}]+)}', html_content, re.DOTALL)

    if style_match:
        styles = style_match.group(1)
        missing_styles = [s for s in required_styles if s not in styles]

        if not missing_styles:
            results.add_test(test_name, True)
            print(f"✓ {test_name}")
        else:
            error = f"Missing required styles: {', '.join(missing_styles)}"
            triage = f"Add missing CSS properties to .cta-button-secondary class"
            results.add_test(test_name, False, error, triage)
            print(f"✗ {test_name}: {error}")
    else:
        error = ".cta-button-secondary CSS class not found"
        triage = "Add .cta-button-secondary CSS class definition to the style section"
        results.add_test(test_name, False, error, triage)
        print(f"✗ {test_name}: {error}")


def test_hover_effect_styling(html_content, results):
    """Test 6: Verify hover effect is defined"""
    test_name = "Secondary button hover effect is defined"

    hover_match = re.search(r'\.cta-button-secondary:hover\s*{([^}]+)}', html_content, re.DOTALL)

    if hover_match:
        hover_styles = hover_match.group(1)
        has_bg = 'background-color' in hover_styles
        has_transform = 'transform' in hover_styles

        if has_bg and has_transform:
            results.add_test(test_name, True)
            print(f"✓ {test_name}")
        else:
            missing = []
            if not has_bg: missing.append('background-color')
            if not has_transform: missing.append('transform')
            error = f"Hover effect missing: {', '.join(missing)}"
            triage = "Add background-color and transform properties to :hover state"
            results.add_test(test_name, False, error, triage)
            print(f"✗ {test_name}: {error}")
    else:
        error = "Hover effect not defined for .cta-button-secondary"
        triage = "Add .cta-button-secondary:hover CSS rule with background and transform effects"
        results.add_test(test_name, False, error, triage)
        print(f"✗ {test_name}: {error}")


def test_responsive_button_group(html_content, results):
    """Test 7: Verify button-group has flex-wrap for responsiveness"""
    test_name = "Button group has flex-wrap for mobile responsiveness"

    # Extract button-group styles
    style_match = re.search(r'\.button-group\s*{([^}]+)}', html_content, re.DOTALL)

    if style_match:
        styles = style_match.group(1)
        has_flex_wrap = 'flex-wrap: wrap' in styles
        has_display_flex = 'display: flex' in styles

        if has_flex_wrap and has_display_flex:
            results.add_test(test_name, True)
            print(f"✓ {test_name}")
        else:
            error = "button-group missing flex-wrap or display: flex"
            triage = "Add 'display: flex' and 'flex-wrap: wrap' to .button-group for mobile support"
            results.add_test(test_name, False, error, triage)
            print(f"✗ {test_name}: {error}")
    else:
        error = ".button-group CSS class not found"
        triage = "Add .button-group CSS class with flex and flex-wrap properties"
        results.add_test(test_name, False, error, triage)
        print(f"✗ {test_name}: {error}")


def test_html_doctype(html_content, results):
    """Test 8: Verify HTML5 doctype"""
    test_name = "HTML5 doctype is present"

    if html_content.strip().startswith('<!DOCTYPE html>'):
        results.add_test(test_name, True)
        print(f"✓ {test_name}")
    else:
        error = "HTML5 doctype missing or incorrect"
        triage = "Add <!DOCTYPE html> as the first line of index.html"
        results.add_test(test_name, False, error, triage)
        print(f"✗ {test_name}: {error}")


def test_proper_button_padding(html_content, results):
    """Test 9: Verify button has adequate padding for touch targets"""
    test_name = "Secondary button has adequate padding (1rem 2.5rem)"

    style_match = re.search(r'\.cta-button-secondary\s*{([^}]+)}', html_content, re.DOTALL)

    if style_match:
        styles = style_match.group(1)
        if 'padding: 1rem 2.5rem' in styles:
            results.add_test(test_name, True)
            print(f"✓ {test_name}")
        else:
            error = "Padding not set to 1rem 2.5rem"
            triage = "Set padding: 1rem 2.5rem for adequate touch target size"
            results.add_test(test_name, False, error, triage)
            print(f"✗ {test_name}: {error}")
    else:
        error = ".cta-button-secondary CSS class not found"
        triage = "Add .cta-button-secondary class with proper padding"
        results.add_test(test_name, False, error, triage)
        print(f"✗ {test_name}: {error}")


def main():
    print("=" * 60)
    print("Save Button Feature - Automated Test Suite")
    print("=" * 60)
    print()

    # Read the HTML file
    html_path = Path(__file__).parent / "index.html"

    if not html_path.exists():
        print(f"ERROR: index.html not found at {html_path}")
        return

    html_content = html_path.read_text()

    # Initialize results
    results = TestResults()

    # Run all tests
    print("Running automated tests...\n")
    test_save_button_exists(html_content, results)
    test_aria_label_attribute(html_content, results)
    test_button_in_hero_section(html_content, results)
    test_button_group_container(html_content, results)
    test_secondary_button_styling(html_content, results)
    test_hover_effect_styling(html_content, results)
    test_responsive_button_group(html_content, results)
    test_html_doctype(html_content, results)
    test_proper_button_padding(html_content, results)

    # Print summary
    print()
    print("=" * 60)
    print(f"Test Summary: {results.passed} passed, {results.failed} failed")
    print("=" * 60)

    # Generate JSON report
    report = {
        "total_tests": results.passed + results.failed,
        "passed_tests": results.passed,
        "failed_tests": results.failed,
        "skipped_tests": 0,
        "pass_rate": results.passed / (results.passed + results.failed) if (results.passed + results.failed) > 0 else 0.0,
        "failures": results.failures,
        "coverage": {},
        "overall_coverage": 0.0,
        "flakiness_signals": [],
        "rerun_results": {},
        "test_duration_seconds": 0.0,
        "test_command": "python3 test_save_button.py"
    }

    # Write report to file
    report_path = Path(__file__).parent / "test_report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\nTest report written to: {report_path}")

    return report


if __name__ == "__main__":
    main()
