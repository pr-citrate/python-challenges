"""
n값을 입력받고, 1부터 k까지의 수를 원소로 가진 list를 k를 1부터 n까지 증가시키며, 총 n개의 list를 가진 list를 출력한다.
"""

n = int(input("n: "))

print([[j for j in range(1, i + 1)] for i in range(1, n + 1)])
