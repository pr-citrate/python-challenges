"""
n값을 입력받고, "fizz"와 "buzz"를 원소로 번갈아가며 총 n개의 원소를 가진 list를 출력한다.
"""

n = int(input("n: "))

print(["fizz" if i % 2 == 0 else "buzz" for i in range(n)])
