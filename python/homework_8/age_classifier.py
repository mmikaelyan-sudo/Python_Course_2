"""Classify a person's age into a life-stage category."""

INFANT_MAX_AGE = 2
CHILD_MAX_AGE = 12
TEENAGER_MAX_AGE = 19
ADULT_MAX_AGE = 64


def classify_age(age):
    """Return the life-stage category for an age in years.

    Args:
        age: Age in whole years (0 or greater).

    Returns:
        The category name as a string.
    """
    if age <= INFANT_MAX_AGE:
        return 'Infant'
    if age <= CHILD_MAX_AGE:
        return 'Child'
    if age <= TEENAGER_MAX_AGE:
        return 'Teenager'
    if age <= ADULT_MAX_AGE:
        return 'Adult'
    return 'Senior'


age = int(input('Enter your age: '))
print(classify_age(age))
