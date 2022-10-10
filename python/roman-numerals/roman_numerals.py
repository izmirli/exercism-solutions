VALUES = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}


def roman(number: int) -> str:
    """Convert from decimal numbers to Roman Numerals.

    :param number: decimal number to convert
    :return: roman Numeral
    """
    output = ''
    for val in sorted(VALUES.keys(), reverse=True):
        times = number // val
        if times:
            output += VALUES[val] * times
            number = number - val*times
        sub_val = val // 5 if str(val)[0] == '5' else val // 10
        if number >= val - sub_val:
            output += VALUES[sub_val] + VALUES[val]
            number = number - (val - sub_val)

    return output
