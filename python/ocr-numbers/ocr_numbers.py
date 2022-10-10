"""Ocr Numbers exercise."""

DIGIT = {
    (" _ ", "| |", "|_|"): "0",
    ("   ", "  |", "  |"): "1",
    (" _ ", " _|", "|_ "): "2",
    (" _ ", " _|", " _|"): "3",
    ("   ", "|_|", "  |"): "4",
    (" _ ", "|_ ", " _|"): "5",
    (" _ ", "|_ ", "|_|"): "6",
    (" _ ", "  |", "  |"): "7",
    (" _ ", "|_|", "|_|"): "8",
    (" _ ", "|_|", " _|"): "9",
}


def convert(input_grid: list) -> str:
    """Return represented numbers.

    Use "?" if digit is garbled.
    Use "," to represent lines separation.

    :param input_grid: display grid as list of lists
    :raises ValueError: if numbers of rows or columns does not conform to 3x4
    :return: a string with converted number
    """
    if len(input_grid) % 4:
        raise ValueError("Number of input lines is not a multiple of four")
    try:
        transpose = list(zip(*input_grid, strict=True))
    except ValueError as exc:
        if str(exc) == "zip() argument 2 is longer than argument 1":
            raise ValueError("Number of input columns is not a multiple of three") from exc
        raise exc
    if len(transpose) % 3:
        raise ValueError("Number of input columns is not a multiple of three")

    lines = [input_grid[i:i + 4] for i in range(0, len(input_grid), 4)]
    numbers = []
    for line in lines:
        digits = []
        for i in range(0, len(line[0]), 3):
            digits.append([row[i:i + 3] for row in line[:-1]])

        numbers.append(digits)

    return ','.join([
        ''.join([DIGIT.get(tuple(digit), "?") for digit in line])
        for line in numbers
    ])


if __name__ == '__main__':
    print(convert([" _ ", "| |", "|_|", "   "]))
