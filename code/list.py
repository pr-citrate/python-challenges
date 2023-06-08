from typing import Any


def add_1(arr: list, a: Any):
    """_summary_

    Args:
        arr (list): _description_
        a (Any): _description_

    Returns:
        _type_: _description_
    """
    return arr.append(a)


def add_2(arr: list, a: Any, n: int):
    """_summary_

    Args:
        arr (list): _description_
        a (Any): _description_
        n (int): _description_

    Returns:
        _type_: _description_
    """
    return arr.insert(n - 1, a)


def slice_1(arr, n):
    """_summary_

    Args:
        arr (_type_): _description_
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    return arr[n - 1]


def slice_2(arr, n):
    """_summary_

    Args:
        arr (_type_): _description_
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    return arr[-n]
