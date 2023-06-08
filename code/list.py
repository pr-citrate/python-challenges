# pylint: disable=invalid-name


from typing import Any, List, Tuple


def add_1(arr: List[Any], a: Any) -> List[Any]:
    arr.append(a)
    return arr


def add_2(arr: List[Any], a: Any, n: int) -> List[Any]:
    arr.insert(n - 1, a)
    return arr


def slice_1(arr: List[Any], n: int) -> Any:
    return arr[n - 1]


def slice_2(arr: List[Any], n: int) -> Any:
    return arr[-n]


def slice_3(arr: List[Any], n: int, m: int) -> List[Any]:
    return arr[n - 1 : m]


def slice_4(arr: List[Any]) -> List[Any]:
    return arr[::2]


def slice_5(arr: List[Any]):
    return arr[::2]


def update_1(arr: List[Any], a: Any, n: int):
    arr[n - 1] = a
    return arr


def update_2(arr: List[Any], a: Any, n: int, m: int) -> List[Any]:
    arr[n - 1 : m] = a
    return arr


def delete_1(arr: List[Any], a: Any) -> List[Any]:
    arr.remove(a)
    return arr


def delete_2(arr: List[Any], n: int) -> Tuple[List[Any], int]:
    t = arr.pop(n)
    return arr, t


def delete_3(arr: List[Any], n: int) -> List[Any]:
    arr.pop(n)
    return arr
