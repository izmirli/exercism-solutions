"""Functions to automate Conda airlines ticketing system."""
from string import ascii_uppercase as letters
from collections.abc import Generator

SEATS_IN_ROW = 4


def generate_seat_letters(number: int) -> Generator[str]:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D
    """
    seats = tuple(letters[:SEATS_IN_ROW])
    for i in range(number):
        yield seats[i % SEATS_IN_ROW]


def generate_seats(number: int) -> Generator[str]:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B
    """
    row = 1
    for seat in generate_seat_letters(number):
        yield str(row) + seat
        if seat == letters[SEATS_IN_ROW - 1]:
            row += 1 if row != 12 else 2


def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}
    """
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers: list[str], flight_id: str) -> Generator[str]:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.
    """
    for seat in seat_numbers:
        yield f"{seat + flight_id:0<12}"
