"""
n값을 입력받아, 한 변의 길이를 n으로 하는 정사각형의 테두리를 "*"를 이용하여 출력한다.
"""

n = int(input("n: "))

if n == 1:
    print("*")
else:
    print("*" * n)
    for i in range(n - 2):
        print("*" + " " * (n - 2) + "*")
    print("*" * n)
