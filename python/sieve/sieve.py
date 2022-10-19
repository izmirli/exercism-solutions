"""Sieve of Eratosthenes.

The Sieve of Eratosthenes is a simple, ancient algorithm for finding
all prime numbers up to any given limit. It does so by iteratively
marking as composite (i.e. not prime) the multiples of each prime,
starting with the multiples of 2. It does not use any division or
remainder operation.
"""


def primes(limit: int) -> list:
    """Return all the primes from 2 up to a given limit."""
    if limit < 2:
        return []
    numbers = set(range(2, limit + 1))
    primes_found = []
    while numbers:
        prime = min(numbers)
        primes_found.append(prime)
        numbers -= {prime * num for num in range(1, limit // prime + 1)}

    return primes_found


def better_primes(limit):
    numbers = set(range(2, limit + 1))
    marked = {m for n in numbers for m in range(2 * n, limit + 1, n)}
    return sorted(numbers - marked)
