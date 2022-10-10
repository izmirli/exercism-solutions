"""Saddle Points Exercise."""


def saddle_points(matrix: list) -> list:
    """Detect saddle points in a matrix.

    A "saddle point" is:
     - greater than or equal to every element in its row.
     - less than or equal to every element in its column.

    :param matrix: matrix as list of lists of integers
    :return: saddle points as list of dicts with "row": & "column" keys
    """
    if len(matrix) == 0:
        return []
    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("irregular matrix")

    row_len = len(matrix[0])
    cols = [[row[col] for row in matrix] for col in range(row_len)]
    cols_min = [min(col) for col in cols]
    row_max = [max(row) for row in matrix]
    saddles = []
    for row_idx, row in enumerate(matrix):
        for col_idx, cell_val in enumerate(row):
            if cell_val == cols_min[col_idx] and cell_val == row_max[row_idx]:
                saddles.append({"row": row_idx + 1, "column": col_idx + 1})

    return saddles
