from collections import Counter
from itertools import product

n = int(input())
V = list(map(int, input().split()))
odd = Counter(V[1::2]).most_common()[:2]
even = Counter(V[::2]).most_common()[:2]

if len(odd) == 1:
    odd.append((0, 0))
if len(even) == 1:
    even.append((0, 0))
INF = 10**18
total = -INF
for p in product((1, 0), repeat=2):
    if odd[p[0]][0] == even[p[1]][0]:
        continue
    total = max(total, odd[p[0]][1]+even[p[1]][1])
ans = n - total
print(ans)
