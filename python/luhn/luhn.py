"""Luhn exercise."""


class Luhn:
    """Numbers validity according to the Luhn formula."""

    def __init__(self, card_num: str):
        """Initialise normalized number."""
        self.num = card_num.replace(' ', '')

    def valid(self) -> bool:
        """Does number conforms to the Luhn formula."""
        if len(self.num) <= 1 or not self.num.isdecimal():
            return False

        checksum = 0
        for i, digit in enumerate(self.num[::-1]):
            digit = int(digit)
            if i % 2:  # every second digit
                checksum += digit * 2 - 9 if digit * 2 > 9 else digit * 2
            else:
                checksum += digit

        return checksum % 10 == 0
