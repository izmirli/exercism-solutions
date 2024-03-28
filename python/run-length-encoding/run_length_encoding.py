"""Run-Length Encoding Exercise."""
from re import findall


def decode(string: str) -> str:
    """Decode given RLE string.

    :param string: the coded string
    :return: the decode string
    """
    parts = findall(r'(\d*)([A-Za-z ])', string)
    return ''.join([group[1] * (1 if group[0] == '' else int(group[0])) for group in parts])


def encode(string: str) -> str:
    """Encode given string with Run-Length Encoding.

    :param string: the original string
    :return: the coded string
    """
    parts = findall(r'(([A-Za-z ])\2*)', string)
    return ''.join([(str(len(group[0])) if len(group[0]) > 1 else '') + group[1] for group in parts])
