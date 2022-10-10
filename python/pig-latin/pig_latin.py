"""English to Pig Latin.

Rule 1: If a word begins with a vowel sound, add an "ay" 
sound to the end of the word. Please note that "xr" and 
"yt" at the beginning of a word make vowel sounds (e.g. 
"xray" -> "xrayay", "yttria" -> "yttriaay").
Rule 2: If a word begins with a consonant sound, move it 
to the end of the word and then add an "ay" sound to the 
end of the word. Consonant sounds can be made up of multiple consonants, a.k.a. a consonant cluster (e.g. "chair" -> 
"airchay").
Rule 3: If a word starts with a consonant sound followed 
by "qu", move it to the end of the word, and then add an 
"ay" sound to the end of the word (e.g. "square" -> "aresquay").
Rule 4: If a word contains a "y" after a consonant cluster 
or as the second letter in a two letter word it makes a 
vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
"""
VOWELS = 'aeoiu'


def first_vowel(word: str) -> int | None:
    """Find first vowel in given string.

    :param word: the string to check
    :return: index of the first vowel, or None
    """
    first = None
    for vowel in VOWELS:
        this_first = word.find(vowel)
        if this_first >= 0 and (first is None or first > this_first):
            first = this_first

    return first


def translate(text: str) -> str:
    """Translate given text to Pig Latin.

    :param text: the text to translate
    :return: the translated text
    """
    translated = []
    for word in text.split():
        word_1st_vowel = first_vowel(word)
        word_1st_qu = word.find('qu')
        word_1st_y = word.find('y')
        if word_1st_vowel is 0 or word[:2] in ('xr', 'yt'):  # Rule 1
            translated.append(word + 'ay')
        elif word_1st_qu >= 0:  # Rule 3
            translated.append(word[word_1st_qu + 2:] + word[:word_1st_qu + 2] + 'ay')
        elif word_1st_vowel is not None:  # Rule 2
            translated.append(word[word_1st_vowel:] + word[:word_1st_vowel] + 'ay')
        elif word_1st_y >= 0:
            translated.append('y' + word[word_1st_y + 1:] + word[:word_1st_y] + 'ay')
        else:
            translated.append(word)

    return ' '.join(translated)
