"""Darts"""
import math


def score(x: float, y: float) -> int:
    """Returns the earned points in a single toss of a Darts game.

    If dart lands:
        outside target: 0 points.
        in outer circle: 1 point.
        in middle circle: 5 points.
        in inner circle: 10 points.

    :param x: the horizontal cartesian coordinate
    :param y: the vertical cartesian coordinate
    :returns: points scored
    """
    radius = math.sqrt( x * x + y * y )
    if radius <= 1:
        return 10
    elif radius <= 5:
        return 5
    elif radius <= 10:
        return 1
    else:
        return 0
