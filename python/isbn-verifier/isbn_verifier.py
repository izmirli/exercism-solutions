"""Validate ISBN-10.

The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:
(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
"""


def is_valid(isbn: str) -> bool:
    """Check if the given value is a valid ISBN-10 number.

    :param isbn: the value to check
    :return: True if valid ISBN-10 format, Fals otherwise
    """
    norm_isbn = str(isbn).casefold().replace('-', '')
    if len(norm_isbn) != 10 or not norm_isbn[:-1].isdecimal() or norm_isbn[-1] not in '0123456789x':
        return False
    check_character = 10 if norm_isbn[9] == 'x' else int(norm_isbn[9])
    checksum = sum([int(digit) * (10 - i) for i, digit in enumerate(norm_isbn) if i < 9]) + check_character
    return checksum % 11 == 0
    
