"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args: int) -> list[int]:
    """Return a list of wagons.

    :param args: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id: list[int], missing_wagons: list[int]) -> list[int]:
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    w1, w2, locomotive, *part1 = each_wagons_id
    return [locomotive] + missing_wagons + part1 + [w1, w2]


def add_missing_stops(route: dict[str], **kwargs) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param kwargs: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = []
    for stop in kwargs.values():
        route["stops"].append(stop)
    return route


def extend_route_information(route: dict[str], more_route_information: dict[str]) -> dict[str]:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict - extra route information.
    :return: dict - extended route information.
    """
    for k, v in more_route_information.items():
        route[k] = v
    return route


def fix_wagon_depot(wagons_rows: list[list[tuple[int, str]]]) -> list[list[tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [[c1_w1, c1_w2, c1_w3], [c2_w1, c2_w2, c2_w3], [c3_w1, c3_w2, c3_w3]] = wagons_rows
    return [[c1_w1, c2_w1, c3_w1], [c1_w2, c2_w2, c3_w2], [c1_w3, c2_w3, c3_w3]]
