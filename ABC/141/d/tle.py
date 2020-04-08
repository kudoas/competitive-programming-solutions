import bisect
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for _ in range(m):
    max_price = A.pop(-1) // 2
    bisect.insort(A, max_price)

total = sum(A)
print(total)
