"""
n값을 입력받아, 한 변의 길이를 n으로 하는 오른쪽 위를 향하는 직각삼각형을 "*"를 이용하여 출력한다.
"""

n = int(input("n: "))

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)
