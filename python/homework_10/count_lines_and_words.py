"""Count the number of lines and words in a text."""

from pathlib import Path

SPEECH_FILE = Path(__file__).parent / 'steve_job_speech.txt'


def count_lines_and_words(text):
    """Return the number of lines and words in a text.

    Args:
        text: The text to analyse.

    Returns:
        A tuple (lines, words) with the number of lines and words.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('Text must be a string.')
    return len(text.splitlines()), len(text.split())


# Test the function with the speech file from the task.
with open(SPEECH_FILE, encoding='utf-8') as file:
    print(count_lines_and_words(file.read()))

# Test the function with a multi-line text, one line and an empty text.
print(count_lines_and_words('Hello world\nI am learning Python\nBye'))
print(count_lines_and_words('Just one line'))
print(count_lines_and_words(''))

# Test an invalid input.
try:
    count_lines_and_words(123)
except TypeError as error:
    print(f'TypeError: {error}')
