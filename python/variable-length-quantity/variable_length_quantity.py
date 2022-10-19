"""Variable Length Quantity.

Implement VLQ encoding/decoding.
Only the first 7 bits of each byte is significant (right-justified). To
indicate which is the last byte of the series, you leave bit #7 clear.
In all of the preceding bytes, you set bit #7.
For this exercise we will restrict ourselves to only numbers that fit in
a 32-bit unsigned integer.
"""


def encode(numbers: list) -> list:
    """Encode given numbers using VLQ.

    :param numbers: list of numbers (up to 32-bit unsigned integer)
    :return: octets that are the VLQ encode value
    """
    encoded = []
    for num in numbers:
        bin_num = bin(num)[2:]
        if len(bin_num) % 7:
            bin_num = bin_num.rjust(len(bin_num) + (7 - len(bin_num) % 7), '0')
        octets = [bin_num[i:i + 7] for i in range(0, len(bin_num), 7)]
        while octets:
            octet = octets.pop(0)
            octet = ('1' if octets else '0') + octet
            encoded.append(int(octet, 2))

    return encoded


def decode(bytes_: list) -> list:
    """Decode given VLQ encoded numbers.

    :param bytes_: numbers that are octets of vale to decode
    :raises ValueError: if one of the octets is invalid sequence
    :return: decoded numbers
    """
    decoded = []
    reconstructed = ''
    for i, octet in enumerate(bytes_):
        if i + 1 == len(bytes_) and octet > 0x7F or octet > 0xFF:
            raise ValueError("incomplete sequence")
        bin_num = bin(octet)[2:].rjust(8, '0')
        last = bin_num[0] == '0'
        reconstructed += bin_num[1:]
        if last:
            decoded.append(int(reconstructed, 2))
            reconstructed = ''

    return decoded
