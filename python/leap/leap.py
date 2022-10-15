"""Leap"""


def leap_year(year: int) -> bool:
    """Is given year a leap year.

    Leap year occures:
    * on every year that is evenly divisible by 4
    * except every year that is evenly divisible by 100
    * unless the year is also evenly divisible by 400

    :paran year: the year toi check
    :return: True if it is a leap yer, False otherwise
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
