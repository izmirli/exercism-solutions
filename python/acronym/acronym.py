import re


def abbreviate(words: str) -> str:
    """Convert a phrase to its acronym.

    :param words: the phrase to convert
    :return: the acronym
    """
    norm_words = re.sub(r'[^A-Z ]', '', words.upper().replace('-', ' '))
    return ''.join([word[0] for word in norm_words.split()])
