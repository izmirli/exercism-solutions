"""Simple Cipher."""
from random import choices, randint
from string import ascii_lowercase


class Cipher:
    """Cipher management."""
    A_ORD = ord('a')
    Z_ORD = ord('z')

    def __init__(self, key=None):
        self.key = key if key is not None else ''.join(choices(ascii_lowercase, k=randint(100, 111)))

    def code_shift(self, text: str, decode: bool = False) -> str:
        result = ''
        for i, char in enumerate(text):
            shift = ord(self.key[i % len(self.key)]) - self.A_ORD
            if decode:
                shift *= -1
            new_ord = ord(char) + shift
            if new_ord > self.Z_ORD:
                new_ord = self.A_ORD + new_ord - self.Z_ORD - 1
            if new_ord < self.A_ORD:
                new_ord = self.Z_ORD - (self.A_ORD - new_ord + 1)
            result += chr(new_ord)
            print(f"{i=}, {char=}, {ord(char)=}, {shift=}, {new_ord=}, {result=}")
            print(f"\t{self.key[i % len(self.key)]=}, {ord(self.key[i % len(self.key)])=}")

        return result

    def encode(self, text: str) -> str:
        return self.code_shift(text)

    def decode(self, text: str) -> str:
        return self.code_shift(text, decode=True)

# abcdefghijklmnopqrstuvwxyz
#    abcdefghijklmnopqrstuvwxyz
