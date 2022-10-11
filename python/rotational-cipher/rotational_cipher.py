"""Rotational cipher.

The Caesar cipher is a simple shift cipher that relies 
on transposing all the letters in the alphabet using an 
integer key between 0 and 26. 
Ciphertext is written out in the same formatting as the 
input including spaces and punctuation.
"""


def rotate(text: str, key: int) -> str:
    """Return ciphertext according to given key rotation.

    :param text: the text to cipher
    :return: the ciphertext
    """
    ord_a, ord_A = ord('a'), ord('A')
    ciphered = ''
    for char in text:
        char_ord = ord(char)
        if ord_a <= char_ord <= ord_a + 26:
            ciphered += chr((char_ord - ord_a + key) % 26 + ord_a)
        elif ord_A <= char_ord <= ord_A + 26:
            ciphered += chr((char_ord - ord_A + key) % 26 + ord_A)
        else:
            ciphered += char

    return ciphered
