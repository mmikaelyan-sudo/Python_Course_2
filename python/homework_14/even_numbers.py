"""Keep only the even numbers in a list using a functional approach."""


def filter_even_numbers(numbers):
    """Return a new list with only the even numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        A new list containing only the even numbers.
    """
    return list(filter(lambda number: number % 2 == 0, numbers))


# Test the function with a list of numbers.
print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))
