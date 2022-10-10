"""Diffie-Hellman key exchange.

Use Diffie-Hellman key exchange to share secrets.
Start with prime numbers, pick private keys, generate and
share public keys, and then generate a shared secret key.
"""
import random


def private_key(prime: int) -> int:
    """Pseudo-random pick of a number greater than 1 and less than prime."""
    return random.randint(2, prime - 1)


def public_key(prime: int, other_prime: int, private: int) -> int:
    """Generate public key from private key and 2 prime numbers."""
    return other_prime**private % prime


def secret(prime: int, public: int, private: int) -> int:
    """Calculate shared secret key.

    :param prime: prime number
    :param public: public key of other party
    :param private: self private key
    :return: hared secret key
    """
    return public**private % prime
