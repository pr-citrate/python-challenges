"""
n값을 입력받고, 0을 원소로 n개 가진 list를 원소로 n개 가지는 list(n*n)를 출력한다.
"""

n = int(input("n: "))

print([[0 for j in range(n)] for i in range(n)])
