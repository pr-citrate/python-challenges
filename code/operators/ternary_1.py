"""
삼항 연산자를 이용해 1부터 n까지의 값중 2의 배수는 출력하고, 그렇지 않으면 0을 출력한다.
"""

n = int(input("n: "))
for i in range(1, n + 1):
    print(i if i % 2 == 0 else 0)
