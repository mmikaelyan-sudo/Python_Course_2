"""Homework 11: lambda functions and comprehensions."""

from functools import reduce

COUNTRY_CODE_LENGTH = 3


def copy_list(numbers):
    """Return a copy of the list using a list comprehension.

    Args:
        numbers: List of numbers to copy.

    Returns:
        A new list with the same items.
    """
    return [number for number in numbers]


def get_even_numbers(numbers):
    """Return only the even numbers using a list comprehension.

    Args:
        numbers: Iterable of integers.

    Returns:
        A list with the even numbers in their original order.
    """
    return [number for number in numbers if number % 2 == 0]


def get_even_numbers_with_filter(numbers):
    """Return only the even numbers using filter() and a lambda.

    Args:
        numbers: Iterable of integers.

    Returns:
        A list with the even numbers in their original order.
    """
    return list(filter(lambda number: number % 2 == 0, numbers))


def sort_by_number(pairs):
    """Sort (name, number) pairs by the number using a lambda.

    Args:
        pairs: List of tuples where the second item is a number.

    Returns:
        A new list of the pairs sorted by the number in ascending order.
    """
    return sorted(pairs, key=lambda pair: pair[1])


def multiply_all(numbers):
    """Multiply all numbers using functools.reduce() and a lambda.

    Args:
        numbers: Iterable of numbers.

    Returns:
        The product of all numbers, or 1 for an empty iterable.
    """
    return reduce(lambda product, number: product * number, numbers, 1)


def flatten(nested):
    """Flatten a list of lists into one list using a list comprehension.

    Args:
        nested: List of lists.

    Returns:
        A single list with all items in their original order.
    """
    return [item for inner in nested for item in inner]


def flip_dict(mapping):
    """Swap keys and values using a dict comprehension.

    If several keys share the same value, the last key wins.

    Args:
        mapping: Dictionary whose values are hashable.

    Returns:
        A new dictionary where every value becomes a key and vice versa.
    """
    return {value: key for key, value in mapping.items()}


def get_non_positive_numbers(numbers):
    """Return only the negative numbers and zero using a list comprehension.

    Args:
        numbers: Iterable of numbers.

    Returns:
        A list with the numbers that are less than or equal to zero.
    """
    return [number for number in numbers if number <= 0]


def build_power_table(max_number, max_power):
    """Build tuples of a number followed by its powers from 0 to max_power.

    Args:
        max_number: Last number of the table (the table starts at 0).
        max_power: Highest power to include.

    Returns:
        A list of tuples ``(n, n**0, n**1, ..., n**max_power)``
        for every ``n`` from 0 to ``max_number``.
    """
    return [
        (number, *(number**power for power in range(max_power + 1)))
        for number in range(max_number + 1)
    ]


def flatten_countries(countries):
    """Flatten nested (country, city) pairs into upper-case lists.

    Args:
        countries: List of lists that hold ``(country, city)`` tuples.

    Returns:
        A list of ``[COUNTRY, CODE, CITY]`` lists, where ``CODE`` is
        the first ``COUNTRY_CODE_LENGTH`` letters of the country.
    """
    return [
        [country.upper(), country[:COUNTRY_CODE_LENGTH].upper(), city.upper()]
        for group in countries
        for country, city in group
    ]


def countries_to_dicts(countries):
    """Convert nested (country, city) pairs into a list of dictionaries.

    Args:
        countries: List of lists that hold ``(country, city)`` tuples.

    Returns:
        A list of ``{"country": COUNTRY, "city": CITY}`` dictionaries
        with upper-case values.
    """
    return [
        {"country": country.upper(), "city": city.upper()}
        for group in countries
        for country, city in group
    ]


def join_full_names(names):
    """Join nested (first, last) name pairs into full-name strings.

    Args:
        names: List of lists that hold ``(first_name, last_name)`` tuples.

    Returns:
        A list of ``"first_name last_name"`` strings.
    """
    return [
        f"{first_name} {last_name}"
        for group in names
        for first_name, last_name in group
    ]


def main():
    """Run every homework task on the example data."""
    original = [1, 2, 3, 4, 5]
    copied = copy_list(original)
    print("Task 1:", copied, "| same object:", copied is original)

    print("Task 2:", get_even_numbers(range(1, 11)))
    print("Task 3:", get_even_numbers_with_filter(range(1, 11)))

    fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
    print("Task 4:", sort_by_number(fruits))

    print("Task 5:", multiply_all([1, 2, 3, 4, 5]))
    print("Task 6:", flatten([[5, 4, 7], [8, 9, 6], [7, 2, 4]]))
    print("Task 7:", flip_dict({"a": 1, "b": 2, "c": 3}))

    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    print("Task 8:", get_non_positive_numbers(numbers))

    print("Task 9:")
    for row in build_power_table(max_number=10, max_power=5):
        print(row)

    countries = [
        [("Finland", "Helsinki")],
        [("Sweden", "Stockholm")],
        [("Norway", "Oslo")],
    ]
    print("Task 10:", flatten_countries(countries))
    print("Task 11:", countries_to_dicts(countries))

    names = [
        [("Asabeneh", "Yetayeh")],
        [("David", "Smith")],
        [("Donald", "Trump")],
        [("Bill", "Gates")],
    ]
    print("Task 12:", join_full_names(names))


if __name__ == "__main__":
    main()
