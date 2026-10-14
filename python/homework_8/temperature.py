"""Check the temperature and tell whether it is a hot day."""

HOT_THRESHOLD = 27


def describe_temperature(temperature):
    """Return a message telling whether it is a hot day.

    Args:
        temperature: Temperature in degrees Celsius.

    Returns:
        A message based on the temperature.
    """
    if temperature > HOT_THRESHOLD:
        return "It's a hot day."
    return "It's not a hot day."


# Test the function with three values: above, equal to, and below 27.
print(describe_temperature(30))
print(describe_temperature(27))
print(describe_temperature(20))
