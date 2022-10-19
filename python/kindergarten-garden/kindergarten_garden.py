"""Kindergarten Garden."""
KIDS = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
        'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry')


class Garden:
    """Kindergarten Garden Manager."""

    PLANTS = {plant[0]: plant for plant in ('Grass', 'Clover', 'Radishes', 'Violets')}

    def __init__(self, diagram: str, students: list = KIDS):
        self.students = sorted(students)
        self.cups = diagram

    @property
    def cups(self):
        """Cups matrix getter."""
        return self._cups

    @cups.setter
    def cups(self, diagram: str):
        """Cups matrix setter.

        :param diagram: plans initials string, separated to 2 rows by new line
        :return: None
        """
        if not set(Garden.PLANTS).issuperset(set(diagram.replace('\n', ''))):
            raise ValueError('Diagram has invalid plants or format.')
        self._cups = [list(row) for row in diagram.splitlines()]

    def plants(self, kid: str) -> list:
        """Return list of plant names belonging to given kid.

        :param kid: name of the kid
        :return: list of plant names.
        """
        kid_i = self.students.index(kid) * 2
        kid_cups = [self.cups[row][col] for row in (0, 1) for col in (kid_i, kid_i + 1)]
        return [self.PLANTS[plant] for plant in kid_cups]
