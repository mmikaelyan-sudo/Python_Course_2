"""Capitalize the first letter of each word in a sentence."""


def capitalize_words(sentence):
    """Return the sentence with the first letter of each word in caps.

    Args:
        sentence: The sentence to capitalize.

    Returns:
        A new sentence where each word starts with a capital letter.
    """
    words = sentence.split()
    capitalized = map(lambda word: word.capitalize(), words)
    return ' '.join(capitalized)


# Test the function with the given sentence.
print(capitalize_words('hello world, how are you?'))
