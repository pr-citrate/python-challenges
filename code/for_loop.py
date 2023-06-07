# pylint: disable=invalid-name

"""
Practice of for loop syntax.
"""
import doctest


def left_down_triangle(n: int) -> str:
    """
    Returns a left-down triangle of stars with a length of `n`.

    Args:
      n (int): The length of the triangle.

    Returns:
      str: A string of stars.

    Examples:
        >>> left_down_triangle(1) == \
        "*"
        True


    """
    result = ""
    for i in range(1, n + 1):
        result += "*" * i
    return result


def right_down_triangle(n: int) -> str:
    """
    Returns a right-down triangle of stars with a length of `n`.

    Args:
      n (int): The length of the triangle.

    Returns:
      str: A string of stars.
    """
    result = ""
    for i in range(1, n + 1):
        result += " " * (n - i) + "*" * i
    return result


def left_up_triangle(n: int) -> str:
    """
    Returns a left-up triangle of stars with a length of `n`.

    Args:
      n (int): The length of the triangle.

    Returns:
      str: A string of stars.
    """
    result = ""
    for i in range(n, 0, -1):
        result += "*" * i + " " * (n - i)
    return result


def right_up_triangle(n: int) -> str:
    """
    Returns a right-up triangle of stars with a length of `n`.

    Args:
      n (int): The length of the triangle.

    Returns:
      str: A string of stars.
    """
    result = ""
    for i in range(n, 0, -1):
        result += " " * (n - i) + "*" * i
    return result


def square(n: int) -> str:
    """
    Returns a square of stars with a length of `n`.

    Args:
      n (int): The length of the square.

    Returns:
      str: A string of stars.
    """
    result = ""
    for _ in range(n):
        result += "*" * n
    return result


def square_border(n: int) -> str:
    """
    Returns a border of square of stars with a length of `n`.

    Args:
      n (int): The length of the square.

    Returns:
      str: A string of stars.
    """
    if n == 1:
        return "*"
    else:
        result = "*" * n
        for _ in range(n - 2):
            result += "*" + " " * (n - 2) + "*"
        result += "*" * n
        return result


def isosceles_triangle(n: int) -> str:
    """
    Returns an isosceles triangle of stars with a height of `n`.

    Args:
      n (int): The height of the triangle.

    Returns:
      str: A string of stars.
    """
    result = ""
    for i in range(1, n + 1):
        result += " " * (n - i) + "*" * (i * 2 - 1)
    return result


if __name__ == "__main__":
    doctest.testmod()
    print(left_down_triangle(5))
