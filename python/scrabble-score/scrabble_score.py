"""Scrabble Score."""
VALUES = {
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10,
}


def score(word: str) -> int:
    """Compute the Scrabble score for given word."""
    return sum(letter_value
               for letter in word.upper()
               for letter_group, letter_value in VALUES.items()
               if letter in letter_group)
