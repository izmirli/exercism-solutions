import re
from collections import Counter


def count_words(sentence: str) -> dict:
    """Count the occurrences of each word in given sentence.

    Words can be:
     * number composed of one or more ASCII digits.
     * A simple word composed of one or more ASCII letters.
     * A contraction of 2 simple words joined by a single apostrophe.
    
    :param sentence: the phrase to count words in
    :return: dictionery words as keys and the count as values
    """
    norm_sentence = sentence.casefold()  #.replace('_', ' ')
    words = re.findall(r'[a-zA-Z]+(?:\'[a-zA-Z]+)?|\d+', norm_sentence)
    return Counter(words)
