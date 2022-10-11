def steps(number: int) -> int:
    """Count steps for Collatz Conjecture of given number.

    :param number: a positive integer to check
    :return: the number of steps to reach 1
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")

    step = 0
    while True:
        if number == 1:
            return step

        step += 1
        number = number // 2 if number % 2 == 0 else number * 3 + 1
