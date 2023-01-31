"""Resistor Color Trio."""
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
METRIC_PREFIX = ['', 'kilo', 'mega', 'giga']


def label(colors: list[str]) -> str:
    """Return resistance, in readable text, according to given colors.

    Expecting 3 colors. Less will raise exception. More will be ignored.

    :param colors: ordered list of colors
    :return: resistance value in readable text
    """
    resistance = int(f"{COLOR_VAL[colors[0]]}{COLOR_VAL[colors[1]]}")
    resistance *= 10 ** COLOR_VAL[colors[2]]
    prefix = 0
    while resistance >= 1000 and resistance % 1000 == 0:
        prefix += 1
        resistance = resistance // 1000

    return f"{resistance} {METRIC_PREFIX[prefix]}ohms"
