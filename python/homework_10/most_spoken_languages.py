"""Find the most spoken languages in the countries data file."""

import json
from collections import Counter
from pathlib import Path
from pprint import pprint

DATA_FILE = Path(__file__).parent / 'data' / 'countries_data.json'


def most_spoken_languages(filename, count=10):
    """Return the most spoken languages and the number of countries.

    Args:
        filename: Path to the JSON file with the countries data.
        count: How many languages to return.

    Returns:
        A list of (number_of_countries, language) tuples, sorted from
        the most to the least spoken language.

    Raises:
        ValueError: If count is not a positive integer.
    """
    if not isinstance(count, int) or count < 1:
        raise ValueError('Count must be a positive integer.')
    with open(filename, encoding='utf-8') as file:
        countries = json.load(file)
    languages = Counter(
        language
        for country in countries
        for language in country['languages']
    )
    return [(total, language)
            for language, total in languages.most_common(count)]


# Test the function with the example from the task.
pprint(most_spoken_languages(filename=DATA_FILE, count=3), width=20)
