"""Little Sister's Vocabulary"""


def add_prefix_un(word: str) -> str:
    """Add 'un' prefix to given word.

    :param word: str of a root word
    :return:  str of root word with un prefix
    """
    return 'un' + word


def make_word_groups(vocab_words: list) -> str:
    """Return string with prefix and all words using it.

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.
    """
    prefix = vocab_words.pop(0)
    return ' :: '.join([prefix] + [prefix + w for w in vocab_words])


def remove_suffix_ness(word: str) -> str:
    """Returns the base word with `ness` removed.

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.
    """
    if not word.endswith('ness'):
        return word

    return word[:-4] if word[-5] != 'i' else word[:-5] + 'y'


def noun_to_verb(sentence: str, index: int):
    """Return indexed word with 'en' sufix.

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.
    """
    return (sentence.strip('.\n\r').split())[index] + 'en'


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """
    return sentence.strip(' .,\r\n').split()[index] + 'en'
