from math import gcd

n = int(input())


def lcm(a, b):
    return a * b // gcd(a, b)


ans = 1
for _ in range(n):
    t = int(input())
    ans = lcm(ans, t)

print(ans)
