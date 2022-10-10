def rebase(input_base: int, digits: list, output_base: int) -> list:
    """Convert a number from one base to other base.

    :param input_base: base of given number
    :param digits: digits list of given number
    :param output_base: base to convert to
    :return: digits list of converted number
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if len([n for n in digits if not 0 <= n < input_base]):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    value = sum(d * input_base**i for i, d in enumerate(digits[::-1]))
    rebased = []
    while value >= output_base:
        rebased.insert(0, value % output_base)
        value = value // output_base

    return [value] + rebased
