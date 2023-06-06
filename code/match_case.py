# pylint: disable=invalid-name

"""
Practice of match-case syntax.
"""


import doctest


def fizzbuzz_1(n: int) -> str:
    """Returns the FizzBuzz output for the given number.

    The FizzBuzz output is generated as follows:

    * If the number is divisible by both 3 and 5, return "fizzbuzz".
    * If the number is divisible by 3, return "fizz".
    * If the number is divisible by 5, return "buzz".
    * Otherwise, return the number itself.

    Args:
        n (int): The number to generate FizzBuzz output for.

    Returns:
        str:The FizzBuzz output for the given number.
        
    Examples:
    >>> fizzbuzz_1(1) == \
        '1'
    True
    
    >>> fizzbuzz_1(3) == \
        'fizz'
    True
    
    >>> fizzbuzz_1(10) == \
        'buzz'
    True
    
    >>> fizzbuzz_1(15) == \
        'fizzbuzz'
    True
    """
    match n % 3, n % 5:
        case 0, 0:
            return "fizzbuzz"
        case 0, _:
            return "fizz"
        case _, 0:
            return "buzz"
        case _, _:
            return str(1)


if __name__ == "__main__":
    doctest.testmod()
