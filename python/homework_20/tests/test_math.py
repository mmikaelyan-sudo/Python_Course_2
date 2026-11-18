"""Tests for the add and multiply functions and the Calculator class."""

import pytest


def add(first, second):
    """Return the sum of two numbers.

    Args:
        first: The first number.
        second: The second number.

    Returns:
        The sum of ``first`` and ``second``.
    """
    return first + second


def multiply(first, second):
    """Return the product of two numbers.

    Args:
        first: The first number.
        second: The second number.

    Returns:
        The product of ``first`` and ``second``.
    """
    return first * second


class Calculator:
    """Basic calculator with four arithmetic operations."""

    def add(self, first, second):
        """Return the sum of two numbers.

        Args:
            first: The first number.
            second: The second number.

        Returns:
            The sum of ``first`` and ``second``.
        """
        return first + second

    def subtract(self, first, second):
        """Return the difference of two numbers.

        Args:
            first: The number to subtract from.
            second: The number to subtract.

        Returns:
            The result of ``first - second``.
        """
        return first - second

    def multiply(self, first, second):
        """Return the product of two numbers.

        Args:
            first: The first number.
            second: The second number.

        Returns:
            The product of ``first`` and ``second``.
        """
        return first * second

    def divide(self, dividend, divisor):
        """Return the quotient of two numbers.

        Args:
            dividend: The number to divide.
            divisor: The number to divide by.

        Returns:
            The result of ``dividend / divisor``.

        Raises:
            ZeroDivisionError: If ``divisor`` is zero.
        """
        return dividend / divisor


@pytest.fixture
def calculator():
    """Create a new Calculator for each test.

    Returns:
        A Calculator instance.
    """
    return Calculator()


@pytest.mark.P0
@pytest.mark.parametrize(('first', 'second', 'expected'), [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
])
def test_add(first, second, expected):
    """Check that add returns the sum for different inputs."""
    assert add(first, second) == expected


@pytest.mark.parametrize(('first', 'second', 'expected'), [
    (2, 3, 5),
    (-2, 5, 3),
])
def test_calculator_add(calculator, first, second, expected):
    """Check that Calculator.add returns the sum."""
    assert calculator.add(first, second) == expected


@pytest.mark.parametrize(('first', 'second', 'expected'), [
    (5, 3, 2),
    (3, 5, -2),
    (0, 0, 0),
])
def test_calculator_subtract(calculator, first, second, expected):
    """Check that Calculator.subtract returns the difference."""
    assert calculator.subtract(first, second) == expected


@pytest.mark.parametrize(('first', 'second', 'expected'), [
    (4, 3, 12),
    (4, 0, 0),
    (-2, 3, -6),
])
def test_calculator_multiply(calculator, first, second, expected):
    """Check that Calculator.multiply returns the product."""
    assert calculator.multiply(first, second) == expected


@pytest.mark.parametrize(('dividend', 'divisor', 'expected'), [
    (10, 2, 5),
    (1, 4, 0.25),
    (-9, 3, -3),
])
def test_calculator_divide(calculator, dividend, divisor, expected):
    """Check that Calculator.divide returns the quotient."""
    assert calculator.divide(dividend, divisor) == expected


def test_calculator_divide_by_zero(calculator):
    """Check that dividing by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)


@pytest.mark.P0
@pytest.mark.parametrize(('first', 'second', 'expected'), [
    (6, 7, 42),
    (-3, 3, -9),
    (5, 0, 0),
])
def test_multiplication(first, second, expected):
    """Check that multiply returns the product of two numbers."""
    assert multiply(first, second) == expected
