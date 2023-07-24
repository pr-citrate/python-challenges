# pylint: disable=invalid-name

"""
Practice of for loop syntax.
"""
import doctest


def left_down_triangle(n: int):
    """
    for문을 이용하여 '*'로 이뤄진 한 변의 길이가 n인 왼쪽 아래 삼각형을 출력한다.

    Args:
      n (int): 한 변의 길이

    Examples:
    >>> left_down_triangle(1)
    *

    >>> left_down_triangle(3)
    *
    **
    ***

    >>> left_down_triangle(4)
    *
    **
    ***
    ****

    """
    for i in range(1, n + 1):
        print("*" * i)


def right_down_triangle(n: int):
    """
    for문을 이용하여 '*'로 이뤄진 한 변의 길이가 n인 왼쪽 아래 삼각형을 출력한다.

    Args:
      n (int): 한 변의 길이

    Examples:
    >>> right_down_triangle(1)
    *

    >>> right_down_triangle(3)
      *
     **
    ***

    >>> right_down_triangle(4)
       *
      **
     ***
    ****

    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


def left_up_triangle(n: int):
    """
    for문을 이용하여 '*'로 이뤄진 한 변의 길이가 n인 오른쪽 위 삼각형을 출력한다.

    Args:
      n (int): 한 변의 길이

    Examples:
    >>> left_up_triangle(1)
    *

    >>> left_up_triangle(3)
    ***
    **
    *

    >>> left_up_triangle(4)
    ****
    ***
    **
    *

    """
    for i in range(n, 0, -1):
        print("*" * i)


def right_up_triangle(n: int):
    """
    for문을 이용하여 '*'로 이뤄진 한 변의 길이가 n인 오른쪽 위 삼각형을 출력한다.

    Args:
      n (int): 한 변의 길이

    Examples:
    >>> right_down_triangle(1)
    *

    >>> right_down_triangle(3)
      *
     **
    ***

    >>> right_down_triangle(4)
       *
      **
     ***
    ****

    """
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)


def square(n: int):
    """
    for문을 이용하여 '*'로 이뤄진 한 변의 길이가 정사각형을 출력한다.

    Args:
      n (int): 한 변의 길이

    Examples:
    >>> square(1)
    *

    >>> square(3)
    ***
    ***
    ***

    >>> square(4)
    ****
    ****
    ****
    ****

    """
    for _ in range(n):
        print("*" * n)


def square_border(n: int):
    """
    for문을 이용하여 '*'로 이뤄진 한 변의 길이가 n인 정사각형의 테두리를 출력한다.

    Args:
      n (int): 한 변의 길이

    Examples:
    >>> square_border(1)
    *

    >>> square_border(2)
    **
    **

    >>> square_border(3)
    ***
    * *
    ***

    >>> square_border(4)
    ****
    *  *
    *  *
    ****

    """
    if n == 1:
        print("*")
    else:
        print("*" * n)
        for _ in range(n - 2):
            print("*" + " " * (n - 2) + "*")
        print("*" * n)


def isosceles_triangle(n: int):
    """
    for문을 이용하여 '*'로 이뤄진 높이가n이고, 밑변이 2n-1인 이등변삼각형을 출력한다.

    Args:
      n (int): 높이

    Examples:
    >>> isosceles_triangle(1)
    *

    >>> isosceles_triangle(2)
     *
    ***

    >>> isosceles_triangle(4)
       *
      ***
     *****
    *******

    >>> isosceles_triangle(5)
        *
       ***
      *****
     *******
    *********


    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (i * 2 - 1))


if __name__ == "__main__":
    doctest.testmod()
