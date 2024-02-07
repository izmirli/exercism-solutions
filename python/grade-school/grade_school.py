"""Grade School."""
from collections import defaultdict


class School:
    """School students managment."""
    
    def __init__(self):
        self.students = defaultdict(list)
        self.added_log = []

    def add_student(self, name: str, grade: int) -> None:
        """Add new student to given grade in school."""
        if self.is_already_added(name):
            self.added_log.append(False)
        else:
            self.students[grade].append(name)
            self.students[grade].sort()
            self.added_log.append(True)

    def roster(self) -> list[str]:
        """Get school's full students roster."""
        students = []
        for grade in sorted(self.students.keys()):
            students += self.students[grade]
        return students

    def grade(self, grade_number: int) -> list[str]:
        """Get given grade students roster."""
        return self.students[grade_number] if grade_number in self.students else []

    def added(self) -> list[bool]:
        """Get add_student result log."""
        return self.added_log

    def is_already_added(self, name: str) -> bool:
        """Check if given name is already in roster."""
        for grade_students in self.students.values():
            if name in grade_students:
                return True
        return False
