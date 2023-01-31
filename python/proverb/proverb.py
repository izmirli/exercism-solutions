"""Proverb."""


def proverb(*inputs: list[str], **kwargs) -> list[str]:
    """Generate rhyme from given input words.

    :param inputs: lists of arbitrary length words
    :param kwargs: should have 'qualifier' key to add its value to rhyme
    :return: list of rhyme liens
    """
    rhyme = []
    for i, word in enumerate(inputs):
        if i + 1 == len(inputs):
            qualifier = f"{kwargs['qualifier']} " if 'qualifier' in kwargs and kwargs['qualifier'] is not None else ''
            rhyme.append(f"And all for the want of a {qualifier}{inputs[0]}.")
        else:
            rhyme.append(f"For want of a {word} the {inputs[i + 1]} was lost.")

    return rhyme
