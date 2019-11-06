import math

a, b = map(int, input().split())

ls = []
ans = []

for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        ls.append(i)
