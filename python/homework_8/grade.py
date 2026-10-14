"""Convert a numerical score into a letter grade."""

A_MIN_SCORE = 90
B_MIN_SCORE = 80
C_MIN_SCORE = 70
D_MIN_SCORE = 60


def letter_grade(score):
    """Return the letter grade for a numerical score.

    Args:
        score: Numerical score, expected from 0 to 100.

    Returns:
        The letter grade as a single character ('A' to 'F').
    """
    if score >= A_MIN_SCORE:
        return 'A'
    if score >= B_MIN_SCORE:
        return 'B'
    if score >= C_MIN_SCORE:
        return 'C'
    if score >= D_MIN_SCORE:
        return 'D'
    return 'F'


# Test the function with one score from each grade band.
print('Score 95:', letter_grade(95))
print('Score 85:', letter_grade(85))
print('Score 72:', letter_grade(72))
print('Score 65:', letter_grade(65))
print('Score 40:', letter_grade(40))
