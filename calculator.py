"""
Calculator module providing basic arithmetic operations.

This module contains functions for addition, subtraction, multiplication,
and division with proper type hints and error handling.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Add two numbers together.

    Args:
        a: The first number to add
        b: The second number to add

    Returns:
        The sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(2.5, 1.5)
        4.0
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract the second number from the first number.

    Args:
        a: The number to subtract from
        b: The number to subtract

    Returns:
        The difference of a and b

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(3, 5)
        -2
        >>> subtract(10.5, 2.5)
        8.0
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers together.

    Args:
        a: The first number to multiply
        b: The second number to multiply

    Returns:
        The product of a and b

    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(-2, 3)
        -6
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b


def divide(a: Number, b: Number) -> float:
    """
    Divide the first number by the second number.

    Args:
        a: The dividend (number to be divided)
        b: The divisor (number to divide by)

    Returns:
        The quotient of a divided by b as a float

    Raises:
        ZeroDivisionError: If b is zero

    Examples:
        >>> divide(6, 2)
        3.0
        >>> divide(5, 2)
        2.5
        >>> divide(-10, 2)
        -5.0
        >>> divide(1, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Cannot divide by zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
