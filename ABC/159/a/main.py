import math

n, m = map(int, input().split())


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


if m >= 2:
    odd = combinations_count(m, 2)
elif m == 0 or m == 1:
    odd = 0

if n >= 2:
    even = combinations_count(n, 2)
elif n == 1:
    even = 1
elif n == 0:
    even = 0

answer = odd + even
if m == 1 and n == 1:
    answer = 0

print(answer)
