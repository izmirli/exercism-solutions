def find_anagrams(word: str, candidates: list) -> list:
    """Find anagrams in candidates for given word.

    :param word: the target word to find anagrams for
    :param candidates: list of candidate words to anagrams
    :return: list of anagrams (can be empty if none found)
    """
    anagrams = []
    normalized = sorted(word.casefold())
    for candidat in candidates:
        if sorted(candidat.casefold()) == normalized and word.casefold() != candidat.casefold():
            anagrams.append(candidat)

    return anagrams
