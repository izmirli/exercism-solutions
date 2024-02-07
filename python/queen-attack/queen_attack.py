"""Queen Attack."""


class Queen:
    """A queen board pice."""
    
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    @property
    def row(self) -> int:
        """Get row property."""
        return self._row

    @row.setter
    def row(self, coordinate: int):
        """The row coordinate property."""
        if self.is_on_board(coordinate, 'row'):
            self._row = coordinate
    
    @property
    def column(self) -> int:
        """The column coordinate property."""
        return self._col
        
    @column.setter
    def column(self, coordinate: int):
        """Set column property."""
        if self.is_on_board(coordinate, 'column'):
            self._col = coordinate
    
    def is_on_board(self, coordinate: int, name: str) -> bool:
        """Validate coordinate is on board.

        :raises ValueError: if coordinate is negative or too big to be on board.
        :returns: True if given coordinate is on board.
        """
        if coordinate < 0:
            raise ValueError(f"{name} not positive")
        if coordinate > 7:
            raise ValueError(f"{name} not on board")
        return True
    
    def can_attack(self, another_queen) -> bool:
        """Check if queens can attack each other.

        :raises ValueError: if both queens in the same square.
        :returns: True if queens can attack each other, False otherwise.
        """
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        row_delta = abs(self.row - another_queen.row)
        col_delta = abs(self.column - another_queen.column)
        if row_delta == 0 or col_delta == 0 or row_delta == col_delta:
            return True
        return False
