"""Dominoes exercise."""


def get_valid_chain(
        in_chain: list[tuple[int, int]], dominoes_left: list[tuple[int, int]]
) -> list[tuple[int, int]] | None:
    """Get dominoes chain from current chain and dominoes pieces left.

    :param in_chain: chain so far
    :param dominoes_left: dominoes left to chain
    :return: the full chain if possible, or None
    """
    if not dominoes_left:
        return in_chain if in_chain[0][0] == in_chain[-1][1] else None
    for domino in dominoes_left:
        if in_chain and in_chain[-1][1] not in domino:
            continue
        dominoes_left_after_this = dominoes_left.copy()
        dominoes_left_after_this.pop(dominoes_left_after_this.index(domino))
        if not in_chain:
            for domino_to_add in (domino, (domino[1], domino[0])):
                res = get_valid_chain([domino_to_add], dominoes_left_after_this)
                if res is not None:
                    return res
        else:
            if domino[1] == in_chain[-1][1]:
                domino = (domino[1], domino[0])
            res = get_valid_chain(in_chain + [domino], dominoes_left_after_this)
            if res is not None:
                return res

    return None


def can_chain(dominoes: list[tuple[int, int]]) -> list[tuple[int, int]] | None:
    """Check if a valid chain can be made form given dominoes."""
    if not dominoes:
        return []
    return get_valid_chain([], dominoes)
