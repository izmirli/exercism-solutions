"""Yacht game score calculator.

In the game, five dice are rolled and the result can be entered in any of twelve categories. The score of a throw of the dice depends on category chosen.
"""

# Score categories.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

# Score calculator function by category.
cat_function = {}


def numbers(num: int):
    """Calculator function maker for numbers categories.

    :param num: th number for the category (1 for Ones, 2 for Twos, etc.)
    :return: a calculator function for the given number
    """
    def ns(dice: list) -> int:
        return num * dice.count(num)
    return ns


def straight(size: str):
    """Calculator function maker for straight categories.

    :param size: big or little straight.
    :return: a calculator function for the given straight type
    """
    def straight_func(dice: list) -> int:
        start, end, total = (2, 6, 20) if size == 'big' else (1, 5, 15)
        return 30 if dice[0] == start and dice[-1] == end and sum(dice) == total else 0
    return straight_func


def full_house(dice: list) -> int:
    """Calculator function for full house category.
    
    :param dice: list of sorted die rolls
    :return: the score for these dice in full house category
    """
    option1 = dice[0] == dice[1] == dice[2] and dice[3] == dice[4]
    option2 = dice[0] == dice[1] and dice[2] == dice[3] == dice[4]
    return sum(dice) if dice[0] != dice[4] and (option1 or option2) else 0


def four_of_a_kind(dice: list) -> int:
    """Calculator function for four of a kinde category.
    
    :param dice: list of die rolls
    :return: the score for these dice in four of a kinde category
    """
    for num in range(1, 7):
        if dice.count(num) >= 4:
            return num * 4
    return 0


def setup():
    """Setup the functions dict."""
    cat_function[YACHT] = lambda d: 50 if d[0] == d[1] == d[2] == d[3] == d[4] else 0
    for cat in range(1, 7):
        cat_function[cat] = numbers(cat)
    cat_function[FULL_HOUSE] = full_house
    cat_function[FOUR_OF_A_KIND] = four_of_a_kind
    cat_function[LITTLE_STRAIGHT] = straight('little')
    cat_function[BIG_STRAIGHT] = straight('big')
    cat_function[CHOICE] = lambda d: sum(d)
    

def score(dice: list, category: int) -> int:
    """Calculate the score for the given dice in given category.
    
    :param dice: list of die rolls
    :return: the score for these dice in four of a kinde categor
    """
    dice.sort()
    return cat_function[category](dice)


setup()
