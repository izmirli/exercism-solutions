"""Clock exercise."""
from typing import Literal, TypeVar

T = TypeVar('T', bound='Clock')  # Bound to the Clock class


class Clock:
    """A 24-hour clock that handles times without dates."""

    def __init__(self, hour: int, minute: int) -> None:
        hours_to_add, self.minute = divmod(minute, 60)
        self.hour = (hour + hours_to_add) % 24

    def __repr__(self) -> str:
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self) -> str:
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other: T) -> bool:
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes: int) -> T:
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int) -> T:
        return Clock(self.hour, self.minute - minutes)
