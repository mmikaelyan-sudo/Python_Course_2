"""Print all prime numbers between 1 and 50 using a for loop."""

SMALLEST_PRIME = 2
RANGE_START = 1
RANGE_END = 50


def is_prime(number):
    """Return whether a positive integer is a prime number.

    Args:
        number: Positive integer to check.

    Returns:
        True if the number is prime, otherwise False.
    """
    if number < SMALLEST_PRIME:
        return False
    for divisor in range(SMALLEST_PRIME, number):
        if number % divisor == 0:
            return False
    return True


# Check every number in the range and print the prime ones.
for candidate in range(RANGE_START, RANGE_END + 1):
    if is_prime(candidate):
        print(candidate)
