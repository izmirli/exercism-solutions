"""Flatten list.

accepts an arbitrarily-deep nested list and returns 
a flattened structure without any nil/null values.
"""

def flatten(iterable: list) -> list:
    """Return a single flattened list.

    :param iterable: an arbitrarily-deep nested list
    :return: flattened list without any null values
    """
    flatten_list = []
    for item in iterable:
        if not item and item != 0:
            continue

        if isinstance(item, list):
            flatten_list.extend(flatten(item))
            continue

        flatten_list.append(item)

    return flatten_list
