"""Square each number in a list using a functional approach."""


def square_numbers(numbers):
    """Return a new list with the square of each number.

    Args:
        numbers: A list of numbers.

    Returns:
        A new list containing the square of each number.
    """
    return list(map(lambda number: number ** 2, numbers))


# Test the function with a list of numbers.
print(square_numbers([1, 2, 3, 4, 5]))
