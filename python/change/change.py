"""Change."""
from functools import lru_cache

INVALID_COINS_FOR_TARGET_MSG = "can't make target with given coins"


@lru_cache
def get_change(target: int, coins: tuple, shortest: int | None = None) -> list:
    """Fined change as shortest number of coins that sum up to target.

    :param target: the target number to reach
    :param coins: list of coins amounts
    :param shortest: shortest change option quantity so far
    :raises ValueError: if target can not be reached with coins
    :return: change as list of coins that sum up to target
    """
    top_coin, coins_left = coins[0], coins[1:] if len(coins) > 1 else None
    quantity = target // top_coin
    if not target % top_coin:  # no remainder
        return [top_coin] * quantity
    if coins_left is None:
        raise ValueError(INVALID_COINS_FOR_TARGET_MSG)

    options = []
    for times in range(quantity, -1, -1):
        if shortest is not None and times >= shortest:
            continue
        change = [top_coin] * times
        left = target - sum(change)
        new_shortest = shortest - times if shortest is not None else None
        try:
            change += get_change(left, coins_left, new_shortest)
        except ValueError as ex:
            if INVALID_COINS_FOR_TARGET_MSG in str(ex):
                continue

            raise ex

        if target == sum(change) and (new_shortest is None or new_shortest >= len(change)):
            options.append(change)
            shortest = len(change)

    if not options:
        raise ValueError(INVALID_COINS_FOR_TARGET_MSG)

    return sorted(options, key=len)[0]


def find_fewest_coins(coins: list, target: int) -> list:
    """Find the combination with the fewest coins to reach target.

    :param coins: list of coins amounts
    :raises ValueError: if target is negative or can not be reached with coins
    :param target: the target number to reach
    :return: change as sorted list of coins to return
    """
    if target == 0:
        return []
    coins.sort(reverse=True)
    if target < 0:
        raise ValueError("target can't be negative")
    if target < coins[-1]:
        raise ValueError(INVALID_COINS_FOR_TARGET_MSG)

    return sorted(get_change(target, tuple(coins)))


if __name__ == '__main__':
    cases = (
        # ([1, 5, 10, 21, 25], 0),
        ([4, 5], 27),
        # ([1, 5, 10, 25, 100], 25),
        # ([1, 5, 10, 21, 25], 63),
        # ([1, 4, 15, 20, 50], 23),
        # ([1, 2, 5, 10, 20, 50, 100], 999),
    )
    for case in cases:
        print(f"find_fewest_coins{case}:\n\t{find_fewest_coins(*case)}")
