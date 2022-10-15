"""Recite the nursery rhyme 'This is the House that Jack Built'."""
BEGIN = "This is the"
VERSES = (
    ("house that Jack built.", "lay in the"),
    ("malt", "ate the"),
    ("rat", "killed the"),
    ("cat", "worried the"),
    ("dog", "tossed the"),
    ("cow with the crumpled horn", "milked the"),
    ("maiden all forlorn", "kissed the"),
    ("man all tattered and torn", "married the"),
    ("priest all shaven and shorn", "woke the"),
    ("rooster that crowed in the morn", "kept the"),
    ("farmer sowing his corn", "belonged to the"),
    ("horse and the hound and the horn",)
)


def get_verse(verse_num: int) -> str:
    """Recite a single verse.

    A single space, and not new line, will separate between lines.

    :param verse_num: normlise verse number (0 for verse 1, 11 for verse 12)
    :return: the full text of given verse number.
    """
    verse = f"{BEGIN} {VERSES[verse_num][0]} "
    for cur_verse_num in range(verse_num - 1, -1, -1):
        verse += f"that {VERSES[cur_verse_num][1]} {VERSES[cur_verse_num][0]} "
    return verse.rstrip()


def recite(start_verse: int, end_verse: int) -> list:
    """Recite the nursery rhyme verses according to given range.

    :param start_verse: start verses range
    :param end_verse: end verses range
    :return: list with verses
    """
    recite_out = []
    for verse in range(start_verse - 1, end_verse):
        recite_out.append(get_verse(verse))
    return recite_out
