"""Minesweeper."""


def validate_and_populate_board(minefield: list) -> tuple[list, int]:
    """Check minefield is valid and return list of list representation.

    :param minefield: minefield as list of rows as strings
    :raises ValueError: if given minefield is not valid
    :return: bord as a list of list representation, and row length
    """
    bord = []
    cols = None
    for row in minefield:
        if cols is None:
            cols = len(row)
        else:
            if cols != len(row):
                raise ValueError("The board is invalid with current input.")

        if cols != row.count(' ') + row.count('*'):
            raise ValueError("The board is invalid with current input.")

        bord.append(list(row))

    return bord, cols


def count_adjacent_mines(y_coordinate: int, x_coordinate: int,
                         board: list[list], rows: int, cols: int) -> int | str:
    """Count adjacent mines to given coordinate.

    :param y_coordinate: rows coordinate
    :param x_coordinate: cols coordinate
    :param board: bord as a list of list representation
    :param rows: number of rows in bord
    :param cols: number of cols in bord
    """
    adjacent_mines = 0
    for delta_y, delta_x in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        new_y, new_x = y_coordinate + delta_y, x_coordinate + delta_x
        if not 0 <= new_y < rows or not 0 <= new_x < cols or board[new_y][new_x] != '*':
            continue
        adjacent_mines += 1

    return str(adjacent_mines) if adjacent_mines else ' '


def annotate(minefield: list) -> list:
    """Annotate empty cells with adjacent mines count.

    :param minefield: minefield as list of rows as strings
    :return: the annotated minefield
    """
    board, cols = validate_and_populate_board(minefield)
    rows = len(board)
    for y_pos in range(rows):
        for x_pos in range(len(board[y_pos])):
            if board[y_pos][x_pos] != ' ':
                continue
            board[y_pos][x_pos] = count_adjacent_mines(y_pos, x_pos, board, rows, cols)

    return [''.join(row) for row in board]
