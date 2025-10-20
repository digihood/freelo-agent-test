import sys
from pathlib import Path

# Add parent directory to path to import greet module
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from greet import greet


def test_greet_with_name():
    """Test that greet returns the correct greeting message."""
    assert greet('Alice') == 'Hello, Alice!'


def test_greet_with_different_name():
    """Test that greet works with different names."""
    assert greet('Bob') == 'Hello, Bob!'


def test_greet_with_empty_string():
    """Test that greet handles empty string."""
    assert greet('') == 'Hello, !'


def test_greet_with_special_characters():
    """Test that greet handles names with special characters."""
    assert greet('O\'Brien') == "Hello, O'Brien!"
