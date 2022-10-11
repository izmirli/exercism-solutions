"""Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.
An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)
A scalene triangle has all sides of different lengths.

For a shape to be a triangle at all, all sides have to be of length > 0, and the sum of the lengths of any two sides must be greater than or equal to the length of the third side.
"""

def valid_triangle(sides: list[int]) -> bool:
    """Is a valid triangle.

    :param sides: 3 triangle size lengths
    :return: True is a valid triangle, False otherwise
    """
    side_a, side_b, side_c = sides
    all_sides_valid = side_a > 0 and side_b > 0 and side_c > 0
    sizes_ok = side_a + side_b >= side_c \
               and side_a + side_c >= side_b \
               and side_c + side_b >= side_a
    return all_sides_valid and sizes_ok


def equilateral(sides: list[int]) -> bool:
    """Is an equilateral triangle.

    :param sides: 3 triangle size lengths
    :return: True is an equilateral triangle, False otherwise
    """
    return valid_triangle(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides: list[int]) -> bool:
    """Is an isosceles triangle.

    :param sides: 3 triangle size lengths
    :return: True is an isosceles triangle, False otherwise
    """
    all_sides_valid = sides[0] > 0 and sides[1] > 0 and sides[2] > 0
    eq_0_1 = sides[0] == sides[1]
    eq_0_2 = sides[0] == sides[2]
    eq_1_2 = sides[1] == sides[2]
    return valid_triangle(sides) and (eq_0_1 or eq_0_2 or eq_1_2)


def scalene(sides: list[int]) -> bool:
    """Is a scalene triangle.

    :param sides: 3 triangle size lengths
    :return: True is a scalene triangle, False otherwise
    """
    return valid_triangle(sides) and not equilateral(sides) and not isosceles(sides)
