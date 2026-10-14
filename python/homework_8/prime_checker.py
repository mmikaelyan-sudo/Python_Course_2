"""Check whether a positive integer is a prime number."""

SMALLEST_PRIME = 2


def is_prime(number):
    """Return whether a positive integer is a prime number.

    Args:
        number: Positive integer to check.

    Returns:
        True if the number is prime, otherwise False.
    """
    if number < SMALLEST_PRIME:
        return False
    divisor = SMALLEST_PRIME
    while divisor < number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


number = int(input('Enter a positive integer: '))
if is_prime(number):
    print(number, 'is a prime number.')
else:
    print(number, 'is not a prime number.')
