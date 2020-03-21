from fractions import gcd
from functools import reduce

n, x = map(int, input().split())
xx = list(map(int, input().split()))

ls = []
xx.sort()


for s in xx:
    diff = abs(x-s)
    ls.append(diff)

ans = reduce(gcd, ls)
print(ans)
