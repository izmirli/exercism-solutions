"""Determine if a sentence is a pangram.

A pangram is a sentence using every letter of the alphabet at least once.
The alphabet used consists of letters a to z, inclusive, and is case insensitive.
"""
import string


def is_pangram(sentence: str) -> bool:
    """Check if given sentence is a pangram.

    :param sentence: the sentence to check.
    :return: True if sentence is a pangram, False otherwise.
    """
    sentence = sentence.casefold()
    for letter in string.ascii_lowercase:
        if letter not in sentence:
            return False
    return True
