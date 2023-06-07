# pylint: disable=invalid-name

"""
Practice of python operators.
"""
import doctest


def ternary_1(n: int) -> str:
    """Return a string of the numbers from 1 to n, with even numbers replaced by 0.

    Args:
        n (int): The upper limit of the range.

    Returns:
        str: A string of the numbers from 1 to n, with even numbers replaced by 0.
    """
    result = ""
    for i in range(1, n + 1):
        result += str(i if i % 2 == 0 else 0)
        result += "\n"

    return result


if __name__ == "__main__":
    doctest.testmod()
