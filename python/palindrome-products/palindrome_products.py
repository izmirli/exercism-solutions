def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return palindrome_product(min_factor, max_factor, True)


def smallest(min_factor: int, max_factor: int):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return palindrome_product(min_factor, max_factor)


def palindrome_product(min_factor: int, max_factor: int, largest: bool = False):
    """Get min/max palindrome product of given factors range.

    :param min_factor: factor range start.
    :param min_factor: factor range end (inclusive).
    :param largest: if true return the largest product, and not the default smallest
    :return: the palindrome, its factors list 
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    factors = tuple(range(min_factor, max_factor + 1))
    smallest_product, largest_product = min_factor**2, max_factor**2
    product, direction = smallest_product, 1
    if largest:
        product, direction = largest_product, -1

    while smallest_product <= product <= largest_product:
        if is_palindrome(product):
            product_factors = get_product_factors(product, factors)
            if product_factors:
                return product, product_factors
        
        product += direction

    return None, []


def get_product_factors(product: int, factors: tuple):
    """Return list of given product's factors.

    Finds pairs of factors, that make given product
    from given factors list.

    :param product: the product
    :param factors: list of possible factors
    :return: pairs of factors (or empty list if none found)
    """
    product_factors = []
    for factor1 in factors:
        if product % factor1 != 0:
            continue
        factor2 = product // factor1
        if factor2 in factors and tuple(sorted((factor1, factor2))) not in product_factors:
            product_factors.append(tuple(sorted((factor1, factor2))))

    return product_factors


def is_palindrome(number: int) -> bool:
    """Check if given number is a palindrome."""
    return number == int(str(number)[::-1])
