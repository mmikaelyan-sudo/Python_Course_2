"""Tests for the is_palindrome function."""

import pytest


def is_palindrome(text):
    """Check whether a string reads the same in both directions.

    Args:
        text: The string to check.

    Returns:
        True if ``text`` equals its reversed version, otherwise False.
    """
    return text == text[::-1]


@pytest.mark.P0
@pytest.mark.palindrome
def test_palindrome_positive():
    """Check that a palindrome word is recognised."""
    assert is_palindrome('level')


@pytest.mark.palindrome
@pytest.mark.parametrize('text', ['', 'a', 'abba'])
def test_palindrome_edge_cases(text):
    """Check that empty, one-char and even-length palindromes pass."""
    assert is_palindrome(text)


@pytest.mark.P0
@pytest.mark.palindrome
def test_palindrome_negative():
    """Check that a non-palindrome word is rejected."""
    assert not is_palindrome('hello')


@pytest.mark.palindrome
def test_palindrome_case_sensitive():
    """Check that letter case is taken into account."""
    assert not is_palindrome('Level')
