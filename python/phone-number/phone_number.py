"""Phone Number.

Clean up user-entered NANP phone numbers.
The North American Numbering Plan (NANP) is a telephone numbering system
used by countries in North America. All NANP-countries share the same
international country code: 1.
NANP numbers are ten-digit numbers consisting of a three-digit Numbering
Plan Area code, commonly known as area code, followed by a seven-digit
local number. The first three digits of the local number represent the
exchange code, followed by the unique four-digit number which is the
subscriber number.

The format is usually represented as:
    (NXX)-NXX-XXXX
where N is any digit from 2 through 9 and X is any digit from 0 through 9.
"""
import re
from string import punctuation


class PhoneNumber:
    """NANP Phone number."""

    def __init__(self, number: str):
        self.number = None
        self.area_code = None
        self.set_number(number)

    def set_number(self, number: str):
        """Validate, normalize and set given phone number.

        :param number: the raw phone number
        :raises ValueError: if number doesn't conform to NANP format
        :return: None
        """
        if re.search(r'[a-z]', number, re.I):
            raise ValueError("letters not permitted")
        norm_punctuation = re.sub(r'[\.\-\+\(\)]', '', punctuation)
        if re.search('[' + norm_punctuation + ']', number, re.I):
            raise ValueError("punctuations not permitted")
        # number_parts = re.match(
        #     r'(\S)? *[\.\-\(]?(\S{3})[\.\-\(]? *(\S{3}) *[\-\.]? *(\S{4})',
        #     number.strip()
        # )
        norm_num = re.sub(r'\D', '', number)
        if len(norm_num) < 10:
            raise ValueError("incorrect number of digits")
        if len(norm_num) > 11:
            raise ValueError("more than 11 digits")
        if len(norm_num) == 11 and norm_num[0] != '1':
            raise ValueError("11 digits must start with 1")
        for poz, part in ((-10, 'area code'), (-7, 'exchange code')):
            for val, name in (('0', 'zero'), ('1', 'one')):
                if norm_num[poz] == val:
                    raise ValueError(f"{part} cannot start with {name}")

        self.number = norm_num[-10:]
        self.area_code = self.number[:3]

    def pretty(self) -> str:
        """Return phone number in (NXX)-NXX-XXXX string format."""
        return f"({self.area_code})-{self.number[3:6]}-{self.number[-4:]}"
