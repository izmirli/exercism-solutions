def transform(legacy_data: dict) -> dict:
    """Transform legacy format score's data to new format.

    :param legacy_data: keys are the score, values are list of letters
    :return: keys are lowercase letters, values is the score
    """
    new_data = {}
    for score in legacy_data:
        new_data.update({letter.casefold(): score for letter in legacy_data[score]})

    return new_data
