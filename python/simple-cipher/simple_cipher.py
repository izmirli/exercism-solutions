"""Simple Cipher."""
from random import choices, randint
from string import ascii_lowercase


class Cipher:
    """Cipher management."""
    A_ORD = ord('a')

    def __init__(self, key=None):
        self.key = key if key is not None else ''.join(choices(ascii_lowercase, k=randint(100, 111)))
        self.shift = [ord(c) - Cipher.A_ORD for c in self.key]
        self.key_len = len(self.key)

    def code_shift(self, text: str, decode: bool = False) -> str:
        direction = -1 if decode else 1
        return ''.join([
            ascii_lowercase[(direction * self.shift[i % self.key_len] + ord(c) - Cipher.A_ORD) % 26]
            for i, c in enumerate(text)
        ])

    def encode(self, text: str) -> str:
        return self.code_shift(text)

    def decode(self, text: str) -> str:
        return self.code_shift(text, decode=True)
