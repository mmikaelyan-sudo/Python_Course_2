"""Return the season for a given month number."""

WINTER_MONTHS = (12, 1, 2)
SPRING_MONTHS = (3, 4, 5)
SUMMER_MONTHS = (6, 7, 8)
AUTUMN_MONTHS = (9, 10, 11)


def check_season(month):
    """Return the season for a given month number.

    Args:
        month: Month number from 1 (January) to 12 (December).

    Returns:
        The season name: 'Winter', 'Spring', 'Summer' or 'Autumn',
        or an error message if the month is out of range.
    """
    if month in WINTER_MONTHS:
        return 'Winter'
    if month in SPRING_MONTHS:
        return 'Spring'
    if month in SUMMER_MONTHS:
        return 'Summer'
    if month in AUTUMN_MONTHS:
        return 'Autumn'
    return 'Invalid month. Please enter a number from 1 to 12.'


# Test the function with one month from each season.
print(check_season(1))
print(check_season(4))
print(check_season(7))
print(check_season(10))
