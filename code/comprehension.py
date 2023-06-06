# pylint: disable=invalid-name

"""
Practice of comprehension syntax.
"""

import doctest


def list_1(n: int) -> list[int]:
    """Returns a list of consecutive integers from 1 to `n`.

    Args:
        n (int): The upper bound of the list.

    Returns:
        list[int]: A list of consecutive integers from 1 to `n`.

    Examples:
    >>> list_1(1) == \
        [1]
    True

    >>> list_1(3) == \
        [1, 2, 3]
    True

    >>> list_1(5) == \
        [1, 2, 3, 4, 5]
    True
    """

    return [i for i in range(1, n + 1)]


def list_2(n: int) -> list[int]:
    """Creates a list of length `n` filled with zeros.

    Args:
        n (int): The length of the list to create.

    Returns:
        list[int]: A list of length `n` filled with zeros.

    Examples:
    >>> list_2(1) == \
        [0]
    True

    >>> list_2(3) == \
        [0, 0, 0]
    True

    >>> list_2(5) == \
        [0, 0, 0, 0, 0]
    True
    """

    return [0 for i in range(n)]


def list_3(n: int) -> list[str]:
    """Returns a list of strings, alternating between "fizz" and "buzz".

    Args:
        n (int): The number of strings to generate.

    Returns:
        list[str]: A list of strings, alternating between "fizz" and "buzz".

    Examples:
    >>> list_3(1) == \
        ['fizz']
    True

    >>> list_3(3) == \
        ['fizz', 'buzz', 'fizz']
    True

    >>> list_3(4) == \
        ['fizz', 'buzz', 'fizz', 'buzz']
    True
    """

    return ["fizz" if i % 2 == 0 else "buzz" for i in range(n)]


def multi_dimentional_list_1(n: int) -> list[list[int]]:
    """Returns a 2D list of `n` x `n` zeros.

    Args:
        n (int): The size of the 2D list.

    Returns:
        list[list[int]]: A 2D list of `n` x `n` zeros.

    Examples:
    >>> multi_dimentional_list_1(1) == \
        [[0]]
    True

    >>> multi_dimentional_list_1(3) == \
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    True

    >>> multi_dimentional_list_1(5) == \
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    True
    """

    return [[0 for j in range(n)] for i in range(n)]


def multi_dimentional_list_2(n: int) -> list[list[int]]:
    """Returns a 2D list of consecutive integers from 1 to `n`.

    Args:
        n (int): The size of the 2D list.

    Returns:
        list[list[int]]: A 2D list of consecutive integers from 1 to `n`.

    Examples:
    >>> multi_dimentional_list_2(1) == \
        [[1]]
    True

    >>> multi_dimentional_list_2(2) == \
        [[1], [1, 2]]
    True

    >>> multi_dimentional_list_2(5) == \
        [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
    True
    """

    return [[j for j in range(1, i + 1)] for i in range(1, n + 1)]


if __name__ == "__main__":
    doctest.testmod()
