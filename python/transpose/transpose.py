"""Transpose exercise."""
from itertools import zip_longest


def transpose(lines: str) -> str:
    """Transpose given text.

    If input has rows of different lengths, pad to the left with spaces.

    :param lines: text to transpose
    :return: transposed text
    """
    if not lines:
        return ""
    lines = lines.split('\n')
    transposed = [
        ''.join(col).rstrip('\n').replace('\n', ' ')
        for col in zip_longest(*lines, fillvalue='\n')
    ]

    return '\n'.join(transposed)
