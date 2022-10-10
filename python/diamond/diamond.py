def rows(letter: str) -> list:
    """Retrun letter diamond's rows.

    :paran letter: letter at diamond's widest point
    :return: diamond's rows
    """
    a_ord = ord('A')
    diff = ord(letter) - a_ord
    output = ['A'.center(diff * 2 + 1)]
    for cur_diff in range(1, diff + 1):
        cur_letter = chr(a_ord + cur_diff)
        left = (cur_letter + ' ' * (cur_diff - 1)).rjust(diff)
        right = (' ' * (cur_diff - 1) + cur_letter).ljust(diff)
        output.append(f"{left} {right}")

    return output + output[-2::-1]