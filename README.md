# freelo-agent-test

## Features

- Automated task processing from Freelo project management system
- Multi-agent orchestration using Claude Agent SDK
- Seamless Git workflow with automatic PR creation
- **Calculator Module**: Basic arithmetic operations with comprehensive testing

## Calculator Module

A Python calculator module providing basic arithmetic operations with type hints, comprehensive documentation, and full test coverage.

### Installation

No installation required. Simply import the module in your Python code.

### Usage

```python
from calculator import add, subtract, multiply, divide

# Addition
result = add(5, 3)
print(result)  # Output: 8

# Subtraction
result = subtract(10, 4)
print(result)  # Output: 6

# Multiplication
result = multiply(6, 7)
print(result)  # Output: 42

# Division
result = divide(15, 3)
print(result)  # Output: 5.0

# Division with error handling
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: Error: Cannot divide by zero
```

### Features

- **Type hints**: All functions include type hints for better IDE support and code clarity
- **Docstrings**: Comprehensive documentation for each function with examples
- **Error handling**: Division by zero raises a clear `ZeroDivisionError`
- **Supports multiple numeric types**: Works with integers and floats
- **Edge case handling**: Tested with negative numbers, zero, very large/small numbers

### API Reference

#### `add(a: Number, b: Number) -> Number`
Returns the sum of two numbers.

#### `subtract(a: Number, b: Number) -> Number`
Returns the difference between two numbers (a - b).

#### `multiply(a: Number, b: Number) -> Number`
Returns the product of two numbers.

#### `divide(a: Number, b: Number) -> float`
Returns the quotient of two numbers (a / b). Raises `ZeroDivisionError` if b is zero.

### Running Tests

The project includes comprehensive tests using pytest:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=calculator --cov-report=term-missing

# Run specific test class
pytest tests/test_calculator.py::TestAdd

# Run specific test
pytest tests/test_calculator.py::TestDivide::test_divide_by_zero_raises_error
```

### Test Coverage

The test suite includes:
- ✅ Basic operations with positive numbers
- ✅ Operations with negative numbers
- ✅ Operations with zero
- ✅ Floating point arithmetic
- ✅ Mixed type operations (int and float)
- ✅ Edge cases (very large/small numbers)
- ✅ Error handling (division by zero)
- ✅ Floating point precision handling

### Examples

```python
from calculator import add, subtract, multiply, divide

# Working with integers
print(add(10, 20))           # 30
print(subtract(50, 30))      # 20
print(multiply(4, 5))        # 20
print(divide(100, 4))        # 25.0

# Working with floats
print(add(1.5, 2.5))         # 4.0
print(subtract(5.5, 2.3))    # 3.2
print(multiply(2.5, 4.0))    # 10.0
print(divide(7.5, 2.5))      # 3.0

# Working with negative numbers
print(add(-5, 3))            # -2
print(subtract(-10, -5))     # -5
print(multiply(-3, 4))       # -12
print(divide(-20, 4))        # -5.0

# Mixed operations
print(add(10, 2.5))          # 12.5
print(multiply(3, 2.5))      # 7.5
```
