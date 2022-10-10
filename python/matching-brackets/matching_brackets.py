CLOSING_BRACKETS = {']': '[', '}': '{', ')': '('}


def is_paired(input_string: str) -> bool:
    """Verify all brackets/braces/parentheses matched and nested correctly.

    :param input_string: string to check
    :return: True if matched and nested correctly, False otherwise
    """
    opend = []
    for char in input_string:
        if char in CLOSING_BRACKETS.values():
            opend.append(char)
        elif char in CLOSING_BRACKETS:
            if not opend or CLOSING_BRACKETS[char] != opend[-1]:
                return False
            opend.pop()

    return False if opend else True
