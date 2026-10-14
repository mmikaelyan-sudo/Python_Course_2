"""Sum an arbitrary number of numeric arguments."""


def add_all_nums(*args):
    """Return the sum of all numeric arguments.

    Args:
        *args: Numbers to add together.

    Returns:
        The sum of all arguments, or an error message if any
        argument is not a number.
    """
    for item in args:
        if not isinstance(item, (int, float)):
            return f'Error: {item!r} is not a number.'
    return sum(args)


# Test the function with valid and invalid inputs.
print(add_all_nums(1, 2, 3, 4))
print(add_all_nums(1.5, 2.5))
print(add_all_nums(1, 2, 'a', 4))
