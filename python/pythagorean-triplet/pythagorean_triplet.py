"""Pythagorean triplets.

A Pythagorean triplet is a set of three natural numbers, {a, b, c},
for which, a² + b² = c² and such that, a < b < c
"""
from math import gcd


def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    """Check if given triplet is a Pythagorean triplet."""
    return a**2 + b**2 == c**2


def triplets_with_sum(number: int) -> list:
    """Find all Pythagorean triplets that suup to given number."""
    triplets = []

    c, m = 0, 2
    while c <= number:
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > number:
                break
            if a + b + c == number:
                triplet = sorted([a, b, c])
                if triplet not in triplets:
                    triplets.append(triplet)

            if gcd(n, m) == 1 and (n % 2 == 0 or m % 2 == 0):
                for k in range(2, number // c):
                    ak = k * a
                    bk = k * b
                    ck = k * c
                    if ak + bk + ck == number:
                        triplet = sorted([ak, bk, ck])
                        if triplet not in triplets:
                            triplets.append(triplet)

        m += 1

    return triplets
