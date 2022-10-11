def commands(binary_str: str) -> list:
    """Convert given binary string to handshake commands.

    :param binary_str: the binary string with handshake code
    :return: list of handshake commands
    """
    handshake = {
        4: 'wink',
        3: 'double blink',
        2: 'close your eyes',
        1: 'jump',
    }
    command_list = []
    for i in range(4, 0, -1):
        if binary_str[i] == '1':
            command_list.append(handshake[i])

    return command_list[::-1] if binary_str[0] == '1' else command_list
