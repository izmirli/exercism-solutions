"""Functions to manage a users shopping cart items."""
from typing import Iterable


def add_item(current_cart: dict[str, int], items_to_add: Iterable) -> dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] += 1
    return current_cart


def read_notes(notes: Iterable) -> dict[str, int]:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}
    for item in notes:
        cart.setdefault(item, 0)
        cart[item] += 1
    return cart


def update_recipes(ideas: dict, recipe_updates: Iterable) -> dict:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas |= recipe_updates
    return ideas


def sort_entries(cart: dict[str, int]) -> dict[str, int]:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart: dict[str, int], isle_mapping: dict[str, list]) -> dict[str, list]:
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for item, quantity in reversed(sorted(cart.items())):
        fulfillment_cart[item] = [quantity] + isle_mapping[item]
    return fulfillment_cart


def update_store_inventory(fulfillment_cart: dict[str, list], store_inventory: dict[str, list]) -> dict[str, list]:
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item, info in fulfillment_cart.items():
        store_inventory[item][0] -= fulfillment_cart[item][0]
        if store_inventory[item][0] <= 0:
            store_inventory[item][0] = 'Out of Stock'
    return store_inventory
