"""Spell out a number in English.

Given a number from 0 to 999,999,999,999, spell out that number in English.
Break number up into chunks of thousands,  inserting the appropriate scale
word between those chunks.
12345 should give: twelve thousand three hundred forty-five.
"""
N2W = {
    'SINGLE': {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    },
    'TEENS': {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    },
    'TENS': {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    },
    'CHUNKS': {
        1: "thousand",
        2: "million",
        3: "billion",
    },
}


def say_double_digit(double_digit: int, hundreds: int) -> str:
    """Spell last 2 digits of a 3-digit chunk.

    :param double_digit: last 2-digits number
    :param hundreds: hundreds digit
    :return: the spelling of given last 2 digits
    """
    tens, ones = double_digit // 10, double_digit % 10
    extra_and = ' ' if hundreds else '' # 'and ' if hundreds else ''
    if tens == 0:
        return extra_and + N2W['SINGLE'][ones]

    if tens == 1:
        return extra_and + N2W['TEENS'][double_digit]

    spell_out = extra_and + N2W['TENS'][tens]
    spell_out += f"-{N2W['SINGLE'][ones]}" if ones else ''
    return spell_out


def say_chank(chank: str, chank_num: int) -> str:
    """Spell a 3-digit chunk.

    :param chank: 3-digits string chunk
    :param chank_num: chunk number (3:billion, 2:million, 1:thousand, 0:first)
    :return: the spelling of given 3-digit chunk
    """
    if not chank:
        return ''

    hundreds, double_digit = int(chank[0]), int(chank[1:])
    spell_out = ''
    if hundreds:
        spell_out += f"{N2W['SINGLE'][hundreds]} hundred"

    if double_digit or hundreds == 0:
        spell_out += say_double_digit(double_digit, hundreds)

    if chank_num:
        spell_out += f" {N2W['CHUNKS'][chank_num]}"

    return spell_out


def say(number: int) -> str:
    """Spell given number.

    :param number: the number to spell
    :return: the spelling of given number
    """
    if not 0 <= number < 1_000_000_000_000:
        raise ValueError("input out of range")

    spell_out = ''
    str_num = str(number)
    chanks = [str_num[i:i + 3] for i in range(-12, -5, 3)] + [str_num[-3:]]
    chank_num = 3
    for chank in chanks:
        if chank and (int(chank) != 0 or (spell_out == '' and chank_num == 0)):
            cur_chank_out = say_chank(chank.zfill(3), chank_num)
            if cur_chank_out:
              spell_out += f" {cur_chank_out}" if spell_out else cur_chank_out
        chank_num -= 1

    return spell_out
