"""Lists relations.

Given any two lists A and B, determine if:
 - List A is equal to list B; or
 - List A contains list B (A is a superlist of B); or
 - List A is contained by list B (A is a sublist of B); or
 - None of the above is true, thus lists A and B are unequal
"""
import re

# Possible sublist categories (enumerated constants).
SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 0


def sublist(list_one: list, list_two: list) -> int:
    """Find relation between the given lists.

    :param list_one: the 1st list
    :param list_two: the 2nd list
    :return: the number reprsnting relation between the lists
    """
    if list_one == list_two:
        return EQUAL

    str_l1 = ','.join([str(num) for num in list_one])
    str_l2 = ','.join([str(num) for num in list_two])
    if not str_l2 or re.search(r'(^|,)' + str_l2 + r'(,|$)', str_l1):
        return SUPERLIST

    if not str_l1 or re.search(r'(^|,)' + str_l1 + r'(,|$)', str_l2):
        return SUBLIST

    return UNEQUAL
