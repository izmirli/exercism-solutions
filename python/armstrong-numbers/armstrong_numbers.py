"""Check Armstrong numbers.

An Armstrong number is a number that is the sum of its own
digits each raised to the power of the number of digits.
"""

def is_armstrong_number(number: int) -> bool:
    """Return whether an Armstrong number."""
    num_of_digits = len(str(number))
    total = 0
    for digit in str(number):
        total += int(digit) ** num_of_digits

    return total == number
