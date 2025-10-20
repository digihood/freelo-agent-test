"""
Comprehensive test suite for the calculator module.

Tests cover normal operations, edge cases, and error handling.
"""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    """Test cases for the add function."""

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test addition of two negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, -20) == -30

    def test_add_mixed_signs(self):
        """Test addition of positive and negative numbers."""
        assert add(-5, 5) == 0
        assert add(10, -5) == 5
        assert add(-10, 5) == -5

    def test_add_with_zero(self):
        """Test addition with zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5

    def test_add_floats(self):
        """Test addition of floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)
        assert add(-1.5, 1.5) == 0.0

    def test_add_mixed_types(self):
        """Test addition of integers and floats."""
        assert add(2, 3.5) == 5.5
        assert add(2.5, 3) == 5.5


class TestSubtract:
    """Test cases for the subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 5) == 5

    def test_subtract_result_negative(self):
        """Test subtraction resulting in negative number."""
        assert subtract(3, 5) == -2
        assert subtract(5, 10) == -5

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-3, -5) == 2
        assert subtract(-5, 3) == -8
        assert subtract(5, -3) == 8

    def test_subtract_with_zero(self):
        """Test subtraction with zero."""
        assert subtract(0, 0) == 0
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5

    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(1.1, 0.1) == pytest.approx(1.0)
        assert subtract(-2.5, -1.5) == -1.0

    def test_subtract_mixed_types(self):
        """Test subtraction of integers and floats."""
        assert subtract(5, 2.5) == 2.5
        assert subtract(5.5, 2) == 3.5


class TestMultiply:
    """Test cases for the multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(2, -3) == -6
        assert multiply(-2, -3) == 6

    def test_multiply_with_zero(self):
        """Test multiplication with zero."""
        assert multiply(0, 0) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(-5, 0) == 0

    def test_multiply_with_one(self):
        """Test multiplication with one (identity)."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5
        assert multiply(-5, 1) == -5

    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        assert multiply(2.5, 2.0) == 5.0
        assert multiply(1.5, 3.0) == 4.5
        assert multiply(-2.5, 2.0) == -5.0

    def test_multiply_mixed_types(self):
        """Test multiplication of integers and floats."""
        assert multiply(2, 2.5) == 5.0
        assert multiply(3.5, 2) == 7.0

    def test_multiply_large_numbers(self):
        """Test multiplication of large numbers."""
        assert multiply(1000, 1000) == 1000000
        assert multiply(999999, 1) == 999999


class TestDivide:
    """Test cases for the divide function."""

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(6, 2) == 3.0
        assert divide(10, 5) == 2.0
        assert divide(9, 3) == 3.0

    def test_divide_with_remainder(self):
        """Test division with remainder (non-integer result)."""
        assert divide(5, 2) == 2.5
        assert divide(7, 4) == 1.75
        assert divide(1, 3) == pytest.approx(0.3333333333)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-6, 2) == -3.0
        assert divide(6, -2) == -3.0
        assert divide(-6, -2) == 3.0

    def test_divide_by_one(self):
        """Test division by one (identity)."""
        assert divide(5, 1) == 5.0
        assert divide(-5, 1) == -5.0
        assert divide(2.5, 1) == 2.5

    def test_divide_zero_by_number(self):
        """Test zero divided by a number."""
        assert divide(0, 5) == 0.0
        assert divide(0, -5) == 0.0
        assert divide(0, 1) == 0.0

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(5, 0)

        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(-5, 0)

        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(0, 0)

    def test_divide_floats(self):
        """Test division of floating point numbers."""
        assert divide(5.0, 2.0) == 2.5
        assert divide(7.5, 2.5) == 3.0
        assert divide(-10.0, 2.0) == -5.0

    def test_divide_mixed_types(self):
        """Test division of integers and floats."""
        assert divide(5, 2.0) == 2.5
        assert divide(5.0, 2) == 2.5

    def test_divide_small_numbers(self):
        """Test division of very small numbers."""
        result = divide(0.1, 0.01)
        assert result == pytest.approx(10.0)

        result = divide(0.001, 0.1)
        assert result == pytest.approx(0.01)


class TestEdgeCases:
    """Additional edge case tests for all functions."""

    def test_very_large_numbers(self):
        """Test operations with very large numbers."""
        large = 10**10
        assert add(large, large) == 2 * large
        assert subtract(large, 1) == large - 1
        assert multiply(large, 2) == 2 * large
        assert divide(large, 2) == large / 2

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        small = 10**-10
        assert add(small, small) == pytest.approx(2 * small)
        assert multiply(small, 2) == pytest.approx(2 * small)
        assert divide(small, 2) == pytest.approx(small / 2)

    def test_precision_with_floats(self):
        """Test floating point precision handling."""
        # Known floating point precision issue
        result = add(0.1, 0.2)
        assert result == pytest.approx(0.3)

        result = subtract(0.3, 0.1)
        assert result == pytest.approx(0.2)
