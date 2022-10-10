def append(list1, list2):
    """Add all items in the second list to the end of the first list."""
    list1 += list2
    return list1


def concat(lists):
    """Combine all items in all lists into one flattened list."""
    combined = []
    for item in lists:
        if isinstance(item, list):
            combined += item
        else:
            combined.append(item)
    return combined


def filter(function, list1):
    """Return list of items for which function(item) is True."""
    filterd = []
    for item in list1:
        if function(item):
            filterd.append(item)
    return filterd


def length(list1):
    """Return the total number of items within list."""
    return len(list1)


def map(function, list1):
    """Return list of results of applying function(item) on all items."""
    maped = []
    for item in list1:
        maped.append(function(item))
    return maped


def foldl(function, list1, initial):
    """Fold item into the accumulator from the left using function."""
    for item in list1:
        initial = function(initial, item)
    return initial


def foldr(function, list1, initial):
    """Fold item into the accumulator from the right using function."""
    for item in list1[::-1]:
        initial = function(item, initial)
    return initial


def reverse(list1):
    """Return list with original items, but in reversed order."""
    return list1[::-1]
