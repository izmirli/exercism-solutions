"""Determine if a word or phrase is an isogram.

An isogram is a word or phrase without a repeating letter.
Spaces and hyphens are allowed to appear multiple times.
"""
import re


def is_isogram(string: str) -> bool:
    """Check if given string is a isogram.

    :param string: the string to check
    :return: True if string is a isogram, Flase otherwise
    """
    letters = re.sub(r'[^a-z]', '', string.casefold())
    return len(letters) == len(set(letters))
