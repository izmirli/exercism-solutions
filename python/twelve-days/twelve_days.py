"""Lyrics generator for "The Twelve Days of Christmas"."""
DAYS = [
    {'day': 'first', 'gift': 'and a Partridge in a Pear Tree.'},
    {'day': 'second', 'gift': 'two Turtle Doves'},
    {'day': 'third', 'gift': 'three French Hens'},
    {'day': 'fourth', 'gift': 'four Calling Birds'},
    {'day': 'fifth', 'gift': 'five Gold Rings'},
    {'day': 'sixth', 'gift': 'six Geese-a-Laying'},
    {'day': 'seventh', 'gift': 'seven Swans-a-Swimming'},
    {'day': 'eighth', 'gift': 'eight Maids-a-Milking'},
    {'day': 'ninth', 'gift': 'nine Ladies Dancing'},
    {'day': 'tenth', 'gift': 'ten Lords-a-Leaping'},
    {'day': 'eleventh', 'gift': 'eleven Pipers Piping'},
    {'day': 'twelfth', 'gift': 'twelve Drummers Drumming'},
]


def get_verse(day: int) -> str:
    """Generate a single verse for given day.

    :param day: day number
    :return: verse for given day
    """
    day_index = day - 1
    verse_start = f"On the {DAYS[day_index]['day']} day of Christmas my true love gave to me: "
    gifts = [DAYS[i]['gift'] for i in range(day_index, -1, -1)]
    if len(gifts) == 1:
        gifts[0] = gifts[0][4:]  # remove the "and "
    return verse_start + ', '.join(gifts)


def recite(start_verse: int, end_verse: int) -> list:
    """Generate verses from song for given days range.

    :param start_verse: start days range
    :param end_verse: end days range
    :return: list of verses for given day range
    """
    return [get_verse(d) for d in range(start_verse, end_verse + 1)]
