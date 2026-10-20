"""Find the most populated countries in the countries data file."""

import json
from pathlib import Path
from pprint import pprint

DATA_FILE = Path(__file__).parent / 'data' / 'countries_data.json'


def most_populated_countries(filename, count=10):
    """Return the most populated countries with their population.

    Args:
        filename: Path to the JSON file with the countries data.
        count: How many countries to return.

    Returns:
        A list of {'country': name, 'population': number} dictionaries,
        sorted from the most to the least populated country.

    Raises:
        ValueError: If count is not a positive integer.
    """
    if not isinstance(count, int) or count < 1:
        raise ValueError('Count must be a positive integer.')
    with open(filename, encoding='utf-8') as file:
        countries = json.load(file)
    countries.sort(key=lambda country: country['population'], reverse=True)
    return [{'country': country['name'], 'population': country['population']}
            for country in countries[:count]]


# Test the function with the example from the task.
pprint(most_populated_countries(filename=DATA_FILE, count=3), width=70)
