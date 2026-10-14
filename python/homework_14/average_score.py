"""Calculate the average score of a list of students."""


def calculate_average_score(scores):
    """Return the average score of the students.

    Args:
        scores: A list of (name, score) tuples.

    Returns:
        The average of all the scores.
    """
    total = sum(map(lambda student: student[1], scores))
    return total / len(scores)


# Test the function with the given list of students.
scores = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
print(calculate_average_score(scores))
