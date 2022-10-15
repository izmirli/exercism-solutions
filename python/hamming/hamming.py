def distance(strand_a: str, strand_b: str) -> int:
    """Calculate the Hamming Distance between two DNA strands.

    :param strand_a: 1st DNA strand.
    :param strand_b: 2nd DNA strand.
    :raises ValueError: if strands have different length
    :return: the Hamming Distance
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    diff = filter(lambda s: s[0] != s[1], zip(strand_a, strand_b))
    return len(list(diff))
