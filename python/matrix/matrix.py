"""Matrix exercise."""


class Matrix:
    """Matrix access class."""

    def __init__(self, matrix_string: str):
        self.matrix = [[int(num) for num in row.split()] for row in matrix_string.split('\n')]

    def row(self, index: int) -> list:
        """Return row by index."""
        return self.matrix[index - 1]

    def column(self, index: int) -> list:
        """Return column by index."""
        return [row[index - 1] for row in self.matrix]
