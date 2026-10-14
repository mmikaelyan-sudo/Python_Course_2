"""Calculate the factorial of a number using a functional approach."""

from functools import reduce


def factorial(number):
    """Return the factorial of a non-negative integer.

    Args:
        number: A non-negative integer.

    Returns:
        The factorial of the number (1 for 0).
    """
    return reduce(lambda result, item: result * item,
                  range(1, number + 1), 1)


# Test the function with several numbers.
print(factorial(0))
print(factorial(1))
print(factorial(5))
