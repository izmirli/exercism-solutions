"""Rail Fence Cipher."""


def encode(message: str, rails: int) -> str:
    """Encode given message with rail fence cipher.

    :param message: message to encode
    :param rails: number of rails for cipher
    :return: encoded message
    """
    norm_msg = message.replace(' ', '')
    msg_rails = [[] for _ in range(rails)]
    rail, direction = 0, 1
    for char in norm_msg:
        msg_rails[rail % rails].append(char)
        rail += direction
        if not 0 <= rail < rails:
            direction *= -1
            rail += direction * 2

    return ''.join([c for row in msg_rails for c in row])


def decode(encoded_message: str, rails: int) -> str:
    """Decode given message with rail fence cipher.

    :param encoded_message: message to decode
    :param rails: number of rails for cipher
    :return: decoded message
    """
    msg_rails = [['-'] * len(encoded_message) for _ in range(rails)]
    rail, direction = 0, 1
    for i in range(len(encoded_message)):
        msg_rails[rail % rails][i] = '*'
        rail += direction
        if not 0 <= rail < rails:
            direction *= -1
            rail += direction * 2
    rail = 0
    for char in encoded_message:
        while True:
            if msg_rails[rail].count('*'):
                break
            rail += 1
        next_pos = msg_rails[rail].index('*')
        msg_rails[rail][next_pos] = char
    return ''.join([c for col in zip(*msg_rails) for c in col if c != '-'])
