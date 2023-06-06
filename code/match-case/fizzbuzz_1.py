"""
자연수 n 값을 입력받고, 만일 3의 배수이면 fizz를, 5의 배수이면 buzz를 출력한다. 두 조건을 모두 만족하면 fizzbuzz를 출력하고, 둘다 만족하지 않으면 출력하지 않는다.
"""


n = int(input("n: "))

match n % 3, n % 5:
    case 0, 0:
        print("fizzbuzz")
    case 0, _:
        print("fizz")
    case _, 0:
        print("buzz")
