"""Eliud's Eggs."""


def egg_count(display_value: int) -> int:
    return bin(display_value)[2:].count('1')
