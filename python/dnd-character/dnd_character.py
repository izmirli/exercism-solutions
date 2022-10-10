from random import randrange
from math import floor


def modifier(init_val: int) -> int:
    """Get modifier accordong to given value.
    
    Finf modifier by subtracting 10 from given value, divide by 2 and round down
    :param init_val: given value to get the modifier from
    :return: the modifier
    """
    return floor((init_val - 10) / 2)


class Character:
    """A D&D character."""
    
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = modifier(self.constitution) + 10

    @staticmethod
    def ability() -> int:
        """Generate ability score."""
        four_rolls = [randrange(1, 7) for _ in range(4)]
        return sum(four_rolls) - min(four_rolls)
