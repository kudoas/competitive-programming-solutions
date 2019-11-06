import itertools
import numpy

n = int(input())
D = list(map(int, input().split()))
ans = 0

ls = itertools.combinations(D, 2)
for i in ls:
    ans += numpy.prod(i)

print(ans)
