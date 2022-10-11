def square_of_sum(number: int) -> int:
    """Find square of the sum of the first n numbers."""
    return (number * (number + 1) / 2) ** 2
    # return sum([num for num in range(1, number + 1)]) ** 2


def sum_of_squares(number: int) -> int:
    """Find the sum of the squares of the first n numbers."""
    return number * (number + 1) * (2 * number + 1) / 6
    # return sum([num ** 2 for num in range(1, number + 1)])


def difference_of_squares(number):
    """Find diff between square of sum and sum of the squares."""
    return square_of_sum(number) - sum_of_squares(number)
