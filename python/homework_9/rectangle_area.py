"""Calculate the area of a rectangle."""


def calculate_rectangle_area(length, width):
    """Return the area of a rectangle.

    Args:
        length: Length of the rectangle.
        width: Width of the rectangle.

    Returns:
        The area, calculated as length multiplied by width.
    """
    return length * width


# Test the function with various inputs.
print(calculate_rectangle_area(10, 6))
print(calculate_rectangle_area(5, 5))
print(calculate_rectangle_area(2, 8))
