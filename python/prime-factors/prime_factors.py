def factors(value: int) -> list[int]:
    prime_factors = []
    factor = 2
    while value >= factor:
        new_value, remainder = divmod(value, factor)
        if remainder == 0:
            prime_factors.append(factor)
            value = new_value
        else:
            factor += 1
    return prime_factors
