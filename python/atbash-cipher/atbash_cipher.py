"""Atbash cipher.

The Atbash cipher is a simple substitution cipher that
relies on transposing all the letters in the alphabet
such that the resulting alphabet is backwards. The first
letter is replaced with the last letter, the second with
the second-last, and so on.

Ciphertext is written out in groups of 5 letters, leaving
numbers unchanged, and punctuation is excluded.
"""
import string

chars = string.ascii_lowercase
chars_reversed = chars[::-1]
ATBASH = {chars[i]: chars_reversed[i] for i in range(len(chars))}


def encode(plain_text: str) -> str:
    """Encode given text with Atbash cipher.

    :param plain_text: the text to encode
    :return: the encoded text
    """
    ciphered = ''
    for char in plain_text.casefold():
        if char in ' ' + string.punctuation:
            continue
        
        if len(ciphered) and len(ciphered.replace(' ', '')) % 5 == 0:
            ciphered += ' '
        ciphered += ATBASH.get(char, char)

    return ciphered


def decode(ciphered_text):
    """Decode given text with Atbash cipher.

    :param plain_text: the text to decode
    :return: the decoded text
    """
    decoded = ''
    for char in ciphered_text:
        if char in ' ':
            continue

        decoded += ATBASH.get(char, char)

    return decoded
