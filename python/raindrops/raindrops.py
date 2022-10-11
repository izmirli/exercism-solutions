"""Raindrop sounds.

Convert a number into a string that contains raindrop sounds
corresponding to certain potential factors.
"""
RAINDROPS = {3: 'Pling', 5: 'Plang', 7: 'Plong'}


def convert(number: int) -> str:
    """Convert given number to raindrop sounds.

    If has raindrop factors, retrun their concatinated sounds
    string. Otherwise, retrun the number's didgits atring.

    :param number: the number to convert
    :retern: raindrop sounds, or digits of the number
    """
    output = ''
    for factor in RAINDROPS:
        if number % factor == 0:
            output += RAINDROPS[factor]

    if not output:
        output = str(number)

    return output
