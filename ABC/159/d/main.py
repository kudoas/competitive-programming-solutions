import collections
import math


n = int(input())
aa = list(map(int, input().split()))
ls = [0] * (n+1)

c = collections.Counter(aa)

for i, j in c.items():
    ls[i] = j*(j-1)//2

total = sum(ls)

for i in aa:
    before = (c[i]-1)*(c[i]-2) // 2
    print(total - ls[i] + before)
