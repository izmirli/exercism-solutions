"""Nicomachus classification by aliquot sum.

The aliquot sum is defined as the sum of the factors of a number
not including the number itself.
Nicomachus classification:
 - Perfect: aliquot sum = number
 - Abundant: aliquot sum > number
 - Deficient: aliquot sum < number
"""
import math


def get_factors(number: int) -> set:
  "Get factors for given number."
  factors = set()
  for i in range(2, int(math.sqrt(number) + 1)):
      if number % i == 0:
          factors.update([i, number // i])
  return factors


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :raises ValueError: if number is not a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"

    factors_sum = sum([1] + list(get_factors(number)))
    if factors_sum == number:
        return "perfect"
    if factors_sum > number:
        return "abundant"
    return "deficient"
