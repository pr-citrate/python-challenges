# pylint: disable=invalid-name

"""
Practice of python operators.
"""
import doctest
from typing import List, Tuple, Any


def arithmetic(a: float, b: float):
    """사칙연산을 하여 반환하는 함수를 작성한다.

    Args:
        a (float): 첫쨰 피연산자, 실수
        b (float): 둘째 피연산자, 0이 아닌 실수

    Examples:
    >>> arithmetic(2, 5)
    7 -3 10 0.4

    >>> arithmetic(10, 3)
    13 7 30 3.3333333333333335

    >>> arithmetic(6, 2)
    8 4 12 3.0

    """
    assert b != 0
    print(a + b, a - b, a * b, a / b)


def divmod_1(n: int, m: int) -> Tuple[int, int]:
    """n을 m으로 나눈 몫과 나머지를 반환하는 함수를 몫 연산자와 나머지 연산자를 이용하여 작성한다.

    Args:
        n (int): 자연수
        m (int): 자연수

    Returns:
        Tuple[int, int]: n을 m으로 나눈 몫, n을 m으로 나눈 나머지

    Examples:
    >>> divmod_1(7, 3)
    (2, 1)

    >>> divmod_1(2, 5)
    (0, 2)

    >>> divmod_1(10, 2)
    (5, 0)
    """

    return n // m, n % m


def power_1(n: int) -> int:
    """n의 제곱을 반횐하는 함수를 거듭제곱 연산자를 이용하여 작성한다

    Args:
        n (int): 양의 실수

    Returns:
        int: n의 제곱

    Examples:
    >>> power_1(0)
    0

    >>> power_1(1)
    1

    >>> power_1(3)
    9

    >>> power_1(111)
    12321

    """
    return n**2


def power_2(n: int) -> float:
    """제곱근 n을 반환하는 함수를 거듭제곱 연산자를 이용하여 작성한다.

    Args:
        n (int): 자연수

    Returns:
        float: 제곱근 n

    Examples:
    >>> power_2(0)
    0.0

    >>> power_2(1)
    1.0

    >>> power_2(4)
    2.0

    >>> power_2(10)
    3.1622776601683795
    """
    return n**0.5


def power_3(n: float) -> float:
    """n의 역수를 반환하는 함수를 거듭제곱 연산자를 이용하여 작성한다.

    Args:
        n (float): 양의 실수

    Returns:
        float: n의 역수

    Examples:
    >>> power_3(1)
    1.0

    >>> power_3(10)
    0.1

    >>> power_3(0.2)
    5.0

    >>> power_3(7)
    0.14285714285714285

    >>> power_3(0.723)
    1.3831258644536653

    """
    return n**-1


def power_4(n: float, m: float) -> float:
    """n의 m제곱을 반환하는 함수를 거듭제곱 연산자를 이용하여 작성한다. 단, n이 0이하라면 m은 양수여야 한다.

    Args:
        n (float): 실수
        m (float): 실수

    Returns:
        float: n의 m제곱

    Examples:
    >>> power_4(3, 2)
    9

    >>> power_4(5, 1)
    5

    >>> power_4(3, -0.5)
    0.5773502691896257

    >>> power_4(7, 0.3)
    1.792789962520997

    >>> power_4(2, -3)
    0.125
    """
    assert m > 0 if n <= 0 else True
    return n**m


def ternary_1(n: int) -> str:
    """n이 홀수이면 buzz, 짝수이면 fizz를 반환하는 함수를 삼항 연산자를 이용하여 작성한다.

    Args:
        n (int): 자연수

    Returns:
        str: "fizz" 또는 "buzz"

    Examples:
    >>> ternary_1(1)
    'buzz'

    >>> ternary_1(4)
    'fizz'

    >>> ternary_1(5)
    'buzz'
    """
    return "fizz" if n % 2 == 0 else "buzz"


def ternary_2(n: int) -> List[Any]:
    """홀수가 0으로 대체된 1부터 n까지의 숫자로 된 리스트를 반환하는 함수를 작성한다

    Args:
        n (int): 자연수

    Returns:
        str: 홀수가 으로 대체된 1부터 n까지의 리스트

    Examples:
    >>> ternary_2(1)
    [0]

    >>> ternary_2(2)
    [0, 2]

    >>> ternary_2(5)
    [0, 2, 0, 4, 0]
    """
    result = []
    for i in range(1, n + 1):
        result += [i if i % 2 == 0 else 0]

    return result


if __name__ == "__main__":
    doctest.testmod()
