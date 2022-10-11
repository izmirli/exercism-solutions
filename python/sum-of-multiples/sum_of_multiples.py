def sum_of_multiples(limit: int, multiples: list):
    """Sum all unique multiples of number's factors up to the number.

    :param limit: the number (and limit)
    :param multiples: list of unique factors
    """
    multiples_sum = 0
    for num in range(1, limit):
        for multipler in multiples:
            if multipler and num % multipler == 0:
                multiples_sum += num
                break

    return multiples_sum
