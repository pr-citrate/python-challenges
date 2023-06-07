# pylint: disable=invalid-name

"""
Practice of python operators.
"""
import doctest


def ternary_1(n: int) -> str:
    """"Returns a string based on whether the input number is even or odd.

    Args:
        n (int): The number to check.

    Returns:
        str: "fizz" if n is even, "buzz" if n is odd.
        
    Examples:
    >>> ternary_1(1) == \
        "buzz"
    True
    
    >>> ternary_1(4) == \
        "fizz"
    True
    
    >>> ternary_1(5) == \
        "buzz"
    True
    """
    return "fizz" if n % 2 == 0 else "buzz"


def ternary_2(n: int) -> str:
    """Return a string of the numbers from 1 to n, with even numbers replaced by 0.

    Args:
        n (int): The upper limit of the range.

    Returns:
        str: A string of the numbers from 1 to n, with even numbers replaced by 0.
        
    Examples:
    >>> ternary_2(1) == \
        "0"
    True
    
    >>> ternary_2(2) == \
        "0\\n2"
    True
    
    >>> ternary_2(5) == \
        "0\\n2\\n0\\n4\\n0"
    True
    """
    result = []
    for i in range(1, n + 1):
        result.append(str(i if i % 2 == 0 else 0))

    return "\n".join(result)


if __name__ == "__main__":
    doctest.testmod()
