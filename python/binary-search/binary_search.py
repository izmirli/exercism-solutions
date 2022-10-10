def find(search_list: list, value: int) -> int:
    """Bnary search for numeric value in a sorted list."""
    limit = {'bottem': 0, 'top': len(search_list) - 1}
    while limit['bottem'] <= limit['top']:
        mid = limit['bottem'] + ((limit['top'] - limit['bottem']) // 2)
        if search_list[mid] == value:
            return mid
        if search_list[mid] > value:
            limit['top'] = mid - 1
        else:
            limit['bottem'] = mid + 1

    raise ValueError("value not in array")
