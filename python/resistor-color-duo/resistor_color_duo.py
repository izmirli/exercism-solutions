"""Resistors color-coded tools.

Each resistor has a resistance value. Manufacturers print
color-coded bands onto the resistors to denote their
resistance values.

The first 2 bands of a resistor have a simple encoding
scheme: each color maps to a single number. For example,
if they printed a brown band (value 1) followed by a green
band (value 5), it would translate to the number 15.
"""
COLOR_VAL = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def value(colors: list) -> int:
    """Return resistance value according to given colors.

    :param colors: orderd list of colors
    :return: resistance value according to first 2 colors
    """
    return int(f"{COLOR_VAL[colors[0]]}{COLOR_VAL[colors[1]]}")
