def square_root(number: int) -> int:
    """Given a natural radicand, return its square root.

    Will work only for natural numbers (positive integers) of both radicand & and its quare root.

    :param number:
    :raises UserWarning: if failed to find the square root of given radicand
    :return: square root of given radicand
    """
    if number in (0, 1):
        return number
    bottom_lim, top_lim = 2, number // 2
    while top_lim >= bottom_lim:
        square = top_lim * top_lim
        if square == number:
            return top_lim
        if square > number:
            top_lim = (top_lim - bottom_lim) // 2 + bottom_lim
        elif square < number:
            midway = (top_lim - bottom_lim) // 2
            top_lim, bottom_lim = top_lim + midway, top_lim

    raise UserWarning(f"Failed to find square_root of: {number}")

