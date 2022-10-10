"""Spiral Matrix Exercise."""


def spiral_matrix(size: int) -> list:
    """Return a square matrix, in given size, of numbers in spiral order.

    :param size: 2D matrix size
    :raise ValueError: if size is not integer >= 0
    :return: matrix
    """
    if not isinstance(size, int) or size < 0:
        raise ValueError(f"Input size should be zero or positive integer - got '{size}'.")
    if size == 0:
        return []
    if size == 1:
        return [[1]]
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    row, col = 0, 0
    direction = 0
    for num in range(1, size * size + 1):
        matrix[row][col] = num
        row += directions[direction % 4][0]
        col += directions[direction % 4][1]
        if not 0 <= row < size or not 0 <= col < size or matrix[row][col] != 0:
            row -= directions[direction % 4][0]
            col -= directions[direction % 4][1]
            direction += 1
            row += directions[direction % 4][0]
            col += directions[direction % 4][1]

    return matrix
