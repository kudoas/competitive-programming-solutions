from collections import Counter
from itertools import product

n, c = map(int, input().split())
A = [int(input()) for _ in range(n)]
odd = Counter(A[::2]).most_common()[:2]
even = Counter(A[1::2]).most_common()[:2]

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

ans = c*(n-total)
print(ans)
