# pylint: disable=invalid-name

import doctest
from typing import Any, List, Tuple


def add_1(arr: List[Any], a: Any) -> List[Any]:
    """append 메서드를 이용해 리스트에 a를 가장 마지막에 추가하는 함수를 작성한다.

    Args:
        arr (List[Any]): 원소를 추가할 리스트
        a (Any): 추가할 원소

    Returns:
        List[Any]: 추가된 리스트

    Examples:
    >>> add_1([1, 2, 3, 4], 5)
    [1, 2, 3, 4, 5]

    >>> add_1(['python', 'javascript', 'c', 'ruby', 'erlang'], 'go')
    ['python', 'javascript', 'c', 'ruby', 'erlang', 'go']

    >>> add_1(['a', 3.7, -52, [1, 2, 3], 'aws'], 5)
    ['a', 3.7, -52, [1, 2, 3], 'aws', 5]

    >>> add_1([], 'py')
    ['py']
    """
    arr.append(a)
    return arr


def add_2(arr: List[Any], a: Any, n: int) -> List[Any]:
    """insert 메서드를 활용하여 리스트의 n번쨰에 a를 추가하는 함수를 작성한다,

    Args:
        arr (List[Any]): 원소를 추가할 리스트
        a (Any): 추가할 원소
        n (int): 원소를 추가할 위치, 자연수

    Returns:
        List[Any]: 원소가 추가된 리스트

    Examples:
    >>> add_2([1, 2, 3, 5], 4, 4)
    [1, 2, 3, 4, 5]

    >>> add_2(['a', 'b', 'c'], 'd', 4)
    ['a', 'b', 'c', 'd']

    >>> add_2([], {'a':'1'}, 1)
    [{'a': '1'}]
    """
    assert len(arr) >= n - 1
    arr.insert(n - 1, a)
    return arr


def slice_1(arr: List[Any], n: int) -> Any:
    """리스트의 n번쨰 항목을 슬라이싱을 이용하여 반환하는 함수를 작성한다.

    Args:
        arr (List[Any]): 리스트
        n (int): 자연수

    Returns:
        Any: 리스트의 n번째 항목

    Examples:
    >>> slice_1([1, 2, 3, 4], 2)
    2

    >>> slice_1(['go', 'js', 'python', 'c'], 4)
    'c'

    >>> slice_1(['a', 3.7, -52, [1, 2, 3], 'aws'], 1)
    'a'

    >>> slice_1([[]], 1)
    []
    """
    return arr[n - 1]


def slice_2(arr: List[Any], n: int) -> Any:
    """리스트에서 끝어서 n번쨰 원소를 슬라이싱을 이용해 반환하는 함수를 작성한다.

    Args:
        arr (List[Any]): 리스트
        n (int): 자연수

    Returns:
        Any: 라스트에서 뒤에서부터 n번쨰 원소

    Examples:
    >>> slice_2([1, 2, 3, 4], 1)
    4

    >>> slice_2(['go', 'js', 'python', 'c'], 3)
    'js'

    >>> slice_2(['a', 3.7, -52, [1, 2, 3], 'aws'], 5)
    'a'

    >>> slice_2([[]], 1)
    []
    """
    return arr[-n]


def slice_3(arr: List[Any], n: int, m: int) -> List[Any]:
    """리스트에서 n번쨰부터 m번째 원소들을 리스트로 반환하는 함수를 작성한다

    Args:
        arr (List[Any]): 리스트
        n (int): m보다 작은 자연수
        m (int): n보다 큰 자연수

    Returns:
        List[Any]: 원래 리스트의 n~m번째 값들

    Examples:
    >>> slice_3([1, 2, 3, 4], 2, 4)
    [2, 3, 4]

    >>> slice_3(['go', 'js', 'python', 'c'], 1, 2)
    ['go', 'js']

    >>> slice_3(['a', 3.7, -52, [1, 2, 3], 'aws'], 2, 4)
    [3.7, -52, [1, 2, 3]]

    >>> slice_3([[]], 1, 1)
    [[]]
    """
    return arr[n - 1 : m]


def slice_4(arr: List[Any]) -> List[Any]:
    """리스트에서 홀수번째 항목을 반환하는 함수를 슬라이싱을 이용해 작성한다.

    Args:
        arr (List[Any]): 리스트

    Returns:
        List[Any]: 리스트의 홀수번째 항목을 원소로 가지는 리스트

    Examples:
    >>> slice_4([1, 2, 3, 4])
    [1, 3]

    >>> slice_4(['go', 'js', 'python', 'c'])
    ['go', 'python']

    >>> slice_4(['a', 3.7, -52, [1, 2, 3], 'aws'])
    ['a', -52, 'aws']

    >>> slice_4([])
    []
    """
    return arr[::2]


def update_1(arr: List[Any], a: Any, n: int) -> List[Any]:
    """리스트의 n번쨰 항목을 a로 바꾼 리스트를 반환하는 함수를 작성한다

    Args:
        arr (List[Any]): 리스트
        a (Any): 새로 변경할 항목
        n (int): 변경할 위치

    Returns:
        List[Any]: 변경된 리스트

    Examples:
    >>> update_1([1, 2, 7, 4], 3, 3)
    [1, 2, 3, 4]

    >>> update_1(['go', 'js', 'python', 'c'], 'ts', 2)
    ['go', 'ts', 'python', 'c']

    >>> update_1(['a', 3.7, -52, [1, 2, 3], 'aws'], '123', 4)
    ['a', 3.7, -52, '123', 'aws']

    >>> update_1([[]], {}, 1)
    [{}]

    """
    arr[n - 1] = a
    return arr


def update_2(arr: List[Any], a: List[Any] | Tuple[Any], n: int, m: int) -> List[Any]:
    """리스트의 n번쨰부터 m번째의 항목을 a의 내용으로 변경하는 함수를 작성한다

    Args:
        arr (List[Any]): 리스트
        a (List[Any] | Tuple[Any]): 변경할 내용
        n (int): 변경 시작 위치
        m (int): 변경 종료 위치

    Returns:
        List[Any]: 변경된 리스트

    Examples:
    >>> update_2([1, 3, 2, 4],[2, 3], 2, 3)
    [1, 2, 3, 4]

    >>> update_2(['go', 'js', 'python', 'c'], ('ruby', 'elixir'), 1, 2)
    ['ruby', 'elixir', 'python', 'c']

    >>> update_2(['a', 3.7, -52, [1, 2, 3], 'aws'], ['b', 'c', 'd', 'e'], 2, 5)
    ['a', 'b', 'c', 'd', 'e']

    >>> update_2([[]], {}, 1, 1)
    []
    """
    arr[n - 1 : m] = a
    return arr


def delete_1(arr: List[Any], a: Any) -> List[Any]:
    """remove 메서드를 이용해 a를 리스트에서 제거해 반환하는 함수를 작성한다

    Args:
        arr (List[Any]): 리스트
        a (Any): 제거할 항목

    Returns:
        List[Any]: 제거된 리스트

    Examples:
    >>> delete_1([1, 2, 3, 4, 5], 3)
    [1, 2, 4, 5]

    >>> delete_1(['a', 'b', 'c'], 'c')
    ['a', 'b']

    >>> delete_1(['python', 'js', 'swift', 'dart'], 'swift')
    ['python', 'js', 'dart']

    >>> delete_1([[1], [2], [1]], [1])
    [[2], [1]]
    """
    arr.remove(a)
    return arr


def delete_2(arr: List[Any], n: int) -> List[Any]:
    """리스트에서 n번쨰 항목을 del 키워드를 이용해 삭제한다.

    Args:
        arr (List[Any]): 리스트
        n (int): 삭제할 순서

    Returns:
        List[Any]: 삭제된 리스트

    Examples:
    >>> delete_2([1, 2, 3, 4, 5], 3)
    [1, 2, 4, 5]

    >>> delete_2(['a', 'b', 'c'], 3)
    ['a', 'b']

    >>> delete_2(['python', 'js', 'swift', 'dart'], 3)
    ['python', 'js', 'dart']

    >>> delete_2([[1], [2], [1]], 1)
    [[2], [1]]
    """
    del arr[n - 1]
    return arr


def delete_3(arr: List[Any], n: int) -> Tuple[List[Any], int]:
    """리스트에서 n번쨰 항목을 pop를 이용해 삭제하고, 그 리스트와 삭제된 항목을 반환한다

    Args:
        arr (List[Any]): 리스트
        n (int): 삭제할 순서

    Returns:
        Tuple[List[Any], int]: 삭제된 리스트, 삭제된 항목

    Examples:
    >>> delete_3([1, 2, 3, 4, 5], 3)
    ([1, 2, 4, 5], 3)

    >>> delete_3(['a', 'b', 'c'], 3)
    (['a', 'b'], 'c')

    >>> delete_3(['python', 'js', 'swift', 'dart'], 3)
    (['python', 'js', 'dart'], 'swift')

    >>> delete_3([[1], [2], [1]], 1)
    ([[2], [1]], [1])
    """
    t = arr.pop(n - 1)
    return arr, t


if __name__ == "__main__":
    doctest.testmod()
