"""Crypto Square.

Given an English text, output the encoded version of that text.
First, the input is normalized: the spaces and punctuation are removed
from the English text and the message is down-cased.
Then, the normalized characters are broken into rows. These rows can be
regarded as forming a rectangle when printed with intervening newlines.
The plaintext should be organized in to a rectangle where c is the
number of columns and r is the number of rows, then for the rectangle
r x c find the smallest possible integer c such that:
    r * c >= length(message)
    and c >= r
    and c - r <= 1
The coded message is obtained by reading down the columns going left to
right. Output the encoded text in chunks that fill perfect rectangles
(r X c), with c chunks of r length, separated by spaces. For phrases that
are n characters short of the perfect rectangle, pad each of the last n
chunks with a single trailing space.
"""
import math
import re
from itertools import zip_longest


def cipher_text(plain_text: str) -> str:
    """Return square code cipher of given text.

    :param plain_text: the text to encod
    :return: square code cipher of given text
    """
    norm_text = re.sub(r'[^a-z0-9]', '', plain_text.strip().casefold())
    if not norm_text:
        return ""
    cols = math.ceil(math.sqrt(len(norm_text)))
    rect = [norm_text[i:i + cols] for i in range(0, len(norm_text), cols)]
    return ' '.join([''.join(c) for c in zip_longest(*rect, fillvalue=' ')])


if __name__ == '__main__':
    cases = (
        ("@1,%!", "1"),
        ("If man was meant to stay on the ground, god would have given us roots.",
         "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "),
        ("   ", ""),
        ("--- ... ---", ""),
    )
    for value, expected in cases:
        print(f"'{cipher_text(value)}'\n'{expected}'")
