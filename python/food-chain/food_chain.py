"""Food Chain exercise."""

VERSE_INFO = (
    ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
    ("spider", "It wriggled and jiggled and tickled inside her."),
    ("bird", "How absurd to swallow a bird!"),
    ("cat", "Imagine that, to swallow a cat!"),
    ("dog", "What a hog, to swallow a dog!"),
    ("goat", "Just opened her throat and swallowed a goat!"),
    ("cow", "I don't know how she swallowed a cow!"),
    ("horse", "She's dead, of course!"),
)


def get_verse(verse_num: int) -> list[str]:
    """Get one verse according to given verse number."""
    cur_animal, following_line = VERSE_INFO[verse_num]
    verse = [f"I know an old lady who swallowed a {cur_animal}.", following_line]
    if verse_num == 7:
        return verse

    for cur_verse in range(verse_num - 1, -1, -1):
        prev_animal, cur_animal = cur_animal, VERSE_INFO[cur_verse][0]
        extra_spider = ' that wriggled and jiggled and tickled inside her' if cur_verse == 1 else ''
        verse.append(f"She swallowed the {prev_animal} to catch the {cur_animal}{extra_spider}.")
        if cur_verse == 0:
            verse.append(VERSE_INFO[0][1])

    return verse


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite verses of song according to given verse range."""
    song = []
    for verse_num in range(start_verse - 1, end_verse):
        if song:
            song.append("")
        song += get_verse(verse_num)

    return song
